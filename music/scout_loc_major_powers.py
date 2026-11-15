#!/usr/bin/env python3
"""Locate culturally plausible complete LOC recordings; scouting only, no publishing."""
import csv,json,re,urllib.request
from io import StringIO
from pathlib import Path

ROOT=Path(__file__).resolve().parent.parent
def read(url):
 req=urllib.request.Request(url,headers={"User-Agent":"TOBS-War-Room/1.0"})
 with urllib.request.urlopen(req,timeout=90) as r:return r.read().decode("utf-8-sig")
records=list(csv.DictReader(StringIO(read("https://data.labs.loc.gov/jukebox/metadata.csv"))))
print("LOC metadata records:",len(records))
if not (5000 <= len(records) <= 6500):raise ValueError("Unexpected metadata count")
print("Metadata fields:",sorted(records[0]))
def field(x,k):return (x.get(k) or "")
# Collect a manageable sample for human/AI curation. Language is evidence,
# not conclusive proof of origin, genre or station suitability.
groups={"France":("french","français"),"Germany":("german","deutsch"),"Italy":("italian","napolet"),"United Kingdom":("english",),"Soviet Union":("russian",),"Japan":("japanese",)}
results={}
for country,langs in groups.items():
 matches=[]
 for rec in records:
  language=field(rec,"Language").lower()
  if not any(t in language for t in langs):continue
  title=field(rec,"Title")
  if not title:continue
  page=field(rec,"Url")
  ident=re.search(r"jukebox-(\d+)",page)
  if not ident:continue
  entry={"id":ident.group(1),"title":title,"language":field(rec,"Language"),"genre":field(rec,"Genre"),"date":field(rec,"Date"),"contributors":field(rec,"Contributors_text")[:220],"source_item":page}
  matches.append(entry)
 # Favor musical rather than spoken/monologue content and metadata completeness.
 matches.sort(key=lambda r:(not any(t in r["genre"].lower() for t in ("music","opera","song","classical","folk","instrument","dance","vocal")),len(r["contributors"])==0,r["title"].lower()))
 results[country]={"total_matches":len(matches),"shortlist":matches[:35]}
print("Language matches:",{k:v["total_matches"] for k,v in results.items()})
output=ROOT/"music/major-power-loc-scout.json"
output.write_text(json.dumps({"version":1,"collection":"LOC National Jukebox full-length 1900-1922 public-domain dataset","rights":"https://data.labs.loc.gov/jukebox/README.html","purpose":"Discovery only, requires deliberate item-level cultural fit selection; not automatically deployed","groups":results},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
