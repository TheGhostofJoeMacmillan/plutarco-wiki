# FieldWriter

> *Minimalist AI writing app — AI assists without overwriting. fieldwriter.ai*

---

## What It Is
The anti-AI writing tool. AI assists your writing without overwriting it. You stay the author.

**Status:** Built (v60), needs business wrapped around it.

---

## Key Features
- BYOK (Bring Your Own Key) — user supplies their own API key
- PWA — works offline, installable
- AI assists — doesn't rewrite, suggests
- Minimalist interface — focus on writing
- Pro tier with monthly credit budget (300-700 cents)

---

## Location
`~/projects/fieldwriter/` — Full v2 source code

---

## Technical Details
- **Source of truth:** `bundle-readable.js` (bundle.js gets overwritten on deploy)
- **Deploy:** `bash deploy.sh` or `cp bundle-readable.js bundle.js && vercel --prod --yes`
- **Vercel project:** `fieldwriter-v2`, domain: `fieldwriter.ai`

### Key Code Locations
- **Plan mode prompt:** `Hn()` function at line ~2283 — currently too deliberative/verbose
- **Base system prompt:** `Re` variable at line ~825
- **Pro model allowlist:** `api/ai-proxy.js` — `ALLOWED_MODELS` (only 3 entries currently)
- **Pro model costs:** Gemini Flash $0.15/$0.60, Gemini Pro $1.25/$5.00, Claude Sonnet $3.00/$15.00

---

## Known Issues
- Plan Mode too deliberative — needs to act like a writing partner, not an analyst
- Pro model selection limited — needs GLM and cheaper writing-friendly models added to ALLOWED_MODELS
- No pricing page
- No payment integration
- No marketing/launch plan

---

## Business Status
- **Highest SaaS ceiling** in our portfolio
- Domain: fieldwriter.ai
- Monday focus day in the weekly rotation
