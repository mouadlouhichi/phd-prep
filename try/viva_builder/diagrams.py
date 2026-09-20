"""Rendered diagrams for the Context & Problematic section.

The four approach slides used to carry hand-placed chip-and-arrow
schematics. The reference viva deck is far denser (its slides average
9.5 pictures each, mostly 512x512 icons on every node, while 1,770 of
its 1,783 shapes are plain rectangles) so the fix is not fancier
vector shapes but properly drawn figures.

Each diagram is rendered with matplotlib at 300 dpi on a transparent
background, in the v14 palette, using the deck's own font files so the
type matches the slides around it.
"""
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import Circle, FancyBboxPatch, FancyArrowPatch, Polygon, Rectangle

# v14 palette
BLUE = "#4472C4"      # reference accent1
NAVY = "#2F5597"      # accent1, darker 25%
PALE = "#D9E2F3"      # accent1, lighter 80%
TEAL = "#1F7A8C"      # accent (was orange)
INK = "#111111"
MUTED = "#6B7280"
RULE = "#D8DEE8"
WHITE = "#FFFFFF"

_W, _H = 8.75, 5.94   # inches, matches the diagram region on the slide


def _fonts(fontdir):
    """Register the deck's fonts and return (title, label) family names."""
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
    fig, ax = plt.subplots(figsize=(_W, _H), dpi=300)
    fig.patch.set_alpha(0)
    ax.set_facecolor("none")
    ax.set_xlim(0, _W)
    ax.set_ylim(0, _H)
    ax.invert_yaxis()          # y grows downward, like slide coordinates
    ax.axis("off")
    fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
    return fig, ax


def _box(ax, x, y, w, h, fc, ec="none", r=0.14, lw=1.6, alpha=1.0, z=2):
    ax.add_patch(FancyBboxPatch((x, y), w, h,
                                boxstyle=f"round,pad=0,rounding_size={r}",
                                fc=fc, ec=ec, lw=lw, alpha=alpha, zorder=z,
                                mutation_aspect=1))


def _txt(ax, x, y, s, size, color, fam, ha="center", va="center", z=5, **kw):
    ax.text(x, y, s, fontsize=size, color=color, family=fam, ha=ha, va=va, zorder=z, **kw)


def _arrow(ax, p, q, color, lw=2.0, rad=0.0, style="-|>", z=3, ls="-", alpha=1.0, ms=14):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle=style, mutation_scale=ms,
                                 color=color, lw=lw, zorder=z, linestyle=ls, alpha=alpha,
                                 connectionstyle=f"arc3,rad={rad}",
                                 shrinkA=0, shrinkB=0))


def _eyebrow(ax, s, F):
    _txt(ax, _W / 2, 0.30, s.upper(), 12.5, TEAL, F["label"], z=6)
    ax.plot([_W / 2 - 1.15, _W / 2 + 1.15], [0.52, 0.52], color=TEAL, lw=1.4, zorder=6, alpha=.6)


# ---------------------------------------------------------------------------
# 1. Content-based filtering: named features you can compare
# ---------------------------------------------------------------------------
def diag_content(ax, F):
    _eyebrow(ax, "Content-based filtering", F)
    feats = [("genre", "Sci-Fi", 0.92, 0.88), ("director", "Nolan", 0.85, 0.79),
             ("cast", "…", 0.41, 0.12), ("year", "2010", 0.33, 0.30)]
    cols = [("USER PROFILE", 0.55, BLUE), ("CANDIDATE ITEM", 4.85, NAVY)]
    for name, x0, c in cols:
        _box(ax, x0, 0.78, 3.35, 3.30, WHITE, ec=RULE, r=0.12, lw=1.5)
        _box(ax, x0, 0.78, 3.35, 0.52, c, r=0.12)
        _txt(ax, x0 + 1.675, 1.05, name, 11.5, WHITE, F["label"])
        for i, (k, v, a, b) in enumerate(feats):
            yy = 1.62 + i * 0.62
            val = a if x0 < 4 else b
            _txt(ax, x0 + 0.22, yy, k, 9.5, MUTED, F["body"], ha="left")
            _txt(ax, x0 + 1.15, yy, v, 9.5, INK, F["body"], ha="left")
            _box(ax, x0 + 0.22, yy + 0.14, 2.9, 0.16, PALE, r=0.08, lw=0)
            hot = (k in ("genre", "director"))
            _box(ax, x0 + 0.22, yy + 0.14, 2.9 * val, 0.16, TEAL if hot else BLUE, r=0.08, lw=0)
    _arrow(ax, (3.95, 2.4), (4.80, 2.4), TEAL, lw=2.4, ms=16)
    _txt(ax, 4.38, 2.05, "cos", 11, TEAL, F["label"])
    _box(ax, 0.55, 4.30, 7.65, 0.62, PALE, r=0.12)
    ax.text(4.375, 4.62, r"$\mathrm{sim}(u,i)=\cos(f_u,f_i)=\mathbf{0.91}$",
            fontsize=13, color=NAVY, family=F["body"], ha="center", va="center", zorder=6)
    _box(ax, 0.55, 5.08, 7.65, 0.66, TEAL, r=0.12)
    _txt(ax, 4.375, 5.41, "Explainable: the reason is a named feature you can act on",
         11, WHITE, F["label"])


# ---------------------------------------------------------------------------
# 2. Collaborative filtering: bipartite graph, neighbourhood, prediction
# ---------------------------------------------------------------------------
def diag_cf(ax, F):
    _eyebrow(ax, "Collaborative filtering  ·  user-based", F)
    U = {"u1": (1.35, 1.55), "u2": (1.15, 2.65), "u3": (1.45, 3.75), "u4": (1.20, 4.80)}
    I = {"i1": (6.05, 1.25), "i2": (6.20, 2.20), "i3": (6.00, 3.15),
         "i4": (6.25, 4.10), "i5": (6.05, 5.05)}
    E = [("u1", "i1"), ("u1", "i2"), ("u2", "i1"), ("u2", "i2"), ("u2", "i3"),
         ("u3", "i3"), ("u3", "i4"), ("u4", "i4"), ("u4", "i5")]
    nb = {"u2", "u3"}
    for a, b in E:
        hot = a == "u1" and b in ("i1", "i2")
        near = a in nb
        c = TEAL if hot else (BLUE if near else RULE)
        _arrow(ax, U[a], I[b], c, lw=2.6 if hot else (1.8 if near else 1.3),
               rad=0.13, style="-", alpha=1.0 if (hot or near) else 0.85)
    _arrow(ax, U["u1"], I["i5"], TEAL, lw=2.6, rad=-0.22, ls=(0, (4, 3)), ms=17)
    _txt(ax, 4.95, 4.55, "predicted", 10, TEAL, F["label"], rotation=-18)
    ax.add_patch(Circle(U["u1"], 0.52, fc=TEAL, ec="none", alpha=0.14, zorder=1))
    for k, (x, y) in U.items():
        on = k == "u1"
        ax.add_patch(Circle((x, y), 0.34, fc=TEAL if on else BLUE, ec=WHITE, lw=2.2, zorder=4))
        _txt(ax, x, y, k, 11, WHITE, F["label"], z=6)
    for k, (x, y) in I.items():
        pred = k == "i5"
        _box(ax, x - 0.32, y - 0.30, 0.64, 0.60,
             WHITE if pred else NAVY, ec=TEAL if pred else "none", r=0.13, lw=2.4, z=4)
        _txt(ax, x, y, k, 11, TEAL if pred else WHITE, F["label"], z=6)
    _txt(ax, 1.30, 0.72, "users", 10.5, MUTED, F["body"])
    _txt(ax, 6.12, 0.62, "items", 10.5, MUTED, F["body"])
    _box(ax, 7.05, 1.15, 1.45, 1.42, PALE, r=0.12)
    _txt(ax, 7.775, 1.42, "u1 ~ u2", 10.5, NAVY, F["label"])
    _txt(ax, 7.775, 1.72, "0.87", 15, NAVY, F["label"])
    _txt(ax, 7.775, 2.10, "u1 ~ u4", 10.5, MUTED, F["body"])
    _txt(ax, 7.775, 2.36, "0.21", 13, MUTED, F["body"])
    _box(ax, 0.55, 5.28, 4.55, 0.56, WHITE, ec=RULE, r=0.12, lw=1.4)
    _txt(ax, 2.825, 5.56, "No item content is used, only the rating pattern",
         9.5, INK, F["body"])


# ---------------------------------------------------------------------------
# 3. Hybrid / matrix factorisation: the actual decomposition
# ---------------------------------------------------------------------------
def diag_mf(ax, F, rng):
    _eyebrow(ax, "Matrix factorisation", F)
    n, m, k = 7, 8, 3
    def ramp(t):
        return "#%02X%02X%02X" % tuple(int(a + (b - a) * t) for a, b in
                                       zip((0xD9, 0xE2, 0xF3), (0x2F, 0x55, 0x97)))
    def cells(x0, y0, M, missing=None, c=0.33):
        for i in range(M.shape[0]):
            for j in range(M.shape[1]):
                v = M[i, j]
                if missing is not None and missing[i, j]:
                    fc, ec = WHITE, RULE
                else:
                    fc, ec = ramp(min(max(v, 0), 1)), "none"
                ax.add_patch(Rectangle((x0 + j * c, y0 + i * c), c * 0.93, c * 0.90,
                                       fc=fc, ec=ec, lw=0.8, zorder=3))
    R = rng.random((n, m))
    miss = rng.random((n, m)) < 0.30
    rx, ry = 0.40, 1.05
    cells(rx, ry, R, miss)
    _txt(ax, rx + m * 0.33 / 2, ry - 0.28, "R  (ratings, mostly empty)", 10, MUTED, F["body"])
    _txt(ax, rx + m * 0.33 / 2, ry + n * 0.33 + 0.30, "30 % observed", 9.5, TEAL, F["label"])
    ux, uy = 3.95, 1.05
    cells(ux, uy, rng.random((n, k)))
    _txt(ax, ux + k * 0.33 / 2, uy - 0.28, "U  (users x k)", 10, MUTED, F["body"])
    vx, vy = 5.85, 1.05
    cells(vx, vy, rng.random((k, m)))
    _txt(ax, vx + m * 0.33 / 2, vy - 0.28, r"$V^{\top}$  (k x items)", 10, MUTED, F["body"])
    _txt(ax, 3.52, 2.20, "\u2248", 24, NAVY, F["body"])
    _txt(ax, 5.42, 1.55, "\u00d7", 20, NAVY, F["body"])
    _box(ax, 0.45, 4.35, 7.85, 0.62, PALE, r=0.12)
    ax.text(4.375, 4.66, r"$\hat{r}_{ui}=\mu+b_u+b_i+\langle u_i,v_j\rangle,\qquad k=8$",
            fontsize=13, color=NAVY, family=F["body"], ha="center", va="center", zorder=6)
    _box(ax, 0.45, 5.13, 7.85, 0.66, TEAL, r=0.12)
    _txt(ax, 4.375, 5.46, "The 8 factors are latent: no name, no unit, nothing to act on",
         10.5, WHITE, F["label"])


# ---------------------------------------------------------------------------
# 4. Graph vs hypergraph: pairwise edges vs one hyperedge over many nodes
# ---------------------------------------------------------------------------
def _hull(pts, pad=0.42):
    """Convex hull (monotone chain), then pushed outward from its centroid."""
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
        _box(ax, x0, 0.78, 3.85, 4.0, WHITE, ec=RULE, r=0.14, lw=1.5, z=1)
        _txt(ax, x0 + 1.925, 1.08, title.upper(), 11, NAVY, F["label"], z=6)
    nodes = {"user": (1.30, 2.10), "item": (3.25, 2.10), "ctx": (2.28, 3.85),
             "time": (3.55, 3.55), "loc": (1.05, 3.60)}
    shift = 4.20
    for a, b in [("user", "item"), ("item", "ctx"), ("user", "ctx"),
                 ("ctx", "time"), ("user", "loc"), ("loc", "ctx")]:
        _arrow(ax, nodes[a], nodes[b], BLUE, lw=1.7, style="-", rad=0.06)
    _txt(ax, 2.28, 4.52, "only 2 nodes per edge", 9.5, MUTED, F["body"], z=6)
    H = {"h1": ["user", "item", "ctx"], "h2": ["ctx", "time", "loc"]}
    for (key, members), col in zip(H.items(), (TEAL, NAVY)):
        pts = [(nodes[m][0] + shift, nodes[m][1]) for m in members]
        hull = _hull(pts)
        if hull:
            ax.add_patch(Polygon(hull, closed=True, fc=col, ec=col, lw=2.0,
                                 alpha=0.16, zorder=2, joinstyle="round"))
    for a, b in [("user", "ctx"), ("item", "ctx"), ("ctx", "time")]:
        _arrow(ax, (nodes[a][0] + shift, nodes[a][1]), (nodes[b][0] + shift, nodes[b][1]),
               RULE, lw=1.2, style="-", rad=0.05, alpha=0.9)
    for k, (x, y) in nodes.items():
        for xx, col in ((x, BLUE), (x + shift, NAVY)):
            ax.add_patch(Circle((xx, y), 0.30, fc=col, ec=WHITE, lw=2.2, zorder=5))
            _txt(ax, xx, y, k[0].upper(), 10.5, WHITE, F["label"], z=7)
    _txt(ax, 6.48, 4.52, "one edge over 3 nodes", 9.5, TEAL, F["label"], z=6)
    _box(ax, 0.35, 4.98, 8.05, 0.80, TEAL, r=0.12)
    _txt(ax, 4.375, 5.24, "A hyperedge joins a user, an item and its whole context at once,", 10.5, WHITE, F["label"])
    _txt(ax, 4.375, 5.53, "which is why the coalition in this thesis is a set, not a pair.", 10.5, WHITE, F["label"])


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
        fig.savefig(p, transparent=True, dpi=300)
        plt.close(fig)
        made.append(p)
    return made


if __name__ == "__main__":
    import sys
    for p in render_all(sys.argv[1], sys.argv[2]):
        print("wrote", p)
