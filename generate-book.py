#!/usr/bin/env python3
"""Genera Electrotecnia-Completa.pdf directamente de los .md"""
import re, os, subprocess, tempfile

DIR = os.path.dirname(os.path.abspath(__file__))
PREAMBLE = os.path.expanduser('~/.agents/skills/pandoc-pdf-generation/assets/table-spacing-template.tex')
FILES = ['00-fundamentos.md','01-corriente-directa.md','02-corriente-alterna.md',
         '03-ejercicios-resueltos.md','04-formulas-tablas.md','05-referencias.md']

def clean(text):
    # Fix | X | = ... patterns (math expressions that look like tables)
    # Convert to: **|X| = ...** (bold, no pipe at start)
    text = re.sub(r'^(\s*)\|\s*([A-Za-z_]\w*)\s*\|(.+)$', r'\1**|\2|**\3', text, flags=re.MULTILINE)
    
    # Greek → ascii
    for g,l in {'α':'alpha','β':'beta','γ':'gamma','δ':'delta','ε':'epsilon','ζ':'zeta',
                'η':'eta','θ':'theta','ι':'iota','κ':'kappa','λ':'lambda','μ':'mu',
                'ν':'nu','ξ':'xi','π':'pi','ρ':'rho','σ':'sigma','τ':'tau','φ':'phi',
                'χ':'chi','ψ':'psi','ω':'omega','Ω':'Omega','Σ':'Sigma','Δ':'Delta'}.items():
        text = text.replace(g,l)
    # Symbols → ascii
    for s,l in {'×':'x','÷':'/','±':'+/-','∞':'inf','≈':'~','≠':'!=',
                '≤':'<=','≥':'>=','→':'->','←':'<-','↑':'^','↓':'v',
                '∥':'||','∠':'angle','°':' deg'}.items():
        text = text.replace(s,l)
    # √ → sqrt
    text = re.sub(r'√\(([^)]+)\)', r'sqrt(\1)', text)
    text = re.sub(r'√(\d+)', r'sqrt(\1)', text)
    # Unicode superscripts/subscripts
    sup = dict(zip('⁰¹²³⁴⁵⁶⁷⁸⁹⁻','0123456789-'))
    text = re.sub(r'([⁰¹²³⁴⁵⁶⁷⁸⁹⁻]+)', lambda m:'^{'+''.join(sup.get(c,c) for c in m.group(1))+'}', text)
    sub = dict(zip('₀₁₂₃₄₅₆₇₈₉','0123456789'))
    text = re.sub(r'([₀₁₂₃₄₅₆₇₈₉]+)', lambda m:'_{_'+''.join(sub.get(c,c) for c in m.group(1))+'}', text)
    # Strip emojis
    text = re.sub(r'[\U0001F300-\U0001F9FF\u2600-\u27BF\uFE00-\uFE0F]','',text)
    # Fix en/em dash
    text = text.replace('\u2013','--').replace('\u2014','---')
    return text

# Combine + clean
parts = []
for f in FILES:
    p = os.path.join(DIR,f)
    if os.path.exists(p):
        parts.append(clean(open(p).read()))
        parts.append('\n\n\\newpage\n\n')
combined = '\n\n'.join(parts)

# Write to temp, generate PDF, delete temp
tmp = tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False)
tmp.write(combined); tmp.close()

out = os.path.join(DIR,'pdfs','Electrotecnia-Completa.pdf')
os.makedirs(os.path.dirname(out), exist_ok=True)

r = subprocess.run([
    'pandoc', tmp.name, '-o', out,
    '--pdf-engine=xelatex', '--toc', '--toc-depth=2', '--number-sections',
    '-V','mainfont=DejaVu Sans','-V','monofont=DejaVu Sans Mono',
    '-V','mathfont=TeX Gyre DejaVu Math','-V','geometry:a4paper',
    '-V','geometry:margin=2.5cm','-V','fontsize=11pt',
    '-V','colorlinks=true','-V','linkcolor=NavyBlue','-V','urlcolor=NavyBlue',
    '-V','toc-title=Tabla de Contenidos','-H',PREAMBLE,
], capture_output=True, text=True, timeout=600)

os.unlink(tmp.name)

if r.returncode != 0:
    # Show last errors
    err = r.stderr
    lines = err.split('\n')
    print("ERROR Ultimas 15 lineas:")
    for ln in lines[-15:]:
        print(ln)
    exit(1)

# Count warnings
warn = r.stderr.count('Missing character')
sz = os.path.getsize(out)
print(f"PDF: {out} ({sz//1024} KB) | warnings: {warn}")
