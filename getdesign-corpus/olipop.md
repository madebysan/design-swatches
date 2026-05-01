# Design System Inspired by Olipop

## 1. Visual Theme & Atmosphere

Olipop's website is a sugar-rush of mid-century soda-fountain nostalgia rebuilt for a wellness brand. The page opens on a saturated hot-pink hero (`#ec5093` /* estimated */) with a chunky condensed display headline ("Bring on the Berry") that feels lifted from a 1960s drugstore poster — confident, candy-shop loud, and unabashedly retro. The whole experience refuses minimalism: pastel flavor tiles in mint, blush, hot pink, and peach stack in a five-up grid; cream-yellow promotional bands punctuate the page; and a deep hunter-green footer (`#0c3b2e` /* estimated */) closes the system with a soda-shop awning quality.

The brand reads less like a beverage DTC and more like a candy wrapper. Where most prebiotic brands lean clinical (white space, sans-serif minimalism, "natural" earth tones), Olipop leans the opposite direction — every section is a different color block, with full-bleed pastels and zero white-space cowardice. The typographic system pairs a condensed, slightly serifed display face for headlines with a cleaner sans for body and UI. Pricing, badges, and benefit callouts get pill treatments in white-on-pastel, evoking sticker placement on vintage cans.

What distinguishes Olipop most is its **chromatic flavor system** — every flavor SKU has a dominant color (mint green for Watermelon Lime, pink for Strawberry Vanilla, hot pink for Raspberry Sherbet, deep berry for Blackberry Vanilla, peach for Crisp Apple) and the entire page palette derives from those cans. The site is not a container for the cans; it's an extension of them. Combined with cherry-red CTAs, decorative berry/strawberry illustrations, and chunky pill buttons with `9999px` radius, the whole system feels like a packaged-goods brand that finally figured out how to translate shelf appeal to a homepage.

**Key Characteristics:**
- Saturated hot-pink hero (`#ec5093`) — soda-fountain confidence, no minimalist instinct
- Chunky condensed display type ("Tagliato"-style) at weights 700–900 — candy-shop poster energy
- Five-up pastel flavor grid (mint, blush, hot pink, deep pink, peach) — chromatic SKU system
- Pill buttons (`9999px` radius) in cherry red, hunter green, white — vintage label aesthetic
- Hunter-green deep footer (`#0c3b2e`) — soda-shop awning closure
- Decorative berry/fruit illustrations as section accents — editorial collage feel
- Pastel-block sectioning — every band is a different color, no neutral connective tissue
- "Pure Nostalgia-ahh" voice — playful copy with hyphenated stretches and dad-pun energy

## 2. Color Palette & Roles

### Primary
- **Olipop Hot Pink** (`#ec5093` /* estimated */): Hero background, primary brand-loud surface. The signature "this is Olipop" color.
- **Olipop Cream** (`#fff4e2` /* estimated */): Soft cream-yellow used for promotional bands ("Get Rewarded for Sipping") and warm neutral panels.
- **Hunter Green** (`#0c3b2e` /* estimated */): Footer, dark-mode surfaces, primary text on light backgrounds. Olipop's grown-up grounding color.
- **Pure White** (`#ffffff`): Top utility nav, button text on dark surfaces, surface insets.

### Brand Accent
- **Cherry Red** (`#c8202b` /* estimated */): Primary CTA buttons ("Shop the Berry", "Sign Up Now"). The action color — the soda-can label red that signals "press here".
- **Strawberry Pink** (`#f5a8be` /* estimated */): Strawberry Vanilla SKU surface, blush flavor tile.
- **Watermelon Mint** (`#a8d9a3` /* estimated */): Watermelon Lime SKU surface, mint flavor tile.
- **Berry Magenta** (`#c43680` /* estimated */): Raspberry Sherbet SKU surface — saturated chromatic anchor.
- **Blackberry Plum** (`#7b2649` /* estimated */): Blackberry Vanilla SKU surface — deepest pastel.
- **Apple Peach** (`#f3b89a` /* estimated */): Crisp Apple SKU surface, warm coral flavor tile.

### Neutrals & Text
- **Display Text Cream** (`#fff4e2`): Headline color on hot-pink and dark surfaces — never pure white, always warmed.
- **Body Hunter Green** (`#0c3b2e`): All long-form text on light backgrounds.
- **Muted Body Gray** (`#5a6a5e` /* estimated */): Secondary copy, captions, metadata.

### Surface & Borders
- **Page Canvas Cream** (`#fbf7ee` /* estimated */): Default light section background — never pure white. Olipop's white is always a paper cream.
- **Card White** (`#ffffff`): Reserved for product cards, modals, and inset surfaces.
- **Border Cream** (`#e8dfc8` /* estimated */): 1px hairline borders on quiet UI dividers.

### Shadow & Decorative Colors
- **Drop Shadow Soft** (`rgba(12, 59, 46, 0.08)`): Subtle elevation on flavor tiles and product cards.
- **Promo Highlight Yellow** (`#ffd24d` /* estimated */): Sticker-style accents, "save 15%" badges, decorative starbursts.

### Gradient System
- Olipop is **gradient-free**. The system is built on flat color blocks — every surface is a solid pastel or saturated brand color. The only blends appear in product photography (the cans themselves carry gradient labels), never in UI.

## 3. Typography Rules

### Font Family
- **Display**: A chunky condensed display face — likely `Tagliato`, `Recoleta`, or a custom OLIPOP wordmark-derived family. Heavy weights (700–900), slightly serifed terminals, vintage-soda-poster character.
- **Body / UI**: A geometric sans-serif — likely `Apercu`, `Inter`, or `Roobert`. Clean, readable, neutral foil to the loud display type.
- **Fallback stack**: `'Tagliato', 'Recoleta', Georgia, serif` for display; `'Apercu', 'Inter', system-ui, sans-serif` for body.

*Note: Actual font names are not exposed in the public CSS. Match the chunky-condensed-display + clean-sans pairing — the contrast is the system, not the specific files.*

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Hero Display | Display Condensed | 88px (5.50rem) /* estimated */ | 800 | 0.95 | -0.5px | Hero headlines — "Bring on the Berry" |
| Section Display | Display Condensed | 56px (3.50rem) | 800 | 0.98 | -0.5px | "Pure Nostalgia-ahh", "Get Rewarded for Sipping" |
| Sub-display | Display Condensed | 40px (2.50rem) | 700 | 1.02 | -0.3px | Section subheads, callout banners |
| Card Title | Display Condensed | 24px (1.50rem) | 700 | 1.10 | -0.2px | Flavor tile names, article cards |
| Body Large | Sans | 18px (1.125rem) | 400 | 1.45 | normal | Hero subheadline, intro paragraphs |
| Body | Sans | 16px (1.00rem) | 400 | 1.50 | normal | Standard reading text |
| Nav Link | Sans | 14px (0.875rem) | 600 | 1.00 | normal | Top navigation, footer links |
| Button | Sans | 14px (0.875rem) | 700 | 1.00 | 0.02em | Pill button labels |
| Caption | Sans | 13px (0.81rem) | 400 | 1.40 | normal | Metadata, legal, footnotes |
| Badge | Sans | 11px (0.69rem) | 700 | 1.00 | 0.06em | Sticker badges, "NEW" tags — uppercase |

### Principles
- **Display weight is the brand voice**: Hero and section heads run at weight 800 in a chunky condensed face. Where wellness brands default to airy serifs or thin sans, Olipop chooses density. The headlines should feel *printed*, not typed.
- **Tight display line-height**: Display sizes run at 0.95–1.10 line-height. The headlines stack as dense visual blocks — they're posters, not paragraphs.
- **Contrast pairing is the system**: Every page mixes the chunky display face with a clean geometric sans for body. Never use the display face for body copy; never use the body sans for headlines. The friction is the brand.
- **Slightly negative tracking on display**: Display sizes get `-0.5px` to `-0.2px` letter-spacing — just enough tightening to lock letters into a poster-block feel without compressing legibility.
- **Body stays neutral**: Body copy uses default tracking, weight 400, line-height 1.45–1.50. Olipop's character lives in the headlines; the body is structural.

## 4. Component Stylings

### Buttons

**Primary Cherry Red Pill**
- Background: Cherry Red (`#c8202b`)
- Text: Pure White (`#ffffff`)
- Padding: 14px 28px
- Radius: `9999px` (full pill)
- Border: none
- Shadow: `0 2px 0 rgba(0, 0, 0, 0.05)` — minimal, sticker-flat
- Font: 14px sans weight 700, slight tracking `0.02em`
- Hover: background darkens to `#a91722` /* estimated */, slight `translateY(-1px)`
- Use: Primary CTA — "Shop the Berry", "Sign Up Now", "Add to Cart"

**Hunter Green Pill**
- Background: Hunter Green (`#0c3b2e`)
- Text: Cream (`#fff4e2`)
- Padding: 14px 28px
- Radius: `9999px`
- Use: Secondary CTA on light backgrounds — "Shop All Flavors"

**Cream Outline Pill**
- Background: transparent
- Text: Hunter Green (`#0c3b2e`)
- Border: `1.5px solid #0c3b2e`
- Radius: `9999px`
- Use: Tertiary actions, filter chips, "Learn More"

**White Pill (on dark)**
- Background: `#ffffff`
- Text: Hunter Green (`#0c3b2e`)
- Radius: `9999px`
- Use: CTAs on the dark green footer surface

### Cards & Containers

**Flavor Tile**
- Background: Flavor-specific pastel (mint, blush, hot pink, deep pink, peach)
- Radius: `16px` /* estimated */
- Padding: 24px 16px
- Shadow: `0 4px 12px rgba(12, 59, 46, 0.06)` — soft elevation
- Internal layout: Can image centered top, flavor name below in display weight 700, supporting metadata in sans 14px
- Hover: subtle lift `translateY(-2px)`, shadow deepens

**Product Hero Card**
- Background: White (`#ffffff`) or flavor-pastel
- Radius: `24px` /* estimated */
- Padding: 32–48px
- Shadow: `0 8px 24px rgba(12, 59, 46, 0.08)`
- Use: Featured product callouts, "OLIPOP Digest" article cards

**Promo Band**
- Background: Cream (`#fff4e2`)
- Radius: `0px` — full-bleed band, no rounding
- Padding: 64px vertical, container-max horizontal
- Use: "Get Rewarded for Sipping" loyalty banner

### Badges / Tags / Pills
**Sticker Badge**
- Background: Promo Yellow (`#ffd24d`) or Cherry Red (`#c8202b`)
- Text: Hunter Green or White
- Padding: 4px 10px
- Radius: `9999px`
- Font: 11px sans weight 700, uppercase, tracking `0.06em`
- Use: "NEW", "BEST SELLER", "SAVE 15%"

**Flavor Pill**
- Background: SKU-specific pastel
- Text: Hunter Green
- Radius: `9999px`
- Use: Flavor selector chips, category navigation

### Inputs & Forms
- Background: `#ffffff`
- Border: `1.5px solid #0c3b2e` (hunter green)
- Radius: `9999px` for short inputs (email signup), `12px` for textareas
- Font: 16px sans weight 400
- Padding: 12–16px vertical, 20px horizontal
- Focus: border thickens to `2px`, no glow halo

### Navigation
- Top utility bar: thin cream/yellow strip with promotional copy ("Save 15% on every order — Shop Now")
- Main nav: white surface, left-aligned OLIPOP wordmark (arched logo with the signature condensed letterforms), center links, right-aligned cart + account icons
- Links: 14px sans weight 600, hunter green
- Hover: link gets cherry-red underline or color shift to cherry red
- Mobile: hamburger collapse, full-screen menu in cream over hunter-green text

### Decorative Elements

**Berry/Fruit Illustrations**
- Hand-drawn or photo-cutout fruit (raspberries, strawberries, blackberries, lime wedges) scattered around hero and product imagery
- Used as collage accents, never as primary content
- Match the pastel palette of the section they sit in

**Polka-Dot Patterning**
- Used sparingly on promotional bands and packaging callouts
- Cream dots on cherry-red, or hunter-green dots on cream
- Vintage candy-wrapper density: 16–24px dots, 32–48px spacing /* estimated */

**Arched Wordmark**
- The OLIPOP logo curves in an upward arch — a direct callback to mid-century soda branding (Coca-Cola script, A&W root beer logo)
- Always paired with the chunky display type for headlines

## 5. Layout Principles

### Spacing System
- Base unit: 8px
- Scale: 4px, 8px, 12px, 16px, 24px, 32px, 48px, 64px, 96px, 128px
- Notable: Olipop uses generous 64–96px section padding to let each color block breathe; tight 8–16px padding inside flavor tiles for poster-style density.

### Grid & Container
- Max content width: approximately 1280px /* estimated */
- Hero: full-width pastel block, two-column (text left, product imagery right)
- Flavor grid: 5 columns desktop → 3 tablet → 2 mobile
- Article grid: 3 columns desktop → 1 mobile
- Full-bleed color bands alternate — hot pink → cream → cream-yellow → cream → dark green
- Container has consistent horizontal padding (24–48px) but section backgrounds always extend full-bleed

### Whitespace Philosophy
- **Color-block pacing**: Sections are paced by background-color shifts, not whitespace. Every band changes color — the page reads like flipping through a colorful magazine.
- **Generous vertical rhythm**: 80–120px between major sections, but the content density inside each section stays high.
- **No timid neutrals**: The page never falls back to a long stretch of white. Even the "neutral" sections are warm cream, not pure white.

### Border Radius Scale
- Sharp (0px): Full-bleed promotional bands, section dividers
- Soft (8–12px): Form inputs, small UI chrome
- Card (16–24px): Flavor tiles, product cards, article cards
- Pill (9999px): All buttons, badges, sticker tags, selector chips
- Olipop's radius system favors generous rounding — sharp corners are rare, used only for full-bleed bands.

## 6. Depth & Elevation

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | No shadow | Page canvas, color-block sections, body text |
| Sticker Lift (Level 1) | `0 2px 0 rgba(0, 0, 0, 0.05)` | Buttons in default state — flat sticker feel |
| Card Lift (Level 2) | `0 4px 12px rgba(12, 59, 46, 0.06)` | Flavor tiles, content cards |
| Hero Lift (Level 3) | `0 8px 24px rgba(12, 59, 46, 0.08)` | Featured product cards, modals |
| Hover Lift (Level 4) | `0 12px 32px rgba(12, 59, 46, 0.10)` + `translateY(-2px)` | Hover state on interactive cards |

**Shadow Philosophy**: Olipop's depth system is soft and atmospheric — the opposite of Cape's hard-stamp shadows. Where Olipop wants something to feel interactive, it gets a gentle drop with a hunter-green tint (never pure black) that mimics a sticker peeling slightly off the page. The shadows are quiet because the colors are loud — saturation does the heavy lifting of drawing attention, so depth can stay subtle. The most-used elevation is the flat sticker lift on buttons; the most-loved is the hover lift on flavor tiles.

### Decorative Depth
- Cans in product imagery sometimes carry their own dimensional shadows (photographic, not CSS)
- Decorative berry illustrations are flat — no shadow, full pastel
- Promotional bands are flat color blocks with zero depth — the color contrast IS the depth

## 7. Do's and Don'ts

### Do
- Use saturated hot pink (`#ec5093`) for hero moments — confidence is the brand
- Pair chunky condensed display type at weight 800 with clean geometric sans for body
- Apply pill radius (`9999px`) to all buttons and badges — never sharp corners on CTAs
- Use cherry red (`#c8202b`) for primary CTAs only — preserve its action signal
- Build every flavor with its own pastel surface — the chromatic SKU system is the merchandising
- Alternate full-bleed color blocks (pink → cream → cream-yellow → green) for editorial pacing
- Use cream (`#fff4e2`) instead of pure white for warm neutrals — Olipop's white is always toasted
- Use hunter green (`#0c3b2e`) as the grounding text and dark-surface color
- Add berry/fruit illustrations as collage accents around hero and product moments
- Use sticker-style badges in promo yellow or cherry red for "NEW" / "SAVE 15%" callouts

### Don't
- Don't use pure white (`#ffffff`) for the page background — always cream
- Don't introduce thin display weights — Olipop's display type is always 700+
- Don't use sharp corners on buttons or pills — pill radius is non-negotiable
- Don't fall back to neutral gray sections — every band is a color block
- Don't use the chunky display face for body copy — friction is the system
- Don't add gradient fills to UI surfaces — the system is flat color
- Don't introduce drop shadows with pure black — always tint shadows hunter green
- Don't use minimalist white space as breathing room — color shifts pace the page
- Don't dilute cherry red across secondary actions — it's a primary CTA stamp
- Don't use sans-serif headlines anywhere display type would fit — the brand voice lives in display

## 8. Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile Small | <375px | Single-column, hero display drops to 44–52px |
| Mobile | 375–650px | Single-column, 56–64px hero, stacked CTAs, 2-up flavor grid |
| Tablet | 650–1000px | 3-up flavor grid, 64–72px hero, side-by-side hero |
| Desktop | 1000–1280px | 5-up flavor grid, 80–88px hero, full multi-column |
| Large Desktop | ≥1280px | Maximum scale, 1280px container, 88px+ hero |

### Touch Targets
- Pill buttons: min 44px tap height, generous horizontal padding
- Flavor tiles: full tile is the tap target, no nested tap zones
- Nav links: 44px minimum tap height with vertical padding

### Collapsing Strategy
- **Nav**: Horizontal nav collapses to hamburger below 1000px; full-screen takeover menu
- **Hero**: Two-column hero (text + product image) stacks to single column on mobile; image moves below text
- **Flavor grid**: 5 → 3 → 2 columns progressively; pastel surfaces and tile structure preserved
- **Promo bands**: Full-bleed bands maintain their colors at every breakpoint; padding reduces from 64px → 32px on mobile
- **Display type**: 88px desktop hero → 56px tablet → 44px mobile; weight 800 maintained throughout
- **Padding**: Horizontal container padding 48px desktop → 24px tablet → 16px mobile

### Image Behavior
- Product can imagery scales fluidly with viewport
- Decorative berry illustrations may hide on mobile to preserve composition
- No art direction changes — the same color blocks adapt
- Wordmark scales but never collapses to a monogram

## 9. Agent Prompt Guide

### Quick Color Reference
- Hero Surface: Olipop Hot Pink (`#ec5093`)
- Page Canvas: Page Canvas Cream (`#fbf7ee`)
- Promotional Band: Olipop Cream (`#fff4e2`)
- Footer / Dark Surface: Hunter Green (`#0c3b2e`)
- Primary CTA: Cherry Red (`#c8202b`)
- Primary Text: Hunter Green (`#0c3b2e`) on light, Cream (`#fff4e2`) on dark
- Flavor Pastels: Mint (`#a8d9a3`), Blush (`#f5a8be`), Magenta (`#c43680`), Plum (`#7b2649`), Peach (`#f3b89a`)
- Drop Shadow: `0 4px 12px rgba(12, 59, 46, 0.06)`

### Example Component Prompts
- "Build a hero section on Olipop Hot Pink (`#ec5093`). Headline at 88px chunky condensed display weight 800, line-height 0.95, letter-spacing -0.5px, color cream `#fff4e2`. Primary CTA: cherry red (`#c8202b`) pill button, `9999px` radius, 14px sans weight 700, white text, padding 14px 28px."
- "Design a flavor tile grid — 5 cards across, each on its own pastel surface (mint `#a8d9a3`, blush `#f5a8be`, hot pink `#ec5093`, plum `#7b2649`, peach `#f3b89a`). 16px radius, 24px padding, can image centered top, flavor name below in display weight 700 at 24px. Soft shadow `0 4px 12px rgba(12, 59, 46, 0.06)`."
- "Create a promotional band on Olipop Cream (`#fff4e2`), full-bleed, 64px vertical padding. Headline at 56px display weight 800 in hunter green (`#0c3b2e`), line-height 0.98. Cherry-red pill CTA on the right."
- "Design a hunter-green (`#0c3b2e`) footer with cream text (`#fff4e2`). Newsletter input as a `9999px` pill in white with a cherry-red submit button. Footer links in 14px sans weight 600."
- "Build a sticker-style badge — promo yellow (`#ffd24d`) background, hunter-green text, `9999px` radius, 4px 10px padding, 11px sans weight 700 uppercase, tracking `0.06em`. Use for 'NEW' or 'SAVE 15%' callouts."

### Iteration Guide
1. Default to the chunky condensed display face at weight 800 for every headline — lightness is off-brand
2. Pill radius (`9999px`) for buttons and badges — sharp corners are reserved for full-bleed color bands
3. Cherry red (`#c8202b`) is sacred for primary CTAs — never demote it to secondary actions
4. Cream (`#fff4e2`), not pure white — Olipop's neutral is always warmed
5. Every flavor SKU has its own pastel surface — match the chromatic SKU system across product surfaces
6. Color blocks pace the page; whitespace does not — alternate full-bleed bands generously
7. Drop shadows tint hunter green (`rgba(12, 59, 46, ...)`) — never pure black
8. Pair the chunky display face with a clean geometric sans for body — never collapse to one family
