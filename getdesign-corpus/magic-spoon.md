# Design System Inspired by Magic Spoon

## 1. Visual Theme & Atmosphere

Magic Spoon's website is a Saturday-morning cartoon broadcast from 1973 — built for a high-protein cereal brand that earns the right to be loud. Where other DTC food sites converge on muted minimalism (cream backgrounds, lowercase wordmarks, pastel sans-serifs), Magic Spoon does the opposite: deep cosmic purple (`#3f0791`) saturates the canvas, headlines stack in extrabold Poppins black caps, and the secondary palette spits hot pink, electric yellow, and ice-blue cyan in equal measure. Every page reads like the back of a sugary cereal box — the kind your parents wouldn't buy you — except the protein math actually pencils out.

The Poppins typeface, deployed at weights 700 and 900 across every display moment, is the brand's structural backbone. Headlines run at 60–90px with `1.00` line-height and minimal tracking, packed into dense, billboard-grade blocks. Body copy steps down to a far gentler weight 400 at 16–22px. The contrast between heavy display and soft body creates a clear hierarchy: the headline shouts, the paragraph explains. Add to that the relentless use of `UPPERCASE` with `0.8–0.9px` letter-spacing for nav, buttons, and section labels — every interactive surface reads as a stamped, declarative label.

What makes Magic Spoon unmistakable is the **shape language**: pill buttons at `50px` radius, asymmetric product cards with one squared corner (`25px 25px 25px 0px`), full-width gradient banners that fade pink → cyan → yellow, and confetti-scatter decorative motifs (sparkles, rainbows, mini cereal pieces) raining across hero and CTA panels. The whole system reads as cosmic 70s nostalgia rendered in 2026 vector — holographic foil energy without the literal foil. Where Cape uses restraint as confidence, Magic Spoon uses joy as confidence.

**Key Characteristics:**
- Poppins extrabold (900) and bold (700) for all display — joyful weight, never lightweight
- Deep cosmic purple (`#3f0791`) as primary canvas — saturated, not subtle
- White pill buttons (`50px` radius) with purple text — high-contrast lozenges
- Asymmetric card radius (`25px 25px 25px 0px`) — one sharp corner per card, signature shape
- Multi-stop gradient banners (hot pink → cyan → yellow) for section breaks
- Uppercase nav and buttons with `0.8px` letter-spacing — billboard-stamped UI
- Confetti decoration: sparkles, mini cereal, rainbow swooshes scattered across hero panels
- White `2px inset` outline on ghost buttons — clean stroke without filled chrome

## 2. Color Palette & Roles

### Primary
- **Cosmic Purple** (`#3f0791`): The defining brand color — page backgrounds, hero sections, primary text on light surfaces. Counted 1,251 times in the extracted CSS — this IS the brand.
- **Pure White** (`#ffffff`): Headlines on purple, button fills, wordmark, content panels.
- **Royal Violet** (`#4a00c4`): Mid-tone link color — inline links and secondary CTAs on white backgrounds.

### Brand Accents (the cereal-box rainbow)
- **Hot Magenta** (`#ec1f8e`): Top promo bar, "Build Your Own Bundle" panel, BEST SELLER badge — the loudest accent, reserved for celebration moments.
- **Ice Cyan** (`#bfefff`): Mid-stop in the hero gradient, secondary surface tint — cooling counterweight to magenta.
- **Sunshine Yellow** (`#fbca10`): Inline "BESTSELLER" sticker tag, sparkle accents, review-star color.
- **Electric Violet** (`#5b1bed` / `#5b00ed`): Hover state for purple buttons — saturated jump signaling interactivity.
- **Pale Lavender** (`#cac4f4`): Secondary button surface, soft container fill.
- **Lavender Mist** (`#e1d4f7`): Page background on collection/product browsing pages.

### Neutrals & Text
- **Cosmic Purple** (`#3f0791`): All body text on light/lavender backgrounds — never pure black.
- **Soft Black** (`#232323`): Search-result product titles and dense data text.
- **Mid Gray** (`#535353`): Price text and metadata.
- **Light Gray** (`#9a9a9a`): Compare-at strikethrough prices, disabled states.
- **Slate Cool** (`#546b7d`): Inactive tab labels in search overlays.

### Surface & Borders
- **Lavender Page** (`#e1d4f7`): Light-mode page canvas for collection and content pages.
- **White Card** (`#ffffff`): Product card and content surfaces inside lavender contexts.
- **Border Faint** (`#eeeeee`): 1px dividers in dense list layouts.
- **Underline 2px solid**: Bottom-only underline on link spans — Cosmic Purple on light, White on dark.

### Gradient System
- **Cosmic Sweep** (linear, magenta → violet → cyan): The signature hero/banner gradient. `linear-gradient(90deg, #ec1f8e 0%, #5b1bed 45%, #00d4ff 100%)` — used for full-width section bars and the rainbow text fill on "EXPLORE OUR PRODUCTS"-style headers.
- **Sunset Wash** (peach → cyan): Top-bar promo strip gradient — a softer warm-to-cool sweep for limited-edition announcements.
- **Holographic Text Fill**: Headlines occasionally fill with a multi-stop rainbow gradient (pink → orange → yellow → green → cyan → purple) using `background-clip: text` — applied sparingly to hero promos for foil-sticker energy.

## 3. Typography Rules

### Font Family
- **Primary**: `Poppins`, with fallback: `Helvetica`, `Arial`, `sans-serif`
- **Display Specialty**: `Mabry Pro` — used at weight 700 for select editorial moments (about-page sub-heads, occasional callouts)
- **Mono / Default**: `Arial` at weight 700 uppercase for some legacy buttons and chrome — phasing into Poppins
- **OpenType Features**: Standard ligatures, no stylistic sets

*Note: Poppins is a free Google geometric sans by Indian Type Foundry. For close substitutes outside Google Fonts, Sofia Pro or Avenir Next at black weight render the same energy. Mabry Pro is a Colophon Foundry typeface used here for editorial accent.*

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Display Hero | Poppins | 90px (5.63rem) | 500 | 1.00 | normal | Maximum size — landing hero on desktop |
| Display XL | Poppins | 80–82px | 500–700 | 0.91–1.00 | normal | Secondary hero, page-section openers |
| Display Large | Poppins | 72px (4.50rem) | 700 | 1.00 | normal | Section heads on white |
| Display Black | Poppins | 64px (4.00rem) | 900 | 1.20 | normal | Editorial-weight section openers |
| Display | Poppins | 60px (3.75rem) | 700 | 1.05 | normal | Standard feature heads |
| Section Heading | Poppins | 48px (3.00rem) | 700 | 1.00 | normal | Sub-section titles |
| Sub-heading Large | Poppins | 32px (2.00rem) | 600–700 | 1.25 | normal | Often `UPPERCASE` for billboard chrome |
| Sub-heading | Poppins | 28px (1.75rem) | 500 | 1.25 | 1.12px | Card titles, often uppercase |
| Editorial | Mabry Pro | 30px (1.88rem) | 700 | 1.80 | normal | Specialty editorial headline weight |
| Body Large | Poppins | 22–24px | 400 | 1.30–1.42 | normal | Hero subhead, intro paragraphs |
| Sub-heading Small | Poppins | 20px (1.25rem) | 700–900 | 1.00 | 0.8px | Uppercase nav links, button labels |
| Body | Poppins | 16–18px | 400 | 1.40 | normal | Standard reading paragraphs |
| Button UI | Poppins | 18–22px | 700–900 | 1.00 | 0.72–0.9px | Uppercase, tracked-out chrome |
| Caption | Poppins | 13–14px | 400 | 1.00–1.40 | normal | Small metadata, fine print |
| Tag / Sticker | Poppins | 10–12px | 500–900 | 1.00–1.40 | normal | Often `UPPERCASE`, tight |

### Principles
- **Joyful weight**: Display headlines run at weight 700–900 by default. Where Cape whispers at 300, Magic Spoon shouts at 900. The ceiling is `Poppins Black 900` — used for the boldest cereal-box moments.
- **Uppercase as chrome signature**: All nav links, buttons, badges, and section sub-heads use `text-transform: uppercase` with `0.72–0.9px` letter-spacing. Mixed case is reserved for headlines and body — uppercase is the action/label register.
- **Tight display line-height**: Display sizes (48px+) lock to `1.00–1.05` line-height for billboard-tight headline blocks. Body relaxes to `1.30–1.42` for readability.
- **No negative tracking**: Letter-spacing stays at `normal` or pushes positive (`0.8px+`) on uppercase chrome. The geometric warmth of Poppins doesn't need optical tightening the way grotesks do.
- **Three-weight system**: Body 400, sub-heads 500–700, display 700–900. No lightweight 300 anywhere — lightness reads off-brand.
- **Mabry Pro as accent**: When a moment needs editorial gravity (about-page heads, founder quotes), Mabry Pro at weight 700 with generous `1.80` line-height creates a softer pause from the Poppins drumbeat.

## 4. Component Stylings

### Buttons

**Primary White Pill (on purple)**
- Background: Pure White (`#ffffff`)
- Text: Royal Violet (`#4a00c4`) or Cosmic Purple (`#3f0791`)
- Padding: `22px 51px` (generous), `18px 30px` (compact)
- Radius: `50px` (full pill)
- Border: `0px` default
- Shadow: `none` default; soft `rgba(0, 0, 0, 0.08) 0px 15px 50px 0px` on elevated CTAs
- Font: 18–22px Poppins weight 700–900, uppercase, letter-spacing `0.72–0.9px`
- Hover: background → Electric Violet (`#5b00ed`), text → white, scale `1.05`
- Use: Primary CTAs — "SHOP CEREAL", "BUILD YOUR OWN BUNDLE", "SHOP NOW"

**Primary Purple Pill (on white/lavender)**
- Background: Cosmic Purple (`#3f0791`)
- Text: Pure White (`#ffffff`)
- Padding: `22px 51px`
- Radius: `50px`
- Font: 22px Poppins weight 900 uppercase
- Hover: background → Electric Violet (`#5b00ed`), 1.05 scale
- Use: Primary CTA on light pages — "SHOP ALL", checkout actions

**Ghost Stroke Pill (white outline on purple)**
- Background: transparent
- Text: White (`#ffffff`)
- Padding: `0px 30px` minimum
- Radius: `28px`
- Shadow: `rgb(255, 255, 255) 0px 0px 0px 2px inset` — 2px inset white stroke
- Font: 20px Poppins weight 700 uppercase, letter-spacing `0.8px`
- Hover: background → Electric Violet (`#5b00ed`), text stays white
- Use: Secondary CTAs on dark/purple sections — "LEARN MORE", "BACK TO SHOP"

**Pale Lavender Toggle**
- Background: Pale Lavender (`#cac4f4`)
- Text: Cosmic Purple (`#3f0791`)
- Radius: `15px`
- Active state: background → `#5b1bed`, text → white
- Use: Tab-style filters, pack-size selectors on product pages

**Hot Pink Action**
- Background: Hot Magenta (`#ec1f8e`)
- Text: Pure White (`#ffffff`)
- Radius: `50px`
- Font: Poppins 700 uppercase
- Use: High-emphasis promo CTAs — "Build Your Own Bundle", "Get Started" inside celebration panels

**Circular Pagination Dot**
- Active: Pure White (`#ffffff`), Cosmic Purple text/border
- Inactive: Cosmic Black (`rgb(0, 0, 0)` at `0.2` opacity)
- Size: ~12–16px
- Radius: `50%` (true circle)
- Use: Carousel dots, swiper navigation across product galleries

### Cards & Containers
- **Product Card**: White (`#ffffff`) background, `25px 25px 25px 0px` asymmetric radius (one squared corner — the signature shape). Internal padding 20–30px. Image area takes 60% of card height.
- **Hero/Promo Panel**: Hot Magenta or full Cosmic Sweep gradient, `25px` radius, white text and pill CTA. Decorative confetti scattered across the surface.
- **Content Panel**: Pale Lavender (`#cac4f4`) or White, `20–25px` radius, 30–60px internal padding.
- **Ribbon/Banner Strip**: Hot Magenta or gradient sweep, full-width, no radius, 40–60px tall, white uppercase Poppins 500–700 text.

### Badges / Tags / Stickers

**Best Seller Pill**
- Background: Hot Magenta (`#ec1f8e`) or Cosmic Purple (`#3f0791`)
- Text: Pure White (`#ffffff`)
- Padding: 8px 14px
- Radius: `50px` (pill)
- Font: 12px Poppins weight 900 uppercase
- Often paired with sparkle/star emoji in copy: "✨ BEST SELLER ✨"

**Sticker Tag (yellow inline)**
- Background: Sunshine Yellow (`#fbca10`)
- Text: Cosmic Purple (`#3f0791`)
- Padding: 4px 8px
- Radius: `15–20px`
- Font: 10–12px Poppins weight 700 uppercase
- Use: Inline emphasis tags inside nav menus ("BESTSELLER" next to Bundle Builder), promo callouts

**Round Stamp Badge**
- Background: Hot Magenta or Cosmic Purple
- Text: White
- Size: 60–80px circle (`50%` radius)
- Rotation: occasionally `-10deg` for sticker-applied feel
- Use: "BEST SELLER" rosette on top product cards, "NEW FLAVOR" call-outs

### Inputs & Forms
- Background: transparent (on dark) or White (`#ffffff`) on light
- Border: `0px` default, paired with `2px inset white` shadow on dark sections
- Radius: `30px` (pill input) — matches button language
- Font: 16px Poppins weight 400
- Text: White on dark, Cosmic Purple on light
- Padding: `0px 20px` horizontal, ~50px row height
- Focus: native webkit focus ring or 2px purple stroke

### Navigation
- **Top promo bar**: Hot Magenta (`#ec1f8e`) full-width strip, white Poppins 500 uppercase 14px text centered, ~40px tall. Often includes sparkle emoji and "SHOP NOW" inline link.
- **Main nav**: Cosmic Purple background on home, White on collection pages. Wordmark left (the "MAGIC SPOON" stacked logotype with sparkle dot). Center: nav links — "CEREAL", "PASTRIES", "TREATS", "GRANOLA", "BUNDLE BUILDER", "SHOP ALL", "ABOUT US" — all Poppins 700 uppercase 18px with 0.9px tracking and dropdown carets.
- **Inline accents**: nav items occasionally include a small sparkle SVG (✦) before/after the label, and the "BUNDLE BUILDER" item has an attached yellow "BESTSELLER" sticker tag.
- **Hover**: text color shifts from Cosmic Purple to Electric Violet, or white to Royal Violet on dark.
- **Right-side icons**: account person icon + cart bag icon, both stroke style at ~24px.

### Decorative Elements

**Confetti Scatter** — Mini illustrated motifs (sparkles ✦/✨, rainbow arcs, cereal pieces, mini bowls, candies) scattered across hero and promo panels. Full secondary rainbow palette. Function: joy texture that fills negative space without competing with type.

**Holographic Text Fill** — Multi-stop rainbow gradient applied to display headlines via `background-clip: text`. Sequence: hot pink → orange → yellow → green → cyan → purple. Used for celebration headers — reads as foil-sticker / 70s lenticular print energy.

**Cartoon Illustration** — Character work (wizards, bunnies, anthropomorphic spoons, cosmic creatures riding cereal pieces). Thick outlines, flat fills, full secondary palette. Used on 404, about, and occasional promo panels. Saturday-morning cartoon voice — warm, weird, never corporate.

## 5. Layout Principles

### Spacing System
- Base unit: 10px (with frequent 5px sub-unit for tight chrome)
- Scale: 5px, 10px, 15px, 20px, 22px, 30px, 40px, 50px, 60px, 100px
- Most-used values: 20px (68 occurrences), 10px (45), 30px (25)
- Notable: The scale leans toward 10px multiples rather than the 8px convention. Sections breathe with 60–100px vertical rhythm; chrome packs tight at 5–22px.

### Grid & Container
- Max content width: ~1200–1400px depending on section
- Hero: full-bleed purple background, content centered with two-column text+product layout
- Collection grid: 3–4 product columns on desktop with `25px 25px 25px 0px` cards
- Promo panels: 1-up full-width gradient bars, occasionally 2-up split (text left, illustration right)
- Generous gutter: 20–30px between cards, 30–60px between sections

### Whitespace Philosophy
- **Joyful density**: Cards, illustrations, and confetti fill space deliberately — Magic Spoon doesn't fear visual noise the way minimalist brands do
- **Saturation over restraint**: Where minimalist sites use whitespace to communicate luxury, Magic Spoon uses color and decoration to communicate fun — but with careful section spacing (60–100px) so the page doesn't feel cluttered
- **Color-block pacing**: The page reads as a sequence of saturated panels — purple hero → magenta promo bar → lavender product grid → purple footer. Whitespace happens between panels, not inside them.

### Border Radius Scale
- Sharp (0px): Almost never — only full-bleed banner strips
- Card (10–15px): Search overlays, tight UI containers
- Standard (20–25px): Cards, content panels, hero containers
- Asymmetric (`25px 25px 25px 0px`): The signature card shape — three rounded corners, one squared. Counted 24 times in extracted CSS.
- Pill (28–50px): All buttons, all input fields, badge tags
- Circle (50% / 100%): Pagination dots, round badges, avatar crops

## 6. Depth & Elevation

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | No shadow | Page canvas, color-block sections, body text |
| Inset Stroke (Level 1) | `rgb(255, 255, 255) 0px 0px 0px 2px inset` | Ghost button outlines, white-stroke pill borders |
| Soft Lift (Level 2) | `rgba(0, 0, 0, 0.08) 0px 15px 50px 0px` | Product cards on lavender backgrounds |
| Card Elevation (Level 3) | `rgba(0, 0, 0, 0.1) 0px 20px 60px 0px` | Featured CTA panels, modal overlays |
| Tight Drop (Level 4) | `rgba(0, 0, 0, 0.5) 0px 1px 4px 0px` | Sticker tags floating on cards (high-contrast lift) |

**Shadow Philosophy**: Magic Spoon uses depth sparingly and atmospherically — soft, large-radius, low-opacity drops that lift cards off the lavender canvas without competing with the saturated color blocks. The signature elevation is the `2px inset white` stroke on ghost buttons — not a shadow at all but a clean outline that reads as raised when paired with the cosmic purple ground. Where Cape stamps with hard offset shadows, Magic Spoon floats with diffuse atmospheric blur.

### Decorative Depth
- Inset white strokes (`2px inset`) carry the ghost-button language — clean outline, no fill
- Soft drop shadows (15–60px blur, 0.08–0.10 opacity) lift product cards just enough
- Sticker tags occasionally use a tighter drop (`0px 1px 4px`) to read as physically applied
- No hard offset shadows, no neumorphic insets — the system stays soft and atmospheric

## 7. Do's and Don'ts

### Do
- Use Poppins weight 700–900 for all display headlines — joyful weight is the brand voice
- Apply Cosmic Purple (`#3f0791`) as the dominant ground color — saturate, don't pastel
- Use white pill buttons (`50px` radius) with purple text on dark sections
- Apply the signature asymmetric card radius (`25px 25px 25px 0px`)
- Use uppercase + `0.8px` letter-spacing for nav, buttons, and badges
- Layer secondary accents (hot pink, yellow, cyan) for celebration moments
- Scatter sparkle/confetti motifs across hero and promo panels
- Use multi-stop gradients (pink → cyan → yellow) for hero banners and section transitions
- Pair Cosmic Purple text with Sunshine Yellow sticker tags for promo emphasis
- Use Mabry Pro 700 for editorial accent moments where Poppins would feel too commercial

### Don't
- Don't use weight 300–400 for display — lightweight type reads off-brand
- Don't use pure black text — body copy is Cosmic Purple or Soft Black (`#232323`)
- Don't use 0px-radius rectangles for cards — asymmetric pill-corner is the signature
- Don't use hard offset shadows — depth is soft and atmospheric, not stamped
- Don't use Cosmic Purple alone — pair it with at least one secondary accent
- Don't dial down the saturation — pastels break the Saturday-morning energy
- Don't use sentence-case for buttons or nav — uppercase chrome is the rule
- Don't tighten letter-spacing on uppercase labels — `0.72–0.9px` positive tracking
- Don't replace illustrations with stock photography — cartoon character work is the voice
- Don't centre everything — asymmetric card corners and offset hero compositions are the brand

## 8. Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile Small | <375px | Single-column, hero type drops to 36–48px |
| Mobile | 375–640px | Stacked cards, 48–60px hero, full-width pill CTAs |
| Tablet | 641–960px | 2-column product grid, 60–72px hero |
| Desktop | 961–1200px | 3-column product grid, 80–90px hero |
| Large Desktop | 1201–1440px | 4-column collection grids, max type scale (90px hero) |
| XL Desktop | ≥1441px | Container caps at 1400px, content centers with margin |

The dembrandt extraction surfaces an enormous breakpoint inventory (~75 distinct values from 340px to 3000px) — typical of a Shopify theme accumulating responsive overrides. The functional cluster is the standard six tiers above.

### Touch Targets
- Primary pill CTAs: ~50px tall (`22px 51px` padding) — well above 44px minimum
- Nav links: 18–20px text with generous click area on mobile dropdown
- Pagination dots: 12–16px with 24px+ tap zone

### Collapsing Strategy
- **Nav**: Horizontal collapses to hamburger; full-screen drawer with same uppercase Poppins 700 styling
- **Hero**: 90px → 60px → 48px → 36px progressive scaling, weight 900 maintained throughout
- **Product grid**: 4-column → 3 → 2 → 1 collapse with consistent `25px 25px 25px 0px` card radius
- **Bundle Builder panel**: Side-by-side hot-pink panel + product grid stacks vertically on tablet
- **Section spacing**: 100px+ desktop → 40–60px mobile

### Image Behavior
- Cereal box product shots maintain aspect ratio across breakpoints — never cropped
- Hero illustrations scale uniformly without art direction changes
- Wordmark scales but never becomes icon-only — the stacked "MAGIC SPOON" type IS the logo

## 9. Agent Prompt Guide

### Quick Color Reference
- Primary Background: Cosmic Purple (`#3f0791`)
- Primary Button (on purple): Pure White (`#ffffff`) fill, Royal Violet (`#4a00c4`) text
- Primary Button (on light): Cosmic Purple (`#3f0791`) fill, White text
- Hot Promo: Hot Magenta (`#ec1f8e`)
- Sticker Yellow: Sunshine Yellow (`#fbca10`)
- Hover Purple: Electric Violet (`#5b00ed`)
- Light Page Canvas: Lavender Mist (`#e1d4f7`)
- Cosmic Sweep Gradient: `linear-gradient(90deg, #ec1f8e 0%, #5b1bed 45%, #00d4ff 100%)`
- Inset Outline: `rgb(255, 255, 255) 0px 0px 0px 2px inset`
- Card Shadow: `rgba(0, 0, 0, 0.08) 0px 15px 50px 0px`

### Example Component Prompts
- "Create a hero on Cosmic Purple (`#3f0791`) with a 90px Poppins weight 900 white headline at line-height 1.00. Add a 22px Poppins 400 white subhead. Primary CTA: white pill (`50px` radius), 22px Poppins 900 uppercase Royal Violet (`#4a00c4`) text, padding `22px 51px`, hover Electric Violet (`#5b00ed`) at scale 1.05."
- "Design a product card with `25px 25px 25px 0px` asymmetric radius (one squared corner — the signature shape), white background, soft shadow `rgba(0, 0, 0, 0.08) 0px 15px 50px 0px`. Title 28px Poppins 700, price 18px Poppins 700 Cosmic Purple. Bottom CTA: full-width white pill with purple `SHOP NOW` text at 18px Poppins 700 uppercase, 0.9px tracking."
- "Build a celebration panel on Hot Magenta (`#ec1f8e`) with `25px` corners. White headline at 48px Poppins 900 uppercase + scattered confetti motifs (sparkles, mini cereal) in cyan/yellow/white. CTA: white pill with magenta text, `50px` radius, `22px 51px` padding."
- "Create a top promo bar — full-width Hot Magenta (`#ec1f8e`) strip, ~40px tall, centered white Poppins 500 uppercase 14px text with sparkle emoji prefix and inline `SHOP NOW` underline link."
- "Build a ghost stroke button — transparent fill, white text, `28px` radius, `2px inset white` outline. 20px Poppins 700 uppercase, `0.8px` letter-spacing, padding `0px 30px`. Hover: fills Electric Violet (`#5b00ed`)."

### Iteration Guide
1. Default to Poppins weight 700–900 for all display — joyful weight is non-negotiable
2. Cosmic Purple (`#3f0791`) is the canvas — pair with at least one secondary accent per page
3. White pills (`50px` radius) on purple backgrounds are the primary CTA — purple text inside
4. Use the asymmetric card radius (`25px 25px 25px 0px`) for all product and content cards
5. Uppercase + `0.8px` letter-spacing for buttons, nav, badges — never sentence-case chrome
6. Layer confetti motifs (sparkles, mini cereal, rainbows) across hero and promo panels
7. Multi-stop gradients (pink → cyan → yellow) signal celebration — use for hero banners and section transitions
8. Soft atmospheric shadows (`0.08` opacity, 50px blur) for card lift — never hard offset stamps
9. Mabry Pro 700 is the editorial accent — use sparingly for about/founder moments
10. When in doubt, saturate further — Magic Spoon earns its volume through joyful commitment, not restraint
