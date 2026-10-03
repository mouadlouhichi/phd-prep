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
json.dump(out, open(os.path.join(HERE, "notes_v20.json"), "w"), ensure_ascii=False, indent=1)

# each speech entry is spoken once, even when two slides share it in notes
spoken = sum(len(rewrite.get(k, v).strip().split()) for k, v in speech.items())
spoken += len(notes[31][0].split()) + len(notes[50][0].split())
print("spoken words (1-76):", spoken, "-> %.1f min @130wpm, %.1f @120" % (spoken / 130.0, spoken / 120.0))
missing = [d for d in range(1, 80) if str(d) not in out]
print("slides without notes:", missing)
bad = [d for d, t in out.items() if ";" in t or "—" in t]
print("notes with ; or em-dash:", bad)
