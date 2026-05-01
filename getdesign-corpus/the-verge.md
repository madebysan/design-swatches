---
slug: the-verge
name: The Verge
url: https://www.theverge.com
domain: theverge.com
category: Media
styles: [Bold, Colorful, Editorial]
tagline: "Acid mint headlines, 90px Manuka over black, ultraviolet focus rings, rave-flyer story tiles."
fonts: [Manuka, PolySans]
primary_color: "#3cffd0"
---

# Design System Inspired by The Verge

> Acid mint headlines, 90px Manuka over black, ultraviolet focus rings, rave-flyer story tiles.

## 1. Visual Theme & Atmosphere

The Verge's homepage looks like a tech magazine that has been art-directed by a flyer designer. The page sits on near-black (`#1a1a1a`) and pure black surfaces with paper-white type, and the entire chromatic identity hinges on a single saturated accent — Verge Mint (`#3cffd0`), a CRT-screen acid green that surfaces on every CTA, every hover-link inset, every brand mark, like a phosphor scanline pulled across the page. That mint, paired with the heavyweight Manuka display face (a custom condensed sans-serif from PolySans designer Pangram Pangram) running at 90px / 5.63rem with a `0.80` line-height, is what makes a Verge page instantly recognizable across the room.

The signature typographic move is the **dual-grotesk stack**: Manuka does the shouting, PolySans (a humanist neo-grotesk) handles every transactional surface — body copy, navigation, buttons, captions — and a serif (FK Roman Standard, fallback Georgia) enters only for editorial pull-quotes and feature decks. The page rotates between three voices: Manuka roaring, PolySans walking, FK Roman whispering. The mint accent appears across all three.

The third defining trait is **editorial chaos contained by hard system grids**. Story tiles use sharp corners (`2px`–`3px` radii), story badges use full pill rounding (`24px`–`30px`), photograph crops never round at all, and section hovers fire an inset shadow underline (`box-shadow: 0 -1px 0 0 inset` in Verge Mint). The colour palette runs hot on accent surfaces — magenta, ultraviolet (`#5200ff`), cyan (`#1eaedb`), screaming pink — but the page itself stays disciplined: black canvas, white type, mint accent, and editorial photography doing the rest.

**Key Characteristics:**
- Verge Mint accent (`#3cffd0`) — CRT-phosphor green for CTAs, link insets, brand glyphs
- Near-black canvas (`#1a1a1a`) and pure black (`#000000`) surfaces — paper-white type sits on top
- Manuka display face — 90px UPPERCASE-allowed condensed sans, weight 900, `0.80` line-height
- PolySans body / UI face — humanist neo-grotesk at 12–24px for everything transactional
- FK Roman Standard serif — sparingly, for pull-quotes and editorial decks
- Pill `24px`–`30px` border-radius on primary CTAs — rave-flyer rounding
- Sharp `2px`–`3px` radii on story tiles and images — editorial framing
- Inset-shadow underlines (`box-shadow: 0 -1px 0 0 inset`) in Verge Mint for hover states
- Ultraviolet focus ring (`#5200ff`) — `1px solid` on keyboard focus, post-millennial publication accent
- Cyan hover (`#1eaedb`) — secondary blue accent on button hover transitions
- Hot Magenta (`#b840cc` / `#dd00ff`) and Lavender (`#8a69a9`) tile accents on showbiz / culture sections
- No traditional shadows — the system uses inset border-shadow as the elevation language

## 2. Color Palette & Roles

### Primary Brand
- **Verge Mint** (`#3cffd0`): The brand-defining acid mint. CRT-phosphor green used on every primary CTA fill, brand mark, hover-inset underline, and feature-section ribbon. So definitional that a Verge page in pure grayscale would be instantly unrecognizable.
- **Pure Black** (`#000000`): Primary type colour on Verge Mint surfaces, body ink on light editorial pages.
- **Near Black** (`#1a1a1a`) (also surfaces as `#313131`): Default page canvas, story-tile background, footer ink. Slightly softened from pure black for editorial readability.

### Brand Accent / Secondary
- **Cyan Hover** (`#1eaedb`): Secondary-button hover transition colour — the "loading-bar blue" that mint flips to.
- **Ultraviolet Focus** (`#5200ff` / `#2285f7`): Keyboard-focus outline. The post-millennial-publication accent that sits just inside accessibility compliance.
- **Hot Magenta** (`#b840cc`): Showbiz / pop-culture / rave-flyer feature tile accent.
- **Screen Pink** (`#dd00ff`): Sister magenta — used on review-section banners.
- **Royal Lavender** (`#8a69a9`): Tertiary section accent for culture content.
- **Sky Blue** (`#3a79bb`): Generic web blue for less-aggressive section markers.

### Text & Surface Greys
- **Headline White** (`#ffffff`): Display headlines, primary type on dark canvas, button text on cyan hover.
- **Body White** (`#e9e9e9`): Body text on near-black canvas — slightly softened from pure white for long-form readability.
- **Caption Gray** (`#949494`): Comments link, byline metadata, ancillary captions — the system's most-frequent gray (1302 occurrences).
- **Tile Gray** (`#2d2d2d`): Secondary-button background, alternative tile fill.
- **Surface Black** (`#000000`): The deepest tier — feature-tile background, primary CTA fill on light pages.
- **Hairline Mint** (`#3cffd0`): Used as a `0 -1px 0 0 inset` underline on hover.

### Functional / State
- **Verge Mint** (`#3cffd0`): Primary CTA fill, brand mark, link hover underline.
- **Cyan Hover** (`#1eaedb`): Secondary CTA hover state.
- **Ultraviolet** (`#5200ff`): Focus ring, error highlights.
- **Photo Background** (`#3cffd0` with overlay): Featured-article hero overlay tint.

### Gradient System
- The Verge is **gradient-free in chrome**. Story tiles are flat. The CTAs are solid mint. The page does no decorative blending — gradients live inside photographs themselves. The closest the system gets is a tonal range inside hero imagery (sky-to-pavement, screen-to-bezel) — never CSS gradients on UI surfaces.

## 3. Typography Rules

### Font Family
- **Display**: `Manuka` (custom from Pangram Pangram), with fallback stack `Impact, Helvetica`. The condensed-grotesque heavyweight that carries hero headlines and section openers.
- **UI / Body**: `PolySans` (humanist neo-grotesk), with fallback stack `Helvetica, Arial`. The transactional face for navigation, body copy, captions, and buttons.
- **Editorial Serif**: `FK Roman Standard`, with fallback `Georgia`. Used sparingly for pull-quotes, deck text, and feature article body where the editorial register flips warm.
- **OpenType Features**: Standard ligatures, lining numerals on prices and timestamps.

*Note: Both Manuka and PolySans are licensed from Pangram Pangram. For external implementations: **Anton** or **Bebas Neue** substitute for Manuka (condensed display); **Inter**, **Söhne**, or **Public Sans** substitute for PolySans (humanist neo-grotesk). FK Roman is replaceable with **Lora** or **Source Serif 4**.*

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Hero Display | Manuka | 90px (5.63rem) | 900 | 0.80 | normal | The brand's loudest moment — feature heros and section openers |
| Mid Display | PolySans | 34px (2.13rem) | 700 | 1.00 | normal | Sub-feature heds, mid-grid section heads |
| Section Title | PolySans | 32px (2.00rem) | 400 | 1.10 | 0.32px | UPPERCASE-allowed section labels |
| H1 | PolySans | 28px (1.75rem) | 700 | 1.00 | normal | Primary story heds inside grid |
| Sub-headline Link | PolySans | 26px (1.63rem) | 700 | 1.10 | normal | Inline mega-link callouts |
| Editorial Serif Deck | FK Roman Standard | 24px (1.50rem) | 400 | 1.20 | normal | Pull-quotes, deck text |
| Bold Card Hed | PolySans | 24px (1.50rem) | 700 | 1.10 | 0.24px | Card headlines |
| Light Card Hed | PolySans | 24px (1.50rem) | 300 | 1.10 | 0.24px | Sub-card headlines |
| Body Hed | PolySans | 24px (1.50rem) | 400 | 1.10 | 0.24px | Mid-card heds |
| Body | PolySans | 16px (1.00rem) | 400 | 1.50 | normal | Default reading copy |
| Body Bold | PolySans | 16px (1.00rem) | 700 | 1.50 | normal | Lead paragraphs, emphasized text |
| Button Pill (primary) | PolySans | 12px (0.75rem) | 600 | 1.00 | normal | The mint pill CTA — UPPERCASE-allowed |
| Button Outline (s) | PolySans | 11px (0.69rem) | 500 | 1.00 | normal | Compact outline CTAs (`duet--cta--s`) |
| Caption / Byline | PolySans | 14px (0.88rem) | 400 | 1.43 | normal | Bylines, timestamps, comment count |
| Eyebrow / Kicker | PolySans | 12px (0.75rem) | 700 | 1.00 | normal | UPPERCASE — story category above headline |

### Principles
- **Three faces, three jobs**: Manuka shouts, PolySans walks, FK Roman whispers. They never trade roles. This separation is what keeps the page from feeling like a typography tour.
- **Tight headlines, generous body**: Manuka runs at `0.80` line-height (touching ascenders), PolySans body opens to `1.50`. The contrast is the editorial fingerprint.
- **Bold is structural**: Manuka exists primarily at weight 900; PolySans rotates through 300 / 400 / 600 / 700 depending on role. The 600/700 pairing on UI gives the system its rave-flyer punch.
- **Letter-spacing is mostly neutral**: Display sizes use the typeface's native metrics. Only mid-display PolySans gets `+0.32px` to `+0.24px` for subtle structural separation.
- **Serif is the editorial pivot**: FK Roman appears only when the content shifts into long-read magazine register. Its rarity is its power.

## 4. Component Stylings

### Buttons

**Primary Mint Pill**
- Background: Verge Mint (`#3cffd0`)
- Text: Pure Black (`#000000`)
- Padding: `10px 24px`
- Border: `0px none`
- Border-radius: `24px` — full pill
- Box-shadow: `none`
- Font: 12px PolySans weight 600 UPPERCASE-allowed, sentence-case default
- Hover: background `#1eaedb` (cyan), text `#ffffff`, opacity `0.9`
- Focus: background `#1eaedb`, border `1px solid #5200ff` (ultraviolet), outline `2px solid #000000`, opacity `0.9`, text `#ffffff`
- Active: background `initial`, opacity `1`
- Use: Primary CTAs — "Subscribe", "Sign Up", "Read More"

**Tile Inset Pill (Secondary)**
- Background: Tile Gray (`#2d2d2d`)
- Text: Body White (`#e9e9e9`)
- Padding: `10px 24px`
- Border-radius: `24px`
- Border: `0px none`
- Hover: background `#1eaedb` (cyan), text `#ffffff`, opacity `0.9`
- Focus: background `#1eaedb`, border `1px solid #5200ff`, outline `2px solid #000000`
- Use: Secondary CTAs in dark zones — "Watch", "Follow"

**Outline Mint (Compact)**
- Background: `transparent`
- Text: Verge Mint (`#3cffd0`)
- Padding: `0 20px`
- Border: `1px solid #3cffd0`
- Border-radius: `1px` — almost-sharp, the "small CTA" variant (`duet--cta--s`)
- Hover: background `#ffffff`, text `#2285f7`, border `1px solid #ffffff`, opacity `0.7`
- Focus: outline `1px solid #5200ff`, transform `none`, background `#1eaedb`, border `1px solid #000000`, color `#ffffff`
- Use: Small inline CTAs, sidebar callouts, in-card actions

**Inline Hover Link**
- Default: text inherits, no underline
- Hover: `box-shadow: 0 -1px 0 0 inset` in Verge Mint (`#3cffd0`) — phosphor scanline appears below text
- Use: Every inline editorial link inside body copy

### Cards & Containers

**Story Tile**
- Background: Pure Black (`#000000`) or Tile Gray (`#2d2d2d`) on alternate sections
- Border: `none`
- Border-radius: `2px`–`3px` for the wrapper, `0px` for full-bleed photographs inside
- Box-shadow: `none` at rest; on hover an inset mint underline appears under the headline
- Internal padding: 16–24px
- Hover: headline underline appears as `box-shadow: 0 -1px 0 0 inset` in Verge Mint

**Feature Tile (Mint Background)**
- Background: Verge Mint (`#3cffd0`)
- Text: Pure Black (`#000000`)
- Border-radius: `3px`
- Padding: 24–32px
- Use: Featured sponsored or magazine-feature blocks

**Magenta Tile (Showbiz)**
- Background: Hot Magenta (`#b840cc`) or Screen Pink (`#dd00ff`)
- Text: Pure White (`#ffffff`)
- Border-radius: `3px`
- Use: Pop-culture and review section heroes

### Badges / Tags / Pills

**Section Pill**
- Background: Verge Mint (`#3cffd0`) for tech, Magenta (`#b840cc`) for showbiz, Lavender (`#8a69a9`) for culture
- Text: Pure Black (`#000000`) on mint, Pure White on magenta/lavender
- Padding: `4px 12px`
- Border-radius: `30px` — full pill
- Font: 12px PolySans weight 700 UPPERCASE
- Use: Section markers above story heds

**"NEW" / "EXCLUSIVE" Tag**
- Background: Verge Mint (`#3cffd0`)
- Text: Pure Black (`#000000`)
- Padding: `4px 8px`
- Border-radius: `2px`
- Font: 11px PolySans weight 700 UPPERCASE

### Inputs & Forms
- Background: Pure Black (`#000000`) on dark theme, white on inverse
- Border: `1px solid #2d2d2d` default, `1px solid #3cffd0` on focus (mint underline)
- Border-radius: `2px`
- Font: 16px PolySans weight 400
- Text colour: Body White (`#e9e9e9`)
- Padding: `12px 16px`
- Focus: outline `1px solid #5200ff` (ultraviolet ring), border becomes mint
- Placeholder: Caption Gray (`#949494`)

### Navigation

**Top Nav Bar**
- Background: Pure Black (`#000000`)
- Height: 56–64px
- Logo: Verge mint glyph + wordmark, ~120–140px wide, left-aligned
- Categories: "Tech · Reviews · Science · Entertainment · AI · Cars · Transport · Policy · Newsletters" — 14px PolySans weight 600, white type
- Right cluster: search icon, account icon, hamburger
- Hover: category text shifts to mint, optional inset underline appears
- Border-bottom: `1px solid #2d2d2d`

### Inline Editorial Links
- Color: inherits from body (white on dark, black on light)
- On hover: `box-shadow: 0 -1px 0 0 inset` in Verge Mint (`#3cffd0`) — phosphor scanline under text
- Use: Every inline editorial link inside body copy

## 5. Layout Principles

### Spacing System
- Base unit: 4px (with 8px and 16px as the primary rhythm)
- Scale: 4px, 8px, 12px, 16px, 20px, 24px, 32px, 40px, 48px, 64px, 80px, 96px
- Notable: The Verge's grid runs on tight 8–24px rhythm. Story tiles stack with `8–16px` gutters and section bands collapse to `0–4px` between blocks. The page is dense but disciplined.

### Grid & Container
- Max content width: 1280–1440px on desktop story grid
- Hero: full-width photograph + Manuka headline overlay inside the 1280px container
- Story grid: 3-up or 4-up desktop, 2-up tablet, 1-up mobile — 8–16px gutters
- Footer: dense link grid in pure black with mint glyph, paper-white type

### Whitespace Philosophy
- **Editorial chaos contained by grids**: Story tiles butt against one another; the page maintains structural calm via rigorous column rhythm rather than generous whitespace.
- **Mint as architecture**: The mint accent does the work that whitespace does elsewhere — it pulls the eye to CTAs and pulls section headers out of the dark canvas.
- **Black canvas is the breath**: Where most editorial sites use white whitespace as breathing room, The Verge uses black canvas — paper-white type and mint accents pop against it.

### Border Radius Scale
- Sharp (`0px`): Default for full-bleed photography inside tiles
- Hairline (`1px`): Compact outline CTAs (`duet--cta--s`)
- Subtle (`2px`–`3px`): Story tiles, image wrappers, badges
- Pill (`20px`–`30px`): Primary CTAs, section pills, tag chips
- Circle (`50%`): Avatars, social icons, in-pager indicator dots
- No mid-range (`8–16px`): The Verge avoids the modern-app look — sharp or pill

## 6. Depth & Elevation

| Level | Box Shadow | Use Case |
|-------|-----------|---------|
| Flat (Level 0) | `none` | Default state for story tiles, body content, footer |
| Inset Mint (Level 1) | `0 -1px 0 0 inset rgb(60, 255, 208)` | Hover underline on inline links and headlines |
| Inset White (Level 2) | `0 -1px 0 0 inset rgb(255, 255, 255)` | Inverse hover underline on light-section content |
| Inset Body (Level 3) | `0 -1px 0 0 inset rgb(233, 233, 233)` | Subtle hover underline in muted contexts |
| Lift Drop (Level 4) | `rgba(0, 0, 0, 0.4) 0px 4px 10px 0px` | Featured-tile elevation on hover (rare, low-confidence) |
| Ultraviolet Focus (Level 5) | `outline: 1px solid #5200ff` | Keyboard-focus on buttons and links |

**Shadow Philosophy**: The Verge has effectively replaced traditional drop-shadows with **inset border-shadows** used as underline states. Hovering an inline link doesn't lift it off the page — it underlines it with a `0 -1px 0 0 inset` mint scanline. Hovering a primary CTA flips it to cyan. The system uses no decorative blur. Where competitor publications lean on glass-morphism, The Verge leans on phosphor inversions and box-shadow underlines. The result feels like a CRT terminal interface refreshed for 2026, not a SaaS dashboard.

### Decorative Depth
- The mint inset underline is the only "elevation" cue most users will encounter
- Ultraviolet focus rings (`#5200ff`) handle keyboard accessibility without lifting elements
- Hot magenta and pink tiles create visual depth via saturation rather than shadow

## 7. Do's and Don'ts

### Do
- Use Verge Mint (`#3cffd0`) on every primary CTA, brand mark, and inline-link hover underline — the phosphor signature
- Run Manuka (or Anton / Bebas substitute) UPPERCASE-allowed at 70–90px for hero displays at `0.80` line-height
- Use PolySans (or Inter / Söhne) at weights 300 / 400 / 600 / 700 for everything transactional
- Default to `24px`–`30px` pill border-radius on primary CTAs — rave-flyer rounding
- Keep story-tile radius sharp at `2px`–`3px` — editorial framing
- Use `box-shadow: 0 -1px 0 0 inset` in Verge Mint for inline-link hover underlines
- Run body copy at 16px PolySans weight 400 with `1.50` line-height
- Use Ultraviolet (`#5200ff`) for keyboard focus rings — post-millennial-publication accent
- Pair Hot Magenta (`#b840cc`) with white type on showbiz / culture tiles
- Reserve FK Roman Standard serif for pull-quotes and editorial decks only — never UI

### Don't
- Don't use traditional drop-shadows on cards or buttons — depth is via mint insets and saturated tile colour
- Don't introduce a third display face — Manuka shouts, PolySans walks, FK Roman whispers
- Don't soften the page background to gray — `#1a1a1a` near-black or `#000000` pure black are the only canvas options
- Don't apply pill `24–30px` radius to story tiles — pills are for CTAs and section badges only
- Don't use Verge Mint as a body text colour — it's the accent, not the type
- Don't lowercase Manuka display heds — UPPERCASE-allowed at 90px is the contract (sentence case is acceptable for shorter heds)
- Don't introduce mid-range radii (`8–16px`) — sharp `2–3px` or pill `20–30px`, nothing in between
- Don't use ultraviolet (`#5200ff`) for non-focus moments — it's the keyboard-accessibility ring, not decoration
- Don't crowd dark canvas with traditional gradients — saturation does the lifting
- Don't add box-shadows to the mint pill CTA — it's flat-on-dark, no halo, no glow

## 8. Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile Small | <375px | Single-column, hero Manuka drops to 56px, hamburger nav |
| Mobile | 375–767px | Single-column, Manuka 56–72px, 1-up tile grid |
| Tablet | 768–1023px | 2-up tile grid, partial inline subnav |
| Desktop | 1024–1279px | 3-up tile grid, full inline nav |
| Large | 1280–1439px | Maximum 1280px container, 3–4-up grid |
| XL | ≥1440px | 1440px container, 4-up grid with wider gutters |

### Touch Targets
- Primary CTAs: min 44px tap height, 24px horizontal padding on mobile
- Story tiles: entire tile is tappable, not just the headline
- Mint pill CTAs maintain `24px` radius and `10px 24px` padding at all breakpoints

### Collapsing Strategy
- **Top nav**: Horizontal categories collapse to hamburger drawer under 1024px
- **Hero Manuka**: 90px → 72px → 56px → 48px progressive scaling, weight stays at 900 throughout
- **Tile grid**: 4-up → 3-up → 2-up → 1-up with maintained aspect ratios
- **Footer**: dense link grid collapses to accordion sections

### Image Behavior
- Story photographs maintain a 16:9 or 4:3 crop across breakpoints
- Hero photographs use art-directed crops at mobile (often a tighter portrait)
- The mint glyph scales but never simplifies — always full Verge mark

## 9. Agent Prompt Guide

### Quick Reference
- Brand Accent: Verge Mint (`#3cffd0`)
- Page Background: Near-Black (`#1a1a1a`) or Pure Black (`#000000`)
- Primary Type: Pure White (`#ffffff`)
- Body Type: Body White (`#e9e9e9`)
- Display Font: Manuka 70–90px UPPERCASE, weight 900, `0.80` line-height
- Body Font: PolySans 16px / 1.50 line-height
- Primary CTA: Mint bg, black text, `24px` pill, PolySans 12px weight 600
- Hover: Cyan (`#1eaedb`) with inset mint underline
- Focus Ring: Ultraviolet (`#5200ff`) `1px solid` outline
- Magenta Tile: `#b840cc` with white type

### Example Component Prompts
- "Create a Verge-style hero on `#1a1a1a` with a 90px Manuka headline at `0.80` line-height in pure white. Below the headline, a 16px PolySans weight 400 body deck. Pair with a Verge Mint (`#3cffd0`) primary CTA — `10px 24px` padding, `24px` border-radius, 12px PolySans weight 600 black label. On hover the CTA flips to cyan (`#1eaedb`) with white text."
- "Build a 3-up story-tile grid on `#000000`. Each tile is a 16:9 photograph with `0px` radius inside a `3px` radius wrapper. Below the image: 24px PolySans weight 700 headline at line-height `1.10` in `#ffffff`, 14px PolySans weight 400 byline in `#949494`. On hover the headline gets a `box-shadow: 0 -1px 0 0 inset` in Verge Mint (`#3cffd0`)."
- "Design a section pill — Verge Mint (`#3cffd0`) background, black text, 12px PolySans weight 700 UPPERCASE 'TECH', `4px 12px` padding, `30px` full-pill radius. Pair with a magenta variant `#b840cc` background and white text for showbiz, lavender `#8a69a9` for culture."
- "Create a featured magazine block — Verge Mint (`#3cffd0`) background, black 90px Manuka weight 900 headline at `0.80` line-height, 18px FK Roman Standard serif weight 400 deck below the headline. Add a black pill CTA on the mint surface — black bg, white text, `24px` radius, 12px PolySans weight 600."
- "Design an inline editorial link inside body copy — text inherits the body white (`#e9e9e9`), no underline at rest. On hover, apply `box-shadow: 0 -1px 0 0 inset rgb(60, 255, 208)` so a phosphor mint scanline appears below the text. On focus, add `outline: 1px solid #5200ff` ultraviolet ring."

### Iteration Guide
1. Default to near-black (`#1a1a1a`) or pure black (`#000000`) page canvas — never soften to gray.
2. Verge Mint (`#3cffd0`) is the brand accent contract — primary CTAs, brand glyph, and inline-link hover underlines only.
3. Three faces, three jobs: Manuka shouts (90px / weight 900), PolySans walks (12–24px UI), FK Roman whispers (pull-quotes).
4. Push display line-height tight (`0.80` on Manuka heros, `1.00–1.10` on PolySans heds).
5. Border-radius is binary: sharp `2–3px` for tiles and images, pill `24–30px` for CTAs and section badges.
6. Use `box-shadow: 0 -1px 0 0 inset` in mint for inline link hover — the system has no traditional shadows.
7. Ultraviolet (`#5200ff`) is the focus ring — `1px solid` outline on keyboard-focused buttons and links.
8. Hot magenta (`#b840cc`) and lavender (`#8a69a9`) are the showbiz / culture tile accents — never on UI chrome.
9. Body copy at 16px PolySans weight 400 with `1.50` line-height — paper-white on near-black.
10. Reserve FK Roman Standard for editorial register pivots only — pull-quotes, decks, magazine-feature body. Never UI.
