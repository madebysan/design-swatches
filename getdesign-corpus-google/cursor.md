---
version: alpha
name: Cursor
description: Warm minimalism meets code-editor elegance — warm off-white #f2f1ed canvas with #26251e warm near-black ink, three-font system (CursorGothic + jjannon serif + berkeleyMono), aggressive negative tracking on display, oklab-based borders, and a "thinking/grep/read/edit" timeline color set.

colors:
  # Primary canvas + ink
  background: "#f2f1ed"          # Cursor Cream / Surface 200
  surface: "#e6e5e0"             # Cursor Light / Surface 400
  surface-100: "#f7f7f4"
  surface-300: "#ebeae5"          # button default bg
  surface-500: "#e1e0db"
  surface-white: "#ffffff"
  surface-black: "#000000"
  ink: "#26251e"                 # Cursor Dark — warm near-black
  ink-inverted: "#f2f1ed"

  # Brand accent
  primary: "#f54e00"             # Cursor Orange
  gold: "#c08532"

  # Semantic
  error: "#cf2d56"               # warm crimson — also hover text color
  success: "#1f8a65"

  # Timeline / feature colors
  timeline-thinking: "#dfa88f"
  timeline-grep: "#9fc9a2"
  timeline-read: "#9fbbe0"
  timeline-edit: "#c0a8dd"

  # Text states
  on-background: "#26251e"
  on-surface: "#26251e"
  on-primary: "#ffffff"
  text-secondary: "#787165"      # opaque approx of rgba(38,37,30,0.55) over Cream — Google format requires hex
  text-muted: "#9c968b"          # opaque approx of rgba(38,37,30,0.6) over Cream

  # Borders (opaque approximations of oklab borders)
  border: "#dad7cf"  # was oklab(0.263 / 0.1) flattened over Cream — Google format requires hex
  border-medium: "#bcb8ad"  # was oklab(0.263 / 0.2)
  border-strong: "#787165"  # was rgba(38,37,30,0.55)
  border-solid: "#26251e"
  border-light: "#f2f1ed"

  # Shadow tints (opaque approximations)
  shadow-card: "#1a1a1a"  # was rgba(0,0,0,0.14) — flattened
  shadow-ambient: "#080808"

typography:
  display-hero:
    fontFamily: "CursorGothic, CursorGothic Fallback, system-ui, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 72px
    fontWeight: 400
    lineHeight: 1.10
    letterSpacing: -2.16px
  section-heading:
    fontFamily: "CursorGothic, CursorGothic Fallback, system-ui, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 36px
    fontWeight: 400
    lineHeight: 1.20
    letterSpacing: -0.72px
  sub-heading:
    fontFamily: "CursorGothic, CursorGothic Fallback, system-ui, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 26px
    fontWeight: 400
    lineHeight: 1.25
    letterSpacing: -0.325px
  title-small:
    fontFamily: "CursorGothic, CursorGothic Fallback, system-ui, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.30
    letterSpacing: -0.11px
  body-serif:
    fontFamily: "jjannon, Iowan Old Style, Palatino Linotype, ui-serif, Georgia, serif"
    fontSize: 19.2px
    fontWeight: 500
    lineHeight: 1.50
    letterSpacing: 0px
  body-serif-sm:
    fontFamily: "jjannon, Iowan Old Style, Palatino Linotype, ui-serif, Georgia, serif"
    fontSize: 17.28px
    fontWeight: 400
    lineHeight: 1.35
    letterSpacing: 0px
  body-sans:
    fontFamily: "CursorGothic, CursorGothic Fallback, system-ui, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0px
  button:
    fontFamily: "CursorGothic, CursorGothic Fallback, system-ui, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0px
  button-caption:
    fontFamily: "CursorGothic, CursorGothic Fallback, system-ui, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0.14px
  caption:
    fontFamily: "CursorGothic, CursorGothic Fallback, system-ui, Helvetica Neue, Helvetica, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0px
  system-heading:
    fontFamily: "system-ui, -apple-system, Segoe UI, Helvetica Neue, Arial, sans-serif"
    fontSize: 20px
    fontWeight: 700
    lineHeight: 1.55
    letterSpacing: 0px
  system-caption:
    fontFamily: "system-ui, -apple-system, Segoe UI, Helvetica Neue, Arial, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.33
    letterSpacing: 0px
  system-micro:
    fontFamily: "system-ui, -apple-system, Segoe UI, Helvetica Neue, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 500
    lineHeight: 1.27
    letterSpacing: 0.048px
  mono-body:
    fontFamily: "berkeleyMono, ui-monospace, SFMono-Regular, Menlo, Monaco, monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.67
    letterSpacing: 0px
  mono-small:
    fontFamily: "berkeleyMono, ui-monospace, SFMono-Regular, Menlo, Monaco, monospace"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: -0.275px

spacing:
  micro: 1.5px
  2xs: 2px
  xs: 3px
  sm: 4px
  md: 6px
  lg: 8px
  xl: 12px
  2xl: 16px
  3xl: 24px
  4xl: 32px
  5xl: 48px
  6xl: 64px
  7xl: 96px

rounded:
  none: 0px
  micro: 1.5px
  xs: 2px
  sm: 3px
  md: 4px
  lg: 8px
  featured: 10px
  pill: 9999px

components:
  # Top navigation
  nav-bar:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    padding: 12px 24px
  nav-link:
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    padding: 8px 12px

  # Primary warm-surface CTA
  button-primary:
    backgroundColor: "{colors.surface-300}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.lg}"
    padding: 10px 14px
  button-primary-hover:
    backgroundColor: "{colors.surface-300}"
    textColor: "{colors.error}"

  # Secondary pill
  button-pill:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text-muted}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 3px 8px
  button-pill-hover:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.error}"

  # Tertiary pill — active filter
  button-pill-active:
    backgroundColor: "{colors.surface-500}"
    textColor: "{colors.text-muted}"
    typography: "{typography.button}"
    rounded: "{rounded.pill}"
    padding: 3px 8px

  # Ghost (transparent)
  button-ghost:
    backgroundColor: "{colors.background}"
    textColor: "{colors.text-secondary}"
    typography: "{typography.button}"
    rounded: "{rounded.lg}"
    padding: 6px 12px

  # Light surface dropdown trigger
  button-light:
    backgroundColor: "{colors.surface-100}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.lg}"
    padding: 1px 12px

  # Card / container
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: 24px
  card-compact:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: 12px
  card-featured:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.featured}"
    padding: 32px

  # Form input
  input:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.body-sans}"
    rounded: "{rounded.lg}"
    padding: 8px 8px
  input-focus:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"

  # Code editor preview
  code-editor:
    backgroundColor: "{colors.surface-black}"
    textColor: "{colors.ink-inverted}"
    typography: "{typography.mono-body}"
    rounded: "{rounded.lg}"
    padding: 16px

  # AI timeline steps
  timeline-step-thinking:
    backgroundColor: "{colors.timeline-thinking}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 6px 10px
  timeline-step-grep:
    backgroundColor: "{colors.timeline-grep}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 6px 10px
  timeline-step-read:
    backgroundColor: "{colors.timeline-read}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 6px 10px
  timeline-step-edit:
    backgroundColor: "{colors.timeline-edit}"
    textColor: "{colors.ink}"
    typography: "{typography.button}"
    rounded: "{rounded.md}"
    padding: 6px 10px

  # Accent link
  link-accent:
    textColor: "{colors.primary}"
    typography: "{typography.body-sans}"
---

# Cursor Design System

## Overview

Cursor's website is a study in warm minimalism meets code-editor elegance. The entire experience is built on a warm off-white canvas (`{colors.background}`) with dark warm-brown text (`{colors.ink}`) — not pure black, not neutral gray, but a deeply warm near-black with a yellowish undertone that evokes old paper, ink, and craft. This warmth permeates every surface: backgrounds lean toward cream, borders dissolve into transparent warm overlays, and even the error state (`{colors.error}`) carries warmth rather than clinical red. The result feels more like a premium print publication than a tech website.

The custom CursorGothic font is the typographic signature — a gothic sans-serif with aggressive negative letter-spacing at display sizes (-2.16px at 72px) that creates a compressed, engineered feel. As a secondary voice, the jjannon serif font (with OpenType `"cswh"` contextual swash alternates) provides literary counterpoint for body copy and editorial passages. The monospace voice comes from berkeleyMono, a refined coding font that connects the marketing site to Cursor's core identity as a code editor. This three-font system gives Cursor one of the most typographically rich palettes in developer tooling.

The border system is particularly distinctive — Cursor uses `oklab()` color space for border colors, applying warm brown at various alpha levels to create borders that feel organic rather than mechanical. For Google's hex-only token format, these are flattened to opaque approximations (`{colors.border}`, `{colors.border-medium}`, `{colors.border-strong}`) that maintain visual consistency.

**Key Characteristics:**
- CursorGothic with aggressive negative letter-spacing (-2.16px at 72px, -0.72px at 36px)
- jjannon serif for body text with OpenType `"cswh"` (contextual swash alternates)
- berkeleyMono for code and technical labels
- Warm off-white background (`{colors.background}`) instead of pure white
- Primary text color `{colors.ink}` (warm near-black with yellow undertone)
- Accent orange `{colors.primary}` for brand highlight and links
- oklab-space borders flattened to opaque hex for Google format compatibility
- Pill-shaped elements with full-pill radius for tags and filters
- 8px base spacing system with fine-grained sub-8px increments

## Colors

### Primary
- **Cursor Dark** (`{colors.ink}`): Primary text, headings, dark UI surfaces. Warm near-black with yellow-brown undertone — the defining color.
- **Cursor Cream** (`{colors.background}`): Page background, primary surface. Warm cream that sets the entire warm tone.
- **Cursor Light** (`{colors.surface}`): Secondary surface, button backgrounds, card fills.
- **Pure White** (`{colors.surface-white}`): Used sparingly for maximum contrast.
- **True Black** (`{colors.surface-black}`): Minimal use, code/console contexts.

### Accent
- **Cursor Orange** (`{colors.primary}`): Brand accent. Vibrant red-orange for primary CTAs, active links, brand moments.
- **Gold** (`{colors.gold}`): Secondary accent for premium contexts.

### Semantic
- **Error** (`{colors.error}`): Warm crimson-rose. Also used as hover text color — the signature interaction shift.
- **Success** (`{colors.success}`): Muted teal-green, warm-shifted.

### Timeline / Feature Colors
- **Thinking** (`{colors.timeline-thinking}`): Warm peach.
- **Grep** (`{colors.timeline-grep}`): Soft sage green.
- **Read** (`{colors.timeline-read}`): Soft blue.
- **Edit** (`{colors.timeline-edit}`): Soft lavender.

### Surface Scale
- **Surface 100** (`{colors.surface-100}`): Lightest button/card surface.
- **Surface 200** (`{colors.background}`): Primary page background.
- **Surface 300** (`{colors.surface-300}`): Button default bg.
- **Surface 400** (`{colors.surface}`): Card backgrounds.
- **Surface 500** (`{colors.surface-500}`): Tertiary button bg, active state.

### Borders
- **Border Primary** (`{colors.border}`): Standard border, 10% warm brown (oklab, flattened).
- **Border Medium** (`{colors.border-medium}`): Emphasized border, 20% warm brown.
- **Border Strong** (`{colors.border-strong}`): Strong borders, table rules.
- **Border Solid** (`{colors.border-solid}`): Full-opacity dark border.
- **Border Light** (`{colors.border-light}`): Light border matching page background.

### Shadows & Depth
- **Card Shadow** (`{colors.shadow-card}`): Heavy elevated card with warm border ring.
- **Ambient Shadow** (`{colors.shadow-ambient}`): Subtle ambient glow for floating elements.

## Typography

### Font Families
- **Display/Headlines**: `CursorGothic`, fallbacks `CursorGothic Fallback, system-ui, Helvetica Neue, Helvetica, Arial`
- **Body/Editorial**: `jjannon`, fallbacks `Iowan Old Style, Palatino Linotype, ui-serif, Georgia`
- **Code/Technical**: `berkeleyMono`, fallbacks `ui-monospace, SFMono-Regular, Menlo, Monaco`
- **OpenType Features**: `"cswh"` on jjannon body text, `"ss09"` on CursorGothic buttons/captions

The complete type scale lives in the `typography:` token block above.

| Token | Use |
|---|---|
| `display-hero` | 72px CursorGothic with -2.16px tracking |
| `section-heading` | 36px section heading with -0.72px tracking |
| `sub-heading` | 26px sub-heading |
| `title-small` | 22px small title |
| `body-serif` | 19.2px jjannon editorial body |
| `body-serif-sm` | 17.28px jjannon standard body |
| `body-sans` | 16px CursorGothic UI body |
| `button` | 14px button label |
| `button-caption` | 14px button with `"ss09"` |
| `caption` | 11px small caption |
| `system-heading` | 20px system-ui heading |
| `system-caption` | 13px system-ui label |
| `system-micro` | 11px system-ui micro label |
| `mono-body` | 12px berkeleyMono |
| `mono-small` | 11px inline berkeleyMono |

### Principles
- **Gothic compression for impact**: CursorGothic at display uses -2.16px letter-spacing at 72px, progressively relaxing.
- **Serif for soul**: jjannon provides literary warmth. The `"cswh"` feature adds contextual swash alternates.
- **Three typographic voices**: Gothic (display/UI), serif (editorial/body), mono (code).
- **Weight restraint**: CursorGothic uses weight 400 almost exclusively, relying on size and tracking for hierarchy.

## Layout

### Spacing System
The complete spacing scale lives in the `spacing:` token block above. Base unit is 8px. Fine-grained sub-8px increments (1.5, 2, 3, 4, 6px) for precise icon/text alignment.

### Grid & Container
- Max content width: ~1200px
- Hero: centered single-column with generous top padding
- Feature sections: 2-3 column grids
- Full-width sections with warm cream or slightly darker backgrounds
- Sidebar layouts for documentation and settings pages

### Whitespace Philosophy
- **Warm negative space**: Cream background means whitespace has warmth and texture.
- **Compressed text, open layout**: Aggressive negative letter-spacing balanced by generous margins.
- **Section variation**: Alternating surface tones create subtle differentiation.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat (Level 0) | No shadow | Page background, text blocks |
| Border Ring (Level 1) | 1px ring with `{colors.border}` | Standard card/container border |
| Border Medium (Level 1b) | 1px ring with `{colors.border-medium}` | Emphasized borders, active states |
| Ambient (Level 2) | Soft ambient glow with `{colors.shadow-ambient}` | Floating elements, subtle glow |
| Elevated Card (Level 3) | Heavy 28px/70px blur drop shadow with `{colors.shadow-card}` + border ring | Modals, popovers, elevated cards |
| Focus | Subtle drop shadow on button focus | Interactive focus feedback |

**Shadow Philosophy**: Cursor's depth system is built around two ideas. First, borders use perceptually uniform oklab color space rather than rgba — flattened to opaque hex for Google compatibility while preserving the warm tone. Second, elevation shadows use dramatically large blur values (28px, 70px) with moderate opacity, creating diffused, atmospheric lift rather than hard-edged drop shadows. Cards don't feel like they float above the page — they feel like the page has gently opened a space for them.

## Shapes

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Sharp inline (rare) |
| `micro` | 1.5px | Fine detail elements |
| `xs` | 2px | Inline elements, code spans |
| `sm` | 3px | Small containers, inline badges |
| `md` | 4px | Cards, images, compact buttons |
| `lg` | 8px | Primary buttons, cards, menus |
| `featured` | 10px | Larger containers, featured cards |
| `pill` | 9999px | Pill buttons, tags, badges |

## Components

The complete component spec lives in the `components:` token block above.

### Buttons
- **`button-primary`** — Surface 300 fill with Cursor Dark text. Hover text shifts to `{colors.error}` warm crimson.
- **`button-pill`** — Surface 400 fill with muted text, full-pill radius. Tags, filters.
- **`button-pill-active`** — Surface 500 fill for active filter state.
- **`button-ghost`** — Cream bg with secondary text, 8px radius. Tertiary actions.
- **`button-light`** — Lightest surface (Surface 100) for dropdown triggers.

### Cards & Containers
- **`card`** — 8px radius standard card.
- **`card-compact`** — 4px radius for compact containers.
- **`card-featured`** — 10px radius for featured cards.
- Hover: shadow intensification (ambient → elevated).

### Inputs
- **`input`** — Transparent or surface, Border Primary.

### Distinctive Components

**AI Timeline**: Vertical timeline showing AI operations: thinking (peach), grep (sage), read (blue), edit (lavender). Each step uses its semantic color. Connected with vertical lines. Core visual metaphor for Cursor's AI-first coding experience. See `{components.timeline-step-thinking}`, `{components.timeline-step-grep}`, `{components.timeline-step-read}`, `{components.timeline-step-edit}`.

**Code Editor Previews**: Dark code editor screenshots with warm cream border frame. berkeleyMono for code text. See `{components.code-editor}`.

**Pricing Cards**: Warm surface backgrounds with bordered containers. Feature lists using jjannon serif for readability.

## Interaction & Motion

### Hover States
- Buttons: text color shifts to `{colors.error}` on hover — the signature warm crimson interaction.
- Links: color shift to accent orange (`{colors.primary}`) or underline decoration.
- Cards: shadow intensification (ambient → elevated).

### Focus States
- Shadow-based focus for depth-based focus indication
- Border focus uses Border Medium for input/form focus
- Consistent warm tone in all focus states — no cold blue focus rings

### Transitions
- Color transitions: 150ms ease for text/background color changes
- Shadow transitions: 200ms ease for elevation changes
- Transform: subtle scale or translate for interactive feedback

## Do's and Don'ts

### Do
- Always use warm tones — `{colors.background}` background, `{colors.ink}` text
- Apply proportional letter-spacing on CursorGothic: -2.16px at 72px, scaling with size
- Use the warm crimson `{colors.error}` for hover text shifts — signature interaction
- Use three fonts, three voices: CursorGothic display/UI, jjannon editorial, berkeleyMono code
- Use full pill (`{rounded.pill}`) for tags and filters; `{rounded.lg}` for primary buttons and cards
- Use atmospheric large-blur shadows for diffused depth
- Maintain the timeline color set for AI operations — peach/sage/blue/lavender
- Use jjannon serif for editorial/body content with `"cswh"` swash alternates

### Don't
- Don't use pure white or pure black for primary surfaces — warm cream and warm near-black only
- Don't use cool blue focus rings — focus is warm-toned
- Don't reduce CursorGothic display tracking — the negative letter-spacing IS the personality
- Don't substitute a generic monospace for berkeleyMono in code blocks
- Don't use sharp 0px corners on primary surfaces
- Don't use blur-less hard shadows — Cursor's shadows are soft and atmospheric
- Don't omit the timeline colors when showing AI operations

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|---|---|---|
| Mobile | <600px | Single column, reduced padding, stacked navigation |
| Tablet Small | 600-768px | 2-column grids begin |
| Tablet | 768-900px | Expanded card grids, sidebar appears |
| Desktop Small | 900-1279px | Full layout forming |
| Desktop | >1279px | Full layout, maximum content width |

### Touch Targets
- Buttons use comfortable padding (6-14px vertical, 8-14px horizontal)
- Pill buttons maintain tap-friendly sizing with 3-10px padding
- Navigation links at 14px with adequate spacing for touch

### Collapsing Strategy
- Hero: 72px → 36px → 26px on smaller screens, maintaining proportional letter-spacing
- Navigation: horizontal links → hamburger menu on mobile
- Feature cards: 3-column → 2-column → single column stacked
- Code editor screenshots: maintain aspect ratio, may shrink with border treatment preserved
- Timeline visualization: horizontal → vertical stacking
- Section spacing: 80px+ → 48px → 32px on mobile

### Image Behavior
- Editor screenshots maintain warm border treatment at all sizes
- AI timeline adapts from horizontal to vertical layout
- Product screenshots use responsive images with consistent border radius
- Full-width hero images scale proportionally

---

## Agent Prompt Guide

### Quick Color Reference
- Primary CTA background: `{colors.surface-300}` (warm cream button)
- Page background: `{colors.background}` (warm off-white)
- Text color: `{colors.ink}` (warm near-black)
- Secondary text: `{colors.text-secondary}` (warm brown)
- Accent: `{colors.primary}` (orange)
- Error/hover: `{colors.error}` (warm crimson)
- Success: `{colors.success}` (muted teal)
- Border: `{colors.border}` (warm brown 10%)

### Example Component Prompts
- "Create a hero section on `{colors.background}` warm cream background. Headline at 72px CursorGothic weight 400, line-height 1.10, letter-spacing -2.16px, color `{colors.ink}`. Subtitle at 17.28px jjannon weight 400, line-height 1.35, color `{colors.text-secondary}`. Primary CTA button (`{colors.surface-300}` bg, 8px radius, 10px 14px padding) with hover text shift to `{colors.error}`."
- "Design a card: `{colors.surface}` background, border 1px solid `{colors.border}`. Radius 8px. Title at 22px CursorGothic weight 400, letter-spacing -0.11px. Body at 17.28px jjannon weight 400, color `{colors.text-secondary}`. Use `{colors.primary}` for link accents."
- "Build a pill tag: `{colors.surface}` background, `{colors.text-muted}` text, full-pill radius (9999px), 3px 8px padding, 14px CursorGothic weight 400."
- "Create navigation: sticky `{colors.background}` background with backdrop-filter blur. 14px system-ui weight 500 for links, `{colors.ink}` text. CTA button right-aligned with `{colors.surface-300}` bg and 8px radius."
- "Design an AI timeline showing four steps: Thinking (`{colors.timeline-thinking}`), Grep (`{colors.timeline-grep}`), Read (`{colors.timeline-read}`), Edit (`{colors.timeline-edit}`). Each step: 14px label + vertical connecting line."

### Iteration Guide
1. Always use warm tones — `{colors.background}` background, `{colors.ink}` text, never pure white/black for primary surfaces
2. Letter-spacing scales with font size for CursorGothic: -2.16px at 72px, -0.72px at 36px, -0.325px at 26px, normal at 16px
3. Use opaque hex approximations of oklab borders — Google format requires hex
4. Three fonts, three voices: CursorGothic (display/UI), jjannon (editorial), berkeleyMono (code)
5. Pill shapes for tags and filters; 8px radius for primary buttons and cards
6. Hover states use `{colors.error}` text color — the warm crimson shift is a signature interaction
7. Shadows use large blur values for diffused atmospheric depth
8. The sub-8px spacing scale is critical for icon/text micro-alignment
