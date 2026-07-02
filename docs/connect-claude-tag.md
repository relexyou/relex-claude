# Connect Relex to Claude in Slack (@Claude)

Claude can join your Slack workspace as a teammate: tag **@Claude** in a channel
and it works there with the tools your admins connect, keeping a per-channel
memory. Connected to Relex, it can read, reason about, and draft on your legal
matters — while every client identity stays sealed. This is the same Relex MCP
server (`https://relex.you/api/mcp`) the other surfaces use; only the connection
point differs.

> Availability: Claude in Slack is an Anthropic **Team/Enterprise** capability and
> may be in beta for your plan. If you don't see it, it isn't enabled for your
> workspace yet — the Relex side is ready regardless.

## 1 — Add the Relex connector (workspace admin)

In your Claude organization's admin/connector settings, add a **custom MCP
connector**:

- **URL:** `https://relex.you/api/mcp`
- **Auth:** leave client id/secret blank — Relex uses **OAuth on connect**. When
  you authorize, your browser opens to sign in to Relex (Google or Apple) and
  approve; no API key to paste. The connection then acts as **you** (the admin who
  connected it), scoped to what your Relex account can see.

## 2 — Enable it on the right channels

Claude in Slack connects tools **per channel**. Turn the Relex connector on only
for the channels that should reach your matters — typically one channel per case
or per practice group. Start with a **private test channel** before a live matter.

## 3 — Bind each channel to its case

So Claude knows which matter a channel is about, put the case deep link where it
can find it:

- Pin the case link (`https://relex.you/dashboard/cases/{caseId}`) in the channel,
  or add it to the channel topic.
- The first time you tag @Claude, confirm the case once ("Working on «Acme
  dispute»?"). Claude keeps that binding in the channel's memory.
- A channel that spans several matters: share the case link in the thread you want
  worked, and Claude binds per-thread.

## What stays confidential

Claude in Slack legitimately learns your **workspace**: channels, threads, and
your teammates' real names. Relex holds the **case** ontology — who's who legally
— as sealed labels. The `relex-participants` skill keeps these apart:

- Sealed legal parties appear only as `[PARTY_NAME_1]`, `[PARTY_NAME_2]`, … with
  roles and descriptions — never a client's name, ID, or contact details.
- Practice members, guests, and partners appear as `[OWNER]`, `[MEMBER_n]`,
  `[GUEST_n]`, `[PARTNER_n]` — never a name, email, or photo.
- If a teammate types a client's real name in the channel, Claude keeps working in
  labels and points to the browser to view or edit the real identity. Reveal is
  always per-person, behind that person's own PII password — it never crosses into
  the channel or to the model.
- Any request that would move party PII, or fetch document content, is refused by
  the server with a deep link. That is the intended path, not an error.

## Audit & control

- The connection acts as the admin who authorized it, with a **scoped API key**
  you can see and revoke under **Relex → Settings → API keys**.
- Every call is in the Relex request logs, and in Slack under Claude's own admin
  activity log.
- Revoke access by removing the connector in the Claude admin console, or revoking
  the key in Relex — either cuts the channel off immediately.

## See also

- `docs/connect-claude-desktop.md` — the same connector for claude.ai / desktop.
- `docs/connect-claude-code.md` — the plugin + connector for Claude Code.
- The `relex-participants` and `relex` skills — the who-is-who protocol and the
  one PII rule Claude follows in every channel.
