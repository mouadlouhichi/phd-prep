"""Build notes_v20.json from try/speech_enhanced.fixed.json.

The fixed speech was authored as 75 entries for an older slide order; this
script re-aligns every entry to the 79-slide v19/v20 deck, trims the longest
entries so the main flow lands on ~36 minutes at 130 wpm, and adds two short
transitions for slides the speech never covered (C1 evaluation protocol and
the Contribution II takeaway). Backup slides 77-79 are not part of the flow.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "speech_enhanced.fixed.json")

speech = json.load(open(SRC))

# --- trims: full replacements for the longest entries (spoken register,
#     no semicolons, no em dashes, technical terms kept verbatim) ----------
rewrite = {}
rewrite["2"] = """So here is how I have organized the next thirty-six minutes.\n\nI will start with the motivation behind this research and introduce the concept of actionable insight, which is the central idea of this thesis.\n\nThen, I will present the research context, the limitations of existing approaches, and the research questions that motivated this work.\n\nAfter that, I will describe the common experimental protocol before presenting the three contributions.\n\nEach contribution follows the same structure: the research gap, the objectives, the methodology, the evaluation protocol, the results, and the main findings.\n\nFinally, I will conclude with the main outcomes of the thesis and the future perspectives."""
rewrite["5"] = """Three questions are behind this thesis.

The first one concerns scale. Recommendation models now influence the experience of billions of users worldwide.

The second concerns transparency. Even state-of-the-art systems are often black boxes. We see their outputs, but not the reasons behind them.

The third concerns trust. Can we integrate transparency directly into the model, instead of adding explanations afterwards?

Accuracy and interpretability should not compete. They are two goals to achieve together."""
rewrite["6"] = """That brings me to the definition the whole thesis turns on.

An explanation is actionable when it points to something we can actually change, and when changing it clearly affects the model output.

It should also speak the language of the domain, like acidity in wine, pollution indicators in air quality, or user preferences in recommendation.

So a good explanation does not only describe what happened. It tells us what to change to improve the outcome."""
rewrite["7"] = """Now let me put this in context by looking at the evolution of recommendation systems.

Early similarity-based approaches were easier to explain because they relied on visible features.

Then matrix factorization improved accuracy and scalability, but introduced latent factors whose meanings were hidden.

Later, neural and graph-based approaches increased modelling power through hidden representations and message passing.

Finally, hypergraph models introduced richer relationships between users, items and contexts.

At each step we gained predictive power while losing transparency. This growing gap is exactly what this thesis addresses."""
rewrite["8"] = """These systems are not only theoretical models. They are already part of everyday applications.

Netflix, Spotify, Amazon and Yelp use recommendation to personalize the experience of millions of users.

The performance is impressive, but the reasoning behind each suggestion stays hidden from the user.

Everywhere, and hidden: that is exactly the gap this thesis targets."""
rewrite["14"] = """From this evolution, several limitations of current recommendation systems appear.

First, data sparsity: the interaction matrix is almost empty in many real-world scenarios. Second, cold-start, when new users or items lack history. Third, popularity bias, where popular items take exposure from relevant but less popular ones.

And above all, the absence of interpretability. For clustering it is even harder, because existing approaches rarely give local and global explanations in a consistent way."""
rewrite["15"] = """These observations lead to three problems that shape this research.

First, complex models are difficult to explain in a way that is faithful and actionable.

Second, explanations often do not scale to large datasets or multi-level structures.

Third, explanations are usually produced after training, so they describe the model without influencing how it learns.

The central idea of this thesis is that Shapley attribution provides one cooperative-game framework for these three challenges."""
rewrite["19"] = """Four datasets are used in this thesis, covering both clustering and recommendation tasks.

For clustering, I use Wine Quality and Beijing Air Quality. The first checks whether explanations stay connected to meaningful physical variables. The second provides a larger and more complex scenario for scalability and multi-level explanations.

For recommendation, I use MovieLens-1M and Amazon-Book, which represent different levels of sparsity."""
rewrite["28"] = """The difficulty comes from the nature of clustering itself.

Unlike supervised learning, clustering has no predefined target variable. The model discovers groups directly from the data, which makes the reason behind each cluster harder to understand.

Existing explanation approaches focus either on individual instances or on global cluster descriptions, but rarely provide both levels at once.

Therefore, the first contribution investigates how Shapley attribution can provide a faithful explanation framework for black-box clustering."""
rewrite["30"] = """Before the methodology, let me introduce the mathematical foundation of this work: cooperative game theory.

A cooperative game has a set of players, the coalitions between them, and a value function that measures what each coalition creates on its own.

The question is how to share the total fairly. The Shapley value answers it: the average marginal contribution of each player across all arrival orders.

Here the players are the input features, and the Shapley value measures each feature's contribution to the clustering result."""
rewrite["31"] = """To apply Shapley values to clustering, the clustering problem is reformulated as a cooperative game.

The players are the features, and the value function is the quality of the clustering obtained with a subset of features, measured by the Silhouette score.

Evaluating every coalition is too expensive, so a surrogate model approximates the clustering decisions and makes Shapley computation practical."""
rewrite["33"] = """One important choice concerns the number of clusters.

Geometrically, two clusters give the best separation according to the clustering metrics.

But three clusters are selected because they give more meaningful chemical interpretations.

This illustrates a principle of the thesis: the goal is not only to optimize mathematical criteria, but also to obtain explanations that support human understanding and decision-making."""
rewrite["34"] = """The results show that several variables play a major role in explaining the wine clusters.

The most important factors include density, pH, acidity, sulfur dioxide variables, and alcohol content, all real physicochemical properties of wine.

And the explanation is not limited to a global ranking: different clusters are characterized by different combinations of important variables."""
rewrite["20"] = """The first dataset is the Portuguese White Wine Quality dataset.

It contains 4,898 samples described by 11 physicochemical measurements, including acidity, density, sulphates, and alcohol.

It suits the first contribution because every variable has a clear meaning in the chemistry of wine."""
rewrite["21"] = """The second dataset is Beijing Multi-Site Air Quality, with 383,585 hourly records of weather variables and pollutant concentrations.

It provides a much larger and more complex scenario, used to test scalability and multi-level explanations."""
rewrite["26"] = """Finally, the computational environment: clustering experiments ran on a standard workstation, while DyHuCoG training used an RTX 4090 GPU.

These configurations let us evaluate performance and scalability in realistic conditions."""
rewrite["45"] = """The clustering results show that the obtained structure is meaningful, with a Silhouette score of about 0.63 and a Davies-Bouldin score around 0.55.

And the stability analysis shows the conclusions remain consistent under changes in the number of clusters, projection dimension, and surrogate complexity."""
rewrite["46"] = """The global explanation gives an interesting environmental interpretation.

The most important variables are temperature, dew point, and pressure, followed by pollutants such as carbon monoxide, nitrogen dioxide, and particulate matter.

Pollution patterns are not determined by pollutant concentrations alone. Weather conditions influence how pollutants accumulate, disperse, and interact."""
rewrite["56"] = """The main challenge is that exact Shapley computation is impossible for large recommendation systems, because the number of coalitions grows exponentially with the number of players.

Therefore, DyHuCoG uses Monte Carlo approximation: we sample a limited number of permutations and estimate the average marginal contribution.

This gives a practical approximation while preserving the main properties of Shapley attribution."""

# v21 alignment pass: the slides are the technical reference, the speech is
# brought up to their level (slide 12), corrected (slide 33: fixed acidity)
# and lightly trimmed to keep the 36-minute budget.
rewrite["13"] = """The fourth family, and the one that is most important for this thesis, is graph-based and hypergraph recommendation.

These approaches represent users, items and their interactions as nodes and edges in a graph, and they use message passing, as in LightGCN, HCCF and HPCF, so that information reaches multi-hop neighbours.

Hypergraphs go one step further: a single hyperedge can connect a user, an item and a context at the same time, which is why these models reach state-of-the-art accuracy on sparse benchmarks such as MovieLens-1M and Amazon-Book.

The price is twofold: large graphs cost compute and memory, and every message is treated as equally important, so the model cannot say which relationships actually mattered. That hidden importance is exactly the gap this thesis addresses."""
rewrite["34"] = """The results show that several variables play a major role in explaining the wine clusters.

The most important factors include density, pH, fixed acidity, sulfur dioxide variables, and alcohol content, all real physicochemical properties of wine.

And the explanation is not limited to a global ranking: different clusters are characterized by different combinations of important variables."""
rewrite["30"] = """To apply Shapley values to clustering, the clustering problem is reformulated as a cooperative game.

The players are the features, and the value function is the quality of the clustering obtained with a subset of features, measured by the Silhouette score.

Evaluating every coalition is too expensive, so a surrogate model approximates the clustering decisions and makes Shapley computation practical.

The pipeline has four steps: K-Means creates the initial clusters, a LightGBM classifier reproduces these assignments, TreeSHAP computes the feature contributions on the surrogate, and the explanations are compared with LIME."""
rewrite["58"] = """The results on MovieLens-1M show that DyHuCoG achieves the best performance among the evaluated methods.

Compared with the strongest baseline, HPCF, the NDCG score improves from 0.2528 to 0.2775, an improvement of approximately 9.8 percent, and Recall improves as well.

Coverage and diversity stay higher too, so the gain does not come from pushing popular items: the variety of the recommendations is preserved."""
rewrite["59"] = """The same evaluation is conducted on Amazon-Book, a much more challenging sparse recommendation scenario.

Despite the higher difficulty, DyHuCoG continues to outperform the baselines, and the improvement over HPCF reaches approximately 13.3 percent in NDCG.

So cooperative attribution remains useful even when interaction information is limited."""

# v22 read-along pass: every note now mirrors its slide's wording and numbers,
# so the presenter can glance at the slide and read from it.
rewrite["4"] = """How do black-box AI systems shape what billions of users see, buy and watch every day? Recommenders now shape news, study, health and credit decisions, and the market is projected above 15 billion dollars by 2029.

Why do state-of-the-art recommenders and clustering pipelines stay black boxes? Deep and graph models hide their logic and are hard to audit, and under the EU AI Act, high-risk systems must explain themselves.

And how can transparency be built into the model instead of being added afterwards, so the insight is accountable, auditable and actionable, not just accurate?"""
rewrite["5"] = """The core tension on this slide is that as models gain power, they lose the transparency needed for trustworthy use.

This thesis treats accuracy and interpretability as goals to be met together, not traded against each other."""
rewrite["15"] = """Five research questions follow, and the slide maps each one to a contribution.

RQ1 asks whether Shapley values can explain black-box clustering faithfully at instance and cluster level. RQ2 extends this to large-scale, multi-level clustering while staying feasible and consistent. RQ3 asks whether cooperative attribution can move beyond post-hoc and become part of how a recommender learns, and RQ4 whether ranking, context and diversity improve together. RQ5 asks what one cooperative-game view brings to both explanation and recommendation."""
rewrite["20"] = """The first dataset is the Portuguese White Wine Quality dataset.

It contains 4,898 samples described by 11 physicochemical measurements, including acidity, density, sulphates, and alcohol.

It suits the first contribution because every variable has a clear meaning in the chemistry of wine. The slide also shows the choice used later: three clusters, selected for interpretability."""
rewrite["21"] = """The second dataset is Beijing Multi-Site Air Quality, with 383,585 hourly records.

The slide lists the 11 modelling variables: six pollutants and five weather variables, including temperature, pressure and dew point.

It provides a much larger and more complex scenario, used to test scalability and multi-level explanations."""
rewrite["23"] = """Reproducibility and the prevention of data leakage are central to the design, as the slide summarises.

For clustering, five-fold cross-validation checks the surrogate and attribution stability, features are standardised, k is chosen by elbow, Silhouette and Davies-Bouldin, and the surrogate must pass a fidelity floor of macro-F1 around 0.82.

For recommendation, the split is user-level and time-ordered, 70 train, 10 validation and 20 test, the latest positive per user is the leave-one-out target, ratings above 3 count as positive, and seeds 42 to 46 with early stopping keep everything reproducible."""
rewrite["24"] = """The baselines cover four families, so the effect of cooperative attribution is not confused with a lucky model choice.

For clustering explanation, the comparison is the LIME surrogate pipeline, the standard alternative to SHAP. For recommendation, the slide lists MF, NCF, LightGCN, RecDCL, HCCF and HPCF, and HPCF is the strongest reference."""
rewrite["30"] = """Before the methodology, the mathematical foundation: cooperative game theory.

A cooperative game has players, the coalitions between them, and a value function that measures what each coalition creates on its own. On the slide, the band example: alone, Guitar, Voice and Drums earn 60, 40 and 20; as a duo, 140; and the whole band earns 200.

The Shapley value shares the total fairly, as the average marginal contribution over every arrival order. The slide's order V, D, G gives 40, then plus 40, then plus 120, and the six orders average to 90, 70, 40. It is the only rule satisfying efficiency, symmetry, null player and additivity at once.

In this thesis, the players are the input features, and the value function is the Silhouette of the clustering."""
rewrite["31"] = """Why a surrogate? As the slide says, direct TreeSHAP on K-Means is impossible, because TreeSHAP explains tree models, not centroids, and explaining the PCA representation would move attribution away from the interpretable variables.

So the surrogate keeps the chemistry and pollution terms that make the analysis actionable, under one validity condition: high fidelity, with macro-F1 of about 0.82 as the floor."""
rewrite["32"] = """The pipeline on the slide has four steps. K-Means produces the cluster labels. A LightGBM multiclass surrogate learns to predict them from the original features. TreeSHAP then gives fast, exact attribution in that same feature space, and the outputs are global importance, cluster profiles and local force plots.

The key point is that the surrogate must faithfully reproduce the original clustering behaviour."""
rewrite["33"] = """One important choice concerns the number of clusters, and the slide shows the trade-off.

Geometrically, k = 2 wins, with Silhouette 0.214 and Davies-Bouldin 1.775, against 0.144 and 2.097 for k = 3.

But k = 3 is selected because three clusters give a richer, more meaningful wine partition, so more actionable explanations. Interpretability outranks geometry. And the higher Silhouette of about 0.63 belongs to Beijing in Contribution II, not to this wine partition."""
rewrite["53"] = """This contribution addresses two research questions: can cooperative attribution move beyond post-hoc and become part of how a recommender learns, and can it improve ranking, context and diversity together?

The slide lists three objectives. First, model recommendation as a cooperative game over users, items and contexts. Second, put preference-aware Monte Carlo Shapley inside message passing as dynamic hyperedge weights. Third, optimise ranking accuracy, diversity and contextual relevance together."""
rewrite["56"] = """The main challenge is that exact Shapley computation is impossible for large recommendation systems, because the number of coalitions grows exponentially with the number of players.

Therefore, DyHuCoG uses Monte Carlo approximation: we sample a limited number of permutations and estimate the average marginal contribution.

This gives a practical approximation while preserving the main properties of Shapley attribution. As the table on the slide shows, M = 50 balances quality and cost, with an MSE around 1.4 times 10 to the minus 5, about 99 percent accuracy."""
rewrite["61"] = """To understand the contribution of each component, an ablation study is performed, removing one component at a time.

The results show that each component plays an important role. Removing contextual information produces the largest degradation, and removing Shapley weighting also reduces performance, so cooperative attribution contributes directly to learning.

The tables make it concrete: removing context costs 8.2 percent on MovieLens-1M and 11.0 percent on Amazon-Book, the hypergraph 6.8 and 8.9, and the Shapley weighting 4.6 and 6.1."""
rewrite["62"] = """Of course, integrating Shapley estimation into training introduces an additional computational cost.

DyHuCoG requires more training time than traditional hypergraph recommenders because attribution is computed during learning. However, inference remains practical.

Concretely, training takes about 1.78 times HPCF on MovieLens-1M, and inference stays at 1.84 milliseconds per query, suitable for real-time use."""
rewrite["63"] = """To verify that the improvements are not due to random variation, statistical validation is performed with paired tests on per-user results.

The tests confirm that the improvements over the baselines are significant, and the effect sizes show that the gain is practically meaningful, not only statistically detectable.

The slide gives the figures: t = 46.38 with 6,039 degrees of freedom, a Cohen's d of 1.33, a large effect, and significance after Holm-Bonferroni correction."""
rewrite["68"] = """The three contributions follow a common progression: explain, scale, and guide.

The first explains black-box clustering with Shapley attribution and meaningful domain variables. The second keeps the explanation consistent across levels at scale. The third uses attribution to guide what the recommender learns.

One cooperative-game definition, three value functions: the same Shapley logic runs through all of them."""
rewrite["72"] = """To conclude, cooperative game theory provides a common framework for explainable AI across clustering and recommendation.

As the slide sums up: Shapley attribution is a common formal language; it explains black-box clustering with meaningful variables; it stays consistent at scale and across levels; and through DyHuCoG it becomes part of the learning process itself.

Explanation does not have to remain a description of what happened. It can help us understand, control and improve AI systems."""

# v22 final pass: punctuation fixes and trims to hold the 36-minute budget.
rewrite["1"] = """Good morning, Mister President. Good morning, Professors. Thank you for the opportunity to present my work today.

My name is Mouad Louhichi, and the thesis I am defending, supervised by Professor Mohamed Lazaar, is entitled Cooperative Game Theory for Explainable AI in Recommendation Systems, A Shapley Framework for Actionable Insight.

The idea to keep in mind: Shapley attribution is not only a post-hoc explanation method. In this thesis it becomes a unified framework that explains black-box models, stays consistent across levels of detail, and guides how recommendation systems learn."""
rewrite["4"] = """How do black-box AI systems shape what billions of users see, buy and watch every day? Recommenders now shape news, study, health and credit decisions, a market above 15 billion dollars by 2029.

Why do state-of-the-art recommenders and clustering pipelines stay black boxes? Deep and graph models hide their logic and are hard to audit, and under the EU AI Act, high-risk systems must explain themselves.

And how can transparency be built into the model instead of being added afterwards, so the insight is accountable, auditable and actionable, not just accurate?"""
rewrite["15"] = """Five research questions follow, mapped on the slide to the contributions.

RQ1 asks whether Shapley values can explain black-box clustering faithfully at instance and cluster level. RQ2 extends this to large-scale, multi-level clustering while staying feasible and consistent. RQ3 asks whether cooperative attribution can move beyond post-hoc and become part of how a recommender learns, and RQ4 whether ranking, context and diversity improve together. RQ5 asks what one cooperative-game view brings to both explanation and recommendation."""
rewrite["16"] = """These research questions lead to three contributions, as the slide maps them.

The first introduces a Shapley-based framework for explaining black-box clustering, evaluated on Wine Quality. The second extends it to large-scale multi-level clustering on Beijing Air Quality, with a formal consistency argument. The third, DyHuCoG, integrates cooperative attribution directly into hypergraph recommendation learning.

Together they follow one progression: from explanation, to scalability, to action."""
rewrite["19"] = """Four datasets are used in this thesis, covering both clustering and recommendation tasks.

For clustering, I use Wine Quality and Beijing Air Quality. The first checks whether explanations stay connected to meaningful physical variables. The second provides a larger and more complex scenario for scalability and multi-level explanations."""
rewrite["21"] = """The second dataset is Beijing Multi-Site Air Quality, with 383,585 hourly records.

The slide lists the 11 modelling variables: six pollutants and five weather variables.

It provides a much larger and more complex scenario, used to test scalability and multi-level explanations."""
rewrite["23"] = """Reproducibility and the prevention of data leakage are central to the design, as the slide summarises.

For clustering, five-fold cross-validation checks the surrogate and attribution stability, features are standardised, k is chosen by elbow, Silhouette and Davies-Bouldin, and the surrogate must pass a fidelity floor of macro-F1 around 0.82.

For recommendation, the split is user-level and time-ordered, 70 train, 10 validation and 20 test, with a leave-one-out target, ratings above 3 as positive, and seeds 42 to 46 with early stopping."""
rewrite["30"] = """Before the methodology, the mathematical foundation: cooperative game theory.

A cooperative game has players, the coalitions between them, and a value function that measures what each coalition creates on its own. On the slide, the band example: alone, Guitar, Voice and Drums earn 60, 40 and 20, reach 140 as a duo, and 200 as the whole band.

The Shapley value shares the total fairly, as the average marginal contribution over every arrival order. As the slide shows, one arrival order adds 40, then 40, then 120, and the average over the six orders is 90, 70, 40. It is the only rule satisfying efficiency, symmetry, null player and additivity at once.

In this thesis, the players are the input features, and the value function is the Silhouette of the clustering."""
rewrite["31"] = """Why a surrogate? As the slide says, direct TreeSHAP on K-Means is impossible, because TreeSHAP explains tree models, not centroids, and explaining the PCA representation would move attribution away from the interpretable variables.

So the surrogate keeps the domain terms that make the analysis actionable, with a fidelity floor of macro-F1 about 0.82."""
rewrite["33"] = """One important choice concerns the number of clusters, and the slide shows the trade-off.

Geometrically, k = 2 wins, with Silhouette 0.214 and Davies-Bouldin 1.775, against 0.144 and 2.097 for k = 3.

But k = 3 is selected because three clusters give a richer, more meaningful wine partition, so more actionable explanations. Interpretability outranks geometry. And the 0.63 Silhouette you will see later belongs to Beijing, not to this partition."""
rewrite["53"] = """This contribution addresses two research questions, shown on the slide: can cooperative attribution become part of how a recommender learns, and can it improve ranking, context and diversity together?

The slide lists three objectives. First, model recommendation as a cooperative game over users, items and contexts. Second, put preference-aware Monte Carlo Shapley inside message passing as dynamic hyperedge weights. Third, optimise ranking accuracy, diversity and contextual relevance together."""
rewrite["56"] = """The main challenge is that exact Shapley computation is impossible for large recommendation systems, because the number of coalitions grows exponentially with the number of players.

Therefore, DyHuCoG uses Monte Carlo approximation: we sample a limited number of permutations and estimate the average marginal contribution.

This gives a practical approximation while preserving the main properties of Shapley attribution, and the table shows M = 50 reaches about 99 percent accuracy."""
rewrite["61"] = """To understand the contribution of each component, an ablation study is performed, removing one component at a time.

The results show that each component plays an important role. Removing contextual information produces the largest degradation, and removing Shapley weighting also reduces performance, so cooperative attribution contributes directly to learning.

The tables give the drops: context 8.2 and 11.0 percent, hypergraph 6.8 and 8.9, Shapley weighting 4.6 and 6.1."""
rewrite["62"] = """Of course, integrating Shapley estimation into training introduces an additional computational cost.

DyHuCoG requires more training time than traditional hypergraph recommenders because attribution is computed during learning, while inference stays practical.

Concretely, training takes about 1.78 times HPCF on MovieLens-1M, and inference stays at 1.84 milliseconds per query, suitable for real-time use."""
rewrite["63"] = """To verify that the improvements are not due to random variation, statistical validation is performed with paired tests on per-user results.

The tests confirm that the improvements over the baselines are significant, and the effect sizes show that the gain is practically meaningful, not only statistically detectable.

The slide gives the figures: t = 46.38, a Cohen's d of 1.33, significant after Holm-Bonferroni correction."""
rewrite["72"] = """To conclude, cooperative game theory provides a common framework for explainable AI across clustering and recommendation.

As the slide sums up, Shapley attribution is a common formal language. It explains black-box clustering with meaningful variables, stays consistent at scale and across levels, and through DyHuCoG becomes part of the learning process itself.

Explanation does not have to remain a description of what happened. It can help us understand, control and improve AI systems."""

# v22 trim to hold 36 minutes
rewrite["13"] = """The fourth family, and the one that is most important for this thesis, is graph-based and hypergraph recommendation.

These approaches represent users, items and their interactions as nodes and edges in a graph, and they use message passing, as in LightGCN, HCCF and HPCF, so that information reaches multi-hop neighbours.

Hypergraphs go one step further: a single hyperedge can connect a user, an item and a context at the same time, which is why they reach state of the art on sparse benchmarks such as MovieLens-1M and Amazon-Book.

The price: large graphs cost compute and memory, and every message is treated as equally important, so which relationships mattered stays hidden. That hidden importance is the gap this thesis addresses."""
rewrite["20"] = """The first dataset is the Portuguese White Wine Quality dataset.

It contains 4,898 samples described by 11 physicochemical measurements, including acidity, density, sulphates, and alcohol.

It suits the first contribution because every variable has a clear meaning in the chemistry of wine."""
rewrite["22"] = """For recommendation experiments, two datasets are considered.

The first one is MovieLens-1M, containing approximately one million ratings from more than six thousand users over thousands of movies. It is the standard benchmark of the field.

The second one is Amazon-Book, which is much more sparse, with millions of interactions but a very low user-item density.

This allows us to evaluate whether the proposed method remains effective when the available signal is limited."""
rewrite["24"] = """The baselines cover four families, so the effect of cooperative attribution is not confused with a lucky model choice.

For clustering explanation, the comparison is the LIME surrogate pipeline. For recommendation, the slide lists MF, NCF, LightGCN, RecDCL, HCCF and HPCF, and HPCF is the strongest reference."""
rewrite["30"] = """Before the methodology, the mathematical foundation: cooperative game theory.

A cooperative game has players, the coalitions between them, and a value function that measures what each coalition creates on its own. On the slide, the band example: alone, Guitar, Voice and Drums earn 60, 40 and 20, reach 140 as a duo, and 200 as the whole band.

The Shapley value shares the total fairly, as the average marginal contribution over every arrival order. As the slide shows, one arrival order adds 40, then 40, then 120, and the average over the six orders is 90, 70, 40. As the orange bar states, it is the only rule satisfying the four axioms at once.

In this thesis, the players are the input features, and the value function is the Silhouette of the clustering."""
rewrite["32"] = """The pipeline on the slide has four steps. K-Means produces the cluster labels. A LightGBM multiclass surrogate learns to predict them from the original features. TreeSHAP then gives fast, exact attribution in that same feature space, and the outputs are global importance, cluster profiles and local force plots."""
rewrite["56"] = """The main challenge is that exact Shapley computation is impossible for large recommendation systems, because the number of coalitions grows exponentially with the number of players.

Therefore, DyHuCoG uses Monte Carlo approximation: we sample a limited number of permutations and estimate the average marginal contribution.

This preserves the main properties of Shapley attribution, and the table shows M = 50 reaches about 99 percent accuracy."""
rewrite["63"] = """To verify that the improvements are not due to random variation, statistical validation is performed with paired tests on per-user results.

The tests confirm that the improvements over the baselines are significant, and the effect sizes show that the gain is practically meaningful.

The slide gives the figures: t = 46.38, a Cohen's d of 1.33, significant after Holm-Bonferroni correction."""

# --- speech entry -> deck slide(s) ----------------------------------------
MAP = {
    1: [1], 2: [2], 3: [3], 4: [4], 5: [4], 6: [5], 7: [6], 8: [7], 9: [8],
    10: [9], 11: [10], 12: [11], 13: [12], 14: [13], 15: [14], 16: [15],
    17: [16], 18: [17], 19: [18], 20: [18], 21: [19], 22: [20, 21], 23: [22],
    24: [23], 25: [24], 26: [25], 27: [26], 28: [27], 29: [28], 30: [29],
    31: [30], 32: [30], 33: [32], 34: [33], 35: [34], 36: [35], 37: [36],
    38: [37], 39: [38], 40: [39], 41: [40], 42: [41], 43: [42], 44: [43],
    45: [44], 46: [45], 47: [46], 48: [47], 49: [48], 50: [49], 51: [51],
    52: [53], 53: [53], 54: [54], 55: [55], 56: [56], 57: [57], 58: [58],
    59: [59], 60: [60], 61: [61], 62: [62], 63: [63], 64: [64], 65: [65],
    66: [66], 67: [67], 68: [68], 69: [69], 70: [70], 71: [71], 72: [72],
    73: [73, 74], 74: [73, 74], 75: [75, 76],
}
# fix: entries 51..75 per alignment analysis
MAP.update({51: [51], 52: [52], 53: [53], 54: [53], 55: [54], 56: [55],
            57: [56], 58: [57], 59: [58], 60: [59], 61: [60], 62: [61],
            63: [62], 64: [63], 65: [64], 66: [65], 67: [66], 68: [67],
            69: [68], 70: [69], 71: [70], 72: [71], 73: [72], 74: [73, 74],
            75: [75, 76]})

notes = {}
for k, v in speech.items():
    text = rewrite.get(k, v).strip()
    for d in MAP[int(k)]:
        notes.setdefault(d, [])
        notes[d].append(text)

# transitions for slides the speech never covered
notes[31] = ["""The protocol for this contribution is straightforward. We compare SHAP and LIME on stability and cross-cluster comparability, and we check the global ranking against the known chemistry of the wine."""]
notes[50] = ["""Contribution II therefore delivers explanations that scale and stay consistent across levels, but the pipeline is still static. Preferences change over time, and nothing here adapts to that. That open point is exactly what Contribution III takes on."""]
for d in (77, 78, 79):
    notes[d] = ["Backup slide. Not part of the main flow. Shown only during the discussion if asked."]

out = {str(d): "\n\n".join(notes[d]) for d in sorted(notes)}
json.dump(out, open(os.path.join(HERE, "notes_v22.json"), "w"), ensure_ascii=False, indent=1)

# each speech entry is spoken once, even when two slides share it in notes
spoken = sum(len(rewrite.get(k, v).strip().split()) for k, v in speech.items())
spoken += len(notes[31][0].split()) + len(notes[50][0].split())
print("spoken words (1-76):", spoken, "-> %.1f min @130wpm, %.1f @120" % (spoken / 130.0, spoken / 120.0))
missing = [d for d in range(1, 80) if str(d) not in out]
print("slides without notes:", missing)
bad = [d for d, t in out.items() if ";" in t or "—" in t]
print("notes with ; or em-dash:", bad)
