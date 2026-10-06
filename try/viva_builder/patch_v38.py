"""v37 -> v38: real paper figure on slide 12; slide 13 rebuilt slim.

Slide 12: the figure is now the thesis's own Figure 2.4 ("Graph versus
hypergraph representation", p. 38), cropped before the concatenation tail so
the comparison reads at slide scale: left the eight nodes as an ordinary graph
with its adjacency matrix W, right the hypergraph view with hyperedge groups
per data type and the incidence matrices H1..HN.  Placed 7.01 x 4.88 in
centred in the picture zone, every label inside it projects at 17 pt or
above.  A one-line grey caption names the source.  Note 12 is rewritten to
describe exactly this figure.

Slide 13: the seven-card grid looked crowded, so the four classical limits
become a row of slim pills (titles only) introduced by a grey lead-in, the
three structural limits become three airy cards (gold oval, 22 pt title,
20 pt one-line key), and the THESIS GAP bar closes the slide.  The 191-word
spoken note is untouched: it already carries everything the slide no longer
shows.
"""
import json
import os

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml.ns import qn
from pptx.util import Inches, Pt

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "MOUAD_LOUHICHI_VIVA_40min_BeigeGreen_v37.pptx")
DST = os.path.join(HERE, "..", "MOUAD_LOUHICHI_VIVA_40min_BeigeGreen_v38.pptx")
FIG = os.path.join(HERE, "assets", "slide12_graph_vs_hypergraph.png")

BLUE = RGBColor(0x44, 0x72, 0xC4)
TEALC = RGBColor(0x1F, 0x7A, 0x8C)
GOLD = RGBColor(0xEC, 0xC6, 0x65)
CREAM = RGBColor(0xF1, 0xED, 0xE6)
LAV = RGBColor(0xE7, 0xEA, 0xF3)
INK = RGBColor(0x11, 0x11, 0x11)
GREY = RGBColor(0x5A, 0x6B, 0x8C)
BANDGREY = RGBColor(0x8A, 0x83, 0x78)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)

PILLS = ["Data sparsity", "Cold-start", "Popularity bias", "No interpretability"]
CARDS = [
    ("1", "Lack of explainability",
     [("Explanations are neither ", False), ("faithful nor actionable", True), (".", False)]),
    ("2", "Difficulty of scaling",
     [("Local explanations break ", False), ("across levels and at scale", True), (".", False)]),
    ("3", "Weak integration into learning",
     [("Post-hoc", True), (" only: training never sees them.", False)]),
]
GAP = [("No ", False), ("cooperative-attribution framework", True),
       (" explains clustering faithfully, stays consistent across levels, and works as an ", False),
       ("in-training signal", True), (". ", False), ("Claim:", True),
       (" Shapley-value attribution can be that framework.", False)]

NOTE_12 = (
    "The figure comes straight from the thesis: on the left, eight nodes as an ordinary graph with its "
    "adjacency matrix W; on the right, the hypergraph view, where each hyperedge groups nodes of one "
    "data type and the incidence matrices H1 to HN concatenate into a single H. Message passing over "
    "these structures carries the collaborative signal across one, two and three hops, and DyHuCoG makes "
    "the hyperedge weights dynamic."
)


def runs(tf, items, size, color):
    for p in list(tf.paragraphs):
        p._p.getparent().remove(p._p)
    p = tf.add_paragraph()
    for text, bold in items:
        r = p.add_run()
        r.text = text
        r.font.size = Pt(size)
        r.font.bold = bold
        r.font.name = "Nunito Semi-Bold"
        r.font.color.rgb = color
    return p


def main():
    prs = Presentation(SRC)

    # ---------------- slide 12: thesis Figure 2.4, cropped
    s12 = prs.slides[11]
    pic = [sh for sh in s12.shapes if sh.shape_id == 33][0]
    rId = pic._element.blipFill.blip.get(qn("r:embed"))
    part = s12.part.related_part(rId)
    part._blob = open(FIG, "rb").read()
    w = 7.01
    pic.width = Inches(w)
    pic.height = Inches(round(w * 682 / 980, 3))
    pic.left = Inches(round(10.12 + (8.75 - w) / 2, 2))
    pic.top = Inches(4.44)
    cap = s12.shapes.add_textbox(Inches(10.12), Inches(9.36), Inches(8.76), Inches(0.32))
    r = cap.text_frame.paragraphs[0].add_run()
    r.text = "Thesis Figure 2.4: the same data as a graph (W) and as a hypergraph (H)."
    r.font.size = Pt(16)
    r.font.bold = True
    r.font.name = "Nunito Semi-Bold"
    r.font.color.rgb = BANDGREY
    s12.notes_slide.notes_text_frame.text = NOTE_12

    # ---------------- slide 13: slim rebuild
    s13 = prs.slides[12]
    for sid in range(29, 48):
        sh = [x for x in s13.shapes if x.shape_id == sid]
        if sh:
            sh[0]._element.getparent().remove(sh[0]._element)

    lead = s13.shapes.add_textbox(Inches(1.12), Inches(3.34), Inches(5.70), Inches(0.45))
    r = lead.text_frame.paragraphs[0].add_run()
    r.text = "Classical limits of recommender systems:"
    r.font.size = Pt(18)
    r.font.bold = True
    r.font.name = "Nunito Semi-Bold"
    r.font.color.rgb = GREY
    for k, label in enumerate(PILLS):
        x = 7.00 + k * 2.9825
        pill = s13.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(3.28),
                                    Inches(2.8575), Inches(0.68))
        pill.adjustments[0] = 0.5
        pill.fill.solid()
        pill.fill.fore_color.rgb = TEALC if k == 3 else BLUE
        pill.line.fill.background()
        pill.shadow.inherit = False
        tf = pill.text_frame
        tf.margin_left = tf.margin_right = Inches(0.05)
        tf.margin_top = tf.margin_bottom = 0
        tf.word_wrap = False
        r = tf.paragraphs[0].add_run()
        r.text = label
        r.font.size = Pt(18)
        r.font.bold = True
        r.font.name = "Nunito Semi-Bold"
        r.font.color.rgb = WHITE
        tf.paragraphs[0].alignment = 2

    lead2 = s13.shapes.add_textbox(Inches(1.12), Inches(4.38), Inches(8.50), Inches(0.45))
    r = lead2.text_frame.paragraphs[0].add_run()
    r.text = "Three structural limits this thesis addresses:"
    r.font.size = Pt(18)
    r.font.bold = True
    r.font.name = "Nunito Semi-Bold"
    r.font.color.rgb = GREY
    for k, (num, title, key) in enumerate(CARDS):
        x = 1.12 + k * 6.035
        card = s13.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(4.95),
                                    Inches(5.68), Inches(2.65))
        card.adjustments[0] = 0.05
        card.fill.solid()
        card.fill.fore_color.rgb = BLUE
        card.line.fill.background()
        card.shadow.inherit = False
        ov = s13.shapes.add_shape(MSO_SHAPE.OVAL, Inches(x + 0.35), Inches(5.28),
                                  Inches(0.62), Inches(0.62))
        ov.fill.solid()
        ov.fill.fore_color.rgb = GOLD
        ov.line.fill.background()
        ov.shadow.inherit = False
        r = ov.text_frame.paragraphs[0].add_run()
        r.text = num
        r.font.size = Pt(20)
        r.font.bold = True
        r.font.name = "Nunito Ultra-Bold"
        r.font.color.rgb = INK
        ov.text_frame.paragraphs[0].alignment = 2
        ov.text_frame.vertical_anchor = 3
        for m in ("left", "right", "top", "bottom"):
            setattr(ov.text_frame, f"margin_{m}", 0)
        tb = s13.shapes.add_textbox(Inches(x + 1.15), Inches(5.31), Inches(4.35), Inches(0.80))
        r = tb.text_frame.paragraphs[0].add_run()
        r.text = title
        r.font.size = Pt(22)
        r.font.bold = True
        r.font.name = "Nunito Ultra-Bold"
        r.font.color.rgb = WHITE
        kb = s13.shapes.add_textbox(Inches(x + 0.35), Inches(6.30), Inches(5.00), Inches(1.15))
        runs(kb.text_frame, key, 20, CREAM)

    bar = s13.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.12), Inches(8.00),
                               Inches(17.75), Inches(1.68))
    bar.adjustments[0] = 0.08
    bar.fill.solid()
    bar.fill.fore_color.rgb = LAV
    bar.line.fill.background()
    bar.shadow.inherit = False
    chip = s13.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.62), Inches(7.77),
                                Inches(2.55), Inches(0.48))
    chip.adjustments[0] = 0.35
    chip.fill.solid()
    chip.fill.fore_color.rgb = BLUE
    chip.line.fill.background()
    chip.shadow.inherit = False
    r = chip.text_frame.paragraphs[0].add_run()
    r.text = "THESIS GAP"
    r.font.size = Pt(16)
    r.font.bold = True
    r.font.name = "Nunito Ultra-Bold"
    r.font.color.rgb = WHITE
    gt = s13.shapes.add_textbox(Inches(1.68), Inches(8.32), Inches(16.70), Inches(1.20))
    runs(gt.text_frame, GAP, 18, INK)

    prs.save(DST)

    back = Presentation(DST)
    nj = {str(i): (sl.notes_slide.notes_text_frame.text if sl.has_notes_slide else "")
          for i, sl in enumerate(back.slides, 1)}
    json.dump(nj, open(os.path.join(HERE, "notes_v38.json"), "w"), indent=1, ensure_ascii=False)
    old = Presentation(SRC)
    dnotes = [i for i, (a, b) in enumerate(zip(
        [s.notes_slide.notes_text_frame.text for s in old.slides],
        [s.notes_slide.notes_text_frame.text for s in back.slides]), 1) if a != b]
    dimg = [i for i, (a, b) in enumerate(zip(old.slides, back.slides), 1)
            if [sh.image.sha1 for sh in a.shapes if sh.shape_type == 13] !=
               [sh.image.sha1 for sh in b.shapes if sh.shape_type == 13]]
    dshp = [i for i, (a, b) in enumerate(zip(old.slides, back.slides), 1)
            if len(a.shapes) != len(b.shapes)]
    words = sum(len(nj[str(i)].split()) for i in range(1, 76))
    print("notes changed:", dnotes, "| images:", dimg, "| shapes:", dshp)
    print("slides:", len(back.slides))
    print("spoken words 1-75:", words, f"= {words/130:.1f} min @130, {words/120:.1f} @120")
    print("note 12 words:", len(nj["12"].split()), "| note 13 words:", len(nj["13"].split()))


if __name__ == "__main__":
    main()
