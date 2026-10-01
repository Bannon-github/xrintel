---
description: "Export a Blender mesh to glTF for WebXR. Read before File → Export → glTF 2.0."
connections: [hotkeys, projects]
---

# glTF export

Blender is Z-up. glTF is Y-up. The exporter converts this. Do not rotate the mesh 90 degrees by hand to "fix" it.

## Before the dialog

1. Scene properties → Units → metres. A Blender metre is a WebXR metre.
2. One object, or a parent empty with children. Apply scale on each mesh: select, Ctrl+A → Scale. Rotation can stay if the origin is intentional.
3. Object → Set Origin → Origin to Geometry, unless the prop must pivot elsewhere (a door hinges at the frame).
4. Outliner name is the node name. Use `vase`, not `Cylinder.001`.
5. Material is Principled BSDF. Base Color, Roughness, and Metallic export. Random node trees do not. Image textures must be saved files, not packed-only generates.
6. Subdivision Surface: leave it unapplied for a low cage. Apply it only if the runtime has no normal map and the silhouette must be smooth. Viewport level 2 is enough for a prop.
7. Hide the camera and light, or export selected objects only. They are not the XR lighting.

## Dialog

File → Export → glTF 2.0.

| Setting | Value |
|---|---|
| Format | glTF Binary (`.glb`) |
| Include | Selected Objects, unless the whole scene is the prop |
| Transform | +Y Up (default) |
| Data → Mesh | Apply Modifiers on, UVs on, Normals on |
| Data → Material | Export |
| Compression | Off for the first file. Draco breaks some viewers. |
| Animation | Off unless the user asked for a clip |

## After export

1. File size under a few megabytes for a first prop. A dense applied subsurf is the usual cause if it is not.
2. Reimport the `.glb` into Blender (File → Import → glTF) or drop it in a WebXR viewer. Check scale against the grid and that the base color survived.
3. If the mesh is tiny or huge, scale was not applied, or units were not metres. Fix the `.blend`, do not compensate in the viewer.
4. If it is black, the material was not Principled, or the texture path was missing at export.
