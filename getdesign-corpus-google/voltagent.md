---
version: alpha
name: VoltAgent
description: Deep-space command terminal aesthetic for an AI agent engineering platform — carbon-black canvas, single emerald green accent, warm-charcoal containment borders, system-ui display + Inter UI + SFMono code.

colors:
  # Brand greens
  primary: "#00d992"
  primary-button-text: "#2fd6a1"
  primary-link: "#10b981"

  # Secondary accents
  accent-purple: "#818cf8"
  accent-cobalt: "#306cce"
  accent-cobalt-deep: "#2554a0"
  focus-ring: "#3b82f6"

  # Surface & background
  background: "#050507"
  surface: "#101010"
  border: "#3d3a39"

  # Neutrals & text
  ink: "#f2f2f2"
  ink-strong: "#ffffff"
  on-surface-secondary: "#b8b3b0"
  on-surface-tertiary: "#8b949e"
  footer-link: "#bdbdbd"
  link-secondary: "#dcdcdc"
  ink-near-white: "#eeeeee"

  # Semantic
  success: "#008b00"
  success-soft: "#80d280"
  warning: "#ffba00"
  warning-soft: "#ffdd80"
  danger: "#fb565b"
  danger-soft: "#fd9c9f"
  info: "#4cb3d4"
  diagram-border: "#7d869f"  # was rgba(79,93,117,0.4) — Google format requires hex

  # Shadow tints (opaque approximations)
  shadow-warm: "#5c5855"   # was rgba(92,88,85,0.2) — flattened for hex
  shadow-deep: "#000000"   # was rgba(0,0,0,0.7) — flattened
  shadow-inset: "#94a3b8"  # was rgba(148,163,184,0.1) — flattened
  hover-darken: "#000000"  # was rgba(0,0,0,0.2)

typography:
  display-hero:
    fontFamily: "system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif"
    fontSize: 60px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: -0.65px
  section-heading:
    fontFamily: "system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.11
    letterSpacing: -0.9px
  sub-heading:
    fontFamily: "system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 700
    lineHeight: 1.33
    letterSpacing: -0.6px
  overline:
    fontFamily: "system-ui, -apple-system, Segoe UI, Roboto, Helvetica, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.5px
  feature-title:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0px
  overline-small:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.56
    letterSpacing: 0.45px
  body:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  nav-link:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 14.45px
    fontWeight: 500
    lineHeight: 1.65
    letterSpacing: 0px
  caption:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0px
  tag-overline:
    fontFamily: "system-ui, -apple-system, Segoe UI, Roboto, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 2.52px
  micro:
    fontFamily: "Inter, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0px
  code-body:
    fontFamily: "SFMono-Regular, Menlo, Monaco, Consolas, monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0px
  code-small:
    fontFamily: "SFMono-Regular, Menlo, Monaco, Consolas, monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
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
  5xl: 48px
  6xl: 64px

rounded:
  sharp: 4px
  sm: 6px
  code: 6.4px
  md: 8px
  pill: 9999px

components:
  # Buttons
  button-ghost:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink-strong}"
    typography: "{typography.body}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
  button-ghost-hover:
    backgroundColor: "{colors.hover-darken}"
    textColor: "{colors.ink-strong}"

  button-primary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.primary-button-text}"
    typography: "{typography.body}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
  button-primary-hover:
    backgroundColor: "{colors.hover-darken}"
    textColor: "{colors.primary-button-text}"

  button-container:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 20px

  # Cards
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 24px
  card-accent:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: 24px
  card-diagram:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.md}"
    padding: 24px

  # Code blocks
  code-block:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.code-body}"
    rounded: "{rounded.code}"
    padding: 16px

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

  # Tags / badges
  tag-pill:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.tag-overline}"
    rounded: "{rounded.pill}"
    padding: 4px 12px

  # Inputs (inferred)
  input:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
  input-focus:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
---

# VoltAgent Design System

## Overview

VoltAgent's interface is a deep-space command terminal for the AI age — a developer-facing darkness built on near-pure-black surfaces (`{colors.background}`) where the only interruption is the electric pulse of emerald green energy. The entire experience evokes the feeling of staring into a high-powered IDE at 2am: dark, focused, and alive with purpose. This is not a friendly SaaS landing page — it's an engineering platform that announces itself through code snippets, architectural diagrams, and raw technical confidence.

The green accent (`{colors.primary}`) is used with surgical precision — it glows from headlines, borders, and interactive elements like a circuit board carrying a signal. Against the carbon-black canvas, this green reads as "power on" — a deliberate visual metaphor for an AI agent engineering platform. The supporting palette is built entirely from warm-neutral grays (`{colors.border}`, `{colors.on-surface-tertiary}`, `{colors.on-surface-secondary}`) that soften the darkness without introducing color noise, creating a cockpit-like warmth that pure blue-grays would lack.

Typography leans on the system font stack for headings — achieving maximum rendering speed and native-feeling authority — while Inter carries the body and UI text with geometric precision. Code blocks use SFMono-Regular, the same font developers see in their terminals, reinforcing the tool's credibility at every scroll.

**Key Characteristics:**
- Carbon-black canvas (`{colors.background}`) with warm-gray border containment (`{colors.border}`) — not cold or sterile
- Single-accent identity: Emerald Signal Green (`{colors.primary}`) as the sole chromatic energy source
- Dual-typography system: system-ui for authoritative headings, Inter for precise UI/body text, SFMono for code credibility
- Ultra-tight heading line-heights (1.0–1.11) creating dense, compressed power blocks
- Warm neutral palette that prevents the dark theme from feeling clinical
- Developer-terminal aesthetic where code snippets ARE the hero content
- Green glow effects (drop-shadow, border accents) that make UI elements feel electrically alive

## Colors

### Primary
- **Emerald Signal Green** (`{colors.primary}`): The core brand energy — used for accent borders, glow effects, and the highest-signal interactive moments. The "power-on" indicator of the entire interface.
- **VoltAgent Mint** (`{colors.primary-button-text}`): The button-text variant of the brand green — slightly warmer and more readable than pure Signal Green, used specifically for CTA text on dark surfaces.
- **Tailwind Emerald** (`{colors.primary-link}`): The ecosystem-standard green used for subtle background tints and link defaults. Bridges VoltAgent's custom palette with Tailwind's utility classes.

### Secondary & Accent
- **Soft Purple** (`{colors.accent-purple}`): A cool indigo-violet used sparingly for secondary categorization, code syntax highlights, and visual variety without competing with green.
- **Cobalt Primary** (`{colors.accent-cobalt}`): Docusaurus primary dark — used in documentation contexts for links and interactive focus states.
- **Deep Cobalt** (`{colors.accent-cobalt-deep}`): The darkest primary shade, reserved for pressed/active states in documentation UI.
- **Ring Blue** (`{colors.focus-ring}`): Tailwind's ring color, visible only during keyboard focus for accessibility compliance.

### Surface & Background
- **Abyss Black** (`{colors.background}`): The landing page canvas — a near-pure black with the faintest warm undertone, darker than most "dark themes" for maximum contrast with green accents.
- **Carbon Surface** (`{colors.surface}`): The primary card and button background — one shade lighter than Abyss, creating a barely perceptible elevation layer. Used across all contained surfaces.
- **Warm Charcoal Border** (`{colors.border}`): The signature containment color — not a cold gray but a warm, almost brownish dark tone that prevents borders from feeling harsh against the black canvas.

### Neutrals & Text
- **Snow White** (`{colors.ink}`): The primary text color on dark surfaces — not pure white but a softened, eye-friendly off-white. The most-used color on the site.
- **Pure White** (`{colors.ink-strong}`): Reserved for the highest-emphasis moments — ghost button text and maximum-contrast headings.
- **Warm Parchment** (`{colors.on-surface-secondary}`): Secondary body text — a warm light gray with a slight pinkish undertone that reads as "paper" against the dark canvas.
- **Steel Slate** (`{colors.on-surface-tertiary}`): Tertiary text, metadata, timestamps, and de-emphasized content. A cool blue-gray that provides clear hierarchy below Warm Parchment.
- **Fog Gray** (`{colors.footer-link}`): Footer links and supporting navigation text — brightens on hover to Pure White.

### Semantic & Accent
- **Success Emerald** (`{colors.success}`): Deep green for success states and positive confirmations.
- **Warning Amber** (`{colors.warning}`): Bright amber for warning alerts and caution states.
- **Danger Coral** (`{colors.danger}`): Vivid red for error states and destructive action warnings.
- **Info Teal** (`{colors.info}`): Cool teal-blue for informational callouts and tip admonitions.

**Glow Effects**: A `drop-shadow(0 0 2px {colors.primary})` animating to `drop-shadow(0 0 8px {colors.primary})` creates a pulsing "electric charge" on the VoltAgent bolt logo. The glow expands and contracts like a heartbeat.

## Typography

### Font Family
- **Primary (Headings)**: `system-ui` with native fallbacks
- **Secondary (Body/UI)**: `Inter`, OpenType features `"calt"`, `"rlig"`
- **Monospace (Code)**: `SFMono-Regular` with mono fallbacks

### Hierarchy

The complete type scale lives in the `typography:` token block above. Reference tokens directly (`{typography.display-hero}`, `{typography.body}`) rather than hardcoding values.

| Token | Use |
|---|---|
| `display-hero` | Maximum impact, compressed hero blocks |
| `section-heading` | Section heads with tightest letter-spacing |
| `sub-heading` | Bold sub-section markers at 24px |
| `overline` | Uppercase overline labels with positive tracking |
| `feature-title` | Card headings, feature names |
| `overline-small` | Uppercase section labels |
| `body` | Standard text, nav links, buttons |
| `nav-link` | Top navigation links |
| `caption` | Descriptions, metadata, badge text |
| `tag-overline` | Widest letter-spacing for uppercase tags |
| `micro` | Smallest sans-serif text |
| `code-body` | Inline code, terminal output |
| `code-small` | Tiny code references, line numbers |

### Principles
- **System-native authority**: Display headings use system-ui rather than a custom web font — the largest text renders instantly and inherits the OS's native personality.
- **Tight compression creates density**: Hero line-heights are extremely compressed (1.0) with negative letter-spacing, creating text blocks that feel like dense technical specifications.
- **Weight gradient, not weight contrast**: The system uses a gentle 300→400→500→600→700 progression. Bold (700) is reserved for sub-headings.
- **Uppercase is earned and wide**: When uppercase appears, it's always paired with generous letter-spacing (0.45px–2.52px).
- **OpenType by default**: Both system-ui and Inter enable `"calt"` and `"rlig"`.

## Layout

### Spacing System
The complete spacing scale lives in the `spacing:` token block above. Base unit is 8px with a fluid scale from 2px (micro) to 64px (6xl).

Button padding: `md lg` (12px 16px) standard. Card internal padding: `2xl`–`3xl`. Section vertical spacing: `6xl`+ between major sections.

### Grid & Container
- Max container width: ~1280–1440px, centered
- Hero: centered single-column with maximum breathing room
- Feature sections: alternating asymmetric layouts (code left / text right, then reversed)
- Logo marquee: full-width, breaking the container constraint
- Card grids: 2–3 column for feature showcases

### Whitespace Philosophy
- **Cinematic breathing room between sections**: massive vertical gaps create a "scroll-through-chapters" experience.
- **Dense within components**: cards and code blocks are internally compact.
- **Border-defined separation**: the Warm Charcoal border system delineates content zones — the border IS the whitespace signal.
- **Hero-first hierarchy**: the top of the page commands the most space.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat (Level 0) | No shadow, no border | Page background, inline text |
| Contained (Level 1) | `1px solid {colors.border}` | Standard cards, nav bar, code blocks |
| Emphasized (Level 2) | `3px solid {colors.border}` | Large interactive buttons, emphasized containers |
| Accent (Level 3) | `2px solid {colors.primary}` | Active/highlighted feature cards, selected states |
| Ambient Glow (Level 4) | warm diffused shadow `{colors.shadow-warm}` | Elevated cards, hover states |
| Dramatic Float (Level 5) | deep `{colors.shadow-deep}` + inset `{colors.shadow-inset}` | Hero feature showcases, modals |

**Shadow Philosophy**: VoltAgent communicates depth primarily through **border weight and color**, not shadows. The standard `1px solid {colors.border}` IS the elevation — adding a `3px` weight or switching to green communicates importance more than adding shadow does. When shadows do appear, they're either warm and diffused or cinematic and dramatic — never medium or generic.

## Shapes

| Token | Value | Use |
|---|---|---|
| `sharp` | 4px | Small inline elements, SVG containers, code spans |
| `sm` | 6px | Buttons, links, clipboard actions — workhorse interactive radius |
| `code` | 6.4px | Code blocks, `pre` elements, clipboard targets — micro-distinction from `sm` |
| `md` | 8px | Content cards, feature containers, emphasized buttons |
| `pill` | 9999px | Tags, badges, status indicators |

## Components

The complete component spec lives in the `components:` token block above. Reference tokens directly (`{components.button-primary}`, `{components.card}`) rather than reconstructing them.

### Buttons
- **`button-ghost`** — transparent ghost button with thin warm-charcoal border. Default interactive element.
- **`button-primary`** — Carbon Surface background, VoltAgent Mint text. The "powered on" CTA.
- **`button-container`** — generous padding, thick `3px` warm-charcoal border for card-like buttons (code copy blocks, feature CTAs).

### Cards & Containers
- **`card`** — `1px solid {colors.border}` standard containment.
- **`card-accent`** — `2px solid {colors.primary}` for highlighted/active features.
- **`card-diagram`** — dashed `{colors.diagram-border}` border for workflow/architecture diagrams.

### Code Blocks
- **`code-block`** — Carbon Surface background, SFMono content, copy-to-clipboard affordance. Functions as primary visual content, not supporting illustration.

### Navigation
- Sticky top nav bar on Abyss Black canvas
- VoltAgent bolt icon with animated green glow on the left
- Snow White nav links at 14–16px Inter, weight 500
- GitHub stars badge integrated as social proof

### Tags / Badges
- **`tag-pill`** — Carbon Surface fill with WiredMono-style uppercase mono, wide letter-spacing.

### Inputs
Inferred Carbon Surface background, Warm Charcoal border, VoltAgent Mint focus ring, Snow White text. Sharp rectangular treatment.

## Do's and Don'ts

### Do
- Use Abyss Black (`{colors.background}`) as the page background and Carbon Surface (`{colors.surface}`) for all contained elements
- Reserve Emerald Signal Green (`{colors.primary}`) exclusively for high-signal moments
- Use VoltAgent Mint (`{colors.primary-button-text}`) for button text on dark surfaces
- Keep heading line-heights compressed (1.0–1.11) with negative letter-spacing
- Use the warm gray palette for borders and secondary text
- Present code snippets as primary content
- Use border weight (1px → 2px → 3px) and color shifts to communicate depth
- Pair system-ui for headings with Inter for body
- Use SFMono-Regular for all code content
- Apply `"calt"` and `"rlig"` OpenType features

### Don't
- Don't use bright or light backgrounds as primary surfaces
- Don't introduce warm colors (orange, red, yellow) as decorative accents — reserve for semantic states only
- Don't use Emerald Signal Green on large surfaces or as background fills — it's an accent
- Don't increase heading line-heights beyond 1.33
- Don't use heavy shadows generously — depth comes from border treatment
- Don't use pure white as default body text
- Don't mix in serif or decorative fonts
- Don't use border-radius larger than 8px on content cards
- Don't skip the warm-gray border system
- Don't animate aggressively — slow and subtle only

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Small Mobile | <420px | Minimum layout, stacked everything, reduced hero text to ~24px |
| Mobile | 420–767px | Single column, hamburger nav, full-width cards, hero text ~36px |
| Tablet | 768–1024px | 2-column grids begin, condensed nav, medium hero text |
| Desktop | 1025–1440px | Full multi-column layout, expanded nav with dropdowns, large hero (60px) |
| Large Desktop | >1440px | Max-width container centered (~1280–1440px), generous horizontal margins |

*23 breakpoints detected in total, ranging from 360px to 1992px — indicating a fluid, heavily responsive grid system rather than fixed breakpoint snapping.*

### Touch Targets
- Buttons use comfortable padding (12px 16px minimum) ensuring adequate touch area
- Navigation links spaced with sufficient gap for thumb navigation
- Interactive card surfaces are large enough to serve as full touch targets
- Minimum recommended touch target: 44x44px

### Collapsing Strategy
- **Navigation**: Full horizontal nav with dropdowns collapses to hamburger menu on mobile
- **Feature grids**: 3-column → 2-column → single-column vertical stacking
- **Hero text**: 60px → 36px → 24px progressive scaling with maintained compression ratios
- **Logo marquee**: Adjusts scroll speed and item sizing; maintains infinite loop
- **Code blocks**: Horizontal scroll on smaller viewports rather than wrapping
- **Section padding**: Reduces proportionally but maintains generous vertical rhythm
- **Cards**: Stack vertically on mobile with full-width treatment

### Image Behavior
- Dark-themed screenshots and diagrams scale proportionally within containers
- Agent flow diagrams simplify or scroll horizontally on narrow viewports
- Dot-pattern decorative backgrounds scale with viewport
- No visible art direction changes between breakpoints
- Lazy loading for below-fold images

---

## Agent Prompt Guide

### Quick Color Reference
- Brand Accent: "Emerald Signal Green (`{colors.primary}`)"
- Button Text: "VoltAgent Mint (`{colors.primary-button-text}`)"
- Page Background: "Abyss Black (`{colors.background}`)"
- Card Surface: "Carbon Surface (`{colors.surface}`)"
- Border / Containment: "Warm Charcoal (`{colors.border}`)"
- Primary Text: "Snow White (`{colors.ink}`)"
- Secondary Text: "Warm Parchment (`{colors.on-surface-secondary}`)"
- Tertiary Text: "Steel Slate (`{colors.on-surface-tertiary}`)"

### Example Component Prompts
- "Create a feature card on Carbon Surface (`{colors.surface}`) with a 1px solid Warm Charcoal (`{colors.border}`) border, comfortably rounded corners (8px). Use Snow White (`{colors.ink}`) for the title in system-ui at 24px weight 700, and Warm Parchment (`{colors.on-surface-secondary}`) for the description in Inter at 16px. Add a subtle warm ambient shadow."
- "Design a ghost button with transparent background, Snow White (`{colors.ink}`) text in Inter at 16px, a 1px solid Warm Charcoal (`{colors.border}`) border, and subtly rounded corners (6px). Padding: 12px vertical, 16px horizontal."
- "Build a hero section on Abyss Black (`{colors.background}`) with a massive heading at 60px system-ui, line-height 1.0, letter-spacing -0.65px. The word 'Platform' should be colored in Emerald Signal Green (`{colors.primary}`). Below the heading, place a code block showing 'npm create voltagent-app@latest' in SFMono-Regular at 14px on Carbon Surface."
- "Create a highlighted feature card using a 2px solid Emerald Signal Green (`{colors.primary}`) border instead of the standard Warm Charcoal. Keep Carbon Surface background, comfortably rounded corners (8px)."
- "Design a navigation bar on Abyss Black (`{colors.background}`) with the VoltAgent logo (bolt icon with animated green glow) on the left, nav links in Inter at 14px weight 500 in Snow White, and a green CTA button on the right."

### Iteration Guide
1. Focus on ONE component at a time
2. Reference specific color names and hex codes — "use Warm Parchment (`{colors.on-surface-secondary}`)" not "make it lighter"
3. Use border treatment to communicate elevation
4. Describe the desired "feel" alongside measurements
5. For glow effects, specify "Emerald Signal Green (`{colors.primary}`) as a drop-shadow with 2–8px blur"
6. Always specify which font — system-ui for headings, Inter for body/UI, SFMono-Regular for code
7. Keep animations slow and subtle
