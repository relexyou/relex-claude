# Connect Relex to Claude Code

The Relex MCP server is served by the Relex backend at `https://relex.you/api/mcp`.
The default auth is a **browser sign-in over OAuth** — no key to paste. A static
API key works as a CI/headless fallback (Option C).

## Option A — install the plugin (recommended)

The `relex-legal` plugin bundles the connector, the workflow skill, the
`/relex-setup` and `/relex-connect` commands, and an onboarding agent.

```
/plugin marketplace add relexyou/relex-claude
/plugin install relex-legal@relex
```

Reload when prompted (or restart Claude Code), then say in a chat:

> set up my practice workflow with Relex

Claude makes its first tool call, the server returns an OAuth challenge, and your
browser opens to sign in with Google/Apple and approve — **no key paste**. Claude
then walks you through your PII password, knowledge, auto-created encrypted
parties, and first case (the `/relex-setup` flow).

## Option B — add the MCP server directly (OAuth)

```bash
claude mcp add --transport http relex https://relex.you/api/mcp
```

No `--header`: on first use, Claude Code discovers the OAuth authorization server
(via the RFC 9728 `WWW-Authenticate` challenge) and runs the browser sign-in.

## Option C — API key fallback (CI / headless)

In Relex, **Settings → API Keys → Create key** (shown once), then:

```bash
claude mcp add --transport http relex https://relex.you/api/mcp \
  --header "Authorization: Bearer rlx_..."
```

## Verify

```
/mcp        # shows `relex` connected, with tools: search, execute
```

Then ask Claude to "set up my practice workflow with Relex" or "start a Relex
case" — it should call `search` then `execute`.
