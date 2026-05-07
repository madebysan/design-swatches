---
version: alpha
name: "Link-Kit"
description: "Token-first design system reference for Link-Kit."

colors:
  background: "#ffffff"
  surface: "#242930"
  surface-elevated: "#f5f5f5"
  ink: "#111111"
  ink-muted: "#e4e4e4"
  primary: "#fafafa"
  on-primary: "#ffffff"
  border: "#1e1e1e"
  focus-ring: "#fafafa"
  success: "#22c55e"
  warning: "#f59e0b"
  error: "#ef4444"
  shadow-soft: "#d9d9d9"

typography:
  display-hero:
    fontFamily: "SFProDisplay, ui-sans-serif, system-ui, sans-serif"
    fontSize: 72px
    fontWeight: 400
    lineHeight: 1.05
    letterSpacing: -1px
  display:
    fontFamily: "SFProDisplay, ui-sans-serif, system-ui, sans-serif"
    fontSize: 50px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.5px
  heading-section:
    fontFamily: "SFProDisplay, ui-sans-serif, system-ui, sans-serif"
    fontSize: 20px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.25px
  heading-sub:
    fontFamily: "SFProDisplay, ui-sans-serif, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 500
    lineHeight: 1.25
    letterSpacing: 0px
  body-large:
    fontFamily: "SFProDisplay, ui-sans-serif, system-ui, sans-serif"
    fontSize: 19px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  body:
    fontFamily: "SFProDisplay, ui-sans-serif, system-ui, sans-serif"
    fontSize: 17px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  button-ui:
    fontFamily: "SFProDisplay, ui-sans-serif, system-ui, sans-serif"
    fontSize: 17px
    fontWeight: 600
    lineHeight: 1.0
    letterSpacing: 0px
  caption:
    fontFamily: "SFProDisplay, ui-sans-serif, system-ui, sans-serif"
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

# Link-Kit Design System

## Overview

Link-Kit is a no-chrome utility — a single-page builder that gets out of its own way. The product is "the link in bio for design conscious creatives," and the homepage performs that brief: it IS the builder. There is no marketing hero, no scroll-jacked feature parade, no testimonial wall. You land on a two-column workspace — a sticky iPhone-shaped preview card on the left, a long form on the right — and you start typing. Every visual decision serves that "tool, not a pitch" stance.

The canvas is near-white (`#fafafa`) with a single floating panel framed by a hairline border (`1px solid rgba(36, 41, 48, 0.1)`) and tucked inside a generously rounded `30px` container. Inside, everything else is gentler: `3px` and `5px` micro-radii on inputs, accordions, and form chrome; `10px` and `20px` on the stacked content cards; `100px` pills on the on-card "Link Title" and "See More" buttons. The palette is functionally monochrome — Slate (`#242930`) for ink, Off-Black (`#1e1e1e`) for primary chrome, Light Heather (`#e4e4e4`) for the header bar — broken only by the user-uploaded media inside the preview cards (cobalt blue, golden yellow, leaf green). The product gets its color from your content, not from the system.

What distinguishes Link-Kit is the **dual-surface composition logic**: a workspace canvas that is light, neutral, and professional, paired with a preview card that is dimensional, playful, and shaped exactly like a phone. The preview is the only place gradients live (the OG image cards layer text over photo-warmth via a black-to-transparent scrim). The form is the only place inputs live. The two halves never bleed into each other. The whole homepage is essentially a live demo masquerading as a marketing site, and the design respects that lie hard enough to make it true.

**Key Characteristics:**
- SF Pro Display top to bottom — the macOS system display face, no custom font
- Single-page builder layout — sticky preview card left, scrolling form right
- Slate ink (`#242930`) and Off-Black chrome (`#1e1e1e`) — no chromatic accent in the UI
- Hairline borders (`1px solid rgba(36, 41, 48, 0.1)`) instead of fills for soft separation
- Mixed radius scale: `3px` (inputs) → `5px` (cards) → `10px` (content cards) → `20px` (preview) → `30px` (page frame) → `100px` (pills)
- Phone-shaped preview card (`max-350px` wide, `br-20`) anchors the left column
- The only color comes from user-uploaded image cards inside the preview
- Dark "Save Progress" button (`#111111`) plus a white-to-dark gradient strip CTA below it
- Heather-gray header bar (`#e4e4e4`) inside a `5px` rounded container — a soft chip floating above white

## Colors

### Primary
- **Slate** (`#242930`): Primary text color — body copy, headings, link text, label text. The base color of all readable content.
- **Off-Black** (`#1e1e1e`): Brand chrome — logo wordmark, "Save Progress" button (after blend), used as the dominant ink in CSS counts (205 occurrences). Slightly warmer than pure black.
- **Pure White** (`#ffffff`): Page canvas, input fills, button text on dark surfaces.

### Background & Surface
- **Canvas White** (`#fafafa` / near-pure white): Page background. Reads as paper.
- **Heather Gray** (`#e4e4e4`): Header bar fill — a soft warm gray that floats the navigation as a rounded chip above the canvas.
- **Card Gray** (`#f4f4f4`): Preview card fallback fill before image uploads — empty state.
- **Inky Slate** (`#111111`): Submit button background — slightly lifted from pure black for screen comfort.

### Borders & Dividers
- **Hairline Slate** (`rgba(36, 41, 48, 0.1)`): The default border for inputs, cards, accordions, and the page-level container — barely visible, defines structure without weight. 38 occurrences.
- **Medium Slate** (`rgba(36, 41, 48, 0.3)`): Stronger border on selected radio labels (Personal Account, Light Mode) — signals active state without color.

### Overlay & Disabled
- **Disabled Gray** (`rgba(100, 100, 100, 0.2)`): Translucent fill on inactive on-card buttons inside preview cards — sits on top of imagery.
- **Placeholder Gray** (`#aaaaaa`): Select dropdown placeholder text, "Number Of Links" empty state.
- **Muted Slate 50%** (`rgba(36, 41, 48, 0.5)`): Helper text, "Upload Profile Icon (max 0.5MB)", numbered link prefix `01.` `02.` `03.`

### Gradient System
- **Card Scrim** (`linear-gradient(to bottom, rgba(0,0,0,0) 0%, rgba(0,0,0,0.6) 100%)`): The only gradient inside the preview cards — drops a black scrim on the bottom 40% of each image so white card text stays legible regardless of the photo behind it.
- **Submit Strip** (`linear-gradient(to right, #ffffff, #1e1e1e)`): The signature "Ready to get started? Sign Up" CTA — a horizontal white-to-near-black wash that runs the full button width. Visually says "this is the action that ends the form."

### Image Accents (Content, Not System)
- Demo imagery ships in cobalt blue, golden yellow, and leaf green — these are not brand colors, they're the sample photography that demonstrates card-with-photo layout. Treat as content, never as system tokens.

## Typography

### Font Family
- **Primary**: `SFProDisplay`, `-apple-system`, `BlinkMacSystemFont`, `system-ui`, sans-serif
- **Monospace**: Not used — Link-Kit has no code, no technical labels, no terminal aesthetic
- **OpenType Features**: Standard ligatures only

*Note: SF Pro Display is Apple's system display face, free for use across web and Apple platforms. It pulls Link-Kit toward a "macOS-native utility" feel rather than an editorial-web feel. Inter is the closest open-source substitute; Helvetica Now Display works for paid licensing.*

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| H0 — Page Title | SF Pro Display | 38px (2.38rem) | 500 | 1.30 | -0.38px | "Build Your Link Kit" — single page-level heading |
| H1 — Preview Name | SF Pro Display | 28px (1.75rem) | 700 | 1.10 | 0.24px | "YOUR NAME" — uppercase, the only bold weight on the page |
| H3 — Section Heading | SF Pro Display | 20px (1.25rem) | 500 | 1.30 | -0.20px | "Your Details", "Your Link Kit" |
| H3 Alt — Accordion | SF Pro Display | 20px (1.25rem) | 400 | 1.30 | 0.24px | "Link 01", "Link 02" — lighter weight |
| Body Large | SF Pro Display | 17px (1.06rem) | 400 | 1.30 | 0.24px | Preview card paragraph copy |
| Body / Input | SF Pro Display | 16px (1.00rem) | 400 | 1.30 | 0.24px | Form labels, slug prefix, button text |
| Section Label | SF Pro Display | 16px (1.00rem) | 500 | 1.30 | 0.24px | "Create your Link Kit" header caption |
| Header Pill | SF Pro Display | 14px (0.88rem) | 500 | 1.00 | 0.24px | "Login", "Sign Up" nav buttons |
| Body Small | SF Pro Display | 14px (0.88rem) | 400 | 1.30 | 0.24px | Helper text, link copy, on-card buttons |
| Caption | SF Pro Display | 11px (0.69rem) | 400 | 1.00 | 0.24px | Micro-labels, on-card chrome |
| Caption Tiny | SF Pro Display | 10px (0.63rem) | 400 | 1.30 | 0.24px | Legal / meta text |

### Principles
- **Weight 500 as default for hierarchy**: Link-Kit's heading scale lives at weight 500, not 700. Bold (700) is reserved for one place — the uppercase preview-card name (`H1: YOUR NAME`). This makes the form feel quiet and the preview feel loud, exactly the inversion of a typical marketing site.
- **Light positive tracking everywhere except H0**: Almost every text style sits at `+0.24px` letter-spacing. This is unusual — most modern systems use negative tracking on display text. The positive tracking creates a subtle airy quality across the form, slightly Apple-Settings-app in feel. H0 (`Build Your Link Kit`) is the lone exception at `-0.38px`.
- **1.30 line-height as the universal default**: From 38px headings to 14px body, almost every style runs at line-height 1.30. The exceptions are the 28px uppercase H1 (1.10 — tight for visual weight) and 11px/14px caption variants (1.00 — single-line chrome).
- **Two effective weights — 400 and 500**: Link-Kit uses 400 for body and supporting text, 500 for everything labeled or interactive (headers, section titles, header buttons), and 700 only once (preview name). No 300, no 600, no 800.
- **Preview = uppercase. Form = mixed case.** The single uppercase block in the system is the preview's name field. Everything else stays sentence case. This contrast separates "your published link kit" from "your editing surface."

## Layout

### Spacing System
- Base unit: 5px (with 8px and 10px as primary working values)
- Scale: 5px, 8px, 10px, 15px, 20px, 40px, 60px
- Notable: 10px is the workhorse — 97 occurrences in the JSON. The `gap-10` class fuels almost every form-row layout.
- Larger units (40px, 60px) appear only in section-level breaks (`mt40`, `gap-40` between Form column and Preview column)

### Grid & Container
- Outer max-width: `1600px` (`max-1600`) — wide for a builder, allows preview + form to breathe side by side at 1440+
- Inner form max-width: `650px` (`max-650`) — keeps right-column form readable
- Preview max-width: `350px` (`max-350`) — phone-shaped, fixed
- Page is a single 2-column flex (`gap-40`) — left 50% / right 50%, collapsing to stacked single column at 991px
- The whole page is wrapped in a 30px-radius `1px` border frame — gives the workspace a "document" feel

### Whitespace Philosophy
- **Functional pacing, not editorial**: Sections inside the form sit at `gap-40` (40px) between major groups (Your Details → Your Link Kit → Profile Url → Number Of Links → Links). Inside each group, fields use `gap-10`/`gap-20`. The rhythm is fast and dense — this is a form, not a marketing page.
- **Single page, no scroll-jacked breaks**: There is no `100vh` hero, no parallax, no animated reveals. The page is one continuous workspace from top to bottom.
- **Sticky asymmetry**: The left preview is `position: sticky`, so it stays in view as you scroll the right form. This is the most important layout move — it gives the user a permanent "what your kit looks like right now" reference without taking up modal space.

### Border Radius Scale
- Micro (3px): Inputs, submit buttons, small chrome — the workhorse interaction radius
- Small (5px): Header bar, link accordions, small cards — soft chips
- Medium (10px): Content cards inside the preview — strong enough to read as "card" but not bubble-y
- Preview (20px): The phone-shaped preview card — slightly oversized to evoke iOS device bezels
- Frame (30px): The page-level outer container — generous enough to read as "this is the entire workspace"
- Pill (100px): Only the on-card translucent buttons — fully rounded micro-pills, no other element uses this

## Elevation & Depth

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | No shadow, no border | Page canvas, body text |
| Hairline (Level 1) | `1px solid rgba(36, 41, 48, 0.1)` | Default state for inputs, cards, the outer page frame, the preview card — defines structure without weight |
| Medium Border (Level 2) | `1px solid rgba(36, 41, 48, 0.3)` | Active/checked state on radio labels — selection cue |
| Soft Drop (Level 3) | `rgba(0, 0, 0, 0.1) 0px 10px 25px 0px` | Used once in the system on a single emphasized card — Link-Kit's only true atmospheric shadow |
| Image Scrim (Level 4) | `linear-gradient(180deg, transparent 0%, rgba(0,0,0,0.6) 100%)` | Inside content cards — a downward fade behind text overlays on imagery |

**Shadow Philosophy**: Link-Kit's depth system is borders, not shadows. The entire workspace is constructed from hairline strokes at `rgba(36, 41, 48, 0.1)` — buttons, inputs, accordions, the preview, and the outer frame all share the same border treatment. The only real drop shadow in the JSON appears once. This is a deliberate move: the design relies on radius variation (3 → 5 → 10 → 20 → 30) to create perceived depth, not on lighting. The result is a system that reads as a flat document with hierarchical rounding rather than a 3D stack of floating cards.

### Decorative Depth
- Inside content cards, the bottom 40% gets a black-to-transparent gradient scrim. This is the only place in the system where "depth" is created via lighting rather than a stroke.
- The `gradient strip CTA` at the bottom of the form (white → near-black) is a graphic device, not a depth cue — it's flagging the action as terminal, not lifting it off the page.

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

**Primary Submit (Inky Slate)**
- Background: Inky Slate (`#111111`)
- Text: Pure White (`#ffffff`)
- Padding: 15px 20px
- Radius: `3px`
- Border: `1px solid rgba(36, 41, 48, 0.1)`
- Shadow: `none`
- Font: 16px SF Pro Display weight 400
- Hover: background stays `#111111`, color stays `#ffffff` — no color change, slight cursor-driven feel only
- Use: "Save Progress" — the main commit action of the page

**Gradient Strip CTA**
- Background: `linear-gradient(to right, #ffffff, #1e1e1e)`
- Text: Pure White (`#ffffff`)
- Padding: 15px 20px
- Radius: `3px`
- Font: 16px SF Pro Display weight 400
- Use: "Ready to get started? Sign Up" — the only gradient-filled element in the system, signals the terminal action of the flow

**Header Pill (Heather)**
- Background: Light Heather (`#e4e4e4`)
- Text: Slate (`#242930`)
- Padding: 8px 12px
- Radius: `5px`
- Border: `0px`
- Font: 14px SF Pro Display weight 500
- Hover: background → `#666666`, text fades to 50% opacity
- Use: "Login", "Sign Up" in the top header bar

**On-Card Translucent Pill**
- Background: `rgba(100, 100, 100, 0.2)` — translucent gray over photography
- Text: Pure White (`#ffffff`)
- Padding: 8px 10px
- Radius: `100px` (full pill)
- Border: `0px`
- Font: 11px SF Pro Display weight 400
- Hover: background → `#333333`
- Use: "Link Title" / "See More" buttons inside the preview content cards — sit on top of imagery without breaking it

### Cards & Containers

**Preview Card (the iPhone)**
- Background: Pure White (`#ffffff`)
- Border: `1px solid rgba(36, 41, 48, 0.1)`
- Radius: `20px`
- Max-width: `350px`
- Padding: 20px (with 0px right padding to allow card carousel bleed)
- Shadow: `none` — sits flat
- Use: Sticky left-column preview that mirrors the form state in real time

**Page Frame**
- Background: Pure White (`#ffffff`)
- Border: `1px solid rgba(36, 41, 48, 0.1)`
- Radius: `30px`
- Max-width: `1600px`
- Padding: 40px desktop, 0 mobile
- Use: The outer container that holds the entire two-column workspace — frames the page like a soft document

**Content Card (Carousel Slide)**
- Background: image with linear-gradient scrim (`bg-grey` fallback)
- Aspect ratio: `1:2` (portrait, phone-tall)
- Radius: `10px`
- Padding: 10px header, 15px body
- Use: The visual cards that appear inside the preview — your actual link kit content

**Link Accordion**
- Background: Pure White (`#ffffff`)
- Border: `1px solid rgba(36, 41, 48, 0.1)`
- Radius: `5px`
- Padding: 15px
- Use: Collapsible per-link form section ("01. Link 01", "02. Link 02"...)

### Badges / Tags
Link-Kit has no badges, status pills, or tags in the system. The only pill-shaped objects are buttons (header CTAs, on-card actions). The product trusts plain text and structure.

### Inputs & Forms

**Text Input**
- Background: Pure White (`#ffffff`)
- Border: `1px solid rgba(36, 41, 48, 0.1)`
- Radius: `3px`
- Padding: 10px
- Font: 16px SF Pro Display weight 400, color `#000000`
- Placeholder: Slate at 50% opacity
- Focus: outline removed, no visible focus ring (a real accessibility gap to fix in a derivative system)
- Use: All single-line text fields (Full Name, Email, URL, Card Title)

**Select**
- Same chrome as text input
- Placeholder color: `#aaaaaa`
- Use: "Number Of Links" — the only select in the system

**Radio (rendered as label chip)**
- Default: hairline border `rgba(36, 41, 48, 0.1)`, radius `3px`, padding 10px, white background
- Checked: background flips to Off-Black (`#1e1e1e`), text to white, with a checkmark icon at right
- Use: Personal vs Business Account; Light vs Dark Mode; Image/GIF vs Video — three places, identical treatment

**Slug Input (Composite)**
- Wrapper: `1px solid rgba(36, 41, 48, 0.1)`, flex, align-center
- Prefix label: 16px Slate text "link-kit.com/" — non-editable
- Input: borderless, fills remaining width
- Use: Username/handle field — visually one chip, mechanically prefix + input

### Navigation
- Header bar: Heather Gray (`#e4e4e4`) chip with `5px` radius, padding 20px, full-width but inside the `1600px` max
- Logo: SVG wordmark "linkkit." in Off-Black (`#1e1e1e`), weight 700, lowercase with terminal period
- Center caption: "Create your Link Kit" — 16px weight 500
- Right CTAs: Login + Sign Up pills (Heather-on-Heather, very low contrast — they're recessive chrome, not heroes)
- No sticky behavior on the header itself; the preview card uses `position: sticky` instead

### Decorative Elements
Link-Kit has none. No icons in the form. No illustrations. No background patterns. The single decorative-feeling element is the on-card scrim gradient inside content cards, and even that exists for a functional reason (text legibility over imagery). The product's aesthetic position is "designer-tool simplicity" and the design honors it.

## Do's and Don'ts

### Do
- Use SF Pro Display weight 400 for body and 500 for hierarchy — reserve 700 for the single uppercase preview name
- Default to hairline borders (`1px solid rgba(36, 41, 48, 0.1)`) for all surface separation — they're the structural primitive
- Apply `+0.24px` letter-spacing to most text — Link-Kit's slightly airy positive tracking is the typographic signature
- Build forms in a 2-column layout that collapses to 1 column under 991px
- Make the preview surface sticky so it follows the user as they scroll the form
- Use the radius ladder (`3 → 5 → 10 → 20 → 30 → 100`) to express hierarchy — small radii on inputs, large radii on the page frame
- Reserve gradients for two places only: the on-card image scrim (functional) and the final-action CTA strip (signal)
- Let user-uploaded media bring all the color — keep the system itself monochrome
- Use 1.30 line-height as the universal default — it's the rhythm Link-Kit runs on
- Build a single-page workspace — no marketing detours, no scroll-jack, the product is the homepage

### Don't
- Don't use pure black (`#000000`) for body ink — Slate (`#242930`) is warmer and matches the ink count in the design
- Don't introduce a chromatic accent color — Link-Kit gets all of its color from user content, not from system tokens
- Don't use shadows for elevation — borders + radius variation handle the entire depth system
- Don't reach for negative letter-spacing on body text — Link-Kit's tracking is positive (+0.24px) almost everywhere
- Don't add a 6th heading level — H0 / H1 / H3 / Body covers the entire scale; mid-levels are intentionally absent
- Don't put the form inside a modal or wizard — it's a single scrollable surface and that's the point
- Don't use the gradient CTA more than once per page — it's the page's terminal action signal
- Don't add iconography to form fields — Link-Kit is text-and-input only, icons would feel foreign
- Don't use bold (700) anywhere except the preview-card name — bold is reserved as a contrast device
- Don't replace SF Pro Display with a serif or display face — the macOS-native feel is load-bearing

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile | <768px | Single column, preview stacks above form, header pills shrink |
| Tablet Small | 768–900px | Still single column, content reflows with `m-grid-1` overrides |
| Tablet | 900–991px | Form starts to relax but preview/form still stacked |
| Desktop | 991–1400px | 2-column layout activates — preview left, form right |
| Wide | ≥1400px | Full `max-1600` container fills out, generous side padding |

### Touch Targets
- Submit buttons: 15px × 20px padding — above 44px tap minimum
- Header pills: 8px × 12px — small but adequate via line-height padding
- Radio chips: 10px padding, full-width within grid cell — easy to thumb-tap
- Accordion arrows (`↑ ↓ +`): tight, would benefit from a larger hit zone in any derivative

### Collapsing Strategy
- 2-column flex collapses to single column on mobile; preview card moves above the form
- Outer `p40` collapses to `p0` — the workspace becomes edge-to-edge on small screens
- `grid-2` becomes `m-grid-1` — Full Name / Email side-by-side becomes stacked
- Sizes hold across breakpoints — no fluid type scale, SF Pro Display looks correct at every width
- "Create your Link Kit" caption hides on mobile (`m-hide`) — only logo + auth pills remain
- Preview card stays at `max-350px` at all breakpoints; surrounding whitespace grows, the card doesn't
- Content cards maintain `1:2` aspect ratio; uploaded images use `object-fit: cover`

---

## Agent Prompt Guide

### Quick Color Reference
- Primary Ink: Slate (`#242930`)
- Brand Chrome: Off-Black (`#1e1e1e`)
- Submit Button: Inky Slate (`#111111`)
- Page Background: Canvas White (`#fafafa`)
- Header Bar: Heather Gray (`#e4e4e4`)
- Hairline Border: `1px solid rgba(36, 41, 48, 0.1)`
- Active Border: `1px solid rgba(36, 41, 48, 0.3)`
- Helper Text: `rgba(36, 41, 48, 0.5)`
- Placeholder: `#aaaaaa`
- Card Scrim Gradient: `linear-gradient(180deg, transparent 0%, rgba(0,0,0,0.6) 100%)`
- Final CTA Gradient: `linear-gradient(to right, #ffffff, #1e1e1e)`

### Example Component Prompts
- "Build a single-page workspace with a 2-column flex layout (50/50, gap 40px). Left column contains a sticky preview card — `350px` max-width, `1px solid rgba(36, 41, 48, 0.1)` border, `20px` border-radius, white background, 20px padding. Right column contains a long scrolling form with `max-width: 650px`. Wrap the entire page in an outer container with `30px` border-radius, hairline border, white fill, `40px` padding."
- "Design the page header as a Heather Gray (`#e4e4e4`) bar with `5px` border-radius and 20px padding, sitting above the workspace. Left: SF Pro Display weight 700 logo wordmark in Off-Black (`#1e1e1e`). Center: 'Create your Link Kit' in SF Pro Display 16px weight 500, hidden on mobile. Right: two pill buttons ('Login', 'Sign Up') with 14px weight 500 text, `5px` radius, 8px × 12px padding, same Heather background."
- "Create a primary submit button — Inky Slate (`#111111`) background, white 16px SF Pro Display text, `15px 20px` padding, `3px` border-radius, `1px solid rgba(36, 41, 48, 0.1)` border, no hover color change. Place a second button directly below it using `linear-gradient(to right, #ffffff, #1e1e1e)` as the background — same padding and radius — for the terminal 'Sign Up' action."
- "Build a content card inside the preview — `1:2` aspect ratio, `10px` border-radius, full-bleed user image with `linear-gradient(180deg, transparent 0%, rgba(0,0,0,0.6) 100%)` scrim on the bottom 40%. Two translucent pill buttons in the top-left and top-right at `rgba(100, 100, 100, 0.2)` background, `100px` border-radius, 11px white SF Pro text, 8px × 10px padding."
- "Style a radio chip — full-width within its grid cell, `1px solid rgba(36, 41, 48, 0.1)` border, `3px` radius, 10px padding, 16px SF Pro text in Slate (`#242930`). When checked: flip background to Off-Black (`#1e1e1e`), text to white, append a right-aligned checkmark icon, upgrade border to `rgba(36, 41, 48, 0.3)`."

### Iteration Guide
1. Default to SF Pro Display + system fallbacks — no custom font, no Google Fonts
2. Use Slate (`#242930`) for text and Off-Black (`#1e1e1e`) for chrome — never pure `#000`
3. Reach for hairline borders (`1px solid rgba(36, 41, 48, 0.1)`) before reaching for shadows — borders are the structural primitive
4. Keep the radius ladder coherent: `3px` for inputs, `5px` for chrome, `10px` for cards, `20px` for the phone-shaped preview, `30px` for the page frame, `100px` only for circular pills
5. Apply `+0.24px` letter-spacing as the default for everything except the H0 page title (which uses `-0.38px`)
6. Anchor hierarchy at weight 500 for headings; reserve weight 700 for a single uppercase moment (preview-card name)
7. Confine gradients to two roles: image scrim inside content cards, and the final CTA strip
8. Make the preview sticky and the form scrolling — the spatial split is the product
9. Let user content provide all color — the system itself stays monochrome
10. Build the homepage AS the product — no marketing hero, no testimonials, no scroll-jacked feature reel. The form is the pitch.
