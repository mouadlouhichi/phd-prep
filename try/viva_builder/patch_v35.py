"""v34 -> v35: slide 12 (Graph-Based and Hypergraph Recommenders) gets an accurate figure.

The old picture drew the pairwise graph as a near-complete graph over users,
items and context (clock-tag, pin-tag, ... edges no recommender graph has)
and grouped the hypergraph blobs arbitrarily.  The new figure
(assets/slide12_graph_hypergraph.png, drawn by fig_slide12.py) shows what the
slide text claims: the bipartite user-item graph of LightGCN / HCCF / HPCF
with edges limited to observed interactions and one 2-hop message highlighted
(u2 - i2 - u1), every edge carrying the same weight; then the same nodes plus
a context node, with hyperedge e1 joining u1, u2, i2 and the context c1 and
hyperedge e2 joining u2, u3, i3, weights re-learned at every step (DyHuCoG).

Note 12 gains one spoken paragraph that walks the jury through that figure.
Nothing else on the slide or in the deck moves.
"""
import json
import os

from pptx import Presentation
from pptx.oxml.ns import qn

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "MOUAD_LOUHICHI_VIVA_40min_BeigeGreen_v34.pptx")
DST = os.path.join(HERE, "..", "MOUAD_LOUHICHI_VIVA_40min_BeigeGreen_v35.pptx")
FIG = os.path.join(HERE, "assets", "slide12_graph_hypergraph.png")

NOTE_12_ADD = (
    "The figure now contrasts the two structures directly: on the left, the bipartite user-item graph "
    "with a two-hop message highlighted, every edge carrying the same weight; on the right, hyperedges "
    "that join users, an item and a context at once, with weights that DyHuCoG re-learns at every step."
)


def main():
    prs = Presentation(SRC)
    slide = prs.slides[11]

    # --- swap the picture part in place (geometry untouched)
    pic = [sh for sh in slide.shapes if sh.shape_id == 33][0]
    rId = pic._element.blipFill.blip.get(qn("r:embed"))
    part = slide.part.related_part(rId)
    assert part.partname.ext == "png", part.partname
    part._blob = open(FIG, "rb").read()

    # --- extend the spoken note
    tf = slide.notes_slide.notes_text_frame
    tf.add_paragraph().text = NOTE_12_ADD

    prs.save(DST)

    # --- notes json + verification
    back = Presentation(DST)
    nj = {str(i): (s.notes_slide.notes_text_frame.text if s.has_notes_slide else "")
          for i, s in enumerate(back.slides, 1)}
    json.dump(nj, open(os.path.join(HERE, "notes_v35.json"), "w"), indent=1, ensure_ascii=False)

    old = Presentation(SRC)
    dnotes = [i for i, (a, b) in enumerate(zip(
        [s.notes_slide.notes_text_frame.text for s in old.slides],
        [s.notes_slide.notes_text_frame.text for s in back.slides]), 1) if a != b]
    dimg = []
    for i, (a, b) in enumerate(zip(old.slides, back.slides), 1):
        ha = [sh.image.sha1 for sh in a.shapes if sh.shape_type == 13]
        hb = [sh.image.sha1 for sh in b.shapes if sh.shape_type == 13]
        if ha != hb:
            dimg.append(i)
    dshp = [i for i, (a, b) in enumerate(zip(old.slides, back.slides), 1)
            if len(a.shapes) != len(b.shapes)]
    words = sum(len(nj[str(i)].split()) for i in range(1, 77))
    print("notes changed:", dnotes)
    print("images changed:", dimg)
    print("shape-count changed:", dshp or "none")
    print("slides:", len(back.slides))
    print("spoken words 1-76:", words, f"= {words/130:.1f} min @130, {words/120:.1f} @120")
    print("note 12 words:", len(nj["12"].split()))


if __name__ == "__main__":
    main()
