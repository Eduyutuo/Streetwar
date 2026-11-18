# Guía de Prompts para Generación en Flow (7 Ángulos Canónicos)

Guía estructurada con prompts listos para copiar y pegar en herramientas de generación de imágenes (Flow, Midjourney, ComfyUI, FLUX).

## ⚙️ Configuración Recomendada en Flow

- **Relación de Aspecto (Aspect Ratio):** `1:1 (Square 1200x1200px / 1024x1024px)`
- **Muestreador (Sampler):** `Euler a / DPM++ 2M Karras`
- **Pasos (Steps):** `30`
- **CFG Scale:** `7.0`
- **Denoising Strength (Img2Img):** `0.45`
- **Image Weight (Referencia):** `1.8`
- **Consistencia de Semilla:** `Fixed Seed per product to maintain identical materials across all 7 angles`

### 🚫 Negative Prompt Común
```text
distorted logos, misspelled text, fake brand badges, asymmetrical deformed sole, warped eyelets, blurry laces, colored background, gradient background, shadows on walls, studio stands, human feet, legs, hands, mannequins, socks, dirty soles, worn leather, scuffs, lowres, oversaturated, chromatic aberration, cartoon, illustration, 3d render plastic sheen
```

---

## 👟 Catálogo de Modelos (45 Productos × 7 Ángulos)

### [00] IX6180-100 — Air Jordan 9 Retro OG "Space Jam"

**Foto de Referencia Primaria recomendada:** `dist/assets/2-norm-std/IX6180-100/01-lateral.webp`

#### Ángulo 1: Perfil Lateral Exterior (90°)
*Muestra silueta completa, logos principales y perfil de suela. Puntera a la izquierda.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 9 Retro OG "Space Jam", SKU: IX6180-100. Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole. Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 9 Retro OG "Space Jam", IX6180-100, 90° Lateral Exterior, Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole., Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 2: Perspectiva 3/4 Frontal (45°)
*Muestra volumen tridimensional, puntera y lateral exterior simultáneamente.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 9 Retro OG "Space Jam", SKU: IX6180-100. Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle. Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 9 Retro OG "Space Jam", IX6180-100, 3/4 Frontal Perspectiva, Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle., Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 3: Frontal Directa (0°)
*Muestra simetría de puntera, lengüeta, ancho de empeine y sistema de cordones.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 9 Retro OG "Space Jam", SKU: IX6180-100. Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker. Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 9 Retro OG "Space Jam", IX6180-100, Frontal Directa 0°, Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker., Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 4: Posterior / Talón (180°)
*Muestra contrafuerte del talón, logo de talón (Jumpman / Nike Air) y altura de caña.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 9 Retro OG "Space Jam", SKU: IX6180-100. Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level. Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 9 Retro OG "Space Jam", IX6180-100, Posterior Talón 180°, Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level., Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 5: Perspectiva 3/4 Trasera (135°)
*Muestra contorno del tobillo, talón tridimensional y curva posterior de entresuela.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 9 Retro OG "Space Jam", SKU: IX6180-100. Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front. Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 9 Retro OG "Space Jam", IX6180-100, 3/4 Trasera Exterior, Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front., Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 6: Perfil Lateral Interior / Medial (90°)
*Muestra el lado interno del pie, soporte del arco y patrón medial.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 9 Retro OG "Space Jam", SKU: IX6180-100. Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level. Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 9 Retro OG "Space Jam", IX6180-100, 90° Lateral Interior (Medial), Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level., Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 7: Cenital / Superior (90° Top-Down)
*Muestra vista plana superior completa: plantilla interior, cordones y lengüeta.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 9 Retro OG "Space Jam", SKU: IX6180-100. Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left. Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 9 Retro OG "Space Jam", IX6180-100, Cenital Superior 90°, Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left., Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

---

### [01] IO2076-100 — Air Jordan 3 Retro "Play Your Way"

**Foto de Referencia Primaria recomendada:** `dist/assets/2-norm-std/IO2076-100/01-lateral.webp`

#### Ángulo 1: Perfil Lateral Exterior (90°)
*Muestra silueta completa, logos principales y perfil de suela. Puntera a la izquierda.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 3 Retro "Play Your Way", SKU: IO2076-100. Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole. Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 3 Retro "Play Your Way", IO2076-100, 90° Lateral Exterior, Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole., Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 2: Perspectiva 3/4 Frontal (45°)
*Muestra volumen tridimensional, puntera y lateral exterior simultáneamente.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 3 Retro "Play Your Way", SKU: IO2076-100. Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle. Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 3 Retro "Play Your Way", IO2076-100, 3/4 Frontal Perspectiva, Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle., Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 3: Frontal Directa (0°)
*Muestra simetría de puntera, lengüeta, ancho de empeine y sistema de cordones.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 3 Retro "Play Your Way", SKU: IO2076-100. Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker. Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 3 Retro "Play Your Way", IO2076-100, Frontal Directa 0°, Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker., Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 4: Posterior / Talón (180°)
*Muestra contrafuerte del talón, logo de talón (Jumpman / Nike Air) y altura de caña.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 3 Retro "Play Your Way", SKU: IO2076-100. Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level. Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 3 Retro "Play Your Way", IO2076-100, Posterior Talón 180°, Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level., Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 5: Perspectiva 3/4 Trasera (135°)
*Muestra contorno del tobillo, talón tridimensional y curva posterior de entresuela.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 3 Retro "Play Your Way", SKU: IO2076-100. Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front. Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 3 Retro "Play Your Way", IO2076-100, 3/4 Trasera Exterior, Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front., Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 6: Perfil Lateral Interior / Medial (90°)
*Muestra el lado interno del pie, soporte del arco y patrón medial.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 3 Retro "Play Your Way", SKU: IO2076-100. Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level. Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 3 Retro "Play Your Way", IO2076-100, 90° Lateral Interior (Medial), Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level., Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 7: Cenital / Superior (90° Top-Down)
*Muestra vista plana superior completa: plantilla interior, cordones y lengüeta.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 3 Retro "Play Your Way", SKU: IO2076-100. Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left. Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 3 Retro "Play Your Way", IO2076-100, Cenital Superior 90°, Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left., Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

---

### [02] AQ9214-006 — Jordan Max Aura Black / Black / Gym Red

**Foto de Referencia Primaria recomendada:** `dist/assets/2-norm-std/AQ9214-006/01-lateral.webp`

#### Ángulo 1: Perfil Lateral Exterior (90°)
*Muestra silueta completa, logos principales y perfil de suela. Puntera a la izquierda.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Jordan Max Aura Black / Black / Gym Red, SKU: AQ9214-006. Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole. Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Jordan Max Aura Black / Black / Gym Red, AQ9214-006, 90° Lateral Exterior, Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole., Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 2: Perspectiva 3/4 Frontal (45°)
*Muestra volumen tridimensional, puntera y lateral exterior simultáneamente.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Jordan Max Aura Black / Black / Gym Red, SKU: AQ9214-006. Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle. Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Jordan Max Aura Black / Black / Gym Red, AQ9214-006, 3/4 Frontal Perspectiva, Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle., Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 3: Frontal Directa (0°)
*Muestra simetría de puntera, lengüeta, ancho de empeine y sistema de cordones.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Jordan Max Aura Black / Black / Gym Red, SKU: AQ9214-006. Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker. Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Jordan Max Aura Black / Black / Gym Red, AQ9214-006, Frontal Directa 0°, Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker., Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 4: Posterior / Talón (180°)
*Muestra contrafuerte del talón, logo de talón (Jumpman / Nike Air) y altura de caña.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Jordan Max Aura Black / Black / Gym Red, SKU: AQ9214-006. Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level. Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Jordan Max Aura Black / Black / Gym Red, AQ9214-006, Posterior Talón 180°, Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level., Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 5: Perspectiva 3/4 Trasera (135°)
*Muestra contorno del tobillo, talón tridimensional y curva posterior de entresuela.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Jordan Max Aura Black / Black / Gym Red, SKU: AQ9214-006. Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front. Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Jordan Max Aura Black / Black / Gym Red, AQ9214-006, 3/4 Trasera Exterior, Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front., Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 6: Perfil Lateral Interior / Medial (90°)
*Muestra el lado interno del pie, soporte del arco y patrón medial.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Jordan Max Aura Black / Black / Gym Red, SKU: AQ9214-006. Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level. Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Jordan Max Aura Black / Black / Gym Red, AQ9214-006, 90° Lateral Interior (Medial), Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level., Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 7: Cenital / Superior (90° Top-Down)
*Muestra vista plana superior completa: plantilla interior, cordones y lengüeta.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Jordan Max Aura Black / Black / Gym Red, SKU: AQ9214-006. Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left. Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Jordan Max Aura Black / Black / Gym Red, AQ9214-006, Cenital Superior 90°, Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left., Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

---

### [03] HF7054-012 — Nike Air Max 95 White / Pink / Brown

**Foto de Referencia Primaria recomendada:** `dist/assets/2-norm-std/HF7054-012/01-lateral.webp`

#### Ángulo 1: Perfil Lateral Exterior (90°)
*Muestra silueta completa, logos principales y perfil de suela. Puntera a la izquierda.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Max 95 White / Pink / Brown, SKU: HF7054-012. Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole. Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Max 95 White / Pink / Brown, HF7054-012, 90° Lateral Exterior, Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole., Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 2: Perspectiva 3/4 Frontal (45°)
*Muestra volumen tridimensional, puntera y lateral exterior simultáneamente.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Max 95 White / Pink / Brown, SKU: HF7054-012. Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle. Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Max 95 White / Pink / Brown, HF7054-012, 3/4 Frontal Perspectiva, Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle., Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 3: Frontal Directa (0°)
*Muestra simetría de puntera, lengüeta, ancho de empeine y sistema de cordones.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Max 95 White / Pink / Brown, SKU: HF7054-012. Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker. Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Max 95 White / Pink / Brown, HF7054-012, Frontal Directa 0°, Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker., Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 4: Posterior / Talón (180°)
*Muestra contrafuerte del talón, logo de talón (Jumpman / Nike Air) y altura de caña.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Max 95 White / Pink / Brown, SKU: HF7054-012. Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level. Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Max 95 White / Pink / Brown, HF7054-012, Posterior Talón 180°, Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level., Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 5: Perspectiva 3/4 Trasera (135°)
*Muestra contorno del tobillo, talón tridimensional y curva posterior de entresuela.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Max 95 White / Pink / Brown, SKU: HF7054-012. Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front. Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Max 95 White / Pink / Brown, HF7054-012, 3/4 Trasera Exterior, Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front., Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 6: Perfil Lateral Interior / Medial (90°)
*Muestra el lado interno del pie, soporte del arco y patrón medial.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Max 95 White / Pink / Brown, SKU: HF7054-012. Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level. Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Max 95 White / Pink / Brown, HF7054-012, 90° Lateral Interior (Medial), Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level., Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 7: Cenital / Superior (90° Top-Down)
*Muestra vista plana superior completa: plantilla interior, cordones y lengüeta.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Max 95 White / Pink / Brown, SKU: HF7054-012. Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left. Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Max 95 White / Pink / Brown, HF7054-012, Cenital Superior 90°, Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left., Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

---

### [04] BQ4212-002 — Nike Flight Legacy Black / White

**Foto de Referencia Primaria recomendada:** `dist/assets/2-norm-std/BQ4212-002/01-lateral.webp`

#### Ángulo 1: Perfil Lateral Exterior (90°)
*Muestra silueta completa, logos principales y perfil de suela. Puntera a la izquierda.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Flight Legacy Black / White, SKU: BQ4212-002. Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole. Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Flight Legacy Black / White, BQ4212-002, 90° Lateral Exterior, Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole., Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 2: Perspectiva 3/4 Frontal (45°)
*Muestra volumen tridimensional, puntera y lateral exterior simultáneamente.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Flight Legacy Black / White, SKU: BQ4212-002. Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle. Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Flight Legacy Black / White, BQ4212-002, 3/4 Frontal Perspectiva, Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle., Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 3: Frontal Directa (0°)
*Muestra simetría de puntera, lengüeta, ancho de empeine y sistema de cordones.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Flight Legacy Black / White, SKU: BQ4212-002. Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker. Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Flight Legacy Black / White, BQ4212-002, Frontal Directa 0°, Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker., Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 4: Posterior / Talón (180°)
*Muestra contrafuerte del talón, logo de talón (Jumpman / Nike Air) y altura de caña.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Flight Legacy Black / White, SKU: BQ4212-002. Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level. Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Flight Legacy Black / White, BQ4212-002, Posterior Talón 180°, Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level., Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 5: Perspectiva 3/4 Trasera (135°)
*Muestra contorno del tobillo, talón tridimensional y curva posterior de entresuela.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Flight Legacy Black / White, SKU: BQ4212-002. Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front. Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Flight Legacy Black / White, BQ4212-002, 3/4 Trasera Exterior, Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front., Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 6: Perfil Lateral Interior / Medial (90°)
*Muestra el lado interno del pie, soporte del arco y patrón medial.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Flight Legacy Black / White, SKU: BQ4212-002. Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level. Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Flight Legacy Black / White, BQ4212-002, 90° Lateral Interior (Medial), Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level., Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 7: Cenital / Superior (90° Top-Down)
*Muestra vista plana superior completa: plantilla interior, cordones y lengüeta.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Flight Legacy Black / White, SKU: BQ4212-002. Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left. Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Flight Legacy Black / White, BQ4212-002, Cenital Superior 90°, Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left., Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

---

### [05] 694862-200 — Nike Air Max Command Premium Light Taupe

**Foto de Referencia Primaria recomendada:** `dist/assets/2-norm-std/694862-200/01-lateral.webp`

#### Ángulo 1: Perfil Lateral Exterior (90°)
*Muestra silueta completa, logos principales y perfil de suela. Puntera a la izquierda.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Max Command Premium Light Taupe, SKU: 694862-200. Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole. Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Max Command Premium Light Taupe, 694862-200, 90° Lateral Exterior, Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole., Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 2: Perspectiva 3/4 Frontal (45°)
*Muestra volumen tridimensional, puntera y lateral exterior simultáneamente.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Max Command Premium Light Taupe, SKU: 694862-200. Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle. Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Max Command Premium Light Taupe, 694862-200, 3/4 Frontal Perspectiva, Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle., Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 3: Frontal Directa (0°)
*Muestra simetría de puntera, lengüeta, ancho de empeine y sistema de cordones.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Max Command Premium Light Taupe, SKU: 694862-200. Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker. Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Max Command Premium Light Taupe, 694862-200, Frontal Directa 0°, Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker., Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 4: Posterior / Talón (180°)
*Muestra contrafuerte del talón, logo de talón (Jumpman / Nike Air) y altura de caña.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Max Command Premium Light Taupe, SKU: 694862-200. Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level. Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Max Command Premium Light Taupe, 694862-200, Posterior Talón 180°, Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level., Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 5: Perspectiva 3/4 Trasera (135°)
*Muestra contorno del tobillo, talón tridimensional y curva posterior de entresuela.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Max Command Premium Light Taupe, SKU: 694862-200. Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front. Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Max Command Premium Light Taupe, 694862-200, 3/4 Trasera Exterior, Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front., Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 6: Perfil Lateral Interior / Medial (90°)
*Muestra el lado interno del pie, soporte del arco y patrón medial.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Max Command Premium Light Taupe, SKU: 694862-200. Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level. Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Max Command Premium Light Taupe, 694862-200, 90° Lateral Interior (Medial), Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level., Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 7: Cenital / Superior (90° Top-Down)
*Muestra vista plana superior completa: plantilla interior, cordones y lengüeta.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Max Command Premium Light Taupe, SKU: 694862-200. Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left. Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Max Command Premium Light Taupe, 694862-200, Cenital Superior 90°, Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left., Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

---

### [06] 511416-011 — Nike Air Max Correlate Black / White / Grey

**Foto de Referencia Primaria recomendada:** `dist/assets/2-norm-std/511416-011/01-lateral.webp`

#### Ángulo 1: Perfil Lateral Exterior (90°)
*Muestra silueta completa, logos principales y perfil de suela. Puntera a la izquierda.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Max Correlate Black / White / Grey, SKU: 511416-011. Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole. Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Max Correlate Black / White / Grey, 511416-011, 90° Lateral Exterior, Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole., Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 2: Perspectiva 3/4 Frontal (45°)
*Muestra volumen tridimensional, puntera y lateral exterior simultáneamente.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Max Correlate Black / White / Grey, SKU: 511416-011. Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle. Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Max Correlate Black / White / Grey, 511416-011, 3/4 Frontal Perspectiva, Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle., Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 3: Frontal Directa (0°)
*Muestra simetría de puntera, lengüeta, ancho de empeine y sistema de cordones.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Max Correlate Black / White / Grey, SKU: 511416-011. Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker. Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Max Correlate Black / White / Grey, 511416-011, Frontal Directa 0°, Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker., Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 4: Posterior / Talón (180°)
*Muestra contrafuerte del talón, logo de talón (Jumpman / Nike Air) y altura de caña.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Max Correlate Black / White / Grey, SKU: 511416-011. Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level. Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Max Correlate Black / White / Grey, 511416-011, Posterior Talón 180°, Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level., Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 5: Perspectiva 3/4 Trasera (135°)
*Muestra contorno del tobillo, talón tridimensional y curva posterior de entresuela.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Max Correlate Black / White / Grey, SKU: 511416-011. Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front. Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Max Correlate Black / White / Grey, 511416-011, 3/4 Trasera Exterior, Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front., Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 6: Perfil Lateral Interior / Medial (90°)
*Muestra el lado interno del pie, soporte del arco y patrón medial.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Max Correlate Black / White / Grey, SKU: 511416-011. Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level. Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Max Correlate Black / White / Grey, 511416-011, 90° Lateral Interior (Medial), Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level., Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 7: Cenital / Superior (90° Top-Down)
*Muestra vista plana superior completa: plantilla interior, cordones y lengüeta.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Max Correlate Black / White / Grey, SKU: 511416-011. Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left. Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Max Correlate Black / White / Grey, 511416-011, Cenital Superior 90°, Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left., Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

---

### [07] IR0519-101 — Jordan Son of Mars Low White / Red / Black

**Foto de Referencia Primaria recomendada:** `dist/assets/2-norm-std/IR0519-101/01-lateral.webp`

#### Ángulo 1: Perfil Lateral Exterior (90°)
*Muestra silueta completa, logos principales y perfil de suela. Puntera a la izquierda.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Jordan Son of Mars Low White / Red / Black, SKU: IR0519-101. Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole. Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Jordan Son of Mars Low White / Red / Black, IR0519-101, 90° Lateral Exterior, Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole., Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 2: Perspectiva 3/4 Frontal (45°)
*Muestra volumen tridimensional, puntera y lateral exterior simultáneamente.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Jordan Son of Mars Low White / Red / Black, SKU: IR0519-101. Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle. Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Jordan Son of Mars Low White / Red / Black, IR0519-101, 3/4 Frontal Perspectiva, Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle., Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 3: Frontal Directa (0°)
*Muestra simetría de puntera, lengüeta, ancho de empeine y sistema de cordones.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Jordan Son of Mars Low White / Red / Black, SKU: IR0519-101. Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker. Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Jordan Son of Mars Low White / Red / Black, IR0519-101, Frontal Directa 0°, Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker., Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 4: Posterior / Talón (180°)
*Muestra contrafuerte del talón, logo de talón (Jumpman / Nike Air) y altura de caña.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Jordan Son of Mars Low White / Red / Black, SKU: IR0519-101. Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level. Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Jordan Son of Mars Low White / Red / Black, IR0519-101, Posterior Talón 180°, Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level., Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 5: Perspectiva 3/4 Trasera (135°)
*Muestra contorno del tobillo, talón tridimensional y curva posterior de entresuela.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Jordan Son of Mars Low White / Red / Black, SKU: IR0519-101. Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front. Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Jordan Son of Mars Low White / Red / Black, IR0519-101, 3/4 Trasera Exterior, Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front., Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 6: Perfil Lateral Interior / Medial (90°)
*Muestra el lado interno del pie, soporte del arco y patrón medial.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Jordan Son of Mars Low White / Red / Black, SKU: IR0519-101. Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level. Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Jordan Son of Mars Low White / Red / Black, IR0519-101, 90° Lateral Interior (Medial), Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level., Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 7: Cenital / Superior (90° Top-Down)
*Muestra vista plana superior completa: plantilla interior, cordones y lengüeta.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Jordan Son of Mars Low White / Red / Black, SKU: IR0519-101. Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left. Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Jordan Son of Mars Low White / Red / Black, IR0519-101, Cenital Superior 90°, Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left., Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

---

### [08] IQ0205-100 — Nike Air Force 1 '07 Black / White / Orange Peel

**Foto de Referencia Primaria recomendada:** `dist/assets/2-norm-std/IQ0205-100/01-lateral.webp`

#### Ángulo 1: Perfil Lateral Exterior (90°)
*Muestra silueta completa, logos principales y perfil de suela. Puntera a la izquierda.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Force 1 '07 Black / White / Orange Peel, SKU: IQ0205-100. Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole. Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Force 1 '07 Black / White / Orange Peel, IQ0205-100, 90° Lateral Exterior, Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole., Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 2: Perspectiva 3/4 Frontal (45°)
*Muestra volumen tridimensional, puntera y lateral exterior simultáneamente.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Force 1 '07 Black / White / Orange Peel, SKU: IQ0205-100. Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle. Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Force 1 '07 Black / White / Orange Peel, IQ0205-100, 3/4 Frontal Perspectiva, Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle., Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 3: Frontal Directa (0°)
*Muestra simetría de puntera, lengüeta, ancho de empeine y sistema de cordones.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Force 1 '07 Black / White / Orange Peel, SKU: IQ0205-100. Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker. Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Force 1 '07 Black / White / Orange Peel, IQ0205-100, Frontal Directa 0°, Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker., Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 4: Posterior / Talón (180°)
*Muestra contrafuerte del talón, logo de talón (Jumpman / Nike Air) y altura de caña.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Force 1 '07 Black / White / Orange Peel, SKU: IQ0205-100. Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level. Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Force 1 '07 Black / White / Orange Peel, IQ0205-100, Posterior Talón 180°, Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level., Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 5: Perspectiva 3/4 Trasera (135°)
*Muestra contorno del tobillo, talón tridimensional y curva posterior de entresuela.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Force 1 '07 Black / White / Orange Peel, SKU: IQ0205-100. Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front. Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Force 1 '07 Black / White / Orange Peel, IQ0205-100, 3/4 Trasera Exterior, Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front., Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 6: Perfil Lateral Interior / Medial (90°)
*Muestra el lado interno del pie, soporte del arco y patrón medial.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Force 1 '07 Black / White / Orange Peel, SKU: IQ0205-100. Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level. Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Force 1 '07 Black / White / Orange Peel, IQ0205-100, 90° Lateral Interior (Medial), Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level., Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 7: Cenital / Superior (90° Top-Down)
*Muestra vista plana superior completa: plantilla interior, cordones y lengüeta.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Force 1 '07 Black / White / Orange Peel, SKU: IQ0205-100. Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left. Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Force 1 '07 Black / White / Orange Peel, IQ0205-100, Cenital Superior 90°, Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left., Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

---

### [09] IR1968-133 — Nike Air Force 1 '07 WNBA 30th Anniversary

**Foto de Referencia Primaria recomendada:** `dist/assets/2-norm-std/IR1968-133/01-lateral.webp`

#### Ángulo 1: Perfil Lateral Exterior (90°)
*Muestra silueta completa, logos principales y perfil de suela. Puntera a la izquierda.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Force 1 '07 WNBA 30th Anniversary, SKU: IR1968-133. Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole. Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Force 1 '07 WNBA 30th Anniversary, IR1968-133, 90° Lateral Exterior, Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole., Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 2: Perspectiva 3/4 Frontal (45°)
*Muestra volumen tridimensional, puntera y lateral exterior simultáneamente.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Force 1 '07 WNBA 30th Anniversary, SKU: IR1968-133. Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle. Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Force 1 '07 WNBA 30th Anniversary, IR1968-133, 3/4 Frontal Perspectiva, Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle., Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 3: Frontal Directa (0°)
*Muestra simetría de puntera, lengüeta, ancho de empeine y sistema de cordones.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Force 1 '07 WNBA 30th Anniversary, SKU: IR1968-133. Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker. Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Force 1 '07 WNBA 30th Anniversary, IR1968-133, Frontal Directa 0°, Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker., Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 4: Posterior / Talón (180°)
*Muestra contrafuerte del talón, logo de talón (Jumpman / Nike Air) y altura de caña.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Force 1 '07 WNBA 30th Anniversary, SKU: IR1968-133. Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level. Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Force 1 '07 WNBA 30th Anniversary, IR1968-133, Posterior Talón 180°, Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level., Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 5: Perspectiva 3/4 Trasera (135°)
*Muestra contorno del tobillo, talón tridimensional y curva posterior de entresuela.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Force 1 '07 WNBA 30th Anniversary, SKU: IR1968-133. Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front. Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Force 1 '07 WNBA 30th Anniversary, IR1968-133, 3/4 Trasera Exterior, Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front., Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 6: Perfil Lateral Interior / Medial (90°)
*Muestra el lado interno del pie, soporte del arco y patrón medial.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Force 1 '07 WNBA 30th Anniversary, SKU: IR1968-133. Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level. Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Force 1 '07 WNBA 30th Anniversary, IR1968-133, 90° Lateral Interior (Medial), Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level., Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 7: Cenital / Superior (90° Top-Down)
*Muestra vista plana superior completa: plantilla interior, cordones y lengüeta.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Force 1 '07 WNBA 30th Anniversary, SKU: IR1968-133. Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left. Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Force 1 '07 WNBA 30th Anniversary, IR1968-133, Cenital Superior 90°, Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left., Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

---

### [10] IR5896-030 — Nike Air Force 1 '07 LV8 "Mexico"

**Foto de Referencia Primaria recomendada:** `dist/assets/2-norm-std/IR5896-030/01-lateral.webp`

#### Ángulo 1: Perfil Lateral Exterior (90°)
*Muestra silueta completa, logos principales y perfil de suela. Puntera a la izquierda.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Force 1 '07 LV8 "Mexico", SKU: IR5896-030. Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole. Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Force 1 '07 LV8 "Mexico", IR5896-030, 90° Lateral Exterior, Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole., Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 2: Perspectiva 3/4 Frontal (45°)
*Muestra volumen tridimensional, puntera y lateral exterior simultáneamente.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Force 1 '07 LV8 "Mexico", SKU: IR5896-030. Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle. Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Force 1 '07 LV8 "Mexico", IR5896-030, 3/4 Frontal Perspectiva, Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle., Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 3: Frontal Directa (0°)
*Muestra simetría de puntera, lengüeta, ancho de empeine y sistema de cordones.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Force 1 '07 LV8 "Mexico", SKU: IR5896-030. Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker. Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Force 1 '07 LV8 "Mexico", IR5896-030, Frontal Directa 0°, Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker., Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 4: Posterior / Talón (180°)
*Muestra contrafuerte del talón, logo de talón (Jumpman / Nike Air) y altura de caña.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Force 1 '07 LV8 "Mexico", SKU: IR5896-030. Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level. Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Force 1 '07 LV8 "Mexico", IR5896-030, Posterior Talón 180°, Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level., Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 5: Perspectiva 3/4 Trasera (135°)
*Muestra contorno del tobillo, talón tridimensional y curva posterior de entresuela.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Force 1 '07 LV8 "Mexico", SKU: IR5896-030. Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front. Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Force 1 '07 LV8 "Mexico", IR5896-030, 3/4 Trasera Exterior, Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front., Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 6: Perfil Lateral Interior / Medial (90°)
*Muestra el lado interno del pie, soporte del arco y patrón medial.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Force 1 '07 LV8 "Mexico", SKU: IR5896-030. Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level. Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Force 1 '07 LV8 "Mexico", IR5896-030, 90° Lateral Interior (Medial), Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level., Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 7: Cenital / Superior (90° Top-Down)
*Muestra vista plana superior completa: plantilla interior, cordones y lengüeta.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Force 1 '07 LV8 "Mexico", SKU: IR5896-030. Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left. Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Force 1 '07 LV8 "Mexico", IR5896-030, Cenital Superior 90°, Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left., Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

---

### [11] IV6222-410 — Nike Air Griffey Max 1

**Foto de Referencia Primaria recomendada:** `dist/assets/2-norm-std/IV6222-410/01-lateral.webp`

#### Ángulo 1: Perfil Lateral Exterior (90°)
*Muestra silueta completa, logos principales y perfil de suela. Puntera a la izquierda.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Griffey Max 1, SKU: IV6222-410. Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole. Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Griffey Max 1, IV6222-410, 90° Lateral Exterior, Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole., Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 2: Perspectiva 3/4 Frontal (45°)
*Muestra volumen tridimensional, puntera y lateral exterior simultáneamente.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Griffey Max 1, SKU: IV6222-410. Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle. Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Griffey Max 1, IV6222-410, 3/4 Frontal Perspectiva, Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle., Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 3: Frontal Directa (0°)
*Muestra simetría de puntera, lengüeta, ancho de empeine y sistema de cordones.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Griffey Max 1, SKU: IV6222-410. Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker. Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Griffey Max 1, IV6222-410, Frontal Directa 0°, Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker., Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 4: Posterior / Talón (180°)
*Muestra contrafuerte del talón, logo de talón (Jumpman / Nike Air) y altura de caña.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Griffey Max 1, SKU: IV6222-410. Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level. Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Griffey Max 1, IV6222-410, Posterior Talón 180°, Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level., Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 5: Perspectiva 3/4 Trasera (135°)
*Muestra contorno del tobillo, talón tridimensional y curva posterior de entresuela.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Griffey Max 1, SKU: IV6222-410. Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front. Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Griffey Max 1, IV6222-410, 3/4 Trasera Exterior, Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front., Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 6: Perfil Lateral Interior / Medial (90°)
*Muestra el lado interno del pie, soporte del arco y patrón medial.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Griffey Max 1, SKU: IV6222-410. Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level. Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Griffey Max 1, IV6222-410, 90° Lateral Interior (Medial), Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level., Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 7: Cenital / Superior (90° Top-Down)
*Muestra vista plana superior completa: plantilla interior, cordones y lengüeta.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Griffey Max 1, SKU: IV6222-410. Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left. Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Griffey Max 1, IV6222-410, Cenital Superior 90°, Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left., Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

---

### [12] 553560-045 — Air Jordan 1 Low Summit White / Black

**Foto de Referencia Primaria recomendada:** `dist/assets/2-norm-std/553560-045/01-lateral.webp`

#### Ángulo 1: Perfil Lateral Exterior (90°)
*Muestra silueta completa, logos principales y perfil de suela. Puntera a la izquierda.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 1 Low Summit White / Black, SKU: 553560-045. Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole. Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 1 Low Summit White / Black, 553560-045, 90° Lateral Exterior, Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole., Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 2: Perspectiva 3/4 Frontal (45°)
*Muestra volumen tridimensional, puntera y lateral exterior simultáneamente.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 1 Low Summit White / Black, SKU: 553560-045. Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle. Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 1 Low Summit White / Black, 553560-045, 3/4 Frontal Perspectiva, Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle., Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 3: Frontal Directa (0°)
*Muestra simetría de puntera, lengüeta, ancho de empeine y sistema de cordones.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 1 Low Summit White / Black, SKU: 553560-045. Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker. Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 1 Low Summit White / Black, 553560-045, Frontal Directa 0°, Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker., Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 4: Posterior / Talón (180°)
*Muestra contrafuerte del talón, logo de talón (Jumpman / Nike Air) y altura de caña.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 1 Low Summit White / Black, SKU: 553560-045. Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level. Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 1 Low Summit White / Black, 553560-045, Posterior Talón 180°, Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level., Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 5: Perspectiva 3/4 Trasera (135°)
*Muestra contorno del tobillo, talón tridimensional y curva posterior de entresuela.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 1 Low Summit White / Black, SKU: 553560-045. Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front. Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 1 Low Summit White / Black, 553560-045, 3/4 Trasera Exterior, Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front., Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 6: Perfil Lateral Interior / Medial (90°)
*Muestra el lado interno del pie, soporte del arco y patrón medial.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 1 Low Summit White / Black, SKU: 553560-045. Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level. Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 1 Low Summit White / Black, 553560-045, 90° Lateral Interior (Medial), Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level., Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 7: Cenital / Superior (90° Top-Down)
*Muestra vista plana superior completa: plantilla interior, cordones y lengüeta.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 1 Low Summit White / Black, SKU: 553560-045. Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left. Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 1 Low Summit White / Black, 553560-045, Cenital Superior 90°, Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left., Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

---

### [13] CT3839-100 — Nike Air Force 1 Blanco / Negro

**Foto de Referencia Primaria recomendada:** `dist/assets/2-norm-std/CT3839-100/01-lateral.webp`

#### Ángulo 1: Perfil Lateral Exterior (90°)
*Muestra silueta completa, logos principales y perfil de suela. Puntera a la izquierda.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Force 1 Blanco / Negro, SKU: CT3839-100. Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole. Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Force 1 Blanco / Negro, CT3839-100, 90° Lateral Exterior, Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole., Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 2: Perspectiva 3/4 Frontal (45°)
*Muestra volumen tridimensional, puntera y lateral exterior simultáneamente.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Force 1 Blanco / Negro, SKU: CT3839-100. Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle. Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Force 1 Blanco / Negro, CT3839-100, 3/4 Frontal Perspectiva, Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle., Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 3: Frontal Directa (0°)
*Muestra simetría de puntera, lengüeta, ancho de empeine y sistema de cordones.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Force 1 Blanco / Negro, SKU: CT3839-100. Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker. Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Force 1 Blanco / Negro, CT3839-100, Frontal Directa 0°, Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker., Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 4: Posterior / Talón (180°)
*Muestra contrafuerte del talón, logo de talón (Jumpman / Nike Air) y altura de caña.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Force 1 Blanco / Negro, SKU: CT3839-100. Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level. Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Force 1 Blanco / Negro, CT3839-100, Posterior Talón 180°, Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level., Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 5: Perspectiva 3/4 Trasera (135°)
*Muestra contorno del tobillo, talón tridimensional y curva posterior de entresuela.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Force 1 Blanco / Negro, SKU: CT3839-100. Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front. Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Force 1 Blanco / Negro, CT3839-100, 3/4 Trasera Exterior, Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front., Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 6: Perfil Lateral Interior / Medial (90°)
*Muestra el lado interno del pie, soporte del arco y patrón medial.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Force 1 Blanco / Negro, SKU: CT3839-100. Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level. Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Force 1 Blanco / Negro, CT3839-100, 90° Lateral Interior (Medial), Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level., Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 7: Cenital / Superior (90° Top-Down)
*Muestra vista plana superior completa: plantilla interior, cordones y lengüeta.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Force 1 Blanco / Negro, SKU: CT3839-100. Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left. Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Force 1 Blanco / Negro, CT3839-100, Cenital Superior 90°, Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left., Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

---

### [14] IW2872-700 — Air Jordan 4 x J Balvin "Amazonas"

**Foto de Referencia Primaria recomendada:** `dist/assets/2-norm-std/IW2872-700/01-lateral.webp`

#### Ángulo 1: Perfil Lateral Exterior (90°)
*Muestra silueta completa, logos principales y perfil de suela. Puntera a la izquierda.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 4 x J Balvin "Amazonas", SKU: IW2872-700. Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole. Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 4 x J Balvin "Amazonas", IW2872-700, 90° Lateral Exterior, Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole., Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 2: Perspectiva 3/4 Frontal (45°)
*Muestra volumen tridimensional, puntera y lateral exterior simultáneamente.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 4 x J Balvin "Amazonas", SKU: IW2872-700. Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle. Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 4 x J Balvin "Amazonas", IW2872-700, 3/4 Frontal Perspectiva, Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle., Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 3: Frontal Directa (0°)
*Muestra simetría de puntera, lengüeta, ancho de empeine y sistema de cordones.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 4 x J Balvin "Amazonas", SKU: IW2872-700. Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker. Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 4 x J Balvin "Amazonas", IW2872-700, Frontal Directa 0°, Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker., Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 4: Posterior / Talón (180°)
*Muestra contrafuerte del talón, logo de talón (Jumpman / Nike Air) y altura de caña.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 4 x J Balvin "Amazonas", SKU: IW2872-700. Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level. Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 4 x J Balvin "Amazonas", IW2872-700, Posterior Talón 180°, Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level., Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 5: Perspectiva 3/4 Trasera (135°)
*Muestra contorno del tobillo, talón tridimensional y curva posterior de entresuela.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 4 x J Balvin "Amazonas", SKU: IW2872-700. Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front. Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 4 x J Balvin "Amazonas", IW2872-700, 3/4 Trasera Exterior, Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front., Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 6: Perfil Lateral Interior / Medial (90°)
*Muestra el lado interno del pie, soporte del arco y patrón medial.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 4 x J Balvin "Amazonas", SKU: IW2872-700. Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level. Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 4 x J Balvin "Amazonas", IW2872-700, 90° Lateral Interior (Medial), Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level., Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 7: Cenital / Superior (90° Top-Down)
*Muestra vista plana superior completa: plantilla interior, cordones y lengüeta.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 4 x J Balvin "Amazonas", SKU: IW2872-700. Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left. Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 4 x J Balvin "Amazonas", IW2872-700, Cenital Superior 90°, Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left., Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

---

### [15] FD1437-008 — Air Jordan 1 High OG "Shattered Backboard"

**Foto de Referencia Primaria recomendada:** `dist/assets/2-norm-std/FD1437-008/01-lateral.webp`

#### Ángulo 1: Perfil Lateral Exterior (90°)
*Muestra silueta completa, logos principales y perfil de suela. Puntera a la izquierda.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 1 High OG "Shattered Backboard", SKU: FD1437-008. Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole. Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 1 High OG "Shattered Backboard", FD1437-008, 90° Lateral Exterior, Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole., Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 2: Perspectiva 3/4 Frontal (45°)
*Muestra volumen tridimensional, puntera y lateral exterior simultáneamente.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 1 High OG "Shattered Backboard", SKU: FD1437-008. Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle. Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 1 High OG "Shattered Backboard", FD1437-008, 3/4 Frontal Perspectiva, Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle., Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 3: Frontal Directa (0°)
*Muestra simetría de puntera, lengüeta, ancho de empeine y sistema de cordones.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 1 High OG "Shattered Backboard", SKU: FD1437-008. Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker. Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 1 High OG "Shattered Backboard", FD1437-008, Frontal Directa 0°, Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker., Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 4: Posterior / Talón (180°)
*Muestra contrafuerte del talón, logo de talón (Jumpman / Nike Air) y altura de caña.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 1 High OG "Shattered Backboard", SKU: FD1437-008. Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level. Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 1 High OG "Shattered Backboard", FD1437-008, Posterior Talón 180°, Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level., Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 5: Perspectiva 3/4 Trasera (135°)
*Muestra contorno del tobillo, talón tridimensional y curva posterior de entresuela.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 1 High OG "Shattered Backboard", SKU: FD1437-008. Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front. Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 1 High OG "Shattered Backboard", FD1437-008, 3/4 Trasera Exterior, Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front., Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 6: Perfil Lateral Interior / Medial (90°)
*Muestra el lado interno del pie, soporte del arco y patrón medial.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 1 High OG "Shattered Backboard", SKU: FD1437-008. Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level. Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 1 High OG "Shattered Backboard", FD1437-008, 90° Lateral Interior (Medial), Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level., Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 7: Cenital / Superior (90° Top-Down)
*Muestra vista plana superior completa: plantilla interior, cordones y lengüeta.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 1 High OG "Shattered Backboard", SKU: FD1437-008. Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left. Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 1 High OG "Shattered Backboard", FD1437-008, Cenital Superior 90°, Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left., Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

---

### [16] 408452-102 — Air Jordan 4 Retro "Tour Yellow"

**Foto de Referencia Primaria recomendada:** `dist/assets/2-norm-std/408452-102/01-lateral.webp`

#### Ángulo 1: Perfil Lateral Exterior (90°)
*Muestra silueta completa, logos principales y perfil de suela. Puntera a la izquierda.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 4 Retro "Tour Yellow", SKU: 408452-102. Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole. Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 4 Retro "Tour Yellow", 408452-102, 90° Lateral Exterior, Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole., Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 2: Perspectiva 3/4 Frontal (45°)
*Muestra volumen tridimensional, puntera y lateral exterior simultáneamente.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 4 Retro "Tour Yellow", SKU: 408452-102. Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle. Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 4 Retro "Tour Yellow", 408452-102, 3/4 Frontal Perspectiva, Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle., Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 3: Frontal Directa (0°)
*Muestra simetría de puntera, lengüeta, ancho de empeine y sistema de cordones.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 4 Retro "Tour Yellow", SKU: 408452-102. Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker. Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 4 Retro "Tour Yellow", 408452-102, Frontal Directa 0°, Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker., Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 4: Posterior / Talón (180°)
*Muestra contrafuerte del talón, logo de talón (Jumpman / Nike Air) y altura de caña.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 4 Retro "Tour Yellow", SKU: 408452-102. Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level. Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 4 Retro "Tour Yellow", 408452-102, Posterior Talón 180°, Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level., Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 5: Perspectiva 3/4 Trasera (135°)
*Muestra contorno del tobillo, talón tridimensional y curva posterior de entresuela.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 4 Retro "Tour Yellow", SKU: 408452-102. Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front. Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 4 Retro "Tour Yellow", 408452-102, 3/4 Trasera Exterior, Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front., Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 6: Perfil Lateral Interior / Medial (90°)
*Muestra el lado interno del pie, soporte del arco y patrón medial.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 4 Retro "Tour Yellow", SKU: 408452-102. Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level. Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 4 Retro "Tour Yellow", 408452-102, 90° Lateral Interior (Medial), Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level., Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 7: Cenital / Superior (90° Top-Down)
*Muestra vista plana superior completa: plantilla interior, cordones y lengüeta.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 4 Retro "Tour Yellow", SKU: 408452-102. Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left. Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 4 Retro "Tour Yellow", 408452-102, Cenital Superior 90°, Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left., Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

---

### [17] AQ9214-011 — Jordan Max Aura Black / White

**Foto de Referencia Primaria recomendada:** `dist/assets/2-norm-std/AQ9214-011/01-lateral.webp`

#### Ángulo 1: Perfil Lateral Exterior (90°)
*Muestra silueta completa, logos principales y perfil de suela. Puntera a la izquierda.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Jordan Max Aura Black / White, SKU: AQ9214-011. Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole. Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Jordan Max Aura Black / White, AQ9214-011, 90° Lateral Exterior, Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole., Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 2: Perspectiva 3/4 Frontal (45°)
*Muestra volumen tridimensional, puntera y lateral exterior simultáneamente.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Jordan Max Aura Black / White, SKU: AQ9214-011. Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle. Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Jordan Max Aura Black / White, AQ9214-011, 3/4 Frontal Perspectiva, Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle., Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 3: Frontal Directa (0°)
*Muestra simetría de puntera, lengüeta, ancho de empeine y sistema de cordones.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Jordan Max Aura Black / White, SKU: AQ9214-011. Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker. Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Jordan Max Aura Black / White, AQ9214-011, Frontal Directa 0°, Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker., Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 4: Posterior / Talón (180°)
*Muestra contrafuerte del talón, logo de talón (Jumpman / Nike Air) y altura de caña.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Jordan Max Aura Black / White, SKU: AQ9214-011. Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level. Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Jordan Max Aura Black / White, AQ9214-011, Posterior Talón 180°, Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level., Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 5: Perspectiva 3/4 Trasera (135°)
*Muestra contorno del tobillo, talón tridimensional y curva posterior de entresuela.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Jordan Max Aura Black / White, SKU: AQ9214-011. Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front. Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Jordan Max Aura Black / White, AQ9214-011, 3/4 Trasera Exterior, Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front., Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 6: Perfil Lateral Interior / Medial (90°)
*Muestra el lado interno del pie, soporte del arco y patrón medial.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Jordan Max Aura Black / White, SKU: AQ9214-011. Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level. Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Jordan Max Aura Black / White, AQ9214-011, 90° Lateral Interior (Medial), Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level., Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 7: Cenital / Superior (90° Top-Down)
*Muestra vista plana superior completa: plantilla interior, cordones y lengüeta.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Jordan Max Aura Black / White, SKU: AQ9214-011. Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left. Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Jordan Max Aura Black / White, AQ9214-011, Cenital Superior 90°, Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left., Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

---

### [18] II1254-001 — Air Jordan 1 Mid SE Black / Gold / Pink

**Foto de Referencia Primaria recomendada:** `dist/assets/2-norm-std/II1254-001/01-lateral.webp`

#### Ángulo 1: Perfil Lateral Exterior (90°)
*Muestra silueta completa, logos principales y perfil de suela. Puntera a la izquierda.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 1 Mid SE Black / Gold / Pink, SKU: II1254-001. Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole. Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 1 Mid SE Black / Gold / Pink, II1254-001, 90° Lateral Exterior, Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole., Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 2: Perspectiva 3/4 Frontal (45°)
*Muestra volumen tridimensional, puntera y lateral exterior simultáneamente.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 1 Mid SE Black / Gold / Pink, SKU: II1254-001. Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle. Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 1 Mid SE Black / Gold / Pink, II1254-001, 3/4 Frontal Perspectiva, Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle., Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 3: Frontal Directa (0°)
*Muestra simetría de puntera, lengüeta, ancho de empeine y sistema de cordones.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 1 Mid SE Black / Gold / Pink, SKU: II1254-001. Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker. Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 1 Mid SE Black / Gold / Pink, II1254-001, Frontal Directa 0°, Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker., Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 4: Posterior / Talón (180°)
*Muestra contrafuerte del talón, logo de talón (Jumpman / Nike Air) y altura de caña.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 1 Mid SE Black / Gold / Pink, SKU: II1254-001. Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level. Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 1 Mid SE Black / Gold / Pink, II1254-001, Posterior Talón 180°, Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level., Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 5: Perspectiva 3/4 Trasera (135°)
*Muestra contorno del tobillo, talón tridimensional y curva posterior de entresuela.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 1 Mid SE Black / Gold / Pink, SKU: II1254-001. Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front. Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 1 Mid SE Black / Gold / Pink, II1254-001, 3/4 Trasera Exterior, Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front., Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 6: Perfil Lateral Interior / Medial (90°)
*Muestra el lado interno del pie, soporte del arco y patrón medial.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 1 Mid SE Black / Gold / Pink, SKU: II1254-001. Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level. Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 1 Mid SE Black / Gold / Pink, II1254-001, 90° Lateral Interior (Medial), Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level., Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 7: Cenital / Superior (90° Top-Down)
*Muestra vista plana superior completa: plantilla interior, cordones y lengüeta.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 1 Mid SE Black / Gold / Pink, SKU: II1254-001. Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left. Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 1 Mid SE Black / Gold / Pink, II1254-001, Cenital Superior 90°, Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left., Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

---

### [19] II0599-600 — Air Jordan 3 Retro GS "Spring Flowers"

**Foto de Referencia Primaria recomendada:** `dist/assets/2-norm-std/II0599-600/01-lateral.webp`

#### Ángulo 1: Perfil Lateral Exterior (90°)
*Muestra silueta completa, logos principales y perfil de suela. Puntera a la izquierda.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 3 Retro GS "Spring Flowers", SKU: II0599-600. Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole. Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 3 Retro GS "Spring Flowers", II0599-600, 90° Lateral Exterior, Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole., Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 2: Perspectiva 3/4 Frontal (45°)
*Muestra volumen tridimensional, puntera y lateral exterior simultáneamente.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 3 Retro GS "Spring Flowers", SKU: II0599-600. Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle. Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 3 Retro GS "Spring Flowers", II0599-600, 3/4 Frontal Perspectiva, Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle., Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 3: Frontal Directa (0°)
*Muestra simetría de puntera, lengüeta, ancho de empeine y sistema de cordones.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 3 Retro GS "Spring Flowers", SKU: II0599-600. Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker. Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 3 Retro GS "Spring Flowers", II0599-600, Frontal Directa 0°, Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker., Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 4: Posterior / Talón (180°)
*Muestra contrafuerte del talón, logo de talón (Jumpman / Nike Air) y altura de caña.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 3 Retro GS "Spring Flowers", SKU: II0599-600. Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level. Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 3 Retro GS "Spring Flowers", II0599-600, Posterior Talón 180°, Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level., Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 5: Perspectiva 3/4 Trasera (135°)
*Muestra contorno del tobillo, talón tridimensional y curva posterior de entresuela.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 3 Retro GS "Spring Flowers", SKU: II0599-600. Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front. Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 3 Retro GS "Spring Flowers", II0599-600, 3/4 Trasera Exterior, Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front., Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 6: Perfil Lateral Interior / Medial (90°)
*Muestra el lado interno del pie, soporte del arco y patrón medial.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 3 Retro GS "Spring Flowers", SKU: II0599-600. Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level. Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 3 Retro GS "Spring Flowers", II0599-600, 90° Lateral Interior (Medial), Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level., Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 7: Cenital / Superior (90° Top-Down)
*Muestra vista plana superior completa: plantilla interior, cordones y lengüeta.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 3 Retro GS "Spring Flowers", SKU: II0599-600. Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left. Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 3 Retro GS "Spring Flowers", II0599-600, Cenital Superior 90°, Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left., Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

---

### [20] 511417-136 — Nike Air Max Correlate White / New Green / Bright Mango / Black

**Foto de Referencia Primaria recomendada:** `dist/assets/2-norm-std/511417-136/01-lateral.webp`

#### Ángulo 1: Perfil Lateral Exterior (90°)
*Muestra silueta completa, logos principales y perfil de suela. Puntera a la izquierda.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Max Correlate White / New Green / Bright Mango / Black, SKU: 511417-136. Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole. Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Max Correlate White / New Green / Bright Mango / Black, 511417-136, 90° Lateral Exterior, Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole., Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 2: Perspectiva 3/4 Frontal (45°)
*Muestra volumen tridimensional, puntera y lateral exterior simultáneamente.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Max Correlate White / New Green / Bright Mango / Black, SKU: 511417-136. Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle. Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Max Correlate White / New Green / Bright Mango / Black, 511417-136, 3/4 Frontal Perspectiva, Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle., Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 3: Frontal Directa (0°)
*Muestra simetría de puntera, lengüeta, ancho de empeine y sistema de cordones.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Max Correlate White / New Green / Bright Mango / Black, SKU: 511417-136. Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker. Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Max Correlate White / New Green / Bright Mango / Black, 511417-136, Frontal Directa 0°, Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker., Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 4: Posterior / Talón (180°)
*Muestra contrafuerte del talón, logo de talón (Jumpman / Nike Air) y altura de caña.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Max Correlate White / New Green / Bright Mango / Black, SKU: 511417-136. Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level. Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Max Correlate White / New Green / Bright Mango / Black, 511417-136, Posterior Talón 180°, Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level., Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 5: Perspectiva 3/4 Trasera (135°)
*Muestra contorno del tobillo, talón tridimensional y curva posterior de entresuela.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Max Correlate White / New Green / Bright Mango / Black, SKU: 511417-136. Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front. Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Max Correlate White / New Green / Bright Mango / Black, 511417-136, 3/4 Trasera Exterior, Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front., Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 6: Perfil Lateral Interior / Medial (90°)
*Muestra el lado interno del pie, soporte del arco y patrón medial.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Max Correlate White / New Green / Bright Mango / Black, SKU: 511417-136. Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level. Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Max Correlate White / New Green / Bright Mango / Black, 511417-136, 90° Lateral Interior (Medial), Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level., Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 7: Cenital / Superior (90° Top-Down)
*Muestra vista plana superior completa: plantilla interior, cordones y lengüeta.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Max Correlate White / New Green / Bright Mango / Black, SKU: 511417-136. Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left. Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Max Correlate White / New Green / Bright Mango / Black, 511417-136, Cenital Superior 90°, Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left., Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

---

### [21] 323419-164 — Jordan 6 Rings White / University Red / Black

**Foto de Referencia Primaria recomendada:** `dist/assets/2-norm-std/323419-164/01-lateral.webp`

#### Ángulo 1: Perfil Lateral Exterior (90°)
*Muestra silueta completa, logos principales y perfil de suela. Puntera a la izquierda.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Jordan 6 Rings White / University Red / Black, SKU: 323419-164. Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole. Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Jordan 6 Rings White / University Red / Black, 323419-164, 90° Lateral Exterior, Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole., Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 2: Perspectiva 3/4 Frontal (45°)
*Muestra volumen tridimensional, puntera y lateral exterior simultáneamente.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Jordan 6 Rings White / University Red / Black, SKU: 323419-164. Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle. Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Jordan 6 Rings White / University Red / Black, 323419-164, 3/4 Frontal Perspectiva, Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle., Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 3: Frontal Directa (0°)
*Muestra simetría de puntera, lengüeta, ancho de empeine y sistema de cordones.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Jordan 6 Rings White / University Red / Black, SKU: 323419-164. Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker. Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Jordan 6 Rings White / University Red / Black, 323419-164, Frontal Directa 0°, Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker., Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 4: Posterior / Talón (180°)
*Muestra contrafuerte del talón, logo de talón (Jumpman / Nike Air) y altura de caña.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Jordan 6 Rings White / University Red / Black, SKU: 323419-164. Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level. Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Jordan 6 Rings White / University Red / Black, 323419-164, Posterior Talón 180°, Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level., Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 5: Perspectiva 3/4 Trasera (135°)
*Muestra contorno del tobillo, talón tridimensional y curva posterior de entresuela.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Jordan 6 Rings White / University Red / Black, SKU: 323419-164. Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front. Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Jordan 6 Rings White / University Red / Black, 323419-164, 3/4 Trasera Exterior, Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front., Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 6: Perfil Lateral Interior / Medial (90°)
*Muestra el lado interno del pie, soporte del arco y patrón medial.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Jordan 6 Rings White / University Red / Black, SKU: 323419-164. Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level. Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Jordan 6 Rings White / University Red / Black, 323419-164, 90° Lateral Interior (Medial), Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level., Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 7: Cenital / Superior (90° Top-Down)
*Muestra vista plana superior completa: plantilla interior, cordones y lengüeta.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Jordan 6 Rings White / University Red / Black, SKU: 323419-164. Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left. Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Jordan 6 Rings White / University Red / Black, 323419-164, Cenital Superior 90°, Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left., Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

---

### [22] IR4727-100 — Nike Air Diamond Turf II

**Foto de Referencia Primaria recomendada:** `dist/assets/2-norm-std/IR4727-100/01-lateral.webp`

#### Ángulo 1: Perfil Lateral Exterior (90°)
*Muestra silueta completa, logos principales y perfil de suela. Puntera a la izquierda.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Diamond Turf II, SKU: IR4727-100. Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole. Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Diamond Turf II, IR4727-100, 90° Lateral Exterior, Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole., Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 2: Perspectiva 3/4 Frontal (45°)
*Muestra volumen tridimensional, puntera y lateral exterior simultáneamente.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Diamond Turf II, SKU: IR4727-100. Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle. Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Diamond Turf II, IR4727-100, 3/4 Frontal Perspectiva, Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle., Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 3: Frontal Directa (0°)
*Muestra simetría de puntera, lengüeta, ancho de empeine y sistema de cordones.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Diamond Turf II, SKU: IR4727-100. Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker. Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Diamond Turf II, IR4727-100, Frontal Directa 0°, Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker., Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 4: Posterior / Talón (180°)
*Muestra contrafuerte del talón, logo de talón (Jumpman / Nike Air) y altura de caña.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Diamond Turf II, SKU: IR4727-100. Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level. Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Diamond Turf II, IR4727-100, Posterior Talón 180°, Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level., Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 5: Perspectiva 3/4 Trasera (135°)
*Muestra contorno del tobillo, talón tridimensional y curva posterior de entresuela.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Diamond Turf II, SKU: IR4727-100. Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front. Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Diamond Turf II, IR4727-100, 3/4 Trasera Exterior, Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front., Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 6: Perfil Lateral Interior / Medial (90°)
*Muestra el lado interno del pie, soporte del arco y patrón medial.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Diamond Turf II, SKU: IR4727-100. Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level. Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Diamond Turf II, IR4727-100, 90° Lateral Interior (Medial), Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level., Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 7: Cenital / Superior (90° Top-Down)
*Muestra vista plana superior completa: plantilla interior, cordones y lengüeta.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Diamond Turf II, SKU: IR4727-100. Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left. Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Diamond Turf II, IR4727-100, Cenital Superior 90°, Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left., Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

---

### [23] IR4714-100 — Nike Air DT Max '96 Low White / Metallic

**Foto de Referencia Primaria recomendada:** `dist/assets/2-norm-std/IR4714-100/01-lateral.webp`

#### Ángulo 1: Perfil Lateral Exterior (90°)
*Muestra silueta completa, logos principales y perfil de suela. Puntera a la izquierda.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air DT Max '96 Low White / Metallic, SKU: IR4714-100. Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole. Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air DT Max '96 Low White / Metallic, IR4714-100, 90° Lateral Exterior, Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole., Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 2: Perspectiva 3/4 Frontal (45°)
*Muestra volumen tridimensional, puntera y lateral exterior simultáneamente.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air DT Max '96 Low White / Metallic, SKU: IR4714-100. Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle. Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air DT Max '96 Low White / Metallic, IR4714-100, 3/4 Frontal Perspectiva, Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle., Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 3: Frontal Directa (0°)
*Muestra simetría de puntera, lengüeta, ancho de empeine y sistema de cordones.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air DT Max '96 Low White / Metallic, SKU: IR4714-100. Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker. Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air DT Max '96 Low White / Metallic, IR4714-100, Frontal Directa 0°, Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker., Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 4: Posterior / Talón (180°)
*Muestra contrafuerte del talón, logo de talón (Jumpman / Nike Air) y altura de caña.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air DT Max '96 Low White / Metallic, SKU: IR4714-100. Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level. Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air DT Max '96 Low White / Metallic, IR4714-100, Posterior Talón 180°, Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level., Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 5: Perspectiva 3/4 Trasera (135°)
*Muestra contorno del tobillo, talón tridimensional y curva posterior de entresuela.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air DT Max '96 Low White / Metallic, SKU: IR4714-100. Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front. Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air DT Max '96 Low White / Metallic, IR4714-100, 3/4 Trasera Exterior, Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front., Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 6: Perfil Lateral Interior / Medial (90°)
*Muestra el lado interno del pie, soporte del arco y patrón medial.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air DT Max '96 Low White / Metallic, SKU: IR4714-100. Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level. Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air DT Max '96 Low White / Metallic, IR4714-100, 90° Lateral Interior (Medial), Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level., Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 7: Cenital / Superior (90° Top-Down)
*Muestra vista plana superior completa: plantilla interior, cordones y lengüeta.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air DT Max '96 Low White / Metallic, SKU: IR4714-100. Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left. Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air DT Max '96 Low White / Metallic, IR4714-100, Cenital Superior 90°, Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left., Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

---

### [24] DR8784-005 — Nike Zoom LeBron NXXT Gen "Black Wolf Grey"

**Foto de Referencia Primaria recomendada:** `dist/assets/2-norm-std/DR8784-005/01-lateral.webp`

#### Ángulo 1: Perfil Lateral Exterior (90°)
*Muestra silueta completa, logos principales y perfil de suela. Puntera a la izquierda.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Zoom LeBron NXXT Gen "Black Wolf Grey", SKU: DR8784-005. Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole. Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Zoom LeBron NXXT Gen "Black Wolf Grey", DR8784-005, 90° Lateral Exterior, Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole., Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 2: Perspectiva 3/4 Frontal (45°)
*Muestra volumen tridimensional, puntera y lateral exterior simultáneamente.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Zoom LeBron NXXT Gen "Black Wolf Grey", SKU: DR8784-005. Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle. Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Zoom LeBron NXXT Gen "Black Wolf Grey", DR8784-005, 3/4 Frontal Perspectiva, Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle., Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 3: Frontal Directa (0°)
*Muestra simetría de puntera, lengüeta, ancho de empeine y sistema de cordones.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Zoom LeBron NXXT Gen "Black Wolf Grey", SKU: DR8784-005. Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker. Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Zoom LeBron NXXT Gen "Black Wolf Grey", DR8784-005, Frontal Directa 0°, Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker., Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 4: Posterior / Talón (180°)
*Muestra contrafuerte del talón, logo de talón (Jumpman / Nike Air) y altura de caña.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Zoom LeBron NXXT Gen "Black Wolf Grey", SKU: DR8784-005. Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level. Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Zoom LeBron NXXT Gen "Black Wolf Grey", DR8784-005, Posterior Talón 180°, Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level., Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 5: Perspectiva 3/4 Trasera (135°)
*Muestra contorno del tobillo, talón tridimensional y curva posterior de entresuela.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Zoom LeBron NXXT Gen "Black Wolf Grey", SKU: DR8784-005. Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front. Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Zoom LeBron NXXT Gen "Black Wolf Grey", DR8784-005, 3/4 Trasera Exterior, Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front., Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 6: Perfil Lateral Interior / Medial (90°)
*Muestra el lado interno del pie, soporte del arco y patrón medial.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Zoom LeBron NXXT Gen "Black Wolf Grey", SKU: DR8784-005. Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level. Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Zoom LeBron NXXT Gen "Black Wolf Grey", DR8784-005, 90° Lateral Interior (Medial), Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level., Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 7: Cenital / Superior (90° Top-Down)
*Muestra vista plana superior completa: plantilla interior, cordones y lengüeta.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Zoom LeBron NXXT Gen "Black Wolf Grey", SKU: DR8784-005. Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left. Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Zoom LeBron NXXT Gen "Black Wolf Grey", DR8784-005, Cenital Superior 90°, Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left., Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

---

### [25] AR3762-001 — Air Jordan Access "Black Gym Red"

**Foto de Referencia Primaria recomendada:** `dist/assets/2-norm-std/AR3762-001/01-lateral.webp`

#### Ángulo 1: Perfil Lateral Exterior (90°)
*Muestra silueta completa, logos principales y perfil de suela. Puntera a la izquierda.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan Access "Black Gym Red", SKU: AR3762-001. Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole. Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan Access "Black Gym Red", AR3762-001, 90° Lateral Exterior, Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole., Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 2: Perspectiva 3/4 Frontal (45°)
*Muestra volumen tridimensional, puntera y lateral exterior simultáneamente.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan Access "Black Gym Red", SKU: AR3762-001. Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle. Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan Access "Black Gym Red", AR3762-001, 3/4 Frontal Perspectiva, Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle., Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 3: Frontal Directa (0°)
*Muestra simetría de puntera, lengüeta, ancho de empeine y sistema de cordones.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan Access "Black Gym Red", SKU: AR3762-001. Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker. Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan Access "Black Gym Red", AR3762-001, Frontal Directa 0°, Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker., Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 4: Posterior / Talón (180°)
*Muestra contrafuerte del talón, logo de talón (Jumpman / Nike Air) y altura de caña.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan Access "Black Gym Red", SKU: AR3762-001. Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level. Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan Access "Black Gym Red", AR3762-001, Posterior Talón 180°, Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level., Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 5: Perspectiva 3/4 Trasera (135°)
*Muestra contorno del tobillo, talón tridimensional y curva posterior de entresuela.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan Access "Black Gym Red", SKU: AR3762-001. Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front. Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan Access "Black Gym Red", AR3762-001, 3/4 Trasera Exterior, Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front., Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 6: Perfil Lateral Interior / Medial (90°)
*Muestra el lado interno del pie, soporte del arco y patrón medial.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan Access "Black Gym Red", SKU: AR3762-001. Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level. Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan Access "Black Gym Red", AR3762-001, 90° Lateral Interior (Medial), Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level., Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 7: Cenital / Superior (90° Top-Down)
*Muestra vista plana superior completa: plantilla interior, cordones y lengüeta.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan Access "Black Gym Red", SKU: AR3762-001. Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left. Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan Access "Black Gym Red", AR3762-001, Cenital Superior 90°, Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left., Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

---

### [26] IV5197-201 — Nike Air Force 1 '07 Light British Tan / Sail / Hemp / Metallic Gold

**Foto de Referencia Primaria recomendada:** `dist/assets/2-norm-std/IV5197-201/01-lateral.webp`

#### Ángulo 1: Perfil Lateral Exterior (90°)
*Muestra silueta completa, logos principales y perfil de suela. Puntera a la izquierda.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Force 1 '07 Light British Tan / Sail / Hemp / Metallic Gold, SKU: IV5197-201. Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole. Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Force 1 '07 Light British Tan / Sail / Hemp / Metallic Gold, IV5197-201, 90° Lateral Exterior, Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole., Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 2: Perspectiva 3/4 Frontal (45°)
*Muestra volumen tridimensional, puntera y lateral exterior simultáneamente.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Force 1 '07 Light British Tan / Sail / Hemp / Metallic Gold, SKU: IV5197-201. Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle. Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Force 1 '07 Light British Tan / Sail / Hemp / Metallic Gold, IV5197-201, 3/4 Frontal Perspectiva, Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle., Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 3: Frontal Directa (0°)
*Muestra simetría de puntera, lengüeta, ancho de empeine y sistema de cordones.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Force 1 '07 Light British Tan / Sail / Hemp / Metallic Gold, SKU: IV5197-201. Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker. Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Force 1 '07 Light British Tan / Sail / Hemp / Metallic Gold, IV5197-201, Frontal Directa 0°, Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker., Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 4: Posterior / Talón (180°)
*Muestra contrafuerte del talón, logo de talón (Jumpman / Nike Air) y altura de caña.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Force 1 '07 Light British Tan / Sail / Hemp / Metallic Gold, SKU: IV5197-201. Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level. Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Force 1 '07 Light British Tan / Sail / Hemp / Metallic Gold, IV5197-201, Posterior Talón 180°, Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level., Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 5: Perspectiva 3/4 Trasera (135°)
*Muestra contorno del tobillo, talón tridimensional y curva posterior de entresuela.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Force 1 '07 Light British Tan / Sail / Hemp / Metallic Gold, SKU: IV5197-201. Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front. Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Force 1 '07 Light British Tan / Sail / Hemp / Metallic Gold, IV5197-201, 3/4 Trasera Exterior, Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front., Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 6: Perfil Lateral Interior / Medial (90°)
*Muestra el lado interno del pie, soporte del arco y patrón medial.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Force 1 '07 Light British Tan / Sail / Hemp / Metallic Gold, SKU: IV5197-201. Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level. Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Force 1 '07 Light British Tan / Sail / Hemp / Metallic Gold, IV5197-201, 90° Lateral Interior (Medial), Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level., Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 7: Cenital / Superior (90° Top-Down)
*Muestra vista plana superior completa: plantilla interior, cordones y lengüeta.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Force 1 '07 Light British Tan / Sail / Hemp / Metallic Gold, SKU: IV5197-201. Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left. Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Force 1 '07 Light British Tan / Sail / Hemp / Metallic Gold, IV5197-201, Cenital Superior 90°, Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left., Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

---

### [27] CU4152-101 — Nike Air Max Bolt

**Foto de Referencia Primaria recomendada:** `dist/assets/2-norm-std/CU4152-101/01-lateral.webp`

#### Ángulo 1: Perfil Lateral Exterior (90°)
*Muestra silueta completa, logos principales y perfil de suela. Puntera a la izquierda.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Max Bolt, SKU: CU4152-101. Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole. Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Max Bolt, CU4152-101, 90° Lateral Exterior, Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole., Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 2: Perspectiva 3/4 Frontal (45°)
*Muestra volumen tridimensional, puntera y lateral exterior simultáneamente.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Max Bolt, SKU: CU4152-101. Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle. Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Max Bolt, CU4152-101, 3/4 Frontal Perspectiva, Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle., Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 3: Frontal Directa (0°)
*Muestra simetría de puntera, lengüeta, ancho de empeine y sistema de cordones.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Max Bolt, SKU: CU4152-101. Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker. Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Max Bolt, CU4152-101, Frontal Directa 0°, Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker., Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 4: Posterior / Talón (180°)
*Muestra contrafuerte del talón, logo de talón (Jumpman / Nike Air) y altura de caña.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Max Bolt, SKU: CU4152-101. Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level. Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Max Bolt, CU4152-101, Posterior Talón 180°, Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level., Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 5: Perspectiva 3/4 Trasera (135°)
*Muestra contorno del tobillo, talón tridimensional y curva posterior de entresuela.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Max Bolt, SKU: CU4152-101. Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front. Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Max Bolt, CU4152-101, 3/4 Trasera Exterior, Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front., Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 6: Perfil Lateral Interior / Medial (90°)
*Muestra el lado interno del pie, soporte del arco y patrón medial.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Max Bolt, SKU: CU4152-101. Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level. Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Max Bolt, CU4152-101, 90° Lateral Interior (Medial), Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level., Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 7: Cenital / Superior (90° Top-Down)
*Muestra vista plana superior completa: plantilla interior, cordones y lengüeta.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Max Bolt, SKU: CU4152-101. Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left. Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Max Bolt, CU4152-101, Cenital Superior 90°, Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left., Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

---

### [28] AR4430-101 — Jordan Lift Off White / Black / Wolf Grey

**Foto de Referencia Primaria recomendada:** `dist/assets/2-norm-std/AR4430-101/01-lateral.webp`

#### Ángulo 1: Perfil Lateral Exterior (90°)
*Muestra silueta completa, logos principales y perfil de suela. Puntera a la izquierda.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Jordan Lift Off White / Black / Wolf Grey, SKU: AR4430-101. Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole. Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Jordan Lift Off White / Black / Wolf Grey, AR4430-101, 90° Lateral Exterior, Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole., Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 2: Perspectiva 3/4 Frontal (45°)
*Muestra volumen tridimensional, puntera y lateral exterior simultáneamente.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Jordan Lift Off White / Black / Wolf Grey, SKU: AR4430-101. Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle. Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Jordan Lift Off White / Black / Wolf Grey, AR4430-101, 3/4 Frontal Perspectiva, Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle., Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 3: Frontal Directa (0°)
*Muestra simetría de puntera, lengüeta, ancho de empeine y sistema de cordones.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Jordan Lift Off White / Black / Wolf Grey, SKU: AR4430-101. Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker. Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Jordan Lift Off White / Black / Wolf Grey, AR4430-101, Frontal Directa 0°, Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker., Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 4: Posterior / Talón (180°)
*Muestra contrafuerte del talón, logo de talón (Jumpman / Nike Air) y altura de caña.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Jordan Lift Off White / Black / Wolf Grey, SKU: AR4430-101. Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level. Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Jordan Lift Off White / Black / Wolf Grey, AR4430-101, Posterior Talón 180°, Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level., Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 5: Perspectiva 3/4 Trasera (135°)
*Muestra contorno del tobillo, talón tridimensional y curva posterior de entresuela.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Jordan Lift Off White / Black / Wolf Grey, SKU: AR4430-101. Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front. Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Jordan Lift Off White / Black / Wolf Grey, AR4430-101, 3/4 Trasera Exterior, Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front., Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 6: Perfil Lateral Interior / Medial (90°)
*Muestra el lado interno del pie, soporte del arco y patrón medial.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Jordan Lift Off White / Black / Wolf Grey, SKU: AR4430-101. Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level. Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Jordan Lift Off White / Black / Wolf Grey, AR4430-101, 90° Lateral Interior (Medial), Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level., Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 7: Cenital / Superior (90° Top-Down)
*Muestra vista plana superior completa: plantilla interior, cordones y lengüeta.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Jordan Lift Off White / Black / Wolf Grey, SKU: AR4430-101. Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left. Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Jordan Lift Off White / Black / Wolf Grey, AR4430-101, Cenital Superior 90°, Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left., Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

---

### [29] DM0967-111 — Air Jordan 3 Retro "Pure Money"

**Foto de Referencia Primaria recomendada:** `dist/assets/2-norm-std/DM0967-111/01-lateral.webp`

#### Ángulo 1: Perfil Lateral Exterior (90°)
*Muestra silueta completa, logos principales y perfil de suela. Puntera a la izquierda.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 3 Retro "Pure Money", SKU: DM0967-111. Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole. Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 3 Retro "Pure Money", DM0967-111, 90° Lateral Exterior, Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole., Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 2: Perspectiva 3/4 Frontal (45°)
*Muestra volumen tridimensional, puntera y lateral exterior simultáneamente.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 3 Retro "Pure Money", SKU: DM0967-111. Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle. Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 3 Retro "Pure Money", DM0967-111, 3/4 Frontal Perspectiva, Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle., Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 3: Frontal Directa (0°)
*Muestra simetría de puntera, lengüeta, ancho de empeine y sistema de cordones.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 3 Retro "Pure Money", SKU: DM0967-111. Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker. Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 3 Retro "Pure Money", DM0967-111, Frontal Directa 0°, Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker., Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 4: Posterior / Talón (180°)
*Muestra contrafuerte del talón, logo de talón (Jumpman / Nike Air) y altura de caña.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 3 Retro "Pure Money", SKU: DM0967-111. Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level. Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 3 Retro "Pure Money", DM0967-111, Posterior Talón 180°, Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level., Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 5: Perspectiva 3/4 Trasera (135°)
*Muestra contorno del tobillo, talón tridimensional y curva posterior de entresuela.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 3 Retro "Pure Money", SKU: DM0967-111. Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front. Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 3 Retro "Pure Money", DM0967-111, 3/4 Trasera Exterior, Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front., Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 6: Perfil Lateral Interior / Medial (90°)
*Muestra el lado interno del pie, soporte del arco y patrón medial.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 3 Retro "Pure Money", SKU: DM0967-111. Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level. Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 3 Retro "Pure Money", DM0967-111, 90° Lateral Interior (Medial), Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level., Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 7: Cenital / Superior (90° Top-Down)
*Muestra vista plana superior completa: plantilla interior, cordones y lengüeta.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 3 Retro "Pure Money", SKU: DM0967-111. Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left. Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 3 Retro "Pure Money", DM0967-111, Cenital Superior 90°, Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left., Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

---

### [30] 553560-081 — Air Jordan 1 Low "Shattered Backboard Alternate"

**Foto de Referencia Primaria recomendada:** `dist/assets/2-norm-std/553560-081/01-lateral.webp`

#### Ángulo 1: Perfil Lateral Exterior (90°)
*Muestra silueta completa, logos principales y perfil de suela. Puntera a la izquierda.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 1 Low "Shattered Backboard Alternate", SKU: 553560-081. Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole. Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 1 Low "Shattered Backboard Alternate", 553560-081, 90° Lateral Exterior, Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole., Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 2: Perspectiva 3/4 Frontal (45°)
*Muestra volumen tridimensional, puntera y lateral exterior simultáneamente.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 1 Low "Shattered Backboard Alternate", SKU: 553560-081. Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle. Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 1 Low "Shattered Backboard Alternate", 553560-081, 3/4 Frontal Perspectiva, Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle., Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 3: Frontal Directa (0°)
*Muestra simetría de puntera, lengüeta, ancho de empeine y sistema de cordones.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 1 Low "Shattered Backboard Alternate", SKU: 553560-081. Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker. Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 1 Low "Shattered Backboard Alternate", 553560-081, Frontal Directa 0°, Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker., Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 4: Posterior / Talón (180°)
*Muestra contrafuerte del talón, logo de talón (Jumpman / Nike Air) y altura de caña.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 1 Low "Shattered Backboard Alternate", SKU: 553560-081. Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level. Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 1 Low "Shattered Backboard Alternate", 553560-081, Posterior Talón 180°, Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level., Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 5: Perspectiva 3/4 Trasera (135°)
*Muestra contorno del tobillo, talón tridimensional y curva posterior de entresuela.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 1 Low "Shattered Backboard Alternate", SKU: 553560-081. Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front. Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 1 Low "Shattered Backboard Alternate", 553560-081, 3/4 Trasera Exterior, Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front., Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 6: Perfil Lateral Interior / Medial (90°)
*Muestra el lado interno del pie, soporte del arco y patrón medial.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 1 Low "Shattered Backboard Alternate", SKU: 553560-081. Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level. Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 1 Low "Shattered Backboard Alternate", 553560-081, 90° Lateral Interior (Medial), Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level., Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 7: Cenital / Superior (90° Top-Down)
*Muestra vista plana superior completa: plantilla interior, cordones y lengüeta.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 1 Low "Shattered Backboard Alternate", SKU: 553560-081. Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left. Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 1 Low "Shattered Backboard Alternate", 553560-081, Cenital Superior 90°, Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left., Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

---

### [31] HV4775-001 — Air Jordan 1 Low "Inner Beast"

**Foto de Referencia Primaria recomendada:** `dist/assets/2-norm-std/HV4775-001/01-lateral.webp`

#### Ángulo 1: Perfil Lateral Exterior (90°)
*Muestra silueta completa, logos principales y perfil de suela. Puntera a la izquierda.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 1 Low "Inner Beast", SKU: HV4775-001. Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole. Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 1 Low "Inner Beast", HV4775-001, 90° Lateral Exterior, Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole., Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 2: Perspectiva 3/4 Frontal (45°)
*Muestra volumen tridimensional, puntera y lateral exterior simultáneamente.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 1 Low "Inner Beast", SKU: HV4775-001. Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle. Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 1 Low "Inner Beast", HV4775-001, 3/4 Frontal Perspectiva, Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle., Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 3: Frontal Directa (0°)
*Muestra simetría de puntera, lengüeta, ancho de empeine y sistema de cordones.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 1 Low "Inner Beast", SKU: HV4775-001. Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker. Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 1 Low "Inner Beast", HV4775-001, Frontal Directa 0°, Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker., Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 4: Posterior / Talón (180°)
*Muestra contrafuerte del talón, logo de talón (Jumpman / Nike Air) y altura de caña.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 1 Low "Inner Beast", SKU: HV4775-001. Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level. Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 1 Low "Inner Beast", HV4775-001, Posterior Talón 180°, Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level., Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 5: Perspectiva 3/4 Trasera (135°)
*Muestra contorno del tobillo, talón tridimensional y curva posterior de entresuela.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 1 Low "Inner Beast", SKU: HV4775-001. Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front. Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 1 Low "Inner Beast", HV4775-001, 3/4 Trasera Exterior, Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front., Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 6: Perfil Lateral Interior / Medial (90°)
*Muestra el lado interno del pie, soporte del arco y patrón medial.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 1 Low "Inner Beast", SKU: HV4775-001. Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level. Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 1 Low "Inner Beast", HV4775-001, 90° Lateral Interior (Medial), Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level., Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 7: Cenital / Superior (90° Top-Down)
*Muestra vista plana superior completa: plantilla interior, cordones y lengüeta.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 1 Low "Inner Beast", SKU: HV4775-001. Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left. Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 1 Low "Inner Beast", HV4775-001, Cenital Superior 90°, Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left., Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

---

### [32] HQ8034-700 — Nike LeBron Witness 9

**Foto de Referencia Primaria recomendada:** `dist/assets/2-norm-std/HQ8034-700/01-lateral.webp`

#### Ángulo 1: Perfil Lateral Exterior (90°)
*Muestra silueta completa, logos principales y perfil de suela. Puntera a la izquierda.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike LeBron Witness 9, SKU: HQ8034-700. Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole. Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike LeBron Witness 9, HQ8034-700, 90° Lateral Exterior, Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole., Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 2: Perspectiva 3/4 Frontal (45°)
*Muestra volumen tridimensional, puntera y lateral exterior simultáneamente.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike LeBron Witness 9, SKU: HQ8034-700. Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle. Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike LeBron Witness 9, HQ8034-700, 3/4 Frontal Perspectiva, Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle., Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 3: Frontal Directa (0°)
*Muestra simetría de puntera, lengüeta, ancho de empeine y sistema de cordones.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike LeBron Witness 9, SKU: HQ8034-700. Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker. Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike LeBron Witness 9, HQ8034-700, Frontal Directa 0°, Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker., Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 4: Posterior / Talón (180°)
*Muestra contrafuerte del talón, logo de talón (Jumpman / Nike Air) y altura de caña.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike LeBron Witness 9, SKU: HQ8034-700. Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level. Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike LeBron Witness 9, HQ8034-700, Posterior Talón 180°, Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level., Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 5: Perspectiva 3/4 Trasera (135°)
*Muestra contorno del tobillo, talón tridimensional y curva posterior de entresuela.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike LeBron Witness 9, SKU: HQ8034-700. Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front. Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike LeBron Witness 9, HQ8034-700, 3/4 Trasera Exterior, Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front., Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 6: Perfil Lateral Interior / Medial (90°)
*Muestra el lado interno del pie, soporte del arco y patrón medial.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike LeBron Witness 9, SKU: HQ8034-700. Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level. Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike LeBron Witness 9, HQ8034-700, 90° Lateral Interior (Medial), Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level., Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 7: Cenital / Superior (90° Top-Down)
*Muestra vista plana superior completa: plantilla interior, cordones y lengüeta.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike LeBron Witness 9, SKU: HQ8034-700. Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left. Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike LeBron Witness 9, HQ8034-700, Cenital Superior 90°, Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left., Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

---

### [33] IQ0213-685 — Nike Air Force 1 Rust Pink / Metallic Red

**Foto de Referencia Primaria recomendada:** `dist/assets/2-norm-std/IQ0213-685/01-lateral.webp`

#### Ángulo 1: Perfil Lateral Exterior (90°)
*Muestra silueta completa, logos principales y perfil de suela. Puntera a la izquierda.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Force 1 Rust Pink / Metallic Red, SKU: IQ0213-685. Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole. Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Force 1 Rust Pink / Metallic Red, IQ0213-685, 90° Lateral Exterior, Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole., Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 2: Perspectiva 3/4 Frontal (45°)
*Muestra volumen tridimensional, puntera y lateral exterior simultáneamente.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Force 1 Rust Pink / Metallic Red, SKU: IQ0213-685. Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle. Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Force 1 Rust Pink / Metallic Red, IQ0213-685, 3/4 Frontal Perspectiva, Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle., Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 3: Frontal Directa (0°)
*Muestra simetría de puntera, lengüeta, ancho de empeine y sistema de cordones.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Force 1 Rust Pink / Metallic Red, SKU: IQ0213-685. Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker. Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Force 1 Rust Pink / Metallic Red, IQ0213-685, Frontal Directa 0°, Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker., Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 4: Posterior / Talón (180°)
*Muestra contrafuerte del talón, logo de talón (Jumpman / Nike Air) y altura de caña.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Force 1 Rust Pink / Metallic Red, SKU: IQ0213-685. Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level. Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Force 1 Rust Pink / Metallic Red, IQ0213-685, Posterior Talón 180°, Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level., Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 5: Perspectiva 3/4 Trasera (135°)
*Muestra contorno del tobillo, talón tridimensional y curva posterior de entresuela.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Force 1 Rust Pink / Metallic Red, SKU: IQ0213-685. Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front. Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Force 1 Rust Pink / Metallic Red, IQ0213-685, 3/4 Trasera Exterior, Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front., Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 6: Perfil Lateral Interior / Medial (90°)
*Muestra el lado interno del pie, soporte del arco y patrón medial.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Force 1 Rust Pink / Metallic Red, SKU: IQ0213-685. Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level. Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Force 1 Rust Pink / Metallic Red, IQ0213-685, 90° Lateral Interior (Medial), Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level., Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 7: Cenital / Superior (90° Top-Down)
*Muestra vista plana superior completa: plantilla interior, cordones y lengüeta.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Force 1 Rust Pink / Metallic Red, SKU: IQ0213-685. Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left. Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Force 1 Rust Pink / Metallic Red, IQ0213-685, Cenital Superior 90°, Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left., Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

---

### [34] CW2626-008 — Nike Shox R4 College Grey / Volt

**Foto de Referencia Primaria recomendada:** `dist/assets/2-norm-std/CW2626-008/01-lateral.webp`

#### Ángulo 1: Perfil Lateral Exterior (90°)
*Muestra silueta completa, logos principales y perfil de suela. Puntera a la izquierda.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Shox R4 College Grey / Volt, SKU: CW2626-008. Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole. Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Shox R4 College Grey / Volt, CW2626-008, 90° Lateral Exterior, Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole., Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 2: Perspectiva 3/4 Frontal (45°)
*Muestra volumen tridimensional, puntera y lateral exterior simultáneamente.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Shox R4 College Grey / Volt, SKU: CW2626-008. Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle. Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Shox R4 College Grey / Volt, CW2626-008, 3/4 Frontal Perspectiva, Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle., Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 3: Frontal Directa (0°)
*Muestra simetría de puntera, lengüeta, ancho de empeine y sistema de cordones.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Shox R4 College Grey / Volt, SKU: CW2626-008. Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker. Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Shox R4 College Grey / Volt, CW2626-008, Frontal Directa 0°, Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker., Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 4: Posterior / Talón (180°)
*Muestra contrafuerte del talón, logo de talón (Jumpman / Nike Air) y altura de caña.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Shox R4 College Grey / Volt, SKU: CW2626-008. Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level. Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Shox R4 College Grey / Volt, CW2626-008, Posterior Talón 180°, Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level., Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 5: Perspectiva 3/4 Trasera (135°)
*Muestra contorno del tobillo, talón tridimensional y curva posterior de entresuela.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Shox R4 College Grey / Volt, SKU: CW2626-008. Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front. Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Shox R4 College Grey / Volt, CW2626-008, 3/4 Trasera Exterior, Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front., Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 6: Perfil Lateral Interior / Medial (90°)
*Muestra el lado interno del pie, soporte del arco y patrón medial.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Shox R4 College Grey / Volt, SKU: CW2626-008. Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level. Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Shox R4 College Grey / Volt, CW2626-008, 90° Lateral Interior (Medial), Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level., Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 7: Cenital / Superior (90° Top-Down)
*Muestra vista plana superior completa: plantilla interior, cordones y lengüeta.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Shox R4 College Grey / Volt, SKU: CW2626-008. Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left. Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Shox R4 College Grey / Volt, CW2626-008, Cenital Superior 90°, Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left., Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

---

### [35] HQ7980-001 — Air Jordan 5 Retro "Halloween"

**Foto de Referencia Primaria recomendada:** `dist/assets/2-norm-std/HQ7980-001/01-lateral.webp`

#### Ángulo 1: Perfil Lateral Exterior (90°)
*Muestra silueta completa, logos principales y perfil de suela. Puntera a la izquierda.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 5 Retro "Halloween", SKU: HQ7980-001. Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole. Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 5 Retro "Halloween", HQ7980-001, 90° Lateral Exterior, Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole., Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 2: Perspectiva 3/4 Frontal (45°)
*Muestra volumen tridimensional, puntera y lateral exterior simultáneamente.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 5 Retro "Halloween", SKU: HQ7980-001. Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle. Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 5 Retro "Halloween", HQ7980-001, 3/4 Frontal Perspectiva, Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle., Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 3: Frontal Directa (0°)
*Muestra simetría de puntera, lengüeta, ancho de empeine y sistema de cordones.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 5 Retro "Halloween", SKU: HQ7980-001. Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker. Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 5 Retro "Halloween", HQ7980-001, Frontal Directa 0°, Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker., Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 4: Posterior / Talón (180°)
*Muestra contrafuerte del talón, logo de talón (Jumpman / Nike Air) y altura de caña.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 5 Retro "Halloween", SKU: HQ7980-001. Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level. Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 5 Retro "Halloween", HQ7980-001, Posterior Talón 180°, Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level., Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 5: Perspectiva 3/4 Trasera (135°)
*Muestra contorno del tobillo, talón tridimensional y curva posterior de entresuela.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 5 Retro "Halloween", SKU: HQ7980-001. Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front. Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 5 Retro "Halloween", HQ7980-001, 3/4 Trasera Exterior, Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front., Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 6: Perfil Lateral Interior / Medial (90°)
*Muestra el lado interno del pie, soporte del arco y patrón medial.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 5 Retro "Halloween", SKU: HQ7980-001. Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level. Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 5 Retro "Halloween", HQ7980-001, 90° Lateral Interior (Medial), Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level., Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 7: Cenital / Superior (90° Top-Down)
*Muestra vista plana superior completa: plantilla interior, cordones y lengüeta.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 5 Retro "Halloween", SKU: HQ7980-001. Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left. Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 5 Retro "Halloween", HQ7980-001, Cenital Superior 90°, Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left., Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

---

### [36] IM4026-100 — Air Jordan 4 Retro "Flight Club"

**Foto de Referencia Primaria recomendada:** `dist/assets/2-norm-std/IM4026-100/01-lateral.webp`

#### Ángulo 1: Perfil Lateral Exterior (90°)
*Muestra silueta completa, logos principales y perfil de suela. Puntera a la izquierda.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 4 Retro "Flight Club", SKU: IM4026-100. Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole. Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 4 Retro "Flight Club", IM4026-100, 90° Lateral Exterior, Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole., Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 2: Perspectiva 3/4 Frontal (45°)
*Muestra volumen tridimensional, puntera y lateral exterior simultáneamente.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 4 Retro "Flight Club", SKU: IM4026-100. Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle. Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 4 Retro "Flight Club", IM4026-100, 3/4 Frontal Perspectiva, Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle., Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 3: Frontal Directa (0°)
*Muestra simetría de puntera, lengüeta, ancho de empeine y sistema de cordones.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 4 Retro "Flight Club", SKU: IM4026-100. Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker. Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 4 Retro "Flight Club", IM4026-100, Frontal Directa 0°, Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker., Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 4: Posterior / Talón (180°)
*Muestra contrafuerte del talón, logo de talón (Jumpman / Nike Air) y altura de caña.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 4 Retro "Flight Club", SKU: IM4026-100. Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level. Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 4 Retro "Flight Club", IM4026-100, Posterior Talón 180°, Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level., Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 5: Perspectiva 3/4 Trasera (135°)
*Muestra contorno del tobillo, talón tridimensional y curva posterior de entresuela.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 4 Retro "Flight Club", SKU: IM4026-100. Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front. Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 4 Retro "Flight Club", IM4026-100, 3/4 Trasera Exterior, Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front., Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 6: Perfil Lateral Interior / Medial (90°)
*Muestra el lado interno del pie, soporte del arco y patrón medial.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 4 Retro "Flight Club", SKU: IM4026-100. Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level. Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 4 Retro "Flight Club", IM4026-100, 90° Lateral Interior (Medial), Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level., Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 7: Cenital / Superior (90° Top-Down)
*Muestra vista plana superior completa: plantilla interior, cordones y lengüeta.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 4 Retro "Flight Club", SKU: IM4026-100. Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left. Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 4 Retro "Flight Club", IM4026-100, Cenital Superior 90°, Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left., Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

---

### [37] IO2829-600 — Air Jordan 4 Retro "She's A Star"

**Foto de Referencia Primaria recomendada:** `dist/assets/2-norm-std/IO2829-600/01-lateral.webp`

#### Ángulo 1: Perfil Lateral Exterior (90°)
*Muestra silueta completa, logos principales y perfil de suela. Puntera a la izquierda.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 4 Retro "She's A Star", SKU: IO2829-600. Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole. Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 4 Retro "She's A Star", IO2829-600, 90° Lateral Exterior, Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole., Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 2: Perspectiva 3/4 Frontal (45°)
*Muestra volumen tridimensional, puntera y lateral exterior simultáneamente.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 4 Retro "She's A Star", SKU: IO2829-600. Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle. Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 4 Retro "She's A Star", IO2829-600, 3/4 Frontal Perspectiva, Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle., Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 3: Frontal Directa (0°)
*Muestra simetría de puntera, lengüeta, ancho de empeine y sistema de cordones.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 4 Retro "She's A Star", SKU: IO2829-600. Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker. Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 4 Retro "She's A Star", IO2829-600, Frontal Directa 0°, Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker., Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 4: Posterior / Talón (180°)
*Muestra contrafuerte del talón, logo de talón (Jumpman / Nike Air) y altura de caña.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 4 Retro "She's A Star", SKU: IO2829-600. Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level. Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 4 Retro "She's A Star", IO2829-600, Posterior Talón 180°, Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level., Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 5: Perspectiva 3/4 Trasera (135°)
*Muestra contorno del tobillo, talón tridimensional y curva posterior de entresuela.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 4 Retro "She's A Star", SKU: IO2829-600. Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front. Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 4 Retro "She's A Star", IO2829-600, 3/4 Trasera Exterior, Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front., Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 6: Perfil Lateral Interior / Medial (90°)
*Muestra el lado interno del pie, soporte del arco y patrón medial.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 4 Retro "She's A Star", SKU: IO2829-600. Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level. Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 4 Retro "She's A Star", IO2829-600, 90° Lateral Interior (Medial), Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level., Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 7: Cenital / Superior (90° Top-Down)
*Muestra vista plana superior completa: plantilla interior, cordones y lengüeta.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 4 Retro "She's A Star", SKU: IO2829-600. Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left. Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 4 Retro "She's A Star", IO2829-600, Cenital Superior 90°, Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left., Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

---

### [38] IV6811-001 — Air Jordan 1 Mid SE Black / Opti Yellow / Silver

**Foto de Referencia Primaria recomendada:** `dist/assets/2-norm-std/IV6811-001/01-lateral.webp`

#### Ángulo 1: Perfil Lateral Exterior (90°)
*Muestra silueta completa, logos principales y perfil de suela. Puntera a la izquierda.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 1 Mid SE Black / Opti Yellow / Silver, SKU: IV6811-001. Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole. Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 1 Mid SE Black / Opti Yellow / Silver, IV6811-001, 90° Lateral Exterior, Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole., Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 2: Perspectiva 3/4 Frontal (45°)
*Muestra volumen tridimensional, puntera y lateral exterior simultáneamente.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 1 Mid SE Black / Opti Yellow / Silver, SKU: IV6811-001. Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle. Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 1 Mid SE Black / Opti Yellow / Silver, IV6811-001, 3/4 Frontal Perspectiva, Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle., Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 3: Frontal Directa (0°)
*Muestra simetría de puntera, lengüeta, ancho de empeine y sistema de cordones.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 1 Mid SE Black / Opti Yellow / Silver, SKU: IV6811-001. Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker. Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 1 Mid SE Black / Opti Yellow / Silver, IV6811-001, Frontal Directa 0°, Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker., Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 4: Posterior / Talón (180°)
*Muestra contrafuerte del talón, logo de talón (Jumpman / Nike Air) y altura de caña.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 1 Mid SE Black / Opti Yellow / Silver, SKU: IV6811-001. Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level. Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 1 Mid SE Black / Opti Yellow / Silver, IV6811-001, Posterior Talón 180°, Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level., Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 5: Perspectiva 3/4 Trasera (135°)
*Muestra contorno del tobillo, talón tridimensional y curva posterior de entresuela.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 1 Mid SE Black / Opti Yellow / Silver, SKU: IV6811-001. Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front. Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 1 Mid SE Black / Opti Yellow / Silver, IV6811-001, 3/4 Trasera Exterior, Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front., Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 6: Perfil Lateral Interior / Medial (90°)
*Muestra el lado interno del pie, soporte del arco y patrón medial.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 1 Mid SE Black / Opti Yellow / Silver, SKU: IV6811-001. Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level. Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 1 Mid SE Black / Opti Yellow / Silver, IV6811-001, 90° Lateral Interior (Medial), Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level., Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 7: Cenital / Superior (90° Top-Down)
*Muestra vista plana superior completa: plantilla interior, cordones y lengüeta.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 1 Mid SE Black / Opti Yellow / Silver, SKU: IV6811-001. Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left. Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 1 Mid SE Black / Opti Yellow / Silver, IV6811-001, Cenital Superior 90°, Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left., Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

---

### [39] IR0519-600 — Jordan Son Of Mars Low Rojo Pasión / Neblina Gris / White / Black

**Foto de Referencia Primaria recomendada:** `dist/assets/2-norm-std/IR0519-600/01-lateral.webp`

#### Ángulo 1: Perfil Lateral Exterior (90°)
*Muestra silueta completa, logos principales y perfil de suela. Puntera a la izquierda.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Jordan Son Of Mars Low Rojo Pasión / Neblina Gris / White / Black, SKU: IR0519-600. Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole. Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Jordan Son Of Mars Low Rojo Pasión / Neblina Gris / White / Black, IR0519-600, 90° Lateral Exterior, Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole., Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 2: Perspectiva 3/4 Frontal (45°)
*Muestra volumen tridimensional, puntera y lateral exterior simultáneamente.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Jordan Son Of Mars Low Rojo Pasión / Neblina Gris / White / Black, SKU: IR0519-600. Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle. Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Jordan Son Of Mars Low Rojo Pasión / Neblina Gris / White / Black, IR0519-600, 3/4 Frontal Perspectiva, Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle., Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 3: Frontal Directa (0°)
*Muestra simetría de puntera, lengüeta, ancho de empeine y sistema de cordones.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Jordan Son Of Mars Low Rojo Pasión / Neblina Gris / White / Black, SKU: IR0519-600. Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker. Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Jordan Son Of Mars Low Rojo Pasión / Neblina Gris / White / Black, IR0519-600, Frontal Directa 0°, Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker., Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 4: Posterior / Talón (180°)
*Muestra contrafuerte del talón, logo de talón (Jumpman / Nike Air) y altura de caña.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Jordan Son Of Mars Low Rojo Pasión / Neblina Gris / White / Black, SKU: IR0519-600. Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level. Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Jordan Son Of Mars Low Rojo Pasión / Neblina Gris / White / Black, IR0519-600, Posterior Talón 180°, Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level., Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 5: Perspectiva 3/4 Trasera (135°)
*Muestra contorno del tobillo, talón tridimensional y curva posterior de entresuela.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Jordan Son Of Mars Low Rojo Pasión / Neblina Gris / White / Black, SKU: IR0519-600. Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front. Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Jordan Son Of Mars Low Rojo Pasión / Neblina Gris / White / Black, IR0519-600, 3/4 Trasera Exterior, Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front., Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 6: Perfil Lateral Interior / Medial (90°)
*Muestra el lado interno del pie, soporte del arco y patrón medial.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Jordan Son Of Mars Low Rojo Pasión / Neblina Gris / White / Black, SKU: IR0519-600. Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level. Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Jordan Son Of Mars Low Rojo Pasión / Neblina Gris / White / Black, IR0519-600, 90° Lateral Interior (Medial), Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level., Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 7: Cenital / Superior (90° Top-Down)
*Muestra vista plana superior completa: plantilla interior, cordones y lengüeta.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Jordan Son Of Mars Low Rojo Pasión / Neblina Gris / White / Black, SKU: IR0519-600. Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left. Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Jordan Son Of Mars Low Rojo Pasión / Neblina Gris / White / Black, IR0519-600, Cenital Superior 90°, Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left., Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

---

### [40] IW6277-001 — Air Jordan 1 Retro Low OG "Banned"

**Foto de Referencia Primaria recomendada:** `dist/assets/2-norm-std/IW6277-001/01-lateral.webp`

#### Ángulo 1: Perfil Lateral Exterior (90°)
*Muestra silueta completa, logos principales y perfil de suela. Puntera a la izquierda.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 1 Retro Low OG "Banned", SKU: IW6277-001. Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole. Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 1 Retro Low OG "Banned", IW6277-001, 90° Lateral Exterior, Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole., Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 2: Perspectiva 3/4 Frontal (45°)
*Muestra volumen tridimensional, puntera y lateral exterior simultáneamente.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 1 Retro Low OG "Banned", SKU: IW6277-001. Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle. Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 1 Retro Low OG "Banned", IW6277-001, 3/4 Frontal Perspectiva, Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle., Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 3: Frontal Directa (0°)
*Muestra simetría de puntera, lengüeta, ancho de empeine y sistema de cordones.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 1 Retro Low OG "Banned", SKU: IW6277-001. Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker. Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 1 Retro Low OG "Banned", IW6277-001, Frontal Directa 0°, Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker., Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 4: Posterior / Talón (180°)
*Muestra contrafuerte del talón, logo de talón (Jumpman / Nike Air) y altura de caña.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 1 Retro Low OG "Banned", SKU: IW6277-001. Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level. Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 1 Retro Low OG "Banned", IW6277-001, Posterior Talón 180°, Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level., Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 5: Perspectiva 3/4 Trasera (135°)
*Muestra contorno del tobillo, talón tridimensional y curva posterior de entresuela.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 1 Retro Low OG "Banned", SKU: IW6277-001. Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front. Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 1 Retro Low OG "Banned", IW6277-001, 3/4 Trasera Exterior, Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front., Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 6: Perfil Lateral Interior / Medial (90°)
*Muestra el lado interno del pie, soporte del arco y patrón medial.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 1 Retro Low OG "Banned", SKU: IW6277-001. Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level. Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 1 Retro Low OG "Banned", IW6277-001, 90° Lateral Interior (Medial), Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level., Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 7: Cenital / Superior (90° Top-Down)
*Muestra vista plana superior completa: plantilla interior, cordones y lengüeta.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Air Jordan 1 Retro Low OG "Banned", SKU: IW6277-001. Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left. Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Air Jordan 1 Retro Low OG "Banned", IW6277-001, Cenital Superior 90°, Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left., Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

---

### [41] IR0519-003 — Jordan Son Of Mars Low Black / University Red

**Foto de Referencia Primaria recomendada:** `dist/assets/2-norm-std/IR0519-003/01-lateral.webp`

#### Ángulo 1: Perfil Lateral Exterior (90°)
*Muestra silueta completa, logos principales y perfil de suela. Puntera a la izquierda.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Jordan Son Of Mars Low Black / University Red, SKU: IR0519-003. Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole. Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Jordan Son Of Mars Low Black / University Red, IR0519-003, 90° Lateral Exterior, Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole., Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 2: Perspectiva 3/4 Frontal (45°)
*Muestra volumen tridimensional, puntera y lateral exterior simultáneamente.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Jordan Son Of Mars Low Black / University Red, SKU: IR0519-003. Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle. Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Jordan Son Of Mars Low Black / University Red, IR0519-003, 3/4 Frontal Perspectiva, Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle., Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 3: Frontal Directa (0°)
*Muestra simetría de puntera, lengüeta, ancho de empeine y sistema de cordones.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Jordan Son Of Mars Low Black / University Red, SKU: IR0519-003. Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker. Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Jordan Son Of Mars Low Black / University Red, IR0519-003, Frontal Directa 0°, Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker., Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 4: Posterior / Talón (180°)
*Muestra contrafuerte del talón, logo de talón (Jumpman / Nike Air) y altura de caña.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Jordan Son Of Mars Low Black / University Red, SKU: IR0519-003. Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level. Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Jordan Son Of Mars Low Black / University Red, IR0519-003, Posterior Talón 180°, Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level., Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 5: Perspectiva 3/4 Trasera (135°)
*Muestra contorno del tobillo, talón tridimensional y curva posterior de entresuela.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Jordan Son Of Mars Low Black / University Red, SKU: IR0519-003. Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front. Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Jordan Son Of Mars Low Black / University Red, IR0519-003, 3/4 Trasera Exterior, Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front., Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 6: Perfil Lateral Interior / Medial (90°)
*Muestra el lado interno del pie, soporte del arco y patrón medial.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Jordan Son Of Mars Low Black / University Red, SKU: IR0519-003. Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level. Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Jordan Son Of Mars Low Black / University Red, IR0519-003, 90° Lateral Interior (Medial), Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level., Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 7: Cenital / Superior (90° Top-Down)
*Muestra vista plana superior completa: plantilla interior, cordones y lengüeta.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Jordan Son Of Mars Low Black / University Red, SKU: IR0519-003. Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left. Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Jordan Son Of Mars Low Black / University Red, IR0519-003, Cenital Superior 90°, Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left., Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

---

### [42] AQ9214-012 — Jordan Max Aura Cool Grey / Gym Red / Black / White

**Foto de Referencia Primaria recomendada:** `dist/assets/2-norm-std/AQ9214-012/01-lateral.webp`

#### Ángulo 1: Perfil Lateral Exterior (90°)
*Muestra silueta completa, logos principales y perfil de suela. Puntera a la izquierda.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Jordan Max Aura Cool Grey / Gym Red / Black / White, SKU: AQ9214-012. Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole. Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Jordan Max Aura Cool Grey / Gym Red / Black / White, AQ9214-012, 90° Lateral Exterior, Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole., Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 2: Perspectiva 3/4 Frontal (45°)
*Muestra volumen tridimensional, puntera y lateral exterior simultáneamente.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Jordan Max Aura Cool Grey / Gym Red / Black / White, SKU: AQ9214-012. Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle. Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Jordan Max Aura Cool Grey / Gym Red / Black / White, AQ9214-012, 3/4 Frontal Perspectiva, Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle., Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 3: Frontal Directa (0°)
*Muestra simetría de puntera, lengüeta, ancho de empeine y sistema de cordones.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Jordan Max Aura Cool Grey / Gym Red / Black / White, SKU: AQ9214-012. Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker. Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Jordan Max Aura Cool Grey / Gym Red / Black / White, AQ9214-012, Frontal Directa 0°, Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker., Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 4: Posterior / Talón (180°)
*Muestra contrafuerte del talón, logo de talón (Jumpman / Nike Air) y altura de caña.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Jordan Max Aura Cool Grey / Gym Red / Black / White, SKU: AQ9214-012. Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level. Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Jordan Max Aura Cool Grey / Gym Red / Black / White, AQ9214-012, Posterior Talón 180°, Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level., Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 5: Perspectiva 3/4 Trasera (135°)
*Muestra contorno del tobillo, talón tridimensional y curva posterior de entresuela.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Jordan Max Aura Cool Grey / Gym Red / Black / White, SKU: AQ9214-012. Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front. Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Jordan Max Aura Cool Grey / Gym Red / Black / White, AQ9214-012, 3/4 Trasera Exterior, Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front., Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 6: Perfil Lateral Interior / Medial (90°)
*Muestra el lado interno del pie, soporte del arco y patrón medial.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Jordan Max Aura Cool Grey / Gym Red / Black / White, SKU: AQ9214-012. Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level. Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Jordan Max Aura Cool Grey / Gym Red / Black / White, AQ9214-012, 90° Lateral Interior (Medial), Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level., Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 7: Cenital / Superior (90° Top-Down)
*Muestra vista plana superior completa: plantilla interior, cordones y lengüeta.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Jordan Max Aura Cool Grey / Gym Red / Black / White, SKU: AQ9214-012. Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left. Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Jordan Max Aura Cool Grey / Gym Red / Black / White, AQ9214-012, Cenital Superior 90°, Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left., Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

---

### [43] IB6644-001 — Nike Air Force 1 '07 Premium "Flowers"

**Foto de Referencia Primaria recomendada:** `dist/assets/2-norm-std/IB6644-001/01-lateral.webp`

#### Ángulo 1: Perfil Lateral Exterior (90°)
*Muestra silueta completa, logos principales y perfil de suela. Puntera a la izquierda.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Force 1 '07 Premium "Flowers", SKU: IB6644-001. Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole. Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Force 1 '07 Premium "Flowers", IB6644-001, 90° Lateral Exterior, Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole., Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 2: Perspectiva 3/4 Frontal (45°)
*Muestra volumen tridimensional, puntera y lateral exterior simultáneamente.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Force 1 '07 Premium "Flowers", SKU: IB6644-001. Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle. Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Force 1 '07 Premium "Flowers", IB6644-001, 3/4 Frontal Perspectiva, Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle., Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 3: Frontal Directa (0°)
*Muestra simetría de puntera, lengüeta, ancho de empeine y sistema de cordones.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Force 1 '07 Premium "Flowers", SKU: IB6644-001. Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker. Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Force 1 '07 Premium "Flowers", IB6644-001, Frontal Directa 0°, Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker., Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 4: Posterior / Talón (180°)
*Muestra contrafuerte del talón, logo de talón (Jumpman / Nike Air) y altura de caña.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Force 1 '07 Premium "Flowers", SKU: IB6644-001. Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level. Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Force 1 '07 Premium "Flowers", IB6644-001, Posterior Talón 180°, Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level., Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 5: Perspectiva 3/4 Trasera (135°)
*Muestra contorno del tobillo, talón tridimensional y curva posterior de entresuela.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Force 1 '07 Premium "Flowers", SKU: IB6644-001. Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front. Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Force 1 '07 Premium "Flowers", IB6644-001, 3/4 Trasera Exterior, Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front., Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 6: Perfil Lateral Interior / Medial (90°)
*Muestra el lado interno del pie, soporte del arco y patrón medial.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Force 1 '07 Premium "Flowers", SKU: IB6644-001. Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level. Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Force 1 '07 Premium "Flowers", IB6644-001, 90° Lateral Interior (Medial), Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level., Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 7: Cenital / Superior (90° Top-Down)
*Muestra vista plana superior completa: plantilla interior, cordones y lengüeta.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Force 1 '07 Premium "Flowers", SKU: IB6644-001. Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left. Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Force 1 '07 Premium "Flowers", IB6644-001, Cenital Superior 90°, Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left., Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

---

### [44] IM6969-451 — Nike Air Force 1 Obsidiana / Azul Difuso / Perla Suave / Aluminio

**Foto de Referencia Primaria recomendada:** `dist/assets/2-norm-std/IM6969-451/01-lateral.webp`

#### Ángulo 1: Perfil Lateral Exterior (90°)
*Muestra silueta completa, logos principales y perfil de suela. Puntera a la izquierda.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Force 1 Obsidiana / Azul Difuso / Perla Suave / Aluminio, SKU: IM6969-451. Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole. Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Force 1 Obsidiana / Azul Difuso / Perla Suave / Aluminio, IM6969-451, 90° Lateral Exterior, Strict 90-degree lateral outer profile side view of single left sneaker, toe box pointing horizontally directly to the LEFT, camera precisely at eye-level with the midsole., Showcasing the exterior brand logo, lateral upper stitching, midsole silhouette, and full outsole profile line., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 2: Perspectiva 3/4 Frontal (45°)
*Muestra volumen tridimensional, puntera y lateral exterior simultáneamente.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Force 1 Obsidiana / Azul Difuso / Perla Suave / Aluminio, SKU: IM6969-451. Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle. Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Force 1 Obsidiana / Azul Difuso / Perla Suave / Aluminio, IM6969-451, 3/4 Frontal Perspectiva, Three-quarter (3/4) perspective front-quarter three-quarter view of single left sneaker, angled toward the LEFT, camera elevated at a 25-degree dynamic product angle., Showcasing the front toe box cap, lateral curved lacing eyestay, tongue badge, and outer lateral panel volume simultaneously., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 3: Frontal Directa (0°)
*Muestra simetría de puntera, lengüeta, ancho de empeine y sistema de cordones.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Force 1 Obsidiana / Azul Difuso / Perla Suave / Aluminio, SKU: IM6969-451. Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker. Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Force 1 Obsidiana / Azul Difuso / Perla Suave / Aluminio, IM6969-451, Frontal Directa 0°, Direct straight-on front eye-level view at 0 degrees, perfectly centered along the vertical axis of the sneaker., Showcasing symmetrical rounded toe box perforation, neat lace row alignment, tongue brand embroidery, and dual collar openings., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 4: Posterior / Talón (180°)
*Muestra contrafuerte del talón, logo de talón (Jumpman / Nike Air) y altura de caña.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Force 1 Obsidiana / Azul Difuso / Perla Suave / Aluminio, SKU: IM6969-451. Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level. Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Force 1 Obsidiana / Azul Difuso / Perla Suave / Aluminio, IM6969-451, Posterior Talón 180°, Direct 180-degree straight rear view looking directly at the heel counter from behind, perfectly centered and level., Highlighting authentic rear branding badge, crisp heel stitch lines, padded heel notch collar, pull tab, and rear outsole tread wrap., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 5: Perspectiva 3/4 Trasera (135°)
*Muestra contorno del tobillo, talón tridimensional y curva posterior de entresuela.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Force 1 Obsidiana / Azul Difuso / Perla Suave / Aluminio, SKU: IM6969-451. Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front. Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Force 1 Obsidiana / Azul Difuso / Perla Suave / Aluminio, IM6969-451, 3/4 Trasera Exterior, Three-quarter (3/4) rear perspective view of single sneaker facing away toward the left, 135-degree angle from front., Highlighting heel counter curve, Achilles tendon collar curvature, outer rear midsole sculpting, and lateral heel logo perspective., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 6: Perfil Lateral Interior / Medial (90°)
*Muestra el lado interno del pie, soporte del arco y patrón medial.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Force 1 Obsidiana / Azul Difuso / Perla Suave / Aluminio, SKU: IM6969-451. Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level. Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Force 1 Obsidiana / Azul Difuso / Perla Suave / Aluminio, IM6969-451, 90° Lateral Interior (Medial), Strict 90-degree medial inner side profile view of single left sneaker, toe box pointing horizontally to the LEFT, camera at direct eye-level., Showcasing the inner arch support contour, medial upper stitch panels, inner midsole geometry, and medial venting., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

#### Ángulo 7: Cenital / Superior (90° Top-Down)
*Muestra vista plana superior completa: plantilla interior, cordones y lengüeta.*

**Prompt en Lenguaje Natural (Recomendado):**
```text
Commercial footwear catalog studio photography of authentic sneaker Nike Air Force 1 Obsidiana / Azul Difuso / Perla Suave / Aluminio, SKU: IM6969-451. Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left. Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo. Pure solid seamless white background (#FFFFFF), clean commercial studio environment. Even balanced dual softbox lighting at 5500K neutral daylight color temperature, eliminating harsh hotspots. Subtle grounded natural soft contact shadow directly underneath the outsole rubber on the floor plane. Shot with 85mm prime lens at f/8 aperture, razor-sharp edge-to-edge focus across all textures, deep depth of field with zero chromatic aberration. 8k UHD resolution, hyper-detailed commercial footwear catalog asset, single shoe isolated, no floating artifacts, no props, zero background distractions.
```

**Variante en Tags (Para Stable Diffusion / ComfyUI):**
```text
footwear product photography, Nike Air Force 1 Obsidiana / Azul Difuso / Perla Suave / Aluminio, IM6969-451, Cenital Superior 90°, Direct 90-degree overhead top-down flat lay cenital view looking straight down onto the sneaker, toe box oriented upward or to the left., Showcasing tongue branding tag, crisp eyelet symmetry, neatly tied flat laces, collar lining padding, and insole footbed printed logo., pure white background #FFFFFF, softbox studio lighting 5500K, grounded contact shadow, 85mm lens f8, pin-sharp detail, 8k resolution, e-commerce catalog
```

---

