# Obsidian Wiki Setup Guide

> *Read Plutarco's knowledge base on your laptop and phone.*

---

## What You'll See

A fully linked wiki with 20+ pages covering every project, contact, and config. Navigation through `[[wikilinks]]`, a Home hub page, and full-text search.

---

## Laptop Setup (5 minutes)

### 1. Install Obsidian
- Download from [obsidian.md](https://obsidian.md) (free, all platforms)
- No account needed

### 2. Clone the wiki repo
Open Terminal and run:
```
cd ~
git clone https://github.com/TheGhostofJoeMacmillan/plutarco-wiki.git
```
(Repo is public — no credentials needed for read access)

### 3. Open in Obsidian
- Launch Obsidian
- Click "Open folder as vault"
- Select the `plutarco-wiki` folder
- Done — you'll see Home.md as the hub with all links

### 4. Install Obsidian Git plugin (auto-sync)
- Settings → Community Plugins → Turn on community plugins
- Browse → Search "Obsidian Git" → Install → Enable
- Settings → Obsidian Git:
  - Auto pull interval: 30 (minutes)
  - Auto backup interval: 0 (disable — Plutarco writes, you read)
  - Commit message: "laptop update"
- Now Obsidian auto-pulls changes every 30 minutes

---

## Phone Setup (5 minutes)

### 1. Install Obsidian
- iOS: App Store → "Obsidian"
- Android: Play Store → "Obsidian"
- Free, no account needed

### 2. Clone the repo
**Android (Termux):**
```
pkg install git
git clone https://github.com/TheGhostofJoeMacmillan/plutarco-wiki.git ~/storage/shared/plutarco-wiki
```

**iOS (Working Copy app — free tier works):**
- Install "Working Copy" from App Store
- Clone repo: TheGhostofJoeMacmillan/plutarco-wiki
- In Obsidian: Open folder → navigate to Working Copy's storage

### 3. Open in Obsidian
- Open vault → select the `plutarco-wiki` folder
- Install Obsidian Git plugin the same way as laptop
- Set auto pull to 30 minutes

---

## How It Works

```
Plutarco updates wiki on VPS
        ↓
Auto-push to GitHub (every hour)
        ↓
Obsidian pulls on your devices (every 30 min)
        ↓
You see the latest on phone/laptop
```

**If you want to force a refresh:** In Obsidian, open command palette (Ctrl/Cmd+P) → "Obsidian Git: Pull"

**If you want to edit a note:** Go ahead — Obsidian Git will push your changes back. Next time I pull on the VPS, I'll see them.

---

## Troubleshooting

- **"Repository not found"** — Make sure you're authenticated with GitHub. Run `gh auth login` on laptop, or use a personal access token.
- **"No changes showing"** — Force pull: Command palette → "Obsidian Git: Pull"
- **Links don't work** — Make sure you opened the folder as a vault, not individual files

---

## Quick Reference

| What | Where |
|------|-------|
| Repo | github.com/TheGhostofJoeMacmillan/plutarco-wiki |
| Hub page | Home.md |
| Project pages | Pathway US, FieldWriter, xNarrator, etc. |
| Contacts | People and Contacts.md |
| Infrastructure | VPS Config, Hermes Setup, Email & Communications |
| History | Timeline.md, Daily Log.md |
