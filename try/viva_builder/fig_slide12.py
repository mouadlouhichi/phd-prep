"""Slide 12 figure, v39: a new figure in the style of thesis Figure 2.4.

The cropped thesis figure showed its seams, so this redraws the same
comparison as one complete composition in the same visual language: two dashed
panels; left "Graph:" with eight grey nodes joined by pairwise edges and the
adjacency matrix W below; right "Hypergraph:" with the same eight nodes,
hyperedges e1, e2, e3 drawn as solid / dashed / dash-dot curves through their
member nodes, the caption "Hyperedge group 1", and the incidence matrix H
beside them.  Sans-serif (DejaVu) type as in the thesis figure; every glyph at
or above 14 pt at slide scale (60 px at 300 dpi).

All matrices are generated from the edge and hyperedge lists below, so the
figure is self-consistent by construction.  Run:
    python3 fig_slide12.py <deck.pptx> <out.png>
"""
import math
import sys

from PIL import Image, ImageDraw, ImageFont

W, H = 2625, 1464  # 8.75 x 4.88 in at 300 dpi
DJ = "/usr/share/fonts/truetype/dejavu/"
BG = (248, 250, 252)
INK = (30, 30, 30)
NODE = (176, 176, 176)
NODE_EDGE = (120, 120, 120)
LINE = (90, 90, 90)
PANEL = (110, 110, 110)
CELL = (255, 255, 255)
ZERO = (190, 190, 190)

NODES = ["n1", "n2", "n3", "n4", "n5", "n6", "n7", "n8"]
EDGES = [("n1", "n5"), ("n1", "n6"), ("n2", "n6"), ("n3", "n6"), ("n3", "n8"), ("n4", "n7")]
HYPER = {"e1": ["n1", "n2", "n3", "n4"],
         "e2": ["n4", "n5", "n6"],
         "e3": ["n6", "n7", "n8", "n1"]}
STYLE = {"e1": "solid", "e2": "dashed", "e3": "dashdot"}


def check():
    for a, b in EDGES:
        assert a in NODES and b in NODES and a != b
    assert len({frozenset(e) for e in EDGES}) == len(EDGES)
    for e, mem in HYPER.items():
        assert set(mem) <= set(NODES) and len(mem) >= 2
    covered = set().union(*[set(m) for m in HYPER.values()])
    assert covered == set(NODES)


def circle(center, r):
    pos = {}
    for k, nm in enumerate(["n8", "n1", "n2", "n3", "n4", "n5", "n6", "n7"]):
        a = -math.pi / 2 + k * math.pi / 4
        pos[nm] = (center[0] + r * math.cos(a), center[1] + r * math.sin(a))
    return pos


def spline(pts, per=28):
    p = [pts[0]] + pts + [pts[-1]]
    out = []
    for i in range(1, len(p) - 2):
        p0, p1, p2, p3 = p[i - 1], p[i], p[i + 1], p[i + 2]
        for t in range(per):
            t = t / per
            t2, t3 = t * t, t * t * t
            x = 0.5 * ((2 * p1[0]) + (-p0[0] + p2[0]) * t + (2 * p0[0] - 5 * p1[0] + 4 * p2[0] - p3[0]) * t2 + (-p0[0] + 3 * p1[0] - 3 * p2[0] + p3[0]) * t3)
            y = 0.5 * ((2 * p1[1]) + (-p0[1] + p2[1]) * t + (2 * p0[1] - 5 * p1[1] + 4 * p2[1] - p3[1]) * t2 + (-p0[1] + 3 * p1[1] - 3 * p2[1] + p3[1]) * t3)
            out.append((x, y))
    out.append(pts[-1])
    return out


def dash_path(d, pts, pattern, width, fill):
    seg = []
    on = True
    remain = pattern[0]
    pi = 0
    for a, b in zip(pts, pts[1:]):
        L = math.hypot(b[0] - a[0], b[1] - a[1])
        if L < 1e-9:
            continue
        u = ((b[0] - a[0]) / L, (b[1] - a[1]) / L)
        s = 0.0
        while s < L:
            step = min(remain, L - s)
            if on:
                seg.append((a[0] + u[0] * s, a[1] + u[1] * s,
                            a[0] + u[0] * (s + step), a[1] + u[1] * (s + step)))
            s += step
            remain -= step
            if remain <= 1e-9:
                pi = (pi + 1) % len(pattern)
                on = not on
                remain = pattern[pi]
    for s0 in seg:
        d.line([(s0[0], s0[1]), (s0[2], s0[3])], fill=fill, width=width)


def main(deck, out_png):
    check()
    reg = lambda px: ImageFont.truetype(DJ + "DejaVuSans.ttf", px)
    bold = lambda px: ImageFont.truetype(DJ + "DejaVuSans-Bold.ttf", px)
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    def txt(x, y, s, f, fill=INK, anchor="la"):
        d.text((x, y), s, font=f, fill=fill, anchor=anchor)

    def dash_rect(x0, y0, x1, y1, width=5, dash=42, gap=26):
        for (ax, ay, bx, by) in ((x0, y0, x1, y0), (x1, y0, x1, y1),
                                 (x1, y1, x0, y1), (x0, y1, x0, y0)):
            L = math.hypot(bx - ax, by - ay)
            ux, uy = (bx - ax) / L, (by - ay) / L
            s = 0.0
            while s < L:
                e = min(s + dash, L)
                d.line([(ax + ux * s, ay + uy * s), (ax + ux * e, ay + uy * e)],
                       fill=PANEL, width=width)
                s = e + gap

    def matrix(x0, y0, cw, chh, rows, cols, get, title, tpos, hdr=None):
        txt(tpos[0], tpos[1], title, bold(68))
        hf = hdr or bold
        for j, c in enumerate(cols):
            txt(x0 + 96 + j * cw + cw / 2, y0, c, hf(60), anchor="ma")
        for i, r in enumerate(rows):
            txt(x0 + 84, y0 + 64 + i * chh + chh / 2, r, bold(60), anchor="rm")
            for j, c in enumerate(cols):
                v = get(r, c)
                cx, cy = x0 + 96 + j * cw, y0 + 64 + i * chh
                d.rectangle([cx, cy, cx + cw - 6, cy + chh - 6], fill=CELL,
                            outline=LINE, width=2)
                txt(cx + (cw - 6) / 2, cy + (chh - 6) / 2, v, reg(60),
                    INK if v == "1" else ZERO, anchor="mm")

    def labels(pos, center, off):
        for n, (x, y) in pos.items():
            ux, uy = x - center[0], y - center[1]
            L = math.hypot(ux, uy)
            txt(center[0] + ux / L * (L + off), center[1] + uy / L * (L + off),
                n, bold(62), anchor="mm")

    # ---------------------------------------------------- left panel
    dash_rect(40, 30, 820, 1430)
    txt(70, 56, "Graph:", reg(68))
    PL = circle((430, 420), 230)
    for a, b in EDGES:
        d.line([PL[a], PL[b]], fill=LINE, width=4)
    for n in NODES:
        x, y = PL[n]
        d.ellipse([x - 40, y - 40, x + 40, y + 40], fill=NODE, outline=NODE_EDGE, width=3)
    labels(PL, (430, 420), 62)
    def wget(r, c):
        return "1" if frozenset((r, c)) in {frozenset(e) for e in EDGES} else "0"
    matrix(50, 824, 84, 64, NODES, NODES, wget, "W:", (50, 756), hdr=reg)

    # ---------------------------------------------------- right panel
    dash_rect(880, 30, 2585, 1430)
    txt(910, 56, "Hypergraph:", reg(68))
    PR = circle((1480, 760), 300)
    for e in ("e3", "e2", "e1"):
        pts = spline([PR[n] for n in HYPER[e]])
        if STYLE[e] == "solid":
            d.line(pts, fill=LINE, width=9, joint="curve")
        elif STYLE[e] == "dashed":
            dash_path(d, pts, (34, 22), 9, LINE)
        else:
            dash_path(d, pts, (56, 20, 8, 20), 9, LINE)
    for n in NODES:
        x, y = PR[n]
        d.ellipse([x - 44, y - 44, x + 44, y + 44], fill=NODE, outline=NODE_EDGE, width=3)
    labels(PR, (1480, 760), 70)
    txt(1620, 680, "e1", bold(66))
    txt(1370, 930, "e2", bold(66))
    txt(1380, 540, "e3", bold(66))
    txt(1480, 1240, "Hyperedge group 1", reg(66), anchor="ma")

    def hget(r, c):
        return "1" if r in HYPER[c] else "0"
    matrix(2060, 470, 108, 64, NODES, ["e1", "e2", "e3"], hget, "H:", (1980, 400))

    img.save(out_png)
    print("wrote", out_png, img.size)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
