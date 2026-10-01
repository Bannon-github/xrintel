# Blender 3D instruction notes

Collected 2026-10-01 from a general YouTube search for 3D Blender instruction videos.

Source material is the public information panel on each video: title, channel, description, chapter markers, and the auto/manual transcript shown there. These notes are a structured extract for XR Intel reference (modeling vocabulary, viewport habits, and pipeline steps that transfer into WebXR asset work). They are not a verbatim republication of the spoken captions.

Official download: https://www.blender.org/download/

## Videos covered

1. **Blender for ABSOLUTE BEGINNERS.** — Poole (Nov 2025, ~36:44)
   - https://www.youtube.com/watch?v=Y0DthPSWjVk
   - Project: a simple vase, then color and render.
   - Author script (linked from the panel): https://docs.google.com/document/d/1k_8fguPPvTM4yeE5drhKpFX75Dyp3ZB0Bz3_Akv5mXY/edit
2. **Getting started — Blender for complete beginners** — Joey Carlino (Feb 2023, ~1:04:18)
   - https://www.youtube.com/watch?v=uOmYInaX-wE
   - Project: navigation plus a simple low-poly scene (flower, tree, cube island).
   - Beginner playlist: https://youtube.com/playlist?list=PLzg4_2BrWAVwSyEgbgYGGflFefgtrmbay
3. **Blender Donut Tutorial Part 1 (2026)** — Blender Guru / Andrew Price (Nov 2025, ~28:29)
   - https://www.youtube.com/watch?v=-tbSCMbJA6o
   - Playlist: https://www.youtube.com/playlist?list=PLjEaoINr3zgGUwGwXlj9kBe7TrVWNjkyv
   - Project: donut series opener; this part is install, navigation, a coffee mug, modifiers.
   - Shortcut guide linked from the panel: https://docs.google.com/document/d/1zPBgZAdftWa6WVa7UIFUqW_7EcqOYE0X743RqFuJL3o/edit

Related short reference also found in the same search: **Blender 3D — ULTIMATE 10 Minute Guide to Blender Basics** by 3DGreenhorn (https://www.youtube.com/watch?v=Be_9yovWwWA). Same core loop: navigate, select, add, edit-mode extrude/inset/bevel/loop cut, materials, lights, camera, render.

## Shared pipeline (all three)

1. Install from blender.org (Steam and the Blender Launcher are optional version managers; Poole prefers the site download so a login is not required).
2. Default scene is a cube, a light, and a camera inside the 3D Viewport.
3. Learn to look around before modeling.
4. Model in Edit Mode on polygon components (vertex, edge, face).
5. Use modifiers (especially Subdivision Surface) for smoothness without destroying the low-poly cage.
6. Assign materials, place lights, frame the camera, render.

Poole’s framing of the whole medium: everything is polygons. A house is four wall faces plus two roof faces; tools only make cutting, warping, and smoothing those faces easier than paper and tape.

## Navigation (from the panels)

Viewport gizmos (top-right of the 3D view):

- Axis widget: orbit.
- Magnifying glass: zoom.
- Hand: pan.
- These exist mainly so laptop users without a scroll wheel can still move.

Mouse defaults (Poole, 3DGreenhorn):

- Middle-mouse drag: orbit.
- Scroll: zoom.
- Shift + middle-mouse: pan.

Rebind under Edit → Preferences → Keymap. Search names Poole gives: Rotate View, Pan View, Zoom View, Frame Selected.

Walk navigation (Poole): View → Navigation → Walk Navigation, or Shift + backtick/tilde. WASD or arrows to move, R/F up and down, mouse to look, Shift to sprint, left-click to confirm, right-click to cancel. Useful when orbit feels unnatural.

Frame selected: View → Frame Selected, shortcut numpad period. Select the object (orange outline), then frame it.

Joey Carlino adds, from the chapter list: F3 search, N-panel, scene units, lock camera to view, outliner, origin point, and orthographic/view options.

## Modeling operations named in the transcripts

- Object Mode vs Edit Mode. Tab or the mode menu. Edit Mode exposes the mesh points.
- Add objects (Add menu / Shift+A). Delete with X.
- Move, rotate, scale. Gizmos or G / R / S. Axis lock (X/Y/Z, and Shift to exclude an axis) so a grab stays on one plane.
- Duplicate: Shift+D. Joey uses this for the flower; Blendy-style tutorials (also in the search) use Shift+D then Z to copy a base under a form.
- Selection modes: vertex, edge, face. A selects all.
- Shade Smooth (right-click or Object menu) so a faceted mesh reads as curved. Blender Guru covers this before the mug.
- Extrude, inset, bevel, loop cut and slide (Ctrl+R). 3DGreenhorn orders them that way in a 10-minute pass. Blender Guru uses inset on the mug and loop cuts to hold shape under subdivision.
- Delete a face to open a mesh (Guru: delete the top face so the mug has an opening).
- 3D cursor: new objects spawn at the cursor; snap/place it before adding.
- Origin point (Joey chapter): transforms pivot around the origin, so a wrong origin makes rotate/scale feel broken.
- Reset transform when a duplicated object carries a bad location/rotation/scale.

## Modifiers

Subdivision Surface is the shared “make it smooth” tool.

- Add it from the modifier stack (wrench).
- Levels around 2 are the usual starting point in the beginner panels.
- The control cage stays low-poly in Edit Mode until the modifier is applied. That is the point: edit eight or a few dozen points, preview a smooth surface.
- Loop cuts (Ctrl+R) pinch the surface so subdivision does not turn a mug or vase into a blob. Place them near edges you want to keep sharp (rim, base).
- Guru sequence in part 1: shade smooth → modifiers intro → subsurf → loop cuts → inset → thickness → save the .blend.

Other modifier named in the Joey chapter list: Array (repeat an object along a count/offset).

## Materials, light, camera, render

- Materials live on the material properties tab (red sphere). Principled-style base color is enough for a first vase or donut.
- Lighting: move the default light; distance and strength change the read of the form more than a fancy shader at this stage.
- Camera: position it, or lock the camera to the view so the viewport is what will render.
- Render from the Render menu or F12. Poole’s last teaching chapter is rendering, then “what’s next.”
- Joey’s late chapters cover Cycles vs the default engine and a final render.

## Chapter maps (information panel)

### Poole — vase in one sitting

- 00:00 Introduction to 3D
- 02:56 Looking around
- 07:44 Starting the model
- 15:12 Modifiers (making it smooth)
- 26:05 Materials and lighting
- 31:18 Rendering
- 33:11 What’s next

### Joey Carlino — first-session map

- 00:00 Start
- 00:47 Downloading Blender
- 02:08 Navigation
- 05:15 F3 search
- 05:59 Adding / deleting objects
- 07:01 Shade smooth
- 07:21 Move, rotate, scale
- 08:54 Duplicating
- 10:04 Axis locking
- 14:30 N panel
- 14:50 Units
- 15:52 Lock camera to view
- 16:06 Object mode
- 17:38 Outliner
- 19:31 Rendering
- 20:17 Materials
- 21:51 Origin point
- Later: Cycles, final render (~01:03:46)

### Blender Guru — Donut part 1 (2026 / Blender 5.0 tools)

- 00:00 Intro
- 00:50 Download and install
- 01:30 Navigation
- 06:02 Adding objects
- 09:32 Shade smooth
- 10:27 Coffee mug
- 12:13 Move tool
- 15:42 Edit mode
- 17:23 Select options
- 17:57 Delete face (mug opening)
- 18:27 Modifiers
- 20:40 Subdivision surface
- 22:43 Loop cuts
- 24:31 Inset
- 27:11 Save the project

The rest of that playlist is the usual Guru arc: editing, modifiers, modeling the donut, sculpting, rendering, texturing, then (in the older 3.0 series) geometry nodes, lighting, compositing, and animation. Older 3.0 playlist: https://www.youtube.com/playlist?list=PLjEaoINr3zgFX8ZsChQVQsuDSjEqdWMAD — panel note says to prefer the newer one.

## What transfers to XR Intel / WebXR

- Keep a low-poly cage and let a modifier or a later decimate/export step produce the mesh that actually ships. glTF viewers do not run Blender modifiers.
- Apply scale (Ctrl+A) before export or modifiers and physics will lie.
- Name objects in the outliner; that name becomes the node name in three.js / WebXR.
- Units: Joey’s units chapter matters because a Blender meter should stay a meter in XR.
- Camera and lights in Blender are look-dev only. Real-time XR relights the mesh; bake only what the target runtime cannot compute.
- First useful exercise matching these videos: a vase or mug (open top, subsurf, two loop cuts, one material), exported as glTF, dropped into a WebXR scene.

## Panel excerpts used as anchors (not full captions)

Poole, opening of the transcript panel: the vase is achievable with common modeling tools and few shortcuts; Blender is free; the lesson is build, color, render — not every feature.

Joey, opening: Blender is free and open source, used for modeling, 2D/3D animation, VFX, sculpting, and simulation; skills transfer to other 3D programs; download the newest build from blender.org, Steam, or the Blender launcher.

3DGreenhorn, opening: orbit with the left-mouse region, pan with the hand icon, zoom with the magnifying glass; then selection, add/delete, 3D cursor, duplicate, transform, edit mode.

Guru panel description: the series teaches Blender 5.0 core tools by making a donut; part 1 stops at save.
