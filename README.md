# api-mcp-wiki

An Open Knowledge Format (OKF) bundle for *From GET to agentic government*.

The repository contains:

- `viewer.html` - a self-contained interactive graph and reader.
- `index.md`, `document/`, `standards/`, `uk-government/`, `organisations/`,
  and `glossary/` - the OKF Markdown corpus.
- `sources-index.md` and `log.md` - source and provenance indexes.

## Read Locally

Open `viewer.html` in a browser, or read the Markdown files directly from the
repository.

## Validate And Build

```sh
python3 scripts/check_okf.py
python3 scripts/build_site.py
```

The build writes a GitHub Pages-ready static site to `_site/`. The site uses
`viewer.html` as both `index.html` and `viewer.html`, then copies the public OKF
Markdown corpus beside it.

## Publication Status

This repository is initialized for publication, but the peer-review Word
document is still a working review artifact. It is intentionally excluded from
Git by default until a clean public paper artifact is produced.

Before public release:

- resolve the tracked changes and comments in the paper;
- choose a repository license;
- add final citation metadata, such as `CITATION.cff`, if the material should be
  formally citable;
- create a GitHub release for the first stable snapshot.

## GitHub Pages

The included workflow publishes the static site from `_site/` when pushed to
`main`, after validation passes. In the GitHub repository settings, configure
Pages to use **GitHub Actions** as the source.
