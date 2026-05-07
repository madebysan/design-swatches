---
version: alpha
name: "Otherkind"
description: "Token-first design system reference for Otherkind."

colors:
  background: "#ffffff"
  surface: "#f5d4cc"
  surface-elevated: "#f5f5f5"
  ink: "#000000"
  ink-muted: "#f0c8be"
  primary: "#f5f5f5"
  on-primary: "#ffffff"
  border: "#ff9500"
  focus-ring: "#f5f5f5"
  success: "#22c55e"
  warning: "#f59e0b"
  error: "#ef4444"
  shadow-soft: "#d9d9d9"

typography:
  display-hero:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 72px
    fontWeight: 400
    lineHeight: 1.05
    letterSpacing: -1px
  display:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 50px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.5px
  heading-section:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.25px
  heading-sub:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0px
  body-large:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  body:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  button-ui:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
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

# Otherkind Design System

## Overview

Otherkind's website is a craft-led studio site dressed as a desktop computer that has been left running. The base layer is editorial restraint — a warm off-white canvas (`#f5f5f5`), a single oversized black wordmark set in heavy display type, and a flat two-column ledger of past engagements with no decorative chrome. But sitting on top of that editorial layer is an OS chrome layer: a tiny mouse-coordinate readout (`X:0000 Y:0000`) in the upper-left corner, a "BACK" indicator next to it, and twin atomic-clock timestamps anchored to the bottom corners of every page (`SEOUL 10:19:46 AM` on the left, `NYC 09:19:46 PM` on the right). These two layers — magazine and machine — are the entire identity. The studio is in two cities, the website tells you what time it is in both, constantly.

The studio runs on Monument Grotesk and Monument Mono — Dinamo's quietly-everywhere pairing of the late 2020s — and uses them with discipline. Display moments use the heavy black weight of the proportional grotesk for the wordmark only; everything else, including the entire body of the page, runs at a single 16px proportional setting and a single 12–14px monospace setting in uppercase. There are no headline sizes between the wordmark and the body. Sections are demarcated by tiny mono labels (`Past Engagements`, `Select Projects`, `Team`) sitting flush-left in the same body size. The page reads like a printed broadsheet that happens to be running on System 7.

What pushes Otherkind from "tasteful studio site" into something more specific is the **modal window**. Click "Photobook" and a Mac Classic / System 7 application window opens in the middle of the screen — pinstriped title bar, close box in the upper-left, real scrollbars, a "Magazine" content area showing TV-static imagery, and a dock-style row of Susan Kare-era pixel icons floating below the window on a dusty pink (`#f5d4cc`-ish) wallpaper. This is not a one-line nostalgia gag. It's a fully realized second context — the studio's "creative output" lives behind that retro chrome, while the studio's "professional surface" stays in the flat editorial frame. Two visual systems, one site, on a switch.

**Key Characteristics:**
- Two-layer aesthetic: flat editorial broadsheet on the outside, classic Mac OS modal on the inside
- One display moment only — the heavy black `Otherkind` wordmark, full-bleed across the top
- Monument Grotesk (proportional) for content, Monument Mono uppercase for chrome and labels
- Twin city timestamps (Seoul + NYC) anchored to bottom corners on every page — live, ticking
- Mouse-coordinate readout (`X:0000 Y:0000`) in upper-left as a vestigial OS HUD
- Dotted-underline links — the only consistent decorative move in the body
- Off-white canvas (`#f5f5f5`) for the studio site; dusty rose/peach for the retro modal layer
- A single tiny accent color — System Orange (`#ff9500`) — used only for one decorative pixel-window border
- Zero shadows, zero gradients, zero ornament outside the OS-chrome modal

## Colors

### Primary
- **Otherkind Black** (`#000000`): The wordmark, body text, every label, every link. Pure, full-strength. The studio does not soften its primary color.
- **Otherkind Off-White** (`#f5f5f5`): The page canvas. A warm neutral that reads as paper, not screen. Same exact value as Cape's canvas — the late-2020s default for craft-led studios.
- **Pure White** (`#ffffff`): Reserved for the modal/window content area, project card backgrounds, and inverted moments.

### Brand Accent
- **System Orange** (`#ff9500`): The Apple system-orange, used in a single place — a 1px border on a small decorative span inside the retro modal. This is not a brand color in the traditional sense; it's a quotation mark around the "this is a Mac" reference. Applied with extreme restraint (one element on the entire site).

### Modal Wallpaper Tones
- **Dusty Rose** (approx `#f5d4cc` / `#f0c8be`): The wallpaper color behind the Mac Classic modal — a warm pinkish-peach that reads like a faded 1996 desktop pattern.
- **Pinstripe Gray** (approx `#cccccc` / `#dddddd`): The classic horizontally-striped title-bar pattern on modal windows.

### Neutrals & Text
- **Otherkind Black** (`#000000`): All body, all headings, all UI labels.
- **LCH Near-Black** (`lab(15.204 0 -0.00000596046)`): A perceptually-near-black that appears on a single link state. Effectively `#000000` for human eyes — kept distinct here only because it's literally what the CSS reports.
- **Pure White on Dark** (`#ffffff`): Link color on dark/imagery surfaces (modal content overlays).

### Surface & Borders
- **Surface Off-White** (`#f5f5f5`): Page background and most flat-section panels.
- **Card White** (`#ffffff`): Project card surfaces — flat rectangles with `20px` corners, no shadow, just sitting on the canvas.
- **Border System Orange** (`#ff9500`): The one-off pixel-art border treatment. Applied as `1px solid #ff9500` on a small decorative span; sometimes as a single-edge rule (`border-bottom: 1px solid #ff9500`).

### Gradient & Shadow System
- Otherkind is **gradient-free and shadow-free**. There is not a single gradient fill or drop shadow anywhere in the body of the site. Cards float on the off-white canvas with their own white fill alone — pure contrast does the work that elevation usually does. The retro modal uses pixel-perfect 1-bit black borders for window chrome, not soft shadows.

## Typography

### Font Family
- **Primary (proportional)**: `Monument Grotesk`, with fallback: `Monument Fallback`, `monumentMono`, `monumentMono Fallback`, `sans-serif`
- **Secondary (monospace)**: `Monument Grotesk Mono`, with fallback: `monumentMono Fallback`, `monospace`
- **Wordmark Display**: A heavy black grotesque/serif hybrid used only for the `Otherkind` logo — likely a custom or licensed display cut. Cooper Black-adjacent in weight but tighter and more constructed. Web-safe substitutes: Druk Heavy, Reckless Bold Italic, or Söhne Breit Kraftig.
- **OpenType Features**: Standard ligatures only. Tabular figures appear in the timestamps and year labels — a deliberate choice so the numbers don't shift width as the clock ticks.

*Note: Monument Grotesk and Monument Grotesk Mono are commercial typefaces from Dinamo. For external implementations, ABC Diatype + ABC Diatype Mono, or Söhne + Söhne Mono serve as close substitutes.*

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Wordmark | Display Black | ~120–180px viewport-fit | 900 | 1.00 | tight | One per site — top of every page |
| Body / Heading-1 | Monument Grotesk | 16px (1.00rem) | 400 | 1.50 | -0.2px | The single content size — intros, paragraphs, list items, section labels |
| Caption (proportional) | Monument Grotesk | 14px (0.88rem) | 400–500 | 1.43 | -0.2px | Engagements list, project titles, team-member names |
| Caption (mono) | Monument Mono | 12px (0.75rem) | 400 | 1.33 | -0.2px | UPPERCASE — used for nav links, footer chrome, button labels |
| Caption Small (mono) | Monument Mono | 10px (0.63rem) | 400 | 1.50 | -0.2px | Cursor coordinate readout, micro-metadata |
| Link (mono, footer) | Monument Mono | 12px (0.75rem) | 400 | 1.33 | -0.2px | UPPERCASE, dotted underline — `CONTACT TWITTER PHOTOBOOK` |

### Principles
- **One body size, no heading scale**: There is effectively no typographic hierarchy between the wordmark and the body. Sections are separated by space, not size. Every paragraph, list, and caption sits at 16px or below. This is unusual — most sites use 4–6 size steps; Otherkind uses 2 (display + body).
- **Mono for chrome, proportional for content**: Monument Mono is reserved exclusively for OS-chrome elements: nav, footer links, timestamps, coordinate readout, button labels. Monument Grotesk handles all reading text. The pairing reads like a UNIX terminal sitting alongside a magazine page.
- **Uniform negative tracking**: Every text size carries `-0.2px` letter-spacing. No progressive scaling like Cape's. The tracking is constant — a precision setting, not a typographic flourish.
- **Uppercase for all UI**: Every Monument Mono usage is uppercase. Every chrome label (`CONTACT`, `TWITTER`, `PHOTOBOOK`, `BACK`, city codes) is uppercased mono. Mixed case is reserved for content.
- **Tabular numerals on the clocks**: Both timestamp readouts use tabular figures so the seconds tick without horizontal jitter — a small detail that elevates the live-clock from gimmick to instrument.

## Layout

### Spacing System
- Base unit: 8px
- Scale: 2px, 8px, 16px, 32px, 64px, 96px
- Notable: The scale skips 4px and 24px entirely — Otherkind doesn't use mid-tight values. It either sits at chrome-density (2–8px) or breathing-section density (32–96px). Nothing in between. The list rows sit at ~8px gaps; the major sections sit at 96px gaps; there's nothing at 24–48px.

### Grid & Container
- Max content width: approximately 720–800px for the body column (engagements list, intro paragraph) — narrow, like an essay column
- Wordmark: full-bleed across the viewport, hugging both edges with ~16px inset
- Project thumbnails: 2-column grid at desktop, full-bleed cards
- Team: 2-column grid of square portraits, single-column on mobile
- The page reads as one tall narrow column with the wordmark and the cards bursting wider — magazine layout, not webapp layout

### Whitespace Philosophy
- **Magazine pacing**: Major sections are separated by ~96px of vertical air. Within sections, rows sit tight (8–16px gaps). The page breathes between chapters and stays dense within them.
- **No section dividers**: Otherkind never uses a horizontal rule, a colored block, or a background tint to separate sections. White space and a small mono label do the work.
- **Centered solitude**: The 404 page strands a single line of text in the middle of the viewport with the chrome (cursor HUD top, timestamps + links bottom) intact. The empty space is not awkward — it's framed.

### Border Radius Scale
- Sharp (0px): All chrome elements — wordmark, list rows, modal window, mono links
- Soft (20px): Project cards only — the single rounded value on the entire site
- Pill (50%): One decorative span inside the retro modal
- No mid-range radii: Like Cape's binary system, Otherkind avoids 4–16px. The system is sharp, soft (20px), or fully circular.

## Elevation & Depth

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | No shadow, no border | Page canvas, body text, list rows, headings |
| Tone Card (Level 1) | White fill on off-white canvas | Project thumbnails — depth via tone, not shadow |
| Pixel Border (Level 2) | `1px solid #000` (modal) or `1px solid #ff9500` (decorative span) | Mac Classic chrome — windows, buttons, decorative spans |
| Modal Lift (Level 3) | None — modal sits flat on its dusty-rose wallpaper | The Photobook window doesn't cast a shadow — it's pinned to its retro desktop |

**Shadow Philosophy**: Otherkind has **no shadow system**. This is rare and intentional. Where Cape uses hard offset stamps and most sites use soft drop shadows, Otherkind uses tone contrast (white-on-off-white) for its only depth move. The retro modal — the one place a shadow would feel natural — also has none, because Mac Classic windows didn't have drop shadows in 1995. The flatness is era-accurate.

### Decorative Depth
- Pixel-rendered chrome supplies all the "depth" the site needs — a 1px black window border around a white modal reads as a window without any rendering trick beyond the border itself.
- Dotted underlines on links create a kind of texture that reads as depth at small sizes.
- The cursor HUD and timestamp bars float above content not via z-index drama but via simple `position: fixed` placement — they're stuck to the viewport edges like menu-bar items.

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
Otherkind technically has no traditional buttons. Where most studio sites use bordered or filled CTAs, Otherkind uses **plain text links with dotted underlines** in Monument Mono uppercase.

**Mono Link (the universal CTA)**
- Background: transparent
- Text: Otherkind Black (`#000000`) on light, Pure White (`#ffffff`) on dark
- Decoration: `underline dotted`
- Padding: 0 (it's text, not a control)
- Font: 12px Monument Mono weight 400, UPPERCASE, letter-spacing `-0.2px`
- Use: Every interactive element on the marketing surface — `CONTACT`, `TWITTER`, `PHOTOBOOK`, "Join the team", `hello@otherkind.design`

**Modal Window Buttons**
- Style: pixel-art mac-classic — 1px solid black border, white fill, hand-pixel-rendered icons in 16×16 or 24×24 squares
- Use: Inside the Photobook modal only — close box, scroll arrows, dock icons

### Cards & Containers
- Background: `#ffffff` for content cards (project thumbnails); `#f5f5f5` (canvas) for everything else
- Border: `0px` — the white card on off-white canvas creates the boundary through tone alone
- Radius: `20px` — the only rounded corner on the site, used uniformly for project cards. Soft enough to read as friendly, large enough to feel deliberate.
- Shadow: `none` — not even subtle. The card system relies on tone contrast.
- Internal padding: minimal (8–32px) — cards are tight crops, not airy containers

### Lists (the signature component)
The "Past Engagements" list is the most distinctive component on the site. It's a left-aligned client name + right-aligned year, repeated 14 times, no bullets, no rules, no hover state visible.
- Layout: flex row, space-between
- Font: 14px Monument Grotesk weight 400 for both name and year
- Spacing: ~8px vertical between rows — tight, like a credits list
- Years: 2024, 2025, 2026 — chronologically descending implicit by recency

### Badges / Tags / Pills
Otherkind does not use badges. Project cards have no category tags, team members have no skill chips. The system rejects this entire UI pattern — context is communicated through copy, not labels.

### Inputs & Forms
- The site has no forms. Contact is handled via mailto links to `hello@otherkind.design` and `jobs@otherkind.design`.
- The Photobook modal contains a faux input field as part of the retro chrome — styled with the Mac Classic 1px black border and white fill.

### Navigation
- **Top nav**: There is no traditional top navigation. The wordmark is the entire header.
- **Footer nav**: Bottom-fixed, three-column layout — left corner Seoul timestamp, center `CONTACT  TWITTER  PHOTOBOOK`, right corner NYC timestamp. All three center links are Monument Mono uppercase with dotted underlines.
- **Cursor HUD**: Top-left of viewport — `X:0000 Y:0000` updates on mouse move; a "BACK" link sits adjacent on inner pages.
- **Sticky behavior**: The footer chrome (timestamps + links) is fixed to the viewport bottom. The cursor HUD is fixed to the upper-left. Both persist while content scrolls.

### Decorative Elements

**Mac Classic Modal Window**
- Title bar: pinstriped horizontal-line pattern (1px alternating black/white rows)
- Close box: solid black square with inner white square — 11×11px
- Window border: 1px solid black, no radius
- Scrollbar: classic 1-bit Mac with arrow caps — pixel-perfect, not approximated
- Dock icons: 24×24 pixel-art rendered with no anti-aliasing
- Wallpaper: dusty rose/peach solid fill behind the modal

**Cursor Coordinate Readout**
- Position: fixed top-left, ~16px inset
- Format: `X:0000` / `Y:0000` stacked
- Font: 10px Monument Mono weight 400, UPPERCASE
- A small "BACK" link sits next to it on inner pages — same font, same size

**City Timestamp Bars**
- Position: fixed bottom-left + bottom-right
- Format: `SEOUL 10:19:46 AM` / `NYC 09:19:46 PM`
- Font: 12px Monument Mono weight 400, UPPERCASE, letter-spacing `-0.2px`
- Updates: live, every second, with tabular figures

## Do's and Don'ts

### Do
- Use Monument Grotesk at 16px weight 400 for the entire body — resist the urge to add heading sizes
- Use Monument Mono at 12px UPPERCASE for every chrome element — nav, footer, timestamps, labels
- Apply `-0.2px` letter-spacing uniformly across all type sizes — it's a precision setting, not a flourish
- Underline links with `dotted` decoration — solid underlines feel wrong in this system
- Anchor twin city timestamps to the bottom corners and let them tick live with tabular figures
- Use white cards (`#ffffff`) on the off-white canvas (`#f5f5f5`) for any visual containers — the tone gap is the boundary
- Use `20px` border-radius on cards and `0px` everywhere else — the system is binary
- Reserve the retro Mac Classic modal for "creative archive" content (Photobook, gallery, behind-the-scenes) — not for nav or core info
- Embrace flatness — no shadows, no gradients, no glass. Tone and 1px borders do all the work.

### Don't
- Don't introduce heading sizes between the wordmark and the body — it breaks the magazine ledger feel
- Don't use solid underlines on links — `dotted` is the house style
- Don't use proportional caps where mono uppercase belongs (and vice versa) — the proportional/mono split is structural
- Don't add drop shadows or elevation gradients — the system is shadow-free everywhere except where pixel borders do the job
- Don't use category tags, badges, or skill chips on cards or team members — Otherkind communicates context through copy
- Don't soften corners between 0 and 20px — there is no 8px or 12px in this system
- Don't translate the timestamps to viewer-local — they're literally Seoul and NYC, the studio's two cities
- Don't make the cursor coordinate readout interactive — it's a vestigial HUD, watching the cursor, not commanding it
- Don't use the orange (`#ff9500`) accent on anything new — it's a one-place quotation mark, not a brand color
- Don't add a hamburger menu — there is no nav to collapse

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile | <768px | Single column, wordmark scales down to ~64–96px, project grid becomes 1-up |
| Desktop | ≥768px | Full layout — wordmark fills viewport, project grid 2-up, team grid 2-up |

The site uses a **single breakpoint** (768px). There is no tablet vs. desktop distinction, no large-desktop tier. The layout either is the mobile stack or the desktop ledger.

### Touch Targets
- Mono links: padded vertically with line-height 1.33 — tap area ~32–40px effective
- Modal close box and scrollbar arrows: kept at pixel-accurate 11×11 / 16×16 sizes — these are decorative reproductions; the modal closes via a wider invisible hit area or click-outside

### Collapsing Strategy
- **Wordmark**: Scales fluidly with viewport width — likely a `clamp()` or vw-based size. Always full-bleed.
- **Engagements list**: Stays as a flex row even on mobile — the year column never wraps below the client name. Both columns just compress.
- **Project cards**: 2-up at desktop, 1-up at mobile, full-bleed both ways
- **Team grid**: 2-up at desktop, 2-up still at mobile (smaller portraits) — keeps the editorial grid feel
- **Cursor HUD**: Hidden on touch devices (no cursor) — would otherwise show `X:0000 Y:0000` perpetually
- **Timestamps**: Persist on mobile, anchored to bottom-left and bottom-right corners
- **Modal window**: Resizes to ~90vw on mobile but keeps its Mac Classic chrome — the title bar, close box, and scrollbar all scale proportionally

### Image Behavior
- Project thumbnails maintain their `20px` border-radius across all viewports
- Team portraits stay square at every breakpoint
- The retro modal's pixel art does not get anti-aliased on retina displays — preserved 1:1 for accuracy

---

## Agent Prompt Guide

### Quick Color Reference
- Page Background: Otherkind Off-White (`#f5f5f5`)
- Primary Text: Otherkind Black (`#000000`)
- Card Surface: Pure White (`#ffffff`)
- Modal Wallpaper: Dusty Rose (~`#f5d4cc`)
- Accent (one place only): System Orange (`#ff9500`)
- Link Decoration: `underline dotted`
- Border (chrome): `1px solid #000000`
- Border (decorative one-off): `1px solid #ff9500`

### Example Component Prompts
- "Create a hero on Otherkind Off-White (`#f5f5f5`) with a single full-bleed wordmark in a heavy black display weight, ~120–180px tall, centered horizontally with ~16px viewport inset. No subtitle. No CTA. Just the wordmark."
- "Build a 'Past Engagements' list — flex rows with `space-between`, client name flush-left in Monument Grotesk 14px weight 400, year flush-right in the same font. ~8px row gap. No bullets, no rules, no hover state."
- "Add a fixed bottom-left timestamp `SEOUL 10:19:46 AM` and a fixed bottom-right timestamp `NYC 09:19:46 PM` — both in Monument Mono 12px weight 400 UPPERCASE with `-0.2px` letter-spacing and tabular figures. Update every second using `Intl.DateTimeFormat` with the corresponding timezone."
- "Add a fixed top-left cursor HUD showing `X:0000` and `Y:0000` stacked, in Monument Mono 10px weight 400 UPPERCASE. Update on `mousemove`, padding both axes to four digits."
- "Create a project card — Pure White (`#ffffff`) fill on the off-white canvas, `20px` border-radius, no border, no shadow, no padding around the image. Caption below in Monument Grotesk 14px weight 400."
- "Build a Mac Classic modal window — `1px solid #000000` border, no border-radius, white fill, pinstriped horizontal-line title bar, 11×11 close box in the upper-left, 16×16 pixel-perfect scroll arrows. Position it centered on a dusty-rose (`#f5d4cc`) wallpaper backdrop. No drop shadow."
- "Footer nav — three Monument Mono uppercase links (`CONTACT  TWITTER  PHOTOBOOK`) at 12px weight 400, `underline dotted`, ~24px gap between them, centered horizontally on the bottom edge."

### Iteration Guide
1. Use exactly two type sizes for content: 16px proportional body + 14px proportional caption. Resist adding any heading scale.
2. Reserve Monument Mono UPPERCASE for chrome only — nav, footer, timestamps, coordinate HUD, button labels. Never use it for prose.
3. Apply `-0.2px` letter-spacing to every text size uniformly. No progressive tracking like Cape — it's a flat setting.
4. Underline every link with `dotted`, never solid. Color it `#000000` on light surfaces, `#ffffff` on dark.
5. Use `20px` border-radius for cards and `0px` for everything else. No mid-range radii.
6. No shadows anywhere. Use white-on-off-white tone gap or `1px solid #000` borders for separation.
7. The twin city timestamps and cursor HUD are non-negotiable identity elements — port them to any new page.
8. The Mac Classic modal is a separable second context — use it for archive/gallery content, never for primary nav or essential info.
9. System Orange (`#ff9500`) is sacred — one element on the entire site. Don't extend it to "primary accent" duty.
10. Let the wordmark do all the visual heavy lifting. The rest of the system is deliberately quiet so it can shout.
