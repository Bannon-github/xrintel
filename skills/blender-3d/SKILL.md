---
name: blender-3d
description: "Run a first Blender session and export a WebXR-ready mesh. Use when teaching Blender, modeling a vase mug or low-poly prop, explaining edit mode modifiers or rendering, or preparing a glTF from Blender."
type: workflow
lifecycle: active
---

# Blender 3D — first asset

Produce one mesh a WebXR scene can load. Menu names drift; if a command is missing, press F3 and search it. Do not paste video transcripts.

Project-only steps: `references/projects.md`.

## Workflow

1. Install from https://www.blender.org/download/ if Blender is not open. Dismiss the splash. Default scene is a cube, a light, and a camera.
2. Navigate before modeling. Middle-mouse drag orbits, scroll zooms, Shift+middle-mouse pans. Top-right gizmos match those (axis, magnifying glass, hand). View → Frame Selected (numpad period) recovers a lost object. Walk mode: View → Navigation → Walk Navigation, or Shift+backtick; left-click keeps the view, right-click cancels.
3. Delete the cube (X). Add a mesh with Shift+A. New objects spawn at the 3D cursor (Shift+right-click to place it).
4. Tab into Edit Mode only with a mesh selected. Points are vertices, lines are edges, filled polygons are faces. 1/2/3 on the number row switch those modes. A selects all. Left-click confirms a transform, right-click cancels.
5. Shape with G, R, S. Press X, Y, or Z after the key to lock an axis; Shift+axis excludes it. Ctrl+R adds a loop cut. I insets a face. Shift+D duplicates.
6. Smooth without destroying the cage. Wrench tab → Subdivision Surface, viewport level 1 or 2. Right-click → Shade Smooth. Put loop cuts near any rim that must stay sharp. Do not Apply the modifier yet.
7. One material (red sphere tab → New → Base Color). Move the light. Numpad 0 or View → Cameras → Active Camera. Lock Camera to View in the N-panel View tab to frame. F12 renders. Image → Save As.
8. File → Save As with a trailing number (`prop_01`). Numpad plus in the save dialog bumps it. Do not overwrite the only copy.
9. Export only after the checks below.

## WebXR export

1. Scene properties → Units → metres.
2. Object → Set Origin → Origin to Geometry if rotate spins around the world.
3. Ctrl+A → Scale. Unapplied scale breaks modifiers and glTF.
4. Rename the object in the outliner. That name is the glTF node.
5. File → Export → glTF 2.0. Apply modifiers only if the runtime needs the dense mesh; otherwise keep the low cage. Blender lights and cameras are look-dev and do not ship as the XR lighting.

## Failures

| Symptom | Fix |
|---|---|
| No Edit Mode | A light or camera is selected |
| Rim deleted | X → Faces, not Vertices |
| Subsurf blob | Ctrl+R at rim and base, or I on a single cap |
| Frozen viewport | Lower viewport subdivision |
| Wrong size in XR | Metres, then Ctrl+A → Scale |
