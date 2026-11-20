# Evidence-Bound Copy Guard Contract

## Purpose

Prevent weak models and image models from expanding a small set of product facts into unsupported marketing, safety, environmental, health, or performance claims.

Copy is a **rendered view of approved facts**, not a source of new facts.

## Copy sources

Every final copy item MUST trace to one or more approved source facts with evidence state:

- `user_confirmed`
- `document_verified`
- `visible_in_reference` when the wording only describes visible appearance/structure
- `estimated` only when explicitly marked as estimated and appropriate
- `unknown` MUST NOT be promoted into copy
- `conflicting` MUST NOT be promoted into copy

## Claim scope

Each copy item SHOULD record:
- `copy_id`
- exact `text`
- `source_fact_ids`
- `evidence_state`
- `scope` (family / variant / bundle / market)
- `copy_type` (title / subtitle / badge / label / dimension)
- `status` (DRAFT / APPROVED / BLOCKED)

## No semantic expansion

The model MUST NOT turn a verified fact into a stronger adjacent claim.

Examples:

```text
"unpainted"                  != "0 VOC"
"natural wood grain"         != "eco certified"
"anti-slip pad is visible"   != "never slips"
"triangular base"            != "safe for all users"
"four lengths available"     != "fits every body type"
"solid connection is visible"!= "supports 200 kg"
```

If the user supplied wording such as “环保无漆”, it may be retained as a user-confirmed claim with that exact scope, but MUST NOT be expanded to “0甲醛”, “0 VOC”, “无有害物质”, certification, or health/safety claims without evidence.

## Copy deck first

Before final infographic/layout generation, create an approved copy deck.

The image model MUST NOT invent final marketing copy.

For exact/repeated Chinese, numbers, units, punctuation, SKU labels, and dimensions:
- render deterministically in a design/layout tool;
- do not rely on stochastic image-model typography.

## Weak-model mode

When model capability is uncertain:

1. provide only the approved fact table;
2. require copy selection/transformation from those facts;
3. forbid introducing nouns, numbers, certifications, outcomes, or safety/performance statements absent from the fact table;
4. compare final text against the approved copy deck before delivery.

Prefer concise factual labels over persuasive invention.

## Forbidden-by-default categories

Unless separately verified, block:
- load capacity;
- safety guarantees;
- injury prevention;
- ergonomic/medical claims;
- posture correction;
- muscle gain / fat loss / performance outcomes;
- “zero formaldehyde”, “zero VOC”, “non-toxic”;
- material species;
- environmental certification;
- food grade / child safe;
- compatibility claims;
- bundle quantity / included items;
- discounts / scarcity / best-seller claims.

## QA

`FAIL` if:
- copy contains a fact not in the approved evidence set;
- a number/unit differs from the verified value;
- user wording was strengthened into a stronger unsupported claim;
- image-model text differs materially from approved exact copy.

When text repeatedly fails, stop regenerating the whole image and move typography to deterministic layout.
