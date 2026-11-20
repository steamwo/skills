# Wood Product Fidelity

A material-specific fidelity layer for real wood e-commerce products.

## Why this exists

Wood products are unusually easy for image models to “improve” into a different product:
- grain changes;
- knots disappear;
- joints become cleaner;
- screws move;
- end grain changes;
- edge profiles shift;
- finish becomes glossier;
- dimensions drift.

For e-commerce production, those changes are SKU identity failures.

## Default workflow

\`\`\`text
real product photo
→ reference audit
→ identity / wood detail lock
→ alpha mask
→ ORIGINAL PRODUCT RGB
→ empty scene generation
→ scale-aware compositing
→ programmatic copy / dimensions
→ QA
\`\`\`

Do not generate the product body from text as the default production method.

## What AI should generate

AI is well suited for:
- empty interior scenes;
- neutral backdrops;
- independent people;
- independent props;
- visual layout concepts.

The real wood product remains a separate locked asset.

## China-commerce notes / 中国电商

原木类商品常见模块：
- 白底 / 主图
- 场景图
- 木纹 / 结构细节
- 尺寸规格
- 包装清单
- 详情页模块

这些模块必须基于真实商品资料。木种、涂层、承重、环保、食品级等声明不能仅凭图片外观推断。

See:
- \`SKILL.md\`
- \`references/wood-rules.md\`
- \`scripts/render.py\`