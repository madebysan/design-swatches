---
version: alpha
name: "Fly By Jing"
description: "Token-first design system reference for Fly By Jing."

colors:
  background: "#ffffff"
  surface: "#cc0000"
  surface-elevated: "#f5f5f5"
  ink: "#000000"
  ink-muted: "#fff2d4"
  primary: "#ab2328"
  on-primary: "#ffffff"
  border: "#ffff00"
  focus-ring: "#ab2328"
  success: "#22c55e"
  warning: "#f59e0b"
  error: "#ef4444"
  shadow-soft: "#d9d9d9"

typography:
  display-hero:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 88px
    fontWeight: 400
    lineHeight: 1.05
    letterSpacing: -1px
  display:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 61px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.5px
  heading-section:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 44px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.25px
  heading-sub:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 30px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0px
  body-large:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  body:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 22px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  button-ui:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 22px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: 0px
  caption:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
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

# Fly By Jing Design System

## Overview

Fly By Jing's website is loud, hand-painted Sichuan packaging translated to web — a saturated, grocery-aisle aesthetic that refuses to apologize for color. The page slams open in deep brick red (`#ab2328` in the logo block, `#cc0000`/`#ab2328` for hero washes) with a screaming yellow (`#ffff00`) wordmark, then alternates with butter-cream sections (`#fff2d4`) and the occasional shock of forest green (`#046135`) or chili orange (`#fc521c`). Where most DTC food brands sand the edges down to beige minimalism, Fly By Jing piles on retro badges, scalloped section dividers, and condensed display type that reads like a mid-century Asian-American grocery sign reissued for the web.

The defining choice is the typography: a chunky condensed grotesque called **JeanLuc** is set everywhere from the 88px hero down to 22px button labels, almost always **UPPERCASE** with line-height locked at **0.80**. That sub-1.0 leading is the signature — headlines stack into dense blocks where the cap height of one line nearly kisses the baseline of the line above. It's the visual rhythm of vintage Chinese-American restaurant menus and bilingual storefront signage, ported to a Shopify theme. A second typeface — **Publico**, a warm transitional serif — handles every drop of body copy at 1.45 line-height, providing the editorial breathing room the headlines deliberately refuse.

What makes Fly By Jing's system distinctive is the **starburst-and-scallop ornament language**: yellow circular "WOMAN OWNED" / "ASIAN OWNED" / "BEST SELLER" badges that look stamped on, wavy scalloped strips dividing red sections from cream ones, and pill-shaped buttons (radius `9999px` or `100px`) that sit on the page like candy. Combined with full-bleed product photography (drippy chili oil, hands holding spoons, jar lids tilted for personality), the whole composition feels designed to be touched — a deliberate counter to the sterile founder-story DTC playbook.

**Key Characteristics:**
- JeanLuc condensed display at line-height 0.80 — uppercase headlines stack into dense vertical blocks
- Brick red (`#ab2328`) and chili red (`#cc0000`) as primary surfaces, never softened to maroon
- Screaming yellow (`#ffff00`) wordmark and accent — sits directly on red with no shadow or stroke
- Cream/butter (`#fff2d4`) as the alternate background, never pure white
- Retro starburst badges (yellow circles, scalloped edges) for callouts and certifications
- Pill buttons at `9999px` or `100px` radius — orange, yellow, pink, and green variants
- Wavy scalloped strips divide colored sections — never flat horizontal rules

## Colors

### Primary
- **Brick Red** (`#ab2328`): Logo background, primary brand surface, header bar. Deep saturated red — the chili paste color, not tomato.
- **Chili Red** (`#cc0000`): Section background variant for hero panels and CTA blocks. Brighter than brick red, used when the surface needs to pop forward.
- **Lantern Yellow** (`#ffff00`): Wordmark, primary headline color on red surfaces, accent type. Pure RGB yellow with no warming — the brightness is the point.

### Secondary
- **Butter Cream** (`#fff2d4`): Alternate page background, body-copy section panels, soft callout cards. The "menu paper" cream that warms anything sitting on it.
- **Forest Green** (`#046135`): Tertiary accent for "Sweet Sichuan" product variant, illustrated leaves, supportive CTAs. Deep saturation — never sage or mint.
- **Chili Orange** (`#fc521c`): Primary CTA pill button color, "fire" callouts, hot-sauce-coded variants. Sits between red and yellow on the wheel — a saturated tangerine.

### Accent / Pop
- **Sunshine Gold** (`#ffcd35`): Underline links, secondary highlights, lighter starburst variants. Warmer than lantern yellow — used when yellow on cream needs more contrast.
- **Marquee Pink** (`#cc3399`): One-off "Spicy Sweet" or seasonal product chip color. Rare but signature when it appears.
- **Sky Blue** (`#0066cc`): Reserved for inline text links inside long-form body copy. Underlined by default.

### Neutrals & Text
- **Ink Black** (`#000000`): Body copy on cream surfaces, button labels on yellow buttons, dense text. Never a softened gray.
- **Charcoal** (`rgb(27, 27, 27)`): Slightly-off-black used for button text on yellow CTAs — shaves harshness without going gray.
- **Border Gray** (`rgb(148, 149, 150)`): The only neutral border in the system, reserved for input fields. Pure mid-gray.
- **Pure White** (`#ffffff`): Reserved for headline text on red panels (when yellow would be too loud) and product card surfaces.

### Surface & Borders
- **Card Red** (`#ab2328`): Product-card background on collection pages — the cards adopt the brand red rather than fading to white.
- **Header Border** (`#e5e7eb`): Light Tailwind gray-200 used as a 1px hairline beneath the announcement bar on cream sections only.
- **CTA Border** (`#fc521c`): 2px solid orange ring on primary outline buttons — matches the fill color of solid orange CTAs.

### Gradient System
- Fly By Jing is **gradient-free in the UI**. Every fill is a flat saturated color. Gradients only appear inside product photography (chili oil glistening, drips catching light) — never in CSS. The energy comes from color clash, not gradient transition.

## Typography

### Font Family
- **Display**: `JeanLuc` — a condensed retro grotesque, used uppercase for almost every headline and button
- **Serif Body**: `Publico` — warm transitional serif for body copy, paragraph text, and editorial passages
- **Display Companion**: `Alia-Jean-Luc` and `Alia-Publico` — bilingual / variant cuts paired with the primary faces
- **System Fallback**: `Helvetica`, `Arial`, with CJK fallbacks (`Hiragino Sans GB`, `STXihei`, `Microsoft YaHei`, `WenQuanYi Micro Hei`, `Apple SD Gothic Neo`)

*Note: JeanLuc is a custom commercial face. Close substitutes: Druk Wide Condensed, GT Walsheim Condensed Bold, or Ohno Blazeface for the chunky condensed feel. For Publico: Tiempos Text or PT Serif as web-safe alternatives.*

### Hierarchy

| Role | Font | Size | Weight | Line Height | Transform | Notes |
|------|------|------|--------|-------------|-----------|-------|
| Display Hero | JeanLuc | 88px (5.50rem) | 400 | 0.80 | UPPERCASE | Landing hero — "UNLOCK 20% OFF", "ALL" |
| Display Large | Alia-Jean-Luc | 68px (4.25rem) | 400 | 1.00 | none | Editorial cross-cut — secondary hero in serif-paired layouts |
| Display Link | JeanLuc | 65.9px (4.12rem) | 400 | 0.80 | UPPERCASE | Large nav-style hero links |
| Section Heading | JeanLuc | 44px (2.75rem) | 400 | 0.80 | UPPERCASE | "WHAT WE VALUE", "OUR STORY" — section anchors |
| Sub-heading | JeanLuc | 33px (2.06rem) | 400 | 0.80 | UPPERCASE | Card titles, mid-section heads |
| Editorial Heading | Publico | 33px (2.06rem) | 400 | 1.45 | none | Serif counterpart to JeanLuc subheads — used for warmer moments |
| Button Large | JeanLuc | 29.4px (1.84rem) | 400 | 1.45 | UPPERCASE | Primary "SHOP NOW" pill button |
| Outline CTA | Alia-Jean-Luc | 20px (1.25rem) | 600 | 1.00 | none | Alternative button variant — heavier weight, mixed case |
| Body Heading | JeanLuc | 22px (1.38rem) | 400 | 0.80 / 1.45 | UPPERCASE | Card heads, badge labels, micro-titles |
| Body Large | Publico | 22px (1.38rem) | 400 | 1.45 | none | Lead paragraphs, intro text |
| Body | Publico | 19.6px (1.22rem) | 400 | 1.45 | none | Standard reading text |
| Nav / UI | Helvetica | 16px (1.00rem) | 400 | 1.00 | none | Top nav links, utility chrome |
| Caption | Arial | 14px (0.88rem) | 400 | normal | none | Metadata, badge sub-text |
| Micro | Arial | 12px (0.75rem) | 400 | normal | none | Legal, footer fine print |

### Principles
- **Line-height 0.80 is the signature**: Every JeanLuc display headline locks to 0.80 line-height. This sub-1.0 leading is what makes the type stack into dense bricks rather than airy passages — it's the central typographic decision of the brand.
- **Uppercase by default for display**: JeanLuc is set UPPERCASE almost everywhere. The condensed letterforms were drawn for caps, and lowercase appears only in paired Publico serif passages.
- **Two-typeface contrast**: JeanLuc (loud, condensed, uppercase) versus Publico (warm, serif, mixed case). The contrast does the work — there is no third display face muddying the system.
- **Yellow on red, white on red, black on cream**: Headline color follows surface color rigidly. Yellow `#ffff00` headlines on red, white `#ffffff` headlines when the type sits on dense imagery, black `#000000` on cream. Never invert.
- **Body always Publico, always 1.45**: The serif body is the breathing room. Where JeanLuc compresses to 0.80, Publico opens to 1.45 — the lungs of the page.
- **System fallback includes CJK**: The font stack carries Hiragino Sans GB, Microsoft YaHei, and Apple SD Gothic Neo — explicit recognition that the brand serves bilingual readers.

## Layout

### Spacing System
- Base unit: 11px (with 5.5px as the half-step for tight UI)
- Scale: 3.3px, 4px, 5.5px, 8px, 11px, 13.75px, 16.5px, 19.25px, 22px, 27.5px, 33px, 44px, 49.6px, 55px, 132px
- Notable: the system runs on 11s and 22s rather than 8s and 16s — every spacing value is a multiple of 5.5 or 11, giving a slightly punchier rhythm than standard Tailwind defaults.

### Grid & Container
- Max content width: ~1200–1280px for centered editorial content
- Hero: full-bleed colored panels with centered display type
- Collection grid: 2-column mobile, 3-column tablet, 4-column desktop
- Section alternation: red panel, cream panel, red panel, cream panel — chapter-like rhythm
- Marquee strip and footer always full-bleed

### Whitespace Philosophy
- **Loud over breathing**: Sections sit close together with the wavy scallop divider as the only separator. The brand prefers visual density to whitespace silence.
- **Type-locked rhythm**: 88px headlines at 0.80 line-height create their own internal density — vertical breathing room comes from section color changes, not padding.
- **Card spacing**: Product cards sit on tight 22–27px gaps. The grid feels grocery-shelf, not gallery.
- **Editorial breathing in cream zones**: When the page hits a cream section, padding opens up to 49–66px to let the Publico serif text breathe.

### Border Radius Scale
- Sharp (`2px`, `4px`): Form inputs, the announcement bar's inner email field — the only sharp corners
- Soft (`8px`, `10px`): Product cards, content cards, small panels
- Pill (`66px`, `100px`, `9999px`): Buttons, badges, call-to-action chips — the dominant radius family
- Full (`44px` on circular images, `50%` on modals): Avatars, circular product halos

The system skews heavily pill — most interactive elements round to `100px+`. Sharp corners are reserved for utility chrome (inputs, hairline borders) where roundness would feel decorative.

## Elevation & Depth

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | No shadow | Page surfaces, sections, dividers, headers |
| Inset Baseline (Level 1) | `#ffffff 0px 0px 0px 0px inset` | Pill button baseline — primes hover transition |
| Soft Drop (Level 2) | `rgba(0, 0, 0, 0.25) 0px 1px 3px 0px` | Primary CTA buttons, hovered product cards |
| Card Lift (Level 3) | `rgba(0, 0, 0, 0.1) 0px 10px 15px -3px, rgba(0, 0, 0, 0.1) 0px 4px 6px -4px` | Modal containers, popup overlays |
| Halo (Level 4) | `rgb(204, 204, 204) 0px 0px 2px 2px` | Focus states on form fields and search |

**Shadow Philosophy**: Fly By Jing is mostly flat. The brand's depth comes from color clash and stacked photography, not from CSS shadows. When shadows do appear, they're tight and grounded — `1px 3px 0.25` opacity drops that hint at the physicality of a real label peeling off a jar, never atmospheric or floating. The yellow burst badges achieve "stamped on" depth through their scalloped edges, not through shadow.

### Decorative Depth
- Photographic drips and splatters stand in for "elevation" — a bit of chili oil running down a panel does what a drop shadow would in a more minimal system
- Yellow starburst badges feel applied (sticker-like) because of their scalloped silhouette, not because of any shadow treatment
- No glassmorphism, no neumorphism, no glow — the brand is allergic to atmospheric depth

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

**Primary Orange Pill**
- Background: Chili Orange (`#fc521c`)
- Text: Lantern Yellow (`#ffff00`)
- Padding: 16px 0px (full-width pill) or 16.5px 22px (inline)
- Radius: `100px` or `9999px` (fully pill)
- Border: `2px solid #fc521c` (matches fill — visible only on hover swap)
- Shadow: `rgba(0, 0, 0, 0.25) 0px 1px 3px 0px` — subtle drop
- Font: 20–29px JeanLuc weight 400–600, often uppercase
- Hover: background flips to `#f6f6f7`, opacity 0.9
- Use: Primary CTAs — "SHOP NOW", "ADD TO CART"

**Yellow Pill**
- Background: Lantern Yellow (`#ffff00`)
- Text: Charcoal (`rgb(27, 27, 27)`)
- Padding: 16.5px 22px
- Radius: `9999px`
- Border: `0px solid #e5e7eb`
- Shadow: `#ffffff 0px 0px 0px 0px inset` — flat baseline
- Font: 29.4px JeanLuc weight 400, uppercase
- Hover: text color shifts to yellow (inverted feel)
- Use: Secondary CTAs on red panels — "JOIN THE CLUB", "GET STARTED"

**Pink Pill / Green Pill / Red Pill (Variant CTAs)**
- Background: `#cc3399` (pink), `#046135` (green), `#cc0000` (red)
- Text: White (`#ffffff`) typically, or yellow on green
- Same padding, radius, font as Yellow Pill — these are color-swapped variants
- Use: Product variant flavor codes ("Spicy Sweet" pink, "Sweet Sichuan" green, "Original" red)

**Outline CTA**
- Background: transparent or white
- Text: Chili Orange (`#fc521c`)
- Border: `2px solid #fc521c`
- Radius: `100px`
- Font: 20px Alia-Jean-Luc weight 600, mixed case
- Use: Tertiary actions, "Learn more" style links inside content

### Cards & Containers
- **Product Card**: Brick Red (`#ab2328`) background, 24–32px padding, `8px` outer radius, no border. Product jar photographed on a circular yellow burst halo. Title in JeanLuc 22–28px white uppercase line-height 0.80. Body in Publico 16px white. Full-width orange pill CTA at the bottom.
- **Cream Callout**: Butter Cream (`#fff2d4`) background, 32–48px padding, `8px` radius, no border — used inside red sections for body-copy warmth.

### Badges / Starbursts

**Yellow Starburst Badge**
- Background: Lantern Yellow (`#ffff00`) with scalloped/burst SVG edge
- Text: Black (`#000000`) or Brick Red (`#ab2328`)
- Diameter: ~80–120px
- Font: JeanLuc 14–18px uppercase, weight 400
- Layout: typically 2 lines, e.g., "WOMAN / OWNED", "BEST / SELLER"
- Use: certifications, social proof, hero callouts

**Header Marquee Pill**
- Background: variable (red, yellow, white)
- Text: contrasting, JeanLuc uppercase 14–16px
- Radius: `9999px`
- Use: "GET 20% OFF", "FREE SHIPPING ALWAYS", "JOIN THE CLUB" — the rolling top-bar announcements

### Inputs & Forms
- Background: White (`#ffffff`)
- Border: `1px solid rgb(148, 149, 150)` — neutral mid-gray
- Radius: `4px` — the only mid-range radius in the system
- Padding: `0px 0px 0px 16px`
- Font: 16px Helvetica or system, weight 400
- Text color: Black (`#000000`)
- Focus: outline `rgb(0, 0, 0) auto 2px`, border shifts to brand accent
- Use: email signup, search, checkout fields

### Navigation
- Top header: Brick Red bar (`#ab2328`) with yellow JeanLuc wordmark centered
- Above the header: announcement marquee strip — black bar with rotating yellow promotional pills
- Nav links: 16px JeanLuc-or-Helvetica uppercase, white text on red, generous spacing
- Hover: text color flips to yellow or black depending on contrast need
- Sticky behavior: header pins to top, marquee scrolls away

### Decorative Elements
- **Wavy Scallop Divider**: full-bleed ~24px yellow scalloped SVG strip separating red sections from cream — the visual hand-off between brand zones
- **Drip / Splatter Imagery**: photographic chili oil drips on colored backgrounds — always real photography, never illustrated
- **Full-Bleed Product Photography**: hero shots of jars, drippy oil, spoons, hands — no scrim, no shadow, raw imagery with display type laid directly on top

## Do's and Don'ts

### Do
- Set every JeanLuc display headline at line-height **0.80** — sub-1.0 leading is the brand's signature
- Use uppercase for all JeanLuc display and button text — the typeface was drawn for caps
- Pair condensed JeanLuc display with warm Publico serif body — the contrast IS the system
- Default to brick red (`#ab2328`) and butter cream (`#fff2d4`) as your two primary surfaces
- Use lantern yellow (`#ffff00`) for headlines on red and accent badges — never tone it warmer
- Apply pill radius (`100px` or `9999px`) on every button — sharp corners are for inputs only
- Alternate red panels and cream panels with wavy scallop dividers between them
- Use real photography for drips, oils, and product hero moments — never illustrated drips
- Keep starburst badges as flat yellow circles with scalloped edges — sticker-like, not skeuomorphic

### Don't
- Don't soften brick red to maroon or burgundy — `#ab2328` and `#cc0000` are the saturation targets
- Don't use Publico for headlines or JeanLuc for body — keep the two-face contract strict
- Don't introduce a third display typeface — JeanLuc + Publico is the entire system
- Don't add gradients to surfaces — every fill is flat. Gradients only live inside product photography.
- Don't use line-height greater than 1.00 on JeanLuc display — the dense stack is the brand
- Don't use mid-range button radius (16–32px) — radius is binary: sharp inputs or full pills
- Don't use atmospheric drop shadows — depth comes from color clash and photography, not CSS lift
- Don't use lowercase JeanLuc — the condensed letterforms break down out of caps
- Don't pair yellow text with cream backgrounds — yellow is exclusively for red surfaces
- Don't replace photographic drips with SVG illustrations — the drips must look real

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile Small | <375px | Single column, hero drops to 44–55px, marquee shortens |
| Mobile | 375–640px | Single column, 55–68px hero, stacked product cards 1–2 wide |
| Tablet | 640–989px | 2-column product grid, 68–77px hero, side-by-side editorial pairs |
| Desktop | 990–1280px | 3-column product grid, 77–88px hero, full marquee strip |
| Wide Desktop | ≥1280px | 4-column product grid, full 88px hero, 1280–1536px container |

### Touch Targets
- Primary pill CTAs: minimum 44px tap height, generous horizontal padding
- Header nav links: 44px minimum touch zone with comfortable spacing
- Product card "SHOP NOW" buttons: full-width inside card on mobile

### Collapsing Strategy
- **Header**: Wordmark stays centered; nav links collapse into a hamburger drawer on mobile
- **Marquee strip**: Pills compress and continue scrolling — never hidden, the brand needs the noise
- **Hero**: 88px → 68px → 55px → 44px progressive scaling; line-height 0.80 maintained
- **Product grid**: 4-col → 3-col → 2-col → 1-col cascade
- **Section dividers**: Wavy scallops scale proportionally; never replaced with flat rules
- **Cream/red alternation**: Section rhythm preserved across all breakpoints

### Image Behavior
- Full-bleed product photography stays full-bleed on mobile — no letterboxing
- Drippy hero imagery crops aggressively on small screens — focal jar stays centered
- Yellow starburst badges scale with content but never shrink below 60px diameter
- Wordmark scales but never reduces to icon-only — "FLY BY JING" must remain readable

---

## Agent Prompt Guide

### Quick Color Reference
- Primary Surface: Brick Red (`#ab2328`)
- Hot Surface: Chili Red (`#cc0000`)
- Accent Surface: Butter Cream (`#fff2d4`)
- Headline on Red: Lantern Yellow (`#ffff00`)
- Headline on Cream: Ink Black (`#000000`)
- Primary CTA: Chili Orange (`#fc521c`) with yellow text
- Secondary Accent: Forest Green (`#046135`), Sunshine Gold (`#ffcd35`)
- Drop Shadow (rare): `rgba(0, 0, 0, 0.25) 0px 1px 3px 0px`

### Example Component Prompts
- "Create a hero section on Brick Red (`#ab2328`) with an 88px JeanLuc uppercase headline at line-height 0.80, color Lantern Yellow (`#ffff00`). Below it, 22px Publico body in white at line-height 1.45. Add a Chili Orange (`#fc521c`) pill CTA — `100px` radius, 20px Alia-Jean-Luc weight 600, white-to-yellow text, `2px solid #fc521c` border, drop shadow `rgba(0, 0, 0, 0.25) 0px 1px 3px 0px`."
- "Design a product card on Brick Red (`#ab2328`) background, `8px` radius, no border. Center a product jar image on a yellow circular halo. Title in JeanLuc 22px uppercase white at line-height 0.80. Price in Publico 16px white. Full-width orange pill CTA at the bottom with yellow JeanLuc 22px uppercase 'SHOP NOW' text."
- "Build a yellow starburst badge — `#ffff00` circle, ~100px diameter, scalloped SVG edge. Text in JeanLuc 14–16px uppercase weight 400, two lines like 'WOMAN / OWNED' or 'BEST / SELLER'. Center on dark imagery or red panels."
- "Create an announcement marquee strip — full-bleed black bar at the top with rotating pills inside. Each pill: `9999px` radius, JeanLuc 14px uppercase, alternating yellow / white / red backgrounds. Content like 'GET 20% OFF · FREE SHIPPING ALWAYS · JOIN THE CLUB'."
- "Design a cream-section editorial card on Butter Cream (`#fff2d4`) with 49px padding, `8px` radius. Heading in JeanLuc 44px uppercase ink black at line-height 0.80. Body in Publico 22px black at line-height 1.45. Optional inline link in Sky Blue (`#0066cc`) underlined."

### Iteration Guide
1. **Line-height 0.80 is non-negotiable** for JeanLuc display sizes — if it feels too tight, you're doing it right
2. Default to brick red + cream as the two-surface system; introduce green or pink only as variant accents
3. Yellow `#ffff00` headlines exclusively on red. On cream, use ink black. Never mix.
4. Buttons round to `100px` or `9999px` — sharp corners are for inputs and hairlines only
5. Pair JeanLuc uppercase display with Publico mixed-case serif body — never break the contract
6. Use real photographic drips, oils, and hands — illustrated drips read as fake
7. Yellow scalloped starbursts are the sticker layer — keep them flat, never add depth shadows
8. Section rhythm: red → wavy yellow scallop → cream → wavy yellow scallop → red. Don't dilute with neutral gray transitions.
9. Pill button text is uppercase JeanLuc 20–29px — never weight under 400, never lowercase
10. Spacing scale runs on 11s and 22s, not 8s and 16s — multiples of 5.5 give the brand its punchier rhythm
