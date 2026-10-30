# Performance

- Animate `transform` and `opacity` wherever possible. Layout properties (width, left, top) are
  acceptable for one or two large elements in a pinned scene, not for many small ones.
- Canvas: size to `clientWidth × min(devicePixelRatio, 2)`; redraw only when the frame changes.
- Pause what is off screen: IntersectionObserver for 3D render loops and heavy canvas work;
  videos outside the viewport can be paused.
- Images and frames: WebP, `decoding="async"`, sized to their display size.
- One smooth-scroll library at most (Lenis); never combine with CSS `scroll-behavior: smooth`
  on the same scroller.
- `will-change` only on elements that are actively animating; remove afterwards.
- Budget per page: total media under ~5 MB on mobile; first view under ~1.5 MB.
- Test on the mobile viewport with CPU throttling when possible (Playwright CDP
  `Emulation.setCPUThrottlingRate`, rate 4).
