#!/usr/bin/env python3
"""
Generador de PDF profesional - Electrotecnia Industrial
Combina todos los archivos .md en un solo PDF tipo libro de texto.
"""

import re
import os
import subprocess
import sys

BASE_DIR = '/home/johnaltamirano2408/electrotecnia-completa'

# ══════════════════════════════════════════════════════════════
# MAPEO DE EMOJIS → TEXTO LATEX
# ══════════════════════════════════════════════════════════════
EMOJI_MAP = {
    # Emojis de UI
    '⚡': '', '💡': '', '⚠️': '', '⚠': '', '📐': '',
    '🧮': '', '🔗': '', '✅': '', '📏': '', '📖': '',
    '📊': '', '🎯': '', '📚': '', '🛠️': '', '📱': '',
    '🏭': '', '🎓': '', '🔋': '', '🔌': '', '⚙️': '',
    '': '', '': '', '': '', '': '', '': '',
    '': '', '': '', '': '', '': '', '': '',
    '': '', '': '', '': '', '': '', '': '',
    '': '', '': '', '': '', '': '', '': '',
    # Block chars
    '┌': '', '┐': '', '└': '', '┘': '', '├': '',
    '┤': '', '┬': '', '┴': '', '┼': '', '│': '',
    '─': '', '═': '', '║': '',
    # Arrows
    '→': '$\\to$', '←': '$\\leftarrow$', '↔': '$\\leftrightarrow$',
    '↑': '$\\uparrow$', '↓': '$\\downarrow$',
    # Math symbols
    '×': '$\\times$', '÷': '$\\div$', '±': '$\\pm$',
    '√': '$\\sqrt{}$', '²': '$^{2}$', '³': '$^{3}$',
    '⁴': '$^{4}$', '⁸': '$^{8}$',
    '∞': '$\\infty$', '≈': '$\\approx$', '≠': '$\\neq$',
    '≤': '$\\leq$', '≥': '$\\geq$', '∠': '$\\angle$',
    '°': '$^{\\circ}$',
    # Greek (common)
    'α': '$\\alpha$', 'β': '$\\beta$', 'γ': '$\\gamma$',
    'δ': '$\\delta$', 'ε': '$\\epsilon$', 'ζ': '$\\zeta$',
    'η': '$\\eta$', 'θ': '$\\theta$', 'ι': '$\\iota$',
    'κ': '$\\kappa$', 'λ': '$\\lambda$', 'μ': '$\\mu$',
    'ν': '$\\nu$', 'ξ': '$\\xi$', 'π': '$\\pi$',
    'ρ': '$\\rho$', 'σ': '$\\sigma$', 'τ': '$\\tau$',
    'φ': '$\\phi$', 'χ': '$\\chi$', 'ψ': '$\\psi$',
    'ω': '$\\omega$',
    'Ω': '$\\Omega$', 'Σ': '$\\Sigma$', 'Φ': '$\\Phi$',
    'Δ': '$\\Delta$',
    # Units
    'Ω': '$\\Omega$', 'μ': '$\\mu$', 'Ω': '$\\Omega$',
    # Misc
    '✓': '\\checkmark', '✗': '\\times', '●': '\\bullet',
    '○': '\\circ', '■': '\\blacksquare', '□': '\\square',
    '★': '\\star', '☆': '\\star',
}

# Unicode ranges to strip (emojis, symbols)
STRIP_RANGES = [
    (0x1F300, 0x1F9FF),  # Emojis
    (0x2600, 0x26FF),    # Misc symbols
    (0x2700, 0x27BF),    # Dingbats
    (0xFE00, 0xFE0F),    # Variation selectors
    (0x200D, 0x200D),    # Zero width joiner
    (0x20E3, 0x20E3),    # Combining enclosing keycap
]

def clean_for_latex(text):
    """Replace emojis and fix Unicode for LaTeX."""
    # Apply emoji map
    for emoji, replacement in EMOJI_MAP.items():
        text = text.replace(emoji, replacement)
    
    # Strip remaining emoji ranges
    for start, end in STRIP_RANGES:
        pattern = f'[\\U{start:08X}-\\U{end:08X}]'
        try:
            text = re.sub(pattern, '', text)
        except:
            pass
    
    # Fix common issues
    text = text.replace('–', '--')   # en-dash
    text = text.replace('—', '---')  # em-dash
    text = text.replace('\u201c', '"')
    text = text.replace('\u201d', '"')
    text = text.replace('\u2018', "'")
    text = text.replace('\u2019', "'")
    
    # Fix broken math expressions
    text = re.sub(r'\$\\sqrt\{\}\$(\d+)', r'$\\sqrt{\1}$', text)
    text = re.sub(r'\$\\sqrt\{\}\$ (\d+)', r'$\\sqrt{\1}$', text)
    
    # Fix patterns like / $Value$ -> just $Value$ (remove orphaned / before math)
    text = re.sub(r'/ \$\\', r' $\\', text)
    
    # Fix double dollar signs
    
    # Additional Unicode fixes
    text = text.replace('\u2220', '$\\angle$')      # ∠
    text = text.replace('\u2225', '$\\parallel$')   # ∥
    text = text.replace('\u221A', '$\\sqrt{}$')     # √
    text = text.replace('\u221E', '$\\infty$')      # ∞
    text = text.replace('\u25CB', '$\\circ$')       # ○
    text = text.replace('\u2713', '$\\checkmark$')  # ✓
    text = text.replace('\u2208', '$\\in$')         # ∈
    text = text.replace('\u00B0', '$^{\\circ}$')    # °
    text = text.replace('\u00B5', '$\\mu$')         # µ
    text = text.replace('\u03A9', '$\\Omega$')      # Ω (capital)
    text = text.replace('\u03C9', '$\\omega$')      # ω (lowercase)
    text = text.replace('\u03B1', '$\\alpha$')      # α
    text = text.replace('\u03B2', '$\\beta$')       # β
    text = text.replace('\u03B3', '$\\gamma$')      # γ
    text = text.replace('\u03B4', '$\\delta$')      # δ
    text = text.replace('\u03B5', '$\\epsilon$')    # ε
    text = text.replace('\u03B8', '$\\theta$')      # θ
    text = text.replace('\u03BB', '$\\lambda$')     # λ
    text = text.replace('\u03BC', '$\\mu$')         # μ
    text = text.replace('\u03C0', '$\\pi$')         # π
    text = text.replace('\u03C1', '$\\rho$')        # ρ
    text = text.replace('\u03C3', '$\\sigma$')      # σ
    text = text.replace('\u03C6', '$\\phi$')        # φ
    text = text.replace('\u0394', '$\\Delta$')      # Δ
    text = text.replace('\u03A3', '$\\Sigma$')      # Σ
    text = text.replace('\u03A6', '$\\Phi$')        # Φ
    
    # Subscript characters
    text = text.replace('\u1D62', 'i')              # ᵢ
    text = text.replace('\u2099', 'n')              # ₙ
    
    # Fix Cyrillic chars that leaked through
    text = text.replace('\u0430', 'a')  # а
    text = text.replace('\u043B', 'l')  # л
    text = text.replace('\u043D', 'n')  # н
    text = text.replace('$$$', '$')
    text = text.replace('$$$$', '$')
    
    # Fix broken math: V_max  $\sqrt{2}$ -> $V_{max} \sqrt{2}$
    text = re.sub(r'V_max\s+\$\\sqrt\{(\d+)\}\$', r'$V_{max} \\sqrt{\1}$', text)
    text = re.sub(r'V_rms\s+\$\\sqrt\{(\d+)\}\$', r'$V_{rms} \\sqrt{\1}$', text)
    
    # Fix / before math expressions
    text = re.sub(r'/\$\{(\w+)\}', r'/$\\{\\1$}', text)
    text = re.sub(r'/\$', ' $', text)
    
    # Fix subscript/superscript Unicode characters
    # Handle combined superscripts like ⁻⁹ → ^{-9}, ⁻¹⁹ → ^{-19}
    def fix_superscripts(text):
        # Match sequences of superscript chars
        sup_pattern = re.compile(r'([⁰¹²³⁴⁵⁶⁷⁸⁹⁻]+)')
        def replace_sup(match):
            seq = match.group(1)
            parts = []
            for c in seq:
                if c == '⁻':
                    parts.append('-')
                else:
                    parts.append(str('⁰¹²³⁴⁵⁶⁷⁸⁹'.index(c)))
            return '^{' + ''.join(parts) + '}'
        return sup_pattern.sub(replace_sup, text)
    
    def fix_subscripts(text):
        sub_pattern = re.compile(r'([₀₁₂₃₄₅₆₇₈₉]+)')
        def replace_sub(match):
            seq = match.group(1)
            parts = []
            for c in seq:
                parts.append(str('₀₁₂₃₄₅₆₇₈₉'.index(c)))
            return '_{' + ''.join(parts) + '}'
        return sub_pattern.sub(replace_sub, text)
    
    text = fix_superscripts(text)
    text = fix_subscripts(text)
    
    # Fix markdown headers that might break LaTeX
    
    return text

def markdown_to_latex_sections(text):
    """Convert markdown structure to LaTeX-friendly structure."""
    lines = text.split('\n')
    result = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        
        # Handle headers
        if stripped.startswith('######'):
            result.append(f'\\subsubsection*{{{stripped[6:].strip()}}}')
        elif stripped.startswith('#####'):
            result.append(f'\\subsubsection*{{{stripped[5:].strip()}}}')
        elif stripped.startswith('####'):
            result.append(f'\\subsection*{{{stripped[4:].strip()}}}')
        elif stripped.startswith('###'):
            result.append(f'\\subsection{{{stripped[3:].strip()}}}')
        elif stripped.startswith('##'):
            result.append(f'\\section{{{stripped[2:].strip()}}}')
        elif stripped.startswith('#'):
            result.append(f'\\chapter{{{stripped[1:].strip()}}}')
        
        # Handle blockquotes -> tcolorbox
        elif stripped.startswith('> **') and 'Tip' in stripped:
            # Collect all lines of this blockquote
            content_lines = []
            i += 1
            while i < len(lines) and lines[i].strip().startswith('>'):
                content_lines.append(lines[i].strip().lstrip('>').strip())
                i += 1
            content = ' '.join(content_lines)
            result.append(f'\\begin{{tipbox}}')
            result.append(content)
            result.append(f'\\end{{tipbox}}')
            continue  # Skip the i++ at end
        
        elif stripped.startswith('> **') and ('Advertencia' in stripped or 'Error' in stripped):
            content_lines = []
            i += 1
            while i < len(lines) and lines[i].strip().startswith('>'):
                content_lines.append(lines[i].strip().lstrip('>').strip())
                i += 1
            content = ' '.join(content_lines)
            result.append(f'\\begin{{warningbox}}')
            result.append(content)
            result.append(f'\\end{{warningbox}}')
            continue
        
        elif stripped.startswith('> **') and ('Fórmula' in stripped or 'formula' in stripped):
            content_lines = []
            i += 1
            while i < len(lines) and lines[i].strip().startswith('>'):
                content_lines.append(lines[i].strip().lstrip('>').strip())
                i += 1
            content = ' '.join(content_lines)
            result.append(f'\\begin{{formulabox}}')
            result.append(content)
            result.append(f'\\end{{formulabox}}')
            continue
        
        elif stripped.startswith('> **') and ('Verificación' in stripped or 'OK' in stripped):
            content_lines = []
            i += 1
            while i < len(lines) and lines[i].strip().startswith('>'):
                content_lines.append(lines[i].strip().lstrip('>').strip())
                i += 1
            content = ' '.join(content_lines)
            result.append(f'\\begin{{checkmarkbox}}')
            result.append(content)
            result.append(f'\\end{{checkmarkbox}}')
            continue
        
        elif stripped.startswith('> **') and ('Nota' in stripped or 'Dato' in stripped):
            content_lines = []
            i += 1
            while i < len(lines) and lines[i].strip().startswith('>'):
                content_lines.append(lines[i].strip().lstrip('>').strip())
                i += 1
            content = ' '.join(content_lines)
            result.append(f'\\begin{{tipbox}}')
            result.append(content)
            result.append(f'\\end{{tipbox}}')
            continue
        
        elif stripped.startswith('>'):
            # Generic blockquote
            content = stripped.lstrip('>').strip()
            result.append(f'\\begin{{tipbox}}')
            result.append(content)
            result.append(f'\\end{{tipbox}}')
        
        # Handle horizontal rules
        elif stripped == '---' or stripped == '***' or stripped == '___':
            result.append('\\vspace{0.5em}{\\color{chapterblue!30}\\rule{\\textwidth}{0.5pt}}\\vspace{0.5em}')
        
        # Handle tables
        elif '|' in stripped and stripped.startswith('|'):
            # Collect table lines
            table_lines = []
            while i < len(lines) and '|' in lines[i].strip():
                table_lines.append(lines[i].strip())
                i += 1
            i -= 1  # Back up one
            
            # Parse table
            if len(table_lines) >= 3:
                # Header
                header = [c.strip().strip('*') for c in table_lines[0].split('|') if c.strip()]
                # Skip separator
                # Data rows
                rows = []
                for tl in table_lines[2:]:
                    if '|' in tl and not tl.strip().startswith('|--'):
                        row = [c.strip() for c in tl.split('|') if c.strip() or c.strip() == '']
                        rows.append(row)
                
                if header:
                    ncols = len(header)
                    col_spec = '|'.join(['l'] * ncols)
                    result.append(f'\\begin{{longtable}}{{|{col_spec}|}}')
                    result.append('\\hline')
                    result.append(' & '.join([f'\\textbf{{{h}}}' for h in header]) + ' \\\\')
                    result.append('\\hline')
                    for row in rows:
                        # Pad row if needed
                        while len(row) < ncols:
                            row.append('')
                        result.append(' & '.join(row[:ncols]) + ' \\\\')
                        result.append('\\hline')
                    result.append('\\end{longtable}')
            continue
        
        # Handle code blocks
        elif stripped.startswith('```'):
            lang = stripped[3:].strip()
            code_lines = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith('```'):
                code_lines.append(lines[i])
                i += 1
            code = '\n'.join(code_lines)
            
            if lang == 'python' or 'print' in code:
                result.append('\\begin{lstlisting}[style=code]')
                result.append(code)
                result.append('\\end{lstlisting}')
            else:
                result.append('\\begin{Verbatim}[fontsize=\\small,frame=leftline,framesep=5pt,framerule=2pt,rulecolor=\\color{accentblue},bgcolor=\\color{codebg}]')
                result.append(code)
                result.append('\\end{Verbatim}')
        
        # Handle inline math ($...$) - pass through
        elif '$' in stripped:
            result.append(line)
        
        # Handle bold (**text**)
        elif stripped.startswith('**') and stripped.endswith('**'):
            result.append(f'\\textbf{{{stripped[2:-2]}}}')
        
        # Handle italic (*text*)
        elif stripped.startswith('*') and stripped.endswith('*') and not stripped.startswith('**'):
            result.append(f'\\textit{{{stripped[1:-1]}}}')
        
        # Handle list items
        elif re.match(r'^(\d+)\.\s', stripped):
            content = re.sub(r'^(\d+)\.\s', '', stripped)
            result.append(f'\\item {content}')
        elif stripped.startswith('- ') or stripped.startswith('* '):
            content = stripped[2:]
            result.append(f'\\item {content}')
        
        # Regular text
        else:
            result.append(line)
        
        i += 1
    
    return '\n'.join(result)

def combine_markdown_files():
    """Read all markdown files and combine them into one."""
    files_order = [
        '00-fundamentos.md',
        '01-corriente-directa.md',
        '02-corriente-alterna.md',
        '03-ejercicios-resueltos.md',
        '04-formulas-tablas.md',
        '05-referencias.md',
    ]
    
    combined = []
    
    for fname in files_order:
        fpath = os.path.join(BASE_DIR, fname)
        if os.path.exists(fpath):
            with open(fpath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Clean emojis
            content = clean_for_latex(content)
            
            # Convert headers to chapters for main files
            if fname.startswith('00'):
                content = content.replace('# 00 — Fundamentos de Electrotecnia', '# Fundamentos de Electrotecnia')
            elif fname.startswith('01'):
                content = content.replace('# 01 — Corriente Directa', '# Corriente Directa')
            elif fname.startswith('02'):
                content = content.replace('# 02 — Corriente Alterna', '# Corriente Alterna')
            elif fname.startswith('03'):
                content = content.replace('# 03 — Ejercicios Resueltos', '# Ejercicios Resueltos')
            elif fname.startswith('04'):
                content = content.replace('# 04 — Tabla Maestra de Fórmulas', '# Tabla Maestra de Fórmulas')
            elif fname.startswith('05'):
                content = content.replace('# 05 — Referencias', '# Referencias y Bibliografía')
            
            combined.append(content)
            combined.append('\n\n\\newpage\n\n')
    
    return '\n\n'.join(combined)

def generate_pdf():
    """Generate the combined PDF."""
    print("📖 Combinando archivos markdown...")
    combined_md = combine_markdown_files()
    
    # Save combined markdown
    combined_path = os.path.join(BASE_DIR, 'pdfs', 'combined.md')
    with open(combined_path, 'w', encoding='utf-8') as f:
        f.write(combined_md)
    print(f"   Guardado: {combined_path} ({len(combined_md)} chars)")
    
    print("🔧 Generando PDF con template profesional...")
    output_pdf = os.path.join(BASE_DIR, 'pdfs', 'Electrotecnia-Completa.pdf')
    template = os.path.join(BASE_DIR, 'book-template.tex')
    
    cmd = [
        'pandoc', combined_path,
        '-o', output_pdf,
        '--template', template,
        '--pdf-engine', 'xelatex',
        '--toc',
        '--toc-depth', '2',
        '--highlight-style', 'tango',
        '-V', 'title=Electrotecnia Industrial',
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
    
    if result.returncode != 0:
        print(f"❌ Error:")
        print(result.stderr[:2000])
        return None
    
    # Count warnings
    warnings = result.stderr.count('Missing character')
    if warnings > 0:
        print(f"   ⚠️  {warnings} caracteres faltantes en fuentes")
    else:
        print("   ✅ 0 caracteres faltantes")
    
    if os.path.exists(output_pdf):
        size = os.path.getsize(output_pdf)
        print(f"   📄 PDF generado: {output_pdf}")
        print(f"   📦 Tamaño: {size/1024:.0f} KB")
        return output_pdf
    else:
        print("❌ PDF no generado")
        return None

if __name__ == '__main__':
    pdf = generate_pdf()
    if pdf:
        print(f"\n🎉 ¡Listo! Abre el PDF: {pdf}")
