"""
Build MOUAD_LOUHICHI_VIVA_40min  (version 12) on the
"Beige Green Modern Illustrative Playful Thesis Defense Presentation" template.

Version VII restructures the deck along the lines of the reference viva
(R. Nesmaoui): section tracker, jury table, research-gap / RQ-table / protocol /
answers / findings / limitations / takeaway slides per contribution, dataset
cards, metric and hardware tables, thesis figures, numbered reference
footnotes, a Shapley deep dive and backup slides.

Version 12 keeps the v11 speech and slide content, and changes only the
look: the green theme becomes blue (palette_blue.py), and the
"Mohammed V University in Rabat  ·  ENSIAS" / "PhD Viva  ·  Mouad LOUHICHI"
header line is dropped.

Usage:  python3 build_v12.py <template.pptx> <out.pptx>
"""
import json
import os
import sys

import layouts
import palette_blue
import tpl

# Green -> blue theme, and no university / viva header line.
# Must run before the star import so the builder sees the blue constants.
palette_blue.apply(tpl, layouts)
layouts.SHOW_HEADER = False

from layouts import *  # noqa
from layouts import _ss_runs, FIT_REPORT

HERE = os.path.dirname(os.path.abspath(__file__))
FIGS = os.environ.get("VIVA_FIG_DIR", "/tmp/viva_build/figs")
THESIS_FIGS = os.environ.get("VIVA_THESIS_FIG_DIR", "/tmp/viva_build/thesis")
NOTES = json.load(open(os.path.join(HERE, "notes_v11.json")))


def N(*keys):
    """Speaker notes: merge the notes stored under the given keys."""
    return "\n\n".join(NOTES[str(k)] for k in keys if NOTES.get(str(k)))


def TF(name):
    """Path of a figure extracted from the thesis PDF."""
    return os.path.join(THESIS_FIGS, name)


# ---------------------------------------------------------------------------
# Numbered references (footnotes use these numbers; the References slides list them)
# ---------------------------------------------------------------------------
REFS = [
    ("Louhichi, M., Nesmaoui, R., Mbarek, M. & Lazaar, M. Shapley Values for Explaining the Black Box Nature of Machine Learning Model Clustering. Procedia Computer Science 220, 806–811 (2023)."),
    ("Louhichi, M., Nesmaoui, R. & Lazaar, M. Game Theory Meets Explainable AI: An Enhanced Approach to Understanding Black Box Models Through Shapley Values. IJACSA 16(7), 716–725 (2025)."),
    ("Louhichi, M., Nesmaoui, R. & Lazaar, M. DyHuCoG: A Dynamic Hypergraph Cooperative Game for Preference-aware Recommendation. IJIES 19(2), 887–902 (2026)."),
    ("Shapley, L. S. A Value for n-Person Games. Contributions to the Theory of Games II, 307–317, Princeton University Press (1953)."),
    ("Lundberg, S. M. & Lee, S.-I. A Unified Approach to Interpreting Model Predictions (SHAP). NeurIPS 30, 4765–4774 (2017)."),
    ("Lundberg, S. M. et al. From Local Explanations to Global Understanding with Explainable AI for Trees (TreeSHAP). Nature Machine Intelligence 2, 56–67 (2020)."),
    ("Ribeiro, M. T., Singh, S. & Guestrin, C. \"Why Should I Trust You?\": Explaining the Predictions of Any Classifier (LIME). KDD, 1135–1144 (2016)."),
    ("Castro, J., Gómez, D. & Tejada, J. Polynomial Calculation of the Shapley Value Based on Sampling. Computers & Operations Research 36(5), 1726–1730 (2009)."),
    ("Štrumbelj, E. & Kononenko, I. An Efficient Explanation of Individual Classifications Using Game Theory. JMLR 11, 1–18 (2010)."),
    ("Koren, Y., Bell, R. & Volinsky, C. Matrix Factorization Techniques for Recommender Systems. Computer 42(8), 30–37 (2009)."),
    ("He, X. et al. Neural Collaborative Filtering. WWW, 173–182 (2017)."),
    ("He, X. et al. LightGCN: Simplifying and Powering Graph Convolution Network for Recommendation. SIGIR, 639–648 (2020)."),
    ("Xia, L. et al. Hypergraph Contrastive Collaborative Filtering (HCCF). SIGIR, 70–79 (2022)."),
    ("Xiangyi, Y. et al. Hypergraph Projection Enhanced Collaborative Filtering (HPCF). Int. J. Data Science and Analytics 19(2), 269–281 (2025)."),
    ("Zhang, D. et al. RecDCL: Dual Contrastive Learning for Recommendation. The Web Conference, 3655–3666 (2024)."),
    ("Feng, Y. et al. Hypergraph Neural Networks. AAAI 33, 3558–3565 (2019)."),
    ("Rousseeuw, P. J. Silhouettes: A Graphical Aid to the Interpretation and Validation of Cluster Analysis. J. Comput. Appl. Math. 20, 53–65 (1987)."),
    ("Gramegna, A. & Giudici, P. SHAP and LIME: An Evaluation of Discriminative Power in Credit Risk. Frontiers in AI 4, 752558 (2021)."),
    ("Cortez, P. et al. Wine Quality. UCI Machine Learning Repository (2009).  ·  Dua, D. & Taniskidou, E. Beijing Multi-Site Air Quality Data. UCI Machine Learning Repository (2017)."),
    ("Harper, F. M. & Konstan, J. A. The MovieLens Datasets: History and Context. ACM TiiS 5(4), 19 (2015).  ·  McAuley, J. et al. Amazon Review Data (Amazon-Book). UCSD (2018)."),
    ("Zhang, Y. & Chen, X. Explainable Recommendation: A Survey and New Perspectives. Foundations and Trends in IR 14(1), 1–101 (2020)."),
    ("Adomavicius, G. & Tuzhilin, A. Toward the Next Generation of Recommender Systems. IEEE TKDE 17(6), 734–749 (2005).  ·  Burke, R. Hybrid Recommender Systems. UMUAI 12(4), 331–370 (2002)."),
    ("Zhu, Z. et al. Popularity Bias in Dynamic Recommendation. KDD, 2439–2449 (2021).  ·  Hurley, N. & Zhang, M. Novelty and Diversity in Top-N Recommendation. ACM TOIT 10(4) (2011)."),
    ("Arrieta, A. B. et al. Explainable Artificial Intelligence (XAI): Concepts, Taxonomies, Opportunities and Challenges. Information Fusion 58, 82–115 (2020)."),
    ("Doshi-Velez, F. & Kim, B. Towards a Rigorous Science of Interpretable Machine Learning. arXiv:1702.08608 (2017).  ·  Rudin, C. et al. Interpretable ML: Fundamental Principles and 10 Grand Challenges. Statistics Surveys 16 (2022)."),
    ("European Union. Regulation (EU) 2024/1689 (AI Act), Art. 13 (2024).  ·  Regulation (EU) 2016/679 (GDPR), Art. 22 (2016).  ·  OECD. Recommendation of the Council on Artificial Intelligence (2019)."),
    ("Holm, S. A Simple Sequentially Rejective Multiple Test Procedure. Scand. J. Statist. 6(2), 65–70 (1979).  ·  Cohen, J. Statistical Power Analysis for the Behavioral Sciences (1988)."),
    ("Nesmaoui, R., Louhichi, M. & Lazaar, M. Dynamic Recommender Systems with Real-time Shapley Value-based Contribution Adjustment. IJIES 18, 241–257 (2025)."),
]


def cite(*nums):
    """Footnote text for the given reference numbers (1-based), abbreviated."""
    parts = []
    for n in nums:
        txt = REFS[n - 1]
        parts.append(f"[{n}] {txt}")
    return "   ".join(parts)


JURY = [
    ("President", "Pr. Abdellatif EL AFIA", "PES", "ENSIAS, Mohammed V University, Rabat"),
    ("Supervisor", "Pr. Mohamed LAZAAR", "PES", "ENSIAS, Mohammed V University, Rabat"),
    ("Reviewer", "Pr. M'hamed AIT KBIR", "PES", "FST, Abdelmalek Essaâdi University, Tangier"),
    ("Reviewer", "Pr. Oussama MAHBOUB", "PES", "ENSA, Abdelmalek Essaâdi University, Tetouan"),
    ("Reviewer", "Pr. Noureddine KERZAZI", "MCH", "ENSIAS, Mohammed V University, Rabat"),
    ("Examiner", "Pr. Hicham OMARA", "MCH", "FP Taza, Sidi Mohamed Ben Abdellah University, Fez"),
    ("Examiner", "Pr. Fatima OUZAYD", "PES", "ENSIAS, Mohammed V University, Rabat"),
    ("Examiner", "Pr. Yasser EL MADANI EL ALAMI", "MCH", "ENSIAS, Mohammed V University, Rabat"),
    ("Guest", "Pr. Yassine AFOUDI", "MC", "Faculty of Sciences, Cadi Ayyad University, Marrakech"),
]


def title_slide(ctx, deck, notes=None, closing=False):
    """Title slide with logos, thesis title, presenter / supervisor cards and the jury table."""
    ctx.n += 1
    s = deck.new_slide()
    picture(s, os.path.join(FIGS, "um5_logo.png"), L, emu(0.5), h=emu(1.0))
    picture(s, os.path.join(FIGS, "ministry_logo.png"), SLIDE_W / 2 - emu(1.25), emu(0.4), h=emu(1.25))
    picture(s, os.path.join(FIGS, "ensias_logo.jpg"), R - emu(1.6), emu(0.45), h=emu(1.1))
    textbox(s, L, emu(1.68), W, emu(0.4),
            [Para([Run("Doctoral Studies Center in Information and Engineering Sciences and Technologies (ST2I)",
                       font="bold", size=15, color=MUTED)], align="ctr", lnspc=19)])
    textbox(s, L, emu(2.12), W, emu(0.4),
            [Para([Run("QUESTIONS & DISCUSSION  ·  THANK YOU" if closing else "PHD THESIS DEFENCE  ·  COMPUTER SCIENCE", font="xbold", size=14, color=ORANGE, spc=2)], align="ctr", lnspc=19)])
    textbox(s, L, emu(2.5), W, emu(2.0),
            [Para([Run("Cooperative Game Theory for", font="title", size=50, color=INK, spc=-3)], align="ctr", lnspc=54),
             Para([Run("Explainable AI in Recommendation Systems", font="title", size=50, color=INK, spc=-3)], align="ctr", lnspc=54)])
    textbox(s, L, emu(4.28), W, emu(0.5),
            [Para([Run("A Shapley Framework for Actionable Insight", font="bold", size=25, color=GREEN, spc=-1.0)], align="ctr", lnspc=30)])
    accent(s, "asterisk_o", R - emu(1.4), emu(2.4), emu(0.55))
    accent(s, "sparkle_y", L + emu(0.1), emu(4.05), emu(0.45), rot=20)
    # presenter + supervisor cards
    cy = emu(4.95)
    ch = emu(0.86)
    cw = emu(6.6)
    c1 = rrect(s, SLIDE_W / 2 - cw - emu(0.2), cy, cw, ch, fill=GREEN, radius=emu(0.24))
    shape_text(c1, [Para([Run("PHD VIVA PRESENTED BY", font="xbold", size=11, color=YELLOW, spc=1.5)], align="ctr", lnspc=14),
                    Para([Run("Mouad LOUHICHI", font="xbold", size=22, color=WHITE)], align="ctr", lnspc=26, spcbef=2)], anchor="ctr")
    c2 = rrect(s, SLIDE_W / 2 + emu(0.2), cy, cw, ch, fill=TINT, radius=emu(0.24))
    shape_text(c2, [Para([Run("SUPERVISED BY", font="xbold", size=11, color=ORANGE, spc=1.5)], align="ctr", lnspc=14),
                    Para([Run("Pr. Mohamed LAZAAR  ·  PES, ENSIAS", font="xbold", size=20, color=INK)], align="ctr", lnspc=24, spcbef=2)], anchor="ctr")
    # jury table (example-deck style)
    jy = emu(6.02)
    textbox(s, L, jy, W, emu(0.3), [Para([Run("JURY MEMBERS", font="xbold", size=12, color=MUTED, spc=2)], lnspc=15)])
    rows = [["Role", "Name", "Grade", "Institution"]] + [list(j) for j in JURY]
    gf, th = table(s, L, jy + emu(0.32), W, rows, col_widths=[1.3, 3.3, 0.9, 5.2], size=13, head_size=12,
                   align=["l", "l", "ctr", "l"], header_align=["l", "l", "ctr", "l"], pad=0.05)
    textbox(s, L, min(jy + emu(0.32) + th + emu(0.18), SLIDE_H - emu(0.5)), W, emu(0.3),
            [Para([Run("Rabat, Morocco  ·  2026", font="bold", size=14, color=MUTED)], align="ctr", lnspc=17)])
    set_notes(s, notes)
    return s


# ---------------------------------------------------------------------------
# Per-contribution slide patterns (example-deck structure)
# ---------------------------------------------------------------------------
def gap_slide(ctx, eyebrow, tabs, active, items, gap_text, notes, refs_=None, title="Research Gap"):
    """Bullets on top, 'Research gap' statement box below."""
    s, top = content_slide(ctx, title, eyebrow=eyebrow, tabs=tabs, active=active, notes=notes, refs=refs_)
    bh = emu(1.75)
    fit_textbox(s, L, top, W, CB - top - bh - emu(0.75), bullets(items, size=21, gap0=12), min_scale=0.7)
    statement(s, L, CB - bh - emu(0.3), W, bh, "Research gap", gap_text, fill=ORANGE, size=22)
    return s


def rq_slide(ctx, eyebrow, tabs, active, rq_label, rq_text, objectives, notes, refs_=None, title=None):
    """RQ statement on top, objectives table (Objective / What it delivers / Evidence) below."""
    s, top = content_slide(ctx, title or f"{rq_label} and Objectives", eyebrow=eyebrow, tabs=tabs, active=active, notes=notes, refs=refs_)
    sh = emu(1.45)
    statement(s, L, top + emu(0.2), W, sh, rq_label, rq_text, fill=GREEN, size=22)
    ty = top + emu(0.2) + sh + emu(0.45)
    rows = [["Objective", "What it delivers", "Where it is shown"]] + [list(o) for o in objectives]
    gf, th = table(s, L, ty, W, rows, col_widths=[4.6, 7.4, 3.6], size=18, head_size=17, row_h=emu(0.9))
    return s


def protocol_slide(ctx, eyebrow, tabs, active, rows, success_items, notes, refs_=None, title="Evaluation Protocol"):
    """Two-column protocol table + 'What counts as success' card."""
    s, top = content_slide(ctx, title, eyebrow=eyebrow, tabs=tabs, active=active, notes=notes, refs=refs_)
    lw = emu(10.9)
    gf, th = table(s, L, top, lw, [["Step", "Setting used in this contribution"]] + [list(r) for r in rows], col_widths=[2.6, 8.3], size=17, head_size=17, row_h=emu(0.6))
    dx = L + lw + emu(0.5)
    dw = R - dx
    card(s, dx, top + emu(0.25), dw, CB - top - emu(0.5), label="What counts as success",
         paras=bullets(success_items, size=19, color=WHITE, c0=YELLOW, c1=YELLOW, gap0=10), pad=(0.5, 0.7, 0.45, 0.3))
    return s


def answer_slide(ctx, eyebrow, tabs, active, rq_label, answer_text, obj_rows, notes, title=None):
    """Answer statement + objectives status table."""
    s, top = content_slide(ctx, title or f"Answer to {rq_label}", eyebrow=eyebrow, tabs=tabs, active=active, notes=notes)
    sh = emu(1.6)
    statement(s, L, top + emu(0.2), W, sh, f"Answer to {rq_label}", answer_text, fill=GREEN, size=22)
    ty = top + emu(0.2) + sh + emu(0.45)
    rows = [["Objective", "Status", "Evidence"]] + [list(r) for r in obj_rows]
    gf, th = table(s, L, ty, W, rows, col_widths=[5.2, 1.4, 9.0], size=18, head_size=17, row_h=emu(0.85),
                   align=["l", "ctr", "l"], header_align=["l", "ctr", "l"])
    return s


def findings_slide(ctx, eyebrow, tabs, active, findings, notes, title="Key Findings", refs_=None):
    """Numbered finding rows (title + one-line body) in alternating tints."""
    s, top = content_slide(ctx, title, eyebrow=eyebrow, tabs=tabs, active=active, notes=notes, refs=refs_)
    n = len(findings)
    gap = emu(0.18)
    rh = (CB - top - emu(0.3) - gap * (n - 1)) / n
    for i, (h1, body) in enumerate(findings):
        yy = top + i * (rh + gap)
        rrect(s, L, yy, W, rh, fill=TINT if i % 2 == 0 else TINT2, radius=emu(0.22))
        badge(s, L + emu(0.3), yy + (rh - emu(0.62)) / 2, emu(0.62), str(i + 1), fill=GREEN, color=WHITE, size=20)
        fit_textbox(s, L + emu(1.25), yy + emu(0.12), W - emu(1.6), rh - emu(0.24),
                    [Para([Run(h1, font="xbold", size=21, color=GREEN)], lnspc=25),
                     Para(md_runs(body, size=19, color=INK), lnspc=24, spcbef=4)], anchor="ctr", min_scale=0.7)
    return s


def limitations_slide(ctx, eyebrow, tabs, active, lims, next_text, notes, title="Limitations"):
    """2x2 limitation cards + 'leads to' bar."""
    s, top = content_slide(ctx, title, eyebrow=eyebrow, tabs=tabs, active=active, notes=notes)
    bar_h = emu(1.05)
    cells = grid(len(lims), 2, L, top, W, CB - top - bar_h - emu(0.6), gap=emu(0.35), vgap=emu(0.3))
    for i, ((h1, body), (x, y, w, h)) in enumerate(zip(lims, cells)):
        f = [GREEN, "1F5C99", "1F5C99", GREEN][i % 4]
        box = rrect(s, x, y, w, h, fill=f, radius=emu(0.28))
        fit_textbox(s, x + emu(0.4), y + emu(0.3), w - emu(0.8), h - emu(0.5),
                    [Para([Run(h1.upper(), font="xbold", size=14, color=YELLOW, spc=1.6)], lnspc=18),
                     Para(md_runs(body, size=19, color=WHITE), lnspc=24, spcbef=8)], anchor="t", min_scale=0.7)
    by = CB - bar_h - emu(0.2)
    bar = rrect(s, L, by, W, bar_h, fill=None, line=ORANGE, line_w=2.5, radius=emu(0.25))
    shape_text(bar, [Para(md_runs(next_text, size=20, color=INK), align="ctr", lnspc=25)], anchor="ctr", insets=(emu(0.5), emu(0.1), emu(0.5), emu(0.1)))
    return s


def takeaway_slide(ctx, eyebrow, tabs, active, label, takeaway_text, tiles, next_text, notes, title=None):
    """Three tiles + 'Takeaway' statement box + next-step bar."""
    s, top = content_slide(ctx, title or f"Takeaway: {label}", eyebrow=eyebrow, tabs=tabs, active=active, notes=notes)
    th = emu(2.9)
    cells = grid(len(tiles), len(tiles), L, top, W, th, gap=emu(0.35))
    for i, ((h1, body), (x, y, w, h)) in enumerate(zip(tiles, cells)):
        f = [GREEN, "1F5C99", ORANGE][i % 3]
        box = rrect(s, x, y, w, h, fill=f, radius=emu(0.3))
        fit_textbox(s, x + emu(0.4), y + emu(0.35), w - emu(0.8), h - emu(0.6),
                    [Para([Run(h1, font="title", size=28, color=YELLOW if f != ORANGE else WHITE, spc=-1.2)], lnspc=32),
                     Para([Run(body, font="body", size=19, color="F7F2EA")], lnspc=24, spcbef=10)], anchor="t", min_scale=0.7)
    sy = top + th + emu(0.5)
    sh = emu(1.75)
    statement(s, L, sy, W, sh, f"Takeaway  ·  {label}", takeaway_text, fill=ORANGE, size=23)
    ny = sy + sh + emu(0.35)
    if next_text and CB - ny > emu(0.7):
        bar = rrect(s, L, ny, W, CB - ny - emu(0.15), fill=GREEN, radius=emu(0.25))
        shape_text(bar, [Para(md_runs(next_text, size=20, color=WHITE), align="ctr", lnspc=25)], anchor="ctr", insets=(emu(0.5), emu(0.05), emu(0.5), emu(0.05)))
    return s


def source_caption(s, x, y, w, text, size=13, align="l"):
    """One-line 'Table x.y / Fig. x.y (thesis)' caption under a table or figure."""
    return textbox(s, x, y, w, emu(0.45), [Para([Run(text, font="body", size=size, color=MUTED)], align=align, lnspc=size + 4)])


def figure_frame(s, path, x, y, w, h, caption=None, pad=0.2):
    """White framed figure, fitted inside (w, h) and centred; optional caption at the bottom."""
    from PIL import Image
    frame = rrect(s, x, y, w, h, fill=WHITE, line=RULE, line_w=1.25, radius=emu(0.25))
    im = Image.open(path)
    ratio = im.height / im.width
    cap_h = emu(0.45) if caption else 0
    pw = w - emu(2 * pad)
    ph = pw * ratio
    if ph > h - emu(2 * pad) - cap_h:
        ph = h - emu(2 * pad) - cap_h
        pw = ph / ratio
    picture(s, path, x + (w - pw) / 2, y + emu(pad) + (h - emu(2 * pad) - cap_h - ph) / 2, w=pw, h=ph)
    if caption:
        textbox(s, x, y + h - cap_h - emu(0.05), w, cap_h, [Para([Run(caption, font="body", size=14, color=MUTED)], align="ctr", lnspc=17)], anchor="ctr")
    return frame


def build(template, out):
    deck = Deck(template)
    ctx = Ctx(deck)

    # ======================================================================
    # 1. TITLE
    # ======================================================================
    layouts.FOOTER_LOGO = os.path.join(FIGS, "ensias_logo.jpg")
    title_slide(ctx, deck, notes=N(1))

    # ======================================================================
    # 2. OUTLINE (template "Overview" style)
    # ======================================================================
    ctx.n += 1
    s = deck.new_slide()
    chrome(s, ctx.n)
    textbox(s, L, emu(1.9), W, emu(1.6), [Para([Run("Outline", font="title", size=92, color=INK, spc=-5)], align="ctr", lnspc=96)])
    accent(s, "sparkle_o", SLIDE_W / 2 + emu(2.7), emu(1.7), emu(0.6))
    accent(s, "sparkle_y", SLIDE_W / 2 - emu(3.5), emu(2.9), emu(0.55), rot=180)
    textbox(s, L, emu(3.55), W, emu(0.5), [Para([Run("Seven parts  ·  each contribution follows the same structure: research gap → objectives → methodology → protocol → results → findings",
                                                     font="body", size=21, color=MUTED)], align="ctr", lnspc=26)])
    parts = [
        ("01", "Introduction", "Motivation · Actionable insight · Why XAI matters"),
        ("02", "Context & Problematic", "Four approaches · Limitations · Research questions"),
        ("03", "Experimental Protocol", "Four datasets · Baselines · Metrics · Hardware"),
        ("04", "Contribution I", "Deep dive: cooperative games · Explainable clustering (Wine)"),
        ("05", "Contribution II", "Multi-level XAI for large-scale clustering (Beijing)"),
        ("06", "Contribution III", "DyHuCoG: a cooperative game on hypergraphs"),
        ("07", "Conclusion & Perspectives", "Synthesis · Publications · Perspectives · References"),
    ]
    cells = grid(8, 4, L, emu(4.45), W, emu(5.4), gap=emu(0.3), vgap=emu(0.3))
    for i, (num, head, sub) in enumerate(parts):
        x, y, w, h = cells[i]
        dark = i % 2 == 0
        box = rrect(s, x, y, w, h, fill=GREEN if dark else None, line=None if dark else GREEN, line_w=2.25, radius=emu(0.4))
        shape_text(box, [Para([Run(num, font="xbold", size=30, color=YELLOW if dark else ORANGE)], lnspc=34),
                         Para([Run(head, font="xbold", size=25, color=WHITE if dark else INK)], lnspc=29, spcbef=6),
                         Para([Run(sub, font="body", size=17, color="D6E2EF" if dark else MUTED)], lnspc=21, spcbef=6)],
                   anchor="t", insets=(emu(0.4), emu(0.4), emu(0.35), emu(0.3)))
    # last cell: thanks / Q&A
    x, y, w, h = cells[7]
    box = rrect(s, x, y, w, h, fill=YELLOW, radius=emu(0.4))
    shape_text(box, [Para([Run("Q & A", font="title", size=44, color=INK, spc=-2)], align="ctr", lnspc=48),
                     Para([Run("Discussion with the jury  ·  backup tables at the end", font="bold", size=17, color=INK)], align="ctr", lnspc=21, spcbef=6)], anchor="ctr")
    set_notes(s, N(2))

    # ======================================================================
    # SECTION 1 — INTRODUCTION
    # ======================================================================
    section_slide(ctx, "01", "Introduction", "Why explainability is a core requirement for recommender systems",
                  [("Motivation", "Black-box AI systems shape what billions of people see, buy and watch every day: accurate, but not transparent."),
                   ("Actionable insight", "An explanation is useful when it names a factor, in the domain's own words, that a designer can change."),
                   ("Research context", "From matrix factorisation to hypergraph recommenders: each step added modelling power and removed transparency.")],
                  notes=N(3))

    # --- Motivation: three questions -----------------------------------------
    s, top = content_slide(ctx, "Motivation: Three Questions", eyebrow="Introduction",
                           tabs=["Motivation", "Actionable Insight", "Research Context"], active="Motivation", notes=N(4), refs=cite(21, 24, 26))
    qs = [("Everywhere", "How do black-box AI systems shape what billions of users see, buy and watch every day?",
           "Recommenders shape news, study, health and credit decisions; market > $15B by 2029."),
          ("The Black Box", "Why do state-of-the-art recommenders and clustering pipelines stay black boxes for users and designers?",
           "Deep & graph models: hidden logic, hard to audit. EU AI Act: high-risk → must explain."),
          ("Toward Trust", "How can transparency be built into the model, instead of being added afterwards?",
           "Insight that is accountable, auditable and actionable, not just accurate.")]
    cells = grid(3, 3, L, top + emu(0.25), W, emu(4.6), gap=emu(0.35))
    for (head, q, sub), (x, y, w, h) in zip(qs, cells):
        card(s, x, y, w, h, label=head, paras=[P(q, size=23, color=WHITE, font="bold"),
                                                 Para([Run(sub, font="body", size=18, color="C9D8E6")], lnspc=23, spcbef=14)],
             pad=(0.5, 0.75, 0.5, 0.4), label_size=21)
    # tension bar
    ty = top + emu(0.25) + emu(4.6) + emu(0.35)
    bar = rrect(s, L, ty, W, emu(0.95), fill=TINT, radius=emu(0.25))
    shape_text(bar, [Para(md_runs("**The core tension:** as models gain power, they lose the transparency needed for trustworthy use. "
                                  "This thesis treats **accuracy and interpretability as goals to be met together**, not traded against each other.",
                                  size=20, color=INK), align="ctr", lnspc=26)], anchor="ctr", insets=(emu(0.4), emu(0.1), emu(0.4), emu(0.1)))

    # --- Actionable insight — definition --------------------------------------
    s, top = content_slide(ctx, "Actionable Insight: the Definition", eyebrow="Introduction",
                           tabs=["Motivation", "Actionable Insight", "Research Context"], active="Actionable Insight", notes=N(5), refs=cite(25))
    lw = emu(8.6)
    fit_textbox(s, L, top, lw, CB - top - emu(0.2), [
        H("Definition 1.1 (Actionable insight)", size=25, color=GREEN),
        *bullets([
            "An explanation is actionable when it points to **at least one factor that can be changed**, and that change leads to a **clear change in the model output**…",
            "… and that factor is **stated in the domain's own terms**.",
            "The domain's own terms: a chemical variable (wine), a pollution indicator (air quality), a preference signal (recommendation), **not a hidden latent code**.",
            "**Why it matters:** an explanation that names a changeable driver supports **action**, not only description.",
        ], size=21)
    ], min_scale=0.7)
    # right: flow diagram "from explanation to action"
    dx = L + lw + emu(0.6)
    dw = R - dx
    textbox(s, dx, top, dw, emu(0.4), [Para([Run("FROM EXPLANATION TO ACTION", font="xbold", size=14, color=ORANGE, spc=1.6)], align="ctr", lnspc=18)])
    steps = [("Modifiable factor", GREEN), ("Change in model output", GREEN), ("Is it actionable?", INK), ("Action lever", ORANGE)]
    n = len(steps)
    bw = emu(1.75)
    gap = (dw - n * bw) / (n - 1)
    by = top + emu(1.4)
    bh = emu(1.55)
    for i, (t, f) in enumerate(steps):
        x = dx + i * (bw + gap)
        chip(s, x, by, bw, bh, t, fill=f, color=WHITE, size=17, radius=emu(0.2))
        if i < n - 1:
            arrow(s, x + bw + emu(0.05), by + bh / 2, x + bw + gap - emu(0.05), by + bh / 2, color=GREEN, w=2.25)
    # return arrow (feedback)
    fy = by + bh + emu(0.45)
    line(s, dx + bw / 2, by + bh + emu(0.05), dx + bw / 2, fy, color=ORANGE, w=2.25)
    line(s, dx + bw / 2, fy, dx + dw - bw / 2, fy, color=ORANGE, w=2.25, dash="dash")
    line(s, dx + dw - bw / 2, by + bh + emu(0.05), dx + dw - bw / 2, fy, color=ORANGE, w=2.25)
    textbox(s, dx, fy + emu(0.2), dw, emu(0.8), [Para(md_runs("**Actionable** = a real-world lever you can pull to change the outcome", size=18, color=ORANGE), align="ctr", lnspc=23)])
    # three domain examples
    ex = [("Wine", "density · pH · acidity"), ("Air quality", "PM2.5 · CO · temperature"), ("Recommendation", "preference · context · diversity")]
    cells = grid(3, 3, dx, fy + emu(1.25), dw, emu(1.35), gap=emu(0.2))
    for (h1, h2), (x, y, w, h) in zip(ex, cells):
        chip(s, x, y, w, h, h1, fill=TINT, color=INK, size=18, sub=h2, sub_size=14, sub_color=MUTED, radius=emu(0.2))

    # --- Research context -----------------------------------------------------
    s, top = content_slide(ctx, "Research Context", eyebrow="Introduction",
                           tabs=["Motivation", "Actionable Insight", "Research Context"], active="Research Context", notes=N(6), refs=cite(10, 12, 16, 26))
    # timeline of recommender evolution
    stages = [("Similarity models", "2003–09"), ("Matrix factorisation", "2009–13"), ("Neural CF", "2016–19"), ("Graph CNN", "2018–22"), ("Hypergraph", "2022+")]
    textbox(s, L, top, W, emu(0.4), [Para([Run("EVOLUTION OF RECOMMENDER SYSTEMS", font="xbold", size=14, color=ORANGE, spc=1.6)], lnspc=18)])
    n = len(stages)
    bw = emu(2.55)
    gap = (W - n * bw) / (n - 1)
    by = top + emu(0.55)
    bh = emu(1.25)
    for i, (t, yr) in enumerate(stages):
        x = L + i * (bw + gap)
        f = GREEN if i < n - 1 else ORANGE
        chip(s, x, by, bw, bh, t, fill=f, color=WHITE, size=19, sub=yr, sub_size=14, radius=emu(0.2))
        if i < n - 1:
            arrow(s, x + bw + emu(0.06), by + bh / 2, x + bw + gap - emu(0.06), by + bh / 2, color=GREEN, w=2.25)
    ay = by + bh + emu(0.3)
    arrow(s, L, ay, R, ay, color=ORANGE, w=4)
    textbox(s, L, ay + emu(0.1), W, emu(0.4), [Para(md_runs("**The interpretability gap grows:** each step improved ranking, but replaced a hidden latent code with a hidden message-passing mechanism. Neither can be acted on.", size=18, color=ORANGE), align="ctr", lnspc=23)])
    # bottom: two cards
    cy = ay + emu(0.85)
    chh = CB - cy - emu(0.1)
    cw = (W - emu(0.4)) / 2
    card(s, L, cy + emu(0.25), cw, chh - emu(0.25), label="Why the gap matters",
         paras=bullets(["**Weakens user trust:** users see outputs without knowing why.",
                        "**Limits debugging** and scientific learning.",
                        "**Conflicts with regulation:** EU AI Act, OECD principles, GDPR.",
                        "EU AI Act (Art. 13): high-risk systems must provide explanations **in human-understandable terms**."],
                       size=19, color=WHITE, c0=YELLOW, c1=YELLOW, gap0=6), pad=(0.5, 0.65, 0.45, 0.3))
    light_card(s, L + cw + emu(0.4), cy + emu(0.25), cw, chh - emu(0.25), label="What this thesis argues",
               paras=bullets(["Recommenders moved from similarity filters to **representation learning on sparse, high-dimensional, changing data**.",
                              "Hypergraph models add higher-order user-item-context relations but assume **every message matters equally**.",
                              "A well-founded attribution method is needed, and it should be **part of the model itself**, not an add-on."],
                             size=19, color=INK, gap0=6), pad=(0.5, 0.65, 0.45, 0.3))

    # --- AI recommenders around us: brand logos (example-deck style) --------
    s, top = content_slide(ctx, "AI-Powered Recommendation Is Everywhere", eyebrow="Introduction",
                           tabs=["Motivation", "Actionable Insight", "Research Context"], active="Research Context", notes=N(7), refs=cite(21, 22))
    brands = [("netflix.png", "Netflix", "Movie and TV recommendation platform"),
              ("spotify.png", "Spotify", "Music recommendation and streaming service"),
              ("yelp.png", "Yelp", "Local business and restaurant recommendation"),
              ("amazon.png", "Amazon", "E-commerce platform with personalised product recommendations")]
    cells = grid(4, 4, L, top + emu(0.1), W, emu(4.9), gap=emu(0.35))
    for (fn, name, desc), (x, y, w, h) in zip(brands, cells):
        box = rrect(s, x, y, w, h, fill=WHITE, line=RULE, line_w=1.25, radius=emu(0.3))
        path = os.path.join(THESIS_FIGS, "logos", fn)
        lw_, lh_ = emu(2.0), emu(2.0)
        if os.path.exists(path):
            from PIL import Image as _Im
            im = _Im.open(path)
            ratio = im.height / im.width
            pw = lw_
            ph = pw * ratio
            if ph > lh_:
                ph = lh_
                pw = ph / ratio
            picture(s, path, x + (w - pw) / 2, y + emu(0.45) + (lh_ - ph) / 2, w=pw, h=ph)
        else:
            chip(s, x + emu(0.5), y + emu(0.45), w - emu(1.0), lh_, name, fill=TINT, color=INK, size=30)
        textbox(s, x + emu(0.3), y + emu(2.75), w - emu(0.6), emu(0.5), [Para([Run(name, font="xbold", size=24, color=INK)], align="ctr", lnspc=28)])
        textbox(s, x + emu(0.3), y + emu(3.3), w - emu(0.6), emu(1.4), [Para([Run(desc, font="body", size=17, color=MUTED)], align="ctr", lnspc=22)])
    by = top + emu(0.1) + emu(4.9) + emu(0.4)
    bar = rrect(s, L, by, W, CB - by - emu(0.35), fill=TINT, radius=emu(0.3))
    shape_text(bar, [Para(md_runs("AI recommendation shapes what **billions** see, buy and listen to every day. Each system is very **accurate, yet a black box**: "
                                  "its reasoning is hidden from the user. Everywhere, and hidden: that is **exactly the gap this thesis targets**.", size=21, color=INK),
                          align="ctr", lnspc=27)], anchor="ctr", insets=(emu(0.6), emu(0.1), emu(0.6), emu(0.1)))

    # ======================================================================
    # SECTION 2 — CONTEXT & PROBLEMATIC
    # ======================================================================
    section_slide(ctx, "02", "Context & Problematic", "The main approaches, their limitations and the five research questions",
                  [("Approaches", "Collaborative, content-based, hybrid, matrix factorisation and graph/hypergraph recommenders: each one stronger, each one less transparent."),
                   ("Problematic", "Three main limitations: lack of explainability, difficulty of scaling, weak link between explanation and learning."),
                   ("Contributions", "Five research questions answered by three contributions that build on each other, under one cooperative-game view.")],
                  notes=N(8))

    # --- Approaches: one slide per family (example-deck style) ----------------
    APTABS = ["Approaches", "Problematic", "Contributions"]

    def approach_slide(title, bullets_, limitation, diagram, notes, refs_):
        s, top = content_slide(ctx, title, eyebrow="Context & Problematic", tabs=APTABS, active="Approaches", notes=notes, refs=refs_)
        lw = emu(8.4)
        fit_textbox(s, L, top, lw, CB - top - emu(1.9), bullets(bullets_, size=21, gap0=12), min_scale=0.7)
        statement(s, L, CB - emu(1.6), lw, emu(1.2), "Limitation", limitation, fill=ORANGE, size=17)
        dx = L + lw + emu(0.6)
        diagram(s, dx, top, R - dx, CB - top - emu(0.3))
        return s

    def diag_content(s, x, y, w, h):
        textbox(s, x, y, w, emu(0.4), [Para([Run("CONTENT-BASED FILTERING", font="xbold", size=14, color=ORANGE, spc=1.4)], align="ctr", lnspc=18)])
        steps = [("User taste profile", GREEN), ("Item feature vectors", GREEN), ("Similarity score", INK), ("Top-N recommend", ORANGE)]
        n = len(steps)
        bw = emu(1.72)
        gap = (w - n * bw) / (n - 1)
        by = y + emu(0.65)
        bh = emu(1.3)
        for i, (t, f) in enumerate(steps):
            xx = x + i * (bw + gap)
            chip(s, xx, by, bw, bh, t, fill=f, color=WHITE, size=16, radius=emu(0.2))
            if i < n - 1:
                arrow(s, xx + bw + emu(0.05), by + bh / 2, xx + bw + gap - emu(0.05), by + bh / 2, color=GREEN, w=2.25)
        ey = by + bh + emu(0.4)
        textbox(s, x, ey, w, emu(0.5), [Para(md_runs("**Example:** liked sci-fi + Nolan  →  suggest films with a similar genre, cast or keywords", size=17, color=INK), align="ctr", lnspc=22)])
        cw = (w - emu(0.3)) / 2
        light_card(s, x, ey + emu(0.75), cw, emu(1.9), label="Candidate item features",
                   paras=[P("genre = Sci-Fi · director = Nolan\ncast = … · year = 2010 · rating = 8.6", size=15, color=INK)], pad=(0.3, 0.55, 0.3, 0.2), label_size=15)
        light_card(s, x + cw + emu(0.3), ey + emu(0.75), cw, emu(1.9), label="Why recommended",
                   paras=[P("high cosine similarity to your profile\n**sim = cos(f_{user}, f_{item})**", size=15, color=INK)], pad=(0.3, 0.55, 0.3, 0.2), label_size=15)
        bar = rrect(s, x, ey + emu(2.95), w, y + h - (ey + emu(2.95)), fill=GREEN, radius=emu(0.25))
        shape_text(bar, [Para(md_runs("Explainable because the factors are **domain-level and can be changed**: exactly what is lost when latent factors and message passing take over.", size=16, color=WHITE), align="ctr", lnspc=21)],
                   anchor="ctr", insets=(emu(0.35), emu(0.1), emu(0.35), emu(0.1)))

    approach_slide("Content-Based Filtering",
                   ["Recommends items **based on their features** and the user's past preferences.",
                    "Builds a **user profile** from previously liked, viewed or selected items.",
                    "Suggests new items with **similar characteristics** (genre, cast, keywords, brand).",
                    "Explainable by construction: the reason is a **named feature** the user recognises."],
                   "Recommendations may become too similar and lack diversity; it needs good item metadata.",
                   diag_content, N("ap_content"), cite(22))

    def diag_cf(s, x, y, w, h):
        textbox(s, x, y, w, emu(0.4), [Para([Run("USER-BASED  ·  ITEM-BASED", font="xbold", size=14, color=ORANGE, spc=1.4)], align="ctr", lnspc=18)])
        # tiny bipartite graph: users left, items right, arcs
        gy = y + emu(0.7)
        users = [("u1", 0), ("u2", 1), ("u3", 2)]
        items = [("i1", 0), ("i2", 1), ("i3", 2), ("i4", 3)]
        ux = x + emu(0.9)
        ix = x + w - emu(1.2)
        upos, ipos = {}, {}
        for name, k in users:
            yy = gy + emu(0.3) + k * emu(1.15)
            badge(s, ux, yy, emu(0.75), name, fill=GREEN, color=WHITE, size=16)
            upos[name] = (ux + emu(0.75), yy + emu(0.375))
        for name, k in items:
            yy = gy + k * emu(0.9)
            rrect(s, ix, yy, emu(0.75), emu(0.7), fill=ORANGE, radius=emu(0.12))
            textbox(s, ix, yy, emu(0.75), emu(0.7), [Para([Run(name, font="xbold", size=15, color=WHITE)], align="ctr", lnspc=18)], anchor="ctr")
            ipos[name] = (ix, yy + emu(0.35))
        edges = [("u1", "i1"), ("u1", "i2"), ("u2", "i1"), ("u2", "i2"), ("u2", "i3"), ("u3", "i3"), ("u3", "i4")]
        for a, b in edges:
            line(s, upos[a][0], upos[a][1], ipos[b][0], ipos[b][1], color=GREEN, w=1.75)
        line(s, upos["u1"][0], upos["u1"][1], ipos["i3"][0], ipos["i3"][1], color=ORANGE, w=2.5, dash="dash")
        textbox(s, x, gy + emu(3.75), w, emu(0.45), [Para(md_runs("u1 behaves like u2  →  **recommend i3 to u1** (dashed)", size=16, color=INK), align="ctr", lnspc=20)])
        cw = (w - emu(0.3)) / 2
        cy2 = gy + emu(4.55)
        light_card(s, x, cy2, cw, y + h - cy2, label="User-based",
                   paras=[P("similar users → their liked items", size=14)], pad=(0.25, 0.5, 0.25, 0.15), label_size=14)
        light_card(s, x + cw + emu(0.3), cy2, cw, y + h - cy2, label="Item-based",
                   paras=[P("items co-liked with the user's items", size=14)], pad=(0.25, 0.5, 0.25, 0.15), label_size=14)

    approach_slide("Collaborative Filtering",
                   ["Recommends items using the **preferences and behaviour of similar users**.",
                    "Finds patterns in **user-item interactions**: ratings, clicks, purchases.",
                    "Can be **user-based** or **item-based**; needs no item content at all.",
                    "The base idea behind matrix factorisation and graph recommenders."],
                   "It struggles with new users or new items because of limited interaction data (cold start).",
                   diag_cf, N("ap_cf"), cite(22))

    def diag_hybrid(s, x, y, w, h):
        textbox(s, x, y, w, emu(0.4), [Para([Run("HYBRID  ·  MATRIX FACTORISATION", font="xbold", size=14, color=ORANGE, spc=1.4)], align="ctr", lnspc=18)])
        cw = (w - emu(0.3)) / 2
        by = y + emu(0.65)
        chip(s, x, by, cw, emu(1.0), "Content signals", fill=GREEN, size=17, sub="features · metadata", sub_size=13)
        chip(s, x + cw + emu(0.3), by, cw, emu(1.0), "Collaborative signals", fill="1F5C99", size=17, sub="ratings · clicks", sub_size=13)
        fy = by + emu(1.45)
        arrow(s, x + cw / 2, by + emu(1.0), x + w / 2 - emu(0.3), fy, color=GREEN)
        arrow(s, x + cw + emu(0.3) + cw / 2, by + emu(1.0), x + w / 2 + emu(0.3), fy, color=GREEN)
        chip(s, x + w / 2 - emu(2.0), fy, emu(4.0), emu(0.95), "Hybrid recommender", fill=ORANGE, size=18)
        # MF block
        my = fy + emu(1.45)
        textbox(s, x, my, w, emu(0.4), [Para([Run("MATRIX FACTORISATION", font="xbold", size=13, color=GREEN, spc=1.4)], align="ctr", lnspc=16)])
        equation(s, x, my + emu(0.4), w, emu(0.9), r"R_{m \times n} \;\approx\; P_{m \times k}\, Q_{n \times k}^{\top}, \qquad \hat r_{ui} = p_u^{\top} q_i", size=22, color=INK)
        bar = rrect(s, x, my + emu(1.45), w, y + h - (my + emu(1.45)), fill=TINT, radius=emu(0.25))
        shape_text(bar, [Para(md_runs("Compact and effective, but the **k latent factors have no readable meaning**: this is where the interpretability gap starts.", size=16, color=INK), align="ctr", lnspc=21)],
                   anchor="ctr", insets=(emu(0.35), emu(0.1), emu(0.35), emu(0.1)))

    approach_slide("Hybrid Approaches and Matrix Factorisation",
                   ["**Hybrid:** combines content-based and collaborative methods to reduce the weaknesses of each.",
                    "Handles limited data, over-specialisation and part of the cold-start problem.",
                    "**Matrix factorisation (MF):** the interaction matrix R is split into user and item factors P and Q.",
                    "MF made recommendation accurate and scalable; it is the standard baseline of the field."],
                   "The latent factors are compact but hidden: a good score cannot be traced back to a factor a person understands.",
                   diag_hybrid, N("ap_hybrid"), cite(10, 22))

    def diag_graph(s, x, y, w, h):
        textbox(s, x, y, w, emu(0.4), [Para([Run("GRAPH  ·  HYPERGRAPH", font="xbold", size=14, color=ORANGE, spc=1.4)], align="ctr", lnspc=18)])
        cw = (w - emu(0.3)) / 2
        gy = y + emu(0.6)
        gh = emu(3.9)
        # left: pairwise graph
        light_card(s, x, gy + emu(0.25), cw, gh, label="Graph: pairwise edges", paras=None, label_size=15)
        cx = x + cw / 2
        pts = {"u": (cx - emu(0.9), gy + emu(1.2)), "i1": (cx + emu(0.9), gy + emu(0.9)), "i2": (cx + emu(0.9), gy + emu(2.1)), "u2": (cx - emu(0.9), gy + emu(2.7)), "i3": (cx + emu(0.9), gy + emu(3.3))}
        for a, b in [("u", "i1"), ("u", "i2"), ("u2", "i2"), ("u2", "i3")]:
            line(s, pts[a][0], pts[a][1], pts[b][0], pts[b][1], color=GREEN, w=1.75)
        for k, (px, py) in pts.items():
            badge(s, px - emu(0.28), py - emu(0.28), emu(0.56), k, fill=GREEN if k.startswith("u") else ORANGE, color=WHITE, size=12)
        # right: hyperedge
        x2 = x + cw + emu(0.3)
        light_card(s, x2, gy + emu(0.25), cw, gh, label="Hypergraph: one edge, many nodes", paras=None, label_size=15)
        cx2 = x2 + cw / 2
        ellipse(s, cx2 - emu(1.55), gy + emu(0.85), emu(3.1), emu(1.9), fill="E4EBF4", line=GREEN)
        for k, (px, py), f in [("u", (cx2 - emu(0.9), gy + emu(1.5)), GREEN), ("i", (cx2 + emu(0.1), gy + emu(1.25)), ORANGE), ("c", (cx2 + emu(0.9), gy + emu(2.0)), INK)]:
            badge(s, px - emu(0.28), py - emu(0.28), emu(0.56), k, fill=f, color=WHITE, size=12)
        textbox(s, x2 + emu(0.2), gy + emu(2.95), cw - emu(0.4), emu(1.0), [Para(md_runs("e = {user, item, context}\n**uniform weight** in standard models", size=14, color=INK), align="ctr", lnspc=18)])
        bar = rrect(s, x, gy + gh + emu(0.55), w, y + h - (gy + gh + emu(0.55)), fill=GREEN, radius=emu(0.25))
        shape_text(bar, [Para(md_runs("Multi-hop and higher-order relations improve ranking, but **message importance stays implicit or uniform**: the assumption DyHuCoG challenges.", size=16, color=WHITE), align="ctr", lnspc=21)],
                   anchor="ctr", insets=(emu(0.35), emu(0.1), emu(0.35), emu(0.1)))

    approach_slide("Graph-Based and Hypergraph Recommenders",
                   ["Represent users, items and their interactions as **nodes and edges** in a graph.",
                    "Use **message passing** (LightGCN, HCCF, HPCF) to reach multi-hop neighbours.",
                    "**Hypergraphs** connect more than two nodes at once: user, item and context in one hyperedge.",
                    "State of the art in accuracy on sparse benchmarks such as MovieLens-1M and Amazon-Book."],
                   "Large graphs cost compute and memory, and all messages are treated as equally important and unexplained.",
                   diag_graph, N("ap_graph"), cite(12, 13, 14, 16))

    # --- Limitations ---------------------------------------------------------
    s, top = content_slide(ctx, "Limitations of Classical Recommenders & Unsupervised Models", eyebrow="Context & Problematic",
                           tabs=APTABS, active="Problematic", notes=N(10), refs=cite(23, 21))
    lims = [("Data sparsity & scalability", "The user-item matrix is almost empty, so there is very little signal to learn from."),
            ("Cold-start", "New users and items are at a disadvantage: no history to learn from."),
            ("Popularity bias & lack of diversity", "Exposure leads to interaction, which leads to more exposure: a filter-bubble loop."),
            ("Absence of interpretability", "The most basic limit, and the one this thesis targets.")]
    cells = grid(4, 4, L, top + emu(0.1), W, emu(3.3), gap=emu(0.3))
    for i, ((h1, body), (x, y, w, h)) in enumerate(zip(lims, cells)):
        f = ORANGE if i == 3 else GREEN
        box = rrect(s, x, y, w, h, fill=f, radius=emu(0.3))
        shape_text(box, [Para([Run(f"0{i+1}", font="xbold", size=26, color=YELLOW if i < 3 else WHITE)], lnspc=30),
                         Para([Run(h1, font="xbold", size=21, color=WHITE)], lnspc=25, spcbef=6),
                         Para([Run(body, font="body", size=17, color="F1EDE6")], lnspc=21, spcbef=8)],
                   anchor="t", insets=(emu(0.35), emu(0.35), emu(0.3), emu(0.25)))
    cy = top + emu(0.1) + emu(3.3) + emu(0.45)
    light_card(s, L, cy + emu(0.25), W, CB - cy - emu(0.45), label="For clustering specifically, the situation is even harder",
               paras=bullets(["Methods give a **local OR a global** explanation, not both.",
                              "They **struggle to scale**, and explanations rarely stay **consistent across levels of detail**.",
                              "**The gap:** no faithful local + global explanation, poor scaling, and no consistency across levels. This is exactly what this thesis works on."],
                             size=21, gap0=8), pad=(0.55, 0.7, 0.5, 0.3))

    # --- Three structuring limitations ---------------------------------------
    s, top = content_slide(ctx, "Three Main Limitations: Problem Statement", eyebrow="Context & Problematic",
                           tabs=APTABS, active="Problematic", notes=N(11), refs=cite(21, 24))
    probs = [("1", "Lack of explainability", "Complex models are still hard to explain in a way that is **faithful and actionable**."),
             ("2", "Difficulty of scaling", "Local explanations do not carry over to **multi-level structures or large datasets**: a method that works on a toy partition may break on hundreds of thousands of nested records."),
             ("3", "Weak integration into learning", "Most explanations stay **post-hoc**: they do not shape how the model learns, nor the **accuracy / diversity / context trade-off**.")]
    cells = grid(3, 3, L, top + emu(0.1), W, emu(3.9), gap=emu(0.35))
    for (num, h1, body), (x, y, w, h) in zip(probs, cells):
        box = rrect(s, x, y, w, h, fill=GREEN, radius=emu(0.32))
        badge(s, x + emu(0.35), y + emu(0.35), emu(0.75), num, fill=YELLOW, color=INK, size=24)
        fit_textbox(s, x + emu(0.35), y + emu(1.3), w - emu(0.7), h - emu(1.5),
                    [H(h1, size=24, color=WHITE), P(body, size=19, color="F1EDE6", spcbef=8)], min_scale=0.7)
    gy = top + emu(0.1) + emu(3.9) + emu(0.4)
    box = rrect(s, L, gy, W, CB - gy - emu(0.15), fill=None, line=ORANGE, line_w=2.5, radius=emu(0.3))
    fit_textbox(s, L + emu(0.5), gy + emu(0.25), W - emu(1.0), CB - gy - emu(0.15) - emu(0.5),
                [Para([Run("THESIS GAP", font="xbold", size=14, color=ORANGE, spc=1.8)], lnspc=18),
                 P("The literature still lacks **one cooperative-attribution framework** that explains clustering faithfully, stays consistent across levels, and then works as an **in-training signal** in recommendation. "
                   "**Claim:** Shapley-value attribution can be that framework.", size=21, spcbef=6)], anchor="ctr", min_scale=0.7)

    # --- Research questions --------------------------------------------------
    s, top = content_slide(ctx, "Research Questions (RQ1–RQ5) and Overall Aim", eyebrow="Context & Problematic",
                           tabs=["Approaches", "Problematic", "Contributions"], active="Problematic", notes=N(12))
    aim = rrect(s, L, top, W, emu(0.95), fill=GREEN, radius=emu(0.25))
    shape_text(aim, [Para(md_runs("**Aim:** develop, justify and evaluate a cooperative-game view of XAI for clustering and recommendation, "
                                  "using Shapley attribution both as an **explanation method** and as an **in-training signal**.", size=20, color=WHITE), align="ctr", lnspc=26)],
               anchor="ctr", insets=(emu(0.5), emu(0.1), emu(0.5), emu(0.1)))
    rqs = [("RQ1", "How can Shapley values explain black-box clustering **faithfully at instance and cluster level**?", "C1"),
           ("RQ2", "How can this extend to **large-scale, multi-level clustering** while staying feasible and consistent?", "C2"),
           ("RQ3", "Can cooperative attribution move **beyond post-hoc** and become part of how graph recommenders learn?", "C3"),
           ("RQ4", "Can a recommender **improve ranking accuracy, context and diversity at the same time** when importance comes from a cooperative-game utility?", "C3"),
           ("RQ5", "What do we gain when clustering explanation and recommendation learning are **two stages of one cooperative-game view**?", "Thesis")]
    y = top + emu(1.2)
    rh = (CB - y - emu(0.15) - emu(0.14) * 4) / 5
    for i, (tag, q, c) in enumerate(rqs):
        yy = y + i * (rh + emu(0.14))
        rrect(s, L, yy, W, rh, fill=TINT if i % 2 == 0 else TINT2, radius=emu(0.2))
        chip(s, L + emu(0.2), yy + emu(0.14), emu(1.25), rh - emu(0.28), tag, fill=ORANGE if i < 4 else INK, color=WHITE, size=19, radius=emu(0.15))
        fit_textbox(s, L + emu(1.7), yy, W - emu(4.0), rh, [P(q, size=20)], anchor="ctr", min_scale=0.7)
        chip(s, R - emu(2.1), yy + emu(0.14), emu(1.9), rh - emu(0.28), "→ " + c, fill=GREEN, color=WHITE, size=16, radius=emu(0.15))

    # --- Three contributions -------------------------------------------------
    s, top = content_slide(ctx, "The Three Contributions", eyebrow="Context & Problematic",
                           tabs=["Approaches", "Problematic", "Contributions"], active="Contributions", notes=N(13))
    cons = [("C1", "Explainable black-box clustering", "PCA → K-Means → LightGBM → TreeSHAP pipeline.", "Wine Quality", "Faithful instance- and cluster-level feature attribution.", "RQ1"),
            ("C2", "Enhanced multi-level XAI", "Large-scale clustering with cross-level SHAP aggregation (Prop. 6.1).", "Beijing Air Quality", "Attribution stays consistent across levels and at scale.", "RQ2"),
            ("C3", "DyHuCoG", "Dynamic Hypergraph Cooperative Game for preference-aware recommendation.", "MovieLens-1M · Amazon-Book", "Preference-aware Monte Carlo Shapley as an in-training signal.", "RQ3 · RQ4")]
    cells = grid(3, 3, L, top + emu(0.1), W, emu(4.9), gap=emu(0.35))
    for i, ((tag, h1, body, ds, res, rq), (x, y, w, h)) in enumerate(zip(cons, cells)):
        f = [GREEN, "1F5C99", ORANGE][i]
        box = rrect(s, x, y, w, h, fill=f, radius=emu(0.32))
        textbox(s, x + emu(0.4), y + emu(0.3), w - emu(0.8), emu(0.7), [Para([Run(tag, font="title", size=40, color=YELLOW if i < 2 else WHITE)], lnspc=44)])
        pill(s, x + w - emu(2.2), y + emu(0.38), rq, active=True, h=emu(0.42), size=15, fill=WHITE, text_color=f, line_color=WHITE)
        fit_textbox(s, x + emu(0.4), y + emu(1.15), w - emu(0.8), h - emu(1.3),
                    [H(h1, size=23, color=WHITE), P(body, size=18, color="F1EDE6", spcbef=6),
                     Para([Run(ds.upper(), font="xbold", size=13, color=YELLOW if i < 2 else WHITE, spc=1.4)], lnspc=17, spcbef=14),
                     P(res, size=18, color=WHITE, spcbef=4)], min_scale=0.7)
    gy = top + emu(0.1) + emu(4.9) + emu(0.4)
    bar = rrect(s, L, gy, W, CB - gy - emu(0.15), fill=TINT, radius=emu(0.25))
    shape_text(bar, [Para(md_runs("**Thesis claim:** cooperative game theory works as **one shared attribution view** for explanation, optimisation and action: three steps that build on each other, not three unrelated papers.", size=21, color=INK), align="ctr", lnspc=27)],
               anchor="ctr", insets=(emu(0.5), emu(0.1), emu(0.5), emu(0.1)))

    # v10: 'Our Thesis in One View' removed. It restated the C1/C2/C3 cards of the
    # previous slide in prose; the thesis spine now appears once there and once in
    # the synthesis (the reference deck states its claim once, in the synthesis).

    # ======================================================================
    # SECTION 3 — EXPERIMENTAL PROTOCOL
    # ======================================================================
    section_slide(ctx, "03", "Experimental Protocol", "One shared protocol so that the three contributions can be read together",
                  [("Datasets", "Wine Quality and Beijing Air Quality for clustering; MovieLens-1M and Amazon-Book for recommendation."),
                   ("Baselines & metrics", "LIME for clustering explanation; MF → HPCF for recommendation; NDCG@20, Recall, Coverage, ILD, Silhouette, Davies–Bouldin."),
                   ("Reproducibility", "Fixed seeds, time-ordered user-level splits, early stopping, standard academic hardware (i9-14900K + RTX 4090).")],
                  notes=N(15))

    # --- Dataset tabs -------------------------------------------------------
    # v10: the 'Datasets Used Throughout' overview table is removed. Slide 18
    # already lists the four datasets and the four cards below give every
    # statistic; the reference deck likewise has no dataset-overview slide in
    # the main flow (its 'General Specifications' sits in the backup).
    PTABS = ["Datasets", "Metrics", "Hardware"]

    # --- Dataset cards: spec table + sample rows (example-deck style) ----------
    def dataset_card(title, intro, spec_rows, sample_rows, sample_widths, why, notes, refs_, sample_note=None):
        s, top = content_slide(ctx, title, eyebrow="Experimental Protocol", tabs=PTABS, active="Datasets", notes=notes, refs=refs_)
        lw = emu(7.6)
        fit_textbox(s, L, top, lw, emu(3.0), bullets(intro, size=19, gap0=8), min_scale=0.7)
        dx = L + lw + emu(0.5)
        dw = R - dx
        gf, th = table(s, dx, top, dw, [["Specification", title.split(":")[0]]] + spec_rows, col_widths=[2.2, 2.0], size=16, head_size=16, row_h=emu(0.42), pad=0.08)
        sy = max(top + emu(3.15), top + th + emu(0.35))
        textbox(s, L, sy, W, emu(0.35), [Para([Run("SAMPLE RECORDS" + (f"  ·  {sample_note}" if sample_note else ""), font="xbold", size=13, color=ORANGE, spc=1.5)], lnspc=16)])
        gf2, th2 = table(s, L, sy + emu(0.38), W, sample_rows, col_widths=sample_widths, size=15, head_size=15, row_h=emu(0.4), pad=0.07,
                         align=["ctr"] * len(sample_rows[0]), header_align=["ctr"] * len(sample_rows[0]), first_col_bold=False)
        wy = sy + emu(0.38) + th2 + emu(0.3)
        if CB - wy - emu(0.3) > emu(0.6):
            bar = rrect(s, L, wy, W, CB - wy - emu(0.3), fill=TINT, radius=emu(0.22))
            shape_text(bar, [Para(md_runs(why, size=17, color=INK), align="ctr", lnspc=22)], anchor="ctr", insets=(emu(0.4), emu(0.05), emu(0.4), emu(0.05)))
        return s

    dataset_card("Wine Quality: Portuguese Vinho Verde",
                 ["**4,898 white-wine samples** described by **11 physicochemical measurements** and a sensory quality score (UCI repository).",
                  "Small, dense and chemically correlated: the ideal place to check that an explanation lands on **variables a wine expert understands**.",
                  "Used for **Contribution I**: single-level clustering, then Shapley attribution back to the chemistry."],
                 [["Observations", "4,898"], ["Features", "11 numeric"], ["Target (not used for clustering)", "quality 3 to 9"], ["Missing values", "none"], ["Scale of features", "standardised"], ["Selected clusters", "k* = 3"]],
                 [["fixed acidity", "volatile acidity", "citric acid", "residual sugar", "chlorides", "free SO₂", "total SO₂", "density", "pH", "sulphates", "alcohol", "quality"],
                  ["7.0", "0.27", "0.36", "20.7", "0.045", "45", "170", "1.0010", "3.00", "0.45", "8.8", "6"],
                  ["6.3", "0.30", "0.34", "1.6", "0.049", "14", "132", "0.9940", "3.30", "0.49", "9.5", "6"],
                  ["8.1", "0.28", "0.40", "6.9", "0.050", "30", "97", "0.9951", "3.26", "0.44", "10.1", "6"]],
                 [1.1, 1.2, 1.0, 1.15, 1.0, 0.9, 0.9, 0.9, 0.7, 0.9, 0.8, 0.7],
                 "Every column is a **lab measurement with a physical meaning**; that is exactly the vocabulary in which the Shapley explanation is returned.",
                 N("ds_wine"), cite(19), sample_note="first rows of the public file")

    dataset_card("Beijing Multi-Site Air Quality",
                 ["**383,585 hourly records** from Beijing monitoring stations, March 2013 to February 2017 (UCI repository).",
                  "**11 modelling variables:** six pollutants (PM2.5, PM10, SO₂, NO₂, CO, O₃) and weather (temperature, pressure, dew point, rain, wind speed).",
                  "Large, noisy, varies with season and weather: the stress test for **Contribution II** (scale + multi-level structure)."],
                 [["Observations", "383,585 hourly"], ["Period", "2013 to 2017"], ["Variables used", "11 (6 pollutants + 5 weather)"], ["Structure", "coarse regimes → sub-clusters"], ["Selected clusters", "k = 3 → 9 sub-clusters"], ["Silhouette", "≈ 0.63"]],
                 [["station", "date · hour", "PM2.5", "PM10", "SO₂", "NO₂", "CO", "O₃", "TEMP", "PRES", "DEWP", "WSPM"],
                  ["Aotizhongxin", "2013-03-01 · 00h", "4", "4", "4", "7", "300", "77", "-0.7", "1023.0", "-18.8", "4.4"],
                  ["Aotizhongxin", "2013-03-01 · 01h", "8", "8", "4", "7", "300", "77", "-1.1", "1023.2", "-18.2", "4.7"],
                  ["Aotizhongxin", "2013-03-01 · 02h", "7", "7", "5", "10", "300", "73", "-1.1", "1023.5", "-18.2", "5.6"]],
                 [1.5, 1.7, 0.8, 0.8, 0.7, 0.7, 0.7, 0.7, 0.8, 0.9, 0.8, 0.8],
                 "Pollutant and weather columns sit **side by side**, so the explanation can show that the weather is what sets the regime.",
                 N("ds_beijing"), cite(19), sample_note="first rows of the Aotizhongxin station file")

    dataset_card("MovieLens-1M",
                 ["**About 1 million ratings** from **6,040 users** on **3,706 movies** (GroupLens, 2000).",
                  "The standard benchmark for collaborative filtering for two decades: LightGCN, HCCF, HPCF and most graph recommenders report on it.",
                  "Comparatively **dense** (0.0447); ratings > 3 become positive implicit feedback. Genre is the context proxy."],
                 [["Users", "6,040"], ["Items", "3,706 movies"], ["Interactions", "1,000,209"], ["Density", "≈ 0.0447"], ["Rating scale", "1 to 5 stars"], ["Min. interactions / user", "20"]],
                 [["UserID", "MovieID", "Title", "Genres", "Rating", "Timestamp"],
                  ["1", "1193", "One Flew Over the Cuckoo's Nest (1975)", "Drama", "5", "978300760"],
                  ["1", "661", "James and the Giant Peach (1996)", "Animation · Children's · Musical", "3", "978302109"],
                  ["1", "914", "My Fair Lady (1964)", "Musical · Romance", "3", "978301968"],
                  ["1", "3408", "Erin Brockovich (2000)", "Drama", "4", "978300275"]],
                 [1.0, 1.0, 4.2, 3.4, 0.9, 1.4],
                 "Using this benchmark keeps the results **directly comparable** with prior work in graph-based recommendation.",
                 N("ds_ml1m"), cite(20), sample_note="first rows of ratings.dat joined with movies.dat")

    dataset_card("Amazon-Book",
                 ["**52,643 users**, **91,599 books** and **2,984,108 interactions** from Amazon review data (McAuley Lab, UCSD).",
                  "Extremely **sparse** (density ≈ 0.0006): the user-item matrix is almost empty.",
                  "Included to test whether Shapley-guided weighting **helps most when the signal is weakest**; the large-scale benchmark of Contribution III."],
                 [["Users", "52,643"], ["Items", "91,599 books"], ["Interactions", "2,984,108"], ["Density", "≈ 0.0006"], ["Feedback", "implicit (review = interaction)"], ["Context proxy", "book category"]],
                 [["user_id", "item_id (ASIN)", "category", "rating", "review summary"],
                  ["A1B2C3", "B000123XYZ", "Literature & Fiction", "5", "Could not put it down"],
                  ["A4D5E6", "B000456ABC", "Science & Math", "4", "Clear and well written"],
                  ["A7F8G9", "B000789DEF", "History", "3", "Good but slow in the middle"]],
                 [1.2, 1.6, 2.0, 0.8, 3.0],
                 "The **0.0447 vs 0.0006** density gap between the two recommendation datasets is the core of the robustness argument.",
                 N("ds_amazon"), cite(20), sample_note="illustrative rows in the format of the public file")

    # --- Splitting & preprocessing -------------------------------------------
    s, top = content_slide(ctx, "Data Splitting & Preprocessing", eyebrow="Experimental Protocol",
                           tabs=PTABS, active="Datasets", notes=N(18), refs=cite(12, 14))
    cw = (W - emu(0.4)) / 2
    ch = CB - top - emu(0.45)
    card(s, L, top + emu(0.25), cw, ch, label="Clustering (C1, C2)",
         paras=bullets(["**Five-fold cross-validation** for surrogate / attribution stability.",
                        "Feature standardisation; PCA used only as a geometric and visual check.",
                        "Multi-criteria k selection: elbow, Silhouette, Davies–Bouldin.",
                        "Surrogate fidelity floor: **macro-F1 ≈ 0.82**."], size=20, color=WHITE, c0=YELLOW, c1=YELLOW, gap0=10), pad=(0.55, 0.7, 0.5, 0.3))
    light_card(s, L + cw + emu(0.4), top + emu(0.25), cw, ch, label="Recommendation (C3)",
               paras=bullets(["**User-level, time-ordered split:** 70 % train / 10 % validation / 20 % test.",
                              "**Leave-one-out:** the latest test positive per user is the target, ranked against negatives.",
                              "Implicit conversion: MovieLens-1M ratings > 3 treated as positive.",
                              "Popularity-aware negative sampling **q(i) ∝ f_{i}^{η}** for harder negatives.",
                              "Reproducibility: seeds {42, 43, 44, 45, 46}; early-stopping patience 20."], size=20, gap0=10), pad=(0.55, 0.7, 0.5, 0.3))

    # --- Baselines ------------------------------------------------------------
    s, top = content_slide(ctx, "Baselines", eyebrow="Experimental Protocol", tabs=PTABS, active="Metrics", notes=N(19), refs=cite(7, 10, 11, 12, 13, 14, 15))
    rows = [["Family", "Baseline", "What it represents", "Used in"],
            ["Explanation", "LIME surrogate pipeline", "Local surrogate explanation; the standard alternative to SHAP", "C1, C2"],
            ["Classical", "MF (BPR)", "Matrix factorisation with pairwise ranking loss", "C3"],
            ["Neural", "NCF", "Neural collaborative filtering (MLP on embeddings)", "C3"],
            ["Graph", "LightGCN", "Simplified graph convolution on the user-item graph", "C3"],
            ["Graph + contrastive", "RecDCL", "Dual contrastive learning for recommendation (2024)", "C3"],
            ["Hypergraph", "HCCF", "Hypergraph contrastive collaborative filtering (2022)", "C3"],
            ["Hypergraph", "HPCF  (strongest reference)", "Hypergraph projection enhanced collaborative filtering (2025)", "C3"]]
    gf, th = table(s, L, top, W, rows, col_widths=[2.2, 3.2, 6.6, 1.4], size=17, head_size=17, row_h=emu(0.58), align=["l", "l", "l", "ctr"], header_align=["l", "l", "l", "ctr"])
    by = top + th + emu(0.4)
    statement(s, L, by + emu(0.2), W, CB - by - emu(0.55), "Why this set",
              "Classical, neural, graph and hypergraph families together, so the effect of **cooperative attribution** is not confused with a lucky model choice. HPCF is the strongest reference; all baselines were finalised in early 2026.",
              fill=GREEN, size=19)

    # --- Metrics: formula table (example-deck style) --------------------------
    s, top = content_slide(ctx, "Evaluation Metrics", eyebrow="Experimental Protocol", tabs=PTABS, active="Metrics", notes=N("metrics"), refs=cite(17, 23))
    metrics = [
        ("NDCG@K  (main)", r"\mathrm{NDCG@}K = \dfrac{1}{\mathrm{IDCG@}K}\, {\sum}_{i=1}^{K} \dfrac{\mathrm{rel}_i}{\log_2 (i+1)}", "Ranking quality; rewards relevant items placed near the top of the list."),
        ("Recall@K", r"\mathrm{Recall@}K = \dfrac{|\, L_u^{K} \cap \mathcal{R}_u \,|}{|\, \mathcal{R}_u \,|}", "Share of the user's relevant items that appear in the top-K list."),
        ("Precision@K", r"\mathrm{Precision@}K = \dfrac{|\, L_u^{K} \cap \mathcal{R}_u \,|}{K}", "Share of the top-K list that is relevant."),
        ("Catalogue Coverage", r"\mathrm{Cov} = \dfrac{\left|\, {\bigcup}_{u} L_u^{K} \,\right|}{\left|\, I \,\right|}", "System-level diversity: how much of the catalogue is ever recommended."),
        ("Intra-List Diversity", r"\mathrm{ILD}(L_u) = \dfrac{2}{K(K-1)} {\sum}_{i<j} \left(1 - \mathrm{sim}(i,j)\right)", "List-level diversity; built into the DyHuCoG coalition utility."),
        ("Silhouette", r"s(x) = \dfrac{b(x) - a(x)}{\max\{a(x),\, b(x)\}}, \qquad s \in [-1, 1]", "Clustering quality; the value function of the clustering game (C1, C2)."),
        ("Davies–Bouldin", r"\mathrm{DB} = \dfrac{1}{k} {\sum}_{c=1}^{k} \max_{c' \neq c} \dfrac{\sigma_c + \sigma_{c'}}{d(\mu_c, \mu_{c'})}", "Cluster overlap; lower is better."),
    ]
    c1w, c2w = emu(2.9), emu(7.1)
    c3w = W - c1w - c2w
    hy = top
    rect(s, L, hy, W, emu(0.42), fill=GREEN)
    for x, w, t in [(L, c1w, "Metric"), (L + c1w, c2w, "Formula"), (L + c1w + c2w, c3w, "Why it is used")]:
        textbox(s, x + emu(0.15), hy, w - emu(0.3), emu(0.42), [Para([Run(t, font="bold", size=15, color=WHITE)], lnspc=18)], anchor="ctr")
    rh = (CB - hy - emu(0.42) - emu(0.62)) / len(metrics)
    yy = hy + emu(0.42)
    for i, (name, tex, why) in enumerate(metrics):
        rect(s, L, yy, W, rh, fill=WHITE if i % 2 == 0 else TINT)
        textbox(s, L + emu(0.15), yy, c1w - emu(0.3), rh, [Para([Run(name, font="bold", size=16, color=INK)], lnspc=19)], anchor="ctr")
        equation(s, L + c1w + emu(0.1), yy + emu(0.03), c2w - emu(0.2), rh - emu(0.06), tex, size=14, color=INK, align="l")
        textbox(s, L + c1w + c2w + emu(0.15), yy, c3w - emu(0.3), rh, [Para([Run(why, font="body", size=14, color=INK)], lnspc=17)], anchor="ctr")
        line(s, L, yy + rh, R, yy + rh, color=RULE, w=1.0)
        yy += rh
    textbox(s, L, yy + emu(0.08), W, emu(0.6), [Para(md_runs("**Notation:** L_{u}^{K} = top-K list of user u; ℛ_{u} = relevant (held-out) items of u; rel_{i} ∈ {0,1}; a(x), b(x) = mean intra- and nearest-cluster distance; σ_{c}, μ_{c} = spread and centroid of cluster c. Reported at K ∈ {5, 10, 20}; NDCG@20 is the main measure.", size=13, color=MUTED), lnspc=16)])

    # --- Hardware & software: table by contribution ---------------------------
    s, top = content_slide(ctx, "Hardware & Software", eyebrow="Experimental Protocol", tabs=PTABS, active="Hardware", notes=N(20))
    rows = [["Contribution", "Hardware", "CPU / GPU", "RAM", "Storage", "Main software"],
            ["I  ·  Wine clustering", "Workstation", "Intel Core i9-14900K (24 cores)", "48 GB", "2 TB SSD", "scikit-learn, LightGBM, SHAP, Altair"],
            ["II  ·  Beijing multi-level", "Workstation", "Intel Core i9-14900K (24 cores)", "48 GB (full dataset in memory)", "2 TB SSD", "scikit-learn, LightGBM, SHAP"],
            ["III  ·  DyHuCoG", "Workstation + GPU", "NVIDIA GeForce RTX 4090 (24 GB)", "48 GB", "2 TB SSD", "Python 3.8, PyTorch 2.0.1, NumPy / SciPy"]]
    gf, th = table(s, L, top, W, rows, col_widths=[2.6, 2.0, 3.4, 2.6, 1.4, 3.6], size=17, head_size=17, row_h=emu(0.85))
    source_caption(s, L, top + th + emu(0.08), W, "Table 4.2 (thesis): hardware and software configuration, arranged here by contribution.")
    cy = top + th + emu(0.6)
    cw = (W - emu(0.4)) / 2
    ch = CB - cy - emu(0.55)
    card(s, L, cy + emu(0.25), cw, ch, label="Why it matters",
         paras=bullets(["The hardware explains the **runtime figures** quoted later (DyHuCoG ≈ 1.78× HPCF training time on MovieLens-1M).",
                        "Metrics at K ∈ {5, 10, 20}; five seeds; early stopping on validation NDCG@20."], size=17, color=WHITE, c0=YELLOW, c1=YELLOW, gap0=6), pad=(0.5, 0.6, 0.45, 0.2))
    light_card(s, L + cw + emu(0.4), cy + emu(0.25), cw, ch, label="Scope",
               paras=bullets(["**Everything runs on standard academic hardware**; nothing needs industrial-scale compute.",
                              "Clustering, surrogates, SHAP and DyHuCoG share the same seeds and splits."], size=17, gap0=6), pad=(0.5, 0.6, 0.45, 0.2))

    # ======================================================================
    # SECTION 4 — CONTRIBUTION I
    # ======================================================================
    C1TABS = ["Objectives", "Methodology", "Results", "Findings"]
    C1 = "Contribution I: Explainable Black-Box Clustering"
    section_slide(ctx, "04", "Contribution I", "Explainable black-box clustering with Shapley values  ·  answers RQ1",
                  [("Objectives", "Cluster-level explanation that keeps feature-level attribution in the original feature space; justify Shapley over LIME."),
                   ("Methodology", "Features are players; Silhouette is the value function; a LightGBM surrogate bridges K-Means to exact TreeSHAP."),
                   ("Results", "Wine Quality: k^{*} = 3 chosen for interpretability; density → pH → acidity → SO₂ → alcohol recovered as a chemically meaningful ranking.")],
                  notes=N(21))

    # --- C1 research gap ------------------------------------------------------
    gap_slide(ctx, C1, C1TABS, "Objectives",
              ["Shapley explanation is **standard in supervised tasks** [5, 6], but clustering is still much less explained.",
               "Existing clustering-interpretability methods favour **local or global** explanation, not both.",
               "They often fail to scale or to stay **consistent across clusters**.",
               "Clustering is the hardest test bed: the model creates its own structure, so cluster meaning must be worked out after the fact.",
               "Local surrogates such as LIME [7] give no guarantee that the credit assigned to a feature is fair or stable."],
              "There is no principled, axiomatic way to explain **why a black-box clustering put an observation in a given cluster**, in the original feature space and consistently across clusters.",
              N(22), cite(5, 6, 7))

    # --- C1 RQ1 -> objectives ---------------------------------------------------
    rq_slide(ctx, C1, C1TABS, "Objectives", "RQ1",
             "How can Shapley values explain black-box clustering **faithfully**, at both instance level and cluster level?",
             [("O1  ·  Cluster-level explanation", "A pipeline that yields a cluster-level explanation while keeping **feature-level attribution**.", "Fig. 5.2, cluster profiles"),
              ("O2  ·  Original feature space", "Attribution in the **original variables** (density, pH, acidity, sulfur dioxide, alcohol), not in a reduced latent space.", "Fig. 5.1, global ranking"),
              ("O3  ·  Justify Shapley over LIME", "An argument from the **four axioms** for why the cooperative concept is the right one.", "SHAP vs LIME comparison")],
             N(23))

    # ======================================================================
    # --- Methodology primer: the cooperative game + the Shapley value, one slide
    # v10: the three "Technical Deep Dive" slides are collapsed into a single
    # methodology slide. "The Same Game, Three Times" is dropped outright (the
    # contribution cards and the synthesis already carry that map), and the
    # six-arrival-order table is reduced to the one worked row that explains it.
    s, top = content_slide(ctx, "The Cooperative Game and the Shapley Value", eyebrow=C1,
                           tabs=C1TABS, active="Methodology", notes=N("dd_game"), refs=cite(4, 5))
    lw = emu(8.4)
    fit_textbox(s, L, top, lw, emu(2.5), [
        H("Three ingredients", size=21, color=GREEN),
        *bullets(["**Players** N = {1, …, n}, and a **coalition** S ⊆ N: any group of them; there are 2^{n}.",
                  "**Characteristic function** v: 2^{N} → ℝ with v(∅) = 0: the value a coalition creates **on its own**.",
                  "**The question:** the grand coalition earns v(N), so **how should it be shared fairly**?"], size=19, gap0=8),
    ], min_scale=0.7)
    ey = top + emu(2.6)
    box = rrect(s, L, ey, lw, emu(0.95), fill=GREEN, radius=emu(0.22))
    textbox(s, L, ey + emu(0.07), lw, emu(0.26), [Para([Run("A COOPERATIVE GAME IS A PAIR", font="xbold", size=12, color=YELLOW, spc=1.5)], align="ctr", lnspc=14)])
    equation(s, L + emu(0.2), ey + emu(0.3), lw - emu(0.4), emu(0.6), r"(N, v), \qquad v : 2^{N} \to \mathbb{R}, \qquad v(\varnothing) = 0", size=19, color=WHITE)
    sy = ey + emu(1.15)
    statement(s, L, sy, lw, emu(1.5), "Toy example: a three-piece band",
              "Guitar, Voice and Drums are paid for a gig. Alone they earn **60, 40 and 20**; Guitar and Voice together earn **140**, more than their sum; all three earn **200**. A fair split must credit what a player **adds to the others**.",
              fill=ORANGE, size=17)
    fy = sy + emu(1.7)
    box = rrect(s, L, fy, lw, emu(2.15), fill=INK, radius=emu(0.28))
    textbox(s, L, fy + emu(0.14), lw, emu(0.28), [Para([Run("SHAPLEY VALUE OF PLAYER j  ·  SHAPLEY, 1953", font="xbold", size=12, color=YELLOW, spc=1.6)], align="ctr", lnspc=15)])
    equation(s, L + emu(0.2), fy + emu(0.44), lw - emu(0.4), emu(1.2),
             r"\varphi_j(v) = \sum_{S \subseteq N \setminus \{j\}} \dfrac{|S|!\,(n-|S|-1)!}{n!}\,\left[\, v(S \cup \{j\}) - v(S) \,\right]", size=20, color=WHITE)
    textbox(s, L, fy + emu(1.68), lw, emu(0.34), [Para([Run("average marginal contribution over every arrival order", font="body", size=15, color="D6E2EF")], align="ctr", lnspc=18)])

    dx = L + lw + emu(0.5)
    dw = R - dx
    textbox(s, dx, top - emu(0.05), dw, emu(0.32), [Para([Run("CHARACTERISTIC FUNCTION v(S) OF THE BAND", font="xbold", size=13, color=ORANGE, spc=1.5)], lnspc=16)])
    rows = [["Coalition S", "Who plays", "v(S)"],
            ["∅", "nobody", "0"],
            ["{G}", "Guitar alone", "60"],
            ["{V}", "Voice alone", "40"],
            ["{D}", "Drums alone", "20"],
            ["{G, V}", "Guitar + Voice", "140"],
            ["{G, D}", "Guitar + Drums", "100"],
            ["{V, D}", "Voice + Drums", "80"],
            ["{G, V, D}", "the whole band", "200"]]
    gf, th = table(s, dx, top + emu(0.32), dw, rows, col_widths=[1.5, 2.4, 1.1], size=15, head_size=14, row_h=emu(0.40),
                   align=["ctr", "l", "ctr"], header_align=["ctr", "l", "ctr"])
    ny = top + emu(0.32) + th + emu(0.22)
    bar = rrect(s, dx, ny, dw, emu(1.25), fill=TINT, radius=emu(0.2))
    shape_text(bar, [Para(md_runs("One arrival order, V → D → G: Voice adds **40**, Drums takes 40 → 80 (**+40**), Guitar completes the band, 80 → 200 (**+120**). Averaged over all six orders: **90 / 70 / 40**, which sums to 200.", size=15, color=INK), align="l", lnspc=19)],
               anchor="ctr", insets=(emu(0.3), emu(0.08), emu(0.3), emu(0.08)))
    ax = [("Efficiency", "the shares add up to v(N)"), ("Symmetry", "equal contributors, equal credit"),
          ("Null player", "adds nothing → gets nothing"), ("Additivity", "linear across games")]
    cells = grid(4, 2, dx, ny + emu(1.45), dw, emu(1.5), gap=emu(0.22), vgap=emu(0.2))
    for (h1, sub), (x, y, w, h) in zip(ax, cells):
        chip(s, x, y, w, h, h1, fill=TINT, color=INK, size=16, sub=sub, sub_size=12, sub_color=MUTED, radius=emu(0.2))
    wy = ny + emu(1.45) + emu(1.5) + emu(0.25)
    bar = rrect(s, dx, wy, dw, CB - wy - emu(0.25), fill=ORANGE, radius=emu(0.2))
    shape_text(bar, [Para(md_runs("**Why this rule:** Shapley proved it is the **only** allocation satisfying all four axioms at once.", size=16, color=WHITE), align="ctr", lnspc=20)],
               anchor="ctr", insets=(emu(0.3), emu(0.08), emu(0.3), emu(0.08)))


    # v10: 'The Same Game, Three Times in This Thesis' removed. It was the third
    # statement of the C1/C2/C3 map (after the contribution cards and before the
    # synthesis table) and it front-loaded C2/C3 detail the jury had not seen.
    # Its 'one definition, three value functions' line moves to the synthesis.

    # v10: 'Clustering as a Cooperative Game' folded into 'The Bridge' slide (its
    #     # v(S) = Silhouette definition now appears there as an equation).
    # --- C1 surrogate bridge -------------------------------------------------
    s, top = content_slide(ctx, "The Bridge: LightGBM Surrogate + TreeSHAP", eyebrow=C1, tabs=C1TABS, active="Methodology", notes=N(25))
    steps = [("K-Means", "cluster labels", GREEN), ("LightGBM", "multiclass surrogate", GREEN), ("TreeSHAP", "exact attribution", INK), ("Explanation", "original feature space", ORANGE)]
    n = len(steps)
    bw = emu(3.2)
    gap = (W - n * bw) / (n - 1)
    by = top + emu(0.1)
    bh = emu(1.3)
    for i, (t, sub, f) in enumerate(steps):
        x = L + i * (bw + gap)
        chip(s, x, by, bw, bh, t, fill=f, color=WHITE, size=22, sub=sub, sub_size=16, radius=emu(0.22))
        if i < n - 1:
            arrow(s, x + bw + emu(0.08), by + bh / 2, x + bw + gap - emu(0.08), by + bh / 2, color=GREEN, w=2.5)
    cy = by + bh + emu(0.45)
    cw = (W - emu(0.4)) / 2
    ch = CB - cy - emu(0.4)
    card(s, L, cy + emu(0.25), cw, ch, label="How",
         paras=bullets(["Once K-Means produces cluster labels, train a **LightGBM multiclass surrogate** to predict them from the original features.",
                        "Apply **TreeSHAP** to the surrogate: fast, exact tree-based attribution in the original feature space.",
                        "Aggregate into **global importance**, **cluster-specific profiles** and **local force plots**."],
                       size=20, color=WHITE, c0=YELLOW, c1=YELLOW, gap0=10), pad=(0.55, 0.7, 0.5, 0.3))
    light_card(s, L + cw + emu(0.4), cy + emu(0.25), cw, ch, label="Why",
               paras=bullets(["Direct TreeSHAP on K-Means is impossible: it explains **tree models, not centroids**.",
                              "Explaining the PCA representation would move attribution away from the interpretable variables.",
                              "The surrogate keeps the **chemistry / pollution terms** that make the analysis actionable.",
                              "**Validity condition:** surrogate fidelity is high, with **macro-F1 ≈ 0.82** as the floor."], size=20, gap0=10), pad=(0.55, 0.7, 0.5, 0.3))

    # v10: 'Pipeline in Five Stages' removed; the evaluation-protocol table that
    #     # follows already lists the same five stages with their settings.
    # --- C1 evaluation protocol ------------------------------------------------
    protocol_slide(ctx, C1, C1TABS, "Results",
                   [("Dataset", "Wine Quality, 4,898 samples × 11 standardised chemical features"),
                    ("Clustering", "K-Means++ on the PCA-stabilised data; k scanned over 2 … 10"),
                    ("Choice of k", "Elbow + Silhouette + Davies–Bouldin, then an interpretability check"),
                    ("Surrogate", "LightGBM multiclass, five-fold cross-validation, macro-F1 as fidelity score"),
                    ("Attribution", "Exact TreeSHAP on the surrogate, in the original 11-feature space"),
                    ("Outputs", "Global mean |SHAP| ranking, per-cluster profiles, local force plots"),
                    ("Comparison", "LIME-based surrogate explanation on the same partition")],
                   ["**Fidelity floor met:** macro-F1 ≈ 0.82 or higher, otherwise the explanation is not trusted.",
                    "**Global ranking is chemically meaningful:** the top features are ones an expert would name.",
                    "**Clusters have distinct signatures:** the same features, different weights per cluster.",
                    "**Shapley beats LIME** on stability and cross-cluster comparison."],
                   N("c1_protocol"), cite(6, 7, 17))

    # --- C1 results: k selection --------------------------------------------
    s, top = content_slide(ctx, "Choosing k: Interpretability over Geometry", eyebrow=C1, tabs=C1TABS, active="Results", notes=N(27))
    lw = emu(8.6)
    fit_textbox(s, L, top, lw, CB - top - emu(0.2), [
        *bullets(["Multi-criteria evaluation across **k ∈ {2 … 10}** using elbow, Silhouette and Davies–Bouldin.",
                  "We select **k^{*} = 3, even though it is NOT the best geometry**.",
                  (1, "k = 2: Silhouette 0.214, Davies–Bouldin 1.775 (better separation)."),
                  (1, "k = 3: Silhouette 0.144, Davies–Bouldin 2.097 (weaker separation)."),
                  "**Why:** three clusters give a richer, more meaningful wine partition → **more actionable**.",
                  "Note: the higher Silhouette ≈ 0.63 belongs to Beijing (C2), not to this wine partition."], size=21, gap0=10),
    ], min_scale=0.7)
    dx = L + lw + emu(0.6)
    dw = R - dx
    rows = [["k", "Silhouette ↑", "Davies–Bouldin ↓", "Reading"],
            ["2", "0.214", "1.775", "best geometry, coarse meaning"],
            ["3 ★", "0.144", "2.097", "richer wine partition · selected"]]
    gf, th = table(s, dx, top, dw, rows, col_widths=[1.0, 1.6, 2.0, 3.4], size=17, align=["ctr", "ctr", "ctr", "l"], header_align=["ctr", "ctr", "ctr", "l"], row_h=emu(0.8))
    ky = top + th + emu(0.4)
    kh = CB - ky - emu(0.2)
    cells = grid(2, 2, dx, ky, dw, kh, gap=emu(0.3))
    kpi(s, *cells[0], "k^{*} = 3", "chosen on **interpretability** grounds", fill=GREEN)
    kpi(s, *cells[1], "0.82", "surrogate **macro-F1** · fidelity floor met", fill=ORANGE, vcolor=WHITE)

    # --- C1 results: global ranking (thesis Fig. 5.1) ---------------------------
    s, top = content_slide(ctx, "Global SHAP Ranking: Wine Quality", eyebrow=C1, tabs=C1TABS, active="Results", notes=N(28), refs=cite(1))
    lw = emu(7.2)
    fit_textbox(s, L, top, lw, CB - top - emu(0.3), [
        H("Reading the ranking", size=22, color=GREEN),
        *bullets(["Mean |SHAP| ranks **density** first, then **pH**, **fixed acidity**, **sulfur dioxide** and **alcohol**.",
                  "The main drivers relate to **structure, preservation and sensory balance**.",
                  "This is **NOT a random side effect of the classifier**: the surrogate reproduces the partition from the original variables, so the ranking reflects the partition itself.",
                  "Density and pH separate wine styles; sulfur dioxide reflects preservation; alcohol shapes body.",
                  "Each driver is a **domain-level factor that can be changed**: exactly Definition 1.1 of an actionable insight."], size=19, gap0=10),
    ], min_scale=0.7)
    fx = L + lw + emu(0.5)
    fw = R - fx
    fh = CB - top - emu(0.3)
    # v10: Fig. 5.2 (cluster signatures, a wide strip) joins Fig. 5.1 on this slide
    h1 = fh * 0.70
    figure_frame(s, TF("fig5_1_wine_global.png"), fx, top, fw, h1,
                 caption="Fig. 5.1 (thesis): global SHAP feature importance for the wine clustering surrogate")
    figure_frame(s, TF("fig5_2_wine_clusters.png"), fx, top + h1 + emu(0.18), fw, fh - h1 - emu(0.18),
                 caption="Fig. 5.2 (thesis): per-cluster SHAP signatures")

    # v10: 'Cluster-Specific Explanatory Signatures' removed; thesis Fig. 5.2 moves
    #     # onto the global-ranking slide as a strip beneath Fig. 5.1.
    # v10: 'SHAP vs LIME' removed. The four axioms are on the deep-dive slide and the
    #     # SHAP-over-LIME argument is row O3 of the answer table plus a key finding.
    # --- C1 answer to RQ1 -------------------------------------------------------
    answer_slide(ctx, C1, C1TABS, "Findings", "RQ1",
                 "**Yes.** Shapley values explain a black-box partition **faithfully** (given a high-fidelity surrogate) and **consistently** at cluster level, in the original feature space.",
                 [("O1  ·  Cluster-level explanation with feature-level attribution", "Met", "Global ranking + per-cluster SHAP profiles (Fig. 5.1, 5.2) + local force plots"),
                  ("O2  ·  Attribution in the original feature space", "Met", "Density, pH, fixed acidity, sulfur dioxide, alcohol: no latent space"),
                  ("O3  ·  Shapley justified over LIME", "Met", "Four axioms; higher stability and cross-cluster comparability")],
                 N(31))

    # --- C1 key findings --------------------------------------------------------
    findings_slide(ctx, C1, C1TABS, "Findings",
                   [("A black-box partition can be explained at two levels at once", "Cluster-level meaning is tied to single feature contributions, so the explanation is both global and local."),
                    ("Attribution lands in the chemistry, not in a latent space", "Density, pH, fixed acidity, sulfur dioxide and alcohol: variables a wine maker can act on."),
                    ("Interpretability can outrank geometry when choosing k", "k = 3 was kept over k = 2 despite a lower Silhouette because it gives a richer, more useful partition."),
                    ("The cooperative concept is what makes the explanation trustworthy", "Efficiency, symmetry, null player and additivity give guarantees that a local surrogate such as LIME does not.")],
                   N(32), refs_=cite(1))

    # --- C1 limitations ---------------------------------------------------------
    limitations_slide(ctx, C1, C1TABS, "Findings",
                      [("Surrogate dependence", "Fidelity depends on the **LightGBM surrogate**, not on the K-Means geometry directly; the fidelity floor must be checked every time."),
                       ("Tabular only", "Limited to **tabular data**; no structured, graph or image input in this contribution."),
                       ("Single level", "Cannot explain how importance changes between a partition and its **sub-partitions**."),
                       ("Smoothing", "The surrogate approximation smooths out variation between single observations.")],
                      "The **single-level** limitation is the one that matters most for what follows: real data are rarely flat.",
                      N(33))

    # --- C1 takeaway ------------------------------------------------------------
    takeaway_slide(ctx, C1, C1TABS, "Findings", "Contribution I",
                   "Shapley attribution is a **well-founded lens** for explaining an unsupervised partition, and keeping it in the **original feature space** is what makes the explanation actionable.",
                   [("Single lens", "One axiomatic rule explains the whole partition, cluster by cluster."),
                    ("Original space", "The answer comes back in variables an expert can change."),
                    ("But…", "Real data are rarely single-level: broad groups contain nested sub-groups.")],
                   "**Next question:** does this logic survive scale and hierarchy?  →  Contribution II",
                   N(34))

    # ======================================================================
    # SECTION 5 — CONTRIBUTION II
    # ======================================================================
    C2 = "Contribution II: Multi-Level XAI for Large-Scale Clustering"
    section_slide(ctx, "05", "Contribution II", "Enhanced multi-level XAI for large-scale clustering  ·  answers RQ2",
                  [("Objectives", "A truly multi-level workflow, a formal cross-level consistency argument (Proposition 6.1), validation on a very different large dataset."),
                   ("Methodology", "Recursive clustering, level-specific surrogates in the same feature space, size-weighted cross-level SHAP aggregation."),
                   ("Results", "Beijing Air Quality (383,585 records): Silhouette ≈ 0.63, three atmospheric regimes, weather variables at the centre of the structure.")],
                  notes=N(35))

    # --- C2 research gap ------------------------------------------------------
    gap_slide(ctx, C2, C1TABS, "Objectives",
              ["Once clustering is multi-level, feature importance must stay readable **within a cluster, across sub-clusters and across the levels**.",
               "Large-scale data make exact explanation **too costly to compute**: 383,585 records cannot be explained coalition by coalition.",
               "A flat explanation may be true yet **incomplete**: it cannot show how importance changes inside a cluster.",
               "Existing hierarchical clustering work reports structure but gives **no formal link** between the explanation of a parent and that of its children."],
              "There is no multi-level explanation method for large-scale clustering that is **both computationally feasible and provably consistent across levels**.",
              N(36), cite(2, 18))

    # --- C2 RQ2 -> objectives ---------------------------------------------------
    rq_slide(ctx, C2, C1TABS, "Objectives", "RQ2",
             "How can the Shapley explanation extend to **large-scale, multi-level clustering** while staying feasible and consistent?",
             [("O1  ·  A truly multi-level workflow", "Recursive clustering with **level-specific surrogates**, not a rerun of the single-level pipeline.", "Workflow, Fig. 6.3"),
              ("O2  ·  A formal consistency argument", "**Proposition 6.1**: parent importance equals the size-weighted expectation over its children.", "Proposition 6.1"),
              ("O3  ·  Validation at scale on new data", "Beijing Multi-Site Air Quality: **383,585 hourly records**, a domain far from wine.", "Table 6.1, Fig. 6.1, 6.2")],
             N(37))

    # --- C2 methodology ------------------------------------------------------
    s, top = content_slide(ctx, "Multi-Level Workflow with Cross-Level Aggregation", eyebrow=C2, tabs=C1TABS, active="Methodology", notes=N(38))
    lw = emu(8.4)
    fit_textbox(s, L, top, lw, CB - top - emu(0.2), bullets([
        "**Recursive / nested:** coarse clustering on the full dataset, then split each cluster again.",
        "For each level, train a **level-specific surrogate** and compute SHAP in the **SAME original feature space**.",
        "Cross-level aggregation is **NOT a naive average**: it respects cluster size and nesting structure.",
        (1, "Parent-level attribution = an **expectation over the explanations of its children**."),
        (1, "The hierarchy is a practical analysis tool, not a claim that nature is really organised this way."),
    ], size=21, gap0=12), min_scale=0.7)
    # tree diagram
    dx = L + lw + emu(0.6)
    dw = R - dx
    root = chip(s, dx + dw * 0.25, top, dw * 0.5, emu(0.95), "Level 1 · coarse clustering (k = 3)", fill=INK, size=18, radius=emu(0.2))
    regs = [("Regime A", "temp · dew point · ozone", GREEN), ("Regime B", "CO · SO₂ · PM · wind", "1F5C99"), ("Regime C", "clean air · weather", ORANGE)]
    cells = grid(3, 3, dx, top + emu(1.6), dw, emu(1.35), gap=emu(0.25))
    for (h1, sub, f), (x, y, w, h) in zip(regs, cells):
        chip(s, x, y, w, h, h1, fill=f, size=19, sub=sub, sub_size=14, radius=emu(0.2))
        arrow(s, dx + dw / 2, top + emu(1.0), x + w / 2, y - emu(0.05), color=GREEN, w=2)
        # level-2 children
        c2 = grid(2, 2, x, y + h + emu(0.5), w, emu(0.7), gap=emu(0.12))
        for j, (cx, cy2, cw2, ch2) in enumerate(c2):
            chip(s, cx, cy2, cw2, ch2, f"sub {j+1}", fill=TINT, color=INK, size=14, radius=emu(0.12))
            arrow(s, x + w / 2, y + h + emu(0.03), cx + cw2 / 2, cy2 - emu(0.04), color=GREEN, w=1.5)
    fy = top + emu(4.35)
    bh = CB - fy - emu(0.2)
    box = rrect(s, dx, fy, dw, bh, fill=GREEN, radius=emu(0.25))
    textbox(s, dx, fy + emu(0.16), dw, emu(0.3), [Para([Run("PROPOSITION 6.1  ·  CROSS-LEVEL CONSISTENCY", font="xbold", size=13, color=YELLOW, spc=1.5)], align="ctr", lnspc=17)])
    equation(s, dx + emu(0.2), fy + emu(0.46), dw - emu(0.4), emu(1.05),
             r"\Phi_j^{(l,c)} = {\sum}_{c' \in \mathrm{child}(c)}\; w_{c'}\, \Phi_j^{(l+1,\,c')} + \varepsilon_j", size=22, color=WHITE)
    equation(s, dx + emu(0.2), fy + emu(1.5), dw - emu(0.4), emu(0.5),
             r"w_{c'} = |c'| \,/\, |c|, \qquad \varepsilon_j \to 0 \ \text{ under perfect surrogate fidelity}", size=14, color="D6E2EF")

    # --- C2 proposition ------------------------------------------------------
    s, top = content_slide(ctx, "Proposition 6.1: Cross-Level Consistency", eyebrow=C2, tabs=C1TABS, active="Methodology", notes=N(39))
    lw = emu(9.0)
    # definitions (equations) → statement → consequences: laid out block by block with generous leading
    yy = top
    defs = [(r"\Phi_j^{(l,c)} = \mathbb{E}_{x \in c}\left[\, \left|\varphi_j^{(l)}(x)\right| \,\right]", "expected absolute SHAP importance of feature j at level l in cluster c"),
            (r"w_{c'} = |c'| \,/\, |c|", "relative size of child c′ within parent c")]
    ew = emu(4.2)
    for tex, desc in defs:
        eh = emu(0.72)
        badge(s, L, yy + (eh - emu(0.3)) / 2, emu(0.3), "", fill=ORANGE)
        equation(s, L + emu(0.45), yy, ew, eh, tex, size=21, color=GREEN, align="l")
        textbox(s, L + emu(0.45) + ew + emu(0.2), yy, lw - emu(0.65) - ew, eh, [P(desc, size=17, color=INK, lnspc=21)], anchor="ctr")
        yy += eh + emu(0.08)
    yy += emu(0.12)
    textbox(s, L, yy, lw, emu(0.4), [P("For a **strict nested hierarchy** on a consistent feature space:", size=21, lnspc=27)])
    yy += emu(0.5)
    eb = rrect(s, L, yy, lw, emu(1.65), fill=GREEN_SOFT, radius=emu(0.2))
    equation(s, L + emu(0.2), yy, lw - emu(0.4), emu(1.65),
             r"\Phi_j^{(l,c)} = \sum_{c' \in \mathrm{child}(c)} w_{c'}\, \Phi_j^{(l+1,\,c')} + \varepsilon_j", size=26, color=GREEN)
    yy += emu(1.65) + emu(0.25)
    fit_textbox(s, L, yy, lw, CB - yy - emu(0.2), bullets([
        "**ε_{j}** is a residual from surrogate mismatch; it vanishes under perfect fidelity.",
        "Derived via the **law of total expectation** (children partition the parent).",
        "Does **NOT** mean explanations are identical across levels. It means differences can be **interpreted**, not ruled out as inconsistency."], size=20, gap0=10), min_scale=0.7)
    dx = L + lw + emu(0.6)
    dw = R - dx
    card(s, dx, top + emu(0.25), dw, emu(3.3), label="Why it matters",
         paras=bullets(["Gives the multi-level explanation a **formal backbone**.",
                        "Parent importance is an **accounting identity** over the children, not a separate story.",
                        "Turns cross-level differences into **interpretable signal**."], size=19, color=WHITE, c0=YELLOW, c1=YELLOW, gap0=8), pad=(0.5, 0.7, 0.45, 0.3))
    ky = top + emu(3.9)
    cells = grid(2, 2, dx, ky, dw, CB - ky - emu(0.2), gap=emu(0.3))
    kpi(s, *cells[0], "383,585", "hourly records · **11** variables", fill=TINT, vcolor=GREEN, lcolor=INK, vsize=34)
    kpi(s, *cells[1], "3 → 9", "coarse regimes → nested sub-clusters", fill=TINT, vcolor=ORANGE, lcolor=INK, vsize=34)

    # --- C2 evaluation protocol ------------------------------------------------
    protocol_slide(ctx, C2, C1TABS, "Results",
                   [("Dataset", "Beijing Multi-Site Air Quality, 383,585 hourly records × 11 variables"),
                    ("Level 1", "K-Means++ on the full dataset; k chosen by elbow, Silhouette and Davies–Bouldin"),
                    ("Level 2", "Each coarse cluster split again into sub-clusters (3 → 9)"),
                    ("Surrogates", "One LightGBM surrogate per level, five-fold cross-validation"),
                    ("Attribution", "Exact TreeSHAP per level, always in the original 11-variable space"),
                    ("Aggregation", "Size-weighted cross-level aggregation (Proposition 6.1)"),
                    ("Sensitivity", "Repeat with small changes in k, projection dimension and surrogate depth")],
                   ["**Separation is strong:** Silhouette and Davies–Bouldin clearly better than the wine case.",
                    "**Regimes have a physical reading:** each cluster maps to a known atmospheric situation.",
                    "**Cross-level differences are interpretable**, not contradictions (Proposition 6.1).",
                    "**Leading drivers are stable** under sensitivity changes."],
                   N("c2_protocol"), cite(17, 19))

    # --- C2 results: coarse level -------------------------------------------
    s, top = content_slide(ctx, "Coarse-Level Clustering: Beijing Air Quality", eyebrow=C2, tabs=C1TABS, active="Results", notes=N(40))
    cells = grid(3, 3, L, top + emu(0.1), W, emu(2.3), gap=emu(0.35))
    kpi(s, *cells[0], "k = 3", "all **k-selection criteria** agree", fill=GREEN)
    kpi(s, *cells[1], "≈ 0.63", "**Silhouette** · much stronger separation than wine", fill="1F5C99")
    kpi(s, *cells[2], "≈ 0.55", "**Davies–Bouldin** · clusters rarely overlap", fill=ORANGE, vcolor=WHITE)
    source_caption(s, L, top + emu(0.1) + emu(2.3) + emu(0.05), W, "Table 6.1 (thesis): validation metrics for the large-scale clustering study (k = 3, Silhouette 0.63, Davies–Bouldin 0.55).")
    cy = top + emu(0.1) + emu(2.3) + emu(0.5)
    cw = (W - emu(0.4)) / 2
    ch = CB - cy - emu(0.4)
    light_card(s, L, cy + emu(0.25), cw, ch, label="Setup",
               paras=bullets(["Full dataset: **383,585 hourly records**, 11 pollutant + weather variables.",
                              "PCA projection (2 components) used **only for visual inspection**.",
                              "Level-specific LightGBM surrogates; TreeSHAP in the original variable space."], size=20, gap0=10), pad=(0.55, 0.7, 0.5, 0.3))
    card(s, L + cw + emu(0.4), cy + emu(0.25), cw, ch, label="Sensitivity",
         paras=bullets(["Robust to small changes in **k**, projection dimension and surrogate depth.",
                        "Only **low-ranked variables shift**; the leading drivers are stable.",
                        "Comparison point: SHAP-based clustering literature (Gramegna & Giudici, credit risk) reports Silhouette **0.37**."],
                       size=20, color=WHITE, c0=YELLOW, c1=YELLOW, gap0=10), pad=(0.55, 0.7, 0.5, 0.3))

    # --- C2 results: global ranking (thesis Fig. 6.1) ---------------------------
    s, top = content_slide(ctx, "Global SHAP Ranking: Weather Variables Are Central", eyebrow=C2, tabs=C1TABS, active="Results", notes=N(41), refs=cite(2))
    lw = emu(7.4)
    fit_textbox(s, L, top, lw, CB - top - emu(0.3), [
        H("Reading the ranking", size=22, color=GREEN),
        *bullets(["**Temperature, dew point and pressure** lead the ranking; CO, NO₂, PM10 and PM2.5 follow.",
                  "It is **NOT only pollutant concentrations** that matter: weather variables play a **central role in the structure**.",
                  "Temperature, dew point and pressure control **dispersion, trapping and sunlight-driven chemistry**.",
                  "This is the kind of insight that flat summaries often fail to make explicit."], size=19, gap0=10),
    ], min_scale=0.7)
    fx = L + lw + emu(0.5)
    figure_frame(s, TF("fig6_1_beijing_global.png"), fx, top, R - fx, CB - top - emu(0.3),
                 caption="Fig. 6.1 (thesis): global SHAP importance at the coarse level, Beijing Air Quality")

    # v10: 'Three Atmospheric Regimes' removed; the regime reading is carried by the
    #     # cross-level slide, which is the point the regimes were there to make.
    # --- C2 results: cross-level ---------------------------------------------
    s, top = content_slide(ctx, "How Importance Changes Across Levels", eyebrow=C2, tabs=C1TABS, active="Results", notes=N(43), refs=cite(2))
    fh = emu(2.55)
    figure_frame(s, TF("fig6_3_beijing_multilevel.png"), L, top, W, fh, caption="Fig. 6.3 (thesis): SHAP importance per sub-cluster, level 2 of the hierarchy", pad=0.15)
    cy = top + fh + emu(0.55)
    cw = (W - emu(0.4)) / 2
    ch = emu(2.35)
    card(s, L, cy, cw, ch, label="Coarse level · regime selection",
         paras=bullets(["**Temperature and dew point dominate**: they separate the broad atmospheric regimes.",
                        "Parent-level story = which regime the observation belongs to."], size=18, color=WHITE, c0=YELLOW, c1=YELLOW, gap0=6), pad=(0.5, 0.6, 0.45, 0.25))
    light_card(s, L + cw + emu(0.4), cy, cw, ch, label="Within clusters · variation inside a regime",
               paras=bullets(["**CO, SO₂, PM10, wind speed, pressure or ozone** become more informative.",
                              "Cluster-level story = what varies once the regime is fixed."], size=18, gap0=6), pad=(0.5, 0.6, 0.45, 0.25))
    gy = cy + ch + emu(0.3)
    box = rrect(s, L, gy, W, CB - gy - emu(0.3), fill=None, line=ORANGE, line_w=2.5, radius=emu(0.3))
    fit_textbox(s, L + emu(0.5), gy + emu(0.12), W - emu(1.0), CB - gy - emu(0.3) - emu(0.24), [
        P("**This change is NOT a contradiction. It is exactly what a multi-level explanation should reveal.** A variable can be **globally important yet locally uninformative** inside a sub-cluster; Proposition 6.1 guarantees the two readings agree, up to the surrogate residual.", size=18, color=INK),
    ], anchor="ctr", min_scale=0.7)

    # v10: 'Generalisation and Comparison' removed; its comparative observations are
    #     # key finding 4 on the findings slide.
    # --- C2 answer to RQ2 -------------------------------------------------------
    answer_slide(ctx, C2, C1TABS, "Findings", "RQ2",
                 "**Yes, within bounds.** Consistency is kept at scale and across levels: a nested workflow with level-specific surrogates, backed by Proposition 6.1, explains 383,585 records in the original variable space.",
                 [("O1  ·  A truly multi-level workflow", "Met", "Coarse regimes, then sub-clusters, each with its own surrogate; no single flat summary"),
                  ("O2  ·  Formal cross-level consistency", "Met", "Proposition 6.1: parent importance = size-weighted expectation over children, up to ε_{j}"),
                  ("O3  ·  Validation on very different large-scale data", "Met", "Beijing Air Quality: Silhouette ≈ 0.63, three physically meaningful regimes")],
                 N(45))

    # --- C2 key findings --------------------------------------------------------
    findings_slide(ctx, C2, C1TABS, "Findings",
                   [("Weather, not only pollution, defines the structure", "Temperature, dew point and pressure lead the coarse-level ranking; they set the regime that pollutants then vary within."),
                    ("Importance legitimately changes with the level", "A variable can be globally important yet locally uninformative; Proposition 6.1 makes that difference interpretable rather than contradictory."),
                    ("The explanation scales", "Level-specific surrogates and exact TreeSHAP keep the cost linear in the data, not exponential in the features."),
                    ("The logic transfers across domains", "Same pipeline, same reading, from 4,898 wines to 383,585 hourly air-quality records, with a Silhouette ≈ 0.63 against 0.37 in the reference SHAP-clustering study.")],
                   N(46), refs_=cite(2, 18))

    # --- C2 limitations ---------------------------------------------------------
    limitations_slide(ctx, C2, C1TABS, "Findings",
                      [("Static clustering", "The partition is **static**, even though the Beijing data are temporal; drift between years is not modelled."),
                       ("Smoothing", "Surrogate-based SHAP plus representative-instance reporting **smooth out variation between single observations**."),
                       ("Tabular only", "Still limited to **tabular data**; no graph, text or image input."),
                       ("Post-hoc", "Still an explanation of a **pre-computed partition**: attribution does not influence learning.")],
                      "The **post-hoc** limitation is the one that opens the door to Contribution III: what if attribution could shape the learning itself?",
                      N(47))

    # --- C2 takeaway ------------------------------------------------------------
    takeaway_slide(ctx, C2, C1TABS, "Findings", "Contribution II",
                   "Shapley attribution stays **consistent across levels of detail** when the hierarchy is explicit, so explanations become interpretable **against scale**, not just against one flat partition.",
                   [("Consistent", "Parent and child explanations agree by construction (Proposition 6.1)."),
                    ("Against scale", "383,585 records explained with level-specific surrogates, at a linear cost."),
                    ("Still post-hoc", "The attribution explains a partition that was already computed.")],
                   "**Next step:** let attribution shape the learning itself  →  Contribution III",
                   N(48))

    # ======================================================================
    # SECTION 6 — CONTRIBUTION III
    # ======================================================================
    C3 = "Contribution III: DyHuCoG, a Dynamic Hypergraph Cooperative Game"
    section_slide(ctx, "06", "Contribution III", "DyHuCoG: a Dynamic Hypergraph Cooperative Game for recommendation  ·  answers RQ3 & RQ4",
                  [("Objectives", "Formulate recommendation as a cooperative game over users, items and contexts; make attribution an in-training signal."),
                   ("Methodology", "Preference-aware Monte Carlo Shapley → dynamic hypergraph edge weights → attention-gated, context-aware scoring; multi-objective loss."),
                   ("Results", "MovieLens-1M & Amazon-Book: NDCG, Recall, Coverage and ILD improve together over HPCF; largest gains on the sparsest data.")],
                  notes=N(49))

    # --- C3 research gap ------------------------------------------------------
    gap_slide(ctx, C3, C1TABS, "Objectives",
              ["Graph and hypergraph recommenders [12, 13, 14] treat message importance as **uniform or attention-weighted**, with no well-founded **marginal-contribution** account.",
               "Diversity is often a secondary goal or a **re-ranking heuristic** applied after the model has been trained [23].",
               "Interpretability is **added after prediction**, not built into the learning objective [21].",
               "Contributions I and II showed that Shapley attribution is faithful and consistent, but it was still **post-hoc**: it never changed what the model learned."],
              "No recommender uses a **cooperative-game utility** to decide, during training, how much each user, item and context should count, while keeping accuracy, context and diversity in the same objective.",
              N(50), cite(12, 13, 14, 21, 23))

    # --- C3 RQ3 / RQ4 -> objectives ---------------------------------------------
    s, top = content_slide(ctx, "RQ3, RQ4 and Objectives", eyebrow=C3, tabs=C1TABS, active="Objectives", notes=N(51))
    cw = (W - emu(0.4)) / 2
    sh = emu(1.55)
    statement(s, L, top + emu(0.2), cw, sh, "RQ3", "Can cooperative attribution move **beyond post-hoc** and become part of how a recommender learns?", fill=GREEN, size=19)
    statement(s, L + cw + emu(0.4), top + emu(0.2), cw, sh, "RQ4", "Can it improve **ranking accuracy, context and diversity together** when importance comes from a cooperative-game utility?", fill=GREEN, size=19)
    ty = top + emu(0.2) + sh + emu(0.45)
    rows = [["Objective", "What it delivers", "Where it is shown"],
            ["O1  ·  Recommendation as a cooperative game", "Users, items and contexts are the **players**; the coalition utility mixes accuracy, diversity and novelty.", "Game formulation, value function"],
            ["O2  ·  Shapley inside message passing", "**Preference-aware Monte Carlo Shapley** estimates become dynamic hyperedge weights during training.", "MC Shapley, architecture"],
            ["O3  ·  Accuracy, coverage and diversity together", "Better NDCG and Recall **and** higher Coverage and ILD than the strongest baseline, on two datasets.", "Table 7.1, Fig. 7.2, 7.3"]]
    gf, th = table(s, L, ty, W, rows, col_widths=[4.6, 7.4, 3.6], size=18, head_size=17, row_h=emu(0.9))

    # --- C3 game formulation + coalition value (v10: two slides merged) -------
    s, top = content_slide(ctx, "Recommendation as a Cooperative Game", eyebrow=C3, tabs=C1TABS, active="Methodology", notes=N(52))
    lw = emu(8.6)
    fit_textbox(s, L, top, lw, emu(2.4), bullets([
        "**Player set N = U ∪ I ∪ C** (users, items, contexts).",
        "**Hypergraph H = (V, E, W)**; V = U ∪ I ∪ C; **W = dynamic edge weights** from Shapley estimates.",
        "A **coalition S ⊆ N** is the set of entities taking part in a recommendation episode.",
    ], size=21, gap0=12), min_scale=0.7)
    # v10: the coalition value, folded in from the removed "Coalition Value" slide
    vy = top + emu(2.5)
    rrect(s, L, vy, lw, emu(1.55), fill=GREEN, radius=emu(0.25))
    equation(s, L + emu(0.25), vy + emu(0.12), lw - emu(0.5), emu(0.72),
             r"v(S) = \alpha \cdot \mathrm{NDCG@20}(S) + \beta \cdot \mathrm{Diversity}(S) + \gamma \cdot \mathrm{ContextScore}(S)",
             size=19, color=WHITE)
    equation(s, L + emu(0.25), vy + emu(0.85), lw - emu(0.5), emu(0.6),
             r"\alpha = 0.60, \;\; \beta = 0.25, \;\; \gamma = 0.15, \;\; \alpha + \beta + \gamma = 1",
             size=18, color=YELLOW)
    ty = vy + emu(1.75)
    fit_textbox(s, L, ty, lw, CB - ty - emu(0.2), [
        P("Preference term **v_{pref}(S) = v(S) + λ_{pref} Σ sim(u,i)**, λ_{pref} = 0.20; weights grid-searched, **< 1.5 % variance** in NDCG@20.", size=18, spcbef=0),
        P("The **same trade-off** the recommender must satisfy is the one from which attribution is computed: explanatory game and predictive objective are **aligned by design**.", size=18, spcbef=8),
    ], min_scale=0.7)
    dx = L + lw + emu(0.6)
    dw = R - dx
    # hyperedge illustration: three player groups joined into a coalition
    textbox(s, dx, top, dw, emu(0.4), [Para([Run("PLAYERS AND COALITIONS", font="xbold", size=14, color=ORANGE, spc=1.6)], align="ctr", lnspc=18)])
    hy = top + emu(0.6)
    hh = emu(3.1)
    rrect(s, dx + emu(0.3), hy, dw - emu(0.6), hh, fill=TINT, radius=emu(0.6))
    textbox(s, dx, hy + emu(0.12), dw, emu(0.4), [Para([Run("coalition S ⊆ N  ·  hyperedge e ∈ E", font="bold", size=15, color=MUTED)], align="ctr", lnspc=18)])
    groups = [("Users", "U", GREEN), ("Items", "I", "1F5C99"), ("Contexts", "C", ORANGE)]
    cells = grid(3, 3, dx + emu(0.7), hy + emu(0.75), dw - emu(1.4), emu(1.9), gap=emu(0.45))
    for (h1, sym, f), (x, y, w, h) in zip(groups, cells):
        d = min(w, h)
        e = ellipse(s, x + (w - d) / 2, y, d, d, fill=f)
        shape_text(e, [Para([Run(sym, font="title", size=34, color=WHITE)], align="ctr", lnspc=38),
                       Para([Run(h1, font="bold", size=15, color="F7F2EA")], align="ctr", lnspc=18, spcbef=2)], anchor="ctr", insets=(0, 0, 0, 0))
    vy = hy + hh + emu(0.35)
    bh = CB - vy - emu(0.2)
    box = rrect(s, dx, vy, dw, bh, fill=GREEN, radius=emu(0.25))
    rh = bh / 2
    ew = emu(2.0)
    equation(s, dx + emu(0.3), vy + emu(0.05), ew, rh, r"v(S)", size=22, color=WHITE)
    textbox(s, dx + emu(0.4) + ew, vy + emu(0.05), dw - emu(0.7) - ew, rh, [Para([Run("quality of the recommendation that coalition S can achieve", font="bold", size=17, color=WHITE)], lnspc=21)], anchor="ctr")
    equation(s, dx + emu(0.3), vy + rh - emu(0.05), ew, rh, r"\hat{\varphi}_j \;\to\; w_{jk}", size=22, color=YELLOW)
    textbox(s, dx + emu(0.4) + ew, vy + rh - emu(0.05), dw - emu(0.7) - ew, rh, [Para([Run("marginal contribution of player j → dynamic hyperedge weight", font="bold", size=17, color=YELLOW)], lnspc=21)], anchor="ctr")

    # v10: 'Coalition Value Aligned with the Objective' folded into the
    # game-formulation slide above (value function, weights and preference term).
    # --- C3 Monte Carlo Shapley ---------------------------------------------
    s, top = content_slide(ctx, "Preference-Aware Monte Carlo Shapley", eyebrow=C3, tabs=C1TABS, active="Methodology", notes=N(54))
    lw = emu(9.4)
    yy = top
    textbox(s, L, yy, lw, emu(0.45), bullets(["Exact Shapley is **combinatorial and not feasible** for real systems."], size=21))
    yy += emu(0.55)
    eqh = emu(1.45)
    eb = rrect(s, L, yy, lw, 2 * eqh + emu(0.2), fill=GREEN_SOFT, radius=emu(0.2))
    equation(s, L + emu(0.2), yy + emu(0.1), lw - emu(0.4), eqh,
             r"\hat{\varphi}_j = \dfrac{1}{M} \sum_{m=1}^{M} \left[\, v(S_m \cup \{j\}) - v(S_m) \,\right]", size=24, color=GREEN)
    equation(s, L + emu(0.2), yy + emu(0.1) + eqh, lw - emu(0.4), eqh,
             r"\hat{\varphi}_j^{\,\mathrm{pref}} = \dfrac{1}{M} \sum_{m=1}^{M} \left[\, v_{\mathrm{pref}}(S_m \cup \{j\}) - v_{\mathrm{pref}}(S_m) \,\right]", size=24, color=ORANGE)
    yy += 2 * eqh + emu(0.2) + emu(0.15)
    equation(s, L + emu(0.2), yy, lw - emu(0.4), emu(0.6),
             r"\mathrm{Var}\left[\hat{\varphi}_j\right] = \sigma^{2}/M \;\;\Rightarrow\;\; \mathrm{MSE} = O(1/M), \quad |\text{error}| = O(1/\sqrt{M})", size=18, color=INK)
    yy += emu(0.7)
    fit_textbox(s, L, yy, lw, CB - yy - emu(0.2), bullets([
        "**Unbiased estimator:** error shrinks as the number of permutations M grows.",
        "**M = 50 selected:** MSE ≈ 1.4×10^{−5}, ≈ 99 % accuracy on MovieLens-1M; M = 100 → MSE 3.5×10^{−6} (diminishing returns).",
        "Refreshed **every 10 batches** (≈ 49 updates / epoch), smoothed by an **exponential moving average**."], size=19, gap0=8), min_scale=0.7)
    dx = L + lw + emu(0.6)
    dw = R - dx
    rows = [["M", "MSE", "Accuracy"], ["25", "≈ 5.6×10⁻⁵", "≈ 96 %"], ["50 ★", "≈ 1.4×10⁻⁵", "≈ 99 %"], ["100", "≈ 3.5×10⁻⁶", "≈ 99.5 %"]]
    gf, th = table(s, dx, top, dw, rows, col_widths=[1.2, 2.2, 1.8], size=18, align=["ctr", "ctr", "ctr"], header_align=["ctr", "ctr", "ctr"], row_h=emu(0.62))
    textbox(s, dx, top + th + emu(0.08), dw, emu(0.4), [Para([Run("M = 50 balances estimator quality against per-epoch cost; rows 25/100 show the O(1/M) trend.", font="body", size=13, color=MUTED)], lnspc=16)])
    ky = top + th + emu(0.55)
    ch = CB - ky - emu(0.45)
    card(s, dx, ky + emu(0.25), dw, ch, label="In the training loop",
         paras=bullets(["Sample M permutations per refresh → estimate φ̂ for the players in the episode.",
                        "Clip, EMA-smooth, normalise → **hypergraph edge weights**.",
                        "Cost per epoch:"], size=18, color=WHITE, c0=YELLOW, c1=YELLOW, gap0=7), pad=(0.5, 0.65, 0.45, 0.85))
    equation(s, dx + emu(0.5), ky + emu(0.25) + ch - emu(0.85), dw - emu(1.0), emu(0.65),
             r"O\left((L+1)\,m\,d\right) + O\left((M/f)\,m\right)", size=19, color=YELLOW)

    # --- C3 architecture -----------------------------------------------------
    s, top = content_slide(ctx, "Shapley-Weighted Hypergraph Message Passing", eyebrow=C3, tabs=C1TABS, active="Methodology", notes=N(55))
    from PIL import Image
    im = Image.open(os.path.join(FIGS, "dyhucog_arch.png"))
    ratio = im.height / im.width
    ph = emu(1.55)   # v10: shortened from 1.9 to make room for the sixth equation row
    pw = ph / ratio
    frame = rrect(s, L, top, W, ph + emu(0.3), fill=WHITE, line=RULE, line_w=1.25, radius=emu(0.25))
    picture(s, os.path.join(FIGS, "dyhucog_arch.png"), L + (W - pw) / 2, top + emu(0.15), w=pw, h=ph)
    source_caption(s, L + emu(0.2), top + ph + emu(0.3) - emu(0.42), W - emu(0.4), "Fig. 7.1 (thesis): workflow of the DyHuCoG architecture", size=12, align="r")
    ey = top + ph + emu(0.3) + emu(0.25)
    eqs = [("Base propagation", r"e^{(l+1)} = \sigma\left( D^{-1/2} A\, D^{-1/2}\, e^{(l)} \right)", None),
           ("Shapley-weighted", r"e_j^{(l+1)} = \sigma\left( W^{(l)} e_j^{(l)} + {\sum}_{k \in \mathcal{N}(j)} w_{jk}\, e_k^{(l)} \right)", None),
           ("Normalised weights", r"w_{jk} = \hat{\varphi}_{jk} \,/\, {\sum}_{k' \in \mathcal{N}(j)} \hat{\varphi}_{jk'}", "clipped + EMA-smoothed"),
           ("Attention gate", r"a_{ui} = \sigma\left( W_a\, [\,e_u, e_i, l_i\,] \right), \qquad y_{ui} = (1 + a_{ui})\, \langle e_u, e_i \rangle", None),
           ("Context-aware score", r"f(u,i,c) = y_{ui} + \lambda_c\, \langle\, g(c_{ui}),\, e_{c_{ui}} \rangle", None),
           # v10: the training loss, folded in from the removed "Multi-Objective Learning" slide
           ("Training loss", r"\mathcal{L} = \mathcal{L}_{\mathrm{rec}} + \lambda_{\mathrm{div}}\, \mathcal{L}_{\mathrm{div}} + \lambda_{\mathrm{ctx}}\, \mathcal{L}_{\mathrm{ctx}} + \lambda_{\mathrm{reg}}\, \mathcal{L}_{\mathrm{reg}}", "BPR + diversity + context + L2")]
    rh = (CB - ey - emu(0.1) - emu(0.1) * 5) / 6
    for i, (h1, tex, note) in enumerate(eqs):
        yy = ey + i * (rh + emu(0.1))
        rrect(s, L, yy, W, rh, fill=TINT if i % 2 == 0 else TINT2, radius=emu(0.16))
        textbox(s, L + emu(0.35), yy, emu(3.6), rh, [Para([Run(h1, font="xbold", size=18, color=GREEN)], lnspc=22)], anchor="ctr")
        ew = W - emu(4.3) - (emu(3.2) if note else 0)
        equation(s, L + emu(4.0), yy, ew, rh, tex, size=22, color=INK, align="l")
        if note:
            textbox(s, R - emu(3.3), yy, emu(3.0), rh, [Para([Run(note, font="body", size=15, color=MUTED)], align="r", lnspc=18)], anchor="ctr")

    # v10: 'Multi-Objective Learning' folded into the message-passing slide as a
    # sixth equation row; the four loss terms are named in that row's caption.
    # --- C3 evaluation protocol ------------------------------------------------
    protocol_slide(ctx, C3, C1TABS, "Results",
                   [("Datasets", "MovieLens-1M (dense, 0.0447) and Amazon-Book (sparse, 0.0006); Yelp2018 as a check"),
                    ("Split", "User-level, time-ordered 70 / 10 / 20; leave-one-out target per user"),
                    ("Baselines", "MF, NCF, LightGCN, RecDCL, HCCF, HPCF (strongest reference)"),
                    ("Metrics", "NDCG@20 (main), Recall@20, Catalogue Coverage, Intra-List Diversity"),
                    ("Repeats", "Five seeds {42 … 46}; mean ± standard deviation reported"),
                    ("Statistics", "Paired t-test and Wilcoxon on per-user NDCG@20; Holm–Bonferroni; Cohen's d_{z}"),
                    ("Ablation", "Remove one component at a time: Shapley, hypergraph, attention, context, diversity")],
                   ["**Beat HPCF on both datasets** in NDCG@20 and Recall@20, with p < 0.05 after correction.",
                    "**Coverage and ILD go up at the same time**: no accuracy-for-diversity trade.",
                    "**Every component matters**: removing any one of them lowers NDCG@20.",
                    "**Overhead stays bounded**: training time within about 2× HPCF; real-time inference."],
                   N("c3_protocol"), cite(20, 27))

    # --- C3 main results: one slide per dataset (all baselines, best row bold) --
    def bold_row(gf, ri, ncols, fill=GREEN_SOFT):
        for ci in range(ncols):
            c = gf.table.cell(ri, ci)
            c.fill.solid()
            c.fill.fore_color.rgb = RGBColor.from_string(fill)
            for para in c.text_frame.paragraphs:
                for r in para.runs:
                    r.font.bold = True

    def results_slide(title, bullets_, rows, notes, key_gain):
        s, top = content_slide(ctx, title, eyebrow=C3, tabs=C1TABS, active="Results", notes=notes, refs=cite(3))
        lw = emu(6.6)
        fit_textbox(s, L, top, lw, CB - top - emu(1.7), bullets(bullets_, size=19, gap0=10), min_scale=0.7)
        kpi(s, L, CB - emu(1.5), lw, emu(1.2), key_gain[0], key_gain[1], fill=GREEN, vsize=30, lsize=15)
        dx = L + lw + emu(0.5)
        dw = R - dx
        al = ["l", "ctr", "ctr", "ctr", "ctr"]
        gf, th = table(s, dx, top, dw, rows, col_widths=[2.3, 2.0, 2.0, 1.9, 1.9], size=17, head_size=16, align=al, header_align=al, row_h=emu(0.66), pad=0.07)
        bold_row(gf, len(rows) - 1, 5)
        textbox(s, dx, top + th + emu(0.12), dw, emu(0.6), [Para([Run("Table 7.1 (thesis): mean over five seeds; ± standard deviation in the backup slides. Best value per column in the bold row.", font="body", size=13, color=MUTED)], lnspc=16)])
        return s

    results_slide("Main Results on MovieLens-1M",
                  ["**DyHuCoG is best on all four metrics** against six baselines from four model families.",
                   "NDCG@20 **0.2775 vs 0.2528** for HPCF (+9.8 %); Recall@20 **0.2362 vs 0.2098** (+12.6 %).",
                   "Coverage **0.397 vs 0.342** (+16.1 %) and ILD **0.516 vs 0.461** (+11.9 %): more of the catalogue reaches users.",
                   "The gap widens from classical (MF) to graph (LightGCN) to hypergraph (HCCF, HPCF) models, and DyHuCoG adds another step on top of the strongest."],
                  [["Model", "NDCG@20", "Recall@20", "Coverage", "ILD"],
                   ["MF", "0.1200", "0.0880", "0.239", "0.367"],
                   ["NCF", "0.1300", "0.1100", "0.269", "0.398"],
                   ["LightGCN", "0.2130", "0.1790", "0.308", "0.423"],
                   ["RecDCL", "0.2296", "0.1918", "0.324", "0.445"],
                   ["HCCF", "0.2470", "0.2050", "0.327", "0.448"],
                   ["HPCF", "0.2528", "0.2098", "0.342", "0.461"],
                   ["DyHuCoG", "0.2775", "0.2362", "0.397", "0.516"]],
                  N(57), ("+9.8 %  ·  +12.6 %", "NDCG@20 · Recall@20 over HPCF"))

    results_slide("Main Results on Amazon-Book",
                  ["Same picture on the **sparse** dataset (density 0.0006), with **larger relative gains**.",
                   "NDCG@20 **0.0306 vs 0.0270** for HPCF (+13.3 %); Recall@20 **0.0417 vs 0.0359** (+16.2 %).",
                   "Coverage **0.336 vs 0.259** (+29.7 %) and ILD **0.602 vs 0.535** (+12.5 %).",
                   "Absolute values are low for every model because the matrix is almost empty; what matters is the **consistent ordering and the widening gap** where data are weakest."],
                  [["Model", "NDCG@20", "Recall@20", "Coverage", "ILD"],
                   ["MF", "0.0049", "0.0093", "0.168", "0.425"],
                   ["NCF", "0.0085", "0.0142", "0.193", "0.458"],
                   ["LightGCN", "0.0236", "0.0320", "0.226", "0.491"],
                   ["RecDCL", "0.0255", "0.0346", "0.242", "0.512"],
                   ["HCCF", "0.0258", "0.0344", "0.248", "0.520"],
                   ["HPCF", "0.0270", "0.0359", "0.259", "0.535"],
                   ["DyHuCoG", "0.0306", "0.0417", "0.336", "0.602"]],
                  N(58), ("+13.3 %  ·  +16.2 %", "NDCG@20 · Recall@20 over HPCF"))

    # v10: 'Ranking Quality Across All Baselines' (thesis Fig. 7.2) removed. It
    # charts the same seven models on the same two metrics already tabulated on
    # the two main-results slides.

    # v10: 'Coverage & Diversity' removed. Coverage and ILD are columns of the two
    #     # main-results tables, so the figure repeated numbers already on screen.
    # --- C3 ablation: per dataset ------------------------------------------------
    s, top = content_slide(ctx, "Ablation: Every Component Contributes", eyebrow=C3, tabs=C1TABS, active="Results", notes=N(60), refs=cite(3))
    abl = [("MovieLens-1M", [["Variant", "NDCG@20", "Drop"],
                              ["Full DyHuCoG", "0.2775", "–"],
                              ["w/o Shapley value", "0.2647", "−4.6 %"],
                              ["w/o Hypergraph", "0.2586", "−6.8 %"],
                              ["w/o Attention", "0.2678", "−3.5 %"],
                              ["w/o Context", "0.2547", "−8.2 %"],
                              ["w/o Diversity", "0.2614", "−5.8 %"]]),
           ("Amazon-Book", [["Variant", "NDCG@20", "Drop"],
                            ["Full DyHuCoG", "0.0306", "–"],
                            ["w/o Shapley value", "0.0287", "−6.1 %"],
                            ["w/o Hypergraph", "0.0279", "−8.9 %"],
                            ["w/o Attention", "0.0295", "−3.5 %"],
                            ["w/o Context", "0.0272", "−11.0 %"],
                            ["w/o Diversity", "0.0288", "−5.8 %"]])]
    cw = (W - emu(0.5)) / 2
    al = ["l", "ctr", "ctr"]
    for i, (name, rows) in enumerate(abl):
        x = L + i * (cw + emu(0.5))
        textbox(s, x, top - emu(0.05), cw, emu(0.35), [Para([Run(("TABLE 7.2  ·  " if i == 0 else "") + name.upper(), font="xbold", size=13, color=ORANGE, spc=1.5)], lnspc=16)])
        gf, th = table(s, x, top + emu(0.35), cw, rows, col_widths=[3.6, 2.0, 1.8], size=17, head_size=16, align=al, header_align=al, row_h=emu(0.5), pad=0.07)
        bold_row(gf, 1, 3)
        # highlight the largest drop
        worst = 5  # w/o Context
        for ci in range(3):
            c = gf.table.cell(worst, ci)
            for para in c.text_frame.paragraphs:
                for r in para.runs:
                    r.font.color.rgb = RGBColor.from_string(ORANGE)
                    r.font.bold = True
    by = top + emu(0.35) + th + emu(0.45)
    light_card(s, L, by + emu(0.25), W, CB - by - emu(0.5), label="Reading",
               paras=bullets(["**Context** is the most important component (−8.2 % / −11.0 %), then the **hypergraph** structure (−6.8 % / −8.9 %).",
                              "Removing **Shapley** weighting costs 4.6 % / 6.1 %: more on the sparser dataset, where fair credit for weak signals matters most.",
                              "The ablation removes one component at a time; it does not test combinations."], size=18, gap0=6), pad=(0.55, 0.6, 0.5, 0.2))

    # --- C3 efficiency -------------------------------------------------------
    s, top = content_slide(ctx, "Efficiency and Shapley Convergence", eyebrow=C3, tabs=C1TABS, active="Results", notes=N(61), refs=cite(3, 8))
    cells = grid(4, 4, L, top + emu(0.1), W, emu(2.3), gap=emu(0.3))
    kpi(s, *cells[0], "1.78×", "training time vs HPCF **(≈ 2000 s vs 1125 s, ML-1M)**", fill=GREEN, vsize=36)
    kpi(s, *cells[1], "1.84 ms", "inference / query on ML-1M **(8.52 ms Amazon)**", fill="1F5C99", vsize=36)
    kpi(s, *cells[2], "4.4 GB", "memory ML-1M vs 4.1 GB **(17.9 vs 16.8 GB Amazon)**", fill=ORANGE, vcolor=WHITE, vsize=36)
    kpi(s, *cells[3], "M = 50", "MSE 1.4×10^{−5} · **≈ 99 % accuracy**", fill=INK, vsize=36)
    source_caption(s, L, top + emu(0.1) + emu(2.3) + emu(0.05), W, "Table 7.3 (thesis): runtime and scalability  ·  Table 7.4 (thesis): Monte Carlo convergence and runtime trade-offs. Full tables in the backup slides.")
    cy = top + emu(0.1) + emu(2.3) + emu(0.5)
    cw = (W - emu(0.4)) / 2
    ch = CB - cy - emu(0.4)
    light_card(s, L, cy + emu(0.25), cw, ch, label="Complexity",
               paras=bullets(["Per-epoch cost: propagation plus periodic Shapley refresh:",
                              "A refresh every f = 10 batches keeps the overhead bounded.",
                              "Inference latency is **suitable for real-time use**."], size=20, gap0=10), pad=(0.55, 0.7, 0.5, 1.0))
    equation(s, L + emu(0.55), cy + emu(0.25) + ch - emu(0.95), cw - emu(1.1), emu(0.7),
             r"O\left((L+1)\,m\,d\right) + O\left((M/f)\,m\right)", size=20, color=GREEN)
    card(s, L + cw + emu(0.4), cy + emu(0.25), cw, ch, label="Convergence",
         paras=bullets(["M = 50 → MSE 1.4×10^{−5}, ≈ 99 % accuracy.",
                        "M = 100 → MSE 3.5×10^{−6}: **diminishing returns**.",
                        "The overhead is the price of an in-training attribution signal: measurable, but modest."],
                       size=20, color=WHITE, c0=YELLOW, c1=YELLOW, gap0=10), pad=(0.55, 0.7, 0.5, 0.3))

    # --- C3 significance -----------------------------------------------------
    s, top = content_slide(ctx, "Statistical Significance", eyebrow=C3, tabs=C1TABS, active="Results", notes=N(62), refs=cite(27))
    cells = grid(3, 3, L, top + emu(0.1), W, emu(2.4), gap=emu(0.35))
    stats = [(r"t = 46.38", "paired t-test vs HPCF · **df = 6,039**", GREEN, YELLOW),
             (r"d_z = 1.33", "**Cohen's d_{z}** · a large effect size", "1F5C99", YELLOW),
             (r"p = 1.8 \times 10^{-270}", "after **Holm–Bonferroni** correction", ORANGE, WHITE)]
    for (tex, lab, f, vc), (x, y, w, h) in zip(stats, cells):
        rrect(s, x, y, w, h, fill=f, radius=emu(0.3))
        equation(s, x + emu(0.2), y + emu(0.3), w - emu(0.4), emu(1.15), tex, size=38, color=vc)
        textbox(s, x + emu(0.3), y + emu(1.5), w - emu(0.6), emu(0.7), [Para(md_runs(lab, size=17, color=WHITE), align="ctr", lnspc=22)], anchor="t")
    source_caption(s, L, top + emu(0.1) + emu(2.4) + emu(0.05), W, "Table 7.6 (thesis): paired tests on per-user NDCG@20, DyHuCoG vs HPCF (all six comparisons in the backup slides).")
    cy = top + emu(0.1) + emu(2.4) + emu(0.5)
    light_card(s, L, cy + emu(0.25), W, CB - cy - emu(0.45), label="Protocol",
               paras=bullets(["Paired t-tests on **per-user NDCG@20** (n = 6,040 users, MovieLens-1M).",
                              "DyHuCoG beats **every baseline** with very small p-values after Holm–Bonferroni correction.",
                              "**Wilcoxon signed-rank test** also significant (p < 0.001): the result does not depend on normality.",
                              "**Effect sizes are large**: the improvements really matter, they are not only statistically visible."], size=21, gap0=9), pad=(0.55, 0.7, 0.5, 0.3))

    # v10: 'Cold-Start, Cross-Dataset Robustness and Interpretability' removed; the
    #     # cold-start gains are key finding 2 and the waterfall read-out is the
    #     # takeaway slide's point.
    # --- C3 answers to RQ3 and RQ4 ---------------------------------------------
    s, top = content_slide(ctx, "Answers to RQ3 and RQ4", eyebrow=C3, tabs=C1TABS, active="Findings", notes=N(64))
    cw = (W - emu(0.4)) / 2
    sh = emu(1.75)
    statement(s, L, top + emu(0.2), cw, sh, "Answer to RQ3", "**Yes.** Attribution becomes an **in-training signal**: Shapley estimates set the hyperedge weights while the model learns, instead of describing it afterwards.", fill=GREEN, size=19)
    statement(s, L + cw + emu(0.4), top + emu(0.2), cw, sh, "Answer to RQ4", "**Yes.** Ranking, coverage and diversity **improve together** on both datasets, with the largest gains where data are sparsest.", fill=GREEN, size=19)
    ty = top + emu(0.2) + sh + emu(0.45)
    rows = [["Objective", "Status", "Evidence"],
            ["O1  ·  Recommendation as a cooperative game over users, items and contexts", "Met", "Player set U ∪ I ∪ C; coalition utility α·accuracy + β·diversity + γ·novelty"],
            ["O2  ·  Preference-aware Monte Carlo Shapley inside message passing", "Met", "M = 50 permutations, ≈ 99 % accuracy, refreshed every 10 batches; ablation −4.6 % / −6.1 % without it"],
            ["O3  ·  Ranking, coverage and diversity together", "Met", "+9.8 % / +13.3 % NDCG@20, +16.1 % / +29.7 % Coverage, +11.9 % / +12.5 % ILD over HPCF"]]
    gf, th = table(s, L, ty, W, rows, col_widths=[5.6, 1.3, 8.7], size=17, head_size=17, row_h=emu(0.8), align=["l", "ctr", "l"], header_align=["l", "ctr", "l"])

    # --- C3 key findings --------------------------------------------------------
    findings_slide(ctx, C3, C1TABS, "Findings",
                   [("The accuracy / diversity / context trade-off is not fixed by nature", "When importance comes from a cooperative-game utility, NDCG, Recall, Coverage and ILD all move up together."),
                    ("Gains are largest where data are weakest", "+13.3 % NDCG@20 on Amazon-Book vs +9.8 % on MovieLens-1M; +10.9 % / +9.6 % for cold users and cold items."),
                    ("Context and structure carry the most weight", "Removing context (−8.2 % / −11.0 %) or the hypergraph (−6.8 % / −8.9 %) hurts most; Shapley weighting adds a further 4.6 % / 6.1 %."),
                    ("The improvement is statistically solid and affordable", "t = 46.38, d_{z} = 1.33, p < 10^{−200} vs HPCF; training ≈ 1.78× HPCF, inference 1.84 ms per query.")],
                   N(65), refs_=cite(3))

    # --- C3 limitations ---------------------------------------------------------
    limitations_slide(ctx, C3, C1TABS, "Findings",
                      [("Compute overhead", "Roughly **1.78× the training time** of HPCF on MovieLens-1M (≈ 3.4× MF); acceptable, but not free."),
                       ("Needs meaningful context", "The largest single component is **context**; on data without usable context the gain shrinks."),
                       ("Monte Carlo variance", "M = 50 gives ≈ 99 % accuracy; **variance reduction** could cut the refresh cost further."),
                       ("Scope of the claim", "Component-wise ablation only; baselines fixed in early 2026, so superiority is claimed **only against the tested baselines**.")],
                      "None of these change the main message: attribution can **guide learning**, not only describe it.",
                      N(66))

    # --- C3 takeaway ------------------------------------------------------------
    takeaway_slide(ctx, C3, C1TABS, "Findings", "Contribution III",
                   "Attribution becomes a **first-class part of the learning objective**: the explanation is a direct read-out of what the model optimises, so it is **faithful by design**, not an outside approximation.",
                   [("First-class", "Shapley estimates shape the hyperedge weights during training."),
                    ("Read-out", "The waterfall shows the same terms the loss optimises: ranking, diversity, context, preference."),
                    ("Axiomatic", "Built on the four Shapley axioms, in line with trustworthy-AI expectations.")],
                   "From **post-hoc description** (C1, C2) to **in-training guidance** (C3): the strongest claim of the thesis.",
                   N(67))

    # ======================================================================
    # SECTION 7 — CONCLUSION
    # ======================================================================
    CTABS = ["Synthesis", "Publications", "Limitations", "Perspectives", "Conclusion"]
    CC = "Conclusion & Perspectives"
    section_slide(ctx, "07", "Conclusion", "Synthesis, publications, limitations and perspectives",
                  [("Synthesis", "Three contributions, one cooperative-game thread: faithful explanation → consistency across levels → in-training attribution."),
                   ("Limitations", "Approximation everywhere; surrogate fidelity; tabular and offline settings; no user study of actionability yet."),
                   ("Perspectives", "Scalable attribution, online / streaming recommendation, user-centred and trustworthy-AI evaluation.")],
                  notes=N(68))

    # --- Synthesis table -----------------------------------------------------
    s, top = content_slide(ctx, "Synthesis of the Three Contributions", eyebrow=CC, tabs=CTABS, active="Synthesis", notes=N(69), refs=cite(1, 2, 3))
    rows = [["", "Main idea", "Achievement", "Key finding"],
            ["C1", "Explain black-box clustering via Shapley", "PCA–K-Means–LightGBM–TreeSHAP pipeline", "Faithful, chemistry-consistent cluster attribution (wine)"],
            ["C2", "Multi-level, large-scale clustering XAI", "Cross-level SHAP aggregation + Proposition 6.1", "Consistent across levels; explains the differences between them"],
            ["C3", "DyHuCoG hypergraph cooperative game", "Preference-aware Shapley as an in-training signal", "Accuracy + coverage + diversity improve together"]]
    gf, th = table(s, L, top, W, rows, col_widths=[0.9, 3.4, 3.6, 4.7], size=16, head_size=16, row_h=emu(0.62), align=["ctr", "l", "l", "l"], header_align=["ctr", "l", "l", "l"], pad=0.08)
    for ri, f in ((1, GREEN), (2, "1F5C99"), (3, ORANGE)):
        c = gf.table.cell(ri, 0)
        c.fill.solid()
        c.fill.fore_color.rgb = RGBColor.from_string(f)
        fill_text_frame(c._tc.get_or_add_txBody(), [Para([Run(rows[ri][0], font="title", size=22, color=WHITE)], align="ctr", lnspc=26)], anchor="ctr")
    gy = top + th + emu(0.4)
    steps = [("Explain", "post-hoc, single level", GREEN), ("Scale", "post-hoc, hierarchical", "1F5C99"), ("Guide", "in-training signal", ORANGE)]
    n = 3
    bw = emu(4.4)
    gap = (W - n * bw) / (n - 1)
    bh = emu(0.9)
    for i, (t, sub, f) in enumerate(steps):
        x = L + i * (bw + gap)
        chip(s, x, gy, bw, bh, t, fill=f, size=21, sub=sub, sub_size=13, radius=emu(0.25))
        if i < n - 1:
            arrow(s, x + bw + emu(0.1), gy + bh / 2, x + bw + gap - emu(0.1), gy + bh / 2, color=GREEN, w=3)
    ty = gy + bh + emu(0.55)
    statement(s, L, ty, W, CB - ty - emu(0.3), "Takeaway  ·  Thesis",
              "One cooperative-game definition, three value functions: the same Shapley logic **explains** a partition, **stays consistent** across levels, and finally **guides** what a recommender learns.",
              fill=ORANGE, size=20)

    # --- Publications (table, correct author lists) -----------------------------
    s, top = content_slide(ctx, "Publications Supporting the Thesis", eyebrow=CC, tabs=CTABS, active="Publications", notes=N(70))
    rows = [["", "Authors", "Title", "Journal", "Year", "DOI", "Status"],
            ["I", "M. Louhichi, R. Nesmaoui, M. Mbarek, M. Lazaar", "Shapley Values for Explaining the Black Box Nature of Machine Learning Model Clustering", "Procedia Computer Science 220, 806–811", "2023", "10.1016/j.procs.2023.03.107", "Published"],
            ["II", "M. Louhichi, R. Nesmaoui, M. Lazaar", "Game Theory Meets Explainable AI: An Enhanced Approach to Understanding Black Box Models Through Shapley Values", "IJACSA 16(7), 716–725", "2025", "10.14569/IJACSA.2025.0160780", "Published"],
            ["III", "M. Louhichi, R. Nesmaoui, M. Lazaar", "DyHuCoG: A Dynamic Hypergraph Cooperative Game for Preference-aware Recommendation", "IJIES 19(2), 887–902", "2026", "10.22266/ijies2026.0228.54", "Published"]]
    al = ["ctr", "l", "l", "l", "ctr", "l", "ctr"]
    gf, th = table(s, L, top, W, rows, col_widths=[0.7, 3.0, 5.6, 3.4, 0.8, 2.6, 1.2], size=14, head_size=14, row_h=emu(0.9), align=al, header_align=al, pad=0.07)
    for ri, f in ((1, GREEN), (2, "1F5C99"), (3, ORANGE)):
        c = gf.table.cell(ri, 0)
        c.fill.solid()
        c.fill.fore_color.rgb = RGBColor.from_string(f)
        fill_text_frame(c._tc.get_or_add_txBody(), [Para([Run(rows[ri][0], font="title", size=24, color=WHITE)], align="ctr", lnspc=28)], anchor="ctr")
        c6 = gf.table.cell(ri, 6)
        c6.fill.solid()
        c6.fill.fore_color.rgb = RGBColor.from_string(GREEN_SOFT)
        for para in c6.text_frame.paragraphs:
            for r in para.runs:
                r.font.bold = True
                r.font.color.rgb = RGBColor.from_string(GREEN)
    by = top + th + emu(0.5)
    cw = (W - emu(0.4)) / 2
    light_card(s, L, by + emu(0.25), cw, CB - by - emu(0.5), label="Mapping to the thesis",
               paras=bullets(["**I** → Contribution I (Chapter 5)  ·  **II** → Contribution II (Chapter 6)  ·  **III** → Contribution III (Chapter 7).",
                              "Three journal articles, candidate as **first author**; IJACSA and IJIES are Scopus-indexed."], size=17, gap0=4), pad=(0.5, 0.6, 0.45, 0.2))
    card(s, L + cw + emu(0.4), by + emu(0.25), cw, CB - by - emu(0.5), label="Related work with the team",
         paras=bullets(["Nesmaoui, R., **Louhichi, M.** & Lazaar, M. Dynamic Recommender Systems with Real-time Shapley Value-based Contribution Adjustment. IJIES 18, 241–257 (2025): the same cooperative-game view, applied to real-time contribution adjustment."], size=16, color=WHITE, c0=YELLOW, c1=YELLOW, gap0=4), pad=(0.5, 0.6, 0.45, 0.2))

    # --- Limitations ---------------------------------------------------------
    s, top = content_slide(ctx, "Limitations, Stated Honestly", eyebrow=CC, tabs=CTABS, active="Limitations", notes=N(71))
    lims = [("Computational", "Exact Shapley is not feasible; every contribution relies on approximation, surrogates or limited reporting.", GREEN),
            ("Methodological", "Clustering depends on surrogate fidelity; recommendation depends on stable approximate contributions and useful context.", "1F5C99"),
            ("Empirical", "Tabular clustering + benchmark recommendation; no multimodal, sequential or online setting; no dedicated user study of actionability.", ORANGE),
            ("Claim scope", "A consistent and productive shared view, not one fully unified framework that removes all tension.", INK)]
    cells = grid(4, 2, L, top + emu(0.1), W, CB - top - emu(0.3), gap=emu(0.3), vgap=emu(0.3))
    for (h1, body, f), (x, y, w, h) in zip(lims, cells):
        box = rrect(s, x, y, w, h, fill=f, radius=emu(0.3))
        shape_text(box, [Para([Run(h1, font="title", size=30, color=YELLOW if f != ORANGE else WHITE, spc=-1.2)], lnspc=34),
                         Para([Run(body, font="body", size=20, color="F7F2EA")], lnspc=26, spcbef=12)],
                   anchor="ctr", insets=(emu(0.5), emu(0.3), emu(0.5), emu(0.3)))

    # --- Perspectives --------------------------------------------------------
    s, top = content_slide(ctx, "Perspectives: Turning Limitations into an Agenda", eyebrow=CC, tabs=CTABS, active="Perspectives", notes=N(72))
    per = [("01", "Scalable cooperative attribution", "Lower-variance Shapley estimators, learned proposal distributions, adaptive refresh rules."),
           ("02", "Online / streaming recommendation", "Truly incremental settings with changing graphs and delayed feedback; this also addresses the static-graph limitation."),
           ("03", "Richer user-centred evaluation", "Do explanations measurably improve analyst judgement, user trust, quality of action or perceived fairness?"),
           ("04", "Broader trustworthy-AI evaluation", "Exposure fairness, transparency requirements, auditing for governance.")]
    cells = grid(4, 2, L, top + emu(0.1), W, CB - top - emu(0.3), gap=emu(0.3), vgap=emu(0.3))
    for i, ((num, h1, body), (x, y, w, h)) in enumerate(zip(per, cells)):
        light = i % 3 == 1 or i == 2
        f = TINT if light else GREEN
        box = rrect(s, x, y, w, h, fill=f, radius=emu(0.3))
        badge(s, x + emu(0.4), y + emu(0.4), emu(0.8), num, fill=YELLOW if not light else ORANGE, color=INK if not light else WHITE, size=20)
        fit_textbox(s, x + emu(1.45), y + emu(0.35), w - emu(1.85), h - emu(0.6),
                    [H(h1, size=24, color=WHITE if not light else INK),
                     P(body, size=19, color="F1EDE6" if not light else INK, spcbef=8)], anchor="ctr", min_scale=0.7)

    # --- Conclusion: thesis answer + key outcomes -------------------------------
    s, top = content_slide(ctx, "Conclusion", eyebrow=CC, tabs=CTABS, active="Conclusion", notes=N(73), refs=cite(24, 26))
    sh = emu(1.7)
    statement(s, L, top + emu(0.2), W, sh, "Thesis answer",
              "Cooperative game theory can serve as a **shared methodological view for actionable explanation** across clustering and recommendation: the same Shapley logic explains, stays consistent across levels, and guides learning.",
              fill=GREEN, size=23)
    textbox(s, L, top + emu(0.2) + sh + emu(0.35), W, emu(0.35), [Para([Run("KEY OUTCOMES", font="xbold", size=14, color=ORANGE, spc=1.6)], lnspc=18)])
    outs = [("Common language", "Shapley attribution as a common formal language for assigning importance to features, interactions and contexts."),
            ("Three achievements", "Faithful clustering explanation, consistent multi-level explanation, contribution-aware recommendation learning."),
            ("Explanation as method", "Not a comment added later: from post-hoc description to in-training guidance."),
            ("Trustworthy AI", "Aligned with EU AI Act, OECD principles and GDPR expectations.")]
    oy = top + emu(0.2) + sh + emu(0.8)
    cells = grid(4, 4, L, oy, W, CB - oy - emu(0.3), gap=emu(0.3))
    for i, ((h1, body), (x, y, w, h)) in enumerate(zip(outs, cells)):
        f = [TINT, TINT2, TINT, TINT2][i]
        box = rrect(s, x, y, w, h, fill=f, line=None, radius=emu(0.3))
        badge(s, x + emu(0.35), y + emu(0.3), emu(0.55), f"{i+1}", fill=ORANGE, color=WHITE, size=17)
        fit_textbox(s, x + emu(0.35), y + emu(1.0), w - emu(0.7), h - emu(1.15),
                    [H(h1, size=21, color=GREEN), P(body, size=17, spcbef=6)], min_scale=0.7)

    # --- References (all numbered footnotes, two slides) -----------------------
    def references_slide(title, items, notes):
        s, top = content_slide(ctx, title, eyebrow=CC, tabs=None, notes=notes)
        n = len(items)
        gap = emu(0.06)
        y = top - emu(0.25)
        rh = (CB - y - gap * (n - 1)) / n
        for i, (num, t) in enumerate(items):
            yy = y + i * (rh + gap)
            rrect(s, L, yy, W, rh, fill=TINT if i % 2 == 0 else TINT2, radius=emu(0.1))
            chip(s, L + emu(0.12), yy + emu(0.06), emu(0.7), rh - emu(0.12), f"[{num}]", fill=GREEN if num <= 3 else ORANGE, size=12, radius=emu(0.08))
            fit_textbox(s, L + emu(1.0), yy, W - emu(1.15), rh, [P(t, size=13)], anchor="ctr", min_scale=0.7)
        return s

    all_refs = list(enumerate(REFS, start=1))
    references_slide("References (1 / 2)", all_refs[:14], N(74))
    references_slide("References (2 / 2)", all_refs[14:], N("refs2"))

    # ======================================================================
    # THANK YOU (template slide 15 style)
    # ======================================================================
    ctx.n += 1
    s = deck.new_slide()
    # grid background like template
    accent(s, "grid", -emu(1.25), 0, emu(11.25))
    accent(s, "grid", emu(10.0), 0, emu(11.25))
    chrome(s, ctx.n)
    textbox(s, L, emu(2.75), W, emu(3.6),
            [Para([Run("Thank You", font="title", size=150, color=INK, spc=-8)], align="ctr", lnspc=150),
             Para([Run("for your attention", font="title", size=72, color=INK, spc=-3.5)], align="ctr", lnspc=84, spcbef=4)])
    accent(s, "asterisk_o", SLIDE_W / 2 + emu(4.6), emu(2.7), emu(0.9))
    accent(s, "fan_y", SLIDE_W / 2 - emu(6.4), emu(5.3), emu(0.75), rot=-15)
    badge(s, R - emu(1.8), emu(6.3), emu(1.1), "?", fill=GREEN, color=WHITE, size=40, font="title")
    textbox(s, L, emu(7.2), W, emu(0.7),
            [Para([Run("Questions & Discussion  ·  I welcome your questions and comments.", font="bold", size=28, color=GREEN)], align="ctr", lnspc=34)])
    # contact strip
    items = [("Candidate", "Mouad LOUHICHI"), ("Supervisor", "Pr. Mohamed LAZAAR"), ("Laboratory", "ENSIAS · UM5 Rabat"), ("Defence", "Rabat · 2026")]
    cells = grid(4, 4, L, emu(8.55), W, emu(1.15), gap=emu(0.3))
    for (h1, v), (x, y, w, h) in zip(items, cells):
        box = rrect(s, x, y, w, h, fill=WHITE, line=RULE, line_w=1.25, radius=emu(0.2))
        shape_text(box, [Para([Run(h1.upper(), font="xbold", size=13, color=ORANGE, spc=1.5)], align="ctr", lnspc=16),
                         Para([Run(v, font="xbold", size=20, color=INK)], align="ctr", lnspc=24, spcbef=4)], anchor="ctr")
    set_notes(s, N(75))

    # ======================================================================
    # CLOSING TITLE SLIDE (jury in front of the panel during Q&A)
    # ======================================================================
    title_slide(ctx, deck, notes=N("closing"), closing=True)

    # ======================================================================
    # BACKUP SLIDES (after the end; shown only if a question calls for them)
    # ======================================================================
    ctx.section = None
    # v10: the 'Backup Slides' index slide is removed; the three backup slides are
    # self-labelled and the reference deck also goes straight into them.

    BK = "Backup"
    # --- Table 7.1 full -----------------------------------------------------------
    s, top = content_slide(ctx, "Backup: Table 7.1, Full Results (mean ± std, 5 seeds)", eyebrow=BK, tabs=None, notes=N("backup_71"), refs=cite(3))
    al = ["l", "ctr", "ctr", "ctr", "ctr"]
    full = [("MovieLens-1M", [["Model", "NDCG@20", "Recall@20", "Coverage", "ILD"],
                              ["MF", "0.1200 ± 0.0025", "0.0880 ± 0.0020", "0.239 ± 0.010", "0.367 ± 0.009"],
                              ["NCF", "0.1300 ± 0.0026", "0.1100 ± 0.0022", "0.269 ± 0.011", "0.398 ± 0.008"],
                              ["LightGCN", "0.2130 ± 0.0030", "0.1790 ± 0.0027", "0.308 ± 0.010", "0.423 ± 0.007"],
                              ["RecDCL", "0.2296 ± 0.0032", "0.1918 ± 0.0029", "0.324 ± 0.010", "0.445 ± 0.007"],
                              ["HCCF", "0.2470 ± 0.0035", "0.2050 ± 0.0031", "0.327 ± 0.009", "0.448 ± 0.006"],
                              ["HPCF", "0.2528 ± 0.0036", "0.2098 ± 0.0032", "0.342 ± 0.009", "0.461 ± 0.006"],
                              ["DyHuCoG", "0.2775 ± 0.0039", "0.2362 ± 0.0036", "0.397 ± 0.011", "0.516 ± 0.005"]]),
            ("Amazon-Book", [["Model", "NDCG@20", "Recall@20", "Coverage", "ILD"],
                             ["MF", "0.0049 ± 0.0005", "0.0093 ± 0.0009", "0.168 ± 0.013", "0.425 ± 0.014"],
                             ["NCF", "0.0085 ± 0.0008", "0.0142 ± 0.0014", "0.193 ± 0.012", "0.458 ± 0.013"],
                             ["LightGCN", "0.0236 ± 0.0024", "0.0320 ± 0.0032", "0.226 ± 0.011", "0.491 ± 0.012"],
                             ["RecDCL", "0.0255 ± 0.0026", "0.0346 ± 0.0035", "0.242 ± 0.010", "0.512 ± 0.011"],
                             ["HCCF", "0.0258 ± 0.0026", "0.0344 ± 0.0034", "0.248 ± 0.010", "0.520 ± 0.011"],
                             ["HPCF", "0.0270 ± 0.0027", "0.0359 ± 0.0036", "0.259 ± 0.010", "0.535 ± 0.011"],
                             ["DyHuCoG", "0.0306 ± 0.0031", "0.0417 ± 0.0042", "0.336 ± 0.012", "0.602 ± 0.010"]])]
    cw = (W - emu(0.5)) / 2
    for i, (name, rows) in enumerate(full):
        x = L + i * (cw + emu(0.5))
        textbox(s, x, top - emu(0.05), cw, emu(0.35), [Para([Run(name.upper(), font="xbold", size=13, color=ORANGE, spc=1.5)], lnspc=16)])
        gf, th = table(s, x, top + emu(0.35), cw, rows, col_widths=[1.7, 2.2, 2.2, 1.9, 1.9], size=14, head_size=14, align=al, header_align=al, row_h=emu(0.52), pad=0.06)
        bold_row(gf, len(rows) - 1, 5)
    by = top + emu(0.35) + th + emu(0.35)
    bar = rrect(s, L, by, W, min(emu(0.9), CB - by - emu(0.3)), fill=TINT, radius=emu(0.22))
    shape_text(bar, [Para(md_runs("Standard deviations are roughly **one tenth of the gap** between DyHuCoG and HPCF on every metric, so the ordering is stable across seeds.", size=17, color=INK), align="ctr", lnspc=22)], anchor="ctr", insets=(emu(0.4), emu(0.05), emu(0.4), emu(0.05)))

    # --- Table 7.6 significance ---------------------------------------------------
    s, top = content_slide(ctx, "Backup: Table 7.6, Paired Tests vs Every Baseline", eyebrow=BK, tabs=None, notes=N("backup_76"), refs=cite(27))
    rows = [["Comparison (per-user NDCG@20, ML-1M)", "t statistic", "p-value", "Cohen's d_{z}", "Holm threshold α", "Result"],
            ["DyHuCoG vs HPCF", "46.38", "1.81 × 10^{−270}", "1.33", "0.0500", "significant"],
            ["DyHuCoG vs RecDCL", "92.72", "< 10^{−300}", "2.67", "0.0083", "significant"],
            ["DyHuCoG vs HCCF", "61.21", "< 10^{−300}", "1.76", "0.0100", "significant"],
            ["DyHuCoG vs LightGCN", "132.19", "< 10^{−300}", "3.80", "0.0125", "significant"],
            ["DyHuCoG vs NCF", "311.13", "< 10^{−300}", "8.95", "0.0167", "significant"],
            ["DyHuCoG vs MF", "341.76", "< 10^{−300}", "9.83", "0.0250", "significant"]]
    al = ["l", "ctr", "ctr", "ctr", "ctr", "ctr"]
    gf, th = table(s, L, top, W, rows, col_widths=[4.6, 2.0, 2.6, 2.0, 2.4, 2.2], size=17, head_size=16, align=al, header_align=al, row_h=emu(0.62))
    by = top + th + emu(0.45)
    cw = (W - emu(0.4)) / 2
    light_card(s, L, by + emu(0.25), cw, CB - by - emu(0.55), label="How to read it",
               paras=bullets(["Paired t-test over **6,040 users** (df = 6,039); Holm–Bonferroni gives each of the six p-values its own threshold.",
                              "Every p-value is far below its threshold; **Wilcoxon** agrees (p < 0.001)."], size=16, gap0=4), pad=(0.5, 0.6, 0.45, 0.2))
    card(s, L + cw + emu(0.4), by + emu(0.25), cw, CB - by - emu(0.55), label="Effect size",
         paras=bullets(["Cohen's d_{z} ≥ 1.33 everywhere: **large** (0.8) is exceeded even against the strongest baseline.",
                        "The improvement is practically meaningful, not only statistically visible."], size=16, color=WHITE, c0=YELLOW, c1=YELLOW, gap0=4), pad=(0.5, 0.6, 0.45, 0.2))

    # --- Tables 7.3 / 7.4 efficiency ---------------------------------------------
    s, top = content_slide(ctx, "Backup: Tables 7.3 and 7.4, Cost and Convergence", eyebrow=BK, tabs=None, notes=N("backup_73"), refs=cite(3, 8))
    lw = emu(11.2)
    rows = [["Model", "Train (s) ML-1M", "Infer (ms)", "Mem (GB)", "Train (s) Amazon", "Infer (ms)", "Mem (GB)", "× MF (ML-1M)"],
            ["MF", "485", "0.54", "2.1", "2,202", "2.46", "8.5", "1.00"],
            ["NCF", "675", "0.76", "2.7", "3,073", "3.42", "11.1", "1.41"],
            ["LightGCN", "786", "0.88", "3.2", "3,645", "4.05", "12.8", "1.63"],
            ["RecDCL", "968", "1.02", "3.6", "4,527", "5.04", "15.6", "1.89"],
            ["HCCF", "952", "1.06", "3.8", "4,419", "4.92", "15.3", "1.96"],
            ["HPCF", "1,125", "1.18", "4.1", "5,234", "5.48", "16.8", "2.19"],
            ["DyHuCoG", "2,000", "1.84", "4.4", "9,279", "8.52", "17.9", "3.41"]]
    al = ["l"] + ["ctr"] * 7
    textbox(s, L, top - emu(0.05), lw, emu(0.35), [Para([Run("TABLE 7.3  ·  RUNTIME AND MEMORY", font="xbold", size=13, color=ORANGE, spc=1.5)], lnspc=16)])
    gf, th = table(s, L, top + emu(0.35), lw, rows, col_widths=[1.6, 1.7, 1.2, 1.2, 1.8, 1.2, 1.2, 1.0], size=14, head_size=13, align=al, header_align=al, row_h=emu(0.5), pad=0.06)
    bold_row(gf, len(rows) - 1, 8)
    dx = L + lw + emu(0.5)
    dw = R - dx
    rows2 = [["M", "MSE", "Accuracy", "Train (s)", "× base"],
             ["10", "1.4 × 10^{−4}", "95 %", "≈ 1,460", "1.3×"],
             ["25", "5.6 × 10^{−5}", "98 %", "≈ 1,800", "1.6×"],
             ["50", "1.4 × 10^{−5}", "99 %", "2,001", "1.78×"],
             ["100", "3.5 × 10^{−6}", "99.5 %", "≈ 2,810", "2.5×"]]
    al2 = ["ctr"] * 5
    textbox(s, dx, top - emu(0.05), dw, emu(0.35), [Para([Run("TABLE 7.4  ·  MONTE CARLO SHAPLEY", font="xbold", size=13, color=ORANGE, spc=1.5)], lnspc=16)])
    gf2, th2 = table(s, dx, top + emu(0.35), dw, rows2, col_widths=[0.8, 1.6, 1.3, 1.3, 1.0], size=14, head_size=13, align=al2, header_align=al2, row_h=emu(0.5), pad=0.06)
    bold_row(gf2, 3, 5)
    by = top + emu(0.35) + max(th, th2) + emu(0.4)
    bar = rrect(s, L, by, W, min(emu(1.1), CB - by - emu(0.3)), fill=TINT, radius=emu(0.22))
    shape_text(bar, [Para(md_runs("DyHuCoG costs about **1.78× HPCF** in training time and stays under **2 ms per query** on MovieLens-1M; M = 50 permutations is the knee of the accuracy / cost curve, which is why it is the default.", size=17, color=INK), align="ctr", lnspc=22)], anchor="ctr", insets=(emu(0.4), emu(0.05), emu(0.4), emu(0.05)))

    deck.finalize(out)
    return ctx.n


if __name__ == "__main__":
    tpl_path = sys.argv[1]
    out_path = sys.argv[2]
    n = build(tpl_path, out_path)
    print(f"built {n} slides -> {out_path}")
    for slide_no, scale, what in FIT_REPORT:
        print(f"  fit note: slide {slide_no} scaled to {scale:.2f}: {what}")
