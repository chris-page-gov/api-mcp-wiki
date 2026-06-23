---
type: "Concept"
title: "Future direction possibilities (six)"
description: "Six strategic directions, with confidence labels and 'Action now' calls."
tags: [theme, future, agentic, security, governance]
timestamp: 2026-06-20T00:00:00Z
verified: "yes"
gap: "S1 addressed via legal-accountability-layer.md"
---

1. **API catalogue → active control plane** *(high confidence)* — continuously expose ownership, descriptions, classification, conformance, SLOs, versions, consumers, lineage. *Action now: require discoverable ownership and machine-readable contracts as a condition of production deployment.*
2. **Treat API + event + workflow descriptions as one family** *(high confidence)* — [OpenAPI](../../standards/openapi.md) + [AsyncAPI](../../standards/asyncapi.md) + [Arazzo](../../standards/arazzo.md) + shared schemas. *Action now: design around business events and user outcomes before choosing the protocol.*
3. **Agent-ready, but not agent-trusting** *(emerging)* — non-human identities, scoped/time-limited authority, read/recommend/act separation, human approval, audit, idempotency, limits, rollback, provenance, redress. *Principle: understanding an API is never authority to use it.* **Now addressed:** see [The legal and accountability layer](legal-accountability-layer.md) (added in review) — DUAA 2025 Arts 22A–22D, ATRS, the duty to give reasons, PSED, and redress.
4. **Semantic > syntactic interoperability** *(hard)* — persistent IDs, shared vocabularies, definitions/provenance, model mappings, effective dates; a *federated* model beats one universal data model.
5. **Bearer access → demonstrable authority** *(high confidence security)* — workload identity, proof-bound credentials, fine-grained policy, short-lived access, continuous audit. *"Who is acting, for whom, for what purpose, under which legal authority, with what evidence retained?"* See [OAuth BCP](../../standards/oauth-2-0-security-bcp.md).
6. **APIs as enduring public products** *(operating model)* — funded ownership, user research, support, reliability targets, lifecycle policy, backward-compatibility, sustainable funding.

**Evaluation:** strong and decision-oriented. Only direction 3 needs the legal layer added.

# Terms
Glossary terms used here: [Bearer token](../../glossary/bearer-token.md), [Executable contract](../../glossary/contract.md), [Human-in-the-loop](../../glossary/human-in-the-loop.md), [Idempotency](../../glossary/idempotency.md), [Provenance](../../glossary/provenance.md), [Redress](../../glossary/redress.md), [Schema](../../glossary/schema.md), [Workflow](../../glossary/workflow.md), [Workload identity](../../glossary/workload-identity.md).
