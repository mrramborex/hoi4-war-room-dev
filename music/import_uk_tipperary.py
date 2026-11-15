#!/usr/bin/env python3
"""Phase 23C.8: verify two genuine 1914 Tipperary performances from LOC."""
import hashlib,json,urllib.request
from pathlib import Path
root=Path(__file__).resolve().parent.parent
d=json.loads((root/"music/uk-tipperary-sources.json").read_text("utf-8"))
assert d["version"]==1 and len(d["tracks"])==2
files=[]
for x in d["tracks"]:
    assert x["url"]==f"https://data.labs.loc.gov/jukebox/audio/jukebox-{x['id']}_1.mp3"
    assert x["filename"]==f"tobs-uk-tipperary-{x['id']}.mp3"
    req=urllib.request.Request(x["url"],headers={"User-Agent":"HOI4-War-Room/TOBS historical full-music importer"})
    with urllib.request.urlopen(req,timeout=120) as response: raw=response.read(15_000_001)
    if not 100000<len(raw)<15000000: raise ValueError("Unexpected recording length: "+x["id"])
    if hashlib.md5(raw).hexdigest()!=x["md5"]:raise ValueError("LOC MD5 mismatch: "+x["id"])
    if not (raw.startswith(b"ID3") or raw[0]==255):raise ValueError("Unexpected MP3 signature: "+x["id"])
    files.append((x,raw))
    print("VERIFIED",x["id"],x["title"],len(raw),"bytes",flush=True)
manifest_file=root/"audio-manifest.json"
manifest=json.loads(manifest_file.read_text("utf-8"))
assert manifest["version"]==1
station=manifest["stations"].setdefault("United Kingdom",[])
for x,raw in files:
    src="audio/"+x["filename"]
    if not any(y.get("src")==src for y in station):
        station.append({"title":x["title"]+" — complete historical recording","src":src})
dest=root/"audio"
dest.mkdir(exist_ok=True)
for x,raw in files:
    f=dest/x["filename"]
    if f.exists() and f.read_bytes()!=raw:raise ValueError("Unexpected existing audio file: "+x["filename"])
for x,raw in files:
    (dest/x["filename"]).write_bytes(raw)
manifest["notes"]="TOBS archival library: two complete, source-verified UK Tipperary recordings from 1914 added; authentic WWI-era recordings, not WWII; modern and copyrighted user-supplied 1940s MP3s remain browser-local, no synthesized songs."
manifest_file.write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+"\n","utf-8")
print("SUCCESS: added two archive-verified complete Tipperary recordings",flush=True)
