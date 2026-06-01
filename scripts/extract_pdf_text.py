#!/usr/bin/env python3
"""
Extract text from a PDF using pypdf.
Usage: python scripts/extract_pdf_text.py input.pdf [output.txt]
"""
import sys
from pathlib import Path


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/extract_pdf_text.py input.pdf [output.txt]")
        sys.exit(1)

    input_path = Path(sys.argv[1])
    if not input_path.exists():
        print(f"Input file not found: {input_path}")
        sys.exit(2)

    output_path = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("extracted_text.txt")

    try:
        from pypdf import PdfReader
    except Exception:
        print("Missing dependency: please run 'python -m pip install pypdf'")
        raise

    reader = PdfReader(str(input_path))
    with output_path.open("w", encoding="utf-8") as f:
        for i, page in enumerate(reader.pages):
            text = page.extract_text()
            f.write(f"\n\n--- Page {i+1} ---\n\n")
            if text:
                f.write(text)
            else:
                f.write("[no text on this page]\n")

    print(f"Wrote extracted text to {output_path}")


if __name__ == "__main__":
    main()
