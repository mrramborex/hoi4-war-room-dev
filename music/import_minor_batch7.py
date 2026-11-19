#!/usr/bin/env python3
"""Import 4 full archival tracks with strict original-file checksum verification.

No synthetic music, no private uploads, no copyrighted 1940s commercial masters.
Only changes the TOBS development repo and only after all files pass.
"""
import hashlib,base64,json,urllib.request
from pathlib import Path
root=Path(__file__).resolve().parent.parent
batch=json.loads((root/"music/minor-batch7-sources.json").read_text("utf-8"))
assert batch["version"]==1 and len(batch["tracks"])==4
def get(url,limit):
 req=urllib.request.Request(url,headers={"User-Agent":"HOI4-War-Room-TOBS/1.0 archival verify"})
 with urllib.request.urlopen(req,timeout=120) as r:b=r.read(limit+1)
 if len(b)>limit:raise ValueError("Download too large")
 return b
archive=json.loads(get("https://data.labs.loc.gov/jukebox/manifest.json",3_000_000))
assert "cols" in archive and "rows" in archive
rows=[dict(zip(archive["cols"],r)) for r in archive["rows"]]
assert 5000<len(rows)<6500
files=[]
for item in batch["tracks"]:
 ident=item["id"]
 url=f"https://data.labs.loc.gov/jukebox/audio/jukebox-{ident}_1.mp3"
 assert item["audio_url"]==url and item["filename"]==f"tobs-c13-{ident}.mp3"
 matching=[r for r in rows if any(f"jukebox-{ident}_1.mp3" in str(v) for v in r.values())]
 if len(matching)!=1:raise ValueError("No exact official archived item: "+ident)
 expected=None
 for k,v in matching[0].items():
  if "md5" in k.lower() and v:
   s=str(v).strip()
   if len(s)==32:expected=s.lower()
   else:
    try:expected=base64.b64decode(s).hex()
    except Exception:pass
 if not expected or len(expected)!=32:raise ValueError("Missing trusted LOC checksum: "+ident)
 raw=get(url,15_000_000)
 if not (100_000<len(raw)<15_000_000) or not(raw.startswith(b"ID3") or raw[0]==255):raise ValueError("Unexpected audio: "+ident)
 actual=hashlib.md5(raw).hexdigest()
 if actual!=expected:raise ValueError(f"LOC MD5 mismatch {ident}: {actual} != {expected}")
 files.append((item,raw,actual))
 print("VERIFIED",ident,item["country"],item["title"],len(raw),"bytes",flush=True)
assert len({i["id"] for i,_,_ in files})==4
mp=root/"audio-manifest.json"
manifest=json.loads(mp.read_text("utf-8"))
assert manifest["version"]==1
dest=root/"audio";dest.mkdir(exist_ok=True)
for item,raw,digest in files:
 p=dest/item["filename"]
 if p.exists() and p.read_bytes()!=raw:raise ValueError("Existing audio mismatch: "+item["filename"])
for item,raw,digest in files:
 (dest/item["filename"]).write_bytes(raw)
 station=manifest["stations"].setdefault(item["country"],[])
 src="audio/"+item["filename"]
 if not any(x.get("src")==src for x in station):
  station.append({"title":item["title"]+" — original "+item["date"][:4]+" recording","src":src})
manifest["notes"]="TOBS 23C.13: 4 real pre-1923 recordings added: a 1915 multinational Allied anthems band medley including Belgium's anthem, an original 1916 Argentine tango, and two Mexican repertoire tracks. No WWII-era master claimed; private MP3s and rejected synthetic music not hosted."
mp.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n","utf-8")
(root/"music/minor-batch7-verified.json").write_text(json.dumps({x["id"]:{"md5":digest,"source":x["source_url"],"country":x["country"],"title":x["title"]} for x,_,digest in files},ensure_ascii=False,indent=2)+"\n","utf-8")
print("SUCCESS all 4 LOC sources verified and imported",flush=True)
