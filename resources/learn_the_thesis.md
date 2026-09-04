# Learning Resource — Understanding the Thesis

> **Title:** *Cooperative Game Theory for Explainable Artificial Intelligence (XAI) in
> Recommendation Systems: A Shapley Framework for Actionable Insight.*
> **Author:** Mouad Louhichi · **Supervisor:** Pr. Mohamed Lazaar
> **Institution:** ENSIAS, Mohammed V University, Rabat, Morocco.

This resource teaches you the thesis from first principles. It is written so that a
colleague, a student, or a jury member can (a) understand the argument, (b) follow the
method, and (c) defend its claims. It is organised as **five modules** that mirror the
defense deck: the core idea, the mathematics, the three contributions, the protocol, and
the honest boundaries.

---

## Module 0 — The thesis in one sentence

> Shapley values (cooperative-game attribution) are used not only as post-hoc explanations
> but as a **single, shared, formally-grounded mechanism** that (1) explains black-box
> clustering, (2) stays coherent when that explanation is scaled to large, hierarchical,
> multi-level clustering, and (3) becomes an **in-training optimisation signal** inside a
> dynamic hypergraph recommender (**DyHuCoG**).

Three words to remember: **explain** (C1), **scale** (C2), **integrate** (C3).

---

## Module 1 — Why this problem matters

### 1.1 The core tension

Recommendation and clustering systems grew more expressive over time — from similarity
filters, to matrix factorisation, to neural collaborative filtering, to graph GNNs, to
hypergraph models. *Every step improved ranking but lowered transparency.* The thesis keeps
accuracy and interpretability as **objectives to be reconciled, not traded against one
another.**

### 1.2 Definition 1.1 — Actionable insight

An explanation is **actionable** when it:

1. Identifies **at least one modifiable factor** whose change is associated with a
   specifiable change in model output, **and**
2. That factor is expressible in the **semantic vocabulary of the task domain** — a
   physicochemical variable (wine), a pollution indicator (air quality), or a preference
   signal (recommendation) — **not** an opaque latent code.

> Why this matters: an explanation that identifies a modifiable driver supports
> **intervention**, not merely description. A credible explanation is judged by whether it
> supports a downstream decision, not by whether it looks plausible.

### 1.3 Why the deficit matters

- **Trust** — opaque systems mediate what billions of users see, buy, and watch.
- **Debugging & science** — you cannot learn from a model you cannot interrogate.
- **Regulation** — the EU AI Act (Reg. 2024/1689), OECD AI principles, and GDPR all put a
  premium on meaningful explanation.

---

## Module 2 — The mathematical backbone

### 2.1 Cooperative (transferable-utility) game

A TU game is a pair `(N, v)` where `N` is a set of *players* and `v: 2^N → ℝ` is a
*coalition value* function. Intuitively, `v(S)` answers: *how valuable is the coalition S?*

### 2.2 The Shapley value

For a player `i`, the Shapley value is the **expected marginal contribution** of `i` over
all orderings of the players:

```
φ_i(v) = Σ_{S ⊆ N\{i}} [ |S|! (|N|-|S|-1)! / |N|! ] · [ v(S ∪ {i}) − v(S) ]
```

It is the *unique* allocation satisfying four axioms:

| Axiom | Formal statement | Interpretive meaning |
|---|---|---|
| **Efficiency** | Σ φ_j = v(N) − v(∅) | All explanatory mass is allocated |
| **Symmetry** | Identical marginal contributors get equal allocation | Equal players are treated fairly |
| **Null player** | Zero marginal contributor gets zero | No spurious credit |
| **Additivity** | φ(v + w) = φ(v) + φ(w) | Explanations compose across tasks |

> **Why Shapley over LIME?** SHAP is grounded in an axiomatic, normative basis; LIME fits a
> local surrogate and has no equivalent guarantee, and it is sensitive to perturbation
> design.

### 2.3 Approximation — the practical necessity

Exact Shapley is **exponential**. The thesis uses two approximations:

- **Monte Carlo estimator** (used in DyHuCoG):
  `φ̂_j = (1/M) Σ_m [ v(S_m ∪ {j}) − v(S_m) ]`. Unbiased; variance = σ²/M; MSE → O(1/M);
  absolute error → O(1/√M).
- **TreeSHAP** (used in the clustering chapters): exact/fast attribution for tree models,
  which is why a LightGBM surrogate is chosen.

### 2.4 The key caveat (be ready to state it)

In the surrogate pipeline, **efficiency holds with respect to the LightGBM surrogate output,
not directly to the Silhouette-based game.** That is exactly why surrogate fidelity is the
critical validity condition.

---

## Module 3 — The three contributions

### C1 — Explainable black-box clustering (Chapter 5; Paper I)

**Goal:** explain a *clustering* (an unsupervised partition) faithfully and actionably.

**The gap:** explainable clustering is fragmented — methods favour a *local* or a *global*
explanation, rarely both; they often fail to scale; and they rarely preserve coherence across
clusters. Shapley is well established in supervised tasks but almost absent from unsupervised
clustering.

**The method — cooperative game framing.** Players are *features* (`N = F`). The coalition
value is the clustering quality of a feature subset:

```
v(S) = Silhouette( KMeans(X_S, k*) )
```

Silhouette is chosen because it is bounded, normalised, and semantically intuitive. The
problem: evaluating `v(S)` for every subset is combinatorial. **Bridge:** train a LightGBM
multiclass **surrogate** to predict the induced cluster labels from the original features,
then apply **TreeSHAP** to the surrogate. This keeps attribution in the original semantic
feature space.

**Pipeline (5 stages):** standardise → PCA (diagnostic only) → K-Means++ + optimal-k →
LightGBM surrogate → TreeSHAP.

**Key result (Wine, 4,898 × 11):**
- `k` is chosen by **interpretability, not geometry**. `k=2` gives Silhouette 0.214 / DB 1.775;
  selected `k=3` gives Silhouette 0.144 / DB 2.097 — weaker separation but three distinct
  oenological narratives.
- **Global importance:** density → pH → fixed acidity → sulfur-dioxide → alcohol.
- **Cluster profiles:** C0 ~ density + SO₂; C1 ~ acidity/pH; C2 ~ acidity, alcohol, related.
- **Surrogate fidelity:** macro-F1 ≈ 0.82 (the floor).

**Findings:** Shapley explains black-box clustering faithfully and coherently; it returns
attribution to original variables; it is theoretically grounded (four axioms); it recovers a
chemically interpretable hierarchy.

**Limitations:** depends on LightGBM surrogate fidelity; tabular only; single-level (cannot
explain how importance reconfigures between a partition and its sub-partitions).

**Takeaway:** Shapley attribution is a single principled lens for explaining an unsupervised
partition — *but real data are rarely single-level.* This motivates C2.

---

### C2 — Multi-level XAI for large-scale clustering (Chapter 6; Paper II)

**Goal:** keep the explanation coherent when clustering becomes **multi-level / large-scale**.

**The gap:** a variable can be *globally* important yet *locally* uninformative (or the
reverse). A flat explanation is **true yet incomplete** — it cannot show how importance
changes as you "zoom in."

**The method.** Recursive/nested clustering: coarse clustering on the full dataset, then
subdivide each cluster. For each level, train a level-specific surrogate and compute SHAP in
the **same** original feature space. **Cross-level aggregation is NOT a naive average** — it
respects cluster size and nesting structure.

**Proposition 6.1 — Hierarchical Attribution Consistency.** Let `Φ^(ℓ,c)_j = E_{x~c}[|φ_j^(ℓ)(x)|]`
be the expected absolute SHAP importance of feature `j` at level `ℓ` in cluster `c`, and let
`w_{c'} = |c'|/|c|` be the relative child size. For a strict nested hierarchy on a consistent
feature space:

```
Φ^(ℓ,c)_j = Σ_{c' ∈ child(c)} w_{c'} · Φ^(ℓ+1,c')_j + ε_j
```

where `ε_j` is a residual from surrogate mismatch, vanishing under perfect fidelity. Derived
via the **law of total expectation** (children partition the parent).

> It does **NOT** claim explanations are identical across levels; it implies differences can
> be *interpreted* rather than dismissed as inconsistency.

**Key result (Beijing, 383,585 × 11):**
- Full dataset, `k=3`; **Silhouette ≈ 0.63, Davies–Bouldin ≈ 0.55** (stronger than wine —
  do **not** confuse this with wine's 0.144/2.097).
- **Global importance:** temperature → dew point → pressure → CO → NO₂ → PM10 → PM2.5.
  Meteorological variables play a structurally central role (they condition dispersion,
  trapping, photochemistry).
- **Three regimes:** warm photochemical (ozone, temp, dew point); wintertime smog (CO, SO₂,
  PM, low wind); clean/well-dispersed events.
- **Multi-level insight:** at coarse level temp/dew point dominate (regime selection); within
  clusters CO, SO₂, PM10, wind speed, pressure, ozone become discriminative (variation within
  regime). This is the *point* of a multi-level explanation — not a contradiction.

**Comparative:** Beijing Silhouette 0.63 vs Gramegna & Giudici (credit-risk) 0.37; LIME
shows weaker structural coherence and less stable local narratives.

**Findings:** scalable multi-granular explanation; formal cross-level consistency (Prop 6.1);
validated on a structurally different dataset.

**Limitations:** clustering remains static (despite temporal Beijing data); surrogate +
representative-instance reporting compress observation-level variation; tabular only; still an
explanation of a *pre-computed* partition.

**Takeaway:** Shapley attribution stays coherent across granularity when the hierarchy is
explicit — *but it is still post-hoc.* This motivates C3.

---

### C3 — DyHuCoG: Dynamic Hypergraph Cooperative Game (Chapter 7; Paper III)

**Goal (the strongest claim):** move attribution **beyond post-hoc analysis into the learning
dynamics** of a recommender — attribution becomes an **in-training signal**.

**The gap:** graph/hypergraph recommenders treat message importance as either *uniform* or
*attention-weighted*, without a principled marginal-contribution account. Diversity is a
secondary objective or a re-ranking heuristic. Interpretability is added *after* prediction.

**Cooperative-game framing.** Players `N = U ∪ I ∪ C` (users, items, contexts). Hypergraph
`H = (V, E, W)`. Coalition value (multi-objective utility):

```
v(S) = α · NDCG@20(S) + β · Diversity(S) + γ · ContextScore(S),   α+β+γ=1
v_pref(S) = v(S) + λ_pref · Σ_{(u,i)∈S} sim(u,i)
```

Tuned: α=0.60, β=0.25, γ=0.15, λ_pref=0.20. Coalition evaluation is scoped to the interaction
**episode** (a few dozen players), not the full catalogue — an honest boundary.

**Preference-aware Monte Carlo Shapley.** `φ̂_j^pref = (1/M) Σ_m [ v_pref(S_m∪{j}) − v_pref(S_m) ]`.
`M=50` gives MSE ≈ 1.4×10⁻⁵, ~99% accuracy. Refreshed every 10 batches, smoothed by EMA.

**Architecture.** Base propagation: `e^(ℓ+1) = σ(D^{-1/2} A D^{-1/2} e^(ℓ))`. Shapley-weighted:
`e_j^(ℓ+1) = σ(W^(ℓ) e_j^(ℓ) + Σ_{k∈N(j)} w_jk e_k^(ℓ))` with normalised weights
`w_jk = φ̂_jk / Σ_{k'∈N(j)} φ̂_jk'` (clipped + smoothed). Layer fusion with learned α_ℓ;
attention gate `a_ui = σ(W_a[e_u, e_i, l_i])`; context-aware score
`f(u,i,c) = y_ui + λ_c ⟨g(c_ui), e_cui⟩`.

**Loss.** `L = L_rec + λ_div L_div + λ_ctx L_ctx + λ_reg L_reg` — BPR ranking, intra-list
diversity regulariser, context alignment, weight decay. *The learning objective and coalition
value are aligned.*

**Key results (relative to strongest baseline HPCF):**

| Dataset | NDCG@20 | Recall@20 | Coverage | ILD |
|---|---|---|---|---|
| MovieLens-1M | +9.77% | +12.58% | +16.1% | +11.9% |
| Amazon-Book | +13.33% | +16.16% | +29.7% | +12.5% |

- Largest relative gains on the **sparsest** data (Amazon) → Shapley weighting helps most
  when signal is weak.
- **Ablation:** removing Shapley value costs −4.6%/−6.1%; removing context is the largest
  single loss (−8.2%/−11.0%); hypergraph −6.8%/−8.9%; attention −3.5%; diversity −5.8%.
- **Statistical validation:** paired t-test per-user NDCG@20 (n=6040), vs HPCF t=46.38,
  Cohen's d=1.33, p≈1.81×10⁻²⁷⁰; Holm–Bonferroni + Wilcoxon signed-rank. (Paired tests apply
  only to MovieLens-1M; Amazon remains descriptive.)
- **Cold-start:** user ~0.061 (+10.9%), item ~0.057 (+9.6%).
- **Computational overhead:** ~1.78× training time (2000s vs 1125s); inference 1.84 ms/query
  (ML-1M).

**Findings:** attribution as an in-training signal; the accuracy–diversity–context trade-off
is not structurally fixed; ranking/coverage/diversity improve together.

**Limitations:** ~1.78× training overhead; depends on meaningful context; MC Shapley could use
variance reduction; ablation is component-wise (no factorial interactions); baselines
finalised early 2026 (claim only vs tested set).

**Takeaway:** attribution is a first-class part of the learning objective; the explanation is
a direct read-out of what the model already optimises — structurally faithful, not an external
approximation.

---

## Module 4 — The shared experimental protocol (Chapter 4)

### Datasets

| Dataset | Scale | Density | Role |
|---|---|---|---|
| Wine Quality (Vinho Verde) | 4,898 × 11 | dense, chemically correlated | C1 single-level clustering |
| Beijing Multi-Site Air Quality | 383,585 × 11 | large, noisy, 2013–2017 | C2 multi-level clustering |
| MovieLens-1M | 6,040 u × 3,706 i | 0.0447 · 1.0M ratings | C3 DyHuCoG |
| Amazon-Book | 52,643 u × 91,599 i | 0.0006 · 3.0M ratings | C3 DyHuCoG |

Selection criterion: clustering datasets have **semantically interpretable features**;
recommendation datasets are **benchmark-standard with established baselines**.

### Splitting

- Recommendation: user-level temporal holdout — 70% train / 10% val / 20% test;
  **leave-one-out** (latest test positive per user is the target).
- MovieLens-1M ratings **> 3** treated as positive implicit feedback.
- Popularity-aware negative sampling `q(i) ∝ f_i^η` for harder contrasts.
- Clustering: 5-fold CV for surrogate/attribution stability.
- Reproducibility: seeds {42,43,44,45,46}; early-stopping patience 20.

### Baselines

Recommendation: MF, NCF, LightGCN, RecDCL, HCCF, HPCF (strongest). Clustering: LIME-based
surrogate pipeline.

### Metrics

- **Ranking:** Precision@K, Recall@K, NDCG@K (NDCG@20 primary; DCG = Σ (2^rel−1)/log₂(i+1)).
- **System diversity:** Catalogue Coverage = |∪ R_u| / |I|.
- **List diversity:** ILD(R_u) = 2/(K(K−1)) Σ_{a<b} [1 − sim(i_a, i_b)] in the learned item space.
- **Clustering:** Silhouette, Davies–Bouldin, Calinski–Harabasz.
- **Statistics:** paired t-test, Holm–Bonferroni, Wilcoxon signed-rank, Cohen's d_z.

### Hardware / software

Intel i9-14900K (24 cores) · RTX 4090 24GB · 48GB RAM · 2TB SSD · Python 3.8 ·
scikit-learn / LightGBM / SHAP / PyTorch 2.0.1 · Altair for interactive SHAP.

---

## Module 5 — The five research questions & how they map

| RQ | Question | Answered by |
|---|---|---|
| RQ1 | How can Shapley explain black-box clustering faithfully at instance and cluster level? | C1 (Ch. 5) |
| RQ2 | How can this extend to large-scale, hierarchical clustering without losing tractability or consistency? | C2 (Ch. 6) |
| RQ3 | Can cooperative attribution move beyond post-hoc and enter the learning dynamics of graph recommenders? | C3 (Ch. 7) |
| RQ4 | Can a recommender jointly optimise ranking, context and diversity when importance is estimated by a cooperative-game utility? | C3 (Ch. 7) |
| RQ5 | What emerges when clustering explanation and recommendation learning are two stages of one cooperative-game perspective? | Thesis-level (Ch. 8) |

**Thesis answer:** cooperative game theory can function as a **shared methodological
perspective** for actionable explanation across clustering and recommendation. It is **not**
claimed to be one fully unified framework eliminating all tension; it is a **common
attribution language**.

---

## Module 6 — Honest boundaries (be ready to concede these)

1. **Computational:** exact Shapley is intractable; every contribution relies on
   approximation, surrogates, or restricted reporting.
2. **Methodological:** clustering depends on surrogate fidelity; recommendation depends on
   stable approximate contributions and adequate context.
3. **Empirical:** tabular clustering + offline recommendation; no multimodal / sequential /
   online deployment; no dedicated human-subject actionability study.
4. **Claim scope:** a coherent perspective, not one fully unified framework.
5. **Efficiency scope:** holds w.r.t. the surrogate output, not the Silhouette-based game.
6. **Scoped player set (DyHuCoG):** per-episode valuation, not the full catalogue.
7. **Baselines capped at early 2026:** superiority claimed only vs the tested set.

---

## Module 7 — The one central claim worth defending

> **Explanation should be part of the modelling logic itself, not a by-product attached after
> prediction.** Shapley-value attribution — because it satisfies efficiency, symmetry,
> null-player, and additivity — provides a **normative** (not heuristic) basis for allocating
> explanatory responsibility across features, interactions, and contexts.

### Quick recall checklist

- [ ] What is an *actionable* insight? (modifiable factor + domain vocabulary, not a latent code)
- [ ] What are the four Shapley axioms? (efficiency, symmetry, null player, additivity)
- [ ] Why a surrogate for clustering? (TreeSHAP explains trees, not centroids)
- [ ] What does Prop. 6.1 guarantee? (cross-level differences are *interpretable*, not noise)
- [ ] How does DyHuCoG make attribution an *in-training* signal? (Shapley-weighted message passing)
- [ ] What is the accuracy–diversity gain pattern? (both improve together; largest on sparsest data)
- [ ] What are the honest limits? (overhead, surrogate fidelity, offline/tabular, early-2026 baselines)
