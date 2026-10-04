#!/usr/bin/env python3
"""
Build the multi-page HTML site version of the viva guide.

    python3 build_site.py      # writes ../../../MOUAD_LOUHICHI_VIVA_PRESENTATION_GUIDE/

Same content as build.py's single file, split into one HTML page per part
(overview, one page per deck section, walkthroughs, glossary, section 7,
Q&A by category, cheat sheets) sharing assets/style.css and assets/app.js.
Equations are TeX rendered with KaTeX (CDN).
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import build as b          # noqa: E402
import content_map         # noqa: E402
import content_map2        # noqa: E402
import content_tech        # noqa: E402
import content_qa1         # noqa: E402
import content_qa2         # noqa: E402
import content_extra       # noqa: E402

SITE = os.path.join(b.ROOT, "MOUAD_LOUHICHI_VIVA_PRESENTATION_GUIDE")

SECS = content_map.SECTIONS + content_map2.SECTIONS
GROUPS = content_qa1.GROUPS + content_qa2.GROUPS
QA_FILES = {"A": "qa-a.html", "B": "qa-b.html", "C": "qa-c.html", "D": "qa-d.html",
            "E": "qa-e.html", "F": "qa-f.html", "G": "qa-g.html", "H": "qa-h.html"}

# --------------------------------------------------------------------------
# page inventory
# --------------------------------------------------------------------------
def _playbook_file(sec):
    return "playbook-%s.html" % sec["id"]


PAGES = [
    ("index.html", "Overview & deck map",
     "The deck in one page, the timing ledger, how every section is built, ten delivery rules"),
]
for _s in SECS:
    PAGES.append((_playbook_file(_s), "Playbook · %s" % _s["title"],
                  "How to present slides %s: %s" % (_s["range"], _s["kicker"])))
PAGES += [
    ("walkthroughs.html", "Technical deep dive · 12 walkthroughs",
     "Worked explanations for every hard idea in sections 3 to 6"),
    ("glossary.html", "Technical deep dive · glossary",
     "Every technical term on the deck, explained for a beginner"),
    ("section-07-delivery.html", "Section 7 · delivery plan",
     "How to present the conclusion: five beats, register, pauses, rehearsal"),
    ("qa.html", "Q&A · 100 questions",
     "How to handle the discussion, and the 100 defence questions by category"),
]
for _letter, _f in QA_FILES.items():
    PAGES.append((_f, "Q&A %s" % _letter, ""))
PAGES += [
    ("cheat-numbers.html", "Cheat · every number in one table",
     "The number sheet: datasets, contributions, significance, cost"),
    ("cheat-never-say.html", "Cheat · never say / always say",
     "The scope fences, phrased as things to avoid and things to say instead"),
    ("cheat-checklist.html", "Cheat · pre-defence checklist",
     "The twelve items to check the night before the defence"),
]

# sidebar anchor -> page
ANCHOR_PAGE = {
    "overview": "index.html", "timing": "index.html", "anatomy": "index.html",
    "rules": "index.html", "sections-intro": "index.html",
    "tech-intro": "walkthroughs.html", "walk": "walkthroughs.html",
    "glossary": "glossary.html", "sec7": "section-07-delivery.html",
    "qa-intro": "qa.html", "numbers": "cheat-numbers.html",
    "never": "cheat-never-say.html", "checklist": "cheat-checklist.html",
}
for _s in SECS:
    ANCHOR_PAGE["sec-" + _s["id"]] = _playbook_file(_s)
for _g in GROUPS:
    _letter = b.re.match(r"\s*([A-H])", _g["title"]).group(1)
    ANCHOR_PAGE["qa-" + b.qa_anchor(_g["title"])] = QA_FILES[_letter]


def esc(s):
    return b.esc(s)


def render_site_nav(current):
    out = ['<h5>Pages</h5>']
    for fname, label, _d in PAGES:
        cls = ' class="cur"' if fname == current else ""
        out.append('<a href="%s"%s>%s</a>' % (fname, cls, esc(label)))
    out.append("<h5>Jump to</h5>")
    for group, items in content_map.SIDEBAR:
        for anchor, label in items:
            target = ANCHOR_PAGE.get(anchor, "index.html")
            href = "#%s" % anchor if target == current else "%s#%s" % (target, anchor)
            out.append('<a href="%s">%s</a>' % (href, esc(label)))
    return "\n".join(out)


def pager(current):
    files = [p[0] for p in PAGES]
    i = files.index(current)
    prevs = PAGES[i - 1] if i > 0 else None
    nexts = PAGES[i + 1] if i + 1 < len(PAGES) else None
    mid = '<a class="p-home" href="index.html">▲ All pages</a>'
    left = ('<a class="p-prev" href="%s">‹ %s</a>' % (prevs[0], esc(prevs[1]))) if prevs else "<span></span>"
    right = ('<a class="p-next" href="%s">%s ›</a>' % (nexts[0], esc(nexts[1]))) if nexts else "<span></span>"
    return '<nav class="pager">%s%s%s</nav>' % (left, mid, right)


CSS_SITE = """
aside a.cur{background:var(--green);color:#fff}
aside .pages{display:block}
.crumbs{display:flex;gap:.5rem;align-items:center;font-size:.88rem;opacity:.95}
.crumbs a{color:#F7F3EC;text-decoration:underline;opacity:.9}
.pager{display:flex;justify-content:space-between;gap:1rem;margin:2.5rem 0 1rem;flex-wrap:wrap}
.pager a{display:inline-block;padding:.55rem .95rem;border-radius:12px;border:1px solid var(--green3);
 background:#fff;color:var(--green);text-decoration:none;font-weight:600;font-size:.9rem}
.pager a:hover{background:var(--green);color:#fff}
.p-home{opacity:.85}
.qindex td a{font-weight:600}
"""

JS_SITE = """
(function(){
  var input=document.getElementById('q');
  var hit=document.getElementById('hits');
  if(!input) return;
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
    if(term.length<2){
      document.querySelectorAll('section.sec, .walk, .gcard, .qgroup, .qa').forEach(function(el){el.classList.remove('hidden');});
      hit.textContent=''; return;
    }
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
  }
  input.addEventListener('input',function(){clearTimeout(timer);timer=setTimeout(run,180);});
  input.addEventListener('keydown',function(e){if(e.key==='Escape'){input.value='';run();}});
  document.addEventListener('keydown',function(e){
    if(e.key==='/' && document.activeElement!==input){e.preventDefault();input.focus();}
  });
  var exp=document.getElementById('expand');
  if(exp) exp.addEventListener('click',function(){
    var open=this.dataset.open==='1';
    document.querySelectorAll('details.qa').forEach(function(d){d.open=!open;});
    this.dataset.open=open?'0':'1'; this.textContent=open?'Expand all answers':'Collapse all answers';
  });
  var tt=document.getElementById('totop');
  if(tt) tt.addEventListener('click',function(){window.scrollTo({top:0,behavior:'smooth'});});
})();
"""


def page(fname, title, desc, body):
    doc = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>%s · Viva Presentation Guide</title>
<meta name="description" content="%s">
%s
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<header class="top">
  <div class="top-in">
    <div class="brand">
      <b>Viva Presentation Guide</b>
      <span>Mouad LOUHICHI · PhD Defence · ENSIAS / UM5 Rabat 2026</span>
    </div>
    <nav class="crumbs"><a href="index.html">Overview</a><span>›</span><b>%s</b></nav>
    <div class="searchbox">
      <input id="q" type="search" placeholder="Search this page…  (press /)" autocomplete="off">
      <span class="hits" id="hits"></span>
    </div>
  </div>
</header>
<div class="wrap">
  <aside>
%s
  </aside>
  <main>
%s
  </main>
</div>
%s
<footer class="foot">
  <p><strong>Built for:</strong> <code>try/MOUAD_LOUHICHI_VIVA_40min_BeigeGreen_v28.pptx</code> (79 slides) ·
  <strong>Sources:</strong> MOUAD_LOUHICHI_Thesis.pdf (159 pp), the three source papers, the French résumé,
  and a full extraction of every slide, table cell and speaker note of v28.</p>
  <p>Every number quoted in this guide was checked against the thesis or the source papers. Generated by
  <code>try/viva_builder/viva_guide/build_site.py</code>; it does not modify the deck, the thesis or any PDF.</p>
</footer>
<button class="toTop" id="totop">↑ Top</button>
<script src="assets/app.js"></script>
</body>
</html>
""" % (esc(title), esc(desc), b.KATEX_HEAD, esc(title), render_site_nav(fname), body, pager(fname))
    path = os.path.join(SITE, fname)
    with open(path, "w", encoding="utf-8") as f:
        f.write(doc)


# --------------------------------------------------------------------------
# Q&A helpers (same markup and global numbering as the single-file build)
# --------------------------------------------------------------------------
def render_qa_group(g, start):
    n = start - 1
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
            % (qid, esc(b.plain(q["q"])), esc(b.plain(q["a"])), esc(g["title"]), n,
               b.md(q["q"]), b.md(q["a"]),
               esc(g["title"]),
               ("".join('<span class="tag wt">%s</span>' % esc(t) for t in q.get("tags", []))))
        )
    return ('<div class="qgroup" id="qa-%s"><h2>%s <span class="qcount">%d questions</span></h2>%s</div>'
            % (b.qa_anchor(g["title"]), esc(g["title"]), len(g["items"]), "".join(items)))


# --------------------------------------------------------------------------
# build
# --------------------------------------------------------------------------
def build():
    os.makedirs(os.path.join(SITE, "assets"), exist_ok=True)
    with open(os.path.join(SITE, "assets", "style.css"), "w", encoding="utf-8") as f:
        f.write(b.CSS + CSS_SITE)
    with open(os.path.join(SITE, "assets", "app.js"), "w", encoding="utf-8") as f:
        f.write(JS_SITE)

    # ---- index
    page("index.html", "Overview & deck map",
         "The deck in one page, the timing ledger, how every section is built, ten delivery rules",
         content_map.render_hero() + content_map.render_deckmap() + content_map.render_sections_intro())

    # ---- one page per deck section
    for sec in SECS:
        page(_playbook_file(sec), "Playbook · %s" % sec["title"],
             "How to present slides %s" % sec["range"],
             b.render_section(sec))

    # ---- technical deep dive
    page("walkthroughs.html", "Technical deep dive · 12 walkthroughs",
         "Worked explanations for every hard idea in sections 3 to 6",
         content_tech.render_intro()
         + '<section class="sec" id="walk"><h2>Concept walkthroughs</h2>'
           '<p class="walklede">Twelve worked explanations, from the three-piece band to the '
           'accuracy-diversity trade. Read these if any slide in sections 3 to 6 feels like a '
           'formula you can recite but not defend.</p>'
         + b.render_walkthroughs(content_tech.WALKTHROUGHS) + "</section>")

    page("glossary.html", "Technical deep dive · glossary",
         "Every technical term on the deck, explained for a beginner",
         '<section class="sec" id="glossary"><h2>Beginner glossary: every technical term on the deck</h2>'
         '<p class="walklede">%d entries. Each one gives a one-line plain definition, the deeper mechanism, '
         'and the exact place the term earns its keep in this thesis. Use the search box to find a term fast.</p>'
         % len(content_tech.GLOSSARY)
         + b.render_glossary(content_tech.GLOSSARY) + "</section>")

    # ---- section 7
    page("section-07-delivery.html", "Section 7 · delivery plan",
         "How to present the conclusion: five beats, register, pauses, rehearsal",
         content_extra.render_sec7())

    # ---- Q&A
    qn = sum(len(g["items"]) for g in GROUPS)
    rows = []
    n = 0
    for g in GROUPS:
        letter = b.re.match(r"\s*([A-H])", g["title"]).group(1)
        start = n + 1
        n += len(g["items"])
        rows.append((letter, g["title"], len(g["items"]), "Q%03d–Q%03d" % (start, n), QA_FILES[letter]))
    index_tbl = b.table(
        ["", "Category", "Questions", "Range", "Open"],
        [[r[0], r[1], str(r[2]), r[3], '<a href="%s">%s ›</a>' % (r[4], r[4])] for r in rows],
        cls="tbl qindex")
    page("qa.html", "Q&A · 100 questions",
         "How to handle the discussion, and the 100 defence questions by category",
         content_extra.render_qa_intro(qn)
         + '<div class="qtools"><span>One page per category. Click any question to open the answer; '
           'answers are written to be spoken in about 45–75 seconds.</span></div>'
         + index_tbl)

    n = 0
    for g in GROUPS:
        letter = b.re.match(r"\s*([A-H])", g["title"]).group(1)
        start = n + 1
        n += len(g["items"])
        page(QA_FILES[letter], "Q&A %s" % letter,
             "Questions Q%03d–Q%03d" % (start, n),
             '<div class="qtools"><button id="expand" data-open="0">Expand all answers</button>'
             '<span><a href="qa.html">‹ back to the Q&amp;A index</a></span></div>'
             + render_qa_group(g, start))

    # ---- cheat sheets (one page per sheet)
    cheat = content_extra.render_cheat()
    parts = re.split(r'(?=<section class="sec" id="(?:numbers|never|checklist)">)', cheat)
    titles = {"numbers": ("cheat-numbers.html", "Cheat · every number in one table",
                          "The number sheet: datasets, contributions, significance, cost"),
              "never": ("cheat-never-say.html", "Cheat · never say / always say",
                        "The scope fences, phrased as things to avoid and things to say instead"),
              "checklist": ("cheat-checklist.html", "Cheat · pre-defence checklist",
                            "The twelve items to check the night before the defence")}
    for part in parts:
        m = re.search(r'<section class="sec" id="(numbers|never|checklist)">', part or "")
        if not m:
            continue
        fname, title, desc = titles[m.group(1)]
        page(fname, title, desc, part)

    written = len([p for p in PAGES if os.path.exists(os.path.join(SITE, p[0]))])
    print("wrote site:", SITE, "·", written, "pages ·", qn, "questions")


if __name__ == "__main__":
    build()
