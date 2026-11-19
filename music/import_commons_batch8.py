#!/usr/bin/env python3
"""Phase 23C.14: direct verified original Commons sound files for 5 silent stations.

Never fetch user-provided commercial uploads or synthetic content. Source each
archive item from its exact Commons File: record, compare the downloaded bytes
to Commons' published SHA1 and size, and fail closed for missing rights docs.
"""
from pathlib import Path
import hashlib,json,urllib.parse,urllib.request,re,html
root=Path(__file__).resolve().parent.parent
d=json.loads((root/"music/commons-batch8-sources.json").read_text("utf-8"))
assert d["version"]==1 and len(d["items"])==6
def get(url,limit):
 req=urllib.request.Request(url,headers={"User-Agent":"HOI4WarRoomTOBS/1.0 (historical recordings importer; contact via github.com/mrramborex/hoi4-war-room-dev)"})
 with urllib.request.urlopen(req,timeout=150) as r:contents=r.read(limit+1)
 if len(contents)>limit:raise ValueError("Downloaded file too large")
 return contents
files=[]
for x in d["items"]:
 name=x["commons_file"]
 assert re.fullmatch(r"[\wÀ-ž\s(),.'-]+\.(?:ogg|oga)",name,re.UNICODE)
 query=urllib.parse.urlencode({"action":"query","format":"json","prop":"imageinfo","iiprop":"url|sha1|size","titles":"File:"+name})
 data=json.loads(get("https://commons.wikimedia.org/w/api.php?"+query,2_000_000))
 pages=list(data["query"]["pages"].values())
 if len(pages)!=1 or not pages[0].get("imageinfo"):raise ValueError("Commons original missing: "+name)
 info=pages[0]["imageinfo"][0]
 url=info["url"]
 assert urllib.parse.urlparse(url).hostname=="upload.wikimedia.org"
 assert url.lower().endswith((".ogg",".oga"))
 raw=get(url,15_000_000)
 if not (50000<len(raw)<15_000_000) or not raw.startswith(b"OggS"):raise ValueError("Invalid source Ogg file: "+name)
 sha=hashlib.sha1(raw).hexdigest()
 if len(raw)!=info["size"] or sha!=info["sha1"]:raise ValueError("Commons SHA1 mismatch: "+name)
 files.append((x,raw,sha,url))
 print("VERIFIED",x["country"],x["title"],len(raw),"bytes",sha,flush=True)
assert len({x["filename"] for x,_,_,_ in files})==6
mf=root/"audio-manifest.json"
manifest=json.loads(mf.read_text("utf-8"))
assert manifest["version"]==1
dest=root/"audio";dest.mkdir(exist_ok=True)
for x,raw,sha,url in files:
 old=dest/x["filename"]
 if old.exists() and old.read_bytes()!=raw:raise ValueError("Existing file differs: "+x["filename"])
for x,raw,sha,url in files:
 (dest/x["filename"]).write_bytes(raw)
 station=manifest["stations"].setdefault(x["country"],[])
 entry={"title":x["title"],"src":"audio/"+x["filename"]}
 if not any(t.get("src")==entry["src"] for t in station):station.append(entry)
manifest["notes"]="Phase 23C.14: historic original recordings for Canada 1915, Australia 1915, Netherlands 1899/1920, Estonia 1914; Belgian 2003 US Navy band is a genuine but MODERN performance of a historic anthem. Each Commons original Ogg verified with official SHA1. No user uploads or synthetic tracks."
mf.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n","utf-8")
out={x["filename"]:{"title":x["title"],"country":x["country"],"source":x["source_url"],"file_url":url,"sha1":sha,"size":len(raw),"original_date":x["recording_date"],"rights":"See source Commons page; recording public domain or U.S. federal government performance"} for x,raw,sha,url in files}
(root/"music/commons-batch8-verified.json").write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n","utf-8")
print("SUCCESS: 6 complete, real performances for 5 new stations",flush=True)
