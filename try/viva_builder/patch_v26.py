"""
Patch MOUAD_LOUHICHI_VIVA_40min_BeigeGreen_v25.pptx -> ..._v26.pptx

Applies the fixes listed in DEEP_READING_REVIEW_v25.md (sections 4 and 6). Every
replacement is kept at or below its old length, or inside a box that has slack,
because the deck cannot be rebuilt here: the template fonts and the thesis-figure
crops live in /tmp/viva_build, which is not part of the repository.

  content   rain -> wind direction (slide 19); "≈ 96 %" -> "≈ 98 %" (slide 55);
            "novelty" -> "context" (slides 53, 63); "k = 3 → 9 sub-clusters" and
            "3 → 9" dropped (slides 19, 42, 43); Fig. 6.3 caption (slide 46);
            "(GroupLens, 2000)" -> "(GroupLens benchmark)" (slide 20);
            reference [19] attribution and reference [28] issue number (slide 74)
  scope     market-size figure removed and AI Act wording corrected (slides 4, 6);
            LIME comparator wording (slides 31, 34); "p < 0.05 ... both datasets"
            (slide 57); "one tenth of the gap ... on every metric" (slide 77)
  speech    speaker notes re-aligned slide by slide (notes_v26.json): the
            Contribution III off-by-one, the RQ note parked on slide 14, the
            duplicated dataset / conclusion / reference notes, the timing cues,
            and a redundancy pass that brings the spoken total back to ~36 min

Run:  python3 patch_v26.py
"""
import json
import os

from pptx import Presentation

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.normpath(os.path.join(HERE, "..", "MOUAD_LOUHICHI_VIVA_40min_BeigeGreen_v25.pptx"))
DST = os.path.normpath(os.path.join(HERE, "..", "MOUAD_LOUHICHI_VIVA_40min_BeigeGreen_v26.pptx"))
NOTES_IN = os.path.join(HERE, "notes_v25.json")
NOTES_OUT = os.path.join(HERE, "notes_v26.json")

# ---------------------------------------------------------------------------
# 1. text replacements, by slide number: (old, new, expected number of hits)
# ---------------------------------------------------------------------------
EDITS = {
    4: [
        ("Recommenders shape news, study, health and credit decisions; market > $15B by 2029.",
         "Recommenders shape news, study, health and credit decisions in systems used at global scale.", 1),
        ("must explain.", "transparency duties.", 1),
    ],
    6: [
        ("EU AI Act (Art. 13): high-risk systems must provide explanations ",
         "EU AI Act: high-risk systems must be transparent (Art. 13) and ", 1),
        ("in human-understandable terms", "decisions can be challenged (Art. 86)", 1),
    ],
    19: [
        ("dew point, rain, wind speed", "dew point, wind direction, wind speed", 1),
    ],
    20: [
        ("(GroupLens, 2000).", "(GroupLens benchmark).", 1),
    ],
    31: [
        ("LIME-based surrogate explanation on the same partition",
         "LIME surrogate, as the theoretical comparator (Ch. 5)", 1),
    ],
    34: [
        ("Four axioms; higher stability and cross-cluster comparability",
         "Four axioms; LIME comparator theoretical (Ch. 5, §5.4)", 1),
    ],
    42: [
        ("3 → 9", "k = 3", 1),
    ],
    43: [
        ("Each coarse cluster split again into sub-clusters (3 → 9)",
         "Each coarse cluster split again into sub-clusters", 1),
    ],
    46: [
        ("Fig. 6.3 (thesis): SHAP importance per sub-cluster, level 2 of the hierarchy",
         "Fig. 6.3 (thesis): cluster-specific SHAP importance, coarse level", 1),
    ],
    53: [
        ("accuracy, diversity and novelty.", "accuracy, diversity and context.", 1),
    ],
    55: [
        ("≈ 96 %", "≈ 98 %", 1),
        ("M = 50 balances estimator quality against per-epoch cost; rows 25/100 show the O(1/M) trend.",
         "Accuracy vs a high-sample reference: M = 25 already reaches ≈ 98 %, rows 25/100 show the O(1/M) trend.", 1),
    ],
    57: [
        (" in NDCG@20 and Recall@20, with p < 0.05 after correction.",
         " in NDCG@20 and Recall@20; significance tabulated on MovieLens-1M (Table 7.6).", 1),
    ],
    63: [
        ("·novelty", "·context", 1),
    ],
    74: [
        ("IJIES 18, 241–257 (2025).", "IJIES 18(9), 241–257 (2025).", 1),
        ("Dua, D. & Taniskidou, E. Beijing Multi-Site Air Quality Data.",
         "Zhang, S. et al. Beijing Multi-Site Air Quality Data Set.", 1),
    ],
    77: [
        ("Standard deviations are roughly ", "The ", 1),
        ("one tenth of the gap", "±1σ bands", 1),
        (" between DyHuCoG and HPCF on every metric, so the ordering is stable across seeds.",
         " never overlap between DyHuCoG and HPCF on MovieLens-1M; on Amazon-Book the standard deviations "
         "are close to the gap for NDCG@20 and Recall@20, so those gains are reported as descriptive.", 1),
    ],
}

# table / KPI rewrites: (slide, row, col, new text); row None = the KPI value
CELLS = [
    (19, 5, 1, "k = 3 coarse regimes"),
    (42, None, None, "k = 3"),
]


# ---------------------------------------------------------------------------
# 2. speaker notes keyed by deck slide number (slides not listed keep the
#    notes_v25.json text). Spoken total is re-measured at the end.
# ---------------------------------------------------------------------------
NOTES = {
    "1": "Good morning, Mister President. Good morning, Professors. Thank you for the opportunity to present my work today.\n\nMy name is Mouad Louhichi, and the thesis I am defending, supervised by Professor Mohamed Lazaar, is entitled Cooperative Game Theory for Explainable AI in Recommendation Systems, A Shapley Framework for Actionable Insight.\n\nThe idea to keep in mind: Shapley attribution is not only a post-hoc explanation method. In this thesis it becomes a unified framework that explains black-box models, stays consistent across levels of detail, and guides how recommendation systems learn.\n\n(Pre-defence check: confirm the jury list on this slide against the official convocation.)",
    "3": "So let me start with the introduction, and more specifically with the motivation behind this research.\n\nThe first question I would like to address is: why has explainability become a core requirement for modern recommendation systems?\n\nTime check: minute one.",
    "4": "Let me start with the motivation. Today, black-box AI systems shape what billions of people see, buy and watch every day. Recommenders already influence news, study, health and credit decisions, so an unexplained ranking is a governance problem, not only a technical one.\n\nBut these state-of-the-art systems stay black boxes for users and designers. Deep and graph models hide their logic and are hard to audit, and regulation now pushes back: under the EU AI Act, high-risk systems must be transparent enough to be interpreted, and an affected person can ask for an explanation of a decision.\n\nSo the real question is how to build transparency into the model, instead of adding it afterwards. What we want is insight that is accountable, auditable and actionable, not just accurate.\n\nThat is the core tension you see on this slide: as models gain power, they lose the transparency needed for trustworthy use.\n\nThis thesis treats accuracy and interpretability as two goals to be met together, not traded against each other.",
    "8": "Now I will move from the motivation to the research problem itself.\n\nTo understand where the difficulty comes from, I will briefly review the main recommendation approaches and explain their respective limitations.\n\nTime check: about minute five.",
    "13": "From this evolution, several limits appear. Data sparsity, because the interaction matrix is almost empty. Cold-start, when new users or items have no history. Popularity bias, where exposure follows exposure. And above all, the absence of interpretability, which for clustering is even harder, because local and global explanations rarely agree.",
    "14": "The three structural limitations are on this slide, and they are what this thesis works on.\n\nLack of explainability: complex models are still hard to explain faithfully and actionably.\n\nDifficulty of scaling: a local explanation does not carry over to a multi-level structure, or to hundreds of thousands of records.\n\nWeak integration into learning: most explanations stay post-hoc, so they never shape how the model learns, nor how it handles the accuracy, diversity and context trade-off.\n\nThe gap is the orange box: the literature still lacks one cooperative-attribution framework that explains clustering faithfully, stays consistent across levels, and then works as an in-training signal in recommendation.",
    "15": "Five questions structure the work, and the slide maps each one to a contribution.\n\nRQ1: can Shapley values explain black-box clustering faithfully, at instance level and at cluster level? RQ2: can this extend to large-scale, multi-level clustering while staying feasible and consistent? RQ3: can cooperative attribution move beyond post-hoc and become part of how a recommender learns? RQ4: can ranking, context and diversity improve together when importance comes from a cooperative-game utility? RQ5: what does one cooperative-game view bring to both tasks?",
    "16": "So the thesis is three contributions that build on each other.\n\nC1 explains a black-box partition: the features are the players, the Silhouette of the clustering is the value function, and a LightGBM surrogate with TreeSHAP brings the attribution back to the original variables.\n\nC2 keeps that explanation consistent across levels and at scale, through the cross-level aggregation of Proposition 6.1.\n\nC3, DyHuCoG, moves attribution inside the model: preference-aware Monte Carlo Shapley becomes an in-training signal on a hypergraph.\n\nExplanation, then scalability, then action.",
    "17": "Before presenting the contributions, I will first describe the common experimental protocol used throughout the thesis.\n\nThe objective is to make the evaluation consistent and reproducible across all experiments.\n\nI will present the datasets, the baselines, the evaluation metrics, and the computational environment.\n\nTime check: about minute ten.",
    "20": "The first recommendation benchmark is MovieLens-1M: about one million ratings from 6,040 users on 3,706 movies, with a density near 0.045.\n\nIt is the standard benchmark of the field, so the comparison with LightGCN, HCCF and HPCF is directly readable.\n\nRatings above 3 become positive implicit feedback, and the genre is used as the context proxy.",
    "21": "The second benchmark is Amazon-Book: 52,643 users, 91,599 books and about three million interactions, so the density is near 0.0006 and the user-item matrix is almost empty.\n\nI include it to test whether Shapley-guided weighting helps most when the signal is weakest, and it is the large-scale benchmark of Contribution III.\n\nThat gap between 0.045 and 0.0006 is the core of the robustness argument.",
    "24": "Different metrics answer different questions. For recommendation, NDCG@20 is the main ranking measure, and coverage and intra-list diversity matter because quality is not only accuracy. For clustering, Silhouette and Davies-Bouldin judge the partitions, and they are also the value function of the clustering game.",
    "26": "With this experimental framework established, I can now move to the first contribution of this thesis.\n\nThe objective here is to answer the following question: can we explain the decisions of a black-box clustering model using a principled attribution method?\n\nTime check: about minute fourteen.",
    "28": "This contribution has three objectives. Provide a cluster-level explanation that keeps feature-level attribution. Keep that attribution in the original variables, because explanations are only useful when domain experts can read them. And justify why the cooperative concept, rather than a local surrogate, is the right attribution rule.",
    "29": "Before the methodology, the mathematical foundation: cooperative game theory.\n\nA cooperative game has players, the coalitions between them, and a value function that measures what each coalition creates on its own. On the slide, the band example: alone, Guitar, Voice and Drums earn 60, 40 and 20, reach 140 as a duo, and 200 as the whole band; Guitar and Drums together are worth 100.\n\nThe Shapley value shares the total fairly, as the average marginal contribution over every arrival order: one order adds 40, then 40, then 120, and the average over the six orders is 90, 70, 40. As the orange bar states, it is the only rule satisfying the four axioms at once.\n\nIn this thesis, the players are the input features and the value function is the Silhouette of the clustering.",
    "30": "Why a surrogate? Direct TreeSHAP on K-Means is impossible, because TreeSHAP explains tree models, not centroids, and explaining the PCA representation would move the attribution away from the interpretable variables. So the pipeline is four steps: K-Means labels, a LightGBM surrogate that predicts them from the original features, TreeSHAP on that surrogate, and then global importance, cluster profiles and local force plots. The bridge is valid only while the surrogate stays faithful: the floor is macro-F1 about 0.82.",
    "33": "The ranking is chemically readable: density first, then pH, fixed acidity, sulfur dioxide and alcohol. Density and pH separate wine styles, sulfur dioxide reflects preservation, alcohol shapes body. This is not a side effect of the classifier: the surrogate reproduces the partition from the original variables, and every driver is something a wine maker can act on.",
    "34": "This answers RQ1. Shapley values can explain a black-box partition when the surrogate is faithful, at cluster level and at instance level, in the original variables. Compared with LIME, the advantage is the formal cooperative-game foundation: efficiency, symmetry, null player and additivity.",
    "37": "The takeaway is that Shapley attribution is a principled way to explain an unsupervised model, and keeping it in the original feature space is what makes it actionable. But real data are rarely single-level: broad groups contain nested sub-groups. That is the next question.",
    "38": "This brings me to the second contribution of the thesis.\n\nThe objective is to extend Shapley-based explanation from single-level clustering to large-scale and multi-level clustering.\n\nThis contribution addresses the second research question.\n\nTime check: about minute twenty.",
    "39": "Here the difficulty is scale and consistency together. When a large cluster is divided, the explanation must stay readable for the parent, for each child, and across levels. Existing hierarchical work reports structure but gives no formal link between a parent explanation and its children: that missing link is the research gap.",
    "40": "Three objectives. Build a genuine multi-level workflow, with a surrogate per level rather than a rerun of the single-level pipeline. Provide a formal consistency argument, Proposition 6.1, that relates parent and child importance. And validate at scale on new data: the Beijing air quality records, a domain far from wine.",
    "41": "The approach is recursive. The full dataset is partitioned into coarse clusters, then each cluster can be divided again. At every level a surrogate is trained and SHAP is computed in the same original feature space, so importance stays comparable across levels. The aggregation is not a naive average: it respects cluster size and the nesting structure.",
    "42": "Proposition 6.1 is the theoretical core: the expected absolute importance of a feature at the parent level equals the size-weighted expectation over its children, plus a residual induced by surrogate approximation, which vanishes under perfect fidelity. It does not say that explanations are identical across levels; it says the differences can be interpreted rather than dismissed as inconsistency.",
    "43": "The protocol keeps the same principles as Contribution I, with two changes. First, clustering runs on the full Beijing dataset. Second, each level gets its own surrogate, and the explanations are then aggregated across levels with size weights, followed by a sensitivity check on k, projection dimension and surrogate depth.",
    "46": "This figure is where the multi-level view earns its keep. At the coarse level, temperature and dew point dominate because they separate the broad regimes: that is regime selection. Inside a cluster, other variables become informative, CO, SO2, PM10, wind speed, pressure or ozone: that is variation within a regime. The change is not a contradiction; it is what Proposition 6.1 makes interpretable.",
    "49": "Some limitations remain. The clustering process is still static, although the air quality data have a temporal dimension. The explanations still depend on surrogate models. And most importantly, attribution is still post-hoc: it explains what the model has learned, but it does not take part in the learning itself. That is what opens Contribution III.",
    "51": "This brings me to the third contribution of this thesis: DyHuCoG, which stands for Dynamic Hypergraph Cooperative Game.\n\nThis contribution represents the main transition of the thesis.\n\nIn the first two contributions, Shapley values were used to explain models after they were trained.\n\nHere, the objective is different: can attribution become part of the learning process itself?\n\nTime check: about minute twenty-six.",
    "52": "The gap in existing models is that message importance is uniform or attention-weighted, with no marginal-contribution account, diversity is a re-ranking heuristic, and interpretability is added after prediction. Contributions I and II showed that Shapley attribution is faithful, but still post-hoc: it never changed what the model learned. That is what DyHuCoG changes.",
    "53": "This contribution addresses two research questions, shown at the top of the slide: can cooperative attribution become part of how a recommender learns, and can it improve ranking, context and diversity together?\n\nThree objectives answer them. First, model recommendation as a cooperative game over users, items and contexts, where the coalition utility mixes accuracy, diversity and context. Second, put preference-aware Monte Carlo Shapley inside message passing, as dynamic hyperedge weights. Third, show that ranking, coverage and diversity improve together on two datasets.",
    "54": "To formulate the idea, recommendation is represented as a cooperative game. The players are the users, the items and the contexts of an episode, and their interactions are hyperedges, which allows higher-order relations. Each entity's contribution is estimated with Shapley values, so the model learns not only that a relationship exists, but how much it is worth for the objective.",
    "55": "The main challenge is that exact Shapley computation is impossible for large recommendation systems, because the number of coalitions grows exponentially with the number of players. So DyHuCoG samples a limited number of permutations and averages the marginal contributions, which preserves the main properties of the estimator. The table gives accuracy against a high-sample reference, not against the exact values: 25 samples already reach about 98 percent, and M = 50 reaches about 99, so 50 is the balance point rather than the cheapest option.",
    "57": "This is the protocol for the recommendation study. Two datasets: MovieLens-1M as the dense benchmark and Amazon-Book as the sparse one, with Yelp2018 as an auxiliary check. The split is user-level and time-ordered, 70, 10 and 20, with a leave-one-out target, and ratings above 3 are positives. Six baselines from four model families, four metrics with NDCG@20 as the main one, five seeds, and a component-wise ablation.",
    "58": "The results on MovieLens-1M show that DyHuCoG achieves the best performance among the evaluated methods.\n\nCompared with the strongest baseline, HPCF, the NDCG score improves from 0.2528 to 0.2775, about 9.8 percent, and Recall improves as well, from 0.2098 to 0.2362.\n\nCoverage and diversity stay higher too, so the gain does not come from pushing popular items: the variety of the recommendations is preserved.",
    "59": "The same evaluation is conducted on Amazon-Book, a much more challenging sparse recommendation scenario.\n\nDespite the higher difficulty, DyHuCoG continues to outperform the baselines, and the improvement over HPCF reaches approximately 13.3 percent in NDCG.\n\nSo cooperative attribution remains useful even when interaction information is limited.",
    "60": "The ablation removes one component at a time, and every component matters. Context is the largest drop, so contextual signals are the substrate; the hypergraph structure comes next; removing Shapley weighting costs 4.6 percent on MovieLens-1M and 6.1 percent on Amazon-Book. So cooperative attribution contributes directly to learning, and more so when the data are sparser.",
    "63": "These results answer RQ3 and RQ4. Shapley attribution can move beyond post-hoc and become part of the learning process, and ranking, coverage and diversity improve together on both datasets, with the largest gains where the data are sparsest. Attribution becomes not only an explanation mechanism, but a learning mechanism.",
    "64": "To summarize Contribution III, DyHuCoG transforms the role of explanation: attribution is used while the model learns. The ablation shows it matters, removing Shapley weighting costs 4.6 percent on MovieLens-1M and 6.1 percent on Amazon-Book. On MovieLens-1M the improvement is statistically solid, t equals 46.38 with an effect size of 1.33 after Holm correction; on Amazon-Book I report the same ordering as a descriptive gain over five seeds.",
    "67": "So let me bring everything together: the synthesis, the publications, the limitations, the perspectives, and then the thesis answer.\n\nBefore the closing claim, I want to state the limitations honestly, and the perspectives they open.\n\nTime check: about minute thirty-four.",
    "68": "This table is the thesis in one view.\n\nC1 explains a black-box partition with Shapley attribution. C2 keeps that explanation consistent across levels at scale. C3, DyHuCoG, uses attribution as an in-training signal, and improves accuracy, coverage and diversity together.\n\nRead across the three rows, the same logic moves from post-hoc description to in-training guidance: explain, scale, guide.",
    "71": "The limitations become an agenda, and I see four directions.\n\nMore scalable cooperative attribution: lower-variance Shapley estimators, learned proposal distributions and adaptive refresh rules.\n\nTruly online and streaming recommendation, with changing graphs and delayed feedback, which also removes the static-graph assumption.\n\nRicher user-centred evaluation: do explanations measurably improve judgement, trust and perceived fairness?\n\nAnd broader trustworthy-AI evaluation, including exposure fairness and auditing for governance.",
    "72": "The thesis answer is in the orange box: cooperative game theory can serve as a shared methodological view for actionable explanation across clustering and recommendation.\n\nFour outcomes support it: a common formal language for assigning importance to features, interactions and contexts; faithful clustering explanation and consistent multi-level explanation; explanation as a method rather than a comment added later; and alignment with the expectations of the AI Act, the OECD principles and the GDPR.\n\nExplanation does not have to remain a description of what happened. It can help us understand, control and improve AI systems.",
    "73": "The first of the two reference slides lists the foundations of this work: my own three papers, Shapley, SHAP, TreeSHAP, LIME, and the recommender baselines from matrix factorisation to HPCF.\n\nI will not discuss them individually, but they are the scientific foundations of the three contributions.",
    "74": "The second reference slide completes the list: the datasets, the evaluation metrics, the AI Act and OECD texts, and the related work with the team.\n\nTaken together, these two slides are the full bibliography of the thesis.",
    "75": "Thank you very much for your attention.\n\nI would be pleased to answer your questions and discuss any aspect of this work: the methodology, the theoretical foundations, or the experimental results.\n\nI will stay on the closing slide for the discussion.",
    "76": "Thank you very much for your attention.\n\nI would be pleased to answer your questions and discuss any aspect of this work, including the methodology, theoretical foundations, or experimental results.\n\n(Pre-defence check: confirm the jury list on this slide against the official convocation.)",
}


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------
def para_text(p):
    return "".join(r.text for r in p.runs)


def set_para(p, text):
    runs = p.runs
    if not runs:
        return False
    runs[0].text = text
    for r in runs[1:]:
        r._r.getparent().remove(r._r)
    return True


def iter_paragraphs(slide):
    for sh in slide.shapes:
        if sh.has_text_frame:
            for p in sh.text_frame.paragraphs:
                yield p
        if getattr(sh, "has_table", False) and sh.has_table:
            for row in sh.table.rows:
                for cell in row.cells:
                    for p in cell.text_frame.paragraphs:
                        yield p


def replace_in_slide(slide, old, new):
    for p in iter_paragraphs(slide):
        for r in p.runs:
            if old in r.text:
                r.text = r.text.replace(old, new)
                return 1
    for p in iter_paragraphs(slide):
        if old in para_text(p):
            set_para(p, para_text(p).replace(old, new))
            return 1
    return 0


def main():
    prs = Presentation(SRC)
    report = []

    for slide_no, pairs in EDITS.items():
        slide = prs.slides[slide_no - 1]
        for old, new, want in pairs:
            n = replace_in_slide(slide, old, new)
            report.append((slide_no, n, want, old[:66]))

    for slide_no, row, col, text in CELLS:
        slide = prs.slides[slide_no - 1]
        done = 0
        if row is None:
            for sh in slide.shapes:
                if sh.has_text_frame and sh.text_frame.text.strip() in ("3 → 9", "k = 3"):
                    set_para(sh.text_frame.paragraphs[0], text)
                    done = 1
        else:
            for sh in slide.shapes:
                if getattr(sh, "has_table", False) and sh.has_table:
                    set_para(sh.table.rows[row].cells[col].text_frame.paragraphs[0], text)
                    done = 1
                    break
        report.append((slide_no, done, 1, f"cell/KPI -> {text!r}"))

    # ---- speaker notes -----------------------------------------------------
    old_notes = json.load(open(NOTES_IN))
    new_notes = dict(old_notes)
    new_notes.update(NOTES)

    spoken = sum(len(v.split()) for k, v in new_notes.items() if k.isdigit() and int(k) <= 76)
    minutes = spoken / 130.0
    new_notes["2"] = old_notes["2"].replace(
        "the next thirty-six minutes", f"the next {int(round(minutes))} minutes")

    for i, s in enumerate(prs.slides, 1):
        if str(i) in new_notes:
            s.notes_slide.notes_text_frame.text = new_notes[str(i)]

    json.dump(new_notes, open(NOTES_OUT, "w"), ensure_ascii=False, indent=1)
    prs.save(DST)

    print(f"wrote {DST}")
    print(f"wrote {NOTES_OUT}")
    print(f"spoken words slides 1-76: {spoken}  ({minutes:.1f} min @130 wpm, {spoken/120:.1f} @120 wpm)")
    print(f"slide 2 note now advertises: the next {int(round(minutes))} minutes")
    bad = [(sl, n, w, o) for sl, n, w, o in report if n != w]
    if bad:
        print("\n!! replacements that did not match the expected count:")
        for sl, n, w, o in bad:
            print(f"   slide {sl}: got {n}, expected {w} for {o!r}")
    else:
        print(f"\nall {len(report)} text replacements matched exactly (one each)")


if __name__ == "__main__":
    main()
