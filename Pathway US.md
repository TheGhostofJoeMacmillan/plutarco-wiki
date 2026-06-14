# Pathway US

> *Immigration lead generation: EU → US corridor. Live at pathway-us.vercel.app*

---

## What It Is
Pay-per-lead service connecting European nationals with US immigration attorneys. We capture qualified leads through a targeted landing page and deliver them exclusively to our partner firm.

**Status:** Site live, form working, Telegram notifications active. 5 items pending before full launch.

---

## Partner Firm
**Law Offices of Foroozandeh, APC**
- **Founded:** 2007
- **Location:** Laguna Hills, California (Orange County)
- **Lead Attorney:** Majid Foroozandeh, ME, MBA, JD — Admitted 2007, 9th Circuit, ED/CD/SD CA
- **Of Counsel:** John Allen Nelson, Esq. — Immigration Law, all 50 states (8 USC 1292.1)
- **Specialties:** E-2, Business Immigration, O-1, Civil Litigation, Family-Based, Asylum
- **Language:** English and Farsi

---

## Pricing (USD — finalized June 14)

| Lead Type | Intro (3 mo) | Standard | Volume (20+/mo) |
|-----------|-------------|----------|-----------------|
| E-2 / EB-1 / O-1 (Business & talent) | $275 | $425 | $375 |
| L-1 / H-1B / EB-2 NIW (Corporate & employment) | $225 | $325 | $275 |
| Family-based (Marriage, K-1, adjustment) | $175 | $225 | $200 |

**Comparison:** Google Ads = $50-150/click (unqualified), Avvo = $200-500/mo (shared). We = $275-425/lead (exclusive, pre-qualified).

**Market context:** Legal services average CPL is $649 blended. Immigration exclusive leads go $75-90 (generic) to $150-500 (premium/pre-qualified). Our pricing sits in the premium range for the EU→US niche.

---

## Site Architecture

**URL:** pathway-us.vercel.app
**Vercel Project ID:** prj_u6e6mIMBo4KvJ4PFQWyKXXWuAVpq
**Code:** ~/projects/immigration-leads/

### Pages
- `/` — Landing page with hero, visa cards, assessment form, advertising disclosures
- `/privacy` — GDPR-compliant privacy policy
- `/terms` — Terms of service (advertising service, not referral)
- `/thank-you` — Post-submission confirmation

### API
- `POST /api/submit` — Validates fields, sends Telegram notification, stores in Vercel Blob
- Validates: name, email format, nationality, visa type required
- Returns: `{success, leadId, notification, storage}`

### Key Features
- Cookie consent banner (localStorage-based)
- Advertising disclosure section (4-step explainer)
- 17 EU nationalities in form dropdown
- Visa cards clickable → pre-fill form + scroll
- Clean URL routing (vercel.json cleanUrls)

---

## Launch Checklist

### ✅ Done
- [x] Landing page live
- [x] Form API working with validation
- [x] Telegram notifications (sends to Phillip's DM, chat ID 7558955416)
- [x] Privacy, Terms, Thank-you pages
- [x] Cookie consent banner
- [x] Advertising disclosure section
- [x] PDF proposal (USD pricing, verified)
- [x] Vercel env vars: TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID

### 🔲 Pending (at computer)
1. **Link Vercel Blob Store** (~2 min) — Vercel dashboard → Storage → link `pathway-us-leads`. Creates BLOB_READ_WRITE_TOKEN. Without this, leads only go to Telegram.
2. **Email Setup** (depends on domain) — Need Gmail App Password for whichever account we use. Add as GMAIL_USER + GMAIL_APP_PASSWORD env vars. Enables confirmation emails to leads + notification emails to firm. Decision: use pltco.ink@gmail.com or create new email? Domain choice affects this.
3. **Telegram Channel** (~5 min) — Create private channel, add Hermes bot as admin, update TELEGRAM_CHAT_ID. Keeps lead alerts separate from our chat.
4. **End-to-End Test** (~5 min) — Submit test lead, verify notification, check all pages.
5. **Domain Purchase** (when ready) — pathway-us.com available. Phillip said not yet. May choose different domain.

---

## PDF Proposal
- **File:** ~/projects/immigration-leads/presentation.html (WeasyPrint/Playwright source)
- **PDF output:** ~/projects/immigration-leads/pathway-us-proposal.pdf
- **5 pages:** Cover, Opportunity + How It Works, Visa Pathways, Legal Structure + Pricing, Firm + Live Site + CTA
- **Last updated:** June 14, 2026 (pricing converted to USD, market data verified)

---

## Broader Vision
Phillip sees this as the first vertical of a **pay-per-lead business**. Future verticals could include:
- Portugal real estate / golden visa leads
- US business formation for EU entrepreneurs
- Crypto/Web3 legal leads
- Personal injury, DUI, criminal defense (highest CPL)

Each vertical gets its own consumer-facing site. One shared backend. Parent brand TBD.
