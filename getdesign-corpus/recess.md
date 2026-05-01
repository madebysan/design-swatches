# Design System Inspired by Recess

## 1. Visual Theme & Atmosphere

Recess's website is a calm-down room rendered as a webpage. The entire experience floats on a single saturated periwinkle field (`#a8b2ff`) that doubles as both background and brand — a deliberately maximalist commitment to one color where most CPG sites stretch for a palette. Everything else (typography, buttons, footer, cards) is built in deep midnight blue (`#25385b`) on top of that periwinkle, with soft cream (`#fffcef`), pink, peach, and apricot blobs appearing as watercolor accents. The result reads less like a beverage e-commerce site and more like a wellness app — a brand that sells "an antidote to modern life" and styles its storefront accordingly.

The custom `Sharp Grotesk Web` typeface anchors the system. Display headlines run heavy at weight 500 with a 1.25 line-height and lowercase styling — never SHOUTING, always whispering. Body text holds at 18–20px weight 400/500, with section headlines stepping up to 80px on the hero. The lowercase rhythm ("relax & unwind with Recess", "why we made Recess") feels like a meditation app's onboarding copy, not a CPG pitch. There is no all-caps display type anywhere except small UI chrome.

What distinguishes Recess most is its **stamp-style button system** combined with **watercolor blob backgrounds**. Buttons have a thick 2px midnight-blue border, no border-radius (sharp rectangles), and a `matrix3d(...)` transform that pushes them −4px up and 4px to the right — creating a 3D "lifted sticker" feel. On hover, the button drops back into place via `translateY` and outlines in electric blue (`#3252f4`). This press-down interaction, paired with airy watercolor gradient blobs that bleed across the periwinkle canvas, gives Recess a hand-made, almost zine-like quality that no other adaptogen brand has. It feels human in a category dominated by sterile tech-wellness aesthetics.

**Key Characteristics:**
- Periwinkle (`#a8b2ff`) as the dominant background — saturated, blue-purple, one-color commitment
- Sharp Grotesk Web at weight 500 for display, 400 for body — lowercase only, never uppercase headlines
- Midnight blue (`#25385b`) for all text, borders, button outlines — the workhorse foreground
- Stamp-button transform — `matrix3d` 4px offset default, `translateY` on hover (press-down sticker)
- Sharp 0px corners on buttons + 50% pill on circular elements + 36px on pill nav links
- Watercolor blob backgrounds in apricot, peach, pink — soft gradient washes across the canvas
- Cream secondary surface (`#fffcef`) for inverted buttons and pull-quote panels
- 8px spacing grid with editorial 64–144px section breathing room
- No drop shadows anywhere — the system is flat, with depth via offset transforms instead

## 2. Color Palette & Roles

### Primary
- **Recess Periwinkle** (`#a8b2ff`): Primary page background — the single signature color that anchors the entire identity. Saturated blue-purple. Used as wall-to-wall canvas, primary CTA fill, and brand surface.
- **Recess Midnight** (`#25385b`): Primary text, headings, body, button borders, button labels, footer surface. The workhorse foreground — sits on every periwinkle and cream surface.
- **Deep Midnight** (`#0a0a3a`): Footer background, modal underlines, deepest text color. A near-black blue that grounds the bottom of the page.

### Brand Accent
- **Soft Lavender** (`#c2caff`): Tinted periwinkle for secondary panels, hover-state surfaces, and background variation — a lighter sibling to the primary.
- **Recess Cream** (`#fffcef`): Warm off-white secondary surface — used for inverted buttons, pull-quote panels, and contrast moments inside the periwinkle canvas. Reads as paper, not screen.
- **Pure White** (`#ffffff`): Text on dark midnight footer surfaces, focus ring highlights.

### Watercolor Blob Palette
- **Apricot** (`#fedab3`): Watercolor gradient blob — used in hero background washes
- **Peach** (`#ffc8a0`): Secondary watercolor accent — pairs with apricot in hero gradient
- **Pink** (`#ffaeae`): Soft warm accent for blob compositions and decorative moments
- **Electric Blue** (`#3252f4`): Active/focus outline color on buttons — the only saturated chromatic moment
- **Ultramarine** (`#0f0f92`): Deep accent for selected states and emphasis
- **Recess Red** (`#ff5a5a`): Alert/notice color, tag accent — used very sparingly
- **Dark Red** (`#c51d1d`): Error and form validation

### Neutrals
- **Recess Midnight** (`#25385b`): All primary text and UI structure
- **Cool Gray** (`#84849c`): Muted secondary text, metadata, captions
- **Soft Gray** (`#b1b1b1`): Disabled state, decorative dividers

### Borders
- **Border Midnight** (`#25385b`): 2px solid borders around buttons, inputs, pills, framed cards
- **Border Deep Midnight** (`#0a0a3a`): 2px solid borders on dark footer elements

### Shadow & Depth
- Recess is **shadow-free**. The system has zero `box-shadow` declarations across the page. Depth comes exclusively from the 4px button offset transform (`matrix3d(1,0,0,0,0,1,0,0,0,0,1,0,4,-4,1,1)`) which creates a stamp/sticker effect without any blur.
- Focus rings: `rgba(255, 255, 255, 0.6) 0px 0px 0px 1px` — a thin 1px white halo for keyboard accessibility.
- Active outline: `3px solid #3252f4` — electric blue ring on press.

### Gradient System
- Watercolor blob gradients only — soft radial bleeds of apricot → peach → pink → periwinkle, used as decorative hero backgrounds rather than UI fills
- No linear gradients on buttons, cards, or text
- The periwinkle field itself is solid, not gradient — the blobs sit on top

## 3. Typography Rules

### Font Family
- **Primary**: `Sharp Grotesk Web`, with fallback: `system-ui, -apple-system, Segoe UI, Roboto, Helvetica Neue, Arial`
- **Display & Body**: Same family throughout — Recess is a single-typeface system
- **OpenType Features**: Standard ligatures only — Sharp Grotesk's lowercase character carries the personality

*Note: Sharp Grotesk is a commercial typeface from Lucas Sharp Type. Söhne, GT America, or Inter at weight 400/500 work as substitutes. Recess uses the medium weights (400–500) consistently — never the thin or bold ends of the family.*

### Hierarchy

| Role | Font | Size | Weight | Line Height | Case | Notes |
|------|------|------|--------|-------------|------|-------|
| Display Hero | Sharp Grotesk Web | 80px (5.00rem) | 500 | 1.25 | lowercase | Landing page headline ("relax & unwind with Recess") |
| Display Large | Sharp Grotesk Web | 60px (3.75rem) | 500 | 1.20 | lowercase | Secondary hero, full-width section heads |
| Display | Sharp Grotesk Web | 48px (3.00rem) | 500 | 1.20 | lowercase | Primary section titles ("why we made Recess") |
| Section Heading | Sharp Grotesk Web | 32px (2.00rem) | 400 | 1.38 | lowercase | Sub-section heads, content blocks |
| Sub-heading Large | Sharp Grotesk Web | 30px (1.88rem) | 400 | 1.25 | lowercase | Card titles, feature heads |
| Sub-heading | Sharp Grotesk Web | 24px (1.50rem) | 400–500 | 1.10–1.33 | lowercase | Smaller headlines, pull quotes, CTAs |
| Body Large | Sharp Grotesk Web | 20px (1.25rem) | 500 | 1.63 | sentence | Intro paragraphs, emphasized body |
| Body | Sharp Grotesk Web | 18px (1.13rem) | 400–500 | 1.63 | sentence | Standard reading text — generous line-height |
| Body Small | Sharp Grotesk Web | 16px (1.00rem) | 400 | 1.50 | sentence | Secondary copy, footer body |
| Button | Sharp Grotesk Web | 16–18px | 500 | 1.10 | sentence | Primary button labels — never uppercase |
| Tag / Eyebrow | Sharp Grotesk Web | 14.4px | 700 | 1.13 | UPPERCASE | One of the only uppercase moments in the system |
| Caption | Sharp Grotesk Web | 14px | 400 | 1.50 | sentence | Metadata, micro-copy |

### Principles
- **Lowercase is the voice**: Every display and section heading runs in lowercase. This is non-negotiable — uppercase headlines would break the meditative tone. Reserve uppercase only for tiny eyebrow tags at 14.4px weight 700.
- **Generous line-height**: Body text runs at 1.50–1.63 line-height — unusually airy, reflecting the "take a recess" philosophy. The page feels calm because no text block is dense.
- **Weight 400/500 only**: No 300, no 700, no 900 in display sizes. The voice is medium — confident but not shouting.
- **Single typeface, no contrast pairing**: Sharp Grotesk handles every size and role. The hierarchy is built from weight (400 vs 500) and scale (16px → 80px), not from typeface contrast.
- **No tracking adjustments on display**: Line-spacing is naturally tight at large sizes (1.20–1.25) but letter-spacing stays at 0 — Sharp Grotesk's natural width is the spacing system.
- **Tag chrome breaks the rule**: The single exception to lowercase-everywhere is small uppercase tags at 14.4px weight 700 — used for category labels and section eyebrows.

## 4. Component Stylings

### Buttons

**Primary Periwinkle Stamp**
- Background: Recess Periwinkle (`#a8b2ff`)
- Text: Recess Midnight (`#25385b`)
- Border: `2px solid #25385b`
- Padding: `24px 36px`
- Radius: `0px` (sharp rectangle)
- Transform: `matrix3d(1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 4, -4, 1, 1)` — translates 4px right, −4px up, creating the lifted-sticker stamp effect
- Outline: `3px none #25385b` (default invisible, becomes visible on active)
- Hover: `background-color: rgba(255, 255, 255, 0.2)` + `transform: translateY(0)` — the button drops back into place
- Active: `outline: 3px solid #3252f4` (electric blue ring) + `transform: translateZ(-1px)`
- Focus: `box-shadow: rgba(255, 255, 255, 0.6) 0 0 0 1px`
- Font: 16–18px Sharp Grotesk weight 500, lowercase
- Use: Primary CTAs — "shop now", "try a recess", "learn more"

**Cream Stamp (Inverted)**
- Background: Recess Cream (`#fffcef`)
- Text: Recess Midnight (`#25385b`)
- Border: `2px solid #25385b`
- Padding: `24px 36px`
- Radius: `0px`
- Transform: same `matrix3d` 4×−4 stamp offset
- Use: Secondary CTAs on periwinkle canvas — "view all" panels, "view our products"

**Skip Link / Tertiary**
- Background: Recess Periwinkle
- Padding: `0px` (inherits parent)
- Border: `0px`
- Font: 14.4px weight 700
- Use: Accessibility skip-links and chrome buttons

**Pill Navigation Link**
- Background: transparent or periwinkle
- Border: `2px solid #25385b`
- Radius: `36px`
- Padding: 8px 16px
- Use: Top nav links, breadcrumbs, category pills

**Circular Slide Dot**
- Size: 12×12px
- Border: `1px solid #25385b`
- Radius: `50%`
- Background: transparent default, midnight when active
- Use: Carousel pagination, slider position indicators

### Cards & Containers
- Background: Recess Cream (`#fffcef`) for content cards on periwinkle; Recess Periwinkle on cream surfaces
- Border: `2px solid #25385b` for framed cards; no border for flat content blocks
- Radius: `0px` rectangular default — Recess does not use mid-range radii
- Shadow: `none` — Recess is flat
- Internal padding: 32–64px for editorial breathing

### Watercolor Hero Background
- Soft radial gradient blob composition: apricot (`#fedab3`) → peach (`#ffc8a0`) → pink (`#ffaeae`) → periwinkle fade
- Implementation: oversized SVG or PNG positioned absolutely behind hero content, low opacity (60–80%)
- The blob is decorative only — typography always sits in front, never on top of saturated blob centers
- Reserved for hero moments and major section transitions — not used decoratively in card grids

### Badges / Tags / Pills
**Eyebrow Tag**
- Background: transparent
- Text: Recess Midnight (`#25385b`)
- Border: `2px solid #25385b`
- Padding: `4px 12px`
- Radius: `36px` or `0px`
- Font: 14.4px Sharp Grotesk weight 700, UPPERCASE
- Use: Category markers ("THE INTRO PACK"), section eyebrows

**Sale Pill**
- Background: Recess Red (`#ff5a5a`)
- Text: White
- Radius: `0px` or `36px`
- Use: Limited-availability tags, sale indicators — used very sparingly

### Inputs & Forms
- Background: Recess Cream (`#fffcef`) or transparent
- Border: `0px 0px 2px solid #0a0a3a` — bottom-only underline border, never full-frame
- Radius: `0px` on most; `8px` on multi-line textarea
- Font: 18px Sharp Grotesk weight 400, color `#25385b`
- Padding: 16px vertical, 0–8px horizontal (underline form aesthetic)
- Focus: border bottom transitions to `2px solid #ffffff` or `#3252f4`
- Placeholder: `#84849c` cool gray

### Navigation
- Top nav: horizontal periwinkle bar that matches the page background — feels "wall to wall"
- Logo: Recess wordmark in midnight, left-aligned
- Right side: account icon, cart icon, primary "shop" CTA in the periwinkle stamp button style
- Hover: link text shifts to electric blue (`#3252f4`)
- Sticky behavior: nav remains fixed at top; periwinkle background means there's no visible separation from the page

### Decorative Elements

**Stamp Offset Transform**
- `matrix3d(1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 4, -4, 1, 1)` for buttons
- `matrix3d(1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 3.6, -3.6, 1, 1)` for skip-links
- This is Recess's signature "press me" affordance — the button looks lifted off the page until you hover, then drops down
- Pairs with `transition: transform 0.2s ease` for the satisfying drop animation

**Watercolor Blob**
- Used sparingly — typically one blob per hero section
- Blob colors mix apricot (`#fedab3`), peach (`#ffc8a0`), pink (`#ffaeae`) at low opacity (40–60%)
- Sits behind hero copy as a soft atmospheric layer
- Edges are deliberately fuzzy/wet — no clean shapes, no geometric forms

## 5. Layout Principles

### Spacing System
- Base unit: 8px
- Scale: 4px, 8px, 12px, 16px, 24px, 28px, 32px, 40px, 48px, 64px, 101px, 144px, 162px
- Notable: Recess has a clear "compact UI" range (4–16px) and a generous "editorial spacing" range (64–162px). Mid-range values (28–48px) handle component internals; the gaps between sections are always 64px+.

### Grid & Container
- Max content width: ~1200px for centered content; full-bleed periwinkle canvas
- Hero: full-width single-column with watercolor blob background
- Feature sections: single-column statements or 2-column product cards
- Press / testimonial sections: scrolling marquees or 3-column grids
- Footer: 4-column nav grid on dark midnight surface

### Whitespace Philosophy
- **Meditation pacing**: Each section gets 100–200px of vertical breathing room — the page reads like a guided meditation, not a sales funnel
- **Type-anchored rhythm**: An 80px display heading commands 144–162px of air above and below; a 16px paragraph only needs 24px
- **Color-blocked sections**: Periwinkle hero → periwinkle middle → periwinkle CTA → dark midnight footer. No alternating canvas — the periwinkle is unbroken until the footer
- **Watercolor as breathing**: When the page feels too uniform, a soft blob fills the negative space rather than introducing a new section divider

### Border Radius Scale
- Sharp (0px): Buttons, content cards, framed containers — the workhorse radius
- Soft (8px): Multi-line inputs and textareas only — a subtle softening for typed content
- Pill nav (36px): Top-nav pill links, eyebrow tags
- Circular (50%): Slide dots, avatars, circular icon buttons
- No mid-range radii: Recess does not use 4px, 12px, 16px, 20px, 24px values. The system is binary at the extremes.

## 6. Depth & Elevation

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | No shadow, no transform | Page canvas, body text, structural containers, footer |
| Stamp Lifted (Level 1) | `matrix3d(...4,-4,1,1)` — translates 4px right and 4px up | Primary buttons, CTAs — the "ready to press" state |
| Stamp Pressed (Level 2) | `translateY(0)` or `translateZ(-1px)` | Hover/active state on buttons — the "I just got pressed" drop |
| Focus Halo (Level 3) | `box-shadow: rgba(255, 255, 255, 0.6) 0 0 0 1px` | Keyboard focus on interactive elements |
| Active Outline (Level 4) | `outline: 3px solid #3252f4` | Press confirmation — electric blue ring |

**Shadow Philosophy**: Recess has zero traditional drop shadows. Where most CPG sites use soft shadows to lift cards off the canvas, Recess achieves depth entirely through the `matrix3d` button transform — a graphic stamp effect that mimics the way a sticker sits proud of a surface. When the user hovers, the button physically drops via `translateY`. This is a tactile, almost analog interaction that feels closer to a paper zine than a webapp. The complete absence of shadows reinforces the watercolor/zine aesthetic — clean shapes on a saturated field.

### Decorative Depth
- The 4×−4 transform creates a 3D "lifted sticker" feel without any blur
- Hover transitions back to translateY(0) at 0.2s ease — satisfying drop response
- No ambient lighting effects; no glow halos except the white focus ring
- Watercolor blobs add visual depth via color softness, not via z-axis lift

## 7. Do's and Don'ts

### Do
- Commit fully to periwinkle (`#a8b2ff`) as the dominant background — not as one of three colors, but as the wall-to-wall canvas
- Use Sharp Grotesk Web at weight 500 for all display headlines, lowercase
- Keep all section headlines in lowercase ("relax & unwind", "why we made Recess") — uppercase is reserved for tiny eyebrow tags
- Apply the `matrix3d` 4×−4 stamp transform to primary buttons — this is the brand's tactile signature
- Use 2px solid midnight borders on buttons, inputs, pills — never 1px, never thicker
- Pair watercolor blob backgrounds (apricot/peach/pink) with periwinkle for hero atmosphere
- Use cream (`#fffcef`) for inverted surfaces and pull-quotes — never pure white on periwinkle
- Run body text at 1.50–1.63 line-height — generous breathing aligns with the brand
- Keep the page shadow-free — depth comes from transforms only

### Don't
- Don't use uppercase for display or section headlines — Recess is lowercase, full stop
- Don't introduce drop shadows or `box-shadow` blurs — the system is flat by design
- Don't use mid-range border-radius (4px, 12px, 16px, 24px) — go sharp 0px or pill 36px / 50%
- Don't break the periwinkle commitment with a different page background — the canvas IS the brand
- Don't stack a second sans-serif against Sharp Grotesk — single typeface only
- Don't use weight 700 for display — only for tiny uppercase eyebrow tags
- Don't put a primary CTA without the matrix3d stamp transform — flat buttons feel un-Recess
- Don't replace watercolor blobs with hard-edged shapes — the brand reads as soft and wet
- Don't use linear gradients on buttons or cards — gradients are for atmospheric blobs only

## 8. Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile Small | <360px | Single column, hero drops to 32–40px, stacked CTAs |
| Mobile | 360–568px | Single column, 40–48px hero, watercolor blob compresses |
| Tablet Small | 568–768px | 2-column grids begin, 48–60px hero |
| Tablet | 768–1024px | Full multi-column product grids, 60–72px hero |
| Desktop | 1024–1460px | Maximum hero (80px), 1200px container |
| Wide Desktop | ≥1460px | Periwinkle field extends edge-to-edge, content max-width holds |

### Touch Targets
- Primary CTAs: min 56px tap height (24px padding + 16px text + 24px padding ≈ 64px) — generous for thumb reach
- Nav links: 44px min tap area on pill links
- Slide dots: 12px visual with 24px tap area

### Collapsing Strategy
- **Nav**: Horizontal pill bar collapses to hamburger on mobile; full-screen periwinkle drawer on open
- **Hero**: 80px → 60px → 48px → 32px progressive scaling, weight 500 maintained throughout
- **Watercolor blob**: scales proportionally on mobile but never crops — full atmospheric layer preserved
- **Product grids**: 4-column → 2-column → 1-column on mobile
- **Section spacing**: 144px+ desktop → 64px mobile — reduces but maintains meditative pace
- **Button transform**: Stamp 4×−4 offset preserved on mobile — touch interaction still triggers the press-down drop

### Image Behavior
- Product imagery (cans, packaging) maintains aspect ratio; floats on periwinkle canvas without containers
- Watercolor blobs scale with viewport; mobile compresses but never crops
- No art direction changes — same visual language adapts to smaller viewports
- Logo wordmark scales proportionally; never becomes an icon-only mark

## 9. Agent Prompt Guide

### Quick Color Reference
- Page Background: Recess Periwinkle (`#a8b2ff`)
- Primary Text: Recess Midnight (`#25385b`)
- Secondary Surface: Recess Cream (`#fffcef`)
- Footer Background: Deep Midnight (`#0a0a3a`)
- Active Outline: Electric Blue (`#3252f4`)
- Watercolor Blob: Apricot `#fedab3` → Peach `#ffc8a0` → Pink `#ffaeae`
- Border Default: `2px solid #25385b`
- Focus Ring: `rgba(255, 255, 255, 0.6) 0px 0px 0px 1px`
- Stamp Transform: `matrix3d(1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 4, -4, 1, 1)`

### Example Component Prompts
- "Create a hero section on Recess Periwinkle (`#a8b2ff`) with a soft watercolor blob background blending apricot, peach, and pink at 50% opacity. Headline at 80px Sharp Grotesk Web weight 500, lowercase, line-height 1.25, color `#25385b`. Subhead at 20px weight 500, line-height 1.63."
- "Design a primary CTA button — periwinkle (`#a8b2ff`) background, midnight (`#25385b`) text, 2px solid midnight border, 24px 36px padding, 0px border-radius. Apply `transform: matrix3d(1,0,0,0,0,1,0,0,0,0,1,0,4,-4,1,1)` for the lifted stamp effect. On hover, transition to `translateY(0)` and add `outline: 3px solid #3252f4`."
- "Build a product card on Recess Cream (`#fffcef`) with a 2px solid midnight border, 0px border-radius, no shadow. Title in Sharp Grotesk 30px weight 400 lowercase, body in 18px weight 400 with 1.63 line-height."
- "Create an eyebrow tag — transparent background, 2px solid midnight border, 36px border-radius, 4px 12px padding, 14.4px Sharp Grotesk weight 700 UPPERCASE in `#25385b`."
- "Design an underline-style input — transparent background, no border-radius, only `border-bottom: 2px solid #0a0a3a`, 18px Sharp Grotesk weight 400 in `#25385b`. Focus state transitions border to `#3252f4`."

### Iteration Guide
1. Default to periwinkle (`#a8b2ff`) as the page background — single-color commitment is the brand
2. All headlines lowercase, Sharp Grotesk Web weight 500. Uppercase only for 14.4px eyebrow tags weight 700.
3. Buttons get the matrix3d 4×−4 stamp transform — this is non-negotiable for primary CTAs
4. Borders are 2px solid midnight (`#25385b`) — never 1px, never 3px, never thicker than 2px
5. Border-radius is binary: 0px sharp or 36px pill or 50% circle. Never mid-range.
6. Body text runs at 1.50–1.63 line-height — generous airiness reinforces the calm brand voice
7. Watercolor blobs are reserved for hero atmospheres — apricot/peach/pink at 40–60% opacity
8. Cream (`#fffcef`) is the only valid secondary surface on periwinkle — pure white never appears as a panel
9. The system is flat — never add `box-shadow`. Depth comes from the stamp transform only.
10. Footer is the only place the page breaks from periwinkle — deep midnight (`#0a0a3a`) with white text
