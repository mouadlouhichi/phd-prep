# VIVA deck builder (template: "Beige Green Modern Illustrative Playful Thesis Defense Presentation")

Generates `../MOUAD_LOUHICHI_VIVA_40min_BeigeGreen.pptx` — the content of
`MOUAD_LOUHICHI_VIVA_40min (6).pptx` re-laid out in the template's visual language
(beige `FEF8F3` background, dark green `124944`, mustard `ECC665`, orange `DF8330`,
embedded fonts *Roca Two Bold* / *Nunito*, the template's decorative asterisks/sparkles).

* `tpl.py`      – design system: palette, embedded-font metrics, rich-text model, native shapes, tables, accents
* `layouts.py`  – slide chrome, section slides, cards, KPI tiles, pills, auto-shrink text fitting
* `build.py`    – the 64 slides (content mapped from the original 75-slide VIVA; speaker notes merged per slide)
* `notes_original.json` – speaker notes extracted from the original VIVA deck (keyed by original slide number)

Build (python-pptx, pillow, fonttools required):

```bash
# one-off: extract the template's embedded fonts + decorative PNGs
python3 prepare_assets.py "../Beige Green Modern Illustrative Playful Thesis Defense Presentation (1).pptx" "../MOUAD_LOUHICHI_VIVA_40min (6).pptx" /tmp/viva_build
# build
VIVA_FONT_DIR=/tmp/viva_build/fonts VIVA_ASSET_DIR=/tmp/viva_build/assets VIVA_FIG_DIR=/tmp/viva_build/figs \
python3 build.py "../Beige Green Modern Illustrative Playful Thesis Defense Presentation (1).pptx" ../MOUAD_LOUHICHI_VIVA_40min_BeigeGreen.pptx
```

Math symbols not present in the embedded font subsets (Greek letters, arrows, ⊆ ∪ …) are set in
Office-bundled *Calibri* / *Cambria Math* so they render in PowerPoint without extra fonts.
