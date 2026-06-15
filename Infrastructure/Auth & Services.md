# Auth & Service Health

All services checked daily at 9am via cron (`auth-health-check`).
Script: `~/.hermes/scripts/auth_health_check.py`

## Services

| Service | Status | Auth Method | Notes |
|---------|--------|-------------|-------|
| GitHub | ✅ | PAT in keyring | Account: TheGhostofJoeMacmillan |
| Google/Gmail | ✅ | OAuth2 (auto-refresh) | pltco.ink@gmail.com, refreshes via cloud function |
| Vercel | ✅ | CLI token | Account: theghostofjoemacmillan |
| Groq API | ✅ | API key in .env | Whisper transcription, chat |
| OpenAI API | ✅ | API key in .env | TTS, chat |
| Vast.ai | ⏭️ | Nous subscription | No local key needed |
| FAL.ai | ⏭️ | Nous subscription | Image generation |
| Laptop SSH | ✅ | Ed25519 key | theghostofjoemacmillan@100.66.152.87 |
| Tailscale | ✅ | Auto | 6 peers |
| Hermes Gateway | ✅ | systemd | Active |
| Wiki Git | ✅ | HTTPS | Auto-push hourly |

## Known Issues

- **Vercel email**: Needs App Password for sending emails from Vercel functions (Gmail SMTP)
- **Google MCP OAuth**: The MCP server requires browser interaction for initial auth, but refresh_token auto-refreshes via cloud function

## How to Fix Common Issues

### Google token expired
The health check auto-refreshes. Manual fix:
```python
python3 -c "
import json, urllib.request
with open('~/.hermes/google_token.json') as f:
    d = json.load(f)
data = json.dumps({'refresh_token': d['refresh_token'], 'grant_type': 'refresh_token'}).encode()
req = urllib.request.Request('https://google-workspace-extension.geminicli.com/token', data=data, headers={'Content-Type': 'application/json'})
result = json.loads(urllib.request.urlopen(req).read())
d['access_token'] = result['access_token']
with open('~/.hermes/google_token.json', 'w') as f:
    json.dump(d, f)
"
```

### Full re-auth (Google)
Run the MCP server and open the auth URL in browser:
```bash
npx -y @presto-ai/google-workspace-mcp
```
