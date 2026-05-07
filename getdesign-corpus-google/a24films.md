---
version: alpha
name: A24
description: Editorial film brutalism — pure monochrome, NB International Web at extreme negative tracking, zero radius corners, and darkened cinematic imagery as atmosphere.

colors:
  # Primary canvas + ink
  background: "#000000"
  surface: "#ffffff"
  ink: "#ffffff"
  ink-inverted: "#000000"

  # Brand accent — used only for hover
  primary: "#1883fd"

  # Text states
  on-background: "#ffffff"
  on-surface: "#000000"
  on-primary: "#ffffff"
  text-muted: "#888888"

  # Borders
  border: "#888888"
  border-light: "#1a1a1a"  # was rgba(255,255,255,0.1) — flattened for divider on dark
  border-dark: "#e6e6e6"   # was rgba(0,0,0,0.1) — flattened for divider on light
  input-border: "#4d4d4d"  # was rgba(255,255,255,0.3) — flattened on dark dialogs

  # Scrim and depth
  scrim: "#000000"  # represents rgba(0,0,0,0.4–0.6) backdrop overlay
  shadow-warm: "#c7c5c7"
  shadow-soft: "#1a1a1a"  # flattened multi-layer dialog shadow approximation

typography:
  display-hero:
    fontFamily: "NB International Web, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 74px
    fontWeight: 500
    lineHeight: 0.92
    letterSpacing: -2.96px
  display-large:
    fontFamily: "NB International Web, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 50px
    fontWeight: 600
    lineHeight: 0.95
    letterSpacing: -2px
  heading-section:
    fontFamily: "NB International Web, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 27px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: 0px
  heading-sub-bold:
    fontFamily: "NB International Web, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 26px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0px
  heading-sub:
    fontFamily: "NB International Web, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 21px
    fontWeight: 500
    lineHeight: 1.0
    letterSpacing: 0.3px
  button-ui:
    fontFamily: "NB International Web, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 19px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: 0px
  body-large:
    fontFamily: "NB International Web, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: -0.225px
  body:
    fontFamily: "NB International Web, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0px
  link:
    fontFamily: "NB International Web, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: -0.075px
  caption:
    fontFamily: "NB International Web, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: 0px
  micro:
    fontFamily: "NB International Web, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0px

spacing:
  micro: 4px
  xs: 6px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
  2xl: 40px
  3xl: 64px
  4xl: 80px
  5xl: 120px
  6xl: 160px

rounded:
  none: 0px
  near: 3px
  pill: 9999px

components:
  # Top navigation
  nav-bar:
    backgroundColor: "{colors.background}"
    textColor: "{colors.text-muted}"
    typography: "{typography.link}"
    padding: 16px 24px
  nav-link:
    textColor: "{colors.text-muted}"
    typography: "{typography.link}"
    padding: 8px 12px
  nav-link-hover:
    textColor: "{colors.primary}"

  # Newsletter / dialog primary CTA — white on black
  button-primary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink-inverted}"
    typography: "{typography.body}"
    rounded: "{rounded.none}"
    padding: 12px 20px

  # Inverted black on white
  button-inverted:
    backgroundColor: "{colors.ink-inverted}"
    textColor: "{colors.surface}"
    typography: "{typography.body}"
    rounded: "{rounded.none}"
    padding: 12px 20px

  # Close / dismiss icon button
  button-close:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    size: 24px

  # Card / container — flat panel
  card:
    backgroundColor: "{colors.background}"
    rounded: "{rounded.none}"
    padding: 32px
  card-light:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.none}"
    padding: 32px

  # Newsletter dialog panel
  dialog:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: 40px

  # Form input — transparent with bordered outline
  input:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.none}"
    padding: 12px 16px
  input-focus:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"

  # Category tag — minimal pure typographic
  badge-category:
    backgroundColor: "{colors.background}"
    textColor: "{colors.text-muted}"
    typography: "{typography.micro}"
    rounded: "{rounded.none}"
    padding: 2px 6px

  # Year annotation badge — superscript metadata
  badge-year:
    backgroundColor: "{colors.background}"
    textColor: "{colors.text-muted}"
    typography: "{typography.micro}"
    rounded: "{rounded.none}"
    padding: 0px 4px
---

# A24 Design System

## Overview

A24's website is editorial film brutalism — a digital cinemagazine where typography, imagery, and negative space are the only materials. The entire system runs on a pure monochromatic palette (`{colors.ink-inverted}`, `{colors.surface}`, `{colors.text-muted}`) with zero chromatic color anywhere. Where every other streaming/studio site leans into poster art, trailer reels, and algorithmic recommendations, A24's page opens with a darkened, out-of-focus still image and a list of film titles rendered as oversized serif-adjacent typography — the way a film critic might notate upcoming releases in a leather-bound notebook.

The signature move is the custom `NB International Web` typeface — a grotesk with pronounced geometric bones — deployed at extreme negative letter-spacing (`-2.96px` at 74px) and condensed line-height (`0.92`). This is the opposite of comfortable: the letterforms lock together into dense masses that read as inscriptions rather than sentences. The film titles ("The Drama", "Mother Mary", "Backrooms") are listed with a small superscript year annotation — a deliberate editorial gesture that turns a homepage into a publication's masthead. Nothing apologizes for the density.

What truly defines A24 is its **refusal of digital chrome**. There are no drop shadows on buttons (because there are barely any buttons). No rounded corners. No gradients. No color accents. No illustrations. The only "UI" is menu chrome in grey (`{colors.text-muted}`) at the top of the viewport and a newsletter dialog that appears as a dark-panel overlay. Everything else — film promotion, brand expression, navigation — happens through typography and cinematic imagery. The entire system is an exercise in subtraction.

**Key Characteristics:**
- Pure monochrome palette — black, white, mid-grey, nothing else
- NB International Web at extreme negative tracking (`-2.96px` at 74px) and tight line-height (`0.92`)
- Zero border-radius on all content surfaces — sharp editorial corners
- Darkened photographic imagery as backdrop (not as decoration — as atmosphere)
- Film titles rendered as oversized editorial lists with superscript year annotations
- Newsletter/modal dialogs as dark panels with soft layered shadows
- No visible drop shadows on primary content elements — depth comes from blur and overlay
- Minimal menu chrome — "MENU" / "A24" wordmark / search icon only

## Colors

### Primary
- **A24 Black** (`{colors.ink-inverted}`): The system's primary color — page backgrounds, dark panel fills, primary text on light surfaces, icon fills. Pure, unsoftened black.
- **A24 White** (`{colors.surface}`): Primary text on dark surfaces, headline color, button fill (when buttons appear), contrast element against black imagery.
- **Editorial Grey** (`{colors.text-muted}`): Secondary text, menu chrome, muted UI indicators, image captions, metadata (years, credits). The only mid-tone in the entire system.

### Accent Colors
- **Cinema Blue** (`{colors.primary}`): A single accent hex that appears in hover states for specific links — the rare chromatic moment in an otherwise monochrome system. Used exclusively for interactive state change, never for branding or decoration.

### Surface & Background
- **Pure Black** (`{colors.background}`): Dark section backgrounds, overlay panels, modal dialogs.
- **Pure White** (`{colors.surface}`): Light section backgrounds (rare on homepage, more common on film detail pages).
- **Image Backdrop**: Photographic or video backgrounds always applied with a slight blur/darken filter so title type sits legibly atop — never pure imagery, always slightly scrimmed.

### Borders
- **Hairline Light** (`{colors.border-light}`): Fine 1px divider on dark surfaces — barely visible.
- **Hairline Dark** (`{colors.border-dark}`): Fine 1px divider on light surfaces — barely visible.
- **Input Border** (`{colors.input-border}`): Border on dark dialog inputs.

### Decorative
- **Shadow Grey Warm** (`{colors.shadow-warm}`): Rare warm-gray used only in highly specific shadow/glow treatments.

### Gradient System
- A24 is **strictly gradient-free**. Depth and contrast come from solid-color relationships and selectively darkened photographic backgrounds. Any appearance of gradient is purely in blurred photographic imagery — never as a CSS effect on UI surfaces.

## Typography

### Font Family
- **Primary**: `NB International Web` (custom), with fallback: `Helvetica Neue`, `Helvetica`, `Arial`
- **Mono / Technical**: Same NB International Web for UI chrome — the typeface handles both display and utility roles
- **OpenType Features**: Standard only — the typeface's built-in character is the style

*Note: NB International is a commercial typeface from Neubau Berlin. For external implementations, Founders Grotesk or GT America serve as close substitutes; Helvetica Neue is the explicit fallback.*

### Hierarchy

The complete type scale lives in the `typography:` token block above. Use those tokens directly via reference (`{typography.display-hero}`, `{typography.body}`, etc.) rather than hardcoding values.

| Token | Use |
|---|---|
| `display-hero` | Maximum size — film titles, homepage master list (74px) |
| `display-large` | Secondary display moments, large section heads |
| `heading-section` | Film year annotations, minor headers (27px) |
| `heading-sub-bold` | Panel headings, feature titles (26px) |
| `heading-sub` | Card labels, navigation prominence (21px) |
| `button-ui` | Button labels (rare — "SIGN UP") |
| `body-large` | Editorial body copy |
| `body` | Standard reading text, button labels |
| `link` | Navigation, inline links |
| `caption` | Metadata, image captions, chrome labels |
| `micro` | Superscript year annotations next to titles |

### Principles
- **Extreme tight tracking as signature**: Display typography runs at `-2.96px` letter-spacing — aggressive enough that letterforms nearly touch. This is the brand's single most recognizable typographic move.
- **Condensed line-height**: Headline line-height of `0.92` (below 1.0) lets stacked title lines compress into dense blocks. Think stacked film titles at the edges of a magazine spread.
- **Mixed weights, no bold convention**: The system uses weights 400–700 fluidly — there's no "headings are bold, body is regular" convention. Weight is applied for tonal variety within a dense monochrome field.
- **Superscript annotations**: Year markers (`2026`, `2025`) appear as small superscript-style metadata attached to titles — an editorial typographic device borrowed from print magazines.
- **No script, no serif, no alternatives**: Only NB International Web, throughout. One typeface carries everything.
- **Uppercase for UI only**: Display text is title-case or proper case. Uppercase is reserved for menu chrome ("MENU") and occasional emphasis ("WANT MORE A24?").

## Layout

### Spacing System
The complete spacing scale lives in the `spacing:` token block above. Base unit is 8px with a fine sub-unit at 4px.

The scale is generous at the section level — `4xl`+ between major sections. Small UI chrome uses the `micro`–`md` range for dense precision.

### Grid & Container
- Max content width: approximately 1400–1500px for centered content
- Full-bleed breakouts dominate — imagery typically fills the viewport
- Two-column layouts appear on film detail pages (poster left, metadata right)
- Homepage is effectively a single-column display: imagery + title masthead list

### Whitespace Philosophy
- **Editorial sparseness**: The page uses massive negative space — especially around the title masthead. Film titles sit on the lower-left of a mostly-empty frame, letting the darkened backdrop image breathe
- **Type-anchored rhythm**: The title list establishes the only typographic hierarchy — everything else steps back to support it
- **Cinematic pacing**: Scroll reveals unfold like film cuts — one frame gives way to another with generous vertical breathing room

### Breakpoint Density
A24 ships with an unusually dense breakpoint list (2000px, 1600px, 1300px, 1024px, 896px, 768px, 640px, 530px, 425px, 371px, 360px) — the system is tuned for pixel-precise layout across hero imagery and title mastheads at every device width.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat (Level 0) | No shadow, no border | Page background, imagery, section containers |
| Hairline Divider (Level 1) | `1px solid {colors.border-light}` or `{colors.border-dark}` | Section separators, menu item dividers |
| Dialog Layered (Level 2) | Multi-layer soft directional shadow (formula below) | Modal dialogs, newsletter panels, overlay cards |
| Scrim Overlay (Level 3) | `{colors.scrim}` overlay at 40–60% on imagery | Darkening hero imagery for text legibility |
| Inset Warm Glow (Level 4) | `{colors.shadow-warm} 0px 0px 12px 2px` | Rare — specialty hover/focus states |

**Multi-Layer Dialog Shadow Formula** (six progressive layers from tight to expansive, each slightly more transparent — flattened representation in `{colors.shadow-soft}`):
- Layer 1: 2.8px 2.8px 2.2px
- Layer 2: 6.7px 6.7px 5.3px
- Layer 3: 12.5px 12.5px 10px
- Layer 4: 22.3px 22.3px 17.9px
- Layer 5: 41.8px 41.8px 33.4px
- Layer 6: 100px 100px 80px

Creates imperceptible-but-present depth under dialog panels. Directional — always cast down-right or up-right for stylistic consistency.

**Shadow Philosophy**: A24's depth system is almost invisible by design. Where most sites use shadows to signal "this element is interactive" or "this element is elevated", A24 hides shadows so subtly that they function more like structural hints than visual effects. The six-layer directional stack creates natural-feeling depth without any single layer being noticeable. On content elements (not dialogs), there are no shadows at all — depth comes entirely from the darkened backdrop imagery and solid-color contrast.

### Decorative Depth
- Photographic scrim overlays are the primary depth mechanism — darker imagery reads as background, lighter as foreground
- Blurred backdrops (CSS `filter: blur(8–16px)`) behind modal dialogs create clear foreground/background separation without any shadow
- No ambient shadows, no glow effects on content — depth is always either photographic or dialog-specific

## Shapes

The system is **binary**: sharp rectangular or fully circular. No mid-range radii.

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Default for **everything** — buttons, cards, panels, inputs, dialogs, images |
| `near` | 3px | Rare, used only on specific utility elements (cookie search box) |
| `pill` | 9999px | Reserved exclusively for toggle switches |

The system's radius philosophy is: sharp by default, pill only for functional switches. No mid-range.

## Components

The complete component spec lives in the `components:` token block above. Reference component tokens directly (`{components.button-primary}`, `{components.dialog}`) rather than reconstructing them.

### Buttons
A24 has almost no traditional buttons — the site is link-driven. When buttons do appear (mostly in dialogs and forms):
- **`button-primary`** — White on black for newsletter/dialog CTAs ("SIGN UP")
- **`button-inverted`** — Black on white for CTAs on light backgrounds
- **`button-close`** — 24×24 X-icon, no fill, no border — icon alone

### Cards & Containers
- **`card`** — `{colors.background}` panel for dark sections; `0px` radius
- **`card-light`** — `{colors.surface}` panel for light sections
- Internal padding: generous — `xl`–`3xl` for editorial content cards

### Dialogs / Modals
**`dialog`** — Pure black panel centered on blurred-darkened backdrop. ~400–480px width. Multi-layer directional soft shadow (extremely soft, almost invisible). Title in uppercase 16–18px weight 500–600. Transparent inputs with `{colors.input-border}` outline.

### Badges / Tags / Pills
- **`badge-year`** — Inline superscript-style next to film titles. No background, no border — pure typographic metadata.
- **`badge-category`** — Transparent background, uppercase 12px, `0px` radius, letter-spacing `0.05em`. Used for "DRAMA", "HORROR" category markers.

### Inputs & Forms
**`input`** — Transparent on dark panels, `{colors.surface}` on light. `{colors.input-border}` on dark, `{colors.ink-inverted}` 1px on light. Focus brightens border to full `{colors.surface}` on dark.

### Navigation
- Top nav: sparse horizontal bar — "MENU" (left), "A24" wordmark (center), search icon (right)
- All chrome in `{colors.text-muted}` or `{colors.surface}` depending on surface
- Hover: link color transitions to `{colors.primary}` — the system's only chromatic moment
- Sticky behavior: nav remains fixed at top, imagery scrolls beneath
- Mobile: "MENU" label expands to full-screen takeover menu

### Decorative Elements
**Darkened Backdrop Imagery** — Photographic or video backgrounds always darkened/scrimmed for text legibility. Applied as `background-image` with overlay `{colors.scrim}` at 40–60% or CSS `filter: brightness(0.6)`. Film imagery always cinematic, treated as brand asset.

**Title Masthead List** — Stacked film titles with superscript year annotations. Left-aligned or centered, full-width max. Active title in full white; upcoming titles in slightly dimmed white or grey. The page layout IS this list.

## Do's and Don'ts

### Do
- Use NB International Web (or Helvetica Neue fallback) for ALL typography — single-typeface system
- Apply extreme negative letter-spacing (`-2.96px`) at display sizes for the signature tight-tracked titles
- Keep line-height tight (`0.92–1.00`) on display type — condensed stacks are the look
- Use pure monochrome (`{colors.ink-inverted}`, `{colors.surface}`, `{colors.text-muted}`) — no chromatic color except rare Cinema Blue hover
- Apply `{rounded.none}` border-radius to all content surfaces — sharp corners are non-negotiable
- Use darkened/blurred photographic imagery as the primary backdrop and atmosphere
- Render film titles as editorial lists with superscript year annotations
- Apply multi-layer soft shadows only to dialog/modal panels, never to content elements
- Preserve generous negative space — especially around title mastheads

### Don't
- Don't introduce any chromatic color beyond the rare Cinema Blue (`{colors.primary}`) hover state
- Don't use rounded corners on content — `{rounded.none}` is a rule, not a default
- Don't add drop shadows to buttons, cards, or content blocks — depth comes from imagery
- Don't use gradients anywhere — solid color only
- Don't use multiple typefaces — NB International Web or Helvetica Neue for everything
- Don't use opacity washes or translucent colored tints — the system is binary (fully opaque or fully transparent)
- Don't default to positive or neutral letter-spacing on display type — tight negative tracking is the brand
- Don't add decorative icons or illustrations — typography and imagery carry all visual work
- Don't use pill-radius on buttons or cards — pill is reserved for functional toggles only
- Don't soften text color to dark-grey for body — either full white/black or `{colors.text-muted}` editorial grey

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Small Mobile | <400px | Reduced hero title (40–48px), stacked single-column |
| Mobile | 400–640px | Hero title 48–56px, mobile menu drawer |
| Large Mobile | 640–768px | Hero title 56–64px, adjusted chrome |
| Tablet | 768–1024px | Multi-column detail pages, hero 64–72px |
| Desktop | 1024–1550px | Full layout, hero at 72–74px |
| Large Desktop | ≥1550px | Maximum scale (74px+ hero), maximum container width |
| XL Cinema | ≥2000px | Specialized scaling for ultra-wide — large imagery, massive mastheads |

### Touch Targets
- Nav links: 15–16px with adequate surrounding padding
- Menu icon / hamburger: min 44×44px tap area
- Dialog close (X): min 24×24px icon with 40×40px tap area
- Newsletter input: standard 48px tap-height input

### Collapsing Strategy
- **Nav**: Horizontal "MENU / A24 / SEARCH" chrome collapses to simplified three-icon bar on mobile
- **Title Masthead**: Homepage film list scales proportionally — 74px desktop → 48–56px tablet → 40–48px mobile
- **Modal dialogs**: Full-width (minus 16px margin) on mobile, centered constrained-width on desktop
- **Imagery**: Hero imagery retains full-bleed treatment at all breakpoints, aspect ratios adjust
- **Section spacing**: Generous 160px desktop → 80–100px mobile — reduces but maintains cinematic pace
- **Letter-spacing**: Negative tracking scales proportionally — `-2.96px` at 74px becomes `-1.5px` at 40px

### Image Behavior
- Hero imagery maintains full-bleed, cinematic aspect at all sizes
- Darkening/blur scrims adapt intensity based on background luminance
- No art direction swaps between breakpoints — the same imagery adapts
- Film poster imagery (on detail pages) maintains 2:3 aspect ratio

---

## Agent Prompt Guide

### Quick Color Reference
- Primary Text (light bg): A24 Black (`{colors.ink-inverted}`)
- Primary Text (dark bg): A24 White (`{colors.surface}`)
- Secondary Text: Editorial Grey (`{colors.text-muted}`)
- Page Background (dark): Pure Black (`{colors.background}`)
- Page Background (light): Pure White (`{colors.surface}`)
- Hover Accent (rare): Cinema Blue (`{colors.primary}`)
- Backdrop Scrim: `{colors.scrim}` at 40–60% opacity

### Example Component Prompts
- "Create a homepage hero with a darkened photographic backdrop (scrim `{colors.scrim}` at 50%). Overlay a masthead film list bottom-left: four or five film titles in NB International Web 74px weight 500, line-height 0.92, letter-spacing -2.96px, pure white (`{colors.surface}`). After each title, place a superscript year annotation in 10–12px weight 400, same typeface, slightly dimmed white."
- "Design a newsletter modal dialog: pure black (`{colors.background}`) panel, `{rounded.none}`, centered over blurred-darkened backdrop. Title in uppercase 16–18px NB International Web weight 500–600. Body text in 15px weight 400 with line-height 1.67. Transparent input with `{colors.input-border}` 1px border. White-background button with black text, 12px 20px padding, 16px NB International Web weight 700. Apply the six-layer soft directional shadow for natural depth."
- "Build a top navigation bar on dark imagery: 'MENU' label left (15px grey `{colors.text-muted}`), 'A24' wordmark centered (white, NB International Web), search icon right (white). All items with 15px NB International Web weight 400. Hover on links transitions text to Cinema Blue (`{colors.primary}`)."
- "Create a film title block — title in NB International Web 74px weight 500, line-height 0.92, letter-spacing -2.96px, pure white. Year annotation in 10–12px weight 400, superscript-style, positioned directly after title. Optional category tag below in uppercase 12px weight 400, letter-spacing 0.05em, grey."
- "Design a section divider — `1px solid {colors.border-light}` on dark backgrounds or `{colors.border-dark}` on light. 40–80px vertical margin above and below. No decorative treatment — pure structural line."

### Iteration Guide
1. Typography is the entire design — invest in letter-spacing and line-height first, layout second
2. Apply `-2.96px` letter-spacing on all display type at 60px+ — this is the signature
3. Line-height `0.92` on headline stacks, `1.00` on single-line display — condensed is the look
4. Monochrome is a rule, not a preference — three hexes (`{colors.ink-inverted}`, `{colors.surface}`, `{colors.text-muted}`) cover 99% of all color decisions
5. Zero border-radius — never introduce rounded corners on content surfaces
6. Use darkened photographic imagery as the primary depth and atmosphere mechanism
7. Apply the six-layer directional shadow only to dialog/modal panels — never to content
8. Reserve Cinema Blue (`{colors.primary}`) for hover states only — one or two applications per page maximum
9. Single-typeface discipline — NB International Web (or Helvetica Neue fallback) everywhere, no exceptions
10. Generous negative space — especially around title mastheads. The empty frame IS the composition
