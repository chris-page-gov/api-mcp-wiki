@AGENTS.md

# Project Overview

Open Knowledge Format (OKF) bundle and GitHub Pages site for the paper
"From GET to agentic government". The Markdown files are the source of truth;
`viewer.html` is a generated interactive graph/reader.

# Validate & Build

```sh
python3 scripts/check_okf.py
python3 scripts/validate_published_document.py
python3 scripts/build_site.py
```

Run all three before committing publication changes. CI runs them on push to
`main` via `.github/workflows/pages.yml`.

# Key Paths

- `document/paper/` — published paper (Markdown, PDF, DOCX)
- `document/`, `glossary/`, `organisations/`, `standards/`, `uk-government/` — OKF corpus
- `scripts/` — validation and build tooling (Python 3, no dependencies)
- `viewer.html` — generated; regenerate with `python3 scripts/update_viewer.py`
- `_site/` — build output (gitignored)

# Conventions

- Every Markdown concept file has YAML frontmatter (`type`, `title`, `description`, `timestamp`).
- Links are plain Markdown links — no Obsidian wikilinks.
- If OKF Markdown changes, run `python3 scripts/update_viewer.py` to keep `viewer.html` in sync.
- Do not commit `.docx` peer-review files, Word lock files (`~$*`), or `.DS_Store`.
