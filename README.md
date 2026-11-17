# 原木无漆电商出图 · 点击运行版

这是给 **淘宝 / 天猫 / 京东 / 拼多多原木无漆产品**准备的第一版高保真图片生产工具。

**你不用先学 Python，也不用先配置 AI 图片 API。** 把真实商品照片上传到仓库，然后在 GitHub Actions 点击运行，就会得到：
- `01_白底主图.jpg`
- `02_暖色展示图.jpg`
- `04_详情长图.jpg`（750px 宽，测试模板）
- `透明产品_裁切.png`、`原始比例_透明产品.png`
- `质检说明.json`（**必须人工核验**）

> 当前第一版做的是 **真实产品抠图 + 保真排版/合成**，不是整张 AI 重绘，也不假装已经接入 AI 室内场景生成。这样的顺序可以先解决原木纹理和构造丢失的问题。如果你已有 AI 生成的空场景背景，可选上传为 `input/background.jpg`，同样点击运行就会增加场景合成图。

## 第一次使用（全程网页操作）

**第 1 步：上传照片**

1. 打开 [input 文件夹](./input)，点击右上角 `Add file` → `Upload files`。
2. 选一张清晰的**实物照片**（背景尽量干净、商品没有被裁切），**在自己电脑上重命名为 `product.jpg`** 后上传。
3. 页面底部点击 `Commit changes` 保存。文件在 GitHub 应显示为 `input/product.jpg`。

注意：本仓库目前是私有仓库，但在任何时候都不要提交 API 密钥。若以后设为公开仓库，上传的商品原图也可能公开。

**第 2 步：点击运行**

1. 打开 [GitHub Actions：原木商品出图](https://github.com/steamwo/skills/actions/workflows/render.yml)。
2. 点左侧 `原木商品出图`，然后点击 `Run workflow` → 绿色 `Run workflow`。
3. 点击刚出现的运行记录；绿色对勾代表完成。若失败，展开红色步骤看报错。

**第 3 步：下载**

1. 打开成功运行记录，向下找到 `Artifacts`。
2. 下载 `wood-product-images` ZIP。
3. 解压，检查白底图、展示图、详情长图和 `质检说明.json`。
4. **人工核对孔位、木纹、榫卯、板材边缘、自然色差后再考虑上架**。这版不代替平台尺寸与合规审核。

## 可选：让 AI 生成室内背景

你可先用 Claude/Codex/Cursor 配套的图片生成工具做一张**没有商品本体**的室内背景，另存为 `input/background.jpg` 再运行。脚本只把实物商品照片抠出后贴进背景，不会要求 AI 重新绘制木纹。**必须确认原拍摄角度与背景透视一致**，否则效果会不自然。

推荐背景提示词：

> Minimal warm neutral living room interior, soft natural daylight, clean empty center space reserved for a real wooden household product, realistic floor perspective, no wooden shelf or wooden product, no text, no brand logos.

## 本地使用（Claude Code / Codex / Cursor）

在电脑上安装 Python **3.11–3.13**，把仓库克隆下来，执行：

```bash
git clone https://github.com/steamwo/skills.git
cd skills
python -m pip install -r requirements.txt
python generate.py --input input/product.jpg --output output
```

在 Codex / Claude Code / Cursor 中打开这个项目后，直接输入：

> 阅读本项目 README 和 wood-product-fidelity Skill。先检查 input/product.jpg 是否存在。不要重绘商品，运行 python generate.py，在 output 检查照片、透明产品、详情图和质检报告，指出需要人工修改的地方。

Skill 文件在 [`.agents/skills/wood-product-fidelity/SKILL.md`](./.agents/skills/wood-product-fidelity/SKILL.md)；`AGENTS.md` 也包含使用约束。

## 常见问题

- **Actions 没有 Run workflow：** 确保你正在仓库的默认分支 `main`，且 GitHub Actions 已启用。
- **提示找不到照片：** 确认上传后路径严格为 `input/product.jpg`，不是 `product.jpg`、`input/product.jpg.jpg`。
- **图片抠图失败：** 尝试背景干净、光照均匀、商品完整的原图。木质镂空部件应手工核验。
- **模型下载：** 第一次运行 rembg 会下载抠图模型。由于下载或 GitHub Actions 权限/额度限制，运行可能失败。
- **图片不好看：** 先检查自动抠图结果。暂时不要通过 AI 重绘木纹来“修复”产品结构。
- **这算 AI 生图吗？** 第一版用 AI 抠图模型，不使用生成式图片 API。第二阶段才接入自动生成空场景，保持商品像素锁定。

## 工作边界

单张照片不能准确推断背面和侧面；详情长图的裁切是自动预览，不保证正好显示有价值的木纹；四个平台的上架尺寸、类目规则需要根据卖家后台独立核验。本工具不是自动上架服务。

底层抠图：[rembg](https://github.com/danielgatis/rembg)；合成和排版：Pillow。
