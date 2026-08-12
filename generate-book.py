#!/usr/bin/env python3
"""
Generador de PDF profesional - Electrotecnia Industrial
Usa la skill pandoc-pdf-generation con preamble profesional.
"""

import re
import os
import subprocess
import sys

BASE_DIR = '/home/johnaltamirano2408/electrotecnia-completa'
SKILL_DIR = '/home/johnaltamirano2408/.agents/skills/pandoc-pdf-generation/assets'
PREAMBLE = os.path.join(SKILL_DIR, 'table-spacing-template.tex')

# ══════════════════════════════════════════════════════════════
# UNICODE CLEANUP FOR LATEX
# ══════════════════════════════════════════════════════════════

def clean_for_latex(text):
    """Strip emojis and fix Unicode for LaTeX XeLaTeX."""
    
    # Greek letters → plain text (avoid broken LaTeX fragments)
    # Use plain text when mixed with non-math content
    greek_map = {
        'α': 'alpha', 'β': 'beta', 'γ': 'gamma', 'δ': 'delta',
        'ε': 'epsilon', 'ζ': 'zeta', 'η': 'eta', 'θ': 'theta',
        'ι': 'iota', 'κ': 'kappa', 'λ': 'lambda', 'μ': 'mu',
        'ν': 'nu', 'ξ': 'xi', 'π': 'pi', 'ρ': 'rho',
        'σ': 'sigma', 'τ': 'tau', 'φ': 'phi', 'χ': 'chi',
        'ψ': 'psi', 'ω': 'omega',
        'Ω': 'Omega', 'Σ': 'Sigma', 'Φ': 'Phi', 'Δ': 'Delta',
        'Π': 'Pi', 'Ψ': 'Psi',
    }
    for g, l in greek_map.items():
        text = text.replace(g, l)
    
    # Math symbols → plain text (avoid broken LaTeX fragments)
    math_map = {
        '×': 'x', '÷': '/', '±': '+/-',
        '√': 'sqrt', '∞': 'inf', '≈': '~',
        '≠': '!=', '≤': '<=', '≥': '>=',
        '∠': 'angle', '∥': '||', '∘': 'o',
        '✓': '[OK]', '●': '*',
        '→': '->', '←': '<-', '↔': '<->',
        '↑': 'up', '↓': 'down',
    }
    for s, l in math_map.items():
        text = text.replace(s, l)
    
    # Superscript Unicode → LaTeX
    sup_map = {'⁰': '0', '¹': '1', '²': '2', '³': '3', '⁴': '4',
               '⁵': '5', '⁶': '6', '⁷': '7', '⁸': '8', '⁹': '9', '⁻': '-'}
    def fix_superscripts(m):
        parts = []
        for c in m.group(1):
            parts.append(sup_map.get(c, c))
        return '^{' + ''.join(parts) + '}'
    text = re.sub(r'([⁰¹²³⁴⁵⁶⁷⁸⁹⁻]+)', fix_superscripts, text)
    
    # Subscript Unicode → LaTeX
    sub_map = {'₀': '0', '₁': '1', '₂': '2', '₃': '3', '₄': '4',
               '₅': '5', '₆': '6', '₇': '7', '₈': '8', '₉': '9'}
    def fix_subscripts(m):
        parts = []
        for c in m.group(1):
            parts.append(sub_map.get(c, c))
        return '_{' + ''.join(parts) + '}'
    text = re.sub(r'([₀₁₂₃₄₅₆₇₈₉]+)', fix_subscripts, text)
    
    # Strip remaining emojis (broad range)
    text = re.sub(r'[\U0001F300-\U0001F9FF]', '', text)
    text = re.sub(r'[\u2600-\u27BF]', '', text)
    text = re.sub(r'[\uFE00-\uFE0F]', '', text)
    
    # Fix broken math: / sqrt{2} → sqrt(2)
    text = re.sub(r'/\s*sqrt\{(\d+)\}', r' sqrt(\1)', text)
    
    # Fix common LaTeX issues
    text = text.replace('\u2013', '--')   # en-dash
    text = text.replace('\u2014', '---')  # em-dash
    text = text.replace('\u201c', '"')
    text = text.replace('\u201d', '"')
    text = text.replace('\u2018', "'")
    text = text.replace('\u2019', "'")
    text = text.replace('\u00B0', '$^{\\circ}$')  # degree
    
    return text


def combine_markdown():
    """Read all markdown files, clean them, and combine."""
    files = [
        '00-fundamentos.md',
        '01-corriente-directa.md', 
        '02-corriente-alterna.md',
        '03-ejercicios-resueltos.md',
        '04-formulas-tablas.md',
        '05-referencias.md',
    ]
    
    parts = []
    for fname in files:
        fpath = os.path.join(BASE_DIR, fname)
        if os.path.exists(fpath):
            with open(fpath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            content = clean_for_latex(content)
            
            # Convert top-level headers to chapter format for book structure
            if fname.startswith('00'):
                content = content.replace('# 00', '#')
            elif fname.startswith('01'):
                content = content.replace('# 01', '#')
            elif fname.startswith('02'):
                content = content.replace('# 02', '#')
            elif fname.startswith('03'):
                content = content.replace('# 03', '#')
            elif fname.startswith('04'):
                content = content.replace('# 04', '#')
            elif fname.startswith('05'):
                content = content.replace('# 05', '#')
            
            parts.append(content)
            parts.append('\n\n\\newpage\n\n')
    
    return '\n\n'.join(parts)


def generate_pdf():
    """Generate PDF using the skill's build approach."""
    
    print("1. Combinando archivos markdown...")
    combined = combine_markdown()
    
    combined_path = os.path.join(BASE_DIR, 'pdfs', 'combined.md')
    with open(combined_path, 'w', encoding='utf-8') as f:
        f.write(combined)
    print(f"   {len(combined)} chars combinados")
    
    print("2. Generando PDF con preamble profesional...")
    output = os.path.join(BASE_DIR, 'pdfs', 'Electrotecnia-Completa.pdf')
    
    cmd = [
        'pandoc', combined_path,
        '-o', output,
        '--pdf-engine=xelatex',
        '--toc',
        '--toc-depth=2',
        '--number-sections',
        '-V', 'mainfont=DejaVu Sans',
        '-V', 'monofont=DejaVu Sans Mono',
        '-V', 'mathfont=TeX Gyre DejaVu Math',
        '-V', 'geometry:a4paper',
        '-V', 'geometry:margin=2.5cm',
        '-V', 'fontsize=11pt',
        '-V', 'colorlinks=true',
        '-V', 'linkcolor=NavyBlue',
        '-V', 'urlcolor=NavyBlue',
        '-V', 'toc-title=Tabla de Contenidos',
        '-H', PREAMBLE,
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=600)
    
    if result.returncode != 0:
        print("   ERROR:")
        print(result.stderr[:3000])
        return None
    
    warnings = result.stderr.count('Missing character')
    if warnings > 0:
        print(f"   {warnings} caracteres faltantes (cosméticos)")
    else:
        print("   0 caracteres faltantes")
    
    if os.path.exists(output):
        size = os.path.getsize(output)
        print(f"   PDF: {output} ({size/1024:.0f} KB)")
        return output
    
    return None


if __name__ == '__main__':
    pdf = generate_pdf()
    if pdf:
        print(f"\nListo: {pdf}")
