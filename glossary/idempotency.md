---
type: "Glossary term"
title: "Idempotency"
description: "An operation that can be repeated safely with the same effect as doing it once."
tags: [glossary]
aliases: "idempotent; safe retry"
timestamp: 2026-06-20T00:00:00Z
verified: "yes"
---

# Definition
An operation is **idempotent** if repeating it has the same effect as doing it once &#x2014; so a safe retry will not, say, charge a card twice. Important for reliable automation and agent actions.

# Used in this bundle
Appears in: [http-semantics](../standards/http-semantics.md), [future-directions](../document/themes/future-directions.md).

# Related terms
[statelessness](statelessness.md).
