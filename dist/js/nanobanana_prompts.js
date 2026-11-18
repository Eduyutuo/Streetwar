const nanoBananaCatalog = [
  {
    "index": 0,
    "sku": "IX6180-100",
    "name": "Air Jordan 9 Retro OG \"Space Jam\"",
    "primary_ref": "assets/2-norm-std/IX6180-100/01-lateral.webp",
    "formats": {
      "json_2x2": {
        "name": "Opción 1: JSON 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "JSON • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IX6180-100 --layout 2x2",
        "prompt": "{\n  \"task\": \"commercial_footwear_catalog_quad_sheet\",\n  \"product\": {\n    \"name\": \"Air Jordan 9 Retro OG \\\"Space Jam\\\"\",\n    \"sku\": \"IX6180-100\",\n    \"authentic\": true\n  },\n  \"layout\": {\n    \"type\": \"2x2_grid_contact_sheet\",\n    \"aspect_ratio\": \"1:1\",\n    \"background_color\": \"#FFFFFF\",\n    \"panels\": {\n      \"top_left\": \"90-degree lateral outer profile, toe pointing LEFT\",\n      \"top_right\": \"45-degree 3/4 perspective front-quarter, facing LEFT\",\n      \"bottom_left\": \"180-degree direct rear heel counter, centered\",\n      \"bottom_right\": \"90-degree overhead top-down flat lay view, laces and tongue\"\n    }\n  },\n  \"lighting\": \"neutral_softbox_5500k_studio\",\n  \"camera\": \"85mm_lens_f8_sharp_focus\",\n  \"output\": \"razor_sharp_focus_pure_white_background_subtle_contact_shadow\"\n}"
      },
      "json_1x3": {
        "name": "Opción 2: JSON 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9 o 4:3",
        "tag": "JSON • 16:9 / 4:3 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IX6180-100 --layout 1x3",
        "prompt": "{\n  \"style\": \"professional_sneaker_catalog\",\n  \"shoe\": \"Air Jordan 9 Retro OG \\\"Space Jam\\\"\",\n  \"sku\": \"IX6180-100\",\n  \"composition\": \"horizontal_triptych_three_equal_panels\",\n  \"aspect_ratio\": \"16:9_or_4:3\",\n  \"background\": \"seamless_solid_pure_white_#FFFFFF\",\n  \"views_left_to_right\": [\n    \"Panel 1: clean lateral outer profile view with toe pointing horizontally LEFT\",\n    \"Panel 2: direct 180-degree rear heel branding badge centered\",\n    \"Panel 3: direct 90-degree overhead top-down view showing laces and tongue\"\n  ],\n  \"render_quality\": \"8k_resolution_sharp_textures_dual_softbox_lighting\"\n}"
      },
      "text_2x2": {
        "name": "Opción 3: Texto Plano 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "Texto • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IX6180-100 --layout 2x2",
        "prompt": "Commercial footwear catalog 2x2 grid contact sheet of authentic sneaker Air Jordan 9 Retro OG \"Space Jam\", SKU: IX6180-100. Exactly 4 symmetrical panels on a seamless pure solid white background (#FFFFFF). Top-left panel: strict 90-degree lateral outer profile pointing LEFT. Top-right panel: three-quarter 3/4 perspective front-quarter facing LEFT. Bottom-left panel: direct 180-degree rear heel view centered. Bottom-right panel: direct 90-degree overhead top-down flat lay view. Identical studio softbox lighting at 5500K across all panels, subtle grounded contact shadows, razor-sharp focus across all textures, 85mm lens f/8, 8k resolution e-commerce standard, no human feet, no props."
      },
      "text_1x3": {
        "name": "Opción 4: Texto Plano 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9",
        "tag": "Texto • 16:9 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IX6180-100 --layout 1x3",
        "prompt": "Commercial footwear catalog triptych row showing exactly 3 side-by-side photographic views of the sneaker Air Jordan 9 Retro OG \"Space Jam\", SKU: IX6180-100 on a pure solid white background (#FFFFFF). Panel 1 (left): strict 90-degree lateral side profile pointing LEFT. Panel 2 (center): direct 180-degree rear heel counter view with branding badge. Panel 3 (right): direct 90-degree overhead top-down flat lay view showing laces and tongue. Uniform 5500K dual softbox lighting, razor-sharp details, subtle soft contact shadow on floor, clean commercial photography, no background clutter."
      }
    },
    "negative_prompt": "distorted logos, misspelled text, fake brand badges, asymmetrical deformed sole, warped eyelets, blurry laces, colored background, gradient background, shadows on walls, studio stands, human feet, legs, hands, mannequins, socks, dirty soles, worn leather, scuffs, lowres, oversaturated, chromatic aberration, cartoon, illustration, 3d render plastic sheen"
  },
  {
    "index": 1,
    "sku": "IO2076-100",
    "name": "Air Jordan 3 Retro \"Play Your Way\"",
    "primary_ref": "assets/2-norm-std/IO2076-100/01-lateral.webp",
    "formats": {
      "json_2x2": {
        "name": "Opción 1: JSON 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "JSON • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IO2076-100 --layout 2x2",
        "prompt": "{\n  \"task\": \"commercial_footwear_catalog_quad_sheet\",\n  \"product\": {\n    \"name\": \"Air Jordan 3 Retro \\\"Play Your Way\\\"\",\n    \"sku\": \"IO2076-100\",\n    \"authentic\": true\n  },\n  \"layout\": {\n    \"type\": \"2x2_grid_contact_sheet\",\n    \"aspect_ratio\": \"1:1\",\n    \"background_color\": \"#FFFFFF\",\n    \"panels\": {\n      \"top_left\": \"90-degree lateral outer profile, toe pointing LEFT\",\n      \"top_right\": \"45-degree 3/4 perspective front-quarter, facing LEFT\",\n      \"bottom_left\": \"180-degree direct rear heel counter, centered\",\n      \"bottom_right\": \"90-degree overhead top-down flat lay view, laces and tongue\"\n    }\n  },\n  \"lighting\": \"neutral_softbox_5500k_studio\",\n  \"camera\": \"85mm_lens_f8_sharp_focus\",\n  \"output\": \"razor_sharp_focus_pure_white_background_subtle_contact_shadow\"\n}"
      },
      "json_1x3": {
        "name": "Opción 2: JSON 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9 o 4:3",
        "tag": "JSON • 16:9 / 4:3 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IO2076-100 --layout 1x3",
        "prompt": "{\n  \"style\": \"professional_sneaker_catalog\",\n  \"shoe\": \"Air Jordan 3 Retro \\\"Play Your Way\\\"\",\n  \"sku\": \"IO2076-100\",\n  \"composition\": \"horizontal_triptych_three_equal_panels\",\n  \"aspect_ratio\": \"16:9_or_4:3\",\n  \"background\": \"seamless_solid_pure_white_#FFFFFF\",\n  \"views_left_to_right\": [\n    \"Panel 1: clean lateral outer profile view with toe pointing horizontally LEFT\",\n    \"Panel 2: direct 180-degree rear heel branding badge centered\",\n    \"Panel 3: direct 90-degree overhead top-down view showing laces and tongue\"\n  ],\n  \"render_quality\": \"8k_resolution_sharp_textures_dual_softbox_lighting\"\n}"
      },
      "text_2x2": {
        "name": "Opción 3: Texto Plano 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "Texto • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IO2076-100 --layout 2x2",
        "prompt": "Commercial footwear catalog 2x2 grid contact sheet of authentic sneaker Air Jordan 3 Retro \"Play Your Way\", SKU: IO2076-100. Exactly 4 symmetrical panels on a seamless pure solid white background (#FFFFFF). Top-left panel: strict 90-degree lateral outer profile pointing LEFT. Top-right panel: three-quarter 3/4 perspective front-quarter facing LEFT. Bottom-left panel: direct 180-degree rear heel view centered. Bottom-right panel: direct 90-degree overhead top-down flat lay view. Identical studio softbox lighting at 5500K across all panels, subtle grounded contact shadows, razor-sharp focus across all textures, 85mm lens f/8, 8k resolution e-commerce standard, no human feet, no props."
      },
      "text_1x3": {
        "name": "Opción 4: Texto Plano 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9",
        "tag": "Texto • 16:9 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IO2076-100 --layout 1x3",
        "prompt": "Commercial footwear catalog triptych row showing exactly 3 side-by-side photographic views of the sneaker Air Jordan 3 Retro \"Play Your Way\", SKU: IO2076-100 on a pure solid white background (#FFFFFF). Panel 1 (left): strict 90-degree lateral side profile pointing LEFT. Panel 2 (center): direct 180-degree rear heel counter view with branding badge. Panel 3 (right): direct 90-degree overhead top-down flat lay view showing laces and tongue. Uniform 5500K dual softbox lighting, razor-sharp details, subtle soft contact shadow on floor, clean commercial photography, no background clutter."
      }
    },
    "negative_prompt": "distorted logos, misspelled text, fake brand badges, asymmetrical deformed sole, warped eyelets, blurry laces, colored background, gradient background, shadows on walls, studio stands, human feet, legs, hands, mannequins, socks, dirty soles, worn leather, scuffs, lowres, oversaturated, chromatic aberration, cartoon, illustration, 3d render plastic sheen"
  },
  {
    "index": 2,
    "sku": "AQ9214-006",
    "name": "Jordan Max Aura Black / Black / Gym Red",
    "primary_ref": "assets/2-norm-std/AQ9214-006/01-lateral.webp",
    "formats": {
      "json_2x2": {
        "name": "Opción 1: JSON 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "JSON • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku AQ9214-006 --layout 2x2",
        "prompt": "{\n  \"task\": \"commercial_footwear_catalog_quad_sheet\",\n  \"product\": {\n    \"name\": \"Jordan Max Aura Black / Black / Gym Red\",\n    \"sku\": \"AQ9214-006\",\n    \"authentic\": true\n  },\n  \"layout\": {\n    \"type\": \"2x2_grid_contact_sheet\",\n    \"aspect_ratio\": \"1:1\",\n    \"background_color\": \"#FFFFFF\",\n    \"panels\": {\n      \"top_left\": \"90-degree lateral outer profile, toe pointing LEFT\",\n      \"top_right\": \"45-degree 3/4 perspective front-quarter, facing LEFT\",\n      \"bottom_left\": \"180-degree direct rear heel counter, centered\",\n      \"bottom_right\": \"90-degree overhead top-down flat lay view, laces and tongue\"\n    }\n  },\n  \"lighting\": \"neutral_softbox_5500k_studio\",\n  \"camera\": \"85mm_lens_f8_sharp_focus\",\n  \"output\": \"razor_sharp_focus_pure_white_background_subtle_contact_shadow\"\n}"
      },
      "json_1x3": {
        "name": "Opción 2: JSON 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9 o 4:3",
        "tag": "JSON • 16:9 / 4:3 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku AQ9214-006 --layout 1x3",
        "prompt": "{\n  \"style\": \"professional_sneaker_catalog\",\n  \"shoe\": \"Jordan Max Aura Black / Black / Gym Red\",\n  \"sku\": \"AQ9214-006\",\n  \"composition\": \"horizontal_triptych_three_equal_panels\",\n  \"aspect_ratio\": \"16:9_or_4:3\",\n  \"background\": \"seamless_solid_pure_white_#FFFFFF\",\n  \"views_left_to_right\": [\n    \"Panel 1: clean lateral outer profile view with toe pointing horizontally LEFT\",\n    \"Panel 2: direct 180-degree rear heel branding badge centered\",\n    \"Panel 3: direct 90-degree overhead top-down view showing laces and tongue\"\n  ],\n  \"render_quality\": \"8k_resolution_sharp_textures_dual_softbox_lighting\"\n}"
      },
      "text_2x2": {
        "name": "Opción 3: Texto Plano 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "Texto • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku AQ9214-006 --layout 2x2",
        "prompt": "Commercial footwear catalog 2x2 grid contact sheet of authentic sneaker Jordan Max Aura Black / Black / Gym Red, SKU: AQ9214-006. Exactly 4 symmetrical panels on a seamless pure solid white background (#FFFFFF). Top-left panel: strict 90-degree lateral outer profile pointing LEFT. Top-right panel: three-quarter 3/4 perspective front-quarter facing LEFT. Bottom-left panel: direct 180-degree rear heel view centered. Bottom-right panel: direct 90-degree overhead top-down flat lay view. Identical studio softbox lighting at 5500K across all panels, subtle grounded contact shadows, razor-sharp focus across all textures, 85mm lens f/8, 8k resolution e-commerce standard, no human feet, no props."
      },
      "text_1x3": {
        "name": "Opción 4: Texto Plano 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9",
        "tag": "Texto • 16:9 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku AQ9214-006 --layout 1x3",
        "prompt": "Commercial footwear catalog triptych row showing exactly 3 side-by-side photographic views of the sneaker Jordan Max Aura Black / Black / Gym Red, SKU: AQ9214-006 on a pure solid white background (#FFFFFF). Panel 1 (left): strict 90-degree lateral side profile pointing LEFT. Panel 2 (center): direct 180-degree rear heel counter view with branding badge. Panel 3 (right): direct 90-degree overhead top-down flat lay view showing laces and tongue. Uniform 5500K dual softbox lighting, razor-sharp details, subtle soft contact shadow on floor, clean commercial photography, no background clutter."
      }
    },
    "negative_prompt": "distorted logos, misspelled text, fake brand badges, asymmetrical deformed sole, warped eyelets, blurry laces, colored background, gradient background, shadows on walls, studio stands, human feet, legs, hands, mannequins, socks, dirty soles, worn leather, scuffs, lowres, oversaturated, chromatic aberration, cartoon, illustration, 3d render plastic sheen"
  },
  {
    "index": 3,
    "sku": "HF7054-012",
    "name": "Nike Air Max 95 White / Pink / Brown",
    "primary_ref": "assets/2-norm-std/HF7054-012/01-lateral.webp",
    "formats": {
      "json_2x2": {
        "name": "Opción 1: JSON 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "JSON • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku HF7054-012 --layout 2x2",
        "prompt": "{\n  \"task\": \"commercial_footwear_catalog_quad_sheet\",\n  \"product\": {\n    \"name\": \"Nike Air Max 95 White / Pink / Brown\",\n    \"sku\": \"HF7054-012\",\n    \"authentic\": true\n  },\n  \"layout\": {\n    \"type\": \"2x2_grid_contact_sheet\",\n    \"aspect_ratio\": \"1:1\",\n    \"background_color\": \"#FFFFFF\",\n    \"panels\": {\n      \"top_left\": \"90-degree lateral outer profile, toe pointing LEFT\",\n      \"top_right\": \"45-degree 3/4 perspective front-quarter, facing LEFT\",\n      \"bottom_left\": \"180-degree direct rear heel counter, centered\",\n      \"bottom_right\": \"90-degree overhead top-down flat lay view, laces and tongue\"\n    }\n  },\n  \"lighting\": \"neutral_softbox_5500k_studio\",\n  \"camera\": \"85mm_lens_f8_sharp_focus\",\n  \"output\": \"razor_sharp_focus_pure_white_background_subtle_contact_shadow\"\n}"
      },
      "json_1x3": {
        "name": "Opción 2: JSON 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9 o 4:3",
        "tag": "JSON • 16:9 / 4:3 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku HF7054-012 --layout 1x3",
        "prompt": "{\n  \"style\": \"professional_sneaker_catalog\",\n  \"shoe\": \"Nike Air Max 95 White / Pink / Brown\",\n  \"sku\": \"HF7054-012\",\n  \"composition\": \"horizontal_triptych_three_equal_panels\",\n  \"aspect_ratio\": \"16:9_or_4:3\",\n  \"background\": \"seamless_solid_pure_white_#FFFFFF\",\n  \"views_left_to_right\": [\n    \"Panel 1: clean lateral outer profile view with toe pointing horizontally LEFT\",\n    \"Panel 2: direct 180-degree rear heel branding badge centered\",\n    \"Panel 3: direct 90-degree overhead top-down view showing laces and tongue\"\n  ],\n  \"render_quality\": \"8k_resolution_sharp_textures_dual_softbox_lighting\"\n}"
      },
      "text_2x2": {
        "name": "Opción 3: Texto Plano 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "Texto • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku HF7054-012 --layout 2x2",
        "prompt": "Commercial footwear catalog 2x2 grid contact sheet of authentic sneaker Nike Air Max 95 White / Pink / Brown, SKU: HF7054-012. Exactly 4 symmetrical panels on a seamless pure solid white background (#FFFFFF). Top-left panel: strict 90-degree lateral outer profile pointing LEFT. Top-right panel: three-quarter 3/4 perspective front-quarter facing LEFT. Bottom-left panel: direct 180-degree rear heel view centered. Bottom-right panel: direct 90-degree overhead top-down flat lay view. Identical studio softbox lighting at 5500K across all panels, subtle grounded contact shadows, razor-sharp focus across all textures, 85mm lens f/8, 8k resolution e-commerce standard, no human feet, no props."
      },
      "text_1x3": {
        "name": "Opción 4: Texto Plano 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9",
        "tag": "Texto • 16:9 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku HF7054-012 --layout 1x3",
        "prompt": "Commercial footwear catalog triptych row showing exactly 3 side-by-side photographic views of the sneaker Nike Air Max 95 White / Pink / Brown, SKU: HF7054-012 on a pure solid white background (#FFFFFF). Panel 1 (left): strict 90-degree lateral side profile pointing LEFT. Panel 2 (center): direct 180-degree rear heel counter view with branding badge. Panel 3 (right): direct 90-degree overhead top-down flat lay view showing laces and tongue. Uniform 5500K dual softbox lighting, razor-sharp details, subtle soft contact shadow on floor, clean commercial photography, no background clutter."
      }
    },
    "negative_prompt": "distorted logos, misspelled text, fake brand badges, asymmetrical deformed sole, warped eyelets, blurry laces, colored background, gradient background, shadows on walls, studio stands, human feet, legs, hands, mannequins, socks, dirty soles, worn leather, scuffs, lowres, oversaturated, chromatic aberration, cartoon, illustration, 3d render plastic sheen"
  },
  {
    "index": 4,
    "sku": "BQ4212-002",
    "name": "Nike Flight Legacy Black / White",
    "primary_ref": "assets/2-norm-std/BQ4212-002/01-lateral.webp",
    "formats": {
      "json_2x2": {
        "name": "Opción 1: JSON 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "JSON • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku BQ4212-002 --layout 2x2",
        "prompt": "{\n  \"task\": \"commercial_footwear_catalog_quad_sheet\",\n  \"product\": {\n    \"name\": \"Nike Flight Legacy Black / White\",\n    \"sku\": \"BQ4212-002\",\n    \"authentic\": true\n  },\n  \"layout\": {\n    \"type\": \"2x2_grid_contact_sheet\",\n    \"aspect_ratio\": \"1:1\",\n    \"background_color\": \"#FFFFFF\",\n    \"panels\": {\n      \"top_left\": \"90-degree lateral outer profile, toe pointing LEFT\",\n      \"top_right\": \"45-degree 3/4 perspective front-quarter, facing LEFT\",\n      \"bottom_left\": \"180-degree direct rear heel counter, centered\",\n      \"bottom_right\": \"90-degree overhead top-down flat lay view, laces and tongue\"\n    }\n  },\n  \"lighting\": \"neutral_softbox_5500k_studio\",\n  \"camera\": \"85mm_lens_f8_sharp_focus\",\n  \"output\": \"razor_sharp_focus_pure_white_background_subtle_contact_shadow\"\n}"
      },
      "json_1x3": {
        "name": "Opción 2: JSON 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9 o 4:3",
        "tag": "JSON • 16:9 / 4:3 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku BQ4212-002 --layout 1x3",
        "prompt": "{\n  \"style\": \"professional_sneaker_catalog\",\n  \"shoe\": \"Nike Flight Legacy Black / White\",\n  \"sku\": \"BQ4212-002\",\n  \"composition\": \"horizontal_triptych_three_equal_panels\",\n  \"aspect_ratio\": \"16:9_or_4:3\",\n  \"background\": \"seamless_solid_pure_white_#FFFFFF\",\n  \"views_left_to_right\": [\n    \"Panel 1: clean lateral outer profile view with toe pointing horizontally LEFT\",\n    \"Panel 2: direct 180-degree rear heel branding badge centered\",\n    \"Panel 3: direct 90-degree overhead top-down view showing laces and tongue\"\n  ],\n  \"render_quality\": \"8k_resolution_sharp_textures_dual_softbox_lighting\"\n}"
      },
      "text_2x2": {
        "name": "Opción 3: Texto Plano 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "Texto • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku BQ4212-002 --layout 2x2",
        "prompt": "Commercial footwear catalog 2x2 grid contact sheet of authentic sneaker Nike Flight Legacy Black / White, SKU: BQ4212-002. Exactly 4 symmetrical panels on a seamless pure solid white background (#FFFFFF). Top-left panel: strict 90-degree lateral outer profile pointing LEFT. Top-right panel: three-quarter 3/4 perspective front-quarter facing LEFT. Bottom-left panel: direct 180-degree rear heel view centered. Bottom-right panel: direct 90-degree overhead top-down flat lay view. Identical studio softbox lighting at 5500K across all panels, subtle grounded contact shadows, razor-sharp focus across all textures, 85mm lens f/8, 8k resolution e-commerce standard, no human feet, no props."
      },
      "text_1x3": {
        "name": "Opción 4: Texto Plano 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9",
        "tag": "Texto • 16:9 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku BQ4212-002 --layout 1x3",
        "prompt": "Commercial footwear catalog triptych row showing exactly 3 side-by-side photographic views of the sneaker Nike Flight Legacy Black / White, SKU: BQ4212-002 on a pure solid white background (#FFFFFF). Panel 1 (left): strict 90-degree lateral side profile pointing LEFT. Panel 2 (center): direct 180-degree rear heel counter view with branding badge. Panel 3 (right): direct 90-degree overhead top-down flat lay view showing laces and tongue. Uniform 5500K dual softbox lighting, razor-sharp details, subtle soft contact shadow on floor, clean commercial photography, no background clutter."
      }
    },
    "negative_prompt": "distorted logos, misspelled text, fake brand badges, asymmetrical deformed sole, warped eyelets, blurry laces, colored background, gradient background, shadows on walls, studio stands, human feet, legs, hands, mannequins, socks, dirty soles, worn leather, scuffs, lowres, oversaturated, chromatic aberration, cartoon, illustration, 3d render plastic sheen"
  },
  {
    "index": 5,
    "sku": "694862-200",
    "name": "Nike Air Max Command Premium Light Taupe",
    "primary_ref": "assets/2-norm-std/694862-200/01-lateral.webp",
    "formats": {
      "json_2x2": {
        "name": "Opción 1: JSON 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "JSON • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku 694862-200 --layout 2x2",
        "prompt": "{\n  \"task\": \"commercial_footwear_catalog_quad_sheet\",\n  \"product\": {\n    \"name\": \"Nike Air Max Command Premium Light Taupe\",\n    \"sku\": \"694862-200\",\n    \"authentic\": true\n  },\n  \"layout\": {\n    \"type\": \"2x2_grid_contact_sheet\",\n    \"aspect_ratio\": \"1:1\",\n    \"background_color\": \"#FFFFFF\",\n    \"panels\": {\n      \"top_left\": \"90-degree lateral outer profile, toe pointing LEFT\",\n      \"top_right\": \"45-degree 3/4 perspective front-quarter, facing LEFT\",\n      \"bottom_left\": \"180-degree direct rear heel counter, centered\",\n      \"bottom_right\": \"90-degree overhead top-down flat lay view, laces and tongue\"\n    }\n  },\n  \"lighting\": \"neutral_softbox_5500k_studio\",\n  \"camera\": \"85mm_lens_f8_sharp_focus\",\n  \"output\": \"razor_sharp_focus_pure_white_background_subtle_contact_shadow\"\n}"
      },
      "json_1x3": {
        "name": "Opción 2: JSON 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9 o 4:3",
        "tag": "JSON • 16:9 / 4:3 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku 694862-200 --layout 1x3",
        "prompt": "{\n  \"style\": \"professional_sneaker_catalog\",\n  \"shoe\": \"Nike Air Max Command Premium Light Taupe\",\n  \"sku\": \"694862-200\",\n  \"composition\": \"horizontal_triptych_three_equal_panels\",\n  \"aspect_ratio\": \"16:9_or_4:3\",\n  \"background\": \"seamless_solid_pure_white_#FFFFFF\",\n  \"views_left_to_right\": [\n    \"Panel 1: clean lateral outer profile view with toe pointing horizontally LEFT\",\n    \"Panel 2: direct 180-degree rear heel branding badge centered\",\n    \"Panel 3: direct 90-degree overhead top-down view showing laces and tongue\"\n  ],\n  \"render_quality\": \"8k_resolution_sharp_textures_dual_softbox_lighting\"\n}"
      },
      "text_2x2": {
        "name": "Opción 3: Texto Plano 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "Texto • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku 694862-200 --layout 2x2",
        "prompt": "Commercial footwear catalog 2x2 grid contact sheet of authentic sneaker Nike Air Max Command Premium Light Taupe, SKU: 694862-200. Exactly 4 symmetrical panels on a seamless pure solid white background (#FFFFFF). Top-left panel: strict 90-degree lateral outer profile pointing LEFT. Top-right panel: three-quarter 3/4 perspective front-quarter facing LEFT. Bottom-left panel: direct 180-degree rear heel view centered. Bottom-right panel: direct 90-degree overhead top-down flat lay view. Identical studio softbox lighting at 5500K across all panels, subtle grounded contact shadows, razor-sharp focus across all textures, 85mm lens f/8, 8k resolution e-commerce standard, no human feet, no props."
      },
      "text_1x3": {
        "name": "Opción 4: Texto Plano 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9",
        "tag": "Texto • 16:9 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku 694862-200 --layout 1x3",
        "prompt": "Commercial footwear catalog triptych row showing exactly 3 side-by-side photographic views of the sneaker Nike Air Max Command Premium Light Taupe, SKU: 694862-200 on a pure solid white background (#FFFFFF). Panel 1 (left): strict 90-degree lateral side profile pointing LEFT. Panel 2 (center): direct 180-degree rear heel counter view with branding badge. Panel 3 (right): direct 90-degree overhead top-down flat lay view showing laces and tongue. Uniform 5500K dual softbox lighting, razor-sharp details, subtle soft contact shadow on floor, clean commercial photography, no background clutter."
      }
    },
    "negative_prompt": "distorted logos, misspelled text, fake brand badges, asymmetrical deformed sole, warped eyelets, blurry laces, colored background, gradient background, shadows on walls, studio stands, human feet, legs, hands, mannequins, socks, dirty soles, worn leather, scuffs, lowres, oversaturated, chromatic aberration, cartoon, illustration, 3d render plastic sheen"
  },
  {
    "index": 6,
    "sku": "511416-011",
    "name": "Nike Air Max Correlate Black / White / Grey",
    "primary_ref": "assets/2-norm-std/511416-011/01-lateral.webp",
    "formats": {
      "json_2x2": {
        "name": "Opción 1: JSON 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "JSON • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku 511416-011 --layout 2x2",
        "prompt": "{\n  \"task\": \"commercial_footwear_catalog_quad_sheet\",\n  \"product\": {\n    \"name\": \"Nike Air Max Correlate Black / White / Grey\",\n    \"sku\": \"511416-011\",\n    \"authentic\": true\n  },\n  \"layout\": {\n    \"type\": \"2x2_grid_contact_sheet\",\n    \"aspect_ratio\": \"1:1\",\n    \"background_color\": \"#FFFFFF\",\n    \"panels\": {\n      \"top_left\": \"90-degree lateral outer profile, toe pointing LEFT\",\n      \"top_right\": \"45-degree 3/4 perspective front-quarter, facing LEFT\",\n      \"bottom_left\": \"180-degree direct rear heel counter, centered\",\n      \"bottom_right\": \"90-degree overhead top-down flat lay view, laces and tongue\"\n    }\n  },\n  \"lighting\": \"neutral_softbox_5500k_studio\",\n  \"camera\": \"85mm_lens_f8_sharp_focus\",\n  \"output\": \"razor_sharp_focus_pure_white_background_subtle_contact_shadow\"\n}"
      },
      "json_1x3": {
        "name": "Opción 2: JSON 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9 o 4:3",
        "tag": "JSON • 16:9 / 4:3 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku 511416-011 --layout 1x3",
        "prompt": "{\n  \"style\": \"professional_sneaker_catalog\",\n  \"shoe\": \"Nike Air Max Correlate Black / White / Grey\",\n  \"sku\": \"511416-011\",\n  \"composition\": \"horizontal_triptych_three_equal_panels\",\n  \"aspect_ratio\": \"16:9_or_4:3\",\n  \"background\": \"seamless_solid_pure_white_#FFFFFF\",\n  \"views_left_to_right\": [\n    \"Panel 1: clean lateral outer profile view with toe pointing horizontally LEFT\",\n    \"Panel 2: direct 180-degree rear heel branding badge centered\",\n    \"Panel 3: direct 90-degree overhead top-down view showing laces and tongue\"\n  ],\n  \"render_quality\": \"8k_resolution_sharp_textures_dual_softbox_lighting\"\n}"
      },
      "text_2x2": {
        "name": "Opción 3: Texto Plano 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "Texto • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku 511416-011 --layout 2x2",
        "prompt": "Commercial footwear catalog 2x2 grid contact sheet of authentic sneaker Nike Air Max Correlate Black / White / Grey, SKU: 511416-011. Exactly 4 symmetrical panels on a seamless pure solid white background (#FFFFFF). Top-left panel: strict 90-degree lateral outer profile pointing LEFT. Top-right panel: three-quarter 3/4 perspective front-quarter facing LEFT. Bottom-left panel: direct 180-degree rear heel view centered. Bottom-right panel: direct 90-degree overhead top-down flat lay view. Identical studio softbox lighting at 5500K across all panels, subtle grounded contact shadows, razor-sharp focus across all textures, 85mm lens f/8, 8k resolution e-commerce standard, no human feet, no props."
      },
      "text_1x3": {
        "name": "Opción 4: Texto Plano 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9",
        "tag": "Texto • 16:9 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku 511416-011 --layout 1x3",
        "prompt": "Commercial footwear catalog triptych row showing exactly 3 side-by-side photographic views of the sneaker Nike Air Max Correlate Black / White / Grey, SKU: 511416-011 on a pure solid white background (#FFFFFF). Panel 1 (left): strict 90-degree lateral side profile pointing LEFT. Panel 2 (center): direct 180-degree rear heel counter view with branding badge. Panel 3 (right): direct 90-degree overhead top-down flat lay view showing laces and tongue. Uniform 5500K dual softbox lighting, razor-sharp details, subtle soft contact shadow on floor, clean commercial photography, no background clutter."
      }
    },
    "negative_prompt": "distorted logos, misspelled text, fake brand badges, asymmetrical deformed sole, warped eyelets, blurry laces, colored background, gradient background, shadows on walls, studio stands, human feet, legs, hands, mannequins, socks, dirty soles, worn leather, scuffs, lowres, oversaturated, chromatic aberration, cartoon, illustration, 3d render plastic sheen"
  },
  {
    "index": 7,
    "sku": "IR0519-101",
    "name": "Jordan Son of Mars Low White / Red / Black",
    "primary_ref": "assets/2-norm-std/IR0519-101/01-lateral.webp",
    "formats": {
      "json_2x2": {
        "name": "Opción 1: JSON 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "JSON • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IR0519-101 --layout 2x2",
        "prompt": "{\n  \"task\": \"commercial_footwear_catalog_quad_sheet\",\n  \"product\": {\n    \"name\": \"Jordan Son of Mars Low White / Red / Black\",\n    \"sku\": \"IR0519-101\",\n    \"authentic\": true\n  },\n  \"layout\": {\n    \"type\": \"2x2_grid_contact_sheet\",\n    \"aspect_ratio\": \"1:1\",\n    \"background_color\": \"#FFFFFF\",\n    \"panels\": {\n      \"top_left\": \"90-degree lateral outer profile, toe pointing LEFT\",\n      \"top_right\": \"45-degree 3/4 perspective front-quarter, facing LEFT\",\n      \"bottom_left\": \"180-degree direct rear heel counter, centered\",\n      \"bottom_right\": \"90-degree overhead top-down flat lay view, laces and tongue\"\n    }\n  },\n  \"lighting\": \"neutral_softbox_5500k_studio\",\n  \"camera\": \"85mm_lens_f8_sharp_focus\",\n  \"output\": \"razor_sharp_focus_pure_white_background_subtle_contact_shadow\"\n}"
      },
      "json_1x3": {
        "name": "Opción 2: JSON 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9 o 4:3",
        "tag": "JSON • 16:9 / 4:3 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IR0519-101 --layout 1x3",
        "prompt": "{\n  \"style\": \"professional_sneaker_catalog\",\n  \"shoe\": \"Jordan Son of Mars Low White / Red / Black\",\n  \"sku\": \"IR0519-101\",\n  \"composition\": \"horizontal_triptych_three_equal_panels\",\n  \"aspect_ratio\": \"16:9_or_4:3\",\n  \"background\": \"seamless_solid_pure_white_#FFFFFF\",\n  \"views_left_to_right\": [\n    \"Panel 1: clean lateral outer profile view with toe pointing horizontally LEFT\",\n    \"Panel 2: direct 180-degree rear heel branding badge centered\",\n    \"Panel 3: direct 90-degree overhead top-down view showing laces and tongue\"\n  ],\n  \"render_quality\": \"8k_resolution_sharp_textures_dual_softbox_lighting\"\n}"
      },
      "text_2x2": {
        "name": "Opción 3: Texto Plano 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "Texto • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IR0519-101 --layout 2x2",
        "prompt": "Commercial footwear catalog 2x2 grid contact sheet of authentic sneaker Jordan Son of Mars Low White / Red / Black, SKU: IR0519-101. Exactly 4 symmetrical panels on a seamless pure solid white background (#FFFFFF). Top-left panel: strict 90-degree lateral outer profile pointing LEFT. Top-right panel: three-quarter 3/4 perspective front-quarter facing LEFT. Bottom-left panel: direct 180-degree rear heel view centered. Bottom-right panel: direct 90-degree overhead top-down flat lay view. Identical studio softbox lighting at 5500K across all panels, subtle grounded contact shadows, razor-sharp focus across all textures, 85mm lens f/8, 8k resolution e-commerce standard, no human feet, no props."
      },
      "text_1x3": {
        "name": "Opción 4: Texto Plano 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9",
        "tag": "Texto • 16:9 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IR0519-101 --layout 1x3",
        "prompt": "Commercial footwear catalog triptych row showing exactly 3 side-by-side photographic views of the sneaker Jordan Son of Mars Low White / Red / Black, SKU: IR0519-101 on a pure solid white background (#FFFFFF). Panel 1 (left): strict 90-degree lateral side profile pointing LEFT. Panel 2 (center): direct 180-degree rear heel counter view with branding badge. Panel 3 (right): direct 90-degree overhead top-down flat lay view showing laces and tongue. Uniform 5500K dual softbox lighting, razor-sharp details, subtle soft contact shadow on floor, clean commercial photography, no background clutter."
      }
    },
    "negative_prompt": "distorted logos, misspelled text, fake brand badges, asymmetrical deformed sole, warped eyelets, blurry laces, colored background, gradient background, shadows on walls, studio stands, human feet, legs, hands, mannequins, socks, dirty soles, worn leather, scuffs, lowres, oversaturated, chromatic aberration, cartoon, illustration, 3d render plastic sheen"
  },
  {
    "index": 8,
    "sku": "IQ0205-100",
    "name": "Nike Air Force 1 '07 Black / White / Orange Peel",
    "primary_ref": "assets/2-norm-std/IQ0205-100/01-lateral.webp",
    "formats": {
      "json_2x2": {
        "name": "Opción 1: JSON 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "JSON • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IQ0205-100 --layout 2x2",
        "prompt": "{\n  \"task\": \"commercial_footwear_catalog_quad_sheet\",\n  \"product\": {\n    \"name\": \"Nike Air Force 1 '07 Black / White / Orange Peel\",\n    \"sku\": \"IQ0205-100\",\n    \"authentic\": true\n  },\n  \"layout\": {\n    \"type\": \"2x2_grid_contact_sheet\",\n    \"aspect_ratio\": \"1:1\",\n    \"background_color\": \"#FFFFFF\",\n    \"panels\": {\n      \"top_left\": \"90-degree lateral outer profile, toe pointing LEFT\",\n      \"top_right\": \"45-degree 3/4 perspective front-quarter, facing LEFT\",\n      \"bottom_left\": \"180-degree direct rear heel counter, centered\",\n      \"bottom_right\": \"90-degree overhead top-down flat lay view, laces and tongue\"\n    }\n  },\n  \"lighting\": \"neutral_softbox_5500k_studio\",\n  \"camera\": \"85mm_lens_f8_sharp_focus\",\n  \"output\": \"razor_sharp_focus_pure_white_background_subtle_contact_shadow\"\n}"
      },
      "json_1x3": {
        "name": "Opción 2: JSON 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9 o 4:3",
        "tag": "JSON • 16:9 / 4:3 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IQ0205-100 --layout 1x3",
        "prompt": "{\n  \"style\": \"professional_sneaker_catalog\",\n  \"shoe\": \"Nike Air Force 1 '07 Black / White / Orange Peel\",\n  \"sku\": \"IQ0205-100\",\n  \"composition\": \"horizontal_triptych_three_equal_panels\",\n  \"aspect_ratio\": \"16:9_or_4:3\",\n  \"background\": \"seamless_solid_pure_white_#FFFFFF\",\n  \"views_left_to_right\": [\n    \"Panel 1: clean lateral outer profile view with toe pointing horizontally LEFT\",\n    \"Panel 2: direct 180-degree rear heel branding badge centered\",\n    \"Panel 3: direct 90-degree overhead top-down view showing laces and tongue\"\n  ],\n  \"render_quality\": \"8k_resolution_sharp_textures_dual_softbox_lighting\"\n}"
      },
      "text_2x2": {
        "name": "Opción 3: Texto Plano 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "Texto • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IQ0205-100 --layout 2x2",
        "prompt": "Commercial footwear catalog 2x2 grid contact sheet of authentic sneaker Nike Air Force 1 '07 Black / White / Orange Peel, SKU: IQ0205-100. Exactly 4 symmetrical panels on a seamless pure solid white background (#FFFFFF). Top-left panel: strict 90-degree lateral outer profile pointing LEFT. Top-right panel: three-quarter 3/4 perspective front-quarter facing LEFT. Bottom-left panel: direct 180-degree rear heel view centered. Bottom-right panel: direct 90-degree overhead top-down flat lay view. Identical studio softbox lighting at 5500K across all panels, subtle grounded contact shadows, razor-sharp focus across all textures, 85mm lens f/8, 8k resolution e-commerce standard, no human feet, no props."
      },
      "text_1x3": {
        "name": "Opción 4: Texto Plano 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9",
        "tag": "Texto • 16:9 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IQ0205-100 --layout 1x3",
        "prompt": "Commercial footwear catalog triptych row showing exactly 3 side-by-side photographic views of the sneaker Nike Air Force 1 '07 Black / White / Orange Peel, SKU: IQ0205-100 on a pure solid white background (#FFFFFF). Panel 1 (left): strict 90-degree lateral side profile pointing LEFT. Panel 2 (center): direct 180-degree rear heel counter view with branding badge. Panel 3 (right): direct 90-degree overhead top-down flat lay view showing laces and tongue. Uniform 5500K dual softbox lighting, razor-sharp details, subtle soft contact shadow on floor, clean commercial photography, no background clutter."
      }
    },
    "negative_prompt": "distorted logos, misspelled text, fake brand badges, asymmetrical deformed sole, warped eyelets, blurry laces, colored background, gradient background, shadows on walls, studio stands, human feet, legs, hands, mannequins, socks, dirty soles, worn leather, scuffs, lowres, oversaturated, chromatic aberration, cartoon, illustration, 3d render plastic sheen"
  },
  {
    "index": 9,
    "sku": "IR1968-133",
    "name": "Nike Air Force 1 '07 WNBA 30th Anniversary",
    "primary_ref": "assets/2-norm-std/IR1968-133/01-lateral.webp",
    "formats": {
      "json_2x2": {
        "name": "Opción 1: JSON 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "JSON • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IR1968-133 --layout 2x2",
        "prompt": "{\n  \"task\": \"commercial_footwear_catalog_quad_sheet\",\n  \"product\": {\n    \"name\": \"Nike Air Force 1 '07 WNBA 30th Anniversary\",\n    \"sku\": \"IR1968-133\",\n    \"authentic\": true\n  },\n  \"layout\": {\n    \"type\": \"2x2_grid_contact_sheet\",\n    \"aspect_ratio\": \"1:1\",\n    \"background_color\": \"#FFFFFF\",\n    \"panels\": {\n      \"top_left\": \"90-degree lateral outer profile, toe pointing LEFT\",\n      \"top_right\": \"45-degree 3/4 perspective front-quarter, facing LEFT\",\n      \"bottom_left\": \"180-degree direct rear heel counter, centered\",\n      \"bottom_right\": \"90-degree overhead top-down flat lay view, laces and tongue\"\n    }\n  },\n  \"lighting\": \"neutral_softbox_5500k_studio\",\n  \"camera\": \"85mm_lens_f8_sharp_focus\",\n  \"output\": \"razor_sharp_focus_pure_white_background_subtle_contact_shadow\"\n}"
      },
      "json_1x3": {
        "name": "Opción 2: JSON 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9 o 4:3",
        "tag": "JSON • 16:9 / 4:3 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IR1968-133 --layout 1x3",
        "prompt": "{\n  \"style\": \"professional_sneaker_catalog\",\n  \"shoe\": \"Nike Air Force 1 '07 WNBA 30th Anniversary\",\n  \"sku\": \"IR1968-133\",\n  \"composition\": \"horizontal_triptych_three_equal_panels\",\n  \"aspect_ratio\": \"16:9_or_4:3\",\n  \"background\": \"seamless_solid_pure_white_#FFFFFF\",\n  \"views_left_to_right\": [\n    \"Panel 1: clean lateral outer profile view with toe pointing horizontally LEFT\",\n    \"Panel 2: direct 180-degree rear heel branding badge centered\",\n    \"Panel 3: direct 90-degree overhead top-down view showing laces and tongue\"\n  ],\n  \"render_quality\": \"8k_resolution_sharp_textures_dual_softbox_lighting\"\n}"
      },
      "text_2x2": {
        "name": "Opción 3: Texto Plano 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "Texto • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IR1968-133 --layout 2x2",
        "prompt": "Commercial footwear catalog 2x2 grid contact sheet of authentic sneaker Nike Air Force 1 '07 WNBA 30th Anniversary, SKU: IR1968-133. Exactly 4 symmetrical panels on a seamless pure solid white background (#FFFFFF). Top-left panel: strict 90-degree lateral outer profile pointing LEFT. Top-right panel: three-quarter 3/4 perspective front-quarter facing LEFT. Bottom-left panel: direct 180-degree rear heel view centered. Bottom-right panel: direct 90-degree overhead top-down flat lay view. Identical studio softbox lighting at 5500K across all panels, subtle grounded contact shadows, razor-sharp focus across all textures, 85mm lens f/8, 8k resolution e-commerce standard, no human feet, no props."
      },
      "text_1x3": {
        "name": "Opción 4: Texto Plano 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9",
        "tag": "Texto • 16:9 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IR1968-133 --layout 1x3",
        "prompt": "Commercial footwear catalog triptych row showing exactly 3 side-by-side photographic views of the sneaker Nike Air Force 1 '07 WNBA 30th Anniversary, SKU: IR1968-133 on a pure solid white background (#FFFFFF). Panel 1 (left): strict 90-degree lateral side profile pointing LEFT. Panel 2 (center): direct 180-degree rear heel counter view with branding badge. Panel 3 (right): direct 90-degree overhead top-down flat lay view showing laces and tongue. Uniform 5500K dual softbox lighting, razor-sharp details, subtle soft contact shadow on floor, clean commercial photography, no background clutter."
      }
    },
    "negative_prompt": "distorted logos, misspelled text, fake brand badges, asymmetrical deformed sole, warped eyelets, blurry laces, colored background, gradient background, shadows on walls, studio stands, human feet, legs, hands, mannequins, socks, dirty soles, worn leather, scuffs, lowres, oversaturated, chromatic aberration, cartoon, illustration, 3d render plastic sheen"
  },
  {
    "index": 10,
    "sku": "IR5896-030",
    "name": "Nike Air Force 1 '07 LV8 \"Mexico\"",
    "primary_ref": "assets/2-norm-std/IR5896-030/01-lateral.webp",
    "formats": {
      "json_2x2": {
        "name": "Opción 1: JSON 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "JSON • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IR5896-030 --layout 2x2",
        "prompt": "{\n  \"task\": \"commercial_footwear_catalog_quad_sheet\",\n  \"product\": {\n    \"name\": \"Nike Air Force 1 '07 LV8 \\\"Mexico\\\"\",\n    \"sku\": \"IR5896-030\",\n    \"authentic\": true\n  },\n  \"layout\": {\n    \"type\": \"2x2_grid_contact_sheet\",\n    \"aspect_ratio\": \"1:1\",\n    \"background_color\": \"#FFFFFF\",\n    \"panels\": {\n      \"top_left\": \"90-degree lateral outer profile, toe pointing LEFT\",\n      \"top_right\": \"45-degree 3/4 perspective front-quarter, facing LEFT\",\n      \"bottom_left\": \"180-degree direct rear heel counter, centered\",\n      \"bottom_right\": \"90-degree overhead top-down flat lay view, laces and tongue\"\n    }\n  },\n  \"lighting\": \"neutral_softbox_5500k_studio\",\n  \"camera\": \"85mm_lens_f8_sharp_focus\",\n  \"output\": \"razor_sharp_focus_pure_white_background_subtle_contact_shadow\"\n}"
      },
      "json_1x3": {
        "name": "Opción 2: JSON 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9 o 4:3",
        "tag": "JSON • 16:9 / 4:3 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IR5896-030 --layout 1x3",
        "prompt": "{\n  \"style\": \"professional_sneaker_catalog\",\n  \"shoe\": \"Nike Air Force 1 '07 LV8 \\\"Mexico\\\"\",\n  \"sku\": \"IR5896-030\",\n  \"composition\": \"horizontal_triptych_three_equal_panels\",\n  \"aspect_ratio\": \"16:9_or_4:3\",\n  \"background\": \"seamless_solid_pure_white_#FFFFFF\",\n  \"views_left_to_right\": [\n    \"Panel 1: clean lateral outer profile view with toe pointing horizontally LEFT\",\n    \"Panel 2: direct 180-degree rear heel branding badge centered\",\n    \"Panel 3: direct 90-degree overhead top-down view showing laces and tongue\"\n  ],\n  \"render_quality\": \"8k_resolution_sharp_textures_dual_softbox_lighting\"\n}"
      },
      "text_2x2": {
        "name": "Opción 3: Texto Plano 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "Texto • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IR5896-030 --layout 2x2",
        "prompt": "Commercial footwear catalog 2x2 grid contact sheet of authentic sneaker Nike Air Force 1 '07 LV8 \"Mexico\", SKU: IR5896-030. Exactly 4 symmetrical panels on a seamless pure solid white background (#FFFFFF). Top-left panel: strict 90-degree lateral outer profile pointing LEFT. Top-right panel: three-quarter 3/4 perspective front-quarter facing LEFT. Bottom-left panel: direct 180-degree rear heel view centered. Bottom-right panel: direct 90-degree overhead top-down flat lay view. Identical studio softbox lighting at 5500K across all panels, subtle grounded contact shadows, razor-sharp focus across all textures, 85mm lens f/8, 8k resolution e-commerce standard, no human feet, no props."
      },
      "text_1x3": {
        "name": "Opción 4: Texto Plano 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9",
        "tag": "Texto • 16:9 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IR5896-030 --layout 1x3",
        "prompt": "Commercial footwear catalog triptych row showing exactly 3 side-by-side photographic views of the sneaker Nike Air Force 1 '07 LV8 \"Mexico\", SKU: IR5896-030 on a pure solid white background (#FFFFFF). Panel 1 (left): strict 90-degree lateral side profile pointing LEFT. Panel 2 (center): direct 180-degree rear heel counter view with branding badge. Panel 3 (right): direct 90-degree overhead top-down flat lay view showing laces and tongue. Uniform 5500K dual softbox lighting, razor-sharp details, subtle soft contact shadow on floor, clean commercial photography, no background clutter."
      }
    },
    "negative_prompt": "distorted logos, misspelled text, fake brand badges, asymmetrical deformed sole, warped eyelets, blurry laces, colored background, gradient background, shadows on walls, studio stands, human feet, legs, hands, mannequins, socks, dirty soles, worn leather, scuffs, lowres, oversaturated, chromatic aberration, cartoon, illustration, 3d render plastic sheen"
  },
  {
    "index": 11,
    "sku": "IV6222-410",
    "name": "Nike Air Griffey Max 1",
    "primary_ref": "assets/2-norm-std/IV6222-410/01-lateral.webp",
    "formats": {
      "json_2x2": {
        "name": "Opción 1: JSON 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "JSON • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IV6222-410 --layout 2x2",
        "prompt": "{\n  \"task\": \"commercial_footwear_catalog_quad_sheet\",\n  \"product\": {\n    \"name\": \"Nike Air Griffey Max 1\",\n    \"sku\": \"IV6222-410\",\n    \"authentic\": true\n  },\n  \"layout\": {\n    \"type\": \"2x2_grid_contact_sheet\",\n    \"aspect_ratio\": \"1:1\",\n    \"background_color\": \"#FFFFFF\",\n    \"panels\": {\n      \"top_left\": \"90-degree lateral outer profile, toe pointing LEFT\",\n      \"top_right\": \"45-degree 3/4 perspective front-quarter, facing LEFT\",\n      \"bottom_left\": \"180-degree direct rear heel counter, centered\",\n      \"bottom_right\": \"90-degree overhead top-down flat lay view, laces and tongue\"\n    }\n  },\n  \"lighting\": \"neutral_softbox_5500k_studio\",\n  \"camera\": \"85mm_lens_f8_sharp_focus\",\n  \"output\": \"razor_sharp_focus_pure_white_background_subtle_contact_shadow\"\n}"
      },
      "json_1x3": {
        "name": "Opción 2: JSON 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9 o 4:3",
        "tag": "JSON • 16:9 / 4:3 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IV6222-410 --layout 1x3",
        "prompt": "{\n  \"style\": \"professional_sneaker_catalog\",\n  \"shoe\": \"Nike Air Griffey Max 1\",\n  \"sku\": \"IV6222-410\",\n  \"composition\": \"horizontal_triptych_three_equal_panels\",\n  \"aspect_ratio\": \"16:9_or_4:3\",\n  \"background\": \"seamless_solid_pure_white_#FFFFFF\",\n  \"views_left_to_right\": [\n    \"Panel 1: clean lateral outer profile view with toe pointing horizontally LEFT\",\n    \"Panel 2: direct 180-degree rear heel branding badge centered\",\n    \"Panel 3: direct 90-degree overhead top-down view showing laces and tongue\"\n  ],\n  \"render_quality\": \"8k_resolution_sharp_textures_dual_softbox_lighting\"\n}"
      },
      "text_2x2": {
        "name": "Opción 3: Texto Plano 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "Texto • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IV6222-410 --layout 2x2",
        "prompt": "Commercial footwear catalog 2x2 grid contact sheet of authentic sneaker Nike Air Griffey Max 1, SKU: IV6222-410. Exactly 4 symmetrical panels on a seamless pure solid white background (#FFFFFF). Top-left panel: strict 90-degree lateral outer profile pointing LEFT. Top-right panel: three-quarter 3/4 perspective front-quarter facing LEFT. Bottom-left panel: direct 180-degree rear heel view centered. Bottom-right panel: direct 90-degree overhead top-down flat lay view. Identical studio softbox lighting at 5500K across all panels, subtle grounded contact shadows, razor-sharp focus across all textures, 85mm lens f/8, 8k resolution e-commerce standard, no human feet, no props."
      },
      "text_1x3": {
        "name": "Opción 4: Texto Plano 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9",
        "tag": "Texto • 16:9 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IV6222-410 --layout 1x3",
        "prompt": "Commercial footwear catalog triptych row showing exactly 3 side-by-side photographic views of the sneaker Nike Air Griffey Max 1, SKU: IV6222-410 on a pure solid white background (#FFFFFF). Panel 1 (left): strict 90-degree lateral side profile pointing LEFT. Panel 2 (center): direct 180-degree rear heel counter view with branding badge. Panel 3 (right): direct 90-degree overhead top-down flat lay view showing laces and tongue. Uniform 5500K dual softbox lighting, razor-sharp details, subtle soft contact shadow on floor, clean commercial photography, no background clutter."
      }
    },
    "negative_prompt": "distorted logos, misspelled text, fake brand badges, asymmetrical deformed sole, warped eyelets, blurry laces, colored background, gradient background, shadows on walls, studio stands, human feet, legs, hands, mannequins, socks, dirty soles, worn leather, scuffs, lowres, oversaturated, chromatic aberration, cartoon, illustration, 3d render plastic sheen"
  },
  {
    "index": 12,
    "sku": "553560-045",
    "name": "Air Jordan 1 Low Summit White / Black",
    "primary_ref": "assets/2-norm-std/553560-045/01-lateral.webp",
    "formats": {
      "json_2x2": {
        "name": "Opción 1: JSON 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "JSON • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku 553560-045 --layout 2x2",
        "prompt": "{\n  \"task\": \"commercial_footwear_catalog_quad_sheet\",\n  \"product\": {\n    \"name\": \"Air Jordan 1 Low Summit White / Black\",\n    \"sku\": \"553560-045\",\n    \"authentic\": true\n  },\n  \"layout\": {\n    \"type\": \"2x2_grid_contact_sheet\",\n    \"aspect_ratio\": \"1:1\",\n    \"background_color\": \"#FFFFFF\",\n    \"panels\": {\n      \"top_left\": \"90-degree lateral outer profile, toe pointing LEFT\",\n      \"top_right\": \"45-degree 3/4 perspective front-quarter, facing LEFT\",\n      \"bottom_left\": \"180-degree direct rear heel counter, centered\",\n      \"bottom_right\": \"90-degree overhead top-down flat lay view, laces and tongue\"\n    }\n  },\n  \"lighting\": \"neutral_softbox_5500k_studio\",\n  \"camera\": \"85mm_lens_f8_sharp_focus\",\n  \"output\": \"razor_sharp_focus_pure_white_background_subtle_contact_shadow\"\n}"
      },
      "json_1x3": {
        "name": "Opción 2: JSON 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9 o 4:3",
        "tag": "JSON • 16:9 / 4:3 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku 553560-045 --layout 1x3",
        "prompt": "{\n  \"style\": \"professional_sneaker_catalog\",\n  \"shoe\": \"Air Jordan 1 Low Summit White / Black\",\n  \"sku\": \"553560-045\",\n  \"composition\": \"horizontal_triptych_three_equal_panels\",\n  \"aspect_ratio\": \"16:9_or_4:3\",\n  \"background\": \"seamless_solid_pure_white_#FFFFFF\",\n  \"views_left_to_right\": [\n    \"Panel 1: clean lateral outer profile view with toe pointing horizontally LEFT\",\n    \"Panel 2: direct 180-degree rear heel branding badge centered\",\n    \"Panel 3: direct 90-degree overhead top-down view showing laces and tongue\"\n  ],\n  \"render_quality\": \"8k_resolution_sharp_textures_dual_softbox_lighting\"\n}"
      },
      "text_2x2": {
        "name": "Opción 3: Texto Plano 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "Texto • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku 553560-045 --layout 2x2",
        "prompt": "Commercial footwear catalog 2x2 grid contact sheet of authentic sneaker Air Jordan 1 Low Summit White / Black, SKU: 553560-045. Exactly 4 symmetrical panels on a seamless pure solid white background (#FFFFFF). Top-left panel: strict 90-degree lateral outer profile pointing LEFT. Top-right panel: three-quarter 3/4 perspective front-quarter facing LEFT. Bottom-left panel: direct 180-degree rear heel view centered. Bottom-right panel: direct 90-degree overhead top-down flat lay view. Identical studio softbox lighting at 5500K across all panels, subtle grounded contact shadows, razor-sharp focus across all textures, 85mm lens f/8, 8k resolution e-commerce standard, no human feet, no props."
      },
      "text_1x3": {
        "name": "Opción 4: Texto Plano 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9",
        "tag": "Texto • 16:9 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku 553560-045 --layout 1x3",
        "prompt": "Commercial footwear catalog triptych row showing exactly 3 side-by-side photographic views of the sneaker Air Jordan 1 Low Summit White / Black, SKU: 553560-045 on a pure solid white background (#FFFFFF). Panel 1 (left): strict 90-degree lateral side profile pointing LEFT. Panel 2 (center): direct 180-degree rear heel counter view with branding badge. Panel 3 (right): direct 90-degree overhead top-down flat lay view showing laces and tongue. Uniform 5500K dual softbox lighting, razor-sharp details, subtle soft contact shadow on floor, clean commercial photography, no background clutter."
      }
    },
    "negative_prompt": "distorted logos, misspelled text, fake brand badges, asymmetrical deformed sole, warped eyelets, blurry laces, colored background, gradient background, shadows on walls, studio stands, human feet, legs, hands, mannequins, socks, dirty soles, worn leather, scuffs, lowres, oversaturated, chromatic aberration, cartoon, illustration, 3d render plastic sheen"
  },
  {
    "index": 13,
    "sku": "CT3839-100",
    "name": "Nike Air Force 1 Blanco / Negro",
    "primary_ref": "assets/2-norm-std/CT3839-100/01-lateral.webp",
    "formats": {
      "json_2x2": {
        "name": "Opción 1: JSON 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "JSON • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku CT3839-100 --layout 2x2",
        "prompt": "{\n  \"task\": \"commercial_footwear_catalog_quad_sheet\",\n  \"product\": {\n    \"name\": \"Nike Air Force 1 Blanco / Negro\",\n    \"sku\": \"CT3839-100\",\n    \"authentic\": true\n  },\n  \"layout\": {\n    \"type\": \"2x2_grid_contact_sheet\",\n    \"aspect_ratio\": \"1:1\",\n    \"background_color\": \"#FFFFFF\",\n    \"panels\": {\n      \"top_left\": \"90-degree lateral outer profile, toe pointing LEFT\",\n      \"top_right\": \"45-degree 3/4 perspective front-quarter, facing LEFT\",\n      \"bottom_left\": \"180-degree direct rear heel counter, centered\",\n      \"bottom_right\": \"90-degree overhead top-down flat lay view, laces and tongue\"\n    }\n  },\n  \"lighting\": \"neutral_softbox_5500k_studio\",\n  \"camera\": \"85mm_lens_f8_sharp_focus\",\n  \"output\": \"razor_sharp_focus_pure_white_background_subtle_contact_shadow\"\n}"
      },
      "json_1x3": {
        "name": "Opción 2: JSON 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9 o 4:3",
        "tag": "JSON • 16:9 / 4:3 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku CT3839-100 --layout 1x3",
        "prompt": "{\n  \"style\": \"professional_sneaker_catalog\",\n  \"shoe\": \"Nike Air Force 1 Blanco / Negro\",\n  \"sku\": \"CT3839-100\",\n  \"composition\": \"horizontal_triptych_three_equal_panels\",\n  \"aspect_ratio\": \"16:9_or_4:3\",\n  \"background\": \"seamless_solid_pure_white_#FFFFFF\",\n  \"views_left_to_right\": [\n    \"Panel 1: clean lateral outer profile view with toe pointing horizontally LEFT\",\n    \"Panel 2: direct 180-degree rear heel branding badge centered\",\n    \"Panel 3: direct 90-degree overhead top-down view showing laces and tongue\"\n  ],\n  \"render_quality\": \"8k_resolution_sharp_textures_dual_softbox_lighting\"\n}"
      },
      "text_2x2": {
        "name": "Opción 3: Texto Plano 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "Texto • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku CT3839-100 --layout 2x2",
        "prompt": "Commercial footwear catalog 2x2 grid contact sheet of authentic sneaker Nike Air Force 1 Blanco / Negro, SKU: CT3839-100. Exactly 4 symmetrical panels on a seamless pure solid white background (#FFFFFF). Top-left panel: strict 90-degree lateral outer profile pointing LEFT. Top-right panel: three-quarter 3/4 perspective front-quarter facing LEFT. Bottom-left panel: direct 180-degree rear heel view centered. Bottom-right panel: direct 90-degree overhead top-down flat lay view. Identical studio softbox lighting at 5500K across all panels, subtle grounded contact shadows, razor-sharp focus across all textures, 85mm lens f/8, 8k resolution e-commerce standard, no human feet, no props."
      },
      "text_1x3": {
        "name": "Opción 4: Texto Plano 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9",
        "tag": "Texto • 16:9 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku CT3839-100 --layout 1x3",
        "prompt": "Commercial footwear catalog triptych row showing exactly 3 side-by-side photographic views of the sneaker Nike Air Force 1 Blanco / Negro, SKU: CT3839-100 on a pure solid white background (#FFFFFF). Panel 1 (left): strict 90-degree lateral side profile pointing LEFT. Panel 2 (center): direct 180-degree rear heel counter view with branding badge. Panel 3 (right): direct 90-degree overhead top-down flat lay view showing laces and tongue. Uniform 5500K dual softbox lighting, razor-sharp details, subtle soft contact shadow on floor, clean commercial photography, no background clutter."
      }
    },
    "negative_prompt": "distorted logos, misspelled text, fake brand badges, asymmetrical deformed sole, warped eyelets, blurry laces, colored background, gradient background, shadows on walls, studio stands, human feet, legs, hands, mannequins, socks, dirty soles, worn leather, scuffs, lowres, oversaturated, chromatic aberration, cartoon, illustration, 3d render plastic sheen"
  },
  {
    "index": 14,
    "sku": "IW2872-700",
    "name": "Air Jordan 4 x J Balvin \"Amazonas\"",
    "primary_ref": "assets/2-norm-std/IW2872-700/01-lateral.webp",
    "formats": {
      "json_2x2": {
        "name": "Opción 1: JSON 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "JSON • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IW2872-700 --layout 2x2",
        "prompt": "{\n  \"task\": \"commercial_footwear_catalog_quad_sheet\",\n  \"product\": {\n    \"name\": \"Air Jordan 4 x J Balvin \\\"Amazonas\\\"\",\n    \"sku\": \"IW2872-700\",\n    \"authentic\": true\n  },\n  \"layout\": {\n    \"type\": \"2x2_grid_contact_sheet\",\n    \"aspect_ratio\": \"1:1\",\n    \"background_color\": \"#FFFFFF\",\n    \"panels\": {\n      \"top_left\": \"90-degree lateral outer profile, toe pointing LEFT\",\n      \"top_right\": \"45-degree 3/4 perspective front-quarter, facing LEFT\",\n      \"bottom_left\": \"180-degree direct rear heel counter, centered\",\n      \"bottom_right\": \"90-degree overhead top-down flat lay view, laces and tongue\"\n    }\n  },\n  \"lighting\": \"neutral_softbox_5500k_studio\",\n  \"camera\": \"85mm_lens_f8_sharp_focus\",\n  \"output\": \"razor_sharp_focus_pure_white_background_subtle_contact_shadow\"\n}"
      },
      "json_1x3": {
        "name": "Opción 2: JSON 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9 o 4:3",
        "tag": "JSON • 16:9 / 4:3 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IW2872-700 --layout 1x3",
        "prompt": "{\n  \"style\": \"professional_sneaker_catalog\",\n  \"shoe\": \"Air Jordan 4 x J Balvin \\\"Amazonas\\\"\",\n  \"sku\": \"IW2872-700\",\n  \"composition\": \"horizontal_triptych_three_equal_panels\",\n  \"aspect_ratio\": \"16:9_or_4:3\",\n  \"background\": \"seamless_solid_pure_white_#FFFFFF\",\n  \"views_left_to_right\": [\n    \"Panel 1: clean lateral outer profile view with toe pointing horizontally LEFT\",\n    \"Panel 2: direct 180-degree rear heel branding badge centered\",\n    \"Panel 3: direct 90-degree overhead top-down view showing laces and tongue\"\n  ],\n  \"render_quality\": \"8k_resolution_sharp_textures_dual_softbox_lighting\"\n}"
      },
      "text_2x2": {
        "name": "Opción 3: Texto Plano 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "Texto • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IW2872-700 --layout 2x2",
        "prompt": "Commercial footwear catalog 2x2 grid contact sheet of authentic sneaker Air Jordan 4 x J Balvin \"Amazonas\", SKU: IW2872-700. Exactly 4 symmetrical panels on a seamless pure solid white background (#FFFFFF). Top-left panel: strict 90-degree lateral outer profile pointing LEFT. Top-right panel: three-quarter 3/4 perspective front-quarter facing LEFT. Bottom-left panel: direct 180-degree rear heel view centered. Bottom-right panel: direct 90-degree overhead top-down flat lay view. Identical studio softbox lighting at 5500K across all panels, subtle grounded contact shadows, razor-sharp focus across all textures, 85mm lens f/8, 8k resolution e-commerce standard, no human feet, no props."
      },
      "text_1x3": {
        "name": "Opción 4: Texto Plano 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9",
        "tag": "Texto • 16:9 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IW2872-700 --layout 1x3",
        "prompt": "Commercial footwear catalog triptych row showing exactly 3 side-by-side photographic views of the sneaker Air Jordan 4 x J Balvin \"Amazonas\", SKU: IW2872-700 on a pure solid white background (#FFFFFF). Panel 1 (left): strict 90-degree lateral side profile pointing LEFT. Panel 2 (center): direct 180-degree rear heel counter view with branding badge. Panel 3 (right): direct 90-degree overhead top-down flat lay view showing laces and tongue. Uniform 5500K dual softbox lighting, razor-sharp details, subtle soft contact shadow on floor, clean commercial photography, no background clutter."
      }
    },
    "negative_prompt": "distorted logos, misspelled text, fake brand badges, asymmetrical deformed sole, warped eyelets, blurry laces, colored background, gradient background, shadows on walls, studio stands, human feet, legs, hands, mannequins, socks, dirty soles, worn leather, scuffs, lowres, oversaturated, chromatic aberration, cartoon, illustration, 3d render plastic sheen"
  },
  {
    "index": 15,
    "sku": "FD1437-008",
    "name": "Air Jordan 1 High OG \"Shattered Backboard\"",
    "primary_ref": "assets/2-norm-std/FD1437-008/01-lateral.webp",
    "formats": {
      "json_2x2": {
        "name": "Opción 1: JSON 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "JSON • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku FD1437-008 --layout 2x2",
        "prompt": "{\n  \"task\": \"commercial_footwear_catalog_quad_sheet\",\n  \"product\": {\n    \"name\": \"Air Jordan 1 High OG \\\"Shattered Backboard\\\"\",\n    \"sku\": \"FD1437-008\",\n    \"authentic\": true\n  },\n  \"layout\": {\n    \"type\": \"2x2_grid_contact_sheet\",\n    \"aspect_ratio\": \"1:1\",\n    \"background_color\": \"#FFFFFF\",\n    \"panels\": {\n      \"top_left\": \"90-degree lateral outer profile, toe pointing LEFT\",\n      \"top_right\": \"45-degree 3/4 perspective front-quarter, facing LEFT\",\n      \"bottom_left\": \"180-degree direct rear heel counter, centered\",\n      \"bottom_right\": \"90-degree overhead top-down flat lay view, laces and tongue\"\n    }\n  },\n  \"lighting\": \"neutral_softbox_5500k_studio\",\n  \"camera\": \"85mm_lens_f8_sharp_focus\",\n  \"output\": \"razor_sharp_focus_pure_white_background_subtle_contact_shadow\"\n}"
      },
      "json_1x3": {
        "name": "Opción 2: JSON 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9 o 4:3",
        "tag": "JSON • 16:9 / 4:3 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku FD1437-008 --layout 1x3",
        "prompt": "{\n  \"style\": \"professional_sneaker_catalog\",\n  \"shoe\": \"Air Jordan 1 High OG \\\"Shattered Backboard\\\"\",\n  \"sku\": \"FD1437-008\",\n  \"composition\": \"horizontal_triptych_three_equal_panels\",\n  \"aspect_ratio\": \"16:9_or_4:3\",\n  \"background\": \"seamless_solid_pure_white_#FFFFFF\",\n  \"views_left_to_right\": [\n    \"Panel 1: clean lateral outer profile view with toe pointing horizontally LEFT\",\n    \"Panel 2: direct 180-degree rear heel branding badge centered\",\n    \"Panel 3: direct 90-degree overhead top-down view showing laces and tongue\"\n  ],\n  \"render_quality\": \"8k_resolution_sharp_textures_dual_softbox_lighting\"\n}"
      },
      "text_2x2": {
        "name": "Opción 3: Texto Plano 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "Texto • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku FD1437-008 --layout 2x2",
        "prompt": "Commercial footwear catalog 2x2 grid contact sheet of authentic sneaker Air Jordan 1 High OG \"Shattered Backboard\", SKU: FD1437-008. Exactly 4 symmetrical panels on a seamless pure solid white background (#FFFFFF). Top-left panel: strict 90-degree lateral outer profile pointing LEFT. Top-right panel: three-quarter 3/4 perspective front-quarter facing LEFT. Bottom-left panel: direct 180-degree rear heel view centered. Bottom-right panel: direct 90-degree overhead top-down flat lay view. Identical studio softbox lighting at 5500K across all panels, subtle grounded contact shadows, razor-sharp focus across all textures, 85mm lens f/8, 8k resolution e-commerce standard, no human feet, no props."
      },
      "text_1x3": {
        "name": "Opción 4: Texto Plano 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9",
        "tag": "Texto • 16:9 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku FD1437-008 --layout 1x3",
        "prompt": "Commercial footwear catalog triptych row showing exactly 3 side-by-side photographic views of the sneaker Air Jordan 1 High OG \"Shattered Backboard\", SKU: FD1437-008 on a pure solid white background (#FFFFFF). Panel 1 (left): strict 90-degree lateral side profile pointing LEFT. Panel 2 (center): direct 180-degree rear heel counter view with branding badge. Panel 3 (right): direct 90-degree overhead top-down flat lay view showing laces and tongue. Uniform 5500K dual softbox lighting, razor-sharp details, subtle soft contact shadow on floor, clean commercial photography, no background clutter."
      }
    },
    "negative_prompt": "distorted logos, misspelled text, fake brand badges, asymmetrical deformed sole, warped eyelets, blurry laces, colored background, gradient background, shadows on walls, studio stands, human feet, legs, hands, mannequins, socks, dirty soles, worn leather, scuffs, lowres, oversaturated, chromatic aberration, cartoon, illustration, 3d render plastic sheen"
  },
  {
    "index": 16,
    "sku": "408452-102",
    "name": "Air Jordan 4 Retro \"Tour Yellow\"",
    "primary_ref": "assets/2-norm-std/408452-102/01-lateral.webp",
    "formats": {
      "json_2x2": {
        "name": "Opción 1: JSON 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "JSON • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku 408452-102 --layout 2x2",
        "prompt": "{\n  \"task\": \"commercial_footwear_catalog_quad_sheet\",\n  \"product\": {\n    \"name\": \"Air Jordan 4 Retro \\\"Tour Yellow\\\"\",\n    \"sku\": \"408452-102\",\n    \"authentic\": true\n  },\n  \"layout\": {\n    \"type\": \"2x2_grid_contact_sheet\",\n    \"aspect_ratio\": \"1:1\",\n    \"background_color\": \"#FFFFFF\",\n    \"panels\": {\n      \"top_left\": \"90-degree lateral outer profile, toe pointing LEFT\",\n      \"top_right\": \"45-degree 3/4 perspective front-quarter, facing LEFT\",\n      \"bottom_left\": \"180-degree direct rear heel counter, centered\",\n      \"bottom_right\": \"90-degree overhead top-down flat lay view, laces and tongue\"\n    }\n  },\n  \"lighting\": \"neutral_softbox_5500k_studio\",\n  \"camera\": \"85mm_lens_f8_sharp_focus\",\n  \"output\": \"razor_sharp_focus_pure_white_background_subtle_contact_shadow\"\n}"
      },
      "json_1x3": {
        "name": "Opción 2: JSON 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9 o 4:3",
        "tag": "JSON • 16:9 / 4:3 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku 408452-102 --layout 1x3",
        "prompt": "{\n  \"style\": \"professional_sneaker_catalog\",\n  \"shoe\": \"Air Jordan 4 Retro \\\"Tour Yellow\\\"\",\n  \"sku\": \"408452-102\",\n  \"composition\": \"horizontal_triptych_three_equal_panels\",\n  \"aspect_ratio\": \"16:9_or_4:3\",\n  \"background\": \"seamless_solid_pure_white_#FFFFFF\",\n  \"views_left_to_right\": [\n    \"Panel 1: clean lateral outer profile view with toe pointing horizontally LEFT\",\n    \"Panel 2: direct 180-degree rear heel branding badge centered\",\n    \"Panel 3: direct 90-degree overhead top-down view showing laces and tongue\"\n  ],\n  \"render_quality\": \"8k_resolution_sharp_textures_dual_softbox_lighting\"\n}"
      },
      "text_2x2": {
        "name": "Opción 3: Texto Plano 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "Texto • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku 408452-102 --layout 2x2",
        "prompt": "Commercial footwear catalog 2x2 grid contact sheet of authentic sneaker Air Jordan 4 Retro \"Tour Yellow\", SKU: 408452-102. Exactly 4 symmetrical panels on a seamless pure solid white background (#FFFFFF). Top-left panel: strict 90-degree lateral outer profile pointing LEFT. Top-right panel: three-quarter 3/4 perspective front-quarter facing LEFT. Bottom-left panel: direct 180-degree rear heel view centered. Bottom-right panel: direct 90-degree overhead top-down flat lay view. Identical studio softbox lighting at 5500K across all panels, subtle grounded contact shadows, razor-sharp focus across all textures, 85mm lens f/8, 8k resolution e-commerce standard, no human feet, no props."
      },
      "text_1x3": {
        "name": "Opción 4: Texto Plano 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9",
        "tag": "Texto • 16:9 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku 408452-102 --layout 1x3",
        "prompt": "Commercial footwear catalog triptych row showing exactly 3 side-by-side photographic views of the sneaker Air Jordan 4 Retro \"Tour Yellow\", SKU: 408452-102 on a pure solid white background (#FFFFFF). Panel 1 (left): strict 90-degree lateral side profile pointing LEFT. Panel 2 (center): direct 180-degree rear heel counter view with branding badge. Panel 3 (right): direct 90-degree overhead top-down flat lay view showing laces and tongue. Uniform 5500K dual softbox lighting, razor-sharp details, subtle soft contact shadow on floor, clean commercial photography, no background clutter."
      }
    },
    "negative_prompt": "distorted logos, misspelled text, fake brand badges, asymmetrical deformed sole, warped eyelets, blurry laces, colored background, gradient background, shadows on walls, studio stands, human feet, legs, hands, mannequins, socks, dirty soles, worn leather, scuffs, lowres, oversaturated, chromatic aberration, cartoon, illustration, 3d render plastic sheen"
  },
  {
    "index": 17,
    "sku": "AQ9214-011",
    "name": "Jordan Max Aura Black / White",
    "primary_ref": "assets/2-norm-std/AQ9214-011/01-lateral.webp",
    "formats": {
      "json_2x2": {
        "name": "Opción 1: JSON 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "JSON • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku AQ9214-011 --layout 2x2",
        "prompt": "{\n  \"task\": \"commercial_footwear_catalog_quad_sheet\",\n  \"product\": {\n    \"name\": \"Jordan Max Aura Black / White\",\n    \"sku\": \"AQ9214-011\",\n    \"authentic\": true\n  },\n  \"layout\": {\n    \"type\": \"2x2_grid_contact_sheet\",\n    \"aspect_ratio\": \"1:1\",\n    \"background_color\": \"#FFFFFF\",\n    \"panels\": {\n      \"top_left\": \"90-degree lateral outer profile, toe pointing LEFT\",\n      \"top_right\": \"45-degree 3/4 perspective front-quarter, facing LEFT\",\n      \"bottom_left\": \"180-degree direct rear heel counter, centered\",\n      \"bottom_right\": \"90-degree overhead top-down flat lay view, laces and tongue\"\n    }\n  },\n  \"lighting\": \"neutral_softbox_5500k_studio\",\n  \"camera\": \"85mm_lens_f8_sharp_focus\",\n  \"output\": \"razor_sharp_focus_pure_white_background_subtle_contact_shadow\"\n}"
      },
      "json_1x3": {
        "name": "Opción 2: JSON 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9 o 4:3",
        "tag": "JSON • 16:9 / 4:3 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku AQ9214-011 --layout 1x3",
        "prompt": "{\n  \"style\": \"professional_sneaker_catalog\",\n  \"shoe\": \"Jordan Max Aura Black / White\",\n  \"sku\": \"AQ9214-011\",\n  \"composition\": \"horizontal_triptych_three_equal_panels\",\n  \"aspect_ratio\": \"16:9_or_4:3\",\n  \"background\": \"seamless_solid_pure_white_#FFFFFF\",\n  \"views_left_to_right\": [\n    \"Panel 1: clean lateral outer profile view with toe pointing horizontally LEFT\",\n    \"Panel 2: direct 180-degree rear heel branding badge centered\",\n    \"Panel 3: direct 90-degree overhead top-down view showing laces and tongue\"\n  ],\n  \"render_quality\": \"8k_resolution_sharp_textures_dual_softbox_lighting\"\n}"
      },
      "text_2x2": {
        "name": "Opción 3: Texto Plano 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "Texto • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku AQ9214-011 --layout 2x2",
        "prompt": "Commercial footwear catalog 2x2 grid contact sheet of authentic sneaker Jordan Max Aura Black / White, SKU: AQ9214-011. Exactly 4 symmetrical panels on a seamless pure solid white background (#FFFFFF). Top-left panel: strict 90-degree lateral outer profile pointing LEFT. Top-right panel: three-quarter 3/4 perspective front-quarter facing LEFT. Bottom-left panel: direct 180-degree rear heel view centered. Bottom-right panel: direct 90-degree overhead top-down flat lay view. Identical studio softbox lighting at 5500K across all panels, subtle grounded contact shadows, razor-sharp focus across all textures, 85mm lens f/8, 8k resolution e-commerce standard, no human feet, no props."
      },
      "text_1x3": {
        "name": "Opción 4: Texto Plano 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9",
        "tag": "Texto • 16:9 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku AQ9214-011 --layout 1x3",
        "prompt": "Commercial footwear catalog triptych row showing exactly 3 side-by-side photographic views of the sneaker Jordan Max Aura Black / White, SKU: AQ9214-011 on a pure solid white background (#FFFFFF). Panel 1 (left): strict 90-degree lateral side profile pointing LEFT. Panel 2 (center): direct 180-degree rear heel counter view with branding badge. Panel 3 (right): direct 90-degree overhead top-down flat lay view showing laces and tongue. Uniform 5500K dual softbox lighting, razor-sharp details, subtle soft contact shadow on floor, clean commercial photography, no background clutter."
      }
    },
    "negative_prompt": "distorted logos, misspelled text, fake brand badges, asymmetrical deformed sole, warped eyelets, blurry laces, colored background, gradient background, shadows on walls, studio stands, human feet, legs, hands, mannequins, socks, dirty soles, worn leather, scuffs, lowres, oversaturated, chromatic aberration, cartoon, illustration, 3d render plastic sheen"
  },
  {
    "index": 18,
    "sku": "II1254-001",
    "name": "Air Jordan 1 Mid SE Black / Gold / Pink",
    "primary_ref": "assets/2-norm-std/II1254-001/01-lateral.webp",
    "formats": {
      "json_2x2": {
        "name": "Opción 1: JSON 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "JSON • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku II1254-001 --layout 2x2",
        "prompt": "{\n  \"task\": \"commercial_footwear_catalog_quad_sheet\",\n  \"product\": {\n    \"name\": \"Air Jordan 1 Mid SE Black / Gold / Pink\",\n    \"sku\": \"II1254-001\",\n    \"authentic\": true\n  },\n  \"layout\": {\n    \"type\": \"2x2_grid_contact_sheet\",\n    \"aspect_ratio\": \"1:1\",\n    \"background_color\": \"#FFFFFF\",\n    \"panels\": {\n      \"top_left\": \"90-degree lateral outer profile, toe pointing LEFT\",\n      \"top_right\": \"45-degree 3/4 perspective front-quarter, facing LEFT\",\n      \"bottom_left\": \"180-degree direct rear heel counter, centered\",\n      \"bottom_right\": \"90-degree overhead top-down flat lay view, laces and tongue\"\n    }\n  },\n  \"lighting\": \"neutral_softbox_5500k_studio\",\n  \"camera\": \"85mm_lens_f8_sharp_focus\",\n  \"output\": \"razor_sharp_focus_pure_white_background_subtle_contact_shadow\"\n}"
      },
      "json_1x3": {
        "name": "Opción 2: JSON 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9 o 4:3",
        "tag": "JSON • 16:9 / 4:3 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku II1254-001 --layout 1x3",
        "prompt": "{\n  \"style\": \"professional_sneaker_catalog\",\n  \"shoe\": \"Air Jordan 1 Mid SE Black / Gold / Pink\",\n  \"sku\": \"II1254-001\",\n  \"composition\": \"horizontal_triptych_three_equal_panels\",\n  \"aspect_ratio\": \"16:9_or_4:3\",\n  \"background\": \"seamless_solid_pure_white_#FFFFFF\",\n  \"views_left_to_right\": [\n    \"Panel 1: clean lateral outer profile view with toe pointing horizontally LEFT\",\n    \"Panel 2: direct 180-degree rear heel branding badge centered\",\n    \"Panel 3: direct 90-degree overhead top-down view showing laces and tongue\"\n  ],\n  \"render_quality\": \"8k_resolution_sharp_textures_dual_softbox_lighting\"\n}"
      },
      "text_2x2": {
        "name": "Opción 3: Texto Plano 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "Texto • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku II1254-001 --layout 2x2",
        "prompt": "Commercial footwear catalog 2x2 grid contact sheet of authentic sneaker Air Jordan 1 Mid SE Black / Gold / Pink, SKU: II1254-001. Exactly 4 symmetrical panels on a seamless pure solid white background (#FFFFFF). Top-left panel: strict 90-degree lateral outer profile pointing LEFT. Top-right panel: three-quarter 3/4 perspective front-quarter facing LEFT. Bottom-left panel: direct 180-degree rear heel view centered. Bottom-right panel: direct 90-degree overhead top-down flat lay view. Identical studio softbox lighting at 5500K across all panels, subtle grounded contact shadows, razor-sharp focus across all textures, 85mm lens f/8, 8k resolution e-commerce standard, no human feet, no props."
      },
      "text_1x3": {
        "name": "Opción 4: Texto Plano 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9",
        "tag": "Texto • 16:9 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku II1254-001 --layout 1x3",
        "prompt": "Commercial footwear catalog triptych row showing exactly 3 side-by-side photographic views of the sneaker Air Jordan 1 Mid SE Black / Gold / Pink, SKU: II1254-001 on a pure solid white background (#FFFFFF). Panel 1 (left): strict 90-degree lateral side profile pointing LEFT. Panel 2 (center): direct 180-degree rear heel counter view with branding badge. Panel 3 (right): direct 90-degree overhead top-down flat lay view showing laces and tongue. Uniform 5500K dual softbox lighting, razor-sharp details, subtle soft contact shadow on floor, clean commercial photography, no background clutter."
      }
    },
    "negative_prompt": "distorted logos, misspelled text, fake brand badges, asymmetrical deformed sole, warped eyelets, blurry laces, colored background, gradient background, shadows on walls, studio stands, human feet, legs, hands, mannequins, socks, dirty soles, worn leather, scuffs, lowres, oversaturated, chromatic aberration, cartoon, illustration, 3d render plastic sheen"
  },
  {
    "index": 19,
    "sku": "II0599-600",
    "name": "Air Jordan 3 Retro GS \"Spring Flowers\"",
    "primary_ref": "assets/2-norm-std/II0599-600/01-lateral.webp",
    "formats": {
      "json_2x2": {
        "name": "Opción 1: JSON 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "JSON • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku II0599-600 --layout 2x2",
        "prompt": "{\n  \"task\": \"commercial_footwear_catalog_quad_sheet\",\n  \"product\": {\n    \"name\": \"Air Jordan 3 Retro GS \\\"Spring Flowers\\\"\",\n    \"sku\": \"II0599-600\",\n    \"authentic\": true\n  },\n  \"layout\": {\n    \"type\": \"2x2_grid_contact_sheet\",\n    \"aspect_ratio\": \"1:1\",\n    \"background_color\": \"#FFFFFF\",\n    \"panels\": {\n      \"top_left\": \"90-degree lateral outer profile, toe pointing LEFT\",\n      \"top_right\": \"45-degree 3/4 perspective front-quarter, facing LEFT\",\n      \"bottom_left\": \"180-degree direct rear heel counter, centered\",\n      \"bottom_right\": \"90-degree overhead top-down flat lay view, laces and tongue\"\n    }\n  },\n  \"lighting\": \"neutral_softbox_5500k_studio\",\n  \"camera\": \"85mm_lens_f8_sharp_focus\",\n  \"output\": \"razor_sharp_focus_pure_white_background_subtle_contact_shadow\"\n}"
      },
      "json_1x3": {
        "name": "Opción 2: JSON 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9 o 4:3",
        "tag": "JSON • 16:9 / 4:3 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku II0599-600 --layout 1x3",
        "prompt": "{\n  \"style\": \"professional_sneaker_catalog\",\n  \"shoe\": \"Air Jordan 3 Retro GS \\\"Spring Flowers\\\"\",\n  \"sku\": \"II0599-600\",\n  \"composition\": \"horizontal_triptych_three_equal_panels\",\n  \"aspect_ratio\": \"16:9_or_4:3\",\n  \"background\": \"seamless_solid_pure_white_#FFFFFF\",\n  \"views_left_to_right\": [\n    \"Panel 1: clean lateral outer profile view with toe pointing horizontally LEFT\",\n    \"Panel 2: direct 180-degree rear heel branding badge centered\",\n    \"Panel 3: direct 90-degree overhead top-down view showing laces and tongue\"\n  ],\n  \"render_quality\": \"8k_resolution_sharp_textures_dual_softbox_lighting\"\n}"
      },
      "text_2x2": {
        "name": "Opción 3: Texto Plano 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "Texto • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku II0599-600 --layout 2x2",
        "prompt": "Commercial footwear catalog 2x2 grid contact sheet of authentic sneaker Air Jordan 3 Retro GS \"Spring Flowers\", SKU: II0599-600. Exactly 4 symmetrical panels on a seamless pure solid white background (#FFFFFF). Top-left panel: strict 90-degree lateral outer profile pointing LEFT. Top-right panel: three-quarter 3/4 perspective front-quarter facing LEFT. Bottom-left panel: direct 180-degree rear heel view centered. Bottom-right panel: direct 90-degree overhead top-down flat lay view. Identical studio softbox lighting at 5500K across all panels, subtle grounded contact shadows, razor-sharp focus across all textures, 85mm lens f/8, 8k resolution e-commerce standard, no human feet, no props."
      },
      "text_1x3": {
        "name": "Opción 4: Texto Plano 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9",
        "tag": "Texto • 16:9 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku II0599-600 --layout 1x3",
        "prompt": "Commercial footwear catalog triptych row showing exactly 3 side-by-side photographic views of the sneaker Air Jordan 3 Retro GS \"Spring Flowers\", SKU: II0599-600 on a pure solid white background (#FFFFFF). Panel 1 (left): strict 90-degree lateral side profile pointing LEFT. Panel 2 (center): direct 180-degree rear heel counter view with branding badge. Panel 3 (right): direct 90-degree overhead top-down flat lay view showing laces and tongue. Uniform 5500K dual softbox lighting, razor-sharp details, subtle soft contact shadow on floor, clean commercial photography, no background clutter."
      }
    },
    "negative_prompt": "distorted logos, misspelled text, fake brand badges, asymmetrical deformed sole, warped eyelets, blurry laces, colored background, gradient background, shadows on walls, studio stands, human feet, legs, hands, mannequins, socks, dirty soles, worn leather, scuffs, lowres, oversaturated, chromatic aberration, cartoon, illustration, 3d render plastic sheen"
  },
  {
    "index": 20,
    "sku": "511417-136",
    "name": "Nike Air Max Correlate White / New Green / Bright Mango / Black",
    "primary_ref": "assets/2-norm-std/511417-136/01-lateral.webp",
    "formats": {
      "json_2x2": {
        "name": "Opción 1: JSON 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "JSON • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku 511417-136 --layout 2x2",
        "prompt": "{\n  \"task\": \"commercial_footwear_catalog_quad_sheet\",\n  \"product\": {\n    \"name\": \"Nike Air Max Correlate White / New Green / Bright Mango / Black\",\n    \"sku\": \"511417-136\",\n    \"authentic\": true\n  },\n  \"layout\": {\n    \"type\": \"2x2_grid_contact_sheet\",\n    \"aspect_ratio\": \"1:1\",\n    \"background_color\": \"#FFFFFF\",\n    \"panels\": {\n      \"top_left\": \"90-degree lateral outer profile, toe pointing LEFT\",\n      \"top_right\": \"45-degree 3/4 perspective front-quarter, facing LEFT\",\n      \"bottom_left\": \"180-degree direct rear heel counter, centered\",\n      \"bottom_right\": \"90-degree overhead top-down flat lay view, laces and tongue\"\n    }\n  },\n  \"lighting\": \"neutral_softbox_5500k_studio\",\n  \"camera\": \"85mm_lens_f8_sharp_focus\",\n  \"output\": \"razor_sharp_focus_pure_white_background_subtle_contact_shadow\"\n}"
      },
      "json_1x3": {
        "name": "Opción 2: JSON 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9 o 4:3",
        "tag": "JSON • 16:9 / 4:3 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku 511417-136 --layout 1x3",
        "prompt": "{\n  \"style\": \"professional_sneaker_catalog\",\n  \"shoe\": \"Nike Air Max Correlate White / New Green / Bright Mango / Black\",\n  \"sku\": \"511417-136\",\n  \"composition\": \"horizontal_triptych_three_equal_panels\",\n  \"aspect_ratio\": \"16:9_or_4:3\",\n  \"background\": \"seamless_solid_pure_white_#FFFFFF\",\n  \"views_left_to_right\": [\n    \"Panel 1: clean lateral outer profile view with toe pointing horizontally LEFT\",\n    \"Panel 2: direct 180-degree rear heel branding badge centered\",\n    \"Panel 3: direct 90-degree overhead top-down view showing laces and tongue\"\n  ],\n  \"render_quality\": \"8k_resolution_sharp_textures_dual_softbox_lighting\"\n}"
      },
      "text_2x2": {
        "name": "Opción 3: Texto Plano 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "Texto • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku 511417-136 --layout 2x2",
        "prompt": "Commercial footwear catalog 2x2 grid contact sheet of authentic sneaker Nike Air Max Correlate White / New Green / Bright Mango / Black, SKU: 511417-136. Exactly 4 symmetrical panels on a seamless pure solid white background (#FFFFFF). Top-left panel: strict 90-degree lateral outer profile pointing LEFT. Top-right panel: three-quarter 3/4 perspective front-quarter facing LEFT. Bottom-left panel: direct 180-degree rear heel view centered. Bottom-right panel: direct 90-degree overhead top-down flat lay view. Identical studio softbox lighting at 5500K across all panels, subtle grounded contact shadows, razor-sharp focus across all textures, 85mm lens f/8, 8k resolution e-commerce standard, no human feet, no props."
      },
      "text_1x3": {
        "name": "Opción 4: Texto Plano 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9",
        "tag": "Texto • 16:9 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku 511417-136 --layout 1x3",
        "prompt": "Commercial footwear catalog triptych row showing exactly 3 side-by-side photographic views of the sneaker Nike Air Max Correlate White / New Green / Bright Mango / Black, SKU: 511417-136 on a pure solid white background (#FFFFFF). Panel 1 (left): strict 90-degree lateral side profile pointing LEFT. Panel 2 (center): direct 180-degree rear heel counter view with branding badge. Panel 3 (right): direct 90-degree overhead top-down flat lay view showing laces and tongue. Uniform 5500K dual softbox lighting, razor-sharp details, subtle soft contact shadow on floor, clean commercial photography, no background clutter."
      }
    },
    "negative_prompt": "distorted logos, misspelled text, fake brand badges, asymmetrical deformed sole, warped eyelets, blurry laces, colored background, gradient background, shadows on walls, studio stands, human feet, legs, hands, mannequins, socks, dirty soles, worn leather, scuffs, lowres, oversaturated, chromatic aberration, cartoon, illustration, 3d render plastic sheen"
  },
  {
    "index": 21,
    "sku": "323419-164",
    "name": "Jordan 6 Rings White / University Red / Black",
    "primary_ref": "assets/2-norm-std/323419-164/01-lateral.webp",
    "formats": {
      "json_2x2": {
        "name": "Opción 1: JSON 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "JSON • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku 323419-164 --layout 2x2",
        "prompt": "{\n  \"task\": \"commercial_footwear_catalog_quad_sheet\",\n  \"product\": {\n    \"name\": \"Jordan 6 Rings White / University Red / Black\",\n    \"sku\": \"323419-164\",\n    \"authentic\": true\n  },\n  \"layout\": {\n    \"type\": \"2x2_grid_contact_sheet\",\n    \"aspect_ratio\": \"1:1\",\n    \"background_color\": \"#FFFFFF\",\n    \"panels\": {\n      \"top_left\": \"90-degree lateral outer profile, toe pointing LEFT\",\n      \"top_right\": \"45-degree 3/4 perspective front-quarter, facing LEFT\",\n      \"bottom_left\": \"180-degree direct rear heel counter, centered\",\n      \"bottom_right\": \"90-degree overhead top-down flat lay view, laces and tongue\"\n    }\n  },\n  \"lighting\": \"neutral_softbox_5500k_studio\",\n  \"camera\": \"85mm_lens_f8_sharp_focus\",\n  \"output\": \"razor_sharp_focus_pure_white_background_subtle_contact_shadow\"\n}"
      },
      "json_1x3": {
        "name": "Opción 2: JSON 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9 o 4:3",
        "tag": "JSON • 16:9 / 4:3 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku 323419-164 --layout 1x3",
        "prompt": "{\n  \"style\": \"professional_sneaker_catalog\",\n  \"shoe\": \"Jordan 6 Rings White / University Red / Black\",\n  \"sku\": \"323419-164\",\n  \"composition\": \"horizontal_triptych_three_equal_panels\",\n  \"aspect_ratio\": \"16:9_or_4:3\",\n  \"background\": \"seamless_solid_pure_white_#FFFFFF\",\n  \"views_left_to_right\": [\n    \"Panel 1: clean lateral outer profile view with toe pointing horizontally LEFT\",\n    \"Panel 2: direct 180-degree rear heel branding badge centered\",\n    \"Panel 3: direct 90-degree overhead top-down view showing laces and tongue\"\n  ],\n  \"render_quality\": \"8k_resolution_sharp_textures_dual_softbox_lighting\"\n}"
      },
      "text_2x2": {
        "name": "Opción 3: Texto Plano 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "Texto • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku 323419-164 --layout 2x2",
        "prompt": "Commercial footwear catalog 2x2 grid contact sheet of authentic sneaker Jordan 6 Rings White / University Red / Black, SKU: 323419-164. Exactly 4 symmetrical panels on a seamless pure solid white background (#FFFFFF). Top-left panel: strict 90-degree lateral outer profile pointing LEFT. Top-right panel: three-quarter 3/4 perspective front-quarter facing LEFT. Bottom-left panel: direct 180-degree rear heel view centered. Bottom-right panel: direct 90-degree overhead top-down flat lay view. Identical studio softbox lighting at 5500K across all panels, subtle grounded contact shadows, razor-sharp focus across all textures, 85mm lens f/8, 8k resolution e-commerce standard, no human feet, no props."
      },
      "text_1x3": {
        "name": "Opción 4: Texto Plano 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9",
        "tag": "Texto • 16:9 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku 323419-164 --layout 1x3",
        "prompt": "Commercial footwear catalog triptych row showing exactly 3 side-by-side photographic views of the sneaker Jordan 6 Rings White / University Red / Black, SKU: 323419-164 on a pure solid white background (#FFFFFF). Panel 1 (left): strict 90-degree lateral side profile pointing LEFT. Panel 2 (center): direct 180-degree rear heel counter view with branding badge. Panel 3 (right): direct 90-degree overhead top-down flat lay view showing laces and tongue. Uniform 5500K dual softbox lighting, razor-sharp details, subtle soft contact shadow on floor, clean commercial photography, no background clutter."
      }
    },
    "negative_prompt": "distorted logos, misspelled text, fake brand badges, asymmetrical deformed sole, warped eyelets, blurry laces, colored background, gradient background, shadows on walls, studio stands, human feet, legs, hands, mannequins, socks, dirty soles, worn leather, scuffs, lowres, oversaturated, chromatic aberration, cartoon, illustration, 3d render plastic sheen"
  },
  {
    "index": 22,
    "sku": "IR4727-100",
    "name": "Nike Air Diamond Turf II",
    "primary_ref": "assets/2-norm-std/IR4727-100/01-lateral.webp",
    "formats": {
      "json_2x2": {
        "name": "Opción 1: JSON 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "JSON • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IR4727-100 --layout 2x2",
        "prompt": "{\n  \"task\": \"commercial_footwear_catalog_quad_sheet\",\n  \"product\": {\n    \"name\": \"Nike Air Diamond Turf II\",\n    \"sku\": \"IR4727-100\",\n    \"authentic\": true\n  },\n  \"layout\": {\n    \"type\": \"2x2_grid_contact_sheet\",\n    \"aspect_ratio\": \"1:1\",\n    \"background_color\": \"#FFFFFF\",\n    \"panels\": {\n      \"top_left\": \"90-degree lateral outer profile, toe pointing LEFT\",\n      \"top_right\": \"45-degree 3/4 perspective front-quarter, facing LEFT\",\n      \"bottom_left\": \"180-degree direct rear heel counter, centered\",\n      \"bottom_right\": \"90-degree overhead top-down flat lay view, laces and tongue\"\n    }\n  },\n  \"lighting\": \"neutral_softbox_5500k_studio\",\n  \"camera\": \"85mm_lens_f8_sharp_focus\",\n  \"output\": \"razor_sharp_focus_pure_white_background_subtle_contact_shadow\"\n}"
      },
      "json_1x3": {
        "name": "Opción 2: JSON 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9 o 4:3",
        "tag": "JSON • 16:9 / 4:3 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IR4727-100 --layout 1x3",
        "prompt": "{\n  \"style\": \"professional_sneaker_catalog\",\n  \"shoe\": \"Nike Air Diamond Turf II\",\n  \"sku\": \"IR4727-100\",\n  \"composition\": \"horizontal_triptych_three_equal_panels\",\n  \"aspect_ratio\": \"16:9_or_4:3\",\n  \"background\": \"seamless_solid_pure_white_#FFFFFF\",\n  \"views_left_to_right\": [\n    \"Panel 1: clean lateral outer profile view with toe pointing horizontally LEFT\",\n    \"Panel 2: direct 180-degree rear heel branding badge centered\",\n    \"Panel 3: direct 90-degree overhead top-down view showing laces and tongue\"\n  ],\n  \"render_quality\": \"8k_resolution_sharp_textures_dual_softbox_lighting\"\n}"
      },
      "text_2x2": {
        "name": "Opción 3: Texto Plano 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "Texto • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IR4727-100 --layout 2x2",
        "prompt": "Commercial footwear catalog 2x2 grid contact sheet of authentic sneaker Nike Air Diamond Turf II, SKU: IR4727-100. Exactly 4 symmetrical panels on a seamless pure solid white background (#FFFFFF). Top-left panel: strict 90-degree lateral outer profile pointing LEFT. Top-right panel: three-quarter 3/4 perspective front-quarter facing LEFT. Bottom-left panel: direct 180-degree rear heel view centered. Bottom-right panel: direct 90-degree overhead top-down flat lay view. Identical studio softbox lighting at 5500K across all panels, subtle grounded contact shadows, razor-sharp focus across all textures, 85mm lens f/8, 8k resolution e-commerce standard, no human feet, no props."
      },
      "text_1x3": {
        "name": "Opción 4: Texto Plano 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9",
        "tag": "Texto • 16:9 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IR4727-100 --layout 1x3",
        "prompt": "Commercial footwear catalog triptych row showing exactly 3 side-by-side photographic views of the sneaker Nike Air Diamond Turf II, SKU: IR4727-100 on a pure solid white background (#FFFFFF). Panel 1 (left): strict 90-degree lateral side profile pointing LEFT. Panel 2 (center): direct 180-degree rear heel counter view with branding badge. Panel 3 (right): direct 90-degree overhead top-down flat lay view showing laces and tongue. Uniform 5500K dual softbox lighting, razor-sharp details, subtle soft contact shadow on floor, clean commercial photography, no background clutter."
      }
    },
    "negative_prompt": "distorted logos, misspelled text, fake brand badges, asymmetrical deformed sole, warped eyelets, blurry laces, colored background, gradient background, shadows on walls, studio stands, human feet, legs, hands, mannequins, socks, dirty soles, worn leather, scuffs, lowres, oversaturated, chromatic aberration, cartoon, illustration, 3d render plastic sheen"
  },
  {
    "index": 23,
    "sku": "IR4714-100",
    "name": "Nike Air DT Max '96 Low White / Metallic",
    "primary_ref": "assets/2-norm-std/IR4714-100/01-lateral.webp",
    "formats": {
      "json_2x2": {
        "name": "Opción 1: JSON 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "JSON • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IR4714-100 --layout 2x2",
        "prompt": "{\n  \"task\": \"commercial_footwear_catalog_quad_sheet\",\n  \"product\": {\n    \"name\": \"Nike Air DT Max '96 Low White / Metallic\",\n    \"sku\": \"IR4714-100\",\n    \"authentic\": true\n  },\n  \"layout\": {\n    \"type\": \"2x2_grid_contact_sheet\",\n    \"aspect_ratio\": \"1:1\",\n    \"background_color\": \"#FFFFFF\",\n    \"panels\": {\n      \"top_left\": \"90-degree lateral outer profile, toe pointing LEFT\",\n      \"top_right\": \"45-degree 3/4 perspective front-quarter, facing LEFT\",\n      \"bottom_left\": \"180-degree direct rear heel counter, centered\",\n      \"bottom_right\": \"90-degree overhead top-down flat lay view, laces and tongue\"\n    }\n  },\n  \"lighting\": \"neutral_softbox_5500k_studio\",\n  \"camera\": \"85mm_lens_f8_sharp_focus\",\n  \"output\": \"razor_sharp_focus_pure_white_background_subtle_contact_shadow\"\n}"
      },
      "json_1x3": {
        "name": "Opción 2: JSON 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9 o 4:3",
        "tag": "JSON • 16:9 / 4:3 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IR4714-100 --layout 1x3",
        "prompt": "{\n  \"style\": \"professional_sneaker_catalog\",\n  \"shoe\": \"Nike Air DT Max '96 Low White / Metallic\",\n  \"sku\": \"IR4714-100\",\n  \"composition\": \"horizontal_triptych_three_equal_panels\",\n  \"aspect_ratio\": \"16:9_or_4:3\",\n  \"background\": \"seamless_solid_pure_white_#FFFFFF\",\n  \"views_left_to_right\": [\n    \"Panel 1: clean lateral outer profile view with toe pointing horizontally LEFT\",\n    \"Panel 2: direct 180-degree rear heel branding badge centered\",\n    \"Panel 3: direct 90-degree overhead top-down view showing laces and tongue\"\n  ],\n  \"render_quality\": \"8k_resolution_sharp_textures_dual_softbox_lighting\"\n}"
      },
      "text_2x2": {
        "name": "Opción 3: Texto Plano 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "Texto • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IR4714-100 --layout 2x2",
        "prompt": "Commercial footwear catalog 2x2 grid contact sheet of authentic sneaker Nike Air DT Max '96 Low White / Metallic, SKU: IR4714-100. Exactly 4 symmetrical panels on a seamless pure solid white background (#FFFFFF). Top-left panel: strict 90-degree lateral outer profile pointing LEFT. Top-right panel: three-quarter 3/4 perspective front-quarter facing LEFT. Bottom-left panel: direct 180-degree rear heel view centered. Bottom-right panel: direct 90-degree overhead top-down flat lay view. Identical studio softbox lighting at 5500K across all panels, subtle grounded contact shadows, razor-sharp focus across all textures, 85mm lens f/8, 8k resolution e-commerce standard, no human feet, no props."
      },
      "text_1x3": {
        "name": "Opción 4: Texto Plano 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9",
        "tag": "Texto • 16:9 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IR4714-100 --layout 1x3",
        "prompt": "Commercial footwear catalog triptych row showing exactly 3 side-by-side photographic views of the sneaker Nike Air DT Max '96 Low White / Metallic, SKU: IR4714-100 on a pure solid white background (#FFFFFF). Panel 1 (left): strict 90-degree lateral side profile pointing LEFT. Panel 2 (center): direct 180-degree rear heel counter view with branding badge. Panel 3 (right): direct 90-degree overhead top-down flat lay view showing laces and tongue. Uniform 5500K dual softbox lighting, razor-sharp details, subtle soft contact shadow on floor, clean commercial photography, no background clutter."
      }
    },
    "negative_prompt": "distorted logos, misspelled text, fake brand badges, asymmetrical deformed sole, warped eyelets, blurry laces, colored background, gradient background, shadows on walls, studio stands, human feet, legs, hands, mannequins, socks, dirty soles, worn leather, scuffs, lowres, oversaturated, chromatic aberration, cartoon, illustration, 3d render plastic sheen"
  },
  {
    "index": 24,
    "sku": "DR8784-005",
    "name": "Nike Zoom LeBron NXXT Gen \"Black Wolf Grey\"",
    "primary_ref": "assets/2-norm-std/DR8784-005/01-lateral.webp",
    "formats": {
      "json_2x2": {
        "name": "Opción 1: JSON 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "JSON • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku DR8784-005 --layout 2x2",
        "prompt": "{\n  \"task\": \"commercial_footwear_catalog_quad_sheet\",\n  \"product\": {\n    \"name\": \"Nike Zoom LeBron NXXT Gen \\\"Black Wolf Grey\\\"\",\n    \"sku\": \"DR8784-005\",\n    \"authentic\": true\n  },\n  \"layout\": {\n    \"type\": \"2x2_grid_contact_sheet\",\n    \"aspect_ratio\": \"1:1\",\n    \"background_color\": \"#FFFFFF\",\n    \"panels\": {\n      \"top_left\": \"90-degree lateral outer profile, toe pointing LEFT\",\n      \"top_right\": \"45-degree 3/4 perspective front-quarter, facing LEFT\",\n      \"bottom_left\": \"180-degree direct rear heel counter, centered\",\n      \"bottom_right\": \"90-degree overhead top-down flat lay view, laces and tongue\"\n    }\n  },\n  \"lighting\": \"neutral_softbox_5500k_studio\",\n  \"camera\": \"85mm_lens_f8_sharp_focus\",\n  \"output\": \"razor_sharp_focus_pure_white_background_subtle_contact_shadow\"\n}"
      },
      "json_1x3": {
        "name": "Opción 2: JSON 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9 o 4:3",
        "tag": "JSON • 16:9 / 4:3 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku DR8784-005 --layout 1x3",
        "prompt": "{\n  \"style\": \"professional_sneaker_catalog\",\n  \"shoe\": \"Nike Zoom LeBron NXXT Gen \\\"Black Wolf Grey\\\"\",\n  \"sku\": \"DR8784-005\",\n  \"composition\": \"horizontal_triptych_three_equal_panels\",\n  \"aspect_ratio\": \"16:9_or_4:3\",\n  \"background\": \"seamless_solid_pure_white_#FFFFFF\",\n  \"views_left_to_right\": [\n    \"Panel 1: clean lateral outer profile view with toe pointing horizontally LEFT\",\n    \"Panel 2: direct 180-degree rear heel branding badge centered\",\n    \"Panel 3: direct 90-degree overhead top-down view showing laces and tongue\"\n  ],\n  \"render_quality\": \"8k_resolution_sharp_textures_dual_softbox_lighting\"\n}"
      },
      "text_2x2": {
        "name": "Opción 3: Texto Plano 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "Texto • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku DR8784-005 --layout 2x2",
        "prompt": "Commercial footwear catalog 2x2 grid contact sheet of authentic sneaker Nike Zoom LeBron NXXT Gen \"Black Wolf Grey\", SKU: DR8784-005. Exactly 4 symmetrical panels on a seamless pure solid white background (#FFFFFF). Top-left panel: strict 90-degree lateral outer profile pointing LEFT. Top-right panel: three-quarter 3/4 perspective front-quarter facing LEFT. Bottom-left panel: direct 180-degree rear heel view centered. Bottom-right panel: direct 90-degree overhead top-down flat lay view. Identical studio softbox lighting at 5500K across all panels, subtle grounded contact shadows, razor-sharp focus across all textures, 85mm lens f/8, 8k resolution e-commerce standard, no human feet, no props."
      },
      "text_1x3": {
        "name": "Opción 4: Texto Plano 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9",
        "tag": "Texto • 16:9 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku DR8784-005 --layout 1x3",
        "prompt": "Commercial footwear catalog triptych row showing exactly 3 side-by-side photographic views of the sneaker Nike Zoom LeBron NXXT Gen \"Black Wolf Grey\", SKU: DR8784-005 on a pure solid white background (#FFFFFF). Panel 1 (left): strict 90-degree lateral side profile pointing LEFT. Panel 2 (center): direct 180-degree rear heel counter view with branding badge. Panel 3 (right): direct 90-degree overhead top-down flat lay view showing laces and tongue. Uniform 5500K dual softbox lighting, razor-sharp details, subtle soft contact shadow on floor, clean commercial photography, no background clutter."
      }
    },
    "negative_prompt": "distorted logos, misspelled text, fake brand badges, asymmetrical deformed sole, warped eyelets, blurry laces, colored background, gradient background, shadows on walls, studio stands, human feet, legs, hands, mannequins, socks, dirty soles, worn leather, scuffs, lowres, oversaturated, chromatic aberration, cartoon, illustration, 3d render plastic sheen"
  },
  {
    "index": 25,
    "sku": "AR3762-001",
    "name": "Air Jordan Access \"Black Gym Red\"",
    "primary_ref": "assets/2-norm-std/AR3762-001/01-lateral.webp",
    "formats": {
      "json_2x2": {
        "name": "Opción 1: JSON 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "JSON • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku AR3762-001 --layout 2x2",
        "prompt": "{\n  \"task\": \"commercial_footwear_catalog_quad_sheet\",\n  \"product\": {\n    \"name\": \"Air Jordan Access \\\"Black Gym Red\\\"\",\n    \"sku\": \"AR3762-001\",\n    \"authentic\": true\n  },\n  \"layout\": {\n    \"type\": \"2x2_grid_contact_sheet\",\n    \"aspect_ratio\": \"1:1\",\n    \"background_color\": \"#FFFFFF\",\n    \"panels\": {\n      \"top_left\": \"90-degree lateral outer profile, toe pointing LEFT\",\n      \"top_right\": \"45-degree 3/4 perspective front-quarter, facing LEFT\",\n      \"bottom_left\": \"180-degree direct rear heel counter, centered\",\n      \"bottom_right\": \"90-degree overhead top-down flat lay view, laces and tongue\"\n    }\n  },\n  \"lighting\": \"neutral_softbox_5500k_studio\",\n  \"camera\": \"85mm_lens_f8_sharp_focus\",\n  \"output\": \"razor_sharp_focus_pure_white_background_subtle_contact_shadow\"\n}"
      },
      "json_1x3": {
        "name": "Opción 2: JSON 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9 o 4:3",
        "tag": "JSON • 16:9 / 4:3 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku AR3762-001 --layout 1x3",
        "prompt": "{\n  \"style\": \"professional_sneaker_catalog\",\n  \"shoe\": \"Air Jordan Access \\\"Black Gym Red\\\"\",\n  \"sku\": \"AR3762-001\",\n  \"composition\": \"horizontal_triptych_three_equal_panels\",\n  \"aspect_ratio\": \"16:9_or_4:3\",\n  \"background\": \"seamless_solid_pure_white_#FFFFFF\",\n  \"views_left_to_right\": [\n    \"Panel 1: clean lateral outer profile view with toe pointing horizontally LEFT\",\n    \"Panel 2: direct 180-degree rear heel branding badge centered\",\n    \"Panel 3: direct 90-degree overhead top-down view showing laces and tongue\"\n  ],\n  \"render_quality\": \"8k_resolution_sharp_textures_dual_softbox_lighting\"\n}"
      },
      "text_2x2": {
        "name": "Opción 3: Texto Plano 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "Texto • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku AR3762-001 --layout 2x2",
        "prompt": "Commercial footwear catalog 2x2 grid contact sheet of authentic sneaker Air Jordan Access \"Black Gym Red\", SKU: AR3762-001. Exactly 4 symmetrical panels on a seamless pure solid white background (#FFFFFF). Top-left panel: strict 90-degree lateral outer profile pointing LEFT. Top-right panel: three-quarter 3/4 perspective front-quarter facing LEFT. Bottom-left panel: direct 180-degree rear heel view centered. Bottom-right panel: direct 90-degree overhead top-down flat lay view. Identical studio softbox lighting at 5500K across all panels, subtle grounded contact shadows, razor-sharp focus across all textures, 85mm lens f/8, 8k resolution e-commerce standard, no human feet, no props."
      },
      "text_1x3": {
        "name": "Opción 4: Texto Plano 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9",
        "tag": "Texto • 16:9 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku AR3762-001 --layout 1x3",
        "prompt": "Commercial footwear catalog triptych row showing exactly 3 side-by-side photographic views of the sneaker Air Jordan Access \"Black Gym Red\", SKU: AR3762-001 on a pure solid white background (#FFFFFF). Panel 1 (left): strict 90-degree lateral side profile pointing LEFT. Panel 2 (center): direct 180-degree rear heel counter view with branding badge. Panel 3 (right): direct 90-degree overhead top-down flat lay view showing laces and tongue. Uniform 5500K dual softbox lighting, razor-sharp details, subtle soft contact shadow on floor, clean commercial photography, no background clutter."
      }
    },
    "negative_prompt": "distorted logos, misspelled text, fake brand badges, asymmetrical deformed sole, warped eyelets, blurry laces, colored background, gradient background, shadows on walls, studio stands, human feet, legs, hands, mannequins, socks, dirty soles, worn leather, scuffs, lowres, oversaturated, chromatic aberration, cartoon, illustration, 3d render plastic sheen"
  },
  {
    "index": 26,
    "sku": "IV5197-201",
    "name": "Nike Air Force 1 '07 Light British Tan / Sail / Hemp / Metallic Gold",
    "primary_ref": "assets/2-norm-std/IV5197-201/01-lateral.webp",
    "formats": {
      "json_2x2": {
        "name": "Opción 1: JSON 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "JSON • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IV5197-201 --layout 2x2",
        "prompt": "{\n  \"task\": \"commercial_footwear_catalog_quad_sheet\",\n  \"product\": {\n    \"name\": \"Nike Air Force 1 '07 Light British Tan / Sail / Hemp / Metallic Gold\",\n    \"sku\": \"IV5197-201\",\n    \"authentic\": true\n  },\n  \"layout\": {\n    \"type\": \"2x2_grid_contact_sheet\",\n    \"aspect_ratio\": \"1:1\",\n    \"background_color\": \"#FFFFFF\",\n    \"panels\": {\n      \"top_left\": \"90-degree lateral outer profile, toe pointing LEFT\",\n      \"top_right\": \"45-degree 3/4 perspective front-quarter, facing LEFT\",\n      \"bottom_left\": \"180-degree direct rear heel counter, centered\",\n      \"bottom_right\": \"90-degree overhead top-down flat lay view, laces and tongue\"\n    }\n  },\n  \"lighting\": \"neutral_softbox_5500k_studio\",\n  \"camera\": \"85mm_lens_f8_sharp_focus\",\n  \"output\": \"razor_sharp_focus_pure_white_background_subtle_contact_shadow\"\n}"
      },
      "json_1x3": {
        "name": "Opción 2: JSON 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9 o 4:3",
        "tag": "JSON • 16:9 / 4:3 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IV5197-201 --layout 1x3",
        "prompt": "{\n  \"style\": \"professional_sneaker_catalog\",\n  \"shoe\": \"Nike Air Force 1 '07 Light British Tan / Sail / Hemp / Metallic Gold\",\n  \"sku\": \"IV5197-201\",\n  \"composition\": \"horizontal_triptych_three_equal_panels\",\n  \"aspect_ratio\": \"16:9_or_4:3\",\n  \"background\": \"seamless_solid_pure_white_#FFFFFF\",\n  \"views_left_to_right\": [\n    \"Panel 1: clean lateral outer profile view with toe pointing horizontally LEFT\",\n    \"Panel 2: direct 180-degree rear heel branding badge centered\",\n    \"Panel 3: direct 90-degree overhead top-down view showing laces and tongue\"\n  ],\n  \"render_quality\": \"8k_resolution_sharp_textures_dual_softbox_lighting\"\n}"
      },
      "text_2x2": {
        "name": "Opción 3: Texto Plano 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "Texto • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IV5197-201 --layout 2x2",
        "prompt": "Commercial footwear catalog 2x2 grid contact sheet of authentic sneaker Nike Air Force 1 '07 Light British Tan / Sail / Hemp / Metallic Gold, SKU: IV5197-201. Exactly 4 symmetrical panels on a seamless pure solid white background (#FFFFFF). Top-left panel: strict 90-degree lateral outer profile pointing LEFT. Top-right panel: three-quarter 3/4 perspective front-quarter facing LEFT. Bottom-left panel: direct 180-degree rear heel view centered. Bottom-right panel: direct 90-degree overhead top-down flat lay view. Identical studio softbox lighting at 5500K across all panels, subtle grounded contact shadows, razor-sharp focus across all textures, 85mm lens f/8, 8k resolution e-commerce standard, no human feet, no props."
      },
      "text_1x3": {
        "name": "Opción 4: Texto Plano 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9",
        "tag": "Texto • 16:9 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IV5197-201 --layout 1x3",
        "prompt": "Commercial footwear catalog triptych row showing exactly 3 side-by-side photographic views of the sneaker Nike Air Force 1 '07 Light British Tan / Sail / Hemp / Metallic Gold, SKU: IV5197-201 on a pure solid white background (#FFFFFF). Panel 1 (left): strict 90-degree lateral side profile pointing LEFT. Panel 2 (center): direct 180-degree rear heel counter view with branding badge. Panel 3 (right): direct 90-degree overhead top-down flat lay view showing laces and tongue. Uniform 5500K dual softbox lighting, razor-sharp details, subtle soft contact shadow on floor, clean commercial photography, no background clutter."
      }
    },
    "negative_prompt": "distorted logos, misspelled text, fake brand badges, asymmetrical deformed sole, warped eyelets, blurry laces, colored background, gradient background, shadows on walls, studio stands, human feet, legs, hands, mannequins, socks, dirty soles, worn leather, scuffs, lowres, oversaturated, chromatic aberration, cartoon, illustration, 3d render plastic sheen"
  },
  {
    "index": 27,
    "sku": "CU4152-101",
    "name": "Nike Air Max Bolt",
    "primary_ref": "assets/2-norm-std/CU4152-101/01-lateral.webp",
    "formats": {
      "json_2x2": {
        "name": "Opción 1: JSON 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "JSON • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku CU4152-101 --layout 2x2",
        "prompt": "{\n  \"task\": \"commercial_footwear_catalog_quad_sheet\",\n  \"product\": {\n    \"name\": \"Nike Air Max Bolt\",\n    \"sku\": \"CU4152-101\",\n    \"authentic\": true\n  },\n  \"layout\": {\n    \"type\": \"2x2_grid_contact_sheet\",\n    \"aspect_ratio\": \"1:1\",\n    \"background_color\": \"#FFFFFF\",\n    \"panels\": {\n      \"top_left\": \"90-degree lateral outer profile, toe pointing LEFT\",\n      \"top_right\": \"45-degree 3/4 perspective front-quarter, facing LEFT\",\n      \"bottom_left\": \"180-degree direct rear heel counter, centered\",\n      \"bottom_right\": \"90-degree overhead top-down flat lay view, laces and tongue\"\n    }\n  },\n  \"lighting\": \"neutral_softbox_5500k_studio\",\n  \"camera\": \"85mm_lens_f8_sharp_focus\",\n  \"output\": \"razor_sharp_focus_pure_white_background_subtle_contact_shadow\"\n}"
      },
      "json_1x3": {
        "name": "Opción 2: JSON 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9 o 4:3",
        "tag": "JSON • 16:9 / 4:3 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku CU4152-101 --layout 1x3",
        "prompt": "{\n  \"style\": \"professional_sneaker_catalog\",\n  \"shoe\": \"Nike Air Max Bolt\",\n  \"sku\": \"CU4152-101\",\n  \"composition\": \"horizontal_triptych_three_equal_panels\",\n  \"aspect_ratio\": \"16:9_or_4:3\",\n  \"background\": \"seamless_solid_pure_white_#FFFFFF\",\n  \"views_left_to_right\": [\n    \"Panel 1: clean lateral outer profile view with toe pointing horizontally LEFT\",\n    \"Panel 2: direct 180-degree rear heel branding badge centered\",\n    \"Panel 3: direct 90-degree overhead top-down view showing laces and tongue\"\n  ],\n  \"render_quality\": \"8k_resolution_sharp_textures_dual_softbox_lighting\"\n}"
      },
      "text_2x2": {
        "name": "Opción 3: Texto Plano 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "Texto • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku CU4152-101 --layout 2x2",
        "prompt": "Commercial footwear catalog 2x2 grid contact sheet of authentic sneaker Nike Air Max Bolt, SKU: CU4152-101. Exactly 4 symmetrical panels on a seamless pure solid white background (#FFFFFF). Top-left panel: strict 90-degree lateral outer profile pointing LEFT. Top-right panel: three-quarter 3/4 perspective front-quarter facing LEFT. Bottom-left panel: direct 180-degree rear heel view centered. Bottom-right panel: direct 90-degree overhead top-down flat lay view. Identical studio softbox lighting at 5500K across all panels, subtle grounded contact shadows, razor-sharp focus across all textures, 85mm lens f/8, 8k resolution e-commerce standard, no human feet, no props."
      },
      "text_1x3": {
        "name": "Opción 4: Texto Plano 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9",
        "tag": "Texto • 16:9 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku CU4152-101 --layout 1x3",
        "prompt": "Commercial footwear catalog triptych row showing exactly 3 side-by-side photographic views of the sneaker Nike Air Max Bolt, SKU: CU4152-101 on a pure solid white background (#FFFFFF). Panel 1 (left): strict 90-degree lateral side profile pointing LEFT. Panel 2 (center): direct 180-degree rear heel counter view with branding badge. Panel 3 (right): direct 90-degree overhead top-down flat lay view showing laces and tongue. Uniform 5500K dual softbox lighting, razor-sharp details, subtle soft contact shadow on floor, clean commercial photography, no background clutter."
      }
    },
    "negative_prompt": "distorted logos, misspelled text, fake brand badges, asymmetrical deformed sole, warped eyelets, blurry laces, colored background, gradient background, shadows on walls, studio stands, human feet, legs, hands, mannequins, socks, dirty soles, worn leather, scuffs, lowres, oversaturated, chromatic aberration, cartoon, illustration, 3d render plastic sheen"
  },
  {
    "index": 28,
    "sku": "AR4430-101",
    "name": "Jordan Lift Off White / Black / Wolf Grey",
    "primary_ref": "assets/2-norm-std/AR4430-101/01-lateral.webp",
    "formats": {
      "json_2x2": {
        "name": "Opción 1: JSON 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "JSON • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku AR4430-101 --layout 2x2",
        "prompt": "{\n  \"task\": \"commercial_footwear_catalog_quad_sheet\",\n  \"product\": {\n    \"name\": \"Jordan Lift Off White / Black / Wolf Grey\",\n    \"sku\": \"AR4430-101\",\n    \"authentic\": true\n  },\n  \"layout\": {\n    \"type\": \"2x2_grid_contact_sheet\",\n    \"aspect_ratio\": \"1:1\",\n    \"background_color\": \"#FFFFFF\",\n    \"panels\": {\n      \"top_left\": \"90-degree lateral outer profile, toe pointing LEFT\",\n      \"top_right\": \"45-degree 3/4 perspective front-quarter, facing LEFT\",\n      \"bottom_left\": \"180-degree direct rear heel counter, centered\",\n      \"bottom_right\": \"90-degree overhead top-down flat lay view, laces and tongue\"\n    }\n  },\n  \"lighting\": \"neutral_softbox_5500k_studio\",\n  \"camera\": \"85mm_lens_f8_sharp_focus\",\n  \"output\": \"razor_sharp_focus_pure_white_background_subtle_contact_shadow\"\n}"
      },
      "json_1x3": {
        "name": "Opción 2: JSON 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9 o 4:3",
        "tag": "JSON • 16:9 / 4:3 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku AR4430-101 --layout 1x3",
        "prompt": "{\n  \"style\": \"professional_sneaker_catalog\",\n  \"shoe\": \"Jordan Lift Off White / Black / Wolf Grey\",\n  \"sku\": \"AR4430-101\",\n  \"composition\": \"horizontal_triptych_three_equal_panels\",\n  \"aspect_ratio\": \"16:9_or_4:3\",\n  \"background\": \"seamless_solid_pure_white_#FFFFFF\",\n  \"views_left_to_right\": [\n    \"Panel 1: clean lateral outer profile view with toe pointing horizontally LEFT\",\n    \"Panel 2: direct 180-degree rear heel branding badge centered\",\n    \"Panel 3: direct 90-degree overhead top-down view showing laces and tongue\"\n  ],\n  \"render_quality\": \"8k_resolution_sharp_textures_dual_softbox_lighting\"\n}"
      },
      "text_2x2": {
        "name": "Opción 3: Texto Plano 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "Texto • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku AR4430-101 --layout 2x2",
        "prompt": "Commercial footwear catalog 2x2 grid contact sheet of authentic sneaker Jordan Lift Off White / Black / Wolf Grey, SKU: AR4430-101. Exactly 4 symmetrical panels on a seamless pure solid white background (#FFFFFF). Top-left panel: strict 90-degree lateral outer profile pointing LEFT. Top-right panel: three-quarter 3/4 perspective front-quarter facing LEFT. Bottom-left panel: direct 180-degree rear heel view centered. Bottom-right panel: direct 90-degree overhead top-down flat lay view. Identical studio softbox lighting at 5500K across all panels, subtle grounded contact shadows, razor-sharp focus across all textures, 85mm lens f/8, 8k resolution e-commerce standard, no human feet, no props."
      },
      "text_1x3": {
        "name": "Opción 4: Texto Plano 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9",
        "tag": "Texto • 16:9 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku AR4430-101 --layout 1x3",
        "prompt": "Commercial footwear catalog triptych row showing exactly 3 side-by-side photographic views of the sneaker Jordan Lift Off White / Black / Wolf Grey, SKU: AR4430-101 on a pure solid white background (#FFFFFF). Panel 1 (left): strict 90-degree lateral side profile pointing LEFT. Panel 2 (center): direct 180-degree rear heel counter view with branding badge. Panel 3 (right): direct 90-degree overhead top-down flat lay view showing laces and tongue. Uniform 5500K dual softbox lighting, razor-sharp details, subtle soft contact shadow on floor, clean commercial photography, no background clutter."
      }
    },
    "negative_prompt": "distorted logos, misspelled text, fake brand badges, asymmetrical deformed sole, warped eyelets, blurry laces, colored background, gradient background, shadows on walls, studio stands, human feet, legs, hands, mannequins, socks, dirty soles, worn leather, scuffs, lowres, oversaturated, chromatic aberration, cartoon, illustration, 3d render plastic sheen"
  },
  {
    "index": 29,
    "sku": "DM0967-111",
    "name": "Air Jordan 3 Retro \"Pure Money\"",
    "primary_ref": "assets/2-norm-std/DM0967-111/01-lateral.webp",
    "formats": {
      "json_2x2": {
        "name": "Opción 1: JSON 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "JSON • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku DM0967-111 --layout 2x2",
        "prompt": "{\n  \"task\": \"commercial_footwear_catalog_quad_sheet\",\n  \"product\": {\n    \"name\": \"Air Jordan 3 Retro \\\"Pure Money\\\"\",\n    \"sku\": \"DM0967-111\",\n    \"authentic\": true\n  },\n  \"layout\": {\n    \"type\": \"2x2_grid_contact_sheet\",\n    \"aspect_ratio\": \"1:1\",\n    \"background_color\": \"#FFFFFF\",\n    \"panels\": {\n      \"top_left\": \"90-degree lateral outer profile, toe pointing LEFT\",\n      \"top_right\": \"45-degree 3/4 perspective front-quarter, facing LEFT\",\n      \"bottom_left\": \"180-degree direct rear heel counter, centered\",\n      \"bottom_right\": \"90-degree overhead top-down flat lay view, laces and tongue\"\n    }\n  },\n  \"lighting\": \"neutral_softbox_5500k_studio\",\n  \"camera\": \"85mm_lens_f8_sharp_focus\",\n  \"output\": \"razor_sharp_focus_pure_white_background_subtle_contact_shadow\"\n}"
      },
      "json_1x3": {
        "name": "Opción 2: JSON 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9 o 4:3",
        "tag": "JSON • 16:9 / 4:3 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku DM0967-111 --layout 1x3",
        "prompt": "{\n  \"style\": \"professional_sneaker_catalog\",\n  \"shoe\": \"Air Jordan 3 Retro \\\"Pure Money\\\"\",\n  \"sku\": \"DM0967-111\",\n  \"composition\": \"horizontal_triptych_three_equal_panels\",\n  \"aspect_ratio\": \"16:9_or_4:3\",\n  \"background\": \"seamless_solid_pure_white_#FFFFFF\",\n  \"views_left_to_right\": [\n    \"Panel 1: clean lateral outer profile view with toe pointing horizontally LEFT\",\n    \"Panel 2: direct 180-degree rear heel branding badge centered\",\n    \"Panel 3: direct 90-degree overhead top-down view showing laces and tongue\"\n  ],\n  \"render_quality\": \"8k_resolution_sharp_textures_dual_softbox_lighting\"\n}"
      },
      "text_2x2": {
        "name": "Opción 3: Texto Plano 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "Texto • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku DM0967-111 --layout 2x2",
        "prompt": "Commercial footwear catalog 2x2 grid contact sheet of authentic sneaker Air Jordan 3 Retro \"Pure Money\", SKU: DM0967-111. Exactly 4 symmetrical panels on a seamless pure solid white background (#FFFFFF). Top-left panel: strict 90-degree lateral outer profile pointing LEFT. Top-right panel: three-quarter 3/4 perspective front-quarter facing LEFT. Bottom-left panel: direct 180-degree rear heel view centered. Bottom-right panel: direct 90-degree overhead top-down flat lay view. Identical studio softbox lighting at 5500K across all panels, subtle grounded contact shadows, razor-sharp focus across all textures, 85mm lens f/8, 8k resolution e-commerce standard, no human feet, no props."
      },
      "text_1x3": {
        "name": "Opción 4: Texto Plano 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9",
        "tag": "Texto • 16:9 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku DM0967-111 --layout 1x3",
        "prompt": "Commercial footwear catalog triptych row showing exactly 3 side-by-side photographic views of the sneaker Air Jordan 3 Retro \"Pure Money\", SKU: DM0967-111 on a pure solid white background (#FFFFFF). Panel 1 (left): strict 90-degree lateral side profile pointing LEFT. Panel 2 (center): direct 180-degree rear heel counter view with branding badge. Panel 3 (right): direct 90-degree overhead top-down flat lay view showing laces and tongue. Uniform 5500K dual softbox lighting, razor-sharp details, subtle soft contact shadow on floor, clean commercial photography, no background clutter."
      }
    },
    "negative_prompt": "distorted logos, misspelled text, fake brand badges, asymmetrical deformed sole, warped eyelets, blurry laces, colored background, gradient background, shadows on walls, studio stands, human feet, legs, hands, mannequins, socks, dirty soles, worn leather, scuffs, lowres, oversaturated, chromatic aberration, cartoon, illustration, 3d render plastic sheen"
  },
  {
    "index": 30,
    "sku": "553560-081",
    "name": "Air Jordan 1 Low \"Shattered Backboard Alternate\"",
    "primary_ref": "assets/2-norm-std/553560-081/01-lateral.webp",
    "formats": {
      "json_2x2": {
        "name": "Opción 1: JSON 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "JSON • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku 553560-081 --layout 2x2",
        "prompt": "{\n  \"task\": \"commercial_footwear_catalog_quad_sheet\",\n  \"product\": {\n    \"name\": \"Air Jordan 1 Low \\\"Shattered Backboard Alternate\\\"\",\n    \"sku\": \"553560-081\",\n    \"authentic\": true\n  },\n  \"layout\": {\n    \"type\": \"2x2_grid_contact_sheet\",\n    \"aspect_ratio\": \"1:1\",\n    \"background_color\": \"#FFFFFF\",\n    \"panels\": {\n      \"top_left\": \"90-degree lateral outer profile, toe pointing LEFT\",\n      \"top_right\": \"45-degree 3/4 perspective front-quarter, facing LEFT\",\n      \"bottom_left\": \"180-degree direct rear heel counter, centered\",\n      \"bottom_right\": \"90-degree overhead top-down flat lay view, laces and tongue\"\n    }\n  },\n  \"lighting\": \"neutral_softbox_5500k_studio\",\n  \"camera\": \"85mm_lens_f8_sharp_focus\",\n  \"output\": \"razor_sharp_focus_pure_white_background_subtle_contact_shadow\"\n}"
      },
      "json_1x3": {
        "name": "Opción 2: JSON 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9 o 4:3",
        "tag": "JSON • 16:9 / 4:3 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku 553560-081 --layout 1x3",
        "prompt": "{\n  \"style\": \"professional_sneaker_catalog\",\n  \"shoe\": \"Air Jordan 1 Low \\\"Shattered Backboard Alternate\\\"\",\n  \"sku\": \"553560-081\",\n  \"composition\": \"horizontal_triptych_three_equal_panels\",\n  \"aspect_ratio\": \"16:9_or_4:3\",\n  \"background\": \"seamless_solid_pure_white_#FFFFFF\",\n  \"views_left_to_right\": [\n    \"Panel 1: clean lateral outer profile view with toe pointing horizontally LEFT\",\n    \"Panel 2: direct 180-degree rear heel branding badge centered\",\n    \"Panel 3: direct 90-degree overhead top-down view showing laces and tongue\"\n  ],\n  \"render_quality\": \"8k_resolution_sharp_textures_dual_softbox_lighting\"\n}"
      },
      "text_2x2": {
        "name": "Opción 3: Texto Plano 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "Texto • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku 553560-081 --layout 2x2",
        "prompt": "Commercial footwear catalog 2x2 grid contact sheet of authentic sneaker Air Jordan 1 Low \"Shattered Backboard Alternate\", SKU: 553560-081. Exactly 4 symmetrical panels on a seamless pure solid white background (#FFFFFF). Top-left panel: strict 90-degree lateral outer profile pointing LEFT. Top-right panel: three-quarter 3/4 perspective front-quarter facing LEFT. Bottom-left panel: direct 180-degree rear heel view centered. Bottom-right panel: direct 90-degree overhead top-down flat lay view. Identical studio softbox lighting at 5500K across all panels, subtle grounded contact shadows, razor-sharp focus across all textures, 85mm lens f/8, 8k resolution e-commerce standard, no human feet, no props."
      },
      "text_1x3": {
        "name": "Opción 4: Texto Plano 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9",
        "tag": "Texto • 16:9 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku 553560-081 --layout 1x3",
        "prompt": "Commercial footwear catalog triptych row showing exactly 3 side-by-side photographic views of the sneaker Air Jordan 1 Low \"Shattered Backboard Alternate\", SKU: 553560-081 on a pure solid white background (#FFFFFF). Panel 1 (left): strict 90-degree lateral side profile pointing LEFT. Panel 2 (center): direct 180-degree rear heel counter view with branding badge. Panel 3 (right): direct 90-degree overhead top-down flat lay view showing laces and tongue. Uniform 5500K dual softbox lighting, razor-sharp details, subtle soft contact shadow on floor, clean commercial photography, no background clutter."
      }
    },
    "negative_prompt": "distorted logos, misspelled text, fake brand badges, asymmetrical deformed sole, warped eyelets, blurry laces, colored background, gradient background, shadows on walls, studio stands, human feet, legs, hands, mannequins, socks, dirty soles, worn leather, scuffs, lowres, oversaturated, chromatic aberration, cartoon, illustration, 3d render plastic sheen"
  },
  {
    "index": 31,
    "sku": "HV4775-001",
    "name": "Air Jordan 1 Low \"Inner Beast\"",
    "primary_ref": "assets/2-norm-std/HV4775-001/01-lateral.webp",
    "formats": {
      "json_2x2": {
        "name": "Opción 1: JSON 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "JSON • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku HV4775-001 --layout 2x2",
        "prompt": "{\n  \"task\": \"commercial_footwear_catalog_quad_sheet\",\n  \"product\": {\n    \"name\": \"Air Jordan 1 Low \\\"Inner Beast\\\"\",\n    \"sku\": \"HV4775-001\",\n    \"authentic\": true\n  },\n  \"layout\": {\n    \"type\": \"2x2_grid_contact_sheet\",\n    \"aspect_ratio\": \"1:1\",\n    \"background_color\": \"#FFFFFF\",\n    \"panels\": {\n      \"top_left\": \"90-degree lateral outer profile, toe pointing LEFT\",\n      \"top_right\": \"45-degree 3/4 perspective front-quarter, facing LEFT\",\n      \"bottom_left\": \"180-degree direct rear heel counter, centered\",\n      \"bottom_right\": \"90-degree overhead top-down flat lay view, laces and tongue\"\n    }\n  },\n  \"lighting\": \"neutral_softbox_5500k_studio\",\n  \"camera\": \"85mm_lens_f8_sharp_focus\",\n  \"output\": \"razor_sharp_focus_pure_white_background_subtle_contact_shadow\"\n}"
      },
      "json_1x3": {
        "name": "Opción 2: JSON 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9 o 4:3",
        "tag": "JSON • 16:9 / 4:3 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku HV4775-001 --layout 1x3",
        "prompt": "{\n  \"style\": \"professional_sneaker_catalog\",\n  \"shoe\": \"Air Jordan 1 Low \\\"Inner Beast\\\"\",\n  \"sku\": \"HV4775-001\",\n  \"composition\": \"horizontal_triptych_three_equal_panels\",\n  \"aspect_ratio\": \"16:9_or_4:3\",\n  \"background\": \"seamless_solid_pure_white_#FFFFFF\",\n  \"views_left_to_right\": [\n    \"Panel 1: clean lateral outer profile view with toe pointing horizontally LEFT\",\n    \"Panel 2: direct 180-degree rear heel branding badge centered\",\n    \"Panel 3: direct 90-degree overhead top-down view showing laces and tongue\"\n  ],\n  \"render_quality\": \"8k_resolution_sharp_textures_dual_softbox_lighting\"\n}"
      },
      "text_2x2": {
        "name": "Opción 3: Texto Plano 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "Texto • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku HV4775-001 --layout 2x2",
        "prompt": "Commercial footwear catalog 2x2 grid contact sheet of authentic sneaker Air Jordan 1 Low \"Inner Beast\", SKU: HV4775-001. Exactly 4 symmetrical panels on a seamless pure solid white background (#FFFFFF). Top-left panel: strict 90-degree lateral outer profile pointing LEFT. Top-right panel: three-quarter 3/4 perspective front-quarter facing LEFT. Bottom-left panel: direct 180-degree rear heel view centered. Bottom-right panel: direct 90-degree overhead top-down flat lay view. Identical studio softbox lighting at 5500K across all panels, subtle grounded contact shadows, razor-sharp focus across all textures, 85mm lens f/8, 8k resolution e-commerce standard, no human feet, no props."
      },
      "text_1x3": {
        "name": "Opción 4: Texto Plano 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9",
        "tag": "Texto • 16:9 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku HV4775-001 --layout 1x3",
        "prompt": "Commercial footwear catalog triptych row showing exactly 3 side-by-side photographic views of the sneaker Air Jordan 1 Low \"Inner Beast\", SKU: HV4775-001 on a pure solid white background (#FFFFFF). Panel 1 (left): strict 90-degree lateral side profile pointing LEFT. Panel 2 (center): direct 180-degree rear heel counter view with branding badge. Panel 3 (right): direct 90-degree overhead top-down flat lay view showing laces and tongue. Uniform 5500K dual softbox lighting, razor-sharp details, subtle soft contact shadow on floor, clean commercial photography, no background clutter."
      }
    },
    "negative_prompt": "distorted logos, misspelled text, fake brand badges, asymmetrical deformed sole, warped eyelets, blurry laces, colored background, gradient background, shadows on walls, studio stands, human feet, legs, hands, mannequins, socks, dirty soles, worn leather, scuffs, lowres, oversaturated, chromatic aberration, cartoon, illustration, 3d render plastic sheen"
  },
  {
    "index": 32,
    "sku": "HQ8034-700",
    "name": "Nike LeBron Witness 9",
    "primary_ref": "assets/2-norm-std/HQ8034-700/01-lateral.webp",
    "formats": {
      "json_2x2": {
        "name": "Opción 1: JSON 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "JSON • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku HQ8034-700 --layout 2x2",
        "prompt": "{\n  \"task\": \"commercial_footwear_catalog_quad_sheet\",\n  \"product\": {\n    \"name\": \"Nike LeBron Witness 9\",\n    \"sku\": \"HQ8034-700\",\n    \"authentic\": true\n  },\n  \"layout\": {\n    \"type\": \"2x2_grid_contact_sheet\",\n    \"aspect_ratio\": \"1:1\",\n    \"background_color\": \"#FFFFFF\",\n    \"panels\": {\n      \"top_left\": \"90-degree lateral outer profile, toe pointing LEFT\",\n      \"top_right\": \"45-degree 3/4 perspective front-quarter, facing LEFT\",\n      \"bottom_left\": \"180-degree direct rear heel counter, centered\",\n      \"bottom_right\": \"90-degree overhead top-down flat lay view, laces and tongue\"\n    }\n  },\n  \"lighting\": \"neutral_softbox_5500k_studio\",\n  \"camera\": \"85mm_lens_f8_sharp_focus\",\n  \"output\": \"razor_sharp_focus_pure_white_background_subtle_contact_shadow\"\n}"
      },
      "json_1x3": {
        "name": "Opción 2: JSON 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9 o 4:3",
        "tag": "JSON • 16:9 / 4:3 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku HQ8034-700 --layout 1x3",
        "prompt": "{\n  \"style\": \"professional_sneaker_catalog\",\n  \"shoe\": \"Nike LeBron Witness 9\",\n  \"sku\": \"HQ8034-700\",\n  \"composition\": \"horizontal_triptych_three_equal_panels\",\n  \"aspect_ratio\": \"16:9_or_4:3\",\n  \"background\": \"seamless_solid_pure_white_#FFFFFF\",\n  \"views_left_to_right\": [\n    \"Panel 1: clean lateral outer profile view with toe pointing horizontally LEFT\",\n    \"Panel 2: direct 180-degree rear heel branding badge centered\",\n    \"Panel 3: direct 90-degree overhead top-down view showing laces and tongue\"\n  ],\n  \"render_quality\": \"8k_resolution_sharp_textures_dual_softbox_lighting\"\n}"
      },
      "text_2x2": {
        "name": "Opción 3: Texto Plano 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "Texto • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku HQ8034-700 --layout 2x2",
        "prompt": "Commercial footwear catalog 2x2 grid contact sheet of authentic sneaker Nike LeBron Witness 9, SKU: HQ8034-700. Exactly 4 symmetrical panels on a seamless pure solid white background (#FFFFFF). Top-left panel: strict 90-degree lateral outer profile pointing LEFT. Top-right panel: three-quarter 3/4 perspective front-quarter facing LEFT. Bottom-left panel: direct 180-degree rear heel view centered. Bottom-right panel: direct 90-degree overhead top-down flat lay view. Identical studio softbox lighting at 5500K across all panels, subtle grounded contact shadows, razor-sharp focus across all textures, 85mm lens f/8, 8k resolution e-commerce standard, no human feet, no props."
      },
      "text_1x3": {
        "name": "Opción 4: Texto Plano 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9",
        "tag": "Texto • 16:9 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku HQ8034-700 --layout 1x3",
        "prompt": "Commercial footwear catalog triptych row showing exactly 3 side-by-side photographic views of the sneaker Nike LeBron Witness 9, SKU: HQ8034-700 on a pure solid white background (#FFFFFF). Panel 1 (left): strict 90-degree lateral side profile pointing LEFT. Panel 2 (center): direct 180-degree rear heel counter view with branding badge. Panel 3 (right): direct 90-degree overhead top-down flat lay view showing laces and tongue. Uniform 5500K dual softbox lighting, razor-sharp details, subtle soft contact shadow on floor, clean commercial photography, no background clutter."
      }
    },
    "negative_prompt": "distorted logos, misspelled text, fake brand badges, asymmetrical deformed sole, warped eyelets, blurry laces, colored background, gradient background, shadows on walls, studio stands, human feet, legs, hands, mannequins, socks, dirty soles, worn leather, scuffs, lowres, oversaturated, chromatic aberration, cartoon, illustration, 3d render plastic sheen"
  },
  {
    "index": 33,
    "sku": "IQ0213-685",
    "name": "Nike Air Force 1 Rust Pink / Metallic Red",
    "primary_ref": "assets/2-norm-std/IQ0213-685/01-lateral.webp",
    "formats": {
      "json_2x2": {
        "name": "Opción 1: JSON 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "JSON • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IQ0213-685 --layout 2x2",
        "prompt": "{\n  \"task\": \"commercial_footwear_catalog_quad_sheet\",\n  \"product\": {\n    \"name\": \"Nike Air Force 1 Rust Pink / Metallic Red\",\n    \"sku\": \"IQ0213-685\",\n    \"authentic\": true\n  },\n  \"layout\": {\n    \"type\": \"2x2_grid_contact_sheet\",\n    \"aspect_ratio\": \"1:1\",\n    \"background_color\": \"#FFFFFF\",\n    \"panels\": {\n      \"top_left\": \"90-degree lateral outer profile, toe pointing LEFT\",\n      \"top_right\": \"45-degree 3/4 perspective front-quarter, facing LEFT\",\n      \"bottom_left\": \"180-degree direct rear heel counter, centered\",\n      \"bottom_right\": \"90-degree overhead top-down flat lay view, laces and tongue\"\n    }\n  },\n  \"lighting\": \"neutral_softbox_5500k_studio\",\n  \"camera\": \"85mm_lens_f8_sharp_focus\",\n  \"output\": \"razor_sharp_focus_pure_white_background_subtle_contact_shadow\"\n}"
      },
      "json_1x3": {
        "name": "Opción 2: JSON 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9 o 4:3",
        "tag": "JSON • 16:9 / 4:3 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IQ0213-685 --layout 1x3",
        "prompt": "{\n  \"style\": \"professional_sneaker_catalog\",\n  \"shoe\": \"Nike Air Force 1 Rust Pink / Metallic Red\",\n  \"sku\": \"IQ0213-685\",\n  \"composition\": \"horizontal_triptych_three_equal_panels\",\n  \"aspect_ratio\": \"16:9_or_4:3\",\n  \"background\": \"seamless_solid_pure_white_#FFFFFF\",\n  \"views_left_to_right\": [\n    \"Panel 1: clean lateral outer profile view with toe pointing horizontally LEFT\",\n    \"Panel 2: direct 180-degree rear heel branding badge centered\",\n    \"Panel 3: direct 90-degree overhead top-down view showing laces and tongue\"\n  ],\n  \"render_quality\": \"8k_resolution_sharp_textures_dual_softbox_lighting\"\n}"
      },
      "text_2x2": {
        "name": "Opción 3: Texto Plano 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "Texto • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IQ0213-685 --layout 2x2",
        "prompt": "Commercial footwear catalog 2x2 grid contact sheet of authentic sneaker Nike Air Force 1 Rust Pink / Metallic Red, SKU: IQ0213-685. Exactly 4 symmetrical panels on a seamless pure solid white background (#FFFFFF). Top-left panel: strict 90-degree lateral outer profile pointing LEFT. Top-right panel: three-quarter 3/4 perspective front-quarter facing LEFT. Bottom-left panel: direct 180-degree rear heel view centered. Bottom-right panel: direct 90-degree overhead top-down flat lay view. Identical studio softbox lighting at 5500K across all panels, subtle grounded contact shadows, razor-sharp focus across all textures, 85mm lens f/8, 8k resolution e-commerce standard, no human feet, no props."
      },
      "text_1x3": {
        "name": "Opción 4: Texto Plano 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9",
        "tag": "Texto • 16:9 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IQ0213-685 --layout 1x3",
        "prompt": "Commercial footwear catalog triptych row showing exactly 3 side-by-side photographic views of the sneaker Nike Air Force 1 Rust Pink / Metallic Red, SKU: IQ0213-685 on a pure solid white background (#FFFFFF). Panel 1 (left): strict 90-degree lateral side profile pointing LEFT. Panel 2 (center): direct 180-degree rear heel counter view with branding badge. Panel 3 (right): direct 90-degree overhead top-down flat lay view showing laces and tongue. Uniform 5500K dual softbox lighting, razor-sharp details, subtle soft contact shadow on floor, clean commercial photography, no background clutter."
      }
    },
    "negative_prompt": "distorted logos, misspelled text, fake brand badges, asymmetrical deformed sole, warped eyelets, blurry laces, colored background, gradient background, shadows on walls, studio stands, human feet, legs, hands, mannequins, socks, dirty soles, worn leather, scuffs, lowres, oversaturated, chromatic aberration, cartoon, illustration, 3d render plastic sheen"
  },
  {
    "index": 34,
    "sku": "CW2626-008",
    "name": "Nike Shox R4 College Grey / Volt",
    "primary_ref": "assets/2-norm-std/CW2626-008/01-lateral.webp",
    "formats": {
      "json_2x2": {
        "name": "Opción 1: JSON 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "JSON • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku CW2626-008 --layout 2x2",
        "prompt": "{\n  \"task\": \"commercial_footwear_catalog_quad_sheet\",\n  \"product\": {\n    \"name\": \"Nike Shox R4 College Grey / Volt\",\n    \"sku\": \"CW2626-008\",\n    \"authentic\": true\n  },\n  \"layout\": {\n    \"type\": \"2x2_grid_contact_sheet\",\n    \"aspect_ratio\": \"1:1\",\n    \"background_color\": \"#FFFFFF\",\n    \"panels\": {\n      \"top_left\": \"90-degree lateral outer profile, toe pointing LEFT\",\n      \"top_right\": \"45-degree 3/4 perspective front-quarter, facing LEFT\",\n      \"bottom_left\": \"180-degree direct rear heel counter, centered\",\n      \"bottom_right\": \"90-degree overhead top-down flat lay view, laces and tongue\"\n    }\n  },\n  \"lighting\": \"neutral_softbox_5500k_studio\",\n  \"camera\": \"85mm_lens_f8_sharp_focus\",\n  \"output\": \"razor_sharp_focus_pure_white_background_subtle_contact_shadow\"\n}"
      },
      "json_1x3": {
        "name": "Opción 2: JSON 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9 o 4:3",
        "tag": "JSON • 16:9 / 4:3 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku CW2626-008 --layout 1x3",
        "prompt": "{\n  \"style\": \"professional_sneaker_catalog\",\n  \"shoe\": \"Nike Shox R4 College Grey / Volt\",\n  \"sku\": \"CW2626-008\",\n  \"composition\": \"horizontal_triptych_three_equal_panels\",\n  \"aspect_ratio\": \"16:9_or_4:3\",\n  \"background\": \"seamless_solid_pure_white_#FFFFFF\",\n  \"views_left_to_right\": [\n    \"Panel 1: clean lateral outer profile view with toe pointing horizontally LEFT\",\n    \"Panel 2: direct 180-degree rear heel branding badge centered\",\n    \"Panel 3: direct 90-degree overhead top-down view showing laces and tongue\"\n  ],\n  \"render_quality\": \"8k_resolution_sharp_textures_dual_softbox_lighting\"\n}"
      },
      "text_2x2": {
        "name": "Opción 3: Texto Plano 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "Texto • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku CW2626-008 --layout 2x2",
        "prompt": "Commercial footwear catalog 2x2 grid contact sheet of authentic sneaker Nike Shox R4 College Grey / Volt, SKU: CW2626-008. Exactly 4 symmetrical panels on a seamless pure solid white background (#FFFFFF). Top-left panel: strict 90-degree lateral outer profile pointing LEFT. Top-right panel: three-quarter 3/4 perspective front-quarter facing LEFT. Bottom-left panel: direct 180-degree rear heel view centered. Bottom-right panel: direct 90-degree overhead top-down flat lay view. Identical studio softbox lighting at 5500K across all panels, subtle grounded contact shadows, razor-sharp focus across all textures, 85mm lens f/8, 8k resolution e-commerce standard, no human feet, no props."
      },
      "text_1x3": {
        "name": "Opción 4: Texto Plano 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9",
        "tag": "Texto • 16:9 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku CW2626-008 --layout 1x3",
        "prompt": "Commercial footwear catalog triptych row showing exactly 3 side-by-side photographic views of the sneaker Nike Shox R4 College Grey / Volt, SKU: CW2626-008 on a pure solid white background (#FFFFFF). Panel 1 (left): strict 90-degree lateral side profile pointing LEFT. Panel 2 (center): direct 180-degree rear heel counter view with branding badge. Panel 3 (right): direct 90-degree overhead top-down flat lay view showing laces and tongue. Uniform 5500K dual softbox lighting, razor-sharp details, subtle soft contact shadow on floor, clean commercial photography, no background clutter."
      }
    },
    "negative_prompt": "distorted logos, misspelled text, fake brand badges, asymmetrical deformed sole, warped eyelets, blurry laces, colored background, gradient background, shadows on walls, studio stands, human feet, legs, hands, mannequins, socks, dirty soles, worn leather, scuffs, lowres, oversaturated, chromatic aberration, cartoon, illustration, 3d render plastic sheen"
  },
  {
    "index": 35,
    "sku": "HQ7980-001",
    "name": "Air Jordan 5 Retro \"Halloween\"",
    "primary_ref": "assets/2-norm-std/HQ7980-001/01-lateral.webp",
    "formats": {
      "json_2x2": {
        "name": "Opción 1: JSON 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "JSON • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku HQ7980-001 --layout 2x2",
        "prompt": "{\n  \"task\": \"commercial_footwear_catalog_quad_sheet\",\n  \"product\": {\n    \"name\": \"Air Jordan 5 Retro \\\"Halloween\\\"\",\n    \"sku\": \"HQ7980-001\",\n    \"authentic\": true\n  },\n  \"layout\": {\n    \"type\": \"2x2_grid_contact_sheet\",\n    \"aspect_ratio\": \"1:1\",\n    \"background_color\": \"#FFFFFF\",\n    \"panels\": {\n      \"top_left\": \"90-degree lateral outer profile, toe pointing LEFT\",\n      \"top_right\": \"45-degree 3/4 perspective front-quarter, facing LEFT\",\n      \"bottom_left\": \"180-degree direct rear heel counter, centered\",\n      \"bottom_right\": \"90-degree overhead top-down flat lay view, laces and tongue\"\n    }\n  },\n  \"lighting\": \"neutral_softbox_5500k_studio\",\n  \"camera\": \"85mm_lens_f8_sharp_focus\",\n  \"output\": \"razor_sharp_focus_pure_white_background_subtle_contact_shadow\"\n}"
      },
      "json_1x3": {
        "name": "Opción 2: JSON 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9 o 4:3",
        "tag": "JSON • 16:9 / 4:3 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku HQ7980-001 --layout 1x3",
        "prompt": "{\n  \"style\": \"professional_sneaker_catalog\",\n  \"shoe\": \"Air Jordan 5 Retro \\\"Halloween\\\"\",\n  \"sku\": \"HQ7980-001\",\n  \"composition\": \"horizontal_triptych_three_equal_panels\",\n  \"aspect_ratio\": \"16:9_or_4:3\",\n  \"background\": \"seamless_solid_pure_white_#FFFFFF\",\n  \"views_left_to_right\": [\n    \"Panel 1: clean lateral outer profile view with toe pointing horizontally LEFT\",\n    \"Panel 2: direct 180-degree rear heel branding badge centered\",\n    \"Panel 3: direct 90-degree overhead top-down view showing laces and tongue\"\n  ],\n  \"render_quality\": \"8k_resolution_sharp_textures_dual_softbox_lighting\"\n}"
      },
      "text_2x2": {
        "name": "Opción 3: Texto Plano 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "Texto • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku HQ7980-001 --layout 2x2",
        "prompt": "Commercial footwear catalog 2x2 grid contact sheet of authentic sneaker Air Jordan 5 Retro \"Halloween\", SKU: HQ7980-001. Exactly 4 symmetrical panels on a seamless pure solid white background (#FFFFFF). Top-left panel: strict 90-degree lateral outer profile pointing LEFT. Top-right panel: three-quarter 3/4 perspective front-quarter facing LEFT. Bottom-left panel: direct 180-degree rear heel view centered. Bottom-right panel: direct 90-degree overhead top-down flat lay view. Identical studio softbox lighting at 5500K across all panels, subtle grounded contact shadows, razor-sharp focus across all textures, 85mm lens f/8, 8k resolution e-commerce standard, no human feet, no props."
      },
      "text_1x3": {
        "name": "Opción 4: Texto Plano 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9",
        "tag": "Texto • 16:9 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku HQ7980-001 --layout 1x3",
        "prompt": "Commercial footwear catalog triptych row showing exactly 3 side-by-side photographic views of the sneaker Air Jordan 5 Retro \"Halloween\", SKU: HQ7980-001 on a pure solid white background (#FFFFFF). Panel 1 (left): strict 90-degree lateral side profile pointing LEFT. Panel 2 (center): direct 180-degree rear heel counter view with branding badge. Panel 3 (right): direct 90-degree overhead top-down flat lay view showing laces and tongue. Uniform 5500K dual softbox lighting, razor-sharp details, subtle soft contact shadow on floor, clean commercial photography, no background clutter."
      }
    },
    "negative_prompt": "distorted logos, misspelled text, fake brand badges, asymmetrical deformed sole, warped eyelets, blurry laces, colored background, gradient background, shadows on walls, studio stands, human feet, legs, hands, mannequins, socks, dirty soles, worn leather, scuffs, lowres, oversaturated, chromatic aberration, cartoon, illustration, 3d render plastic sheen"
  },
  {
    "index": 36,
    "sku": "IM4026-100",
    "name": "Air Jordan 4 Retro \"Flight Club\"",
    "primary_ref": "assets/2-norm-std/IM4026-100/01-lateral.webp",
    "formats": {
      "json_2x2": {
        "name": "Opción 1: JSON 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "JSON • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IM4026-100 --layout 2x2",
        "prompt": "{\n  \"task\": \"commercial_footwear_catalog_quad_sheet\",\n  \"product\": {\n    \"name\": \"Air Jordan 4 Retro \\\"Flight Club\\\"\",\n    \"sku\": \"IM4026-100\",\n    \"authentic\": true\n  },\n  \"layout\": {\n    \"type\": \"2x2_grid_contact_sheet\",\n    \"aspect_ratio\": \"1:1\",\n    \"background_color\": \"#FFFFFF\",\n    \"panels\": {\n      \"top_left\": \"90-degree lateral outer profile, toe pointing LEFT\",\n      \"top_right\": \"45-degree 3/4 perspective front-quarter, facing LEFT\",\n      \"bottom_left\": \"180-degree direct rear heel counter, centered\",\n      \"bottom_right\": \"90-degree overhead top-down flat lay view, laces and tongue\"\n    }\n  },\n  \"lighting\": \"neutral_softbox_5500k_studio\",\n  \"camera\": \"85mm_lens_f8_sharp_focus\",\n  \"output\": \"razor_sharp_focus_pure_white_background_subtle_contact_shadow\"\n}"
      },
      "json_1x3": {
        "name": "Opción 2: JSON 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9 o 4:3",
        "tag": "JSON • 16:9 / 4:3 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IM4026-100 --layout 1x3",
        "prompt": "{\n  \"style\": \"professional_sneaker_catalog\",\n  \"shoe\": \"Air Jordan 4 Retro \\\"Flight Club\\\"\",\n  \"sku\": \"IM4026-100\",\n  \"composition\": \"horizontal_triptych_three_equal_panels\",\n  \"aspect_ratio\": \"16:9_or_4:3\",\n  \"background\": \"seamless_solid_pure_white_#FFFFFF\",\n  \"views_left_to_right\": [\n    \"Panel 1: clean lateral outer profile view with toe pointing horizontally LEFT\",\n    \"Panel 2: direct 180-degree rear heel branding badge centered\",\n    \"Panel 3: direct 90-degree overhead top-down view showing laces and tongue\"\n  ],\n  \"render_quality\": \"8k_resolution_sharp_textures_dual_softbox_lighting\"\n}"
      },
      "text_2x2": {
        "name": "Opción 3: Texto Plano 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "Texto • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IM4026-100 --layout 2x2",
        "prompt": "Commercial footwear catalog 2x2 grid contact sheet of authentic sneaker Air Jordan 4 Retro \"Flight Club\", SKU: IM4026-100. Exactly 4 symmetrical panels on a seamless pure solid white background (#FFFFFF). Top-left panel: strict 90-degree lateral outer profile pointing LEFT. Top-right panel: three-quarter 3/4 perspective front-quarter facing LEFT. Bottom-left panel: direct 180-degree rear heel view centered. Bottom-right panel: direct 90-degree overhead top-down flat lay view. Identical studio softbox lighting at 5500K across all panels, subtle grounded contact shadows, razor-sharp focus across all textures, 85mm lens f/8, 8k resolution e-commerce standard, no human feet, no props."
      },
      "text_1x3": {
        "name": "Opción 4: Texto Plano 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9",
        "tag": "Texto • 16:9 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IM4026-100 --layout 1x3",
        "prompt": "Commercial footwear catalog triptych row showing exactly 3 side-by-side photographic views of the sneaker Air Jordan 4 Retro \"Flight Club\", SKU: IM4026-100 on a pure solid white background (#FFFFFF). Panel 1 (left): strict 90-degree lateral side profile pointing LEFT. Panel 2 (center): direct 180-degree rear heel counter view with branding badge. Panel 3 (right): direct 90-degree overhead top-down flat lay view showing laces and tongue. Uniform 5500K dual softbox lighting, razor-sharp details, subtle soft contact shadow on floor, clean commercial photography, no background clutter."
      }
    },
    "negative_prompt": "distorted logos, misspelled text, fake brand badges, asymmetrical deformed sole, warped eyelets, blurry laces, colored background, gradient background, shadows on walls, studio stands, human feet, legs, hands, mannequins, socks, dirty soles, worn leather, scuffs, lowres, oversaturated, chromatic aberration, cartoon, illustration, 3d render plastic sheen"
  },
  {
    "index": 37,
    "sku": "IO2829-600",
    "name": "Air Jordan 4 Retro \"She's A Star\"",
    "primary_ref": "assets/2-norm-std/IO2829-600/01-lateral.webp",
    "formats": {
      "json_2x2": {
        "name": "Opción 1: JSON 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "JSON • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IO2829-600 --layout 2x2",
        "prompt": "{\n  \"task\": \"commercial_footwear_catalog_quad_sheet\",\n  \"product\": {\n    \"name\": \"Air Jordan 4 Retro \\\"She's A Star\\\"\",\n    \"sku\": \"IO2829-600\",\n    \"authentic\": true\n  },\n  \"layout\": {\n    \"type\": \"2x2_grid_contact_sheet\",\n    \"aspect_ratio\": \"1:1\",\n    \"background_color\": \"#FFFFFF\",\n    \"panels\": {\n      \"top_left\": \"90-degree lateral outer profile, toe pointing LEFT\",\n      \"top_right\": \"45-degree 3/4 perspective front-quarter, facing LEFT\",\n      \"bottom_left\": \"180-degree direct rear heel counter, centered\",\n      \"bottom_right\": \"90-degree overhead top-down flat lay view, laces and tongue\"\n    }\n  },\n  \"lighting\": \"neutral_softbox_5500k_studio\",\n  \"camera\": \"85mm_lens_f8_sharp_focus\",\n  \"output\": \"razor_sharp_focus_pure_white_background_subtle_contact_shadow\"\n}"
      },
      "json_1x3": {
        "name": "Opción 2: JSON 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9 o 4:3",
        "tag": "JSON • 16:9 / 4:3 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IO2829-600 --layout 1x3",
        "prompt": "{\n  \"style\": \"professional_sneaker_catalog\",\n  \"shoe\": \"Air Jordan 4 Retro \\\"She's A Star\\\"\",\n  \"sku\": \"IO2829-600\",\n  \"composition\": \"horizontal_triptych_three_equal_panels\",\n  \"aspect_ratio\": \"16:9_or_4:3\",\n  \"background\": \"seamless_solid_pure_white_#FFFFFF\",\n  \"views_left_to_right\": [\n    \"Panel 1: clean lateral outer profile view with toe pointing horizontally LEFT\",\n    \"Panel 2: direct 180-degree rear heel branding badge centered\",\n    \"Panel 3: direct 90-degree overhead top-down view showing laces and tongue\"\n  ],\n  \"render_quality\": \"8k_resolution_sharp_textures_dual_softbox_lighting\"\n}"
      },
      "text_2x2": {
        "name": "Opción 3: Texto Plano 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "Texto • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IO2829-600 --layout 2x2",
        "prompt": "Commercial footwear catalog 2x2 grid contact sheet of authentic sneaker Air Jordan 4 Retro \"She's A Star\", SKU: IO2829-600. Exactly 4 symmetrical panels on a seamless pure solid white background (#FFFFFF). Top-left panel: strict 90-degree lateral outer profile pointing LEFT. Top-right panel: three-quarter 3/4 perspective front-quarter facing LEFT. Bottom-left panel: direct 180-degree rear heel view centered. Bottom-right panel: direct 90-degree overhead top-down flat lay view. Identical studio softbox lighting at 5500K across all panels, subtle grounded contact shadows, razor-sharp focus across all textures, 85mm lens f/8, 8k resolution e-commerce standard, no human feet, no props."
      },
      "text_1x3": {
        "name": "Opción 4: Texto Plano 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9",
        "tag": "Texto • 16:9 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IO2829-600 --layout 1x3",
        "prompt": "Commercial footwear catalog triptych row showing exactly 3 side-by-side photographic views of the sneaker Air Jordan 4 Retro \"She's A Star\", SKU: IO2829-600 on a pure solid white background (#FFFFFF). Panel 1 (left): strict 90-degree lateral side profile pointing LEFT. Panel 2 (center): direct 180-degree rear heel counter view with branding badge. Panel 3 (right): direct 90-degree overhead top-down flat lay view showing laces and tongue. Uniform 5500K dual softbox lighting, razor-sharp details, subtle soft contact shadow on floor, clean commercial photography, no background clutter."
      }
    },
    "negative_prompt": "distorted logos, misspelled text, fake brand badges, asymmetrical deformed sole, warped eyelets, blurry laces, colored background, gradient background, shadows on walls, studio stands, human feet, legs, hands, mannequins, socks, dirty soles, worn leather, scuffs, lowres, oversaturated, chromatic aberration, cartoon, illustration, 3d render plastic sheen"
  },
  {
    "index": 38,
    "sku": "IV6811-001",
    "name": "Air Jordan 1 Mid SE Black / Opti Yellow / Silver",
    "primary_ref": "assets/2-norm-std/IV6811-001/01-lateral.webp",
    "formats": {
      "json_2x2": {
        "name": "Opción 1: JSON 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "JSON • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IV6811-001 --layout 2x2",
        "prompt": "{\n  \"task\": \"commercial_footwear_catalog_quad_sheet\",\n  \"product\": {\n    \"name\": \"Air Jordan 1 Mid SE Black / Opti Yellow / Silver\",\n    \"sku\": \"IV6811-001\",\n    \"authentic\": true\n  },\n  \"layout\": {\n    \"type\": \"2x2_grid_contact_sheet\",\n    \"aspect_ratio\": \"1:1\",\n    \"background_color\": \"#FFFFFF\",\n    \"panels\": {\n      \"top_left\": \"90-degree lateral outer profile, toe pointing LEFT\",\n      \"top_right\": \"45-degree 3/4 perspective front-quarter, facing LEFT\",\n      \"bottom_left\": \"180-degree direct rear heel counter, centered\",\n      \"bottom_right\": \"90-degree overhead top-down flat lay view, laces and tongue\"\n    }\n  },\n  \"lighting\": \"neutral_softbox_5500k_studio\",\n  \"camera\": \"85mm_lens_f8_sharp_focus\",\n  \"output\": \"razor_sharp_focus_pure_white_background_subtle_contact_shadow\"\n}"
      },
      "json_1x3": {
        "name": "Opción 2: JSON 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9 o 4:3",
        "tag": "JSON • 16:9 / 4:3 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IV6811-001 --layout 1x3",
        "prompt": "{\n  \"style\": \"professional_sneaker_catalog\",\n  \"shoe\": \"Air Jordan 1 Mid SE Black / Opti Yellow / Silver\",\n  \"sku\": \"IV6811-001\",\n  \"composition\": \"horizontal_triptych_three_equal_panels\",\n  \"aspect_ratio\": \"16:9_or_4:3\",\n  \"background\": \"seamless_solid_pure_white_#FFFFFF\",\n  \"views_left_to_right\": [\n    \"Panel 1: clean lateral outer profile view with toe pointing horizontally LEFT\",\n    \"Panel 2: direct 180-degree rear heel branding badge centered\",\n    \"Panel 3: direct 90-degree overhead top-down view showing laces and tongue\"\n  ],\n  \"render_quality\": \"8k_resolution_sharp_textures_dual_softbox_lighting\"\n}"
      },
      "text_2x2": {
        "name": "Opción 3: Texto Plano 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "Texto • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IV6811-001 --layout 2x2",
        "prompt": "Commercial footwear catalog 2x2 grid contact sheet of authentic sneaker Air Jordan 1 Mid SE Black / Opti Yellow / Silver, SKU: IV6811-001. Exactly 4 symmetrical panels on a seamless pure solid white background (#FFFFFF). Top-left panel: strict 90-degree lateral outer profile pointing LEFT. Top-right panel: three-quarter 3/4 perspective front-quarter facing LEFT. Bottom-left panel: direct 180-degree rear heel view centered. Bottom-right panel: direct 90-degree overhead top-down flat lay view. Identical studio softbox lighting at 5500K across all panels, subtle grounded contact shadows, razor-sharp focus across all textures, 85mm lens f/8, 8k resolution e-commerce standard, no human feet, no props."
      },
      "text_1x3": {
        "name": "Opción 4: Texto Plano 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9",
        "tag": "Texto • 16:9 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IV6811-001 --layout 1x3",
        "prompt": "Commercial footwear catalog triptych row showing exactly 3 side-by-side photographic views of the sneaker Air Jordan 1 Mid SE Black / Opti Yellow / Silver, SKU: IV6811-001 on a pure solid white background (#FFFFFF). Panel 1 (left): strict 90-degree lateral side profile pointing LEFT. Panel 2 (center): direct 180-degree rear heel counter view with branding badge. Panel 3 (right): direct 90-degree overhead top-down flat lay view showing laces and tongue. Uniform 5500K dual softbox lighting, razor-sharp details, subtle soft contact shadow on floor, clean commercial photography, no background clutter."
      }
    },
    "negative_prompt": "distorted logos, misspelled text, fake brand badges, asymmetrical deformed sole, warped eyelets, blurry laces, colored background, gradient background, shadows on walls, studio stands, human feet, legs, hands, mannequins, socks, dirty soles, worn leather, scuffs, lowres, oversaturated, chromatic aberration, cartoon, illustration, 3d render plastic sheen"
  },
  {
    "index": 39,
    "sku": "IR0519-600",
    "name": "Jordan Son Of Mars Low Rojo Pasión / Neblina Gris / White / Black",
    "primary_ref": "assets/2-norm-std/IR0519-600/01-lateral.webp",
    "formats": {
      "json_2x2": {
        "name": "Opción 1: JSON 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "JSON • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IR0519-600 --layout 2x2",
        "prompt": "{\n  \"task\": \"commercial_footwear_catalog_quad_sheet\",\n  \"product\": {\n    \"name\": \"Jordan Son Of Mars Low Rojo Pasi\\u00f3n / Neblina Gris / White / Black\",\n    \"sku\": \"IR0519-600\",\n    \"authentic\": true\n  },\n  \"layout\": {\n    \"type\": \"2x2_grid_contact_sheet\",\n    \"aspect_ratio\": \"1:1\",\n    \"background_color\": \"#FFFFFF\",\n    \"panels\": {\n      \"top_left\": \"90-degree lateral outer profile, toe pointing LEFT\",\n      \"top_right\": \"45-degree 3/4 perspective front-quarter, facing LEFT\",\n      \"bottom_left\": \"180-degree direct rear heel counter, centered\",\n      \"bottom_right\": \"90-degree overhead top-down flat lay view, laces and tongue\"\n    }\n  },\n  \"lighting\": \"neutral_softbox_5500k_studio\",\n  \"camera\": \"85mm_lens_f8_sharp_focus\",\n  \"output\": \"razor_sharp_focus_pure_white_background_subtle_contact_shadow\"\n}"
      },
      "json_1x3": {
        "name": "Opción 2: JSON 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9 o 4:3",
        "tag": "JSON • 16:9 / 4:3 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IR0519-600 --layout 1x3",
        "prompt": "{\n  \"style\": \"professional_sneaker_catalog\",\n  \"shoe\": \"Jordan Son Of Mars Low Rojo Pasi\\u00f3n / Neblina Gris / White / Black\",\n  \"sku\": \"IR0519-600\",\n  \"composition\": \"horizontal_triptych_three_equal_panels\",\n  \"aspect_ratio\": \"16:9_or_4:3\",\n  \"background\": \"seamless_solid_pure_white_#FFFFFF\",\n  \"views_left_to_right\": [\n    \"Panel 1: clean lateral outer profile view with toe pointing horizontally LEFT\",\n    \"Panel 2: direct 180-degree rear heel branding badge centered\",\n    \"Panel 3: direct 90-degree overhead top-down view showing laces and tongue\"\n  ],\n  \"render_quality\": \"8k_resolution_sharp_textures_dual_softbox_lighting\"\n}"
      },
      "text_2x2": {
        "name": "Opción 3: Texto Plano 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "Texto • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IR0519-600 --layout 2x2",
        "prompt": "Commercial footwear catalog 2x2 grid contact sheet of authentic sneaker Jordan Son Of Mars Low Rojo Pasión / Neblina Gris / White / Black, SKU: IR0519-600. Exactly 4 symmetrical panels on a seamless pure solid white background (#FFFFFF). Top-left panel: strict 90-degree lateral outer profile pointing LEFT. Top-right panel: three-quarter 3/4 perspective front-quarter facing LEFT. Bottom-left panel: direct 180-degree rear heel view centered. Bottom-right panel: direct 90-degree overhead top-down flat lay view. Identical studio softbox lighting at 5500K across all panels, subtle grounded contact shadows, razor-sharp focus across all textures, 85mm lens f/8, 8k resolution e-commerce standard, no human feet, no props."
      },
      "text_1x3": {
        "name": "Opción 4: Texto Plano 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9",
        "tag": "Texto • 16:9 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IR0519-600 --layout 1x3",
        "prompt": "Commercial footwear catalog triptych row showing exactly 3 side-by-side photographic views of the sneaker Jordan Son Of Mars Low Rojo Pasión / Neblina Gris / White / Black, SKU: IR0519-600 on a pure solid white background (#FFFFFF). Panel 1 (left): strict 90-degree lateral side profile pointing LEFT. Panel 2 (center): direct 180-degree rear heel counter view with branding badge. Panel 3 (right): direct 90-degree overhead top-down flat lay view showing laces and tongue. Uniform 5500K dual softbox lighting, razor-sharp details, subtle soft contact shadow on floor, clean commercial photography, no background clutter."
      }
    },
    "negative_prompt": "distorted logos, misspelled text, fake brand badges, asymmetrical deformed sole, warped eyelets, blurry laces, colored background, gradient background, shadows on walls, studio stands, human feet, legs, hands, mannequins, socks, dirty soles, worn leather, scuffs, lowres, oversaturated, chromatic aberration, cartoon, illustration, 3d render plastic sheen"
  },
  {
    "index": 40,
    "sku": "IW6277-001",
    "name": "Air Jordan 1 Retro Low OG \"Banned\"",
    "primary_ref": "assets/2-norm-std/IW6277-001/01-lateral.webp",
    "formats": {
      "json_2x2": {
        "name": "Opción 1: JSON 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "JSON • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IW6277-001 --layout 2x2",
        "prompt": "{\n  \"task\": \"commercial_footwear_catalog_quad_sheet\",\n  \"product\": {\n    \"name\": \"Air Jordan 1 Retro Low OG \\\"Banned\\\"\",\n    \"sku\": \"IW6277-001\",\n    \"authentic\": true\n  },\n  \"layout\": {\n    \"type\": \"2x2_grid_contact_sheet\",\n    \"aspect_ratio\": \"1:1\",\n    \"background_color\": \"#FFFFFF\",\n    \"panels\": {\n      \"top_left\": \"90-degree lateral outer profile, toe pointing LEFT\",\n      \"top_right\": \"45-degree 3/4 perspective front-quarter, facing LEFT\",\n      \"bottom_left\": \"180-degree direct rear heel counter, centered\",\n      \"bottom_right\": \"90-degree overhead top-down flat lay view, laces and tongue\"\n    }\n  },\n  \"lighting\": \"neutral_softbox_5500k_studio\",\n  \"camera\": \"85mm_lens_f8_sharp_focus\",\n  \"output\": \"razor_sharp_focus_pure_white_background_subtle_contact_shadow\"\n}"
      },
      "json_1x3": {
        "name": "Opción 2: JSON 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9 o 4:3",
        "tag": "JSON • 16:9 / 4:3 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IW6277-001 --layout 1x3",
        "prompt": "{\n  \"style\": \"professional_sneaker_catalog\",\n  \"shoe\": \"Air Jordan 1 Retro Low OG \\\"Banned\\\"\",\n  \"sku\": \"IW6277-001\",\n  \"composition\": \"horizontal_triptych_three_equal_panels\",\n  \"aspect_ratio\": \"16:9_or_4:3\",\n  \"background\": \"seamless_solid_pure_white_#FFFFFF\",\n  \"views_left_to_right\": [\n    \"Panel 1: clean lateral outer profile view with toe pointing horizontally LEFT\",\n    \"Panel 2: direct 180-degree rear heel branding badge centered\",\n    \"Panel 3: direct 90-degree overhead top-down view showing laces and tongue\"\n  ],\n  \"render_quality\": \"8k_resolution_sharp_textures_dual_softbox_lighting\"\n}"
      },
      "text_2x2": {
        "name": "Opción 3: Texto Plano 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "Texto • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IW6277-001 --layout 2x2",
        "prompt": "Commercial footwear catalog 2x2 grid contact sheet of authentic sneaker Air Jordan 1 Retro Low OG \"Banned\", SKU: IW6277-001. Exactly 4 symmetrical panels on a seamless pure solid white background (#FFFFFF). Top-left panel: strict 90-degree lateral outer profile pointing LEFT. Top-right panel: three-quarter 3/4 perspective front-quarter facing LEFT. Bottom-left panel: direct 180-degree rear heel view centered. Bottom-right panel: direct 90-degree overhead top-down flat lay view. Identical studio softbox lighting at 5500K across all panels, subtle grounded contact shadows, razor-sharp focus across all textures, 85mm lens f/8, 8k resolution e-commerce standard, no human feet, no props."
      },
      "text_1x3": {
        "name": "Opción 4: Texto Plano 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9",
        "tag": "Texto • 16:9 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IW6277-001 --layout 1x3",
        "prompt": "Commercial footwear catalog triptych row showing exactly 3 side-by-side photographic views of the sneaker Air Jordan 1 Retro Low OG \"Banned\", SKU: IW6277-001 on a pure solid white background (#FFFFFF). Panel 1 (left): strict 90-degree lateral side profile pointing LEFT. Panel 2 (center): direct 180-degree rear heel counter view with branding badge. Panel 3 (right): direct 90-degree overhead top-down flat lay view showing laces and tongue. Uniform 5500K dual softbox lighting, razor-sharp details, subtle soft contact shadow on floor, clean commercial photography, no background clutter."
      }
    },
    "negative_prompt": "distorted logos, misspelled text, fake brand badges, asymmetrical deformed sole, warped eyelets, blurry laces, colored background, gradient background, shadows on walls, studio stands, human feet, legs, hands, mannequins, socks, dirty soles, worn leather, scuffs, lowres, oversaturated, chromatic aberration, cartoon, illustration, 3d render plastic sheen"
  },
  {
    "index": 41,
    "sku": "IR0519-003",
    "name": "Jordan Son Of Mars Low Black / University Red",
    "primary_ref": "assets/2-norm-std/IR0519-003/01-lateral.webp",
    "formats": {
      "json_2x2": {
        "name": "Opción 1: JSON 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "JSON • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IR0519-003 --layout 2x2",
        "prompt": "{\n  \"task\": \"commercial_footwear_catalog_quad_sheet\",\n  \"product\": {\n    \"name\": \"Jordan Son Of Mars Low Black / University Red\",\n    \"sku\": \"IR0519-003\",\n    \"authentic\": true\n  },\n  \"layout\": {\n    \"type\": \"2x2_grid_contact_sheet\",\n    \"aspect_ratio\": \"1:1\",\n    \"background_color\": \"#FFFFFF\",\n    \"panels\": {\n      \"top_left\": \"90-degree lateral outer profile, toe pointing LEFT\",\n      \"top_right\": \"45-degree 3/4 perspective front-quarter, facing LEFT\",\n      \"bottom_left\": \"180-degree direct rear heel counter, centered\",\n      \"bottom_right\": \"90-degree overhead top-down flat lay view, laces and tongue\"\n    }\n  },\n  \"lighting\": \"neutral_softbox_5500k_studio\",\n  \"camera\": \"85mm_lens_f8_sharp_focus\",\n  \"output\": \"razor_sharp_focus_pure_white_background_subtle_contact_shadow\"\n}"
      },
      "json_1x3": {
        "name": "Opción 2: JSON 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9 o 4:3",
        "tag": "JSON • 16:9 / 4:3 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IR0519-003 --layout 1x3",
        "prompt": "{\n  \"style\": \"professional_sneaker_catalog\",\n  \"shoe\": \"Jordan Son Of Mars Low Black / University Red\",\n  \"sku\": \"IR0519-003\",\n  \"composition\": \"horizontal_triptych_three_equal_panels\",\n  \"aspect_ratio\": \"16:9_or_4:3\",\n  \"background\": \"seamless_solid_pure_white_#FFFFFF\",\n  \"views_left_to_right\": [\n    \"Panel 1: clean lateral outer profile view with toe pointing horizontally LEFT\",\n    \"Panel 2: direct 180-degree rear heel branding badge centered\",\n    \"Panel 3: direct 90-degree overhead top-down view showing laces and tongue\"\n  ],\n  \"render_quality\": \"8k_resolution_sharp_textures_dual_softbox_lighting\"\n}"
      },
      "text_2x2": {
        "name": "Opción 3: Texto Plano 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "Texto • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IR0519-003 --layout 2x2",
        "prompt": "Commercial footwear catalog 2x2 grid contact sheet of authentic sneaker Jordan Son Of Mars Low Black / University Red, SKU: IR0519-003. Exactly 4 symmetrical panels on a seamless pure solid white background (#FFFFFF). Top-left panel: strict 90-degree lateral outer profile pointing LEFT. Top-right panel: three-quarter 3/4 perspective front-quarter facing LEFT. Bottom-left panel: direct 180-degree rear heel view centered. Bottom-right panel: direct 90-degree overhead top-down flat lay view. Identical studio softbox lighting at 5500K across all panels, subtle grounded contact shadows, razor-sharp focus across all textures, 85mm lens f/8, 8k resolution e-commerce standard, no human feet, no props."
      },
      "text_1x3": {
        "name": "Opción 4: Texto Plano 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9",
        "tag": "Texto • 16:9 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IR0519-003 --layout 1x3",
        "prompt": "Commercial footwear catalog triptych row showing exactly 3 side-by-side photographic views of the sneaker Jordan Son Of Mars Low Black / University Red, SKU: IR0519-003 on a pure solid white background (#FFFFFF). Panel 1 (left): strict 90-degree lateral side profile pointing LEFT. Panel 2 (center): direct 180-degree rear heel counter view with branding badge. Panel 3 (right): direct 90-degree overhead top-down flat lay view showing laces and tongue. Uniform 5500K dual softbox lighting, razor-sharp details, subtle soft contact shadow on floor, clean commercial photography, no background clutter."
      }
    },
    "negative_prompt": "distorted logos, misspelled text, fake brand badges, asymmetrical deformed sole, warped eyelets, blurry laces, colored background, gradient background, shadows on walls, studio stands, human feet, legs, hands, mannequins, socks, dirty soles, worn leather, scuffs, lowres, oversaturated, chromatic aberration, cartoon, illustration, 3d render plastic sheen"
  },
  {
    "index": 42,
    "sku": "AQ9214-012",
    "name": "Jordan Max Aura Cool Grey / Gym Red / Black / White",
    "primary_ref": "assets/2-norm-std/AQ9214-012/01-lateral.webp",
    "formats": {
      "json_2x2": {
        "name": "Opción 1: JSON 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "JSON • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku AQ9214-012 --layout 2x2",
        "prompt": "{\n  \"task\": \"commercial_footwear_catalog_quad_sheet\",\n  \"product\": {\n    \"name\": \"Jordan Max Aura Cool Grey / Gym Red / Black / White\",\n    \"sku\": \"AQ9214-012\",\n    \"authentic\": true\n  },\n  \"layout\": {\n    \"type\": \"2x2_grid_contact_sheet\",\n    \"aspect_ratio\": \"1:1\",\n    \"background_color\": \"#FFFFFF\",\n    \"panels\": {\n      \"top_left\": \"90-degree lateral outer profile, toe pointing LEFT\",\n      \"top_right\": \"45-degree 3/4 perspective front-quarter, facing LEFT\",\n      \"bottom_left\": \"180-degree direct rear heel counter, centered\",\n      \"bottom_right\": \"90-degree overhead top-down flat lay view, laces and tongue\"\n    }\n  },\n  \"lighting\": \"neutral_softbox_5500k_studio\",\n  \"camera\": \"85mm_lens_f8_sharp_focus\",\n  \"output\": \"razor_sharp_focus_pure_white_background_subtle_contact_shadow\"\n}"
      },
      "json_1x3": {
        "name": "Opción 2: JSON 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9 o 4:3",
        "tag": "JSON • 16:9 / 4:3 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku AQ9214-012 --layout 1x3",
        "prompt": "{\n  \"style\": \"professional_sneaker_catalog\",\n  \"shoe\": \"Jordan Max Aura Cool Grey / Gym Red / Black / White\",\n  \"sku\": \"AQ9214-012\",\n  \"composition\": \"horizontal_triptych_three_equal_panels\",\n  \"aspect_ratio\": \"16:9_or_4:3\",\n  \"background\": \"seamless_solid_pure_white_#FFFFFF\",\n  \"views_left_to_right\": [\n    \"Panel 1: clean lateral outer profile view with toe pointing horizontally LEFT\",\n    \"Panel 2: direct 180-degree rear heel branding badge centered\",\n    \"Panel 3: direct 90-degree overhead top-down view showing laces and tongue\"\n  ],\n  \"render_quality\": \"8k_resolution_sharp_textures_dual_softbox_lighting\"\n}"
      },
      "text_2x2": {
        "name": "Opción 3: Texto Plano 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "Texto • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku AQ9214-012 --layout 2x2",
        "prompt": "Commercial footwear catalog 2x2 grid contact sheet of authentic sneaker Jordan Max Aura Cool Grey / Gym Red / Black / White, SKU: AQ9214-012. Exactly 4 symmetrical panels on a seamless pure solid white background (#FFFFFF). Top-left panel: strict 90-degree lateral outer profile pointing LEFT. Top-right panel: three-quarter 3/4 perspective front-quarter facing LEFT. Bottom-left panel: direct 180-degree rear heel view centered. Bottom-right panel: direct 90-degree overhead top-down flat lay view. Identical studio softbox lighting at 5500K across all panels, subtle grounded contact shadows, razor-sharp focus across all textures, 85mm lens f/8, 8k resolution e-commerce standard, no human feet, no props."
      },
      "text_1x3": {
        "name": "Opción 4: Texto Plano 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9",
        "tag": "Texto • 16:9 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku AQ9214-012 --layout 1x3",
        "prompt": "Commercial footwear catalog triptych row showing exactly 3 side-by-side photographic views of the sneaker Jordan Max Aura Cool Grey / Gym Red / Black / White, SKU: AQ9214-012 on a pure solid white background (#FFFFFF). Panel 1 (left): strict 90-degree lateral side profile pointing LEFT. Panel 2 (center): direct 180-degree rear heel counter view with branding badge. Panel 3 (right): direct 90-degree overhead top-down flat lay view showing laces and tongue. Uniform 5500K dual softbox lighting, razor-sharp details, subtle soft contact shadow on floor, clean commercial photography, no background clutter."
      }
    },
    "negative_prompt": "distorted logos, misspelled text, fake brand badges, asymmetrical deformed sole, warped eyelets, blurry laces, colored background, gradient background, shadows on walls, studio stands, human feet, legs, hands, mannequins, socks, dirty soles, worn leather, scuffs, lowres, oversaturated, chromatic aberration, cartoon, illustration, 3d render plastic sheen"
  },
  {
    "index": 43,
    "sku": "IB6644-001",
    "name": "Nike Air Force 1 '07 Premium \"Flowers\"",
    "primary_ref": "assets/2-norm-std/IB6644-001/01-lateral.webp",
    "formats": {
      "json_2x2": {
        "name": "Opción 1: JSON 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "JSON • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IB6644-001 --layout 2x2",
        "prompt": "{\n  \"task\": \"commercial_footwear_catalog_quad_sheet\",\n  \"product\": {\n    \"name\": \"Nike Air Force 1 '07 Premium \\\"Flowers\\\"\",\n    \"sku\": \"IB6644-001\",\n    \"authentic\": true\n  },\n  \"layout\": {\n    \"type\": \"2x2_grid_contact_sheet\",\n    \"aspect_ratio\": \"1:1\",\n    \"background_color\": \"#FFFFFF\",\n    \"panels\": {\n      \"top_left\": \"90-degree lateral outer profile, toe pointing LEFT\",\n      \"top_right\": \"45-degree 3/4 perspective front-quarter, facing LEFT\",\n      \"bottom_left\": \"180-degree direct rear heel counter, centered\",\n      \"bottom_right\": \"90-degree overhead top-down flat lay view, laces and tongue\"\n    }\n  },\n  \"lighting\": \"neutral_softbox_5500k_studio\",\n  \"camera\": \"85mm_lens_f8_sharp_focus\",\n  \"output\": \"razor_sharp_focus_pure_white_background_subtle_contact_shadow\"\n}"
      },
      "json_1x3": {
        "name": "Opción 2: JSON 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9 o 4:3",
        "tag": "JSON • 16:9 / 4:3 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IB6644-001 --layout 1x3",
        "prompt": "{\n  \"style\": \"professional_sneaker_catalog\",\n  \"shoe\": \"Nike Air Force 1 '07 Premium \\\"Flowers\\\"\",\n  \"sku\": \"IB6644-001\",\n  \"composition\": \"horizontal_triptych_three_equal_panels\",\n  \"aspect_ratio\": \"16:9_or_4:3\",\n  \"background\": \"seamless_solid_pure_white_#FFFFFF\",\n  \"views_left_to_right\": [\n    \"Panel 1: clean lateral outer profile view with toe pointing horizontally LEFT\",\n    \"Panel 2: direct 180-degree rear heel branding badge centered\",\n    \"Panel 3: direct 90-degree overhead top-down view showing laces and tongue\"\n  ],\n  \"render_quality\": \"8k_resolution_sharp_textures_dual_softbox_lighting\"\n}"
      },
      "text_2x2": {
        "name": "Opción 3: Texto Plano 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "Texto • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IB6644-001 --layout 2x2",
        "prompt": "Commercial footwear catalog 2x2 grid contact sheet of authentic sneaker Nike Air Force 1 '07 Premium \"Flowers\", SKU: IB6644-001. Exactly 4 symmetrical panels on a seamless pure solid white background (#FFFFFF). Top-left panel: strict 90-degree lateral outer profile pointing LEFT. Top-right panel: three-quarter 3/4 perspective front-quarter facing LEFT. Bottom-left panel: direct 180-degree rear heel view centered. Bottom-right panel: direct 90-degree overhead top-down flat lay view. Identical studio softbox lighting at 5500K across all panels, subtle grounded contact shadows, razor-sharp focus across all textures, 85mm lens f/8, 8k resolution e-commerce standard, no human feet, no props."
      },
      "text_1x3": {
        "name": "Opción 4: Texto Plano 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9",
        "tag": "Texto • 16:9 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IB6644-001 --layout 1x3",
        "prompt": "Commercial footwear catalog triptych row showing exactly 3 side-by-side photographic views of the sneaker Nike Air Force 1 '07 Premium \"Flowers\", SKU: IB6644-001 on a pure solid white background (#FFFFFF). Panel 1 (left): strict 90-degree lateral side profile pointing LEFT. Panel 2 (center): direct 180-degree rear heel counter view with branding badge. Panel 3 (right): direct 90-degree overhead top-down flat lay view showing laces and tongue. Uniform 5500K dual softbox lighting, razor-sharp details, subtle soft contact shadow on floor, clean commercial photography, no background clutter."
      }
    },
    "negative_prompt": "distorted logos, misspelled text, fake brand badges, asymmetrical deformed sole, warped eyelets, blurry laces, colored background, gradient background, shadows on walls, studio stands, human feet, legs, hands, mannequins, socks, dirty soles, worn leather, scuffs, lowres, oversaturated, chromatic aberration, cartoon, illustration, 3d render plastic sheen"
  },
  {
    "index": 44,
    "sku": "IM6969-451",
    "name": "Nike Air Force 1 Obsidiana / Azul Difuso / Perla Suave / Aluminio",
    "primary_ref": "assets/2-norm-std/IM6969-451/01-lateral.webp",
    "formats": {
      "json_2x2": {
        "name": "Opción 1: JSON 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "JSON • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IM6969-451 --layout 2x2",
        "prompt": "{\n  \"task\": \"commercial_footwear_catalog_quad_sheet\",\n  \"product\": {\n    \"name\": \"Nike Air Force 1 Obsidiana / Azul Difuso / Perla Suave / Aluminio\",\n    \"sku\": \"IM6969-451\",\n    \"authentic\": true\n  },\n  \"layout\": {\n    \"type\": \"2x2_grid_contact_sheet\",\n    \"aspect_ratio\": \"1:1\",\n    \"background_color\": \"#FFFFFF\",\n    \"panels\": {\n      \"top_left\": \"90-degree lateral outer profile, toe pointing LEFT\",\n      \"top_right\": \"45-degree 3/4 perspective front-quarter, facing LEFT\",\n      \"bottom_left\": \"180-degree direct rear heel counter, centered\",\n      \"bottom_right\": \"90-degree overhead top-down flat lay view, laces and tongue\"\n    }\n  },\n  \"lighting\": \"neutral_softbox_5500k_studio\",\n  \"camera\": \"85mm_lens_f8_sharp_focus\",\n  \"output\": \"razor_sharp_focus_pure_white_background_subtle_contact_shadow\"\n}"
      },
      "json_1x3": {
        "name": "Opción 2: JSON 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9 o 4:3",
        "tag": "JSON • 16:9 / 4:3 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IM6969-451 --layout 1x3",
        "prompt": "{\n  \"style\": \"professional_sneaker_catalog\",\n  \"shoe\": \"Nike Air Force 1 Obsidiana / Azul Difuso / Perla Suave / Aluminio\",\n  \"sku\": \"IM6969-451\",\n  \"composition\": \"horizontal_triptych_three_equal_panels\",\n  \"aspect_ratio\": \"16:9_or_4:3\",\n  \"background\": \"seamless_solid_pure_white_#FFFFFF\",\n  \"views_left_to_right\": [\n    \"Panel 1: clean lateral outer profile view with toe pointing horizontally LEFT\",\n    \"Panel 2: direct 180-degree rear heel branding badge centered\",\n    \"Panel 3: direct 90-degree overhead top-down view showing laces and tongue\"\n  ],\n  \"render_quality\": \"8k_resolution_sharp_textures_dual_softbox_lighting\"\n}"
      },
      "text_2x2": {
        "name": "Opción 3: Texto Plano 2×2 (Cuadrícula 4 Ángulos)",
        "ratio": "1:1",
        "tag": "Texto • 1:1 Cuadrado",
        "layout": "2x2",
        "angles_count": 4,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IM6969-451 --layout 2x2",
        "prompt": "Commercial footwear catalog 2x2 grid contact sheet of authentic sneaker Nike Air Force 1 Obsidiana / Azul Difuso / Perla Suave / Aluminio, SKU: IM6969-451. Exactly 4 symmetrical panels on a seamless pure solid white background (#FFFFFF). Top-left panel: strict 90-degree lateral outer profile pointing LEFT. Top-right panel: three-quarter 3/4 perspective front-quarter facing LEFT. Bottom-left panel: direct 180-degree rear heel view centered. Bottom-right panel: direct 90-degree overhead top-down flat lay view. Identical studio softbox lighting at 5500K across all panels, subtle grounded contact shadows, razor-sharp focus across all textures, 85mm lens f/8, 8k resolution e-commerce standard, no human feet, no props."
      },
      "text_1x3": {
        "name": "Opción 4: Texto Plano 1×3 (Tira Horizontal 3 Ángulos)",
        "ratio": "16:9",
        "tag": "Texto • 16:9 Horizontal",
        "layout": "1x3",
        "angles_count": 3,
        "split_cmd": "python scripts/split_grid_angles.py \"imagen_descargada.png\" --sku IM6969-451 --layout 1x3",
        "prompt": "Commercial footwear catalog triptych row showing exactly 3 side-by-side photographic views of the sneaker Nike Air Force 1 Obsidiana / Azul Difuso / Perla Suave / Aluminio, SKU: IM6969-451 on a pure solid white background (#FFFFFF). Panel 1 (left): strict 90-degree lateral side profile pointing LEFT. Panel 2 (center): direct 180-degree rear heel counter view with branding badge. Panel 3 (right): direct 90-degree overhead top-down flat lay view showing laces and tongue. Uniform 5500K dual softbox lighting, razor-sharp details, subtle soft contact shadow on floor, clean commercial photography, no background clutter."
      }
    },
    "negative_prompt": "distorted logos, misspelled text, fake brand badges, asymmetrical deformed sole, warped eyelets, blurry laces, colored background, gradient background, shadows on walls, studio stands, human feet, legs, hands, mannequins, socks, dirty soles, worn leather, scuffs, lowres, oversaturated, chromatic aberration, cartoon, illustration, 3d render plastic sheen"
  }
];
