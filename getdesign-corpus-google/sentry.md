---
version: alpha
name: Sentry
description: Dark-mode-first developer tool aesthetic — deep purple-black canvas, Dammit Sans display headlines, Rubik UI workhorse, lime-green and coral accents, and signature inset-shadow buttons.

colors:
  # Canvas + surfaces
  background: "#1f1633"
  background-deep: "#150f23"
  surface: "#362d59"
  surface-light: "#ffffff"

  # Brand purple spectrum
  primary: "#6a5fc1"
  on-primary: "#ffffff"
  purple-muted: "#79628c"
  purple-deep: "#422082"
  border-purple: "#584674"

  # Vibrant accents
  accent-lime: "#c2ef4e"
  accent-coral: "#ffb287"
  accent-pink: "#fa7faa"

  # Ink
  ink: "#ffffff"
  ink-muted: "#e5e7eb"
  ink-on-light: "#1f1633"
  code-yellow: "#dcdcaa"

  # Glass / overlays (opaque approximations of original rgba)
  glass-light: "#3d3450"  # was rgba(255,255,255,0.18) over #1f1633 — Google format requires hex
  glass-hover: "#2a1a4a"  # was rgba(54,22,107,0.14) over #1f1633 — Google format requires hex

  # Borders
  border-input: "#cfcfdb"
  border-dark: "#362d59"

  # Shadow tints (opaque approximations)
  shadow-ambient: "#160f24"  # was rgba(22,15,36,0.9) — Google format requires hex
  shadow-elevated: "#1a1422"  # was rgba(0,0,0,0.18) over background — Google format requires hex
  shadow-card: "#15101f"  # was rgba(0,0,0,0.1) over background — Google format requires hex
  shadow-inset: "#150f23"  # was rgba(0,0,0,0.1) inset — Google format requires hex

typography:
  display-hero:
    fontFamily: "Dammit Sans, Rubik, system-ui, sans-serif"
    fontSize: 88px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0px
  display-secondary:
    fontFamily: "Dammit Sans, Rubik, system-ui, sans-serif"
    fontSize: 60px
    fontWeight: 500
    lineHeight: 1.1
    letterSpacing: 0px
  heading-section:
    fontFamily: "Rubik, -apple-system, system-ui, sans-serif"
    fontSize: 30px
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: 0px
  heading-sub:
    fontFamily: "Rubik, -apple-system, system-ui, sans-serif"
    fontSize: 27px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0px
  card-title:
    fontFamily: "Rubik, -apple-system, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0px
  feature-title:
    fontFamily: "Rubik, -apple-system, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0px
  body:
    fontFamily: "Rubik, -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  body-emphasis:
    fontFamily: "Rubik, -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: 0px
  nav-label:
    fontFamily: "Rubik, -apple-system, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0px
  uppercase-label:
    fontFamily: "Rubik, -apple-system, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0.2px
  button-text:
    fontFamily: "Rubik, -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: 0.2px
  caption:
    fontFamily: "Rubik, -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.2px
  caption-small:
    fontFamily: "Rubik, -apple-system, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 2.0
    letterSpacing: 0px
  micro-label:
    fontFamily: "Rubik, -apple-system, system-ui, sans-serif"
    fontSize: 10px
    fontWeight: 600
    lineHeight: 1.8
    letterSpacing: 0.25px
  code:
    fontFamily: "Monaco, Menlo, Ubuntu Mono, monospace"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px

spacing:
  hairline: 1px
  micro: 2px
  xxs: 4px
  xs: 6px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
  2xl: 32px
  3xl: 40px
  4xl: 64px
  5xl: 80px
  6xl: 120px

rounded:
  none: 0px
  sm: 6px
  md: 8px
  lg: 12px
  xl: 13px
  pill: 18px

components:
  # Primary muted purple button (signature inset-shadow)
  button-primary:
    backgroundColor: "{colors.purple-muted}"
    textColor: "{colors.ink}"
    typography: "{typography.button-text}"
    rounded: "{rounded.xl}"
    padding: 12px 16px
  button-primary-hover:
    backgroundColor: "{colors.purple-muted}"
    textColor: "{colors.ink}"

  # Glass white button
  button-glass:
    backgroundColor: "{colors.glass-light}"
    textColor: "{colors.ink}"
    typography: "{typography.button-text}"
    rounded: "{rounded.lg}"
    padding: 8px 8px
  button-glass-hover:
    backgroundColor: "{colors.glass-hover}"
    textColor: "{colors.ink}"

  # White solid CTA
  button-white:
    backgroundColor: "{colors.surface-light}"
    textColor: "{colors.ink-on-light}"
    typography: "{typography.button-text}"
    rounded: "{rounded.md}"
    padding: 12px 16px
  button-white-hover:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.ink}"
  button-white-focus:
    backgroundColor: "{colors.accent-coral}"
    textColor: "{colors.ink-on-light}"

  # Deep violet (select / dropdown)
  button-violet:
    backgroundColor: "{colors.purple-deep}"
    textColor: "{colors.ink}"
    typography: "{typography.button-text}"
    rounded: "{rounded.md}"
    padding: 8px 16px

  # Text input
  input:
    backgroundColor: "{colors.surface-light}"
    textColor: "{colors.ink-on-light}"
    typography: "{typography.body}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
  input-focus:
    backgroundColor: "{colors.surface-light}"
    textColor: "{colors.ink-on-light}"

  # Cards / panels
  card:
    backgroundColor: "{colors.background-deep}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 24px
  card-glass:
    backgroundColor: "{colors.glass-light}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.lg}"
    padding: 24px

  # Navigation
  nav-bar:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-label}"
    padding: 16px 32px
  nav-link:
    textColor: "{colors.ink}"
    typography: "{typography.nav-label}"
    padding: 8px 12px
  nav-link-hover:
    textColor: "{colors.primary}"

  # Badges
  badge-lime:
    backgroundColor: "{colors.accent-lime}"
    textColor: "{colors.ink-on-light}"
    typography: "{typography.micro-label}"
    rounded: "{rounded.pill}"
    padding: 4px 8px
  badge-purple:
    backgroundColor: "{colors.purple-deep}"
    textColor: "{colors.ink}"
    typography: "{typography.micro-label}"
    rounded: "{rounded.pill}"
    padding: 4px 8px
---

# Sentry Design System

## Overview

Sentry's website is a dark-mode-first developer tool interface that speaks the language of code editors and terminal windows. The entire aesthetic is rooted in deep purple-black backgrounds (`{colors.background}`, `{colors.background-deep}`) that evoke the late-night debugging sessions Sentry was built for. Against this inky canvas, a carefully curated set of purples, pinks, and a distinctive lime-green accent (`{colors.accent-lime}`) create a visual system that feels simultaneously technical and vibrant.

The typography pairing is deliberate: "Dammit Sans" appears at hero scale (88px, weight 700) as a display font with personality and attitude that matches Sentry's irreverent brand voice ("Code breaks. Fix it faster."), while Rubik serves as the workhorse UI font across all functional text — headings, body, buttons, captions, and navigation. Monaco provides the monospace layer for code snippets and technical content, completing the developer-tool trinity.

What makes Sentry distinctive is its embrace of the "dark IDE" aesthetic without feeling cold or sterile. Warm purple tones replace the typical cool grays of developer tools, and bold illustrative elements (3D characters, colorful product screenshots) punctuate the dark canvas. The button system uses a signature muted purple (`{colors.purple-muted}`) with inset shadows that creates a tactile, almost physical quality — buttons feel like they could be pressed into the surface.

**Key Characteristics:**
- Dark purple-black backgrounds (`{colors.background}`, `{colors.background-deep}`) — never pure black
- Warm purple accent spectrum: from deep (`{colors.surface}`) through mid (`{colors.purple-muted}`, `{colors.primary}`) to vibrant (`{colors.purple-deep}`)
- Lime-green accent (`{colors.accent-lime}`) for high-visibility CTAs and highlights
- Pink/coral accents (`{colors.accent-coral}`, `{colors.accent-pink}`) for focus states and secondary highlights
- "Dammit Sans" display font for brand personality at hero scale
- Rubik as primary UI font with uppercase letter-spaced labels
- Monaco monospace for code elements
- Inset shadows on buttons creating tactile depth
- Frosted glass effects with `blur(18px) saturate(180%)`

## Colors

### Primary Brand
- **Deep Purple** (`{colors.background}`): Primary background, the defining color of the brand.
- **Darker Purple** (`{colors.background-deep}`): Deeper sections, footer, secondary backgrounds.
- **Border Purple** (`{colors.surface}`): Borders, dividers, subtle structural lines.

### Accent Colors
- **Sentry Purple** (`{colors.primary}`): Primary interactive color — links, hover states, focus rings.
- **Muted Purple** (`{colors.purple-muted}`): Button backgrounds, secondary interactive elements.
- **Deep Violet** (`{colors.purple-deep}`): Select dropdowns, active states, high-emphasis surfaces.
- **Lime Green** (`{colors.accent-lime}`): High-visibility accent, special links, badge highlights.
- **Coral** (`{colors.accent-coral}`): Focus state backgrounds, warm accent.
- **Pink** (`{colors.accent-pink}`): Focus outlines, decorative accents.

### Text Colors
- **Pure White** (`{colors.ink}`): Primary text on dark backgrounds.
- **Light Gray** (`{colors.ink-muted}`): Secondary text, muted content.
- **Code Yellow** (`{colors.code-yellow}`): Syntax highlighting, code tokens.

### Surface & Overlay
- **Glass Light** (`{colors.glass-light}`): Frosted glass button backgrounds (opaque approximation of `rgba(255, 255, 255, 0.18)` over the canvas).
- **Glass Hover** (`{colors.glass-hover}`): Hover overlay on glass elements (opaque approximation of `rgba(54, 22, 107, 0.14)`).
- **Input White** (`{colors.surface-light}`): Form input backgrounds (light context).
- **Input Border** (`{colors.border-input}`): Form field borders.

### Shadows
- **Ambient Glow** (`{colors.shadow-ambient}`): Deep purple ambient shadow tint.
- **Elevated Hover** (`{colors.shadow-elevated}`): Elevated hover state tint.
- **Card Shadow** (`{colors.shadow-card}`): Standard card elevation tint.
- **Inset Button** (`{colors.shadow-inset}`): Tactile pressed effect tint.

## Typography

### Font Families
- **Display**: `Dammit Sans` — brand personality font for hero headings
- **Primary UI**: `Rubik`, with fallbacks `-apple-system, system-ui, Segoe UI, Helvetica, Arial`
- **Monospace**: `Monaco`, with fallbacks `Menlo, Ubuntu Mono`

### Hierarchy

The complete type scale lives in the `typography:` token block above. Reference tokens directly (`{typography.display-hero}`, `{typography.body}`).

| Token | Use |
|---|---|
| `display-hero` | Maximum impact, brand voice (88px Dammit Sans) |
| `display-secondary` | Secondary hero text (60px Dammit Sans) |
| `heading-section` | Major section titles (30px) |
| `heading-sub` | Feature section headers (27px) |
| `card-title` | Card and block headings (24px) |
| `feature-title` | Emphasized feature names (20px) |
| `body` | Standard body text (16px) |
| `body-emphasis` | Bold body, nav items |
| `nav-label` | Navigation links (15px) |
| `uppercase-label` | Uppercase category labels |
| `button-text` | Button labels (14px uppercase) |
| `caption` | Often uppercase metadata |
| `caption-small` | Subtle annotations (12px) |
| `micro-label` | Uppercase tiny labels (10px) |
| `code` | Code blocks, technical text |

### Principles
- **Dual personality**: Dammit Sans brings irreverent brand character at display scale; Rubik provides clean professionalism for everything functional.
- **Uppercase as system**: Buttons, captions, labels, and micro-text all use `text-transform: uppercase` with subtle letter-spacing (0.2px–0.25px), creating a systematic "technical label" pattern throughout.
- **Weight stratification**: Rubik uses 400 (body), 500 (emphasis/nav), 600 (titles/strong), 700 (buttons/CTAs) — a clean four-tier weight system.
- **Tight headings, relaxed body**: All headings use 1.10–1.25 line-height; body uses 1.50; small captions expand to 2.00 for readability at tiny sizes.

## Layout

### Spacing System
The complete spacing scale lives in the `spacing:` token block above. Base unit is 8px.

The scale supports both compact UI chrome (`hairline`–`sm`) and generous section breaks (`4xl`–`6xl`).

### Grid & Container
- Max content width: 1152px (XL breakpoint)
- Responsive padding: 32px (mobile) → 64px (tablet+)
- Content centered within container
- Full-width dark sections with contained inner content

### Whitespace Philosophy
- **Dark breathing room**: Generous vertical spacing between sections (`4xl`–`5xl`+) lets the dark background serve as a visual rest.
- **Content islands**: Feature sections are self-contained blocks floating in the dark purple sea, each with its own internal spacing rhythm.
- **Asymmetric padding**: Buttons use asymmetric padding patterns (12×16px, 8×12px) that feel organic rather than rigid.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Sunken (Level -1) | Inset shadow tinted with `{colors.shadow-inset}` | Primary buttons (tactile pressed feel) |
| Flat (Level 0) | No shadow | Default surfaces, dark backgrounds |
| Surface (Level 1) | Subtle drop shadow tinted `{colors.shadow-card}` | Glass buttons, subtle cards |
| Elevated (Level 2) | Mid drop shadow tinted `{colors.shadow-card}` | Cards, floating panels |
| Prominent (Level 3) | Larger drop shadow tinted `{colors.shadow-elevated}` | Hover states, modals |
| Ambient (Level 4) | Deep purple ambient glow tinted `{colors.shadow-ambient}` | Hero glow halos |

**Shadow Philosophy**: Sentry uses a unique combination of inset shadows (buttons feel pressed INTO the surface) and ambient glows (content radiates from the dark background). The deep purple ambient shadow (`{colors.shadow-ambient}`) is the signature — it creates a bioluminescent quality where content seems to emit its own purple-tinted light.

## Shapes

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Rare — Sentry avoids fully sharp corners |
| `sm` | 6px | Form inputs, small interactive elements |
| `md` | 8px | Buttons, cards, containers |
| `lg` | 12px | Larger containers, glass panels |
| `xl` | 13px | Primary muted buttons (signature value) |
| `pill` | 18px | Image containers, badges |

Note: Sentry uses 13px specifically for primary buttons — a nudge above the standard 12px that gives them a softer, more tactile profile.

## Components

The complete component spec lives in the `components:` token block above. Reference tokens directly (`{components.button-primary}`, `{components.card}`).

### Buttons
- **`button-primary`** — Muted purple (`{colors.purple-muted}`) with `1px solid {colors.border-purple}` border, `{rounded.xl}` corners, and the signature inset shadow that gives a pressed-in feel. Hover lifts with a deeper drop shadow.
- **`button-glass`** — Frosted glass panel (`{colors.glass-light}`) for secondary actions on dark surfaces. Pair with `backdrop-filter: blur(18px) saturate(180%)`.
- **`button-white`** — High-visibility white CTA on dark backgrounds. Hover transitions to `{colors.primary}`; focus shifts to coral (`{colors.accent-coral}`) with a 2px purple outline.
- **`button-violet`** — Deep violet (`{colors.purple-deep}`) used for selects, dropdowns, and high-emphasis surfaces.

### Inputs
- **`input`** — White surface, dark text, `1px solid {colors.border-input}` border, `{rounded.sm}` corners. Focus state retains border color but adds an inner shadow.

### Links
- Default on dark: `{colors.ink}` underlined; hover transitions to `{colors.primary}`.
- Purple links: `{colors.primary}` default, hover underline.
- Lime accent links: `{colors.accent-lime}` default, hover to `{colors.primary}`.
- Dark context links: `{colors.surface}`, hover to `{colors.ink}`.

### Cards & Containers
- **`card`** — Dark deep-purple panel for content blocks.
- **`card-glass`** — Glass-effect panel with backdrop blur for layered surfaces.

### Navigation
Dark transparent header over hero content. Rubik 15px weight 500 for nav links, white text, hover to Sentry Purple. Uppercase category labels with `0.2px` letter-spacing. Mobile collapses to hamburger with full-width expansion.

### Badges
- **`badge-lime`** — Lime-green pill for highlight tags.
- **`badge-purple`** — Deep violet pill for category markers.

## Do's and Don'ts

### Do
- Use deep purple backgrounds (`{colors.background}`, `{colors.background-deep}`) — never pure black
- Apply inset shadows on primary buttons for the tactile pressed effect
- Use Dammit Sans ONLY for hero/display headings — Rubik for everything else
- Apply `text-transform: uppercase` with `letter-spacing: 0.2px` on buttons and labels
- Use the lime-green accent (`{colors.accent-lime}`) sparingly for maximum impact
- Employ frosted glass effects (`blur(18px) saturate(180%)`) for layered surfaces
- Maintain warm purple shadow tones — shadows should feel purple-tinted, not neutral gray
- Use Rubik's 4-tier weight system: 400 (body), 500 (nav/emphasis), 600 (titles), 700 (CTAs)

### Don't
- Don't use pure black for backgrounds — always use the warm purple-blacks
- Don't apply Dammit Sans to body text or UI elements — it's display-only
- Don't use standard gray (`#666`, `#999`) for borders — use purple-tinted grays (`{colors.surface}`, `{colors.border-purple}`)
- Don't drop the uppercase treatment on buttons — it's a system-wide pattern
- Don't use sharp corners (0px radius) — minimum `{rounded.sm}` for all interactive elements
- Don't mix the lime-green accent with the coral/pink accents in the same component
- Don't use flat (non-inset) shadows on primary buttons — the tactile quality is signature
- Don't forget letter-spacing on uppercase text — 0.2px minimum

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile | <576px | Single column, hamburger nav, stacked CTAs |
| Tablet | 576–768px | 2-column feature grids begin |
| Small Desktop | 768–992px | Full navigation, side-by-side layouts |
| Desktop | 992–1152px | Max-width container, full layout |
| Large | >1152px | Content max-width maintained, generous margins |

### Collapsing Strategy
- Hero text: 88px Dammit Sans → 60px → mobile scales
- Navigation: horizontal → hamburger with slide-out
- Feature sections: side-by-side → stacked cards
- Buttons: inline → full-width stacked on mobile
- Container padding: 4rem → 2rem

---

## Agent Prompt Guide

### Quick Color Reference
- Background: `{colors.background}` (primary), `{colors.background-deep}` (deeper)
- Text: `{colors.ink}` (primary), `{colors.ink-muted}` (secondary)
- Interactive: `{colors.primary}` (links/hover), `{colors.purple-muted}` (buttons)
- Accent: `{colors.accent-lime}` (lime highlight), `{colors.accent-coral}` (coral focus)
- Border: `{colors.border-dark}` (dark), `{colors.border-input}` (light context)

### Example Component Prompts
- "Create a hero section on deep purple background (`{colors.background}`). Headline at 88px Dammit Sans weight 700, line-height 1.20, white text. Sub-text at 16px Rubik weight 400, line-height 1.50. White solid CTA button (8px radius, 12px 16px padding), hover transitions to `{colors.primary}`."
- "Design a navigation bar: transparent over dark background. Rubik 15px weight 500, white text. Uppercase category labels with 0.2px letter-spacing. Hover color `{colors.primary}`."
- "Build a primary button: background `{colors.purple-muted}`, border 1px solid `{colors.border-purple}`, inset shadow tinted `{colors.shadow-inset}`, white uppercase text at 14px Rubik weight 700, letter-spacing 0.2px, radius 13px. Hover: shadow tinted `{colors.shadow-elevated}`."
- "Create a glass card panel: background `{colors.glass-light}`, backdrop-filter blur(18px) saturate(180%), radius 12px. White text content inside."
- "Design a feature section: `{colors.background-deep}` background, 24px Rubik weight 500 heading, 16px Rubik weight 400 body text. 14px uppercase lime-green (`{colors.accent-lime}`) label above heading."

### Iteration Guide
1. Always start with the dark purple background — the color palette is built FOR dark mode
2. Use inset shadows on buttons, ambient purple glows on hero sections
3. Uppercase + letter-spacing is the systematic pattern for labels, buttons, and captions
4. Lime green (`{colors.accent-lime}`) is the "pop" color — use once per section maximum
5. Frosted glass for overlaid panels, solid purple for primary surfaces
6. Rubik handles 90% of typography — Dammit Sans is hero-only
