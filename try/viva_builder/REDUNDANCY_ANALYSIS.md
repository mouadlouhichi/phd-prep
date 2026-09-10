# Redundancy analysis — `MOUAD_LOUHICHI_VIVA_40min_BeigeGreen_v9.pptx`

Measured from the built deck (python-pptx): every slide's on-slide text and speaker notes.
Reference benchmark: `example-phd-passes/VIVA_Redwane_NESMAOUI.pdf`.

## 1. Headline numbers

| Measure | Value |
|---|---|
| Slides | **95** (91 main flow + 4 backup) |
| Spoken words | **5,780** total · **5,525** in the main flow (slides 1–91) |
| Duration | **39.5 min** @ 140 wpm · **42.5 min** @ 130 wpm · **46.0 min** @ 120 wpm |
| Average time per slide | **26–30 s** |
| Non-content slides | 13 (title, outline, 7 dividers, 2 refs, thank-you, closing title) |
| Content slides | 78 |
| Reference viva (Nesmaoui, passed) | **77 pages** |

The README claims v8 is "about 5,500 words, 39 min at 140 wpm". The word count is right
(5,525). The duration is only right **at 140 wpm**, which is a fast reading pace. A viva with
technical content, equations and a mixed-language jury realistically runs **120–130 wpm**, which
puts this script at **42.5–46 min** — already over before a single pause.

The deck's own `Time check` cues confirm the drift is progressive, not constant:

| Slide | Declared cue | Actual @ 130 wpm |
|---|---|---|
| 18 | minute 8 | 8.5 |
| 46 | minute 20 | 22.0 |
| 61 | minute 27 | 28.9 |
| 82 | minute 36 | **39.2** |
| 90 | minute 40 | **42.3** |

**The binding constraint is not the words, it is the slide count.** 26 s per slide means the
results tables, the two equation slides and Proposition 6.1 all have to be rushed. Slides need
cutting *and* the script shortened; neither alone is enough.

---

## 2. Redundancy findings, ranked by measured evidence

### R1 — The closing quartet: 12 slides, 13% of the deck, saying 4 claims three times ⚠️ biggest win

Every contribution ends with **Answer to RQ → Key Findings → Limitations → Takeaway**
(slides 42–45, 57–60, 78–81). That is **12 slides and 591 spoken words (4.5 min)**.

`Answer` and `Key Findings` are the same list. In C I:

| Slide 42 (`Answer to RQ1`) | Slide 43 (`Key Findings`) |
|---|---|
| "O1 met: global + per-cluster reading" | #1 "explained at two levels at once" |
| "O2 met: attribution returns to the original chemical variables" | #2 "attribution lands in the chemistry, not a latent space" |
| "O3 met: four axioms, LIME does not" | #4 "the cooperative concept is what makes it trustworthy" |
| — | #3 "k = 3 over geometry" — **already slide 38** |

Then slide 45 (`Takeaway`) states it a third time: *"a well-founded lens … original feature
space is what makes it actionable"*. Same pattern in C II (57/58/60) and C III (78/79/81).

Slide 79 is the worst offender — every number on it was already spoken two to twelve slides
earlier: `+13.3/+9.8` (70, 71), cold-start `+10.9/+9.6` (77), ablation `−8.2/−11.0/−6.8/−8.9/
−4.6/−6.1` (74), `t = 46.38, dz = 1.33` (76), `1.78×, 1.84 ms` (75, 80).

**Note:** the `Limitations` slides (44, 59, 80) are *not* redundant with each other — each one
is the bridge into the next contribution ("These limits start Contribution II"). Keep 44 and 59.

### R2 — The thesis spine is stated five times

| Slide | Title | Words | What it says |
|---|---|---|---|
| 16 | The Three Contributions | 64 | C1/C2/C3 + "three steps that build on each other" |
| 17 | Our Thesis in One View | 49 | C1/C2/C3 + "from post-hoc description to in-training guidance" |
| 33 | The Same Game, Three Times | 119 | C1/C2/C3 players + value functions table |
| 83 | Synthesis of the Three Contributions | 61 | C1/C2/C3 table + "explains, stays consistent, guides" |
| 87 | Conclusion | 72 | "the same Shapley logic explains … stays consistent … guides learning" |

**365 words, 2.8 min.** Slides 16 and 17 are effectively the same slide — 17 is a prose
restatement of the cards on 16. Slide 33 is the same map again as a technical table, and it
front-loads C2/C3 detail the jury has not yet seen, so it gets re-explained at 49 and 65.

Verbatim one-liner count in the speech: **7 slides** (2, 15, 17, 18, 31, 85, 87).

### R3 — Datasets are described three times

Slide 18 (divider) lists all four datasets. Slide 19 ("Datasets Used Throughout the Thesis",
69 words) gives sizes and densities for all four. Slides 20–23 then give a card each
(186 words). Slide 19's entire content reappears on 20–23, including the `0.0447` / `0.0006`
density contrast, which is also on 69 and 71.

`383,585` is printed on **12 separate slides**: 19, 21, 46, 47, 48, 50, 51, 52, 56, 57, 58, 60.

### R4 — C III results: the same seven models three times

Slides 70 (ML-1M table) and 71 (Amazon-Book table) contain NDCG@20 and Recall@20 for all seven
models. Slide 72 ("Ranking Quality Across All Baselines") is thesis Fig. 7.2 — a bar chart of
**the same seven models on the same two metrics**. Its speech adds one point ("a monotone
ladder") that costs 64 words and a slide.

### R5 — Five slides on "what is a cooperative game"

31 (game in one picture, 120 w) + 32 (Shapley value, 134 w) + 33 (three value functions, 119 w)
+ 34 (clustering as a game, 73 w) + 64 (recommendation as a game, 68 w) = **514 words, 4 min**.

Slides 31 and 32 are genuinely valuable (the band example is the best teaching device in the
deck) but they are two slides where one dense one would do — 32's arrival-order table and its
axiom box can share a slide with 31's characteristic-function table. Slide 34 restates the game
for a third time before the method starts.

### R6 — Housekeeping duplication

| Slide | Issue |
|---|---|
| 89 | "References (2 / 2)" — 28 refs across two slides, 20 spoken words |
| 91 | Closing title slide with the full jury table — slide 90 already says thank you |
| 92 | "Backup Slides" index listing the three backup slides that follow |
| 27 | "Hardware & Software" — 30 spoken words for a four-row table |

### R7 — The speech paraphrases instead of repeating (this is why it feels longer than it is)

Measured speech-to-speech 4-gram overlap between *consecutive* slides is almost nil, and
content-word Jaccard between `Answer`/`Findings`/`Takeaway` is **0.00–0.13**.

That is not a sign of low redundancy — it is the opposite. The same claim is restated in
*different words each time*, so the jury never gets the cue that a summary is being repeated.
Verbatim repetition would at least signal "recap". Paraphrased repetition just sounds like new
material that happens to mean the same thing.

Highest verbatim slide-reading (speech that duplicates its own slide): slide 47 at **49.1%**,
slide 14 at 40.5%, slide 87 at 39.1%, slide 45 at 37.8%.

### R8 — Numbers repeated across slides

| Value | Spoken on | Printed on |
|---|---|---|
| Silhouette `0.63` | 38, 52, 56 (3×) | 21, 38, 46, 52, 56, 57, 58 (7×) |
| overhead `1.78×` | 75, 80, 95 (3×) | 27, 75, 79, 80, 95 (5×) |
| `+9.8 %` NDCG | 70, 78 | 70, 78, 79, 94 |
| ablation `4.6 / 6.1` | 74 | 18 slides |

Slide 38 also spends 17 words disambiguating *"the 0.63 Silhouette belongs to Beijing in
Contribution II, not to wine"* — a confusion the deck created by printing `0.63` seven times.

---

## 3. Cut plan

### Tier 1 — 12 slides, zero information lost (pure restatement + housekeeping)

| Cut | Slide | Words saved | Why it is safe |
|---|---|---|---|
| 1 | 17 Our Thesis in One View | 49 | prose restatement of the C1/C2/C3 cards on 16 |
| 2 | 19 Datasets Used Throughout | 69 | every fact reappears on cards 20–23 |
| 3 | 43 Key Findings (C I) | 29 | = O1/O2/O3 of slide 42, plus slide 38 |
| 4 | 45 Takeaway (C I) | 48 | third statement of 42 + 44 |
| 5 | 58 Key Findings (C II) | 28 | = O1/O2/O3 of slide 57 |
| 6 | 60 Takeaway (C II) | 49 | third statement of 57 + 59 |
| 7 | 72 Ranking Quality (chart) | 64 | same 7 models, same 2 metrics as tables 70/71 |
| 8 | 79 Key Findings (C III) | 28 | every number already on 70, 71, 74, 75, 76, 77 |
| 9 | 81 Takeaway (C III) | 59 | third statement of 78 + 62 |
| 10 | 89 References (2 / 2) | 20 | fold 28 refs onto one slide |
| 11 | 91 closing title + jury | 24 | slide 90 already closes |
| 12 | 92 Backup index | 41 | 93/94/95 are self-labelled "Backup:" |

**Subtotal: −12 slides, −508 words.**

Move the surviving `Answer to RQ` slide so it also carries the takeaway box: one slide per
contribution that says *the answer, the evidence table, and what it means next*.

### Tier 2 — 11 slides, needs rewriting but keeps all content

| Cut | Slides | Words saved | How |
|---|---|---|---|
| 13 | 20–23 → 2 cards | 46 | one card for the clustering pair, one for the rec pair |
| 14 | 31 + 32 → 1 | 100 | band table + arrival-order table + axioms on one slide |
| 15 | 34 fold into 35 | 40 | the clustering value function belongs on the bridge slide |
| 16 | 13 + 14 → 1 | 50 | classical limits and the three problems are one argument |
| 17 | 6 + 7 → 1 | 25 | evolution timeline + brand logos on one context slide |
| 18 | 37 fold into 36 | 45 | C1 protocol rows join "Pipeline in Five Stages" |
| 19 | 51 fold into 49 | 40 | C2 protocol rows join "Multi-Level Workflow" |
| 20 | 33 → move to 83 | 70 | the three-value-function table *is* the synthesis slide |
| 21 | 80 merge into 78 | 35 | keep 44/59 as bridges; C3 limits join the answer slide |
| 22 | 27 merge into 26 | 20 | hardware row under the metrics table |
| 23 | 5 shorten | 20 | keep Definition 1.1, drop the three-domain chips |

**Subtotal: −11 slides, −491 words.**

### Result

| | Now | Tier 1 | Tier 1 + 2 |
|---|---|---|---|
| Slides | 95 | 83 | **72** |
| Main flow | 91 | 80 | **69** |
| Spoken words | 5,525 | 5,017 | **4,526** |
| @ 130 wpm | 42.5 min | 38.6 min | **34.8 min** |
| @ 120 wpm | 46.0 min | 41.8 min | **37.7 min** |
| Sec / slide (main flow, @ 130) | 28.0 | 28.9 | **30.3** |

72 slides lands next to the reference deck's 77, and 35–38 min leaves the 2–5 min of slack a
40-minute slot actually needs.

---

## 4. Speech: five rules to stop repeating

1. **Never speak the slide.** Slides 47 (49%), 14 (41%), 87 (39%) are read aloud. If the text is
   on the screen, say what is *not* on the screen — the reason, the caveat, the next step.
2. **Say each headline number once.** `0.63` → slide 52 only. `1.78×` → slide 75 only.
   `+9.8 / +13.3` → slides 70/71 only. Elsewhere say "the Beijing partition" / "about twice
   HPCF" / "the gains on the sparse dataset".
3. **One answer per RQ, stated once.** Cut "The answer to RQ1 is yes … O1 is met … O2 is met …
   O3 is met". The evidence table is on the slide; say the answer and the one caveat.
4. **Delete the recap openers.** "The findings in short:", "In short:", "The takeaway:" appear on
   43, 58, 60, 79, 81 — five slides whose entire function is to restate. These are the slides to
   delete, not to shorten.
5. **Plant the thesis once, cash it once.** State the one-liner on slide 16, do not restate it on
   17, 31 or 83; land it again only in the conclusion (87). Currently 7 slides carry it.

Two lines to delete outright:

- Slide 38: *"And to avoid a confusion: the 0.63 Silhouette belongs to Beijing in Contribution II,
  not to wine."* — unnecessary once `0.63` is printed on one slide.
- Slide 44/59: *"These limits start Contribution II"* / *"That is the bridge to Contribution III"*
  — say it once, on the slide that introduces the next contribution.

---

## 5. Do **not** cut

- **31/32** the band example and the six arrival orders — the strongest teaching slides in the deck.
- **5** Definition 1.1 (actionable insight) — the thesis's key concept; trim, don't drop.
- **44, 59** per-contribution Limitations — they are the argument that makes the three
  contributions one story rather than three papers.
- **50** Proposition 6.1 — the only formal result in the talk.
- **84** Publications — the jury needs the mapping to chapters.
- **85** "Limitations, Stated Honestly" — the global version is the one the jury will probe.
- **93–95** backup tables — free, they cost nothing unless asked.
- **7 section dividers** — 205 words total, and they carry the time-check cues.

---

## 6. Suggested target structure (72 slides)

| Section | Now | Target | Change |
|---|---|---|---|
| Title + outline | 2 | 2 | — |
| 01 Introduction | 5 | 4 | merge logos (7) into research context (6) |
| 02 Context & Problematic | 10 | 8 | merge 13+14; drop 17 (dup of 16) |
| 03 Experimental Protocol | 10 | 6 | drop 19; four cards → two; 27 into 26 |
| 04 Contribution I | 18 | 12 | deep dive 2→1; 33→83; 34 into 35; 37 into 36; drop 43, 45 |
| 05 Contribution II | 15 | 12 | 51 into 49; drop 58, 60 |
| 06 Contribution III | 21 | 17 | drop 72, 79, 81; 80 into 78 |
| 07 Conclusion | 8 | 7 | 33's value-function table lands on 83; refs 2→1 |
| Closing + backup | 6 | 4 | drop 91 (dup of 90), 92 (index) |
| **Total** | **95** | **72** | |

---

*Generated from the built v9 deck. Every figure above is a count over the slide text and speaker
notes extracted from `MOUAD_LOUHICHI_VIVA_40min_BeigeGreen_v9.pptx`.*
