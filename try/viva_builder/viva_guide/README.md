# Viva guide generator

Generates the presentation guide for `try/MOUAD_LOUHICHI_VIVA_40min_BeigeGreen_v28.pptx`.

## Builds

- `python3 build.py` — single-file guide → `MOUAD_LOUHICHI_VIVA_PRESENTATION_GUIDE.html`
  (inline CSS/JS; KaTeX for equations, loaded from the jsDelivr CDN).
- `python3 build_site.py` — multi-page site → `MOUAD_LOUHICHI_VIVA_PRESENTATION_GUIDE/`
  (25 pages + `assets/style.css` + `assets/app.js`; same content split one page per
  part: overview, one playbook per deck section, walkthroughs, glossary, section 7
  delivery, Q&A by category A–H, three cheat sheets). Each page has the full
  cross-page sidebar, a prev/next pager and a page-local search box.
- `python3 preview_server.py [port]` — serves the site at `/` (default port 8080);
  the single-file build stays reachable at `/MOUAD_LOUHICHI_VIVA_PRESENTATION_GUIDE.html`.

## Content modules

| file | contents |
|---|---|
| `content_map.py` | sidebar, hero, deck map & timing ledger, section playbooks 0–3 |
| `content_map2.py` | section playbooks 4–7, Q&A stage, backup slides |
| `content_tech.py` | glossary part A + the 12 concept walkthroughs |
| `content_tech_b.py` | glossary part B (baselines, metrics, statistics) |
| `content_qa1.py` | Q&A categories A–D (Q001–Q050) |
| `content_qa2.py` | Q&A categories E–H (Q051–Q100) |
| `content_extra.py` | section 7 delivery plan, cheat sheets (tables run through `build.rich`) |

## Math

Formulas live in the content as plain Unicode (backticked where they sit inline).
`build.py` rewrites them to TeX (`$...$`) via the `MATH_REPS` table and wraps them
in `<span class="math">\(…\)</span>`; KaTeX + auto-render then typesets them on
page load. To fix or add a formula, edit `MATH_REPS` (literal replacement strings —
group refs `\1` are only supported in lambda entries). `plain()`/`detex()` give the
readable text form used in `data-search` attributes.
