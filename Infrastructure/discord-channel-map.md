# Discord Server Channel Map

**Server:** The Ghost of Joe MacMillan's server
**Guild ID:** `1468496098120433738`
**Bot:** Plutarco (`1468491933486940314`)

## How to Look Up Channels

Run the list_channels script:
```bash
python3 ~/.hermes/skills/devops/discord-server-admin/scripts/list_channels.py --ids
```

This uses the Discord Bot API (requires `DISCORD_BOT_TOKEN` in `~/.hermes/.env`). Plutarco **can** look up channel IDs — no need to ask Phillip for them.

## Channel IDs (as of 2026-06-22)

### No Category
| Channel | ID | Topic |
|---------|-----|-------|
| #art-studio | `1469444843892637859` | Plutarco's art studio |
| #las-pozas | `1469782904430399669` | Plutarco & Phillip's space |
| #plutarco-ink | `1469478566587531386` | plutarco.ink website |
| #operations | `1477073377083523093` | Business, marketing, operations, product launches |
| #commercial-art | `1476054385573498954` | Galleries, collections, outreach |
| #roplotica | `1469478568718504007` | roplotica.com |
| #xnarrator | `1476659853819645982` | X Audio Feed product dev |
| #fieldwriter | `1516068359161122816` | fieldwriter.ai |
| #immigration-leads | `1516068360130003125` | Pathway US |
| #maxine-agency | `1516079513597903011` | Maxine Agency — Bea's operations |

### Channels Category
| Channel | ID | Topic |
|---------|-----|-------|
| #sales | `1469478564729589974` | eBay, Craigslist, Marketplace |
| #sleepy-classics | `1477955360919912629` | YouTube audiobook channel |
| #selling | `1475936464536600587` | eBay, Etsy, Craigslist, vintage goods |
| #polymarket | `1479910756110696672` | Polymarket prediction market signals |
| #narrative-alpha | `1480107958653292544` | Narrative-driven token alerts |
| #movers | `1479394422511894619` | Token movers and market signals |
| #smart-money | `1481799910931300393` | Smart money wallet tracking |
| #logistics | `1469444823160193054` | Operations & logistics |
| #robotics | `1478163122505388164` | Robot arms, 3D printing, hardware |
| #ibm-5150 | `1476389181763620956` | IBM 5150/5160/AT serial bridge |
| #pocket-claw | `1479906169488408677` | Pocket Claw 3D-printable companion |
| #projects | `1477555838376869981` | Builds, tech, art, logistics, planning |
| #operations-2 | `1483236950566764745` | Second ops board |

### Text Channels Category
| Channel | ID | Topic |
|---------|-----|-------|
| #marketing | `1478116109856280679` | Marketing strategy, social media, outreach |
| #general | `1468496098904637598` | General chat |
| #code | `1469444819586646029` | Code & infrastructure |
| #crypto | `1469444821461504205` | Crypto & markets |
| #research | `1469475619803889773` | Research & intel |

### Trading Category
| Channel | ID | Topic |
|---------|-----|-------|
| #alpha-trading | `1475936466222841896` | Solana alpha scanner |
| #copy-trades | `1501243493928927342` | Live copy trading alerts |
| #alpha-signals | `1476642266050203679` | Real-time memecoin alpha signals |

### Voice Channels Category
| Channel | ID |
|---------|-----|
| #General (voice) | `1468496098904637599` |

## Cron Job Delivery Routing

- **Weekly Wiki Audit** (Mon 7am) → `discord:1477073377083523093` (#operations)
- **xNarrator Daily Scrape** → `discord:1476659853819645982` (#xnarrator) [paused]
- **xNarrator Weekly Scout** → `discord:1476659853819645982` (#xnarrator) [paused]
- **Roplotica Payment Verification** → `telegram` [paused]
- **Wiki Auto-Update** → `local` (no delivery)
- **Auth Health Check** → `origin` (whatever channel last active)

## Notes

- Re-run `list_channels.py --ids` after creating/moving channels to refresh this page
- Cron `deliver` format: `discord:<channel_id>` for specific channel, `origin` for current chat, `local` for no delivery
