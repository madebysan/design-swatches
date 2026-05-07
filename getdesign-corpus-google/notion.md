---
version: alpha
name: Notion
description: Warm-neutral minimalism with NotionInter's compressed display type, whisper-weight 1px borders, and the singular Notion Blue accent on a pure-white canvas.

colors:
  # Canvas and surfaces
  background: "#ffffff"
  surface: "#ffffff"
  surface-warm: "#f6f5f4"  # warm white section alternation
  surface-dark: "#31302e"  # warm dark section background

  # Ink — warm near-black instead of pure black
  ink: "#0d0d0d"  # was rgba(0,0,0,0.95) — flattened to opaque approx
  ink-inverted: "#ffffff"
  text-secondary: "#615d59"  # warm gray 500
  text-muted: "#a39e98"  # warm gray 300

  # Brand accent
  primary: "#0075de"  # Notion Blue
  primary-active: "#005bab"  # active/pressed
  on-primary: "#ffffff"

  # Secondary brand
  secondary: "#213183"  # deep navy

  # Semantic accents
  success: "#1aae39"
  success-teal: "#2a9d99"
  warning: "#dd5b00"
  accent-pink: "#ff64c8"
  accent-purple: "#391c57"
  accent-brown: "#523410"

  # Interactive
  link: "#0075de"
  link-light: "#62aef0"
  focus-ring: "#097fe8"
  badge-bg: "#f2f9ff"
  badge-text: "#097fe8"

  # Surfaces and borders
  surface-translucent: "#f2f2f2"  # was rgba(0,0,0,0.05) — flattened over white
  border: "#e6e6e6"  # was rgba(0,0,0,0.1) — flattened over white
  border-input: "#dddddd"

  # Shadow tint
  shadow-soft: "#ebebeb"  # was rgba(0,0,0,0.04) — flattened over white

typography:
  display-hero:
    fontFamily: "NotionInter, Inter, -apple-system, system-ui, sans-serif"
    fontSize: 64px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: -2.125px
  display-secondary:
    fontFamily: "NotionInter, Inter, -apple-system, system-ui, sans-serif"
    fontSize: 54px
    fontWeight: 700
    lineHeight: 1.04
    letterSpacing: -1.875px
  section-heading:
    fontFamily: "NotionInter, Inter, -apple-system, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: -1.5px
    fontFeature: "'lnum'"
  sub-heading-large:
    fontFamily: "NotionInter, Inter, -apple-system, system-ui, sans-serif"
    fontSize: 40px
    fontWeight: 700
    lineHeight: 1.5
    letterSpacing: 0px
  sub-heading:
    fontFamily: "NotionInter, Inter, -apple-system, system-ui, sans-serif"
    fontSize: 26px
    fontWeight: 700
    lineHeight: 1.23
    letterSpacing: -0.625px
  card-title:
    fontFamily: "NotionInter, Inter, -apple-system, system-ui, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: -0.25px
  body-large:
    fontFamily: "NotionInter, Inter, -apple-system, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: -0.125px
  body:
    fontFamily: "NotionInter, Inter, -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  body-medium:
    fontFamily: "NotionInter, Inter, -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0px
  body-semibold:
    fontFamily: "NotionInter, Inter, -apple-system, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.5
    letterSpacing: 0px
  nav-button:
    fontFamily: "NotionInter, Inter, -apple-system, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0px
  caption:
    fontFamily: "NotionInter, Inter, -apple-system, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.43
    letterSpacing: 0px
  badge:
    fontFamily: "NotionInter, Inter, -apple-system, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.33
    letterSpacing: 0.125px

spacing:
  micro: 2px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
  2xl: 32px
  3xl: 48px
  4xl: 64px
  5xl: 80px
  6xl: 120px

rounded:
  none: 0px
  micro: 4px
  subtle: 5px
  sm: 8px
  md: 12px
  lg: 16px
  pill: 9999px

components:
  # Primary blue CTA
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.nav-button}"
    rounded: "{rounded.micro}"
    padding: 8px 16px
  button-primary-hover:
    backgroundColor: "{colors.primary-active}"
    textColor: "{colors.on-primary}"

  # Secondary translucent
  button-secondary:
    backgroundColor: "{colors.surface-translucent}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-button}"
    rounded: "{rounded.micro}"
    padding: 8px 16px

  # Ghost / link
  button-ghost:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-button}"
    rounded: "{rounded.micro}"
    padding: 8px 16px

  # Pill badge
  badge-pill:
    backgroundColor: "{colors.badge-bg}"
    textColor: "{colors.badge-text}"
    typography: "{typography.badge}"
    rounded: "{rounded.pill}"
    padding: 4px 8px

  # Standard card
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: 24px
  card-featured:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: 32px

  # Form input
  input:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.micro}"
    padding: 6px

  # Top nav
  nav-bar:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.nav-button}"
    padding: 16px 24px
---

# Notion Design System

## Overview

Notion's website embodies the philosophy of the tool itself: a blank canvas that gets out of your way. The design system is built on warm neutrals rather than cold grays, creating a distinctly approachable minimalism that feels like quality paper rather than sterile glass. The page canvas is pure white (`{colors.background}`) but the text isn't pure black — it's a warm near-black (`{colors.ink}`) that softens the reading experience imperceptibly. The warm gray scale (`{colors.surface-warm}`, `{colors.surface-dark}`, `{colors.text-secondary}`, `{colors.text-muted}`) carries subtle yellow-brown undertones, giving the interface a tactile, almost analog warmth.

The custom NotionInter font (a modified Inter) is the backbone of the system. At display sizes (64px), it uses aggressive negative letter-spacing (-2.125px), creating headlines that feel compressed and precise. The weight range is broader than typical systems: 400 for body, 500 for UI elements, 600 for semi-bold labels, and 700 for display headings. OpenType features `"lnum"` (lining numerals) and `"locl"` (localized forms) are enabled on larger text, adding typographic sophistication that rewards close reading.

What makes Notion's visual language distinctive is its border philosophy. Rather than heavy borders or shadows, Notion uses ultra-thin `{colors.border}` borders — borders that exist as whispers, barely perceptible division lines that create structure without weight. The shadow system is equally restrained: multi-layer stacks with cumulative opacity never exceeding 0.05, creating depth that's felt rather than seen.

**Key Characteristics:**
- NotionInter (modified Inter) with negative letter-spacing at display sizes (-2.125px at 64px)
- Warm neutral palette: grays carry yellow-brown undertones (`{colors.surface-warm}` warm white, `{colors.surface-dark}` warm dark)
- Near-black text (`{colors.ink}`) — not pure black, creating micro-warmth
- Ultra-thin borders (`{colors.border}`) throughout — whisper-weight division
- Multi-layer shadow stacks with sub-0.05 opacity for barely-there depth
- Notion Blue (`{colors.primary}`) as the singular accent color for CTAs and interactive elements
- Pill badges (9999px radius) with tinted blue backgrounds for status indicators
- 8px base spacing unit with an organic, non-rigid scale

## Colors

### Primary
- **Notion Black** (`{colors.ink}`): Primary text, headings, body copy. The 95% opacity flattening softens pure black without sacrificing readability.
- **Pure White** (`{colors.background}`): Page background, card surfaces, button text on blue.
- **Notion Blue** (`{colors.primary}`): Primary CTA, link color, interactive accent — the only saturated color in the core UI chrome.

### Brand Secondary
- **Deep Navy** (`{colors.secondary}`): Secondary brand color, used sparingly for emphasis and dark feature sections.
- **Active Blue** (`{colors.primary-active}`): Button active/pressed state — darker variant of Notion Blue.

### Warm Neutral Scale
- **Warm White** (`{colors.surface-warm}`): Background surface tint, section alternation, subtle card fill. The yellow undertone is key.
- **Warm Dark** (`{colors.surface-dark}`): Dark surface background, dark section text. Warmer than standard grays.
- **Warm Gray 500** (`{colors.text-secondary}`): Secondary text, descriptions, muted labels.
- **Warm Gray 300** (`{colors.text-muted}`): Placeholder text, disabled states, caption text.

### Semantic Accent Colors
- **Teal** (`{colors.success-teal}`): Success states, positive indicators.
- **Green** (`{colors.success}`): Confirmation, completion badges.
- **Orange** (`{colors.warning}`): Warning states, attention indicators.
- **Pink** (`{colors.accent-pink}`): Decorative accent, feature highlights.
- **Purple** (`{colors.accent-purple}`): Premium features, deep accents.
- **Brown** (`{colors.accent-brown}`): Earthy accent, warm feature sections.

### Interactive
- **Link Blue** (`{colors.link}`): Primary link color with underline-on-hover.
- **Link Light Blue** (`{colors.link-light}`): Lighter link variant for dark backgrounds.
- **Focus Blue** (`{colors.focus-ring}`): Focus ring on interactive elements.
- **Badge Blue Bg** (`{colors.badge-bg}`): Pill badge background, tinted blue surface.
- **Badge Blue Text** (`{colors.badge-text}`): Pill badge text, darker blue for readability.

### Borders & Shadows
- **Whisper Border** (`{colors.border}`): Standard division border — cards, dividers, sections.
- **Input Border** (`{colors.border-input}`): Slightly stronger 1px border for form inputs.
- **Shadow Tint** (`{colors.shadow-soft}`): Multi-layer card elevation — flattened approximation of Notion's 4-5 layer shadow stacks.

## Typography

### Font Family
- **Primary**: `NotionInter`, with fallbacks: `Inter, -apple-system, system-ui, Segoe UI, Helvetica, Arial`
- **OpenType Features**: `"lnum"` (lining numerals) and `"locl"` (localized forms) enabled on display and heading text.

### Hierarchy

The complete type scale lives in the `typography:` token block above. Use those tokens directly via reference (`{typography.display-hero}`, `{typography.body}`, etc.) rather than hardcoding values.

| Token | Use |
|---|---|
| `display-hero` | Maximum compression, billboard headlines |
| `display-secondary` | Secondary hero, feature headlines |
| `section-heading` | Feature section titles |
| `sub-heading-large` | Card headings, feature sub-sections |
| `sub-heading` | Section sub-titles, content headers |
| `card-title` | Feature cards, list titles |
| `body-large` | Introductions, feature descriptions |
| `body` | Standard reading text |
| `body-medium` | Navigation, emphasized UI text |
| `body-semibold` | Strong labels, active states |
| `nav-button` | Navigation links, button text |
| `caption` | Metadata, secondary labels |
| `badge` | Pill badges, tags, status labels |

### Principles
- **Compression at scale**: NotionInter at display sizes uses -2.125px letter-spacing at 64px, progressively relaxing to -0.625px at 26px and normal at 16px. The compression creates density at headlines while maintaining readability at body sizes.
- **Four-weight system**: 400 (body/reading), 500 (UI/interactive), 600 (emphasis/navigation), 700 (headings/display). The broader weight range compared to most systems allows nuanced hierarchy.
- **Warm scaling**: Line height tightens as size increases — 1.50 at body (16px), 1.23-1.27 at sub-headings, 1.00-1.04 at display.
- **Badge micro-tracking**: The 12px badge text uses positive letter-spacing (0.125px) — the only positive tracking in the system, creating wider, more legible small text.

## Layout

### Spacing System
The complete spacing scale lives in the `spacing:` token block above. Base unit is 8px with an organic, non-rigid scale.

### Grid & Container
- Max content width: approximately 1200px
- Hero: centered single-column with generous top padding (`5xl`–`6xl`)
- Feature sections: 2-3 column grids for cards
- Full-width warm white (`{colors.surface-warm}`) section backgrounds for alternation
- Code/dashboard screenshots contained with whisper border

### Whitespace Philosophy
- **Generous vertical rhythm**: `4xl`–`6xl` between major sections. Notion lets content breathe with vast vertical padding.
- **Warm alternation**: White sections alternate with warm white (`{colors.surface-warm}`) sections, creating gentle visual rhythm without harsh color breaks.
- **Content-first density**: Body text blocks are compact (line-height 1.50) but surrounded by ample margin, creating islands of readable content in a sea of white space.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat (Level 0) | No shadow, no border | Page background, text blocks |
| Whisper (Level 1) | `1px solid {colors.border}` | Standard borders, card outlines, dividers |
| Soft Card (Level 2) | 4-layer shadow stack (max opacity 0.04) | Content cards, feature blocks |
| Deep Card (Level 3) | 5-layer shadow stack (max opacity 0.05, 52px blur) | Modals, featured panels, hero elements |
| Focus (Accessibility) | `2px solid {colors.focus-ring}` outline | Keyboard focus on all interactive elements |

**Shadow Philosophy**: Notion's shadow system uses multiple layers with extremely low individual opacity (0.01 to 0.05) that accumulate into soft, natural-looking elevation. The 4-layer card shadow spans from 1.04px to 18px blur, creating a gradient of depth rather than a single hard shadow. The 5-layer deep shadow extends to 52px blur at 0.05 opacity, producing ambient occlusion that feels like natural light rather than computer-generated depth.

## Shapes

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Edge-to-edge sections |
| `micro` | 4px | Buttons, inputs, functional interactive elements |
| `subtle` | 5px | Links, list items, menu items |
| `sm` | 8px | Small cards, containers, inline elements |
| `md` | 12px | Standard cards, feature containers, image tops |
| `lg` | 16px | Hero cards, featured content, promotional blocks |
| `pill` | 9999px | Badges, pills, status indicators |

Notion's radius system spans from sharp 4px button corners up to fully-pill badges. The 12px standard card radius is the workhorse for content surfaces.

## Components

The complete component spec lives in the `components:` token block above. Reference component tokens directly rather than reconstructing them.

### Buttons
- **`button-primary`** — Notion Blue solid CTA. Hover: background darkens to `{colors.primary-active}`. Active: scale(0.9). Use for primary actions ("Get Notion free", "Try it").
- **`button-secondary`** — Translucent warm-gray surface. For secondary actions and form submissions.
- **`button-ghost`** — Transparent background, near-black text. Underline on hover. Tertiary actions and inline links.
- **`badge-pill`** — Tinted blue pill (`{colors.badge-bg}` / `{colors.badge-text}`) for status badges, feature labels, "New" tags.

### Cards
- **`card`** — Standard 12px-radius card with whisper border and soft 4-layer shadow.
- **`card-featured`** — Hero/featured card at 16px radius with 5-layer deep shadow.

Image cards use 12px top-radius (`12px 12px 0 0`) with the image filling the top half.

### Inputs
White surface, 1px `{colors.border-input}` border, 4px radius, 6px padding. Focus brings a blue outline ring. Placeholder uses `{colors.text-muted}`.

### Navigation
Clean horizontal nav on white, not sticky. Brand logo left-aligned. Links at 15px weight 500-600. CTA: blue pill button right-aligned. Mobile collapses to hamburger menu.

## Do's and Don'ts

### Do
- Use warm neutrals — Notion's grays have yellow-brown undertones, never blue-gray
- Letter-spacing scales with font size: -2.125px at 64px, -1.875px at 54px, -0.625px at 26px, normal at 16px
- Use four weights: 400 (read), 500 (interact), 600 (emphasize), 700 (announce)
- Borders are whispers: `1px solid {colors.border}` — never heavier
- Shadows use 4-5 layers with individual opacity never exceeding 0.05
- Use the warm white (`{colors.surface-warm}`) section background for visual rhythm
- Use pill badges (`{rounded.pill}`) for status/tags, micro radius (`{rounded.micro}`) for buttons and inputs
- Reserve Notion Blue (`{colors.primary}`) for CTAs and links — it is the only saturated color in core UI

### Don't
- Don't use cold blue-gray neutrals — the palette is intentionally warm
- Don't use heavy borders or hard drop shadows — depth is whispered, not stated
- Don't introduce additional saturated colors beyond Notion Blue and the semantic accents
- Don't use pure black for text — the near-black `{colors.ink}` is the only ink color
- Don't tighten body text below 1.50 line-height — comfort comes from generous body leading

---

## Responsive Behavior

*(Preserved from original 9-section format — Google's parser keeps unknown sections.)*

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile Small | <400px | Tight single column, minimal padding |
| Mobile | 400-600px | Standard mobile, stacked layout |
| Tablet Small | 600-768px | 2-column grids begin |
| Tablet | 768-1080px | Full card grids, expanded padding |
| Desktop Small | 1080-1200px | Standard desktop layout |
| Desktop | 1200-1440px | Full layout, maximum content width |
| Large Desktop | >1440px | Centered, generous margins |

### Touch Targets
- Buttons use comfortable padding (8px-16px vertical)
- Navigation links at 15px with adequate spacing
- Pill badges have 8px horizontal padding for tap targets
- Mobile menu toggle uses standard hamburger button

### Collapsing Strategy
- Hero: 64px display -> scales to 40px -> 26px on mobile, maintains proportional letter-spacing
- Navigation: horizontal links + blue CTA -> hamburger menu
- Feature cards: 3-column -> 2-column -> single column stacked
- Product screenshots: maintain aspect ratio with responsive images
- Trust bar logos: grid -> horizontal scroll on mobile
- Footer: multi-column -> stacked single column
- Section spacing: 80px+ -> 48px on mobile

### Image Behavior
- Workspace screenshots maintain whisper border at all sizes
- Hero illustrations scale proportionally
- Product screenshots use responsive images with consistent border radius
- Full-width warm white sections maintain edge-to-edge treatment

---

## Agent Prompt Guide

*(Preserved from original 9-section format — the copy-paste payload section.)*

### Quick Color Reference
- Primary CTA: Notion Blue (`{colors.primary}`)
- Background: Pure White (`{colors.background}`)
- Alt Background: Warm White (`{colors.surface-warm}`)
- Heading text: Near-Black (`{colors.ink}`)
- Body text: Near-Black (`{colors.ink}`)
- Secondary text: Warm Gray 500 (`{colors.text-secondary}`)
- Muted text: Warm Gray 300 (`{colors.text-muted}`)
- Border: `1px solid {colors.border}`
- Link: Notion Blue (`{colors.link}`)
- Focus ring: Focus Blue (`{colors.focus-ring}`)

### Example Component Prompts
- "Create a hero section on white background. Headline at 64px NotionInter weight 700, line-height 1.00, letter-spacing -2.125px, color `{colors.ink}`. Subtitle at 20px weight 600, line-height 1.40, color `{colors.text-secondary}`. Blue CTA button (`{colors.primary}`, 4px radius, 8px 16px padding, white text) and ghost button (transparent bg, near-black text, underline on hover)."
- "Design a card: white background, 1px solid `{colors.border}`, 12px radius. Use 4-layer shadow stack flattened to `{colors.shadow-soft}`. Title at 22px NotionInter weight 700, letter-spacing -0.25px. Body at 16px weight 400, color `{colors.text-secondary}`."
- "Build a pill badge: `{colors.badge-bg}` background, `{colors.badge-text}` text, 9999px radius, 4px 8px padding, 12px NotionInter weight 600, letter-spacing 0.125px."
- "Create navigation: white header. NotionInter 15px weight 600 for links, near-black text. Blue pill CTA 'Get Notion free' right-aligned (`{colors.primary}` bg, white text, 4px radius)."
- "Design an alternating section layout: white sections alternate with warm white (`{colors.surface-warm}`) sections. Each section has 64-80px vertical padding, max-width 1200px centered. Section heading at 48px weight 700, line-height 1.00, letter-spacing -1.5px."

### Iteration Guide
1. Always use warm neutrals — Notion's grays have yellow-brown undertones, never blue-gray
2. Letter-spacing scales with font size: -2.125px at 64px, -1.875px at 54px, -0.625px at 26px, normal at 16px
3. Four weights: 400 (read), 500 (interact), 600 (emphasize), 700 (announce)
4. Borders are whispers: `1px solid {colors.border}` — never heavier
5. Shadows use 4-5 layers with individual opacity never exceeding 0.05
6. The warm white (`{colors.surface-warm}`) section background is essential for visual rhythm
7. Pill badges (`{rounded.pill}`) for status/tags, micro radius (`{rounded.micro}`) for buttons and inputs
8. Notion Blue (`{colors.primary}`) is the only saturated color in core UI — use it sparingly for CTAs and links
