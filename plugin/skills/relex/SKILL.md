---
name: relex
description: Use for ANY Relex work — setting up Relex, starting or running a case, drafting documents, parties, attachments, payments, collaboration, or client/guest invitations. Teaches how to drive Relex over its MCP server while the user's personal data stays encrypted in their browser.
---

# Working in Relex

Relex is a case-management platform used by professionals and the clients they
work with. You are the **reasoning agent**: you read a case, reason about it,
draft, and record your work — over the Relex MCP server (`search` + `execute`).

You do **not** hold or enter the user's data. Adding know-how, parties, and
documents — and anything touching personal data — happens in **Relex, in the
user's browser**, where it is encrypted with a password only they hold. When
something must be added or decrypted, you **point the user into Relex**; you
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
execute({ method: "POST", path: "/cases", body: { name: "Acme dispute", caseTier: 1 } })
```

## The one rule: personal data never crosses to you

Names, national IDs, contact details, and document content are end-to-end
encrypted and only decrypt in the user's browser. Therefore:

- **Never** ask the user to type a name, ID, address, or document text into chat.
- `execute` calls that would move personal data (reading or writing parties,
  reading or uploading document content) are **refused** by the server and come
  back with a deep link. Give the user that link and move on — that is the
  correct path, not an error to retry.
- You work only with de-identified labels (`[Party 1]`) and anonymized counts.

## Setting up a new user (status-driven)

When the user is new or asks you to set them up, drive it from
`execute({ method: "GET", path: "/onboarding/status" })`, which returns only
anonymized flags/counts + deep links (never PII):
`{ connected, piiConfigured, knowledge:{total,indexed,processing,awaitingParties,failed},
   detectedParties, parties:{count}, nextStep, deepLinks:{ pii, knowledge, parties, cases } }`.

Act on `nextStep`, one step at a time, re-reading after the user acts. You don't
do these yourself — you hand the user the right link and explain it:

- `set_pii_password` → `deepLinks.pii`: the user sets a password (and saves the
  recovery key) that encrypts personal data in their browser. This comes first.
- `add_knowledge` → `deepLinks.knowledge`: the user uploads playbooks, templates,
  and past matters. Relex indexes them privately and finds the parties in them.
- `processing` → indexing is still running; wait, then re-read.
- `finish_parties` → with the password unlocked on the knowledge page, Relex
  encrypts and creates the detected parties in the browser. Confirm `parties.count`.
- `create_case` / `ready` → setup is done; offer to start the first case.

Report progress with the counts ("✅ 4 parties created from your know-how") —
never echo a name or ID. (The `/relex-setup` command runs exactly this.)

## Running a case

- **Start a case** — `execute POST /cases` `{ name, caseTier }` (tier 1/2/3). On
  `402 Payment Required`, point the user to billing (`deepLinks.cases` / the
  billing page); never collect card details.
- **Parties & documents** — the user adds these in Relex (encrypted in the
  browser); point them to the case page. You may do the **id-only** attach/detach
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

## The deeper skills (installed alongside this one)

- `relex-counsel` — your role: senior counsel + oversight over the harness;
  deadline-first snapshot, question-brake, vota, red-team gate, stop-criteria.
- `relex-ontology` — the collaboration loop: audit the case's understanding,
  repair the graph, direct acquisition, converge.
- `relex-research` — you discover (web + public legal MCPs), the harness
  fetches-and-caches verbatim text (`POST /research/scrape`), drafts cite only
  cached law. LOCUS for US local ordinances.
- `relex-citations` — three-tier epistemic labels, hard locks, anchors instead
  of memorized citations.
- `relex-matter` — deadlines, timeline, conflicts, comms log, closing.

## Remember

You don't replace the user or hold their data — you read, reason, draft, and
record. Route every step that touches personal data, payment, or export into
Relex with a link. Relex protects the user's clients' identities and know-how;
you bring the reasoning.
