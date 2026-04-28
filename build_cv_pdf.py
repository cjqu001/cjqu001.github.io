"""Generate cv.pdf from cv.md. Used by .github/workflows/build-cv.yml."""
import re
import markdown
from weasyprint import HTML, CSS

with open('cv.md', 'r') as f:
    md = f.read()

# Strip Jekyll frontmatter
md = re.sub(r'^---\n.*?\n---\n', '', md, count=1, flags=re.DOTALL)

# Strip the "Download PDF" line so it doesn't appear inside the PDF itself
md = re.sub(r'\[\*\*Download CV \(PDF\)\*\*\][^\n]*\n', '', md)

# Header block at top of CV
header_md = (
    "# Christian J. Quinones, MD\n\n"
    "Family Medicine Physician — Research, Systems, and Infrastructure  \n"
    "[cjqu001.github.io](https://cjqu001.github.io)\n\n"
    "---\n\n"
)
md = header_md + md.lstrip()

html_body = markdown.markdown(md, extensions=['extra', 'sane_lists'])
html = f"""<!doctype html><html><head><meta charset='utf-8'><title>Christian J. Quinones, MD — CV</title></head><body>{html_body}</body></html>"""

css = CSS(string="""
@page {
  size: Letter;
  margin: 0.6in 0.7in;
  @bottom-right { content: counter(page) " / " counter(pages); font-family: Georgia, serif; font-size: 9pt; color: #888; }
  @bottom-left  { content: "Christian J. Quinones, MD"; font-family: Georgia, serif; font-size: 9pt; color: #888; }
}
body { font-family: Georgia, "Times New Roman", serif; font-size: 10.5pt; line-height: 1.45; color: #222; }
h1 { font-size: 22pt; margin: 0 0 4pt 0; letter-spacing: 0.5pt; }
h1 + p { margin-top: 0; color: #555; font-size: 11pt; }
h2 { font-size: 13pt; border-bottom: 1px solid #999; padding-bottom: 2pt; margin-top: 16pt; margin-bottom: 6pt; text-transform: uppercase; letter-spacing: 0.6pt; }
h3 { font-size: 11pt; margin: 8pt 0 2pt 0; font-style: italic; font-weight: 600; }
hr { border: none; border-top: 1px solid #bbb; margin: 8pt 0 12pt 0; }
ul { margin: 4pt 0 4pt 18pt; padding: 0; }
li { margin-bottom: 3pt; }
p  { margin: 4pt 0; }
em { color: #444; }
a  { color: #2a5298; text-decoration: none; }
""")

HTML(string=html).write_pdf('cv.pdf', stylesheets=[css])
print("cv.pdf written")
