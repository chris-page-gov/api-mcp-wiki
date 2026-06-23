# Publication Plan

Status: initialized for local Git and GitHub Pages publication.

## Public Surfaces

- Repository: canonical OKF Markdown source, provenance, issues, pull requests,
  and review history.
- GitHub Pages: public interactive viewer generated from `viewer.html` and the
  OKF Markdown corpus.
- GitHub Releases: versioned snapshots once the paper review is complete.
- Optional DOI: connect the public repository to Zenodo after the first release
  if a persistent scholarly citation is required.

## Current Release Gates

- Resolve tracked changes and comments in
  `From GET to Agentic Government__PEER-REVIEW-tracked.docx`.
- Produce a clean public paper artifact if the paper itself should be released.
- Choose an explicit license before inviting reuse.
- Add final citation metadata, preferably `CITATION.cff`, before publicizing as
  a citable research object.
- Push to a GitHub remote and enable Pages with **GitHub Actions** as the source.

## Publication Checks

Run these before publishing or cutting a release:

```sh
python3 scripts/check_okf.py
python3 scripts/build_site.py
```

The Pages build deliberately excludes `.docx` files, Word lock files,
`.DS_Store`, Git internals, and generated caches.
