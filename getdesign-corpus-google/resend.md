---
version: alpha
name: Resend
description: Cinematic dark gallery for email infrastructure — pure black void, three-font editorial hierarchy (Domaine, ABC Favorit, Inter), icy blue-tinted frost borders, multi-color accent scale, and pill primary CTAs.

colors:
  # Primary
  background: "#000000"
  ink: "#f0f0f0"
  ink-pure: "#ffffff"

  # Brand / Primary accent
  primary: "#3b9eff"

  # Orange scale
  orange-base: "#ff5900"
  orange-primary: "#ff801f"
  orange-light: "#ffa057"

  # Green scale
  green-base: "#22ff99"
  green-primary: "#11ff99"

  # Blue scale
  blue-mid: "#0075ff"
  blue-strong: "#0081fd"

  # Other accents
  yellow: "#ffc53d"
  red: "#ff2047"

  # Neutrals
  silver: "#a1a4a5"
  dark-gray: "#464a4d"
  mid-gray: "#5c5c5c"
  medium-gray: "#494949"

  # Frost (opaque approximations)
  border: "#222b35"      # was rgba(214,235,253,0.19) — flatten for hex
  border-soft: "#1c2731" # was rgba(217,237,254,0.145)
  ring-shadow: "#1f2935" # was rgba(176,199,217,0.145)

  # Surfaces
  surface-frost: "#fcfdff"

  # Hover overlay
  hover-glass: "#474747"  # was rgba(255,255,255,0.28) — flatten over background

typography:
  display-hero:
    fontFamily: "domaine, Georgia, serif"
    fontSize: 96px
    fontWeight: 400
    lineHeight: 1.00
    letterSpacing: -0.96px
    fontFeature: "'ss01', 'ss04', 'ss11'"
  display-hero-mobile:
    fontFamily: "domaine, Georgia, serif"
    fontSize: 76.8px
    fontWeight: 400
    lineHeight: 1.00
    letterSpacing: -0.768px
    fontFeature: "'ss01', 'ss04', 'ss11'"
  section-heading:
    fontFamily: "aBCFavorit, ui-sans-serif, system-ui, sans-serif"
    fontSize: 56px
    fontWeight: 400
    lineHeight: 1.20
    letterSpacing: -2.8px
    fontFeature: "'ss01', 'ss04', 'ss11'"
  sub-heading:
    fontFamily: "aBCFavorit, ui-sans-serif, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.30
    letterSpacing: 0px
    fontFeature: "'ss01', 'ss04', 'ss11'"
  sub-heading-compact:
    fontFamily: "aBCFavorit, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: -0.8px
    fontFeature: "'ss01', 'ss04', 'ss11'"
  feature-title:
    fontFamily: "inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.50
    letterSpacing: 0px
  body-large:
    fontFamily: "inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0px
  body:
    fontFamily: "inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0px
  body-semibold:
    fontFamily: "inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.50
    letterSpacing: 0px
  nav-link:
    fontFamily: "aBCFavorit, ui-sans-serif, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0.35px
    fontFeature: "'ss01', 'ss03', 'ss04'"
  button:
    fontFamily: "inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0px
  caption:
    fontFamily: "inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.60
    letterSpacing: 0px
  small:
    fontFamily: "inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0px
  code-body:
    fontFamily: "commitMono, ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0px
  code-small:
    fontFamily: "commitMono, ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0px

spacing:
  micro: 1px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 20px
  2xl: 24px
  3xl: 32px
  4xl: 40px

rounded:
  sharp: 4px
  sm: 6px
  md: 8px
  lg: 12px
  xl: 16px
  2xl: 24px
  pill: 9999px

components:
  # Buttons
  button-pill-transparent:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 5px 12px
  button-pill-transparent-hover:
    backgroundColor: "{colors.hover-glass}"
    textColor: "{colors.ink}"
  button-pill-white:
    backgroundColor: "{colors.ink-pure}"
    textColor: "{colors.background}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 5px 12px
  button-ghost:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.sharp}"
    padding: 5px 12px

  # Cards / containers
  card:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xl}"
    padding: 24px
  card-large:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    rounded: "{rounded.2xl}"
    padding: 32px

  # Inputs
  input:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.sharp}"
    padding: 8px 12px

  # Navigation
  nav-bar:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: 16px 24px
  nav-link:
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: 8px 12px

  # Tabs
  tab:
    backgroundColor: "{colors.background}"
    textColor: "{colors.silver}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 8px 12px

  # Code panel
  code-panel:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.code-body}"
    rounded: "{rounded.2xl}"
    padding: 24px

  # Badges (multi-color accent)
  badge-orange:
    backgroundColor: "{colors.orange-base}"
    textColor: "{colors.orange-light}"
    typography: "{typography.small}"
    rounded: "{rounded.pill}"
    padding: 2px 10px
  badge-blue:
    backgroundColor: "{colors.blue-mid}"
    textColor: "{colors.primary}"
    typography: "{typography.small}"
    rounded: "{rounded.pill}"
    padding: 2px 10px
  badge-green:
    backgroundColor: "{colors.green-base}"
    textColor: "{colors.green-primary}"
    typography: "{typography.small}"
    rounded: "{rounded.pill}"
    padding: 2px 10px
  badge-yellow:
    backgroundColor: "{colors.background}"
    textColor: "{colors.yellow}"
    typography: "{typography.small}"
    rounded: "{rounded.pill}"
    padding: 2px 10px
  badge-red:
    backgroundColor: "{colors.background}"
    textColor: "{colors.red}"
    typography: "{typography.small}"
    rounded: "{rounded.pill}"
    padding: 2px 10px

  # Status / muted text
  text-muted:
    backgroundColor: "{colors.background}"
    textColor: "{colors.silver}"
    typography: "{typography.body}"
  text-faint:
    backgroundColor: "{colors.background}"
    textColor: "{colors.dark-gray}"
    typography: "{typography.caption}"
  text-tertiary:
    backgroundColor: "{colors.background}"
    textColor: "{colors.medium-gray}"
    typography: "{typography.caption}"
  text-hover:
    backgroundColor: "{colors.background}"
    textColor: "{colors.mid-gray}"
    typography: "{typography.body}"

  # Frost surfaces
  frost-panel:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xl}"
    padding: 24px
  frost-card-soft:
    backgroundColor: "{colors.border-soft}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: 16px

  # Border-only emphasis
  border-emphasis:
    backgroundColor: "{colors.border}"
    rounded: "{rounded.sharp}"
    padding: 0px

  # Strong blue surface
  surface-blue-strong:
    backgroundColor: "{colors.blue-strong}"
    textColor: "{colors.ink-pure}"
    rounded: "{rounded.lg}"
    padding: 16px

  # Frost primary surface (light)
  surface-frost:
    backgroundColor: "{colors.surface-frost}"
    textColor: "{colors.background}"
    rounded: "{rounded.lg}"
    padding: 16px

  # Subtle hairline / ring
  ring-shadow-rule:
    backgroundColor: "{colors.ring-shadow}"
    rounded: "{rounded.sharp}"
    padding: 0px

  # Sub-heading compact display
  feature-block:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.sub-heading-compact}"
    padding: 24px

  # Secondary heading
  helvetica-heading:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.feature-title}"
    padding: 0px
---

# Resend Design System

## Overview

Resend's website is a dark, cinematic canvas that treats email infrastructure like a luxury product. The entire page is draped in pure black (`{colors.background}`) with text that glows in near-white (`{colors.ink}`), creating a theater-like experience where content performs on a void stage. This isn't the typical developer-tool darkness — it's the controlled darkness of a photography gallery, where every element is lit with intention and nothing competes for attention.

The typography system is the star of the show. Three carefully chosen typefaces create a hierarchy that feels both editorial and technical: Domaine Display (a Klim Type Foundry serif) appears at massive 96px for hero headlines with barely-there line-height (1.00) and negative tracking (-0.96px), creating display text that feels like a magazine cover. ABC Favorit (by Dinamo) handles section headings with an even more aggressive letter-spacing (-2.8px at 56px), giving a compressed, engineered quality to mid-tier text. Inter takes over for body and UI, providing the clean readability that lets the display fonts shine. Commit Mono rounds out the family for code blocks.

What makes Resend distinctive is its icy, blue-tinted border system. Instead of neutral gray borders, Resend uses a frosty, slightly blue-tinted line that gives every container and divider a cold, crystalline quality against the black background. Combined with pill-shaped buttons (9999px radius), multi-color accent system (orange, green, blue, yellow, red — each with its own CSS variable scale), and OpenType stylistic sets (`"ss01"`, `"ss03"`, `"ss04"`, `"ss11"`), the result is a design system that feels premium, precise, and quietly confident.

**Key Characteristics:**
- Pure black background with near-white (`{colors.ink}`) text — theatrical, gallery-like darkness
- Three-font hierarchy: Domaine Display (serif hero), ABC Favorit (geometric sections), Inter (body/UI)
- Icy blue-tinted borders (`{colors.border}`) — every border has a cold, crystalline shimmer
- Multi-color accent system: orange, green, blue, yellow, red — each with numbered scales
- Pill-shaped buttons and tags (9999px radius) with transparent backgrounds
- OpenType stylistic sets (`"ss01"`, `"ss03"`, `"ss04"`, `"ss11"`) on display fonts
- Commit Mono for code — monospace as a design element, not an afterthought
- Whisper-level shadows using blue-tinted ring

## Colors

### Primary
- **Void Black** (`{colors.background}`): Page background, the defining canvas color.
- **Near White** (`{colors.ink}`): Primary text, button text, high-contrast elements.
- **Pure White** (`{colors.ink-pure}`): Maximum emphasis text, link highlights.

### Accent — Orange
- **Orange Base** (`{colors.orange-base}`): Subtle warm glow base.
- **Orange Primary** (`{colors.orange-primary}`): Primary orange accent — warm, energetic.
- **Orange Light** (`{colors.orange-light}`): Lighter orange for secondary use.

### Accent — Green
- **Green Base** (`{colors.green-base}`): Faint emerald wash base.
- **Green Primary** (`{colors.green-primary}`): Success indicator glow.

### Accent — Blue
- **Blue Mid** (`{colors.blue-mid}`): Medium blue accent.
- **Blue Strong** (`{colors.blue-strong}`): Stronger blue surface.
- **Bright Blue** (`{colors.primary}`): Bright blue — links, interactive elements.

### Accent — Other
- **Yellow** (`{colors.yellow}`): Warm gold for warnings or highlights.
- **Red** (`{colors.red}`): Error states, destructive actions.

### Neutral Scale
- **Silver** (`{colors.silver}`): Secondary text, muted links, descriptions.
- **Dark Gray** (`{colors.dark-gray}`): Tertiary text, de-emphasized content.
- **Mid Gray** (`{colors.mid-gray}`): Hover states, subtle emphasis.
- **Medium Gray** (`{colors.medium-gray}`): Quaternary text.

### Borders & Surfaces
- **Frost Border** (`{colors.border}`): The signature — icy blue-tinted borders.
- **Frost Border Alt** (`{colors.border-soft}`): Slightly lighter variant for list items.
- **Ring Shadow** (`{colors.ring-shadow}`): Blue-tinted shadow-as-border.
- **Frost Primary** (`{colors.surface-frost}`): Primary color token (slight blue tint).
- **Hover Glass** (`{colors.hover-glass}`): Button hover state on dark.

## Typography

### Font Families
- **Display Serif**: `domaine` (Domaine Display by Klim Type Foundry) — hero headlines.
- **Display Sans**: `aBCFavorit` (ABC Favorit by Dinamo), fallbacks: `ui-sans-serif, system-ui` — section headings.
- **Body / UI**: `inter`, fallbacks: `ui-sans-serif, system-ui` — body text, buttons, navigation.
- **Monospace**: `commitMono`, fallbacks: `ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas`.

### Hierarchy

The complete type scale lives in the `typography:` token block above. Reference tokens directly (`{typography.display-hero}`, `{typography.body}`, etc.) rather than hardcoding values.

| Token | Use |
|---|---|
| `display-hero` | Domaine 96px — hero headlines |
| `display-hero-mobile` | Domaine 76.8px scaled for mobile |
| `section-heading` | ABC Favorit 56px — section headings |
| `sub-heading` | ABC Favorit 20px — sub-headings |
| `sub-heading-compact` | ABC Favorit 16px compact display |
| `feature-title` | Inter 24px medium — section sub-headings |
| `body-large` | Inter 18px — introductions |
| `body` | Inter 16px — standard body |
| `body-semibold` | Inter 16px 600 — emphasis |
| `nav-link` | ABC Favorit 14px with positive tracking |
| `button` | Inter 14px medium — buttons |
| `caption` | Inter 14px relaxed — descriptions |
| `small` | Inter 12px — tags, fine print |
| `code-body` | Commit Mono 16px — code blocks |
| `code-small` | Commit Mono 14px — inline code |

### Principles
- **Three-font editorial hierarchy**: Domaine Display (serif, hero), ABC Favorit (geometric sans, sections), Inter (readable body). Each font has a strict role — they never cross lanes.
- **Aggressive negative tracking on display**: Domaine at -0.96px, ABC Favorit at -2.8px. Display type feels compressed, urgent, and designed.
- **Positive tracking on nav**: ABC Favorit nav links use +0.35px letter-spacing — the only positive tracking in the system.
- **OpenType as identity**: `ss01`, `ss03`, `ss04`, `ss11` stylistic sets are enabled on all ABC Favorit and Domaine text.
- **Commit Mono as design element**: The monospace font is used prominently for code examples, treated as a first-class visual element.

## Layout

### Spacing System
Base unit is **8px**. Scale ranges from 1px micro to 40px (`4xl`).

### Grid & Container
- Centered content with generous max-width
- Full-width black sections with contained inner content
- Single-column hero, expanding to feature grids below
- Code preview panels as full-width or contained showcases

### Whitespace Philosophy
- **Cinematic black space**: The black background IS the whitespace. Generous vertical spacing (80px–120px+) between sections creates a scroll-through-darkness experience where each section emerges like a scene.
- **Tight content, vast surrounds**: Text blocks and cards are compact internally, but float in vast dark space.
- **Typography-led rhythm**: The massive display fonts (96px) create their own vertical rhythm — each headline is a visual event.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat (Level 0) | No shadow, transparent background | Default — most elements on dark void |
| Ring (Level 1) | Ring-shadow border tint | Shadow-as-border for cards |
| Frost Border (Level 1b) | 1px solid frost border | Explicit borders — buttons, dividers, tabs |
| Subtle (Level 2) | `rgba(0,0,0,0.1) 0px 1px 3px` layered | Light card elevation |
| Focus (Level 3) | Heavy black focus ring | Accessibility |

**Shadow Philosophy**: Resend barely uses shadows at all. On a pure black background, traditional shadows are invisible — you can't cast a shadow into the void. Instead, Resend creates depth through its signature frost borders — thin, icy blue-tinted lines that catch light against the darkness. This creates a "glass panel floating in space" aesthetic where borders are the primary depth mechanism.

### Decorative Depth
- Subtle warm gradient glows behind hero content (orange/amber tints)
- Product screenshots create visual depth through their own internal UI
- No gradient backgrounds — depth comes from border luminance and content contrast

## Shapes

| Token | Value | Use |
|---|---|---|
| `sharp` | 4px | Buttons (ghost), inputs, small interactive elements |
| `sm` | 6px | Menu panels, navigation items |
| `md` | 8px | Tabs, content blocks |
| `lg` | 12px | Clipboard buttons, medium containers |
| `xl` | 16px | Feature cards, images, main buttons |
| `2xl` | 24px | Large panels, section containers |
| `pill` | 9999px | Primary CTAs, tags, badges |

## Components

The complete component spec lives in the `components:` token block above. Reference component tokens directly rather than reconstructing them.

### Buttons
- **`button-pill-transparent`** — Transparent fill, frost border, near-white text. Hover: hover-glass surface.
- **`button-pill-white`** — White solid pill, black text. High-contrast CTA ("Get started").
- **`button-ghost`** — Transparent, near-white text, sharp 4px radius. Secondary actions, tab items.

### Cards & Containers
- **`card`** — Transparent or subtle dark tint, frost border, 16px radius.
- **`card-large`** — Larger panels at 24px radius for sections.
- **`frost-panel`** — Frost-bordered panel for content showcases.
- **`frost-card-soft`** — Softer frost border for list items.

### Inputs & Forms
- **`input`** — Sharp 4px radius, near-white text, minimal styling — inherits dark theme.

### Navigation
- **`nav-bar`** — Sticky dark header with frost border bottom. "Resend" wordmark left-aligned.
- **`nav-link`** — ABC Favorit 14px weight 500 with +0.35px tracking.
- **`tab`** — Tabs with subtle selection indicator, 8px radius.

### Code Preview
- **`code-panel`** — Dark code blocks using Commit Mono with frost borders. Syntax-highlighted with multi-color accent tokens.

### Badges (multi-color accent)
- **`badge-orange`** / **`badge-blue`** / **`badge-green`** / **`badge-yellow`** / **`badge-red`** — Each product feature has its own accent color from the scale, low-opacity background with full-opacity text.

### Status / Text Variants
- **`text-muted`** / **`text-faint`** / **`text-tertiary`** / **`text-hover`** — Tiered neutral scale for descriptions and de-emphasized content.

### Surfaces
- **`surface-blue-strong`** — Stronger blue surface for selected emphasis.
- **`surface-frost`** — Light frost surface for inverted contexts.

## Do's and Don'ts

### Do
- Use pure black (`{colors.background}`) as the page background — the void is the canvas
- Apply frost borders (`{colors.border}`) for all structural lines — they're the blue-tinted signature
- Use Domaine Display ONLY for hero headings (96px), ABC Favorit for section headings, Inter for everything else
- Enable OpenType `"ss01"`, `"ss04"`, `"ss11"` on Domaine and ABC Favorit text
- Apply pill radius (9999px) to primary CTAs and tags
- Use the multi-color accent scale (orange/green/blue/yellow/red) with opacity variants for context-specific highlighting
- Keep shadows at ring level — on black, traditional shadows don't work
- Use +0.35px letter-spacing on ABC Favorit nav links — the only positive tracking

### Don't
- Don't lighten the background above pure black — the void is non-negotiable
- Don't use neutral gray borders — all borders must have the frost blue tint
- Don't apply Domaine Display to body text — it's a display-only serif
- Don't mix accent colors in the same component — each feature gets one accent color
- Don't use box-shadow for elevation on the dark background — use frost borders instead
- Don't skip the OpenType stylistic sets — they define the typographic character
- Don't use negative letter-spacing on nav links — ABC Favorit nav uses positive +0.35px
- Don't make buttons opaque on dark — transparency with frost border is the pattern

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|---|---|---|
| Mobile Small | <480px | Single column, tight padding, 76.8px hero |
| Mobile | 480–600px | Standard mobile, stacked layout |
| Desktop | >600px | Full layout, 96px hero, expanded sections |

*Note: Resend uses a minimal breakpoint system — only 480px and 600px detected. The design is desktop-first with a clean mobile collapse.*

### Touch Targets
- Pill buttons: adequate padding (5px 12px minimum)
- Tab items: 8px radius with comfortable hit areas
- Navigation links spaced with 0.35px tracking for visual separation

### Collapsing Strategy
- Hero: Domaine 96px → 76.8px on mobile
- Navigation: horizontal → hamburger
- Feature sections: side-by-side → stacked
- Code panels: maintain width, horizontal scroll if needed
- Spacing compresses proportionally

### Image Behavior
- Product screenshots maintain aspect ratio
- Dark screenshots blend seamlessly with dark background at all sizes
- Rounded corners (12px–16px) maintained across breakpoints

## Agent Prompt Guide

### Quick Color Reference
- Background: Void Black (`{colors.background}`)
- Primary text: Near White (`{colors.ink}`)
- Secondary text: Silver (`{colors.silver}`)
- Border: Frost Border (`{colors.border}`)
- Orange accent: `{colors.orange-primary}`
- Green accent: `{colors.green-primary}`
- Blue accent: `{colors.primary}`

### Example Component Prompts
- "Create a hero section on pure black (`{colors.background}`) background. Headline at 96px Domaine Display weight 400, line-height 1.00, letter-spacing -0.96px, near-white (`{colors.ink}`) text, OpenType 'ss01 ss04 ss11'. Subtitle at 20px ABC Favorit weight 400, line-height 1.30. Two pill buttons: white solid (`{colors.ink-pure}`, 9999px radius) and transparent with frost border (`{colors.border}`)."
- "Design a navigation bar: dark background with frost border bottom (1px solid `{colors.border}`). Nav links at 14px ABC Favorit weight 500, letter-spacing +0.35px, OpenType 'ss01 ss03 ss04'. White pill CTA right-aligned."
- "Build a feature card: transparent background, frost border (`{colors.border}`), 16px radius. Title at 56px ABC Favorit weight 400, letter-spacing -2.8px. Body at 16px Inter weight 400, `{colors.silver}` text."
- "Create a code block using Commit Mono 16px on dark background. Frost border container (24px radius). Syntax colors: orange (`{colors.orange-primary}`), blue (`{colors.primary}`), green (`{colors.green-primary}`), yellow (`{colors.yellow}`)."
- "Design an accent badge: background `{colors.orange-base}` low opacity, text `{colors.orange-light}`, 9999px radius, 12px Inter weight 500."

### Iteration Guide
1. Start with pure black — everything floats in the void
2. Frost borders (`{colors.border}`) are the universal structural element — not gray, not neutral
3. Three fonts, three roles: Domaine (hero), ABC Favorit (sections), Inter (body) — never cross
4. OpenType stylistic sets are mandatory on display fonts — they define the character
5. Multi-color accents at low opacity for backgrounds, full opacity for text
6. Pill shape (9999px) for CTAs and badges, standard radius (4px–16px) for containers
7. No shadows — use frost borders for depth against the void
