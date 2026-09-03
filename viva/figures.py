#!/usr/bin/env python3
"""Generate clean vector-style architecture diagrams for the viva deck.

Each figure is drawn with PIL in the deck's teal + charcoal palette and saved as
a PNG under viva/_figs/.  The deck builder embeds the relevant PNG on the
corresponding methodology slide.

Palette (matches build_colleague_style.py):
    ACCENT  #0E7C7B  primary teal
    DEEP    #0A5F5E  deep teal
    DARK    #22303C  charcoal text
    BODY    #2F3B49  body text
    MINT    #E8F1F0  soft panel
"""
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
FIGDIR = os.path.join(HERE, "_figs")
os.makedirs(FIGDIR, exist_ok=True)

ACCENT = (0x0E, 0x7C, 0x7B)
DEEP   = (0x0A, 0x5F, 0x5E)
DARK   = (0x22, 0x30, 0x3C)
BODY   = (0x2F, 0x3B, 0x49)
MINT   = (0xE8, 0xF1, 0xF0)
MINT2  = (0xD5, 0xE6, 0xE5)
WHITE  = (0xFF, 0xFF, 0xFF)

FONT_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_R = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

def _font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except Exception:
        return ImageFont.load_default()

def _text(draw, xy, text, fill=DARK, font=None, anchor="mm"):
    draw.text(xy, text, fill=fill, font=font or _font(FONT_R, 16), anchor=anchor)

def rounded_box(draw, box, fill, outline=None, radius=14, width=2):
    draw.rounded_rectangle(box, radius=radius, fill=fill,
                           outline=outline, width=width)

def arrow(draw, x1, y1, x2, y2, color=ACCENT, width=4, head=12):
    draw.line([(x1, y1), (x2, y2)], fill=color, width=width)
    import math
    ang = math.atan2(y2 - y1, x2 - x1)
    for da in (math.radians(150), math.radians(210)):
        hx = x2 + head * math.cos(ang + da)
        hy = y2 + head * math.sin(ang + da)
        draw.line([(x2, y2), (hx, hy)], fill=color, width=width)


# ---------------------------------------------------------------------------
# Figure 1 -- C1 pipeline: PCA -> KMeans++ -> LightGBM surrogate -> TreeSHAP
# ---------------------------------------------------------------------------
def fig_c1(out="c1_pipeline.png"):
    W, H = 1600, 450
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    steps = [
        ("1. Standardise", "original features", ACCENT),
        ("2. PCA", "diagnostic", ACCENT),
        ("3. K-Means++", "labels (k*)", ACCENT),
        ("4. LightGBM", "surrogate", DEEP),
        ("5. TreeSHAP", "attribution", ACCENT),
        ("6. Aggregate", "global / cluster / local", DARK),
    ]
    n = len(steps)
    margin = 24
    boxw = (W - 2 * margin - (n - 1) * 34) / n
    boxh = 150
    cy = H / 2 - 10
    for i, (title, sub, color) in enumerate(steps):
        x = margin + i * (boxw + 34)
        box = (x, cy - boxh / 2, x + boxw, cy + boxh / 2)
        rounded_box(d, box, color, radius=16)
        _text(d, (x + boxw / 2, cy - 28), title, fill=WHITE, font=_font(FONT_B, 18))
        _text(d, (x + boxw / 2, cy + 12), sub, fill=(0xE8, 0xF1, 0xF0), font=_font(FONT_R, 14))
        if i < n - 1:
            arrow(d, x + boxw + 2, cy, x + boxw + 32, cy)
    # label under the pipeline: high-fidelity surrogate (macro-F1 ~0.82)
    rounded_box(d, (W / 2 - 300, H - 60, W / 2 + 300, H - 20), MINT, outline=ACCENT, radius=12, width=2)
    _text(d, (W / 2, H - 40), "Validity condition: surrogate fidelity high (macro-F1 \u2248 0.82)",
          fill=BODY, font=_font(FONT_R, 16))
    img.save(os.path.join(FIGDIR, out))
    return os.path.join(FIGDIR, out)


# ---------------------------------------------------------------------------
# Figure 2 -- C2 multi-level hierarchy with cross-level SHAP aggregation
# ---------------------------------------------------------------------------
def fig_c2(out="c2_hierarchy.png"):
    W, H = 1600, 450
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    # level 1 root (centred, wide enough)
    rootw = 420
    root = (W / 2 - rootw / 2, 36, W / 2 + rootw / 2, 118)
    rounded_box(d, root, DEEP, radius=16)
    _text(d, (W / 2, 77), "Level 1 \u00b7 Coarse clustering (k=3)", fill=WHITE, font=_font(FONT_B, 20))
    # three level-2 children evenly spaced across the full width
    cy1 = 190
    children = [
        ("Regime A", "temp, dew point, ozone"),
        ("Regime B", "CO, SO2, PM, wind"),
        ("Regime C", "clean air, meteorology"),
    ]
    cw = 330; ch = 110
    margin = 40
    gap = (W - 2 * margin - 3 * cw) / 2
    xs = [margin + i * (cw + gap) for i in range(3)]
    for (name, sub), x in zip(children, xs):
        box = (x, cy1, x + cw, cy1 + ch)
        rounded_box(d, box, ACCENT, radius=16)
        _text(d, (x + cw / 2, cy1 + 34), name, fill=WHITE, font=_font(FONT_B, 18))
        _text(d, (x + cw / 2, cy1 + 70), sub, fill=(0xE8, 0xF1, 0xF0), font=_font(FONT_R, 14))
        arrow(d, W / 2, 118, x + cw / 2, cy1)
    # level 3 -- Regime A expanded into nested sub-groups
    cy2 = 350
    leaf_w = cw - 60
    leaf = (xs[0] + 30, cy2, xs[0] + 30 + leaf_w, cy2 + 74)
    rounded_box(d, leaf, MINT, outline=ACCENT, radius=14, width=3)
    _text(d, (leaf[0] + leaf_w / 2, cy2 + 37), "nested sub-group (level 3)", fill=DARK, font=_font(FONT_R, 15))
    arrow(d, xs[0] + cw / 2, cy1 + ch, leaf[0] + leaf_w / 2, cy2)
    # Prop 6.1 note placed to the right, below the children, not overlapping
    note = (W - margin - 300, cy2 - 10, W - margin, cy2 + 74)
    rounded_box(d, note, MINT, outline=DEEP, radius=14, width=3)
    _text(d, (note[0] + 150, note[1] + 26), "Prop. 6.1 cross-level", fill=DARK, font=_font(FONT_B, 15))
    _text(d, (note[0] + 150, note[1] + 55), "\u03a6^(l,c) = \u03a3 w_c'\u00b7\u03a6^(l+1,c') + \u03b5", fill=DEEP, font=_font(FONT_R, 14))
    img.save(os.path.join(FIGDIR, out))
    return os.path.join(FIGDIR, out)


# ---------------------------------------------------------------------------
# Figure 3 -- C3 DyHuCoG hypergraph architecture
# ---------------------------------------------------------------------------
def fig_c3(out="c3_dyhucog.png"):
    W, H = 1600, 450
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    # left block: inputs / players
    left = (30, 90, 300, 380)
    rounded_box(d, left, MINT, outline=ACCENT, radius=18, width=4)
    _text(d, (165, 130), "Players", fill=DARK, font=_font(FONT_B, 20))
    _text(d, (165, 180), "U \u222a I \u222a C", fill=ACCENT, font=_font(FONT_B, 24))
    _text(d, (165, 250), "users \u00b7 items \u00b7 contexts", fill=BODY, font=_font(FONT_R, 14))
    _text(d, (165, 300), "hypergraph H=(V,E,W)", fill=BODY, font=_font(FONT_R, 14))
    # middle block: coalition value + Shapley
    mid = (360, 60, 640, 410)
    rounded_box(d, mid, ACCENT, radius=18)
    _text(d, (500, 120), "Coalition value", fill=WHITE, font=_font(FONT_B, 20))
    _text(d, (500, 165), "v(S) = \u03b1\u00b7NDCG@20", fill=(0xE8,0xF1,0xF0), font=_font(FONT_R, 17))
    _text(d, (500, 200), "+ \u03b2\u00b7Diversity + \u03b3\u00b7Ctx", fill=(0xE8,0xF1,0xF0), font=_font(FONT_R, 17))
    _text(d, (500, 250), "\u03c6\u0302_j = (1/M)\u03a3 \u0394v", fill=WHITE, font=_font(FONT_B, 20))
    _text(d, (500, 290), "Monte Carlo Shapley (M=50)", fill=(0xE8,0xF1,0xF0), font=_font(FONT_R, 14))
    _text(d, (500, 330), "normalised weights w_jk", fill=(0xE8,0xF1,0xF0), font=_font(FONT_R, 14))
    # right block: message passing output
    right = (700, 90, 1170, 380)
    rounded_box(d, right, DEEP, radius=18)
    _text(d, (935, 130), "Shapley-weighted message passing", fill=WHITE, font=_font(FONT_B, 18))
    # nodes graph
    nodes = [(760, 220), (880, 180), (1000, 220), (880, 300), (1030, 300), (760, 320)]
    for nx, ny in nodes:
        d.ellipse([nx - 22, ny - 22, nx + 22, ny + 22], fill=WHITE, outline=ACCENT, width=4)
    edges = [(0,1),(1,2),(1,3),(2,4),(3,5),(0,5)]
    for a, b in edges:
        d.line([nodes[a], nodes[b]], fill=(0xE8,0xF1,0xF0), width=3)
    _text(d, (935, 360), "e^(l+1) = \u03c3(W e^(l) + \u03a3 w_jk e_k)", fill=WHITE, font=_font(FONT_R, 15))
    # arrows
    arrow(d, 300, 235, 360, 235)
    arrow(d, 640, 235, 700, 235)
    img.save(os.path.join(FIGDIR, out))
    return os.path.join(FIGDIR, out)


if __name__ == "__main__":
    print(fig_c1())
    print(fig_c2())
    print(fig_c3())
