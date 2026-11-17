# wood-product-fidelity（原木电商商品保真 Skill）

供 Claude Code、Codex、Cursor 使用的**单个 Skill**，不是单独的项目应用。

它的任务是保留真实无漆原木制品的木纹与结构，使用原照片产品层合成白底或室内场景背景。脚本是该 Skill 的辅助工具。

## 使用方法（最容易）

1. 把 `wood-product-fidelity` 文件夹作为 Skill 提供给你的 Agent，或在打开的代码工作区中让 Agent 读取它的 `SKILL.md`。
2. 将一张真实照片放进工作目录，例如 `product.jpg`。
3. 对 Agent 说：

   > 使用 wood-product-fidelity Skill 处理 product.jpg。先生成一张白底主图和一张中性色展示图，保留真实木纹、天然色差、连接结构，不许重绘产品。检查抠图并提供质量报告。

4. Agent 应安装依赖，运行脚本，查看 `qa-report.json` 并把需要人工检查的地方告诉你。

## 不经过 Agent 也能测试（在仓库根目录执行）

Python 3.11 或更高（若 rembg 当前版本不支持你安装的 Python 版本，请改用 Python 3.11–3.13）：

```bash
python -m pip install -r wood-product-fidelity/requirements.txt
python wood-product-fidelity/scripts/render.py --input product.jpg --output output/test
```

若已有**不含商品的空场景背景**：

```bash
python wood-product-fidelity/scripts/render.py --input product.jpg --background room.png --output output/test
```

这样会额外生成 `03-scene.png`。本 Skill **不包含自动 AI 场景生图 API**；背景可由 Agent 已连接的图像生成能力制作，切记让 AI 只绘制背景，不重绘产品。

## 输出文件

| 文件 | 内容 |
|---|---|
| `product-cutout.png` | 真实 RGB 像素 + Alpha 透明通道 |
| `mask.png` | 抠图 Mask（一定人工检查） |
| `01-white.png` | 白底商品图预览 |
| `02-neutral.png` | 中性背景商品图预览 |
| `03-scene.png` | 可选：实物与空场景合成 |
| `qa-report.json` | 全不透明区域像素检查及复核说明 |

每张图默认是 1200 × 1200 PNG（可选场景也输出 1200 × 1200），不等于四个平台当前类目要求。

## 重要限制

- 一张照片不能恢复实物的背面、底面或隐蔽榫卯。
- 自动抠图会漏掉一些原木镂空、纹理和透明边缘，**一定要审图**。
- 若需要整套详情长图，需要后续在 Agent 中基于真实照片逐模块排版；本版本不伪称能一键产出完整商业详情页。
- 首次运行 `rembg` 可能下载模型并需要网络；请核对模型权重的使用授权。
- 仓库中的代码与文字不应包含 API 密钥或私有商品素材。

更完整规则参见 [SKILL.md](./SKILL.md)。
