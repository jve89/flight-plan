# Mobile, fallback and performance

- **Framing per device**: separate camera distance, FOV and look-at height for narrow screens.
- **Poster image**: a rendered still behind each canvas, hidden when the view is ready. Stays visible
  if WebGL fails or JS is off.
- **Reduced motion**: no idle motion or spin, scroll views show their final state.
- **Labels**: max ~5 on phones.
- **Budget**: model < 500 KB (meshopt), textures WebP/KTX2, frames < 1 MB, pixel ratio ≤ 1.5,
  shadow map 1024, one shadow-casting light, pause off-screen views.
- **Several WebGL views on one page** compete for the CPU/GPU; keep them small and paused off screen.

## Testing 3D
- Headless Chromium has no GPU: use `--use-gl=angle --use-angle=swiftshader --enable-unsafe-swiftshader`;
  expect ~1 frame per second. Wait 6–12 s before screenshots or you capture mid-transition states.
- **Test each 3D view in isolation** (`?only=a|b|c` query switch in the page) when several views
  exist; together they starve each other in software rendering.
- Run johan-motion's `motion_test.py` for scroll logic on all four devices.
- Ask Johan to check the real page on his Mac and phone: software rendering hides GPU-specific issues.
