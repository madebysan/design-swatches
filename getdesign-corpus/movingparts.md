# Design System Inspired by Moving Parts

## 1. Visual Theme & Atmosphere

Moving Parts is a Swift component studio that designs its marketing site like an art-directed magazine masquerading as a developer landing page. The homepage is built on a warm off-white canvas (`#fcfcfc`) with hard pure-black ink (`#000000`), but the section-level art direction throws competing color blocks at the reader — saturated lime (`#00ffa6`), violet (`#9c66ff`), magenta (`#dd4a68`), electric blue (`color(display-p3 0 0 1)`), and chrome yellow — each owning a full-bleed editorial chapter. The composition reads less like SaaS and more like the inside of an issue of Émigré: huge mvp-prefixed component mockups float on flat color fields, captioned with mono labels, paced by a 100px display headline that announces every chapter the way a print magazine announces a department.

The defining typeface is **Unica77** (Lineto's neo-grotesk reissue) at weight 700, run at 100–110px with extreme negative tracking (`-4.4px`, line-height `0.93`). It is the brand's voice — confident, mechanical, almost slab-like in its weight, the opposite of Cape's whisper-light grotesk. Underneath, **PP Neue Montreal**, **Whyte Semi-Mono**, **Fraunces 72pt Soft**, and **IBM Plex Mono** appear in supporting roles — Moving Parts treats type the way a magazine treats it, mixing five families to give each section a different editorial register. Articles flip the system entirely: long-form essays sit on a near-black canvas (`#13161d`) with **Inter** display at 100px weight 600, sky-blue links (`#69c9ff`), and IBM Plex Mono for code blocks at relaxed 1.88 line-height. Two complete visual systems share one studio identity.

What separates Moving Parts from its peers is the willingness to **art-direct the components themselves**. Buttons, cards, sliders, and code samples are rendered as oversized hero artifacts on flat color backgrounds — a violet "Add to Cart" pill on lime, a magenta product card with thick white photo borders, a yellow code panel with hand-drawn arrows. The components ARE the visual identity. There is no separate illustration system; every piece of marketing imagery is a real (or stylized) SwiftUI component sitting on a colored stage, sized large enough to function as poster art.

**Key Characteristics:**
- Unica77 weight 700 at 100–110px with `-4.4px` letter-spacing and `0.93` line-height — slab-grotesk display
- Editorial section-blocking: each scroll module owns a saturated full-bleed color (lime, violet, magenta, electric blue, yellow)
- Off-white homepage canvas (`#fcfcfc`) with pure black ink; near-black (`#13161d`) for long-form essays
- Five-family type stack — Unica77, PP Neue Montreal, Whyte Semi-Mono, Fraunces 72pt Soft, IBM Plex Mono — each with editorial intent
- Component-as-illustration: oversized SwiftUI mockups serve as the hero art on every section
- Soft rounded geometry on components (12–18px radius), 50% pills on circular controls, large-radius (95px) hero buttons
- Atmospheric drop shadows (`9.8px 18.5px 28.3px rgba(0,0,0,0.1)`) on floating component cards
- Thick, declarative borders — 1px, 4px, 7px, even 13px solid black — used as graphic borders, not hairlines

## 2. Color Palette & Roles

### Primary
- **Ink Black** (`#000000`): All primary type on the homepage, button outlines, decorative borders. Pure, uncompromised black — no softening.
- **Page Off-White** (`#fcfcfc`): The marketing site canvas. A breath warmer than `#ffffff`, reads as paper.
- **Pure White** (`#ffffff`): Component backgrounds, photo borders (5px solid white as a print-frame device), inverted text on color blocks.

### Long-Form / Essays
- **Essay Ink** (`#13161d`): The dark canvas for `/articles` and individual essay pages. A blue-leaning near-black, never pure `#000`.
- **Essay Body** (`#999999`): Muted body gray on the dark canvas — readable but quiet.
- **Essay Mid** (`#585858`): Secondary gray for captions, metadata, code comment text.

### Editorial Accents (Section-blocking)
- **Studio Lime** (`#00ffa6`): The signature accent. Used as full-bleed section background ("Compose anything mobile") and on component highlights.
- **Studio Violet** (`#9c66ff`): Second-tier accent for component callouts, hero garnish, link emphasis on light surfaces.
- **Studio Magenta** (`#dd4a68`): Section block for product card moments and form-related demos.
- **Electric Blue** (`color(display-p3 0 0 1)` / `#0000ff`): The "Pow" / button blue — used on primary CTAs and a full chapter background. Rendered in display-p3 for extra saturation on capable displays.
- **Studio Yellow** (`#fef07a`-ish, hand-keyed): The "Code Good" panel — yellow with hand-drawn red arrow annotations.
- **Code Active Blue** (`#0000dd`): The pressed/active state of the primary blue button — drops one notch deeper.

### Body / UI Neutrals
- **Caption Gray** (`#999999`): Universal muted text on either canvas.
- **Burnt Sienna** (`#9a6e3a`): Syntax highlighting accent in code blocks.
- **Code Pink** (`#dd4a68`): Doubles as syntax color and section accent.
- **Link Sky** (`#69c9ff`): Hyperlinks within essays — only chromatic moment in body copy.

### Borders & Strokes
- **Thick Border Black** (`#000000`): 1px / 3px / 4px / 7px / 13px solid black, used as graphic ink line, not hairline detail.
- **Photo Frame White** (`#ffffff`): 5px solid white border on figure elements — the magazine "white-mounted print" effect.

### Gradient System
- Moving Parts uses **gradient meshes** (a SceneKit-rendered house specialty) as decorative imagery in the wordmark and select hero moments — soft warm-to-cool sweeps rendered as raster art, not CSS gradients. CSS surfaces themselves are flat solid color.

## 3. Typography Rules

### Font Stack
- **Display / Brand**: `Unica77` (Lineto), fallback `-apple-system, system-ui, Inter var, Segoe UI`
- **Display alt**: `PP Neue Montreal` — used at 42px on certain section heads
- **Mono Display**: `Whyte Semi-Mono` (ABC Dinamo) — for technical headings and labels
- **Editorial Serif**: `Fraunces 72pt Soft` weight 200 with `ss01` — used for occasional pull quotes / soft moments
- **Essay Display**: `Inter` weight 500–700 — long-form on dark canvas only
- **Code**: `IBM Plex Mono` 16px line-height 1.88 — code blocks
- **OpenType**: Heavy use of stylistic sets on Unica77 (`salt, ss01–ss05, ss07–ss09`) for uppercase tracked labels, plus `ss01` on Fraunces

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Hero Display Max | Unica77 | 110px (6.88rem) | 700 | 0.95 | -4.4px | Homepage chapter openers |
| Hero Display | Unica77 | 100px (6.25rem) | 700 | 0.93 | -4px | Standard section heroes |
| Essay Display | Inter | 100px (6.25rem) | 600 | 1.00 | -1.3px | Article headlines on dark |
| Display Large | Unica77 | 70px (4.38rem) | 700 | 0.96 | -2.8px | Mid-tier section heads |
| Display Mono | Whyte Semi-Mono | 45.7px (2.86rem) | 600 | normal | normal | Technical section markers |
| Display Soft Serif | Fraunces 72pt Soft | 46.8px (2.93rem) | 200 | 1.35 | normal | Pull quotes, soft moments |
| Section | Unica77 / PP Neue Montreal | 42.5px (2.66rem) | 500 | 0.87 | normal | Sub-section heads |
| Sub-Display Tracked | Unica77 (uppercase) | 37px (2.31rem) | 500 | 1.71 | 1.11px | Uppercase eyebrow labels |
| Essay H2 | Inter | 44px (2.75rem) | 400 | 1.19 | -0.5px | In-article headings |
| Essay H3 | Inter | 40px (2.50rem) | 700 | 1.42 | normal | Section breaks within essays |
| Body Large | Unica77 / Inter | 24px (1.50rem) | 400 | 1.42 | normal | Intro paragraphs |
| Body | Inter | 18px (1.13rem) | 600 | 1.40 | normal | Standard body, lead links |
| Body Small | Inter | 17px (1.06rem) | 500 | 1.40 | normal | Secondary copy |
| Code Block | IBM Plex Mono | 16px (1.00rem) | 400 | 1.88 | normal | All code samples |
| Caption | Unica77 | 14px (0.88rem) | 400 | 1.42 | 0.14px | Component labels, metadata |
| Caption Mono | monospace | 12px (0.75rem) | 400 | 2.50 | normal | Footnotes, technical chrome |
| Micro Link | Inter | 10px (0.63rem) | 400 | 1.00 | normal | Footer / utility links |

### Principles
- **Weight 700 is the brand voice.** Where Cape whispers at weight 300, Moving Parts shouts at weight 700 — Unica77 700 at 100–110px is the studio's signature register. Treat lower weights as supporting cast.
- **Aggressive negative tracking on display.** Letter-spacing scales with size: `-4.4px` at 110px, `-2.8px` at 70px, `-1.3px` at 100px Inter, `-0.5px` at 44px. Locks display type into solid graphic blocks.
- **Tight display line-height (0.87–0.96).** Headlines pack vertically. Body relaxes to 1.40–1.42. The contrast between dense type and airy body is part of the editorial pacing.
- **Five-family rotation.** Unica77 carries 80% of the work; PP Neue Montreal, Whyte Semi-Mono, Fraunces, and IBM Plex Mono each appear in deliberate, sparing roles. Treat each new family as a section signal, not decoration.
- **Uppercase mono labels.** Whyte Semi-Mono and uppercase Unica77 (with `0.14–1.39px` tracking) are used for component captions, version labels, and technical chrome — the magazine "running head" effect.
- **Code blocks breathe.** IBM Plex Mono at line-height 1.88 — much looser than typical 1.4 — gives long Swift snippets a relaxed, scannable cadence.

## 4. Component Stylings

### Buttons

**Primary Electric Blue (Square)**
- Background: `color(display-p3 0 0 1)` / `#0000ff`
- Text: Pure White (`#ffffff`), 28px Unica77 weight 600
- Padding: `25px 30px`
- Radius: `0px` (sharp rectangular, on dark sections)
- Border: `0px none`
- Outline: `3px` (focus indicator)
- Active: background flips to white, text to `#0000dd`
- Use: Hero CTAs in dark/blue chapters, "Book a demo"

**Primary Blue (Pill, Hero-scale)**
- Background: `color(display-p3 0 0 1)`
- Text: Pure White, 45.7px weight 700
- Padding: `47.9px 95.8px` — extreme generous padding
- Radius: `95.8px` — full pill (≥ height/2)
- Shadow: `rgba(0, 0, 0, 0.15) 20.7px 27.2px 28.3px 0` — strong directional drop
- Use: Component-as-art "Add to Cart" hero artifact

**Mock Circular Button**
- Background: Off-white `#fcfcfc`
- Text: Black, 32px weight 400
- Radius: `100%` (perfect circle)
- Padding: `0px`, sized by container
- Use: Back buttons, icon controls in component mockups

**Article CTA / Secondary**
- Background: Black or transparent
- Text: White or sky-blue `#69c9ff`
- Radius: `12px`
- Use: Inline article CTAs, footer actions

### Cards & Containers
- **Component Mockups**: White card on saturated color block, 12–18px radius, atmospheric shadow `9.8px 18.5px 28.3px rgba(0,0,0,0.1)`. Sized large — these are the hero illustrations.
- **Article Cards**: 14px radius, image-first layout, off-white surface, mono caption metadata.
- **Code Panels**: Dark navy (`#13161d`) on light pages, near-black on dark pages, 12px radius, 30–40px internal padding, IBM Plex Mono 16px content.
- **Aside / Pull Quote**: 14px radius, lighter slate fill on dark canvas, used for warnings ("here be dragons") and side commentary in essays.

### Photos & Figures
- **White Print Frame**: 5px solid white border on figure elements — the signature "magazine print mounted on color paper" device.
- Atmospheric shadow on white-framed photos (`5px 5px 20px rgba(0,0,0,0.25)`) gives them the "lifted from the page" effect.
- Border-radius on figure: `14px` — matched to article cards.

### Component Mocks (mvp- prefix)
Moving Parts ships its own design language for product-screenshot mocks: `mvp-button`, `mvp-stepper`, `mvp-slider`, `mvp-text`, `mvp-rectangle`, `mvp-hstack`, `mvp-switch-thumb`. These appear as oversized art on the homepage:
- `mvp-button` radius `32–40px`
- `mvp-stepper` radius `45.7px` with 4px black border
- `mvp-slider` track radius `94.7px` with 8px white border on thumb
- `mvp-text` decorative borders `7px solid #000` (graphic underline, not hairline)
- `mvp-rectangle` 3.27px radius — near-sharp content blocks

### Navigation
- Top bar: minimal — logo (158×59 SVG with gradient mesh), "Pow" link, "Articles" link
- Sticky, transparent over hero, opaque over content
- Link styling: 18–24px Inter weight 500–600, color shifts white-on-dark to black-on-light

### Decorative Elements
- **Hand-drawn red arrows** on yellow "Code Good" panels — adds a sketch-annotation editorial layer
- **Gradient mesh wordmark** — the only non-flat color element, rendered in their proprietary SceneKit pipeline
- **Asymmetric border radius** on hero rectangles: `0px 0px 138.9px 138.9px` and `138.9px 138.9px 0px 0px` — pure stadium shapes used as decorative backgrounds

## 5. Layout Principles

### Spacing System
- Base unit: 8px (with non-aligned editorial values like 6.5px, 8.7px, 15.1px, 30.2px breaking the grid for visual interest)
- Marketing scale: 8, 14, 16, 22, 25, 30, 40, 52, 60, 120, 148px
- Essay scale: 10, 15, 20, 30, 33, 38, 40, 54, 55, 250px
- The 250px value drives generous side margins on dark essay pages

### Grid & Container
- Marketing site: full-bleed sections, no fixed max-width — content blocks span the viewport, then internal max-width controls reading length
- Essay max-content: ~720px reading column, centered, with 250px side air on `≥1201px`
- Each homepage section is a **chapter** — full color block, hero component centered or offset, headline below or above

### Whitespace Philosophy
- **Editorial chapter pacing**: Sections are visually segmented by full-bleed color, not by spacing — color IS the divider.
- **Component breathing room**: Hero mockups get 60–148px of air around them before the headline arrives.
- **Essay calm**: Long-form pages use 30–55px paragraph spacing and 250px outer margins for a reading-room feel that contrasts with the homepage's noise.

### Border Radius Scale
- **Sharp (0px)**: Square buttons in editorial sections, decorative rectangles
- **Soft (12–18px)**: Component cards, code panels, asides — the workhorse radius
- **Stepper / Slider (45.7px)**: Compound controls with internal pills
- **Hero Pill (95–100px)**: Oversized CTA buttons used as poster artifacts
- **Stadium (138.9px on two corners)**: Decorative half-stadiums as background shapes
- **Circle (50% / 100%)**: Avatars, mock back buttons, slider thumbs

## 6. Depth & Elevation

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (0) | No shadow, flat color block | Section backgrounds, body type, color chapters |
| Soft Lift (1) | `rgba(0,0,0,0.1) 9.8px 18.5px 28.3px 0` | Component mockup cards, primary illustration depth |
| Photo Lift (2) | `rgba(0,0,0,0.25) 5px 5px 20px 0` | White-framed figures and photos |
| Hero Drop (3) | `rgba(0,0,0,0.15) 20.7px 27.2px 28.3px 0` | Oversized hero CTA buttons |
| Stage Drop (4) | `rgba(0,0,0,0.3) 19.6px 26.1px 39.2px 0` | Floating product mockups on saturated color |
| Focus Ring | `rgb(0,0,0) 0px 0px 0px 4.9px` | Keyboard-focus indicator on inputs |

**Shadow Philosophy**: Moving Parts uses **directional atmospheric shadows** — the offset is meaningfully larger than the blur (5–20px offset, 20–39px blur), creating a sense that components are physically lifted off the colored page. Shadows always tilt down-right (positive X, positive Y), as if a single editorial light source lives upper-left. This is the opposite of Cape's hard graphic stamps — Moving Parts wants softness, magazine-print depth, photographed-component realism.

### Decorative Depth
- All depth concentrates on **components-as-art** — the oversized button, the framed product photo, the floating sweater card. Body content stays flat.
- Code panels use no shadow on the dark canvas; their depth comes from radius and contrast.
- White-framed figures get a second shadow inside the frame (the print-mount effect) plus an outer drop, giving a layered editorial feel.

## 7. Do's and Don'ts

### Do
- Use Unica77 weight 700 at 100–110px for hero display — bold confidence is the brand
- Apply aggressive negative tracking (`-4.4px` at 110px, scaling proportionally) on all display type
- Block sections in saturated full-bleed color (lime, violet, magenta, blue, yellow) — color IS the chapter divider
- Render components themselves as oversized hero art with directional drop shadows
- Use 5px white photo borders on figures for the print-mounted-on-color-paper feel
- Mix five families with editorial intent — Unica77 lead, PP Neue Montreal section, Whyte Semi-Mono technical, Fraunces soft, IBM Plex Mono code
- Set code blocks at line-height 1.88 — relaxed scanning is part of the brand
- Switch to dark canvas (`#13161d`) and Inter for long-form essays — two visual systems, one identity
- Use thick declarative borders (4px, 7px, 13px solid black) as graphic ink lines

### Don't
- Don't use weight 300–500 on Unica77 display — the brand reads at 600–700
- Don't use pure white (`#ffffff`) for the marketing canvas — always `#fcfcfc`
- Don't apply soft pastel section blocks — saturated, near-fluorescent color is the editorial register
- Don't render hero illustrations separately from product — components ARE the illustrations
- Don't use blurred ambient shadows with no offset — directional (offset > blur) is the signature
- Don't reach for bright-blue `#0000ff` outside its assigned button/chapter role
- Don't introduce a 4–11px border radius — stay in the 0 / 12–18 / 45 / 95+ tiers
- Don't tighten essay body line-height below 1.4 — long-form needs the air
- Don't let a section live without a color block, an oversized component, or both
- Don't use Inter for the marketing display — Unica77 owns the homepage voice

## 8. Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Phone Small | <620px | Single column, hero drops to 48–60px, section blocks stack |
| Phone | 620–800px | Single column, hero 60–70px |
| Tablet | 800–1000px | 2-column component mocks emerge, hero 70–80px |
| Laptop | 1000–1200px | Full multi-column, hero 90–100px |
| Desktop | 1200–1728px | Maximum scale, 110px hero, full chapter widths |
| Cinema | ≥1728px | Container caps but type holds at 110px |

Essay pages add finer breakpoints (`1201/1199/999/840/620/600px`) to control reading column width and side margin.

### Touch Targets
- Primary CTAs: 47–95px tap height on hero buttons (oversized by design)
- Mock controls: minimum 44px tap area on circular buttons, 60px on hero-scale
- Article links: generous 18–24px text with 30px line-height for thumb scanning

### Collapsing Strategy
- **Hero display**: 110 → 100 → 70 → 48px progressive scale; weight stays at 700
- **Section color blocks**: stack vertically on mobile, maintain full-bleed
- **Component mockups**: re-center and resize, never crop or rotate
- **Photo frames**: maintain 5px white border at all sizes
- **Code blocks**: switch to horizontal scroll on phone rather than wrap
- **Five-family stack**: holds across breakpoints — type voice is non-negotiable

### Image / Component Behavior
- Oversized hero components scale proportionally; never become icons
- Gradient mesh logo holds at 158×59 minimum, never reduces to a glyph
- Article header images maintain 14px radius and aspect ratio across breakpoints

## 9. Agent Prompt Guide

### Quick Color Reference
- Marketing Canvas: Page Off-White (`#fcfcfc`)
- Marketing Ink: Black (`#000000`)
- Essay Canvas: Essay Ink (`#13161d`)
- Essay Body: Caption Gray (`#999999`)
- Hero Accent — Lime: (`#00ffa6`)
- Hero Accent — Violet: (`#9c66ff`)
- Hero Accent — Magenta: (`#dd4a68`)
- Hero Accent — Blue: `color(display-p3 0 0 1)` / `#0000ff`
- Hero Accent — Sky (links in essays): (`#69c9ff`)
- Component Lift: `rgba(0,0,0,0.1) 9.8px 18.5px 28.3px 0`
- Hero Button Drop: `rgba(0,0,0,0.15) 20.7px 27.2px 28.3px 0`

### Example Component Prompts
- "Build a Moving Parts homepage chapter on a full-bleed `#00ffa6` lime block. Headline: Unica77 100px weight 700, line-height 0.93, letter-spacing -4px, color `#000000`. Place an oversized SwiftUI component mockup card (white, 14px radius, atmospheric shadow `9.8px 18.5px 28.3px rgba(0,0,0,0.1)`) centered above. Caption below in Whyte Semi-Mono 14px uppercase with 0.14px tracking."
- "Design an essay header on `#13161d` canvas. Title in Inter 100px weight 600, line-height 1.00, letter-spacing -1.3px, color `#ffffff`. Subtitle in Inter 24px weight 400 line-height 1.42 in `#999999`. Author/date row in Unica77 14px with 0.14px tracking, color `#585858`."
- "Render a hero CTA button — `color(display-p3 0 0 1)` background, white Unica77 weight 700 at 45.7px, padding 47.9px × 95.8px, radius 95.8px, drop shadow `rgba(0,0,0,0.15) 20.7px 27.2px 28.3px 0`. The button should read as a poster artifact, not a UI element."
- "Style a code block on a dark page: IBM Plex Mono 16px line-height 1.88, dark navy background `#13161d`, 12px radius, 30–40px internal padding, syntax highlighting in `#dd4a68` (keywords), `#9a6e3a` (numbers), `#69c9ff` (function names)."
- "Build a framed product photo: 14px outer radius, 5px solid white border (the print-frame device), atmospheric shadow `5px 5px 20px rgba(0,0,0,0.25)`. Place on a saturated magenta `#dd4a68` section block."
- "Create an uppercase eyebrow label: Unica77 37px weight 500, line-height 1.71, letter-spacing 1.11px, OpenType features `salt, ss01–ss05, ss07–ss09` enabled, transform uppercase."

### Iteration Guide
1. Default to Unica77 weight 700 at 100–110px for marketing display — anything lighter loses the brand voice
2. Section-block in saturated color FIRST, then place type and components on top — color is the chapter
3. Components are the illustrations — render mockups oversized with directional shadows, not as small UI examples
4. Negative tracking scales with size: `-4.4px / -4px / -2.8px / -1.3px / -0.5px` from 110px down to 44px
5. Keep two visual systems — light marketing (Unica77 / `#fcfcfc`) and dark long-form (Inter / `#13161d`) — don't mix them mid-page
6. Border-radius lives in distinct tiers: 0 (sharp), 12–18 (cards), 45 (steppers), 95+ (hero pills) — avoid the 4–11 dead zone
7. Drop shadows are directional and atmospheric — offset > blur, light from upper-left, never blurred ambient haze
8. Use Whyte Semi-Mono uppercase for technical chrome and labels — the "running head" of the magazine
9. White photo frames (5px solid `#ffffff`) on figures are the secret sauce — they sell the editorial print-mount feel
10. Code breathes at line-height 1.88 in IBM Plex Mono — a relaxed scanning rhythm, not dense type
