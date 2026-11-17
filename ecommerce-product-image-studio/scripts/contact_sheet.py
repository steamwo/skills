#!/usr/bin/env python3
"""Create a labelled contact sheet from a directory of ecommerce image assets."""
from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps

SUPPORTED = {".png", ".jpg", ".jpeg", ".webp", ".tif", ".tiff", ".bmp"}


def ascii_label(value: str, limit: int = 46) -> str:
    safe = value.encode("ascii", "replace").decode("ascii")
    if len(safe) > limit:
        safe = safe[: limit - 3] + "..."
    return safe


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Build a contact sheet for manual ecommerce image review."
    )
    parser.add_argument("--input-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--columns", type=int, default=3)
    parser.add_argument("--cell-width", type=int, default=360)
    parser.add_argument("--cell-height", type=int, default=300)
    parser.add_argument("--padding", type=int, default=16)
    args = parser.parse_args()

    if not args.input_dir.is_dir():
        parser.error(f"Input directory does not exist: {args.input_dir}")
    if min(args.columns, args.cell_width, args.cell_height) <= 0 or args.padding < 0:
        parser.error("Columns and cell dimensions must be positive; padding cannot be negative.")

    output_resolved = args.output.resolve()
    files = sorted(
        path for path in args.input_dir.rglob("*")
        if path.is_file()
        and path.suffix.lower() in SUPPORTED
        and path.resolve() != output_resolved
    )
    if not files:
        parser.error(f"No supported images found in {args.input_dir}")

    rows = (len(files) + args.columns - 1) // args.columns
    sheet_width = args.columns * args.cell_width + (args.columns + 1) * args.padding
    sheet_height = rows * args.cell_height + (rows + 1) * args.padding
    sheet = Image.new("RGB", (sheet_width, sheet_height), "#EAEAEA")
    draw = ImageDraw.Draw(sheet)
    font = ImageFont.load_default()

    for index, path in enumerate(files):
        col = index % args.columns
        row = index // args.columns
        x = args.padding + col * (args.cell_width + args.padding)
        y = args.padding + row * (args.cell_height + args.padding)
        draw.rounded_rectangle(
            (x, y, x + args.cell_width, y + args.cell_height),
            radius=8,
            fill="#FFFFFF",
        )
        try:
            with Image.open(path) as source:
                image = ImageOps.exif_transpose(source).convert("RGB")
            image.thumbnail((args.cell_width - 20, args.cell_height - 54), Image.Resampling.LANCZOS)
            px = x + (args.cell_width - image.width) // 2
            py = y + 8 + (args.cell_height - 54 - image.height) // 2
            sheet.paste(image, (px, py))
        except Exception as exc:
            draw.text((x + 12, y + 18), "UNREADABLE IMAGE", fill="#B00020", font=font)
            draw.text((x + 12, y + 36), ascii_label(str(exc), 38), fill="#333333", font=font)

        label = ascii_label(path.relative_to(args.input_dir).as_posix())
        draw.text((x + 10, y + args.cell_height - 34), label, fill="#222222", font=font)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(args.output, format="JPEG", quality=90, optimize=True)
    print(f"Saved {args.output} with {len(files)} image(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
