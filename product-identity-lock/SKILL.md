---
name: product-identity-lock
description: 从用户确认的商品资料与实拍图建立 SKU 产品身份档案，锁定外形、比例、部件、材质、颜色和关键细节，防止 AI 生图改款；物理尺寸由 product-dimension-lock 独立管理。
---

# Product Identity Lock

## 目标

为每个 SKU 建立可追溯的视觉身份契约。后续任何主图、场景图、卖点图和详情图都必须遵守此契约。物理尺寸、测量口径和公差由 product-dimension-lock 管理；本 Skill 不从图片估算尺寸。

## 建档流程

1. 读取 product-reference-audit 的审查结果。
2. 选择当前 SKU 的权威实拍参考图；标注图像路径与视角。
3. 记录可见几何特征：轮廓、长宽高视觉比例、部件数量、相对位置、孔位、连接、缝线、五金、边缘和倒角。
4. 记录材质特征：颜色、纹理方向、天然瑕疵、表面光泽、加工/涂层状态。
5. 将每个字段关联到具体照片或用户确认内容。
6. 把不确定项保留为 unknown，不允许模型根据常识补齐。
7. 定义锁定区、可编辑区和需要用户授权的条件编辑区。
8. 将产品尺寸/重量/包装规格交给 product-dimension-lock，不在身份档案中重复猜测。

## 锁定策略

- 锁定区：商品本体身份关键区域，优先使用源图 RGB 像素，不做生成式重绘。
- 可编辑区：背景、留白、非商品道具、文字、图标和装饰。
- 条件编辑区：只有用户明确授权后才可修改；必须记录修改范围并保留原始版本。

## 每个 SKU 必须锁定

- 轮廓、可见比例、部件数量和结构关系。
- 颜色与真实材质纹理。
- 孔位、接缝、榫卯、螺丝、铰链、商标和标识。
- 真实瑕疵与自然差异（不能擅自磨平或复制）。
- 参考图覆盖的视角，以及未被照片证明的视角。
- 与 product-dimension-lock 关联的尺寸档案 ID/路径。

## 输出

生成 product-identity.json，至少包含：
- sku、reference_images、geometry、material、surface_finish。
- must_preserve、must_not_invent、editable_regions。
- evidence、unknowns、conflicts、approved_edits。
- dimension_profile_ref（关联 product-dimensions.json）。
- 创建日期、版本号和源文件哈希（如可获得）。

## 后续检查

每张成品必须与身份档案及权威参考图逐项比较。身份关键特征无法确认时，暂停该图并请求补拍/确认。不能以“整体看起来相似”作为通过标准。