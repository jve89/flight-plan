"""
render_drone.py  -  studio-lit photoreal renders of drone.blend with Cycles.

  blender -b drone.blend -P render_drone.py -- preview OUTDIR
  blender -b drone.blend -P render_drone.py -- turntable OUTDIR START END TOTAL

Turntable: the camera orbits 360 degrees over TOTAL frames while rising slightly;
render frames START..END (inclusive) so long jobs can be split into batches.
"""
import bpy, math, sys, os
from mathutils import Vector

args = sys.argv[sys.argv.index("--") + 1:]
mode, out = args[0], args[1]
os.makedirs(out, exist_ok=True)
sc = bpy.context.scene

def srgb(h):
    h = h.lstrip("#"); c = [int(h[i:i+2], 16) / 255 for i in (0, 2, 4)]
    return tuple(((x + 0.055) / 1.055) ** 2.4 if x > 0.04045 else x / 12.92 for x in c)

# world: dark studio
w = bpy.data.worlds.new("Studio"); sc.world = w; w.use_nodes = True
w.node_tree.nodes["Background"].inputs[0].default_value = (*srgb("#07090d"), 1)
w.node_tree.nodes["Background"].inputs[1].default_value = 1.0

# floor that catches soft shadows and a faint reflection
bpy.ops.mesh.primitive_plane_add(size=12, location=(0, 0, -0.1375))
floor = bpy.context.object
fm = bpy.data.materials.new("Floor"); fm.use_nodes = True
fb = fm.node_tree.nodes["Principled BSDF"]
fb.inputs["Base Color"].default_value = (*srgb("#050608"), 1); fb.inputs["Roughness"].default_value = 0.62
floor.data.materials.append(fm)
floor.is_shadow_catcher = True          # invisible floor, only the shadow remains
sc.render.film_transparent = True       # transparent background: blends into any page colour

def area(name, loc, size, energy, color="#ffffff"):
    bpy.ops.object.light_add(type="AREA", location=loc)
    l = bpy.context.object; l.name = name
    l.data.size = size; l.data.energy = energy; l.data.color = srgb(color)
    d = Vector((0, 0, 0)) - l.location
    l.rotation_euler = d.to_track_quat("-Z", "Y").to_euler()
    return l

area("Key", (0.9, -0.7, 1.3), 1.0, 90)
area("Rim", (-1.0, 1.0, 0.7), 0.8, 75, "#9db8ff")
area("Fill", (0.0, -1.6, 0.3), 1.6, 14)
area("Top", (0.0, 0.0, 1.6), 0.8, 18)

# camera on an orbit
target = bpy.data.objects.new("Target", None); sc.collection.objects.link(target)
target.location = (0, 0, -0.02)
cam_data = bpy.data.cameras.new("Cam"); cam_data.lens = 55
cam = bpy.data.objects.new("Cam", cam_data); sc.collection.objects.link(cam); sc.camera = cam
tc = cam.constraints.new("TRACK_TO"); tc.target = target; tc.track_axis = "TRACK_NEGATIVE_Z"; tc.up_axis = "UP_Y"

# product turntable: the DRONE rotates, camera and lights stay fixed -> consistent lighting
pivot = bpy.data.objects.new("Pivot", None); sc.collection.objects.link(pivot)
for o in list(sc.objects):
    if o.type == "MESH" and o is not floor:
        o.parent = pivot
a0 = math.radians(-50); R_CAM = 1.75
cam.location = (math.cos(a0) * R_CAM, math.sin(a0) * R_CAM, 0.55)

def place(t):  # t in [0,1)
    pivot.rotation_euler = (0, 0, -t * 2 * math.pi)

sc.render.engine = "CYCLES"; sc.cycles.device = "CPU"
sc.cycles.samples = 12; sc.cycles.use_denoising = True; sc.cycles.max_bounces = 4; sc.cycles.diffuse_bounces = 2; sc.cycles.glossy_bounces = 2; sc.cycles.transmission_bounces = 2; sc.render.use_persistent_data = True; sc.cycles.use_adaptive_sampling = True
sc.render.resolution_x, sc.render.resolution_y = 1280, 720
sc.render.resolution_percentage = 70
sc.view_settings.view_transform = "AgX"; sc.view_settings.look = "AgX - Medium High Contrast"
sc.render.image_settings.file_format = "PNG"; sc.render.image_settings.color_mode = "RGBA"

if mode == "preview":
    place(0.0)
    sc.render.filepath = os.path.join(out, "preview.png")
    bpy.ops.render.render(write_still=True)
else:
    start, end, total = int(args[2]), int(args[3]), int(args[4])
    for f in range(start, end + 1):
        place(f / total)
        sc.render.filepath = os.path.join(out, f"t_{f:03d}.png")
        bpy.ops.render.render(write_still=True)
print("RENDER_OK")
