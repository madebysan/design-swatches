---
version: alpha
name: "Loom"
description: "Token-first design system reference for Loom."

colors:
  background: "#ffffff"
  surface: "#1868db"
  surface-elevated: "#f5f5f5"
  ink: "#000000"
  ink-muted: "#27282b"
  primary: "#ffffff"
  on-primary: "#ffffff"
  border: "#e7eefb"
  focus-ring: "#ffffff"
  success: "#22c55e"
  warning: "#f59e0b"
  error: "#ef4444"
  shadow-soft: "#d9d9d9"

typography:
  display-hero:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 96px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -1px
  display:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 67px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  heading-section:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 36px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.25px
  heading-sub:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 25px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0px
  body-large:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  body:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  button-ui:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: 0px
  caption:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 20px
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

# Loom Design System

## Overview

Loom — now Atlassian Loom — is async-video-meets-enterprise: friendly, productive, immediately legible. The page opens on pure white (`#ffffff`) with a single dominant brand color, Atlassian Blue (`#1868db`), carrying every primary action. Where Loom's earlier identity leaned purple and playful-illustrated, the current Atlassian-era Loom is markedly more grown-up: rounded geometric type, pill-shaped CTAs, generous whitespace, and a clean co-branded "ATLASSIAN / Loom" lockup in the top-left. The vibe is *productivity tool that respects your time* — not "fun consumer app."

The defining typographic move is a soft geometric grotesk (in the Charlie Display / Charlie Text family Atlassian uses across its rebrand) at heavy weight 700, with mildly humanist letterforms — open apertures, slightly rounded terminals, just enough warmth to feel approachable next to the bold blue. Hero headlines run around 80–96px on desktop, weight 700, line-height ~1.05, with normal-to-slightly-tight tracking. There's no all-caps chrome, no monospace, no editorial tightness — Loom communicates *clarity*, not *craft*.

What distinguishes the system most is the **fully-pill button shape paired with deep dark product canvases**. CTAs are 9999px-rounded, sized for thumb confidence (min ~44–48px tall), filled with saturated `#1868db` blue or a tinted secondary `#e7eefb` light-blue panel. Below the hero, product moments live inside large dark-charcoal containers (`#27282b` / `#1f2024`) with substantial 16–24px outer corner radius — softening the typically-rectangular product-shot moment into something friendlier. Subtle radial glows (a faint blue-violet `glow.webp` plate behind hero) replace hard gradients. Loom's depth is atmospheric, not graphic.

**Key Characteristics:**
- Atlassian Blue (`#1868db`) as the single brand action color, used liberally on primary CTAs
- Pure white (`#ffffff`) page canvas — no off-white tinting
- Co-branded Atlassian / Loom lockup in nav (small uppercase ATLASSIAN tag above Loom wordmark)
- Fully-pill (`9999px`) buttons — confident, thumb-friendly, no sharp corners
- Charlie Display-family geometric grotesk at weight 700 for all hero/heading text
- Dark charcoal product containers (`#27282b`) with 16–24px rounded corners — softened product moments
- Subtle radial glow plates behind hero — atmospheric depth, no harsh gradients
- AI-feature callouts framed in sparkle-icon + light-tint panels (`#e7eefb`) — feature-rich, not overwhelming
- Generous whitespace and conservative type scale — productivity-tool restraint

## Colors

### Primary
- **Atlassian Blue** (`#1868db`): The signature brand action color. Applied to every primary CTA ("Get Loom for free"), the Atlassian-mark logo tile, link hovers, and selected states. Pure saturated blue — no tints, no shifts.
- **Hover Blue** (`#3860be`): A darker, slightly desaturated blue used on hovered links and pressed CTA states. Adds a "pressed" sensation without leaving the blue family.
- **Loom Black** (`#101214`): Primary text on light surfaces — headings, body. A near-black with a hair of cool warmth, lifted off pure `#000` for screen comfort.

### Secondary / Accent
- **Soft Blue Tint** (`#e7eefb`): Background fill for the secondary "Contact Sales" / "Install Chrome Extension" pill buttons. A near-white blue that signals interactive without competing with the primary CTA.
- **Link Default** (`#1868db`): Inline links use the same brand blue at default state.
- **Link Hover** (`#3860be`) + underline: Hovered links shift to deep blue with a 1px underline.

### Neutrals & Text
- **Loom Black** (`#101214`): Primary heading and body text.
- **Body Slate** (`#292a2e`): Slightly lighter text variant for paragraph copy beneath hero, footnotes, and dense content blocks. Decoration: underline 1px on inline links.
- **Mid Gray** (`#7d818a`): Secondary text — meta, captions, deemphasized nav labels.
- **Pure White** (`#ffffff`): Page canvas, button text on dark fills, chrome surfaces.

### Surface & Backgrounds
- **Page Canvas** (`#ffffff`): Default page background, no tinting.
- **Product Canvas Dark** (`#27282b`): Dark charcoal container around hero product video and feature mockups. Slightly cool, nearly black.
- **Product Canvas Deep** (`#1f2024`): A second darker variant used for deeper product chrome — tooltips, video timeline fills.
- **Soft Lavender-Blue Wash** (`#f4f6fb`): Occasional section background for testimonial bands and logo carousel rails.

### Borders
- **Border Subtle** (`rgba(16, 18, 20, 0.08)`): Hairline borders on cards and dividers.
- **Border Default** (`#dfe1e6`): Standard 1px input and card border, Atlassian-system-derived.
- **Focus Ring** (`#1868db` at 40% opacity): 2px blue ring on keyboard focus.

### AI / Feature Accents
- **Sparkle Purple** (`#8777d9`): Reserved for AI-feature iconography — sparkle/wand glyphs marking AI-powered features (auto-titles, summaries, transcripts). The only purple in the system.
- **Sparkle Pink-Lavender** (`#c8a8ff`): Occasional gradient-stop partner for the sparkle accent on AI panels.

### Gradient System
- Loom's gradients are **soft and atmospheric**, not graphic. The hero ships with a subtle `glow.webp` plate — a faint radial blue-to-transparent wash that sits behind the headline. AI feature panels occasionally use a gentle lavender-to-blue diagonal gradient (`linear-gradient(135deg, #c8a8ff 0%, #1868db 100%)` at ~10% opacity) as a tinted background. No hard banded gradients, no rainbow flourishes.

## Typography

### Font Family
- **Primary Display & Body**: Charlie Display, Charlie Text (Atlassian's proprietary family — geometric grotesk with humanist warmth). Fallback: `-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif`.
- **Monospace**: Not used in marketing surfaces. Code blocks (in docs only) fall back to `ui-monospace, SFMono-Regular`.
- **OpenType Features**: Standard ligatures, `case` and `cv01` enabled for slightly straighter capital terminals.

*Note: Charlie is Atlassian's commercial typeface. For external implementations, **Inter** at weight 700 or **Plus Jakarta Sans** at weight 700 ship as close substitutes; both share the geometric-with-humanist-warmth character.*

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Display Hero | Charlie Display | 80–96px (5–6rem) | 700 | 1.05 | -0.01em | Landing hero ("One video is worth a thousand words") |
| Display Large | Charlie Display | 64px (4rem) | 700 | 1.08 | -0.01em | Section opener heads |
| Display | Charlie Display | 48px (3rem) | 700 | 1.10 | -0.005em | Feature-block headlines |
| Section Heading | Charlie Display | 36px (2.25rem) | 700 | 1.15 | normal | Sub-section heads |
| Sub-heading Large | Charlie Display | 28px (1.75rem) | 700 | 1.20 | normal | Card titles |
| Sub-heading | Charlie Display | 24px (1.5rem) | 600 | 1.25 | normal | Feature titles, callouts |
| Sub-heading Small | Charlie Display | 20px (1.25rem) | 600 | 1.30 | normal | Small card heads |
| Body Large | Charlie Text | 20px (1.25rem) | 400 | 1.50 | normal | Hero supporting copy |
| Body | Charlie Text | 16px (1rem) | 400 | 1.55 | normal | Standard reading text |
| Body Small | Charlie Text | 14px (0.875rem) | 400 | 1.50 | normal | Captions, helper text |
| Nav Link | Charlie Text | 16px (1rem) | 600 | 1.00 | normal | Top nav, with small dropdown caret |
| Button | Charlie Text | 16px (1rem) | 700 | 1.00 | normal | Pill CTAs — bold, never uppercase |
| Brand Tag | Charlie Display | 11px (0.69rem) | 700 | 1.00 | 0.08em | "ATLASSIAN" lockup label only |
| Caption | Charlie Text | 12px (0.75rem) | 400 | 1.40 | normal | Footer legal, micro-meta |

### Principles
- **Bold weight is the brand**: every headline runs at weight 700. Loom doesn't whisper — it states. The geometric warmth of Charlie at heavy weight does the work of being friendly without going light.
- **No uppercase chrome**: button labels are mixed case, weight 700, no letter-spacing tricks. The only uppercase moment is the tiny "ATLASSIAN" tag above the Loom wordmark.
- **Tight but not crushing line-height**: hero headlines lock to 1.05 for density without overlapping descenders. Body relaxes to 1.50–1.55 for comfortable reading.
- **Subtle negative tracking on display only**: a hair of `-0.01em` on hero text, returning to normal at 28px and below.
- **Two effective weights**: 700 (headings + buttons) and 400 (body). Weight 600 used sparingly for sub-headings and nav links to bridge the gap.
- **No italics, no monospace flourishes**: Loom's voice is direct and one-tone.

## Layout

### Spacing System
- Base unit: 8px
- Scale: 4px, 8px, 12px, 16px, 24px, 32px, 48px, 64px, 96px, 128px, 160px
- Notable: Loom uses generous mid-range values (24–48px) heavily — sections breathe but don't shout. Hero CTAs sit ~32px below the supporting paragraph; section-to-section runs 96–128px on desktop.

### Grid & Container
- Max content width: ~1200px for centered content; ~1280px for the dark product container (slightly wider than text)
- Hero: centered single-column, max-width ~960px for headline, ~720px for sub-paragraph
- Use-case cards: 4-column grid on desktop, 2-column tablet, 1-column mobile
- Logo carousel: full-width band, logos auto-scrolling
- Testimonial section: 1- or 2-up cards, max-width 1200px

### Whitespace Philosophy
- **Productivity-tool restraint**: each section gets 96–128px of vertical air. Not editorial-magazine wide, not SaaS-cramped — calibrated for "I'm here to learn, not to admire."
- **Centered hero pacing**: hero text centered, with substantial padding above and below before the product container drops in
- **Light/dark alternation**: white sections alternate with the dark product container moments to provide visual rhythm without hard dividers

### Border Radius Scale
- Small (8px): Inputs, small chips, dense UI
- Medium (16px): Cards, testimonial blocks, secondary containers
- Large (24px): Hero product container, large feature mockups
- Pill (9999px): All buttons, AI badges, brand tags
- No 0px: Loom does not use sharp rectangular corners anywhere in the marketing surface. Soft-everything is an explicit choice.

## Elevation & Depth

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | No shadow | Page canvas, body text, structural sections |
| Hairline (Level 1) | `0 1px 2px rgba(16, 18, 20, 0.08)` | Default button rest, input rest |
| Subtle Card (Level 2) | `0 2px 8px rgba(16, 18, 20, 0.06)` | Use-case cards, testimonial cards at rest |
| Card Hover (Level 3) | `0 8px 24px rgba(16, 18, 20, 0.10)` + `translateY(-2px)` | Hovered cards, interactive panels |
| Hero Product (Level 4) | `0 24px 60px rgba(16, 18, 20, 0.12)` | Dark product container, primary product moments |
| Branded CTA Hover (Level 5) | `0 4px 12px rgba(24, 104, 219, 0.24)` | Primary pill button hover — blue-tinted glow |

**Shadow Philosophy**: Loom's depth is **atmospheric and physical** — soft, blurred, biased downward, modeled on real ambient light. Every shadow runs through `rgba(16, 18, 20, ...)` (the cool-black text color) so shadows feel chromatically integrated with text rather than disconnected pure-black drops. The only colored shadow is the brand-blue glow on primary CTA hover, which lights the pill from within rather than dropping below it.

### Decorative Depth
- Soft drop shadows pair with 16–24px rounded corners to feel cushioned
- The hero glow plate creates a third depth tier behind the headline — atmospheric, not structural
- No inset shadows, no offset stamps, no neumorphism — just clean ambient lift

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

**Primary Pill (Brand Blue)**
- Background: Atlassian Blue (`#1868db`)
- Text: Pure White (`#ffffff`)
- Padding: 12px 24px (compact), 14px 28px (standard hero CTA)
- Radius: `9999px` (fully pill)
- Border: none
- Shadow: `0 1px 2px rgba(16, 18, 20, 0.08)` — subtle elevation
- Font: 16px Charlie Text weight 700, no letter-spacing
- Hover: background shifts to `#1453b8`, shadow deepens to `0 4px 12px rgba(24, 104, 219, 0.24)`
- Use: "Get Loom for free", every primary conversion CTA

**Secondary Pill (Light Blue Tint)**
- Background: Soft Blue Tint (`#e7eefb`)
- Text: Loom Black (`#101214`)
- Padding: 12px 24px
- Radius: `9999px`
- Border: none
- Optional leading icon: 16×16px stroke-style glyph (download arrow, sparkle, chrome logo)
- Font: 16px Charlie Text weight 700
- Hover: background shifts to `#d6e2f7`
- Use: "Contact Sales", "Install Chrome Extension", "Watch demo"

**Tertiary Text Link**
- Background: transparent
- Text: Atlassian Blue (`#1868db`), no underline default
- Hover: text shifts to `#3860be` with `underline 1px`
- Use: in-paragraph links, "Learn more →" inline CTAs

**Dark Surface Pill**
- Background: Pure White (`#ffffff`)
- Text: Loom Black (`#101214`)
- Radius: `9999px`
- Use: CTA inverted onto the dark product canvas — same pill geometry, flipped for contrast

### Cards & Containers

**Product Container (Dark)**
- Background: `#27282b`
- Radius: `24px` (large outer rounding)
- Padding: 24–48px
- Shadow: `0 24px 60px rgba(16, 18, 20, 0.12)` — soft atmospheric lift
- Use: Hero video frame, feature product mockups, demo carousels

**Use-Case Card (Light)**
- Background: `#ffffff`
- Border: `1px solid #dfe1e6` or borderless with `0 2px 8px rgba(16, 18, 20, 0.06)` shadow
- Radius: `16px`
- Padding: 32px
- Hover: shadow deepens to `0 8px 24px rgba(16, 18, 20, 0.10)`, lift `translateY(-2px)`
- Use: "Sales / Engineering / Support / Design" feature cards

**Testimonial Card**
- Background: `#f4f6fb` (lavender-blue wash)
- Radius: `16px`
- Padding: 32px
- Internal: avatar (40px circle) + name + role + quote
- Use: customer testimonial carousel

### Badges / Tags / Pills

**AI Sparkle Badge**
- Background: linear-gradient(135deg, `#c8a8ff` 0%, `#e7eefb` 100%)
- Text: `#101214`
- Padding: 4px 10px
- Radius: `9999px`
- Leading icon: 12×12px sparkle glyph in `#8777d9`
- Font: 12px Charlie Text weight 700
- Use: "AI" feature flags — auto-titles, summaries, transcripts

**Logo Carousel Pill**
- Background: transparent
- Border: none
- Use: company logos rendered at consistent ~24px height in monochrome `#7d818a`

### Inputs & Forms
- Background: `#ffffff`
- Border: `1px solid #dfe1e6`
- Radius: `8px`
- Font: 16px Charlie Text weight 400
- Text color: `#101214`
- Placeholder: `#7d818a`
- Focus: border shifts to `#1868db`, focus ring `0 0 0 3px rgba(24, 104, 219, 0.25)`
- Padding: 12px 14px

### Navigation
- Top nav: white bar, ~72px tall, generous horizontal padding
- Left: Atlassian-Loom co-brand lockup — blue square Atlassian mark + tiny "ATLASSIAN" cap-tag + Loom wordmark
- Center: nav links with dropdown carets ("Apps ▾", "Solutions ▾", "Resources ▾"), plus flat links ("Enterprise", "Pricing", "Sign In")
- Right: primary blue pill "Get Loom for free" + secondary tint pill "Contact Sales"
- Links: Charlie Text 16px weight 600, color `#101214`
- Hover: link color shifts to `#1868db`
- Sticky: fixed at top with subtle `0 1px 0 rgba(16, 18, 20, 0.04)` divider on scroll

### Decorative Elements

**Hero Glow Plate**
- A soft radial blue-violet wash positioned behind the hero headline
- Implemented as a `glow.webp` plate or CSS `radial-gradient(ellipse at center, rgba(24, 104, 219, 0.12) 0%, transparent 70%)`
- Provides depth without competing with type

**Sparkle Glyphs**
- 4-point star/sparkle icons in `#8777d9` mark every AI feature
- Sized 12–24px depending on context (badge vs. feature heading)
- Pair with brief AI-action labels — "Auto-title", "Summarize", "Transcribe"

## Do's and Don'ts

### Do
- Use Atlassian Blue (`#1868db`) for every primary CTA — preserve its instant-recognition role
- Default to fully-pill (`9999px`) buttons — the shape is non-negotiable
- Keep heading weight at 700 throughout — the geometric grotesk reads warm at heavy weight
- Use the dark charcoal (`#27282b`) container with 24px corners for product video moments
- Pair soft drop shadows with rounded corners — depth is atmospheric, not graphic
- Use the soft blue tint (`#e7eefb`) for secondary pills — subtle but unmistakably interactive
- Mark AI features with the sparkle glyph in `#8777d9` and a gradient-tinted badge
- Stick to mixed case — no uppercase chrome anywhere except the tiny ATLASSIAN tag
- Lead headlines with the value prop, not the feature ("One video is worth a thousand words")

### Don't
- Don't use sharp 0px corners on any button or card — Loom is soft-everything
- Don't introduce a second brand color — blue is the action color, period
- Don't use uppercase button labels with letter-spacing — that's a different system
- Don't use light-weight headings (300, 400) — bold 700 is the brand
- Don't replace the soft drop shadows with hard offset stamps — atmospheric only
- Don't use the sparkle purple (`#8777d9`) for non-AI moments — it's a feature flag
- Don't tint the page canvas — Loom's white is pure `#ffffff`
- Don't use harsh banded gradients — only soft radial glows or subtle diagonals at low opacity
- Don't crowd the hero — generous whitespace is the productivity-tool signal

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile Small | <375px | Single-column, hero drops to 40px, CTAs stack full-width |
| Mobile | 375–640px | Single-column, 48–56px hero, CTAs stack |
| Tablet | 640–1024px | 2-column use-case grid, 64–72px hero |
| Desktop | 1024–1280px | 4-column use-case grid, 80–88px hero |
| Large Desktop | ≥1280px | Maximum 96px hero, 1200–1280px container |

### Touch Targets
- Primary pill CTA: min 48px tall on mobile, 16–20px horizontal padding for thumb confidence
- Nav links: 44px+ tap zones on collapsed mobile menu
- Carousel arrows: 48×48px circular tap targets

### Collapsing Strategy
- **Nav**: full horizontal nav collapses to hamburger on tablet and below; full-screen overlay menu on open with the same pill CTAs at the bottom
- **Hero**: 96px → 80px → 64px → 48px → 40px progressive scaling, weight 700 maintained throughout
- **Use-case grid**: 4 → 2 → 1 column collapse; cards keep 16px radius and shadow at all sizes
- **Product container**: 24px outer radius reduces to 16px on mobile, padding tightens from 48px to 24px
- **CTAs**: side-by-side on desktop, stacked full-width on mobile with 12px vertical gap
- **Section spacing**: 128px desktop → 64px mobile

### Image Behavior
- Product mockups maintain dark-container framing across all breakpoints
- Logo carousel speeds up scroll on mobile, logos resize from 32px to 24px height
- Hero glow plate scales with hero text — never crops, never disappears
- Avatars in testimonials lock to 40px round across all sizes

---

## Agent Prompt Guide

### Quick Color Reference
- Primary CTA: Atlassian Blue (`#1868db`)
- CTA Hover: Deep Blue (`#1453b8`) or link-state (`#3860be`)
- Page Background: Pure White (`#ffffff`)
- Primary Text: Loom Black (`#101214`)
- Body Slate: (`#292a2e`)
- Mid Gray: (`#7d818a`)
- Secondary Pill Tint: Soft Blue (`#e7eefb`)
- Product Canvas: Dark Charcoal (`#27282b`)
- Wash Background: Soft Lavender-Blue (`#f4f6fb`)
- AI Accent: Sparkle Purple (`#8777d9`)
- Border Default: (`#dfe1e6`)
- Focus Ring: `0 0 0 3px rgba(24, 104, 219, 0.25)`
- Card Shadow: `0 2px 8px rgba(16, 18, 20, 0.06)` rest, `0 8px 24px rgba(16, 18, 20, 0.10)` hover

### Example Component Prompts
- "Create a hero section on pure white (`#ffffff`) with a centered headline at 88px Charlie Display weight 700, line-height 1.05, color `#101214`. Below it, a 20px Charlie Text weight 400 paragraph in `#292a2e` at max-width 720px. Two pill CTAs: primary `#1868db` background with white 16px weight 700 text, secondary `#e7eefb` background with `#101214` text, both at `9999px` radius and 14px 28px padding."
- "Design a use-case card on `#ffffff` with `16px` border-radius, `0 2px 8px rgba(16, 18, 20, 0.06)` shadow. Title at 24px Charlie Display weight 700 in `#101214`, body at 16px weight 400 in `#292a2e`. Hover lifts to `0 8px 24px rgba(16, 18, 20, 0.10)` with `translateY(-2px)`."
- "Build a dark product container at `#27282b` with `24px` border-radius and `0 24px 60px rgba(16, 18, 20, 0.12)` shadow. Wrap a 16:9 product video inside with 24–48px internal padding. Reserve a fully-pill `#ffffff` CTA at the bottom for inverted-state actions."
- "Create an AI feature badge — fully-pill `9999px`, gradient background `linear-gradient(135deg, #c8a8ff 0%, #e7eefb 100%)`, leading 12×12px sparkle glyph in `#8777d9`, label at 12px Charlie Text weight 700 in `#101214`, padding 4px 10px."
- "Design a testimonial card on `#f4f6fb` with `16px` radius and 32px padding. 40px circular avatar at top-left, name in 16px weight 700, role in 14px weight 400 `#7d818a`, quote in 18px weight 400 line-height 1.5 `#101214`."

### Iteration Guide
1. Default to pill (`9999px`) for all buttons and AI badges — never sharp, never mid-range on actions
2. Headings always weight 700 in Charlie Display — the geometric warmth at bold is the brand
3. Atlassian Blue (`#1868db`) is the only CTA color — secondary pills use the soft `#e7eefb` tint
4. Page canvas is pure white (`#ffffff`) — no off-white tinting, no warmth shift
5. Product moments live inside dark `#27282b` containers with 24px radius and atmospheric shadow
6. AI features always carry the sparkle glyph in `#8777d9` plus a gradient-tinted badge
7. Shadows are soft, blurred, downward-biased — through `rgba(16, 18, 20, ...)` for chromatic harmony
8. Mixed case everywhere — uppercase only on the tiny ATLASSIAN co-brand tag (11px, 0.08em tracking)
9. Generous whitespace: 96–128px section spacing on desktop, 64px on mobile
10. Hero glow plate behind the headline adds depth without competing — atmospheric, never graphic
