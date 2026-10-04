# -*- coding: utf-8 -*-
"""Section 7 delivery plan, Q&A tactics, number cheat sheet, never/always sheet, checklist."""


def _rich(s):
    fn = globals().get("RICH")
    return fn(s) if fn else s


def tbl(headers, rows, cls="tbl"):
    h = "".join("<th>%s</th>" % _rich(c) for c in headers)
    return ('<div class="tw"><table class="%s"><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>'
            % (cls, h, "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % _rich(c) for c in r) for r in rows)))


# ==========================================================================
# SECTION 7 — how it should be presented
# ==========================================================================
def render_sec7():
    beats = [
        ["<strong>67</strong> · Reset", "3-4 sentences, 16 s",
         "Announce the five beats: synthesis, publications, limitations, perspectives, thesis answer. Deliberately "
         "slow down here; the room has just finished the most technical section and a change of register tells them "
         "the argument is closing.",
         "“So let me bring everything together.” Then name the five beats. Do not read the three cards."],
        ["<strong>68</strong> · Compress", "3 sentences + 1, 27 s",
         "The three rows are the three contributions; the three verbs on the right are the arc. Say the rows as "
         "sentences and then point at the verbs: explain, scale, guide. Read the takeaway box last, because it is the "
         "sentence you want quoted.",
         "“One cooperative-game definition, three value functions.” Pause after it."],
        ["<strong>69</strong> · Evidence", "3 sentences, 18 s",
         "Publications are credibility, not argument. Map paper to chapter out loud — I to Chapter 5, II to Chapter "
         "6, III to Chapter 7 — say you are first author on all three, and stop.",
         "Do not read the DOIs. Have them ready only if asked."],
        ["<strong>70</strong> · Honesty", "4 sentences, 26 s",
         "Four limitations, said plainly, no hedging. The most valuable clause is the claim-scope one: “a consistent "
         "and productive shared view, not one fully unified framework that removes all tension.”",
         "If you say only one thing here, say that clause. It disarms the hardest question of the whole viva."],
        ["<strong>71</strong> · Agenda", "4 sentences, 30 s",
         "Turn each limitation into a direction and link it plainly: lower-variance estimators address sampling "
         "noise; streaming addresses the static graph; user studies address unmeasured actionability; trustworthy-AI "
         "evaluation extends the governance framing of the introduction.",
         "Present this as a research programme, not a wish list. One clause of justification per direction."],
        ["<strong>72</strong> · The claim", "2 sentences + 4 clauses, 43 s",
         "Read the answer box slowly, once. Then the four outcomes, one clause each. Then the closing line: "
         "“Explanation does not have to remain a description of what happened; it can help us understand, control and "
         "improve AI systems.” Then <em>stop talking</em>.",
         "Two full seconds of silence after the answer box. This is the only slide where a pause is mandatory."],
        ["<strong>73-74</strong> · References", "10 s each",
         "Name the families, not the entries: foundations and baselines on 73, datasets, metrics, regulation and the "
         "team's related work on 74. Nothing more is needed.",
         "These slides exist so that a reference question can be answered from the screen rather than from memory."],
        ["<strong>75</strong> · Courtesy", "2 sentences, 16 s",
         "Thank the jury, offer the three areas — method, theoretical foundations, experimental results — and "
         "state that you will stay on the closing slide for the discussion.",
         "Do not summarise again. The summary happened on 68 and 72."],
        ["<strong>76</strong> · Handover", "nothing spoken",
         "Leave the title slide with the jury table on screen for the whole discussion. It keeps their names visible "
         "and gives you a neutral backdrop while you think.",
         "This is where you answer questions from. Know that slides 77-79 are three keystrokes away."],
    ]

    return """
<section class="sec" id="sec7">
  <div class="sec-head"><div class="sec-kicker">Part four · slides 67-76 · 3.9 min at 130 wpm</div>
  <h2>Section 7: how to present the conclusion</h2>
  <div class="sec-meta"><span class="pill">the only section that is rhetoric, not report</span>
  <span class="pill g">501 spoken words</span><span class="pill o">2 pauses that must be real</span></div></div>

  <p>The conclusion is the only part of the viva where you are not reporting; you are <em>deciding what the jury
  writes down</em>. Sections 1 to 6 build the evidence; section 7 compresses it into three sentences they can
  repeat, states the limits before anyone asks, and puts the answer to the thesis question in their hands. It is
  also the cheapest part of the deck to get wrong, because a conclusion that simply repeats results reads as if you
  did not know what you had proved.</p>

  <div class="callout goal"><h4>The rule for section 7</h4>
  <p><strong>Nothing new appears here.</strong> Every claim in section 7 must already have been earned earlier — the
  synthesis repeats, the limitations were already on slides 36, 49 and 65, the perspectives are the forward
  versions of those limitations, and the thesis answer is the closing of the gap stated on slide 14. If you find
  yourself adding an argument in the conclusion, it belongs in the discussion.</p></div>

  <h3>The five-beat structure, and what each beat is for</h3>
  <div class="tw"><table class="tbl"><thead><tr><th>Beat</th><th>Length</th><th>What it must reach</th>
  <th>Delivery note</th></tr></thead><tbody>
  """ + "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % c for c in r) for r in beats) + """
  </tbody></table></div>

  <h3>Register: four things that must change in your voice</h3>
  <div class="grid2">
    <div class="mini"><h5>1 · Slower</h5>About ten percent slower than section 6, and with shorter sentences. The
    jury is writing their report in these three minutes; give them time to write. A conclusion delivered at the speed
    of a results section produces notes that read like a results section.</div>
    <div class="mini"><h5>2 · Up, not down</h5>In sections 3 to 6 your gaze is partly on the tables. Here it should be
    on the jury, with the slide used as an anchor rather than a script. Slide 68 is the one you may read from; slide
    72 is the one you must say <em>to</em> the room.</div>
    <div class="mini"><h5>3 · Fewer numbers, more structure</h5>The only numbers worth saying in section 7 are the
    three verbs — explain, scale, guide — and the fact that there are three publications. Everything quantitative was
    already delivered; repeating numbers here makes the conclusion sound like a summary of a summary.</div>
    <div class="mini"><h5>4 · First person, past tense for the work, present for the claim</h5>“I showed…”, “the
    thesis argues…”, “this work has…”. Avoid the passive voice here; the jury is evaluating an author, and the
    conclusion is where authorship is audible.</div>
  </div>

  <h3>Two pauses that are part of the content</h3>
  <p><strong>Pause 1, after the answer box on slide 72.</strong> Read the box, then hold two seconds of silence
  before the four outcomes. The silence is what makes the sentence feel like a conclusion rather than a bullet. It
  also lets the jury finish writing it.</p>
  <p><strong>Pause 2, after the last sentence.</strong> The note for slide 72 ends with “Explanation does not have to
  remain a description of what happened; it can help us understand, control and improve AI systems.” Say it, pause,
  and then move to the thanks on slide 75 as a separate, lighter beat. If you run the two together, the closing
  sentence is swallowed by the courtesy.</p>

  <h3>What to say, in the deck's own words</h3>
  <p>The v32 speaker notes for this section are the delivered script, and they are already the right length. The
  three that matter most, quoted so you can keep the wording stable between rehearsal and delivery:</p>
  <div class="callout"><h4>Slide 68 · the arc</h4>
  <p>“This table is the thesis in one view. C1 explains a black-box partition with Shapley attribution. C2 keeps that
  explanation consistent across levels at scale. C3, DyHuCoG, uses attribution as an in-training signal, and improves
  accuracy, coverage and diversity together. Read across the three rows, the same logic moves from post-hoc
  description to in-training guidance: explain, scale, guide.”</p></div>
  <div class="callout"><h4>Slide 70 · the honest clause</h4>
  <p>“…no dedicated user study of actionability. A consistent and productive shared view, not one fully unified
  framework that removes all tension.” Say the second half verbatim; it is the sentence that protects the whole
  thesis from the “is it really one framework?” question.</p></div>
  <div class="callout win"><h4>Slide 72 · the landing</h4>
  <p>“Cooperative game theory can serve as a shared methodological view for actionable explanation across clustering
  and recommendation: the same Shapley logic explains, stays consistent across levels, and guides learning.” Then the
  four outcomes, then the final sentence, then silence.</p></div>

  <h3>Six ways candidates ruin a conclusion — all avoidable here</h3>
  <ol class="steps">
    <li><strong>Re-reading the results.</strong> The jury has just heard them. Repetition inside a conclusion reads as
    padding and burns the seconds you need for the claim.</li>
    <li><strong>Apologising.</strong> “Unfortunately we could not…” turns a limitation into a failure. The deck's
    limitations slides are phrased as boundaries: keep that frame — “the scope of the claim is…”, not “we failed
    to…”</li>
    <li><strong>Promising more than the deck says.</strong> Saying that explanations are “ready for the AI Act” or
    that the method “solves cold start” costs more credibility than any gain it buys. The thesis is careful; the
    speaker must be equally careful.</li>
    <li><strong>Ending on the thanks.</strong> The last scientific sentence must be the answer on slide 72, not
    “thank you for your attention”. The order is: claim, then courtesy.</li>
    <li><strong>Speeding up to save time.</strong> If you are late, cut slides 73 and 74 entirely — ten seconds each
    — and never cut the pauses or slide 72. The conclusion is the last thing the jury hears, and it is what they
    remember when they write.</li>
    <li><strong>Handing over mid-thought.</strong> Finish the final sentence, look at the president, and only then
    say you are ready for questions. Slide 75 to 76 is a handover, not an interruption.</li>
  </ol>

  <h3>The rehearsal protocol for section 7 (20 minutes, three passes)</h3>
  <div class="grid3">
    <div class="stat"><b>Pass 1</b><span>Read slides 68, 70, 71 and 72 aloud with a timer. Target: 2 min 40 s for
    the four beats. Do not stop to fix wording; note where you hesitated.</span></div>
    <div class="stat"><b>Pass 2</b><span>Same four slides, standing, no notes on 72 except the answer box. Insert the
    two mandatory pauses and hold them for a real two seconds.</span></div>
    <div class="stat"><b>Pass 3</b><span>Full run from slide 67 to 76, including the reference slides at speed and the
    handover. Target 3 min 50 s. Then rehearse the first sentence of the discussion: “Thank you — I am ready for your
    questions.”</span></div>
  </div>

  <div class="callout warn"><h4>The three lines to have word-perfect</h4>
  <ul>
    <li>“One cooperative-game definition, three value functions: the same Shapley logic explains a partition, stays
    consistent across levels, and finally guides what a recommender learns.”</li>
    <li>“A consistent and productive shared view, not one fully unified framework that removes all tension.”</li>
    <li>“Explanation does not have to remain a description of what happened; it can help us understand, control and
    improve AI systems.”</li>
  </ul></div>
</section>
"""


# ==========================================================================
# Q&A intro / tactics
# ==========================================================================
def render_qa_intro(qn):
    return """
<section class="sec" id="qa-intro">
  <div class="sec-head"><div class="sec-kicker">Part five</div><h2>The discussion: 100 questions, and how to answer any of them</h2>
  <div class="sec-meta"><span class="pill">__QN__ questions</span><span class="pill g">8 categories</span>
  <span class="pill o">answers written to be spoken in 45-75 seconds</span></div></div>

  <p>Every question below is one a jury member could plausibly ask this thesis: some are certain, some are the
  questions an examiner asks when they want to see how a candidate behaves under pressure. Each answer is written to
  be <em>spoken</em> — one direct answer, one piece of evidence with a number, one boundary — and each is grounded in
  the thesis, the three papers or the deck, never in invention. Answers marked <span class="tag wt">danger</span>
  are the ones where an over-claim would be fatal; read those twice and rehearse the correct phrasing until it is
  automatic.</p>

  <div class="callout goal"><h4>The future-work rule: anything you did not do is future work</h4>
  <p>This is the single most useful piece of advice for the discussion. When the honest answer is “we did not do
  that”, do not defend the gap and do not apologise for it. Do three things instead: <strong>1.</strong> say plainly
  that it is not in the thesis — one sentence, no excuses; <strong>2.</strong> name it as future work;
  <strong>3.</strong> give one sentence of plan: what you would do, or why it is the right next step. Then stop.</p>
  <p>The formula in one line: <em>“That is not in the thesis — it is future work, and my plan is …”</em> A gap
  turned into a plan sounds like a researcher with an agenda. The same gap defended sounds like a hole in the work.
  Three worked conversions:</p>
  <ul>
    <li><strong>No user study of the explanations.</strong> “A user study with domain analysts is future work. The
    thesis measures fidelity and argues actionability; whether analysts really act on the explanations is the next
    experiment, and it is designed.”</li>
    <li><strong>No significance test on Amazon-Book.</strong> “The paired tests are tabulated on MovieLens-1M;
    Amazon-Book is descriptive over five seeds — that scope is stated on slide 59. Extending the full significance
    protocol to Amazon-Book is future work.”</li>
    <li><strong>No streaming or online updates.</strong> “The hypergraph is built offline on the training period;
    online updates are future work, named as such on slide 71.”</li>
    <li><strong>No lower-variance Shapley estimator.</strong> “M = 50 leaves a stated variance of 1.4×10⁻⁵; better
    estimators — stratified sampling, antithetic permutations — are future work, on the slide 71 agenda.”</li>
  </ul>
  <p>Two guard rails. The rule is for things that are <em>not done</em>: never use it to blur something that was
  done imperfectly — that gets its own honest answer. And the three never-claims stay absolute: no significance on
  Amazon-Book, no empirical SHAP-versus-LIME bake-off, no count of sub-clusters. “It is future work” is not a way
  to smuggle those claims in; it is a way to close a gap question in three sentences and move on.</p></div>

  <div class="callout goal"><h4>The three-part answer shape</h4>
  <p><strong>1. Answer.</strong> Say “yes”, “no”, or “within this scope” in the first four words. Juries remember
  evasions, and a delayed answer sounds like a search for an exit. <strong>2. Evidence.</strong> One number, one
  table, one proposition — from memory, or by displaying the slide. <strong>3. Boundary.</strong> The sentence that
  says where the claim stops. This third move is what distinguishes a doctoral answer from a student answer: a
  doctoral candidate knows their scope.</p></div>

  <div class="grid2">
    <div class="mini"><h5>If you know the answer</h5>Answer in the three-part shape, then stop. Do not keep talking
    after the boundary sentence: extra sentences create new attack surface. If the jury wants more,
    they will ask.</div>
    <div class="mini"><h5>If you do not know</h5>Say what you do know, then use the future-work rule: “that
    analysis is not in the thesis; it is future work, and my plan is …” — one sentence of plan, then stop. Never
    invent a number, a citation or an experiment. An honest gap with a plan is a strength; a fabricated result is
    the end of the viva.</div>
    <div class="mini"><h5>If the question is about the statistics</h5>Name the test first — a paired t-test on
    per-user NDCG@20 differences — then the hypotheses, then the Holm correction, then the effect size. Know this
    chain end to end; it is the most likely technical probe of the whole defence. The full drill is in
    <a href="#stats">Statistical tests at a glance</a>.</div>
    <div class="mini"><h5>If the question is ambiguous</h5>Restate it in one sentence — “so the question is whether
    the attribution is stable under a change of surrogate depth” — and answer the restated version. This buys three
    seconds and prevents answering the wrong question, which is worse than not answering.</div>
    <div class="mini"><h5>If the question is hostile</h5>Separate the technical content from the tone: concede the
    part that is true (“you are right that the ablation is not factorial”), then give the boundary and the reason the
    design is nevertheless defensible. Confident concession is the strongest move available.</div>
    <div class="mini"><h5>If you need a slide</h5>Say “let me show you the table”, name the slide, and go to it.
    Slides 77, 78 and 79 exist for exactly this. Announcing the slide is a professional move, not a stall.</div>
    <div class="mini"><h5>If you are interrupted mid-answer</h5>Stop immediately, listen to the new question, and
    answer it. Do not resume the interrupted answer unless asked. Interruption is a signal that the jury has what it
    needs from the first question.</div>
  </div>

  <h3>The twelve questions most likely to be asked, in order of probability</h3>
  <p>Why k = 3 when k = 2 is better (C1) · are you explaining K-Means or the surrogate (C3) · did you run LIME
  (B4) · is Amazon-Book significant (E6) · what does Proposition 6.1 actually prove (B7) · is the gain from Shapley
  or from the other components (E2) · why not more Monte Carlo samples (E3) · why is the wine Silhouette so low and
  where does 0.63 come from (C2) · how did you prevent leakage (F7) · what is the biggest limitation (H1) · what is
  actionable about this (G1) · why is this one thesis (A2). Every one of them has a full answer below.</p>

  <div class="callout warn"><h4>The three things never to say</h4>
  <ul>
    <li>“The experiments show statistical significance on Amazon-Book.” They do not: the paired tests are tabulated
    on MovieLens-1M, and Amazon-Book is reported as a descriptive gain over five seeds.</li>
    <li>“We benchmarked SHAP against LIME on the wine data.” Chapter 5 states the comparison is theoretical and
    literature-backed, not a rerun empirical bake-off.</li>
    <li>“The hierarchy has nine sub-clusters.” No source gives a count of level-2 sub-clusters; the “9” in an early
    draft came from a misreading of nine principal components explaining 97 % of variance.</li>
  </ul></div>

  <div class="callout"><h4>How to use the 100 questions</h4>
  <p>Use the search box in the header to find a term or a slide number, and use the “Expand all answers” button when
  you want to read straight through. If you have one evening before the defence, read the twelve most likely
  questions with their answers, then read every question tagged <span class="tag wt">danger</span>, then skim the
  rest for vocabulary. If you are rehearsing with a colleague, ask them to pick questions at random and time your
  answers at 45 to 75 seconds.</p></div>
</section>
""".replace("__QN__", str(qn))


# ==========================================================================
# CHEAT SHEETS
# ==========================================================================
def render_cheat():
    numbers = [
        ["<strong>Datasets</strong>", "Wine 4,898 × 11 features · Beijing 383,585 hourly records × 11 variables (2013-2017) · "
         "MovieLens-1M 6,040 users / 3,706 items / 1,000,209 interactions / density 0.0447 · "
         "Amazon-Book 52,643 / 91,599 / 2,984,108 / density 0.0006"],
        ["<strong>Clustering</strong>", "Wine k* = 3: Silhouette 0.144, DB 2.097; k = 2: 0.214 / 1.775 (better geometry, not chosen). "
         "Beijing k = 3: Silhouette ≈ 0.63, DB ≈ 0.55. Reference point Gramegna &amp; Giudici 0.37 (positioning, not like-for-like). "
         "Surrogate: 100 trees, 31 leaves, macro-F1 ≈ 0.82 (floor ≈ 0.80)."],
        ["<strong>Wine SHAP ranking</strong>", "density → pH → fixed acidity → sulfur dioxide → alcohol. "
         "Beijing SHAP ranking: temperature, dew point, pressure → CO, NO₂, PM10, PM2.5."],
        ["<strong>DyHuCoG setting</strong>", "α = 0.60 (NDCG@20), β = 0.25 (diversity), γ = 0.15 (context), λ_pref = 0.20, "
         "M = 50 permutations, refresh every 10 batches (≈ 49 per epoch), batch 2048, seeds 42-46, patience 20."],
        ["<strong>Main results, MovieLens-1M</strong>", "NDCG@20 0.2775 vs HPCF 0.2528 (+9.8 %); Recall@20 0.2362 vs 0.2098 (+12.6 %); "
         "Coverage 0.397 vs 0.342 (+16.1 %); ILD 0.516 vs 0.461 (+11.9 %)."],
        ["<strong>Main results, Amazon-Book</strong>", "NDCG@20 0.0306 vs 0.0270 (+13.3 %); Recall@20 0.0417 vs 0.0359 (+16.2 %); "
         "Coverage 0.336 vs 0.259 (+29.7 %); ILD 0.602 vs 0.535 (+12.5 %). <em>Descriptive</em>, not tabulated as significant."],
        ["<strong>Ablation (NDCG@20 drop)</strong>", "Context −8.2 % / −11.0 %; hypergraph −6.8 % / −8.9 %; diversity −5.8 % / −5.8 %; "
         "Shapley −4.6 % / −6.1 %; attention −3.5 % / −3.5 % (MovieLens-1M / Amazon-Book)."],
        ["<strong>Cost</strong>", "Training 2,000 s vs HPCF 1,125 s = 1.78× (Amazon 9,279 s); inference 1.84 ms vs 1.18 ms "
         "(Amazon 8.52 ms); memory 4.4 vs 4.1 GB (Amazon 17.9 vs 16.8 GB). MF baseline ×1.00, DyHuCoG ×3.41."],
        ["<strong>Monte Carlo</strong>", "M = 10: MSE 1.4×10⁻⁴, 95 %, 1.3× · M = 25: 5.6×10⁻⁵, 98 %, 1.6× · "
         "M = 50: 1.4×10⁻⁵, 99 %, 1.78× · M = 100: 3.5×10⁻⁶, 99.5 %, 2.5×. Accuracy is against a high-sample reference."],
        ["<strong>Significance (ML-1M)</strong>", "vs HPCF t = 46.38, p = 1.81×10⁻²⁷⁰, dz = 1.33; vs RecDCL 92.72 / 2.67; "
         "vs HCCF 61.21 / 1.76; vs LightGCN 132.19 / 3.80; vs NCF 311.13 / 8.95; vs MF 341.76 / 9.83. "
         "Holm thresholds 0.0083-0.05; Wilcoxon p &lt; 0.001; df = 6,039."],
        ["<strong>Cold start</strong>", "Users with ≤ 5 training interactions: 0.061 vs 0.055 (+10.9 %); items: 0.057 vs 0.052 (+9.6 %)."],
        ["<strong>Proposition 6.1</strong>", "Φ_parent = Σ w_c′ Φ_child + ε, with w_c′ = |c′| / |c|; ε from surrogate mismatch, "
         "vanishes under perfect fidelity, treated as conceptual (not estimated). Derived from the law of total expectation."],
        ["<strong>Publications</strong>", "Procedia CS 220, 806-811 (2023) DOI 10.1016/j.procs.2023.03.107 · "
         "IJACSA 16(7), 716-725 (2025) DOI 10.14569/IJACSA.2025.0160780 · "
         "IJIES 19(2), 887-902 (2026) DOI 10.22266/ijies2026.0228.54."],
        ["<strong>Hardware</strong>", "Intel Core i9-14900K (24 cores), 48 GB RAM, 2 TB SSD, NVIDIA RTX 4090 24 GB for C3, "
         "Python 3.8, PyTorch 2.0.1."],
    ]

    says = [
        ["<strong>Is the gain from Shapley?</strong>",
         "“It contributes, and the ablation isolates it: −4.6 % on MovieLens-1M and −6.1 % on Amazon-Book when removed.”",
         "“Shapley is the main reason for the improvement.” (Context is the largest single component.)"],
        ["<strong>Is Amazon-Book significant?</strong>",
         "“The paired tests are tabulated on MovieLens-1M; Amazon-Book is a consistent descriptive gain over five seeds, "
         "where the standard deviations are close to the gap.”",
         "“Yes, it is significant.”"],
        ["<strong>Did you compare against LIME?</strong>",
         "“The comparison is theoretical and literature-backed (Chapter 5); LIME is the protocol comparator, not an "
         "empirical bake-off in this thesis.”",
         "“We benchmarked SHAP against LIME on the wine data.”"],
        ["<strong>Are you explaining K-Means?</strong>",
         "“I explain a faithful supervised reconstruction of the partition, with macro-F1 ≈ 0.82 as the validity condition.”",
         "“Yes, the SHAP values explain the K-Means geometry.”"],
        ["<strong>How many sub-clusters?</strong>",
         "“Coarse regimes, then level-2 sub-clusters where appropriate; no count of sub-clusters is reported.”",
         "“Nine sub-clusters.”"],
        ["<strong>Was actionability measured?</strong>",
         "“It is a framing concept, illustrated by the nature of the variables; the user study is future work.”",
         "“We validated that the explanations are actionable.”"],
        ["<strong>Is the k = 3 choice objective?</strong>",
         "“k = 2 is geometrically better (0.214 versus 0.144); k = 3 was chosen on interpretability grounds, and both "
         "criteria are reported.”",
         "“Three is the best number of clusters.”"],
        ["<strong>Which Silhouette is 0.63?</strong>",
         "“Beijing, not wine. Wine is 0.144 at k = 3; Beijing is about 0.63.”",
         "Any sentence that attaches 0.63 to the wine partition."],
        ["<strong>How is the in-training signal validated?</strong>",
         "“By ablation, and by reading the explanation against the objective; a random-weight control is a natural next "
         "experiment and is not reported here.”",
         "“We proved the weights are necessary.”"],
        ["<strong>What is the scope of the framework?</strong>",
         "“A consistent and productive shared view, not one fully unified framework that removes all tension.”",
         "“This is a general theory of explanation and recommendation.”"],
        ["<strong>Any gap: “did you do X?”</strong>",
         "“That is not in the thesis — it is future work, and my plan is …” (one sentence of plan, then stop).",
         "“We could not do it.” / “I forgot.” / a long apology with no plan."],
        ["<strong>Why no confidence intervals?</strong>",
         "“The thesis reports means, standard deviations and Cohen's dz; intervals follow from the same quantities. "
         "Adding them is future work.”",
         "“We did not think of it.” / pretending they are in the thesis."],
    ]

    checklist = [
        ["1", "Jury list", "Confirm the names, roles, grades and institutions on slides 1 and 76 against the official "
         "convocation. The table was inherited from the reference deck and cannot be verified from the documents."],
        ["2", "Slot length", "Confirm whether the 40 minutes include questions. If they do, plan the cut list: slide 13, "
         "slide 24, slides 73-74, slide 69, then compress 29 and 42."],
        ["3", "Pronounce the numbers", "Rehearse aloud: 0.2775, 0.2528, 0.0306, 0.0270, 1.81×10⁻²⁷⁰, 1.4×10⁻⁵, 383,585, "
         "6,040, df 6,039, 1.78×. Numbers mispronounced sound like numbers misunderstood."],
        ["4", "Slide 32 and slide 44 together", "Say both out loud in one breath so the 0.144 (wine) and 0.63 (Beijing) "
         "never swap places."],
        ["5", "Open the backup slides once", "Navigate to 77, 78 and 79 in the actual presentation mode before the "
         "defence, so the keystrokes are automatic."],
        ["6", "Check the fonts render", "The deck uses embedded Roca Two Bold and Nunito. Open it on the defence machine "
         "in PowerPoint, not in a web preview, and check that equations (OMML) display."],
        ["7", "Check the logos and figures", "Slides 7, 33, 45, 46 and 56 use images. Confirm they are present on the "
         "machine you will present from."],
        ["8", "Rehearse the seven transitions", "One sentence each, at the seven section boundaries. They are the "
         "cheapest way to look rehearsed, because they are the moments where a talk usually stumbles."],
        ["9", "Time the last three minutes", "Run slides 67-76 with a timer: target 3 min 50 s, with the two pauses "
         "actually held."],
        ["10", "Prepare the first answer", "The first question is usually about k = 3 or about the surrogate. Have both "
         "answers in the three-part shape and word-perfect."],
        ["11", "Bring a printed A4", "One page: the twelve numbers, the four-sentence statistics drill, the never-say "
         "items, and the question-to-slide "
         "index (77 stability, 78 significance, 79 cost). No slides on paper, just the sheet."],
        ["12", "Decide the ending", "The last spoken sentence of the presentation is the closing line on slide 72, then "
         "the thanks. Never the reverse."],
    ]

    stats_a = [
        ["<strong>Which test</strong>", "Paired samples t-test on per-user NDCG@20 differences: for each user u, "
         "d = NDCG@20_u(DyHuCoG) − NDCG@20_u(baseline). Six comparisons, one per baseline."],
        ["<strong>Why paired</strong>", "The same 6,040 users are scored by both models. Pairing removes the "
         "between-user variance — some users are simply easier to predict — so the test sees only the model "
         "difference. An unpaired test would answer the wrong question."],
        ["<strong>Hypotheses</strong>", "H0: the mean of the differences is zero (no model effect). H1: the mean "
         "difference is not zero — two-sided. The direction of the gain is read from the sign of the mean "
         "difference, not from the choice of tail."],
        ["<strong>Statistic and df</strong>", "t = mean(d) / (sd(d)/√n), df = n − 1 = 6,039 (6,040 users, one "
         "constraint consumed by the estimated mean). Headline row: t = 46.38 versus HPCF."],
        ["<strong>Assumptions</strong>", "1. Differences are independent across users — one row per user. "
         "2. Differences are roughly normal — with n = 6,040 the central limit theorem makes the test robust to "
         "moderate non-normality, and Wilcoxon (no normality assumption) agrees at p < 0.001. "
         "3. NDCG@20 is a bounded continuous score, so its differences are on a usable scale."],
        ["<strong>p-value</strong>", "The probability, assuming H0, of seeing |t| at least this large. Not the "
         "probability that H0 is true; not the size of the gain. With 6,040 users it only separates noise from "
         "signal — which is why effect size is reported next to it."],
        ["<strong>α and multiplicity</strong>", "α = 0.05 per test. Six tests would raise the chance of at least "
         "one false positive well above 5 %; Holm–Bonferroni controls the family-wise error rate at 5 %."],
        ["<strong>Holm step-down</strong>", "Sort the six p-values, compare the k-th with α/(m − k + 1): 0.00833, "
         "0.0100, 0.0125, 0.0167, 0.0250, 0.0500; stop at the first failure. All six comparisons pass (slide 78)."],
        ["<strong>Effect size</strong>", "Cohen's dz = mean(d)/sd(d). Conventional benchmarks: 0.2 small, 0.5 "
         "medium, 0.8 large. The thesis reports dz ≥ 1.33 against every baseline — dz = 1.33 against the "
         "strongest (HPCF)."],
        ["<strong>Robustness check</strong>", "Wilcoxon's signed-rank test, which does not assume normality, "
         "agrees at p < 0.001 on all six comparisons, so the conclusion does not rest on the normality "
         "assumption."],
        ["<strong>What is not tested</strong>", "Amazon-Book and the other metrics are descriptive over five "
         "seeds (±1σ bands, slide 77). The five seeds measure run-to-run noise; the 6,040 users measure "
         "generalisation across users — two different questions, both reported, neither confused with the other."],
        ["<strong>If asked for a confidence interval</strong>", "“The thesis reports means, standard deviations "
         "and dz; a confidence interval follows from the same quantities — mean(d) ± t* · sd(d)/√n. Tabulating "
         "it is future work.” Then stop."],
    ]

    stats_b = [
        ["Why a paired t-test?",
         "Same users, two models: the pairing removes user difficulty and tests only the model difference."],
        ["Why not an unpaired test?",
         "It would mix user-to-user variance into the error term and ask whether two user populations differ — "
         "not the question."],
        ["Are the differences normal?",
         "That is the assumption; with 6,040 users the central limit theorem covers moderate non-normality, and "
         "Wilcoxon agrees at p < 0.001."],
        ["One-tailed or two-tailed?",
         "Two-sided, by convention. The sign of the mean difference gives the direction; the test itself does not."],
        ["What does p = 1.81×10⁻²⁷⁰ mean?",
         "Under no real difference, a t this large would be almost impossible. It is not the probability that "
         "H0 is true, and it says nothing about the size of the gain."],
        ["Why correct for multiplicity?",
         "Six tests at α = 0.05 inflate the chance of a false positive; Holm keeps the family-wise error at 5 % "
         "with only a small loss of power."],
        ["What is a Type I error here?",
         "Declaring DyHuCoG better when the difference is noise. Holm controls the chance of even one such error "
         "across the six comparisons. At n = 6,040 the Type II risk is small."],
        ["What does df = 6,039 mean?",
         "6,040 user differences minus one for the estimated mean; it fixes the exact shape of the t distribution "
         "used for the p-value."],
        ["Why not a z-test, why not bootstrap?",
         "A z-test needs a known standard deviation; with an estimated one, the t distribution is the right "
         "reference. Bootstrap is a fair extra robustness check — future work."],
        ["Why 6,040 and not 5 seeds?",
         "Seeds measure training noise (the ±1σ bands on slide 77); users support the claim about users. The test "
         "is over users, the bands are over seeds."],
        ["What does dz = 1.33 mean?",
         "The average gain is 1.33 standard deviations of the per-user differences — 'large' against the 0.8 "
         "benchmark — and it rides on a +9.8 % relative NDCG@20 gain."],
        ["Is the effect large in practice?",
         "Effect size and relative gain answer together: dz = 1.33 and +9.8 % NDCG@20 over HPCF on MovieLens-1M."],
    ]

    return """
<section class="sec" id="numbers">
  <div class="sec-head"><div class="sec-kicker">Cheat sheet 1</div><h2>Every number in one table</h2>
  <div class="sec-meta"><span class="pill">verified against the thesis and the three papers</span></div></div>
  <p>If you memorise one page from this guide, make it this one. Every value below appears on the slides or in the
  speaker notes and was checked against the thesis or a source paper.</p>
  """ + tbl(["Topic", "The numbers"], numbers) + """
  <div class="callout warn"><h4>Four numbers people confuse</h4>
  <ul>
    <li><strong>0.144 versus 0.63</strong> — wine versus Beijing Silhouette. Never swap them.</li>
    <li><strong>+9.8 % versus +13.3 %</strong> — relative NDCG@20 gain on MovieLens-1M versus Amazon-Book.</li>
    <li><strong>−4.6 % versus −8.2 %</strong> — removing Shapley weighting versus removing context (MovieLens-1M).</li>
    <li><strong>M = 25 versus M = 50</strong> — 98 % versus 99 % agreement with the high-sample reference; 50 is the default.</li>
  </ul></div>
</section>

<section class="sec" id="stats">
  <div class="sec-head"><div class="sec-kicker">Cheat sheet 2</div><h2>Statistical tests at a glance</h2>
  <div class="sec-meta"><span class="pill">know this end to end</span><span class="pill o">the most likely technical probe</span></div></div>
  <p>Your supervisor is right: expect the jury to probe the statistics. The whole defence rests on one test — the
  paired t-test on slides 62 and 78 — plus one correction and one effect size. Below is the full chain, then the
  one-breath answers to the questions examiners actually ask. Rehearse the four-sentence drill until it is
  automatic: <em>name the test, give the hypotheses, give the statistic with its degrees of freedom, give the
  correction and the effect size.</em></p>
  """ + tbl(["Item", "What you must be able to say"], stats_a) + """
  <h3>If the jury probes the statistics</h3>
  """ + tbl(["Question", "Answer in one breath"], stats_b) + """
  <div class="callout warn"><h4>The four-sentence drill</h4>
  <p>“The comparison is a <strong>paired t-test</strong> on per-user NDCG@20 differences across 6,040 users. The
  null hypothesis is that the mean difference is zero; the alternative is that it is not. The statistic is
  t = 46.38 with 6,039 degrees of freedom, and the six baseline comparisons are corrected with Holm–Bonferroni.
  The effect size is Cohen's dz = 1.33 — large by the standard benchmarks.” Then stop.</p></div>
</section>

<section class="sec" id="never">
  <div class="sec-head"><div class="sec-kicker">Cheat sheet 3</div><h2>Never say / always say</h2>
  <div class="sec-meta"><span class="pill o">scope fences</span><span class="pill g">rehearse the right-hand column</span></div></div>
  <p>These are not style preferences. Each left-hand formulation is wider than the thesis, and a jury member who has
  read Chapter 5, 6 or 7 can falsify it in one sentence. The right-hand version is equally strong and defensible.</p>
  """ + tbl(["If the thought is…", "Say this", "Never say this"], says) + """
</section>

<section class="sec" id="checklist">
  <div class="sec-head"><div class="sec-kicker">Cheat sheet 4</div><h2>Pre-defence checklist</h2>
  <div class="sec-meta"><span class="pill">twelve items</span><span class="pill g">technical and rhetorical</span></div></div>
  """ + tbl(["#", "Item", "What to do"], checklist) + """
  <div class="callout win"><h4>The one-sentence summary of this whole guide</h4>
  <p>Present the deck as it is written, keep the three scope fences intact — significance on MovieLens-1M, the LIME
  comparison theoretical, no count of sub-clusters — volunteer every limitation before it is requested, and end the
  presentation on the thesis answer rather than on the thanks. A candidate who knows exactly where their claim stops
  is harder to challenge than one who claims more.</p></div>
</section>
"""
