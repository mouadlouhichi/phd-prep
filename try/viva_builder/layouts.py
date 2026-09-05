"""Slide-level layout helpers built on top of tpl.py (template design system)."""
import copy
import re

from tpl import *  # noqa
import mathkit

UNI = "Mohammed V University in Rabat  ·  ENSIAS"
VIVA = "PhD Viva  ·  Mouad LOUHICHI"
SHORT_TITLE = "Cooperative Game Theory for Explainable AI in Recommendation Systems  —  A Shapley Framework for Actionable Insight"

L = MARGIN_L
R = MARGIN_R
W = CONTENT_W
CT = emu(3.72)      # content top when a tab strip is present
CT2 = emu(3.05)     # content top without tabs
CB = emu(10.38)     # content bottom
GUTTER = emu(0.3)
MUTED = "8A8378"

ACCENT_CYCLE = ["sparkle_y", "asterisk_o", "flower_y", "fan_y", "sparkle_o", "dots_y",
                "v_o", "half_y", "trident_y", "comb_y", "flower_o", "asterisk_y"]


class Ctx:
    def __init__(self, deck):
        self.deck = deck
        self.n = 0
        self.acc = 0

    def next_accent(self):
        k = ACCENT_CYCLE[self.acc % len(ACCENT_CYCLE)]
        self.acc += 1
        return k


# --------------------------------------------------------------------------
# Rich text helpers
# --------------------------------------------------------------------------
_MD = re.compile(r"(\*\*.+?\*\*)")
_SS = re.compile(r"(\^\{[^{}]*\}|_\{[^{}]*\})")
FIT_REPORT = []


def _ss_runs(text, **kw):
    """Expand ^{...} / _{...} into baseline-shifted runs."""
    out = []
    for part in _SS.split(text):
        if not part:
            continue
        if part.startswith("^{") and part.endswith("}"):
            out.append(Run(part[2:-1], baseline=30000, **kw))
        elif part.startswith("_{") and part.endswith("}"):
            out.append(Run(part[2:-1], baseline=-25000, **kw))
        else:
            out.append(Run(part, **kw))
    return out


def md_runs(text, size=22, color=INK, font="body", bold_font="bold", spc=None):
    """'plain **bold** x^{2} y_{i}' -> runs (bold + real sub/superscripts)."""
    runs = []
    for part in _MD.split(text):
        if not part:
            continue
        if part.startswith("**") and part.endswith("**"):
            runs += _ss_runs(part[2:-2], font=bold_font, size=size, color=color, spc=spc)
        else:
            runs += _ss_runs(part, font=font, size=size, color=color, spc=spc)
    return runs


def P(text, size=22, color=INK, font="body", align="l", lnspc=None, spcbef=0, bold_font="bold"):
    return Para(md_runs(text, size=size, color=color, font=font, bold_font=bold_font), align=align, lnspc=lnspc, spcbef=spcbef)


def H(text, size=24, color=INK, font="xbold", align="l", spcbef=0):
    return Para(_ss_runs(text, font=font, size=size, color=color), align=align, lnspc=size * 1.25, spcbef=spcbef)


def bullets(items, size=22, color=INK, c0=ORANGE, c1=None, gap0=9, gap1=3, font="body", pitch=None):
    """items: str | (level, str). Level-0 bullet '•' (c0), level-1 '–' (c1)."""
    if c1 is None:
        c1 = GREEN if color == INK else color
    out = []
    first = True
    for it in items:
        lvl, text = (0, it) if isinstance(it, str) else it
        sz = size if lvl == 0 else size - 2
        auto_pitch = sz * (1.48 if _SS.search(text) else 1.40)     # extra leading for sub/superscripts
        para = Para(md_runs(text, size=sz, color=color, font=font), align="l",
                    lnspc=pitch or auto_pitch, spcbef=0 if first else (gap0 if lvl == 0 else gap1),
                    level=lvl, bullet="•" if lvl == 0 else "–", bullet_color=c0 if lvl == 0 else c1)
        out.append(para)
        first = False
    return out


def _scaled(paras, f):
    out = []
    for p in paras:
        q = copy.deepcopy(p)
        for r in q.runs:
            r.size = r.size * f
        if q.lnspc:
            q.lnspc = q.lnspc * f
        q.spcbef = q.spcbef * f
        out.append(q)
    return out


def shrink_to_fit(paras, w, h, min_scale=0.62, insets=(0, 0, 0, 0), safety=1.05):
    f = 1.0
    h_pt = h / IN * 72
    while f > min_scale:
        test = _scaled(paras, f)
        if paras_height_pt(test, w, insets) * safety <= h_pt:
            return test, f
        f -= 0.03
    return _scaled(paras, min_scale), min_scale


def fit_textbox(slide, x, y, w, h, paras, anchor="t", insets=(0, 0, 0, 0), min_scale=0.62, name=None):
    fitted, f = shrink_to_fit(paras, w, h, min_scale=min_scale, insets=insets)
    if f < 0.86:
        FIT_REPORT.append((len(slide.part.package.presentation_part.presentation.slides._sldIdLst), round(f, 2), (paras[0].text[:40] if paras else "")))
    tb = textbox(slide, x, y, w, h, fitted, anchor=anchor, insets=insets, name=name)
    return tb, f


# --------------------------------------------------------------------------
# Equations (native PowerPoint math, see mathkit.py)
# --------------------------------------------------------------------------
def equation(slide, x, y, w, h, tex, size=24, color=INK, align="ctr", anchor="ctr", name="Equation"):
    """Typeset `tex` as a real PowerPoint equation centred in the (x, y, w, h) EMU box.
    The font size is reduced (never below 11 pt) until the equation fits the box with
    comfortable leading above and below."""
    fitted = mathkit.fit_size(tex, size, w / mathkit.PT, h / mathkit.PT, min_size=11)
    if fitted < size * 0.8:
        FIT_REPORT.append((len(slide.part.package.presentation_part.presentation.slides._sldIdLst), round(fitted / size, 2), "EQ " + tex[:40]))
    return mathkit.add_equation(slide, x, y, w, h, tex, size_pt=fitted, color=color, align=align, anchor=anchor, name=name)


def eq_height(tex, size):
    """Comfortable box height (EMU) for an equation at `size` pt."""
    return emu(mathkit.box_size(tex, size)[1] / 72.0)


def eq_width(tex, size):
    return emu(mathkit.box_size(tex, size)[0] / 72.0)


# --------------------------------------------------------------------------
# Chrome
# --------------------------------------------------------------------------
def chrome(slide, n, dark=False):
    col = WHITE if dark else INK
    textbox(slide, L, HEADER_Y, emu(8), emu(0.4), [Para([Run(UNI, font="bold", size=20, color=col, spc=-1.1)], lnspc=28)])
    textbox(slide, R - emu(8), HEADER_Y, emu(8), emu(0.4), [Para([Run(VIVA, font="bold", size=20, color=col, spc=-1.1)], align="r", lnspc=28)])
    # footer
    textbox(slide, L, emu(10.66), emu(14), emu(0.3), [Para([Run(SHORT_TITLE, font="bold", size=13, color=MUTED if not dark else "CFDAD6")], lnspc=16)])
    textbox(slide, R - emu(1.2), emu(10.6), emu(1.2), emu(0.36), [Para([Run(f"{n:02d}", font="xbold", size=18, color=col)], align="r", lnspc=22)])


def title_block(ctx, slide, headline, eyebrow=None, tabs=None, active=None, accent_key=None):
    """Eyebrow (section), Roca headline, optional tab pills. Returns content-top y."""
    y = emu(1.52)
    if eyebrow:
        textbox(slide, L, y, W, emu(0.36), [Para([Run(eyebrow.upper(), font="xbold", size=15, color=ORANGE, spc=1.6)], lnspc=20)])
        y += emu(0.36)
    else:
        y += emu(0.1)
    # headline: auto-shrink to one line within ~W - accent space
    size = 46
    max_w = (W - emu(1.0)) / IN * 72
    while size > 28 and text_width_pt(headline, "title", size, -0.05 * size) > max_w:
        size -= 2
    th = emu(size / 72 * 1.25)
    textbox(slide, L, y, W, th, [Para([Run(headline, font="title", size=size, color=INK)], lnspc=size * 1.1)])
    tw = text_width_pt(headline, "title", size, -0.05 * size) / 72 * IN
    accent(slide, accent_key or ctx.next_accent(), L + tw + emu(0.28), y - emu(0.05), emu(0.5))
    y += th + emu(0.12)
    if tabs:
        x = L
        for t in tabs:
            shp, w = pill(slide, x, y, t, active=(t == active), h=emu(0.46), size=18, pad=0.3)
            x += w + emu(0.14)
        y += emu(0.46)
    return y


def content_slide(ctx, headline, eyebrow=None, tabs=None, active=None, notes=None):
    ctx.n += 1
    s = ctx.deck.new_slide()
    chrome(s, ctx.n)
    top = title_block(ctx, s, headline, eyebrow=eyebrow, tabs=tabs, active=active)
    set_notes(s, notes)
    return s, top + emu(0.42)


def set_notes(slide, notes):
    if notes:
        slide.notes_slide.notes_text_frame.text = notes


# --------------------------------------------------------------------------
# Section slide (template slide 4 style)
# --------------------------------------------------------------------------
def section_slide(ctx, number, title, subtitle, columns, accent_key="arrow_black", notes=None):
    ctx.n += 1
    s = ctx.deck.new_slide()
    chrome(s, ctx.n)
    # title
    size = 150
    max_w = (W - emu(1.6)) / IN * 72
    while size > 60 and text_width_pt(title, "title", size, -0.058 * size) > max_w:
        size -= 6
    ty = emu(2.55)
    textbox(s, L, ty, W - emu(1.5), emu(size / 72 * 1.2), [Para([Run(title, font="title", size=size, color=INK, spc=-0.058 * size)], lnspc=size * 1.02)])
    tw = text_width_pt(title, "title", size, -0.058 * size) / 72 * IN
    # numbered yellow badge with the template's black arrow
    d = emu(1.1)
    bx = min(L + tw + emu(0.45), R - d)
    by = ty + emu(size / 72 * 0.5) - d / 2 + emu(0.15)
    ellipse(s, bx, by, d, d, fill=YELLOW)
    textbox(s, bx, by, d, d, [Para([Run(number, font="xbold", size=30, color=INK)], align="ctr", lnspc=34)], anchor="ctr")
    # subtitle
    sy = ty + emu(size / 72 * 1.12)
    textbox(s, L, sy, W, emu(0.7), [Para([Run(subtitle, font="bold", size=30, color=GREEN, spc=-1.5)], lnspc=38)])
    # green band
    band_y = emu(5.95)
    rect(s, 0, band_y, SLIDE_W, SLIDE_H - band_y, fill=GREEN)
    n = len(columns)
    gap = emu(0.45)
    cw = (W - gap * (n - 1)) / n
    for i, (head, body) in enumerate(columns):
        x = L + i * (cw + gap)
        textbox(s, x, band_y + emu(0.55), cw, emu(0.5), [Para([Run(head, font="xbold", size=23, color=YELLOW)], lnspc=28)])
        line(s, x, band_y + emu(1.12), x + emu(0.7), band_y + emu(1.12), color=YELLOW, w=2.5)
        fit_textbox(s, x, band_y + emu(1.35), cw, emu(3.4), [P(body, size=21, color=WHITE)], min_scale=0.75)
    set_notes(s, notes)
    return s


# --------------------------------------------------------------------------
# Cards & diagram primitives
# --------------------------------------------------------------------------
def card(slide, x, y, w, h, label=None, paras=None, fill=GREEN, label_fill=WHITE, label_color=GREEN,
         text_color=WHITE, pad=None, label_size=22, anchor="t", min_scale=0.62, radius=None, line_color=None):
    shp = rrect(slide, x, y, w, h, fill=fill, line=line_color, radius=radius if radius else emu(0.34))
    if pad is None:
        pad = (0.45, 0.62 if label else 0.4, 0.45, 0.35)
    if label:
        lh = emu(0.48)
        pill(slide, x + emu(0.5), y - lh / 2 - emu(0.02), label, active=True, h=lh, size=label_size, pad=0.36,
             fill=label_fill, text_color=label_color, line_color=label_fill)
    if paras:
        fit_textbox(slide, x + emu(pad[0]), y + emu(pad[1]), w - emu(pad[0] + pad[2]), h - emu(pad[1] + pad[3]),
                    paras, anchor=anchor, min_scale=min_scale)
    return shp


def light_card(slide, x, y, w, h, label=None, paras=None, **kw):
    return card(slide, x, y, w, h, label=label, paras=paras, fill=TINT, label_fill=GREEN, label_color=WHITE,
                text_color=INK, **kw)


def chip(slide, x, y, w, h, text, fill=GREEN, color=WHITE, size=19, font="bold", sub=None, sub_size=15, sub_color=None, radius=None, line_color=None):
    shp = rrect(slide, x, y, w, h, fill=fill, line=line_color, radius=radius if radius is not None else emu(0.22))
    paras = [Para([Run(text, font=font, size=size, color=color)], align="ctr", lnspc=size * 1.15)]
    if sub:
        paras.append(Para([Run(sub, font="body", size=sub_size, color=sub_color or color)], align="ctr", lnspc=sub_size * 1.2, spcbef=3))
    fitted, _ = shrink_to_fit(paras, w - emu(0.2), h - emu(0.1), min_scale=0.6)
    shape_text(shp, fitted, anchor="ctr", insets=(emu(0.1), emu(0.05), emu(0.1), emu(0.05)))
    return shp


def arrow(slide, x1, y1, x2, y2, color=GREEN, w=2.5):
    return line(slide, x1, y1, x2, y2, color=color, w=w, arrow=True)


def numbered_rows(slide, x, y, w, rows, num_fill=YELLOW, num_color=INK, size=21, gap=0.16, min_h=0.62, badge_d=0.5, text_color=INK, label_font="bold"):
    """rows: list of (num, text). Returns bottom y."""
    cy = y
    for num, text in rows:
        paras = [P(text, size=size, color=text_color)]
        tw = w - emu(badge_d + 0.35)
        hpt = paras_height_pt(paras, tw) * 1.04
        h = max(emu(min_h), emu(hpt / 72))
        badge(slide, x, cy + (h - emu(badge_d)) / 2, emu(badge_d), num, fill=num_fill, color=num_color, size=17, font=label_font)
        textbox(slide, x + emu(badge_d + 0.3), cy, tw, h, paras, anchor="ctr")
        cy += h + emu(gap)
    return cy


def kpi(slide, x, y, w, h, value, label, fill=GREEN, vcolor=YELLOW, lcolor=WHITE, vsize=40, lsize=17):
    shp = rrect(slide, x, y, w, h, fill=fill, radius=emu(0.3))
    paras = [Para(_ss_runs(value, font="xbold", size=vsize, color=vcolor), align="ctr", lnspc=vsize * 1.1),
             Para(md_runs(label, size=lsize, color=lcolor), align="ctr", lnspc=lsize * 1.25, spcbef=4)]
    fitted, _ = shrink_to_fit(paras, w - emu(0.3), h - emu(0.2), min_scale=0.6)
    shape_text(shp, fitted, anchor="ctr", insets=(emu(0.15), emu(0.1), emu(0.15), emu(0.1)))
    return shp


def grid(n, cols, x, y, w, h, gap=GUTTER, vgap=None):
    """Return list of (x, y, w, h) cells for n items in a grid."""
    if vgap is None:
        vgap = gap
    rows = (n + cols - 1) // cols
    cw = (w - gap * (cols - 1)) / cols
    ch = (h - vgap * (rows - 1)) / rows
    cells = []
    for i in range(n):
        r, c = divmod(i, cols)
        cells.append((x + c * (cw + gap), y + r * (ch + vgap), cw, ch))
    return cells
