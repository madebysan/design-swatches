---
version: alpha
name: Mastercard
description: Editorial payments-network aesthetic — warm putty-cream canvas, MarkForMC at weight 450, oversized radii (20/40/999px), circular orbital portraits with satellite CTAs, and Signal Orange reserved for legal consent.

colors:
  # Base
  background: "#f3f0ee"
  surface: "#fcfbfa"
  surface-pure: "#ffffff"
  surface-cool: "#f4f4f4"
  ink: "#141413"
  on-primary: "#f3f0ee"

  # Brand mark colors (logo only, never UI)
  brand-red: "#eb001b"
  brand-yellow: "#f79e1b"

  # Charcoal alt
  charcoal: "#262627"

  # Signal / consent (legal use only)
  primary: "#cf4500"
  signal-light: "#f37338"
  clay-brown: "#9a3a0a"

  # Neutral text
  slate-gray: "#696969"
  granite: "#555555"
  graphite: "#565656"
  dust-taupe: "#d1cdc7"

  # Link
  link-blue: "#3860be"

  # Watermark cream (ghost headlines)
  watermark: "#e8e2da"

  # Borders / shadows (opaque approximations)
  border-soft: "#e8e2da"  # near-watermark for soft borders
  shadow-nav: "#ebe9e7"  # was rgba(0,0,0,0.04) — Google format requires hex
  shadow-card: "#dcd8d4"  # was rgba(0,0,0,0.08) — Google format requires hex
  shadow-deep: "#a8a39e"  # was rgba(0,0,0,0.25) — Google format requires hex

typography:
  h1:
    fontFamily: "MarkForMC, SofiaSans, Arial, sans-serif"
    fontSize: 64px
    fontWeight: 500
    lineHeight: 1.00
    letterSpacing: -1.28px
  h2:
    fontFamily: "MarkForMC, SofiaSans, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 500
    lineHeight: 1.22
    letterSpacing: -0.72px
  h3:
    fontFamily: "MarkForMC, SofiaSans, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.20
    letterSpacing: -0.48px
  h4:
    fontFamily: "MarkForMC, SofiaSans, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.30
    letterSpacing: 0px
  eyebrow:
    fontFamily: "MarkForMC, SofiaSans, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.00
    letterSpacing: 0.56px
  body:
    fontFamily: "MarkForMC, SofiaSans, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 450
    lineHeight: 1.40
    letterSpacing: 0px
  nav-link:
    fontFamily: "MarkForMC, SofiaSans, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.00
    letterSpacing: -0.48px
  button:
    fontFamily: "MarkForMC, SofiaSans, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.00
    letterSpacing: -0.32px
  footer-link:
    fontFamily: "MarkForMC, SofiaSans, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 450
    lineHeight: 1.43
    letterSpacing: 0px
  footer-header:
    fontFamily: "MarkForMC, SofiaSans, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.00
    letterSpacing: 0.56px

spacing:
  xs: 8px
  sm: 16px
  md: 24px
  lg: 32px
  xl: 48px
  2xl: 64px
  3xl: 96px
  4xl: 128px

rounded:
  none: 0px
  micro: 6px
  button: 20px
  consent: 24px
  hero: 40px
  pill: 999px
  circle: 9999px

components:
  # Primary — Ink Pill (the workhorse CTA)
  button-primary:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button}"
    rounded: "{rounded.button}"
    padding: 6px 24px

  # Secondary — Outlined Pill
  button-outlined:
    backgroundColor: "{colors.surface-pure}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.button}"
    padding: 6px 24px

  # Consent — Orange Pill (legal/cookie only)
  button-consent:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.surface-pure}"
    typography: "{typography.button}"
    rounded: "{rounded.consent}"
    padding: 1px 30px

  # Satellite — circular micro-CTA
  button-satellite:
    backgroundColor: "{colors.surface-pure}"
    textColor: "{colors.ink}"
    rounded: "{rounded.circle}"
    size: 56px

  # Icon-only circle button
  button-icon-circle:
    backgroundColor: "{colors.surface-pure}"
    textColor: "{colors.ink}"
    rounded: "{rounded.circle}"
    size: 40px

  # Hero media frame (stadium)
  hero-frame:
    backgroundColor: "{colors.ink}"
    rounded: "{rounded.hero}"
    padding: 0px 0px

  # Service portrait card (circular)
  card-portrait:
    backgroundColor: "{colors.background}"
    rounded: "{rounded.circle}"
    padding: 0px 0px

  # Pill carousel card
  card-pill:
    backgroundColor: "{colors.background}"
    rounded: "{rounded.hero}"
    padding: 0px 0px

  # Chip inside pill carousel
  chip:
    backgroundColor: "{colors.surface-pure}"
    textColor: "{colors.ink}"
    typography: "{typography.eyebrow}"
    rounded: "{rounded.pill}"
    padding: 8px 20px

  # Lifted card (one step up from canvas)
  card-lifted:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.hero}"
    padding: 32px

  # Floating navigation pill
  nav-pill:
    backgroundColor: "{colors.surface-pure}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    rounded: "{rounded.pill}"
    padding: 16px 40px

  # Search input (expanded state)
  input:
    backgroundColor: "{colors.surface-pure}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.pill}"
    padding: 12px 24px

  # Country/language selector (footer)
  selector-footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-pure}"
    typography: "{typography.footer-link}"
    rounded: "{rounded.pill}"
    padding: 8px 16px

  # Footer surface
  footer:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface-pure}"
    typography: "{typography.footer-link}"
    padding: 100px 48px
---

# Mastercard Design System

## Overview

Mastercard's experience reads like a warm, editorial magazine built from soft stone and signal orange. The canvas is a muted putty-cream (`{colors.background}`) — not white, not gray, but a color that feels like the paper of a premium annual report. On top of that canvas, everything that matters is shaped like a stadium, a pill, or a perfect circle. The dominant visual gesture is the **oversized radius**: heroes carry 40-point corners, cards go fully pill-shaped, service images are cropped into circular orbits, and buttons either complete the pill or fit snugly at 20 points. There are almost no sharp corners anywhere on the page.

The second gesture is **orbit and trajectory**. Circular image masks don't sit still — they're connected by thin, hand-drawn-feeling orange arcs that span entire viewport widths, implying a constellation of services rather than a list. Each circle has a small attached "satellite" — a white micro-CTA holding an arrow icon — docked onto its perimeter like a moon. This is the most distinctive thing about Mastercard's current design language: the circles feel like they're in motion even though the page is still.

Typography is rendered entirely in **MarkForMC**, Mastercard's proprietary geometric sans. Headlines are set at a medium weight (500) with tight negative letter-spacing (-2%), giving them confidence without shouting. Body copy runs at the same family in a slightly lighter weight (450) — a weight you rarely see on the web, chosen because it reads softer than regular 400 without feeling thin. The whole system — warm cream surfaces, pill shapes, circular portraits, traced-orange orbits, black CTAs — feels simultaneously institutional (a 60-year-old payments network) and editorial (a modern brand magazine).

**Key Characteristics:**
- Warm cream canvas (`{colors.background}`) replaces traditional white — every surface is tinted, never sterile
- Extreme border-radius as design language: 40px, 99px, 1000px dominate; anything square is a third-party
- Circular image portraits with attached white satellite-CTAs and traced-orange orbital paths
- Ghost "watermark" headlines (cream-on-cream text at heading scale) layered behind circle portraits
- Black primary CTAs with 20px radius in the body — the cookie-banner orange is kept to consent flows
- Floating pill-shaped navigation that docks below the viewport top with rounded shoulders
- Eyebrow labels with a tiny accent dot + uppercase bold tracking — used as the section-category signal
- Dark warm-black footer (`{colors.ink}`) with four-column link layout and large conversational headline

## Colors

### Primary
- **Mastercard Red** (`{colors.brand-red}`): The left circle of the Mastercard mark — used only in the brand logo, never as a UI color.
- **Mastercard Yellow** (`{colors.brand-yellow}`): The right circle of the Mastercard mark — used only in the brand logo, never as a UI color.
- **Ink Black** (`{colors.ink}`): The warm near-black used for primary CTAs, headline text on cream, and the footer surface.

### Secondary & Accent
- **Signal Orange** (`{colors.primary}`): The burnt/rust CTA orange used on consent actions and eyebrow dots. The page's single aggressive color and must be used sparingly.
- **Light Signal Orange** (`{colors.signal-light}`): A lighter carroty orange used for carousel active indicators and decorative orbital arcs.
- **Clay Brown** (`{colors.clay-brown}`): The deep rust used for secondary link-style buttons.

### Surface & Background
- **Canvas Cream** (`{colors.background}`): The page canvas. Warm, putty-toned, the default body background.
- **Lifted Cream** (`{colors.surface}`): One step lighter than canvas — used for nested "raised" sections.
- **White** (`{colors.surface-pure}`): Reserved for the floating navigation pill, modal cards, secondary button fills, and small satellite-CTA circles.
- **Soft Bone** (`{colors.surface-cool}`): A cool-gray alternative surface.

### Neutrals & Text
- **Ink Black** (`{colors.ink}`): Primary headline and body text color.
- **Charcoal** (`{colors.charcoal}`): A slightly softer black used for some text alternates.
- **Slate Gray** (`{colors.slate-gray}`): Muted secondary text.
- **Granite/Graphite** (`{colors.granite}`, `{colors.graphite}`): Deeper gray for inline body accents.
- **Dust Taupe** (`{colors.dust-taupe}`): Very muted cream-gray used for "whisper" text.

### Semantic & Accent
- **Link Blue** (`{colors.link-blue}`): A deep, slightly dusty blue used for inline links.
- **Watermark** (`{colors.watermark}`): The cream-on-cream tone for ghost headlines.

### Gradient System
Mastercard uses no programmatic gradients. The visual impression of "gradient" comes from circular image portraits where a warm-orange photo subject fades to the cream canvas at its edge, and from deep card shadows that create a soft halo beneath pill-shaped media.

## Typography

### Font Family
- **Primary**: `MarkForMC` — Mastercard's proprietary geometric sans
- **Secondary**: `MarkOffcForMC` — used in legal text, some forms
- **Fallback stack**: `SofiaSans, Arial, sans-serif`

### Hierarchy

The complete type scale lives in the `typography:` token block above. Reference tokens (`{typography.h1}`, `{typography.body}`) directly.

| Token | Use |
|---|---|
| `h1` | 64px hero — set at 1:1 line-height for tight vertical rhythm |
| `h2` | 36px section titles, ghost-watermark headlines |
| `h3` | 24px card titles |
| `h4` | 14px subhead (rare) |
| `eyebrow` | 14px uppercase paired with a tiny accent dot |
| `body` | 16px body — the signature 450 weight |
| `nav-link` | 16px nav and button label, tight tracking |
| `button` | 16px CTA label |
| `footer-link` | 14px lighter footer copy |
| `footer-header` | 14px uppercase column header |

### Principles
- **Weight 450 is load-bearing**. Most brands use 400/500/700; Mastercard uses 450 for body copy, creating an unusually soft reading tone.
- **Tight negative tracking on headlines** (-2%) gives display text its editorial density.
- **Uppercase tracking only on the eyebrow scale** (14px / 700 / +4% tracking).
- **One-font system**. No serif accent, no script, no secondary display font.
- **Line-height ratio drops with size**. H1 is 1:1, H3 is 1.2, body is 1.4.

### Note on Font Substitutes
MarkForMC is proprietary. **Sofia Sans** (Google Fonts) is the closest open-source match. **Inter** at weights 450/500/700 works as a generic stand-in. Whichever substitute is used, preserve the **-2% letter-spacing on headlines** and the **450 body weight**.

## Layout

### Spacing System
The complete spacing scale lives in the `spacing:` token block above. Base unit is **8px** (powers of 8: 8 / 16 / 24 / 32 / 48 / 64 / 96 / 128).

### Grid & Container
- **Max content width**: ~1200–1280px centered, with ~48–100px horizontal gutter
- **Column pattern**: 12-column implied; practical layouts use 2-up asymmetric, 1-up full-bleed, or staggered single-portrait placement (the "constellation" feel)
- **Footer grid**: 4 equal columns on desktop, collapses to single column accordion on mobile

### Whitespace Philosophy
Mastercard treats whitespace as structure, not absence. A typical service section has a ghost headline occupying the top ~40% of the section (mostly empty cream), a single circular portrait positioned ~60% down asymmetric to left or right, and ~300–500px of blank canvas between the portrait and the next section. This deliberate emptiness tells the eye "slow down, read one thing at a time."

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| 0 | No shadow | The default — 95% of surfaces sit directly on cream canvas |
| 1 | `0 4px 24px {colors.shadow-nav}` | Floating nav pill — barely-there lift |
| 2 | `0 24px 48px {colors.shadow-card}` | Hero media frames, elevated cards — soft large-radius halo |
| 3 | `0 70px 110px {colors.shadow-deep}` | Rare; dramatic elevation on a feature tile |

### Shadow Philosophy
Mastercard uses shadows as **atmospheric cushioning**, not directional light. The Level 2 shadow has 48px spread and very low opacity — it barely exists as dark pixels but creates a "the card is breathing above the canvas" feel. Border lines are preferred over shadows for functional delineation.

### Decorative Depth
- **Orbital arcs** (Light Signal Orange `{colors.signal-light}`, ~1px): trace connective paths across sections
- **Ghost watermark headlines**: cream-on-cream text gives sections an almost-pressed-paper quality
- **Circle-image fade**: warm-toned photography at the edge of circular portraits dissolves into the canvas

## Shapes

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Tiny decorative elements (rare) |
| `micro` | 6px | Cookie banner micro-chips |
| `button` | 20px | Primary and secondary body CTAs — the signature button radius |
| `consent` | 24px | Consent/orange pill buttons, modal inner chips |
| `hero` | 40px | Hero media frames, large section container corners |
| `pill` | 999px | Full pill shapes — navigation, carousel cards, footer country selector |
| `circle` | 9999px | Circular portraits, icon-only buttons, satellite CTAs |

The scale skips the 8–12 range — Mastercard commits to **either small (≤6), medium-large (20–40), or full-pill (99+)**.

## Components

The complete component spec lives in the `components:` token block above. Reference components directly (`{components.button-primary}`, `{components.nav-pill}`).

### Buttons
- **`button-primary`** — Ink black pill, cream text, 20px radius, the workhorse CTA.
- **`button-outlined`** — White surface, black text, 1.5px black border, 20px radius.
- **`button-consent`** — Signal Orange pill — exclusive to consent / legal / compliance flows.
- **`button-satellite`** — Circular white micro-CTA docked onto circular portraits.
- **`button-icon-circle`** — 40px circular icon-only.

### Cards & Containers
- **`hero-frame`** — Stadium-shaped media frame at 40px radius for full-width video/imagery.
- **`card-portrait`** — Perfect circle service card, paired with a satellite CTA.
- **`card-pill`** — Pill-shaped portrait carousel card.
- **`chip`** — White pill chip used inside carousel cards.
- **`card-lifted`** — One step up from canvas, 40px radius.

### Inputs
- **`input`** — Pill-shaped, 999px radius, used for the expanded search field in the nav.

### Navigation
- **`nav-pill`** — Floating white pill below the viewport top — soft shadow, full pill, ~16/40px padding.

### Footer
- **`footer`** — Ink black surface with white text, large conversational headline above a 4-column link grid.
- **`selector-footer`** — Country/language pill in the footer.

### Decorative Orbital Lines
A signature motif: thin (~1–1.5px) single-weight curved lines in `{colors.signal-light}` tracing arcs between circular portraits. These imply connection, span widths from ~200px up to full-viewport arcs, and feel hand-drawn (subtle irregularity) rather than perfect CSS curves. Appear only in sections with circular portrait content.

## Do's and Don'ts

### Do
- Use Canvas Cream (`{colors.background}`) as the default body background — never pure white
- Mask service/feature imagery as perfect circles, not rectangles or rounded rectangles
- Attach a white satellite CTA to the bottom-right of each circular portrait
- Set headlines in MarkForMC weight 500 with -2% letter-spacing
- Use weight 450 (not 400) for body paragraphs
- Keep primary CTAs as Ink Black pills (20px radius) with cream text
- Use Signal Orange only on consent, legal, or compliance actions
- Float the nav as a rounded white pill below the viewport top, not flush at y=0
- Build page rhythm from three surface tones: canvas cream → lifted cream → ink footer
- Use thin Light Signal Orange arcs between service cards to imply connection

### Don't
- Don't use pure white as a page background — it breaks the warm editorial tone
- Don't round image frames at 8–16px — Mastercard either uses full-pill, 40px, or full-circle
- Don't use Signal Orange for marketing CTAs — it reads as cookie-consent orange
- Don't mix typefaces — no serif accent, no script, no secondary display font
- Don't crowd the nav with more than six top-level links
- Don't drop hard shadows — all elevation should use 48px+ spread
- Don't use uppercase for anything larger than the 14px eyebrow label
- Don't omit the tiny accent dot before eyebrow labels — it's the identity
- Don't place circular portraits on a grid — their magic comes from asymmetric placement

---

## Responsive Behavior

### Breakpoints

| Name | Width | Key Changes |
|---|---|---|
| Mobile | ≤ 767px | Nav pill shows logo + menu + search only; primary links hide behind hamburger; service portraits stack single-column centered; hero headline drops from 64px to ~40px; footer columns collapse into a vertical accordion |
| Tablet | 768–1023px | Nav pill shows 2–3 primary links truncated; service portraits arrange 2-up; hero headline ~48px |
| Desktop | ≥ 1024px | Full nav with 5 primary links centered; service portraits asymmetrically placed with decorative orbital lines; hero headline 64px |
| Wide | ≥ 1440px | Content max-width caps at ~1280px; gutters grow symmetrically; orbital lines extend further |

### Touch Targets
All interactive elements comfortably exceed 44×44px. The satellite CTA is ~50–60px. The nav pill buttons are ~48px tall. Mobile hamburger and search are 48×48px. No link or button drops below 40px in any breakpoint.

### Collapsing Strategy
- **Nav**: full pill → compact pill with hamburger. Pill shape is preserved across breakpoints.
- **Service grid**: asymmetric constellation → 2-up → 1-up stack. Orbital arcs are removed on mobile.
- **Spacing**: section vertical padding compresses from 128px to 48px on mobile.
- **Content**: two-column hero becomes stacked.
- **Footer**: 4 columns → 1 column accordion with chevron toggles per section.

### Image Behavior
Circular portraits scale proportionally (maintaining the perfect circle at every size). Hero video frames maintain their 40px radius at every breakpoint, but the frame itself shrinks with the viewport. Lazy loading is standard with a cream-tinted blur-up placeholder.

---

## Agent Prompt Guide

### Quick Color Reference
- Primary CTA: "Ink Black (`{colors.ink}`) — the warm near-black"
- Background: "Canvas Cream (`{colors.background}`) — warm putty body canvas, never pure white"
- Lifted surface: "Lifted Cream (`{colors.surface}`)"
- Heading text: "Ink Black (`{colors.ink}`)"
- Body text: "Ink Black (`{colors.ink}`) at weight 450"
- Muted text: "Slate Gray (`{colors.slate-gray}`)"
- Signal / Consent: "Signal Orange (`{colors.primary}`) — reserve for cookie consent and legal actions"
- Accent arc: "Light Signal Orange (`{colors.signal-light}`) — orbital decorative lines only"
- Footer: "Ink Black (`{colors.ink}`) with White text"

### Example Component Prompts
- "Create a circular portrait card 300px in diameter, with a square photograph cropped to a perfect circle. Attach a 56px white satellite button with a dark arrow icon at the bottom-right, so it protrudes ~40% outside the portrait. Below the portrait, add an eyebrow label with a Light Signal Orange dot and uppercase 'SERVICES' text in MarkForMC weight 700 at 14px. Below the eyebrow, set a 24px / weight 500 title in `{colors.ink}`."
- "Design a primary CTA button: `{colors.ink}` background, `{colors.background}` text, 20px border-radius, 6px vertical and 24px horizontal padding, MarkForMC font at 16px weight 500 with -2% letter-spacing."
- "Build a floating navigation pill: white background with soft shadow, 999px border-radius, ~16px vertical and 40px horizontal internal padding. Position it 24px below the viewport top, centered, with the Mastercard logo at the left, five primary links centered with 48px gap, and a circular 48px search button at the right."
- "Create a hero media frame: 40px border-radius on all corners, full viewport width minus 48px gutters, ~60% viewport height, dark background for video content. Place it directly on the cream canvas with no shadow."
- "Design a footer: `{colors.ink}` background, white text, 4-column link grid with uppercase muted column headers at 14px weight 700 +4% tracking. Include a large conversational H2 above the grid, a 1px white-at-30%-opacity horizontal divider below, and a bottom row with copyright, legal small-print links, a pill-shaped country selector, and four social icons."

### Iteration Guide
1. Focus on ONE component at a time — don't redesign multiple surfaces in parallel
2. Reference specific color names AND tokens from this document
3. Use natural language ("warm putty cream", "stadium pill", "circular portrait with satellite CTA") alongside technical values
4. Describe the desired "feel" (editorial, soft, institutional) alongside specific measurements
5. When in doubt, reach for one of three radii: 20px (buttons), 40px (hero/stadium), or 999px (pill/nav)
6. Default backgrounds to Canvas Cream (`{colors.background}`), not white — this single change shifts the entire mood toward Mastercard

### Known Gaps
- The live page uses MarkForMC, a proprietary licensed typeface. Sofia Sans is the closest open-source substitute and is listed in Mastercard's own fallback stack.
- Tablet breakpoint specifics (768–1023px) were inferred; intermediate layouts may vary per section.
- The exact "whisper" cream tone for ghost-watermark headlines varies per section.
- Third-party consent orange (`{colors.primary}`) is Mastercard's documented consent signal and should not be confused with any marketing CTA color.
- The Mastercard logo mark (`{colors.brand-red}` + `{colors.brand-yellow}`) is a brand asset, not a UI palette entry.
