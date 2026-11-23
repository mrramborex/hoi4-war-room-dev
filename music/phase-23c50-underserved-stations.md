# Phase 23C.50 — Underserved Station Audit and Sourcing Gate

**Decision:** Stop adding Swedish music. Focus on stations with one or two distinct audio sources. This report is a verified manifest audit, **not** a claim that external files play or are rights-cleared. No production deployment.

Baseline: **232 distinct source URLs**, **261 playlist entries**, **65 stations**.

## Underserved stations (one or two unique sources)

| Station | Playlist entries | Unique source URLs | Entries explicitly marked modern/after 1945 |
|---|---:|---:|---:|
| Afghanistan | 1 | 1 | 0 |
| Aussa | 1 | 1 | 1 |
| Australia | 1 | 1 | 0 |
| Belgium | 1 | 1 | 1 |
| Bulgaria | 1 | 1 | 0 |
| Canada | 1 | 1 | 0 |
| Chile | 1 | 1 | 1 |
| Estonia | 1 | 1 | 0 |
| Ethiopia | 1 | 1 | 1 |
| Iceland | 1 | 1 | 1 |
| Iraq | 1 | 1 | 0 |
| Latvia | 1 | 1 | 1 |
| Lithuania | 1 | 1 | 1 |
| Paraguay | 1 | 1 | 1 |
| Philippines | 1 | 1 | 1 |
| Romania | 1 | 1 | 0 |
| South Africa | 1 | 1 | 1 |
| Switzerland | 1 | 1 | 0 |
| Turkey | 1 | 1 | 1 |
| Uruguay | 1 | 1 | 1 |
| Austria | 2 | 2 | 0 |
| British Raj / India | 2 | 2 | 0 |
| Communist China | 2 | 2 | 0 |
| Congo | 2 | 2 | 0 |
| Gansu Ma | 2 | 2 | 0 |
| Greece | 2 | 2 | 0 |
| Guangdong Clique | 2 | 2 | 0 |
| Guangxi Clique | 2 | 2 | 0 |
| Hebei-Chahar | 2 | 2 | 0 |
| Iran | 2 | 2 | 1 |
| Khotan Ma | 2 | 2 | 0 |
| New Zealand | 2 | 2 | 2 |
| Ningxia Ma | 2 | 2 | 0 |
| Northeastern Army | 2 | 2 | 0 |
| Portugal | 2 | 2 | 1 |
| Qinghai Ma | 2 | 2 | 0 |
| Shandong Clique | 2 | 2 | 0 |
| Shanxi | 2 | 2 | 0 |
| Sichuan Clique | 2 | 2 | 0 |
| Sinkiang | 2 | 2 | 0 |
| Yugoslavia | 2 | 2 | 1 |
| Yunnan | 2 | 2 | 0 |

## Phase rules

1. **Sweden frozen** — no new Swedish music or playlist placements unless the user explicitly reverses this decision.
2. Prioritize the one-source stations first, then two-source stations; aim for at least three distinct recordings per station.
3. Prefer original 1936–1945 recordings and full songs. Earlier period recordings are fallback only if authentic wartime sources cannot be found.
4. Candidate sources can be questionable or incompletely documented **in research**, but not in the playable manifest until the exact audio file, metadata, playable format, provenance and rights are checked.
5. Do not treat a photograph, modern anthem recording, unverified URL or a second URL for the same performance as a newly verified historical track.
6. Keep new commits consolidated, and do not claim browser testing or rights clearance without evidence.

## Research result this phase

- Broad searches for Canadian, Australian and Romanian wartime audio yielded mostly non-music media or unrelated image archives, so no new audio was added.
- A verified Commons file page exists for a **1942 Korean Aegukga recording** (https://commons.wikimedia.org/wiki/File:Aegukga,_1942.oga), but it is not assigned to any existing country station because no appropriate Korean station appears in the current 65-station map and US recording rights are not established. Research-only candidate.
- Existing single-entry stations often rely on modern US Navy Band performances or much older recordings. These count as playlist entries, not authenticated 1940s sources.

Next: target **Canada, Australia, Romania, Belgium, Estonia, Bulgaria, Turkey and the Philippines** with direct archive item searches and individual recording verification. Add only files that pass checks.
