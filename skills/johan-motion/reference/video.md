# Video as a building block

Holo and AirHub get much of their quality from video: real footage, screen recordings of the
product, and pre-rendered 3D loops, moved and layered with code. Use video when the subject
is physical, or when a product UI should look truly alive.

## Sources
- **Real footage** of the work (best). Ask Johan; never use stock footage pretending to be the client.
- **Screen recordings** of the product: record at 2× resolution, hide cursor or use a smooth
  cursor, real-looking data, 6–15 s per feature, crop to the interesting area. Tools such as
  Screen Studio or the built-in recorder plus an editor work; verify current tools before advising.
- **Pre-rendered 3D** (Blender, Spline, AI video): good for isometric "how it works" scenes like Holo.

## Encoding (ffmpeg)
Looping background or layer video, H.264 MP4, no audio, fast start:
```bash
ffmpeg -i in.mp4 -vf scale=960:-2 -c:v libx264 -crf 30 -preset slow -an \
  -movflags +faststart -profile:v main -pix_fmt yuv420p loop.mp4
```
Add a WebM/AV1 variant for big hero videos on real sites. Target 0.5–3 MB per loop.
Mobile: serve a smaller file via `<source media="(max-width: 899px)">`.

Frame sequence for scroll-linked video:
```bash
ffmpeg -i in.mp4 -vf "fps=6,scale=960:-2" -c:v libwebp -quality 52 frames/f_%03d.webp
```

Poster: the first frame (or the most telling frame) as WebP.

## Markup
```html
<video autoplay muted loop playsinline preload="auto" poster="poster.webp" aria-label="What the video shows">
  <source src="loop.mp4" type="video/mp4">
</video>
```
Reduced motion: remove `autoplay`, show the poster.

## Claude artifacts
Published artifact pages cannot load remote media. Embed small files as data URIs (keep the
page under 16 MB). In the lab: 0.6 MB loop + 1.1 MB of frames → 2.1 MB page. Build the page
from a template with placeholders (`__VIDEO__`, `__POSTER__`, `__FRAMES__`) and inject the
base64 data with a small script, so the source stays readable.

## Text over video
Scrim (gradient or overlay) under text; check contrast against the brightest frame; small
labels on video get a glass background (`rgba(7,9,13,.62)` + blur).
