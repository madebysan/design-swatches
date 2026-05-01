---
slug: paris-review
name: The Paris Review
url: https://www.theparisreview.org
domain: theparisreview.org
category: Media
styles: [Light, Editorial, Serif]
tagline: "Heldane serif at 16-26px on bone-white paper, ivy-green accents, hand-set quarterly chrome built around the issue color"
fonts: [heldane, founders-grotesk]
primary_color: "#217d05"
---

# Design System Inspired by The Paris Review

> Heldane serif at 16-26px on bone-white paper, ivy-green accents, hand-set quarterly chrome built around the issue color

## 1. Visual Theme & Atmosphere

The Paris Review's website is a literary quarterly translated to the screen with the seam-line still showing. The page sits on pure white (`#ffffff`) — but every surface, rule, and headline is set by Heldane, a transitional serif that lands somewhere between Bembo and modern Caslon. Body text runs in a deep softened black (`#414141`) at 16px, secondary text steps down to `#7d7d7d`, and the entire chrome is held together by a single chromatic note: an ivy green (`#217d05`) that tracks the "issue color" — a season-by-season accent that recolors links, hovers, and editorial flourishes as each new issue ships. There are no gradients, no shadows, and no decorative iconography. The page reads like a bound journal that has been very carefully unbound.

What makes the Paris Review unmistakable is the **dual-typeface contract between Heldane and Founders Grotesk**. Heldane (a serif from Klim Type Foundry, sub Bembo/Caslon transitional) handles every editorial heading, body paragraph, and pull quote. Founders Grotesk (a wide-figure grotesk with an `uppercase` `letter-spacing: 0.05em` cap voice) handles all UI chrome — section labels, navigation, button text, and category eyebrows. The serif sets pace; the grotesk sets structure. The contract never breaks: Heldane never appears in lowercase nav, Founders never appears as long-form body. This is a literary quarterly's editorial chrome, hand-translated from print to web with the printer's instincts intact.

The third defining trait is **near-zero ornament with one chromatic concession**. Border-radius defaults to `0` everywhere (the only `50%` use is icon dots), borders are `1px solid #000` or hairline `#d7d7d7` rules, and shadows are absent from the entire scrape (`shadows: []`). The single concession to color is the issue-color system — `--issue-color-mid: #91bf83` and the corresponding deep ivy `#217d05` — which seasonally recolors hovers, button states, and the subtle inline link-mark. It is the digital equivalent of a printed issue's spot color.

**Key Characteristics:**
- Pure white canvas (`#ffffff`) with very rare warm-paper sections (`#f7f7f7`)
- Deep softened black text (`#414141`) — never pure `#000` for body
- Dual-typeface contract — Heldane serif for editorial, Founders Grotesk for UI chrome
- Issue-color accent system — `#217d05` ivy green and `#91bf83` mid-green seasonally rotate
- Founders Grotesk UI text always set `uppercase` with positive letter-spacing (`0.04em–0.1em`)
- Heldane bodies use OpenType features: `"kern", "liga", "pnum"` (and `"onum"` for old-style figures in editorial captions)
- Border-radius is `0` — sharp rules, sharp inputs, sharp images
- Hairline rules: `1px solid #000` for editorial separators, `#d7d7d7` for tertiary
- Zero shadows in the system — depth comes from rule weight and serif weight, not blur
- Body type sits at `16px` Heldane, captions step down to `13–14px` with old-style numerals

## 2. Color Palette & Roles

### Primary Brand
- **Issue Green** (`#217d05`): The signature ivy green — used for the active link state, button hover, the inline issue-color mark above section dividers, and the brand's seasonal accent. The "issue color" is variable per quarterly issue but the spring/literary-perennial green is the canonical default.

### Brand Accent
- **Issue Color Mid** (`#91bf83`): The lightened companion green — surfaces in hover states, soft fills, and the secondary accent. From the dembrandt CSS variable `--issue-color-mid: #91bf83`. Reads as faded sage when paired with cream sections.

### Text Scale
- **Body Ink** (`#414141`): All long-form body text — the dominant text color, slightly softened from pure black for editorial readability.
- **Headline Black** (`#000000`): Display type, navigation, section headers — used where editorial weight matters most.
- **Caption Grey** (`#7d7d7d`): Secondary text, bylines, dates, image captions.
- **Tertiary Grey** (`#cccccc`): Disabled text, quiet meta labels.

### Surface & Background
- **Paper White** (`#ffffff`): The default page canvas.
- **Soft Cream** (`#f7f7f7`): Used very sparingly — alternate-section fills and table rows.
- **Hairline Tertiary** (`#d7d7d7`): Footer dividers and section separators.

### Borders & Dividers
- **Editorial Rule** (`1px solid #000000`): The signature horizontal rule under section headers — a tight, hand-set-feeling stroke.
- **Body Rule** (`1px solid #414141`): Ink-toned underlines on input fields, figure captions, and inline emphasis marks.
- **Faint Rule** (`1px solid #d7d7d7`): Tertiary card and module separators.
- **Footer Rule** (`1px solid #cccccc`): One-step-lighter footer dividers.

### Shadow System
The Paris Review is **shadow-free**. The dembrandt scrape returned `shadows: []` — no drop shadows, glows, or ambient elevations exist anywhere on the production site. Depth communicates through rule weight (`1px`, `2px`) and serif weight, not blur.

## 3. Typography Rules

### Font Family
- **Editorial / Body**: `heldane`, fallback chain: `Georgia, Cambria, "Times New Roman", Times, serif`
- **UI / Chrome**: `founders-grotesk`, fallback chain: `"Helvetica Neue", Helvetica, Roboto, Arial, sans-serif`
- **Loading source**: Adobe Fonts (verified — `adobeFonts: true` in dembrandt). Both faces are licensed via Klim Type Foundry through Adobe Fonts.
- **OpenType features**: `"kern"`, `"liga"`, `"pnum"` are universal; editorial captions add `"onum"` (old-style numerals — the digit `1` has a descender, the digit `0` is taller, signature print-quarterly feel)

For external implementation, **Bembo Std** or **EB Garamond** substitute for Heldane; **Inter** or **Söhne** can substitute for Founders Grotesk.

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Transform | Notes |
|------|------|------|--------|-------------|----------------|-----------|-------|
| Display Heading | heldane | 26px (1.63rem) | 400 | normal | normal | none | Section openers, "Issue 252" |
| Article Title | heldane | 25.6px (1.6rem) | 400 | 1.06 | normal | none | Article landing titles, headline-grade |
| Sub Headline | heldane | 24px (1.5rem) | 400 | 1.10 | normal | none | Secondary headlines |
| Card Title (large) | heldane | 20px (1.25rem) | 400 | 1.18 | normal | none | Featured-card editorial titles |
| Pull Quote / Body Lead | heldane | 16.8px (1.05rem) | 400 | 1.40 | normal | none | Article lede, opens an issue piece |
| Body | heldane | 16px (1rem) | 400 | 1.40 | normal | none | Default body — uses old-style figures (onum) |
| Body Card | heldane | 16px (1rem) | 400 | 1.40 | normal | none | Card-level body text |
| Nav / UI Label | founders-grotesk | 16px (1rem) | 500 | 1.40 | 0.05em (0.8px) | uppercase | Top-level navigation |
| Button (Light) | founders-grotesk | 16px (1rem) | 300 | 1.40 | 0.05em (0.8px) | uppercase | Primary CTA label |
| Section Eyebrow | founders-grotesk | 14px (0.88rem) | 500 | 3.43 | 0.1em (1.4px) | uppercase | Above-headline eyebrow with massive line-height as decoration |
| Tab / Filter Label | founders-grotesk | 14px (0.88rem) | 300 | 1.40 | 0.05em (0.7px) | uppercase | Tab strip, secondary nav |
| Caption Body | heldane | 14px (0.88rem) | 400 | 1.40 | 0.01em (0.14px) | none | Image captions, footnotes |
| Caption Editorial | heldane | 13px (0.81rem) | 400 | 1.40 | 0.01em (0.13px) | none | Page-level meta with old-style numerals |
| Caption Uppercase | heldane | 12px (0.75rem) | 400 | 1.80 | 0.1em (1.2px) | uppercase | Section labels, masthead chrome |
| Footer Tertiary | founders-grotesk | 12px (0.75rem) | 300 | 1.40 | 0.05em (0.6px) | uppercase | Footer links, micro-nav |
| Micro Eyebrow | founders-grotesk | 11.2px (0.7rem) | 500 | 2.50 | 0.1em (1.12px) | uppercase | The smallest UI label, often above section dividers |
| Micro Bold | founders-grotesk | 11.2px (0.7rem) | 700 | 3.21 | 0.1em (1.12px) | uppercase | Issue number markings, masthead micro-labels |

### Principles
- **Two-typeface contract is non-negotiable**: Heldane for everything editorial (titles, body, captions, pull-quotes), Founders Grotesk for everything chrome (nav, buttons, section labels, eyebrows).
- **All Founders Grotesk text is `uppercase`**: There is no lowercase Founders Grotesk anywhere in the system. Every UI label, button, and chrome string runs uppercase with positive letter-spacing.
- **Heldane stays sentence case**: Editorial headings and body text use natural sentence-case prose. Heldane never uppercases.
- **Tracking is wide on UI**: Founders Grotesk runs at `0.05em–0.1em` letter-spacing, often 1.0–1.5px positive — the printer's instinct for spacing wide caps.
- **Old-style figures for editorial captions**: `font-feature-settings: "onum"` activates for 13px and 12px editorial captions — page numbers, dates, image attributions get the print-set look.
- **Light weight on UI buttons**: Founders Grotesk weight 300 on primary CTAs is unusually light — a literary-quarterly choice. The button reads as printed annotation, not e-commerce CTA.
- **Body line-height stays at `1.4`**: Uniform across body sizes. Heldane's serifs do the visual breathing; line-height stays moderate.

## 4. Component Stylings

### Buttons (Editorial Style)

**Primary (Light Caps)**
- Background: `transparent` or white (`#ffffff`)
- Text: `#000000` or current issue green (`#217d05`)
- Border: `1px solid #000000` (bottom border only is also common — `0px 0px 1px`)
- Padding: `12px 16px` typical
- Radius: `0`
- Font: 16px Founders Grotesk weight 300, line-height 1.4, letter-spacing 0.05em, uppercase
- Hover: text recolors to `#91bf83` (issue-color-mid)
- Use: "Subscribe", "Read more", "Sign in"

**Hairline-Underline Button (Inline Editorial)**
- Background: `transparent`
- Text: `#000000`
- Border: `0px 0px 1px solid #000` — bottom border only
- Padding: `4px 0`
- Radius: `0`
- Font: 14px Founders Grotesk weight 300, uppercase, letter-spacing 0.05em
- Use: Inline article links, "More from this issue"

### Cards & Containers
- Background: `#ffffff` default; `#f7f7f7` rare alternate
- Border: top border `1px solid #d7d7d7` for stacked cards; otherwise `0`
- Radius: `0` — every editorial card is a sharp rectangle
- Shadow: `none`
- Internal padding: `24–48px` standard for editorial cards, `16px` for compact list rows

### Article Cards
- Border-top: `1px solid #d7d7d7`
- Padding: `24px 0`
- Heldane title at 20px weight 400 line-height 1.18
- Founders Grotesk eyebrow at 11.2px weight 500 letter-spacing 1.12px uppercase, in `#217d05` (issue green)
- Caption byline at 13px Heldane with `onum` numerals in `#7d7d7d`

### Inputs & Forms
- Background: `#ffffff`
- Border: `0px 0px 1px solid #000` — bottom-only ink rule, the print quarterly's signature input style
- Radius: `0`
- Font: 16px Heldane weight 400 in `#414141`
- Padding: `8px 0` (vertical only — bottom border, no left/right inset)
- Focus: border darkens, no glow, no shadow

### Navigation
- Top bar: white background, no border-bottom
- Wordmark / Masthead: Heldane at `26px` weight 400, sentence case, `#000`
- Primary nav: horizontal row of `16px Founders Grotesk weight 500 uppercase letter-spacing 0.05em` links in `#000`
- Hover: text color shifts to current issue color (`#91bf83` mid or `#217d05` deep)
- Active: text color is the deep issue green (`#217d05`)
- Section dividers: `1px solid #000` horizontal rules between major nav clusters
- Hamburger / mobile: opens to a full-screen white overlay, nav set as a vertical Heldane stack

### Links
- Default: `#414141` Heldane body, no underline
- Hover: color shifts to `#91bf83` (issue-color-mid)
- Active editorial link: `#217d05` (issue green)
- White-on-image link: `#ffffff` over photography, hover same shift to `#91bf83`

### Decorative Elements
- **Editorial Rule**: A single `1px solid #000` horizontal rule under section headers — never thicker, never dashed
- **Issue Color Mark**: a small `12px × 12px` dot or square in the issue color (`#217d05`) above section dividers — the spot-color-printed feel
- **Drop Cap**: editorial features open with a Heldane drop cap at ~`60px` line-height span 2 lines, in `#000`, with `kern + liga + onum` features active
- **Folio Numbers**: page numbers and issue numerals always in 12px Heldane with `onum` (old-style figures)

## 5. Layout Principles

### Spacing System
- Base unit: `8px` (verified — `scaleType: "8px"`)
- Common scale: `2.6px`, `3px`, `4px`, `8px`, `11.2px`, `12px`, `16px`, `22.4px`, `24px`, `32px`, `48px`, `128px`, `258px`
- The `258.4px` value is reserved for the longest-form editorial article column gutter — Paris Review pages use a long-measure column with significant outer whitespace
- The most-used values are `8px`, `16px`, `24px` — a tight 8px-base scale with editorial outer margins layered on top

### Grid & Container
- Max content width: implied at `~1200px` for landing modules
- Editorial article column: ~`640–720px` for body copy — long measure preserved for reading rhythm
- Hero: full-bleed photography with overlaid Heldane title at 25–30px, white text on dark scrim
- Footer: 4-column nav, ample top padding, `1px solid #cccccc` divider above

### Whitespace Philosophy
- **Quarterly journal pacing**: sections separated by `48–128px` vertical padding — large but not luxurious
- **Long-measure body**: editorial paragraphs sit in 640–720px columns regardless of viewport — Heldane's serifs require breathing room to read well
- **Image isolation**: photography and editorial imagery are full-bleed or contained at the article column width — never mid-size hero crops
- **Caption tightness**: image captions sit `8–12px` below image with `#7d7d7d` color and old-style numerals — distinctly tighter than body

### Border Radius Scale
- Sharp (`0`): the universal default — buttons, cards, inputs, modals, every container
- Circular (`50%`): ONLY the issue-color dot/icon — no other circular elements

The system is functionally `0`-radius. Sharpness is the brand.

## 6. Depth & Elevation

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | `box-shadow: none` | Default for every surface — articles, cards, modals at rest |
| Hairline Top Rule (Level 1) | `border-top: 1px solid #d7d7d7` | Stacked article cards in lists |
| Editorial Rule (Level 2) | `border-bottom: 1px solid #000` | Section headers, input fields, masthead dividers |
| Issue Color Mark (Level 3) | small `#217d05` color block | The single non-rule depth indicator — a print-style spot color over dividers |
| Footer Rule (Level 4) | `border-top: 1px solid #cccccc` | One-step-lighter rule reserved for footer separation |

**Shadow Philosophy**: The Paris Review uses zero drop shadows — confirmed by an empty `shadows` array in dembrandt. The system communicates depth and structure entirely through `1px` rules and the issue-color spot mark. This is not a stylistic restraint; it is the explicit aesthetic of a literary quarterly translated to web. Where most editorial sites use ambient elevation to imply premium, the Paris Review achieves the opposite by refusing to lift anything off the page. The masthead lives on the paper. The article card lives on the paper. The issue color is printed onto the paper, not hovering above it.

## 7. Do's and Don'ts

### Do
- Use Heldane (or substitute serif) for ALL editorial type — titles, body, captions, pull-quotes
- Use Founders Grotesk (or substitute grotesk) for ALL UI chrome — nav, buttons, eyebrows, section labels
- Set every Founders Grotesk string in `text-transform: uppercase` with `letter-spacing: 0.05em` minimum
- Keep Heldane sentence case — never uppercase the editorial face
- Use the issue-color system: `#217d05` deep for active states, `#91bf83` mid for hovers
- Set body text at `16px` Heldane weight 400 line-height 1.4 in `#414141`
- Default `border-radius: 0` for everything — sharp is the brand
- Use `1px solid #000` editorial rules under section headers
- Use OpenType features (`kern, liga, pnum`) on body, add `onum` for editorial captions and folio numbers
- Keep buttons `0` radius with `1px` borders or bottom-only underlines

### Don't
- Don't add drop shadows to ANY component — the system is shadow-free
- Don't lowercase Founders Grotesk text — every UI label must be uppercase
- Don't uppercase Heldane — the editorial face stays sentence case
- Don't use `border-radius` above `0` — sharpness is non-negotiable
- Don't introduce CTAs in saturated red, blue, or orange — the issue-color (green) is the only accent
- Don't tighten line-height on editorial body below `1.4` — Heldane needs breath
- Don't replace Heldane with a sans serif — the brand IS the typeface contract
- Don't substitute the issue green (`#217d05`) with a brand-bright equivalent — it must read as ivy/sage, not lime
- Don't break the column measure — editorial body sits at 640–720px regardless of viewport width
- Don't mix `pnum` and `onum` in the same paragraph — body uses `pnum`, editorial captions use `onum`

## 8. Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile | <800px | Single-column, hamburger nav, body type stays at 16px |
| Desktop | ≥800px | Multi-column issue grid, full horizontal nav, masthead expands |

The Paris Review uses a single hard breakpoint at `800px` — a refreshingly simple responsive strategy that mirrors print-issue thinking (mobile is the "small" issue, desktop is the "spread").

### Touch Targets
- Primary buttons: `44px+` tap height via `12px` vertical padding × 2 plus 16px line-height
- Nav links: `44px+` zone with generous vertical padding in mobile drawer
- Card-level link area: full card surface is tappable

### Collapsing Strategy
- **Nav**: Horizontal row collapses to hamburger icon → full-screen white overlay with vertical Heldane stack
- **Masthead**: Heldane `26px` wordmark scales down to `20px` on mobile but never simplifies
- **Hero**: Article hero stays full-bleed image with overlaid Heldane title
- **Footer**: 4-column desktop layout stacks to vertical accordion with hairline `#cccccc` dividers
- **Body**: stays at `16px` regardless of viewport — long-measure becomes single-column on mobile

## 9. Agent Prompt Guide

### Quick Reference
- Page Background: `#ffffff` (paper white)
- Body Text: `#414141` (softened black)
- Headlines: `#000000` (deep black)
- Issue Color (deep): `#217d05`
- Issue Color (mid / hover): `#91bf83`
- Caption Grey: `#7d7d7d`
- Hairline Rule: `#d7d7d7`
- Editorial Rule: `1px solid #000`
- Editorial Font: `heldane, Georgia, Cambria, "Times New Roman", serif`
- UI Font: `founders-grotesk, "Helvetica Neue", Helvetica, sans-serif`

### Example Component Prompts
- "Create an article card on `#ffffff` with a `1px solid #d7d7d7` top border, `24px 0` padding. Above the title: 11.2px Founders Grotesk weight 500 uppercase letter-spacing 0.1em in `#217d05` (issue green). Title: 20px Heldane weight 400 line-height 1.18 in `#000`. Body: 16px Heldane weight 400 line-height 1.4 in `#414141` with old-style numerals. Byline: 13px Heldane with `font-feature-settings: 'onum'` in `#7d7d7d`."
- "Design a primary CTA — transparent background, `1px solid #000` border, `0` radius, padding 12px 16px, 16px Founders Grotesk weight 300 uppercase letter-spacing 0.05em in `#000`. Hover: text shifts to `#91bf83`."
- "Build a navigation bar on `#ffffff` with the masthead in 26px Heldane weight 400 sentence case `#000`, a horizontal row of 16px Founders Grotesk weight 500 uppercase letter-spacing 0.05em links in `#000`, and `1px solid #000` divider rule between masthead and nav row."
- "Create a section eyebrow / heading pair: 14px Founders Grotesk weight 500 uppercase letter-spacing 0.1em in `#217d05`, then a 25.6px Heldane weight 400 line-height 1.06 sentence-case title in `#000`. Below: a `1px solid #000` editorial rule with 24px top margin."
- "Design an input field — `#ffffff` background, `0px 0px 1px solid #000` (bottom-only ink rule), `0` radius, padding `8px 0`, 16px Heldane weight 400 in `#414141`. No left/right padding — the line is the input. No focus glow."

### Iteration Guide
1. Default to two typefaces only: Heldane for editorial, Founders Grotesk for UI. No third face, no specialty display.
2. Founders Grotesk is ALWAYS uppercase with positive letter-spacing — there is no lowercase grotesk in the system.
3. Heldane is ALWAYS sentence case for editorial — there is no uppercase serif in the system.
4. Body type is `16px` Heldane at `1.4` line-height in `#414141`. Don't shift either value.
5. Border-radius is `0` everywhere except a single `50%` for the issue-color spot dot.
6. The page is white. Use `#f7f7f7` for alternate sections only when absolutely needed.
7. Drop shadows do not exist in this system. Use `1px` rules and the issue-color spot mark for depth.
8. The issue green (`#217d05`) is sacred — active links, button hovers, the spot mark only. Not for primary CTA fills.
9. Use OpenType features on every body block: `"kern", "liga", "pnum"` always, add `"onum"` for captions and folios.
10. Buttons use light weights (300) — Founders Grotesk should read as printed annotation, not retail signal.
