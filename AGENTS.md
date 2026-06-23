# Codex Instructions

This repository publishes an Open Knowledge Format (OKF) Markdown bundle and a
self-contained HTML viewer for the "From GET to agentic government" material.

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

## Publication Model

- GitHub repository: canonical OKF source and review history.
- GitHub Pages: static public site built into `_site/`.
- GitHub Releases: frozen snapshots of the paper and OKF corpus.

The public paper artifacts live under `document/paper/`.
