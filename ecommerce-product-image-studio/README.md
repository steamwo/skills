# 电商 AI 产品图生产套件

这是 steamwo/skills 技能合集中的总控 Skill。它组合多个专项 Skill，面向 Claude Code、Codex、Cursor。当前重点是淘宝/天猫/京东/拼多多的家居、日用品与原木制品。

## 它解决什么问题

给 Agent 一组真实商品照片和 SKU 资料，让它完成：

- 商品素材审查与产品身份档案
- 主图、辅图、场景图、材质细节图、结构图、尺寸图规划
- 保留真实商品主体的抠图与场景合成
- 中文卖点图和规格图排版
- 详情页模块与长图拼接
- 跨图片一致性质检
- 平台规格预检与分平台导出

不是所有工作都由一个生图模型完成。高保真生产应把商品主体、背景、阴影、文字、图标、规格参数分层处理。

## 目录

- SKILL.md：总控流程。
- references/：身份档案、图片规划、QA 和平台预检规范。
- templates/：可复制的商品资料、品牌配置和图片计划模板。
- scripts/：验证商品资料、拼接详情长图、生成质检联系表的辅助脚本。

## 在 Claude Code / Codex / Cursor 使用

### 方式 A：直接在技能仓库中工作

将 steamwo/skills 克隆到本地，在 Claude Code、Codex 或 Cursor 中打开仓库。告诉 Agent：

> 阅读 README.md 和 ecommerce-product-image-studio/SKILL.md，使用本套件处理我提供的 SKU 图片。不要修改或提交我的商品原图。

### 方式 B：复制到自己的项目

每个 Skill 是一个独立文件夹，里面有 SKILL.md。按工具支持的项目级目录复制：

- Claude Code：.claude/skills/<skill-name>/
- Codex：.agents/skills/<skill-name>/
- Cursor：.cursor/skills/<skill-name>/（请确认当前 Cursor 版本启用了 Agent Skills）

最少安装总控与本 SKU 需要的专项 Skill；推荐一次安装整套电商技能。不要把整套 Skills 复制到用户商品素材目录。

## 最小可用流程

1. 在自己的工作项目中建立 sku-001/input/，放入实拍图。
2. 复制 templates/product.example.json 为 sku-001/product.json，填写已确认的商品信息。
3. 复制 templates/brand.example.json 为 brand.json（可选）。
4. 在 Agent 中打开本套件并输入：

   > 使用 ecommerce-product-image-studio 处理 sku-001。先盘点照片、核对商品事实，生成图片计划和缺失素材清单。不要猜测木种、尺寸或售卖数量。先做白底主图和一张场景图样张；商品主体必须保留真实像素。通过 QA 后再继续整套图。

5. Agent 运行验证脚本：

~~~bash
python ecommerce-product-image-studio/scripts/validate_product.py --manifest sku-001/product.json --root sku-001
~~~

6. 详情页模块制作完成后，可按顺序拼接：

~~~bash
python ecommerce-product-image-studio/scripts/stitch_detail.py --width 750 --gap 0 --output sku-001/output/detail-long.png sku-001/output/modules/01-hero.png sku-001/output/modules/02-benefits.png sku-001/output/modules/03-scenes.png sku-001/output/modules/04-material.png sku-001/output/modules/05-specs.png
~~~

7. 生成视觉 QA 联系表：

~~~bash
python ecommerce-product-image-studio/scripts/contact_sheet.py --input-dir sku-001/output --output sku-001/qa/contact-sheet.jpg
~~~

辅助脚本需要 Pillow：

~~~bash
python -m pip install -r ecommerce-product-image-studio/requirements.txt
~~~

## 重要说明

- 本套件是 Agent 工作流与辅助脚本，不自带图像生成模型，不内置付费 API 密钥。
- Agent 必须使用你当前已经配置的图像工具、CLI 或 MCP；如果没有，先输出 Prompt 和待执行步骤，不得声称已生成。
- 单张照片不能证明未拍摄的侧面、背面、底面和内部结构。
- 产品身份锁、Prompt 和 AI 视觉检查都不能替代真实像素合成与人工核验。
- 淘宝、天猫、京东、拼多多的图片尺寸和规则需按当前类目/卖家后台核验；模板不会把未验证的数值写死。
- 不自动上传、不自动发布商品。
