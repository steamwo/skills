#!/usr/bin/env python3
"""Render an ecommerce infographic grid from approved image masters and exact copy."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from PIL import Image, ImageColor, ImageDraw, ImageFont, ImageOps


def load_manifest(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, dict):
        raise ValueError("manifest root must be an object")
    return data


def positive_int(value: Any, name: str) -> int:
    if not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")
    return value


def color(value: Any, name: str) -> str:
    if not isinstance(value, str) or not value:
        raise ValueError(f"{name} must be a color string")
    ImageColor.getrgb(value)
    return value


def fit_image(image: Image.Image, size: tuple[int, int], mode: str, background: str) -> Image.Image:
    if mode == "cover":
        return ImageOps.fit(image, size, method=Image.Resampling.LANCZOS)
    if mode == "contain":
        contained = ImageOps.contain(image, size, method=Image.Resampling.LANCZOS)
        canvas = Image.new("RGB", size, background)
        x = (size[0] - contained.width) // 2
        y = (size[1] - contained.height) // 2
        canvas.paste(contained, (x, y))
        return canvas
    raise ValueError(f"unsupported fit mode: {mode!r}")


def text_width(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont) -> int:
    box = draw.textbbox((0, 0), text, font=font)
    return box[2] - box[0]


def wrap_text(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont, max_width: int) -> list[str]:
    if not text:
        return []
    lines: list[str] = []
    current = ""
    for ch in text:
        candidate = current + ch
        if current and text_width(draw, candidate, font) > max_width:
            lines.append(current)
            current = ch
        else:
            current = candidate
    if current:
        lines.append(current)
    return lines


def draw_text_block(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    text: str,
    font: ImageFont.FreeTypeFont,
    fill: str,
    max_width: int,
    line_gap: int,
) -> int:
    x, y = xy
    for line in wrap_text(draw, text, font, max_width):
        draw.text((x, y), line, font=font, fill=fill)
        box = draw.textbbox((x, y), line, font=font)
        y = box[3] + line_gap
    return y


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Build a deterministic ecommerce grid from approved semantic masters."
    )
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument(
        "--font",
        type=Path,
        help="CJK-capable font file. Required when any cell contains title/subtitle text.",
    )
    parser.add_argument(
        "--font-bold",
        type=Path,
        help="Optional bold font for titles; defaults to --font.",
    )
    args = parser.parse_args()

    if not args.manifest.is_file():
        parser.error(f"manifest not found: {args.manifest}")

    try:
        data = load_manifest(args.manifest)
        canvas_cfg = data.get("canvas", {})
        if not isinstance(canvas_cfg, dict):
            raise ValueError("canvas must be an object")

        width = positive_int(canvas_cfg.get("width"), "canvas.width")
        height = positive_int(canvas_cfg.get("height"), "canvas.height")
        columns = positive_int(canvas_cfg.get("columns"), "canvas.columns")
        rows = positive_int(canvas_cfg.get("rows"), "canvas.rows")
        gap = canvas_cfg.get("gap", 0)
        padding = canvas_cfg.get("padding", 0)
        if not isinstance(gap, int) or gap < 0:
            raise ValueError("canvas.gap must be a non-negative integer")
        if not isinstance(padding, int) or padding < 0:
            raise ValueError("canvas.padding must be a non-negative integer")

        background = color(canvas_cfg.get("background", "#FFFFFF"), "canvas.background")
        cell_background = color(
            canvas_cfg.get("cell_background", "#FFFFFF"), "canvas.cell_background"
        )
        text_color = color(canvas_cfg.get("text_color", "#222222"), "canvas.text_color")
        accent_color = color(canvas_cfg.get("accent_color", text_color), "canvas.accent_color")

        cells = data.get("cells")
        if not isinstance(cells, list) or not cells:
            raise ValueError("cells must be a non-empty array")
        if len(cells) > rows * columns:
            raise ValueError("cell count exceeds rows × columns")

        has_text = any(
            isinstance(cell, dict) and (cell.get("title") or cell.get("subtitle"))
            for cell in cells
        )
        if has_text and (args.font is None or not args.font.is_file()):
            raise ValueError("a valid --font is required for exact text rendering")
        if args.font_bold is not None and not args.font_bold.is_file():
            raise ValueError(f"bold font not found: {args.font_bold}")

        inner_w = width - 2 * padding - (columns - 1) * gap
        inner_h = height - 2 * padding - (rows - 1) * gap
        if inner_w <= 0 or inner_h <= 0:
            raise ValueError("canvas is too small for configured padding/gap")
        cell_w = inner_w // columns
        cell_h = inner_h // rows
        if cell_w <= 0 or cell_h <= 0:
            raise ValueError("computed cell size is invalid")

        output = Image.new("RGB", (width, height), background)
        draw = ImageDraw.Draw(output)
        base_font_size = max(18, round(min(cell_w, cell_h) * 0.055))
        title_font = (
            ImageFont.truetype(str(args.font_bold or args.font), base_font_size)
            if has_text
            else None
        )
        subtitle_font = (
            ImageFont.truetype(str(args.font), max(14, round(base_font_size * 0.58)))
            if has_text
            else None
        )

        base_dir = args.manifest.parent
        for index, cell in enumerate(cells):
            if not isinstance(cell, dict):
                raise ValueError(f"cells[{index}] must be an object")
            image_value = cell.get("image")
            if not isinstance(image_value, str) or not image_value:
                raise ValueError(f"cells[{index}].image is required")
            image_path = (base_dir / image_value).resolve()
            if not image_path.is_file():
                raise ValueError(f"cells[{index}] image not found: {image_path}")

            col = index % columns
            row = index // columns
            x = padding + col * (cell_w + gap)
            y = padding + row * (cell_h + gap)
            draw.rectangle((x, y, x + cell_w, y + cell_h), fill=cell_background)

            title = cell.get("title", "")
            subtitle = cell.get("subtitle", "")
            if not isinstance(title, str) or not isinstance(subtitle, str):
                raise ValueError(f"cells[{index}] title/subtitle must be strings")

            text_pad = max(12, round(cell_w * 0.04))
            text_h = 0
            if title or subtitle:
                text_h = max(round(cell_h * 0.24), base_font_size * 2)
                draw.rectangle((x, y, x + 5, y + text_h), fill=accent_color)
                ty = y + text_pad
                if title and title_font is not None:
                    ty = draw_text_block(
                        draw,
                        (x + text_pad, ty),
                        title,
                        title_font,
                        text_color,
                        cell_w - 2 * text_pad,
                        3,
                    )
                if subtitle and subtitle_font is not None:
                    draw_text_block(
                        draw,
                        (x + text_pad, ty + 2),
                        subtitle,
                        subtitle_font,
                        text_color,
                        cell_w - 2 * text_pad,
                        2,
                    )

            image_top = y + text_h
            image_h = cell_h - text_h
            if image_h <= 0:
                raise ValueError(f"cells[{index}] text zone leaves no image area")

            fit_mode = cell.get("fit", "cover")
            if fit_mode not in {"cover", "contain"}:
                raise ValueError(f"cells[{index}].fit must be cover or contain")
            with Image.open(image_path) as source:
                image = ImageOps.exif_transpose(source).convert("RGB")
            rendered = fit_image(image, (cell_w, image_h), fit_mode, cell_background)
            output.paste(rendered, (x, image_top))

        args.output.parent.mkdir(parents=True, exist_ok=True)
        output.save(args.output, format="PNG", optimize=True)
        print(f"Saved {args.output} ({width}x{height}) from {len(cells)} approved cell(s)")
        return 0
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    raise SystemExit(main())
