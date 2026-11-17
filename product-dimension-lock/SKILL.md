---
name: product-dimension-lock
description: 从用户确认资料、制造商规格、工程图或可靠测量建立 SKU 物理尺寸档案，定义长宽高轴、测量口径、单位、来源、公差和变体差异，阻止 AI 猜测尺寸。
---

# Product Dimension Lock

## 目标

为每个 SKU 建立可追溯的物理尺寸契约。尺寸不是图片上的装饰文字，而是产品身份和空间规划的输入。所有场景比例、人物比例、尺寸图和包装图都必须引用同一份尺寸档案。

## 输入与证据优先级

优先读取：
1. 用户提供并确认的实测记录。
2. 当前 SKU 的工程图、CAD、BOM、制造商规格或正式产品资料。
3. 用户确认的尺寸照片/测量视频，且测量基准、方向和标尺清晰。
4. 其他视觉材料只能辅助理解外形，不能单独证明完整三维尺寸。

禁止把竞品规格、同类商品常见尺寸、图片像素、模型估算或不明来源网页数据当作当前 SKU 的已验证尺寸。

## 尺寸字段与单位

标准化存储：
- 产品本体：length_mm、width_mm、height_mm。
- 商品净重：net_weight_g；如有毛重，单独记录 gross_weight_g。
- 包装：package_length_mm、package_width_mm、package_height_mm、gross_weight_g。
- 可选尺寸：直径、厚度、内径、孔距、展开尺寸、折叠尺寸、最大外廓、有效使用尺寸。
- 变体：每个 SKU/尺寸/颜色/套装分别记录，不用一个变体的数据覆盖其他变体。

统一使用 mm 和 g 存储；展示时再转换为 cm、m 或 kg。原始值和原始单位应保留在证据记录中。净重、毛重、包装尺寸与产品本体尺寸必须明确区分。

## 轴定义与测量口径

每个产品必须明确尺寸轴：
- length：按商品主视图定义的左右/主方向。
- width：前后/深度方向。
- height：底部支撑平面至最高点。
- 非标准形状、圆形、可折叠或多姿态产品必须单独定义测量方向和状态。

不得默认所有产品的长宽高方向相同。记录测量状态（组装/折叠/展开/压缩/空载）、是否含突出件、脚垫、把手、盖子和配件。包装尺寸永远独立于产品尺寸。

## 状态模型

每个尺寸记录一个状态：
- user_confirmed：用户明确确认的测量值。
- document_verified：当前 SKU 的正式规格/工程文件支持。
- estimated：由照片、模型或间接信息估算；只用于内部草案，不得作为规格承诺或精确尺度基准。
- unknown：没有足够证据。
- conflicting：多个可信来源不一致，等待解决。
- partial：部分尺寸轴有证据；必须逐轴记录来源，不得作为完整三维尺度。

## 建档步骤

1. 读取产品身份档案和素材审查报告，确认 SKU 与变体。
2. 从证据源提取原始尺寸，保留原始单位、原始文本和文件/页码/表格位置。
3. 标准化到 mm/g，同时保留原始值，检查单位换算。
4. 定义长宽高轴、测量基准、产品状态和是否包含突出件。
5. 记录测量方法、测量者/来源、日期、公差或不确定度。
6. 对冲突值逐项列出来源，不取平均、不擅自选择。
7. 将尺寸档案回写到 product.json 或独立 product-dimensions.json。
8. 将未知项和补测建议写入 missing-assets.md。

## 数据结构建议

~~~json
{
  "sku": "SKU-001",
  "unit": "mm",
  "dimensions": {
    "length_mm": null,
    "width_mm": null,
    "height_mm": null,
    "net_weight_g": null,
    "status": "unknown",
    "measurement_method": "unknown",
    "measurement_state": "assembled",
    "axis_definition": {
      "length": "front-view left-to-right",
      "width": "front-to-back",
      "height": "support plane to highest point"
    },
    "tolerance_mm": null,
    "evidence": [],
    "notes": []
  },
  "packaging_dimensions": {
    "length_mm": null,
    "width_mm": null,
    "height_mm": null,
    "gross_weight_g": null,
    "status": "unknown",
    "evidence": []
  }
}
~~~

## 输出

- product-dimensions.json：机器可读尺寸档案。
- dimensions-evidence.md：来源、测量口径、单位换算、公差和冲突记录。
- missing-dimensions.md：待确认轴、重量、包装或变体信息。
- dimension-diagram-brief.md：尺寸图需要呈现的方向、数值和单位。

## 下游约束

- product-scale-calibration 只能把已验证的尺寸作为精确尺度输入；estimated 必须显式标记。
- ecommerce-gallery-planner 不得规划无证据的数字规格图。
- ecommerce-infographic-detail-builder 只能使用档案中的数值，尺寸线与轴定义必须一致。
- ecommerce-visual-qa 必须逐项对照尺寸档案和最终文案。

## 完成条件

每个已输出的数字都有来源、单位、轴定义和测量口径。未知项仍然是 unknown；冲突项仍然是 conflicting。不得为追求“资料完整”而补造数值。