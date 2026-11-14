#!/usr/bin/env python3
"""Post-process the lowlighter/metrics isocalendar SVG so it is never cropped.

The plugin emits an outer <svg> with a tight fixed height, so the bottom of
the isometric calendar gets cropped. We add vertical padding and a viewBox so
the whole image scales uniformly and the calendar always fits.
"""
import re
import sys

path = sys.argv[1]
width = int(sys.argv[2]) if len(sys.argv) > 2 else 480
height = int(sys.argv[3]) if len(sys.argv) > 3 else 290

s = open(path, encoding="utf-8").read()
s, n = re.subn(
    r'<svg xmlns="http://www.w3.org/2000/svg" width="[^"]*" height="\d+"',
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
    f'viewBox="0 0 {width} {height}"',
    s,
    count=1,
)
if n != 1:
    sys.exit("outer <svg> tag not found; plugin output format changed?")
open(path, "w", encoding="utf-8").write(s)
