# Connect Relex to Claude desktop / claude.ai (co-work)

Use Relex as a **custom connector** in Claude desktop and on claude.ai (including
"co-work" and mobile once connected). Sign-in is a **browser OAuth flow** — no
key to paste. A static API key works as a fallback (see the end).

**MCP URL:**

```
https://relex.you/api/mcp
```

## Which plan do you have?

| Plan | Who adds the custom connector | Who clicks Connect |
|------|-------------------------------|--------------------|
| **Pro / Max** (personal) | **You** | **You** |
| **Team / Enterprise** | **Owner or admin** (once, for the organisation) | **Each member** (for their own Relex account) |

Members on Team / Enterprise **cannot** add custom connectors themselves. If
you only see “available connectors” and no “Add custom connector”, you are on a
managed plan — ask your admin.

---

## Pro / Max (personal)

1. Open **Customize → Connectors** (or **Settings → Connectors**) in claude.ai
   or the Claude desktop app.
2. Click **Add custom connector**.
3. Name it **Relex**. Paste the MCP URL:
   ```
   https://relex.you/api/mcp
   ```
   Leave OAuth client id/secret blank unless instructed otherwise.
4. Save, then click **Connect**. Your browser opens to sign in to Relex with
   Google/Apple and approve — **no key paste**.
5. The connector shows **Connected** with tools `search` and `execute`.

Then say: *"set up my practice workflow with Relex"*.

---

## Team / Enterprise

### Admin / owner — install once

1. Sign in as a workspace **owner or admin**.
2. Open the **organisation’s settings → Connectors** (admin / org connectors,
   not only your personal Customize menu).
3. **Add custom connector**:
   - Name: **Relex**
   - URL: `https://relex.you/api/mcp`
4. Save and make it available to members (publish / enable per your Claude org UI).
5. Tell the team: *“Relex is under Customize → Connectors — click Connect and
   sign into your Relex account.”*

Admin install only makes the connector **visible**. It does **not** sign members
into Relex.

### Member — connect your account

1. Open **Customize → Connectors**.
2. Find **Relex** under **available connectors** (already installed by admin).
3. Click **Connect** → complete the Relex browser OAuth for **your** account.
4. Say: *"set up my practice workflow with Relex"*.

| If you see… | Meaning | What to do |
|-------------|---------|------------|
| Relex listed, not connected | Admin installed; you have not authorized | Click **Connect** |
| No Relex at all | Admin has not added it (or not published to your group) | Ask admin |
| No “Add custom connector” | Team policy — only admins install | Expected; use Connect on available list |
| Connect fails / popup blocked | Browser blocked OAuth | Allow popups; retry |

---

## Fallback — API key (CI / headless)

If you prefer a static key instead of the browser flow: in Relex open
**Settings → API Keys → Create key** (shown once), and add it to the connector as
an HTTP header `Authorization: Bearer rlx_...`. OAuth stays the primary path —
the key is only a fallback.

## Use it

Ask: "Start a Relex case for me" or "Help me draft on my Relex case." Claude
works on the case structure and drafting; for anything involving client personal
data, documents, payment, or export it gives you a secure link to do it in the
browser.
