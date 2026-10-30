# Hero patterns

The hero media must show the subject. Pick the pattern that demonstrates best, not the most
impressive one. All four are approved; several roads lead to Rome.

| Pattern | Best when | Example |
|---|---|---|
| Looped video | Physical work or a place that looks good moving | Lendav (drone washing a roof), AirHub |
| Choreographed scroll scene | A product transforms something (input → output) | Complai A: law text becomes a task list |
| Explanatory infographic | A process or logic the visitor must understand | Complai B: AI use → risk level → documents |
| 3D object | A tangible deliverable or product that benefits from depth and touch | Complai C: dossier stack that fans out; friend's 3D plate on a phone |

## 1. Looped video

- Real footage only. 6–15 s seamless loop, muted, `playsinline`, `autoplay`, `loop`, with a poster
  image. Encode H.264 MP4 + WebM, ~2–4 MB, 1920 wide max; a smaller file for mobile via `<source media>`.
- Put a dark scrim (gradient or `rgba` overlay) under text for contrast; check 4.5:1 on the
  brightest frame.
- Respect reduced motion: show the poster, no autoplay.
- AirHub level: the video is a layer in a choreography. On scroll it moves (e.g. left, then right)
  while a schematic app UI in the center animates. That is pattern 1 + 2 combined.

## 2. Choreographed scroll scene

- Pin the stage (`ScrollTrigger pin: true`, scrub ~0.8) for about 2–3 viewport heights.
- Write the choreography as phases, each with a caption that changes in sync:
  1. show the input (raw, overwhelming),
  2. highlight what matters,
  3. move the input aside and build the output,
  4. resolve (progress fills, statuses turn done).
- Start state = the input centered alone; end state = input and output side by side.
- Mobile: no pinning; stack vertically and play each phase once when it enters the viewport.

## 3. Explanatory infographic

- SVG with real text, drawn paths (`stroke-dashoffset`), counters that increase as connections land.
- Three columns max on desktop. Labels must fit: shorten copy rather than shrinking text.
- **Mandatory separate mobile composition** (vertical flow). Never let the desktop SVG scale down
  until text is unreadable, and do not rely on horizontal scrolling.
- Use `stroke-linecap: butt` on paths that animate from zero, or round caps show stray dots.

## 4. 3D object

- Three.js. Procedural geometry is fine and often enough (extruded rounded shapes, lathe forms,
  canvas-generated textures with text). Use real assets when realism matters.
- Interaction: pointer tilt (lerp ~0.05), subtle idle float, scroll-driven state change
  (stack → fanned out, closed → open, assembled → exploded).
- The end state must make the object readable (labels facing the camera, overlap following the
  reading direction).
- Separate mobile composition (e.g. horizontal fan becomes vertical cascade, wider FOV).
- Render only while visible (IntersectionObserver), cap pixel ratio at 2, soft shadows on a
  `ShadowMaterial` ground plane for grounding.
- Details belong to the 3D pipeline skill when it exists.

## Hero copy (all patterns)

- Headline: the outcome or the visitor's situation, not the company name.
- One or two sentences of support.
- Primary CTA (a concrete action: "Doe de gratis scan", "Vraag een offerte aan") + ghost CTA.
- Optional small reassurance line under the buttons ("Vijf minuten. Geen account nodig.").
- The media peeks into the first viewport below the CTA, inviting the scroll.
