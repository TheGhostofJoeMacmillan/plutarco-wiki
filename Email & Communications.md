# Email & Communications

> *All email, messaging, and notification setup.*

---

## Gmail Accounts

### Plutarco — pltco.ink@gmail.com
- **Purpose:** Agent's primary email, GitHub commits, CJ Dropshipping, art correspondence
- **Access:** Google Workspace MCP OAuth on VPS
- **OAuth token:** ~/.config/google-workspace-mcp/credentials.json
- **Client ID:** 338689075775-o75k922vn5fdl18qergr96rp8g63e4d7.apps.googleusercontent.com
- **Usage from VPS:** Direct Python API calls (google.oauth2.credentials.Credentials + googleapiclient). mcporter MCP server times out headless.
- **Usage from Vercel:** NOT possible with OAuth token. Need App Password for serverless functions.
- **Status:** ✅ Working for read/send from VPS

### Phillip — psb.duo@gmail.com
- **Purpose:** Personal email, domain registrations (Afternic/GoDaddy use this)
- **Access:** Not directly accessible by agent
- **Status:** No OAuth/App Password set up

### Business Emails (TBD)
- **Pathway US:** Need dedicated email for lead notifications. Depends on domain choice.
- **Maxine Agency:** hello@maxineagency.com (services.maxineagency.com → Vercel)
- **FieldWriter:** Covered by Google Workspace subscription (invoice comes to pltco.ink@gmail.com)

---

## Telegram

### Bot
- Hermes bot token stored in Vercel env and ~/.hermes/.env
- Current lead notifications go to Phillip's DM (chat ID: 7558955416)

### Channels (TODO)
- **Pathway US leads:** Need to create private channel, add bot as admin, update TELEGRAM_CHAT_ID in Vercel
- Phillip wants separate channels per project — can create from desktop Telegram

---

## SMTP for Vercel Serverless

For any site that needs to send emails from Vercel functions:
1. Create or choose a Gmail account
2. Enable 2FA → Generate App Password (Google Account → Security → App Passwords)
3. Add as Vercel env vars: `GMAIL_USER`, `GMAIL_APP_PASSWORD`
4. Use nodemailer in the serverless function

**Important:** OAuth tokens on the VPS cannot be used by Vercel serverless functions. They run in different environments. App Passwords are the only way.

---

## Key Lesson
OAuth = works from VPS (this machine). App Password = works from Vercel (serverless). Don't confuse them.
