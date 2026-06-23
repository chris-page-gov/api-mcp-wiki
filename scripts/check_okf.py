#!/usr/bin/env python3
"""Validate the OKF bundle before publication."""

from __future__ import annotations

import sys
from pathlib import Path

import update_viewer

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    graph, errors = update_viewer.build_graph()

    if "index.md" not in graph["nodes"]:
        errors.append("index.md is missing from the OKF graph")
    if "sources-index.md" not in graph["nodes"]:
        errors.append("sources-index.md is missing from the OKF graph")
    if "glossary/index.md" not in graph["nodes"]:
        errors.append("glossary/index.md is missing from the OKF graph")
    if not (ROOT / "viewer.html").exists():
        errors.append("viewer.html is missing")

    try:
        updated = update_viewer.rendered_viewer(graph)
    except ValueError as exc:
        errors.append(str(exc))
        updated = ""

    if updated and updated != (ROOT / "viewer.html").read_text(encoding="utf-8"):
        errors.append("viewer.html is not synchronized; run python3 scripts/update_viewer.py")

    if errors:
        print("OKF validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    review_docs = sorted(ROOT.glob("*__PEER-REVIEW-tracked.docx"))
    if review_docs:
        print("Publication note: tracked-review .docx exists locally and is ignored until clean release.")

    print(f"OKF validation passed: {len(graph['nodes'])} nodes, {len(graph['edges'])} edges")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
