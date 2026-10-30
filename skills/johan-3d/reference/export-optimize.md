# Export and optimise

## glTF-Transform (npm `@gltf-transform/cli`)
**`optimize` merges meshes by default**, which destroys named parts (the lab went from 18 parts to 4).
Always use:
```bash
gltf-transform optimize in.glb out.glb --compress meshopt --texture-compress false \
  --simplify false --join false --flatten false --instance false --palette false
```
Result in the lab: 553 KB → 98 KB, all 18 parts and 8 materials intact.
- `--instance false`: GPU instancing extensions are not supported by older loaders.
- `--palette false`: palette merging breaks material-name style swaps.
- Add `--texture-compress webp` (or ktx2 with a KTX2 loader) when the model has textures.

## Verify every time
`python3 scripts/inspect_glb.py out.glb` → node names, multi-material meshes, materials, required
extensions. Multi-material meshes load as a **Group** in Three.js (see `threejs.md`).

## Loader requirements
`EXT_meshopt_compression` needs `MeshoptDecoder`; `KHR_mesh_quantization` is supported by GLTFLoader.
