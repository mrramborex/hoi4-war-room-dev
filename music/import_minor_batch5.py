#!/usr/bin/env python3
"""Phase 23C.11: import authentic archived national performances.

All files must be present in the official LOC 5,882-file downloadable package,
match the exact original manifest hash, be nontrivial length and valid MP3s.
No synthetic audio, no user-uploaded copyrighted 1940s recordings.
"""
from pathlib import Path
import hashlib,base64,json,urllib.request
root=Path(__file__).resolve().parent.parent
batch=json.loads((root/"music/minor-batch5-sources.json").read_text("utf-8"))
assert batch["version"]==1 and len(batch["items"])==5
def read(url,limit):
 req=urllib.request.Request(url,headers={"User-Agent":"HOI4-War-Room-TOBS/1.0 (historical source verification)"})
 with urllib.request.urlopen(req,timeout=130) as r:
  data=r.read(limit+1)
 if len(data)>limit:raise ValueError("Source exceeds allowed file size")
 return data
manifest_json=json.loads(read("https://data.labs.loc.gov/jukebox/manifest.json",3000000))
assert "cols" in manifest_json and "rows" in manifest_json
records=[dict(zip(manifest_json["cols"],row)) for row in manifest_json["rows"]]
assert 5000<len(records)<6500
print("Archive manifest columns",manifest_json["cols"],flush=True)
all_rows={str(v) for row in records for v in row.values() if isinstance(v,str)}
print("LOC manifest records:",len(records),flush=True)
files=[]
for item in batch["items"]:
 ident=item["id"]
 expected_url=f"https://data.labs.loc.gov/jukebox/audio/jukebox-{ident}_1.mp3"
 if item["url"]!=expected_url:raise ValueError("Untrusted source URL")
 matched=[row for row in records if any(f"jukebox-{ident}_1.mp3" in str(v) for v in row.values())]
 if len(matched)!=1:raise ValueError(f"LOC original file not uniquely indexed: {ident}, {len(matched)}")
 row=matched[0]
 raw=read(expected_url,15000000)
 if not 100000<len(raw)<=15000000:raise ValueError("Suspicious original audio size")
 if not(raw.startswith(b"ID3") or raw[:1]==b"\xff"):raise ValueError("Expected MP3")
 expected_hash=None
 for key,val in row.items():
  if "md5" in key.lower() and val:
   h=str(val).strip()
   if len(h)==32:expected_hash=h.lower()
   else:
    try:expected_hash=base64.b64decode(h).hex()
    except Exception:pass
 if expected_hash is None:
  raise ValueError("Official MD5 metadata missing; columns "+str(list(row)))
 actual=hashlib.md5(raw).hexdigest()
 if actual!=expected_hash:raise ValueError(f"Official LOC MD5 mismatch for {ident}: {actual} vs {expected_hash}")
 files.append((item,raw,actual))
 print("VERIFIED",item["country"],ident,item["title"],len(raw),"bytes, MD5",actual,flush=True)
assert len({x["id"] for x,_,_ in files})==5
out=root/"audio-manifest.json"
music=json.loads(out.read_text("utf-8"))
assert music["version"]==1
dest=root/"audio";dest.mkdir(exist_ok=True)
for item,raw,_ in files:
 path=dest/item["filename"]
 if path.exists() and path.read_bytes()!=raw:raise ValueError("Existing audio differs from LOC: "+str(path))
for item,raw,_ in files:
 path=dest/item["filename"];path.write_bytes(raw)
 station=music["stations"].setdefault(item["country"],[])
 src="audio/"+item["filename"]
 if not any(t.get("src")==src for t in station):
  station.append({"title":item["title"]+" — original historical recording","src":src})
music["notes"]="Phase 23C.11: authentic complete pre-1923 historical recordings for Argentina, Brazil, Greece and Mexico; not genuine WWII-era 1940s masters, no synthetic audio or restricted user uploads. Official LOC original hash verified."
out.write_text(json.dumps(music,indent=2,ensure_ascii=False)+"\n","utf-8")
proof={x["id"]:{"country":x["country"],"title":x["title"],"md5":digest,"source":x["source"],"audio":x["url"],"file":x["filename"]} for x,_,digest in files}
(root/"music/minor-batch5-verified.json").write_text(json.dumps(proof,indent=2,ensure_ascii=False)+"\n","utf-8")
print("SUCCESS: 5 historical recordings fully verified and added",flush=True)
