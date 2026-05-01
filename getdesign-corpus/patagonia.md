# Design System Inspired by Patagonia

## 1. Visual Theme & Atmosphere

Patagonia's website is the digital expression of a 50-year-old outdoor outfitter that has earned the right to act like a magazine, a manifesto, and a catalog at once. The page opens on pure white (`#ffffff`) with edge-to-edge climbing, surfing, and mountain photography — never a studio shot, always a person mid-effort in a real place. The signature blue-mountain wordmark (`#03245c`) sits top-left as a dense, geometric anchor that has barely changed since 1973, and the entire interface defers to it: thin neutral chrome, generous photographic real estate, and copy that reads more like an environmental dispatch than e-commerce.

Where most outdoor brands lean into adventure-marketing tropes (warm earth gradients, badge-heavy chrome, "EXPLORE MORE" overlay scrims), Patagonia chooses the opposite: a quiet white canvas, system-sans typography, and trust that the photography and the writing will carry the brand. The top utility bar runs an activist message — "Earth Is Now Our Only Shareholder" — in 11px white-on-black, treating the corporate position as a permanent header element rather than a campaign. This is the defining move: the activism isn't separate from the commerce, it sits one pixel above it.

The atmospheric distinction is **density of conviction over density of decoration**. Product tiles are unornamented — a square photograph, a product name in 14px, a price, a color count. Stories pages run long-form journalism with full-bleed editorial photography and 18px body copy at generous line-height. The visual system does almost nothing on its own; it exists to frame imagery and prose that have been doing the heavy lifting since before the web existed.

**Key Characteristics:**
- Patagonia Blue wordmark (`#03245c`) — the only persistent color anchor, mountain silhouette + serif-leaning sans wordmark
- Pure white (`#ffffff`) page canvas — uncompromising, gives photography full chromatic range
- Full-bleed photographic heroes — climbers, surfers, fishers, alpinists in real conditions, never studio
- Activist utility bar (`#000000` background, white text, 11px) — environmental copy as permanent chrome
- System sans typography (Helvetica Neue / Arial stack) — chosen for legibility and refusal of trend
- Thin 1px borders, sharp 2–4px radii on buttons, no decorative shadows — chrome stays out of the way
- Editorial copy density on Stories pages — long-form journalism inside a commerce site
- Product photography on plain backgrounds in grid; lifestyle photography full-bleed in hero

## 2. Color Palette & Roles

### Primary
- **Patagonia Blue** (`#03245c`): The brand wordmark and the only saturated color in default chrome. Deep navy-blue with red and green chroma — the mountain silhouette gradient (red peak top, blue body, green base) appears only in the full color logo on key brand surfaces.
- **Pure White** (`#ffffff`): Primary page background. Patagonia commits to white — no warm off-white, no neutral tint. The photography needs the full contrast range.
- **True Black** (`#000000`): The activist utility bar background, primary CTA fill on white surfaces, and body text on the lightest contexts.

### Brand Logo Gradient (decorative only)
- **Mountain Peak Red** (`#cc1f1f`): Top-of-mountain accent in the full color logo.
- **Mountain Body Blue** (`#03245c`): Mid-section of the mountain silhouette.
- **Mountain Base Green** (`#0e7c4a`): Base of the mountain silhouette and occasional environmental-content highlight.
- These three only appear together inside the iconic mountain logo — never as separate UI accents.

### Neutrals & Text
- **Body Text Black** (`#1a1a1a`): Primary running copy and product names — slightly softened from pure black for long-form readability on white.
- **Secondary Text Gray** (`#5c5c5c`): Sub-copy, metadata, breadcrumbs, color counts ("4 colors").
- **Tertiary Gray** (`#8a8a8a`): Disabled states, timestamps, ancillary captions.
- **Hairline Border** (`#e5e5e5`): 1px borders between product cards, table dividers, footer separators.

### Surface & Borders
- **Surface White** (`#ffffff`): Default panel background.
- **Surface Stone** (`#f5f4f1`): A barely-warm neutral used on Stories/editorial pages and certain category landing zones — the closest Patagonia gets to off-white, and it appears sparingly.
- **Surface Black** (`#000000`): Reserved for the activist utility bar and full-bleed dark editorial moments.

### Functional / State
- **Sale Red** (`#b3261e`): Sale prices, markdowns, "WEB SPECIALS" badges. Used only for commerce-state communication.
- **Activist Green** (`#1f7a3a`): "Worn Wear" badges, "Recycled materials" indicators, environmental certifications. Differentiates the activist commerce track from the regular catalog.
- **Link Blue** (`#0050a0`): Inline text links inside body copy — slightly brighter than logo blue for contrast.

### Gradient System
- Patagonia is **gradient-free in UI**. The only gradient in the entire system is inside the corporate mountain logo — a vertical red→blue→green hand-drawn-feeling transition that has been preserved since 1973. UI surfaces, buttons, hero scrims, and cards never use gradient fills.

## 3. Typography Rules

### Font Family
- **Primary**: `Helvetica Neue`, with fallback: `Helvetica`, `Arial`, sans-serif
- **Editorial / Long-form**: Same `Helvetica Neue` — Patagonia does not split into a separate serif for stories, the system stays mono-typeface
- **Logo wordmark**: A custom condensed sans modeled on 1970s climbing-shop signage; not used outside the logo itself
- **OpenType Features**: Standard ligatures, lining numerals on prices

*Note: Helvetica Neue is licensed by Linotype/Monotype. Web-safe substitutes: Inter, Söhne, or Arial Nova all carry the same workmanlike-Swiss tone Patagonia is after. Avoid display-y geometric sans (Avenir, Futura) — they break the catalog feel.*

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Editorial Hero | Helvetica Neue | 64px (4.00rem) | 400 | 1.05 | -0.5px | Stories landing, full-bleed editorial titles |
| Hero Display | Helvetica Neue | 48px (3.00rem) | 400 | 1.10 | -0.4px | "New Arrivals", category landing heads |
| H1 | Helvetica Neue | 36px (2.25rem) | 500 | 1.15 | -0.3px | Page titles, story article heads |
| H2 | Helvetica Neue | 28px (1.75rem) | 500 | 1.20 | -0.2px | Section heads inside categories |
| H3 | Helvetica Neue | 22px (1.375rem) | 500 | 1.25 | -0.1px | Card titles, product spec heads |
| H4 | Helvetica Neue | 18px (1.125rem) | 500 | 1.30 | normal | Sub-section, product name in detail view |
| Body Large | Helvetica Neue | 18px (1.125rem) | 400 | 1.55 | normal | Stories long-form running text |
| Body | Helvetica Neue | 16px (1.00rem) | 400 | 1.50 | normal | Product descriptions, default reading |
| Body Small | Helvetica Neue | 14px (0.875rem) | 400 | 1.45 | normal | Product card name, secondary copy |
| Nav Link | Helvetica Neue | 14px (0.875rem) | 500 | 1.00 | normal | Top navigation categories |
| Button UI | Helvetica Neue | 14px (0.875rem) | 500 | 1.00 | 0.02em | CTA labels, often mixed case |
| Caption | Helvetica Neue | 12px (0.75rem) | 400 | 1.40 | normal | Color counts, metadata, breadcrumbs |
| Activist Bar | Helvetica Neue | 11px (0.6875rem) | 500 | 1.00 | 0.05em | Top utility-bar messaging, often UPPERCASE |

### Principles
- **Workmanlike sans, not display sans**: Patagonia uses Helvetica Neue at functional weights (400 / 500) and refuses display-trend typography. The brand's age earns it the right to look unstylish.
- **Editorial over marketing**: Body copy on stories pages runs at 18px / 1.55 line-height — magazine generosity, not commerce-page tightness. Patagonia treats its writing as the reason you stay.
- **Mostly mixed case**: Buttons, headlines, and product names use sentence or title case. Uppercase is reserved for the activist utility bar and certain badge labels — never for primary CTAs.
- **No bold display headings**: Hero and H1 sit at weight 400, with 500 reserved for H2–H4 and UI. The scale climbs with size, not weight — keeps display type calm even at 64px.
- **Negative tracking only above 22px**: Sub-22px text uses normal letter-spacing for legibility. Display sizes get gentle `-0.2px` to `-0.5px` to keep large type from looking spaced-out.

## 4. Component Stylings

### Buttons

**Primary Black**
- Background: True Black (`#000000`)
- Text: Pure White (`#ffffff`)
- Padding: 12px 24px standard, 14px 32px on hero CTAs
- Radius: `2px` (subtle softening, almost-square)
- Border: `1px solid #000000`
- Shadow: `none` — Patagonia does not use elevation shadows on chrome
- Font: 14px Helvetica Neue weight 500, mixed case, letter-spacing `0.02em`
- Hover: background to `#1a1a1a`, no transform
- Use: Primary CTAs — "Add to Bag", "Shop Now", "Read the Story"

**White Outline (Hero Pill)**
- Background: Pure White (`#ffffff`)
- Text: True Black (`#000000`)
- Padding: 12px 28px
- Radius: `9999px` (full pill)
- Border: `1px solid #ffffff` on dark photography, `1px solid #1a1a1a` on white surfaces
- Font: 14px Helvetica Neue weight 500
- Hover: background fades to `rgba(255, 255, 255, 0.85)` over imagery
- Use: Hero overlay CTA — "Explore", "Shop the Collection" sitting on photography

**Ghost Underlined Link**
- Background: transparent
- Text: True Black (`#000000`) or Patagonia Blue (`#03245c`)
- Border-bottom: `1px solid currentColor`
- Font: 14px Helvetica Neue weight 500
- Padding: 0 (inline)
- Use: Tertiary actions, "Learn more", "View all stories"

**Sale Red**
- Background: Sale Red (`#b3261e`)
- Text: Pure White (`#ffffff`)
- Radius: `2px`
- Use: "Web Specials", flash-sale entry CTAs — only for commerce-state, never for activist content

### Cards & Containers

**Product Card**
- Background: Pure White (`#ffffff`)
- Border: `none` on hover, `1px solid #e5e5e5` only at grid boundaries
- Radius: `0px` for the photograph, `0px` for the wrapper
- Shadow: `none`
- Internal padding: 0 around image, 12px above name, 4px between name and price
- Hover: subtle 1.02× image scale within fixed crop, name underline appears

**Story Card**
- Background: Pure White (`#ffffff`)
- Photograph: full-width, 16:9 or 4:5 crop
- Title below image at 22px weight 500
- Byline / category in 12px gray (`#5c5c5c`)
- Internal padding: 0 around image, 16px around text block
- Use: "Stories" feed entries, journal index

### Badges / Tags / Pills

**Worn Wear Green Badge**
- Background: Activist Green (`#1f7a3a`)
- Text: Pure White (`#ffffff`)
- Padding: 4px 10px
- Radius: `2px`
- Font: 11px Helvetica Neue weight 500, UPPERCASE, letter-spacing `0.05em`
- Use: Recycled, repaired, fair-trade indicators

**Sale Badge**
- Background: Sale Red (`#b3261e`)
- Text: Pure White (`#ffffff`)
- Padding: 4px 8px
- Radius: `2px`
- Font: 11px weight 500 UPPERCASE
- Use: Discounted-product flag in the upper-left of product cards

**Color Swatch Dot**
- Size: 16px × 16px (selectable), 12px × 12px (count indicator)
- Radius: `9999px`
- Border: `1px solid #e5e5e5` default, `1px solid #000000` on selected
- Use: Color variant picker on product cards and PDP

### Inputs & Forms
- Background: Pure White (`#ffffff`)
- Border: `1px solid #1a1a1a`
- Radius: `2px`
- Font: 16px Helvetica Neue weight 400
- Text color: `#1a1a1a`
- Focus: border thickens to `2px solid #03245c` (Patagonia Blue)
- Placeholder: `#8a8a8a`
- Padding: 12px 16px

### Navigation

**Top utility bar (the activist bar)**
- Background: True Black (`#000000`)
- Text: Pure White (`#ffffff`)
- Height: 32px
- Font: 11–12px weight 500, mixed case or light uppercase
- Content: rotating environmental / corporate-position copy ("Earth Is Now Our Only Shareholder")
- Sticky: scrolls with page, not pinned

**Primary nav bar**
- Background: Pure White (`#ffffff`)
- Height: 64px
- Logo: Patagonia wordmark + mountain glyph, ~120px wide, left-aligned
- Categories: "Featured / Men's / Women's / Kids' / Packs & Gear / Food & Beer / Sports", center-aligned, 14px weight 500
- Right cluster: search pill (`#f5f4f1` background, 1px border), wishlist heart icon, account icon, bag icon
- Hover: category underline appears 4px below text, mega-menu drops with sub-categories
- Border-bottom: `1px solid #e5e5e5`

### Decorative Elements

**Full-bleed Photography**
- Hero imagery, story imagery, and category-landing imagery extends edge-to-edge
- No gradient scrim by default — text overlays rely on photographic composition (negative space in upper-left or lower-left of frame)
- When a scrim is used, it's a soft `rgba(0, 0, 0, 0.25)` linear from bottom — applied sparingly

**The Mountain Logo**
- Used sparingly outside the navigation header — the wordmark is enough for most surfaces
- The full color version (red peak / blue body / green base) appears on About, Activism, and corporate content
- Always reproduced at minimum 24px height to preserve mountain silhouette legibility

## 5. Layout Principles

### Spacing System
- Base unit: 4px (with 8px as the rhythm increment for most components)
- Scale: 4px, 8px, 12px, 16px, 20px, 24px, 32px, 40px, 48px, 64px, 96px, 128px
- Notable: Patagonia's grid is a four-up product layout on desktop (96px gutters reduced to 16px between tiles), with editorial story sections breaking out to a single-column 720px reading width centered in a 1440px viewport.

### Grid & Container
- Max content width: 1440px on category and product pages, 720px reading column on Stories articles
- Hero: full-width photograph, text overlay positioned via 12-column grid (typically left-aligned columns 2–6)
- Product grid: 4-up desktop, 2-up tablet, 1-up mobile — generous 16–24px gutters
- Stories: alternating full-bleed photo sections and centered 720px text columns — magazine pacing
- Footer: 5-column dense link grid with mountain logo in the bottom-left, activist links pulled out (Activism, Worn Wear, Patagonia Films) above standard commerce links

### Whitespace Philosophy
- **Magazine pacing on stories, catalog density on commerce**: Editorial pages give 96–128px between sections; product grids run tight at 16–24px between tiles. The system flips its breathing strategy based on context.
- **Photography as the visual structure**: Full-bleed imagery does the work that decorative dividers do elsewhere. A category page reads as photo → grid → photo → grid, never with section-rule lines.
- **Quiet chrome**: Navigation, search, footer, and utility elements use thin 1px borders and no shadows. The interface stays out of the way of the photography and the writing.

### Border Radius Scale
- Sharp (0px): Default for product photography, full-bleed imagery, story cards — sharpness preserves the editorial feel
- Subtle (2px): Default for buttons, inputs, badges — almost-square but barely softened
- Soft (4px): Mega-menu panels, dropdown surfaces, hover popovers
- Pill (9999px): Hero overlay buttons, search input, color swatches, occasional activist-content CTAs
- No mid-range radii (8–24px): Patagonia avoids the modern-app look — the system is editorial first

## 6. Depth & Elevation

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | No shadow | Page canvas, full-bleed imagery, body content |
| Hairline (Level 1) | `1px solid #e5e5e5` | Product grid boundaries, footer separators, table dividers |
| Soft Card (Level 2) | `0 2px 4px rgba(0, 0, 0, 0.04)` | Search dropdown, mega-menu panels, popovers — barely-there |
| Modal Lift (Level 3) | `0 8px 24px rgba(0, 0, 0, 0.10)` | Cookie banner, cart drawer, modal dialogs |
| Photo Scrim (Level 4) | `linear-gradient(180deg, rgba(0,0,0,0) 60%, rgba(0,0,0,0.25) 100%)` | Photographic CTAs needing legibility — used sparingly |

**Shadow Philosophy**: Patagonia treats elevation the way a print catalog does — almost not at all. The interface is layered through photography, type weight, and 1px hairlines, not through atmospheric depth. The two shadow tiers that do exist (Soft Card and Modal Lift) are reserved for elements that genuinely float above the page (dropdowns, modals) — never on cards, buttons, or persistent chrome. The result is a flat, paper-like surface that lets photography deliver the visual punch.

### Decorative Depth
- The activist utility bar sits on `#000000` against the white nav, which creates a graphic depth-by-contrast rather than shadow-based depth
- Hover states on product cards use a 1.02× image scale inside a fixed crop window — depth via motion, not shadow
- Mega-menu panels drop with a 4px radius and soft shadow only at the moment of expansion

## 7. Do's and Don'ts

### Do
- Use Patagonia Blue (`#03245c`) only for the wordmark, focus states, and inline editorial links — preserve its brand-anchor role
- Lead with full-bleed photography of real people in real conditions — climbing, surfing, fishing, never staged
- Run the activist utility bar (`#000000`) above all commerce — environmental copy as permanent chrome
- Use Helvetica Neue (or Inter / Söhne / Arial Nova as substitute) at workmanlike weights 400 and 500
- Set Stories long-form copy at 18px / 1.55 line-height — magazine generosity, not commerce-page tightness
- Keep button radius at `2px` and pill `9999px` only on photographic overlay CTAs
- Treat product cards as bordered-only at grid boundaries — let the photograph carry the tile
- Reserve Sale Red (`#b3261e`) for actual sale states, Activist Green (`#1f7a3a`) for environmental certifications
- Let copy run dense and editorial — environmental specificity over marketing brevity

### Don't
- Don't introduce gradient backgrounds anywhere in UI — the only gradient is inside the mountain logo itself
- Don't soften the page background to off-white — Patagonia commits to pure `#ffffff` for photographic contrast
- Don't apply drop shadows to product cards, buttons, or persistent chrome — depth is via hairlines and photography
- Don't use display-trend typography (geometric sans, condensed display, slab serifs) — system Helvetica is the brand
- Don't bold display headlines — weight 400 at 48–64px is the calm-confidence Patagonia move
- Don't replace the activist utility bar with a promo banner — environmental copy is non-negotiable chrome
- Don't use studio product photography on lifestyle / hero surfaces — only real conditions, real athletes
- Don't introduce mid-range radii (8–24px) — sharp, 2px, or pill, nothing in between
- Don't crowd photography with overlay scrims — choose images with built-in negative space instead

## 8. Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile Small | <375px | Single-column, hero type drops to 32–36px, 1-up product grid |
| Mobile | 375–768px | Single-column, 36–40px hero, hamburger nav, 1-up product grid |
| Tablet | 768–1024px | 2-up product grid, 40–48px hero, partial inline nav |
| Desktop | 1024–1440px | 4-up product grid, full inline nav, 48–56px hero |
| Large Desktop | ≥1440px | Maximum 1440px container, 64px editorial hero, 4-up grid with wider gutters |

### Touch Targets
- Primary CTAs: min 44px tap height, 16–24px horizontal padding on mobile
- Nav links collapse into a full-screen hamburger menu under 1024px with 56px row heights
- Color swatch picker: 24px tap area on mobile (16px visual), 16px desktop

### Collapsing Strategy
- **Nav**: Horizontal categories collapse to hamburger under 1024px; the activist utility bar remains visible at all breakpoints
- **Hero**: 64px → 48px → 36px → 32px progressive scaling, weight stays at 400 throughout
- **Product grid**: 4-up → 2-up → 1-up with maintained aspect ratios, no crop changes
- **Stories pages**: 720px reading column scales to 100% width minus 24px gutters on mobile, line-height stays 1.55
- **Photography**: Hero photographs preserve their full-bleed treatment at every breakpoint, with art-directed crops at mobile widths
- **Footer**: 5-column link grid collapses to accordion sections on mobile, mountain logo moves to centered top of footer

### Image Behavior
- Hero photography uses art-directed crops at mobile (often a tighter portrait crop of the same scene)
- Product imagery maintains square aspect ratio at all breakpoints
- Story imagery preserves full-bleed treatment but reduces intermediate margins
- The mountain logo wordmark scales proportionally; collapses to glyph-only under 375px

## 9. Agent Prompt Guide

### Quick Color Reference
- Brand Wordmark: Patagonia Blue (`#03245c`)
- Page Background: Pure White (`#ffffff`)
- Activist Bar Background: True Black (`#000000`)
- Primary Text: Body Text Black (`#1a1a1a`)
- Secondary Text: Secondary Gray (`#5c5c5c`)
- Hairline Border: `#e5e5e5`
- Sale State: Sale Red (`#b3261e`)
- Activist Certification: Activist Green (`#1f7a3a`)
- Inline Link: Link Blue (`#0050a0`)
- Editorial Surface: Surface Stone (`#f5f4f1`)

### Example Component Prompts
- "Create a Patagonia-style hero section with a full-bleed photograph of a climber on textured rock. Overlay a 48px Helvetica Neue weight 400 headline 'New Arrivals' in pure white, left-aligned at column 2 of a 12-column grid. Below, a 16px weight 400 subhead, then a white pill button — `1px solid #ffffff`, `9999px` radius, 12px 28px padding, 14px weight 500 text 'Explore'. Above the entire page, a 32px black activist bar (`#000000`) in 11px white text reading 'Earth Is Now Our Only Shareholder'."
- "Build a 4-up product grid on `#ffffff`. Each card is a square photograph with `0px` radius, no shadow, no border. Below the image: 14px Helvetica Neue weight 500 product name in `#1a1a1a`, 14px weight 400 price below, then a 12px gray (`#5c5c5c`) caption '4 colors'. Add a Sale Red (`#b3261e`) 11px UPPERCASE 'WEB SPECIAL' badge in the top-left of any sale items, 4px 8px padding, 2px radius."
- "Design a Stories editorial article. Full-bleed hero photograph at the top, then a centered 720px reading column. Headline at 64px Helvetica Neue weight 400, line-height 1.05, byline below in 12px gray. Body copy at 18px weight 400 with 1.55 line-height in `#1a1a1a`. Inline links in Link Blue (`#0050a0`) with 1px underline."
- "Create a primary nav bar — pure white background, 64px height, 1px bottom border (`#e5e5e5`). Patagonia wordmark left at 120px, category links centered at 14px weight 500 mixed case, search pill + heart + account + bag icons right-aligned. On hover, a 4px underline appears below the active category and a mega-menu panel drops with `0 2px 4px rgba(0,0,0,0.04)` soft shadow."
- "Design an Activist Green badge — `#1f7a3a` background, white text, 4px 10px padding, 2px radius, 11px Helvetica Neue weight 500 UPPERCASE with `0.05em` letter-spacing. Reads 'WORN WEAR' or 'RECYCLED MATERIALS'."

### Iteration Guide
1. Default to pure white (`#ffffff`) page background — never off-white, never warm-tinted
2. Use full-bleed photography of real people in real conditions for every hero — no studio shots, no stock illustrations
3. The activist utility bar is permanent chrome — environmental copy in 11px white-on-black, not a promotional banner
4. Helvetica Neue (or Inter / Söhne / Arial Nova substitute) at weights 400 and 500 only — no display fonts, no bold display headings
5. Patagonia Blue (`#03245c`) is the brand anchor — wordmark, focus states, and inline links only
6. Border radius is binary: `2px` for chrome (buttons, inputs, badges), `9999px` for hero pill CTAs and color swatches, `0px` for everything photographic
7. Run editorial copy at 18px / 1.55 line-height with 720px max reading width — magazine pacing, not commerce pacing
8. Avoid drop shadows on cards, buttons, and chrome — use 1px hairlines (`#e5e5e5`) and photographic contrast for layering
9. Sale Red (`#b3261e`) for commerce state, Activist Green (`#1f7a3a`) for environmental certifications — never blend the two tracks
10. Let typography stay calm at every size — climb the scale via px, not via weight
