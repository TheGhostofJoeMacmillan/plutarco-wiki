# VPS Config

> *Hetzner CX22 Falkenstein — our home base.*

---

## Server
- **Provider:** Hetzner
- **Type:** CX22
- **Location:** Falkenstein, Germany
- **Public IP:** 178.104.112.161
- **Tailscale IP:** 100.96.245.70
- **User:** go
- **RAM:** 3.7Gi (typically 1.1Gi used, ~2.6Gi available)
- **CPU:** 2 vCPU (shared AMD EPYC-Genoa)
- **Disk:** 75G (17G used, 56G free, 24% full)
- **GPU:** None
- **Swap:** None

---

## Security
- Key-only SSH (no password auth)
- UFW firewall
- fail2ban
- Auto-updates enabled
- Tailscale-only SSH recommended
- Secret redaction enabled (`security.redact_secrets: true`)

---

## Tailscale Network

| Device | Tailscale IP | Notes |
|--------|-------------|-------|
| VPS | 100.96.245.70 | Primary server |
| ThinkPad T480 | 100.66.152.87 | Laptop, SSH accessible from VPS |
| S24 Ultra | (dynamic) | Phone, Termius |

---

## Services
- **Hermes Agent** — systemd service (`--replace`)
- **Tailscale** — VPN mesh
- **Cron:** 2 active jobs — wiki auto-update (daily 6am) + auth health check (daily 9am)

---

## Key Directories
| Path | Purpose |
|------|---------|
| `/home/go/` | Home base |
| `/home/go/.hermes/` | Agent config, sessions, cron |
| `/home/go/.hermes/config.yaml` | Main agent config |
| `/home/go/.hermes/.env` | Tokens and keys |
| `/home/go/.openclaw-archived/` | Full OpenClaw archive (symlinked) |
| `/home/go/projects/` | Symlinks to active projects |
| `/home/go/art-memory/` | Art taste, toolbox, studies docs |
| `/home/go/wiki/` | Knowledge base (this wiki) |
| `/home/go/projects/mesa-porto/` | Restaurant log + Portugal TODO |

---

## Git Backup
- **Repo:** TheGhostofJoeMacmillan/hermes-backup
- **Auth:** Fine-grained PAT (restored Apr 10)
- **Content:** Full ~/.hermes backup

---

## Access
- **From phone:** Termius on S24 Ultra → ssh hermes
- **From laptop:** ThinkPad T480 → ssh hermes
- **Direct:** `ssh go@100.96.245.70` (Tailscale)

---

## Pending Maintenance
- ⚠️ Server reboot needed for kernel update (6.8.0-90 → 6.8.0-110)
