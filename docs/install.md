# Install Relex for Claude

Relex lets you use Claude end-to-end on your legal matters **without ever exposing
client PII**. You install one plugin, sign in once in your browser, and Claude
sets up your whole practice workflow — your know-how powers the drafting, and your
clients' names, IDs, and documents stay encrypted in your browser.

## Claude Code (recommended)

1. **Add the Relex marketplace** (one time):

   ```
   /plugin marketplace add relexyou/relex-claude
   ```

2. **Install the plugin:**

   ```
   /plugin install relex-legal@relex
   ```

   Reload when prompted (or restart Claude Code).

3. **Set up your practice workflow.** In a chat, just say:

   > set up my practice workflow with Relex

   Claude opens your browser to **sign in with Google or Apple** and approve
   access — there is **no key to paste**. Then it walks you through:

   1. **Set your PII password** — encrypts every client name, ID, and document in
      your browser. Claude only ever sees labels like `[Party 1]`. (Save your
      recovery key.)
   2. **Add your know-how** — upload your playbooks, templates, and past matters.
      Relex indexes them privately.
   3. **Auto-create parties** — Relex extracts the people and companies from your
      know-how and creates them as **encrypted** parties, in your browser. Claude
      sees only the count, never the identities.
   4. **Start your first case.**

That's it. From then on, ask Claude to start cases, draft, and manage matters —
it routes anything PII-bearing (parties, documents, payments, exports) to your
browser via secure deep links.

## Claude Desktop / claude.ai

Add a custom connector:

- **Settings → Connectors → Add custom connector**
- URL: `https://relex.you/api/mcp`

Sign-in is automatic (OAuth) the first time Claude uses it. Then say *"set up my
practice workflow with Relex"* as above. See `connect-claude-desktop.md`.

## OpenAI Codex

Add an MCP server pointing at `https://relex.you/api/mcp`. Codex clients that
don't drive OAuth use the **API-key fallback** below. See `connect-codex.md`.

## Fallback — connect with an API key (CI / headless / no-OAuth clients)

1. In Relex: **Settings → API Keys → Create key** and copy it (shown once).
2. Add the server with the key as a bearer token:

   ```bash
   claude mcp add --transport http relex https://relex.you/api/mcp \
     --header "Authorization: Bearer rlx_..."
   ```

You can revoke any connection anytime in **Settings → API Keys** (revoking an
OAuth connection also ends its sign-in session) or unpair clients in
**Settings → Agents**.

## How your data is protected

- Claude signs in to **your** Relex account; every call runs as you.
- Client PII — names, national IDs, contacts, document content — is end-to-end
  encrypted under your PII password and **only ever decrypted in your browser**.
- The API refuses any call that would move plaintext PII and hands back a browser
  deep link instead. Claude works with de-identified labels (`[Party 1]`) and
  anonymized counts.
- Your know-how is searched through a private, per-tenant index — never copied to
  a model and never used for training.
