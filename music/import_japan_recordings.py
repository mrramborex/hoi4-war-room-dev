#!/usr/bin/env python3
"""Download precisely two public-domain original Japanese recordings from Wikimedia Commons.

The original archive source and per-layer licensing are documented in
music/japan-recordings-batch-1.json. Fail closed if Commons metadata changes
or the media checks fail; no playlist is modified unless both files validate.
"""
import hashlib,json,urllib.parse,urllib.request
from pathlib import Path
root=Path(__file__).resolve().parent.parent
catalog=json.loads((root/"music/japan-recordings-batch-1.json").read_text("utf-8"))
assert catalog["version"]==1 and catalog["station"]=="Japan" and len(catalog["items"])==2
files=[]
for item in catalog["items"]:
 title=item["commons_title"]
 q=urllib.parse.urlencode({"action":"query","format":"json","prop":"imageinfo","iiprop":"url|size|sha1","titles":title})
 req=urllib.request.Request("https://commons.wikimedia.org/w/api.php?"+q,headers={"User-Agent":"HOI4-War-Room-TOBS/1.0 (research archive import; contact via GitHub)"})
 with urllib.request.urlopen(req,timeout=35) as res:payload=json.load(res)
 pages=list(payload["query"]["pages"].values())
 if len(pages)!=1 or "imageinfo" not in pages[0]:raise ValueError("Source not found: "+title)
 info=pages[0]["imageinfo"][0]
 url=info["url"]
 if not url.startswith("https://upload.wikimedia.org/wikipedia/commons/"):raise ValueError("Unexpected Commons host: "+url)
 if item.get("sha1") and item["sha1"]!=info["sha1"]:raise ValueError("Locked historical SHA1 changed: "+title)
 if item.get("size") and item["size"]!=info["size"]:raise ValueError("Historical archive filesize changed: "+title)
 if info["size"]>10_000_000:raise ValueError("Oversized audio file")
 media_req=urllib.request.Request(url,headers={"User-Agent":"HOI4-War-Room-TOBS/1.0 (research archive import; contact via GitHub)"})
 with urllib.request.urlopen(media_req,timeout=90) as resp:raw=resp.read(10_000_001)
 if len(raw)!=info["size"] or not raw.startswith(b"OggS"):raise ValueError("Invalid OGG or mismatched size: "+title)
 if hashlib.sha1(raw).hexdigest()!=info["sha1"]:raise ValueError("SHA1 checksum mismatch: "+title)
 files.append((item,raw))
 print("VERIFIED",title,len(raw),"bytes SHA1",info["sha1"])
assert len({x["filename"] for x,_ in files})==2
manifest_file=root/"audio-manifest.json"
manifest=json.loads(manifest_file.read_text("utf-8"))
assert manifest["version"]==1
assert not manifest.setdefault("stations",{}).get("Japan")
manifest["stations"]["Japan"]=[{"title":x["title"]+" — historical recording","src":"audio/"+x["filename"]} for x,_ in files]
manifest["notes"]="Phase 23C live receiver: 17 complete historical recordings across 7 major-power stations. Japanese originals from Wikimedia Commons have explicit PD recording/composition tags. Silent stations have no playlist."
dest=root/"audio";dest.mkdir(exist_ok=True)
for x,raw in files:(dest/x["filename"]).write_bytes(raw)
manifest_file.write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+"\n","utf-8")
print("SUCCESS: Japanese station populated with two complete historic recordings")
