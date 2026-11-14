#!/usr/bin/env python3
"""Post-process the lowlighter/metrics isocalendar SVG (idempotent).

1. The plugin emits an outer <svg> with a tight fixed height, so the bottom of
   the isometric calendar is cropped. We set a taller size plus a viewBox.
2. The calendar tiles are pale, so they vanish on GitHub's light theme
   (logged-out / incognito visitors). We draw our own dark card behind it.
"""
import re
import sys

path = sys.argv[1]
width = int(sys.argv[2]) if len(sys.argv) > 2 else 480
height = int(sys.argv[3]) if len(sys.argv) > 3 else 290

s = open(path, encoding="utf-8").read()

s, n = re.subn(
    r'<svg xmlns="http://www.w3.org/2000/svg"[^>]*>',
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
    f'viewBox="0 0 {width} {height}">',
    s,
    count=1,
)
if n != 1:
    sys.exit("outer <svg> tag not found; plugin output format changed?")

s = re.sub(r'<rect id="card-bg"[^>]*/>', "", s)
s, n = re.subn(
    r'<foreignObject [^>]*>',
    f'<rect id="card-bg" width="{width}" height="{height}" rx="12" '
    f'fill="#0d1117" stroke="#30363d"/>'
    f'<foreignObject x="14" y="10" width="{width - 28}" height="{height - 10}">',
    s,
    count=1,
)
if n != 1:
    sys.exit("foreignObject not found")

open(path, "w", encoding="utf-8").write(s)
