---
description: Set up your Relex practice workflow — sign in, set your PII password, add your know-how, and let Relex auto-create your encrypted parties.
---

# /relex-setup

The user said something like *"set up my practice workflow with Relex"*. Run the
guided, deep-link-first onboarding. Drive it from the live status endpoint — never
guess where the user is. Follow the PII discipline in the `relex` skill at every
step (PII, documents, payments, and exports happen in the browser, never in chat).

## How to drive it

1. **Make sure you're connected.** Issue any tool call (e.g. the status read in
   step 2). If you are not signed in, the Relex MCP server replies with an OAuth
   challenge and your client opens the user's browser to sign in with Google or
   Apple and approve access — **no key paste**. Tell the user: "A browser window
   will open — sign in to Relex and approve, then come back." Wait for them.

2. **Read progress** with `execute` → `GET /onboarding/status`. It returns only
   anonymized counts + flags + deep links (never PII):
   `{ connected, piiConfigured, knowledge:{total,indexed,processing,awaitingParties,failed},
      detectedParties, parties:{count}, nextStep, deepLinks:{pii,knowledge,parties,cases} }`.
   Use `nextStep` to decide what to do, then re-read after the user acts.

3. **Act on `nextStep`** (one step at a time, wait for the user, then re-read status):

   - `set_pii_password` → "First, let's protect the personal data in your matters.
     Open **{deepLinks.pii}**, set a password, and save your recovery key. It
     encrypts every name, ID, and document in your browser — I only ever see
     labels like `[Party 1]`." Wait, then re-read status.

   - `add_knowledge` → "Now add your know-how. Open **{deepLinks.knowledge}** and
     upload your playbooks, templates, and past matters. Relex indexes them
     privately and reads out the parties it finds." Wait, then re-read status.

   - `processing` → indexing/OCR is still running. Tell the user it's processing,
     wait a bit, and re-read status. Don't loop aggressively — check back when
     they say they've uploaded, or after a short pause.

   - `finish_parties` → Relex found parties in the knowledge but they aren't
     created yet (PII is probably locked). "Open **{deepLinks.knowledge}** with
     your PII password unlocked — Relex will auto-create the {detectedParties}
     parties it found, encrypted in your browser." Wait, then re-read; confirm
     `parties.count` went up.

   - `create_case` → setup is done. Confirm: "You're set up — {parties.count}
     parties are encrypted and ready, and your know-how is indexed. Want me to
     start your first case?" If yes, `execute` → `POST /cases` `{ name, caseTier }`
     (see the `relex` skill). If it returns `402`, deep-link **{deepLinks.cases}**
     / billing to pay.

   - `ready` → everything's set; move on to real case work via the `relex` skill.

4. **Report progress in the chat** as you go (e.g. "✅ PII password set",
   "✅ 4 parties created from your knowledge") using the anonymized counts — never
   echo a name or ID. If a step stalls, hand the user the relevant deep link again
   and wait.

Keep it warm and short. The whole point: the user logs in once, and you walk them
through a private setup where their know-how powers the work and their clients'
identities never leave their browser.
