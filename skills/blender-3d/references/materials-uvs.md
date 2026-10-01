---
description: "Blender materials and UVs that survive glTF. Read when texturing, unwrapping, or a WebXR mesh looks black or flat."
connections: [gltf-export, projects, hotkeys]
---

# Materials and UVs

Procedural nodes do not export. If a texture must show in WebXR, it has to be an image on a Principled BSDF, and the mesh needs a UV map. Bake noise, voronoi, or color-ramp setups to an image before export. See [[gltf-export]].

## Material

1. Select the mesh. Material properties (red sphere) → New. The default is Principled BSDF. Keep it.
2. One slot is enough for a first prop. Name it (`vase_clay`), not `Material.001`.
3. Set Base Color, Roughness, and Metallic. Those three export. Roughness 0.4–0.6 reads as plastic or clay. Metallic 1 is metal; leave it at 0 for everything else.
4. Image texture: Base Color socket → Image Texture → Open a saved PNG or JPEG. Set Color Space to sRGB for color, Non-Color for roughness, metallic, and normal maps.
5. Normal map: Image Texture (Non-Color) → Normal Map node → Normal socket. Strength near 1. A purple-blue image is a tangent-space normal, not a height map.
6. Emission exports as emissive. Use it for screens and lamps, not as a substitute for a scene light.
7. Alpha: set the material Blend Mode / Alpha to blend or clip only if the texture has transparency. Opaque is the default and the cheapest in XR.
8. Second material: plus on the slot list, New, then Edit Mode, select faces, Assign. Unassigned faces keep slot 1.

Shade Smooth is not a material. It only changes vertex normals. A normal map still needs UVs.

## UV unwrap

1. The mesh needs a UV map before an image texture can stick. Default primitives already have one. Edited meshes often do not.
2. Edit Mode. A to select all. U → Unwrap. Smart UV Project is the safe first choice for a hard-surface prop (vase, mug). Angle limit 66, island margin 0.02.
3. Mark seams when Smart UV Project splits a face you need whole. Edge select the cut, Ctrl+E → Mark Seam. Seams go where a real object would have a join: under a vase, behind a mug handle, along the back of a character.
4. U → Unwrap (not Smart) after seams. Check the UV Editor. Islands should sit inside the 0–1 square and not overlap if they share one texture.
5. U → Cube Projection for crates and buildings. U → Project from View for a decal facing the camera.
6. Scale islands in the UV Editor (S) so important faces get more pixels. Do not scale a single face to the full square if the rest of the prop shares that image; they will fight.
7. Image size: 1024 for a small prop, 2048 if it fills the view. Power of two. Save the image next to the `.blend` before export.

## Checks before export

| Symptom | Fix |
|---|---|
| Color missing in the viewer | Texture was procedural, or the image was not saved |
| Texture smeared | No UV map, or islands overlap |
| Normal map looks wrong | Color space was sRGB; set Non-Color |
| Only one face textured | Faces were not Assigned to that material slot |
| Black mesh | No Principled BSDF, or the image path was missing at export |
