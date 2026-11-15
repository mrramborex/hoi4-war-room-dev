# Phase 23C.2 — Library of Congress Jazz Import
Five exact public-domain **Citizen DJ Jazz curated excerpts** are staged in `loc-curated-excerpts.json`, each with a specific original WAV download URL, item page, and rights evidence.
Official archive reuse statement: https://citizen-dj.labs.loc.gov/loc-jukebox-jazz/use/

**Status:** source URLs verified; external WAV bytes are not yet in this repository. The original seven synth test tracks remain in `audio-manifest.json`.

## Import on a connected computer
1. From the repository root run `python3 music/import_loc_jazz.py`.
2. Confirm each WAV is validated, and `audio-manifest.json` lists all new local `audio/tobs-loc-*.wav` files.
3. Commit the five WAV files and updated manifest to the development branch.
4. Test playback and track transitions in the development radio; leave production unchanged.

Do not deploy alternate commercial recordings from National Jukebox without a separate rights review. These rights claims apply specifically to **Citizen DJ's curated excerpt downloads**.
Suggested credit for the site's music credits: **Citizen DJ Project, Library of Congress, National Jukebox.**
