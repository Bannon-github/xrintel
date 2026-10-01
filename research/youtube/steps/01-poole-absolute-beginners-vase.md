# Poole — Blender for absolute beginners (vase)

Source: https://www.youtube.com/watch?v=Y0DthPSWjVk
Channel: Poole. About 36 minutes. Captions from the information panel, rewritten as steps.
Author script: https://docs.google.com/document/d/1k_8fguPPvTM4yeE5drhKpFX75Dyp3ZB0Bz3_Akv5mXY/edit

Goal: a cartoony vase (wide base, narrow neck), colored and rendered. No fringe tools.

## 0. What 3D actually is

1. Treat the mesh as taped-together polygons. A house is four wall faces and two roof faces. Blender only makes cutting, warping, and smoothing those faces easier.
2. You will not learn every feature. You will learn enough to build, color, and render simple objects.

## 1. Install and open

1. Download from https://www.blender.org/download/ (preferred). Steam works but needs a login.
2. Version does not matter for these steps. If the install is old, update.
3. Open Blender. Click off the splash. The scene has a cube, a light, and a camera in the 3D Viewport.
4. Drag the right-hand panel edges outward if they crowd the view. Leave the bottom editor; it is unused here.

## 2. Look around (about 02:56)

Gizmos, top-right of the viewport:

1. Drag the axis widget to orbit.
2. Drag the magnifying glass to zoom.
3. Drag the hand to pan.

Mouse:

1. Middle-mouse drag: orbit.
2. Scroll: zoom.
3. Shift + middle-mouse: pan.

Rebind if needed: Edit → Preferences → Keymap. Search Rotate View, Pan View, Zoom View. Save Preferences (bottom-left of that window).

Walk navigation (most natural for many people):

1. View → Navigation → Walk Navigation, or Shift + backtick (tilde, left of 1).
2. WASD or arrows to move. R and F for up and down. Mouse looks. Shift sprints.
3. Left-click to keep the new view. Right-click to cancel back.

Frame the selection:

1. Click an object. Orange outline means selected.
2. View → Frame Selected, or numpad period.
3. Rebind Frame Selected in the keymap if there is no numpad.

## 3. Start the vase (about 07:44)

1. Select the default cube. Right-click → Delete, or press X, or press Delete. Confirm if asked.
2. Add → Mesh → Cylinder. Non-mesh items (lights, cameras, empties) are not modeling primitives.
3. Optional reference: drag a vase photo from a browser into the viewport. It lands as a reference image.
4. With the cylinder selected, top-left mode menu: Object Mode → Edit Mode. Edit Mode is hidden if a light or camera is selected, because those are not meshes.
5. Names: points are vertices, lines are edges, filled quads are faces.
6. Left toolbar holds the edit tools. Hover a tool for its name.
7. Select a vertex. Use the move gizmo, or G, and drag. Left-click confirms. Right-click cancels.
8. Scale with the scale gizmo or S. Keep changes small.
9. Add loop cuts so the cylinder can pinch and bulge:
   - Select the Loop Cut tool on the left.
   - Hover the cylinder until a preview ring appears. Click to place it. Slide, then click to confirm.
   - Add loops on the upper half and lower half, not only the middle.
10. Select rings of vertices and scale them (S) to puff the base and shrink the neck. Orbit often so you are not editing a flat silhouette only.

## 4. Smooth it (about 15:12)

1. Do not hand-place hundreds of loops. Use a modifier.
2. With the vase selected, open the modifier tab (wrench). Add Modifier → Subdivision Surface.
3. It inserts loops between existing edges and places them so the form rounds. The Edit Mode cage stays the original points.
4. Viewport level and Render level are separate. Work at viewport level 1 or 2 so the scene stays fast. Raise the render level for the final image.
5. Too many levels freeze the viewport. That is expected; lower the viewport level.
6. Right-click the object → Shade Smooth. This fakes a smooth normal. The silhouette is still faceted until subdivision is high enough. Use both.

## 5. Materials and lighting (about 26:05)

1. Select the vase. Material properties (red sphere) → New.
2. Set Base Color. That is enough for this exercise.
3. Select the light. Move it (G or the move gizmo) and change power in the light properties (green bulb). Distance and strength change the read of the form more than a complex shader.
4. Keep the camera in frame. Numpad 0 is camera view if a numpad exists; otherwise use the camera gizmo or View → Cameras → Active Camera.

## 6. Render (about 31:18)

1. Render → Render Image, or F12.
2. The render uses the render subdivision level, so it can look smoother than the viewport.
3. Image → Save As to write the picture out.
4. File → Save the .blend before you close.

## 7. What to do next

1. Repeat the same cage-plus-subsurf pattern on other rotation shapes (cup, bottle, simple character limb).
2. Poole points at Blender Guru's donut playlist and a low-poly character tutorial once this vase feels easy.
