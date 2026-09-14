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
| v10 | `../MOUAD_LOUHICHI_VIVA_40min_BeigeGreen_v10.pptx` | `build_v10.py` | `notes_v10.json` | **de-redundant rebuild: 95 → 79 slides, 5,525 → 4,568 spoken words**, three deep-dive slides collapsed into one methodology slide, speech rewritten in the v7 spoken register |

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
**95 → 79 slides** (the reference is 80) and **5,525 → 4,568 spoken words**, i.e. 42.5 → 35.1 min
at 130 wpm and 38.1 min at 120. Words per slide 60.7 → 60.1, with 16 fewer slides carrying the
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
| connectors per 100 words | 6.5 | 6.1 | **8.4** |
| first-person " I " per 100 words | 0.45 | 0.33 | **0.77** |
| sentences opening "And"/"So" | 5.4% | 4.0% | **1.7%** |

The last row is deliberate: an earlier draft of this rewrite opened 38.7% of sentences with
"And" or "So", which reads as a tic rather than as connection. The markers are now spread across
*now / then / which / in other words / here is / notice that / that is why / let me*.

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
