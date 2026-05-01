# Design System Inspired by Athletic Brewing

## 1. Visual Theme & Atmosphere

Athletic Brewing's website is the visual translation of pleased-to-be-sober, outdoor, masculine wholesomeness. The page opens on a soft off-white canvas with a deep navy (`#003a5d`) carrying the brand authority — applied to the logo, headlines, and link text — while a saturated outdoor-utility orange (`#ff5a1f`) and a high-vis chairlift yellow (`#fadf33`) handle the action layer. Nothing here whispers craft beer in the dim-bar sense; this is brewery-as-trailhead, designed to read at a glance from a phone screen mid-run, mid-hike, mid-ski-lift.

The layout is unapologetically commerce-first — Shopify-style product grids, fat announcement bar at the top, "WELCOME OFFER: 25% OFF + FREE SHIPPING" hammering the value prop before scroll — but the brand veneer overlaying that grid is deeply outdoor-heritage. Beer can illustrations carry woodcut-style adventure motifs (mountains, rivers, fish, pines), and the typography splits the difference between condensed athletic display (bold, slightly varsity) for headlines and a clean humanist sans for body. Where Cape uses restraint and Liquid Death uses shock, Athletic Brewing uses confidence-of-purpose: a grown-up outdoor lifestyle brand that happens to ship cans.

What distinguishes the system most is its **color tension between heritage navy and trail-hazard orange/yellow**. The navy gives the brand its quiet authority — the kind of color a national park sign uses. The orange and yellow give it its pulse, marking every place a customer should tap or look. There is almost no black; nearly every "dark" element is actually `#003a5d`. There is almost no neutral gray; subtle warmth lives in the off-white background and in cream card surfaces. The result feels like a 1970s ski resort poster reissued for a modern e-commerce stack.

**Key Characteristics:**
- Navy `#003a5d` as the workhorse "dark" — replaces black across text, logo, and outline elements
- Outdoor-utility orange (`#ff5a1f`) for primary CTAs — "ORDER UP", "SHOP NOW", "ADD TO CART"
- Chairlift yellow (`#fadf33`) for promotional pills and welcome-offer CTAs
- Soft off-white canvas (`#f7f4ee`) with cream product-card surfaces — never harsh white
- Bold athletic-display headlines paired with clean humanist body sans
- Woodcut-style can illustrations carry the outdoor-adventure motif (mountains, rivers, fish)
- Pill-shaped buttons (`1000px` radius) — a very deliberate non-tech, non-luxury choice
- 25% off / free shipping / member-only stickers used as recurring visual rhythm
- Product photography is hero — cans on table with full-pour pint glass, lifestyle in supporting role

## 2. Color Palette & Roles

### Primary
- **Athletic Navy** (`#003a5d`): Primary text, headlines, logo, footer surface, body copy, link default. The brand's anchor color — this is the "black" of the system.
- **Brewery Cream** (`#f7f4ee`): Primary page background. Warm off-white with a paper-bag undertone — never pure `#ffffff`.
- **Card Cream** (`#ede4d3`): Slightly toasted warm neutral used on product card backgrounds, banner blocks, and section dividers.

### Brand Accent
- **Trail Orange** (`#ff5a1f`): Primary CTA color — "ORDER UP", "SHOP NOW", "ADD TO CART", "GET STARTED". The action layer of the entire site.
- **Chairlift Yellow** (`#fadf33`): Secondary accent for promotional CTAs, welcome-offer banners, "GET THE WELCOME OFFER" buttons, and badge/sticker treatments.
- **Sky Cyan** (`#a8d8e8`): Soft promotional-bar fill — used on the top "WELCOME OFFER" announcement bar and seasonal callouts.

### Secondary Brand
- **Deep Sea Blue** (`#005677`): Lighter navy used for secondary links, hover states, and product subtitle text.
- **Hop Green** (`#3f8f4f`): Occasional accent tied to product variant tags ("Light", "IPA"), eco/wellness moments, and "Run Club" event copy.
- **Brick Red** (`#c0432e`): Reserved for sale tags, urgency stickers, and limited-release callouts.

### Neutrals & Text
- **Athletic Navy** (`#003a5d`): All primary text, headings, body copy.
- **Mid Slate** (`#5a6770`): Secondary copy, captions, metadata, breadcrumbs.
- **Pebble Gray** (`#cdcdcd`): Dividers, input borders, disabled states.
- **Cloud White** (`#ffffff`): Inverted surfaces only — text on navy footer, modal interiors.

### Surface & Borders
- **Page Background**: Brewery Cream (`#f7f4ee`)
- **Card Surface**: Card Cream (`#ede4d3`) or Cloud White (`#ffffff`) depending on density
- **Footer Surface**: Athletic Navy (`#003a5d`) — full-width dark band closing the page
- **Border Default**: `1px solid #003a5d` for outline buttons; `1px solid #cdcdcd` for inputs

### Sticker / Badge Colors
- **Sale Sticker Yellow** (`#fadf33`) — black `#003a5d` text
- **Limited Sticker Orange** (`#ff5a1f`) — white text
- **Members Sticker Navy** (`#003a5d`) — yellow `#fadf33` text
- **Best Seller Cream** (`#ede4d3`) — navy text

### Gradient System
- Athletic Brewing is **largely gradient-free**. The system relies on solid blocks of navy/orange/yellow/cream with woodcut illustration carrying any tonal complexity. The only gradient surface is the very top of the page where a soft sky-cyan announcement bar sits above the cream canvas — and even that reads as a flat fill, not an interpolation.

## 3. Typography Rules

### Font Family
- **Display**: `Knockout`, `Industry`, or `Trade Gothic Bold Condensed` — a condensed athletic sans with high contrast and bold weights. Headlines lean varsity-yearbook without crossing into kitsch.
- **Body**: `Inter`, `Söhne`, or `GT America` — a clean humanist sans for paragraph copy and UI chrome
- **Accent / Script**: occasional hand-drawn marker script on can labels and promotional stickers ("Aftershift", "Run Club") — never used in UI
- **Fallbacks**: `'Helvetica Neue', Arial, sans-serif`

*Note: Athletic Brewing's exact display family appears to be a custom or licensed condensed grotesk. Trade Gothic Next Bold Condensed and Knockout HTF49 Liteweight serve as close substitutes; Inter Tight Bold or Barlow Condensed work as web-safe alternatives.*

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Display Hero | Knockout / Trade Gothic | 72px (4.50rem) | 700 | 1.00 | -0.5px | Landing hero ("OUR CHEFS' CHOICE") |
| Display Large | Knockout | 56px (3.50rem) | 700 | 1.05 | -0.5px | Section heads, category titles |
| Display | Knockout | 40px (2.50rem) | 700 | 1.10 | -0.25px | Sub-section heads, product collection titles |
| Section Heading | Knockout | 32px (2.00rem) | 700 | 1.15 | -0.25px | Card titles, "GREAT TASTING, NON-ALC" panels |
| Sub-heading | Knockout | 24px (1.50rem) | 700 | 1.20 | normal | Product names on cards |
| Body Large | Inter | 18px (1.125rem) | 400 | 1.50 | normal | Intro paragraphs, hero subheadlines |
| Body | Inter | 16px (1.00rem) | 400 | 1.55 | normal | Standard reading text |
| Body Small | Inter | 14px (0.875rem) | 400 | 1.45 | normal | Card descriptions, metadata |
| Nav Link | Inter | 14px (0.875rem) | 600 | 1.00 | 0.04em | Top navigation, often uppercase |
| Button UI | Inter or Knockout | 14–16px | 700 | 1.00 | 0.05em | Always uppercase, bold |
| Caption | Inter | 12px (0.75rem) | 400 | 1.40 | normal | Footer copy, legal, micro-tags |
| Sticker | Marker Script | 18–28px | 700 | 1.00 | normal | Hand-drawn promo overlays only |

### Principles
- **Display does the shouting**: All hero, section, and product titles use the condensed bold display face — uppercased, weight 700, with negative tracking. This is where the brand swagger lives.
- **Body does the explaining**: Inter (or equivalent humanist sans) at weight 400 keeps paragraph copy approachable and legible. The contrast between condensed-display and round-humanist body is the typographic personality.
- **Uppercase as default for chrome**: Nav links, button labels, banner copy, and badges are nearly always uppercase. Mixed-case is reserved for body and longform content.
- **Tight tracking on display**: `-0.25` to `-0.5px` on display sizes locks bold headlines into dense blocks. Body returns to normal tracking.
- **Two-family discipline**: Display family + body family. The marker script appears only on illustrated stickers, never inside the UI grid.

## 4. Component Stylings

### Buttons

**Primary Trail Orange**
- Background: Trail Orange (`#ff5a1f`)
- Text: Cloud White (`#ffffff`)
- Padding: 14px 28px standard, 10px 20px compact
- Radius: `1000px` (full pill)
- Border: none default; on hover, transform `scale(1.02)` and shift to `#e54a14`
- Font: 14px Inter weight 700, uppercase, letter-spacing `0.05em`
- Use: Primary CTA — "ORDER UP", "SHOP NOW", "ADD TO CART"

**Secondary Yellow**
- Background: Chairlift Yellow (`#fadf33`)
- Text: Athletic Navy (`#003a5d`)
- Padding: 14px 28px
- Radius: `1000px` (pill)
- Hover: rotate decorative icon 90deg, scale 1.1, opacity 0.9
- Use: Welcome-offer CTAs, promotional pills — "GET THE WELCOME OFFER"

**Navy Outline**
- Background: transparent
- Text: Athletic Navy (`#003a5d`)
- Border: `2px solid #003a5d`
- Radius: `1000px` (pill)
- Hover: fill with `#003a5d`, text flips to `#ffffff`
- Use: Secondary actions — "LEARN MORE", "JOIN THE CLUB"

**Navy Solid**
- Background: Athletic Navy (`#003a5d`)
- Text: Cloud White (`#ffffff`)
- Radius: `1000px`
- Hover: lifts to `#005677`
- Use: Footer CTAs, account/login flows

### Cards & Containers

**Product Card**
- Background: Card Cream (`#ede4d3`) or `#ffffff`
- Border: none, or `1px solid rgba(0, 58, 93, 0.1)`
- Radius: `12–16px` — soft but not pillowy
- Shadow: `0 2px 8px rgba(0, 58, 93, 0.08)` — quiet elevation
- Internal padding: 20–24px
- Anatomy: badge (top-left or top-right) + can image (centered) + product name (display, bold, uppercase) + price + ATC button
- Hover: subtle lift `translateY(-2px)`, shadow deepens to `0 6px 16px rgba(0, 58, 93, 0.12)`

**Promo Banner**
- Background: Sky Cyan (`#a8d8e8`)
- Text: Athletic Navy (`#003a5d`)
- Height: 36–44px sticky top
- Content: centered uppercase Inter bold 14px — "WELCOME OFFER: 25% OFF + FREE SHIPPING"

### Badges / Stickers / Pills

**Promo Sticker (hand-drawn)**
- Decorative cream/yellow shapes with marker-style script — "Aftershift", "Best Seller", "New Brew"
- Slight rotation (`-3deg` to `5deg`) — never perfectly aligned
- Layered over hero imagery and product cards as visual punctuation

**Status Pill**
- Background: Trail Orange (`#ff5a1f`) for "Limited", Chairlift Yellow for "Sale", Athletic Navy for "Members Only"
- Text: contrast color (white/navy), 12px Inter weight 700, uppercase, 0.05em tracking
- Padding: 4px 10px
- Radius: `1000px` (pill)

### Inputs & Forms
- Background: `#ffffff`
- Border: `1px solid #cdcdcd`
- Radius: `8px`
- Font: 16px Inter weight 400
- Text color: `#003a5d`
- Focus: border `#003a5d`, outline `rgba(0, 58, 93, 0.2) 0 0 0 3px`
- Padding: 12px 16px
- Newsletter / age-gate forms are the most prominent form moments — large, centered, single-field

### Navigation
- Top utility bar: thin sky-cyan promo strip, dismissible
- Main nav: cream (`#f7f4ee`) bar with navy logo centered, primary links left ("SHOP", "JOIN THE CLUB", "SUBSCRIBE", "LEARN"), utility right ("FIND IN STORE", account icon, cart)
- Links: Inter 14px weight 600 uppercase, navy default, hop-green hover or underline-on-hover (`underline 0.3rem`)
- Mega-menu on hover: full-width drop panel with product collection imagery in a 3–4 column grid

### Decorative Elements

**Woodcut Illustration**
- Black-line-on-flat-color illustrations of mountains, pines, rivers, fish, sunsets — applied to product cans and supporting marketing imagery
- Heritage outdoor aesthetic — suggests national park / craft brewery / 70s ski-poster rather than tech-startup
- Used on can labels first, then echoed in section dividers and editorial headers

**Marker Script Overlays**
- Hand-drawn callouts ("Aftershift", "Run Club", "New") layered over photography
- Always tilted 3–5 degrees — the deliberate not-perfectly-aligned moment

## 5. Layout Principles

### Spacing System
- Base unit: 4px (with 8px as the workhorse)
- Scale: 4px, 8px, 12px, 16px, 20px, 24px, 32px, 40px, 48px, 64px, 80px, 120px
- Notable: Athletic Brewing uses a denser commerce-first scale — sections at 64–80px, card grids at 16–24px gaps, button padding at 14×28px. Less editorial breathing than Cape, more product density.

### Grid & Container
- Max content width: ~1280px for centered content; full-bleed for hero and announcement strips
- Hero: split layout — text left (cream), product photography right (full-bleed)
- Product grid: 4-column desktop, 2-column tablet, 2-column mobile (cans are wide enough that single-column wastes space)
- Footer: 4–5 column navy block with newsletter signup hero
- Modals: centered, max-width 480px, cream background, navy heading, yellow CTA

### Whitespace Philosophy
- **Commerce-first density**: The grid is meant to move product, not to read like a magazine. Cards pack tightly with 16–24px gaps.
- **Hero and footer breathe**: 80–120px vertical space at the top hero and bottom footer give the brand its premium-outdoor feel before the grid takes over.
- **Sticker punctuation**: Decorative marker stickers (rotated slightly) interrupt grid rhythm — keeps the page feeling hand-assembled rather than CMS-stamped.

### Border Radius Scale
- Sharp (0px): Announcement strip, footer block
- Soft (8px): Inputs, small surface chips
- Card (12–16px): Product cards, content panels, modals
- Pill (`1000px`): All buttons, all status badges, image avatar/circle moments
- No radius is mid-range (24–32px). The system is structured: container = 12–16px, button = full pill.

## 6. Depth & Elevation

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | No shadow | Page canvas, banner strips, footer block |
| Subtle Card (Level 1) | `0 2px 8px rgba(0, 58, 93, 0.08)` | Product cards default state |
| Lifted Card (Level 2) | `0 6px 16px rgba(0, 58, 93, 0.12)` | Product cards on hover, modal cards |
| Sticky Header (Level 3) | `0 1px 0 rgba(0, 58, 93, 0.1)` | Sticky nav after scroll — single-pixel shadow line |
| Modal (Level 4) | `0 24px 48px rgba(0, 58, 93, 0.18)` | Welcome-offer modal, age gate, cart drawer |
| Sticker Pop (Decorative) | `0 3px 0 #003a5d` | Hand-drawn promo stickers — hard offset shadow for "stuck-on" feel |

**Shadow Philosophy**: Athletic Brewing's depth system is quiet on the grid (subtle navy-tinted shadows on cards) and punchy on the decoration (hard offset shadows on hand-drawn stickers). The atmospheric shadows never use pure black — they're tinted with the brand navy at low opacity, so the page feels color-coordinated even in its lifts. Stickers get the hard offset treatment, signaling a different visual register: "this was added by a person, not generated."

### Decorative Depth
- Stickers get `0 3px 0 #003a5d` — hard offset, no blur
- Cards get soft, low-opacity navy-tinted shadows
- No glow effects, no neumorphism, no glassmorphism — the system is honestly flat-with-lifts

## 7. Do's and Don'ts

### Do
- Use Athletic Navy (`#003a5d`) as the "black" of the system — it goes on text, logos, footers, and outline borders
- Apply Trail Orange (`#ff5a1f`) only to primary CTAs — preserve its action signal
- Pair condensed bold display headlines with clean humanist body sans — that contrast is the typographic identity
- Use full pill (`1000px`) radius on every button and status badge
- Keep the page background warm cream (`#f7f4ee`), never pure white
- Use marker-script stickers as decorative punctuation, slightly tilted
- Stack sale/limited/members badges on product cards for scannable scanning
- Lean into woodcut illustration on cans and editorial moments — outdoor heritage is the visual anchor
- Uppercase nav, buttons, and banner copy with `0.04–0.05em` tracking
- Pair Trail Orange with Chairlift Yellow when promotional energy needs to dial up — never use them on the same element

### Don't
- Don't use pure `#000` for text — Athletic Navy (`#003a5d`) is the dark
- Don't use pure `#ffffff` for the page canvas — always Brewery Cream (`#f7f4ee`)
- Don't use mid-range button radius (4–16px) — buttons are always pill
- Don't introduce purple, pink, or magenta accents — the palette is navy + orange + yellow + green only
- Don't use marker-script for UI labels or paragraph copy — it lives on stickers, not in the grid
- Don't stack all three accents (orange + yellow + cyan) on a single card — pick one action color per surface
- Don't use sterile drop shadows with black alpha — tint them navy
- Don't over-illustrate UI surfaces — woodcut imagery belongs on cans and editorial moments, not on form fields or chrome
- Don't make the hero text-only — Athletic Brewing always pairs hero copy with a beer-can-on-table photograph

## 8. Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile Small | <420px | Hero drops to 36–40px, single-column product grid (2 cans wide) |
| Mobile | 420–660px | 2-column product grid, 48–56px hero, stacked nav (hamburger) |
| Tablet | 660–990px | 2–3 column grid, 56–64px hero, condensed top nav |
| Desktop | 990–1199px | 4-column product grid, 64–72px hero, full mega-menu nav |
| Large Desktop | ≥1200px | Maximum 1280px container, 72px hero, full visual richness |

### Touch Targets
- Primary CTAs: min 44px tap height (most run 48–52px), 28px horizontal padding
- Nav links: 44px tap height with 16px horizontal padding
- ATC buttons on product cards: full-width pill, 44px min height
- Sticker overlays: not interactive — purely decorative

### Collapsing Strategy
- **Nav**: Full mega-menu collapses to hamburger on mobile; off-canvas drawer opens with stacked links
- **Hero**: Two-column layout (text + photo) collapses to stacked single-column with photo first
- **Product grid**: 4-column → 2-column → 2-column (cans don't go single-column)
- **Footer**: 5-column → 2-column → single accordion on mobile
- **Stickers**: Reduce in count and complexity on mobile — keep one or two anchor stickers per section

### Image Behavior
- Can-on-table hero photography maintains aspect ratio across breakpoints
- Woodcut illustrations on cans scale fluidly without becoming icon-blurry
- Lifestyle photography (hiking, climbing, running, brewing) crops to portrait on mobile
- Marker stickers scale to maintain readability — never below 14px effective text size

## 9. Agent Prompt Guide

### Quick Color Reference
- Primary CTA: Trail Orange (`#ff5a1f`)
- Secondary CTA: Chairlift Yellow (`#fadf33`)
- Promo Banner: Sky Cyan (`#a8d8e8`)
- Page Background: Brewery Cream (`#f7f4ee`)
- Card Background: Card Cream (`#ede4d3`)
- Primary Text / Logo / Dark: Athletic Navy (`#003a5d`)
- Secondary Link: Deep Sea Blue (`#005677`)
- Hop Green Accent: (`#3f8f4f`)
- Sale Red: (`#c0432e`)
- Card Shadow: `0 2px 8px rgba(0, 58, 93, 0.08)`
- Modal Shadow: `0 24px 48px rgba(0, 58, 93, 0.18)`

### Example Component Prompts
- "Create a hero section on Brewery Cream (`#f7f4ee`) with a 72px Knockout Bold Condensed headline (`#003a5d`), uppercase, line-height 1.00, letter-spacing -0.5px. Subhead in Inter 18px weight 400 below. Primary CTA: Trail Orange (`#ff5a1f`) pill button with white uppercase 14px Inter bold label, padding 14px 28px, radius `1000px`. Right side: full-bleed photograph of a beer can next to a poured pint glass on a wooden table."
- "Design a product card on Card Cream (`#ede4d3`) background, 16px radius, soft shadow `0 2px 8px rgba(0,58,93,0.08)`. Top-left: yellow `#fadf33` 'Best Seller' pill badge with navy uppercase 12px Inter bold text, padding 4px 10px. Centered: woodcut-illustrated beer can. Below: product name in Knockout 24px bold uppercase navy, then price in Inter 16px navy, then full-width orange `#ff5a1f` 'ADD TO CART' pill button."
- "Build a sticky promo bar at the very top of the page: 40px tall, Sky Cyan (`#a8d8e8`) background, centered Inter 14px weight 700 uppercase navy text 'WELCOME OFFER: 25% OFF + FREE SHIPPING'. No shadow, no border."
- "Create a welcome-offer modal: cream `#f7f4ee` background, 480px max-width, 16px radius, shadow `0 24px 48px rgba(0,58,93,0.18)`. Heading in Knockout 32px bold uppercase navy '25% OFF TWO 6-PACKS', body in Inter 14px navy with terms-and-conditions copy, CTA button in Chairlift Yellow `#fadf33` with navy uppercase 'GET THE WELCOME OFFER' label, full pill radius."
- "Design a hand-drawn marker sticker overlay: cream-yellow shape with navy outline, marker-script text 'Aftershift', tilted -3deg, hard offset shadow `0 3px 0 #003a5d`. Position absolutely over the hero photograph."

### Iteration Guide
1. Default to Athletic Navy (`#003a5d`) for any element you'd normally use black on — text, logos, borders, dark surfaces
2. Trail Orange (`#ff5a1f`) is sacred for primary CTAs — never water it down with secondary uses
3. Buttons are always full pill (`1000px`) — never sharp, never mid-radius
4. Pair condensed bold display headlines (Knockout / Trade Gothic Bold Condensed) with humanist body sans (Inter) — that contrast is the brand
5. Page background is warm cream (`#f7f4ee`), never pure white
6. Stickers and marker-script callouts get hard offset shadows and slight rotation — they're the "hand-made" punctuation
7. Product cards get subtle navy-tinted shadows on hover — never harsh black
8. Lean into woodcut illustration for can artwork and editorial heroes; keep UI chrome clean
9. Uppercase nav, buttons, and banners with `0.04–0.05em` tracking — mixed-case is for body
10. The visual story is heritage outdoor, not tech-craft — every choice should feel like it could live on a national park sign before it lives on a SaaS dashboard
