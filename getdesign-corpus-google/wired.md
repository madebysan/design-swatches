---
version: alpha
name: WIRED
description: Newsstand-density editorial system — paper-white canvas, ink-black headlines, hairline rules, custom serif display + technical mono kickers, single ink-blue accent for links. Strictly square corners, no shadows, no cards.

colors:
  # Editorial ink
  primary: "#057dbc"        # the only accent — link blue
  ink-pure: "#000000"       # ribbons, button borders, headline rules
  ink-page: "#1a1a1a"       # headlines, body type — softened black
  background: "#ffffff"     # newsprint canvas
  surface: "#ffffff"

  # Inverted footer
  footer-ink: "#1a1a1a"

  # Neutrals
  on-background: "#1a1a1a"
  on-surface: "#1a1a1a"
  on-primary: "#ffffff"
  caption: "#757575"        # bylines, timestamps, photo credits
  disabled: "#999999"
  hairline: "#e2e8f0"       # quiet section divider
  hairline-strong: "#000000"
  rule-secondary: "#4a5568"

  # Borders
  border-pure: "#000000"
  border-soft: "#757575"
  border-disabled: "#a0aec0"

  # Semantic (rare)
  error: "#e53e3e"

typography:
  display-hero:
    fontFamily: "WiredDisplay, helvetica, serif"
    fontSize: 64px
    fontWeight: 400
    lineHeight: 0.93
    letterSpacing: -0.5px
  display-mid:
    fontFamily: "WiredDisplay, helvetica, serif"
    fontSize: 26px
    fontWeight: 400
    lineHeight: 1.08
    letterSpacing: 0px
  section-heading:
    fontFamily: "Apercu, helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.28px
  sub-heading:
    fontFamily: "Apercu, helvetica, sans-serif"
    fontSize: 17px
    fontWeight: 700
    lineHeight: 1.29
    letterSpacing: -0.144px
  article-deck:
    fontFamily: "BreveText, helvetica, serif"
    fontSize: 19px
    fontWeight: 400
    lineHeight: 1.47
    letterSpacing: 0.108px
  article-body:
    fontFamily: "BreveText, helvetica, serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0.09px
  ui-heading:
    fontFamily: "Apercu, helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.3px
  button-ui:
    fontFamily: "Apercu, helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0.3px
  link-ui:
    fontFamily: "Apercu, helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.29
    letterSpacing: 0.4px
  eyebrow:
    fontFamily: "WiredMono, Monaco, Courier New, monospace"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.23
    letterSpacing: 0.92px
  eyebrow-bold:
    fontFamily: "WiredMono, Monaco, Courier New, monospace"
    fontSize: 13px
    fontWeight: 700
    lineHeight: 1.23
    letterSpacing: 0px
  ribbon:
    fontFamily: "WiredMono, Monaco, Courier New, monospace"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: 1.2px
  photo-caption:
    fontFamily: "BreveText, helvetica, serif"
    fontSize: 12.73px
    fontWeight: 700
    lineHeight: 2.2
    letterSpacing: 0.108px
  timestamp:
    fontFamily: "WiredMono, Monaco, Courier New, monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 1.1px
  footer-link:
    fontFamily: "ProximaNova, helvetica, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: 0px

spacing:
  hairline: 1px
  xs: 4px
  sm: 8px
  md: 12px
  micro-fract: 14.11px
  lg: 15px
  xl: 16px
  2xl: 24px
  fract-25: 25.46px
  fract-30: 29.66px
  3xl: 32px
  4xl: 40px
  5xl: 48px
  6xl: 64px

rounded:
  none: 0px
  pill-text: 1920px
  circle: 9999px

components:
  # Buttons
  button-primary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink-pure}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.none}"
    padding: 12px 24px
  button-primary-hover:
    backgroundColor: "{colors.ink-pure}"
    textColor: "{colors.surface}"

  button-inverted:
    backgroundColor: "{colors.ink-pure}"
    textColor: "{colors.surface}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.none}"
    padding: 12px 24px

  button-tertiary-link:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink-page}"
    typography: "{typography.link-ui}"
    padding: 0px

  button-icon:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink-page}"
    rounded: "{rounded.circle}"
    padding: 8px

  pill-text:
    backgroundColor: "{colors.ink-pure}"
    textColor: "{colors.surface}"
    typography: "{typography.timestamp}"
    rounded: "{rounded.pill-text}"
    padding: 2px 8px

  # Inputs
  input:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink-page}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.none}"
    padding: 12px 16px
  input-disabled:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.border-disabled}"

  # Section ribbons
  ribbon-section:
    backgroundColor: "{colors.ink-pure}"
    textColor: "{colors.surface}"
    typography: "{typography.ribbon}"
    rounded: "{rounded.none}"
    padding: 8px 16px

  # Story tile (no card chrome)
  story-tile:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink-page}"
    rounded: "{rounded.none}"
    padding: 0px

  # Navigation
  nav-utility:
    backgroundColor: "{colors.ink-pure}"
    textColor: "{colors.surface}"
    typography: "{typography.timestamp}"
    padding: 8px 16px
  nav-main:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink-page}"
    typography: "{typography.link-ui}"
    padding: 12px 16px
  nav-link-hover:
    textColor: "{colors.primary}"

  # Footer
  footer:
    backgroundColor: "{colors.footer-ink}"
    textColor: "{colors.surface}"
    typography: "{typography.footer-link}"
    padding: 48px 24px
---

# WIRED Design System

## Overview

WIRED's homepage feels like a printed broadsheet that someone has plugged into a wall socket. The grid is dense, the rules are thin, the type is loud, and almost every surface is paper-white or pure black with no rounded corners and no decoration that doesn't earn its place. Image rectangles butt directly against headlines, hairline dividers separate stories the way pica rules separate columns in a real magazine, and the only colors that aren't grayscale come from the photography itself. There is no "card with shadow" anywhere — the entire layout is held together by typographic weight and the discipline of rules and whitespace, the same way a Condé Nast print page would be assembled in a paste-up room.

The signature move is the **typographic stack**: a brutally large custom serif (WiredDisplay) for the main headline, a humanist serif (BreveText) for body and decks, a geometric sans (Apercu) for UI affordances, and a hard mono uppercase (WiredMono) for the kickers, eyebrows, and timestamps that mark every story. That mono kicker — usually black caps with letter-spacing wide enough to read as a Geiger-counter tick — is what makes a WIRED page instantly recognizable from across the room.

There is exactly one accent color that matters: a saturated link blue (`{colors.primary}`) that lights up underlined hover states like a CRT scanline. Everything else is black, paper white, and two grays — the design's confidence comes from refusing to invent more.

**Key Characteristics:**
- Newsstand-density editorial grid: rules and whitespace, never cards or shadows
- Custom serif display + technical mono kickers — the Condé-Nast-meets-engineering-lab voice
- Strictly square corners on every image, container, and ribbon (only icon buttons are circular)
- 2px hard black borders on buttons and links — printerly, not webby
- Mono ALL-CAPS eyebrows on every story with wide tracking (0.9–1.2px)
- Single ink-blue accent for links; everything else lives in pure grayscale
- Dark theme = the *footer*, not the page; the page itself is committed paper-white

## Colors

### Primary (Editorial Ink)
- **WIRED Black** (`{colors.ink-pure}`): Pure ink for ribbons, section dividers, button borders, headline rules — the strongest hand on the page.
- **Page Ink** (`{colors.ink-page}`): Near-black used for headlines and body type. Slightly softened so long-form reading doesn't feel like staring at a power button.
- **Paper White** (`{colors.background}`): Default canvas for the entire site. Treat it like newsprint stock — uninterrupted, never tinted.

### Secondary (Editorial Voice)
- **Link Blue** (`{colors.primary}`): The single brand accent. Used for inline link hovers, breadcrumbs, and the rare button — never for backgrounds, never decorated. Think of it as the only color allowed in a black-and-white film.

### Surface & Background
- **Newsprint** (`{colors.background}`): Editorial pages, story grids, hero zones.
- **Footer Ink** (`{colors.footer-ink}`): The only inverted region on the homepage.
- **Hairline Tint** (`{colors.hairline}`): Reserved for `<hr>` elements between sections — barely visible, like a margin rule.

### Neutrals & Text
- **Headline Black** (`{colors.ink-page}`): All H1/H2 display type.
- **Body Gray** (`{colors.ink-page}`): Long-form body — same ink as headlines for unity.
- **Caption Gray** (`{colors.caption}`): Secondary metadata: bylines, timestamps, photo credits.
- **Disabled Gray** (`{colors.disabled}`): Inactive links, low-priority labels.
- **Hairline Border** (`{colors.hairline}`): Subtle separators only.
- **Secondary Rule** (`{colors.rule-secondary}`): Page-fold-style column rules.

### Semantic & Accent
- **Brand Hover Blue** (`{colors.primary}`): Link rollover — also serves as the only "interactive" cue.
- **Error** (`{colors.error}`): Form error label color (used very sparingly).
- *(WIRED's homepage intentionally omits semantic success/warning palettes — this is editorial, not a SaaS dashboard.)*

**No gradients.** WIRED uses zero gradients. The closest thing to a gradient on the page is the tonal range inside a photograph — gradients live *in the imagery*, not in the chrome.

## Typography

### Font Family
- **WiredDisplay** (custom serif, fallback `helvetica`) — display headlines and feature titles
- **BreveText** (humanist serif, fallback `helvetica`) — article body, decks, longer captions
- **Apercu** (geometric sans, fallback `helvetica`) — UI labels, buttons, navigation, mid-weight headings
- **WiredMono** (custom monospace, fallback `Monaco, Courier New, Courier`) — eyebrows, kickers, timestamps, ALL CAPS
- **Inter** (sans, system fallback) — utility UI in newer modules
- **ProximaNova** (sans, fallback `helvetica`) — legacy UI surfaces

### Hierarchy

The complete type scale lives in the `typography:` token block above. Reference tokens directly.

| Token | Use |
|---|---|
| `display-hero` | 64px hero headline (WiredDisplay) |
| `display-mid` | 26px grid-block headline |
| `section-heading` | 20px Apercu module title |
| `sub-heading` | 17px Apercu story deck |
| `article-deck` | 19px BreveText lead paragraph |
| `article-body` | 16px BreveText body |
| `ui-heading` | 16px Apercu UI label |
| `button-ui` | 16px Apercu button label |
| `link-ui` | 14px Apercu inline link |
| `eyebrow` | 13px WiredMono uppercase kicker |
| `eyebrow-bold` | 13px WiredMono bold kicker |
| `ribbon` | 12px WiredMono ribbon section label |
| `photo-caption` | 12.73px BreveText photo caption |
| `timestamp` | 12px WiredMono timestamp |
| `footer-link` | 11px ProximaNova footer link |

### Principles
- **Four faces, four jobs.** WiredDisplay is for shouting, BreveText is for reading, Apercu is for clicking, WiredMono is for labeling. They never trade roles.
- **Tight headlines, generous body.** Display type runs as low as 0.93 line-height, while body BreveText opens out to 1.47–1.50.
- **Mono is always uppercase.** Every WiredMono usage carries `text-transform: uppercase` and 0.9–1.2px letter-spacing. Treat lowercase mono as broken.
- **Bold is rare.** Apercu uses weight 700 only for UI emphasis; the editorial layer leans entirely on size and ink color, never on bolding.
- **Letter-spacing has two registers**: positive (0.9–1.2px) for ALL-CAPS mono, negative (-0.144 to -0.5px) for large display serif.

### Note on Font Substitutes
The line-height values (especially the 0.93 on the 64px hero) assume the proprietary WiredDisplay and BreveText faces, which have tight metrics with short ascenders/descenders. If you substitute these with wide-metric open-source fonts like Playfair Display or Libre Caslon, loosen display line-heights by approximately +0.10 to +0.12 to prevent ascender/descender collisions. Apercu substitutes (Inter, Work Sans, Manrope) work at the token values without adjustment. BreveText body substitutes (Lora, Source Serif 4) also work without adjustment.

## Layout

### Spacing System
The complete spacing scale lives in the `spacing:` token block above. Base unit is 8px with frequent fractional values for editorial column tuning.

Section padding: `3xl`–`5xl` (32–48px) vertical between major editorial blocks. Card padding: there are no cards; story tile gutters are `2xl`–`3xl` horizontally and `xl`–`2xl` vertically. Inline spacing: kickers ~`xs`–`sm` above headlines; decks ~`sm`–`md` below.

### Grid & Container
- Max width: ~1280–1600px on desktop, centered with generous outer margins
- Column patterns: 12-column grid resolving into 2/3/4 column story arrangements depending on module
- Column gutters: `2xl`–`3xl`, separated by hairline `{colors.hairline-strong}` or `{colors.rule-secondary}` 1px rules

### Whitespace Philosophy
WIRED treats whitespace the way a magazine art director treats margin: it's the silence around the type, not a styling choice. The page never breathes excessively (this is not Stripe or Apple); it breathes *editorially* — enough room to keep adjacent stories from arguing, never enough to suggest there's nothing on the page.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| 0 | No shadow, no border | Default editorial surface — text on paper |
| 1 | 1px solid `{colors.hairline}` hairline `<hr>` | Quiet section divider |
| 2 | 1px solid `{colors.ink-pure}` hairline rule | Editorial column divider |
| 3 | 2px solid `{colors.ink-pure}` border | Buttons, inputs, ribbons |
| 4 | Black ribbon bar (`{colors.ink-pure}` fill) | Section labels |
| 5 | Inverted footer block | Dark `{colors.footer-ink}` zone with white type |

WIRED's depth philosophy is **flat by religion**. There is exactly one shadow token in the entire site (a default placeholder) and no `box-shadow` is applied to story tiles, headers, modals, or cards. Depth is communicated by **rule weight** (1px hairline → 2px hard rule → solid black ribbon), not by simulated lighting.

### Decorative Depth
None. No gradients, no glow, no halos. WIRED earns its visual interest from photography and typographic contrast, not from chrome.

## Shapes

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Every container, every image, every button, every input — the default |
| `pill-text` | 1920px | Inline text spans that need to look like a full pill ("BREAKING", "LIVE") |
| `circle` | 50% | Round icon buttons and circular author avatars |

There are exactly three radii on the entire site, and two of them are reserved for non-rectangular shapes. This is the **strictest** corner discipline of any major editorial property.

## Components

The complete component spec lives in the `components:` token block above.

### Buttons
- **`button-primary`** — White background, 2px solid black border, square corners, Apercu 16px / 700 / 0.3px tracking. Hover inverts to `button-primary-hover`.
- **`button-inverted`** — Black on white, 2px solid white border (used in dark zones).
- **`button-tertiary-link`** — Underlined inline link, no padding/border/background — editorial linking, not UI.
- **`button-icon`** — Round icon button (`50%` radius), used exclusively for header icon controls.
- **`pill-text`** — Inline text pill ("BREAKING") with mono caps.

### Cards & Containers
- **Cards do not exist.** A "story tile" is just an image rectangle stacked above a kicker + headline + deck, separated from neighbors by 1px hairline rules or raw whitespace.
- **`story-tile`** — bare layout primitive (no chrome).
- **`ribbon-section`** — full-bleed black bar with white WiredMono caps, no padding refinement, no rounded ends.

### Inputs & Forms
- **`input`** — rectangular, 2px solid black border, square corners, white background, Apercu 16px placeholder.
- Focus: border stays 2px black, no glow ring, no color change — focus is signaled by the blinking caret only. (Add a 2px outset for accessibility if you ship this.)
- Error: text label below in `{colors.error}`. Disabled drops to `{colors.border-disabled}`.

### Navigation
- **`nav-utility`** — black full-bleed strip, mono caps links, white text, hover → blue.
- **`nav-main`** — paper-white row beneath the bug logo, Apercu 14–16px regular, hover → blue underline.
- Logo: WIRED bug, ~209×42px, never recolored.
- Mobile: nav collapses to a hamburger left of the bug logo.

### Image Treatment
- Aspect ratios: 16:9 hero, 4:3 grid story tiles, 1:1 thumbnails.
- Corners: ALWAYS 0 radius. The only rounded image is a circular author avatar.
- Full-bleed: hero photographs run edge-to-edge of the column they occupy.
- Captions: BreveText 12.73px / 700 with relaxed 2.20 line-height.
- Hover: no zoom, no opacity dip — only the headline below responds.

### Editorial Ribbons & Section Markers
Black bar full-bleed with white WiredMono uppercase label inside (e.g., "MOST POPULAR", "BACKCHANNEL", "GEAR"). Height ~32–40px, no padding refinement, no rounded ends.

### Numbered Lists ("Most Popular")
A vertical list of stories prefixed with WiredDisplay numerals (01, 02, 03…) at ~40–48px, sitting tight against the headline they label. Hairline rule between each item, no other decoration.

## Do's and Don'ts

### Do
- Use 2px hard black borders on every primary button — no 1px softness, no rounded edges
- Put a WiredMono ALL-CAPS kicker above every story headline (4–8px above, 0.9–1.2px tracking)
- Use BreveText for any paragraph longer than two lines — Apercu is for UI, not reading
- Keep images square-cornered, edge-to-edge, with the caption hugging the bottom edge
- Separate story tiles with hairline rules or whitespace, never with cards or shadows
- Invert (black background, white type) only for footers, ribbons, and the utility nav strip
- Use `{colors.primary}` link blue exclusively for hover states — never as a background or button fill
- Scale headlines aggressively: 64px on hero, 26px on grid blocks, never 32px "safe middle ground"

### Don't
- Don't add `box-shadow` to anything. Ever. WIRED doesn't ship shadows.
- Don't round corners on rectangular containers — `border-radius: 0` is law
- Don't mix typefaces inside one role: WiredDisplay never sets body, BreveText never sets buttons
- Don't use color outside grayscale + `{colors.primary}`. No orange CTAs, no green success pills
- Don't use Apercu in lowercase for kickers — that's WiredMono's job, and it must be UPPERCASE
- Don't use gradients, blurs, glassmorphism, or atmospheric effects
- Don't rely on hover lift effects. WIRED's hover is a color swap on text, nothing more
- Don't invent new pill shapes. Round = icons only. Pill = inline text spans only

---

## Responsive Behavior

### Breakpoints

| Name | Width | Key Changes |
|---|---|---|
| Small Mobile | <375px | Single column, hamburger nav, all hero modules collapse to stacked image-headline-deck |
| Mobile | 375–767px | Single column, story grid becomes vertical scroll, "Most Popular" numbers shrink to 32px |
| Tablet | 768–1023px | 2-column story grid, sidebar collapses below main feed, nav becomes condensed |
| Desktop | 1024–1599px | Full editorial 3–4 column grid, sidebar restored, max headline scale active |
| Large Desktop | ≥1600px | Page caps at ~1600px container, whitespace expands at the margins, no further scaling |

The dembrandt sweep detected an unusual range of intermediate breakpoints (1280, 1025, 1024, 1023, 768, 767, 667, 599, 570, 569, 480, 425, 375, 320, 319) — Wired's grid micro-tunes at almost every common viewport, especially around the iPad portrait/landscape boundary.

### Touch Targets
- Primary button: ~44x44px minimum (16px text + 12–14px vertical padding satisfies WCAG AAA).
- Mono caps links in the utility bar are smaller (~32px tall) — WIRED's own implementation undershoots WCAG here. **For derivative work, pad mono nav links to 44px.**
- Round icon buttons in the header are ~40px circles.

### Collapsing Strategy
- **Nav**: utility bar drops below 768px; main nav collapses into hamburger drawer. Bug logo recenters on mobile.
- **Grid**: 4-col → 3-col → 2-col → 1-col as viewport tightens. Hairline rules persist between every column count.
- **Spacing**: vertical rhythm tightens from 48px → 32px → 24px between modules on mobile. Horizontal page padding shrinks from 64px → 24px → 16px.
- **Type**: WiredDisplay hero scales from 64px to ~36–42px on mobile, headlines from 26px to ~22px, kickers stay locked at 12–13px.

### Image Behavior
- All images are responsive raster (`srcset`-driven), aspect ratios preserved: 16:9 hero, 4:3 mid, 1:1 thumbnails.
- No art-direction swaps — the same crop scales across breakpoints.
- `loading="lazy"` on all below-the-fold imagery, `eager` on the hero only.

---

## Agent Prompt Guide

### Quick Color Reference
- **Primary Ink (text + ribbons)**: "WIRED Black (`{colors.ink-pure}`)"
- **Page Canvas**: "Paper White (`{colors.background}`)"
- **Headline / Body Text**: "Page Ink (`{colors.ink-page}`)"
- **Caption / Metadata**: "Caption Gray (`{colors.caption}`)"
- **Hairline / Quiet Border**: "Hairline Tint (`{colors.hairline}`)"
- **Link Hover Accent (the only color)**: "Link Blue (`{colors.primary}`)"

### Example Component Prompts
1. *"Create an editorial story tile with a 16:9 image (square corners), an UPPERCASE WiredMono kicker in `{colors.ink-page}` above a 26px WiredDisplay headline. Separate the tile from its neighbor with a 1px black hairline rule. No card, no shadow, no border-radius."*
2. *"Design a primary subscribe button with a 2px solid `{colors.ink-pure}` border, square corners, `{colors.surface}` background, Apercu 16px / 700 / 0.3px tracking text in `{colors.ink-pure}`. Hover state inverts to black background with white text in 150ms."*
3. *"Build a 'Most Popular' module: full-bleed black ribbon header with WiredMono uppercase label in white, followed by a numbered list (01–05) using 40px WiredDisplay numerals and 17px Apercu 700 headlines, separated by hairline rules."*
4. *"Create a newsletter signup form with a 2px solid black input border, no radius, Apercu 16px placeholder in `{colors.caption}`, and an inverted black submit button beside it."*
5. *"Design a footer in `{colors.footer-ink}` with paper-white tertiary navigation in ProximaNova 11px, hover color `{colors.primary}`, and a centered WIRED bug logo at the top of the block."*

### Iteration Guide
1. **Audit corners first.** If you see any `border-radius` other than `0`, `50%` (icons/avatars), or `1920px` (text pills), flatten it.
2. **Audit shadows.** Strip every `box-shadow`. If a tile needs to feel "lifted", use a 2px black border or a hairline rule instead.
3. **Audit typeface roles.** Make sure WiredDisplay only sets headlines, BreveText only sets reading body, Apercu only sets UI, WiredMono only sets ALL-CAPS labels.
4. **Audit color sprawl.** If a color outside `{colors.ink-pure}`, `{colors.ink-page}`, `{colors.caption}`, `{colors.hairline}`, `{colors.background}`, `{colors.primary}` appears in chrome (not photography), remove it.
5. **Audit kickers.** Every story should have an UPPERCASE mono kicker.
6. **Audit rules.** Add hairline `1px solid` dividers wherever two stories or modules meet without a clear visual break.
