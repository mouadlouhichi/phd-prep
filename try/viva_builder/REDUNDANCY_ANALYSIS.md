# Redundancy analysis — `MOUAD_LOUHICHI_VIVA_40min_BeigeGreen_v9.pptx`

**Rev 2.** Measured from two built decks with python-pptx:

- ours — `try/MOUAD_LOUHICHI_VIVA_40min_BeigeGreen_v9.pptx` (95 slides)
- reference — `example-phd-passes/Presentation1 (1) (1).pptx` (80 slides, the Nesmaoui viva that passed)

---

## ⚠️ Correction to Rev 1

Rev 1 claimed the reference viva passed *"at 77 slides with **no per-contribution recap
slides**"*, and on that basis recommended deleting slides 43, 45, 58, 60, 79 and 81
(the `Key Findings` and `Takeaway` slides).

**That claim is false and the recommendation is withdrawn.** The reference deck has the
identical closing quartet on every contribution:

| | Answers | Key findings | Limitations | Takeaways | words |
|---|---|---|---|---|---|
| C I | 36 | 37 | 38 | 39 | 153 |
| C II | 49 | 50 | 51 | 52 | 215 |
| C III | 65 | 66 | 67 | 68 | 187 |
| | | | | **total** | **555** |

Ours: 591 words across the same 12 slides — within 7% of the reference.

The error came from extracting titles out of `VIVA_Redwane_NESMAOUI.pdf`, where a
font-size heuristic latched onto the tab bar and returned "Objectives" for all 40
contribution slides, hiding the real headers. Reading the `.pptx` directly this time
exposed them. **Rev 1's "R1 — biggest win" is demoted: the closing quartet is the
accepted template, not a deviation from it.**

---

## 1. The reference deck's actual structure

80 slides, 16:9, only two layouts in use (`Title and Content` × 78, `Title Slide` × 2).

| Block | Slides | Words |
|---|---|---|
| Title + jury table | 1 | 45 |
| VIVA Outline | 1 | 44 |
| Introduction | 3–7 | 244 |
| Context and Problematic | 8–16 | 310 |
| Protocols (6 datasets + 4 metrics) | 17–27 | 276 |
| Contribution I | 28–39 | 397 |
| Contribution II | 40–52 | 621 |
| Contribution III | 53–68 | 608 |
| Conclusion / Synthesis | 69–75 | 252 |
| Questions + closing title | 76–77 | 14 |
| Backup | 78–80 | 94 |
| **Total** | **80** | **2,905** |

Main flow (1–77): **2,811 words = 21.6 min @ 130 wpm / 23.4 min @ 120 wpm.**
**36.5 words per slide.**

Per-contribution spine, identical in all three:

```
Research Gap
Research Questions → Objectives
<theory / architecture slides>
Evaluation protocol
Key results findings
────────────────────────────
Answers to the questions and objectives
Key findings
Limitations
Takeaways
```

Tab bar: `Objectives | Methodology | Results | Findings`. Five outline parts
(Introduction, Context & Problematic, Protocols, Contributions, Conclusion & Perspectives) —
the three contributions are **one** part, not three.

Seven section dividers carrying **78 words in total** (5, 11, 11, 16, 14, 15, 6).
One slide has no notes at all (77, the closing title).

> **Caveat I cannot resolve from the file:** the notes are full prose sentences, not bullet
> prompts, so 2,811 words is a real script — but I do not know the reference viva's time
> slot, nor how much the presenter ad-libbed past the notes. I can only report the script
> length, not the delivered talk length.

---

## 2. Side-by-side: the excess is in the contributions, nowhere else

| Section | REF slides | REF words | OURS slides | OURS words | × slides | × words |
|---|---|---|---|---|---|---|
| Introduction | 5 | 244 | 5 | 281 | 1.00 | 1.15 |
| Context & Problematic | 9 | 310 | 10 | 668 | 1.11 | **2.15** |
| Protocols | 11 | 276 | 10 | 477 | 0.91 | 1.73 |
| Contribution I | 12 | 397 | 18 | 1,285 | **1.50** | **3.24** |
| Contribution II | 13 | 621 | 15 | 883 | 1.15 | 1.42 |
| Contribution III | 16 | 608 | 21 | 1,359 | **1.31** | **2.24** |
| Conclusion | 7 | 252 | 8 | 390 | 1.14 | 1.55 |
| **Contributions total** | **41** | **1,626** | **54** | **3,527** | 1.32 | **2.17** |

Introduction, Protocols and Conclusion already match the reference almost exactly. The
contributions carry 13 extra slides and **2.2× the words**.

### The method + results block is where it concentrates

| | REF slides | REF words | OURS slides | OURS words | × words |
|---|---|---|---|---|---|
| C I method + results | 5 | 133 | 11 | 917 | **6.9** |
| C II method + results | 6 | 269 | 8 | 562 | 2.1 |
| C III method + results | 9 | 304 | 14 | 985 | **3.2** |
| **total** | **20** | **706** | **33** | **2,464** | **3.49** |

Concretely, side by side:

| Reference C I (5 slides, 133 w) | Ours C I (11 slides, 917 w) |
|---|---|
| 31 Euclidean Space · 17 w | 31 A Cooperative Game in One Picture · **120 w** |
| 32 Euclidean Space · 40 w | 32 The Shapley Value · **134 w** |
| 33 Architecture Walkthrough · 17 w | 33 The Same Game, Three Times · **119 w** |
| 34 Architecture Walkthrough · 23 w | 34 Clustering as a Cooperative Game · 73 w |
| 35 Key results findings · 36 w | 35 The Bridge · 79 w |
| | 36 Pipeline in Five Stages · 59 w |
| | 37 Evaluation Protocol · 63 w |
| | 38 Choosing k · 69 w |
| | 39 Global SHAP Ranking · 67 w |
| | 40 Cluster-Specific Signatures · 68 w |
| | 41 SHAP vs LIME · 66 w |

The reference spends **133 words** on the whole method-and-results block of its first
contribution; we spend **917**. The three-slide *Technical Deep Dive* (31–33, 373 words)
has no counterpart in the reference at all.

### Word density, deck-wide

| | REF | OURS | ratio |
|---|---|---|---|
| Words per slide | 36.5 | 60.7 | **1.66×** |
| Words per section divider | 11.1 | 29.3 | 2.6× |
| Main-flow words | 2,811 | 5,525 | 1.97× |

---

## 3. What still stands from Rev 1

These were measured directly and are unaffected by the correction:

- **Over budget at any realistic pace.** 5,525 words = 39.5 min @ 140, **42.5 @ 130**, 46.0 @ 120.
  The README's "39 min" only holds at 140 wpm. The deck's own `Time check` cues drift:
  slide 82 declares "minute 36", the words put you at 39.2 min @ 130 wpm.
- **The speech reads the slide aloud.** Share of spoken 4-grams already printed on the same
  slide: slide 47 **49.1%**, slide 14 40.5%, slide 87 39.1%, slide 45 37.8%.
- **Number repetition.** `0.63` printed on 7 slides and spoken 3× (hence slide 38's 17-word
  "that's Beijing, not wine" disambiguation); `383,585` printed on 12 slides; `1.78×` spoken
  3× and printed 5×; the ablation pair `4.6 / 6.1` printed on 18 slides.
- **Thesis one-liner spoken on 7 slides** (2, 15, 17, 18, 31, 85, 87).
- **Slide 72 re-charts tables 70/71** — same seven models, same two metrics, 64 words for
  "a monotone ladder".
- **Datasets described three times**: divider 18, overview 19, cards 20–23. The reference puts
  its equivalent (`General Specifications`) in **backup**, slide 78.

Withdrawn: the "no per-contribution recap slides" benchmark and the six slide deletions
based on it.

---

## 4. Corrected cut plan

Target: **match the reference's shape exactly.** Every section below lands on the
reference's slide count.

### Slide cuts (−18 → 77 slides)

**Contribution I: 18 → 12** (reference: 12)

| Cut | Slides | Why |
|---|---|---|
| deep dive 2 → 1 | 31 + 32 | band table + arrival-order table + axioms fit one slide |
| drop | 33 | the three-value-function table *is* the synthesis; move it to slide 83 |
| fold into 35 | 34 | the clustering value function belongs on the bridge slide |
| fold into 36 | 37 | C1 protocol rows join "Pipeline in Five Stages" |
| merge into 39 | 40 | cluster signatures are a second view of the same SHAP output |
| merge into 42 | 41 | SHAP-vs-LIME is the answer to O3; it belongs on the answer slide |

**Contribution II: 15 → 13** (reference: 13)

| Cut | Slides | Why |
|---|---|---|
| fold into 49 | 51 | C2 protocol rows join "Multi-Level Workflow" |
| merge into 53 | 54 | the three regimes are the same force plots as the global ranking |

**Contribution III: 21 → 16** (reference: 16)

| Cut | Slides | Why |
|---|---|---|
| merge into 64 | 65 | coalition value is the utility already defined on 64 |
| merge into 67 | 68 | the loss is part of the message-passing story |
| drop | 72 | chart of the same 7 models / 2 metrics as tables 70 and 71 |
| merge into 70/71 | 73 | coverage and ILD are already columns in those tables |
| merge into 76 | 77 | cold-start and robustness belong with significance |

**Context: 10 → 9** (reference: 9) — drop 17, a prose restatement of the C1/C2/C3 cards on 16.

**Protocol: 10 → 9** — move 19 to backup, exactly as the reference does with its
`General Specifications` slide.

**Conclusion: 8 → 7** (reference: 7) — fold references 89 into 88.

**Closing/backup: 6 → 4** — drop 91 (slide 90 already closes) and 92 (93/94/95 are
self-labelled "Backup:").

### Word cuts

| | Slides | Words | @130 wpm | w/slide |
|---|---|---|---|---|
| Now | 95 | 5,525 | 42.5 min | 60.7 |
| Slide cuts only (−18) | 77 | 4,704 | 36.2 min | 61.1 |
| **+ trim to 57 w/slide** | **77** | **4,400** | **33.8 min** | 57.1 |
| reference density (for scale) | 80 | 2,905 | 22.3 min | 36.5 |

Slide removals alone recover ~820 words and still leave the density unchanged. The density
is the real problem, so **the trim is not optional**: target 45–60 words per content slide,
which means roughly a 1-in-4 sentence cut on most slides, concentrated in the
method-and-results blocks where we are 2–7× the reference.

Two possible endpoints, and which one is right depends on your actual slot:

- **~4,400 words / 34 min** — fills a 40-minute slot with slack. Safe.
- **~2,900 words / 22 min** — matches the passed reference exactly. Requires cutting half the
  script; only worth it if the reference viva really ran that short.

---

## 5. Do **not** cut

- **The closing quartet — 42–45, 57–60, 78–81.** The reference has the same twelve slides at
  555 words against our 591. This is the template the jury saw and passed. *(Rev 1 wrongly
  listed six of these for deletion.)*
- **31/32** the band example and the six arrival orders — keep the content, put it on one slide.
- **5** Definition 1.1 (actionable insight) — the thesis's key concept; the reference has no
  equivalent and this is a genuine strength.
- **44, 59** per-contribution Limitations — they are the bridge that makes three contributions
  one story.
- **50** Proposition 6.1 — the only formal result in the talk.
- **84** Publications, **85** "Limitations, Stated Honestly".
- **93–95** backup tables — free unless asked.
- **7 section dividers** — but cut them to the reference's density: 78 words, not 205.

---

## 6. Speech rules (unchanged from Rev 1, all still valid)

1. **Never speak the slide.** Slides 47 (49%), 14 (41%), 87 (39%) are read aloud. Say what is
   not on the screen.
2. **Say each headline number once.** `0.63` → 52 only. `1.78×` → 75 only. `+9.8 / +13.3` →
   70/71 only. Elsewhere: "the Beijing partition", "about twice HPCF", "the sparse dataset".
3. **One answer per RQ, stated once.** The evidence table is on the slide; say the answer and
   the one caveat. (This is a *wording* cut, not a slide cut — see §5.)
4. **Cut recap openers, not recap slides.** "The findings in short:", "In short:", "The
   takeaway:" on 43, 58, 60, 79, 81 are where the words go; the slides stay.
5. **Plant the thesis once, cash it once.** Slide 16, then the conclusion. Not on 17, 31 or 83.

Plus: drop slide 38's 17-word `0.63` disambiguation once `0.63` appears on one slide, and say
"these limits start Contribution II" once, on the slide that introduces it.

---

*Every figure is a count over text and speaker notes extracted from the two `.pptx` files.
The reference-deck headers were read from the `.pptx` directly, not from the PDF.*
