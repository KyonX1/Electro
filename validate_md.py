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
        
        # Tables: pandoc pipe tables require ONE alignment row (the one
        # right after the header). Extra alignment rows between data rows
        # are rendered as literal ':---:' content, so flag them. A data row
        # is valid when its block contains exactly one alignment row.
        if stripped.startswith('|') and not in_code:
            # find the whole contiguous table block (rows separated by
            # blank lines break the block)
            start = i - 1
            while start > 0 and lines[start - 1].strip().startswith('|'):
                start -= 1
            end = i
            while end < len(lines) and lines[end].strip().startswith('|'):
                end += 1
            block = [lines[j].strip() for j in range(start, end)]
            align_rows = [b for b in block if '---' in b]
            is_align = '---' in stripped
            if is_align:
                # alignment rows are only valid as the 2nd line of the block
                if len(block) < 2 or block[1] != stripped:
                    errors.append(f"{fpath}:{i}: Alignment row not right after header: {stripped[:60]}")
            else:
                # data rows are valid only if the block has exactly 1 alignment row
                if len(align_rows) != 1:
                    errors.append(f"{fpath}:{i}: Table block has {len(align_rows)} alignment rows (expected 1): {stripped[:60]}")
        
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
