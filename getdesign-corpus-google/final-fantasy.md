---
version: alpha
name: "Final Fantasy"
description: "Square Enix red `#c80000` on near-paper-white, Proxima Nova bold at 44px, restrained corporate-game-publisher chrome."

colors:
  background: "#ffffff"
  surface: "#f0f0f0"
  surface-elevated: "#f5f5f5"
  ink: "#111111"
  ink-muted: "#4d4d4d"
  primary: "#c80000"
  on-primary: "#ffffff"
  border: "#a6a6a6"
  focus-ring: "#c80000"
  success: "#22c55e"
  warning: "#f59e0b"
  error: "#ef4444"
  shadow-soft: "#d9d9d9"

typography:
  display-hero:
    fontFamily: "Proxima Nova, ui-sans-serif, system-ui, sans-serif"
    fontSize: 72px
    fontWeight: 400
    lineHeight: 1.05
    letterSpacing: -1px
  display:
    fontFamily: "Proxima Nova, ui-sans-serif, system-ui, sans-serif"
    fontSize: 50px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.5px
  heading-section:
    fontFamily: "Proxima Nova, ui-sans-serif, system-ui, sans-serif"
    fontSize: 42px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.25px
  heading-sub:
    fontFamily: "Proxima Nova, ui-sans-serif, system-ui, sans-serif"
    fontSize: 29px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0px
  body-large:
    fontFamily: "Proxima Nova, ui-sans-serif, system-ui, sans-serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  body:
    fontFamily: "Proxima Nova, ui-sans-serif, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  button-ui:
    fontFamily: "Proxima Nova, ui-sans-serif, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: 0px
  caption:
    fontFamily: "Proxima Nova, ui-sans-serif, system-ui, sans-serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0px

spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  2xl: 48px
  3xl: 64px
  4xl: 96px

rounded:
  none: 0px
  sm: 4px
  md: 8px
  lg: 16px
  pill: 9999px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.pill}"
    padding: 12px 24px
  button-primary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.background}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.pill}"
    padding: 12px 24px
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.pill}"
    padding: 12px 24px
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: 24px
  input:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 12px 16px
  input-focus:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    borderColor: "{colors.focus-ring}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 12px 16px
  badge:
    backgroundColor: "{colors.surface-elevated}"
    textColor: "{colors.ink-muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.pill}"
    padding: 4px 10px
---

# Final Fantasy Design System

## Overview

The Square Enix landing page for Final Fantasy is a **publisher-portal** rather than a game-UI surface — and the chrome reflects that. Where the JRPG itself is famous for cobalt menu windows, gold-highlight selections, and Optimus-Princeps-style display serifs with drop shadows, the corporate-facing site at `finalfantasy.square-enix-games.com` redirects to a Square Enix news article hub with a much quieter aesthetic: paper-white canvas (`#f0f0f0`), Proxima Nova as the workhorse sans, and the brand's characteristic deep red (`#c80000`) doing all the heavy lifting as the single chromatic accent.

The typographic signature is **Proxima Nova at weight 700, sized from 24px up to 44px** — a humanist sans designed by Mark Simonson that has become the de-facto "premium publisher" face for game and entertainment companies. At 44px / line-height 1.50 / weight 700, it carries every page H1. Below it, weights 600, 500, and 400 cascade down to 12px caption text. There is no display serif, no Optimus-Princeps moment, no fantasy chrome on the corporate site — that aesthetic lives **inside** the games and on dedicated marketing landings, not on this publisher hub. For external implementations that want the in-game feel, layer a serif display face like **Cinzel**, **Cormorant Garamond**, or true **Optimus Princeps** for hero moments.

What makes the page feel **publisher-restrained** is the **near-empty radius scale** (only `4px` for buttons, `14px` for span chips, `32px` for one button, and `50%` for modal close buttons), the **single-shadow system** (one drop shadow plus a 1920px-wide modal scrim), and the **dotted-row dividers** in `rgb(230, 230, 230)`. The page reads like a press-release portal — calm, gridded, restrained — with the red `#c80000` reserved exclusively for date stamps, logos, and form-field borders. This DESIGN.md captures both the extracted publisher-portal chrome AND the public-knowledge in-game JRPG aesthetic, so an agent generating "Final Fantasy" content has both registers available.

**Key Characteristics:**
- Square Enix Red `#c80000` — 69 occurrences as the primary chromatic accent (date stamps, logos, form borders)
- Proxima Nova workhorse sans, weights 400/500/600/700, sized 12–44px
- Paper White `#f0f0f0` link/text canvas — 120 occurrences (the dominant content tone)
- Mid Gray `#a6a6a6` for secondary text — 48 occurrences
- Charcoal `#4d4d4d` for newsletter chrome and language switcher — 30 occurrences
- Hover red shifts to `#f71a27` — single-step brighter, more saturated red
- Sparse radius scale: 4px buttons, 14px span chips, 32px feature buttons, 50% modal closes
- Dotted-row dividers `rgb(230, 230, 230) 1px 0px 0px solid none none` — subtle hairline rhythm
- No declared shadow system on the homepage — the page lives flat
- *In-game JRPG aesthetic (estimated from public knowledge):* cobalt menu windows (`#1a3a8e`), gold-select highlights (`#ffd700`), Optimus Princeps display serif with drop shadows

## Colors

### Primary Brand
- **Square Enix Red** (`#c80000`): The brand-defining accent. 69 occurrences. Used for date stamps, the logo wordmark, form-field 1px solid borders, and select interactive moments. A deep blood-red — saturated but not bright. Distinct from the in-game palette.
- **Hover Red** (`#f71a27`): Single-step brighter red used on `:hover` states. Slightly more saturated and orange-leaning than the rest red.

### Brand Accent (In-Game / Estimated)
- **Cobalt Menu Blue** (`#1a3a8e`): /* estimated */ The signature window-fill of FF menu UIs since FFI. Use for hero panels, fantasy chrome, "fantasy mode" surfaces.
- **Gold Highlight** (`#ffd700`): /* estimated */ The select-cursor / active-row color in FF menu UIs. Reserve for active states, "selected" cues, hover on fantasy chrome.
- **Crystal Cyan** (`#7fdbff`): /* estimated */ The magic/spell tint used across multiple FF UI palettes for accent highlights and crystal motifs.

### Text
- **Paper White** (`#f0f0f0`): Primary text and link color — 120 occurrences. Slightly off-white, suggesting a near-paper or aged-print feel. Doubles as a content surface tone.
- **Mid Gray** (`#a6a6a6`): Secondary text — 48 occurrences. Used for de-emphasized metadata and form labels.
- **Charcoal** (`#4d4d4d`): Tertiary chrome — newsletter strip, language switcher, footer text. 30 occurrences.
- **Hover Mute** (`#cccccc`): Single-step brighter gray for `:hover` on muted text.

### Surface
- **Paper White** (`#f0f0f0`): Primary content canvas. The page is light-default, with content surfaces sitting on this near-white tone.
- **Pure White** (`#ffffff`): Reserved for elevated buttons and form-input fills. 1px solid white borders appear on dark-anchored buttons (3 occurrences).
- **Charcoal** (`#4d4d4d`): The dark-mode alternative — used for newsletter strips, language switchers, and grounded chrome anchors.
- **Black Modal Scrim** (`rgba(0, 0, 0, 0.66)`): The 1920px-wide modal overlay scrim — the system's dramatic depth moment.

### Border System
- **Top Divider** (`rgb(230, 230, 230)`): `1px 0px 0px` solid top border on `<div>` rows — the dotted-row rhythm of the news index. 6 occurrences.
- **Charcoal Border** (`rgb(58, 58, 58)`): 2px solid border on `<span>` chips — used for emphasized inline tags. 3 occurrences.
- **White Border** (`rgb(255, 255, 255)`): 1px solid white on dark buttons — 3 occurrences.
- **Red Border** (`#c80000`): 1px solid red on form chrome — 2 occurrences. The red-bordered input is a Square Enix tell.
- **Light Gray Border** (`rgb(191, 191, 191)`): 1px solid on default inputs — utility chrome.

### Status & Highlight
- **Square Enix Red** (`#c80000`): Doubles as the "new" / "release date" / "highlight" color. There is no separate sale/promotional tint.
- **No declared error/warning colors** — the page does not surface form validation chrome on the homepage.

### Gradient System
- The Square Enix portal page is **gradient-free**. All depth comes from solid color blocks, dotted dividers, and the modal scrim.
- *In-game FF gradients (estimated):* The classic FF menu window uses a vertical gradient from cobalt `#1a3a8e` to a darker `#0a1f5e` — used for hero surfaces only when going for the in-game register.

## Typography

### Font Family
- **Primary Sans**: `proxima-nova` (Adobe Fonts / Typekit). 700/600/500/400 weights used. The publisher-portal workhorse face.
- **Display Serif (Estimated In-Game)**: `Optimus Princeps`, `Cinzel`, or `Cormorant Garamond` for fantasy chrome. /* estimated */ Not present on the publisher portal but synonymous with FF marketing materials and in-game logo treatments since FFXII.
- **System Sans Fallback**: `sans-serif` — a single 34px link occurrence escapes Proxima Nova and falls to system stack.

*Note: Proxima Nova requires an Adobe Fonts subscription for production use. **Inter** at weight 600/700 is the closest open-source substitute. For Optimus Princeps fantasy chrome, **Cinzel** (Google Fonts) is the most accessible substitute — same Roman-capitals-with-flourish character.*

### Hierarchy

| Role | Font | Size | Weight | Line Height | Notes |
|------|------|------|--------|-------------|-------|
| Page H1 (XL) | proxima-nova | 44px (2.75rem) | 700 | 1.50 | Page-anchor headline |
| Button (XL) | proxima-nova | 36px (2.25rem) | 400 | 1.15 | Largest button label — feature CTA |
| Link (XL) | sans-serif | 34px (2.13rem) | 400 | 1.50 | Single fallback occurrence |
| H1 / Link (L) | proxima-nova | 32px (2rem) | 700 | 1.15 | Section heads |
| Link (L-mid) | proxima-nova | 30px (1.88rem) | 600 | 1.50 | Sub-section anchors |
| H1 (mid) | proxima-nova | 28px (1.75rem) | 700 | 1.00 | Card titles, feature names |
| Link / Button (mid) | proxima-nova | 24px (1.50rem) | 400/600 | 1.00–1.15 | Feature button label |
| H1 (small) | proxima-nova | 22px (1.38rem) | 700 | 1.30 | Compact card titles |
| Body Large | proxima-nova | 18–20px | 400 | 1.50 | Lead paragraphs |
| Body | proxima-nova | 16px (1rem) | 400 | 1.50 | Standard reading body |
| Caption / UI | proxima-nova | 14px (0.88rem) | 400–500 | 1.40 | Metadata, byline |
| Micro | proxima-nova | 12px (0.75rem) | 400 | 1.40 | Footer microcopy |

*Estimated in-game hierarchy (for fantasy-mode work):*
- Hero Display: Optimus Princeps / Cinzel 64–96px weight 600, drop-shadow `0 2px 4px rgba(0,0,0,0.8)`, gold `#ffd700` on cobalt `#1a3a8e`
- Menu Heading: Cinzel 24–32px weight 500, white on cobalt window
- Menu Body: Optimus Princeps 16–20px weight 400, white on cobalt

### Principles
- **Weight 700 is the publisher headline.** Every page H1 lands on Proxima Nova 700 — there is no light-weight display moment on the corporate site.
- **Restrained casing.** Title case dominates, no ALL-CAPS hero treatments.
- **No serif on the portal.** The publisher-facing site is 100% Proxima Nova sans. The serif fantasy register lives only in game-marketing landings.
- **Compact line-height on display.** 28px headings run at line-height 1.00 — tight stacking for press-release efficiency.
- **No letter-spacing.** Every typography rule omits letter-spacing — type runs at default tracking.
- *In-game estimated:* JRPG menu chrome uses a serif display face with hard 1–2px drop shadows in pure black, simulating crystal/etched-stone engravings.

## Layout

### Spacing System
- Base unit: estimated 8px (no explicit `spacing.commonValues` extracted from the publisher portal)
- Scale (estimated): 4, 8, 12, 16, 24, 32, 48, 64, 96px
- Section padding: 48–96px between major panels
- Card padding: 16–24px standard

### Grid & Container
- Estimated max content width: 1200px
- News list: single-column dense list with dotted-row dividers
- Feature panels: occasional 2–3 column grids for game-spotlight rows
- *In-game estimated:* fixed 16:9 viewport with 8-row × 16-col grid for menu windows

### Whitespace Philosophy
- **Press-release pacing.** Sections breathe modestly with 48–64px between blocks — not luxurious, but enough to feel calm
- **Dotted-row rhythm.** The news list uses 1px top-borders in `rgb(230, 230, 230)` to pace items — a calm horizontal grid
- *In-game estimated:* fantasy-mode chrome packs density inside menu windows, with 8–12px gaps between rows and 16–20px outer padding

### Border Radius Scale
- Sharp (`0px`): Default elements, news rows
- Compact (`4px`): Buttons, modal containers
- Mid (`14px`): Span chips, inline tags
- Feature (`32px`): Hero CTAs
- Pill (`50%`): Modal close buttons

## Elevation & Depth

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | No shadow | Default page surfaces |
| Soft Lift (Level 1) | `rgba(0, 0, 0, 0.1) 1px 1px 10px 1px` | Modal containers, elevated cards |
| Ring Highlight (Level 2) | `rgb(204, 204, 204) 0px 0px 2px 2px` | Focus / hover state |
| Modal Scrim (Level 3) | `rgba(0, 0, 0, 0.66) 0px 0px 0px 1920px` | Modal overlay backdrop |
| In-Game Engraving (Estimated) | `0 2px 4px rgba(0, 0, 0, 0.8)` | Fantasy mode display type drop shadow |

**Shadow Philosophy**: The publisher portal's depth system is **almost entirely flat** — only three shadow patterns appear on the homepage. The dramatic moment is reserved for the modal scrim, which uses a 1920px-wide box-shadow as an overlay. There is no Material Design elevation tier system here.

*In-game philosophy (estimated):* Fantasy mode uses **hard 2px drop shadows** in pure black for engraved display type, simulating crystal/stone engravings. Menu windows use a single soft 4px drop shadow at 0.5 opacity for floating panels.

## Shapes

The complete radius scale is declared in the `rounded:` token block above.

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Hard-edged brand moments and flush layouts |
| `sm` | 4px | Small controls and tight UI details |
| `md` | 8px | Inputs and compact interface elements |
| `lg` | 16px | Cards and larger containers |
| `pill` | 9999px | CTAs, chips, and rounded badges |

## Components

### Buttons

**Primary — Red Pill (Estimated for Fantasy Mode)**
- Background: `#c80000` (Square Enix Red)
- Text: `#ffffff`, Proxima Nova 16px weight 700
- Padding: `12px 24px`
- Radius: `4px` (publisher chrome) or `32px` (feature button)
- Border: none
- Hover: background shifts to `#f71a27` (brighter red)
- Use: Newsletter signup, primary publisher CTAs

**Feature Pill (32px Radius)**
- Background: `#ffffff` or `#c80000`
- Text: 24px Proxima Nova weight 400
- Padding: `12px 32px`
- Radius: `32px`
- Border: optional `1px solid #ffffff`
- Use: "Watch Trailer", "Learn More" hero CTAs

**Standard Button (4px)**
- Background: `#4d4d4d` or `#ffffff`
- Text: Proxima Nova 14–16px weight 500
- Padding: `8px 16px`
- Radius: `4px`
- Border: optional `1px solid rgb(255, 255, 255)` on dark
- Use: News-list affordances, secondary CTAs

**In-Game Cobalt Menu Button (Estimated)**
- Background: `#1a3a8e` (Cobalt Menu Blue) /* estimated */
- Text: `#ffffff`, Cinzel 18px weight 500
- Border: `1px solid #ffd700` (gold) on the active/selected state
- Drop shadow: `0 2px 4px rgba(0,0,0,0.8)` — hard fantasy-engraving shadow
- Use: In-game menu windows, fantasy-mode surfaces

### Cards & Containers

**News Index Row**
- Background: transparent over `#f0f0f0` paper canvas
- Border: `rgb(230, 230, 230) 1px 0px 0px solid none none` — top-only dotted rhythm
- Radius: `0`
- Padding: 16–24px
- Use: News list items, article previews

**Feature Card (Estimated In-Game Treatment)**
- Background: `#1a3a8e` cobalt or photographic key art /* estimated */
- Border: `2px solid #ffd700` gold for selected state
- Radius: `4px` or sharp `0px`
- Drop shadow: `0 4px 12px rgba(0,0,0,0.5)`
- Use: Game-spotlight panels, fantasy chrome

### Badges / Tags / Pills

**Span Chip (14px Radius)**
- Background: transparent or `#4d4d4d`
- Text: Proxima Nova 12–14px weight 500
- Padding: `4px 14px`
- Radius: `14px`
- Border: `2px solid rgb(58, 58, 58)` for emphasized variant
- Use: Genre tags, "release date" chips, news category labels

### Inputs & Forms

**Standard Input**
- Background: `#ffffff`
- Text: `#4d4d4d`
- Border: `1px solid rgb(191, 191, 191)`
- Radius: `0` or `4px`
- Padding: 8–12px

**Red-Bordered Input (Newsletter)**
- Background: `#ffffff`
- Border: `1px solid #c80000`
- Radius: `0` or `4px`
- Use: Newsletter signup form — the red border is a Square Enix tell

### Navigation

- Top nav: charcoal `#4d4d4d` strip with white wordmark and Proxima Nova 14–16px weight 500 links
- Hover: text color shifts; no underline appears
- Sticky behavior: fixed on scroll
- Mobile: collapses to hamburger drawer

### Modal / Overlay

- Backdrop scrim: `rgba(0, 0, 0, 0.66) 0px 0px 0px 1920px` — a 1920px-wide box-shadow used as a scrim. The most dramatic depth moment.
- Modal container: white `#ffffff` panel with `4px` radius and a single soft drop shadow `rgba(0, 0, 0, 0.1) 1px 1px 10px 1px`
- Close button: 50% radius circular icon button

### In-Game Decorative Elements (Estimated)

- **Cobalt menu windows**: gradient cobalt fill `#1a3a8e → #0a1f5e`, with `1px solid white` border and `2px solid gold` inner border — the iconic FF menu chrome
- **Gold cursor / selection arrow**: gold `#ffd700` triangle pointer indicating active row
- **Crystal motif**: cyan `#7fdbff` accent highlights on magic/spell labels
- **Fantasy logo treatment**: title in Cinzel-style serif with hard 2px drop shadow and gold-to-amber gradient fill

## Do's and Don'ts

### Do
- Use Square Enix Red `#c80000` for date stamps, logos, and form-field borders — the brand's signature accent
- Apply Proxima Nova weight 700 for all H1s sized 22–44px on the publisher portal
- Use the `rgb(230, 230, 230) 1px 0px 0px` top-only border for news-list rows
- Reserve the `#f71a27` brighter red for `:hover` states only — never as a default
- For fantasy mode, layer in cobalt menus (`#1a3a8e`), gold highlights (`#ffd700`), and Cinzel/Optimus serif display
- Use 4px border-radius for buttons, 14px for span chips, 32px for feature CTAs
- Apply hard 2px black drop shadows for in-game-mode display type — engraved fantasy feel
- Keep the publisher-portal chrome quiet — the games are loud, the portal is calm

### Don't
- Don't introduce additional saturated colors on the publisher portal — it lives in red + grays + whites only
- Don't use display serifs on the corporate page — Proxima Nova is the publisher voice
- Don't soften the red to coral, salmon, or burgundy — Square Enix red is `#c80000`
- Don't blur the in-game drop shadows — fantasy chrome uses hard 2px shadows in pure black
- Don't mix the publisher and in-game registers in one composition without a clear hand-off — the two aesthetics are deliberately separate
- Don't ALL-CAPS the hero — Square Enix uses title and sentence case
- Don't add gradients to the corporate portal — the system is solid-color flat

---

## Responsive Behavior

### Breakpoints
The extracted data does not declare explicit breakpoints — the publisher portal uses implicit fixed-width container behavior. Estimated:

| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile | <640px | Single-column news list, hamburger nav, reduced typography |
| Tablet | 640–1024px | Single-column with wider content rail, condensed nav |
| Desktop | 1024–1280px | Full multi-column feature grids, max hero typography (44px) |
| Large Desktop | ≥1280px | Container caps ~1200px, expanded outer margins |

### Touch Targets
- Buttons: 40–48px tall (Proxima Nova 14–16px + 8–12px vertical padding)
- Nav links: ~36–44px tap area through padding
- News-row tap targets: full-row clickable, ~80–120px tall

### Collapsing Strategy
- Nav: full horizontal nav collapses to hamburger drawer on mobile
- Type scale: 44px → 32px → 24px → 22px progressive heading scale
- Section padding: 96px → 64px → 48px → 32px
- Feature grids: 3-col → 2-col → 1-col

### Image Behavior
- Game key art: 16:9 hero crops with `object-fit: cover`
- Article thumbnails: 4:3 or 16:9 thumbnails, lazy-loaded
- *In-game estimated:* fixed-aspect menu windows preserve 16:9 framing without art-direction swaps

---

## Agent Prompt Guide

### Quick Color Reference

**Publisher Portal (Extracted):**
- Brand Red: `#c80000`
- Hover Red: `#f71a27`
- Paper White: `#f0f0f0`
- Pure White: `#ffffff`
- Charcoal: `#4d4d4d`
- Mid Gray: `#a6a6a6`
- Mute Hover: `#cccccc`
- Border: `rgb(230, 230, 230)` (top-only divider)

**In-Game / Fantasy Mode (Estimated):**
- Cobalt Menu: `#1a3a8e` /* estimated */
- Gold Select: `#ffd700` /* estimated */
- Crystal Cyan: `#7fdbff` /* estimated */

### Example Component Prompts

1. *"Create a publisher hero on `#f0f0f0` paper white with a Proxima Nova 44px weight 700 headline in `#4d4d4d` charcoal, line-height 1.50. Below it, a 18px Proxima Nova weight 400 lead paragraph. CTA button in `#c80000` Square Enix Red with white text, 32px border-radius, 12×32px padding."*

2. *"Build a news-index row: full-width on `#f0f0f0`, top border `rgb(230, 230, 230) 1px 0px 0px solid`, 16–24px padding, headline in Proxima Nova 22px weight 700, date stamp in `#c80000` Square Enix Red 14px weight 500."*

3. *"Style a span chip: `#4d4d4d` background, `#f0f0f0` text in Proxima Nova 12px weight 500, `4px 14px` padding, `14px` border-radius. Emphasized variant gets `2px solid rgb(58, 58, 58)` border."*

4. *"Design a fantasy-mode menu window (in-game register): `#1a3a8e` cobalt background with vertical gradient to `#0a1f5e`, 1px solid white outer border, 2px solid `#ffd700` gold inner border. Title in Cinzel serif 24px weight 500 in white, drop shadow `0 2px 4px rgba(0, 0, 0, 0.8)`. Active row gets a gold triangle cursor on the left."* /* estimated */

5. *"Build a newsletter signup form: white `#ffffff` input with `1px solid #c80000` red border (the Square Enix tell), Proxima Nova 14px weight 400 placeholder. Submit button in `#c80000` red with white text, 4px radius."*

6. *"Create a modal overlay: backdrop scrim using `rgba(0, 0, 0, 0.66) 0px 0px 0px 1920px` box-shadow trick. Modal container is `#ffffff` with `4px` radius and `rgba(0, 0, 0, 0.1) 1px 1px 10px 1px` soft drop shadow. Close button is a 50%-radius circular icon."*

### Iteration Guide

1. **Audit the red.** Square Enix red is `#c80000` (deep blood red), hover is `#f71a27`. If you see `#ff0000`, `#dc143c`, or any other red, correct it.
2. **Audit the typography register.** Publisher portal = Proxima Nova sans, all weights. In-game / fantasy mode = Cinzel or Optimus Princeps serif. Don't mix the two without intent.
3. **Audit the radius scale.** Publisher buttons land on 4px or 32px. Span chips at 14px. Modal closes at 50%. There is no 8px or 12px middle ground.
4. **Audit shadow weight.** The publisher portal uses essentially three shadows: the modal scrim, the modal container drop, and the hover ring. Fantasy mode adds the hard 2px engraving shadow.
5. **Audit casing.** Title case dominates. No ALL-CAPS hero treatments on either register.
6. **Audit color sprawl.** Publisher portal: red + grays + whites only. Fantasy mode: cobalt + gold + cyan + white only. Mixing chromatic accents across registers breaks both voices.
7. **Audit register clarity.** If building publisher chrome, stay restrained. If building fantasy chrome, lean into Cinzel + cobalt + gold + drop shadows. The two aesthetics are separate Square Enix registers — pick one per composition.
8. **When in doubt, ask: "publisher portal or in-game window?"** — and commit to the chosen register fully. The voice is in the consistency.
