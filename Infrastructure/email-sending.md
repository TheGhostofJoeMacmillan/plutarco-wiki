# Email Sending

## How to send email from the VPS

Gmail OAuth is set up at `~/.hermes/google_token.json`, authenticated as **Plutarco <pltco.ink@gmail.com>**.

### Send email
```bash
GAPI="python3 /home/go/.hermes/skills/productivity/google-workspace/scripts/google_api.py"

$GAPI gmail send \
  --to "recipient@example.com" \
  --from '"Plutarco" <pltco.ink@gmail.com>' \
  --subject "Subject line" \
  --body "Email body text"
```

Add `--html` flag for HTML body.

### Search email
```bash
$GAPI gmail search "is:unread" --max 10
$GAPI gmail search "from:hello@maxineagency.com newer_than:7d"
```

### Read email
```bash
$GAPI gmail get MESSAGE_ID
```

### Reply to email
```bash
$GAPI gmail reply MESSAGE_ID --body "Reply text"
```

## Notes
- Token auto-refreshes — no manual intervention needed
- Can send to hello@maxineagency.com (Bea's inbox)
- Phillip reviews all emails before anything goes out on behalf of Maxine Agency
- Scopes: gmail.modify, calendar, drive, docs, userinfo.profile
