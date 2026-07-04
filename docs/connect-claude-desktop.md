# Connect Relex to Claude desktop / claude.ai (co-work)

Use Relex as a **custom connector** in Claude desktop and on claude.ai (including
"co-work"). Sign-in is a **browser OAuth flow** — no key to paste. A static API
key works as a fallback (see the end).

## Add the connector

1. Open **Settings → Connectors** (claude.ai or the Claude desktop app).
2. Click **Add custom connector**.
3. Paste the MCP URL:
   ```
   https://relex.you/api/mcp
   ```
4. Click **Add** / **Connect**. The first time Claude uses it, it opens your
   browser to sign in to Relex with Google/Apple and approve — **no key paste**.
   The connector then shows **Connected** with the tools `search` and `execute`.

Then say *"set up my practice workflow with Relex"*.

### Fallback — API key (CI / headless)

If you prefer a static key instead of the browser flow: in Relex open
**Settings → API Keys → Create key** (shown once), and add it to the connector as
an HTTP header `Authorization: Bearer rlx_...`. OAuth stays the primary path — the
key is only a fallback.

## Use it

Ask: "Start a Relex case for me" or "Help me draft on my Relex case." Claude
works on the case structure and drafting; for anything involving client personal
data, documents, payment, or export it gives you a secure link to do it in the
browser.
