---
version: alpha
name: Aceternity UI
description: Motion-first dark-mode component system with Aurora violet-pink-blue gradients, non-standard radii (7.6/9.6/13.6px), and atmospheric glow elevation.

colors:
  # Dark canvas + ink
  background: "#09090b"
  surface: "#18181b"
  surface-elevated: "#1c1c22"
  border: "#27272a"
  ink: "#fafafa"
  ink-inverted: "#09090b"

  # Text states
  on-background: "#fafafa"
  on-surface: "#fafafa"
  on-primary: "#ffffff"
  text-muted: "#a1a1aa"
  text-disabled: "#52525b"

  # Brand accents — the Aurora trio
  primary: "#8b5cf6"
  secondary: "#ec4899"
  tertiary: "#3b82f6"

  # State colors
  success: "#22c55e"
  warning: "#f59e0b"
  error: "#ef4444"

  # Glow / elevation tints (opaque approximations)
  glow-violet: "#1f1535"  # was rgba(139,92,246,0.1) — flattened over background
  glow-violet-strong: "#2e1f4f"  # was rgba(139,92,246,0.2)
  glow-pink: "#2a1422"  # was rgba(236,72,153,0.2)
  glow-modal: "#000000"  # was rgba(0,0,0,0.8)
  focus-ring: "#3a2960"  # was rgba(139,92,246,0.3)

typography:
  display-hero:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 60px
    fontWeight: 700
    lineHeight: 1.0
    letterSpacing: -1.5px
  display-large:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 500
    lineHeight: 1.08
    letterSpacing: -1.2px
  heading-1:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 36px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.9px
  heading-2:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 30px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.75px
  heading-3:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: -0.6px
  body-large:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.56
    letterSpacing: 0px
  body:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  button-ui:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.0
    letterSpacing: 0px
  caption:
    fontFamily: "ui-monospace, SFMono-Regular, Menlo, monospace"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: 0px

spacing:
  micro: 4px
  xs: 8px
  sm: 12px
  md: 16px
  lg: 24px
  xl: 32px
  2xl: 40px
  3xl: 64px
  4xl: 96px

rounded:
  none: 0px
  xs: 3px
  sm: 5.6px
  md: 7.6px
  lg: 9.6px
  xl: 13.6px
  pill: 9999px

components:
  # Gradient primary button — Aurora fill
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.md}"
    padding: 8px 20px
  button-primary-hover:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.on-primary}"

  # Moving border button — animated gradient border
  button-moving-border:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.md}"
    padding: 8px 20px

  # Ghost button — outline only
  button-ghost:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.md}"
    padding: 8px 20px
  button-ghost-hover:
    backgroundColor: "{colors.surface}"

  # Card — workhorse surface
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xl}"
    padding: 24px
  card-hover:
    backgroundColor: "{colors.surface-elevated}"

  # 3D card — perspective transform on hover
  card-3d:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xl}"
    padding: 24px

  # Spotlight card — radial gradient follows cursor
  card-spotlight:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xl}"
    padding: 24px

  # Form input
  input:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 8px 12px
  input-focus:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"

  # Pill badge / chip
  badge:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.caption}"
    rounded: "{rounded.pill}"
    padding: 2px 10px

  # Modal / dialog
  modal:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xl}"
    padding: 32px
---

# Aceternity UI Design System

## Overview

Aceternity UI is a design system built for **motion**. The homepage is a reel of animated components — Aurora backgrounds, 3D cards, text-generation effects, scroll-driven gradients — each demonstrating why Aceternity exists: to make Next.js landing pages look like they were shipped by a Cupertino design team at 4am. Dark canvas (`{colors.background}`) is the default, violet-to-pink gradients bleed through hero sections, and every interactive element ships with a framer-motion transition.

Typography is **Inter** — same as HeroUI — but used dramatically: weight 700 at 60px with `-1.5px` letter-spacing on a gradient-text fill, weight 500 at 48px for section heads, weight 400 for body. Aceternity doesn't innovate typographically; it innovates **presentationally**. Gradient text, outline text, blur effects, glow on hover — the typeface is a canvas for motion, not a voice of its own.

The distinctive radius system: **non-standard values** — `7.6px`, `9.6px`, `13.6px`. These are derived from Tailwind's arbitrary value syntax (`rounded-[9.6px]`) and compound through component composition. The result is a radius vocabulary that feels slightly off-standard — deliberately, calibrated to look premium rather than pre-made.

**Key Characteristics:**
- Dark-first (`{colors.background}`) with violet gradient accents — `{colors.primary}` → `{colors.secondary}`
- Motion-driven: every component has framer-motion transitions built in
- Inter typeface with gradient-fill display treatments
- Non-standard radii (`7.6px`, `9.6px`, `13.6px`) — premium calibration
- Aurora, 3D cards, background beams, moving borders — the signature effects
- Built on Tailwind + Framer Motion + shadcn primitives underneath
- Pro tier unlocks advanced animations; free tier has the base components
- Dark mode IS the mode — light is derived, not primary

## Colors

### Core Neutrals (dark-first)
- **Background** (`{colors.background}`): Primary canvas (zinc-950).
- **Surface** (`{colors.surface}`): Card background (zinc-900).
- **Surface Elevated** (`{colors.surface-elevated}`): Hover state.
- **Border** (`{colors.border}`): Hairline borders (zinc-800).
- **Foreground** (`{colors.ink}`): Primary text (zinc-50).
- **Muted Foreground** (`{colors.text-muted}`): Secondary text (zinc-400).
- **Disabled** (`{colors.text-disabled}`): Placeholder, disabled text.

### Accent Gradients (the signature)
- **Violet** (`{colors.primary}`): Primary accent (violet-500).
- **Pink** (`{colors.secondary}`): Secondary accent (pink-500).
- **Blue** (`{colors.tertiary}`): Tertiary accent (blue-500).
- **Aurora Gradient**: `linear-gradient(135deg, {colors.primary} 0%, {colors.secondary} 50%, {colors.tertiary} 100%)` — the house gradient.

### State Colors
- **Success** (`{colors.success}`): Green (green-500).
- **Warning** (`{colors.warning}`): Amber.
- **Error** (`{colors.error}`): Red.

### Raw Color Distribution (from scan)
- `{colors.background}` appears 567 times — the canvas is truly dominant
- `#ffffff` appears 189 times as text/glyph color
- `{colors.surface}` appears in hover states

## Typography

### Font Family
- **Primary**: `Inter`, fallback: `ui-sans-serif, system-ui, sans-serif`
- **Monospace**: `ui-monospace, SFMono-Regular, Menlo, monospace`
- Aceternity often uses **`system-ui`** for smaller chrome elements — favors the native feel

### Hierarchy

The complete type scale lives in the `typography:` token block above. Use those tokens directly via reference rather than hardcoding values.

| Token | Use |
|---|---|
| `display-hero` | Maximum size — landing hero (60px, often gradient-filled) |
| `display-large` | Secondary hero, large section heads |
| `heading-1` | Major page heads |
| `heading-2` | Section heads |
| `heading-3` | Card titles, sub-section markers |
| `body-large` | Intro paragraphs |
| `body` | Standard reading text |
| `button-ui` | Button labels, UI chrome |
| `caption` | Monospace metadata, technical labels |

### Principles
- **Gradient fills at display**: Many hero titles use `background-clip: text` with Aurora gradient — the headline IS the brand color application.
- **Wide weight range**: 400, 500, 600, 700 all appear at display sizes — Aceternity uses weight as an expressive variable, not a hierarchy.
- **Negative tracking proportional to size**: -1.5px at 60px, -0.9px at 36px, -0.6px at 24px — progressive.
- **Monospace for captions**: 12px `ui-monospace` weight 500 is the branded small label treatment.

## Layout

### Spacing System
The complete spacing scale lives in the `spacing:` token block above. Base unit is 4px.

Dominant values: `md` (16px — heavy use), `xs` (8px), `2xl` (40px), `xl` (32px), `micro` (4px). The `md` dominance suggests Aceternity's rhythm favors `4` at the small end and jumps to `16/24/32` for section breathing.

### Grid
- 12-column Tailwind
- Max content width: `1280px`
- Hero sections: often full-bleed with max-width content inside
- Gutter: `lg`–`xl` between sections

## Elevation & Depth

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | No shadow | Background |
| Glow 1 | Subtle violet glow ~20px | Subtle brand glow |
| Glow 2 | Medium violet glow ~30px (`{colors.glow-violet-strong}` tinted) | Hover lift |
| Glow 3 | Wide violet+pink stack ~50–80px | Featured elements |
| Modal | Heavy black drop + violet glow combo | Dialogs |

**Shadow Philosophy**: Aceternity treats elevation as **atmospheric bloom** — gradient-tinted glows that emit from elements rather than cast shadows. This reads as premium/technological and masks the dark background beautifully. Motion-driven components often animate the glow intensity on hover/interaction — static elevation is a starting point, not the end state.

## Shapes

Non-standard Tailwind arbitrary values define the system. The off-standard pixel radii are intentional — they're a brand fingerprint.

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Edge cases, full-bleed sections |
| `xs` | 3px | Small inline elements (kbd) |
| `sm` | 5.6px | Small buttons, chips |
| `md` | 7.6px | Buttons, inputs — the workhorse (22 uses) |
| `lg` | 9.6px | Cards, wider containers (35 uses) |
| `xl` | 13.6px | Featured cards, heroes (53 uses — the signature) |
| `pill` | 9999px | Pill shapes, avatars, badges |

## Components

The complete component spec lives in the `components:` token block above. Reference component tokens directly rather than reconstructing them.

### Buttons
- **`button-primary`** — Aurora gradient fill, white text, `{rounded.md}` radius, the headline CTA
- **`button-moving-border`** — Animated gradient-border, transparent interior
- **`button-ghost`** — Transparent, zinc-800 border, hover zinc-900 bg

### Cards
- **`card`** — `{colors.surface}` bg, `1px solid {colors.border}`, `{rounded.xl}` radius, 24px padding
- **`card-3d`** — Transforms on hover with perspective + translateZ
- **`card-spotlight`** — Follows cursor with a radial gradient overlay

### Inputs
**`input`** — `{colors.surface}` bg, `1px solid {colors.border}`, `{rounded.md}` radius. Focus shows violet border with `{colors.focus-ring}` ring.

### Backgrounds (Aceternity's signature feature)
- **Aurora Background**: Animated gradient blobs behind content
- **Background Beams**: Animated line beams moving diagonally
- **Sparkles**: Dotted star particles with fade animations
- **Grid Pattern**: Subtle dot/grid SVG background
- **Vortex**: Conic gradient animation
- **Meteors**: Falling streak animations

### Badges / Chips
**`badge`** — `{rounded.pill}` radius, `2px 10px` padding, 12px weight 500. Optional gradient border via `background-clip: padding-box`.

## Do's and Don'ts

### Do
- Build every component with motion in mind — framer-motion is the dance partner
- Use Aurora gradients (violet → pink → blue) for hero accent moments
- Apply `background-clip: text` for gradient-filled display headlines
- Use non-standard radii (`{rounded.md}`, `{rounded.lg}`, `{rounded.xl}`) — the off-standard look is intentional
- Pair dark canvas (`{colors.background}`) with brand glow shadows
- Use ui-monospace for 12px captions and technical labels

### Don't
- Don't strip motion — Aceternity without animation is Aceternity without personality
- Don't use flat solid colors for elevation — use gradient glows
- Don't use standard Tailwind radii (`0.5rem`, `0.75rem`) — break for the non-standard pixels
- Don't mix bright light-mode chrome with Aceternity components — design for dark first
- Don't use text-only buttons for primary CTAs — the gradient is the voice

---

## Responsive Behavior

### Breakpoints
| Name | Width | Changes |
|------|-------|---------|
| Mobile | `<640px` | Single column, reduced motion (media query) |
| md | `768px+` | 2-column grids, motion enabled |
| lg | `1024px+` | Full desktop, motion at full intensity |
| xl | `1280px+` | Max-width applies |

### Touch Targets
- Buttons: minimum `40px` height
- Animated components: disable transform-heavy animations on mobile (reduced motion media query)

### Collapsing Strategy
- Hero: 60px → 42px → 32px, gradient fill maintained
- 3D cards flatten on mobile (no perspective transforms)
- Aurora backgrounds simplify to static gradients on low-power devices
- Font weight variation collapses: keep 400 body, 700 display

---

## Agent Prompt Guide

### Quick Color Reference
- Background: `{colors.background}` (zinc-950)
- Surface: `{colors.surface}` (zinc-900)
- Border: `{colors.border}` (zinc-800)
- Text: `{colors.ink}` (primary), `{colors.text-muted}` (muted)
- Violet: `{colors.primary}`
- Pink: `{colors.secondary}`
- Blue: `{colors.tertiary}`
- Aurora: `linear-gradient(135deg, {colors.primary}, {colors.secondary}, {colors.tertiary})`

### Example Component Prompts
- "Create a hero on `{colors.background}` with aurora gradient background (animated radial blobs of `{colors.primary}`, `{colors.secondary}`, `{colors.tertiary}` at 25% alpha). Headline at 60px Inter weight 700 letter-spacing -1.5px, gradient text fill (background-clip: text). Subtitle 18px weight 400 color `{colors.text-muted}`. Gradient button: aurora bg, white text, `{rounded.md}` radius, 8px 20px padding, weight 500."
- "Design a card: `{colors.surface}` bg, 1px solid `{colors.border}`, `{rounded.xl}` radius, 24px padding, box-shadow with `{colors.glow-violet-strong}` tint. Title 20px Inter weight 600 color `{colors.ink}`. On hover: scale(1.02) and shadow intensifies."
- "Build a moving-border button: 40px height, `{rounded.md}` radius, transparent bg, 2px gradient border that animates around the perimeter (conic-gradient rotating 360deg). Interior: `{colors.surface}`. Text: `{colors.ink}` 14px weight 500."

### Iteration Guide
1. Motion is the message — start with framer-motion, add static as fallback
2. Dark-first; light mode is a derivative theme
3. Use the non-standard radii (`{rounded.md}`, `{rounded.lg}`, `{rounded.xl}`) — they're intentional
4. Gradient glows (not drop shadows) for elevation
5. Aurora is the house gradient — violet → pink → blue at 135deg
6. `ui-monospace` at 12px weight 500 for technical captions/labels
