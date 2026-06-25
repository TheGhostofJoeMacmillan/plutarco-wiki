# Roplotica Security Fixes — June 25, 2026

## Context
6 orders appeared (4 spam from today, 2 from May). All pending_payment, no money received. Triggered full audit.

## Wallets (both Phillip's)
- **Solana**: `4UuBL55iT5HVpvfnFBreSrLRKg22jCaRqbswaGqBCkYi` — Phillip's Phantom wallet
- **Base**: `0xf523DEb77bBf257F69D669443F4B1Ae8bea5Be3B` — Phillip's Phantom/Base wallet
- Originally Solana was `Gnr8T2avMvLQ2VVFe2CAnR32AQWyVQFCdyEoxpwMGVDy` (changed during ClawPlot→Roplotica rebrand in April)
- Private keys are in Phillip's wallet apps, never stored on server (good)
- Solana wallet has 1 incoming tx ever (Feb 16, 1 USDC, not tied to any order)
- Base wallet is completely empty, never received anything

## Email
- MX → ImprovMX (mx1.improvmx.com, mx2.improvmx.com)
- SPF: `v=spf1 include:spf.improvmx.com ~all`
- Forwarding: `hello@` and `api@` → `pltco.ink@gmail.com` (set up Feb 2026)
- Site currently shows `orders@roplotica.com` — needs verification this alias is configured in ImprovMX
- Phillip set up ImprovMX under pltco.ink@gmail.com account

## Security Fixes Applied (deployed June 25)

### 1. PII Exposure (FIXED)
- Status API (`/api/status`) no longer returns shipping name/address
- Only returns: order ID, status, payment info, order details (size/paper/ink)

### 2. Rate Limiting (FIXED)
- 5 orders per minute per IP, then 429 response
- In-memory rate limit map (per Vercel instance)

### 3. Bot Detection (FIXED)
- Honeypot field (`website` — if filled, bot)
- Fake name detection (test, fake, bot, asdf, john doe, jane doe)
- Fake address detection (123 apple, 456 banana, etc.)
- SVG size check (< 100 chars = test/empty)
- Bots get fake success response (no data stored) — don't tip them off

### 4. Blob Storage Privacy (FIXED)
- Order metadata JSON no longer stored as `access: 'public'`
- Now defaults to private (only accessible via signed URL from server code)
- SVGs remain public (needed for plotting preview)

### 5. Stripe Env Vars Removed
- STRIPE_SECRET_KEY, STRIPE_PUBLISHABLE_KEY, STRIPE_WEBHOOK_SECRET removed from Vercel
- GMAIL_USER, GMAIL_APP_PASSWORD also removed (unused)

## Remaining Items
- Can't delete old fake/spam orders from Vercel Blob (no delete API). They'll sit as pending_payment forever, harmless.
- `orders@roplotica.com` alias needs verification in ImprovMX dashboard
- DMARC record not configured (`_dmarc.roplotica.com` has no TXT record)
- Consider adding DMARC for email deliverability
- The 2 Maja Lindberg orders from May are potentially real interest — same person ordered twice but never paid
