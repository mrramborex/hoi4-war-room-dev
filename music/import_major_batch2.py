#!/usr/bin/env python3
"""TOBS Phase 23C.4: checksum-verified complete historical recordings.

All ten files must match the official LOC data manifest hashes before changing
the playlist. The operation is idempotent and never adds duplicate tracks.
Only the HOI4 War Room development repository should run this script.
"""
from pathlib import Path
import hashlib,json,urllib.request
root=Path(__file__).resolve().parent.parent
entries=json.loads((root/"music/major-batch2-sources.json").read_text("utf-8"))
assert entries["version"]==1 and len(entries["songs"])==10
media=[]
for row in entries["songs"]:
    rid=row["id"]
    target=f"https://data.labs.loc.gov/jukebox/audio/jukebox-{rid}_1.mp3"
    assert row["url"]==target and row["filename"]==f"tobs-major-batch2-{rid}.mp3"
    assert len(row["md5"])==32 and all(c in "0123456789abcdef" for c in row["md5"])
    request=urllib.request.Request(target,headers={"User-Agent":"HOI4-War-Room-TOBS/1.0"})
    with urllib.request.urlopen(request,timeout=120) as response:
        raw=response.read(15_000_001)
    if not 100_000<len(raw)<=15_000_000:raise ValueError("Invalid size: "+rid)
    actual=hashlib.md5(raw).hexdigest()
    if actual!=row["md5"]:raise ValueError(f"LOC official MD5 mismatch {rid}: {actual}")
    if not(raw.startswith(b"ID3") or raw[0]==255):raise ValueError("Invalid MP3: "+rid)
    media.append((row,raw))
    print(f"VERIFIED {row['country']} | {row['title']} | {len(raw)} bytes | {actual}",flush=True)
assert len({row["id"] for row,raw in media})==10
manifest_path=root/"audio-manifest.json"
manifest=json.loads(manifest_path.read_text("utf-8"))
assert manifest["version"]==1
for row,raw in media:
    src="audio/"+row["filename"]
    entries=manifest.setdefault("stations",{}).setdefault(row["country"],[])
    if not any(item.get("src")==src for item in entries):
        entries.append({"title":row["title"]+" — LOC full recording","src":src})
manifest["notes"]="TOBS Phase 23C.4: 27 complete rights-documented historical recordings, across all 7 major powers. US & Japan unchanged by this batch. Other 58 stations await cleared music."
dest=root/"audio"
dest.mkdir(exist_ok=True)
for row,raw in media:
    path=dest/row["filename"]
    if path.exists() and path.read_bytes()!=raw:
        raise ValueError("Existing file changed: "+row["filename"])
for row,raw in media:
    (dest/row["filename"]).write_bytes(raw)
manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n","utf-8")
print("SUCCESS: all 10 full recordings imported into five station playlists",flush=True)
