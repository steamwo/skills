# 电商 AI 产品视觉生产套件

这是 steamwo/skills 中的总控 Skill。它组合商品素材审查、身份锁定、物理尺寸锁定、场景尺度校准、主图规划、人物场景融合、规格图排版、视觉 QA 和平台导出预检。

## 解决的问题

给 Agent 提供真实商品照片、SKU 资料、尺寸规格和目标平台，完成一套可审核的电商视觉资产：
- 产品素材审查、证据矩阵和缺失素材清单。
- 产品身份档案与物理尺寸档案。
- 场景相机、接触平面、参照物和人物的尺度校准。
- 多张差异化主图、角度图、卖点图和生活场景/人物图。
- 尺寸规格图、材质/结构细节图、包装清单图（有证据时）。
- 详情页独立模块与长图。
- 逐图 QA、跨图一致性 QA 和平台预检。

## 核心工作流

1. 审查素材和 SKU 事实；列出哪些信息可见、已确认、估算、未知或冲突。
2. 建立 product-identity.json；锁定真实产品形状、结构、颜色和纹理。
3. 建立 product-dimensions.json；记录长宽高、单位、轴定义、测量状态、证据、公差和包装尺寸。
4. 建立 scale-calibration.json；定义场景坐标、相机、接触平面、参照物和尺度状态。
5. 生成 image-plan.json；规划多张主图、场景/人物图、规格图、细节图和详情页模块。
6. 制作背景、人物、真实商品 cutout、阴影和文字图层。
7. 执行身份、尺寸、尺度、人物交互、文案和跨图 QA。
8. 核验目标平台当期规则后导出。

## 推荐目录

~~~text
sku-001/
  input/
  product.json
  product-identity.json
  product-dimensions.json
  brand.json
  plan/
    asset-audit.md
    evidence-matrix.json
    missing-assets.md
    image-plan.json
    scale-calibration.json
    copy-deck.md
  work/
    masks/
    cutouts/
    backgrounds/
    people/
    shadows/
    composites/
    layouts/
  output/
    master/
    platform/
    detail-modules/
    detail-long.png
  qa/
    contact-sheet.png
    per-image/
    qa-report.md
~~~

## 快速使用

1. 在 SKU 项目目录建立 input/，放入真实照片、尺寸图、CAD/工程资料和包装图（如有）。
2. 复制 templates/product.example.json 为 product.json，填写已确认信息；未知值保持 null/unknown。
3. 如有品牌规范，复制 templates/brand.example.json 为 brand.json。
4. 如制作场景图，复制 templates/scale-calibration.example.json 并按场景填写。
5. 在 Agent 中使用总控 Skill：

   > 使用 ecommerce-product-image-studio 处理 SKU-001。先审查素材、产品事实和尺寸证据，建立产品身份档案、物理尺寸档案和场景尺度计划；然后规划多张有明确用途的主图、场景/人物图、尺寸规格图、细节图和详情页模块。不要猜尺寸、材质、数量或隐藏结构。先展示图片计划和风险，再制作样张并通过身份/尺度 QA 后批量完成。

6. 验证商品资料：

~~~bash
python ecommerce-product-image-studio/scripts/validate_product.py --manifest sku-001/product.json --root sku-001
~~~

7. 详情页模块完成后可拼接成长图：

~~~bash
python ecommerce-product-image-studio/scripts/stitch_detail.py --width 750 --gap 0 --output sku-001/output/detail-long.png sku-001/output/modules/01-hero.png sku-001/output/modules/02-benefits.png sku-001/output/modules/03-scenes.png sku-001/output/modules/04-material.png sku-001/output/modules/05-specs.png
~~~

8. 生成视觉 QA 联系表：

~~~bash
python ecommerce-product-image-studio/scripts/contact_sheet.py --input-dir sku-001/output --output sku-001/qa/contact-sheet.jpg
~~~

## 重要说明

- 本套件是 Agent 工作流和辅助脚本，不自带图像生成模型、CAD 软件或付费 API。
- 商品身份锁定不等于物理尺寸已验证；尺寸图和比例准确场景图必须引用独立尺寸证据。
- 单张无标尺照片不能恢复完整三维尺寸；单一已知长度不能推导所有尺寸轴。
- 2D 合成可以保持商品像素，但不能凭空改变商品视角。需要新视角时使用对应实拍或可靠 CAD/3D。
- 视觉协调不等于计量准确。尺度状态必须明确为 METRICALLY_GROUNDED、VISUALLY_APPROXIMATED 或 SCALE_UNVERIFIED。
- 当前 Agent 没有图像工具时，只输出可执行 Prompt/图层计划，不得假装已生成。
- 平台图片尺寸、格式和槽位按当前类目/卖家后台核验，不硬编码未经验证的数值。
- 不自动上传或发布商品图片。