#!/usr/bin/env python3
"""原木商品高保真出图：抠图仅提供透明度，商品颜色和纹理来自真实照片。"""
import argparse
import json
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

FONT_CANDIDATES = [
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
    "/usr/share/fonts/truetype/wqy/wqy-microhei.ttc",
    "C:/Windows/Fonts/msyh.ttc",
    "/System/Library/Fonts/PingFang.ttc",
]


def load_font(size):
    for path in FONT_CANDIDATES:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default(size)


def cutout_from_photo(photo):
    """只使用分割模型的 alpha；商品 RGB 从原始照片直接复制。"""
    if photo.mode in ("RGBA", "LA") and photo.getextrema()[-1][0] < 255:
        return photo.convert("RGBA"), "input_alpha"
    from rembg import remove, new_session

    original = photo.convert("RGB")
    segmentation = remove(original, session=new_session("u2net")).convert("RGBA")
    result = original.convert("RGBA")
    result.putalpha(segmentation.getchannel("A"))
    return result, "rembg_u2net"


def crop_alpha(product):
    mask = product.getchannel("A")
    bbox = mask.point(lambda a: 255 if a > 12 else 0).getbbox()
    if bbox is None:
        raise ValueError("没有识别到商品主体。请换一张背景简单、商品完整的照片。")
    return product.crop(bbox)


def fit_product(product, max_w, max_h):
    ratio = min(max_w / product.width, max_h / product.height)
    size = (
        max(1, round(product.width * ratio)),
        max(1, round(product.height * ratio)),
    )
    return product.resize(size, Image.Resampling.LANCZOS)


def draw_shadow(background, px, py, pw, ph):
    """影子始终位于原始商品像素之下，避免涂改商品纹理。"""
    layer = Image.new("RGBA", background.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    foot = py + ph
    rx = max(32, round(pw * 0.40))
    ry = max(10, round(pw * 0.06))
    d.ellipse(
        (px + pw // 2 - rx, foot - ry, px + pw // 2 + rx, foot + ry),
        fill=(40, 30, 20, 50),
    )
    layer = layer.filter(ImageFilter.GaussianBlur(max(8, round(pw * 0.025))))
    background.alpha_composite(layer)


def place_product(background, product, scale=0.78, y_bias=0.54, shadow=True):
    item = fit_product(
        product, int(background.width * scale), int(background.height * scale)
    )
    x = (background.width - item.width) // 2
    y = max(
        0,
        min(
            background.height - item.height,
            int(background.height * y_bias - item.height / 2),
        ),
    )
    if shadow:
        draw_shadow(background, x, y, item.width, item.height)
    background.alpha_composite(item, (x, y))
    return background


def soft_background(width, height):
    """中性非生成式背景，不模仿木纹，也不覆盖商品纹理。"""
    bg = Image.new("RGBA", (width, height), (246, 241, 232, 255))
    d = ImageDraw.Draw(bg)
    for y in range(height):
        t = y / max(height - 1, 1)
        rgb = (246 - round(7 * t), 241 - round(7 * t), 232 - round(9 * t))
        d.line((0, y, width, y), fill=(*rgb, 255))
    d.line(
        (0, int(height * 0.79), width, int(height * 0.79)),
        fill=(222, 212, 198, 255),
        width=2,
    )
    return bg


def make_detail_long(product):
    canvas = Image.new("RGBA", (750, 2700), (249, 247, 243, 255))
    d = ImageDraw.Draw(canvas)
    title = load_font(43)
    sub = load_font(24)
    small = load_font(19)

    d.text((52, 82), "原木 · 实物展示", font=title, fill=(59, 46, 35))
    d.text(
        (54, 151),
        "保留真实商品的木纹、结构与自然色差",
        font=sub,
        fill=(93, 80, 67),
    )

    first = Image.new("RGBA", (650, 930), "white")
    place_product(first, product, scale=0.86, y_bias=0.49, shadow=False)
    canvas.alpha_composite(first, (50, 220))

    d.text((52, 1195), "01 / 实物整体", font=title, fill=(59, 46, 35))
    d.text(
        (54, 1265),
        "产品主体来自原始照片，不用 AI 重绘木材纹理",
        font=sub,
        fill=(93, 80, 67),
    )

    # 真实产品的中心裁切是示范模板，不保证一定是需要展示的木纹部位。
    resized = fit_product(product, 620, 720)
    cx, cy = resized.width // 2, resized.height // 2
    cw = min(resized.width, max(140, resized.width // 2))
    ch = min(resized.height, max(140, resized.height // 2))
    crop = resized.crop(
        (cx - cw // 2, cy - ch // 2, cx - cw // 2 + cw, cy - ch // 2 + ch)
    )
    crop_bg = Image.new("RGBA", (650, 650), "white")
    fitted_crop = fit_product(crop, 640, 640)
    crop_bg.alpha_composite(
        fitted_crop,
        ((650 - fitted_crop.width) // 2, (650 - fitted_crop.height) // 2),
    )
    canvas.alpha_composite(crop_bg, (50, 1360))
    d.text((52, 2060), "02 / 真实局部放大", font=title, fill=(59, 46, 35))
    d.text(
        (54, 2135),
        "请人工检查：局部是否包含需要展示的木纹与结构",
        font=small,
        fill=(93, 80, 67),
    )
    d.line((52, 2340, 698, 2340), fill=(208, 196, 182), width=2)
    d.text(
        (52, 2405), "无漆原木 · 以实物资料为准",
        font=sub, fill=(59, 46, 35)
    )
    d.text(
        (52, 2460),
        "具体木种、尺寸及工艺信息请由商家确认后添加",
        font=small,
        fill=(93, 80, 67),
    )
    return canvas.convert("RGB")


def main():
    parser = argparse.ArgumentParser(description="原木制品：使用真实产品像素合成商品图")
    parser.add_argument("--input", default="input/product.jpg")
    parser.add_argument("--background", default="input/background.jpg")
    parser.add_argument("--output", default="output")
    args = parser.parse_args()

    src = Path(args.input)
    if not src.exists():
        raise SystemExit(
            f"未找到照片：{src}。请先将真实照片上传到 input/product.jpg"
        )
    dest = Path(args.output)
    dest.mkdir(parents=True, exist_ok=True)
    photo = Image.open(src)
    product_raw, method = cutout_from_photo(photo)

    alpha_preview = product_raw.getchannel("A").resize((100, 100))
    coverage = sum(a > 128 for a in list(alpha_preview.getdata())) / 10000
    if coverage < 0.015 or coverage > 0.985:
        raise SystemExit(
            "抠图可能失败，前景比例为 %.1f%%；请换背景干净、商品完整的照片。"
            % (coverage * 100)
        )

    product_raw.save(dest / "原始比例_透明产品.png")
    product = crop_alpha(product_raw)
    product.save(dest / "透明产品_裁切.png")

    white = Image.new("RGBA", (1200, 1200), "white")
    place_product(white, product, 0.78, 0.51, False)
    white.convert("RGB").save(dest / "01_白底主图.jpg", quality=95)

    warm = soft_background(1200, 1200)
    place_product(warm, product, 0.76, 0.54, True)
    warm.convert("RGB").save(dest / "02_暖色展示图.jpg", quality=95)

    scene_file = Path(args.background)
    scene_out = None
    if scene_file.exists():
        bg = Image.open(scene_file).convert("RGBA")
        bg = bg.resize((1200, 1200), Image.Resampling.LANCZOS)
        place_product(bg, product, 0.69, 0.54, True)
        bg.convert("RGB").save(dest / "03_自选场景合成.jpg", quality=95)
        scene_out = "03_自选场景合成.jpg"

    make_detail_long(product).save(dest / "04_详情长图.jpg", quality=95)

    outputs = [
        "01_白底主图.jpg",
        "02_暖色展示图.jpg",
        "04_详情长图.jpg",
    ]
    if scene_out:
        outputs.append(scene_out)
    report = {
        "source": str(src),
        "source_size": list(photo.size),
        "alpha_source": method,
        "mask_coverage_approx": round(coverage, 4),
        "outputs": outputs,
        "status": "需要人工核验；未自动通过任何电商平台审核",
        "review": [
            "检查镂空、圆孔、木节、连接件、板材边缘是否被抠错",
            "检查原木颜色、无漆哑光质感和商品比例是否合理",
            "检查详情页局部裁切是否包含需要展示的木纹与结构",
            "输出仍是原始拍摄视角，不代表真实的新角度",
            "上传前独立核对淘宝/天猫/京东/拼多多的最新图片规范",
        ],
        "important": (
            "第一版使用 AI 抠图，不调用 AI 生成式图片 API。"
            "要添加自己的空场景背景，可上传 input/background.jpg 再运行。"
        ),
    }
    (dest / "质检说明.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    print("制作完成，输出目录：", dest.resolve())
    for filename in outputs:
        print(" -", filename)
    print("请先检查", dest / "质检说明.json")


if __name__ == "__main__":
    main()
