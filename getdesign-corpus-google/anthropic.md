---
version: alpha
name: "Anthropic"
description: "Research journal printed on warm stone — authoritative typographic composition where word-level underlines replace color as the primary emphasis mechanism, and the only warmth comes from the paper itself."

colors:
  background: "#ffffff"
  surface: "#faf9f5"
  surface-elevated: "#f5f5f5"
  ink: "#000000"
  ink-muted: "#141413"
  primary: "#e3dacc"
  on-primary: "#ffffff"
  border: "#d97757"
  focus-ring: "#e3dacc"
  success: "#22c55e"
  warning: "#f59e0b"
  error: "#ef4444"
  shadow-soft: "#d9d9d9"

typography:
  display-hero:
    fontFamily: "Anthropic Sans, ui-sans-serif, system-ui, sans-serif"
    fontSize: 91px
    fontWeight: 400
    lineHeight: 1.05
    letterSpacing: -1px
  display:
    fontFamily: "Anthropic Sans, ui-sans-serif, system-ui, sans-serif"
    fontSize: 63px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.5px
  heading-section:
    fontFamily: "Anthropic Sans, ui-sans-serif, system-ui, sans-serif"
    fontSize: 61px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.25px
  heading-sub:
    fontFamily: "Anthropic Sans, ui-sans-serif, system-ui, sans-serif"
    fontSize: 42px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0px
  body-large:
    fontFamily: "Anthropic Sans, ui-sans-serif, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  body:
    fontFamily: "Anthropic Sans, ui-sans-serif, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  button-ui:
    fontFamily: "Anthropic Sans, ui-sans-serif, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: 0px
  caption:
    fontFamily: "Anthropic Sans, ui-sans-serif, system-ui, sans-serif"
    fontSize: 12px
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

# Anthropic Design System

## Overview

Anthropic's site runs on warm ivory parchment (`#faf9f5`) — not white, not gray, but the color of aged paper under good light. The palette is almost entirely achromatic, with the entire chromatic budget spent on a single earthy terracotta accent (`#d97757`) held in reserve in CSS tokens but largely absent from the visible UI. The result reads less like a tech site and more like a research institution's broadsheet — authoritative, paper-textured, and confident enough to skip every default web flourish.

Two custom type families do all the personality work. Anthropic Sans drives navigation and UI at tight tracking, while Anthropic Serif delivers editorial weight in headlines and featured content — the serif-plus-grotesque pairing signals research institution, not startup. Headlines use a thick double-underline on key words (visible on 'research' and 'products' in the hero) as the sole decorative device — it replaces color as the emphasis mechanism. With no color drawing the eye, typographic decoration carries the entire semantic weight.

Composition is governed by a strict thermal alternation. The ivory page base gives way to massive feature cards that flip to near-black (`#141413`) background — hard-edged inverted bands with zero gradient or shadow softening. The dark cards aren't full viewport-width but full content-column-width with a 24px radius, creating a 'contained inversion' rather than a full-bleed band. Ivory peeks around all four corners, maintaining the sense that dark is a surface element, not a background takeover.

**Key Characteristics:**
- Warm ivory base (`#faf9f5`) — never pure white, never gray; aged-paper undertone throughout
- Custom type pairing: Anthropic Sans (grotesque, UI) + Anthropic Serif (editorial display) + Anthropic Mono (metadata)
- Underline as the sole emphasis mechanism — no color, no bold weight, no highlight
- Strict thermal alternation: ivory page → dark editorial card → light card grid → repeat
- Asymmetric radius signature on the primary CTA: flat top, rounded bottom (`0px 0px 8px 8px`)
- Zero shadows, zero gradients — all depth comes from surface contrast and 1px borders
- Dark feature cards at 24px radius with full content-column width, never browser-edge bleed
- Anthropic Mono used sparingly for `DATE` / `CATEGORY` metadata — signals structured data within editorial layout
- Chromatic accent palette (Clay, Olive, Sky, Fig, Cactus) reserved as categorical tags, never combined
- Single recurring 3D dark-field visualization — biological cell mesh aesthetic, contained within dark cards

## Colors

### Background Surfaces
- **Ivory Light** (`#faf9f5`): Page base — the warm parchment canvas. Never pure white.
- **Ivory Medium** (`#f0eee6`): Navigation bar, secondary card surfaces. One step warmer than the page.
- **Oat** (`#e3dacc`): Tertiary card backgrounds, callout sections. The primary anchor.
- **Feature Dark** (`#141413`): Editorial dark card surface — maximum contrast against the page base.

### Text & Content
- **Slate Dark** (`#141413`): Primary text. Doubles as the dark surface — the system uses one dense slate for both text and inverted backgrounds.
- **Slate Light** (`#5e5d59`): Tertiary text.
- **Cloud Dark** (`#87867f`): Secondary text and metadata.
- **Cloud Medium** (`#b0aea5`): Disabled and muted borders.
- **Ivory Dark** (`#e8e6dc`): Body text on dark backgrounds.

### Brand & Accent
- **Clay** (`#d97757`): The single chromatic accent. CTA elements when chromatic emphasis is needed — sparingly.
- **Accent Ember** (`#c6613f`): Deeper Clay state for hover or pressed.

### Categorical Tag Colors (one-per-section, never combined)
- **Olive** (`#788c5d`): Thematic tag variant.
- **Sky** (`#6a9bcc`): Thematic tag variant.
- **Fig** (`#c46686`): Thematic tag variant.
- **Cactus** (`#bcd1ca`): Thematic tag variant.

### Border & Divider
- **Slate Medium** (`#3d3d3a`): Mid-dark borders, scrolled-nav border state.
- **Cloud Light** (`#d1cfc5`): Default dividers.

## Typography

### Font Families
- **Anthropic Sans** (substitute: Inter, DM Sans): All UI chrome — navigation, buttons, labels, footer, body copy. The custom grotesque with tight negative tracking at large sizes — at 61px with -0.02em it reads as architectural lettering, not typical web type. Used at weight 700 for hero headlines, 400 for body, 500–600 for interactive elements.
- **Anthropic Serif** (substitute: Playfair Display, Lora): Feature card headlines, editorial hero text, project titles. At 91px it dominates the dark feature cards — the serif at display scale against near-black reads as a printed broadsheet masthead.
- **Anthropic Mono** (substitute: JetBrains Mono, IBM Plex Mono): Technical labels, metadata fields, category tags. Appears sparingly — its presence signals 'data' or 'classification' within otherwise typographic layouts.

### Hierarchy

| Role | Font | Size | Line Height | Letter Spacing |
|------|------|------|-------------|----------------|
| Display | Anthropic Serif | 91px | 1.10 | normal |
| Heading-lg (Hero) | Anthropic Sans | 61px | 1.10 | -1.22px |
| Heading | Anthropic Sans | 24px | 1.30 | -0.12 |
| Heading-sm | Anthropic Sans | 20px | 1.40 | normal |
| Subheading | Anthropic Sans | 18px | 1.40 | normal |
| Body | Anthropic Sans | 15px | 1.40 | normal |
| Body-sm | Anthropic Sans | 15px | 1.40 | -0.03 |
| Caption | Anthropic Mono | 12px | 1.30 | normal |

### Principles
- **Underline is the only emphasis device**: In hero headlines, key nouns ('research', 'products') receive a thick text-decoration underline. This replaces accent color or bold weight increase. With near-zero chromatic color in the system, typographic decoration carries all semantic weight.
- **Serif lives on dark, grotesque lives on light**: Anthropic Serif at 91px is reserved for inverted (dark) editorial cards. The grotesque carries every light-surface headline. The pairing isn't decorative — it's a surface rule.
- **Mono signals structured data**: Anthropic Mono appears at 16px for `DATE` and `CATEGORY` field labels in card footers. The mono-against-grotesque contrast tags content as classified or timestamped within editorial layout.
- **Aggressive negative tracking at scale**: -1.22px at 61px compresses display headlines into authoritative blocks. Below 24px, tracking relaxes to normal.

## Layout

### Spacing System
- **Element gap**: 8–16px
- **Section gap**: 61px
- **Card padding**: 31px
- The 31px card padding is unusual — most systems land on 24 or 32. Anthropic's 31 is deliberate, breaking the standard 8px grid for an editorial-feeling rhythm.

### Border Radius Scale
- **Buttons**: `0px` (default) or `0px 0px 8px 8px` (primary nav CTA — asymmetric signature)
- **Badges**: `0px` (no chrome at all)
- **Cards**: `8px`
- **Panels**: `16px`
- **Featured Cards**: `24px` (the dark editorial cards)

### Grid
- Max-width centered layout at ~1200px
- Hero is split-column: ~55% headline column on left, ~30% descriptive paragraph on right
- 3-column grid for 'Latest releases' below dark editorial bands
- Section gaps at ~61px establish vertical rhythm

### Layout & Composition
The page rhythm is: hero → dark editorial band → light card grid → repeat. Hero sits on ivory with ~80px top padding, headline in the left column, brief paragraph on the right. Below it, dark cards (radius 24px) break the ivory field — left half carries Anthropic Serif display headline plus CTA, right half holds the 3D visualization image. These dark cards are full-column-width, not full-bleed. Below them, a 3-column release card grid on oat or ivory-dark backgrounds. Navigation is a sticky top bar at full width, ~68px tall. No sidebar. No mega-menu — dropdown triggers are inline with chevrons. The strict alternating thermal pattern (light → dark → light) is the page's structural beat.

## Elevation & Depth

| Level | Hex | Name | Purpose |
|-------|-----|------|---------|
| 1 | `#faf9f5` | Page Base | Root background, button fills, default surface |
| 2 | `#f0eee6` | Nav / Elevated Light | Navigation bar, secondary card surfaces |
| 3 | `#e3dacc` | Oat Card | Tertiary card backgrounds, callout sections |
| 4 | `#141413` | Feature Dark | Editorial feature cards, inverted content blocks |

**Shadow Philosophy**: Anthropic refuses shadows entirely. There is no drop-shadow, no inner shadow, no glow on any component. Elevation is communicated through three signals only — surface color shifts (the four-step ivory ladder above), 1px solid borders (`#141413` on light, `#3d3d3a` on dark), and the dark inversion bands. The absence of shadow is the system's strongest formal signal: this is paper, not glass.

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

**Primary Nav Button — 'Try Claude'**
- Background: `#faf9f5`, Text: `#141413`, Border: `1px solid #141413`
- Radius: `0px 0px 8px 8px` — flat top, rounded bottom (the asymmetric signature)
- Padding: `12px 31px`, Anthropic Sans 15px weight 500
- No hover shadow — border color shifts to indicate state

**Continue Reading Button (on dark card)**
- Same chrome as the nav CTA but with `0px` radius — flat all corners
- Background: `#faf9f5` on `#141413` card surface
- The asymmetric radius is a signature reserved for the global nav; on dark surfaces it goes square

**Ghost Nav Button**
- Background: transparent, Text: `#141413`, Border: `1px solid #141413`
- Radius: `0px`, Padding: `22px 12px`
- Anthropic Sans 15px weight 400. Used for dropdown triggers ('Commitments', 'Learn')

**Muted Ghost Button**
- Background: transparent, Text: `#b0aea5`, Border: `1px solid #b0aea5`
- Radius: `0px`. Disabled or de-emphasized state

**Inline Underlined Headline Link**
- No background, no padding. Text: `#141413`, weight 700 at 61px
- `text-decoration: underline` with thick visible style — the keyword emphasis mechanism in headlines
- Only appears on selected words in display text, never in body

### Cards

**Dark Editorial Feature Card**
- Background: `#141413`, Radius: `24px`, Padding: `31px`
- Headline: Anthropic Serif 91px weight 400, color `#faf9f5`, line-height 1.10
- Subtitle: Anthropic Sans 20px weight 400, color `#e8e6dc`
- Right half holds 3D abstract imagery clipped to the same 24px radius
- Full content-column width, never full-bleed to browser edge

**Release Card (Light)**
- Background: `#f0eee6` or `#e3dacc`, Radius: `8px`, Padding: `31px`
- Headline: Anthropic Sans 20px weight 600, `#141413`
- Body: Anthropic Sans 15px weight 400, `#141413`
- Footer: `DATE` label in Anthropic Mono 16px `#87867f`, value `#141413`
- 'Read announcement →' link in Anthropic Sans 15px `#141413`
- No border, no shadow — surface color alone differentiates the card

### Badges & Labels
- **Metadata Label**: zero chrome — pure typographic structure
- Background: transparent, Border: none, Radius: `0px`, no padding
- Anthropic Mono 16px or Anthropic Sans 12px weight 500
- `DATE`, `CATEGORY` appear as uppercase tracking labels above values
- No pill, no chip, no capsule — Anthropic refuses background fills on metadata

### Navigation
- **Top Navigation Bar**: `#f0eee6` or `#faf9f5` background, sticky, ~68px height
- Wordmark left: 'ANTHROPIC\' in Anthropic Sans 16px weight 700 `#141413`
- Center links: Anthropic Sans 15px weight 400 `#141413`, transparent background
- Right: 'Try Claude' asymmetric-radius button
- No bottom border by default; subtle `#3d3d3a` border appears on scroll

### Inline Arrow Link
- No background, no border. Anthropic Sans 15px weight 400, `#141413`
- Arrow glyph '→' appended directly to text. No underline until hover
- Used for 'Read announcement →', 'Read the story', 'Model details'

## Do's and Don'ts

### Do

- Use `#faf9f5` (Ivory Light) as the page base — never pure white (`#ffffff`) or neutral gray.
- Apply borderRadius `0px` to all buttons and interactive controls except the primary 'Try Claude' CTA which uses `0px 0px 8px 8px` (asymmetric: flat top, rounded bottom only).
- Emphasize headline keywords with a thick text-decoration underline only — never color, bold weight increase, or highlight backgrounds — as the sole decorative emphasis mechanism.
- Use Anthropic Serif at display sizes (91px, weight 400) exclusively within dark (`#141413`) surface cards; use Anthropic Sans for all light-surface headlines.
- Restrict chromatic color to the CSS accent palette (Clay `#d97757`, Olive `#788c5d`, etc.) and deploy it sparingly — one accent per section maximum; default state uses zero chromatic color.
- Set dark editorial feature cards to borderRadius 24px and keep them full content-column width with hard clipping of interior imagery at the same radius.
- Use Anthropic Mono 16px for metadata field labels (DATE, CATEGORY) in card footers — the mono/grotesque contrast signals structured data within editorial layout.

### Don't

- Never use pure white (`#ffffff`) or pure black (`#000000`) as a surface background — all surfaces must come from the ivory/slate token range.
- Never add box-shadows or drop-shadows to any component — surface contrast and border lines are the only depth signals.
- Never round button corners uniformly — the 0px radius is a deliberate formal signal; avoid introducing 4px, 6px, or pill buttons.
- Never use Anthropic Serif on the page's ivory background at large sizes — the serif display scale is reserved for the dark card inversion.
- Never apply multiple chromatic accent colors within a single section — the palette tokens (Clay, Sky, Fig, Olive) are categorical variants, not combinable accents.
- Never use background fills for badge or label components — metadata labels are pure text with no chip, pill, or capsule treatment.
- Never replace the underline emphasis mechanic with color emphasis on headlines — links within headlines underline, they do not change color.

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile | <640px | Hero collapses to single column, headline drops to ~36–42px, dark cards remain 24px radius but stack vertically |
| md | 768px+ | Two-column hero returns, 2-column release card grid |
| lg | 1024px+ | Full 3-column release grid, dark editorial cards at full width |
| xl | 1280px+ | Max-width 1200px applies, generous side margins |

### Touch Targets
- Buttons maintain `12px 31px` padding at all sizes — comfortable thumb target on mobile
- Nav links keep `22px 12px` padding for adequate tap area
- 'Try Claude' CTA preserves its asymmetric radius even at mobile sizes — the signature shape doesn't break

### Collapsing Strategy
- Hero headline scales 61px → 42px → 32px, retaining underline emphasis on keywords
- Dark editorial cards remain card-shaped at all sizes, never going full-bleed even on mobile
- 3-column release grid → 2-col → single stacked column, card padding reduces from 31px to ~20px at mobile
- Section gaps compress from 61px to ~40px on mobile but keep the alternating thermal pattern intact

---

## Agent Prompt Guide

### Quick Color Reference
- Page background: `#faf9f5` (Ivory Light)
- Primary text: `#141413` (Slate Dark)
- Dark card surface: `#141413`
- Light card surface: `#f0eee6` / `#e3dacc`
- Muted / disabled: `#b0aea5`
- Accent (use sparingly): `#d97757` (Clay)
- Border default: `#141413` (1px solid)

### Example Component Prompts

1. **Hero Section**: Ivory (`#faf9f5`) background. Left column: headline 'AI research and products' at 61px Anthropic Sans weight 700, `#141413`, letter-spacing -1.22px; the words 'research' and 'products' have a thick underline text-decoration. Right column: body text 18px Anthropic Sans weight 400, `#141413`, max-width ~320px. No background image. 80px top padding.

2. **Dark Editorial Feature Card**: backgroundColor `#141413`, borderRadius 24px, padding 31px. Left: project title at 91px Anthropic Serif weight 400, `#faf9f5`, line-height 1.10. Subtitle at 20px Anthropic Sans weight 400, `#e8e6dc`. CTA button: backgroundColor `#faf9f5`, color `#141413`, border 1px solid `#141413`, borderRadius 0px, padding 12px 31px, Anthropic Sans 15px weight 500. Right: dark-field 3D mesh visualization image clipped to 24px radius.

3. **Release Card Grid (3-col)**: Each card backgroundColor `#f0eee6`, borderRadius 8px, padding 31px. Headline: Anthropic Sans 20px weight 600, `#141413`. Body: Anthropic Sans 15px weight 400, `#141413`, line-height 1.40. Footer row: 'DATE' label in Anthropic Mono 16px `#87867f`, value `#141413`. Arrow link 'Read announcement →' Anthropic Sans 15px `#141413`. No border, no shadow.

4. **Top Navigation Bar**: backgroundColor `#f0eee6`, height 68px, full-width. Left: wordmark 'ANTHROPIC\' Anthropic Sans 16px weight 700 `#141413`. Center: nav links 15px weight 400 `#141413`, transparent bg, 0px radius, padding 22px 12px, 1px solid `#141413` border. Right: 'Try Claude' button backgroundColor `#faf9f5`, border 1px solid `#141413`, borderRadius 0px 0px 8px 8px, padding 12px 31px, Anthropic Sans 15px weight 500.

5. **Metadata Label + Value Pair**: Label 'DATE' or 'CATEGORY' in Anthropic Mono 16px weight 400, `#87867f`, uppercase, no background, no border. Value below in Anthropic Sans 15px weight 400 `#141413`. Zero padding, zero border-radius — pure typographic structure.

### Iteration Guide
1. Ivory-first; never use pure white. The warm undertone is the entire atmosphere.
2. Underline is the only emphasis device — never color, never bold weight, never highlight.
3. Serif lives on dark surfaces; grotesque lives on light. Don't mix.
4. Asymmetric radius (`0px 0px 8px 8px`) is reserved for the primary nav CTA only.
5. Anthropic Mono is data clothing — use it for `DATE`, `CATEGORY`, and structured metadata.
6. Zero shadows. Surface contrast and 1px borders carry all elevation.
7. The thermal alternation (ivory → dark → ivory) is structural, not decorative — preserve the pattern.
