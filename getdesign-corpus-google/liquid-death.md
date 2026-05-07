---
version: alpha
name: "Liquid Death"
description: "Token-first design system reference for Liquid Death."

colors:
  background: "#ffffff"
  surface: "#d2ac5a"
  surface-elevated: "#f5f5f5"
  ink: "#000000"
  ink-muted: "#151515"
  primary: "#000000"
  on-primary: "#ffffff"
  border: "#999999"
  focus-ring: "#000000"
  success: "#22c55e"
  warning: "#f59e0b"
  error: "#ef4444"
  shadow-soft: "#d9d9d9"

typography:
  display-hero:
    fontFamily: "Acumin Pro, ui-sans-serif, system-ui, sans-serif"
    fontSize: 60px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -1px
  display:
    fontFamily: "Acumin Pro, ui-sans-serif, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 700
    lineHeight: 1.1
    letterSpacing: -0.5px
  heading-section:
    fontFamily: "Acumin Pro, ui-sans-serif, system-ui, sans-serif"
    fontSize: 40px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.25px
  heading-sub:
    fontFamily: "Acumin Pro, ui-sans-serif, system-ui, sans-serif"
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0px
  body-large:
    fontFamily: "Acumin Pro, ui-sans-serif, system-ui, sans-serif"
    fontSize: 28px
    fontWeight: 700
    lineHeight: 1.5
    letterSpacing: 0px
  body:
    fontFamily: "Acumin Pro, ui-sans-serif, system-ui, sans-serif"
    fontSize: 26px
    fontWeight: 700
    lineHeight: 1.5
    letterSpacing: 0px
  button-ui:
    fontFamily: "Acumin Pro, ui-sans-serif, system-ui, sans-serif"
    fontSize: 26px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: 0px
  caption:
    fontFamily: "Acumin Pro, ui-sans-serif, system-ui, sans-serif"
    fontSize: 28px
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

# Liquid Death Design System

## Overview

Liquid Death's website is heavy-metal album art weaponized as a beverage e-commerce site. The page opens on a pure black canvas (`#000000`) wallpapered with crushed-can textures, skull engravings, and full-bleed product photography of tallboy cans. Where every other water brand reaches for serene blue gradients and dewdrop typography, Liquid Death does the opposite — sharp condensed sans-serif at heroic sizes, all-caps everywhere, and a brand voice that reads like a death-metal record sleeve crossed with a 1980s VHS box. The signature gold-on-black logo (`#d2ac5a` over `#000000`) is the only chromatic ornamentation; product cans (pink Scary Strawberry, blue Tropical Terror, orange Orange Horror) supply the rest of the color through photography, not CSS.

The defining visual move is **uppercase Acumin Pro at weight 700** running at 56–60px across nearly every headline — "MURDER YOUR THIRST," "KILLER MERCH," "JOIN THE CLUB." Line-height locks at exactly `1.00`, letter-spacing stays neutral or barely positive (`+1px` on buttons), and there's no negative tracking finesse — this is blunt-force typography that wants to look stamped on the side of a metal can. The condensed cut (`acumin-pro-condensed`) at line-height `0.62` appears on price tags and small labels, compressing vertical space the way thrash-metal logos compress letterforms. There is zero ornamental script, zero hand-lettering on the actual web pages (the hand-lettered look lives on the can artwork imagery), and zero gradient softening.

What makes Liquid Death distinct from other punk/edgy brands is the **disciplined minimalism underneath the chaos**. The CTAs are flat black or flat white rectangles. Borders are 1px solid black, no shadow stack, no gradients. Hover states do exactly one thing: text fades from `#000000` (or `#ffffff`) to a desaturated `#999999`. No transforms, no scale, no color shifts to red. The visual aggression comes entirely from the photography, the copy, and the typographic weight — the chrome itself is Swiss-grade restrained. It's the opposite of skeuomorphic edginess; the system is austere so the heavy-metal cans can scream uncontested.

**Key Characteristics:**
- Acumin Pro weight 700 at 56–60px for hero headlines — uppercase, line-height 1.00, no tracking
- Pure black canvas (`#000000`) with white inverted sections — no off-blacks, no warm whites
- Crushed-aluminum and skull photography fills full-bleed sections instead of CSS textures
- Gold-on-black logo (`#d2ac5a`) is the only non-mono accent in the chrome itself
- Sharp 0-radius corners on every interactive element — no rounded corners anywhere visible
- Simple text-fade hover (`#000` → `#999`) replaces the entire hover/focus motion vocabulary
- Product cans (saturated pink/blue/orange/lime) provide all chromatic energy via photography
- Heavy-metal/punk copywriting ("MURDER YOUR THIRST," "DEATH TO PLASTIC") drives brand voice more than visual ornamentation

## Colors

### Primary
- **Death Black** (`#000000`): Primary canvas, primary text on white sections, default button background. Pure black — Liquid Death never softens.
- **Skull White** (`#ffffff`): Inverted canvas for the merch and product grid sections, primary text on dark sections, button background on inverted CTAs.
- **Crushed Aluminum** (`#151515`): Near-black used on dark UI surfaces, footer backgrounds, and overlay panels — a half-step warmer than pure black for layered dark sections.
- **Concrete Gray** (`#232323`): Slightly lighter dark surface for cards and form fields on dark backgrounds.

### Brand Accent
- **Logo Gold** (`#d2ac5a`): The signature death-skull logo color — applied to the wordmark, the seal/badge graphics, and occasionally to underlined inline links. The only chromatic accent in the system chrome.
- **Bronze Gold** (`#8a6d35`): A darker gold variant — used as a hover/pressed state for gold links and as an underlined link default before hover.

### Hover & Disabled
- **Fog Gray** (`#999999`): The universal hover color. Every link, every nav item, every text-CTA fades from its default (`#000` or `#fff`) to `#999999` on hover. No color shifts, no underlines, just a desaturation pulse.
- **Mid Gray** (`#757575` /* dembrandt-extracted */): Compare-at price color in product listings.
- **Slate Inactive** (`#546b7d` /* search component variable */): Inactive tab text in search results.

### Surfaces & Borders
- **Border Black** (`#000000`): Full-weight 1px borders on white-section buttons, badges, and merch card frames.
- **Border White** (`#ffffff`): Inverted 1px borders on dark-section CTAs.
- **Card Black** (`#000000`): Default card/panel background on the merch grid; also used for the "JOIN THE CLUB" / "SELL LIQUID DEATH" dual-CTA panels.

### Functional Colors (extracted from third-party search component)
- **Sale Green** (`#39a25f` /* search widget */): Discount/sale price callout in product search.
- **Star Yellow** (`#FBCA10` /* search widget */): Review-star fill color in search results.
- **Action Blue** (`#335eea` /* search widget */): Active tab indicator in search panels.

### Gradient System
- Liquid Death is **gradient-free** in its chrome. Every fill is solid. The only "gradients" on the site come from photographic backgrounds — crushed-can metallics, ice cubes, water splashes — which are raster images, not CSS. The system itself is binary black-or-white with gold as the single chromatic note.

## Typography

### Font Family
- **Primary**: `Acumin Pro`, with fallback chain `-apple-system, system-ui, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue"`
- **Condensed Variant**: `acumin-pro-condensed`, fallback `Arial, "Helvetica Neue", Helvetica` — used for tight vertical contexts (price tags, micro labels) at line-height `0.62`
- **OpenType Features**: Standard ligatures only — no stylistic sets. Weight 700 carries the entire system.

*Note: Acumin Pro is a Robert Slimbach typeface (Adobe Fonts). For external implementations, Neue Haas Grotesk or Söhne are close substitutes; Inter Bold or Barlow Condensed work as web-safe alternatives. The condensed cut at very low line-height is critical for the heavy-metal compression effect.*

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Display Hero | Acumin Pro | 60px (3.75rem) | 700 | 1.00 | normal | Maximum size — hero statements like "MURDER YOUR THIRST" |
| Display Large | Acumin Pro | 56px (3.50rem) | 700 | 1.00 | normal | Section heroes, full-width statements |
| Display Condensed | acumin-pro-condensed | 45px (2.81rem) | 700 | 0.62 | normal | Compressed display variant for stacked headlines |
| Section Heading | Acumin Pro | 40px (2.50rem) | 700 | 1.00 | normal | Feature section titles |
| Sub-heading Large | Acumin Pro | 36px (2.25rem) | 700 | 1.67 | normal | Sub-section markers with breathing line-height |
| Sub-heading | Acumin Pro | 32px (2.00rem) | 700 | 1.00 | 1px (button) / normal | Card titles, link headlines, CTA labels (uppercase variant common) |
| Sub-heading Small | Acumin Pro | 28px (1.75rem) | 700 | 1.00 | normal | Uppercase link headlines, smaller section heads |
| Body Large | Acumin Pro | 26.4px (1.65rem) | 700 | 1.37 | -0.44px | Emphasized body, pull statements — only place tracking goes negative |
| Body | Acumin Pro | 24px (1.50rem) | 400 | 1.20 | normal | Standard reading text — weight 400 appears here |
| Body Small | Acumin Pro | 16px (1.00rem) | 400 | 1.40 /* estimated */ | normal | Paragraph text, descriptions |
| Nav Link | Acumin Pro | 14–16px /* estimated */ | 700 | 1.00 | normal | Top navigation, often uppercase |
| Button UI | Acumin Pro | 14–16px /* estimated */ | 700 | 1.00 | 1px | Button labels, uppercase |
| Caption | Acumin Pro | 12px /* estimated */ | 400 | 1.33 /* estimated */ | normal | Calorie counts, micro metadata |

### Principles
- **Weight 700 is the ceiling and the floor**: Every headline, every link headline, every button is weight 700. Body copy drops to 400 only when readability demands it. There is no weight 500 or 600 anywhere — the system is binary heavy or normal.
- **Line-height 1.00 locks the headline blocks**: At 32px and above, headlines run at exactly `1.00` line-height, creating dense rectangular type blocks that read like t-shirt graphics or album-cover lockups. The 36px size at `1.67` is the rare exception for breathing sub-heads.
- **Uppercase is the default for action and headline**: Hero copy ("MURDER YOUR THIRST"), button labels ("SHOP NOW," "JOIN THE CLUB"), nav links, and section markers all run uppercase. Sentence-case is reserved for body paragraphs and product descriptions only.
- **Letter-spacing stays neutral**: Unlike most editorial systems, Liquid Death does not tighten display headlines with negative tracking. Tracking is `normal` at hero sizes; `1px` positive on buttons; `-0.44px` only at the 26.4px body-emphasized size. This keeps the type blocky and stamped, not refined.
- **Condensed cut for vertical compression**: When a stacked label needs to fit tight (price callouts, badge copy, navigation chips), the condensed variant runs at line-height `0.62` — letterforms nearly touching, classic metal-band-logo compression.

## Layout

### Spacing System
- Base unit: 8px /* estimated */
- Scale: 4px, 8px, 12px, 16px, 24px, 32px, 48px, 64px, 96px, 128px /* estimated */
- Notable: Section spacing is generous (96–128px between major sections) but card/grid spacing is tight (16–24px). The contrast between dense product grids and airy section breaks is deliberate.

### Grid & Container
- Max content width: approximately 1280–1440px /* estimated from breakpoint data */
- Hero: full-bleed black-canvas with a centered modal overlay (newsletter capture) on first visit
- Product grid: 3-up on desktop, generous gutter, no card chrome
- Merch grid: 4-up on desktop with t-shirt and drinkware photography, also no card chrome
- Dual-CTA panel: 2-column black panels at full width — "JOIN THE CLUB" + "SELL LIQUID DEATH"
- Footer: 3–4 column on desktop, condensed legal-style links

### Whitespace Philosophy
- **Sectional alternation**: black sections alternate with white sections, creating chapter breaks without dividers — every other section is inverted
- **Photo-anchored rhythm**: Full-bleed photography (crushed cans, ice, lifestyle) carries more weight than CSS spacing — sections without photos use 96–128px vertical padding to compensate
- **Tight grids inside loose pages**: The merch and beverage grids run tight with minimal gutter, but the section above and below breathes generously

### Border Radius Scale
- Sharp (0px): Default for every interactive element — buttons, badges, cards, inputs, modals
- Pill (9999px): Reserved for circular avatars or icon-only social-link buttons /* estimated */
- No mid-range radii: Liquid Death does not use 4–16px values. The system is sharp-rectangular by default.

## Elevation & Depth

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | No shadow, no border, no inset | Default page surface, body text, photo backgrounds |
| Hairline (Level 1) | `1px solid #000000` (or `#ffffff` inverted) | Buttons, badges, form fields, outlined cards |
| Photo-Embedded (Level 2) | Full-bleed raster image as background | Hero sections, dual-CTA panels, product feature blocks |
| Modal Overlay (Level 3) | `rgba(0, 0, 0, 0.6)` /* estimated */ scrim + centered black panel | Newsletter signup, age verification, cart slide-in |

**Shadow Philosophy**: Liquid Death does not believe in elevation shadows. The dembrandt audit returned no extracted shadow values — there are no `box-shadow` declarations carrying the visual hierarchy. Depth comes from contrast (black-on-white, white-on-black), from photographic backgrounds (crushed metal, ice), and from the gold logo seal embossed into dark panels. This is intentional: a heavy-metal aesthetic doesn't need atmospheric softness. Everything is flat, stamped, and printed-feeling — closer to album-cover composition than to material design.

### Decorative Depth
- Gold logo seals act as the only "embossed" elements — their raster shading creates the illusion of a stamped medal
- Photographic full-bleeds carry depth via their own light/shadow content, not via CSS
- Hover/focus states do not introduce shadow — the `#000` → `#999` text fade is the entire motion vocabulary

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

**Primary Black**
- Background: Death Black (`#000000`)
- Text: Skull White (`#ffffff`)
- Padding: 12px 24px /* estimated */
- Radius: `0px` (sharp rectangular)
- Border: `1px solid #000000` or none
- Shadow: none
- Font: Acumin Pro 14–16px weight 700, uppercase, letter-spacing `1px`
- Hover: text color `#ffffff` → `#999999` (text fade only — background stays black)
- Use: Primary CTA on white sections — "SHOP NOW," "TELL ME"

**Inverted White**
- Background: Skull White (`#ffffff`)
- Text: Death Black (`#000000`)
- Padding: 12px 24px /* estimated */
- Radius: `0px`
- Border: `1px solid #ffffff` or `1px solid #000000` (context-dependent)
- Shadow: none
- Font: Acumin Pro 14–16px weight 700, uppercase, `1px` tracking
- Hover: text color `#000000` → `#999999`
- Use: Primary CTA on black sections — "JOIN THE CLUB," "SELL LIQUID DEATH"

**Outline Black**
- Background: transparent
- Text: Death Black (`#000000`)
- Border: `1px solid #000000`
- Radius: `0px`
- Hover: text fades to `#999999`, border may fade in tandem
- Use: Secondary CTAs on white sections — "LEARN MORE," "ADD TO CART"

**Outline White**
- Background: transparent
- Text: Skull White (`#ffffff`)
- Border: `1px solid #ffffff`
- Radius: `0px`
- Hover: text fades to `#999999`
- Use: Secondary CTAs on dark/photographic sections

### Cards & Containers
- Product Card: white background, `0px` radius, no border, no shadow — relies on grid spacing alone
- Merch Card: same treatment with 1:1 product photo, weight 700 product name underneath, calorie/price below
- Dual-CTA Panel: black `#000000` background with embossed gold logo seal centered, weight 700 white headline below, full-bleed clickable
- Internal padding: 24–48px /* estimated */ — generous but not editorial
- Border: rare; spacing and contrast carry separation

### Badges / Tags / Pills
**Calorie Badge** (estimated from product grid)
- Format: small text label beneath product name ("5 cal," "0 cal")
- Font: Acumin Pro 12px /* estimated */ weight 400
- Color: Death Black (`#000000`) on white surfaces
- Treatment: pure text, no pill chrome, no border

**Sale Tag** (search component)
- Background: transparent or white
- Text: Sale Green (`#39a25f`) for sale price, Mid Gray (`#757575`) strikethrough for compare-at
- Font: Acumin Pro 14–16px /* estimated */ weight 700

### Inputs & Forms
- Background: `#ffffff` on light, `#000000` or `#151515` on dark
- Border: `1px solid #000000` (or `#ffffff` on dark)
- Radius: `0px`
- Font: Acumin Pro 16px /* estimated */ weight 400
- Text color: `#000000` (or `#ffffff` on dark)
- Focus: no custom focus ring extracted — likely browser default or `1px` outline /* estimated */
- Padding: 12–16px vertical, 16px horizontal /* estimated */
- Email signup is a single field + black submit button with all-caps label

### Navigation
- Top nav: horizontal black bar on dark sections, white on light sections — no transparency
- Logo: gold (`#d2ac5a`) skull-and-LD wordmark, left-aligned
- Links: Acumin Pro weight 700, uppercase, ~14px /* estimated */
- Hover: text fades to `#999999`
- Right side: "SHOP," "ACCOUNT," cart count
- Sticky behavior: sticky at top with no background-blur — solid color carries through

### Decorative Elements

**Gold Seal / Logo Lockup**
- Used on dark dual-CTA panels and at the top of newsletter modals
- Color: `#d2ac5a` foreground, `#000000` background
- Always rendered as a raster image (not SVG with chrome) for the engraved-medal look
- Carries the heavy-metal "death seal" iconography (skull, crossed elements, ornate framing)

**Crushed-Can Backgrounds**
- Full-bleed sections use raster photography of crushed aluminum cans, ice, water splashes
- Text overlays sit directly on top in white, weight 700 uppercase
- No gradient scrim — trust the photo's contrast
- This is where the visual aggression lives — the chrome stays Swiss

**Skull / Death Iconography**
- Limited to product can artwork and the gold logo seal
- The website chrome itself does not pepper skull icons everywhere
- This restraint is what keeps the brand from feeling cosplay-edgy

## Do's and Don'ts

### Do
- Use Acumin Pro weight 700 for every headline, link headline, and button — weight 700 is non-negotiable
- Run uppercase on every CTA, hero, and section header — sentence-case only for body paragraphs
- Lock display headlines at line-height `1.00` — let the type form dense rectangular blocks
- Keep all interactive corner radii at `0px` — sharpness is the brand
- Use the `#000` → `#999` text fade for every hover state — no color shifts, no transforms
- Alternate black and white sections — every major section should invert from the one above
- Let product photography (cans, ice, crushed metal) carry chromatic energy — keep the chrome mono
- Apply gold (`#d2ac5a`) only to the logo and seal graphics — never to body text or buttons
- Embrace the heavy-metal copy voice ("MURDER YOUR THIRST," "DEATH TO PLASTIC") — the typography is the costume

### Don't
- Don't use weight 400, 500, or 600 on headlines — Acumin 700 or nothing
- Don't introduce mid-range border-radius (4–16px) — sharp or fully circular only
- Don't add `box-shadow` for elevation — depth comes from photography and contrast
- Don't soften pure black to `#0a0a0a` or `#111` — Liquid Death is `#000000` or near-blacks like `#151515`
- Don't introduce additional accent colors beyond gold — pink/blue/orange come from product cans only
- Don't sentence-case CTA labels — every button is uppercase weight 700
- Don't tighten letter-spacing on display sizes — tracking is neutral, almost stamped
- Don't use gradients anywhere in the chrome — all fills solid
- Don't add decorative skull icons to the website chrome — skulls live on cans and seals only
- Don't use rounded photography corners — full-bleed or sharp-cropped only

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile Small | <425px | Single-column, 36–40px hero, stacked CTAs |
| Mobile | 425–768px | Single-column, 40–48px hero, sticky bottom CTA |
| Tablet | 768–1024px | 2-column product grids, 48–56px hero |
| Desktop | 1024–1440px | 3–4 column grids, 56px hero, full nav visible |
| Large Desktop | ≥1440px | Maximum 60px hero, 1280px+ container |

*Source: dembrandt extracted breakpoints span 425px → 1750px, with major transitions at 768px, 1024px, and 1280px.*

### Touch Targets
- Primary CTAs: min 44px tap height /* estimated */
- Nav links: generous tap area on mobile hamburger menu
- Add-to-cart buttons on product cards: full-width on mobile

### Collapsing Strategy
- **Nav**: Horizontal link bar collapses to hamburger on mobile; full-screen black overlay menu on open
- **Hero**: 60px → 48px → 36px progressive scaling, weight 700 maintained throughout
- **Product grids**: 3-up desktop → 2-up tablet → 1-up mobile (or 2-up tight)
- **Merch grids**: 4-up desktop → 2-up tablet → 1-up mobile
- **Dual-CTA panels**: 2-column black panels stack to single column on mobile
- **Section spacing**: 128px desktop → 64px mobile — proportional reduction

### Image Behavior
- Product photography maintains full-bleed treatment on mobile
- Crushed-can hero photos compress aspect ratio but stay edge-to-edge
- No art-direction swap — same can shots scale down rather than reframe
- Logo gold seal scales but never simplifies to a non-chrome version

---

## Agent Prompt Guide

### Quick Color Reference
- Primary CTA Background: Death Black (`#000000`)
- Primary CTA Text: Skull White (`#ffffff`)
- Inverted CTA Background: Skull White (`#ffffff`)
- Inverted CTA Text: Death Black (`#000000`)
- Hover Text: Fog Gray (`#999999`)
- Logo Accent: Logo Gold (`#d2ac5a`)
- Underlined Link Default: Bronze Gold (`#8a6d35`)
- Dark Surface Variant: Crushed Aluminum (`#151515`)
- Border: `1px solid #000000` (or `#ffffff` inverted)

### Example Component Prompts
- "Create a hero section on Death Black (`#000000`) with a full-bleed crushed-aluminum background photo. Headline at 60px Acumin Pro weight 700, uppercase, line-height 1.00, color `#ffffff`. Place a primary CTA below: white background, black text, `0px` radius, `1px` letter-spacing, weight 700 uppercase label. On hover, text fades to `#999999`."
- "Design a product card on white. Image fills card width with `0px` radius. Product name in Acumin Pro 28px weight 700 uppercase. Calorie count below in 12px weight 400. Price in 16px weight 700. No border, no shadow — let grid spacing carry the separation."
- "Build a dual-CTA black panel section. Two equal-width black (`#000000`) panels, each centered on a gold (`#d2ac5a`) embossed seal graphic with a weight 700 uppercase headline below in white ('JOIN THE CLUB' / 'SELL LIQUID DEATH'). Sharp `0px` corners, no shadows, full-width."
- "Create a newsletter modal — black panel on a dark scrim. Gold logo seal at top, white weight 700 uppercase headline, body paragraph in weight 400, single email input with `1px solid #ffffff` border and `0px` radius, white submit button with black uppercase label."
- "Design a top navigation. Solid black bar (no transparency, no blur). Gold logo on the left. Right side: weight 700 uppercase nav links in white, separated by generous spacing. On hover, links fade to `#999999`."

### Iteration Guide
1. Default to Acumin Pro weight 700 for every headline and CTA — there is no weight 500 or 600
2. Default to uppercase on all action labels and headlines — sentence-case only for body paragraphs
3. Lock display line-height at `1.00` — heroes read as dense type blocks, not airy editorial
4. Keep border-radius at `0px` for every rectangular element — no mid-range values
5. Use only `#000000` and `#ffffff` for backgrounds — `#151515` and `#232323` for dark layered surfaces
6. Hover = text fade to `#999999`, nothing else — no color shifts, no transforms, no shadow
7. Gold (`#d2ac5a`) is sacred — logo and seals only, never on buttons or body text
8. Alternate black and white sections to create chapter rhythm — every major section inverts
9. Photography (crushed cans, skulls, ice) supplies all texture — chrome stays solid-color
10. Copy voice should match the visual aggression — "MURDER YOUR THIRST" not "Stay hydrated today"
