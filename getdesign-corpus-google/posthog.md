---
version: alpha
name: PostHog
description: Warm, irreverent developer analytics with a sage-cream canvas, IBM Plex Sans bold headings, hand-drawn hedgehog personality, and a hidden orange that surprises on hover.

colors:
  # Surface & background
  background: "#fdfdf8"
  surface: "#eeefe9"
  surface-tertiary: "#e5e7e0"
  surface-featured: "#d4c9b8"
  surface-hover: "#f4f4f4"

  # Text / ink
  ink: "#4d4f46"
  ink-deep: "#23251d"
  ink-strong: "#111827"
  text-secondary: "#65675e"
  text-muted: "#9ea096"
  text-input: "#374151"

  # Brand accent
  primary: "#F54E00"
  primary-amber: "#F7A501"
  primary-amber-border: "#b17816"

  # Interactive / focus
  focus-ring: "#3b82f6"
  focus-ring-tint: "#9dc1fb"  # opaque approx of rgba(59,130,246,0.5) over #fdfdf8 — Google format requires hex

  # Borders
  border: "#bfc1b7"
  border-strong: "#b6b7af"

  # Dark CTA
  cta-dark: "#1e1f23"
  on-cta-dark: "#ffffff"

  # Shadow
  shadow-deep: "#bfbfbf"  # opaque approx of rgba(0,0,0,0.25) over #fdfdf8 — Google format requires hex

typography:
  display-hero:
    fontFamily: "IBM Plex Sans Variable, IBM Plex Sans, -apple-system, system-ui, sans-serif"
    fontSize: 30px
    fontWeight: 800
    lineHeight: 1.20
    letterSpacing: -0.75px
  section-heading:
    fontFamily: "IBM Plex Sans Variable, IBM Plex Sans, -apple-system, system-ui, sans-serif"
    fontSize: 36px
    fontWeight: 700
    lineHeight: 1.50
    letterSpacing: 0px
  feature-heading:
    fontFamily: "IBM Plex Sans Variable, IBM Plex Sans, -apple-system, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: 0px
  card-heading:
    fontFamily: "IBM Plex Sans Variable, IBM Plex Sans, -apple-system, system-ui, sans-serif"
    fontSize: 21.4px
    fontWeight: 700
    lineHeight: 1.40
    letterSpacing: -0.54px
  sub-heading:
    fontFamily: "IBM Plex Sans Variable, IBM Plex Sans, -apple-system, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.40
    letterSpacing: -0.5px
  label-uppercase:
    fontFamily: "IBM Plex Sans Variable, IBM Plex Sans, -apple-system, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.50
    letterSpacing: 0px
  body-semi:
    fontFamily: "IBM Plex Sans Variable, IBM Plex Sans, -apple-system, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.56
    letterSpacing: 0px
  body:
    fontFamily: "IBM Plex Sans Variable, IBM Plex Sans, -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0px
  body-relaxed:
    fontFamily: "IBM Plex Sans Variable, IBM Plex Sans, -apple-system, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.71
    letterSpacing: 0px
  nav-link:
    fontFamily: "IBM Plex Sans Variable, IBM Plex Sans, -apple-system, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.50
    letterSpacing: 0px
  caption:
    fontFamily: "IBM Plex Sans Variable, IBM Plex Sans, -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0px
  small-label:
    fontFamily: "IBM Plex Sans Variable, IBM Plex Sans, -apple-system, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.50
    letterSpacing: 0px
  micro:
    fontFamily: "IBM Plex Sans Variable, IBM Plex Sans, -apple-system, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0px
  code:
    fontFamily: "Source Code Pro, ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0px

spacing:
  micro: 2px
  xs: 4px
  sm: 6px
  md: 8px
  lg: 10px
  xl: 12px
  2xl: 16px
  3xl: 18px
  4xl: 24px
  5xl: 32px
  6xl: 34px

rounded:
  sharp: 2px
  sm: 4px
  md: 6px
  pill: 9999px

components:
  # Navigation
  nav-bar:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink-deep}"
    typography: "{typography.nav-link}"
    padding: 16px 24px
  nav-link:
    textColor: "{colors.ink-deep}"
    typography: "{typography.nav-link}"
    padding: 8px 12px
  nav-link-hover:
    textColor: "{colors.primary}"

  # Buttons
  button-primary:
    backgroundColor: "{colors.cta-dark}"
    textColor: "{colors.on-cta-dark}"
    typography: "{typography.caption}"
    rounded: "{rounded.md}"
    padding: 10px 12px
  button-primary-hover:
    backgroundColor: "{colors.cta-dark}"
    textColor: "{colors.primary-amber}"
  button-sage:
    backgroundColor: "{colors.surface-tertiary}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: 4px 8px
  button-sage-hover:
    backgroundColor: "{colors.surface-hover}"
    textColor: "{colors.primary}"
  button-featured:
    backgroundColor: "{colors.surface-featured}"
    textColor: "#000000"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
  button-ghost:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.sm}"
    padding: 4px 12px

  # Cards
  card:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: 16px
  card-sage:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: 16px
  card-shadow:
    backgroundColor: "{colors.background}"
    rounded: "{rounded.md}"
    padding: 16px

  # Inputs
  input:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text-input}"
    typography: "{typography.body}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
  input-focus:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text-input}"

  # Badges
  badge-pill:
    backgroundColor: "{colors.surface-tertiary}"
    textColor: "{colors.ink}"
    typography: "{typography.small-label}"
    rounded: "{rounded.pill}"
    padding: 2px 8px
---

# PostHog Design System

## Overview

PostHog's website feels like a startup's internal wiki that escaped into the wild — warm, irreverent, and deliberately anti-corporate. The background isn't the expected crisp white or dark void of developer tools; it's a warm, sage-tinted cream (`{colors.background}`) that gives every surface a handmade, paper-like quality. Colors lean into earthy olive greens and muted sage rather than the conventional blues and purples of the SaaS world. It's as if someone designed a developer analytics platform inside a cozy garden shed.

The personality is the star: hand-drawn hedgehog illustrations, quirky action figures, and playful imagery replace the stock photography and abstract gradients typical of B2B SaaS. IBM Plex Sans Variable serves as the typographic foundation — a font with genuine technical credibility (created by IBM, widely used in developer contexts) deployed here with bold weights (700, 800) on headings and generous line-heights on body text. The typography says "we're serious engineers" while everything around it says "but we don't take ourselves too seriously."

The interaction design carries the same spirit: hover states flash PostHog Orange (`{colors.primary}`) text — a hidden brand color that doesn't appear at rest but surprises on interaction. Dark near-black buttons (`{colors.cta-dark}`) use opacity reduction on hover rather than color shifts, and active states scale slightly. The border system uses sage-tinted grays (`{colors.border}`) that harmonize with the olive text palette. Built on Tailwind CSS with Radix UI and shadcn/ui primitives, the technical foundation is modern and component-driven, but the visual output is stubbornly unique.

**Key Characteristics:**
- Warm sage/olive color palette instead of conventional blues — earthy and approachable
- IBM Plex Sans Variable font at bold weights (700/800) for headings with generous 1.50+ line-heights
- Hidden brand orange (`{colors.primary}`) that only appears on hover interactions — a delightful surprise
- Hand-drawn hedgehog illustrations and playful imagery — deliberately anti-corporate
- Sage-tinted borders (`{colors.border}`) and backgrounds (`{colors.surface}`) creating a unified warm-green system
- Dark near-black CTAs (`{colors.cta-dark}`) with opacity-based hover states
- Content-heavy editorial layout — the site reads like a magazine, not a typical landing page
- Tailwind CSS + Radix UI + shadcn/ui component architecture

## Colors

### Primary
- **Olive Ink** (`{colors.ink}`): Primary text — a distinctive olive-gray that gives all text a warm, earthy tone.
- **Deep Olive** (`{colors.ink-deep}`): Link text and high-emphasis headings — near-black with green undertone.
- **PostHog Orange** (`{colors.primary}`): Hidden brand accent — appears only on hover states, a vibrant orange that surprises.

### Secondary & Accent
- **Amber Gold** (`{colors.primary-amber}`): Secondary hover accent on dark buttons — warm gold that pairs with the orange.
- **Gold Border** (`{colors.primary-amber-border}`): Special button borders — an amber-gold for featured CTAs.
- **Focus Blue** (`{colors.focus-ring}`): Focus ring color (Tailwind default) — the only blue in the system, reserved for accessibility.

### Surface & Background
- **Warm Parchment** (`{colors.background}`): Primary page background — warm near-white with yellow-green undertone.
- **Sage Cream** (`{colors.surface}`): Input backgrounds, secondary surfaces — light sage tint.
- **Light Sage** (`{colors.surface-tertiary}`): Button backgrounds, tertiary surfaces — muted sage-green.
- **Warm Tan** (`{colors.surface-featured}`): Featured button backgrounds — warm tan/khaki for emphasis.
- **Hover White** (`{colors.surface-hover}`): Universal hover background state.

### Neutrals & Text
- **Olive Ink** (`{colors.ink}`): Primary body and UI text.
- **Muted Olive** (`{colors.text-secondary}`): Secondary text, button labels on light backgrounds.
- **Sage Placeholder** (`{colors.text-muted}`): Placeholder text, disabled states — warm sage-green.
- **Sage Border** (`{colors.border}`): Primary border color — olive-tinted gray for all borders.
- **Light Border** (`{colors.border-strong}`): Secondary border, toolbar borders — slightly darker sage.

### Semantic & Accent
- **Dark Text** (`{colors.ink-strong}`): High-contrast link text — near-black for important links.
- **Focus Ring Tint** (`{colors.focus-ring-tint}`): Keyboard focus rings — accessibility-only blue.

### Gradient System
- No gradients on the marketing site — PostHog's visual language is deliberately flat and warm.
- Depth is achieved through layered surfaces and border containment, not color transitions.

## Typography

### Font Family
- **Display & Body**: `IBM Plex Sans Variable` — variable font (100–700+ weight range). Fallbacks: `IBM Plex Sans, -apple-system, system-ui, Avenir Next, Avenir, Segoe UI, Helvetica Neue, Helvetica, Ubuntu, Roboto, Noto, Arial`.
- **Monospace**: `ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, Liberation Mono, Courier New` — system monospace stack.
- **Code Display**: `Source Code Pro` — with fallbacks: `Menlo, Consolas, Monaco`.

### Hierarchy

The complete type scale lives in the `typography:` token block above. Reference tokens directly (`{typography.display-hero}`, `{typography.body}`, etc.) rather than hardcoding values.

| Token | Use |
|---|---|
| `display-hero` | Maximum size — landing hero statements |
| `section-heading` | Large section headings — feature areas |
| `feature-heading` | Feature section titles |
| `card-heading` | Card titles (slightly unusual scaled size) |
| `sub-heading` | Content sub-sections |
| `label-uppercase` | Uppercase category labels |
| `body-semi` | Semi-bold body text and emphasis |
| `body` | Standard reading text |
| `body-relaxed` | Long-read passages with relaxed line-height |
| `nav-link` | Top navigation and UI labels |
| `caption` | Small text, button labels |
| `small-label` | Tags, badges, micro labels |
| `micro` | Smallest text, metadata |
| `code` | Code snippets and terminal output |

### Principles
- **Bold heading dominance**: Headings use 700–800 weight — PostHog's typography is confident and assertive, not whispery.
- **Generous body line-heights**: Body text at 1.50–1.71 line-height creates extremely comfortable reading — the site is content-heavy and optimized for long sessions.
- **Fractional sizes**: Several sizes (21.4px, 13.7px) suggest a fluid/scaled type system rather than fixed stops — likely computed from Tailwind's rem scale at non-standard base.
- **Uppercase as category signal**: Bold uppercase labels (18px–20px weight 700) are used for product category headings — a magazine-editorial convention.
- **Selective negative tracking**: Letter-spacing tightens on display text (-0.75px at 30px) but relaxes to 0px on body — headlines compress, body breathes.

## Layout

### Spacing System
The complete spacing scale lives in the `spacing:` token block above. Base unit is 8px with a compact micro range (2–6px) reserved for tight UI chrome.

- Section padding: `5xl`–`6xl` vertical between sections (compact for a content-heavy site)
- Card padding: `xs`–`xl` internal (notably compact)
- Component gaps: `xs`–`md` between related elements

### Grid & Container
- Max width: 1536px (largest breakpoint), with content containers likely 1200px–1280px
- Column patterns: Varied — single column for text content, 2-3 column grids for feature cards, asymmetric layouts for product demos
- Breakpoints: 13 defined — 1px, 425px, 482px, 640px, 768px, 767px, 800px, 900px, 1024px, 1076px, 1160px, 1280px, 1536px

### Whitespace Philosophy
- **Content-dense by design**: PostHog's site is information-rich — whitespace is measured, not lavish.
- **Editorial pacing**: Content sections flow like a magazine with varied layouts keeping the eye moving.
- **Illustrations as breathing room**: Hand-drawn hedgehog art breaks up dense content sections naturally.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Level 0 (Flat) | No shadow, warm parchment background | Page canvas, most surfaces |
| Level 1 (Border) | `1px solid {colors.border}` | Card containment, input borders, section dividers |
| Level 2 (Compound Border) | Multiple 1px borders on different sides | Input groupings, toolbar elements |
| Level 3 (Deep Shadow) | `0px 25px 50px -12px {colors.shadow-deep}` | Modals, floating elements, mega-menu dropdowns |

**Shadow Philosophy**: PostHog's elevation system is remarkably minimal — only one shadow definition exists in the entire system. Depth is communicated through border containment (sage-tinted borders at 1px create gentle warm separation), surface color shifts (moving from `{colors.background}` to `{colors.surface}` to `{colors.surface-tertiary}`), and the single deep shadow reserved for modals, dropdowns, and popovers.

### Decorative Depth
- **Illustration layering**: Hand-drawn hedgehog art creates visual depth naturally.
- **No gradients or glow**: The flat, warm surface system relies entirely on border and surface-color differentiation.
- **No glassmorphism**: Fully opaque surfaces throughout.

## Shapes

| Token | Value | Use |
|---|---|---|
| `sharp` | 2px | Small inline elements, tags |
| `sm` | 4px | Primary UI components — buttons, inputs, dropdowns, menu items |
| `md` | 6px | Secondary containers — larger buttons, list items, card variants |
| `pill` | 9999px | Pill shape — badges, status indicators, rounded tags |

PostHog stays in the 2–6px radius range for all rectangular elements — the system is functionally subtle, never decoratively rounded.

## Components

The complete component spec lives in the `components:` token block above. Reference component tokens directly (`{components.button-primary}`, `{components.card-sage}`) rather than reconstructing them.

### Buttons
- **`button-primary`** — Dark near-black (`{colors.cta-dark}`), white text. Hover: opacity 0.7 with Amber Gold text. The main CTA — dark and confident.
- **`button-sage`** — Light sage surface, olive ink text. Hover: hover-white background with PostHog Orange text. Compact utility button.
- **`button-featured`** — Warm tan surface, black text. Hover: same orange text flash. Featured/premium actions.
- **`button-ghost`** — Near-white, transparent border, olive ink text. Minimal presence.
- **Hover pattern**: All buttons flash PostHog Orange (`{colors.primary}`) or Amber Gold (`{colors.primary-amber}`) text on hover — the brand's signature interaction surprise.

### Cards & Containers
- **`card`** — Warm Parchment or white background, 1px sage border, 4–6px radius. Clean and minimal.
- **`card-sage`** — Sage Cream background for secondary content containers.
- **`card-shadow`** — A single deep shadow (`0px 25px 50px -12px`) for elevated content (modals, dropdowns).
- **Hover**: Orange text flash on interactive cards — consistent with button behavior.

### Inputs & Forms
- **`input`** — Sage Cream background, sage placeholder text, 1px Light Border, 4px radius.
- **Focus**: Tailwind blue focus ring at 50% opacity.
- **Text color**: `{colors.text-input}` for input values — darker than primary text for readability.

### Navigation
- **Top nav**: Warm background, IBM Plex Sans at 15px weight 600.
- **Dropdown menus**: Rich mega-menu structure with product categories.
- **Link color**: Deep Olive (`{colors.ink-deep}`) for nav links, underline on hover.
- **CTA**: Dark Primary button in the nav — "Get started — free".

### Badges
- **`badge-pill`** — Pill-shaped tag with sage surface and olive ink, 13px small label type.

### Image Treatment
- **Hand-drawn illustrations**: Hedgehog mascot and quirky illustrations — the signature visual element.
- **Product screenshots**: UI screenshots embedded in device frames or clean containers.
- **Action figures**: Playful product photography of hedgehog figurines — anti-corporate.
- **Trust logos**: Enterprise logos displayed in a muted trust bar.

## Do's and Don'ts

### Do
- Use the olive/sage color family (`{colors.ink}`, `{colors.ink-deep}`, `{colors.border}`) for text and borders — the warm green undertone is essential to the brand
- Flash PostHog Orange (`{colors.primary}`) on hover states — it's the hidden brand signature
- Use IBM Plex Sans at bold weights (700/800) for headings — the font carries technical credibility
- Keep body text at generous line-heights (1.50–1.71) — the content-heavy site demands readability
- Maintain the warm parchment background (`{colors.background}`) — not pure white, never cold
- Use 4px border-radius for most UI elements — keep corners subtle and functional
- Include playful, hand-drawn illustration elements — the personality is the differentiator
- Apply opacity-based hover states (0.7 opacity) on dark buttons rather than color shifts

### Don't
- Don't use blue, purple, or typical tech-SaaS colors — PostHog's palette is deliberately olive/sage
- Don't add heavy shadows — the system uses one shadow for floating elements only; everything else uses borders
- Don't make the design look "polished" or "premium" in a conventional sense — PostHog's charm is its irreverent, scrappy energy
- Don't use tight line-heights on body text — the generous 1.50+ spacing is essential for the content-heavy layout
- Don't apply large border-radius (12px+) on cards — PostHog uses 4–6px, keeping things tight and functional
- Don't remove the orange hover flash — it's a core interaction pattern, not decoration
- Don't replace illustrations with stock photography — the hand-drawn hedgehog art is the brand
- Don't use pure white (`#ffffff`) as page background — the warm sage-cream tint is foundational

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|---|---|---|
| Mobile Small | <425px | Single column, compact padding, stacked cards |
| Mobile | 425px–640px | Slight layout adjustments, larger touch targets |
| Tablet | 640px–768px | 2-column grids begin, nav partially visible |
| Tablet Large | 768px–1024px | Multi-column layouts, expanded navigation |
| Desktop | 1024px–1280px | Full layout, 3-column feature grids, expanded mega-menu |
| Large Desktop | 1280px–1536px | Max-width container, generous margins |
| Extra Large | >1536px | Centered container at max-width |

### Touch Targets
- Buttons: 4px–6px radius with `4px–12px` padding — compact but usable
- Nav links: 15px text at weight 600 with adequate padding
- Mobile: Hamburger menu with simplified navigation
- Inputs: Generous vertical padding for thumb-friendly forms

### Collapsing Strategy
- **Navigation**: Full mega-menu with dropdowns → hamburger menu on mobile
- **Feature grids**: 3-column → 2-column → single column stacked
- **Typography**: Display sizes reduce across breakpoints (30px → smaller)
- **Illustrations**: Scale within containers, some may hide on mobile for space
- **Section spacing**: Reduces proportionally while maintaining readability

### Image Behavior
- Illustrations scale responsively within containers
- Product screenshots maintain aspect ratios
- Trust logos reflow into multi-row grids on mobile
- AI chat widget may reposition or simplify on small screens

## Agent Prompt Guide

### Quick Color Reference
- Primary Text: Olive Ink (`{colors.ink}`)
- Dark Text: Deep Olive (`{colors.ink-deep}`)
- Hover Accent: PostHog Orange (`{colors.primary}`)
- Dark CTA: Near-Black (`{colors.cta-dark}`)
- Button Surface: Light Sage (`{colors.surface-tertiary}`)
- Page Background: Warm Parchment (`{colors.background}`)
- Border: Sage Border (`{colors.border}`)
- Placeholder: Sage Placeholder (`{colors.text-muted}`)

### Example Component Prompts
- "Create a hero section on warm parchment background (`{colors.background}`) with 30px IBM Plex Sans heading at weight 800, line-height 1.20, letter-spacing -0.75px, olive ink text (`{colors.ink}`), and a dark CTA button (`{colors.cta-dark}`, 6px radius, white text, opacity 0.7 on hover)"
- "Design a feature card with `{colors.background}` background, 1px `{colors.border}` border, 4px radius, IBM Plex Sans heading at 20px weight 700, and 16px body text at weight 400 with 1.50 line-height in olive ink (`{colors.ink}`)"
- "Build a navigation bar with warm background, IBM Plex Sans links at 15px weight 600 in deep olive (`{colors.ink-deep}`), underline on hover, and a dark CTA button (`{colors.cta-dark}`) at the right"
- "Create a button group: primary dark (`{colors.cta-dark}`, white text, 6px radius), secondary sage (`{colors.surface-tertiary}`, `{colors.ink}` text, 4px radius), and ghost/text button — all flash `{colors.primary}` orange text on hover"
- "Design an input field with `{colors.surface}` background, 1px `{colors.border-strong}` border, 4px radius, `{colors.text-muted}` placeholder text, focus ring in `{colors.focus-ring}` at 50% opacity"

### Iteration Guide
1. Verify the background is warm parchment (`{colors.background}`) not pure white — the sage-cream warmth is essential
2. Check that all text uses the olive family (`{colors.ink}`, `{colors.ink-deep}`) not pure black or neutral gray
3. Ensure hover states flash PostHog Orange (`{colors.primary}`) — if hovering feels bland, you're missing this
4. Confirm borders use sage-tinted gray (`{colors.border}`) not neutral gray — warmth runs through every element
5. The overall tone should feel like a fun, scrappy startup wiki — never corporate-polished or sterile
