#!/usr/bin/env python3
"""TOBS Phase 23C.10: nine complete, original minor-nation archive recordings.

Fail closed if an official LOC file no longer matches its MD5. No files or
playlists are modified until all 9 archive files validate. Idempotent repeat.
"""
from pathlib import Path
import hashlib,json,urllib.request
root=Path(__file__).resolve().parent.parent
catalog=json.loads((root/"music/minor-batch4-sources.json").read_text("utf-8"))
assert catalog["version"]==1 and len(catalog["tracks"])==9
files=[]
for x in catalog["tracks"]:
    ident=x["id"]
    assert x["url"]==f"https://data.labs.loc.gov/jukebox/audio/jukebox-{ident}_1.mp3"
    assert x["filename"]==f"tobs-minors-batch4-{ident}.mp3"
    request=urllib.request.Request(x["url"],headers={"User-Agent":"HOI4-War-Room-TOBS/1.0 (full historical recordings archive importer)"})
    with urllib.request.urlopen(request,timeout=120) as resp:
        raw=resp.read(15_000_001)
    if not 100_000<len(raw)<15_000_000:raise ValueError("Invalid recording length: "+ident)
    digest=hashlib.md5(raw).hexdigest()
    if digest!=x["md5"]:raise ValueError(f"LOC official MD5 mismatch for {ident}: {digest}")
    if not(raw.startswith(b"ID3") or raw[0]==255):raise ValueError("Expected MP3 encoding: "+ident)
    files.append((x,raw))
    print("VERIFIED",x["country"],x["title"],len(raw),"bytes",flush=True)
assert len({x["id"] for x,raw in files})==9
path=root/"audio-manifest.json"
manifest=json.loads(path.read_text("utf-8"))
assert manifest["version"]==1
dest=root/"audio";dest.mkdir(exist_ok=True)
for x,raw in files:
    filepath=dest/x["filename"]
    if filepath.exists() and filepath.read_bytes()!=raw:raise ValueError("Existing file mismatches archive: "+x["filename"])
for x,raw in files:
    station=manifest.setdefault("stations",{}).setdefault(x["country"],[])
    src="audio/"+x["filename"]
    if not any(s.get("src")==src for s in station):
        station.append({"title":x["title"]+" — original "+x["date"][:4]+" recording","src":src})
for x,raw in files:(dest/x["filename"]).write_bytes(raw)
manifest["notes"]="TOBS historical music archive: nine original real musical recordings, 1906–1916, added to Sweden, Norway, Finland, Denmark, Mexico, and Poland. No synthetic or restricted commercial WWII originals published. Genuine WWII period performance research continues separately."
path.write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+"\n","utf-8")
print("SUCCESS: 9 full recordings imported and playlists updated",flush=True)
