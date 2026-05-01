---
slug: carbon
name: Carbon Design System
url: https://carbondesignsystem.com
domain: carbondesignsystem.com
category: Design System
styles: [Light, Minimal, Bold]
tagline: "Sharp-cornered geometry, IBM Plex Sans at weight 300, IBM Blue as the only accent allowed."
fonts: [IBM Plex Sans, IBM Plex Mono, IBM Plex Serif]
primary_color: "#0f62fe"
---

# Design System Inspired by Carbon Design System

> Sharp-cornered geometry, IBM Plex Sans at weight 300, IBM Blue as the only accent allowed.

## 1. Visual Theme & Atmosphere

Carbon is IBM's enterprise design system — the chrome that ships mainframe administration consoles, Watson dashboards, cloud platform UIs, and 40+ other products to half a million IBM employees. The homepage opens in a restrained palette: white canvas (`#ffffff`), IBM Blue (`#0f62fe`) as the singular interactive color, and IBM Plex Sans as the typeface. This is enterprise design with capital E — precise, structural, intentional in its refusal to be consumer-friendly.

Typography is **IBM Plex Sans** — IBM's custom variable-font family — used at weight 300 (light) for display, weight 400 for UI, weight 600 for emphasis. The weight 300 at display is a deliberate signature: where most enterprise systems lean on 600-700 for authority, Carbon chose lightness. Body text uses weight 400 with `+0.16px` tracking — a barely perceptible positive letter-spacing that opens the text for readability. IBM Plex Mono handles code and data.

The defining structural choice is **0px border-radius**. Carbon has no rounded corners. The scan found 1 instance of `2px` radius and 1 instance of `50%` (for a "Back to Top" button) — that's it. Every button, every card, every input is **sharp-cornered**. This is deliberate aesthetic philosophy: Carbon communicates precision, engineering density, and enterprise heritage through angular geometry. Rounded corners signal consumer software; Carbon intentionally rejects that vocabulary.

**Key Characteristics:**
- Sharp corners everywhere — `0px` radius on all interactive elements
- IBM Plex Sans (variable font) at weight 300 display, weight 400 body
- IBM Blue (`#0f62fe`) as the singular interactive color — 45 occurrences
- Positive letter-spacing (`+0.16px`) on body — readability-first
- IBM Plex Mono for code and data tables
- Bottom-only input borders — material-inspired but simpler
- 20-year enterprise heritage — Carbon has powered IBM products since 2014
- Used across 40+ IBM products in 40+ languages — design for global scale

## 2. Color Palette & Roles

### Interactive Scale
- **Interactive 01** (`#0f62fe`): IBM Blue — primary interactive. Tier-1 CTAs.
- **Interactive 02** (`#161616`): Near-black — secondary CTAs.
- **Interactive 03** (`#0f62fe`): Tertiary interactive.
- **Hover Primary** (`#0353e9`): Blue hover state.
- **Active Primary** (`#002d9c`): Pressed state.

### Layer Scale (Carbon's unique elevation system)
- **Background** (`#ffffff`): Base canvas layer.
- **Layer 01** (`#f4f4f4`): First elevation layer — cards sit here.
- **Layer 02** (`#ffffff`): Alternating layer for nested cards.
- **Layer 03** (`#f4f4f4`): Deepest nested layer.
- Carbon explicitly names elevation as "layers" rather than shadows — they alternate background tints for depth, not drop shadows.

### Text
- **Text Primary** (`#161616`): Primary text. 14 occurrences in the scan.
- **Text Secondary** (`#525252`): Secondary text — 192 occurrences (the dominant text color).
- **Text Placeholder** (`#a8a8a8`): Placeholder.
- **Text On Color** (`#ffffff`): Text on filled surfaces.
- **Text Disabled** (`#c6c6c6`): Disabled text — 56 occurrences.

### Border
- **Border Strong** (`#8d8d8d`): Emphasized border.
- **Border Subtle** (`#c6c6c6`): Default border (56 uses).
- **Border Interactive** (`#0f62fe`): Focus/interactive border.

### Semantic
- **Success** (`#24a148`): Success state.
- **Warning** (`#f1c21b`): Amber caution.
- **Error** (`#da1e28`): Critical/destructive.
- **Info** (`#4589ff`): Info callouts.

## 3. Typography Rules

### Font Family
- **Primary**: `IBM Plex Sans` (variable font — `IBM Plex Sans Var`), fallback: `-apple-system, system-ui, sans-serif`
- **Monospace**: `IBM Plex Mono`, fallback: `ui-monospace, monospace`
- **Serif** (editorial): `IBM Plex Serif` — used rarely, for marketing long-form content
- Variable font weight axis: 100-700 available

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display 04 | IBM Plex Sans | 92px | 300 | 1.05 | -1.8px |
| Display 03 | IBM Plex Sans | 72px | 300 | 1.10 | -1.44px |
| Display 02 | IBM Plex Sans | 54px | 300 | 1.15 | 0 |
| Display 01 | IBM Plex Sans | 42px | 300 | 1.20 | 0 |
| Productive Heading 07 | IBM Plex Sans | 54px | 300 | 1.20 | 0 |
| Productive Heading 04 | IBM Plex Sans | 32px | 300 | 1.25 | 0 |
| Productive Heading 03 | IBM Plex Sans | 20px | 400 | 1.40 | 0 |
| Productive Heading 02 | IBM Plex Sans | 16px | 600 | 1.40 | 0 |
| Body Long | IBM Plex Sans | 16px | 400 | 1.50 | 0 |
| Body Short | IBM Plex Sans | 14px | 400 | 1.43 | +0.16px |
| Label | IBM Plex Sans | 12px | 400 | 1.33 | +0.32px |
| Caption | IBM Plex Sans | 12px | 400 | 1.33 | +0.32px |
| Code 02 | IBM Plex Mono | 14px | 400 | 1.43 | +0.16px |
| Code 01 | IBM Plex Mono | 12px | 400 | 1.33 | +0.32px |

### Principles
- **Weight 300 at display**: The Carbon signature. Enterprise lightness — confident without bold.
- **Positive letter-spacing at small sizes**: `+0.16px` at 14px, `+0.32px` at 12px — opens characters for readability on dense UI.
- **Productive vs Expressive type**: Carbon names styles `Productive Heading 04` (for app UI) vs `Display 03` (for marketing) — the same size, different weight, different tracking, different context.
- **Code is identity-forward**: IBM Plex Mono appears throughout technical documentation and data displays.

## 4. Component Stylings

### Buttons
- **Primary**: `#0f62fe` bg, white text, `0px` radius, `0 16px` padding, `48px` height, 14px IBM Plex Sans weight 400 tracking `+0.16px`.
- **Secondary**: `#393939` bg, white text, `0px` radius.
- **Tertiary**: transparent bg, `1px solid #0f62fe`, `#0f62fe` text, `0px` radius.
- **Ghost**: transparent, `#0f62fe` text, no border.
- **Danger**: `#da1e28` bg, white text.
- Sizes: `sm` (32px), `md` (40px), `lg` (48px — default), `xl` (64px), `2xl` (80px).

### Cards (Tiles in Carbon terminology)
- `#f4f4f4` bg (Layer 01), no border, `0px` radius, `16px` padding.
- **Clickable tile**: hover fills `#e0e0e0` — no lift, no shadow.
- **Selectable tile**: left border thickens on selection to `4px solid #0f62fe`.

### Inputs (Text Input)
- Background: `#f4f4f4` (Layer 01), no top/left/right borders.
- Bottom border only: `1px solid #8d8d8d`.
- `0px` radius, `11px 16px` padding.
- Focus: bottom border becomes `2px solid #0f62fe`, no ring.
- Error: bottom border `2px solid #da1e28`.

### Data Tables
- `0px` radius, no border on cells (only on outer container).
- Header: `#e0e0e0` bg, `#161616` text, 14px weight 600 tracking `+0.16px`.
- Row separator: `1px solid #e0e0e0`.
- Hover row: `#e5e5e5` bg.

### Notifications
- `0px` radius, `16px` padding.
- Colored left border (4px): error `#da1e28`, warning `#f1c21b`, success `#24a148`, info `#4589ff`.

## 5. Layout Principles

### Spacing System
- Base unit: **4px** (Carbon uses a `spacing-01` through `spacing-13` scale)
- Dominant: `6px` (28 uses), `8px` (13), `4px` (6), `5.2px` (1)
- The sub-pixel values suggest density calculations for 24px grid UI

### Grid
- 2x grid (4-4-8-12-16-24 etc.) — Carbon follows IBM's enterprise grid
- Max content widths: `1584px` (max), `1312px` (xlg), `1056px` (lg), `672px` (md)
- Nav: `48px` tall top bar, `256px` or `16px` side nav

### Border Radius Scale
**There is no radius scale in Carbon.** The system uses `0px` radius exclusively except for:
- `2px`: Reserved for Inline Notifications (a single use)
- `50%`: Circular elements only (avatars, the "Back to Top" button)

This is Carbon's most defining visual choice — **sharp corners** as structural philosophy.

## 6. Depth & Elevation

| Level | Treatment | Use |
|-------|-----------|-----|
| Layer 01 | `#f4f4f4` bg on white canvas | Cards, first elevation |
| Layer 02 | `#ffffff` bg on layer-01 | Nested cards, second elevation |
| Layer 03 | `#f4f4f4` bg on layer-02 | Deepest nesting, third elevation |
| Modal | `0 2px 6px rgba(0,0,0,0.3)` | Dialog only — the one drop shadow in the system |
| Notification | `rgb(42,42,42) 1px 5px 5px 3px` | Toast, notification overlay |

**Shadow Philosophy**: Carbon uses **alternating layer backgrounds** instead of drop shadows for elevation. A card sits on Layer 01 (`#f4f4f4`) on a white canvas; a nested panel inside that card returns to Layer 02 (`#ffffff`) for contrast. This creates depth through tonal alternation — an enterprise-aware choice that renders identically in any printing context, doesn't rely on shadow rendering, and remains interpretable in high-contrast accessibility modes. Drop shadows appear only on modal dialogs and system-level notifications.

## 7. Do's and Don'ts

### Do
- Use `0px` radius on EVERY interactive element — the sharpness IS the brand
- Use IBM Plex Sans at weight 300 for display — enterprise lightness
- Apply positive letter-spacing (`+0.16-0.32px`) on body/caption sizes
- Use alternating layer backgrounds for elevation, not drop shadows
- Use IBM Blue (`#0f62fe`) as the singular interactive color
- Default to bottom-only borders on inputs — Material-inspired but simpler
- Use IBM Plex Mono for all code, data, and identifiers

### Don't
- Don't add border-radius — breaks 20 years of Carbon consistency
- Don't use weight 700 for display — Carbon caps at 600 for emphasis
- Don't use drop shadows on cards — use Layer 01/02/03 alternation
- Don't use Inter, SF Pro, or any non-IBM-Plex typeface — brand requirement
- Don't mix Carbon with Material or iOS components — the geometric language clashes
- Don't skip the accessibility audits — Carbon enforces WCAG AAA for IBM products

## 8. Responsive Behavior

### Breakpoints (Carbon's grid)
| Name | Width | Max Content | Changes |
|------|-------|-------------|---------|
| sm | `320px+` | 672px | Mobile, bottom nav, single column |
| md | `672px+` | 1056px | Tablet, 2-column layout |
| lg | `1056px+` | 1312px | Desktop, side nav visible |
| xlg | `1312px+` | 1584px | Wide desktop |
| max | `1584px+` | 1584px | Max content width |

### Touch Targets
- Buttons: `40-48px` height
- Data table row height: `40px` (compact), `48px` (default), `64px` (tall)
- Icon buttons: `40px × 40px`

### Collapsing Strategy
- Display: 92px → 54px → 42px across breakpoints, weight 300 maintained
- Navigation: top bar + side nav → top bar + hamburger drawer
- Data tables: horizontal scroll with sticky first column
- Cards: grid → stacked, `0px` radius maintained

## 9. Agent Prompt Guide

### Quick Color Reference
- Primary Blue: `#0f62fe` (IBM Blue)
- Background: `#ffffff`
- Layer 01: `#f4f4f4`
- Text: `#161616` (primary), `#525252` (secondary)
- Border: `#c6c6c6`
- Success: `#24a148`
- Error: `#da1e28`

### Example Component Prompts
- "Create a primary button: #0f62fe bg, white text, 0px radius (sharp corners), 0 16px padding, 48px height, 14px IBM Plex Sans weight 400 tracking +0.16px. Hover: #0353e9. Focus: 2px inset white + 4px solid #0f62fe outer ring."
- "Design a Carbon tile: #f4f4f4 bg (Layer 01) on white canvas, no border, 0px radius, 16px padding. Title 16px IBM Plex Sans weight 600 color #161616. Body 14px weight 400 tracking +0.16px color #525252. Clickable hover: #e0e0e0 bg."
- "Build a text input: #f4f4f4 bg, no top/left/right border, 1px solid #8d8d8d bottom-only border, 0px radius, 11px 16px padding. Label above at 12px weight 400 tracking +0.32px. Focus: bottom border becomes 2px solid #0f62fe."

### Iteration Guide
1. Sharp corners are non-negotiable — `0px` radius everywhere
2. IBM Plex Sans + weight 300 display = Carbon's voice
3. Positive tracking (`+0.16px`, `+0.32px`) on 14px and 12px text — readability at density
4. Layer-01/02/03 alternation replaces drop shadows
5. Bottom-only input borders — Material-inspired, not Material-copied
6. IBM Blue (`#0f62fe`) is the only interactive color — discipline is the design
