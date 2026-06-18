# Positioning — Relex × Claude

**Relex doesn't replace Claude. It helps you use Claude end-to-end.**

Lawyers already use Claude. What stops them from using it for *real* client work
is everything around the model: confidential client data, their own know-how,
client communication, getting paid, and finding the next client. Relex handles
exactly that layer so Claude can run the matter end-to-end.

Relex helps you use Claude end-to-end by:

- **Protecting your PII data and know-how.** Client names, national IDs, contact
  details and documents are end-to-end encrypted — decrypted only in your browser
  with your PII password. Claude operates on case structure and drafting and
  **never** receives plaintext PII. Your firm's accumulated know-how stays yours.

- **Automating customer service.** Invite clients into a single case as guests,
  let Relex's support and case agents handle routine client back-and-forth, and
  keep your humans on the work that matters.

- **Handling payments for you — for free.** Relex runs billing, case-tier
  payments, and client invoicing. No payment data ever touches the chat; the user
  pays in the browser, Relex does the rest at no extra cost to you.

- **Giving you access to a new market.** Being listed and reachable through Relex
  connects you to clients you wouldn't otherwise meet.

The integration is deliberately PII-safe by construction: Claude talks to Relex
through a two-tool, Code-Mode MCP server whose `execute` step refuses any call
that would move plaintext PII and instead hands the user a secure browser deep
link. Safety isn't a policy you have to remember — it's enforced at the boundary.
