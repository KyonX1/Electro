# Electrotecnia Industrial PDF Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Generate a professional textbook-quality PDF (Boylestad/Alexander-Sadiku style) covering all electrotecnia industrial topics from DC through AC machines and installations, with proper LaTeX formatting, cross-references, bibliography, and diagrams.

**Architecture:** Modular markdown chapters (00-07) combined at build time, processed by pandoc + XeLaTeX with custom book-class template. Uses skill `pandoc-pdf-generation` assets (`build-pdf.sh`, `table-spacing-template.tex`) for production-proven formatting. Bibliography via `biblatex`+`biber` with IEEE CSL style. Diagrams generated via `graph-easy` skill.

**Tech Stack:**
- pandoc 2.9+, XeLaTeX (TeX Live/MacTeX)
- LaTeX: `book` class, `fontspec`, `unicode-math`, `fancyhdr`, `booktabs`, `tocloft`, `biblatex`+`biber`
- Fonts: DejaVu Sans, DejaVu Sans Mono, TeX Gyre DejaVu Math
- Skills: `pandoc-pdf-generation`, `graph-easy`, `dispatching-parallel-agents`

## Global Constraints

- **NO manual section numbering** in markdown — use `--number-sections`
- **NO emojis** in headings or body text
- **ALL tables** must have header + alignment row (`| --- |`) + data rows
- **ALL code blocks** must specify language (` ```python`, ` ```bash`)
- **ALL diagrams** via `graph-easy` skill — no manual ASCII art
- **Bibliography** in `referencias.bib` + `ieee.csl` style
- **Output:** portrait A4, 11pt, symmetric margins (inner=outer=2.5cm)
- **Verification:** 0 missing characters, TOC correct, cross-refs resolve, PDF valid

---

### Task 1: Initialize Git Repo & Scaffold Structure

**Files:**
- Create: `/home/johnaltamirano2408/electrotecnia/.git/`
- Create: `/home/johnaltamirano2408/electrotecnia/00-portada.md`
- Create: `/home/johnaltamirano2408/electrotecnia/01-fundamentos.md`
- Create: `/home/johnaltamirano2408/electrotecnia/02-corriente-directa.md`
- Create: `/home/johnaltamirano2408/electrotecnia/03-corriente-alterna.md`
- Create: `/home/johnaltamirano2408/electrotecnia/04-maquinas.md`
- Create: `/home/johnaltamirano2408/electrotecnia/05-instalaciones.md`
- Create: `/home/johnaltamirano2408/electrotecnia/06-ejercicios.md`
- Create: `/home/johnaltamirano2408/electrotecnia/07-apendice.md`
- Create: `/home/johnaltamirano2408/electrotecnia/referencias.bib`
- Create: `/home/johnaltamirano2408/electrotecnia/ieee.csl`
- Create: `/home/johnaltamirano2408/electrotecnia/build.sh`
- Create: `/home/johnaltamirano2408/electrotecnia/template.tex`
- Create: `/home/johnaltamirano2408/electrotecnia/validate_md.py`
- Create: `/home/johnaltamirano2408/electrotecnia/verify_pdf.py`

**Interfaces:**
- Produces: empty scaffold files ready for content

- [ ] **Step 1: Init git repo**
```bash
cd /home/johnaltamirano2408/electrotecnia
git init
git config user.name "KyonX1"
git config user.email "kyonx1@users.noreply.github.com"
```

- [ ] **Step 2: Create chapter files with front matter**
```bash
# 00-portada.md
cat > 00-portada.md << 'EOF'
---
title: "Electrotecnia Industrial"
subtitle: "Desde fundamentos hasta máquinas e instalaciones"
author: "KyonX1"
date: "2026"
lang: es
---

# Electrotecnia Industrial

**Desde fundamentos hasta máquinas e instalaciones**

---

*Texto de referencia para nivel intermedio-avanzado (C/D)*

![CC BY-SA 4.0](https://licensebuttons.net/l/by-sa/4.0/88x31.png)
EOF

# Create empty chapter files
for f in 01-fundamentos 02-corriente-directa 03-corriente-alterna 04-maquinas 05-instalaciones 06-ejercicios 07-apendice; do
  echo "# ${f#*-}" > "${f}.md"
done
```

- [ ] **Step 3: Create minimal referencias.bib**
```bibtex
@book{boylestad2023,
  title = {Introductory Circuit Analysis},
  author = {Boylestad, Robert L.},
  edition = {14},
  year = {2023},
  publisher = {Pearson}
}

@book{alexander2021,
  title = {Fundamentals of Electric Circuits},
  author = {Alexander, Charles K. and Sadiku, Matthew N. O.},
  edition = {7},
  year = {2021},
  publisher = {McGraw-Hill}
}

@book{chapman2012,
  title = {Electric Machinery Fundamentals},
  author = {Chapman, Stephen J.},
  edition = {5},
  year = {2012},
  publisher = {McGraw-Hill}
}

@standard{iec60364,
  title = {Low-voltage electrical installations},
  author = {{IEC}},
  number = {60364},
  year = {2017},
  organization = {International Electrotechnical Commission}
}

@standard{retie,
  title = {Reglamento Técnico de Instalaciones Eléctricas (RETIE)},
  author = {{Gobierno de Colombia}},
  year = {2024}
}
```

- [ ] **Step 4: Create ieee.csl** (download standard IEEE style)
```bash
curl -sL "https://raw.githubusercontent.com/citation-style-language/styles/master/ieee.csl" -o ieee.csl
```

- [ ] **Step 5: Create build.sh using skill's build-pdf.sh**
```bash
cat > build.sh << 'EOF'
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
EOF
chmod +x build.sh
```

- [ ] **Step 6: Create template.tex (book class + skill preamble)**
```latex
% template.tex — LaTeX book class template for electrotecnia
\documentclass[11pt,a4paper,twoside,openright]{book}

% Fonts (XeLaTeX)
\usepackage{fontspec}
\usepackage{unicode-math}
\setmainfont{DejaVu Sans}
\setsansfont{DejaVu Sans}
\setmonofont{DejaVu Sans Mono}
\setmathfont{TeX Gyre DejaVu Math}

% Geometry: symmetric margins for book binding
\usepackage[inner=2.5cm,outer=2.5cm,top=2.5cm,bottom=2.5cm,includeheadfoot]{geometry}

% Headers/footers
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[LE,RO]{\thepage}
\fancyhead[LO]{\leftmark}
\fancyhead[RE]{\rightmark}
\renewcommand{\headrulewidth}{0.4pt}
\renewcommand{\footrulewidth}{0pt}

% Bibliography
\usepackage[backend=biber,style=ieee,sorting=nty]{biblatex}
\addbibresource{referencias.bib}

% Cross-references
\usepackage{hyperref}
\hypersetup{
    colorlinks=true,
    linkcolor=NavyBlue,
    citecolor=NavyBlue,
    urlcolor=NavyBlue
}

% Include skill's production preamble (booktabs, tocloft, fancyvrb, raggedright)
\input{table-spacing-template.tex}

% Custom commands for electrotecnia
\newcommand{\ohm}{\,\Omega}
\newcommand{\uV}{\,\mu V}
\newcommand{\uA}{\,\mu A}
\newcommand{\mA}{\,mA}
\newcommand{\kV}{\,kV}
\newcommand{\kA}{\,kA}

\begin{document}

% Title page
\frontmatter
\thispagestyle{empty}
\begin{center}
\vspace*{3cm}
{\Huge \bfseries Electrotecnia Industrial}\\[1cm]
{\Large Desde fundamentos hasta máquinas e instalaciones}\\[2cm]
{\large KyonX1}\\[0.5cm]
{\large 2026}
\vfill
{\small CC BY-SA 4.0}
\end{center}
\clearpage

% Table of contents
\tableofcontents
\clearpage

% List of figures/tables
\listoffigures
\listoftables
\clearpage

% Main matter
\mainmatter

% Chapters included via pandoc --include-in-header or markdown \input
% Pandoc will insert chapter content here

% Bibliography
\backmatter
\printbibliography[heading=bibintoc]

\end{document}
```

- [ ] **Step 7: Create validate_md.py**
```python
#!/usr/bin/env python3
"""Validate markdown before PDF build."""
import re, sys, os

def check_file(fpath):
    errors = []
    with open(fpath) as f:
        lines = f.readlines()
    
    in_code = False
    for i, line in enumerate(lines, 1):
        stripped = line.strip()
        
        # Track code blocks
        if stripped.startswith('```'):
            in_code = not in_code
            continue
        
        # No manual numbering in headings
        if stripped.startswith('#') and re.match(r'^#+\s+\d+\.', stripped):
            errors.append(f"{fpath}:{i}: Manual numbering in heading: {stripped[:50]}")
        
        # No emojis
        if re.search(r'[\U0001F300-\U0001F9FF\u2600-\u27BF]', stripped):
            errors.append(f"{fpath}:{i}: Emoji found: {stripped[:50]}")
        
        # Tables must have alignment row
        if stripped.startswith('|') and not in_code:
            if '---' not in stripped:
                # Check if previous or next line is alignment
                prev = lines[i-2].strip() if i > 1 else ''
                nxt = lines[i].strip() if i < len(lines) else ''
                if not ('---' in prev or '---' in nxt):
                    errors.append(f"{fpath}:{i}: Table row without alignment: {stripped[:60]}")
        
        # Code blocks must have language
        if stripped.startswith('```') and not stripped[3:].strip() and not in_code:
            errors.append(f"{fpath}:{i}: Code block without language tag")
    
    return errors

if __name__ == '__main__':
    all_errors = []
    for f in ['00-portada.md','01-fundamentos.md','02-corriente-directa.md',
              '03-corriente-alterna.md','04-maquinas.md','05-instalaciones.md',
              '06-ejercicios.md','07-apendice.md']:
        if os.path.exists(f):
            all_errors.extend(check_file(f))
    
    if all_errors:
        print("VALIDATION FAILED:")
        for e in all_errors:
            print(f"  {e}")
        sys.exit(1)
    else:
        print("All markdown files valid!")
```

- [ ] **Step 8: Create verify_pdf.py**
```python
#!/usr/bin/env python3
"""Verify generated PDF quality."""
import subprocess, sys, os

def verify(pdf_path):
    errors = []
    warnings = []
    
    # Check file exists and is valid PDF
    if not os.path.exists(pdf_path):
        return ["PDF not found"], []
    
    with open(pdf_path, 'rb') as f:
        if f.read(5) != b'%PDF-':
            return ["Not a valid PDF"], []
    
    # Get page count
    try:
        result = subprocess.run(['pdfinfo', pdf_path], capture_output=True, text=True)
        pages = None
        for line in result.stdout.split('\n'):
            if line.startswith('Pages:'):
                pages = int(line.split(':')[1].strip())
                break
        if pages is None:
            warnings.append("Could not determine page count")
        elif pages < 20:
            warnings.append(f"Only {pages} pages - may be incomplete")
    except:
        warnings.append("pdfinfo not available")
    
    # Check for missing characters in build log (not available here)
    # This would be checked during build
    
    return errors, warnings

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: verify_pdf.py <pdf_path>")
        sys.exit(1)
    
    errors, warnings = verify(sys.argv[1])
    
    if errors:
        print("ERRORS:")
        for e in errors:
            print(f"  {e}")
    
    if warnings:
        print("WARNINGS:")
        for w in warnings:
            print(f"  {w}")
    
    if not errors and not warnings:
        print("PDF verification PASSED")
    
    sys.exit(1 if errors else 0)
```

- [ ] **Step 9: Commit scaffold**
```bash
git add .
git commit -m "chore: scaffold electrotecnia repo with chapters, build, validation"
```

---

### Task 2: Write Chapter 01 — Fundamentos

**Files:**
- Modify: `01-fundamentos.md` (full content)

**Interfaces:**
- Consumes: scaffold from Task 1
- Produces: Complete chapter with proper markdown structure

- [ ] **Step 1: Write 01-fundamentos.md with full content**
```markdown
# Fundamentos de Electrotecnia

## 1. Carga Eléctrica y Ley de Coulomb

La carga eléctrica es una propiedad intrínseca de la materia...

### Ley de Coulomb

$$F = k \frac{|q_1 q_2|}{r^2}$$

| **Variable** | **Significado** | **Unidad** |
| :------------: | :---------------: | :----------: |
| $F$ | Fuerza entre cargas | N |
| $k$ | Constante de Coulomb | $8.99 \times 10^9$ N·m²/C² |
| $q_1, q_2$ | Magnitud de cada carga | C |
| $r$ | Distancia entre cargas | m |

```python
# Ejemplo: Fuerza entre +3 μC y -5 μC a 0.2 m
k = 8.99e9
q1 = 3e-6
q2 = -5e-6
r = 0.2
F = k * abs(q1) * abs(q2) / r**2
print(f"F = {F:.2f} N")
```

> **Nota:** $k = 1/(4\pi\varepsilon_0)$, $\varepsilon_0 = 8.854 \times 10^{-12}$ F/m

---

## 2. Campo Eléctrico

...

## 3. Potencial Eléctrico y Voltaje

...

## 4. Energía y Potencia Eléctrica

...

## 5. Resistividad y Resistencia

| **Material** | **$\rho$ ($\Omega\cdot$m)** |
| :------------: | :--------------------------: |
| Cobre | $1.68 \times 10^{-8}$ |
| Aluminio | $2.82 \times 10^{-8}$ |
| Acero | $1.0 \times 10^{-7}$ |

...

## 6. Ley de Ohm y Potencia en DC

$$V = IR \qquad P = VI = I^2R = \frac{V^2}{R}$$

...

---

*Referencias: [@boylestad2023, cap. 1-3]; [@alexander2021, cap. 1-2]*
```

- [ ] **Step 2: Validate**
```bash
python3 validate_md.py
```

- [ ] **Step 3: Commit**
```bash
git add 01-fundamentos.md
git commit -m "feat(chapter): add 01-fundamentos complete"
```

---

### Task 3: Write Chapter 02 — Corriente Directa

**Files:**
- Modify: `02-corriente-directa.md`

- [ ] **Step 1: Write complete chapter with these sections:**
  - 2.1 Circuitos en serie y paralelo
  - 2.2 Leyes de Kirchhoff (KCL, KVL)
  - 2.3 Teoremas de circuitos (Thévenin, Norton, Superposición, Máxima transferencia)
  - 2.4 Divisores de voltaje y corriente
  - 2.5 Análisis de mallas y nodos
  - 2.6 Condensadores en DC (carga/descarga, $\tau = RC$)
  - 2.7 Inductores en DC (transitorios, $\tau = L/R$)
  - 2.8 Energía almacenada ($W_C = ½CV^2$, $W_L = ½LI^2$)
  - 2.9 Instrumentación (multímetro, osciloscopio)

- [ ] **Step 2: Include tables with alignment rows, code blocks with `python`, citations `[@boylestad2023]`**

- [ ] **Step 3: Validate + Commit**

---

### Task 4: Write Chapter 03 — Corriente Alterna

**Files:**
- Modify: `03-corriente-alterna.md`

- [ ] **Step 1: Write complete chapter with these sections:**
  - 3.1 Forma de onda sinusoidal ($v(t) = V_m \sin(\omega t + \phi)$)
  - 3.2 Valores: pico, pico-pico, RMS, promedio
  - 3.3 Fasores y números complejos ($Z = R + jX$)
  - 3.4 Impedancia: R, L, C ($X_L = \omega L$, $X_C = 1/\omega C$)
  - 3.5 Circuitos serie RLC, paralelo RLC
  - 3.6 Potencia en AC: activa (P), reactiva (Q), aparente (S), factor de potencia
  - 3.7 Resonancia serie y paralelo ($f_r = 1/2\pi\sqrt{LC}$)
  - 3.8 Sistemas trifásicos (estrella, delta, potencias)
  - 3.9 Filtros (pasabajo, pasaalto, pasabanda, rechazabanda)
  - 3.10 Análisis de Fourier básico

- [ ] **Step 2: All tables, code blocks, diagrams via `graph-easy` skill**

- [ ] **Step 3: Validate + Commit**

---

### Task 5: Write Chapter 04 — Máquinas Eléctricas

**Files:**
- Modify: `04-maquinas.md`

- [ ] **Step 1: Write complete chapter:**
  - 4.1 Principios electromagnéticos (ley de Faraday, Lenz)
  - 4.2 Transformadores (ideal, real, autotransformador, ensayos)
  - 4.3 Máquinas de CC (generador, motor, tipos de excitación)
  - 4.4 Máquinas de CA síncronas (generador, motor, curva V)
  - 4.5 Máquinas de inducción (principio, equivalentes, arranque, velocidad)
  - 4.6 Motores especiales (paso a paso, brushless, lineales)

- [ ] **Step 2: Include transformer equivalent circuit diagram via `graph-easy`**

- [ ] **Step 3: Validate + Commit**

---

### Task 6: Write Chapter 05 — Instalaciones Eléctricas

**Files:**
- Modify: `05-instalaciones.md`

- [ ] **Step 1: Write complete chapter:**
  - 5.1 Normativa (IEC 60364, RETIE, NEC, UNE)
  - 5.2 Sistemas de puesta a tierra (TT, TN, IT)
  - 5.3 Protecciones (magnetotérmico, diferencial, sobretensión)
  - 5.4 Cálculo de secciones de conductor (caída de tensión, calentamiento)
  - 5.5 Alumbrado y fuerza (circuitos, mandos, cuadros)
  - 5.6 Instalaciones especiales (baños, piscinas, médicos, peligrosas)
  - 5.7 Verificación y ensayos (continuidad, aislamiento, bucle, RCD)

- [ ] **Step 2: Tables for secciones, protecciones, caídas de tensión**

- [ ] **Step 3: Validate + Commit**

---

### Task 7: Write Chapter 06 — Ejercicios Resueltos y Propuestos

**Files:**
- Modify: `06-ejercicios.md`

- [ ] **Step 1: 30+ ejercicios resueltos paso a paso** cubriendo todos los capítulos
- [ ] **Step 2: 15+ ejercicios propuestos con respuestas numéricas al final**
- [ ] **Step 3: Organizar por tema: DC, AC, trifásica, máquinas, instalaciones**
- [ ] **Step 4: Validate + Commit**

---

### Task 8: Write Chapter 07 — Apéndice (Tablas, Constantes, Fórmulas)

**Files:**
- Modify: `07-apendice.md`

- [ ] **Step 1: Tablas maestras:**
  - Resistividad de materiales
  - Secciones de cable y capacidad de corriente (IEC 60364)
  - Código de colores resistores/condensadores
  - Símbolos normalizados (IEC 60617)
  - Prefijos SI
  - Constantes físicas ($\varepsilon_0$, $\mu_0$, $e$, $k$, $g$)

- [ ] **Step 2: Fórmulas maestras por tema (una tabla por capítulo)**
- [ ] **Step 3: Validate + Commit**

---

### Task 9: Generate Diagrams with graph-easy Skill

**Files:**
- Create: `diagrams/` directory with `.txt` source files
- Modify: chapters to include rendered diagrams

- [ ] **Step 1: Invoke skill for each diagram needed:**
  - Circuitos serie/paralelo (cap. 2)
  - Divisor de voltaje/corriente (cap. 2)
  - Fasor RLC serie (cap. 3)
  - Triángulo de potencias (cap. 3)
  - Conexiones estrella/delta (cap. 3)
  - Transformador equivalente (cap. 4)
  - Curvas característica motor CC (cap. 4)
  - Esquema puesta a tierra TT/TN/IT (cap. 5)

- [ ] **Step 2: Embed in markdown as code blocks with `graph-easy` source in `<details>` (hidden via `--hide-details`)**

- [ ] **Step 3: Commit diagrams + updated chapters**

---

### Task 10: Build & Verify PDF (Double Verification)

**Files:**
- Run: `build.sh`
- Verify: `verify_pdf.py`

- [ ] **Step 1: Run validation**
```bash
python3 validate_md.py
```

- [ ] **Step 2: Build PDF**
```bash
./build.sh
```

- [ ] **Step 3: Verify PDF**
```bash
python3 verify_pdf.py electrotecnia.pdf
# Check: 0 missing chars, >50 pages, TOC correct, cross-refs work
```

- [ ] **Step 4: Manual visual inspection**
  - Open PDF, check: headers/footers, page numbers, chapter starts on right page, figures/tables numbered, bibliography formatted, no widows/orphans in tables

- [ ] **Step 5: If any issue → fix source → rebuild → reverify**

- [ ] **Step 6: Commit final PDF + sources**
```bash
git add electrotecnia.pdf
git commit -m "build: final electrotecnia.pdf textbook quality"
```

---

### Task 11: Push to GitHub

**Files:**
- Remote: `https://github.com/KyonX1/Electro.git`

- [ ] **Step 1: Add remote + push**
```bash
git remote add origin https://github.com/KyonX1/Electro.git
git push -u origin main
```

- [ ] **Step 2: Verify on GitHub** (PDF visible in repo)

---

## Execution Notes

- Use `subagent-driven-development` skill: dispatch one subagent per Task 2-8 (chapters) for parallel writing
- Tasks 9-10 are sequential (diagrams depend on chapters; build depends on all)
- Each chapter task is independent — no shared state
- Verify after EVERY task with `python3 validate_md.py`