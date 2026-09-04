# 40-Minute Defense Speech — Mouad Louhichi

> **How to use this script.** Each block is the spoken text for a slide (or a group of
> slides), with the target slide number and a running time. The whole script is timed to land
> **in or around 38–40 minutes**, leaving a margin for the jury's interruptions and the Q&A.
> Words in **[brackets]** are stage directions or emphasis cues — do not read them aloud.
> Pauses are marked as *(pause)*.

**Total: ~5,800 words ≈ 38 min at a measured ~150 words/min.** If you run long, the two
marked "**CUT IF TIGHT**" segments are the safest places to drop.

---

## Introduction (Slides 3–6) — ~4 min

### Slide 3 — Title & hello *(0:00–0:30)*
Good morning. Thank you, President and Professors, for the time you are giving me to present
and discuss my thesis. My name is **Mouad Louhichi**. My thesis is titled *Cooperative Game
Theory for Explainable Artificial Intelligence in Recommendation Systems: A Shapley Framework
for Actionable Insight*, supervised by Professor **Mohamed Lazaar**. *(pause)* In one sentence,
it advances this idea: Shapley-value attribution is not just a post-hoc explanation — it is a
single formal mechanism that can explain black-box clustering, stay coherent under
hierarchical scale, and finally operate as an **in-training signal** inside a recommender.

### Slide 4 — Motivation: three questions *(0:30–1:30)*
Three questions frame the whole work. **First, ubiquity.** Opaque systems mediate what
billions of people see, buy and watch every day — not only on streaming platforms, but in
e-commerce, news feeds and search. **Second, the black box.** Even strong recommenders and
clustering pipelines are hard to interrogate. We observe their outputs without understanding
why a particular item was chosen. **Third, trust.** Transparency should be built into the
modelling logic, not bolted on afterwards. *(pause)* The core tension of the thesis is that as
models gain expressive power, they lose the transparency needed for trustworthy deployment.
Throughout this work I hold accuracy and interpretability as objectives to be **reconciled**,
not traded against one another.

### Slide 5 — Actionable insight *(1:30–2:30)*
Let me define the frame. I call an explanation **actionable** when it identifies at least one
**modifiable factor** whose change is associated with a specifiable change in model output —
and when that factor is expressible in the **semantic vocabulary of the task domain**: a
physicochemical variable for wine, a pollution indicator for air quality, a preference signal
for recommendation. The crucial constraint is that it must **not** be an opaque latent code.
This distinction separates explanations that let a designer **intervene and act** from those
that merely describe what happened. By this definition, a credible explanation is judged by
whether it supports a **downstream decision**, not by whether it looks plausible.

### Slide 6 — Research context *(2:30–3:30)*
The context is a progression from simple to hypergraph recommenders. Matrix factorisation
showed that latent factors could capture preferences — but those factors were immediately
uninterpretable. Graph and graph-neural-network models improved ranking by exploiting
connectivity, yet replaced an opaque latent code with an opaque message-passing mechanism.
Finally, hypergraph models added higher-order user–item–context relations, but typically assume
that every message contributes uniformly. *(pause)* Each step raised expressiveness while
lowering transparency. The deficit matters for **trust, debugging and regulation** — the EU AI
Act, the OECD principles and the GDPR all put a premium on meaningful explanation. That is why
a principled attribution mechanism is needed, and why I will argue it should be part of the
modelling logic rather than an afterthought.

---

## Context & Problematic (Slides 7–12) — ~5 min

### Slide 7 (section) + Slide 8 — Paradigms *(3:30–4:30)*
Quick orientation across the paradigms we build on. Collaborative filtering recommends on the
principle that similar users will value similar items. Content-based filtering recommends items
sharing attributes with a profile, while hybrid methods combine both. Matrix factorisation
factorises the interaction matrix into latent factors — compact and effective, but immediately
opaque. Graph-based methods, including LightGCN and hypergraph extensions, propagate
information over an interaction structure and capture multi-hop or higher-order relations. Each
strengthens the modelling, but each complicates interpretation in a specific way: matrix
factorisation made latent dimensions opaque; graph models kept importance implicit; hypergraph
models added higher-order relations but **assumed uniform message importance**. That uniformity
assumption is one of the things I challenge.

### Slide 9 — Limitations of classical models *(4:30–5:15)*
Four classical limitations. **Data sparsity and scalability** are the most cited: the user–item
matrix is overwhelmingly empty. **Cold-start** is the structural consequence — a new user or
item has no history to learn from. **Popularity bias and the lack of diversity** create a
filter-bubble loop. And the most fundamental limitation, and the one this thesis targets, is
the **absence of interpretability**. For clustering specifically it is even harder: methods
privilege a *local* explanation or a *global* one but not both; they struggle to scale; and
their explanations rarely remain coherent across resolutions.

### Slide 10 — Problem statement *(5:15–6:00)*
Three structuring problems. **First, lack of explainability.** **Second, difficulty of
scaling** — local explanations do not transfer naturally to hierarchical structures or large
datasets. **Third, weak integration into learning** — most explanations are post-hoc and do not
shape model dynamics, nor the accuracy–diversity–context trade-off. The thesis gap follows
directly: the literature still lacks a single cooperative-attribution framework that explains
clustering faithfully, stays coherent under hierarchy, and then operates as an in-training
signal in recommendation. My claim is that Shapley-value attribution can be that framework.

### Slide 11 — Research questions *(6:00–6:45)*
Five questions form the spine. **RQ1:** how can Shapley values explain black-box clustering
faithfully at instance and cluster level? **RQ2:** how can that extend to large-scale,
hierarchical clustering without losing tractability or consistency? **RQ3:** can cooperative
attribution move beyond post-hoc analysis into the learning dynamics of graph recommenders?
**RQ4:** can a recommender jointly optimise ranking, context and diversity when importance is
estimated by a cooperative-game utility? And **RQ5**, the thesis-level question: what emerges
when clustering explanation and recommendation learning are read as two stages of one shared
perspective?

### Slide 12 — Three contributions *(6:45–7:30)*
Three contributions, one thread. **C1** establishes Shapley-based explanation for black-box
clustering through a PCA–K-Means–LightGBM–TreeSHAP pipeline, validated on wine. **C2** scales
it to hierarchy and large data via multi-level clustering with cross-level SHAP aggregation,
validated on Beijing air quality. **C3** is the strongest claim: **DyHuCoG** replaces post-hoc
attribution with an in-training signal inside a hypergraph recommender, validated on
MovieLens-1M and Amazon-Book. Each answers a distinct research question, but they are designed
to be read together as a **cumulative** argument — cooperative game theory as a shared
attribution perspective for explanation, optimisation and intervention.

---

## Experimental Protocol (Slides 13–17) — ~2.5 min

### Slide 14 — Datasets *(7:30–8:20)*
Two clustering datasets and two recommendation datasets. For clustering I deliberately picked
datasets with **semantically interpretable features**, because the whole point of the method is
to return attribution to the original variables. Wine Quality is a small, dense, chemically
correlated dataset of almost five thousand samples with eleven features. Beijing Multi-Site Air
Quality is a large, noisy, temporally and meteorologically variable dataset of over three
hundred and eighty thousand hourly records. For recommendation I used benchmark-standard
datasets with established baselines: MovieLens-1M, with roughly a million interactions and a
density of 0.0447, and Amazon-Book, which is far sparser at 0.0006. **The sparsity contrast is
deliberate** — it stress-tests whether a Shapley-guided model helps most precisely when
interaction data are weak.

### Slide 15 — Splitting *(8:20–8:50)*
Splitting is designed against leakage. For clustering I use five-fold cross-validation to test
the stability of the surrogate and the attribution. For recommendation I use a **user-level,
temporal holdout** — seventy percent train, ten percent validation, twenty percent test — with
**leave-one-out** evaluation, where the latest test positive per user is the target. Because
MovieLens contains explicit ratings, I convert ratings greater than three into positive
implicit feedback, and draw negatives from a **popularity-aware** distribution to produce
harder contrasts. Results are reported across five seeds, with early stopping on validation
NDCG.

### Slide 16 — Baselines & metrics *(8:50–9:30)*
Baselines span classical, neural, graph and hypergraph methods, so I isolate the contribution
of cooperative attribution rather than a favourable model choice. For recommendation I compare
against MF, NCF, LightGCN, RecDCL, HCCF and HPCF, treating HPCF as the strongest reference. For
clustering interpretability I compare against a LIME-based surrogate. Ranking is measured with
Precision, Recall and NDCG at twenty as the principal measure. On diversity I measure
**catalogue coverage** and **intra-list diversity**, defined as the average pairwise
dissimilarity inside a ranked list. I want to emphasise that ILD is **not decorative** — it is
deliberately built into the DyHuCoG coalition utility. Finally, every headline comparison is
backed by statistical validation.

### Slide 17 — Hardware *(9:30–9:55)*
The hardware matters mainly because it explains some runtime figures I will quote. All
clustering, preprocessing and data loading run on an Intel Core i9 with twenty-four cores.
DyHuCoG training and inference run on an NVIDIA RTX 4090 with twenty-four gigabytes, alongside
forty-eight gigabytes of RAM. The stack is Python 3.8, scikit-learn, LightGBM, SHAP and PyTorch
2.0.1. Everything stays within ordinary academic compute.

---

## Contribution I (Slides 18–31) — ~5 min

### Slide 19 (objectives) + 20 (RQ1→objectives) *(9:55–10:40)*
Why start with clustering? Here the model creates its own structure, so cluster meaning must be
inferred after the fact — which makes clustering the hardest and most natural test bed for
attribution. The gap is that explainable clustering is fragmented: methods favour a local or a
global explanation, rarely both; they often fail to scale; and they rarely preserve coherence
across clusters. Because Shapley explanation is well established in supervised problems, its
near absence from unsupervised clustering is striking. **RQ1** decomposes into three objectives:
O1, a pipeline yielding cluster-level explanation while preserving feature-level attribution;
O2, to preserve the semantics of the original feature space rather than a latent space; and O3,
to justify why Shapley is the right concept rather than an ad-hoc surrogate such as LIME.

### Slide 21 — Cooperative-game framing *(10:40–11:20)*
We frame clustering as a cooperative game where **features are the players**. The value function
measures how well the data cluster when we use only the features in a given coalition: the value
of coalition S is the Silhouette of K-Means run on the feature subset, with fixed k. I choose
Silhouette because it is bounded, normalised and semantically intuitive. A feature then receives
a high Shapley value when its presence consistently improves separation across all coalitions.
The problem is that evaluating Silhouette for every subset is **combinatorial and infeasible** —
which is exactly why we need a bridge between the unsupervised partition and a tractable
attribution method.

### Slide 22 — The surrogate bridge *(11:20–12:05)*
The bridge is the heart of the method. TreeSHAP explains tree models; it cannot explain K-Means
centroids. And explaining the PCA representation would move attribution away from the
interpretable variables we care about. So we convert an unsupervised partition into a supervised
task: once K-Means produces cluster labels, we train a **LightGBM multiclass surrogate** to
predict them from the original features, then apply TreeSHAP to that surrogate. This keeps
attribution in the original semantic feature space, which is what makes the explanation
actionable. The key validity condition is **surrogate fidelity** — we require a macro-F1 of
around 0.82 as the floor.

### Slide 23 — Pipeline *(12:05–12:40)*
The pipeline has five stages. Standardisation, then PCA as a computational and visual
diagnostic — deliberately **not** the explanatory space. Then K-Means-plus-plus with
multi-criteria k selection. Then the LightGBM surrogate. Then TreeSHAP attribution in the
original feature space, aggregated into global importance, cluster-specific profiles, and local
force plots. Complexity is dominated by PCA and repeated K-Means; TreeSHAP scales with tree
count and depth rather than exponentially in features — which is what makes the approach
tractable.

### Slide 24 — k selection *(12:40–13:20)*
This is an honest and important point. We evaluate k from two to ten, and deliberately select
**k equal to three even though it is not geometrically optimal**. With k equal to two we get a
stronger Silhouette of 0.214 and a Davies-Bouldin of 1.775; with k equal to three the Silhouette
drops to 0.144. On raw geometry, two is the better partition. We choose three nonetheless,
because three clusters support three distinct, chemically meaningful oenological narratives — far
more actionable than a dichotomous split. I select the partition a domain expert would find
useful, not the one that maximises a separation index. And to avoid a common confusion: the 0.63
Silhouette belongs to the Beijing dataset in Contribution II, not this one.

### Slide 25 — Global importance *(13:20–13:55)*
The global SHAP ranking is dominated by density, followed by pH, fixed acidity,
sulfur-dioxide-related variables and alcohol. These are precisely the variables an oenologist
would point to as governing structure, preservation and sensory balance. The important point is
that this is **not an arbitrary classifier artefact** — because the surrogate was trained to
reproduce the partition from the original variables, and because TreeSHAP attributes in that
original space, the recovered hierarchy corresponds to a chemically interpretable structure.
This is the strongest evidence that the pipeline is faithful: it recovers domain knowledge
without being told to.

### Slide 26 — Cluster profiles *(13:55–14:30)*
The cluster-specific profiles show the solution is not only globally interpretable but
internally differentiated. Cluster zero is driven by density and sulfur-dioxide variables;
cluster one by acidity and pH; cluster two by a different balance across acidity, alcohol and
related chemicals. Crucially, the same small set of variables recurs across all three clusters,
but with different relative weights within each. This is the actionable insight: a cluster is
not just a label, it is a distinct, domain-meaningful combination of drivers.

### Slide 27 (Answers) + 28 (Key findings) *(14:30–15:15)*
To answer **RQ1** directly: yes. Shapley values explain a black-box partition faithfully,
provided the surrogate is high-fidelity, and coherently at cluster level. Each objective is met.
O1 is met because the pipeline yields both a global and a per-cluster reading. O2 is met because
attribution is returned to the original chemical variables. O3 is met because Shapley satisfies
efficiency, symmetry, the null-player property and additivity, whereas LIME has no equivalent
guarantee. The honest caveat is that efficiency holds with respect to the surrogate output, not
directly to the Silhouette-based game.

### Slide 29 — Limitations *(15:15–15:40)*
Let me be clear about the scope. First, the explanation depends on the fidelity of the LightGBM
surrogate; it is not a direct mechanism of the K-Means geometry. Second, the approach is confined
to tabular data. Third, and most importantly for what follows, **it is single-level**: it cannot
yet address hierarchical coherence, meaning it cannot explain how feature importance
reconfigures between a partition and its sub-partitions. These limits define the point of
departure for Contribution II.

### Slide 30 — Takeaways *(15:40–16:00)*
The takeaway is that Shapley attribution works as a single, principled lens for explaining an
unsupervised partition, and that keeping attribution in the original feature space is what makes
it actionable. But real data are rarely single-level — broad regimes contain nested sub-groups.
That flat limitation directly motivates Contribution II: can the explanation logic be scaled to
multi-level, large-scale clustering without losing coherence?

---

## Contribution II (Slides 32–45) — ~5 min

### Slide 33 (obj) + 34 (RQ2) *(16:00–16:45)*
C2 asks whether the C1 logic survives scale and hierarchy. Large real-world data contain
structure at more than one granularity: broad regimes at the top, nested sub-groups within them.
A variable can be globally important yet locally uninformative, so a flat explanation is true but
incomplete. The chapter adds three things. First, a genuine multi-level workflow. Second, a
formal cross-level consistency argument, **Proposition 6.1**. Third, validation on a structurally
different large-scale dataset, Beijing air quality.

### Slide 35 — Multi-level architecture *(16:45–17:30)*
The architecture proceeds recursively: coarse clustering on the full dataset, then subdivide each
cluster where appropriate, producing a nested structure. For each level we train a level-specific
surrogate and compute SHAP in the same original feature space. The cross-level aggregation is
deliberately **not a naive average** — it respects cluster size and nesting structure. A
parent-level attribution is an expectation over the explanatory structure of its descendants. One
methodological point: the hierarchy here is a **pragmatic analytical device**. I am not claiming
the data have a true ontological hierarchy; the nested structure is a computational and
interpretive tool.

### Slide 36 — Proposition 6.1 *(17:30–18:15)*
Proposition 6.1 is the mathematical heart. Let Phi at level l in cluster c for feature j be the
expected absolute SHAP importance over examples in that cluster, and let w sub c-prime be the
relative size of a child within its parent. For a strict nested hierarchy on a consistent feature
space, the parent's expected absolute importance equals the sum over its children of the child's
relative size times the child's expected absolute importance, plus a residual epsilon that comes
from surrogate mismatch. The derivation uses the law of total expectation. Crucially, it does not
claim explanations are identical across levels; it says differences can be **interpreted** rather
than dismissed as inconsistency — which makes a hierarchical explanation self-consistent and
auditable.

### Slide 37 — Evaluation on Beijing *(18:15–18:50)*
On Beijing, the multi-criteria evaluation converges much more strongly than on wine. The full
dataset clusters cleanly into k equal to three, with a **Silhouette of about 0.63** and a
Davies-Bouldin of about 0.55. Recall this is where the 0.63 figure comes from — it belongs to
Beijing, not to the wine partition. I also tested sensitivity: the conclusions are robust to
modest variation in k, in projection dimension, and in surrogate depth; only low-ranked
variables shift.

### Slide 38 — Global importance (Beijing) *(18:50–19:30)*
The dominant features are temperature, dew point and pressure, followed by carbon monoxide,
nitrogen dioxide, PM10 and PM2.5. It is striking that it is **not** simply the pollutant
concentrations that dominate. Meteorological variables play a structurally central role,
because temperature, dew point and pressure condition dispersion, trapping and photochemical
behaviour. This is exactly the kind of insight flat, descriptive summaries often fail to make
explicit.

### Slide 39 — Regimes *(19:30–20:10)*
The force plots reveal three representative regimes. Regime A is a warm, photochemical regime,
where ozone, temperature and dew point are prominent — characteristic of summer photochemical
smog. Regime B is a wintertime smog regime, dominated by carbon monoxide, sulfur dioxide and
particulate matter, with low wind speed suppressing dispersion. Regime C is a comparatively
clean-air regime associated with favourable meteorology. The interpretative value is not merely
showing that these regimes exist — it is showing **which combinations of variables define each
one**.

### Slide 40 — Multi-level insight *(20:10–20:50)*
This is the conceptual payoff. At the coarse level, temperature and dew point dominate, because
they differentiate broad atmospheric regimes. Within individual clusters, the discriminative
variables shift to carbon monoxide, sulfur dioxide, PM10, wind speed, pressure or ozone. This
change is **not a contradiction** — it is exactly what a multi-level explanation should reveal.
The parent-level story is regime selection; the cluster-level story is variation within a regime.
Proposition 6.1 lets us interpret these shifts as meaningful structure rather than noise.

### Slide 41 — Cross-dataset generality *(20:50–21:25)*
The same logic works on both a small, dense, chemically correlated dataset and a large, noisy,
environmentally variable one, which supports the generality of the approach — it is not tied to a
domain-specific peculiarity of wine chemistry. Compared against the SHAP-based clustering
literature, our Beijing partition achieves a Silhouette of about 0.63 versus around 0.37 for
Gramegna and Giudici on credit-risk. On LIME we observe weaker structural coherence and less
stable local narratives for hierarchical reasoning. I want to be careful: these are comparative
observations rather than a comprehensive benchmark.

### Slide 42 (Answers) + 43 (Key findings) *(21:25–22:05)*
To answer **RQ2** directly: yes, with bounds. Shapley-based clustering explanation can scale to
hierarchical, large-scale settings without losing interpretive coherence, provided the hierarchy
is modelled explicitly and the approximation is transparent. O1, O2 and O3 are all met. The
honest bound is that the model is still an explanation of a pre-computed partition — it does not
yet influence learning itself. That is the bridge to Contribution III.

### Slide 44 — Limitations *(22:05–22:30)*
The clustering remains static even though the Beijing data are temporal. The surrogate-based
SHAP plus representative-instance reporting compresses observation-level variation. The approach
is confined to tabular data. And, most importantly, the model is still an explanation of a
pre-computed partition: it does not yet influence learning itself.

### Slide 45 — Takeaways *(22:30–22:50)*
Shapley attribution stays coherent across granularity when the hierarchy is made explicit. But
the attribution is still post-hoc: it explains a partition that was already computed, and it
never influences how the model learns. That is the limit that motivates Contribution III — can
cooperative attribution move beyond explanation and enter the learning dynamics of a recommender?

---

## Contribution III — DyHuCoG (Slides 46–64) — ~7.5 min

### Slide 47 (obj) + 48 (RQ3/RQ4) *(22:50–23:45)*
C3 is the flagship contribution and the conceptual shift of the whole thesis. The gap is that
graph and hypergraph recommenders treat message importance as either uniform or
attention-weighted, without a principled account of marginal contribution. Diversity is
typically a secondary objective or a re-ranking heuristic. And interpretability is added after
prediction rather than integrated into the objective. Our objectives are threefold: formulate
recommendation as a cooperative game; embed preference-aware Monte Carlo Shapley into hypergraph
message passing; and improve ranking, coverage and diversity jointly. The strongest claim is not
that we explain a recommender — it is that **attribution becomes an in-training signal**.

### Slide 49 — Cooperative-game framing *(23:45–24:30)*
We model recommendation as a cooperative game whose players are users, items and contexts. The
hypergraph has vertices from this same set, and hyperedges encode user–item–context
interactions, with dynamic edge weights derived from Shapley estimates. A coalition represents
the entities participating in a recommendation episode, and the coalition value measures the
quality of the recommendation outcome. This parallels the clustering formulation, but with a
recommendation-oriented value function. That parallelism is deliberate, and is one of the
thesis-level contributions.

### Slide 50 — Coalition utility *(24:30–25:15)*
The coalition utility combines ranking quality, diversity and context: a weighted sum of NDCG at
twenty, a diversity term and a context score, with weights summing to one. The key point is that
this is **the same trade-off the recommender must satisfy and also the trade-off from which
attribution is computed** — so the explanatory game and the predictive objective are aligned by
design. Alpha, beta, gamma were grid-searched to 0.60, 0.25, 0.15. One honest boundary: coalition
evaluation is scoped to the interaction episode, a few dozen players, not the full catalogue.

### Slide 51 — Monte Carlo Shapley *(25:15–26:00)*
Exact Shapley is combinatorial, so we use a Monte Carlo estimator that averages, over M sampled
coalitions, the difference between the value including a player and the value excluding it; the
preference-aware variant applies the same estimator to the preference-weighted utility. It is
unbiased, with variance decaying as sigma squared over M. We chose M equal to fifty: mean squared
error about one point four times ten to the minus five, and roughly ninety-nine percent accuracy.
Estimates are refreshed every ten batches and smoothed with an exponential moving average, so
attribution is adaptive without making training hypersensitive to a single estimate.

### Slide 52 — Architecture *(26:00–26:50)*
The architecture is the decisive move. The base propagation is standard hypergraph message
passing; the Shapley-weighted version weights each message by a normalised Shapley coefficient. I
clip and exponentially smooth the estimates before normalising, which stabilises the sparse
regime. Layer fusion combines embeddings across layers with learned coefficients. On top of that,
an interaction-level attention gate interpolates between the Shapley-weighted score and the
standard inner-product score, acting as a stabiliser; a context-aware score adds a context term.
The essential point is that the model is told not only who is connected to whom, but **how much
each coalition is worth**, and that worth directly governs how information propagates.

### Slide 53 — Loss *(26:50–27:35)*
The composite loss combines four terms: a Bayesian Personalised Ranking loss; an intra-list
diversity regulariser; a context alignment term; and weight decay. Negatives are drawn from a
popularity-aware distribution with periodic hard-negative refresh, and optimisation uses Adam.
The conceptual point I want to drive home is **alignment**: the model is trained to optimise the
same accuracy–diversity–context balance that later determines cooperative attribution. So the
explanation is not a separate diagnostic — it is a direct read-out of the objective the model is
already optimising. This is what gives the explanation its structural faithfulness.

### Slide 54 — Headline results *(27:35–28:30)*
This is the headline result. On MovieLens-1M, the strongest baseline HPCF achieves NDCG at twenty
of 0.2528 and recall of 0.2098; DyHuCoG improves these to 0.2775 and 0.2362 — plus nine point
seven seven percent in NDCG and plus twelve point five eight percent in recall. At the same time,
coverage rises from 0.342 to 0.397 and intra-list diversity from 0.461 to 0.516. On Amazon-Book,
which is much sparser, the relative gains are larger: plus thirteen point three percent NDCG and
plus sixteen point one six percent recall, with coverage up by nearly **thirty percent**. The
sparser the data, the larger the gain — precisely the pattern you would expect if Shapley-driven
weighting is most valuable when signal is weak.

### Slide 55 — Relative gains *(28:30–29:05)*
This summarises the relative gains over the strongest baseline, and the key message is that
DyHuCoG improves ranking accuracy, coverage and diversity simultaneously — it does not sacrifice
one for the others. Together these results are evidence that the accuracy–diversity trade-off,
often treated as structurally fixed, is in fact **negotiable** if attribution is handled as a
first-class part of the learning objective.

### Slide 56 — Diversity *(29:05–29:40)*
Both levels of diversity improve. On MovieLens-1M, catalogue coverage rises by sixteen percent and
intra-list diversity by eleven point nine percent. On Amazon-Book, coverage rises by nearly
thirty percent. The practical consequence is a reduced filter-bubble effect and greater discovery
opportunity. And I want to stress: both diversity metrics improve **while** NDCG and recall also
improve — so we are not trading accuracy for diversity.

### Slide 57 — Ablation *(29:40–30:30)*
This ablation isolates each component, and every component contributes. Removing the Shapley
value drops NDCG by four point six percent. Removing the hypergraph structure costs six point
eight percent. Removing the attention gate costs three point five percent. Removing context
causes the largest single loss at eight point two percent. Removing diversity costs five point
eight percent. The four to six percent drop when Shapley is removed supports the argument that
marginal-contribution estimation is **load-bearing rather than decorative**.

### Slide 58 — Computational cost *(30:30–31:10)*
The attribution cost is proportionate, and I report it transparently because it bears on
deployability. DyHuCoG takes about two thousand seconds to train versus roughly eleven hundred
for HPCF — about one point seven eight times. Inference is one point eight four milliseconds per
query on MovieLens, comfortably within real-time requirements. Memory is modestly higher. On
Shapley convergence, M equal to fifty gives ninety-nine percent accuracy, while M equal to one
hundred gives ninety-nine point five with diminishing returns — so fifty is the right operating
point.

### Slide 59 — Statistical validation *(31:10–31:50)*
I validated that the improvements are statistically significant and substantively meaningful with
paired t-tests on per-user NDCG at twenty across six thousand and forty users. Against HPCF, the
t-statistic is 46.38, Cohen's d is 1.33, and the p-value is on the order of ten to the minus two
hundred and seventy. The Wilcoxon signed-rank test is also significant. I should be scrupulous
about scope: these tabulated paired tests apply only to MovieLens-1M; the Amazon-Book results
remain descriptive.

### Slide 60 — Cold-start & interpretability *(31:50–32:35)*
DyHuCoG also improves the regimes where recommenders are at their most brittle. For users with
five or fewer interactions, NDCG at twenty is about 0.061, roughly ten percent over HPCF; for
cold-start items about 0.057. On interpretability, the model produces a SHAP waterfall that
decomposes a recommendation into the same ranking, diversity, context and preference components
used during training — so the explanation is structurally faithful rather than an external
approximation. And Shapley measures marginal utility rather than raw frequency, so weak but
informative interactions retain influence, mitigating popularity bias.

### Slide 61 (Answers) + 62 (Key findings) *(32:35–33:20)*
To answer **RQ3 and RQ4** directly: yes. RQ3 is answered because attribution is no longer a
post-hoc diagnostic but an in-training signal that directly shapes message passing. RQ4 is
answered because ranking, coverage and diversity improve together rather than trading against one
another. The strongest claim is that the explanation is **structurally faithful**, because it
reads out the same components the model already optimises. Within the stated edges, the claim
stands.

### Slide 63 — Limitations *(33:20–33:50)*
The limitations must be stated honestly. There is a measurable computational overhead, roughly
one point seven eight times the training time of HPCF. The method depends on the availability of
meaningful context. The Monte Carlo Shapley estimator could be improved by variance reduction. The
ablation is component-wise, so it does not test factorial interactions. And the baselines were
finalised in early 2026, so I claim superiority only against the tested baselines. Within those
bounds, the claim stands.

### Slide 64 — Takeaways *(33:50–34:15)*
The takeaway is the conceptual shift of the thesis. Attribution is a first-class part of the
learning objective, not a post-hoc diagnostic, and the explanation is a direct read-out of the
objective the model already optimises. That is what makes it structurally faithful. And because
Shapley values rest on an axiomatic, normative basis, this perspective is well aligned with the
transparency and accountability requirements of emerging AI regulation. *(pause)* This is the
central claim worth defending: explanation should be part of the modelling logic itself.

---

## Conclusion & Perspectives (Slides 65–72) — ~3.5 min

### Slide 66 — Synthesis *(34:15–34:55)*
Three contributions, one thread. C1 makes hidden structure intelligible. C2 keeps that
explanation coherent under scale and hierarchy. C3 carries the same attribution logic inside the
learning dynamics of a recommender. The common thread is that cooperative attribution is a single
mechanism used for explanation, for interpretation and for optimisation — not three unrelated
tools.

### Slide 67 — Published papers *(34:55–35:25)*
The thesis synthesises three peer-reviewed publications: Paper I in Procedia Computer Science
2023, Paper II in IJACSA 2025, and Paper III, DyHuCoG, in IJIES 2026. What the thesis adds on top
of the papers is the multi-level formalisation, the cross-chapter comparisons, and the explicit
mapping to the five research questions. In other words, the thesis is a **cumulative** argument,
not merely a bound collection of three papers.

### Slide 68 — Limitations *(35:25–35:55)*
Let me state the limitations honestly. Computationally, exact Shapley is intractable.
Methodologically, the clustering chapters depend on surrogate fidelity, and the recommendation
results depend on stable approximate contributions and meaningful context. Empirically, the work
is confined to tabular data and offline evaluation — no multimodal, sequential or online
deployment, and no dedicated human-subject study of actionability. And on the claim itself: I am
not claiming one fully unified framework that eliminates all tension between accuracy and
interpretability; I am claiming a shared perspective, a common attribution language, coherent and
productive across the three tasks.

### Slide 69 — Perspectives *(35:55–36:25)*
Future work turns these limitations into a concrete agenda. First, scalable cooperative
attribution, with lower-variance Shapley estimators and adaptive refresh. Second, online and
streaming recommendation with evolving graphs and delayed feedback. Third, richer human-centred
evaluation — do these explanations measurably improve analyst judgement, user trust,
intervention quality or perceived fairness? And fourth, broader trustworthy-AI and fairness
evaluation, connecting the work to the EU AI Act, the OECD principles and the GDPR.

### Slide 70 — Conclusion *(36:25–37:00)*
To close: the thesis answer is that cooperative game theory can function as a shared
methodological perspective for actionable explanation across clustering and recommendation. The
key outcomes are fourfold: Shapley attribution provides a common formal language for allocating
importance to features, interactions and contexts; it yields faithful clustering explanation,
hierarchical explanatory coherence, and contribution-aware recommendation learning; and it moves
explanation from commentary to method — from post-hoc description to in-training guidance. I
believe this is the central claim worth defending.

### Slides 71–72 — References *(37:00–37:20)* *(CUT IF TIGHT)*
These are the core references that ground the argument — the original Shapley value, the SHAP
framework and its tree extension, the LIME and XAI taxonomy work, the key recommender and
hypergraph baselines, and the regulatory anchor of the EU AI Act. I will be happy to go deeper on
any of them during the questions.

### Slide 73 — Q&A *(37:20)*
Thank you very much for your attention. I am now happy to take your questions and comments — I
will do my best to answer them directly, and I am happy to go deeper into any of the methodology,
the mathematics, or the experimental details.

---

## Timing summary

| Section | Slides | Target time | Running total |
|---|---|---|---|
| Introduction | 3–6 | 4 min | 4 min |
| Context & Problematic | 7–12 | 5 min | 9 min |
| Experimental Protocol | 13–17 | 2.5 min | 11.5 min |
| Contribution I | 18–31 | 5 min | 16.5 min |
| Contribution II | 32–45 | 5 min | 21.5 min |
| Contribution III | 46–64 | 7.5 min | 29 min |
| Conclusion & Perspectives | 65–72 | 3.5 min | 32.5 min |
| Q&A opening | 73 | — | — |

**Target: 32–33 minutes of talking + interruptions ≈ 38–40 min.** The two "CUT IF TIGHT"
segments let you reclaim ~1.5 min.
