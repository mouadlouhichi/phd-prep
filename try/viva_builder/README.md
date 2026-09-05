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

Speaker notes live in `notes_v7.json` (numeric keys = v6 notes, string keys = the new slides).

```bash
# thesis figure crops (pymupdf): page / clip rectangles in PDF points, zoom 4
#   fig5_1 p86 (113,83,468,301)   fig5_2 p86 (69,642,512,697)   fig6_1 p96 (135,83,446,293)
#   fig6_2 p96 (69,575,512,763)   fig6_3 p97 (83,157,526,260)   fig7_2 p113 (92,636,518,763)
#   fig7_3 p114 (108,83,473,239)  fig7_4 p118 (157,147,424,264)
VIVA_FONT_DIR=/tmp/viva_build/fonts VIVA_ASSET_DIR=/tmp/viva_build/assets VIVA_FIG_DIR=/tmp/viva_build/figs \
VIVA_THESIS_FIG_DIR=/tmp/viva_build/thesis \
python3 build_v7.py "../Beige Green Modern Illustrative Playful Thesis Defense Presentation (1).pptx" ../MOUAD_LOUHICHI_VIVA_40min_BeigeGreen_v7.pptx
```

`tpl.table()` now understands `**bold**` and `x_{i}` / `x^{2}` inside cell strings.
