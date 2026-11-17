#!/usr/bin/env python3
"""Join independently designed detail-page modules into one vertical image."""
from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageOps


def load_module(path: Path, width: int) -> Image.Image:
    with Image.open(path) as source:
        image = ImageOps.exif_transpose(source).convert("RGBA")
    if image.width != width:
        height = max(1, round(image.height * width / image.width))
        image = image.resize((width, height), Image.Resampling.LANCZOS)
    return image


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Stitch detail page modules vertically without distorting them."
    )
    parser.add_argument("images", nargs="+", type=Path, help="Modules in display order")
    parser.add_argument("--width", type=int, required=True, help="Output width in pixels")
    parser.add_argument("--gap", type=int, default=0, help="Vertical gap between modules")
    parser.add_argument(
        "--background",
        default="#FFFFFF",
        help="Canvas background color, e.g. #FFFFFF",
    )
    parser.add_argument("--output", type=Path, required=True, help="Output PNG path")
    args = parser.parse_args()

    if args.width <= 0:
        parser.error("--width must be greater than zero")
    if args.gap < 0:
        parser.error("--gap cannot be negative")

    missing = [str(path) for path in args.images if not path.is_file()]
    if missing:
        parser.error("Missing input image(s): " + ", ".join(missing))

    modules = [load_module(path, args.width) for path in args.images]
    total_height = sum(image.height for image in modules) + args.gap * (len(modules) - 1)
    try:
        canvas = Image.new("RGBA", (args.width, total_height), args.background)
    except ValueError as exc:
        parser.error(f"Invalid --background color: {exc}")

    y = 0
    for image in modules:
        canvas.alpha_composite(image, (0, y))
        y += image.height + args.gap

    args.output.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(args.output, format="PNG", optimize=True)
    print(f"Saved {args.output} ({args.width} x {total_height})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
