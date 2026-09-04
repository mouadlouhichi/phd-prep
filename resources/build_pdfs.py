#!/usr/bin/env python3
"""Render the three defense resources to PDF.

Reads the markdown files in this directory and produces matching .pdf files with
a simple, readable layout (headers, body, bullets) using fpdf2.  No external
HTML/Pandoc dependency.
"""
import os, re
from fpdf import FPDF

HERE = os.path.dirname(os.path.abspath(__file__))

ACCENT = (0x0E, 0x7C, 0x7B)
DARK   = (0x22, 0x30, 0x3C)
BODY   = (0x2F, 0x3B, 0x49)

# DejaVu fonts ship with the environment and support the unicode used in the docs.
def _fonts():
    base = "/usr/share/fonts/truetype/dejavu/"
    reg   = os.path.join(base, "DejaVuSans.ttf")
    bold  = os.path.join(base, "DejaVuSans-Bold.ttf")
    return reg, bold


class PDF(FPDF):
    def header(self):
        if self.page_no() <= 1:
            return
        self.set_font("DejaVu", "", 8)
        self.set_text_color(*BODY)
        self.cell(0, 7, "Defense resources — Mouad Louhichi", align="C")
        self.ln(8)

    def footer(self):
        self.set_y(-14)
        self.set_font("DejaVu", "", 8)
        self.set_text_color(*BODY)
        self.cell(0, 8, f"{self.page_no()}", align="C")


def _clean(line):
    # strip markdown emphasis markers for PDF text
    return re.sub(r'[*_`]', '', line)


def render(md_path, out_path):
    reg, bold = _fonts()
    pdf = PDF(format="A4")
    pdf.set_auto_page_break(auto=True, margin=18)
    pdf.add_font("DejaVu", "", reg)
    pdf.add_font("DejaVu", "B", bold)
    # fpdf2 needs an 'I' face registered; reuse the regular file (no true italic
    # available on the system) so blockquotes don't error.
    pdf.add_font("DejaVu", "I", reg)
    pdf.set_margins(20, 20, 20)
    pdf.add_page()

    title_done = False
    with open(md_path, encoding="utf-8") as fh:
        lines = fh.read().split("\n")

    for line in lines:
        s = line.rstrip()
        if not s.strip():
            pdf.ln(3)
            continue
        # H1
        if s.startswith("# "):
            text = _clean(s[2:].strip())
            pdf.set_font("DejaVu", "B", 19)
            pdf.set_text_color(*ACCENT)
            pdf.multi_cell(0, 10, text)
            pdf.ln(3)
            # title rule
            pdf.set_draw_color(*ACCENT); pdf.set_line_width(0.6)
            pdf.line(20, pdf.get_y(), 190, pdf.get_y())
            pdf.ln(5)
            continue
        # H2
        if s.startswith("## "):
            text = _clean(s[3:].strip())
            pdf.set_font("DejaVu", "B", 15)
            pdf.set_text_color(*DARK)
            pdf.multi_cell(0, 8, text)
            pdf.ln(2)
            continue
        # H3
        if s.startswith("### "):
            text = _clean(s[4:].strip())
            pdf.set_font("DejaVu", "B", 12)
            pdf.set_text_color(*DARK)
            pdf.multi_cell(0, 7, text)
            pdf.ln(1)
            continue
        # table-ish line or horizontal rule
        if s.startswith("---"):
            pdf.set_draw_color(*BODY); pdf.set_line_width(0.3)
            pdf.line(20, pdf.get_y(), 190, pdf.get_y())
            pdf.ln(3)
            continue
        # bullet line
        m = re.match(r'^(\s*)- (.*)$', s)
        if m:
            indent = len(m.group(1))
            text = _clean(m.group(2))
            pdf.set_font("DejaVu", "", 11)
            pdf.set_text_color(*BODY)
            left = 22 + indent * 4
            pdf.set_x(left)
            pdf.multi_cell(0, 6, "\u2022 " + text)
            pdf.ln(1)
            continue
        # numbered list item
        m = re.match(r'^(\s*)(\d+[.)])\s+(.*)$', s)
        if m:
            indent = len(m.group(1))
            num = m.group(2)
            text = _clean(m.group(3))
            pdf.set_font("DejaVu", "B", 11)
            pdf.set_text_color(*DARK)
            left = 22 + indent * 4
            pdf.set_x(left)
            pdf.multi_cell(0, 6, f"{num} {text}")
            pdf.ln(1)
            continue
        # blockquote
        if s.startswith(">"):
            text = _clean(s.lstrip("> ").strip())
            pdf.set_font("DejaVu", "I", 11)
            pdf.set_text_color(*ACCENT)
            pdf.set_x(24)
            pdf.multi_cell(0, 6, text)
            pdf.set_text_color(*BODY)
            pdf.ln(1)
            continue
        # plain paragraph
        pdf.set_font("DejaVu", "", 11)
        pdf.set_text_color(*BODY)
        pdf.multi_cell(0, 6, _clean(s.strip()))
        pdf.ln(1)

    pdf.output(out_path)
    print(f"wrote {out_path} ({pdf.page_no()} pages)")


if __name__ == "__main__":
    for md, pdf in [
        ("learn_the_thesis.md", "learn_the_thesis.pdf"),
        ("40min_speech.md", "40min_speech.pdf"),
        ("qa_bank.md", "qa_bank.pdf"),
    ]:
        render(os.path.join(HERE, md), os.path.join(HERE, pdf))
