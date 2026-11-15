#!/usr/bin/env python3
"""Import ten specifically curated LOC full-length international historical songs.

This is NOT an open-ended language scrape. Only the ten IDs and checksums in
music/loc-international-batch-1.json are approved for this import. No automatic
rights classifications for other recordings.
"""
import hashlib,json,urllib.request
from pathlib import Path
root=Path(__file__).resolve().parent.parent
source=json.loads((root/"music/loc-international-batch-1.json").read_text(encoding="utf-8"))
assert source["version"]==1 and len(source["items"])==10
files=[]
for item in source["items"]:
 id=item["id"]
 url=f"https://data.labs.loc.gov/jukebox/audio/jukebox-{id}_1.mp3"
 assert item["url"]==url and item["filename"]==f"tobs-international-{id}.mp3"
 assert len(item["md5"])==32
 req=urllib.request.Request(url,headers={"User-Agent":"HOI4-War-Room-TOBS/1.0"})
 with urllib.request.urlopen(req,timeout=120) as resp:data=resp.read(12_000_001)
 if not (100_000<len(data)<=12_000_000):raise RuntimeError(f"Source file wrong size for {id}")
 if hashlib.md5(data).hexdigest()!=item["md5"]:raise RuntimeError(f"LOC manifest checksum mismatch {id}")
 if not (data.startswith(b"ID3") or data[0]==255):raise RuntimeError(f"Not MP3 {id}")
 files.append((item,data))
 print(f"VERIFIED {item['country']} | {item['title']} | {len(data)} bytes")
assert len({x["id"] for x,_ in files})==10
manifest_file=root/"audio-manifest.json"
manifest=json.loads(manifest_file.read_text(encoding="utf-8"))
assert manifest["version"]==1
for item,data in files:
 manifest.setdefault("stations",{}).setdefault(item["country"],[]).append({
  "title":item["title"]+" — LOC historical recording",
  "src":"audio/"+item["filename"]})
manifest["notes"]="TOBS live receiver: 5 complete United States recordings plus 10 rights-documented LOC historical international recordings. Unpopulated stations have no audio until appropriate files are cleared."
audio=root/"audio";audio.mkdir(exist_ok=True)
for item,data in files:(audio/item["filename"]).write_bytes(data)
manifest_file.write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
print("READY: imported 10 additional whole-song recordings, 5 new station playlists")
