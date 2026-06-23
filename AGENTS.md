# Codex Instructions

This repository publishes an Open Knowledge Format (OKF v0.1) Markdown bundle
and a self-contained HTML viewer for the "From GET to agentic government"
material.

## Working Rules

- Treat the Markdown files as the source of truth.
- Keep links browser-compatible Markdown links. Do not introduce Obsidian-only
  wikilinks.
- Do not edit historical peer-review Word documents unless the user explicitly asks.
- Do not add the tracked-review `.docx`, Word lock files, or `.DS_Store` files
  to Git.
- If OKF Markdown changes, run `python3 scripts/update_viewer.py` so
  `viewer.html` stays synchronized.
- Before committing publication changes, run:

```sh
python3 scripts/check_okf.py
python3 scripts/validate_published_document.py
python3 scripts/build_site.py
```

## OKF Frontmatter

Every concept Markdown file must begin with YAML frontmatter containing these
**required** fields (enforced by `scripts/update_viewer.py`):

| Field         | Purpose                          |
|---------------|----------------------------------|
| `type`        | Concept type (e.g. "Specification", "Glossary term", "Organisation") |
| `title`       | Human-readable title             |
| `description` | One-line summary                 |
| `timestamp`   | ISO 8601 date (e.g. `2026-06-20T00:00:00Z`) |

**Optional fields** (conventional, not enforced):

| Field             | Purpose                              |
|-------------------|--------------------------------------|
| `resource`        | External canonical URL               |
| `tags`            | YAML array of topic tags             |
| `verified`        | Citation verification status (`"yes"`) |
| `aliases`         | Semicolon-separated alternative names |
| `citation_status` | Editorial note for pending fixes     |

## OKF Linking Conventions

Links are **unidirectional and untyped** — plain Markdown `[text](path.md)`.
The viewer infers relationship types from section position and direction.

- **Terms section**: Each concept ends with a `# Terms` heading listing glossary
  entries it uses, e.g. `[Contract](../glossary/contract.md)`.
- **Reverse links in glossary**: Glossary entries include a `# Used in this bundle`
  section listing concepts that reference them — making the relationship
  bidirectional in the files.
- **Organisations** carry few glossary links by design; they are actors, not
  concepts. They connect to vocabulary through the standards they steward.
- **UK-government** pages link to governance terms (automated decision, meaningful
  human involvement, redress) and reach technical vocabulary via adopted standards.

## Publication Model

- GitHub repository: canonical OKF source and review history.
- GitHub Pages: static public site built into `_site/`.
- GitHub Releases: frozen snapshots of the paper and OKF corpus.

The public paper artifacts live under `document/paper/`.
