---
slug: sega
name: Sega
url: https://www.sega.com
domain: sega.com
category: Gaming
styles: [Dark, Bold, Colorful]
tagline: "Deep navy arcade chrome, electric-blue CTAs, and heavyweight uppercase type at 144px"
fonts: [Inter Tight, Poppins, Arial]
primary_color: "#0057ff"
---

# Design System Inspired by Sega

> Deep navy arcade chrome, electric-blue CTAs, and heavyweight uppercase type at 144px

## 1. Visual Theme & Atmosphere

Sega's website is a digital arcade cabinet — a high-energy, dark-field entertainment portal where game worlds collide on a single screen without apology. The page opens on a deep navy void (`#002366`) punctuated by full-bleed game art panels: Yakuza characters snarling at the camera, Persona anniversary typography exploding across the frame in red and black, Alien Isolation dissolving in acid-green shadow. The canvas is fundamentally dark — not the quiet darkness of a luxury brand, but the charged darkness of a CRT monitor in a 1990s arcade, where every illuminated element pops with the urgency of a high-score notification. This is a company that has been making things glow for fifty years, and its website knows it.

The typographic engine running beneath all this visual intensity is Inter Tight at weight 800 — a compressed, aggressive grotesque that earns its keep at display sizes by refusing to waste horizontal space. At 144px with a line-height of 0.75 and `text-transform: uppercase`, section headings like "WORLDS" become typographic architecture, not text. They function more like structural elements — steel girders holding up the game art above them — than readable copy. This is headline type as spectacle: the words matter less than the visual mass they create against the blue-black background. At smaller sizes (20–48px), the same uppercase treatment in Inter Tight 800 maintains the pulse, turning navigation links and section labels into punchy UI chrome.

What unifies the visual intensity is a surprisingly disciplined three-color hierarchy. Sega Blue (`#002366`) is the container, the void, the dark matter that holds everything together. Electric Blue (`#0057ff`) is the primary interactive signal — the color of CTAs, link hover states, game card accents, and carousel navigation. Between these two blues, `#3379ff` (`--color-sega-primary-400`) serves as a mid-tone hover state and interactive feedback color. Combined with white text and game-specific accent colors injected from each title's own visual identity (Persona's red and black, Alien's toxic green), the system has the structured chaos of a well-designed arcade floor: each cabinet has its own personality, but the carpeting is the same.

**Key Characteristics:**
- Inter Tight weight 800 uppercase as the brand's headline voice — maximum compression, maximum presence at 144px, line-height 0.75
- Deep navy canvas (`#002366`) as the primary background — not black, but a saturated dark blue that reads as brand-owned darkness
- Electric blue (`#0057ff`) as the exclusive interactive accent — every link, CTA, badge, and hover state in the system
- `#3379ff` as the primary-400 hover feedback color, creating a legible two-stop blue ramp
- Full-bleed game art panels as the primary visual content — each title's world bleeds edge-to-edge without chrome or framing
- Near-zero letter-spacing on display type; uppercase + tight line-height creates text-as-mass
- Pill badges (`border-radius: 48px`) for game category tags — white background, blue text, a clean interruption in the dark field
- Carousel-driven content delivery with circular chevron navigation and Swiper.js infrastructure
- Hard white borders (2px and 4px solid `#ffffff`) used as structural dividers and button outlines
- `rgba(0, 0, 0, 0.2) 0px 16px 48px 0px` as the signature card shadow — deep, soft, pure dark

## 2. Color Palette & Roles

### Primary Brand
- **Sega Navy** (`#002366`): The foundational canvas color — page backgrounds, section fills, header backgrounds, and the `logo.background` value. A highly saturated royal blue that reads as brand-owned darkness, distinct from either pure black or generic dark gray.
- **Near Black Navy** (`#0d1126`): Secondary dark surface — used for layout containers, certain section backgrounds, and disabled-state carousel buttons at 50% opacity. Almost imperceptibly blue against the Sega Navy field.

### Brand Accent
- **Electric Blue** (`#0057ff`): The chromatic signature of the entire system. Primary CTAs, game card accent icons, link colors on dark surfaces, badge text, carousel navigation hover, and the interactive heartbeat of every component. The single most important hex in the system.
- **Brand Blue Mid** (`#3379ff`): `--color-sega-primary-400` — hover state for buttons and links. A lighter, more luminous blue that signals activation without jumping out of the blue family.
- **Sega Tertiary** (`#3649a5`): `--color-sega-tertiary-0` — a mid-dark indigo for layered UI surfaces, secondary backgrounds within dark sections, and structural depth between the navy and the electric blue.

### Semantic Light
- **Pale Blue** (`#e1eaff`): `--color-sega-secondary-0` — the semantic primary color in the extraction. Used for link hover states on white backgrounds and soft-tinted text elements on dark fields. A barely-there blue tint that whispers interactivity.
- **Light Wash** (`#f4f6f9`): Near-white with a blue undertone — alternate light surface for specific contrast contexts. The lightest surface in the system before reaching pure white.

### Text & Surfaces
- **Pure White** (`#ffffff`): Primary text on all dark surfaces, button labels on ghost buttons, section headers, badge backgrounds, and the dominant content color across the entire dark-theme page.
- **Pure Black** (`#000000`): Text in light-surface contexts (cookie consent overlays, external tool overlays). The system's only true neutral.

### Warning & Status
- **Sega Warning** (`#daa125`): `--color-sega-warning-500` — an amber-gold for warning states. Warm and readable against dark backgrounds without competing with the blue accent palette.
- **Input Border Gray** (`rgb(166, 167, 191)`): The only truly neutral border color — used on text input outlines in form contexts. A muted blue-gray that sits between system grays and the brand blues.

### Game-Specific Accents (CSS Variables — Contextual Only)
These appear scoped to individual game sections and should not be used as global UI colors:
- **Persona Red** (`#ff0000` / `#e50012`): Persona franchise — `--color-per-primary-0`, `--color-per4r-primary-400`
- **Neon Magenta** (`#f948ff` / `#fa66ff`): Sonic Colors / Shadow DT — `--color-sthdt-secondary-0`, `--color-sthdt-secondary-300`
- **Acid Green** (`#0f0` / `#86fc5c`): Alien Isolation / RAI — `--color-per4r-tertiary-0`, `--color-rai-warning-0`
- **SMT Deep Red** (`#e10028`): Shin Megami Tensei — `--color-smtv-primary-0`
- **Football Manager Orange** (`#f97e39`): TWW / FM — `--color-tww40-primary-400`

### Shadow Colors
- **Primary Shadow** (`rgba(0, 0, 0, 0.2)`): Deep soft shadow for cards and elevated panels — `0px 16px 48px 0px`
- **Secondary Shadow** (`rgba(0, 0, 0, 0.15)`): Directional soft shadow for carousel navigation buttons — `-2px 2px 6px 0px`

## 3. Typography Rules

### Font Family
- **Primary Display**: `Inter Tight`, with fallback: `system-ui, -apple-system, sans-serif`
- **Secondary/Body**: `Poppins`, with fallback: `Arial, sans-serif`
- **Utility/Fallback**: `Arial`, `ui-sans-serif`, `system-ui`
- **OpenType Features**: Variable font support confirmed. No explicit stylistic sets; the character comes from weight 800 + uppercase transform combination.

*Note: Both Inter Tight and Poppins are served via Google Fonts. Inter Tight at 800 is the display voice; Poppins handles body, captions, and softer UI contexts. Arial appears in cookie/consent overlays and third-party widget contexts.*

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Transform | Notes |
|------|------|------|--------|-------------|----------------|-----------|-------|
| Display Mega | Inter Tight | 144px (9.00rem) | 800 | 0.75 | normal | uppercase | Maximum hero statements — text as architecture |
| Display XL | Inter Tight | 88px (5.50rem) | 800 | 1.00 | normal | uppercase | Primary section headings ("WORLDS") |
| Display Large | Inter Tight | 64px (4.00rem) | 800 | 1.00 | normal | uppercase | Secondary hero headers |
| Display | Inter Tight | 56px (3.50rem) | 800 | 1.00 | normal | uppercase | Section title anchors |
| Display Small | Inter Tight | 48px (3.00rem) | 800 | 1.00 | normal | uppercase | Subsection headers, link-style CTAs |
| Sub-heading Bold | Inter Tight | 20px (1.25rem) | 800 | 1.50 | 1px | none | Emphasized sub-headings with tracking |
| Sub-heading | Inter Tight | 20px (1.25rem) | 700 | 1.50 | normal | uppercase | Navigation labels, section intro |
| Sub-heading Poppins | Poppins | 20px (1.25rem) | 800 | 1.50 | normal | none | Game title cards, feature headings |
| Nav Link | Poppins | 20px (1.25rem) | 600 | 1.50 | normal | none | Primary navigation links |
| Body Large | Poppins | 18px (1.13rem) | 400 | 1.50 | normal | none | Descriptive body text, editorial copy |
| Body / Button | Inter Tight | 16px (1.00rem) | 700–800 | 1.50 | normal | uppercase | Button labels, interactive CTAs |
| Body Standard | Poppins | 16px (1.00rem) | 400–600 | 1.50 | normal | none | Standard reading text, UI labels |
| Body System | ui-sans-serif | 16px (1.00rem) | 400 | 1.50 | normal | none | Cookie consent, fallback UI |
| Carousel Header | lg / system | 24px (1.50rem) | 400 | 1.13 | normal | none | Carousel section labels |
| Caption Bold | Arial | 12px (0.75rem) | 700 | 1.87 | normal | none | Utility captions, secondary labels |
| Caption Poppins | Poppins | 12px (0.75rem) | 700 | 1.50 | -0.3px | uppercase | Badge text, category tags |
| Micro Link | Inter Tight | 12px (0.75rem) | 800 | 1.50 | normal | uppercase | Small uppercase interactive links |

### Principles
- **Weight 800 is the brand voice**: Every headline at display sizes uses Inter Tight 800. This isn't decorative boldness — it's the maximum available weight deployed at maximum size to create text that reads as graphic mass rather than typography. The brand communicates through density.
- **Uppercase is structural, not stylistic**: All Inter Tight display text uses `text-transform: uppercase`. Lowercase Inter Tight at weight 800 would feel softer; the system specifically refuses that softness. Mixed-case is reserved for Poppins body text.
- **Two-family split**: Inter Tight owns everything high-energy (headlines, CTAs, badges, section labels). Poppins handles everything that needs to breathe (navigation, body text, game descriptions). The split is clean: compressed aggression vs. open warmth.
- **Line-height 0.75 at maximum size**: The 144px heading runs at `line-height: 0.75` — characters sit below their notional baseline, creating dense stacked lines that look like stencilled signage. This is intentional visual compression.
- **Tight compression, no explicit tracking**: Unlike systems that add negative letter-spacing at display sizes, Inter Tight relies on its inherently tight proportions. Only the 20px weight-800 variant adds 1px tracking, and the badge/caption Poppins uses -0.3px for density at small uppercase sizes.

## 4. Component Stylings

### Buttons

**Ghost / Outline (Primary Dark)**
- Background: transparent (`rgba(0, 0, 0, 0)`)
- Text: `#ffffff`
- Padding: `8px 16px`
- Radius: `4px`
- Border: `2px solid rgb(255, 255, 255)`
- Shadow: none
- Font: Inter Tight 16px weight 700, uppercase
- Hover: background shifts to Electric Blue `#3379ff` (`--color-sega-primary-400`), white text maintained, outline auto
- Active: background shifts to `var(--color-fm26-primary-600)` (deep indigo `#3f1fad`)
- Focus: background `rgb(17, 17, 37)`, shadow `rgba(0,0,0,0.2) 0px 4px 8px, rgba(0,0,0,0.2) 0px 6px 20px`
- Use: Primary CTA on dark backgrounds — "ACCEPT ALL", "SEE ALL WORLDS"

**Ghost / Outline (Secondary, Wide Padding)**
- Background: transparent
- Text: `#ffffff`
- Padding: `8px 16px 8px 80px` (asymmetric — icon or logo space on left)
- Radius: `0px`
- Border: `1px solid rgb(255, 255, 255)`
- Font: Inter Tight 16px weight 400, uppercase
- Hover: background shifts to `#3379ff`, white text
- Active: background `var(--color-fm26-primary-600)`
- Use: Section-level navigation CTAs with left-side graphic treatment

**Electric Blue Pill (Play/Pause)**
- Background: Electric Blue `#0057ff`
- Text: Sega Navy `#002366`
- Padding: `0px` (icon-only circular)
- Radius: `9999px`
- Border: none
- Shadow: `rgba(0,0,0,0.2) 0px 16px 48px 0px`
- Font: 16px weight 400
- Hover: background shifts to `#3379ff`
- Opacity: 1 (disabled state: 0.5 on `#0d1126` background)
- Use: Video play/pause controls, media toggles

**Carousel Prev/Next**
- Background: `#ffffff` (default), `#0d1126` (disabled)
- Text/Icon: Electric Blue `rgb(0, 122, 255)`
- Padding: `0px`
- Radius: `0px 40px 40px 0px` (next), `40px 0px 0px 40px` (prev) — half-pill tab shape
- Shadow: `rgba(0,0,0,0.15) -2px 2px 6px 0px`
- Hover: background shifts to `#0057ff` (`--color-sega-primary-0`)
- Disabled: opacity 0.5
- Use: Swiper carousel navigation tabs

### Cards & Containers
- Background: Sega Navy `#002366` (primary containers), Near Black Navy `#0d1126` (secondary panels)
- Border: none (game art bleeds edge-to-edge) or `4px solid #ffffff` for featured card framing
- Radius: `8px` (standard cards), `12px` (larger content blocks)
- Shadow: `rgba(0,0,0,0.2) 0px 16px 48px 0px` — the signature deep lift
- Internal padding: 24–32px for text cards, 0 for full-bleed art panels
- Game cards feature icon elements in Electric Blue (`#0057ff`) as interactive overlays

### Badges / Tags / Pills
**Game Category Tag**
- Background: `#ffffff`
- Text: Electric Blue `#0057ff`
- Padding: `8px 16px`
- Radius: `48px` (heavily rounded pill)
- Border: none
- Font: Poppins 12px weight 700, uppercase, letter-spacing `-0.3px`
- Line height: `18px`
- Use: Genre labels ("RACING", "RPG", "PLATFORMER") on game cards and section headers

### Inputs & Forms
**Text Input (Number/Quantity)**
- Background: `#ffffff`
- Text: `#000000`
- Border: `1px solid rgb(166, 167, 191)`
- Radius: `0px`
- Padding: `8px 16px`
- Shadow: none
- Focus: outline none (relies on border state change)

**Email Input (Newsletter)**
- Background: `#ffffff`
- Text: Sega Navy `#002366`
- Border: `0px none`
- Radius: `0px`
- Padding: `0px 0px 0px 8px`
- Focus: outline none
- Use: Embedded in dark footer sections, no visible border — contained by a parent wrapper border

### Navigation
- Top navigation: horizontal, sticky, on Sega Navy (`#002366`) background
- Logo: Sega wordmark / favicon SVG, left-aligned or centered
- Links: Poppins 20px weight 600, white text (`#ffffff`), no underline by default
- Hover: text shifts to Electric Blue `#0057ff` or underline appears
- CTA area: Ghost button (white border) right-aligned for account/shop actions
- "SEE ALL WORLDS" label style: Inter Tight uppercase, white, with directional arrow icon (northeast arrow character)
- Mobile: collapses to hamburger with full-screen drawer

### Links
- **White with underline** (dark backgrounds): `#ffffff`, `text-decoration: underline`, weight 700; hover to Pale Blue `#e1eaff`
- **Black no underline** (light surfaces): `#000000`, no decoration; hover shows underline + Electric Blue `#0057ff`
- **Pale Blue** (dark informational): `#e1eaff`, no decoration, weight 700; hover to `#0057ff`
- **Near-white nav**: `#f4f6f9`, no decoration, weight 800; hover to `#0057ff`
- **Dark navy on light**: `#0d1126`, no decoration, weight 800; hover to `#0057ff`
- **Electric Blue** (explicit interactive): `#0057ff`, no decoration, weight 400; hover to Pale Blue `#e1eaff`

### Decorative / Structural Elements

**Section Header Rule**
- `4px solid rgb(17, 17, 37)` bottom border on section containers for structural separation
- `0px 0px 2px solid rgb(255, 255, 255)` underline treatment for specific section labels

**Full-Bleed Game Panels**
- Game art images fill panel containers edge-to-edge, `object-fit: cover`
- No frame, no border-radius on the artwork itself
- Title typography overlays positioned absolutely within the panel
- Panels sit in a carousel/grid structure with Swiper.js

## 5. Layout Principles

### Spacing System
- Base unit: 8px
- Scale: 1px, 4px, 5px, 8px, 10px, 12px, 16px, 20px, 24px, 30px, 32px, 40px, 44px, 48px, 64px, 80px
- Notable: 8px and 16px are the dominant values (106 instances each) — the system breathes in clean 8-unit multiples
- Outlier: `517.891px` — a single calculated/computed value likely from a full-viewport-height measurement
- Button padding: 8px 16px (standard), 8px 80px left (icon-offset variant)
- Section vertical rhythm: 48px–80px between major content sections

### Grid & Container
- Max width: content varies — 1200px for editorial sections, 1920px+ for full-bleed panels (breakpoints extend to 3840px for 4K)
- Game art panels: full viewport width, no container constraint
- Carousel sections: horizontally scrollable with arrow navigation
- Text+nav sections: centered column with 24–64px horizontal padding
- Footer: multi-column grid with 32px gaps

### Whitespace Philosophy
- **Darkness as space**: The Sega Navy background acts as a surrogate for whitespace — dark sections between game art panels provide visual breathing room without emptiness
- **Density over padding**: Content is packed with intentional tightness. The 144px headline at line-height 0.75 proves that the system values visual impact over comfort
- **Full-bleed as rhythm**: Game art panels fill the viewport to establish a cinematic pace, with nav labels and section headers as the only pauses between immersive moments

### Border Radius Scale
| Value | Context |
|-------|---------|
| 0px | Form inputs, sharp containers, some buttons |
| 2px | Carousel slide indicators (minimal softening) |
| 4px | Standard buttons and small interactive elements |
| 8px | Standard cards and div containers |
| 12px | Larger content panels |
| `0px 40px 40px 0px` | Carousel prev/next half-pill tab shape |
| 48px | Category tag badges (pill-ish, not full pill) |
| 50px / 50% | Circular icon buttons, avatar containers |
| 9999px | Full pill — cards, circular media buttons |

The radius system spans a wide range — from completely sharp (forms, some buttons) to full circle (play buttons, game icon badges) — reflecting the multi-game, multi-genre content where each title may have its own visual convention.

## 6. Depth & Elevation

| Level | Box Shadow Value | Use Case |
|-------|-----------------|----------|
| Level 0 (Flat) | none | Dark background sections, full-bleed game art, inline text |
| Level 1 (Directional Soft) | `rgba(0,0,0,0.15) -2px 2px 6px 0px` | Carousel navigation buttons, floating UI elements |
| Level 2 (Standard Card) | `rgba(0,0,0,0.2) 0px 16px 48px 0px` | Game cards, featured panels, play buttons |
| Level 3 (Focus State) | `rgba(0,0,0,0.2) 0px 4px 8px 0px, rgba(0,0,0,0.2) 0px 6px 20px 0px` | Focused button states, active interactive elements |

**Shadow Philosophy**: Sega's shadow system is unambiguously dark — pure black at varying opacities, with no brand-tinting or color undertones. Unlike Stripe's blue-tinted shadows or Claude's warm-black lifts, these shadows are meant to ground bright game art and electric-blue UI elements against an already-dark canvas. The `0px 16px 48px 0px` formula at 0.2 opacity creates a deep, wide-spread shadow that makes card elements appear to float significantly above the surface — cinematic rather than subtle. The directional variant (`-2px 2px 6px`) on carousel buttons creates a tactile, left-catching light source that implies three-dimensionality. On this dark a canvas, shadow isn't about indicating hierarchy — it's about punch.

### Decorative Depth
- Section depth comes primarily from alternating between `#002366` (lighter navy) and `#0d1126` (near-black navy) backgrounds
- Game art panels at full saturation read as the "highest" visual layer simply through image brightness against the dark field
- Electric Blue (`#0057ff`) interactive elements read as "lit" — glowing from within rather than elevated above

## 7. Do's and Don'ts

**Do**
- Use Inter Tight weight 800 uppercase for all section headings — the compression and weight are the brand's visual signature
- Deploy Electric Blue (`#0057ff`) as the exclusive interactive color — every button hover, every CTA, every game card accent should speak this hue
- Fill game art panels edge-to-edge with no framing or chrome — the artwork IS the design
- Use Sega Navy (`#002366`) as the primary dark canvas rather than pure black — the saturated blue darkness is brand-specific
- Apply the pill badge pattern (48px radius, white background, blue text) for genre/category tags on game cards
- Maintain uppercase text transform on all Inter Tight display text regardless of size — it's structural, not decorative
- Use `#3379ff` (`--color-sega-primary-400`) for hover states on Electric Blue elements — the two-stop blue ramp is the interaction language
- Allow game-specific accent colors (Persona's red, Sonic's magenta) scoped to their respective game panels as local overrides

**Don't**
- Don't use Inter Tight weight 800 in lowercase at display sizes — the uppercase transform is non-negotiable for headlines
- Don't introduce warm accent colors (orange, red, yellow) as global UI colors — they belong only within specific game-section scopes
- Don't use pure black (`#000000`) as the page background — Sega Navy (`#002366`) is the brand darkness
- Don't apply rounded corners (8px+) to game art image containers — artwork bleeds to the panel edge without softening
- Don't add secondary border colors or decorative frames around game art panels — the full-bleed treatment is the point
- Don't use Poppins at weight 400 for interactive elements (buttons, CTAs) — reserve Poppins lightness for body text; CTAs need Inter Tight's aggression
- Don't use the Pale Blue (`#e1eaff`) for primary CTAs — it's a hover-feedback and soft-tint color only, too low-contrast for buttons
- Don't apply the badge pill style (48px radius) to primary action buttons — pills are for read-only category labels, not user actions

## 8. Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile XS | 400px | Minimum layout — stacked single column, hero text drops to 48–56px |
| Mobile | 480px | Single column, reduced nav, game cards stack vertically |
| Mobile Large | 600px | Wider single column, carousel becomes 1-up |
| Tablet S | 640px | 2-column card grids begin, nav links visible |
| Tablet | 768px | Multi-column feature sections, hero at 64–88px |
| Tablet Large | 960px | 3-column game grids, full nav bar |
| Desktop S | 1020px | Full navigation, carousel 3-up visible |
| Desktop | 1200px | Standard desktop layout, hero at 88–144px |
| Desktop L | 1280px | Max standard content width |
| Large | 1600px | Generous margins, 4+ carousel panels |
| XL | 1920px | Full cinematic layout |
| 4K | 2560–3840px | Scaled for ultra-wide — massive game art, 144px+ hero type |

### Touch Targets
- Primary buttons: 8px 16px padding minimum, ensuring 44px+ tap height when combined with font size
- Carousel arrows: 44px+ touch area (half-pill shape extends to edge for thumb reach)
- Badge tags: 8px 16px padding with 48px radius — comfortable for touch
- Navigation links: Poppins 20px with 1.50 line-height provides natural finger-sized targets
- Play/pause circular button: 50% radius, 44×44px minimum

### Collapsing Strategy
- **Navigation**: Full horizontal nav with links collapses to hamburger icon on mobile; drawer expands full-screen with white links on navy background
- **Display type**: 144px → 88px → 64px → 48px progression across breakpoints; weight 800 and uppercase maintained throughout all sizes
- **Game panels**: Full-bleed carousel transitions from 3-up desktop view to 1-up mobile, with same arrow navigation preserved
- **Category tags**: Pill badges maintain 48px radius and white-on-blue treatment at all sizes; padding may reduce to 6px 12px on mobile
- **Section spacing**: 80px section gaps → 48px → 32px on mobile; rhythm is preserved though compressed
- **Grid to stack**: Multi-column game card grids collapse to 2-column tablet → 1-column mobile with maintained card shadow treatment

### Image Behavior
- Game art: full-bleed at all breakpoints using `object-fit: cover` — art direction favors the subject (character or logo) over environment
- Character art panels (Yakuza, Persona): cropped to maintain face/upper body in mobile viewport
- Logo art panels (Alien Isolation title treatment): centered crop ensures wordmark remains readable
- No art direction swaps specified — single image scales to fit at all breakpoints

## 9. Agent Prompt Guide

### Quick Reference
- Primary CTA color: Electric Blue (`#0057ff`)
- CTA Hover: Brand Blue Mid (`#3379ff`)
- Page Background: Sega Navy (`#002366`)
- Secondary Dark Surface: Near Black Navy (`#0d1126`)
- Primary Text (dark bg): Pure White (`#ffffff`)
- Primary Text (light bg): Pure Black (`#000000`)
- Badge Background: Pure White (`#ffffff`)
- Badge Text: Electric Blue (`#0057ff`)
- Pale Blue (hover/soft): `#e1eaff`
- Card Shadow: `rgba(0,0,0,0.2) 0px 16px 48px 0px`
- Display Font: Inter Tight, weight 800, uppercase
- Body Font: Poppins, weight 400–600

### Example Component Prompts
- "Create a hero section on Sega Navy (`#002366`) background. Heading: 'WORLDS' in Inter Tight 88px weight 800, line-height 1.00, uppercase, color `#ffffff`. 'SEE ALL WORLDS' link label at Inter Tight 20px weight 700 uppercase in white with a right-arrow icon. Ghost CTA button: transparent background, `2px solid #ffffff`, `4px` border-radius, `8px 16px` padding, Inter Tight 16px weight 700 uppercase white text. Hover state shifts button background to `#3379ff`."
- "Design a game card grid on Near Black Navy (`#0d1126`). Each card: full-bleed game art image, `8px` border-radius on container, `rgba(0,0,0,0.2) 0px 16px 48px 0px` shadow. Category badge overlay: `#ffffff` background, Electric Blue (`#0057ff`) text, Poppins 12px weight 700 uppercase letter-spacing -0.3px, `8px 16px` padding, `48px` border-radius."
- "Build a section header on Sega Navy. Large display text 'GAMES' at Inter Tight 144px weight 800 line-height 0.75 uppercase `#ffffff`. Below it, a horizontal rule of `4px solid #111125`. Body text below in Poppins 18px weight 400 line-height 1.50 `#e1eaff`."
- "Create a carousel navigation button: white (`#ffffff`) background, chevron icon in Electric Blue (`rgb(0, 122, 255)`), border-radius `0px 40px 40px 0px` (right-side arrow), shadow `rgba(0,0,0,0.15) -2px 2px 6px 0px`. Hover shifts background to `#0057ff` with white icon."
- "Design a newsletter signup bar on Near Black Navy (`#0d1126`). Label in Inter Tight 20px weight 800 uppercase white. Email input: white background, `#002366` text, `0px` border, `0px` radius, `8px` left padding, no shadow. Submit button: transparent background, `2px solid #ffffff`, `4px` radius, `8px 16px` padding, white Inter Tight 16px weight 700 uppercase. Hover shifts to Electric Blue `#3379ff`."

### Iteration Guide
1. Inter Tight weight 800 uppercase is non-negotiable for all section headings — scale the size, never the weight or transform
2. Electric Blue (`#0057ff`) is the only interactive color — all hovers, all CTAs, all badge text should reference this value
3. The hover ramp is always: rest state → `#3379ff` (lighter blue) → active state (deep indigo `#3f1fad`) — three stops, one hue family
4. Dark backgrounds oscillate between `#002366` (brand navy) and `#0d1126` (near-black) — never pure black, never generic dark gray
5. Game art panels always bleed edge-to-edge with no framing; apply shadow only to card containers, never to the artwork itself
6. Pill badges (48px radius) are read-only labels — action buttons use 4px or 9999px radius, never 48px
7. Poppins is the softening agent — use it when content needs to breathe (body text, descriptions) while Inter Tight handles every moment of high energy
8. The `rgba(0,0,0,0.2) 0px 16px 48px 0px` shadow is the system's single elevation expression — apply it consistently to all raised cards and panels
9. Game-specific accent colors (Persona red, Sonic magenta) are always locally scoped — never bleed into global UI chrome
10. White borders (1px–4px solid `#ffffff`) are structural tools in this system — used as dividers, button outlines, and section separators against the dark field