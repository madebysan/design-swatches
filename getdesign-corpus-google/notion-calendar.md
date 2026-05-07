---
version: alpha
name: "Notion Calendar"
description: "Token-first design system reference for Notion Calendar."

colors:
  background: "#ffffff"
  surface: "#2383e2"
  surface-elevated: "#f5f5f5"
  ink: "#000000"
  ink-muted: "#fdecc8"
  primary: "#ffffff"
  on-primary: "#ffffff"
  border: "#d3e5ef"
  focus-ring: "#ffffff"
  success: "#22c55e"
  warning: "#f59e0b"
  error: "#ef4444"
  shadow-soft: "#d9d9d9"

typography:
  display-hero:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 64px
    fontWeight: 600
    lineHeight: 1.05
    letterSpacing: -1px
  display:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: -0.5px
  heading-section:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 32px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.25px
  heading-sub:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0px
  body-large:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  body:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  button-ui:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: 0px
  caption:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 14px
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

# Notion Calendar Design System

## Overview

Notion Calendar (formerly Cron) is the rare productivity product that designs against the productivity-app aesthetic. Where Google Calendar leans on blue chrome and Apple Calendar leans on system materials, Notion Calendar treats its surface like a sheet of paper — generous warm white, hairline rules, monospaced metadata, and a single confident sans-serif doing almost all the typographic work. The marketing site at `notion.com/product/calendar` mirrors that ethos: a centered hero on near-white canvas (`#ffffff`), a quietly personal headline ("It's time."), and product screenshots that double as the visual identity. There are no illustrations carrying weight — the calendar UI itself is the hero illustration, and the page is built to frame it cleanly.

The defining quality is **density without noise**. The calendar week-view mockups pack seven columns, half-hour rows, multi-day events, and a left rail of accounts and filters into a layout that still reads as calm. This is achieved by a strict three-color event palette (sky blue, pale yellow, lavender purple) at low saturation, hairline `1px` dividers in cool gray (`rgb(232, 232, 231)`), and a complete absence of fills or shadows on the canvas itself. Every piece of UI chrome is held by a single-pixel rule or a 4–6px radius — never by elevation. This is a calendar that trusts the reader to find structure in the grid.

The third signature is its **keyboard-first restraint**. The product is famous for its command bar (`⌘K`) and shortcut overlay, and the marketing reflects that: small monospace tags appear near features like `⌘K`, `⌥`, `→`, signaling that the real interface is the keyboard. Body type runs in a humanist sans (Notion's GT Walsheim-derived stack), but UI metadata — timestamps, time zones, shortcut hints — flips into a mono. That mono/sans pairing is the most copyable signal of the brand outside the calendar grid itself.

**Key Characteristics:**
- Pure white canvas (`#ffffff`) — paper-like, no warm tint, no off-white softening
- Single saturated accent: Notion Blue (`#2383e2`) for primary CTAs and "now" indicators
- Three-color event palette: sky blue (`#d3e5ef`), butter yellow (`#fdecc8`), lavender (`#e8deee`)
- Hairline `1px solid rgb(232, 232, 231)` dividers do all the structural work — no shadows
- Sans + mono pairing — humanist sans for prose, mono for shortcuts/timestamps/UI metadata
- 4–6px corner radius on cards and event blocks — soft but not playful
- Centered hero composition, product screenshots float alone without device chrome decoration
- Dense schedule grid as the brand's primary hero asset
- Subtle decorative emoji/icon flourishes (`✏️`, `🚲`, `📖`) drift in margins as personality cues

## Colors

### Primary
- **Notion Blue** (`#2383e2`): The single primary accent. CTA buttons ("Get Notion Calendar free"), today indicator, time-now line, primary links. The only saturated chromatic in the system.
- **Notion Black** (`#191918`): Primary text — headlines, body, event titles, navigation. Slightly warm off-black, not pure `#000`.
- **Pure White** (`#ffffff`): Page canvas, card surfaces, hero background. White is the workhorse.

### Secondary Text & Neutrals
- **Mid Ink** (`#31302e`): Body text on light surfaces, where `#191918` would be too heavy at small sizes.
- **Cool Gray** (`#787774`): Secondary metadata — timestamps, account labels, helper copy, "by Notion" footer notes.
- **Quiet Gray** (`rgba(0, 0, 0, 0.95)`): Default link color before hover — appears black but flips to Notion Blue on hover.

### Surface & Borders
- **Canvas White** (`#ffffff`): Page background and card fills.
- **Hairline Gray** (`rgb(232, 232, 231)`): The signature `1px` divider — between calendar rows, between sidebar items, around event cards. Does the heavy lifting that other systems give to shadows.
- **Hover Surface** (`#f6f5f4`): Subtle warm-gray hover state for nav items, sidebar rows, and command-bar entries. Two ticks warmer than the canvas.
- **Section Divider** (`#f6f5f4` 2px): Used as a section break on the marketing page.

### Event Color Palette
Notion Calendar's event chips use a tinted-fill + matching-text pattern — pastel background, saturated text in the same hue.
- **Event Sky** fill (`#d3e5ef`) / text (`#183347`)
- **Event Butter** fill (`#fdecc8`) / text (`#64473a`)
- **Event Lavender** fill (`#e8deee`) / text (`#492f64`)
- **Event Sage** fill (`#dbeddb`) / text (`#1c3829`)
- **Event Blush** fill (`#ffe2dd`) / text (`#5d1715`)
- **Event Stone** fill (`#e3e2e0`) / text (`#32302c`)

Each event color is paired so text-on-fill contrast clears WCAG AA at 4.5:1. The whole palette runs at low saturation so a dense week view never visually fights itself.

### Status & Functional
- **Now Line** (`#eb5757`): The horizontal "current time" line in day/week view — soft red, never pure red.
- **Link Blue** (`#0075de`): Inline text links inside content — slightly more saturated than Notion Blue for legibility in body copy.
- **Focus Ring** (`rgba(35, 131, 226, 0.25)`): 2px focus ring on inputs and command-bar entries.

### Gradient System
Notion Calendar is **gradient-free**. Every fill is a flat color. The closest thing to a gradient is the soft fade of the inverted hover row in the command palette — and that's just `#f6f5f4` flat.

## Typography

### Font Family
- **Primary Sans**: `"GT Walsheim"`, `Inter`, `-apple-system`, `BlinkMacSystemFont`, `"Segoe UI"`, `sans-serif`
- **Monospace**: `"iA Writer Mono"`, `"SF Mono"`, `Menlo`, `Consolas`, `monospace` — used for shortcut tags (`⌘K`), timestamps in dense UI, time zone labels
- **OpenType Features**: Tabular numerals (`tnum`) on every clock-style number so columns align across the calendar grid

*Note: Notion uses a custom GT Walsheim variant. For external implementations, Inter at weight 400/500/600 is the closest free substitute. Söhne, Aeonik, or Söhne Breit also work as licensed alternatives.*

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Display Hero | Sans | 64px (4.00rem) | 600 | 1.05 | -0.02em | Marketing hero — "It's time." |
| Display | Sans | 48px (3.00rem) | 600 | 1.10 | -0.02em | Section headlines — "Time management, simplified." |
| Heading 1 | Sans | 32px (2.00rem) | 600 | 1.15 | -0.01em | Feature group titles |
| Heading 2 | Sans | 24px (1.50rem) | 600 | 1.25 | -0.01em | Feature card titles |
| Heading 3 | Sans | 18px (1.13rem) | 600 | 1.30 | normal | Sidebar labels, sub-feature heads |
| Body Large | Sans | 18px (1.13rem) | 400 | 1.50 | normal | Hero subhead and intro paragraphs |
| Body | Sans | 16px (1.00rem) | 400 | 1.55 | normal | Standard paragraph text |
| Body Small | Sans | 14px (0.88rem) | 400 | 1.45 | normal | Helper text, FAQ answers |
| UI Label | Sans | 13px (0.81rem) | 500 | 1.30 | normal | Nav links, sidebar headers, button labels |
| Event Title | Sans | 12px (0.75rem) | 500 | 1.20 | -0.005em | Event chip text in calendar grid |
| Caption | Sans | 12px (0.75rem) | 400 | 1.40 | normal | Timestamps, secondary metadata |
| Mono Tag | Mono | 12px (0.75rem) | 400 | 1.00 | normal | Shortcut keys (`⌘K`), time zone codes |
| Mono Mini | Mono | 11px (0.69rem) | 400 | 1.00 | normal | Timestamps in dense schedule rows |

### Principles
- **Sans for content, mono for chrome**: Prose, headings, and event titles are sans. Anything that represents a key, code, or precise time slips into mono. The contrast is the brand.
- **Weight 600 is the heading ceiling**: Notion never goes 700/bold for display type. The weight stops at 600, keeping headlines confident but not loud.
- **Tight display tracking**: `-0.02em` to `-0.01em` on display sizes; body and UI run at normal tracking. Never positive (loose) tracking — Notion Calendar isn't an editorial brand.
- **Tabular numerals everywhere**: Every clock readout, time zone offset, and date stamp uses tabular figures so dense schedule columns lock into the grid.
- **Generous body line-height**: Body text at 1.50–1.55 — calm, readable, scannable in long FAQ sections.

## Layout

### Spacing System
- Base unit: 4px
- Scale: 4px, 6.5px, 8px, 12px, 16px, 24px, 32px, 48px, 64px, 96px, 128px
- Notable: dembrandt picked up `6.5px` as a recurring half-unit — used for tight chrome inside the calendar grid (event chip vertical padding, sidebar row gaps).

### Grid & Container
- Marketing page max-width: 1080px centered, with 24px gutters on tablet and 16px on mobile
- Hero section: vertically centered, narrow text column (~640px) above a wider product screenshot (~960px)
- Feature sections: alternating 2-column (text + screenshot) and full-width centered
- Product mockups: float on canvas with subtle drop shadow, no device chrome unless mobile
- Breakpoints stack: 1600px → 1440px → 1280px → 1200px → 1080px → 942px → 840px → 712px → 600px → 480px → 400px → 375px

### Whitespace Philosophy
- **Calm pacing**: 96–128px of vertical space between major marketing sections. The page never feels rushed.
- **Tight inside chrome**: Inside the calendar UI itself, padding contracts to 4–8px to fit dense schedule data. The site rhythm and the product rhythm are deliberately different.
- **Centered axis**: The marketing hero sits dead-center horizontally, with marginalia stickers offsetting any feeling of academic stiffness.

### Border Radius Scale
- `4px`: Event chips, mono shortcut tags, small toolbar buttons
- `6px`: Buttons, inputs, sidebar cards
- `8px`: Feature cards, dropdowns, popovers
- `12px`: Large product mockups, command palette overlay
- No fully-pill (`9999px`) elements anywhere — Notion Calendar avoids the round-button productivity-app cliche

## Elevation & Depth

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | No shadow, no border | Page canvas, body text, calendar grid background |
| Hairline (Level 1) | `1px solid rgb(232, 232, 231)` | Cards, sidebar dividers, calendar grid lines, top nav border |
| Whisper Shadow (Level 2) | `rgba(0, 0, 0, 0.04) 0px 1px 2px` | Primary buttons, active toolbar items |
| Lift Shadow (Level 3) | `rgba(0,0,0,0.01) 0px 0.175px 1.041px, rgba(0,0,0,0.02) 0px 0.8px 2.925px, rgba(0,0,0,0.027) 0px 2.025px 7.847px, rgba(0,0,0,0.04) 0px 4px 18px` | Product screenshots in marketing, dropdowns, popovers |
| Overlay Shadow (Level 4) | `rgba(0, 0, 0, 0.08) 0px 8px 24px` | Command palette, modals, multi-step picker overlays |

**Shadow Philosophy**: Notion Calendar treats elevation as a last resort. Hairline borders separate 95% of components — shadows only enter when an element genuinely needs to float (a popover, a command palette, a marketing screenshot lifting off the page). The shadow stack at level 3 is famously layered (4 distinct stops at decreasing opacity) which produces a smooth, paper-on-paper softness rather than a sharp drop. There are no inner shadows, no glows, and no inset effects anywhere in the system.

### Decorative Depth
- Multi-stop layered shadows replace single-blur drop shadows for any "lift" moment
- Hairline borders never combine with shadows — an element gets one or the other, never both, except at modal/overlay levels
- The today-column tint (`#f6f5f4`) functions as ambient depth without using a shadow at all

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

**Primary Blue**
- Background: Notion Blue (`#2383e2`)
- Text: Pure White (`#ffffff`)
- Padding: `10px 16px` (compact), `12px 20px` (standard)
- Radius: `6px`
- Font: 14px sans weight 500
- Shadow: `rgba(0, 0, 0, 0.04) 0px 1px 2px` — barely-there
- Hover: background darkens to `#0b6cca`
- Use: Primary CTA — "Get Notion Calendar free", "Download for Mac"

**Black Inverted**
- Background: Notion Black (`#191918`)
- Text: Pure White (`#ffffff`)
- Padding: `10px 16px`
- Radius: `6px`
- Font: 14px sans weight 500
- Hover: background lightens to `#31302e`
- Use: Top-nav CTA on the marketing site — "Get Notion Calendar free"

**Ghost / Tertiary**
- Background: transparent
- Text: Notion Black (`#191918`)
- Padding: `8px 12px`
- Radius: `6px`
- Hover: background fills with `#f6f5f4`
- Use: Secondary nav links, inline actions, "Log in"

**Icon Button**
- Size: 28px × 28px
- Background: transparent default, `#f6f5f4` on hover
- Radius: `4px`
- Use: Toolbar buttons inside the calendar UI — view switcher, search, settings

### Cards & Containers
- Background: `#ffffff`
- Border: `1px solid rgb(232, 232, 231)` — the signature hairline
- Radius: `6px` (small cards), `8px` (feature cards), `12px` (large product mockups)
- Shadow: optional soft `rgba(0, 0, 0, 0.04) 0px 0.175px 1.041px, rgba(0, 0, 0, 0.04) 0px 4px 18px` — only on screenshots that need to lift off the canvas
- Internal padding: 16–24px standard, 32–48px for marketing feature cards

### Event Chips (the signature component)
- Height: 22–24px for compact, 44–60px for half-hour blocks, multi-row for longer events
- Background: tinted fill from event palette (e.g., `#d3e5ef`)
- Text: matching saturated text color (e.g., `#183347`)
- Radius: `4px`
- Padding: `2px 6px`
- Border: none — fill alone separates events
- Left edge: optional `2px` solid bar in saturated text color for "category" emphasis
- Font: 12px sans weight 500, single-line truncation with ellipsis

### Calendar Grid
- Day column width: equal `1fr` distribution, minimum 96px
- Hour row height: 48px per hour (24px per half-hour)
- Grid lines: `1px solid rgb(232, 232, 231)` between rows, slightly stronger `rgb(220, 220, 219)` between days
- Today column: subtle `#f6f5f4` background tint, full-height
- Now line: `1px solid #eb5757` horizontal across all day columns, with a 6px filled circle at the left edge of "today"
- Header row (day names + dates): sticky top, white background, hairline bottom border, day name in 11px mono uppercase, date in 18px sans weight 500

### Sidebar (Calendar List)
- Width: 240px fixed on desktop
- Background: `#ffffff` with `1px solid rgb(232, 232, 231)` right edge
- Section header: 11px mono uppercase, color `#787774`, padding `12px 16px 6px`
- Calendar item: 32px row height, 12px square color swatch on left, 13px sans label, hover `#f6f5f4`
- Account groups: collapsible with rotating chevron, no animation flourish

### Command Bar (`⌘K`)
- Container: centered overlay, max-width 640px, `12px` radius, `rgba(0, 0, 0, 0.04) 0px 4px 18px` shadow
- Background: `#ffffff`
- Input: 16px sans, no border, full-width, padding `16px 20px`
- Result row: 40px height, `12px 16px` padding, hover/selected fill `#f6f5f4`
- Result icon: 16px monochrome glyph in `#787774`
- Result text: 14px sans `#191918` for primary, 12px mono `#787774` for shortcut on the right
- Divider between sections: `1px solid rgb(232, 232, 231)`

### Inputs & Forms
- Background: `#ffffff`
- Border: `1px solid rgb(232, 232, 231)`
- Radius: `6px`
- Font: 14px sans weight 400, color `#191918`
- Padding: `8px 12px`
- Focus: border shifts to `#2383e2`, plus `0 0 0 2px rgba(35, 131, 226, 0.25)` ring
- Placeholder: `#787774`

### Navigation
- Top bar: 56px tall, white background, `1px solid rgb(232, 232, 231)` bottom border
- Logo: Notion mark on the left, 24px square
- Nav links: 13px sans weight 500, color `#191918`, underline on hover
- Right cluster: "Log in" ghost + "Get Notion Calendar free" black inverted CTA
- Dropdowns: `8px` radius, `rgba(0, 0, 0, 0.08) 0px 8px 24px` shadow, hairline border, 16px internal padding

### Decorative Elements

**Marginalia Stickers**
- Small emoji or hand-drawn icons (✏️, 🚲, 📖, 💌) drift in the marketing margins
- Sized 28–48px, never anchored to a grid — they feel scattered, like a planner's stickers
- Used to add personality to an otherwise austere page without breaking the productivity-tool tone

**Mono Shortcut Tag**
- Background: `#f6f5f4`
- Text: 12px mono `#31302e`
- Padding: `2px 6px`
- Radius: `4px`
- Use: Inline keyboard shortcut indicators (`⌘K`, `⌥+drag`, `→`)

## Do's and Don'ts

### Do
- Use pure white (`#ffffff`) for the canvas — no off-white softening
- Hold structure with `1px solid rgb(232, 232, 231)` hairlines, not shadows
- Pair humanist sans with a clean mono — mono carries shortcuts, timestamps, and time zone codes
- Reserve Notion Blue (`#2383e2`) for primary CTAs and the now-line; one or two uses per screen
- Pick from the six-color event palette — pastel fill + saturated matching text
- Use `6–8px` radius for cards and buttons; `4px` for tight chrome; `12px` for overlays
- Keep heading weight at 600 maximum — never 700/bold for display
- Apply tabular numerals to every clock and date readout
- Layer multi-stop shadows for screenshots and overlays — never a single sharp blur
- Let the product UI itself be the marketing illustration — minimal extra art

### Don't
- Don't use off-white or warm canvas tints — Notion Calendar is paper-white
- Don't use bold (700+) on display headings — 600 is the ceiling
- Don't use single-stop shadows for elevation — use the layered 4-stop stack
- Don't mix shadow + hairline border on the same component (except modals)
- Don't introduce a second saturated accent — Notion Blue is the only chromatic CTA color
- Don't use pill-shape buttons — radius caps at 12px
- Don't saturate event colors above the published palette — they will fight in dense weeks
- Don't use serif fonts anywhere — Notion Calendar is sans + mono only
- Don't add gradients — every fill is flat
- Don't add device chrome to product mockups — float them clean

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile Small | <375px | Single-column, hero drops to 36px, stacked CTA |
| Mobile | 375–600px | Single-column, 40–48px hero, calendar mockup becomes phone-frame |
| Tablet | 600–942px | 2-column starts, 48–56px hero, sidebar collapses to icon rail |
| Desktop | 942–1280px | Full 3-zone calendar (sidebar + main + agenda), 56–64px hero |
| Large Desktop | ≥1280px | Maximum scale (64px hero), 1080px content max-width holds |

### Touch Targets
- Primary CTAs: min 44px tap height on mobile, 12px vertical padding
- Calendar event chips: bumped to 32px tap target on touch (vs 22px on desktop)
- Sidebar rows: 40px tap height on mobile (vs 32px desktop)
- Icon buttons: 36px on touch, 28px on desktop

### Collapsing Strategy
- **Top nav**: Full link bar collapses to hamburger below 942px
- **Hero**: Stacks vertically below 942px; product screenshot moves below text
- **Calendar UI mockups**: Desktop screenshot crossfades to mobile phone frame below 600px
- **Feature grid**: 3-column → 2-column → 1-column at 942px and 600px
- **FAQ section**: Stays single-column at all breakpoints; max-width 720px

### Image Behavior
- Product screenshots scale proportionally with `max-width: 100%`
- Layered 4-stop shadow simplifies to a single softer shadow on mobile to save paint cost
- Marginalia stickers reposition to corners on mobile rather than scattering through margins
- No art-direction swaps for the calendar UI itself — same screenshot scales

---

## Agent Prompt Guide

### Quick Color Reference
- Primary CTA: Notion Blue (`#2383e2`)
- Page Background: Pure White (`#ffffff`)
- Primary Text: Notion Black (`#191918`)
- Secondary Text: Cool Gray (`#787774`)
- Hairline Border: `rgb(232, 232, 231)`
- Hover Surface: `#f6f5f4`
- Now Line: `#eb5757`
- Event Sky: fill `#d3e5ef` / text `#183347`
- Event Butter: fill `#fdecc8` / text `#64473a`
- Event Lavender: fill `#e8deee` / text `#492f64`
- Event Sage: fill `#dbeddb` / text `#1c3829`
- Event Blush: fill `#ffe2dd` / text `#5d1715`
- Layered Shadow: `rgba(0,0,0,0.01) 0px 0.175px 1.041px, rgba(0,0,0,0.02) 0px 0.8px 2.925px, rgba(0,0,0,0.027) 0px 2.025px 7.847px, rgba(0,0,0,0.04) 0px 4px 18px`

### Example Component Prompts
- "Build a calendar week view on `#ffffff` with seven equal-width day columns separated by `1px solid rgb(232, 232, 231)` dividers, 48px hour rows. Today column gets a subtle `#f6f5f4` background tint. Add a `1px solid #eb5757` horizontal now-line. Day headers in 11px mono uppercase color `#787774`, date numbers in 18px sans weight 500."
- "Design an event chip — 22px tall, `4px` radius, fill `#d3e5ef`, text color `#183347`, 12px sans weight 500, padding `2px 6px`, single-line truncate with ellipsis."
- "Create a command palette overlay — centered, max-width 640px, `12px` radius, white background, layered 4-stop shadow. Input 16px sans no border, padding `16px 20px`. Result rows 40px tall with hover fill `#f6f5f4`, label in 14px sans `#191918`, shortcut tag on the right in 12px mono inside a `#f6f5f4` chip with `4px` radius."
- "Build a primary CTA button — Notion Blue (`#2383e2`) background, white text, 14px sans weight 500, padding `12px 20px`, `6px` radius, whisper shadow `rgba(0, 0, 0, 0.04) 0px 1px 2px`. Hover darkens to `#0b6cca`."
- "Design a sidebar account list — 240px wide, white background with `1px solid rgb(232, 232, 231)` right edge. Section headers in 11px mono uppercase `#787774`. Each calendar row 32px tall, 12px square color swatch left of a 13px sans label, hover row fills with `#f6f5f4`."
- "Create a marketing hero section centered on white with the headline 'It's time.' at 64px sans weight 600 line-height 1.05 letter-spacing -0.02em. Subhead at 18px sans weight 400 in `#31302e`. Primary CTA below, then a product screenshot floating with the layered 4-stop shadow."

### Iteration Guide
1. Default to pure white (`#ffffff`) — never off-white. The canvas is paper.
2. Hold structure with `1px` hairlines in `rgb(232, 232, 231)`, not shadows.
3. Heading weight stops at 600 — never go bolder for display type.
4. Notion Blue (`#2383e2`) is the only saturated chromatic — preserve its scarcity.
5. Pair sans for content, mono for chrome (shortcuts, timestamps, time zones).
6. Use the six-color event palette as published — fill + matching saturated text. Don't recolor.
7. Apply tabular numerals to every clock and date readout so columns align.
8. Layered 4-stop shadow for screenshots and overlays — never a single blurred drop.
9. Radius scale tops out at 12px — no pills, no fully-rounded buttons.
10. Let the calendar UI itself be the visual interest — keep marketing chrome quiet.
