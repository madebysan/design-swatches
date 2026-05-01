# Design System Inspired by Nécessaire

## 1. Visual Theme & Atmosphere

Nécessaire treats body care like dermatology. The site reads as a clinical-spa hybrid: pure white canvas, a single warm grey for chrome (`#f1f1f1`), near-black ink (`#111111`) for type, and product photography that sits in soft natural daylight on neutral linen and tile. Where most personal-care brands lean colorful and decorative, Nécessaire strips the page down to white space, one tasteful family of greys, and the products themselves — lined up like reagents on a lab bench. The accented French name on the logo is the one ornamental moment in the entire system.

The typographic spine of the brand is **Graebenbach** — a quietly humanist contemporary grotesk by Milieu Grotesque used at weight 500 for display and weight 400 for body. Headlines hit 72px with tight `-1px` tracking and a confident `1.10` line-height, but never shout — the letterforms are warm enough to read as editorial rather than corporate. A secondary face, **Nunito**, appears in select utility moments (review widgets, embedded buttons) but the rest of the page belongs to Graebenbach. Caption text leans on uppercase with `0.16px` tracking — an apothecary label cadence that pairs well with the white-coat palette.

What distinguishes Nécessaire most is the **pill button system**. Every primary CTA is a full pill (`40px` to `50px` radius) — black on white or white on black — with asymmetric vertical padding (`12px 20px 10px`) that gives the button a slightly weighted, hand-tooled feel. There are no gradients, no outlines beyond a single 1px hairline, no shadows except a barely-there `0px 8px 15px -10px` soft drop on a couple of overlay surfaces. The system is binary in the same way a clinical product is binary: either it's there with quiet certainty, or it isn't there at all.

**Key Characteristics:**
- Graebenbach at weight 500 for display, weight 400 for body — humanist grotesk, not serif
- Pure white (`#ffffff`) page canvas — clinical, but warmed by photography
- Off-white surface tier (`#f1f1f1`) for cards, panels, and section breaks
- Near-black text (`#111111`) instead of pure black — softens the read without losing contrast
- Pill-radius buttons (`40–50px`) with asymmetric padding — the signature interactive shape
- Mid-grey hairlines (`#c4c4c4`) on inputs and dividers — the only border weight in the system
- Uppercase caption labels with `0.16px` tracking — apothecary chrome
- Soft minimal shadow vocabulary — `0px 8px 15px -10px rgba(0,0,0,0.15)` only when absolutely needed
- Product photography on neutral linen / tile sits inside `8px` softly-rounded tiles — never full-bleed bleed-through

## 2. Color Palette & Roles

### Primary
- **Necessaire Ink** (`#111111`): Primary text, headings, body, button labels. Near-black — softer than `#000` for editorial readability.
- **Pure White** (`#ffffff`): Primary page canvas. The clinical white that everything else negotiates against.
- **Surface Grey** (`#f1f1f1`): Tier-2 background — section bands, card surfaces, the warm grey panel that breaks the white.

### Neutrals & Text
- **Body Grey** (`#494949`): Secondary text, link default state, footer text. A confident mid-tone that reads as deliberate, not faded.
- **Caption Grey** (`#737373`): Tertiary text, metadata, fine-print labels. Pairs with uppercase tracking for clinical micro-copy.
- **Hairline Grey** (`#c4c4c4`): Input borders, hairline dividers, select-field outlines. The single stroke weight in the system.
- **Subtle Grey** (`#b4b4b4`): Hover-state borders on quiet buttons. Sits just below hairline for differentiation.

### Surface & Borders
- **Canvas White** (`#ffffff`): Page background and primary card surface.
- **Tier Grey** (`#f1f1f1`): Section-band background, cart drawer surface, secondary card.
- **Border Hairline** (`1px solid #c4c4c4`): Default border on form controls and select fields.
- **Border Ink** (`1px solid #111111`): Emphasized borders on cards or dividers — used sparingly.
- **Border Transparent** (`1px solid rgba(0,0,0,0)`): Default state on outlined buttons; primes the hover transition.

### Accent / Functional
- **Nécessaire is accent-free.** The system has no hero hue, no signature lavender, no brand orange. Color comes from the product photography (skin tones, glass amber, cream beige) — never from UI chrome. The closest the system has to "accent" is the warm putty (`#c4c4bd`) that flickers on a single hover state on a form control.
- **Putty Hover** (`#c4c4bd`): A barely-perceptible warm grey-beige used on input hover/focus borders. The only chromatic warmth in the chrome.

### Compare-At / Review (Embedded Widgets)
- **Strikethrough Grey** (`#9a9a9a`): Compare-at (was-price) text in product cards.
- **Review Star** (`#fbca10`): Yellow star fill — confined to the review widget, never used elsewhere. Treat as a third-party token that shouldn't migrate into your own UI.

### Gradient System
- Nécessaire is **gradient-free.** Every surface is solid color. Photography carries any gradient feel through natural daylight falloff.

## 3. Typography Rules

### Font Family
- **Primary**: `Graebenbach`, with fallback `Arial`, `sans-serif` — a humanist contemporary grotesk by Milieu Grotesque. Used for headings, body, navigation, and most buttons.
- **Secondary**: `Nunito` — a softer rounded sans, served via Google Fonts. Appears only in select utility components (review-widget chrome, certain embedded buttons). Treat as third-party-tier, not core.
- **OpenType Features**: Standard ligatures only. The name "Nécessaire" carries the only stylistic flourish (the acute accent), and it lives in the logo SVG.

*Note: Graebenbach is a commercial typeface from Milieu Grotesque. Close substitutes for prototyping include Söhne, Inter (weight 500), or Neue Haas Grotesk Display. Nunito is free via Google Fonts but use it sparingly — it doesn't share Graebenbach's structure.*

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Display Hero | Graebenbach | 72px (4.50rem) | 500 | 1.10 | -1px | Maximum size — landing hero statements |
| Display | Graebenbach | 45px (2.81rem) | 500 | 1.10 | -1px | Secondary hero, full-width section heads |
| Heading Large | Graebenbach | 28px (1.75rem) | 500 | 1.10 | -0.5px | Sub-section heads, large card titles |
| Heading | Graebenbach | 24px (1.50rem) | 700 | 1.00 | normal | Section heads, emphasized card chrome |
| Heading Small | Graebenbach | 21px (1.31rem) | 500 | 1.10–1.50 | 0.16px | Card titles, product names |
| Sub-heading | Graebenbach | 20px (1.25rem) | 500 | 1.20 | normal | Small section heads |
| Body Large | Graebenbach | 18px (1.13rem) | 400 | 1.33 | normal | Intro paragraphs, emphasized body |
| Body | Graebenbach | 16px (1.00rem) | 400 | 1.50 | 0.16px | Standard reading text |
| Body Tight | Graebenbach | 16px (1.00rem) | 500 | 1.19 | normal | Nav links, denser body blocks |
| Caption | Graebenbach | 14px (0.88rem) | 400 | 1.50 | 0.16px | Metadata, small labels |
| Caption Bold | Graebenbach | 14px (0.88rem) | 700 | 1.50 | 0.16px | Uppercase badge text, eyebrow labels |
| Caption Small | Graebenbach | 12px (0.75rem) | 400 | 1.17 | 0.16px | Fine print, footer legal |
| Micro | Graebenbach | 10px (0.63rem) | 400 | 1.50–2.20 | 0.16px | Uppercase chrome labels (often `text-transform: uppercase`) |

### Principles
- **Weight 500 is the headline default.** Graebenbach's weight 500 (medium) does the work that Bold does on most sites — the typeface has enough density at 500 that reaching for 700 feels heavy. Reserve weight 700 for caption-size uppercase badges.
- **Negative tracking on display only.** Headings 45px and above use `-1px` tracking. From 21px down to body, tracking shifts to `0.16px` positive — a subtle apothecary widening that gives caption text a labeled, almost pharmacy-printed feel.
- **Line-height as scale signal.** Display sizes run tight at `1.10`. Body sits airy at `1.50`. The system uses line-height almost as much as size to communicate hierarchy.
- **Uppercase + 0.16px for chrome.** Eyebrow labels, badges, and certain links shift to uppercase with letter-spacing `0.16px` and weight 400 or 700. The signal is "this is metadata, not content."
- **Two-weight body simplicity.** Body text is weight 400 unless tightening to a denser navigation/menu line, where 500 takes over. No italics in the chrome, ever.

## 4. Component Stylings

### Buttons

**Primary Pill (Black)**
- Background: Necessaire Ink (`#111111`)
- Text: Pure White (`#ffffff`)
- Padding: `12px 20px 10px` — note the asymmetric vertical (12 top, 10 bottom)
- Radius: `40px` (full pill)
- Border: `0px none` default, `1px solid #ffffff` on hover
- Shadow: `none`
- Font: 16px Graebenbach weight 400
- Hover: subtle ring `0 0 0 2px` of background-active token
- Use: Primary CTA — "Add to Cart", "Shop The Body", "Subscribe & Save"

**Primary Pill (White)**
- Background: Pure White (`#ffffff`)
- Text: Necessaire Ink (`#111111`)
- Padding: `12px 20px 10px`
- Radius: `40px` (full pill)
- Border: `1px solid rgba(0,0,0,0)` default — transparent placeholder; transitions to `1px solid #ffffff` on hover when on dark backgrounds
- Font: 16px Graebenbach weight 400
- Use: Inverted primary CTA on dark/photography sections

**Quiet Pill (Hairline)**
- Background: Pure White (`#ffffff`)
- Text: Necessaire Ink (`#111111`)
- Padding: `6px 5px 4px` (compact)
- Radius: `40px`
- Border: `1px solid #c4c4c4`
- Font: 14px Graebenbach weight 400
- Use: Tertiary buy-again or quick-action buttons on product cards

**Round Cart Pill (50px)**
- Background: Pure Black (`#000000`)
- Text: Pure White (`#ffffff`)
- Padding: `16px`
- Radius: `50px` (slightly rounder than 40px standard for visual emphasis)
- Font: 18px Graebenbach weight 400
- Use: Sticky cart, persistent floating CTAs — the most rounded interactive surface in the system

**Circular Carousel Control**
- Background: Transparent (`rgba(255,255,255,0)`)
- Color: Black (`#000000`)
- Padding: `0px`
- Radius: `50%` (true circle)
- Transform: `matrix(1, 0, 0, 1, 0, -20)` — vertically nudged for visual centering on imagery
- Use: Carousel prev/next, modal close

### Cards & Containers
- Background: `#ffffff` for product cards on white sections; `#f1f1f1` for product cards on tinted bands
- Border: `0px` default — cards rely on space and the photo, not frames
- Radius: `8px` for image-bearing tiles (the most-used radius in the system); `0px` for full-width content panels
- Shadow: `none` standard; `rgba(0,0,0,0.15) 0px 8px 15px -10px` for floating overlays
- Internal padding: 24–48px for product cards, generous (96–100px+) for editorial sections

### Badges / Tags / Pills
**Eyebrow Badge (Default)**
- Background: Hairline Grey (`#c4c4c4`)
- Text: Necessaire Ink (`#111111`)
- Padding: `6px 10px`
- Radius: `0px` (sharp rectangle — the one place sharp corners persist)
- Font: 14px Graebenbach weight 700, uppercase, `0.16px` tracking
- Use: Status chips, certification labels, "NEW" / "BESTSELLER" markers

**Page Dot (Carousel)**
- Background: rotating black/grey based on active state
- Size: 11×11px
- Radius: `11px` (full circle — coincidentally the same as size, giving a true dot)
- Use: Carousel pagination

### Inputs & Forms
- Background: `#ffffff`
- Border: `1px solid #c4c4c4`
- Radius: `0px` — inputs are sharp; only buttons take the pill radius
- Font: 16px Graebenbach weight 400
- Text color: `#111111`
- Placeholder color: `#737373`
- Padding: `10px 40px 10px 15px` (extra right padding accommodates the chevron icon on selects)
- Focus: `outline: 0.2rem solid var(--rc-active-color)`, `box-shadow: rgba(0,0,0,0.25) 0px 0px 0px 0.2rem` — a subtle dark ring rather than a chromatic accent
- Search Input variant: Border bottom only (`0px 0px 2px solid #c4c4bd`) — flat underlined style, no surrounding box

### Navigation
- Top nav: full-width white bar, centered Nécessaire wordmark logo, left/right utility links flanking
- Logo color: `#494949` (Body Grey) — slightly recessive, not pure ink; reinforces the quiet luxury read
- Hover menus: large multi-column dropdown panels filled with category links, product thumbnails, and editorial micro-copy
- Links: Graebenbach 16px weight 400, color `#494949` default with `text-decoration: underline` on most contexts
- Hover: link color shifts to `#ffffff` on dark surfaces, `#111111` on light — high-contrast resolution rather than a fade
- Sticky behavior: nav remains fixed; certain promo bars sit above and dismiss on scroll

### Decorative Elements

**Soft Shadow (Overlay Only)**
- `rgba(0, 0, 0, 0.15) 0px 8px 15px -10px` — used on cart drawer, modal overlays, and floating cart pills
- Reserved for genuinely layered content; never applied to inline cards

**Modal Lift Shadow**
- `rgba(0, 0, 0, 0.176) 0px 16px 48px 0px` — used on the cart modal and gallery zoom
- Note the slightly higher `y: 16px` and larger `48px` blur — a deliberately atmospheric drop reserved for the highest layer

**Photography-as-Color**
- Nécessaire's product photography functions as the system's color palette
- Skin tones, amber bottles, cream tubes, linen and travertine surroundings — these are where any warmth in the page comes from
- UI never competes; it stays in the white-grey-black register and lets the photo do the heavy lifting

## 5. Layout Principles

### Spacing System
- Base unit: 5px (with cascading common values 5, 10, 15, 20, 25, 30 — a 5-grid leaning toward fives rather than pure 8s)
- Frequent values: 5, 8, 10, 12, 15, 16, 20, 27, 30, 40, 48, 100px
- Notable: Nécessaire uses **27px** unusually often (likely an asymmetric padding value derived from typography metrics) and jumps to 100px for major section breaks. Mid-range (50–80px) is rare.

### Grid & Container
- Max content width: ~1200–1280px
- Hero: full-width single-column hero photography with type overlaid
- Product grids: 2-column on tablet, 3–4 column on desktop with consistent 8px-radius image tiles
- Editorial sections: full-width photography alternating with centered text columns at ~720px max
- Footer: full-width 3-4 column layout on `#111111` ink background

### Whitespace Philosophy
- **Spa-pacing**: Each section gets 80–100px+ of vertical air. The page feels unhurried, like a printed editorial.
- **White as the dominant surface**: Most of the page is white. The grey (`#f1f1f1`) panels exist to mark chapters, not to fill space.
- **Photography breathing**: Product hero shots are surrounded by white margins rather than pushed edge-to-edge. The product, not the viewport, is the focus.

### Border Radius Scale
- Sharp (`0px`): Inputs, badges, dividers, content panels — the chrome of the system
- Soft (`8px`): Image tiles, product cards, photography containers — the most-used radius
- Pill Compact (`40px`): Standard buttons — the signature interactive shape
- Pill Round (`50px`): Floating/sticky CTAs — slightly more emphatic
- Circle (`50%` or `11px` on dots): Carousel controls, page dots, avatar masks

## 6. Depth & Elevation

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | No shadow | Page canvas, cards, buttons in default state |
| Subtle Lift (Level 1) | `rgba(0,0,0,0.15) 0px 8px 15px -10px` | Floating cart pill, hover-elevated tiles |
| Drawer (Level 2) | `rgba(0,0,0,0.176) 0px 16px 48px 0px` | Cart drawer, modal overlays, gallery zoom |
| Focus Ring (Level 3) | `rgba(0,0,0,0.25) 0px 0px 0px 0.2rem` + `0.2rem solid` outline | Keyboard focus on inputs and buttons |

**Shadow Philosophy**: Nécessaire's depth system is deliberately understated. Where most product/e-commerce sites lean on multi-layer shadow stacks for "elevation realism," Nécessaire uses two shadows total — one subtle (`-10` spread) and one atmospheric (`48` blur) — and only on genuinely floating layers. The defaults are flat. The system trusts white space and typography to handle hierarchy and reserves shadow for moments where a layer literally floats above content (the cart drawer pulls in from the side; the floating pill follows scroll). This restraint is what makes the page feel premium rather than busy.

### Decorative Depth
- Buttons stay flat — no offset, no inner shadow, no gradient. The pill shape carries the weight.
- Cards stay flat by default; hover may add the Subtle Lift to communicate interactivity, but most product cards never elevate.
- No glow, no inset, no neumorphism. The system reads as "matte print magazine" rather than "glossy app."

## 7. Do's and Don'ts

### Do
- Use Graebenbach weight 500 for display sizes — medium is the headline weight
- Default to weight 400 for body and most buttons
- Keep page background pure white (`#ffffff`); use `#f1f1f1` for tier-2 surface bands only
- Use Necessaire Ink (`#111111`) instead of pure black for body type — it reads softer
- Apply pill radius (`40px` standard, `50px` for floating) on every button
- Keep inputs sharp (`0px` radius) — only buttons take the pill
- Use `8px` radius on image tiles and product cards
- Apply `0.16px` letter-spacing on body and caption sizes; `-1px` tracking on display
- Use uppercase + weight 700 on caption-size eyebrows and badges
- Reserve shadows for genuinely floating layers (cart drawer, modal, sticky pill)

### Don't
- Don't use pure black (`#000000`) for body text — Necessaire Ink (`#111111`) is the warmer default
- Don't introduce a chromatic accent color — the system is white/grey/ink and stays that way
- Don't reach for weight 700 on display headlines — weight 500 carries the size
- Don't use rounded radius (4–16px) on buttons — buttons are full pills, end of discussion
- Don't apply pill radius to inputs or content cards — those are sharp or `8px`-soft
- Don't stack multiple shadows for "elevation realism" — flat by default, two shadows total
- Don't replace photography with illustration — the products are the visuals
- Don't let typography shout — the brand voice is quiet, confident, clinical
- Don't use Nunito for primary content — it's a third-party widget face only
- Don't let buttons exceed 18px font-size — the pill stays compact and legible

## 8. Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile Small | <400px | Single column, hero drops to 32–36px, full-width pills |
| Mobile | 400–576px | Single column, 36–45px hero, stacked CTAs |
| Mobile Large | 576–768px | 2-column product grid begins, 45px hero |
| Tablet | 768–992px | 3-column product grid, 56–60px hero |
| Desktop | 992–1280px | Full multi-column layouts, 60–72px hero |
| Large Desktop | ≥1280px | Maximum scale (72px hero), centered 1200–1280px container |

The system declares an unusually wide set of breakpoints (98, 360, 400, 480, 481, 500, 550, 576, 600, 640, 750, 767, 768, 991, 992, 1023, 1024, 1080, 1200, 1280, 1480, 1536) — most are micro-tweaks for product-grid alignment rather than meaningful layout shifts. Treat 480 / 768 / 1024 / 1280 as the canonical four.

### Touch Targets
- Primary pills: min 44px tap height; padding scales to ensure thumb-friendly hit area on mobile
- Carousel controls: 44×44px tap target around the visual circle
- Page dots: 11px visual / ~28px tap area
- Nav links: 16px font with generous line-height padding

### Collapsing Strategy
- **Nav**: Horizontal nav collapses to hamburger on mobile; full-screen overlay menu on open with category accordion
- **Hero**: 72px → 45px → 36px progressive scaling; weight 500 maintained throughout
- **Product grid**: 4-column desktop → 3 → 2 → 1 on smallest viewports
- **Footer**: 4-column desktop → 2-column tablet → stacked mobile
- **Section spacing**: 100px desktop → 48–64px mobile
- **Caption tracking**: Stays at `0.16px` across all breakpoints

### Image Behavior
- Product photography preserves `8px` corner radius across all viewports
- Hero photography crops slightly tighter on mobile but maintains the centered-product framing
- No art direction changes — the same shot adapts; the brand never swaps to a "mobile version"
- Logo wordmark scales proportionally; never reduces to a monogram

## 9. Agent Prompt Guide

### Quick Color Reference
- Primary CTA: Necessaire Ink on White (`#111111` on `#ffffff`) or White on Ink (inverted on photography)
- Page Background: Pure White (`#ffffff`)
- Tier-2 Surface: Surface Grey (`#f1f1f1`)
- Primary Text: Necessaire Ink (`#111111`)
- Secondary Text: Body Grey (`#494949`)
- Caption Text: Caption Grey (`#737373`)
- Hairline Border: `1px solid #c4c4c4`
- Subtle Shadow: `rgba(0, 0, 0, 0.15) 0px 8px 15px -10px`
- Drawer Shadow: `rgba(0, 0, 0, 0.176) 0px 16px 48px 0px`

### Example Component Prompts
- "Build a hero section on Pure White (`#ffffff`) with a 72px Graebenbach weight 500 headline in `#111111`, line-height 1.10, letter-spacing -1px. Below it, a 16px Graebenbach weight 400 sub-headline in `#494949` with `0.16px` letter-spacing. Primary CTA: black pill (`#111111` background, `#ffffff` text, 40px radius, 12px 20px 10px asymmetric padding, 16px Graebenbach weight 400)."
- "Design a product card on `#ffffff` with `8px` border-radius on the image, `0px` radius on the surrounding panel, no border, no shadow. Product name in 21px Graebenbach weight 500, `0.16px` letter-spacing. Price in 16px Graebenbach weight 400 in `#494949`. Quiet pill button: white background, `1px solid #c4c4c4`, 14px Graebenbach weight 400, 40px radius."
- "Create an eyebrow badge — Hairline Grey (`#c4c4c4`) background, `#111111` text, `0px` radius (sharp rectangle), 6px 10px padding, 14px Graebenbach weight 700 uppercase with `0.16px` letter-spacing."
- "Style a form input — pure white background (`#ffffff`), `1px solid #c4c4c4` border, `0px` radius (sharp), 16px Graebenbach weight 400 in `#111111`, padding `10px 40px 10px 15px`. Focus state: `0.2rem solid` outline + `rgba(0,0,0,0.25) 0px 0px 0px 0.2rem` ring. Placeholder text in `#737373`."
- "Build a sticky floating cart pill — pure black (`#000000`) background, white text, `50px` radius, 16px padding, 18px Graebenbach weight 400. Apply `rgba(0,0,0,0.15) 0px 8px 15px -10px` soft shadow to lift it off the page."
- "Create a section divider band — full-width `#f1f1f1` background, 100px vertical padding, centered content column at 720px max-width. Section heading in 45px Graebenbach weight 500, `-1px` letter-spacing, `1.10` line-height."

### Iteration Guide
1. Default to Graebenbach weight 500 for display, weight 400 for body — medium is the new bold here
2. Page background is always pure white (`#ffffff`); use Surface Grey (`#f1f1f1`) only for chaptering
3. Buttons are pills (`40px` standard, `50px` floating); inputs and badges stay sharp (`0px`)
4. Image tiles use `8px` radius — the only mid-range value in the system
5. Body text is `#111111`, not pure `#000` — preserve the warm-clinical read
6. Apply `0.16px` letter-spacing on body/caption; `-1px` tracking only on 45px+ display
7. No accent color exists — if a moment needs warmth, source it from photography
8. Reserve shadows for floating layers only (cart drawer, modal, sticky CTA)
9. Uppercase + weight 700 + `0.16px` tracking is the apothecary chrome formula
10. Let the products carry color; let the type carry hierarchy; let the white space carry mood
