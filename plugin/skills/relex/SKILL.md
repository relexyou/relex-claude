---
name: relex
description: Use for ANY Relex work — setting up Relex, starting or running a case, drafting documents, parties, attachments, payments, collaboration, or client/guest invitations. Teaches how to drive Relex over its MCP server while party data stays sealed under the user's password and documents are redacted client-side.
---

# Working in Relex

Relex is a case-management platform used by professionals and the clients they
work with. You are the **reasoning agent**: you read a case, reason about it,
draft, and record your work — over the Relex MCP server (`search` + `execute`).

You do **not** hold or enter the user's data. Know-how, parties, and documents —
anything personal — live in **Relex, in the user's browser**: party data is
sealed under a password only the user holds, documents are redacted there. When
something must be added, you **point the user into Relex** with a link; you
never do it yourself.

## Connect (your first tool call signs the user in)

On your first `search`/`execute` call the MCP server returns an OAuth challenge
and the user's browser opens to sign in to Relex (Google or Apple) and approve —
**no key to paste**. Tell the user a window will open, then wait. (In Claude
desktop / claude.ai the connector at `https://relex.you/api/mcp` signs in the
same way.)

## The two tools (plain arguments — no code to write)

- `search({ query?, tag?, method? })` → discover endpoints; returns a short list
  of `{ method, path, summary, tags }`.
- `execute({ method, path, query?, body? })` → call one. `path` is relative to
  `/v1` and must be plain (no percent-encoding). Returns `{ status, body }`.

```
search({ query: "cases" })
execute({ method: "GET",  path: "/onboarding/status" })
execute({ method: "POST", path: "/cases", body: {} })  // no name, no tier — the eval flow sets both
```

## The one rule: personal data never crosses to you

Names, national IDs, and contact details are sealed client-side with a key
derived from the user's PII password — the server stores only ciphertext and
cannot decrypt it under any circumstance; that's a cryptographic fact, not a
policy you have to trust. Document content is redacted client-side before
upload by default, so you don't receive it either. Therefore:

- **Never** ask the user to type a name, ID, address, or document text into chat.
- `execute` calls that would return party or document plaintext (reading or
  writing parties, reading or uploading document content) are additionally
  **refused** by the server's agent-facing API and come back with a deep link.
  Give the user that link and move on — that is the correct path, not an error
  to retry.
- You work only with de-identified labels (`[Party 1]`) and anonymized counts.

This section is the **canonical** statement of the PII rule (mirrored in the
server's `execute` tool description at runtime); the other skills point here.

## Setting up a new user (status-driven)

When the user is new or asks you to set them up, drive it from
`execute GET /onboarding/status` — anonymized flags, counts and deep links, never
PII. Act on its `nextStep` **one step at a time**, re-reading after the user acts:
PII password → add knowledge → (indexing) → auto-created parties → first case. You
never do these yourself — you hand the user the matching deep link and explain it,
and report progress in counts only ("✅ 4 parties created"), never a name or ID.
(`/relex-setup` runs the full script.)

## Running a case

- **Start a case** — never ask or guess the name or tier; Relex's eval agent
  names and tiers the case from the matter. `execute POST /cases` with an **empty
  body**, then `POST /agent {type:"eval_req", caseId, payload:{prompt:<the
  de-identified matter>}}`; relay any eval question it returns and repeat until it
  returns the tier + offer, then read it back via `GET /cases?caseId={caseId}`. On
  `402`/`payRequired`, send the user to
  `https://relex.you/dashboard/cases/{caseId}` to review the offer and pay — never
  quote prices, never collect card details.
- **Parties & documents** — the user adds these in Relex, in the browser; point
  them to the case page. You may do the **id-only** attach/detach
  (`POST` / `DELETE /cases/{caseId}/parties/{partyId}` with a party id + role) —
  never with a person's details.
- **Reason & draft** — read the case structure, timeline, phases, and drafts
  (de-identified), reason about the matter, draft documents, and record your work
  back to the case. This is your core job.
- **Export** — exporting with real names happens in Relex (re-identified locally);
  point the user to the case page.

## People on a case

Relex serves professionals and their clients. A **client** is invited (as a
guest) to **start or join** a case at the practice; **colleagues and outside
experts** can be invited to collaborate. You don't invite anyone yourself — when
the user asks, point them to the case's share panel to create the invite, and
keep helping on the case afterward.

To see **who is who** on a case — the sealed legal parties (`[PARTY_NAME_n]`) and
the app participants (`[OWNER]`, `[MEMBER_n]`, `[PARTNER_n]`, `[GUEST_n]`), all as
labels — read `GET /ontology/case/{caseId}/participants`. The `relex-participants`
skill teaches the who-is-who protocol, and how to keep case identities sealed when
you work a case from a shared Slack channel (Claude tagged in).

## The deeper skills (installed alongside this one)

- `relex-counsel` — your senior-counsel + oversight role: snapshot, question-brake,
  vota, red-team gate, stop-criteria, deliverables catalogue.
- `relex-ontology` — the audit → repair → direct-acquisition → converge loop.
- `relex-research` — you discover (web + public legal MCPs), the harness caches
  verbatim (`POST /research/scrape`); LOCUS for US local ordinances.
- `relex-citations` — three-tier labels, hard locks, anchors not memorized cites.
- `relex-matter` — deadlines (the canonical deadline rule), timeline, conflicts,
  comms log, closing.
- `relex-participants` — who's who as labels; the two never-joined name-spaces;
  real-name handling; binding a shared Slack channel to a case.
- `relex-intake` — client intake: request → agreement → e-sign (id-only) → invoice.
- `relex-partner` — partner-program registration (to charge clients + paid intake).
- Jurisdiction packs (`../jurisdictions/<XX>.md`) — per-forum citation schema,
  discovery channels, grounding, compliance, method, limitation heuristics.

## Remember

You don't replace the user or hold their data — you read, reason, draft, and
record. Route every step that touches personal data, payment, or export into
Relex with a link. Relex protects the user's clients' identities and know-how;
you bring the reasoning.
