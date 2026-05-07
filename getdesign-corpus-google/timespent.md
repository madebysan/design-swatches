---
version: alpha
name: "Timespent"
description: "Token-first design system reference for Timespent."

colors:
  background: "#ffffff"
  surface: "#ffd600"
  surface-elevated: "#f5f5f5"
  ink: "#111111"
  ink-muted: "#e84545"
  primary: "#1f1f1f"
  on-primary: "#ffffff"
  border: "#fcfcfc"
  focus-ring: "#1f1f1f"
  success: "#22c55e"
  warning: "#f59e0b"
  error: "#ef4444"
  shadow-soft: "#d9d9d9"

typography:
  display-hero:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 80px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -1px
  display:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 56px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  heading-section:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 28px
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
    fontSize: 26px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  body:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  button-ui:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 24px
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

# Timespent Design System

## Overview

Timespent's marketing site is the rare indie-iOS-app landing page that doesn't lean on glassmorphism, gradients, or App Store boilerplate. It's an off-white canvas (`hsl(0 0% 99%)`), near-black ink (`#1f1f1f`), and one screaming yellow highlighter (`#ffd600`) used as a literal `<mark>` tag on the words that matter, "be **the best** you can be", "your questions, **answered**". The effect is a freshly-printed product manual that someone went through with a Sharpie. Confident, opinionated, slightly handmade.

The defining typeface is **Bricolage Grotesque** at weight 700, scaled up to 80px for the hero. Bricolage is a parametric variable font with deliberate quirks, slightly chunky, slightly geometric, with a softness in the curves that keeps it from reading as corporate. Where most habit-tracker apps default to SF or Inter, Timespent picks a typeface with personality and runs it bold across every section heading. Body copy drops to system-font (`-apple-system`) for legibility, but the brand voice is carried entirely by Bricolage at 700.

What sets Timespent apart is the **product-card system**: each iPhone screenshot is wrapped in a saturated-color frame (poppy red, citrus orange, teal, mint, navy) with `24px` radius, a 1px hairline border in `#1f1f1f`, and a soft layered drop shadow. The cards feel sticker-like, flat color blocks with a thin black outline that locks them into the page. Combined with App Store credibility laurels ("Editors' Choice — Apps We Love / Best New Apps") under the CTA and a pill-shaped black CTA button, the whole page reads as a competent, slightly nerdy software builder showing off what they made.

**Key Characteristics:**
- Bricolage Grotesque weight 700 for every display heading
- Off-white canvas (`#fcfcfc`) with near-black text (`#1f1f1f`)
- Yellow highlighter (`#ffd600`) applied as `<mark>` on emphasized words only
- Saturated-color iPhone card frames (red, orange, teal, mint, navy) with `24px` radius and 1px black outline
- Pill buttons (`999px` radius) throughout — black-filled primary, outlined ghost
- Layered soft drop shadows (`0 2px 8px` + `0 1px 3px`) for sticker-card depth
- SF Mono uppercase 10–12px for credibility chrome (laurels, version strings)
- System font (`-apple-system`) for body copy keeps reading text invisible

## Colors

### Primary
- **Timespent Ink** (`#1f1f1f`): Primary text, headings, body, button backgrounds, borders. Not pure black — softened to a warm-leaning very dark gray so it reads as intentional, not generic.
- **Off-White Canvas** (`#fcfcfc` / `hsl(0 0% 99%)`): Page background. Just barely off pure white — keeps the page from feeling sterile.
- **Pure White** (`#ffffff`): Reserved for button text on dark, and the iPhone screen mockups themselves.

### Brand Accent
- **Highlighter Yellow** (`#ffd600`): The signature accent — applied as a `<mark>` tag behind specific phrases ("the best", "answered"). The only saturated brand color used decoratively. Reads as literal Sharpie or felt-tip highlight, not as a color block.

### Card Frame Palette
The product cards each use a different saturated background, chosen to maximize against the iPhone screenshot inside. Curated set, not a random palette:
- **Poppy Red** (`~#e84545`): "Better Habits" — energetic, urgent
- **Citrus Orange** (`~#ff7a3d`): "Harder Workouts" — high-effort, kinetic
- **Pine Teal** (`~#2d5a4f`): "Focus & Study Time" — deep, contemplative
- **Mint Green** (`~#a8d896`): "Rx & Supplements" — clinical, healthy
- **Navy Black** (`~#1a1a2e`): Testimonial — gravitas, premium

### Neutrals & Text
- **Ink** (`#1f1f1f`): Headings, body, button fills, hairline borders
- **Link Black** (`#111111`): Slightly deeper black for inline links
- **Border Hairline** (`#eeeeee`): Subtle dividers, secondary borders
- **Caption Gray** (`#666–#999`): Footer copy, metadata, legal

### Shadow Palette
- **Sticker Shadow** (`rgba(17, 17, 17, 0.11)`): Primary drop-shadow at `0px 2px 8px`
- **Sticker Shadow Soft** (`rgba(17, 17, 17, 0.08)`): Inner-layer at `0px 1px 3px`
- **Sticker Shadow Strong** (`rgba(17, 17, 17, 0.14)`): Floating cards at `0px 8px 8px`

### Gradient System
Timespent is **gradient-free**. Every surface is a flat color. The system relies on saturated card frames, hairline borders, and layered soft shadows for depth, no gradient fills, no glow, no glassmorphism.

## Typography

### Font Family
- **Display & Headings**: `Bricolage Grotesque` (Google Fonts variable font, weights 200–800)
- **Body & UI**: `-apple-system, system-ui, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, "Fira Sans", "Droid Sans", "Helvetica Neue", sans-serif`
- **Monospace / Chrome**: `"SF Mono", -apple-system-ui-monospace, ui-monospace`
- **OpenType Features**: Variable axis usage on Bricolage — weight scales fluidly from 400 to 700. No stylistic alternates beyond the default.

*Note: Bricolage Grotesque is a free Google Font designed by Mathieu Triay — described by its designer as "non-conformist," with optical sizing and a parametric width axis. Fall-back substitutes: Söhne, Inter, or Geist if Bricolage is unavailable.*

### Hierarchy

| Role | Font | Size | Weight | Line Height | Notes |
|------|------|------|--------|-------------|-------|
| Display Hero | Bricolage Grotesque | 80px (5.00rem) | 700 | 1.10 | Primary hero — "Focus. Flourish. Go timespent." |
| Display Large | Bricolage Grotesque | 56px (3.50rem) | 700 | 1.10 | Section openers — "To be the best you can be." |
| Display | Bricolage Grotesque | 48px (3.00rem) | 700 | 1.10 | Sub-section heads, FAQ openers |
| Sub-heading | Bricolage Grotesque | 28px (1.75rem) | 700 | 1.10 | Card titles ("Better Habits", "Harder Workouts") |
| Body Large | Bricolage Grotesque | 24px (1.50rem) | 400 | 1.60 | Subtitle and intro paragraphs |
| Body Lead | Bricolage Grotesque / system | 20px (1.25rem) | 400 | 1.60 | Hero subtitle, section descriptions |
| Body | Bricolage Grotesque | 18px (1.13rem) | 400 | 1.40 | Standard reading text |
| UI / Nav | system | 16px (1.00rem) | 600 | 1.60 | Nav links, primary button labels |
| Button Label | Bricolage Grotesque | 14px (0.88rem) | 500 | — | Standard CTA labels |
| Caption | system / Bricolage | 14px (0.88rem) | 400–600 | 1.60 | Metadata, FAQ answers, footer |
| Pill Tag | Bricolage Grotesque | 12px (0.75rem) | 600 | 1.60 | Category pills inside iPhone mockup |
| Mono Chrome | SF Mono | 12px (0.75rem) | 400 | 1.00 | Uppercase chrome — "EDITORS' CHOICE" |
| Micro Mono | SF Mono | 10px (0.63rem) | 400 | 1.60 | Tiny footer metadata, version strings |

### Principles
- **Bricolage 700 carries the brand**: Every display heading runs at weight 700. Where Cape whispers at weight 300, Timespent shouts at weight 700 — confident, declarative, almost like a print headline.
- **System font for body**: Reading-size paragraphs drop to `-apple-system` to disappear into native legibility. Bricolage sings only at heading sizes.
- **Highlighter on emphasis**: 1–2 phrases per page get wrapped in `<mark>` with `#ffd600`. Not just color, a typographic device that mimics felt-tip annotation.
- **Tight display line-height**: Headings run at 1.10 — editorial display feel, handles two-line wraps cleanly.
- **Mono for chrome only**: SF Mono uppercase appears on "EDITORS' CHOICE" laurels and version strings. Signals "spec sheet" without going full retro-tech.
- **No letter-spacing tricks**: Bricolage at default tracking. The font's parametric design carries the personality.

## Layout

### Spacing System
- Base unit: 8px
- Scale (from JSON sample): 1px, 2px, 4px, 5.6px, 6px, 8px, 14px, 16px, 20px, 24px, 32px, 40px, 48px, 64px, 76px
- High-frequency values: **16px (57 instances)**, **32px (37)**, **20px (33)**, **8px (35)** — these four carry most of the layout
- Sub-pixel `5.6px` and odd values like `14px` and `76px` suggest some bespoke component tuning over a strict scale

### Grid & Container
- Max content width: ~1200px for the hero section
- Hero: 2-column — text left (headline + subtitle + CTA + laurels), iPhone product mockup right
- Feature grids: 2×2 or 3-up product card rows depending on viewport
- Widget grid section: 3–4 columns of varied tile sizes (asymmetric, gallery-style)
- FAQ section: single-column, full-width within container, left-aligned with hairline `<details>` rows

### Whitespace Philosophy
- **Indie-app pacing**: ~80–120px vertical between sections — each card group reads as its own chapter
- **Heading-anchored air**: 80px hero gets ~80–100px above/below; 28px card titles take ~20–32px
- **Cards float**: Product cards never touch — minimum 24–32px gutter on all sides
- **Uninterrupted canvas**: No full-bleed dark sections, the off-white canvas runs uninterrupted top to bottom

### Border Radius Scale
| Value | Use |
|-------|-----|
| `4px` | `<mark>` highlighter background corners (barely soft) |
| `12px` | Small widget tiles in the customization grid |
| `18px` | Mid-size widget cards |
| `24px` | **Default product card radius** — every iPhone-mockup card |
| `36px–38px` | Imagery rounded crops, large feature panels |
| `40px` | Largest hero cards |
| `999px` | Pills, buttons, theme-picker chips, category tabs |

Timespent's radius scale is **multi-tiered, not binary**: small (4–18px) for utility, medium (24–40px) for hero cards, full pill (999px) for buttons. Mid-range values are used deliberately, unlike Cape's binary system.

## Elevation & Depth

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | No shadow, no border | Page canvas, body text, section containers |
| Hairline (Level 1) | `1px solid #1f1f1f` | Card outlines, button borders, `<details>` dividers |
| Sticker (Level 2) | `rgba(17,17,17,0.11) 0px 2px 8px 0px, rgba(17,17,17,0.08) 0px 1px 3px 0px` | Default card lift — used 22+ times across the page |
| Sticker Lifted (Level 3) | `rgba(17,17,17,0.11) 0px 4px 8px 0px, rgba(17,17,17,0.08) 0px 2px 4px 0px` | Hover state and emphasized cards |
| Sticker Floating (Level 4) | `rgba(17,17,17,0.14) 0px 8px 8px 0px, rgba(17,17,17,0.11) 0px 4px 4px 0px` | Largest hero product cards, dropdowns |
| Modal Drop (Level 5) | `rgba(0,0,0,0.15) 0px 8px 24px 0px, rgba(0,0,0,0.1) 0px 4px 8px 0px` | Reserved — modal/popover surfaces |

**Shadow Philosophy**: Timespent's depth is **soft, layered, and atmospheric**, the opposite of Cape's hard offset stamps. Every shadow is a two-layer stack: a tight blur (1–4px) for crispness, a wider blur (8–24px) for ambient lift. Shadow color is warm-leaning ink (`rgba(17,17,17, x)`) rather than pure black, so cards feel like they're sitting on warm paper. Combined with the 1px ink hairline, every card gets both a sharp graphic edge AND a soft physical lift, sticker on a fridge. Cards always pair the border WITH the shadow, never one alone. No inset shadows, no glow rings, no colored shadows.

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

**Primary Pill (Black)**
- Background: Timespent Ink (`#1f1f1f`)
- Text: Off-White (`#fcfcfc`)
- Padding: 6px 12px compact, 12px 24px standard, 16px 32px large
- Radius: `999px` (full pill)
- Border: `0px none` default
- Shadow: `none` default; on hover gains `rgba(17,17,17,0.11) 0px 2px 8px`
- Font: 14–16px Bricolage Grotesque weight 500–600
- Use: Primary CTA — "Get timespent", "Download on the App Store", "See for yourself"

**Outlined Pill (Light)**
- Background: Off-White (`#fcfcfc`)
- Text: Timespent Ink (`#1f1f1f`)
- Border: `1px solid #1f1f1f`
- Radius: `999px`
- Shadow: `none` default; subtle drop shadow on hover
- Use: Secondary actions, theme-picker options, "Join Discord" nav link

**App Store Badge Button**
- Background: `#1f1f1f`
- Text: White, with Apple logo SVG
- Padding: 12px 20px
- Radius: `999px`
- Use: Specifically "Download on the App Store" — signature App Store-shaped CTA but rendered in the brand's pill language, not Apple's official badge

### Cards & Containers

**Sticker Product Card**
- Background: One of the saturated frame colors (poppy red, citrus orange, pine teal, mint green, navy black)
- Border: `1px solid #1f1f1f` (the signature hairline)
- Radius: `24px`
- Shadow: `rgba(17,17,17,0.11) 0px 2px 8px 0px, rgba(17,17,17,0.08) 0px 1px 3px 0px`
- Internal padding: 24–32px around the screenshot, with the title at the top-left
- Content: iPhone 15 Pro screenshot inset on the colored ground, title above or below in white/black depending on contrast

**Quote / Testimonial Card**
- Background: Navy Black or Poppy Red, white text, `24px` radius, 1px ink border, same sticker-shadow stack
- Padding: 32–48px. Star rating (`★★★★★`) top, quote in Bricolage 28px weight 700, attribution in caption mono

**Widget Tile**
- Background: Various (calendar grids, chart panels, progress rings)
- Radius: `12px` or `18px` (smaller than product cards), 1px border (`#1f1f1f` or `#eee`), lighter shadow
- Use: Widget showcase grid in "Endlessly customizable" section

### Pills / Tags

**Category Pill (Outlined)**
- Background: White or transparent
- Text: Ink (`#1f1f1f`)
- Border: `1px solid #1f1f1f`
- Radius: `999px`
- Padding: 4px 12px
- Font: 12px Bricolage Grotesque weight 600
- Use: Inside iPhone mockups — "Widgets / Goals / Routines / Streaks / Progress / Mood"

**Active Pill (Filled)**
- Background: Ink (`#1f1f1f`)
- Text: White
- Same dimensions as outlined
- Use: Selected state of category pill — selected tab indicator

### Highlighter Mark
- Element: `<mark>` HTML tag
- Background: Highlighter Yellow (`#ffd600`)
- Text: Ink (`#1f1f1f`) — inherited from parent heading
- Padding: 0 (sits flush against the text)
- Display: inline, no border-radius (or 4px on the `mark` element)
- Use: One or two emphasized phrases per page — "be **the best**", "**answered**", "**Seriously my new favorite app**"

### Inputs & Forms
Marketing page is form-light. FAQ accordion uses `<details>` with `0 0 1px 0 solid #1f1f1f` (bottom hairline only), 16–20px vertical padding, Bricolage 18–20px weight 400 for question, system font for answer.

### Navigation
Top nav is minimal: left-aligned `timespent` wordmark with circular icon, right-aligned "Join Discord" text link and "Get timespent" pill button. Sticky on scroll. Links 16px system font weight 600, `#1f1f1f`, underline on hover. No mega-menu, just two right-aligned actions.

### App Store Laurels
Two SVG laurel-leaf wreaths flanking "EDITORS' CHOICE — APPS WE LOVE" and "EDITORS' CHOICE — BEST NEW APPS", sitting directly below the primary CTA. Typography: 10–12px SF Mono uppercase weight 400, color Ink (`#1f1f1f`). No gold or color treatment, just black.

## Do's and Don'ts

### Do
- Use Bricolage Grotesque weight 700 for every display heading — bold is the brand voice
- Apply yellow highlighter (`#ffd600`) as `<mark>` on 1–2 phrases per page maximum — preserve the felt-tip moment
- Pair every card with both a `1px solid #1f1f1f` border AND the layered sticker shadow — never one alone
- Use `999px` pill radius for every button and tab — the system is button-as-pill consistently
- Wrap iPhone screenshots in saturated-color frames (red, orange, teal, mint, navy) at `24px` radius
- Drop body copy to `-apple-system` for legibility — let Bricolage carry the headings
- Use SF Mono uppercase for credibility-stamp chrome (laurels, version strings) at 10–12px weight 400
- Keep the canvas off-white (`#fcfcfc`) — never pure white, never gray
- Stack soft shadows in 2 layers for the sticker effect (`0 2px 8px` + `0 1px 3px`)

### Don't
- Don't use Bricolage at weight 400–500 for display sizes — weight 700 is the floor for headings
- Don't apply the yellow highlight as a button background or large color block — it's a marker, not a fill
- Don't use mid-weight (300–400) Bricolage on body text — drop to system font for body
- Don't add gradients anywhere — every surface is a flat color
- Don't use card frames without the 1px ink hairline — the border is non-negotiable
- Don't use hard offset shadows (`-4px 4px 0`) — Timespent is soft layered shadows only
- Don't introduce new chromatic accents beyond yellow + the curated card palette
- Don't use rectangular (0px) buttons — every CTA is a pill (`999px`)
- Don't crowd the canvas — sections need 80–120px of vertical breathing room

---

## Responsive Behavior

### Breakpoints (extracted)
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile | <640px | Single-column, 36–48px hero, stacked product cards, full-width CTA |
| Mobile Large | 640–768px | Single-column, 48–56px hero, 1-up cards |
| Tablet | 768–900px | 2-up product card grid begins, 56px hero |
| Desktop | ≥900px | Full layout — 2-column hero, 2×2 card grid, 80px hero, widget gallery in 3–4 columns |

### Touch Targets
Primary CTA pill: min 44px tap height, 24px horizontal padding on mobile. Category pills inside iPhone mockup: 32px tap height (decorative — inside a screenshot). FAQ `<details>` rows: full-row tap target, 56–64px tall.

### Collapsing Strategy
- **Hero**: 2-column desktop → text-above-image stack on mobile (text first, then iPhone mockup)
- **Hero type**: 80px → 56px → 48px → 36px progressive scaling, weight 700 maintained
- **Product card grid**: 2×2 desktop → 1-up stacked mobile, full-width cards
- **Widget gallery**: 3–4 columns desktop → 2 columns tablet → 1 column mobile
- **Nav**: "Join Discord" link drops, only the pill CTA remains on smallest screens
- **Section spacing**: 120px desktop → 64–80px mobile — reduces but maintains indie-app pace
- **Highlighter `<mark>`**: stays inline, scales with the heading

### Image Behavior
- iPhone product mockups maintain 9:19.5 aspect ratio at all breakpoints
- Card frame color and border preserved across viewports
- Widget gallery images crop closer on mobile rather than re-flowing
- App Store laurels stack vertically on mobile if both don't fit horizontally

---

## Agent Prompt Guide

### Quick Color Reference
- Primary Text: Timespent Ink (`#1f1f1f`)
- Page Background: Off-White Canvas (`#fcfcfc` / `hsl(0 0% 99%)`)
- Highlight Mark: Highlighter Yellow (`#ffd600`)
- Link Black: (`#111111`)
- Border Hairline: (`#eeeeee`) for soft, (`#1f1f1f`) for ink card outlines
- Card Frame Palette: Poppy Red, Citrus Orange, Pine Teal, Mint Green, Navy Black
- Sticker Shadow: `rgba(17,17,17,0.11) 0px 2px 8px 0px, rgba(17,17,17,0.08) 0px 1px 3px 0px`
- Border Radius: `24px` for cards, `999px` for pills

### Example Component Prompts
- "Create a hero section on Off-White (`#fcfcfc`) with a headline at 80px Bricolage Grotesque weight 700, line-height 1.10, color `#1f1f1f`. Wrap one phrase like 'the best' in a `<mark>` with background `#ffd600`. Place a black pill CTA below — `999px` radius, `#1f1f1f` background, white text, 14px weight 500, padding 12px 24px. Show the App Store laurels ('EDITORS' CHOICE — APPS WE LOVE') in 10px SF Mono uppercase below the CTA."
- "Design a product card with a Poppy Red (`#e84545`) background, `24px` border-radius, `1px solid #1f1f1f` hairline border, and a soft shadow `rgba(17,17,17,0.11) 0px 2px 8px 0px, rgba(17,17,17,0.08) 0px 1px 3px 0px`. Title 'Better Habits' at 28px Bricolage weight 700 in white, top-left padding 32px. Inset an iPhone screenshot below the title."
- "Build a category pill row inside an iPhone mockup — 6 pills (Widgets, Goals, Routines, Streaks, Progress, Mood). Each: white background, `1px solid #1f1f1f`, `999px` radius, padding 4px 12px, 12px Bricolage Grotesque weight 600 text in `#1f1f1f`. Active state: filled `#1f1f1f` background with white text."
- "Create a testimonial card on Navy Black (`#1a1a2e`) ground, `24px` radius, white text. Five gold stars at top, then the quote 'Seriously my new favorite app' at 28px Bricolage weight 700, attribution in 12px SF Mono uppercase below."
- "Design an FAQ accordion — `<details>` element with `0 0 1px 0 solid #1f1f1f` bottom border, no top/side borders. Question in 18–20px Bricolage weight 400, answer in 16px system font weight 400 line-height 1.60."

### Iteration Guide
1. Default to Bricolage Grotesque weight 700 for every display heading — never drop below 700 at heading sizes
2. The yellow highlighter (`#ffd600`) is sacred — apply as `<mark>` on 1–2 emphasized words per page only, never as a button background
3. Every card needs both `1px solid #1f1f1f` AND a layered sticker shadow — the duo is the system signature
4. Buttons are always pills (`999px`) — never rectangular, never mid-radius
5. Body copy drops to `-apple-system` so Bricolage stays a brand-only voice at headings
6. Card frame colors come from the curated palette (red, orange, teal, mint, navy) — don't introduce new ones
7. Off-white canvas (`#fcfcfc`) is non-negotiable — pure white reads sterile, gray reads dated
8. SF Mono uppercase belongs only on credibility chrome (laurels, version strings) — never on body or headings
9. Soft layered shadows (2-layer stack) for depth — no hard offset stamps, no glow, no inset
10. Spacing rhythm: 16/20/24/32 for component-level, 64/80/120 for section-level — let the page breathe
