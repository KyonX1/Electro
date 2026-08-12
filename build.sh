#!/usr/bin/env bash
set -euo pipefail

SKILL_DIR="$HOME/.agents/skills/pandoc-pdf-generation/assets"
BUILD_SH="$SKILL_DIR/build-pdf.sh"
PREAMBLE="$SKILL_DIR/table-spacing-template.tex"

# Combine chapters in order
cat 00-portada.md \
    01-fundamentos.md \
    02-corriente-directa.md \
    03-corriente-alterna.md \
    04-maquinas.md \
    05-instalaciones.md \
    06-ejercicios.md \
    07-apendice.md > electrotecnia-combined.md

# Run skill's build script (portrait, with bibliography)
bash "$BUILD_SH" --portrait \
    --bibliography=referencias.bib \
    --csl=ieee.csl \
    electrotecnia-combined.md electrotecnia.pdf

# Cleanup
rm electrotecnia-combined.md

echo "PDF generated: electrotecnia.pdf"
