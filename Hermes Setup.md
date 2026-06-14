# Hermes Setup

> *Agent configuration, models, and cron jobs.*

---

## Current Model
- **Main:** GLM-5.1 via Nous Portal (`z-ai/glm-5.1`)
- **Vision:** google/gemini-2.5-flash via OpenRouter (auxiliary in config.yaml)
- **Delegation:** Kimi K2.6 via Nous Portal (`moonshotai/kimi-k2.6`)
- **STT:** Groq, pinned to English (`language: en`) — prevents French transcription errors

---

## Config
- **Location:** `~/.hermes/config.yaml`
- **Memory:** Built-in (2,200 char limit) + Wiki (~/wiki/) for deep knowledge
- **Secret redaction:** Enabled (`security.redact_secrets: true`)

---

## Cron Jobs

| Job | Schedule | Status | Notes |
|-----|----------|--------|-------|
| xNarrator Daily Scrape | 4:00 AM | ⏸️ PAUSED | Last ran Apr 18 |
| xNarrator Weekly Scout | Monday 10:00 AM | ⏸️ PAUSED | Last ran Apr 13 |
| Roplotica Verification | 9:00 AM daily | ⏸️ PAUSED | Has `safe_url_for_log` import error |

---

## Key Skills (Post-Migration)
- `hermes-agent` — Configure, extend, or troubleshoot Hermes
- `google-workspace` — Gmail, Calendar, Drive, Sheets via OAuth
- `note-taking` — Obsidian wiki + Notion API
- `portugal-todo` — Manage Portugal settling-in tasks
- `laptop-files` — Remote laptop file management

---

## Migration Notes
- OpenClaw archived at `~/.openclaw-archived/` (symlinked)
- 617 files backed up to GitHub (TheGhostofJoeMacmillan/hermes-backup)
- GitHub auth: Fine-grained PAT (restored Apr 10, stored in keyring)

---

## Known Issues
- Roplotica `safe_url_for_log` import error in gateway — blocks Telegram delivery
- Server reboot pending for kernel update (6.8.0-90 → 6.8.0-110)
