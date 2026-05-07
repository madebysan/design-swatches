---
version: alpha
name: NVIDIA
description: High-contrast technology-forward design built on stark black and white with the signature NVIDIA Green accent used exclusively for borders and underlines.

colors:
  # Canvas
  background: "#000000"
  background-light: "#ffffff"
  surface: "#ffffff"
  surface-dark: "#1a1a1a"

  # Ink
  ink: "#000000"
  ink-inverted: "#ffffff"
  text-secondary: "#757575"
  text-muted: "#a7a7a7"
  text-tertiary: "#898989"

  # Brand accent
  primary: "#76b900"  # NVIDIA Green
  primary-light: "#bff230"  # bright lime accent
  on-primary: "#000000"

  # Extended brand
  orange-400: "#df6500"
  yellow-300: "#ef9100"
  yellow-050: "#feeeb2"
  purple-800: "#4d1368"
  purple-100: "#f9d4ff"
  fuchsia-700: "#8c1c55"

  # Status
  error: "#e52020"
  error-deep: "#650b0b"
  success: "#3f8500"
  info: "#0046a4"

  # Interactive
  link-hover: "#3860be"
  button-hover: "#1eaedb"
  button-active: "#007fff"
  border-active: "#003eff"
  focus-ring: "#000000"

  # Borders
  border: "#5e5e5e"

  # Shadow tint
  shadow-card: "#4d4d4d"  # was rgba(0,0,0,0.3) — flattened approximation

typography:
  display-hero:
    fontFamily: "NVIDIA-EMEA, Arial, Helvetica, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0px
  section-heading:
    fontFamily: "NVIDIA-EMEA, Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0px
  sub-heading:
    fontFamily: "NVIDIA-EMEA, Arial, Helvetica, sans-serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.75
    letterSpacing: 0px
  card-title:
    fontFamily: "NVIDIA-EMEA, Arial, Helvetica, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0px
  body-large:
    fontFamily: "NVIDIA-EMEA, Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.67
    letterSpacing: 0px
  body:
    fontFamily: "NVIDIA-EMEA, Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  body-bold:
    fontFamily: "NVIDIA-EMEA, Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.5
    letterSpacing: 0px
  body-small:
    fontFamily: "NVIDIA-EMEA, Arial, Helvetica, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.67
    letterSpacing: 0px
  button-large:
    fontFamily: "NVIDIA-EMEA, Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0px
  button:
    fontFamily: "NVIDIA-EMEA, Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: 0px
  button-compact:
    fontFamily: "NVIDIA-EMEA, Arial, Helvetica, sans-serif"
    fontSize: 14.4px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: 0.144px
  link-uppercase:
    fontFamily: "NVIDIA-EMEA, Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 700
    lineHeight: 1.43
    letterSpacing: 0px
  caption:
    fontFamily: "NVIDIA-EMEA, Arial, Helvetica, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: 0px
  caption-small:
    fontFamily: "NVIDIA-EMEA, Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: 0px
  micro-label:
    fontFamily: "NVIDIA-EMEA, Arial, Helvetica, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.5
    letterSpacing: 0px

spacing:
  micro: 2px
  xs: 4px
  sm: 8px
  md: 11px
  lg: 16px
  xl: 24px
  2xl: 32px
  3xl: 48px
  4xl: 64px
  5xl: 80px

rounded:
  none: 0px
  micro: 1px
  sm: 2px
  pill: 9999px

components:
  # Primary green-bordered CTA
  button-primary:
    backgroundColor: "{colors.background-light}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.sm}"
    padding: 11px 13px
  button-primary-hover:
    backgroundColor: "{colors.button-hover}"
    textColor: "{colors.ink-inverted}"
  button-primary-active:
    backgroundColor: "{colors.button-active}"
    textColor: "{colors.ink-inverted}"

  # Compact / inline button
  button-compact:
    backgroundColor: "{colors.background-light}"
    textColor: "{colors.ink}"
    typography: "{typography.button-compact}"
    rounded: "{rounded.sm}"
    padding: 8px 11px

  # Card on light surface
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: 24px
  card-dark:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.ink-inverted}"
    rounded: "{rounded.sm}"
    padding: 24px

  # Top nav (dark)
  nav-bar:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink-inverted}"
    typography: "{typography.link-uppercase}"
    padding: 16px 24px

  # Link variants
  link-on-dark:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink-inverted}"
    typography: "{typography.body-bold}"
    padding: 0px

  link-on-light:
    backgroundColor: "{colors.background-light}"
    textColor: "{colors.ink}"
    typography: "{typography.body-bold}"
    padding: 0px
---

# NVIDIA Design System

## Overview

NVIDIA's website is a high-contrast, technology-forward experience that communicates raw computational power through design restraint. The page is built on a stark black (`{colors.background}`) and white (`{colors.background-light}`) foundation, punctuated by NVIDIA's signature green (`{colors.primary}`) — a color so specific it functions as a brand fingerprint. This is not the lush green of nature; it's the electric, lime-shifted green of GPU-rendered light, a color that sits between chartreuse and kelly green and immediately signals "NVIDIA" to anyone in technology.

The custom NVIDIA-EMEA font family (with Arial and Helvetica fallbacks) creates a clean, industrial typographic voice. Headings at 36px bold with tight 1.25 line-height create dense, authoritative blocks of text. The font lacks the geometric playfulness of Silicon Valley sans-serifs — it's European, pragmatic, and engineering-focused. Body text runs at 15-16px, comfortable for reading but not generous, maintaining the sense that screen real estate is optimized like GPU memory.

What distinguishes NVIDIA's design from other dark-background tech sites is the disciplined use of the green accent. The `{colors.primary}` appears in borders (`2px solid`), link underlines, and CTAs — but never as backgrounds or large surface areas on the main content. The green is a signal, not a surface. Combined with a deep shadow system (`{colors.shadow-card}` ambient) and minimal border radius (1-2px), the overall effect is of precision engineering hardware rendered in pixels.

**Key Characteristics:**
- NVIDIA Green (`{colors.primary}`) as pure accent — borders, underlines, and interactive highlights only
- Black (`{colors.background}`) dominant background with white (`{colors.ink-inverted}`) text on dark sections
- NVIDIA-EMEA custom font with Arial/Helvetica fallback — industrial, European, clean
- Tight line-heights (1.25 for headings) creating dense, authoritative text blocks
- Minimal border radius (1-2px) — sharp, engineered corners throughout
- Green-bordered buttons (`2px solid {colors.primary}`) as primary interactive pattern
- Multi-framework architecture (PrimeReact, Fluent UI, Element Plus) enabling rich interactive components

## Colors

### Primary Brand
- **NVIDIA Green** (`{colors.primary}`): The signature — borders, link underlines, CTA outlines, active indicators. Never used as large surface fills.
- **True Black** (`{colors.background}`): Primary page background, text on light surfaces, dominant tone.
- **Pure White** (`{colors.background-light}`): Text on dark backgrounds, light section backgrounds, card surfaces.

### Extended Brand Palette
- **NVIDIA Green Light** (`{colors.primary-light}`): Bright lime accent for highlights and hover states.
- **Orange 400** (`{colors.orange-400}`): Warm accent for alerts, featured badges, or energy-related contexts.
- **Yellow 300** (`{colors.yellow-300}`): Secondary warm accent, product category highlights.
- **Yellow 050** (`{colors.yellow-050}`): Light warm surface for callout backgrounds.

### Status & Semantic
- **Red 500** (`{colors.error}`): Error states, destructive actions, critical alerts.
- **Red 800** (`{colors.error-deep}`): Deep red for severe warning backgrounds.
- **Green 500** (`{colors.success}`): Success states, positive indicators (darker than brand green).
- **Blue 700** (`{colors.info}`): Informational accents, link hover alternative.

### Decorative
- **Purple 800** (`{colors.purple-800}`): Deep purple for gradient ends, premium/AI contexts.
- **Purple 100** (`{colors.purple-100}`): Light purple surface tint.
- **Fuchsia 700** (`{colors.fuchsia-700}`): Rich accent for special promotions or featured content.

### Neutral Scale
- **Gray 300** (`{colors.text-muted}`): Muted text, disabled labels.
- **Gray 400** (`{colors.text-tertiary}`): Secondary text, metadata.
- **Gray 500** (`{colors.text-secondary}`): Tertiary text, placeholders, footers.
- **Gray Border** (`{colors.border}`): Subtle borders, divider lines.
- **Near Black** (`{colors.surface-dark}`): Dark surfaces, card backgrounds on black pages.

### Interactive States
- **Link Hover** (`{colors.link-hover}`): Blue shift on hover across all link variants.
- **Button Hover** (`{colors.button-hover}`): Teal highlight for button hover states.
- **Button Active** (`{colors.button-active}`): Bright blue for active/pressed button states.
- **Border Active** (`{colors.border-active}`): Border on active button state.
- **Focus Ring** (`{colors.focus-ring}`): Black outline for keyboard focus.

### Shadows & Depth
- **Card Shadow** (`{colors.shadow-card}`): Flattened approximation of `rgba(0, 0, 0, 0.3) 0px 0px 5px` — subtle ambient shadow for elevated cards.

## Typography

### Font Family
- **Primary**: `NVIDIA-EMEA`, with fallbacks: `Arial, Helvetica, sans-serif`
- **Icon Font**: `Font Awesome 6 Pro` (weight 900 for solid icons, 700 for regular)
- **Icon Sharp**: `Font Awesome 6 Sharp` (weight 300 for light icons, 400 for regular)

### Hierarchy

The complete type scale lives in the `typography:` token block above. Reference tokens directly (`{typography.display-hero}`, `{typography.body}`).

| Token | Use |
|---|---|
| `display-hero` | Maximum impact headlines |
| `section-heading` | Section titles, card headings |
| `sub-heading` | Feature descriptions, subtitles |
| `card-title` | Card and module headings |
| `body-large` | Emphasized body, lead paragraphs |
| `body` | Standard reading text |
| `body-bold` | Strong labels, nav items |
| `body-small` | Secondary content, descriptions |
| `button-large` | Primary CTA buttons |
| `button` | Standard buttons |
| `button-compact` | Small/compact buttons |
| `link-uppercase` | Navigation links (text-transform: uppercase) |
| `caption` | Metadata, timestamps |
| `caption-small` | Fine print, legal |
| `micro-label` | Tiny badges (text-transform: uppercase) |

### Principles
- **Bold as the default voice**: NVIDIA leans heavily on weight 700 for headings, buttons, links, and labels. The 400 weight is reserved for body text and descriptions.
- **Tight headings, relaxed body**: Heading line-height is consistently 1.25 (tight), while body text relaxes to 1.50-1.67.
- **Uppercase for navigation**: Link labels use `text-transform: uppercase` with weight 700, creating a navigation voice that reads like hardware specification labels.
- **No decorative tracking**: Letter-spacing is normal throughout, except for compact buttons (0.144px). The font itself carries the industrial character.

## Layout

### Spacing System
The complete spacing scale lives in the `spacing:` token block above. Base unit is 8px with mid values at 11px and 13px reflecting NVIDIA's purposeful density.

### Grid & Container
- Max content width: approximately 1200px (contained)
- Full-width hero sections with contained text
- Feature sections: 2-3 column grids for product cards
- Single-column for article/blog content
- Sidebar layouts for documentation

### Whitespace Philosophy
- **Purposeful density**: NVIDIA uses tighter spacing than typical SaaS sites, reflecting the density of technical content. White space exists to separate concepts, not to create luxury emptiness.
- **Section rhythm**: Dark sections alternate with white sections, using background color (not just spacing) to separate content blocks.
- **Card density**: Product cards sit close together with 16-20px gaps, creating a catalog feel rather than a gallery feel.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat (Level 0) | No shadow | Page backgrounds, inline text |
| Subtle (Level 1) | `0px 0px 5px {colors.shadow-card}` | Standard cards, modals |
| Border (Level 1b) | `1px solid {colors.border}` | Content dividers, section borders |
| Green Accent (Level 2) | `2px solid {colors.primary}` | Active elements, CTAs, selected items |
| Focus (Accessibility) | `2px solid {colors.focus-ring}` outline | Keyboard focus ring |

**Shadow Philosophy**: NVIDIA's depth system is minimal and utilitarian. There is essentially one shadow value — a 5px ambient blur — used sparingly for cards and modals. The primary depth signal is not shadow but _color contrast_: black backgrounds next to white sections, green borders on black surfaces. This creates hardware-like visual layering where depth comes from material difference, not simulated light.

## Shapes

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Edge-to-edge sections |
| `micro` | 1px | Inline spans, tiny elements |
| `sm` | 2px | Buttons, cards, containers, inputs — the default for nearly everything |
| `pill` | 9999px | Avatar images, circular tab indicators (50% radius equivalent) |

NVIDIA's radius system is intentionally minimal: 1-2px corners read as engineered precision rather than soft friendliness. The pill is reserved for circular avatars only.

## Components

The complete component spec lives in the `components:` token block above. Reference component tokens directly.

### Buttons
- **`button-primary`** — Transparent surface with `2px solid {colors.primary}` green border. Primary CTA pattern. Hover: background `{colors.button-hover}`, text white. Active: background `{colors.button-active}` with `1px solid {colors.border-active}`.
- **`button-compact`** — Smaller variant at 14.4px with 0.144px tracking for inline CTAs and compact navigation.

### Cards
- **`card`** — White surface, 2px radius. Optional `0px 0px 5px {colors.shadow-card}` ambient shadow for elevated cards.
- **`card-dark`** — Dark surface (`{colors.surface-dark}`) for cards on black pages. Optional `1px solid {colors.border}` for definition.

### Links
- **`link-on-dark`** — White text on black background, no underline, hover shifts to `{colors.link-hover}`.
- **`link-on-light`** — Black text on white surface with `2px solid {colors.primary}` green underline. Hover: shift to `{colors.link-hover}`, underline removed.

### Navigation
- **`nav-bar`** — Dark black background, prominent NVIDIA wordmark left-aligned. Links at 14px weight 700 uppercase, white. Sticky on scroll with backdrop. Mega-menu dropdowns for product categories.

## Do's and Don'ts

### Do
- Use `{colors.primary}` as accent — never as a background fill. It is a signal color for borders, underlines, and highlights
- Buttons are transparent with green borders by default — filled backgrounds appear only on hover/active states
- Use weight 700 as the dominant voice for all interactive and heading elements; 400 is only for body paragraphs
- Use `{rounded.sm}` (2px) for everything — sharp, minimal rounding is core to the industrial aesthetic
- Dark sections use white text; light sections use black text — green accent works identically on both
- Link hover is always `{colors.link-hover}` regardless of the link's default color
- Use line-height 1.25 for headings, 1.50-1.67 for body text
- Use uppercase 14px bold for navigation — hardware-label typography is part of the brand voice

### Don't
- Don't use NVIDIA Green as a background fill or large surface — it loses its signal quality
- Don't soften corners with mid-range radius — the system is sharp by design
- Don't use blurred drop shadows for emphasis — material/color contrast carries depth
- Don't introduce playful or geometric display fonts — the EMEA voice is industrial and pragmatic
- Don't add gradients to UI chrome — the green-on-black contrast is the system's signature

---

## Responsive Behavior

*(Preserved from original 9-section format — Google's parser keeps unknown sections.)*

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile Small | <375px | Compact single column, reduced padding |
| Mobile | 375-425px | Standard mobile layout |
| Mobile Large | 425-600px | Wider mobile, some 2-col hints |
| Tablet Small | 600-768px | 2-column grids begin |
| Tablet | 768-1024px | Full card grids, expanded nav |
| Desktop | 1024-1350px | Standard desktop layout |
| Large Desktop | >1350px | Maximum content width, generous margins |

### Touch Targets
- Buttons use 11px 13px padding for comfortable tap targets
- Navigation links at 14px uppercase with adequate spacing
- Green-bordered buttons provide high-contrast touch targets on dark backgrounds
- Mobile: hamburger menu collapse with full-screen overlay

### Collapsing Strategy
- Hero: 36px heading scales down proportionally
- Navigation: full horizontal nav collapses to hamburger menu at ~1024px
- Product cards: 3-column to 2-column to single column stacked
- Footer: multi-column grid collapses to single stacked column
- Section spacing: 64-80px reduces to 32-48px on mobile
- Images: maintain aspect ratio, scale to container width

### Image Behavior
- GPU/product renders maintain high resolution at all sizes
- Hero images scale proportionally with viewport
- Card images use consistent aspect ratios
- Full-bleed dark sections maintain edge-to-edge treatment

### Typography Scaling
- Display 36px scales to ~24px on mobile
- Section headings 24px scale to ~20px on mobile
- Body text maintains 15-16px across all breakpoints
- Button text maintains 16px for consistent tap targets

### Dark/Light Section Strategy
- Dark sections (black bg, white text) alternate with light sections (white bg, black text)
- The green accent remains consistent across both surface types
- On dark: links are white, underlines are green
- On light: links are black, underlines are green

---

## Agent Prompt Guide

*(Preserved from original 9-section format — the copy-paste payload section.)*

### Quick Color Reference
- Primary accent: NVIDIA Green (`{colors.primary}`)
- Background dark: True Black (`{colors.background}`)
- Background light: Pure White (`{colors.background-light}`)
- Heading text (dark bg): White (`{colors.ink-inverted}`)
- Heading text (light bg): Black (`{colors.ink}`)
- Body text (light bg): Black (`{colors.ink}`) or Near Black (`{colors.surface-dark}`)
- Body text (dark bg): White (`{colors.ink-inverted}`) or Gray 300 (`{colors.text-muted}`)
- Link hover: Blue (`{colors.link-hover}`)
- Border accent: `2px solid {colors.primary}`
- Button hover: Teal (`{colors.button-hover}`)

### Example Component Prompts
- "Create a hero section on black background. Headline at 36px NVIDIA-EMEA weight 700, line-height 1.25, color white. Subtitle at 18px weight 400, line-height 1.67, color `{colors.text-muted}`. CTA button with transparent background, `2px solid {colors.primary}` border, 2px radius, 11px 13px padding, white text. Hover: background `{colors.button-hover}`, text white."
- "Design a product card: white background, 2px border-radius, ambient shadow `{colors.shadow-card}`. Title at 20px NVIDIA-EMEA weight 700, line-height 1.25, color black. Body at 15px weight 400, line-height 1.67, color `{colors.text-secondary}`. Green underline accent on title."
- "Build a navigation bar: `{colors.background}` background, sticky top. NVIDIA logo left-aligned. Links at 14px NVIDIA-EMEA weight 700 uppercase, color white. Hover: color `{colors.link-hover}`. Green-bordered CTA button right-aligned."
- "Create a dark feature section. Section label at 14px weight 700 uppercase, color `{colors.primary}`. Heading at 24px weight 700, color white. Description at 16px weight 400, color `{colors.text-muted}`. Three product cards in a row with 20px gap."
- "Design a footer: black background. Multi-column layout with link groups. Links at 14px weight 400, color `{colors.text-muted}`. Hover: color `{colors.primary}`. Bottom bar with legal text at 12px, color `{colors.text-secondary}`."

### Iteration Guide
1. Always use `{colors.primary}` as accent, never as a background fill — it's a signal color for borders, underlines, and highlights
2. Buttons are transparent with green borders by default — filled backgrounds appear only on hover/active states
3. Weight 700 is the dominant voice for all interactive and heading elements; 400 is only for body paragraphs
4. Border radius is 2px for everything — this sharp, minimal rounding is core to the industrial aesthetic
5. Dark sections use white text; light sections use black text — green accent works identically on both
6. Link hover is always `{colors.link-hover}` regardless of the link's default color
7. Line-height 1.25 for headings, 1.50-1.67 for body text — maintain this contrast for visual hierarchy
8. Navigation uses uppercase 14px bold — this hardware-label typography is part of the brand voice
