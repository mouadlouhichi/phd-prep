"""v35 -> v36: merge slides 13 and 14 into one problem-statement slide.

Slide 13 (four classical limits + a clustering panel) and slide 14 (three
structural limits + the thesis gap) told one story in two passes.  The merged
slide keeps every piece of content in three rows:

  row 1  the four classical limits (slide 13 cards, same blue/teal style);
  row 2  the three structural limits (slide 14 cards, gold-oval numbers);
  row 3  the THESIS GAP bar (slide 14 gap text, verbatim).

The citation band becomes the union of both bands ([21], [23] with its two
works, [24]), in the v29 full form, falling back to the v29 compact form if
the full form would need more than three lines.  Slide 14 is deleted and every
later page number is decremented, so the deck goes from 79 to 78 slides.

The spoken note merges the two notes without repeating itself (103 words).
"""
import io
import json
import os
import zipfile

from fontTools.ttLib import TTFont
from PIL import ImageFont
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml.ns import qn
from pptx.util import Emu, Inches, Pt

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "MOUAD_LOUHICHI_VIVA_40min_BeigeGreen_v35.pptx")
DST = os.path.join(HERE, "..", "MOUAD_LOUHICHI_VIVA_40min_BeigeGreen_v36.pptx")

BLUE = RGBColor(0x44, 0x72, 0xC4)
TEALC = RGBColor(0x1F, 0x7A, 0x8C)
GOLD = RGBColor(0xEC, 0xC6, 0x65)
CREAM = RGBColor(0xF1, 0xED, 0xE6)
LAV = RGBColor(0xE7, 0xEA, 0xF3)
INK = RGBColor(0x11, 0x11, 0x11)
NAVY = RGBColor(0x11, 0x11, 0x11)

ROW1 = [
    ("01", "Data sparsity & scalability",
     [("The user-item matrix is almost empty, so there is very little signal to learn from.", False)], BLUE),
    ("02", "Cold-start",
     [("New users and items are at a disadvantage: no history to learn from.", False)], BLUE),
    ("03", "Popularity bias & lack of diversity",
     [("Exposure leads to interaction, which leads to more exposure: a filter-bubble loop.", False)], BLUE),
    ("04", "Absence of interpretability",
     [("The most basic limit, and the one this thesis targets.", False)], TEALC),
]
ROW2 = [
    ("1", "Lack of explainability",
     [("Complex models are still hard to explain in a way that is ", False),
      ("faithful and actionable", True), (".", False)]),
    ("2", "Difficulty of scaling",
     [("Local explanations do not carry over to ", False),
      ("multi-level structures or large datasets", True),
      (": a method that works on a toy partition may break on hundreds of thousands of nested records.", False)]),
    ("3", "Weak integration into learning",
     [("Most explanations stay ", False), ("post-hoc", True),
      (": they do not shape how the model learns, nor the ", False),
      ("accuracy / diversity / context trade-off", True), (".", False)]),
]
GAP = [("The literature still lacks ", False), ("one cooperative-attribution framework", True),
       (" that explains clustering faithfully, stays consistent across levels, and then works as an ", False),
       ("in-training signal", True), (" in recommendation. ", False), ("Claim:", True),
       (" Shapley-value attribution can be that framework.", False)]

NOTE_13 = (
    "From this evolution, four limits appear: data sparsity, cold-start, popularity bias, and above all "
    "the absence of interpretability. For clustering specifically, methods give a local or a global "
    "explanation, not both, and rarely stay consistent across levels of detail. Three structural "
    "limitations follow: complex models are hard to explain faithfully and actionably; local explanations "
    "do not scale to multi-level structures; and most explanations stay post-hoc, so they never shape how "
    "the model learns. The gap bar closes the slide: the literature still lacks one cooperative-attribution "
    "framework that explains clustering faithfully, stays consistent across levels, and then works as an "
    "in-training signal in recommendation."
)

B21 = ("[21] Zhang, Y. & Chen, X. Explainable Recommendation: A Survey and New Perspectives. "
       "Foundations and Trends in IR 14(1), 1–101 (2020).")
B23 = ("[23] Zhu, Z. et al. Popularity Bias in Dynamic Recommendation. KDD, 2439–2449 (2021).  ·  "
       "Hurley, N. & Zhang, M. Novelty and Diversity in Top-N Recommendation. ACM TOIT 10(4) (2011).")
B24 = ("[24] Arrieta, A. B. et al. Explainable Artificial Intelligence (XAI): Concepts, Taxonomies, "
       "Opportunities and Challenges. Information Fusion 58, 82–115 (2020).")
C21 = "[21] Zhang, Y. & Chen, X. Foundations and Trends in IR 14(1), 1–101 (2020)."
C23 = "[23] Zhu, Z. et al. KDD, 2439–2449 (2021).  ·  Hurley, N. & Zhang, M. ACM TOIT 10(4) (2011)."
C24 = "[24] Arrieta, A. B. et al. Information Fusion 58, 82–115 (2020)."
SEP3 = "   "


def raw_fonts(deck):
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


def band_lines(text, raw):
    f = ImageFont.truetype(io.BytesIO(raw["Nunito SemiBold"]), 56)  # 14 pt at 4 px/pt
    width = 17.76 * 72 * 4 * 0.97
    lines, cur = 1, ""
    for w in text.split(" "):
        t = (cur + " " + w).strip()
        if f.getlength(t) > width and cur:
            lines += 1
            cur = w
        else:
            cur = t
    return lines


def set_runs(tf, paras, wrap=None):
    """paras: list of lists of (text, size_pt, color, bold, face)."""
    tf.word_wrap = True
    for pi, para in enumerate(paras):
        p = tf.paragraphs[0] if pi == 0 else tf.add_paragraph()
        for (text, size, color, bold, face) in para:
            r = p.add_run()
            r.text = text
            r.font.size = Pt(size)
            r.font.color.rgb = color
            r.font.bold = bold
            r.font.name = face


def main():
    raw = raw_fonts(SRC)
    prs = Presentation(SRC)
    s = prs.slides[12]

    # ---- headline + icon
    hl = [sh for sh in s.shapes if sh.shape_id == 24][0]
    hl.text_frame.paragraphs[0].runs[0].text = "Limitations & Problem Statement"
    hl.text_frame.paragraphs[0].runs[0].font.size = Pt(46)
    hl.height = Inches(0.80)
    f = ImageFont.truetype(io.BytesIO(raw["Roca Two Bold"]), 46 * 4)
    w_in = f.getlength("Limitations & Problem Statement") / 4 / 72
    icon = [sh for sh in s.shapes if sh.shape_id == 25][0]
    icon.left = Inches(round(1.12 + w_in + 0.25, 2))

    # ---- clear the old content zone
    for sid in (29, 30, 31, 32, 33, 34, 35):
        sh = [x for x in s.shapes if x.shape_id == sid][0]
        sh._element.getparent().remove(sh._element)

    # ---- row 1: four classical limits
    for k, (num, title, body, fill) in enumerate(ROW1):
        x = 1.12 + k * 4.52
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(3.30),
                                  Inches(4.21), Inches(2.20))
        card.adjustments[0] = 0.06
        card.fill.solid()
        card.fill.fore_color.rgb = fill
        card.line.fill.background()
        card.shadow.inherit = False
        tf = card.text_frame
        tf.margin_left = Inches(0.22)
        tf.margin_right = Inches(0.18)
        tf.margin_top = Inches(0.14)
        numcol = GOLD if fill == BLUE else RGBColor(0xFF, 0xFF, 0xFF)
        set_runs(tf, [
            [(num, 20, numcol, True, "Nunito Ultra-Bold")],
            [(title, 17, RGBColor(0xFF, 0xFF, 0xFF), True, "Nunito Ultra-Bold")],
            [(t, 16, CREAM, b, "Nunito Semi-Bold") for t, b in body],
        ])

    # ---- row 2: three structural limits
    for k, (num, title, body) in enumerate(ROW2):
        x = 1.12 + k * 6.035
        card = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(5.80),
                                  Inches(5.68), Inches(2.30))
        card.adjustments[0] = 0.05
        card.fill.solid()
        card.fill.fore_color.rgb = BLUE
        card.line.fill.background()
        card.shadow.inherit = False
        ov = s.shapes.add_shape(MSO_SHAPE.OVAL, Inches(x + 0.35), Inches(6.08),
                                Inches(0.62), Inches(0.62))
        ov.fill.solid()
        ov.fill.fore_color.rgb = GOLD
        ov.line.fill.background()
        ov.shadow.inherit = False
        set_runs(ov.text_frame, [[(num, 20, INK, True, "Nunito Ultra-Bold")]])
        ov.text_frame.paragraphs[0].alignment = 2  # centre
        ov.text_frame.vertical_anchor = 3  # middle
        ov.text_frame.margin_left = 0
        ov.text_frame.margin_right = 0
        ov.text_frame.margin_top = 0
        ov.text_frame.margin_bottom = 0
        tb = s.shapes.add_textbox(Inches(x + 1.12), Inches(6.14), Inches(4.40), Inches(0.50))
        set_runs(tb.text_frame, [[(title, 19, RGBColor(0xFF, 0xFF, 0xFF), True, "Nunito Ultra-Bold")]])
        bb = s.shapes.add_textbox(Inches(x + 0.35), Inches(6.82), Inches(5.00), Inches(1.15))
        set_runs(bb.text_frame, [[(t, 16, CREAM, b, "Nunito Semi-Bold") for t, b in body]])

    # ---- row 3: thesis gap bar
    bar = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.12), Inches(8.35),
                             Inches(17.75), Inches(1.33))
    bar.adjustments[0] = 0.10
    bar.fill.solid()
    bar.fill.fore_color.rgb = LAV
    bar.line.fill.background()
    bar.shadow.inherit = False
    chip = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.62), Inches(8.12),
                              Inches(2.55), Inches(0.48))
    chip.adjustments[0] = 0.35
    chip.fill.solid()
    chip.fill.fore_color.rgb = BLUE
    chip.line.fill.background()
    chip.shadow.inherit = False
    set_runs(chip.text_frame, [[("THESIS GAP", 16, RGBColor(0xFF, 0xFF, 0xFF), True,
                                 "Nunito Ultra-Bold")]])
    gt = s.shapes.add_textbox(Inches(1.68), Inches(8.66), Inches(16.70), Inches(0.95))
    set_runs(gt.text_frame, [[(t, 16, INK, b, "Nunito Semi-Bold") for t, b in GAP]])

    # ---- band: union of both slides, v29 geometry
    full = SEP3.join([B21, B23, B24])
    n = band_lines(full, raw)
    text = full if n <= 3 else SEP3.join([C21, C23, C24])
    if n > 3:
        n = band_lines(text, raw)
    band = [sh for sh in s.shapes if sh.shape_id == 6][0]
    strip = [sh for sh in s.shapes if sh.shape_id == 5][0]
    top = {1: 10.24, 2: 10.01, 3: 9.77}[n]
    band.top = Inches(top)
    band.height = Inches(round(10.54 - top, 2))
    strip.top = Inches(round(top - 0.04, 2))
    strip.height = Inches(round(10.54 - top + 0.08, 2))
    btf = band.text_frame
    btf.clear()
    r = btf.paragraphs[0].add_run()
    r.text = text
    r.font.size = Pt(14)
    r.font.color.rgb = RGBColor(0x8A, 0x83, 0x78)
    r.font.bold = True
    r.font.name = "Nunito Semi-Bold"
    from pptx.util import Emu as _E
    btf.paragraphs[0].line_spacing = _E(Pt(17).emu)
    print("band lines:", n, "compact:" , n != band_lines(full, raw) or text != full)

    # ---- merged note
    s.notes_slide.notes_text_frame.text = NOTE_13

    # ---- delete slide 14
    sldIdLst = prs.slides._sldIdLst
    ids = list(sldIdLst)
    victim = ids[13]
    rId = victim.get(qn("r:id"))
    sldIdLst.remove(victim)
    prs.part.drop_rel(rId)

    # ---- renumber every page number
    for i, sl in enumerate(prs.slides, 1):
        for sh in sl.shapes:
            if sh.name == "TextBox 7" and sh.has_text_frame:
                sh.text_frame.paragraphs[0].runs[0].text = str(i)

    prs.save(DST)

    back = Presentation(DST)
    nj = {str(i): (sl.notes_slide.notes_text_frame.text if sl.has_notes_slide else "")
          for i, sl in enumerate(back.slides, 1)}
    json.dump(nj, open(os.path.join(HERE, "notes_v36.json"), "w"), indent=1, ensure_ascii=False)
    words = sum(len(nj[str(i)].split()) for i in range(1, 76))
    print("slides:", len(back.slides))
    print("spoken words 1-75:", words, f"= {words/130:.1f} min @130, {words/120:.1f} @120")
    print("note 13 words:", len(nj["13"].split()))
    nums = []
    for i, sl in enumerate(back.slides, 1):
        for sh in sl.shapes:
            if sh.name == "TextBox 7" and sh.has_text_frame:
                nums.append((i, sh.text_frame.text))
    bad = [t for i, t in nums if str(i) != t]
    print("page numbers ok:", not bad, bad[:5])


if __name__ == "__main__":
    main()
