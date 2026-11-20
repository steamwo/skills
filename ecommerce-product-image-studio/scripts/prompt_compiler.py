#!/usr/bin/env python3
"""Compile a structured ecommerce image job into a deterministic image prompt."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


ALLOWED_FIDELITY_MODES = {
    "REFERENCE_GENERATE",
    "REFERENCE_EDIT",
    "SOURCE_PRODUCT_PIXEL",
    "STRICT_PIXEL_COMPOSITE",
    "VERIFIED_CAD_3D",
    "CONCEPT_ONLY",
}

STANDARD_PRESERVE = [
    "preserve the exact product component count and visible proportions",
    "preserve all identity-critical hardware, joints, holes, supports, and edge profiles",
    "preserve every relation in CRITICAL GEOMETRY LOCK when present",
    "preserve verified real-world scale when a REAL-WORLD SCALE LOCK is present",
    "preserve the referenced material appearance and visible texture direction",
]

STANDARD_MUST_NOT = [
    "redesign the product",
    "add or remove product components",
    "relocate screws, hardware, holes, ports, or joints",
    "merge separate product components",
    "invent unseen product structure",
    "change the product into a cleaner or alternate design",
    "add unapproved accessories",
    "add marketing text, dimensions, logos, certifications, or unsupported claims",
]


def load_object(path: Path, label: str) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, dict):
        raise ValueError(f"{label} root must be an object")
    return data


def require_text(data: dict[str, Any], key: str, label: str) -> str:
    value = data.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label}.{key} must be a non-empty string")
    return value.strip()


def optional_text(data: dict[str, Any], key: str, label: str) -> str | None:
    value = data.get(key)
    if value is None:
        return None
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label}.{key} must be a non-empty string when present")
    return value.strip()


def string_list(value: Any, label: str, allow_empty: bool = True) -> list[str]:
    if value is None:
        return []
    if not isinstance(value, list) or not all(isinstance(x, str) and x.strip() for x in value):
        raise ValueError(f"{label} must be an array of non-empty strings")
    result = [x.strip() for x in value]
    if not allow_empty and not result:
        raise ValueError(f"{label} must not be empty")
    return result


def validate_job(job: dict[str, Any]) -> None:
    require_text(job, "asset_id", "job")
    mode = require_text(job, "fidelity_mode", "job")
    if mode not in ALLOWED_FIDELITY_MODES:
        raise ValueError(
            f"job.fidelity_mode must be one of {sorted(ALLOWED_FIDELITY_MODES)}"
        )
    require_text(job, "buyer_question", "job")
    require_text(job, "asset_role", "job")

    refs = string_list(job.get("reference_ids"), "job.reference_ids")
    if mode != "CONCEPT_ONLY" and not refs:
        raise ValueError(
            f"job.reference_ids must be non-empty for fidelity mode {mode}"
        )

    shot = job.get("shot")
    if not isinstance(shot, dict):
        raise ValueError("job.shot must be an object")
    for key in ("camera", "lighting", "composition"):
        require_text(shot, key, "job.shot")
    optional_text(shot, "environment", "job.shot")
    optional_text(shot, "product_occupancy", "job.shot")
    optional_text(shot, "person_action", "job.shot")
    string_list(shot.get("props"), "job.shot.props")

    string_list(job.get("hard_negatives"), "job.hard_negatives")
    string_list(job.get("repair_sentences"), "job.repair_sentences")


def validate_locks(locks: dict[str, Any], fidelity_mode: str) -> None:
    identity = string_list(
        locks.get("product_identity_lock"),
        "locks.product_identity_lock",
        allow_empty=False,
    )
    if not identity and fidelity_mode != "CONCEPT_ONLY":
        raise ValueError("product identity lock is required for factual SKU generation")

    for key in (
        "critical_geometry_lock",
        "real_world_scale_lock",
        "campaign_style_lock",
        "platform_style_lock",
    ):
        string_list(locks.get(key), f"locks.{key}")


def block(title: str, lines: list[str]) -> str:
    if not lines:
        return ""
    body = "
".join(f"- {line}" for line in lines)
    return f"{title}
{body}"


def compile_prompt(job: dict[str, Any], locks: dict[str, Any]) -> str:
    shot = job["shot"]
    sections: list[str] = []

    if job["fidelity_mode"] == "CONCEPT_ONLY":
        sections.append(
            "Create a concept-only ecommerce product visualization. "
            "Do not present it as a verified current SKU."
        )
    else:
        sections.append(
            "Use the exact current-SKU product shown in the supplied authoritative "
            "reference images. Keep it recognisably the same product."
        )

    ordered_locks = [
        ("PRODUCT IDENTITY LOCK", locks.get("product_identity_lock")),
        ("CRITICAL GEOMETRY LOCK", locks.get("critical_geometry_lock")),
        ("REAL-WORLD SCALE LOCK", locks.get("real_world_scale_lock")),
        ("CAMPAIGN STYLE LOCK", locks.get("campaign_style_lock")),
        ("PLATFORM COMMERCE STYLE LOCK", locks.get("platform_style_lock")),
    ]
    for title, value in ordered_locks:
        lines = string_list(value, f"locks.{title}")
        rendered = block(title, lines)
        if rendered:
            sections.append(rendered)

    sections.append(
        "ASSET JOB
"
        f"Buyer question: {job['buyer_question']}
"
        f"Image role: {job['asset_role']}
"
        f"Fidelity mode: {job['fidelity_mode']}"
    )

    shot_lines = [
        f"Camera: {shot['camera']}",
        f"Lighting: {shot['lighting']}",
        f"Composition: {shot['composition']}",
    ]
    for key, label in (
        ("environment", "Environment"),
        ("product_occupancy", "Product occupancy"),
        ("person_action", "Person action"),
    ):
        value = shot.get(key)
        if isinstance(value, str) and value.strip():
            shot_lines.append(f"{label}: {value.strip()}")
    props = string_list(shot.get("props"), "job.shot.props")
    if props:
        shot_lines.append("Supporting props: " + "; ".join(props))
    sections.append("SHOT
" + "
".join(shot_lines))

    preserve = STANDARD_PRESERVE + string_list(job.get("preserve"), "job.preserve")
    sections.append(block("PRESERVE", preserve))

    must_not = (
        STANDARD_MUST_NOT
        + string_list(job.get("hard_negatives"), "job.hard_negatives")
    )
    sections.append(block("MUST NOT", must_not))

    repairs = string_list(job.get("repair_sentences"), "job.repair_sentences")
    if repairs:
        sections.append(block("TARGETED REPAIR — CHANGE ONLY THESE FAILED POINTS", repairs))
        sections.append(
            "PRESERVE APPROVED CONTENT
"
            "- preserve every other approved product detail, material, camera, lighting, "
            "composition, and background unless a repair sentence explicitly changes it"
        )

    sections.append(
        "OUTPUT INTENT
"
        "- commercial ecommerce photography
"
        "- no final infographic typography unless explicitly required by this asset job
"
        "- product truth has priority over visual beautification"
    )

    return "

".join(section for section in sections if section.strip()).strip() + "
"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Compile structured ecommerce prompt inputs into a deterministic prompt."
    )
    parser.add_argument("--job", type=Path, required=True)
    parser.add_argument("--locks", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    parser.add_argument(
        "--json-output",
        type=Path,
        help="Optional machine-readable compiled request manifest.",
    )
    args = parser.parse_args()

    try:
        job = load_object(args.job, "job")
        locks = load_object(args.locks, "locks")
        validate_job(job)
        validate_locks(locks, job["fidelity_mode"])
        prompt = compile_prompt(job, locks)

        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(prompt, encoding="utf-8")
        else:
            sys.stdout.write(prompt)

        if args.json_output:
            payload = {
                "schema_version": 1,
                "asset_id": job["asset_id"],
                "fidelity_mode": job["fidelity_mode"],
                "reference_ids": job.get("reference_ids", []),
                "prompt": prompt,
                "source_job": str(args.job),
                "source_locks": str(args.locks),
            }
            args.json_output.parent.mkdir(parents=True, exist_ok=True)
            args.json_output.write_text(
                json.dumps(payload, ensure_ascii=False, indent=2),
                encoding="utf-8",
            )
        return 0
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    raise SystemExit(main())
