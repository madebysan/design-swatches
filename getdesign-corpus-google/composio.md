---
version: alpha
name: Composio
description: Nocturnal developer command center — pitch-black canvas with near-invisible white-opacity borders, dual-font identity (abcDiatype + JetBrains Mono), bioluminescent cyan glows, hard-offset brutalist shadows, and ultra-tight 0.87 heading line-heights.

colors:
  # Primary canvas + ink
  background: "#0f0f0f"          # Void Black
  surface: "#000000"             # Pure Black for cards
  surface-elevated: "#1a1a1a"
  ink: "#ffffff"
  ink-near: "#252525"            # opaque approx of oklch(0.145 0 0) — Google format requires hex
  ink-inverted: "#000000"

  # Brand accent
  primary: "#0007cd"             # Composio Cobalt
  primary-cyan: "#00ffff"        # Electric Cyan
  primary-signal: "#0089ff"      # Signal Blue
  primary-ocean: "#0096ff"       # Ocean Blue

  # Charcoal divider
  charcoal: "#2c2c2c"

  # Text on dark
  on-background: "#ffffff"
  on-surface: "#ffffff"
  on-primary: "#ffffff"
  text-muted: "#444444"          # Muted Smoke
  text-ghost: "#999999"          # opaque approx of rgba(255,255,255,0.6) — Google format requires hex
  text-whisper: "#808080"        # opaque approx of rgba(255,255,255,0.5)
  text-phantom: "#333333"        # opaque approx of rgba(255,255,255,0.2) over black

  # Borders (opaque approximations of low-opacity white borders)
  border-mist-12: "#1f1f1f"  # was rgba(255,255,255,0.12) — flattened over Void Black
  border-mist-10: "#1a1a1a"  # was rgba(255,255,255,0.10)
  border-mist-08: "#171717"  # was rgba(255,255,255,0.08)
  border-mist-06: "#141414"  # was rgba(255,255,255,0.06)
  border-mist-04: "#121212"  # was rgba(255,255,255,0.04)
  border-light: "#e0e0e0"

  # Cyan accent surface (opaque approx)
  cyan-surface: "#003333"  # was rgba(0,255,255,0.12) flattened over near-black

  # Shadow tints
  shadow-brutalist: "#000000"  # used at 15% in prose; opaque base
  shadow-floating: "#000000"

typography:
  display-hero:
    fontFamily: "abcDiatype, abcDiatype Fallback, ui-sans-serif, system-ui, sans-serif"
    fontSize: 64px
    fontWeight: 400
    lineHeight: 0.87
    letterSpacing: 0px
  section-heading:
    fontFamily: "abcDiatype, abcDiatype Fallback, ui-sans-serif, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0px
  sub-heading-large:
    fontFamily: "abcDiatype, abcDiatype Fallback, ui-sans-serif, system-ui, sans-serif"
    fontSize: 40px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: 0px
  sub-heading:
    fontFamily: "abcDiatype, abcDiatype Fallback, ui-sans-serif, system-ui, sans-serif"
    fontSize: 28px
    fontWeight: 400
    lineHeight: 1.20
    letterSpacing: 0px
  card-title:
    fontFamily: "abcDiatype, abcDiatype Fallback, ui-sans-serif, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.20
    letterSpacing: 0px
  feature-label:
    fontFamily: "abcDiatype, abcDiatype Fallback, ui-sans-serif, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.20
    letterSpacing: 0px
  body-large:
    fontFamily: "abcDiatype, abcDiatype Fallback, ui-sans-serif, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.20
    letterSpacing: 0px
  body:
    fontFamily: "abcDiatype, abcDiatype Fallback, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0px
  body-small:
    fontFamily: "abcDiatype, abcDiatype Fallback, ui-sans-serif, system-ui, sans-serif"
    fontSize: 15px
    fontWeight: 400
    lineHeight: 1.63
    letterSpacing: 0px
  caption:
    fontFamily: "abcDiatype, abcDiatype Fallback, ui-sans-serif, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.63
    letterSpacing: 0px
  label:
    fontFamily: "abcDiatype, abcDiatype Fallback, ui-sans-serif, system-ui, sans-serif"
    fontSize: 13px
    fontWeight: 500
    lineHeight: 1.50
    letterSpacing: 0px
  tag-overline:
    fontFamily: "abcDiatype, abcDiatype Fallback, ui-sans-serif, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 500
    lineHeight: 1.0
    letterSpacing: 0.3px
  code-body:
    fontFamily: "JetBrains Mono, JetBrains Mono Fallback, ui-monospace, SFMono-Regular, monospace"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: -0.32px
  code-small:
    fontFamily: "JetBrains Mono, JetBrains Mono Fallback, ui-monospace, SFMono-Regular, monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: -0.28px
  code-overline:
    fontFamily: "JetBrains Mono, JetBrains Mono Fallback, ui-monospace, SFMono-Regular, monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0.7px

spacing:
  micro: 1px
  2xs: 4px
  xs: 6px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
  2xl: 32px
  3xl: 40px

rounded:
  none: 0px
  xs: 2px
  sm: 4px
  pill: 37px
  full: 9999px

components:
  # Top navigation
  nav-bar:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    padding: 16px 24px
  nav-link:
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    padding: 8px 12px

  # Primary white CTA
  button-primary:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.ink-near}"
    typography: "{typography.body}"
    rounded: "{rounded.sm}"
    padding: 8px 24px
  button-primary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.ink-near}"

  # Cyan accent button — bioluminescent
  button-cyan:
    backgroundColor: "{colors.cyan-surface}"
    textColor: "{colors.ink-near}"
    typography: "{typography.body}"
    rounded: "{rounded.sm}"
    padding: 8px 24px

  # Ghost outlined — Signal Blue
  button-ghost-signal:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink-near}"
    typography: "{typography.body}"
    rounded: "{rounded.sm}"
    padding: 10px 16px

  # Ghost outlined — Charcoal
  button-ghost-charcoal:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink-near}"
    typography: "{typography.body}"
    rounded: "{rounded.sm}"
    padding: 10px 16px

  # Phantom button — deeply de-emphasized
  button-phantom:
    backgroundColor: "{colors.text-phantom}"
    textColor: "{colors.text-whisper}"
    typography: "{typography.body}"
    rounded: "{rounded.sm}"
    padding: 8px 16px

  # Card / container
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: 24px
  card-brutalist:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: 24px
  card-elevated:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: 32px

  # Code block
  code-block:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.code-small}"
    rounded: "{rounded.sm}"
    padding: 16px

  # Form input
  input:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.sm}"
    padding: 10px 12px
  input-focus:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
---

# Composio Design System

## Overview

Composio's interface is a nocturnal command center — a dense, developer-focused darkness punctuated by electric cyan and deep cobalt signals. The entire experience is built on an almost-pure-black canvas (`{colors.background}`) where content floats within barely-visible containment borders, creating the feeling of a high-tech control panel rather than a traditional marketing page. It's a site that whispers authority to developers who live in dark terminals.

The visual language leans heavily into the aesthetic of code editors and terminal windows. JetBrains Mono appears alongside the geometric precision of abcDiatype, reinforcing the message that this is a tool built *by* developers *for* developers. Decorative elements are restrained but impactful — subtle cyan-blue gradient glows emanate from cards and sections like bioluminescent organisms in deep water, while hard-offset shadows on select elements add a raw, brutalist edge that prevents the design from feeling sterile.

What makes Composio distinctive is its tension between extreme minimalism and strategic bursts of luminous color. The site never shouts — headings use tight line-heights (0.87) that compress text into dense, authoritative blocks. Color is rationed like a rare resource: white text for primary content, ghost-white opacity tiers for secondary, and brand blue (`{colors.primary}`) or electric cyan (`{colors.primary-cyan}`) reserved exclusively for interactive moments and accent glows.

**Key Characteristics:**
- Pitch-black canvas with near-invisible white-border containment (4-12% opacity)
- Dual-font identity: geometric sans-serif (abcDiatype) for content, monospace (JetBrains Mono) for technical credibility
- Ultra-tight heading line-heights (0.87-1.0) creating compressed, impactful text blocks
- Bioluminescent accent strategy — cyan and blue glows that feel like they're emitting light from within
- Hard-offset brutalist shadows on select interactive elements
- Monochrome hierarchy with color used only at the highest-signal moments
- Developer-terminal aesthetic that bridges marketing and documentation

## Colors

### Primary
- **Composio Cobalt** (`{colors.primary}`): The core brand color — a deep, saturated blue used sparingly for high-priority interactive elements and brand moments.

### Secondary & Accent
- **Electric Cyan** (`{colors.primary-cyan}`): The attention-grabbing accent — used at low opacity for glowing button backgrounds and card highlights. The energetic counterpoint to the dark canvas.
- **Signal Blue** (`{colors.primary-signal}`): Used for select button borders and interactive focus states.
- **Ocean Blue** (`{colors.primary-ocean}`): Accent border color on CTA buttons.

### Surface & Background
- **Void Black** (`{colors.background}`): Primary page background — not pure black, but a hair warmer.
- **Pure Black** (`{colors.surface}`): Card interiors and deep-nested containers.
- **Charcoal** (`{colors.charcoal}`): Used for secondary button borders and divider lines on dark surfaces.

### Text
- **Pure White** (`{colors.ink}`): Primary heading and high-emphasis text.
- **Muted Smoke** (`{colors.text-muted}`): De-emphasized body text, metadata, tertiary content.
- **Ghost White** (`{colors.text-ghost}`): Secondary body text and link labels — visible but receded.
- **Whisper White** (`{colors.text-whisper}`): Tertiary button text and placeholder content.
- **Phantom White** (`{colors.text-phantom}`): Subtle button backgrounds and deeply receded UI chrome.

### Borders (Mist scale — flattened to opaque hex)
- **Border Mist 12** (`{colors.border-mist-12}`): Highest-opacity border treatment — prominent card edges.
- **Border Mist 10** (`{colors.border-mist-10}`): Standard container borders.
- **Border Mist 08** (`{colors.border-mist-08}`): Subtle section dividers.
- **Border Mist 06** (`{colors.border-mist-06}`): Near-invisible containment borders.
- **Border Mist 04** (`{colors.border-mist-04}`): The faintest border — atmospheric only.
- **Light Border** (`{colors.border-light}`): Reserved for light-surface contexts (rare).

### Cyan Surface
- **Cyan Surface** (`{colors.cyan-surface}`): Flattened low-opacity Electric Cyan for glowing button fills.

### Gradient System
- **Cyan Glow**: Radial gradients using `{colors.primary-cyan}` at very low opacity — bioluminescent halos behind cards.
- **Blue-to-Black Fade**: Linear gradients from Composio Cobalt fading into Void Black.
- **White Fog**: Bottom-of-page gradient transitioning from dark to diffused white/gray.

## Typography

### Font Families
- **Primary**: `abcDiatype`, fallbacks `abcDiatype Fallback, ui-sans-serif, system-ui`
- **Monospace**: `JetBrains Mono`, fallbacks `JetBrains Mono Fallback, ui-monospace, SFMono-Regular, Menlo, Monaco`

The complete type scale lives in the `typography:` token block above.

| Token | Use |
|---|---|
| `display-hero` | 64px massive compressed heading (line-height 0.87) |
| `section-heading` | 48px major feature section title |
| `sub-heading-large` | 40px secondary section marker |
| `sub-heading` | 28px card titles, feature names |
| `card-title` | 24px medium-emphasis card heading (weight 500) |
| `feature-label` | 20px small card title, label |
| `body-large` | 18px intro paragraph |
| `body` | 16px standard body, nav, button |
| `body-small` | 15px longer-form body |
| `caption` | 14px descriptions, metadata |
| `label` | 13px UI label |
| `tag-overline` | 12px uppercase overline with 0.3px tracking |
| `code-body` | 16px JetBrains Mono with -0.32px tracking |
| `code-small` | 14px code snippet |
| `code-overline` | 14px uppercase technical label with 0.7px tracking |

### Principles
- **Compression creates authority**: Heading line-heights are drastically tight (0.87-1.0).
- **Dual personality**: abcDiatype carries marketing voice — geometric, precise. JetBrains Mono carries technical voice.
- **Weight restraint**: Almost everything is weight 400. Weight 500 is reserved for small labels, badges, and select card titles.
- **Negative letter-spacing on code**: JetBrains Mono uses negative letter-spacing for dense, IDE-like code blocks.
- **Uppercase is earned**: Reserved exclusively for tiny overline labels and technical tags.

## Layout

### Spacing System
The complete spacing scale lives in the `spacing:` token block above. Base unit is 8px.

### Grid & Container
- Max container width: ~1200px, centered
- Single-column or 2-3 column grids for feature cards
- Hero: centered single-column with maximum impact
- Asymmetric layouts mixing text blocks with product screenshots

### Whitespace Philosophy
- **Breathing room between sections**: Large vertical gaps create distinct "chapters".
- **Dense within components**: Cards and text blocks are internally compact (tight line-heights).
- **Contrast-driven separation**: Border opacity differences and subtle background shifts delineate content zones.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat (Level 0) | No shadow, no border | Page background, inline text |
| Contained (Level 1) | `{colors.border-mist-04}` to `{colors.border-mist-08}`, no shadow | Background groupings, subtle sections |
| Card (Level 2) | `{colors.border-mist-10}` to `{colors.border-mist-12}`, no shadow | Standard content cards, code blocks |
| Brutalist (Level 3) | Hard offset shadow (4px 4px) using `{colors.shadow-brutalist}` | Select interactive cards, distinctive feature highlights |
| Floating (Level 4) | Soft diffuse shadow using `{colors.shadow-floating}` | Modals, overlays, deeply elevated content |

**Shadow Philosophy**: Composio uses shadows sparingly and with deliberate contrast. The hard-offset brutalist shadow is the signature — it breaks the sleek darkness with a raw, almost retro-computing feel. Most depth is communicated through border opacity gradations rather than shadows.

### Decorative Depth
- **Cyan Glow Halos**: Radial gradient halos using Electric Cyan at low opacity behind feature cards.
- **Blue-Black Gradient Washes**: Linear gradients from Composio Cobalt to Void Black as section backgrounds.
- **White Fog Horizon**: Gradient from dark to diffused white/gray near the footer.

## Shapes

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Sharp edges (rare) |
| `xs` | 2px | Inline code spans, small tags |
| `sm` | 4px | Content cards, images, standard containers — workhorse |
| `pill` | 37px | Select buttons and badges — softer for key CTAs |
| `full` | 9999px | Circular elements, decorative dots |

## Components

The complete component spec lives in the `components:` token block above.

### Buttons
- **`button-primary`** — White fill with near-black text. The clean, high-signal CTA.
- **`button-cyan`** — Electric Cyan at 12% opacity (flattened to `{colors.cyan-surface}`) with Ocean Blue border. Glowing-from-within effect on dark.
- **`button-ghost-signal`** — Transparent with Signal Blue border. Secondary actions.
- **`button-ghost-charcoal`** — Transparent with Charcoal border. Tertiary on dark.
- **`button-phantom`** — Phantom White bg, Whisper text. Deeply de-emphasized.

### Cards & Containers
- **`card`** — Pure Black bg with `{colors.border-mist-10}` border, 4px radius.
- **`card-brutalist`** — Same shape with hard-offset shadow.
- **`card-elevated`** — Larger padding for elevated content.

### Code Blocks
- **`code-block`** — Pure Black bg with JetBrains Mono. Syntax-highlighted content.

### Inputs
- **`input`** — Transparent or pure black, Border Mist 10 border, focus shifts to Signal Blue or Electric Cyan.

### Navigation
- Sticky top nav on dark/black bg. Composio wordmark left, white nav links, white-fill CTA right.

### Distinctive Components

**Stats/Metrics Display**: Large monospace numbers in JetBrains Mono with subtle label text beneath.

**Code Blocks / Terminal Previews**: Dark containers with JetBrains Mono, syntax-highlighted, subtle bordered (Border Mist 10).

**Integration/Partner Logos Grid**: Grid layout of tool logos on dark surface, contained within bordered card.

**"COMPOSIO" Brand Display**: Oversized brand typography as section divider/brand statement.

## Do's and Don'ts

### Do
- Use Void Black (`{colors.background}`) as the primary page background
- Keep heading line-heights ultra-tight (0.87-1.0)
- Use white-opacity borders (4-12%) for containment
- Reserve Electric Cyan (`{colors.primary-cyan}`) for high-signal moments only
- Pair abcDiatype with JetBrains Mono
- Use the hard-offset shadow intentionally on select elements for brutalist personality
- Keep button text dark (`{colors.ink-near}`) even on the darkest backgrounds
- Layer opacity-based borders to create subtle depth without shadows
- Use uppercase + letter-spacing only for tiny overline labels (12px or smaller)

### Don't
- Don't use bright backgrounds or light surfaces as primary containers
- Don't apply heavy shadows everywhere — depth comes from border opacity
- Don't use Composio Cobalt (`{colors.primary}`) as a text color
- Don't increase heading line-heights beyond 1.2
- Don't use bold (700) weight for body or heading text
- Don't mix warm colors — palette is strictly cool (blue, cyan, white, black)
- Don't use border-radius larger than 4px on content cards
- Don't place Electric Cyan at full opacity on large surfaces — accent only
- Don't use decorative serif or handwritten fonts
- Don't skip the monospace font for technical content

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|---|---|---|
| Mobile | <768px | Single column, hamburger nav, full-width cards, hero ~28-40px |
| Tablet | 768-1024px | 2-column grid, condensed nav |
| Desktop | 1024-1440px | Full multi-column, expanded nav, hero 64px |
| Large Desktop | >1440px | Max-width container centered |

### Touch Targets
- Minimum 44×44px for interactive elements
- Buttons use 8px 24px minimum padding
- Nav links spaced for thumb navigation

### Collapsing Strategy
- **Navigation**: full horizontal → hamburger
- **Feature grids**: 3-column → 2-column → single
- **Hero text**: 64px → 40px → 28px
- **Section padding**: reduces but maintains generous rhythm
- **Code blocks**: horizontal scroll on smaller viewports

### Image Behavior
- Product screenshots scale proportionally
- Dark-themed images maintain contrast at all sizes
- Gradient glow effects scale with container size

---

## Agent Prompt Guide

### Quick Color Reference
- Primary CTA: Pure White `{colors.ink}`
- Page Background: Void Black `{colors.background}`
- Brand Accent: Composio Cobalt `{colors.primary}`
- Glow Accent: Electric Cyan `{colors.primary-cyan}`
- Heading Text: Pure White `{colors.ink}`
- Body Text: Ghost White `{colors.text-ghost}`
- Card Border: Border Mist 10 `{colors.border-mist-10}`
- Button Border: Signal Blue `{colors.primary-signal}`

### Example Component Prompts
- "Create a feature card with a near-black background (`{colors.surface}`), barely visible white border at 10% opacity, subtly rounded corners (4px), and a hard-offset shadow (4px right, 4px down). Use Pure White for the title in abcDiatype at 24px weight 500, and Ghost White for the description at 16px."
- "Design a primary CTA button with a solid white background, near-black text, comfortable padding (8px vertical, 24px horizontal), and subtly rounded corners. Place it next to a secondary button with transparent background, Signal Blue border, and matching padding."
- "Build a hero section on Void Black (`{colors.background}`) with a massive heading at 64px, line-height 0.87, in abcDiatype. Center the text. Add a subtle blue-to-black gradient glow behind the content. Include a white CTA button and a cyan-accented secondary button below."
- "Create a code snippet display using JetBrains Mono at 14px with -0.28px letter-spacing on a black background. Add a Border Mist 10 border and 4px radius."
- "Design a navigation bar on Void Black with the Composio wordmark in white on the left, 4-5 nav links in white abcDiatype at 16px, and a white-fill CTA button on the right."

### Iteration Guide
1. Focus on ONE component at a time
2. Reference specific color names and tokens — "use Ghost White (`{colors.text-ghost}`)"
3. Use natural language descriptions — "make the border barely visible" = Border Mist 04-06
4. Describe the desired "feel" alongside specific measurements
5. For glow effects, specify "Electric Cyan at 12% opacity as a radial gradient behind the element"
6. Always specify which font — abcDiatype for marketing, JetBrains Mono for technical/code content
