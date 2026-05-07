---
version: alpha
name: Bugatti
description: Cinema-black couture-showroom design — pure #000 canvas, monochrome austerity, monumental 288px Bugatti Display headlines, mono-caps UI, pill-shaped CTAs, and a strict refusal to compete with the product photography.

colors:
  # Primary canvas + ink
  background: "#000000"
  surface: "#000000"
  ink: "#ffffff"
  ink-inverted: "#000000"

  # Brand "accent" — there is none; treat white as primary interactive
  primary: "#ffffff"

  # Tertiary / disabled / hairline
  tertiary: "#999999"

  # Borders
  border: "#ffffff"
  border-subtle: "#999999"

  # Vignette overlay (legibility gradient over video)
  scrim: "#000000"  # used at low opacity in prose; flatten as opaque ink

  # Text states
  on-background: "#ffffff"
  on-surface: "#ffffff"
  on-primary: "#000000"
  text-secondary: "#999999"

typography:
  display-hero:
    fontFamily: "Bugatti Display, ui-sans-serif, system-ui, sans-serif"
    fontSize: 288px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0px
  display-mid:
    fontFamily: "Bugatti Display, ui-sans-serif, system-ui, sans-serif"
    fontSize: 60px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 1.4px
  display-section:
    fontFamily: "Bugatti Display, ui-sans-serif, system-ui, sans-serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.11
    letterSpacing: 0px
  mono-display:
    fontFamily: "Bugatti Monospace, ui-monospace, monospace"
    fontSize: 60px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0px
  body-display:
    fontFamily: "Bugatti Display, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  body-lead:
    fontFamily: "Bugatti Text Regular, ui-sans-serif, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0px
  body:
    fontFamily: "Bugatti Text Regular, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  body-compact:
    fontFamily: "Bugatti Text Regular, ui-sans-serif, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0px
  ui-link-caps:
    fontFamily: "Bugatti Monospace, ui-monospace, monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 1.4px
  button-caps:
    fontFamily: "Bugatti Monospace, ui-monospace, monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 1.4px
  button-compact:
    fontFamily: "Bugatti Monospace, ui-monospace, monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 1.2px
  caption:
    fontFamily: "Bugatti Monospace, ui-monospace, monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 1.4px
  caption-micro:
    fontFamily: "Bugatti Monospace, ui-monospace, monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 1.2px

spacing:
  xs: 4px
  sm: 6px
  md: 12px
  lg: 36px
  xl: 48px
  2xl: 64px

rounded:
  none: 0px
  sm: 6px
  pill: 9999px

components:
  # Top navigation
  nav-bar:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.ui-link-caps}"
    padding: 12px 24px
  nav-link:
    textColor: "{colors.ink}"
    typography: "{typography.ui-link-caps}"
    padding: 8px 12px

  # Primary CTA — white-outlined pill
  button-primary:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.button-caps}"
    rounded: "{rounded.pill}"
    padding: 12px 24px
  button-primary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.ink-inverted}"

  # Secondary — slightly rounded gray-bordered button
  button-secondary:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.button-compact}"
    rounded: "{rounded.sm}"
    padding: 6px 12px
  button-secondary-hover:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"

  # Ghost / link button
  button-ghost:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.button-compact}"
    rounded: "{rounded.none}"
    padding: 0px 0px

  # Bordered container — cookie/dialog frame
  card-bordered:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: 24px

  # Form input (deep-page default since homepage has none)
  input:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
  input-focus:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
---

# Bugatti Design System

## Overview

Bugatti.com does not behave like a website — it behaves like a feature-length car film that a visitor happens to be standing inside. The canvas is pure `{colors.background}`, the only color that appears at rest is `{colors.ink}`, and the entire page is carried by full-bleed hero video and photography with a single typographic moment laid over the top. There are no cards, no grids, no promotional modules, no newsletter signups, no three-column editorial layouts. It is one continuous cinema-black channel, interrupted only by the cars themselves and a few pill-shaped calls to action that quietly say things like "EXPLORE OUR OPPORTUNITIES" in ALL CAPS monospace.

The single most distinctive move in the entire system is **scale**: the `Bugatti Display` typeface runs at **288px** at hero moments. Two hundred and eighty-eight pixels. That is meant to be read the way you read a brand mark on the front of a Chiron: from across a showroom floor. At 288px the headline is no longer text, it is architecture. The secondary display scale of 60px feels almost miniature next to it, and the 36px mid-display feels like fine print. This typographic hierarchy is the most extreme of any production brand website in this catalog, and it is what gives Bugatti.com its sculptural, couture-showroom presence.

The other signature is **monochromatic austerity**. The entire homepage uses exactly three colors at rest: `{colors.background}`, `{colors.ink}`, and `{colors.tertiary}`. There is no accent, no brand blue, no hazard color, no commerce orange, no gradient wash. The designers have made a conscious decision that Bugatti's color system should be the car paint itself — the page is a black velvet display stand, and the only color that exists is whatever lacquer the hero vehicle happens to be wearing today. Bugatti refuses to compete with its own product.

**Key Characteristics:**
- Cinema-black `{colors.background}` canvas for the entire page — no gradients, no tints, no accents
- 288px Bugatti Display ALL-CAPS headline — the most extreme display scale in the catalog
- Three-font custom family: Bugatti Display (sculptural), Bugatti Monospace (UI labels), Bugatti Text Regular (body)
- Monochrome-only palette: black, white, and a single `{colors.tertiary}` mid gray for tertiary/disabled
- Pill buttons at `{rounded.pill}` radius — transparent with a 1px white border, padding 12px 24px
- Video- and photography-first page — the chrome is almost silent so the product can speak
- Mono UPPERCASE labels with 1.2–1.4px letter-spacing on every CTA, navigation link, and caption

## Colors

### Primary
- **Velvet Black** (`{colors.background}`): The entire canvas. Not near-black, not warm black — pure black. Bugatti treats this as a display-stand surface, the way a jewelry brand treats a black velvet cloth.
- **Showroom White** (`{colors.ink}`): All text, all borders, all CTAs. White is the only color that appears at rest on the chrome. It has the weight of typeset print on a matte museum label.

### Secondary & Tertiary
- **Silver Mist** (`{colors.tertiary}`): The single gray in the system. Used for secondary button borders, disabled states, and the thinnest hairline dividers. Treat this as the "75%-volume" version of white — never a color, just a quieter version of the same voice.

### Surface & Background
- **Velvet Black** (`{colors.surface}`): The only surface. There is no secondary surface, no elevated card, no modal backdrop. If something needs to feel "separate", it sits on the same black and is marked with a thin `{colors.tertiary}` border — no color change.

### Text
- **Primary Text** (`{colors.on-background}`): All headlines, body copy, button labels, and navigation items.
- **Tertiary Text** (`{colors.text-secondary}`): Disclaimer text, placeholder labels, and the faintest supporting metadata.

### Accent
There is none. Do not add one. If a real focus state is needed, use a 1px `{colors.ink}` ring instead.

### Gradient System
None. There are zero decorative gradients on Bugatti.com. The only "gradient" on the page is whatever natural light gradient exists inside the hero video of the car itself. The brand refuses to apply any chrome gradient that could compete with the atmospheric lighting of the product photography.

## Typography

### Font Families
- **Bugatti Display** — proprietary custom display, used only at very large sizes for hero and mid-display headlines. Designed to be read at architectural scale.
- **Bugatti Monospace** — custom monospaced face reserved for every UI label on the site. Strict mono tracking (1.2–1.4px letter-spacing) gives the UI the appearance of a technical dossier or telemetry printout.
- **Bugatti Text Regular** — body workhorse, used only for short paragraphs and inline reading copy.

The complete type scale lives in the `typography:` token block above. Reference tokens directly (`{typography.display-hero}`, `{typography.button-caps}`) rather than hardcoding values.

| Token | Use |
|---|---|
| `display-hero` | 288px monumental hero — architectural in presence |
| `display-mid` | 60px feature headlines, ALL CAPS optional |
| `display-section` | 36px section title |
| `mono-display` | 60px UPPERCASE technical/section labels |
| `body-display` | Display face used sparingly at body size |
| `body-lead` | Lead paragraph |
| `body` | Standard reading body |
| `body-compact` | Dense body |
| `ui-link-caps` | UPPERCASE primary navigation links |
| `button-caps` | UPPERCASE primary pill-button label |
| `button-compact` | UPPERCASE small pill-button label |
| `caption` | UPPERCASE eyebrows and tech-spec labels |
| `caption-micro` | Smallest tagging label |

### Principles
- **Bugatti Display is a sculpture, not a font.** Reserve for headlines at 36px minimum, ideally 60px+, and at least once per page use it at 200px+.
- **Bugatti Monospace owns the UI.** Every navigation link, every button, every caption, every eyebrow runs in Bugatti Monospace — usually UPPERCASE with 1.2–1.4px tracking.
- **Bugatti Text Regular is invisible.** It appears only in short paragraphs and inline reading copy.
- **There is no bold.** Every weight is regular (400). Bugatti uses scale for hierarchy, not weight.
- **Line-height is brutally tight at display.** Every Bugatti Display usage runs at line-height 1.00 or 1.11.

### Note on Substitutes
The 1.00 line-height and 288px scale assume the proprietary Bugatti Display face. If you substitute (Unbounded, Big Shoulders Display, Archivo Black), loosen line-height to ~1.05–1.10 and cap maximum display size at ~104–128px. Bugatti Monospace substitutes (Space Mono, JetBrains Mono) and Bugatti Text Regular substitutes (Inter, DM Sans) work without adjustment.

## Layout

### Spacing System
The complete spacing scale lives in the `spacing:` token block above. Bugatti uses a small handful of discrete gaps (4, 6, 12, 36, 48, 64px) and refuses to invent in-between values. Section padding is typically `{spacing.xl}`–`{spacing.2xl}` vertical. Hero panels are full-viewport-height, bypassing the scale entirely.

### Grid & Container
- Max width: 1720px (scales to ultra-wide for showroom and cinema monitors)
- No multi-column grid on the homepage — a stack of single full-width blocks
- Outer padding minimal — most sections bleed to the viewport edge

### Whitespace Philosophy
Bugatti's whitespace is **cinematic negative space** — the page is 90% empty even when content is present. The rhythm is full-bleed media → monumental headline → single pill CTA → scroll → next full-bleed media. The page breathes the way a museum breathes, with each exhibit getting its own silent room.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat (Level 0) | No shadow, no border | Default text and media on `{colors.background}` |
| Hairline (Level 1) | `1px solid {colors.border-subtle}` | Secondary containers, cookie-style dialogs |
| Outline (Level 2) | `1px solid {colors.border}` | Primary button outline, active state indicators |
| Vignette (Level 3) | Bottom-to-top dark scrim → transparent | Text-legibility gradient when type sits over video |

**Shadow Philosophy**: Zero meaningful `box-shadow` values. Bugatti does not use drop shadows. It does not use elevation rings. It does not use glowing focus states. Depth is implied by the 1px hairline of a border or the presence of a vignette gradient — nothing more. Decorative depth is zero gradients (except the legibility vignette), zero blurs, zero glows.

## Shapes

The radius system is binary plus one utility value — **rectangle, slightly-rounded utility, or full pill**. Nothing in between.

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Default for all media, cards, hero canvas |
| `sm` | 6px | Secondary rounded buttons, bordered frames, small utility containers |
| `pill` | 9999px | Primary pill buttons |

Bugatti has made an active decision that "slightly rounded rectangle" is a vulgar shape between 6px and 9999px, and committed to either true rectangle or true pill.

## Components

The complete component spec lives in the `components:` token block above. Reference component tokens directly rather than reconstructing them.

### Buttons
- **`button-primary`** — Transparent pill with 1px white border. The signature CTA. Hover fills white with black text.
- **`button-secondary`** — Transparent with 1px `{colors.border-subtle}` border, 6px radius. Compact utility (menu toggles, dialog close).
- **`button-ghost`** — Unbordered link button. Footer and tertiary nav.

### Cards & Containers
- **There are no cards.** Bugatti has no card component. The closest thing is the rare bordered section (`card-bordered`) for cookie-consent and modal-style dialogues.

### Inputs
- The homepage has no forms. On deeper pages, inputs default to black bg, 1px `{colors.border-subtle}` border, 6px radius. Focus shifts border to `{colors.border}` — no glow.

### Navigation
- Pure `{colors.background}` strip with the EB monogram or full BUGATTI wordmark centered, MENU left, STORE right. Both nav links Bugatti Monospace 14px UPPERCASE with 1.4px tracking. Hover signal is opacity shift to ~0.75 — no color change.

### Image & Video Treatment
- Aspect ratios: 16:9 and 21:9 hero, 4:3 mid-feature, 1:1 portraits.
- Most media is full-bleed with zero radius. When radius appears, it's `{rounded.sm}`.
- No zoom, no scale, no scrim on hover. The video plays — that is the hover state.

### Atmospheric Overlay
When type sits over video, Bugatti uses a subtle dark linear gradient from bottom (low-opacity black) to top (transparent) — the only "shadow-like" effect in the system. It's a vignette, not a drop shadow.

## Do's and Don'ts

### Do
- Keep the entire canvas `{colors.background}`. No off-black, no near-black, no warm black.
- Use Bugatti Display at architectural scale — minimum 36px, ideally 60px+, and once per page land a monumental 200px+ headline.
- Use Bugatti Monospace UPPERCASE with 1.2–1.4px tracking for every button, link, nav item, and caption.
- Use only white text at rest. `{colors.tertiary}` is only for disabled, tertiary, and thin borders.
- Use `{rounded.pill}` border radius for primary buttons — full pill, thin 1px white outline, transparent fill.
- Use full-bleed video and photography for every hero section. The product is the UI.
- Maintain line-height 1.00–1.11 on display headlines. Tight leading is the architecture.
- Treat whitespace like cinematic negative space — give every block its own silent room.

### Don't
- Don't introduce accent colors. No blue, no red, no commerce orange, no warning red.
- Don't use bold weights for hierarchy. Scale is the only hierarchy device.
- Don't use drop shadows on any element. Bugatti has no `box-shadow` in its chrome.
- Don't use cards or elevated surfaces.
- Don't use rounded rectangles between 6px and 9999px.
- Don't use Bugatti Display for body, buttons, or UI labels.
- Don't use Bugatti Monospace in lowercase for primary UI. Buttons and nav links are always ALL CAPS.
- Don't add gradients, glows, blurs, or glassmorphism anywhere.
- Don't put text over photography without a low-opacity bottom-up vignette if legibility is at risk.

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|---|---|---|
| Mobile | <640px | Single column, hamburger MENU, hero 9:16 or 16:9, headline ~48–72px |
| Small Tablet | 640–767px | Single column, padding opens slightly |
| Tablet | 768–1023px | Single column, nav expands to wordmark, headline ~120px |
| Small Desktop | 1024–1279px | Full desktop nav, headline ~200px |
| Desktop | 1280–1535px | Full layout, headline 240–260px |
| Large Desktop | 1536–1719px | Max headline (288px), ultra-wide hero |
| Ultra-Wide | ≥1720px | Container caps, hero locks at 21:9+ |

The dembrandt sweep detected 6 breakpoints (1720 → 1536 → 1280 → 1024 → 768 → 640) — Bugatti tunes for six clean thresholds rather than micro-adjusting every device boundary.

### Touch Targets
- Primary pill buttons at `12px 24px` padding with 14px text are ~38–42px tall — slightly below WCAG AAA 44px. Bump vertical padding to 14–16px for derivative work.
- Secondary buttons at `6px 12px` are ~28–32px tall — desktop pointer contexts only.
- Nav links: add `12–14px` vertical padding on mobile.

### Collapsing Strategy
- **Nav**: stays MENU / wordmark / STORE — there is no drawer.
- **Spacing**: section padding tightens 64 → 48 → 36 → 12px.
- **Type**: hero scales 288 → 200 → 120 → 60 → 48px.
- **Video**: 21:9 desktop ↔ 16:9 or 9:16 mobile cuts.

### Image & Video Behavior
- Hero video uses adaptive bitrate streaming with `poster=` fallback.
- Below-fold media uses `loading="lazy"` with `srcset`.
- Imagery served through `imgix` with transformation parameters.

---

## Agent Prompt Guide

### Quick Color Reference
- **Primary Canvas**: Velvet Black `{colors.background}`
- **Primary Text**: Showroom White `{colors.ink}`
- **Secondary / Disabled / Hairline**: Silver Mist `{colors.tertiary}`
- **Accent**: None. Do not add one.
- **Hover Signal**: Opacity shift or border-color shift — no color change

### Example Component Prompts
1. *"Create a monumental hero headline using Bugatti Display at 288px, ALL CAPS, white text on a pure black canvas, line-height 1.0, no letter-spacing. Place a full-bleed 21:9 hero video behind it with a low-opacity black bottom-up vignette for legibility."*
2. *"Design a primary pill CTA button: transparent background, 1px solid white border, 9999px border radius, 12px × 24px padding, Bugatti Monospace 14px / 400 / 1.4px letter-spacing UPPERCASE label in white. Hover fills the background white with black text, 250ms ease."*
3. *"Build a navigation bar: pure black background, MENU link left, centered BUGATTI wordmark (128×29px), STORE link right. All links in Bugatti Monospace 14px UPPERCASE with 1.4px letter-spacing in white."*
4. *"Create a mid-feature section heading: Bugatti Display 60px ALL CAPS in white, line-height 1.0, centered over a full-bleed photograph. Place a single primary pill CTA 48–64px below."*
5. *"Design a secondary utility button for a cookie dialog: transparent, 1px solid `{colors.border-subtle}` border, 6px border radius, 6px × 12px padding, Bugatti Monospace 12px UPPERCASE in white."*

### Iteration Guide
1. **Audit the canvas.** If it isn't pure `{colors.background}`, change it.
2. **Audit the palette.** Any color that isn't `{colors.background}`, `{colors.ink}`, or `{colors.tertiary}` is drift.
3. **Audit display scale.** Minimum monumental moment is 60px; aim for the upper half of the 60–288px range.
4. **Audit mono-caps discipline.** Every button, every nav link, every caption, every CTA should be Bugatti Monospace UPPERCASE with 1.2–1.4px tracking.
5. **Audit shadows and gradients.** Strip every `box-shadow`. Strip every gradient except the one legibility vignette.
6. **Audit radius.** Every container should land on `0`, `6px`, or `9999px`.
7. **Audit type weight.** All weights should be 400.
8. **Audit whitespace.** If a section feels cramped, add 48–64px.
9. **Audit product presence.** Every hero section should have a vehicle as the primary visual.
