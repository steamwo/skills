#!/usr/bin/env python3
"""Validate ecommerce-product-image-studio task-input.json against task-input-schema.json."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


SOURCE_ALIASES = {
    "user_explicit_only": {"user_explicit"},
    "user_explicit_or_verified_document": {"user_explicit", "verified_document"},
    "uploaded_attachment": {"uploaded_attachment"},
}


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def option_keys(field: dict[str, Any]) -> set[str]:
    return {
        item["key"]
        for item in field.get("options", [])
        if isinstance(item, dict) and isinstance(item.get("key"), str)
    }


def validate_value(field: dict[str, Any], value: Any, errors: list[str]) -> None:
    key = field["key"]
    field_type = field.get("type")

    if field_type in {"text", "textarea"}:
        if not isinstance(value, str):
            errors.append(f"{key}: expected string.")
            return
        max_len = field.get("maxLength")
        if isinstance(max_len, int) and len(value) > max_len:
            errors.append(f"{key}: exceeds maxLength={max_len}.")

    elif field_type == "file_upload":
        if not isinstance(value, list) or not all(isinstance(x, str) and x for x in value):
            errors.append(f"{key}: expected non-empty string file paths in an array.")
            return
        max_count = field.get("maxCount")
        if isinstance(max_count, int) and len(value) > max_count:
            errors.append(f"{key}: exceeds maxCount={max_count}.")

    elif field_type in {"select", "radio_tags"}:
        if not isinstance(value, str):
            errors.append(f"{key}: expected one option key.")
            return
        legal = option_keys(field)
        if value not in legal:
            errors.append(f"{key}: illegal option {value!r}; legal={sorted(legal)}.")

    elif field_type == "checkbox_tags":
        if not isinstance(value, list) or not all(isinstance(x, str) for x in value):
            errors.append(f"{key}: expected an array of option keys.")
            return
        legal = option_keys(field)
        illegal = [x for x in value if x not in legal]
        if illegal:
            errors.append(f"{key}: illegal options {illegal}; legal={sorted(legal)}.")

    else:
        errors.append(f"{key}: unsupported schema field type {field_type!r}.")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True, help="task-input.json")
    parser.add_argument(
        "--schema",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "references" / "task-input-schema.json",
        help="task-input-schema.json",
    )
    args = parser.parse_args()

    try:
        schema = load_json(args.schema)
        task = load_json(args.input)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}")
        return 1

    errors: list[str] = []
    warnings: list[str] = []

    fields = {
        field["key"]: field
        for field in schema.get("fields", [])
        if isinstance(field, dict) and isinstance(field.get("key"), str)
    }
    values = task.get("values", {})
    if not isinstance(values, dict):
        print("ERROR: task-input.values must be an object.")
        return 1

    if task.get("skill") != schema.get("skill"):
        errors.append("skill does not match schema.skill.")

    unknown = sorted(set(values) - set(fields))
    if unknown:
        errors.append(f"Unknown fields: {unknown}")

    for key, field in fields.items():
        entry = values.get(key)
        if field.get("required") and entry is None:
            errors.append(f"Missing required field: {key}")
            continue
        if entry is None:
            continue
        if not isinstance(entry, dict) or "value" not in entry or "source" not in entry:
            errors.append(f"{key}: expected object with value and source.")
            continue

        validate_value(field, entry["value"], errors)

        source = entry["source"]
        policy = field.get("source_policy")
        allowed = SOURCE_ALIASES.get(policy)
        if allowed is not None and source not in allowed:
            errors.append(
                f"{key}: source={source!r} violates source_policy={policy!r}; "
                f"allowed={sorted(allowed)}."
            )

        if key == "product_images" and not entry["value"]:
            errors.append("product_images: at least one image is required.")

        if key == "extra_requirements" and source != "user_explicit":
            errors.append("extra_requirements must come from explicit user text.")

    omitted = task.get("omitted_fields", [])
    if omitted and not isinstance(omitted, list):
        errors.append("omitted_fields must be an array.")
    elif isinstance(omitted, list):
        overlap = sorted(set(omitted) & set(values))
        if overlap:
            errors.append(f"Fields cannot be both values and omitted: {overlap}")

    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")

    if errors:
        print("Result: FAIL")
        return 1

    print("Result: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
