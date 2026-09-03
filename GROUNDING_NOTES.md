# Grounding Notes — Mouad Louhichi's PhD Thesis & Associated Papers

> Prepared by reading all five PDFs in this repository in full. This document is a
> working reference that consolidates the thesis (159 pp.), its 3-page résumé, and
> the three peer-reviewed publications it is built on. It is intended to ground
> deep familiarity with the research arc, the fields involved, the mathematics,
> the experiments, and the claims — so the work can be summarized, defended, or
> extended without re-reading the source PDFs.

---

## 0. Repo inventory

| File | Type | Pages | Role |
|---|---|---|---|
| `MOUAD_LOUHICHI_Thesis.pdf` | Thesis (PhD, ENSIAS, Mohammed V Univ.) | 159 | The full dissertation (French résumé + English body) |
| `MOUAD_LOUHICHI_Thesis_Resume.pdf` | Thesis abstract (French) | 3 | Official 3-page résumé / abstract |
| `Shapley Values for Explaining the Black Box Nature of ML Model Clustering.pdf` | Paper I | 16 | Procedia Computer Science 220 (2023) 806–811, DOI 10.1016/j.procs.2023.03.107 |
| `Game Theory Meets Explainable AI...` | Paper II | 10 | IJACSA 16(7) (2025) 716–725, DOI 10.14569/IJACSA.2025.0160780 |
| `DyHuCoG: A Dynamic Hypergraph Cooperative Game...` | Paper III | 16 | IJIES 19(2) (2026) 887–902, DOI 10.22266/ijies2026.0228.54 |

Author: Mouad Louhichi. Supervisor: Pr. Mohamed Lazaar. Co-authors on papers: Redwane
Nesmaoui, Marwan Mbarek (paper I only), Mohamed Lazaar.
Institution: ENSIAS, Mohammed V University, Rabat, Morocco.

---

## 1. Thesis in one sentence

> Shapley values (cooperative-game attribution) are used not only as post-hoc
> explanations but as a single, shared, formally-grounded mechanism that (1) explains
> black-box clustering, (2) remains coherent when that explanation is scaled to
> large, hierarchical, multi-level clustering, and (3) becomes an **in-training
> optimisation signal** inside a dynamic hypergraph recommender (DyHuCoG).

Title: *Cooperative Game Theory for Explainable Artificial Intelligence (XAI) in
Recommendation Systems: A Shapley Framework for Actionable Insight.*

### Central claim / thesis-level argument
Attribution should be treated **as part of the modelling logic itself**, not as a
by-product attached after prediction. Cooperative game theory provides a **common
formal language** for importance allocation across tasks normally studied separately
(clustering, hierarchical interpretation, recommendation). The thesis is explicitly
presented as a **cumulative argument**, not as three unrelated papers.

### Definition 1.1 — Actionable insight
An explanation is *actionable* when it identifies **at least one modifiable factor** whose
change is associated with a specifiable change in model output, **and** that factor is
expressible in the semantic vocabulary of the task domain (physicochemical variable,
pollution indicator, preference signal) rather than in an opaque latent code.

---

## 2. The five research questions (RQ1–RQ5)

- **RQ1** — How can Shapley values adapt to explain black-box clustering so explanation is
  faithful at instance level and coherent at cluster level? → *Chapter 5.*
- **RQ2** — How can Shapley-based clustering explanation scale to large, hierarchical settings
  without losing tractability or attribution consistency? → *Chapter 6.*
- **RQ3** — Can cooperative attribution move beyond post-hoc analysis and be incorporated
  directly into the learning dynamics of graph-based recommenders? → *Chapter 7.*
- **RQ4** — Can a recommender jointly optimise ranking accuracy, contextual relevance, and
  diversity when interaction importance is estimated via a cooperative-game utility rather
  than assumed uniform? → *Chapter 7 (+ synthesis in Ch. 8).*
- **RQ5** — What insights emerge when clustering explanation and recommendation learning are
  read as two stages of one shared cooperative-game perspective? → *Thesis level, Ch. 8.*

---

## 3. The three contributions (C1–C3) and their chapters

| Contrib. | What it is | Dataset(s) | Chapter | Paper |
|---|---|---|---|---|
| **C1** | Partially model-agnostic Shapley framework for explainable black-box clustering → **PCA–K-Means–LightGBM–TreeSHAP** pipeline | Portuguese Wine Quality (4,898×11) | Ch. 5 | **Paper I** (Procedia CS, 2023) |
| **C2** | Large-scale **multi-level** clustering with hierarchical attribution aggregation + formal cross-level consistency | Beijing Multi-Site Air Quality (383,585×11) | Ch. 6 | **Paper II** (IJACSA, 2025) |
| **C3** | **DyHuCoG** — Dynamic Hypergraph Cooperative Game embed preference-aware Monte Carlo Shapley into hypergraph message passing | MovieLens-1M, Amazon-Book (aux: Yelp2018) | Ch. 7 | **Paper III** (IJIES, 2026) |

Mapping note (important): Paper I = Ch.5 single-level; Paper II = Ch.6 multi-level (wine +
Beijing); Paper III = Ch.7 DyHuCoG. The thesis adds **thesis-level synthesis** on top of the
papers (proofs, cross-chapter comparisons, explicit research-question mapping). Chapter 8 is
the synthesis; Chapter 9 is the general conclusion.

---

## 4. Fields / topics involved (the intellectual terrain)

### 4.1 Recommender systems
- **Collaborative filtering** (user-based UBCF, item-based IBCF), **content-based**,
  **hybrid**, **matrix factorisation** (R ≈ PQ^T, ŷ = pᵤᵀqᵢ).
- **Limitations motivating the thesis**: data sparsity & scalability, cold-start,
  popularity bias / lack of diversity (filter-bubble feedback loop), and **absence of
  interpretability**. The last is "the most fundamental limitation" for the thesis.
- **Graph-based recommenders**: bipartite user–item interaction graph, hypergraph extensions
  for higher-order relations, knowledge-graph-augmented recommendation.
- **GNN-based recommendation**: embedding propagation on interaction graphs (LightGCN
  simplified linear propagation + layer fusion), contrastive self-supervised learning
  (RecDCL, SimGCL, LightGCL, etc.), context-aware graph recommendation.

### 4.2 Graph / hypergraph neural networks
- **Message passing**: hᵥ^(ℓ+1) = φ(hᵥ^(ℓ), AGG_{u∈N(v)} ψ(hᵥ^(ℓ), hᵤ^(ℓ), eᵤᵥ)).
- **GCN**: spectral smoothing; weakness = oversmoothing with depth, unnecessary feature
  transforms.
- **LightGCN**: eᵤ^(ℓ+1) = Σ_{i∈N(u)} (1/√(|N(u)||N(i)|)) eᵢ^(ℓ); final eᵤ = Σℓ αℓ eᵤ^(ℓ).
  Lesson for the thesis: structural propagation matters more than neural complexity.
- **Hypergraph NN**: propagation through hyperedges (incidence matrix H, node-degree Dᵥ,
  hyperedge-degree Dₑ):
  E^(ℓ+1) = σ(Dᵥ^(-1/2) H W Dₑ^(-1) Hᵀ Dᵥ^(-1/2) E^(ℓ)).
  Hypergraphs express **multiway** interactions (user–item–context) irreducible to dyads.
- **Attention** in GNNs (GAT) — can weight neighbours, but attention weights alone don't
  guarantee fairness/completeness/symmetry. The thesis argues Shapley weighting is a more
  principled account of importance than attention.

### 4.3 Explainable AI (XAI)
- Taxonomy: intrinsic vs post-hoc; local vs global; model-specific vs model-agnostic.
- **Post-hoc**: LIME (local surrogate, perturbation-sensitive), SHAP (additive,
  axiomatic), integrated gradients, counterfactuals.
- **Evaluation of explanations** is multi-criterion in the thesis: formal coherence,
  local accuracy, stability under approximation, semantic plausibility, usefulness for
  downstream analysis (NOT just visual plausibility). Faithfulness via deletion/insertion;
  stability under perturbation; sparsity/usability; causability (human-centred).
- The thesis position: SHAP-family methods have a **normative** (axiom-backed) basis that
  ad-hoc or purely local methods (esp. LIME) lack — crucial for cluster comparison and for
  regulatory/trustworthy-AI motivations (EU AI Act, OECD AI principles, GDPR).

### 4.4 Cooperative game theory & Shapley values (theoretical backbone)
- **Transferable-utility (TU) game**: G = (N, v), v: 2^N → ℝ.
- **Shapley value** (axiomatic): φᵢ(v) = Σ_{S⊆N\{i}} [|S|!(|N|-|S|-1)!/|N|!] [v(S∪{i}) − v(S)].
- **Four axioms** (all satisfied uniquely by Shapley):
  - **Efficiency**: Σφⱼ = v(N) − v(∅) — all explanatory mass allocated (completeness).
  - **Symmetry**: identical marginal contributors get equal allocation (fairness).
  - **Null player**: zero marginal contributor gets zero (no spurious credit).
  - **Additivity**: φ(v+w) = φ(v) + φ(w) — explanations compose (linearity).
- Compared to alternatives: **Banzhaf index** (not efficient in standard form), **nucleolus**
  (dissatisfaction-minimisation, not additive feature attribution).
- **Approximation**: exact is exponential. **Monte Carlo** estimator
  ˆφⱼ = (1/M) Σ_m [v(S_m ∪ {j}) − v(S_m)]; unbiased, variance = σ²/M (MSE → O(1/M),
  absolute error → O(1/√M)).
- **TreeSHAP** (exact/fast for tree ensembles; used because LightGBM surrogate is a tree model)
  and **KernelSHAP** (general but costlier).
- **Preference-aware variants**: FW-Shapley (weighted real-time), Owen-style coalition
  structure (pre-specified unions). **DyHuCoG avoids exogenous coalition blocks**; it uses
  an **additive preference-consistency bonus** inside the utility → weighted utility
  modulation rather than coalition-structure redefinition.
- Important caveat: SHAP explains the **surrogate's** multiclass prediction game, not the
  K-Means geometry. Efficiency holds w.r.t. the LightGBM log-odds output, i.e.
  Σφ = f(x) − E[f(x)].

### 4.5 Clustering & dimensionality reduction
- **PCA**: Y = XW; explained-variance ratio rₖ = λₖ/Σλᵢ. Used as a computational/visual aid,
  **deliberately not** as the explanatory space.
- **K-Means** (K-Means++ init): J = Σᵢ Σ_{x∈Cᵢ} ‖x − μᵢ‖². Non-deterministic → multiple runs.
- **Validation metrics**: Silhouette s(x) = (b(x)−a(x))/max{a,b}; Davies–Bouldin
  DB = (1/k) Σᵢ max_{j≠i} ((σᵢ+σⱼ)/d(μᵢ,μⱼ)); also Calinski–Harabasz (CH) and elbow method.
- **Surrogate classifier**: LightGBM (tree-boosting, leaf-wise growth) trained to predict
  the *induced* cluster labels from the **original** feature space → enables TreeSHAP on
  the original variables.

---

## 5. Method / protocols (shared across chapters — Ch. 4)

### 5.1 Datasets
| Dataset | Users / Instances | Items / Features | Interactions / Period | Density |
|---|---|---|---|---|
| Wine Quality (Portuguese "Vinho Verde", white) | 4,898 | 11 physicochemical | single snapshot | — |
| Beijing Multi-Site Air Quality | 383,585 hourly | 11 (PM2.5, PM10, NO2, SO2, CO, O3, temp, pressure, dew point, wind dir, wind speed) | 2013–2017 | — |
| MovieLens-1M | 6,040 users | 3,706 items | 1,000,209 | 0.0447 |
| Amazon-Book | 52,643 users | 91,599 items | 2,984,108 | 0.0006 |

- **Implicit conversion**: MovieLens-1M ratings **> 3** treated as positive implicit feedback.
- Clustering datasets have **semantically interpretable features** (selection criterion);
  recommendation datasets are **benchmark-standard** with established baselines.

### 5.2 Splitting
- **Recommendation**: user-level, temporal holdout. Sort per user by time → 70% train /
  10% val / 20% test. **Leave-one-out** evaluation: the latest test positive per user is the
  target, ranked against sampled negatives.
- **Clustering**: 5-fold CV where appropriate to test surrogate/attribution stability.

### 5.3 Baselines
- **Recommendation**: MF, NCF, LightGCN, RecDCL, HCCF, HPCF (HPCF = strongest reference).
- **Clustering interpretability**: LIME-based surrogate pipeline (Perturbation-sensitive local
  surrogate, ξ(x) = argmin_g L(f,g,π_x) + Ω(g)).

### 5.4 Metrics
- **Ranking**: Precision@K, Recall@K, NDCG@K (NDCG@20 primary; DCG = Σ (2^rel − 1)/log₂(i+1)).
- **System-level**: Catalogue Coverage = |∪ᵤ Rᵤ| / |I|.
- **List-level diversity**: ILD(Rᵤ) = (2/(K(K−1))) Σ_{a<b} [1 − sim(iₐ,i_b)] (cosine sim in
  learned item space). **Built into the coalition utility** (not decorative).
- **Clustering**: Silhouette, Davies–Bouldin.

### 5.5 Training / optimisation / statistics
- BPR pairwise ranking loss: L_BPR = −Σ_{(u,i⁺,i⁻)} log σ(ŷ_{ui⁺} − ŷ_{ui⁻}).
- L2 regularisation: L_reg = (λ/2)‖Θ‖². Early stopping on validation NDCG@20.
- **Reproducibility**: seeds {42,43,44,45,46}; 5 seeds; early-stopping patience 20.
- **Statistical validation**: paired t-test per-user NDCG@20; **Holm–Bonferroni** correction;
  **Wilcoxon signed-rank** as non-parametric robustness check; **Cohen's d_z** effect size.
- **Hardware**: CPU Intel i9-14900K (24 cores), GPU RTX 4090 24GB, 48GB RAM, 2TB SSD.
- **Software**: Python 3.8, scikit-learn, LightGBM, SHAP, PyTorch 2.0.1, SciPy, NumPy, pandas;
  Altair for interactive visualisation.

---

## 6. Chapter 5 — C1 (explainable black-box clustering)

### Cooperative-game formulation (clustering)
- Player set **N = F** (features). Coalition value = clustering quality of feature subset:
  **v(S) = Silhouette[KMeans(X_S, k*)]**. Alternative metrics (DB, CH) possible but Silhouette
  chosen (bounded, normalised, intuitive).
- **Problem**: direct evaluation of v(S) for every coalition is intractable.
- **Bridge**: once K-Means yields labels, train a **LightGBM multiclass surrogate** to predict
  those labels from original features; apply **TreeSHAP**. Surrogate's multiclass loss with
  cross-entropy on induced labels. **Validity depends on surrogate fidelity**; thesis treats
  macro-F1 ≥ ~0.80 as the practical floor.

### Pipeline (5 stages)
1. Feature standardisation → 2. PCA (stabilise geometry + visualisation) → 3. K-Means++ +
   optimal-k selection → 4. LightGBM surrogate → 5. TreeSHAP attribution in original feature space.

### Key empirical results (Wine)
- **k-selection is by interpretability, NOT geometry.** k=2 gives Silhouette 0.214, DB 1.775;
  selected **k=3 gives Silhouette 0.144, DB 2.097** — weaker separation but more interpretable
  oenological segmentation (three distinct cluster narratives).
- **Global feature importance**: density, pH, fixed acidity, sulfur-dioxide variables, alcohol
  (chemically interpretable hierarchy; density dominant).
- **Cluster profiles (Fig 5.2)**: Cluster 0 ~ density + sulfur-dioxide; Cluster 1 ~ acidity/pH;
  Cluster 2 ~ acidity, alcohol, related chemicals.
- **Surrogate fidelity**: ~macro-F1 0.82 (shared default 100-tree / 31-leaf LightGBM) — the wine
  paper itself didn't tabulate a standalone F1 table; thesis treats it as a standing condition.

### SHAP vs LIME (Table 5.1)
| Criterion | SHAP | LIME |
|---|---|---|
| Basis | Cooperative-game marginal contribution | Local surrogate approximation |
| Local/global | Both | Primarily local |
| Theoretical guarantee | Efficiency, symmetry, null player, additivity | None equivalent |
| Stability | Higher when surrogate faithful | Sensitive to perturbation design |
| Cluster comparison | Strong | Limited |

### Findings / claims
- LIME comparison is presented as **theoretical + literature-backed**, not a full empirical
  bake-off on wine (bounded scope, stated honestly).
- The explanation explains the **faithful surrogate reconstruction of the partition** (not
  K-Means geometry mechanistically).
- **Partially model-agnostic**: flexible at clustering stage, tree-specific at explanation stage.

---

## 7. Chapter 6 — C2 (multi-level, large-scale XAI)

### Motivation
Beyond scale, the real issue is **multi-granularity**: a variable can be globally important yet
locally uninformative (or vice-versa). Flat explanation is "true yet incomplete." The chapter adds:
(1) a genuine multi-level workflow, (2) a **formal cross-level consistency** interpretation
(Prop 6.1), (3) validation on a structurally different large-scale dataset.

### Hierarchical design (pragmatic, not ontological)
Nested clustering as an **analytical device** — the framework does NOT claim data has a true
ontology of hierarchy. Coarse clustering → subdivide each cluster → train level-specific surrogate
+ compute SHAP in the same original feature space → **size-weighted cross-level aggregation**.

### Formal result — Proposition 6.1 (Hierarchical Attribution Consistency)
Let Φ^(ℓ,c)ⱼ = E_{x~c}[|φⱼ^(ℓ)(x)|] = expected absolute SHAP importance of feature j at level ℓ in
cluster c, and w_{c'} = |c'|/|c| be relative child size. For a strict nested hierarchy on a
**consistent feature space**:

  Φ^(ℓ,c)ⱼ = Σ_{c' ∈ child(c)} w_{c'} Φ^(ℓ+1,c')ⱼ + εⱼ

where εⱼ is a residual from surrogate mismatch → 0 under perfect surrogate fidelity.
- Derived via **law of total expectation** and the fact that child clusters partition the parent.
- Does **not** imply explanations are identical across levels; it implies differences can be
  *interpreted* rather than dismissed as inconsistency.
- Proof sketch in Appendix A.2. εⱼ treated as a **conceptual residual**, not empirically
  estimated (no separate Beijing residual analysis).

### Key empirical results (Beijing)
- Clustering full dataset, **k=3**; **Silhouette ≈ 0.63, Davies–Bouldin ≈ 0.55** (much clearer
  separation than wine; do NOT confuse with wine's 0.144/2.097).
- Global feature importance: **temperature, dew point, pressure** dominant; then CO, NO2,
  PM10, PM2.5. (Meteorological variables condition dispersion/trapping/photochemistry → they
  structurally define pollution regimes.)
- **Three regimes (Fig 6.2 force plots)**: warm photochemical (ozone, temp, dew point); wintertime
  smog (CO, SO2, PM, low wind); cleaner/well-dispersed events (favourable meteorology, weak pollutants).
- **Multi-level insight**: at coarse level temp/dew point dominate (regime selection); within
  clusters CO, SO2, PM10, wind speed, pressure, ozone become discriminative (variation within regime).
  This change is the *point* of a multi-level explanation, not a contradiction.

### Comparative
- vs Gramegna & Giudici (credit-risk, SHAP-space): Beijing Silhouette 0.63 vs their 0.37.
- vs LIME: less stable, weaker structural coherence for hierarchical reasoning.
- **Cross-dataset (Table 6.2)** wine vs Beijing: small/dense/determinable vs large/heterogeneous
  → tests explanation under two complexity regimes; same logic remains productive ⇒ generalisable.

### Limitations
Still **static** (despite temporal Beijing data); relies on surrogate + representative-instance
reporting (compresses observation-level variation); confined to tabular data.

---

## 8. Chapter 7 — C3 (DyHuCoG, the flagship)

### What it is
A **Dynamic Hypergraph Cooperative Game** recommender. Embeds **preference-aware Monte Carlo
Shapley** estimates as dynamic hyperedge weights into a lightweight hypergraph GNN with an
**interaction-level attention gate**, trained with a multi-objective loss (ranking + diversity
+ context alignment + regularisation).

**Conceptual shift**: attribution is no longer post-hoc commentary — it's a training signal that
determines how information flows through the hypergraph.

Formally, at §7.5:
- Base propagation: e^(ℓ+1) = σ(D^{-1/2} A D^{-1/2} e^(ℓ)).
- Shapley-weighted: e_j^(ℓ+1) = σ(W^(ℓ) e_j^(ℓ) + Σ_{k∈N(j)} w_jk e_k^(ℓ)).
- Normalised neighbourhood weights: **w_jk = φ̂_jk / Σ_{k'∈N(j)} φ̂_jk'** (φ̂ clipped +
  exponentially smoothed before normalisation).
- Layer fusion: e_j = Σ_{ℓ=0}^L α_ℓ e_j^(ℓ) (α_ℓ **learned**).
- Attention gate: a_ui = σ(W_a[e_u, e_i, l_i]).
- Intermediate score: y_ui = (1 + a_ui) ⟨e_u, e_i⟩.
- Final context-aware score: f(u,i,c) = y_ui + λ_c ⟨g(c_ui), e_cui⟩.

### Cooperative game (recall notation)
- Players N = U ∪ I ∪ C. Coalition S ⊆ N. Hypergraph H=(V,E,W), V=U∪I∪C.
- **Multi-objective utility**:
  v(S) = α·NDCG@20(S) + β·Diversity(S) + γ·ContextScore(S), with α+β+γ=1.
- **Preference-weighted**:
  v_pref(S) = v(S) + λ_pref·Σ_{(u,i)∈S} sim(u,i).
- α,β,γ tuned by grid search over [0.1,0.8] with α+β+γ=1. **α=0.60, β=0.25, γ=0.15**;
  **λ_pref = 0.20**. NDCG@20 variance < 1.5%.
- Coalition evaluation is **scoped to the interaction episode** (one focal user + small candidate
  item set + context nodes → player set of a few dozen, NOT the full catalogue). Read as an
  approximate in-training valuation aligned with the local recommendation context.

### Monte Carlo Shapley (preference-aware)
- Exact φ_j = Σ_{S⊆N\{j}} [|S|!(|N|−|S|−1)!/|N|!] [v(S∪{j}) − v(S)] (infeasible).
- MC estimator: φ̂_j = (1/M) Σ_m [v(S_m∪{j}) − v(S_m)].
- Preference-aware: φ̂_j^pref = (1/M) Σ_m [v_pref(S_m∪{j}) − v_pref(S_m)].
- Unbiased; variance σ²/M. **M = 50** chosen: MSE ≈ 1.4×10⁻⁵, ~99% accuracy on MovieLens-1M.
- **Refresh smoothing**: refresh every **10 batches** (~49 updates/epoch on ML-1M, batch 2048);
  exponential moving average with decay ρ. Treats attribution as adaptive but not hypersensitive.

### Multi-objective training
- L = L_rec + λ_div L_div + λ_ctx L_ctx + λ_reg L_reg.
- **L_rec**: BPR pairwise (scores of positive > negative).
- **L_div**: L_div = −(1/|U|) Σ_u ILD(R_u) (penalises redundant lists).
- **L_ctx**: L_ctx = (1/|E|) Σ_{(u,i)} ‖g(c_ui) − e_cui‖₂² (align context embedding with
  context-node representation).
- **L_reg**: (1/2)(‖E_U‖_F² + ‖E_I‖_F²).
- Optimiser: Adam. Negatives from **popularity-aware** distribution (q(i) ∝ f_i^η) + periodic
  hard-negative refresh.

### Key empirical results
**Main performance (Table 7.1)** — mean ± std over 5 seeds:

| Dataset | Model | NDCG@20 | Recall@20 | Coverage | Diversity(ILD) |
|---|---|---|---|---|---|
| ML-1M | HPCF | 0.2528 | 0.2098 | 0.342 | 0.461 |
| ML-1M | **DyHuCoG** | **0.2775** | **0.2362** | **0.397** | **0.516** |
| Amazon | HPCF | 0.0270 | 0.0359 | 0.259 | 0.535 |
| Amazon | **DyHuCoG** | **0.0306** | **0.0417** | **0.336** | **0.602** |

Relative to HPCF:
- ML-1M: **+9.77% NDCG@20, +12.58% Recall@20**; coverage 0.342→0.397 (+16.1%); ILD 0.461→0.516 (+11.9%).
- Amazon: **+13.33% NDCG@20, +16.16% Recall@20**; coverage 0.259→0.336 (**+29.7%**); ILD 0.535→0.602 (+12.5%).
- **Interpretation**: largest relative gain on the sparser benchmark supports the claim that
  Shapley-guided weighting helps most when interaction data are weak.

**Ablation (Table 7.2)** — % drop in NDCG@20 (ML-1M / Amazon):
- w/o Shapley Value: −4.6% / −6.1% (0.2647 / 0.0287) *→ supports non-decorative attribution.*
- w/o Hypergraph: −6.8% / −8.9% (0.2586 / 0.0279).
- w/o Attention: −3.5% / −3.5% (0.2678 / 0.0295).
- w/o Context: **−8.2% / −11.0%** (0.2547 / 0.0272) *→ largest single removal.*
- w/o Diversity: −5.8% / −5.8% (0.2614 / 0.0288).

**Runtime/scalability (Table 7.3)**: DyHuCoG ~2000.2s train (ML-1M) vs HPCF 1124.6s (~1.78×);
inference 1.84ms/query (ML-1M), 8.52ms (Amazon); memory 4.4GB vs 4.1GB (ML-1M). Amazon:
9278.9s vs 5234.2s. Per-epoch cost O((L+1)md) + O((M/f)m).

**MC convergence (Table 7.4)** — MovieLens-1M:
| M | MSE | Accuracy | Runtime | Overhead vs HPCF | Recommendation |
|---|---|---|---|---|---|
| 10 | 1.4e-4 | 95% | ~1460s | 1.3× | Minimum viable |
| 25 | 5.6e-5 | 98% | ~1800s | 1.6× | Lightweight |
| 50 | 1.4e-5 | 99% | 2001s | 1.78× | **Production** |
| 100 | 3.5e-6 | 99.5% | ~2810s | 2.5× | High-accuracy |

**Cold-start & cross-dataset (Table 7.5)** (NDCG@20):
- Cold-start user 0.061 (+10.9% vs HPCF 0.055); cold-start item 0.057 (+9.6% vs 0.052).
- Cross-dataset: ML +9.9%, Amazon +14.8%, Yelp2018 +11.8% (Yelp2018 = auxiliary robustness
  benchmark, NOT a third primary benchmark).
- Note small discrepancy: paper text says "+9.8%" and cold-start user "0.0606", while the
  thesis table shows "+10.9%" and 0.061 — likely rounding.

**Paired t-tests (Table 7.6)** — per-user NDCG@20, n=6040, df=6039:
| Comparison | t | p | Cohen's d_z | Holm α_i |
|---|---|---|---|---|
| vs HPCF | 46.38 | 1.81e-270 | 1.3345 | 0.050000 |
| vs RecDCL | 92.72 | <1e-300 | 2.6677 | 0.008333 |
| vs HCCF | 61.21 | <1e-300 | 1.7610 | 0.010000 |
| vs LightGCN | 132.19 | <1e-300 | 3.8035 | 0.012500 |
| vs NCF | 311.13 | <1e-300 | 8.9518 | 0.016667 |
| vs MF | 341.76 | <1e-300 | 9.8330 | 0.025000 |
- All significant after Holm–Bonferroni; Wilcoxon signed-rank also p<0.001.
- **Scope discipline**: fully tabulated paired tests apply ONLY to MovieLens-1M per-user
  NDCG@20; Amazon-Book and auxiliary metrics remain descriptive.

### Limitations (DyHuCoG)
- Measurable computational overhead vs strongest baselines; depends on availability of meaningful
  context; MC Shapley could be improved by variance reduction; ablation is component-wise (no
  factorial interaction effects tested); Monte Carlo convergence reported via MSE+runtime, not a
  downstream NDCG@20-vs-M table; explanation evaluated via structural plausibility/utility
  decomposition, not a large-scale user study. Baselines finalised early-2026; later models
  (e.g. post-2024 LLM-augmented recommenders) **not** audited — superiority claimed only vs the
  tested baseline set.

---

## 9. Chapter 8 — Synthesis & Chapter 9 — Conclusion

- Three synthesis-level findings: (1) **methodological** — cooperative attribution transfers across
  model families/data types when the game is defined to match task structure; (2) **conceptual** —
  the real problem is *allocation of explanatory responsibility* (which feature/interaction/context
  counts as important, by how much, under what guarantees); (3) **actionability** — explanations are
  more actionable when they identify modifiable drivers, not merely describe.
- **Theoretical implications**: Shapley reasoning = common formal language across tasks; explanation
  and optimisation need not be temporally separated (DyHuCoG) — this is the strongest conceptual
  advance; axiomatic basis supports trustworthy-AI/transparency language better than persuasive-but-
  underspecified methods.
- **RQ answers** (Ch. 9): RQ1–RQ4 yes (with bounds); RQ5 answered at thesis level (a shared
  importance-allocation framework).
- **Consolidated limitations**: computational (approximation everywhere); methodological (depends on
  surrogate fidelity / stability of approximate contributions / adequacy of context); empirical
  (no multimodal/sequential/online, no human-subject actionability study); claim scope (not a single
  unified framework eliminating all tension).
- **Future work**: lower-variance Shapley & learned proposal distributions & adaptive refresh;
  online/streaming (incremental graph evolution, delayed feedback); richer human-centred evaluation;
  trustworthiness/fairness/governance audits.

---

## 10. Mathematical appendix highlights (A & B)

- **A.1 Uniqueness of Shapley value**: expr (v) as linear combination of unanimity games
  u_T (u_T(S)=1 iff T⊆S); show φ on unanimity basis: φᵢ(u_T) = 1/|T| if i∈T, 0 if i∉T; additivity
  + agreement on all unanimity games ⇒ φ = Shapley.
- **A.2 Hierarchical consistency**: law of total expectation + child partition ⇒
  Φ^(ℓ,c)ⱼ = Σ_r Pr(x∈cᵣ|x∈c)·Φ^(ℓ+1,cᵣ)ⱼ + εⱼ; under perfect fidelity εⱼ=0.
- **A.3 MC convergence**: Z_j(π) = v_pref(S_j(π)∪{j})−v_pref(S_j(π)); φ̂^(M)ⱼ unbiased;
  Var = σ²/M ⇒ RMSE O(M^{−1/2}), MSE O(M^{-1}). (Wording care: variance/MSE at rate 1/M,
  absolute error in probability at 1/√M.)
- **A.4 Composite-loss stability (DyHuCoG)**: L = L_BPR + μ₁L_ILD + μ₂L_ctx + λ‖Θ‖₂². No full
  non-convex convergence theorem; instead a **stability** statement: within each refresh interval
  (components L-smooth, unbiased stochastic gradients w/ bounded 2nd moment, refresh perturbs
  objective by ≤ρ in operator norm) standard non-convex arguments give decreasing average gradient
  norm; small ρ keeps trajectory in a slowly drifting basin (bounded descent, not global convergence).
- **A.5 Preference-weighted utility**: v_pref(S) = v(S) + λ_pref Σ p_ui; marginal contribution of
  player j=(u,i) is [v(S∪{j})−v(S)] + λ_pref·p_j ⇒ additive shift + coalition-aware first term.

### Algorithms (Appendix B)
- **B.1** PCA–KMeans–LightGBM–SHAP pipeline (global + cluster-specific + local force plots).
- **B.2** Multi-level clustering with size-weighted cross-level SHAP aggregation.
- **B.3** Preference-aware Monte Carlo Shapley estimator (O(Mn) coalition evals).
- **B.4** DyHuCoG training loop with periodic Shapley refresh (mod every Δ; smooth EMA).
- **B.5** Popularity-aware negative sampling (q(i) ∝ f_i^η).

---

## 11. Reproducibility (Appendices C–F) & honesty boundaries

- Config (Table D.1): L=3 layers, d=64, M=50, refresh every 10 batches, (α,β,γ)=(0.60,0.25,0.15),
  λ_pref=0.20; negative-sampling exponent η is a **scheme-level setting** (no standalone scalar).
- The thesis is careful about **not fabricating statistics**: no per-seed raw logs distributed;
  no reconstructed Amazon-Book paired tests; MC convergence shown via MSE+runtime not a separate
  metric-sensitivity table; Yelp2018 only as auxiliary robustness.
- No public archival code URL claimed; the appendix documents the *expected* repository structure
  and reproducibility workflow rather than claiming external end-to-end audit.

---

## 12. Noted discrepancies / points of care (for defense)

1. **Paper II DOI mismatch**: Résumé/abstract lists `10.14569/IJACSA.2025.0160770`; the thesis
   "List of Publications" and the paper itself use `10.14569/IJACSA.2025.0160780`. Verify the
   canonical DOI.
2. **Cold-start numbers**: DyHuCoG paper §4.8 text says cold-start user 0.0606 / "+9.8%"; the
   thesis Table 7.5 and the paper's own Table 8 show 0.061 / "+10.9%" (and item 0.057 / +9.6%).
   Likely rounding / minor inconsistency.
3. **Wine vs Beijing Silhouette**: The thesis repeatedly warns that the ~0.63 Silhouette belongs
   to Beijing, NOT the retained wine k=3 (0.144). Do not conflate.
4. **k=3 wine selection is interpretability-driven, not geometry-driven** — this is a deliberate,
   defensible choice, and the thesis says so explicitly.
5. **"Unified framework" scope restraint**: The thesis does NOT claim one fully unified mathematical
   framework eliminating all tension; it claims a *shared perspective* / common attribution language.
6. **SHAP efficiency scope**: In the surrogate pipeline, efficiency holds w.r.t. the LightGBM
   surrogate output, not the Silhouette-based game directly.
7. **Scoped player set in DyHuCoG**: coalition evaluation is per-episode (a few dozen players), not
   the full catalogue — the estimator is an *approximate in-training valuation*, an honest boundary.
8. **Baselines capped at early 2026**: superiority claimed only vs the tested set (MF, NCF,
   LightGCN, RecDCL, HCCF, HPCF); later models not audited.

---

## 13. Quick "punch list" — what this research is really about

- **Core question**: What is the principled way to allocate *explanatory responsibility*
  (which feature / interaction / context is important, by how much, under what guarantees)?
- **Answer** (thesis claim): Shapley-value attribution — because it satisfies efficiency,
  symmetry, null-player, and additivity, providing a normative (not heuristic) basis.
- **Three demonstrations of transferability**:
  1. Explain unsupervised clusters (wine) — post-hoc, single-level.
  2. Scale + hierarchy (Beijing air quality) — post-hoc, multi-level, with a formal
     cross-level consistency property.
  3. Put the same attribution inside the learning loop (DyHuCoG, MovieLens & Amazon) — the
     strongest claim: attribution becomes an *in-training* signal, improving accuracy,
     coverage, and diversity **together**.
- **Broader significance**: a foundation for transparent / accountable / trustworthy AI
  (ties to EU AI Act, OECD AI principles, GDPR) where explanation is an accountability
  mechanism, not a usability add-on.

---

## 14. Keywords
Explainable AI (XAI), Cooperative Game Theory, Shapley Values, Recommender Systems,
Hypergraph Neural Networks, Graph Neural Networks, Interpretable Clustering, Feature
Attribution, Intra-List Diversity (ILD), Trustworthy AI, PCA, K-Means, LightGBM,
TreeSHAP, Transparent/Accountable AI.
