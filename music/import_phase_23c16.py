#!/usr/bin/env python3
"""Import seven genuine National Jukebox pre-1923 originals, one guarded batch."""
from pathlib import Path
import hashlib,base64,json,urllib.request
root=Path(__file__).resolve().parent.parent
info=json.loads((root/"music/phase-23c16-sources.json").read_text("utf-8"))
assert info["version"]==1 and len(info["tracks"])==7
def fetch(url,maximum):
 request=urllib.request.Request(url,headers={"User-Agent":"HOI4WarRoomTOBS/1.0 archive verification"})
 with urllib.request.urlopen(request,timeout=120) as response: contents=response.read(maximum+1)
 if len(contents)>maximum:raise ValueError("File exceeds size limit")
 return contents
archive=json.loads(fetch(info["archive_manifest"],3000000))
rows=[dict(zip(archive["cols"],r)) for r in archive["rows"]]
assert 5000<len(rows)<6500
files=[]
for item in info["tracks"]:
 ident=item["id"]
 assert item["url"]=="https://data.labs.loc.gov/jukebox/audio/jukebox-"+ident+"_1.mp3"
 matched=[r for r in rows if any("jukebox-"+ident+"_1.mp3" in str(v) for v in r.values())]
 if len(matched)!=1:raise ValueError("Not in downloadable LOC archive: "+ident)
 md5=None
 for k,v in matched[0].items():
  if "md5" in k.lower() and v:
   h=str(v).strip()
   if len(h)==32:md5=h.lower()
   else:
    try:md5=base64.b64decode(h).hex()
    except Exception:pass
 if not md5 or len(md5)!=32:raise ValueError("Missing checksum: "+ident)
 raw=fetch(item["url"],15000000)
 if not 100000<len(raw)<15000000 or not(raw.startswith(b"ID3") or raw[:1]==b"\xff"):raise ValueError("Invalid MP3 "+ident)
 actual=hashlib.md5(raw).hexdigest()
 if actual!=md5:raise ValueError("Original checksum mismatched: "+ident)
 files.append((item,raw,actual))
 print("VERIFIED",item["country"],ident,item["title"],actual,flush=True)
assert len(files)==7 and len({x["id"] for x,_,_ in files})==7
audio=root/"audio"
audio.mkdir(exist_ok=True)
manifest_file=root/"audio-manifest.json"
manifest=json.loads(manifest_file.read_text("utf-8"))
coverage_file=root/"music/station-coverage.json"
coverage=json.loads(coverage_file.read_text("utf-8"))
credits_file=root/"music/CREDITS.md"
credits=credits_file.read_text("utf-8")
assert manifest["version"]==1
for x,raw,_ in files:
 target=audio/x["filename"]
 if target.exists() and target.read_bytes()!=raw:raise ValueError("Existing master altered: "+x["filename"])
for x,raw,digest in files:
 (audio/x["filename"]).write_bytes(raw)
 playlist=manifest["stations"].setdefault(x["country"],[])
 src="audio/"+x["filename"]
 if not any(y.get("src")==src for y in playlist):
  playlist.append({"title":x["title"]+" — original "+x["date"][:4]+" recording","src":src})
manifest["notes"]="Phase 23C.16: 7 verified full original pre-1923 LOC recordings for Hungary, Czechoslovakia and Bulgaria; NOT 1936-1945 broadcasts. No synths or personal user uploads. Existing Commons sources preserved."
for station in coverage["stations"]:
 if station["country"] not in ("Hungary","Czechoslovakia","Bulgaria"):continue
 station["rights_cleared_track_count"]=len(manifest["stations"][station["country"]])
 station["research_status"]="audio_deployed"
 station["notes"]="23C.16: genuine pre-1923 historical LOC originals, verified MD5, from Hungarian, Czech/Bohemian or Bulgarian repertoire. Not WWII era or necessarily made in represented country."
proof={x["id"]:{"country":x["country"],"title":x["title"],"source":x["source"],"md5":digest,"filename":x["filename"]} for x,_,digest in files}
title="Phase 23C.16 — Hungary, Czechoslovakia, Bulgaria: seven original archive recordings"
if title not in credits:
 lines=["## "+title,"","Seven full, original pre-1923 performances from the Library of Congress National Jukebox. Each MP3 matched the official LOC manifest MD5. All are pre-WWII and must not be described as wartime broadcasts.","","| Station | Music | Year | Historical performers/composers | LOC source and MD5 |","| --- | --- | --- | --- | --- |"]
 for x,_,digest in files:
  lines.append("| "+x["country"]+" | "+x["title"]+" | "+x["date"]+" | "+x["credits"]+" | [LOC "+x["id"]+"]("+x["source"]+"), "+digest+" |")
 lines+=["","Bulgaria's selection is a historical accordion performance titled Bulgarian Dance. Czech/Bohemian works are grouped under Czechoslovakia for cultural repertoire; not Czech government radio broadcasts.",""]
 credits=credits.rstrip()+"\n\n"+"\n".join(lines)
manifest_file.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n","utf-8")
coverage_file.write_text(json.dumps(coverage,ensure_ascii=False,indent=2)+"\n","utf-8")
credits_file.write_text(credits,"utf-8")
(root/"music/phase-23c16-verified.json").write_text(json.dumps(proof,ensure_ascii=False,indent=2)+"\n","utf-8")
print("SUCCESS: 7 complete authentic recordings added in one checked batch",flush=True)
