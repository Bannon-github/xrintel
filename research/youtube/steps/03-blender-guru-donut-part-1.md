# Blender Guru — Donut tutorial part 1 (2026)

Source: https://www.youtube.com/watch?v=-tbSCMbJA6o
Channel: Blender Guru (Andrew Price). About 28 minutes. Blender 5.0 series.
Playlist: https://www.youtube.com/playlist?list=PLjEaoINr3zgGUwGwXlj9kBe7TrVWNjkyv
Shortcut guide: https://docs.google.com/document/d/1zPBgZAdftWa6WVa7UIFUqW_7EcqOYE0X743RqFuJL3o/edit

Goal of this part: install, navigate, shade smooth, build a coffee mug with modifiers, place a donut primitive, save a numbered .blend. The donut itself is finished in later parts.

## 1. Install (00:50)

1. Download from https://www.blender.org/download/.
2. Open and click off the splash.

## 2. Navigation (01:30)

1. Middle-mouse drag orbits. Scroll zooms. Shift + middle-mouse pans.
2. Numpad period frames the selected object. Use View → Frame Selected if there is no numpad.
3. Stay oriented before you model. Losing the object wastes more time than a slow orbit.

## 3. Add objects (06:02)

1. Select the default cube. X → Delete.
2. Shift+A → Mesh to add. This part uses a cylinder for the mug and a torus for the donut.
3. Objects spawn at the 3D cursor.

## 4. Shade smooth (09:32)

1. Select the mesh. Right-click → Shade Smooth.
2. Facets remain in the silhouette. Smooth shading only blends the normals.

## 5. Mug base (10:27)

1. Add → Mesh → Cylinder. This is the cup body, not the donut.
2. Scale it (S) into a short, wide cup. S then Z if you only want height.

## 6. Move tool (12:13)

1. Left toolbar: Move. Drag an arrow to stay on one axis, or drag the center to move free.
2. G is the same tool. X, Y, or Z after G locks the axis.
3. Left-click confirms. Right-click cancels.

## 7. Edit mode (15:42)

1. Tab, or the mode menu, into Edit Mode. The cylinder must be selected.
2. Header of the viewport: vertex, edge, and face select (1, 2, 3 on the number row, not the numpad).
3. A selects all. Alt+A or click empty space clears. B box-selects. C circle-selects.

## 8. Open the mug (17:57)

1. Face select. Click the top cap.
2. X → Faces. Only Faces, not Vertices or Edges, or you dissolve the ring.
3. You now have an open cylinder.

## 9. Modifiers, without applying (18:27)

1. Modifiers are non-destructive. The Edit Mode cage stays simple. The viewport shows the result.
2. Wrench tab → Add Modifier. Search by name if the menu moved.
3. Do not Apply yet. Applying bakes the result and you lose the live control.

## 10. Thickness — Solidify

1. Add Modifier → Solidify.
2. Thickness gives the wall. Negative thickness flips inside vs outside; flip if the wall grows the wrong way.
3. In Edit Mode you still edit the original skin. Solidify offsets every face.

## 11. Subdivision surface (20:40)

1. Add Modifier → Generate → Subdivision Surface. Search "subdivision" if it is buried.
2. The mug rounds and the rim softens. That is the modifier averaging neighboring points.
3. Levels Viewport 2 is plenty while working. An n-gon (face with more than 4 vertices) under subsurf pinches. Avoid them on the rim.

## 12. Loop cuts to hold the rim (22:43)

1. Ctrl+R. Hover a side face until a vertical or horizontal ring previews.
2. Click to set the cut, slide it toward the rim, click to confirm.
3. A second Ctrl+R near the base holds the bottom edge.
4. Menu path if the hotkey fails: Edge → Loop Cut and Slide.
5. Loop cut needs a ring of faces. It cannot cut a single isolated face.

## 13. Inset the bottom (24:31)

1. If the underside is one face and subsurf turns it into a star, inset it.
2. Face-select the bottom. I for Inset. Drag to set the border. Left-click confirms.
3. The new face loop gives subsurf a place to tighten, same job as a loop cut on a ring.

## 14. Donut placeholder

1. Object Mode. Shift+A → Mesh → Torus.
2. G and place it beside or above the mug. This part only starts the donut; later videos sculpt and shade it.
3. Numpad period to frame whichever object you are editing.

## 15. Save with a version number (27:11)

1. File → Save As, or Shift+Ctrl+S.
2. Name like `donut_01`. Do not overwrite the only copy.
3. In the save dialog, numpad plus/minus (or the plus/minus on the name field) bumps the trailing number. Save `donut_02` before a risky change.
4. Part 2 continues from this file.
