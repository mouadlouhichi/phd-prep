# -*- coding: utf-8 -*-
"""Deck map, timing ledger, sidebar and section playbooks 0-3 (slides 1-25)."""

PANES_PLACEHOLDER = [
    {"id": "map", "label": "Deck map & timing"},
    {"id": "sections", "label": "Section playbooks 0-7"},
    {"id": "tech", "label": "Technical deep dive"},
    {"id": "sec7", "label": "Section 7 delivery plan"},
    {"id": "qa", "label": "Q&A · 100 questions"},
    {"id": "cheat", "label": "Cheat sheets"},
]

SIDEBAR = [
    ("Start here", [
        ("overview", "The deck in one page"),
        ("timing", "Timing ledger & checkpoints"),
        ("anatomy", "How every section is built"),
        ("rules", "Ten delivery rules"),
    ]),
    ("Section playbooks", [
        ("sec-title-and-outline", "Title + Outline · slides 1-2"),
        ("sec-introduction", "1 · Introduction · 3-7"),
        ("sec-context-problematic", "2 · Context & Problematic · 8-16"),
        ("sec-protocol", "3 · Experimental Protocol · 17-25"),
        ("sec-contribution-i", "4 · Contribution I · 26-37"),
        ("sec-contribution-ii", "5 · Contribution II · 38-50"),
        ("sec-contribution-iii", "6 · Contribution III · 51-66"),
        ("sec-conclusion", "7 · Conclusion · 67-76"),
        ("sec-discussion", "Q&A stage + backup · 75-79"),
    ]),
    ("Technical deep dive (sections 3-6)", [
        ("walk", "Twelve concept walkthroughs"),
        ("glossary", "Beginner glossary"),
    ]),
    ("Section 7", [("sec7", "How to present the conclusion")]),
    ("Q&A", [
        ("qa-intro", "How to handle the discussion"),
        ("qa-framing", "A · Framing & contribution"),
        ("qa-game", "B · Cooperative game theory"),
        ("qa-c1", "C · Contribution I"),
        ("qa-c2", "D · Contribution II"),
        ("qa-c3", "E · Contribution III"),
        ("qa-method", "F · Protocol, metrics, statistics"),
        ("qa-ethics", "G · Ethics, regulation, actionability"),
        ("qa-limits", "H · Limitations & future work"),
    ]),
    ("Cheat sheets", [
        ("numbers", "Every number in one table"),
        ("never", "Never say / always say"),
        ("checklist", "Pre-defence checklist"),
    ]),
]


def render_hero():
    return """
<div class="hero" id="overview">
  <h1>How to present this viva, and how to defend every line of it</h1>
  <p class="sub">A complete reading of <code>MOUAD_LOUHICHI_VIVA_40min_BeigeGreen_v28.pptx</code> (79 slides),
  its 4,584 spoken words, its speaker notes, the thesis it defends and the three papers behind it.</p>
  <div class="meta">
    <span class="pill o">4,584 spoken words in the main flow</span>
    <span class="pill">≈ 35.3 min at 130 wpm</span>
    <span class="pill">≈ 38.2 min at 120 wpm</span>
    <span class="pill g">7 sections + Q&amp;A + 3 backup tables</span>
    <span class="pill g">3 contributions · 5 research questions</span>
  </div>
  <p>This guide has four jobs. <strong>First</strong>, it explains what each of the seven sections is doing, and how
  to deliver every one of the 79 slides: what is on screen, what to say, what to point at, how long it takes, and
  where the risks are. <strong>Second</strong>, it gives sections 3, 4, 5 and 6 — the shared protocol, the two
  clustering contributions and DyHuCoG — a beginner-level technical deep dive: every term, every formula, every
  result, explained from first principles so you can defend the substance and not only the slides.
  <strong>Third</strong>, it gives section 7 its own presentation plan, because a conclusion is delivered
  differently from a results section. <strong>Fourth</strong>, it proposes 100 likely jury questions with
  dissertation-level answers, each one written to be spoken.</p>
  <div class="legend">
    <div><b>If you have 20 minutes before the defence</b>Read “Ten delivery rules”, the timing ledger, and the
    “Never say / always say” sheet. Then rehearse the seven transitions.</div>
    <div><b>If you have two hours</b>Add the section playbooks for 3, 4, 5 and 6, and the eight walkthroughs.</div>
    <div><b>If a jury member is a game theorist</b>Read glossary 43-54 and questions B1-B14, then Q021-Q026.</div>
    <div><b>If a jury member is an applied ML researcher</b>Read the walkthroughs on SHAP, the surrogate bridge and
    the statistics, then questions C1-C14 and F1-F15.</div>
  </div>
</div>
"""


def render_deckmap():
    rows = [
        ["1-2", "Title slide with the jury table + Outline", "2", "161", "1.2", "1.3"],
        ["3-7", "<strong>1 · Introduction</strong> — motivation, actionable insight, research context", "5", "405", "3.1", "3.4"],
        ["8-16", "<strong>2 · Context &amp; Problematic</strong> — four approaches, limitations, RQ1-RQ5", "9", "682", "5.2", "5.7"],
        ["17-25", "<strong>3 · Experimental Protocol</strong> — datasets, splits, baselines, metrics, hardware", "9", "503", "3.9", "4.2"],
        ["26-37", "<strong>4 · Contribution I</strong> — explainable black-box clustering (wine)", "12", "730", "5.6", "6.1"],
        ["38-50", "<strong>5 · Contribution II</strong> — multi-level XAI at scale (Beijing)", "13", "631", "4.9", "5.3"],
        ["51-66", "<strong>6 · Contribution III</strong> — DyHuCoG, the in-training signal", "16", "971", "7.5", "8.1"],
        ["67-76", "<strong>7 · Conclusion &amp; Perspectives</strong> — synthesis, publications, limits, answer", "10", "501", "3.9", "4.2"],
        ["<strong>1-76</strong>", "<strong>Main flow, spoken</strong>", "<strong>76</strong>", "<strong>4,584</strong>", "<strong>35.3</strong>", "<strong>38.2</strong>"],
        ["77-79", "Backup tables (7.1 with ± std, 7.6 paired tests, 7.3 + 7.4 cost and convergence)", "3", "45 (not spoken)", "—", "—"],
    ]
    t = ('<div class="tw"><table class="tbl"><thead><tr><th>Slides</th><th>Block</th><th>#</th>'
         '<th>Spoken words</th><th>Min @130</th><th>Min @120</th></tr></thead><tbody>')
    for r in rows:
        t += "<tr>" + "".join("<td>%s</td>" % c for c in r) + "</tr>"
    t += "</tbody></table></div>"

    ck = [
        ["Slide 3 (start of §1)", "minute 1", "1.2 min", "on time"],
        ["Slide 8 (start of §2)", "about minute 5", "4.4 min", "slightly early — the cue is generous, use the margin"],
        ["Slide 17 (start of §3)", "about minute 10", "9.6 min", "on time"],
        ["Slide 26 (start of §4)", "about minute 14", "13.5 min", "on time"],
        ["Slide 38 (start of §5)", "about minute 20", "19.1 min", "on time"],
        ["Slide 51 (start of §6)", "about minute 26", "23.9 min", "cue is 2 min conservative — you have built-in slack"],
        ["Slide 67 (start of §7)", "about minute 34", "31.4 min", "2.5 min of buffer here: that is your safety margin"],
        ["Slide 75/76 (end)", "—", "≈ 35.3 min", "≈ 4.7 min in hand inside a 40-minute slot"],
    ]
    ck_t = ('<div class="tw"><table class="tbl"><thead><tr><th>Checkpoint</th><th>Cue on the deck</th>'
            '<th>Planned cumulative time @130 wpm</th><th>Reading</th></tr></thead><tbody>')
    for r in ck:
        ck_t += "<tr>" + "".join("<td>%s</td>" % c for c in r) + "</tr>"
    ck_t += "</tbody></table></div>"

    return """
<section class="sec" id="timing">
  <div class="sec-head"><div class="sec-kicker">Orientation</div><h2>The deck at a glance, and the timing ledger</h2>
  <div class="sec-meta"><span class="pill">79 slides</span><span class="pill g">76 spoken + 3 backup</span>
  <span class="pill o">4,584 words = 35.3 min</span></div></div>
  <p>Every word count below was measured from the speaker notes actually stored in the v28 file, excluding the
  seven <em>Time check</em> cues and the two pre-defence reminder lines, which are not spoken. The deck therefore
  fits a 40-minute slot with about four and a half minutes in hand at a normal 130 words per minute, or about one and
  a half minutes at 120 wpm. If the 40 minutes include the jury's questions, you are 5 to 10 minutes over and should
  use the cut list at the end of this page.</p>
  """ + t + """
  <h3>The seven time-check cues, verified</h3>
  <p>The notes on slides 3, 8, 17, 26, 38, 51 and 67 carry a spoken cue. Here is what each cue means against the
  measured script, so you know on the day whether you are ahead or behind.</p>
  """ + ck_t + """
  <div class="callout win"><h4>The one number to remember</h4>
  <p>At the start of section 7 you should be at about <strong>31 to 32 minutes</strong>, with the cue saying
  “about minute thirty-four”. That gap is deliberate: the cue is a warning line, not a target. If you hear yourself
  at the conclusion divider and you are past minute 34, you have lost the buffer and should compress slides 68-72
  by reading only the takeaway box on each.</p></div>

  <h3>How to spend a 40-minute slot, in four plans</h3>
  <div class="grid2">
    <div class="mini"><h5>Plan A · 40 minutes including questions</h5>Speak 30 minutes, keep 10 for the jury.
    Cut, in this order: slide 13 (limits of classical recommenders, 50 words), slide 24 (metrics table, 45 words),
    slide 73 and 74 (references, 83 words), slide 69 (publications table, 39 words), then trim slide 29 (band example)
    and slide 42 (Proposition 6.1) to their takeaway boxes. That is ≈ 4.5 min of text plus the presentation of
    tables that needs no narration.</div>
    <div class="mini"><h5>Plan B · 40 minutes of presentation only</h5>Deliver the deck as written, at a measured
    pace, and land at 35-36 minutes. Use the remaining minutes for a transition sentence between sections and for
    pointing at the table you just described instead of talking over it.</div>
    <div class="mini"><h5>Plan C · 30 minutes</h5>Keep every section but halve the per-slide commentary:
    slide 4 (three motivation questions), slide 12 (graph and hypergraph families), slide 22 (splits), slide 29
    (band example), slide 46 (cross-level change), slide 55 (Monte Carlo), slide 60 (ablation) and slide 68
    (synthesis) are the eight slides worth the most words; the rest can be one sentence each.</div>
    <div class="mini"><h5>Plan D · Questions go badly</h5>If the jury interrupts early, the deck still works in
    fragments: every contribution is built as gap → objectives → method → protocol → results → answer → findings →
    limitations → takeaway, so you can jump to any contribution's “Answer to RQ” slide and the story closes.</div>
  </div>

  <div class="callout warn"><h4>The three things you must not do with timing</h4>
  <ul>
    <li>Do not read the tables aloud cell by cell. Read the row that matters, name the comparison, move on.</li>
    <li>Do not skip the limitations slides to save time. They are the cheapest credibility you have, and juries
    test them (questions H1-H6).</li>
    <li>Do not abandon a cue because you are ahead. Cues tell you to speed up or slow down; the buffer before
    section 7 is intentional.</li>
  </ul></div>
</section>

<section class="sec" id="anatomy">
  <div class="sec-head"><div class="sec-kicker">Structure</div><h2>How every contribution is built (the same spine, three times)</h2></div>
  <p>The three contributions use one repeatable spine, which is why the deck feels calm even though it carries
  three datasets, six baselines and forty numbers. Learn the spine and you can find your place from any slide.</p>
  <div class="tw"><table class="tbl"><thead><tr><th>Beat</th><th>C1 (26-37)</th><th>C2 (38-50)</th><th>C3 (51-66)</th><th>What it must do on the day</th></tr></thead><tbody>
  <tr><td><strong>Divider</strong></td><td>26</td><td>38</td><td>51</td><td>Name the contribution, its RQ, and the one-line result. Do not read the three bullets.</td></tr>
  <tr><td><strong>Research gap</strong></td><td>27</td><td>39</td><td>52</td><td>State what the literature does not have, in one sentence, then read the orange gap box.</td></tr>
  <tr><td><strong>RQ + objectives</strong></td><td>28</td><td>40</td><td>53</td><td>Give the objective table as three promises. The jury will check them later, so say them cleanly.</td></tr>
  <tr><td><strong>Method</strong></td><td>29-30</td><td>41-42</td><td>54-56</td><td>The only part that is genuinely technical: players, value function, pipeline, aggregation.</td></tr>
  <tr><td><strong>Protocol</strong></td><td>31-32</td><td>43</td><td>57</td><td>One slide of settings. Signal that the details are in Chapter 4 and move on.</td></tr>
  <tr><td><strong>Results</strong></td><td>33</td><td>44-46</td><td>58-62</td><td>Point at the figure or the bold row; give the number and the reading, never the whole table.</td></tr>
  <tr><td><strong>Answer to the RQ</strong></td><td>34</td><td>47</td><td>63</td><td>Say “Yes”, then the one condition that limits the yes.</td></tr>
  <tr><td><strong>Findings</strong></td><td>35</td><td>48</td><td>64</td><td>Four numbered findings: the jury may quote these back to you.</td></tr>
  <tr><td><strong>Limitations</strong></td><td>36</td><td>49</td><td>65</td><td>Volunteer them before you are asked. This is where trust is bought.</td></tr>
  <tr><td><strong>Takeaway</strong></td><td>37</td><td>50</td><td>66</td><td>One sentence, plus the bridge to the next contribution.</td></tr>
  </tbody></table></div>
  <div class="callout"><h4>Why this matters for delivery</h4>
  <p>Because the spine repeats, the jury learns your rhythm by slide 34 and stops needing orientation. That means the
  two things you must never improvise are the <em>answer slides</em> and the <em>limitation slides</em>: those are the
  anchors they will remember when they write their report.</p></div>
</section>

<section class="sec" id="rules">
  <div class="sec-head"><div class="sec-kicker">Delivery</div><h2>Ten delivery rules for this deck</h2></div>
  <div class="steps-wrap"><ol class="steps">
  <li><strong>Say the number, then the meaning.</strong> “NDCG@20 goes from 0.2528 to 0.2775, about ten percent” —
  number first, interpretation second. Never leave a number uninterpreted, never interpret one you have not said.</li>
  <li><strong>Point, then speak.</strong> The tables and figures are dense; name the column, the row, the colour,
  then give the sentence. Silence while you point is fine and reads as control.</li>
  <li><strong>One idea per slide, one transition per section.</strong> The transitions are written for you in each
  playbook below; say them out loud in rehearsal.</li>
  <li><strong>Never read a bullet verbatim.</strong> The slide already says it. Say the consequence of it, or the
  evidence for it, or the caveat on it.</li>
  <li><strong>Volunteer the limitation before the jury asks.</strong> Every contribution has its own limitation
  slide; use the sentence “this is the honest boundary of the claim” and stop there.</li>
  <li><strong>Keep the three scope fences.</strong> Significance is tabulated on MovieLens-1M; the SHAP-versus-LIME
  comparison is theoretical; the hierarchy has coarse regimes then sub-clusters with no published count.</li>
  <li><strong>Give the jury a landing place.</strong> Every results slide ends with what the result means, not with
  the last table cell.</li>
  <li><strong>Slow down on the four most technical slides</strong> (29, 42, 54, 55). Those are the ones where a
  jury member decides whether you understand your own mathematics.</li>
  <li><strong>Treat the backup slides as instruments.</strong> Slides 77-79 are not decoration: if someone asks about
  stability, significance or cost, you can show the exact table instead of paraphrasing it.</li>
  <li><strong>End on the claim, not on the thanks.</strong> The last spoken sentence of the presentation should be
  the thesis answer on slide 72. Slide 75 is the handshake; slide 76 stays up for the discussion.</li>
  </ol></div>
</section>
"""


def render_sections_intro():
    return """
<section class="sec" id="sections-intro">
  <div class="sec-head"><div class="sec-kicker">Part two</div><h2>Section playbooks · how to present slides 1 to 79</h2>
  <div class="sec-meta"><span class="pill">7 sections</span><span class="pill g">every slide covered</span>
  <span class="pill o">time, content, delivery, risk</span></div></div>
  <p>Each section below opens with what that section must achieve in front of the jury, then gives a row for every
  slide: what the jury sees, how to present it, the measured speaking time, and the cue or the risk attached to that
  slide. The times are computed from the v28 speaker notes at 130 words per minute, which is a normal academic
  delivery pace; add roughly 8 percent if you speak at 120 wpm.</p>
  <div class="callout"><h4>How to read a “How to present it” cell</h4>
  <p>The cell is not a script; the speaker notes in the deck are the script. The cell tells you the <em>intention</em>
  of the slide — what the jury should be able to say back to you after it — and the delivery move that makes that
  happen. Where the deck already contains a good sentence, the cell quotes it so you can keep the wording consistent
  between the screen and your voice.</p></div>
</section>
"""


def render_sidebar():
    out = []
    for group, items in SIDEBAR:
        out.append("<h5>%s</h5>" % group)
        for anchor, label in items:
            out.append('<a href="#%s">%s</a>' % (anchor, label))
    return "\n".join(out)


# --------------------------------------------------------------------------
# Section 0: title + outline
# --------------------------------------------------------------------------
S0 = {
    "id": "title-and-outline",
    "kicker": "Slides 1-2 · 1.2 min",
    "title": "Title slide and outline",
    "range": "1-2",
    "words": "161",
    "m130": "1.2",
    "m120": "1.3",
    "search": "title slide jury outline presentation opening speech",
    "purpose": """
- Establish, in about seventy seconds, who you are, what the thesis is called, and the one idea the jury should carry into the whole presentation.
- Make the jury table and the supervisor visible so that the formal part of the defence is done before the science starts.
- Give the plan in seven parts, so that later, when you say “this is section five”, the jury already knows where they are.
""",
    "arc": [
        ("The opening is a speech, not a slide read", "Slides 1 and 2 carry the candidate's own delivered opening. "
         "Say it as written in the notes: greeting, name, title, one-sentence claim, then the plan. Do not add a "
         "second greeting, and do not thank the jury twice."),
        ("The one-sentence claim is the whole thesis", "“Shapley attribution is not only a method to explain a model "
         "after it has been trained: it can be one framework that explains black-box models, stays consistent across "
         "levels of detail, and guides how recommenders learn.” Every later section is an instance of that sentence. "
         "Deliver it slowly, then pause."),
    ],
    "slides": [
        {"n": "1", "title": "Title, jury, supervisor",
         "screen": "Title in full, presenter and supervisor cards, the nine-member jury table, Rabat 2026.",
         "how": "Greet the president and the jury, give your name, then read the title **as the slide has it**: "
                "“Cooperative Game Theory for Explainable Artificial Intelligence in Recommendation Systems”, with "
                "the subtitle “A Shapley Framework for Actionable Insight”. Then state the claim: attribution is not "
                "only a post-hoc tool; here it explains, scales, and guides learning. Do not read the jury table aloud. "
                "One glance at the president and a nod is enough.",
         "time": "≈ 50 s", "cue": "Pre-defence check: confirm the jury names against the official convocation. The table "
                                  "was inherited from the reference deck and cannot be verified from the documents."},
        {"n": "2", "title": "Outline",
         "screen": "Seven numbered parts plus Q&amp;A, each with a one-line description.",
         "how": "Walk the seven parts in one breath each: introduction, problem, protocol, three contributions, "
                "conclusion. Then say the sentence that buys you the right to a uniform structure: each contribution "
                "follows the same path, gap → objectives → methodology → protocol → results → findings. Finish with "
                "“the next thirty-six minutes” as the note says. Do not describe the Q&amp;A block, just name it.",
         "time": "≈ 25 s", "cue": "The note says “the next 36 minutes”, which matches the measured 35.3 min at 130 wpm. "
                                  "If you know you speak faster, say “about half an hour”."},
    ],
    "extra": [
        ("Delivery notes that actually matter here",
         "Stand still for slide 1, both hands free, no pointer. The jury is forming a first impression of composure, "
         "not of content. On slide 2, use your hand to count the seven parts — it gives the jury a visual index and "
         "gives you a rhythm. If a jury member is still settling, wait. Starting late costs nothing; restarting costs "
         "credibility."),
    ],
    "transition": "“Let me start with why this question matters.”",
}


# --------------------------------------------------------------------------
# Section 1: Introduction (3-7)
# --------------------------------------------------------------------------
S1 = {
    "id": "introduction",
    "kicker": "Section 1 · slides 3-7 · 3.1 min",
    "title": "Introduction: the motivation and the definition",
    "range": "3-7",
    "words": "405",
    "m130": "3.1",
    "m120": "3.4",
    "search": "introduction motivation actionable insight research context black box Netflix Spotify Amazon Yelp",
    "purpose": """
- Move the jury from “recommenders are everywhere” to “and their reasoning is hidden, which is a governance problem as well as a technical one”.
- Install <strong>Definition 1.1</strong> — the definition of an actionable explanation — because every later claim is measured against it.
- Show the historical arc of recommenders so that the loss of transparency looks like a structural consequence of progress, not an accident.
""",
    "arc": [
        ("One definition carries the whole thesis", "Actionable means two things only: the explanation names a factor "
         "that someone can actually change, and it speaks the language of the domain (acidity in wine, pollution "
         "indicators in air, preferences in recommendation). Say both halves; juries remember definitions that come in "
         "two halves."),
        ("Be precise about the regulation", "The deck says high-risk systems have transparency duties under the AI Act "
         "(Art. 13) and that decisions can be challenged (Art. 86). Do not upgrade this into “the AI Act requires "
         "explanations for everything”, which is what a well-informed jury member will attack."),
    ],
    "slides": [
        {"n": "3", "title": "Introduction divider",
         "screen": "Section number 01, four cards: motivation, actionable insight, research context.",
         "how": "Open with the framing question: why has explainability become a core requirement for recommendation? "
                "Give the arc in one sentence: systems that decide what billions of people see, buy and watch are "
                "accurate but not transparent. Say the first time-check cue without drama: “time check: minute one”.",
         "time": "≈ 17 s", "cue": "Cue 1. Keep it. It tells the jury that you manage your slot, which is itself a signal of preparation."},
        {"n": "4", "title": "Motivation: Three Questions",
         "screen": "Three cards — Everywhere, The Black Box, Toward Trust — plus the tension strip.",
         "how": "This is the most spoken slide of the section (105 words) and it deserves it: read the three questions "
                "as three questions, with a small pause after each. Land on the tension sentence: as models gain power "
                "they lose transparency, and this thesis refuses the trade-off. Do not read the card subtitles.",
         "time": "≈ 48 s", "cue": "The “&#36;15B by 2029” market number was removed in v26 because it could not be sourced. Do not reintroduce it from memory or from an older deck."},
        {"n": "5", "title": "Actionable Insight: the Definition",
         "screen": "Definition 1.1 in three blocks: what we can change, the language of the domain, why it matters.",
         "how": "Read the definition once, slowly, then give the three domains that instantiate it: acidity in wine, "
                "pollution indicators in air, user preferences in recommendation. Close with the operational sentence: "
                "a good explanation tells us what to change to improve the outcome. This slide is quoted back to you "
                "later (question G1-G4), so the wording must be identical every time.",
         "time": "≈ 35 s", "cue": "Do not claim that actionability was measured. It is a framing concept in this thesis; the user study is future work (slide 70)."},
        {"n": "6", "title": "Research Context",
         "screen": "Evolution timeline: similarity models → matrix factorisation → neural CF → graph CNN → hypergraph, plus the two blocks “Why the gap matters” and “What this thesis argues”.",
         "how": "Walk the timeline with your hand, one step per generation, and say the same clause each time: each step "
                "improved ranking and hid more of the reasoning. Then the three reasons the gap matters (trust, "
                "debugging, regulation) and the three claims of the thesis (attribution inside the model, consistent "
                "across levels, domain language). The note for this slide is deliberately in spoken register; keep it.",
         "time": "≈ 61 s", "cue": "This slide and its note say the same three things three times. Nothing on screen is left unsaid, and nothing said is missing from the screen — that symmetry is the point."},
        {"n": "7", "title": "AI-Powered Recommendation Is Everywhere",
         "screen": "Four platform cards — Netflix, Spotify, Yelp, Amazon — with logos.",
         "how": "Fast slide, about 25 seconds. Name the four and give the shared punchline: everywhere, and hidden. "
                "Do not explain what Netflix is; the jury knows. The rhetorical job of this slide is scale, so the only "
                "word that matters is “everywhere”.",
         "time": "≈ 25 s", "cue": "If a logo fails to render in the room's PowerPoint, the text chips still carry the slide. Do not stop to fix it."},
    ],
    "extra": [
        ("The three sentences to rehearse until they are automatic",
         "“An explanation is actionable when it points to something we can actually change, and changing it clearly "
         "affects the model output.” · “Each step improved ranking and hid more of the reasoning.” · “This thesis "
         "argues that attribution belongs inside the model, not added on afterwards.” These three lines carry section 1; "
         "everything else on slides 3-7 supports them."),
    ],
    "transition": "“That is the motivation. Now the research problem itself: what the main approaches can do, and where each one stops.”",
}


# --------------------------------------------------------------------------
# Section 2: Context and problematic (8-16)
# --------------------------------------------------------------------------
S2 = {
    "id": "context-problematic",
    "kicker": "Section 2 · slides 8-16 · 5.2 min",
    "title": "Context &amp; Problematic: four families, four limits, five questions",
    "range": "8-16",
    "words": "682",
    "m130": "5.2",
    "m120": "5.7",
    "search": "context problematic content-based collaborative filtering hybrid matrix factorisation graph hypergraph limitations research questions",
    "purpose": """
- Give the jury a taxonomy they can argue with: four recommender families, each stronger and each less transparent.
- State the three structural limitations — explainability, scaling, integration into learning — as the problem statement of the thesis.
- Fix the five research questions in the jury's mind, mapped to the three contributions, so that every later “Answer to RQ” slide lands on a question they already hold.
""",
    "arc": [
        ("Four slides, one pattern per family", "Slides 9-12 each describe one family with four bullets and one "
         "limitation box. Deliver them with the same rhythm: principle, mechanism, strength, limitation. The repetition "
         "is the argument: transparency decreases monotonically."),
        ("The gap statement is the pivot of the whole viva", "Slide 14's orange box is the sentence the jury will test "
         "against everything you show later: “no single cooperative-attribution framework that explains clustering "
         "faithfully, stays consistent across levels, and then works as an in-training signal in recommendation.” "
         "Read it as three claims, with a pause between them. Those three claims are exactly C1, C2, C3."),
    ],
    "slides": [
        {"n": "8", "title": "Context &amp; Problematic divider",
         "screen": "Section 02 with three cards: approaches, problematic, contributions.",
         "how": "Announce the plan for the section: the main approaches, then their limitations, then the five research "
                "questions and the three contributions that answer them. Say the time-check cue: about minute five.",
         "time": "≈ 15 s", "cue": "Cue 2. Measured arrival here is 4.4 min, so you have half a minute in hand — spend it on slide 12 if the jury looks engaged there."},
        {"n": "9", "title": "Content-Based Filtering",
         "screen": "Four bullets — features and past preferences, user profile, similar items, explainable by construction — plus the limitation box.",
         "how": "This is the only family the thesis calls explainable by construction, so say it plainly: the reason is "
                "a named feature the user recognises. Then the limitation: over-specialisation and dependence on rich "
                "metadata. This slide matters later, because it sets the bar that SHAP has to clear in an unsupervised "
                "setting.",
         "time": "≈ 34 s", "cue": "Do not let this slide drift into a tutorial on TF-IDF or embeddings. The jury needs the trade-off, not the implementation."},
        {"n": "10", "title": "Collaborative Filtering",
         "screen": "Four bullets — similar users, interaction patterns, user- or item-based, foundation of MF and graph models — plus the cold-start limitation.",
         "how": "Emphasise that no item content is needed, which is exactly why the method scales and exactly why it "
                "cannot explain itself in words a user owns. Name cold start as the limitation the thesis returns to on "
                "slide 64 with the +10.9 % / +9.6 % cold-start gains.",
         "time": "≈ 30 s", "cue": "Cold start is a question magnet. Have the numbers ready: user 0.061 vs 0.055, item 0.057 vs 0.052."},
        {"n": "11", "title": "Hybrid Approaches and Matrix Factorisation",
         "screen": "Hybrid combination, then MF with R = P·Q, then the limitation: latent factors are hidden.",
         "how": "Use the formula as the hinge: the interaction matrix is split into user and item factors, which is "
                "accurate and scalable, but a score cannot be traced to a factor a person understands. Say the phrase "
                "“the gap between accuracy and interpretability becomes stronger here” — it is the sentence that "
                "justifies the next slide.",
         "time": "≈ 32 s", "cue": "Do not attempt to explain matrix factorisation mathematics here; the glossary in this guide has the version you need if asked."},
        {"n": "12", "title": "Graph-Based and Hypergraph Recommenders",
         "screen": "Nodes and edges, message passing (LightGCN, HCCF, HPCF), hyperedges connecting user, item and context, state of the art on sparse benchmarks, and the limitation: compute, memory, uniform unexplained messages.",
         "how": "This is the most spoken slide of the section (119 words) and the most important one: the thesis is "
                "built on this family. Deliver it in three beats — graphs, hypergraphs, the price. The price is the "
                "research opportunity: every message is treated as equally important, so which relationships mattered "
                "stays hidden.",
         "time": "≈ 55 s", "cue": "If the jury is technical, this is where they will start taking notes. Be exact: hyperedges connect more than two nodes, which is what makes context expressible."},
        {"n": "13", "title": "Limitations of Classical Recommenders &amp; Unsupervised Models",
         "screen": "Four numbered limits — sparsity and scalability, cold start, popularity bias and diversity, absence of interpretability — plus the clustering paragraph and the gap box.",
         "how": "Keep it brisk: four numbers, four sentences. Then shift register for the clustering part, which is "
                "about a different literature: methods give a local OR a global explanation, not both, and they rarely "
                "stay consistent across levels. Close on the gap sentence.",
         "time": "≈ 23 s", "cue": "This is the first slide to cut if you are behind. Its content reappears on slide 14 with sharper wording."},
        {"n": "14", "title": "Three Main Limitations: Problem Statement",
         "screen": "Three numbered cards — lack of explainability, difficulty of scaling, weak integration into learning — and the THESIS GAP box.",
         "how": "This is the pivot of the viva. Say the three limitations as three separate claims, each with its own "
                "consequence, then read the orange box word by word: “explains clustering faithfully, stays consistent "
                "across levels, and then works as an in-training signal in recommendation.” Pause. Then the claim: "
                "Shapley attribution can be that framework. Everything that follows is evidence for that sentence.",
         "time": "≈ 49 s", "cue": "Point at the box and physically hold the pause. This is the slide a jury member will photograph with their memory."},
        {"n": "15", "title": "Research Questions (RQ1-RQ5) and Overall Aim",
         "screen": "Aim strip, then five RQ cards with an arrow to C1, C2, C3 or the thesis.",
         "how": "Read the five questions as questions, not as labels. Group them while you speak: RQ1 and RQ2 are about "
                "explanation, RQ3 and RQ4 are about learning, RQ5 is the synthesis. Then say the mapping: C1 answers "
                "RQ1, C2 answers RQ2, C3 answers RQ3 and RQ4, and RQ5 is answered by the thesis as a whole.",
         "time": "≈ 38 s", "cue": "Do not read the aim strip twice; the note already states the aim once at the start."},
        {"n": "16", "title": "The Three Contributions",
         "screen": "Three cards: C1 / C2 / C3 with RQ labels, methods, datasets and one-line outcomes, then the thesis claim strip.",
         "how": "One sentence per card, in the same order as the arrows on slide 15: explain, scale, guide. Name the "
                "datasets as anchors — wine, Beijing, MovieLens-1M and Amazon-Book — because they return in section 3. "
                "Close with “three steps that build on each other, not three unrelated papers”, which is the claim the "
                "jury will test by asking why this is one thesis (question A3).",
         "time": "≈ 39 s", "cue": "If asked later why these three papers form one thesis, answer from this slide plus question A3 — not by inventing a new narrative."},
    ],
    "extra": [
        ("The four families in one table you can recall under pressure",
         "Content-based: explainable, over-specialised. Collaborative: scalable, cold-start blind. Hybrid and MF: "
         "accurate, latent. Graph and hypergraph: state of the art, opaque and expensive. That sentence covers slides "
         "9-12 if a jury member asks you to summarise the state of the art in thirty seconds."),
        ("The mapping to memorise",
         "RQ1 → C1 (faithful clustering explanation). RQ2 → C2 (multi-level, large-scale, consistent). RQ3 → C3 "
         "(beyond post-hoc). RQ4 → C3 (accuracy, context and diversity together). RQ5 → the whole thesis (what one "
         "cooperative-game view buys). Five questions, three contributions, one answer — that is the shape of the viva."),
    ],
    "transition": "“Before I show the three contributions, let me fix the experimental protocol they all share.”",
}


# --------------------------------------------------------------------------
# Section 3: Experimental protocol (17-25)
# --------------------------------------------------------------------------
S3 = {
    "id": "protocol",
    "kicker": "Section 3 · slides 17-25 · 3.9 min",
    "title": "Experimental Protocol: datasets, splits, baselines, metrics, hardware",
    "range": "17-25",
    "words": "503",
    "m130": "3.9",
    "m120": "4.2",
    "search": "protocol datasets wine bjair movielens amazon split preprocessing baselines metrics NDCG silhouette hardware",
    "purpose": """
- Convince the jury that the three contributions can be read together, because they share one protocol: same seeds, same splitting logic, same surrogate configuration, same reporting discipline.
- Justify the four datasets: two clustering (wine, Beijing) and two recommendation (MovieLens-1M, Amazon-Book), chosen for contrast — small/dense versus large/noisy, dense versus extremely sparse.
- Pre-empt the methodological questions: why these baselines, why these metrics, why this hardware, how leakage is prevented.
""",
    "arc": [
        ("The protocol is the single best place to look prepared", "Nine slides, only 503 words: this section is a "
         "checklist, not a narrative. Deliver it calmly and completely, name where each item is specified in the thesis "
         "(Chapter 4), and let the jury see that the discipline is uniform across the three studies."),
        ("Two contrasts do the work", "Wine connects explanation to chemistry; Beijing stress-tests scale and "
         "hierarchy. MovieLens-1M is dense (0.0447) and comparable with prior work; Amazon-Book is almost empty "
         "(0.0006) and tests whether cooperative weighting helps when signal is weakest. Say these four justifications; "
         "they explain the dataset table better than the table does."),
    ],
    "slides": [
        {"n": "17", "title": "Experimental Protocol divider",
         "screen": "Section 03 with three cards: datasets, baselines and metrics, reproducibility.",
         "how": "One sentence: the protocol is shared so that the three contributions can be read together. Say the "
                "time-check cue: about minute ten. Announce the four blocks you are about to give — datasets, "
                "preprocessing, baselines and metrics, hardware.",
         "time": "≈ 20 s", "cue": "Cue 3. Arrival time here is 9.6 min, which is on plan."},
        {"n": "18", "title": "Wine Quality: Portuguese Vinho Verde",
         "screen": "Three intro bullets, a specification table (4,898 observations, 11 numeric features, target quality 3-9 not used, no missing values, standardised, k* = 3) and the caption.",
         "how": "Say the numbers once — 4,898 samples, 11 physicochemical measurements — then the justification: small, "
                "dense and chemically correlated, so an explanation can be checked against the domain. Note explicitly "
                "that the taste score exists but is not used for clustering. Do not read the table row by row.",
         "time": "≈ 42 s", "cue": "The first of the four datasets: the notes open with a sentence that frames all four, then narrow to wine. Keep that order."},
        {"n": "19", "title": "Beijing Multi-Site Air Quality",
         "screen": "383,585 hourly records, eleven variables (six pollutants and five weather), the specification table, and the caption about weather setting the regime.",
         "how": "Emphasise scale: 383,585 records is roughly eighty times the wine data, which is why this dataset tests "
                "feasibility, not just accuracy. Name the eleven variables as six pollutants plus five weather "
                "variables; if you list weather, list wind direction, not rain. Preview the finding without giving it "
                "away: the explanation will show that weather sets the regime.",
         "time": "≈ 20 s", "cue": "Do not say “nine sub-clusters”; the deck and the thesis only support “coarse regimes → level-2 sub-clusters”."},
        {"n": "20", "title": "MovieLens-1M",
         "screen": "About one million ratings, 6,040 users, 3,706 movies, density 0.0447, rating scale 1-5, at least 20 interactions per user.",
         "how": "Call it the standard benchmark of the field, which is what makes the comparison with LightGCN, HCCF "
                "and HPCF readable. Give the density (0.0447), the conversion rule (ratings above 3 become positives) "
                "and the context proxy (genre). Twenty-five seconds.",
         "time": "≈ 27 s", "cue": "Do not cite “GroupLens 2000”; v26 corrected this to “GroupLens benchmark”. The dataset paper is Harper and Konstan 2015 in the reference list."},
        {"n": "21", "title": "Amazon-Book",
         "screen": "52,643 users, 91,599 books, 2,984,108 interactions, density ≈ 0.0006, implicit feedback, category as context proxy.",
         "how": "The point of this slide is the contrast: 0.0447 versus 0.0006 is a factor of seventy-five in density. "
                "Say why it is included — to test whether Shapley-guided weighting helps most when the signal is "
                "weakest — and note that Amazon-Book is the large-scale benchmark of Contribution III.",
         "time": "≈ 30 s", "cue": "Amazon-Book is where significance is descriptive, not tabulated (question F11). Say “descriptive gain” if you compare it."},
        {"n": "22", "title": "Data Splitting &amp; Preprocessing",
         "screen": "Two blocks: clustering (five-fold CV, standardisation, PCA for geometry, multi-criteria k selection, macro-F1 floor 0.82) and recommendation (70/10/20 user-level time-ordered split, leave-one-out target, ratings &gt; 3 as positive, popularity-aware negative sampling, seeds 42-46, patience 20).",
         "how": "Two blocks, two sentences each. For clustering: five-fold cross-validation for stability, k chosen by "
                "elbow, Silhouette and Davies-Bouldin, surrogate must clear macro-F1 ≈ 0.82. For recommendation: "
                "user-level, time-ordered, 70/10/20, leave-one-out target, seeds 42 to 46, early stopping. Then the "
                "sentence that prevents a leakage question: the split is user-level and time-ordered, so no future "
                "interaction leaks into training.",
         "time": "≈ 37 s", "cue": "Leakage is the single most likely methods question (F8). Have slide 22 up and answer from it."},
        {"n": "23", "title": "Baselines",
         "screen": "Table of seven rows: LIME surrogate pipeline for explanation; MF (BPR), NCF, LightGCN, RecDCL, HCCF and HPCF for recommendation, with HPCF marked as the strongest reference.",
         "how": "Do not read the table. Say the argument: classical, neural, graph and hypergraph families together, so "
                "the effect of cooperative attribution is not confused with a lucky model choice; HPCF is the strongest "
                "reference; all baselines were finalised in early 2026. Then name the honest boundary: superiority is "
                "claimed against this tested set only, which includes no post-2024 LLM-augmented recommender.",
         "time": "≈ 22 s", "cue": "Say “LIME surrogate pipeline” as a comparator, not as something you benchmarked head-to-head (question C5)."},
        {"n": "24", "title": "Evaluation Metrics",
         "screen": "Six metrics with formulas: NDCG@K, Recall@K, catalogue coverage, intra-list diversity, Silhouette, Davies-Bouldin, plus the notation line (K ∈ {5,10,20}, NDCG@20 is the main measure).",
         "how": "Group the metrics into two families while you speak: recommendation metrics (ranking quality, "
                "retrieval, system-level diversity, list-level diversity) and clustering metrics (separation and "
                "overlap). Say which one is the main measure — NDCG@20 — and why accuracy is not enough: coverage and "
                "intra-list diversity are the metrics that make the accuracy-versus-diversity trade-off visible.",
         "time": "≈ 21 s", "cue": "Precision@K was dropped from this table in v25 because it was not reported in the results. Do not reintroduce it."},
        {"n": "25", "title": "Hardware &amp; Software",
         "screen": "Table by contribution: i9-14900K (24 cores), 48 GB RAM, 2 TB SSD, RTX 4090 24 GB for DyHuCoG, Python 3.8, PyTorch 2.0.1; plus the why-it-matters and scope cards.",
         "how": "Fifteen seconds. The message is that everything ran on standard academic hardware, so the runtime "
                "figures later are honest and reproducible. Link forward: these are the machines behind the 1.78× "
                "training overhead on slide 61.",
         "time": "≈ 14 s", "cue": "Do not apologise for the hardware. One workstation and one consumer GPU is a strength for reproducibility, not a limitation."},
    ],
    "extra": [
        ("The protocol in five sentences, if you are asked to summarise section 3",
         "Four datasets: wine and Beijing for clustering, MovieLens-1M and Amazon-Book for recommendation. Clustering: "
         "standardised features, k chosen by elbow, Silhouette and Davies-Bouldin, a LightGBM surrogate per level with "
         "macro-F1 around 0.82, TreeSHAP in the original variables. Recommendation: user-level time-ordered 70/10/20 "
         "splits, leave-one-out targets, five seeds, popularity-aware negative sampling. Baselines from four families "
         "with HPCF as the strongest reference. Metrics: NDCG@20 as the main ranking measure, plus Recall, coverage, "
         "intra-list diversity, and Silhouette and Davies-Bouldin for clustering."),
        ("Where every protocol detail lives in the thesis",
         "Chapter 4 is the shared protocol: dataset statistics in Table 4.1, hardware in Table 4.2, splitting and "
         "preprocessing in §4.2 and §4.5.6, metrics in §4.4 (equations 4.8 to 4.14). If a jury member wants a page "
         "number, these are the ones to quote; the deck says “the details are in Chapter 4” and that is a complete "
         "answer for a forty-minute defence."),
    ],
    "transition": "“With that shared protocol fixed, I can start the first contribution: explaining a black-box partition.”",
}


SECTIONS = [S0, S1, S2, S3]
