---
type: "Index"
title: "api-mcp-wiki — From GET to agentic government (OKF bundle)"
description: "An Open Knowledge Format bundle: the reviewed document, its evaluation, and every source as a cross-linked concept."
tags: [index, root, okf, agentic, uk-government]
timestamp: 2026-06-20T00:00:00Z
---

# api-mcp-wiki

An **Open Knowledge Format (OKF v0.1)** bundle for *From GET to agentic government*. OKF represents knowledge as a directory of markdown files with YAML frontmatter (`type`, `title`, `description`, `resource`, `tags`, `timestamp`) and markdown cross-links that turn the directory into a graph. This bundle is **just files** — readable in any editor, on GitHub, or via the included offline viewer.

## Contents
- **[The reviewed document](document/index.md)** — overview, [timeline](document/timeline/index.md), [themes](document/themes/index.md), and the [peer review](document/peer-review.md).
- **[Sources index](sources-index.md)** — every source mentioned, with verified citations.
- **[Standards & specifications](standards/index.md)** — 21 concepts.
- **[UK government sources](uk-government/index.md)** — 11 concepts.
- **[Glossary](glossary/index.md)** — plain-English definitions of technical terms.
- **[Organisations](organisations/index.md)** — 11 concepts.
- **[Change log / provenance](log.md)**

## How to use
Open **`viewer.html`** for an interactive graph + browser (no install, works offline), or read the markdown directly. Each concept links to related concepts; follow the links to explore.

## Linking conventions

OKF v0.1 links are plain markdown — **unidirectional and untyped**. This bundle adopts two conventions the spec leaves open:

1. **Glossary/vocabulary** terms are linked **from the concept that uses them** (a `Terms` section at the foot of each concept), mirroring wiki practice; each glossary entry also lists where it is used, so the term↔concept relationship is bidirectional in the files.
2. **Direction is meaningful** (a link means *source references target*); consumers build the reverse index (the viewer's "Referenced by"). Relationship *types* (defines, stewards, introduces, adopts…) are inferred by the viewer from section + direction.

**Organisations** carry few glossary links by design — they are actors / standards bodies, not described by technical vocabulary; they connect to the vocabulary via the standards they steward. **UK-government** pages use policy/legal language, so they link to the governance terms (automated decision, meaningful human involvement, redress) and otherwise reach the vocabulary through the standards they adopt.

## Verdict
The document is **accept with minor revisions** — accurate and well-structured; revisions concern citation hygiene and one substantive gap (the legal/accountability layer). See the [peer review](document/peer-review.md).

# Terms
Glossary terms used here: [Provenance](glossary/provenance.md).
