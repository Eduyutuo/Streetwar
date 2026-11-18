# RITMO / Lil David — Catálogo Digital Streetwear

> **Catálogo digital de moda urbana y calzado exclusivo** (Jordan Retro, Nike Air Force 1, Air Max, Dunk, colaboraciones y performance). Desarrollado con una arquitectura moderna, diseño limpio y minimalista, optimizado para consulta rápida, visualización de alta fidelidad y cierre de ventas directo vía WhatsApp (con soporte binacional EE.UU. / Perú).

---

## 1. Identidad de Marca y Recursos Visuales

### 1.1 Logotipo Oficial y Variantes
Los activos vectoriales y de alta resolución se ubican en [`dist/assets/`](file:///c:/Users/eduar/Documents/CATALOGO/dist/assets):
- **Logo Vectorial Principal:** [`dist/assets/LOGO.svg`](file:///c:/Users/eduar/Documents/CATALOGO/dist/assets/LOGO.svg) (Escalable, uso en cabecera y footer).
- **Logo Bitmap:** [`dist/assets/LOGO.png`](file:///c:/Users/eduar/Documents/CATALOGO/dist/assets/LOGO.png) (Versión rasterizada de alta densidad).
- **Aplicación:** Sobre fondo claro (`#FFFFFF` o `#F4F1EA`) en color Ink (`#111111`), o sobre modo oscuro en blanco puro con contraste máximo.

---

### 1.2 Paleta Cromática Oficial

El diseño sigue una línea **Minimalista / Editorial** limpia con acentos contemporáneos:

| Muestra | Nombre | HEX | Rol en la Interfaz | Aplicación |
| :---: | :--- | :--- | :--- | :--- |
| ![#111111](https://via.placeholder.com/15/111111/000000?text=+) | **Ink** | `#111111` | Primario | Textos principales, cabeceras, botones sólidos y bordes de contraste. |
| ![#FFFFFF](https://via.placeholder.com/15/FFFFFF/000000?text=+) | **Pure White** | `#FFFFFF` | Fondo de Producto | Fondo obligatorio para todas las imágenes de zapatillas en estudio. |
| ![#F4F1EA](https://via.placeholder.com/15/F4F1EA/000000?text=+) | **Paper Editorial** | `#F4F1EA` | Fondo Secundario | Fondos de secciones, banners informativos y módulos destacados. |
| ![#C7FF16](https://via.placeholder.com/15/C7FF16/000000?text=+) | **Lime Volt** | `#C7FF16` | Acento Energético | Badges de ofertas, estados de stock y llamadas de acción (*kicker*). |
| ![#0757E8](https://via.placeholder.com/15/0757E8/000000?text=+) | **Electric Blue** | `#0757E8` | Acento Interactivo | Enlaces activos, categorías seleccionadas y microinteracciones. |
| ![#FF5B2B](https://via.placeholder.com/15/FF5B2B/000000?text=+) | **Street Orange** | `#FF5B2B` | Alertas / Drops | Indicadores de lanzamientos, drops exclusivos y stock limitado. |
| ![#CBC8C0](https://via.placeholder.com/15/CBC8C0/000000?text=+) | **Line / Grid** | `#CBC8C0` | Líneas de División | Grillas modulares de catálogo (1px solid editorial). |

---

### 1.3 Tipografía y Jerarquía Visual

- **Familia Primaria:** `Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif`
  - **Titulares (`H1`, `H2`):** `font-weight: 800` o `900` (Black/Heavy), en mayúsculas sostenidas (`uppercase`), interletreado ligeramente compacto (`letter-spacing: -0.02em` a `0.04em`).
  - **Subtítulos y Kickers:** Mayúsculas, tamaño reducido (11–13px), espaciado abierto (`letter-spacing: 0.1em`).
  - **Precios y Datos Técnicos:** `font-weight: 600` / `700`, números claros y destacados.

---

## 2. Canales de Venta y Atención por WhatsApp

El catálogo cuenta con integración directa para atención y cierre de pedidos en dos regiones clave:

| Región | Número de Contacto | Enlace Directo | Función |
| :--- | :--- | :--- | :--- |
| **Estados Unidos (EE.UU.)** | `+1 (301) 793-3122` | [WhatsApp USA](https://wa.me/13017933122) | Gestión de pedidos internacionales / drops directos |
| **Perú (PE)** | `+51 940 640 679` | [WhatsApp Perú](https://wa.me/51940640679) | Ventas locales, disponibilidad inmediata y envíos nacionales |

> **Plantilla de mensaje prellenado:**
> *"Hola Lil David / RITMO, me interesa el modelo [NOMBRE DEL PRODUCTO] (SKU: [CÓDIGO]) en talla [TALLA], precio [PRECIO]. ¿Tienen disponibilidad y opciones de entrega?"*

---

## 3. Estándar de Ficha de Producto (Data Obligatoria)

Basado en el inventario maestro oficial [`_source_data/inventory/SNKRS (1).xlsx`](file:///c:/Users/eduar/Documents/CATALOGO/_source_data/inventory/SNKRS%20(1).xlsx), cada modelo exhibido en el catálogo debe contener los siguientes campos obligatorios:

1. **Nombre / Modelo Oficial:** Silueta y nombre de colorway exacto (ej. *Air Jordan 9 Retro OG "Space Jam"*).
2. **Categoría / Silueta:** Clasificación de línea (ej. *Jordan Retro 9*, *Air Jordan 1 Low*, *Nike Air Force 1*).
3. **SKU / Código Original de Fabricante:** Código exacto de estilo/color de Nike/Jordan (ej. `IX6180-100`, `IO2076-100`, `AQ9214-006`).
4. **Tallas Disponibles:**
   - Curva Hombre / General (ej. `39-40-41-42` o `40-41-42`).
   - Curva Mujer / GS (ej. `36-37-38`).
5. **Precio:** En moneda local / Soles (ej. `S/ 1,200`, `S/ 790`).
6. **Público / Género:** Clasificación de audiencia (`Hombre`, `Mujer`, `Unisex`).
7. **Estado del Producto:** `Nuevo en caja original (DS - Deadstock)` / 100% Auténtico.
8. **Opciones de Entrega y Envío:**
   - Envíos a todo el Perú (Olva Courier / Shalom / Entrega coordinada).
   - Envíos o importación directa desde EE.UU.

---

## 4. Estándar Fotográfico de Estudio para Catálogo

Todas las fotografías en `dist/assets/galleries/` y `dist/assets/products/` cumplen la norma técnica de catálogo internacional:
1. **Fondo de Estudio:** Blanco puro `#FFFFFF` (RGB: 255, 255, 255) sin sombras de fondo ni viñetas.
2. **Sombra de Contacto:** Oclusión ambiental y sombra natural difusa proyectada directamente bajo la suela.
3. **Fidelidad Absoluta:** Silueta original intacta (materiales, texturas de cuero, logos Jumpman/Swoosh, costuras y cordones sin recortes agresivos).
4. **Formato:** Optimizado para la web con orientación EXIF corregida.

---

## 5. Referencias Visuales y Benchmarks de la Industria

- **[SNKRS / Nike Launch](https://www.nike.com/launch):** Minimalismo extremo, protagonismo absoluto de la zapatilla, ficha técnica con SKU y narrativa de drop.
- **[KITH](https://kith.com):** Estética editorial sobria, grillas refinadas y tipografía contemporánea.
- **[END. Clothing](https://www.endclothing.com):** Sistema de filtros eficiente por talla, marca y modelo con bordes sutiles.
- **[GOAT / StockX](https://stockx.com):** Transparencia en SKU, estado nuevo en caja y verificación de autenticidad.

---

## 6. Arquitectura de Archivos del Proyecto

```text
CATALOGO/
├── dist/                          # WEB EN PRODUCCIÓN (Desplegada en GitHub Pages)
│   ├── assets/
│   │   ├── LOGO.svg / LOGO.png    # Identidad visual oficial
│   │   ├── galleries/             # Fotos de alta fidelidad procesadas (Grupos A a G)
│   │   └── products/              # Imágenes de catálogo
│   ├── catalog.css / styles.css   # Hojas de estilo modulares
│   ├── products.js                # Base de datos del catálogo (mapeada con el Excel oficial)
│   └── *.html                     # Páginas (novedades, hombre, mujer, ofertas, producto)
│
├── _source_data/                  # ARCHIVOS DE TRABAJO Y RESPALDO (Ignorados por Git)
│   ├── inventory/
│   │   └── SNKRS (1).xlsx         # Inventario maestro con modelos, SKUs, tallas y precios
│   ├── raw_photos_BC/             # Fotografías originales de cámara sin editar
│   ├── raw_photos_DE/
│   ├── raw_photos_FG/
│   └── tools/                     # Scripts de utilidad
│
├── .github/workflows/pages.yml    # Pipeline de despliegue automatizado a GitHub Pages
└── README.md                      # Manual de marca, especificaciones y documentación
```
