"""Slide 12 (Graph-Based and Hypergraph Recommenders) figure, v37 paper style.

Drawn the way the recommender-systems literature draws these objects (cf. the
LightGCN and HCCF figures, and the hypergraph surveys that pair a hypergraph
with its incidence matrix H):

  (a) Pairwise graph G = (U u I, E): the bipartite user-item graph, observed
      interactions as thin grey edges, the 2-hop message u2 -> i2 -> u1 as a
      bold black directed path, and the symmetric-normalisation propagation
      rule of LightGCN / HCCF / HPCF set in mathematical type;
  (b) Hypergraph H = (V, E): the same nodes plus a context node, hyperedges
      drawn as dashed closed contours with translucent fills, and the
      incidence matrix H (nodes x hyperedges) beside them; hyperedge weights
      w(e, t) are re-learned at every step (DyHuCoG).

Typography: DejaVu Serif for mathematics (variables italic by shear), every
glyph at or above 16 pt at slide scale for the equation (68 px at 300 dpi) and
at or above 14 pt for labels (60 px).  Run:
    python3 fig_slide12.py <deck.pptx> <out.png>
"""
import math
import sys

from PIL import Image, ImageDraw, ImageFont

W, H = 2625, 1464  # 8.75 x 4.88 in at 300 dpi
DJ = "/usr/share/fonts/truetype/dejavu/"

WHITE = (255, 255, 255)
INK = (40, 40, 40)
GREY = (150, 150, 150)
DARK = (70, 70, 70)
USERF = (189, 215, 238)
ITEMF = (244, 197, 142)
IDLEF = (224, 224, 224)
CTXF = (178, 214, 209)
TEAL = (23, 118, 107)
NAVY = (31, 56, 100)

USERS = ["u1", "u2", "u3"]
ITEMS = ["i1", "i2", "i3"]
EDGES = [("u1", "i1"), ("u1", "i2"), ("u2", "i2"), ("u2", "i3"), ("u3", "i3")]
PATH = [("u2", "i2"), ("i2", "u1")]
E1 = ["u1", "u2", "i2", "c1"]
E2 = ["u2", "u3", "i3"]
HCOLS = ["e1", "e2"]
HROWS = ["u1", "u2", "u3", "i1", "i2", "i3", "c1"]


def check():
    for a, b in EDGES:
        assert (a in USERS) != (b in USERS)
    for a, b in PATH:
        assert (a, b) in EDGES or (b, a) in EDGES
    assert PATH[0][1] == PATH[1][0] == "i2"
    inc = {"e1": E1, "e2": E2}
    for r in HROWS:
        for c in HCOLS:
            assert (r in inc[c]) in (True, False)
    assert "c1" in E1 and len(E1) == 4 and len(E2) == 3


class Typer:
    """Serif math typesetter with true sub/superscript baselines."""

    def __init__(self):
        self.reg = lambda px: ImageFont.truetype(DJ + "DejaVuSerif.ttf", px)
        self.bold = lambda px: ImageFont.truetype(DJ + "DejaVuSerif-Bold.ttf", px)
        self.sans = lambda px: ImageFont.truetype(DJ + "DejaVuSans.ttf", px)

    def itext_img(self, text, px, fill, italic=True, bold=False):
        f = self.bold(px) if bold else self.reg(px)
        pad = px
        w = int(f.getlength(text)) + 2 * pad
        h = int(px * 1.6)
        tmp = Image.new("RGBA", (w, h), (0, 0, 0, 0))
        ImageDraw.Draw(tmp).text((pad, px * 0.25), text, font=f, fill=fill + (255,))
        if italic:
            k = 0.22
            nw = w + int(k * h)
            tmp = tmp.transform((nw, h), Image.AFFINE, (1, k, -k * h, 0, 1, 0),
                                resample=Image.BICUBIC)
        return tmp

    def place(self, img, xy, text, px, fill, italic=True, bold=False, anchor="la"):
        t = self.itext_img(text, px, fill, italic, bold)
        x, y = xy
        if anchor in ("ma", "mm"):
            x -= t.width // 2
        if anchor in ("mm",):
            y -= t.height // 2
        if anchor == "la":
            y -= int(px * 0.25)
        img.paste(t, (int(x), int(y)), t)
        f = self.bold(px) if bold else self.reg(px)
        return int(f.getlength(text))  # true ink advance


def main(deck, out_png):
    check()
    T = Typer()
    img = Image.new("RGB", (W, H), WHITE)
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    d = ImageDraw.Draw(img)

    def node(xy, label, kind, r=58):
        x, y = xy
        if kind == "ctx":
            d.polygon([(x, y - r - 8), (x + r + 8, y), (x, y + r + 8), (x - r - 8, y)],
                      fill=CTXF, outline=TEAL, width=3)
        else:
            fill = USERF if kind == "u" else (ITEMF if kind == "i" else IDLEF)
            d.ellipse([x - r, y - r, x + r, y + r], fill=fill, outline=DARK, width=3)
        T.place(img, (x, y), label, 62, INK, italic=True, bold=True, anchor="mm")

    def arrow(x0, y0, x1, y1, fill, wdt, head=30):
        d.line([(x0, y0), (x1, y1)], fill=fill, width=wdt)
        a = math.atan2(y1 - y0, x1 - x0)
        pts = [(x1, y1)]
        for s in (-1, 1):
            b = a + math.pi + s * 0.38
            pts.append((x1 + head * math.cos(b), y1 + head * math.sin(b)))
        d.polygon(pts, fill=fill)

    def dash_poly(pts, fill, wdt, dash=30, gap=20):
        ring = pts + [pts[0]]
        for (ax, ay), (bx, by) in zip(ring, ring[1:]):
            L = math.hypot(bx - ax, by - ay)
            n = int(L // (dash + gap)) + 1
            ux, uy = (bx - ax) / L, (by - ay) / L
            for i in range(n):
                s0 = i * (dash + gap)
                s1 = min(s0 + dash, L)
                d.line([(ax + ux * s0, ay + uy * s0), (ax + ux * s1, ay + uy * s1)],
                       fill=fill, width=wdt)

    def hull(pts, grow):
        cx = sum(p[0] for p in pts) / len(pts)
        cy = sum(p[1] for p in pts) / len(pts)
        out = []
        for (x, y) in pts:
            a = math.atan2(y - cy, x - cx)
            out.append((x + grow * math.cos(a), y + grow * math.sin(a)))
        return out

    def blob_fill(pts, rgba, grow):
        hp = hull(pts, grow)
        od.polygon(hp, fill=rgba)
        for p in pts:
            od.ellipse([p[0] - grow, p[1] - grow, p[0] + grow, p[1] + grow], fill=rgba)

    # ---------------------------------------------------- panel (a)
    T.place(img, (80, 40), "(a)  Pairwise graph   G = (U, I, E)", 68, INK, italic=False, bold=True)
    LA = {"u1": (330, 360), "u2": (330, 640), "u3": (330, 920),
          "i1": (1010, 360), "i2": (1010, 640), "i3": (1010, 920)}
    for a, b in EDGES:
        if (a, b) in PATH or (b, a) in PATH:
            continue
        d.line([LA[a], LA[b]], fill=GREY, width=4)
    arrow(*LA["u2"], *LA["i2"], (20, 20, 20), 9)
    arrow(LA["i2"][0], LA["i2"][1], LA["u1"][0] + 62, LA["u1"][1] + 26, (20, 20, 20), 9)
    for u in USERS:
        node(LA[u], u, "u", r=62)
    for i in ITEMS:
        node(LA[i], i, "i", r=62)
    # propagation rule: typeset on a strip, then centred under both panels
    strip = Image.new("RGBA", (2400, 420), (0, 0, 0, 0))
    ds = ImageDraw.Draw(strip)
    y0 = 150
    x = 60

    def mterm(x, var, sub, sup):
        x += T.place(strip, (x, y0), var, 68, INK, italic=True, bold=True)
        x += 2
        x += T.place(strip, (x, y0 + 26), sub, 68, INK, italic=True)
        if sup:
            x += 4
            x += T.place(strip, (x, y0 - 34), sup, 68, INK, italic=False)
        return x + 8

    x = mterm(x, "m", "u", "(l+1)")
    x += T.place(strip, (x, y0), "= ", 68, INK, italic=False)
    sx = x
    sigw = T.place(strip, (x, y0 - 10), "Σ", 84, INK, italic=False)
    subw = T.place(strip, (x + sigw + 4, y0 + 26), "i ∈ N(u)", 60, INK, italic=True)
    x = sx + sigw + subw + 12
    x = mterm(x, "m", "i", "(l)")
    x += T.place(strip, (x, y0), "/ ", 68, INK, italic=False)
    x += T.place(strip, (x, y0 - 6), "√", 84, INK, italic=False)
    arg = "( |N(u)| · |N(i)| )"
    aw = int(T.reg(68).getlength(arg))
    x += T.place(strip, (x, y0), arg, 68, INK, italic=False)
    ds.line([(x - aw + 4, y0 - 10), (x + 6, y0 - 10)], fill=INK, width=4)
    bb = strip.getbbox()
    cut = strip.crop(bb)
    img.paste(cut, ((W - cut.width) // 2, 1060), cut)
    T.place(img, (W // 2, 1290), "symmetric normalisation over the neighbours (LightGCN, HCCF, HPCF);",
            60, DARK, italic=False, anchor="ma")
    T.place(img, (W // 2, 1356), "hyperedge weights w(e, t) are re-learned at every step t (DyHuCoG)",
            60, DARK, italic=False, anchor="ma")

    # ---------------------------------------------------- panel (b)
    T.place(img, (1420, 40), "(b)  Hypergraph   H = (V, E)",
            68, INK, italic=False, bold=True)
    LB = {"u1": (1650, 340), "u2": (1520, 650), "u3": (1600, 950),
          "i2": (2020, 600), "i3": (2130, 920), "c1": (1990, 300),
          "i1": (2180, 260)}
    blob_fill([LB[n] for n in E2], (70, 90, 140, 42), 104)
    blob_fill([LB[n] for n in E1], (23, 118, 107, 46), 104)
    img.paste(overlay, (0, 0), overlay)
    dash_poly(hull([LB[n] for n in E2], 104), NAVY, 6)
    dash_poly(hull([LB[n] for n in E1], 104), TEAL, 6)
    node(LB["i1"], "i1", "idle", r=54)
    for u in USERS:
        node(LB[u], u, "u", r=54)
    for i in ("i2", "i3"):
        node(LB[i], i, "i", r=54)
    node(LB["c1"], "c1", "ctx", r=48)
    T.place(img, (2130, 420), "e1", 66, TEAL, italic=True, bold=True)
    T.place(img, (1950, 985), "e2", 66, NAVY, italic=True, bold=True)

    # incidence matrix H
    mx, my, cw, ch = 2270, 600, 96, 76
    T.place(img, (mx + 160, my - 128), "H", 68, INK, italic=False, bold=True)
    for j, c in enumerate(HCOLS):
        T.place(img, (mx + 120 + j * cw + cw / 2, my - 44), c, 60, INK,
                italic=True, bold=True, anchor="ma")
    for i, r in enumerate(HROWS):
        T.place(img, (mx + 95, my + i * ch + ch / 2), r, 60, INK,
                italic=True, anchor="ma")
        for j, c in enumerate(HCOLS):
            v = "1" if r in (E1 if c == "e1" else E2) else "0"
            T.place(img, (mx + 120 + j * cw + cw / 2, my + i * ch + ch / 2), v,
                    60, INK if v == "1" else GREY, italic=False, anchor="mm")
    gx0, gx1 = mx + 120 - 14, mx + 120 + 2 * cw + 14
    gy0, gy1 = my - 20, my + 7 * ch + 6
    for gx in (gx0, gx1):
        d.line([(gx, gy0), (gx, gy1)], fill=INK, width=4)
        s = -1 if gx == gx0 else 1
        d.line([(gx, gy0), (gx + 16 * s, gy0)], fill=INK, width=4)
        d.line([(gx, gy1), (gx + 16 * s, gy1)], fill=INK, width=4)

    # ---------------------------------------------------- legend
    ly = 205
    d.line([(110, ly), (190, ly)], fill=GREY, width=4)
    T.place(img, (210, ly - 30), "interaction", 60, DARK, italic=False)
    arrow(560, ly, 650, ly, (20, 20, 20), 8, head=24)
    T.place(img, (680, ly - 30), "2-hop message", 60, DARK, italic=False)
    dash_poly([(1050, ly), (1170, ly)], TEAL, 6, dash=22, gap=14)
    T.place(img, (1190, ly - 30), "hyperedge", 60, DARK, italic=False)

    img.save(out_png)
    print("wrote", out_png, img.size)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
