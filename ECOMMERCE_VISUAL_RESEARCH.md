# E-commerce Visual Skill Research Notes

This document records external design patterns studied for this repository.

The goal is **conceptual learning**, not copying vendor-specific APIs or model names.

## Reviewed repositories

### xianyu110/ecommerce-image-skills

Reviewed snapshot:
- repository: https://github.com/xianyu110/ecommerce-image-skills
- main tree reviewed: \`f4566fdc812584425728862ad8e08c90883d81ee\`

Useful patterns adopted:
- concise PRODUCT IDENTITY LOCK reused verbatim across prompts;
- campaign-wide style lock;
- real product reference image passed directly into capable image tools;
- scene libraries / shot routing;
- one purpose per ecommerce visual;
- platform-oriented gallery planning;
- regenerate only failed assets;
- deterministic scripts for exact crop / size / checks.

Important adaptation:
- this repository does not hard-code another project's model names or gateway;
- marketplace dimensions remain subject to current verification;
- product identity is separated from exact pixel identity.

### dlazy-ai/ecommerce-skills

Reviewed snapshot:
- repository: https://github.com/dlazy-ai/ecommerce-skills
- main tree reviewed: \`a938b76511dc2021e1e924195a09120ede47c696\`

Useful patterns adopted:
- ecommerce production as a composable pipeline, not a prompt pack;
- stable product-fidelity paragraph + stable atmosphere/style paragraph + variable shot paragraph;
- brand configuration sections injected only into relevant skills;
- one-image-to-many asset planning;
- detail modules generated independently;
- thumbnail readability as a real conversion constraint;
- bounded multi-candidate generation;
- generation → QC → targeted prompt repair → rerun;
- deterministic batching / resume / compliance logic kept outside free-form reasoning.

Important adaptation:
- use buyer-decision and evidence contracts already present in this repository;
- retain SKU/variant matrices and asset derivation graph;
- keep official platform compliance separate from platform style heuristics.

## Other current ecosystem signals

Additional public ecommerce-image skills were reviewed to confirm the broader pattern:
- real product reference → hero / feature / lifestyle / size / in-box asset families;
- multiple image-model backends;
- reference-first product photography;
- platform-specific output families.

These confirm that the useful abstraction is a **commercial visual production workflow**, not a single universal prompt.

## Principles resulting from the research

1. Reference-image generation first for most consumer products.
2. Strict cutout compositing only when exact pixels are actually required.
3. Stable identity + campaign + platform style locks.
4. Different shot grammar for different buyer questions.
5. Platform style changes asset mix and hierarchy, not product truth.
6. Generate candidates for important assets; do not trust the first random result.
7. QA must produce actionable repair instructions.
8. Retry only failed assets.
9. Detail pages are semantic modules first, long images second.
10. Deterministic checks belong in code / schemas whenever possible.