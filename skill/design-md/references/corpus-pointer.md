# Corpus Reference

The corpus of 183 real-company DESIGN.md files in **Google's `design.md` format** (YAML + markdown, lint-validated) lives in the design-swatches repo:

```
{repo-root}/getdesign-corpus-google/
```

The corpus is hosted at https://github.com/madebysan/design-swatches if you need to fetch it.

## Locating the corpus from any project

The skill can be invoked from any directory. Try these in order:

1. **Current working directory** — check if `./getdesign-corpus-google/` exists (you're working inside the repo)
2. **Common local paths** — check `~/Projects/design-swatches/getdesign-corpus-google/`, `~/Downloads/design-swatches-main/getdesign-corpus-google/`, or `~/code/design-swatches/getdesign-corpus-google/`
3. **Ask the user** if you can't find it and they want voice-matched exemplars — they may know where they cloned the repo
4. **Skip exemplar reference** — if the corpus isn't accessible, proceed without it. The template (`references/template.md`) is sufficient. You'll just lose the prose voice tuning. Lint-validate as usual.

The original prose-only corpus is preserved at `getdesign-corpus/` (same repo) for historical reference. Don't use it for new generations — it predates the Google format spec.

## How to use the corpus

**Before writing:** read 2-3 files from the corpus that match the target's visual category. Skim for:
- How the YAML front matter is organized (which color tokens, which typography names, how components reference base tokens)
- How the "Overview" section reads (evocative, design-critic voice — was "Visual Theme & Atmosphere" in the old format)
- How the color palette is documented in prose, grouped by role
- How the typography table maps token names to use cases
- How the Agent Prompt Guide writes copy-paste prompts that reference YAML tokens

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

## Files with the cleanest YAML (good template references)

These have the lowest lint warning counts, meaning their token-to-component bindings are tightly wired:

- `runwayml.md` (1 warning) — single typeface, restrained palette
- `spacex.md` (1 warning) — minimal monochrome system
- `figma.md` (3 warnings) — strict B/W chrome
- `x.ai.md` (3 warnings) — opacity-based whites flattened cleanly
- `bmw.md` (5 warnings) — single-radius, single-accent system
- `superhuman.md` (5 warnings) — small palette, near-zero waste

## Files with the richest content (deep references)

Best for matching prose voice on dense brand systems:

- `stripe.md`, `nike.md`, `meta.md`, `notion.md` — large multi-surface design systems
- `ferrari.md`, `lamborghini.md`, `bugatti.md` — luxury/automotive prose voice
- `a24films.md`, `wired.md`, `theverge.md` — editorial voice
- `clay.md`, `granola.md`, `notboring.md` — distinctive accent palettes

## Format checklist before saving

The corpus exemplars all pass lint. Match their structural patterns:

- [ ] YAML front matter with `version: alpha`, `name`, `description`, `colors`, `typography`, `spacing`, `rounded`, `components`
- [ ] All colors are opaque 6-digit hex (no `rgba()`, no 8-digit hex, no `oklab()`)
- [ ] Components reference base tokens via `{path.x}`, not raw hex
- [ ] Body section order: Overview → Colors → Typography → Layout → Elevation & Depth → Shapes → Components → Do's and Don'ts → Responsive Behavior → Agent Prompt Guide
- [ ] `npx @google/design.md lint` returns 0 errors

## Notes

- `claude-ai.md` is Anthropic's Claude (renamed from `claude.md` to avoid conflict with `CLAUDE.md` project-instruction files)
- Files run 250-650 lines (15-32KB). Richer sites produce richer files.
- All 183 files passed lint with 0 errors as of conversion. Re-run `getdesign-corpus-google/lint-all.sh` to verify.
