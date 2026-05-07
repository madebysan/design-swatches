---
version: alpha
name: The Verge
description: Editorial dark-canvas tabloid — Manuka 900 at 107px, acid-mint and ultraviolet hazard accents, color-block story tiles, pill cards, mono uppercase labels, color-as-elevation.

colors:
  # Canvas + dark surfaces
  background: "#131313"
  surface: "#2d2d2d"
  surface-frame: "#313131"
  ink: "#ffffff"
  ink-inverted: "#131313"
  ink-absolute: "#000000"

  # Brand hazards
  primary: "#3cffd0"
  primary-border: "#309875"
  secondary: "#5200ff"
  secondary-border: "#3d00bf"

  # Link / focus
  link-hover: "#3860be"
  focus-ring: "#1eaedb"

  # Text hierarchy on dark
  on-background: "#ffffff"
  on-primary: "#000000"
  on-secondary: "#ffffff"
  on-surface: "#e9e9e9"
  text-secondary: "#949494"
  text-pressed: "#8c8c8c"

  # Borders
  border: "#ffffff"
  border-subtle: "#313131"

  # Subtle ring (opaque approximation)
  shadow-ring: "#0d0d0d"  # was rgba(0,0,0,.33) — flattened over canvas

typography:
  display-hero:
    fontFamily: "Manuka, Impact, Helvetica, sans-serif"
    fontSize: 107px
    fontWeight: 900
    lineHeight: 0.80
    letterSpacing: 1.07px
  display-secondary:
    fontFamily: "Manuka, Impact, Helvetica, sans-serif"
    fontSize: 90px
    fontWeight: 900
    lineHeight: 0.80
    letterSpacing: 0px
  display-tertiary:
    fontFamily: "Manuka, Impact, Helvetica, sans-serif"
    fontSize: 60px
    fontWeight: 900
    lineHeight: 0.80
    letterSpacing: 0px
  headline-large:
    fontFamily: "PolySans, Helvetica, Arial, sans-serif"
    fontSize: 34px
    fontWeight: 700
    lineHeight: 1.00
    letterSpacing: 0px
  heading-wide:
    fontFamily: "PolySans, Helvetica, Arial, sans-serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.10
    letterSpacing: 0.32px
  heading-medium:
    fontFamily: "PolySans, Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.00
    letterSpacing: 0px
  heading-small:
    fontFamily: "PolySans, Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.00
    letterSpacing: 0px
  light-cap-label:
    fontFamily: "PolySans, Helvetica, Arial, sans-serif"
    fontSize: 19px
    fontWeight: 300
    lineHeight: 1.20
    letterSpacing: 1.9px
  allcaps-label-xl:
    fontFamily: "PolySans, Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.10
    letterSpacing: 1.8px
  body-bold:
    fontFamily: "PolySans, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.00
    letterSpacing: 0px
  body:
    fontFamily: "PolySans, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.60
    letterSpacing: 0px
  inline-label:
    fontFamily: "PolySans, Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.20
    letterSpacing: 0.15px
  body-compact:
    fontFamily: "PolySans, Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.60
    letterSpacing: 0px
  eyebrow-cap:
    fontFamily: "PolySans, Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.30
    letterSpacing: 1.8px
  tag-label:
    fontFamily: "PolySans, Helvetica, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.20
    letterSpacing: 0.72px
  caption-micro:
    fontFamily: "PolySans, Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.20
    letterSpacing: 1.1px
  meta-nano:
    fontFamily: "PolySans, Helvetica, Arial, sans-serif"
    fontSize: 10px
    fontWeight: 500
    lineHeight: 1.40
    letterSpacing: 1.5px
  mono-button:
    fontFamily: "PolySans Mono, Courier New, Courier, monospace"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 2.00
    letterSpacing: 1.5px
  mono-timestamp:
    fontFamily: "PolySans Mono, Courier New, Courier, monospace"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.20
    letterSpacing: 1.1px
  serif-body:
    fontFamily: "FK Roman Standard, Georgia, serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.30
    letterSpacing: -0.16px
  serif-caption:
    fontFamily: "FK Roman Standard, Georgia, serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.20
    letterSpacing: 0px

spacing:
  micro: 2px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
  2xl: 32px
  3xl: 48px
  4xl: 64px

rounded:
  none: 0px
  xs: 2px
  sm: 3px
  md: 4px
  lg: 20px
  xl: 24px
  2xl: 30px
  3xl: 40px
  pill: 9999px

components:
  # Primary jelly-mint pill
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.mono-button}"
    rounded: "{rounded.xl}"
    padding: 10px 24px
  button-primary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
  button-primary-focus:
    backgroundColor: "{colors.focus-ring}"
    textColor: "{colors.ink}"

  # Secondary slate pill
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface}"
    typography: "{typography.body-bold}"
    rounded: "{rounded.xl}"
    padding: 10px 24px
  button-secondary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.ink-inverted}"

  # Tertiary outlined mint
  button-outlined-mint:
    backgroundColor: "{colors.background}"
    textColor: "{colors.primary}"
    typography: "{typography.mono-button}"
    rounded: "{rounded.3xl}"
    padding: 10px 20px
    borderColor: "{colors.primary}"
  button-outlined-mint-hover:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"

  # Outlined ultraviolet promo
  button-outlined-uv:
    backgroundColor: "{colors.background}"
    textColor: "{colors.secondary}"
    typography: "{typography.mono-button}"
    rounded: "{rounded.2xl}"
    padding: 10px 20px
    borderColor: "{colors.secondary}"

  # Pill tag (non-interactive)
  tag-pill:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.caption-micro}"
    rounded: "{rounded.lg}"
    padding: 4px 10px

  # StoryStream tile (default dark with hairline)
  story-tile:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.heading-medium}"
    rounded: "{rounded.lg}"
    padding: 24px
    borderColor: "{colors.border}"

  # Story tile — mint accent
  story-tile-mint:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.heading-medium}"
    rounded: "{rounded.lg}"
    padding: 24px

  # Story tile — ultraviolet accent
  story-tile-uv:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-secondary}"
    typography: "{typography.heading-medium}"
    rounded: "{rounded.lg}"
    padding: 24px

  # Feature card (top story)
  feature-card:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.headline-large}"
    rounded: "{rounded.xl}"
    padding: 32px
    borderColor: "{colors.border}"

  # Input
  input:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.inline-label}"
    rounded: "{rounded.xs}"
    padding: 8px 12px
    borderColor: "{colors.border}"
  input-focus:
    backgroundColor: "{colors.background}"
    borderColor: "{colors.primary}"
  input-error:
    borderColor: "{colors.secondary}"

  # Inline image frame
  image-frame:
    backgroundColor: "{colors.background}"
    rounded: "{rounded.sm}"
    padding: 0px
    borderColor: "{colors.surface-frame}"

  # Top nav
  nav-bar:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.mono-button}"
    padding: 16px 24px
  nav-link-hover:
    textColor: "{colors.link-hover}"

  # Active nav underline (mint inset)
  nav-link-active:
    textColor: "{colors.primary}"
    borderColor: "{colors.primary}"
---

# The Verge Design System

## Overview

The Verge's 2024 redesign feels like somebody wired a Condé Nast magazine to a chiptune soundboard. The canvas is almost-black (`{colors.background}`), the headlines are built from a brutally heavy display face (Manuka) that runs up to 107px, and the whole page is peppered with acid-mint `{colors.primary}` and ultraviolet `{colors.secondary}` that behave less like brand colors and more like hazard tape. Story tiles are not quiet gray cards — they're saturated, full-bleed color blocks (yellow, pink, orange, blue, purple) that feel like pasted-up rave flyers arranged into a timeline. The mood is "developer console meets club night meets tech tabloid": serious enough to cover a congressional hearing, loud enough to review a synthesizer.

What makes this system unmistakable is the **StoryStream** timeline: a vertical feed where every post is a rounded rectangle — often 20–40px radius — filled edge-to-edge with color, framed by a thin border, and marked by a mono-uppercase timestamp on its left rail. Stories don't float on a grid; they stack on a dashed vertical rule like commits in a git log. Above that, a massive **"The Verge" wordmark** dominates the masthead in Manuka at hero scale, letting the reader know before any headline loads that this is editorial territory, not a template.

There is no "light mode" on the homepage — the dark canvas is the product, and the only time the palette inverts is when a single story tile takes a mint or yellow fill. The depth is almost entirely flat: **hairline 1px borders** (`{colors.border}`, `{colors.primary}`, or `{colors.secondary}`) do the work that shadows would do on a Material-flavored site. Every container is either `{colors.background}` with a 1px outline, a fully saturated accent block, or a slate-gray `{colors.surface}` secondary surface.

**Key Characteristics:**
- Near-black editorial canvas (`{colors.background}`) as the default surface — no light mode
- Acid-mint `{colors.primary}` + ultraviolet `{colors.secondary}` as hazard-tape accents
- Massive Manuka display headlines up to 107px — the loudest type move in mainstream tech media
- Rounded pill-card everything: 20/24/30/40px corner radii, never square
- Fully saturated color-block story tiles (mint, purple, yellow, pink, orange, electric blue) on dark
- Timeline "StoryStream" feed with mono uppercase timestamps rather than a magazine grid
- Flat depth — 1px borders in white, mint, purple do the work shadows would do elsewhere

## Colors

### Primary (Brand Hazards)
- **Jelly Mint** (`{colors.primary}`): The Verge's signature acid-mint. Used as CTA fill, link underlines, active tab borders, and high-attention story-tile backgrounds.
- **Verge Ultraviolet** (`{colors.secondary}`): The complementary hazard. Used for secondary color-block tiles, promotional spans, and outlined buttons.

### Secondary & Accent
- **Console Mint Border** (`{colors.primary-border}`): Darker mint variant for card outlines and borders.
- **Deep Link Blue** (`{colors.link-hover}`): The link hover color across every link style.
- **Focus Cyan** (`{colors.focus-ring}`): Reserved for keyboard focus.
- **Purple Rule** (`{colors.secondary-border}`): The vertical border on StoryStream items.

### Surface & Background
- **Canvas Black** (`{colors.background}`): The default surface — almost-but-not-pure black, warmth of newsprint negative.
- **Surface Slate** (`{colors.surface}`): Secondary card background.
- **Image Frame** (`{colors.surface-frame}`): The 1px border that wraps inline imagery.
- **Hazard White** (`{colors.ink}`): Used as story-tile fill, button border, and primary text.
- **Absolute Black** (`{colors.ink-absolute}`): Reserved for text on mint/yellow/white tiles.

### Neutrals & Text
- **Primary Text** (`{colors.ink}`): Headlines and display on canvas.
- **Secondary Text** (`{colors.text-secondary}`): Bylines, timestamps, photo credits.
- **Muted Text** (`{colors.on-surface}`): Button text on dark slate buttons.
- **Inverted Text** (`{colors.ink-inverted}`): Used only on accent tiles for contrast.

The Verge uses zero decorative gradients. Color is applied in solid blocks; the hazard-tape identity would dissolve if anything faded.

## Typography

### Font Family
- **Manuka** (Klim Type Foundry) — the signature display face. Heavy 900, condensed athletic stance. Runs at 60–107px, never smaller.
- **PolySans** — UI and secondary headline workhorse, weights 300/500/700.
- **PolySans Mono** — used exclusively for ALL-CAPS labels, timestamps, tags, button text. Lowercase mono doesn't exist here.
- **FK Roman Standard** — sparingly for serif body/captions. Print-magazine counterpoint.

### Hierarchy

The complete type scale lives in the `typography:` token block above. Reference tokens directly (`{typography.display-hero}`, `{typography.body}`, etc.).

| Token | Use |
|---|---|
| `display-hero` | The 107px "The Verge" wordmark and feature headlines |
| `display-secondary` | Section-level feature headlines |
| `display-tertiary` | Inline feature callouts |
| `headline-large` | Section and module headlines |
| `heading-wide` | Sub-heroes, promotional units |
| `heading-medium` | Story tile headlines in main feed |
| `heading-small` | Compact tile headlines |
| `light-cap-label` | Thin-weight 300 capitalized eyebrows — the Verge whisper |
| `allcaps-label-xl` | UPPERCASE section kickers |
| `body-bold` | Emphasis within decks |
| `body` | Long-form reading body |
| `inline-label` | UI labels and secondary headlines |
| `body-compact` | Secondary captions and decks |
| `eyebrow-cap` | UPPERCASE kicker above tile headlines |
| `tag-label` | UPPERCASE category tags |
| `caption-micro` | UPPERCASE bylines |
| `meta-nano` | UPPERCASE timestamp microtext |
| `mono-button` | UPPERCASE button text |
| `mono-timestamp` | UPPERCASE StoryStream timestamps |
| `serif-body` | Review decks, print-voice excerpts |
| `serif-caption` | Magazine-style pull quotes |

### Principles
- **Manuka is always the hero, never the UI.** If you see Manuka below 60px you're looking at a bug.
- **PolySans is the workhorse, PolySans Mono is its uniformed sibling.** Mono is exclusively UPPERCASE for labels, timestamps, tags, buttons.
- **Thin-weight (300) capitalized headlines** at 19–20px with 1.9px tracking — a "fashion magazine whisper" against the 107px Manuka shout.
- **Letter-spacing has two registers**: positive (0.72–1.9px) for ALL-CAPS, negative (-0.16px) for serif, barely-positive for massive display.
- **FK Roman Standard is the editorial exception**, not the rule. Reserve for long-form print-voice. Never UI.
- **Line heights are tight** (0.80–1.30) for display and labels, relaxed (1.60–2.00) only for body and mono buttons.

### Note on Font Substitutes
The 0.80 line-height on Manuka assumes the proprietary Klim face. If substituting Anton/Oswald/Bebas Neue/Archivo Black, loosen display line-heights by +0.10 to +0.15. PolySans substitutes (Space Grotesk, DM Sans) work at token values. PolySans Mono substitutes (Space Mono, JetBrains Mono) and FK Roman substitutes (Newsreader, Literata) work without adjustment.

## Layout

### Spacing System
The complete spacing scale lives in the `spacing:` token block above. Base unit is 8px. Section padding runs 32–64px between major feed sections; StoryStream items are tighter at 12–16px gaps. Card padding: 20–32px interior; feature cards 40–48px.

### Grid & Container
- Max width: ~1280–1300px
- Underlying 12-column grid resolving into 3-column hero + 1-column StoryStream rail + feature panels
- Container padding: 24px mobile / 48px desktop
- Gutters: 16–24px between columns, 8–12px inside StoryStream items

### Whitespace Philosophy
The Verge treats whitespace like a club DJ treats silence — as a dramatic reset between loud moments. Even 32px of empty `{colors.background}` between two saturated tiles acts as a palette cleanser. The page is paced, not airy.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| 0 | No border, no shadow | Default `{colors.background}` canvas text |
| 1 | Reset (placeholder) | Reset state for interactive elements |
| 2 | `1px solid {colors.border}` or `{colors.surface-frame}` | Image frames and quiet card outlines |
| 3 | `1px solid {colors.primary}` hairline | Active button outlines, focused story tiles |
| 4 | `1px solid {colors.secondary}` hairline | Promotional/alternate state outlines |
| 5 | `{colors.shadow-ring}` 1px ring | Subtle "atmospheric" ring for layered cards |
| 6 | `0 -1px 0 inset` (mint/black/white) | Active tab underline — a signature Verge move |
| 7 | Saturated accent fill (`{colors.primary}`, `{colors.secondary}`, white, yellow, pink) | Story-tile elevation via color, not shadow |

The Verge's depth philosophy is **color-as-elevation**. When something needs to stand out, it doesn't get a shadow — it gets a mint fill or a 1px hazard-color border.

## Shapes

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Reserved |
| `xs` | 2px | Inputs, small badges (typewriter tag feel) |
| `sm` | 3px | Inline images |
| `md` | 4px | Nested card images and small button variants |
| `lg` | 20px | Standard pill cards and color-block tiles |
| `xl` | 24px | Feature tile radius and primary button pill |
| `2xl` | 30px | Large promotional buttons |
| `3xl` | 40px | Outlined CTA pills — the loudest pill in the system |
| `pill` | 9999px | Avatar circles, icon buttons, round badges |

Eight discrete radius values is a lot for a single site — it's deliberate. Every component announces its hierarchy through its corners.

## Components

The full component spec lives in the `components:` token block above. Reference tokens directly (`{components.button-primary}`, `{components.story-tile}`).

### Buttons
- **`button-primary`** — Jelly Mint pill, black mono uppercase text, 24px radius. Hover inverts to translucent white over canvas.
- **`button-secondary`** — Surface slate pill, muted text. Same hover treatment.
- **`button-outlined-mint`** — Transparent with mint border, 40px radius. Hover inverts to mint fill with black text.
- **`button-outlined-uv`** — Transparent with ultraviolet border, 30px radius. Subscribe / promotional callouts.

### Pill Tags
- **`tag-pill`** — Saturated accent fill, mono uppercase 11px with 1.8px tracking, 20px radius.

### Cards & Containers
- **`story-tile`** — Default dark canvas with white hairline, 20px radius. Hover only shifts headline color to deep link blue.
- **`story-tile-mint`** / **`story-tile-uv`** — Saturated accent fills.
- **`feature-card`** — Top story version, 24px radius, 32px+ padding.

### StoryStream Rail (Timeline)
- Vertical dashed/solid rule (1px `{colors.secondary-border}` or white) along left edge
- Timestamps in PolySans Mono UPPERCASE 1.1px tracking
- Each entry pill-cornered, 12–16px vertical gap

### Inputs
- **`input`** — Dark canvas, white or muted hairline, 2px tight radius. Focus shifts border to `{colors.primary}`. Error uses `{colors.secondary}`.

### Image Treatment
- 16:9 hero / feature; 4:3 mid-feed; 1:1 thumbnails and avatars
- Corners always rounded to match parent — 3px, 4px, or inherit 20/24px
- 1px `{colors.surface-frame}` or `{colors.border}` hairline frame
- Static on hover — only headline below shifts color

### Navigation
- **`nav-bar`** — Thin canvas bar with Manuka wordmark left, mono uppercase category links, mint pill CTA right
- **Hover**: every link transitions to `{colors.link-hover}` deep link blue
- **Active**: 1px mint inset underline

## Do's and Don'ts

### Do
- Use `{colors.background}` as the canvas for every view — there is no light mode
- Use Jelly Mint and Verge Ultraviolet as hazard accents — buttons, borders, active states, saturated tile fills
- Use Manuka exclusively at 60px+ — anything smaller is a bug
- Round everything: 20px cards, 24px feature cards, 30–40px pill buttons
- Use PolySans Mono for UPPERCASE labels, timestamps, kickers, button text
- Apply 1.5–1.9px letter-spacing to every ALL-CAPS label
- Use saturated color-block tiles to elevate a story — never a drop shadow
- Use `{colors.link-hover}` as the hover color on every link
- Apply the StoryStream timeline rail on feed views
- Use thin-weight (300) PolySans 19–20px with 1.9px tracking for "fashion-whisper" eyebrows

### Don't
- Don't use a light background — the dark canvas is the product
- Don't add `box-shadow` for elevation — use 1px borders or saturated accent fills
- Don't use square corners — every interactive container is rounded
- Don't use Manuka for UI, buttons, or body — strictly display
- Don't use lowercase mono — PolySans Mono is always UPPERCASE
- Don't let mint/ultraviolet appear as background washes — they're hazard accents
- Don't use gradients anywhere — solid color blocks only
- Don't introduce new accent colors outside the declared tile palette
- Don't pair Manuka with FK Roman in the same headline cluster
- Don't use `{colors.primary}` text on `{colors.background}` under 16px — contrast vibrates

---

## Responsive Behavior

### Breakpoints

| Name | Width | Key Changes |
|---|---|---|
| Small Mobile | <400px | Single column, Manuka hero scales to ~48–54px, StoryStream rail collapses |
| Mobile | 400–549px | Single column, color-block tiles stack full-width, hamburger nav |
| Large Mobile | 550–767px | Single column, padding opens, tile radii at 20px |
| Tablet | 768–1023px | 2-column StoryStream with feature card spanning, wordmark shrinks |
| Small Desktop | 1024–1179px | Full 3–4 column editorial grid, mint pill CTA in nav |
| Desktop | 1180–1299px | Max padding, Manuka wordmark at full hero scale |
| Large Desktop | ≥1300px | Container caps ~1280–1300px, whitespace expands at margins |

The Verge tunes its grid at virtually every major device boundary — an unusually aggressive responsive strategy.

### Touch Targets
- Primary pill buttons: ~44px minimum height (meets WCAG AA)
- Mono uppercase nav links: smaller (~28–32px tall) — pad to 44px on mobile in derivative work
- Circle icon buttons: 40–44px circles

### Collapsing Strategy
- **Nav**: wordmark scales from hero to ~24–32px; category links collapse to hamburger below 900px
- **Grid**: 4-col → 3-col → 2-col → 1-col
- **Spacing**: section padding tightens 64px → 32px → 20px; tile padding 32px → 20px
- **Type**: Manuka 107px → ~48–54px on mobile; PolySans 34px → 24px; mono labels stay pinned at 11–12px
- **Color tiles**: never lose saturation — they reflow to full width

### Image Behavior
- Responsive raster via `srcset`, aspect ratios preserved
- No art-direction swaps — same crop scales across all viewports
- `loading="lazy"` below fold, `eager` on masthead hero
- Images inside color-block tiles inherit the tile's inner radius

---

## Agent Prompt Guide

### Quick Color Reference
- **Primary CTA**: Jelly Mint `{colors.primary}`
- **Background (Canvas)**: Canvas Black `{colors.background}`
- **Accent (Secondary Hazard)**: Verge Ultraviolet `{colors.secondary}`
- **Heading Text**: Hazard White `{colors.ink}`
- **Body Text**: `{colors.ink}` or Muted `{colors.on-surface}`
- **Secondary Text / Metadata**: `{colors.text-secondary}`
- **Card Border**: `{colors.border}` hairline on dark, `{colors.primary-border}` on mint variants
- **Link Hover**: Deep Link Blue `{colors.link-hover}`

### Example Component Prompts
1. *"Create a StoryStream timeline item on a `{colors.background}` canvas: a 20px-radius rectangle with a 1px solid `{colors.border}` border, a PolySans Mono 11px / 600 / UPPERCASE / 1.1px tracking timestamp on the left rail, a 12px PolySans UPPERCASE kicker in mint (`{colors.primary}`), and a 24px / 700 PolySans headline in white below. No shadow — hover only shifts headline color to `{colors.link-hover}`."*
2. *"Design a primary subscribe button with a Jelly Mint (`{colors.primary}`) fill, black text in PolySans Mono 12px / 600 / UPPERCASE / 1.5px tracking, 24px border radius, 10px × 24px padding."*
3. *"Build a feature hero with a 107px Manuka 900 headline in white with 1.07px letter-spacing and 0.80 line-height, a thin-weight 300 PolySans 20px capitalized kicker above with 1.9px tracking, on a `{colors.background}` canvas with 64px vertical padding."*
4. *"Create a color-block accent tile filled with Verge Ultraviolet (`{colors.secondary}`), 24px border radius, white text, a PolySans Mono 11px UPPERCASE category label with 1.5px tracking at top, and a 32px PolySans 400 capitalized headline with 0.32px tracking below."*
5. *"Design a dark slate secondary button with a `{colors.surface}` background, `{colors.on-surface}` PolySans 16px text, 24px radius pill shape, 10px × 24px padding."*

### Iteration Guide
1. **Audit the canvas.** If you see a light background anywhere, flatten to `{colors.background}`.
2. **Audit corners.** Every rectangle should land on 2/3/4/20/24/30/40px or 50%.
3. **Audit shadows.** Strip every `box-shadow` that isn't a 1px inset underline or 1px hazard-color border.
4. **Audit type roles.** Manuka only ≥60px. PolySans Mono only UPPERCASE. PolySans 300 at 19–20px should have 1.9px tracking. FK Roman only for body/magazine moments.
5. **Audit accent usage.** Mint and ultraviolet should appear as hazard accents — buttons, 1px borders, active underlines, saturated tile fills.
6. **Audit labels.** Every kicker, timestamp, category tag, button label should be ALL CAPS with 1.1–1.9px letter-spacing.
7. **Audit link hover.** Every link should hover to `{colors.link-hover}` with no underline.
