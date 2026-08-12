#!/usr/bin/env python3
"""Genera Electrotecnia-Completa.pdf usando build-pdf.sh de la skill pandoc-pdf-generation"""
import re, os, subprocess, tempfile

DIR = os.path.dirname(os.path.abspath(__file__))
BUILD_SH = os.path.expanduser('~/.agents/skills/pandoc-pdf-generation/assets/build-pdf.sh')
FILES = ['00-fundamentos.md','01-corriente-directa.md','02-corriente-alterna.md',
         '03-ejercicios-resueltos.md','04-formulas-tablas.md','05-referencias.md']

def clean(text):
    # Fix | X | = ... (math that looks like tables)
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
    # Superscripts/subscripts
    sup = dict(zip('⁰¹²³⁴⁵⁶⁷⁸⁹⁻','0123456789-'))
    text = re.sub(r'([⁰¹²³⁴⁵⁶⁷⁸⁹⁻]+)', lambda m:'^{'+''.join(sup.get(c,c) for c in m.group(1))+'}', text)
    sub = dict(zip('₀₁₂₃₄₅₆₇₈₉','0123456789'))
    text = re.sub(r'([₀₁₂₃₄₅₆₇₈₉]+)', lambda m:'_{_'+''.join(sub.get(c,c) for c in m.group(1))+'}', text)
    # Strip emojis
    text = re.sub(r'[\U0001F300-\U0001F9FF\u2600-\u27BF\uFE00-\uFE0F]','',text)
    text = text.replace('\u2013','--').replace('\u2014','---')
    return text

# Combine + clean into temp file
parts = []
for f in FILES:
    p = os.path.join(DIR,f)
    if os.path.exists(p):
        parts.append(clean(open(p).read()))
        parts.append('\n\n\\newpage\n\n')
combined = '\n\n'.join(parts)

tmp = tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False, dir='/tmp')
tmp.write(combined); tmp.close()

out = os.path.join(DIR,'pdfs','Electrotecnia-Completa.pdf')
os.makedirs(os.path.dirname(out), exist_ok=True)

# Use the skill's build-pdf.sh (portrait, since it's a textbook)
r = subprocess.run(
    ['bash', BUILD_SH, '--portrait', tmp.name, out],
    capture_output=True, text=True, timeout=600
)

os.unlink(tmp.name)

print(r.stdout)
if r.returncode != 0:
    print("STDERR:", r.stderr[-2000:])
    exit(1)

if os.path.exists(out):
    sz = os.path.getsize(out)
    print(f"PDF listo: {out} ({sz//1024} KB)")
