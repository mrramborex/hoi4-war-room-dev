#!/usr/bin/env python3
"""Stage *specific* LOC Citizen DJ curated public-domain WAV excerpts for TOBS.
Run from the repository root: python3 music/import_loc_jazz.py
Requires internet, Python 3.9+, no external packages.
Import only from the source manifest below; never substitute other masters.
This script validates file signatures and leaves the existing audio manifest
untouched until the entire collection downloads and validates successfully.
"""
import json
import pathlib
import struct
import urllib.request
import hashlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
SOURCES = ROOT / "music" / "loc-curated-excerpts.json"
OUTPUT = ROOT / "audio"
MANIFEST = ROOT / "audio-manifest.json"

def main():
    source = json.loads(SOURCES.read_text(encoding="utf-8"))
    assert source["version"] == 1
    files = []
    for item in source["items"]:
        url = item["url"]
        assert url.startswith("https://s3.amazonaws.com/citizen-dj-assets.labs.loc.gov/audio/samplepacks/loc-jukebox-jazz/")
        name = item["filename"]
        assert name.startswith("tobs-loc-") and name.endswith(".wav") and pathlib.Path(name).name == name
        out = OUTPUT / name
        if out.exists():
            data = out.read_bytes()
        else:
            req = urllib.request.Request(url, headers={"User-Agent":"TOBS-War-Room/1.0 (public-domain-archive-download)"})
            with urllib.request.urlopen(req, timeout=45) as response:
                data = response.read(18_000_001)
            if len(data) > 18_000_000:
                raise ValueError(f"Too large: {name}")
        if len(data) < 44 or data[:4] != b"RIFF" or data[8:12] != b"WAVE":
            raise ValueError(f"Not a RIFF WAVE file: {name}")
        if struct.unpack_from("<I", data, 4)[0] + 8 != len(data):
            raise ValueError(f"Invalid RIFF file size: {name}")
        files.append((item, out, data))
        print(f"VALIDATED {name} bytes={len(data)} sha256={hashlib.sha256(data).hexdigest()}")
    # Atomic final writes for each file; manifest updates last. Validate everything first.
    OUTPUT.mkdir(exist_ok=True)
    for item, out, data in files:
        if not out.exists():
            tmp=out.with_suffix(".wav.tmp")
            tmp.write_bytes(data)
            tmp.replace(out)
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    assert manifest["version"] == 1
    station = manifest.setdefault("stations", {}).setdefault("United States", [])
    existing = {t["src"] for t in station}
    for item, out, data in files:
        path="audio/"+item["filename"]
        if path not in existing:
            station.append({"title":item["title"], "src":path})
    tmp = MANIFEST.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    tmp.replace(MANIFEST)
    print(f"READY: {len(files)} curated LOC samples in audio-manifest.json")
    print("Next: commit generated files and verify browser playback on development site.")

if __name__ == "__main__":
    main()
