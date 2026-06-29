Audit Date: June 29, 2026

Files Checked:
- ~/wiki/AUDIT_REPORT.md
- ~/wiki/Art References.md
- ~/wiki/Art Taste & Direction.md
- ~/wiki/Art Techniques.md
- ~/wiki/ClawPlot-Roplotica.md
- ~/wiki/Daily/2026-06-15.md
- ~/wiki/Deprioritized Projects.md
- ~/wiki/Email & Communications.md
- ~/wiki/FieldWriter.md
- ~/wiki/Hermes Setup.md
- ~/wiki/Home.md
- ~/wiki/Infrastructure/Auth & Services.md
- ~/wiki/Infrastructure/discord-channel-map.md
- ~/wiki/Infrastructure/email-sending.md
- ~/wiki/Infrastructure/Laptop & Wiki.md
- ~/wiki/Lessons Learned.md
- ~/wiki/LocalIntelligence.md
- ~/wiki/Maxine Agency.md
- ~/wiki/Music/songwriting-jaguar-de-plata.md
- ~/wiki/Obsidian Setup Guide.md
- ~/wiki/Pathway US.md
- ~/wiki/People and Contacts.md
- ~/wiki/Plutarco Art.md
- ~/wiki/Projects/ami-license-application.md
- ~/wiki/Projects/knitwear-fabric-suppliers-portugal.md
- ~/wiki/Projects/knitwear-footwear-portugal.md
- ~/wiki/Projects/portugal-real-estate.md
- ~/wiki/Projects/real-estate-buildout.md
- ~/wiki/Projects/roplotica-security-fixes.md
- ~/wiki/Reflections.md
- ~/wiki/Tailscale Network.md
- ~/wiki/Timeline.md
- ~/wiki/Trading.md
- ~/wiki/VPS Config.md
- ~/wiki/xNarrator.md

Issues Found:

CRITICAL:
- None. The previous critical issues have been addressed.

MEDIUM:
1. **VPS Config.md - Disk usage:** The wiki states "17G used / 24% full", but the actual usage is "23G used / 32% full".
2. **VPS Config.md - Hermes services:** The wiki states "Hermes Agent — systemd service (`--replace`)", but only `hermes-gateway.service` is a systemd unit. The dashboard runs as a background process.
3. **Tailscale Network.md - Device list:** The device list is incomplete, only listing the VPS, ThinkPad, S24 Ultra, desktop-dmorc4p, go-surface-go-3, and samsung-sm-s928u1. The actual tailnet has more devices.
4. **Tailscale Network.md - Surface Go status:** The Surface Go is described as "intermittent" but was last seen "59d ago".
5. **Tailscale Network.md - S24 Ultra IP:** The wiki states "dynamic" IP for S24 Ultra, but `tailscale status` shows a static IP of `100.92.13.94`.
6. **Infrastructure/Laptop & Wiki.md - Wiki repo privacy:** The wiki states the repo is "private" but it is actually public.
7. **xNarrator.md - Voice count:** The wiki mentions "26 voices total" then later "Total: 39 .wav files". This discrepancy needs clarification.
8. **Plutarco Art.md - Generator count:** The wiki states "77 generators", but `ls ~/projects/plotter-art/techniques/` shows 125 entries (including non-generator files). This should be clarified to avoid misinterpretation of the number of actual generators.
9. **Obsidian Setup Guide.md - Repo privacy:** The wiki states the repo is "private," but it is public.
10. **Trading.md - Code location:** The wiki points to `~/projects/sol-trading/` (symlink to archived OpenClaw suite), but `~/projects/sol-copytrader/` appears to have more active code.
11. **Home.md - Missing page:** The [[LocalIntelligence]] link points to a page that doesn't exist, only the project directory.

LOW:
1. **Home.md - Status date:** The "Current Status" date in `Home.md` is June 17, 2026, while the current date is June 29, 2026.
2. **Home.md - GitHub repo:** The wiki lists `TheGhostofJoeMacmillan/hermes-backup` as the GitHub repo, which is for `.hermes` backup, not the wiki. The wiki repo is `plutarco-wiki`.
3. **VPS Config.md - Kernel pending:** The wiki says "6.8.0-90 → 6.8.0-110" pending, but `/var/run/reboot-required.pkgs` lists `110`, `111`, `117`, and `124`.
4. **Tailscale Network.md - Relay:** The wiki claims `LAX (Los Angeles)` as the relay, but the actual relay for VPS is `nue` (Nuremberg).
5. **Daily Log.md - Date header:** The date in `Daily Log.md` still says "updated June 14" in `Home.md`, it should be bumped to match the current date.
6. **Daily Log.md - June 15 content:** The master log only lists the date, while actual detail lives in `Daily/2026-06-15.md`. Consider linking.
7. **FieldWriter.md - Domain:** The wiki claims `fieldwriter.ai`, but `vercel domains inspect fieldwriter.ai` returns an access error.
8. **Trading.md - Helius subscription:** The wiki notes "Helius subscription ($49/mo) needed — lapsed?" This needs verification.
9. **Plutarco Art.md - Physical works path:** The path `~/projects/plotter-art/Works by Plutarco/` should be verified on disk before being treated as authoritative.
10. **Art Taste & Direction.md - Deep-file table:** The deep-file table lists `TASTE.md` as 597 lines; the actual line count was not checked, but the file size is similar. No critical issue, but could be more precise.
11. **Music/songwriting-jaguar-de-plata.md:** The file has a header from markdown Front Matter and references `[[phillip-birdsong]]` and `[[plutarco]]` as links, which is fine, but `plutarco` should link to the main `Plutarco Art.md` page.
12. **Projects/knitwear-fabric-suppliers-portugal.md, Projects/knitwear-footwear-portugal.md:** These files are very long and detailed. It might be useful to have a summary page that links to them, or to break them up into smaller, more digestible chunks if they grow further. Currently, not an issue but something to keep in mind.

Specific Fixes Needed:

**MEDIUM PRIORITY:**
1. **File: `~/wiki/VPS Config.md`**
   - **Old string:** `Disk: 75G (17G used, 58G free, 24% full)`
   - **New string:** `Disk: 75G (23G used, 50G free, 32% full)`
   - **Old string:** `Hermes Agent — systemd service (--replace)`
   - **New string:** `Hermes Gateway — systemd service (hermes-gateway.service, --replace)` (Clarify that Hermes Agent is not a systemd service but the gateway is)
2. **File: `~/wiki/Tailscale Network.md`**
   - Rewrite the "Devices" section with the actual `tailscale status` output. Update 'Surface Go' status as 'offline, last seen 59d', and the 'S24 Ultra' IP to `100.92.13.94`. Update relay to `nue`.
3. **File: `~/wiki/Infrastructure/Laptop & Wiki.md`**
   - **Old string:** `-- Repository: TheGhostofJoeMacmillan/plutarco-wiki (private)`
   - **New string:** `-- Repository: TheGhostofJoeMacmillan/plutarco-wiki (public)`
4. **File: `~/wiki/xNarrator.md`**
   - Reconcile the "26 voices total" and "Total: 39 .wav files" statements to accurately reflect the voice inventory (e.g., explaining cloned voices vs. individual wav files).
5. **File: `~/wiki/Plutarco Art.md`**
   - Clarify the "77 generators" statement to explain that this refers to functional generators, while the directory contains other supporting files, or update the number if more generators have been added.
6. **File: `~/wiki/Obsidian Setup Guide.md`**
   - **Old string:** `(Repo is private — no credentials needed for read access)`
   - **New string:** `(Repo is public — no credentials needed for read access)`
7. **File: `~/wiki/Trading.md`**
   - Update the "Location" section to clearly state whether `~/projects/sol-copytrader/` is the current active trading codebase, and if so, update project references.
8. **File: `~/wiki/Home.md`**
   - **Old string:** `- [[LocalIntelligence]] — Domain listed at $95K on Afternic, acquisition bar live`
   - **New string:** `- [[LocalIntelligence.md]] — Domain listed at $95K on Afternic, acquisition bar live` (Add .md to link to the existing LocalIntelligence.md file)

**LOW PRIORITY:**
1. **File: `~/wiki/Home.md`**
   - Update "Current Status" date from June 17, 2026 to June 29, 2026.
   - **Old string:** `- **GitHub:** TheGhostofJoeMacmillan/hermes-backup`
   - **New string:** `- **GitHub:** TheGhostofJoeMacmillan/plutarco-wiki` (Change the GitHub link to the Wiki's actual repo)
2. **File: `~/wiki/VPS Config.md`**
   - Update the "Pending Maintenance" section to list all pending kernel updates (110, 111, 117, 124).
3. **File: `~/wiki/Tailscale Network.md`**
   - **Old string:** `Tailscale relay: LAX (Los Angeles)`
   - **New string:** `Tailscale relay: nue (Nuremberg)`
4. **File: `~/wiki/Daily Log.md`**
   - Update the date header.
   - Add a wikilink to `Daily/2026-06-15.md` from the `Daily Log.md` entry for June 15.
5. **File: `~/wiki/FieldWriter.md`**
   - Verify why `vercel domains inspect fieldwriter.ai` returns an access error. If it's a known issue that won't be fixed, add a note.
6. **File: `~/wiki/Trading.md`**
   - Verify the Helius subscription status and update the note accordingly.
7. **File: `~/wiki/Plutarco Art.md`**
   - Verify the path to physical works `~/projects/plotter-art/Works by Plutarco/` and update the note if needed.
8. **File: `~/wiki/Music/songwriting-jaguar-de-plata.md`**
   - Ensure `[[plutarco]]` links to `[[Plutarco Art]]` for consistency.

New Wiki Pages to Be Created:
1. **`~/wiki/LocalIntelligence.md`**: This page is linked in `Home.md` but does not exist. It should be created to centralize information about the LocalIntelligence project, including its status, domain, and business model.