"""Rendered diagrams for the Context & Problematic section.

v15 drew these figures at 300 dpi with 9-13 pt type and 1-2 px strokes;
placed at 8.75 in on a 20 in slide that reads as faint, blurry text.
This version renders at 600 dpi with a much larger type scale
(minimum 13 pt, node/panel labels 15-16 pt, figures and callouts up to
24 pt) and heavier strokes, using the deck's own font files so the type
matches the slides around it.
"""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import Circle, FancyBboxPatch, FancyArrowPatch, Polygon, Rectangle

# v14 palette
BLUE = "#4472C4"
NAVY = "#2F5597"
PALE = "#D9E2F3"
TEAL = "#1F7A8C"
INK = "#232A33"
MUTED = "#6B7280"
RULE = "#D8DEE8"
WHITE = "#FFFFFF"

DPI = 600
_W, _H = 8.75, 5.94


def _fonts(fontdir):
    reg = {}
    for key, fn in (("title", "RocaTwo-Bold.otf"), ("label", "Nunito-ExtraBold.ttf"),
                    ("body", "Nunito-SemiBold.ttf")):
        p = os.path.join(fontdir, fn)
        if os.path.exists(p):
            font_manager.fontManager.addfont(p)
            reg[key] = font_manager.FontProperties(fname=p).get_name()
    reg.setdefault("title", "DejaVu Sans")
    reg.setdefault("label", reg["title"])
    reg.setdefault("body", reg["title"])
    return reg


def _fig():
    fig, ax = plt.subplots(figsize=(_W, _H), dpi=DPI)
    fig.patch.set_alpha(0)
    ax.set_facecolor("none")
    ax.set_xlim(0, _W)
    ax.set_ylim(0, _H)
    ax.invert_yaxis()
    ax.axis("off")
    fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
    return fig, ax


def _box(ax, x, y, w, h, fc, ec="none", r=0.16, lw=2.0, alpha=1.0, z=2):
    ax.add_patch(FancyBboxPatch((x, y), w, h,
                                boxstyle=f"round,pad=0,rounding_size={r}",
                                fc=fc, ec=ec, lw=lw, alpha=alpha, zorder=z,
                                mutation_aspect=1))


def _txt(ax, x, y, s, size, color, fam, ha="center", va="center", z=5, **kw):
    ax.text(x, y, s, fontsize=size, color=color, family=fam, ha=ha, va=va, zorder=z, **kw)


def _arrow(ax, p, q, color, lw=2.8, rad=0.0, style="-|>", z=3, ls="-", alpha=1.0, ms=18):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle=style, mutation_scale=ms,
                                 color=color, lw=lw, zorder=z, linestyle=ls, alpha=alpha,
                                 connectionstyle=f"arc3,rad={rad}", shrinkA=0, shrinkB=0))


def _eyebrow(ax, s, F):
    _txt(ax, _W / 2, 0.32, s.upper(), 16, TEAL, F["label"], z=6)
    ax.plot([_W / 2 - 1.35, _W / 2 + 1.35], [0.60, 0.60], color=TEAL, lw=2.2, zorder=6, alpha=.7)


# ---------------------------------------------------------------------------
# 1. Content-based filtering
# ---------------------------------------------------------------------------
def diag_content(ax, F):
    _eyebrow(ax, "Content-based filtering", F)
    feats = [("genre", "Sci-Fi", 0.92, 0.88), ("director", "Nolan", 0.85, 0.79),
             ("year", "2010", 0.33, 0.30)]
    for name, x0, c in (("USER PROFILE", 0.45, BLUE), ("CANDIDATE ITEM", 4.75, NAVY)):
        _box(ax, x0, 0.85, 3.55, 3.05, WHITE, ec=RULE, r=0.14, lw=2.0)
        _box(ax, x0, 0.85, 3.55, 0.62, c, r=0.14)
        _txt(ax, x0 + 1.775, 1.16, name, 15, WHITE, F["label"])
        for i, (k, v, a, b) in enumerate(feats):
            yy = 1.80 + i * 0.72
            val = a if x0 < 4 else b
            _txt(ax, x0 + 0.26, yy, f"{k}: {v}", 14, INK, F["body"], ha="left")
            _box(ax, x0 + 0.26, yy + 0.20, 3.03, 0.22, PALE, r=0.10, lw=0)
            hot = k != "year"
            _box(ax, x0 + 0.26, yy + 0.20, 3.03 * val, 0.22, TEAL if hot else BLUE, r=0.10, lw=0)
    _arrow(ax, (4.05, 2.35), (4.70, 2.35), TEAL, lw=3.4, ms=22)
    _txt(ax, 4.375, 1.95, "cos", 15, TEAL, F["label"])
    _box(ax, 0.45, 4.10, 7.85, 0.78, PALE, r=0.14)
    ax.text(4.375, 4.49, r"$\mathrm{sim}(u,i)=\cos(f_u,f_i)=\mathbf{0.91}$",
            fontsize=19, color=NAVY, family=F["body"], ha="center", va="center", zorder=6)
    _box(ax, 0.45, 5.05, 7.85, 0.78, TEAL, r=0.14)
    _txt(ax, 4.375, 5.44, "Explainable: the reason is a named feature you can act on",
         15, WHITE, F["label"])


# ---------------------------------------------------------------------------
# 2. Collaborative filtering
# ---------------------------------------------------------------------------
def diag_cf(ax, F):
    _eyebrow(ax, "Collaborative filtering", F)
    U = {"u1": (1.30, 1.60), "u2": (1.10, 2.80), "u3": (1.40, 4.00)}
    I = {"i1": (6.05, 1.30), "i2": (6.20, 2.35), "i3": (6.00, 3.40),
         "i4": (6.25, 4.45), "i5": (6.05, 5.40)}
    E = [("u1", "i1"), ("u1", "i2"), ("u2", "i1"), ("u2", "i2"), ("u2", "i3"),
         ("u3", "i3"), ("u3", "i4")]
    for a, b in E:
        hot = a == "u1"
        near = a == "u2"
        _arrow(ax, U[a], I[b], TEAL if hot else (BLUE if near else RULE),
               lw=3.4 if hot else (2.4 if near else 1.8), rad=0.12, style="-",
               alpha=1.0 if (hot or near) else 0.9)
    _arrow(ax, U["u1"], I["i5"], TEAL, lw=3.4, rad=-0.22, ls=(0, (4, 3)), ms=24)
    _txt(ax, 4.90, 4.60, "predicted", 15, TEAL, F["label"], rotation=-20)
    ax.add_patch(Circle(U["u1"], 0.62, fc=TEAL, ec="none", alpha=0.16, zorder=1))
    for k, (x, y) in U.items():
        on = k == "u1"
        ax.add_patch(Circle((x, y), 0.42, fc=TEAL if on else BLUE, ec=WHITE, lw=3.0, zorder=4))
        _txt(ax, x, y, k, 15, WHITE, F["label"], z=6)
    for k, (x, y) in I.items():
        pred = k == "i5"
        _box(ax, x - 0.40, y - 0.36, 0.80, 0.72, WHITE if pred else NAVY,
             ec=TEAL if pred else "none", r=0.16, lw=3.0, z=4)
        _txt(ax, x, y, k, 15, TEAL if pred else WHITE, F["label"], z=6)
    _txt(ax, 1.25, 0.85, "users", 14, MUTED, F["body"])
    _txt(ax, 6.12, 0.78, "items", 14, MUTED, F["body"])
    _box(ax, 7.05, 1.10, 1.50, 1.55, PALE, r=0.14)
    _txt(ax, 7.80, 1.40, "u1 ~ u2", 14, NAVY, F["label"])
    _txt(ax, 7.80, 1.78, "0.87", 22, NAVY, F["label"])
    _txt(ax, 7.80, 2.20, "u1 ~ u4", 13, MUTED, F["body"])
    _txt(ax, 7.80, 2.47, "0.21", 17, MUTED, F["body"])


# ---------------------------------------------------------------------------
# 3. Matrix factorisation
# ---------------------------------------------------------------------------
def diag_mf(ax, F, rng):
    _eyebrow(ax, "Matrix factorisation", F)
    def ramp(t):
        return "#%02X%02X%02X" % tuple(int(a + (b - a) * t) for a, b in
                                       zip((0xD9, 0xE2, 0xF3), (0x2F, 0x55, 0x97)))
    def cells(x0, y0, M, missing=None, c=0.36):
        for i in range(M.shape[0]):
            for j in range(M.shape[1]):
                v = M[i, j]
                if missing is not None and missing[i, j]:
                    fc, ec = WHITE, RULE
                else:
                    fc, ec = ramp(min(max(v, 0), 1)), "none"
                ax.add_patch(Rectangle((x0 + j * c, y0 + i * c), c * 0.93, c * 0.90,
                                       fc=fc, ec=ec, lw=1.0, zorder=3))
    n, m, k = 6, 7, 3
    R = rng.random((n, m))
    miss = rng.random((n, m)) < 0.30
    rx, ry = 0.45, 1.10
    cells(rx, ry, R, miss)
    _txt(ax, rx + m * 0.36 / 2, ry - 0.32, "R  (mostly empty)", 14, MUTED, F["body"])
    ux, uy = 4.05, 1.10
    cells(ux, uy, rng.random((n, k)))
    _txt(ax, ux + k * 0.36 / 2, uy - 0.32, "U", 16, NAVY, F["label"])
    vx, vy = 6.00, 1.10
    cells(vx, vy, rng.random((k, m)))
    _txt(ax, vx + m * 0.36 / 2, vy - 0.32, "V", 16, NAVY, F["label"])
    _txt(ax, 3.55, 2.10, "\u2248", 30, NAVY, F["body"])
    _txt(ax, 5.52, 1.62, "\u00d7", 26, NAVY, F["body"])
    _txt(ax, rx + m * 0.36 / 2, ry + n * 0.36 + 0.34, "30 % observed", 14, TEAL, F["label"])
    _box(ax, 0.45, 4.10, 7.85, 0.78, PALE, r=0.14)
    ax.text(4.375, 4.49, r"$\hat{r}_{ui}=\mu+b_u+b_i+\langle u_i,v_j\rangle,\qquad k=8$",
            fontsize=19, color=NAVY, family=F["body"], ha="center", va="center", zorder=6)
    _box(ax, 0.45, 5.05, 7.85, 0.78, TEAL, r=0.14)
    _txt(ax, 4.375, 5.44, "The 8 factors are latent: no name, no unit, nothing to act on",
         15, WHITE, F["label"])


# ---------------------------------------------------------------------------
# 4. Graph vs hypergraph
# ---------------------------------------------------------------------------
def _hull(pts, pad=0.5):
    p = sorted(set(pts))
    if len(p) < 3:
        return None
    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    lo = []
    for q in p:
        while len(lo) >= 2 and cross(lo[-2], lo[-1], q) <= 0:
            lo.pop()
        lo.append(q)
    up = []
    for q in reversed(p):
        while len(up) >= 2 and cross(up[-2], up[-1], q) <= 0:
            up.pop()
        up.append(q)
    h = lo[:-1] + up[:-1]
    cx = sum(q[0] for q in h) / len(h)
    cy = sum(q[1] for q in h) / len(h)
    out = []
    for x, y in h:
        dx, dy = x - cx, y - cy
        d = (dx * dx + dy * dy) ** 0.5 or 1
        out.append((cx + dx * (1 + pad / d), cy + dy * (1 + pad / d)))
    return out


def diag_hyper(ax, F):
    _eyebrow(ax, "Graph vs hypergraph", F)
    for x0, title in ((0.35, "Pairwise graph"), (4.55, "Hypergraph")):
        _box(ax, x0, 0.85, 3.85, 3.95, WHITE, ec=RULE, r=0.16, lw=2.0, z=1)
        _txt(ax, x0 + 1.925, 1.18, title.upper(), 15, NAVY, F["label"], z=6)
    nodes = {"u": (1.30, 2.20), "i": (3.25, 2.20), "c": (2.28, 3.80),
             "t": (3.55, 3.45), "l": (1.05, 3.55)}
    shift = 4.20
    for a, b in [("u", "i"), ("i", "c"), ("u", "c"), ("c", "t"), ("u", "l"), ("l", "c")]:
        _arrow(ax, nodes[a], nodes[b], BLUE, lw=2.4, style="-", rad=0.06)
    for (members), col in ((["u", "i", "c"], TEAL), (["c", "t", "l"], NAVY)):
        pts = [(nodes[m][0] + shift, nodes[m][1]) for m in members]
        hull = _hull(pts)
        if hull:
            ax.add_patch(Polygon(hull, closed=True, fc=col, ec=col, lw=2.6,
                                 alpha=0.16, zorder=2, joinstyle="round"))
    for k, (x, y) in nodes.items():
        for xx, col in ((x, BLUE), (x + shift, NAVY)):
            ax.add_patch(Circle((xx, y), 0.36, fc=col, ec=WHITE, lw=3.0, zorder=5))
            _txt(ax, xx, y, k.upper(), 14, WHITE, F["label"], z=7)
    _txt(ax, 2.28, 4.50, "2 nodes per edge", 13, MUTED, F["body"], z=6)
    _txt(ax, 6.48, 4.50, "1 edge over 3 nodes", 14, TEAL, F["label"], z=6)
    _box(ax, 0.35, 4.98, 8.05, 0.84, TEAL, r=0.14)
    _txt(ax, 4.375, 5.26, "A hyperedge joins a user, an item and its whole context at once,", 14.5, WHITE, F["label"])
    _txt(ax, 4.375, 5.56, "which is why the coalition here is a set, not a pair.", 14.5, WHITE, F["label"])


FIGURES = {
    "ctx_content.png": diag_content,
    "ctx_cf.png": diag_cf,
    "ctx_mf.png": diag_mf,
    "ctx_hyper.png": diag_hyper,
}


def render_all(outdir, fontdir, seed=7):
    import numpy as np
    os.makedirs(outdir, exist_ok=True)
    F = _fonts(fontdir)
    made = []
    for name, fn in FIGURES.items():
        fig, ax = _fig()
        if fn is diag_mf:
            fn(ax, F, np.random.default_rng(seed))
        else:
            fn(ax, F)
        p = os.path.join(outdir, name)
        fig.savefig(p, transparent=True, dpi=DPI)
        plt.close(fig)
        made.append(p)
    return made


if __name__ == "__main__":
    import sys
    for p in render_all(sys.argv[1], sys.argv[2]):
        print("wrote", p)
