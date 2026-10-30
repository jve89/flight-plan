# Timing, stack and glue code

## Stack
GSAP + ScrollTrigger (+ MotionPathPlugin when needed), Lenis for smooth scroll, Three.js only
for real-time 3D. In Astro install from npm (ask Johan first); in prototypes and artifacts use
pinned CDN builds:

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/MotionPathPlugin.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/lenis@1.1.13/dist/lenis.min.js"></script>
```

## Values that worked

| Thing | Value |
|---|---|
| Scrub smoothing on pinned scenes | `scrub: 0.4` (0.8 felt laggy and let sections release unfinished) |
| Pinned scene length | 2200–3200 px (`end: "+=2600"`); Johan approved this tempo |
| Hold buffer at the end of a pinned timeline | ~20% of its duration (`tl.to({}, {duration: .9})`) |
| Headline line reveal | `yPercent: 110`, 1.15 s, `expo.out`, stagger .09 |
| Small reveals | 0.4–0.8 s, `power2.out` / `power3.out`, 8–16 px movement |
| UI transitions (hover, state) | 0.15–0.3 s |
| Caption crossfade | 0.2–0.25 s, 8 px |
| Stagger for lists | 0.08–0.2 s per item |
| Ease for scrubbed timelines | `"none"` as default, `power2.inOut` for big layout moves |

## Glue code

```js
gsap.registerPlugin(ScrollTrigger);
const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;
if (reduce) { showFinalStates(); /* no pins, no scrub */ }

let lenis = null;
if (!reduce && window.Lenis) {
  lenis = new Lenis({ lerp: 0.1, smoothWheel: true });
  lenis.on("scroll", ScrollTrigger.update);
  gsap.ticker.add(t => lenis.raf(t * 1000));
  gsap.ticker.lagSmoothing(0);
}

const mm = gsap.matchMedia();
mm.add("(min-width: 900px)", () => { /* pinned, scrubbed choreography */ });
mm.add("(max-width: 899px)", () => { /* unpinned, scrubbed or toggled */ });
```

## Refresh rules (prevents the cold-load bug)
Positions are measured once; anything that changes layout afterwards breaks them. On a first
visit fonts, video and images arrive late, so a step could be wrong only the first time.

```js
ScrollTrigger.config({ ignoreMobileResize: true });
const refreshSoon = (() => { let t; return () => { clearTimeout(t); t = setTimeout(() => ScrollTrigger.refresh(), 120); }; })();
document.fonts?.ready.then(refreshSoon);
video?.addEventListener("loadedmetadata", refreshSoon);
addEventListener("load", refreshSoon);
new ResizeObserver(() => refreshSoon()).observe(document.body); // guard against loops with a height check
```

## Order rules
- Create ScrollTriggers in page order. Any trigger defined before a pin further down ignores
  that pin's spacing (navigation highlighting lit up too early until created last).
- `anticipatePin: 1` on pins avoids a one-frame jump when pinning starts.
- `invalidateOnRefresh: true` whenever values are functions of layout.

## Header on light sections
The pill header must adapt to the section under it. Toggle a class while a `.theme-light`
section is under the header:

```js
document.querySelectorAll(".theme-light").forEach(sec =>
  ScrollTrigger.create({ trigger: sec, start: "top 48px", end: "bottom 48px",
    toggleClass: { targets: ".site-header", className: "on-light" } }));
```
