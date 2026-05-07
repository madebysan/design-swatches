---
version: alpha
name: "Sesame Street"
description: "Sesame Sans display over Source Sans Pro body, character-coded primary buttons in sky blue, orange, magenta, purple, and red, all 9999px pill radii."

colors:
  background: "#ffffff"
  surface: "#54585a"
  surface-elevated: "#f5f5f5"
  ink: "#000000"
  ink-muted: "#f30fa2"
  primary: "#14bcf3"
  on-primary: "#ffffff"
  border: "#f78600"
  focus-ring: "#14bcf3"
  success: "#22c55e"
  warning: "#f59e0b"
  error: "#ef4444"
  shadow-soft: "#d9d9d9"

typography:
  display-hero:
    fontFamily: "Sesame Sans, ui-sans-serif, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 300
    lineHeight: 1.05
    letterSpacing: -1px
  display:
    fontFamily: "Sesame Sans, ui-sans-serif, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 300
    lineHeight: 1.1
    letterSpacing: -0.5px
  heading-section:
    fontFamily: "Sesame Sans, ui-sans-serif, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.25px
  heading-sub:
    fontFamily: "Sesame Sans, ui-sans-serif, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0px
  body-large:
    fontFamily: "Sesame Sans, ui-sans-serif, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.5
    letterSpacing: 0px
  body:
    fontFamily: "Sesame Sans, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.5
    letterSpacing: 0px
  button-ui:
    fontFamily: "Sesame Sans, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: 0px
  caption:
    fontFamily: "Sesame Sans, ui-sans-serif, system-ui, sans-serif"
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

# Sesame Street Design System

## Overview

Sesame Street's website is what 55 years of educational television has earned: the right to be unapologetically loud, primary, and joyful in a design landscape that has otherwise migrated toward muted neutrals. The page sits on pure white (`#ffffff`) and a soft warm grey (`#54585a`) for body type, but the chrome is built around five character-coded primary CTA colours arranged like a row of plush toys in a playroom — Cookie Sky Blue (`#14bcf3`), Big Bird Orange (`#f78600`), Abby Magenta (`#f30fa2`), Grover Purple (`#901889`), and Elmo Red (`#e51a1a`). Each colour belongs to a navigation destination — "Watch", "Play", "Learn", "Explore", "Family" — and each button is a fully-rounded `9999px` pill, the way a child would draw a button.

The defining typographic move is the **Sesame Sans / Source Sans Pro contract**. Sesame Sans (a custom rounded grotesk commissioned for the show) handles the display moments at weight 300 — yes, weight 300, because the rounded letterforms are already so warm and chunky that lightening the weight reads as "approachable" rather than "delicate". Source Sans Pro carries every body line, every navigation link, every "PLAY NOW" CTA at weights 400/600/700. UPPERCASE is reserved for buttons and category eyebrows ("ALL ABOUT US", "MEET THE FAMILY") with a warm `0.22px` letter-spacing that pulls the caps slightly apart for kindergarten legibility. Where most kids' brands use a chunky display heavy at weight 800+, Sesame Street goes the opposite direction: rounded display at weight 300, letting the friendly character of the typeface carry the warmth.

What separates Sesame Street from every other primary-color kids' brand (Crayola, Fisher-Price, McDonald's) is the **pill-radius commitment**. The dembrandt extraction confirms `9999px` border-radius appearing 61 times across buttons, search inputs, character avatars, and floating navigation chips — by far the dominant radius in the system. There are no sharp rectangles in primary chrome. There are no 8px brick-cards. Every interactive element is a soft rounded pill, the way a puppet is shaped from foam. The design is character-led photography (Elmo, Big Bird, Cookie Monster) on white seamless backgrounds, then anchored to colourful pill-shaped CTAs that read as the route to play. There's no austerity, no tasteful muted grid — the system is joyful by design and proud of it.

**Key Characteristics:**
- Pure white canvas (`#ffffff`) — playroom-clean, never tinted
- Body text in warm slate (`#54585a`) — softer than black for kid-friendly long-form reading
- Character-coded primary CTAs: Sky Blue (`#14bcf3`), Orange (`#f78600`), Magenta (`#f30fa2`), Purple (`#901889`), Elmo Red (`#e51a1a`)
- Sesame Sans display at weight 300 — rounded grotesk, light weight as warmth
- Source Sans Pro for body, navigation, and primary CTAs at weights 400/600/700
- `9999px` pill radius on buttons, inputs, avatars, and floating chips — 61 confirmed instances
- UPPERCASE button labels with `0.22px` letter-spacing in Source Sans Pro 700 — kindergarten legibility
- Hover state turns every button green (`#0095389`) with a 3px dark border — playful confirmation
- 4px white border (`4px solid #ffffff`) frames character avatars — sticker-style cutout
- 4-corner radius oddity: `4px 4px 8px 8px` on article cards (top corners tighter than bottom)
- Light shadow scale: `rgba(0, 0, 0, 0.1) 0px 3px 6px 0px` and `rgb(255, 255, 255) 0px 0px 0px 4px` for sticker-cutout effect

## Colors

### Primary (the Character Quintet)
- **Cookie Sky Blue** (`#14bcf3`): The "Watch" zone CTA colour — sky blue extracted from the hover/focus context. Reads as Cookie Monster blue. Also appears as the brighter `#21cfff` on default-state buttons. The signature "play video / watch now" colour.
- **Big Bird Orange** (`#f78600`): The "Play" zone CTA colour — also surfaces at `#ff9800` in default-state buttons. Big Bird's signature warmth, used for game-launch and activity CTAs.
- **Abby Magenta** (`#f30fa2`): The "Learn" zone CTA colour — also surfaces at `#ff07a7` in default state. Abby Cadabby's hot-pink magenta, used for educational content and activity CTAs.
- **Grover Purple** (`#901889`): The "Explore" zone CTA colour — also surfaces at `#9d1d96`. Grover's deep purple, used for character-feature and explore-the-world CTAs.
- **Elmo Red** (`#e51a1a`): The "Family" zone CTA colour — also surfaces at `#f91d1d`. Elmo's warm red, used for family-content and parent-resources CTAs.

### Brand Accent
- **Sesame Yellow** (`#ffd400`): The hover-state and focus-state warm yellow that surfaces when any character button is hovered. The single "feedback" colour that ties all five character zones together.
- **Confirmation Green** (`#00b140`): The default state for "ACT NOW" / sign-up CTAs and the universal hover-text colour. Used sparingly as a confirmation accent.
- **Hover Green** (`#009523`): Slightly deeper green that appears as the hover background on neutral CTAs.

### Neutrals & Text
- **Body Slate** (`#54585a`): The workhorse body-text colour — softer than black, warmer than grey, used 657 times across the page. The primary reading colour for kid-and-parent prose.
- **Caption Slate** (`#3d3d3d`): Heading body / link emphasis colour — 50 instances. Slightly darker than body for contrast.
- **Active Black** (`#151515`): Active-state link and pressed-button text colour — only appears on interaction.
- **Light Surface** (`#f8f8f8`): Search-pill and inactive-tab background colour.
- **Hairline Light** (`#eeeeee`): List-item bottom-border colour — barely-visible navigation separator.
- **Chip Light** (`#d8d8d8`): Search-input border, low-emphasis structural lines.
- **Pure White** (`#ffffff`): Page background — used 279 times. The crisp playroom canvas.

### Surface & Borders
- **Page Surface** (`#ffffff`): Default canvas.
- **Tinted Surface** (`#f8f8f8`): Search-input fill, tab inactive state.
- **White Border (sticker-cut)** (`4px solid #ffffff`): The signature avatar / character-frame border — 12 confirmed instances. Used to cut character photography out of its background as a sticker.
- **Hairline Bottom Rule** (`0px 0px 1px solid #eeeeee`): Navigation list-item separators.
- **Search Border** (`1px solid #d8d8d8`): Default search-input outline at rest.
- **Hover Border** (`3px solid #333333`): The signature hover-state border on character buttons — thick, dark, intentional.

### Shadow Colors
- **Card Drop** (`rgba(0, 0, 0, 0.1) 0px 3px 6px 0px`): The standard shadow — 19 confirmed uses. Soft, light, downward — used on featured tiles and elevated cards.
- **Sticker Cutout Ring** (`rgb(255, 255, 255) 0px 0px 0px 4px`): The signature white ring around character avatars — 12 uses. Functions as the sticker-cut outline.
- **Soft Glow** (`rgb(204, 204, 204) 0px 0px 2px 2px`): Tooltip and floating-chip ambient glow.
- **Drawer Drop** (`rgba(0, 0, 0, 0.16) -5px 0px 6px 0px`): Side-drawer left-edge shadow for mobile nav drawer.

### Gradient System
- Sesame Street is **gradient-restrained**. Every character CTA is a flat saturated colour — never blended. Imagery (character photography) carries chromatic richness; surfaces stay solid. The only place gradients appear is in third-party iframe content (video player thumbnails) — never in brand chrome.

## Typography

### Font Family
- **Display**: `Sesame Sans`, weights 300/600/700, fallback chain `ui-sans-serif, system-ui, -apple-system, system-ui, Segoe UI, Roboto, Helvetica Neue, Arial, Noto Sans, ...`. A custom rounded grotesk commissioned for the brand. Used for the hero headlines and character-page openers.
- **Body / UI**: `Source Sans Pro`, weights 400/600/700, fallback chain identical to Sesame Sans. Adobe's open-source humanist sans — workhorse for navigation, body, and primary buttons.
- **Auxiliary / Internationalization**: `Helvetica` with Asian-language fallback chain (`Hiragino Sans GB, STXihei, Microsoft YaHei, WenQuanYi Micro Hei, Hind, MS Gothic, Apple SD Gothic Neo, NanumBarunGothic`) — used for international-character footer disclaimers and territory selectors.
- **OpenType Features**: Standard ligatures only. No stylistic alternates, no opticals — the rounded character of Sesame Sans is in the default character set.

*Note: Sesame Sans is a proprietary commissioned typeface for Sesame Workshop. For external implementations, `Quicksand`, `Hanken Grotesk Rounded`, `Nunito`, or `Inter Rounded` substitute well; Source Sans Pro is freely available via Google Fonts.*

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Transform | Notes |
|------|------|------|--------|-------------|----------------|-----------|-------|
| Display Hero | Sesame Sans | 48px (3.00rem) | 300 | 1.10 | normal | none | Page-front headlines — "Welcome to Sesame Street" |
| Display | Sesame Sans | 24px (1.50rem) | 300 | 1.33 | normal | none | Card titles, sub-section openers |
| Section Heading Large | Source Sans Pro | 20px (1.25rem) | 400 | 1.50 | normal | none | Body-context heads, link-list titles |
| Button Large | Source Sans Pro | 20px (1.25rem) | 400 | 1.15 | normal | none | Large character-zone navigation buttons |
| Sub-Heading UPPER | Source Sans Pro | 18px (1.13rem) | 700 | 1.67 | normal | UPPERCASE | "ALL ABOUT US" eyebrows, category heads |
| Sub-Heading | Source Sans Pro | 18px (1.13rem) | 700 | 1.67 | normal | none | Mixed-case bold sub-heads |
| Button Standard | Sesame Sans | 17px (1.06rem) | 700 | 1.76 | normal | none | Character-coded navigation buttons |
| Section Sub-Heading | Sesame Sans | 17px (1.06rem) | 700 | 1.76 | normal | none | Mid-section heads in Sesame Sans bold |
| Link Bold | Source Sans Pro | 16px (1.00rem) | 600 | 1.63 | normal | none | Featured links in body |
| Body Bold | Source Sans Pro | 16px (1.00rem) | 700 | 1.56 | normal | none | Emphasized body text |
| Body | Source Sans Pro | 16px (1.00rem) | 400 | 1.63 | normal | none | Standard reading text |
| Section Title | Sesame Sans | 16px (1.00rem) | 600 | 1.50 | normal | none | In-card heads at body scale |
| Helvetica Body | Helvetica | 16px (1.00rem) | 400 | 1.00 | normal | none | International-character chrome / disclaimer |
| Caption UPPER | Sesame Sans | 14px (0.88rem) | 700 | 2.14 | 0.22px | UPPERCASE | Section eyebrows — "WATCH NOW", "MEET THE FAMILY" |
| Caption | Source Sans Pro | 14px (0.88rem) | 400 | 1.50 | normal | none | Image captions, fine print |
| Button Compact UPPER | Source Sans Pro | 12px (0.75rem) | 700 | 1.15 | normal | UPPERCASE | Compact CTAs in card footers |

### Principles
- **Two-typeface contract, three operative voices**: Sesame Sans for display + character-zone buttons, Source Sans Pro for body + nav + primary CTAs, Helvetica for international chrome only. Roles do not trade.
- **Light weight as warmth**: Sesame Sans at weight 300 for display is the brand's signature. The rounded letterforms are already chunky enough that lightening the weight reads as "approachable" rather than "delicate" — a deliberate inversion of the kids'-brand convention.
- **Bold on character buttons**: Sesame Sans at weight 700 carries the navigation buttons. The rounded grotesk at heavy weight reads as "press me" without losing the warmth.
- **UPPERCASE for category eyebrows and compact CTAs**: 14px Sesame Sans 700 with `0.22px` letter-spacing on eyebrow labels. 12px Source Sans Pro 700 on compact card CTAs. Mixed case for headlines and body.
- **Generous body line-height**: Source Sans Pro body at 16px / `1.63` line-height — kid-friendly reading rhythm with extra air. Caption at `1.50`, body bold at `1.56`. The system breathes.
- **No tracking adjustments on body**: Body and caption text use default letter-spacing — only the UPPERCASE eyebrows get the warm `0.22px` to pull caps apart for legibility.

## Layout

### Spacing System
- Base unit: `4–5px` for tight chrome, with strong reliance on `8`, `16`, `20`
- Scale: `3.5px, 4px, 5px, 6px, 7px, 8px, 9px, 12px, 14px, 16px, 18.99px, 20px, 21px, 24px, 26px, 32px, 40px, 41px, 45px, 60px`
- Notable: `8px` (43 uses) and `5px` (39) anchor the small-end grid; `16px` (39), `20px` (15), and `60px` (6) carry the section-level spacing. The unusual `18.99px`, `41px`, and `3.5px` values come from a Sass tokenization tied to `1.187rem` design-token quirks rather than strict 8-grid discipline.

### Grid & Container
- Max content width: ~`1200–1280px` for centered content
- Hero: full-bleed character photography with overlaid Sesame Sans 48px headlines
- Feature sections: 3 or 4-column tile grids with consistent 16–20px gutters
- Footer: centered logo with 4-column nav columns and stacked Helvetica disclaimers for international rights

### Whitespace Philosophy
- **Playroom breathing**: 40–60px between major sections. Pages feel like an illustrated children's book, not a stacked landing page.
- **Tile rhythm**: Article and episode tiles use uniform spacing with clear gutters; tiles never touch.
- **Character-anchored composition**: Every hero is anchored by a character photograph. The chrome surrounds the character, never crops or competes.
- **Pill-spacing rhythm**: The 5-button character navigation row sets the visual cadence — five colourful pills evenly spaced, each one a portal.

### Border Radius Scale
- Compact (`8px`): Image cards, modal dialogs (default rectangular containers)
- Asymmetric Article (`4px 4px 8px 8px`): The signature article-card radius — top corners tighter (50 uses)
- Half-circle (`50%`): Modal centerpieces and circular character avatars (2 uses)
- Image fill (`100%`): Internal image elements (25 uses)
- Pill (`9999px`): Buttons, inputs, search, avatars, badges, floating chips (61 uses) — by far the dominant radius
- The system reads either fully-rounded pill or hand-cut asymmetric — no mid-range workhorse.

## Elevation & Depth

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | No shadow | Page canvas, body content, color-block sections |
| Sticker Cutout (Level 1) | `rgb(255, 255, 255) 0px 0px 0px 4px` | Character avatars — the signature sticker-frame ring |
| Card Drop (Level 2) | `rgba(0, 0, 0, 0.1) 0px 3px 6px 0px` | Article tiles, featured content cards (19 uses) |
| Tooltip Glow (Level 3) | `rgb(204, 204, 204) 0px 0px 2px 2px` | Floating chips, tooltips, hint cards |
| Drawer Drop (Level 4) | `rgba(0, 0, 0, 0.16) -5px 0px 6px 0px` | Side-drawer left-edge shadow on mobile nav |
| Hover Border | `3px solid #333333` | Universal hover state on character buttons — thick dark outline |
| Focus Border | `3px solid #cccccc` | Keyboard focus on character buttons — light grey outline |

**Shadow Philosophy**: Sesame Street's depth language is **sticker-and-tile**. The signature elevation is a 4px white outer ring (`rgb(255, 255, 255) 0px 0px 0px 4px`) around character avatars — it acts as a literal sticker outline cutting the character photo out of its background. Article cards lift slightly with a soft 3-6px blur drop. There are no atmospheric multi-layer shadows, no blue-tinted depth, no dark-mode glows. The shadows are the kind a child would draw: a soft outline behind the picture, a thin shadow under the card. The system rewards visual clarity over spatial sophistication, which matches the audience.

### Decorative Depth
- The 4px white sticker ring is the system's most distinctive elevation — character photos appear cut from their backgrounds and pasted onto the page
- Hover-state thick dark borders (`3px solid #333333`) on character buttons function as elevation through outline rather than shadow
- The asymmetric `4px 4px 8px 8px` card radius gives article tiles a hand-cut feel without engaging shadow

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

**Primary Character CTA — Cookie Sky Blue ("Watch")**
- Background: Cookie Sky Blue (`#21cfff` default, `#14bcf3` in hover/focus context)
- Text: Pure White (`#ffffff`)
- Padding: `0px 12px` (height carried by 17px line-height × 1.76)
- Radius: `9999px` (fully pill)
- Border: `0px solid #ffffff` (no border at rest)
- Shadow: `none` at rest
- Font: 17px Sesame Sans weight 700
- Hover: background turns Confirmation Green (`#009523`), text turns Hover Green (`#00b140`), border thickens to `3px solid #333333`
- Active: background drops to `rgba(0, 149, 59, 0.65)` (translucent green), text turns Active Black (`#151515`)
- Focus: background turns Sesame Yellow (`#ffd400`), text turns white, border `3px solid #cccccc`
- Use: "WATCH" navigation chip — Cookie Monster zone

**Primary Character CTA — Big Bird Orange ("Play")**
- Background: Big Bird Orange (`#ff9800` default, `#f78600` in hover/focus)
- Text: Pure White (`#ffffff`)
- Padding: `0px 12px`
- Radius: `9999px`
- Font: 17px Sesame Sans weight 700
- Hover/Active/Focus: identical green/yellow flow as Cookie Sky Blue
- Use: "PLAY" navigation chip — Big Bird zone

**Primary Character CTA — Abby Magenta ("Learn")**
- Background: Abby Magenta (`#ff07a7` default, `#f30fa2` in hover/focus)
- Text: Pure White (`#ffffff`)
- Padding: `0px 12px`
- Radius: `9999px`
- Font: 17px Sesame Sans weight 700
- Hover/Active/Focus: identical green/yellow flow
- Use: "LEARN" navigation chip — Abby Cadabby zone

**Primary Character CTA — Grover Purple ("Explore")**
- Background: Grover Purple (`#9d1d96` default, `#901889` in hover/focus)
- Text: Pure White (`#ffffff`)
- Padding: `0px 12px`
- Radius: `9999px`
- Font: 17px Sesame Sans weight 700
- Hover/Active/Focus: identical green/yellow flow
- Use: "EXPLORE" navigation chip — Grover zone

**Primary Character CTA — Elmo Red ("Family")**
- Background: Elmo Red (`#f91d1d` default, `#e51a1a` in hover/focus)
- Text: Pure White (`#ffffff`)
- Padding: `0px 12px`
- Radius: `9999px`
- Font: 17px Sesame Sans weight 700
- Hover/Active/Focus: identical green/yellow flow
- Use: "FAMILY" navigation chip — Elmo zone

**Universal Action CTA — Confirmation Green**
- Background: Confirmation Green (`#00b140`)
- Text: Pure White (`#ffffff`)
- Padding: `9px 24px`
- Radius: `9999px`
- Font: 18px Source Sans Pro weight 700
- Hover/Active/Focus: identical green/yellow flow as character buttons
- Use: "DONATE", "SIGN UP", "GET INVOLVED" — universal action that doesn't belong to a character zone

**Neutral Pill (Action Card)**
- Background: Light Surface (`#f8f8f8`)
- Text: Caption Slate (`#3d3d3d`)
- Padding: `12px 18px`
- Radius: `9999px`
- Border: `0px solid #3d3d3d`
- Font: 16px Source Sans Pro weight 700
- Hover: background `#eeeeee`, text turns Hover Green, border `3px solid #333333`
- Use: Filter / sort chips, secondary actions on light surfaces

**Search Input Pill**
- Background: Pure White (`#ffffff`)
- Text: Body Slate (`#54585a`)
- Padding: `0px 16px 0px 48px` — left-padded for search icon
- Radius: `9999px`
- Border: `1px solid #d8d8d8`
- Font: 16px Source Sans Pro weight 400
- Focus: background turns Sesame Yellow (`#ffd400`), border `rgba(0, 177, 64, 0.46)`, text turns white
- Use: Site search, content filter

### Cards & Containers

**Article Card (oddity radius)**
- Background: Pure White (`#ffffff`)
- Border: `0px 0px 1px solid #eeeeee`
- Radius: `4px 4px 8px 8px` — top corners tighter than bottom — 50 confirmed instances
- Shadow: `rgba(0, 0, 0, 0.1) 0px 3px 6px 0px`
- Padding: `16–20px` internal
- Use: Article tiles, episode cards — the asymmetric radius is the brand's signature card shape

**Image Card (square radius)**
- Background: Pure White (`#ffffff`)
- Border: none
- Radius: `8px`
- Padding: 0px (image fills frame)
- Shadow: `rgba(0, 0, 0, 0.1) 0px 3px 6px 0px`
- Use: Standard featured-content tiles

**Character Avatar (sticker-cutout)**
- Background: character photo
- Border: `4px solid #ffffff` — the white sticker frame
- Radius: `100%` (circle) or `9999px` (pill)
- Shadow: `rgb(255, 255, 255) 0px 0px 0px 4px` — outer white ring sealing the cutout
- Inner image: 100% radius
- Use: Elmo / Cookie Monster / Big Bird character avatars, "Meet the Family" tiles

**Modal / Dialog**
- Background: Pure White (`#ffffff`)
- Border: none
- Radius: `50%` (rare circular modals) or `8px`
- Shadow: stacked drop with 6px blur
- Padding: `24–40px`

### Badges / Tags / Pills

**Category Pill**
- Background: Cookie Sky Blue (`#14bcf3`) or character-coded
- Text: Pure White (`#ffffff`)
- Padding: `4px 12px`
- Radius: `9999px`
- Font: 14px Sesame Sans weight 700, UPPERCASE, `0.22px` letter-spacing
- Use: Content category tags — "VIDEO", "GAME", "ACTIVITY"

**Inline Tag (subtle)**
- Background: Light Surface (`#f8f8f8`)
- Text: Body Slate (`#54585a`)
- Padding: `4px 10px`
- Radius: `9999px`
- Font: 12px Source Sans Pro weight 700, UPPERCASE
- Use: Filter chips, age-recommendation pills, "AGES 3-5"

### Inputs & Forms

**Search Input** (see Buttons section above for pill detail)

**Email Newsletter**
- Background: Pure White (`#ffffff`)
- Border: `1px solid #d8d8d8`
- Radius: `9999px` — fully pill
- Padding: `0px 24px`
- Font: 16px Source Sans Pro weight 400, color `#54585a`
- Focus: border thickens to Confirmation Green hairline
- Submit attached as flush pill: Confirmation Green fill, white "SUBSCRIBE" text in 16px Source Sans Pro 700

### Navigation

- Top nav: white background, Sesame Workshop logo (282x70 SVG) anchored top-left
- Primary nav: row of 5 character-coded pills — Cookie Sky Blue ("WATCH"), Big Bird Orange ("PLAY"), Abby Magenta ("LEARN"), Grover Purple ("EXPLORE"), Elmo Red ("FAMILY")
- Secondary utility: Source Sans Pro 14px weight 600 sentence-case links — "About", "Shop", "Donate"
- Search: white pill input with magnifier icon, right-aligned
- Hover: nav pills turn green; secondary links underline
- Mobile: hamburger reveals full-screen overlay with stacked character pills

### Decorative Elements

**Sticker-Cutout Frame**
- The signature treatment: 4px white border + 4px white outer shadow ring around character photography
- Reads as cut-from-magazine sticker
- Applied to character avatars, "Meet the Family" tiles, and homepage character heroes

**Pill Everywhere**
- 61 confirmed `9999px` radius instances across buttons, inputs, search, avatars, and floating chips
- The single most-distinctive structural decision in the system

**Asymmetric Card Radius**
- `4px 4px 8px 8px` on article cards — top tighter than bottom — 50 confirmed instances
- A subtle but consistent oddity that makes article tiles feel hand-cut

**Character Photography on White**
- Plush characters (Elmo, Big Bird, Cookie Monster, Grover, Abby) on white seamless backgrounds
- Character photography is the brand's true decoration — no abstract illustration, no icon library
- Each character's "zone" colour matches the character's plush colour

## Do's and Don'ts

### Do
- Use the five character-coded primary CTA colours (Sky Blue / Orange / Magenta / Purple / Red) for navigation pills — each colour belongs to its character zone
- Set primary CTA labels in Sesame Sans weight 700 — bold rounded grotesk reads as friendly authority
- Set hero display headlines in Sesame Sans weight 300 — light weight on rounded letterforms reads as warm and approachable
- Use Source Sans Pro at weights 400/600/700 for body, navigation, and secondary CTAs
- Apply `9999px` pill radius on all primary CTAs, search inputs, and avatars — fully rounded is the system's signature
- Use the `4px 4px 8px 8px` asymmetric radius on article cards — the brand's hand-cut tile shape
- Wrap character photography in a 4px white border + 4px white outer shadow ring for the sticker-cutout effect
- UPPERCASE category eyebrows in 14px Sesame Sans 700 with `0.22px` letter-spacing — kindergarten legibility
- Use Body Slate (`#54585a`) for body text — softer than black, warmer than grey
- Apply the universal green hover state (`#0095389` background, `3px solid #333` border) to every character button
- Show character photography on white seamless backgrounds — toy-catalogue convention
- Pair Confirmation Green (`#00b140`) action CTAs with character-coded zone CTAs as a "do" / "explore" hierarchy

### Don't
- Don't use sharp `0px` corners on primary buttons — pill (`9999px`) is the system's signature
- Don't desaturate the character colours — they need to be at full saturation to function as recognizable plush identifiers
- Don't use Sesame Sans at weight 700 for body — only for display heads and primary CTAs
- Don't use Source Sans Pro for hero headlines — Sesame Sans carries display
- Don't replace character photography with abstract illustrations or stock kid imagery — the Muppets ARE the brand
- Don't introduce gradient fills on character buttons — flat saturated colour is the brand's chromatic identity
- Don't use cool greys on body text — Body Slate (`#54585a`) is intentionally warm
- Don't skip the 4px white sticker frame on character avatars — the sticker effect is the brand's signature elevation
- Don't add atmospheric multi-layer shadows — Sesame Street's depth is sticker-and-tile, not architectural
- Don't change the asymmetric `4px 4px 8px 8px` card radius to a uniform 8px — the asymmetry is intentional
- Don't darken the white canvas to cream or off-white — the playroom needs crisp white
- Don't shrink character buttons below 17px Sesame Sans 700 — they must remain tappable for kid-sized fingers

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile Tiny | <320px | Single-column, character pills stack vertically, hero scales to 24–32px |
| Mobile | 320–600px | Single-column, hamburger nav, character pills wrap to 2 rows |
| Tablet | 600–800px | 2-column tile grid, character pills in single horizontal row |
| Desktop | 800–1200px | 3-column tile grid, full character pill nav, 48px hero display |
| Large Desktop | ≥1200px | 4-column tile grid, max content width 1280px |

### Touch Targets
- Primary character CTAs: 17px text + minimum 12px horizontal padding produces ~44–48px tap height — kid-finger comfortable
- Search pill: 48px minimum height for tap-comfortable entry
- Character avatars: minimum 80px diameter on mobile to remain identifiable
- Article cards: full-card tappable, no nested clickable regions

### Collapsing Strategy
- **Nav**: Horizontal character-pill row maintains at all sizes ≥800px; below tablet, collapses to hamburger with stacked character pills full-width
- **Hero**: Character photography full-bleed on mobile; sticker-cutout treatment maintained at all sizes
- **Article grid**: 4 → 3 → 2 → 1 columns as viewport narrows; asymmetric radius held at every breakpoint
- **Display type**: Sesame Sans 48px → 32px → 24px progressive scaling; weight 300 maintained
- **Section spacing**: 60px desktop → 40px tablet → 24px mobile

### Image Behavior
- Character photography preserves white seamless background at all breakpoints
- Sticker-cutout 4px white frame maintained at every size — never reduced to 2px
- Hero character photos crop to portrait on mobile, landscape on desktop
- Logo (282x70 SVG) scales but never simplifies — always full Sesame Workshop wordmark

---

## Agent Prompt Guide

### Quick Color Reference
- Primary CTAs (character-coded):
  - Cookie Sky Blue (Watch): `#14bcf3` (also default `#21cfff`)
  - Big Bird Orange (Play): `#f78600` (also default `#ff9800`)
  - Abby Magenta (Learn): `#f30fa2` (also default `#ff07a7`)
  - Grover Purple (Explore): `#901889` (also default `#9d1d96`)
  - Elmo Red (Family): `#e51a1a` (also default `#f91d1d`)
- Universal Action CTA: Confirmation Green (`#00b140`)
- Hover State: Hover Green (`#009523`) background, Sesame Yellow (`#ffd400`) on focus
- Page Background: Pure White (`#ffffff`)
- Body Text: Body Slate (`#54585a`)
- Heading Text: Caption Slate (`#3d3d3d`)
- Sticker Frame: `4px solid #ffffff` + `rgb(255, 255, 255) 0px 0px 0px 4px` outer ring
- Card Shadow: `rgba(0, 0, 0, 0.1) 0px 3px 6px 0px`

### Quick Type Reference
- Hero display: Sesame Sans 48px / weight 300 / line-height 1.10
- Card title: Sesame Sans 24px / weight 300 / line-height 1.33
- Eyebrow: Sesame Sans 14px / weight 700 / UPPERCASE / `0.22px` letter-spacing
- Body: Source Sans Pro 16px / weight 400 / line-height 1.63
- Button: Sesame Sans 17px / weight 700 / line-height 1.76
- Compact CTA: Source Sans Pro 12px / weight 700 / UPPERCASE

### Example Component Prompts
- "Create a Sesame Street-style character navigation row with 5 pill buttons. Each button: `9999px` radius, `0px 12px` padding, 17px Sesame Sans weight 700, white text. Colors in order: Cookie Sky Blue (`#21cfff`) 'WATCH', Big Bird Orange (`#ff9800`) 'PLAY', Abby Magenta (`#ff07a7`) 'LEARN', Grover Purple (`#9d1d96`) 'EXPLORE', Elmo Red (`#f91d1d`) 'FAMILY'. On hover, all buttons turn Confirmation Green (`#009523`) with `3px solid #333` border."
- "Build a character avatar tile: Elmo character photograph centered, framed with `4px solid #ffffff` border, `100%` border-radius. Apply `box-shadow: rgb(255, 255, 255) 0px 0px 0px 4px` outer ring for sticker-cutout effect. Below: character name in Sesame Sans 24px weight 300 line-height 1.33 in `#54585a`."
- "Design an article tile: white background, `4px 4px 8px 8px` border-radius (top corners tighter than bottom), `box-shadow: rgba(0, 0, 0, 0.1) 0px 3px 6px 0px`, 16px internal padding. Top: 16:9 image. Eyebrow tag in 14px Sesame Sans weight 700 UPPERCASE color `#14bcf3` with `0.22px` letter-spacing. Title in Sesame Sans 24px weight 300 line-height 1.33 color `#3d3d3d`. Body in Source Sans Pro 16px weight 400 color `#54585a`."
- "Create a search-input pill: white background, `1px solid #d8d8d8` border, `9999px` radius, padding `0px 16px 0px 48px` (left-padded for magnifier icon at 48px), 16px Source Sans Pro weight 400 color `#54585a`. On focus, background turns Sesame Yellow (`#ffd400`) and text inverts to white."
- "Build a 'DONATE' universal action CTA: Confirmation Green (`#00b140`) background, white text, `9999px` radius, padding `9px 24px`, 18px Source Sans Pro weight 700. Hover same as character buttons — green background with `3px solid #333` border."
- "Design a hero section: full-bleed character photo of Big Bird on white seamless. Overlay headline at 48px Sesame Sans weight 300 line-height 1.10 in `#3d3d3d`. Eyebrow above: 14px Sesame Sans weight 700 UPPERCASE `0.22px` tracking, color Cookie Sky Blue (`#14bcf3`). Below: Confirmation Green CTA pill 'PLAY NOW'."

### Iteration Guide
1. Default to the five character-coded CTA colours — each one belongs to its zone (Watch / Play / Learn / Explore / Family). No deviating to "brand-neutral" CTA colours.
2. Sesame Sans at weight 300 for display, weight 700 for primary CTAs; Source Sans Pro for body and secondary chrome.
3. Pill radius (`9999px`) is the workhorse — 61 confirmed uses across buttons, inputs, search, avatars. Never use sharp `0px` corners on primary chrome.
4. Article cards use the asymmetric `4px 4px 8px 8px` radius — top tighter, bottom softer. This is the brand's hand-cut tile signature.
5. Wrap character photography in `4px solid #ffffff` border + `rgb(255, 255, 255) 0px 0px 0px 4px` outer ring — the sticker-cutout effect.
6. UPPERCASE category eyebrows in 14px Sesame Sans 700 with `0.22px` letter-spacing for kindergarten legibility.
7. Body text in Body Slate (`#54585a`), heading text in Caption Slate (`#3d3d3d`) — warm greys, not cool.
8. Hover state on every character button turns green with `3px solid #333` border — universal across all five colours.
9. Card shadows are soft and light: `rgba(0, 0, 0, 0.1) 0px 3px 6px 0px`. No multi-layer atmospheric shadows.
10. The Muppets ARE the brand. Show character photography on white seamless backgrounds; let the chrome support the characters, never compete.
