# Question & Answer Bank — Defense Preparation

> A curated bank of the questions a jury is most likely to ask, organised by theme, with
> **suggested answers** you can adapt to your own voice. It also flags the questions designed to
> probe your honest boundaries and the points you should anticipate. Each answer is written as a
> **delivery-ready** paragraph, not a bullet list.

---

## Theme 1 — The big picture

### Q1. What is your thesis in one sentence?
Shapley-value attribution — because it satisfies efficiency, symmetry, null-player and
additivity — is used not only as a post-hoc explanation but as a **single, shared, formally
grounded mechanism** that explains black-box clustering, stays coherent under hierarchical
scale, and becomes an in-training optimisation signal inside a dynamic hypergraph recommender.

### Q2. What is the central claim?
Explanation should be **part of the modelling logic itself**, not a by-product attached after
prediction. Cooperative game theory provides a common formal language for allocating explanatory
responsibility across features, interactions and contexts.

### Q3. Why cooperative game theory, and not something else?
Because the Shapley value is the **unique** allocation satisfying four axioms — efficiency,
symmetry, null-player and additivity. That gives it a **normative** basis. Alternatives such as
LIME or attention weights are heuristic: LIME fits a local surrogate with no equivalent
guarantee and is sensitive to perturbation design; attention weights alone do not guarantee
fairness, completeness or symmetry.

### Q4. What is the difference between this thesis and a survey?
This is not a survey. It makes three concrete, reproducible methodological contributions — a
surrogate pipeline for explainable clustering, a formal multi-level consistency property, and a
fully-integrated hypergraph recommender where attribution is a training signal — and it argues
they should be read as one cumulative framework.

### Q5. Is this "one unified framework" or three separate papers?
I want to be precise. It is **not** one fully unified framework that eliminates all tension
between accuracy and interpretability. It is a **shared perspective** — a common attribution
language that is coherent and productive across the three tasks. It is a cumulative argument,
not a bound collection.

---

## Theme 2 — The mathematics

### Q6. State the Shapley value and its axioms.
The Shapley value of player `i` is the expected marginal contribution over all orderings:
`φ_i = Σ_{S⊆N\{i}} [|S|!(|N|-|S|-1)!/|N|!]·[v(S∪{i}) − v(S)]`. The four axioms are efficiency
(all explanatory mass is allocated), symmetry (equal marginal contributors get equal credit),
null-player (zero marginal contributors get zero), and additivity (explanations compose).

### Q7. Why is exact Shapley intractable, and how do you approximate it?
Exact computation sums over all `2^|N|` coalitions, which is exponential. I use two
approximations: **TreeSHAP** (exact and fast for tree ensembles, used because the surrogate is a
LightGBM tree) and a **Monte Carlo estimator** (DyHuCoG) that samples `M` coalitions. The MC
estimator is unbiased with variance `σ²/M`, so MSE decays `O(1/M)` and absolute error `O(1/√M)`.

### Q8. Why a surrogate for clustering? Why not explain K-Means directly?
TreeSHAP explains tree models; it cannot explain K-Means centroids. And explaining the PCA
representation would move attribution away from the interpretable variables we care about. So I
convert an unsupervised partition into a supervised task — train a LightGBM surrogate to predict
the induced cluster labels from the original features — then apply TreeSHAP to the surrogate.
This keeps attribution in the **semantic** feature space, which is what makes it actionable.

### Q9. What is the validity condition of the surrogate approach?
**Surrogate fidelity.** If the surrogate does not reproduce the partition well, the attribution
is not faithful. I treat a macro-F1 of about 0.82 as the practical floor.

### Q10. Where does efficiency hold in your surrogate pipeline?
Efficiency holds with respect to the **LightGBM surrogate output**, not directly to the
Silhouette-based game. That is exactly why surrogate fidelity is the critical validity condition.

### Q11. State Proposition 6.1 and its derivation.
Let `Φ^(ℓ,c)_j` be the expected absolute SHAP importance of feature `j` at level `ℓ` in cluster
`c`, and `w_{c'}=|c'|/|c|` the relative child size. For a strict nested hierarchy on a consistent
feature space, `Φ^(ℓ,c)_j = Σ_{c'∈child(c)} w_{c'}·Φ^(ℓ+1,c')_j + ε_j`, where `ε_j` is a residual
from surrogate mismatch that vanishes under perfect fidelity. It is derived via the law of total
expectation, since children partition the parent.

### Q12. Does Prop. 6.1 claim explanations are identical across levels?
No. It implies the differences across levels can be **interpreted rather than dismissed as
inconsistency**. That makes a hierarchical explanation self-consistent and auditable.

---

## Theme 3 — The contributions

### Q13. What is the contribution of C1 over the state of the art?
C1 provides a principled, partially model-agnostic pipeline that yields **both** instance- and
cluster-level explanation in the **original** semantic feature space, and it gives a
theoretically grounded argument for Shapley over LIME. Existing clustering-interpretability
methods typically privilege local OR global, rarely both, and often fail to scale or preserve
coherence across clusters.

### Q14. Why did you choose k=3 for wine when k=2 is geometrically better?
This is a deliberate, defensible choice. On raw geometry, k=2 has a better Silhouette (0.214)
and Davies-Bouldin (1.775) than k=3 (0.144 / 2.097). But k=3 supports three distinct,
chemically meaningful oenological narratives — far more actionable than a dichotomous split. I
select the partition a domain expert would find useful, not the one that maximises a separation
index. The interpretability criterion guides model selection.

### Q15. What is the important thing about the wine global importance ranking?
Density, pH, fixed acidity, sulfur-dioxide and alcohol dominate — precisely the variables an
oenologist points to as governing structure, preservation and sensory balance. Because the
surrogate was trained to reproduce the partition from the original variables, and because
TreeSHAP attributes in that original space, the recovered hierarchy is **chemically
interpretable and faithful** — it recovers domain knowledge without being told to.

### Q16. What does C2 add beyond scale?
The real issue is **multi-granularity**, not just scale. A variable can be globally important
yet locally uninformative. C2 provides a genuine multi-level workflow, a formal cross-level
consistency argument (Prop. 6.1), and validation on a structurally different large-scale
dataset. The Beijing results show that at the coarse level meteorology dominates (regime
selection), while within clusters pollutants become discriminative — and Prop. 6.1 lets us
interpret this shift as structure, not noise.

### Q17. What is the key Beijing finding?
Temperature, dew point and pressure are the dominant features, not simply pollutant
concentrations. Meteorological variables condition dispersion, trapping and photochemistry, so
they structurally define pollution regimes. A naive ranking of pollutant concentrations would
overlook that the weather is what sets the regime.

### Q18. What is the strongest claim of C3?
**Attribution becomes an in-training signal.** In DyHuCoG, Shapley estimates are used as dynamic
hyperedge weights in message passing, so attribution directly shapes how information flows. The
model is told not only who is connected to whom, but **how much each coalition is worth**.

### Q19. How does DyHuCoG improve both accuracy AND diversity?
Ranking, coverage and intra-list diversity are all part of the coalition utility and the
training loss, so they are optimised together rather than traded off. Empirically, NDCG, recall,
coverage and ILD all improve on both datasets — the largest gains on the sparsest data.

### Q20. What is the "accuracy–diversity trade-off not structurally fixed" claim?
The literature often treats the accuracy–diversity trade-off as a fixed structural constraint. We
show it is **negotiable**: if attribution is handled as a first-class part of the learning
objective, both can improve together.

### Q21. Why is the gain largest on the sparsest dataset (Amazon-Book)?
Shapley-driven weighting is most valuable precisely when interaction data are weak. When signal
is sparse, a principled marginal-contribution weighting recovers more useful signal than uniform
or attention weighting, so the relative gain is largest.

---

## Theme 4 — Experimental design & rigor

### Q22. How do you prevent leakage in the recommendation split?
I use a **user-level, temporal holdout**: sort interactions by time per user, split 70/10/20, and
evaluate with leave-one-out, where the latest test positive per user is the target, ranked
against sampled negatives. This prevents using future interactions to predict the past.

### Q23. Why popularity-aware negative sampling?
Uniform negatives are too easy and underestimate the difficulty of the task. By drawing negatives
with probability proportional to item popularity, `q(i) ∝ f_i^η`, I produce **harder contrasts**
that better reflect real recommendation difficulty.

### Q24. How do you validate statistical significance?
Paired t-tests on per-user NDCG@20 (n=6,040), with Holm–Bonferroni correction for multiple
comparisons, the Wilcoxon signed-rank test as a non-parametric check, and Cohen's d as an effect
size. Against HPCF, t=46.38, Cohen's d=1.33, p≈1.81×10⁻²⁷⁰.

### Q25. What is the scope of your statistical claims?
Full tabulated paired tests apply **only to MovieLens-1M** per-user NDCG@20. The Amazon-Book
results and auxiliary metrics remain **descriptive**. I would rather make a bounded claim
rigorously than over-claim.

### Q26. What baselines do you compare against, and why HPCF?
MF, NCF, LightGCN, RecDCL, HCCF and HPCF. HPCF is the strongest reference — the most recent
hypergraph method and the best-performing baseline — so I isolate the contribution of cooperative
attribution rather than a favourable model choice.

---

## Theme 5 — Honest limitations

### Q27. What are the main limitations?
Computationally, exact Shapley is intractable and every contribution relies on approximation or
surrogates. Methodologically, clustering depends on surrogate fidelity and recommendation
depends on stable approximate contributions and adequate context. Empirically, the work is
tabular clustering and offline recommendation — no multimodal, sequential or online deployment,
and no dedicated human-subject actionability study. And on the claim scope, it is a coherent
perspective, not one fully unified framework.

### Q28. Is the computational overhead acceptable?
DyHuCoG trains in about 1.78× the time of HPCF (~2000s vs ~1125s on MovieLens-1M), but inference
is 1.84 ms/query — comfortably within real-time requirements. The per-epoch cost grows with
layers, embedding dimension and the Monte Carlo budget, and M=50 is a deliberate accuracy/cost
operating point.

### Q29. Why did you not do a user study of actionability?
That is a genuine limitation and a clear future direction. The explanations are validated for
structural faithfulness and utility decomposition, not through a large-scale human study. A
human-centred evaluation of whether explanations measurably improve analyst judgement or user
trust is exactly the next step I propose.

### Q30. Are your baselines up to date?
The baselines were finalised in early 2026, so I claim superiority only against the tested set
(MF, NCF, LightGCN, RecDCL, HCCF, HPCF). Later models, including post-2024 LLM-augmented
recommenders, were not audited. That is an honest boundary.

### Q31. Does the DyHuCoG Shapley use the full catalogue?
No. Coalition evaluation is scoped to the interaction **episode** — one focal user plus a small
candidate item set plus context nodes — so the player set is a few dozen, not the full catalogue.
It is an approximate in-training valuation aligned with the local recommendation context, and I
state this frankly.

### Q32. Is the hierarchy in C2 a claim about reality?
No. The hierarchy is a **pragmatic analytical device**, not a claim that the data have a true
ontological hierarchy of levels. The nested structure is a computational and interpretive tool,
and Proposition 6.1 is stated with that in mind.

---

## Theme 6 — Trustworthy AI & broader impact

### Q33. How does this connect to the EU AI Act?
The EU AI Act (Reg. 2024/1689), the OECD AI principles and the GDPR all put a premium on
meaningful explanation. Because Shapley values rest on an axiomatic, normative basis, this
perspective is well aligned with the transparency and accountability requirements of emerging AI
regulation.

### Q34. Does Shapley address fairness?
Shapley measures **marginal utility**, not raw frequency, so weak but informative interactions
retain influence — which mitigates popularity bias. It is a step toward fairer attribution, but I
would not claim it solves exposure fairness or other fairness notions; those are explicitly
future work.

### Q35. Is your explanation "actionable" per your own definition?
I test structural faithfulness and utility decomposition. The modifiable-factor and
domain-vocabulary criteria are met by keeping attribution in the original semantic space. Whether
they measurably change analyst or user behaviour is the open human-centred question.

---

## Theme 7 — Questions designed to catch you out

### Q36. "Is this just three papers stapled together?"
No — deliberately not. The thesis adds the multi-level formalisation, the cross-chapter
comparisons, and the explicit mapping to the five research questions. It is a cumulative
argument: the same cooperative-attribution logic is used for explanation, for interpretation and
for optimisation.

### Q37. "Your C1 surrogate can't explain the actual K-Means geometry, so your explanation is of the surrogate, not the clustering."
Correct, and I state that honestly. The explanation is of the **faithful surrogate reconstruction**
of the partition, not a mechanistic explanation of the centroids. That is why surrogate fidelity
is the critical validity condition, and why I frame the approach as partially model-agnostic.

### Q38. "Your LIME comparison isn't a full empirical bake-off."
Correct. The SHAP-vs-LIME comparison is presented as theoretical and literature-backed, not a
comprehensive empirical bake-off on wine. I bound the scope of that claim on the slide.

### Q39. "How do you know the improvement isn't just from the extra model complexity?"
The ablation isolates this. Removing the Shapley value (while keeping the hypergraph model) costs
−4.6%/−6.1% NDCG, and removing the hypergraph structure costs −6.8%/−8.9%. So the gains are
attributable to the Shapley weighting and the hypergraph structure, not to a blanket increase in
capacity.

### Q40. "Can you prove Monte Carlo convergence in downstream NDCG, not just MSE?"
The MC convergence is reported via MSE and runtime, not a separate metric-sensitivity table. That
is a stated boundary. I could extend it to a downstream metric-vs-M sensitivity study as future
work.

### Q41. "Why not compare against LLM-augmented recommenders?"
The baselines were finalised in early 2026, and later models were not audited. I claim superiority
only against the tested set. Auditing post-2024 LLM-augmented recommenders is a legitimate and
valuable extension.

---

## Theme 8 — Future work

### Q42. What is the single most important next step?
The most impactful is **closing the computational gap** — lower-variance Shapley estimators,
learned proposal distributions, and adaptive refresh policies — because that would make the
in-training attribution approach affordable at industrial scale.

### Q43. Would you extend to online/streaming?
Yes. The static-clustering and static-graph limitations naturally motivate online, incremental
settings with evolving graphs and delayed feedback. This is a clear, concrete extension.

### Q44. How would you make the explanations truly actionable?
By running a proper **human-centred evaluation** — testing whether the explanations measurably
improve analyst judgement, user trust, intervention quality or perceived fairness. That is the
natural test of the "actionable" part of my definition.

---

## Cheat sheet — the four points to always land

1. **The claim:** explanation should be part of the modelling logic, not bolted on.
2. **The mechanism:** Shapley attribution, uniquely grounded by the four axioms, is the common
   formal language.
3. **The arc:** explain (C1) → scale (C2) → integrate (C3), read as one cumulative argument.
4. **The honesty:** state the bounds (surrogate fidelity, offline/tabular, early-2026 baselines,
   per-episode valuation) before a jury probes them.

## If you are stuck, return to this

> "Cooperative attribution is not three unrelated tools; it is a single mechanism for
> explanation, for interpretation, and for optimisation."
