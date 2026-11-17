---
name: ecommerce-gallery-planner
description: 根据已核实的 SKU 事实、物理尺寸、平台槽位和购买决策路径，规划多张差异化电商主图、场景/人物图、尺寸规格图、材质细节图、包装图和详情页模块。
---

# Ecommerce Gallery Planner

## 目标

把商品事实、产品身份、物理尺寸和购买决策路径转化为可执行的完整图片计划。规划的是一套有明确分工的图片，不是同一张图反复换背景。

## 必需输入

- product.json、product-identity.json、product-dimensions.json。
- product-reference-audit 的素材审查、证据矩阵和缺失素材清单。
- scale-calibration.json（任何比例型场景图/人物图必须有）。
- brand.json（如有）。
- 目标平台、店铺类目、广告位和当前图片槽位规则。

## 基准图片组

先核验目标平台当前主图槽位和详情页要求，再确定数量。未指定平台时规划通用母版，不宣称符合任何平台槽位。通常应覆盖以下不同用途：

| 图片角色 | 内容与验收重点 |
|---|---|
| 01 首图/核心主图 | 一眼识别商品；主体清晰；商品本体真实 |
| 02 其他主图视角 | 展示结构/侧面/背面；必须有对应实拍或可靠 CAD/3D |
| 03 核心卖点图 | 只呈现已证实的功能、材质或差异 |
| 04 生活场景图 | 产品进入真实用途环境；比例和透视经过校准 |
| 05 人物使用场景图 | 仅在使用逻辑适用时制作；人物尺度、动作和接触合理 |
| 06 尺寸规格图 | 使用已确认尺寸、单位、轴定义和测量口径 |
| 07 材质/结构细节图 | 真实细节来源；不补造木纹、孔位或工艺 |
| 08 包装/配件/售卖清单图 | 只按当前 SKU 和包装证据呈现 |
| 09 详情页模块 | 商品整体、价值点、场景、细节、尺寸、包装/注意事项 |

以上是内容角色，不是每个商品都必须凑齐九张。每个 SKU 至少应规划多张彼此不同的主图/展示图；若某角色缺少证据，应标记 BLOCKED/NOT_APPLICABLE，并说明补充资料，不得虚构填充。

## 图片计划字段

每张图片记录：
- id、sku、role、platform、slot、output_path、priority。
- purpose、target_question、headline、body_copy、evidence_sources。
- source_images、source_view、required_missing_assets。
- composition、camera_view、camera_height、lens_look、perspective、background、lighting、props、negative_space。
- product_pixel_policy、product_pose、product_anchor、contact_plane。
- scale_status、scale_calibration_ref、reference_objects、person_ref（如适用）。
- generation_method、layer_plan、text_overlay_plan、aspect_ratio_source。
- risks、acceptance_criteria、status。

## 规划规则

1. 一张图只承担一个主要购买决策任务；不要重复信息。
2. 首图先让用户识别商品，不堆叠未经证实的卖点。
3. 其他视角必须有同 SKU 的实拍或可信 CAD/3D 支持；不能让模型猜背面。
4. 场景图必须先有尺寸/尺度计划。尺寸未知时标记 SCALE_UNVERIFIED，不用门、沙发、人物等制造“看似准确”的比例。
5. 人物图必须说明人物动作、身高依据/估算状态、接触点和遮挡关系。
6. 尺寸图只用 product-dimensions.json 中可核实的数值；未知轴不画数字。
7. 包装、配件、数量和套装内容必须来自 SKU/包装证据。
8. 每个卖点对应一个 evidence_source；没有证据就删去或标记待确认。
9. 平台像素尺寸、格式、体积和槽位按当期官方/卖家后台核验，不硬编码。
10. 每张图指定 identity gate、scale gate、copy gate 和最终验收标准。

## 输出

- image-plan.json：机器可读的逐图计划。
- plan-summary.md：图片列表、用途、优先级、数量和制作顺序。
- blocked-assets.md：因缺少视角、尺寸、人物参考、包装或卖点证据而不能制作的图片。
- copy-deck.md：最终文案与事实来源。

先展示计划、风险和缺失素材。得到确认后批量制作；用户已明确要求直接执行时，先做代表性样张并执行 QA。