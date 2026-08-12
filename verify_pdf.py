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
