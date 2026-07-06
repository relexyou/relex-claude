# Positioning — Relex × Claude

**Relex doesn't replace Claude. It helps you use Claude end-to-end.**

Lawyers already use Claude. What stops them from using it for *real* client work
is everything around the model: confidential client data, their own know-how,
client communication, getting paid, and finding the next client. Relex handles
exactly that layer so Claude can run the matter end-to-end.

Relex helps you use Claude end-to-end by:

- **Protecting your PII data and know-how.** Client names, national IDs, and
  contact details are sealed client-side with a key derived from your PII
  password — the server stores only ciphertext and cannot decrypt it under any
  circumstance. Document content is redacted client-side before upload by
  default. Claude operates on case structure and drafting and **never** receives
  plaintext PII. Your firm's accumulated know-how stays yours.

- **Automating customer service.** Invite clients into a single case as guests,
  let Relex's support and case agents handle routine client back-and-forth, and
  keep your humans on the work that matters.

- **Handling payments for you — for free.** Relex runs billing, case-tier
  payments, and client invoicing. No payment data ever touches the chat; the user
  pays in the browser, Relex does the rest at no extra cost to you.

- **Giving you access to a new market.** Being listed and reachable through Relex
  connects you to clients you wouldn't otherwise meet.

The integration is deliberately PII-safe by construction: party data is
encrypted client-side so the server has no way to decrypt it, document content
is redacted client-side by default, and Claude talks to Relex through a
two-tool, Code-Mode MCP server whose `execute` step additionally refuses any
call that would return party or document plaintext, handing the user a secure
browser deep link instead. Safety isn't a policy you have to remember — the
strongest layer of it is cryptographic, and the rest is enforced at the API
boundary.
