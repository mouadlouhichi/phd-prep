#!/usr/bin/env python3
"""
Build the standalone HTML study guide for the viva deck
`try/MOUAD_LOUHICHI_VIVA_40min_BeigeGreen_v32.pptx`.

Usage:  python3 build.py            # writes ../../../MOUAD_LOUHICHI_VIVA_PRESENTATION_GUIDE.html
        python3 build.py out.html

Design: self-contained single file (inline CSS + JS, no network requests).
Content lives in the sibling modules:
    content_map.py      deck map, timing ledger, section playbooks 0-3
    content_map2.py     section playbooks 4-7, Q&A stage, backup slides
    content_tech.py     beginner glossary + worked concept walkthroughs
    content_qa1.py      100 viva questions, categories A-D
    content_qa2.py      100 viva questions, categories E-H
    content_extra.py    section 7 delivery plan, cheat sheets, checklists
"""
import html
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
DEFAULT_OUT = os.path.join(ROOT, "MOUAD_LOUHICHI_VIVA_PRESENTATION_GUIDE.html")

sys.path.insert(0, HERE)

import content_map      # noqa: E402
import content_map2     # noqa: E402
import content_tech     # noqa: E402
import content_qa1      # noqa: E402
import content_qa2      # noqa: E402
import content_extra    # noqa: E402

content_extra.RICH = None  # set below, once rich() exists


# --------------------------------------------------------------------------
# mini-markup -> HTML
# --------------------------------------------------------------------------
INLINE = [
    (re.compile(r"\$([^$]+)\$"), r'<span class="math">\\(\1\\)</span>'),
    (re.compile(r"\*\*(.+?)\*\*", re.S), r"<strong>\1</strong>"),
    (re.compile(r"(?<!\w)\*(?!\s)(.+?)(?<!\s)\*(?!\w)", re.S), r"<em>\1</em>"),
    (re.compile(r"`([^`]+)`"), r"<code>\1</code>"),
    (re.compile(r"\[([0-9ivx]+)\]"), r'<span class="code-chip">[\1]</span>'),
]


# --------------------------------------------------------------------------
# math: every formula in the content is rewritten to TeX ($...$) and rendered
# with KaTeX; detex() gives a readable text form for the search attributes.
# --------------------------------------------------------------------------
_TEX2U = [
    (r"\hat\varphi", "φ̂"), (r"\varphi", "φ"), (r"\Phi", "Φ"), (r"\sigma", "σ"),
    (r"\alpha", "α"), (r"\beta", "β"), (r"\gamma", "γ"), (r"\lambda", "λ"),
    (r"\varepsilon", "ε"), (r"\eta", "η"), (r"\ell", "ℓ"), (r"\mu", "μ"),
    (r"\sum", "Σ"), (r"\cdot", "·"), (r"\times", "×"), (r"\propto", "∝"),
    (r"\langle", "⟨"), (r"\rangle", "⟩"), (r"\subseteq", "⊆"), (r"\setminus", "∖"),
    (r"\cup", "∪"), (r"\varnothing", "∅"), (r"\mid", "|"), (r"\sqrt", "√"),
    (r"\bigl", ""), (r"\bigr", ""), (r"\left", ""), (r"\right", ""),
    (r"\overline", ""), (r"\mathrm", ""), (r"\mathbb", ""), (r"\,", " "),
    (r"\;", " "), (r"\!", ""), (r"\ ", " "), (r"\{", "{"), (r"\}", "}"),
]


def detex(t):
    for a, b in _TEX2U:
        t = t.replace(a, b)
    t = re.sub(r"\\frac\{([^{}]*)\}\{([^{}]*)\}", r"(\1)/(\2)", t)
    t = re.sub(r"\\dfrac\{([^{}]*)\}\{([^{}]*)\}", r"(\1)/(\2)", t)
    t = re.sub(r"\\[a-zA-Z]+", "", t)
    return t.replace("{", "").replace("}", "").replace("\\", "")


SUP = str.maketrans("⁻⁰¹²³⁴⁵⁶⁷⁸⁹", "-0123456789")


def _sci(m):
    return "$%s.%s\\times 10^{%s}$" % (m.group(1), m.group(2), m.group(3).translate(SUP))


MATH_REPS = [
    # scientific notation, e.g. 1.81×10⁻²⁷⁰
    (re.compile(r"(?<![\d.])(\d+)\.(\d+)×10([⁻⁰¹²³⁴⁵⁶⁷⁸⁹]+)"), _sci),
    # Shapley value, long form (walkthrough 2 / glossary)
    (re.compile(r"`φ_j\(v\) = Σ over S ⊆ N\s*\\+\s*\{j\} of.*?\[ v\(S ∪ \{j\}\) − v\(S\) \]`"),
     r"$\varphi_j(v) = \sum_{S \subseteq N \setminus \{j\}} \frac{|S|!\,(n-|S|-1)!}{n!}\,"
     r"\bigl[v(S \cup \{j\}) - v(S)\bigr]$"),
    # Proposition 6.1, aggregation + weights
    (re.compile(r"`Φ_j\^\(level ℓ, cluster c\) = Σ over children.*?ε_j`"),
     r"$\Phi_j^{(\ell,c)} = \sum_{c' \in \mathrm{child}(c)} w_{c'}\,\Phi_j^{(\ell+1,c')} + \varepsilon_j$"),
    (re.compile(r"`?w_c′ = \|c′\| / \|c\|`?"), r"$w_{c'} = \dfrac{|c'|}{|c|}$"),
    (re.compile(r"Φ_parent = Σ w_c′ Φ_child \+ ε"),
     r"$\Phi_{\mathrm{parent}} = \sum w_{c'} \Phi_{\mathrm{child}} + \varepsilon$"),
    # Monte Carlo estimator
    (re.compile(r"`φ̂_j = \(1/M\) Σ_\{m=1\.\.M\} \[ v\(S_m ∪ \{j\}\) − v\(S_m\) \]`"),
     r"$\hat\varphi_j = \frac{1}{M}\sum_{m=1}^{M}\bigl[v(S_m \cup \{j\}) - v(S_m)\bigr]$"),
    # coalition value of DyHuCoG
    (re.compile(r"`?v\(S\) = α ?· ?NDCG@20\(S\) \+ β ?· ?Diversity\(S\) \+ γ ?· ?ContextScore\(S\)`?"),
     r"$v(S) = \alpha\cdot \mathrm{NDCG@20}(S) + \beta\cdot \mathrm{Diversity}(S)"
     r" + \gamma\cdot \mathrm{ContextScore}(S)$"),
    (re.compile(r"`?v_pref\(S\) = v\(S\) \+ λ_pref ?· ?Σ sim\(u, ?i\)`?"),
     r"$v_{\mathrm{pref}}(S) = v(S) + \lambda_{\mathrm{pref}} \sum \mathrm{sim}(u,i)$"),
    (re.compile(r"λ_pref\s*·\s*Σ sim\(u, ?i\)"), r"$\lambda_{\mathrm{pref}} \sum \mathrm{sim}(u,i)$"),
    # the DyHuCoG model: gate, score, prediction, loss
    (re.compile(r"`a_ui = σ\(W_a \[e_u, e_i, l_i\]\)`"),
     r"$a_{ui} = \sigma\!\left(W_a\,[e_u, e_i, l_i]\right)$"),
    (re.compile(r"`y_ui = \(1 \+ a_ui\) ?⟨e_u, e_i⟩`"),
     r"$y_{ui} = (1 + a_{ui})\,\langle e_u, e_i\rangle$"),
    (re.compile(r"`f\(u, i, c\) = y_ui \+ λ_c ⟨g\(c\), e_c⟩`"),
     r"$f(u,i,c) = y_{ui} + \lambda_c\,\langle g(c), e_c\rangle$"),
    (re.compile(r"`L = L_BPR \+ λ_div L_div \+ λ_ctx L_ctx \+ λ_reg L_reg`"),
     r"$L = L_{\mathrm{BPR}} + \lambda_{\mathrm{div}} L_{\mathrm{div}}"
     r" + \lambda_{\mathrm{ctx}} L_{\mathrm{ctx}} + \lambda_{\mathrm{reg}} L_{\mathrm{reg}}$"),
    (re.compile(r"`L_div = −\(1/\|U\|\) Σ(_u)? ILD\(R_u\)`"),
     r"$L_{\mathrm{div}} = -\frac{1}{|U|}\sum_u \mathrm{ILD}(R_u)$"),
    # metrics
    (re.compile(r"`DCG@K = Σ_\{i=1\.\.K\} \(2\^rel_i − 1\) / log₂\(i \+ 1\)`"),
     r"$\mathrm{DCG@K} = \sum_{i=1}^{K} \frac{2^{\mathrm{rel}_i} - 1}{\log_2(i+1)}$"),
    (re.compile(r"`NDCG@K = DCG@K / IDCG@K`"),
     r"$\mathrm{NDCG@K} = \dfrac{\mathrm{DCG@K}}{\mathrm{IDCG@K}}$"),
    (re.compile(r"`s\(x\) = \(b\(x\) − a\(x\)\) / max\(a\(x\), b\(x\)\)`"),
     r"$s(x) = \dfrac{b(x) - a(x)}{\max\bigl(a(x), b(x)\bigr)}$"),
    # statistics
    (re.compile(r"`?t = mean\(d\) / \(sd\(d\)/√n\)`?"),
     r"$t = \dfrac{\overline{d}}{s_d / \sqrt{n}}$"),
    (re.compile(r"\bdz = (\d+\.\d+)"), lambda m: "$d_z = %s$" % m.group(1)),
    (re.compile(r"α/\(m − k \+ 1\)"), r"$\alpha/(m-k+1)$"),
    (re.compile(r"α \+ β \+ γ = 1"), r"$\alpha + \beta + \gamma = 1$"),
    # variance, expectation, axioms
    (re.compile(r"σ²/M"), r"$\sigma^2/M$"),
    (re.compile(r"(?<![\w$])σ²(?![\w$])"), r"$\sigma^2$"),
    (re.compile(r"E\[X\] = Σ P\(c′\) · E\[X \| c′\]"),
     r"$\mathbb{E}[X] = \sum P(c') \cdot \mathbb{E}[X \mid c']$"),
    (re.compile(r"E\[φ̂\] = φ"), r"$\mathbb{E}[\hat\varphi] = \varphi$"),
    (re.compile(r"Σ φ_j = v\(N\) − v\(∅\)"), r"$\sum_j \varphi_j = v(N) - v(\varnothing)$"),
    (re.compile(r"φ\(v \+ w\) = φ\(v\) \+ φ\(w\)"), r"$\varphi(v + w) = \varphi(v) + \varphi(w)$"),
    # structures and sets
    (re.compile(r"H = \(V, E, W\)"), r"$H = (V, E, W)$"),
    (re.compile(r"N = U ∪ I ∪ C"), r"$N = U \cup I \cup C$"),
    (re.compile(r"q\(i\) ∝ f_i\^η"), r"$q(i) \propto f_i^{\eta}$"),
    (re.compile(r"2\^N\b"), r"$2^{N}$"),
    (re.compile(r"2³⁰"), r"$2^{30}$"),
    # prose variants without backticks
    (re.compile(r"DCG@K = Σ 2\^rel_i − 1 over log₂\(i\+1\)"),
     r"$\mathrm{DCG@K} = \sum_{i=1}^{K} \frac{2^{\mathrm{rel}_i} - 1}{\log_2(i+1)}$"),
    (re.compile(r"α·NDCG@20\(S\) \+ …"), r"$\alpha\cdot \mathrm{NDCG@20}(S) + \dots$"),
    (re.compile(r"α·NDCG@20\(S\)"), r"$\alpha\cdot \mathrm{NDCG@20}(S)$"),
    # worked numbers (walkthroughs 1, 2, 6, 11)
    (re.compile(r"`v\((G,V,D|G,V|G,D|V,D|G|V|D)\) = (\d+)`"),
     lambda m: "$v(%s) = %s$" % (m.group(1), m.group(2))),
    (re.compile(r"90 \+ 70 \+ 40 = 200 = v\(N\)"), r"$90 + 70 + 40 = 200 = v(N)$"),
    (re.compile(r"\|S\| = (\d):"), lambda m: "$|S| = %s$:" % m.group(1)),
    (re.compile(r"([0-2]!)·([0-2]!)/3! = ([\d/]+)"),
     lambda m: "$%s\\cdot%s/3! = %s$" % (m.group(1), m.group(2), m.group(3))),
    (re.compile(r"1/3 \+ 2·\(1/6\) \+ 1/3 = 1"), r"$1/3 + 2\cdot(1/6) + 1/3 = 1$"),
    (re.compile(r"w₁ = 600/1000 = 0\.6"), r"$w_1 = 600/1000 = 0.6$"),
    (re.compile(r"w₂ = 400/1000 = 0\.4"), r"$w_2 = 400/1000 = 0.4$"),
    (re.compile(r"0\.6 × 0\.10 \+ 0\.4 × 0\.20 = 0\.14"),
     r"$0.6 \times 0.10 + 0.4 \times 0.20 = 0.14$"),
    (re.compile(r"ε = 0\b"), r"$\varepsilon = 0$"),
    (re.compile(r"\(2¹ − 1\)/log₂\((\d+)\) = ([\d./]+)"),
     lambda m: "$(2^1 - 1)/\\log_2(%s) = %s$" % (m.group(1), m.group(2))),
    (re.compile(r"1/log₂\((\d+)\) = ([\d./]+)"),
     lambda m: "$1/\\log_2(%s) = %s$" % (m.group(1), m.group(2))),
    (re.compile(r"1/log₂\(i\+1\)"), r"$1/\log_2(i+1)$"),
]


def apply_math(text):
    for pat, rep in MATH_REPS:
        if callable(rep):
            text = pat.sub(rep, text)
        else:
            text = pat.sub(lambda m, _r=rep: _r, text)  # TeX backslashes are literal
    return text


def md(text):
    """Paragraphs (blank-line separated), '- ' bullets, '1. ' numbered lines."""
    if text is None:
        return ""
    text = str(text).strip()
    if not text:
        return ""
    text = apply_math(text)
    blocks, para, bullets, numbers = [], [], [], []

    def flush():
        if para:
            blocks.append("<p>" + " ".join(para).strip() + "</p>")
            para.clear()
        if bullets:
            blocks.append("<ul>" + "".join("<li>%s</li>" % b for b in bullets) + "</ul>")
            bullets.clear()
        if numbers:
            blocks.append("<ol>" + "".join("<li>%s</li>" % b for b in numbers) + "</ol>")
            numbers.clear()

    for raw in text.split("\n"):
        line = raw.strip()
        if not line:
            flush()
            continue
        if line.startswith("- "):
            if para or numbers:
                flush()
            bullets.append(line[2:].strip())
        elif bullets and raw[:1] in (" ", "\t"):
            # indented continuation of the previous bullet
            bullets[-1] = bullets[-1] + " " + line
            continue
        elif re.match(r"^\d+\.\s", line):
            if para or bullets:
                flush()
            numbers.append(re.sub(r"^\d+\.\s*", "", line))
        elif line.startswith("| "):
            flush()
            blocks.append(line)
        else:
            if bullets or numbers:
                flush()
            para.append(line)
    flush()
    out = "\n".join(blocks)
    for pat, rep in INLINE:
        out = pat.sub(rep, out)
    return out


def rich(s):
    """Inline formatting only (no block wrapping): math, bold, italic, code."""
    out = apply_math(str(s))
    for pat, rep in INLINE:
        out = pat.sub(rep, out)
    return out


content_extra.RICH = rich


def esc(s):
    return html.escape(str(s))


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", str(s).lower()).strip("-")


def plain(s):
    """Text with the mini-markup stripped, for search attributes."""
    s = apply_math(str(s))
    s = re.sub(r"\$([^$]+)\$", lambda m: detex(m.group(1)), s)
    return re.sub(r"[*`]", "", s).replace("\n", " ")


def table(headers, rows, cls="tbl"):
    h = "".join("<th>%s</th>" % md(c) for c in headers)
    body = []
    for r in rows:
        cells = []
        for i, c in enumerate(r):
            klass = ""
            if i == 0 and cls == "tbl slides":
                klass = ' class="slidecell"'
            cells.append("<td%s>%s</td>" % (klass, md(c)))
        body.append("<tr>%s</tr>" % "".join(cells))
    return (
        '<div class="tw"><table class="%s"><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>'
        % (cls, h, "".join(body))
    )


# --------------------------------------------------------------------------
# renderers
# --------------------------------------------------------------------------
def render_slide_table(slides):
    rows = []
    for s in slides:
        rows.append([
            '<span class="sn">%s</span>' % s["n"],
            "<strong>%s</strong>" % s["title"],
            s.get("screen", ""),
            s.get("how", ""),
            s.get("time", ""),
            s.get("cue", "—"),
        ])
    return table(["#", "Slide", "What the jury sees", "How to present it",
                  "Spoken", "Cue / risk"], rows, cls="tbl slides")


def render_section(sec):
    sid = "sec-" + slug(sec["id"])
    parts = ['<section class="sec" id="%s" data-search="%s">' % (sid, esc(sec.get("search", sec["title"])))]
    parts.append(
        '<div class="sec-head"><div class="sec-kicker">%s</div><h2>%s</h2>'
        '<div class="sec-meta"><span class="pill">slides %s</span>'
        '<span class="pill">%s spoken words</span>'
        '<span class="pill">%s min @ 130 wpm</span>'
        '<span class="pill">%s min @ 120 wpm</span></div></div>'
        % (esc(sec["kicker"]), esc(sec["title"]), esc(sec["range"]),
           esc(sec["words"]), esc(sec["m130"]), esc(sec["m120"]))
    )
    if sec.get("purpose"):
        parts.append('<div class="callout goal"><h4>What this section must achieve</h4>%s</div>' % md(sec["purpose"]))
    if sec.get("arc"):
        parts.append('<div class="grid2">%s</div>' % "".join(
            '<div class="mini"><h5>%s</h5>%s</div>' % (esc(t), md(b)) for t, b in sec["arc"]))
    if sec.get("slides"):
        parts.append('<h3>Slide-by-slide delivery</h3>')
        parts.append(render_slide_table(sec["slides"]))
    if sec.get("extra"):
        for t, b in sec["extra"]:
            parts.append('<div class="callout"><h4>%s</h4>%s</div>' % (esc(t), md(b)))
    if sec.get("transition"):
        parts.append('<div class="transition"><span>Say this as you change section</span><p>“%s”</p></div>'
                     % md(sec["transition"]))
    parts.append("</section>")
    return "\n".join(parts)


def render_glossary(entries):
    cards = []
    for i, e in enumerate(entries, 1):
        cards.append(
            '<div class="gcard" data-search="%s %s %s">'
            '<div class="ghead"><span class="gnum">%02d</span><h4>%s</h4>'
            '<span class="gtag">%s</span></div>'
            '<p class="gplain"><span class="lab">In one line</span>%s</p>'
            '<div class="gdeep"><span class="lab">Going deeper</span>%s</div>'
            '<p class="gwhy"><span class="lab">In this thesis</span>%s</p>'
            "</div>"
            % (esc(e["term"]), esc(e.get("tag", "")), esc(e.get("where", "")),
               i, rich(e["term"]), esc(e.get("tag", "")), md(e["plain"]), md(e["deep"]),
               md(e.get("why", "")))
        )
    return "\n".join(cards)


def render_walkthroughs(items):
    out = []
    for w in items:
        out.append('<div class="walk" id="walk-%s"><h3>%s</h3><p class="walklede">%s</p>%s</div>'
                   % (slug(w["title"]), esc(w["title"]), md(w.get("lede", "")), md(w["body"])))
    return "\n".join(out)


QA_ANCHOR = {"A": "framing", "B": "game", "C": "c1", "D": "c2",
             "E": "c3", "F": "method", "G": "ethics", "H": "limits"}


def qa_anchor(title):
    m = re.match(r"\s*([A-H])\s*[\u00b7:\-]", str(title))
    return QA_ANCHOR.get(m.group(1), slug(title)) if m else slug(title)


def render_qa(groups):
    out = []
    n = 0
    for g in groups:
        items = []
        for q in g["items"]:
            n += 1
            qid = "q%03d" % n
            items.append(
                '<details class="qa" id="%s" data-search="%s %s %s">'
                '<summary><span class="qnum">Q%03d</span><span class="qtext">%s</span>'
                '<span class="qchev">›</span></summary>'
                '<div class="abody">%s'
                '<div class="qmeta"><span class="tag">%s</span>%s</div></div></details>'
                % (qid, esc(plain(q["q"])), esc(plain(q["a"])), esc(g["title"]), n, md(q["q"]), md(q["a"]),
                   esc(g["title"]), ("".join('<span class="tag wt">%s</span>' % esc(t) for t in q.get("tags", []))))
            )
        out.append('<div class="qgroup" id="qa-%s"><h3>%s <span class="qcount">%d questions</span></h3>%s</div>'
                   % (qa_anchor(g["title"]), esc(g["title"]), len(g["items"]), "".join(items)))
    return "\n".join(out), n


# --------------------------------------------------------------------------
# page
# --------------------------------------------------------------------------
CSS = """
:root{
 --beige:#FEF8F3; --beige2:#F7EDE2; --green:#124944; --green2:#1E6B60; --green3:#2F8A7C;
 --mustard:#ECC665; --mustard2:#F6E3B0; --orange:#DF8330; --ink:#1C2B29; --ink2:#3E5250;
 --line:#E3D6C6; --white:#fff; --shadow:0 1px 2px rgba(28,43,41,.06),0 6px 20px rgba(28,43,41,.07);
 --mono:ui-monospace,SFMono-Regular,Menlo,Consolas,"Liberation Mono",monospace;
 --sans:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--beige);color:var(--ink);font:16px/1.62 var(--sans);
 -webkit-font-smoothing:antialiased}
a{color:var(--green2);text-underline-offset:2px}
h1,h2,h3,h4,h5{line-height:1.25;color:var(--green);margin:0 0 .5em}
h2{font-size:1.72rem;letter-spacing:-.01em}
h3{font-size:1.24rem;margin-top:1.6em}
h4{font-size:1.05rem}
p{margin:0 0 .85em}
code{font-family:var(--mono);font-size:.87em;background:#F1E7DA;padding:.12em .38em;border-radius:5px;
 color:#0F3D38;white-space:nowrap}
strong{color:#0F3D38}
ul,ol{margin:0 0 .9em;padding-left:1.25em}
li{margin:.22em 0}

/* ---------- header ---------- */
header.top{position:sticky;top:0;z-index:60;background:linear-gradient(180deg,#0F3D38,#124944);
 color:#F7F3EC;box-shadow:0 2px 14px rgba(15,61,56,.25)}
.top-in{max-width:1560px;margin:0 auto;padding:.6rem 1.1rem;display:flex;gap:1rem;align-items:center;flex-wrap:wrap}
.brand{display:flex;flex-direction:column;min-width:250px}
.brand b{font-size:1.02rem;letter-spacing:.01em}
.brand span{font-size:.74rem;opacity:.8;letter-spacing:.04em;text-transform:uppercase}
nav.tabs{display:flex;gap:.3rem;flex-wrap:wrap;margin-left:auto}
nav.tabs button{background:rgba(255,255,255,.08);color:#F7F3EC;border:1px solid rgba(255,255,255,.18);
 padding:.32rem .66rem;border-radius:99px;font:inherit;font-size:.82rem;cursor:pointer}
nav.tabs button:hover{background:rgba(255,255,255,.18)}
nav.tabs button.on{background:var(--mustard);color:#123;border-color:var(--mustard);font-weight:600}
.searchbox{display:flex;align-items:center;gap:.4rem;background:rgba(255,255,255,.1);border:1px solid rgba(255,255,255,.2);
 border-radius:99px;padding:.22rem .6rem;min-width:230px}
.searchbox input{background:none;border:0;color:#fff;font:inherit;font-size:.85rem;outline:none;width:100%}
.searchbox input::placeholder{color:rgba(255,255,255,.6)}
.searchbox .hits{font-size:.7rem;opacity:.75;white-space:nowrap}

/* ---------- layout ---------- */
.wrap{max-width:1560px;margin:0 auto;display:grid;grid-template-columns:302px minmax(0,1fr);gap:0}
aside{position:sticky;top:58px;align-self:start;height:calc(100vh - 58px);overflow:auto;
 padding:1.1rem .8rem 3rem 1.1rem;border-right:1px solid var(--line);font-size:.86rem}
aside h5{font-size:.7rem;text-transform:uppercase;letter-spacing:.09em;color:var(--green3);margin:1.1em 0 .4em}
aside a{display:block;padding:.22rem .45rem;border-radius:7px;text-decoration:none;color:var(--ink2)}
aside a:hover{background:var(--beige2);color:var(--green)}
aside a.sub{padding-left:1.2rem;font-size:.82rem;opacity:.92}
main{padding:1.4rem 1.6rem 6rem;min-width:0;max-width:1180px}
body.focus aside{display:none}
body.focus .wrap{grid-template-columns:minmax(0,1fr)}
body.focus main{max-width:1180px;margin:0 auto}

/* ---------- hero ---------- */
.hero{background:var(--white);border:1px solid var(--line);border-radius:18px;padding:1.5rem 1.6rem;
 box-shadow:var(--shadow);margin-bottom:1.5rem}
.hero h1{font-size:2rem;margin-bottom:.35rem}
.hero .sub{color:var(--ink2);font-size:1.03rem;margin-bottom:1rem}
.hero .meta{display:flex;gap:.45rem;flex-wrap:wrap;margin-bottom:1rem}
.pill{display:inline-block;background:var(--mustard2);color:#5A4410;border-radius:99px;padding:.16rem .62rem;
 font-size:.76rem;font-weight:600;letter-spacing:.01em}
.pill.g{background:#DDEDE9;color:#124944}
.pill.o{background:#FBE4CC;color:#7A3F08}
.legend{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:.7rem;margin-top:1rem}
.legend div{background:var(--beige);border:1px solid var(--line);border-radius:12px;padding:.7rem .85rem;font-size:.88rem}
.legend b{display:block;color:var(--green);margin-bottom:.15rem}

/* ---------- sections ---------- */
section.sec{background:var(--white);border:1px solid var(--line);border-radius:16px;padding:1.35rem 1.5rem;
 margin:0 0 1.6rem;box-shadow:var(--shadow);scroll-margin-top:74px}
.sec-head{border-bottom:2px solid var(--mustard);padding-bottom:.7rem;margin-bottom:1rem}
.sec-kicker{font-size:.75rem;letter-spacing:.11em;text-transform:uppercase;color:var(--orange);font-weight:700}
.sec-head h2{margin:.15rem 0 .5rem}
.sec-meta{display:flex;gap:.4rem;flex-wrap:wrap}
.callout{background:var(--beige);border-left:4px solid var(--green3);border-radius:0 12px 12px 0;
 padding:.85rem 1rem;margin:1rem 0}
.callout h4{margin:0 0 .35rem;font-size:.95rem;text-transform:uppercase;letter-spacing:.06em;color:var(--green2)}
.callout.goal{border-left-color:var(--orange);background:#FDF1E4}
.callout.goal h4{color:#8A4A0C}
.callout.warn{border-left-color:#C0392B;background:#FCEDEA}
.callout.warn h4{color:#8E2B20}
.callout.win{border-left-color:var(--mustard);background:#FDF7E6}
.grid2{display:grid;grid-template-columns:repeat(auto-fit,minmax(255px,1fr));gap:.8rem;margin:1rem 0}
.mini{background:var(--beige);border:1px solid var(--line);border-radius:12px;padding:.8rem .9rem;font-size:.92rem}
.mini h5{margin:0 0 .3rem;font-size:.85rem;text-transform:uppercase;letter-spacing:.06em;color:var(--green3)}
.transition{margin-top:1.1rem;background:#EAF4F1;border:1px dashed var(--green3);border-radius:12px;padding:.75rem .95rem}
.transition span{font-size:.72rem;letter-spacing:.1em;text-transform:uppercase;color:var(--green3);font-weight:700}
.transition p{margin:.25rem 0 0;font-style:italic;color:#0F3D38}

/* ---------- tables ---------- */
.tw{overflow-x:auto;margin:.6rem 0 1.1rem;border:1px solid var(--line);border-radius:12px}
table.tbl{border-collapse:collapse;width:100%;font-size:.87rem;background:var(--white)}
table.tbl th{background:var(--green);color:#F6F1E8;text-align:left;padding:.55rem .65rem;font-size:.76rem;
 text-transform:uppercase;letter-spacing:.05em;position:sticky;top:0}
table.tbl td{padding:.55rem .65rem;border-top:1px solid var(--line);vertical-align:top}
table.tbl tr:nth-child(even) td{background:#FCF7F1}
table.tbl td.slidecell{white-space:nowrap;font-weight:700;color:var(--green)}
.sn{display:inline-block;min-width:1.9em;text-align:center;background:var(--green);color:#fff;border-radius:7px;
 padding:.06rem .3rem;font-size:.78rem;font-weight:700}
table.tbl td p{margin:0 0 .4em}
table.tbl td ul{margin:0 0 .4em;padding-left:1.05em}

/* ---------- glossary ---------- */
.gcard{background:var(--white);border:1px solid var(--line);border-left:5px solid var(--green3);border-radius:12px;
 padding:.85rem 1rem;margin:.75rem 0;box-shadow:var(--shadow)}
.ghead{display:flex;align-items:baseline;gap:.6rem;flex-wrap:wrap}
.ghead h4{margin:0;font-size:1.06rem}
.gnum{font-family:var(--mono);font-size:.76rem;color:var(--orange);font-weight:700}
.gtag{margin-left:auto;background:var(--beige2);color:var(--green);border-radius:99px;padding:.1rem .55rem;font-size:.72rem}
.lab{display:inline-block;font-size:.68rem;letter-spacing:.09em;text-transform:uppercase;color:var(--orange);
 font-weight:700;margin-right:.4rem}
.gplain{margin:.5rem 0 .5rem}
.gdeep{background:var(--beige);border-radius:10px;padding:.6rem .75rem;font-size:.94rem}
.gdeep p:last-child{margin-bottom:0}
.gwhy{margin:.5rem 0 0;font-size:.92rem;color:var(--ink2);margin:.5rem 0 0}
.code-chip{font-family:var(--mono);font-size:.85em;background:#EAF4F1;border-radius:5px;padding:.08em .32em}

/* ---------- walkthroughs ---------- */
.walk{background:var(--white);border:1px solid var(--line);border-radius:14px;padding:1.1rem 1.3rem;margin:1rem 0;
 box-shadow:var(--shadow);scroll-margin-top:74px}
.walklede{color:var(--ink2);font-size:1rem}
.walk table.tbl{font-size:.85rem}
.steps{counter-reset:st;list-style:none;padding:0}
.steps>li{counter-increment:st;position:relative;padding-left:2.3rem;margin:.55rem 0}
.steps>li:before{content:counter(st);position:absolute;left:0;top:.05rem;width:1.6rem;height:1.6rem;border-radius:50%;
 background:var(--mustard);color:#4A3708;font-weight:700;display:grid;place-items:center;font-size:.82rem}
.math{font-family:var(--mono);background:#0F3D38;color:#F4EFE6;border-radius:10px;padding:.7rem .9rem;
 overflow-x:auto;font-size:.86rem;margin:.6rem 0}
.kv{display:grid;grid-template-columns:auto 1fr;gap:.2rem .8rem;font-size:.9rem;margin:.4rem 0 .9rem}
.kv b{color:var(--green2)}

/* ---------- Q&A ---------- */
details.qa{background:var(--white);border:1px solid var(--line);border-radius:12px;margin:.5rem 0;overflow:hidden}
details.qa>summary{cursor:pointer;padding:.7rem .9rem;display:flex;gap:.7rem;align-items:flex-start;list-style:none;
 font-weight:600;color:var(--ink)}
details.qa>summary::-webkit-details-marker{display:none}
details.qa>summary:hover{background:var(--beige)}
details.qa[open]>summary{background:#EAF4F1;color:var(--green);border-bottom:1px solid var(--line)}
.qnum{font-family:var(--mono);font-size:.74rem;color:var(--orange);font-weight:700;padding-top:.15rem;flex:0 0 auto}
.qtext{flex:1 1 auto;font-weight:600;font-size:.97rem}
.qchev{transition:transform .2s;color:var(--green3);font-size:1.2rem;line-height:1}
details.qa[open] .qchev{transform:rotate(90deg)}
.abody{padding:.85rem 1rem .95rem;font-size:.95rem}
.abody p:last-child{margin-bottom:.4rem}
.qmeta{display:flex;gap:.35rem;flex-wrap:wrap;margin-top:.5rem}
.tag{background:var(--beige2);border-radius:99px;padding:.1rem .55rem;font-size:.71rem;color:var(--green)}
.tag.wt{background:#FBE4CC;color:#7A3F08}
.qgroup{margin:1.5rem 0}
.qgroup h3{display:flex;align-items:baseline;gap:.6rem;flex-wrap:wrap}
.qcount{font-size:.76rem;font-weight:600;color:var(--orange);background:var(--mustard2);border-radius:99px;padding:.12rem .6rem}
.qtools{display:flex;gap:.5rem;flex-wrap:wrap;align-items:center;margin:.8rem 0}
.qtools button{background:var(--green);color:#fff;border:0;border-radius:99px;padding:.35rem .8rem;font:inherit;
 font-size:.83rem;cursor:pointer}
.qtools button:hover{background:var(--green2)}
.qtools span{font-size:.82rem;color:var(--ink2)}

/* ---------- misc ---------- */
.hidden{display:none !important}
.math{font-family:KaTeX_Main,"Times New Roman",serif;font-size:1.03em;white-space:nowrap}
.math .katex{font-size:1.04em}
@media(max-width:760px){.math{white-space:normal;overflow-x:auto;display:inline-block;max-width:100%}}
.katex-display{margin:.6em 0;overflow-x:auto;overflow-y:hidden}
.toTop{position:fixed;right:1.1rem;bottom:1.1rem;background:var(--green);color:#fff;border:0;border-radius:99px;
 padding:.6rem .9rem;font:inherit;font-size:.85rem;cursor:pointer;box-shadow:var(--shadow);opacity:.9;z-index:50}
.toTop:hover{opacity:1}
mark{background:#FCE9A8;padding:0 .1em;border-radius:3px}
footer.foot{max-width:1560px;margin:0 auto;padding:2rem 1.6rem 3rem;color:var(--ink2);font-size:.84rem;
 border-top:1px solid var(--line)}
.grid3{display:grid;grid-template-columns:repeat(auto-fit,minmax(215px,1fr));gap:.7rem;margin:1rem 0}
.stat{background:var(--white);border:1px solid var(--line);border-radius:12px;padding:.8rem .9rem}
.stat b{display:block;font-size:1.5rem;color:var(--green);line-height:1.1}
.stat span{font-size:.82rem;color:var(--ink2)}
.two-col{columns:2;column-gap:1.6rem}
@media (max-width:900px){.two-col{columns:1}}
@media (max-width:1000px){
 .wrap{grid-template-columns:1fr}
 aside{position:static;height:auto;border-right:0;border-bottom:1px solid var(--line);max-height:260px}
 main{padding:1.1rem .9rem 5rem}
 .hero h1{font-size:1.5rem}
}
@media print{
 header.top,aside,.toTop,.qtools{display:none}
 .wrap{grid-template-columns:1fr}
 section.sec,.hero,.walk,.gcard{box-shadow:none;break-inside:avoid}
 details.qa{break-inside:avoid}
}
"""

KATEX_HEAD = (
    '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css" '
    'crossorigin="anonymous">\n'
    '<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js" '
    'crossorigin="anonymous"></script>\n'
    '<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js" '
    'crossorigin="anonymous"\n'
    "  onload=\"renderMathInElement(document.body,{delimiters:[{left:'\\\\(',right:'\\\\)',display:false},"
    "{left:'\\\\[',right:'\\\\]',display:true},{left:'$$',right:'$$',display:true}],"
    "throwOnError:false,strict:false});\"></script>"
)

JS = """
(function(){
  var tabs=document.querySelectorAll('nav.tabs button');
  var panes=document.querySelectorAll('[data-pane]');
  function show(id){
    panes.forEach(function(p){p.classList.toggle('hidden', id!=='all' && p.getAttribute('data-pane')!==id);});
    tabs.forEach(function(b){b.classList.toggle('on', b.getAttribute('data-tab')===id);});
    window.scrollTo({top:0,behavior:'instant'});
  }
  tabs.forEach(function(b){b.addEventListener('click',function(){show(b.getAttribute('data-tab'));});});
  show('all');

  var input=document.getElementById('q');
  var hit=document.getElementById('hits');
  var searchable=document.querySelectorAll('[data-search]');
  function clearMarks(root){
    root.querySelectorAll('mark').forEach(function(m){m.replaceWith(document.createTextNode(m.textContent));});
  }
  function mark(root,term){
    if(!term) return 0;
    var walker=document.createTreeWalker(root,NodeFilter.SHOW_TEXT,null);
    var nodes=[],n,c=0;
    while(n=walker.nextNode()){ if(/\\S/.test(n.nodeValue) && n.nodeValue.toLowerCase().indexOf(term)>=0) nodes.push(n); }
    nodes.forEach(function(node){
      var idx=node.nodeValue.toLowerCase().indexOf(term), frag=document.createDocumentFragment(), last=0;
      while(idx>=0){
        frag.appendChild(document.createTextNode(node.nodeValue.slice(last,idx)));
        var m=document.createElement('mark'); m.textContent=node.nodeValue.substr(idx,term.length);
        frag.appendChild(m); c++; last=idx+term.length; idx=node.nodeValue.toLowerCase().indexOf(term,last);
      }
      frag.appendChild(document.createTextNode(node.nodeValue.slice(last)));
      node.parentNode.replaceChild(frag,node);
    });
    return c;
  }
  var timer=null;
  function run(){
    var term=(input.value||'').trim().toLowerCase();
    document.querySelectorAll('mark').forEach(function(m){m.replaceWith(document.createTextNode(m.textContent));});
    if(term.length<2){ searchable.forEach(function(el){el.classList.remove('hidden');});
      document.querySelectorAll('section.sec, .walk, .gcard, .qgroup').forEach(function(el){el.classList.remove('hidden');});
      hit.textContent=''; return; }
    var n=0;
    document.querySelectorAll('section.sec, .walk, .gcard, .qgroup, .qa').forEach(function(el){
      var hitHere=el.getAttribute('data-search') && el.getAttribute('data-search').toLowerCase().indexOf(term)>=0;
      var textHit=el.innerText.toLowerCase().indexOf(term)>=0;
      if(el.tagName==='DETAILS'){
        if(!textHit){el.classList.add('hidden');}
        else {el.classList.remove('hidden'); el.open=true; n++;}
        return;
      }
      if(!hitHere && !textHit){el.classList.add('hidden');}
      else {el.classList.remove('hidden'); n++;}
    });
    hit.textContent=n+' block'+(n===1?'':'s');
    document.body.classList.add('focus');
  }
  input.addEventListener('input',function(){clearTimeout(timer);timer=setTimeout(run,180);});
  input.addEventListener('keydown',function(e){if(e.key==='Escape'){input.value='';run();}});
  document.addEventListener('keydown',function(e){
    if(e.key==='/' && document.activeElement!==input){e.preventDefault();input.focus();}
  });
  document.getElementById('expand').addEventListener('click',function(){
    var open=this.dataset.open==='1';
    document.querySelectorAll('details.qa').forEach(function(d){d.open=!open;});
    this.dataset.open=open?'0':'1'; this.textContent=open?'Expand all answers':'Collapse all answers';
  });
  document.getElementById('focusbtn').addEventListener('click',function(){
    document.body.classList.toggle('focus');
    this.textContent=document.body.classList.contains('focus')?'Show sidebar':'Hide sidebar';
  });
  document.getElementById('totop').addEventListener('click',function(){window.scrollTo({top:0,behavior:'smooth'});});
  document.querySelectorAll('aside a').forEach(function(a){
    a.addEventListener('click',function(){ if(document.body.classList.contains('focus')) { document.body.classList.remove('focus'); } });
  });
})();
"""


def build(out_path=DEFAULT_OUT):
    body = []

    # ---- tabs
    tabs = [("all", "Everything")] + [(p["id"], p["label"]) for p in content_map.PANES_PLACEHOLDER]
    tabbar = "".join('<button data-tab="%s">%s</button>' % (i, esc(l)) for i, l in tabs)
    panes = {p["id"] for p in content_map.PANES_PLACEHOLDER}

    def wrap_pane(pid, inner):
        if pid not in panes:
            return inner
        return '<div data-pane="%s">%s</div>' % (pid, inner)

    # ---- hero / overview
    body.append(wrap_pane("map", content_map.render_hero() + content_map.render_deckmap()))

    # ---- sections
    secs = content_map.SECTIONS + content_map2.SECTIONS
    body.append(wrap_pane("sections", content_map.render_sections_intro() + "\n".join(render_section(s) for s in secs)))

    # ---- technical deep dive
    tech_intro = content_tech.render_intro()
    walks = render_walkthroughs(content_tech.WALKTHROUGHS)
    gloss = render_glossary(content_tech.GLOSSARY)
    body.append(wrap_pane("tech", tech_intro
                          + '<section class="sec" id="walk"><h2>Concept walkthroughs</h2>'
                            '<p class="walklede">Twelve worked explanations, from the three-piece band to the accuracy-diversity trade. '
                            'Read these if any slide in sections 3 to 6 feels like a formula you can recite but not defend.</p>'
                          + walks + "</section>"
                          + '<section class="sec" id="glossary"><h2>Beginner glossary: every technical term on the deck</h2>'
                            '<p class="walklede">%d entries. Each one gives a one-line plain definition, the deeper mechanism, '
                            'and the exact place the term earns its keep in this thesis. Use the search box in the header to find a term fast.</p>'
                            % len(content_tech.GLOSSARY)
                          + gloss + "</section>"))

    # ---- section 7
    body.append(wrap_pane("sec7", content_extra.render_sec7()))

    # ---- Q&A
    qa_html, qn = render_qa(content_qa1.GROUPS + content_qa2.GROUPS)
    body.append(wrap_pane("qa", content_extra.render_qa_intro(qn)
                          + '<div class="qtools">'
                            '<button id="expand" data-open="0">Expand all answers</button>'
                            '<span>Click any question to open it. Answers are written to be spoken in about 45–75 seconds.</span>'
                          '</div>' + qa_html))

    # ---- cheat sheets
    body.append(wrap_pane("cheat", content_extra.render_cheat()))

    css, js = CSS, JS
    doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Viva Presentation Guide · Mouad LOUHICHI · PhD Defence 2026</title>
<meta name="description" content="Section-by-section presentation guide, beginner-level technical deep dive and 100 defence questions for the PhD viva of Mouad Louhichi.">
{KATEX_HEAD}
<style>{css}</style>
</head>
<body>
<header class="top">
  <div class="top-in">
    <div class="brand">
      <b>Viva Presentation Guide</b>
      <span>Mouad LOUHICHI · PhD Defence · ENSIAS / UM5 Rabat 2026</span>
    </div>
    <nav class="tabs">{tabbar}</nav>
    <div class="searchbox">
      <input id="q" type="search" placeholder="Search a term, a slide, a question…  (press /)" autocomplete="off">
      <span class="hits" id="hits"></span>
    </div>
    <button id="focusbtn" style="background:rgba(255,255,255,.1);color:#F7F3EC;border:1px solid rgba(255,255,255,.2);border-radius:99px;padding:.32rem .7rem;font:inherit;font-size:.82rem;cursor:pointer">Hide sidebar</button>
  </div>
</header>
<div class="wrap">
  <aside>
    {content_map.render_sidebar()}
  </aside>
  <main>
    {''.join(body)}
  </main>
</div>
<footer class="foot">
  <p><strong>Built for:</strong> <code>try/MOUAD_LOUHICHI_VIVA_40min_BeigeGreen_v32.pptx</code> (79 slides) ·
  <strong>Sources:</strong> MOUAD_LOUHICHI_Thesis.pdf (159 pp), the three source papers, the French résumé,
  the version history and README of try/viva_builder, DEEP_READING_REVIEW_v25.md, and a full extraction of every
  slide, table cell and speaker note of v32.</p>
  <p>Every number quoted in this guide was checked against the thesis or the source papers. Where the deck and the
  thesis differ in scope, the guide says so explicitly rather than smoothing it over. Generated by
  <code>try/viva_builder/viva_guide/build.py</code>; it does not modify the deck, the thesis or any PDF.</p>
</footer>
<button class="toTop" id="totop">↑ Top</button>
<script>{js}</script>
</body>
</html>
"""
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(doc)
    print("wrote", out_path, "%.0f KB" % (os.path.getsize(out_path) / 1024.0), "·", qn, "questions")
    return out_path


if __name__ == "__main__":
    build(sys.argv[1] if len(sys.argv) > 1 else DEFAULT_OUT)
