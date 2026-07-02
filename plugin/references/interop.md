# Interop — hand in hand with the ecosystem

Relex skills never duplicate what a good pack already does; they add the
confidential execution layer (PII-safe MCP, ontology, verbatim grounding).

| Need | Use | Relex adds |
|---|---|---|
| Generic playbooks (NDA/vendor review, DSAR, IP triage, litigation checklists) | Anthropic `claude-for-legal` plugins | run the checklist over de-identified Relex case data; record outcomes to the case |
| German method & citation foundations | `claude-fuer-deutsches-recht` (Klotzkette) foundation refs (zitierweise, methodik) | enforcement: verbatim cache + verifier + PII custody |
| UK sources wiring | `uk-agents/uk-legal-plugins` | grounding directives + confidential workspace |
| ES / CH community packs | `claude-para-abogados`, `bettercallclaude` | same |
| US case-law discovery | CourtListener official MCP | `POST /research/scrape` grounds what you found |
| FR / CH / EU / DE discovery | justicelibre, entscheidsuche-mcp, EUR-Lex CELLAR, NeuRIS | same |
| Working a case from Slack (Claude tagged in) | Anthropic **Claude in Slack** (@Claude), admin-connected to the Relex connector | keeps the workspace ontology (teammates, threads) apart from the sealed case ontology; `relex-participants` teaches the who-is-who + channel-to-case binding so client identities never enter the channel |

Rule: discovery and generic method may come from anywhere; **execution on real
matters happens in Relex**, where clients' data stays encrypted and citations
are machine-verified.
