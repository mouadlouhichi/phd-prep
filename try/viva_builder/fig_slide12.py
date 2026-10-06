"""Slide 12 (Graph-Based and Hypergraph Recommenders) figure, v35.

The old picture drew the "pairwise graph" as a near-complete graph over users,
items and context nodes (clock-tag, pin-tag, ... edges that no recommender
graph contains), and the hypergraph blobs grouped nodes arbitrarily with no
tie to message passing or to DyHuCoG.  The new figure shows what the slide
text actually claims:

  * left: the bipartite user-item graph used by LightGCN / HCCF / HPCF, whose
    edges are exactly the observed interactions, with one 2-hop message path
    (u2 - i2 - u1) highlighted and every edge carrying the same weight (the
    limitation named on the slide);
  * right: the same nodes plus a context node, with two hyperedges, one of
    them joining a user, an item and a context at once, and weights that are
    re-learned at every step (DyHuCoG);
  * bottom tag kept in spirit: one hyperedge joins many nodes.

Drawn at 300 dpi in the deck palette with the deck's Nunito; no label below
14 pt at slide scale (60 px here).  Run:
    python3 fig_slide12.py <deck.pptx> <out.png>
"""
import io
import math
import sys
import zipfile

from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFont

W, H = 2625, 1464  # 8.75 x 4.88 in at 300 dpi

BG = (248, 250, 252)
NAVY = (31, 56, 100)
BLUE = (68, 114, 196)
CARD = (220, 228, 246)
LINE = (201, 212, 232)
TEAL = (23, 118, 107)
TEALF = (127, 181, 172)
GREYF = (174, 182, 204)
GREY = (90, 107, 140)
WHITE = (255, 255, 255)

USERS = ["u1", "u2", "u3"]
ITEMS = ["i1", "i2", "i3"]
EDGES = [("u1", "i1"), ("u1", "i2"), ("u2", "i2"), ("u2", "i3"), ("u3", "i3")]
PATH = [("u2", "i2"), ("i2", "u1")]          # 2-hop message to u1
E1 = ["u1", "u2", "i2", "c1"]               # hyperedge with context
E2 = ["u2", "u3", "i3"]


def check():
    nodes = set(USERS) | set(ITEMS)
    for a, b in EDGES:
        assert (a in USERS and b in ITEMS) or (a in ITEMS and b in USERS)
    for a, b in PATH:
        assert (a, b) in EDGES or (b, a) in EDGES
    assert PATH[0][1] == PATH[1][0] == "i2"  # genuine 2-hop path through i2
    for e in (E1, E2):
        assert set(e) <= nodes | {"c1"}
    assert "c1" in E1 and len(E1) > 2


def load_raw(deck):
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
    return raw


def main(deck, out_png):
    check()
    raw = load_raw(deck)

    def FNT(name, px):
        return ImageFont.truetype(io.BytesIO(raw[name]), px)

    semi, bold, xbold = (FNT("Nunito SemiBold", 60), FNT("Nunito Bold", 62),
                         FNT("Nunito Bold", 66))
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    def txt(x, y, s, font, fill, anchor="la"):
        d.text((x, y), s, font=font, fill=fill, anchor=anchor)

    def node(xy, label, kind):
        x, y = xy
        if kind == "u":
            d.ellipse([x - 58, y - 58, x + 58, y + 58], fill=CARD, outline=NAVY, width=4)
            txt(x, y, label, FNT("Nunito Bold", 60), NAVY, anchor="mm")
        elif kind == "i":
            d.rounded_rectangle([x - 58, y - 58, x + 58, y + 58], 18, fill=CARD,
                                outline=NAVY, width=4)
            txt(x, y, label, FNT("Nunito Bold", 60), NAVY, anchor="mm")
        else:  # context chip
            d.rounded_rectangle([x - 66, y - 40, x + 66, y + 40], 20, fill=TEALF,
                                outline=TEAL, width=4)
            txt(x, y, label, FNT("Nunito Bold", 52), WHITE, anchor="mm")

    def blob(pts, fill, edge, w_out=196, w_in=168):
        d.line(pts + [pts[0]], fill=edge, width=w_out, joint="curve")
        for p in pts:
            d.ellipse([p[0] - w_out / 2, p[1] - w_out / 2,
                       p[0] + w_out / 2, p[1] + w_out / 2], fill=edge)
        d.polygon(pts, fill=edge)
        d.line(pts + [pts[0]], fill=fill, width=w_in, joint="curve")
        for p in pts:
            d.ellipse([p[0] - w_in / 2, p[1] - w_in / 2,
                       p[0] + w_in / 2, p[1] + w_in / 2], fill=fill)
        d.polygon(pts, fill=fill)

    def arrow(x0, y0, x1, y1, fill, wdt):
        d.line([(x0, y0), (x1, y1)], fill=fill, width=wdt)
        a = math.atan2(y1 - y0, x1 - x0)
        for s in (-1, 1):
            b = a + math.pi + s * 0.42
            d.line([(x1, y1), (x1 + 34 * math.cos(b), y1 + 34 * math.sin(b))],
                   fill=fill, width=wdt)

    # ---------------------------------------------------------- panels
    d.rounded_rectangle([60, 40, 1270, 1240], 44, fill=BG, outline=NAVY, width=4)
    d.rounded_rectangle([1330, 40, 2565, 1240], 44, fill=BG, outline=NAVY, width=4)
    txt(665, 88, "PAIRWISE GRAPH", xbold, NAVY, anchor="ma")
    txt(665, 168, "(LightGCN, HCCF, HPCF)", semi, GREY, anchor="ma")
    txt(1948, 88, "HYPERGRAPH (DyHuCoG)", xbold, NAVY, anchor="ma")

    L = {"u1": (330, 380), "u2": (330, 620), "u3": (330, 860),
         "i1": (980, 380), "i2": (980, 620), "i3": (980, 860)}
    Rpos = {"u1": (1640, 380), "u2": (1640, 620), "u3": (1640, 860),
            "i1": (2290, 380), "i2": (2290, 620), "i3": (2290, 860),
            "c1": (1965, 350)}

    # ---------------------------------------------------------- left panel
    for a, b in EDGES:
        if (a, b) in PATH or (b, a) in PATH:
            continue
        d.line([L[a], L[b]], fill=LINE, width=6)
    # one directed 2-hop message u2 -> i2 -> u1
    d.line([L["u2"], L["i2"]], fill=TEAL, width=13)
    arrow(L["i2"][0], L["i2"][1], L["u1"][0] + 82, L["u1"][1] + 33, TEAL, 13)
    for u in USERS:
        node(L[u], u, "u")
    for i in ITEMS:
        node(L[i], i, "i")
    txt(120, 1010, "Edges are observed interactions;", semi, GREY)
    txt(120, 1077, "teal: a 2-hop message, u2 - i2 - u1;", semi, GREY)
    txt(120, 1144, "every message weighs the same.", semi, GREY)

    # ---------------------------------------------------------- right panel
    for a, b in EDGES:
        d.line([Rpos[a], Rpos[b]], fill=LINE, width=4)
    blob([Rpos[n] for n in E2], GREYF, NAVY)
    blob([Rpos[n] for n in E1], TEALF, TEAL)
    for u in USERS:
        node(Rpos[u], u, "u")
    for i in ITEMS:
        node(Rpos[i], i, "i")
    node(Rpos["c1"], "c1", "c")
    txt(1965, 190, "context", semi, TEAL, anchor="ma")
    txt(1390, 1010, "A hyperedge joins many nodes at", semi, GREY)
    txt(1390, 1077, "once: users, an item, a context;", semi, GREY)
    txt(1390, 1144, "weights re-learned at each step t.", semi, GREY)

    # ---------------------------------------------------------- bottom tag
    tag = "one hyperedge joins many nodes; DyHuCoG re-weights them at every step"
    px = 62
    while px > 40:
        f = FNT("Nunito Bold", px)
        if f.getlength(tag) <= 2140:
            break
        px -= 2
    d.rounded_rectangle([165, 1290, 2460, 1414], 62, fill=TEAL)
    txt(1312, 1352, tag, FNT("Nunito Bold", px), WHITE, anchor="mm")
    print("tag font px:", px)

    img.save(out_png)
    print("wrote", out_png, img.size)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
