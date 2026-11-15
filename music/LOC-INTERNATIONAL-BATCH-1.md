# Phase 23C.2 — International Full-Length Music Batch 1

Ten complete archival recordings have been selected from the Library of Congress [National Jukebox dataset](https://data.labs.loc.gov/jukebox/) for five previously silent major-power stations: United Kingdom, France, Germany, Italy, Soviet Union. The latter carries **pre-Soviet Russian repertoire** as a temporary cultural-music fit; do not misrepresent these as original Soviet broadcasts. Audio was recorded on Victor records in the United States, so this is historical repertoire, not genuine local radio output.

Sources:
- Rights statement: https://data.labs.loc.gov/jukebox/README.html
- File-by-file MD5 hashes: https://data.labs.loc.gov/jukebox/manifest.html
- Exact recording IDs, performer/composer credits, and hashes: `music/loc-international-batch-1.json`

The Library's dataset covers 1900–1922 and identifies its items as assumed public domain in the United States. These are full records, unlike Citizen DJ's short sample pack. International rights and the underlying works must still be considered for use in other jurisdictions; country assignments are editorial and not assertions of provenance. New recordings must continue to pass the public-domain/free-use-only rule.

Japan is not filled by this batch: LOC's searched dataset had no Japanese-language matches. No unverified Japanese audio is substituted.

The importer `music/import_loc_international.py` validates each downloaded file against the LOC manifest checksum before writing any media or changing the playable radio manifest. Its GitHub Action runs solely on the development repository.
