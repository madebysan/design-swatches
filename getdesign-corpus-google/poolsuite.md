---
version: alpha
name: "Poolsuite"
description: "Token-first design system reference for Poolsuite."

colors:
  background: "#ffffff"
  surface: "#e5e7eb"
  surface-elevated: "#f5f5f5"
  ink: "#000000"
  ink-muted: "#f6d5d5"
  primary: "#f9f0e9"
  on-primary: "#ffffff"
  border: "#afe2e5"
  focus-ring: "#f9f0e9"
  success: "#22c55e"
  warning: "#f59e0b"
  error: "#ef4444"
  shadow-soft: "#d9d9d9"

typography:
  display-hero:
    fontFamily: "Lineage, ui-sans-serif, system-ui, sans-serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.05
    letterSpacing: -1px
  display:
    fontFamily: "Lineage, ui-sans-serif, system-ui, sans-serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.5px
  heading-section:
    fontFamily: "Lineage, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.25px
  heading-sub:
    fontFamily: "Lineage, ui-sans-serif, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0px
  body-large:
    fontFamily: "Lineage, ui-sans-serif, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  body:
    fontFamily: "Lineage, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  button-ui:
    fontFamily: "Lineage, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: 0px
  caption:
    fontFamily: "Lineage, ui-sans-serif, system-ui, sans-serif"
    fontSize: 10px
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

# Poolsuite Design System

## Overview

Poolsuite is committed bit. The whole site behaves as if it were a 1995 Macintosh desktop that has been left running poolside for 30 years — a peachy-cream wallpaper (`#f9f0e9`), a top-left System 7 menu icon, a clock in the top-right reading `THU 30 APR 1997 / 21:18`, and a single faux-application window (titled `POOLSUITE`) floating dead-center streaming a fuzzy low-fi music video over a 1-bit television-static field. Where most retro sites flirt with the aesthetic, Poolsuite commits to the simulation: it's not "inspired by" old Mac OS, it IS old Mac OS, accurate down to the bevels, the pixelated dropdowns, and the way the window control buttons sit slightly inside their chrome.

The atmosphere is **vacation freeware**. Sunshine, palm cocktails, FM radio, screen savers, video noise — all quoted with affectionate precision rather than nostalgia kitsch. The faux-window is the dominant compositional move: a single hard-bordered rectangle (`1px solid #000`) with `4px` corners, an inset bevel highlight (`rgb(255,255,255) 1px 1px 0 0 inset`), an inset shadow lowlight (`rgb(155,155,155) -1px -1px 0 0 inset`), and a draggable header bar in light gray (`#e5e7eb`) with a Chicago-style title set in pixel type. The page exists only as scaffolding for the window — there is no scroll, no sections below the fold, no marketing copy, no hero pitch. You arrive directly inside the artifact.

What distinguishes Poolsuite is its **typographic monoculture of pixel fonts**. Five different bitmap typefaces stack on top of each other in this single screen — Pixolde, ChiKareGo2, Ishmeria, Everyday, and Pixelated Times New Roman — each used in its lane, all locked at 16px or 10px with negative `-1px` letter-spacing and aggressive sub-1.00 line-heights (`0.87`, `0.88`, `0.94`). There are no Google Fonts and no variable fonts. Every glyph is hand-pixeled; every weight is hard-coded. The system reads as a mid-90s "Fonts" folder where someone installed every freeware bitmap they could find and wired each one to a specific UI role.

**Key Characteristics:**
- Peachy-cream desktop background (`#f9f0e9`) — warm, vacation-skin tone, never white or gray
- Faux Mac OS window chrome as primary container — every piece of UI lives inside one
- Five-typeface bitmap stack (Pixolde, ChiKareGo2, Ishmeria, Everyday, Pixelated Times New Roman) — pixel fonts assigned by role
- 16px and 10px almost exclusively — type sizes barely vary; weight 400 with occasional 700
- 1-bit static / television noise as video poster frame — committed lo-fi visual
- Retro inset bevels (white-top, gray-bottom inner shadows) for window chrome and buttons
- 1px solid black borders everywhere — every element framed, no borderless surfaces
- Tiny radii (2-4px) on most elements; 9999px reserved for round chips
- Decorative menubar at top with phone-receiver icon, "BECOME A MEMBER / LOG IN", and live date+clock
- Bottom dock with cocktail-glass app icon ("Player") and tab bar (Newsroom · Mixtapes · Members · Events · Instagram · Vacation · Guestbook · Settings)

## Colors

### Desktop & Surfaces
- **Poolsuite Peach** (`#f9f0e9` / `rgb(249, 240, 233)`): The desktop wallpaper. Warm pinkish-cream — reads as Florida sunlight on a stucco wall. Used for the body, the inside of the player chrome, and any "freshly-painted" Mac surface.
- **Drag-Header Gray** (`#e5e7eb` / `rgb(229, 231, 235)`): Window title bars and toolbar strips. The classic System 7 light-gray that signals "this is grabbable / this is chrome."
- **Pure Black** (`#000000`): Window borders, all type, button outlines, divider rules, drop shadows. Workhorse line color. Appears 194 times in the extracted style count — the spine of the system.

### Accent Surfaces (Buttons & Highlights)
- **Player Mint** (`#afe2e5` / `rgb(175, 226, 229)`): A washed-out aqua used on the play/pause/skip transport button row. Cocktail-pool blue, faded. The closest the system gets to "primary CTA" color.
- **Player Pink** (`#f6d5d5` / `rgb(246, 213, 213)`): A washed-out rose used on the shuffle/queue button (right-most transport control). Pairs with mint as a candy-button duo. Calamine-lotion pink.

### State / System Colors (inherited from libraries)
- **Reject Red** (`#fb5858`): Vue Select dropdown deselect state. A bright punchy red used only for destructive/reject moments inside dropdowns.
- **Active Blue** (`#5897fb`): Vue Select dropdown active option. A 90s Aqua-style highlight blue.
- **Focus Ring Blue** (`#3b82f680`): Tailwind default ring color (50% opacity). Keyboard focus only — rarely visible on the surface.
- **Dark Slate** (`#333` / `#3c3c3c80` / `#3c3c3c42`): Vue Select control text and secondary borders, usually at 25-50% opacity for muted UI strokes.
- **Hairline Black** (`#00000026`): 15% opacity black used as the lightest divider tint.

### Bevel & Inset Tones
- **Bevel Highlight** (`#ffffff`): Inset top-left highlight on all chrome — `rgb(255,255,255) 1px 1px 0 0 inset`. The "light source from above-left" pixel.
- **Bevel Lowlight** (`rgb(155, 155, 155)`): Inset bottom-right shadow on chrome — `rgb(155,155,155) -1px -1px 0 0 inset`. The "depressed pixel" companion to the highlight.
- **Window-Drop Shadow** (`rgba(0, 0, 0, 0.3) 0 50px 80px -50px`): The single soft drop shadow in the system — used to float the main application window above the desktop. Reads as a long sun-cast shadow.

### Gradient System
- Poolsuite is **gradient-free in its surfaces** — no smooth color transitions on backgrounds. The illusion of depth comes entirely from inset bevel pairs, never from gradients. Where a modern site would use a gradient (button, header, hero), Poolsuite uses a flat tint plus a 1px bevel.

## Typography

### Font Family
The defining trait: **every typeface is a bitmap pixel font**, no Google Fonts, no variable fonts, no system stack except a `ui-sans-serif` fallback for accessibility. Each pixel face is assigned a specific UI role.

| Family | Lineage | Used For |
|--------|---------|----------|
| **Pixelated Times New Roman** | Bitmap revival of TNR | Display headings (`POOLSUITE` window title at 32px) |
| **Pixolde** | Modern pixel sans, multi-weight | Buttons, dock labels, primary UI labels (16px/400 and 16px/700) |
| **ChiKareGo2** | Chicago-flavored bitmap (Mac OS Chicago revival) | Links, Mac-style buttons, body chrome (16px/400, `-1px` tracking) |
| **Ishmeria** | Decorative pixel display | Specialty headings (16px/400 uppercase, `-1px` tracking) |
| **Everyday** | Tiny 5×7-cell pixel face | Captions, micro-labels, timestamps (10px/400, `-1px` tracking) |
| `ui-sans-serif` (system) | Fallback only | Aria-labels, screen-reader text, edge cases |

*Note: All five pixel faces are bitmap-style hinting designed for crisp rendering at fixed sizes. Substitutes for external implementations: Chicago FLF or Sevenet 7 (for ChiKareGo2), Press Start 2P or Pixeloid Sans (for Pixolde), Silkscreen or Tiny5 (for Everyday), VCR OSD Mono (for Pixelated Times New Roman).*

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Transform |
|------|------|------|--------|-------------|----------------|-----------|
| Window Title (Display) | Pixelated Times New Roman | 32px (2.00rem) | 400 | 0.47–1.00 | normal | uppercase |
| Section Heading (Specialty) | Ishmeria | 16px (1.00rem) | 400 | 0.88 | -1px | uppercase |
| Heading (Bold Pixel) | Pixolde | 16px (1.00rem) | 700 | 0.94 | -1px / normal | uppercase or mixed |
| Heading (Regular Pixel) | Pixolde | 16px (1.00rem) | 400 | 0.87–0.94 | normal | uppercase |
| Mac-Style Body / Link | ChiKareGo2 | 16px (1.00rem) | 400 | 1.00 | -1px | none |
| Button Label (UI) | Pixolde | 16px (1.00rem) | 400–700 | 0.87–1.50 | normal | uppercase |
| Button Label (Mac) | ChiKareGo2 | 16px (1.00rem) | 400 | 1.00 | -1px | none |
| Caption (Micro) | Everyday | 10px (0.63rem) | 400 | 1.00–1.50 | -1px | none |
| Fallback Body | ui-sans-serif | 16px | 400 | 1.50 | normal | none |

### Principles
- **Pixel-perfect fixed sizing**: Type is locked to 10px or 16px almost exclusively. There is no fluid scale, no responsive type-step, no clamp-based ramp. Pixel fonts only render crisp at their designed em-size, so the system refuses to deviate. The only display exception is the 32px window title.
- **Sub-1.00 line-heights**: Most pixel faces run at line-heights between `0.87` and `0.94` — tighter than is ergonomic for prose, but correct for fixed-cell pixel glyphs that already include vertical breathing room in the cell. The window title pushes to `0.47` for compressed Chicago-style stacking.
- **Negative `-1px` tracking**: Applied across ChiKareGo2, Ishmeria, and Everyday. At 10–16px sizes, `-1px` is a hefty proportional tightening — it pulls bitmap glyphs into ransom-note density.
- **Uppercase as a shouting register**: Headings, the menubar greeting (`BECOME A MEMBER / LOG IN`), the date strip (`THU 30 APR 1997`), and most buttons run uppercase. Mixed case is reserved for body text, song titles, and secondary metadata.
- **Five-face stack as identity**: The system explicitly does NOT consolidate typefaces. Each face does one job — collapsing to two faces would erase the "found-font" feeling that makes the page feel like an authentic 90s artifact.

## Layout

### Spacing System
- Base unit: **2px** (with 5px and 6px as common sub-rhythms — denser than 8px)
- Scale: 2px, 5px, 6px, 8px, 10px, 12px, 16px, 17px, 20px, 24px, 32px, 40px
- Most-used: 2px (88 instances), 10px (85), 6px (58), 5px (53) — the system runs on a 2-pixel rhythm, correct for pixel UIs aligning to literal pixels rather than a multiplied design grid
- 16px is the comfortable gap; 32px is the maximum interior padding on the page

### Grid & Container
- No traditional grid — a single centered floating window. Roughly 600px wide × 730px tall, centered, anchored ~50px from top.
- Top menubar and bottom-of-window dock: full-width strips
- Fixed-canvas, not fluid — everything fits in a single 1280×720 region, no scroll

### Whitespace Philosophy
- **Desktop expanse**: The pink desktop is mostly empty. The window sits in a sea of peach. Whitespace IS the desktop — it's not "negative space," it's "the operating system."
- **Tight UI density**: Inside the window, components pack tight — 5–10px between transport buttons, 2px between dock tabs. Pixel UIs honor pixels, not luxury whitespace.
- **No chapter breaks**: No scrolling sections means no vertical pacing rhythm. The composition is single-shot.

### Border Radius Scale
- **0px**: Sharp default for tabs, divider strokes, transport row interior segments
- **2px**: The workhorse mild round — used on 49 elements (input fields, pill buttons, micro-chips)
- **3-4px**: Outer window radius and the bevel on the largest buttons (56 elements at 4px)
- **6px**: Occasional medium round on certain panels (14 elements)
- **9999px**: Reserved for genuinely circular status dots and badges (15 instances)
- The system uses radii surgically — every value is a deliberate choice with a purpose, not a global rule

## Elevation & Depth

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | No shadow | Desktop body, plain text |
| 1px Drop Rule (Level 1) | `rgb(0,0,0) 0 1px 0 0` | Tab baselines, divider rules under headers |
| Mac Bevel Pair (Level 2) | `rgb(255,255,255) 1px 1px 0 0 inset` + `rgb(155,155,155) -1px -1px 0 0 inset` + `rgb(0,0,0) 0 0 0 1px` | Default raised state — buttons, panels, chrome |
| Recessed Inset (Level 3) | `rgba(0,0,0,0.2) 0 0 0 1px inset, rgba(0,0,0,0.2) 0 -11px 0 0 inset` | Pressed/grooved input wells, scrollbar tracks |
| Mac Bevel + Drop (Level 4) | Mac bevel pair + `rgb(0,0,0) 0 1px 0 0` | Aqua transport buttons (mint/pink) — full physical click |
| Window Float (Level 5) | `rgba(0,0,0,0.3) 0 50px 80px -50px` | The main application window's drop shadow on the desktop |

**Shadow Philosophy**: Poolsuite uses **two-stop bevels**, not blurred shadows. Every interactive element has a 1px white inset on its top-left and a 1px gray (or warm-gray `rgb(123,107,107)` on warm surfaces) inset on its bottom-right. This is the canonical "raised pixel button" of Mac System 7 / Windows 95-era UI, ported faithfully. The single soft blurred shadow in the entire system is the long sunset shadow under the main window — and even that uses a low-opacity (`0.3`) wash, no glow, no halo.

### Decorative Depth
- The system gives a **physical click feel** on aqua transport buttons (Level 4) by stacking a black 1px drop shadow under the bevel — when pressed, the shadow collapses
- Dropdown wells are **carved into** their parent (Level 3 inset) using two stacked dark-rgba inset shadows that read as routed grooves
- Window-on-desktop separation is the only "atmospheric" depth in the entire system — every other elevation is graphic-bevel, not blur

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

**Mac Aqua Transport (Mint)**
- Background: Player Mint (`#afe2e5`)
- Text/Icon: Pure Black (`#000000`)
- Padding: 0 (icon-only); chrome height locks at the toolbar row
- Radius: `4px 0 0 4px` (left-segment of a button group)
- Border: `1px solid #000`
- Shadow: `rgb(0,0,0) 0 1px 0 0, rgb(255,255,255) 0 1px 0 0 inset` — black bottom drop + white top inset, the canonical Mac button bevel
- Use: Play / Pause / Skip Back / Skip Forward (the four central transport controls)

**Mac Aqua Transport (Pink)**
- Background: Player Pink (`#f6d5d5`)
- Text/Icon: Pure Black (`#000000`)
- Radius: `4px` (full radius, end-cap segment)
- Border: `1px solid #000`
- Shadow: same Mac bevel pair as Mint variant
- Use: Shuffle / Queue Tools (rightmost transport control)

**Chrome Square (Window Controls)**
- Background: Pure Black (`#000`) for top-bar controls; Peach (`#f9f0e9`) for content-area controls
- Radius: `0px` (sharp) for chrome; `0px 0px 4px 0` for corner-anchored buttons
- Border: contextual partial borders — `0 1px 1px 0 solid #000` for leading-edge segments, `1px 1px 0 0` for trailing-edge segments
- Padding: `9px 10px 8px` typical
- Shadow: Mac-bevel pair (`rgb(155,155,155) -1px -1px 0 0 inset, rgb(255,255,255) 1px 1px 0 0 inset, rgb(0,0,0) 0 0 0 1px`) on framed variant
- Use: Window close `×`, screen-saver toggle, minimize, app-icon header buttons

**Tab Pill (Footer Dock)**
- Background: transparent
- Border: `1px 1px 0 solid #000` (top + sides, no bottom — the tab joins the toolbar baseline)
- Padding: 8–10px horizontal, 6–8px vertical
- Radius: `0px`
- Font: Pixolde 16px / 400 / uppercase
- Shadow: `rgb(0,0,0) 0 1px 0 0, rgb(255,255,255) 0 1px 0 0 inset`
- Use: Bottom dock tabs — Newsroom, Mixtapes, Members, Events, Instagram, Vacation, Guestbook, Settings

**Outline Header Pill**
- Background: peach (`#f9f0e9`)
- Border: `1px solid #000`
- Radius: `2px`
- Padding: 6–10px horizontal
- Shadow: Mac-bevel pair
- Font: ChiKareGo2 16px / 400 / `-1px` tracking, uppercase
- Use: Top-left "BECOME A MEMBER / LOG IN" CTA, top-right date and clock chips

### Window Chrome (Primary Container)
- Background: Drag-Header Gray (`#e5e7eb`) for the title bar; Peach (`#f9f0e9`) for the body
- Border: `1px solid #000` exterior
- Radius: `4px` outer corners (4px on all four corners — softly rounded but unmistakably square)
- Inner Bevel: `rgb(255,255,255) 1px 1px 0 0 inset, rgba(0,0,0,0.2) 0 0 0 1px inset, rgba(0,0,0,0.2) 0 -11px 0 0 inset` — light from top-left, deep recessed bottom edge
- Drop Shadow: `rgba(0,0,0,0.3) 0 50px 80px -50px` — a single long, soft, low cast shadow that sits the window above the desktop
- Title bar: 17px tall, pixel-type wordmark right-aligned, three icons left-aligned (`×` close, calendar/screen-saver, minimize)
- Status bar (bottom): 17px tall, divided into three cells — caption (filename like `Martini-Bianco.mpeg`), fixed-width spacer, dimensions (`591x455`)

### Cards & Containers
- Cards in Poolsuite are not "cards" — they are **inset panels** carved out of the window body
- Background: matches parent (peach or gray)
- Border: `0px 0px 1px 1px solid #000` for left+bottom rules, or full `1px solid #000`
- Radius: `0` or `2px`
- Shadow: inverted Mac bevel — `rgb(0,0,0) 0 0 0 1px, rgb(255,255,255) 1px 1px 0 0 inset, rgb(123,107,107) -1px -1px 0 0 inset` (the duller `rgb(123,107,107)` lowlight is used on warm/peach surfaces vs. the cooler `rgb(155,155,155)` on gray surfaces)
- Internal padding: 8–10px (tight) — pixel UIs don't waste pixels

### Pills & Status Chips
- Round pills (`9999px` radius) appear 15 times — used for circular status dots, member badges, signal-strength indicators
- Background: black or transparent
- Border: `1px solid #000`
- Size: typically 8–12px diameter
- Use: ornamental status, decorative dots, never primary text containers

### Inputs (Vue Select Dropdown)
- Background: peach `#f9f0e9` or white `#fff` for active option
- Border: `1px solid #000`, Radius: `2px`
- Open dropdown: black background (`#000`) with white text, the active option highlights in `#5897fb` (Mac Aqua blue), reject states flash `#fb5858` red
- Font: ChiKareGo2 16px / `-1px`
- Used in the channel switcher (`Channel: Poolsuite FM (Default)`)

### Top Menubar (Page Chrome)
- Position: fixed, full width, 32px tall
- Left side: phone-receiver icon (telephone glyph) + "BECOME A MEMBER / LOG IN" pill at 32px height with `1px` black border, peach interior
- Right side: two chips — date (`THU 30 APR 1997`) with calendar/clock icon and time (`21:18`) with watch icon, separated by a vertical 1px divider
- Mimics System 7 menu bar exactly: white-ish (peach) interior, black 1px border on the bottom edge

### Bottom Dock
- Position: anchored to bottom of the main window
- Left: large 32×32 cocktail-glass icon (martini), labeled `Player` in 10px Everyday — this is the running "app"
- Center: 8 horizontal tab buttons (Newsroom, Mixtapes, Members, Events, Instagram, Vacation, Guestbook), each rendered as a top-bordered Pixolde-uppercase tab
- Right: square 32×32 settings icon (computer monitor glyph), labeled `Settings` in 10px Everyday
- Background: peach (`#f9f0e9`)
- Border: 1px solid #000 along the top edge, dividing the dock from the player content above

### Decorative Elements
- **Television Static**: 1-bit black-and-white noise field on the video player when paused — not a placeholder, the brand identity for "media is loading"
- **Pixel Glyphs**: All system icons (telephone, calendar, clock, cocktail glass, monitor) are hand-pixeled bitmaps, not SVG line icons
- **Bevel-Pair Buttons**: Every interactive element wears the canonical Mac OS bevel — white-top inset + dark-bottom inset — even at the smallest 16×16 sizes

## Do's and Don'ts

### Do
- Frame everything inside a Mac-style window with `1px solid #000` border, `4px` radius, gray title bar, and a Mac-bevel pair
- Use peach (`#f9f0e9`) as the desktop wallpaper — never pure white, never gray
- Stack pixel typefaces by role: Pixolde for buttons, ChiKareGo2 for body, Pixelated Times New Roman for display, Everyday for 10px captions, Ishmeria for specialty heads
- Set negative `-1px` letter-spacing on bitmap fonts at 10–16px
- Use sub-1.00 line-heights (0.87–0.94) on pixel headings
- Use Mac-bevel inset pairs (`#fff` top-left, `rgb(155,155,155)` bottom-right) on every interactive surface
- Reserve gradient-free, flat-tint surfaces with bevels for depth — never CSS gradients
- Use mint (`#afe2e5`) and pink (`#f6d5d5`) ONLY for transport / aqua-style buttons — they are not theme colors
- Pin a top menubar with phone icon + member CTA + live date/time
- Pin a bottom dock with one big "app" icon (cocktail glass) + tab row + settings icon
- Use 1-bit static / TV noise as the loading state for any media surface
- Lock to fixed 16px and 10px type sizes — pixel fonts blur if interpolated

### Don't
- Don't use sans-serif system fonts as primary text — pixel fonts are the brand
- Don't use border radii in the 5–8px range for buttons — Poolsuite is binary on radii (0/2/4 for sharp, 9999 for round)
- Don't use blurred drop shadows except for the single window-on-desktop float shadow
- Don't introduce gradients, glassmorphism, or modern soft-UI effects — every depth cue is a 1px bevel
- Don't pad generously — 2–10px is the working spacing range, not 16–32px
- Don't scroll — the page is fixed-canvas, single-shot
- Don't smooth pixel fonts with antialiasing tricks — they should render crisp and steppy
- Don't drop the menubar or dock — the OS chrome IS the design
- Don't use mint or pink as backgrounds for body text — they're transport-button-only
- Don't replace the 1-bit static with a smooth gradient placeholder — committing to the static is the joke

---

## Responsive Behavior

### Breakpoints (Tailwind defaults)
| Name | Width | Behavior |
|------|-------|----------|
| Mobile | <640px | Window scales proportionally; some controls collapse to icon-only |
| Tablet | 640–1024px | Standard fixed window size, centered |
| Desktop | 1024–1280px | Default canvas |
| Large Desktop | ≥1280px | Window stays fixed; desktop wallpaper expands as empty peach field |

### Touch Targets
- Transport buttons: ~32×32px; dock tabs: 32×~60px; window chrome controls (`×`, min): 16×16, intentionally tiny and faithful to Mac OS scale

### Collapsing Strategy
- **Window scaling**: On smaller viewports the window shrinks proportionally rather than reflowing — Mac windows don't reflow, neither does Poolsuite
- **Tab dock**: Tabs collapse to icon-only or scroll horizontally on narrow widths
- **Top menubar**: "BECOME A MEMBER / LOG IN" abbreviates to icon-only on mobile; date may shorten (`30 APR` → `4/30`)
- **Type sizing**: Type does NOT step down — pixel fonts stay locked at 16px / 10px at every viewport. The brand is the pixel grid; rescaling would corrupt it.

### Image Behavior
- 1-bit video static and bitmap icons render identically at every breakpoint — no vector scaling, no responsive art direction

---

## Agent Prompt Guide

### Quick Color Reference
- Desktop Background: Poolsuite Peach (`#f9f0e9`)
- Window Title Bar: Drag-Header Gray (`#e5e7eb`)
- Window Body: Poolsuite Peach (`#f9f0e9`)
- All Text & Borders: Pure Black (`#000000`)
- Transport Mint Button: `#afe2e5`
- Transport Pink Button: `#f6d5d5`
- Bevel Highlight (Inset): `#ffffff` top-left
- Bevel Lowlight (Inset, cool): `rgb(155, 155, 155)` bottom-right
- Bevel Lowlight (Inset, warm): `rgb(123, 107, 107)` bottom-right (on peach surfaces)
- Window Float Shadow: `rgba(0,0,0,0.3) 0 50px 80px -50px`
- Active Highlight (Dropdown): `#5897fb`
- Reject (Dropdown): `#fb5858`

### Example Component Prompts
- "Create a Poolsuite-style application window centered on a `#f9f0e9` desktop. Window: `1px solid #000`, `4px` radius, drop shadow `rgba(0,0,0,0.3) 0 50px 80px -50px`. Title bar: 17px tall, `#e5e7eb` background, Pixelated Times New Roman 16px uppercase right-aligned. Body padding 8–10px on `#f9f0e9`."
- "Build a Mac-bevel transport button: 32×32px, `#afe2e5` background, `1px solid #000`, `4px 0 0 4px` radius for the leftmost button in a group. Apply box-shadow `rgb(0,0,0) 0 1px 0 0, rgb(255,255,255) 0 1px 0 0 inset`. Center a black playback icon. Font N/A — icon only."
- "Create a top menubar pinned to the top of the viewport — 32px tall, `#f9f0e9` background, `1px solid #000` bottom border. Left: a 16×16 black telephone icon followed by 'BECOME A MEMBER / LOG IN' in ChiKareGo2 16px uppercase with `-1px` letter-spacing inside a peach pill (`1px solid #000`, `2px` radius). Right: two pill chips for date and time, each with a 10px Everyday font caption."
- "Build a dock tab — Pixolde 16px weight 400 uppercase label inside a top-bordered tab cell. Border: `1px 1px 0 solid #000`. Background: transparent. Apply `rgb(255,255,255) 1px 1px 0 0 inset, rgba(0,0,0,0.2) 0 0 0 1px inset, rgba(0,0,0,0.2) 0 -11px 0 0 inset` for the recessed bottom-edge feel. Padding: 8px 12px."
- "Create a status caption — Everyday font, 10px, weight 400, `-1px` letter-spacing, color `#000`, line-height 1.00. Use for filenames like `Martini-Bianco.mpeg` and dimensions like `591x455`."
- "Build a 1-bit static placeholder — full-bleed black-and-white noise pattern (random 1px black/white pixels), no smoothing, no antialiasing. Used as the video player poster frame."

### Iteration Guide
1. The faux-window is the design — every UI lives inside one. Never ship borderless surfaces.
2. Pixel fonts are locked at 16px or 10px. Do not use other sizes; do not antialias.
3. Bevel pairs (`#fff` top-left inset + `rgb(155,155,155)` bottom-right inset) replace gradients everywhere. Never use a CSS gradient.
4. Peach (`#f9f0e9`) for desktop and warm surfaces, gray (`#e5e7eb`) for chrome only.
5. Mint and pink are transport-button-only. Never use them for backgrounds, text, or general theming.
6. Spacing rhythm is 2px-based, not 8px. Tight UI density is correct.
7. Negative `-1px` letter-spacing on ChiKareGo2, Ishmeria, and Everyday at all sizes.
8. Use uppercase for nav, labels, and headings. Mixed case for body and song titles.
9. Single soft drop shadow exists only on the main window. All other depth is bevel.
10. Commit to the simulation — top menubar, bottom dock, draggable title bars, fake date/time stamps. The bit IS the brand.
