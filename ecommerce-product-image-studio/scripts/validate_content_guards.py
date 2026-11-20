#!/usr/bin/env python3
"""Validate critical-geometry and evidence-bound copy guard records."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


ALLOWED_EVIDENCE = {"user_confirmed", "document_verified", "visible_in_reference", "estimated"}
BLOCKED_EVIDENCE = {"unknown", "conflicting"}
COPY_STATUSES = {"DRAFT", "APPROVED", "BLOCKED"}


def load(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def validate_geometry(data: dict[str, Any], errors: list[str]) -> None:
    relations = data.get("relations")
    if not isinstance(relations, list) or not relations:
        errors.append("critical-geometry-lock: relations must be a non-empty array.")
        return

    ids: set[str] = set()
    required = ("relation_id", "subject", "relation", "object", "evidence_refs")
    for i, item in enumerate(relations):
        if not isinstance(item, dict):
            errors.append(f"critical-geometry-lock[{i}]: expected object.")
            continue
        for key in required:
            if key not in item or item.get(key) in ("", None, []):
                errors.append(f"critical-geometry-lock[{i}]: {key} is required.")
        rid = item.get("relation_id")
        if isinstance(rid, str):
            if rid in ids:
                errors.append(f"critical-geometry-lock: duplicate relation_id {rid!r}.")
            ids.add(rid)
        must_not = item.get("must_not", [])
        if not isinstance(must_not, list) or not all(isinstance(x, str) and x for x in must_not):
            errors.append(f"critical-geometry-lock[{i}]: must_not must be an array of strings.")


def validate_copy(data: dict[str, Any], errors: list[str]) -> None:
    facts = data.get("facts")
    copy = data.get("copy")
    if not isinstance(facts, list):
        errors.append("copy-deck: facts must be an array.")
        return
    if not isinstance(copy, list):
        errors.append("copy-deck: copy must be an array.")
        return

    fact_map: dict[str, dict[str, Any]] = {}
    for i, fact in enumerate(facts):
        if not isinstance(fact, dict):
            errors.append(f"copy-deck.facts[{i}]: expected object.")
            continue
        fid = fact.get("fact_id")
        if not isinstance(fid, str) or not fid:
            errors.append(f"copy-deck.facts[{i}]: fact_id is required.")
            continue
        if fid in fact_map:
            errors.append(f"copy-deck: duplicate fact_id {fid!r}.")
        fact_map[fid] = fact
        state = fact.get("evidence_state")
        if state not in ALLOWED_EVIDENCE | BLOCKED_EVIDENCE:
            errors.append(f"copy-deck.facts[{i}]: illegal evidence_state {state!r}.")

    blocked_expansions = data.get("blocked_expansions", [])
    if not isinstance(blocked_expansions, list) or not all(
        isinstance(x, str) and x for x in blocked_expansions
    ):
        errors.append("copy-deck: blocked_expansions must be an array of strings.")
        blocked_expansions = []

    for i, item in enumerate(copy):
        if not isinstance(item, dict):
            errors.append(f"copy-deck.copy[{i}]: expected object.")
            continue
        text = item.get("text")
        status = item.get("status")
        source_ids = item.get("source_fact_ids")
        if not isinstance(text, str) or not text:
            errors.append(f"copy-deck.copy[{i}]: text is required.")
        if status not in COPY_STATUSES:
            errors.append(f"copy-deck.copy[{i}]: illegal status {status!r}.")
        if not isinstance(source_ids, list) or not source_ids:
            errors.append(f"copy-deck.copy[{i}]: source_fact_ids must be non-empty.")
            continue

        missing = [fid for fid in source_ids if fid not in fact_map]
        if missing:
            errors.append(f"copy-deck.copy[{i}]: unknown source facts {missing}.")
            continue

        if status == "APPROVED":
            bad = [
                fid for fid in source_ids
                if fact_map[fid].get("evidence_state") in BLOCKED_EVIDENCE
            ]
            if bad:
                errors.append(
                    f"copy-deck.copy[{i}]: APPROVED copy depends on blocked facts {bad}."
                )
            for phrase in blocked_expansions:
                if phrase.lower() in text.lower():
                    errors.append(
                        f"copy-deck.copy[{i}]: text contains blocked expansion {phrase!r}."
                    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--geometry-lock", type=Path)
    parser.add_argument("--copy-deck", type=Path)
    args = parser.parse_args()

    if not args.geometry_lock and not args.copy_deck:
        parser.error("provide --geometry-lock and/or --copy-deck")

    errors: list[str] = []
    try:
        if args.geometry_lock:
            data = load(args.geometry_lock)
            if not isinstance(data, dict):
                errors.append("critical-geometry-lock root must be an object.")
            else:
                validate_geometry(data, errors)
        if args.copy_deck:
            data = load(args.copy_deck)
            if not isinstance(data, dict):
                errors.append("copy-deck root must be an object.")
            else:
                validate_copy(data, errors)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}")
        return 1

    for error in errors:
        print(f"ERROR: {error}")
    if errors:
        print("Result: FAIL")
        return 1

    print("Result: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
