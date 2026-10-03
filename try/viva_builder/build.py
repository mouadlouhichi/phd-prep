"""
Build MOUAD_LOUHICHI_VIVA_40min on the
"Beige Green Modern Illustrative Playful Thesis Defense Presentation" template.

Usage:  python3 build.py <template.pptx> <out.pptx>
"""
import json
import os
import sys

from layouts import *  # noqa
from layouts import _ss_runs, FIT_REPORT

HERE = os.path.dirname(os.path.abspath(__file__))
FIGS = os.environ.get("VIVA_FIG_DIR", "/tmp/viva_build/figs")
NOTES = json.load(open(os.path.join(HERE, "notes_speech.json")))


def N(*orig):
    """Speaker notes: merge notes of the original slide numbers."""
    return "\n\n".join(NOTES[str(o)] for o in orig if NOTES.get(str(o)))


def build(template, out):
    deck = Deck(template)
    ctx = Ctx(deck)

    # ======================================================================
    # 1. TITLE
    # ======================================================================
    ctx.n += 1
    s = deck.new_slide()
    # logos row
    picture(s, os.path.join(FIGS, "um5_logo.png"), L, emu(0.55), h=emu(1.05))
    picture(s, os.path.join(FIGS, "ministry_logo.png"), SLIDE_W / 2 - emu(1.3), emu(0.45), h=emu(1.3))
    picture(s, os.path.join(FIGS, "ensias_logo.jpg"), R - emu(1.65), emu(0.5), h=emu(1.15))
    textbox(s, L, emu(1.85), W, emu(0.4),
            [Para([Run("Doctoral Studies Center in Information and Engineering Sciences and Technologies (ST2I)",
                       font="bold", size=17, color=MUTED)], align="ctr", lnspc=22)])
    textbox(s, L, emu(2.5), W, emu(0.4),
            [Para([Run("PHD THESIS DEFENCE  ·  COMPUTER SCIENCE", font="xbold", size=16, color=ORANGE, spc=2)], align="ctr", lnspc=22)])
    textbox(s, L, emu(2.95), W, emu(2.6),
            [Para([Run("Cooperative Game Theory for", font="title", size=64, color=INK, spc=-3.5)], align="ctr", lnspc=70),
             Para([Run("Explainable AI in Recommendation Systems", font="title", size=64, color=INK, spc=-3.5)], align="ctr", lnspc=70)])
    textbox(s, L, emu(5.25), W, emu(0.6),
            [Para([Run("A Shapley Framework for Actionable Insight", font="bold", size=30, color=GREEN, spc=-1.2)], align="ctr", lnspc=36)])
    accent(s, "asterisk_o", R - emu(1.45), emu(2.8), emu(0.7))
    accent(s, "sparkle_y", L + emu(0.1), emu(4.9), emu(0.55), rot=20)
    # presenter + supervisor cards
    cy = emu(6.25)
    ch = emu(1.15)
    cw = emu(7.2)
    c1 = rrect(s, SLIDE_W / 2 - cw - emu(0.2), cy, cw, ch, fill=GREEN, radius=emu(0.3))
    shape_text(c1, [Para([Run("PRESENTED BY", font="xbold", size=13, color=YELLOW, spc=1.5)], align="ctr", lnspc=16),
                    Para([Run("Mouad LOUHICHI", font="xbold", size=27, color=WHITE)], align="ctr", lnspc=32, spcbef=3)],
               anchor="ctr")
    c2 = rrect(s, SLIDE_W / 2 + emu(0.2), cy, cw, ch, fill=TINT, line=None, radius=emu(0.3))
    shape_text(c2, [Para([Run("SUPERVISED BY", font="xbold", size=13, color=ORANGE, spc=1.5)], align="ctr", lnspc=16),
                    Para([Run("Pr. Mohamed LAZAAR  ·  PES, ENSIAS", font="xbold", size=23, color=INK)], align="ctr", lnspc=28, spcbef=3)],
               anchor="ctr")
    # jury table
    jy = emu(7.75)
    textbox(s, L, jy, W, emu(0.35), [Para([Run("JURY MEMBERS", font="xbold", size=14, color=MUTED, spc=2)], align="ctr", lnspc=18)])
    jury = [
        ("President", "[to complete]", "[Institution]"),
        ("Reviewer", "[to complete]", "[Institution]"),
        ("Reviewer", "[to complete]", "[Institution]"),
        ("Reviewer", "[to complete]", "[Institution]"),
        ("Examiner", "[to complete]", "[Institution]"),
        ("Examiner", "[to complete]", "[Institution]"),
        ("Examiner", "[to complete]", "[Institution]"),
        ("Guest", "[to complete]", "[Institution]"),
        ("Supervisor", "Pr. Mohamed LAZAAR", "PES, ENSIAS · UM5 Rabat"),
    ]
    cells = grid(9, 3, L, jy + emu(0.4), W, emu(2.05), gap=emu(0.2), vgap=emu(0.14))
    for (role, name, inst), (x, y, w, h) in zip(jury, cells):
        box = rrect(s, x, y, w, h, fill=WHITE, line=RULE, line_w=1.25, radius=emu(0.14))
        shape_text(box, [Para([Run(role.upper(), font="xbold", size=11, color=ORANGE, spc=1.2)], lnspc=13),
                         Para([Run(name, font="bold", size=16, color=INK)], lnspc=19, spcbef=1),
                         Para([Run(inst, font="body", size=13, color=MUTED)], lnspc=15)],
                   anchor="ctr", insets=(emu(0.2), emu(0.05), emu(0.1), emu(0.05)))
    textbox(s, L, emu(10.55), W, emu(0.35), [Para([Run("Rabat, Morocco  ·  2026", font="bold", size=16, color=MUTED)], align="ctr", lnspc=20)])
    set_notes(s, N(1))

    # ======================================================================
    # 2. OUTLINE (template "Overview" style)
    # ======================================================================
    ctx.n += 1
    s = deck.new_slide()
    chrome(s, ctx.n)
    textbox(s, L, emu(1.9), W, emu(1.6), [Para([Run("Outline", font="title", size=92, color=INK, spc=-5)], align="ctr", lnspc=96)])
    accent(s, "sparkle_o", SLIDE_W / 2 + emu(2.7), emu(1.7), emu(0.6))
    accent(s, "sparkle_y", SLIDE_W / 2 - emu(3.5), emu(2.9), emu(0.55), rot=180)
    textbox(s, L, emu(3.55), W, emu(0.5), [Para([Run("Five parts  ·  each contribution follows the same structure: objectives → methodology → results → findings",
                                                     font="body", size=21, color=MUTED)], align="ctr", lnspc=26)])
    parts = [
        ("01", "Introduction", "Motivation · Actionable insight · Why XAI matters"),
        ("02", "Context & Problematic", "Approaches · Limitations · Research questions"),
        ("03", "Experimental Protocol", "Datasets · Baselines · Metrics · Hardware"),
        ("04", "Contribution I", "Explainable black-box clustering (Wine)"),
        ("05", "Contribution II", "Multi-level XAI for large-scale clustering (Beijing)"),
        ("06", "Contribution III", "DyHuCoG: a cooperative game on hypergraphs"),
        ("07", "Conclusion & Perspectives", "Synthesis · Limitations · Future work"),
    ]
    cells = grid(8, 4, L, emu(4.45), W, emu(5.4), gap=emu(0.3), vgap=emu(0.3))
    for i, (num, head, sub) in enumerate(parts):
        x, y, w, h = cells[i]
        dark = i % 2 == 0
        box = rrect(s, x, y, w, h, fill=GREEN if dark else None, line=None if dark else GREEN, line_w=2.25, radius=emu(0.4))
        shape_text(box, [Para([Run(num, font="xbold", size=30, color=YELLOW if dark else ORANGE)], lnspc=34),
                         Para([Run(head, font="xbold", size=25, color=WHITE if dark else INK)], lnspc=29, spcbef=6),
                         Para([Run(sub, font="body", size=17, color="DCE7E3" if dark else MUTED)], lnspc=21, spcbef=6)],
                   anchor="t", insets=(emu(0.4), emu(0.4), emu(0.35), emu(0.3)))
    # last cell: thanks / Q&A
    x, y, w, h = cells[7]
    box = rrect(s, x, y, w, h, fill=YELLOW, radius=emu(0.4))
    shape_text(box, [Para([Run("Q & A", font="title", size=44, color=INK, spc=-2)], align="ctr", lnspc=48),
                     Para([Run("Discussion with the jury", font="bold", size=18, color=INK)], align="ctr", lnspc=22, spcbef=6)], anchor="ctr")
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
                           tabs=["Motivation", "Actionable Insight", "Research Context"], active="Motivation", notes=N(4))
    qs = [("Everywhere", "How do black-box AI systems shape what billions of users see, buy and watch every day?",
           "Recommenders shape news, study, health and credit decisions; market > $15B by 2029."),
          ("The Black Box", "Why do state-of-the-art recommenders and clustering pipelines stay black boxes for users and designers?",
           "Deep & graph models: hidden logic, hard to audit. EU AI Act: high-risk → must explain."),
          ("Toward Trust", "How can transparency be built into the model, instead of being added afterwards?",
           "Insight that is accountable, auditable and actionable, not just accurate.")]
    cells = grid(3, 3, L, top + emu(0.25), W, emu(4.6), gap=emu(0.35))
    for (head, q, sub), (x, y, w, h) in zip(qs, cells):
        card(s, x, y, w, h, label=head, paras=[P(q, size=23, color=WHITE, font="bold"),
                                                 Para([Run(sub, font="body", size=18, color="CFDAD6")], lnspc=23, spcbef=14)],
             pad=(0.5, 0.75, 0.5, 0.4), label_size=21)
    # tension bar
    ty = top + emu(0.25) + emu(4.6) + emu(0.35)
    bar = rrect(s, L, ty, W, emu(0.95), fill=TINT, radius=emu(0.25))
    shape_text(bar, [Para(md_runs("**The core tension:** as models gain power, they lose the transparency needed for trustworthy use. "
                                  "This thesis treats **accuracy and interpretability as goals to be met together**, not traded against each other.",
                                  size=20, color=INK), align="ctr", lnspc=26)], anchor="ctr", insets=(emu(0.4), emu(0.1), emu(0.4), emu(0.1)))

    # --- Actionable insight — definition --------------------------------------
    s, top = content_slide(ctx, "Actionable Insight: the Definition", eyebrow="Introduction",
                           tabs=["Motivation", "Actionable Insight", "Research Context"], active="Actionable Insight", notes=N(5))
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
                           tabs=["Motivation", "Actionable Insight", "Research Context"], active="Research Context", notes=N(6))
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

    # --- AI recommenders around us -------------------------------------------
    s, top = content_slide(ctx, "AI-Powered Recommendation Is Everywhere", eyebrow="Introduction",
                           tabs=["Motivation", "Actionable Insight", "Research Context"], active="Research Context", notes=N(7))
    domains = [("Streaming & Video", "Netflix · Prime Video · YouTube"), ("Music", "Spotify · YouTube Music · Deezer"),
               ("Shopping & E-commerce", "Amazon · AliExpress · Noon"), ("Social & Feeds", "TikTok · Instagram · LinkedIn"),
               ("Maps & Mobility", "Google Maps · Uber · Booking"), ("Ads & Search", "Google Ads · Bing · Meta")]
    cells = grid(6, 3, L, top + emu(0.1), W, emu(4.4), gap=emu(0.3), vgap=emu(0.3))
    for i, ((h1, h2), (x, y, w, h)) in enumerate(zip(domains, cells)):
        f = [GREEN, "1E5F58", ORANGE][i % 3] if i % 3 != 2 else ORANGE
        f = GREEN if i in (0, 4) else ("1E5F58" if i in (1, 3) else ORANGE)
        chip(s, x, y, w, h, h1, fill=f, color=WHITE, size=25, sub=h2, sub_size=17, sub_color="F1EDE6", radius=emu(0.3))
    by = top + emu(0.1) + emu(4.4) + emu(0.4)
    bar = rrect(s, L, by, W, CB - by - emu(0.1), fill=TINT, radius=emu(0.3))
    shape_text(bar, [Para(md_runs("AI recommendation shapes what **billions** see, buy and listen to every day. Each system is very **accurate, yet a black box**: "
                                  "its reasoning is hidden from the user. Everywhere, and hidden: that is **exactly the gap this thesis targets**.", size=22, color=INK),
                          align="ctr", lnspc=29)], anchor="ctr", insets=(emu(0.6), emu(0.1), emu(0.6), emu(0.1)))

    # ======================================================================
    # SECTION 2 — CONTEXT & PROBLEMATIC
    # ======================================================================
    section_slide(ctx, "02", "Context & Problematic", "The main approaches, their limitations and the five research questions",
                  [("Approaches", "Collaborative, content-based, hybrid, matrix factorisation and graph/hypergraph recommenders: each one stronger, each one less transparent."),
                   ("Problematic", "Three main limitations: lack of explainability, difficulty of scaling, weak link between explanation and learning."),
                   ("Contributions", "Five research questions answered by three contributions that build on each other, under one cooperative-game view.")],
                  notes=N(8))

    # --- Paradigms -----------------------------------------------------------
    s, top = content_slide(ctx, "Recommendation & Clustering Approaches", eyebrow="Context & Problematic",
                           tabs=["Approaches", "Problematic", "Contributions"], active="Approaches", notes=N(9))
    lw = emu(8.7)
    fit_textbox(s, L, top, lw, CB - top - emu(0.2), bullets([
        "**Collaborative filtering:** users who behaved alike will like similar items (user- or item-based).",
        "**Content-based:** recommends items whose features match the user profile.",
        "**Hybrid:** combines both kinds of signal.",
        "**Matrix factorisation:** R ≈ PQ^{T}, compact but hidden latent factors.",
        "**Graph-based:** an interaction graph with neighbourhood propagation (LightGCN, hypergraph).",
        "Each step makes the model stronger but harder to read: MF hid the meaning of latent factors; graph models left importance implicit; hypergraphs assumed **all messages matter equally**.",
    ], size=21, gap0=10), min_scale=0.7)
    # right: content-based example diagram
    dx = L + lw + emu(0.6)
    dw = R - dx
    textbox(s, dx, top, dw, emu(0.4), [Para([Run("CONTENT-BASED FILTERING  ·  AN EXPLAINABLE EXAMPLE", font="xbold", size=14, color=ORANGE, spc=1.4)], align="ctr", lnspc=18)])
    steps = [("User taste profile", GREEN), ("Item feature vectors", GREEN), ("Similarity score", INK), ("Top-N recommend", ORANGE)]
    n = len(steps)
    bw = emu(1.72)
    gap = (dw - n * bw) / (n - 1)
    by = top + emu(0.65)
    bh = emu(1.3)
    for i, (t, f) in enumerate(steps):
        x = dx + i * (bw + gap)
        chip(s, x, by, bw, bh, t, fill=f, color=WHITE, size=16, radius=emu(0.2))
        if i < n - 1:
            arrow(s, x + bw + emu(0.05), by + bh / 2, x + bw + gap - emu(0.05), by + bh / 2, color=GREEN, w=2.25)
    ey = by + bh + emu(0.4)
    textbox(s, dx, ey, dw, emu(0.5), [Para(md_runs("**Example:** liked sci-fi + Nolan  →  suggest films with a similar genre, cast or keywords", size=17, color=INK), align="ctr", lnspc=22)])
    cw = (dw - emu(0.3)) / 2
    light_card(s, dx, ey + emu(0.75), cw, emu(1.9), label="Candidate item features",
               paras=[P("genre = Sci-Fi · director = Nolan\ncast = … · year = 2010 · rating = 8.6", size=15, color=INK)], pad=(0.3, 0.55, 0.3, 0.2), label_size=15)
    light_card(s, dx + cw + emu(0.3), ey + emu(0.75), cw, emu(1.9), label="Why recommended",
               paras=[P("high cosine similarity to your profile\n**sim = cos(f_user, f_item)**", size=15, color=INK)], pad=(0.3, 0.55, 0.3, 0.2), label_size=15)
    bar = rrect(s, dx, ey + emu(2.95), dw, CB - (ey + emu(2.95)) - emu(0.2), fill=GREEN, radius=emu(0.25))
    shape_text(bar, [Para(md_runs("Explainable because the factors are **domain-level and can be changed**: exactly what is lost when latent factors and message passing take over.", size=17, color=WHITE), align="ctr", lnspc=22)],
               anchor="ctr", insets=(emu(0.35), emu(0.1), emu(0.35), emu(0.1)))

    # --- Limitations ---------------------------------------------------------
    s, top = content_slide(ctx, "Limitations of Classical Recommenders & Unsupervised Models", eyebrow="Context & Problematic",
                           tabs=["Approaches", "Problematic", "Contributions"], active="Problematic", notes=N(10))
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
                           tabs=["Approaches", "Problematic", "Contributions"], active="Problematic", notes=N(11))
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
        f = [GREEN, "1E5F58", ORANGE][i]
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

    # --- Our thesis ----------------------------------------------------------
    s, top = content_slide(ctx, "Our Thesis in One View", eyebrow="Context & Problematic",
                           tabs=["Approaches", "Problematic", "Contributions"], active="Contributions", notes=N(14))
    lw = emu(7.6)
    fit_textbox(s, L, top, lw, CB - top - emu(0.2), [
        H("Thesis", size=25, color=GREEN),
        P("Cooperative game theory (Shapley) is **one shared, explainable way to attribute importance**.", size=21, spcbef=6),
        H("The same logic spans clustering and recommendation", size=22, color=GREEN, spcbef=18),
        *bullets(["**C1:** explains black-box clustering faithfully (wine).",
                  "**C2:** keeps the explanation consistent at scale and across levels (Beijing).",
                  "**C3:** DyHuCoG turns attribution into an **in-training signal**."], size=20, gap0=6),
        P("**From post-hoc description to in-training guidance.**", size=22, color=ORANGE, spcbef=18),
    ], min_scale=0.7)
    # right: tree diagram
    dx = L + lw + emu(0.7)
    dw = R - dx
    n1 = chip(s, dx + dw * 0.15, top + emu(0.05), dw * 0.7, emu(1.0), "Everyday AI recommenders are powerful but not transparent", fill=GREEN, size=18, radius=emu(0.2))
    n2 = chip(s, dx + dw * 0.08, top + emu(1.65), dw * 0.84, emu(1.2), "Our thesis: cooperative game theory (Shapley) as one shared, explainable attribution method", fill=INK, size=18, radius=emu(0.2))
    arrow(s, dx + dw / 2, top + emu(1.08), dx + dw / 2, top + emu(1.6), color=GREEN)
    leaves = [("C1", "Explainable clustering", GREEN), ("C2", "Multi-level XAI", "1E5F58"), ("C3", "DyHuCoG recommender", ORANGE)]
    cells = grid(3, 3, dx, top + emu(3.75), dw, emu(1.7), gap=emu(0.3))
    for (tag, t, f), (x, y, w, h) in zip(leaves, cells):
        chip(s, x, y, w, h, tag, fill=f, size=26, sub=t, sub_size=16, radius=emu(0.2))
        arrow(s, dx + dw / 2, top + emu(2.9), x + w / 2, y - emu(0.05), color=GREEN, w=2)
    by = top + emu(5.8)
    bar = rrect(s, dx, by, dw, CB - by - emu(0.2), fill=TINT, radius=emu(0.25))
    shape_text(bar, [Para(md_runs("Same axioms · same terms · same value-function logic: **explanation as part of the method, not a comment added later.**", size=17, color=INK), align="ctr", lnspc=22)],
               anchor="ctr", insets=(emu(0.3), emu(0.1), emu(0.3), emu(0.1)))

    # ======================================================================
    # SECTION 3 — EXPERIMENTAL PROTOCOL
    # ======================================================================
    section_slide(ctx, "03", "Experimental Protocol", "One shared protocol so that the three contributions can be read together",
                  [("Datasets", "Wine Quality and Beijing Air Quality for clustering; MovieLens-1M and Amazon-Book for recommendation."),
                   ("Baselines & metrics", "LIME for clustering explanation; MF → HPCF for recommendation; NDCG@20, Recall, Coverage, ILD, Silhouette, Davies–Bouldin."),
                   ("Reproducibility", "Fixed seeds, time-ordered user-level splits, early stopping, standard academic hardware (i9-14900K + RTX 4090).")],
                  notes=N(15))

    # --- Datasets table ------------------------------------------------------
    s, top = content_slide(ctx, "Datasets Used Throughout the Thesis", eyebrow="Experimental Protocol",
                           tabs=["Datasets", "Metrics", "Hardware"], active="Datasets", notes=N(16, 17))
    rows = [["Dataset", "Scale", "Type", "Role", "Why it was chosen"],
            ["Wine Quality (vinho verde)", "4,898 × 11", "Tabular, numeric", "C1: single-level clustering", "11 interpretable chemical features; small, dense, strongly correlated → attribution in a feature space experts trust."],
            ["Beijing Multi-Site Air Quality", "383,585 × 11", "Tabular, pollutants + weather", "C2: multi-level clustering", "Hourly records → tests scale, noise, and time / weather structure."],
            ["MovieLens-1M", "6,040 u / 3,706 i / 1.0 M int.", "Implicit feedback (density 0.0447)", "C3: DyHuCoG", "Standard benchmark with well-known baselines."],
            ["Amazon-Book", "52,643 u / 91,599 i / 3.0 M int.", "Implicit feedback (density 0.0006)", "C3: DyHuCoG", "Very sparse, on purpose → stress-tests Shapley weighting when the signal is weak."]]
    gf, th = table(s, L, top, W, rows, col_widths=[2.6, 2.4, 2.3, 2.2, 5.2], size=17, head_size=17, row_h=emu(0.95))
    by = top + th + emu(0.4)
    bar = rrect(s, L, by, W, min(emu(1.0), CB - by - emu(0.1)), fill=GREEN, radius=emu(0.25))
    shape_text(bar, [Para(md_runs("The **0.0447 vs 0.0006** density contrast is on purpose: the claim is that **gains are largest where data are weakest**.", size=21, color=WHITE), align="ctr", lnspc=27)],
               anchor="ctr", insets=(emu(0.5), emu(0.1), emu(0.5), emu(0.1)))

    # --- Splitting & preprocessing -------------------------------------------
    s, top = content_slide(ctx, "Data Splitting & Preprocessing", eyebrow="Experimental Protocol",
                           tabs=["Datasets", "Metrics", "Hardware"], active="Datasets", notes=N(18))
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

    # --- Baselines & metrics -------------------------------------------------
    s, top = content_slide(ctx, "Baselines & Evaluation Metrics", eyebrow="Experimental Protocol",
                           tabs=["Datasets", "Metrics", "Hardware"], active="Metrics", notes=N(19))
    lw = emu(7.4)
    fit_textbox(s, L, top, lw, CB - top - emu(0.2), [
        H("Baselines", size=24, color=GREEN),
        *bullets(["**Clustering benchmark:** LIME-based surrogate explanation pipeline.",
                  "**Recommendation:** MF, NCF, LightGCN, RecDCL, HCCF, **HPCF (strongest reference)**: classical, neural, graph and hypergraph families, so the effect of cooperative attribution is not confused with a lucky model choice."], size=20, gap0=8),
        H("Metrics", size=24, color=GREEN, spcbef=16),
        *bullets(["**Ranking:** Precision@K, Recall@K, **NDCG@20 (principal)**, K ∈ {5, 10, 20}.",
                  "**System diversity:** Catalogue Coverage = |⋃_{u} R_{u}| / |I|.",
                  "**List diversity:** Intra-List Diversity (ILD), **built into the coalition utility** on purpose.",
                  "**Clustering quality:** Silhouette, Davies–Bouldin."], size=20, gap0=8),
    ], min_scale=0.68)
    dx = L + lw + emu(0.6)
    dw = R - dx
    textbox(s, dx, top, dw, emu(0.4), [Para([Run("EVALUATION METRICS", font="xbold", size=14, color=ORANGE, spc=1.6)], align="ctr", lnspc=18)])
    cols = [("Ranking", ["NDCG@K", "Recall@K", "Precision@K", "MAP@K / HR@K"], GREEN),
            ("Beyond accuracy", ["Coverage", "Intra-List Diversity", "Novelty", "Fairness"], "1E5F58"),
            ("Clustering validity", ["Silhouette", "Davies–Bouldin", "Calinski–Harabasz", "Stability"], ORANGE)]
    cells = grid(3, 3, dx, top + emu(0.6), dw, CB - top - emu(0.9), gap=emu(0.3))
    for (h1, items, f), (x, y, w, h) in zip(cols, cells):
        box = rrect(s, x, y, w, h, fill=f, radius=emu(0.3))
        shape_text(box, [Para([Run(h1, font="xbold", size=22, color=WHITE)], align="ctr", lnspc=27)] +
                   [Para([Run("• " + it, font="body", size=18, color="F1EDE6")], align="ctr", lnspc=24, spcbef=12) for it in items],
                   anchor="ctr", insets=(emu(0.2), emu(0.2), emu(0.2), emu(0.2)))

    # --- Hardware ------------------------------------------------------------
    s, top = content_slide(ctx, "Hardware & Software", eyebrow="Experimental Protocol",
                           tabs=["Datasets", "Metrics", "Hardware"], active="Hardware", notes=N(20))
    hw = [("CPU", "Intel Core i9-14900K · 24 cores", "clustering, preprocessing, data loading"),
          ("GPU", "NVIDIA GeForce RTX 4090 · 24 GB", "DyHuCoG training & inference"),
          ("Memory", "48 GB RAM · 2 TB SSD", "full Beijing dataset in memory"),
          ("Software", "Python 3.8 · PyTorch 2.0.1", "scikit-learn, LightGBM, SHAP, NumPy / SciPy / pandas")]
    cells = grid(4, 4, L, top + emu(0.1), W, emu(3.4), gap=emu(0.3))
    for i, ((h1, v, sub), (x, y, w, h)) in enumerate(zip(hw, cells)):
        f = GREEN if i % 2 == 0 else "1E5F58"
        box = rrect(s, x, y, w, h, fill=f, radius=emu(0.3))
        shape_text(box, [Para([Run(h1.upper(), font="xbold", size=14, color=YELLOW, spc=1.6)], lnspc=18),
                         Para([Run(v, font="xbold", size=22, color=WHITE)], lnspc=27, spcbef=8),
                         Para([Run(sub, font="body", size=17, color="DCE7E3")], lnspc=21, spcbef=8)],
                   anchor="t", insets=(emu(0.4), emu(0.4), emu(0.35), emu(0.3)))
    cy = top + emu(0.1) + emu(3.4) + emu(0.45)
    light_card(s, L, cy + emu(0.25), W, CB - cy - emu(0.45), label="Notes",
               paras=bullets(["Altair for interactive SHAP visualisation; metrics reported at K ∈ {5, 10, 20}.",
                              "The hardware mainly explains the runtime figures quoted later (e.g. DyHuCoG ≈ 1.78× HPCF training time).",
                              "**Everything runs on standard academic hardware; nothing needs industrial-scale compute.**"], size=20, gap0=8), pad=(0.55, 0.7, 0.5, 0.3))

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

    # --- C1 objectives -------------------------------------------------------
    s, top = content_slide(ctx, "Gap and Objectives", eyebrow=C1, tabs=C1TABS, active="Objectives", notes=N(22, 23))
    cw = (W - emu(0.4)) / 2
    ch = CB - top - emu(0.45)
    card(s, L, top + emu(0.25), cw, ch, label="Gap",
         paras=bullets(["Shapley explanation is **standard in supervised tasks**, but clustering is still much less explained.",
                        "Existing clustering-interpretability methods favour **local or global** explanation, not both.",
                        "They often fail to scale or to stay **consistent across clusters**.",
                        "Clustering is the hardest test bed: the model creates its own structure, so cluster meaning must be worked out after the fact."],
                       size=20, color=WHITE, c0=YELLOW, c1=YELLOW, gap0=10), pad=(0.55, 0.7, 0.5, 0.3))
    x2 = L + cw + emu(0.4)
    rrect(s, x2, top + emu(0.25), cw, ch, fill=TINT, radius=emu(0.34))
    pill(s, x2 + emu(0.5), top + emu(0.25) - emu(0.26), "RQ1 → Objectives", active=True, h=emu(0.48), size=22, pad=0.36)
    fit_textbox(s, x2 + emu(0.5), top + emu(0.9), cw - emu(1.0), ch - emu(0.95), [
        P("**RQ1 ·** How can Shapley values explain black-box clustering faithfully at instance and cluster level?", size=20, color=GREEN),
    ], min_scale=0.8)
    numbered_rows(s, x2 + emu(0.5), top + emu(2.05), cw - emu(1.0), [
        ("O1", "Build a pipeline that yields **cluster-level explanation while keeping feature-level attribution**."),
        ("O2", "Keep the meaning of the **original feature space** (density, pH, acidity, sulfur dioxide, alcohol), not a reduced latent space."),
        ("O3", "**Justify Shapley** over an ad-hoc surrogate such as LIME."),
    ], size=19, min_h=0.9, gap=0.14)

    # --- C1 game formulation -------------------------------------------------
    s, top = content_slide(ctx, "Clustering as a Cooperative Game", eyebrow=C1, tabs=C1TABS, active="Methodology", notes=N(24))
    lw = emu(8.4)
    fit_textbox(s, L, top, lw, CB - top - emu(0.2), bullets([
        "**Player set N = F:** each feature is a player.",
        "**Value function v(S) = Silhouette( KMeans(X_{S}, k^{*}) ):** how well the data cluster using only the features in S.",
        "A feature's Shapley value = its **expected marginal contribution to clustering quality** over all coalition orders.",
        "**Why Silhouette:** bounded, normalised, easy to interpret (Davies–Bouldin or Calinski–Harabasz would also be defensible).",
        "Direct evaluation of every coalition is **not feasible** → we need a bridge.",
    ], size=21, gap0=12), min_scale=0.7)
    dx = L + lw + emu(0.6)
    dw = R - dx
    bh = emu(3.2)
    box = rrect(s, dx, top, dw, bh, fill=GREEN, radius=emu(0.3))
    textbox(s, dx, top + emu(0.22), dw, emu(0.3), [Para([Run("SHAPLEY VALUE OF FEATURE j", font="xbold", size=14, color=YELLOW, spc=1.6)], align="ctr", lnspc=18)])
    equation(s, dx + emu(0.2), top + emu(0.55), dw - emu(0.4), emu(1.95),
             r"\varphi_j = \sum_{S \subseteq N \setminus \{j\}} \dfrac{|S|!\,(n-|S|-1)!}{n!}\,\left[\, v(S \cup \{j\}) - v(S) \,\right]", size=24, color=WHITE)
    textbox(s, dx, top + bh - emu(0.6), dw, emu(0.4), [Para([Run("expected marginal contribution over all orders of arrival", font="body", size=16, color="DCE7E3")], align="ctr", lnspc=20)])
    ax = [("Efficiency", r"{\sum}_{j}\, \varphi_j = v(N) - v(\varnothing)"), ("Symmetry", "equal contributors get equal credit"),
          ("Null player", "no marginal effect → zero"), ("Additivity", "linear across games")]
    cells = grid(4, 2, dx, top + bh + emu(0.3), dw, emu(2.2), gap=emu(0.25), vgap=emu(0.25))
    for i, ((h1, sub), (x, y, w, h)) in enumerate(zip(ax, cells)):
        if i == 0:
            tile = chip(s, x, y, w, h, h1, fill=TINT, color=INK, size=19, radius=emu(0.2))
            # label anchored to the top of the tile, the axiom set as an equation below it
            shape_text(tile, [Para([Run(h1, font="bold", size=19, color=INK)], align="ctr", lnspc=22)], anchor="t", insets=(emu(0.1), emu(0.22), emu(0.1), emu(0.05)))
            equation(s, x + emu(0.1), y + emu(0.5), w - emu(0.2), h - emu(0.55), sub, size=15, color=MUTED)
        else:
            chip(s, x, y, w, h, h1, fill=TINT, color=INK, size=19, sub=sub, sub_size=15, sub_color=MUTED, radius=emu(0.2))
    ny = top + bh + emu(0.3) + emu(2.2) + emu(0.3)
    bar = rrect(s, dx, ny, dw, CB - ny - emu(0.2), fill=None, line=ORANGE, line_w=2.5, radius=emu(0.25))
    shape_text(bar, [Para(md_runs("**2^{|F|} coalitions:** for 11 wine features that is 2,048 K-Means runs per evaluation; for large data, not feasible.", size=17, color=INK), align="ctr", lnspc=23)],
               anchor="ctr", insets=(emu(0.3), emu(0.1), emu(0.3), emu(0.1)))

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

    # --- C1 pipeline ---------------------------------------------------------
    s, top = content_slide(ctx, "Pipeline in Five Stages", eyebrow=C1, tabs=C1TABS, active="Methodology", notes=N(26))
    stages = [("1", "PCA", "Stabilise geometry + visual check; **NOT** the explanatory space."),
              ("2", "K-Means++", "Multi-criteria k selection: elbow, Silhouette, Davies–Bouldin."),
              ("3", "LightGBM surrogate", "Trained on original features to predict cluster labels."),
              ("4", "TreeSHAP", "Attribution in the original feature space."),
              ("5", "Aggregate", "Global importance, cluster-specific profiles, local force plots.")]
    lw = emu(9.8)
    y = top
    rh = emu(0.92)
    for i, (num, h1, body) in enumerate(stages):
        yy = y + i * (rh + emu(0.14))
        rrect(s, L, yy, lw, rh, fill=TINT if i % 2 == 0 else TINT2, radius=emu(0.2))
        badge(s, L + emu(0.2), yy + (rh - emu(0.62)) / 2, emu(0.62), num, fill=GREEN if i < 4 else ORANGE, color=WHITE, size=20)
        fit_textbox(s, L + emu(1.05), yy, lw - emu(1.25), rh,
                    [Para(md_runs(f"**{h1}**: " + body, size=19), lnspc=24)], anchor="ctr", min_scale=0.75)
    cy = y + 5 * (rh + emu(0.14)) + emu(0.1)
    bar = rrect(s, L, cy, lw, CB - cy - emu(0.15), fill=GREEN, radius=emu(0.22))
    shape_text(bar, [Para(md_runs("**Complexity:** dominated by PCA and repeated K-Means; TreeSHAP scales with tree count and depth, **not exponentially in the number of features**.", size=17, color=WHITE), align="ctr", lnspc=22)],
               anchor="ctr", insets=(emu(0.4), emu(0.1), emu(0.4), emu(0.1)))
    fx = L + lw + emu(0.5)
    fw = R - fx
    fh = CB - top - emu(0.2)
    frame = rrect(s, fx, top, fw, fh, fill=WHITE, line=RULE, line_w=1.25, radius=emu(0.25))
    from PIL import Image
    im = Image.open(os.path.join(FIGS, "c1_pipeline.png"))
    ratio = im.height / im.width
    pw = fw - emu(0.5)
    ph = pw * ratio
    if ph > fh - emu(0.9):
        ph = fh - emu(0.9)
        pw = ph / ratio
    picture(s, os.path.join(FIGS, "c1_pipeline.png"), fx + (fw - pw) / 2, top + emu(0.2), w=pw, h=ph)
    textbox(s, fx, top + fh - emu(0.6), fw, emu(0.5), [Para([Run("Flowchart of the explainable clustering pipeline (Chapter 5)", font="body", size=14, color=MUTED)], align="ctr", lnspc=18)])

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

    # --- C1 results: global ranking -----------------------------------------
    s, top = content_slide(ctx, "Global SHAP Ranking: Wine Quality", eyebrow=C1, tabs=C1TABS, active="Results", notes=N(28))
    feats = [("density", 1.0), ("pH", 0.82), ("fixed acidity", 0.68), ("sulfur dioxide", 0.55), ("alcohol", 0.44)]
    lw = emu(9.2)
    textbox(s, L, top, lw, emu(0.4), [Para([Run("MEAN |SHAP|  ·  RELATIVE RANKING (HIGH → LOW)", font="xbold", size=14, color=ORANGE, spc=1.6)], lnspc=18)])
    by = top + emu(0.6)
    bh = emu(0.72)
    label_w = emu(2.6)
    for i, (name, v) in enumerate(feats):
        yy = by + i * (bh + emu(0.22))
        textbox(s, L, yy, label_w, bh, [Para([Run(name, font="bold", size=20, color=INK)], align="r", lnspc=24)], anchor="ctr")
        rrect(s, L + label_w + emu(0.25), yy, (lw - label_w - emu(0.25)) * v, bh, fill=GREEN if i < 3 else ORANGE, radius=emu(0.1))
        textbox(s, L + label_w + emu(0.4), yy, emu(1.2), bh, [Para([Run(f"{i+1}", font="xbold", size=18, color=WHITE)], lnspc=22)], anchor="ctr")
    ny = by + 5 * (bh + emu(0.22)) + emu(0.1)
    textbox(s, L, ny, lw, emu(0.4), [Para([Run("Bar lengths show the rank order only; exact values in Chapter 5, Fig. 5.6.", font="body", size=14, color=MUTED)], lnspc=18)])
    dx = L + lw + emu(0.6)
    dw = R - dx
    card(s, dx, top + emu(0.25), dw, CB - top - emu(0.45), label="Reading the ranking",
         paras=bullets(["The main drivers relate to **structure, preservation and sensory balance**.",
                        "This is **NOT a random side effect of the classifier**: it recovers a chemically meaningful ranking.",
                        "Density and pH separate wine styles; sulfur dioxide reflects preservation; alcohol shapes body.",
                        "Each driver is a **domain-level factor that can be changed**: exactly Definition 1.1."],
                       size=20, color=WHITE, c0=YELLOW, c1=YELLOW, gap0=10), pad=(0.55, 0.7, 0.5, 0.3))

    # --- C1 results: cluster signatures -------------------------------------
    s, top = content_slide(ctx, "Cluster-Specific Explanatory Signatures", eyebrow=C1, tabs=C1TABS, active="Results", notes=N(29))
    sig = [("Cluster 0", "density + sulfur-dioxide-related variables", GREEN),
           ("Cluster 1", "acidity and pH-related effects", "1E5F58"),
           ("Cluster 2", "a different balance of acidity, alcohol and related chemical attributes", ORANGE)]
    cells = grid(3, 3, L, top + emu(0.1), W, emu(3.4), gap=emu(0.35))
    for (h1, body, f), (x, y, w, h) in zip(sig, cells):
        box = rrect(s, x, y, w, h, fill=f, radius=emu(0.3))
        shape_text(box, [Para([Run(h1.upper(), font="xbold", size=14, color=YELLOW if f != ORANGE else WHITE, spc=1.6)], lnspc=18),
                         Para([Run(body, font="xbold", size=23, color=WHITE)], lnspc=28, spcbef=10)],
                   anchor="t", insets=(emu(0.45), emu(0.45), emu(0.4), emu(0.3)))
    cy = top + emu(0.1) + emu(3.4) + emu(0.45)
    light_card(s, L, cy + emu(0.25), W, CB - cy - emu(0.45), label="What the signatures show",
               paras=bullets(["The three clusters show **distinct explanatory signatures**: the explanation is consistent, not a single summary number.",
                              "The **same small set of variables recurs** across clusters, with **different relative weights** within each.",
                              "Local force plots break any single wine down into its per-feature contributions to cluster membership."], size=21, gap0=8), pad=(0.55, 0.7, 0.5, 0.3))

    # --- C1 SHAP vs LIME ----------------------------------------------------
    s, top = content_slide(ctx, "SHAP vs LIME: Why the Cooperative Concept Wins", eyebrow=C1, tabs=C1TABS, active="Results", notes=N(30))
    rows = [["Criterion", "SHAP (cooperative)", "LIME (local surrogate)"],
            ["Basis", "Cooperative-game marginal contribution", "Local surrogate approximation"],
            ["Local / global", "Both", "Primarily local"],
            ["Theoretical guarantee", "Efficiency, symmetry, null player, additivity", "None equivalent"],
            ["Stability", "Higher when surrogate faithful", "Sensitive to perturbation design"],
            ["Cluster comparison", "Strong", "Limited"]]
    gf, th = table(s, L, top, W, rows, col_widths=[2.6, 4.4, 4.4], size=19, head_size=19, row_h=emu(0.82))
    by = top + th + emu(0.4)
    bar = rrect(s, L, by, W, CB - by - emu(0.15), fill=GREEN, radius=emu(0.25))
    shape_text(bar, [Para(md_runs("Shapley rests on **four axioms**; LIME has no equivalent guarantee. With a faithful surrogate, cooperative attribution is **more stable and comparable across clusters**.", size=21, color=WHITE), align="ctr", lnspc=27)],
               anchor="ctr", insets=(emu(0.5), emu(0.1), emu(0.5), emu(0.1)))

    # --- C1 findings ---------------------------------------------------------
    s, top = content_slide(ctx, "Answers, Key Findings and Limitations", eyebrow=C1, tabs=C1TABS, active="Findings", notes=N(31, 32, 33))
    cw = (W - emu(0.4)) / 2
    ch = CB - top - emu(0.45)
    card(s, L, top + emu(0.25), cw, ch, label="RQ1 answered · objectives met",
         paras=bullets(["**RQ1: yes.** Faithful, consistent cluster-level explanation from Shapley values.",
                        "**O1 met** · cluster-level explanation anchored to individual feature contributions.",
                        "**O2 met** · attribution returned to the original chemical variables, not a latent space.",
                        "**O3 met** · Shapley rests on four axioms; LIME has no equivalent guarantee.",
                        "Recovers a ranking that makes sense in wine chemistry: density, pH, acidity, sulfur dioxide, alcohol."],
                       size=19, color=WHITE, c0=YELLOW, c1=YELLOW, gap0=8), pad=(0.55, 0.7, 0.5, 0.3))
    light_card(s, L + cw + emu(0.4), top + emu(0.25), cw, ch, label="Limitations",
               paras=bullets(["Fidelity depends on the **LightGBM surrogate**, not on the K-Means geometry directly.",
                              "Limited to **tabular data**; no structured, graph or image input.",
                              "**Single-level structure:** cannot explain how importance changes between a partition and its sub-partitions.",
                              "The surrogate approximation smooths out variation between single observations."], size=19, gap0=8), pad=(0.55, 0.7, 0.5, 0.3))

    # --- C1 takeaways -------------------------------------------------------
    s, top = content_slide(ctx, "Takeaways, and the Next Question", eyebrow=C1, tabs=C1TABS, active="Findings", notes=N(34))
    tk = [("Single lens", "Shapley attribution is one well-founded lens for explaining an unsupervised partition."),
          ("Original space", "Keeping attribution in the original feature space is what makes it actionable."),
          ("But…", "Real data are rarely single-level: broad groups contain nested sub-groups.")]
    cells = grid(3, 3, L, top + emu(0.1), W, emu(3.6), gap=emu(0.35))
    for i, ((h1, body), (x, y, w, h)) in enumerate(zip(tk, cells)):
        f = [GREEN, "1E5F58", ORANGE][i]
        box = rrect(s, x, y, w, h, fill=f, radius=emu(0.3))
        shape_text(box, [Para([Run(h1, font="title", size=30, color=YELLOW if i < 2 else WHITE, spc=-1.2)], lnspc=34),
                         Para([Run(body, font="body", size=20, color="F7F2EA")], lnspc=25, spcbef=12)],
                   anchor="t", insets=(emu(0.45), emu(0.45), emu(0.4), emu(0.3)))
    ny = top + emu(0.1) + emu(3.6) + emu(0.5)
    box = rrect(s, L, ny, W, CB - ny - emu(0.15), fill=None, line=GREEN, line_w=2.5, radius=emu(0.3))
    shape_text(box, [Para([Run("NEXT", font="xbold", size=14, color=ORANGE, spc=1.8)], align="ctr", lnspc=18),
                     Para(md_runs("So the next question is whether this logic **survives scale and hierarchy**: Contribution II.", size=26, color=INK, font="bold"), align="ctr", lnspc=32, spcbef=8)],
               anchor="ctr", insets=(emu(0.5), emu(0.1), emu(0.5), emu(0.1)))
    accent(s, "uparrow_g", R - emu(1.4), ny + emu(0.25), emu(0.28))

    # ======================================================================
    # SECTION 5 — CONTRIBUTION II
    # ======================================================================
    C2 = "Contribution II: Multi-Level XAI for Large-Scale Clustering"
    section_slide(ctx, "05", "Contribution II", "Enhanced multi-level XAI for large-scale clustering  ·  answers RQ2",
                  [("Objectives", "A truly multi-level workflow, a formal cross-level consistency argument (Proposition 6.1), validation on a very different large dataset."),
                   ("Methodology", "Recursive clustering, level-specific surrogates in the same feature space, size-weighted cross-level SHAP aggregation."),
                   ("Results", "Beijing Air Quality (383,585 records): Silhouette ≈ 0.63, three atmospheric regimes, weather variables at the centre of the structure.")],
                  notes=N(35))

    # --- C2 objectives -------------------------------------------------------
    s, top = content_slide(ctx, "Gap and Objectives", eyebrow=C2, tabs=C1TABS, active="Objectives", notes=N(36, 37))
    cw = (W - emu(0.4)) / 2
    ch = CB - top - emu(0.45)
    card(s, L, top + emu(0.25), cw, ch, label="Gap",
         paras=bullets(["Once clustering is multi-level, feature importance must stay readable **within a cluster, across sub-clusters and across the levels**.",
                        "Large-scale data make exact explanation **too costly to compute**.",
                        "A flat explanation may be true yet **incomplete**: it cannot show how importance changes inside a cluster."],
                       size=20, color=WHITE, c0=YELLOW, c1=YELLOW, gap0=10), pad=(0.55, 0.7, 0.5, 0.3))
    x2 = L + cw + emu(0.4)
    rrect(s, x2, top + emu(0.25), cw, ch, fill=TINT, radius=emu(0.34))
    pill(s, x2 + emu(0.5), top + emu(0.25) - emu(0.26), "RQ2 → Objectives", active=True, h=emu(0.48), size=22, pad=0.36)
    fit_textbox(s, x2 + emu(0.5), top + emu(0.9), cw - emu(1.0), emu(1.1), [
        P("**RQ2 ·** How can this extend to large-scale, multi-level clustering while staying feasible and consistent?", size=20, color=GREEN)], min_scale=0.8)
    numbered_rows(s, x2 + emu(0.5), top + emu(2.05), cw - emu(1.0), [
        ("O1", "A **truly multi-level workflow**, not a rerun of the single-level pipeline."),
        ("O2", "A **formal cross-level consistency argument** (Proposition 6.1)."),
        ("O3", "Validation on a **very different large-scale dataset**."),
    ], size=19, min_h=0.9, gap=0.14)

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
    regs = [("Regime A", "temp · dew point · ozone", GREEN), ("Regime B", "CO · SO₂ · PM · wind", "1E5F58"), ("Regime C", "clean air · weather", ORANGE)]
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
             r"w_{c'} = |c'| \,/\, |c|, \qquad \varepsilon_j \to 0 \ \text{ under perfect surrogate fidelity}", size=14, color="DCE7E3")

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

    # --- C2 results: coarse level -------------------------------------------
    s, top = content_slide(ctx, "Coarse-Level Clustering: Beijing Air Quality", eyebrow=C2, tabs=C1TABS, active="Results", notes=N(40))
    cells = grid(3, 3, L, top + emu(0.1), W, emu(2.3), gap=emu(0.35))
    kpi(s, *cells[0], "k = 3", "all **k-selection criteria** agree", fill=GREEN)
    kpi(s, *cells[1], "≈ 0.63", "**Silhouette** · much stronger separation than wine", fill="1E5F58")
    kpi(s, *cells[2], "≈ 0.55", "**Davies–Bouldin** · clusters rarely overlap", fill=ORANGE, vcolor=WHITE)
    cy = top + emu(0.1) + emu(2.3) + emu(0.45)
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

    # --- C2 results: global ranking -----------------------------------------
    s, top = content_slide(ctx, "Global SHAP Ranking: Weather Variables Are Central", eyebrow=C2, tabs=C1TABS, active="Results", notes=N(41))
    feats = [("temperature", 1.0, GREEN), ("dew point", 0.86, GREEN), ("pressure", 0.72, GREEN), ("CO", 0.58, ORANGE), ("NO₂", 0.48, ORANGE), ("PM10", 0.40, ORANGE), ("PM2.5", 0.34, ORANGE)]
    lw = emu(9.2)
    textbox(s, L, top, lw, emu(0.4), [Para([Run("MEAN |SHAP|  ·  RELATIVE RANKING (HIGH → LOW)", font="xbold", size=14, color=ORANGE, spc=1.6)], lnspc=18)])
    by = top + emu(0.55)
    bh = emu(0.58)
    label_w = emu(2.4)
    for i, (name, v, f) in enumerate(feats):
        yy = by + i * (bh + emu(0.16))
        textbox(s, L, yy, label_w, bh, [Para([Run(name, font="bold", size=19, color=INK)], align="r", lnspc=23)], anchor="ctr")
        rrect(s, L + label_w + emu(0.25), yy, (lw - label_w - emu(0.25)) * v, bh, fill=f, radius=emu(0.08))
        textbox(s, L + label_w + emu(0.4), yy, emu(1.2), bh, [Para([Run(f"{i+1}", font="xbold", size=16, color=WHITE)], lnspc=20)], anchor="ctr")
    ly = by + 7 * (bh + emu(0.16)) + emu(0.05)
    rrect(s, L + label_w + emu(0.25), ly + emu(0.08), emu(0.3), emu(0.3), fill=GREEN, radius=emu(0.05))
    textbox(s, L + label_w + emu(0.65), ly, emu(2.5), emu(0.45), [Para([Run("weather", font="body", size=15, color=MUTED)], lnspc=19)], anchor="ctr")
    rrect(s, L + label_w + emu(3.2), ly + emu(0.08), emu(0.3), emu(0.3), fill=ORANGE, radius=emu(0.05))
    textbox(s, L + label_w + emu(3.6), ly, emu(2.5), emu(0.45), [Para([Run("pollutant", font="body", size=15, color=MUTED)], lnspc=19)], anchor="ctr")
    dx = L + lw + emu(0.6)
    dw = R - dx
    card(s, dx, top + emu(0.25), dw, CB - top - emu(0.45), label="Reading the ranking",
         paras=bullets(["It is **NOT only pollutant concentrations** that matter: weather variables play a **central role in the structure**.",
                        "Temperature, dew point and pressure control **dispersion, trapping and sunlight-driven chemistry**.",
                        "This is the kind of insight that flat summaries often fail to make explicit."],
                       size=20, color=WHITE, c0=YELLOW, c1=YELLOW, gap0=10), pad=(0.55, 0.7, 0.5, 0.3))

    # --- C2 results: regimes -------------------------------------------------
    s, top = content_slide(ctx, "Three Atmospheric Regimes", eyebrow=C2, tabs=C1TABS, active="Results", notes=N(42))
    regs = [("Regime A", "Warm, sunlight-driven", "Ozone, temperature and dew point stand out: summer photochemical smog.", GREEN),
            ("Regime B", "Wintertime smog", "CO, SO₂ and particulate matter dominate; low wind speed limits dispersion.", "1E5F58"),
            ("Regime C", "Comparatively clean air", "Favourable weather, weak pollutant signals.", ORANGE)]
    cells = grid(3, 3, L, top + emu(0.1), W, emu(4.2), gap=emu(0.35))
    for (tag, h1, body, f), (x, y, w, h) in zip(regs, cells):
        box = rrect(s, x, y, w, h, fill=f, radius=emu(0.3))
        shape_text(box, [Para([Run(tag.upper(), font="xbold", size=14, color=YELLOW if f != ORANGE else WHITE, spc=1.6)], lnspc=18),
                         Para([Run(h1, font="title", size=30, color=WHITE, spc=-1.2)], lnspc=34, spcbef=8),
                         Para([Run(body, font="body", size=19, color="F7F2EA")], lnspc=24, spcbef=14)],
                   anchor="t", insets=(emu(0.45), emu(0.45), emu(0.4), emu(0.3)))
    gy = top + emu(0.1) + emu(4.2) + emu(0.45)
    bar = rrect(s, L, gy, W, CB - gy - emu(0.15), fill=TINT, radius=emu(0.25))
    shape_text(bar, [Para(md_runs("The framework shows not only **that these regimes exist**, but **which variable combinations define them**.", size=22, color=INK), align="ctr", lnspc=28)],
               anchor="ctr", insets=(emu(0.5), emu(0.1), emu(0.5), emu(0.1)))

    # --- C2 results: cross-level ---------------------------------------------
    s, top = content_slide(ctx, "How Importance Changes Across Levels", eyebrow=C2, tabs=C1TABS, active="Results", notes=N(43))
    cw = (W - emu(0.4)) / 2
    ch = emu(3.4)
    card(s, L, top + emu(0.25), cw, ch, label="Coarse level · regime selection",
         paras=bullets(["**Temperature and dew point dominate**: they separate the broad atmospheric regimes.",
                        "Parent-level story = which regime the observation belongs to."], size=20, color=WHITE, c0=YELLOW, c1=YELLOW, gap0=10), pad=(0.55, 0.7, 0.5, 0.3))
    light_card(s, L + cw + emu(0.4), top + emu(0.25), cw, ch, label="Within clusters · variation inside a regime",
               paras=bullets(["**CO, SO₂, PM10, wind speed, pressure or ozone** become more informative.",
                              "Cluster-level story = what varies once the regime is fixed."], size=20, gap0=10), pad=(0.55, 0.7, 0.5, 0.3))
    gy = top + emu(0.25) + ch + emu(0.4)
    box = rrect(s, L, gy, W, CB - gy - emu(0.15), fill=None, line=ORANGE, line_w=2.5, radius=emu(0.3))
    fit_textbox(s, L + emu(0.5), gy + emu(0.25), W - emu(1.0), CB - gy - emu(0.15) - emu(0.5), [
        P("**This change is NOT a contradiction. It is exactly what a multi-level explanation should reveal.**", size=23, color=INK),
        P("A variable can be **globally important yet locally uninformative** inside a sub-cluster; Proposition 6.1 guarantees the two readings agree, up to the surrogate residual.", size=20, spcbef=10),
    ], anchor="ctr", min_scale=0.7)

    # --- C2 results: generalisation -----------------------------------------
    s, top = content_slide(ctx, "Generalisation and Comparison", eyebrow=C2, tabs=C1TABS, active="Results", notes=N(44))
    rows = [["", "Wine Quality (C1)", "Beijing Air Quality (C2)"],
            ["Scale", "4,898 × 11", "383,585 × 11"],
            ["Nature", "small, dense, chemically correlated", "large, noisy, varies with time & weather"],
            ["Structure", "single-level", "multi-level (nested regimes)"],
            ["Silhouette", "0.144 (k* = 3, chosen for meaning)", "≈ 0.63 (k = 3)"],
            ["Explanatory logic", "Shapley in original feature space", "same logic · still works"]]
    gf, th = table(s, L, top, W, rows, col_widths=[2.4, 4.4, 4.6], size=18, head_size=18, row_h=emu(0.58))
    by = top + th + emu(0.4)
    cw = (W - emu(0.4)) / 2
    card(s, L, by + emu(0.25), cw, CB - by - emu(0.45), label="vs the literature",
         paras=bullets(["The same explanatory logic works on **both datasets** → not tied to one domain.",
                        "Beijing Silhouette ≈ 0.63 vs **0.37** in Gramegna & Giudici's SHAP-based credit-risk clustering."],
                       size=19, color=WHITE, c0=YELLOW, c1=YELLOW, gap0=8), pad=(0.55, 0.7, 0.5, 0.3))
    light_card(s, L + cw + emu(0.4), by + emu(0.25), cw, CB - by - emu(0.45), label="vs LIME",
               paras=bullets(["Weaker **consistency** across levels.",
                              "Less stable local stories for **multi-level reasoning**."], size=19, gap0=8), pad=(0.55, 0.7, 0.5, 0.3))

    # --- C2 findings ---------------------------------------------------------
    s, top = content_slide(ctx, "Answers, Key Findings and Limitations", eyebrow=C2, tabs=C1TABS, active="Findings", notes=N(45, 46, 47))
    cw = (W - emu(0.4)) / 2
    ch = CB - top - emu(0.45)
    card(s, L, top + emu(0.25), cw, ch, label="RQ2 answered · objectives met",
         paras=bullets(["**RQ2: yes, within bounds.** Consistency is kept at scale and across levels.",
                        "**O1 met** · a multi-level explanation that does not collapse into a single flat summary.",
                        "**O2 met** · Proposition 6.1 provides a formal cross-level consistency argument.",
                        "**O3 met** · validated on a very different large-scale dataset (Beijing).",
                        "Differences across levels are **interpretable**, not ruled out as inconsistency."],
                       size=19, color=WHITE, c0=YELLOW, c1=YELLOW, gap0=8), pad=(0.55, 0.7, 0.5, 0.3))
    light_card(s, L + cw + emu(0.4), top + emu(0.25), cw, ch, label="Limitations",
               paras=bullets(["Clustering remains **static**, even though the Beijing data are temporal.",
                              "Surrogate-based SHAP plus representative-instance reporting **smooth out variation between single observations**.",
                              "Limited to **tabular data**.",
                              "Still an explanation of a **pre-computed partition**: it does not influence learning."], size=19, gap0=8), pad=(0.55, 0.7, 0.5, 0.3))

    # --- C2 takeaways -------------------------------------------------------
    s, top = content_slide(ctx, "Takeaways, and the Next Step", eyebrow=C2, tabs=C1TABS, active="Findings", notes=N(48))
    tk = [("Consistent", "Shapley attribution stays consistent across levels of detail, when the hierarchy is explicit."),
          ("Against scale", "Explanations become interpretable against scale, not just against a single flat partition."),
          ("Still post-hoc", "The attribution explains a partition that was already computed.")]
    cells = grid(3, 3, L, top + emu(0.1), W, emu(3.6), gap=emu(0.35))
    for i, ((h1, body), (x, y, w, h)) in enumerate(zip(tk, cells)):
        f = [GREEN, "1E5F58", ORANGE][i]
        box = rrect(s, x, y, w, h, fill=f, radius=emu(0.3))
        shape_text(box, [Para([Run(h1, font="title", size=30, color=YELLOW if i < 2 else WHITE, spc=-1.2)], lnspc=34),
                         Para([Run(body, font="body", size=20, color="F7F2EA")], lnspc=25, spcbef=12)],
                   anchor="t", insets=(emu(0.45), emu(0.45), emu(0.4), emu(0.3)))
    ny = top + emu(0.1) + emu(3.6) + emu(0.5)
    box = rrect(s, L, ny, W, CB - ny - emu(0.15), fill=None, line=GREEN, line_w=2.5, radius=emu(0.3))
    shape_text(box, [Para([Run("NEXT", font="xbold", size=14, color=ORANGE, spc=1.8)], align="ctr", lnspc=18),
                     Para(md_runs("So the next step is to let attribution **shape the learning itself**: Contribution III.", size=26, color=INK, font="bold"), align="ctr", lnspc=32, spcbef=8)],
               anchor="ctr", insets=(emu(0.5), emu(0.1), emu(0.5), emu(0.1)))
    accent(s, "uparrow_g", R - emu(1.4), ny + emu(0.25), emu(0.28))

    # ======================================================================
    # SECTION 6 — CONTRIBUTION III
    # ======================================================================
    C3 = "Contribution III: DyHuCoG, a Dynamic Hypergraph Cooperative Game"
    section_slide(ctx, "06", "Contribution III", "DyHuCoG: a Dynamic Hypergraph Cooperative Game for recommendation  ·  answers RQ3 & RQ4",
                  [("Objectives", "Formulate recommendation as a cooperative game over users, items and contexts; make attribution an in-training signal."),
                   ("Methodology", "Preference-aware Monte Carlo Shapley → dynamic hypergraph edge weights → attention-gated, context-aware scoring; multi-objective loss."),
                   ("Results", "MovieLens-1M & Amazon-Book: NDCG, Recall, Coverage and ILD improve together over HPCF; largest gains on the sparsest data.")],
                  notes=N(49))

    # --- C3 objectives -------------------------------------------------------
    s, top = content_slide(ctx, "Gap and Objectives", eyebrow=C3, tabs=C1TABS, active="Objectives", notes=N(50, 51))
    cw = (W - emu(0.4)) / 2
    ch = CB - top - emu(0.45)
    card(s, L, top + emu(0.25), cw, ch, label="Gap",
         paras=bullets(["Graph and hypergraph recommenders treat message importance as **uniform or attention-weighted**, with no well-founded **marginal-contribution** account.",
                        "Diversity is often a secondary goal or a **re-ranking heuristic**.",
                        "Interpretability is **added after prediction**, not built into the learning objective."],
                       size=20, color=WHITE, c0=YELLOW, c1=YELLOW, gap0=10), pad=(0.55, 0.7, 0.5, 0.3))
    x2 = L + cw + emu(0.4)
    rrect(s, x2, top + emu(0.25), cw, ch, fill=TINT, radius=emu(0.34))
    pill(s, x2 + emu(0.5), top + emu(0.25) - emu(0.26), "RQ3 · RQ4 → Objectives", active=True, h=emu(0.48), size=22, pad=0.36)
    fit_textbox(s, x2 + emu(0.5), top + emu(0.85), cw - emu(1.0), emu(1.55), [
        P("**RQ3 ·** Can cooperative attribution move beyond post-hoc and become part of how a recommender learns?", size=18, color=GREEN),
        P("**RQ4 ·** Can it improve ranking accuracy, context and diversity together when importance comes from a cooperative-game utility?", size=18, color=GREEN, spcbef=6)], min_scale=0.75)
    numbered_rows(s, x2 + emu(0.5), top + emu(2.6), cw - emu(1.0), [
        ("O1", "Formulate recommendation as a **cooperative game** with users, items and contexts as players."),
        ("O2", "Embed **preference-aware Monte Carlo Shapley** into hypergraph message passing."),
        ("O3", "Improve **ranking, coverage and diversity together**."),
    ], size=18, min_h=0.8, gap=0.12)

    # --- C3 game formulation -------------------------------------------------
    s, top = content_slide(ctx, "Recommendation as a Cooperative Game", eyebrow=C3, tabs=C1TABS, active="Methodology", notes=N(52))
    lw = emu(8.6)
    fit_textbox(s, L, top, lw, CB - top - emu(0.2), bullets([
        "**Player set N = U ∪ I ∪ C** (users, items, contexts).",
        "**Hypergraph H = (V, E, W)**; V = U ∪ I ∪ C; **W = dynamic edge weights** from Shapley estimates.",
        "A **coalition S ⊆ N** is the set of entities taking part in a recommendation episode.",
        "**Coalition value v(S)** measures the quality of the recommendation that S can achieve.",
        "**Top-N task:** produce a ranked list L_{u} balancing relevance, diversity and contextual fit.",
    ], size=21, gap0=12), min_scale=0.7)
    dx = L + lw + emu(0.6)
    dw = R - dx
    # hyperedge illustration: three player groups joined into a coalition
    textbox(s, dx, top, dw, emu(0.4), [Para([Run("PLAYERS AND COALITIONS", font="xbold", size=14, color=ORANGE, spc=1.6)], align="ctr", lnspc=18)])
    hy = top + emu(0.6)
    hh = emu(3.1)
    rrect(s, dx + emu(0.3), hy, dw - emu(0.6), hh, fill=TINT, radius=emu(0.6))
    textbox(s, dx, hy + emu(0.12), dw, emu(0.4), [Para([Run("coalition S ⊆ N  ·  hyperedge e ∈ E", font="bold", size=15, color=MUTED)], align="ctr", lnspc=18)])
    groups = [("Users", "U", GREEN), ("Items", "I", "1E5F58"), ("Contexts", "C", ORANGE)]
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

    # --- C3 value function ---------------------------------------------------
    s, top = content_slide(ctx, "Coalition Value Aligned with the Objective", eyebrow=C3, tabs=C1TABS, active="Methodology", notes=N(53))
    bh = emu(1.75)
    box = rrect(s, L, top, W, bh, fill=GREEN, radius=emu(0.3))
    equation(s, L + emu(0.4), top + emu(0.15), W - emu(0.8), emu(0.7),
             r"v(S) = \alpha \cdot \mathrm{NDCG@20}(S) + \beta \cdot \mathrm{Diversity}(S) + \gamma \cdot \mathrm{ContextScore}(S), \qquad \alpha + \beta + \gamma = 1",
             size=24, color=WHITE)
    equation(s, L + emu(0.4), top + emu(0.9), W - emu(0.8), emu(0.7),
             r"v_{\mathrm{pref}}(S) = v(S) + \lambda_{\mathrm{pref}} \, {\sum}_{(u,i) \in S} \operatorname{sim}(u,i)", size=22, color=YELLOW)
    py = top + bh + emu(0.3)
    params = [(r"\alpha = 0.60", "ranking accuracy"), (r"\beta = 0.25", "diversity"), (r"\gamma = 0.15", "context"), (r"\lambda_{\mathrm{pref}} = 0.20", "preference weighting")]
    ph = emu(1.2)
    cells = grid(4, 4, L, py, W, ph, gap=emu(0.3))
    for i, ((v, lab), (x, y, w, h)) in enumerate(zip(params, cells)):
        rrect(s, x, y, w, h, fill=TINT, radius=emu(0.3))
        equation(s, x + emu(0.15), y + emu(0.08), w - emu(0.3), emu(0.68), v, size=26, color=GREEN if i < 3 else ORANGE)
        textbox(s, x, y + emu(0.76), w, emu(0.35), [Para([Run(lab, font="bold", size=16, color=INK)], align="ctr", lnspc=20)])
    cy = py + ph + emu(0.35)
    cw = (W - emu(0.4)) / 2
    ch = CB - cy - emu(0.4)
    light_card(s, L, cy + emu(0.25), cw, ch, label="Alignment by design",
               paras=bullets(["The **same trade-off** the recommender must satisfy is the one from which attribution is computed.",
                              "Explanatory game and predictive objective are **aligned by design**."], size=20, gap0=10), pad=(0.55, 0.7, 0.5, 0.3))
    card(s, L + cw + emu(0.4), cy + emu(0.25), cw, ch, label="Tuning & scope",
         paras=bullets(["Weights **grid-searched**; stable, with **< 1.5 % variance** in NDCG@20 around the optimum.",
                        "Coalition evaluation is limited to the **interaction episode** (a few dozen players), not the full catalogue."],
                       size=20, color=WHITE, c0=YELLOW, c1=YELLOW, gap0=10), pad=(0.55, 0.7, 0.5, 0.3))

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
    ph = emu(1.9)
    pw = ph / ratio
    frame = rrect(s, L, top, W, ph + emu(0.3), fill=WHITE, line=RULE, line_w=1.25, radius=emu(0.25))
    picture(s, os.path.join(FIGS, "dyhucog_arch.png"), L + (W - pw) / 2, top + emu(0.15), w=pw, h=ph)
    ey = top + ph + emu(0.3) + emu(0.25)
    eqs = [("Base propagation", r"e^{(l+1)} = \sigma\left( D^{-1/2} A\, D^{-1/2}\, e^{(l)} \right)", None),
           ("Shapley-weighted", r"e_j^{(l+1)} = \sigma\left( W^{(l)} e_j^{(l)} + {\sum}_{k \in \mathcal{N}(j)} w_{jk}\, e_k^{(l)} \right)", None),
           ("Normalised weights", r"w_{jk} = \hat{\varphi}_{jk} \,/\, {\sum}_{k' \in \mathcal{N}(j)} \hat{\varphi}_{jk'}", "clipped + EMA-smoothed"),
           ("Attention gate", r"a_{ui} = \sigma\left( W_a\, [\,e_u, e_i, l_i\,] \right), \qquad y_{ui} = (1 + a_{ui})\, \langle e_u, e_i \rangle", None),
           ("Context-aware score", r"f(u,i,c) = y_{ui} + \lambda_c\, \langle\, g(c_{ui}),\, e_{c_{ui}} \rangle", None)]
    rh = (CB - ey - emu(0.1) - emu(0.1) * 4) / 5
    for i, (h1, tex, note) in enumerate(eqs):
        yy = ey + i * (rh + emu(0.1))
        rrect(s, L, yy, W, rh, fill=TINT if i % 2 == 0 else TINT2, radius=emu(0.16))
        textbox(s, L + emu(0.35), yy, emu(3.6), rh, [Para([Run(h1, font="xbold", size=18, color=GREEN)], lnspc=22)], anchor="ctr")
        ew = W - emu(4.3) - (emu(3.2) if note else 0)
        equation(s, L + emu(4.0), yy, ew, rh, tex, size=22, color=INK, align="l")
        if note:
            textbox(s, R - emu(3.3), yy, emu(3.0), rh, [Para([Run(note, font="body", size=15, color=MUTED)], align="r", lnspc=18)], anchor="ctr")

    # --- C3 loss -------------------------------------------------------------
    s, top = content_slide(ctx, "Multi-Objective Learning", eyebrow=C3, tabs=C1TABS, active="Methodology", notes=N(56))
    box = rrect(s, L, top, W, emu(1.3), fill=GREEN, radius=emu(0.3))
    equation(s, L + emu(0.4), top, W - emu(0.8), emu(1.3),
             r"\mathcal{L} = \mathcal{L}_{\mathrm{rec}} + \lambda_{\mathrm{div}}\, \mathcal{L}_{\mathrm{div}} + \lambda_{\mathrm{ctx}}\, \mathcal{L}_{\mathrm{ctx}} + \lambda_{\mathrm{reg}}\, \mathcal{L}_{\mathrm{reg}}",
             size=30, color=WHITE)
    terms = [(r"\mathcal{L}_{\mathrm{rec}}", "Bayesian Personalised Ranking", "pairwise loss for implicit feedback", GREEN),
             (r"\mathcal{L}_{\mathrm{div}}", "Intra-List Diversity regulariser", "penalises redundant ranked lists", "1E5F58"),
             (r"\mathcal{L}_{\mathrm{ctx}}", "Context alignment", "match context embedding to context-node representation", ORANGE),
             (r"\mathcal{L}_{\mathrm{reg}}", "L2 weight decay", "regularisation", INK)]
    cells = grid(4, 4, L, top + emu(1.7), W, emu(3.5), gap=emu(0.3))
    for (sym, h1, sub, f), (x, y, w, h) in zip(terms, cells):
        box = rrect(s, x, y, w, h, fill=f, radius=emu(0.3))
        equation(s, x + emu(0.4), y + emu(0.3), emu(2.0), emu(0.85), sym, size=32, color=YELLOW if f != ORANGE else WHITE, align="l")
        shape_text(box, [Para([Run(h1, font="xbold", size=20, color=WHITE)], lnspc=25),
                         Para([Run(sub, font="body", size=17, color="F1EDE6")], lnspc=21, spcbef=8)],
                   anchor="t", insets=(emu(0.4), emu(1.35), emu(0.35), emu(0.3)))
    gy = top + emu(1.7) + emu(3.5) + emu(0.45)
    bar = rrect(s, L, gy, W, CB - gy - emu(0.15), fill=TINT, radius=emu(0.25))
    shape_text(bar, [Para(md_runs("The learning objective and the coalition value are **aligned**: DyHuCoG trains to optimise the **same balance** that later determines attribution.", size=22, color=INK), align="ctr", lnspc=28)],
               anchor="ctr", insets=(emu(0.5), emu(0.1), emu(0.5), emu(0.1)))

    # --- C3 results: main table ---------------------------------------------
    s, top = content_slide(ctx, "Main Results vs the Strongest Baseline (HPCF)", eyebrow=C3, tabs=C1TABS, active="Results", notes=N(57, 58))
    rows = [["Dataset", "Model", "NDCG@20", "Recall@20", "Coverage", "Diversity (ILD)"],
            ["MovieLens-1M", "HPCF", "0.2528", "0.2098", "0.342", "0.461"],
            ["MovieLens-1M", "DyHuCoG", "0.2775", "0.2362", "0.397", "0.516"],
            ["Amazon-Book", "HPCF", "0.0270", "0.0359", "0.259", "0.535"],
            ["Amazon-Book", "DyHuCoG", "0.0306", "0.0417", "0.336", "0.602"]]
    al = ["l", "l", "ctr", "ctr", "ctr", "ctr"]
    gf, th = table(s, L, top, W, rows, col_widths=[2.4, 2.0, 1.8, 1.8, 1.8, 2.0], size=20, head_size=19, align=al, header_align=al, row_h=emu(0.78))
    # emphasise DyHuCoG rows
    for ri in (2, 4):
        for ci in range(6):
            c = gf.table.cell(ri, ci)
            c.fill.solid()
            c.fill.fore_color.rgb = RGBColor.from_string(GREEN_SOFT)
    gy = top + th + emu(0.45)
    textbox(s, L, gy, W, emu(0.4), [Para([Run("RELATIVE IMPROVEMENT OVER HPCF", font="xbold", size=14, color=ORANGE, spc=1.6)], lnspc=18)])
    gains = [("NDCG@20", "+9.77 %", "+13.33 %"), ("Recall@20", "+12.58 %", "+16.16 %"), ("Coverage", "+16.1 %", "+29.7 %"), ("Intra-List Diversity", "+11.9 %", "+12.5 %")]
    cells = grid(4, 4, L, gy + emu(0.5), W, CB - gy - emu(0.65), gap=emu(0.3))
    for i, ((m, a, b), (x, y, w, h)) in enumerate(zip(gains, cells)):
        box = rrect(s, x, y, w, h, fill=GREEN if i % 2 == 0 else "1E5F58", radius=emu(0.25))
        shape_text(box, [Para([Run(m.upper(), font="xbold", size=13, color=YELLOW, spc=1.4)], align="ctr", lnspc=16),
                         Para([Run(a, font="xbold", size=26, color=WHITE)], align="ctr", lnspc=30, spcbef=6),
                         Para([Run("MovieLens-1M", font="body", size=13, color="DCE7E3")], align="ctr", lnspc=15),
                         Para([Run(b, font="xbold", size=26, color=YELLOW)], align="ctr", lnspc=30, spcbef=6),
                         Para([Run("Amazon-Book", font="body", size=13, color="DCE7E3")], align="ctr", lnspc=15)],
                   anchor="ctr", insets=(emu(0.1), emu(0.1), emu(0.1), emu(0.1)))

    # --- C3 results: diversity -----------------------------------------------
    s, top = content_slide(ctx, "Coverage & Diversity: No Accuracy Trade-Off", eyebrow=C3, tabs=C1TABS, active="Results", notes=N(59))
    # paired bars
    groups = [("Coverage · MovieLens-1M", 0.342, 0.397, "+16.1 %"), ("ILD · MovieLens-1M", 0.461, 0.516, "+11.9 %"),
              ("Coverage · Amazon-Book", 0.259, 0.336, "+29.7 %"), ("ILD · Amazon-Book", 0.535, 0.602, "+12.5 %")]
    cells = grid(4, 4, L, top + emu(0.1), W, emu(4.3), gap=emu(0.3))
    for (lab, a, b, g), (x, y, w, h) in zip(groups, cells):
        rrect(s, x, y, w, h, fill=TINT, radius=emu(0.25))
        textbox(s, x, y + emu(0.15), w, emu(0.4), [Para([Run(lab, font="xbold", size=15, color=INK)], align="ctr", lnspc=19)])
        base_y = y + h - emu(0.75)
        maxh = h - emu(1.55)
        bw = emu(0.9)
        gapb = emu(0.35)
        x0 = x + (w - 2 * bw - gapb) / 2
        scale = maxh / max(b, 0.7)
        rrect(s, x0, base_y - a * scale, bw, a * scale, fill="B9B2A6", radius=emu(0.05))
        rrect(s, x0 + bw + gapb, base_y - b * scale, bw, b * scale, fill=GREEN, radius=emu(0.05))
        textbox(s, x0 - emu(0.2), base_y - a * scale - emu(0.4), bw + emu(0.4), emu(0.35), [Para([Run(f"{a:.3f}", font="bold", size=14, color=MUTED)], align="ctr", lnspc=17)])
        textbox(s, x0 + bw + gapb - emu(0.2), base_y - b * scale - emu(0.4), bw + emu(0.4), emu(0.35), [Para([Run(f"{b:.3f}", font="xbold", size=14, color=GREEN)], align="ctr", lnspc=17)])
        textbox(s, x0 - emu(0.2), base_y + emu(0.05), bw + emu(0.4), emu(0.3), [Para([Run("HPCF", font="body", size=13, color=MUTED)], align="ctr", lnspc=15)])
        textbox(s, x0 + bw + gapb - emu(0.2), base_y + emu(0.05), bw + emu(0.4), emu(0.3), [Para([Run("DyHuCoG", font="bold", size=13, color=GREEN)], align="ctr", lnspc=15)])
        pill(s, x + w / 2 - emu(0.75), y + h - emu(0.45) + emu(0.05), g, active=True, h=emu(0.34), size=14, pad=0.2, fill=ORANGE, text_color=WHITE, line_color=ORANGE, w=emu(1.5))
    gy = top + emu(0.1) + emu(4.3) + emu(0.45)
    bar = rrect(s, L, gy, W, CB - gy - emu(0.15), fill=GREEN, radius=emu(0.25))
    shape_text(bar, [Para(md_runs("**Smaller filter-bubble effect and more discovery for the user**, while NDCG and Recall also improve: **accuracy is not traded for diversity**.", size=22, color=WHITE), align="ctr", lnspc=28)],
               anchor="ctr", insets=(emu(0.5), emu(0.1), emu(0.5), emu(0.1)))

    # --- C3 ablation ---------------------------------------------------------
    s, top = content_slide(ctx, "Ablation: Every Component Contributes", eyebrow=C3, tabs=C1TABS, active="Results", notes=N(60))
    rows = [["Variant", "ML-1M NDCG@20", "% drop", "Amazon NDCG@20", "% drop"],
            ["Full DyHuCoG", "0.2775", "–", "0.0306", "–"],
            ["w/o Shapley value", "0.2647", "4.6 %", "0.0287", "6.1 %"],
            ["w/o Hypergraph", "0.2586", "6.8 %", "0.0279", "8.9 %"],
            ["w/o Attention", "0.2678", "3.5 %", "0.0295", "3.5 %"],
            ["w/o Context", "0.2547", "8.2 %", "0.0272", "11.0 %"],
            ["w/o Diversity", "0.2614", "5.8 %", "0.0288", "5.8 %"]]
    al = ["l", "ctr", "ctr", "ctr", "ctr"]
    lw = emu(10.6)
    gf, th = table(s, L, top, lw, rows, col_widths=[3.0, 2.2, 1.5, 2.4, 1.5], size=19, head_size=18, align=al, header_align=al, row_h=emu(0.7))
    for ci in range(5):
        c = gf.table.cell(1, ci)
        c.fill.solid()
        c.fill.fore_color.rgb = RGBColor.from_string(GREEN_SOFT)
    dx = L + lw + emu(0.5)
    dw = R - dx
    card(s, dx, top + emu(0.25), dw, CB - top - emu(0.45), label="Reading",
         paras=bullets(["**Context** is the most important component (−8.2 % / −11.0 %).",
                        "**Hypergraph** structure second (−6.8 % / −8.9 %).",
                        "Removing **Shapley** weighting costs 4.6 % / 6.1 %, more on the sparser dataset.",
                        "The ablation removes one component at a time; it does not test combinations."],
                       size=18, color=WHITE, c0=YELLOW, c1=YELLOW, gap0=8), pad=(0.5, 0.7, 0.45, 0.3))

    # --- C3 efficiency -------------------------------------------------------
    s, top = content_slide(ctx, "Efficiency and Shapley Convergence", eyebrow=C3, tabs=C1TABS, active="Results", notes=N(61))
    cells = grid(4, 4, L, top + emu(0.1), W, emu(2.3), gap=emu(0.3))
    kpi(s, *cells[0], "1.78×", "training time vs HPCF **(≈ 2000 s vs 1125 s, ML-1M)**", fill=GREEN, vsize=36)
    kpi(s, *cells[1], "1.84 ms", "inference / query on ML-1M **(8.52 ms Amazon)**", fill="1E5F58", vsize=36)
    kpi(s, *cells[2], "4.4 GB", "memory ML-1M vs 4.1 GB **(17.9 vs 16.8 GB Amazon)**", fill=ORANGE, vcolor=WHITE, vsize=36)
    kpi(s, *cells[3], "M = 50", "MSE 1.4×10^{−5} · **≈ 99 % accuracy**", fill=INK, vsize=36)
    cy = top + emu(0.1) + emu(2.3) + emu(0.45)
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
    s, top = content_slide(ctx, "Statistical Significance", eyebrow=C3, tabs=C1TABS, active="Results", notes=N(62))
    cells = grid(3, 3, L, top + emu(0.1), W, emu(2.4), gap=emu(0.35))
    stats = [(r"t = 46.38", "paired t-test vs HPCF · **df = 6,039**", GREEN, YELLOW),
             (r"d_z = 1.33", "**Cohen's d_{z}** · a large effect size", "1E5F58", YELLOW),
             (r"p = 1.8 \times 10^{-270}", "after **Holm–Bonferroni** correction", ORANGE, WHITE)]
    for (tex, lab, f, vc), (x, y, w, h) in zip(stats, cells):
        rrect(s, x, y, w, h, fill=f, radius=emu(0.3))
        equation(s, x + emu(0.2), y + emu(0.3), w - emu(0.4), emu(1.15), tex, size=38, color=vc)
        textbox(s, x + emu(0.3), y + emu(1.5), w - emu(0.6), emu(0.7), [Para(md_runs(lab, size=17, color=WHITE), align="ctr", lnspc=22)], anchor="t")
    cy = top + emu(0.1) + emu(2.4) + emu(0.45)
    light_card(s, L, cy + emu(0.25), W, CB - cy - emu(0.45), label="Protocol",
               paras=bullets(["Paired t-tests on **per-user NDCG@20** (n = 6,040 users, MovieLens-1M).",
                              "DyHuCoG beats **every baseline** with very small p-values after Holm–Bonferroni correction.",
                              "**Wilcoxon signed-rank test** also significant (p < 0.001): the result does not depend on normality.",
                              "**Effect sizes are large**: the improvements really matter, they are not only statistically visible."], size=21, gap0=9), pad=(0.55, 0.7, 0.5, 0.3))

    # --- C3 robustness & interpretability -----------------------------------
    s, top = content_slide(ctx, "Cold-Start, Cross-Dataset Robustness and Interpretability", eyebrow=C3, tabs=C1TABS, active="Results", notes=N(63))
    cw = (W - emu(0.4)) / 2
    ch = emu(3.2)
    card(s, L, top + emu(0.25), cw, ch, label="Cold-start (≤ 5 interactions)",
         paras=bullets(["NDCG@20 ≈ **0.061** (user) and **0.057** (item).",
                        "About **10 % over HPCF**: Shapley weighting helps exactly where the signal is weakest."], size=20, color=WHITE, c0=YELLOW, c1=YELLOW, gap0=10), pad=(0.55, 0.7, 0.5, 0.3))
    x2 = L + cw + emu(0.4)
    rrect(s, x2, top + emu(0.25), cw, ch, fill=TINT, radius=emu(0.34))
    pill(s, x2 + emu(0.5), top + emu(0.25) - emu(0.26), "Cross-dataset NDCG@20 gain", active=True, h=emu(0.48), size=22, pad=0.36)
    cells = grid(3, 3, x2 + emu(0.5), top + emu(1.0), cw - emu(1.0), ch - emu(1.25), gap=emu(0.25))
    for (ds, g), (x, y, w, h) in zip([("MovieLens-1M", "+9.9 %"), ("Amazon-Book", "+14.8 %"), ("Yelp2018", "+11.8 %")], cells):
        kpi(s, x, y, w, h, g, ds, fill=WHITE, vcolor=GREEN, lcolor=INK, vsize=30, lsize=15)
    gy = top + emu(0.25) + ch + emu(0.4)
    light_card(s, L, gy + emu(0.25), W, CB - gy - emu(0.45), label="Interpretability & popularity bias",
               paras=bullets(["A **SHAP waterfall** breaks a recommendation down into ranking, diversity, context and preference contributions.",
                              "Shapley measures **marginal utility, not raw frequency**: weak but informative interactions keep their influence, which counters popularity bias."], size=21, gap0=9), pad=(0.55, 0.7, 0.5, 0.3))

    # --- C3 findings ---------------------------------------------------------
    s, top = content_slide(ctx, "Answers, Key Findings and Limitations", eyebrow=C3, tabs=C1TABS, active="Findings", notes=N(64, 65, 66))
    cw = (W - emu(0.4)) / 2
    ch = CB - top - emu(0.45)
    card(s, L, top + emu(0.25), cw, ch, label="RQ3 & RQ4 answered · objectives met",
         paras=bullets(["**RQ3: yes.** Attribution becomes an **in-training signal**, not a post-hoc check.",
                        "**RQ4: yes.** Ranking, coverage and diversity **improve together**.",
                        "**O1 met** · recommendation formulated as a cooperative game over users, items and contexts.",
                        "**O2 met** · preference-aware Monte Carlo Shapley embedded in message passing.",
                        "**O3 met** · +9.9 % (MovieLens) / +14.8 % (Amazon) NDCG with higher coverage and diversity.",
                        "The accuracy / diversity / context trade-off is **not fixed by nature**; largest gains on the sparsest data."],
                       size=18, color=WHITE, c0=YELLOW, c1=YELLOW, gap0=7), pad=(0.55, 0.7, 0.5, 0.3))
    light_card(s, L + cw + emu(0.4), top + emu(0.25), cw, ch, label="Limitations",
               paras=bullets(["Measurable compute overhead: roughly **1.78× the training time** of HPCF.",
                              "Depends on the availability of **meaningful context**.",
                              "Monte Carlo Shapley could be improved by **variance reduction**.",
                              "Ablation is component-wise, so it does not test factorial interactions.",
                              "Baselines fixed in early 2026: superiority is claimed **only against the tested baselines**."], size=18, gap0=7), pad=(0.55, 0.7, 0.5, 0.3))

    # --- C3 takeaways -------------------------------------------------------
    s, top = content_slide(ctx, "Takeaways", eyebrow=C3, tabs=C1TABS, active="Findings", notes=N(67))
    tk = [("First-class", "Attribution is a first-class part of the learning objective, not a post-hoc check."),
          ("Read-out", "The explanation is a direct read-out of the objective the model already optimises."),
          ("Faithful", "This makes the explanation faithful by design, rather than an outside approximation."),
          ("Axiomatic", "Built on the four Shapley axioms, in line with trustworthy-AI expectations.")]
    cells = grid(4, 4, L, top + emu(0.1), W, emu(4.2), gap=emu(0.3))
    for i, ((h1, body), (x, y, w, h)) in enumerate(zip(tk, cells)):
        f = [GREEN, "1E5F58", ORANGE, INK][i]
        box = rrect(s, x, y, w, h, fill=f, radius=emu(0.3))
        shape_text(box, [Para([Run(h1, font="title", size=28, color=YELLOW if i != 2 else WHITE, spc=-1.2)], lnspc=32),
                         Para([Run(body, font="body", size=19, color="F7F2EA")], lnspc=24, spcbef=12)],
                   anchor="t", insets=(emu(0.4), emu(0.4), emu(0.35), emu(0.3)))
    gy = top + emu(0.1) + emu(4.2) + emu(0.5)
    box = rrect(s, L, gy, W, CB - gy - emu(0.15), fill=None, line=GREEN, line_w=2.5, radius=emu(0.3))
    shape_text(box, [Para(md_runs("From **post-hoc description** (C1, C2) to **in-training guidance** (C3): the strongest claim of the thesis.", size=26, color=INK, font="bold"), align="ctr", lnspc=32)],
               anchor="ctr", insets=(emu(0.5), emu(0.1), emu(0.5), emu(0.1)))

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
    s, top = content_slide(ctx, "Synthesis of the Three Contributions", eyebrow=CC, tabs=CTABS, active="Synthesis", notes=N(69))
    rows = [["", "Main idea", "Achievement", "Key finding"],
            ["C1", "Explain black-box clustering via Shapley", "PCA–K-Means–LightGBM–TreeSHAP pipeline", "Faithful, chemistry-consistent cluster attribution (wine)"],
            ["C2", "Multi-level, large-scale clustering XAI", "Cross-level SHAP aggregation + Proposition 6.1", "Consistent across levels; explains the differences between them"],
            ["C3", "DyHuCoG hypergraph cooperative game", "Preference-aware Shapley as an in-training signal", "Accuracy + coverage + diversity improve together"]]
    gf, th = table(s, L, top, W, rows, col_widths=[1.0, 3.6, 3.8, 4.2], size=19, head_size=18, row_h=emu(1.05), align=["ctr", "l", "l", "l"], header_align=["ctr", "l", "l", "l"])
    for ri, f in ((1, GREEN), (2, "1E5F58"), (3, ORANGE)):
        c = gf.table.cell(ri, 0)
        c.fill.solid()
        c.fill.fore_color.rgb = RGBColor.from_string(f)
        fill_text_frame(c._tc.get_or_add_txBody(), [Para([Run(rows[ri][0], font="title", size=26, color=WHITE)], align="ctr", lnspc=30)], anchor="ctr")
    gy = top + th + emu(0.45)
    steps = [("Explain", "post-hoc, single level", GREEN), ("Scale", "post-hoc, hierarchical", "1E5F58"), ("Guide", "in-training signal", ORANGE)]
    n = 3
    bw = emu(4.4)
    gap = (W - n * bw) / (n - 1)
    bh = min(emu(1.35), CB - gy - emu(0.2))
    for i, (t, sub, f) in enumerate(steps):
        x = L + i * (bw + gap)
        chip(s, x, gy, bw, bh, t, fill=f, size=26, sub=sub, sub_size=16, radius=emu(0.25))
        if i < n - 1:
            arrow(s, x + bw + emu(0.1), gy + bh / 2, x + bw + gap - emu(0.1), gy + bh / 2, color=GREEN, w=3)

    # --- Publications --------------------------------------------------------
    s, top = content_slide(ctx, "Publications Supporting the Thesis", eyebrow=CC, tabs=CTABS, active="Publications", notes=N(70))
    pubs = [("I", "Shapley Values for Explaining the Black Box Nature of ML Model Clustering", "Procedia Computer Science 220, 806–811", "Published · 2023", GREEN),
            ("II", "Game Theory Meets Explainable AI: An Enhanced Approach to Understanding Black Box Models Through Shapley Values", "IJACSA 16(7), 716–725", "Published · 2025", "1E5F58"),
            ("III", "DyHuCoG: A Dynamic Hypergraph Cooperative Game for Preference-aware Recommendation", "IJIES 19(2), 887–902", "Published · 2026", ORANGE)]
    y = top
    rh = (CB - top - emu(0.2) - emu(0.3) * 2) / 3
    for (num, t, venue, status, f), i in zip(pubs, range(3)):
        yy = y + i * (rh + emu(0.3))
        rrect(s, L, yy, W, rh, fill=TINT, radius=emu(0.3))
        rrect(s, L, yy, emu(1.7), rh, fill=f, radius=emu(0.3))
        rect(s, L + emu(1.2), yy, emu(0.5), rh, fill=f)
        textbox(s, L, yy, emu(1.7), rh, [Para([Run(num, font="title", size=40, color=WHITE)], align="ctr", lnspc=44)], anchor="ctr")
        fit_textbox(s, L + emu(2.1), yy + emu(0.2), W - emu(5.6), rh - emu(0.4),
                    [Para([Run("Louhichi, M. & Lazaar, M.", font="xbold", size=15, color=ORANGE)], lnspc=19),
                     P("**" + t + "**", size=21, spcbef=4),
                     Para([Run(venue, font="body", size=17, color=MUTED)], lnspc=21, spcbef=4)], anchor="ctr", min_scale=0.7)
        pill(s, R - emu(3.3), yy + rh / 2 - emu(0.24), status, active=True, h=emu(0.48), size=16, pad=0.3, fill=f, text_color=WHITE, line_color=f, w=emu(3.0))

    # --- Limitations ---------------------------------------------------------
    s, top = content_slide(ctx, "Limitations, Stated Honestly", eyebrow=CC, tabs=CTABS, active="Limitations", notes=N(71))
    lims = [("Computational", "Exact Shapley is not feasible; every contribution relies on approximation, surrogates or limited reporting.", GREEN),
            ("Methodological", "Clustering depends on surrogate fidelity; recommendation depends on stable approximate contributions and useful context.", "1E5F58"),
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

    # --- Conclusion ----------------------------------------------------------
    s, top = content_slide(ctx, "Conclusion", eyebrow=CC, tabs=CTABS, active="Conclusion", notes=N(73))
    box = rrect(s, L, top, W, emu(1.6), fill=GREEN, radius=emu(0.3))
    shape_text(box, [Para([Run("THESIS ANSWER", font="xbold", size=14, color=YELLOW, spc=1.8)], align="ctr", lnspc=18),
                     Para(md_runs("Cooperative game theory can serve as a **shared methodological view for actionable explanation** across clustering and recommendation.", size=24, color=WHITE, font="bold", bold_font="xbold"), align="ctr", lnspc=30, spcbef=8)],
               anchor="ctr", insets=(emu(0.5), emu(0.1), emu(0.5), emu(0.1)))
    outs = [("Common language", "Shapley attribution as a common formal language for assigning importance to features, interactions and contexts."),
            ("Three achievements", "Faithful clustering explanation, consistent multi-level explanation, contribution-aware recommendation learning."),
            ("Explanation as method", "Not a comment added later: from post-hoc description to in-training guidance."),
            ("Trustworthy AI", "Aligned with EU AI Act, OECD principles and GDPR expectations.")]
    cells = grid(4, 4, L, top + emu(2.0), W, CB - top - emu(2.2), gap=emu(0.3))
    for i, ((h1, body), (x, y, w, h)) in enumerate(zip(outs, cells)):
        f = [TINT, TINT2, TINT, TINT2][i]
        box = rrect(s, x, y, w, h, fill=f, line=None, radius=emu(0.3))
        badge(s, x + emu(0.35), y + emu(0.35), emu(0.6), f"{i+1}", fill=ORANGE, color=WHITE, size=18)
        fit_textbox(s, x + emu(0.35), y + emu(1.15), w - emu(0.7), h - emu(1.35),
                    [H(h1, size=22, color=GREEN), P(body, size=18, spcbef=8)], min_scale=0.7)

    # --- References ----------------------------------------------------------
    s, top = content_slide(ctx, "References", eyebrow=CC, tabs=None, notes=N(74))
    refs = [("R1", "Louhichi, M. & Lazaar, M. Shapley Values for Explaining the Black Box Nature of ML Model Clustering. Procedia Computer Science 220, 806–811 (2023)."),
            ("R2", "Louhichi, M. & Lazaar, M. Game Theory Meets Explainable AI: An Enhanced Approach to Understanding Black Box Models Through Shapley Values. IJACSA 16(7), 716–725 (2025)."),
            ("R3", "Louhichi, M. & Lazaar, M. DyHuCoG: A Dynamic Hypergraph Cooperative Game for Preference-aware Recommendation. IJIES 19(2), 887–902 (2026)."),
            ("R4", "Lundberg, S.M. & Lee, S.-I. A Unified Approach to Interpreting Model Predictions (SHAP). NeurIPS 30, 4765–4774 (2017)."),
            ("R5", "Lundberg, S.M. et al. Consistent Individualized Feature Attribution for Tree Ensembles. KDD 2018, 2713–2723 (2018)."),
            ("R6", "Shapley, L.S. A Value for n-Person Games. Contributions to the Theory of Games II, 307–317 (1953)."),
            ("R7", "Gramegna, A. & Giudici, P. SHAP-based Clustering Explanations. Stats 4(4), 938–959 (2021)."),
            ("R8", "Wang, X. et al. Hypergraph Learning: Methods and Practices. IEEE TPAMI 44(5), 2543–2563 (2022)."),
            ("R9", "European Commission. Proposal for a Regulation on Artificial Intelligence (EU AI Act). COM(2021) 206 final (2021).")]
    y = top - emu(0.2)
    rh = (CB - y - emu(0.1) - emu(0.1) * 8) / 9
    for i, (tag, t) in enumerate(refs):
        yy = y + i * (rh + emu(0.1))
        rrect(s, L, yy, W, rh, fill=TINT if i % 2 == 0 else TINT2, radius=emu(0.14))
        chip(s, L + emu(0.15), yy + emu(0.1), emu(0.9), rh - emu(0.2), tag, fill=GREEN if i < 3 else ORANGE, size=15, radius=emu(0.1))
        fit_textbox(s, L + emu(1.3), yy, W - emu(1.5), rh, [P(t, size=17)], anchor="ctr", min_scale=0.7)

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

    deck.finalize(out)
    return ctx.n


if __name__ == "__main__":
    tpl_path = sys.argv[1]
    out_path = sys.argv[2]
    n = build(tpl_path, out_path)
    print(f"built {n} slides -> {out_path}")
    for slide_no, scale, what in FIT_REPORT:
        print(f"  fit note: slide {slide_no} scaled to {scale:.2f}: {what}")
