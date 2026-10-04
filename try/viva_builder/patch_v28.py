#!/usr/bin/env python3
# ---------------------------------------------------------------------------
# patch_v28.py: v27 -> v28
#
# Two changes only:
#
#   titles     slides 1 and 76 (the same title block, opening and closing
#              slide) spell out the acronym: "Explainable Artificial
#              Intelligence in Recommendation Systems" instead of
#              "Explainable AI ...". The two lines are re-broken as
#                Cooperative Game Theory for Explainable
#                Artificial Intelligence in Recommendation Systems
#              and the font stays at 50 pt with the same line spacing. The
#              script measures the two lines against the 17.8 in box with the
#              metrics of the font embedded in the file (Roca Two Bold), so
#              "it fits" is a measurement, not an estimate.
#
#   note 6     the speech on slide 6 is rewritten in spoken register: short
#              sentences, direct questions, no written-essay phrasing. It says
#              the same three things as the two cards on the slide.
# ---------------------------------------------------------------------------
import io
import json
import os
import zipfile

from pptx import Presentation

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "MOUAD_LOUHICHI_VIVA_40min_BeigeGreen_v27.pptx")
DST = os.path.join(HERE, "..", "MOUAD_LOUHICHI_VIVA_40min_BeigeGreen_v28.pptx")
NOTES_IN = os.path.join(HERE, "notes_v27.json")
NOTES_OUT = os.path.join(HERE, "notes_v28.json")

WPM = 130.0

OLD_L1 = "Cooperative Game Theory for"
OLD_L2 = "Explainable AI in Recommendation Systems"
NEW_L1 = "Cooperative Game Theory for Explainable"
NEW_L2 = "Artificial Intelligence in Recommendation Systems"
TITLED_SLIDES = (1, 76)

SPOKEN_NOTE_6 = (
    "Let me put this in context.\n\n"
    "Recommendation systems started with similarity models, then matrix "
    "factorisation, then neural and graph models, and now hypergraphs. "
    "Each step made the ranking stronger, and each step hid more of the "
    "reasoning. So the gap keeps growing: the models do more, and we can "
    "explain less.\n\n"
    "Why does this matter? Three reasons. Users get outputs without any "
    "reason, so trust drops. Designers cannot debug what they cannot "
    "inspect. And regulators now ask for transparency.\n\n"
    "So what does this thesis argue? That attribution belongs inside the "
    "model, not added on afterwards. That one method should stay consistent "
    "at every level of detail, from the global picture down to a single "
    "cluster. And that the explanation has to speak the language of the "
    "domain, otherwise nobody can act on it."
)


# ---------------------------------------------------------------------------
# measuring with the font that is actually embedded in the deck
# ---------------------------------------------------------------------------
def embedded_font(path, typeface):
    """Pull a named font out of the pptx (Canva wraps it in a 188-270 byte
    preface, so the real font is found by its signature)."""
    from fontTools.ttLib import TTFont
    z = zipfile.ZipFile(path)
    rels = z.read("ppt/_rels/presentation.xml.rels").decode()
    pres = z.read("ppt/presentation.xml").decode()
    import re
    # map typeface -> rId -> part
    rid = None
    for m in re.finditer(r'<p:embeddedFont>(.*?)</p:embeddedFont>', pres, re.S):
        block = m.group(1)
        if f'typeface="{typeface}"' in block:
            rid = re.search(r'r:id="(rId\d+)"', block).group(1)
    if rid is None:
        return None
    part = re.search(rf'Id="{rid}"[^>]*Target="([^"]+)"', rels).group(1)
    if not part.startswith("ppt/"):
        part = "ppt/" + part.lstrip("/")
    data = z.read(part)
    for off in range(0, 4096):
        if data[off:off + 4] in (b"OTTO", b"\x00\x01\x00\x00", b"true"):
            try:
                return TTFont(io.BytesIO(data[off:]), lazy=True)
            except Exception:
                continue
    return None


def text_width_pt(font, text, size_pt, tracking_pt=0.0):
    upm = font["head"].unitsPerEm
    cmap = font.getBestCmap()
    hmtx = font["hmtx"]
    return sum(hmtx[cmap.get(ord(ch)) or cmap.get(ord("?"))][0] / upm * size_pt
               for ch in text) + tracking_pt * len(text)


def main():
    prs = Presentation(SRC)
    report = []

    # --- the title on slides 1 and 76 --------------------------------------
    for slide_no in TITLED_SLIDES:
        hit = False
        for sh in prs.slides[slide_no - 1].shapes:
            if not sh.has_text_frame:
                continue
            paras = sh.text_frame.paragraphs
            texts = [p.text for p in paras]
            if len(texts) == 2 and texts[0] == OLD_L1 and texts[1] == OLD_L2:
                for para, new in zip(paras, (NEW_L1, NEW_L2)):
                    runs = para.runs
                    runs[0].text = new
                    for r in runs[1:]:
                        r._r.getparent().remove(r._r)
                hit = True
                break
        report.append(f"slide {slide_no} title: {'rewritten' if hit else '!! NOT FOUND'}")

    # --- the spoken note for slide 6 ---------------------------------------
    notes = json.load(open(NOTES_IN))
    prs.slides[5].notes_slide.notes_text_frame.text = SPOKEN_NOTE_6
    notes["6"] = SPOKEN_NOTE_6
    report.append(f"note 6: rewritten in spoken register ({len(SPOKEN_NOTE_6.split())} words)")

    prs.save(DST)
    json.dump(notes, open(NOTES_OUT, "w"), ensure_ascii=False, indent=1)

    # --- does the new title still fit? -------------------------------------
    try:
        font = embedded_font(SRC, "Roca Two Bold")
        if font is not None:
            box = 17.8 * 72
            report.append("title width, measured with the embedded Roca Two Bold at 50 pt, "
                          f"tracking -3 pt/char, box {box:.0f} pt:")
            for line in (NEW_L1, NEW_L2, OLD_L2):
                w = text_width_pt(font, line, 50, -3.0)
                report.append(f"   {w:7.1f} pt  ({w / box * 100:5.1f} % of the box)  {line!r}")
        else:
            report.append("title width: font not found, not measured")
    except Exception as exc:                                   # pragma: no cover
        report.append(f"title width: skipped ({exc})")

    spoken = sum(len(notes[str(i)].split()) for i in range(1, 77))
    report.append(f"wrote {os.path.relpath(DST, HERE)}")
    report.append(f"wrote {os.path.relpath(NOTES_OUT, HERE)}")
    report.append(f"spoken words slides 1-76: {spoken}  "
                  f"({spoken / WPM:.1f} min @130 wpm, {spoken / 120:.1f} @120 wpm)")
    for block, lo, hi in [("Intro 3-7", 3, 7), ("Context 8-16", 8, 16), ("Protocol 17-25", 17, 25),
                          ("C1 26-37", 26, 37), ("C2 38-50", 38, 50), ("C3 51-66", 51, 66),
                          ("Conclusion 67-76", 67, 76)]:
        w = sum(len(notes[str(i)].split()) for i in range(lo, hi + 1))
        report.append(f"   {block:<16} {w:>5} words  {w / WPM:>4.1f} min")
    print("\n".join(report))
    return prs, notes


if __name__ == "__main__":
    main()
