#!/usr/bin/env python3
"""Scan actual LOC downloadable package for minor-station repertoire, scouting only."""
import csv,json,re,urllib.request
from io import StringIO
from pathlib import Path
root=Path(__file__).resolve().parent.parent
def get(url):
 req=urllib.request.Request(url,headers={"User-Agent":"HOI4-War-Room-TOBS/1.0"})
 with urllib.request.urlopen(req,timeout=120) as res:return res.read().decode("utf-8-sig")
rows=list(csv.DictReader(StringIO(get("https://data.labs.loc.gov/jukebox/metadata.csv"))))
assert 5000<len(rows)<6500
targets={
 "Sweden":["swedish"],"Norway":["norwegian"],"Denmark":["danish"],"Netherlands":["dutch"],"Belgium":["flemish","belgian"],"Finland":["finnish"],"Mexico":["spanish"],"Spain":["spanish"],"Portugal":["portuguese"],"Poland":["polish"],"Canada":["french","english"],"Austria":["german"],"Turkey":["turkish"],"Greece":["greek"]
}
groups={}
for country,needles in targets.items():
 matches=[]
 for row in rows:
  language=(row.get("Language") or "").lower()
  audience=(row.get("Target audience") or row.get("Target Audience") or "").lower()
  genre=(row.get("Genre") or "").lower()
  if not any(q in (language+" "+audience+" "+genre) for q in needles):continue
  title=(row.get("Title") or "").strip()
  url=row.get("Url") or ""
  id_match=re.search(r"jukebox-(\d+)",url)
  if not title or not id_match:continue
  if any(x in genre for x in ["spoken","monologue","dialogue","comedies"]):continue
  item={"id":id_match.group(1),"title":title,"date":row.get("Date",""),"language":row.get("Language",""),"audience":row.get("Target audience",row.get("Target Audience","")),"genre":row.get("Genre",""),"credits":(row.get("Contributors_text") or "")[:330],"source":url}
  matches.append(item)
 matches.sort(key=lambda x:(not any(w in x["genre"].lower() for w in ("folk","ethnic","popular","instrument","dance","classical","music")), x["title"].lower()))
 groups[country]={"count":len(matches),"shortlist":matches[:50]}
out=root/"music/minor-nation-loc-scout.json"
out.write_text(json.dumps({"version":1,"scope":"LOC downloadable complete MP3 subset, no inferred rights for unverified compositions","rights":"https://data.labs.loc.gov/jukebox/README.html","groups":groups},indent=2,ensure_ascii=False)+"\n","utf-8")
print("Total records:",len(rows),flush=True)
print("Country metadata:",{k:v["count"] for k,v in groups.items()},flush=True)
