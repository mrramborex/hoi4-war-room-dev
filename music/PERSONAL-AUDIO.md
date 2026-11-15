# TOBS Personal Music Loader (browser-local only)

## Purpose
User-provided recordings may be subject to independent recording and composition copyrights. The public radio keeps its 28 verified historical tracks on the repository; the user may select MP3s on their own device for **private browser playback** without hosting them or sending them to GitHub.

Open `radio.html`, turn on the receiver, select **LOAD PERSONAL MUSIC** and choose extracted MP3 files (not a RAR file). File objects are converted to temporary `blob:` URLs and played in the existing receiver with track switching and random tune-in. **No upload, network transmission, storage or persistent playlist** is performed. To use the files again after refreshing, choose them again.

The local matcher sends files with `Bing Crosby`, `Boogie Woogie`, or `Over There` to United States; files with `Firth of Forth` to United Kingdom; and `Erika`, `Drei Lilien`, `Teufelslied`, or `Machtigste` to Germany. Other selected files go to the currently tuned station.

The matcher is based only on supplied filenames and does **not** verify the recording date, performer, musical accuracy, historical context or licensing. The public `audio-manifest.json` is unchanged. The long modern Bundeswehr compilation in the user's archive is not an original WWII-era recording; do not characterize all personally loaded files as WWII recordings.

The personal loader must never automatically commit user-selected audio files or build public playback URLs for restricted recordings. If a source obtains independently documented permission covering website distribution, it can be separately processed through the existing rights audit.
