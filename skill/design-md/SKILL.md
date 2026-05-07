---
name: design-md
description: Generate a comprehensive DESIGN.md file by reverse-engineering the visual design system of any website. Output follows Google's official design.md format (YAML tokens + markdown rationale, lint-validated). Use when the user provides a URL or screenshot and wants a design system document, says 'design md', 'extract design system', 'reverse engineer the design', or wants to create a DESIGN.md for a site.
---

# Design MD Generator

## Purpose

Reverse-engineer any website's visual design system from its URL and produce a structured DESIGN.md file in **Google's official `design.md` format** — YAML front matter with structured tokens, plus markdown body for rationale.

The output passes `npx @google/design.md lint` and works as a portable visual identity reference for AI coding agents.

## When to Use

- User provides a URL and wants a DESIGN.md or design system document
- User says "design md", "extract design system", "reverse engineer the design"
- User wants to document a website's visual language for code generation
- User wants to create an AI-readable design reference from any live site

## Workflow

### Phase 0: Check Existing DESIGN.md

Before starting, check if a DESIGN.md already exists in the current project root. If it does:
- Ask the user: update/merge into the existing one, or create a new standalone file (e.g., `DESIGN-{brand}.md`)?
- If merging, read the existing DESIGN.md first and preserve any project-specific Decisions, Patterns, or Shared Components sections.

### Phase 1: Gather Raw Design Data

**Primary path — dembrandt CLI** (preferred for any URL):

```bash
mkdir -p /tmp/designmd-extract && cd /tmp/designmd-extract
npx -y dembrandt {URL} --save-output --pages 1 --screenshot screenshot.png --slow
```

Dembrandt extracts structured JSON with 15 top-level keys: colors (palette + semantic + CSS variables), typography (styles + sources + contexts), spacing, borderRadius, borders, shadows, components (buttons, inputs, links, badges), breakpoints, iconSystem, frameworks. The JSON lands at `output/{domain}/{timestamp}.json`.

Read that JSON as your authoritative data source. Dembrandt also writes a shallow `DESIGN.md` — **ignore it** and write your own deeper version using the JSON + the template + corpus exemplars.

**Fallback path — WebFetch + Playwright** (only if dembrandt fails):

1. **Try WebFetch first** to get the HTML and inline/linked CSS.
2. **If JS-rendered or empty**, use Playwright:
   - `npx playwright screenshot {url} --full-page screenshot.png` for a visual reference
   - A Playwright script to extract computed styles from key elements (body, h1-h6, buttons, cards, nav, inputs, links)
3. **For rich sites**, fetch 2-3 pages (homepage + pricing/docs/product) to discover more component variants.

**Screenshot-only path** (when the user provides an image, not a URL):
- Use Claude vision on the screenshot + 2-3 corpus exemplars as few-shot reference
- Mark all values as estimated with `/* estimated */` since exact CSS isn't available

Extract these categories:

**Colors:** all hex/rgb/rgba/hsl values, CSS custom properties, backgrounds, text colors, borders, semantic colors. **CRITICAL: Google's spec only accepts opaque 6-digit hex.** Plan to flatten any `rgba()`, 8-digit hex, or `oklab()` to opaque approximations.

**Typography:** font families (custom + fallbacks), OpenType features, variable font settings, font sizes, weights, line heights, letter-spacing, text transforms.

**Spacing & Layout:** padding/margin values, base unit and scale, grid/container widths, gap values.

**Border Radius:** all radius values, mapped to a scale (typically `none / sm / md / lg / pill`).

**Shadows:** all box-shadow values, layered, mapped to elevation levels.

**Components:** button variants, card styles, input/form styles, navigation pattern, badge/tag styles, image treatment.

**Responsive:** media query breakpoints, layout changes, touch target sizing.

### Phase 2: Analyze and Interpret

After gathering raw data, analyze it to identify:

1. **Brand personality** — adjectives (warm, minimal, luxurious, technical, playful, immersive)
2. **Color strategy** — monochromatic, duotone, multi-color? What role does each play?
3. **Typography signature** — weight range, tracking behavior, OpenType features
4. **Geometric language** — sharp corners vs. rounded? Pill shapes? Binary (sharp + pill) or graduated?
5. **Shadow approach** — flat, subtle, heavy? Brand-tinted? Multi-layered?
6. **Content strategy** — photography-first? Illustration-driven? Text-heavy? Dark or light default?

### Phase 3: Generate DESIGN.md (Google format)

**Read the template before writing**: `references/template.md` defines the exact YAML schema and section structure.

**Consult the corpus for prose voice**: read `references/corpus-pointer.md` to find 2-3 exemplar files in `getdesign-corpus-google/` that match the target's visual category (minimal tech, editorial dark, luxury auto, warm retail, etc.). Skim them for tone, depth, and Agent Prompt Guide richness. Don't copy content — match voice and depth.

**The output has two layers:**

1. **YAML front matter** between `---` delimiters
   - `version: alpha`, `name`, `description`
   - `colors:` — opaque 6-digit hex only, organized by role
   - `typography:` — 8-13 named tokens with fontFamily/fontSize/fontWeight/lineHeight/letterSpacing
   - `spacing:` — brand-appropriate scale
   - `rounded:` — only the values the brand actually uses
   - `components:` — every variant as a structured entry, hover/focus = separate entries with suffix

2. **Markdown body** in canonical section order
   1. `# {Brand} Design System` — title
   2. `## Overview` — was "Visual Theme & Atmosphere" in old corpus. 2-3 paragraphs design-critic prose, then 8-12 bullet "Key Characteristics"
   3. `## Colors` — group by role, reference YAML tokens via `{colors.x}`
   4. `## Typography` — font family note + token-to-use table
   5. `## Layout` — spacing rationale
   6. `## Elevation & Depth` — shadow ladder table + philosophy
   7. `## Shapes` — radius scale table (pulled out as own section in Google format)
   8. `## Components` — brief description per variant, full specs live in YAML
   9. `## Do's and Don'ts` — brand-specific rules
   10. `## Responsive Behavior` — preserved from old format (unknown section, parser keeps it)
   11. `## Agent Prompt Guide` — preserved from old format (the copy-paste payload — keep this rich)

**Critical rules to pre-empt lint failures:**

- **No `rgba()`, no 8-digit hex, no `oklab()`** in YAML. Convert to opaque approximations and add `# was rgba(...) — Google format requires hex` comment.
- **Every `{path.x}` token reference must resolve** to a declared token. Lint catches `broken-ref` errors.
- **Padding values need units** — `12px 24px` not `12 24` or `0`.
- **Radius values need units** — `0px` not `0`.
- **Hover/focus/active states are separate component entries** — `button-primary` and `button-primary-hover` are two distinct entries.
- **Component blocks reference base tokens, not raw hex** — `backgroundColor: "{colors.primary}"` not `backgroundColor: "#9891e1"`.

**If data is incomplete** (e.g., Playwright screenshot only), be honest about what's estimated vs. extracted. Mark estimated values with `/* estimated */` in prose.

### Phase 4: Lint and Save

**Lint is mandatory.** Run before saving:

```bash
npx -y @google/design.md lint /path/to/your/DESIGN.md 2>&1 | tail -30
```

- **0 errors required.** Fix and re-lint until clean.
- **Warnings are acceptable** but worth understanding:
  - `orphaned-tokens` — color declared but no component references it. Often expected (shadow tints used only in prose).
  - `contrast-ratio` — text/background pair below 4.5:1. Often intentional brand decision.
  - `missing-typography` / `missing-primary` — rare; flag for user review.

If errors persist:
- Most common fix: a YAML color is `rgba()` or 8-digit hex. Convert to opaque 6-digit.
- Second most common: a `{path.x}` reference points at an undeclared token. Either declare the token or fix the reference.
- Third: padding/radius missing unit (`0` should be `0px`).

Save the DESIGN.md to the project root (or current working directory). Use the filename decided in Phase 0.

### Phase 5: Report

Report a summary:
- Brand personality in one sentence
- Token counts (colors, typography, components)
- Lint result (errors/warnings count)
- Any data gaps where estimation was needed

Optional: mention `npx @google/design.md export <file> --format tailwind` or `--format dtcg` as a downstream step if the user wants tokens in another format.

## Playwright Computed Styles Helper

When WebFetch doesn't yield enough CSS data, run this via Bash to extract computed styles:

```javascript
const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto(process.argv[2], { waitUntil: 'networkidle' });

  const styles = await page.evaluate(() => {
    const selectors = ['body', 'h1', 'h2', 'h3', 'h4', 'p', 'a', 'button', 'input', 'nav', '[class*="card"]', '[class*="badge"]', '[class*="tag"]', 'footer'];
    const props = ['color', 'background-color', 'font-family', 'font-size', 'font-weight', 'line-height', 'letter-spacing', 'border-radius', 'box-shadow', 'padding', 'margin', 'border', 'max-width'];
    const results = {};
    for (const sel of selectors) {
      const el = document.querySelector(sel);
      if (!el) continue;
      const cs = getComputedStyle(el);
      results[sel] = {};
      for (const p of props) results[sel][p] = cs.getPropertyValue(p);
    }
    const rootStyles = getComputedStyle(document.documentElement);
    const rootVars = {};
    for (const sheet of document.styleSheets) {
      try {
        for (const rule of sheet.cssRules) {
          if (rule.selectorText === ':root' || rule.selectorText === 'html') {
            for (const prop of rule.style) {
              if (prop.startsWith('--')) rootVars[prop] = rootStyles.getPropertyValue(prop).trim();
            }
          }
        }
      } catch(e) {}
    }
    results[':root-vars'] = rootVars;
    return results;
  });

  console.log(JSON.stringify(styles, null, 2));
  await browser.close();
})();
```

## Important Guidelines

- **Exact values over approximations.** Extract actual CSS values. If a color is `#061b31`, write that — not "dark blue."
- **Name colors descriptively** in prose. "Rausch Red" for Airbnb's `#ff385c`, "Brand Indigo" for Linear's `#5e6ad2`. The YAML token uses semantic role names (`primary`, `background`, `ink`).
- **Capture OpenType features.** `"ss01"`, `"cv01"`, `"tnum"` etc. Goes in `typography.{token}.fontFeature`.
- **Document the shadow philosophy** in prose. Is it flat? Multi-layered? Brand-tinted?
- **Note the singular accent rule.** Many great design systems use ONE brand accent color. Identify it.
- **Don't invent what isn't there.** If the site has no dark mode, don't create dark mode tokens. If there's no spacing scale, derive one from observed values.
- **CSS custom properties are gold.** Capture `--var-name` naming conventions in prose; the YAML uses semantic names.
- **Multiple fetches may be needed.** The homepage alone may not reveal all component states. Fetch 2-3 key pages if sparse.
- **Mark uncertainty.** If a value was estimated from a screenshot, say so in prose.
- **Lint before declaring done.** No file ships with errors.
