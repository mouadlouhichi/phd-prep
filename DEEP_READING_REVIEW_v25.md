# Deep reading: all root documents + `try/MOUAD_LOUHICHI_VIVA_40min_BeigeGreen_v25.pptx`

Review date: 2026-10-04 · Reviewer: Arena agent · Method: full text extraction of every PDF
(PyMuPDF) and of every slide, table cell and speaker note of the deck (python-pptx), then a
claim-by-claim cross-check of the deck against the thesis and the three source papers, plus a
programmatic audit of the deck's typography, footers and speech timing.

> **STATUS: the fixes below are applied in `try/MOUAD_LOUHICHI_VIVA_40min_BeigeGreen_v26.pptx`
> (produced from v25 by `try/viva_builder/patch_v26.py`; the equivalent source edits are in
> `try/viva_builder/build_v26.py`, the delivered speech is `try/viva_builder/notes_v26.json`).**
> Every slide-text correction landed exactly once (the patcher asserts it), no text box grew a
> line, the layout, fonts, native OMML equations and the v25 footer/citation geometry are
> untouched, and the spoken total is now **4,692 words on 79 slides = 36.1 min at 130 wpm**
> (39.1 min at 120 wpm), with seven `Time check` cues restored. Details in section 9.
> One item could not be resolved from the documents alone and is flagged for you: **the jury
> list** (item 1 below).

Everything below is traceable: page numbers refer to `MOUAD_LOUHICHI_Thesis.pdf`, table and
figure numbers to the thesis and the three papers, line numbers to
`try/viva_builder/build_v25.py` (the script that produced v25).

---

## 0. Executive summary: six things to act on before the defence

| # | Severity | Item | Where |
|---|---|---|---|
| 1 | **Needs your confirmation** | The jury table on slides 1 and 76 carries the **same nine names as Redwane Nesmaoui's viva deck** (`example-phd-passes/Presentation1 (1) (1).pptx`). The build README documents that choice as deliberate ("real jury table (9 members, same jury as the reference deck)") — and a shared lab, supervisor and doctoral centre makes the same jury perfectly plausible. But it cannot be verified from the documents: your original 75-slide deck has `[President to complete]` / `[Reviewer to complete]` placeholders, and the thesis title page has **blank ruled lines** with a *Reporter ×3 / Examiner ×2* template (the deck shows *Reviewer ×3 / Examiner ×3*). Confirm against the official convocation. I kept the names and added a pre-defence check to the notes of slides 1 and 76 rather than replacing them with placeholders or inventing a list. | deck 1, 76; thesis p. i |
| 2 | **Blocking** | **Speaker notes are off by one slide in Contribution III**: slide 57 (Evaluation Protocol) is narrated with the MovieLens-1M *results*; slide 58 (Main Results ML-1M) is narrated with the *Amazon-Book* results; slide 59 repeats the Amazon text (90 % identical to slide 58). Root cause: notes are written by slide number at the end of the build (`build_v25.py:1791-1794`), and the JSON still follows an older 95-slide numbering. | notes 57, 58, 59 |
| 3 | **Blocking** | The same off-by-one hits the problem statement: slide 14 ("Three Main Limitations") is narrated with the **five research questions** (the text that belongs to slide 15), and slides 15/16 carry near-identical contribution summaries (85 % overlap). Slide 53 reads its own three objectives twice. Slides 20 and 21 have **identical** notes. | notes 14, 15, 16, 20, 21, 53 |
| 4 | **Content error** | Slide 19 lists the Beijing weather variables as "temperature, pressure, dew point, **rain**, wind speed". The thesis (p. 43) and the IJACSA paper (Table III) list **wind direction**, not rain. | build_v25.py:656 |
| 5 | **Content error** | Slide 55's Monte-Carlo table says M = 25 gives **96 %** accuracy. The paper's Table 7 and the thesis Table 7.4 say **98 %** (and the deck's own backup slide 79 says 98 %). Slide 53/63 also call the third utility term "novelty"; it is **ContextScore** in the paper (Eq. 1) and in the thesis (Eq. 7.1). | build_v25.py:1293, 1219, 1495 |
| 6 | **Overstatement** | Three claims are wider than the thesis: (a) slide 57 requires `p < 0.05 after correction` **on both datasets** while the thesis tabulates paired tests for MovieLens-1M only and calls Amazon-Book "descriptive"; (b) slide 34 marks the SHAP-over-LIME objective "Met" with "higher stability" as evidence, while Chapter 5 says the LIME comparison is **theoretical, not a full empirical bake-off**; (c) backup slide 77 says the standard deviations are "roughly one tenth of the gap ... on **every** metric", which is false on Amazon-Book (SD/gap = 0.81 for NDCG@20 and 0.67 for Recall@20, with ±1σ bands overlapping). | build_v25.py:1342, 961, 1726 |

Nothing else in the deck contradicts the thesis. Every headline number I checked (main results,
ablation, runtime, Monte-Carlo, significance, cold start, dataset statistics, k-selection,
hardware) matches the thesis and the source publications. Section 5 gives the full verification
ledger.

---

## 9. What v26 changes, exactly

Produced by `try/viva_builder/patch_v26.py` from the v25 file (never a rebuild: the template
fonts and figure crops are outside the repository, so patching in place is both possible and the
safest way to preserve layout, fonts, equations and the footer/citation fix). The script asserts
that every target string matches exactly once; all 17 text edits and the two table rewrites
matched.

**Slide text (verified in the delivered file)**

| Slide | Before | After |
|---|---|---|
| 4 | "market > $15B by 2029" | "…decisions in systems used at global scale" |
| 4 | "EU AI Act: high-risk → must explain." | "EU AI Act: high-risk → transparency duties." |
| 6 | "high-risk systems must provide explanations **in human-understandable terms**" | "high-risk systems must be transparent (**Art. 13**) and decisions can be challenged (Art. 86)" |
| 19 | "weather (…, dew point, **rain**, wind speed)" | "…, dew point, **wind direction**, wind speed" |
| 19 | "Selected clusters: k = 3 → **9 sub-clusters**" | "k = 3 coarse regimes" |
| 20 | "(GroupLens, **2000**)" | "(GroupLens benchmark)" |
| 31 | "LIME-based surrogate explanation on the same partition" | "LIME surrogate, as the theoretical comparator (Ch. 5)" |
| 34 | O3 evidence "Four axioms; **higher stability** and cross-cluster comparability" | "Four axioms; LIME comparator theoretical (Ch. 5, §5.4)" |
| 42 | KPI "**3 → 9**" | "k = 3" (label unchanged) |
| 43 | "…sub-clusters **(3 → 9)**" | "…sub-clusters" |
| 46 | caption "SHAP importance **per sub-cluster, level 2 of the hierarchy**" | "cluster-specific SHAP importance, coarse level" |
| 53 | "…accuracy, diversity and **novelty**" | "…accuracy, diversity and **context**" |
| 55 | "≈ **96** %" (M = 25) | "≈ **98** %"; caption now says accuracy is measured against a high-sample reference |
| 57 | "…with **p < 0.05** after correction" | "…; significance tabulated on MovieLens-1M (Table 7.6)" |
| 63 | "γ·**novelty**" | "γ·**context**" |
| 74 | ref [19] "**Dua & Taniskidou** … Beijing Multi-Site Air Quality Data" | "**Zhang, S. et al.** … Data Set" |
| 74 | ref [28] "IJIES 18, 241–257" | "IJIES **18(9)**, 241–257" |
| 77 | "**one tenth of the gap** … on **every** metric" | "**±1σ bands** never overlap … on MovieLens-1M; on Amazon-Book the standard deviations are close to the gap for NDCG@20 and Recall@20, so those gains are reported as descriptive" |

**Speaker notes** (`notes_v26.json`, 46 slides rewritten)

* Contribution III realigned: 57 = protocol, 58 = MovieLens-1M results, 59 = Amazon-Book.
* Slide 14 now carries the three limitations (it was narrated with the RQs); 15 and 16 are
  distinct (RQ map vs contribution cards); 20 and 21 no longer share one note.
* Slide 53 states its three objectives once; 55 and 64 carry the honest scope (high-sample
  reference for accuracy; paired tests tabulated on MovieLens-1M, Amazon-Book descriptive).
* Slides 67/68/71/72 became four distinct closing beats; 73/74 differentiated; 75/76 differentiated.
* Seven `Time check` cues restored (slides 3, 8, 17, 26, 38, 51, 67), calibrated to 130 wpm:
  minute one / five / ten / fourteen / twenty / twenty-six / thirty-four.
* Redundancy pass on 17 more notes that were restating their own slides (13, 24, 28, 30, 33, 34,
  37, 39–43, 46, 49, 52, 54, 60, 63) — this is what brings the total down from the 4,912 of v25
  instead of the 5,121 that the pure realignment produced.
* Slide 2 now says **"the next 36 minutes"**, matching the measured 4,692 words.
* Slides 1 and 76 carry a bracketed *(Pre-defence check: confirm the jury list on this slide
  against the official convocation.)* — the one item that needs your input.
* Slide 29's note now states the value the table omits: **Guitar + Drums = 100**, which is what
  makes the 90 / 70 / 40 average work out (the table has no room for a seventh coalition row:
  it would collide with the footer band).

### v27 addendum: the candidate's own opening speech

The opening and the plan (slides 1 and 2) are now the speech Mouad Louhichi delivered, verbatim
except that the spoken thesis title spells out "artificial intelligence" (the slide title keeps
the registered wording, "Explainable AI"). Slide 4 carries a short spoken note that follows its
three motivation cards, and slide 6 is now internally consistent: the note and the two blocks
("Why the gap matters", "What this thesis argues") say the same three things, in three short
bullets each, so nothing on screen is left unsaid and nothing said is missing from the screen.
The last "Pre-defence check" line on notes 1 and 76 still stands until the jury list is confirmed.
Speech total: 4,594 words on slides 1-76 = 35.3 min at 130 wpm.

### v28 addendum: the title in full, and the slide 6 speech in spoken register

The title block of slides 1 and 76 now reads "Cooperative Game Theory for Explainable /
Artificial Intelligence in Recommendation Systems", still at 50 pt: with the metrics of the
embedded Roca Two Bold the long line measures 1054.9 pt against a 1281.6 pt box (82 %), so
nothing wraps and the subtitle below is untouched. The running footer on the other 77 slides
keeps the acronym; measured, the full form fits there too (88-92 % of the footer box) if it
should be rolled out. The speech on slide 6 is now spoken register ("Let me put this in
context", "Why does this matter?", "So what does this thesis argue?") and still says the same
three things as the two cards. Speech total 4,641 words = 35.7 min at 130 wpm.

### v29 addendum: the citation bands, in full and visible

Every slide that cites work now prints the complete reference in its band (the text of slides 73-74,
verbatim), at 14 pt, over one to three lines, split into a maximum of three so that no band eats the
slide. On the two dense slides (23, seven references; 52, five) the title of the cited paper is
dropped to keep it to three lines, authors, venue, volume, pages and year staying in.

Visibility was the other half of the problem, and it was real: the bands sat at z-order four of
thirty-odd, and on twelve slides a card or note bar ended at y = 10.28 over a band that ended at
10.50. The bands are now drawn last and the content was lifted group by group, only as far as the
shape above it allows (49 slides, 94 shapes, 3 card panels gave up padding, no new overlaps were
created). Text height is measured with the embedded Nunito Semi-Bold, so the line counts are real.

### v30 addendum: slide 6 trimmed to two blocks

At the candidate's request slide 6 now carries the evolution timeline and one card only: "Why the gap
matters". The one-line conclusion above the cards ("The interpretability gap grows: ...") and the card
"What this thesis argues" were deleted, and the surviving card became a full-width panel (y 6.38-9.74,
which keeps it clear of the three-line citation band below) with its three points in three columns at
22 pt. The speech for the slide loses its closing paragraph, the one about the removed card.

### v31 addendum: slide 4 speech shortened

The note on slide 4 is now eighty words: the three motivation questions the slide asks, then the
tension the banner states. Nothing else changed anywhere else in the deck.

### v32 addendum: slide 4 turned into description

The three cards on slide 4 stated questions; they now state what the talk is about: recommenders decide at
scale, the reasoning behind those decisions is hidden, and transparency is now expected. The headline changed
with them ("Motivation: Why Explainability Matters") and the speech was replaced so that each column is said
once, in 85 words.

### v33 addendum: slide 16 speech

Slide 16 (the three contribution cards) now carries the candidate's own spoken text: the research questions
lead to three concrete contributions, presented in order; the first introduces the Shapley framework for
black-box clustering on Wine Quality, the second extends it to large-scale multi-level clustering on Beijing
Air Quality with the cross-level consistency guarantee, the third is DyHuCoG, which brings attribution inside
the recommendation model on MovieLens-1M and Amazon-Book. It closes on the sentence the candidate wrote:
"from explanation, to scalability, and finally to action."

### v34 addendum: slide 10 figure made accurate

The slide 10 picture was a decorative bipartite sketch: users and items joined by curves, a dashed
"predicted" edge, and two similarity chips (u1~u2 0.87, u1~u4 0.21) derived from nothing on the slide.
v34 replaces it with a figure in which every number follows from what is printed (fig_slide10.py asserts
this at run time): a 4 x 5 user-item rating matrix with 16 of 20 cells observed; Pearson similarity of u2,
u3, u4 with u1 computed on the columns both rated (i1, i2, i4), giving 0.87, 0.50 and 0.00; the missing
cell r(u1, i3) filled by the similarity-weighted average over the neighbours who rated i3, (0.87×5 +
0.50×3) / (0.87 + 0.50) = 5.85 / 1.37 = 4.3 out of 5; and a strip recalling the sparsity of the real
matrices, MovieLens-1M 4.47% of cells observed (6,040 users, 3,706 items) and Amazon-Book 0.06%
(52,643 users, 91,599 items), which is what makes cold start hard. The figure is drawn at 300 dpi in the
deck palette with the deck's own Nunito (operators the embedded subset lacks are drawn as vectors), and
no label is set below 14 pt at slide scale. Note 10 gains the paragraph that walks the jury through it.

### v35 addendum: slide 12 figure made accurate

The slide 12 picture drew the pairwise graph as a near-complete graph over users, items and context
(clock-tag, pin-tag, clock-pin edges that no recommender graph contains), and its hypergraph blobs
grouped nodes arbitrarily with no tie to message passing or to DyHuCoG. v35 replaces it with a figure
that shows exactly what the slide text claims (fig_slide12.py): left, the bipartite user-item graph of
LightGCN / HCCF / HPCF, whose five edges are the observed interactions only, with the 2-hop message
u2 - i2 - u1 drawn as a directed teal path and every edge carrying the same weight (the limitation named
on the slide); right, the same six nodes plus a context node c1, with hyperedge e1 joining u1, u2, i2 and
c1 (a user, an item and a context at once, as the speech says) and hyperedge e2 joining u2, u3, i3, the
pairwise edges kept underneath and the caption stating that hyperedge weights are re-learned at every
step t, which is DyHuCoG's dynamic part. The bottom tag keeps the old line in spirit: one hyperedge joins
many nodes. Same palette, Nunito and 300 dpi as the v34 figure, placed at the old geometry (8.75 x 4.88 in,
1:1 pixels), no label below 14 pt. Note 12 gains the paragraph that walks the jury through it.

### v36 addendum: slides 13 and 14 merged

Slide 13 (four classical limits plus a clustering panel) and slide 14 (three structural limits plus the
thesis gap) told one story in two passes, repeating the interpretability and scaling arguments. v36 keeps
slide 13 as the single problem-statement slide, headed "Limitations & Problem Statement", and lays the
content in three rows: the four classical limits in the original blue cards (04 still teal, the limit the
thesis targets); the three structural limits in slide 14's gold-oval card style; and the THESIS GAP bar with
slide 14's gap sentence verbatim, including the claim that Shapley-value attribution can be that framework.
The clustering panel's distinct point (local or global, not both; consistency across levels) survives inside
the gap sentence and the merged note. The band is the union of both bands, [21], [23] with its two works and
[24], still in the v29 full form because it wraps on exactly three lines. Slide 14 is deleted, every later
page number decrements, the deck is 78 slides (spoken 1-75, backup 76-78), and the two notes merge into one
103-word note that repeats nothing. Spoken total 4,627 words = 35.6 min at 130 wpm.

**Not done, on purpose**

* No new backup slides. The three candidates I suggested (Proposition 6.1 + proof sketch, Table 7.5
  cold-start/Yelp2018, a scope slide) would require laying out new slides with the template's
  embedded fonts and figure assets, which are not in the repository; that is a rebuild, not a patch.
* The jury names were kept, not replaced (see item 1).
* Nothing was deleted: the two claims that were narrowed (slide 57, slide 77) keep their substance
  and now say exactly what the thesis says.

---

## 1. Inventory of what was read

| File | Pages / words | What it is |
|---|---|---|
| `MOUAD_LOUHICHI_Thesis.pdf` | 159 pp · 46,060 words · 19 figures · 20 tables · 110 references | The monograph: 9 chapters, 6 appendices (proofs, pseudocode, dataset appendix, extended results, reproducibility, statistics). Chapters 5–7 are the three contributions; the three papers are declared the "primary source of truth" for them. |
| `MOUAD_LOUHICHI_Thesis_Resume.pdf` | 3 pp · 822 words (FR) | French thesis summary: general abstract, three structural limits, three contributions, the three publications with DOIs, conclusion (AI Act framing). |
| `Shapley Values for Explaining the Black Box Nature of Machine Learning Model Clustering.pdf` | 6 pp (Procedia CS 220, 806–811, 2023) | Contribution I source paper (C1). PCA + K-Means + LightGBM + SHAP on white "Vinho Verde" wine; no numeric Silhouette/DB values in the paper itself; no LIME experiment. |
| `Game Theory Meets Explainable AI ... Shapley Values.pdf` | 10 pp (IJACSA 16(7), 716–725, 2025) | Contribution II source paper (C2). This is where the **wine k-selection table lives** (Table VI: k=2 → 0.214 / 1.775; k=3 → 0.144 / 2.097), together with the Beijing values (k=2 → 0.265 / 1.503; k=3 → 0.626 / 0.553) and the LightGBM fidelity result (31 leaves → macro-F1 0.82; 63 leaves → 0.84 for +4 min). |
| `DyHuCoG ... Preference-aware Recommendation.pdf` | 16 pp (IJIES 19(2), 887–902, 2026; DOI 10.22266/ijies2026.0228.54) | Contribution III source paper (C3): coalition utility Eq. (1) with **ContextScore**, preference term Eq. (2), exact and Monte-Carlo Shapley Eqs. (3)–(5), weights α=0.60 β=0.25 γ=0.15 λpref=0.20 (variance < 1.5 % in NDCG@20), main results, ablation, Table 7 (Monte-Carlo: 95 / 98 / 99 / 99.5 %), Table 8 (cold start +10.9 % / +9.6 %), Table 9 (paired tests). |
| `try/MOUAD_LOUHICHI_VIVA_40min (6).pptx` + `... .pptx (1).pdf` | 75 slides | The original (pre-Beige Green) viva deck. Same section logic; the Beige Green line is a re-layout of it. Its title used "Cooperative Game Theory & Shapley for XAI in Recommendation Systems"; the thesis title is the longer form used on v25's title slide. |
| `try/MOUAD_LOUHICHI_VIVA_40min_BeigeGreen*.pptx` | 22 files, v0 → v25 | The version history. v25 is the current deliverable: 79 slides, 4,912 notes words. |
| `try/speech_enhanced.json`, `speech_enhanced.fixed.json` · `try/viva_builder/*.py`, `*.json`, `*.md` | 15 MB | The build system: `tpl.py` (design system), `layouts.py`, `mathkit.py` (native OMML equations), `build_vNN.py` per version, `notes_vNN.json` per version, `README.md` (version log), `REDUNDANCY_ANALYSIS.md` (why 95 → 79 slides). |
| `example-phd-passes/` (Nesmaoui deck, thesis, viva PDF, résumé) | 80 slides + PDFs | The reference viva the deck's structure was modelled on, **including its jury table**, which is the source of finding #1. |

---

## 2. Deep reading of the thesis: the claim, the three contributions, and the exact scope

**Thesis claim.** Shapley attribution is not only a post-hoc explanation method: it is a common
cooperative-game language that (i) explains a black-box partition, (ii) stays consistent across
levels of detail at scale, and (iii) becomes an in-training signal in a recommender (Ch. 1, 8, 9).

**Definition 1.1 (p. 2).** An explanation is *actionable* when it identifies at least one
**modifiable** factor whose change is associated with a specifiable change in model output, and the
factor is expressed in the semantic vocabulary of the task domain (acidity in wine, pollution
indicators in air, preference signals in recommendation). Actionability is a framing concept, not
a measured endpoint: the thesis says so explicitly, and reports no user study.

**C1 (Ch. 5, pp. 55–67).** Players = the 11 features; value function = Silhouette of the K-Means
solution on the feature subset; but the **operational** attribution is TreeSHAP on a LightGBM
multiclass surrogate trained on the K-Means labels in the original feature space. Three scope
statements that matter for the viva:

* "the chapter does not claim to explain K-Means geometry in a mechanistic sense; it explains a
  faithful supervised reconstruction of the discovered partition" (p. 58), and efficiency holds
  "with respect to the LightGBM surrogate's log-odds output ... rather than with respect to the
  Silhouette-based cooperative-game value directly" (p. 62).
* The SHAP-vs-LIME comparison is "theoretical and literature-backed rather than a fully rerun
  empirical benchmark on the wine data" (p. 65) and "not a full empirical bake-off" (p. 66).
* No wine-specific surrogate-F1 table exists in the source paper; the macro-F1 ≈ 0.82 figure is
  the default 100-tree / 31-leaf surrogate of Chapter 6, reported for both wine and Beijing
  (p. 70). The practical floor is stated as "roughly 0.80" (p. 62).

Wine numbers used by the deck, verified: k=2 → Silhouette 0.214, DB 1.775; k=3 → 0.144 / 2.097;
k*=3 chosen on interpretability grounds, and the 0.63 Silhouette belongs to **Beijing**, not to the
wine partition (stated twice, pp. 59, 63, 66, precisely because a reader may confuse them).

**C2 (Ch. 6, pp. 68–79).** Recursive clustering: coarse partition on the full data, then each
coarse cluster subdivided "where appropriate"; one surrogate per level; SHAP always in the same
11 original variables; cross-level aggregation weighted by child size. **Proposition 6.1**:
parent-level expected absolute importance = size-weighted expectation over children + residual εj,
derived from the law of total expectation for a strict nested hierarchy; εj "is treated as a
conceptual residual term rather than as an empirically estimated quantity, because a separate
Beijing-level residual analysis is not reported" (p. 71). Beijing validation: ~383,585 hourly
records, 11 variables (PM2.5, PM10, NO2, SO2, CO, O3, temperature, pressure, dew point, **wind
direction**, wind speed), 2013–2017, k=3, Silhouette ≈ 0.63, DB ≈ 0.55, three physically readable
regimes (warm photochemical / winter smog / cleaner air), comparison point Gramegna & Giudici
Silhouette 0.37.

**C3 (Ch. 7, pp. 81–99).** DyHuCoG: players N = U ∪ I ∪ C; v(S) = α·NDCG@20(S) +
β·Diversity(S) + γ·**ContextScore**(S); v_pref(S) = v(S) + λ_pref·Σ sim(u,i); α=0.60, β=0.25,
γ=0.15, λ_pref=0.20; Monte-Carlo Shapley with M=50 refreshed every 10 batches (~49 updates/epoch,
batch 2048) and EMA-smoothed, clipped, normalised into hyperedge weights; attention gate;
context-aware score; loss = BPR + diversity + context + L2. Results (ML-1M): NDCG@20 0.2775 vs
HPCF 0.2528 (+9.77 %), Recall 0.2362 vs 0.2098 (+12.58 %), Coverage 0.397 vs 0.342 (+16.1 %),
ILD 0.516 vs 0.461 (+11.9 %); Amazon-Book: 0.0306 vs 0.0270 (+13.33 %), 0.0417 vs 0.0359
(+16.16 %), Coverage 0.336 vs 0.259 (+29.7 %), ILD 0.602 vs 0.535 (+12.5 %). Ablation (thesis
Table 7.2): context −8.2 %/−11.0 %, hypergraph −6.8 %/−8.9 %, Shapley −4.6 %/−6.1 %, diversity
−5.8 %/−5.8 %, attention −3.5 %/−3.5 %. Efficiency: 2000.2 s vs 1124.6 s (1.78×), 1.84 ms vs
1.18 ms inference, 4.4 vs 4.1 GB. Significance (Table 7.6, ML-1M per-user NDCG@20, df=6039):
vs HPCF t=46.38, p=1.81e−270, dz=1.3345, Holm α=0.05; all six comparisons significant; Wilcoxon
p<0.001. Cold start (Table 7.5): user 0.061 (HPCF 0.055), item 0.057 (0.052), i.e. +10.9 % /
+9.6 % on the rounded figures; the paper's prose computes the same gain from unrounded values as
+9.8 % for both. Yelp2018 is an auxiliary robustness benchmark only.

**Three scope fences in Ch. 7 that the deck should honour**: (i) "the strongest fully tabulated
paired tests ... apply to per-user NDCG@20 on MovieLens-1M, while Amazon-Book and the auxiliary
metrics remain descriptive" (p. 91); (ii) the ablation is component-wise only, no factorial
interaction design; (iii) baselines were frozen in early 2026, no post-2024 LLM-augmented
recommenders, so superiority is claimed only against the tested set. Appendix D adds that no raw
per-seed logs or public code URL are distributed.

---

## 3. The deck as delivered (v25), mapped

79 slides at 20 × 11.25 in. Main flow 1–76, backup 77–79. Section tracker 1…7 in the header,
ENSIAS footer, numbered citation band above the footer on 42 slides.

| Block | Slides | Slides | Words | min @140 | min @130 | min @120 |
|---|---|---:|---:|---:|---:|---:|
| Title + outline | 1–2 | 2 | 195 | 1.4 | 1.5 | 1.6 |
| 1 Introduction | 3–7 | 5 | 406 | 2.9 | 3.1 | 3.4 |
| 2 Context & Problematic | 8–16 | 9 | 663 | 4.7 | 5.1 | 5.5 |
| 3 Experimental Protocol | 17–25 | 9 | 553 | 4.0 | 4.3 | 4.6 |
| 4 Contribution I | 26–37 | 12 | 802 | 5.7 | 6.2 | 6.7 |
| 5 Contribution II | 38–50 | 13 | 707 | 5.0 | 5.4 | 5.9 |
| 6 Contribution III | 51–66 | 16 | 1023 | 7.3 | 7.9 | 8.5 |
| 7 Conclusion & Perspectives | 67–76 | 10 | 518 | 3.7 | 4.0 | 4.3 |
| **Main flow** | **1–76** | **76** | **4,867** | **34.8** | **37.4** | **40.6** |
| Backup (Tables 7.1, 7.6, 7.3+7.4) | 77–79 | 3 | 45 | not spoken | | |

Spine per contribution is identical and matches the reference deck: Research Gap → RQ and
Objectives → method (2–4 slides) → Evaluation Protocol → Results (2–5) → Answer to RQ →
Key Findings → Limitations → Takeaway. C1 has the extra cooperative-game/shapley-value
methodology slides (29, 30) replacing the old three "technical deep dive" slides, and C1's
"Choosing k" slide (32) is the one result slide that is pure thesis framing.

**Vertical checks (all pass).** Footer text present on 77/79 slides (absent only on the two title
slides, by design). No text run anywhere below 14 pt; 25 native OMML equation blocks, none with a
run below 16 pt; every citation band sits above the footer (0 violations). The v25 changelog
claims are true as built.

---

## 4. Claim-by-claim verification ledger

### 4.1 Verified against the thesis and the source papers (no action)

| Deck claim | Source |
|---|---|
| Wine: 4,898 × 11, k*=3, k=2 geo better (0.214 / 1.775 vs 0.144 / 2.097) | thesis pp. 59, 63; IJACSA Table VI |
| Global wine ranking density > pH > fixed acidity > SO2 > alcohol | thesis p. 63; Procedia Fig. 1 |
| Beijing: 383,585 records, 11 variables, k=3, Silhouette 0.63, DB 0.55, regimes A/B/C | thesis pp. 72–74; IJACSA §IV.E, Figs. 6–8 |
| Gramegna & Giudici comparison 0.37 | thesis p. 76 |
| ML-1M 6,040 / 3,706 / 1,000,209 / 0.0447; Amazon 52,643 / 91,599 / 2,984,108 / 0.0006 | thesis Table 4.1; Ch. 4 |
| Splits (70/10/20, LOO, ratings > 3, seeds 42–46, patience 20) | thesis §4.2, §4.5.6 |
| Surrogate fidelity 0.82 (100 trees / 31 leaves) | thesis p. 70; IJACSA Table VI |
| All main results, both datasets, all four metrics, all percentages | thesis Table 7.1 (identical to IJIES) |
| Ablation drops (context largest, Shapley −4.6/−6.1) | thesis Table 7.2 |
| Runtime 1.78× (2000 vs 1125 s), 1.84 ms, 4.4 GB, ×3.41 MF | thesis Table 7.3 |
| Monte Carlo M=50 MSE 1.4e−5, 99 %, refresh 10 batches, 49 updates/epoch | thesis Table 7.4, §7.4.4 |
| α/β/γ = 0.60/0.25/0.15, λ_pref = 0.20, < 1.5 % variance | thesis §7.3.3; IJIES §3.3 |
| t = 46.38, dz = 1.33, p = 1.81e−270, Holm thresholds, df = 6039 | thesis Table 7.6; IJIES Table 9 |
| Cold start +10.9 % / +9.6 % | thesis Table 7.5; IJIES Table 8 |
| Publications I/II/III, journals, volumes, pages, DOIs, first author | thesis p. xxii; the three PDFs |
| Hardware i9-14900K / RTX 4090 24 GB / 48 GB / 2 TB / Python 3.8 / PyTorch 2.0.1 | thesis Table 4.2 |

### 4.2 Errors to fix

| # | Slide(s) | Now | Should be | Evidence |
|---|---|---|---|---|
| E1 | 19 | weather "(temperature, pressure, dew point, **rain**, wind speed)" | "(temperature, pressure, dew point, **wind direction**, wind speed)" | thesis p. 43; IJACSA Table III |
| E2 | 55 | table "25 · ≈ 96 %" | "25 · ≈ 98 %" (and header "Accuracy" → "Accuracy vs. reference") | IJIES Table 7; thesis Table 7.4 |
| E3 | 53, 63 | "coalition utility mixes accuracy, diversity and **novelty**"; "α·accuracy + β·diversity + γ·**novelty**" | "…and **context**"; "γ·**context**" | IJIES Eq. (1); thesis Eq. (7.1) |
| E4 | 19, 42, 43 | "k = 3 → **9 sub-clusters**"; KPI "**3 → 9**"; "Each coarse cluster split again into sub-clusters (**3 → 9**)" | no number: "coarse regimes → level-2 sub-clusters" | thesis §6.2 ("subdivided where appropriate"); neither source gives a count of sub-clusters anywhere. The "9" most plausibly comes from a misreading of IJACSA Table VI's "9 PCs ≈ 97 % var." (PCA components, not clusters) |
| E5 | 46 | caption "Fig. 6.3 (thesis): SHAP importance **per sub-cluster, level 2 of the hierarchy**" | "cluster-specific SHAP importance (coarse level)" | thesis Fig. 6.3 shows panels per cluster 0/1/2, not level-2 sub-clusters |

### 4.3 Claims wider than the thesis (reword, do not delete the substance)

| # | Slide(s) | Now | Problem | Suggested wording |
|---|---|---|---|---|
| O1 | 57 | success criterion "Beat HPCF **on both datasets** in NDCG@20 and Recall@20, **with p < 0.05 after correction**" | the thesis tabulates paired tests for ML-1M only and calls Amazon-Book evidence "descriptive" | "Beat HPCF on both datasets in NDCG@20 and Recall@20; significance established on MovieLens-1M (Table 7.6), Amazon-Book reported as a descriptive gain" |
| O2 | 31, 34 | protocol row "Comparison: LIME-based surrogate explanation on the same partition"; O3 "Met \| Four axioms; **higher stability** and cross-cluster comparability" | Chapter 5 states the LIME comparison is theoretical and literature-backed, not a rerun bake-off | protocol: "Comparison: LIME surrogate pipeline as the theoretical / literature comparator"; O3 evidence: "Four axioms (Ch. 5, §5.4); LIME comparator discussed in Ch. 5–6" |
| O3 | 77 | "Standard deviations are roughly **one tenth of the gap** between DyHuCoG and HPCF **on every metric**, so the ordering is stable across seeds" | false on Amazon-Book; ±1σ bands overlap there | "On MovieLens-1M the ±1σ bands of DyHuCoG and HPCF do not overlap on any metric; on Amazon-Book the SDs are comparable to the gap on NDCG@20 and Recall@20, so those gains are descriptive" |
| O4 | 2 | note: "the next **thirty-six minutes**" | 4,867 spoken words = 37.4 min at 130 wpm, 40.6 at 120 | either trim ≈ 120 words (the note rewrites in §6 do it) or say "about thirty-five to forty minutes" |
| O5 | 4, 6 | "market > $15B by 2029"; "EU AI Act (Art. 13): high-risk systems must provide explanations in human-understandable terms" | the $15B/2029 figure appears **nowhere** in the thesis or the three papers and has no citable source in the deck's own reference band; Art. 13 is transparency/instructions-for-use for deployers, the individual right to explanation of a decision is Art. 86 | market: drop the number or cite a specific market report; AI Act: "high-risk systems must be transparent enough to be interpreted (Art. 13), and affected persons can request an explanation of an individual decision (Art. 86)" |

Note on the stability table (computed from thesis Table 7.1 means and SDs):

| Dataset | Metric | Gap (DyHuCoG − HPCF) | Pooled SD | SD/gap | ±1σ overlap? |
|---|---|---:|---:|---:|---|
| ML-1M | NDCG@20 | 0.0247 | 0.0038 | 0.15 | no |
| ML-1M | Recall@20 | 0.0264 | 0.0034 | 0.13 | no |
| ML-1M | Coverage | 0.0550 | 0.0100 | 0.18 | no |
| ML-1M | ILD | 0.0550 | 0.0055 | 0.10 | no |
| Amazon-Book | NDCG@20 | 0.0036 | 0.0029 | **0.81** | **YES** |
| Amazon-Book | Recall@20 | 0.0058 | 0.0039 | **0.67** | **YES** |
| Amazon-Book | Coverage | 0.0770 | 0.0110 | 0.14 | no |
| Amazon-Book | ILD | 0.0670 | 0.0105 | 0.16 | no |

This is exactly consistent with the thesis's own decision to keep Amazon-Book descriptive. The
deck should say the same thing, not claim seed separability on every metric.

### 4.4 Small polish items (low risk, high credibility)

1. **Slide 29, band game**: the coalition table lists {G}, {V}, {D}, {G,V}, {V,D}, {G,V,D} but not
   **{G,D}**. The stated Shapley values 90 / 70 / 40 are only consistent with v({G,D}) = 100, i.e.
   guitar + drums exactly additive. Add the row `{G, D} | Guitar + Drums | 100`, or a jury member
   may ask why one 2-player coalition is missing.
2. **Slide 55 / 64**: when asked "9.8 % or 10.9 % for cold users?" the honest answer is that the
   table uses rounded NDCG values (0.061 / 0.055 → +10.9 %) while the paper's prose uses unrounded
   ones (0.0606 / 0.0552 → +9.8 %). Know this; optionally footnote the slide.
3. **Slide 20**: "GroupLens, 2000" → MovieLens-1M was released in 2003 (Harper & Konstan, 2015).
4. **Reference [19]**: attribute the Beijing dataset to Zhang, S. et al. (UCI, 2017); Dua &
   Taniskidou are the repository curators, not the dataset authors. Same line already correctly
   attributes Wine Quality to Cortez et al. (2009).
5. **Reference [28]**: add the issue number: IJIES **18(9)**, 241–257 (2025).
6. **Slide 30 / 34**: consider one line of explicit scope, e.g. "SHAP explains the surrogate's
   reconstruction of the partition, in the original variables; the fidelity floor (macro-F1 ≈ 0.82)
   is what keeps that bridge valid." This is the thesis's own caveat and pre-empts the obvious
   question "are you explaining K-Means or the surrogate?".
7. **Backup slides**: three additions would pay for themselves during Q&A, all cut-ready from the
   thesis: (i) Proposition 6.1 + the Appendix A.2 proof sketch and the εj scope note (thesis
   pp. 71, 109); (ii) Table 7.5 cold-start + Yelp2018 robustness (thesis p. 95) since the deck
   mentions Yelp only in a protocol row; (iii) a "scope and limitations" slide quoting Ch. 8.3/9.4
   (approximation everywhere, surrogate dependence, tabular/offline, no user study, no public code
   release per Appendix E).

---

## 5. Speech, timing and rehearsal

* The main flow carries **4,867 words on 76 slides** (mean 64 / slide; thinnest notes: slides 3, 8,
  25, 31, 38, 48, 50, 64, 69 at 28–39 words; thickest: 14, 29, 53, 72 at 100–152).
* At a rehearsed 130 wpm that is **37.4 min**, i.e. the deck's own "thirty-six minutes" is
  optimistic by about 1.5 min, and at a slower 120 wpm it is 40.6 min, which would overrun a
  40-minute slot on its own.
* **There are no time-check cues left in the deck.** They existed in v8/v10 and were lost when the
  notes were replaced in v20. Four cues on the section dividers would restore control: after the
  protocol (slide 17, target ≈ 11 min), at Contribution I (26, ≈ 17), Contribution II (38, ≈ 24),
  Contribution III (51, ≈ 33).
* Easy, non-destructive cuts (**≈ 120 words ≈ 1 min**), all in notes that are misaligned or
  duplicated anyway: slide 14 (76 → 80 words, but replaces a misaligned note), 15 (65 → 85),
  16 (90 → 70), 20/21 (144 → 125, kills the identical pair), 53 (135 → 95, kills the self-repeat),
  57 gets a real protocol note (55) while 58 takes the ML-1M results text (63) and 59 the Amazon
  text (46) instead of the current duplicate pair, 67/68/71/72 (306 → 240, four overlapping
  conclusion notes become four distinct beats). Net **−123 words → 4,744 words ≈ 36.5 min at
  130 wpm**, which finally matches the slide-2 promise.

---

## 6. Ready-to-apply fix list (exact locations)

### 6.1 Slide-text edits in `build_v25.py` (or as a patch on the PPTX)

| Line | Current | Replacement |
|---|---|---|
| 357 | `market > $15B by 2029.` | drop the number, or cite the report explicitly |
| 419 | `EU AI Act (Art. 13): high-risk systems must provide explanations **in human-understandable terms**.` | `EU AI Act: high-risk systems must be transparent enough to be interpreted (Art. 13); affected persons can request an explanation of a decision (Art. 86).` |
| 656 | `... dew point, rain, wind speed)...` | `... dew point, wind direction, wind speed)...` |
| 658 | `["Selected clusters", "k = 3 → 9 sub-clusters"]` | `["Selected clusters", "k = 3 coarse regimes"]` |
| 668 | `(GroupLens, 2000)` | `(GroupLens; released 2003)` |
| 901 | `("Comparison", "LIME-based surrogate explanation on the same partition")` | `("Comparison", "LIME surrogate pipeline, used as the theoretical / literature comparator (Ch. 5, §5.4)")` |
| 961 | `("O3  ·  Shapley justified over LIME", "Met", "Four axioms; higher stability and cross-cluster comparability")` | `("O3  ·  Shapley justified over LIME", "Met", "Four axioms (Ch. 5, §5.4); LIME comparator discussed in Ch. 5–6")` |
| 1084 | KPI `"3 → 9"` | `"k = 3 → L2"` (sublabel unchanged: "coarse regimes → nested sub-clusters") |
| 1090 | `("Level 2", "Each coarse cluster split again into sub-clusters (3 → 9)")` | `("Level 2", "Each coarse cluster split again into sub-clusters (level 2)")` |
| 1140 | caption `"Fig. 6.3 (thesis): SHAP importance per sub-cluster, level 2 of the hierarchy"` | `"Fig. 6.3 (thesis): cluster-specific SHAP importance, coarse level"` |
| 1219 | `...accuracy, diversity and novelty.` | `...accuracy, diversity and context.` |
| 1293 | `["M","MSE","Accuracy"]`, row `["25","≈ 5.6×10⁻⁵","≈ 96 %"]` | header `"Accuracy vs. reference"`, row `"≈ 98 %"` |
| 1342 | `Beat HPCF on both datasets in NDCG@20 and Recall@20, with p < 0.05 after correction.` | `Beat HPCF on both datasets in NDCG@20 and Recall@20; significance tabulated on MovieLens-1M (Table 7.6), Amazon-Book reported as a descriptive gain.` |
| 1495 | `γ·novelty` | `γ·context` |
| 1726 | banner "one tenth of the gap ... on every metric, so the ordering is stable across seeds" | see O3 suggested wording |
| 91 | `Dua, D. & Taniskidou, E. Beijing Multi-Site Air Quality Data. UCI (2017).` | `Zhang, S. et al. Beijing Multi-Site Air Quality Data Set. UCI Machine Learning Repository (2017).` |
| 100 | `IJIES 18, 241–257 (2025)` | `IJIES 18(9), 241–257 (2025)` |

### 6.2 Speaker-note rewrites (keys in `notes_v25.json`, by deck slide number)

The four note families below replace the misaligned / duplicated ones. They are written in the
deck's own spoken register (plain sentences, one transition per note, no em dashes) and their word
counts are the ones used in the timing calculation above.

**Slide 14** (now: the five RQs, wrong slide) → the three limitations and the gap:

> Here the three structural limitations are stated together, and they are exactly what this thesis
> works on. First, lack of explainability: complex models are still hard to explain in a way that
> is faithful and actionable. Second, difficulty of scaling: a local explanation does not carry
> over to a multi-level structure or to hundreds of thousands of records. Third, weak integration
> into learning: most explanations stay post-hoc, so they never shape how the model learns or how
> it handles the accuracy, diversity and context trade-off. The gap is the sentence in the orange
> box: the literature still lacks one cooperative-attribution framework that explains clustering
> faithfully, stays consistent across levels, and then works as an in-training signal in
> recommendation. My claim is that Shapley-value attribution can be that framework.

**Slide 15** (now: 65 words, 85 % similar to slide 16) → the five questions:

> Five questions structure the work. RQ1 asks whether Shapley values can explain black-box
> clustering faithfully, at instance level and at cluster level. RQ2 extends this to large-scale,
> multi-level clustering while staying feasible and consistent. RQ3 asks whether cooperative
> attribution can move beyond post-hoc and become part of how a recommender learns. RQ4 asks
> whether ranking, context and diversity can improve together when importance comes from a
> cooperative-game utility. RQ5 asks what one cooperative-game view brings to both explanation and
> recommendation. The aim is in the strip at the top: develop, justify and evaluate that view.

**Slide 16** (now: 90 words, duplicates slide 15) → trim the framing sentence and keep the cards:

> So the thesis is three contributions that build on each other. C1 explains a black-box partition:
> features are the players, the Silhouette of the clustering is the value function, and a LightGBM
> surrogate with TreeSHAP brings the attribution back to the original variables. C2 keeps that
> explanation consistent across levels at scale, with the cross-level aggregation of
> Proposition 6.1. C3, DyHuCoG, moves attribution inside the model: preference-aware Monte Carlo
> Shapley becomes an in-training signal on a hypergraph. Explanation, then scalability, then
> action.

**Slide 20** (MovieLens-1M) → half of the merged note:

> The first recommendation benchmark is MovieLens-1M: about one million ratings from 6,040 users
> on 3,706 movies, with a density near 0.045. It is the standard benchmark of the field, so the
> comparison with LightGCN, HCCF and HPCF is directly readable. Ratings above 3 become positive
> implicit feedback, and the genre is the context proxy.

**Slide 21** (Amazon-Book) → the other half:

> The second benchmark is Amazon-Book: 52,643 users, 91,599 books and about three million
> interactions, which gives a density near 0.0006, so the user-item matrix is almost empty. I
> include it to test whether Shapley-guided weighting helps most when the signal is weakest, and it
> is the large-scale benchmark of Contribution III. That 0.045 against 0.0006 density gap is the
> core of the robustness argument.

**Slide 53** (now: 135 words, states the objectives twice) → one statement of each:

> This contribution addresses two research questions, shown at the top of the slide: can
> cooperative attribution become part of how a recommender learns, and can it improve ranking,
> context and diversity together? Three objectives answer them. First, model recommendation as a
> cooperative game over users, items and contexts, where the coalition utility mixes accuracy,
> diversity and context. Second, put preference-aware Monte Carlo Shapley inside message passing as
> dynamic hyperedge weights. Third, show that ranking, coverage and diversity can improve together
> on two datasets, with the evidence in Table 7.1.

**Slide 57** (now: the ML-1M results, wrong slide) → the C3 protocol:

> This is the protocol for the recommendation study. Two datasets: MovieLens-1M as the dense
> benchmark and Amazon-Book as the sparse one, with Yelp2018 only as an auxiliary check. The split
> is user-level and time-ordered, 70, 10 and 20, with a leave-one-out target. Six baselines from
> four model families are compared on NDCG@20, Recall@20, catalogue coverage and intra-list
> diversity, over five seeds, and the ablation removes one component at a time.

**Slides 58 / 59** (now: Amazon text on both) → slide 58 takes the ML-1M results note currently
attached to slide 57 ("The results on MovieLens-1M show ... 9.8 percent ..."), slide 59 keeps one
of the two Amazon notes ("The same evaluation is conducted on Amazon-Book ... 13.3 percent ...").

**Slides 67 / 68 / 71 / 72** (now: four overlapping conclusion notes, 306 words) → four distinct
beats, ≈ 240 words:

> **67 (divider):** So let me bring everything together. Three contributions, one cooperative-game
> thread: faithful explanation of a partition, consistency across levels of detail, and attribution
> used as an in-training signal. Before the closing claim, I want to state the limitations honestly
> and the perspectives they open.
>
> **68 (synthesis):** This table is the thesis in one view. C1 explains a black-box partition with
> Shapley. C2 keeps that explanation consistent across levels at scale. C3, DyHuCoG, uses
> attribution as an in-training signal. Read across the three, the same logic moves from post-hoc
> description to in-training guidance, and the three takeaways at the bottom are the ones I would
> like the jury to remember.
>
> **71 (perspectives):** The limitations become an agenda. Four directions: lower-variance Shapley
> estimators with adaptive refresh rules; truly online and streaming recommendation, which also
> removes the static-graph assumption; user-centred evaluation, to measure whether explanations
> improve judgement, trust and perceived fairness; and broader trustworthy-AI evaluation, including
> exposure fairness and auditing.
>
> **72 (conclusion):** The thesis answer is in the orange box: cooperative game theory can serve as
> a shared methodological view for actionable explanation across clustering and recommendation.
> Four outcomes support it: a common formal language for attributing importance; faithful
> clustering explanation and consistent multi-level explanation; explanation as a method rather
> than a comment added later; and alignment with the expectations of the AI Act, the OECD
> principles and the GDPR. Explanation does not have to remain a description of what happened; it
> can help us understand, control and improve AI systems.

### 6.3 Build hygiene

The notes are injected by slide number after the build (`build_v25.py:1791-1794`), so changing
`notes_v25.json` alone is enough to fix every note problem, with no rebuild needed: open the
existing v25 PPTX with python-pptx and rewrite the notes text frames for the slides above, save as
v26. That preserves all layout, fonts, equations and the footer/citation fix from v25, which is the
safest possible edit. The slide-text edits in §6.1 are small string substitutions inside existing
runs; if you prefer, they can also be applied to the PPTX in place (low risk for the pure
substitutions; the two table-cell corrections are single-run strings as well).

---

## 7. Q&A preparation (answers grounded in the thesis, with the honest scope)

**Method and game theory**

1. *Why Shapley and not another attribution method?* Four axioms: efficiency, symmetry, null
   player, additivity (Ch. 2.8.2, Ch. 5.4.2). Shapley is the unique allocation satisfying them,
   which is what makes cluster-level claims comparable; LIME has no equivalent guarantee and is
   sensitive to perturbation design.
2. *Did you run LIME?* In Chapter 5 the comparison is theoretical and literature-backed, and the
   thesis says so explicitly; the LIME pipeline is described as the comparator in the shared
   protocol (Ch. 4.3.7) and discussed again in Ch. 6.5.2. Do not claim an empirical bake-off.
3. *Are you explaining K-Means, or the surrogate?* The surrogate: TreeSHAP explains tree models,
   not centroids, and efficiency holds with respect to the surrogate's log-odds output. The
   surrogate reconstructs the partition with macro-F1 ≈ 0.82 (100 trees, 31 leaves), and that
   fidelity is the validity condition for the explanation (Ch. 5.3.4, 5.4.2).
4. *Why is Silhouette the value function if the SHAP values are computed on the surrogate?*
   Silhouette defines the cooperative game that motivates the analysis; the surrogate is the
   tractable bridge to it. The thesis is explicit that these are two objects.
5. *What exactly does Proposition 6.1 prove?* For a strict nested hierarchy on a consistent feature
   space, parent-level expected absolute importance equals the size-weighted expectation over
   children plus a residual εj from surrogate mismatch, which vanishes under perfect fidelity. It
   is derived from the law of total expectation; it is a bounded accounting identity, not a general
   invariance theorem, and εj is not empirically estimated in the thesis (p. 71).
6. *Why does importance change between levels, then?* Because the parent story is regime selection
   and the child story is variation within a regime; Proposition 6.1 makes those differences
   interpretable rather than contradictory.

**Clustering results**

7. *Why k = 3 for wine when k = 2 is geometrically better?* k = 2 gives Silhouette 0.214 / DB 1.775,
   k = 3 gives 0.144 / 2.097; k = 3 is selected on interpretability grounds, because it supports
   three distinct explanatory profiles instead of one coarse split (Ch. 5.3.2).
8. *Where does 0.63 come from?* Beijing, not wine. The thesis repeats this twice to prevent the
   confusion.
9. *Why is the Beijing Silhouette so much higher?* The regime structure is physically strong; the
   thesis compares it against the 0.37 reported by Gramegna & Giudici as a positioning point, not
   as a like-for-like benchmark.
10. *Which variables define the regimes?* Global: temperature, dew point, pressure, then CO, NO2,
    PM10, PM2.5. Per regime: ozone/temperature for warm photochemical, CO/SO2/PM10 with low wind
    speed for winter smog, and favourable meteorology with negative pollutant contributions for the
    clean-air regime.
11. *What is the residual limitation of the whole clustering line?* It is post-hoc: attribution
    explains a partition that already exists, which is exactly what C3 changes.

**Recommendation (DyHuCoG)**

12. *What is actually new versus HCCF/HPCF?* Those models treat message importance as uniform or
    attention-weighted; DyHuCoG derives it from a cooperative-game utility that mirrors the
    training objective (accuracy, diversity, context) and injects it as dynamic hyperedge weights.
13. *Is the gain from Shapley or from the extra components?* The ablation answers it: removing
    Shapley weighting costs 4.6 % on ML-1M and 6.1 % on Amazon-Book; context is the largest single
    component (−8.2 % / −11.0 %) and the hypergraph is next.
14. *Is Amazon-Book significant?* The thesis does not claim it: the fully tabulated paired tests
    are per-user NDCG@20 on MovieLens-1M (all six comparisons, Holm-corrected, dz ≥ 1.33), and
    Amazon-Book is reported as a descriptive gain. Slide 77's stability claim should be limited the
    same way.
15. *Why M = 50 permutations?* MSE 1.4e−5 against a high-sample reference, about 99 % accuracy,
    refresh every 10 batches (≈ 49 updates/epoch), 1.78× HPCF training time; M = 100 buys 3.5e−6
    for 2.5× the cost, i.e. diminishing returns.
16. *Overhead?* 1.78× HPCF training (2000 s vs 1125 s), 1.84 ms inference per query on ML-1M, 4.4
    vs 4.1 GB; acceptable in an academic setting and bounded by the refresh period.
17. *Where does it fail?* Compute overhead, dependence on meaningful context, Monte Carlo variance,
    component-wise ablation only, baselines frozen in early 2026, and no user study of explanation
    quality.
18. *Why call it "actionable"?* Definition 1.1: a modifiable factor expressed in domain language.
    The thesis is explicit that actionability is a framing concept, empirically illustrated rather
    than measured; a user study is listed as future work. Say that rather than overclaiming.

**Three things never to say in the viva**

1. "The experiments show statistical significance on Amazon-Book" (they do not; descriptive only).
2. "We benchmarked SHAP against LIME on the wine data" (Chapter 5 says theoretical, not a bake-off).
3. "The hierarchy has nine sub-clusters" (unsupported; the "9" is PCA components explaining 97 %
   variance).

---

## 8. What still needs a human decision

1. **Jury list** (slides 1 and 76): supply the official composition (roles, grades, institutions)
   from the defence convocation. Nothing else in the deck should be published to the jury before
   this is corrected.
2. **Slot length**: confirm whether the 40 minutes include questions. If yes, use the ~120-word cut
   set in §5/§6.2 plus the four time-check cues; if no, the deck is comfortably in range.
3. **Whether the "9 sub-clusters" was an actual experiment** (three coarse × three fine). If a
   level-2 run exists outside the thesis and the papers, then the deck should carry its numbers and
   the thesis should be fixed instead; if not, remove the number as proposed.
4. **Chinese/other market figure** for slide 4: cite a specific report or drop the number.

---

*Prepared from: `MOUAD_LOUHICHI_Thesis.pdf`, `MOUAD_LOUHICHI_Thesis_Resume.pdf`, the three source
papers, `try/MOUAD_LOUHICHI_VIVA_40min (6).pptx` (+ its 75-slide PDF export), all 22 Beige Green
versions, `try/speech_enhanced*.json`, the full `try/viva_builder/` sources, and
`example-phd-passes/`. Extracted text and audit scripts are reproducible from the commands in this
review; no thesis or paper file was modified.*
