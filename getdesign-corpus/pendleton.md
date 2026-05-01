---
slug: pendleton
name: Pendleton
url: https://www.pendleton-usa.com
domain: pendleton-usa.com
category: Retail
styles: [Warm, Editorial, Tactile]
tagline: "Modesto slab display over Mukta body, deep navy hero block, ink-grey type on paper-cream surfaces, zero-radius rectangles."
fonts: [Modesto-Lite, Modesto-Open, Mukta]
primary_color: "#152a48"
---

# Design System Inspired by Pendleton

> Modesto slab display over Mukta body, deep navy hero block, ink-grey type on paper-cream surfaces, zero-radius rectangles.

## 1. Visual Theme & Atmosphere

Pendleton's website is a heritage Pacific Northwest mill catalogue rendered as a digital storefront. The page sits on crisp white (`#ffffff`) and a subtle paper-cream secondary surface (`#f1ebdf`), with deep ink-grey type (`#333333`) carrying every line of body copy and a single deep-navy block (`#152a48`) anchoring the hero and signup moments. There is no ornament here — the brand's actual ornament is the textile, and the website knows it. Where every other heritage retailer reaches for distressed textures or vintage borders, Pendleton lets the wool do the decoration: full-bleed product photography of charcoal blanket coats and Nordic-knit jacquards sits inside flat rectangular frames with `0px` border-radius, separated by hairline 1px rules. The chrome is so quiet it functions as a frame around the cloth.

The signature move is the **Modesto / Mukta typographic contract**. Modesto-Lite (a humanist slab serif at weight 300) and Modesto-Open (an open-counter editorial slab) handle every display moment — the wordmark, section openers, "Shop Wool" callouts, hero titles. Mukta (a humanist sans-serif workhorse) handles every body line, every navigation item, every button label, every price. The slab carries the Western mill heritage, the sans handles the transactional surface, and they never trade roles. Modesto runs at sizes from 22–48px with a generous `2px` letter-spacing that pulls the slabs apart into legible plaque type. Mukta handles 12–32px at weights 300–500, with sentence-case body and uppercase-with-tracking on buttons. The two faces talk to each other across every page like a stamped wooden sign sharing space with a packing slip.

What separates Pendleton from every other heritage retailer is **rectangular discipline**. Buttons have `0px` radius. Cards have `0px` radius. Inputs have `0px` radius. The only rounded element in the entire system is a 15px-radius signup pill that lives inside the deep-navy hero block — and it's the exception that proves the rule. No gradients live on brand chrome; the only chromatic depth comes from the navy hero (`#152a48`), the cream secondary (`#f1ebdf`), an occasional brick-red link tone (`#9c564b`), and a 5px gold border (`#cfb776`) that surrounds editorial photography on the heritage pages. The aesthetic is letterpress catalogue meets blanket-mill receipt — confident Americana without the costume.

**Key Characteristics:**
- Crisp white canvas (`#ffffff`) with paper-cream secondary surface (`#f1ebdf`) for editorial alternation
- Ink-grey body type (`#333333`) — no pure black anywhere; softened for long-form reading
- Modesto slab display (Lite + Open variants) at weight 300–400 with `2px` letter-spacing
- Mukta humanist sans for every body, button, nav link, and caption
- Deep navy hero block (`#152a48`) — the single chromatic anchor for signup and hero CTAs
- `0px` border-radius on all primary buttons, cards, and inputs — rectangular by conviction
- 1px hairline borders (`#333` solid) carry all structural separation; no shadows on primary chrome
- Brick-red link accent (`#9c564b`) for editorial Americana moments — vintage saddle-leather feel
- Gold mat border (`5px solid #cfb776`) frames heritage editorial photography
- Buttons UPPERCASE with `1px` letter-spacing in Mukta-Medium — receipt-stamp legibility
- 539px content column for newsletter / editorial moments — magazine-standard line measure

## 2. Color Palette & Roles

### Primary
- **Pendleton Ink** (`#333333`): Primary text color across body, headings, navigation, and the wordmark. Used 906 times across the page — the workhorse neutral. Not pure black; softened for catalogue legibility.
- **Pure White** (`#ffffff`): Default canvas, button text on dark surfaces, inverted text on the navy hero.
- **Paper Cream** (`#f1ebdf`): Secondary surface for alternate sections, secondary buttons, callout panels. Reads as an old packing slip.

### Brand Accent
- **Pendleton Navy** (`#152a48`): The chromatic signature — appears on the homepage signup hero, primary CTA hero blocks, and feature panels. The single saturated colour the system permits, and it carries the brand's institutional weight.
- **Deep Ink** (`#051c2c`): Editorial link colour and dark feature accents — a near-black with a navy undertone. Used for editorial captions and museum-style attribution lines.
- **Saddle Brick** (`#9c564b`): Vintage Americana link colour — appears on heritage editorial pages, bound-book references, and historical features. The single warm chromatic note in the otherwise institutional palette.
- **Heritage Gold** (`#cfb776`): A 5px mat border colour that frames editorial photography on heritage and lookbook pages. Reads as gilt frame around portraiture.

### Neutrals & Text
- **Ink** (`#333333`): All headings, body, navigation links — `text-decoration: underline` on default link state, removed on hover.
- **Mid Grey** (`#565656`): Hover state for ink links — a softening lift.
- **Hairline Mid** (`#757575`): SVG icon stroke colour, secondary metadata.
- **Disabled / Stroke** (`#979797`): Form input borders at rest, disabled state text.
- **Pale Surface** (`#f3f3f3`): Tinted alternate panel for filter chips and inactive tabs — half-step lighter than cream.
- **Hairline Border** (`#e0e0e0`): 1px footer dividers, menu rule strokes — barely-there structure.

### Surface & Borders
- **Page Surface** (`#ffffff`): Default canvas.
- **Cream Surface** (`#f1ebdf`): Secondary panel, secondary button background, signup callout.
- **Tinted Surface** (`#f3f3f3`): Filter and chip background.
- **Solid Border** (`1px solid #333333`): Primary structural border — 12 confirmed uses across buttons and cards.
- **Hairline Border** (`1px solid #e0e0e0`): Menu and footer dividers, rule strokes.
- **Heavy Form Border** (`3px solid #152a48`): The newsletter input border — unusually thick to read as institutional plaque.
- **Gold Mat Border** (`5px solid #cfb776`): Editorial photo mat — heritage-page exclusive.

### Shadow System
- **Button Hover Inset** (`box-shadow: rgb(255, 255, 255) 0px 0px 0px 3px inset`): The signature button-hover treatment — a 3px inset white ring that fills the button with cream and inverts the text colour. No drop shadow.
- **Active Inset Wash** (`box-shadow: rgb(255, 255, 255) 0px 0px 0px 30px inset`): Pressed-state full white wash — the button "fills" rather than depresses.
- **Callout Drop** (`rgba(0, 0, 0, 0.35) 0px 3px 15px 0px`): Reserved for floating banners and modal overlays.
- **Footer Hairline** (`rgb(224, 224, 224) 0px -1px 0px 0px`): Top-edge hairline used as a structural shadow on footer accordion buttons.

### Gradient System
- Pendleton is **gradient-free in core brand applications**. Surface colour transitions are solid: white → cream → navy as the chapter rhythm. The only gradient ever observed is the standard scrim used to anchor white type over photography — never a brand decoration.

## 3. Typography Rules

### Font Family
- **Display Slab**: `Modesto-Lite`, weight 300, fallback `Helvetica, Arial`. The condensed slab serif handling section openers and editorial headlines. Carries the heritage mill voice.
- **Display Slab Open**: `Modesto-Open`, weight 300–400, fallback `Helvetica, Arial`. The open-counter variant — used for inverse type on dark navy and large display moments where the negative space inside letters becomes a graphic element.
- **Body / UI / Headlines Sans**: `Mukta`, weights 300/400/500/600/700, fallback `Helvetica, Arial`. The humanist sans workhorse — every body paragraph, every button, every navigation link.
- **OpenType Features**: Standard ligatures only. No stylistic alternates, no opticals — the typefaces' default character set carries the work.

*Note: Modesto is a commercial typeface (Parkinson Type Design); Mukta is open-source from EkType (Indian Type Foundry). For external implementations, `Rockwell Light` or `Roboto Slab Light` substitute for Modesto-Lite; `Mukta` itself is freely available via Google Fonts.*

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Transform | Notes |
|------|------|------|--------|-------------|----------------|-----------|-------|
| Display Hero (Slab) | Modesto-Lite | 48px (3.00rem) | 300 | 0.71 | 2px | none | Section openers — tight line-height creates plaque-like blocks |
| Display Hero (Open) | Modesto-Open | 48px (3.00rem) | 300 | 1.20 | 1px | none | Open-counter variant for navy-hero inverse type |
| Section Heading (Sans) | Mukta | 64px (4.00rem) | 400 | 1.25 | normal | none | Page-level headline on landing pages |
| Sub-Display Slab | Modesto-Open | 28px (1.75rem) | 400 | 1.20 | 1px | none | Sub-hero serif heads |
| Sub-Display Slab Tight | Modesto-Lite | 28px (1.75rem) | 300 | 1.21 | 2px | none | Sub-hero alternate, tighter feel |
| Editorial Slab | Modesto-Lite | 26px (1.63rem) | 300 | 1.31 | 2px | none | Long-form editorial heads |
| Section Heading (Sans Heavy) | Mukta | 32px (2.00rem) | 500 | 0.72 | normal | none | Bold sans block — dense graphic title |
| H2 Sans | Mukta | 24px (1.50rem) | 500 | 1.25 | 2px | none | Card titles, secondary section heads |
| H3 Sans | Mukta | 22px (1.38rem) | 500 | 1.05 | 1px | none | Tertiary heading |
| Body Lead | Mukta | 20px (1.25rem) | 300 | 1.50 | 2px | none | Lead paragraph, intro copy |
| Body | Mukta | 18px (1.13rem) | 300 | 1.28–1.67 | 1–2px | none | Standard body text |
| Body Default | Mukta | 16px (1.00rem) | 300 | 1.44–1.63 | 1px | none | Default body, footer copy |
| Button (Sans) | Mukta | 16px (1.00rem) | 500 | 1.50 | 1px | uppercase | Primary button label |
| Button Small | Mukta | 14px (0.88rem) | 500 | 1.57 | 1px | uppercase | Compact tile / filter button |
| Caption | Mukta | 14px (0.88rem) | 300 | 1.64 | 1px | none | Image captions, fine print |
| Micro Link | Mukta | 12px (0.75rem) | 500 | 1.83 | 1px | uppercase | Footer category links, breadcrumbs |

### Principles
- **Two-typeface contract, three operative voices**: Modesto-Lite for tight slab display, Modesto-Open for open-counter heroes, Mukta for everything sans. The slab + sans pairing is the brand's typographic signature and never wavers.
- **Generous letter-spacing on slab display**: `2px` letter-spacing on Modesto sizes 22px+ creates the stamped-plaque feel — letters pulled apart for legibility at distance.
- **`1px` letter-spacing as default for body and links**: Mukta runs at `1px` tracking across nearly every body and link role. This produces the slightly wide, institutional reading rhythm.
- **Sentence case for body, UPPERCASE for buttons**: Buttons and category labels run uppercase with `1px` letter-spacing in Mukta-Medium. Body and headlines stay sentence case.
- **Light weights as the body voice**: Mukta-Light (300) is the most-used body weight, paired with Medium (500) for buttons and emphasis. The system rarely uses 700 except for occasional bold meta labels.
- **Tight slab line-height**: Modesto-Lite at 48px runs `0.71` line-height — display blocks are vertically compressed, reading as horizontal banners rather than paragraphs.

## 4. Component Stylings

### Buttons

**Primary Ink**
- Background: Pendleton Ink (`#333333`)
- Text: Pure White (`#ffffff`)
- Padding: `0px 40px` horizontal, height carried by `1.50` line-height on `14px` text
- Radius: `0px`
- Border: `1px solid #333333`
- Shadow: `none` at rest
- Font: 14px Mukta weight 500, UPPERCASE, `1px` letter-spacing
- Hover: background goes transparent, text drops to `rgba(255, 255, 255, 0.46)`, `box-shadow: rgb(255, 255, 255) 0px 0px 0px 3px inset` adds a 3px inset cream ring
- Active: background `#333` again, full inset white wash (`box-shadow: rgb(255, 255, 255) 0px 0px 0px 30px inset`)
- Use: Primary CTA — "Shop Now", "Add to Bag", "Continue"

**Secondary Cream**
- Background: Paper Cream (`#f1ebdf`)
- Text: Pendleton Ink (`#333333`)
- Padding: `0px 40px`
- Radius: `0px`
- Border: `1px solid #f1ebdf`
- Font: 14px Mukta weight 500, UPPERCASE
- Hover: same inset cream-ring treatment as primary
- Use: Secondary CTA on cream-section pages

**Outline Ghost**
- Background: `transparent`
- Text: Pendleton Ink (`#333333`)
- Padding: `0px 40px`
- Radius: `0px`
- Border: `1px solid #333333`
- Font: 14px Mukta weight 500, UPPERCASE
- Hover: text fades to `rgba(255, 255, 255, 0.46)`, transform `translate(0.5em, -50%)`
- Use: Newsletter submit, "Read More", secondary inline actions

**Inverse Outline (on photography)**
- Background: `transparent`
- Text: Pure White (`#ffffff`)
- Padding: `0px 16px`
- Radius: `0px`
- Border: `1px solid #ffffff`
- Font: 12px Mukta weight 500, UPPERCASE
- Use: CTAs over carousel photography — "Shop the Collection"

**Navy Signup Pill (the exception)**
- Background: Pendleton Navy (`#152a48`)
- Text: Pendleton Navy (label sits inside the panel)
- Padding: `25px`
- Radius: `15px` — the only meaningful radius in the system, reserved for the signup hero
- Font: 32px Mukta weight 500
- Use: Email signup hero on the homepage — the brand's single departure from rectangular discipline

### Cards & Containers

**Product Tile**
- Background: Pure White (`#ffffff`)
- Border: `0px` default, `1px solid #e0e0e0` separator-only on grids
- Radius: `0px`
- Shadow: `none`
- Internal padding: `20px–32px` — generous editorial padding around photography
- Image: full-bleed within tile, no inset, no caption box

**Cream Editorial Panel**
- Background: Paper Cream (`#f1ebdf`)
- Border: none
- Radius: `0px`
- Padding: `32–60px` — magazine-spread generous padding
- Use: Heritage editorial blocks, "Our Story" panels, lookbook callouts

**Navy Hero Block**
- Background: Pendleton Navy (`#152a48`)
- Text: White or Cream
- Border: none
- Radius: `0px`
- Padding: `60–100px` vertical
- Use: Email signup hero, "Become a Member" CTAs, feature article opener

**Gold-Matted Editorial Frame**
- Border: `5px solid #cfb776`
- Radius: `0px`
- Inside: full-bleed editorial photography with caption below
- Use: Heritage-page imagery — "100 Years of Pendleton", museum-style features

### Badges / Tags / Pills

**Sale Tag**
- Background: `transparent`
- Text: Pendleton Ink (`#333333`)
- Padding: `4px 8px`
- Radius: `0px`
- Font: 12px Mukta weight 500, `1px` letter-spacing
- Use: Sale price callout, "Limited Edition" markers — typography only, no chip

**Filter Chip**
- Background: `#f3f3f3`
- Text: Ink (`#333333`)
- Padding: `12px 10px`
- Radius: `2px` — the only mid-range radius in the system, reserved for filter chips
- Border: `1px solid #333333`
- Font: 13.008px Mukta weight 600
- Use: Size, colour, category filter chips on PLP pages

### Inputs & Forms

**Standard Email**
- Background: `transparent`
- Border: `0px 0px 1px solid #333333` — bottom-border only, sketchbook-style
- Radius: `0px`
- Padding: `0px`
- Font: 16px Mukta weight 300, color `#333333`
- Focus: full `1px solid #000` border replaces underline; cream wash inside via `box-shadow: rgb(255, 255, 255) 0px 0px 0px 30px inset`

**Newsletter Heavy**
- Background: `transparent`
- Border: `3px solid #152a48` — institutional thick navy border
- Radius: `0px`
- Padding: `0px 0px 0px 14px`
- Font: Mukta weight 300, color `#152a48`
- Use: Newsletter signup inside the navy hero — heavy border reads as plaque

### Navigation

- Top utility strip: white background, 12px Mukta UPPERCASE links — "Stores", "Customer Service" left; "Account", "Wishlist", "Bag" right
- Main nav: white background with the Pendleton wordmark (Modesto-Open) centered at ~44px height, never resized below 32px on mobile
- Primary nav links: 16px Mukta weight 500 UPPERCASE, `1px` letter-spacing, Ink colour (`#333333`)
- Hover: subtle underline appears below the link — no colour change
- Mega-menu: drops as full-width white panel with category columns and secondary editorial imagery on the right
- Sticky behaviour: full nav stack remains fixed on scroll; cream tinted background fades in at scroll position 200px

### Decorative Elements

**Hairline Rules**
- `1px solid #e0e0e0` horizontal dividers between footer columns and menu sections
- The system's primary structural device — Pendleton trusts hairlines over shadow

**Plaid / Jacquard Photography**
- Pendleton's actual visual ornament is the textile itself — every blanket-coat photograph and product hero is the page's decoration. The chrome stays mute so the wool can carry the page.

**Cream-Wash Hover**
- The signature interactive metaphor: every primary button has a `box-shadow: rgb(255, 255, 255) 0px 0px 0px 30px inset` active state that fills the button with cream from inside. No depress, no lift — just a wash.

## 5. Layout Principles

### Spacing System
- Base unit: `4px` (with strong reliance on `8` and `20`)
- Scale: `1px, 4px, 8px, 10px, 12px, 14px, 15px, 20px, 24px, 28px, 30px, 32px, 40px, 50px, 60px`
- Notable: `4px` is the most-used spacing value (63 instances), followed by `20px` (48) and `8px` (43). The system has unusual mid-range increments (`13px`, `15px`, `25px`) that come from a Sass tokenization tied to a 16px-rooted scale rather than a strict 8px ladder. Section padding lives at `32–60px`, and the editorial column maxes at `539.375px` — the magazine-standard line measure for long-form reading.

### Grid & Container
- Max content width: `1280px–1440px` for product grids; `539px` reading column for editorial / signup
- Hero: full-bleed product photography or full-bleed navy block — 60–100px vertical padding
- Section content: 4-column footer (`width: 25%` per column), 3-column or 4-column product grids on desktop
- Primary content alternates between cream and white panels for chapter-like rhythm

### Whitespace Philosophy
- **Magazine pacing**: Each section gets generous vertical padding — 60–100px between major content blocks. Pages feel like printed catalogue spreads.
- **Cream / white alternation as section break**: Instead of dividers or shadows, Pendleton swaps surface colour (`#ffffff` → `#f1ebdf`) to chapter the page.
- **Editorial column air**: Reading column at 539px max — narrow, magazine-style for long-form heritage features. Body type at 18–20px stays generous.
- **Navy as gravitational anchor**: The navy block (`#152a48`) appears once or twice per page max — when it shows up, it carries weight.

### Border Radius Scale
- Sharp (`0px`): Default for every rectangular element — buttons, cards, inputs, sale tags, image containers. Rectangular by conviction.
- Slight (`2px`): Reserved exclusively for filter chips on PLP pages.
- Slight Plus (`3px`): One-off micro-radius for cookie banner CTAs (third-party origin).
- Editorial (`15px`): The signup hero pill — the system's single intentional rounded element.
- Pill (`100px`): Cookie-banner buttons (third-party origin, not first-party brand).
- No mid-range: Pendleton does not use 4–12px radii. The system reads either letterpress-rectangular or fully editorial.

## 6. Depth & Elevation

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | `box-shadow: none` | Default state for nearly every surface — buttons, cards, hero blocks |
| Hairline (Level 1) | `1px solid #333333` or `1px solid #e0e0e0` | Card edges, dividers, button outlines |
| Inset Cream Ring (Level 2) | `box-shadow: rgb(255, 255, 255) 0px 0px 0px 3px inset` | Button hover state |
| Inset Cream Wash (Level 3) | `box-shadow: rgb(255, 255, 255) 0px 0px 0px 30px inset` | Button active state — full wash |
| Footer Hairline (Level 4) | `box-shadow: rgb(224, 224, 224) 0px -1px 0px 0px` | Top-edge structural hairline on accordion buttons |
| Modal Drop (Level 5) | `box-shadow: rgba(0, 0, 0, 0.35) 0px 3px 15px 0px` | Reserved for floating banners and modal overlays |
| Heavy Drop (rare) | `box-shadow: rgba(51, 51, 51, 0.4) 0px 540px 0px 540px` | Carousel-control viewport-darkening overlay (8 uses) |
| Focus Outline | `outline: 0px` + `box-shadow: rgb(255, 255, 255) 0px 0px 0px 30px inset` | Button focus state |

**Shadow Philosophy**: Pendleton's elevation is letterpress, not architectural. The default state of every surface is flat — the page reads as a printed catalogue, not a UI. Where elevation needs to communicate, the system uses 1px hairline borders rather than blurred shadows. The signature interactive metaphor is the **inset cream wash**: buttons fill from inside on hover and active, rather than lifting off the page. This is the antithesis of Material Design's "lift" — Pendleton's buttons stay rooted on the page like wooden type blocks pressed into paper. Drop shadows exist only on modal overlays and floating banners, never on primary chrome.

### Decorative Depth
- Hairline rules do double duty as borders and section dividers
- Cream / white alternation is the primary "elevation" — moving from white onto cream reads as turning a catalogue page
- The navy hero (`#152a48`) is the only true tonal shift in the system — it functions as a chapter break

## 7. Do's and Don'ts

### Do
- Use `#ffffff` (white) as the page canvas with `#f1ebdf` (cream) as the alternating secondary surface
- Set all body and heading text in Pendleton Ink (`#333333`) — softer than pure black, easier on long-form reading
- Pair Modesto-Lite (slab display) with Mukta (sans body) — every screen should show this contrast
- Apply `2px` letter-spacing on Modesto display sizes 22px+ for the stamped-plaque feel
- Use `1px` letter-spacing on Mukta body and links for the institutional reading rhythm
- Set buttons UPPERCASE with `1px` letter-spacing in Mukta-Medium (500)
- Keep border-radius at `0px` for every primary button, card, and input — rectangular is the brand's tactile signature
- Use 1px hairlines (`#e0e0e0` or `#333333`) instead of shadows for separation
- Use the inset cream-wash hover (`box-shadow: rgb(255, 255, 255) 0px 0px 0px 30px inset`) for primary button interactivity
- Reserve Pendleton Navy (`#152a48`) for one or two anchor moments per page — signup hero, hero feature
- Frame heritage editorial photography with a `5px solid #cfb776` gold mat border
- Let the textile photography carry the visual ornament; the chrome stays muted

### Don't
- Don't use pure black (`#000000`) — Pendleton Ink (`#333333`) is the workhorse neutral
- Don't add drop shadows to primary buttons or cards — flat is the brand
- Don't use rounded corners on buttons or inputs — `0px` radius is the rectangular signature
- Don't introduce gradients on brand chrome — solid colour fills only
- Don't use sans-serif for display heads — Modesto slab carries every editorial moment
- Don't tighten Mukta letter-spacing below `1px` — the institutional rhythm depends on the wide tracking
- Don't crowd display line-height above `1.20` on Modesto — the slab needs vertical compression
- Don't use Mukta-Bold (700) as the body voice — Light (300) is the default; Medium (500) is for emphasis
- Don't replace the navy (`#152a48`) with a softer or brighter blue — the deep institutional note is what carries the page
- Don't use the gold mat border (`#cfb776`) on every photo — it's reserved for heritage editorial moments only
- Don't decorate with vintage textures, distressed borders, or western iconography — the textile is the decoration

## 8. Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile Small | <426px | Single-column, hamburger nav, hero photography full-bleed |
| Mobile | 426–769px | Single-column, 2-up product grids on mid-mobile, hamburger nav |
| Tablet | 769–1024px | 2-up to 3-up product grids, full nav appears at upper end |
| Desktop | 1024–1280px | Full horizontal nav, 4-column footer, 3-up product grids |
| Large Desktop | ≥1280px | Maximum container width 1440px, 4-up product grids, full editorial spacing |

### Touch Targets
- Primary buttons: `0px 40px` horizontal padding produces ~48px tap height with the 14px line-height — comfortable on mobile
- Nav links: 12–16px tap padding
- Filter chips: `12px 10px` padding produces 40–44px tap height
- Footer accordion buttons: `14px 20px 14px 0px` — generous tap zone with hairline top-border

### Collapsing Strategy
- **Nav**: Horizontal nav collapses to hamburger drawer at <896px; full-screen overlay on open with white background
- **Hero**: Centred composition stacks tighter on mobile; navy hero block compresses padding from 100px → 48px
- **Footer**: 4-column desktop nav collapses to vertical accordion on mobile with `+`/`-` indicators
- **Product grids**: 4-up desktop → 3-up tablet → 2-up mobile, gutters scale proportionally
- **Editorial column**: Maintains 539px max even on large desktop — the editorial line measure is sacred
- **Display type**: Modesto 48px → 32px → 28px progressive scaling, letter-spacing held at `2px` throughout

### Image Behavior
- Product photography fills viewport edge-to-edge on mobile hero; on desktop sits inside the 1440px container with margin
- Editorial / heritage photography maintains the 5px gold mat border at all breakpoints
- The Pendleton wordmark scales but never simplifies to an icon — always full Modesto-Open type
- Carousel controls maintain their 1px white outline on photography across all viewports

## 9. Agent Prompt Guide

### Quick Color Reference
- Page Background: Pure White (`#ffffff`)
- Secondary Surface: Paper Cream (`#f1ebdf`)
- Primary Text / Headlines: Pendleton Ink (`#333333`)
- Brand Anchor / Hero Block: Pendleton Navy (`#152a48`)
- Editorial Link: Saddle Brick (`#9c564b`)
- Heritage Frame Border: Heritage Gold (`#cfb776`)
- Hairline Border: `#e0e0e0`
- Solid Border: `#333333`
- Tinted Surface: `#f3f3f3`
- Button Hover Inset: `box-shadow: rgb(255, 255, 255) 0px 0px 0px 3px inset`

### Quick Type Reference
- Display slab: Modesto-Lite or Modesto-Open at 28–48px / weight 300–400 / letter-spacing 2px
- Body: Mukta at 14–18px / weight 300 / letter-spacing 1px
- Button: Mukta at 14–16px / weight 500 / letter-spacing 1px / UPPERCASE
- Caption: Mukta at 12–14px / weight 300 / letter-spacing 1px

### Example Component Prompts
- "Create a Pendleton-style hero on `#ffffff` with a 48px Modesto-Lite weight 300 headline, line-height 0.71, letter-spacing 2px, color `#333333`. Sub-deck in Mukta 20px weight 300 line-height 1.50 letter-spacing 2px. Primary CTA: `#333` background, `#fff` text, `0px` radius, `1px solid #333` border, 14px Mukta weight 500 UPPERCASE with `1px` letter-spacing. Hover applies `box-shadow: rgb(255, 255, 255) 0px 0px 0px 3px inset`."
- "Design a navy signup hero on `#152a48` with 32px Mukta weight 500 white headline. Email input: `transparent` bg, `3px solid #152a48` border, `0px` radius, 16px Mukta weight 300 in `#152a48`. Submit button: `#333` bg, `#fff` text, 14px Mukta weight 500 UPPERCASE."
- "Build a product card on `#ffffff`: square photography full-bleed at the top, no border, `0px` radius. Below: 16px Mukta weight 500 UPPERCASE category label in `#333` with `1px` letter-spacing, 18px Mukta weight 400 product name, 16px Mukta weight 500 price."
- "Create an editorial heritage frame: 5px solid `#cfb776` gold mat border around full-bleed photography, with caption below in 14px Mukta weight 300 line-height 1.64 letter-spacing 1px in `#333`."
- "Design a filter chip — `#f3f3f3` bg, `#333` text, `1px solid #333` border, `2px` radius, 13px Mukta weight 600, padding 12px 10px."
- "Build a primary CTA — `#333` background, `#fff` text, `0px` radius, `1px solid #333` border, padding `0px 40px`, 14px Mukta weight 500, UPPERCASE, `1px` letter-spacing. Hover transitions to `transparent` bg with `box-shadow: rgb(255, 255, 255) 0px 0px 0px 3px inset` cream ring."

### Iteration Guide
1. Default to white canvas (`#ffffff`) with cream secondary surface (`#f1ebdf`) — never reach for warm off-white. The cream is for alternation, not the base.
2. Pendleton Ink (`#333333`) replaces black entirely. Use it for every heading, body line, and primary border.
3. Pair Modesto slab display with Mukta sans body on every screen — this is the brand's typographic contract.
4. Letter-spacing rules: `2px` on Modesto display 22px+, `1px` on Mukta body and buttons, normal on small captions.
5. Buttons are rectangles with `0px` radius. The single 15px-radius signup pill in the navy hero is the system's only intentional rounding.
6. UPPERCASE all button labels and category indicators with `1px` letter-spacing in Mukta-Medium.
7. Use the inset cream-wash hover on primary buttons (`box-shadow: rgb(255, 255, 255) 0px 0px 0px 3px inset`) — this is the brand's signature interaction.
8. Reserve Pendleton Navy (`#152a48`) for one anchor block per page — signup hero or feature opener.
9. Use 1px hairlines for separation, not drop shadows. Drop shadows are for modal overlays only.
10. The textile photography is the decoration. Keep chrome muted so the wool can carry the page.
