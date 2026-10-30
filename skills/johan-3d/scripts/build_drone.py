"""
build_drone.py  -  builds a quadcopter in Blender with named parts, then saves
drone.blend and exports drone.glb (glTF binary) for the web.

Run headless:  blender -b -P build_drone.py -- /output/dir
Blender is Z-up; the glTF exporter converts to Y-up for Three.js automatically.
Every part is its own object with its origin at its own center, so the web page can
move parts individually (exploded view) and spin the propellers.
"""
import bpy, bmesh, math, sys, os
from mathutils import Vector

OUT = sys.argv[sys.argv.index("--") + 1] if "--" in sys.argv else "/tmp"
bpy.ops.wm.read_factory_settings(use_empty=True)

# ---------- helpers ----------
def mat(name, color, rough=0.5, metal=0.0, coat=0.0, coat_rough=0.3):
    m = bpy.data.materials.new(name); m.use_nodes = True
    b = m.node_tree.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value = (*color, 1)
    b.inputs["Roughness"].default_value = rough
    b.inputs["Metallic"].default_value = metal
    b.inputs["Coat Weight"].default_value = coat
    b.inputs["Coat Roughness"].default_value = coat_rough
    return m

def srgb(h):  # hex -> linear rgb
    h = h.lstrip("#"); c = [int(h[i:i+2], 16) / 255 for i in (0, 2, 4)]
    return tuple(((x + 0.055) / 1.055) ** 2.4 if x > 0.04045 else x / 12.92 for x in c)

def finish(obj, material, bevel=0.0, segs=3, smooth=True, name=None):
    if bevel:
        m = obj.modifiers.new("Bevel", "BEVEL"); m.width = bevel; m.segments = segs; m.limit_method = "ANGLE"
    if smooth:
        bpy.ops.object.shade_smooth_by_angle(angle=math.radians(40))
    obj.data.materials.clear(); obj.data.materials.append(material)
    if name: obj.name = name; obj.data.name = name
    return obj

def apply_all(obj):
    bpy.context.view_layer.objects.active = obj
    for m in list(obj.modifiers):
        bpy.ops.object.modifier_apply(modifier=m.name)

def join(objs, name):
    bpy.ops.object.select_all(action="DESELECT")
    for o in objs:
        apply_all(o); o.select_set(True)
    bpy.context.view_layer.objects.active = objs[0]
    bpy.ops.object.join()
    o = bpy.context.object; o.name = name; o.data.name = name
    bpy.ops.object.origin_set(type="ORIGIN_GEOMETRY", center="BOUNDS")
    return o

def box(size, loc, rot=(0, 0, 0)):
    bpy.ops.mesh.primitive_cube_add(size=1, location=loc, rotation=rot)
    o = bpy.context.object; o.scale = size; bpy.ops.object.transform_apply(scale=True)
    return o

def cyl(r, h, loc, rot=(0, 0, 0), v=40):
    bpy.ops.mesh.primitive_cylinder_add(radius=r, depth=h, location=loc, rotation=rot, vertices=v)
    return bpy.context.object

# ---------- materials ----------
M = {
    "carbon":   mat("Carbon",   srgb("#16191e"), rough=0.34, coat=0.6, coat_rough=0.18),
    "graphite": mat("Graphite", srgb("#2b3038"), rough=0.55),
    "lime":     mat("Lime",     srgb("#c3d92b"), rough=0.38, coat=0.3),
    "metal":    mat("Metal",    srgb("#a7afb8"), rough=0.26, metal=1.0),
    "prop":     mat("Prop",     srgb("#101215"), rough=0.42),
    "glass":    mat("Glass",    srgb("#0a0e14"), rough=0.04, metal=0.3, coat=1.0, coat_rough=0.02),
    "rubber":   mat("Rubber",   srgb("#0c0c0d"), rough=0.9),
    "accent":   mat("Accent",   srgb("#1f5eff"), rough=0.4),
}

parts = []
R = 0.32  # motor distance from center along each axis (diagonal ~0.42 m)

# body
body = box((0.24, 0.27, 0.055), (0, 0, 0)); finish(body, M["carbon"], bevel=0.022, segs=5, name="body"); apply_all(body)
# top cover
cover = box((0.17, 0.21, 0.026), (0, -0.005, 0.038)); finish(cover, M["graphite"], bevel=0.012, segs=5, name="cover"); apply_all(cover)
# battery with a lime stripe
bat = box((0.12, 0.07, 0.036), (0, 0.0, 0.069)); finish(bat, M["graphite"], bevel=0.008, name="bat_core")
stripe = box((0.122, 0.016, 0.038), (0, 0.024, 0.069)); finish(stripe, M["lime"], bevel=0.004)
battery = join([bat, stripe], "battery")
# GPS mast
mast = cyl(0.005, 0.07, (0, -0.085, 0.085)); finish(mast, M["graphite"])
puck = cyl(0.024, 0.011, (0, -0.085, 0.122)); finish(puck, M["graphite"], bevel=0.006)
gps = join([mast, puck], "gps")

for i, (sx, sy) in enumerate([(1, 1), (-1, 1), (-1, -1), (1, -1)]):
    ang = math.atan2(sy, sx)
    length = math.hypot(R, R) - 0.06
    mid = Vector((math.cos(ang), math.sin(ang), 0)) * (0.09 + length / 2)
    # arm: lime tube + fold joint
    tube = cyl(0.0105, length, (mid.x, mid.y, 0.0), rot=(0, math.pi / 2, ang), v=24); finish(tube, M["lime"])
    jpos = Vector((math.cos(ang), math.sin(ang), 0)) * 0.15
    joint = cyl(0.017, 0.026, (jpos.x, jpos.y, 0.0), v=24); finish(joint, M["carbon"], bevel=0.004)
    arm = join([tube, joint], f"arm_{i+1}")
    # motor: metal bell + base
    mx, my = sx * R, sy * R
    base = cyl(0.026, 0.018, (mx, my, 0.014), v=40); finish(base, M["carbon"], bevel=0.004)
    bell = cyl(0.031, 0.034, (mx, my, 0.04), v=40); finish(bell, M["metal"], bevel=0.006)
    cap = cyl(0.01, 0.01, (mx, my, 0.062), v=24); finish(cap, M["accent"], bevel=0.003)
    motor = join([base, bell, cap], f"motor_{i+1}")
    # propeller: two twisted blades + hub, origin on the motor axis
    blades = []
    for k in (0, 1):
        b = box((0.19, 0.028, 0.0035), (mx + math.cos(k * math.pi) * 0.1, my + math.sin(k * math.pi) * 0.1, 0.074),
                rot=(math.radians(12 if k == 0 else -12), 0, 0))
        m = b.modifiers.new("Bevel", "BEVEL"); m.width = 0.012; m.segments = 4
        finish(b, M["prop"]); blades.append(b)
    hub = cyl(0.012, 0.012, (mx, my, 0.074), v=24); finish(hub, M["prop"], bevel=0.004)
    prop = join(blades + [hub], f"prop_{i+1}")
    bpy.ops.object.origin_set(type="ORIGIN_CURSOR") if False else None
    # put origin exactly on the motor axis
    bpy.context.scene.cursor.location = (mx, my, 0.074)
    bpy.ops.object.origin_set(type="ORIGIN_CURSOR")
    bpy.context.scene.cursor.location = (0, 0, 0)

# landing gear
legs = []
for sx in (1, -1):
    for sy in (1, -1):
        leg = cyl(0.005, 0.11, (sx * 0.075, sy * 0.055, -0.075), rot=(sy * math.radians(14), 0, 0), v=16)
        finish(leg, M["carbon"]); legs.append(leg)
    skid = cyl(0.007, 0.27, (sx * 0.075, 0, -0.13), rot=(math.pi / 2, 0, 0), v=20); finish(skid, M["rubber"]); legs.append(skid)
gear = join(legs, "gear")

# gimbal camera under the front
yoke = box((0.05, 0.04, 0.024), (0, 0.105, -0.04)); finish(yoke, M["graphite"], bevel=0.006)
ball = None
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.03, location=(0, 0.112, -0.072), segments=48, ring_count=24)
ball = bpy.context.object; finish(ball, M["carbon"])
lens = cyl(0.015, 0.016, (0, 0.14, -0.072), rot=(math.pi / 2, 0, 0), v=40); finish(lens, M["glass"], bevel=0.003)
camera = join([yoke, ball, lens], "camera")

bpy.ops.object.select_all(action="DESELECT")
for o in bpy.data.objects:
    if o.type == "MESH":
        bpy.context.view_layer.objects.active = o
        o.select_set(True); apply_all(o); o.select_set(False)

os.makedirs(OUT, exist_ok=True)
bpy.ops.wm.save_as_mainfile(filepath=os.path.join(OUT, "drone.blend"))
bpy.ops.export_scene.gltf(filepath=os.path.join(OUT, "drone.glb"), export_format="GLB",
                          export_apply=True, export_yup=True, use_selection=False)
print("PARTS:", sorted(o.name for o in bpy.data.objects if o.type == "MESH"))
print("BUILD_OK")
