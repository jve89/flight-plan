#!/usr/bin/env python3
"""inspect_glb.py  -  list node names, materials, required extensions and size of a .glb.
Run after every export and every optimisation step: if parts were merged, you see it here.
    python3 inspect_glb.py model.glb
"""
import json, struct, sys, os
p = sys.argv[1]; b = open(p, "rb").read()
l = struct.unpack("<I", b[12:16])[0]; j = json.loads(b[20:20 + l])
print(f"{p}: {os.path.getsize(p)/1024:.0f} KB")
print("nodes     :", len(j.get("nodes", [])), sorted(n.get("name", "?") for n in j.get("nodes", [])))
print("meshes    :", len(j.get("meshes", [])), " (meshes with >1 primitive load as a Group in Three.js)")
multi = [m.get("name") for m in j.get("meshes", []) if len(m.get("primitives", [])) > 1]
if multi: print("  multi-material:", multi)
print("materials :", [m.get("name") for m in j.get("materials", [])])
print("extensions:", j.get("extensionsRequired", []))
