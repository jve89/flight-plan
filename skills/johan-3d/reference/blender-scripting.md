# Blender scripting

## Running Blender
- Headless: `blender -b -P script.py -- ARGS` (arguments after `--` are for the script).
- On Johan's Mac the binary is `/Applications/Blender.app/Contents/MacOS/Blender`.
- In Claude's sandbox: download the Linux LTS build from download.blender.org/release, extract it,
  run the binary (tested: 4.5 LTS). The `bpy` pip wheel may be unavailable for the platform.
- Sandbox commands time out after ~5 minutes and background processes die with the command:
  split long work into batches.
- Inside the Blender GUI (Scripting tab, Alt+P) a script that starts with
  `read_factory_settings(use_empty=True)` wipes the open scene. Tell Johan to run it in a new file.

## Modelling rules (from the drone lab)
- **One object per part that moves or is highlighted**, named in lowercase with an index:
  `body`, `battery`, `arm_1`…`arm_4`, `motor_1`, `prop_1`. These names are the API for the web page.
- **Origins** where the part rotates: a propeller's origin on the motor axis (set the 3D cursor there,
  `origin_set(type="ORIGIN_CURSOR")`), others at their geometric centre.
- **Bevel everything** (Bevel modifier, `limit_method="ANGLE"`, 3–5 segments). Sharp primitive edges
  are what makes 3D look cheap. Then `shade_smooth_by_angle(angle≈40°)`.
- **Apply modifiers** before export (`modifier_apply`) so the GLB contains the final geometry.
- **Join** sub-pieces that move together (`bpy.ops.object.join`) and give the result the part name.
- **Proportions first**: compare with a reference photo before adding detail. The first lab model was
  "too blocky"; flatter body, slimmer arms and longer motor distance fixed it.
- Scale in metres, Z up in Blender. The glTF exporter converts to Y up (`export_yup=True`).

## Materials (Principled BSDF, Blender 4.x/5.x input names)
`Base Color`, `Roughness`, `Metallic`, `Coat Weight`, `Coat Roughness`. Convert hex colours to linear
(see `srgb()` in `build_drone.py`). Lab palette: carbon `#16191e` rough .34 coat .6; metal `#a7afb8`
metallic 1 rough .26; paint `#c3d92b` rough .38; glass `#0a0e14` rough .04 coat 1.
Name materials meaningfully: the web page swaps styles by material name.

## Export
```python
bpy.ops.export_scene.gltf(filepath="model.glb", export_format="GLB",
                          export_apply=True, export_yup=True, use_selection=False)
```
Also save the `.blend` (`wm.save_as_mainfile`) for Johan.
