# Corpus Reference

The corpus of 81 real-company DESIGN.md files lives in this repo at:

```
./getdesign-corpus/
```

(Relative to the repo root. From the skill folder, it's `../../getdesign-corpus/`.)

These files were extracted from [getdesign.md](https://getdesign.md) (VoltAgent/awesome-design-md) plus a handful generated locally with [dembrandt](https://github.com/dembrandt/dembrandt) for token extraction + Claude for prose. Each follows the 9-section template exactly. Use them as **prose-voice references** before writing a new DESIGN.md.

## How to use the corpus

**Before writing:** read 2-3 files from the corpus that match the target's visual category. Skim for:
- How the "Visual Theme & Atmosphere" section reads (evocative, design-critic voice)
- How the color palette is organized (by role, not hue)
- How the typography table is structured (13-18 rows typical)
- How the Agent Prompt Guide writes copy-paste prompts

**Don't copy structure blindly** — each DESIGN.md adapts depth to what the target site offers. Match the corpus's depth when the site supports it, but don't fabricate content to hit section length.

## Picking the right exemplars

Choose 1-3 corpus files that most resemble the target's visual category:

| Target style | Exemplars to consult |
|---|---|
| Minimal tech / SaaS (light) | `stripe.md`, `linear.app.md`, `vercel.md`, `cursor.md`, `notion.md` |
| Warm / editorial / paper-like | `cape.md`, `claude-ai.md`, `mintlify.md`, `sanity.md` |
| Dark developer tool / terminal | `warp.md`, `cursor.md`, `hashicorp.md`, `ollama.md` |
| Editorial / magazine / cinema | `a24films.md`, `wired.md`, `theverge.md` |
| Luxury / automotive / heritage | `ferrari.md`, `lamborghini.md`, `bugatti.md` |
| Retail / warm-consumer | `starbucks.md`, `airbnb.md`, `nike.md` |
| Bold / energetic / sport | `tesla.md`, `nike.md`, `ferrari.md` |
| Finance / trust-forward | `stripe.md`, `mastercard.md`, `revolut.md`, `wise.md` |
| AI labs / research | `claude-ai.md`, `cohere.md`, `mistral.ai.md`, `elevenlabs.md` |
| Gaming / entertainment | `playstation.md`, `spotify.md`, `spacex.md` |
| Craft tools / opinionated UI | `things.md`, `arc.md`, `fey.md`, `granola.md`, `ivory.md`, `mercury-weather.md` |

## Notes

- `claude-ai.md` is Anthropic's Claude (renamed from `claude.md` to avoid conflict with `CLAUDE.md` project-instruction files)
- Files run 250-550 lines (15-37KB). Richer sites produce richer files.
- Outliers to avoid as exemplars (thinner content): `airtable.md`, `webflow.md`, `kraken.md`
- Strongest exemplars (rich + distinctive): `stripe.md`, `a24films.md`, `ferrari.md`, `starbucks.md`, `cape.md`, `claude-ai.md`, `linear.app.md`
