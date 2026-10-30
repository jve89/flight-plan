# Three.js

## Loading
- Artifacts/prototypes (UMD, pinned):
  `three.js/r128/three.min.js` (cdnjs), `three@0.128.0/examples/js/loaders/GLTFLoader.js` and
  `three@0.128.0/examples/js/libs/meshopt_decoder.js` (jsdelivr).
- Astro: current `three` from npm with ES module imports (`three/addons/...`). Ask before installing.
- Embedded model: decode base64 to an ArrayBuffer and call `loader.parse(buffer, "", onLoad, onError)`
  after `MeshoptDecoder.ready`. One parse, then `gltf.scene.clone(true)` per view.

## Finding parts
A node with one material is a `Mesh`; with several materials it becomes a `Group` of Meshes.
Match by name, topmost wins:
```js
function partsOf(model){ const map={}; model.traverse(o=>{ if(!map[o.name] && PART_RE.test(o.name)) map[o.name]=o; }); return map; }
```
(The lab first matched only Meshes and found 7 of 18 parts.)

## Renderer and light
`antialias`, `alpha`, `outputEncoding = sRGBEncoding`, ACES tone mapping, `physicallyCorrectLights`,
pixel ratio ≤ 1.5. Environment light without an HDR file: build a small scene with a back-side box and
bright panels and run `PMREMGenerator.fromScene()` (see `studioEnv()` in the lab). Ground: a
`ShadowMaterial` plane. Key light with soft shadow (map 1024).

## The four style recipes
- **Realistic**: original materials, `envMapIntensity` 1.5–1.6, exposure ~1.45 on dark pages.
- **Stylised**: replace materials by name with `MeshStandardMaterial` (roughness .8, pastel palette),
  warm environment, light ground shadow (.22), idle bob, cursor follow, click = hop and spin.
- **Technical**: transparent `MeshBasicMaterial` fill (opacity .03–.22) + `EdgesGeometry(geometry, 28)`
  line overlay; highlight one system at a time by lerping colour and opacity.
- **Pre-rendered**: frames on a canvas (johan-motion scrub pattern), no WebGL.

## Motion
- **Time-based damping**, never per-frame lerp (slow devices lag otherwise):
  `cur += (target - cur) * (1 - Math.exp(-lambda * dt))`, lambda 3 (cursor) to 7–9 (scroll).
- Scroll drives a progress value through ScrollTrigger; the render loop damps towards it.
- Exploded view: per-part offset vectors (outward + up/down by part type) times an eased progress.
- Rotation order `YXZ` when a part tilts and turns.
- Labels: `part.getWorldPosition(v).project(camera)` → screen px; fade in late in the explode; flip to
  the left side when on the right third; fewer labels on phones.

## Loop
Render only while visible (IntersectionObserver, rootMargin 0), pass `dt` to the tick, stop the
requestAnimationFrame when hidden.
