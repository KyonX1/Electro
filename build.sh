#!/usr/bin/env bash
set -euo pipefail

SKILL_DIR="$HOME/.agents/skills/pandoc-pdf-generation/assets"
LATEX_PREAMBLE="$SKILL_DIR/table-spacing-template.tex"

# Bibliography: symlinks created (references.bib -> referencias.bib,
# chicago-note-bibliography.csl -> ieee.csl) so pandoc finds them here.
# pandoc 2.9.x uses the pandoc-citeproc filter (--citeproc is 2.11+).

# Combine chapters in order, ensuring a blank line between files so
# pandoc parses every ATX heading (a heading glued to the previous line
# is not recognized, which breaks --number-sections chapter numbering).
: > electrotecnia-combined.md
for f in 00-portada.md 01-fundamentos.md 02-corriente-directa.md \
         03-corriente-alterna.md 04-maquinas.md 05-instalaciones.md \
         06-ejercicios.md 07-apendice.md; do
  cat "$f" >> electrotecnia-combined.md
  printf '\n' >> electrotecnia-combined.md
done

# Build PDF (portrait A4, TOC, numbering, IEEE citations via CSL)
pandoc electrotecnia-combined.md \
  -o electrotecnia.pdf \
  --pdf-engine=xelatex \
  --toc \
  --toc-depth=3 \
  --number-sections \
  --filter=pandoc-citeproc \
  --bibliography=references.bib \
  --csl=chicago-note-bibliography.csl \
  -V mainfont="DejaVu Sans" \
  -V monofont="DejaVu Sans Mono" \
  -V geometry:a4paper \
  -V geometry:margin=1in \
  -V toc-title="Table of Contents" \
  -H "$LATEX_PREAMBLE"

# Cleanup
rm electrotecnia-combined.md

echo "PDF generated: electrotecnia.pdf"