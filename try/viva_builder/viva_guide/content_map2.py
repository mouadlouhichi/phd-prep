# -*- coding: utf-8 -*-
"""Section playbooks 4-7 plus the discussion stage (slides 26-79)."""

S4 = {
    "id": "contribution-i",
    "kicker": "Section 4 · slides 26-37 · 5.6 min",
    "title": "Contribution I: explainable black-box clustering",
    "range": "26-37",
    "words": "730",
    "m130": "5.6",
    "m120": "6.1",
    "search": "contribution I clustering shapley value cooperative game band example surrogate LightGBM TreeSHAP wine k selection interpretability density pH",
    "purpose": """
- Make the cooperative-game idea concrete before any result appears: players, coalitions, the value function, the Shapley value, the four axioms.
- Justify the surrogate bridge without hiding its cost: TreeSHAP explains trees, K-Means is not a tree, so a LightGBM surrogate reconstructs the partition and the explanation is valid only up to its fidelity (macro-F1 ≈ 0.82).
- Deliver the wine result as a domain reading (density, pH, fixed acidity, sulfur dioxide, alcohol), not as a bar chart, and defend the choice of k = 3 although k = 2 has better geometry.
""",
    "arc": [
        ("Slides 29 and 30 are the two technical slides of the section", "Slide 29 teaches the Shapley value with "
         "the three-piece band; slide 30 shows the four-step pipeline. Everything else in section 4 is a consequence. "
         "Budget your voice: these two slides are 213 of the section's 730 words and they are where a jury decides "
         "whether you understand your own method."),
        ("The k-selection result is a philosophical claim, not a metric", "Choosing k = 3 with Silhouette 0.144 over "
         "k = 2 with 0.214 tests whether you meant what you said on slide 5: interpretability can outrank geometry. "
         "Deliver it as a deliberate trade-off, name the cost, and repeat that 0.63 belongs to Beijing, not to wine."),
    ],
    "slides": [
        {"n": "26", "title": "Contribution I divider",
         "screen": "Section 04: objectives, methodology, results in three cards.",
         "how": "Frame the contribution in one sentence: explain a black-box partition with a principled attribution "
                "method, and keep the answer in the language of the domain. Say the time-check cue: about minute "
                "fourteen. Do not read the three cards.",
         "time": "≈ 18 s", "cue": "Cue 4. Arrival time ≈ 13.5 min, on plan."},
        {"n": "27", "title": "Research Gap",
         "screen": "Five gap bullets and the orange gap box: no axiomatic way to explain why clustering put an observation in a cluster, in the original space and consistently across clusters.",
         "how": "Give the four reasons clustering is the hardest test bed — no target variable, structure created by the "
                "model, local-or-global but not both, no fairness guarantee for LIME-style credit — then read the box. "
                "The sentence to land: in clustering the model creates its own structure, so cluster meaning must be "
                "worked out after the fact.",
         "time": "≈ 34 s", "cue": "Do not say “SHAP is better than LIME empirically” here; the deck's position is that SHAP is better founded (question C5)."},
        {"n": "28", "title": "RQ1 and Objectives",
         "screen": "RQ1 strip plus a three-row table: O1 cluster-level explanation, O2 original feature space, O3 justify Shapley over LIME, with where each is shown.",
         "how": "State RQ1 as a question, then the three objectives as three promises you will be held to. Point to the "
                "“where it is shown” column so the jury knows the evidence is coming. Note the honest framing of O3: "
                "the justification is axiomatic, and the LIME comparison is theoretical (Chapter 5, §5.4).",
         "time": "≈ 22 s", "cue": "The status table on slide 34 marks all three “Met”. If asked, say what “met” means for O3: an argument, not an experiment."},
        {"n": "29", "title": "The Cooperative Game and the Shapley Value",
         "screen": "Three ingredients (players, coalitions, characteristic function), the Shapley formula, and a six-row band table: Guitar 60, Voice 40, Drums 20, G+V 140, V+D 80, G+V+D 200; the six arrival orders average to 90 / 70 / 40.",
         "how": "Slow down. This is the mathematical heart of the whole thesis. Tell the band story in four sentences: "
                "three players, what each subset can earn, one arrival order adds 40 then 40 then 120, and the average "
                "over all six orders gives 90 / 70 / 40, summing to the 200 the band earns. Then transfer the "
                "vocabulary: in this thesis the players are the input features and the value function is the Silhouette "
                "of the clustering. Close on the four axioms and why the average-over-orders rule is the only "
                "allocation satisfying all four at once.",
         "time": "≈ 62 s", "cue": "The table omits the coalition {G, Drums} = 100 because there is no room; if asked, give it — the 90/70/40 average is only consistent with it. This is exactly the kind of detail that turns a good answer into a convincing one."},
        {"n": "30", "title": "The Bridge: LightGBM Surrogate + TreeSHAP",
         "screen": "Four-step flow: K-Means → cluster labels → LightGBM multiclass surrogate → TreeSHAP → explanation in the original feature space, plus “How” and “Why” columns.",
         "how": "Use the four boxes as your four sentences, then spend the rest on the why: TreeSHAP cannot explain "
                "K-Means directly because it explains trees, not centroids; explaining the PCA representation would "
                "move the answer away from interpretable variables; the surrogate keeps the chemistry terms. State the "
                "validity condition clearly: the bridge is only as good as the surrogate, and the floor is macro-F1 "
                "around 0.82.",
         "time": "≈ 36 s", "cue": "The most likely attack is “you are explaining the surrogate, not K-Means” (question C3). Meet it before it is thrown: say “the explanation is faithful to a faithful reconstruction of the partition”."},
        {"n": "31", "title": "Evaluation Protocol",
         "screen": "Eight-row protocol table: dataset, clustering, choice of k, surrogate, attribution, outputs, comparison; plus four “what counts as success” bullets.",
         "how": "Six short sentences, one per row that matters: 4,898 by 11 standardised features, K-Means++ over k "
                "2-10, elbow plus Silhouette plus Davies-Bouldin, LightGBM with five-fold cross-validation, exact "
                "TreeSHAP in the original eleven features, global ranking plus cluster profiles plus force plots. Then "
                "the success criteria, especially the fidelity floor. Fifteen to twenty seconds total.",
         "time": "≈ 14 s", "cue": "In v26 the comparison row was narrowed to “LIME surrogate, theoretical comparator (Ch. 5)”. Keep that wording."},
        {"n": "32", "title": "Choosing k: Interpretability over Geometry",
         "screen": "k-scan bullets, the two-row comparison table (k = 2: 0.214 / 1.775; k = 3: 0.144 / 2.097), the k* = 3 tile and the 0.82 fidelity tile.",
         "how": "Say the trade-off explicitly: geometrically k = 2 wins, and we choose k = 3 anyway, because three "
                "clusters give distinct explanatory profiles and therefore more actionable output. Name the price you "
                "paid for that choice — a weaker separation — instead of hiding it. Then close the trap: the higher "
                "Silhouette 0.63 belongs to Beijing, not to this partition.",
         "time": "≈ 31 s", "cue": "This is the most quotable slide of section 4. If the jury asks “is that scientific?”, answer with question C7. If pressed, add the corroborating detail: the same k = 3 choice also wins geometrically on the Beijing corpus (0.626 / 0.553 against 0.265 / 1.503 at k = 2), so the selection is a balance across both corpora, not a wine-only judgement."},
        {"n": "33", "title": "Global SHAP Ranking: Wine Quality",
         "screen": "Reading bullets, Fig. 5.1 (global importance) and Fig. 5.2 (per-cluster signatures).",
         "how": "Read the ranking as chemistry: density first, then pH, fixed acidity, sulfur dioxide and alcohol. Give "
                "one clause of meaning per variable — density and pH separate styles, sulfur dioxide reflects "
                "preservation, alcohol shapes body — and then the argument that matters: this is not a side effect of "
                "the classifier, because the surrogate reproduces the partition from the original variables. End on "
                "Definition 1.1: every driver is something a wine maker can change.",
         "time": "≈ 26 s", "cue": "Point at Fig. 5.2 and say “the same features, different weights per cluster” — that is the cluster-level claim in one clause."},
        {"n": "34", "title": "Answer to RQ1",
         "screen": "ANSWER TO RQ1 box, then the objective/status/evidence table with three “Met” rows.",
         "how": "Say “Yes”, then the condition: given a high-fidelity surrogate, Shapley values explain a black-box "
                "partition faithfully at both cluster and instance level, in the original feature space. Read the "
                "evidence column once. For O3, use the corrected wording: four axioms; the LIME comparator is discussed "
                "theoretically in Chapter 5, §5.4.",
         "time": "≈ 19 s", "cue": "Never say “we benchmarked SHAP against LIME on the wine data”. The thesis says the comparison is theoretical; that is the third of the three never-say items."},
        {"n": "35", "title": "Key Findings",
         "screen": "Four numbered findings: two-level explanation, attribution in the chemistry, interpretability over geometry, cooperative concept as the guarantor.",
         "how": "Read the four titles, then one clause of evidence each. These are the sentences the jury may write in "
                "their report, so keep the wording stable across rehearsals. Do not add new claims here; this slide is "
                "a summary and juries notice inflation in summaries.",
         "time": "≈ 22 s", "cue": "Finding 3 (k = 3 over k = 2) will be probed; it is a deliberate methodological choice, not an oversight."},
        {"n": "36", "title": "Limitations",
         "screen": "Four boxes: surrogate dependence, tabular only, single level, smoothing.",
         "how": "Volunteer all four without hedging, then say which one matters for what follows: “single level”. That "
                "sentence is the bridge to section 5, and it converts a limitation into the logic of the thesis.",
         "time": "≈ 31 s", "cue": "Do not soften “surrogate dependence” into “approximation”; the honest form is also the stronger form."},
        {"n": "37", "title": "Takeaway: Contribution I",
         "screen": "Three cards (single lens, original space, but…) and the takeaway box plus the forward arrow to Contribution II.",
         "how": "One sentence: Shapley attribution is a well-founded lens for an unsupervised partition, and keeping it "
                "in the original feature space is what makes it actionable. Then the pivot: real data are rarely "
                "single-level; broad groups contain nested sub-groups. Pause and move.",
         "time": "≈ 20 s", "cue": "The pivot sentence is the load-bearing transition of the thesis. Rehearse it."},
    ],
    "extra": [
        ("If the jury interrupts during section 4",
         "The two interruptions to expect are “why a surrogate?” and “why k = 3?”. Both are answered without leaving "
         "the section: the surrogate is the only way to obtain exact tree attribution in the original variables, and "
         "k = 3 is chosen for interpretability with the geometric cost stated openly. Answer in two sentences, point at "
         "the slide, and continue. Do not open the LIME comparison unless asked — it is theoretical in this thesis."),
    ],
    "transition": "“The single-level limit is the one that opens the next question: does this logic survive scale and hierarchy?”",
}


S5 = {
    "id": "contribution-ii",
    "kicker": "Section 5 · slides 38-50 · 4.9 min",
    "title": "Contribution II: multi-level XAI at large scale",
    "range": "38-50",
    "words": "631",
    "m130": "4.9",
    "m120": "5.3",
    "search": "contribution II multi-level hierarchical clustering Beijing proposition 6.1 cross-level aggregation regime weather temperature dew point pressure",
    "purpose": """
- Extend the C1 pipeline from a flat partition to a nested one, without letting the extension look like “the same thing run twice”.
- Deliver Proposition 6.1 as the formal backbone: parent importance equals the size-weighted expectation over children plus a residual, which vanishes under perfect fidelity.
- Show that scale and hierarchy together are survivable: 383,585 records, three physically readable atmospheric regimes, and a sensitivity check on the parameters that could have produced the result by accident.
""",
    "arc": [
        ("Proposition 6.1 is an accounting identity, not a theorem of nature", "Deliver it exactly that way. It says "
         "the parent story is an expectation over the child stories, up to a residual induced by surrogate "
         "approximation; it does not say explanations are identical across levels. The second half of that sentence is "
         "what makes slide 46 work, so say it twice."),
        ("The Beijing result is a domain result, not a number", "Temperature, dew point and pressure lead; CO, NO2, "
         "PM10 and PM2.5 follow; inside clusters the pollutants or wind speed take over. The claim that matters is "
         "interpretive: meteorology sets the regime, pollution varies within it. If you only say “Silhouette 0.63”, the "
         "section collapses into benchmarking."),
    ],
    "slides": [
        {"n": "38", "title": "Contribution II divider",
         "screen": "Section 05 with objectives, methodology and results cards.",
         "how": "One sentence: extend Shapley explanation from single-level to large-scale multi-level clustering. Say "
                "the time-check cue: about minute twenty. Name the two new things the jury should watch for — a real "
                "multi-level workflow and a formal consistency argument.",
         "time": "≈ 18 s", "cue": "Cue 5. Arrival ≈ 19.1 min."},
        {"n": "39", "title": "Research Gap",
         "screen": "Four gap bullets and the orange box: no multi-level explanation method that is both feasible and provably consistent.",
         "how": "Frame the gap as a conjunction: readable within a cluster, across sub-clusters and across levels; and "
                "feasible on 383,585 records, where coalition-by-coalition explanation is impossible. Then the key "
                "missing link: existing hierarchical work reports structure but never relates a parent explanation to "
                "its children.",
         "time": "≈ 24 s", "cue": "The word “provably” is doing real work here. Do not let it drift into “practically consistent” — the proposition is the claim."},
        {"n": "40", "title": "RQ2 and Objectives",
         "screen": "RQ2 strip plus three objective rows: multi-level workflow, formal consistency argument, validation at scale on new data.",
         "how": "Three objectives, three sentences. Point at the “where it is shown” column: the workflow figure, "
                "Proposition 6.1, and Table 6.1 with Figures 6.1 and 6.2. This mapping is what lets you say “yes, "
                "within bounds” later on slide 47.",
         "time": "≈ 23 s", "cue": "Note the phrasing “within bounds” on slide 47. It is deliberate and it protects you in questions D1-D3."},
        {"n": "41", "title": "Multi-Level Workflow with Cross-Level Aggregation",
         "screen": "Five workflow bullets, the level-1 diagram with regime A/B/C and sub-clusters, and the Proposition 6.1 banner.",
         "how": "Explain the recursion: coarse clustering on the full data, then each coarse cluster subdivided where "
                "appropriate; a surrogate per level; SHAP always in the same eleven variables; aggregation that "
                "respects size and nesting rather than averaging. Then the honest note that raises your credibility: "
                "the hierarchy is a practical analysis tool, not a claim that nature is organised this way.",
         "time": "≈ 26 s", "cue": "Say “where appropriate”, not “every cluster is split”. And never say “nine sub-clusters” — no source gives that count."},
        {"n": "42", "title": "Proposition 6.1: Cross-Level Consistency",
         "screen": "The proposition with the size-weighted sum, the two definition strips (expected absolute importance; relative child size), three explanation bullets, the why-it-matters block and two KPI tiles.",
         "how": "Read the formula as a sentence: expected absolute importance of a feature at a parent level equals the "
                "size-weighted expectation over its children, plus a residual from surrogate mismatch. Then the three "
                "qualifiers: the residual vanishes under perfect fidelity; the derivation uses the law of total "
                "expectation because children partition the parent; and the result does not make levels identical, it "
                "makes their differences interpretable. Finally, why it matters: parent importance is an accounting "
                "identity over children, not a separate story.",
         "time": "≈ 27 s", "cue": "If asked for the proof, go to question D6 and quote the unanimity-game argument from Appendix A.1 and the partitioning argument in A.2 — and admit that ε is conceptual, not estimated."},
        {"n": "43", "title": "Evaluation Protocol",
         "screen": "Eight-row protocol table, then four success criteria (separation, physical reading, interpretable differences, stability under sensitivity).",
         "how": "Say what changed relative to Contribution I: clustering runs on the full Beijing dataset, and each "
                "level gets its own surrogate. Name the sensitivity check explicitly, because it is the defence "
                "against “your result is a parameter artefact”. Twenty seconds, no more.",
         "time": "≈ 23 s", "cue": "Sensitivity on k, projection dimension and tree depth is what question D7 will probe."},
        {"n": "44", "title": "Coarse-Level Clustering: Beijing Air Quality",
         "screen": "Three KPI tiles (k = 3 with all criteria agreeing; Silhouette ≈ 0.63; Davies-Bouldin ≈ 0.55), setup and sensitivity blocks, Gramegna and Giudici 0.37 comparison.",
         "how": "Give the two metrics, then immediately the context that stops the number floating: 0.63 is much stronger "
                "than the wine partition's 0.144 and clearly better than the 0.37 reported in the SHAP-clustering "
                "credit-risk study — but that comparison is a positioning point, not a like-for-like benchmark. Say "
                "that distinction yourself.",
         "time": "≈ 20 s", "cue": "Never let “0.63” be attached to wine in your speech. The thesis repeats the correction twice on purpose."},
        {"n": "45", "title": "Global SHAP Ranking: Weather Variables Are Central",
         "screen": "Reading bullets plus Fig. 6.1 (global importance at coarse level).",
         "how": "Lead with the finding, not the figure: temperature, dew point and pressure come first; CO, NO2, PM10 "
                "and PM2.5 follow — meteorology conditions dispersion, trapping and photochemistry, so the explanation "
                "reveals that pollution regimes are not decided by pollutant concentrations alone. This is the sentence "
                "that makes a domain expert in the room nod.",
         "time": "≈ 22 s", "cue": "Be ready for “isn't that obvious to an air-quality scientist?” — answer with question D9."},
        {"n": "46", "title": "How Importance Changes Across Levels",
         "screen": "Fig. 6.3 (cluster-specific importance), two blocks — coarse level: regime selection; within clusters: variation inside a regime — and the reconciliation paragraph.",
         "how": "This is the slide that justifies the whole multi-level machinery. Say the two readings: at the coarse "
                "level temperature and dew point dominate because they separate broad atmospheric regimes; inside a "
                "cluster, CO, SO2, PM10, wind speed, pressure or ozone become more informative. Then the reconciliation: "
                "this is not a contradiction; a variable can be globally important and locally uninformative, and "
                "Proposition 6.1 makes the two readings agree up to the surrogate residual.",
         "time": "≈ 29 s", "cue": "Do not over-claim Fig. 6.3 as a level-2 analysis; the thesis figure shows cluster-specific panels at the coarse level."},
        {"n": "47", "title": "Answer to RQ2",
         "screen": "ANSWER TO RQ2 box: “Yes, within bounds…”, plus the three-row objective table.",
         "how": "Say the answer with its boundary in the same breath: yes, consistency is kept at scale and across "
                "levels, through a nested workflow with level-specific surrogates and Proposition 6.1, explaining "
                "383,585 records in the original variable space. Then the honest closing clause the notes already "
                "carry: attribution is still post-hoc.",
         "time": "≈ 22 s", "cue": "“Within bounds” is the strongest form of the claim the thesis supports. Do not upgrade it to “proved in general”."},
        {"n": "48", "title": "Key Findings",
         "screen": "Four numbered findings: weather defines structure; importance legitimately changes with level; the explanation scales; the logic transfers across domains.",
         "how": "Four titles, four evidence clauses. Finding 4 is the transplant argument: the same pipeline and the same "
                "reading, from 4,898 wines to 383,585 hourly air-quality records. Do not mention the 0.37 comparison "
                "again unless asked.",
         "time": "≈ 17 s", "cue": "Finding 3's phrase “linear in the data, not exponential in the features” is a good line to have ready for question D10."},
        {"n": "49", "title": "Limitations",
         "screen": "Four boxes: static clustering, smoothing, tabular only, post-hoc.",
         "how": "Volunteer all four, then make the last one the hinge: attribution still explains a partition that was "
                "already computed, and does not influence learning. That is precisely the question Contribution III "
                "takes on. Say it as a design decision, not as a confession.",
         "time": "≈ 25 s", "cue": "The temporal point is sharp: Beijing data are hourly time series but the partition is static. Say “drift between years is not modelled” exactly."},
        {"n": "50", "title": "Takeaway: Contribution II",
         "screen": "Three cards — consistent, against scale, still post-hoc — plus the takeaway box and the arrow to Contribution III.",
         "how": "One sentence: Shapley attribution stays consistent across levels of detail when the hierarchy is "
                "explicit, so explanations become interpretable against scale, not just against one flat partition. "
                "Then the pivot: the pipeline is still static, and preferences change over time.",
         "time": "≈ 18 s", "cue": "The pivot sentence introduces Contribution III; deliver it as a question, not a summary."},
    ],
    "extra": [
        ("The two sentences that carry section 5",
         "“The parent story is regime selection; the child story is variation within a regime, and Proposition 6.1 "
         "makes those differences interpretable rather than contradictory.” · “It does not say explanations are "
         "identical across levels; it says the differences can be interpreted.” If you remember only two lines from "
         "this section, remember those."),
        ("What to do if someone asks for the residual ε",
         "Say three things: it is induced by surrogate approximation; it vanishes under perfect fidelity; and in this "
         "thesis it is treated as a conceptual residual rather than an empirically estimated quantity, because a "
         "separate Beijing-level residual analysis is not reported. That answer is both accurate and impressive, "
         "because it shows you know exactly where your own formal result stops."),
    ],
    "transition": "“So explanation scales and stays consistent, but it is still post-hoc. In the third contribution I ask the question the thesis was built on: can attribution change how the model learns?”",
}


S6 = {
    "id": "contribution-iii",
    "kicker": "Section 6 · slides 51-66 · 7.5 min",
    "title": "Contribution III: DyHuCoG, attribution as an in-training signal",
    "range": "51-66",
    "words": "971",
    "m130": "7.5",
    "m120": "8.1",
    "search": "contribution III DyHuCoG hypergraph cooperative game monte carlo shapley in-training ablation results movielens amazon significance efficiency cold start",
    "purpose": """
- Show the conceptual leap: the same cooperative game that explained a partition now defines the value that the recommender optimises while it trains.
- Carry the jury through five technical objects in order — player set, coalition utility, preference-aware Monte Carlo estimation, dynamic hyperedge weights, composite loss — without losing the thread that each one is still Shapley.
- Deliver the empirical package honestly: gains on both datasets, the component-wise ablation, the convergence table, the paired tests on MovieLens-1M and the descriptive status of Amazon-Book.
""",
    "arc": [
        ("The section is a pipeline, so present it as one", "Slide 54 defines the game, 55 estimates it, 56 injects it "
         "into message passing. Each slide is the output of the previous one. If you say “the estimator from the "
         "previous slide becomes the edge weight here”, the jury never has to reconstruct the chain."),
        ("Numbers are the easy part; scope is the hard part", "The results are strong and the deck reports them well. "
         "The risk is overshooting: significance is tabulated on MovieLens-1M only, the ablation is component-wise "
         "rather than factorial, and the baselines were frozen in early 2026. Say those three boundaries yourself, "
         "early, and the results become more credible rather than less."),
        ("Two figures, two minutes", "Fig. 7.1 (architecture) on slide 56 and Fig. 7.2/7.3 (results and diversity) are "
         "worth pointing at rather than narrating. Let the jury read them; your voice should say what the figure proves."),
    ],
    "slides": [
        {"n": "51", "title": "Contribution III divider",
         "screen": "Section 06 with objectives, methodology and results, including the name DyHuCoG spelled out.",
         "how": "Name it and expand it: Dynamic Hypergraph Cooperative Game. Frame the transition in one sentence: in "
                "the first two contributions Shapley values explained models after training; here the question is "
                "whether attribution can become part of the learning process. Say the time-check cue: about minute "
                "twenty-six.",
         "time": "≈ 26 s", "cue": "Cue 6. Arrival ≈ 23.9 min, so the cue is conservative by about two minutes — that slack is your protection for section 6, the longest one."},
        {"n": "52", "title": "Research Gap",
         "screen": "Four gap bullets and the orange box: no recommender decides during training how much each user, item and context should count, while keeping accuracy, context and diversity in one objective.",
         "how": "Three problems, one gap. Problem one: hypergraph recommenders treat message importance as uniform or "
                "attention-weighted, with no marginal-contribution account. Problem two: diversity is often a "
                "re-ranking heuristic applied after training. Problem three: interpretability is added after "
                "prediction. Then the pivot from your own work: C1 and C2 showed Shapley attribution is faithful and "
                "consistent, but it never changed what the model learned.",
         "time": "≈ 24 s", "cue": "The word “during training” is the whole novelty claim. Say it explicitly; it is what separates DyHuCoG from attention mechanisms."},
        {"n": "53", "title": "RQ3, RQ4 and Objectives",
         "screen": "Two RQ strips and a three-row objective table (game formulation, Shapley inside message passing, accuracy + coverage + diversity together).",
         "how": "Two questions, three objectives. First objective: model recommendation as a cooperative game over "
                "users, items and contexts, with a utility that mixes accuracy, diversity and context. Second: put "
                "preference-aware Monte Carlo Shapley inside message passing as dynamic hyperedge weights. Third: show "
                "ranking, coverage and diversity improving together on two datasets, with the evidence in Table 7.1.",
         "time": "≈ 38 s", "cue": "The note states these objectives once; earlier versions repeated them twice on the same slide. Keep it single."},
        {"n": "54", "title": "Recommendation as a Cooperative Game",
         "screen": "Player set N = U ∪ I ∪ C, the hypergraph H = (V, E, W) with dynamic weights, coalition definition, and the preference term.",
         "how": "Define the three objects in order: players are users, items and contexts; a coalition is the set of "
                "entities taking part in one recommendation episode; the value of a coalition is the quality of the "
                "recommendation it can achieve. Then the preference-aware extension with λpref = 0.20 and the reason "
                "the design is elegant: the trade-off the recommender must satisfy is exactly the trade-off from which "
                "attribution is computed, so explanatory game and predictive objective are aligned by design.",
         "time": "≈ 28 s", "cue": "If asked about the size of the player set, use question E4: the estimator is scoped to the local episode, so a coalition is on the order of a few dozen entities, not the whole catalogue."},
        {"n": "55", "title": "Preference-Aware Monte Carlo Shapley",
         "screen": "Why exact Shapley is infeasible, the unbiased estimator with variance σ²/M, the convergence table (M = 25 → 5.6e-5 / 98 %, M = 50 → 1.4e-5 / 99 %, M = 100 → 3.5e-6 / 99.5 %), the training-loop steps and the per-epoch cost.",
         "how": "Explain the sampling idea in one sentence: instead of summing over all 2^N coalitions, sample M "
                "permutations and average the marginal contributions, which keeps the estimator unbiased and reduces "
                "its variance as σ²/M. Then the choice: M = 50 gives MSE 1.4×10⁻⁵ and about 99 % accuracy against a "
                "high-sample reference, while M = 100 buys a modest improvement for 2.5× the cost — diminishing "
                "returns. Say the two operational details: refresh every 10 batches, about 49 updates per epoch, and "
                "smoothing by exponential moving average.",
         "time": "≈ 39 s", "cue": "Accuracy here is measured against a high-sample reference, not against exact Shapley values. Say that phrase yourself — it is the correction v26 made for a reason."},
        {"n": "56", "title": "Shapley-Weighted Hypergraph Message Passing",
         "screen": "Fig. 7.1 (architecture), the Shapley-weighted block, the attention gate, the context-aware score and the composite loss line.",
         "how": "Narrate the pipeline from left to right in four sentences: information propagates through hypergraph "
                "message passing; Shapley estimates, clipped and smoothed, set the edge weights; an attention gate "
                "stabilises early training when those estimates are still noisy; the objective combines ranking, "
                "diversity, context and regularisation. Then the sentence that explains why the read-out is faithful: "
                "the explanation reports the same terms the loss optimises.",
         "time": "≈ 32 s", "cue": "Distinguish the two mechanisms clearly: Shapley weights act before propagation, the attention gate reweights the propagated signal. Confusing them is the classic error here (question E9)."},
        {"n": "57", "title": "Evaluation Protocol",
         "screen": "Eight-row protocol table (datasets, split, baselines, metrics, repeats, statistics, ablation) and four success criteria.",
         "how": "Protocol slide, keep it tight: two datasets — MovieLens-1M dense, Amazon-Book sparse, Yelp2018 as an "
                "auxiliary check; user-level time-ordered 70/10/20 with a leave-one-out target; six baselines; four "
                "metrics with NDCG@20 as the main one; five seeds; paired tests with Holm correction; component-wise "
                "ablation. Then the success criteria in one breath, with the scope already attached: significance is "
                "tabulated on MovieLens-1M.",
         "time": "≈ 31 s", "cue": "This slide replaced a misaligned note in v26. If you feel short of time, it is a good slide to speed up — but do not skip the scope clause."},
        {"n": "58", "title": "Main Results on MovieLens-1M",
         "screen": "Four reading bullets, two KPI tiles (+9.8 % / +12.6 %), the seven-row table with DyHuCoG in bold.",
         "how": "Give the two headline numbers against HPCF — NDCG@20 0.2775 versus 0.2528, Recall@20 0.2362 versus "
                "0.2098 — then the diversity story, which is the distinguishing claim: coverage 0.397 versus 0.342 and "
                "ILD 0.516 versus 0.461 rise at the same time as accuracy. Close with the ordering argument: the gap "
                "widens from classical to graph to hypergraph models, and DyHuCoG adds another step on top of the "
                "strongest. Point at the bold row; do not read the table.",
         "time": "≈ 30 s", "cue": "The percentages as spoken: +9.8 % NDCG, +12.6 % Recall (the thesis tabulates +9.77 % and +12.58 %)."},
        {"n": "59", "title": "Main Results on Amazon-Book",
         "screen": "Same structure on the sparse dataset: +13.3 % / +16.2 % KPI tiles, the seven-row table.",
         "how": "Same rhythm, bigger numbers, plus the honest framing: absolute values are low for every model because "
                "the matrix is almost empty, so what matters is the consistent ordering and the widening gap where "
                "data are weakest. Say “descriptive gain” here — the paired tests are tabulated on MovieLens-1M.",
         "time": "≈ 22 s", "cue": "Never say Amazon-Book is statistically significant. The thesis calls it descriptive; slide 77 says the same."},
        {"n": "60", "title": "Ablation: Every Component Contributes",
         "screen": "Two ablation tables (MovieLens-1M and Amazon-Book) and the reading bullets: context −8.2 % / −11.0 %, hypergraph −6.8 % / −8.9 %, Shapley −4.6 % / −6.1 %, diversity −5.8 % / −5.8 %, attention −3.5 % / −3.5 %.",
         "how": "Read the ranking, then the two conclusions: context is the largest single component, so contextual "
                "signals are the substrate; and removing Shapley weighting costs more on the sparser dataset (6.1 % "
                "versus 4.6 %), which is exactly the robustness argument of the thesis. Then the boundary: the ablation "
                "removes one component at a time; it does not test combinations.",
         "time": "≈ 27 s", "cue": "This is the slide that answers “is the gain from Shapley or from the extra components?” — question E6. Own it."},
        {"n": "61", "title": "Efficiency and Shapley Convergence",
         "screen": "Four KPI tiles (1.78× training time, 1.84 ms inference, 4.4 GB memory, M = 50), plus complexity and convergence blocks.",
         "how": "Lead with the trade: training about 1.78 times HPCF — roughly 2,000 seconds versus 1,125 on "
                "MovieLens-1M — while inference stays at 1.84 ms per query, which is real-time. Say that the overhead is "
                "bounded by the refresh period (every 10 batches) and that the convergence table on the backup slide "
                "shows the knee at M = 50. Do not defend the cost; quantify and bound it.",
         "time": "≈ 26 s", "cue": "Amazon-Book: 9,279 s, 8.52 ms, 17.9 GB. Have those three numbers ready; the backup slide 79 has the full table."},
        {"n": "62", "title": "Statistical Significance",
         "screen": "Four indicator boxes (paired t-test with df = 6,039, Cohen's dz, Holm-Bonferroni, Table 7.6) and the protocol block.",
         "how": "Explain the design in two sentences: per-user NDCG@20 for 6,040 users, paired tests against every "
                "baseline, Holm-Bonferroni to control the family-wise error over six comparisons, and Wilcoxon as a "
                "distribution-free check. Then the result: DyHuCoG versus HPCF gives t = 46.38, p = 1.81×10⁻²⁷⁰, "
                "dz = 1.33 — significant after correction, with a large effect size. Say the phrase “large effect size, "
                "not only a small p-value”; it shows you know the difference.",
         "time": "≈ 27 s", "cue": "The scope fence: these tests are MovieLens-1M only. The full table is backup slide 78."},
        {"n": "63", "title": "Answers to RQ3 and RQ4",
         "screen": "Two answer boxes and the three-row objective table with evidence.",
         "how": "Answer RQ3 first: yes, attribution becomes an in-training signal, because Shapley estimates set the "
                "hyperedge weights while the model learns. Then RQ4: yes, ranking, coverage and diversity improve "
                "together on both datasets, with the largest gains where data are sparsest. Then the evidence column, "
                "briefly. Close with the sentence from the notes: attribution becomes not only an explanation "
                "mechanism, but a learning mechanism.",
         "time": "≈ 23 s", "cue": "O2's evidence includes “−4.6 % / −6.1 % without it”. Those numbers are the ablation, not the main gain; do not mix them up under pressure."},
        {"n": "64", "title": "Key Findings",
         "screen": "Four numbered findings: the trade-off is not fixed by nature; gains are largest where data are weakest; context and structure carry the most weight; the improvement is statistically solid and affordable.",
         "how": "Four titles with one evidence clause each. Finding 2 is the one to stress: +13.3 % on Amazon-Book "
                "versus +9.8 % on MovieLens-1M, and cold-start gains of +10.9 % for cold users and +9.6 % for cold "
                "items. Finding 4 carries the statistics and the cost together, which is how an engineering jury will "
                "remember the contribution.",
         "time": "≈ 31 s", "cue": "Cold-start figures 0.061 vs 0.055 and 0.057 vs 0.052 are the rounded-table values; the paper's prose computes +9.8 % for both from unrounded values. Give the deck's numbers."},
        {"n": "65", "title": "Limitations",
         "screen": "Four boxes: compute overhead, needs meaningful context, Monte Carlo variance, scope of the claim.",
         "how": "Four sentences, no hedging: about 1.78× the training time of HPCF; the largest component is context so "
                "the gain shrinks without usable context; M = 50 leaves variance that better sampling could reduce; and "
                "the ablation is component-wise with baselines frozen in early 2026, so superiority is claimed only "
                "against the tested set. Then close on the line that keeps the section whole: none of these change the "
                "main message, that attribution can guide learning and not only describe it.",
         "time": "≈ 28 s", "cue": "Also true and worth volunteering if asked: no post-2024 LLM-augmented recommenders, no public code or per-seed logs (Appendix D)."},
        {"n": "66", "title": "Takeaway: Contribution III",
         "screen": "Three cards (first-class, read-out, axiomatic) and the takeaway box plus the closing arrow.",
         "how": "One sentence: attribution becomes a first-class part of the learning objective, so the explanation is a "
                "direct read-out of what the model optimises and is faithful by design rather than an outside "
                "approximation. Then the arc of the whole thesis in one line: from post-hoc description in C1 and C2 to "
                "in-training guidance in C3. Pause before moving to the conclusion.",
         "time": "≈ 18 s", "cue": "“Faithful by design” is a strong phrase. Keep it for the takeaway and do not spend it earlier in the section."},
    ],
    "extra": [
        ("The five sentences that make section 6 defensible",
         "1. “The players are users, items and contexts, and the value of a coalition is the quality of the "
         "recommendation it can achieve.” 2. “Exact Shapley is exponential, so we sample M permutations and average "
         "marginal contributions, which stays unbiased and shrinks variance as σ²/M.” 3. “Those estimates become the "
         "hyperedge weights, so attribution is computed with the same trade-off the model is trained on.” 4. “Removing "
         "that weighting costs 4.6 % on MovieLens-1M and 6.1 % on Amazon-Book, more where data are sparser.” 5. “The "
         "paired tests are tabulated on MovieLens-1M; Amazon-Book is reported as a descriptive gain.”"),
        ("If the jury asks the hardest question of the section",
         "“Isn't this just attention with a different name?” Answer: attention learns importance implicitly from the "
         "loss and carries no allocation guarantee; here importance is a Shapley value of an explicit coalition "
         "utility, so it satisfies efficiency, symmetry, null-player and additivity, and it is computed from the same "
         "three objectives the model is trained on. Then add the empirical control: the ablation removes the "
         "hypergraph, the attention, the context, the diversity and the Shapley weighting separately, and the Shapley "
         "row has its own measurable cost. That is question E2."),
    ],
    "transition": "“That is the last contribution. Let me bring the three together, state the limitations honestly, and give the answer to the thesis question.”",
}


S7 = {
    "id": "conclusion",
    "kicker": "Section 7 · slides 67-76 · 3.9 min",
    "title": "Conclusion &amp; Perspectives: synthesis, publications, limits, answer",
    "range": "67-76",
    "words": "501",
    "m130": "3.9",
    "m120": "4.2",
    "search": "conclusion synthesis publications limitations perspectives references thank you thesis answer",
    "purpose": """
- Compress the whole thesis into three sentences the jury can repeat, then show that the work has a public record (three first-author papers) and a stated edge (limitations).
- Turn the limitations into an agenda, so the jury hears a researcher with a programme rather than a student defending a product.
- Land the thesis answer on slide 72, then hand the floor over cleanly on slides 75 and 76.
""",
    "arc": [
        ("Delivery register changes here", "Sections 1-6 are exposition with a downward gaze at tables. Section 7 is "
         "the only part where you address the jury as readers of a whole: slower, fewer numbers, more first person, "
         "pauses after the two big boxes. Section 7 has its own detailed plan in the next tab."),
        ("The last spoken sentence is the closing box, not the thanks", "Slide 72's orange box is the answer. Slide 75 "
         "is a courtesy. If you reverse that order you end the scientific part of the viva with “thank you” instead of "
         "with the claim — and the jury's notes will remember the order in which they heard things."),
    ],
    "slides": [
        {"n": "67", "title": "Conclusion divider",
         "screen": "Section 07 with three cards: synthesis, limitations, perspectives.",
         "how": "Take a breath and reset the pace. Announce the five beats you will cover: synthesis, publications, "
                "limitations, perspectives, thesis answer. Say the time-check cue: about minute thirty-four.",
         "time": "≈ 16 s", "cue": "Cue 7. Measured arrival ≈ 31.4 min, so you should still have about 2.5 minutes of buffer; the cue is your alarm, not your deadline."},
        {"n": "68", "title": "Synthesis of the Three Contributions",
         "screen": "A three-row synthesis table (main idea, achievement, key finding), three verbs on the right — explain, scale, guide — and the thesis takeaway box.",
         "how": "Read the three rows as three sentences, then the three verbs as the arc: C1 explains, C2 scales, C3 "
                "guides. Then the takeaway: one cooperative-game definition, three value functions — a partition's "
                "Silhouette, a hierarchy of clusters, a recommender's coalition utility — and the same Shapley logic "
                "throughout. Point at the arrows on the right while you say the three verbs; it photographs well.",
         "time": "≈ 27 s", "cue": "This is the single most useful slide to leave on screen during a long answer. It is also backup slide material if a jury member asks “what is the thesis in one slide?”"},
        {"n": "69", "title": "Publications Supporting the Thesis",
         "screen": "Three-row table with authors, titles, journals, years, DOIs and status, plus the mapping to chapters and the related work with the team.",
         "how": "Name the mapping only: paper one to Contribution I, Chapter 5; paper two to Contribution II, Chapter "
                "6; paper three to Contribution III, Chapter 7. Say that you are first author on all three. One sentence "
                "for the team's related work if you wish, but do not dwell: the jury cares about your own record.",
         "time": "≈ 18 s", "cue": "Have the DOIs in memory: 10.1016/j.procs.2023.03.107, 10.14569/IJACSA.2025.0160780, 10.22266/ijies2026.0228.54."},
        {"n": "70", "title": "Limitations, Stated Honestly",
         "screen": "Four blocks: computational, methodological, empirical, claim scope.",
         "how": "Say all four plainly, then stop. The most valuable clause is the claim-scope one: this is a consistent "
                "and productive shared view, not one fully unified framework that removes all tension. Saying that "
                "yourself disarms the most damaging version of the question “is this really one framework?”",
         "time": "≈ 26 s", "cue": "Do not apologise, and do not add limitations that are not on the slide; a jury will write down every one you volunteer and check whether the thesis supports it."},
        {"n": "71", "title": "Perspectives: Turning Limitations into an Agenda",
         "screen": "Four numbered directions: scalable cooperative attribution, online and streaming recommendation, richer user-centred evaluation, broader trustworthy-AI evaluation.",
         "how": "Present them as a research programme, not as a wish list. For each one, link it back to a limitation you "
                "just stated: lower-variance estimators address the Monte Carlo variance and the cost; streaming "
                "addresses the static graph; user-centred evaluation addresses the fact that actionability was never "
                "measured; trustworthy-AI evaluation extends the governance framing of the introduction.",
         "time": "≈ 30 s", "cue": "The second direction is the one to advertise if you are applying for a postdoc: it is a full research agenda, not a patch."},
        {"n": "72", "title": "Conclusion",
         "screen": "THESIS ANSWER box, then four KEY OUTCOMES cards (common language, three achievements, explanation as method, trustworthy AI).",
         "how": "This is the landing. Read the answer box once, slowly: cooperative game theory can serve as a shared "
                "methodological view for actionable explanation across clustering and recommendation — the same Shapley "
                "logic explains, stays consistent across levels, and guides learning. Then the four outcomes in one "
                "clause each, and end on the closing line the notes carry: “Explanation does not have to remain a "
                "description of what happened; it can help us understand, control and improve AI systems.” Then stop "
                "talking.",
         "time": "≈ 43 s", "cue": "This is the last thing the jury should hear before you leave the science. Rehearse the final sentence until you can say it without looking at the slide."},
        {"n": "73", "title": "References (1 / 2)",
         "screen": "Entries [1] to [14]: your three papers, Shapley 1953, SHAP, TreeSHAP, LIME, Monte Carlo Shapley, matrix factorisation, NCF, LightGCN, HCCF, HPCF.",
         "how": "Ten seconds, no more: “the first of the two reference slides lists the foundations: my own three papers, "
                "the Shapley and SHAP literature, and the recommender baselines from matrix factorisation to HPCF.” Do "
                "not read entries.",
         "time": "≈ 18 s", "cue": "If a jury member asks for a specific reference, use these two slides rather than guessing a year."},
        {"n": "74", "title": "References (2 / 2)",
         "screen": "Entries [15] to [28]: RecDCL, hypergraph neural networks, Silhouette, SHAP/LIME in credit risk, the datasets, the XAI surveys, HPCF, Holm and Cohen, and the team's IJIES paper.",
         "how": "Same treatment: name the families (datasets, metrics, regulation, related work), then move on. Five to "
                "ten seconds.",
         "time": "≈ 14 s", "cue": "This slide is where you would point if asked about Holm-Bonferroni or Cohen's dz: references [27]."},
        {"n": "75", "title": "Thank You",
         "screen": "A thank-you statement, a large question mark, and the candidate, supervisor, laboratory and defence place cards.",
         "how": "Thank the jury for their attention and say you are glad to take questions on methodology, theory or "
                "results. Do not summarise again. This slide lasts about fifteen seconds and then you stop.",
         "time": "≈ 16 s", "cue": "Say explicitly that you will stay on the closing slide: it tells the jury you intend to answer from the title slide with the jury table, which is the professional move."},
        {"n": "76", "title": "Closing title (Q&amp;A)",
         "screen": "The title slide again with the jury table and “Questions &amp; Discussion · Thank you”.",
         "how": "Leave this on screen for the whole discussion. It flatters the jury by keeping their names visible, "
                "and it gives you a neutral backdrop while you think. Nothing is spoken on this slide beyond the thanks "
                "already given.",
         "time": "—", "cue": "Pre-defence check repeated here: the jury list must be confirmed against the official convocation before the defence."},
    ],
    "extra": [
        ("Three things that change the room in section 7",
         "First, slow down by about 10 percent and look up more. Second, use the pause: after the answer box on slide "
         "72, let two full seconds pass before the outcomes. Third, do not add new evidence in the conclusion; if a "
         "thought is not in the three contributions, it belongs in the discussion, not in the closing."),
    ],
    "transition": "“Thank you. I am ready for your questions.”",
}


SQ = {
    "id": "discussion",
    "kicker": "Discussion stage · slides 75-79 · not spoken",
    "title": "The Q&amp;A stage and the three backup slides",
    "range": "75-79",
    "words": "45 (notes only)",
    "m130": "—",
    "m120": "—",
    "search": "questions discussion backup tables significance standard deviation runtime memory Monte Carlo convergence",
    "purpose": """
- Turn the discussion from a threat into a demonstration: the deck already contains the tables a jury normally has to ask for.
- Keep three instruments loaded — stability, significance, cost — and know exactly which slide answers which class of question.
- Leave the closing title slide up for the whole discussion so the jury sees their own names while they question you.
""",
    "arc": [
        ("You are allowed to say “let me show you”", "Slides 77-79 exist precisely so that answers can be evidence "
         "rather than memory. When a question touches stability, go to 77; significance, go to 78; cost or convergence, "
         "go to 79. Announcing the slide number is a professional move, not a stall."),
        ("Thirty seconds of silence is not a failure", "Aim to answer in three beats: the direct answer, the evidence, "
         "and the boundary. If you do not know, say what you do know and name where the thesis stops. Never invent a "
         "number, and never guess a citation."),
    ],
    "slides": [
        {"n": "77", "title": "Backup: Table 7.1 with standard deviations",
         "screen": "Both datasets, all seven models, mean ± standard deviation over five seeds, plus the honest note about overlapping bands on Amazon-Book.",
         "how": "Use it when asked about run-to-run stability. Say that the ±1σ bands never overlap between DyHuCoG and "
                "HPCF on MovieLens-1M, and that on Amazon-Book the standard deviations are close to the gap for "
                "NDCG@20 and Recall@20 — which is exactly why those gains are reported as descriptive rather than "
                "significant. Offering that limitation before it is extracted from you is the strongest possible use "
                "of this slide.",
         "time": "as needed", "cue": "Do not claim “every metric is stable”. The corrected wording is the one on the slide."},
        {"n": "78", "title": "Backup: Table 7.6, paired tests",
         "screen": "Six comparisons against DyHuCoG on per-user NDCG@20 with t statistic, p-value, Cohen's dz, the Holm threshold and the result.",
         "how": "Use it when asked about significance. Walk one row to explain the procedure — for example DyHuCoG "
                "versus HPCF, t = 46.38, p = 1.81×10⁻²⁷⁰, dz = 1.33 against a Holm threshold of 0.05 — then say that "
                "all six comparisons are significant and that Wilcoxon agrees at p &lt; 0.001. Mention that the "
                "thresholds differ per row because Holm-Bonferroni orders the p-values.",
         "time": "as needed", "cue": "The df = 6,039 and n = 6,040 belong together: 6,040 users, one degree of freedom consumed by the paired mean."},
        {"n": "79", "title": "Backup: Tables 7.3 and 7.4, cost and convergence",
         "screen": "Runtime, inference latency and memory for all seven models on both datasets, and the Monte Carlo table M = 10, 25, 50, 100 with MSE, accuracy and training cost.",
         "how": "Use it for the cost question, and structure the answer around the knee of the curve: M = 50 costs "
                "1.78× a base hypergraph model in training and about 1.84 ms per query at inference; M = 100 improves "
                "MSE from 1.4×10⁻⁵ to 3.5×10⁻⁶ but costs 2.5×, so 50 is the balance point. Note that the latency, not "
                "the training time, is what a production system would feel.",
         "time": "as needed", "cue": "The Amazon-Book numbers are the ones people forget: 9,279 s training, 8.52 ms inference, 17.9 GB."},
    ],
    "extra": [
        ("Question-to-slide index for the discussion",
         "Stability, variance, seeds, error bars → slide 77. Significance, p-values, effect size, multiple comparisons "
         "→ slide 78. Cost, latency, memory, convergence, why M = 50 → slide 79. Thesis in one slide → slide 68. "
         "Question mapping → slide 15. Method figures → slides 33, 45, 46, 56. Objectives and their status → slides 34, "
         "47, 63. Limitations → slides 36, 49, 65, 70. Perspectives → slide 71."),
        ("The four moves when you do not know the answer",
         "1. Restate the question to buy three seconds and to make sure you answer the right thing. 2. Answer what you "
         "do know, with the scope attached (“what I can tell you from the thesis is…”). 3. Name the boundary precisely "
         "(“that analysis is not reported; it is listed as future work”). 4. Offer the adjacent evidence you do have, "
         "and stop. Do not fill silence with speculation."),
    ],
    "transition": "—",
}


SECTIONS = [S4, S5, S6, S7, SQ]
