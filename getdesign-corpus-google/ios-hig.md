---
version: alpha
name: iOS Human Interface Guidelines
description: Apple's design doctrine — SF Pro Display/Text optical pair, System Blue as the singular brand, 18px card radius, full-pill buttons, and soft single-layer shadows.

colors:
  # Base
  background: "#ffffff"
  surface: "#f5f5f7"
  surface-secondary: "#f2f2f7"
  ink: "#1d1d1f"
  on-primary: "#ffffff"

  # Brand — System Blue
  primary: "#0071e3"
  primary-tint: "#cce2f9"  # was rgba(0,113,227,0.15) — Google format requires hex
  focus-ring-tint: "#cce2f9"  # opaque approx of primary at 0.15

  # System semantic colors
  danger: "#ff3b30"
  success: "#34c759"
  warning: "#ff9500"
  attention: "#ffcc00"
  pink: "#ff2d55"
  purple: "#af52de"
  teal: "#5ac8fa"
  indigo: "#5856d6"

  # Gray scale (System Gray)
  gray-6: "#f2f2f7"
  gray-5: "#e5e5ea"
  gray-4: "#d1d1d6"
  gray-3: "#c7c7cc"
  gray-2: "#aeaeb2"
  gray-1: "#8e8e93"
  gray-alt: "#515154"

  # Label hierarchy
  label-secondary: "#515154"
  label-tertiary: "#424245"
  label-quaternary: "#c7c7cc"

  # Borders / dividers
  separator: "#d2d2d7"
  border: "#d2d2d7"

  # Shadow tints (opaque)
  shadow-subtle: "#f5f5f5"  # was rgba(0,0,0,0.04) — Google format requires hex
  shadow-card: "#ebebeb"  # was rgba(0,0,0,0.08) — Google format requires hex
  shadow-popover: "#dedede"  # was rgba(0,0,0,0.12) — Google format requires hex
  shadow-modal: "#cccccc"  # was rgba(0,0,0,0.2) — Google format requires hex

  # Tinted button background
  gray-button-tint: "#ededee"  # was rgba(120,120,128,0.16) — Google format requires hex

typography:
  large-title:
    fontFamily: "SF Pro Display, -apple-system, BlinkMacSystemFont, Helvetica Neue, sans-serif"
    fontSize: 34px
    fontWeight: 700
    lineHeight: 1.21
    letterSpacing: 0.374px
  title-1:
    fontFamily: "SF Pro Display, -apple-system, BlinkMacSystemFont, Helvetica Neue, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.21
    letterSpacing: 0.364px
  title-2:
    fontFamily: "SF Pro Display, -apple-system, BlinkMacSystemFont, Helvetica Neue, sans-serif"
    fontSize: 22px
    fontWeight: 700
    lineHeight: 1.27
    letterSpacing: 0.352px
  title-3:
    fontFamily: "SF Pro Display, -apple-system, BlinkMacSystemFont, Helvetica Neue, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: 0.38px
  headline:
    fontFamily: "SF Pro Text, -apple-system, BlinkMacSystemFont, Helvetica Neue, sans-serif"
    fontSize: 17px
    fontWeight: 600
    lineHeight: 1.29
    letterSpacing: -0.374px
  body:
    fontFamily: "SF Pro Text, -apple-system, BlinkMacSystemFont, Helvetica Neue, sans-serif"
    fontSize: 17px
    fontWeight: 400
    lineHeight: 1.29
    letterSpacing: -0.374px
  callout:
    fontFamily: "SF Pro Text, -apple-system, BlinkMacSystemFont, Helvetica Neue, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.31
    letterSpacing: -0.24px
  subhead:
    fontFamily: "SF Pro Text, -apple-system, BlinkMacSystemFont, Helvetica Neue, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: -0.24px
  footnote:
    fontFamily: "SF Pro Text, -apple-system, BlinkMacSystemFont, Helvetica Neue, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.38
    letterSpacing: -0.078px
  caption-1:
    fontFamily: "SF Pro Text, -apple-system, BlinkMacSystemFont, Helvetica Neue, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0px
  caption-2:
    fontFamily: "SF Pro Text, -apple-system, BlinkMacSystemFont, Helvetica Neue, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.36
    letterSpacing: 0.066px

spacing:
  xs: 2px
  sm: 4px
  md: 7px
  lg: 9px
  xl: 16px
  2xl: 24px
  3xl: 32px
  4xl: 48px

rounded:
  none: 0px
  sm: 6px
  md: 12px
  lg: 18px
  pill: 980px

components:
  # Filled (primary) button — pill
  button-filled:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body}"
    rounded: "{rounded.pill}"
    padding: 8px 20px

  # Tinted button
  button-tinted:
    backgroundColor: "{colors.primary-tint}"
    textColor: "{colors.primary}"
    typography: "{typography.body}"
    rounded: "{rounded.pill}"
    padding: 8px 20px

  # Plain text-only button
  button-plain:
    backgroundColor: "{colors.background}"
    textColor: "{colors.primary}"
    typography: "{typography.body}"
    rounded: "{rounded.pill}"
    padding: 8px 20px

  # Gray button
  button-gray:
    backgroundColor: "{colors.gray-button-tint}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.pill}"
    padding: 8px 20px

  # Destructive
  button-destructive:
    backgroundColor: "{colors.danger}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body}"
    rounded: "{rounded.pill}"
    padding: 8px 20px

  # Card — soft 18px radius
  card:
    backgroundColor: "{colors.background}"
    rounded: "{rounded.lg}"
    padding: 16px

  # Grouped card (inside grouped table)
  card-grouped:
    backgroundColor: "{colors.background}"
    rounded: "{rounded.md}"
    padding: 12px

  # Text field
  input:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 11px 16px
  input-focus:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"

  # Switch
  switch-on:
    backgroundColor: "{colors.success}"
    rounded: "{rounded.pill}"
  switch-off:
    backgroundColor: "{colors.gray-5}"
    rounded: "{rounded.pill}"

  # Navigation (large title)
  nav-bar:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.large-title}"
    padding: 16px 16px
---

# iOS Human Interface Guidelines Design System

## Overview

The iOS Human Interface Guidelines are Apple's design doctrine — the reference that governs what "iOS" looks like. The Apple Developer Documentation site serves as both reference and example: pure white canvas (`{colors.background}`), Apple's specific near-black (`{colors.ink}`), System Blue (`{colors.primary}`) for interactive elements, and **SF Pro** — the typeface that defines Apple across iPhone, iPad, Mac, and Vision Pro. The aesthetic is restraint and deference: every pixel serves the content, every component borrowed from the system UI the user already knows.

Typography uses Apple's **SF Pro Display** for sizes 20px+ and **SF Pro Text** for sizes below 20px — a metric-matched family with optical-size-aware rendering. Weight 700 at 48px with tight `-0.144px` tracking for display. Body text at 17px weight 400 with subtle `-0.374px` tracking — the signature iOS body. Letter-spacing shifts from negative (`-0.374px` at body) to positive (`+0.216px` at 24px headings) depending on size — an unusual pattern that reflects SF's optical tuning.

The defining structural choice is **`18px` border-radius** as the dominant rounding (36 occurrences) — slightly larger than Material's 16px, much larger than shadcn's 10px. Combined with full-pill (`980px` in Apple's legacy notation, effectively `9999px`) for buttons, the system creates the soft, approachable iOS aesthetic. Colors are few: System Blue (`{colors.primary}`) as the one true brand, with system-defined red/green/amber/purple for semantic roles.

**Key Characteristics:**
- SF Pro Display (20px+) and SF Pro Text (<20px) — metric-matched, optical-size aware
- System Blue (`{colors.primary}`) as the singular brand anchor
- `18px` dominant radius — the softened-card iOS signature
- Full-pill buttons (`980px` radius) — Apple's historical pill notation
- Mixed letter-spacing: negative at body (`-0.374px`), positive at headings (`+0.216px`)
- Restrained shadows: only on cards, never on chrome
- SF Symbols for iconography — Apple's variable icon font
- Defers to system colors when possible — systemBlue, systemGreen, systemRed

## Colors

### System (Semantic)
- **System Blue** (`{colors.primary}`): Primary interactive — links, buttons, active states
- **System Red** (`{colors.danger}`): Destructive — delete, error
- **System Green** (`{colors.success}`): Positive — success, go
- **System Orange** (`{colors.warning}`): Warning, caution
- **System Yellow** (`{colors.attention}`): Attention
- **System Pink** (`{colors.pink}`): Tertiary accent
- **System Purple** (`{colors.purple}`): Creative, Photos accent
- **System Teal** (`{colors.teal}`): Info, Apple TV accent
- **System Indigo** (`{colors.indigo}`): Alternative blue

### Gray Scale
Apple's System Gray runs from `{colors.gray-6}` (lightest secondary background) through `{colors.gray-1}` (secondary label). `{colors.gray-alt}` is the body chrome workhorse.

### Label Hierarchy
- **Label** (`{colors.ink}`) — primary
- **Secondary** (`{colors.label-secondary}`)
- **Tertiary** (`{colors.label-tertiary}`)
- **Quaternary** (`{colors.label-quaternary}`)

### Background
- **System Background** (`{colors.background}`): Primary canvas
- **Background Secondary** (`{colors.surface}`): Grouped lists, table sections
- **Background Tertiary** (`{colors.surface-secondary}`): Nested content

## Typography

### Font Family
- **Display** (20px+): `SF Pro Display`, fallback `-apple-system, BlinkMacSystemFont, Helvetica Neue`
- **Text** (below 20px): `SF Pro Text`, same fallback chain
- **Rounded** (display accent): `SF Pro Rounded` for headlines like Memoji labels
- **Mono**: `SF Mono`, fallback `ui-monospace, Menlo, monospace`
- **Web fallback**: `Inter` is often used as a web approximation since SF Pro requires Apple's font license

### Hierarchy

The complete type scale lives in the `typography:` token block above. Reference tokens (`{typography.large-title}`, `{typography.body}`) directly.

| Token | Use |
|---|---|
| `large-title` | Navigation-scroll-expandable hero title |
| `title-1` | Top-level page titles |
| `title-2` | Major section heads |
| `title-3` | Sub-section heads, card titles |
| `headline` | Emphasized 17px text |
| `body` | Standard reading — iOS's reference size |
| `callout` | 16px secondary body |
| `subhead` | 15px body |
| `footnote` | 13px supporting text |
| `caption-1` | 12px metadata |
| `caption-2` | 11px micro labels |

### Principles
- **Mixed letter-spacing**: Display sizes use POSITIVE tracking, body sizes use NEGATIVE — counter-intuitive but reflects SF's optical tuning.
- **SF Display vs SF Text threshold at 20px**: Apple's automatic swap.
- **Weight 700 at Large Title**: standard headlines use weight 600.
- **Body at 17px**: iOS's default body text with `-0.374px` tracking as the signature.

## Layout

### Spacing System
The complete spacing scale lives in the `spacing:` token block above. Base unit is **4pt** (rendered as px on web). Apple's web docs lean heavily on `md` (7px) and `lg` (9px) for fine-grained vertical rhythm — an unusually granular pattern.

### Grid & Container
- Safe area insets determine layout — `xl` (16pt) margins on compact, `2xl` (24pt) on regular
- Max content width on web docs: ~980px (reading), ~1392px (full layout)
- Navigation: 44pt standard, 96pt with Large Title

### Whitespace Philosophy
iOS pacing favors generous rounded surfaces over editorial whitespace. Sections breathe through 18px-radius cards rather than vast empty padding — the rounded geometry itself produces visual rest.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat | None | Cards default |
| Subtle | `0 1px 3px {colors.shadow-subtle}` | Card rest |
| Card | `0 4px 24px {colors.shadow-card}` | Floating card |
| Popover | `0 8px 32px {colors.shadow-popover}` | Popovers, action sheets |
| Modal | `0 16px 48px {colors.shadow-modal}` | Modal dialogs |

**Shadow Philosophy**: iOS uses soft, diffused shadows — large offsets, high blur, low opacity. Rather than crisp layered shadows (Stripe, Material), iOS shadows suggest thin floating glass. Apple's native UI also leans on **materials** — translucent vibrancy effects that blur and tint content underneath — recreated on web via `backdrop-filter: blur()`.

## Shapes

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Sharp corners (rare) |
| `sm` | 6px | Kbd, chips |
| `md` | 12px | Text fields, small cards |
| `lg` | 18px | Primary cards — the iOS workhorse |
| `pill` | 980px | Buttons, badges, search bars (Apple's historical pill notation) |

## Components

The complete component spec lives in the `components:` token block above. Reference components directly (`{components.button-filled}`, `{components.card}`).

### Buttons
- **`button-filled`** — System Blue fill, white text, full pill, the canonical CTA.
- **`button-tinted`** — light tint of primary as background, primary text, full pill.
- **`button-plain`** — text-only, no background.
- **`button-gray`** — neutral gray tint background, ink text.
- **`button-destructive`** — System Red variant for delete/error actions.

### Cards & Lists
- **`card`** — white surface, 18px radius, soft single-layer shadow.
- **`card-grouped`** — used inside grouped tables (`{colors.surface}` outer, white inner).

Apple uses "insets" heavily — cards have internal borders separating rows.

### Inputs
- **`input`** — surface fill, 12px radius, no visible border. Focus state shifts to white background with a 2px primary ring.

### Switches
- **`switch-on`** / **`switch-off`** — 51×31px pill track, 27px white thumb with subtle shadow.

### Navigation
- **`nav-bar`** — top bar transitions from 96px tall (expanded Large Title) to 44px tall (collapsed Title 1) on scroll.

## Do's and Don'ts

### Do
- Use SF Pro Display for 20px+ sizes and SF Pro Text for smaller — respect the metric split
- Use POSITIVE letter-spacing on display headings (`+0.216–0.374px`)
- Use NEGATIVE letter-spacing on body text (`-0.374px` at 17px)
- Apply `{rounded.lg}` (18px) to cards, `{rounded.pill}` (980px) to buttons
- Use System Blue (`{colors.primary}`) sparingly — it's the singular interactive color
- Apply soft diffused shadows
- Use SF Symbols for iconography — variable axes (weight, fill, grade, opsz)

### Don't
- Don't use Inter or Roboto as primary — use SF Pro via `-apple-system` or fallback
- Don't use sharp corners — iOS is categorically rounded
- Don't use colored brand colors beyond System Blue — rely on system semantic colors
- Don't mix letter-spacing direction — Display positive, Text negative, consistent by size
- Don't override system dark mode behaviors — respect user preference
- Don't use layered multi-shadow systems — iOS is single-layer soft shadow

---

## Responsive Behavior

### Breakpoints (iOS size classes)
| Class | Width | Changes |
|---|---|---|
| Compact W | `<414pt` | iPhone portrait, single-column, bottom tab bar |
| Regular W | `>414pt` | iPhone landscape / iPad, master-detail |
| Compact H | `<568pt` | iPhone landscape |
| Regular H | `>568pt` | Standard portrait orientation |

### Touch Targets
- **Minimum 44pt × 44pt** — Apple's strict accessibility floor
- Buttons: 44pt default, scales to 50pt for prominent CTAs
- Navigation links: 44pt minimum with padding

### Collapsing Strategy
- Large Title: 34px → 28px on scroll (navigation collapse animation)
- Lists: grouped-table → single-column inset list on compact
- Modals: full-screen on compact, centered card on regular
- Split views: side-by-side on regular, stack on compact

---

## Agent Prompt Guide

### Quick Color Reference
- System Blue: `{colors.primary}`
- Label: `{colors.ink}`
- Secondary Label: `{colors.label-secondary}`
- Tertiary Label: `{colors.label-tertiary}`
- Separator: `{colors.separator}`
- System Background: `{colors.background}`
- Secondary Background: `{colors.surface}`
- System Red: `{colors.danger}`
- System Green: `{colors.success}`

### Example Component Prompts
- "Create a large title navigation: 96pt tall at rest, white bg. Title 34px SF Pro Display weight 700, letter-spacing +0.374px, color `{colors.ink}`. On scroll, collapses to 44pt with Title 1 (20px weight 600) centered. Back button in System Blue."
- "Design a grouped list: `{colors.surface}` outer bg, 16pt padding. Inset cards white bg, 18px radius, soft card shadow. Row title 17px SF Pro Text weight 400, letter-spacing -0.374px, color `{colors.ink}`. Chevron 12px System Gray."
- "Build a pill button: `{colors.primary}` bg, white text, 980px radius (full pill), 8px 20px padding, 17px SF Pro Text weight 400. Press state: 85% opacity. Disabled: System Gray 4 bg."

### Iteration Guide
1. SF Pro Display above 20px, SF Pro Text below — the metric split matters
2. Positive letter-spacing at display, negative at body — iOS inverts the norm
3. `18px` radius on cards is the iOS signature; `980px` on buttons
4. System Blue is the only brand color — everything else is system-defined
5. Soft single-layer shadows
6. Respect native dark mode — don't override user system preferences
