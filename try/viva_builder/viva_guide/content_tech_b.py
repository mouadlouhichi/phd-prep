# -*- coding: utf-8 -*-
"""Beginner glossary, part B: recommenders, metrics, statistics, theory, governance."""

GLOSSARY_B = [
# ---------------------------------------------------------------- recommenders
{
 "term": "Collaborative filtering (CF)", "tag": "Recommenders", "where": "slides 10, 23, 52",
 "plain": "Recommending items by looking at what similar users did, without using any description of the items themselves.",
 "deep": "CF builds its model from the user-item interaction matrix alone: ratings, clicks, purchases. It comes in "
         "user-based form (find users like you) and item-based form (find items that co-occur with what you liked). "
         "Its power is that it needs no metadata; its weakness is that it cannot say *why* in domain words, because "
         "the only thing it knows is co-occurrence. It is also blind to brand-new users and items, which is the cold "
         "start problem.",
 "why": "The thesis's second research family and the ancestor of everything it compares against: matrix "
        "factorisation, neural CF, graph convolutions and hypergraphs are all ways of doing collaborative filtering "
        "with more expressive machinery.",
},
{
 "term": "Content-based filtering", "tag": "Recommenders", "where": "slides 9, 23",
 "plain": "Recommending items that resemble the ones you already liked, using the items' own features.",
 "deep": "The system builds a profile of the user from earlier liked items, then scores new items by feature "
         "similarity: genre, cast, keywords, brand. Because the reason for a recommendation is a named feature, this "
         "family is explainable by construction. The cost is over-specialisation (the filter bubble) and a hard "
         "dependence on rich, well-maintained metadata.",
 "why": "It sets the bar the thesis has to clear: content-based systems are transparent *by construction*, while "
        "the thesis has to get transparency for systems that have no such construction, by attributing credit "
        "after the fact (C1, C2) or during training (C3).",
},
{
 "term": "Hybrid systems", "tag": "Recommenders", "where": "slide 11",
 "plain": "Systems that combine content-based and collaborative signals to cover each other's weaknesses.",
 "deep": "Typical hybrids mix the two predictions, use content features inside a collaborative model, or switch "
         "between strategies. They reduce over-specialisation and part of the cold-start problem, but they add "
         "complexity and inherit the opacity of whichever component dominates the final score.",
 "why": "Hybrids and matrix factorisation are presented together in the deck as the moment accuracy improved and "
        "traceability got worse — the exact tension the whole thesis attacks.",
},
{
 "term": "Matrix factorisation (MF) and the BPR loss", "tag": "Recommenders", "where": "slides 11, 23, 56, 57",
 "plain": "Represent every user and every item by a short vector of latent numbers, and score a pair by the dot "
          "product of the two vectors.",
 "deep": "The interaction matrix R is approximated as P·Qᵀ where P holds user factors and Q item factors. The "
         "factors are learned; nothing forces them to be interpretable, and usually they are not. The loss used in "
         "this thesis for the MF baseline is Bayesian Personalised Ranking (BPR): for a triple (user, observed item, "
         "sampled negative item) it pushes the score of the positive above the score of the negative through a "
         "logistic function, which is the standard way to train on *implicit* feedback where you know what a user "
         "interacted with but not what they rejected.",
 "why": "MF is the classical baseline on both datasets (NDCG@20 = 0.1200 on MovieLens-1M, 0.0049 on Amazon-Book), "
        "and BPR is also the ranking term inside DyHuCoG's composite loss.",
},
{
 "term": "Neural collaborative filtering (NCF)", "tag": "Recommenders", "where": "slides 23, 58",
 "plain": "Replace the dot product of matrix factorisation with a small neural network over the two embeddings.",
 "deep": "NCF learns user and item embeddings and feeds them through multi-layer perceptrons, so the interaction "
         "function is learned rather than fixed. It captures non-linear patterns that a dot product cannot, at the "
         "price of more parameters and less interpretability.",
 "why": "It is the neural-family baseline in the comparison, with NDCG@20 = 0.1300 on MovieLens-1M and 0.0085 on "
        "Amazon-Book. Its gap to the graph models shows how much structure matters on sparse data.",
},
{
 "term": "Message passing and LightGCN", "tag": "Recommenders", "where": "slides 12, 54, 56",
 "plain": "Build a graph of users and items, then let each node update its representation by aggregating messages "
          "from its neighbours, several hops deep.",
 "deep": "One round of message passing gives a node information about its direct neighbours; repeating it k times "
         "brings k-hop information. Graph convolution networks usually add non-linearities and feature transforms at "
         "every layer. LightGCN showed that for recommendation most of that machinery is unnecessary: keep only the "
         "neighbourhood aggregation (a normalised average of neighbour embeddings) and performance improves. This is "
         "why 'simplified graph convolution' is the standard strong baseline on MovieLens-1M and Amazon-Book.",
 "why": "Slide 12 introduces message passing as the mechanism that made recommenders powerful and opaque at once, "
        "and DyHuCoG is a message-passing model whose message weights come from Shapley estimates: the same "
        "mechanism, made accountable.",
},
{
 "term": "Hypergraph, hyperedge, and hypergraph convolution", "tag": "Recommenders", "where": "slides 12, 54, 56",
 "plain": "A graph whose edges can connect more than two nodes at once, so a whole group can share one edge.",
 "deep": "A normal edge is a pair; a hyperedge is a set. That matters because some relations are genuinely "
         "higher-order: a user, an item and a context belong together, a basket contains five products, a session "
         "contains a sequence. A hypergraph is written H = (V, E, W) with V the nodes, E the hyperedges and W the "
         "edge weights; message passing on a hypergraph propagates information from a node to all nodes sharing one "
         "of its hyperedges, usually written with an incidence matrix and degree normalisation. When W is a single "
         "learned scalar per edge, every relation is treated with the same strength — the opacity the thesis targets.",
 "why": "The player set of DyHuCoG is a hypergraph, and W is exactly the matrix that Shapley estimates fill: "
        "'dynamic edge weights derived from Shapley estimates' is the technical definition of the contribution.",
},
{
 "term": "HCCF and HPCF", "tag": "Recommenders", "where": "slides 12, 23, 57, 58",
 "plain": "Two strong hypergraph recommenders: HCCF adds contrastive learning, HPCF adds a projection step.",
 "deep": "Hypergraph Contrastive Collaborative Filtering (HCCF, SIGIR 2022) combines hypergraph convolution with "
         "self-supervised contrastive objectives; Hypergraph Projection Improved Collaborative Filtering (HPCF, 2025) "
         "improves how hypergraph structure is projected into the node space. In this thesis HPCF is plainly the "
         "strongest reference point: NDCG@20 = 0.2528 on MovieLens-1M and 0.0270 on Amazon-Book, the numbers DyHuCoG "
         "has to beat.",
 "why": "Beating a 2025 state-of-the-art hypergraph model, and not a weak baseline, is the core empirical claim of "
        "Contribution III. HPCF also supplies the denominator of every percentage on slides 58 and 59.",
},
{
 "term": "Contrastive learning and RecDCL", "tag": "Recommenders", "where": "slides 23, 57",
 "plain": "Train the model to pull two views of the same interaction together and push random pairs apart.",
 "deep": "Contrastive objectives (for example InfoNCE) create a self-supervised signal: two corrupted or augmented "
         "views of the same user-item relation should have similar embeddings, while unrelated samples should not. "
         "It improves robustness on sparse data without extra labels. RecDCL applies dual contrastive learning at "
         "the graph level for recommendation (The Web Conference, 2024).",
 "why": "RecDCL is the newest architectural baseline in the comparison (NDCG@20 = 0.2296 on MovieLens-1M), so the "
        "claim to beat includes a 2024 method, not only classical ones.",
},
{
 "term": "Embedding", "tag": "Recommenders", "where": "slides 11, 22, 54",
 "plain": "A learned vector of numbers that represents an entity (a user, an item, a context) so the model can "
          "compute similarities and scores with it.",
 "deep": "Almost every modern recommender works in embedding space: two entities are 'similar' when their vectors "
         "point in similar directions. This is powerful and, by itself, unreadable: dimension 37 of an item vector "
         "has no name. The thesis's answer is not to abandon embeddings, but to attribute importance to *named* "
         "inputs (features, contexts, entities) and to use embeddings only where they are needed.",
 "why": "The latent-versus-original distinction is the reason Contribution I insists on returning the explanation "
        "in the original eleven wine variables rather than in principal components.",
},
{
 "term": "Attention, and the attention gate in DyHuCoG", "tag": "Recommenders", "where": "slide 56",
 "plain": "A mechanism that learns how much weight to give each part of the input; the gate is a small such weight "
          "computed for each user-item interaction.",
 "deep": "Attention produces a score in [0,1] that reweights a contribution. In DyHuCoG the gate is "
         "`a_ui = σ(W_a [e_u, e_i, l_i])`, where `l_i` is the item-context representation; the intermediate score "
         "becomes `y_ui = (1 + a_ui)⟨e_u, e_i⟩`. Conceptually the gate interpolates between Shapley-weighted "
         "propagation and a more uniform propagation. Its role is robustness: in early training the Shapley "
         "estimates are still noisy, so the model is allowed to lean on them less; as they stabilise, the gate can "
         "shift the balance.",
 "why": "The ablation removes the gate and loses 3.5 % NDCG@20 on both datasets — the smallest drop of the five "
        "components, which is exactly what a stabiliser should cost. And the difference between 'attention learns "
        "importance implicitly' and 'Shapley allocates it under axioms' is the novelty claim of the chapter.",
},
{
 "term": "Context and ContextScore", "tag": "Recommenders", "where": "slides 21, 54, 56, 60, 65",
 "plain": "Extra information about the situation of an interaction — here the genre of a movie or the category of "
          "a book — that modifies how relevant an item is.",
 "deep": "A context is whatever surrounds an interaction: time, place, mood, season, device, category. The thesis "
         "uses genre (MovieLens-1M) and book category (Amazon-Book) as context proxies, and encodes context as a "
         "node in the hypergraph, so it can be a player in the cooperative game. ContextScore(S) is the mean "
         "context-alignment score of the entities in a coalition: the average embedding-space alignment between the "
         "learned context representation and the context node of the episode. It is one of the three terms of the "
         "coalition utility, and it also appears as a loss term that keeps recommended items coherent with the "
         "contextual state.",
 "why": "Remove context and NDCG@20 drops 8.2 % on MovieLens-1M and 11.0 % on Amazon-Book — the largest drop of "
        "any component. Slide 65 then states the consequence honestly: on data without usable context, the gain of "
        "the whole method would shrink.",
},
{
 "term": "The composite loss and regularisation", "tag": "Recommenders", "where": "slides 56, 61",
 "plain": "The single objective the model minimises, made of four terms added together: ranking, diversity, "
          "context and regularisation.",
 "deep": "Written as `L = L_BPR + λ_div L_div + λ_ctx L_ctx + λ_reg L_reg`. The first term is the pairwise ranking "
         "loss. The second is the negative mean intra-list diversity, so minimising it *increases* diversity. The "
         "third penalises the distance between the encoded context and the context node representation. The fourth "
         "is an L2 penalty on the parameters, which controls overfitting. Each λ is a hyperparameter weighting one "
         "concern against the others. Having all four in one differentiable objective is what makes joint training "
         "possible: there is no post-hoc re-ranking step.",
 "why": "Because diversity and context appear both in the loss and in the coalition utility, the explanation the "
        "model produces reports the same terms it optimises — the property the deck calls 'faithful by design'.",
},
{
 "term": "Catalogue coverage and intra-list diversity as objectives", "tag": "Recommenders", "where": "slides 24, 58, 59, 60",
 "plain": "Coverage measures how much of the whole catalogue the system ever recommends; intra-list diversity "
          "measures how different the items inside one recommendation list are.",
 "deep": "Both are diversity measures at different granularities: coverage is system-level (which items get any "
         "exposure at all), ILD is list-level (are the twenty items in front of me varied). A system that only ever "
         "recommends blockbusters can have excellent ranking accuracy and terrible coverage. Treating diversity as "
         "a *training* objective rather than a post-hoc re-ranking rule is a design decision with a measurable "
         "effect: DyHuCoG raises coverage and ILD while also raising NDCG and Recall, while most accuracy-first "
         "models show a trade-off.",
 "why": "The joint improvement is the empirical answer to RQ4 and appears in every results table. It is also why "
        "the ablation keeps the diversity term as a separate row (−5.8 % on both datasets when removed).",
},

# ------------------------------------------------------------------- metrics
{
 "term": "NDCG@K (normalised discounted cumulative gain)", "tag": "Metrics", "where": "slides 24, 57, 58, 62",
 "plain": "A ranking score that rewards putting relevant items near the top of the list, discounted by position.",
 "deep": "You compute DCG@K = Σ 2^rel_i − 1 over log₂(i+1) for the first K positions, then divide by the best "
         "possible value IDCG@K to get a number in [0,1]. With binary relevance (as here, where an implicit "
         "interaction counts as relevant) the numerator is a sum of 1/log₂(i+1) terms over the positions where a "
         "relevant item sits. Two consequences matter: position 20 counts roughly four times less than position 1, "
         "and a relevant item placed nowhere in the top K contributes zero, so NDCG@20 measures both retrieval and "
         "ordering.",
 "why": "NDCG@20 is the thesis's main measure and the metric on which the paired significance tests are run "
        "(per user, MovieLens-1M, df = 6,039). Every headline percentage on slides 58 and 59 is a relative change "
        "in NDCG@20 or Recall@20.",
},
{
 "term": "Recall@K", "tag": "Metrics", "where": "slides 24, 58, 59",
 "plain": "The share of a user's relevant items that actually appear in the top-K list.",
 "deep": "Where NDCG cares about order, Recall cares about coverage of the user's relevant set: did we find the "
         "items at all? In many implicit-feedback protocols each user has a single held-out target, and Recall@K "
         "becomes a hit-rate: was the target in the list? The thesis runs both, which is why a model can improve "
         "both metrics at once (items are both found and ranked higher).",
 "why": "Recall@20 improves from 0.2098 to 0.2362 on MovieLens-1M (+12.6 %) and from 0.0359 to 0.0417 on "
        "Amazon-Book (+16.2 %) — the second half of every results slide.",
},
{
 "term": "Precision@K (and why it is not on the metrics slide)", "tag": "Metrics", "where": "not shown in v32",
 "plain": "The share of the K recommended items that are relevant.",
 "deep": "Precision answers the complementary question to Recall: how much of what I showed was wanted? With "
         "binary implicit feedback and leave-one-out evaluation it is largely determined by Recall (with 1 relevant "
         "item, Precision@20 = Recall@20/20), which makes it redundant in this protocol.",
 "why": "An earlier version of the deck listed it; v25 removed the row because the metric is not tabulated in the "
        "results. If a jury member asks, this redundancy is the reason, and it is a good answer.",
},
{
 "term": "Silhouette coefficient", "tag": "Metrics", "where": "slides 24, 32, 44",
 "plain": "For one point, how much closer it is to its own cluster than to the nearest other cluster, on a scale "
          "from −1 to +1.",
 "deep": "For point x, `s(x) = (b(x) − a(x)) / max(a(x), b(x))` where a(x) is the mean distance to the other points "
         "in its own cluster and b(x) is the smallest mean distance to any other cluster. Averaging over all points "
         "gives the clustering's Silhouette. Values near 1 mean compact, well-separated clusters; values near 0 mean "
         "overlapping ones; negative values mean points may be in the wrong cluster. It is a geometric criterion "
         "only: it says nothing about whether a partition is interpretable or useful.",
 "why": "Silhouette is doing two jobs in the thesis. It is the clustering-quality metric (wine 0.144 at k = 3, "
        "Beijing 0.63), and it is the value function of the cooperative game in C1 — the thing being shared among "
        "the features.",
},
{
 "term": "Davies–Bouldin index", "tag": "Metrics", "where": "slides 24, 32, 43, 44",
 "plain": "A measure of how much clusters overlap, where lower is better.",
 "deep": "For each cluster you find the worst case — the most similar other cluster, measured by the ratio of "
         "within-cluster spread to between-cluster distance — and average those worst cases. A DB of 0 means "
         "perfectly separated; larger values mean more overlap. It uses a different geometry from Silhouette "
         "(distance ratios instead of point-wise neighbourhoods), which is exactly why the thesis uses both and "
         "reports them together: agreement between the two is weak evidence, disagreement is a warning.",
 "why": "The wine k-selection table pairs Silhouette with DB for k = 2 (0.214 / 1.775) and k = 3 (0.144 / 2.097), "
        "and Beijing reports DB ≈ 0.55 alongside Silhouette ≈ 0.63.",
},
{
 "term": "K ∈ {5, 10, 20} and why @20 is the main measure", "tag": "Metrics", "where": "slide 24",
 "plain": "Every ranking metric is computed at several list lengths; the thesis reports the top twenty as its "
          "headline.",
 "deep": "Longer lists are easier for Recall (more chances to hit) and harder for NDCG (irrelevant items dilute "
         "the top). Reporting K = 5, 10 and 20 shows that a gain is not an artefact of one cut-off. @20 is the "
         "headline because the recommendation task is 'what to show next', where twenty candidates is a realistic "
         "page, and because the coalition utility itself is built on NDCG@20.",
 "why": "The choice is not cosmetic: the value function of the DyHuCoG game is α·NDCG@20(S) + …, so the metric and "
        "the training signal are the same object evaluated at the same cut-off.",
},

# ---------------------------------------------------------------- statistics
{
 "term": "p-value", "tag": "Statistics", "where": "slides 62, 78",
 "plain": "The probability of seeing a difference at least this large if there were really no difference.",
 "deep": "A p-value is not the probability that the null hypothesis is true, and it is not a measure of how big "
         "the effect is. It depends on sample size: with 6,040 users, trivially small differences become "
         "significant. That is exactly why the thesis reports effect sizes next to p-values: significance says "
         "'this is unlikely to be noise', the effect size says 'and it is worth caring about'.",
 "why": "The headline p-value is 1.81×10⁻²⁷⁰ for DyHuCoG versus HPCF. It is a formality; the sentence that "
        "matters is the effect size, dz = 1.33, and the +9.8 % NDCG gain behind it.",
},
{
 "term": "Paired t-test on per-user results", "tag": "Statistics", "where": "slides 57, 62, 78",
 "plain": "Compare the two models user by user, then test whether the average of the individual differences is "
          "distinguishable from zero.",
 "deep": "A two-sample test compares two averages and must absorb all the variation between users. A paired test "
         "removes that variation by looking at each user's own difference: `t = mean(d) / (sd(d)/√n)`. Because "
         "users differ hugely in how predictable they are, pairing gives a far more sensitive test. With n = 6,040 "
         "users the test has df = n − 1 = 6,039 degrees of freedom.",
 "why": "It is the primary significance test in the thesis, and the reason the p-values are so extreme: the same "
        "users, the same splits, and only the model changes.",
},
{
 "term": "Wilcoxon signed-rank test", "tag": "Statistics", "where": "slides 62, 78",
 "plain": "A paired test that uses the ranks of the differences instead of their sizes, so it does not assume "
          "normally distributed differences.",
 "deep": "The paired t-test assumes the per-user differences are roughly normal. Per-user NDCG differences need "
         "not be. Wilcoxon sorts the absolute differences, ranks them, and tests whether the positive and negative "
         "ranks balance. It loses some power when the t-test's assumption does hold, and gains robustness when it "
         "does not.",
 "why": "Reporting both is a standard defence: the deck states that Wilcoxon agrees at p < 0.001, so the "
        "conclusion does not depend on the normality assumption.",
},
{
 "term": "Holm–Bonferroni correction and the family-wise error rate", "tag": "Statistics", "where": "slides 57, 62, 78",
 "plain": "When you run several significance tests at once, correct the thresholds so that the chance of at least "
          "one false positive stays under 5 %.",
 "deep": "Six comparisons at α = 0.05 each give a family-wise error rate well above 5 %. Holm's procedure sorts "
         "the six p-values ascending and compares the k-th smallest with α/(m − k + 1), rejecting from the top and "
         "stopping at the first failure. The thresholds for m = 6 are 0.00833, 0.0100, 0.0125, 0.0167, 0.0250 and "
         "0.0500 — the numbers on backup slide 78. It is uniformly more powerful than plain Bonferroni, which would "
         "use 0.05/6 for every comparison.",
 "why": "The deck states that all six comparisons survive correction, with the largest row-level p-value still "
        "far below its threshold. This is the answer to 'did you correct for multiple comparisons?' — question "
        "F13.",
},
{
 "term": "Cohen's dz and effect size", "tag": "Statistics", "where": "slides 62, 64, 78",
 "plain": "How large the difference is, measured in units of the variability of the differences.",
 "deep": "Cohen's dz for paired data is the mean difference divided by the standard deviation of the differences. "
         "The conventional reading is 0.2 small, 0.5 medium, 0.8 large. Unlike a p-value it does not grow "
         "automatically with sample size, so it answers the question a jury actually cares about: is this "
         "improvement practically meaningful?",
 "why": "dz ≥ 1.33 in every one of the six comparisons, and 1.33 against the strongest baseline. That is an "
        "unusually large effect, and it is the honest counterweight to the extreme p-values.",
},
{
 "term": "Standard deviation over seeds and the ±1σ band", "tag": "Statistics", "where": "slides 57, 77",
 "plain": "Run the whole experiment with five different random seeds and report the mean plus or minus the spread.",
 "deep": "Neural recommenders are sensitive to initialisation, sampling and batch order, so a single run can be "
         "lucky. Five seeds give a mean and a standard deviation; a ±1σ band is a rough visual test of "
         "separability between two models. It is not a confidence interval and overlapping bands are not proof of "
         "no difference — which is why the thesis also runs paired tests.",
 "why": "Slide 77 shows the bands: they never overlap between DyHuCoG and HPCF on MovieLens-1M, and on Amazon-Book "
        "they nearly touch for NDCG@20 and Recall@20, which is exactly why those two gains are called descriptive.",
},
{
 "term": "Sensitivity analysis", "tag": "Statistics", "where": "slides 43, 44",
 "plain": "Re-run the analysis with slightly different settings to check that the conclusion does not depend on "
          "one arbitrary choice.",
 "deep": "In C2 the settings varied are the number of clusters, the projection dimension and the surrogate tree "
         "depth. The reported outcome is nuanced: conclusions are robust, with changes concentrated in "
         "low-ranked variables while the leading drivers stay stable. This is a more credible claim than "
         "'nothing changes at all'.",
 "why": "It is the pre-emptive answer to 'is your Beijing result an artefact of k = 3?' — question D7.",
},

# ------------------------------------------------------------------- theory
{
 "term": "Nested (strict) hierarchy", "tag": "Theory", "where": "slides 41, 42",
 "plain": "A tree of clusters in which every child belongs to exactly one parent and the children of a parent "
          "cover it completely.",
 "deep": "The strictness matters: if a child could belong to two parents, or if some records were unassigned, the "
         "children would no longer form a partition of the parent, and the law of total expectation could not be "
         "applied. The thesis also says plainly that the hierarchy is an analytical device, not a claim that "
         "nature is organised that way.",
 "why": "Proposition 6.1 is stated under exactly this condition: 'for a strict nested hierarchy on a consistent "
        "feature space'. If asked about the hypothesis, that is the answer — question D5.",
},
{
 "term": "Law of total expectation", "tag": "Theory", "where": "slide 42",
 "plain": "The average of a quantity over a whole group equals the size-weighted average of its averages over the "
          "subgroups.",
 "deep": "Formally, E[X] = Σ P(c′) · E[X | c′] when the c′ partition the space. It is the entire engine of "
         "Proposition 6.1: expected absolute importance inside a parent is the weighted average of expected "
         "absolute importance inside its children, provided both levels measure the same quantity on the same "
         "feature space. No deeper theorem is needed — and the thesis is careful to say so.",
 "why": "It explains why cross-level aggregation must be size-weighted rather than a plain mean, and why the "
        "residual ε exists: the two levels do not measure exactly the same quantity, because they use different "
        "surrogates.",
},
{
 "term": "The residual ε", "tag": "Theory", "where": "slides 42, 47",
 "plain": "The gap in Proposition 6.1 caused by the fact that the parent and child explanations come from "
          "different surrogate models.",
 "deep": "With perfect fidelity the identity holds exactly. In practice each level has its own LightGBM surrogate, "
         "so the quantity being averaged at level ℓ is not literally the same random variable as the one at level "
         "ℓ+1; the difference shows up as ε. The thesis is explicit that ε is a conceptual residual, not an "
         "empirically estimated quantity, because a separate Beijing-level residual analysis is not reported, and "
         "that the result is a bounded accounting identity rather than a general invariance theorem.",
 "why": "This is the most sophisticated honesty in the thesis. Say it exactly like that if asked, and you will "
        "have answered question D6 better than most candidates could.",
},
{
 "term": "Unanimity games and the uniqueness proof", "tag": "Theory", "where": "Appendix A.1, slides 29, 34",
 "plain": "A short argument showing that the four axioms leave exactly one possible attribution rule.",
 "deep": "The proof takes the 'unanimity games' u_T, where a coalition earns 1 only if it contains all of T. Every "
         "game is a unique weighted sum of such games. The null-player axiom forces the value to be zero outside T, "
         "symmetry forces it to be equal inside T, and efficiency forces each member to get 1/|T|. Because the "
         "candidate rule and the Shapley value agree on every basis element and both are additive, they agree "
         "everywhere. That is the whole proof, and it is why 'the only rule satisfying all four axioms' is a "
         "statement you can defend rather than a slogan.",
 "why": "It is the formal backing of objective O3 in Contribution I: Shapley is justified over LIME by uniqueness "
        "under axioms, not by a benchmark.",
},
{
 "term": "Proposition versus theorem", "tag": "Theory", "where": "slides 40, 42, 47",
 "plain": "A proposition is a proved statement, but a smaller one than a theorem — usually local to a chapter and "
          "resting on stated conditions.",
 "deep": "The distinction is not decorative. Calling 6.1 a proposition is a claim about its scope: it holds under "
         "the conditions stated (strict nesting, consistent feature space, surrogate fidelity) and within this "
         "thesis's setting. The thesis says so in as many words: it is 'an original thesis-level formalisation "
         "layered on top of the empirical multi-level framework', to be read as 'a careful formal clarification', "
         "not 'a stand-alone general theory of hierarchical Shapley consistency'.",
 "why": "If a jury member asks 'isn't that just the law of total expectation?', the right answer is yes — the "
        "formal content is the accounting identity plus the residual, and the value is that it makes cross-level "
        "differences interpretable in a setting where nobody had written the relation down.",
},

# --------------------------------------------------------------- governance
{
 "term": "The EU AI Act, Articles 13 and 86", "tag": "Governance", "where": "slides 4, 6, 72",
 "plain": "The European regulation that puts transparency duties on high-risk AI systems and gives affected "
          "people a route to contest decisions.",
 "deep": "Article 13 concerns transparency and the provision of information to deployers of high-risk systems; "
         "Article 86 concerns the right to an explanation of an individual decision in certain cases. The deck's "
         "careful wording - 'high-risk systems have transparency duties' and 'decisions can be challenged' - is "
         "deliberately narrower than the popular version, which claims the Act mandates explanations everywhere. "
         "This matters in a viva, because a jury member who knows the regulation will test exactly that drift.",
 "why": "It is the motivation for the whole thesis at the governance level, and it appears in the closing claim "
        "as alignment with trustworthy-AI expectations. Say it as a direction of travel, not as a legal "
        "obligation you have verified for every system.",
},
{
 "term": "GDPR Article 22 and the OECD AI Principles", "tag": "Governance", "where": "slides 4, 72",
 "plain": "The data-protection rule on automated decision-making, and the international policy principles on "
          "trustworthy AI.",
 "deep": "GDPR Article 22 limits decisions based solely on automated processing when they produce legal or "
         "similarly significant effects, and gives a right to get human intervention. The OECD principles "
         "define the policy vocabulary - human-centred values, transparency and explainability, robustness, "
         "accountability - that most national AI frameworks reuse. Together they make explanation a governance "
         "expectation rather than a research preference.",
 "why": "Slide 72 lists all three instruments as the alignment of the thesis's outcome 4. It is also the answer to "
        "'why does this matter outside computer science?' — question G11.",
},
{
 "term": "Trustworthy AI", "tag": "Governance", "where": "slides 66, 71, 72",
 "plain": "The policy expectation that an AI system be not only accurate but also transparent, fair, robust and "
          "accountable.",
 "deep": "Trustworthy AI is a broad framing with several pillars; explanation is one of them, and it is the pillar "
         "this thesis works on. The thesis does not claim to deliver fairness or robustness — it delivers a "
         "principled attribution method and shows that it can also be used as a training signal. Its fairness "
         "content is indirect: Shapley's symmetry and null-player axioms guarantee that equivalent players are "
         "treated equally and irrelevant ones are not credited.",
 "why": "Slide 66 calls the in-training signal 'in line with trustworthy-AI expectations', and slide 71 lists "
        "exposure fairness and auditing as future work. That is the honest boundary: axioms about attribution, "
        "not a claim about social fairness.",
},
{
 "term": "Post-hoc versus in-training attribution", "tag": "Explainability", "where": "slides 6, 36, 49, 52, 66, 70",
 "plain": "Post-hoc explanation describes a model after it is trained; in-training attribution is computed during "
          "learning and shapes the model itself.",
 "deep": "Post-hoc methods are attractive because they work on any model you already have, and limited because "
         "they cannot change what the model does. In-training attribution reverses the dependency: the importance "
         "signal is part of the objective, so the explanation is a read-out of what the model optimises rather "
         "than an external reconstruction. The price is computation (about 1.78× training time here) and a "
         "dependence on the approximation quality of the importance estimates during training.",
 "why": "The post-hoc to in-training move is the single narrative of the thesis — explain (C1), scale (C2), guide "
        "(C3) — and every limitations slide marks where the move stops.",
},
{
 "term": "Null and alternative hypothesis", "tag": "Statistics", "where": "slides 62, 78",
 "plain": "H0 is the boring world where the two models are equal; H1 is the claim that they are not.",
 "deep": "A statistical test never proves H1; it only reports how incompatible the observed data are with H0. "
         "Here H0 says the mean of the per-user NDCG@20 differences is zero. The test computes how extreme the "
         "observed mean difference would be in a world where that holds. Because H1 is two-sided — the mean is "
         "not zero, in either direction — the direction of the gain is read from the sign of the mean difference, "
         "not baked into the test.",
 "why": "The thesis claims DyHuCoG beats six baselines on MovieLens-1M; the paired tests on slides 62 and 78 are "
        "the formal version of that claim, one H0 per baseline.",
},
{
 "term": "Type I and Type II errors, and power", "tag": "Statistics", "where": "slides 62, 78",
 "plain": "A Type I error is crying wolf — claiming a gain that is really noise. A Type II error is missing a "
          "real gain.",
 "deep": "The significance level α bounds the Type I error per test. When six tests are run at α = 0.05, the "
         "chance of at least one false positive in the family rises well above 5 % — the family-wise error rate "
         "problem — and Holm–Bonferroni is what brings it back to 5 %. Type II risk shrinks with sample size "
         "(statistical power grows); with 6,040 paired users, power against a large effect is very high, so "
         "neither error is likely in this protocol.",
 "why": "If asked 'what error are you controlling?', the answer is: Type I, across the family of six comparisons, "
        "through Holm — stated implicitly by the correction table on backup slide 78.",
},
{
 "term": "Degrees of freedom (df)", "tag": "Statistics", "where": "slides 62, 78",
 "plain": "How many independent numbers the test is actually working with.",
 "deep": "For the paired t-test on n differences, one degree of freedom is consumed by estimating the mean, so "
         "df = n − 1. With 6,040 users that is 6,039. The df fixes the exact shape of the t distribution used to "
         "convert the statistic into a p-value; at this size the t distribution is almost identical to the normal "
         "distribution, but the thesis reports df correctly anyway.",
 "why": "'df = 6,039' and 'n = 6,040' always travel together on slides 78 and 62 — never quote one without the "
        "other.",
},
{
 "term": "One-tailed versus two-tailed", "tag": "Statistics", "where": "slide 78",
 "plain": "A one-tailed test only counts surprises in one direction; a two-tailed test counts surprises in both.",
 "deep": "A two-sided test — used here — asks whether the mean difference is not zero, in either direction, and "
         "splits α across both tails. A one-tailed test would be justified only if the direction of the effect "
         "were fixed in advance and a large effect in the opposite direction would be treated as no finding. "
         "Two-sided is the convention in the field and is the more conservative choice, so the thesis uses it.",
 "why": "If the jury asks which one you used: two-sided. Then note that the observed t is positive and enormous, "
        "so the tail choice changes nothing about the conclusion.",
},
{
 "term": "Normality and the central limit theorem", "tag": "Statistics", "where": "slides 62, 78",
 "plain": "The t-test assumes the differences are roughly bell-shaped; with thousands of users the average is "
          "bell-shaped almost automatically.",
 "deep": "The exact assumption is about the distribution of the per-user differences, not of the raw NDCG values. "
         "The central limit theorem says that with a large sample the sampling distribution of the mean is close "
         "to normal even when the differences themselves are not. The thesis adds the Wilcoxon signed-rank test — "
         "which ranks the differences and assumes no normality — as a robustness check; it agrees at p < 0.001.",
 "why": "'Is the normality assumption safe?' — answer: large n plus the central limit theorem, and the "
        "distribution-free Wilcoxon agrees; the conclusion does not depend on the assumption.",
},
{
 "term": "Confidence interval", "tag": "Statistics", "where": "slides 62, 78",
 "plain": "A range of plausible values for the real average gain, not just a yes/no verdict.",
 "deep": "A 95 % confidence interval for the mean paired difference is mean(d) ± t* · sd(d)/√n, with t* from the "
         "t distribution at n − 1 degrees of freedom. It conveys precision and size in one number pair, which a "
         "p-value cannot do. The thesis tabulates means, standard deviations and Cohen's dz instead; intervals "
         "follow from the same reported quantities.",
 "why": "If asked for intervals: they are not tabulated, they are computable from the reported statistics, and "
        "reporting them is future work — the future-work rule, in its cleanest form.",
},
]
