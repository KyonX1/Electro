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
