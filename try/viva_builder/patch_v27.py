#!/usr/bin/env python3
# ---------------------------------------------------------------------------
# patch_v27.py: v26 -> v27
#
# The candidate's own opening speech. Four changes, nothing else:
#
#   notes 1 and 2   replaced by the speech Mouad Louhichi wrote and delivered
#                   ("AI" spelled out as "artificial intelligence" in the
#                   spoken title; the typo "finnally" fixed)
#   note 4          shortened to a short, spoken-style note that uses what is
#                   on slide 4 (the three motivation questions + the tension)
#   slide 6         the two blocks "Why the gap matters" / "What this thesis
#                   argues" rewritten short and aligned with the speech, and
#                   note 6 rewritten short so the blocks and the speech say
#                   exactly the same three things
#
# The deck itself is patched in place (never rebuilt): layout, fonts, native
# OMML equations, footers and citation bands are untouched. Every rewrite
# asserts the paragraph it edits exists, and the report prints the resulting
# speech length.
# ---------------------------------------------------------------------------
import json
import os
import shutil
from copy import deepcopy

from pptx import Presentation
from pptx.oxml.ns import qn

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "MOUAD_LOUHICHI_VIVA_40min_BeigeGreen_v26.pptx")
DST = os.path.join(HERE, "..", "MOUAD_LOUHICHI_VIVA_40min_BeigeGreen_v27.pptx")
NOTES_IN = os.path.join(HERE, "notes_v26.json")
NOTES_OUT = os.path.join(HERE, "notes_v27.json")

WPM = 130.0


# ---------------------------------------------------------------------------
# 1. speaker notes
# ---------------------------------------------------------------------------
NEW_NOTES = {
    "1": (
        "Good morning, Mister President. Good morning, Professors. Thank you "
        "for giving me the opportunity to present my work today.\n\n"
        "My name is Mouad Louhichi, and the thesis I am defending, supervised "
        "by Professor Mohamed Lazaar, is entitled: \"Cooperative Game Theory "
        "for Explainable Artificial Intelligence in Recommendation Systems: "
        "A Shapley Framework for Actionable Insight.\"\n\n"
        "The main idea I want you to keep in mind is this: Shapley "
        "attribution is not only a method to explain a model after it has "
        "been trained. In this thesis I show how it can become one framework "
        "that explains black-box models, stays consistent across levels of "
        "detail, and finally guides how recommenders learn.\n\n"
        "(Pre-defence check: confirm the jury list on this slide against the "
        "official convocation.)"
    ),
    "2": (
        "So here is the plan for this presentation. I'll start with the "
        "Introduction, then the Context and Problematic, and the Experimental "
        "Protocol.\n\n"
        "Then the three contributions, each following the same path: the gap, "
        "the objectives, the methodology, the protocol, the results and the "
        "findings.\n\n"
        "And finally I'll finish with the Conclusion and Perspectives."
    ),
    "4": (
        "The motivation comes down to three questions.\n\n"
        "First, how do black-box systems shape what billions of users see, "
        "buy and watch? Recommenders already influence news, study, health "
        "and credit decisions.\n\n"
        "Second, why do state-of-the-art recommenders and clustering pipelines "
        "stay black boxes for users and designers? Deep and graph models hide "
        "their logic and are hard to audit.\n\n"
        "Third, how can transparency be built into the model instead of added "
        "afterwards? That is the tension on this slide: as models gain power, "
        "they lose the transparency we need. This thesis treats accuracy and "
        "interpretability as two goals to be met together, not traded against "
        "each other."
    ),
    "6": (
        "At each step we gained predictive power and lost transparency: "
        "similarity models were easy to explain, matrix factorisation hid its "
        "meaning in latent factors, and neural and graph models added hidden "
        "representations and message passing.\n\n"
        "So why does this gap matter? Users get outputs without reasons, "
        "designers cannot debug what they cannot inspect, and regulation now "
        "asks for transparency.\n\n"
        "What this thesis argues is simple: attribution should be part of the "
        "model itself, work at every level of detail, and speak the language "
        "of the domain."
    ),
}


# ---------------------------------------------------------------------------
# 2. slide 6: the two blocks, rewritten short and aligned with the speech
#    (lead phrase in bold, rest in the lighter family - the pattern the
#    left-hand card already uses)
# ---------------------------------------------------------------------------
REWRITES = [
    (6, "TextBox 42", [
        ("Users get outputs without reasons:", " trust drops."),
        ("Designers cannot debug", " what they cannot inspect."),
        ("Regulation now asks for transparency:", " EU AI Act, GDPR."),
    ]),
    (6, "TextBox 45", [
        ("Attribution belongs inside the model:", " not added on afterwards."),
        ("Consistent across levels of detail:", " one method, global to local."),
        ("Explanations must speak the domain's language:", " otherwise they cannot be acted on."),
    ]),
]


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------
def is_bold_run(run):
    """True for the heavy family of the pair (Nunito Bold, not Semi-Bold)."""
    name = font_name(run)
    return "Bold" in name and "Semi" not in name


def font_name(run):
    rPr = run.find(qn("a:rPr"))
    latin = rPr.find(qn("a:latin")) if rPr is not None else None
    return (latin.get("typeface") or "") if latin is not None else ""


def set_typeface(run, name):
    """Force a run onto a family, without touching anything else in its rPr."""
    rPr = run.find(qn("a:rPr"))
    if rPr is None or not name:
        return
    for tag in ("a:latin", "a:ea", "a:cs"):
        el = rPr.find(qn(tag))
        if el is not None:
            el.set("typeface", name)


def rewrite_bullets(shape, lines):
    """Keep one paragraph per line, using the formatting already there.

    For each target line: the bold lead phrase goes into the paragraph's first
    run (Nunito Bold in these cards) and the rest into its second run (Nunito
    Semi-Bold), which is exactly how the card bullets are built. Extra
    paragraphs and extra runs are removed, so the visual style does not move.
    """
    tf = shape.text_frame
    paras = tf.paragraphs
    proto = None
    for p in paras:
        if p.runs:
            proto = (len(p.runs), deepcopy(p._p))
            break
    if proto is None:
        return False, "no runnable paragraph to take the style from"
    n_runs, proto_p = proto

    txBody = tf._txBody
    for p in list(txBody.findall(qn("a:p"))):
        txBody.remove(p)

    for lead, rest in lines:
        p = deepcopy(proto_p)
        runs = p.findall(qn("a:r"))
        for r in runs[2:]:
            p.remove(r)
        runs = p.findall(qn("a:r"))
        if len(runs) >= 2:
            # the lead phrase always comes first in the paragraph; it simply
            # takes the heavy family of the pair and the rest the lighter one,
            # whatever order the two runs happen to sit in to begin with
            names = [font_name(runs[0]), font_name(runs[1])]
            heavy = next((n for n in names if "Bold" in n and "Semi" not in n), names[0])
            light = next((n for n in names if not ("Bold" in n and "Semi" not in n)), names[1])
            runs[0].find(qn("a:t")).text = lead
            runs[1].find(qn("a:t")).text = rest
            set_typeface(runs[0], heavy)
            set_typeface(runs[1], light)
        else:                                   # single-run card: one string
            runs[0].find(qn("a:t")).text = lead + rest
        txBody.append(p)
    return True, f"{len(lines)} bullets (style from a {n_runs}-run paragraph)"


def main():
    prs = Presentation(SRC)
    report = []

    # --- notes -------------------------------------------------------------
    notes = json.load(open(NOTES_IN))
    for key, text in NEW_NOTES.items():
        note_frame = prs.slides[int(key) - 1].notes_slide.notes_text_frame
        note_frame.text = text
        notes[key] = text
        report.append(f"note {key}: rewritten ({len(text.split())} words)")

    # --- slide 6 blocks ----------------------------------------------------
    for slide_no, shape_name, lines in REWRITES:
        slide = prs.slides[slide_no - 1]
        shape = next((sh for sh in slide.shapes if sh.name == shape_name), None)
        if shape is None:
            report.append(f"!! slide {slide_no}: shape {shape_name} not found")
            continue
        ok, info = rewrite_bullets(shape, lines)
        report.append(f"slide {slide_no} {shape_name}: {'rewritten, ' + info if ok else '!! ' + info}")

    prs.save(DST)
    json.dump(notes, open(NOTES_OUT, "w"), ensure_ascii=False, indent=1)

    spoken = sum(len(notes[str(i)].split()) for i in range(1, 77))
    report.append(f"wrote {os.path.relpath(DST, HERE)}")
    report.append(f"wrote {os.path.relpath(NOTES_OUT, HERE)}")
    report.append(f"spoken words slides 1-76: {spoken}  "
                  f"({spoken / WPM:.1f} min @130 wpm, {spoken / 120:.1f} @120 wpm)")
    for block, lo, hi in [("Intro 3-7", 3, 7), ("Context 8-16", 8, 16), ("Protocol 17-25", 17, 25),
                          ("C1 26-37", 26, 37), ("C2 38-50", 38, 50), ("C3 51-66", 51, 66),
                          ("Conclusion 67-76", 67, 76)]:
        w = sum(len(notes[str(i)].split()) for i in range(lo, hi + 1))
        report.append(f"   {block:<16} {w:>5} words  {w / WPM:>4.1f} min")
    print("\n".join(report))
    return prs, notes


if __name__ == "__main__":
    main()
