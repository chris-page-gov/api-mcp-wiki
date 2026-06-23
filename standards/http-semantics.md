---
type: "Specification"
title: "HTTP Semantics — RFC 9110 (2022)"
description: "Separates durable HTTP semantics from the wire formats that carry them."
resource: "https://www.rfc-editor.org/info/rfc9110"
tags: [http, rfc, standard, semantics]
timestamp: 2022-06-01T00:00:00Z
verified: "yes"
---

# What it is
**RFC 9110 (June 2022)** defines the semantics shared by all HTTP versions; **HTTP/1.1 (9112)**, **HTTP/2 (9113)** and **HTTP/3 (9114)** are separate specs for representing and transporting them.

# Why it matters (document's key lesson)
**GET, POST, status codes, headers, caching and resource semantics are the enduring contract.** Versions are just different ways of carrying it — so *standardise durable semantics and outcomes, not incidental infrastructure*.

# Evaluation
Accurate and well-used as a conceptual anchor. Relates to: [HTTP/3](http-3.md), [Six shifts](../document/themes/six-shifts.md).

# Terms
Glossary terms used here: [Semantic interoperability](../glossary/semantic-interoperability.md).
