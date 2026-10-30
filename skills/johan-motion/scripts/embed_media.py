#!/usr/bin/env python3
"""
embed_media.py  -  inject video, poster and frame sequence into an HTML template as data URIs,
for Claude artifacts (which cannot load remote media). Keeps the source template readable.

Usage:
    python3 embed_media.py template.html out.html --video loop.mp4 --frames "frames/*.webp" [--poster poster.webp]

Placeholders in the template: __VIDEO__ (src of <source>), __POSTER__ (video poster),
__FRAMES__ (a JS array literal, e.g. `var FRAMES = __FRAMES__;`).
If --poster is omitted, the first frame is used. Keep the result under 16 MB.
"""
import argparse, base64, glob, json, mimetypes, os

def uri(path):
    mime = mimetypes.guess_type(path)[0] or ("image/webp" if path.endswith(".webp") else "application/octet-stream")
    return f"data:{mime};base64," + base64.b64encode(open(path, "rb").read()).decode()

ap = argparse.ArgumentParser()
ap.add_argument("template"); ap.add_argument("out")
ap.add_argument("--video"); ap.add_argument("--frames"); ap.add_argument("--poster")
a = ap.parse_args()
html = open(a.template, encoding="utf-8").read()
frames = [uri(f) for f in sorted(glob.glob(a.frames))] if a.frames else []
if a.video:  html = html.replace("__VIDEO__", uri(a.video))
poster = uri(a.poster) if a.poster else (frames[0] if frames else "")
html = html.replace("__POSTER__", poster).replace("__FRAMES__", json.dumps(frames))
open(a.out, "w", encoding="utf-8").write(html)
mb = os.path.getsize(a.out) / 1e6
print(f"wrote {a.out}: {mb:.2f} MB" + ("  WARNING: over 16 MB" if mb > 16 else ""))
