#!/usr/bin/env python3
"""TOBS Phase 23C.9: validated historic complete international performances.

All archive files must match the official Library of Congress MD5 before any
playlist edits. Fail closed rather than substituting a different master.
"""
from pathlib import Path
import hashlib,json,urllib.request
root=Path(__file__).resolve().parent.parent
dataset=json.loads((root/"music/international-batch3-sources.json").read_text("utf-8"))
assert dataset["version"]==1 and len(dataset["tracks"])==3
files=[]
for item in dataset["tracks"]:
    ident=item["id"]
    assert item["audio_url"]==f"https://data.labs.loc.gov/jukebox/audio/jukebox-{ident}_1.mp3"
    req=urllib.request.Request(item["audio_url"],headers={"User-Agent":"HOI4-War-Room-TOBS/1.0 (public domain historical audio importer)"})
    with urllib.request.urlopen(req,timeout=120) as response:
        raw=response.read(15_000_001)
    if not (100_000<len(raw)<15_000_000):raise ValueError("Invalid size: "+ident)
    if hashlib.md5(raw).hexdigest()!=item["md5"]:raise ValueError("LOC MD5 mismatch: "+ident)
    if not (raw.startswith(b"ID3") or raw[0]==255):raise ValueError("Expected MP3: "+ident)
    files.append((item,raw))
    print("VERIFIED",item["country"],item["title"],len(raw),"bytes",flush=True)
assert len(set(item["country"] for item,raw in files))==3
manifest_path=root/"audio-manifest.json"
manifest=json.loads(manifest_path.read_text("utf-8"))
assert manifest["version"]==1
for item,raw in files:
    tracks=manifest.setdefault("stations",{}).setdefault(item["country"],[])
    src="audio/"+item["filename"]
    if not any(t.get("src")==src for t in tracks):
        tracks.append({"title":item["title"]+" — original historical recording","src":src})
manifest["notes"]="TOBS historical music archive: three additional full verified pre-1923 LOC recordings (France, Germany, and first Austrian broadcast) in Phase 23C.9. Historic repertoire, not actual WWII performances. No copyrighted user audio or rejected synthesized music."
dest=root/"audio"
dest.mkdir(exist_ok=True)
for item,raw in files:
    f=dest/item["filename"]
    if f.exists() and f.read_bytes()!=raw:raise ValueError("Unexpected original file differs: "+item["filename"])
for item,raw in files:(dest/item["filename"]).write_bytes(raw)
manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n","utf-8")
print("SUCCESS: three archive-verified historical recordings added",flush=True)
