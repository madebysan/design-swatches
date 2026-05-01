# Design System Inspired by Mainframe Manifesto

## 1. Visual Theme & Atmosphere

The Mainframe Manifesto (`manifesto.mainframe.inc`) is not a marketing page — it is a single-page art-directed essay about computing, dressed as a museum installation of a vintage CRT monitor. The page opens on a warm eggshell canvas (`#e2deda`) overlaid with a tactile noise texture, and the entire reading experience is staged inside a beige "monitor frame" device that fills the viewport. Inside that frame, content scrolls as if it were the screen — the page literally reads as a computer narrating its own origin myth. "Once upon a time, we pressed ENTER" is the opening line, and the word ENTER stretches across the full screen-width with horizontal scanlines slicing through it. Every section after that — terminals, tasks, shift, products, membership card, CTA — is staged as another "screen" within the same monitor.

The system runs on three colors and exactly three colors: graphite text (`#292929`), eggshell paper (`#e2deda`), and a single high-energy red signal (`#eb4e3d`) used as a power-light, an underline, a system-error glyph. There is no blue, no neutral grey scale, no on-brand gradient. The discipline is total — and that scarcity is what makes the red feel earned every time it appears. The only chromatic tension on the page is the `#eb4e3d` flicker, which functions like the LED on a vintage console: rare, mechanical, intentional. Combine that with `PP Neue Montreal` (the warm-grotesk workhorse) for body, `SimpleLLWeb-Bold` for monumental display, and `Consolas` for terminal-style metadata, and the brand reads as: a contemporary type studio writing love letters to 1984 hardware.

What distinguishes Mainframe most is its **frame-within-frame staging**. Where most product pages dissolve their chrome and let content breathe edge-to-edge, Mainframe does the opposite — it constructs a literal `_frameBorder_1h08d_9` around the viewport, with an `_outer_1h08d_24` and `_inner_1h08d_32` shell, a circular "logo" status indicator at the bottom-center (the home button on a pretend bezel), and a `_serialNumberPositioner` that runs vertical-rl text down the right edge like an etched serial plate. The page does not pretend to be flat HTML; it pretends to be hardware. Layered on top of all this: a 60%-opacity eggshell-paper texture and a 3%-opacity noise grain that gives every surface the dust of a museum exhibit. CSS grid-template-areas (`"t t t t" "g g g g" ". . s s"` and similar) handle the editorial composition section by section, so each "screen" of the monitor has its own typographic spread.

**Key Characteristics:**
- Three-color discipline: graphite (`#292929`), eggshell (`#e2deda`), signal red (`#eb4e3d`) — nothing else
- Monitor-frame staging — content lives inside a literal CRT bezel device, not edge-to-edge
- Three typefaces with distinct jobs: `PP Neue Montreal` (body), `SimpleLLWeb-Bold` (display), `Consolas` (terminal data)
- Eggshell paper texture (60% opacity) + grain noise (3% opacity) on every surface
- Scanline display headlines — large type sliced by horizontal rules, evoking CRT raster lines
- CSS grid-template-areas drive editorial layout, not flex containers
- Aspect-ratio-locked graphics (e.g., `1440/204`, `108/40`, `64/42`) for editorial-precise crops
- Vertical-rl writing mode for serial numbers and metadata — print-graphic small caps on edges
- Numeric-flow ticker and Rive/Lottie animations for ambient motion (oxygen lines, typing text)
- The red is rare. One application per screen, reserved for status, signal, and the "Power" indicator

## 2. Color Palette & Roles

### Primary
- **Mainframe Graphite** (`#292929`): The primary text color, button background, frame edges, and structural rule lines. Not pure black — a deliberately warm graphite that pairs with eggshell instead of fighting it.
- **Mainframe Eggshell** (`#e2deda`): The page canvas and the inverted text color on dark surfaces. A warm off-beige that reads as aged paper or unbleached photo board.

### Brand Accent
- **Signal Red** (`#eb4e3d`): The only chromatic color in the system. Used for the power-light circle, error/status glyphs, the underline beneath active links, animated oxygen-line graphics, and rare CTA emphasis. One application per screen maximum — the red is sacred.
- **Signal Red 10%** (`rgba(235, 78, 61, 0.1)`): A faint red wash used for hover states on red-labeled elements and animation glow tints. Never used as a panel background.

### Neutrals & Tints
- **Graphite 10%** (`rgba(41, 41, 41, 0.1)`): Default button background — a translucent stamp of the primary color over the eggshell canvas, so buttons read as "embossed paper" rather than chips.
- **Graphite 15%** (`rgba(41, 41, 41, 0.15)`): Focus state background — slightly darker translucent panel for keyboard focus.
- **Graphite 16%** (`rgba(41, 41, 41, 0.16)`): Border color on inputs — a hairline that lives in the noise without dominating it.
- **Pure White** (`#ffffff`): Used exclusively as the inverted text color on hover (text flips to white on dark hover-fill).

### Surface & Texture
- **Eggshell Texture** (`/_nuxt/eggshell.BZdXW5nt.png` at 60% opacity): The canvas grain — a paper-like background image laid over `#e2deda` to produce material warmth.
- **Noise Texture** (`/_nuxt/noise.BU9aNW8K.png` at 3% opacity): A faint dust-grain layer applied across full sections to break the digital flatness.
- **Card Logo** (`/_nuxt/card-logo.CkINcT4q.svg`): The branded SVG mark used as the membership-card graphic — locked to its grid area as decorative metadata.

### Gradient System
- The system uses one gradient: a subtle vignette inside the monitor frame combining `linear-gradient(180deg, rgba(41,41,41,0), rgba(41,41,41,0.06))` with `radial-gradient(64.62% 100% at 50% 0, hsla(0,0%,100%,0.2), hsla(0,0%,100%,0))`. This produces a soft "screen glare" effect at the top of the inner frame, like light catching a glass tube. Never used elsewhere — the system is otherwise solid-color.

## 3. Typography Rules

### Font Family
- **Primary Sans**: `PP Neue Montreal`, with fallback: `sans-serif` — body, captions, links, button labels, paragraph text. Pangram Pangram's grotesk workhorse — warmer than Söhne, more mechanical than Inter.
- **Display**: `SimpleLLWeb-Bold`, with fallback: `monospace` — used for the colossal "ENTER" graphic and select monumental moments. A bold display face that reads like industrial signage.
- **Monospace / Terminal**: `Consolas` (and `ConsolasRegular`) — used for serial numbers, cohort metadata, console output, vintage-system data display. Letter-spacing pulled tight (`-1.36px`) for compact terminal density.

*Note: `PP Neue Montreal` is a commercial typeface from Pangram Pangram. For external implementations, `Söhne` or `Neue Haas Grotesk` serve as close substitutes; `Inter` works as the web-safe fallback. `SimpleLLWeb-Bold` is from Lineto — substitute `GT America Mono Bold` or `IBM Plex Mono Bold` if unavailable.*

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Display Hero ("ENTER") | SimpleLLWeb-Bold | clamp(2.06rem → 3.25rem) (~33–52px) | 700 | 0.98 | -0.08em | The marquee headline — sits behind scanlines |
| Display Large | PP Neue Montreal | clamp(34→24px) | 500 | 1.24 | -0.01em | Section openings, "Once upon a time…" |
| Display | PP Neue Montreal | clamp(20→40px) | 400 | clamp(28→32px) | -0.01em | Story-beat headers |
| Sub-heading | PP Neue Montreal | 23.26px (1.45rem) | 500–700 | 1.30 | normal | Card titles, sub-section heads |
| Body Large | PP Neue Montreal | clamp(17→20px) | 400 | 1.50 | normal | Paragraph runs, manifesto prose |
| Body | PP Neue Montreal | 17px (1.06rem) | 700 | 1.98 | normal | Emphasized inline labels |
| Body Console | Consolas | 17px (1.06rem) | 400 | 1.50 | -1.36px | Serial numbers, terminal output |
| Link / UI | PP Neue Montreal | 16.44px (1.03rem) | 500 | 1.14 | normal | Nav links — sometimes lowercase-forced |
| Label-01 | PP Neue Montreal | clamp(0.75→1.0625rem) | 500 | 1.43 | normal | Section labels, footer metadata |
| Label-02 | PP Neue Montreal | clamp(0.875→1.25rem) | 500 | 1.30 | normal | Button labels, small headers |
| Caption | PP Neue Montreal | clamp(0.625→0.875rem) | 500 | 1.25 | 0.0922px | Figure numbers, captions |
| Caption Small | PP Neue Montreal | 9.22px (0.58rem) | 500 | 1.25 | 0.092px | Micro labels, "Fig 4", serial digits |

### Principles
- **Three faces, three jobs**: Sans for content, display-bold for monuments, mono for machine data. No mixing — Consolas never appears in body prose, PP Neue Montreal never appears as the giant ENTER.
- **Tight display, looser body**: Display headlines run at line-height 0.98 with `-0.08em` tracking — locked into dense monolithic blocks. Body prose relaxes to 1.5 line-height with normal tracking — readable as actual writing.
- **Lowercase forcing as a UI tic**: Nav links use `text-transform: lowercase` in CSS even when the source markup is mixed-case — a deliberate typographic tell that nods to modernist editorial convention ("blog / careers / @mainframe").
- **Fluid clamps everywhere**: Every type size is wrapped in `clamp()` with viewport-width interpolation (`calc(... + Xvw - Ypx)`) — type scales smoothly with viewport, no breakpoint pops. Display headline scales 33px → 52px across the responsive range.
- **Vertical-rl for chrome**: Serial numbers and edge metadata use `writing-mode: vertical-rl` to run sideways down the bezel — a small print-graphic touch you don't see on contemporary product sites.
- **Numeric ticker animations**: Numbers in the page (cohort counts, dates) use a custom `--number-flow-char-height` ticker that animates digit changes in place, like a flip-clock.

## 4. Component Stylings

### Buttons

**Primary (Default)**
- Background: Graphite 10% (`rgba(41, 41, 41, 0.1)`)
- Text: Mainframe Graphite (`#292929`)
- Padding: 0 (text sets its own breathing room via the inner span)
- Radius: `8px`
- Border: `0`
- Box-shadow: `none`
- Outline: `rgb(41, 41, 41) none 3px` (declared but invisible — primes the focus state)
- Font: PP Neue Montreal weight 400 at button-context size (up to 40px on hero CTAs)
- Hover: text inverts to `#ffffff`, background fills to solid graphite
- Focus: background → `rgba(41, 41, 41, 0.15)`, outline removed
- Use: All primary CTAs — "Enter", "Continue", footer link cluster

**Email Submit Button**
- Background: Graphite 10% transitioning to solid `#292929` on success
- Has internal `_loading_1039t_28` state with Rive animation
- Has internal `_icon_1039t_32` slot for arrow glyph
- Use: The single signup form on the page

**Inline Text Link (Primary)**
- Color: `#292929` default (or `#e2deda` when on dark inverted surface)
- Text-decoration: `none`
- Font-weight: 500
- Includes a small arrow icon (8×8 SVG) at right — `_icon_16kk5_9`
- Hover: paired with red underline reveal on certain links

### Frame Border Device (Signature Component)
- The page's defining structure: an `_outer_1h08d_24` shell wrapping an `_inner_1h08d_32` content area
- Outer frame: rounded `border-radius: clamp(16px, 24px)` corners with eggshell texture, drop shadow `0 48px 112px -32px rgba(41,41,41,0.3)`
- Inner area: `aspect-ratio: 1440/204` for the top bar; full-bleed for the screen content
- Includes a `_logo_1h08d_52` circle at bottom-center — the home-button bezel detail with the red dot
- Includes a top metadata strip: brand name, copyright, nav links, social handle
- Use: Wraps the entire page — every section is a "screen" inside this frame

### Cards & Containers (Membership Card)
- Background: Mainframe Graphite (`#292929`) with eggshell texture overlay at 60% opacity
- Text: Mainframe Eggshell (`#e2deda`)
- Radius: `8px` for soft cards, `42px` for pill-style framed sections
- Layout: CSS Grid with `grid-template-areas: ". . g g g g g g g . t t t t t . ."` — graphic on left, text on right, with explicit gutters
- Includes `_serialNumberPositioner` running vertical-rl down the right edge
- Header/Footer: small `label-01` rows with cohort/date/serial metadata
- Use: Membership card, product graphic cards, terminal screens

### Inputs (Email Form)
- Background: `transparent` — sits directly on canvas
- Color: Mainframe Graphite (`#292929`)
- Border: `1px solid rgba(41, 41, 41, 0.16)` (hairline)
- Radius: `0px` (sharp — buttons round, inputs do not)
- Padding: `12px 16px 0px` (top-heavy — leaves room for floated labels)
- Font: PP Neue Montreal at body size, 500 weight
- Focus: border-color jumps to solid `#292929`, outline removed
- Use: The single CTA email input on the closing section

### Badges / Status Indicators
- **Notification Badge** (`_notificationBadge_1xboc_9`): A small red pill with white number, used over icon dock app tiles
- Background: Signal Red (`#eb4e3d`)
- Text: White
- Radius: pill / circle
- Animated number using `numberFlow` ticker

### Navigation
- Top nav lives inside the frame's bezel — fixed at the top of the `_inner_1h08d_32` shell
- Left side: brand wordmark "Mainframe Computer, Inc." + copyright line in `label-01`
- Right side: link cluster — `blog ↗`, `careers ↗`, `@mainframe`
- Each external link includes the 8×8 SVG arrow glyph
- Hover: red underline appears beneath the lowercase label
- The whole nav reads like the metadata strip on a blueprint or the spine of a hardware manual

### Decorative Elements

**Scanlines / Oxygen Lines**
- The signature graphic device — horizontal rules slicing through display headlines
- Implemented as either pure CSS borders or as a Rive/Lottie animation (`_oxygenLines_gco19_9`)
- Animated: lines pulse and breathe, hence the "oxygen" naming
- Used over the ENTER hero, terminal section, and shift section
- Effect: turns flat type into a CRT-display moment

**Power Light**
- A single circular dot in Signal Red (`#eb4e3d`)
- Located at the bottom-center of the frame border (the "power button" of the pretend monitor)
- Sometimes animated with a subtle pulse
- The brand's most concentrated atom

**Apps Wrapper / Dock**
- A row of small app-tile icons (`_appsWrapper_1u2kr_9`, `_appTile_1u2kr_14`)
- Each tile shows a small product/feature graphic
- Sits like a Mac OS Classic dock at the bottom of one of the screens
- Some tiles carry red notification badges

**Card Logo**
- An SVG mark (`/_nuxt/card-logo.CkINcT4q.svg`)
- Used as the engraved graphic on the membership card surface
- Behaves like an etched ID-card emblem, not a corporate logo placement

## 5. Layout Principles

### Spacing System
- Base unit: `8px` (with `4px` and `7px` as compact sub-units for chrome)
- Scale: `4px, 7px, 12px, 16px, 24px, 31.36px, 52.28px, 64px, 73.19px, 96px, 97.2px`
- Notable: Mainframe uses *fractional pixel values* (`31.36px`, `52.28px`, `73.19px`) generated by clamp expressions — these are not arbitrary, they're the interpolated mid-points of fluid responsive scales. The system breathes proportionally with the viewport rather than snapping at breakpoints.

### Grid & Container
- The page is wrapped in a fixed-aspect frame (`_frameBorder`) — not a max-width container
- Internal sections use `grid-template-areas` with named regions: `t` (text), `g` (graphic), `c` (caption), `p` (primary), `s` (secondary), `m` (membership), `l` (leading)
- 9-column or 17-column grids depending on section — the editorial rhythm shifts mid-page
- Padding inside the frame: `9dvh 7.5dvw` (using dynamic viewport units, not pixel padding)
- Section gaps: `clamp(72px → 96px)` vertical, `clamp(32px → 64px)` for tight pairs

### Whitespace Philosophy
- **Editorial pacing inside a fixed window**: Because content lives inside the monitor frame, every section gets generous internal breathing room (`9dvh` vertical padding) but the outer container does not grow — composition discipline replaces sprawl
- **Asymmetric gutters via grid-template-areas**: Empty cells (`.`) in the grid create deliberate negative-space columns, so a paragraph might occupy columns 3-9 while a graphic occupies columns 12-15, leaving columns 1-2 and 10-11 deliberately empty
- **Fluid type + fluid space**: Both type sizes and gap values use `clamp()` with viewport interpolation, so the page never feels under-sized on small screens or over-stretched on large ones
- **Section-as-screen rhythm**: Each section is a self-contained "screen" of the monitor — there are no decorative dividers, but each section reads as a chapter because its grid composition resets

### Border Radius Scale
- Sharp (0px): Inputs only — text fields stay rectangular
- Small (2px): Spans, the canvas element — barely-there softening
- Medium (8px): Buttons, soft cards — the workhorse rounding
- Frame (clamp 16-24px): The monitor frame's outer corners — fluid with viewport
- Large (42px): Pill-shaped framed sections, when used
- Pattern: rectangular for content, generously rounded for the device-frame metaphor

## 6. Depth & Elevation

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | No shadow | Body text, paragraphs, structural containers |
| Texture (Level 1) | Eggshell texture (60% opacity) + noise (3% opacity) | Canvas, frame surfaces — material warmth without elevation |
| Inset Hairline (Level 2) | `1px solid rgba(41, 41, 41, 0.16)` | Input borders, divider rules |
| Soft Card (Level 3) | `box-shadow: 0 48px 112px -32px rgba(41, 41, 41, 0.3)` | Membership card, product cards — long, soft, atmospheric drop |
| Screen Glare (Level 4) | Linear + radial gradient combo (graphite tint + white halo at top) | Inside the monitor frame — simulates light catching a CRT glass tube |

**Shadow Philosophy**: Mainframe's depth system is photographic, not graphic. Where Cape uses hard offset stamps and most product pages use blurred elevation cards, Mainframe uses one signature shadow — a long, soft, deeply offset cast (`0 48px 112px -32px`) — that reads like a museum object photographed under raking light. The shadow is far too long for a UI panel; it's the shadow you get from a physical object lit from above. Combined with the eggshell paper texture, this creates the "object on a curated table" mood that the entire page depends on. Soft drop shadows do not appear on buttons or chrome — only on the hero card-like artifacts that the page wants you to perceive as physical.

### Decorative Depth
- The screen-glare gradient inside the frame is the only "atmospheric" effect — it implies a light source, not an elevation
- Texture layers are blended (not stacked) — `mix-blend-mode` is used to let the noise grain interact with the eggshell rather than sit on top
- No glow effects, no neon — the red signal color is rendered as a flat fill, never with a glow

## 7. Do's and Don'ts

### Do
- Use exactly three colors: graphite (`#292929`), eggshell (`#e2deda`), signal red (`#eb4e3d`) — nothing else
- Apply Signal Red sparingly — one occurrence per screen as a status, underline, or power-light moment
- Layer the eggshell texture (60% opacity) + noise grain (3%) on every canvas surface — the material warmth is the brand
- Wrap content in a frame-border device — even mini-sections benefit from the bezel metaphor
- Use CSS `grid-template-areas` for editorial layouts with named regions (`t`, `g`, `c`, `p`, `s`)
- Use `clamp()` with viewport-width interpolation for every type size and major gap value — fluid scaling, no breakpoint pops
- Pair `PP Neue Montreal` for prose with `Consolas` for terminal/data and `SimpleLLWeb-Bold` for monumental display
- Use `writing-mode: vertical-rl` for serial-number metadata on edge positions
- Apply scanline rules to display headlines for the CRT raster-line effect
- Lock graphics to `aspect-ratio` values rather than fixed pixel heights — composition stays stable across viewports
- Force lowercase on nav links via `text-transform` for the modernist editorial tic

### Don't
- Don't introduce a fourth color — no blue, no green, no neutral grey scale beyond graphite tints
- Don't over-apply Signal Red — it stops being a signal if it appears more than once per screen
- Don't use blurred elevation shadows on buttons or cards — the only soft shadow is the long museum-object cast
- Don't use rounded corners on inputs — they stay sharp (radius 0); rounding belongs to buttons and frames
- Don't use sans-serif for terminal/data content — Consolas owns that role
- Don't mix Consolas into body prose — it's metadata-only
- Don't use a max-width container — wrap everything in the frame-border device instead
- Don't drop the textures — pure flat `#e2deda` reads as digital, not material
- Don't use bold (700) on `PP Neue Montreal` for hero display — that's `SimpleLLWeb-Bold`'s job
- Don't snap layout at breakpoints — the system is fluid, use clamp() and dvh/dvw units
- Don't break the monitor metaphor — adding decorative chrome that isn't a hardware element pulls the page apart

## 8. Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile Small | <480px | Frame device collapses to a stylized retro-Mac window; pink/cream variant; dock icons row |
| Mobile | 480–768px | Single-column manifesto reading; ENTER hero shrinks but keeps scanlines |
| Tablet | 768–1024px | Frame device returns; grid-template-areas drop to 2-column variants |
| Desktop | 1024–1480px | Full monitor-frame metaphor; multi-column grid layouts; 17-column rhythm |
| Large Desktop | ≥1480px | Maximum scale — fluid clamps cap, type plateaus, frame breathes wider |

### Touch Targets
- Primary CTAs: 40px+ tap height with generous padding
- Nav links: 44px+ vertical hit area, even when text is small
- Dock app tiles (mobile): 48px+ square targets

### Collapsing Strategy
- **Frame device**: Desktop CRT-monitor metaphor → mobile reframes as classic Mac System window, complete with TV static and dock — the metaphor adapts but does not disappear
- **ENTER headline**: Scales from `52.28px` peak down to `33px` minimum via clamp() interpolation; scanlines remain proportional
- **Grid sections**: 17-column desktop grids → 9-column tablet → single-column mobile stacks
- **Membership card**: Locked aspect ratio, scales proportionally — never reflows internally
- **Padding**: Switches from `9dvh 7.5dvw` (viewport-relative) to `9dvh 8px` on mobile — vertical breathing preserved, horizontal collapses
- **Vertical-rl serials**: Hidden on mobile or rotated to horizontal label
- **Texture overlays**: Maintained at all breakpoints — material warmth is non-negotiable

### Image Behavior
- Aspect-ratio-locked graphics maintain crops across all breakpoints — never crop algorithmically
- Lottie/Rive animations (oxygen lines, typing text, app icons) scale proportionally inside their grid cells
- The card-logo SVG remains contained — never crops, never reflows
- Hero scanline overlays scale with type, preserving the CRT raster proportion

## 9. Agent Prompt Guide

### Quick Color Reference
- Page Background: Mainframe Eggshell (`#e2deda`) + eggshell texture overlay
- Primary Text: Mainframe Graphite (`#292929`)
- Inverted Text: Mainframe Eggshell (`#e2deda`)
- Brand Accent / Signal: Signal Red (`#eb4e3d`)
- Button Background: Graphite 10% (`rgba(41, 41, 41, 0.1)`)
- Hover Fill: Mainframe Graphite (`#292929`) with white text
- Input Border: `1px solid rgba(41, 41, 41, 0.16)`
- Card Shadow: `0 48px 112px -32px rgba(41, 41, 41, 0.3)`

### Example Component Prompts
- "Build a hero section on Mainframe Eggshell (`#e2deda`) wrapped in a rounded `clamp(16px, 24px)` frame border with a soft drop shadow `0 48px 112px -32px rgba(41,41,41,0.3)`. Inside the frame, place a small line of `PP Neue Montreal 17px weight 400` reading 'Once upon a time, we pressed' followed by a colossal `SimpleLLWeb-Bold` headline 'ENTER' at `clamp(2.06rem, 3.25rem)`, weight 700, line-height 0.98, letter-spacing -0.08em. Slice horizontal scanline rules across the headline at every 8px."
- "Design a membership card — graphite background (`#292929`) with a 60%-opacity eggshell paper texture on top. Layout via CSS grid-template-areas: `'. . g g g g g g g . t t t t t . .'`. Place the brand SVG mark in the `g` region, and stack 'Mainframe Computer' / serial number / cohort / date as `Consolas 17px weight 400 letter-spacing -1.36px` in the `t` region. Add a vertical-rl serial number reading down the right edge at `9.22px Caption Small`."
- "Create a primary button with `border-radius: 8px`, background `rgba(41, 41, 41, 0.1)`, text `#292929`, font `PP Neue Montreal weight 400`. On hover, fill background to solid `#292929` and flip text to `#ffffff`. On focus, background → `rgba(41, 41, 41, 0.15)`, outline removed."
- "Build a top metadata strip styled like a CRT bezel — left side has 'Mainframe Computer, Inc.' wordmark and copyright line in `label-01` (PP Neue Montreal 500 weight, ~13px). Right side has lowercase nav links 'blog ↗ careers ↗ @mainframe' with 8×8 SVG arrow glyphs and red-underline hover."
- "Design an email signup input — transparent background, `1px solid rgba(41, 41, 41, 0.16)` border, `0px` radius, `12px 16px 0px` padding, `PP Neue Montreal 17px`. On focus, border-color → solid `#292929`."

### Iteration Guide
1. Start with the frame-border device — wrap everything inside the monitor metaphor before composing internal content
2. Three colors only: graphite, eggshell, signal red. If you reach for a fourth, the system is broken
3. Layer the eggshell paper texture (60%) and noise grain (3%) on every canvas — flat eggshell looks digital, textured eggshell reads as material
4. Use `clamp()` with viewport-width interpolation for type and gaps — never hard-code px sizes that don't fluidly scale
5. Use CSS `grid-template-areas` with named regions (`t`, `g`, `c`, `p`, `s`) — flex layouts will not produce the editorial composition this brand demands
6. The Signal Red is sacred — one application per screen as a status, underline, or power-light. More than one, and the system loses its bite
7. Pair `PP Neue Montreal` (sans, body) with `Consolas` (terminal data) and `SimpleLLWeb-Bold` (display monuments). Never mix roles
8. Use `writing-mode: vertical-rl` for serial numbers and edge metadata — print-graphic small caps on the bezel
9. Apply scanline rules to display headlines for the CRT raster effect — large type without scanlines reads as generic editorial
10. The shadow is one specific value: `0 48px 112px -32px rgba(41,41,41,0.3)`. No other shadows. No glows. No blurs.
