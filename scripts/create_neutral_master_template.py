import os
from PIL import Image, ImageDraw, ImageFont

def generate_template(out_path="dist/assets/master_grid_template_4x2.png"):
    W, H = 2048, 2048
    img = Image.new('RGB', (W, H), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    cols, rows = 2, 4
    cell_w = W // cols # 1024
    cell_h = H // rows # 512

    # Grid lines: 1px dark-gray #333333
    line_color = (51, 51, 51)
    # Vertical line at x = 1024
    draw.line([(cell_w, 0), (cell_w, H)], fill=line_color, width=1)
    # Horizontal lines
    for r in range(1, rows):
        draw.line([(0, r * cell_h), (W, r * cell_h)], fill=line_color, width=1)
    # Outer border
    draw.rectangle([(0, 0), (W - 1, H - 1)], outline=line_color, width=1)

    # Fonts
    font_bold = "C:/Windows/Fonts/arialbd.ttf" if os.path.exists("C:/Windows/Fonts/arialbd.ttf") else None
    font_reg = "C:/Windows/Fonts/arial.ttf" if os.path.exists("C:/Windows/Fonts/arial.ttf") else None

    title_font = ImageFont.truetype(font_bold, 28) if font_bold else ImageFont.load_default()
    hint_font = ImageFont.truetype(font_bold, 36) if font_bold else ImageFont.load_default()
    sub_font = ImageFont.truetype(font_reg, 20) if font_reg else ImageFont.load_default()

    # Panel definitions: (row, col, label, direction_hint, description)
    panels = [
        (0, 0, '01 | LATERAL', '<- TOE POINTING LEFT', 'Single sneaker exterior profile (90 deg)'),
        (0, 1, '02 | MEDIAL', 'TOE POINTING RIGHT ->', 'Single sneaker interior medial profile (90 deg)'),
        (1, 0, '03 | 3/4 FRONT', '<- TOE POINTING DOWN-LEFT', 'Single sneaker 3/4 front perspective (45 deg)'),
        (1, 1, '04 | 3/4 REAR', 'HEEL LEFT, TOE RIGHT ->', 'Single sneaker 3/4 rear-quarter perspective (135 deg)'),
        (2, 0, '05 | FRONT', 'DIRECT FRONT VIEW [PAIR]', 'Direct eye-level front view (matching pair)'),
        (2, 1, '06 | REAR', 'DIRECT REAR VIEW [PAIR]', 'Direct eye-level heel view (matching pair)'),
        (3, 0, '07 | TOP-DOWN', '^ TOP-DOWN OVERHEAD ^', 'Bird\'s-eye overhead view of pair, toes pointing up'),
        (3, 1, '08 | OUTSOLE', '<- HORIZONTAL OUTSOLE ->', 'Horizontal bottom sole tread pattern')
    ]

    for row, col, label, hint, desc in panels:
        x0 = col * cell_w
        y0 = row * cell_h
        
        # Label in top-left corner
        draw.text((x0 + 40, y0 + 35), label, fill=(40, 40, 40), font=title_font)
        
        # Center hint
        hint_bbox = draw.textbbox((0, 0), hint, font=hint_font)
        hw = hint_bbox[2] - hint_bbox[0]
        hh = hint_bbox[3] - hint_bbox[1]
        cx = x0 + (cell_w - hw) // 2
        cy = y0 + (cell_h - hh) // 2 - 15
        draw.text((cx, cy), hint, fill=(185, 185, 185), font=hint_font)
        
        # Center description below hint
        desc_bbox = draw.textbbox((0, 0), desc, font=sub_font)
        dw = desc_bbox[2] - desc_bbox[0]
        draw.text((x0 + (cell_w - dw) // 2, cy + hh + 16), desc, fill=(205, 205, 205), font=sub_font)

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    img.save(out_path, quality=95)
    print(f"Neutral master template saved to {out_path} ({W}x{H})")

if __name__ == "__main__":
    generate_template()
