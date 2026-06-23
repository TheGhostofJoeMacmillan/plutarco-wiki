# Portugal Real Estate — Legal & Business Research

**Date:** 2026-06-22
**Status:** Initial research complete. Legal consultation recommended before action.

## The Core Question: Can Phillip work in Portuguese real estate on a D8 visa?

**Short answer: Not directly as a licensed agent. The D8 restricts you to foreign-sourced income.**

### D8 Visa Restrictions
- The D8 (Digital Nomad Visa) is specifically for remote workers earning income from **outside Portugal**
- It does **NOT** grant the right to take up local employment or local self-employment in Portugal
- Working as a real estate agent serving the Portuguese local market = local self-employment = **visa violation**
- To work locally, you'd need a different visa pathway (D2 entrepreneur, or work permit via employer)

### AMI License (Agência de Mediação Imobiliária)
- **Mandatory** for anyone acting as a real estate mediator in Portugal
- Issued by **IMPIC** (Instituto dos Mercados Públicos, do Imobiliário e da Construção)
- Issued to **companies**, not individuals — agents work under a company's AMI license
- **Requirements:**
  - No criminal record
  - €150,000 civil liability insurance
  - Commercial suitability
  - **No formal real estate education or exam required** (low barrier!)
- Must display AMI number on all advertising, contracts, listings
- Operating without AMI = illegal, fines, no consumer protection
- Verify at: [impic.pt](https://www.impic.pt/impic/)

### Commission Structure
- Seller pays commission (typically 3-8%, average ~5% + 23% IVA)
- No MLS in Portugal — portals (Idealista, Imovirtual) are advertising channels
- Commission splitting between agencies is common
- No formal "buyer's agent" profession exists
- Open mandates (multiple agencies list same property) are the default

## What Phillip CAN Do Right Now (on D8 visa, no AMI license)

### 1. Property Listing Website / Aggregator ✅
- Build a site that aggregates or curates Porto listings
- No AMI needed — you're a platform, not a mediator
- Can monetize via ads, premium listings, lead generation
- Legal risk: Must NOT present yourself as an agent or facilitate transactions

### 2. Social Media / Content Marketing ✅
- YouTube, Instagram, TikTok about Porto real estate
- "House tours," neighborhood guides, market analysis
- Monetize via content revenue, sponsorships, affiliate
- No license needed for content creation

### 3. Referral Arrangements ⚠️ (Gray Area)
- Introduce foreign buyers to licensed Portuguese agencies
- Receive a "finder's fee" or referral commission
- Legal gray area: if you're just making introductions, arguably OK
- If you're "mediating" (facilitating negotiations, showing properties), you need AMI
- **Recommend:** Formal referral agreements with AMI-licensed agencies, structured as marketing/consulting fees paid to a foreign entity

### 4. Consulting for AMI-Licensed Agencies ⚠️
- Work as a marketing consultant / international client specialist
- Income would need to come from foreign entity (your US company?), not directly as Portuguese self-employment
- Could structure as B2B contract between your foreign company and the Portuguese agency

## What Phillip Would Need to Do It Officially as a Licensed Agent

### Option A: Work for an AMI-Licensed Agency
- Get hired by an existing agency (e.g., Berkshire Hathaway Portugal, Porterford, etc.)
- Would need a **work visa** (not D8) — employer sponsors residency
- Or convert D8 to work permit if possible (check with immigration lawyer)
- Agent works under company's AMI — no individual license needed

### Option B: Register Own Agency with AMI License
- Register a Portuguese company (Lda)
- Apply for AMI license through IMPIC
- Would need **D2 entrepreneur visa** or similar that allows local self-employment
- Requirements: business plan, capital, AMI application, insurance
- D8 → D2 conversion may be possible (consult lawyer)

### Option C: Wait for Permanent Residency (5 years)
- After 5 years of legal residency, apply for permanent residency
- Permanent residency = full work rights, no restrictions
- Then get AMI license or work for any agency
- Long play, but eventually full freedom

## Recommended Path (Pragmatic)

1. **Phase 1 (Now, on D8):** Build content + platform
   - Start social media (Instagram/YouTube) focused on Porto real estate
   - Build a curated listing site (aggregate from Idealista/Imovirtual APIs or manual curation)
   - Build audience and brand as "the English-speaking Porto real estate resource"

2. **Phase 2 (3-6 months):** Referral partnerships
   - Approach 2-3 AMI-licensed agencies in Porto
   - Propose referral agreements: you bring foreign buyers, they handle transactions
   - Structure as consulting/marketing fees to foreign entity

3. **Phase 3 (when ready):** Go official
   - Consult immigration lawyer about visa adjustment (D8 → D2 or work permit)
   - Either get hired by an agency OR register own company + AMI license
   - Full legal operation as a real estate professional

## Key Contacts / Resources
- IMPIC: https://www.impic.pt/impic/ — AMI license verification and application
- ASMIP: Association of Real Estate Agents of Portugal
- Idealista.pt, Imovirtual.com — main listing portals
- Recommended: Consult an immigration lawyer for visa conversion options

## Website — LIVE
- **URL:** https://porto-realestate.vercel.app
- **Location:** ~/projects/porto-realestate/ on VPS
- **Stack:** Pure HTML/CSS/JS + Vercel serverless API
- **Lead capture:** POST /api/lead → Telegram notification to Phillip ✅
- **Vercel Blob:** Store needs to be created in dashboard + BLOB_STORE_ID env var added, then redeploy to persist leads
- **Idealista API:** Apply at developers.idealista.com/access-request — pending Phillip's application
- **Domain:** Not yet purchased. Need to pick one.

## Visa Update (2026-06-22, revised 2026-06-23)
- Bea has D2 entrepreneur visa → Phillip is likely on D6 family reunification (spouse of D2)
- D6 grants FULL work rights in Portugal — including self-employment
- D8 digital nomad restrictions do NOT apply to Phillip
- **Phillip should verify his exact visa type on his residency card** — he's unsure if it's D6 or something else
- If all three (Bea, Phillip, child) applied together at the consulate with Bea as primary D2 applicant, Phillip would be D6 dependent
- Key: whatever the visa type, as spouse of D2 holder, Phillip has full work rights
- Existing Lda can potentially be used — just add CAE 68311 (real estate mediation)
- AMI license requires Título de Residência (residency card), not just visa
- AMI exam is in Portuguese only — need B1/B2 level
- Total AMI cost: ~€700-1,400, timeline 3-6 months from residency card

## Site Update (2026-06-23)
- Added personal story section ("We Moved From California to Porto")
- Added services/differentiation section (video walkthroughs, neighborhood reality checks, trusted agents, move-from-abroad guide)
- Updated hero copy to be personal: "We Moved Here. Now We Help You Do the Same."
- Updated How It Works to mention video walkthroughs and neighborhood profiles
- Updated contact form placeholder and benefits list
- Removed old generic About section, replaced with personal story
- Differentiation: honest on-the-ground guidance vs. cold listing portals

## Next Steps
- [ ] Phillip: Request Idealista API access at developers.idealista.com/access-request
- [ ] Phillip: Ask accountant about adding CAE 68311 to existing Lda
- [ ] Pick a domain name for the real estate site
- [ ] Create Vercel Blob store + link to project (dashboard) for lead persistence
- [ ] Start Instagram/YouTube content plan for Porto real estate
- [ ] Identify 3-5 AMI-licensed agencies in Porto for referral partnerships
- [ ] Study Portuguese (needed for AMI exam)
