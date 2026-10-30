# Five routes to 3D

| Route | How | Best for | Device cost | Notes |
|---|---|---|---|---|
| 1. Procedural in Three.js | Shapes and canvas textures built in the browser | Abstract objects, UI-like props (Complai dossier stack) | Light | No asset pipeline; limited realism |
| 2. Blender script → real-time GLB | Claude writes a Blender script, exports GLB, Three.js shows it | Products and hardware that react to cursor and scroll | Medium | The lab's routes A–C |
| 3. Blender → pre-rendered | Cycles renders images/video, tied to scroll (johan-motion scrub pattern) | Hero shots; Holo-style scenes | Very light | Best quality per byte; not interactive |
| 4. Existing assets | Poly Haven (CC0 models, HDRIs, textures), Sketchfab (check each licence) | Realistic objects you should not model yourself | Medium | Check licence and polygon count; rename parts |
| 5. AI image-to-3D | Services that turn photos into models (verify current tools and terms) | Quick drafts, organic shapes | Varies | Messy topology, odd UVs; clean up in Blender |

Choosing:
- Must react to the cursor or come apart → route 2 (or 4 if realism is required).
- Must look like a product photo → route 3, often combined with route 2 elsewhere on the page.
- Abstract or schematic → route 1 or the technical style of route 2.
- Hosting in a Claude artifact: no remote files; embed GLB and frames as base64 (see `scripts/build_lab_page.py`).
- Spline (visual web 3D editor) is an option when Johan wants to edit scenes by hand; it exports to the web.
