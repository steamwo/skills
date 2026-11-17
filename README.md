# steamwo / Skills

面向 Claude Code、Codex、Cursor 等 Agent 的可复用 Skills 合集。

## 电商 AI 产品图套件

从真实商品资料出发，完成商品身份锁定、图片规划、主图/辅图/场景图/细节图/规格图/详情页制作、保真质检与平台导出预检。

**总控入口：** [ecommerce-product-image-studio](./ecommerce-product-image-studio/SKILL.md)

### 推荐组合

| Skill | 用途 |
|---|---|
| [ecommerce-product-image-studio](./ecommerce-product-image-studio/SKILL.md) | 总控编排：从商品资料到整套电商产品图 |
| [product-reference-audit](./product-reference-audit/SKILL.md) | 检查实拍素材、视角覆盖和缺失信息 |
| [product-identity-lock](./product-identity-lock/SKILL.md) | 建立产品身份档案，锁定外形、结构、颜色和细节 |
| [wood-product-fidelity](./wood-product-fidelity/SKILL.md) | 原木/无漆木制品纹理与构造保真 |
| [product-cutout-composite](./product-cutout-composite/SKILL.md) | 抠图、Mask 检查、真实商品像素合成 |
| [ecommerce-gallery-planner](./ecommerce-gallery-planner/SKILL.md) | 主图、辅图、卖点图、细节图和场景图规划 |
| [lifestyle-scene-composite](./lifestyle-scene-composite/SKILL.md) | 空场景生成与真实商品合成 |
| [ecommerce-infographic-detail-builder](./ecommerce-infographic-detail-builder/SKILL.md) | 中文卖点图、规格图、详情页模块与长图 |
| [brand-visual-system](./brand-visual-system/SKILL.md) | 品牌色彩、字体、版式和跨 SKU 视觉统一 |
| [ecommerce-visual-qa](./ecommerce-visual-qa/SKILL.md) | 产品保真、画面、文案和整套图一致性质检 |
| [marketplace-export-preflight](./marketplace-export-preflight/SKILL.md) | 淘宝/天猫/京东/拼多多规格预检和导出 |

### 快速使用

在 Agent 中打开本仓库，先说：

> 使用 ecommerce-product-image-studio，为我提供的商品照片制作一套电商产品图。先检查素材和商品事实，锁定产品身份，输出图片规划；未经证实的参数不要编造，商品本体不要重绘。先完成主图与场景图样张，再通过保真质检后继续制作其余图片。

完整使用说明见 [电商产品图套件 README](./ecommerce-product-image-studio/README.md)。

## 目录约定

每个 Skill 是一个独立目录，包含 SKILL.md，可按需复制到 Agent 所支持的 Skills 目录。通用规则与专项规则分离；专项 Skill 不重复实现总控流程。

## 设计原则

- 先事实，后创意；商品真实性高于视觉创意。
- AI 生成场景、布景和装饰；商品本体尽量使用真实像素。
- 图片模型、CLI、MCP 和 API 由使用者配置；Skills 不内置密钥，也不默认调用付费服务。
- 自动检查只报告可验证项目；不能把“模型说没问题”当作产品保真证明。
- 平台尺寸、格式、类目限制按商家后台当期规则核验，不硬编码未经验证的数值。
- 未经人工审核不自动上传或发布商品图片。

## 参考与致谢

本套件为独立编写，工作流设计参考了公开的电商图片 Skills 项目，包括：
- [xianyu110/ecommerce-image-skills](https://github.com/xianyu110/ecommerce-image-skills)
- [dlazy-ai/ecommerce-skills](https://github.com/dlazy-ai/ecommerce-skills)

本仓库不复制上述项目的实现文件；参考其电商任务拆分、批量工作流、品牌配置和生成后质检等思路，并针对家居/日用品及原木材质重新设计。若未来引入其代码或实质性复制内容，需单独保留相应版权和 MIT License 声明。
