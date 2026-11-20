---
name: ecommerce-product-image-studio
description: Create commercially strong ecommerce product images from real SKU references with a lightweight workflow: understand the product, protect critical details, direct the image model with short visual prompts, write evidence-based copy, plan multi-image sets, and run simple visual QA.
---

# Ecommerce Product Image Studio

## Objective

Produce **commercially strong, same-SKU ecommerce images** without turning the workflow into a large agent system.

This skill is the main controller. Do not require other skills unless the user explicitly needs a specialized workflow.

Priority:
1. product must still be the same SKU;
2. critical visible construction must be correct;
3. facts and copy must be truthful;
4. the image should sell the product well;
5. the set should feel visually coherent.

## Core idea

Use the controller model as a **visual director**, not as a rules engine.

The controller should:
- inspect the real product references;
- understand what visually defines the SKU;
- decide what each image should communicate;
- write a short, natural image prompt;
- check the result;
- repair only the failed detail.

Do not force the controller to produce large schemas, long state-machine records, or compiler-ready prompt fragments.

## Step 1 — Make a short product brief

Study all authoritative product photos.

Create a compact internal brief with only:

### Product
- what the product is;
- visible components;
- visible material / finish;
- important proportions;
- visible hardware / joints.

### Critical details
List only the details that would make the generated product visibly wrong if changed.

Write them as simple spatial facts when useful.

Example:

```text
- cylindrical handle sits horizontally above two triangular wooden bases
- handle and bases remain visibly separate parts
- recessed metal screw is on the TOP surface of the handle near each end
- screw axis is approximately vertical to the floor
- screw is NOT in the circular end-grain face
- black anti-slip pads remain under the bases
```

### Confirmed facts
Only user-confirmed or document-supported facts such as:
- sizes;
- finish;
- included items;
- material name;
- claims.

### Do not invent
Keep a short list of unknown or risky claims.

Examples:
- load capacity;
- certifications;
- wood species;
- 0 VOC / zero formaldehyde;
- medical / ergonomic benefits;
- safety guarantees;
- training outcomes.

The brief should be short enough to stay visually useful.

## Step 2 — Plan the image set

Plan images by buyer question, not by fixed image count.

Typical jobs:
- hero — what is this?
- feature/detail — why is this construction/material worth noticing?
- variant/size — which option should I choose?
- lifestyle — how is it used?
- infographic/grid — what are the main purchase reasons at a glance?

For a multi-image set, avoid near-duplicate shots.

For a six-grid, a useful starting structure is:

1. hero / product recognition;
2. size or variant choice;
3. material / finish;
4. construction / joint;
5. functional visible detail;
6. lifestyle / usage.

Adjust to the actual product.

## Step 3 — Write natural image prompts

Read `references/visual-director-playbook.md`.

Prompts should be **short, visual, and specific**.

Preferred structure:

```text
Use the exact product shown in the reference images as the only product prototype.

Keep:
{3–7 most important product details}

Create:
{commercial shot / scene / composition}

Lighting:
{simple lighting direction}

Do not:
{the few likely failure modes}
```

Do not turn every prompt into a large specification document.

Do not repeat every known fact if it does not affect the visible image.

## Step 4 — Generate one visual job at a time

For important hero / lifestyle images, generate 1–3 candidates when useful.

Keep the product brief stable.

Vary only what helps:
- camera;
- scene;
- light;
- person action;
- composition.

For identity-critical close-ups, prefer the reference view that best proves the detail.

If a real crop already shows the detail well, use it rather than asking the image model to reinvent it.

## Step 5 — Simple visual QA

After generation, compare directly against the authoritative references.

Check only:

### Product identity
- same silhouette / component count;
- same important proportions;
- same visible material appearance.

### Critical details
- hardware is in the correct place;
- joint / support relationship is correct;
- holes / ports / fasteners did not move;
- separate parts did not merge.

### Scene
- product scale is believable;
- person contact is plausible;
- props do not imply included accessories.

### Copy
- numbers / units are correct;
- no unsupported claims appeared;
- Chinese text is readable when text is part of the generated image.

Any obvious critical-detail error = reject that image.

## Step 6 — Repair only the failed point

Use one short repair instruction.

Example:

```text
Keep the entire approved image unchanged except the screw placement:
move the visible screw to the top surface of the cylindrical handle near the end;
the screw axis is vertical to the floor;
do not place the screw in the circular end-grain face.
```

If the same identity-critical detail fails twice:
- use a better reference view;
- switch to edit mode / source crop;
- or avoid using a generated close-up as factual proof.

Do not keep making the prompt longer.

## Step 7 — Copy and six-grid

This skill owns the copy and grid planning. A separate copy/layout skill is not required.

Write copy from confirmed facts and visible product evidence.

Good ecommerce copy is usually:
- short;
- concrete;
- easy to scan;
- specific to one panel.

For Chinese six-grid images:
- title: usually 4–10 Chinese characters;
- subtitle: optional, usually one short line;
- use verified dimensions exactly;
- do not invent stronger claims to make the layout feel fuller.

Example:
- `原生木材纹理`
- `环保无漆` only when user-confirmed
- `四种长度可选`
- `20 / 25 / 30 / 40 cm`
- `连接结构细节`
- `底部防滑脚垫`
- `居家训练场景`

For final six-grid assembly:
- prefer any native design/compositing capability already available in the environment;
- use approved product images as the visual sources;
- do not require Python, Node, or a particular design application;
- if exact text is important, prefer a deterministic/native text layer over asking the image model to redraw the product and typography together.

If only image generation is available, a generated six-grid may be used as a visual concept, but exact factual copy and identity-critical details must still be checked carefully.

## Few-shot principle

For weaker controller models, examples are more useful than extra contracts.

Imitate the prompt patterns in `references/visual-director-playbook.md`:
- preserve the actual SKU;
- name only the critical product details;
- describe the desired commercial image naturally;
- keep negatives short;
- let the image model handle photography.

## Failure conditions

Reject when:
- the product is visibly another SKU;
- a critical hardware / joint / connection detail is wrong;
- a verified size or fact is wrong;
- unsupported customer-facing claims appear;
- a person interacts with the product implausibly.

Do not reject merely because source pixels differ when the product is still clearly the same SKU.

## Core principle

**Give the image model a good visual brief, not a legal contract.**

Protect the few details that define the real product, then leave enough freedom for the image model to create strong commercial photography.
