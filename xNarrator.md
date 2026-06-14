# xNarrator

> *AI-generated audio content from X posts. Fully automated pipeline.*

---

## What It Is
Reads REAL X posts in DIFFERENT VOICES per author. NOT documentary. Narrator = attributions only. Posts read by cloned/roster voice.

**26 voices total.** YouTube channel: @xNarratorHQ

---

## Pipeline (10 Steps)

1. **bird** scrapes X posts → JSON
2. **Review** — filter for quality/relevance
3. **Assign** — map each author to a voice
4. **Script** — format for TTS with proper breaks
5. **Chatterbox on Vast.ai** — generate audio per voice ⚠️ ALWAYS Chatterbox, NEVER OpenAI TTS
6. **Resample 24kHz → 44100Hz FIRST** — CRITICAL: Chatterbox outputs 24kHz, MUST resample before concat or chipmunk audio
7. **Stitch** — concatenate all segments
8. **Normalize** — loudness normalization
9. **Preview MP3 for Phillip** — ALWAYS preview before YouTube upload
10. **Upload to YouTube**

---

## Voice Assets

**Location:** `~/projects/xnarrator/voices/`

### Cloned Voices (11)
alexjones, candace, fuentes, garrytan, greenwald, karpathy, kirk, mtg, sama, shroyer, vitalik

### Narrator
`narrator/narrator.wav` — V15 Justin voice

### Helena
`helena/helena.wav`

### Roster
`voice-roster/` — 10M+7F voices + ROSTER.md + pmarca_voice.wav

**Total: 39 .wav files**

---

## YouTube
- **Channel:** @xNarratorHQ
- **OAuth tokens:** `~/projects/xnarrator/youtube/`
- **Upload script:** In same directory
- **Thumbnail:** `gen_episode_thumbnail.py` on `today_on_x_template.png`

---

## Chrome Extension
`~/projects/xnarrator/extension/` — For capturing X content

## Intro Music
`~/projects/xnarrator/intro_music/` — 4 tracks

---

## Cron Jobs (CURRENTLY PAUSED)
- **Daily Scrape** — 4:00 AM
- **Weekly Scout** — Monday 10:00 AM

---

## ⚠️ Critical Rules
- **ALWAYS** Chatterbox on Vast.ai for TTS
- **NEVER** OpenAI TTS
- **ALWAYS** resample 24kHz → 44100Hz BEFORE concatenation
- **ALWAYS** preview MP3 for Phillip before YouTube upload
- Narrator voice = `narrator.wav` (V15 Justin)
