---
type: "Glossary term"
title: "Request–response"
description: "Call-and-wait: a client sends a request and waits for the server's reply."
tags: [glossary]
aliases: "request-response; request response; synchronous; request/response"
timestamp: 2026-06-20T00:00:00Z
verified: "yes"
---

# Definition
The classic **call-and-wait** pattern: a client sends a request and blocks until the server returns a reply. Most HTTP/REST calls work this way. Contrast with [event-driven](event-driven.md) interaction, where no immediate reply is expected.

# Used in this bundle
Appears in: [rest](../standards/rest.md), [http-semantics](../standards/http-semantics.md).

# Related terms
[statelessness](statelessness.md), [event driven](event-driven.md).
