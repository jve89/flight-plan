# Johan's learning path

Johan is learning Blender (installed on his Mac, version 5.x). Every 3D deliverable includes the
`.blend`, the scripts, and one exercise that changes one thing and shows the effect. Explain in plain
Dutch, one step at a time, with exact menu paths and shortcuts.

## Stage 1: find your way
- Navigate: middle mouse = orbit, Shift+middle = pan, scroll = zoom, numpad . = frame selection.
- Select in the Outliner; G move, R rotate, S scale, Esc cancel; Tab edit mode.
- If an editor turns into something else: Shift+F5 is the 3D Viewport (Fn on a Mac keyboard).
- Exercise: open `drone.blend`, click each part in the Outliner, move `battery` up with G Z.

## Stage 2: scripts build models
- New file first (scripts may wipe the scene), Scripting tab, Open `build_drone.py`, Alt+P.
- Exercise: change `R = 0.32` (motor distance), run again, compare.

## Stage 3: materials and light
- Material tab, Principled BSDF: change Base Color, Roughness, Metallic, Coat.
- Exercise: make the arms carbon instead of lime; render with F12.

## Stage 4: renders from the Terminal
```bash
/Applications/Blender.app/Contents/MacOS/Blender -b drone.blend -P render_drone.py -- preview ~/Desktop/renders
```
- Exercise: change the camera distance `R_CAM` and render a preview.

## Stage 5: modelling by hand (level 2)
- Bevel, loop cuts, subdivision surface, booleans for vents and screw holes.
- Exercise: add vents to the body with a boolean.
