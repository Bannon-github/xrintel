# Joey Carlino — Getting started (low-poly scene)

Source: https://www.youtube.com/watch?v=uOmYInaX-wE
Channel: Joey Carlino. About 64 minutes.
Beginner playlist: https://youtube.com/playlist?list=PLzg4_2BrWAVwSyEgbgYGGflFefgtrmbay
Shortcut PDF linked from the panel: https://joeycarlino.gumroad.com/l/shortcuts

The information panel published the chapter map and the opening of the transcript. YouTube rate-limited the full caption file, so the middle steps follow that chapter map plus the tools the panel names. Confirm any shortcut against the in-app menu if a version differs.

Goal: install Blender, learn navigation and object tools, assemble a simple low-poly scene (flower, tree, cube island), then render.

## 1. Download (00:47)

1. Go to https://www.blender.org/download/ and take the newest version.
2. Optional version managers from the panel: Steam, or the Blender Launcher (https://github.com/Victor-IX/Blender-Launcher-V2).
3. Open Blender and dismiss the splash. Default scene: cube, light, camera.

## 2. Navigation (02:08)

1. Middle-mouse drag orbits. Scroll zooms. Shift + middle-mouse pans.
2. Top-right gizmos do the same with a click-drag: axis widget, magnifying glass, hand.
3. Practice until you can circle the cube without losing it. View → Frame Selected (numpad period) if you fly off.

## 3. Search instead of hunting (05:15)

1. Press F3. Type the tool name (Extrude, Shade Smooth, Subdivision).
2. Use this whenever a menu moved between versions.

## 4. Add and delete (05:59)

1. Select the cube. X → Delete, or right-click → Delete.
2. Add (Shift+A) → Mesh → pick Cube, UV Sphere, Cone, Cylinder.
3. New meshes appear at the 3D cursor. Place the cursor with Shift + right-click before adding, if you do not want the object at the world origin.

## 5. Shade smooth (07:01)

1. Right-click a round mesh → Shade Smooth.
2. This only changes shading. The mesh is still faceted. Pair it with subdivision later if you need a real smooth silhouette.

## 6. Move, rotate, scale (07:21)

1. G move, R rotate, S scale. Left-click confirms, right-click cancels.
2. After G, R, or S, press X, Y, or Z to lock an axis. Shift+X (or Y, Z) excludes that axis.
3. The left toolbar gizmos do the same without hotkeys.
4. Duplicate with Shift+D, then move the copy. Right-click cancels the move but keeps the duplicate where it was spawned; left-click places it.

## 7. Build the flower (09:30)

1. Add a thin cylinder or scaled cube for the stem. S then Z to stretch on height, S then Shift+Z to shrink the width.
2. Shift+D the petal mesh. R to rotate each copy around the stem.
3. Add a small UV sphere or cube at the center. G to seat it on the stem.
4. Select all flower parts, Object → Join (Ctrl+J) if you want one object. Skip join if you still need to edit parts.

## 8. Cube island and a simple tree (11:59, 13:50)

1. Add a cube. S to scale it into a ground slab. G then Z to sit it under the flower.
2. If a duplicated object rotates around the wrong point: Object → Set Origin → Origin to Geometry, or place the origin in the N-panel.
3. Tree: cube or cylinder trunk, scaled on Z. Duplicate and scale a cone or UV sphere for the canopy. G to stack it on the trunk.
4. Object → Clear → Location / Rotation / Scale if a transform went wrong. Alt+G, Alt+R, Alt+S are the shortcuts.

## 9. Side panels you will actually use (14:30)

1. N toggles the sidebar. Item tab shows location, rotation, scale numerically.
2. Scene properties → Units. Leave metres if the mesh will go to WebXR. A Blender metre should stay a metre.
3. Outliner (top-right list): rename objects (double-click). That name exports.
4. Eye icon hides. Camera icon disables render. Arrow disables selection.

## 10. Camera and render (15:52, 19:31)

1. View → Cameras → Active Camera, or numpad 0.
2. Sidebar View tab → Lock Camera to View, then orbit; the camera follows. Unlock when framed.
3. Render properties: Eevee for speed, Cycles for the final look (late chapter, about 01:03).
4. F12 renders. Image → Save As.

## 11. Materials (20:17)

1. Select an object. Material properties → New.
2. Base Color only. One material per part (stem, petal, ground, canopy) is enough.
3. If several objects share a look, use the material dropdown to pick an existing slot instead of New.

## 12. Origin point (21:51)

1. The orange dot is the origin. Rotate and scale happen around it.
2. A wrong origin makes a petal orbit the world center.
3. Object Mode: Object → Set Origin → Origin to Geometry, or Origin to 3D Cursor after placing the cursor where the pivot should be.

## 13. Final render

1. Frame the camera on the island.
2. Move the light off-axis so the tree casts a shadow on the slab.
3. F12. Save the image and File → Save the .blend.
