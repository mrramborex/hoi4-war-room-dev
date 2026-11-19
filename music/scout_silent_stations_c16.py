#!/usr/bin/env python3
"""Phase 23C.16 discovery only: locate source-verified cultural leads for silent TOBS countries."""
import csv,json,re,urllib.request
from io import StringIO
from pathlib import Path
root=Path(__file__).resolve().parent.parent
req=urllib.request.Request("https://data.labs.loc.gov/jukebox/metadata.csv",headers={"User-Agent":"HOI4WarRoomTOBS/1.0 archival metadata research"})
with urllib.request.urlopen(req,timeout=120) as response:
  content=response.read().decode("utf-8-sig")
rows=list(csv.DictReader(StringIO(content)))
assert 5000<len(rows)<6500
targets={
 "Hungary":["hungarian","magyar","csardas","csárdás","liszt","brahms hungarian"],
 "Romania":["romanian","rumanian","roumanian","ivanovici","enescu","romania"],
 "Portugal":["portuguese (portugal)","portugal","fado","portuguese"],
 "Czechoslovakia":["czech","bohemian","dvorak","dvořák","smetana","czechoslovak"],
 "Yugoslavia":["serbian","croatian","slovenian","yugoslav","serbo-croatian"],
 "Turkey":["turkish","ottoman","turkey","osmanli","istanbul"],
 "Bulgaria":["bulgarian","bulgaria"],
 "Iceland":["icelandic","iceland"],
 "Latvia":["latvian","latvia"],
 "Lithuania":["lithuanian","lithuania"],
 "Ethiopia":["ethiopian","ethiopia","abyssinian"],
 "Iran":["persian","iranian","persia"],
 "South Africa":["south african","afrikaans","boer"],
 "Chile":["chilean","chile"],
 "Uruguay":["uruguayan","uruguay"],
 "Paraguay":["paraguayan","paraguay"]
}
groups={}
for nation,terms in targets.items():
 items=[]
 for row in rows:
  searchable=" | ".join([row.get(k,"") or "" for k in ["Title","Language","Genre","Contributors_text","Target audience","Notes"]]).lower()
  matched=[term for term in terms if term in searchable]
  if not matched:continue
  item_url=row.get("Url") or ""
  m=re.search(r"jukebox-(\d+)",item_url)
  if not m:continue
  items.append({"id":m.group(1),"title":row.get("Title",""),"date":row.get("Date",""),"language":row.get("Language",""),"genre":row.get("Genre",""),"credits":(row.get("Contributors_text") or "")[:500],"source":item_url,"matched":matched})
 items.sort(key=lambda i:(-len(i["matched"]),i["title"]))
 groups[nation]={"count":len(items),"candidates":items[:100]}
out=root/"music/phase-23c16-archive-scout.json"
out.write_text(json.dumps({"version":1,"phase":"23C.16","source":"https://data.labs.loc.gov/jukebox/metadata.csv","note":"Metadata-only leads. Country relevance, soundtrack suitability, copyright and downloadable files require separate human review and hash checks. European composers are not proof original recordings were made within that country.", "groups":groups},indent=2,ensure_ascii=False)+"\n","utf-8")
print("Total LOC metadata:",len(rows))
print("Results:",{k:v["count"] for k,v in groups.items()},flush=True)
