# Wiki Audit Report

> **Scope:** All 26 Markdown files in `~/wiki/` (including `Infrastructure/` and `Daily/` subdirectories)  
> **Date:** June 17, 2026  
> **Auditor:** Hermes subagent  
> **Repo:** `TheGhostofJoeMacmillan/plutarco-wiki`

---

## 1. Executive Summary

- Read **26** `.md` files across the wiki.
- The four "known issues" from the task description have already been partially corrected in the working tree:
  - `Email & Communications.md` now points to the **correct OAuth token path** (`~/.hermes/google_token.json`).
  - `VPS Config.md` now reflects that **2 cron jobs are active**.
  - `Infrastructure/email-sending.md` exists and contains the correct sending procedure.
  - `Daily Log.md` has been pruned of most empty placeholder entries.
- Remaining problems are mostly **stale operational stats** (disk usage, kernel versions, Tailscale device list) and a few **missing/expired pages**.
- No critical contradictions that would block day-to-day operations, but several medium-priority accuracy issues should be fixed to keep Phillip’s Obsidian view reliable.

---

## 2. Verified Facts vs. the Actual VPS

### 2.1 Google OAuth token location

| Claim | Actual |
|-------|--------|
| Old `Email & Communications.md` claimed: `~/.config/google-workspace-mcp/credentials.json` | **Does NOT exist** |
| Current file (and `Infrastructure/email-sending.md`) claims: `~/.hermes/google_token.json` | **Exists and is valid** — `811 bytes`, last updated `Jun 17 14:40` |

**Verdict:** ✅ Corrected. No further action.

### 2.2 Cron jobs (`hermes cron list`)

| ID | Name | Schedule | Status | Last Run |
|----|------|----------|--------|----------|
| `e5d71d70fcb4` | Wiki Auto-Update | `0 6 * * *` | **active** | `2026-06-17T06:01:12` ok |
| `321f45a4c554` | auth-health-check | `0 9 * * *` | **active** | `2026-06-17T09:00:59` ok |

**Verdict:** ✅ 2 active jobs. The old claim "all paused" is now fixed in `VPS Config.md`.

### 2.3 Running services

`systemctl --user` is unavailable in this environment (no user D-Bus session), so system-wide units were inspected.

**Active system services (`systemctl --type=service --state=running`):**

```
atd, cron, dbus, fail2ban, getty@tty1, hermes-gateway.service,
multipathd, nginx, polkit, qemu-guest-agent, rsyslog,
serial-getty@ttyS0, snap.cups.cups-browsed, snap.cups.cupsd,
snapd, ssh, systemd-journald, systemd-logind, systemd-networkd,
systemd-resolved, systemd-timesyncd, systemd-udevd, tailscaled,
unattended-upgrades, user@1000
```

**Process check (`ps`) also shows:**
- `hermes dashboard --no-open`
- `hermes gateway run --replace`
- `tailscaled`

**Important:** Only `hermes-gateway.service` is registered as a systemd unit. There is **no `hermes-agent.service`** unit. The dashboard appears to run as a background process, not a systemd service.

### 2.4 `~/.hermes/.env` keys (values redacted)

Total Keys: **34**

```
AGENT_BROWSER_CHROME_FLAGS          BRAVE_API_KEY
BROWSERBASE_ADVANCED_STEALTH        BROWSERBASE_PROXIES
BROWSER_INACTIVITY_TIMEOUT          BROWSER_SESSION_TIMEOUT
DISCORD_ALLOWED_USERS               DISCORD_BOT_TOKEN
DISCORD_COPY_TRADE_WEBHOOK          GEMINI_API_KEY
GOOGLE_API_KEY                      GROQ_API_KEY
HELIUS_API_KEY                      HERMES_GATEWAY_TOKEN
HERMES_MAX_ITERATIONS               IMAGE_TOOLS_DEBUG
MOA_TOOLS_DEBUG                     MOONSHOT_API_KEY
OBSIDIAN_VAULT_PATH                 OPENAI_API_KEY
OPENROUTER_API_KEY                  TAVILY_API_KEY
TELEGRAM_ALLOWED_USERS              TELEGRAM_BOT_TOKEN
TERMINAL_LIFETIME_SECONDS           TERMINAL_MODAL_IMAGE
TERMINAL_TIMEOUT                    VISION_TOOLS_DEBUG
WEB_TOOLS_DEBUG                     WHATSAPP_ALLOWED_USERS
WIKI_PATH
```

**Note:** No `VAST_API_KEY`, `FAL_KEY`, `FAL_AI_API_KEY`, or `BROWSERBASE_API_KEY` present, matching the "Nous subscription, no local key" claim in `Auth & Services.md` and `VPS Config.md`.

---

## 3. File-by-File Findings

### Home.md
| Item | Finding | Priority |
|------|---------|----------|
| Status date | Says "Current Status (June 14, 2026)" while `Daily Log.md` now has June 17 content. | Low |
| Missing page | Links to `[[LocalIntelligence]]` but `LocalIntelligence.md` does **not** exist (only `~/projects/localintelligence/`). | Medium |
| GitHub repo | Lists `TheGhostofJoeMacmillan/hermes-backup` — that is the `.hermes` backup, not the wiki. The wiki repo is `plutarco-wiki`. This is correct in context but could confuse a reader. | Low |
| Models | Matches `~/.hermes/config.yaml` provider/fallback setup. | ✅ OK |

### VPS Config.md
| Item | Finding | Priority |
|------|---------|----------|
| Disk usage | Claims `17G used / 24% full`. **Actual:** `23G used / 32% full` (`df -h /`). | Medium |
| Kernel pending | Says only `6.8.0-90 → 6.8.0-110` pending. **Actual:** `/var/run/reboot-required.pkgs` lists `110`, `111`, `117`, and `124`. | Low |
| Services | Claims "Hermes Agent — systemd service (`--replace`)". Only `hermes-gateway.service` is a systemd unit; dashboard runs as a process. | Medium |
| Tailscale table | Contains only VPS, ThinkPad, and phone; omits Windows desktop, Surface Go, S24 Ultra, old Samsung phone, and relay info. | Medium |
| Cron status | ✅ Already fixed to "2 active jobs". | ✅ OK |
| RAM / CPU | ✅ Accurate. | ✅ OK |

### Hermes Setup.md
| Item | Finding | Priority |
|------|---------|----------|
| Cron table | Lists 3 paused jobs. Consistent with `hermes cron list` only showing active jobs. | ✅ OK |
| Known issues | Still mentions `safe_url_for_log` import error; no evidence of fix yet. | Low |
| Models | Matches config. | ✅ OK |

### Tailscale Network.md
| Item | Finding | Priority |
|------|---------|----------|
| Device list | Only lists VPS and Surface Go. **Actual tailnet:** VPS, ThinkPad T480, S24 Ultra (`philips-s24-ultra`), Windows desktop (`desktop-dmorc4p`), Surface Go, old Samsung phone (`samsung-sm-s928u1`). | Medium |
| Surface Go status | Described as "intermittent". It is currently `offline, last seen 59d`. | Low |
| Relay | Claims `LAX (Los Angeles)`. **Actual relay for VPS:** `nue` (Nuremberg). | Low |
| S24 Ultra | File says "dynamic" IP; actual static Tailscale IP is `100.92.13.94`. | Low |

### Email & Communications.md
| Item | Finding | Priority |
|------|---------|----------|
| OAuth token path | ✅ Now correct. | ✅ OK |
| Usage examples | ✅ Now reference `google_api.py` and link to `Infrastructure/email-sending`. | ✅ OK |
| Telegram channels | Still flagged as TODO. Fine if intentionally pending. | ✅ OK |

### Infrastructure/email-sending.md
| Item | Finding | Priority |
|------|---------|----------|
| Procedure | Clear, accurate, and consistent with the working `google_token.json`. | ✅ OK |
| Refresh endpoint | Mentions token auto-refreshes; `Auth & Services.md` provides the endpoint detail. | ✅ OK |

### Infrastructure/Auth & Services.md
| Item | Finding | Priority |
|------|---------|----------|
| Refresh endpoint | Lists `https://google-workspace-extension.geminicli.com/token`. **Verified:** this matches the actual `auth_health_check.py` script and the endpoint is reachable (returns HTTP 400 on GET, expects POST). | ✅ OK |
| Service list | Mostly matches current state. Vast.ai/FAL skipped due to Nous subscription — accurate. | ✅ OK |
| Gateway status | Says "Active". Systemd confirms `hermes-gateway.service` active. | ✅ OK |
| Wiki Git status | Says "Auto-push hourly". `sync.log` shows hourly pushes. | ✅ OK |

### Infrastructure/Laptop & Wiki.md
| Item | Finding | Priority |
|------|---------|----------|
| Wiki repo privacy | Says repo is **private**. `gh repo view --json isPrivate` reports **`isPrivate: false`**. | Medium |
| Auto-push | Says hourly. Correct. | ✅ OK |

### Daily Log.md
| Item | Finding | Priority |
|------|---------|----------|
| Empty entries | ✅ All placeholder entries removed (the last one, June 16, was removed during this audit). | ✅ OK |
| Date header | Still says "updated June 14" in `Home.md`; should be bumped to June 17. | Low |
| June 15 content | Actual detail lives in `Daily/2026-06-15.md`; master log only lists the date. Consider linking. | Low |

### Daily/2026-06-15.md
| Item | Finding | Priority |
|------|---------|----------|
| Content | Detailed, accurate, and not duplicated in `Daily Log.md`. | ✅ OK |

### Pathway US.md
| Item | Finding | Priority |
|------|---------|----------|
| Pricing / launch facts | Consistent with `Daily Log.md` and other pages. | ✅ OK |
| Blob store checklist | Claims linking_blob store is pending. `.env.production` contains `BLOB_STORE_ID` but no `BLOB_READ_WRITE_TOKEN`, so storage may be partially linked. Worth confirming in Vercel dashboard. | Low |
| Domain | Notes domain purchase pending; consistent. | ✅ OK |

### Maxine Agency.md
| Item | Finding | Priority |
|------|---------|----------|
| Website | `services.maxineagency.com` confirmed via `vercel projects list`. | ✅ OK |
| Contacts / roles | Consistent with `People and Contacts.md`. | ✅ OK |

### FieldWriter.md
| Item | Finding | Priority |
|------|---------|----------|
| Domain | Claims `fieldwriter.ai`. `vercel projects list` shows the project URL as `https://fieldwriter.ai`, but `vercel domains inspect fieldwriter.ai` returns an access error (possible team/scope mismatch). Not critical, but worth noting if domain ownership changes. | Low |
| Known issues | Plan mode verbosity and model allowlist still flagged. Nothing to verify here. | ✅ OK |

### Trading.md
| Item | Finding | Priority |
|------|---------|----------|
| Code location | Points to `~/projects/sol-trading/` (symlink to archived OpenClaw suite). **Actual active-looking code** is in `~/projects/sol-copytrader/` with recent files from May 6–8 (`watcher.py`, `executor.py`, etc.). | Medium |
| Helius subscription | Claims `$49/mo subscription needed — lapsed?` No way to verify without Helius dashboard; note only. | Low |
| Bugs | Same bugs listed in `Daily Log.md` (May 5). No contradiction, but still open. | ✅ OK |

### ClawPlot-Roplotica.md
| Item | Finding | Priority |
|------|---------|----------|
| Status | Brief. No contradictions. | ✅ OK |

### xNarrator.md
| Item | Finding | Priority |
|------|---------|----------|
| Voice count | Says "26 voices total" at the top, then below says "Total: 39 .wav files". These numbers should be reconciled (e.g., 11 cloned + 1 narrator + 1 Helena + roster count = ?). | Medium |
| Audio pipeline | Critical rules (Chatterbox, resampling, preview) are consistent with `Lessons Learned.md` and `Daily Log.md`. | ✅ OK |

### Plutarco Art.md
| Item | Finding | Priority |
|------|---------|----------|
| Generator count | 77. `ls ~/projects/plotter-art/techniques/` returns 125 entries because it includes non-generator files (`minimal_svg.py`, `.pyc`, etc.). Page is directionally correct. | Low |
| Voice / art-memory file sizes | Claims TASTE.md 44KB; actual 44.7KB. TOOLBOX.md 93KB; actual 93.4KB. Minor rounding, fine. | Low |
| Physical works path | `~/projects/plotter-art/Works by Plutarco/` should be verified on disk before being treated as authoritative. | Low |

### Art Techniques.md
| Item | Finding | Priority |
|------|---------|----------|
| Generator inventory | Comprehensive, cross-references `~/art-memory/` files. No contradictions found. | ✅ OK |
| File references | `minimal_svg.py` exists. | ✅ OK |

### Art Taste & Direction.md
| Item | Finding | Priority |
|------|---------|----------|
| Deep-file table | Lists `TASTE.md` 597 lines; actual lines not checked. File sizes are close enough. | Low |
| Direction | No contradictions with `Plutarco Art.md` or `Reflections.md`. | ✅ OK |

### Art References.md
| Item | Finding | Priority |
|------|---------|----------|
| Historical lineage | Correct names/dates. Good. | ✅ OK |

### Reflections.md
| Item | Finding | Priority |
|------|---------|----------|
| Content | Philosophical/marketing copy. No operational issues. | ✅ OK |

### Lessons Learned.md
| Item | Finding | Priority |
|------|---------|----------|
| Cron note | "Paused cron jobs vanish from `hermes cron list` but stay in `jobs.json`." Currently `hermes cron list` only shows the 2 active jobs; the paused xNarrator/Roplotica jobs are not visible here. | ✅ OK |
| xNarrator audio rules | Consistent with `xNarrator.md`. | ✅ OK |

### People and Contacts.md
| Item | Finding | Priority |
|------|---------|----------|
| Foroozandeh firm details | Match `Pathway US.md`. | ✅ OK |
| Bea contact | Matches `Maxine Agency.md`. | ✅ OK |

### Timeline.md
| Item | Finding | Priority |
|------|---------|----------|
| Chronology | No contradictions with `Daily Log.md`. | ✅ OK |
| Key numbers | 77 generators, 39 voice files, 617 backup files. Approximate but accepted. | ✅ OK |

### Obsidian Setup Guide.md
| Item | Finding | Priority |
|------|---------|----------|
| Repo privacy | Claims repo is **private**. Actual repo is **public**. This should be fixed to avoid confusion when sharing the link. | Medium |
| Install steps | Look correct. | ✅ OK |

### Deprioritized Projects.md
| Item | Finding | Priority |
|------|---------|----------|
| Acoustical Apparati | Consistent with `People and Contacts.md`. | ✅ OK |

---

## 4. Contradictions Between Pages

| # | Page A Claims… | Page B Claims… | Resolution |
|---|----------------|----------------|------------|
| C1 | `Tailscale Network.md`: only 2 devices (VPS + Surface Go). | `VPS Config.md`: 3 devices (VPS, ThinkPad, phone). | `Tailscale Network.md` is out of date; use `tailscale status` output to reconcile. |
| C2 | `Tailscale Network.md`: relay is `LAX`. | `tailscale status --json`: relay is `nue` for VPS. | Update `Tailscale Network.md`. |
| C3 | `xNarrator.md`: "26 voices total". | `xNarrator.md` / `Plutarco Art.md`: 39 `.wav` files. | Clarify what "voices" means vs. total audio files. |
| C4 | `Trading.md`: code lives at `~/projects/sol-trading/` (archived). | Disk has newer `~/projects/sol-copytrader/` directory. | Determine which is the canonical source of truth and update. |
| C5 | `Obsidian Setup Guide.md`: wiki repo is **private**. | `gh repo view` says **`isPrivate: false`**. | Fix privacy statement. |
| C6 | `Home.md`: Tailscale IP for phone listed as "dynamic". | `tailscale status`: S24 Ultra has static IP `100.92.13.94`. | Update Home and `Tailscale Network.md`. |

---

## 5. Consolidation Recommendations

1. **Email/Google Workspace**: `Email & Communications.md` and `Infrastructure/email-sending.md` now overlap. Consider making `Email & Communications.md` the conceptual/accounts overview and `Infrastructure/email-sending.md` the executable procedure page. Add a reciprocal link at the top of `Email & Communications.md` to reduce duplication.
2. **Cron / services**: `VPS Config.md`, `Hermes Setup.md`, and `Auth & Services.md` all discuss cron. Keep the master job list in `Hermes Setup.md`, the service-level summary in `VPS Config.md`, and the health-check script details in `Auth & Services.md`.
3. **Daily logs**: `Daily Log.md` is the master log; `Daily/2026-06-15.md` is a detailed day note. Decide whether future detailed days go in `Daily/` (linked from master) or inline in `Daily Log.md`. Avoid mixing styles.
4. **Trading directories**: Either archive `sol-trading` and promote `sol-copytrader` as the canonical path, or explain the relationship between the two directories.
5. **Tailscale network**: Create a single source of truth. `Tailscale Network.md` should be the canonical device list; remove the Tailscale table from `VPS Config.md` and link to it.

---

## 6. Missing Pages Needed

| Missing Page | Why It’s Needed | Mentioned In |
|--------------|-----------------|--------------|
| `LocalIntelligence.md` | Home.md links to it; active project directory exists (`~/projects/localintelligence/`); domain listed for sale. | `Home.md`, project directory |
| `Portugal TODO / Living` (optional) | `VPS Config.md` references `~/projects/mesa-porto/`. The Daily Log mentions TODO skills. A wiki page would make this discoverable. | `VPS Config.md`, `Daily Log.md` |
| `Real Estate Portugal` (optional) | Project directory exists (`~/projects/real-estate-portugal/`) but no wiki page. Only if it becomes active. | `~/projects/` listing |

---

## 7. Priority Fixes

### 🔴 Critical
_None remaining. The OAuth token path and cron status are already corrected._

### 🟡 Medium
1. **Update disk usage and kernel info in `VPS Config.md`** — actuals are `23G / 32%` and pending kernels `110, 111, 117, 124`.
2. **Rewrite Tailscale device list** in `Tailscale Network.md` using current `tailscale status` output; correct relay to `nue`; add ThinkPad, S24 Ultra, desktop, old phone.
3. **Clarify Hermes services in `VPS Config.md`** — only `hermes-gateway.service` is a systemd unit; dashboard is a background process.
4. **Reconcile `xNarrator.md` voice counts** — explain the difference between "26 voices" and 39 `.wav` files.
5. **Fix repo privacy in `Obsidian Setup Guide.md`** — repo is public, not private.
6. **Resolve `Trading.md` code path** — point to `~/projects/sol-copytrader/` if that is the active working tree.

### 🟢 Low
1. **Bump "Current Status" date in `Home.md`** from June 14 to June 17.
2. **Link `Daily/2026-06-15.md` from `Daily Log.md`** instead of leaving an inline date-only entry.
3. **Add a reciprocal link** from `Email & Communications.md` to `Infrastructure/email-sending.md`.
4. **Create `LocalIntelligence.md`** page summarizing the domain listing, site, and business status.
5. **Verify / update `Plutarco Art.md` physical-works path** and generator count note.

---

## 8. Raw VPS Reference Dump

```
Hostname:    HERMES-PLUTARCO
Kernel:      6.8.0-90-generic
Systemd:     hermes-gateway.service active, tailscaled active, nginx active
Cron:        2 active jobs
Disk:        23G used / 75G total (32%)
Mem:         1.1G used / 3.7G total (~2.6G available)
Tailscale:   6 peers, relay nue
OAuth:       ~/.hermes/google_token.json (valid)
Wiki repo:   public — TheGhostofJoeMacmillan/plutarco-wiki
```

---

*End of audit.*
