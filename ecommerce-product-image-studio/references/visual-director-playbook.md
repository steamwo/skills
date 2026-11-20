# Visual Director Playbook

## Purpose

Give a weaker controller model a few strong patterns to imitate when directing a capable image model.

These are **visual examples**, not rigid templates.

The controller should write concise prompts that:
- anchor to the real reference product;
- name the few critical details that must survive;
- describe the commercial image naturally;
- avoid unsupported copy;
- leave photography decisions to the image model where possible.

---

## Pattern 1 — Clean hero

### When to use
Main product image / recognition.

### Prompt pattern

```text
Use the exact product shown in the reference images as the only product prototype.

Keep the product structure unchanged:
- {critical detail 1}
- {critical detail 2}
- {critical detail 3}

Create a premium ecommerce studio photograph on a clean {background}.
Show {quantity/composition} from a {camera angle}.
Use {lighting} with realistic contact shadows.
Keep the product large, sharp, and easy to understand at thumbnail size.

No text, no extra accessories, no alternate product design.
```

### Wooden push-up support example

```text
Use the exact wooden push-up supports shown in the reference images as the only product prototype.

Keep the cylindrical wooden handle, the two separate triangular wooden bases, natural light wood grain, black anti-slip pads, and the real handle-to-base connection unchanged. The recessed metal screws sit on the top surface of the handle near each end, with the screw axis approximately vertical to the floor; do not move them into the circular end-grain face.

Create a premium clean ecommerce studio photograph on pure white. Show the pair in a natural staggered three-quarter composition, with soft large-area side light and realistic contact shadows. Keep the product large and visually clear.

No text, no props, no redesign.
```

---

## Pattern 2 — Construction detail

### When to use
Joint / screw / port / material detail.

### Prompt pattern

```text
Use the supplied product reference as the factual source.

Create a close commercial detail photograph of {detail area}.
The image should clearly show:
- {verified relation}
- {verified hardware location}
- {verified material detail}

Keep the surrounding geometry exactly consistent with the reference.
Use a close three-quarter camera angle and soft directional light so the construction is easy to read.

Do not simplify, relocate, merge, or redesign the visible parts.
No text.
```

### Wooden push-up support example

```text
Use the supplied wooden push-up support reference as the factual source.

Create a close commercial detail photograph of one handle-to-base connection. Clearly show the cylindrical handle resting above the triangular base, the visible circular end grain, and the recessed metal screw on the top surface of the handle near the end. The screw axis is approximately vertical to the floor and the screw must not appear in the center of the end-grain face.

Keep the surrounding wood geometry and natural grain consistent with the reference. Use a close three-quarter angle and soft side light.

No redesign, no extra hardware, no text.
```

---

## Pattern 3 — Lifestyle / person-use

### When to use
Show use context and desirability.

### Prompt pattern

```text
Use the exact referenced product and keep its visible construction unchanged.

Show {person} using it for {realistic action} in {environment}.
The interaction must be physically believable: {contact details}.
Use a {camera angle} that keeps both the product and the action easy to read.
Lighting should feel {lighting mood}.

The product remains a clear commercial hero.
Use only a few relevant supporting props.
No text, no extra product units, no invented accessories.
```

### Wooden push-up support example

```text
Use the exact referenced wooden push-up supports and keep their construction unchanged, including the handle-to-base connection and screw placement.

Show an adult athlete using the pair for an elevated push-up in a bright modern home-training corner. Both hands grip the wooden handles naturally and both products sit flat on the floor at the same believable scale. Use a low three-quarter camera angle near floor level, soft window daylight, and realistic contact shadows.

Keep the product clearly visible. Only a yoga mat and towel may appear as supporting props.

No text, no extra bars, no alternate handle design.
```

---

## Pattern 4 — Variant / size image

### When to use
Help the buyer choose among verified size variants.

### Prompt pattern

```text
Use the exact referenced product family.

Show the verified variants together using one consistent camera and scale basis.
Only the confirmed variant axis should visibly change: {variant axis and values}.
Keep all shared construction details visually consistent.

Use a clean ecommerce studio composition with enough whitespace for later labels.
Do not invent unverified differences in width, height, hardware, color, or included items.
No text unless exact labels are explicitly requested and will be checked.
```

---

## Pattern 5 — Six-grid planning

Do not begin with “make a beautiful six-grid”.

First choose six distinct buyer questions.

Example for a wooden fitness product:

| Cell | Buyer question | Visual | Copy |
|---|---|---|---|
| 1 | What is it? | clean hero | 原木俯卧撑支架 |
| 2 | Which size? | four verified variants | 四种长度可选 / 20 · 25 · 30 · 40 cm |
| 3 | What does the material look like? | real wood close-up | 原生木材纹理 |
| 4 | How is it built? | joint / screw close-up | 连接结构细节 |
| 5 | What touches the floor? | bottom / pad detail | 底部防滑脚垫 |
| 6 | How is it used? | lifestyle image | 居家训练场景 |

If the user explicitly confirmed `环保无漆`, it may be used as copy.
Do not expand it into `0甲醛`, `0 VOC`, `无毒`, or certification claims.

For final assembly:
- reuse the approved images;
- keep copy short;
- use consistent spacing / typography / background family;
- do not ask the image model to redesign the product just to create the grid.

---

## Prompt quality check

Before sending a prompt, ask:

1. Did I clearly anchor to the real reference product?
2. Did I name the 3–7 details most likely to drift?
3. Is the commercial shot easy to imagine?
4. Did I avoid irrelevant facts and giant negative lists?
5. Did I leave enough freedom for the image model to make a strong photograph?

If yes, send the prompt.
