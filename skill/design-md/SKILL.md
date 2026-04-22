---
name: design-md
description: Generate a comprehensive DESIGN.md file by reverse-engineering the visual design system of any website from its URL. Extracts colors, typography, spacing, components, shadows, and responsive behavior into a structured 9-section markdown document optimized for AI agent consumption. Use when the user provides a website URL and wants a design system document, says 'design md', 'extract design system', 'reverse engineer the design', or wants to create a DESIGN.md for a site.
---

# Design MD Generator

## Purpose

Reverse-engineer any website's visual design system from its URL and produce a structured DESIGN.md file following the 9-section format from VoltAgent/awesome-design-md. The output is optimized for AI coding agents to use as a reference when building UIs inspired by the target site.

## When to Use

- User provides a URL and wants a DESIGN.md or design system document
- User says "design md", "extract design system", "reverse engineer the design"
- User wants to document a website's visual language for code generation
- User wants to create an AI-readable design reference from any live site

## Workflow

### Phase 0: Check Existing DESIGN.md

Before starting, check if a DESIGN.md already exists in the current project root. If it does:
- Ask the user: update/merge into the existing one, or create a new standalone file (e.g., `DESIGN-{brand}.md`)?
- If merging, read the existing DESIGN.md first and preserve any Decisions, Patterns, or Shared Components sections that contain project-specific content.

### Phase 1: Gather Raw Design Data

**Primary path — dembrandt CLI** (preferred for any URL):

```bash
mkdir -p /tmp/designmd-extract && cd /tmp/designmd-extract
npx -y dembrandt {URL} --save-output --pages 1 --screenshot screenshot.png --slow
```

Dembrandt extracts structured JSON with 15 top-level keys: colors (palette + semantic + CSS variables), typography (styles + sources + contexts), spacing, borderRadius, borders, shadows, components (buttons, inputs, links, badges), breakpoints, iconSystem, frameworks. The JSON lands at `output/{domain}/{timestamp}.json`.

Read that JSON as your authoritative data source. Dembrandt also writes a shallow `DESIGN.md` — **ignore it** and write your own deeper version using the JSON + the template + corpus exemplars.

**Fallback path — WebFetch + Playwright** (only if dembrandt fails, e.g., heavy WAF, auth gate):

1. **Try WebFetch first** to get the HTML and inline/linked CSS.
2. **If the site is JS-rendered, Framer-built, or returns mostly empty/CSS-only content**, use Playwright:
   - Use `npx playwright screenshot {url} --full-page screenshot.png` for a visual reference
   - Use a Playwright script to extract computed styles from key elements (body, h1-h6, buttons, cards, nav, inputs, links)
3. **For rich sites**, fetch 2-3 pages (homepage + pricing/docs/product) to discover more component variants.

**Screenshot-only path** (when the user provides an image, not a URL):
- Use Claude vision on the screenshot + 2-3 corpus exemplars as few-shot reference
- Mark all values as estimated with `/* estimated */` since exact CSS isn't available

Extract these categories of raw data:

**Colors:**
- All hex values, rgb/rgba values, hsl values from CSS
- CSS custom properties (`--color-*`, `--palette-*`, etc.)
- Background colors on major elements (body, header, cards, buttons, footer)
- Text colors at each hierarchy level
- Border colors, shadow colors, accent colors
- Semantic colors (error, success, warning, info states)

**Typography:**
- Font families: custom fonts (via @font-face or CDN), system fonts, fallback stacks
- OpenType features (`font-feature-settings`)
- Variable font settings (`font-variation-settings`)
- Font sizes across the hierarchy (hero/display down to micro/caption)
- Font weights used and where they appear
- Line heights, letter-spacing values
- Text transforms (uppercase, capitalize)

**Spacing & Layout:**
- Padding and margin values (identify the base unit and scale)
- Grid/container max-widths
- Gap values in flex/grid layouts
- Section spacing rhythm

**Border Radius:**
- All border-radius values, map to a scale (micro, standard, card, pill, circle)

**Shadows:**
- All box-shadow values, identify layers and opacity levels
- Map to elevation levels (flat, subtle, card, elevated, dialog)

**Components:**
- Button variants (primary, secondary, ghost, outlined, pill, icon)
- Card styles (background, border, radius, shadow)
- Input/form styles (border, focus state, radius)
- Navigation pattern (layout, colors, sticky behavior)
- Badge/tag/pill styles
- Image treatment (radius, overlay, aspect ratio)

**Responsive:**
- Media query breakpoints
- Layout changes at each breakpoint
- Touch target sizing

### Phase 2: Analyze and Interpret

After gathering raw data, analyze it to identify:

1. **Brand personality** — What adjectives describe the visual feel? (warm, minimal, luxurious, technical, playful, immersive)
2. **Color strategy** — How many brand colors? Monochromatic, duotone, or multi-color? What role does each color play?
3. **Typography signature** — What makes the type choices distinctive? Weight range, tracking behavior, OpenType features?
4. **Geometric language** — Sharp corners vs. rounded? Pill shapes? Circles? What's the border-radius philosophy?
5. **Shadow approach** — Flat, subtle, heavy? Brand-tinted? Multi-layered? How does elevation work?
6. **Content strategy** — Photography-first? Illustration-driven? Text-heavy? Dark or light default?

### Phase 3: Generate DESIGN.md

Write the document following the exact 9-section structure defined in `references/template.md`. Read that file before generating output.

**Consult the corpus for prose voice.** Before writing, read `references/corpus-pointer.md` to locate 2-3 exemplar DESIGN.md files from the 71-file corpus that match the target's visual category (minimal tech, editorial dark, luxury auto, warm retail, etc.). Skim them for tone, depth, and Agent Prompt Guide richness. Don't copy their content — match their voice and depth.

Key quality requirements:
- Every color must include the hex/rgba value AND its role/usage
- Every typography entry must include size, weight, line-height, letter-spacing
- Component styles must include exact CSS values (not descriptions like "rounded corners")
- Shadow values must be complete (full `box-shadow` syntax)
- The "Visual Theme & Atmosphere" section must read like a design critic's review — evocative, specific, opinionated
- The "Agent Prompt Guide" section must include copy-paste-ready component prompts with all CSS values inline
- Do's and Don'ts must be specific to THIS design system — no generic advice

**If data is incomplete** (e.g., Playwright screenshot was the only source), be honest about what's estimated vs. extracted. Mark estimated values with `/* estimated */` so the user knows to verify.

### Phase 4: Save and Report

1. Save the DESIGN.md to the project root (or current working directory if no project). Use the filename decided in Phase 0.
2. If a Playwright screenshot was taken, mention it so the user can cross-reference.
3. Report a summary: brand personality in one sentence, number of colors/type styles/components documented, and any gaps where data couldn't be extracted.

## Playwright Computed Styles Helper

When WebFetch doesn't yield enough CSS data, run this via Bash to extract computed styles from key elements:

```javascript
// Save as /tmp/extract-styles.mjs and run with: npx playwright test --config=... or node with playwright
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
    // Also grab CSS custom properties from :root
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
      } catch(e) {} // cross-origin sheets
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
- **Name colors descriptively.** "Rausch Red" for Airbnb's `#ff385c`, "Brand Indigo" for Linear's `#5e6ad2`. Use the brand's own naming if discoverable.
- **Identify the font stack.** Custom fonts first, then the full fallback chain as declared in CSS.
- **Capture OpenType features.** `"ss01"`, `"cv01"`, `"tnum"` etc. These define brand typography identity.
- **Document the shadow philosophy.** Is it flat? Multi-layered? Brand-tinted? Heavy or subtle?
- **Note the singular accent rule.** Many great design systems use ONE brand accent color. Identify it.
- **Don't invent what isn't there.** If the site has no dark mode, don't create dark mode tokens. If there's no explicit spacing scale, derive one from observed values.
- **CSS custom properties are gold.** If the site uses `--var-name` tokens, capture the naming convention.
- **Multiple fetches may be needed.** The homepage alone may not reveal all component states. Fetch 2-3 key pages if the homepage is sparse.
- **Mark uncertainty.** If a value was estimated from a screenshot rather than extracted from CSS, say so.
