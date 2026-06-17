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
- **Disk:** 75G (23G used, 50G free, 32% full)
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

See [[Tailscale Network]] for full device list.

---

## Services
- **Hermes Gateway** — systemd service (`hermes-gateway.service`, `--replace`)
- **Hermes Dashboard** — background process (`hermes dashboard --no-open`)
- **Tailscale** — VPN mesh (systemd)
- **Nginx** — reverse proxy
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
- **Wiki repo:** TheGhostofJoeMacmillan/plutarco-wiki (public, auto-push hourly)
- **Hermes backup:** TheGhostofJoeMacmillan/hermes-backup
- **Auth:** Fine-grained PAT (restored Apr 10)

---

## Access
- **From phone:** Termius on S24 Ultra → ssh hermes
- **From laptop:** ThinkPad T480 → ssh hermes
- **Direct:** `ssh go@100.96.245.70` (Tailscale)

---

## Pending Maintenance
- ⚠️ Server reboot needed — kernel updates pending (6.8.0-110, 111, 117, 124)
