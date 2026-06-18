---
name: relex
description: Use for ANY Relex legal-case work — starting or managing a case, drafting legal documents, contracts, handling client matters, parties, attachments, payments, or guest/client invitations in Relex. Teaches the PII-safe, deep-link-first workflow over the Relex MCP server.
---

# Working inside Relex from Claude

Relex is a legal case-management platform. This skill lets you (Claude) operate
inside a lawyer's Relex case **without ever touching their clients' personal
data**. You sign in once over OAuth — on your first tool call the Relex MCP
server returns an OAuth challenge and your client opens the user's browser to
sign in with Google/Apple and approve access; **there is no key to paste** — and
then work through the Relex MCP server (`search` + `execute` tools).

## The one rule: PII never crosses this boundary

Client PII — names, national IDs (CNP/SSN), contact details, and **document
content** — is **end-to-end encrypted**. It can only be decrypted in the user's
**browser** with their PII password. The API only ever returns encrypted blobs.

Therefore:

- **Never** ask the user to paste a client's name, ID number, address, contact
  info, or a document's contents into the chat.
- **Never** expect `execute` to return plaintext PII. Reads of party data and
  attachment/document content are **refused** by the server and come back with a
  deep link — when that happens, hand the user the deep link and stop trying.
- For anything PII-bearing — adding/editing parties, viewing or exporting
  documents, attaching files — **send the user a browser deep link** and let them
  do it in the Relex UI. That is the correct, secure path, not a limitation to
  work around.

## How to call the API (Code Mode)

You have two tools. Always `search` first, then `execute`.

Both tools take **plain arguments** (no code/JS to write):

- `search({ query?, tag?, method? })` — discover endpoints. Returns a small list
  of `{ method, path, summary, tags }`. Example: `search({ query: "cases" })`.
- `execute({ method, path, query?, body? })` — call an endpoint. `path` is
  relative to `/v1` and must be a plain path (no percent-encoding). The server
  validates it against the spec, applies the PII guard, runs it with your auth,
  and returns `{ status, body }`. Examples:
  ```
  execute({ method: "GET",  path: "/onboarding/status" })
  execute({ method: "POST", path: "/cases", body: { name: "Acme dispute", caseTier: 1 } })
  ```

## First run — set up the practice workflow

When a user says *"set up my practice workflow with Relex"* (or is brand new),
run the guided setup. The `/relex-setup` command has the full script; the core is:
drive it from `GET /onboarding/status` and act on its `nextStep`.

`execute({ method: "GET", path: "/onboarding/status" })` returns only anonymized
counts + flags + deep links — never PII:
`{ connected, piiConfigured, knowledge:{total,indexed,processing,awaitingParties,failed},
   detectedParties, parties:{count}, nextStep, deepLinks:{pii,knowledge,parties,cases} }`.

Sequence (one step at a time; re-read status after each, report progress with the
anonymized counts — never echo a name or ID):

1. **Sign in** — your first tool call triggers the OAuth browser sign-in. Tell the
   user a browser window will open; wait for them to finish.
2. **PII password** (`nextStep: set_pii_password`) — deep-link `deepLinks.pii`. The
   user sets a PII password (and saves a recovery key) that encrypts all client
   identities in their browser. This is required before any party can be created.
3. **Knowledge** (`add_knowledge`) — deep-link `deepLinks.knowledge`. The user
   uploads playbooks, templates, and past matters. Relex indexes them privately
   and extracts the parties it finds.
4. **Auto-create parties** (`finish_parties`) — Relex found parties in the
   knowledge; with the PII password unlocked on the knowledge page, it encrypts
   and creates them in the browser. Confirm `parties.count` rises. You never see
   the names — only the count.
5. **Ready** (`create_case` / `ready`) — offer to start the first case.

This is the heart of the product: the user's know-how powers the work and their
clients' identities are auto-extracted into **encrypted** parties without you ever
seeing them.

## End-to-end workflow

### 1. Start a case
`POST /cases` with `{ name, caseTier }` (tier 1 = €9, 2 = €29, 3 = €99). For an
org case use `POST /organizations/{organizationId}/cases`. You get back a
`caseId`. Read a case with `GET /cases?caseId=…` (encrypted/structural fields
only — no plaintext PII).

If creation returns **`402 Payment Required`**, the user must pay → see §5.

### 2. Set up parties & PII — via the browser, always
Parties carry PII, so you do **not** create or read them over the API. Guide the
user:
> "Add the people/companies involved in your case in Relex — open
> **https://relex.you/dashboard/parties** to add a party, then attach it to the
> case from **https://relex.you/dashboard/cases/{caseId}**. Your data is
> encrypted locally; I never see it."

Once parties exist, you *may* perform the **structural, PII-free** attach/detach
(party id + role only): `POST /cases/{caseId}/parties` `{ partyId, role }` and
`DELETE /cases/{caseId}/parties/{partyId}`. You will only have a `partyId` if the
user gives you the id (not the person's details) — ask for the id, never the
identity.

### 3. Attach documents — via the browser, always
Document content is encrypted. Do **not** ask for file contents or try to read
attachments. Deep-link:
> "Upload your documents to the case here:
> **https://relex.you/dashboard/cases/{caseId}** (drag-and-drop). They're
> encrypted in your browser before upload."

You can see *that* attachments/drafts exist via case/branch/phase metadata, but
`GET /attachment/{id}` and `GET /attachments` are PII-refused by design.

### 4. Draft
Relex's case agent produces drafts on the case timeline (branches → phases →
drafts). Use `GET /timeline/{timelineId}`, `GET /phases`, `GET /drafts?branchId=…`
to see structure and `GET /draft/{draftId}` for draft text (drafts are working
legal text the agent itself wrote — not client PII). Help the user reason about
the matter, propose argument structure, and iterate on drafts. Heavy
case-reasoning happens in the Relex agent; you orchestrate and advise.

### 5. When the user must pay → deep-link
If you hit `402`, or a tier upgrade / subscription is needed, **do not** try to
collect card details. Send them to billing:
> "This case needs payment to continue — open
> **https://relex.you/dashboard/billing** to pay (Relex handles the payment for
> you). Tell me once it's done and I'll continue."
(`POST /payments/intent` / `/payments/checkout` exist, but card entry is a
browser/Stripe flow — never gather payment data in chat.)

### 6. Exporting documents with PII → deep-link
Never export documents containing PII over the API. Send the user to the in-app
export on the case page (**https://relex.you/dashboard/cases/{caseId}**) so the
content is decrypted and rendered locally.

### 7. Customer / client invitations (guest links)
Lawyers can invite an external client into a single case as a **guest** (the
guest is never an org member and never owns the case). End-to-end:
1. Ask the user which case the client should join (the `caseId`).
2. Generate the guest invite from the Relex dashboard — deep-link the lawyer to
   the case's sharing panel: **https://relex.you/dashboard/cases/{caseId}**
   ("Invite client / Share"), where they create a one-time or permanent secret
   link. (Guest-link minting is part of the Relex guest-role flow; it is done in
   the UI so the secret and any PII stay in the browser.)
3. The lawyer sends that link to their client; the client opens it, signs in, and
   lands scoped to just that one case. Confirm with the lawyer and offer to keep
   helping on the case.

## Positioning to keep in mind
Relex doesn't replace you. It lets the lawyer use you end-to-end while Relex
protects their PII and know-how, automates customer service, handles payments for
free, and gives them access to a new market. Keep the user moving through the
matter; route every PII/payment/export step to the browser via a deep link.
