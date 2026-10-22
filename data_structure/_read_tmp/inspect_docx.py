# -*- coding: utf-8 -*-
import sys, io
from docx import Document
from docx.shared import Pt

path = sys.argv[1]
doc = Document(path)

def rpr(r):
    f = r.font
    bits = []
    if f.name:
        bits.append("ascii=%s" % f.name)
    rPr = r._element.rPr
    if rPr is not None:
        ea = rPr.find('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}rFonts')
        if ea is not None:
            v = ea.get('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}eastAsia')
            if v:
                bits.append("ea=%s" % v)
    if f.size:
        bits.append("%gpt" % (f.size / 12700.0))
    if f.bold:
        bits.append("B")
    if f.italic:
        bits.append("I")
    if f.color and f.color.rgb:
        bits.append("color=%s" % (f.color.rgb,))
    return ",".join(bits)

out = io.open(sys.argv[2], "w", encoding="utf-8")
out.write("=== STYLE DEFS ===\n")
for s in doc.styles:
    try:
        if s.type is None:
            continue
    except Exception:
        continue
    try:
        f = s.font
        extra = []
        if f.name: extra.append("ascii=%s" % f.name)
        if f.size: extra.append("%gpt" % (f.size / 12700.0))
        if f.bold: extra.append("B")
        pf = s.paragraph_format
        if pf.alignment is not None: extra.append("align=%s" % pf.alignment)
        if pf.space_before is not None: extra.append("sb=%g" % (pf.space_before.pt))
        if pf.space_after is not None: extra.append("sa=%g" % (pf.space_after.pt))
        if pf.line_spacing is not None: extra.append("ls=%s" % (pf.line_spacing,))
        if pf.first_line_indent is not None: extra.append("fli=%g" % (pf.first_line_indent.pt))
        out.write("%-22s %s\n" % (s.name, " ".join(extra)))
    except Exception as e:
        out.write("%-22s <err %s>\n" % (s.name, e))

out.write("\n=== PARAGRAPHS (body xml order) ===\n")
from docx.oxml.ns import qn
from docx.oxml.table import CT_Tbl
from docx.oxml.text.paragraph import CT_P
from docx.text.paragraph import Paragraph
from docx.table import Table

for child in doc.element.body.iterchildren():
    if isinstance(child, CT_P):
        p = Paragraph(child, doc)
        pf = p.paragraph_format
        out.write("P style=%s align=%s sb=%s sa=%s ls=%s fli=%s li=%s\n" % (
            p.style.name, pf.alignment,
            pf.space_before.pt if pf.space_before else None,
            pf.space_after.pt if pf.space_after else None,
            pf.line_spacing,
            pf.first_line_indent.pt if pf.first_line_indent else None,
            pf.left_indent.pt if pf.left_indent else None))
        out.write("   text=%r\n" % p.text)
        for i, r in enumerate(p.runs):
            out.write("   run%d %r [%s]\n" % (i, r.text, rpr(r)))
        if 'graphicData' in p._p.xml:
            out.write("   <has image>\n")
    elif isinstance(child, CT_Tbl):
        t = Table(child, doc)
        out.write("TABLE %dx%d style=%s\n" % (len(t.rows), len(t.columns), t.style.name if t.style else None))
out.close()
print("ok")
