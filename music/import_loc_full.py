#!/usr/bin/env python3
"""Import full-length Library of Congress National Jukebox MP3s into TOBS.
Requires stdlib only; intended for dev GitHub Actions. No third-party masters.
Five exact MP3 URLs and file checksums come from the official LOC data manifest.
All files are verified before the audio playlist is modified.
"""
import hashlib
import json
from pathlib import Path
import urllib.request

root = Path(__file__).resolve().parent.parent
items = json.loads((root / "music/loc-full-recordings.json").read_text(encoding="utf-8"))["songs"]
out_dir = root / "audio"
manifest_file = root / "audio-manifest.json"
files = []
for item in items:
    expected = f'https://data.labs.loc.gov/jukebox/audio/jukebox-{item["id"]}_1.mp3'
    assert item["url"] == expected
    assert len(item["md5"]) == 32 and all(c in "0123456789abcdef" for c in item["md5"])
    name = item["filename"]
    assert name.startswith("tobs-full-") and name.endswith(".mp3") and Path(name).name == name
    req = urllib.request.Request(expected, headers={"User-Agent": "TOBS-War-Room/1.0"})
    with urllib.request.urlopen(req, timeout=90) as res:
        data = res.read(15_000_001)
    if not (100_000 < len(data) <= 15_000_000):
        raise ValueError(f"Unexpected source size: {name} / {len(data)}")
    actual = hashlib.md5(data).hexdigest()
    if actual != item["md5"]:
        raise ValueError(f"Official LOC checksum mismatch for {name}: {actual}")
    if not (data.startswith(b"ID3") or data[:1] == b"\\xff"):
        raise ValueError(f"Not MP3 audio: {name}")
    print(f"PASS {item['title']}: {len(data)} bytes, MD5={actual}")
    files.append((name,data,item))
assert len(files)==5 and len({x[0] for x in files})==5
manifest = json.loads(manifest_file.read_text(encoding="utf-8"))
assert manifest["version"]==1
manifest.setdefault("stations",{})["United States"] = [
 {"title": item["title"] + " — LOC complete recording", "src":"audio/"+name}
 for name,data,item in files
]
manifest["notes"] = "Phase 23C: five full-length LOC National Jukebox historic public-domain performances; original short Citizen DJ excerpts retired. Stations without verified audio have no playlist yet."
out_dir.mkdir(parents=True,exist_ok=True)
for name,data,item in files:
    (out_dir/name).write_bytes(data)
manifest_file.write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
print("READY: five full-length recordings; legacy excerpt paths no longer in manifest")
