#!/usr/bin/env python3
"""Regenerate og-image.png — the 1200x630 social share card for epochdigital.ai.

Run from the repo root:  python3 tools/generate-og-image.py
Requires Pillow. Not deployed (see .vercelignore).
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "og-image.png"

W, H = 1200, 630
BG = (5, 5, 5)
BLUE = (59, 130, 246)
ORANGE = (249, 115, 22)

FONT_DIR = Path("/System/Library/Fonts")
NEUE = FONT_DIR / "HelveticaNeue.ttc"
MONO = FONT_DIR / "Menlo.ttc"


def font(path, size, index=0):
    return ImageFont.truetype(str(path), size, index=index)


# HelveticaNeue.ttc face indices: 0 regular, 2 bold-ish, 3 light, 4 medium.
f_head = font(NEUE, 68, index=4)
f_sub = font(NEUE, 27, index=0)
f_mark = font(NEUE, 22, index=4)
f_mono = font(MONO, 19)
f_chip = font(NEUE, 19, index=0)


def radial_glow(size, center, radius, color, peak):
    """A soft circular glow, drawn small and upscaled so it stays smooth."""
    scale = 8
    w, h = size[0] // scale, size[1] // scale
    layer = Image.new("L", (w, h), 0)
    d = ImageDraw.Draw(layer)
    cx, cy, r = center[0] / scale, center[1] / scale, radius / scale
    steps = 48
    for i in range(steps, 0, -1):
        t = i / steps
        rr = r * t
        d.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], fill=int(peak * (1 - t) ** 2))
    layer = layer.resize(size, Image.LANCZOS).filter(ImageFilter.GaussianBlur(24))
    tint = Image.new("RGB", size, color)
    return tint, layer


img = Image.new("RGB", (W, H), BG)

# Ambient brand lighting: cool glow behind the headline, warm accent bottom-right.
for center, radius, color, peak in (
    ((250, 120), 900, BLUE, 62),
    ((1180, 700), 700, ORANGE, 34),
    ((900, 60), 520, BLUE, 26),
):
    tint, mask = radial_glow((W, H), center, radius, color, peak)
    img = Image.composite(Image.blend(img, tint, 1.0), img, mask.point(lambda v: v))
    img = Image.composite(tint, img, mask)

# Faint grid, so the card reads as "systems" rather than a plain gradient.
grid = Image.new("RGBA", (W, H), (0, 0, 0, 0))
gd = ImageDraw.Draw(grid)
for x in range(0, W, 60):
    gd.line([(x, 0), (x, H)], fill=(255, 255, 255, 8))
for y in range(0, H, 60):
    gd.line([(0, y), (W, y)], fill=(255, 255, 255, 8))
img = Image.alpha_composite(img.convert("RGBA"), grid).convert("RGB")

draw = ImageDraw.Draw(img)

MARGIN = 80

# Logo + wordmark
logo = Image.open(ROOT / "epoch_logo_blue.png").convert("RGBA")
logo = logo.crop(logo.getchannel("A").getbbox())
lh = 52
logo = logo.resize((round(logo.width * lh / logo.height), lh), Image.LANCZOS)
img.paste(logo, (MARGIN, 74), logo)


def tracked(d, xy, text, fnt, fill, tracking=0):
    x, y = xy
    for ch in text:
        d.text((x, y), ch, font=fnt, fill=fill)
        x += d.textlength(ch, font=fnt) + tracking
    return x


tracked(
    draw,
    (MARGIN + logo.width + 18, 74 + (lh - 26) // 2),
    "EPOCH DIGITAL",
    f_mark,
    (255, 255, 255),
    tracking=1.6,
)

# Headline
y = 214
for line in ("AI Systems That", "Replace Bottlenecks."):
    draw.text((MARGIN, y), line, font=f_head, fill=(255, 255, 255))
    y += 84

# Subhead
draw.text(
    (MARGIN, y + 22),
    "Applied AI automation for small businesses — so leads get answered,",
    font=f_sub,
    fill=(255, 255, 255, 0) if False else (168, 172, 178),
)
draw.text(
    (MARGIN, y + 60),
    "appointments get booked, and follow-ups happen automatically.",
    font=f_sub,
    fill=(168, 172, 178),
)

# Capability chips
chip_y = H - 128
chip_x = MARGIN
for label in ("AI Receptionist", "Voice Agent", "Booking", "Follow-Up"):
    tw = draw.textlength(label, font=f_chip)
    pad_x, pad_h = 18, 40
    draw.rounded_rectangle(
        [chip_x, chip_y, chip_x + tw + pad_x * 2, chip_y + pad_h],
        radius=20,
        fill=(18, 18, 20),
        outline=(46, 48, 54),
        width=1,
    )
    draw.text((chip_x + pad_x, chip_y + 11), label, font=f_chip, fill=(196, 200, 208))
    chip_x += tw + pad_x * 2 + 12

# Footer rule + domain
draw.line([(MARGIN, H - 58), (W - MARGIN, H - 58)], fill=(36, 38, 42), width=1)
draw.line([(MARGIN, H - 58), (MARGIN + 96, H - 58)], fill=BLUE, width=2)
draw.text((MARGIN, H - 42), "epochdigital.ai", font=f_mono, fill=(150, 154, 162))

right = "15-MIN SYSTEM AUDIT"
draw.text(
    (W - MARGIN - draw.textlength(right, font=f_mono), H - 42),
    right,
    font=f_mono,
    fill=(110, 114, 122),
)

img.save(OUT, "PNG", optimize=True)
print(f"wrote {OUT} ({OUT.stat().st_size / 1024:.0f} KB) {img.size}")
