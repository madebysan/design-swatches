---
version: alpha
name: Readwise
description: Reading-app warmth — cream paper canvas, Source Serif 4 for content with Inter for chrome, amber-gold highlighter accent, and warm amber-tinted shadows that evoke pages on a desk.

colors:
  # Surfaces
  background: "#f8f4ed"
  surface: "#f2ece0"
  surface-elevated: "#fdfaf4"
  surface-hover: "#e8dfd0"

  # Text / Ink
  ink: "#1c1813"
  text-secondary: "#3d3530"
  text-tertiary: "#6b6258"
  text-muted: "#9a9086"
  text-divider: "#c7bfb3"

  # Brand accent
  primary: "#c19a3d"
  primary-warm: "#d4b15a"
  accent-terracotta: "#b85c3e"

  # Borders
  border: "#e0d6c3"
  border-strong: "#d4c9b3"

  # Dark candle mode
  candle-background: "#1a1613"
  candle-surface: "#26201a"
  candle-border: "#3a3128"
  candle-text: "#e8dfd0"
  candle-text-secondary: "#b8ac9a"
  candle-accent: "#d4b15a"

  # Highlights (opaque approximations)
  highlight-yellow: "#e2cea0"  # was rgba(193,154,61,0.22) — flattened over background
  highlight-blue: "#bcc7d2"    # was rgba(88,130,166,0.18) — flattened over background

  # Semantic
  success: "#6b8e4e"
  error: "#a0472c"

  # Inputs
  on-primary: "#1c1813"

typography:
  display-hero:
    fontFamily: "Source Serif 4, Charter, Georgia, Times New Roman, serif"
    fontSize: 58px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -1.16px
  h1:
    fontFamily: "Source Serif 4, Charter, Georgia, Times New Roman, serif"
    fontSize: 40px
    fontWeight: 600
    lineHeight: 1.15
    letterSpacing: -0.4px
  h2:
    fontFamily: "Source Serif 4, Charter, Georgia, Times New Roman, serif"
    fontSize: 28px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.28px
  h3:
    fontFamily: "Source Serif 4, Charter, Georgia, Times New Roman, serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.30
    letterSpacing: -0.22px
  pull-quote:
    fontFamily: "Source Serif 4, Charter, Georgia, Times New Roman, serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.45
    letterSpacing: -0.24px
  body-reading:
    fontFamily: "Source Serif 4, Charter, Georgia, Times New Roman, serif"
    fontSize: 19px
    fontWeight: 400
    lineHeight: 1.65
    letterSpacing: 0px
  body-compact:
    fontFamily: "Source Serif 4, Charter, Georgia, Times New Roman, serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.60
    letterSpacing: 0px
  highlight-text:
    fontFamily: "Source Serif 4, Charter, Georgia, Times New Roman, serif"
    fontSize: 17px
    fontWeight: 400
    lineHeight: 1.55
    letterSpacing: 0px
  ui-label:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, Segoe UI, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.40
    letterSpacing: 0.02em
  ui-button:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, Segoe UI, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.00
    letterSpacing: 0.01em
  caption:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, Segoe UI, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0.04em
  overline:
    fontFamily: "Inter, -apple-system, BlinkMacSystemFont, Segoe UI, system-ui, sans-serif"
    fontSize: 11px
    fontWeight: 600
    lineHeight: 1.20
    letterSpacing: 0.12em
  code:
    fontFamily: "iA Writer Mono, SF Mono, Menlo, ui-monospace, monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0px

spacing:
  micro: 2px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 20px
  2xl: 24px
  3xl: 32px
  4xl: 40px
  5xl: 64px
  6xl: 80px

rounded:
  none: 0px
  sm: 4px
  md: 6px
  lg: 8px
  xl: 10px

components:
  # Buttons
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.ui-button}"
    rounded: "{rounded.lg}"
    padding: 10px 20px
  button-primary-hover:
    backgroundColor: "{colors.primary-warm}"
    textColor: "{colors.on-primary}"
  button-ghost-serif:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.ui-button}"
    rounded: "{rounded.lg}"
    padding: 10px 20px
  button-ghost-serif-hover:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
  button-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.surface}"
    typography: "{typography.ui-button}"
    rounded: "{rounded.lg}"
    padding: 10px 20px

  # Cards
  card-reading:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xl}"
    padding: 24px
  card-highlight:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: 18px 20px 18px 22px
  card-elevated:
    backgroundColor: "{colors.surface-elevated}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xl}"
    padding: 24px

  # Inputs
  input:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.ui-button}"
    rounded: "{rounded.lg}"
    padding: 10px 14px
  input-focus:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"

  # Sidebar
  sidebar:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text-secondary}"
    typography: "{typography.ui-label}"
    padding: 16px
  sidebar-item:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text-secondary}"
    typography: "{typography.ui-label}"
    rounded: "{rounded.md}"
    padding: 8px 12px
  sidebar-item-active:
    backgroundColor: "{colors.surface-hover}"
    textColor: "{colors.ink}"

  # Highlights
  highlight-yellow-mark:
    backgroundColor: "{colors.highlight-yellow}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: 0px 2px
  highlight-blue-mark:
    backgroundColor: "{colors.highlight-blue}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: 0px 2px

  # Candle (dark) mode
  candle-canvas:
    backgroundColor: "{colors.candle-background}"
    textColor: "{colors.candle-text}"
    typography: "{typography.body-reading}"
    padding: 32px
  candle-card:
    backgroundColor: "{colors.candle-surface}"
    textColor: "{colors.candle-text}"
    rounded: "{rounded.lg}"
    padding: 24px

  # Status
  status-success:
    backgroundColor: "{colors.background}"
    textColor: "{colors.success}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: 4px 8px
  status-error:
    backgroundColor: "{colors.background}"
    textColor: "{colors.error}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: 4px 8px
---

# Readwise Design System

## Overview

Readwise Reader is what happens when a reading app is designed by people who actually love books. The interface rejects the cold, blue-tinted sterility of most read-later tools and opts instead for a warm cream canvas (`{colors.background}`) that feels less like a screen and more like the opened page of a hardback — a surface that acknowledges the eye has to spend hours here and responds with literal warmth. Every pixel is tuned for long-form ergonomics: comfortable measure, relaxed line-height, and a serif body that makes 5,000-word essays a pleasure rather than a chore.

The signature move is typographic allegiance to the serif. Where the industry default for productivity tools is a neutral sans (Inter, SF Pro, the usual suspects), Readwise commits to **Source Serif 4** — and later, Charter — for the reading surface itself. Headlines carry the gravitas of a book title; body copy has the cadence of an essay. The sans-serif (Inter) is demoted to UI chrome duty: sidebar labels, filter chips, button text. The hierarchy is unmistakable: **serif is for content, sans is for controls**. This small inversion is what makes Reader feel less like an app you tolerate and more like a reading room you inhabit.

What ties it together is a paper-like depth system that never tries to be glossy. Shadows are diffuse and amber-tinted, radii stay restrained between 6 and 10 pixels (anything more would feel app-y, anything less would feel chart-y), and the single saturated accent — a warm amber gold (`{colors.primary}`) — stands in for the physical highlighter marks a reader would leave on a real page. Quotes sit on pale cream cards with a thin left rule, as if torn from the margins of a book and taped into a commonplace book. The result is a visual language that says: this is not a feed, this is not a dashboard, this is a place you come to read.

**Key Characteristics:**
- Warm cream canvas (`{colors.background}`) evoking book paper — never pure white
- Source Serif 4 for display and body; Inter reserved for UI chrome
- Amber/gold accent (`{colors.primary}`) standing in for literal highlighter strokes
- Restrained 6–10px radii — readable, not toy-like
- Paper-shadow depth: diffuse, amber-tinted, low-opacity
- Highlight cards with left-rule indent — commonplace-book DNA
- Warm dark "candle" mode for evening reading — never cold black
- Reading-ergonomic measure (62–72ch) with generous 1.65 body line-height

## Colors

### Primary
- **Cream Paper** (`{colors.background}`): The canonical page surface. A warm off-white with yellow-green undertone that reads unmistakably as paper rather than screen.
- **Parchment** (`{colors.surface}`): One tone darker — used for sidebar panels, subtle section dividers, and elevated-from-below containers.
- **Ink Black** (`{colors.ink}`): Primary body and heading ink. Never pure black — always carries a faint brown undertone.

### Brand Accent
- **Amber Gold** (`{colors.primary}`): The signature accent — borrowed from highlighter pens and brass bookmark clasps. Used for primary CTAs, active states, the literal highlight marker, and the hairline rule on pull quotes.
- **Amber Warm** (`{colors.primary-warm}`): A lighter variant for hover states.
- **Terracotta** (`{colors.accent-terracotta}`): Secondary warm accent used sparingly for annotations, tags, and error-adjacent moments.

### Neutrals & Text
- **Ink Black** (`{colors.ink}`): Primary heading and body text on light surfaces.
- **Warm Graphite** (`{colors.text-secondary}`): Secondary text — subheads, key labels.
- **Warm Gray** (`{colors.text-tertiary}`): Tertiary text — metadata, timestamps, reading-time estimates.
- **Muted Stone** (`{colors.text-muted}`): Quaternary text — footnotes, disabled states, UI hints.
- **Ash** (`{colors.text-divider}`): Dividers, hairlines, faint borders between list items.

### Surface & Borders
- **Cream Paper** (`{colors.background}`): Canvas.
- **Parchment** (`{colors.surface}`): Elevated panels, sidebar, modal scrim.
- **Linen** (`{colors.surface-hover}`): Hover surface for list items.
- **Border Cream** (`{colors.border}`): Standard hairline border on cards and list dividers.
- **Border Warm** (`{colors.border-strong}`): Emphasized border for active cards and focused inputs.

### Dark Reader ("Candle" Mode)
- **Candle Dark** (`{colors.candle-background}`): Dark-reader canvas — warm near-black, the color of a lamplit room after dusk.
- **Candle Surface** (`{colors.candle-surface}`): Elevated panels on dark.
- **Candle Border** (`{colors.candle-border}`): Dark-mode hairlines.
- **Parchment Text** (`{colors.candle-text}`): Body text on dark — warm off-white, not stark.
- **Warm Silver** (`{colors.candle-text-secondary}`): Secondary dark-mode text.
- **Amber on Dark** (`{colors.candle-accent}`): Brand accent shifts to lighter amber on dark surfaces.

### Semantic
- **Highlight Yellow** (`{colors.highlight-yellow}`): The literal highlighter swipe on reading text.
- **Highlight Blue** (`{colors.highlight-blue}`): Secondary highlight color for shared notes.
- **Success Moss** (`{colors.success}`): Confirmed states — moss green rather than spring green.
- **Error Rust** (`{colors.error}`): Error states — rust rather than red.

### Gradient System
Gradients are nearly absent. The only gradient work happens in the hero atmosphere — a radial cream-to-parchment that mimics the faint vignette of book paper under a reading lamp. No tech-blue gradients, no neon, no animated shimmer.

## Typography

### Font Family
- **Reading & Display**: `Source Serif 4`, with fallbacks `Charter`, `Georgia`, `"Times New Roman"`, `serif`.
- **UI Chrome**: `Inter`, with fallbacks `-apple-system`, `BlinkMacSystemFont`, `"Segoe UI"`, `system-ui`, `sans-serif`.
- **Monospace**: `iA Writer Mono`, fallback `"SF Mono"`, `Menlo`, `ui-monospace`, `monospace`.

*Note: Source Serif 4 is Adobe's open-source transitional serif. Charter is a bundled system serif on macOS. Source Serif for display and rendered body, Charter as a performant fallback that matches the rhythm.*

### Hierarchy

The complete type scale lives in the `typography:` token block above. Reference tokens directly (`{typography.body-reading}`, `{typography.ui-label}`, etc.) rather than hardcoding values.

| Token | Use |
|---|---|
| `display-hero` | Landing hero — book-title presence |
| `h1` | Article opening headlines |
| `h2` | In-article section anchors |
| `h3` | Minor section marks, card titles |
| `pull-quote` | Block quotes — italic invocation |
| `body-reading` | Long-form reading — relaxed and generous |
| `body-compact` | Article previews, feed descriptions |
| `highlight-text` | Saved highlights, daily review |
| `ui-label` | Inter — sidebar items, filter chips |
| `ui-button` | Inter — button text, tabs |
| `caption` | Inter — metadata |
| `overline` | Inter — uppercase category labels |
| `code` | iA Writer Mono — inline code blocks |

### Principles
- **Serif carries the content, sans carries the controls**: Every piece of text the reader is meant to *read* uses Source Serif 4. Every piece of text the reader is meant to *operate* uses Inter.
- **No display-weight serif**: Headlines use weight 600, not 700. The serif letterforms have enough inherent weight.
- **Italic for emphasis, not oblique**: Source Serif 4's italic is a true italic, used for pull quotes, book titles within body copy, and foreign phrases.
- **Generous reading line-height (1.65)**: Body reading text breathes at 1.65 — well above the 1.4–1.5 typical of UI-centered designs. The single biggest lever for perceived reading comfort.
- **Letter-spacing tightens with size**: Display runs at -1.16px, body at zero, labels slightly positive.
- **Optical sizing**: Source Serif 4 supports optical size — use the `opsz` axis if available.

## Layout

### Spacing System
Base unit is **8px**. Card padding 24px internal. Reading column gap 32px between metadata, 20px between body paragraphs. Section spacing 64–80px between major sections.

### Grid & Container
- Reading measure: **62–72 characters per line** — the single most important layout constant
- Max reading container: 680px
- Dashboard max: 1200px, centered
- Sidebar: fixed 240–280px on desktop
- No 12-column grid insistence — reading-first layouts dominate

### Whitespace Philosophy
- **Reading-first**: Content containers have generous horizontal padding (32–48px on desktop) to prevent text from kissing the container edge.
- **Paragraph rhythm**: Body paragraphs separated by roughly one line-height worth of space.
- **Card quiet**: Cards carry 24px internal padding so highlights and metadata don't feel cramped.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat (Level 0) | No shadow, no border | Body copy on canvas, inline elements |
| Hairline (Level 1) | `1px solid {colors.border}` | Feed list rows, sidebar dividers |
| Contained (Level 2) | 1px border + warm paper-rest shadow | Standard cards |
| Elevated (Level 3) | Strong border + warm shadow-lift | Hover cards, modals |
| Floating (Level 4) | Layered warm shadow | Popovers, command palettes |

**Shadow Philosophy**: Depth is communicated through **warm amber-tinted shadows** (always derived from a deep brown-black) — never cool gray, never pure black. Shadows are diffuse and low-opacity — the sensation is of a page lightly lifted from the desk, not a UI card floating in 3D space.

### Decorative Depth
- **Vignette hero**: The hero section uses a radial cream-to-parchment gradient, mimicking lamp falloff.
- **Left-rule accent**: Highlight cards use a 3px solid Amber Gold left rule.
- **Alternation**: Sections alternate Cream Paper → Parchment → Candle Dark to create chapter-like rhythm.

## Shapes

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Hairline dividers |
| `sm` | 4px | Tags, inline badges, faint chips |
| `md` | 6px | Secondary buttons, small UI controls |
| `lg` | 8px | Primary buttons, inputs, standard cards |
| `xl` | 10px | Article cards, reading containers |

*No radius above 12px in the light UI* — reading apps should feel bookish, not toy-like.

## Components

The complete component spec lives in the `components:` token block above. Reference component tokens directly rather than reconstructing them.

### Buttons
- **`button-primary`** — Amber Gold bg, Ink Black text (high contrast, deliberately not white). Inter 14px weight 500. Hover: Amber Warm.
- **`button-ghost-serif`** — Transparent bg with cream border, Source Serif 4 italic text — yes, italic, because it reads like a book's "see also". Hover: Parchment background.
- **`button-dark`** — Ink Black bg, Parchment text. For inverted emphasis moments.

### Cards & Containers
- **`card-reading`** — Article preview card, cream background, 1px border, 10px radius, 24px padding.
- **`card-highlight`** — The signature component. Parchment bg, 3px Amber Gold left rule, italic Source Serif 4 quote text, source metadata in Inter below.
- **`card-elevated`** — Slightly lighter surface for focused reading views, modal content.

### Inputs & Forms
- **`input`** — Cream Paper bg, 1px Border Cream, 8px radius, Inter 14px text.
- **`input-focus`** — Amber Gold border with tinted ring.

### Sidebar
- **`sidebar`** — Parchment bg, Border Cream right border, Inter 13px weight 500 for items.
- **`sidebar-item-active`** — Linen background with Amber Gold left rule (3px).

### Highlights
- **`highlight-yellow-mark`** — The literal highlighter swipe on reading text.
- **`highlight-blue-mark`** — Secondary color for shared notes.

### Dark Candle Mode
- **`candle-canvas`** — Candle Dark bg with Parchment Text body in Source Serif 4 19px line-height 1.65.
- **`candle-card`** — Candle Surface elevated panels.

### Status
- **`status-success`** / **`status-error`** — Subtle moss/rust accents on canvas, never bright spring/red.

### Icons
- Icon set: **Solar Linear** and **Phosphor Regular** — both have book/reading-adjacent glyphs
- Default color: Warm Graphite (`{colors.text-secondary}`)
- Active / accent color: Amber Gold (`{colors.primary}`)
- Size: 18px standard, 22px in navigation, 14px inline

### Distinctive Components

**Daily Review Card** — Surfaces 5 saved highlights per day. Each highlight rendered as a Highlight Card, stacked with 16px gap. Header in Source Serif 4 20px.

**Reading Progress Bar** — Thin 2px Amber-Gold bar at the top of reading view, fills left-to-right as the reader scrolls.

**Feed List Item** — No background, no card — just a list row with hairline divider. Favicon left-aligned, title in Source Serif 4 18px weight 600, excerpt in Source Serif 4 15px weight 400 Warm Graphite, metadata in Inter 12px Warm Gray.

## Do's and Don'ts

### Do
- Use Cream Paper (`{colors.background}`) as the canonical canvas — warmth is the brand
- Use Source Serif 4 for any text the reader is meant to *read*; use Inter for controls
- Use Amber Gold (`{colors.primary}`) sparingly — as a highlight marker, a CTA, an active-state rule
- Keep body line-height at 1.65 — this is the single biggest reading-comfort lever
- Use warm amber-tinted shadows — never cold black
- Keep radii between 6 and 10 px — readable, not rounded-to-death
- Use italic (not bold) for in-body emphasis — the serif has a true italic
- Offer a warm Candle dark mode (`{colors.candle-background}`) — never pure black
- Use the Highlight Card pattern (left-rule, italic quote, source below) for all saved quotes
- Respect a 62–72ch measure in reading views

### Don't
- Don't use pure white (`#ffffff`) as a canvas — Cream Paper always
- Don't use a sans-serif for body reading text — Reader's identity is serif-led
- Don't use blue or purple accents — the palette is warm earth only
- Don't push headlines past weight 600 — the serifs carry themselves
- Don't use drop shadows larger than 32px blur — this is a reading app, not a glassmorphism demo
- Don't use pill-shaped elements in the reading UI — too app-y
- Don't introduce any cool-gray neutrals — every gray carries a warm undertone
- Don't underline body links by default — use Amber Gold color + hover underline instead
- Don't animate scroll progress or page turns — Reader respects stillness
- Don't put UI chrome (buttons, inputs) in a serif — that's the sans's job

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|---|---|---|
| Mobile | <640px | Single column, sidebar collapses to drawer, body reading at 17px |
| Tablet | 640–1024px | Sidebar persists as icon rail, reading column 600px max |
| Desktop | 1024–1440px | Full sidebar 240px, reading column 680px, dashboard grids enable |
| Wide | 1440px+ | Optional third column for highlights/notes alongside reading view |

### Touch Targets
- Minimum 40x40px for all interactive elements
- List rows in feed have generous 12px vertical padding — easy thumb targeting
- Highlight gesture: long-press on mobile, drag-select on desktop

### Collapsing Strategy
- **Sidebar**: persistent panel → icon rail → drawer (hamburger) as width decreases
- **Reading column**: 680px → 600px → 100% (with 20px horizontal padding)
- **Hero**: 58px → 40px → 32px display headline scaling
- **Highlight cards**: grid on wide views → single column on tablet/mobile

### Image Behavior
- Inline article images: 10px radius, max-width 100% of reading column
- Hero images: full-bleed within container, with 10px radius
- No art-direction changes — aspect ratios preserved across breakpoints

## Agent Prompt Guide

### Quick Color Reference
- Canvas: Cream Paper (`{colors.background}`)
- Panel: Parchment (`{colors.surface}`)
- Hover: Linen (`{colors.surface-hover}`)
- Primary text: Ink Black (`{colors.ink}`)
- Secondary text: Warm Graphite (`{colors.text-secondary}`)
- Tertiary text: Warm Gray (`{colors.text-tertiary}`)
- Accent: Amber Gold (`{colors.primary}`)
- Border: Border Cream (`{colors.border}`)
- Dark canvas: Candle Dark (`{colors.candle-background}`)
- Dark panel: Candle Surface (`{colors.candle-surface}`)

### Example Component Prompts
- "Build a reading hero on Cream Paper (`{colors.background}`) with a headline at 58px Source Serif 4 weight 600, line-height 1.15. Body subtitle in Source Serif 4 at 19px weight 400 line-height 1.65, color Warm Graphite (`{colors.text-secondary}`). Primary CTA: Amber Gold (`{colors.primary}`) background, Ink Black text, 8px radius, Inter 14px weight 500."
- "Design a highlight card on Parchment (`{colors.surface}`) with a 3px solid Amber Gold left rule. Quote text in Source Serif 4 italic 17px Ink Black. Source domain and date below in Inter 12px Warm Gray. Radius 8px (0 on the left rule side), 18px padding."
- "Create an article feed row: no card background, 16px vertical padding, hairline divider Border Cream (`{colors.border}`). Favicon left, title in Source Serif 4 18px weight 600 Ink Black, excerpt in Source Serif 4 15px weight 400 Warm Graphite, metadata in Inter 12px Warm Gray."
- "Build a dark 'Candle' reading view on Candle Dark (`{colors.candle-background}`) with Parchment Text (`{colors.candle-text}`) body in Source Serif 4 19px line-height 1.65. Headings in Source Serif 4 weight 600. Amber on Dark (`{colors.candle-accent}`) for the highlight accent."
- "Design a sidebar nav item — 13px Inter weight 500, Warm Graphite text, 8px 12px padding, Linen background on hover, 3px Amber Gold left rule when active."

### Iteration Guide
1. Lead with the serif — every reading surface starts from Source Serif 4
2. Reserve Inter for anything a user clicks, selects, or configures
3. Always specify Cream Paper (`{colors.background}`) as canvas — never white
4. Use Amber Gold (`{colors.primary}`) as a garnish, not a surface — primary CTA, active state, left rules
5. Shadows use warm ink, never pure black
6. Radii stay between 6 and 10px — anything more feels consumery
7. Body reading text always at 1.65 line-height — non-negotiable
8. Italic (not bold) for emphasis within body copy
9. For dark mode, use Candle Dark (`{colors.candle-background}`), never pure black
10. Respect the 62–72ch reading measure — wider is not better
