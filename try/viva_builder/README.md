# VIVA deck builder (template: "Beige Green Modern Illustrative Playful Thesis Defense Presentation")

Generates `../MOUAD_LOUHICHI_VIVA_40min_BeigeGreen.pptx` — the content of
`MOUAD_LOUHICHI_VIVA_40min (6).pptx` re-laid out in the template's visual language
(beige `FEF8F3` background, dark green `124944`, mustard `ECC665`, orange `DF8330`,
embedded fonts *Roca Two Bold* / *Nunito*, the template's decorative asterisks/sparkles).

* `tpl.py`      – design system: palette, embedded-font metrics, rich-text model, native shapes, tables, accents
* `layouts.py`  – slide chrome, section slides, cards, KPI tiles, pills, auto-shrink text fitting, `equation()`
* `mathkit.py`  – LaTeX → native PowerPoint equations (OMML) with a rendered PNG fallback
* `build.py`    – the 64 slides (content mapped from the original 75-slide VIVA; speaker notes merged per slide)
* `notes_speech.json`   – speaker notes actually used by the build: the original notes rewritten in plain,
  easy-to-pronounce English (technical terms, numbers and structure unchanged; no em dashes). Keyed by original slide number.
* `notes_original.json` – the untouched speaker notes extracted from the original VIVA deck (kept for reference)

Build (python-pptx, pillow, fonttools, matplotlib, latex2mathml required):

```bash
# one-off: extract the template's embedded fonts + decorative PNGs
python3 prepare_assets.py "../Beige Green Modern Illustrative Playful Thesis Defense Presentation (1).pptx" "../MOUAD_LOUHICHI_VIVA_40min (6).pptx" /tmp/viva_build
# build
VIVA_FONT_DIR=/tmp/viva_build/fonts VIVA_ASSET_DIR=/tmp/viva_build/assets VIVA_FIG_DIR=/tmp/viva_build/figs \
python3 build.py "../Beige Green Modern Illustrative Playful Thesis Defense Presentation (1).pptx" ../MOUAD_LOUHICHI_VIVA_40min_BeigeGreen.pptx
```

The build prints `built 64 slides` followed by *fit notes*: text blocks that had to be auto-shrunk
below 0.85× to fit their box (plain text only; equations are never shrunk below 0.8× without a note).

## Equations

All formulas (Shapley value, Proposition 6.1, coalition value function, Monte Carlo estimator,
message passing, loss, complexity, significance stats — 33 equations on slides 22, 33, 34, 44–48, 52, 53)
are **native, editable PowerPoint equations** (Office Math / OMML, *Cambria Math*), written from LaTeX by
`mathkit.py`:

* LaTeX → MathML (`latex2mathml`) → intermediate tree → OMML (`m:oMathPara` / `m:oMath`, fractions,
  n-ary operators with limits, sub/superscripts, delimiters, accents, radicals, script/bold letters).
* Each equation is wrapped in `mc:AlternateContent`: the `Choice` (requires `a14`) is the live equation,
  the `Fallback` is a PNG rendered with matplotlib's mathtext (STIX), so viewers without Office Math
  support still show the formula.
* Sizes are measured with mathtext and auto-fitted to the target box (`layouts.equation(...)`).
* `VIVA_EQ_MODE=picture python3 build.py ...` emits the PNGs only — useful for renderers whose OMML
  layout is unreliable (e.g. Spire.Presentation previews).

Any new LaTeX must parse in both `latex2mathml` and matplotlib mathtext: use `\dfrac`, `{\sum}_{k}` for
side limits, `\left( … \right)` instead of `\big(`, and avoid `\!`.

## Typography

Body copy uses a 1.40× line pitch (1.48× for lines containing sub/superscripts) with explicit paragraph
spacing; text that would overflow its box is shrunk with measured wrapping (min 0.62×). Math symbols not
present in the embedded font subsets (Greek letters, arrows, ⊆ ∪ …) are set in Office-bundled
*Calibri* / *Cambria Math* so they render in PowerPoint without extra fonts.

## Wording

Slide text (`build.py`) and speech (`notes_speech.json`) use short sentences and plain words that are easy
to say out loud, in the register of a typical viva (e.g. *shows*, *helps*, *works*, *the gap is*, *so*).
Technical terms are kept as they are (Shapley, surrogate, post-hoc, hypergraph, Silhouette, Davies–Bouldin,
NDCG, Proposition 6.1, regime, ...). No em dashes ("—") are used anywhere: titles use a colon
(*Choosing k: Interpretability over Geometry*), footers and labels use a middle dot (·), sentences use
a comma, a colon or a full stop. En dashes remain only inside compound names and numeric ranges
(Davies–Bouldin, Holm–Bonferroni, 2003–09, pages 806–811).

## Version VII (`build_v7.py` → `../MOUAD_LOUHICHI_VIVA_40min_BeigeGreen_v7.pptx`)

Version VII keeps the Beige Green look and every v6 constraint (native OMML equations, plain wording,
no em dashes, speaker notes on every slide) and restructures the deck along the lines of the reference
viva deck (R. Nesmaoui). 95 slides: 90 in the main flow + a closing title slide (jury, for the Q&A) +
4 backup slides.

What is new, per area:

* **Chrome**: 1…7 section tracker in the header, ENSIAS logo in the footer, numbered reference
  footnotes (`cite(...)` + `REFS`, 28 entries listed on two References slides).
* **Title**: real jury table (9 members, same jury as the reference deck) under the presenter /
  supervisor cards; duplicated at the end for the discussion.
* **Context**: one slide per approach (content-based, collaborative, hybrid + MF, graph / hypergraph),
  each with a diagram and a "Limitation" box; brand-logo slide (falls back to text chips when
  `$VIVA_THESIS_FIG_DIR/logos/{netflix,spotify,yelp,amazon}.png` are absent).
* **Protocol**: four dataset cards (spec table + sample rows + why), baselines table, metrics table with
  the formulas (native equations), hardware table by contribution.
* **Per contribution** (same order every time): Research Gap (bullets + statement box) → RQ → Objectives
  table → methodology → Evaluation Protocol → results (bullets left, table right, best row bold; C3 main
  results split ML-1M / Amazon-Book, ablation per dataset) → Answer to RQ (+ objectives status table) →
  Key Findings → Limitations → Takeaway statement box.
* **Technical deep dive** (3 slides at the start of Contribution I): a cooperative game in one picture
  (three-piece band example, characteristic function table), the Shapley value as the average marginal
  contribution (all 6 arrival orders, formula, four axioms), and the same game three times in the thesis.
* **Thesis figures** (cropped from the thesis PDF into `$VIVA_THESIS_FIG_DIR`): Fig. 5.1, 5.2, 6.1, 6.2,
  6.3, 7.2, 7.3, 7.4.
* **Conclusion**: "Takeaway · Thesis" box under the synthesis, publications table with the correct author
  lists / journal / DOI / status, "Thesis answer" statement box + key outcomes.
* **Backup**: Table 7.1 with ± std, Table 7.6 paired tests, Tables 7.3 / 7.4 cost and convergence.

## Versions (never overwritten; each version has its own build script and notes file)

| Version | Deliverable | Build | Notes | What it is |
|---|---|---|---|---|
| v6 | `../MOUAD_LOUHICHI_VIVA_40min_BeigeGreen.pptx` | `build.py` | `notes_speech.json` | 64 slides, first Beige Green deck |
| v7 | `../MOUAD_LOUHICHI_VIVA_40min_BeigeGreen_v7.pptx` | `build_v7.py` | `notes_v7.json` | 95 slides, full detailed script (about 10,300 words, roughly 70 min: rehearsal / Q&A reference) |
| v8 | `../MOUAD_LOUHICHI_VIVA_40min_BeigeGreen_v8.pptx` | `build_v8.py` | `notes_v8.json` | same 95 slides, **40-minute script** (about 5,500 words, 39 min at 140 wpm; "Time check" cues on section slides) |
| v9 | `../MOUAD_LOUHICHI_VIVA_40min_BeigeGreen_v9.pptx` | `build_v9.py` | `notes_v9.json` | v8 + brand logos on the "AI-Powered Recommendation Is Everywhere" slide + audited thesis figure / table numbers |
| v10 | `../MOUAD_LOUHICHI_VIVA_40min_BeigeGreen_v10.pptx` | `build_v10.py` | `notes_v10.json` | **de-redundant rebuild: 95 → 79 slides, 5,525 → 4,563 spoken words**, three deep-dive slides collapsed into one methodology slide, speech rewritten as spoken delivery |
| v19 | `../MOUAD_LOUHICHI_VIVA_40min_BeigeGreen_v19.pptx` | `build_v19.py` | `notes_v19.json` | projection pass: wider title logos, real platform logos on slide 7, on-palette slide-9 figure, slide 29 de-cluttered (no bottom clipping), DyHuCoG figure enlarged with 6 → 3 equation rows, variance / big-O equations folded into bullets deck-wide, captions floored at 14 pt |
| v20 | `../MOUAD_LOUHICHI_VIVA_40min_BeigeGreen_v20.pptx` | `build_v20.py` | `notes_v20.json` | speaker notes replaced by `speech_enhanced.fixed.json`, re-aligned entry-by-entry to the 79-slide order (the speech was authored for an older numbering), two short transitions added for the C1 protocol and C2 takeaway slides, longest entries trimmed to land at 4,665 spoken words ≈ 36 min at 130 wpm |
| v21 | `../MOUAD_LOUHICHI_VIVA_40min_BeigeGreen_v21.pptx` | `build_v21.py` | `notes_v21.json` | full slide-vs-speech technical audit: speech upgraded to the slides' level (slide 12 now names nodes/edges, LightGCN/HCCF/HPCF, hyperedges, benchmarks and the compute/memory limitation), "forty minutes" corrected to thirty-six, "acidity" corrected to fixed acidity (slide 33), small trims keep 4,679 words = 36.0 min at 130 wpm |
| v22 | `../MOUAD_LOUHICHI_VIVA_40min_BeigeGreen_v22.pptx` | `build_v22.py` | `notes_v22.json` | read-along pass: notes on the gap slides (4, 18-19, 22-23, 29-30, 32, 55, 60-62) now mirror the slide wording and numbers so the presenter can read from the slide; the spoken "players = features, v(S) = Silhouette" line added to slide 29; 4,713 words = 36.3 min at 130 wpm |
| v23 | `../MOUAD_LOUHICHI_VIVA_40min_BeigeGreen_v23.pptx` | `build_v23.py` | `notes_v23.json` | slide 4 note rewritten as natural spoken delivery while keeping the slide's facts ($15B by 2029, EU AI Act, accountable/auditable/actionable, core tension); slide 5 text rewritten to mirror the speech (what we can change, domain language, what to change to improve the outcome); 4,737 words = 36.4 min at 130 wpm |
| v24 | `../MOUAD_LOUHICHI_VIVA_40min_BeigeGreen_v24.pptx` | `build_v24.py` | `notes_v24.json` | dataset slides (18-21) reduced to the example deck's level: SAMPLE RECORDS tables dropped, intro bullets and the specification table get the freed room; speech unchanged |
| v25 | `../MOUAD_LOUHICHI_VIVA_40min_BeigeGreen_v25.pptx` | `build_v25.py` | `notes_v25.json` | footer never replaced: citations move to a compact `[n] Surname Year` band above the intact running footer (40 slides), no font below 14 pt anywhere and no equation below 16 pt (metrics formulas 18 pt), slide 29 coalition table trimmed to 6 rows, Precision@K row dropped, speech unchanged |
| v26 | `../MOUAD_LOUHICHI_VIVA_40min_BeigeGreen_v26.pptx` | `build_v26.py` | `notes_v26.json` | **review pass** (see `../../DEEP_READING_REVIEW_v25.md`): slide facts corrected against the thesis and the three papers (Beijing weather = wind direction, Monte-Carlo M = 25 = 98 %, coalition utility = context not novelty, the unsupported "3 → 9 sub-clusters" count dropped, Fig. 6.3 caption, GroupLens wording, refs [19] and [28]); claims trimmed to thesis scope (market figure removed, AI Act Art. 13/86 wording, LIME comparator theoretical, significance tabulated on MovieLens-1M only, backup-slide SD claim corrected); speaker notes re-aligned slide by slide (the Contribution III off-by-one, the RQ note parked on slide 14, the duplicated dataset / conclusion / reference notes), seven `Time check` cues restored and the speech de-duplicated to **4,692 words = 36.1 min at 130 wpm** |
| v27 | `../MOUAD_LOUHICHI_VIVA_40min_BeigeGreen_v27.pptx` | `build_v27.py` | `notes_v27.json` | **the candidate's own opening speech**: slides 1 and 2 carry the speech as written (the spoken title spells out "artificial intelligence"), slide 4 is a short spoken note that follows the three motivation cards, and slide 6's notes and the two blocks "Why the gap matters" / "What this thesis argues" were rewritten short so that screen and speech say the same three things; speech now **4,594 words = 35.3 min at 130 wpm** |
| v28 | `../MOUAD_LOUHICHI_VIVA_40min_BeigeGreen_v28.pptx` | `build_v28.py` | `notes_v28.json` | the title on slides 1 and 76 spells out **Explainable Artificial Intelligence**, re-broken as "Cooperative Game Theory for Explainable" / "Artificial Intelligence in Recommendation Systems" and still 50 pt (measured with the embedded Roca Two Bold: 82.3 % of the box); the slide 6 speech is rewritten in spoken register; **4,641 words = 35.7 min at 130 wpm** |
| v29 | `../MOUAD_LOUHICHI_VIVA_40min_BeigeGreen_v29.pptx` | `build_v28.py` + `patch_v29.py` | `notes_v28.json` | **full-citation bands**: every citation band now carries the complete reference from slides 73-74 instead of "[21] Zhang 2020", at 14 pt over one to three lines; the bands are drawn last (nothing can cover them again) and the content that used to sit over them was moved up shape by shape, only as far as needed (49 slides, 94 shapes, no card overlaps created) |
| v30 | `../MOUAD_LOUHICHI_VIVA_40min_BeigeGreen_v30.pptx` | `build_v30.py` | `notes_v30.json` | slide 6 keeps the evolution timeline and **one** card: the one-line "The interpretability gap grows" note and the card "What this thesis argues" are gone, and "Why the gap matters" is now a full-width card whose three bullets sit in three columns at 22 pt; the speech for slide 6 loses its last paragraph, spoken total **4,587 words = 35.3 min** |
| v31 | `../MOUAD_LOUHICHI_VIVA_40min_BeigeGreen_v31.pptx` | `build_v31.py` | `notes_v31.json` | speech only: the note on slide 4 is cut to **80 words** (the three motivation questions and the tension, nothing else); spoken total **4,562 words = 35.1 min at 130 wpm** |
| v32 | `../MOUAD_LOUHICHI_VIVA_40min_BeigeGreen_v32.pptx` | `build_v32.py` | `notes_v32.json` | slide 4 describes instead of asking: same three cards, new headline "Motivation: Why Explainability Matters", and each card now states a claim plus the facts behind it (recommenders decide at scale / the reasoning is hidden / transparency is now expected); slide 4 speech replaced, **85 words**; spoken total **4,567 words = 35.1 min** |
| v33 | `../MOUAD_LOUHICHI_VIVA_40min_BeigeGreen_v33.pptx` | `build_v33.py` | `notes_v33.json` | speech only: slide 16 now uses the candidate's own text about the three contributions, with the third sentence completed (DyHuCoG "brings attribution inside the model itself") and each contribution's ground named (Wine Quality / Beijing Air Quality / MovieLens-1M and Amazon-Book), closing on "from explanation, to scalability, and finally to action"; **97 words**, spoken total **4,580 words = 35.2 min** |
| v34 | `../MOUAD_LOUHICHI_VIVA_40min_BeigeGreen_v34.pptx` | `build_v34.py` | `notes_v34.json` | slide 10 figure replaced by `fig_slide10.py` + `assets/slide10_collaborative_filtering.png`: a 4 x 5 rating matrix, Pearson similarity computed on the co-rated columns (0.87 / 0.50 / 0.00), the missing cell filled by the similarity-weighted average (5.85 / 1.37 = 4.3) and the real sparsity strip (MovieLens-1M 4.47%, Amazon-Book 0.06%); note 10 +52 words; spoken total **4,632 words = 35.6 min** |
| v35 | `../MOUAD_LOUHICHI_VIVA_40min_BeigeGreen_v35.pptx` | `build_v35.py` | `notes_v35.json` | slide 12 figure replaced by `fig_slide12.py` + `assets/slide12_graph_hypergraph.png`: the pairwise panel is now the bipartite user-item graph (observed interactions only) with a directed 2-hop message u2 - i2 - u1 and equal edge weights; the hypergraph panel puts hyperedge e1 on u1, u2, i2 and the context c1 and e2 on u2, u3, i3 over the same nodes, weights re-learned at every step (DyHuCoG); note 12 +48 words; spoken total **4,680 words = 36.0 min** |
| v36 | `../MOUAD_LOUHICHI_VIVA_40min_BeigeGreen_v36.pptx` | `build_v36.py` + `patch_v36.py` | `notes_v36.json` | slides 13 + 14 merged into one problem-statement slide: row 1 the four classical limits (blue/teal cards), row 2 the three structural limits (gold-oval cards), row 3 the THESIS GAP bar verbatim; band is the union [21] [23] (two works) [24] in full form on three lines; slide 14 deleted, page numbers decremented (79 to 78 slides); merged note 103 words; spoken total **4,627 words on slides 1-75 = 35.6 min** |

v9 changes in detail:

* Slide 7 shows the Netflix, Spotify, Yelp and Amazon logos (the SVG icons used by the reference deck,
  rasterised to `$VIVA_THESIS_FIG_DIR/logos/{netflix,spotify,yelp,amazon}.png`; text chips are the fallback).
* Every thesis table used on a slide now carries its thesis number in a small caption: Table 4.1 (datasets),
  4.2 (hardware), 5.1 (SHAP vs LIME), 6.1 (Beijing validation), 6.2 / 6.3 (generalisation, literature),
  7.1 (main results), 7.2 (ablation), 7.3 / 7.4 (efficiency), 7.5 (cold-start), 7.6 (significance).
  Figures: 5.1, 5.2, 6.1, 6.2, 6.3, 7.1 (architecture), 7.2, 7.3, 7.4. All numbers were checked against
  the captions in `MOUAD_LOUHICHI_Thesis.pdf` (pages 66 to 119).
* Corrected: the objective-evidence pointers now cite the exact tables / figures ("Table 6.1, Fig. 6.1, 6.2";
  "Table 7.1, Fig. 7.2, 7.3" instead of "Tables 7.1 to 7.6"); the backup Table 7.3 scale-factor column uses the
  thesis values (× MF on MovieLens-1M: 1.41, 1.63, 1.89, 1.96, 2.19, 3.41).

## Version X (`build_v10.py` → `../MOUAD_LOUHICHI_VIVA_40min_BeigeGreen_v10.pptx`)

Rebuilt to remove the redundancy measured in `REDUNDANCY_ANALYSIS.md`, with the structure
matched slide-for-slide to the reference viva (`example-phd-passes/Presentation1 (1) (1).pptx`).
**95 → 79 slides** (the reference is 80) and **5,525 → 4,563 spoken words**, i.e. 42.5 → 35.1 min
at 130 wpm and 38.0 min at 120. Words per slide 60.7 → 60.0, with 16 fewer slides carrying the
same argument.

Per-contribution spine is now identical to the reference in all three contributions:
`Research Gap → RQ and Objectives → method → Evaluation Protocol → results → Answer →
Key Findings → Limitations → Takeaway`. Counts land on the reference: C I 12 (ref 12),
C II 13 (ref 13), C III 16 (ref 16), backup 3 (ref 3).

**The three "Technical Deep Dive" slides are now one methodology slide.** *A Cooperative Game in
One Picture* and *The Shapley Value: Average Marginal Contribution* were merged into *The
Cooperative Game and the Shapley Value* (tab: Methodology), and *The Same Game, Three Times in
This Thesis* was dropped — the contribution cards and the synthesis already carry that map. The
six-arrival-order table became a single worked row (V → D → G: +40, +40, +120 → 90/70/40).
Left column: three ingredients, the `(N, v)` pair, the band example, the Shapley formula.
Right column: the `v(S)` table, the worked row, the four axiom chips, "why this rule".

**Speech rewritten in the v7 spoken register.** `notes_v10.json` (97 → 79 keys, 18 orphaned by
the removed slides) now reads as talk rather than as notes: first-person framing ("I want to be
careful here", "a member of the jury may well notice it"), varied discourse markers instead of
the terse v8/v9 fragments, and explicit signposting between slides. Measured against the decks
it replaces:

| | v7 | v9 | **v10** |
|---|---|---|---|
| connectors per 100 words | 6.5 | 6.1 | **10.0** |
| contractions per 100 words | 0.13 | 0.14 | **2.17** |
| first-person " I " per 100 words | 0.45 | 0.33 | **0.55** |
| sentences opening "And"/"So" | 5.4% | 4.0% | **16.0%** |

The deck is written to be *said*, not read: contractions throughout (`let's`, `we're`, `isn't`,
`you'll`), inter-slide transitions that name the move ("So let's move to the problem itself",
"So let's move on to Contribution I", "And that brings us to Contribution III", "So let's bring
everything together"), and direct address ("as you can see", "you'll notice", "look at the
orange box").

**Plain wording applies to everything except the technical vocabulary.** Simplify the connective
tissue, never the terms of art. `interpretability`, `transparency`, `clustering pipelines`,
`attribution`, `surrogate`, `coalition`, `characteristic function`, `Silhouette`, `NDCG`,
`hyperedge`, `message passing`, `surrogate fidelity`, `Proposition 6.1`, `Holm`, `Cohen` and
`Wilcoxon` are kept verbatim wherever they appear, because they are the thesis's own language and
the jury will use them in questions. A simplification pass on slide 4 wrongly turned them into
`clear explanation` / `clear` / `clustering tools`; they were restored. The rule that survives is:
`interpretability` (6 syllables) stays, while `widespread` becomes `how big these systems are`,
`afterwards` becomes `later`, and `the pattern we keep seeing` becomes `what keeps happening`.

The last row is the guard rail. Two earlier drafts of this rewrite opened **38.7%** and **37.2%**
of sentences with "And" or "So" — that is a tic, not connection, and both were measured and
reverted. The rule that works is *one* "And"/"So" transition per note, with the remaining
sentence-initial positions varied across *now / then / which / finally / in other words / here
is / notice that / put simply / in short / rather than*.

**Other repetition removed.** Each headline number is spoken once in the main flow (`0.63` 4 → 1,
`1.78` 2 → 1, `13.3 percent` 2 → 1); the recap openers ("In short:", "The findings in short:")
are gone; the thesis one-liner is planted on *The Three Contributions* and cashed only in the
*Conclusion*; all seven `Time check` cues are retained and re-timed; slides 47/14/87 no longer
read their own text aloud.

**Slides deliberately kept.** The closing quartet stays on every contribution. Rev 1 of the
analysis wrongly proposed deleting `Key Findings` and `Takeaway`; the reference deck has the
same twelve slides (555 words against our 591), so it is the accepted template, not a deviation.
Also kept: the band example and the Shapley axioms, Definition 1.1, both bridging `Limitations`
slides, Proposition 6.1, publications, section dividers.

**Other slides removed (13).** Redundant restatements: *Our Thesis in One View* (prose version of
the contribution cards), *Datasets Used Throughout* (the four cards already give every
statistic), *Ranking Quality Across All Baselines* (charts the same 7 models / 2 metrics as the
two main-results tables), *Backup Slides* index. Merged: *Clustering as a Cooperative Game* →
*The Bridge* (its `v(S) = Silhouette` definition), *Pipeline in Five Stages* → *Evaluation
Protocol*, *Cluster-Specific Signatures* → *Global SHAP Ranking* (Fig. 5.2 now a strip beneath
Fig. 5.1), *SHAP vs LIME* → *Answer to RQ1* (row O3), *Three Atmospheric Regimes* → *How
Importance Changes Across Levels*, *Generalisation and Comparison* → *Key Findings*, *Coalition
Value* → *Recommendation as a Cooperative Game*, *Multi-Objective Learning* → *Shapley-Weighted
Message Passing* (sixth equation row; the architecture figure is shortened from 1.9″ to 1.55″ to
make room), *Coverage & Diversity* → main-results tables, *Cold-Start / Robustness* →
*Statistical Significance*.

Build:

```bash
VIVA_FONT_DIR=/tmp/viva_build/fonts VIVA_ASSET_DIR=/tmp/viva_build/assets VIVA_FIG_DIR=/tmp/viva_build/figs \
VIVA_THESIS_FIG_DIR=/tmp/viva_build/thesis \
python3 build_v10.py "../Beige Green Modern Illustrative Playful Thesis Defense Presentation (1).pptx" \
  ../MOUAD_LOUHICHI_VIVA_40min_BeigeGreen_v10.pptx
```

Thesis figure crops must be named `fig5_1_wine_global.png`, `fig5_2_wine_clusters.png`,
`fig6_1_beijing_global.png`, `fig6_2_beijing_force.png`, `fig6_3_beijing_multilevel.png`,
`fig7_2_ranking.png`, `fig7_3_coverage_ild.png`, `fig7_4_waterfall.png` in
`$VIVA_THESIS_FIG_DIR` (crop rectangles at the bottom of this file). Brand logos are optional:
`$VIVA_THESIS_FIG_DIR/logos/{netflix,spotify,yelp,amazon}.png`, text chips otherwise.

## Build any version

```bash
# thesis figure crops (pymupdf): page / clip rectangles in PDF points, zoom 4
#   fig5_1 p86 (113,83,468,301)   fig5_2 p86 (69,642,512,697)   fig6_1 p96 (135,83,446,293)
#   fig6_2 p96 (69,575,512,763)   fig6_3 p97 (83,157,526,260)   fig7_2 p113 (92,636,518,763)
#   fig7_3 p114 (108,83,473,239)  fig7_4 p118 (157,147,424,264)  fig7_1 p104 (60,295,535,403)
VIVA_FONT_DIR=/tmp/viva_build/fonts VIVA_ASSET_DIR=/tmp/viva_build/assets VIVA_FIG_DIR=/tmp/viva_build/figs \
VIVA_THESIS_FIG_DIR=/tmp/viva_build/thesis \
python3 build_v9.py "../Beige Green Modern Illustrative Playful Thesis Defense Presentation (1).pptx" ../MOUAD_LOUHICHI_VIVA_40min_BeigeGreen_v9.pptx
```

`tpl.table()` now understands `**bold**` and `x_{i}` / `x^{2}` inside cell strings.

## v32: slide 4 describes, it does not ask

```bash
python3 patch_v32.py    # ../MOUAD_LOUHICHI_VIVA_40min_BeigeGreen_v32.pptx + notes_v32.json
```

The first slide where the talk starts describing its subject carried three questions. It now carries three
statements, in the same three cards (same geometry, colours, pills and type sizes):

| Card | Claim (23 pt) | Facts (18 pt) |
|---|---|---|
| Everywhere | Recommenders decide at scale. | They shape what billions of users see, buy and watch every day: news, study, health and credit decisions. |
| The Black Box | The reasoning behind those decisions is hidden. | Matrix factorisation hid it in latent factors; deep and graph models hide it in message passing. Neither can be audited or acted on. |
| Toward Trust | Transparency is now expected. | Users, designers and regulators now ask for reasons. It has to be built into the model, not added afterwards. |

The headline follows ("Motivation: Why Explainability Matters") and the speech is replaced to match the three
columns word for word, in 85 words. Measured with the embedded fonts, the longest card needs four lines at
18 pt in a box that holds ten, so nothing overflows.

## v30: slide 6, two blocks only

```bash
python3 patch_v30.py    # ../MOUAD_LOUHICHI_VIVA_40min_BeigeGreen_v30.pptx + notes_v30.json
```

Slide 6 keeps the evolution diagram and "Why the gap matters". The card is rebuilt as a full-width
panel (y 6.38-9.74, clear of the three-line citation band) with its three bullets as three columns of
one bullet each at 22 pt, centred vertically. The columns are copies of the original bullet
paragraph, so the bold lead-in, the yellow bullet and the white Nunito in both weights are exactly
the ones the deck already used. The speech loses the paragraph about the removed card.

## v29: the reference bands in full

```bash
python3 patch_v29.py    # ../MOUAD_LOUHICHI_VIVA_40min_BeigeGreen_v29.pptx
```

There is no `build_v29.py`: the bands are a post-build pass, and doing it here rather than in the
builder is what makes it safe. The pass reads the 28 entries out of the deck's own reference
slides, joins the works inside one numbered reference with ` · ` and separate references with
three spaces, wraps them at 14 pt with the metrics of the embedded Nunito Semi-Bold (measured on a
3 % narrower box than PowerPoint will use, so a borderline wrap counts as a line), and then:

* puts each band's white strip and text at the bottom of the tree, so no shape can cover them;
* lifts whatever sat over the band, group by group, never further than the nearest shape above
  it, and gives up the empty strip under a card's text when the group is boxed in (three panels on
  slides 12, 27, 29, 61, 68, 72 lost 0.03-0.18 in of padding);
* keeps the footer and page number exactly where they were.

Slides that cite four or more works (23 with seven, 52 with five) would need four or five lines, so
they print authors, venue, volume, pages and year and drop the paper title, which brings them back to
three lines. Everything is asserted in the report, including any group that could not move.

## v28: the full title

```bash
python3 patch_v28.py    # ../MOUAD_LOUHICHI_VIVA_40min_BeigeGreen_v28.pptx + notes_v28.json
```

`patch_v28.py` takes v27 as its source. It measures the new title lines against the 17.8 in
title box with the metrics of the font embedded in the file (Canva wraps each `.fntdata` in a
small preface; `embedded_font()` finds the real sfnt by its signature), so the fit is a
measurement rather than an estimate. The running footer on the other 77 slides still says
"Explainable AI"; the same measurement says the full form fits there too (≈ 88-92 % of the
footer box) whenever it should be rolled out.

## v27: the opening speech

The candidate's own opening and plan (slides 1 and 2), a short spoken note on slide 4, and a
short note plus rewritten cards on slide 6.

```bash
python3 patch_v27.py    # ../MOUAD_LOUHICHI_VIVA_40min_BeigeGreen_v27.pptx + notes_v27.json
```

`patch_v27.py` takes v26 as its source, so the whole review pass of v26 stays in the chain. The
slide 6 cards are rebuilt from the paragraph style already in the file, so the bold lead-in and
the two font families are preserved; the extra fourth bullet of the left card is dropped.

## v26: how the delivered deck was produced

The v26 PPTX was not rebuilt from the template: the template's embedded fonts and the
thesis-figure crops live outside the repository (`/tmp/viva_build`), so the deck was patched in
place, which also guarantees that every layout, font, native OMML equation and the v25
footer/citation fix survive untouched.

```bash
python3 patch_v26.py    # ../MOUAD_LOUHICHI_VIVA_40min_BeigeGreen_v26.pptx + notes_v26.json
```

`patch_v26.py` carries the same corrections as `build_v26.py` (kept for provenance and for a
future rebuild) and fails loudly if any target string does not match exactly once. Both files
apply the findings of `../../DEEP_READING_REVIEW_v25.md`; the notes in `notes_v26.json` are the
delivered speech and are the only thing you need to edit to change wording in future versions,
since the builder writes them onto the deck by slide number.

