# Design System Inspired by A24

## 1. Visual Theme & Atmosphere

A24's website is editorial film brutalism — a digital cinemagazine where typography, imagery, and negative space are the only materials. The entire system runs on a pure monochromatic palette (`#000000`, `#ffffff`, `#888888`) with zero chromatic color anywhere. Where every other streaming/studio site leans into poster art, trailer reels, and algorithmic recommendations, A24's page opens with a darkened, out-of-focus still image and a list of film titles rendered as oversized serif-adjacent typography — the way a film critic might notate upcoming releases in a leather-bound notebook.

The signature move is the custom `NB International Web` typeface — a grotesk with pronounced geometric bones — deployed at extreme negative letter-spacing (`-2.96px` at 74px) and condensed line-height (`0.92`). This is the opposite of comfortable: the letterforms lock together into dense masses that read as inscriptions rather than sentences. The film titles ("The Drama", "Mother Mary", "Backrooms") are listed with a small superscript year annotation — a deliberate editorial gesture that turns a homepage into a publication's masthead. Nothing apologizes for the density.

What truly defines A24 is its **refusal of digital chrome**. There are no drop shadows on buttons (because there are barely any buttons). No rounded corners. No gradients. No color accents. No illustrations. The only "UI" is menu chrome in grey (`#888888`) at the top of the viewport and a newsletter dialog that appears as a dark-panel overlay. Everything else — film promotion, brand expression, navigation — happens through typography and cinematic imagery. The entire system is an exercise in subtraction.

**Key Characteristics:**
- Pure monochrome palette — black, white, mid-grey, nothing else
- NB International Web at extreme negative tracking (`-2.96px` at 74px) and tight line-height (`0.92`)
- Zero border-radius on all content surfaces — sharp editorial corners
- Darkened photographic imagery as backdrop (not as decoration — as atmosphere)
- Film titles rendered as oversized editorial lists with superscript year annotations
- Newsletter/modal dialogs as dark panels with soft layered shadows
- No visible drop shadows on primary content elements — depth comes from blur and overlay
- Minimal menu chrome — "MENU" / "A24" wordmark / search icon only

## 2. Color Palette & Roles

### Primary
- **A24 Black** (`#000000`): The system's primary color — page backgrounds, dark panel fills, primary text on light surfaces, icon fills. Pure, unsoftened black.
- **A24 White** (`#ffffff`): Primary text on dark surfaces, headline color, button fill (when buttons appear), contrast element against black imagery.
- **Editorial Grey** (`#888888`): Secondary text, menu chrome, muted UI indicators, image captions, metadata (years, credits). The only mid-tone in the entire system.

### Accent Colors
- **Cinema Blue** (`#1883fd`): A single accent hex that appears in hover states for specific links — the rare chromatic moment in an otherwise monochrome system. Used exclusively for interactive state change, never for branding or decoration.

### Surface & Background
- **Pure Black** (`#000000`): Dark section backgrounds, overlay panels, modal dialogs.
- **Pure White** (`#ffffff`): Light section backgrounds (rare on homepage, more common on film detail pages).
- **Image Backdrop**: Photographic or video backgrounds always applied with a slight blur/darken filter so title type sits legibly atop — never pure imagery, always slightly scrimmed.

### Neutrals & Text
- **Title White** (`#ffffff`): All display typography on dark backgrounds.
- **Body White** (`#ffffff` at varying opacity): Body copy on dark panels.
- **Menu Grey** (`#888888`): Navigation text, metadata, de-emphasized labels, secondary copy.
- **Shadow Grey Warm** (`#c7c5c7`): Rare warm-gray used only in highly specific shadow/glow treatments.

### Semantic Usage
- **Dividers**: Fine `1px solid rgba(255,255,255,0.1)` on dark, `1px solid rgba(0,0,0,0.1)` on light — barely visible.
- **Input borders**: `rgba(255, 255, 255, 0.3)` on dark dialog inputs.

### Gradient System
- A24 is **strictly gradient-free**. Depth and contrast come from solid-color relationships and selectively darkened photographic backgrounds. Any appearance of gradient is purely in blurred photographic imagery — never as a CSS effect on UI surfaces.

## 3. Typography Rules

### Font Family
- **Primary**: `NB International Web` (custom), with fallback: `Helvetica Neue`, `Helvetica`, `Arial`
- **Mono / Technical**: Same NB International Web for UI chrome — the typeface handles both display and utility roles
- **OpenType Features**: Standard only — the typeface's built-in character is the style

*Note: NB International is a commercial typeface from Neubau Berlin. For external implementations, Founders Grotesk or GT America serve as close substitutes; Helvetica Neue is the explicit fallback.*

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Display Hero / Title | NB International Web | 74px (4.63rem) | 500 | 0.92 (very tight) | -2.96px | Maximum size — film titles, homepage master list |
| Section Heading Large | NB International Web | 40–50px | 500–600 | 0.95–1.00 | -1.5 to -2.0px | Secondary display moments |
| Section Heading | NB International Web | 27px (1.69rem) | 400 | — | — | Film year annotations, minor headers |
| Sub-heading Bold | NB International Web | 26.656px (1.67rem) | 600 | 1.20 | normal | Panel headings, feature titles |
| Sub-heading | NB International Web | 21px (1.31rem) | 500 | 1.00 | 0.3px | Card labels, navigation prominence |
| Button / Emphasis | NB International Web | 19.2px (1.20rem) | 600 | 1.00 | normal | Button labels (rare — "SIGN UP") |
| Body Large | NB International Web | 18px (1.13rem) | 400 | 1.33 | -0.225px | Editorial body copy |
| Body / Button Heavy | NB International Web | 16px (1.00rem) | 400–700 | 1.30–1.40 | normal | Standard reading text, button labels |
| Link Body | NB International Web | 15px (0.94rem) | 400 | 1.07–1.67 | -0.075px | Navigation, inline links |
| Caption / Label | NB International Web | 12–14px | 400–500 | 1.20–1.50 | normal | Metadata, image captions, chrome labels |
| Micro / Year | NB International Web | 10–12px | 400 | 1.00 | normal | Superscript year annotations next to titles |

### Principles
- **Extreme tight tracking as signature**: Display typography runs at `-2.96px` letter-spacing — aggressive enough that letterforms nearly touch. This is the brand's single most recognizable typographic move.
- **Condensed line-height**: Headline line-height of `0.92` (below 1.0) lets stacked title lines compress into dense blocks. Think stacked film titles at the edges of a magazine spread.
- **Mixed weights, no bold convention**: The system uses weights 400–700 fluidly — there's no "headings are bold, body is regular" convention. Weight is applied for tonal variety within a dense monochrome field.
- **Superscript annotations**: Year markers (`2026`, `2025`) appear as small superscript-style metadata attached to titles — an editorial typographic device borrowed from print magazines.
- **No script, no serif, no alternatives**: Only NB International Web, throughout. One typeface carries everything.
- **Uppercase for UI only**: Display text is title-case or proper case. Uppercase is reserved for menu chrome ("MENU") and occasional emphasis ("WANT MORE A24?").

## 4. Component Stylings

### Buttons

A24 has almost no traditional buttons — the site is link-driven. When buttons do appear (mostly in dialogs and forms), they follow a minimal treatment:

**Newsletter Signup Button**
- Background: Pure White (`#ffffff`)
- Text: A24 Black (`#000000`)
- Padding: 12px 20px
- Radius: `0px` (sharp rectangular)
- Border: `0px`
- Font: 16px NB International Web weight 700, tracking normal
- Hover: minimal state change — opacity shift or subtle background darken
- Use: Dialog CTAs ("SIGN UP"), newsletter submission

**Inverted Black Button**
- Background: A24 Black (`#000000`)
- Text: Pure White (`#ffffff`)
- Padding: 12px 20px
- Radius: `0px`
- Use: CTAs on light/white backgrounds

**Close / Dismiss Icon**
- Background: transparent
- Icon: 24×24px X-shape in white or black depending on surface
- No background fill, no border — icon alone

### Cards & Containers
- Background: `#000000` on dark sections, `#ffffff` on light sections — no mid-tone panels
- Border: `0px` default, or `1px solid rgba(255,255,255,0.1)` / `rgba(0,0,0,0.1)` for section dividers
- Radius: `0px` (sharp rectangular) for all content surfaces
- Shadow: layered soft shadows for dialog overlays (see Depth section)
- Internal padding: generous — 32–64px for editorial content cards

### Dialogs / Modals
**Newsletter Dialog**
- Background: pure `#000000` panel centered on blurred-darkened backdrop
- Panel width: ~400–480px
- Radius: `0px` (sharp)
- Shadow: multi-layer directional soft shadow (`rgba(0,0,0,0.02) 2.8px 2.8px 2.2px → rgba(0,0,0,0.07) 100px 100px 80px`) — extremely soft, almost invisible, present for form rather than function
- Padding: 32–40px
- Title: 16–18px NB International Web weight 500–600, uppercase
- Input: transparent background, `1px solid rgba(255,255,255,0.3)` border, white text
- Close button: X icon top-right, 24×24px

### Badges / Tags / Pills
**Year Annotation**
- Inline superscript-style: `10–12px` NB International Web weight 400
- Placed directly after film title, slightly raised
- No background, no border — pure typographic metadata

**Minimal Category Tag**
- Transparent background
- Text: uppercase 12px
- `0px` radius, letter-spacing `0.05em`
- Use: "DRAMA", "HORROR" category tags on film detail pages

### Inputs & Forms
- Background: transparent on dark panels, `#ffffff` on light
- Border: `1px solid rgba(255, 255, 255, 0.3)` on dark, `1px solid #000` on light
- Radius: `0–3px` (nearly sharp)
- Font: 15–16px NB International Web weight 400
- Placeholder: grey (`#888888`)
- Focus: border brightens to full white (`rgba(255,255,255,1)`) on dark, or a 1px inset outline on light

### Navigation
- Top nav: sparse horizontal bar — "MENU" (left), "A24" wordmark (center), search icon (right)
- All chrome in Editorial Grey (`#888888`) or white depending on surface
- Links inline, 15px NB International Web weight 400
- Hover: link color transitions to Cinema Blue (`#1883fd`) — the system's only chromatic moment
- Sticky behavior: nav remains fixed at top, imagery scrolls beneath
- Mobile: "MENU" label expands to full-screen takeover menu

### Decorative Elements

**Darkened Backdrop Imagery**
- Photographic or video backgrounds — always darkened/scrimmed for text legibility
- Applied as `background-image` with overlay `rgba(0,0,0,0.4-0.6)` or CSS `filter: brightness(0.6)`
- Film imagery is always cinematic, never stock — treated as brand asset, not decoration

**Title Masthead List**
- Stacked film titles with superscript year annotations
- Left-aligned or centered, full-width max
- Active/featured title in full white; upcoming titles in slightly dimmed white or grey
- The page layout IS this list — no additional hero treatment needed

## 5. Layout Principles

### Spacing System
- Base unit: 8px with a fine sub-unit at 4px
- Scale: 4px, 5px, 6px, 8px, 9px, 10px, 12px, 15px, 20px, 22px, 40px, 80px, 160px
- Notable: The scale is generous at the section level — 80px+ between major sections. Small UI chrome uses the 4–15px range for dense precision.

### Grid & Container
- Max content width: approximately 1400–1500px for centered content
- Full-bleed breakouts dominate — imagery typically fills the viewport
- Two-column layouts appear on film detail pages (poster left, metadata right)
- Homepage is effectively a single-column display: imagery + title masthead list

### Whitespace Philosophy
- **Editorial sparseness**: The page uses massive negative space — especially around the title masthead. Film titles sit on the lower-left of a mostly-empty frame, letting the darkened backdrop image breathe
- **Type-anchored rhythm**: The title list establishes the only typographic hierarchy — everything else steps back to support it
- **Cinematic pacing**: Scroll reveals unfold like film cuts — one frame gives way to another with generous vertical breathing room

### Breakpoint Density
A24 ships with an unusually dense breakpoint list (2000px, 1600px, 1300px, 1024px, 896px, 768px, 640px, 530px, 425px, 371px, 360px) — the system is tuned for pixel-precise layout across hero imagery and title mastheads at every device width.

### Border Radius Scale
- Sharp (0px): Default for **everything** — buttons, cards, panels, inputs, dialogs, images
- Near-sharp (2–3px): Rare, used only on specific utility elements (cookie search box)
- Pill (46–50px): Reserved exclusively for toggle switches
- The system's radius philosophy is: sharp by default, pill only for functional switches. No mid-range.

## 6. Depth & Elevation

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | No shadow, no border | Page background, imagery, section containers |
| Hairline Divider (Level 1) | `1px solid rgba(255,255,255,0.1)` or `rgba(0,0,0,0.1)` | Section separators, menu item dividers |
| Dialog Layered (Level 2) | Multi-layer soft directional shadow (see formula below) | Modal dialogs, newsletter panels, overlay cards |
| Scrim Overlay (Level 3) | `rgba(0,0,0,0.4–0.6)` overlay on imagery | Darkening hero imagery for text legibility |
| Inset Warm Glow (Level 4) | `rgb(199, 197, 199) 0px 0px 12px 2px` | Rare — specialty hover/focus states |

**Multi-Layer Dialog Shadow Formula**:
```
rgba(0, 0, 0, 0.02) 2.8px 2.8px 2.2px 0px,
rgba(0, 0, 0, 0.027) 6.7px 6.7px 5.3px 0px,
rgba(0, 0, 0, 0.035) 12.5px 12.5px 10px 0px,
rgba(0, 0, 0, 0.043) 22.3px 22.3px 17.9px 0px,
rgba(0, 0, 0, 0.05) 41.8px 41.8px 33.4px 0px,
rgba(0, 0, 0, 0.07) 100px 100px 80px 0px
```
Six progressive layers from tight (2.8px) to expansive (100px), each slightly more transparent. Creates imperceptible-but-present depth under dialog panels. Directional — always cast down-right or up-right for stylistic consistency.

**Shadow Philosophy**: A24's depth system is almost invisible by design. Where most sites use shadows to signal "this element is interactive" or "this element is elevated", A24 hides shadows so subtly that they function more like structural hints than visual effects. The six-layer directional stack creates natural-feeling depth without any single layer being noticeable. On content elements (not dialogs), there are no shadows at all — depth comes entirely from the darkened backdrop imagery and solid-color contrast.

### Decorative Depth
- Photographic scrim overlays are the primary depth mechanism — darker imagery reads as background, lighter as foreground
- Blurred backdrops (CSS `filter: blur(8–16px)`) behind modal dialogs create clear foreground/background separation without any shadow
- No ambient shadows, no glow effects on content — depth is always either photographic or dialog-specific

## 7. Do's and Don'ts

### Do
- Use NB International Web (or Helvetica Neue fallback) for ALL typography — single-typeface system
- Apply extreme negative letter-spacing (`-2.96px`) at display sizes for the signature tight-tracked titles
- Keep line-height tight (`0.92–1.00`) on display type — condensed stacks are the look
- Use pure monochrome (`#000000`, `#ffffff`, `#888888`) — no chromatic color except rare Cinema Blue hover
- Apply `0px` border-radius to all content surfaces — sharp corners are non-negotiable
- Use darkened/blurred photographic imagery as the primary backdrop and atmosphere
- Render film titles as editorial lists with superscript year annotations
- Apply multi-layer soft shadows only to dialog/modal panels, never to content elements
- Preserve generous negative space — especially around title mastheads

### Don't
- Don't introduce any chromatic color beyond the rare Cinema Blue (`#1883fd`) hover state
- Don't use rounded corners on content — `0px` is a rule, not a default
- Don't add drop shadows to buttons, cards, or content blocks — depth comes from imagery
- Don't use gradients anywhere — solid color only
- Don't use multiple typefaces — NB International Web or Helvetica Neue for everything
- Don't use opacity washes or translucent colored tints — the system is binary (fully opaque or fully transparent)
- Don't default to positive or neutral letter-spacing on display type — tight negative tracking is the brand
- Don't add decorative icons or illustrations — typography and imagery carry all visual work
- Don't use pill-radius on buttons or cards — pill is reserved for functional toggles only
- Don't soften text color to dark-grey for body — either full white/black or the `#888888` editorial grey

## 8. Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Small Mobile | <400px | Reduced hero title (40–48px), stacked single-column |
| Mobile | 400–640px | Hero title 48–56px, mobile menu drawer |
| Large Mobile | 640–768px | Hero title 56–64px, adjusted chrome |
| Tablet | 768–1024px | Multi-column detail pages, hero 64–72px |
| Desktop | 1024–1550px | Full layout, hero at 72–74px |
| Large Desktop | ≥1550px | Maximum scale (74px+ hero), maximum container width |
| XL Cinema | ≥2000px | Specialized scaling for ultra-wide — large imagery, massive mastheads |

### Touch Targets
- Nav links: 15–16px with adequate surrounding padding
- Menu icon / hamburger: min 44×44px tap area
- Dialog close (X): min 24×24px icon with 40×40px tap area
- Newsletter input: standard 48px tap-height input

### Collapsing Strategy
- **Nav**: Horizontal "MENU / A24 / SEARCH" chrome collapses to simplified three-icon bar on mobile
- **Title Masthead**: Homepage film list scales proportionally — 74px desktop → 48–56px tablet → 40–48px mobile
- **Modal dialogs**: Full-width (minus 16px margin) on mobile, centered constrained-width on desktop
- **Imagery**: Hero imagery retains full-bleed treatment at all breakpoints, aspect ratios adjust
- **Section spacing**: Generous 160px desktop → 80–100px mobile — reduces but maintains cinematic pace
- **Letter-spacing**: Negative tracking scales proportionally — `-2.96px` at 74px becomes `-1.5px` at 40px

### Image Behavior
- Hero imagery maintains full-bleed, cinematic aspect at all sizes
- Darkening/blur scrims adapt intensity based on background luminance
- No art direction swaps between breakpoints — the same imagery adapts
- Film poster imagery (on detail pages) maintains 2:3 aspect ratio

## 9. Agent Prompt Guide

### Quick Color Reference
- Primary Text (light bg): A24 Black (`#000000`)
- Primary Text (dark bg): A24 White (`#ffffff`)
- Secondary Text: Editorial Grey (`#888888`)
- Page Background (dark): Pure Black (`#000000`)
- Page Background (light): Pure White (`#ffffff`)
- Hover Accent (rare): Cinema Blue (`#1883fd`)
- Backdrop Scrim: `rgba(0, 0, 0, 0.4)` to `rgba(0, 0, 0, 0.6)`

### Example Component Prompts
- "Create a homepage hero with a darkened photographic backdrop (scrim `rgba(0,0,0,0.5)`). Overlay a masthead film list bottom-left: four or five film titles in NB International Web 74px weight 500, line-height 0.92, letter-spacing -2.96px, pure white (`#ffffff`). After each title, place a superscript year annotation in 10–12px weight 400, same typeface, slightly dimmed white."
- "Design a newsletter modal dialog: pure black (`#000000`) panel, 0px radius, centered over blurred-darkened backdrop. Title in uppercase 16–18px NB International Web weight 500–600. Body text in 15px weight 400 with line-height 1.67. Transparent input with `1px solid rgba(255,255,255,0.3)` border. White-background button with black text, 12px 20px padding, 16px NB International Web weight 700. Apply the six-layer soft directional shadow for natural depth."
- "Build a top navigation bar on dark imagery: 'MENU' label left (15px grey `#888888`), 'A24' wordmark centered (white, NB International Web), search icon right (white). All items with 15px NB International Web weight 400. Hover on links transitions text to Cinema Blue (`#1883fd`)."
- "Create a film title block — title in NB International Web 74px weight 500, line-height 0.92, letter-spacing -2.96px, pure white. Year annotation in 10–12px weight 400, superscript-style, positioned directly after title. Optional category tag below in uppercase 12px weight 400, letter-spacing 0.05em, grey."
- "Design a section divider — `1px solid rgba(255,255,255,0.1)` on dark backgrounds or `rgba(0,0,0,0.1)` on light. 40–80px vertical margin above and below. No decorative treatment — pure structural line."

### Iteration Guide
1. Typography is the entire design — invest in letter-spacing and line-height first, layout second
2. Apply `-2.96px` letter-spacing on all display type at 60px+ — this is the signature
3. Line-height `0.92` on headline stacks, `1.00` on single-line display — condensed is the look
4. Monochrome is a rule, not a preference — three hexes (`#000`, `#fff`, `#888`) cover 99% of all color decisions
5. Zero border-radius — never introduce rounded corners on content surfaces
6. Use darkened photographic imagery as the primary depth and atmosphere mechanism
7. Apply the six-layer directional shadow only to dialog/modal panels — never to content
8. Reserve Cinema Blue (`#1883fd`) for hover states only — one or two applications per page maximum
9. Single-typeface discipline — NB International Web (or Helvetica Neue fallback) everywhere, no exceptions
10. Generous negative space — especially around title mastheads. The empty frame IS the composition
