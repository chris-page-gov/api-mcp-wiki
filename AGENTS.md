# Codex Instructions

This repository publishes an Open Knowledge Format (OKF) Markdown bundle and a
self-contained HTML viewer for the "From GET to agentic government" material.

## Working Rules

- Treat the Markdown files as the source of truth.
- Keep links browser-compatible Markdown links. Do not introduce Obsidian-only
  wikilinks.
- Do not edit the peer-review Word document unless the user explicitly asks.
- Do not add the tracked-review `.docx`, Word lock files, or `.DS_Store` files
  to Git.
- If OKF Markdown changes, run `python3 scripts/update_viewer.py` so
  `viewer.html` stays synchronized.
- Before committing publication changes, run:

```sh
python3 scripts/check_okf.py
python3 scripts/build_site.py
```

## Publication Model

- GitHub repository: canonical OKF source and review history.
- GitHub Pages: static public site built into `_site/`.
- GitHub Releases: frozen snapshots after the paper review is complete.

The current publication gate is the unresolved paper review: publish the viewer
and OKF bundle, but only add a clean paper artifact after tracked changes and
comments have been resolved.
