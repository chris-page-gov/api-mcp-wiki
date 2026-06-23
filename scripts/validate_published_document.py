#!/usr/bin/env python3
"""Validate published paper artifacts against the OKF corpus."""

from __future__ import annotations

import re
import sys
import zipfile
from pathlib import Path
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

ROOT = Path(__file__).resolve().parents[1]
PAPER_MD = ROOT / "document/paper/from-get-to-agentic-government.md"
PAPER_PDF = ROOT / "document/paper/from-get-to-agentic-government.pdf"
PAPER_DOCX = ROOT / "document/paper/from-get-to-agentic-government.docx"
OKF_ROOT_FILES = {"index.md", "sources-index.md", "log.md"}
OKF_DIRS = {"document", "glossary", "organisations", "standards", "uk-government"}
URL_RE = re.compile(r"https?://[^\s)>\"']+")


def normalize_url(url: str) -> str:
    url = url.rstrip(".,;")
    parts = urlsplit(url)
    query = urlencode(
        [(key, value) for key, value in parse_qsl(parts.query, keep_blank_values=True) if not key.lower().startswith("utm_")]
    )
    path = parts.path.rstrip("/") or "/"
    return urlunsplit((parts.scheme.lower(), parts.netloc.lower(), path, query, ""))


def urls_in_text(text: str) -> set[str]:
    return {normalize_url(match.group(0)) for match in URL_RE.finditer(text)}


def iter_okf_markdown() -> list[Path]:
    paths: list[Path] = []
    for path in ROOT.rglob("*.md"):
        rel = path.relative_to(ROOT)
        parts = rel.parts
        if parts[0] in {"_site", "tmp"}:
            continue
        if path == PAPER_MD:
            continue
        if parts[0] in OKF_DIRS or (len(parts) == 1 and parts[0] in OKF_ROOT_FILES):
            paths.append(path)
    return sorted(paths)


def docx_contains_tracking(path: Path) -> bool:
    with zipfile.ZipFile(path) as archive:
        for name in archive.namelist():
            if name.endswith(".xml") or name.endswith(".rels"):
                if b"utm_source" in archive.read(name):
                    return True
    return False


def main() -> int:
    errors: list[str] = []
    for path in (PAPER_MD, PAPER_PDF, PAPER_DOCX):
        if not path.exists():
            errors.append(f"missing published artifact: {path.relative_to(ROOT)}")

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    paper_text = PAPER_MD.read_text(encoding="utf-8")
    if "utm_source" in paper_text:
        errors.append(f"{PAPER_MD.relative_to(ROOT)} contains a tracking URL")
    if docx_contains_tracking(PAPER_DOCX):
        errors.append(f"{PAPER_DOCX.relative_to(ROOT)} contains a tracking URL")
    if b"utm_source" in PAPER_PDF.read_bytes():
        errors.append(f"{PAPER_PDF.relative_to(ROOT)} contains a tracking URL")

    if "# References" not in paper_text:
        errors.append(f"{PAPER_MD.relative_to(ROOT)} is missing a References section")
    else:
        reference_text = paper_text.split("# References", 1)[1]
        reference_urls = urls_in_text(reference_text)
        corpus_urls: set[str] = set()
        for path in iter_okf_markdown():
            corpus_urls.update(urls_in_text(path.read_text(encoding="utf-8", errors="ignore")))
        missing = sorted(reference_urls - corpus_urls)
        if missing:
            errors.append("published paper reference URLs missing from OKF corpus:")
            errors.extend(f"  - {url}" for url in missing)

    if errors:
        print("Published document validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print("Published document validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
