# steamwo / Skills

面向 Claude Code、Codex、Cursor 等 Agent 的可复用 Skills 合集。

## 电商产品视觉生产套件

本仓库包含一套模块化的电商产品视觉工作流：从真实 SKU 素材、产品身份与物理尺寸建档，到空间比例校准、多张主图、场景/人物图、规格图、详情页、视觉质检和平台导出预检。

**总控入口：** [ecommerce-product-image-studio](./ecommerce-product-image-studio/SKILL.md)

### 生产链路

1. **事实与素材审查**：识别实拍视角、缺失证据、SKU、售卖数量、材质和规格来源。
2. **产品身份锁定**：锁定轮廓、部件、结构、颜色、纹理和不可修改区域。
3. **物理尺寸锁定**：记录长宽高、重量、包装尺寸、测量口径、来源和公差。
4. **空间比例校准**：使用已知尺寸、场景参照物、地面/桌面平面和相机信息建立尺度关系；无法校准时明确降级。
5. **整套图片规划**：按平台槽位与购买决策规划多张主图、场景图、尺寸图、细节图和详情页模块。
6. **分层制作**：真实商品像素、生成背景、人物、阴影、文字和图形分别处理。
7. **质检与导出**：检查商品身份、物理比例、透视、人物交互、事实文案、跨图一致性和平台规则。

### Skills

| Skill | 用途 |
|---|---|
| [ecommerce-product-image-studio](./ecommerce-product-image-studio/SKILL.md) | 总控编排：从 SKU 资料到完整电商视觉套图 |
| [product-reference-audit](./product-reference-audit/SKILL.md) | 审查实拍、尺寸图、CAD、包装图及证据缺口 |
| [product-identity-lock](./product-identity-lock/SKILL.md) | 锁定商品外形、结构、材质、颜色和细节 |
| [product-dimension-lock](./product-dimension-lock/SKILL.md) | 建立可追溯的物理尺寸与规格档案 |
| [product-scale-calibration](./product-scale-calibration/SKILL.md) | 校准商品、场景参照物、人物和镜头的空间尺度 |
| [ecommerce-gallery-planner](./ecommerce-gallery-planner/SKILL.md) | 规划多张主图、场景图、规格图、细节图和详情页 |
| [product-cutout-composite](./product-cutout-composite/SKILL.md) | 分割真实商品并保留源图 RGB 合成 |
| [lifestyle-scene-composite](./lifestyle-scene-composite/SKILL.md) | 按尺度与透视约束制作产品生活场景图 |
| [human-lifestyle-composite](./human-lifestyle-composite/SKILL.md) | 设计人物参考、姿势、动作和人物图层 |
| [product-human-scene-integration](./product-human-scene-integration/SKILL.md) | 融合真实商品、人物、场景和接触/遮挡关系 |
| [ecommerce-infographic-detail-builder](./ecommerce-infographic-detail-builder/SKILL.md) | 制作尺寸规格图、卖点图和详情页模块 |
| [brand-visual-system](./brand-visual-system/SKILL.md) | 品牌色彩、字体、版式和跨 SKU 视觉统一 |
| [ecommerce-visual-qa](./ecommerce-visual-qa/SKILL.md) | 产品身份、尺度、人物交互、文案和跨图质检 |
| [marketplace-export-preflight](./marketplace-export-preflight/SKILL.md) | 淘宝/天猫/京东/拼多多规格预检和导出 |

### 默认交付范围

每个 SKU 先形成一份可审核的图片计划，再按目标平台规则制作。基准内容通常包括：

- 多张差异化主图：首图、可证实的其他视角、核心卖点/功能展示。
- 产品生活场景图；适用时增加人物使用场景图。
- 产品尺寸规格图和必要的局部尺寸图。
- 材质、工艺、结构和细节图。
- 包装、配件、售卖数量图（仅在资料确认时制作）。
- 独立详情页模块及长图。
- 产品身份档案、尺寸档案、尺度校准记录、素材来源和 QA 报告。

图片数量和槽位以目标平台当前规则及商品实际信息为准。不得为了凑数量伪造视角、卖点、尺寸或配件。

### 快速使用

在 Agent 中打开本仓库，提供 SKU 实拍图、规格表/工程图（如有）和目标平台，然后说：

> 使用 ecommerce-product-image-studio 处理这个 SKU。先审查全部素材和商品事实，建立产品身份档案与物理尺寸档案，检查缺失证据；然后校准场景比例并规划完整图片套图。先展示图片计划和风险，不要猜尺寸、材质、售卖数量或隐藏结构。商品主体优先使用真实像素。先制作代表性样张，通过身份、尺度和文案 QA 后再批量制作。

### 设计原则

- **先事实，后创意**：未知信息必须保持 unknown；估算不能冒充规格。
- **商品真实性优先**：AI 优先生成环境、道具和人物；商品本体使用真实像素或经验证的 CAD/3D 资产。
- **尺寸进入生成前置条件**：物理尺寸、测量口径和证据必须在场景规划前确认。
- **尺度必须有依据**：单张无标尺照片不能恢复完整三维尺寸；视觉上“看起来合理”不等于尺度已验证。
- **透视不能靠拉伸修复**：视角不匹配时重做背景、换用匹配视角或使用可靠 3D/CAD，不扭曲商品。
- **文字与参数单独排版**：图像模型不负责生成最终数字、中文文案和 Logo。
- **可追溯、可复核**：保留源图、Mask、图层、Prompt、工具、尺寸来源、版本和 QA 记录。
- **平台规则当期核验**：不硬编码未经验证的图片尺寸或类目要求。
- **人工审核优先**：不自动上传或发布商品。

本仓库是可复用的 Agent 工作流与辅助工具集合，不内置图像生成模型、API 密钥或付费服务。