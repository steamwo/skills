# E-commerce Product Image Studio

A lightweight visual-director skill for producing same-SKU ecommerce images from real product references.

## Why this version is intentionally simple

The controller model does not need to run a large state machine.

The practical workflow is:

```text
real product photos
→ short product brief
→ identify 3–7 critical visible details
→ plan a small set of buyer-focused images
→ write short natural visual prompts
→ generate
→ compare against references
→ repair only failed details
→ write concise evidence-based copy
→ assemble the final grid with whatever native layout capability is available
```

The image model does the photography.
The controller provides visual direction and protects product truth.

## No required runtime

Core use requires:
- no Python;
- no Node;
- no prompt compiler;
- no mandatory JSON pipeline;
- no mandatory sub-skill chain.

Existing scripts and specialized skills in the repository remain optional utilities for users who need them.

## What the controller should preserve

Focus on the small number of visible details that define the SKU:
- component count;
- proportions;
- joints;
- screws / fasteners;
- holes / ports;
- handle / support relationships;
- material appearance;
- variant-specific geometry.

Do not bury these in a huge checklist.

## Prompt style

Use short visual prompts.

Example pattern:

```text
Use the exact product shown in the reference images as the only product prototype.

Keep:
- exact handle and base geometry
- screw on the top surface of the handle near each end
- visible natural wood grain
- black anti-slip pads

Create a premium clean ecommerce studio shot on white,
three-quarter camera angle, soft side light, realistic contact shadow,
product large and clear in frame.

No text, no extra accessories, no redesign.
```

See `references/visual-director-playbook.md` for more patterns.

## Six-grid / infographic

The same main skill plans:
- six visual jobs;
- short copy;
- image order;
- hierarchy.

Use the environment's available native layout/design capability for final assembly.

Exact text/layout does not require a Python implementation.

## QA

Check only what matters:
1. same SKU;
2. critical visible details;
3. factual sizes/copy;
4. believable use/contact.

When one detail fails, repair that detail only.

## Design principle

**Minimal guardrails + strong visual examples > a large orchestration framework for this use case.**
