# VIVA deck builder (template: "Beige Green Modern Illustrative Playful Thesis Defense Presentation")

Generates `../MOUAD_LOUHICHI_VIVA_40min_BeigeGreen.pptx` — the content of
`MOUAD_LOUHICHI_VIVA_40min (6).pptx` re-laid out in the template's visual language
(beige `FEF8F3` background, dark green `124944`, mustard `ECC665`, orange `DF8330`,
embedded fonts *Roca Two Bold* / *Nunito*, the template's decorative asterisks/sparkles).

* `tpl.py`      – design system: palette, embedded-font metrics, rich-text model, native shapes, tables, accents
* `layouts.py`  – slide chrome, section slides, cards, KPI tiles, pills, auto-shrink text fitting, `equation()`
* `mathkit.py`  – LaTeX → native PowerPoint equations (OMML) with a rendered PNG fallback
* `build.py`    – the 64 slides (content mapped from the original 75-slide VIVA; speaker notes merged per slide)
* `notes_original.json` – speaker notes extracted from the original VIVA deck (keyed by original slide number)

Build (python-pptx, pillow, fonttools, matplotlib, latex2mathml required):

```bash
# one-off: extract the template's embedded fonts + decorative PNGs
python3 prepare_assets.py "../Beige Green Modern Illustrative Playful Thesis Defense Presentation (1).pptx" "../MOUAD_LOUHICHI_VIVA_40min (6).pptx" /tmp/viva_build
# build
VIVA_FONT_DIR=/tmp/viva_build/fonts VIVA_ASSET_DIR=/tmp/viva_build/assets VIVA_FIG_DIR=/tmp/viva_build/figs \
python3 build.py "../Beige Green Modern Illustrative Playful Thesis Defense Presentation (1).pptx" ../MOUAD_LOUHICHI_VIVA_40min_BeigeGreen.pptx
```

The build prints `built 64 slides` followed by *fit notes* — text blocks that had to be auto-shrunk
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
