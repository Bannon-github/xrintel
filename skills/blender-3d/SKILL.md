---
name: blender-3d
description: "Guide beginner Blender 3D modeling from the xrintel lesson files. Use when asked to teach Blender, model a vase mug or donut, explain edit mode modifiers navigation or rendering, or produce step-by-step Blender instructions."
type: workflow
lifecycle: active
---

# Blender 3D — beginner instruction

Teach or execute a first Blender session from the three lesson files. Do not invent hotkeys. If a menu moved, say to press F3 and search the tool name.

Lesson files (xrintel repo):

- `research/youtube/steps/01-poole-absolute-beginners-vase.md` — vase, navigation, subsurf, material, render
- `research/youtube/steps/02-joey-carlino-getting-started.md` — low-poly scene, F3, origin, units, camera
- `research/youtube/steps/03-blender-guru-donut-part-1.md` — mug, solidify, loop cut, inset, versioned save

## Pick a lesson

| Ask | File |
|---|---|
| First hour, vase, few shortcuts | Poole |
| Low-poly scene, flower, tree, units for WebXR | Joey Carlino |
| Donut series, mug, modifiers | Blender Guru part 1 |

Read that file before answering. Quote steps, do not paste the video transcript.

## Session order

1. Confirm Blender is installed from blender.org. Version can be 4.x or 5.x for these tools.
2. Navigation before modeling: middle-mouse orbit, scroll zoom, Shift+middle-mouse pan, Frame Selected.
3. One primitive. Delete the default cube. Cylinder for vase or mug, torus for donut, cubes for the low-poly scene.
4. Edit Mode only on a selected mesh. Name vertices, edges, faces once.
5. Shape with move, scale, loop cut (Ctrl+R). Open a mug by deleting the top face only.
6. Modifiers stay unapplied: Subdivision Surface, Solidify for thickness. Viewport level 1-2.
7. Shade Smooth after subsurf. Loop cuts or inset near rims so subsurf does not melt edges. Avoid n-gons on those rims.
8. One Principled material, Base Color only. Move the light. Frame the camera. F12.
9. File → Save As with a trailing number (`name_01`). Numpad plus in the save dialog bumps it.

## WebXR export

1. Scene units in metres.
2. Apply scale (Ctrl+A → Scale) before glTF export. Do not apply subdivision unless the target needs the dense mesh; prefer a low cage plus a baked normal, or apply at render level 1.
3. Outliner names become glTF node names.
4. Lights and camera in the .blend are look-dev. Real-time XR relights the mesh.

## Common failures

| Symptom | Fix |
|---|---|
| Edit Mode missing | A light or camera is selected. Select the mesh. |
| Delete destroyed the rim | X → Faces, not Vertices. |
| Subsurf turned the cup into a blob | Ctrl+R near rim and base, or I inset on a single cap. |
| Rotate orbits the world | Object → Set Origin → Origin to Geometry. |
| Viewport frozen | Lower viewport subdivision. Keep render level higher. |
| Export scale wrong | Ctrl+A → Scale. Check metres. |
