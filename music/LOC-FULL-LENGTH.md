# Full-length TOBS recordings (Phase 23C)

The first five WRS Victory Ballroom tracks were mistakenly imported from Citizen DJ's **short excerpt sample pack**. Those are not complete songs.

The Library of Congress [National Jukebox data package](https://data.labs.loc.gov/jukebox/) provides full recorded performances from 1900–1922. Its [rights statement](https://data.labs.loc.gov/jukebox/README.html) regards included recordings as U.S. public domain, and its [official file manifest](https://data.labs.loc.gov/jukebox/manifest.html) provides file-specific URLs and MD5 checksums.

`loc-full-recordings.json` contains the exact five sources and checksums. `import_loc_full.py` downloads all five, verifies MD5 and MP3 signatures, and **only then** replaces American station playlist entries. The development-only workflow removes five obsolete short WAV excerpts after a successful import. This makes complete historical songs available to the live-radio player while maintaining random mid-song tuning.

Proposed credit: Library of Congress, National Jukebox. Preserve the existing music rights hard gate for subsequent nations.
