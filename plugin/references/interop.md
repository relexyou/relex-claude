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

Rule: discovery and generic method may come from anywhere; **execution on real
matters happens in Relex**, where clients' data stays encrypted and citations
are machine-verified.
