# -*- coding: utf-8 -*-
"""100 viva questions with dissertation-level answers — categories E to H (Q051-Q100)."""

GROUPS = [
# ============================================================ E. CONTRIBUTION III
{
 "title": "E · Contribution III — DyHuCoG and in-training attribution",
 "items": [
{
 "q": "What is genuinely new here compared with HCCF, HPCF, or a standard attention mechanism?",
 "a": """Three things, and they can be stated precisely. First, the origin of the weights. Hypergraph recommenders
 treat message importance as uniform or learn it implicitly through attention or through the loss; here the
 importance of an entity is a Shapley value of an explicitly defined cooperative game whose characteristic function
 is the recommendation quality achievable by a coalition, v(S) = α·NDCG@20(S) + β·Diversity(S) + γ·ContextScore(S),
 plus a preference term. So the weight has an allocation-theoretic interpretation with the four Shapley properties,
 not just a learned scalar. Second, the alignment of objectives: the game is built from the same three concerns
 the composite loss optimises, so the explanation is a read-out of what the model is trained for, rather than an
 external reconstruction. Third, the temporality: the weights are refreshed periodically during training and
 smoothed, so the attribution evolves with the model instead of being computed once after convergence.""",
 "tags": ["must know"],
},
{
 "q": "Is the gain from the Shapley weighting, or from adding more components?",
 "a": """The ablation answers this directly, component by component, and it is the reason the ablation slide exists.
 Removing the Shapley weighting costs 4.6 % NDCG@20 on MovieLens-1M and 6.1 % on Amazon-Book. For calibration,
 the other drops are: context −8.2 % / −11.0 %, hypergraph structure −6.8 % / −8.9 %, diversity −5.8 % / −5.8 %,
 and attention −3.5 % / −3.5 %. So Shapley weighting is not the largest single component — context is — but it has
 its own measurable contribution, and it contributes *more* on the sparser dataset, which is exactly where the
 thesis expects cooperative weighting to matter most. The honest caveat is that the ablation removes one component
 at a time; it does not test combinations, so it cannot separate interactions between components. I would rather
 state that limitation than claim a larger effect than the design supports.""",
 "tags": ["danger", "must know"],
},
{
 "q": "Why M = 50 permutations and not more?",
 "a": """Because it is the knee of the accuracy-versus-cost curve. The reported convergence table has four points:
 M = 10 gives MSE ≈ 1.4×10⁻⁴ and about 95 % agreement with a high-sample reference at roughly 1.3× the base
 training cost; M = 25 gives 5.6×10⁻⁵ and about 98 % at 1.6×; M = 50 gives 1.4×10⁻⁵ and about 99 % at 1.78×; and
 M = 100 gives 3.5×10⁻⁶ and about 99.5 % at 2.5×. Between 50 and 100 the error falls by a factor of four while the
 training cost rises by about 40 %, and the practical benefit at that point is below the noise of the downstream
 metric. The estimator's variance is σ²/M, so error falls with the square root of the sample count — halving the
 error costs four times the samples. M = 50 also interacts well with the refresh period: estimates are refreshed
 every 10 batches, about 49 times per epoch, then clipped, exponentially smoothed and normalised.""",
 "tags": ["numbers", "must know"],
},
{
 "q": "What is the per-epoch cost of the method, and where does it go?",
 "a": """The slide gives the expression O((L+1)·m·d) + O((M/f)·m): the first term is the hypergraph propagation over
 L layers with m edges and d-dimensional embeddings, and the second is the periodic Shapley refresh with M
 permutations amortised over a refresh period of f batches. The second term is what makes the method distinctive
 and it is why f matters: refreshing every batch would multiply the cost of the sampling, while refreshing every
 10 batches keeps it bounded — about 49 refreshes per epoch at batch size 2048. Empirically this lands at about
 1.78× the training time of HPCF on MovieLens-1M (roughly 2,000 s versus 1,125 s, which is about 3.4× the
 MF baseline), while inference stays at 1.84 ms per query. The important structural point is that the extra cost
 is confined to the refresh period, so it is a tunable trade-off rather than an unavoidable multiplier.""",
 "tags": ["numbers"],
},
{
 "q": "If Shapley estimates already encode importance, why do you also need an attention gate?",
 "a": """Because they do different jobs at different points in the pipeline, and this is a distinction the thesis
 makes explicitly. The Shapley coefficients encode coalition utility *before* propagation: they determine how
 strongly a relationship is allowed to carry information. The attention gate adaptively reweights the propagated
 signal *during* representation learning and scoring, acting as an interpolation between Shapley-weighted
 propagation and a more uniform mode. Its practical role is robustness: in early training the sampled Shapley
 estimates are noisy, and the gate lets the model lean less on them until they stabilise. That is why the ablation
 removes the gate and loses only 3.5 % NDCG@20 — the smallest drop of the five components, which is the expected
 signature of a stabiliser rather than a source of signal. If the question is "is the gate redundant with the
 weights?", the answer is no: one is the input to propagation, the other is a correction on its output.""",
 "tags": ["danger"],
},
{
 "q": "Is the Amazon-Book improvement statistically significant?",
 "a": """No, and the thesis does not claim that it is. The fully tabulated paired tests — paired t-tests on per-user
 NDCG@20 with Holm-Bonferroni correction and Wilcoxon as a distribution-free check — are reported for
 MovieLens-1M, where all six comparisons against the baselines are significant with Cohen's dz ≥ 1.33. For
 Amazon-Book the thesis reports the same ordering over five seeds and calls the gains descriptive; the standard
 deviations on the backup table show why, since the ±1σ bands for NDCG@20 and Recall@20 approach each other
 between DyHuCoG and HPCF. The correct sentence is: "on Amazon-Book I report a consistent descriptive gain over
 five seeds, roughly 13.3 % in NDCG@20, with the caveat that the variance there is large relative to the
 difference." That is the third of the three things never to say in the viva, and it is worth rehearsing the
 correct phrasing until it is automatic.""",
 "tags": ["danger", "must know"],
},
{
 "q": "Is 0.2775 against 0.2528 a meaningful improvement in practice?",
 "a": """It is a 9.8 % relative improvement in NDCG@20 over the strongest baseline, and three pieces of context make
 it meaningful rather than cosmetic. First, it is not isolated: Recall@20 rises 12.6 %, catalogue coverage 16.1 %
 and intra-list diversity 11.9 % at the same time, so the gain is not a narrow trade. Second, it is a large effect
 by convention: Cohen's dz = 1.33 against HPCF, where 0.8 is already considered large, and the paired test is
 significant after correction for six comparisons. Third, the comparison is against a recent strong model, not a
 weak baseline: MF sits at 0.1200 and LightGCN at 0.2130, so most of the improvement in the table comes from
 architecture and the last step comes from this contribution. In a production system, however, a 9.8 % NDCG gain
 is only one input to a decision that includes latency, cost and business metrics — and the cost here is about
 1.78× the training time, which I would state alongside the gain.""",
 "tags": ["numbers"],
},
{
 "q": "How does the method perform on cold start, and why?",
 "a": """On cold-start users — those with at most five training interactions — NDCG@20 is 0.061 against 0.055 for
 HPCF, an improvement of about 10.9 %; for cold items it is 0.057 against 0.052, about 9.6 %. The mechanism is the
 one the architecture predicts: entities with little interaction history have weak individual evidence, so a model
 that propagates information over hyperedges and weights those relationships by their contribution to a
 multi-objective utility can draw more from structure and context than a model that relies mainly on the entity's
 own sparse history. The thesis states the appropriate caveat: this improves performance in precisely the regime
 where it is hardest, but it does not solve cold start. The figures are computed from the rounded table values;
 the source paper's prose computes the same gain from unrounded values as about 9.8 % for both cases, so I give
 the deck's numbers and note the derivation when asked.""",
 "tags": ["numbers", "danger"],
},
{
 "q": "Why does context matter most in the ablation?",
 "a": """Because context is doing structural work in this design, not decorating it. It appears in three places at
 once: as nodes in the hypergraph (so it participates in message passing), as one of the three terms of the
 coalition utility (ContextScore, weight γ = 0.15), and as an explicit loss term L_ctx that aligns the encoded
 contextual state with the learned context representation. Removing it therefore removes a source of information,
 a term of the training objective and a component of the attribution game at the same time — which is why the drop
 is the largest of the five: −8.2 % on MovieLens-1M and −11.0 % on Amazon-Book. The consequence, stated on the
 limitations slide, is a genuine dependency: on data without meaningful context, the gain of the method would
 shrink, and the thesis says so rather than presenting context as a free addition.""",
 "tags": ["danger"],
},
{
 "q": "What exactly is ContextScore, and is it not circular with the loss?",
 "a": """ContextScore(S) is the mean context-alignment score of the entities participating in the coalition: in the
 implementation, the average embedding-space alignment between a learned context representation and the context
 node representation associated with the interaction episode. It is measured in the same space used later by the
 scoring and regularisation terms. On circularity, the relationship is better described as *designed alignment*
 than as circularity. The loss contains L_ctx, which encourages the context encoder's output g(c) to agree with
 the context node e_c; ContextScore measures alignment in that same space. So the model is trained to make this
 quantity meaningful, and the coalition utility then uses it. This is deliberate: the thesis argues that the
 explanatory game and the predictive objective should be aligned by design, so that the explanation reports what
 the model actually optimises. The risk — and it is a real one — is that the term is easy for the model to
 optimise, so context can look important partly because it was trained to be important. The ablation's context row
 should be read with that in mind.""",
 "tags": ["danger"],
},
{
 "q": "How do you know the in-training signal is not just an extra regulariser?",
 "a": """Three arguments, in increasing strength. First, the ablation: removing the Shapley weighting specifically
 costs 4.6 % on MovieLens-1M and 6.1 % on Amazon-Book, while the attention stabiliser, which is purely a
 regularisation-like mechanism, costs only 3.5 % on both — so the two mechanisms behave differently in the
 measurements. Second, the weighting is directed: it is computed from a utility that encodes what a good
 recommendation is, so it modulates propagation according to the objective rather than uniformly shrinking or
 smoothing it. Third, the interpretation of the mechanism: the weights are Shapley values of a cooperative game,
 and the same estimand — average marginal contribution to a coalition's value — is what the explanation reports at
 inference time, so the training signal and the explanation are the same object measured at different moments.
 What I cannot claim from this thesis is a separate control experiment that isolates "coherent weighting" from
 "any non-uniform weighting"; that would require the random-weight control in the next question.""",
 "tags": ["danger"],
},
{
 "q": "Have you tried replacing the Shapley weights with random noise, or with a fixed pattern?",
 "a": """No, and I would be honest that this is the control experiment the design most obviously invites. The
 reported ablation compares full DyHuCoG with a variant that removes the Shapley weighting, which shows that the
 weighting contributes. What it does not show is whether the benefit comes from the *coherence* of the weights
 with the objective or merely from having a non-uniform, dynamically changing modulation of message passing. A
 random-weight variant with the same distributional properties — same clipping, same smoothing, same refresh
 schedule, but weights sampled independently of the game — would separate the two explanations, and a
 fixed-pattern control would rule out the trivial interpretation. The thesis does not report either, and the
 limitations slide does not claim them. I would put this at the top of the next-experiment list, alongside a
 factorial ablation, because it is cheap to run and it directly tests the causal story.""",
 "tags": ["danger"],
},
{
 "q": "Why is the method called “dynamic”? What changes during training?",
 "a": """The hyperedge weights change. In a standard hypergraph recommender, the weight matrix W is either fixed or
 learned monotonically with the rest of the parameters, so a relationship's importance is largely a property of
 the final fitted model. In DyHuCoG, the weights are recomputed periodically from the current state of training:
 every 10 batches, the model samples M = 50 permutations for the entities of the episode under consideration,
 estimates their marginal contributions to the coalition utility, then clips, exponentially smooths and
 normalises those estimates into the edge weights. The exponential moving average is what prevents the weights
 from jumping; the clipping prevents a single noisy episode from dominating. The consequence is that the same
 relationship can carry different weight early and late in training, which is the sense in which the model — and
 its explanation — is dynamic rather than static.""",
},
{
 "q": "Is λ_pref = 0.20 principled, or just tuned?",
 "a": """It is tuned, and the thesis is explicit about the tuning. The preference weight controls how much the
 additive preference term λ_pref·Σ sim(u,i) contributes to the coalition value, and λ_pref = 0.20 is reported as
 the setting that gives stable performance with variance below 1.5 % in NDCG@20; the coalition weights α, β, γ were
 selected by grid search over [0.1, 0.8] under the constraint that they sum to one, landing at 0.60 / 0.25 / 0.15
 on MovieLens-1M with similar behaviour on Amazon-Book. The thesis also states honestly that the full validation
 surface and the top-five configurations are not tabulated, so it reports the validated optimum rather than
 reconstructing unreported intermediate settings. The design rationale for the preference term is separable and
 interpretable: it lets entities carrying richer preference evidence contribute more, while keeping that
 contribution additive and distinct from the frequency-driven component of the utility.""",
 "tags": ["danger"],
},
{
 "q": "How were negatives sampled, and is that fair to the baselines?",
 "a": """Negatives are sampled with a popularity-aware distribution q(i) ∝ f_i^η, so that frequently interacted
 items are more likely to appear as negatives; this produces harder, more informative negatives than uniform
 sampling, which mostly yields items the user would never have seen. Crucially, the protocol is shared: the
 splitting rule, the leave-one-out target, the negative sampling distribution and the five seeds are the same for
 DyHuCoG and for every baseline, so the comparison is like-for-like on the data pipeline. What is not identical
 across models is the training objective — DyHuCoG optimises a composite loss with diversity and context terms,
 which is the contribution, not a protocol advantage. The fair statement is therefore: data, splits, evaluation
 and seeds are shared; the objective and the architecture differ, which is what is being tested.""",
 "tags": ["danger"],
},
{
 "q": "Could this scale to an industrial catalogue with hundreds of millions of items?",
 "a": """Not in its current form without substantial engineering, and the reasons are concrete rather than
 hypothetical. The coalition value is evaluated on the episode induced by a coalition, which involves ranking
 candidate items and computing NDCG@20, diversity and context alignment — cheap on a local episode of a few dozen
 entities, expensive if the candidate set must be drawn from a catalogue of hundreds of millions of items. The
 periodic refresh adds a bounded but real overhead, about 1.78× the training time of HPCF in this setting, and
 inference at 1.84 ms per query is real-time but was measured on a 3,706-item catalogue; the Amazon-Book setting
 already shows the direction of travel at 8.52 ms and 91,599 items. Scaling would need candidate generation with
 approximate nearest neighbours, negative sampling tailored to the new distribution, and probably a
 lower-variance estimator than permutation sampling. The perspectives slide names exactly this: scalable
 cooperative attribution with lower-variance estimators and adaptive refresh rules.""",
 "tags": ["danger"],
},
{
 "q": "What if context is not available at inference time?",
 "a": """Then the model degrades in a predictable way, because context is genuinely part of the design rather than
 an optional extra. It appears as nodes in the hypergraph, as a term of the coalition utility and as an explicit
 loss component; removing it from inference means the scored representation loses the component that the training
 aligned it with. The ablation quantifies the training-time effect — context removal costs 8.2 % on MovieLens-1M
 and 11.0 % on Amazon-Book — but the inference-time behaviour would depend on how the missing context is handled:
 substituting a default or the most common context is different from dropping the term, and the thesis does not
 report that experiment. The honest answer is that context availability is a stated dependency and a limitation:
 the sensitivity of the method to missing or noisy context is exactly the kind of robustness study that belongs in
 the future work, together with a fallback design in which the gate interpolates toward the context-free score.""",
 "tags": ["danger"],
},
{
 "q": "Is the explanation you get at inference the same object as the training signal?",
 "a": """They are the same *estimand* measured at different moments and on different supports. The estimand is the
 Shapley value of an entity in a cooperative game whose value function is the recommendation quality of a
 coalition. During training it is computed on the local episode under consideration, refreshed every ten batches,
 clipped and smoothed, and used to weight message passing. At inference, the explanation is presented as a
 decomposition — the waterfall read-out on the entity's contribution to the score — whose terms correspond to the
 same quantities the objective optimises: ranking, diversity, context and preference. So the claim is that the
 explanation is faithful by design because it reports what the model was trained on, not that the two computations
 are identical. The difference to state clearly is the support: the training-time estimate is local and periodic,
 while the explanation at inference is a per-instance read-out. That distinction is what the thesis means when it
 describes the estimator as an approximate in-training valuation procedure.""",
 "tags": ["danger"],
},
{
 "q": "How does the read-out relate to the objective? Could a user act on it?",
 "a": """The read-out shows the same terms the loss optimises — accuracy, diversity, context and preference — which
 is what makes it faithful by design: it is a direct expression of what the model was trained to balance. Whether a
 user can act on it is a different question, and the honest answer is that the thesis does not claim a user-facing
 explanation interface. For a designer or auditor, the read-out is actionable in the sense that it identifies
 which objective term dominated a particular decision, which supports debugging and monitoring. For an end user,
 "this recommendation is driven by context alignment" is not yet a natural-language justification, and turning
 Shapley read-outs into user-facing explanations is precisely the user-centred evaluation direction on the
 perspectives slide: do explanations measurably improve judgement, trust and perceived fairness? That study has
 not been run here.""",
 "tags": ["danger"],
},
{
 "q": "Does your evaluation protocol favour your model in any way a reviewer would catch?",
 "a": """Three things a reviewer should check, and I would rather name them than have them extracted. First,
 hyperparameter budgets: the baselines are used as published, while DyHuCoG's coalition weights and preference
 weight were tuned on validation performance; the tuning is reported, but the search surface is not tabulated, so
 the comparison is not perfectly symmetric in tuning effort. Second, the baselines were frozen in early 2026 and
 the set contains no post-2024 LLM-augmented recommender, so superiority is claimed only against the tested set —
 the thesis says this on the limitations slide. Third, the ablation is component-wise rather than factorial, so
 interactions are not characterised. On the other side, the protocol is shared, five seeds are used, the statistical
 treatment is conservative (Holm-Bonferroni on six comparisons), and the Amazon-Book results are explicitly labelled
 descriptive rather than significant. That combination is, I think, the right balance of ambition and restraint.""",
 "tags": ["danger"],
},
]},

# ============================================================ F. PROTOCOL / METRICS / STATS
{
 "title": "F · Protocol, metrics and statistics",
 "items": [
{
 "q": "Why these four datasets?",
 "a": """They are chosen in pairs, and each pair tests a different axis. Wine and Beijing test the clustering line
 on contrasting regimes: wine is small (4,898 samples), dense, chemically correlated and tabular, with variables a
 domain expert can read; Beijing is large (383,585 hourly records), noisy, seasonal and hierarchical in a way that
 makes a multi-level explanation meaningful. MovieLens-1M and Amazon-Book test the recommendation line on
 contrasting density: 0.0447 against 0.0006, a factor of about seventy-five, which is the core of the robustness
 argument. All four are public, standard benchmarks, so the results are comparable with prior work — MovieLens-1M
 in particular is the reference benchmark for LightGCN, HCCF and HPCF. The four together also support the thesis's
 cross-domain claim: the same pipeline returns a readable explanation in wine chemistry, air quality and
 recommendation.""",
},
{
 "q": "Why a 70 / 10 / 20 split with a leave-one-out target, rather than a simpler protocol?",
 "a": """Because the recommendation task is to rank what comes next, so the split must respect time and the
 evaluation must mimic a real request. The split is user-level and time-ordered: each user's interactions are
 divided 70 / 10 / 20 so that the test interactions are the most recent ones. The target is leave-one-out — the
 latest held-out positive per user — which is ranked against the remaining candidate items, so the evaluation asks
 the question a deployed system asks: given everything up to now, is the item the user actually chose near the top?
 The validation split is used for early stopping on NDCG@20 with patience 20, and the test split is touched once.
 This combination is standard in the modern implicit-feedback literature, which is what makes the numbers
 comparable with the baselines instead of bespoke.""",
},
{
 "q": "Why is NDCG@20 the main metric rather than Recall@20 or precision?",
 "a": """Because it is the only one of the three that measures both retrieval and ranking position. Recall@20
 rewards finding the relevant items somewhere in the top twenty, without caring where; with one held-out target it
 degenerates into a hit indicator, and Precision@20 is essentially determined by it. NDCG@20 weights each position
 by a logarithmic discount, so placing the relevant item first counts about four times more than placing it
 twentieth, which matches the user experience of a recommendation list. It is also the metric the coalition utility
 is built on — v(S) uses α·NDCG@20(S) — so the headline metric and the training signal are aligned by design,
 which is one of the small consistencies the thesis is careful about.""",
},
{
 "q": "The absolute NDCG values on Amazon-Book are tiny. Does that not invalidate the result?",
 "a": """No, but the numbers must be read correctly. Amazon-Book has 91,599 items and about three million implicit
 interactions, and the evaluation ranks a single held-out target against a very large candidate set, so an NDCG@20
 of 0.0306 corresponds to a genuinely hard retrieval problem. Absolute values in this range are normal in the
 sparse-recommendation literature and are not comparable across datasets with different catalogues, splits and
 negative samplers — which is why the thesis reports the comparison at equal difficulty rather than the absolute
 level. The claim is relational: 0.0306 against 0.0270 for HPCF, a relative gain of about 13.3 %, with the same
 ordering across all four metrics, and a larger relative gain than on the dense dataset. The honest qualifier is
 that this gain is descriptive, not statistically tabulated.""",
 "tags": ["numbers", "danger"],
},
{
 "q": "Why five seeds, and why report means rather than the best run?",
 "a": """Because recommender training is stochastic — initialisation, negative sampling and batch order all
 introduce randomness — so a single run can be lucky. Five seeds (42 to 46, fixed) give a mean and a standard
 deviation, which is the standard of evidence in the field and the basis of the ±1σ table on the backup slide.
 Reporting the best run instead of the mean would be a form of selection: it would hide variance and flatter every
 model, including the baselines, but it would make the comparison meaningless as an estimate of expected
 performance. The chosen protocol reports mean over seeds with standard deviations in the backup and the honest
 reading on the main slides: for MovieLens-1M the bands never overlap between DyHuCoG and HPCF, while on
 Amazon-Book they nearly touch for NDCG@20 and Recall@20 — which is exactly why those two gains are called
 descriptive.""",
},
{
 "q": "What does a ±1σ band show, and what does it not show?",
 "a": """It shows the spread of the metric across the five seeds: a band of one standard deviation around the mean.
 If two models' bands do not overlap, the difference is large relative to run-to-run variability, which is weak but
 real evidence of a difference. What it does not show is a significance test. Bands can overlap while a paired
 test is highly significant, because pairing removes between-user variance that the bands include; and bands can
 be narrow while the comparison is not meaningful, if the metrics are correlated across seeds. That is why the
 thesis reports both: the bands for stability, and the paired tests on per-user NDCG@20 for inference. The
 corrected wording on backup slide 77 is important here — the bands never overlap on MovieLens-1M, but on
 Amazon-Book the standard deviations are close to the gap for NDCG@20 and Recall@20.""",
 "tags": ["danger"],
},
{
 "q": "How exactly did you prevent data leakage?",
 "a": """Through three design choices. First, the recommendation split is user-level and time-ordered: each user's
 interactions are ordered in time and divided 70 / 10 / 20, so no future interaction enters training, and the
 leave-one-out target comes from the most recent portion. Second, everything that depends on data statistics —
 standardisation parameters, popularity distributions for negative sampling, surrogate training — is fitted on the
 training portion and applied unchanged to validation and test. Third, in the clustering pipeline the surrogate is
 evaluated with five-fold cross-validation on held-out cluster labels, so the fidelity figure is not a
 training-set score. The one thing to be precise about is that the clustering studies are unsupervised: there is no
 target label to leak, and the closest analogue to leakage is choosing k after seeing the explanation, which is why
 the criteria are stated in advance and the sensitivity is reported.""",
 "tags": ["danger"],
},
{
 "q": "What does the η in the negative sampling distribution do?",
 "a": """It controls how strongly the sampling distribution is tilted towards popular items: negatives are drawn
 with probability proportional to f_i^η, where f_i is the item's frequency. At η = 0 the distribution is uniform
 and most negatives are items a user would never plausibly consider, which makes training easy; as η grows, popular
 items are sampled more often as negatives, so the model is forced to separate a positive from plausible rather
 than absurd alternatives. The exact η used is part of the shared protocol configuration and applies identically
 to every model in the comparison, which is what matters for fairness. The methodological point to make in a viva
 is that with implicit feedback the negatives are constructed, so the choice of distribution is a design decision
 that affects difficulty for all models, not a neutral preprocessing step.""",
},
{
 "q": "Is a component-wise ablation enough to claim that every component matters?",
 "a": """It is enough to claim that each component contributes in this configuration, which is exactly what the
 slide claims, and not enough to claim more. Removing one component at a time shows that the model's performance
 depends on each of the five: context −8.2 % / −11.0 %, hypergraph structure −6.8 % / −8.9 %, diversity −5.8 % /
 −5.8 %, Shapley weighting −4.6 % / −6.1 %, attention −3.5 % / −3.5 %. What it does not show is interaction
 effects — for instance, whether the Shapley weighting still matters once the attention gate is removed, or whether
 context and diversity are partly redundant. A factorial or leave-two-out design would answer that, and the thesis
 lists "component-wise ablation only" as a limitation on the C3 limitations slide rather than pretending the
 evidence is stronger than it is.""",
 "tags": ["danger"],
},
{
 "q": "Why paired t-tests rather than just comparing the means?",
 "a": """Because the comparison is naturally paired: for every user, both models produce a score, so the unit of
 analysis is the per-user difference rather than two independent samples. Comparing means would treat the 6,040
 users as two unrelated groups and would have to absorb all the between-user variation — some users are simply much
 easier to predict than others — which would make the test far less sensitive and the conclusion less informative.
 The paired t-test computes t = mean(d) / (sd(d)/√n) on the differences with n = 6,040 and df = 6,039, testing
 whether the average user-level difference is distinguishable from zero. For the DyHuCoG versus HPCF comparison,
 t = 46.38 with p = 1.81×10⁻²⁷⁰ and dz = 1.33.""",
 "tags": ["numbers"],
},
{
 "q": "Why Holm-Bonferroni and not plain Bonferroni, or a false-discovery-rate procedure?",
 "a": """Because the family is small, six comparisons, and the goal is strict control of the probability of even
 one false positive. Plain Bonferroni would compare every p-value with 0.05/6 = 0.00833, which is unnecessarily
 conservative when the p-values are extremely small; Holm's procedure sorts them and compares the k-th smallest
 with α/(m − k + 1), so the most significant comparison gets the strictest threshold and the least significant
 gets the full 0.05, while still controlling the family-wise error rate. That is why the threshold column on
 backup slide 78 runs from 0.00833 to 0.0500: each p-value faces its own threshold, and all six are far below
 theirs. A false-discovery-rate procedure such as Benjamini-Hochberg would control an expected proportion rather
 than the probability of any error and would be more powerful, but with six comparisons and overwhelming evidence,
 the conservative choice costs nothing and is easier to defend.""",
 "tags": ["danger"],
},
{
 "q": "What does Cohen's dz = 1.33 mean in plain words?",
 "a": """It means that the average improvement for a user is about 1.33 standard deviations of the per-user
 differences. Since the conventional benchmarks are 0.2 for small, 0.5 for medium and 0.8 for large, 1.33 is a
 large effect — the gain is not just statistically detectable, it is substantial relative to how much users differ
 in how much they improve. This matters because with 6,040 users almost any difference becomes significant, so the
 p-value alone would be uninformative; the effect size is what says the improvement is worth having. The thesis
 reports dz ≥ 1.33 in all six comparisons, and 1.33 specifically against HPCF, the strongest baseline, which is the
 number to quote.""",
 "tags": ["numbers"],
},
{
 "q": "If the MovieLens tests are so overwhelming, why not claim significance on Amazon-Book too?",
 "a": """Because the analysis on Amazon-Book was not designed to support it, and the variance there does not allow
 the same conclusion. The paired tests are computed on per-user NDCG@20 for the 6,040 MovieLens users; on
 Amazon-Book there are 52,643 users but the signal per user is far weaker, the standard deviations are close to
 the gap between DyHuCoG and HPCF for NDCG@20 and Recall@20, and the thesis reports the comparison as descriptive
 over five seeds. Running the same test there would technically produce p-values, but the more honest position is
 to state what the evidence supports: a consistent ordering and a larger relative gain on the sparser dataset,
 with the caveat that it is not tabulated as significant. Claiming otherwise is the first of the three things I
 have been careful never to say, and it is worth remembering that over-claiming on a secondary dataset would
 jeopardise the credibility of the primary result.""",
 "tags": ["danger", "must know"],
},
{
 "q": "Are these improvements large enough to matter in a deployed system?",
 "a": """For ranking quality, a 9.8 % relative NDCG@20 gain over the strongest baseline would be considered
 substantial in a production recommender, and the joint improvement in coverage and diversity would matter to a
 platform worried about catalogue concentration. The qualification is the cost: training takes about 1.78× HPCF —
 roughly 2,000 s against 1,125 s on MovieLens-1M — and inference is 1.84 ms per query against 1.18 ms, which is
 still real-time but not free. So the realistic framing is a trade: better ranking and better catalogue coverage
 for a bounded increase in training cost and a modest inference cost. Whether that trade is worth it depends on
 the platform's constraints, and the thesis is careful to describe the overhead as "measurable, but modest" rather
 than as negligible. I would also note that all of this is offline evaluation; no online A/B test was run, and
 that is the evidence a platform would ultimately require.""",
 "tags": ["danger"],
},
{
 "q": "What about reproducibility — is the code available?",
 "a": """No, and this is one of the honest limitations of the work. The thesis appendix states that no public code
 URL is distributed and that raw per-seed logs are not released, so what a reader can reproduce is the method and
 the reported summary statistics rather than the exact runs. What is documented is substantial: the configuration
 is specified (100-tree, 31-leaf LightGBM surrogate; α = 0.60, β = 0.25, γ = 0.15; λ_pref = 0.20; M = 50; refresh
 every 10 batches; batch size 2048; seeds 42-46; early-stopping patience 20), the datasets are three public
 benchmarks plus a UCI repository dataset, and the tables report means and standard deviations over five seeds.
 The next step I would take is a released reference implementation with fixed seeds and per-seed logs, because
 that is what converts a documented result into an independently checkable one. I would not defend the absence of
 code as unimportant.""",
 "tags": ["danger"],
},
]},

# ============================================================ G. ETHICS / REGULATION / IMPACT
{
 "title": "G · Ethics, regulation, actionability and impact",
 "items": [
{
 "q": "Define actionability and give me one actionable result from the thesis.",
 "a": """Definition 1.1 says an explanation is actionable when it identifies a modifiable factor whose change is
 associated with a specifiable change in model output, expressed in the semantic vocabulary of the domain. The
 wine result is the cleanest example: the global ranking puts density, pH, fixed acidity, sulfur dioxide and
 alcohol at the top, and each of those is a quantity a wine maker controls directly — density through must
 composition and fermentation management, pH through acidification or blending, sulfur dioxide through
 preservation practice, alcohol through harvest timing and must adjustment. The explanation therefore names
 levers, not latent dimensions. What I must add, because the thesis says it explicitly, is that actionability is
 used as a framing concept in this work: it is illustrated by the nature of the variables and not measured with
 users, so the causal claim that changing pH changes the cluster membership in a specified way is a hypothesis
 that a domain study would need to test.""",
 "tags": ["must know"],
},
{
 "q": "Does your work satisfy the AI Act's explanation requirements?",
 "a": """No, and I would resist that claim. The thesis is positioned relative to the regulation rather than
 certified against it. Article 13 places transparency and information duties on providers of high-risk systems,
and Article 86 gives affected persons a route to request an explanation of an individual decision in certain
circumstances; the deck's wording is deliberately limited to "transparency duties" and "decisions can be
challenged" rather than the popular claim that explanations are mandated everywhere. What this work offers in that
direction is a technically grounded attribution method whose guarantees are explicit (efficiency, symmetry, null
player, additivity) and a demonstration that attribution can also shape training. What it does not offer is a
compliance analysis: that would require a specific system, a specific risk classification, a legal reading of the
applicable articles, and evidence about how explanations are delivered to and understood by affected people. The
honest sentence is that the thesis contributes a component of the technical basis, not a compliance argument.""",
 "tags": ["danger", "must know"],
},
{
 "q": "What about fairness and bias? Does your method address them?",
 "a": """Indirectly and honestly, not substantively. The Shapley axioms give two properties that matter for
 fairness of attribution: symmetry, so that equivalent players are treated equally, and null player, so that
 irrelevant ones are not credited. Those are fairness properties of the explanation, not of the outcomes. On
 recommendation fairness, the thesis touches the issue through popularity bias: the coverage and intra-list
 diversity results show that DyHuCoG's accuracy gain is not obtained by concentrating exposure on popular items —
 coverage rises from 0.342 to 0.397 and intra-list diversity from 0.461 to 0.516 on MovieLens-1M. But there is no
 group-fairness evaluation — no analysis by user demographics or by item category, no exposure-fairness metric, no
 audit of disparate impact — and the perspectives slide names broader trustworthy-AI evaluation, including exposure
 fairness and auditing, as future work. That is the accurate boundary of the claim.""",
 "tags": ["danger"],
},
{
 "q": "Could your explanations be misused — for gaming the system or for manipulating users?",
 "a": """Yes, and there are three distinct misuse paths worth naming. First, if a platform uses attribution to
 optimise engagement metrics, the same machinery that identifies which factors drive a recommendation could be
 used to amplify whichever behaviour is easiest to exploit — the method is objective-agnostic, and the objective
 was chosen here to balance accuracy, diversity and context. Second, exposing entity-level attributions about users
 could enable inference about individual behaviour, which is a privacy question, particularly where the
 explanations are shown or logged. Third, an explanation can create undue trust: a probabilistic attribution
 presented as a causal statement invites users to act on it as if it were a mechanism, which is precisely why the
 thesis insists that its attributions are decompositions of a surrogate's output rather than causal claims. The
 mitigations are in the design: the objective is explicit and multi-dimensional, the read-out is a decomposition
 rather than a narrative, and the limitations state what is not claimed.""",
 "tags": ["danger"],
},
{
 "q": "What are the privacy implications of computing Shapley values over users and items?",
 "a": """The cooperative game in Contribution III is defined over users, items and contexts, so the attributions
 are quantities attached to individuals and to their interactions. In this thesis they are used internally, as
 training signals for edge weights, and no explanation is shown to users or released; nothing in the reported
 experiments publishes per-user attributions. That said, the design would need care in deployment: entity-level
 attribution values are derived from interaction histories, so they inherit whatever sensitivity that data has,
 and aggregated statistics over small groups can still be identifying. The technical mitigations that would apply
 are the standard ones — differential privacy on the released quantities, aggregation before exposure, and access
 control — and the governance question is whether attributions count as derived personal data under the applicable
 regime, which is a legal determination rather than a technical one. The thesis does not address this, and I would
 flag it rather than dismiss it.""",
 "tags": ["danger"],
},
{
 "q": "Would a real user understand these explanations?",
 "a": """Not in their current form. The outputs are SHAP values in the units of a surrogate's log-odds, cluster
 profiles, and coalition attributions over objective terms; these are legible to an analyst or an auditor who knows
 the model, not to a lay user. Making them user-facing would require a translation layer — natural-language
 statements grounded in the domain vocabulary of Definition 1.1, evidence about comprehension, and a decision
 about what to show and when. That is a research problem in its own right, and it is exactly the third perspective
 on slide 71: do explanations measurably improve analyst judgement, user trust, quality of action or perceived
 fairness? The thesis is honest that it converts the technical output — an attribution with stated guarantees —
 and does not claim to have solved the human-facing problem.""",
 "tags": ["danger"],
},
{
 "q": "Is a Shapley value the truth about the model?",
 "a": """No, and it is important not to let the axiomatic language imply that. A Shapley value is the unique
 allocation of the model's output satisfying four stated properties under a stated value function; it is exact with
 respect to that game, not a causal statement about the world. Two consequences follow. First, with dependent
 features the value function itself embodies a choice — conditional versus interventional expectations — so the
 decomposition depends on how feature dependence is modelled. Second, in this thesis the attribution is computed
 on a surrogate and therefore describes a faithful reconstruction of the partition rather than the K-Means geometry
 itself. The right way to describe it is: a principled, axiomatically characterised decomposition of the model's
 behaviour, whose value derives from the guarantees it carries and from being reported with its scope, not from
 being metaphysically correct.""",
 "tags": ["danger"],
},
{
 "q": "What is the societal benefit that justifies the extra computation?",
 "a": """The benefit is not in the recommender's accuracy; it is in what the accuracy costs. Recommenders shape
 what billions of people see, and the thesis's motivation is that each step of architectural progress made ranking
 stronger and reasoning less inspectable, at the same time as the AI Act and the GDPR made transparency a
 governance expectation. If attribution can be made faithful (C1), consistent across levels of detail (C2) and
 part of how the model learns (C3), then systems that are more accurate need not be less accountable, and the
 explanation is a property of the model rather than a document written about it. Whether that justifies the cost —
 about 1.78× the training time and 4.4 GB instead of 4.1 GB in this study — is a deployment decision, and the
 thesis is careful to frame the overhead as bounded and measurable rather than negligible. It is also worth saying
 that no user study was run, so the human benefit is argued rather than demonstrated.""",
},
{
 "q": "How does the work relate to human-in-the-loop decision making?",
 "a": """It supplies the attribution layer that a human-in-the-loop process needs, and it stops short of supplying
 the interface and the study. A human in the loop needs three things from an explanation: a decomposition of the
 decision that accounts for the output (which efficiency provides), a statement about which factors are
 controllable (which Definition 1.1 requires), and enough stability that the same situation does not produce
 contradictory explanations (which the axioms and the fidelity floor support). What the thesis does not provide is
 the human side of the loop: no study of whether an analyst given these read-outs makes better or faster decisions,
 no measurement of trust or of perceived fairness, and no interface design. That is the user-centred evaluation
 direction on the perspectives slide, and the thesis presents it as an agenda rather than as an achievement.""",
 "tags": ["danger"],
},
]},

# ============================================================ H. LIMITATIONS / FUTURE
{
 "title": "H · Limitations, threats to validity and future work",
 "items": [
{
 "q": "What is the most serious limitation of the thesis?",
 "a": """That every explanation in it is an approximation of an approximation, and the thesis is honest that this
 is systematic rather than incidental. In the clustering contributions the attribution is exact for a surrogate
 whose fidelity to the partition is macro-F1 ≈ 0.82, so the explanation is one modelling step away from the object
 of interest; in the recommendation contribution the Shapley estimates are sampled (variance σ²/M), computed on a
 local episode, and refreshed periodically, so they are approximate in a second sense. The thesis names this in its
 own limitations: exact Shapley is not feasible, every contribution relies on approximation, surrogates or limited
 reporting. The mitigating design is that the approximation is quantified at each level — a fidelity floor, an MSE
 and accuracy curve against a high-sample reference — and reported with the claim, so a reader knows exactly how
 far the conclusion extends.""",
 "tags": ["must know"],
},
{
 "q": "What did you not do that a reviewer might demand?",
 "a": """Four things, and I would rather list them than have them extracted. A user study: actionability is defined
 and illustrated but not measured with people. A released implementation: no code URL and no per-seed logs, per the
 appendix. A factorial ablation: the component-wise design shows each component contributes but does not
 characterise interactions. And a fair-comparison audit of tuning effort: DyHuCoG's coalition weights were
 grid-searched while the baselines were used as published. To those I would add two that a recommender-systems
 reviewer would name — no post-2024 LLM-augmented baseline, since the set was frozen in early 2026, and no online
 or streaming evaluation, since preferences change over time while the partitions and the graph are static. Each
 of these is either in the thesis's own limitations section or in the perspectives agenda, which is the right place
 for them.""",
 "tags": ["danger"],
},
{
 "q": "What is the next experiment you would run, and why?",
 "a": """The random-weight control for the Shapley signal in DyHuCoG, because it tests the causal story directly and
 it is cheap. The current ablation removes the Shapley weighting and observes a 4.6 % / 6.1 % drop, which shows the
 weighting contributes, but it does not distinguish "weights coherent with the multi-objective utility" from "any
 non-uniform, dynamically refreshed modulation of message passing". A control that replaces the estimates with
 samples drawn from the same distribution — same clipping, same smoothing, same refresh schedule — would separate
 those two explanations. After that, I would run a factorial ablation to characterise interactions, and then a
 small expert study on the wine profiles, because the k = 3 decision on slide 32 is the weakest link in
 Contribution I and the one that a human study could actually settle.""",
 "tags": ["danger"],
},
{
 "q": "If you had ten times the compute, what would change?",
 "a": """Three things, in order of value. First, larger and more numerous Monte Carlo samples with adaptive
 refresh rules, which would reduce the estimator variance and let me test whether the in-training signal becomes
 stronger when it is less noisy — M = 100 already improves MSE to 3.5×10⁻⁶ at 2.5× the cost, so the question is
 whether the recommendation metrics eventually follow. Second, a genuine factorial ablation over the five
 components, which is computationally expensive because each cell requires a full training run on two datasets.
 Third, an online or streaming formulation with a time-evolving hypergraph, which is the perspective the thesis
 argues for on slide 71 and which needs infrastructure more than it needs raw compute. What I would not change is
 the evaluation protocol: more compute does not fix a protocol that is already shared, seeded and corrected for
 multiple comparisons.""",
},
{
 "q": "Where would this fail in deployment?",
 "a": """Four failure modes, each tied to a documented dependency. First, context: the largest ablation component is
 context, so a system without usable context would lose most of the gain, and missing context at inference is not
 studied. Second, cost: 1.78× the training time of HPCF and 1.84 ms per query on a 3,706-item catalogue, which is
 real-time but grows with the catalogue — Amazon-Book already shows 8.52 ms and 17.9 GB. Third, drift: the graph
 and the partitions are static, so a system whose user base or item catalogue changes rapidly would be explaining
 a stale structure, and the thesis does not model temporal drift. Fourth, explanation quality without
 maintainability: the attribution depends on the surrogate for the clustering line and on sampled estimates for
 the recommendation line, so a deployment would need fidelity monitoring and refresh diagnostics, which the
 thesis describes but does not operationalise.""",
 "tags": ["danger"],
},
{
 "q": "What do you want the jury to remember?",
 "a": """Three sentences. First: Shapley attribution is not only a post-hoc explanation method; it is a common
 cooperative-game language that can explain a black-box partition faithfully, stay consistent across levels of
 detail at scale, and then become an in-training signal that guides what a recommender learns. Second: the three
 contributions each remove a limitation the previous one leaves open — explain, scale, guide — and the evidence for
 each is reported with its scope stated, from the fidelity floor in the wine study to the descriptive status of
 Amazon-Book. Third: the honest boundary is that actionability is argued rather than measured, exact Shapley is
 never computed, and the code is not released — and I would rather the jury remember a thesis that knows its own
 limits than one that claims more than it shows.""",
 "tags": ["must know"],
},
]},
]
