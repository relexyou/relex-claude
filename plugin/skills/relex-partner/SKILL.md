---
name: relex-partner
description: Use to guide a lawyer or firm through joining the Relex partner program — the registration that lets them charge their own clients (engagement fees and invoices) through their own Stripe account. Teaches the whole process — profile and credentials, the program subscription, payment onboarding, then manual Relex verification and going live. Explains the states (pending, verified, published) and when client invoicing unlocks. Process guidance only; the user enters details and pays in their browser.
---

# Joining the Relex partner program

Registering as a partner is what lets a firm **charge its own clients** — issue an
engagement fee or invoice that the client pays by card, straight to the firm.
Relex never holds that money: registration provisions the firm's **own** payment
account, and client charges go directly to it. So client invoicing and paid guest
intake stay locked until the firm is a verified, published partner.

You **guide** the process; the user does every step that touches their details or
payment **in their browser**. Point them to the right page and explain what each
step is for. You never enter their credentials, bank details, or rates.

## The path (point the user to each step)

1. **Register** — `https://relex.you/partners/register` (a short wizard):
   - Profile: name, type (lawyer / notary / specialist), photo, bio, region.
   - Legal details: bar/registration number, regulator, admission region.
   - Proof of standing: upload a licence/registration document.
   - Consent: agree to the partner terms + screening.
   - Rate card: the firm sets its own fees (you don't set or quote these).
2. **Program subscription** — completed inside the wizard: the firm starts the
   partner-program subscription and adds a payment method. This is a prerequisite
   for the next step.
3. **Payment onboarding** — the wizard hands off to set up the firm's payment
   account (identity + bank details, entered on the processor's secure pages).
   Track progress at `https://relex.you/dashboard/settings/partner/status`.
4. **Manual Relex verification** — once submitted, a Relex reviewer checks the
   firm's standing (they receive the registration for review). The firm's status
   shows **pending verification** meanwhile. Nothing the user can do but wait.
5. **Published / live** — after Relex verifies and publishes the firm, it is
   **active**: it appears in the partner directory and can now issue client
   invoices and run paid guest intake.

## The states — read them back to the user

- **pending** — registered, awaiting Relex verification. Client invoicing is
  locked. Check `…/settings/partner/status`.
- **verified (not yet published)** — Relex confirmed standing; the firm is one
  step from live. Still awaiting the publish.
- **active / published** — live. Client invoicing + paid guest intake unlocked.

If the firm tries to invoice a client before this, the server refuses with a link
to finish registration or check verification status — relay that link; it's the
correct path, not an error.

## What to tell the user

- Why it's needed: to charge clients directly, the firm needs its own registered,
  verified payment identity — that's the partner program.
- The order matters: subscription → payment onboarding → verification → publish.
  Each unlocks the next; skipping isn't possible.
- Verification is done by a person at Relex, so there's a short wait after
  submitting — that's expected.
- Everything sensitive (documents, bank details, rates, card) is entered by the
  user in their browser. You never handle it.

## What NOT to do

- Never quote or set the firm's fees, or Relex's own prices — the firm sets its
  rate card; you don't advise amounts.
- Never enter the user's credentials, bank details, or payment info — always the
  browser.
- Don't promise a verification timeline or outcome — it's a manual review.
- Don't retry a "registration required" / "pending verification" refusal — relay
  the link.

## Alongside

- `relex-intake` — once live, the end-to-end client intake (agreement → e-sign →
  invoice) and paid guest onboarding.
- `relex` — connect, the two tools, the one PII rule.
