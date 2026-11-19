#!/usr/bin/env python3
"""TOBS Phase 23C.12 four real historical songs with LOC manifest validation.

All masters are original pre-1923 recordings. Verify that every source
is in the official downloadable collection and MD5-check all 4 before
touching any public audio or playlists. Safe to rerun.
"""
from pathlib import Path
import hashlib,base64,json,urllib.request
root=Path(__file__).resolve().parent.parent
batch=json.loads((root/"music/minor-batch6-sources.json").read_text("utf-8"))
assert batch["version"]==1 and len(batch["tracks"])==4
def read(url,limit):
 req=urllib.request.Request(url,headers={"User-Agent":"HOI4-War-Room-TOBS/1.0 verified historical public domain music"})
 with urllib.request.urlopen(req,timeout=130) as r:
  data=r.read(limit+1)
 if len(data)>limit:raise ValueError("Excessive archive file")
 return data
loc=json.loads(read("https://data.labs.loc.gov/jukebox/manifest.json",3000000))
assert "cols" in loc and "rows" in loc
rows=[dict(zip(loc["cols"],row)) for row in loc["rows"]]
assert 5000<len(rows)<6500
files=[]
for x in batch["tracks"]:
 ident=x["id"]
 url=f"https://data.labs.loc.gov/jukebox/audio/jukebox-{ident}_1.mp3"
 assert x["audio_url"]==url and x["filename"]==f"tobs-c12-{ident}.mp3"
 candidates=[r for r in rows if any(f"jukebox-{ident}_1.mp3" in str(v) for v in r.values())]
 if len(candidates)!=1:raise ValueError("Not a uniquely identified downloadable LOC recording: "+ident)
 file=read(url,15000000)
 if not (100000<len(file)<15000000) or not(file.startswith(b"ID3") or file[0]==255):raise ValueError("Invalid original recording: "+ident)
 expected=None
 for key,val in candidates[0].items():
  if "md5" in key.lower() and val:
   h=str(val).strip()
   if len(h)==32:expected=h.lower()
   else:
    try:expected=base64.b64decode(h).hex()
    except Exception:pass
 if not expected or hashlib.md5(file).hexdigest()!=expected:raise ValueError("Original LOC recording MD5 changed: "+ident)
 files.append((x,file,expected))
 print("VERIFIED",x["country"],x["title"],len(file),expected,flush=True)
assert len({x["id"] for x,_,_ in files})==4
path=root/"audio-manifest.json"
m=json.loads(path.read_text("utf-8"))
assert m["version"]==1
dest=root/"audio";dest.mkdir(exist_ok=True)
for x,b,_ in files:
 f=dest/x["filename"]
 if f.exists() and f.read_bytes()!=b:raise ValueError("Existing track differs: "+x["filename"])
for x,b,digest in files:
 (dest/x["filename"]).write_bytes(b)
 playlist=m["stations"].setdefault(x["country"],[])
 src="audio/"+x["filename"]
 if not any(t.get("src")==src for t in playlist):
  playlist.append({"title":x["title"]+" — original "+x["date"][:4]+" recording","src":src})
m["notes"]="TOBS: four additional historically authentic LOC music records added for Spain, Argentina, Mexico in Phase 23C.12. Historical pre-WWII original performances, not copyrighted commercial WWII masters, user uploads, or synthetic recordings."
path.write_text(json.dumps(m,ensure_ascii=False,indent=2)+"\n","utf-8")
proof={x["id"]:{"country":x["country"],"title":x["title"],"source":x["source_url"],"md5":digest,"filename":x["filename"]} for x,_,digest in files}
(root/"music/minor-batch6-verified.json").write_text(json.dumps(proof,ensure_ascii=False,indent=2)+"\n","utf-8")
print("SUCCESS: 4 complete historical performances imported",flush=True)
