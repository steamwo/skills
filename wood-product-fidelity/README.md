# wood-product-fidelity｜原木电商产品图 Skill

这是 `steamwo/skills` 中的一个可复用 Agent Skill，供 Claude Code、Codex、Cursor 使用。它不是独立电商软件。

## 目标不是只抠图

本 Skill 的主题是**电商产品图生产**：围绕真实无漆原木商品，规划和制作主图、辅图/卖点图、场景图、木纹与结构细节图、规格图、详情页分屏和详情长图。

产品保真是贯穿所有图片的底线：商品本体尽量使用真实照片像素，AI 主要负责空场景、背景、装饰、视觉策划和排版。不能为了凑齐图片数量而虚构看不到的结构或参数。

## 使用方法

1. 把 `wood-product-fidelity` 文件夹作为 Skill 提供给 Agent，或在打开的 `steamwo/skills` 工作区中让 Agent 读取 `wood-product-fidelity/SKILL.md`。
2. 将真实商品照片放在工作目录，例如 `product.jpg`；如有，准备侧面、背面、木纹微距和尺寸资料。
3. 对 Agent 说：

   > 使用 wood-product-fidelity Skill，为 product.jpg 规划一套电商产品图。先列出主图、辅图、场景图、细节图、规格图和详情页分屏的内容及所需素材。先生成一张白底主图样张和一张场景图样张，保留真实木纹、天然色差和连接结构，不许重绘产品。列出缺失资料与质检问题。

4. Agent 应先展示图片策划，再运行基础脚本和已配置的图像生成能力；查看 `qa-report.json`，并把需要人工检查的地方告诉你。

## 基础处理（不经过 Agent）

Python 3.11 或更高（若 rembg 当前版本不支持你安装的 Python 版本，请改用 Python 3.11–3.13）：

```bash
python -m pip install -r wood-product-fidelity/requirements.txt
python wood-product-fidelity/scripts/render.py --input product.jpg --output output/test
```

若已有**不含商品的空场景背景**：

```bash
python wood-product-fidelity/scripts/render.py --input product.jpg --background room.png --output output/test
```

这会额外生成 `03-scene.png`。本 Skill **不包含自动 AI 场景生图 API**；背景可由 Agent 已连接的图像生成能力制作，必须要求 AI 只绘制背景，不重绘商品。

## 当前脚本能做什么

| 输出 | 内容 |
|---|---|
| `product-cutout.png` | 真实 RGB 像素 + Alpha 透明通道 |
| `mask.png` | 抠图 Mask（一定人工检查） |
| `01-white.png` | 白底商品图预览 |
| `02-neutral.png` | 中性背景商品图预览 |
| `03-scene.png` | 可选：实物与空场景合成 |
| `qa-report.json` | 像素合成检查及复核说明 |

**重要：这些是电商套图工作流的基础组件，不是完整的一键详情页生成器。** 当前脚本尚未自动产出整套卖点图、尺寸图、详情分屏与各平台导出。Agent 应先基于商品真实资料策划这些图片，再逐项制作。

## 一套电商产品图通常要规划什么

根据具体商品和平台要求决定，不机械套固定张数：

- 主图：清晰展示真实商品。
- 辅图/卖点图：用真实商品图配合准确卖点。
- 场景图：真实商品合成到匹配的家居场景。
- 细节图：木纹、端面、连接、孔位、倒角等真实细节。
- 规格图：使用已确认的尺寸、数量和包装信息。
- 详情页：按真实卖点组织分屏，最后拼成长图。
- 平台导出：分别检查淘宝、天猫、京东、拼多多的当前类目与槽位要求。

## 重要限制

- 一张照片不能恢复实物背面、底面或隐蔽榫卯。
- 自动抠图会漏掉原木镂空、细杆和边缘，必须审图。
- 自动裁切放大不能创造原图不存在的木纹细节。
- 首次运行 `rembg` 可能下载模型并需要网络；请核对模型权重的使用授权。
- 不要将 API 密钥、私有商品素材或生成结果提交到公开仓库。

更完整规则参见 [SKILL.md](./SKILL.md) 和 [wood-rules.md](./references/wood-rules.md)。
