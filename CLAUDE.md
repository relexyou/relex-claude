# relex-claude

The public Claude plugin for Relex (`plugin/` — skills, agents, commands,
references) plus docs. It teaches Claude the PII-safe, deep-link-first workflow
over the Relex MCP server. There is no build step; the deliverable is the
markdown itself.

## Checks

```bash
python3 -c "import json;json.load(open('plugin/.claude-plugin/plugin.json'))"  # manifest valid
grep -rn "relex.you/api" plugin/ | head   # endpoints must match the live MCP surface
```

## Non-negotiables

- **Every content change bumps `plugin/.claude-plugin/plugin.json` version** —
  installed plugins only pick up updates on a version change.
- **Verify against the backend, not memory.** Any endpoint, steering-block key,
  onboarding field, or deep link mentioned in a skill must exist in
  `relex/backend/functions/src/mcp_openapi.yaml` / `mcp_server.py` and the
  frontend routes at the time of writing.
- **PII claims must be exact.** Never overstate ("Claude never sees X" only when
  the backend actually enforces it). Verification internals (`verified_ai`,
  screening method) are never mentioned.
- **No pricing/cost-control details** in skills or tool descriptions.
- **Claude is the steering layer, not an unattended actor**: skills teach
  branch/conclude and deep-link handoffs into Relex for anything involving raw
  PII (parties, documents, payments).
