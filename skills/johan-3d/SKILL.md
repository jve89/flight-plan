---
name: "johan-3d"
description: Johan's 3D pipeline for websites. Use this skill whenever a web page needs a 3D object or scene - a product, device, drone, vehicle, building, abstract shape or character - shown interactively (rotating, following the cursor, exploding into parts on scroll) or as photoreal pre-rendered images or video. Covers modelling in Blender via Python scripts, rendering with Cycles, exporting and optimising glTF/GLB, and showing models with Three.js in Astro or Claude artifacts. Also use it when Johan asks to learn Blender or 3D, mentions .blend, .glb, glTF, Three.js, Spline, renders or "3D", or wants something like his friend's 3D plate or Holo's 3D scenes. Works with johan-design-dna (look) and johan-motion (scroll behaviour).
---

# Johan's 3D Pipeline

One model, many uses. Build the model once (usually in Blender), then show it in the style the
project needs: realistic, stylised, technical, or pre-rendered. Johan approved a lab with all four
(`examples/drone-3d-lab-source.html`, model `examples/drone.blend`). The lab is **level 1** on the
quality ladder: it proves the pipeline, not the ceiling.

Johan is learning 3D. He executes in his own environment, so every 3D deliverable comes with the
script and the `.blend` file, plus one short exercise (see `reference/learning-path.md`).

Always also apply **johan-design-dna** (overall look) and **johan-motion** (scroll behaviour, tests).

## Principles

1. **3D preferably shows something real**: the product, its parts, how it works. Purely aesthetic
   3D (an object that is simply beautiful, sets the mood or carries the brand) is also fine when it's
   a deliberate choice, not filler. State in the plan which of the two it is.
2. **Style follows the project**, like everything in Johan's DNA. Choose per site:

| Style | How | Fits |
|---|---|---|
| Realistic | PBR materials, studio environment light, soft shadows | Products, hardware, drones, engineering |
| Stylised | Same model, soft pastel materials, playful idle motion, click reactions | Apps, consumer brands, exuberant sites |
| Technical | Transparent fill + glowing edges, systems highlighted one by one | Tech, compliance, engineering explainers |
| Pre-rendered | Cycles renders as a scroll-linked frame sequence | Hero shots where image quality matters most |

3. **Pick the cheapest route that reaches the quality the page needs** (`reference/routes.md`).
4. **Name every part** that should move or be highlighted. Names are the contract between Blender and the web page.
5. **Be honest about the ceiling.** Scripted modelling is excellent for clean, stylised and technical
   objects. Photoreal hero products need level 3–4 (see ladder); say so and propose the route.
6. **Mobile and slow devices are first-class**: separate camera framing, fewer labels, a poster image,
   time-based motion, rendering paused when off screen.

## Quality ladder

| Level | What changes | Typical effort |
|---|---|---|
| 1. Basic (the lab) | Primitive shapes with bevels, flat PBR materials, studio light | Minutes to an hour |
| 2. Refined modelling | Real dimensions from reference photos; subdivision and smooth transitions; details (screws, seams, vents, cables); booleans | Hours |
| 3. Real materials and light | Textures (carbon weave, wear, decals, labels), HDRI environment light (Poly Haven), baked ambient occlusion | Hours, assets |
| 4. Hero | Professional or purchased models, renders on a GPU machine, or a hired 3D artist | Days or budget |

State the level in the plan. Moving up one level is a valid follow-up task; never pretend level 1 is level 4.

## Workflow

1. **Plan** (short, in the reply): what the 3D must show, style, route, quality level, which parts
   are named and how they move, desktop vs mobile framing, fallback image. Ask for reference photos
   or real dimensions when realism matters.
2. **Model** with a Blender Python script (`scripts/build_drone.py` is the template): named parts, one
   object per moving part, origins where they rotate, modifiers applied before export.
   See `reference/blender-scripting.md`.
3. **Export + optimise** to GLB with the safe glTF-Transform flags, then **verify with
   `scripts/inspect_glb.py`** that all parts survived (`reference/export-optimize.md`).
4. **Render** (pre-rendered route): object rotates, camera and lights fixed, shadow catcher,
   transparent film, 15% framing margin, batch long jobs (`reference/rendering.md`, `scripts/render_drone.py`).
5. **Show it** with Three.js (`reference/threejs.md`): style by swapping materials, time-based damping,
   pause off screen, labels projected from part positions.
6. **Test**: johan-motion's `motion_test.py` for scroll behaviour on all devices, plus isolated 3D
   screenshots (`?only=a` pattern) with long waits, because headless Chromium renders WebGL in
   software at ~1 frame per second. See `reference/mobile-performance.md`.
7. **Self-critique** against the checklist below, fix, then deliver: page, `.blend`, scripts, exercise.

## Self-critique checklist

- [ ] Is the 3D a deliberate choice: does it explain something, or is it aesthetic on purpose? If it explains, would a photo do it better? If aesthetic, could it also show something useful (suggest once, don't block)?
- [ ] All named parts present after optimisation (`inspect_glb.py`)?
- [ ] Silhouette reads at a glance; nothing clipped by the frame (15% margin) at any angle or scroll position?
- [ ] Light: key, rim and environment; no blown-out or muddy areas; dark scenes not too dark?
- [ ] Exploded/animated end state readable; labels not overlapping (fewer on phones)?
- [ ] Mobile framing, poster fallback, reduced motion (static, final state), no WebGL (poster stays)?
- [ ] Off-screen sections stop rendering; pixel ratio ≤ 1.5; shadow maps ≤ 1024 unless hero?
- [ ] Download budget: model < 500 KB, frames < 1 MB where possible; artifact page < 16 MB?
- [ ] Which quality level is this, and what would the next level need? Say it in the delivery note.

## Reference files

- `reference/routes.md`: the five routes to 3D and when to use each.
- `reference/blender-scripting.md`: headless Blender, modelling rules, materials, naming, export.
- `reference/rendering.md`: Cycles studio setup, turntables, shadow catcher, batching, frame sizes.
- `reference/export-optimize.md`: glTF-Transform settings that keep parts separate; verification.
- `reference/threejs.md`: loading, environment light, the four style recipes, interaction, labels.
- `reference/mobile-performance.md`: framing, fallbacks, performance budget, how to test 3D.
- `reference/learning-path.md`: Johan's Blender learning path and exercises.
- `scripts/build_drone.py`, `scripts/render_drone.py`: templates. `scripts/inspect_glb.py`: verifier.
  `scripts/build_lab_page.py`: injects GLB, frames and poster into an artifact template.
- `examples/drone.blend`, `examples/drone-3d-lab-source.html`: the approved level-1 lab.
