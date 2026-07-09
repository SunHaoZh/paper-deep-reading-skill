#!/usr/bin/env python3
"""Render PDF pages and extract embedded images with PyMuPDF.

Install dependency when needed:
    python -m pip install pymupdf
"""

from __future__ import annotations

import argparse
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf", type=Path)
    parser.add_argument("out_dir", type=Path)
    parser.add_argument("--dpi", type=int, default=180)
    parser.add_argument("--render-pages", action="store_true")
    parser.add_argument("--extract-images", action="store_true")
    args = parser.parse_args()

    try:
        import fitz  # type: ignore
    except ImportError:
        print("ERROR: PyMuPDF is required. Run: python -m pip install pymupdf")
        return 2

    args.out_dir.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(args.pdf)

    if args.render_pages:
        zoom = args.dpi / 72
        matrix = fitz.Matrix(zoom, zoom)
        pages_dir = args.out_dir / "pages"
        pages_dir.mkdir(exist_ok=True)
        for index, page in enumerate(doc, start=1):
            pix = page.get_pixmap(matrix=matrix, alpha=False)
            pix.save(pages_dir / f"page-{index:03d}.png")

    if args.extract_images:
        images_dir = args.out_dir / "images"
        images_dir.mkdir(exist_ok=True)
        count = 0
        for page_index, page in enumerate(doc, start=1):
            for image_index, image in enumerate(page.get_images(full=True), start=1):
                xref = image[0]
                extracted = doc.extract_image(xref)
                ext = extracted.get("ext", "png")
                data = extracted["image"]
                count += 1
                (images_dir / f"page-{page_index:03d}-image-{image_index:02d}.{ext}").write_bytes(data)
        print(f"Extracted {count} embedded images.")

    print(f"Processed {len(doc)} pages.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
