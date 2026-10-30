# Stack

Johan is the executor in his own repo: propose stack changes and installs, never assume them.
Ask before adding dependencies. Return complete files, and ask for the current version of a file
before changing it.

## Default

| Part | Choice | Notes |
|---|---|---|
| Framework | **Astro** | Static-first, fast. Interactive parts as islands or plain `<script>` in components |
| Fonts | `@fontsource-variable/inter` | Self-hosted Inter |
| Scroll animation | **GSAP + ScrollTrigger** | Industry standard for pinning and scrubbing. Verify the current license terms on gsap.com before a commercial project (it was made free for all uses, but check) |
| Smooth scroll | **Lenis** (`lenis` on npm) | Optional; gives the premium scroll feel. Skip if it fights native behavior on a page |
| 3D | **Three.js** (`three` on npm) | Load only on pages that use it |
| Hosting | Cloudflare Pages (his current sites) | |

## Prototypes and Claude artifacts (no build step)

Load UMD builds from a CDN with pinned versions, as in `examples/complai-proef.html`:

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/lenis@1.1.13/dist/lenis.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
```

Three r128 is the last UMD build on cdnjs: no `RoundedBoxGeometry`, no `CapsuleGeometry`,
no `RoomEnvironment` in core. Use `ExtrudeGeometry` from a rounded `Shape` instead.
In Astro, use current npm versions instead.

## Glue code that works

```js
gsap.registerPlugin(ScrollTrigger);
const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

// Lenis + ScrollTrigger
let lenis = null;
if (!reduce && window.Lenis) {
  lenis = new Lenis({ lerp: 0.1, smoothWheel: true });
  lenis.on('scroll', ScrollTrigger.update);
  gsap.ticker.add(t => lenis.raf(t * 1000));
  gsap.ticker.lagSmoothing(0);
}

// Desktop pinned choreography vs mobile play-once
const mm = gsap.matchMedia();
mm.add('(min-width: 900px)', () => {
  const tl = gsap.timeline({ defaults: { ease: 'none' }, scrollTrigger: {
    trigger: stage, start: 'top top', end: '+=2600', pin: true, scrub: 0.8, invalidateOnRefresh: true } });
  // phases...
});
mm.add('(max-width: 899px)', () => {
  gsap.timeline({ scrollTrigger: { trigger: stage, start: 'top 70%', once: true } });
  // same phases, no pin
});

document.fonts?.ready.then(() => ScrollTrigger.refresh());
```

## Hard-won lessons

1. **Create ScrollTriggers in page order, pinned sections first.** Any trigger created before a
   pin further down ignores that pin's spacing (the variant switcher in the proof page lit up
   too early until its triggers were created last).
2. **Reduced motion and no-JS show final states.** Write CSS so the default (no JS) state is the
   readable end state; let JS set the starting state for the animation.
3. **Headline reveal**: wrap each line in `.line > span` with `overflow: hidden` and a little
   bottom padding (`padding-bottom: .09em; margin-bottom: -.09em`) so descenders are not clipped.
4. **3D performance**: `setPixelRatio(Math.min(devicePixelRatio, 2))`, render only when visible,
   lerp scroll progress inside the render loop for smoothness.
5. **3D rotation order**: when a card tilts toward the camera and also turns, set
   `rotation.order = 'YXZ'` or the card shears.
6. **Testing 3D in headless Chromium is slow** (software rendering). Wait several seconds before
   screenshots or you capture mid-transition states.
7. **Canvas textures with text**: wait for `document.fonts.load('800 58px Inter')` before drawing.
