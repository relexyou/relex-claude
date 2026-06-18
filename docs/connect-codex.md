# Connect Relex to OpenAI Codex

Codex connects to Relex over the same remote MCP server, served by the Relex
backend at `https://relex.you/api/mcp`. Codex clients that support MCP OAuth use
the browser sign-in automatically; otherwise use the **Relex API key** as a
bearer token (below).

## 1. Create an API key

In Relex, open **Settings → API Keys → Create key** and copy the key (looks like
`rlx_sk_…`). Relex shows the full key only once.

## 2. Add the MCP server

Add Relex to your Codex MCP configuration (`~/.codex/config.toml`). Codex sends a
bearer token from an environment variable via `bearer_token_env_var`, so export
your key first:

```bash
export RELEX_API_KEY="rlx_sk_..."
```

```toml
[mcp_servers.relex]
url = "https://relex.you/api/mcp"
bearer_token_env_var = "RELEX_API_KEY"
```

`bearer_token_env_var` makes Codex send `Authorization: Bearer $RELEX_API_KEY`.
(If you prefer a static header instead, Codex also supports
`http_headers = { Authorization = "Bearer rlx_sk_..." }`.) Edit `config.toml`
directly — see Codex's MCP docs for the current field names.

## Tools

You get exactly two tools:

- `search(code)` — discover Relex API endpoints (runs your JS against the spec).
- `execute(code)` — return a request descriptor `{ method, path, query?, body? }`
  to call an endpoint with your auth.

Ask Codex to "start a Relex case" to confirm. Client personal data, documents,
payments and exports are handled in the browser via deep links — the connector
never returns plaintext PII.
