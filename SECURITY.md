# Security

Relex lets you use Claude end-to-end on your legal matters **without exposing
client PII to the model**. This document describes the security posture of the
`relex-legal` plugin and how to control access.

## Authentication

- The plugin connects to the hosted Relex MCP server at
  `https://relex.you/api/mcp`. On first use it performs a **browser sign-in over
  OAuth 2.1 with PKCE** (Google or Apple) — you authenticate to your own Relex
  account; **there is no key to paste**.
- The access token issued to the agent is a per-connection credential scoped to
  your account. Revoke it anytime in Relex under **Settings → API Keys**
  (revoking also ends the connection); paired clients are listed under
  **Settings → Agents**.
- A static API key is supported as a CI/headless fallback. Treat it like a
  password; revoke it the same way.

## Client PII never reaches the model

- Party data — names, national IDs, contact details — is **sealed client-side**
  with a key derived from your PII password. The server stores only ciphertext
  and **cannot decrypt it under any circumstance**: this is a cryptographic
  guarantee, not a policy choice. Your password never leaves your browser.
- Document content is redacted client-side before upload by default. Claude
  never receives document content either way.
- The MCP server's agent-facing API additionally **blocks** any endpoint that
  would return party or document plaintext (party reads/writes,
  document/attachment content, uploads) and instead returns a deep link so you
  complete that step securely in the browser.
- Claude works only with de-identified labels (e.g. `[Party 1]`) and anonymized
  counts. Your know-how is searched through a private, per-tenant index — never
  copied to a model and never used for training.

## This repository

- The plugin ships **no credentials or secrets**. It only declares the public
  MCP endpoint; you authenticate yourself at runtime.
- The MCP tools (`search`, `execute`), descriptor validation, and the PII guard
  run server-side in the Relex backend, not in this repo.

## Reporting a vulnerability

Please report security issues privately to **security@relex.you**. Do not open a
public issue for a suspected vulnerability.
