# -*- coding: utf-8 -*-
"""100 viva questions with dissertation-level answers — categories A to D (Q001-Q050)."""

GROUPS = [
# ============================================================ A. FRAMING
{
 "title": "A · Framing, scope and contribution",
 "items": [
{
 "q": "In one sentence, what is this thesis?",
 "a": """Shapley attribution is usually presented as a post-hoc explanation tool; this thesis shows that one
 cooperative-game language can do three things with the same formal object. First, explain a black-box unsupervised
 partition faithfully in the original feature space (Contribution I, wine). Second, keep that explanation consistent
 across levels of detail and at scale (Contribution II, 383,585 Beijing records, Proposition 6.1). Third, turn the
 same attribution into an in-training signal, so that explanation becomes part of how a hypergraph recommender
 learns (Contribution III, DyHuCoG, MovieLens-1M and Amazon-Book). The unifying sentence is: one cooperative-game
 definition, three value functions — a partition's Silhouette, a hierarchy of clusters, and a recommender's
 coalition utility — sharing the same Shapley allocation rule.""",
 "tags": ["must know"],
},
{
 "q": "Why is this one thesis and not three papers stapled together?",
 "a": """Because the three contributions are three instantiations of one formal object, and each one removes a
 limitation the next one inherits. Contribution I explains a partition but is single-level and post-hoc. Contribution
 II keeps the explanation but makes it hierarchical, and its own limitation is that it is still post-hoc. Contribution
 III answers exactly that: attribution is computed during training and shapes the model. The invariant across all
 three is the pair (players, value function) plus the Shapley allocation rule; what changes is who the players are
 (features, then features at two levels, then entities of a recommendation episode) and what a coalition is worth
 (Silhouette, then hierarchical Silhouette, then a multi-objective recommendation utility). Slide 68 states it as one
 cooperative-game definition with three value functions, and the thesis claim-scope limitation on slide 70 is
 deliberately worded as "a consistent and productive shared view, not one fully unified framework that removes all
 tension".""",
 "tags": ["must know"],
},
{
 "q": "What is the single most original element of the work?",
 "a": """I would name two, and I would be explicit about which is formal and which is architectural. Formally, the
 most original element is Proposition 6.1: in a strict nested hierarchy on a consistent feature space, parent-level
 expected absolute importance equals the size-weighted expectation over children plus a residual induced by
 surrogate approximation. It is a small result — the core is the law of total expectation — but it converts "the
 explanation changed between levels" from a suspicion into an accounting identity with a named error term.
 Architecturally, the most original element is the DyHuCoG design: using a preference-aware Monte Carlo Shapley
 estimate, computed from the same multi-objective utility the model is trained on, as dynamic hyperedge weights.
 The thesis is careful not to claim either as a general theory: the first is a bounded identity under stated
 conditions, and the second is shown on two benchmarks against a frozen baseline set.""",
 "tags": ["danger"],
},
{
 "q": "You define actionable insight in Definition 1.1. Did you measure actionability?",
 "a": """No, and the thesis says so plainly. Definition 1.1 gives two conditions: the explanation must identify a
 modifiable factor, and it must express that factor in the vocabulary of the domain — acidity in wine, pollution
 indicators in air quality, preference signals in recommendation. Actionability is used in this work as a framing
 concept and an interpretive criterion, illustrated by showing that the wine drivers (density, pH, fixed acidity,
 sulfur dioxide, alcohol) and the air-quality drivers (temperature, dew point, pressure, then CO, NO2, PM10, PM2.5)
 are quantities that a domain practitioner could in principle act on. It was not measured with users, and no user
 study was run. A user-centred evaluation — do explanations measurably improve analyst judgement, trust and
 decisions? — is listed as a research perspective on slide 71 and as a limitation on slide 70.""",
 "tags": ["danger", "must know"],
},
{
 "q": "Is this an XAI thesis or a recommender-systems thesis?",
 "a": """It is an XAI thesis that uses recommendation as its hardest application. The formal contribution is about
 how explanation is defined, computed and — in the third contribution — how it can enter learning. The application
 domain matters because the thesis's second requirement on an explanation is that it speak the domain's language,
 and recommendation is a domain in which the entities (users, items, contexts) have names and the objective
 (relevance, diversity, context) is a stated trade-off rather than a single accuracy number. The empirical work is
 evaluated with the standard apparatus of recommender-systems research — NDCG@20, Recall@20, coverage, intra-list
 diversity, six baselines from four families, HPCF as the strongest reference — exactly so that the claims are
 legible to that community. The two clustering chapters exist because clustering is the clearest test of
 faithfulness, since the model invents its own structure.""",
},
{
 "q": "Why choose recommendation systems as the main application?",
 "a": """Three reasons. First, ubiquity: recommender systems decide what billions of people see, buy and listen to,
 so the transparency gap has practical weight, and the EU AI Act and the GDPR make it a governance question rather
 than only a research one. Second, an exploitable structure: a recommender is naturally a cooperative game —
 users, items and contexts are entities whose joint value is a quality of recommendation, so the Shapley framework
 does not have to be forced onto it. Third, measurability: ranking quality, catalogue coverage and intra-list
 diversity are all well-defined, so the claim that attribution can guide learning is falsifiable against strong
 baselines rather than argued qualitatively.""",
},
{
 "q": "What would the thesis look like if you had only done Contribution III?",
 "a": """It would be a strong applied paper but a weaker thesis, for two reasons. First, without Contributions I and
 II, the claim "the same cooperative-game language works for explanation and for optimisation" would be an
 assertion rather than a demonstration: the two clustering chapters are what show that the framework is not
 specific to recommendation architecture. Second, the in-training signal in C3 is built from a utility over
 entities, while C1 and C2 compute attribution over features of a partition; having both makes the argument that
 the choice of players and value function is a design decision within one framework, not a different method each
 time. What C3 would gain is depth — more datasets, more baselines, an online evaluation — and that is exactly where
 the future work points.""",
},
{
 "q": "Who is the intended user of your explanations?",
 "a": """Three audiences, with different needs, and the thesis serves two of them directly. For the *analyst or
 domain expert* — a wine technologist, an air-quality scientist — the explanation is the global ranking and the
 cluster profiles in the original variables: which measurements separate the regimes, and what distinguishes each
 one. For the *model designer or auditor*, the explanation is the axiomatic attribution: it shows how the decision
 decomposes, with efficiency guaranteeing that the parts account for the whole. For the *end user* of a
 recommender, the thesis does not deliver a user-facing explanation interface: the waterfall read-out described in
 C3 is a mechanism for showing which terms the objective valued, not a natural-language justification, and
 user-facing explanation quality is plainly left as future work.""",
 "tags": ["danger"],
},
{
 "q": "What is the thesis's answer to RQ5?",
 "a": """RQ5 asks what is gained when clustering explanation and recommendation learning are treated as two stages of
 one cooperative-game view. The answer the thesis gives is fourfold. First, a *common formal language*: features,
 interactions and contexts are all players, and attribution is always the same allocation rule, so results from
 different stages are comparable. Second, *three achievements under one logic*: faithful clustering explanation,
 consistent multi-level explanation, and contribution-aware recommendation learning. Third, *explanation as a
 method rather than a comment*: because the same game can be optimised, attribution moves from post-hoc description
 into training. Fourth — and I would present this as positioning rather than a result — *alignment with the
 expectations of the AI Act, the OECD principles and the GDPR*. The honest bound is stated on slide 70: a
 consistent and productive shared view, not one fully unified framework that removes all tension.""",
 "tags": ["must know"],
},
{
 "q": "If you had to remove one of the three contributions, which one and why?",
 "a": """I would remove neither, but if forced, the removable one is Contribution II — and I would want to say why
 that choice is uncomfortable. Contribution I establishes that Shapley attribution can explain an unsupervised
 partition faithfully in the original feature space; Contribution III is the thesis's principal claim, the move
 from post-hoc to in-training. Contribution II is the bridge, and the bridge carries two things the other two do
 not: Proposition 6.1, which is the only formal result in the thesis beyond the axiomatic justification, and the
 scale test on 383,585 records. Removing it would leave a two-step story with a large jump from a 4,898-row wine
 table to a hypergraph recommender, and it would remove the only place where cross-level consistency is addressed
 — which is one of the three limitations stated on slide 14. So: it is the contribution whose loss would cost the
 least empirically and the most structurally.""",
 "tags": ["danger"],
},
]},

# ============================================================ B. GAME THEORY
{
 "title": "B · Cooperative game theory and the Shapley value",
 "items": [
{
 "q": "Why Shapley rather than another attribution method?",
 "a": """Because the Shapley value is the unique allocation rule that satisfies four properties at once: efficiency
 (the attributions sum to the total value), symmetry (identical contributors receive equal credit), null player
 (irrelevant variables receive zero) and additivity (attributions compose across games). Chapter 2, section 2.8.2,
 states the axioms, and Appendix A.1 proves uniqueness by decomposing any game into unanimity games. That matters
 for this thesis in a specific way: cluster-level claims need credit assigned to a feature to be comparable
 across clusters, and LIME-style local surrogates give no such guarantee, because their explanation depends on the
 neighbourhood definition, the perturbation process and the quality of the local fit. So the argument is
 normative rather than empirical — and the thesis is explicit that the SHAP-versus-LIME comparison in Chapter 5 is
 theoretical and literature-backed, not an experimental bake-off.""",
 "tags": ["must know"],
},
{
 "q": "State the four axioms and say what each one prevents.",
 "a": """*Efficiency*: the values sum to v(N) minus v(empty), so the parts account for the whole and nothing is left
 unexplained. *Symmetry*: players making identical marginal contributions to every coalition receive equal value,
 which prevents arbitrary differences in credit and makes cross-cluster comparison meaningful. *Null player*: a
 player whose presence never changes any coalition's value receives zero, which prevents the "importance" that
 correlation-driven methods assign to irrelevant variables. *Additivity*: attributions are additive across games,
 which is what allows local attributions to be averaged into a global ranking and allows composite objectives to be
 decomposed. The Shapley value satisfies all four; the thesis's Appendix A.1 shows it is the only rule that does.
 The deck's orange bar on slide 29 is the compressed version of this answer.""",
 "tags": ["must know"],
},
{
 "q": "Why not the Banzhaf index or the nucleolus?",
 "a": """The Banzhaf index also averages marginal contributions, but over coalitions rather than over orderings, and
 in its standard form it does not satisfy efficiency: its attributions need not sum to the total value being
 explained. For a thesis that treats completeness of the attribution as a design requirement — if the model's
 output is explained, the explanation should account for it — that is a disqualifying property. The nucleolus was
 developed for dissatisfaction minimisation in cooperative bargaining; it answers a different question and is not
 aimed at additive feature attribution, so it is less naturally suited here. Both are legitimate tools in the
 cooperative-game literature, and the thesis cites them as alternatives rather than dismissing them: it selects
 Shapley because it is the rule characterised by the four properties the thesis relies on.""",
},
{
 "q": "Did you run LIME?",
 "a": """No, and I will be precise about what that means. In Chapter 5 the comparison between SHAP and LIME is
 theoretical and literature-backed, not a full empirical bake-off on the wine data. LIME is described in the
 protocol of Chapter 4 as the comparator in a shared explanation pipeline (section 4.3.7) and discussed again in
 Chapter 6, and Table 5.1 in Chapter 5 sets out the theoretical contrasts: SHAP is grounded in an allocation rule
 with axiomatic guarantees, while LIME's explanation depends on neighbourhood definition, perturbation design and
 local fit quality. The reason the comparison is theoretical is that the thesis's argument for Shapley is
 axiomatic, not empirical: it does not depend on which method produces nicer-looking plots on one dataset. If you
 want an empirical comparison, that is not claimed here, and I would put it in the future work rather than
 overstate what the chapter shows.""",
 "tags": ["danger", "must know"],
},
{
 "q": "Are you explaining K-Means, or are you explaining the surrogate?",
 "a": """I am explaining a faithful supervised reconstruction of the partition, and the thesis states this in its own
 words on page 58: the chapter does not claim to explain K-Means geometry in a mechanistic sense. The reason for the
 surrogate is mechanical: TreeSHAP computes exact Shapley values for tree ensembles, and K-Means is a set of
 centroids with a distance function, so there is no exact tree attribution available for it. Explaining the PCA
 representation would instead move the attribution out of the interpretable variables, which would break objective
 O2 and the actionability requirement. The surrogate is a 100-tree, 31-leaf LightGBM multiclass classifier that
 predicts cluster labels from the original eleven features and reaches macro-F1 around 0.82 on held-out labels. That
 fidelity is the validity condition: the bridge is trustworthy exactly as long as the reconstruction is.""",
 "tags": ["danger", "must know"],
},
{
 "q": "If the value function is the Silhouette of the clustering, why are the SHAP values computed on the surrogate?",
 "a": """Because they are two different objects, and the thesis says so plainly. The Silhouette-based cooperative
 game motivates the analysis — it defines who the players are and what a coalition is worth in principle. The
 surrogate is the tractable bridge that makes exact TreeSHAP possible. A consequence is that the efficiency
 property holds with respect to the surrogate's log-odds output rather than with respect to the Silhouette-based game
 value directly: SHAP values sum to f(x) minus the expected output for the surrogate. The thesis calls this a known
 constraint of the surrogate strategy, not a reason to abandon it, and the safeguard is the fidelity floor of
 roughly macro-F1 0.80-0.82: the explanation is faithful to the surrogate, and the surrogate is useful only when it
 is faithful to the partition.""",
 "tags": ["danger"],
},
{
 "q": "What exactly does Proposition 6.1 prove, and what does it not prove?",
 "a": """It proves a decomposition: for a strict nested hierarchy on a consistent feature space, the expected
 absolute importance of feature j at hierarchy level l in cluster c equals the size-weighted expectation of the
 same quantity over the children of c, plus a residual term induced by surrogate approximation that vanishes under
 perfect fidelity. It is derived from the law of total expectation, because the children partition the parent. What
 it does not prove is any kind of invariance: it does not say explanations are identical across levels, and it is
 not a general theory of hierarchical Shapley consistency. The thesis is unusually careful here — it says the
 proposition is an original thesis-level formalisation to be read as a careful clarification, that the residual is
 treated as a conceptual term rather than an empirically estimated quantity, and that no separate Beijing-level
 residual analysis is reported.""",
 "tags": ["danger", "must know"],
},
{
 "q": "Then why does feature importance change between levels?",
 "a": """Because the two levels answer different questions about the same data. At the coarse level, importance
 reflects regime selection: temperature and dew point dominate because they separate the broad atmospheric regimes.
 Inside a cluster, importance reflects variation within a regime: CO, SO2, PM10, wind speed, pressure or ozone
 become more discriminative depending on which regime is being described. Proposition 6.1 makes those two readings
 commensurable — it says the parent-level expected importance is the size-weighted expectation over the children up
 to a surrogate residual — so a difference is not evidence that one of the two explanations is wrong. The slide's
 formulation is the one to keep: the change is not a contradiction, it is exactly what a multi-level explanation
 should reveal.""",
},
{
 "q": "Is your hierarchy real, or did you impose it?",
 "a": """It is imposed, deliberately, and the thesis says so: the hierarchy is a pragmatic analytical device, not a
 claim that nature is organised hierarchically. What the method assumes is only the operational property needed by
 the proposition — a strict nesting, where every child cluster is a subset of exactly one parent and the children
 partition the parent — together with a consistent feature space across levels. In the Beijing case the hierarchy
 comes from recursive K-Means: a coarse partition into k = 3 regimes, then each coarse cluster subdivided where
 appropriate, with a level-specific LightGBM surrogate and TreeSHAP computed in the same eleven variables. The
 useful consequence of stating this openly is that the method's claim is not "the world is a tree"; it is "if you
 adopt a nested view, here is how the explanations at the two levels relate".""",
 "tags": ["danger"],
},
{
 "q": "Your C3 estimates are sampled. Are they still Shapley values?",
 "a": """The estimator is unbiased for the Shapley value of the defined game, so on average it is exactly the
 Shapley value; each individual estimate has variance σ²/M. That is the correct technical statement, and the deck
 says it on slide 55: "unbiased estimator: variance σ²/M". What the estimates are *not* is the exact Shapley value
 of a fixed game computed at every step of training, for two reasons: they are sampled, and the game itself is
 defined on the local episode under consideration at each refresh rather than on an exhaustive full-catalogue
 player set. The thesis is explicit that the resulting estimator should be read as an approximate in-training
 valuation procedure aligned with the local recommendation context. Practical consequences: M = 50 gives MSE
 1.4×10⁻⁵ and about 99 % agreement with a high-sample reference; clipping, exponential smoothing and
 normalisation keep the resulting weights stable.""",
 "tags": ["danger"],
},
{
 "q": "What is the size of the player set in Contribution III, given that exact Shapley is exponential?",
 "a": """The player set is scoped to the interaction episode under consideration at each refresh stage, not to the
 full catalogue. A typical local episode contains one focal user, a small set of candidate items and the associated
 context nodes, so the effective player set is on the order of a few dozen entities. That is a modelling decision
 with two consequences I should state clearly. First, the method never attempts a Shapley value over the whole
 catalogue, so the exponential objection does not apply to what is actually computed. Second, and correspondingly,
 the value computed is a local valuation of that episode's entities, which is why the thesis describes it as an
 approximate in-training valuation procedure rather than as an exact global attribution. The coalition utility is
 evaluated on the recommendation episode induced by the coalition: only interactions whose user, item and context
 are present in S survive, the surviving candidates are ranked, and NDCG@20, diversity and context alignment are
 averaged over those lists.""",
 "tags": ["danger"],
},
{
 "q": "Is v(S) well defined for an arbitrary coalition of users, items and contexts?",
 "a": """Yes, by construction, and the thesis specifies exactly how. The player set is N = U ∪ I ∪ C; a coalition S
 is a subset of entities participating in a recommendation episode; the value v(S) measures the quality of the
 recommendation outcome achievable by coalition S. Operationally, the value is evaluated on the episode induced by
 the coalition: interactions whose user, item and context entities are all present in S are retained, the surviving
 candidate items are ranked for the eligible users, and NDCG@20, diversity and context alignment are computed on
 those restricted top-20 lists and averaged over eligible interactions. So NDCG@20(S) is a recommendation utility
 on a coalition-induced candidate set rather than an abstract score on isolated entities. The preference-aware
 extension adds λ_pref times the sum of user-item similarity over pairs in S, keeping the preference component
 separable and interpretable.""",
 "tags": ["danger"],
},
{
 "q": "What about correlated features? SHAP values are not unique when inputs are dependent.",
 "a": """This is the sharpest technical objection to any SHAP-based analysis, and it deserves a precise answer. The
 Shapley value is unique once the value function is fixed, but the value function itself depends on how you model
 feature dependence. With correlated inputs, the conditional expectation (what the model predicts given only the
 values of a coalition, respecting the data distribution) and the interventional expectation (what the model
 predicts when the other features are marginalised independently) give different numbers; TreeSHAP uses the
 tree-structure-based conditional expectation, so the values reflect the model's behaviour under the data
 distribution. Wine's eleven physicochemical variables are heavily correlated — density integrates sugar, alcohol
 and extract — so I would not claim that the attributions partition causation among them. What I do claim is that
 the values are the exact and unique allocation of the surrogate's output under the stated value function,
 satisfying efficiency, symmetry, null player and additivity. The practical implication for interpretation is to
 read the ranking as a structured decomposition and, where two features are near-substitutes, to treat their
 split of credit as a modelling choice rather than as a physical law.""",
 "tags": ["danger"],
},
{
 "q": "Could the cooperative game in C3 be criticised as a metaphor rather than a model?",
 "a": """It is a legitimate criticism to raise, and the right response is to be precise about what is claimed. The
 game is formally well defined — a player set, a coalition structure, a characteristic function with a stated
 operational evaluation — and the Shapley value of that game is what is estimated and used as a weight. What is
 specific about it is that the characteristic function is instantiated on a local episode rather than on the global
 entity set, so it is a local valuation game; the thesis says this rather than hiding it. Where the design is
 genuinely a modelling choice rather than a theorem is the choice of utility: the weights α = 0.60, β = 0.25,
 γ = 0.15 were selected by grid search on validation performance, so the game encodes a value judgement about what
 makes a recommendation good — accuracy first, then diversity, then context. That is the honest version of the
 claim: an explicit, multi-objective, testable valuation, not a natural law.""",
 "tags": ["danger"],
},
]},

# ============================================================ C. CONTRIBUTION I
{
 "title": "C · Contribution I — explainable black-box clustering",
 "items": [
{
 "q": "Why k = 3 for wine when k = 2 has better geometry?",
 "a": """Because the number of clusters was chosen on interpretability grounds, and the geometric cost is reported
 openly. The k-scan uses elbow, Silhouette and Davies-Bouldin over k from 2 to 10; at k = 2 the Silhouette is 0.214
 with Davies-Bouldin 1.775, and at k = 3 it is 0.144 with Davies-Bouldin 2.097, so k = 2 separates better. It was
 rejected because it supports one coarse split rather than three distinct explanatory profiles: with three clusters
 the per-cluster SHAP signatures are materially different, which is what makes the explanation useful to a wine
 analyst and what makes the cluster-level claim of RQ1 meaningful. It is also worth adding that k = 3 is not a
 wine-only judgement: on the air-quality corpus the same choice wins geometrically as well, 0.626 against 0.265,
 so the adopted setting is the best overall balance across the two corpora. This is a deliberate methodological choice, it is
 stated on the slide, and it is consistent with Definition 1.1: the value of an explanation is its actionability,
 not only its geometry. If a jury prefers the geometric criterion, the position to defend is that both criteria are
 reported and the trade-off is declared, not hidden.""",
 "tags": ["danger", "must know"],
},
{
 "q": "Where does the 0.63 Silhouette come from?",
 "a": """From the Beijing air-quality clustering, not from the wine partition. The wine partition at k = 3 has a
 Silhouette of 0.144 and a Davies-Bouldin index of 2.097; the Beijing coarse partition has a Silhouette of about
 0.63 with Davies-Bouldin about 0.55. The thesis repeats this distinction twice, exactly because the two numbers
 appear in consecutive chapters and are easy to confuse. In speech: whenever you say 0.63, say "Beijing"; whenever
 you say 0.144, say "wine". The reason the two differ so much is substantive, not a modelling error: the Beijing
 data contain a strong, physically driven regime structure, while the wine data are a small, dense,
 chemically correlated table where a three-way split is a useful description rather than a natural separation.""",
 "tags": ["danger", "must know"],
},
{
 "q": "What is macro-F1 ≈ 0.82, and what happens if the surrogate is not faithful?",
 "a": """Macro-F1 is the average of the per-class F1 scores — the harmonic mean of precision and recall for each
 cluster — computed without weighting by class size, so a small cluster counts as much as a large one. It measures
 how well the LightGBM surrogate reproduces the K-Means labels on held-out data; 0.82 is the value reached with
 the default 100-tree, 31-leaf configuration for both wine and Beijing, and the thesis treats roughly 0.80 as the
 practical floor. If fidelity were low, the explanation would describe a model that is not the partition: the
 attribution would be faithful to the surrogate and misleading about the clustering. That is why the thesis calls
 surrogate fidelity a standing interpretive condition and lists surrogate dependence as the first limitation of
 Contribution I. The mitigation is procedural: fidelity is measured with five-fold cross-validation and must clear
 the floor before the attribution is reported.""",
 "tags": ["must know"],
},
{
 "q": "Why LightGBM as the surrogate rather than a neural network or a linear model?",
 "a": """Because the surrogate has to satisfy three requirements at once, and a gradient-boosted tree ensemble is
 the point where they meet. It must be expressive enough to reproduce a non-linear partition of eleven features —
 a linear model would underfit and the fidelity floor would fail. It must run TreeSHAP, which is exact and
 polynomial-time for tree ensembles; a neural surrogate would force a model-agnostic estimator such as KernelSHAP
 and add a second layer of approximation. And it must be stable under small changes of configuration, which the
 thesis checks in the sensitivity analysis on tree depth. LightGBM's leaf-wise growth also makes it fast on tabular
 data of this size, which matters for the Beijing study with 383,585 rows. The choice is so not a
 preference: it is determined by the requirement that the attribution step be exact for the model it explains.""",
},
{
 "q": "Are the wine clusters chemically meaningful, or are you narrating bars?",
 "a": """The check is not a narrative; it is the ranking plus the profiles. The global mean |SHAP| ranking puts
 density first, then pH, fixed acidity, sulfur dioxide and alcohol, and these are structure, preservation and
 sensory-balance variables in wine chemistry — a wine technologist would name them. Each also has a distinct
 reading in the per-cluster profiles: density and pH separate wine styles, sulfur dioxide reflects preservation
 practice, alcohol shapes body. What the thesis does not claim is that the clusters correspond to a known
 enological classification: the two-cluster solution is geometrically better, and the three-cluster solution was
 chosen because it supports three distinct explanatory profiles, which is an argument about explanatory richness,
 not about chemistry. The strongest available check would be a domain expert's assessment of the profiles, and that
 is not reported — it belongs to the same user-centred future work as actionability.""",
 "tags": ["danger"],
},
{
 "q": "Density being the most important feature — is that an artefact of standardisation or of the surrogate?",
 "a": """It is not an artefact of standardisation, and the reasoning is worth stating because it is a common
 objection. Standardisation puts all eleven variables on a common scale of one standard deviation, so a feature
 cannot dominate merely by being measured in larger units; without it, density — measured in grams per millilitre
 with a very small variance — would in fact tend to be underweighted rather than over-weighted. Density is also a
 derived physical quantity that integrates sugar, alcohol and extract, so it is chemically plausible that it
 separates production styles. As for the surrogate: the ranking is reported for the model that reproduces the
 partition, at fidelity macro-F1 ≈ 0.82, and the sensitivity analysis shows that the leading drivers are stable
 under changes in projection dimension and tree depth while low-ranked variables move. What cannot be ruled out
 from the thesis alone is a dependence on the particular surrogate family, and that is exactly the surrogate
 dependence listed as a limitation.""",
 "tags": ["danger"],
},
{
 "q": "What is the difference between the global ranking and the per-cluster profiles?",
 "a": """They are two levels of the same attribution. The global ranking sorts features by mean absolute SHAP value
 over all instances: it answers "which variables move the model's decision most on average" and says nothing about
 direction or about differences between clusters. The per-cluster profiles are the same values restricted to the
 instances of one cluster — the same features, different weights — and they answer "what defines membership in this
 particular group as opposed to the others". This two-level output is exactly what objective O1 promises, and it
 is the reason clustering is described in the thesis as the hardest explanatory test bed: the model creates its own
 structure, so cluster meaning has to be established after the fact, from the profiles, rather than being read off
 a label. The figure pair on slide 33 (Fig. 5.1 global, Fig. 5.2 per cluster) is the visual form of this answer.""",
},
{
 "q": "Why does the thesis say “partially model-agnostic”?",
 "a": """Because two different things are being kept separate. The *game definition* is model-agnostic: any
 partition-producing method can be given the same treatment, since the players are the input features and the value
 function is a quality measure of the clustering on a feature subset. The *exact attribution step* is not
 model-agnostic: it relies on the surrogate being a tree ensemble so that TreeSHAP can compute exact values. Calling
 the pipeline fully model-agnostic would overstate it, because a different surrogate family would change the
 attribution method; calling it model-specific would understate it, because the framework itself does not depend on
 K-Means. The phrase in the thesis abstract and on slide 27 is the honest middle term, and using it correctly is
 itself evidence of understanding the method.""",
 "tags": ["danger"],
},
{
 "q": "Did you evaluate the explanation, rather than only the model?",
 "a": """Partially, and I would distinguish three levels of evaluation. The *fidelity* of the surrogate is measured
 quantitatively (macro-F1 ≈ 0.82 on held-out labels, five-fold cross-validation), which is an evaluation of the
 explanation's validity condition. The *interpretability* of the result is assessed qualitatively: the global
 ranking and cluster profiles are checked against domain knowledge in wine chemistry and air quality. What is not
 evaluated is the *human* dimension — whether the explanations improve understanding, trust, or decisions — and the
 thesis says so plainly in the limitations and in the perspectives. Faithfulness metrics for explanations
 themselves (for example deletion or perturbation-based tests on the explanation) are also not run in this work.
 So the honest answer is: the bridge was validated, the domain plausibility was argued, the user effect was left
 open.""",
 "tags": ["danger"],
},
{
 "q": "What is the biggest weakness of Contribution I?",
 "a": """That the explanation is one modelling step away from the thing being explained. TreeSHAP cannot be applied
 to K-Means directly, so the pipeline explains a LightGBM surrogate whose fidelity to the partition is
 macro-F1 ≈ 0.82 rather than 1.0, and the efficiency guarantee applies to the surrogate's log-odds output rather
 than to the Silhouette-based game value. The thesis names this as surrogate dependence and states it on page 58.
 The second weakness is the single level: importance cannot be shown to change between a partition and its
 sub-partitions, which is exactly why the next contribution exists. The third is scope: tabular data only, with
 no graph, text or image input. All three are volunteered on slide 36 rather than extracted by the jury, which is
 the correct posture.""",
 "tags": ["must know"],
},
{
 "q": "Could the pipeline work for a non-tabular dataset — text, images, graphs?",
 "a": """Not as it stands, and the thesis lists that as a limitation of both clustering contributions. The obstacles
 are concrete. The value function is a distance-based clustering quality (Silhouette on a feature subset), which
 presupposes a fixed, low-dimensional, comparable feature space. The surrogate is a tree ensemble, which handles
 tabular data naturally and images or text poorly without a learned representation. And the actionability
 requirement demands that the players be named, modifiable factors, which is exactly what raw pixels or tokens are
 not. A non-tabular version would so need either a meaningful engineered feature space — as the eleven
 physicochemical and pollutant variables are — or a different formulation in which players are concepts or
 learned factors whose meaning is established separately. That is a research programme, not an extension, and it is
 honest to say so.""",
},
{
 "q": "What would a counterfactual version of your explanation look like, and why did you not do it?",
 "a": """A counterfactual explanation would answer a different question: not "how much did density contribute to
 this membership" but "what would density have to be for this sample to be assigned to a different cluster". That
 is an intervention-style statement, and it is arguably the most natural bridge from attribution to action, because
 it produces a target for the modifiable factor. The thesis stays in the attribution family: SHAP says how the
 prediction decomposes, while counterfactuals say what to change. The reasons for not adding them here are scope
 and the fact that the contribution's claim is about faithful attribution and cross-cluster consistency, not about
 generating interventions; but I would agree that a combined read-out — attribution to identify the factor,
 counterfactual to quantify the change — is a natural and valuable extension, and it fits the user-centred
 evaluation direction on slide 71.""",
},
{
 "q": "Why K-Means and not another clustering algorithm — a Gaussian mixture, DBSCAN, or hierarchical clustering?",
 "a": """Because K-Means is the algorithm whose opacity is easiest to describe, and because its geometry makes the
 value function well defined. A Gaussian mixture would give probabilistic memberships and a likelihood, which is a
 different attribution question; DBSCAN produces density-based clusters with noise points and a variable number of
 clusters, which complicates both the partition and the cross-level nesting; hierarchical clustering gives a tree
 directly, but with a linkage-driven structure that the thesis wanted to control plainly. K-Means with an
 explicit k scan makes the selection criteria visible — elbow, Silhouette, Davies-Bouldin — and produces hard
 assignments that map cleanly onto the surrogate classification task, which is what makes the TreeSHAP bridge
 possible. The framework itself is not tied to K-Means: the players are the features and the value function is a
 partition-quality measure, so the same treatment could be applied to any hard-assignment clustering algorithm
 whose quality can be evaluated on a feature subset. That is the sense in which the thesis describes the pipeline
 as partially model-agnostic.""",
},
{
 "q": "Which result in Contribution I would you defend hardest, and which is weakest?",
 "a": """Defend hardest: the two-level output in the original feature space. The pipeline returns a global ranking
 and per-cluster profiles in the same eleven named variables, with a measured fidelity condition, and that
 combination is what makes the result usable — it is also the property that C2 then extends and C3 then reuses.
 Weakest: the selection of k = 3. It is a defensible decision, but it is a judgement: the geometric criteria prefer
 k = 2, and the argument for three clusters rests on explanatory richness rather than on a measured outcome such as
 "analysts made better decisions with three". If I were to strengthen the thesis, that is where a small expert study
 would add the most, and it is consistent with the user-centred evaluation that the thesis lists as future work.""",
 "tags": ["danger"],
},
]},

# ============================================================ D. CONTRIBUTION II
{
 "title": "D · Contribution II — multi-level explanation at scale",
 "items": [
{
 "q": "Why Beijing after wine? What does the second dataset add?",
 "a": """It adds three things that the wine study cannot test. Scale: 383,585 hourly records against 4,898 wine
 samples, which is roughly eighty times more data and the point where explanation by enumeration becomes
 infeasible. Structure: the data are dense enough to support a nested hierarchy of regimes and sub-regimes, so the
 multi-level question becomes real rather than hypothetical. Domain distance: wine and air quality share almost no
 variables, so a method that works in both is not a wine-specific procedure; the same pipeline, the same surrogate
 family, the same metric logic and the same reading apply, which is finding 4 on slide 48. There is also a
 substantive gain: the Beijing structure is physically strong (Silhouette ≈ 0.63 against 0.144 for wine), which
 makes it a fair test of whether the explanation tells a story that a domain expert recognises.""",
},
{
 "q": "How do you know the three Beijing regimes are real rather than artefacts of k-means?",
 "a": """There are four pieces of evidence, and none of them is conclusive on its own. First, metric agreement: at
 k = 3 the elbow, Silhouette and Davies-Bouldin criteria agree, with Silhouette ≈ 0.63 and Davies-Bouldin ≈ 0.55,
 which is a much stronger separation than the wine partition. Second, physical readability: the three clusters map
 onto recognisable atmospheric situations — warm photochemical episodes with ozone, temperature and dew point;
 winter smog with CO, SO2 and particulate matter and low wind speed suppressing dispersion; and comparatively clean
 periods with favourable meteorology. Third, stability: the sensitivity analysis varies k, projection dimension and
 surrogate depth, and the leading drivers remain stable while low-ranked variables move. Fourth, independent
 reference: the literature on air quality describes similar regimes. The honest caveat is that this is an
 unsupervised analysis: the regimes are a useful description of the data, not a verified physical classification,
 and the thesis does not claim otherwise.""",
 "tags": ["danger"],
},
{
 "q": "Is your 0.63 Silhouette comparable with the 0.37 reported in the credit-risk study?",
 "a": """No, and the deck calls it a positioning point rather than a like-for-like benchmark. Gramegna and Giudici
 report a Silhouette of about 0.37 in a SHAP-based clustering study on credit-risk data, and the comparison is
 cited to locate the Beijing result in the literature, not to claim superiority. Three things prevent a fair direct
 comparison: the datasets come from different domains with different dimensionality, noise levels and natural
 cluster separation; Silhouette depends on the number of clusters and on the distance structure, so two values from
 different features are not on a common scale; and the preprocessing and the value function differ between studies.
 The defensible statement is: on this dataset with these variables, the three-regime structure separates strongly
 (≈ 0.63), considerably more strongly than the wine partition, and the thesis cites the literature value as
 context.""",
 "tags": ["danger"],
},
{
 "q": "The weather variables include wind direction. Where did “rain” come from?",
 "a": """From an error in an earlier version of the deck, which was corrected. The thesis and the source paper list
 eleven modelling variables: six pollutants (PM2.5, PM10, SO2, NO2, CO, O3) and five weather variables —
 temperature, pressure, dew point, wind direction and wind speed. "Rain" appeared in a draft of the slide and was
 replaced with "wind direction" in v26 after the deck was checked against the thesis (p. 43) and the IJACSA paper
 (Table III). The current v32 file is correct, and this is a good example of why the deck was audited against the
 sources rather than trusted: the version history in the repository documents the change, including the exact
 before-and-after text.""",
 "tags": ["danger"],
},
{
 "q": "What is the computational cost of the multi-level pipeline at this scale?",
 "a": """The pipeline is deliberately designed so that cost grows with the data and not exponentially with the
 features. The expensive step in Shapley computation is coalition enumeration, which is avoided entirely: exact
 TreeSHAP runs on each level's LightGBM surrogate in time polynomial in the trees, the leaves and the depth, and
 the data are processed in one pass per level. The surrogate itself is a modest 100-tree, 31-leaf model, and the
 reporting scope is global summaries plus one representative local force plot per cluster, which is what the thesis
 states rather than an undocumented subsample. In practice the Beijing study runs on a standard workstation — an
 i9-14900K with 48 GB of RAM and the full dataset in memory — with no GPU, which is itself the evidence that the
 cost is manageable. The qualitative statement on slide 48 is the one to keep: cost linear in the data, not
 exponential in the features.""",
},
{
 "q": "Why not use an established hierarchical clustering algorithm with a dendrogram?",
 "a": """A dendrogram from agglomerative clustering would give a hierarchy, but not the object this contribution
 needs. Agglomerative linkage defines clusters by a merge criterion and produces a single tree whose levels are
 determined by the linkage, while the framework here needs an explicit, controllable level structure with a
 surrogate fitted at each level and explanations expressed in the same feature space at every level — the
 conditions under which Proposition 6.1 applies. Recursive K-Means with a chosen k per level gives that control: it
 is transparent, reproducible, comparable across levels, and each level's partition is a strict refinement of the
 parent, which is exactly the nesting hypothesis. A dendrogram would also make the "subdivide where appropriate"
 decision implicit in the linkage rather than explicit in the analysis, and the thesis prefers the explicit
 version exactly because it has to be defended.""",
},
{
 "q": "How sensitive are the conclusions to k, to the projection dimension and to surrogate depth?",
 "a": """The reported outcome is deliberately nuanced rather than binary. The analysis is robust to modest variation
 in all three: the dominant meteorological and pollutant drivers remain stable, and the changes are concentrated in
 low-ranked variables. That is a more credible claim than "nothing changes at all", because with real data some
 reordering among low-importance features is expected. Two qualifications belong to the answer. First, the
 sensitivity study varies one family of settings at a time; it is not a full factorial design, so interactions
 between, say, k and surrogate depth are not characterised. Second, the stability statement is about the leading
 drivers and the physical reading, not about exact SHAP magnitudes, which do move. Both qualifications are the kind
 of thing a careful jury member will appreciate hearing volunteered.""",
 "tags": ["danger"],
},
{
 "q": "Your aggregation weights children by size. Why size and not importance?",
 "a": """Because size is what makes the identity true. Proposition 6.1 comes from the law of total expectation, and
 the law of total expectation needs the weights to be the probabilities of the conditioning events — here, the
 relative frequencies of the children within the parent, w_c' = |c'| / |c|. Weighting by importance would introduce a
 second, unexplained weighting scheme and the identity would no longer hold; the residual would absorb the
 difference and stop being interpretable as surrogate mismatch. It is worth adding what the size weighting implies:
 with perfect fidelity, parent importance is a convex combination of child importances, so it cannot fall outside
 the range of the children. If a reported parent value is outside that range, the residual is doing work, and that
 is a diagnostic rather than a puzzle.""",
 "tags": ["danger"],
},
{
 "q": "Is Proposition 6.1 falsifiable? How would you test it?",
 "a": """Yes, in the sense that it makes a quantitative prediction that could fail. Under the stated conditions —
 strict nesting, consistent feature space, surrogate fidelity — the parent-level expected absolute importance
 should equal the size-weighted average of the child-level values up to the residual. A direct test would be to
 estimate the parent-level expectations with high-precision SHAP on the parent surrogate and compare them with the
 weighted child values, reporting both the discrepancy per feature and its relationship to the fidelity gap; if the
 discrepancy were large and unrelated to fidelity, the identity's practical value would be undermined. What the
 thesis does instead is state the identity, prove it under its hypotheses and treat the residual as conceptual. It
 does not report the residual analysis, and the thesis says so in as many words: ε is "a conceptual residual term
 rather than an empirically estimated quantity". That is the honest position, and it also marks the most natural
 next experiment.""",
 "tags": ["danger"],
},
{
 "q": "The Beijing data are hourly and span four years, but your partition is static. Is that a problem?",
 "a": """It is a real limitation, and it is the first item on the limitations slide for a reason. The clustering
 treats the 383,585 records as one pool, so it describes the regimes that exist across the period rather than how
 those regimes evolve; inter-annual drift, seasonality and long-run trends are not modelled, and no temporal
 validation is reported. Two things reduce the concern without removing it. First, the question the chapter asks
 is about explanation at scale and across levels, not about forecasting, so a static partition is a legitimate
 object for that question. Second, the regime descriptions are consistent with the known seasonal structure of
 Beijing pollution, so the pooled view is not obviously misleading. But if the intended use were monitoring or
 early warning, a temporal model — sliding windows, change detection, or a streaming formulation — would be
 needed, and that is exactly the online and streaming direction on the perspectives slide.""",
 "tags": ["danger"],
},
{
 "q": "What is the practical use of the Beijing result?",
 "a": """The practical value is explanatory rather than predictive, and I would not overstate it. The result says
 that the structure of the pollution data is defined by meteorology as much as by pollutant concentrations:
 temperature, dew point and pressure lead the coarse-level ranking, and pollutants then vary within those regimes.
 For an air-quality analyst, that reframes the question from "which pollutant is high" to "which regime are we in,
 and what varies inside it" — a distinction that flat summary statistics typically do not make explicit, which is
 the point the chapter makes on page 73. It also shows the method: the same pipeline that explained a
 4,898-row wine table works on 383,585 rows with an interpretable result. What it does not provide is a forecasting
 or policy-evaluation tool, and the thesis does not claim one.""",
},
{
 "q": "Which of the three objectives of Contribution II is least convincingly met?",
 "a": """Objective O2, the formal consistency argument, is the one I would describe as met in a bounded sense rather
 than completely. The proposition is proved under hypotheses that the empirical setting only approximates: the
 nesting is strict as imposed by the recursive clustering, the feature space is consistent by design, but the
 residual induced by surrogate approximation is not estimated — the thesis treats it as a conceptual term. So the
 honest status is analytical support for the cross-level reading, shown on one dataset, rather than a
 verified quantitative identity. O1, the genuinely multi-level workflow, is met straightforwardly: coarse regimes,
 then level-specific surrogates, then size-weighted aggregation. O3, validation at scale on a new domain, is met:
 383,585 records, Silhouette ≈ 0.63, three physically readable regimes with a sensitivity check.""",
 "tags": ["danger"],
},
]},
]
