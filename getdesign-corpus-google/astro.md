---
version: alpha
name: "Astro"
description: "Deep-space console light show. Gradient-infused dark surfaces illuminated by precise, vibrant accents and high-contrast text."

colors:
  background: "#ffffff"
  surface: "#060913"
  surface-elevated: "#f5f5f5"
  ink: "#111111"
  ink-muted: "#54b9ff"
  primary: "#858b98"
  on-primary: "#ffffff"
  border: "#4bf3c8"
  focus-ring: "#858b98"
  success: "#22c55e"
  warning: "#f59e0b"
  error: "#ef4444"
  shadow-soft: "#d9d9d9"

typography:
  display-hero:
    fontFamily: "ui-sans-serif, ui-sans-serif, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.05
    letterSpacing: -1px
  display:
    fontFamily: "ui-sans-serif, ui-sans-serif, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.5px
  heading-section:
    fontFamily: "ui-sans-serif, ui-sans-serif, system-ui, sans-serif"
    fontSize: 36px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.25px
  heading-sub:
    fontFamily: "ui-sans-serif, ui-sans-serif, system-ui, sans-serif"
    fontSize: 25px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0px
  body-large:
    fontFamily: "ui-sans-serif, ui-sans-serif, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  body:
    fontFamily: "ui-sans-serif, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  button-ui:
    fontFamily: "ui-sans-serif, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: 0px
  caption:
    fontFamily: "ui-sans-serif, ui-sans-serif, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.4
    letterSpacing: 0px

spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  2xl: 48px
  3xl: 64px
  4xl: 96px

rounded:
  none: 0px
  sm: 4px
  md: 8px
  lg: 16px
  pill: 9999px

components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.pill}"
    padding: 12px 24px
  button-primary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.background}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.pill}"
    padding: 12px 24px
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.pill}"
    padding: 12px 24px
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.lg}"
    padding: 24px
  input:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 12px 16px
  input-focus:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    borderColor: "{colors.focus-ring}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 12px 16px
  badge:
    backgroundColor: "{colors.surface-elevated}"
    textColor: "{colors.ink-muted}"
    typography: "{typography.caption}"
    rounded: "{rounded.pill}"
    padding: 4px 10px
---

# Astro Design System

## Overview

Astro's homepage reads like the cockpit of a spacecraft — a deep, near-black canvas (`#060913`) where vibrant gradients bloom across hero sections and crystalline accent colors (`#4bf3c8` mint, `#54b9ff` blue, `#acafff` violet) act as instrument lights. The system pairs technical precision with cosmic wonder. Dark surfaces are layered through small luminance steps rather than shadows, and the signature interstellar gradient (violet → magenta) carries the brand voice across hero backgrounds, primary CTAs, and decorative illustrations.

Typography sets up a deliberate three-way conversation. **Obviously** (a custom display face) handles marketing headlines with confident weight and slightly technical character. **ui-sans-serif** (Inter as substitute) handles body copy and UI chrome with calm neutrality. **ui-monospace** owns code snippets — and the `npm create astro@latest` install string isn't decorative, it's a recurring brand element rendered in mint accent. **MDIO** appears as a small functional face for labels and tags, identifiable by its 0.4px positive tracking.

What makes Astro's atmosphere unmistakable is the radius/color discipline. Every interactive button is a full pill (`9999px`), every card is a soft rectangle (`16px`), and color is rationed: bright accents never spread to large surface areas — they stay confined to gradients, badges, code highlights, and single key accents. Sections alternate between Deep Space (`#060913`) and Cosmic Dust (`#1f232e`) backgrounds without dividers, creating rhythm through luminance rather than line.

**Key Characteristics:**
- Deep Space (`#060913`) canvas with Cosmic Dust (`#1f232e`) elevated surfaces — no shadows, only luminance steps
- Interstellar gradient (`#b845ed` violet → `#f041ff` magenta → `#2f4cb3` blue) for hero backgrounds and primary CTAs
- Aurora (`#f2f6fa`) and White Dwarf (`#ffffff`) text — high-contrast, never pure gray on dark
- Vivid accents reserved for code and highlights: Cosmic Sparkle Vivid (`#4bf3c8`), Cosmic Sparkle Blue (`#54b9ff`), Galaxy Violet (`#acafff`)
- Five-typeface stack — Obviously (display), ui-sans-serif (body), ui-monospace (code), MDIO (labels), Inter (alt body)
- Pill buttons (`9999px`) everywhere, paired with rectangular cards (`16px`)
- 64px section gaps create generous vertical rhythm without visible dividers
- 1280px max-width centers content; hero is full-bleed, body is contained
- No drop shadows — depth communicated through background contrast

## Colors

### Background Surfaces
- **Deep Space** (`#060913`): Primary page background — the canvas everything sits against.
- **Cosmic Dust** (`#1f232e`): Elevated surface — card backgrounds and section variations.
- **Void Shadow** (`#0c0f19`): Slightly darker shade for subtle button backgrounds and recessed elements.
- **Stellar Blue** (`#162a4c`): Background for illustrative or feature sections.

### Text & Content
- **Aurora** (`#f2f6fa`): Primary text — body copy and most headings.
- **White Dwarf** (`#ffffff`): Maximum-contrast text for critical display elements.
- **Stardust** (`#858b98`): Secondary text — subdued headings, captions, default nav links.
- **Lunar Gray** (`#545864`): Subtle borders and dividers.

### Brand & Accent
- **Interstellar Gradient Alpha** (`#b845ed`): Primary brand gradient anchor (violet).
- **Interstellar Gradient Beta** (`#f041ff`): Secondary gradient anchor (magenta).
- **Interstellar Gradient Gamma** (`#2f4cb3`): Tertiary gradient anchor (blue).
- **Signature Gradient**: `linear-gradient(83.21deg, rgb(50, 69, 255), rgb(184, 69, 237))` — the house gradient for hero sections.

### Highlight Accents
- **Cosmic Sparkle Vivid** (`#4bf3c8`): Mint accent for code highlights and key information.
- **Cosmic Sparkle Blue** (`#54b9ff`): Vivid blue for inline links.
- **Galaxy Violet** (`#acafff`): Violet accent for code tokens.
- **Asteroid Dust** (`#ffd493`): Amber highlight for keywords or badge text.

## Typography

### Font Families
- **ui-sans-serif** (substitute: Inter): Default UI text — body copy, buttons, navigation, small headings. Neutral foundation.
- **Obviously** (substitute: Poppins): Display and marketing headlines. Custom OpenType features create the signature confident-but-technical voice.
- **ui-monospace** (substitute: Fira Code): Code snippets and install strings. Consistent width supports the developer-tool brand.
- **MDIO** (substitute: Space Mono): Small functional text for labels, tags, and iconography support. Identifiable by its 0.4px positive tracking.
- **Inter**: Alternative body text where a different x-height adds typographic texture.

### Hierarchy

| Role | Font | Size | Line Height | Letter Spacing |
|------|------|------|-------------|----------------|
| Display | Obviously | 48px | 1.10 | normal |
| Heading Large | Obviously | 36px | 1.11 | normal |
| Heading | Obviously | 30px | 1.10 | normal |
| Subheading | Obviously / ui-sans-serif | 20px | 1.10 | normal |
| Body | ui-sans-serif | 16px | 1.50 | normal |
| Body Small | ui-sans-serif | 14px | 1.50 | normal |
| Caption | MDIO / ui-monospace | 12px | 1.33 | 0.48px |

### Principles
- **Three-typeface signal**: Obviously announces, ui-sans-serif explains, ui-monospace demonstrates. Each face has a job and never trespasses on the others.
- **Weight as voice for Obviously**: Weights 300, 400, and 700 are all in active use. Light weight (300) at large sizes creates authority through restraint; 700 reserved for maximum impact.
- **Code strings as brand elements**: `npm create astro@latest` rendered in `ui-monospace` with `Cosmic Sparkle Vivid` (`#4bf3c8`) is a recurring identity moment, not a generic code block.
- **Positive tracking for MDIO only**: 0.4px positive letter-spacing is signature for technical labels. Obviously and ui-sans-serif stay at normal tracking.
- **Aurora for body, White Dwarf for emphasis**: Two text colors handle 95% of the system. Stardust appears only for genuinely secondary content.

## Layout

### Spacing System
- **elementGap**: `8px` — small inline spacing
- **sectionGap**: `64px` — generous vertical breathing between sections
- **cardPadding**: `24px` — standard interior padding for cards

### Border Radius Scale
- **buttons / badges**: `9999px` (full pill — non-negotiable)
- **cards / code blocks**: `16px`
- **small elements**: `8px`

### Grid
- Max content width: `1280px`
- Hero: full-bleed gradient with centered content stack inside
- Body sections: contained within max-width, centered
- Two-column layouts (text + visual) and feature card grids dominate
- Section alternation: Deep Space → Cosmic Dust → Deep Space, no dividers

### Layout & Composition
The page maintains a `1280px` max-width with content centered. The hero is full-bleed with the Interstellar Gradient Alpha background; subsequent sections alternate Deep Space and Cosmic Dust to create rhythm. Inside sections, content typically follows a two-column (text-left + visual-right) or feature-card-grid pattern. Vertical generosity is the rule — `64px` between sections supports a comfortable reading density even when content is information-rich. The sticky nav stays minimal, with a subtle GitHub icon as a recurring brand-fit detail.

## Elevation & Depth

| Level | Hex | Name | Purpose |
|-------|-----|------|---------|
| 0 | `#060913` | Deep Space | Page background — the canvas |
| 1 | `#0c0f19` | Void Shadow | Recessed elements, subtle button backgrounds |
| 2 | `#1f232e` | Cosmic Dust | Elevated surfaces — cards, alternating sections |
| 3 | `#162a4c` | Stellar Blue | Illustrative backgrounds for feature areas |

**Shadow Philosophy**: Astro deliberately avoids drop shadows. Depth is communicated through background luminance steps and the gradient illuminations that bleed across hero areas. Elevation reads as "stepping closer to the light," not "casting darkness." The result is a system that stays graphically clean at any zoom level — no shadow blur to manage at responsive sizes — and reinforces the cosmic atmosphere where surfaces emit light rather than block it.

## Shapes

The complete radius scale is declared in the `rounded:` token block above.

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Hard-edged brand moments and flush layouts |
| `sm` | 4px | Small controls and tight UI details |
| `md` | 8px | Inputs and compact interface elements |
| `lg` | 16px | Cards and larger containers |
| `pill` | 9999px | CTAs, chips, and rounded badges |

## Components

### Buttons

**Primary Filled (Pill)**
- Background: `#ffffff` (rendered with transparent overlay over gradient backgrounds)
- Text: Aurora (`#f2f6fa`)
- Radius: `9999px` (full pill)
- Padding: `8px 16px`
- Font: ui-sans-serif, weight 400
- Use: Hero CTAs, "Get Started" actions

**Subtle Pill (Ghost)**
- Background: `rgba(44, 44, 44, 0.3)` (Cosmic Dust at 30% alpha)
- Text: Aurora (`#f2f6fa`)
- Radius: `9999px`
- Padding: `8px 24px`
- Use: Framework selection, less prominent actions

**Text Link**
- Background: transparent
- Text: Aurora (`#f2f6fa`)
- No border, no padding chrome
- Use: Inline tertiary navigation

### Badges

**Version Badge**
- Background: `rgba(44, 44, 44, 0.3)`
- Text: Aurora (`#f2f6fa`)
- Radius: `9999px` (pill)
- Padding: `8px 24px`
- Pattern: small announcement chip, e.g. "Astro 5.0 — Available now!"

### Cards

**Feature Card**
- Background: Cosmic Dust (`#1f232e`)
- Radius: `16px`
- Padding: `24px`
- No shadow, no border — depth via background contrast
- Title: Obviously, 20px, weight 400, Aurora
- Body: ui-sans-serif, 16px, weight 400, Stardust

**Code Block**
- Background: Deep Space (`#060913`)
- Border: `1px solid #1f232e` (Cosmic Dust)
- Radius: `16px`
- Padding: `24px`
- Code: ui-monospace, 14px, weight 400, Cosmic Sparkle Vivid (`#4bf3c8`)
- Line height: 1.65

### Navigation
- Sticky top bar over Deep Space background
- Links: Stardust (`#858b98`), ui-sans-serif, weight 400 — lighten to Aurora on hover
- GitHub icon: monochrome, single-fill, White Dwarf or Stardust
- No solid bar background — relies on the dark canvas continuing through

## Do's and Don'ts

### Do
- Use Deep Space (`#060913`) as the default page background to establish the dark theme.
- Apply the Interstellar Gradient (`linear-gradient(83.21deg, rgb(50, 69, 255), rgb(184, 69, 237))`) to hero sections and primary CTAs for high visual impact.
- Render all primary body and heading text in Aurora (`#f2f6fa`) or White Dwarf (`#ffffff`) for optimal contrast.
- Utilize `9999px` border-radius for all interactive buttons and badges — the pill is the brand voice.
- Employ Obviously (weights 300, 400, 700) for all display headings to leverage its custom OpenType character.
- Maintain `8px` element gap and `64px` section gap to preserve the cosmic breathing rhythm.
- Use MDIO specifically for technical labels with its 0.4px positive letter-spacing.
- Render install strings (`npm create astro@latest`) in ui-monospace with Cosmic Sparkle Vivid for the signature code-as-brand moment.

### Don't
- Avoid using bright, high-saturation colors for large background areas; reserve them strictly for accents and gradients.
- Do not deviate from `9999px` for buttons or `16px` for cards — these radii are key to the aesthetic.
- Never use generic system monospace for code; always use ui-monospace (or Fira Code) for consistency.
- Do not introduce drop shadows for card elevation; rely on background luminance steps.
- Do not use multi-color or complex iconography; stick to monochrome outline or single-fill in White Dwarf or Stardust.
- Avoid wide line lengths or excessive justification; body text stays at 16px with 1.5 line-height.
- Do not apply letter-spacing on Obviously headings — its inherent OpenType features define its character.

---

## Responsive Behavior

### Breakpoints
| Name | Width | Changes |
|------|-------|---------|
| Mobile | `<640px` | Single column, hero gradient simplifies, section gap reduces |
| md | `768px+` | Two-column feature layouts engage |
| lg | `1024px+` | Full desktop composition with side-by-side text + visual |
| xl | `1280px+` | Max-width container caps; content stays centered |

### Touch Targets
- Pill buttons: minimum `40px` height including padding
- Nav links: comfortable hit areas with at least `8px` gap between

### Collapsing Strategy
- Display: 48px → 36px → 30px on mobile; line-height stays tight
- Two-column text+visual layouts collapse to stacked single column
- Section gap `64px` → `40px` on mobile to maintain rhythm at smaller scales
- Code blocks maintain padding; horizontal scroll for overflow rather than text wrap
- Hero gradient stays full-bleed; CTA stack centers and stacks vertically

---

## Agent Prompt Guide

### Quick Color Reference
- Background: `#060913` (Deep Space)
- Surface: `#1f232e` (Cosmic Dust)
- Border: `#545864` (Lunar Gray) or `#1f232e`
- Text: `#f2f6fa` (Aurora) primary, `#858b98` (Stardust) secondary
- Brand Gradient: `linear-gradient(83.21deg, rgb(50, 69, 255), rgb(184, 69, 237))`
- Code Accent: `#4bf3c8` (Cosmic Sparkle Vivid)
- Link Accent: `#54b9ff` (Cosmic Sparkle Blue)

### Example Component Prompts
1. **Hero Section**: Full-width background using `linear-gradient(83.21deg, rgb(50, 69, 255), rgb(184, 69, 237))`. Centered headline "The web framework for content-driven websites" using Obviously, 48px, weight 700, color Aurora (`#f2f6fa`), line-height 1.1. Below, secondary text "Astro powers the world's fastest..." using ui-sans-serif, 18px, weight 400, color Stardust (`#858b98`), line-height 1.5. Primary pill button "Get Started": `#ffffff` background, Aurora text, `9999px` radius, `8px 16px` padding.
2. **Feature Card**: Cosmic Dust (`#1f232e`) background, `16px` radius, no shadow. Heading "Server-First" in Obviously, 20px, weight 400, Aurora. Body in ui-sans-serif, 16px, weight 400, Stardust. `8px` gap between elements, `24px` card padding.
3. **Subtle Pill Button**: `rgba(44, 44, 44, 0.3)` background, Aurora text, `9999px` radius, `8px 24px` padding. Text "React" in ui-sans-serif, 16px, weight 400.
4. **Code Snippet Block**: Deep Space (`#060913`) background with `1px solid #1f232e` border, `16px` radius, `24px` padding. Code text in ui-monospace, 14px, weight 400, color Cosmic Sparkle Vivid (`#4bf3c8`), line-height 1.65. Render `npm create astro@latest`.
5. **Version Badge**: `rgba(44, 44, 44, 0.3)` background, Aurora text, `9999px` radius, `8px 24px` padding. Text "Astro 5.0 — Available now!" in ui-sans-serif, 14px.

### Iteration Guide
1. Dark canvas first — Deep Space is non-negotiable as the page background.
2. Pills (`9999px`) for buttons, rectangles (`16px`) for cards. Don't blur the boundary.
3. Three typefaces signal three jobs: Obviously announces, ui-sans-serif explains, ui-monospace demonstrates.
4. Reserve bright accents (mint, blue, violet, amber) for code and key highlights — never large surfaces.
5. No shadows. Use Cosmic Dust on Deep Space for elevation.
6. The Interstellar Gradient is the house brand moment — use it for hero and primary CTAs only.
