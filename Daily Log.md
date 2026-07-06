# Daily Log

> *What happened, day by day.*

---




















## July 6, 2026
- (auto-generated entry — no activity logged yet)
## July 5, 2026
- (auto-generated entry — no activity logged yet)
## July 4, 2026
- (auto-generated entry — no activity logged yet)
## July 3, 2026
- (auto-generated entry — no activity logged yet)
## July 2, 2026
- (auto-generated entry — no activity logged yet)
## July 1, 2026
- (auto-generated entry — no activity logged yet)
## June 30, 2026
- (auto-generated entry — no activity logged yet)
## June 29, 2026
- (auto-generated entry — no activity logged yet)
## June 28, 2026
- (auto-generated entry — no activity logged yet)
## June 27, 2026
- (auto-generated entry — no activity logged yet)
## June 26, 2026
- (auto-generated entry — no activity logged yet)
## June 25, 2026
- (auto-generated entry — no activity logged yet)
## June 24, 2026
- (auto-generated entry — no activity logged yet)
## June 23, 2026
- (auto-generated entry — no activity logged yet)
## June 22, 2026
- (auto-generated entry — no activity logged yet)
## June 21, 2026
- (auto-generated entry — no activity logged yet)
## June 20, 2026
- (auto-generated entry — no activity logged yet)
## June 19, 2026
- (auto-generated entry — no activity logged yet)
## June 18, 2026
- (auto-generated entry — no activity logged yet)
## June 17, 2026 — Maxine Agency Website + Trade Show DB + Memory System
- 🌐 Maxine Agency website updates: removed service numbers, removed Monthly Retainer, renamed "Connection + Sampling" → "Sourcing & Sampling" (merged sourcing into it), expanded all service descriptions
- 🌐 Fixed "past clients" → "brands they've produced for", "in Portugal" → "at the factories"
- 🌐 Brands list replaced: Acne Studios, Balenciaga, Casablanca, Veja, Hugo Boss, Dôen
- 📋 Comporta store list created (16 stores/hotels with addresses, phones, emails, Maps links)
- 📧 Emailed Comporta store list to hello@maxineagency.com from pltco.ink@gmail.com
- 📧 Email sending set up: Gmail OAuth via google_api.py, documented in wiki
- 🏪 Trade show exhibitor database in progress: 644 brands extracted (87 MAN/WOMAN, 20 Splash, 537 Playtime), batch email scraper running in background
- 🧠 Memory system overhaul: trimmed memory from 97% to 66%, consolidated to pure pointers, wiki audit running via background subagent
- 🧠 Fixed wiki: Email & Communications (wrong token path), VPS Config (cron status), Daily Log (removed empty entries)
- 🧠 Created Infrastructure/email-sending.md wiki page

## June 14, 2026 — Pathway US Launch + Wiki Refresh
- 🚀 Pathway US site fully built and deployed: pathway-us.vercel.app
- ✅ Form API working with Telegram notifications
- ✅ Privacy, Terms, Thank-you pages all live
- ✅ Cookie consent banner + advertising disclosures
- ✅ PDF proposal finalized — pricing converted to USD, market data verified
- 💰 Pricing: E-2/EB-1/O-1 $275-425, L-1/H-1B/EB-2 $225-325, Family $175-225
- 🔲 5 items pending: Blob store link, email setup, Telegram channel, e2e test, domain
- 📋 Launch checklist saved at ~/projects/immigration-leads/LAUNCH-CHECKLIST.md
- 💡 Discussed broader lead gen business — multiple verticals beyond immigration
- 🧠 Wiki refreshed — new pages for Pathway US, Maxine Agency, Email & Communications
- 🧠 Hermes memory trimmed to pointers, wiki used for depth

## May 5, 2026 — Copy Trading Deep Dive + Wiki Refresh
- 🔍 Deep dive into Solana copy-trading infrastructure (wallet watcher, copy executor, sizing logic)
- 🐛 Identified bugs: state-cursor error (missed sells), timezone bug (wrong sizing), 0.02 SOL sizing bug, partial sell string bug in PumpPortal
- ✅ Confirmed $CIA token success — 75% take-profit at 500% and 1000% gains
- 🔄 Decision: copy trading is being revisited, may be part of the rotation going forward
- 🧠 Delegation model updated to Kimi K2.6 via Nous Portal (from MiMo)
- 🔧 Hermes memory plugins evaluated — 8 options available, decided to stick with wiki + cron auto-updates for now

## May 3, 2026 — LocalIntelligence Domain + Gmail Setup
- 💰 Afternic listing confirmed: localintelligence.ai at $95,000 Buy Now
- 🖥️ Added "domain available for acquisition" bar to live site (gold INQUIRE button)
- 🔐 Gmail/Google Workspace OAuth setup for pltco.ink@gmail.com — working
- 📋 Decision: keep consulting site live + domain-for-sale bar (hybrid approach)

## April 30, 2026 — Kimi K2.6 + FieldWriter Analysis
- 🤖 Kimi K2.6 confirmed available via Nous Portal
- ⚙️ Delegation config updated: `moonshotai/kimi-k2.6` via `nous` provider
- 📝 FieldWriter plan mode analyzed — prompt at `Hn()` line ~2283, too deliberative
- 📝 FieldWriter Pro model selection reviewed — only 3 models, needs GLM/cheaper options
- 🛠️ `kimi-k2-6-delegation` skill created

## April 29, 2026 — Portugal Settling + Server Maintenance
- 🍽️ Restaurant log: Bar Tolo 4.5/5, Sài Gòn 4.5/5, Lareira on wishlist
- ✅ Portugal TODO created at `~/projects/mesa-porto/TODO.md` with `portugal-todo` skill
- 🔧 Server: 50 packages upgraded, kernel update pending (6.8.0-90 → 6.8.0-110, reboot needed)
- 💻 Laptop SSH access set up — ThinkPad T480 at 100.66.152.87
- 🖥️ Hermes dashboard skill created but frontend not built (web_dist missing)

## April 19, 2026 — Hetzner Migration Day
- ✅ VPS health check — HERMES-PLUTARCO, 660Mi/3.7Gi RAM, 7% disk
- ✅ STT fixed — pinned to English (no more French hallucinations)
- ✅ Holographic memory enabled — local SQLite structured facts
- ✅ Wiki rebuilt — 18 pages covering full project history
- ✅ Projects symlinked — `~/projects/` → archive (plotter-art, xnarrator, fieldwriter, sol-trading, discord-voice-bot)
- ✅ Art memory recovered — TASTE.md (44KB), TOOLBOX.md (93KB), TECHNIQUES.md, STUDIES.md, etc. copied to `~/art-memory/`
- ✅ All 77 art generators confirmed present
- ✅ 39 voice files confirmed present (11 cloned + roster + narrator + helena)
- ✅ Surface Go unreachable — all critical data verified on VPS, no dependency on old machine

## April 7, 2026 — Hermes Migration Day
- OpenClaw → Hermes Agent migration completed
- 617 files backed up to GitHub (TheGhostofJoeMacmillan/hermes-backup)
- Model set to GLM-5.1 via OpenRouter
- Discord + Telegram connected
- 7 old bots removed
- 4 Vast.ai zombie instances killed
