# design-swatches — Project Notes

Living reference for non-obvious gotchas. Plain CLAUDE.md (global) covers san's general preferences; this file is for things specific to this repo.

## Architecture

Project root layout matters for deploys:

```
design-swatches/
├── vercel.json          # /  → /explorer/ redirect + URL fallbacks
├── explorer/            # the gallery (deployed at /explorer/)
│   ├── index.html
│   ├── bentos/{slug}.html
│   ├── thumbnails/{slug}.png
│   └── shared/          # ⚠ gitignored — local tooling only
├── getdesign-corpus/    # 167 canonical DESIGN.md files (deployed at /getdesign-corpus/)
└── research/            # refero scraping + conversion tooling
```

Key relationship: each bento HTML links to `../../getdesign-corpus/{slug}.md` for "View full DESIGN.md →". This relative path **only resolves when the deploy root is the project root, not `explorer/`**.

## Deploy gotchas (HARD-LEARNED)

- **Vercel project**: `designmd` (custom domain `designmd.santiagoalonso.com`). Don't accidentally create a new project — `vercel link --project designmd --yes` to point `.vercel/` at the right one.
- **Deploy root**: `/Users/san/Projects/_done/design-swatches/` (project root). NOT `explorer/`. If `.vercel/` ends up in `explorer/`, getdesign-corpus links 404.
- **vercel.json redirects**: don't switch `/` → `/explorer/` from a redirect to a rewrite. Rewrites silently serve the gallery HTML at `/` but break relative asset paths. The current setup also has `/bentos/*` → `/explorer/bentos/*` etc. fallbacks for old bookmarks.
- **Pre-deploy check**: `cd <project root> && cat .vercel/project.json` should show `"projectName": "designmd"`. If it shows `"explorer"`, re-link.

## Sonnet vs Opus (this project)

Empirical findings from session 3 batch4 (10 brands):

- **DESIGN.md voice/rebucket pass: Sonnet OK** (~90-95% of Opus quality at 1/5 cost). Voice imitation + structural rebucket from canonical exemplars. Use Sonnet by default.
- **Bento HTML generation: Opus until Sonnet brief is hardened.** Sonnet produced 5/10 bentos with broken sidebars (custom `<aside>` HTML, 0-indent CSS that bypassed modernize regex, "Filter tiles..." instead of "Search" placeholder). Both an Opus default AND a tighter Sonnet brief that says "use the EXACT sidebar HTML from `aceternity.html`, don't invent" are workable answers.

## Live taxonomy (categories + styles)

When integrating new brands, frontmatter `category:` MUST match the 13 live categories in `explorer/shared/brand-categories.json`:

> AI · Dev Tools · Design System · Media · Retail · Finance · SaaS · Productivity · Design · Auto · Enterprise · Gaming · Browser

`research/convert-refero-to-canonical.py` has an `INDUSTRY_TO_CATEGORY` map that historically introduced "AI Lab", "Music", "Type Foundry", "Developer Tools" — these create single-brand orphan filters. Either remap pre-integration or fix the converter's table.

Live styles tags: `Bold · Colorful · Cool · Dark · Editorial · Gradient · Light · Mono · Minimal · Minimalist · Monochromatic · Playful · Serif · Tactile · Warm`. New styles tags are OK if the brand genuinely calls for one.

## Pipeline scripts (`explorer/shared/`, gitignored)

- `modernize-bentos.py` — idempotent patcher (favicon, theme init, sidebar CSS, sb-head HTML, full-width canvas, Search placeholder). **Brittle regex**: requires 2-space indent on `.sidebar {`; doesn't handle some sb-head child orderings. Sonnet output variations have triggered silent skips → backlog has a hardening item.
- `regen-all-sidebars.py` — rewrites `<ul class="sb-list" id="sbList">` content across all bentos
- `regen-gallery-index.py` — injects DOMAINS + CATEGORIES inline into `explorer/index.html`
- `screenshot-bentos.sh` — Playwright batch screenshot, crops 240px sidebar off the left
- `fix-batch4-sidebars.py` + `fix-batch4-sidebar-html.py` — one-shot fixers from session 3 for broken Sonnet output. Reuse pattern if future Sonnet batches break.

## Refero pipeline (`research/`)

Generated 2026-05-01 to ingest the 1,247 brands from styles.refero.design that aren't in our corpus.

- `build-refero-mds.py` — paginate `/api/styles?page=N&limit=100`, write thin .md
- `fetch-refero-details.py` — hit `/api/styles/{id}`, write rich .md from `style.fullResult.designSystem`
- `convert-refero-to-canonical.py` — mechanical refero → canonical 9-section. ~70% canonical out the box; needs LLM follow-up for §1 voice expansion + §4 component re-bucket + §8 responsive defaults

`research/refero-data/` (3,700+ files) is gitignored. Re-running the fetch is safe — resume-aware via existence check.

## Workflow for adding a refero batch (10-25 brands)

See `plan.md` "Future-batch refero workflow" — full step-by-step. Key points:
1. Cherry-pick by recognizable + design-distinctive + category-gap fit
2. Run mechanical converter
3. Sonnet voice/rebucket pass → `getdesign-corpus/`
4. Post-edit category strings to live taxonomy
5. Opus bento generation
6. Standard pipeline (modernize, screenshots, regen, deploy from project root)
