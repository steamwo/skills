# Agent working instructions

This repository is a wood-product image production starter. The user sells unpainted natural-wood home products on Chinese ecommerce marketplaces.

1. Read `.agents/skills/wood-product-fidelity/SKILL.md` before image-related tasks.
2. Never regenerate or hallucinate product wood grain, joints, knots, openings, geometry, back side or finishing.
3. Use the original RGB product pixels and the alpha mask from background removal.
4. The first working command is `python generate.py --input input/product.jpg --output output`.
5. If the photo is missing, ask the user to upload it; do not invent a stock product.
6. Images are drafts pending manual product-accuracy and marketplace checks.
7. No paid or third-party image generation requests without explicit user setup and approval.
