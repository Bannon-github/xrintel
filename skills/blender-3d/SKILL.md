---
name: blender-3d
description: "Run a first Blender session and export a WebXR-ready mesh. Use when teaching Blender, modeling a prop, explaining edit mode modifiers materials or UVs, or preparing a glTF from Blender."
type: workflow
lifecycle: active
---

# Blender 3D — first asset

Produce one mesh a WebXR scene can load. Menu names drift; if a command is missing, press F3 and search it. No tutorial walkthroughs.

## Knowledge graph

Start at `references/INDEX.md` only if the task is not the workflow below.

- Shortcut asked: `references/hotkeys.md`
- Texture, unwrap, black or smeared mesh: `references/materials-uvs.md`
- Export or a huge glTF: `references/gltf-export.md`

## Workflow

1. Install from https://www.blender.org/download/ if Blender is not open. Dismiss the splash. Default scene is a cube, a light, and a camera.
2. Navigate before modeling. Middle-mouse drag orbits, scroll zooms, Shift+middle-mouse pans. View → Frame Selected (numpad period) recovers a lost object.
3. Delete the cube (X). Add a mesh with Shift+A. New objects spawn at the 3D cursor (Shift+right-click to place it).
4. Tab into Edit Mode only with a mesh selected. 1/2/3 on the number row select vertex, edge, face. Left-click confirms a transform, right-click cancels.
5. Shape with G, R, S. Axis lock is X, Y, or Z after the key. Ctrl+R loop-cuts. I insets. Shift+D duplicates. Full table: `references/hotkeys.md`.
6. Smooth without destroying the cage. Subdivision Surface, viewport level 1 or 2. Shade Smooth. Loop cuts near any rim that must stay sharp. Do not Apply yet.
7. Principled BSDF, Base Color. For an image texture, unwrap first (U → Smart UV Project), then follow `references/materials-uvs.md`. Procedural nodes do not export.
8. Move the light. Frame the camera. F12. Image → Save As.
9. File → Save As with a trailing number (`prop_01`). Do not overwrite the only copy.
10. Export with `references/gltf-export.md`. Metres, origin, Ctrl+A → Scale, outliner name, `.glb`, selected objects only.

## Failures

| Symptom | Fix |
|---|---|
| No Edit Mode | A light or camera is selected |
| Rim deleted | X → Faces, not Vertices |
| Subsurf blob | Ctrl+R at rim and base, or I on a single cap |
| Frozen viewport | Lower viewport subdivision |
| Wrong size in XR | Metres, then Ctrl+A → Scale. See `references/gltf-export.md` |
| Black or smeared mesh | No UV map, or the texture was procedural. See `references/materials-uvs.md` |
