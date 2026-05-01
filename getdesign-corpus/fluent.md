---
slug: fluent
name: Microsoft Fluent 2
url: https://fluent2.microsoft.design
domain: fluent2.microsoft.design
category: Design System
styles: [Gradient, Light, Minimal]
tagline: "Acrylic blur and Communication Blue on a cool-gray token grid, depth as structure."
fonts: [Segoe UI Variable, Fluent 2 ships]
primary_color: "#0078D4"
---

# Design System Inspired by Microsoft Fluent 2

> Acrylic blur and Communication Blue on a cool-gray token grid, depth as structure.

## 1. Visual Theme & Atmosphere

Fluent 2 is Microsoft's design language for Windows 11, Microsoft 365, Teams, and Copilot — a system built around the idea that software surfaces should have **material depth**, not just visual hierarchy. Where iOS glassmorphism leans hedonistic and atmospheric, Fluent 2 leans architectural: translucency is used to signal structure, layering, and intent. The signature of the system is the pairing of two specific materials — **Acrylic** (a blurred, translucent surface with luminosity and noise) and **Mica** (a subtle, opaque wallpaper-tinted background that shifts with the user's desktop). Together they replace flat "dark mode vs light mode" with a spatial model of stacked, semi-permeable planes.

The typography is built on **Segoe UI** — Microsoft's decades-old humanist sans — with Segoe UI Variable now shipping on Windows 11 for optical size adjustments at display, text, and small sizes. Display headings run 400–600 weight with tight negative tracking (`-1.6px` at 52px); body copy sits at a comfortable 16/1.38; captions drop to 10–12px with 600 weight when they need presence in chrome. Compared with Linear's aggressive 72px headlines, Fluent 2's hero scale tops out around 52px — this is a workhorse system designed to live inside productivity apps, not marketing pages.

The neutral palette is the restrained part: near-pure black (`#000000`), a signature 61-gray (`#616161`), pure white, and a cool `#F5F5F5` canvas tint. The brand anchor is **Communication Blue `#0078D4`** — Microsoft's interactive link blue, used for buttons, focus states, and emphasized UI. Beyond that, Fluent 2 ships the richest semantic palette of any modern design system: 28+ numbered neutral backgrounds, 12 foreground variants, and a full personality palette (Red, Orange, Marigold, Green, Teal, Lavender, Plum, Berry, Grape, Navy, Seafoam) with 1–3 intensity steps each. The job of Fluent 2 is to ship a credible, accessible, theme-aware UI across every surface Microsoft makes — the restraint in chrome leaves room for content to breathe.

**Key Characteristics:**
- Acrylic material: `backdrop-filter: blur(20–60px) saturate(180%)` over a translucent surface (`rgba(255,255,255,0.6)` light, `rgba(32,32,32,0.6)` dark) with luminosity tint
- Mica material: opaque, subtly wallpaper-tinted canvas — cool `#F3F3F3` light / `#202020` dark, with imperceptible warm/cool shift based on desktop wallpaper
- Segoe UI / Segoe UI Variable — humanist sans, optical sizes, Microsoft's native typeface since Vista
- 4px baseline precision throughout — radius scale is `2px · 4px · 6px · 8px`, with 12px reserved for cards and 24px+ for pill buttons
- Communication Blue `#0078D4` as the single brand anchor across every product surface
- Token-driven color system: `--colorNeutralBackground1` through `--colorNeutralBackground27`, `--colorBrandBackground`, etc.
- Shadow layers are precise, not atmospheric: `rgba(0,0,0,0.12) 0px 0px 2px, rgba(0,0,0,0.14) 0px 2px 4px` (Level 4)
- Cool neutral tint (slight blue-gray undertone) rather than warm — this is "office software", not "editorial"

## 2. Color Palette & Roles

### Neutral Backgrounds (Light Theme)
- **Canvas** (`#F5F5F5`): Page background — the Mica-adjacent neutral base.
- **Surface** (`#FAFAFA`): Card surfaces one level above canvas.
- **Surface Alt** (`#FFFFFF`): Elevated panels, dialog bodies, input fields.
- **Subtle** (`#F0F0F0`): Hover states on surfaces, inset zones.

### Neutral Backgrounds (Dark / Mica Theme)
- **Mica Dark** (`#202020`): Dark canvas — wallpaper-tinted base.
- **Surface Dark** (`#292929`): Elevated surface on dark.
- **Surface Alt Dark** (`#2F2F2F`): Highest elevation on dark.
- **Subtle Dark** (`#1A1A1A`): Recessed / inset areas on dark.

### Text & Foreground
- **Foreground 1** (`#242424`): Primary text — near-black with a cool cast, not pure `#000`.
- **Foreground 2** (`#424242`): Secondary text, labels.
- **Foreground 3** (`#616161`): **Fluent's signature gray** — muted labels, placeholders, metadata.
- **Foreground 4** (`#707070`): Disabled text, tertiary info.
- **Foreground Inverse** (`#FFFFFF`): Text on brand / dark surfaces.

### Brand Anchor
- **Communication Blue** (`#0078D4`): The primary brand color — used for buttons, links, focus rings, selected states. Microsoft's "default CTA blue" across every product.
- **Brand Hover** (`#115EA3`): Darker shade for hover.
- **Brand Pressed** (`#0F548C`): Pressed / active state.
- **Brand Stroke** (`#0F6CBD`): Compound brand stroke for borders around branded chrome.
- **Brand Link** (`#0F6CBD` → pressed `#0C3B5E`): Hyperlink blue.

### Personality Palette (sampled)
- **Red** (`#D13438`): Destructive actions, error badges.
- **Dark Red** (`#C50F1F`): Pressed red.
- **Orange** (`#F7630C`): Status warning background 3.
- **Marigold** (`#EAA300`): Warning accent.
- **Yellow** (`#FDE300`): Yellow border 2.
- **Green** (`#107C10`): Success foreground 3.
- **Light Green** (`#13A10E`): Success state, affirmative signal.
- **Teal** (`#02767A`): Link variant, documentation accent.
- **Lavender** (`#7160E8`): Lavender border active.
- **Grape** (`#881798`): Grape border active, rich personality.
- **Magenta** (`#6B0043`): Deep magenta foreground 2.
- **Berry** (`#C239B3`): Berry border 2.

### Status Semantic
- **Success** (`#107C10`): Confirmed, online, completed.
- **Warning** (`#F7630C`): Caution, attention needed.
- **Error** (`#D13438`): Destructive, failed, invalid.
- **Info** (`#0078D4`): Brand blue reused as informational accent.

### Borders & Strokes
- **Stroke 1** (`#D1D1D1`): Standard light border — the default visible edge.
- **Stroke 2** (`#E0E0E0`): Subtle border.
- **Stroke 3** (`#F0F0F0`): Nearly invisible hairline.
- **Stroke Dark 1** (`#757575`): Standard dark-theme border.
- **Focus Stroke** (`#0078D4`, 2px): Keyboard focus ring — always Communication Blue.

## 3. Typography Rules

### Font Family
- **Primary**: `Segoe UI Variable`, falling back to `Segoe UI Web (West European), Segoe UI, -apple-system, system-ui, Roboto, Helvetica Neue`
- **Fluent 2 ships with Segoe UI Variable** (Windows 11+): optical sizes at Display, Text, and Small points for rendering consistency from 8pt captions to 68pt titles
- **No OpenType display features** — Segoe UI is already optically tuned; no cv01/ss03-style stylistic alternates are required

### Hierarchy

| Role | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|--------|-------------|----------------|-------|
| Title XL | 52px (3.25rem) | 600 | 1.00 | -1.6px | Hero heading (`Welcome to Fluent 2`) |
| Title | 40px (2.50rem) | 600 | 1.30 | -1.6px | Section titles |
| Subtitle | 28px (1.75rem) | 400 | 1.15 | normal | Sub-hero / page section |
| Heading | 24px (1.50rem) | 600 | 1.33 | normal | Feature headings |
| Large | 20px (1.25rem) | 400–600 | 1.00–1.30 | normal | Button XL, prominent labels |
| Body Large | 18px (1.13rem) | 400 | 1.15 | normal | Intro / lead paragraph |
| Body Strong | 16px (1.00rem) | 600 | 1.38 | normal | Emphasized body, link |
| Body | 16px (1.00rem) | 400 | 1.38 | normal | Default reading |
| Caption | 14px (0.88rem) | 400 | 1.36 | normal | Secondary text, captions |
| Caption Strong | 14px (0.88rem) | 600 | 1.15 | normal | Button text, strong labels |
| Caption 2 | 12px (0.75rem) | 400 | 1.33 | normal | Metadata, footer |
| Micro | 10px (0.63rem) | 600 | 1.40 | normal | Chip labels, tiny UI |
| Overline | 16px (1.00rem) | 700 | 1.38 | 2.56px | Uppercase eyebrow / section label |

### Principles
- **Segoe UI Variable does the optical work**: use Display OpSz for 24px+, Text OpSz for 12–23px, Small OpSz for ≤11px when the variable font is available — otherwise fall back to static Segoe UI
- **Tight tracking at display, relaxed at body**: `-1.6px` at 52px, `-0.24–0.48px` at 28–40px, normal below 24px
- **Three weights do most of the work**: 400 (read), 600 (emphasize), 700 (overline only). No 500, no 800+
- **Uppercase lives only in overlines**: 16px/700 with `2.56px` tracking is the signature eyebrow treatment — everywhere else, sentence case
- **Line-height tightens as size grows**: 1.40 at 10px → 1.36 at 14px → 1.38 at 16px → 1.33 at 24px → 1.15 at 28px → 1.00 at 52px

## 4. Component Stylings

### Buttons

**Primary Button**
- Background: `#0078D4` (Communication Blue)
- Text: `#FFFFFF`
- Padding: 6px 12px (medium) / 8px 16px (large)
- Radius: 4px
- Border: none
- Hover: `#115EA3`
- Pressed: `#0F548C`
- Focus ring: 2px `#0078D4`, 2px offset

**Secondary Button**
- Background: `#FFFFFF`
- Text: `#242424`
- Border: 1px solid `#D1D1D1`
- Radius: 4px
- Hover: background `#F5F5F5`, border `#C7C7C7`

**Subtle Button** (default in toolbars)
- Background: transparent
- Text: `#242424`
- Border: none
- Hover: background `#F5F5F5`
- Used for: icon buttons, menu items, command bars

**Pill Button** (Fluent's 24px-radius variant for prominent CTAs)
- Background: `#0078D4`
- Text: `#FFFFFF`
- Padding: 8px 20px
- Radius: 24px
- Font: 16px weight 600

### Cards (Acrylic + Standard)

**Standard Card**
- Background: `#FFFFFF`
- Border: 1px solid `#E0E0E0`
- Radius: 8px (standard) / 12px (featured)
- Padding: 16–24px
- Shadow (resting): `rgba(0,0,0,0.12) 0px 0px 2px, rgba(0,0,0,0.14) 0px 2px 4px`
- Shadow (hover): `rgba(0,0,0,0.12) 0px 0px 2px, rgba(0,0,0,0.14) 0px 8px 16px`

**Acrylic Card** (the signature treatment)
- Background: `rgba(255,255,255,0.60)` (or `rgba(32,32,32,0.60)` dark)
- Backdrop filter: `blur(20px) saturate(180%)` — the Acrylic effect
- Border: 1px solid `rgba(255,255,255,0.30)` (light) / `rgba(255,255,255,0.08)` (dark)
- Radius: 8px
- Shadow: `rgba(0,0,0,0.14) 0px 8px 16px`
- **Must sit over colored or image-filled backdrop** — otherwise the effect is invisible

### Inputs

**Text Input**
- Background: `#FFFFFF`
- Text: `#242424`
- Border: 1px solid `#D1D1D1` (resting) / bottom border 2px `#0078D4` (focus)
- Padding: 6px 10px
- Radius: 4px
- Focus: no outline — instead, the bottom border thickens to 2px Communication Blue (the signature Fluent focus treatment)

### Badges & Chips

**Neutral Badge**: background `#F5F5F5`, text `#424242`, padding 2px 8px, radius 4px, 12px weight 600

**Brand Badge**: background `#0078D4`, text `#FFFFFF`, padding 2px 8px, radius 4px

**Success Badge**: background `#DFF6DD`, text `#107C10`, padding 2px 8px, radius 4px

**Pill Chip**: any badge with radius 9999px — used for tags and filters

### Navigation
- Left sidebar (Fluent 2 docs pattern): `#FAFAFA` background, 1px `#E0E0E0` right border, 240px width
- Active item: background `rgba(0,120,212,0.08)`, left border 2px `#0078D4`, text `#242424` weight 600
- Hover item: background `#F0F0F0`
- Nav link font: 13–14px weight 400

## 5. Layout Principles

### Spacing Scale
Base unit: **4px**. Scale: `4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80`. The 4px baseline is non-negotiable — every padding, margin, and gap snaps to it. This is what makes Fluent 2 feel engineered rather than crafted: there is no "roughly 15px" — there is 12 or 16.

### Grid & Container
- Max content width: 1200px (docs), 1440px (full app shells)
- Docs layout: 240px left rail + 1fr content + 240px right TOC
- Card grids: 2, 3, or 4 columns with 16–24px gutters
- Responsive collapse: rails become drawers at <1024px

### Whitespace Philosophy
- **Density serves productivity**: Fluent 2 is noticeably denser than Stripe or Linear — this is a system for apps where users spend hours, not marketing pages they scan
- **4px precision over generous padding**: where other systems use 24/32/48, Fluent 2 uses 12/16/20. The eye reads the rhythm as "tight" rather than "breathable"
- **Material stacking creates space, not margin**: depth via Acrylic/Mica means you don't need white gaps to separate sections — the translucent layers do that job

### Border Radius Scale
- **2px** (22 uses): Inline UI elements, toggle tracks, small tags
- **4px** (default, most common): Buttons, inputs, badges, standard cards — the Fluent 2 default
- **6px** (78 uses): Secondary buttons, dropdowns
- **8px** (78 uses): Cards, panels, menus
- **12px** (rare): Featured cards, images with rounded corners
- **20–22px** (featured cards only): Hero cards, callouts
- **24px** (pill buttons): Large CTA pills
- **9999px** (chips): Filter pills, status chips

## 6. Depth & Elevation — THE SIGNATURE

Fluent 2's depth model is the single most important thing to get right. It has **two materials and six elevation levels**, and they're not interchangeable — each answers a different question about "what kind of surface is this?"

### Materials

**Acrylic** — Translucent + Blurred + Luminous
- The "glassmorphism" surface, but with precise physics
- Formula: `background: rgba(255,255,255,0.60); backdrop-filter: blur(20px) saturate(180%);` (light theme)
- Dark variant: `background: rgba(32,32,32,0.60); backdrop-filter: blur(20px) saturate(180%);`
- Adds **Luminosity layer** on top: 40% noise texture OR `rgba(255,255,255,0.08)` overlay for that "glass with grain" look
- Adds **Tint layer**: a subtle chromatic wash (brand blue at 3%, or theme-colored)
- **Used for**: flyouts, menus, command bars, tooltips, dialogs, taskbar — any transient surface that benefits from showing what's beneath it
- **Must appear over content** to work — Acrylic over a solid page is just a fuzzy square

**Mica** — Opaque + Wallpaper-Tinted + Subtle
- The "warm grey that isn't quite grey" base layer used for window chrome in Windows 11
- Formula (approximated for web): `background: #F3F3F3; background-image: linear-gradient(rgba(desktop-tint, 0.03), rgba(desktop-tint, 0.03));`
- Dark variant: `background: #202020;` with an imperceptible warm/cool shift
- **Not blurred, not translucent** — this is a solid surface that SAMPLES the user's wallpaper to introduce a whisper of color
- **Used for**: Window backgrounds, app shells, the foundational canvas
- **Stable layer** — Mica is where content lives, Acrylic is where UI floats

### Elevation Layers

| Level | Treatment | Use |
|-------|-----------|-----|
| Base (0) | Flat Mica surface, no shadow | Window background, page canvas |
| Shadow 2 | `rgba(0,0,0,0.12) 0px 0px 2px` | Subtle card hairline, resting state |
| Shadow 4 | `rgba(0,0,0,0.12) 0px 0px 2px, rgba(0,0,0,0.14) 0px 2px 4px` | Standard cards, resting surface |
| Shadow 8 | `rgba(0,0,0,0.14) 0px 4px 8px, rgba(0,0,0,0.12) 0px 0px 2px` | Hover state, raised panels |
| Shadow 16 | `rgba(0,0,0,0.14) 0px 8px 16px, rgba(0,0,0,0.12) 0px 0px 2px` | Flyouts, popovers, tooltips |
| Shadow 28 | `rgba(0,0,0,0.14) 0px 14px 28px, rgba(0,0,0,0.12) 0px 0px 8px` | Dialogs, modals |
| Shadow 64 | `rgba(0,0,0,0.14) 0px 32px 64px, rgba(0,0,0,0.12) 0px 0px 8px` | Full-window dialogs, context menus |

### The 4px Depth Step
Fluent 2's precision comes from locking shadow offsets to the 4px grid: `0, 2, 4, 8, 16, 28, 64`. The blur radius always equals or exceeds 2× the offset. This is what makes Fluent's shadows feel "surgical" rather than "atmospheric" — they're shallow, directional, and consistent across every surface.

**Acrylic + Mica working together**: The app window uses Mica. Inside the window, sidebar rails sit at Shadow 2. Cards on the canvas sit at Shadow 4. Hover a card → Shadow 8. Open a dropdown → it uses **Acrylic** (not just Shadow 16) because it needs to FLOAT, not just lift. The material signals "this is a transient UI chrome layer," the shadow signals "this is how high it is."

## 7. Do's and Don'ts

### Do
- Use `#0078D4` (Communication Blue) as the anchor — not a competing brand color
- Snap every size, padding, margin, and radius to the 4px grid
- Use 4px radius as the default — only go to 8px for cards, 24px for pill CTAs
- Use Segoe UI Variable when on Windows, Segoe UI as fallback, then -apple-system
- Apply Acrylic to transient UI chrome (menus, flyouts, tooltips) — not to static page surfaces
- Use Mica as the foundational window background, not for content panels
- Use `#616161` for muted text and placeholders — Fluent's signature gray
- Focus state = bottom border thickens to 2px Communication Blue (don't use a ring outline)
- Use numbered semantic tokens when possible (`--colorNeutralBackground1`, `--colorBrandBackground`) — they're what Figma components expect
- Keep the shadow stack precise: `0px 0px 2px + 0px 2px 4px` for Shadow 4, etc. Never a single fat shadow

### Don't
- Don't use pure black `#000000` for text — `#242424` (Foreground 1) prevents eye strain
- Don't apply Acrylic to full-page backgrounds — it only reads as Acrylic over colored content
- Don't use Mica for cards or buttons — it's a canvas material, not a component material
- Don't use rounded-full (9999px) buttons as the default — Fluent's default is 4px
- Don't use warm neutrals (beige, cream) — Fluent's palette is cool-leaning
- Don't use 500 or 800 weights — 400/600/700 is the entire weight system
- Don't use custom focus rings — the 2px bottom-border-in-Communication-Blue is the Fluent focus treatment
- Don't scale display text below 1.0 line-height — at 52px/600/-1.6px/1.00 it's already at its compression limit
- Don't use soft atmospheric drop shadows (large blur, no offset) — Fluent shadows are directional and shallow
- Don't theme Acrylic with heavy color tints — 3–8% is the ceiling, beyond that it stops reading as glass

## 8. Responsive Behavior

### Breakpoints
| Name | Width | Changes |
|------|-------|---------|
| Small | <480px | Single column, compact chrome, rails become drawers |
| Medium | 480–768px | 2-col grids, visible but collapsible rail |
| Large | 768–1280px | Standard app shell — rail + content + optional TOC |
| XL | >1280px | Full app shell with right TOC, generous margins |

### Touch Targets
- Minimum 32px tall for buttons (medium), 40px for large
- Icon buttons: 32×32px default, 28px compact
- Pill CTAs: 40–48px tall for marketing / onboarding
- Input fields: 32px height default

### Collapsing Strategy
- Display headings scale: 52px → 40px → 28px
- Left rail (240px) collapses to 48px icon rail at Medium, to drawer at Small
- Card grids: 4 → 3 → 2 → 1
- Padding: 24px → 16px → 12px at Small
- Acrylic menus become full-screen sheets on Small

### Material Behavior
- Acrylic degrades gracefully: on browsers without `backdrop-filter`, fall back to solid `rgba(255,255,255,0.92)` with higher opacity — material integrity matters more than visual fidelity
- Mica wallpaper sampling is Windows-native; on web, use a static cool-neutral `#F3F3F3` as approximation
- Reduced motion: disable Acrylic reveal animations but keep the blur

## 9. Agent Prompt Guide

### Quick Color Reference
- Primary: Communication Blue `#0078D4`
- Primary Hover: `#115EA3`
- Primary Pressed: `#0F548C`
- Page background (Mica-adjacent): `#F5F5F5`
- Surface: `#FFFFFF`
- Surface subtle: `#F0F0F0`
- Primary text (Foreground 1): `#242424`
- Secondary text (Foreground 2): `#424242`
- Muted text (Foreground 3): `#616161` (signature)
- Border default: `#D1D1D1`
- Border subtle: `#E0E0E0`
- Success: `#107C10`
- Warning: `#F7630C`
- Error: `#D13438`
- Focus: `#0078D4` (2px bottom border)

### Example Component Prompts
- "Create a hero on `#F5F5F5` background. Headline 52px Segoe UI Variable weight 600, line-height 1.00, letter-spacing -1.6px, color `#242424`. Subtitle 18px weight 400, color `#616161`. Primary button: `#0078D4` bg, white text, 4px radius, 6px 12px padding."
- "Design a standard card: `#FFFFFF` background, 1px solid `#E0E0E0` border, 8px radius, 16px padding, shadow `rgba(0,0,0,0.12) 0px 0px 2px, rgba(0,0,0,0.14) 0px 2px 4px`. Title 16px Segoe UI weight 600, body 14px weight 400 color `#616161`."
- "Design an Acrylic menu flyout: background `rgba(255,255,255,0.60)`, backdrop-filter `blur(20px) saturate(180%)`, 1px solid `rgba(255,255,255,0.30)` border, 8px radius, shadow `rgba(0,0,0,0.14) 0px 8px 16px`. Must sit over colored or image backdrop to read as Acrylic."
- "Build an input field: `#FFFFFF` bg, 1px solid `#D1D1D1`, 4px radius, 6px 10px padding. On focus: bottom border thickens to 2px `#0078D4` — no outline ring. Text color `#242424`, placeholder `#616161`."
- "Create a pill CTA: `#0078D4` background, white text 16px weight 600, 24px radius, 8px 20px padding. Hover `#115EA3`. For onboarding and marketing surfaces only — not for in-app chrome."

### Iteration Guide
1. Start with Segoe UI Variable if available, Segoe UI as fallback — never Arial or system-ui alone
2. Communication Blue `#0078D4` is the only brand color you need; every other hue is semantic (status) or personality palette (charts, tags)
3. Snap to 4px — if your spacing or radius ends in an odd number, fix it
4. Default radius is 4px, not 6 or 8; 8 is for cards only; 24 is for pill CTAs only
5. Shadow stacks are additive: `0px 0px 2px + 0px 2px 4px` for Shadow 4 — never a single fat shadow
6. Acrylic only over content backdrops; Mica only as canvas; Shadow for standard elevation
7. Focus = 2px bottom border in `#0078D4`, never a full outline ring
8. Muted text is `#616161` — the signature Fluent gray that nearly every site gets wrong
