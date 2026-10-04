# -*- coding: utf-8 -*-
"""Concept walkthroughs and beginner glossary part A (learning, clustering, XAI, game theory, trees)."""

from content_tech_b import GLOSSARY_B


def render_intro():
    return """
<section class="sec" id="tech-intro">
  <div class="sec-head"><div class="sec-kicker">Part three</div><h2>Technical deep dive for sections 3, 4, 5 and 6</h2>
  <div class="sec-meta"><span class="pill">86 glossary entries</span><span class="pill g">12 worked walkthroughs</span>
  <span class="pill o">written for a reader who has never built a model</span></div></div>
  <p>Everything the deck says in sections 3 to 6 is technical, and the viva will test whether you can unpack it.
  This part of the guide does that unpacking in two layers. The <strong>walkthroughs</strong> take the twelve ideas
  that carry the contributions — the Shapley average, the axioms, the surrogate bridge, the cross-level identity,
  Monte Carlo estimation, hypergraph propagation, the composite loss, the statistical tests, NDCG — and work them
  through by hand. The <strong>glossary</strong> then covers every remaining term that appears on the slides, in the
  speaker notes or in a jury question, in three lines each: what it means, how it works, and what it is doing in
  this specific thesis.</p>
  <div class="callout"><h4>How to use this part in the last days before the defence</h4>
  <p>Do not read it front to back. Read the walkthrough for the slide you find hardest, then use the glossary entry
  as your spoken definition when the term comes up. A definition that takes three sentences and contains one number
  is the right length in a viva; a definition that takes thirty seconds invites an interruption.</p></div>
  <div class="grid3">
    <div class="stat"><b>4</b><span>sections given the full deep-dive treatment: the shared protocol (3), and the three contributions (4, 5, 6).</span></div>
    <div class="stat"><b>86</b><span>terms explained, from “black box” to “Cohen's dz”, each with its place in this thesis.</span></div>
    <div class="stat"><b>12</b><span>worked walkthroughs with numbers you can reproduce on a whiteboard if the jury asks.</span></div>
  </div>
</section>
"""


# ==========================================================================
# WALKTHROUGHS
# ==========================================================================
WALKTHROUGHS = [
{
 "title": "1 · The three-piece band: a Shapley value computed the long way",
 "lede": "Slide 29 uses a band of three players. This is the full arithmetic behind the numbers 90 / 70 / 40, "
         "including the coalition the slide does not have room to show.",
 "body": """
The easiest way to understand a Shapley value is to stop thinking about formulas and to imagine that the players
arrive in a random order, each one adding whatever it adds to the group already present. The Shapley value is the
average of what a player adds over all possible arrival orders.

**The game.** Three musicians: Guitar (G), Voice (V), Drums (D). The characteristic function says what each group
can earn on its own:

- `v(G) = 60` — a solo guitar act earns 60.
- `v(V) = 40` — a solo voice earns 40.
- `v(D) = 20` — solo drums earn 20.
- `v(G,V) = 140` — guitar and voice together.
- `v(G,D) = 100` — guitar and drums together. *This row is not on the slide (no space in the table); it is in the
  speaker note and it is needed for the arithmetic.*
- `v(V,D) = 80` — voice and drums together.
- `v(G,V,D) = 200` — the whole band.

**All six arrival orders.** For each order, write down what each player adds at the moment they arrive:

1. G, V, D — G adds 60; V raises 60 → 140, so V adds 80; D raises 140 → 200, so D adds 60.
2. G, D, V — G adds 60; D raises 60 → 100, so D adds 40; V raises 100 → 200, so V adds 100.
3. V, G, D — V adds 40; G raises 40 → 140, so G adds 100; D adds 60.
4. D, G, V — D adds 20; G raises 20 → 100, so G adds 80; V adds 100.
5. V, D, G — V adds 40; D raises 40 → 80, so D adds 40; G raises 80 → 200, so G adds 120.
6. D, V, G — D adds 20; V raises 20 → 80, so V adds 60; G raises 80 → 200, so G adds 120.

**Average each column.**

- Guitar: (60 + 60 + 100 + 80 + 120 + 120) / 6 = 540 / 6 = **90**.
- Voice: (80 + 100 + 40 + 100 + 40 + 60) / 6 = 420 / 6 = **70**.
- Drums: (60 + 40 + 60 + 20 + 40 + 20) / 6 = 240 / 6 = **40**.

**Check efficiency:** 90 + 70 + 40 = 200 = v(N). The band's total is fully allocated. That is not a coincidence; it
is the efficiency axiom, which the slide's orange bar mentions and which no other allocation rule guarantees in the
same way.

**Transfer to the thesis.** Players are the eleven wine variables (or the eleven air-quality variables). The value
function is the Silhouette of the clustering computed on the subset of variables in the coalition. A Shapley value
for "density" is so the average amount by which the clustering's separation improves when density joins a
group of variables, averaged over every possible order in which variables could be introduced. That is the sentence
to say if a jury member asks what your explanation actually measures.
""",
},
{
 "title": "2 · Why the Shapley formula has those factorials in it",
 "lede": "The formula looks arbitrary the first time. It is not: the coefficient is the probability that a random "
         "arrival order puts exactly the coalition S before player j.",
 "body": """
The definition is

`φ_j(v) = Σ over S ⊆ N \\ {j} of  [ |S|! · (n − |S| − 1)! / n! ] · [ v(S ∪ {j}) − v(S) ]`.

Read the bracket in the middle first: `v(S ∪ {j}) − v(S)` is the **marginal contribution** of j to the coalition S.
The Shapley value is a weighted average of these marginal contributions, where the weight is the probability that,
in a uniformly random arrival order of all n players, the players already present are exactly the set S.

Why that probability? Fix n players and a random permutation. The set of players arriving before j has size |S|,
and there are |S|! ways to order them and (n − |S| − 1)! ways to order the players arriving after j; dividing by the
n! possible orders gives the weight. For three players the weights are easy to check:

- |S| = 0: weight = 0!·2!/3! = 2/6 = 1/3.
- |S| = 1: weight = 1!·1!/3! = 1/6 for each of the two singleton sets.
- |S| = 2: weight = 2!·0!/3! = 2/6 = 1/3.

The three cases sum to 1/3 + 2·(1/6) + 1/3 = 1, as they must: every arrival order is counted exactly once.

This is also the bridge to the Monte Carlo estimator used in Contribution III. If the Shapley value is an average
over orders, you do not need to enumerate all orders; you can **sample** some of them and average. Slide 55 does
exactly that, with M = 50 permutations. For 30 players, the exact version needs on the order of 10⁹ coalition
evaluations; the sampled version needs 50 marginal-contribution evaluations per player per refresh, which is the
difference between impossible and real time.
""",
},
{
 "title": "3 · The four axioms, and what breaks without them",
 "lede": "The deck says Shapley is 'the only allocation satisfying all four axioms at once'. Here is what each axiom "
         "buys, and what happens with the alternatives.",
 "body": """
**Efficiency.** The shares sum to the total value: Σ φ_j = v(N) − v(∅). In an explanation this means the attributions
account for the entire output. If a model's prediction is 0.8 above the average and the top three features have
SHAP values 0.4, 0.2 and 0.1, the remaining 0.1 is distributed among the others. Nothing is left unexplained.

**Symmetry.** Two players that contribute identically to every possible coalition receive the same value. This is
what makes cross-feature and cross-cluster comparisons legitimate: two variables with identical marginal behaviour
cannot receive different credit.

**Null player.** A player that adds nothing to any coalition receives zero. This is the axiom that prevents
attributing importance to a variable that is irrelevant to the outcome — the exact failure mode of methods that
inherit importance from correlations in the data.

**Additivity.** For two games v and w, φ(v + w) = φ(v) + φ(w). Explanations compose: if the model output is a sum
of components, the attributions of the components add up to the attribution of the sum. This is why SHAP values can
be aggregated from individual predictions into global importance without losing their meaning.

**What breaks without them.** The Banzhaf index also averages marginal contributions, but in its standard form it
does not satisfy efficiency, so its attributions need not sum to the total — for a thesis that treats completeness as
a design requirement, that is disqualifying. The nucleolus comes from cooperative bargaining, not from additive
feature attribution, so it is less natural here. LIME fits a local linear model to perturbed samples: it is flexible
and intuitive, but its explanation depends on how the neighbourhood was defined and how the perturbations were
generated, and it offers no guarantee that credit is fair (symmetry) or that irrelevant features get zero
(null player).

**The uniqueness result.** It is not enough that Shapley satisfies the four axioms; the thesis's Appendix A.1 proves
that it is the *only* rule that does. That proof is the entire formal content of objective O3 in Contribution I:
the justification of Shapley over LIME is axiomatic, not empirical — and the deck says so in as many words.
""",
},
{
 "title": "4 · The surrogate bridge: why TreeSHAP cannot touch K-Means",
 "lede": "This is the most frequently asked methodological question in the whole viva, so here is the whole argument, "
         "with its cost stated.",
 "body": """
**The problem.** SHAP comes in several implementations, and the fast exact one, TreeSHAP, works only for tree-based
models. It exploits the structure of a decision tree to compute exact Shapley values of the model's output in
polynomial rather than exponential time. K-Means is not a tree: it is a set of centroids and a distance function.
There is no TreeSHAP for centroids.

**Three ways out, and why two are rejected.**

- *KernelSHAP on K-Means directly.* Model-agnostic, so it works in principle, but it estimates Shapley values by
  sampling coalitions and fitting a weighted linear model. On 4,898 samples with 11 features it is feasible; the
  thesis's reason for not using it is the cost-quality trade-off at the scale of the Beijing study and the desire for
  exact attribution rather than a second layer of sampling.
- *Explain the PCA representation.* PCA components are linear combinations of the original variables, so an
  attribution in that space cannot be read as "density" or "sulphates". It would break the actionability requirement
  of Definition 1.1.
- *Train a surrogate.* Fit a LightGBM multiclass classifier to predict the cluster labels from the original
  features, then apply exact TreeSHAP to that classifier. The explanation is expressed in the original eleven
  variables, and the computation is fast and exact for the surrogate.

**The cost, stated honestly.** You are now explaining the surrogate, not K-Means. The thesis says this plainly:
"the chapter does not claim to explain K-Means geometry in a mechanistic sense; it explains a faithful supervised
reconstruction of the discovered partition." The explanation is valid to the extent that the surrogate reconstructs
the partition, which is why the thesis imposes a fidelity floor: macro-F1 around 0.82 for a 100-tree, 31-leaf
LightGBM, with the practical floor stated as roughly 0.80.

**One more subtlety worth knowing.** The efficiency axiom then holds with respect to the surrogate's log-odds output —
SHAP values sum to f(x) − E[f(x)] — and not with respect to the Silhouette-based game value directly. The Silhouette
game motivates the analysis; the surrogate is the tractable bridge to it. The thesis says these are two objects, and
the viva answer is to say the same thing: "I explain a faithful reconstruction of the partition, and the fidelity
floor is what keeps that bridge valid."
""",
},
{
 "title": "5 · How to read the three SHAP plots on the deck",
 "lede": "Slides 33, 45 and 46 show SHAP output. If you can describe what a dot, a colour and a bar mean, you can "
         "answer any figure question with confidence.",
 "body": """
**Global importance (mean absolute SHAP).** Each feature gets one bar, the average of the absolute SHAP values over
all instances. In the wine study the ranking is density, pH, fixed acidity, sulfur dioxide, alcohol; in Beijing it is
temperature, dew point and pressure, then CO, NO₂, PM10 and PM2.5. The bars tell you how much each variable moves the
model's output on average, and nothing about direction.

**Summary or beeswarm plot (Fig. 5.2, Fig. 6.3).** One dot per instance per feature. Horizontal position is the
SHAP value for that instance — how much this feature pushed this prediction up or down — and colour encodes the
feature's own value (typically red high, blue low). Reading a beeswarm answers questions the bar chart cannot: does
high density systematically push toward one cluster? Is a variable's effect consistent or split? If a jury asks
"what does a negative SHAP value mean here?", the precise answer is: this instance's value of the feature moved the
model's log-odds for that class *below* the average prediction, relative to the baseline, all else being equal in
the cooperative-game sense.

**Force plot (Fig. 6.2).** One instance, exploded. Contributions in one direction push the prediction up from the
base value (the average output), contributions in the other push it down, until they add to the instance's actual
output. It is the additive structure of SHAP made visual: the width of each segment is that feature's attribution,
and efficiency says the segments close the gap exactly.

**The caveat that earns credibility.** SHAP values live in the units of the model's output, here log-odds of the
multiclass surrogate, not in physical units and not in probabilities. So "density has the largest mean |SHAP|" means
"density moves the surrogate's decision most" — and the surrogate reproduces the partition, so density also moves
the membership decision most. Making that distinction out loud, unprompted, is one of the strongest things you can
do in the viva.
""",
},
{
 "title": "6 · Proposition 6.1 with real numbers",
 "lede": "A formal statement becomes memorable when you attach numbers to it. This is the two-child case, plus the "
         "consequence that makes the residual meaningful.",
 "body": """
**The claim.** For a strict nested hierarchy, the expected absolute importance of feature j in a parent cluster
equals the size-weighted average of the same quantity in its children, plus a residual:

`Φ_j^(level ℓ, cluster c) = Σ over children c′ of  w_c′ · Φ_j^(level ℓ+1, cluster c′) + ε_j`,  with `w_c′ = |c′| / |c|`.

**A concrete example.** Suppose a parent cluster c holds 1,000 records and is split into two children: c₁ with 600
and c₂ with 400. Suppose the expected absolute SHAP value of "temperature" is 0.10 inside c₁ and 0.20 inside c₂.

- Weights: w₁ = 600/1000 = 0.6, w₂ = 400/1000 = 0.4.
- Weighted average: 0.6 × 0.10 + 0.4 × 0.20 = 0.14.
- With perfect fidelity, ε = 0, so the parent's expected importance for temperature is 0.14.

**Two consequences worth understanding.**

1. *The parent value is a convex combination of the children's values.* It cannot lie outside the range of its
   children. If your reported parent importance for a feature is, say, 0.30 while the children are 0.10 and 0.20,
   then ε is doing real work — and the honest interpretation is surrogate mismatch between the two levels, not a
   mysterious new effect.
2. *Differences are still allowed and expected.* The identity is about the **expected absolute** importance, not
   about per-instance explanations, and not about the ranking of features. At the coarse level, temperature and dew
   point dominate because they separate the broad atmospheric regimes; inside a cluster, CO, SO₂, PM10, wind speed or
   ozone become more informative. Both statements can be true at once, and Proposition 6.1 is exactly what makes
   the pair non-contradictory.

**The scope, in the thesis's own words.** ε is "a conceptual residual term rather than an empirically estimated
quantity, because a separate Beijing-level residual analysis is not reported", and the proposition is "a bounded
accounting identity, not a general invariance theorem". If you say that sentence in the viva, you are quoting your
own thesis accurately and you cannot be cornered.
""",
},
{
 "title": "7 · Monte Carlo Shapley: what sampling buys, and what “M = 50” means",
 "lede": "Slide 55's table has four rows and looks harmless. Behind it is the difference between an unusable method "
         "and a trainable one.",
 "body": """
**Why exact is impossible.** With n players there are 2ⁿ coalitions. For the recommendation game, n is the number of
entities in a local episode: a focal user, a set of candidate items and their context nodes — on the order of a few
dozen entities. At n = 30, 2³⁰ is about a billion coalition evaluations, and the model would need them at every
refresh, for every episode, during training. Exact Shapley is not slow here; it is simply outside the problem.

**The estimator.** Sample M random permutations of the players. For each permutation, take player j's marginal
contribution: the value of the coalition formed by j and the players arriving before it, minus the value of that
coalition without j. Average the M numbers. This is the estimator on slide 55:

`φ̂_j = (1/M) Σ_{m=1..M} [ v(S_m ∪ {j}) − v(S_m) ]`.

**Why it is trustworthy.** The estimator is **unbiased**: its expected value is the true Shapley value, because each
sampled permutation is an equally likely arrival order and the average over all permutations is exactly the
definition. Its **variance** falls as σ²/M, so to halve the error you need four times the samples. This is the
"unbiased estimator: variance σ²/M" line on the slide, and it explains the shape of the convergence table: doubling
M from 25 to 50 and from 50 to 100 cuts the reported MSE by a factor of about four each time.

**Reading the table on the slide.**

- M = 25 → MSE ≈ 5.6×10⁻⁵, accuracy ≈ 98 %.
- M = 50 → MSE ≈ 1.4×10⁻⁵, accuracy ≈ 99 %. **This is the default.**
- M = 100 → MSE ≈ 3.5×10⁻⁶, accuracy ≈ 99.5 %, at about 2.5× the training cost.

**What "accuracy" means here — say this before you are asked.** It is agreement with a high-sample reference
estimate, not with the exact Shapley value, because the exact value is not computable at this scale. The deck's
caption says it; the correction was made deliberately in v26.

**The engineering details.** Estimates are refreshed every 10 batches (about 49 refreshes per epoch at batch size
2048), then clipped, smoothed with an exponential moving average and normalised before becoming hyperedge weights.
Clipping and smoothing exist because a noisy weight that jumps every few batches would destabilise training; the
attention gate is the second stabiliser. Together, the four mechanisms are why the method trains at all.
""",
},
{
 "title": "8 · From user-item graph to hypergraph: where the Shapley weights enter",
 "lede": "One paragraph of mechanism is worth ten of vocabulary. This is the DyHuCoG pipeline in plain language, with "
         "the equation it implements written in words.",
 "body": """
**Step 1 — the structure.** Build a hypergraph H = (V, E, W). The nodes V are users U, items I and contexts C. A
hyperedge e ∈ E is a group of nodes that belong to one interaction episode: typically a user, an item and the
context in which the interaction happened. Because a hyperedge is a set, not a pair, the model can express
higher-order relations that a plain graph cannot.

**Step 2 — the weights.** In a standard hypergraph convolution, each hyperedge has a weight, and the weight matrix W
is either fixed (often all ones) or learned implicitly. DyHuCoG instead computes a Shapley value for every entity in
the episode, from a cooperative game whose value function is the coalition's recommendation quality:

`v(S) = α · NDCG@20(S) + β · Diversity(S) + γ · ContextScore(S)`, with α = 0.60, β = 0.25, γ = 0.15,

plus a preference term `v_pref(S) = v(S) + λ_pref · Σ sim(u, i)` with λ_pref = 0.20. The estimates are clipped,
smoothed and normalised, and then they *are* the entries of W.

**Step 3 — message passing.** Each node updates its representation by aggregating the representations of the nodes it
shares hyperedges with, weighted by W and normalised by node and edge degrees. In words: information flows along the
relationships the model judged valuable, in proportion to how much they contributed to the recommendation objective.
Where a standard model treats every message as equally important, this one makes importance a measured quantity.

**Step 4 — the gate and the score.** An attention gate `a_ui = σ(W_a [e_u, e_i, l_i])` produces the intermediate
score `y_ui = (1 + a_ui) ⟨e_u, e_i⟩`, and the final prediction adds a context term:
`f(u, i, c) = y_ui + λ_c ⟨g(c), e_c⟩`. The gate is the stabiliser for early training, when the sampled Shapley values
are still noisy.

**Step 5 — training.** Minimise `L = L_BPR + λ_div L_div + λ_ctx L_ctx + λ_reg L_reg`. Note what this means
conceptually: **the explanation and the objective are the same object**. The Shapley game is built from NDCG@20,
diversity and context; the loss is built from ranking, diversity and context. That is the meaning of the sentence
"the explanatory game and the predictive objective are aligned by design", and it is the thesis's answer to the
question "why is this explanation faithful rather than decorative?"
""",
},
{
 "title": "9 · What the composite loss optimises, term by term",
 "lede": "Four terms, four concerns, four λs. If you can name what each term wants the model to do, the ablation "
         "table becomes obvious instead of memorised.",
 "body": """
**Ranking term (BPR).** For each triple (user, observed item, sampled negative) it increases the logistic gap
between the positive and the negative score. This is the accuracy engine, and it is the term the baselines use too.

**Diversity term.** `L_div = −(1/|U|) Σ_u ILD(R_u)`. Because ILD measures the average pairwise dissimilarity inside a
list, minimising the negative ILD means *maximising* diversity. This is the design decision that separates DyHuCoG
from models that add diversity by re-ranking after training: here, a list that repeats the same taste is penalised
during learning. Removing it costs 5.8 % NDCG@20 on both datasets — note that removing diversity hurts *accuracy* too,
which is the empirical refutation of the assumption that diversity is a cost.

**Context term.** `L_ctx` penalises the distance between the encoded contextual state `g(c)` and the learned context
node representation `e_c`, keeping recommendations coherent with the situation of the interaction. Removing it costs
8.2 % on MovieLens-1M and 11.0 % on Amazon-Book, the largest drop in the ablation.

**Regularisation term.** An L2 penalty on the parameters, controlling overfitting. Boring, necessary, and the reason
the ablation does not report it as a component.

**Why the terms must be differentiable and balanced.** Because they are added into one loss, the weights λ matter:
α, β and γ are grid-searched over [0.1, 0.8] under α + β + γ = 1, and the chosen 0.60 / 0.25 / 0.15 keeps ranking
primary while giving diversity and context non-trivial weight. The thesis reports that the configuration is stable
with variance below 1.5 % in NDCG@20, and states honestly that the full validation surface is not tabulated — that
last clause is worth knowing, because a jury member may ask for the grid and the correct answer is "the validated
optimum is reported; the intermediate surface is not in the paper."
""",
},
{
 "title": "10 · The statistical tests, end to end",
 "lede": "The defence rests on one test, one correction and one effect size. Here is the whole chain with the "
         "actual numbers of the thesis — know this page by heart, because the statistics are the most likely "
         "technical probe of the viva.",
 "body": """
**1. The test and its hypotheses.** The test on slides 62 and 78 is a paired samples t-test. For every one of the
6,040 users you compute one number: d = NDCG@20(DyHuCoG) − NDCG@20(baseline). The null hypothesis H0 is "the mean
of these 6,040 differences is zero" — the two models are equal for this population of users. The alternative H1 is
"the mean difference is not zero", and the test is two-sided: the direction of the gain comes from the sign of the
mean difference, not from the choice of tail. Everything else follows from this one design.

**2. Why paired.** The comparison is not "does DyHuCoG have a higher average NDCG than HPCF". It is "for each of the
6,040 users, did DyHuCoG do better?". The pairing removes the enormous between-user variance — some users are simply
easier to predict — and makes the test far more sensitive. An unpaired test would answer a different, weaker
question.

**3. The statistic, the degrees of freedom, the assumptions.** The statistic is `t = mean(d) / (sd(d)/√n)` with
df = n − 1 = 6,039: 6,040 differences, minus one constraint consumed by the estimated mean. Three assumptions: the
differences are independent across users (one row per user); the differences are roughly normal — with n = 6,040
the central limit theorem makes the test robust to moderate non-normality, and the Wilcoxon signed-rank test, which
does not assume normality at all, agrees at p < 0.001; and NDCG@20 is a bounded continuous score, so its
differences live on a usable scale.

**4. What the p-value says, and what it does not say.** A p-value is the probability, assuming H0 is true, of
seeing a |t| at least this large. It is not the probability that H0 is true, and it is not the size of the gain.
With 6,040 users almost any real difference becomes significant, so the p-value mostly separates noise from signal —
which is why the thesis reports effect sizes next to it.

**5. The six comparisons and their thresholds.** Holm–Bonferroni orders the six p-values from smallest to largest and
compares the k-th with α/(m − k + 1). With m = 6 and α = 0.05 the thresholds are 0.00833, 0.0100, 0.0125, 0.0167,
0.0250, 0.0500 — exactly the last column of backup slide 78. Each p-value is compared with its own, increasingly
generous threshold, and the procedure stops at the first failure. It controls the probability of even one false
positive across the family of tests — the family-wise error rate — which plain uncorrected testing would not.

**6. The results in the thesis.**

- DyHuCoG vs HPCF: t = 46.38, p = 1.81×10⁻²⁷⁰, dz = 1.33, threshold 0.0500.
- vs RecDCL: t = 92.72, dz = 2.67, threshold 0.0083.
- vs HCCF: t = 61.21, dz = 1.76, threshold 0.0100.
- vs LightGCN: t = 132.19, dz = 3.80, threshold 0.0125.
- vs NCF: t = 311.13, dz = 8.95, threshold 0.0167.
- vs MF: t = 341.76, dz = 9.83, threshold 0.0250.

All six are significant after correction; Wilcoxon's signed-rank test agrees at p < 0.001, so the conclusion does
not rest on normality.

**7. Why the effect size is the interesting number.** Cohen's dz is the mean paired difference divided by its
standard deviation; the conventional reading is 0.2 small, 0.5 medium, 0.8 large. The thesis reports dz ≥ 1.33
against every baseline, including 1.33 against the strongest one. The sentence to say is: "the gain is large by the
standard benchmarks, and it survives correction for multiple comparisons."

**8. The scope fence.** These tests are tabulated for per-user NDCG@20 on MovieLens-1M. Amazon-Book and the other
metrics are reported as descriptive over five seeds, and the standard deviations on backup slide 77 show why: on
Amazon-Book the ±1σ bands for NDCG@20 and Recall@20 nearly touch between DyHuCoG and HPCF. The five seeds measure
run-to-run noise; the 6,040 users support the claim about users — two different questions, both reported. Saying
the fence yourself is not a weakness; it is the difference between a candidate who knows the limits of their
analysis and one who does not.

**9. If pressed further.** Confidence intervals are not tabulated in the thesis; they follow from the same
quantities — mean(d) ± t* · sd(d)/√n — and adding them is future work (the future-work rule again: name it, give
the plan, stop). The full question drill — why not a z-test, why not bootstrap, one-tailed or two-tailed, what a
Type I error is here — is in the cheat sheet "Statistical tests at a glance".
""",
},
{
"title": "11 · NDCG@20 by hand: why position matters",
 "lede": "One worked example and the metric will never feel mysterious again.",
 "body": """
**The formula.** `DCG@K = Σ_{i=1..K} (2^rel_i − 1) / log₂(i + 1)`, normalised by the best achievable ordering:
`NDCG@K = DCG@K / IDCG@K`.

**A worked case.** A user has two relevant items. The model ranks one at position 1 and the other at position 5.

- Position 1 contributes (2¹ − 1)/log₂(2) = 1/1 = 1.000.
- Position 5 contributes 1/log₂(6) = 1/2.585 = 0.387.
- DCG@20 = 1.387. The ideal ordering puts both at the top: 1/1 + 1/1.585 = 1.631.
- NDCG@20 = 1.387 / 1.631 = **0.850**.

Now move that second item from position 5 to position 20: it contributes 1/log₂(21) = 0.228, so DCG falls to 1.228
and NDCG to **0.753**. Same two items found, same relevance, twelve points of NDCG gone because of position. That is
what "rank quality" means, and it is why the thesis uses NDCG@20 as its headline rather than Recall alone.

**Why the numbers in the deck are small on Amazon-Book.** The dataset has 91,599 books and about three million
interactions, with one held-out target per user ranked against a huge catalogue. An NDCG@20 of 0.0306 is not a
failure; it is the scale of the task. What matters is the comparison at equal difficulty: 0.0306 versus 0.0270 for
HPCF, the same +13 % direction as on the dense dataset — and that is exactly how slide 59 frames it.

**If someone asks "is 0.2775 a good number?"** The right answer is comparative, not absolute: it is the best of seven
models on a standard benchmark, it beats a 2025 state-of-the-art hypergraph model by about ten percent, and it is
significant after correction with a large effect size. Absolute NDCG values are not comparable across papers unless
the split and the negative sampling match, and the thesis reports both.
""",
},
{
 "title": "12 · Why accuracy and diversity rise together here (and usually do not)",
 "lede": "This is the most counter-intuitive empirical claim in the thesis, and the one a recommender-systems jury "
         "will press hardest.",
 "body": """
**The usual story.** Recommenders are trained to rank popular, safe items highly. Accuracy metrics reward that;
diversity metrics punish it. The standard remedy — re-rank the list after training to inject variety — costs
accuracy, which is why papers describe an accuracy-diversity *trade-off*.

**What DyHuCoG does differently.** Diversity is not a post-processing step. It appears twice in the training
machinery:

1. In the **loss**: `L_div = −(1/|U|) Σ ILD(R_u)`, so lists made of near-duplicate items are penalised during
   learning.
2. In the **coalition utility**: the same diversity term is one of the three components of v(S), so the Shapley
   weights themselves are computed from a utility that values variety.

Because the model is optimised for both at once, the gradient does not have to choose. The result on MovieLens-1M:
NDCG@20 0.2775 (up 9.8 %), Recall@20 0.2362 (up 12.6 %), coverage 0.397 (up 16.1 %) and ILD 0.516 (up 11.9 %) —
all four move in the same direction.

**The evidence that it is not an artefact.** If diversity were being bought with popularity, coverage would rise
while accuracy fell. It does not. And the ablation shows the reverse causality: *removing* the diversity term costs
5.8 % NDCG@20 on both datasets. In other words, diversity is not a tax on accuracy in this architecture; it is part
of what produces it.

**The honest boundary, and the sentence to use.** This is shown on two benchmarks with offline evaluation,
and the thesis does not claim that the trade-off disappears in general — slide 64 says the trade-off "is not fixed
by nature" when importance comes from a cooperative-game utility, which is a claim about this design, tested on
these datasets. If a jury member asks whether the gain comes from the diversity regulariser rather than from
Shapley, the ablation answers it: the Shapley weighting has its own row, −4.6 % / −6.1 % when removed.
""",
},
]


# ==========================================================================
# GLOSSARY part A
# ==========================================================================
GLOSSARY_A = [
# -------------------------------------------------------------- ML basics
{
 "term": "Supervised versus unsupervised learning", "tag": "ML basics", "where": "slides 13, 27",
 "plain": "Supervised learning has an answer key; unsupervised learning has to invent the categories itself.",
 "deep": "In supervised learning each training example comes with a label, and the model learns a mapping from "
         "features to label. In unsupervised learning there are no labels, and the algorithm finds structure — "
         "groups, densities, directions of variation — on its own. That difference has an explanatory consequence: "
         "in supervised learning you can always ask which features mattered *for predicting the label*; in "
         "clustering there is no label to predict, so 'why is this point in this group?' has to be posed differently.",
 "why": "It is the reason Contribution I is harder than the usual SHAP application, and the reason slide 27 calls "
        "clustering 'the hardest test bed'.",
},
{
 "term": "Clustering", "tag": "ML basics", "where": "slides 13, 14, 18, 27",
 "plain": "Grouping data points so that points in the same group are more similar to each other than to points in "
          "other groups.",
 "deep": "Clustering has no ground truth, which means two things follow. First, the number of clusters is a choice, "
         "not a fact — so the multi-criteria selection in this thesis. Second, validity must be argued: internal "
         "metrics such as Silhouette and Davies-Bouldin measure geometry, while domain plausibility measures "
         "usefulness. The thesis uses both, and says so.",
 "why": "Contributions I and II are about explaining clustering, and the thesis deliberately picks two domains "
        "(wine chemistry, air quality) where a domain expert can judge whether the groups make sense.",
},
{
 "term": "Features, labels, and the original feature space", "tag": "ML basics", "where": "slides 16, 28, 30, 33",
 "plain": "Features are the measurable inputs of a model; the original feature space is the set of measurements as "
          "they exist in the world, before any transformation.",
 "deep": "A wine sample has eleven measured features: fixed acidity, volatile acidity, citric acid, residual sugar, "
         "chlorides, free sulfur dioxide, total sulfur dioxide, density, pH, sulphates and alcohol. They are "
         "physically meaningful and, crucially, some of them are controllable. A transformed space (principal "
         "components, embeddings) is often better for the algorithm and worse for the human, because a component is "
         "a mixture and an embedding dimension has no name.",
 "why": "Keeping attribution in the original feature space is objective O2 of Contribution I and the operational "
        "content of actionability: 'acidity' can be acted on, 'component 2' cannot.",
},
{
 "term": "Latent space and latent factors", "tag": "ML basics", "where": "slide 11",
 "plain": "A learned, compressed representation in which the model does its reasoning; the individual numbers in it "
          "have no fixed meaning.",
 "deep": "Matrix factorisation represents each user and item as a vector of, say, 64 latent numbers, and scores a "
         "pair by their dot product. The model is accurate and compact, but nothing constrains the factors to "
         "correspond to anything a person can name; two runs with different seeds can produce rotated versions of "
         "the same space. Explanation in latent space is so not actionable; it merely re-describes the model "
         "in other unreadable terms.",
 "why": "It is the technical reason phrase 'the answer comes back in variables an expert can change' matters, and "
        "why the surrogate bridge in Contribution I exists at all.",
},
{
 "term": "Training, validation and test splits (and the leave-one-out target)", "tag": "ML basics", "where": "slide 22",
 "plain": "Data is divided into a part used to train, a part used to tune, and a part used once to report the final "
          "number.",
 "deep": "The training set fits the parameters; the validation set chooses hyperparameters and decides when to stop; "
         "the test set is used once, at the end, and touching it earlier leaks information into your choices and "
         "inflates the result. In recommendation the split must also respect time: here it is user-level and "
         "time-ordered, 70 / 10 / 20, and the evaluation is leave-one-out — each user's latest test interaction is "
         "the target, ranked against a large set of non-interacted items.",
 "why": "It is the skeleton of the shared protocol in section 3, and the source of the most common methods question "
        "in a viva: 'how did you prevent leakage?' The answer is the user-level, time-ordered split.",
},
{
 "term": "Cross-validation (five-fold)", "tag": "ML basics", "where": "slides 22, 31, 43",
 "plain": "Split the data into five parts; train on four and score on the fifth, five times, and average the five "
          "scores.",
 "deep": "Every point is used for evaluation exactly once, so the estimate is less dependent on one arbitrary split "
         "than a single hold-out. The cost is five times the computation. In this thesis five-fold cross-validation "
         "is used for the clustering surrogates and for the stability of the attributions, where the question is not "
         "'how well does the model predict' but 'does the explanation survive a change of data partition'.",
 "why": "It is part of the answer to 'are your SHAP rankings stable?' — the attributions are checked across folds, "
        "not produced once and presented as truth.",
},
{
 "term": "Standardisation (z-scores)", "tag": "ML basics", "where": "slides 18, 22, 31",
 "plain": "Rescale every feature so it has mean zero and standard deviation one.",
 "deep": "K-Means and PCA both use distances, and distances are dominated by whichever variable happens to have the "
         "largest numeric range. Residual sugar is measured in grams per litre, density in grams per millilitre: "
         "without standardisation, density would effectively be ignored. Standardising puts all eleven wine "
         "variables on the same footing so that a distance reflects a standard deviation of change, not a unit of "
         "measurement.",
 "why": "It is a small line on slide 22 with a large consequence: without it, the SHAP ranking would say more about "
        "measurement units than about wine. It is also why SHAP values are comparable across features here.",
},
{
 "term": "Random seed and reproducibility", "tag": "ML basics", "where": "slides 22, 25, 57",
 "plain": "The number that fixes all the random choices in an experiment so that another person can repeat it.",
 "deep": "Model initialisation, negative sampling, batch order and Monte Carlo Shapley sampling are all randomised. "
         "Fixing the seeds makes a run repeatable; running several seeds (here 42, 43, 44, 45, 46) and reporting "
         "mean ± standard deviation shows that the finding is not an artefact of one lucky draw. Both together are "
         "the standard of evidence in modern machine-learning papers.",
 "why": "The five-seed protocol and the fixed seeds in the shared configuration are what make the ±1σ table on "
        "backup slide 77 possible.",
},
{
 "term": "Early stopping and patience", "tag": "ML basics", "where": "slide 22",
 "plain": "Stop training when the validation score stops improving, and wait a fixed number of epochs before "
          "deciding that it has stopped.",
 "deep": "The patience parameter defines 'stops improving': here, 20 epochs without an improvement in validation "
         "NDCG@20. Early stopping is a regulariser — it prevents the model from continuing to fit the training data "
         "once generalisation has peaked — and it is also a fairness mechanism, because every model in the "
         "comparison is allowed to train until its own validation optimum rather than for a fixed number of epochs "
         "that might favour one architecture.",
 "why": "It is one of the small protocol choices that makes the comparison on slides 58 and 59 defensible.",
},
{
 "term": "Hyperparameters versus parameters", "tag": "ML basics", "where": "slides 22, 31, 43, 54",
 "plain": "Parameters are learned from data; hyperparameters are chosen by you and control how learning happens.",
 "deep": "The weights of a network are parameters. The number of clusters k, the number of Monte Carlo permutations "
         "M, the coalition weights α, β, γ, the preference weight λ_pref and the surrogate's tree depth are "
         "hyperparameters: they are set before or around training, by a grid search, a criterion, or a design "
         "decision. Because hyperparameters can silently produce the result you wanted, the thesis reports how each "
         "was chosen (elbow/Silhouette/DB for k, grid search under a sum-to-one constraint for α, β, γ, the "
         "convergence table for M) and adds a sensitivity analysis on the ones that matter most.",
 "why": "Slides 31, 43 and 54 exist mainly to show that the choices were principled and pre-declared, which is what "
        "question F2 is really asking.",
},
{
 "term": "Baseline", "tag": "ML basics", "where": "slide 23",
 "plain": "A reference method you compare against, so the reader can judge whether your improvement is meaningful.",
 "deep": "A good baseline set spans the space of reasonable approaches, including at least one strong recent "
         "method, so that a gain cannot be attributed to a lucky choice of comparison. Here the set spans four "
         "families: classical matrix factorisation, neural collaborative filtering, graph convolution, and two "
         "hypergraph models — with HPCF, a 2025 model, designated the strongest reference.",
 "why": "Slide 23's 'why this set' panel is the answer to 'did you compare against a straw man?', which is the "
        "opening move of many recommendation juries.",
},
{
 "term": "Ablation study", "tag": "ML basics", "where": "slides 60, 65",
 "plain": "Remove one component at a time and measure how much performance drops, to show that each component earns "
          "its place.",
 "deep": "An ablation is the standard way to argue that a complex architecture is not complexity for its own sake. "
         "The version in this thesis removes the Shapley weighting, the hypergraph structure, the attention gate, "
         "the context term and the diversity term, one at a time, on both datasets. Two honest caveats are stated: "
         "the ablation is component-wise, so it does not measure interactions between components; and an ablation "
         "cannot prove that a component is necessary in general, only that it contributes in this configuration.",
 "why": "It is the empirical core of the answer to 'is the gain from Shapley or from the extra machinery?' — "
        "question E6 — with the Shapley row at −4.6 % on MovieLens-1M and −6.1 % on Amazon-Book.",
},
{
 "term": "Overfitting, and why a surrogate can overfit", "tag": "ML basics", "where": "slides 22, 30, 36",
 "plain": "Learning the training data too well, including its noise, so performance on new data suffers.",
 "deep": "A flexible model can memorise rather than generalise. In this thesis overfitting would be fatal in a "
         "specific way: if the LightGBM surrogate simply memorised the cluster labels of the training points but "
         "generalised badly, then the SHAP explanation would describe a model that is not the clustering, and the "
         "entire bridge would be invalid. That is why surrogate fidelity is measured on held-out labels with "
         "five-fold cross-validation and bounded by a floor, and why the thesis also checks a modest tree capacity "
         "(100 trees, 31 leaves) rather than a large one.",
 "why": "It is the technical justification for the macro-F1 ≈ 0.82 floor, and the honest content of the "
        "'surrogate dependence' limitation on slide 36.",
},
{
 "term": "Explicit versus implicit feedback", "tag": "ML basics", "where": "slides 20, 21, 22",
 "plain": "Explicit feedback is a rating; implicit feedback is a behaviour, such as a click, a view or a purchase.",
 "deep": "Ratings are more informative per record but rare and biased by who chooses to rate. Implicit signals are "
         "abundant but ambiguous: a purchase is positive evidence, absence of a purchase is *not* evidence of "
         "dislike — the user may simply never have seen the item. Standard practice, followed here, is to treat "
         "observed interactions as positives and to sample negatives from unobserved items, and to use a pairwise "
         "ranking loss rather than a rating-prediction loss.",
 "why": "It explains the protocol line 'MovieLens-1M ratings above 3 become positives' and why Amazon-Book, which "
        "is implicit by nature, is included as the sparse stress test.",
},
{
 "term": "Density and sparsity", "tag": "ML basics", "where": "slides 20, 21",
 "plain": "Density is the fraction of the user-item matrix that is filled; sparsity is its complement.",
 "deep": "MovieLens-1M has 6,040 × 3,706 possible user-item pairs and about one million observed ratings, so about "
         "4.47 % of the matrix is filled. Amazon-Book has 52,643 × 91,599 pairs and about three million "
         "interactions, so about 0.06 % is filled — seventy-five times sparser. On such data, co-occurrence signal "
         "is scarce, so differences between models show up more clearly, and a method that can weight weak signals "
         "sensibly should help more.",
 "why": "The 0.0447 versus 0.0006 gap is the core of the robustness argument, and the reason the C3 gain is larger "
        "on Amazon-Book (+13.3 % versus +9.8 % NDCG@20).",
},
{
 "term": "Cold start", "tag": "ML basics", "where": "slides 10, 64",
 "plain": "The problem of recommending to a brand-new user or recommending a brand-new item, when there is almost "
          "no interaction history to learn from.",
 "deep": "Collaborative models learn from co-occurrence, so an entity with no co-occurrences has a representation "
         "driven only by its initialisation or its side features. Cold start is so the regime where "
         "structure-aware models can add the most — if they can propagate information from context and from "
         "neighbours rather than relying on the entity's own sparse history.",
 "why": "The thesis reports cold-start results: 0.061 versus 0.055 NDCG@20 for users with at most five training "
        "interactions (+10.9 %) and 0.057 versus 0.052 for cold items (+9.6 %). 'It does not solve cold start "
        "completely, but it improves performance in exactly the regime where it is hardest.'",
},
{
 "term": "Popularity bias", "tag": "ML basics", "where": "slides 13, 58, 59",
 "plain": "The tendency of recommenders to show already-popular items, which makes them even more popular.",
 "deep": "A feedback loop: exposure produces interactions, interactions make an item look better supported, and the "
         "model exposes it further. The measurable consequences are low catalogue coverage (few items ever shown) "
         "and low intra-list diversity (lists that repeat the same taste). Breaking the loop without losing "
         "relevance is the practical importance of treating diversity as a training objective rather than a "
         "post-hoc correction.",
 "why": "The coverage and ILD columns of the results tables are the evidence that DyHuCoG's accuracy gain is not "
        "bought with popularity: both diversity measures rise at the same time as NDCG and Recall.",
},
{
 "term": "Negative sampling (popularity-aware)", "tag": "ML basics", "where": "slide 22",
 "plain": "Choosing which non-interacted items to present to the model as negative examples.",
 "deep": "With implicit feedback, the negatives are constructed. Uniform sampling produces mostly trivially "
         "irrelevant items, which makes training easy and uninformative. Popularity-aware sampling draws negatives "
         "with a probability related to an item's frequency — written `q(i) ∝ f_i^η` — so the sampled negatives "
         "are popular enough to be plausible and so hard. The exponent η tunes how strongly frequency is "
         "emphasised; η = 0 recovers uniform sampling. Harder negatives sharpen the ranking boundary.",
 "why": "It is a protocol line on slide 22 that a recommender-systems jury will notice, and the honest answer to "
        "'how were negatives drawn?' — question F9.",
},

# -------------------------------------------------------------- clustering
{
 "term": "K-Means and K-Means++", "tag": "Clustering", "where": "slides 18, 30, 31, 43",
 "plain": "K-Means groups points into k clusters by repeatedly assigning each point to the nearest of k centres and "
          "moving each centre to the mean of its points.",
 "deep": "The algorithm alternates two steps until the assignment stops changing. It minimises the total squared "
         "distance from points to their centre, which is a local optimum, so the initial centres matter. K-Means++ "
         "chooses the initial centres spread out from each other, which makes the result more stable and better "
         "than random initialisation. The number of clusters k must be supplied by the analyst — the algorithm "
         "cannot infer it — which is why choosing k is a methodological decision rather than a hyperparameter "
         "search.",
 "why": "It is the clustering engine of both C1 and C2, and the object whose behaviour the SHAP attribution is "
        "meant to explain.",
},
{
 "term": "The elbow method", "tag": "Clustering", "where": "slides 22, 31, 43",
 "plain": "Plot the within-cluster error against k and look for the point where the curve stops falling steeply.",
 "deep": "Within-cluster error always decreases as k grows — at k = number of points it is zero — so it cannot be "
         "used as a score to be maximised. The elbow heuristic reads the curve's shape: before the elbow, extra "
         "clusters buy real structure; after it, they buy only finer subdivision. Because the elbow is a visual and "
         "sometimes ambiguous criterion, the thesis combines it with Silhouette and Davies-Bouldin and then applies "
         "an interpretability check.",
 "why": "It is the first of the three criteria on slide 22, and part of the answer to 'why k = 3?': the metric "
        "criteria, plus the interpretability argument on slide 32.",
},
{
 "term": "Principal Component Analysis (PCA)", "tag": "Clustering", "where": "slides 30, 31, 43, 44",
 "plain": "A linear transformation that replaces correlated variables with a smaller number of uncorrelated "
          "directions of maximum variance.",
 "deep": "The first principal component is the direction along which the data vary most; the second is the "
         "direction of most remaining variance orthogonal to the first, and so on. PCA is useful for visualisation "
         "in two dimensions and for removing redundancy before distance-based algorithms. Its costs are that "
         "components are mixtures of the original variables and that scaling changes the result, so it must be "
         "applied to standardised data.",
 "why": "The thesis uses PCA for clustering support and for the two-dimensional visual inspection of the Beijing "
        "structure — and plainly not as the space in which explanations are reported. That restraint is what "
        "keeps the attribution in the eleven named variables.",
},
{
 "term": "Regime (and cluster profile)", "tag": "Clustering", "where": "slides 41, 44, 45, 46",
 "plain": "A cluster that corresponds to a recognisable situation in the world, described by the variables that "
          "define it.",
 "deep": "A regime is a cluster with a story. The Beijing study produces three: warm photochemical episodes where "
         "ozone, temperature and dew point are prominent; winter smog where CO, SO2 and particulate matter dominate "
         "and low wind speed suppresses dispersion; and cleaner-air periods with favourable meteorology. A cluster "
         "profile is the set of SHAP values that explains membership in one cluster — the same features with "
         "different weights, which is what makes the story checkable rather than decorative.",
 "why": "The physical readability of the three regimes is what turns a clustering metric into a domain finding, "
        "and it is the substance of question D8.",
},

# --------------------------------------------------------------------- XAI
{
 "term": "Black box", "tag": "Explainability", "where": "slides 4, 6, 27, 52",
 "plain": "A model whose internal reasoning cannot be inspected in terms a human can use.",
 "deep": "Strictly speaking, most modern models are inspectable: you can read their weights. The problem is "
         "interpretation, not access. A deep network with millions of parameters is technically transparent and "
         "practically opaque, because the mapping from an input to a score is distributed over many units with no "
         "individual meaning. This is why the field moved from 'can we see inside?' to 'can we attribute the "
         "output to named inputs in a way that is faithful and useful?'.",
 "why": "The thesis's black boxes are specifically an unsupervised partition (C1, C2) and a hypergraph recommender "
        "(C3) — and the claim is not that they become white boxes, but that their behaviour can be attributed "
        "principledly.",
},
{
 "term": "Explainable AI (XAI)", "tag": "Explainability", "where": "slides 3-6, 72",
 "plain": "The field that studies how to produce explanations of model behaviour that people can understand and "
          "act on.",
 "deep": "XAI contains several distinct families: attribution methods (which inputs mattered), counterfactuals "
         "(what would have to change), prototypes and exemplars (what this resembles), rules and concept-based "
         "methods, and intrinsically interpretable models. The thesis works in the attribution family and adds a "
         "criterion to it: an explanation must be actionable, meaning it names a modifiable factor in the "
         "vocabulary of the domain.",
 "why": "Slides 4-6 set up the field's taxonomy and the thesis's specific contribution to it: a cooperative-game "
        "language shared between explanation and optimisation.",
},
{
 "term": "Intrinsic versus post-hoc interpretability", "tag": "Explainability", "where": "slides 6, 36, 49, 52, 66",
 "plain": "Intrinsic models are readable by design; post-hoc methods explain a model that was built without "
          "explanation in mind.",
 "deep": "Intrinsic approaches constrain the architecture — linear models, small decision trees, sparse rule "
         "lists — and pay for readability with flexibility. Post-hoc approaches leave the model free and explain it "
         "afterwards, at the risk of producing an explanation that is an account of a proxy rather than of the "
         "model. The thesis's arc is a third option: keep the model free, but inject the attribution signal during "
         "training so that the explanation is a read-out of the objective.",
 "why": "It is the axis along which C3 is positioned: from post-hoc description (C1, C2) to in-training guidance "
        "(C3). Slide 66 states the claim, slide 70 states its scope.",
},
{
 "term": "Local versus global explanation", "tag": "Explainability", "where": "slides 13, 14, 27, 33, 46",
 "plain": "A local explanation is about one prediction; a global explanation is about the model's behaviour overall.",
 "deep": "Local explanations answer 'why this instance?', global ones answer 'what does this model generally rely "
         "on?'. They can disagree, and reconciling them is a research problem in itself: a feature can be globally "
         "important yet irrelevant for a particular instance, and vice versa. The Shapley framework addresses this "
         "formally — the same value function produces both levels, and global importance is the mean absolute value "
         "of the local attributions.",
 "why": "Producing both levels at once, and consistent across clusters, is objective O1 of Contribution I and the "
        "whole point of the multi-level extension in C2.",
},
{
 "term": "Model-agnostic versus model-specific", "tag": "Explainability", "where": "slides 27, 31, 34",
 "plain": "A model-agnostic method treats the model as a black box; a model-specific method exploits its internals.",
 "deep": "Model-agnostic methods such as LIME and KernelSHAP can be applied to anything, at the cost of extra "
         "approximation and of ignoring structure that could make the explanation exact. Model-specific methods "
         "such as TreeSHAP exploit the structure of a family of models to compute exact values quickly. The thesis "
         "describes its own pipeline as *partially* model-agnostic: the game definition is general, but the exact "
         "attribution step relies on the surrogate being a tree ensemble.",
 "why": "The phrase on slide 27 and in the thesis abstract — 'partially model-agnostic' — is precise, and using it "
        "correctly signals that you know what your method does and does not promise.",
},
{
 "term": "Actionable insight (Definition 1.1)", "tag": "Explainability", "where": "slide 5",
 "plain": "An explanation that names a factor the designer can change, in the words of the domain, and connects the "
          "change to a change in output.",
 "deep": "The definition has two requirements. The first is modifiability: the factor must be something a decision "
         "maker can act on (a process parameter, a policy variable), not an artefact of the modelling pipeline. The "
         "second is vocabulary: the factor must be expressed in the domain's language — acidity in wine, pollution "
         "indicators in air quality, preference signals in recommendation. The thesis is explicit that actionability "
         "is a framing concept here, illustrated rather than measured; a user study is future work.",
 "why": "It is the criterion against which every result in the thesis is read, and the anchor of questions G1-G4. "
        "Say the two halves, and say that it was not measured — that is the complete, honest answer.",
},
{
 "term": "Surrogate model and fidelity", "tag": "Explainability", "where": "slides 30, 31, 36",
 "plain": "A simpler model trained to imitate a complex one, used as a stand-in so that an explanation can be "
          "computed; fidelity is how faithfully it imitates.",
 "deep": "The surrogate must be expressive enough to reproduce the target's behaviour and simple enough to be "
         "explained. Here it is a LightGBM multiclass classifier trained to predict K-Means cluster labels from the "
         "original features, and fidelity is measured with macro-F1 on held-out labels (about 0.82, with roughly "
         "0.80 as the practical floor). Fidelity is not a decorative number: it is the validity condition of the "
         "entire explanation, because everything computed on the surrogate is presented as evidence about the "
         "partition.",
 "why": "It is simultaneously the method (slide 30) and the first limitation (slide 36). A candidate who "
        "volunteers that trade-off — as the thesis does on page 58 — looks stronger, not weaker.",
},
{
 "term": "Macro-F1", "tag": "Explainability", "where": "slides 22, 30, 31, 32",
 "plain": "The average of the F1 score across classes, where F1 balances precision and recall for each class.",
 "deep": "Precision is the share of predicted members that truly belong to a class; recall is the share of true "
         "members that are predicted. F1 is their harmonic mean. Macro-F1 averages the per-class F1 values without "
         "weighting by class size, so a rare cluster counts as much as a large one. That is the right choice here, "
         "because clustering produces clusters of unequal size and a surrogate that ignores a small cluster would "
         "still look good under a weighted average.",
 "why": "It is the fidelity metric on slides 30-32 and the reason the floor is stated as 'macro-F1 ≈ 0.82' rather "
        "than 'accuracy ≈ 0.95', which would be trivially achievable by predicting the majority cluster.",
},
{
 "term": "LIME", "tag": "Explainability", "where": "slides 7, 23, 27, 31, 34",
 "plain": "Local Interpretable Model-agnostic Explanations: perturb an instance, see how the model's output changes, "
          "and fit a simple interpretable model locally.",
 "deep": "LIME generates neighbourhood samples around the instance, gets the model's predictions for them, "
         "weights the samples by proximity and fits a sparse linear model whose coefficients are the explanation. "
         "It is intuitive and applies to any model. Its explanations depend on how the neighbourhood was defined, "
         "how the perturbations were generated and how well the local linear fit approximates the true boundary — "
         "and none of those choices carries an axiomatic guarantee about fairness or completeness of the credit.",
 "why": "LIME is the designated comparator in the protocol, but the thesis is explicit that the comparison in "
        "Chapter 5 is theoretical and literature-backed, not a rerun empirical bake-off. That distinction is the "
        "second of the three never-say items.",
},
{
 "term": "SHAP (SHapley Additive exPlanations)", "tag": "Explainability", "where": "slides 5, 6, 29, 30, 33",
 "plain": "The framework that applies the Shapley value to a model's prediction by treating the input features as "
          "players in a cooperative game.",
 "deep": "SHAP defines the value of a coalition of features as the model's expected output when only those features "
         "are known — technically, the conditional expectation of the prediction given those feature values. The "
         "Shapley value of a feature is then its average marginal contribution to that expectation over all "
         "coalitions and orders. The result is an additive attribution: the SHAP values of an instance sum exactly "
         "to the difference between the instance's prediction and the base value. That additivity is what makes SHAP "
         "plots (waterfalls, force plots, beeswarms) readable as decomposition rather than as heuristics.",
 "why": "It is the methodological backbone of all three contributions — the same language applied to a clustering "
        "partition (C1), to a hierarchy of partitions (C2) and to a recommendation coalition (C3).",
},
{
 "term": "TreeSHAP and KernelSHAP", "tag": "Explainability", "where": "slides 30, 31, 43",
 "plain": "Two implementations of SHAP: TreeSHAP computes exact values for tree ensembles very fast; KernelSHAP "
          "estimates values for any model by sampling.",
 "deep": "TreeSHAP uses the structure of the trees to compute the conditional expectations exactly, in polynomial "
         "time rather than exponentially many coalition evaluations; it is exact for the model it runs on. "
         "KernelSHAP treats the model as a black box, samples coalitions, and solves a weighted least-squares "
         "problem whose solution converges to the Shapley values — it is model-agnostic, slower, and approximate. "
         "The practical rule: if your model is a tree ensemble, use TreeSHAP. Here the surrogate is deliberately a "
         "tree ensemble for exactly that reason.",
 "why": "The choice of a LightGBM surrogate is a choice of TreeSHAP: the pipeline is designed so that the "
        "attribution step is exact rather than doubly approximate. That is the answer to 'why LightGBM?'.",
},
{
 "term": "Reading a SHAP output: global ranking, summary plot, force plot", "tag": "Explainability", "where": "slides 33, 45, 46",
 "plain": "Three views of the same numbers: one bar per feature on average, one dot per instance per feature, and "
          "one instance decomposed additively.",
 "deep": "The global ranking sorts features by mean absolute SHAP value and says which variables move the output "
         "most on average, with no direction. The summary or beeswarm plot adds direction and heterogeneity: "
         "horizontal position is each instance's attribution, colour is the feature's value, so a vertical split "
         "pattern means the feature acts in opposite directions for different sub-populations. The force plot takes "
         "one instance and shows the contributions as segments pushing from the base value to the prediction, "
         "closing the gap exactly because of efficiency. All three are the same underlying list of numbers per "
         "instance.",
 "why": "These are the three figures on slides 33, 45 and 46, and the vocabulary to describe them — mean absolute "
        "importance, sign, spread, per-cluster profiles — is what a figures question is really testing.",
},

# ------------------------------------------------------------ game theory
{
 "term": "Cooperative game theory", "tag": "Game theory", "where": "slides 29, 54, 68, 72",
 "plain": "The branch of mathematics that studies how groups of players who can gain by working together should "
          "divide what they jointly earn.",
 "deep": "The central object is a pair (N, v): a set of players and a function that assigns a value to every "
         "possible subset. The theory then asks which allocations are fair, stable or defensible, and the answers "
         "come as axioms — properties a rule should satisfy — rather than as intuitions. This makes it a natural "
         "language for attribution, because attribution is exactly a division problem: the model's output is the "
         "joint value, and the features, or the entities, are the players who produced it.",
 "why": "It is the thesis's unifying language and its title. The claim is not that Shapley values are a useful "
        "heuristic, but that cooperative game theory provides one formal vocabulary in which clustering "
        "explanation and recommender learning can both be expressed.",
},
{
 "term": "Players, coalitions, and the grand coalition", "tag": "Game theory", "where": "slides 29, 54",
 "plain": "The players are the participants in the game; a coalition is any subset of them; the grand coalition is "
          "all of them together.",
 "deep": "With n players there are 2ⁿ possible coalitions, including the empty coalition. In this thesis the "
         "players change with the task: the eleven wine or air-quality variables in C1 and C2, and the users, "
         "items and contexts of an interaction episode in C3. The grand coalition is the whole model — the full "
         "feature set whose Silhouette defines the clustering, or the complete set of entities behind one "
         "recommendation — and its value is what the Shapley values must jointly account for.",
 "why": "Naming the players correctly is the first sentence of every explanation: 'the features are the players' "
        "in Contribution I, 'users, items and contexts are the players' in Contribution III. Juries listen for "
        "that sentence.",
},
{
 "term": "Characteristic function v(S)", "tag": "Game theory", "where": "slides 29, 54",
 "plain": "The rule that says what each coalition can reach on its own, without help from the players outside it.",
 "deep": "The only formal constraints are that the empty coalition is worth zero, v(∅) = 0, and that the function "
         "be defined for every subset. Everything else is a modelling choice, and it is where the domain enters: "
         "in C1 the value of a coalition of features is the Silhouette of the K-Means solution computed on those "
         "features; in C3 the value of a coalition of entities is the recommendation quality — NDCG@20, diversity "
         "and context — achievable by that coalition. Choosing v is the modelling act; the Shapley value that "
         "follows is then determined.",
 "why": "Because the value function can be redefined, the thesis can apply the same machinery to a partition, a "
        "hierarchy and a recommender — 'one cooperative-game definition, three value functions', as slide 68 puts "
        "it.",
},
{
 "term": "Marginal contribution", "tag": "Game theory", "where": "slides 29, 54, 55",
 "plain": "How much more the group can reach with you than without you.",
 "deep": "Formally, the marginal contribution of player j to coalition S is v(S ∪ {j}) − v(S). It is the natural "
         "definition of 'what you add', but it is coalition-dependent: a guitarist adds a lot to drums and little "
         "to another guitarist. That dependence is not a flaw to be removed but the reason a value must be "
         "*averaged* over coalitions rather than read off one of them. In DyHuCoG this quantity is computed during "
         "training for each entity of the episode and becomes the hyperedge weight.",
 "why": "It is the quantity the whole Monte Carlo estimator samples, and the intuition to give if a jury member "
        "asks what the Shapley value is in one sentence.",
},
{
 "term": "Shapley value", "tag": "Game theory", "where": "slides 29, 34, 42, 54, 63",
 "plain": "A player's average marginal contribution over all possible arrival orders — equivalently, over all "
          "coalitions weighted by the probability that they form.",
 "deep": "Defined by Shapley in 1953, it is the unique allocation rule satisfying efficiency, symmetry, "
         "null-player and additivity. Three properties are worth remembering for a viva: it is exact by "
         "definition, not a heuristic; it is additive, so attributions of parts sum to attributions of wholes; and "
         "it can be estimated unbiasedly by sampling permutations, which is what makes it usable at scale. Its "
         "computational cost is the price: exponential in the number of players without approximation.",
 "why": "It is the thesis's central object: the explanation of a partition in C1, the aggregation rule across "
        "levels in C2, and the training signal in C3. Everything in the deck is a consequence of taking one "
        "allocation rule seriously.",
},
{
 "term": "The four Shapley axioms", "tag": "Game theory", "where": "slides 29, 34, 35",
 "plain": "Efficiency, symmetry, null player and additivity — the four properties that together determine the "
          "Shapley value uniquely.",
 "deep": "**Efficiency**: the contributions sum to the total value, so nothing is left unexplained. **Symmetry**: "
         "two players with identical marginal behaviour receive equal value, which makes comparisons across "
         "features and clusters fair. **Null player**: a player who never changes any coalition's value receives "
         "zero, so irrelevant variables are not credited. **Additivity**: for two games v and w, φ(v + w) = φ(v) + "
         "φ(w), so explanations compose. Together they are not merely desirable properties; they characterise the "
         "rule — the Shapley value is the only one satisfying all four (proved in Appendix A.1 through unanimity "
         "games).",
 "why": "They are objective O3 of Contribution I: the justification of Shapley over LIME is axiomatic. Say the "
        "four names and what each one prevents; that is a complete answer.",
},
{
 "term": "Uniqueness (why the four axioms determine the value)", "tag": "Game theory", "where": "slides 29, 34",
 "plain": "Because the axioms leave no freedom: any rule satisfying all four must give exactly the Shapley value.",
 "deep": "The proof strategy is to decompose an arbitrary game into unanimity games — one per non-empty coalition, "
         "each worth 1 only if the coalition is fully present. Any game is a unique weighted sum of those. On a "
         "unanimity game the four axioms force the answer: null player sets it to zero outside the coalition, "
         "symmetry equalises it inside, and efficiency fixes each member's share at 1/|T|. Additivity then extends "
         "the result to every game. This is why the thesis can say 'Shapley is the right rule' without running a "
         "comparative experiment.",
 "why": "It is the formal answer to the strongest methodological question in section 4 — 'why Shapley and not "
        "something else?' — and the reason the LIME comparison can be theoretical and still persuasive.",
},
{
 "term": "Banzhaf index and the nucleolus", "tag": "Game theory", "where": "slide 34 (implied)",
 "plain": "Two alternative allocation rules from cooperative game theory, rejected here for specific reasons.",
 "deep": "The Banzhaf index also averages marginal contributions, but over coalitions rather than orders, and in "
         "its standard form it does not satisfy efficiency: its attributions need not sum to the total value being "
         "explained. The nucleolus allocates by minimising the maximum dissatisfaction of any coalition; it comes "
         "from bargaining theory and does not target additive feature attribution. Both are respected tools; "
         "neither provides the property set this thesis needs.",
 "why": "Knowing the alternatives is what makes 'we chose Shapley because of the axioms' an argument rather than a "
        "preference. It is question B3, and the honest answer is short.",
},
{
 "term": "Choosing the value function: Silhouette versus coalition utility", "tag": "Game theory", "where": "slides 29, 30, 54",
 "plain": "The same Shapley machinery with two different definitions of what a coalition is worth.",
 "deep": "In C1 and C2 a coalition's worth is the quality of the clustering it supports — the Silhouette of the "
         "K-Means solution on that subset of features. In C3 a coalition's worth is the quality of the "
         "recommendation it can reach — a weighted combination of NDCG@20, diversity and context alignment, plus "
         "a preference term. Nothing about the Shapley value changes; what changes is what the players are trying "
         "to reach. This is the thesis's answer to 'why is this one framework and not three projects?'",
 "why": "It is the second philosophical pillar after the axioms, and the content of the takeaway box on slide 68: "
        "'one cooperative-game definition, three value functions'.",
},
{
 "term": "Monte Carlo Shapley (permutation sampling)", "tag": "Game theory", "where": "slides 55, 61, 79",
 "plain": "Estimate the Shapley value by sampling some of the possible arrival orders and averaging the marginal "
          "contributions you observe.",
 "deep": "Because the Shapley value is an average over orders, a random sample of orders gives an unbiased estimate: "
         "its expected value is the true Shapley value. The estimator's variance is σ²/M, so error falls with the "
         "square root of the sample count — halving the error costs four times the samples. The practical choices "
         "are M (50 here, refreshed every 10 batches, about 49 times per epoch) and the sampling distribution. "
         "Castro, Gómez and Tejada (2009), reference [8] in the deck, is the standard citation for this estimator.",
 "why": "It is what makes Contribution III a trainable model rather than a theoretical proposal, and the answer "
        "to the cost questions on slide 61.",
},
{
 "term": "Unbiasedness, variance and σ²/M", "tag": "Game theory", "where": "slide 55",
 "plain": "The sampling estimate is right on average; its spread shrinks as you take more samples.",
 "deep": "Unbiasedness says E[φ̂] = φ: running the estimator many times gives the true value on average, with no "
         "systematic offset. Variance measures the spread around that average and equals σ²/M where σ² is the "
         "variance of a single sampled marginal contribution. This is why the deck writes 'variance σ²/M' next to "
         "'unbiased estimator' — the two words together are the whole statistical justification for using a sample "
         "in place of the exact value.",
 "why": "It is the precise form of the claim that M = 50 is enough, and it grounds the convergence table on slide "
        "55 and backup slide 79.",
},
{
 "term": "MSE, and 'accuracy against a high-sample reference'", "tag": "Game theory", "where": "slides 55, 61, 79",
 "plain": "MSE is the average squared difference between the estimate and a reference; the reference here is a "
          "much larger sample, because the exact value cannot be computed.",
 "deep": "For an unbiased estimator, mean squared error equals variance, so MSE inherits the 1/M behaviour. The "
         "reference against which accuracy is measured is a high-sample estimate — the deck says so plainly — "
         "not the exact Shapley value, because exact computation is infeasible at this scale. The reported pairs "
         "are M = 25 → MSE 5.6×10⁻⁵ and about 98 %; M = 50 → 1.4×10⁻⁵ and about 99 %; M = 100 → 3.5×10⁻⁶ and about "
         "99.5 %, at 2.5× the training cost.",
 "why": "It is the correction made in v26 and a favourite trap: saying '99 % accurate against the exact Shapley "
        "value' would overstate the method. Saying 'against a high-sample reference' is both accurate and more "
        "impressive.",
},
{
 "term": "Clipping, exponential moving average, and normalisation", "tag": "Game theory", "where": "slides 55, 56",
 "plain": "Three engineering steps that turn noisy sampled Shapley estimates into stable training weights.",
 "deep": "Clipping bounds extreme estimates, so that one unlucky sample cannot produce a huge weight. The "
         "exponential moving average — a running average that gives recent values more weight — smooths the "
         "sequence across refreshes, so the weights evolve rather than jump. Normalisation rescales the estimates "
         "so they can be used as hyperedge weights with comparable magnitudes across episodes. Without these "
         "three, the training signal would be a noisy sequence of large shocks.",
 "why": "Slide 55's 'clip, EMA-smooth, normalise → hypergraph edge weights' is one line, but it is the difference "
        "between a method that converges and one that does not. It is also why the attention gate exists as a "
        "second stabiliser.",
},

# ------------------------------------------------------------- tree models
{
 "term": "Decision tree, split, leaf and depth", "tag": "Tree models", "where": "slides 22, 25, 30, 31",
 "plain": "A model that makes a prediction by asking a sequence of yes/no questions about the features.",
 "deep": "Each internal node tests a feature against a threshold; each split sends an instance left or right; each "
         "leaf holds a prediction. Depth is the number of questions on the longest path. A single tree is readable "
         "but weak; the power comes from combining many of them. The tree depth is one of the parameters tested in "
         "the sensitivity analysis of C2, because deeper trees can fit the cluster labels more exactly while "
         "becoming less stable.",
 "why": "The surrogate used throughout C1 and C2 is a tree ensemble, and TreeSHAP exists because the tree "
        "structure makes exact Shapley values computable in polynomial time.",
},
{
 "term": "Gradient boosting and LightGBM", "tag": "Tree models", "where": "slides 22, 30, 31",
 "plain": "Train many small trees in sequence, each one correcting the errors of the trees already built.",
 "deep": "Boosting fits the first tree to the data, then fits the next tree to the residual error, and so on, "
         "combining them with a learning rate. LightGBM is an efficient implementation that grows trees "
         "leaf-wise rather than level-wise — it expands whichever leaf reduces the loss most — which makes it fast "
         "and accurate on tabular data. The configuration in this thesis is deliberately modest: 100 trees with 31 "
         "leaves, chosen because it reaches macro-F1 ≈ 0.82 on the cluster labels while remaining stable under "
         "changes of depth.",
 "why": "It is the 'bridge' model of Contribution I: accurate enough to reconstruct the partition, and a tree "
        "ensemble so that TreeSHAP can attribute its output exactly.",
},
{
 "term": "Log-odds and multiclass log-loss", "tag": "Tree models", "where": "slides 16, 30",
 "plain": "The model's raw score before it is converted into a probability; the loss measures how well the "
          "predicted class probabilities match the truth.",
 "deep": "A classifier outputs a score per class, and the softmax function converts the scores into probabilities. "
         "The log-odds for a class is the log of the ratio between its probability and the alternatives. Multiclass "
         "log-loss penalises confident wrong probabilities and rewards well-calibrated ones. The important "
         "consequence for this thesis is the unit of the explanation: SHAP values are additive in the model's "
         "output space, which for a LightGBM classifier means log-odds, so 'density has a SHAP value of +0.3' is a "
         "statement about the log-odds of the predicted cluster, not about the probability.",
 "why": "It is the technical content behind the honest qualifier on page 62 of the thesis: efficiency holds with "
        "respect to the surrogate's log-odds output. Say 'log-odds' once in the viva and the jury knows you "
        "understand what the numbers mean.",
},
]


GLOSSARY = GLOSSARY_A + GLOSSARY_B
__all__ = ['GLOSSARY', 'WALKTHROUGHS', 'render_intro']
