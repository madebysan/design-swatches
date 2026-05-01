# Design System Inspired by Frame.io

## 1. Visual Theme & Atmosphere

Frame.io's website is a video editor's color grade rendered as a marketing site: deep, neutral, and cinematic. The page opens on near-black (`#000000`) with subsequent sections shifting into a slightly lifted navy-black (`#0D0D18`) — the kind of two-step dark you see in Resolve or Premiere panel chrome. Every surface, card, and panel sits inside a calibrated dark range from `#000` to `#12131D`, and almost all primary text reads in an off-white (`#FCFCFC`) that's been deliberately pulled back from pure white to avoid retina burn during long review sessions. The whole composition feels like opening a professional NLE timeline at 11pm.

The display typography is what announces Frame.io as a serious tool. Hero headlines use **FrameGothic** at 80px, weight 600, with aggressive negative tracking (`-3.6px` at the H1, `-1.92px` at the H2 size of 48px). FrameGothic is a custom variable-grotesk built specifically for the brand — sharp shoulders, generous x-height, and the wide-open apertures you need when type sits over moving footage. The secondary typeface is **NeueMachinaInktrap**, deployed almost exclusively for eyebrow labels at 12px with positive `0.72px` tracking and uppercase styling. The contrast is intentional: Machina's inktrap detailing feels mechanical and instrument-panel-like, while FrameGothic carries the editorial weight. Body copy runs FrameGothic at 14–15px in a half-opacity off-white (`rgba(234, 234, 255, 0.5)`), creating a soft hierarchy where headlines lock in and supporting copy steps quietly back.

What distinguishes Frame.io most is its **chromatic restraint plus one cinema-monitor blue**. The accent — `#6199F6`, a slightly desaturated cobalt — appears on the "MOST POPULAR" plan markers, "Save 13%" subscription badges, and the inset glow on the dark hero device frame. There's also a deeper Adobe-adjacent violet (`#5B53FF` / `#5237F9`) reserved for promotional banners (the announcement strip across the top), tying the site visually back to Adobe Creative Cloud without dominating the palette. The signature depth treatment isn't a drop shadow — it's a **layered inset glow**, like a screen behind glass, where blue light bleeds through the frame edges of product mockups. Combined with fully-pill (`100px`) CTAs, sharply-cornered display type, and full-bleed product imagery on dark surfaces, the system reads as professional broadcast software dressed for a pitch deck.

**Key Characteristics:**
- Two-tier dark palette: pure black canvas (`#000000`) with `#0D0D18` secondary surface for cards and panels
- FrameGothic at weight 600 for all display type — confident, wide, and tracked tight
- NeueMachinaInktrap for uppercase eyebrows at 12px with `0.72px` positive tracking — the mechanical counterpoint
- Off-white text (`#FCFCFC`) over pure black for cinema-monitor neutrality
- Half-opacity body copy (`rgba(234, 234, 255, 0.5)`) — quiet supporting hierarchy
- Cobalt accent (`#6199F6`) for status badges and inset hero glows — the only true chromatic
- Adobe violet (`#5B53FF`) reserved for promo bars and ownership cues
- Pill CTAs (`100px` radius) with off-white fill and pure black text — the primary trial button
- Layered inset shadows that glow blue from inside product frames — the depth signature
- Aggressive negative letter-spacing scaling to `-3.6px` at 80px display

## 2. Color Palette & Roles

### Primary
- **Frame Black** (`#000000`): Page canvas, navigation backdrop, marquee hero sections. Pure black — the system commits.
- **Frame Navy** (`#0D0D18`): Secondary surface — pricing cards, feature panels, footer. A near-black with a faint blue cast that reads as "elevated black" against the pure-black canvas.
- **Frame Off-White** (`#FCFCFC`): Primary text, primary CTA fill. Pulled 3 points off pure white — easier on the eye on dark, identical-looking on light.

### Brand Accent
- **Frame Cobalt** (`#6199F6`): The signature accent. Used on "MOST POPULAR" plan stamps, "Save 13%" subscription badges, inset hero glows, and selected-state markers. Cinema-monitor blue, slightly desaturated.
- **Cobalt Inset Glow** (`rgba(97, 153, 246, 0.1)`): The 10%-opacity tinted glow inside hero device frames — `0px 4px 74px 30px inset`.
- **Adobe Violet** (`#5B53FF`): Promotional announcement bar fill — top-of-page "Talk to sales" strip. Ties to Creative Cloud branding.
- **Deep Adobe Violet** (`#5237F9`): Hover state and emphasized variant of the violet — appears on inverted promo CTAs.

### Neutrals & Text
- **Primary Text** (`#FCFCFC`): Headlines, body, primary CTA labels, navigation links.
- **Body Muted** (`rgba(234, 234, 255, 0.5)`): Half-opacity supporting body copy — secondary descriptions, feature list text. The hierarchy workhorse.
- **Body Soft** (`rgba(233, 233, 255, 0.7)`): 70%-opacity intermediate text — disclaimers, secondary nav.
- **Cool Gray** (`#81859F`): Disabled state, fine-print metadata, currency labels in pricing.
- **Text Light Tint** (`#D5D6EA`): Eyebrow labels in alternate light contexts, selected-state link color.
- **Sign-In Text** (`#F5F5F8`): A faintly cooler off-white reserved for nav "Sign In" — subtly cooler than primary text to recede from CTAs.

### Surface & Borders
- **Card Surface** (`#0D0D18`): Pricing tier cards, feature panels.
- **Card Surface Lifted** (`#12131D`): Sticky CTA bar at section bottoms — slightly more lifted than card surface.
- **Surface Tint** (`rgba(157, 157, 255, 0.05)`): 5%-opacity violet wash for soft container fills inside dark cards.
- **Surface Highlight** (`rgba(189, 189, 244, 0.1)`): Hover tint on card-inner CTAs.
- **Surface Stroke** (`rgba(209, 209, 251, 0.2)`): Hairline border for divider rules and card edges.
- **Light Surface** (`#F0F0F7`): Rare inverted moments — cookie banner, certain modal chrome.

### Shadow & Inset Glow
- **Layered Drop Stack** (six-stop cascade): `rgba(0, 0, 0, 0.31) 84.68px 149.711px 80px 0px, rgba(0, 0, 0, 0.26) 54.885px 97.035px 46.852px 0px, rgba(0, 0, 0, 0.23) 32.618px 57.666px 25.481px 0px, rgba(0, 0, 0, 0.2) 16.936px 29.942px 13px 0px, rgba(0, 0, 0, 0.18) 6.9px 12.199px 6.519px 0px, rgba(0, 0, 0, 0.2) 1.568px 2.772px 3.148px 0px`. Six progressively-tightening drops simulate atmospheric depth on dark.
- **Inset Navy Glow** (`rgb(24, 24, 38) 12px 12px 50px 0px inset`): A self-glow inside dark device frames.
- **Inset Cobalt Glow** (`rgba(97, 153, 246, 0.1) 0px 4px 74px 30px inset`): Blue-light bleed from inside the hero product mockup.
- **Soft Halo** (`rgba(0, 0, 0, 0.5) 0px 0px 16px 0px`): Localized darken under floating UI on bright backgrounds.

### Gradient System
- Frame.io is largely **gradient-free in surfaces** but uses tonal step-downs across full-bleed sections — pure black hero → `#0D0D18` feature blocks → `#0E0F20` secondary panels — to simulate camera-DOF depth. The only true gradient moment is the **violet promotional bar**, where `#5B53FF` sits unmodulated as a flat color. Inset glow effects (cobalt and navy) function as the system's gradient substitute, casting color *into* surfaces rather than across them.

## 3. Typography Rules

### Font Family
- **Display**: `FrameGothic, "FrameGothic Fallback", Arial, sans-serif` — custom variable grotesk used for all headings, primary body, and most UI labels
- **Eyebrow / Mechanical**: `NeueMachinaInktrap, "NeueMachinaInktrap Fallback"` — uppercase eyebrow labels and small UI markers
- **Fallback Stack**: `Arial, sans-serif` — graceful degradation, never visible in production

*Note: FrameGothic and NeueMachinaInktrap are bespoke / commercial typefaces. For external implementations, **Söhne** or **Neue Haas Grotesk Display** at weights 500–600 substitute well for FrameGothic; **PP Neue Machina** (the public Pangram Pangram release) is the exact source for the inktrap variant.*

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Display Hero (H1) | FrameGothic | 80px (5.00rem) | 600 | 83.2px (1.04) | -3.6px | Maximum size — landing hero ("One platform for all your creative work.") |
| Display Large (H2) | FrameGothic | 48px (3.00rem) | 600 | 48.96px (1.02) | -1.92px | Section heads ("Features", "Plans designed for how you work.") |
| Display Medium (H3) | FrameGothic | 38px (2.38rem) | 600 | 44.08px (1.16) | -1.33px | Sub-section heads ("Start using Frame.io", FAQ heads) |
| Display Quote (H2 alt) | FrameGothic | 32px (2.00rem) | 600 | 35.2px (1.10) | normal | Pull quotes, testimonial heads |
| Body Large | FrameGothic | 18px (1.13rem) | 400 | 27px (1.50) | normal | Hero subhead, intro paragraphs |
| Body | FrameGothic | 16px (1.00rem) | 400 | 24px (1.50) | normal | Standard reading text |
| Body Small | FrameGothic | 15px (0.94rem) | 400–500 | 19.5px (1.30) | normal | Feature card body, secondary descriptions |
| Body Tight | FrameGothic | 14px (0.88rem) | 400–600 | 21.75px (1.55) | 0.14px | Nav links, button labels — note the `0.14px` positive tracking |
| Caption | FrameGothic | 13–13.33px | 400 | 18.85px (1.42) | normal | Metadata, fine-print disclaimers |
| UI Eyebrow | NeueMachinaInktrap | 12px (0.75rem) | 400 | 10.8px (0.90) | 0.72px | Uppercase section markers ("PRODUCT", "FOR PROFESSIONALS") |
| Micro Label | FrameGothic | 10px | 400 | 10px (1.00) | normal | Footer legal, micro-chrome |

### Principles
- **Negative tracking scales aggressively with size**: from `-3.6px` at the 80px H1 down to `-1.92px` at 48px and `-1.33px` at 38px. Below 24px, tracking returns to normal. This locks display type into dense, optically-corrected blocks where letter shapes nearly touch.
- **Weight 600 is the display ceiling**: every heading runs 600 — never 700 or 800. Frame.io's confidence is in the geometry of the typeface, not the weight.
- **The 12px Machina eyebrow is sacred**: every section is announced with a NeueMachinaInktrap eyebrow at 12px, weight 400, uppercase, `0.72px` tracking, line-height `0.9`. It's the system's signature — never use FrameGothic at this size for the same role.
- **Half-opacity body for hierarchy**: secondary body copy uses `rgba(234, 234, 255, 0.5)` rather than a separate gray color. This creates a perceptual recession where body text feels "behind glass" relative to headlines.
- **Tight display line-height (1.02–1.16)**: headline blocks lock vertically, reading more like a logotype than a paragraph. Body text breathes at 1.50.
- **Two-weight discipline**: weight 400 for body and most chrome, weight 600 for display and emphasized UI labels. Weight 500 appears occasionally on small card headings (15px). No weight 700+ anywhere.

## 4. Component Stylings

### Buttons

**Primary White Pill (Trial CTA)**
- Background: Frame Off-White (`#FCFCFC`)
- Text: Frame Black (`#000000`)
- Padding: `0px 24px` (with 40px implicit height)
- Radius: `100px` (fully pill)
- Border: none
- Font: 14px FrameGothic weight 600, letter-spacing `0.14px`
- Hover: subtle opacity drop (~95%) — no shape or color shift
- Use: The *one* primary CTA — "Start Free Trial" in the top nav and hero. Exactly one per screen.

**Ghost Pill (Secondary Nav CTA)**
- Background: transparent
- Text: Frame Off-White (`#FCFCFC`)
- Padding: `0px 24px`
- Radius: `100px`
- Border: none (the pill is implied by hover state)
- Font: 14px FrameGothic weight 600, letter-spacing `0.14px`
- Use: "Contact Us", secondary nav actions sharing the same row as the trial CTA

**Adobe Violet Promo Bar CTA**
- Background: Adobe Violet (`#5B53FF` / `#5237F9` on hover)
- Text: Frame Off-White (`#FCFCFC`)
- Padding: full-bleed announcement strip
- Radius: `0px` (the bar itself; CTAs inside use pill `100px`)
- Font: 13–14px FrameGothic weight 400–600
- Use: Top-of-page promotional bar — "Talk to sales: 877-702-3623"

**Cobalt Status Badge**
- Background: Frame Cobalt (`#6199F6`)
- Text: Frame Black (`#000000`)
- Padding: `3px 12px 1px` (asymmetric — 1px less on bottom for optical centering)
- Radius: `100px`
- Font: 12px FrameGothic weight 600
- Use: "Save 13%", "MOST POPULAR" — system status markers

**Sticky Footer CTA Bar**
- Background: `#12131D` (lifted card surface)
- Text: Frame Off-White (`#FCFCFC`)
- Padding: `24px` vertical
- Radius: `20px 20px 0px 0px` (top corners only, anchored to viewport bottom)
- Use: Persistent "Sign Up Now" / "Start Free Trial" anchored bar on long pricing pages

**Carousel Nav Circle**
- Background: transparent or `rgba(13, 13, 24, 0.1)`
- Size: ~40px × 40px
- Radius: `50%` (true circle)
- Border: hairline `rgba(209, 209, 251, 0.2)`
- Use: "Go to previous slide" / next-slide carousel navigation

### Cards & Containers
- Background: `#0D0D18` (Frame Navy) for pricing tier cards and feature panels
- Border: hairline `rgba(209, 209, 251, 0.2)` 1px — visible but recessive
- Radius: `10px` for pricing cards; `24px` for hero feature blocks; rare `12px` for inline content cards
- Padding: 24–48px internal — generous for pricing cards, tighter for feature grids
- Shadow: typically none on cards; the layered drop stack reserved for floating product mockups
- Hover: faint surface lift to `rgba(189, 189, 244, 0.1)` overlay; border brightens to `rgba(233, 233, 255, 0.7)`

### Badges / Tags / Pills
**Cobalt Status Pill**
- Background: Frame Cobalt (`#6199F6`)
- Text: Frame Black (`#000000`)
- Radius: `100px`
- Padding: `3px 12px 1px`
- Font: 12px FrameGothic weight 600
- Use: "MOST POPULAR", "Save 13%"

**Surface Tint Pill**
- Background: `rgba(157, 157, 255, 0.05)`
- Text: Frame Off-White (`#FCFCFC`)
- Border: `rgba(209, 209, 251, 0.2)` 1px
- Radius: `100px`
- Use: Toggle indicators (e.g., Monthly / Annually selector)

### Inputs & Forms
- Background: `#0D0D18` or transparent on dark surface
- Border: `rgba(209, 209, 251, 0.2)` 1px
- Radius: `9.33px` (the `0.583rem` quirk) or `10px`
- Font: 14–15px FrameGothic weight 400, color `#FCFCFC`
- Placeholder: `rgba(234, 234, 255, 0.5)` (matches body-muted)
- Focus: border brightens to Frame Cobalt (`#6199F6`); no ring halo, just a hue shift
- Padding: 12–16px vertical, 16–24px horizontal

### Navigation
- Top nav: pure black bar, fixed at top, ~64px tall
- Logo: angle-bracket Frame.io mark at left (the inverted-triangle emblem)
- Center links: "Features", "Enterprise", "Resources", "Pricing" — 14px FrameGothic weight 600, color `#FCFCFC`, `0.14px` tracking
- Right group: "Contact Us" (ghost pill) → "Sign In" (text only, color `#F5F5F8`) → "Start Free Trial" (white pill) → Adobe corner mark
- Hover: text shifts toward `rgba(233, 233, 255, 0.7)`; underline never appears
- Promo bar: full-width Adobe Violet (`#5B53FF`) strip stacked above the nav with a phone-number CTA and a small dismiss `×`

### Decorative Elements

**Inset Cobalt Glow**
- `rgba(97, 153, 246, 0.1) 0px 4px 74px 30px inset` paired with `rgb(24, 24, 38) 12px 12px 50px 0px inset`
- Applied to: hero device mockups, product UI screenshots framed inside dark cards
- Effect: a soft blue light bleeds in from the screen edge, mimicking a calibrated reference monitor in a dim grading suite

**Layered Atmospheric Drop**
- Six progressively-blurred drops (`84px → 1.5px` blur cascade) with offset y values from 149px down to 2px
- Applied to: floating hero mockups that need to read as physically suspended above the canvas
- Effect: room-scale atmospheric depth — the kind of shadow a real object casts in low-key studio lighting

**Full-Bleed Product Imagery**
- Product UI screenshots fill the viewport edge-to-edge inside dark sections, often with a faint `#0D0D18` vignette at the corners
- No frosted glass, no decorative chrome — the product is shown as it is, with the inset glow doing the heavy lifting

## 5. Layout Principles

### Spacing System
- Base unit: 8px, with `4px` and `2px` micro-units for badge padding adjustments
- Scale: 2px, 4px, 8px, 12px, 16px, 24px, 32px, 48px, 64px, 96px, 128px
- Notable: Frame.io leans on the `24px` and `48px` rungs heavily — section padding tends to be `48–96px` on desktop, dropping to `24–48px` on mobile. The asymmetric `3px 12px 1px` button padding is intentional optical correction for FrameGothic's baseline.

### Grid & Container
- Max content width: ~1200px with generous outer gutters
- Hero: full-width left-aligned headline with right-side product imagery overflowing the container
- Pricing: 4-column equal-width plan card grid at desktop, collapsing to 2-up tablet, 1-up mobile
- Feature sections: alternating left/right text-vs-imagery rhythms with full-bleed dark backgrounds
- Footer: dense 5–6 column link grid at the bottom

### Whitespace Philosophy
- **Cinematic pacing**: Sections are paced like film acts — long establishing shots (hero, big imagery) followed by tight cut-rhythm (feature grids). Vertical rhythm runs 96–160px between major sections at desktop.
- **Eyebrow → headline → body triplet**: Every major block opens with a 12px Machina eyebrow, drops 12–16px to the FrameGothic display headline, then 24–32px to body — a consistent vertical signature.
- **Tonal section breaks**: Rather than dividing rules, Frame.io shifts surface color (`#000` → `#0D0D18` → `#0E0F20`) to chapter the page. The eye reads the tonal shift before it reads the headline.

### Border Radius Scale
- Sharp (0px): Promo bars, full-bleed sections, occasional UI chrome
- Small (1–2px): Accent dividers and rare hairline frames
- Medium (10–12px): Pricing cards, feature panels, inline content cards
- Large (20–24px): Hero feature blocks, sticky footer bars (top-only `20px 20px 0px 0px`)
- Pill (100px): Every primary, secondary, and badge button — the brand's interactive radius
- Circle (50% / 100%): Carousel nav, avatars, certain icon buttons

## 6. Depth & Elevation

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | No shadow | Page canvas, body text, footer surfaces |
| Tonal Lift (Level 1) | Surface color shift `#000 → #0D0D18` | Card surfaces, feature panels — depth via tone, not shadow |
| Card Edge (Level 2) | `rgba(209, 209, 251, 0.2) 0px 0px 0px 1px` hairline | Pricing cards, content panels — edge definition without elevation |
| Inset Navy Glow (Level 3) | `rgb(24, 24, 38) 12px 12px 50px 0px inset` | Inside device frames — self-illumination |
| Inset Cobalt Glow (Level 4) | `rgba(97, 153, 246, 0.1) 0px 4px 74px 30px inset` (paired with Level 3) | Hero product mockup — the signature reference-monitor glow |
| Atmospheric Drop (Level 5) | Six-stop cascade from `1.5px` to `84px` blur | Floating product mockups, hero hardware — room-scale depth |

**Shadow Philosophy**: Frame.io's depth system is **photographic, not graphic**. Where Cape uses hard offset stamps and most marketing sites use a single 0/4/12 generic drop, Frame.io stacks six progressively-tightening drops to simulate the actual light falloff of a real object suspended in front of a dark studio backdrop. The cascade was almost certainly handed off as a Figma effect from the brand team, not authored by an engineer. The other depth signature — the **inset cobalt glow** — does the opposite work: instead of pushing the element forward, it pulls light *into* the surface, making the screen-within-the-image appear as if it's actually on. Together, these two systems give every product mockup a sense of being a real device in a real room rather than a flat PNG on a canvas.

### Decorative Depth
- Inset glows pair with the layered atmospheric drop on the same element — the device floats in the room (drop) and is internally lit (inset)
- Tonal surface shifts replace borders for most section divisions — the page chapters itself through value, not lines
- No ambient glow effects on body content; the depth treatment is reserved for product imagery and rarely buttons

## 7. Do's and Don'ts

### Do
- Use FrameGothic at weight 600 with aggressive negative tracking (`-1.92px` to `-3.6px`) for all display sizes
- Open every major section with a 12px NeueMachinaInktrap eyebrow, uppercase, `0.72px` tracking
- Apply `#FCFCFC` (off-white) for primary text, never pure white — the 3-point pullback is intentional
- Use `rgba(234, 234, 255, 0.5)` half-opacity off-white for body copy hierarchy
- Reserve Frame Cobalt (`#6199F6`) for status badges and inset hero glows — one or two applications per screen
- Use `100px` pill radius for every CTA — the system's interactive shape signature
- Stack tonal surfaces (`#000 → #0D0D18`) to chapter the page — depth via value, not rules
- Pair inset cobalt glow with inset navy glow inside product device frames — the screen-on-in-a-dark-room effect
- Keep the white-pill primary CTA truly singular — one "Start Free Trial" per screen, top-right
- Apply atmospheric six-stop drop shadows for floating product hardware

### Don't
- Don't use weight 700+ on FrameGothic — weight 600 is the ceiling
- Don't use FrameGothic at 12px for eyebrow labels — that role belongs exclusively to NeueMachinaInktrap
- Don't use pure white (`#FFFFFF`) for text — always Frame Off-White (`#FCFCFC`)
- Don't introduce gradient fills on surfaces — depth is achieved via tonal stepping and inset glows
- Don't use mid-radius values (4–8px) on CTAs — the system is binary on buttons (sharp `0px` or full pill `100px`)
- Don't apply Frame Cobalt as a button background fill — it's a status accent, not a CTA color
- Don't saturate dark surfaces with multiple cobalt elements — one accent moment per fold
- Don't use bold weight inside the announcement bar — keep it 400–600 only
- Don't put hairline borders on top of inset glows — let the glow define the edge
- Don't use hard offset shadows (`-4px 4px 0`) — Frame.io's signature is atmospheric, not graphic

## 8. Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile Small | <375px | Single-column, hero drops to 40–48px |
| Mobile | 375–640px | Single-column, 48–56px hero, stacked CTAs |
| Tablet | 640–1024px | 2-column pricing grid, 56–64px hero |
| Desktop | 1024–1280px | 4-column pricing grid, 72px hero |
| Large Desktop | ≥1280px | Full 80px H1 with `-3.6px` tracking, max 1200px container |

### Touch Targets
- Pill CTAs: min 40px height, `100px` radius preserved across all breakpoints
- Nav links: 44px tap target with generous padding
- Carousel nav circles: 40px min, 50% radius
- Promo bar dismiss `×`: 32px tap target

### Collapsing Strategy
- **Nav**: Center link group collapses to hamburger on tablet and below; right-side trial CTA persists
- **Hero**: 80px → 56px → 48px → 40px progressive scaling, weight 600 maintained throughout
- **Pricing grid**: 4-up → 2-up → 1-up cascade; "MOST POPULAR" cobalt badge persists at every breakpoint
- **Letter-spacing**: Tracking scales proportionally — `-3.6px` at 80px reduces to `-2px` at 56px and `-1.6px` at 48px
- **Feature alternation**: Left/right text-vs-imagery pairs collapse to stacked image-on-top, text-below
- **Section padding**: 96–128px desktop → 48–64px mobile

### Image Behavior
- Hero product mockup remains full-bleed at every breakpoint, but the inset cobalt glow scales its blur radius proportionally (74px → 32px on mobile)
- Six-stop atmospheric drop simplifies to a single 32px blur on mobile to reduce paint cost
- No art direction changes — the same dark visual language scales without alternate compositions
- Wordmark logo never becomes icon-only; the angle-bracket emblem and "frame.io" wordmark stay paired

## 9. Agent Prompt Guide

### Quick Color Reference
- Page Canvas: Frame Black (`#000000`)
- Card Surface: Frame Navy (`#0D0D18`)
- Lifted Surface: Frame Surface Lifted (`#12131D`)
- Primary Text: Frame Off-White (`#FCFCFC`)
- Body Muted: `rgba(234, 234, 255, 0.5)`
- Accent: Frame Cobalt (`#6199F6`)
- Promo Violet: Adobe Violet (`#5B53FF`)
- Card Border: `rgba(209, 209, 251, 0.2)`
- Inset Cobalt Glow: `rgba(97, 153, 246, 0.1) 0px 4px 74px 30px inset`
- Inset Navy Glow: `rgb(24, 24, 38) 12px 12px 50px 0px inset`
- Layered Atmospheric Drop: six-stop cascade ending `rgba(0, 0, 0, 0.31) 84.68px 149.711px 80px 0px`

### Example Component Prompts
- "Create a hero section on Frame Black (`#000000`) with a 12px NeueMachinaInktrap eyebrow in `#FCFCFC` reading 'PRODUCT' (uppercase, `0.72px` tracking, line-height `0.9`). Below it, a 80px FrameGothic headline weight 600 in `#FCFCFC`, line-height `1.04`, letter-spacing `-3.6px`. Add a primary white pill CTA — `#FCFCFC` background, `#000000` text, `100px` radius, padding `0px 24px`, 14px FrameGothic weight 600, `0.14px` letter-spacing."
- "Design a pricing card on Frame Navy (`#0D0D18`) with `10px` radius and a `rgba(209, 209, 251, 0.2)` 1px border. Top of card: 12px NeueMachinaInktrap eyebrow in `#FCFCFC` reading 'FOR PROFESSIONALS' (uppercase, `0.72px` tracking). Plan name in 24px FrameGothic weight 600. Price in 48px FrameGothic weight 600 with `-1.92px` tracking. The MOST POPULAR card carries a Frame Cobalt (`#6199F6`) pill badge at the top with `#000000` text, padding `3px 12px 1px`, `100px` radius, 12px FrameGothic weight 600."
- "Build a hero product mockup floating in front of Frame Black. Apply a layered drop shadow stack ending `rgba(0, 0, 0, 0.31) 84.68px 149.711px 80px 0px`. Inside the device frame, apply two inset glows: `rgb(24, 24, 38) 12px 12px 50px 0px inset` for the navy fall-off and `rgba(97, 153, 246, 0.1) 0px 4px 74px 30px inset` for the blue screen-light bleed."
- "Create an Adobe Violet (`#5B53FF`) full-width promotional bar pinned to the top of the viewport. Centered text 'Talk to sales: 877-702-3623' in 14px FrameGothic weight 600, color `#FCFCFC`. Right-aligned dismiss `×` icon. Bar height ~36px, no radius, no shadow."
- "Design a Monthly/Annually toggle on Frame Navy. Capsule container `rgba(157, 157, 255, 0.05)` background with `100px` radius and a `rgba(209, 209, 251, 0.2)` border. Active state slides a Frame Cobalt (`#6199F6`) pill behind the selected option with a 'Save 13%' badge — `#6199F6` background, `#000000` text, padding `3px 12px 1px`."

### Iteration Guide
1. Default to FrameGothic weight 600 for every display size — no weight 700+, no weight 500 in headlines
2. Open every section with a 12px NeueMachinaInktrap eyebrow at `0.72px` tracking, uppercase — never use FrameGothic for this role
3. Negative tracking scales with size: `-3.6px` at 80px, `-1.92px` at 48px, `-1.33px` at 38px, `normal` below 24px
4. Use `#FCFCFC` for all primary text — pure white is reserved for nothing
5. Body copy hierarchy uses `rgba(234, 234, 255, 0.5)` opacity rather than a separate gray color
6. Frame Cobalt (`#6199F6`) is sacred — status badges and inset glows only, never as a button fill
7. Every CTA is a `100px` pill — no exceptions, no alternate radii on buttons
8. Tonal surface stepping (`#000 → #0D0D18 → #12131D`) replaces borders for section breaks
9. Pair inset cobalt + inset navy glows inside product device frames for the screen-on effect
10. The white-pill "Start Free Trial" is singular — exactly one per screen, never duplicated
