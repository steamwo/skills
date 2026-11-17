# E-commerce AI Product Visual Production Suite

总控 Skill：把真实 SKU 素材、规格、尺寸和品牌资料组织成可审查的电商视觉资产。

## What this suite is for

The suite can orchestrate:
- source reference audit;
- product identity and dimension records;
- scale / perspective calibration;
- multiple hero and supporting images;
- lifestyle and person-use scenes;
- dimension / specification graphics;
- detail-page modules;
- per-image and cross-image QA;
- marketplace export preflight.

## Critical production rule / 商品像素保真

If the user supplies an authoritative product photo:

**MUST use original product RGB as the default product body.**

The preferred pipeline is:

\`\`\`text
real SKU photo
→ alpha mask
→ original RGB cutout
→ generated EMPTY scene
→ independent generated person layer if needed
→ scale / perspective calibration
→ compositing
→ programmatic Chinese copy / dimensions
→ QA
\`\`\`

Do not send the whole product image through a generative model and then call the result “the same SKU”. A visually similar generated product is a fidelity failure.

## Project structure

\`\`\`text
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
  qa/
    contact-sheet.png
    per-image/
    qa-report.md
\`\`\`

## Recommended execution

1. Put real SKU photos, spec sheets, CAD, packaging references, and approved documents in \`input/\`.
2. Copy \`templates/product.example.json\` to the SKU project and fill only verified facts.
3. Run the reference audit.
4. Build product identity and dimension locks.
5. If a scene is required, build \`scale-calibration.json\` before compositing.
6. Build the gallery plan.
7. Generate empty scenes / person layers independently.
8. Composite the original product RGB.
9. Add final Chinese copy and numeric dimensions with design/programmatic tools.
10. Run visual QA and marketplace preflight.

## China marketplace notes / 中国电商说明

淘宝、天猫、京东、拼多多的主图槽位、详情页宽度、文字限制、文件大小等必须以当前卖家后台或官方资料为准，不在 Skill 中永久写死。

中文、数字、尺寸线、Logo、参数表建议使用设计工具或程序排版，避免图像模型生成乱码或错误数字。

## Important limitations

- A single unscaled photo cannot establish complete 3D dimensions.
- A single camera view cannot prove an unseen side.
- Pixel preservation does not guarantee that the alpha mask is correct.
- Visual plausibility does not equal metric accuracy.
- If no image/compositing tool is available, output the plan and executable steps; do not pretend files were generated.
- Do not automatically upload or publish product assets.