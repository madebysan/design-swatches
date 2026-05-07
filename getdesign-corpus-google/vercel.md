---
version: alpha
name: Vercel
description: Engineered minimalism — Geist Sans with extreme negative tracking, shadow-as-border (0 0 0 1px) replacing CSS borders, multi-layer card shadow stacks, workflow accent colors (red/pink/blue), pure-white canvas with Vercel Black text.

colors:
  # Canvas + ink
  background: "#ffffff"
  surface: "#ffffff"
  surface-soft: "#fafafa"
  ink: "#171717"
  ink-pure: "#000000"

  # Workflow accents — used only in workflow context
  primary: "#0a72ef"      # Develop Blue
  ship-red: "#ff5b4f"
  preview-pink: "#de1d8d"

  # Console / code colors
  console-blue: "#0070f3"
  console-purple: "#7928ca"
  console-pink: "#eb367f"

  # Interactive
  link-blue: "#0072f5"
  focus-blue: "#007aff"     # was hsla(212,100%,48%,1) — opaque equivalent
  ring-blue: "#bcdcfd"      # was rgba(147,197,253,.5) — flattened over white

  # Neutral scale
  gray-900: "#171717"
  gray-600: "#4d4d4d"
  gray-500: "#666666"
  gray-400: "#808080"
  gray-100: "#ebebeb"
  gray-50: "#fafafa"

  # On-color
  on-primary: "#ffffff"
  on-ink: "#ffffff"

  # Surface tints + overlays
  overlay-backdrop: "#fafafa"   # was hsla(0,0%,98%,1)
  selection-text: "#f2f2f2"     # was hsla(0,0%,95%,1)
  badge-blue-bg: "#ebf5ff"
  badge-blue-text: "#0068d6"

  # Shadow tints (opaque approximations)
  shadow-border: "#ebebeb"      # was rgba(0,0,0,.08) — flattened over white
  shadow-soft: "#f5f5f5"        # was rgba(0,0,0,.04) — flattened over white

typography:
  display-hero:
    fontFamily: "Geist, Arial, Apple Color Emoji, Segoe UI Emoji, Segoe UI Symbol, sans-serif"
    fontSize: 48px
    fontWeight: 600
    lineHeight: 1.00
    letterSpacing: -2.4px
  section-heading:
    fontFamily: "Geist, Arial, sans-serif"
    fontSize: 40px
    fontWeight: 600
    lineHeight: 1.20
    letterSpacing: -2.4px
  sub-heading-large:
    fontFamily: "Geist, Arial, sans-serif"
    fontSize: 32px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -1.28px
  sub-heading:
    fontFamily: "Geist, Arial, sans-serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: -1.28px
  card-title:
    fontFamily: "Geist, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: -0.96px
  card-title-light:
    fontFamily: "Geist, Arial, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: -0.96px
  body-large:
    fontFamily: "Geist, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.80
    letterSpacing: 0px
  body:
    fontFamily: "Geist, Arial, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.56
    letterSpacing: 0px
  body-small:
    fontFamily: "Geist, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0px
  body-medium:
    fontFamily: "Geist, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.50
    letterSpacing: 0px
  body-semibold:
    fontFamily: "Geist, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.50
    letterSpacing: -0.32px
  button-ui:
    fontFamily: "Geist, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0px
  button-small:
    fontFamily: "Geist, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.00
    letterSpacing: 0px
  caption:
    fontFamily: "Geist, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0px
  mono-body:
    fontFamily: "Geist Mono, ui-monospace, SFMono-Regular, Menlo, monospace"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0px
  mono-caption:
    fontFamily: "Geist Mono, ui-monospace, SFMono-Regular, Menlo, monospace"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.54
    letterSpacing: 0px
  mono-small:
    fontFamily: "Geist Mono, ui-monospace, SFMono-Regular, Menlo, monospace"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.00
    letterSpacing: 0px
  micro-badge:
    fontFamily: "Geist, Arial, sans-serif"
    fontSize: 10px
    fontWeight: 700
    lineHeight: 1.00
    letterSpacing: 0px

spacing:
  micro: 1px
  micro-2: 2px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 32px
  2xl: 40px
  3xl: 80px
  4xl: 120px

rounded:
  none: 0px
  micro: 2px
  xs: 4px
  sm: 6px
  md: 8px
  lg: 12px
  xl: 64px
  2xl: 100px
  pill: 9999px

components:
  # Primary dark CTA
  button-primary:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-ink}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.sm}"
    padding: 8px 16px

  # Secondary white with shadow-border
  button-secondary:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.sm}"
    padding: 8px 16px
    borderColor: "{colors.gray-100}"

  # Pill badge
  badge:
    backgroundColor: "{colors.badge-blue-bg}"
    textColor: "{colors.badge-blue-text}"
    typography: "{typography.caption}"
    rounded: "{rounded.pill}"
    padding: 0px 10px

  # Tab pill
  button-tab-pill:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.xl}"
    padding: 8px 16px

  # Standard card — shadow-bordered
  card:
    backgroundColor: "{colors.background}"
    rounded: "{rounded.md}"
    padding: 24px
    borderColor: "{colors.shadow-border}"

  # Featured / image card
  card-featured:
    backgroundColor: "{colors.background}"
    rounded: "{rounded.lg}"
    padding: 24px
    borderColor: "{colors.gray-100}"

  # Metric card — large display number
  card-metric:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.display-hero}"
    rounded: "{rounded.md}"
    padding: 32px
    borderColor: "{colors.shadow-border}"

  # Input
  input:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.body-small}"
    rounded: "{rounded.sm}"
    padding: 8px 12px
    borderColor: "{colors.gray-100}"
  input-focus:
    backgroundColor: "{colors.background}"
    borderColor: "{colors.focus-blue}"

  # Top nav bar
  nav-bar:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.button-ui}"
    padding: 16px 24px
    borderColor: "{colors.shadow-border}"

  # Workflow step — develop
  workflow-develop:
    textColor: "{colors.primary}"
    typography: "{typography.mono-small}"

  # Workflow step — preview
  workflow-preview:
    textColor: "{colors.preview-pink}"
    typography: "{typography.mono-small}"

  # Workflow step — ship
  workflow-ship:
    textColor: "{colors.ship-red}"
    typography: "{typography.mono-small}"
---

# Vercel Design System

## Overview

Vercel's website is the visual thesis of developer infrastructure made invisible — a design system so restrained it borders on philosophical. The page is overwhelmingly white (`{colors.background}`) with near-black (`{colors.ink}`) text, creating a gallery-like emptiness where every element earns its pixel. This isn't minimalism as decoration; it's minimalism as engineering principle. The Geist design system treats the interface like a compiler treats code — every unnecessary token is stripped away until only structure remains.

The custom Geist font family is the crown jewel. Geist Sans uses aggressive negative letter-spacing (-2.4px to -2.88px at display sizes), creating headlines that feel compressed, urgent, and engineered — like code that's been minified for production. At body sizes, the tracking relaxes but the geometric precision persists. Geist Mono completes the system as the monospace companion for code, terminal output, and technical labels. Both fonts enable OpenType `"liga"` (ligatures) globally, adding a layer of typographic sophistication that rewards close reading.

What distinguishes Vercel from other monochrome design systems is its shadow-as-border philosophy. Instead of traditional CSS borders, Vercel uses `box-shadow: 0 0 0 1px {colors.shadow-border}` — a zero-offset, zero-blur, 1px-spread shadow that creates a border-like line without the box model implications. This technique allows borders to exist in the shadow layer, enabling smoother transitions and rounded corners without clipping. The entire depth system is built on layered, multi-value shadow stacks where each layer serves a specific purpose: one for the border, one for soft elevation, one for ambient depth.

**Key Characteristics:**
- Geist Sans with extreme negative letter-spacing (-2.4px to -2.88px at display) — text as compressed infrastructure
- Geist Mono for code and technical labels with OpenType `"liga"` globally
- Shadow-as-border technique replacing traditional borders throughout
- Multi-layer shadow stacks for nuanced depth
- Near-pure white canvas with `{colors.ink}` text — not quite black, micro-contrast softness
- Workflow-specific accent colors: Ship Red (`{colors.ship-red}`), Preview Pink (`{colors.preview-pink}`), Develop Blue (`{colors.primary}`)
- Focus ring system using saturated blue
- Pill badges with tinted backgrounds for status indicators

## Colors

### Primary
- **Vercel Black** (`{colors.ink}`): Primary text, headings. Not pure black — the slight warmth prevents harshness.
- **Pure White** (`{colors.background}`): Page background, card surfaces, button text on dark.
- **True Black** (`{colors.ink-pure}`): Specific console/code contexts.

### Workflow Accent Colors
- **Ship Red** (`{colors.ship-red}`): The "ship to production" workflow step.
- **Preview Pink** (`{colors.preview-pink}`): The preview deployment workflow.
- **Develop Blue** (`{colors.primary}`): The development workflow.

### Console / Code Colors
- **Console Blue** (`{colors.console-blue}`): Syntax highlighting blue.
- **Console Purple** (`{colors.console-purple}`): Syntax highlighting purple.
- **Console Pink** (`{colors.console-pink}`): Syntax highlighting pink.

### Interactive
- **Link Blue** (`{colors.link-blue}`): Primary link color with underline.
- **Focus Blue** (`{colors.focus-blue}`): Focus ring on interactive elements.
- **Ring Blue** (`{colors.ring-blue}`): Tailwind ring utility.

### Neutral Scale
- **Gray 900** (`{colors.gray-900}`): Primary text, headings, nav text.
- **Gray 600** (`{colors.gray-600}`): Secondary text, description copy.
- **Gray 500** (`{colors.gray-500}`): Tertiary text, muted links.
- **Gray 400** (`{colors.gray-400}`): Placeholder text, disabled states.
- **Gray 100** (`{colors.gray-100}`): Borders, card outlines, dividers.
- **Gray 50** (`{colors.gray-50}`): Subtle surface tint, inner shadow highlight.

### Surface & Overlay
- **Overlay Backdrop** (`{colors.overlay-backdrop}`): Modal/dialog backdrop.
- **Selection Text** (`{colors.selection-text}`): Text selection highlight.
- **Badge Blue Bg** (`{colors.badge-blue-bg}`): Pill badge background.
- **Badge Blue Text** (`{colors.badge-blue-text}`): Pill badge text.

### Shadows & Depth
- **Shadow Border** (`{colors.shadow-border}`): The signature — replaces traditional borders.
- **Shadow Soft** (`{colors.shadow-soft}`): Minimal lift for cards.

## Typography

### Font Family
- **Primary**: `Geist`, with fallbacks: `Arial, sans-serif`
- **Monospace**: `Geist Mono`, with fallbacks: `ui-monospace, SFMono-Regular, Menlo, monospace`
- **OpenType Features**: `"liga"` enabled globally on all Geist text; `"tnum"` for tabular numbers on captions.

### Hierarchy

The complete type scale lives in the `typography:` token block above. Reference tokens directly (`{typography.display-hero}`, `{typography.body}`, etc.).

| Token | Use |
|---|---|
| `display-hero` | 48px hero — billboard impact, maximum compression |
| `section-heading` | Feature section titles |
| `sub-heading-large` | Card headings, sub-sections |
| `sub-heading` | Lighter sub-headings |
| `card-title` | Feature cards |
| `card-title-light` | Secondary card headings |
| `body-large` | Introductions, feature descriptions |
| `body` | Standard reading text |
| `body-small` | Standard UI text |
| `body-medium` | Navigation, emphasized text |
| `body-semibold` | Strong labels, active states |
| `button-ui` | Buttons, links, captions |
| `button-small` | Compact buttons |
| `caption` | Metadata, tags |
| `mono-body` | Code blocks |
| `mono-caption` | Code labels |
| `mono-small` | Uppercase technical labels |
| `micro-badge` | Tiny badges |

### Principles
- **Compression as identity**: Geist Sans at display sizes uses -2.4px to -2.88px tracking — the most aggressive negative tracking of any major design system. The tracking progressively relaxes as size decreases.
- **Ligatures everywhere**: Every Geist text element enables `"liga"`. Ligatures aren't decorative — they're structural.
- **Three weights, strict roles**: 400 (body/reading), 500 (UI/interactive), 600 (headings/emphasis). No bold (700) except tiny micro-badges.
- **Mono for identity**: Geist Mono in uppercase serves as the "developer console" voice — connecting marketing to product.

## Layout

### Spacing System
The complete scale lives in the `spacing:` token block above. Base unit is 8px. Notable: the scale jumps from `{spacing.lg}` (16px) to `{spacing.xl}` (32px) — no 20px or 24px in primary scale.

### Grid & Container
- Max content width: approximately 1200px
- Hero: centered single-column with generous top padding
- Feature sections: 2–3 column grids
- Full-width dividers using `border-bottom: 1px solid {colors.ink}`

### Whitespace Philosophy
- **Gallery emptiness**: Massive vertical padding between sections (`{spacing.3xl}`–`{spacing.4xl}`+). White space IS the design.
- **Compressed text, expanded space**: Aggressive negative tracking on headlines is counterbalanced by generous surrounding whitespace.
- **Section rhythm**: White sections alternate with white sections. Separation comes from shadow-borders and spacing alone.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat (Level 0) | No shadow | Page background, text blocks |
| Ring (Level 1) | `0 0 0 1px {colors.shadow-border}` | Shadow-as-border for most elements |
| Light Ring (Level 1b) | `0 0 0 1px {colors.gray-100}` | Lighter ring for tabs, images |
| Subtle Card (Level 2) | Ring + `0 2px 2px {colors.shadow-soft}` | Standard cards with minimal lift |
| Full Card (Level 3) | Ring + Subtle + `0 8px 8px -8px {colors.shadow-soft}` + inner `{colors.gray-50}` ring | Featured cards |
| Focus (Accessibility) | `2px solid {colors.focus-blue}` outline | Keyboard focus on all interactive elements |

**Shadow Philosophy**: Vercel has arguably the most sophisticated shadow system in modern web design. Multi-value shadow stacks where each layer has a distinct architectural purpose: one creates the "border" (0px spread, 1px), another adds ambient softness (2px blur), another handles depth at distance (8px blur with negative spread), and an inner ring (`{colors.gray-50}`) creates the subtle highlight that makes the card "glow" from within. Cards feel built, not floating.

### Decorative Depth
- Hero gradient: soft, pastel multi-color gradient wash behind hero content (barely visible, atmospheric)
- Section borders: 1px solid `{colors.ink}` between major sections
- No background color variation — depth comes entirely from shadow layering and border contrast

## Shapes

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Reserved |
| `micro` | 2px | Inline code snippets, small spans |
| `xs` | 4px | Small containers |
| `sm` | 6px | Buttons, links, functional elements |
| `md` | 8px | Cards, list items |
| `lg` | 12px | Featured cards, image containers |
| `xl` | 64px | Tab navigation pills |
| `2xl` | 100px | Large navigation links |
| `pill` | 9999px | Badges, status pills, tags |

## Components

The full component spec lives in the `components:` token block above. Reference tokens directly (`{components.button-primary}`, `{components.card}`).

### Buttons
- **`button-primary`** — Vercel Black, white text, `{rounded.sm}`. The default CTA.
- **`button-secondary`** — White surface with `{colors.gray-100}` shadow-border.
- **`button-tab-pill`** — Large pill (`{rounded.xl}`) for tab/section navigation.

### Pills & Badges
- **`badge`** — Tinted blue surface, blue text, full pill, 12px Geist weight 500.

### Cards
- **`card`** — White, shadow-as-border instead of CSS border. Multi-layer shadow stack for depth.
- **`card-featured`** — `{rounded.lg}` for featured/image cards. Image cards use 1px solid `{colors.gray-100}`.
- **`card-metric`** — Large number display (Geist 48px weight 600) with description below in gray.

### Inputs
- **`input`** — White surface, shadow-bordered. Focus uses `{colors.focus-blue}` 2px outline plus the focus ring shadow.

### Navigation
- **`nav-bar`** — Sticky white header. Geist 14px weight 500 links. Dark pill CTA right.

### Image Treatment
- Product screenshots with 1px solid `{colors.gray-100}` border
- Top-rounded images: `12px 12px 0px 0px` radius
- Soft pastel gradient backgrounds behind hero images

### Distinctive Components
- **Workflow Pipeline**: Three-step horizontal pipeline — Develop (blue) → Preview (pink) → Ship (red). Each step uses its workflow color and Geist Mono uppercase label.
- **Trust Bar / Logo Grid**: Company logos in grayscale with subtle gray-100 separation.
- **Metric Cards**: Large display numbers (48px Geist weight 600) over gray description.

## Do's and Don'ts

### Do
- Use Geist Sans with aggressive negative letter-spacing at display sizes (-2.4px to -2.88px at 48px)
- Use shadow-as-border (`0 0 0 1px {colors.shadow-border}`) instead of traditional CSS borders
- Enable `"liga"` on all Geist text — ligatures are structural
- Use the three-weight system: 400 (body), 500 (UI), 600 (headings)
- Apply workflow accent colors only in workflow context
- Use multi-layer shadow stacks for cards
- Keep the palette achromatic — grays from `{colors.ink}` to `{colors.background}`
- Use `{colors.ink}` instead of `{colors.ink-pure}` for primary text — the micro-warmth matters

### Don't
- Don't use positive letter-spacing on Geist Sans
- Don't use weight 700 on body text — 600 is the maximum
- Don't use traditional CSS `border` on cards — use shadow-border
- Don't introduce warm colors (oranges, yellows, greens) into UI chrome
- Don't apply workflow accent colors decoratively
- Don't use heavy shadows (>0.1 opacity) — the system is whisper-level
- Don't increase body text letter-spacing
- Don't use pill radius on primary action buttons — pills are for badges/tags
- Don't skip the inner `{colors.gray-50}` ring in card shadows — it's the glow that makes the system work

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile Small | <400px | Tight single column, minimal padding |
| Mobile | 400–600px | Standard mobile, stacked layout |
| Tablet Small | 600–768px | 2-column grids begin |
| Tablet | 768–1024px | Full card grids, expanded padding |
| Desktop Small | 1024–1200px | Standard desktop layout |
| Desktop | 1200–1400px | Full layout, maximum content width |
| Large Desktop | >1400px | Centered, generous margins |

### Touch Targets
- Buttons use comfortable padding (8px–16px vertical)
- Navigation links at 14px with adequate spacing
- Pill badges have 10px horizontal padding for tap targets
- Mobile menu toggle uses 50% radius circular button

### Collapsing Strategy
- Hero: display 48px → scales down, maintains negative tracking proportionally
- Navigation: horizontal links + CTAs → hamburger menu
- Feature cards: 3-column → 2-column → single column
- Code screenshots: maintain aspect ratio, may horizontally scroll
- Trust bar logos: grid → horizontal scroll
- Footer: multi-column → stacked single column
- Section spacing: 80px+ → 48px on mobile

### Image Behavior
- Dashboard screenshots maintain border treatment at all sizes
- Hero gradient softens/simplifies on mobile
- Product screenshots use responsive images with consistent border radius
- Full-width sections maintain edge-to-edge treatment

---

## Agent Prompt Guide

### Quick Color Reference
- Primary CTA: Vercel Black `{colors.ink}`
- Background: Pure White `{colors.background}`
- Heading text: Vercel Black `{colors.ink}`
- Body text: Gray 600 `{colors.gray-600}`
- Border (shadow): `0 0 0 1px {colors.shadow-border}`
- Link: Link Blue `{colors.link-blue}`
- Focus ring: Focus Blue `{colors.focus-blue}`

### Example Component Prompts
- "Create a hero section on white background. Headline at 48px Geist weight 600, line-height 1.00, letter-spacing -2.4px, color `{colors.ink}`. Subtitle at 20px Geist weight 400, line-height 1.80, color `{colors.gray-600}`. Dark CTA button (`{colors.ink}`, 6px radius, 8px 16px padding) and ghost button (white, shadow-border `0 0 0 1px {colors.shadow-border}`, 6px radius)."
- "Design a card: white background, no CSS border. Use shadow stack: `0 0 0 1px {colors.shadow-border}, 0 2px 2px {colors.shadow-soft}, 0 0 0 1px {colors.gray-50}` (inner). Radius 8px. Title at 24px Geist weight 600, letter-spacing -0.96px. Body at 16px weight 400, `{colors.gray-600}`."
- "Build a pill badge: `{colors.badge-blue-bg}` background, `{colors.badge-blue-text}` text, 9999px radius, 0px 10px padding, 12px Geist weight 500."
- "Create navigation: white sticky header. Geist 14px weight 500 for links, `{colors.ink}` text. Dark pill CTA 'Start Deploying' right-aligned. Shadow-border on bottom."
- "Design a workflow section showing three steps: Develop (text color `{colors.primary}`), Preview (`{colors.preview-pink}`), Ship (`{colors.ship-red}`). Each step: 14px Geist Mono uppercase label + 24px Geist weight 600 title + 16px weight 400 description in `{colors.gray-600}`."

### Iteration Guide
1. Always use shadow-as-border instead of CSS border — `0 0 0 1px {colors.shadow-border}` is the foundation
2. Letter-spacing scales with font size: -2.4px at 48px, -1.28px at 32px, -0.96px at 24px, normal at 14px
3. Three weights only: 400 (read), 500 (interact), 600 (announce)
4. Color is functional, never decorative — workflow colors mark pipeline stages only
5. The inner `{colors.gray-50}` ring in card shadows gives Vercel cards their subtle inner glow
6. Geist Mono uppercase for technical labels, Geist Sans for everything else
