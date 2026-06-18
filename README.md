# Relex × Claude

Let a lawyer's **Claude** (Claude Code, Claude desktop / claude.ai "co-work", and
OpenAI **Codex**) operate inside a **Relex** legal case — **without ever
receiving PII**.

> Relex doesn't replace Claude. It helps you use Claude end-to-end by protecting
> your PII data and know-how, automating customer service, handling payments for
> you for free, and giving you access to a new market. See
> [`docs/positioning.md`](docs/positioning.md).

## How it works

Claude connects to a **remote MCP server** that exposes exactly two tools —
`search` and `execute` — with a fixed ~1k-token cost no matter how large the
Relex API is. `search({query,tag,method})` discovers endpoints from the OpenAPI
spec; `execute({method,path,query,body})` calls one — the server validates it
against the spec, applies the PII guard, and runs it with the user's auth.

That MCP server is **served by the Relex backend** at `https://relex.you/api/mcp`
(the SvelteKit `/api/*` proxy forwards `/api/mcp` → backend `/v1/mcp`). Auth is a
**browser sign-in over OAuth 2.1 + PKCE**: on the first tool call the server
returns an RFC 9728 challenge, the client opens the user's browser to sign in
with Google/Apple and approve, and a per-connection credential is provisioned —
**no key paste**. A static **Relex API key** (Settings → API Keys) works as a
CI/headless fallback. No separate service and no DNS to provision.

PII / party data / document content is **end-to-end encrypted** and only the
user's browser can decrypt it. `execute` **refuses** any call that would move
plaintext PII and instead hands the user a **deep link** to do it securely in the
Relex UI. The guarantee is enforced at the boundary, not by convention.

## Layout

```
relex-claude/
├── plugin/                     Claude Code plugin "relex-legal"
│   ├── .claude-plugin/plugin.json
│   ├── .mcp.json                Remote MCP connector (https://relex.you/api/mcp; OAuth sign-in)
│   ├── commands/                /relex-setup (guided onboarding) + /relex-connect
│   ├── skills/relex/SKILL.md    End-to-end PII-safe workflow (auto-loaded)
│   └── agents/relex-guide.md    Onboarding subagent
└── docs/
    ├── connect-claude-code.md
    ├── connect-claude-desktop.md
    ├── connect-codex.md
    └── positioning.md
```

The MCP handler itself (the `search`/`execute` tools, descriptor validation, and
the PII guard) lives in the **Relex backend** (`/v1/mcp`), not in this repo. This
repo is just the plugin + docs.

## Quick start

1. `/plugin marketplace add relexyou/relex-claude` then `/plugin install relex-legal@relex`.
2. Say *"set up my practice workflow with Relex"* — sign in in the browser (no key
   paste); Claude walks you through PII password → knowledge → auto-created
   encrypted parties → first case. Full guide:
   [`docs/install.md`](docs/install.md) (per-client:
   [`connect-claude-code.md`](docs/connect-claude-code.md),
   [`connect-claude-desktop.md`](docs/connect-claude-desktop.md),
   [`connect-codex.md`](docs/connect-codex.md)).
3. From then on, ask Claude to start cases, draft, and manage matters.
