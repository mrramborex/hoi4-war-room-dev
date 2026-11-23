#!/usr/bin/env python3
"""TOBS playlist integrity audit. Run: python3 music/audit_tobs_manifest.py"""
import json
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
manifest = json.loads((ROOT / "audio-manifest.json").read_text(encoding="utf-8"))
stations = manifest["stations"]
errors = []
warnings = []
sources = Counter()
titles = Counter()
total = 0
for country, playlist in stations.items():
    if not isinstance(playlist, list) or not playlist:
        errors.append(f"{country}: empty/non-list playlist")
        continue
    for index, track in enumerate(playlist, 1):
        total += 1
        title = track.get("title", "").strip()
        src = track.get("src", "").strip()
        if not title or not src:
            errors.append(f"{country} #{index}: missing title or src")
            continue
        titles[(country, title.casefold())] += 1
        sources[src] += 1
        if src.startswith(("http://", "https://")):
            if urlparse(src).scheme != "https":
                warnings.append(f"{country} #{index}: insecure remote URL")
        else:
            local = ROOT / src
            if not local.is_file():
                errors.append(f"{country} #{index}: local file missing: {src}")
for (country, title), count in titles.items():
    if count > 1:
        warnings.append(f"{country}: duplicate title {title!r} ({count})")
for src, count in sources.items():
    if count > 1:
        warnings.append(f"shared source URL ({count}): {src}")
remote = sum(src.startswith(("https://", "http://")) for src in sources for _ in range(sources[src]))
print(f"TOBS manifest: {len(stations)} represented stations, {total} playlist entries, {total-remote} local, {remote} remote")
print("NOTE: Remote URLs are not network-checked; this audit cannot establish playback or rights.")
for issue in errors:
    print("ERROR:", issue)
for issue in warnings:
    print("WARN:", issue)
raise SystemExit(1 if errors else 0)
