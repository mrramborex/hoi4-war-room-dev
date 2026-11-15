# TOBS — Music Rights & Source Audit (Phase 23C.1)
Date: 2026-11-15. Scope: research guidance for U.S.-hosted development website; not legal advice.

## Gate: no audio is deployed without per-recording approval
Before adding any historical or third-party recording to `audio-manifest.json`, record:
- Track title; performer; composer and lyricist (when known); recording owner/label; first *publication* year and country.
- Original catalog/item page URL; direct recording URL; explicit rights/license statement URL; date reviewed and who reviewed it.
- Rights to **sound recording** and **underlying composition**, assessed separately; any foreign rights or restoration concerns.
- License exact version, attribution text, rights-holder name, modifications, redistribution/commercial permission, and any share-alike implications.
- **Decision**: candidate | needs_review | cleared | rejected. Only `cleared` is deployable. Store a rights statement snapshot/evidence separately where feasible.
- Audio-quality check, geographic/cultural relevance, accessible metadata, and content review.

## Status: sources researched, no third-party tracks licensed or added
The seven original synthesized proof-of-concept clips already in the radio are NOT cleared historical tracks. The 65-station tracker is in `music/station-coverage.json`. The empty candidate register in `music/track-candidates.csv` holds individual rights reviews.

## Legal reference, U.S. as of November 2026
- U.S. pre-1972 sound recordings first published 1923–1946 generally receive 100 years from year of first publication under the Music Modernization Act; 1925 publications generally entered U.S. public domain January 1, 2026.
- The musical **composition** and the **sound recording** can each have rights. Historical appearance, archive streaming access, and a date of composition do NOT prove permission to redistribute an audio file.
- Foreign recordings, remasters/transfers, performances, and non-U.S. audiences may create added complexity. Escalate uncertainty to specialist advice rather than assuming public domain.
- CC0 is preferred when properly applied by the rights-holder; CC BY 4.0 permits commercial reuse subject to attribution/license-link/change notices; CC BY-SA has share-alike adaptation obligations. Treat NC, ND, unspecified, contradictory, or unclear rights as needs_review unless separately authorized.
- Do not infer that user support via Ko-fi makes NonCommercial licensing safe.
- Avoid copying protected broadcasts just because they appear on YouTube, streaming sites, Internet Archive, or in a museum streaming collection.
- Use original commissioned music with written rights permission as a fallback for 1936–1945 styles.

## Source leads (collection-level research, NOT individual-track clearance)
1. Library of Congress Citizen DJ — National Jukebox Jazz, pre-1923 samples identified public domain; commercial reuse supported:
   https://citizen-dj.labs.loc.gov/loc-jukebox-jazz/use/
2. Library of Congress Citizen DJ — Popular Music, same stated rights for selected pre-1923 samples:
   https://citizen-dj.labs.loc.gov/loc-jukebox-popular/use/
3. Library of Congress Citizen DJ — Musical Theater, same stated rights for selected clips:
   https://citizen-dj.labs.loc.gov/loc-jukebox-musical-theater/use/
4. Library of Congress Citizen DJ — Edison / Inventing Entertainment (collection-specific public-domain explanation):
   https://citizen-dj.labs.loc.gov/loc-edison/use/
5. National Jukebox catalog (research ONLY; library's stream permission does not automatically authorize our redistribution):
   https://www.loc.gov/collections/national-jukebox/about-this-collection/rights-and-access/
6. Wikimedia Commons music files; investigate per-file recording rights and license:
   https://commons.wikimedia.org/wiki/Category:Audio_files_of_music

## Rights sources
- U.S. Copyright Office: https://www.copyright.gov/music-modernization/faq.html
- Library of Congress recording rights overview: https://ask.loc.gov/recorded-sound/faq/313179
- CC0: https://creativecommons.org/public-domain/
- CC BY 4.0: https://creativecommons.org/licenses/by/4.0/deed.en
- CC license differences: https://creativecommons.org/cc-licenses/

## 23C.2 entry gate
Identify and verify candidate recordings for the **seven major-power countries**; distinguish public-domain excerpts from original or newly licensed recordings, and do not put unclear items in the playable manifest. Confirm final musical mix and credits before release.
