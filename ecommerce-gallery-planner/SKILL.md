---
name: ecommerce-gallery-planner
description: 为淘宝、天猫、京东、拼多多商品策划主图、辅图、场景图、卖点图、细节图、规格图和详情页内容，输出可执行的图片清单。
---

# Ecommerce Gallery Planner

## 目标

把商品事实和购买决策路径转化为一套完整图片计划。先规划再制作，不机械套用固定张数。

## 输入

- product.json 与 product-identity.json。
- 素材审查报告和缺失素材清单。
- 品牌视觉配置（如有）。
- 目标平台、店铺类目和图片槽位。
- 用户确认的商品卖点、尺寸、包装和价格信息（如需要）。

## 推荐内容模块

1. 主图：一眼识别商品，真实主体清晰。
2. 核心卖点图：只呈现已证实的功能/特点。
3. 使用场景图：真实商品放入兼容的生活环境。
4. 材质细节图：来自真实照片的木纹、纹理、表面处理特写。
5. 结构细节图：孔位、接缝、五金、连接和边缘。
6. 尺寸规格图：只使用已确认参数和单位。
7. 包装/配件图：准确展示真实售卖内容。
8. 详情页模块：按购买决策顺序组织信息。
9. 对比图：仅在对比依据可靠且表达公平时制作。

## 每张图的计划字段

- id、role、platform、slot、output_path。
- purpose、headline、body_copy、evidence_sources。
- source_images、required_missing_assets。
- composition、camera_view、background、lighting、props、negative_space。
- product_pixel_policy、generation_method、aspect_ratio_source。
- risks、acceptance_criteria、status。

## 策划原则

- 一张图只承担一个主要信息任务。
- 不把未知参数写进文案，不编造卖点。
- 不为了凑张数重复相同内容。
- 不同平台的图槽位和尺寸需单独核验。
- 细节图不得用 AI 创造源图不存在的纹理。
- 套装、配件和数量必须有 SKU/包装资料支持。
- 图片文字应在生图后单独排版。

## 输出

生成 image-plan.json 和 plan-summary.md。标明哪些图可以立即制作、哪些图需要补拍、哪些图需要用户确认。先展示计划，得到确认后再批量制作。
