# Rendering (pre-rendered route)

## Studio setup (see `scripts/render_drone.py`)
- Cycles, CPU in the sandbox (GPU/Metal on Johan's Mac is far faster), samples 12 + denoising,
  adaptive sampling, max bounces 4, persistent data. View transform AgX, "Medium High Contrast".
- Lights: large soft key (area 1.0 m, front-right, above), cool rim from behind-left, weak fill, small top.
- **Shadow catcher floor** (`floor.is_shadow_catcher = True`) + **transparent film**
  (`render.film_transparent = True`, RGBA PNG). The render blends into any page colour and there is
  no visible floor edge. (First attempt had a visible floor edge and blue floor glare.)
- **Turntable: rotate the object, not the camera.** Parent all meshes to an empty and rotate it.
  Lights stay fixed relative to the camera, so lighting is consistent in every frame.
  (First attempt orbited the camera: lighting jumped between angles.)
- **Framing margin 15%** at every angle: test the widest angle (props diagonal) before the full run.
  The lab clipped a propeller tip at some angles.

## Time and batches
In the sandbox one 896×504 frame took ~27 s (opaque) to ~45 s (shadow catcher + alpha) on one core.
48 frames ≈ 35 minutes: render in batches that fit the command limit
(`render_drone.py -- turntable OUT START END TOTAL`). Render one preview and check it before batching.

## Output sizes
- Keep RGBA PNG masters.
- For a page with a known background, **flatten onto that colour** and save WebP (quality ~60):
  48 frames = 544 KB. With alpha WebP the same frames were 3.7 MB.
- Use Pillow in one process for batch conversion; the sandbox ffmpeg webp encoder has no alpha options.
- Frames per turn: 48 for a full 360° (7.5° steps) feels smooth with scroll easing; 24 is choppy.
