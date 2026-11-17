#!/usr/bin/env python3
"""Unpainted wood product fidelity: preserve source RGB, use AI only for alpha masks."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from PIL import Image, ImageOps


def read_oriented_image(path: Path) -> Image.Image:
    with Image.open(path) as fp:
        return ImageOps.exif_transpose(fp).copy()


def extract_product(source: Image.Image):
    original = source.convert("RGBA")

    if "A" in source.getbands() and source.getchannel("A").getextrema()[0] < 255:
        # If already manually cut out, keep its existing Alpha and RGB.
        return original, original.getchannel("A"), "existing_transparency"

    try:
        from rembg import remove
    except ImportError as exc:
        raise RuntimeError(
            "缺少 rembg。请先执行 python -m pip install "
            "-r wood-product-fidelity/requirements.txt"
        ) from exc

    # Segmentation is used ONLY to obtain an Alpha mask.
    # Original RGB values are not copied from the model's result.
    try:
        segmented = remove(source.convert("RGB"))
    except Exception as exc:
        raise RuntimeError(
            "自动抠图失败。首次运行可能需要下载模型；"
            "也可以先手工抠图，输入透明 PNG 再试。"
        ) from exc

    if not isinstance(segmented, Image.Image):
        raise RuntimeError("rembg 没有返回预期的图像结果。")

    mask = segmented.convert("RGBA").getchannel("A")
    original.putalpha(mask)
    return original, mask, "rembg_mask_original_rgb"


def alpha_bbox(mask: Image.Image):
    # Remove very faint alpha noise only for computing the crop bounds.
    bounds = mask.point(lambda p: 255 if p > 10 else 0).getbbox()
    if bounds is None:
        raise RuntimeError("无法识别商品主体：Mask 完全为空。")
    return bounds


def fit_product(foreground: Image.Image, max_w: int, max_h: int):
    ratio = min(max_w / foreground.width, max_h / foreground.height)
    w = max(1, round(foreground.width * ratio))
    h = max(1, round(foreground.height * ratio))
    return foreground.resize((w, h), Image.Resampling.LANCZOS)


def compose(
    foreground: Image.Image,
    background: Image.Image,
    width_ratio: float = 0.80,
    height_ratio: float = 0.80,
    bottom_ratio: float | None = None,
):
    base = background.convert("RGBA")
    width, height = base.size
    layer = fit_product(
        foreground, int(width * width_ratio), int(height * height_ratio)
    )
    x = (width - layer.width) // 2
    if bottom_ratio is None:
        y = (height - layer.height) // 2
    else:
        y = max(0, min(height - layer.height, int(height * bottom_ratio) - layer.height))
    base.alpha_composite(layer, (x, y))
    result = base.convert("RGB")
    return result, layer, x, y


def verify_opaque_product_pixels(
    composite: Image.Image, layer: Image.Image, x: int, y: int
):
    """Verify opaque product pixels were not overwritten during compositing.

    This only checks the compositing stage. It cannot confirm alpha mask quality,
    scene perspective, exact species of wood, or any marketplace rules.
    """
    region = composite.crop((x, y, x + layer.width, y + layer.height)).convert("RGB")
    region_pixels = region.getdata()
    layer_pixels = layer.convert("RGB").getdata()
    alpha_pixels = layer.getchannel("A").getdata()

    checked = 0
    mismatches = 0
    for actual, expected, alpha in zip(region_pixels, layer_pixels, alpha_pixels):
        if alpha == 255:
            checked += 1
            if actual != expected:
                mismatches += 1
    return {
        "fully_opaque_pixels_checked": checked,
        "mismatch_pixels": mismatches,
        "compositing_preserved_opaque_pixels": checked > 0 and mismatches == 0,
    }


def compose_and_save(
    name: str,
    foreground: Image.Image,
    background: Image.Image,
    out_dir: Path,
    **kwargs,
):
    image, layer, x, y = compose(foreground, background, **kwargs)
    image.save(out_dir / name, format="PNG")
    return verify_opaque_product_pixels(image, layer, x, y)


def mask_ratio(mask: Image.Image):
    m = mask.copy()
    m.thumbnail((250, 250))
    pixels = list(m.getdata())
    if not pixels:
        return 0
    return sum(1 for a in pixels if a >= 128) / len(pixels)


def main():
    parser = argparse.ArgumentParser(
        description="Generate wood ecommerce image drafts using REAL product pixels."
    )
    parser.add_argument("--input", type=Path, required=True, help="实拍 JPG 或透明 PNG")
    parser.add_argument("--background", type=Path, default=None, help="不含产品的空场景图片")
    parser.add_argument("--output", type=Path, default=Path("output/wood-product"))
    args = parser.parse_args()

    if not args.input.is_file():
        parser.error(f"找不到真实商品照片：{args.input}")
    if args.background is not None and not args.background.is_file():
        parser.error(f"找不到空场景背景：{args.background}")

    out = args.output
    out.mkdir(parents=True, exist_ok=True)

    image = read_oriented_image(args.input)
    real_product, mask, mask_source = extract_product(image)
    bounds = alpha_bbox(mask)
    cropped = real_product.crop(bounds)

    # Store cutout at the source dimensions so a reviewer can inspect the mask.
    real_product.save(out / "product-cutout.png")
    mask.save(out / "mask.png")

    canvas_size = (1200, 1200)
    white = Image.new("RGB", canvas_size, (255, 255, 255))
    neutral = Image.new("RGB", canvas_size, (246, 241, 234))
    qa = {}
    qa["01-white.png"] = compose_and_save(
        "01-white.png", cropped, white, out
    )
    qa["02-neutral.png"] = compose_and_save(
        "02-neutral.png", cropped, neutral, out
    )

    if args.background is not None:
        # Fit by cropping rather than distorting the scene.
        scene = ImageOps.fit(
            read_oriented_image(args.background).convert("RGB"),
            canvas_size,
            method=Image.Resampling.LANCZOS,
            centering=(0.5, 0.5),
        )
        qa["03-scene.png"] = compose_and_save(
            "03-scene.png",
            cropped,
            scene,
            out,
            width_ratio=0.72,
            height_ratio=0.72,
            bottom_ratio=0.86,
        )

    warnings = [
        "自动抠图可能误删木条、镂空、榫卯、孔洞和天然木纹，请检查 mask.png。",
        "同一拍摄视角合成，不代表真实多角度照片。",
        "像素检查仅检查完全不透明的商品内部，不证明原图颜色、Mask 或场景透视准确。",
        "商品未经过淘宝/天猫/京东/拼多多最新上架规则审核。",
        "原木无漆不等于零表面处理，不可自行编造木种、材质等级或功能宣称。",
    ]
    coverage = mask_ratio(mask)
    if coverage < 0.025 or coverage > 0.95:
        warnings.append(
            "前景遮罩占比异常，可能发生严重抠图错误；必须人工修正后使用。"
        )
    if min(image.size) < 800:
        warnings.append("输入照片分辨率较低，缩放不能恢复真实木纹细节。")
    if args.background is not None:
        warnings.append("请人工检查实物拍摄视角、尺度和场景光线是否协调。")

    report = {
        "status": "MANUAL_REVIEW_REQUIRED",
        "input": str(args.input),
        "input_sha256": hashlib.sha256(args.input.read_bytes()).hexdigest(),
        "original_resolution": list(image.size),
        "mask_source": mask_source,
        "foreground_mask_coverage_approx": round(coverage, 4),
        "mask_crop_bbox_xyxy": list(bounds),
        "opaque_pixel_checks": qa,
        "warnings": warnings,
    }
    (out / "qa-report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print("已输出以下文件：")
    for name in ["product-cutout.png", "mask.png", *qa.keys(), "qa-report.json"]:
        print(" -", out / name)
    if not all(
        item["compositing_preserved_opaque_pixels"] for item in qa.values()
    ):
        print("警告：没有足够的不透明产品像素可验证，或合成像素校验失败。")
    print("状态：需要人工检查木纹、孔位、边缘和场景视角后才可使用。")


if __name__ == "__main__":
    main()
