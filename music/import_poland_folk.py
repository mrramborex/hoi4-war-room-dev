#!/usr/bin/env python3
"""Phase 23C.7 — import one verified Polish historical folk recording.

No synthetic audio or copyrighted 1940s master. Validate LOC official checksum
before writing any file or manifest changes.
"""
from pathlib import Path
import hashlib,json,urllib.request
root=Path(__file__).resolve().parent.parent
r=json.loads((root/"music/poland-ulan-source.json").read_text("utf-8"))
assert r["version"]==1 and r["country"]=="Poland" and r["id"]=="17105"
assert r["url"]==f"https://data.labs.loc.gov/jukebox/audio/jukebox-{r['id']}_1.mp3"
request=urllib.request.Request(r["url"],headers={"User-Agent":"TOBS War Room historical archival importer"})
with urllib.request.urlopen(request,timeout=120) as response:raw=response.read(15_000_001)
assert 100_000<len(raw)<15_000_000
digest=hashlib.md5(raw).hexdigest()
if digest!=r["md5"]:raise ValueError("Official Library of Congress checksum failed: "+digest)
if not(raw.startswith(b"ID3") or raw[0]==255):raise ValueError("Invalid MP3 signature")
f=root/"audio-manifest.json"
m=json.loads(f.read_text("utf-8"))
assert m["version"]==1
station=m.setdefault("stations",{}).setdefault("Poland",[])
src="audio/"+r["filename"]
if not any(x.get("src")==src for x in station):
 station.append({"title":"Ulan (Pieśń Narodowa) — 1916 Polish historical folk performance","src":src})
m["notes"]="TOBS historical archive recordings: 27 earlier genuine selections plus 1 full Polish 1916 folk recording. No rejected synthesized music or copyrighted commercial WWII masters."
dest=root/"audio";dest.mkdir(exist_ok=True)
(dest/r["filename"]).write_bytes(raw)
f.write_text(json.dumps(m,indent=2,ensure_ascii=False)+"\n","utf-8")
print("SUCCESS: imported verified authentic 1916 Polish folk recording, MD5",digest)
