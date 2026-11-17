---
name: wood-product-fidelity
description: Produce faithful ecommerce images for unpainted natural-wood household products. Use when a user wants real product images, listings or detail pages without lost wood grain or product construction.
---

# 原木商品保真 Skill

## 用户入口

用户只需提供 `input/product.jpg`。第一步运行：

```bash
python -m pip install -r requirements.txt
python generate.py --input input/product.jpg --output output
```

如果使用 GitHub 网页端：上传照片后，在 Actions 手动运行 `原木商品出图` 工作流并下载工件。

## 优先级

真实商品的木纹、端面、榫卯、孔洞、板材数量、倒角、自然色差和无漆质感 > 创意场景。不能通过生成式模型重画或虚构商品。

## 输出与 QA

1. 查看 `output/原始比例_透明产品.png` 和 `output/透明产品_裁切.png`，确认木质镂空和边缘没有被抠错。
2. 查看 `01_白底主图.jpg` 和 `02_暖色展示图.jpg`，检查是否改变木纹、天然色差或产品结构。
3. 查看 `04_详情长图.jpg`，确认自动局部放大是否真的包含关键细节；若没有，要求用户补拍特写，而不是编造纹理。
4. 阅读 `质检说明.json`；输出属于 **待人工审核**，不得宣称已通过平台合规检查。
5. 如果 `input/background.jpg` 存在，额外合成室内场景；必须保证透视、拍摄视角和接触关系合理。
6. 如果需要新视角，明确要求补充实拍图，不能虚构木材背面或隐藏构造。

## 能力边界

这是抠图加合成的第一版，不包含自动生成背景的付费 API。优先指导用户完成一次成功运行，不要一开始安装多个大型开源 Skill 仓库，也不要在用户没有明确授权时调用付费 API 或上传图片到其他服务。
