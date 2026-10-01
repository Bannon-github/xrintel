---
description: "Project-only Blender steps for the vase, low-poly scene, and donut-part-1 mug. Read when the user names one of those exercises."
---

# Projects

Shared navigation, modifiers, and export live in `SKILL.md`. These are the steps that differ.

## Vase (Poole)

Source: https://www.youtube.com/watch?v=Y0DthPSWjVk

1. Delete the cube. Add → Mesh → Cylinder.
2. Optional: drag a vase photo into the viewport as a reference.
3. Edit Mode. Loop Cut tool (or Ctrl+R) on the upper half and lower half.
4. Scale vertex rings (S) so the base puffs and the neck shrinks. Orbit while doing it.
5. Subdivision Surface, then Shade Smooth. Viewport level 1–2, higher render level.
6. Base Color, move the light, F12.

## Low-poly scene (Joey Carlino)

Source: https://www.youtube.com/watch?v=uOmYInaX-wE
Caption file was rate-limited; middle steps follow the published chapters.

1. Stem: cylinder, S then Z to stretch, S then Shift+Z to thin.
2. Petals: Shift+D, R around the stem. Small UV sphere at the center. Join with Ctrl+J only if you are done editing parts.
3. Ground: cube scaled into a slab, G then Z under the flower.
4. Tree: cylinder trunk, cone or UV sphere canopy, G to stack.
5. Alt+G / Alt+R / Alt+S clears a bad transform.
6. N-panel for numeric transforms. One Base Color per part. Eevee to preview, Cycles for the still.

## Mug, donut part 1 (Blender Guru)

Source: https://www.youtube.com/watch?v=-tbSCMbJA6o
Playlist: https://www.youtube.com/playlist?list=PLjEaoINr3zgGUwGwXlj9kBe7TrVWNjkyv

1. Cylinder, scaled short and wide. Shade Smooth.
2. Edit Mode, face select, click the top cap, X → Faces. That opens the cup. Vertices delete will destroy the rim.
3. Solidify for wall thickness. Flip the sign if the wall grows the wrong way.
4. Subdivision Surface. Ctrl+R near the rim and the base so the cup does not melt.
5. If the bottom is one n-gon and pinches, I to inset it, then subsurf again.
6. Object Mode. Shift+A → Torus. Place it beside the mug. Later videos finish the donut.
7. Save as `donut_01`, then bump the number before the next part.
