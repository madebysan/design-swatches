---
slug: 1password
name: 1Password
url: https://1password.com
domain: 1password.com
category: SaaS
styles: [Playful]
tagline: "Secure Airlock Behind Glass. A system that moves from the protective dark of an airlock to the bright clarity of a control room."
fonts: [agileSans, ui-sans-serif]
primary_color: "#145fe4"
---

# Design System Inspired by 1Password

> Secure Airlock Behind Glass. A system that moves from the protective dark of an airlock to the bright clarity of a control room.

## 1. Visual Theme & Atmosphere

1Password's homepage choreographs a deliberate transition from dark to light. The hero opens in Deep Space (`#1d1d21`) — a near-black surface that fades into the brand's signature blue (`#145fe4`), establishing the security-product gravitas. After the fold, the page shifts to crisp white (`#ffffff`) and stays there: feature cards, integration lists, navigation, and footer all sit on the bright canvas. The dark hero feels like the airlock; the white content area is the control room behind it.

The signature brand blue (`#145fe4`) is rationed with discipline. It only appears on primary CTAs, active states, and inline links — never as decorative flourish. Every appearance is a confirmation moment, an indicator light. The rest of the system is tightly monochrome: black text on white, white text on dark, with a single muted Warning Tan (`#cbb88e`) reserved for the announcement banner.

What makes the system unmistakable is the typographic posture. `agileSans` at large display sizes (88px, weight 300) carries aggressive negative letter-spacing (`-2.02px`) — light weight plus tight tracking creates a dense, architectural authority that doesn't shout. The radius vocabulary reinforces the dual character: full-pill buttons (`9999px`) sit inside modestly-rounded cards (`16px`) and tighter list items (`8px`), creating a focused tension between interactive and container elements.

**Key Characteristics:**
- Hero-to-body shift: Deep Space (`#1d1d21`) → Brand Blue (`#145fe4`) gradient → white content area
- Brand Blue (`#145fe4`) reserved exclusively for CTAs, active states, and inline links
- agileSans (custom typeface) at light weight (300) for largest headlines — authority through restraint
- Aggressive negative letter-spacing on display text (`-2.02px` at 88px, `-1.47px` at 64px, `-1.1px` at 48px)
- Pill buttons (`9999px`) contrasted with rectangular cards (`16px`) and list rows (`8px`)
- Sticky nav transitions from transparent over hero to white-with-bottom-border on scroll
- Subtle drop shadow on cards (`0 4px 12px 0 rgba(0,0,0,0.05)`) — barely-there depth
- Generous vertical section spacing (80–120px) creates a measured, deliberate cadence
- Monochrome icon set, line-style, no decorative color
- Grayscale customer logos for social proof — trust without visual noise

## 2. Color Palette & Roles

### Background Surfaces
- **White** (`#ffffff`): Primary page background and card surfaces.
- **Deep Space** (`#1d1d21`): Hero and footer backgrounds.
- **Void** (`#242529`): Secondary dark surfaces.

### Text & Content
- **Onyx** (`#000000`): Primary text on light backgrounds.
- **Graphite** (`#303136`): Secondary text on light backgrounds.
- **White** (`#ffffff`): Primary text on dark backgrounds.

### Brand & Accent
- **Brand Blue** (`#145fe4`): Primary CTAs, active states, inline links, hero gradient terminus.

### Border & Divider
- **Ash** (`#d7d7db`): Hairline borders for cards, list items, nav bottom border.

### Status & Notification
- **Warning Tan** (`#cbb88e`): Announcement banner background — muted, calm, non-alarming.

## 3. Typography Rules

### Font Families
- **agileSans** (substitute: Inter, Manrope): The primary brand font, used for everything from display headlines to body copy. Lighter weights (300) reserved for the largest display text — authority through restraint. Mid-weights (400, 500) handle body and UI labels.
- **ui-sans-serif** (substitute: System UI): Fallback or for cross-platform UI contexts where the custom font might not load.

### Hierarchy

| Role | Font | Size | Line Height | Letter Spacing |
|------|------|------|-------------|----------------|
| Display | agileSans | 88px | 1.10 | -2.02px |
| Heading Large | agileSans | 64px | 1.10 | -1.47px |
| Heading | agileSans | 48px | 1.20 | -1.10px |
| Heading Small | agileSans | 32px | 1.25 | -0.74px |
| Subheading | agileSans | 20px | 1.43 | normal |
| Body | agileSans | 16px | 1.50 | normal |
| Caption | agileSans | 14px | 1.50 | normal |

### Principles
- **Light weight at scale**: The 88px display uses weight 300 — light weight at large size creates editorial authority without aggression. This is the system's signature move.
- **Negative tracking proportional to size**: -2.02px at 88px, -1.47px at 64px, -1.1px at 48px, -0.74px at 32px. Below 20px, tracking is normal.
- **Single-typeface system**: agileSans handles every typographic role from display to caption. Hierarchy comes from size, weight, and tracking — not face changes.
- **Restraint as voice**: 1Password never uses weight 700+ for display — its biggest headlines stay at 300. The result feels engineered, not promotional.

## 4. Component Stylings

### Buttons

**Primary CTA (Filled Pill)**
- Background: Brand Blue (`#145fe4`)
- Text: White (`#ffffff`)
- Radius: `9999px`
- Padding: `10px 24px`
- Font: agileSans, weight 500
- Use: "Get started free", primary site CTAs

**Secondary CTA (Outline Pill)**
- Background: transparent
- Border: `1px solid #ffffff`
- Text: White (`#ffffff`)
- Radius: `9999px`
- Padding: `10px 24px`
- Use: Secondary action on dark hero backgrounds

**Inline Text Link**
- Text: Brand Blue (`#145fe4`), often followed by `→`
- No underline by default; underline on hover
- Use: In-text navigation, "Learn more →" patterns

### Cards

**Feature Card**
- Background: White (`#ffffff`)
- Radius: `16px`
- Padding: `24px` minimum
- Shadow: `0 4px 12px 0 rgba(0, 0, 0, 0.05)` — barely-there
- Title: agileSans, 32px, weight 400, Onyx
- Body: agileSans, 16px, weight 400, Graphite
- Link: agileSans, 16px, weight 500, Brand Blue with `→`

### Lists

**Integration List Item**
- Background: White (`#ffffff`)
- Border: `1px solid Ash (#d7d7db)`
- Radius: `8px`
- Padding: `16px 24px`
- Layout: 24×24 logo left, title in agileSans 16px weight 500, chevron right

### Toggles

**Business / Personal Toggle**
- Container: pill switch, neutral background
- Active inner pill: Brand Blue (`#145fe4`)
- Radius: `9999px`
- Use: Switching between two primary user segments

### Navigation
- Sticky header — starts transparent over hero, transitions to White (`#ffffff`) with `1px solid Ash` bottom border on scroll
- Links: Graphite (`#303136`) text, agileSans
- Primary CTA: filled Brand Blue button, right-aligned

### Banners

**Announcement Banner**
- Full-width bar at top of page
- Background: Warning Tan (`#cbb88e`)
- Text: Onyx (`#000000`)
- Use: Site-wide non-critical notifications

## 5. Layout Principles

### Spacing System
- **elementGap**: `8–16px` — small inline spacing between adjacent elements
- **sectionGap**: `80–120px` — generous vertical spacing between major sections
- **cardPadding**: `24px` minimum — never tight on cards

### Border Radius Scale
- **buttons**: `9999px` (full pill — non-negotiable for CTAs)
- **cards**: `16px`
- **list items / inputs**: `8px`

### Grid
- Max content width: `~1200px`
- Hero: full-bleed, viewport-height with centered headline stack
- Feature sections: 3-column card grids
- Text-and-image: 2-column splits

### Layout & Composition
The page opens with a full-bleed, viewport-height hero — centered headline stack on the dark Deep Space → Brand Blue gradient. After the hero, content shifts to a centered max-width (~1200px) container on white. Sections alternate between centered headline stacks, 3-column feature card grids, and 2-column text-and-image blocks. The sticky nav handles the dark-to-light transition by going transparent over the hero and solid white with a bottom border once the user scrolls past it.

## 6. Depth & Elevation

| Level | Hex | Name | Purpose |
|-------|-----|------|---------|
| 0 | `#ffffff` | White | Page background, primary canvas |
| 0 (dark) | `#1d1d21` | Deep Space | Hero and footer backgrounds |
| 1 | `#242529` | Void | Secondary dark surfaces |
| 2 | `#ffffff` + `0 4px 12px 0 rgba(0,0,0,0.05)` | Feature Card | Subtle elevation on light surfaces |

**Shadow Philosophy**: 1Password uses one shadow, applied sparingly. The card shadow (`0 4px 12px 0 rgba(0, 0, 0, 0.05)`) is barely-there — depth as suggestion rather than statement. Primary depth communication comes from the dark/light surface shift between hero and body, not from layered drop shadows. Buttons and inline elements never carry shadows; only feature cards earn the lift, and even there it's whispered.

## 7. Do's and Don'ts

### Do
- Use Brand Blue (`#145fe4`) exclusively for primary CTAs, inline links, and active state indicators.
- Apply tight negative letter-spacing (`-1px` to `-2px`) to all headlines 48px and larger.
- Employ `9999px` radius for all buttons — pill is the brand voice for interactive elements.
- Contrast pill buttons with rectangular cards (`16px`) and tighter list items (`8px`).
- Use the Deep Space → Brand Blue gradient solely for hero sections.
- Maintain generous vertical spacing between sections (`80–120px`).
- Use agileSans for all typography — single-font system is part of the brand discipline.
- Apply weight 300 at the largest display size for the signature restrained authority.

### Don't
- Do not use Brand Blue for static headlines or body text — it's reserved for interaction.
- Avoid rounded corners on main layout containers; reserve rounding for buttons (`9999px`), cards (`16px`), and list items (`8px`).
- Do not apply shadows to buttons or inline elements — only cards earn the subtle lift.
- Avoid introducing new saturated colors; the palette is intentionally monochrome with one blue accent.
- Do not use system fonts for headings; agileSans is a critical brand element.
- Avoid card padding below `24px` — cramped cards break the deliberate spaciousness.
- Do not use outlines on primary filled buttons.
- Do not use bold weights (700+) at display sizes — the system's largest text is light (300).

## 8. Responsive Behavior

### Breakpoints
| Name | Width | Changes |
|------|-------|---------|
| Mobile | `<640px` | Single column, hero shortens, display drops to ~48px |
| md | `768px+` | 2-column text+image layouts engage |
| lg | `1024px+` | 3-column feature card grids, full nav visible |
| xl | `1280px+` | Max-width container caps at ~1200px |

### Touch Targets
- Pill buttons: minimum `40px` height with `10px 24px` padding
- List items: comfortable `16px 24px` padding ensures touch-friendly hit areas

### Collapsing Strategy
- Display headline: 88px → 64px → 48px on mobile, tracking adjusts proportionally
- Hero gradient maintained but viewport-height tightens on short mobile screens
- 3-column feature card grid → 2-column → single stacked column
- Section gap: `120px` → `80px` → `48px` on mobile
- Sticky nav collapses to hamburger on mobile; CTA remains visible
- Integration list rows stack at full width with maintained padding

## 9. Agent Prompt Guide

### Quick Color Reference
- Text (Light BG): `#000000` (Onyx)
- Text (Dark BG): `#ffffff` (White)
- Background (Light): `#ffffff`
- Background (Dark): `#1d1d21` (Deep Space)
- CTA / Accent: `#145fe4` (Brand Blue)
- Border: `#d7d7db` (Ash)
- Banner: `#cbb88e` (Warning Tan)

### Example Component Prompts
1. **Hero Section**: Full-bleed hero with `linear-gradient(180deg, #1d1d21 25%, #145fe4 70%)` background. Headline "Secure access for every human" in agileSans, 88px, weight 300, color `#ffffff`, letter-spacing `-2.02px`. Sub-headline at 20px, weight 400, color `#ffffff`. Primary CTA: `#145fe4` background, `#ffffff` text, `9999px` radius, `10px 24px` padding. Secondary CTA: transparent with `1px solid #ffffff` border, same dimensions.
2. **Feature Card Grid**: 3-column grid on white. Each card: `#ffffff` background, `24px` padding, `16px` radius, shadow `0 4px 12px 0 rgba(0,0,0,0.05)`. Title in agileSans, 32px, weight 400, color `#000000`. Body at 16px, weight 400, color `#303136`. Link "Learn more →" in agileSans, 16px, weight 500, color `#145fe4`.
3. **Integration List Item**: White rectangle with `16px 24px` padding, `8px` radius, `1px solid #d7d7db` border. Left: 24×24 logo. Center-left: text "GitHub Actions" in agileSans, 16px, weight 500, `#000000`. Right: black chevron-right icon.
4. **Announcement Banner**: Full-width bar, `#cbb88e` background, `#000000` text in agileSans 14px weight 500, centered.
5. **Toggle**: Pill switch (`9999px`) with neutral container; active inner pill in Brand Blue (`#145fe4`). Labels "Business" / "Personal" in agileSans, weight 500.

### Iteration Guide
1. Hero is dark, body is white — the airlock-to-control-room transition is structural, not decorative.
2. Brand Blue (`#145fe4`) only on interactive elements. Never on static type.
3. Pills for buttons, rectangles for cards, tighter rectangles for list items — the radius vocabulary signals function.
4. agileSans handles every role; weight and size do the hierarchy work.
5. Display weight stays light (300) — the brand voice is restrained authority, not aggression.
6. Single shadow on feature cards only; everything else stays flat.

## Preview

![1Password](https://ysxnuuuj3kqhdyj2.public.blob.vercel-storage.com/1775929689940-thumb.jpg)
