---
version: alpha
name: "Ubuntu"
description: "Fedora-aubergine masthead, warm orange CTAs, terminal-amber accents and the humanist Ubuntu typeface carrying every word"

colors:
  background: "#ffffff"
  surface: "#772953"
  surface-elevated: "#f5f5f5"
  ink: "#111111"
  ink-muted: "#cdcdcd"
  primary: "#e95420"
  on-primary: "#ffffff"
  border: "#666666"
  focus-ring: "#e95420"
  success: "#22c55e"
  warning: "#f59e0b"
  error: "#ef4444"
  shadow-soft: "#d9d9d9"

typography:
  display-hero:
    fontFamily: "Ubuntu, ui-sans-serif, system-ui, sans-serif"
    fontSize: 56px
    fontWeight: 300
    lineHeight: 1.05
    letterSpacing: -1px
  display:
    fontFamily: "Ubuntu, ui-sans-serif, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: -0.5px
  heading-section:
    fontFamily: "Ubuntu, ui-sans-serif, system-ui, sans-serif"
    fontSize: 42px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.25px
  heading-sub:
    fontFamily: "Ubuntu, ui-sans-serif, system-ui, sans-serif"
    fontSize: 29px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0px
  body-large:
    fontFamily: "Ubuntu, ui-sans-serif, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  body:
    fontFamily: "Ubuntu, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  button-ui:
    fontFamily: "Ubuntu, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: 0px
  caption:
    fontFamily: "Ubuntu, ui-sans-serif, system-ui, sans-serif"
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

# Ubuntu Design System

## Overview

The Ubuntu site is open-source warmth made navigable. The canvas is pure white (`#ffffff`) with deep aubergine and warm orange providing the brand's two-note chromatic system. The masthead and footer are saturated aubergine (`#772953`) — a slightly purpled deep brown that recalls the original Fedora hat and the terminal session — and primary CTAs run in Ubuntu's signature warm orange (`#E95420`), a color so brand-defining that it doubles as the cursor blink in the official terminal palette. Body text sits in deep neutral (`#111111`) on white, with secondary copy stepping down to `#666666`. Imagery is community-warm — circuits and silicon photography, Linux-in-the-wild diversity shots, and clean product photography of laptops running Ubuntu desktop.

What makes Ubuntu unmistakable is the **humanist Ubuntu typeface contract**. The system uses the bespoke Ubuntu typeface — a humanist sans designed by Dalton Maag specifically for Canonical, with subtle calligraphic terminals and a warm, approachable rhythm — for every piece of body and display chrome. Code samples switch to **Ubuntu Mono**, a perfectly-tuned monospaced companion that matches the body's optical weight. This gives ubuntu.com the rare quality of looking like the operating system it sells: warm, slightly tactile, recognizably Linux but distinctly not corporate. There is no secondary face anywhere.

The third defining trait is **bold tactile chrome**. The Vanilla framework defaults to `0.125rem` (2px) border-radius — barely-there rounding that gives buttons and inputs a slightly softened rectangle without going friendly. Borders are `1px` strokes in `#cdcdcd` (cool grey hairlines) on white. Drop shadows are minimal but present — Vanilla uses two soft shadow tiers for elevation (cards and modals), giving the chrome a faintly tactile lift without becoming Material Design. The CTA orange button has a slightly rounded `2px` corner and uses Ubuntu's signature warm orange that, on a hover, deepens by 8% — the result is a button that reads as a real, pressable object rather than a flat web rectangle.

**Key Characteristics:**
- Pure white canvas (`#ffffff`) with aubergine `#772953` masthead and footer
- Warm orange CTA color (`#E95420`) — the signature Ubuntu accent
- Deep neutral text (`#111111`) on light, white text on aubergine surfaces
- Single-typeface system — Ubuntu (humanist sans by Dalton Maag) for everything, Ubuntu Mono for code
- Tactile but minimal corners — `0.125rem` (2px) default radius
- 8px-grid spacing system inherited from Vanilla Framework
- Cool grey hairlines (`#cdcdcd`) for borders, warm orange accent only on chromatic moments
- Minimal but real shadows — `box-shadow: 0 0 4px rgba(0,0,0,0.1)` for cards, slightly deeper for modals
- 16px base body at `1.5` line-height
- Code samples in Ubuntu Mono on `#f7f7f7` /* estimated */ light grey panels

## Colors

### Primary Brand
- **Ubuntu Orange** (`#E95420`): The signature warm orange — used for primary buttons, active link states, key brand-mark moments, and the original Ubuntu logo. Reads as cursor-amber on a CRT. The defining accent.

### Brand Accent
- **Aubergine** (`#772953`): The deep brand purple-brown — used for the masthead background, footer background, and dark-surface treatments. The original Fedora-derived brand color.
- **Warm Grey** (`#AEA79F`) /* from Canonical brand guidelines */: The neutral warm grey used as a secondary brand neutral on secondary surfaces and dividers.
- **Cool Grey** (`#333333` / `#111111`): Deep neutrals for text and dark UI.

### Text Scale
- **Deep Text** (`#111111`): Primary text and headings on light surfaces — Vanilla's default body color.
- **Mid Text** (`#666666`) /* estimated */: Secondary text, captions, meta labels.
- **Quiet Text** (`#999999`) /* estimated */: Disabled and placeholder text.
- **Inverse Text** (`#ffffff`): All text on aubergine surfaces and orange CTAs.

### Surface & Background
- **Pure White** (`#ffffff`): The default canvas — Vanilla's primary surface.
- **Light Panel** (`#f7f7f7`) /* estimated */: Used for code blocks, alternate sections, terminal blocks.
- **Cool Border Grey** (`#cdcdcd`) /* estimated */: Default border and divider color.
- **Aubergine Surface** (`#772953`): The dark masthead and footer surface.
- **Aubergine Mid** (`#5e2750`) /* estimated, derived from masthead hover state */: Mid-tone aubergine for layered nav components.

### Borders & Dividers
- **Default Border** (`1px solid #cdcdcd`): The standard hairline used for cards, inputs, and secondary buttons.
- **Subtle Divider** (`1px solid #e5e5e5`) /* estimated */: Tertiary dividers for footer and quiet sections.
- **Aubergine Hairline** (`1px solid #5e2750`) /* estimated */: Used in the masthead for sub-nav separators.
- **Orange Border** (`1px solid #E95420`): Used on focused inputs and active button outlines.

### Shadow System
- **Card Shadow** (`box-shadow: 0 1px 5px 1px rgba(17, 17, 17, 0.1)`) /* estimated based on Vanilla Framework conventions */: The default card-elevation shadow — soft, low-opacity, used on product cards and feature blocks.
- **Modal Shadow** (`box-shadow: 0 1px 14px 1px rgba(17, 17, 17, 0.2)`) /* estimated */: Deeper shadow for dialogs, modals, and pop-out menus.
- **Hover Lift** (`box-shadow: 0 2px 8px 1px rgba(17, 17, 17, 0.15)`) /* estimated */: Card hover state — slightly deeper than default rest.

The shadow system is intentionally restrained — Vanilla uses two-to-three subtle elevation tiers, giving the UI a faint tactility without resembling a Material Design site. Most surfaces are flat at rest.

## Typography

### Font Family
- **Primary**: `Ubuntu`, fallback chain: `-apple-system, "Segoe UI", Roboto, Oxygen, Cantarell, sans-serif`
- **Monospaced**: `"Ubuntu Mono"`, fallback: `"Courier New", Courier, monospace`
- **Loading source**: Self-hosted from ubuntu.com / Canonical CDN. Both faces are open-source — designed by Dalton Maag for Canonical, released under the Ubuntu Font License.
- **External use**: Ubuntu and Ubuntu Mono are freely available on Google Fonts and via the Ubuntu Font License. Substitute with **Inter** for the body and **JetBrains Mono** for the monospace if Ubuntu cannot be loaded.

The Ubuntu typeface has subtle calligraphic terminals (look at the lowercase `t` and `e`), warm openness, and a slightly humanist character that sets it apart from corporate-grade grotesks like Inter or Helvetica.

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Hero / H1 | Ubuntu | 56px (3.5rem) /* estimated */ | 300 | 1.15 | normal | Largest headline — landing pages |
| Display H1 | Ubuntu | 40px (2.5rem) /* estimated */ | 300 | 1.2 | normal | Page-level H1, lighter weight feel |
| H2 | Ubuntu | 32px (2rem) /* estimated */ | 300 | 1.25 | normal | Section openers |
| H3 | Ubuntu | 24px (1.5rem) /* estimated */ | 400 | 1.3 | normal | Subsection headings |
| H4 | Ubuntu | 20px (1.25rem) /* estimated */ | 400 | 1.4 | normal | In-body headings |
| H5 | Ubuntu | 18px (1.125rem) /* estimated */ | 400 | 1.4 | normal | Minor headings |
| Body | Ubuntu | 16px (1rem) | 400 | 1.5 | normal | Default long-form body |
| Body Lead | Ubuntu | 18px (1.125rem) /* estimated */ | 400 | 1.5 | normal | Article lede, slightly larger |
| Button | Ubuntu | 16px (1rem) | 400 | 1.5 | normal | Primary and secondary CTAs — sentence case |
| Nav Link | Ubuntu | 16px (1rem) /* estimated */ | 400 | 1.5 | normal | Top-level navigation |
| Caption | Ubuntu | 14px (0.875rem) /* estimated */ | 400 | 1.4 | normal | Image captions, meta |
| Code Block | Ubuntu Mono | 14px (0.875rem) /* estimated */ | 400 | 1.5 | normal | Inline code, code samples |
| Code Display | Ubuntu Mono | 16px (1rem) /* estimated */ | 400 | 1.5 | normal | Featured code snippets, terminal previews |

### Principles
- **Light weight on display**: Ubuntu's display sizes (32px+) traditionally use weight 300 — the typeface's calligraphic warmth reads better at light weight than at bold display
- **Regular weight on body**: 16px body sits at weight 400 with `1.5` line-height — comfortable reading rhythm
- **Sentence case for UI**: Buttons, navigation, and labels use natural prose case
- **Ubuntu Mono for code**: every code snippet, terminal example, and inline command uses Ubuntu Mono — matched to the body's optical weight
- **No italics on display**: emphasis through weight contrast or color shift, not italic
- **Open-source ethos**: The typeface itself is part of the brand promise — Canonical commits the Ubuntu font to the same open license as the OS

## Layout

### Spacing System
- Base unit: `8px` (Vanilla Framework convention)
- Common scale: `4px`, `8px`, `16px`, `24px`, `32px`, `48px`, `64px`, `96px` /* estimated */
- Vanilla uses a `0.25rem`-based scale where everything snaps to 4px or 8px multiples

### Grid & Container
- Vanilla grid: 12-column responsive grid with consistent gutters
- Max content width: `1200px` /* estimated, Vanilla default */
- Hero: full-bleed with overlaid text; on aubergine surfaces, text is `#ffffff`
- Footer: 4–5 column desktop layout with aubergine background

### Whitespace Philosophy
- **Documentation pacing**: sections separated by `48–96px` vertical padding — generous but not luxurious
- **Image isolation**: laptop and product photography sits with `24px+` of negative space
- **Code-block breathing**: code samples have `1rem 1.5rem` internal padding for comfortable reading
- **Aubergine band rhythm**: the brand uses full-width aubergine sections to break up white-on-white monotony

### Border Radius Scale
- Sharp (`0`): full-bleed sections, hero banners
- Tactile (`0.125rem` / 2px): the workhorse — buttons, inputs, cards, code blocks — all use this barely-there radius
- Modal (`0.25rem` / 4px): dialog and modal containers
- Pill (`50%`): used for the circle-of-friends logo elements only

The system trusts the `2px` workhorse radius — it gives chrome a faint tactility without going friendly.

## Elevation & Depth

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | `box-shadow: none` | Default for buttons, inputs, sections |
| Hairline Border (Level 1) | `1px solid #cdcdcd` | Default card and input border |
| Card Shadow (Level 2) | `0 1px 5px 1px rgba(17, 17, 17, 0.1)` /* estimated */ | Product cards, feature blocks |
| Hover Lift (Level 3) | `0 2px 8px 1px rgba(17, 17, 17, 0.15)` /* estimated */ | Hovered card state |
| Modal Shadow (Level 4) | `0 1px 14px 1px rgba(17, 17, 17, 0.2)` /* estimated */ | Dialogs, popovers, overlays |

**Shadow Philosophy**: Ubuntu's design system uses shadows tactically — most chrome is flat with `1px` borders, but cards and modals get subtle real shadows that communicate depth without feeling Material. The brand intentionally lands between "flat brutalism" (which would feel cold for an open-source community brand) and "soft elevation everywhere" (which would feel corporate). The result is a faintly tactile UI that reads as a real, friendly desktop environment.

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

### Buttons (Vanilla Framework Style)

**Primary (Orange CTA)**
- Background: `#E95420`
- Text: `#ffffff`
- Padding: `0.5rem 1rem` /* estimated */
- Radius: `0.125rem` (2px)
- Border: `1px solid #E95420`
- Font: 16px Ubuntu weight 400
- Hover: background deepens to `#c7401c` /* estimated 8% darker */
- Active: even deeper, slight inset shadow
- Use: Primary CTAs — "Download Ubuntu", "Get started", "Sign up"

**Negative (Red Destructive)**
- Background: `#c7162b` /* estimated, Vanilla negative red */
- Text: `#ffffff`
- Padding: `0.5rem 1rem`
- Radius: `0.125rem` (2px)
- Use: Destructive actions, delete confirmations

**Neutral (Outline / Ghost)**
- Background: `transparent`
- Text: `#111111`
- Border: `1px solid #cdcdcd`
- Padding: `0.5rem 1rem`
- Radius: `0.125rem`
- Hover: background fills `#f7f7f7`, border stays
- Use: Secondary CTAs

**Inverse (For Aubergine Surfaces)**
- Background: `transparent`
- Text: `#ffffff`
- Border: `1px solid #ffffff`
- Padding: `0.5rem 1rem`
- Radius: `0.125rem`
- Hover: background fills `rgba(255, 255, 255, 0.1)`
- Use: CTAs on aubergine masthead and footer

### Cards & Containers
- Background: `#ffffff`
- Border: `1px solid #cdcdcd` /* estimated */
- Radius: `0.125rem` (2px)
- Shadow: subtle `0 1px 5px 1px rgba(17, 17, 17, 0.1)` /* estimated */
- Internal padding: `1.5rem` (24px) standard, `2rem` (32px) for feature cards

### Inputs & Forms
- Background: `#ffffff`
- Border: `1px solid #cdcdcd` /* estimated */
- Radius: `0.125rem` (2px)
- Padding: `0.5rem 0.75rem` /* estimated */
- Font: 16px Ubuntu weight 400 in `#111111`
- Focus: border shifts to `1px solid #E95420` (orange focus), no glow ring

### Navigation

**Masthead (Aubergine)**
- Background: `#772953` (aubergine)
- Wordmark: white "ubuntu" wordmark with circle-of-friends symbol
- Primary nav: 16px Ubuntu weight 400 links in `#ffffff`, sentence case
- Hover: text underlines or shifts to slight opacity change
- Sub-nav: opens as a layered panel below the masthead with `#ffffff` background

**Page Nav (White)**
- Background: `#ffffff`
- Primary links: 16px Ubuntu weight 400 in `#111111`
- Hover: text underlines, color stays
- Active: bottom border `2px solid #E95420` /* estimated */

### Code Blocks
- Background: `#f7f7f7` /* estimated */
- Border: `0` or `1px solid #cdcdcd` /* estimated */
- Radius: `0.125rem`
- Font: Ubuntu Mono 14px weight 400 line-height 1.5 in `#111111`
- Padding: `1rem 1.5rem` /* estimated */
- Use: Documentation snippets, install commands, terminal examples

### Terminal Block (Stylized)
- Background: `#300A24` /* estimated, Ubuntu's official terminal background */
- Text: `#ffffff` (or amber `#FAB913` for prompt and cursor) /* estimated */
- Font: Ubuntu Mono 14px weight 400
- Padding: `1.5rem`
- Radius: `0.125rem`
- Optional: leading `$ ` prompt in amber, command in white
- Use: "Try it" interactive terminal previews

### Decorative Elements
- **Circle of Friends**: The Ubuntu logo's iconic three-figure circle — appears in branded contexts as background watermark or as the favicon
- **Ubuntu Orange Underline**: hovered editorial links get a `2px` orange underline — the brand's hover signature
- **Aubergine Section Bands**: full-width `#772953` bands break up the page rhythm, used for testimonials and quote sections

## Do's and Don'ts

### Do
- Use Ubuntu (or Inter as substitute) for ALL text — there is one face for body and chrome
- Use Ubuntu Mono for every code sample, command, and terminal example
- Set body text at `16px` Ubuntu weight 400 with `1.5` line-height in `#111111`
- Reserve Ubuntu Orange (`#E95420`) for primary CTAs, active states, and brand-mark moments
- Use aubergine (`#772953`) for masthead, footer, and full-width brand bands
- Default to `0.125rem` (2px) border-radius for buttons, inputs, and cards
- Use light weights (300) for display sizes — Ubuntu's calligraphic warmth shines at light weight
- Stack regular weight (400) for body and chrome
- Apply subtle shadows to cards and modals only — buttons and inputs stay flat
- Use sentence case throughout UI labels, buttons, and navigation
- Include the circle-of-friends logo as the brand mark in masthead and footer

### Don't
- Don't substitute the Ubuntu typeface with a corporate grotesk (Helvetica, Arial) — the warmth is the brand
- Don't use heavy weights (700+) on display sizes — Ubuntu lights up at 300
- Don't use `border-radius` above `0.25rem` (4px) — the 2px workhorse is the brand's tactile signature
- Don't introduce a tertiary brand color — the system is orange + aubergine, full stop
- Don't use the orange (`#E95420`) for body text or large surface fills — it is a CTA accent only
- Don't add hard drop shadows to buttons — buttons are flat with subtle hover state
- Don't bleed code blocks edge-to-edge on white — always frame with `#f7f7f7` background and `1rem+` padding
- Don't use uppercase aggressively in UI labels — Ubuntu sits in sentence case
- Don't replace Ubuntu Mono with a generic monospace — the character match between Ubuntu and Ubuntu Mono is part of the system
- Don't use Material Design elevation conventions — Vanilla's shadows are flatter and warmer

---

## Responsive Behavior

### Breakpoints (Vanilla Framework defaults)
| Name | Width | Key Changes |
|------|-------|-------------|
| Small | <620px /* estimated */ | Single-column, hamburger nav |
| Medium | 620–1036px /* estimated */ | 2-column grids, condensed nav |
| Large | ≥1036px /* estimated */ | Full horizontal nav, multi-column grids |
| X-Large | ≥1681px /* estimated */ | Maximum container, expanded margins |

### Touch Targets
- Primary buttons: `44px+` tap height via `0.5rem` vertical padding plus 16px line-height
- Nav links: `44px+` zone in mobile drawer
- Form inputs: `40px+` minimum height

### Collapsing Strategy
- **Masthead**: aubergine bar collapses to hamburger drawer with full-screen aubergine overlay
- **Hero**: stacks vertically on mobile; display sizes scale proportionally
- **Footer**: 4–5 column desktop layout collapses to vertical accordion
- **Code blocks**: stay full-width but allow horizontal scroll if commands exceed viewport
- **Body type**: stays at `16px` regardless of viewport

---

## Agent Prompt Guide

### Quick Reference
- Page Background: `#ffffff` (white)
- Aubergine Surface: `#772953`
- Primary CTA: `#E95420` (Ubuntu Orange)
- Primary Text: `#111111`
- Secondary Text: `#666666`
- Border: `1px solid #cdcdcd`
- Code Surface: `#f7f7f7`
- Terminal Surface: `#300A24` (aubergine-deep)
- Body Font: `Ubuntu, -apple-system, "Segoe UI", Roboto, sans-serif`
- Code Font: `"Ubuntu Mono", "Courier New", monospace`

### Example Component Prompts
- "Create a hero on `#ffffff` with a 40px Ubuntu weight 300 headline at line-height 1.2 in `#111111`, an 18px Ubuntu weight 400 lede paragraph at line-height 1.5 in `#666666`, and a primary orange CTA: `#E95420` background, white text, 16px Ubuntu weight 400, padding `0.5rem 1rem`, `0.125rem` (2px) radius, no shadow."
- "Build a navigation masthead — `#772953` aubergine background, white Ubuntu wordmark on the left, horizontal row of 16px Ubuntu weight 400 white nav links in sentence case. On hover, links underline. Sub-nav opens as a `#ffffff` panel below the masthead."
- "Design a code block — `#f7f7f7` background, 14px Ubuntu Mono weight 400 in `#111111`, padding `1rem 1.5rem`, `0.125rem` radius, no border (or thin `1px solid #cdcdcd`). Optional: stylize as a terminal with `#300A24` (aubergine-deep) background and white-on-aubergine text."
- "Create a feature card on `#ffffff` with `1px solid #cdcdcd` border, `0.125rem` radius, `0 1px 5px 1px rgba(17, 17, 17, 0.1)` shadow, `1.5rem` padding. Inside: a 24px Ubuntu weight 400 heading in `#111111`, 16px Ubuntu weight 400 body in `#666666` at line-height 1.5, and a neutral outline button at the bottom."
- "Build an aubergine quote band — full-width `#772953` background, white Ubuntu 24px weight 300 quote text, smaller 16px weight 400 attribution below, generous `64px+` vertical padding for the band itself."

### Iteration Guide
1. Default to one typeface — Ubuntu for body and chrome, Ubuntu Mono for code. No third face.
2. Display sizes prefer weight 300 — the calligraphic warmth shines at light weight.
3. Body type is `16px` Ubuntu weight 400 at `1.5` line-height in `#111111`.
4. Border-radius is `0.125rem` (2px) for the workhorse — buttons, inputs, cards. The barely-there roundness is the brand's tactile signature.
5. The brand color system is binary: orange (`#E95420`) for CTAs and active states, aubergine (`#772953`) for masthead/footer/brand bands. No third brand color.
6. Drop shadows are tactile but subtle — `0 1px 5px 1px rgba(17, 17, 17, 0.1)` for cards, slightly deeper for modals. Buttons stay flat.
7. Code is sacred — every command and snippet runs in Ubuntu Mono on `#f7f7f7` panels. For interactive terminals, use `#300A24` aubergine-deep with white text.
8. Sentence case throughout UI — Ubuntu sits in natural prose case, never aggressive uppercase.
9. Use the orange focus indicator (`1px solid #E95420`) on inputs — accessibility-first.
10. The page is community-warm. Aubergine bands and orange accents punctuate white space — the result reads like a printed Linux user-group flyer translated to web.
