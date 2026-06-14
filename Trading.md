# Trading

> *SOL token analysis, copy trading, and alpha scanning.*

---

## What We Have
- **Wallet Watcher v4** — tracks alpha wallet via Helius RPC `logsSubscribe` (~8s detection)
- **Copy Executor** — local signing via PumpPortal API, Jupiter V6 fallback for non-Pump.fun
- **Buyer Momentum Scanner** — detects buying pressure
- **Memetic Trend Scanner** — social sentiment analysis
- **6 pre-entry filters** for SOL token analysis
- **Paper trading** — validating before live
- **Live trading** at 0.02 SOL entries alongside paper validation

---

## Tracked Wallets
- **Alpha wallet:** `BZmxuXQ68QeZABbDFSzveHyrXCv5EG6Ut1ATw5qZgm2Q` ("Hermes Trader")
- **Copy wallet:** `AoVYcB8cAHu4ToUCj8UXpMiZr9XLxxGSg1Hj2Aq85i8S`

---

## Sizing Logic
- Time-of-day tiers: Morning (0.25-0.50 SOL), Evening (0.10-0.20 SOL)
- 1.0 SOL conviction filter

---

## Key Wins
- **$CIA token** — 75% take-profit executed at 500% and 1000% gains ✅

---

## Known Bugs (Unpatched, Archived)
- State-cursor error causing missed sells
- Timezone bug causing incorrect trade sizing
- 0.02 SOL sizing bug
- Partial sell string bug in PumpPortal

---

## Location
`~/projects/sol-trading/` (symlink to `.openclaw-archived`)
Full codebase: `~/.openclaw-archived/workspace/projects/sol-trading-suite/alpha/`

---

## Status
- **Active — revisiting** — worked on setup May 5, may be part of the rotation going forward
- Infrastructure intact, bugs documented but unpatched
- Trading runs as funding channel alongside core products
- Profits fund the mission
- ⚠️ Helius subscription ($49/mo) needed for WebSocket detection — lapsed?

---

## Key Principle
Trading funds the mission. Art is the soul. Revenue from trading = operational runway.
