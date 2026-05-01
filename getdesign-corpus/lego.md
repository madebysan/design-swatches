# Design System Inspired by Lego

## 1. Visual Theme & Atmosphere

Lego's website is the digital extension of the most rigorously codified play system in the world: a literal grid of plastic studs translated into a literal grid of pixels. The lego.com surface opens with the unmistakable red-on-white LEGO logotype anchored to the top, immediately followed by saturated primary-color panels — Lego Red (`#E3000B`), Lego Yellow (`#FFCF00`), and Lego Blue (`#006DB7`) — used as full-bleed billboards for product zones, age groups, and themes. Where most e-commerce sites whisper neutrality, Lego shouts in primary colors, then disciplines the shouting with a corporate-clean grotesk and a strict 8px brick-derived grid. The result reads as child-meets-corporate: maximum visual energy on the surface, military-grade brand consistency underneath.

The defining tension is between **chromatic exuberance and typographic restraint**. Headlines are set in `Cera Pro` (Lego's official corporate typeface since 2018, replacing the earlier `LEGO Sans` lineage) at heavy weights — usually 700 or 900 — in either pure white on color blocks or pure black on white. There is no light-weight display type, no editorial italics, no decorative flourish. The typography behaves like a sticker applied to a brick: confident, opaque, instantly legible from across a toy-aisle distance. Letterforms run at near-normal tracking with line-heights tightened to 1.05–1.15 on display sizes, so titles read as solid blocks of voice rather than airy magazine spreads.

What separates Lego from every other primary-color brand (Crayola, Fisher-Price, McDonald's) is the **brick-grid discipline** that governs every layout. Cards snap to clean rectangles with consistent 8px or 16px corner radii — never sharp-zero, because real Lego bricks have softened edges, and never fully-pill, because pills aren't bricks. Spacing increments stack predictably (`8, 16, 24, 32, 48, 64, 96`) like studs. Imagery sits inside the card frame the way a minifigure sits inside a baseplate — centered, framed, never bleeding chaotically. The color blocks themselves act as oversized bricks tiled across the page, each one a billboard for a single product family or play zone.

**Key Characteristics:**
- Three-color primary palette as billboard panels (`#E3000B` red, `#FFCF00` yellow, `#006DB7` blue) used full-bleed
- Cera Pro at weight 700–900 for all display and heading text — no lightweight display
- 8px brick-grid spacing system, scaled in stud-multiples (`8, 16, 24, 32, 48, 64, 96`)
- Soft brick-edge corner radii (`8px`, `12px`, `16px`) — never zero, never fully pill
- Iconic LEGO logotype lockup (red square, white wordmark, yellow rule) inviolable
- Pure white panels alternate with primary color blocks — high-saturation contrast as rhythm
- Photographic product hero shots on white seamless — toy-catalog convention, no environmental staging
- Generous whitespace inside saturated color blocks — color does the loud work, layout stays calm

## 2. Color Palette & Roles

### Primary (the Lego Trinity)
- **Lego Red** (`#E3000B`): The signature. Used for the logo background, primary CTAs, sale tags, age 4+ category panels, and any "this is the Lego brand" moment. Pantone 032 C is the print equivalent.
- **Lego Yellow** (`#FFCF00`): Play-zone backgrounds, kids' content surfaces, secondary attention-grabbing CTAs, the rule beneath the wordmark in the corporate logo. Pantone Yellow C.
- **Lego Blue** (`#006DB7`): Premium/adult lines (Lego Icons, Architecture, Technic landing zones), informational panels, link color on white surfaces. Pantone 293 C.

### Brand Black & White
- **Lego Black** (`#000000`): Logo wordmark drop, primary body text, button text on yellow. Pure black — no softening.
- **Pure White** (`#FFFFFF`): Page background default, button text on red and blue, logo wordmark counters. The negative space the bricks sit on.

### Secondary Accents (used sparingly, mostly in product photography and theme-specific zones)
- **Lego Bright Green** (`#00AF4D`): Lego City landscapes, plant-themed sets, "new" badges. Pantone 354 C.
- **Lego Orange** (`#F47B20`): Lego Friends accents, autumn product launches, secondary CTAs in city zones.
- **Lego Lime** (`#A8E000`): Used in Lego Star Wars, Ninjago, and other action-IP zones for energetic backgrounds.
- **Lego Magenta** (`#E6007E`): Lego Friends, Lego Disney, Lego Dots — the "girls' aisle" historical anchor that has since broadened.
- **Lego Purple** (`#7D3F98`): Magic and fantasy IP zones (Harry Potter, Disney castle sets).

### Neutrals & Text
- **Body Text** (`#000000`): All paragraph text on white surfaces — pure black for maximum legibility at small sizes.
- **Muted Gray** (`#5A5A5A`): Secondary copy, captions, age-recommendation labels, breadcrumb separators.
- **Light Gray** (`#E5E5E5`): Card borders on white, divider lines, disabled-state backgrounds.
- **Surface Gray** (`#F7F7F7`): Alternate panel background for category sections that aren't using a primary color block.

### Status Colors
- **Sale Red** (`#E3000B`): Same as Lego Red — sale prices, "save" badges, urgency moments. Brand red and discount red are intentionally identical.
- **Success Green** (`#00AF4D`): "Added to bag" confirmations, in-stock indicators.
- **Warning Yellow** (`#FFCF00`): Low-stock alerts, age-restriction notices.

### Gradient System
- Lego is **gradient-free in core brand applications**. Color blocks are flat, primary, and uncompromised — a gradient on a Lego red panel would look like a printing mistake. The only gradients appear in product photography (studio lighting on plastic) and occasional special-edition theme launches, never in brand chrome.

## 3. Typography Rules

### Font Family
- **Primary**: `Cera Pro`, with fallback: `"Helvetica Neue"`, `Helvetica`, `Arial`, `sans-serif`
- **Headline / Display**: Same `Cera Pro` at weights 700–900 — geometric grotesk, near-rounded terminals, optimized for headline confidence
- **Body**: `Cera Pro` at weights 400–500 for paragraph copy
- **OpenType Features**: Tabular figures (`tnum`) enabled for prices and product numbers; standard ligatures only

*Note: Cera Pro is a commercial typeface from TypeMates. For external implementations, `Avenir Next`, `Proxima Nova`, or `Poppins` serve as close substitutes; `Inter` at weight 700+ works as a free web alternative. Lego's older marketing materials used `LEGO Sans` (a custom rounded grotesk) — Cera Pro is the modern corporate replacement adopted ~2018.*

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Hero Display | Cera Pro | 72px (4.50rem) | 900 | 1.05 | -0.5px | Homepage billboard headlines on color blocks |
| Display Large | Cera Pro | 56px (3.50rem) | 800 | 1.08 | -0.4px | Theme landing page heroes |
| Display | Cera Pro | 40px (2.50rem) | 700 | 1.10 | -0.3px | Section titles, product family heads |
| Section Heading | Cera Pro | 32px (2.00rem) | 700 | 1.15 | -0.2px | Mid-page section heads, modal titles |
| Sub-heading Large | Cera Pro | 24px (1.50rem) | 700 | 1.20 | -0.1px | Card titles, feature blocks |
| Sub-heading | Cera Pro | 20px (1.25rem) | 700 | 1.25 | normal | Smaller card heads, product titles |
| Body Large | Cera Pro | 18px (1.13rem) | 500 | 1.50 | normal | Intro paragraphs, emphasized body |
| Body | Cera Pro | 16px (1.00rem) | 400 | 1.50 | normal | Standard reading text |
| Body Small | Cera Pro | 14px (0.88rem) | 400 | 1.45 | normal | Secondary copy, descriptions |
| Nav Link | Cera Pro | 14px (0.88rem) | 700 | 1.00 | 0.02em | Top navigation, breadcrumbs |
| Button UI | Cera Pro | 16px (1.00rem) | 700 | 1.00 | 0.02em | Primary CTAs, often uppercase |
| Caption | Cera Pro | 12px (0.75rem) | 400 | 1.40 | 0.01em | Age labels, legal text, fine print |
| Price Display | Cera Pro | 24px (1.50rem) | 800 | 1.00 | tabular | Product prices, must use `tnum` |

### Principles
- **Heavy weights as voice**: Display type lives at weight 700–900. Lego does not whisper. Where competitors use light grotesks for sophistication, Lego stays bold because the audience starts at age 4 and reading distance is a meter, not a screen-foot.
- **Tight display line-height**: Headlines run at 1.05–1.15. Tight blocks of type read as graphic billboards rather than editorial paragraphs.
- **Slight negative tracking on display**: `-0.2px` to `-0.5px` on sizes 32px+. Below 24px tracking returns to normal for legibility.
- **Uppercase reserved for CTAs and category labels**: Primary buttons ("SHOP NOW", "EXPLORE") use uppercase with `0.02em` tracking. Body and headlines stay mixed case for warmth.
- **No italic anywhere in chrome**: Italics never appear in nav, buttons, or headlines. Reserved exclusively for editorial body copy emphasis (rare).
- **Tabular figures for prices and product numbers**: Every price and 5-digit product code (e.g., 75192) uses `tnum` so columns align across listings.

## 4. Component Stylings

### Buttons

**Primary Red CTA**
- Background: Lego Red (`#E3000B`)
- Text: Pure White (`#FFFFFF`)
- Padding: 14px 28px standard, 18px 36px large
- Radius: `8px` (soft brick-edge)
- Border: none
- Shadow: `0 2px 0 0 rgba(0,0,0,0.15)` — subtle hard offset, like a brick sitting on a baseplate
- Font: 16px Cera Pro weight 700, uppercase, letter-spacing `0.02em`
- Hover: background shifts to `#C70009` (10% darker), shadow lifts to `0 4px 0 0 rgba(0,0,0,0.2)`
- Active: shadow collapses to `0 0 0 0`, button drops 2px (the "press" feel)
- Use: Primary CTA — "SHOP NOW", "ADD TO BAG", "BUY NOW"

**Yellow Action**
- Background: Lego Yellow (`#FFCF00`)
- Text: Lego Black (`#000000`)
- Padding: 14px 28px
- Radius: `8px`
- Shadow: `0 2px 0 0 rgba(0,0,0,0.15)`
- Font: 16px Cera Pro weight 700, uppercase
- Hover: background shifts to `#E6BB00`
- Use: Secondary action on red/blue panels, "PLAY", kids-zone CTAs ("START PLAYING")

**Blue Outline / Link Action**
- Background: transparent
- Text: Lego Blue (`#006DB7`)
- Padding: 14px 28px
- Radius: `8px`
- Border: `2px solid #006DB7`
- Font: 16px Cera Pro weight 700
- Hover: background fills to `#006DB7`, text inverts to `#FFFFFF`
- Use: Secondary informational actions, "Learn more", filter toggles

**White-on-Color Inverse**
- Background: Pure White (`#FFFFFF`)
- Text: Lego Black (`#000000`)
- Padding: 14px 28px
- Radius: `8px`
- Shadow: `0 2px 0 0 rgba(0,0,0,0.15)`
- Use: CTAs sitting on red, blue, or yellow panels where the brand color is already the background

**Icon Button (circular)**
- Background: transparent or `#FFFFFF`
- Size: 40px × 40px
- Radius: `9999px` (only place fully-circular appears)
- Border: none default, `2px solid #000` on focus
- Use: Cart, account, search, wishlist icons in top nav

### Cards & Containers

**Product Card**
- Background: Pure White (`#FFFFFF`)
- Border: `1px solid #E5E5E5`
- Radius: `8px`
- Shadow: `0 2px 8px rgba(0,0,0,0.08)` on hover only — flat at rest
- Internal padding: 16px around the product image, 16px around the metadata block
- Image: square aspect ratio, white seamless background, product centered
- Typography: 16px weight 700 title, 14px weight 400 subtitle, 18px weight 800 price

**Theme Billboard (Color Block)**
- Background: one of the primary trinity (`#E3000B`, `#FFCF00`, `#006DB7`)
- Border: none
- Radius: `12px` for desktop tiles, `0px` (full-bleed) for hero sections
- Internal padding: 32px–64px depending on card size
- Typography: 32–56px weight 800–900 in white (on red/blue) or black (on yellow)

**Modal / Country Gate**
- Background: Pure White (`#FFFFFF`) over a darkened scrim (`rgba(0,0,0,0.6)`)
- Radius: `12px`
- Inside: split into two color blocks (blue + yellow seen on lego.com gate) with bold panel headlines
- Shadow: `0 12px 48px rgba(0,0,0,0.25)` for elevated modal feel

### Badges / Tags / Pills

**New / Sale Badge**
- Background: Lego Red (`#E3000B`)
- Text: Pure White (`#FFFFFF`)
- Padding: 4px 10px
- Radius: `4px` (tight brick-edge)
- Font: 12px Cera Pro weight 800, uppercase, letter-spacing `0.04em`
- Use: "NEW", "SALE", "EXCLUSIVE" markers on product cards

**Age Recommendation Pill**
- Background: Pure White (`#FFFFFF`)
- Text: Lego Black (`#000000`)
- Border: `1px solid #000`
- Padding: 4px 12px
- Radius: `9999px`
- Font: 12px Cera Pro weight 700
- Use: "Ages 4+", "9+", "18+" — the iconic Lego age marker

### Inputs & Forms
- Background: Pure White (`#FFFFFF`)
- Border: `2px solid #5A5A5A` default, `2px solid #006DB7` on focus
- Radius: `8px`
- Font: 16px Cera Pro weight 400
- Text color: Lego Black (`#000000`)
- Placeholder: `#5A5A5A`
- Focus: blue border + `0 0 0 3px rgba(0,109,183,0.2)` halo ring
- Padding: 12px 16px
- Error state: border becomes `#E3000B`, helper text below in same red

### Navigation
- Top nav: pure white background, full-width, sticky on scroll
- Logo lockup: red square (`#E3000B`) with white "LEGO" wordmark + yellow rule beneath, anchored top-left, never resized below 40px
- Links: Cera Pro 14px weight 700, `#000000`, uppercase
- Hover: link gains underline `2px solid #E3000B` with 4px offset
- Mega-menu: drops from top nav as full-width white panel with category color-blocks inside (each theme zone gets its IP color)

### Decorative Elements

**Brick-Press Shadow**
- `0 2px 0 0 rgba(0,0,0,0.15)` resting → `0 4px 0 0 rgba(0,0,0,0.2)` hover → `0 0 0 0` pressed
- The signature interactive metaphor: every primary CTA behaves like a Lego brick being pressed onto a baseplate

**Color-Block Tiling**
- Homepage and category pages tile theme zones as flat primary-color rectangles
- Each tile contains a hero product photo + theme logo + CTA — minimum 320px tall, 480px on desktop
- Tiles never overlap; gutters are 8–16px (one or two studs)

## 5. Layout Principles

### Spacing System
- Base unit: 8px (one Lego stud)
- Scale: `4px, 8px, 16px, 24px, 32px, 48px, 64px, 96px, 128px`
- Notable: 4px exists only for tight chrome (badge padding, icon-to-label gaps). 24px is the workhorse for component-internal spacing. Section breaks sit at 64–128px on desktop. Every value is a stud-multiple — there are no 13px or 22px values anywhere.

### Grid & Container
- Max content width: 1440px for centered content; full-bleed sections extend edge-to-edge
- Hero: full-bleed color block or full-bleed product photography
- Theme billboard grid: typically 3 or 4 columns on desktop, 2 on tablet, 1 on mobile
- Product grid: 4 columns desktop, 3 tablet, 2 mobile (never 1 — toy aisles are about adjacency)
- Gutters: 16px between cards, 24–48px between sections

### Whitespace Philosophy
- **Saturated economy**: Color blocks are loud, but the layout inside them is calm. A red billboard with one headline + one product photo + one CTA reads as confident. Crowding it would break the brick-aisle feel.
- **Stud-aligned breathing room**: Every margin, gap, and padding lands on the 8px grid. The eye registers this as order even before consciously noticing.
- **Color rhythm as pacing**: Pages alternate white panels with red/yellow/blue billboards, creating a chapter-like rhythm. No two adjacent billboards share a color.

### Border Radius Scale
- Tight (`4px`): Badges, age pills, small chips, sale tags
- Soft brick (`8px`): Buttons, inputs, product cards, default UI containers — the workhorse
- Rounded brick (`12px`): Hero billboards on desktop, modals, large feature tiles
- Generous (`16px–24px`): Marketing hero panels, special-edition campaign cards
- Pill (`9999px`): Age-recommendation pills, circular icon buttons only
- **No sharp-zero (`0px`)**: Lego corners are never razor-cut except in full-bleed edges where the radius would be invisible anyway. Real bricks have softened edges; the system honors that.

## 6. Depth & Elevation

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | No shadow | Page canvas, inline content, color billboards |
| Brick Rest (Level 1) | `0 2px 0 0 rgba(0,0,0,0.15)` | Default state for primary CTAs and elevated cards |
| Brick Hover (Level 2) | `0 4px 0 0 rgba(0,0,0,0.2)` | Hover state — the brick lifts slightly |
| Card Hover Soft (Level 3) | `0 2px 8px rgba(0,0,0,0.08)` | Product cards and tiles on hover — atmospheric, not graphic |
| Modal Elevation (Level 4) | `0 12px 48px rgba(0,0,0,0.25)` | Country gates, age confirmations, full-screen modals |
| Focus Ring | `0 0 0 3px rgba(0,109,183,0.2)` | Keyboard focus on inputs and interactive elements |

**Shadow Philosophy**: Lego mixes two shadow languages on purpose. Primary CTAs use **hard offset shadows** (`0 2px 0 0`) that mimic a real brick sitting on a baseplate — the shadow has no blur, it's a flat color rectangle offset downward. This is the brand's tactile metaphor. Cards and modals, by contrast, use **soft atmospheric shadows** that follow standard material-design conventions, because they represent informational surfaces rather than physical bricks. The split keeps the "Lego-ness" focused on the pieces a child would press.

### Decorative Depth
- Buttons depress on click — `transform: translateY(2px)` + shadow collapse to zero — completing the brick-press metaphor
- Product photography brings its own depth via studio lighting on plastic; the surrounding chrome stays graphically flat
- Color billboards never carry shadow — they're flat planes, like baseplates

## 7. Do's and Don'ts

### Do
- Use the Lego trinity (`#E3000B` red, `#FFCF00` yellow, `#006DB7` blue) as full-bleed billboards
- Set all display type in Cera Pro at weight 700–900 — confidence comes from weight, not size alone
- Honor the 8px stud-grid for every margin, gap, and padding value
- Apply `8px` radius as the default; `12px` for hero billboards; `9999px` only for age pills and circular icons
- Use the brick-press shadow (`0 2px 0 0 rgba(0,0,0,0.15)`) on primary CTAs to convey tactility
- Keep the LEGO logotype lockup intact — red square, white wordmark, yellow rule, never recolored
- Use uppercase for primary CTAs with `0.02em` letter-spacing — never for headlines or body
- Alternate white panels with primary-color billboards for chapter-like page rhythm
- Use `tnum` tabular figures for prices and product numbers so columns align
- Show product photography on white seamless backgrounds — toy-catalog convention

### Don't
- Don't use light-weight type (300 or below) on display sizes — Lego is never delicate
- Don't introduce sharp `0px` corners on cards or buttons — bricks have softened edges
- Don't gradient the brand colors — Lego Red is one flat color, always
- Don't crowd a saturated color block with multiple competing elements — one headline, one photo, one CTA
- Don't recolor the LEGO logo, rotate it, or remove the yellow rule beneath the wordmark
- Don't use the trinity colors at < 100% saturation — desaturated red looks like a misprint
- Don't use atmospheric soft shadows on primary CTAs — that breaks the brick-press metaphor
- Don't put yellow text on white or red text on blue — every pairing must hit WCAG AA contrast
- Don't use italic anywhere in nav, buttons, or headlines — the system has no italic voice
- Don't use age-pill border radius (`9999px`) on rectangular cards — pills are reserved

## 8. Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile | 320–599px | Single-column, hero type 32–40px, stacked CTAs, tile gutters drop to 8px |
| Tablet | 600–959px | 2-column theme grid, hero type 40–56px, sticky nav with hamburger |
| Desktop | 960–1279px | 3-column theme grid, hero type 56–64px, full mega-menu |
| Large Desktop | 1280–1439px | 4-column product grid, hero type 64–72px, max content width 1440px |
| XL Desktop | ≥1440px | Layout caps at 1440px, additional whitespace flanks the content |

### Touch Targets
- Primary CTAs: min 44px tap height (typically 48px on mobile with 16px horizontal padding)
- Nav icon buttons: 40px × 40px circular, with 8px hit-area buffer
- Age-pills and badges: stay at 32px+ even on mobile to remain tappable

### Collapsing Strategy
- **Nav**: Mega-menu collapses to hamburger drawer on tablet and below; logo lockup stays anchored top-left at minimum 40px height
- **Hero**: Two-column color-block heroes stack vertically on mobile — color block on top, product photo below
- **Theme grid**: 4 → 3 → 2 → 1 columns as viewport narrows; minimum tile height stays 280px to preserve billboard impact
- **Product grid**: 4 → 3 → 2 columns; never collapses to 1 — adjacency matters
- **Section spacing**: 96–128px desktop → 48–64px mobile, but still stud-aligned
- **Type scale**: Hero shrinks from 72 → 56 → 40 → 32px; weights stay heavy throughout

### Image Behavior
- Product photography preserves white seamless background at all breakpoints
- Theme billboards crop responsively — primary-color background extends, product photo recenters
- The LEGO logo lockup never scales below 40px wide — instead, it loses the yellow rule on tiny screens before disappearing entirely (minified app-icon variant)

## 9. Agent Prompt Guide

### Quick Color Reference
- Primary CTA: Lego Red (`#E3000B`)
- Secondary CTA: Lego Yellow (`#FFCF00`) with black text
- Informational CTA: Lego Blue (`#006DB7`)
- Page Background: Pure White (`#FFFFFF`)
- Primary Text: Lego Black (`#000000`)
- Secondary Text: Muted Gray (`#5A5A5A`)
- Card Border: Light Gray (`#E5E5E5`)
- Brick-Press Shadow: `0 2px 0 0 rgba(0,0,0,0.15)` rest, `0 4px 0 0 rgba(0,0,0,0.2)` hover
- Focus Ring: `0 0 0 3px rgba(0,109,183,0.2)`

### Example Component Prompts
- "Create a hero billboard on Lego Red (`#E3000B`) full-bleed with a 72px Cera Pro weight 900 headline in pure white, line-height 1.05, letter-spacing -0.5px. Add a white-background CTA — 16px Cera Pro weight 700 uppercase, `0.02em` letter-spacing, `8px` radius, `0 2px 0 0 rgba(0,0,0,0.15)` brick-press shadow."
- "Design a product card with white background, `1px solid #E5E5E5` border, `8px` radius, 16px internal padding. Square product image on white seamless. Title in Cera Pro 16px weight 700, price in Cera Pro 18px weight 800 with `tnum` tabular figures."
- "Build a 3-column theme grid: each tile is a `12px` radius color billboard (alternating Lego Red / Yellow / Blue), 320px min-height, 32px internal padding, with a 24px Cera Pro weight 800 theme name and a white CTA at the bottom."
- "Create an age-recommendation pill — pure white background, `1px solid #000`, `9999px` radius, 12px Cera Pro weight 700 black text reading 'Ages 9+', padding 4px 12px."
- "Design a country-gate modal — split horizontally into a Lego Blue (`#006DB7`) panel and a Lego Yellow (`#FFCF00`) panel, each with a 24px weight 800 headline, an icon row, and a centered white CTA with `8px` radius. Wrap in a `12px` radius white container with `0 12px 48px rgba(0,0,0,0.25)` shadow."

### Iteration Guide
1. Start with the Lego trinity — red, yellow, blue — as full-bleed billboards. White is the connective tissue.
2. Cera Pro at weight 700–900 for all display. Never lighter. Never italic.
3. Snap every spacing value to the 8px stud-grid (`8, 16, 24, 32, 48, 64, 96`). No 13px, no 22px.
4. Default radius is `8px`. Hero billboards get `12px`. Age pills and circular icons get `9999px`. Never zero.
5. Primary CTAs use the brick-press shadow (`0 2px 0 0 rgba(0,0,0,0.15)`) and depress on click — that's the brand's tactile signature.
6. Uppercase + `0.02em` tracking belongs on CTAs and category labels, not headlines.
7. Tabular figures (`tnum`) on every price and product number — they must align across listings.
8. Color pairings must hit WCAG AA: white on red and blue, black on yellow. Never the reverse.
9. The LEGO logotype lockup is sacred — red square, white wordmark, yellow rule. Don't recolor, rotate, or strip the rule.
10. One color block, one headline, one product photo, one CTA. The system rewards restraint inside saturation.
