# Grounding Notes — Redwane Nesmaoui's PhD (Colleague) — "Example PhD Pass"

> Prepared by reading the colleague's full PhD defense package that was added to
> `main` (commit `ae0ce7f add example phd`, folder `example-phd-passes/`). The
> user asked me to ground deeply on it, "especially on the presentation". The
> **presentation** is the priority deliverable of this grounding: it is an 80-slide
> PhD viva deck with full speaker notes (`Presentation1 (1) (1).pptx`). I have read
> every slide and every note, plus the thesis PDF (154 pp.), the 2-page résumé,
> and the VIVA PDF (same deck exported to PDF, image-heavy so text is sparse).

---

## 0. Repo inventory of the colleague's materials

| File | What it is | Notes |
|---|---|---|
| `Presentation1 (1) (1).pptx` | **The viva presentation** (13.33×7.5 in, 80 slides, speaker notes) | PRIMARY FOCUS |
| `Thesis_Redwane_NESMAOUI.pdf` | Full PhD thesis (154 pp.) | Abstract + TOC + contributions read |
| `ResumeThese_Redwane_NESAMOUI 2.pdf` | 2-page French résumé | Read in full |
| `VIVA_Redwane_NESMAOUI.pdf` | The viva deck as PDF (77 pp., mostly images) | Same content as pptx |

> Relationship to the user's work: both are PhDs from the **same lab/supervisor
> (Pr. Mohamed Lazaar, ENSIAS–UM5 Rabat)**, and Redwane Nesmaoui is actually a
> **co-author on the user's own papers** (Papers I & II in `MOUAD_LOUHICHI_Thesis`).
> So this is a genuine "like mine" (`passe comme le mien`) reference: same group,
> same XAI + Shapley + recommender-Systems thread, diverging on architecture
> (Mouad → clustering + hypergraph recommendation; Redwane → graph CF + adaptive
> Shapley + hyperbolic hierarchical modeling).

---

## 1. The presentation at a glance

- **Title:** *Explainable Artificial Intelligence (XAI) for Decision-Making in Graph-Based Recommendation Systems*
- **Presented by:** Redwane NESMAOUI
- **Doctoral center:** ST2I (Doctoral Studies Center in Information and Engineering Sciences and Technologies)
- **Institution:** ENSIAS, Mohammed V University, Rabat
- **Defense date/status:** PhD viva, Rabat, 2026

### Jury
| Role | Name | Grade | Affiliation |
|---|---|---|---|
| President | Pr. Abdellatif EL AFIA | PES | ENSIAS, UM5, Rabat |
| Supervisor | Pr. Mohamed LAZAAR | PES | ENSIAS, UM5, Rabat |
| Reviewer | Pr. M'hamed AIT KBIR | PES | FST, Abdelmalek Essaâdi Univ., Tangier |
| Reviewer | Pr. Oussama MAHBOUB | PES | ENSA, Abdelmalek Essaâdi Univ., Tetouan |
| Reviewer | Pr. Noureddine KERZAZI | MCH | ENSIAS, UM5, Rabat |
| Examiner | Pr. Hicham OMARA | MCH | FP Taza, Sidi Mohamed Ben Abdellah Univ., Fez |
| Examiner | Pr. Fatima OUZAYD | PES | ENSIAS, UM5, Rabat |
| Examiner | Pr. Yasser EL MADANI EL ALAMI | MCH | ENSIAS, UM5, Rabat |
| Guest | Pr. Yassine AFOUDI | MC | Fac. Sciences, Cadi Ayyad Univ., Marrakech |

### Viva outline (slide 2)
Structure of the talk: **Introduction** (recommenders, black-box problem, why XAI) →
**Context & Problematic** (limitations, research gap) → **Protocols** (datasets, baseline,
metrics, hardware) → **Three Contributions** (GNN-CF; Adaptive Shapley; Hyperbolic GNN+XAI)
→ **Conclusion & Perspectives** (synthesis, limitations, future work). Each contribution
follows the same structure: *objectives → methodology → results → findings*.

---

## 2. Context & problematic (slides 3–16)

### Motivation (slide 4)
- **Ubiquity:** How do recommender systems shape what billions of users see, buy, watch daily?
- **The black box:** Why do state-of-the-art graph-based RS remain opaque to users & designers?
- **Toward trust:** How can transparency be built *as part of* the recommendation process, not afterwards?
- Motivating refs: Zhang & Chen (Explainable Recommendation survey), Gunning & Aha (DARPA XAI),
  Das & Rad, Linardatos et al., Kunkel et al. (trust & explanations, CHI), Jacovi et al. (formalizing trust, FAccT).

### Real-world context (slides 5–7)
Examples: **Netflix, Spotify, Yelp, Amazon** — all rely on recommendation engines. Speaker notes
emphasize Netfix's ~$1B/yr retention value from recommendations → scale amplifies small biases.

### Recommendation system paradigms (slides 10–14)
- **Content-based filtering** (features + user profile; limitation: over-specialization / lack of diversity).
- **Collaborative filtering** (behavior of similar users; user-based or item-based; limitation: cold-start).
- **Hybrid** (combines both; mitigates cold-start, overspecialization).
- **Graph-based RS** (users/items/interactions as nodes/edges, multi-hop, embeddings/GNN; limitation: compute/memory).
- **Cold-start problem** (user/item with insufficient data; common mitigations listed).

### The three structural problems (slide 15)
1. **Lack of explainability** — graph recommenders are black boxes.
2. **Weak adaptability** — existing explainability methods are post-hoc and weakly integrated;
   user preferences evolve but most models don't adapt.
3. **Limited hierarchical modeling** — hierarchies (categories/subcategories/taxonomies) are
   poorly represented in conventional Euclidean spaces.

**Objective:** design a **unified framework combining accuracy, explainability, adaptability,
and hierarchical modeling.**

### Three concrete contributions (slide 16)
1. **GNN-based collaborative filtering** (LightGCN-style recommender);
2. **Shapley-value-based explanation of historical user–item interactions** + adaptive
   contribution-aware inference-time reweighting;
3. **Hierarchical recommendation with hyperbolic GNNs** (combines hierarchy-awareness with explainability).
   All validated on MovieLens and Amazon.

---

## 3. Shared experimental protocol (slides 17–27)

### Datasets
| Dataset | Users | Items | Interactions | Sparsity | Min per user |
|---|---|---|---|---|---|
| MovieLens 100K | 943 | 1,682 movies | 100,000 ratings | 93.7% | 20 |
| MovieLens 1M | 6,040 | 3,952 movies | 1,000,209 ratings | 95.8% | 20 |
| Amazon Products | ≈15.5 M | ≈9.4 M products | ≈233.1 M reviews | extremely sparse | none |

- MovieLens 100K: fast prototyping / ablations. MovieLens 1M: the long-standing standard
  (LightGCN, NGCF, most GNN recommenders). Amazon (McAuley Lab, 2018): realistic large sparse
  scale, tests generalization beyond movies; has review text (flagged as future work, not used).
- **Feedback:** explicit ratings 1–5 (with timestamps); Amazon also has textual reviews.

### Metrics
Precision@10, Recall@10, F1@10 for top-K recommendation. (Speaker notes: "I won't read the
formulas, happy to detail in questions.")

### Hardware (slide 27)
- Contribution I: **Lenovo ThinkPad X1 Carbon** — Intel Core i7-7600U, 16 GB RAM, 512 GB.
- Contributions II & III: **MacBook Pro** — Apple M4 Max, 48 GB RAM, 1 TB.

---

## 4. Contribution I — GNN-CF (slides 28–39)
> Based on: *A Collaborative Filtering Movies Recommendation System based on Graph Neural Network*
> (ANT/EDI40, 2023; Procedia CS 220, 456–461).

### Research gap
Sparse matrices give weak signals; classical CF misses indirect multi-hop user–item relations;
matrix models ignore the natural graph structure. → Need a graph-CF model exploiting higher-order
connectivity *without side information*.

### Research questions → objectives (slide 30)
- RQ1.1 Does graph-based link prediction beat traditional CF? → Compare LightGCN vs UBCF/IBCF/MF/SVD/SVD++.
- RQ1.2 Do multi-hop propagation + layer aggregation help? → Combine representations across layers.
- RQ1.3 Can a simple graph model support stable future extensions? → Linear aggregation + inner-product scoring.
- RQ1.4 What limitations remain despite accuracy? → Identify static/uniform/opaque interactions (motivates Contr. II).

### Methodology
- Euclidean space (slide 31) as the standard embedding geometry (MF, word embeddings, most GNNs incl. LightGCN).
- Pipeline (slides 33–34): user–item interactions → bipartite graph → embedding init → multi-layer
  neighborhood aggregation → layer fusion → inner-product prediction (the LightGCN-style design).

### Results (slide 35) — MovieLens link-prediction (Precision / Recall)
| Method | Precision | Recall |
|---|---|---|
| UBCF | 0.7423 | 0.8015 |
| IBCF | 0.7689 | 0.8247 |
| MF | 0.8012 | 0.8619 |
| SVD | 0.8294 | 0.8896 |
| SVD++ | 0.8627 | 0.9138 |
| **LightGCN-CF** | **0.9101** | **0.9625** |

**Key findings:** best of all baselines; biggest gain in recall; captures multi-hop patterns
invisible to matrix methods. **Caveat: this is link-prediction, not full top-N ranking.**

### Findings / limitations
- Graph structure improves prediction; higher-order neighborhoods improve recall; simple architectures suffice.
- Accuracy is not enough — model remains static and opaque.
- **Limitations (slide 38):** closely follows LightGCN (not fundamentally novel); only MovieLens-100k,
  link-prediction protocol; no ablation isolates propagation depth; interactions are uniformly
  weighted, static, not explainable.
- **Takeaway (slide 39):** all historical interactions influence the graph implicitly & uniformly.
  Motivating questions: Which interactions actually drive a recommendation? Can their influence be
  adjusted during inference? → motivates Shapley-based Contribution II.

---

## 5. Contribution II — Adaptive Shapley (ASV) (slides 40–52)
> Based on: *Dynamic Recommender Systems with Real-time Shapley Value-based Contribution Adjustment*
> (IJIES 18, 241–257, 2025; DOI 10.22266/ijies2025.1031.16). This is the paper the user's plan already cites.

### Research gap
Most recommenders assume (a) preferences are stable and (b) all historical interactions are
comparably relevant — both false. Adaptive methods use heuristics without explaining importance;
post-hoc explanations describe without influencing. Shapley is normally used post-hoc. **Gap:** a
unified, model-agnostic mechanism that quantifies interaction importance, uses it to adapt, **and**
exposes it as an explanation.

### Research questions → objectives (slide 42)
- RQ2.1 Can Shapley quantify each interaction's contribution? → Model interactions as cooperative-game players, recommendation score as value function.
- RQ2.2 Does Shapley-based reweighting improve top-10 across models/datasets? → UBCF/IBCF/MF/NCF on ML-1M & Amazon.
- RQ2.3 Can contribution scores both adjust and explain? → Reweight + identify influential interactions.
- RQ2.4 Do gains justify cost? → Runtime, memory, cost–benefit.
- RQ2.5 Does it demonstrate long-term adaptation? → Distinguish offline reweighting from streaming; limit claim.

### Methodology (slides 43–44)
- Each historical interaction = a **player** in a cooperative game; recommendation score = **value function**.
- Shapley value = expected marginal contribution over all coalitions; computed via **Monte Carlo** sampling.
- Shapley scores become **adaptive interaction weights** applied directly inside the scoring rule
  (e.g., inside user-based CF). Same score doubles as an **explanation**.

### Evaluation protocol (slide 45)
MovieLens-1M & Amazon; sampled-candidate top-10 (held-out positives + 99 sampled unobserved per user);
Precision@10, Recall@10, F1@10. Evidence limitation noted: point estimates only, no full multi-seed variance.

### Results — MovieLens-1M (slide 46)
| Model | P@10 | R@10 | F1@10 |
|---|---|---|---|
| UBCF | 0.750 | 0.650 | 0.696 |
| **ASV-UBCF** | 0.820 | 0.709 | 0.760 |
| IBCF | 0.780 | 0.700 | 0.738 |
| **ASV-IBCF** | 0.851 | 0.763 | 0.805 |
| MF | 0.810 | 0.730 | 0.768 |
| **ASV-MF** | 0.886 | 0.798 | **0.840** (best, +9.4%) |
| NCF | 0.850 | 0.780 | 0.813 |
| **ASV-NCF** | 0.873 | 0.796 | 0.832 (smallest gain) |

### Results — Amazon (slide 47)
| Model | P@10 | R@10 | F1@10 |
|---|---|---|---|
| UBCF | 0.698 | 0.673 | 0.685 |
| **ASV-UBCF** | 0.768 | 0.740 | 0.753 |
| IBCF | 0.705 | 0.696 | 0.700 |
| **ASV-IBCF** | 0.790 | 0.779 | 0.784 (largest F1 gain +12.0%) |
| MF | 0.886 | 0.800 | 0.841 |
| **ASV-MF** | 0.898 | 0.808 | 0.849 (highest F1, only +0.95%) |
| NCF | 0.742 | 0.715 | 0.728 |
| **ASV-NCF** | 0.841 | 0.776 | 0.807 (+10.9%) |

**Insight:** gains depend on the headroom of the baseline and are dataset-dependent
(ASV-MF best on MovieLens but weak on Amazon; ASV-IBCF/ASV-NCF strongest gains on Amazon).

### Computational overhead (slide 48)
| Method | Training overhead | Prediction change | Memory change |
|---|---|---|---|
| ASV-UBCF | +60% | 8.7 → 14.2 ms | 145 → 189 MB |
| ASV-IBCF | **+83%** | 7.4 → 13.8 ms | 138 → 185 MB |
| ASV-MF | +39% | 12.1 → 18.9 ms | 267 → 341 MB |
| ASV-NCF | +30% | 15.4 → 24.7 ms | 412 → 523 MB |

### Findings / limitations (slides 50–52)
- Broadly reusable (neighborhood, latent-factor, neural); dual-purpose (weighting + explanation);
  uneven gains; real efficiency cost; limited adaptivity (inference-time/precomputed, not continuous learning).
- **Limitations (slide 51):** high computation for long histories; clean implicit-positive bias;
  no drift testing; no live validation (no A/B, no user study); missing multi-seed variance/significance;
  deep graph recommenders not tested; sampled ranking may overstate full-catalog performance.
- **Takeaway (slide 52):** still models **flat** user–item structures in **Euclidean** space. Movies
  → genres, products → nested categories: hierarchical domains, preferences propagate across levels.
  ⟶ motives Contribution III (non-Euclidean + multi-level Shapley).

---

## 6. Contribution III — Hyperbolic GNN + Shapley (HGNN-SV) (slides 53–68)
> Based on: *Graph Neural Networks with Shapley-Value Explanations for Hierarchical Recommendation Systems*
> (IJACSA 16, 806–817, 2025; DOI 10.14569/IJACSA.2025.0160977).

### Research gap (slide 54)
Products → categories/subcategories; movies → genres; preferences exist at item/category/higher
abstraction levels; parent–child relations create long-range dependencies. Hyperbolic models are
more expressive for hierarchies but harder to interpret; existing Shapley explainers are built
around Euclidean scoring and don't stay consistent with hyperbolic distance.

### Research questions → objectives (slide 55)
- RQ3.1 Does hyperbolic learning improve accuracy for hierarchical relations? → Compare full model vs Euclidean, flattened, LightGCN, Hyperbolic GCN.
- RQ3.2 Can Shapley be added without reducing performance? → Hyperbolic Shapley vs non-Shapley variant.
- RQ3.3 Do explanations reflect hierarchy & preferences? → Hierarchical relevance, faithfulness, user judgments, preference alignment.

### Hyperbolic geometry (slides 56–58)
- **Hyperbolic space:** negatively curved; distances grow exponentially outward, matching tree/hierarchy growth.
- **Poincaré model:** points inside a ball, edge = infinity; compatible with gradient training;
  used for WordNet hierarchies, hyperbolic GNNs, and 2024–25 hierarchical recommendation.

### Methodology (slide 59)
Embed users & items in hyperbolic space (naturally captures hierarchy); compute Shapley contributions
adapted to hyperbolic distance (not Euclidean scoring); produce both a ranking and a multi-level,
hierarchy-aware explanation.

### Evaluation protocol (slide 60)
Same sampled-candidate top-K as before (ML-1M & Amazon); P@10/R@10/F1@10; plus **ablation,
runtime, perturbation faithfulness, and a user study** (more complete evidence than Contribution II).

### Results — MovieLens-1M (slide 61)
| Method | P@10 | R@10 | F1@10 |
|---|---|---|---|
| LightGCN | 0.763 | 0.703 | 0.732 |
| Hyperbolic GCN | 0.795 | 0.742 | 0.768 |
| LightGCN + GNNShap | 0.774 | 0.715 | 0.743 |
| LightGCN + MAGE | 0.783 | 0.731 | 0.756 |
| **HGNN-SV (full)** | **0.822** | **0.785** | **0.803** |

Hyperbolic GCN alone beats LightGCN (geometry matters); adding Shapley gives a further boost;
largest gains in Recall@10.

### Ablation — MovieLens-1M (slide 62)
| Variant | F1@10 | F1 drop |
|---|---|---|
| Full | 0.803 | — |
| Without Shapley | 0.794 | -0.009 |
| Without hyperbolic geometry | 0.770 | -0.033 |
| **Without hierarchy** | 0.740 | **-0.063** |

### Ablation — Amazon (slide 63)
| Variant | F1@10 | F1 drop |
|---|---|---|
| Full | 0.756 | — |
| Without Shapley | 0.745 | -0.011 |
| Without hyperbolic geometry | 0.721 | -0.035 |
| **Without hierarchy** | 0.690 | **-0.066** |

**Key insight (both datasets): removing hierarchy hurts most, then geometry, then Shapley —
hierarchical modeling is the main driver; geometry & explainability add incrementally.**

### Computational overhead (slide 64) — train / infer (s)
| Method | MovieLens train/infer | Amazon train/infer |
|---|---|---|
| LightGCN | 8.5 / 1.2 | 22.3 / 3.1 |
| Hyperbolic GCN | 11.7 / 1.6 | 27.9 / 4.4 |
| LightGCN + GNNShap | 14.2 / 2.3 | 35.1 / 5.8 |
| **Full (HGNN-SV)** | 15.6 / 2.4 | 38.5 / 6.2 |

Training 33–38% slower than Hyperbolic GCN; inference 41–50% slower. Manageable experimentally
but production readiness not yet established.

### Findings / limitations (slides 65–68)
- Graph structure improves edge prediction beyond matrix methods; higher-order neighborhoods mainly help recall;
  simple LightGCN-style architecture is sufficient; predictive accuracy doesn't address static weighting or explainability.
- **Limitations (slide 67):** resembles existing architectures; ML-1M + link prediction; no ablation
  on propagation depth; uniform edge weights; no local explanations; preference adaptation not validated;
  claims follow link-prediction framing, not top-N.
- **Takeaway (slide 68):** moves beyond static graph propagation by measuring interaction importance,
  using it both to improve recommendation generation and to explain the result.

---

## 7. Conclusion & perspectives (slides 69–76)

### Synthesis (slide 70)
| C | Main idea | Main achievement | Key finding |
|---|---|---|---|
| C1 | Explainable graph-based RS using Shapley | Faithful explanations for GNN recommenders by quantifying interaction contribution | Explainability improves transparency while preserving performance |
| C2 | Adaptive recommendation via contribution-aware inference | Dynamically reweight historical interactions at inference | Adaptive weighting improves robustness & personalization |
| C3 | Hyperbolic GNNs for recommendation | Model hierarchical relations in hyperbolic space | Hyperbolic representations outperform Euclidean for hierarchical recommendation |

**Thesis statement (slide 75):** explainability is not only a post-hoc interpretation tool but a
**fundamental component** for building accurate, adaptive, and trustworthy graph-based recommender systems.

### Publications (slides 71–72)
| No. | Title | Venue | Status |
|---|---|---|---|
| I | Dynamic Recommender Systems with Real-time Shapley Value-based Contribution Adjustment | IJIES 18 (2025) | Published |
| II | Graph Neural Networks with Shapley-Value Explanations for Hierarchical Recommendation Systems | IJACSA 16 (2025) | Published |
| III | Shapley Values for Explaining Adaptive Recommendations in Temporal Hyperbolic Graph Neural Networks | Discover Artificial Intelligence | Under review |
| IV | Toward Temporal Stability in Explainable AI: A Framework for Measuring Explanation Drift | Results in Engineering | Under review |
| V | A Collaborative Filtering Movies Recommendation System based on Graph Neural Network | ANT/EDI40 (2023) | Published |
| VI | A Hybrid Machine Learning Method for Movies Recommendation | BDIoT (2022) | Published |

(Note: the résumé lists I & II (and V & VI) with DOIs; slides list all six. The résumé's DOI for
paper II is 10.14569/IJACSA.2025.0160977 vol 16 pp 806–817.)

### Limitations (slide 73)
- Limited domain evaluation (MovieLens & Amazon only); scalability of Shapley explanations (expensive at scale);
  **static graph assumption** (no continuously evolving relations); limited multimodal information
  (no text/visual/KG); hyperbolic architecture scope (single HGNN design); **offline evaluation** (no A/B testing).

### Perspectives / future work (slide 74)
1. **Dynamic graph recommender systems** — temporal & continuously evolving user–item graphs.
2. **Scalable explainable recommendation** — efficient Shapley approximations for real-time use.
3. **Multimodal recommendation** — text/visual/knowledge-graph information.
4. **Advanced hyperbolic graph learning** — Hyperbolic Graph Transformers, mixed-curvature embeddings.
5. **Online & real-world deployment** — A/B testing and industrial deployment for long-term trust/satisfaction.

---

## 8. How this relates to the user's (Mouad's) thesis

**Shared lineage:** same supervisor (Lazaar), same lab (ENSIAS/UM5), same overarching theme
(XAI via cooperative-game Shapley values for recommender systems), and Redwane is a co-author
on Mouad's papers I & II. Both use **Shapley values as the common lens** and both argue
explainability should be more than post-hoc.

**Divergence / complementarity:**

| Dimension | Mouad (user) | Redwane (colleague) |
|---|---|---|
| Core object | Clustering (wine, Beijing air quality) + **hypergraph** recommender (DyHuCoG) | **Graph** CF + adaptive Shapley + **hyperbolic** GNN |
| Shapley role | Post-hoc cluster explanation + in-training signal in DyHuCoG | Interaction-level attribution → adaptive reweighting + explanation |
| Utility/objective | Multi-objective (NDCG + diversity + context) | Ranking + adaptive fairness/reweighting |
| Geometry | Euclidean (hypergraph incidence) | **Hyperbolic (Poincaré)** for hierarchy |
| Key metric emphasis | NDCG@20, Recall@20, coverage, ILD | Precision@10, Recall@10, F1@10 |
| Datasets | Wine, Beijing, MovieLens-1M, Amazon-Book | MovieLens-100K/1M, Amazon Products |
| Papers counted | 3 | 6 (2 published journal + 2 under review + 2 older conference) |

**Useful reference value for the user's own defense:**
- The colleague's viva is a **template for the user's own viva structure** (intro → problematic →
  protocols → 3 contributions each with objectives/methodology/results/findings → synthesis →
  limitations → perspectives → Q&A).
- The speaker notes are a strong model for **how to narrate** each slide (what to emphasize, what
  to scope down, self-aware limitations).
- The colleague **explicitly limits claims** ("link prediction, not top-N"; "offline reweighting,
  not streaming adaptation"; "point estimates, no multi-seed variance") — a strong exam-integrity
  practice worth mirroring (the user's thesis already does this too, e.g. scoping Amazon-Book
  results as descriptive).

---

## 9. Noted discrepancies / caveats (for cross-checking)

1. **Amazon item count inconsistency:** presentation slide 20 says MovieLens-1M has "3,952 movie"
   items; slide 79 says "3,952" but the user thesis / DyHuCoG list 3,706. Cross-check against the
   official MovieLens-1M figure (3,952 movies is standard; 3,706 may be a filtered subset).
2. **Paper II reference formatting:** the résumé gives DOI 10.14569/IJACSA.2025.0160977 (vol 16,
   pp. 806–817); the presentation doesn't give a DOI. Verify against the published record.
3. **Slide 71 notes contradiction:** narrator says "two published in 2025, one accepted in 2026,
   one under review", but the table shows two *journal-track published (2025)*, two *under review*
   — the "accepted in 2026" count isn't fully reflected. Minor narration/table mismatch.
4. **Speaker-note cut/paste:** Several slides (6, 7, 32, 56, 57, 58) reuse the same notes ("Experiments
   ran on a ThinkPad..." / "Netflix... billion dollars") — these are template re-use, not errors.
5. **"Explainable AI (XAI) for Decision-Making"** uses "(XAI)" though title slide also shows
   "Explainable Artificial Intelligence" inconsistently across slides — cosmetic only.

---

## 10. Keywords
Explainable AI (XAI), Recommender Systems, Graph Neural Networks (GNN), Cooperative Game Theory,
Shapley Values, Adaptive Recommendation, Contribution-aware Inference, Hyperbolic Geometry,
Poincaré Embeddings, Hierarchical Recommendation, Algorithmic Transparency/Fairness,
Trustworthy AI, MovieLens, Amazon Reviews.
