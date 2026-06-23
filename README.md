# api-mcp-wiki

An Open Knowledge Format (OKF) bundle for *From GET to agentic government*.

The repository contains:

- `viewer.html` - a self-contained interactive graph and reader.
- `document/paper/from-get-to-agentic-government.md` - the published paper in
  Markdown.
- `document/paper/from-get-to-agentic-government.pdf` - the published paper as
  a PDF.
- `document/paper/from-get-to-agentic-government.docx` - the public DOCX source.
- `index.md`, `document/`, `standards/`, `uk-government/`, `organisations/`,
  and `glossary/` - the OKF Markdown corpus.
- `sources-index.md` and `log.md` - source and provenance indexes.

## Read Locally

Open `viewer.html` in a browser, or read the Markdown files directly from the
repository.

## Validate And Build

```sh
python3 scripts/check_okf.py
python3 scripts/validate_published_document.py
python3 scripts/build_site.py
```

The build writes a GitHub Pages-ready static site to `_site/`. The site uses
`viewer.html` as both `index.html` and `viewer.html`, then copies the public OKF
Markdown corpus beside it.

## Publication Status

This repository is publication-ready locally. Push it to GitHub and enable
GitHub Pages with **GitHub Actions** as the source.

## License

The paper, OKF corpus, PDF, DOCX, and documentation are licensed under
[CC BY-NC 4.0](LICENSE.md): free non-commercial reuse with attribution.

The viewer and build/validation scripts are licensed under the
[MIT License](LICENSE-CODE.md).

## GitHub Pages

The included workflow publishes the static site from `_site/` when pushed to
`main`, after validation passes. In the GitHub repository settings, configure
Pages to use **GitHub Actions** as the source.
