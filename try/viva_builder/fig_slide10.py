"""Slide 10 (Collaborative Filtering) figure, v34.

Replaces the decorative bipartite sketch (which carried un-derived similarity
values) with a figure in which every number is computed from what is shown:

  * a 4 x 5 user-item rating matrix (16 of 20 cells observed),
  * Pearson similarity of u2/u3/u4 with u1 on the co-rated columns i1, i2, i4,
  * the missing cell r(u1, i3) filled by the similarity-weighted average of the
    neighbours who rated i3,
  * a strip with the real sparsity of the thesis datasets (MovieLens-1M 4.47%
    of cells observed, Amazon-Book 0.06%).

The embedded Nunito subsets lack x, middle dot, en dash, arrow and star, so
those marks are drawn as vectors.  No text is set below 14 pt at slide scale
(300 dpi: 14 pt = 58.3 px), the smallest size used here is 60 px.

Run:  python3 fig_slide10.py <deck.pptx> <out.png>
"""
import io
import sys
import zipfile

from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFont

W, H = 2625, 1431  # 8.75 x 4.77 in at 300 dpi

BG = (248, 250, 252)
NAVY = (31, 56, 100)
BLUE = (68, 114, 196)
CARD = (220, 228, 246)
LINE = (201, 212, 232)
TEAL = (23, 118, 107)
TEALBG = (232, 244, 242)
GREY = (90, 107, 140)
LGREY = (154, 167, 191)
STRIP = (234, 240, 248)
WHITE = (255, 255, 255)

# ---------------------------------------------------------------- data (all
# values below are computed from this matrix; see check at the bottom)
R = {           # columns i1 i2 i3 i4 i5
    "u1": [5, 3, None, 4, None],
    "u2": [5, 2, 5, 2, 4],
    "u3": [3, 2, 3, 4, 2],
    "u4": [4, 4, None, 3, None],
}
USERS = ["u1", "u2", "u3", "u4"]
ITEMS = ["i1", "i2", "i3", "i4", "i5"]
CORATED = [0, 1, 3]          # columns rated by u1 (and by u2, u3, u4)
TARGET = (0, 2)              # r(u1, i3), the cell to predict
SIM = {"u2": 0.87, "u3": 0.50, "u4": 0.00}
PRED_NUM, PRED_DEN, PRED = 5.85, 1.37, 4.3


def check():
    """Every printed number must follow from R."""
    import math

    def pearson(a, b):
        ma, mb = sum(a) / len(a), sum(b) / len(b)
        da, db = [x - ma for x in a], [x - mb for x in b]
        num = sum(x * y for x, y in zip(da, db))
        den = math.sqrt(sum(x * x for x in da)) * math.sqrt(sum(y * y for y in db))
        return num / den

    u1 = [R["u1"][j] for j in CORATED]
    sims = {}
    for u in ("u2", "u3", "u4"):
        r = pearson(u1, [R[u][j] for j in CORATED])
        sims[u] = r
        assert round(r, 2) == SIM[u], (u, r)
    nb = ["u2", "u3"]  # neighbours who rated i3
    num = sum(round(sims[u], 2) * R[u][2] for u in nb)
    den = sum(round(sims[u], 2) for u in nb)
    assert round(num, 2) == PRED_NUM and round(den, 2) == PRED_DEN
    assert round(num / den, 1) == PRED
    true = sum(sims[u] * R[u][2] for u in nb) / sum(sims[u] for u in nb)
    assert round(true, 1) == PRED
    obs = sum(v is not None for row in R.values() for v in row)
    assert obs == 16
    return sims


def main(deck, out_png):
    check()
    raw = {}
    z = zipfile.ZipFile(deck)
    for n in z.namelist():
        if "font" in n.lower() and not n.endswith("/"):
            data = z.read(n)
            for o in range(0, 4096):
                if data[o:o + 4] in (b"OTTO", b"\x00\x01\x00\x00", b"true"):
                    f = TTFont(io.BytesIO(data[o:]))
                    raw[f["name"].getDebugName(4)] = data[o:]
                    break

    def FNT(name, px):
        return ImageFont.truetype(io.BytesIO(raw[name]), px)

    semi = FNT("Nunito SemiBold", 60)

    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    def txt(x, y, s, font, fill, anchor="la"):
        d.text((x, y), s, font=font, fill=fill, anchor=anchor)

    def cross(cx, cy, r, width, fill, plus=False):
        if plus:
            d.line([(cx - r, cy), (cx + r, cy)], fill=fill, width=width)
            d.line([(cx, cy - r), (cx, cy + r)], fill=fill, width=width)
        else:
            k = r * 0.72
            d.line([(cx - k, cy - k), (cx + k, cy + k)], fill=fill, width=width)
            d.line([(cx - k, cy + k), (cx + k, cy - k)], fill=fill, width=width)

    def star(cx, cy, r, fill):
        import math
        pts = []
        for i in range(10):
            rad = r if i % 2 == 0 else r * 0.45
            a = -math.pi / 2 + i * math.pi / 5
            pts.append((cx + rad * math.cos(a), cy + rad * math.sin(a)))
        d.polygon(pts, fill=fill)

    def dash_rect(x0, y0, x1, y1, fill, width, dash=26, gap=16):
        for (ax, ay, bx, by) in ((x0, y0, x1, y0), (x1, y0, x1, y1),
                                 (x1, y1, x0, y1), (x0, y1, x0, y0)):
            import math
            L = math.hypot(bx - ax, by - ay)
            n = int(L // (dash + gap)) + 1
            ux, uy = (bx - ax) / L, (by - ay) / L
            for i in range(n):
                s0 = i * (dash + gap)
                s1 = min(s0 + dash, L)
                d.line([(ax + ux * s0, ay + uy * s0), (ax + ux * s1, ay + uy * s1)],
                       fill=fill, width=width)

    def seq(x, y, tokens, font, fill, op=46, pad=16):
        """tokens: ('t', text) or ('x',) times or ('p',) plus; returns end x."""
        for tk in tokens:
            if tk[0] == "t":
                txt(x, y, tk[1], font, fill)
                x += font.getlength(tk[1]) + pad
            else:
                cx = x + op / 2
                cross(cx, y + 31, 20, 6, fill, plus=(tk[0] == "p"))
                x += op + pad
        return x

    # ---------------------------------------------------- panel A: matrix
    left, cw, cg = 220, 168, 12
    top, ch, rg = 260, 168, 12
    for j, it in enumerate(ITEMS):
        x = left + j * (cw + cg)
        d.rounded_rectangle([x, 150, x + cw, 230], 18, fill=CARD, outline=NAVY, width=3)
        txt(x + cw / 2, 190, it, FNT("Nunito Bold", 62), NAVY, anchor="mm")
        if j in CORATED:
            d.rectangle([x + 8, 238, x + cw - 8, 246], fill=TEAL)
    for i, u in enumerate(USERS):
        cy = top + i * (ch + rg) + ch / 2
        if u == "u1":
            d.ellipse([140 - 50, cy - 50, 140 + 50, cy + 50], fill=TEAL)
            txt(140, cy, u, FNT("Nunito Bold", 60), WHITE, anchor="mm")
        else:
            d.ellipse([140 - 50, cy - 50, 140 + 50, cy + 50], fill=CARD, outline=NAVY, width=3)
            txt(140, cy, u, FNT("Nunito Bold", 60), NAVY, anchor="mm")
        for j in range(5):
            x = left + j * (cw + cg)
            y = top + i * (ch + rg)
            v = R[u][j]
            if (i, j) == TARGET:
                d.rectangle([x, y, x + cw, y + ch], fill=TEALBG)
                dash_rect(x, y, x + cw, y + ch, TEAL, 5)
                star(x + cw / 2, y + ch / 2, 46, TEAL)
            elif v is None:
                d.rounded_rectangle([x, y, x + cw, y + ch], 16, fill=WHITE, outline=LINE, width=3)
                txt(x + cw / 2, y + ch / 2, "?", FNT("Nunito Bold", 62), LGREY, anchor="mm")
            else:
                d.rounded_rectangle([x, y, x + cw, y + ch], 16, fill=CARD, outline=NAVY, width=3)
                txt(x + cw / 2, y + ch / 2, str(v), FNT("Nunito Bold", 78), NAVY, anchor="mm")
    txt(70, 985, "User-item rating matrix,", semi, GREY)
    txt(70, 1052, "ratings 1 to 5, 16 of 20 observed", semi, GREY)

    # ---------------------------------------------------- panel B: similarity
    txt(1210, 150, "Similarity to u1", FNT("Nunito Bold", 66), NAVY)
    x0 = 1430
    d.line([(x0, 260), (x0, 740)], fill=LINE, width=3)
    for k, u in enumerate(("u2", "u3", "u4")):
        cy = 330 + k * 170
        txt(1215, cy, u, FNT("Nunito Bold", 62), NAVY, anchor="lm")
        v = SIM[u]
        bw = int(v * 260)
        if bw:
            d.rounded_rectangle([x0, cy - 28, x0 + bw, cy + 28], 14, fill=BLUE)
            txt(x0 + bw + 16, cy, f"{v:.2f}", FNT("Nunito Bold", 62), NAVY, anchor="lm")
        else:
            d.ellipse([x0 - 7, cy - 7, x0 + 7, cy + 7], fill=NAVY)
            txt(x0 + 16, cy, "0.00", FNT("Nunito Bold", 62), GREY, anchor="lm")
    txt(1210, 940, "Pearson correlation", semi, GREY)
    txt(1210, 1007, "on co-rated columns", semi, GREY)
    d.rectangle([1210, 1088, 1270, 1096], fill=TEAL)
    txt(1286, 1074, "i1, i2, i4", semi, GREY)

    # ---------------------------------------------------- panel C: prediction
    txt(1860, 150, "The prediction", FNT("Nunito Bold", 66), NAVY)
    txt(1860, 268, "Neighbours rating i3:", semi, NAVY)
    for k, u in enumerate(("u2", "u3")):
        cx = 1900 + k * 110
        d.ellipse([cx - 34, 372 - 34, cx + 34, 372 + 34], fill=CARD, outline=NAVY, width=3)
        txt(cx, 372, u, FNT("Nunito Bold", 52), NAVY, anchor="mm")
    vfont = FNT("Nunito Bold", 62)
    seq(1860, 452, [("t", "0.87"), ("x",), ("t", "5"), ("p",), ("t", "0.50"), ("x",), ("t", "3")], vfont, NAVY)
    d.line([(1860, 548), (2400, 548)], fill=NAVY, width=4)
    seq(1860, 572, [("t", "0.87"), ("p",), ("t", "0.50")], vfont, NAVY)
    txt(1860, 660, "= 4.3", FNT("Nunito ExtraBold", 84), TEAL)
    d.rounded_rectangle([2120, 664, 2560, 764], 50, fill=TEAL)
    star(2176, 714, 28, WHITE)
    txt(2216, 714, "predicted", FNT("Nunito Bold", 60), WHITE, anchor="lm")
    txt(1860, 990, "Weighted average of", semi, GREY)
    txt(1860, 1057, "neighbours' ratings", semi, GREY)

    # ---------------------------------------------------- sparsity strip
    d.rounded_rectangle([70, 1150, 2555, 1385], 24, fill=STRIP, outline=LINE, width=3)
    txt(150, 1172, "The real matrices are far sparser than this sketch:", FNT("Nunito SemiBold", 60), NAVY)
    txt(150, 1242, "MovieLens-1M: 4.47% of cells observed (6,040 users, 3,706 items)", semi, NAVY)
    txt(150, 1312, "Amazon-Book: 0.06% of cells observed (52,643 users, 91,599 items)", semi, NAVY)

    img.save(out_png)
    print("wrote", out_png, img.size)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
