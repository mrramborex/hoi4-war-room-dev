#!/usr/bin/env python3
"""Phase 23C.15: source and import 12 complete genuine recorded performances.

Atomic validation before any changed music: check archive inclusion, MD5, MP3
header and bounds for all 12. Each run only adds unique missing entries.
"""
import hashlib,base64,json,urllib.request
from pathlib import Path
root=Path(__file__).resolve().parent.parent
s=json.loads((root/"music/northern-europe-batch9-sources.json").read_text("utf-8"))
assert s["version"]==1 and len(s["tracks"])==12
def fetch(url,limit):
 req=urllib.request.Request(url,headers={"User-Agent":"HOI4WarRoomTOBS/1.0 archival uploader"})
 with urllib.request.urlopen(req,timeout=140) as r:b=r.read(limit+1)
 if len(b)>limit:raise ValueError("Archive item exceeds size bound")
 return b
d=json.loads(fetch(s["archive_manifest"],3000000))
assert "cols" in d and "rows" in d
records=[dict(zip(d["cols"],x)) for x in d["rows"]]
assert 5000<len(records)<6500
files=[]
for x in s["tracks"]:
 ident=x["id"]
 url=f"https://data.labs.loc.gov/jukebox/audio/jukebox-{ident}_1.mp3"
 assert x["audio"]==url and x["filename"]==f"tobs-c15-{ident}.mp3"
 matching=[r for r in records if any(f"jukebox-{ident}_1.mp3" in str(v) for v in r.values())]
 if len(matching)!=1:raise ValueError(f"Not available in official LOC full dataset: {ident}")
 expected=None
 for key,value in matching[0].items():
  if "md5" not in key.lower() or not value:continue
  v=str(value).strip()
  if len(v)==32:expected=v.lower()
  else:
   try:expected=base64.b64decode(v).hex()
   except Exception:pass
 if not expected or len(expected)!=32:raise ValueError("Invalid official MD5: "+ident)
 raw=fetch(url,15000000)
 if not 100000<len(raw)<15000000 or not(raw.startswith(b"ID3") or raw[:1]==b"\xff"):raise ValueError("Invalid MP3: "+ident)
 actual=hashlib.md5(raw).hexdigest()
 if actual!=expected:raise ValueError(f"LOC MD5 mismatch {ident} {expected} != {actual}")
 files.append((x,raw,actual))
 print("VERIFIED",x["country"],ident,x["title"],len(raw),"bytes",flush=True)
assert len({x["id"] for x,_,_ in files})==12
mf=root/"audio-manifest.json"
manifest=json.loads(mf.read_text("utf-8"))
assert manifest["version"]==1
dest=root/"audio";dest.mkdir(exist_ok=True)
for x,raw,md5 in files:
 file=dest/x["filename"]
 if file.exists() and file.read_bytes()!=raw:raise ValueError("Previously imported audio changed: "+x["filename"])
for x,raw,md5 in files:
 (dest/x["filename"]).write_bytes(raw)
 station=manifest["stations"].setdefault(x["country"],[])
 src="audio/"+x["filename"]
 if not any(y.get("src")==src for y in station):
  station.append({"title":x["title"]+" — historical "+x["recorded"][:4]+" performance","src":src})
manifest["notes"]="TOBS Phase 23C.15: 12 genuine complete early 1900s historic LOC records added to Sweden Norway Denmark Poland Austria; official checksum validated. Not WW2-era original masters. Six Commons streaming files from Phase 23C.14 preserved; no synthetic recordings or user uploads."
mf.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n","utf-8")
verified={x["id"]:{"country":x["country"],"title":x["title"],"loc_url":x["loc_catalog"],"md5":md5,"filename":x["filename"]} for x,raw,md5 in files}
(root/"music/northern-europe-batch9-verified.json").write_text(json.dumps(verified,ensure_ascii=False,indent=2)+"\n","utf-8")
print("SUCCESS verified 12 real historical performances; catalog updated",flush=True)
