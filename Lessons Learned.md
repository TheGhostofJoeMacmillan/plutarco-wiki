# Lessons Learned

> *Things that broke and how we fixed them. Don't repeat these.*

---

## Audio / xNarrator
- **Chatterbox outputs 24kHz** — MUST resample to 44100Hz BEFORE concatenation, or you get chipmunk audio. Non-negotiable.
- **NEVER use OpenAI TTS** for xNarrator — always Chatterbox on Vast.ai
- **Always preview MP3** for Phillip before YouTube upload

## STT / Transcription
- Groq STT can hallucinate French text ("Sous-titrage Société Radio-Canada") — fixed by pinning `language: en` in config.yaml

## Plotting / Art
- **Paint stripes:** Diagonal stripes read as "crossing out" — avoid full-width diagonals through pieces
- **Three layers = muddy** — max two layers per piece
- **Molotow 2mm spacing:** Must be 2mm+ apart, not 1mm (just overwrites)
- **Large signatures break visuals** — use classic PLUTARCO ◇ only
- **Standalone paint SVGs are dangerous** — ALWAYS use composite variants (A/B/C) from composites.html. See Paint Pass Lesson in TASTE.md

## VPS / Infrastructure
- **VPS disk full?** Pipe tar over SSH: `tar cf - src | ssh host tar xf -`
- **Paused cron jobs** vanish from `hermes cron list` but stay in `jobs.json`
- **hermes cron edit** (not update) for modifying jobs
- **Nous Portal** = OAuth via hermes model (NOT API key page)

## Memory
- Built-in memory is only 2,200 chars — use wiki for deep knowledge, memory for pointers
- Holographic (local SQLite) for structured facts — no external dependencies needed
