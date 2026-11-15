# TOBS Music Credits — Full Historical Recordings

## Library of Congress — National Jukebox Data Package

**Suggested credit:** Library of Congress, National Jukebox.

Official source and rights statement: https://data.labs.loc.gov/jukebox/
Dataset documentation: https://data.labs.loc.gov/jukebox/README.html
Official per-file manifest and MD5 checksum evidence: https://data.labs.loc.gov/jukebox/manifest.html

The dataset includes complete historical recordings from 1900–1922 that the Library of Congress regards as public domain in the United States. The files were retrieved from the Library's official dataset, and MD5 checksums were matched to its file manifest. Do not substitute different recordings or restorations without validating their rights separately.

### WRS Victory Ballroom — United States

| Complete historic recording | LOC catalog item | File |
| --- | --- | --- |
| 'Joe Turner Blues' Medley | https://www.loc.gov/item/jukebox-19795/ | `audio/tobs-full-joe-turner-blues.mp3` |
| 12th Street Rag | https://www.loc.gov/item/jukebox-38191/ | `audio/tobs-full-12th-street-rag.mp3` |
| A Classical Spasm | https://www.loc.gov/item/jukebox-20378/ | `audio/tobs-full-classical-spasm.mp3` |
| A Rag-Time Episode | https://www.loc.gov/item/jukebox-129854/ | `audio/tobs-full-rag-time-episode.mp3` |
| After You've Gone | https://www.loc.gov/item/jukebox-313413/ | `audio/tobs-full-after-youve-gone.mp3` |

The full-length recordings replaced five short Citizen DJ excerpt files on 2026-11-15. All seven original synthetic station test clips were removed before this update.

Import sources and validation: `music/loc-full-recordings.json`, `music/import_loc_full.py`, `.github/workflows/import-loc-full.yml`.

**Rights rule:** Only recordings with documented public-domain status or an explicit free-use license permitting intended website redistribution are eligible. Other researched recordings remain outside the playable radio until they meet that gate.

## International repertoire — LOC National Jukebox Batch 1

Ten additional complete historical MP3 recordings imported on 2026-11-15, validated against individual official Library of Congress MD5 file checksums. They date from 1900–1922 and are drawn from the same public-domain-designated National Jukebox data package. Source and checksum index: https://data.labs.loc.gov/jukebox/manifest.html. **These recordings were made on Victor records in the United States**, and the station selections reflect language and musical repertoire, not original national radio broadcasts.

### United Kingdom

| Track | Library of Congress source | Performers / composition | Local file |
| --- | --- | --- | --- |
| A Bowl of Roses | [LOC 131863](https://www.loc.gov/item/jukebox-131863/) | Marguerite Dunlap; music Robert Coningsby Clarke, lyrics W.E. Henley | `audio/tobs-international-131863.mp3` |
| A Child's Song | [LOC 259778](https://www.loc.gov/item/jukebox-259778/) | John McCormack; lyrics Thomas Moore, music Charles Marshall | `audio/tobs-international-259778.mp3` |

### France

| Track | Library of Congress source | Performers / composition | Local file |
| --- | --- | --- | --- |
| Adieu, notre petite table | [LOC 127011](https://www.loc.gov/item/jukebox-127011/) | Geraldine Farrar; Jules Massenet | `audio/tobs-international-127011.mp3` |
| Air de Lia | [LOC 129652](https://www.loc.gov/item/jukebox-129652/) | Jeanne Gerville-Réache; Claude Debussy | `audio/tobs-international-129652.mp3` |

### Germany

| Track | Library of Congress source | Performers / composition | Local file |
| --- | --- | --- | --- |
| Aus der Jugendzeit | [LOC 213054](https://www.loc.gov/item/jukebox-213054/) | Emil Muench; Robert Radecke | `audio/tobs-international-213054.mp3` |
| Bärbchen | [LOC 127819](https://www.loc.gov/item/jukebox-127819/) | Ernestine Schumann-Heink; Hans Hermann | `audio/tobs-international-127819.mp3` |

### Italy

| Track | Library of Congress source | Performers / composition | Local file |
| --- | --- | --- | --- |
| A tanto amor | [LOC 28011](https://www.loc.gov/item/jukebox-28011/) | Giuseppe De Luca; Gaetano Donizetti | `audio/tobs-international-28011.mp3` |
| Abbietta zingara | [LOC 187534](https://www.loc.gov/item/jukebox-187534/) | Marcel Journet; Giuseppe Verdi | `audio/tobs-international-187534.mp3` |

### Soviet Union (historical pre-Soviet Russian repertoire)

| Track | Library of Congress source | Performers / composition | Local file |
| --- | --- | --- | --- |
| Eugene Onegin — Aria | [LOC 122060](https://www.loc.gov/item/jukebox-122060/) | Albert G. Janpolski; Pyotr Ilyich Tchaikovsky (pre-Soviet historical Russian repertoire) | `audio/tobs-international-122060.mp3` |
| Douchechka devitza | [LOC 16142](https://www.loc.gov/item/jukebox-16142/) | Nina Dimitrieff; Alexander Dargomyzhsky (pre-Soviet historical Russian repertoire) | `audio/tobs-international-16142.mp3` |

Japan is deliberately not included yet: no suitable Japanese-language music was found within this particular LOC dataset. Our public-domain/free-use gate still applies to other sources. 
