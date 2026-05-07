---
version: alpha
name: OpenCode
description: Terminal-native monospace-first design with warm near-black canvas, Berkeley Mono throughout, and zero shadows — depth via warm transparent borders only.

colors:
  # Canvas (warm dark)
  background: "#201d1d"
  surface: "#302c2c"
  surface-light: "#f1eeee"
  surface-input: "#f8f7f7"

  # Ink
  ink: "#fdfcfc"
  ink-inverted: "#201d1d"
  text-secondary: "#9a9898"
  text-muted: "#6e6e73"
  text-secondary-light: "#424245"

  # Brand accent (system blue plays primary role)
  primary: "#007aff"
  primary-hover: "#0056b3"
  primary-active: "#004085"
  on-primary: "#fdfcfc"

  # Semantic
  danger: "#ff3b30"
  danger-hover: "#d70015"
  danger-active: "#a50011"
  success: "#30d158"
  warning: "#ff9f0a"
  warning-hover: "#cc7f08"
  warning-active: "#995f06"

  # Borders — warm transparent flattened to opaque approximations
  border: "#2c2424"  # was rgba(15,0,0,0.12) — flattened over #201d1d
  border-tab: "#9a9898"
  border-outline: "#646262"
  border-light: "#dad6d6"  # was rgba(15,0,0,0.12) — flattened over #f8f7f7

typography:
  display-hero:
    fontFamily: "Berkeley Mono, IBM Plex Mono, ui-monospace, SFMono-Regular, Menlo, Monaco, monospace"
    fontSize: 38px
    fontWeight: 700
    lineHeight: 1.5
    letterSpacing: 0px
  heading:
    fontFamily: "Berkeley Mono, IBM Plex Mono, ui-monospace, SFMono-Regular, Menlo, Monaco, monospace"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.5
    letterSpacing: 0px
  body:
    fontFamily: "Berkeley Mono, IBM Plex Mono, ui-monospace, SFMono-Regular, Menlo, Monaco, monospace"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  body-medium:
    fontFamily: "Berkeley Mono, IBM Plex Mono, ui-monospace, SFMono-Regular, Menlo, Monaco, monospace"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0px
  body-tight:
    fontFamily: "Berkeley Mono, IBM Plex Mono, ui-monospace, SFMono-Regular, Menlo, Monaco, monospace"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.0
    letterSpacing: 0px
  caption:
    fontFamily: "Berkeley Mono, IBM Plex Mono, ui-monospace, SFMono-Regular, Menlo, Monaco, monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 2.0
    letterSpacing: 0px

spacing:
  micro: 1px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 20px
  2xl: 24px
  3xl: 32px
  4xl: 48px
  5xl: 64px
  6xl: 96px

rounded:
  none: 0px
  sm: 4px
  md: 6px
  pill: 9999px

components:
  # Primary button — dark fill on dark page
  button-primary:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.body-medium}"
    rounded: "{rounded.sm}"
    padding: 4px 20px

  # Email/text input
  input:
    backgroundColor: "{colors.surface-input}"
    textColor: "{colors.ink-inverted}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 20px

  # Link variants
  link-default:
    textColor: "{colors.ink-inverted}"
    typography: "{typography.body-medium}"
    backgroundColor: "{colors.surface-light}"
    padding: 0px

  link-light:
    textColor: "{colors.ink}"
    typography: "{typography.body-medium}"
    backgroundColor: "{colors.background}"
    padding: 0px

  link-muted:
    textColor: "{colors.text-secondary}"
    typography: "{typography.body}"
    backgroundColor: "{colors.background}"
    padding: 0px

  # Tab
  tab-active:
    textColor: "{colors.ink}"
    typography: "{typography.body-tight}"
    backgroundColor: "{colors.background}"
    padding: 8px 12px

  # Navigation
  nav-bar:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.body-medium}"
    padding: 16px 24px

  # Card / container
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: 24px
---

# OpenCode Design System

## Overview

OpenCode's website embodies a terminal-native, monospace-first aesthetic that reflects its identity as an open source AI coding agent. The entire visual system is built on a stark dark-on-light contrast using a near-black background (`{colors.background}`) with warm off-white text (`{colors.ink}`). This isn't a generic dark theme — it's a warm, slightly reddish-brown dark that feels like a sophisticated terminal emulator rather than a cold IDE. The warm undertone in both the darks and lights (notice the subtle red channel in `{colors.background}` — rgb(32, 29, 29)) creates a cohesive, lived-in quality.

Berkeley Mono is the sole typeface, establishing an unapologetic monospace identity. Every element — headings, body text, buttons, navigation — shares this single font family, creating a unified "everything is code" philosophy. The heading at 38px bold with 1.50 line-height is generous and readable, while body text at 16px with weight 500 provides a slightly heavier-than-normal reading weight that enhances legibility on screen. The monospace grid naturally enforces alignment and rhythm across the layout.

The color system is deliberately minimal. The primary palette consists of just three functional tones: the warm near-black (`{colors.background}`), a medium warm gray (`{colors.text-secondary}`), and a bright off-white (`{colors.ink}`). Semantic colors borrow from the Apple HIG palette — blue accent (`{colors.primary}`), red danger (`{colors.danger}`), green success (`{colors.success}`), orange warning (`{colors.warning}`) — giving the interface familiar, trustworthy signal colors without adding brand complexity. Borders use a subtle warm transparency (`{colors.border}`) that ties into the warm undertone of the entire system.

**Key Characteristics:**
- Berkeley Mono as the sole typeface — monospace everywhere, no sans-serif or serif voices
- Warm near-black primary (`{colors.background}`) with reddish-brown undertone, not pure black
- Off-white text (`{colors.ink}`) with warm tint, not pure white
- Minimal 4px border radius throughout — sharp, utilitarian corners
- 8px base spacing system scaling up to 96px
- Apple HIG-inspired semantic colors (blue, red, green, orange)
- Transparent warm borders flattened to `{colors.border}`
- Email input with generous 20px padding and 6px radius — the most generous component radius
- Single button variant: dark background, light text, tight vertical padding (4px 20px)
- Underlined links as default link style, reinforcing the text-centric identity

## Colors

### Primary
- **OpenCode Dark** (`{colors.background}`): Primary background, button fills, link text. A warm near-black with subtle reddish-brown warmth — rgb(32, 29, 29).
- **OpenCode Light** (`{colors.ink}`): Primary text on dark surfaces, button text. A barely-warm off-white that avoids clinical pure white.
- **Mid Gray** (`{colors.text-secondary}`): Secondary text, muted links. A neutral warm gray that bridges dark and light.

### Secondary
- **Dark Surface** (`{colors.surface}`): Slightly lighter than primary dark, used for elevated surfaces and subtle differentiation.
- **Border Gray** (`{colors.border-outline}`): Stronger borders, outline rings on interactive elements.
- **Light Surface** (`{colors.surface-light}`): Light mode surface, subtle background variation.

### Accent
- **Accent Blue** (`{colors.primary}`): Primary accent, links, interactive highlights. Apple system blue.
- **Accent Blue Hover** (`{colors.primary-hover}`): Darker blue for hover states.
- **Accent Blue Active** (`{colors.primary-active}`): Deepest blue for pressed/active states.

### Semantic
- **Danger Red** (`{colors.danger}`): Error states, destructive actions. Apple system red.
- **Danger Hover** (`{colors.danger-hover}`): Darker red for hover on danger elements.
- **Danger Active** (`{colors.danger-active}`): Deepest red for pressed danger states.
- **Success Green** (`{colors.success}`): Success states, positive feedback. Apple system green.
- **Warning Orange** (`{colors.warning}`): Warning states, caution signals. Apple system orange.
- **Warning Hover** (`{colors.warning-hover}`): Darker orange for hover on warning elements.
- **Warning Active** (`{colors.warning-active}`): Deepest orange for pressed warning states.

### Text Scale
- **Text Muted** (`{colors.text-muted}`): Muted labels, disabled text, placeholder content.
- **Text Secondary Light** (`{colors.text-secondary-light}`): Secondary text on light backgrounds, captions.

### Border
- **Border Warm** (`{colors.border}`): Primary border color, warm transparent black flattened to opaque.
- **Border Tab** (`{colors.border-tab}`): Tab underline border, 2px solid bottom.
- **Border Outline** (`{colors.border-outline}`): 1px solid outline border for containers.

## Typography

### Font Family
- **Universal**: `Berkeley Mono`, with fallbacks: `IBM Plex Mono, ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace`

### Hierarchy

The complete type scale lives in the `typography:` token block above. Reference tokens directly.

| Token | Use |
|---|---|
| `display-hero` | Hero headlines, page titles |
| `heading` | Section titles, bold emphasis |
| `body` | Standard body text, paragraphs |
| `body-medium` | Links, button text, nav items |
| `body-tight` | Compact labels, tab items |
| `caption` | Footnotes, metadata, small labels |

### Principles
- **One font, one voice**: Berkeley Mono is used exclusively. There is no typographic variation between display, body, and code — everything speaks in the same monospace register. Hierarchy is achieved through size and weight alone.
- **Weight as hierarchy**: 700 for headings, 500 for interactive/medium emphasis, 400 for body text. Three weight levels create the entire hierarchy.
- **Generous line-height**: 1.50 as the standard line-height gives text room to breathe within the monospace grid. The relaxed 2.00 line-height on captions creates clear visual separation.
- **Tight for interaction**: Interactive elements (tabs, compact labels) use 1.00 line-height for dense, clickable targets.

## Layout

### Spacing System
The complete spacing scale lives in the `spacing:` token block above. Base unit is 8px with extended scale up to 96px.

### Grid & Container
- Max content width: approximately 800-900px (narrow, reading-optimized)
- Single-column layout as the primary pattern
- Centered content with generous horizontal margins
- Hero section: full-width dark terminal element
- Feature sections: single-column text blocks
- Footer: multi-column link grid

### Whitespace Philosophy
- **Monospace rhythm**: The fixed-width nature of Berkeley Mono creates a natural vertical grid. Line-heights of 1.50 and 2.00 maintain consistent rhythm.
- **Narrow and focused**: Content is constrained to a narrow column, creating generous side margins that focus attention on the text.
- **Sections through spacing**: No decorative dividers. Sections are separated by generous vertical spacing (`4xl`–`6xl`) rather than borders or background changes.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat (Level 0) | No shadow, no border | Default state for most elements |
| Border Subtle (Level 1) | `1px solid {colors.border}` | Section dividers, input borders, horizontal rules |
| Border Tab (Level 2) | `2px solid {colors.border-tab}` bottom only | Active tab indicator |
| Border Outline (Level 3) | `1px solid {colors.border-outline}` | Container outlines, elevated elements |

**Shadow Philosophy**: OpenCode's depth system is intentionally flat. There are no box-shadows in the extracted tokens — zero shadow values. Depth is communicated exclusively through border treatments and background color shifts. This flatness is consistent with the terminal aesthetic: terminals don't have shadows, and neither does OpenCode. The three border levels (transparent warm, tab indicator, solid outline) create sufficient visual hierarchy without any elevation illusion.

## Shapes

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Edge-to-edge sections |
| `sm` | 4px | Default for all elements — buttons, containers, badges |
| `md` | 6px | Form inputs (the most generous radius in the system) |
| `pill` | 9999px | Rare, reserved for circular elements |

The entire system uses just two utility radius values — 4px and 6px — reinforcing the utilitarian aesthetic.

## Components

The complete component spec lives in the `components:` token block above. Reference component tokens directly.

### Buttons
- **`button-primary`** — Dark fill matching the page background, light text, 4px radius, 4px 20px padding. The single button pattern.

### Inputs
- **`input`** — Light background (`{colors.surface-input}`) on dark page, 1px warm border, 6px radius, 20px padding. Used for newsletter/waitlist email capture.

### Links
- **`link-default`** — Dark text with 1px underline on light backgrounds.
- **`link-light`** — Light text with no decoration on dark backgrounds.
- **`link-muted`** — Mid-gray text for footer/secondary navigation.

### Tabs
- **`tab-active`** — `2px solid {colors.border-tab}` bottom border, weight 500 at line-height 1.0.

### Navigation
- **`nav-bar`** — Solid dark surface matching page background. Berkeley Mono throughout. Brand logotype left-aligned. No backdrop blur or transparency.

## Do's and Don'ts

### Do
- Use Berkeley Mono exclusively — never introduce a second typeface
- Keep surfaces flat: no shadows, no gradients, no blur effects
- Use warm-tinted darks and lights — `{colors.background}` not pure black, `{colors.ink}` not pure white
- Set border radius to 4px everywhere except inputs (6px)
- Follow Apple HIG for semantic color (blue, red, green, orange) with three-stage hover sequences
- Tie borders to the warm palette via `{colors.border}` — not neutral gray
- Keep spacing on an 8px grid: 8, 16, 24, 32, 40, 48, 64, 80, 96px. Use 4px for fine adjustments only
- Underline default links to reinforce the text-centric identity

### Don't
- Don't introduce non-monospace typefaces — the single-font philosophy is core
- Don't use box-shadows — depth is borders and background shifts only
- Don't use cool grays for borders — the system is warm-tinted throughout
- Don't use rounded pill buttons — corners are sharp and utilitarian
- Don't add hover scale or transform animations — interactions are color-shift only

---

## Responsive Behavior

*(Preserved from original 9-section format — Google's parser keeps unknown sections.)*

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile | <640px | Single column, reduced padding, heading scales down |
| Tablet | 640-1024px | Content width expands, slight padding increase |
| Desktop | >1024px | Full content width (~800-900px centered), maximum whitespace |

### Touch Targets
- Buttons with 4px 20px padding provide adequate horizontal touch area
- Input fields with 20px padding ensure comfortable mobile typing
- Tab items at 16px with tight line-height may need mobile adaptation

### Collapsing Strategy
- Hero heading: 38px → 28px → 24px on smaller screens
- Navigation: horizontal links → hamburger/drawer on mobile
- Feature lists: maintain single-column, reduce horizontal padding
- Terminal hero: maintain full-width, reduce internal padding
- Footer columns: multi-column → stacked single column
- Section spacing: 96px → 64px → 48px on mobile

### Image Behavior
- Terminal screenshots maintain aspect ratio and border treatment
- Full-width elements scale proportionally
- Monospace type maintains readability at all sizes due to fixed-width nature

---

## Agent Prompt Guide

*(Preserved from original 9-section format — the copy-paste payload section.)*

### Quick Color Reference
- Page background: `{colors.background}` (warm near-black)
- Primary text: `{colors.ink}` (warm off-white)
- Secondary text: `{colors.text-secondary}` (warm gray)
- Muted text: `{colors.text-muted}`
- Accent: `{colors.primary}` (blue)
- Danger: `{colors.danger}` (red)
- Success: `{colors.success}` (green)
- Warning: `{colors.warning}` (orange)
- Button bg: `{colors.background}`, button text: `{colors.ink}`
- Border: `{colors.border}` (warm transparent flattened)
- Input bg: `{colors.surface-input}`, input border: `{colors.border-light}`

### Example Component Prompts
- "Create a hero section on `{colors.background}` warm dark background. Headline at 38px Berkeley Mono weight 700, line-height 1.50, color `{colors.ink}`. Subtitle at 16px weight 400, color `{colors.text-secondary}`. Primary CTA button (`{colors.background}` bg with `1px solid {colors.border-outline}` border, 4px radius, 4px 20px padding, `{colors.ink}` text at weight 500)."
- "Design a feature list: single-column on `{colors.background}`. Feature name at 16px Berkeley Mono weight 700, color `{colors.ink}`. Description at 16px weight 400, color `{colors.text-secondary}`. No cards, no borders — pure text with 16px vertical gap between items."
- "Build an email capture form: `{colors.surface-input}` background input, `1px solid {colors.border-light}` border, 6px radius, 20px padding. Adjacent dark button (`{colors.background}` bg, `{colors.ink}` text, 4px radius, 4px 20px padding). Berkeley Mono throughout."
- "Create navigation: sticky `{colors.background}` background. 16px Berkeley Mono weight 500 for links, `{colors.ink}` text. Brand name left-aligned in monospace. Links with underline decoration. No blur, no transparency — solid dark surface."
- "Design a footer: `{colors.background}` background, multi-column link grid. Links at 16px Berkeley Mono weight 400, color `{colors.text-secondary}`. Section headers at weight 700. Border-top `1px solid {colors.border}` separator."

### Iteration Guide
1. Berkeley Mono is the only font — never introduce a second typeface. Size and weight create all hierarchy.
2. Keep surfaces flat: no shadows, no gradients, no blur effects. Use borders and background shifts only.
3. The warm undertone matters: use `{colors.background}` not `#000000`, use `{colors.ink}` not `#ffffff`. The reddish warmth is subtle but essential.
4. Border radius is 4px everywhere except inputs (6px). Never use rounded pills or large radii.
5. Semantic colors follow Apple HIG: `{colors.primary}` blue, `{colors.danger}` red, `{colors.success}` green, `{colors.warning}` orange. Each has hover and active darkened variants.
6. Three-stage interaction: default → hover (darkened) → active (deeply darkened) for all semantic colors.
7. Borders use `{colors.border}` — a warm transparent dark, not neutral gray. This ties borders to the warm palette.
8. Spacing follows an 8px grid: 8, 16, 24, 32, 40, 48, 64, 80, 96px. Use 4px for fine adjustments only.
