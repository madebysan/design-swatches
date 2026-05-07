# Corpus Conversion Report

**183/183 files converted from the legacy swatches format to Google's `design.md` format. All pass lint with 0 errors.**

Original: `getdesign-corpus/` (legacy prose-first, 9 sections)
Converted: `getdesign-corpus-google/` (YAML tokens + markdown rationale)

## Method

- 98 files came from the v2 Google-format conversion.
- 85 local-only legacy files were converted from `getdesign-corpus/` into the same Google format.
- Each converted file now has YAML front matter with `version`, `name`, `description`, `colors`, `typography`, `spacing`, `rounded`, and `components`.
- The body was normalized to Google's canonical section order, with `Responsive Behavior` and `Agent Prompt Guide` preserved as extra sections.
- Every file was linted with `npx @google/design.md lint`.

## Results

- **Files converted**: 183 / 183 (100%)
- **Lint errors**: 0 / 183
- **Total warnings**: 2,224 (mean 12.2 per file)
- **Corpus size**: 3.9MB → 4.5MB (+15% from YAML overhead and structured component blocks)

### Warning distribution

| Bucket | Count |
|---|---:|
| Files with ≤5 warnings | 11 |
| Files with 6-15 warnings | 121 |
| Files with 16-25 warnings | 44 |
| Files with 26+ warnings | 7 |

Warnings are not errors. The Google linter flags useful review areas:

- **`orphaned-tokens`** — a token is declared in YAML but no `components.*` entry references it. This is expected for colors described in prose, shadow tints, and secondary brand accents.
- **`contrast-ratio`** — a text/background pair is below WCAG AA. Some are intentional brand decisions, especially in editorial, luxury, or muted systems.
- **`missing-typography` / `missing-primary`** — rare warnings to review when a brand has a very restrained or monochrome system.

### Highest warning counts

| File | Warnings |
|---|---:|
| `nike.md` | 43 |
| `meta.md` | 38 |
| `untitled-ui.md` | 32 |
| `fluent.md` | 30 |
| `notboring.md` | 28 |
| `granola.md` | 27 |
| `clay.md` | 26 |
| `ios-hig.md` | 25 |
| `mercury-weather.md` | 25 |
| `composio.md` | 24 |
| `tremor.md` | 24 |
| `vercel.md` | 24 |

### Cleanest files

| File | Warnings |
|---|---:|
| `runwayml.md` | 1 |
| `spacex.md` | 1 |
| `figma.md` | 3 |
| `x.ai.md` | 3 |
| `zapier.md` | 3 |
| `renault.md` | 4 |
| `replicate.md` | 4 |
| `bmw.md` | 5 |
| `revolut.md` | 5 |
| `superhuman.md` | 5 |
| `warp.md` | 5 |

## Format conversions applied

| Conversion | Reason |
|---|---|
| `rgba(...)`, `hsla(...)`, `oklab(...)`, and 8-digit hex values flattened to opaque 6-digit hex where they appear in YAML | Google spec only accepts opaque hex color tokens |
| Border radius and padding values normalized with explicit units | Lint requires values like `0px` and `12px 24px` |
| 9-section body converted to canonical Google section order | Google lint checks section ordering |
| "Visual Theme & Atmosphere" moved into `Overview` | Google uses `Overview` as the canonical first section |
| Radius guidance pulled into `Shapes` | Google has a dedicated Shapes section |
| Reusable component values encoded under `components:` | Enables linting and downstream export |

## Preserved content

- The original design-critic prose is preserved in each `Overview` where available.
- Legacy `Responsive Behavior` sections are preserved after the canonical sections.
- Legacy `Agent Prompt Guide` sections are preserved as the copy-paste payload.
- The original prose-first corpus remains in `getdesign-corpus/` for reference.

## Validation

Run `./lint-all.sh` from this directory to re-validate every file. It writes `lint-results.tsv`.

```
Total files: 183
Pass (0 errors): 183
Fail (>0 errors): 0
```

Generated: 2026-05-07
