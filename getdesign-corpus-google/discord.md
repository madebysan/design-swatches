---
version: alpha
name: "Discord"
description: "Token-first design system reference for Discord."

colors:
  background: "#ffffff"
  surface: "#1eaedb"
  surface-elevated: "#f5f5f5"
  ink: "#000000"
  ink-muted: "#f6f6fe"
  primary: "#5865f2"
  on-primary: "#ffffff"
  border: "#404eed"
  focus-ring: "#5865f2"
  success: "#22c55e"
  warning: "#f59e0b"
  error: "#ef4444"
  shadow-soft: "#d9d9d9"

typography:
  display-hero:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 82px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -1px
  display:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 57px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  heading-section:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.25px
  heading-sub:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 33px
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

# Discord Design System

## Overview

Discord's website is a warm, cartoony product surface that doesn't take itself seriously, even though it sits behind a hundred-million-user chat platform. The page reads like a kids' book cover that happens to be selling software: chunky uppercase headlines, friendly mascot characters mid-action, and the signature Blurple (`#5865F2`) anchoring every primary moment. Where most B2C tech homepages chase neutrality, Discord leans hard into illustration and play — Wumpus, Clyde, and a small zoo of game-coded characters drop into hero sections, scroll into corners, and peek out from feature cards. The composition is loud, generous, and unapologetically gamer-adjacent.

The custom typeface `ABC Ginto Discord Nord` does the heaviest lifting in the visual identity. Display headlines run at weights 700–800 in **uppercase** with negative letter-spacing (`-0.82px` at 82px display) and aggressively tight line-height (`0.41`–`0.93`) — letterforms practically stack on top of each other for a stamped, almost impact-poster feel. Body and UI shift to the friendlier `ABC Ginto Discord` (mixed case, weight 400–500), and the in-product `gg sans` shows up wherever real chat UI is rendered. Three sibling typefaces handle three jobs: Nord shouts, Discord speaks, gg sans operates.

What distinguishes Discord most is its **gradient-driven section backgrounds**. The `--bg-gradient-*` token system runs deep — Aurora, Sunset, Cotton Candy, Lofi Vibes, Blurple Twilight, Crimson Moon, Midnight Blurple, Forest, Sepia, Chroma Glow, Hanami, Sunrise, Strawberry Lemonade, Mint Apple, Citrus Sherbert, Dusk, Mars, Easter Egg, Neon Nights, Retro Raincloud, Retro Storm, Desert Khaki, Under the Sea — each with 1–5 stops. Sections swap themes top-to-bottom like a comic book turning pages, and Blurple stays the only constant across the parade. Combined with chunky `16px` border radii on every card and button, this gives the system its trademark "soft toy" geometry: nothing sharp, nothing sterile, everything rounded and saturated.

**Key Characteristics:**
- ABC Ginto Discord Nord at weights 700–800, **always uppercase** for display — chunky, stamped, poster-like
- Blurple (`#5865F2`) as the single brand constant across rotating gradient sections
- Multi-theme gradient backgrounds (Aurora, Sunset, Cotton Candy, Blurple Twilight, etc.) — each section gets a "mood"
- Chunky `16px` radius as the default — soft-toy roundness everywhere
- Hover micro-shifts (`translate(2px, -2px)` on cards, `translateY(-10px)` on dropdowns) — playful jiggle, not slick fade
- Illustrated mascots and game-coded characters as the primary visual anchors — typography shares the stage with Wumpus, Clyde, and friends
- Retro-pixel touches and Quest/server-themed iconography hint at the gamer DNA without going full 8-bit
- Tight uppercase display tracking (`-0.82px` to `-0.48px`) keeps the impact-poster feel

## Colors

### Primary Brand
- **Blurple** (`#5865F2`): The defining brand color. Primary CTA backgrounds, link accents, focus outlines, and the spine of every gradient that includes it. Discord's only non-negotiable color.
- **Blurple Hover Cyan** (`#1EAEDB`): Hover-state replacement for primary blurple buttons — the CTA gets brighter and friendlier on hover, not darker.
- **Deep Blurple** (`#404EED`): Secondary Blurple tint, the default deep value behind many "Twilight" gradient hero sections.

### Brand Scale (Blurple ladder)
- **Brand 100** (`hsl(240, 78%, 98%)` ≈ `#F6F6FE`): Lightest tint, washed background panels.
- **Brand 200/230/260/300/330/345/360/400/430/460/500/530**: Mid-tier blurples from very pale to mid-saturation, used for hover surfaces, decorative panels, and badge fills.
- **Brand 560/600/630/660** (`#5865F2` family): Core action color range.
- **Brand 700/730/760/800/830/860/900**: Deep navy-blurples, used for dark-mode surfaces, navigation backgrounds, and footer panels. `Brand 900` (`hsl(232, 50%, 3%)` ≈ `#040514`) functions as near-black with brand undertone.

### Surface Neutrals
- **White** (`#FFFFFF`): Primary page surface for marketing pages, default button background, primary text on dark.
- **Black** (`#000000`): Pure black — primary text on white, icon strokes, dark-section text inversions.
- **Discord Slate** (`#23272A`): The legacy product background tone — used in older sections, footer, and dark UI moments. Pairs with `#FFFFFF` text.
- **Discord Gray** (`#333333`): Secondary text on light surfaces.
- **Hover Gray** (`#565656`): Universal link hover color — every link, regardless of starting color, drifts toward this neutral mid-gray on hover.
- **Animated Background Not-Black** (`hsl(240, 7%, 5%)` ≈ `#0D0D0F`): The "almost black" used for animated gradient hero sections — slightly blue-undertoned so it never feels flat.

### Link & Utility
- **Link Blue** (`#00B0F4`): The in-product chat link color, surfaces in marketing where text-link styling is needed. Distinct from Blurple — Blurple is action, Link Blue is information.
- **LoL Text Light** (`hsl(41, 50%, 59%)` ≈ `#C9A968`): Warm gold for League-of-Legends-themed sections.
- **LoL Text Dark** (`hsl(37, 81%, 32%)` ≈ `#92560F`): Deeper gold companion.

### Gradient System (the signature)
Discord's themed gradients are the visual identity. Each gradient is a 2–5 stop set; below are the primary themes:

- **Blurple Twilight**: `hsl(234, 80%, 54%)` → `hsl(245, 64%, 31%)` — the default brand hero gradient.
- **Aurora**: 4-stop, deep navy → teal → mint, used for "explore" and feature sections.
- **Midnight Blurple**: deep navy `hsl(259, 75%, 11%)` → mid blurple — quieter night-sky moments.
- **Cotton Candy**: pastel pink → soft blue, friendly "join a server" sections.
- **Sunset**: warm violet → coral.
- **Sunrise**: pink → coral → yellow, 3-stop dawn gradient.
- **Lofi Vibes**: pale blue → mint → sage, the chillout-room aesthetic.
- **Hanami**: cherry-blossom pink → cream → sage.
- **Forest**: deep green stack, 5-stop.
- **Crimson Moon**: deep red → black, intense gaming-night moments.
- **Chroma Glow**: 5-stop neon teal → magenta → blue.
- **Citrus Sherbert / Strawberry Lemonade / Mint Apple / Mars / Sepia / Desert Khaki / Dusk / Easter Egg / Neon Nights / Retro Raincloud / Retro Storm / Under the Sea**: themed scenes used to color-code feature sections, communities, and gameplay moods.

### Shadow & Glow
- **Soft Purple Drop** (`rgba(69, 42, 124, 0.1) 0px 3px 68px 0px`): The signature card shadow — large, soft, blurple-tinted. Not gray. Subtle but unmistakable.
- **Hover Lift Shadow** (`rgba(0, 0, 0, 0.2) 0px 8px 15px`): Slightly heavier on white-card hover.

## Typography

### Font Family
- **Display**: `ABC Ginto Discord Nord` (weight 700–800, uppercase) with fallback `Arial`, `sans-serif`
- **UI / Body**: `ABC Ginto Discord` (weight 400–500, mixed case)
- **Product / Chat**: `gg sans` (weight 400, the in-product Discord client typeface)
- **Fallback**: `ABC Ginto Normal` for pages that haven't migrated to the Discord-branded variant
- **OpenType Features**: Standard ligatures; no stylistic alternates — the typeface character carries everything.

*Note: ABC Ginto Discord and ABC Ginto Discord Nord are custom commissions from Dinamo (`abcdinamo.com`). For external work, use Ginto Nord and Ginto Normal directly, or substitute `Druk Wide` (Nord) and `Inter` / `Söhne` (body) as web-safe alternatives.*

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Transform |
|------|------|------|--------|-------------|----------------|-----------|
| Display Hero | ABC Ginto Discord Nord | 82px (5.13rem) | 700 | 0.41 | -0.82px | UPPERCASE |
| Display Large | ABC Ginto Discord Nord | 62px (3.88rem) | 700 | 1.20 | -0.62px | UPPERCASE |
| Display | ABC Ginto Discord Nord | 56px (3.50rem) | 700 | 0.86 | -0.56px | UPPERCASE |
| Section Heading | ABC Ginto Discord Nord | 48px (3.00rem) | 800 | 0.93 | -0.48px | UPPERCASE |
| Sub-heading Compact | ABC Ginto Discord Nord | 22px (1.38rem) | 700 | 0.80 | -0.66px | UPPERCASE |
| Lead Paragraph | ABC Ginto Discord | 20px (1.25rem) | 400 | 1.30 | 0.32px | — |
| Body Large | ABC Ginto Discord | 20px (1.25rem) | 400 | 1.30 | 0.25px | — |
| Body | ABC Ginto Discord | 16px (1.00rem) | 400 | 1.50 | normal | — |
| Body Medium | ABC Ginto Discord | 16px (1.00rem) | 500 | 1.20–1.38 | normal | — |
| Nav / Button | ABC Ginto Discord | 16px (1.00rem) | 500 | 1.20 | 0.25px | — |
| Caption | ABC Ginto Discord | 14px (0.88rem) | 500 | 1.30 | 0.25px | — |
| Product Body | gg sans | 16px (1.00rem) | 400 | 1.50 | normal | — |
| Long Link | ABC Ginto Discord | 18px (1.13rem) | 500 | 1.94 | normal | — |

### Principles
- **Uppercase Nord for every display moment**: Headlines never run in mixed case. The combination of weight 700–800, uppercase, and tight tracking is the brand's defining typographic gesture.
- **Aggressively tight display line-height**: Hero headlines run at `0.41`–`0.93` line-height — letterforms compress vertically into a stamped block. This is intentional, not a bug.
- **Negative letter-spacing scales with size**: From `-0.82px` at 82px down to `-0.48px` at 48px. Sub-display sizes tighten further (`-0.66px` at 22px) for badge-like compression.
- **Mixed-case body, weight 400–500**: ABC Ginto Discord handles all reading and UI work in friendly mixed case. No bold (700) on body — the contrast is between Nord display and Discord body, not between weights within one face.
- **Three-typeface system, three roles**: Nord = shout. Discord = speak. gg sans = operate. Never mix them within a single context.
- **Positive tracking on body** (`0.25px`–`0.32px`): The body face gets slightly opened tracking for legibility against busy gradient backgrounds.

## Layout

### Spacing System
- Base unit: 4px (scale doubles to 8px for most rhythm)
- Scale: 4px, 7px, 10px, 12px, 16px, 17.5px, 20px, 24px, 32px, 40px, 48px, 80px, 128px, 150px
- Notable: `17.5px` shows up 64 times — Discord's button vertical-padding constant (uneven, but tuned to sit the 16–20px text comfortably). `661px` content-width constant for hero text blocks at desktop.

### Grid & Container
- Max content width: ~1280px for centered marketing content; full-bleed for gradient hero sections
- Hero: full-bleed gradient, content centered with mascot anchored to one side
- Feature sections: alternating two-column (illustration left/right + text)
- Section pacing: each major section gets its own gradient theme — Aurora → Cotton Candy → Sunset → Forest, etc., creating a "scroll through chapters" rhythm

### Whitespace Philosophy
- **Generous vertical pacing**: 80–150px between major sections — the gradient changes need room to breathe
- **Tight headline density**: 0.41 line-height on hero display means the headline itself is compact, but it sits inside a generous section frame
- **Mascot real estate**: illustrated characters get 30–50% of the hero composition — they're not decoration, they're co-leads with the headline

### Border Radius Scale
- **Default**: `16px` for cards, panels, and most surfaces
- **Compact**: `12px` for buttons and small UI
- **Soft**: `14px` for medium-emphasis cards
- **Pill / Round**: `50px` for fully rounded buttons and avatar crops; `60px`–`120px` for oversized image containers
- **Drop Sheet**: `0px 0px 88px 88px` for the signature bottom-curved section terminator
- **Asymmetric**: `40px 0px 0px 40px` for left-rounded image panels in two-column layouts

## Elevation & Depth

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | No shadow | Page canvas, gradient sections, body text |
| Soft Purple (Level 1) | `rgba(69, 42, 124, 0.1) 0px 3px 68px 0px` | Card baseline — the signature blurple-tinted glow |
| Hover Lift (Level 2) | `rgba(0, 0, 0, 0.2) 0px 8px 15px` + `translate(2px, -2px)` | Interactive card hover — heavier shadow + diagonal nudge |
| Float Pop (Level 3) | `translateY(-10px)` (no shadow change) | Featured tile hover, dropdown buttons — the big vertical hop |
| Focus Halo (Level 4) | `outline: 2px solid #5865F2`, `box-shadow: 0 0 0 3px var(--focus-border)` | Keyboard focus on interactive elements — Blurple-rimmed |

**Shadow Philosophy**: Discord's depth system is **soft, warm, and slightly purple-tinted** — atmospheric, not graphic. The signature `0px 3px 68px` is a huge-blur, low-opacity glow that wraps cards in ambient light rather than dropping them onto a hard surface. There are no hard offset shadows, no harsh gray fills — the goal is to make the page feel plush and game-room cozy. When elements interact, the shift is in *transform* more than in shadow: cards lift diagonally, dropdowns hop straight up. Motion does the affordance work that other systems delegate to elevation changes.

### Decorative Depth
- The bottom-curved `88px` section radius creates a faux-Z-axis depth — sections appear to be discrete plates stacked in space
- Mascot illustrations frequently break section boundaries (a Wumpus head pokes above the gradient line) — adding parallax-style depth without actual parallax
- No glassmorphism or backdrop-blur except on sticky nav

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

**Primary Blurple**
- Background: Blurple (`#5865F2`)
- Text: White (`#FFFFFF`)
- Padding: `19.5px 24px`
- Radius: `12px`
- Border: `0px none`
- Shadow: `none` default; `none` on hover (the color shift is the affordance)
- Font: 20px ABC Ginto Discord, weight 400
- Hover: background shifts to `#1EAEDB` (cyan), `transform: translateX(-2px)` (small horizontal nudge)
- Active: background `rgb(6, 10, 11)` (near-black)
- Focus: `outline: rgb(0, 0, 0) solid 2px`, `box-shadow: 0 0 0 3px var(--focus-border)`
- Use: Primary CTA — "Download for Mac", "Open Discord in your browser", "Sign Up"

**White Pill (on dark/gradient surfaces)**
- Background: `#FFFFFF`
- Text: `#23272A` (Discord Slate) or `#000000`
- Padding: `15px 24px`
- Radius: `12px`
- Shadow: `none` default; `rgba(0, 0, 0, 0.2) 0px 8px 15px` on hover
- Hover: `transform: translate(2px, -2px)` — the playful 2-pixel diagonal lift
- Font: 20px ABC Ginto Discord, weight 400
- Use: Primary CTA on dark/gradient hero sections — "Download" on the gradient hero

**Compact White Nav**
- Background: `#FFFFFF`
- Text: `#000000`
- Padding: `10px 16px`
- Radius: `16px`
- Shadow: `none`
- Font: 16px ABC Ginto Discord, weight 500
- Hover: `transform: translate(2px, -2px)`, color stays
- Use: Top-nav "Login" / "Open Discord" buttons

**Translucent Glass (on dark)**
- Background: `rgba(255, 255, 255, 0.1)`
- Text: `#FFFFFF`
- Padding: `17.5px 16px 17.5px 24px` (asymmetric — extra space on left for icon)
- Radius: `16px`
- Border: `0px` default; `2px solid rgba(255, 255, 255, 0.1)` for outlined variant
- Hover: `transform: translateY(-10px)` (the full pop), text shifts to `var(--blurple)`
- Focus: `outline: rgb(88, 101, 242) solid 2px`
- Use: Language dropdown, secondary nav controls on dark hero sections

### Cards & Containers
- Background: White (`#FFFFFF`) on light sections; brand-scale blurple tints (`Brand 100`–`Brand 230`) for soft panels; gradient fills for themed feature cards
- Border: `0px` default — Discord cards use shadow + radius for definition, not borders
- Radius: `16px` (the workhorse), `12px` for compact cards, `40px`–`120px` for oversized hero containers, `0px 0px 88px 88px` for the bottom-rounded "drop sheet" hero pattern (flat top, dramatic bottom curve)
- Shadow: `rgba(69, 42, 124, 0.1) 0px 3px 68px 0px` — the signature soft purple shadow
- Internal padding: 24–48px standard, 80–128px for hero content blocks
- Hover: `transform: translate(2px, -2px)` on interactive cards — diagonal pop, not scale

### Badges / Pills
- Background: brand tint (`Brand 200`–`Brand 300`) or theme gradient stop
- Text: `#000000` or `#FFFFFF` depending on contrast
- Padding: 6–10px vertical, 12–16px horizontal
- Radius: `50px` (full pill) or `16px` (rounded rect)
- Font: 14–16px ABC Ginto Discord, weight 500, `0.25px` tracking
- Use: "NEW" markers, feature tags, server category labels

### Inputs & Forms
- Background: `#FFFFFF` or `Brand 100` (`#F6F6FE`)
- Border: `0px` default with internal shadow, or `1px solid rgba(0,0,0,0.1)`
- Radius: `12px`–`16px`
- Font: 16px ABC Ginto Discord, weight 400
- Text color: `#23272A`
- Placeholder: `#565656`
- Focus: `outline: rgb(88, 101, 242) solid 2px`, `box-shadow: 0 0 0 3px var(--focus-border)` (brand-160 halo)
- Padding: 12–16px vertical, 16px horizontal

### Navigation
- Top nav: white horizontal bar with Discord wordmark logo (left), section links (center), "Login" + "Open Discord" CTAs (right)
- Logo: SVG wordmark, 165×24px at desktop
- Hover dropdowns: large multi-column panels with illustrated category icons and feature lists
- Links: `#000000` weight 500 default, drift to `#565656` on hover (universal hover color across all link variants)
- Sticky behavior: nav remains pinned on scroll, gains `rgba(255,255,255,0.95)` backdrop blur over gradient sections

### Decorative Elements

**Mascot Illustrations**
- Wumpus, Clyde, Quest characters drop into hero sections at large scale (often 300–600px tall)
- Always positioned to feel "in motion" — leaning, peeking, mid-jump
- Color-treated to match the section's gradient theme, not always brand-canonical colors

**Bottom-Curve Drop Sheets**
- Sections frequently terminate with a `0px 0px 88px 88px` radius — flat top, deep curved bottom
- Creates a "torn paper" or "comic panel" transition between gradient sections

**Hover Lift Pattern**
- Two flavors: `translate(2px, -2px)` (small diagonal pop, used on cards/buttons) and `translateY(-10px)` (big vertical hop, used on prominent dropdowns/featured tiles)
- Always paired with a color or shadow shift for compounded affordance

## Do's and Don'ts

### Do
- Use ABC Ginto Discord Nord at weights 700–800, **always uppercase**, for every display headline — this is the brand's loudest signal
- Apply Blurple (`#5865F2`) as the only constant across rotating gradient themes — it's the spine of the system
- Use chunky `16px` radius as the default — softness is the brand
- Use the soft purple shadow (`rgba(69, 42, 124, 0.1) 0px 3px 68px 0px`) for cards — never gray drop shadows
- Use `translate(2px, -2px)` on card hover and `translateY(-10px)` on featured tile hover — these are the signature motion gestures
- Pair every major section with its own themed gradient (Aurora, Sunset, Cotton Candy, etc.) — variety is the visual rhythm
- Use mascot illustrations as co-equal hero elements, not decoration
- Use `gg sans` only inside actual product UI screenshots/contexts; ABC Ginto Discord for everything else
- Use uppercase Nord at tight `0.41`–`0.93` line-height — the compressed letterform stack is intentional
- Apply tight negative letter-spacing (`-0.82px` to `-0.48px`) on uppercase display

### Don't
- Don't write display headlines in mixed case — uppercase Nord is non-negotiable
- Don't use Nord for body text or buttons — it's display-only
- Don't use a gray drop shadow — Discord's shadow is purple-tinted and large-blur
- Don't use sharp `0px` corners on interactive elements — every button, card, and panel rounds at 12px+
- Don't introduce a different primary color — Blurple is sacred, themed gradients orbit around it
- Don't use blurred-glass / glassmorphism backgrounds on cards — Discord cards are solid white or solid gradient stops
- Don't pair Nord with another bold display face — let it carry the typographic load alone
- Don't animate hovers with scale (`transform: scale(1.05)`) — Discord uses translate, not scale
- Don't use neutral page backgrounds in hero sections — every hero gets a themed gradient
- Don't strip mascot illustrations to "clean up" a hero — the characters are the brand

---

## Responsive Behavior

### Breakpoints
Discord ships an unusually granular breakpoint system (every 50px from 240px to 1991px), but the meaningful tiers are:

| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile Small | <400px | Hero Nord drops to 36–48px, single-column, mascot scales below text |
| Mobile | 400–768px | 48–62px hero, stacked CTAs, mascot inline |
| Tablet | 768–1024px | 2-column begins, 62–72px hero, side-by-side mascot |
| Desktop | 1024–1440px | Full multi-column, 72–82px hero |
| Large Desktop | ≥1440px | Maximum hero (82px), 1280px+ container, mascot at full scale |

### Touch Targets
- Primary CTAs: 50–60px tap height on mobile (Discord uses `19.5px` vertical padding = 56px effective height)
- Nav links: 44px minimum touch zone
- Featured tiles: full-width tap targets with `translateY(-10px)` motion preserved on touch (becomes a press-down feedback)

### Collapsing Strategy
- **Nav**: Horizontal links collapse to hamburger; full-screen menu opens with section illustrations preserved
- **Hero**: 82px → 62px → 48px → 36px progressive Nord scaling, uppercase maintained throughout
- **Two-column**: Image+text features collapse to stacked single-column, mascot reorders below or above text
- **Gradient sections**: Theme gradients persist across breakpoints — never simplified to flat color
- **Section spacing**: 150px desktop → 80px tablet → 48px mobile
- **Mascot scale**: Illustrations downscale proportionally but never get cropped — Discord prefers a smaller-but-complete Wumpus over a partial one

### Image Behavior
- Mascot illustrations: SVG wherever possible, retain crispness at all scales
- Product UI screenshots: scaled with art direction — mobile screens show mobile UI, desktop shows desktop UI
- Gradient backgrounds: extend to full bleed, never get letterboxed
- Logo wordmark: scales but never reduces to icon-only

---

## Agent Prompt Guide

### Quick Color Reference
- Primary CTA: Blurple (`#5865F2`)
- Primary CTA Hover: `#1EAEDB` (cyan)
- Page Background: White (`#FFFFFF`) or themed gradient
- Dark Surface: Discord Slate (`#23272A`) or Brand 900 (`#040514`)
- Primary Text on Light: Black (`#000000`) or `#23272A`
- Primary Text on Dark: White (`#FFFFFF`)
- Universal Link Hover: `#565656`
- Link / Info Color: `#00B0F4`
- Card Shadow: `rgba(69, 42, 124, 0.1) 0px 3px 68px 0px`
- Focus Outline: `2px solid #5865F2`

### Example Component Prompts
- "Create a hero section with a Blurple Twilight gradient background (`#404EED` → `#5865F2`). Headline at 82px ABC Ginto Discord Nord weight 700, uppercase, line-height 0.41, letter-spacing -0.82px, color `#FFFFFF`. Place a White CTA button (`#FFFFFF` background, `#23272A` text, `12px` radius, `15px 24px` padding, 20px ABC Ginto Discord weight 400) — on hover apply `transform: translate(2px, -2px)` and `box-shadow: rgba(0,0,0,0.2) 0px 8px 15px`. Anchor a Wumpus mascot illustration to the right side of the hero at 500px tall."
- "Design a feature card on white with `16px` border-radius, no border, and shadow `rgba(69, 42, 124, 0.1) 0px 3px 68px 0px`. Title in ABC Ginto Discord Nord 48px weight 800, uppercase, line-height 0.93, letter-spacing -0.48px. Body in ABC Ginto Discord 16px weight 400, line-height 1.50, color `#23272A`. On hover, apply `transform: translate(2px, -2px)`."
- "Build a Blurple primary button — background `#5865F2`, text `#FFFFFF`, padding `19.5px 24px`, radius `12px`, font 20px ABC Ginto Discord weight 400. Hover: background shifts to `#1EAEDB`, `transform: translateX(-2px)`. Focus: outline `2px solid #000`, box-shadow `0 0 0 3px rgba(88, 101, 242, 0.5)`."
- "Create a translucent glass dropdown — `rgba(255,255,255,0.1)` background, white text, `17.5px 16px 17.5px 24px` asymmetric padding, `16px` radius. On hover, `transform: translateY(-10px)` and text color shifts to `#5865F2`. Focus outline `2px solid #5865F2`."
- "Design a section terminator with a bottom-curved drop sheet — gradient background extending edge-to-edge, terminating with `border-radius: 0px 0px 88px 88px`. Below it, the next section uses a different theme gradient (e.g. Cotton Candy → Lofi Vibes)."

### Iteration Guide
1. Default to ABC Ginto Discord Nord weight 700–800 uppercase for every display heading — uppercase is non-negotiable
2. Keep the radius chunky: `16px` default, `12px` compact, `50px+` for pill/circular. Never below 12px on interactive elements.
3. Use the soft purple card shadow (`rgba(69, 42, 124, 0.1) 0px 3px 68px 0px`) — never gray, never harsh
4. Blurple (`#5865F2`) is the brand spine; themed gradients are the variety. Don't substitute another primary.
5. Negative letter-spacing scales with size: `-0.82px` at 82px, `-0.48px` at 48px, drops to `0.25px` positive at body
6. Hover motion = translate, not scale. `translate(2px, -2px)` for cards, `translateY(-10px)` for featured tiles, `translateX(-2px)` for primary CTAs.
7. Every major section gets its own gradient theme — rotate through Aurora, Sunset, Cotton Candy, Forest, etc.
8. Mascot illustrations are co-leads with the headline — never decoration, never optional
9. Three typefaces, three jobs: Nord shouts, Discord speaks, gg sans operates. Never mix within one context.
