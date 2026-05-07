---
version: alpha
name: Ferrari
description: Digital editorial for the Prancing Horse — chiaroscuro alternation between absolute black cinematic sections and crisp white panels, FerrariSans precision, surgical 2px corners, and Ferrari Red used as singular CTA stamp.

colors:
  # Brand
  primary: "#da291c"           # Ferrari Red
  primary-hover: "#b01e0a"     # Dark Red
  primary-active: "#9d2211"    # Deep Red

  # Surfaces
  background: "#ffffff"
  surface-dark: "#000000"      # Absolute Black
  surface-mid-dark: "#303030"  # Dark Surface
  surface-light: "#d2d2d2"     # Light Gray Surface
  overlay-dark: "#121212"      # opaque approx of hsla(0,0%,7%,0.8) — Google format requires hex

  # Text
  ink: "#181818"               # Near Black — primary body
  ink-inverted: "#ffffff"
  text-secondary: "#666666"
  text-muted: "#8f8f8f"
  text-placeholder: "#969696"

  # Heritage accents
  yellow-racing: "#fff200"     # Racing Yellow
  yellow-modena: "#f6e500"     # Modena Yellow

  # Semantic
  warning: "#f13a2c"
  success: "#03904a"
  info: "#4c98b9"
  link-hover: "#3860be"
  hover-teal: "#1eaedb"

  # Borders
  border: "#cccccc"

  # Shadow stand-in
  shadow-soft: "#999999"       # opaque approx of subtle 1px-cookie-dialog shadow

typography:
  section-title:
    fontFamily: "FerrariSans, Arial, Helvetica, sans-serif"
    fontSize: 26px
    fontWeight: 500
    lineHeight: 1.20
    letterSpacing: 0px
  card-heading:
    fontFamily: "FerrariSans, Arial, Helvetica, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.20
    letterSpacing: 0px
  subheading:
    fontFamily: "FerrariSans, Arial, Helvetica, sans-serif"
    fontSize: 18px
    fontWeight: 700
    lineHeight: 1.20
    letterSpacing: 0px
  ui-heading:
    fontFamily: "FerrariSans, Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.40
    letterSpacing: 0.08px
  body-bold:
    fontFamily: "FerrariSans, Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 700
    lineHeight: 1.30
    letterSpacing: 0px
  button:
    fontFamily: "FerrariSans, Arial, Helvetica, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.20
    letterSpacing: 1.28px
  small-button:
    fontFamily: "FerrariSans, Arial, Helvetica, sans-serif"
    fontSize: 14.4px
    fontWeight: 700
    lineHeight: 1.00
    letterSpacing: 0px
  nav-link:
    fontFamily: "FerrariSans, Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 600
    lineHeight: 1.20
    letterSpacing: 0.13px
  caption:
    fontFamily: "FerrariSans, Arial, Helvetica, sans-serif"
    fontSize: 13px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0.195px
  micro-button:
    fontFamily: "FerrariSans, Arial, Helvetica, sans-serif"
    fontSize: 12px
    fontWeight: 700
    lineHeight: 1.00
    letterSpacing: 0.96px
  label-upper:
    fontFamily: "Body-Font, FerrariSans, Arial, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.27
    letterSpacing: 1px
  micro-label:
    fontFamily: "Body-Font, FerrariSans, Arial, sans-serif"
    fontSize: 11px
    fontWeight: 400
    lineHeight: 1.27
    letterSpacing: 1px

spacing:
  micro: 1px
  xs: 2px
  sm: 4px
  md: 8px
  lg: 12px
  xl: 16px
  2xl: 20px
  3xl: 25px
  4xl: 40px
  5xl: 60px
  6xl: 80px

rounded:
  none: 0px
  micro: 1px
  sharp: 2px
  modal: 8px
  pill: 9999px

components:
  button-primary:
    backgroundColor: "{colors.background}"
    textColor: "{colors.surface-dark}"
    typography: "{typography.button}"
    rounded: "{rounded.sharp}"
    padding: 12px 10px
  button-primary-hover:
    backgroundColor: "{colors.hover-teal}"
    textColor: "{colors.ink-inverted}"

  button-subscribe:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.ink-inverted}"
    typography: "{typography.button}"
    rounded: "{rounded.sharp}"
    padding: 12px 10px
  button-subscribe-hover:
    backgroundColor: "{colors.primary-hover}"

  button-ghost:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.ink-inverted}"
    typography: "{typography.button}"
    rounded: "{rounded.sharp}"
    padding: 12px 10px
  button-ghost-hover:
    backgroundColor: "{colors.hover-teal}"

  button-small:
    backgroundColor: "{colors.background}"
    textColor: "{colors.surface-dark}"
    typography: "{typography.small-button}"
    rounded: "{rounded.sharp}"
    padding: 8px 12px

  card-editorial:
    backgroundColor: "{colors.background}"
    rounded: "{rounded.none}"
    padding: 0px

  card-cinematic:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.ink-inverted}"
    rounded: "{rounded.none}"
    padding: 40px

  input-newsletter:
    backgroundColor: "{colors.surface-mid-dark}"
    textColor: "{colors.ink-inverted}"
    typography: "{typography.body-bold}"
    rounded: "{rounded.sharp}"
    padding: 12px 10px

  modal:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    rounded: "{rounded.modal}"
    padding: 24px

  nav-bar:
    backgroundColor: "{colors.surface-dark}"
    textColor: "{colors.ink-inverted}"
    typography: "{typography.nav-link}"
    padding: 16px 25px

  link:
    textColor: "{colors.ink}"
    typography: "{typography.nav-link}"
    padding: 0px
  link-hover:
    textColor: "{colors.link-hover}"
---

# Ferrari Design System

## Overview

Ferrari's website is a digital editorial — a curated magazine where the Prancing Horse brand is presented with the gravitas of an art institution and the precision of Italian coachwork. The page opens onto an expanse of absolute black, broken only by the iconic Prancing Horse emblem floating alone in its own atmosphere. Below, the content unfolds in dramatic alternations between inky-dark cinematic sections and crisp white editorial panels. This chiaroscuro rhythm — darkness yielding to light, machinery yielding to human story — feels more like paging through a Ferrari yearbook than scrolling a commercial website. Every section is a curated vignette: a concept car dissolving from shadow, two F1 drivers posed with sculptural stillness, a lineup of production models arranged in a jewel-toned parade.

The color language is monastically restrained for a brand built on speed and emotion. Ferrari Red (`{colors.primary}`) appears with almost surgical sparseness — reserved for the Subscribe CTA and accent moments that need to command immediate attention. The vast majority of the interface lives in black, white, and a carefully calibrated gray scale. Two yellows — Racing Yellow (`{colors.yellow-racing}`) and the deeper Modena Yellow (`{colors.yellow-modena}`) — exist in the token system as heritage accents for special contexts, honoring Ferrari's racing provenance. The restraint means that when red does appear, it carries the weight of the entire brand.

Typography relies on FerrariSans — a proprietary sans-serif family with medium-weight headings (500–700) and compact proportions. Display text runs at 24–26px for section titles, while the UI chrome lives at 12–16px in weights ranging from regular to bold. A secondary "Body-Font" custom typeface handles captions and utility text, rendered in uppercase with wide letter-spacing (1px) to create a label-like editorial quality. This two-font system gives the site a print-magazine hierarchy. No text decoration is gratuitous. Letter-spacing is tight for headlines and deliberately expanded for labels, creating a visual rhythm that alternates between urgency and composure.

**Key Characteristics:**
- Chiaroscuro layout alternating between deep black sections and clean white editorial panels
- Ferrari Red (`{colors.primary}`) used with extreme sparseness — accent, not atmosphere
- Prancing Horse emblem as isolated hero element on a void-black field
- FerrariSans proprietary typeface with compact proportions and medium weights
- Photo-journalism imagery: concept renders, driver portraits, lineup parades — each section is a story
- Uppercase Body-Font labels with wide letter-spacing (1px) for editorial annotation
- Nearly zero border-radius (`{rounded.sharp}` default) reflecting precision engineering
- Dual-framework architecture (PrimeReact + Element Plus) powering 32+ interactive components
- Carousel-driven hero with editorial slides and arrow/dot navigation

## Colors

### Primary
- **Ferrari Red** (`{colors.primary}`): The iconic Rosso Corsa — primary accent and CTA color. Used for the Subscribe button, key action triggers, and brand moments where maximum visual authority is needed. The single most important color in the system.
- **Pure White** (`{colors.background}`): Primary surface for editorial content panels, navigation text on dark backgrounds, and button fills.

### Secondary & Accent
- **Dark Red** (`{colors.primary-hover}`): Deeper variant of Ferrari Red for hover/pressed states.
- **Deep Red** (`{colors.primary-active}`): The most saturated dark red — used for active states.
- **Racing Yellow** (`{colors.yellow-racing}`): Heritage accent from Ferrari's racing livery — reserved for special highlights.
- **Modena Yellow** (`{colors.yellow-modena}`): Slightly warmer and more golden — used for secondary heritage accents.

### Surface & Background
- **Absolute Black** (`{colors.surface-dark}`): Hero sections, cinematic backgrounds.
- **Dark Surface** (`{colors.surface-mid-dark}`): Secondary dark surface for footer regions, newsletter sections.
- **Light Gray Surface** (`{colors.surface-light}`): Subtle alternate surface for dividers.
- **Overlay Dark** (`{colors.overlay-dark}`): Near-black for modal overlays and image caption backgrounds.

### Neutrals & Text
- **Near Black** (`{colors.ink}`): Primary body text color on light surfaces.
- **Dark Gray** (`{colors.text-secondary}`): Secondary text and subdued UI labels.
- **Mid Gray** (`{colors.text-muted}`): Tertiary text for metadata, timestamps.
- **Silver Gray** (`{colors.text-placeholder}`): Placeholder text and disabled state indicators.

### Semantic & Accent
- **Warning Red** (`{colors.warning}`): Accessible warning state — brighter and more orange-shifted than Ferrari Red.
- **Success Green** (`{colors.success}`): Confirmation and positive status indicators.
- **Info Blue** (`{colors.info}`): Informational callouts, tooltips, and neutral status messaging.
- **Link Hover Blue** (`{colors.link-hover}`): Interactive hover state for text links.

### Gradient System
- No explicit gradients in the token system
- Depth is achieved through photography and the binary contrast between black and white surfaces
- The overlay (`{colors.overlay-dark}`) creates depth through transparency layering over imagery
- Occasional photographic gradients (light falloff in studio shots) provide atmospheric depth

## Typography

### Font Family
- **FerrariSans**: Primary typeface for headings, navigation, buttons, and editorial content. Fallbacks: Arial, Helvetica, sans-serif.
- **Body-Font**: Secondary typeface for captions, labels, and utility text. Frequently rendered in uppercase with expanded letter-spacing (1px).
- **Arial / Helvetica**: System fallback fonts used in cookie consent modals and form elements.

### Hierarchy

| Token | Use |
|---|---|
| `section-title` | 26px FerrariSans 500 — primary editorial headings |
| `card-heading` | 24px FerrariSans 400 — content card titles |
| `subheading` | 18px FerrariSans 700 — bold subsection labels |
| `ui-heading` | 16px FerrariSans 500 — component headings, nav |
| `body-bold` | 16px FerrariSans 700 — emphasized inline text |
| `button` | 16px FerrariSans 400 with 1.28px tracking |
| `small-button` | 14.4px FerrariSans 700 — compact CTAs |
| `nav-link` | 13px FerrariSans 600 — navigation/footer |
| `caption` | 13px FerrariSans 400 — metadata |
| `micro-button` | 12px FerrariSans 700 with 0.96px tracking |
| `label-upper` | 12px Body-Font uppercase 1px tracking |
| `micro-label` | 11px Body-Font uppercase smallest annotation |

### Principles
- **Proprietary identity**: FerrariSans is exclusive to Ferrari — it cannot be substituted without losing brand recognition.
- **Two-register system**: FerrariSans handles narrative voice (headings, content, buttons) while Body-Font handles structural annotation (labels, tags, micro-captions).
- **Uppercase as emphasis tool**: Body-Font captions use `text-transform: uppercase` with expanded letter-spacing (1px).
- **Compact line-heights**: Headlines use tight line-heights (1.00–1.30) creating dense, impactful text blocks.
- **Weight range 400–700**: Four weights active in the system (400, 500, 600, 700). 500 is the default "voice."

## Layout

### Spacing System
Base unit is **8px**. Scale lives in YAML; observed values include 1, 2, 4, 5, 6, 9, 10, 12, 13, 15, 16, 19, 20, 25px. Button padding is 12px vertical, 10px horizontal — compact and precise.

### Grid & Container
- Max width: 1920px (largest breakpoint) with content constraining at narrower widths
- Hero: Full-bleed on black, content centered
- Editorial sections: 2-column layouts with image + text, alternating sides
- Vehicle lineup: Horizontal scroll/carousel, 5–6 models visible at desktop width
- Footer: 4-column grid for link categories

### Whitespace Philosophy
Ferrari treats white space as a gallery wall. Each section — whether a concept car render on black void or a pair of F1 drivers on neutral gray — is given its own "room" of breathing space. The alternating black/white sections create a pacing rhythm: dark = immersive moment, white = editorial content, dark = immersive moment. This cadence makes scrolling feel like turning pages in a luxury publication.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Level 0 (Flat) | No shadow, no border | Default state for all content sections and cards |
| Level 1 (Subtle) | 1px soft shadow `{colors.shadow-soft}` | Rare — cookie consent dialogs and dropdown menus |
| Level 2 (Overlay) | `{colors.overlay-dark}` backdrop | Modal overlays and image caption backgrounds |
| Level 3 (Border) | 1px solid `{colors.border}` | Input fields, form containers — depth through delineation |

### Shadow Philosophy
Ferrari's approach to elevation is nearly flat. The single shadow token is extremely subtle — a 1-pixel whisper used only in utilitarian contexts like consent dialogs. The site communicates hierarchy through three strategies:
1. **Surface color contrast**: Black sections vs. white sections create unmistakable layering
2. **Overlay transparency**: The overlay color creates depth without shadow
3. **Photographic depth**: Studio-lit car imagery with reflections, ground shadows, and atmospheric haze

### Decorative Depth
- No UI gradients, no glows, no blur effects on interface elements
- The Prancing Horse logo on black creates a "floating in void" effect through pure contrast
- Dark-to-light section transitions are hard cuts, not gradient blends — reinforcing the editorial page-turn metaphor

## Shapes

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Editorial cards — no rounding |
| `micro` | 1px | Subtle softening on small inline elements |
| `sharp` | 2px | Default for buttons, inputs — barely perceptible, razor-precision |
| `modal` | 8px | Modal dialogs and overlay containers |
| `pill` | 9999px | Circular elements: carousel dots, avatar thumbnails, slider handles |

## Components

The complete component spec lives in YAML.

### Buttons
Ferrari's buttons are minimal white rectangles with near-zero radius — the CTA philosophy is "architecture, not decoration."

- **`button-primary`** — White on black border, the default action. Hover transitions to teal.
- **`button-subscribe`** — Ferrari Red, the high-emphasis action. The only button using brand red.
- **`button-ghost`** — Transparent on dark backgrounds with white border, for actions overlaid on cinematic imagery.
- **`button-small`** — Compact action button with `small-button` typography.

### Cards
- **`card-editorial`** — White-bg content card. Image above, heading + caption below. No border, no shadow, no border-radius.
- **`card-cinematic`** — Black-bg full-bleed hero with text overlay.

### Inputs
- **`input-newsletter`** — Transparent on dark surface (footer), 1px border, white text, sharp 2px radius.

### Modal
- **`modal`** — Cookie consent / overlay dialog with `{rounded.modal}` (8px) radius and subtle shadow.

### Navigation
- **`nav-bar`** — Black-bg header with FerrariSans 13px 600 white links.

### Links
- **`link`** / **`link-hover`** — Inline text link, hover shifts to `{colors.link-hover}`.

## Do's and Don'ts

### Do
- Use Ferrari Red (`{colors.primary}`) sparingly — only for primary CTAs and brand-critical moments
- Alternate between black cinematic sections and white editorial sections to create the signature chiaroscuro rhythm
- Use FerrariSans at weight 500 as the default heading voice
- Apply Body-Font in uppercase with 1px letter-spacing for all labels, category tags, and structural annotations
- Keep border-radius at `{rounded.sharp}` (2px) for all interactive elements — razor precision
- Let photography carry the emotional weight — every image should be art-directed studio quality
- Use the Prancing Horse emblem as a standalone hero element on black
- Maintain the 12px/10px button padding ratio — compact, purposeful
- Use `{colors.ink}` (Near Black) for body text instead of pure black — the subtle warmth improves readability
- Reserve the yellow accents strictly for motorsport and racing heritage contexts

### Don't
- Scatter Ferrari Red across the interface as decoration — it's a CTA signal, not a theme color
- Use rounded-pill buttons or large border-radii — the 2px precision is non-negotiable
- Add box-shadows to cards or content containers — depth comes from surface color contrast
- Mix FerrariSans and Body-Font within the same text block
- Use colorful backgrounds (blue, green, etc.) for sections — the palette is exclusively black/white/gray with red and yellow accents
- Apply text transforms to FerrariSans headings — uppercase is reserved for Body-Font labels
- Display low-quality or user-generated imagery
- Use the Link Hover Blue for anything other than interactive hover states
- Create busy layouts with multiple competing focal points
- Override the semantic color system with brand colors — `{colors.warning}` is deliberately different from `{colors.primary}`

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|---|---|---|
| Mobile Small | ≤375px | Single-column, minimal padding (12px), stacked navigation, hero text scales to ~18px, full-width CTAs |
| Mobile | 376–600px | Single-column, slightly larger padding (16px), hamburger nav, body text at 13px |
| Tablet Small | 601–768px | 2-column editorial grid begins, hero images maintain full-width, footer switches to 2-column |
| Tablet | 769–960px | Full 2-column layout, carousel shows 3 vehicles, padding increases to 20px |
| Desktop | 961–1280px | Full navigation, 2-column editorial with larger imagery, vehicle lineup shows 5 models |
| Large Desktop | 1281–1920px | Maximum content width, generous whitespace, hero photography at full cinematic scale |

### Touch Targets
- Primary CTA buttons: minimum 44px height with 12px vertical padding (meets WCAG AAA 44×44px target)
- Navigation links: 13px text with 1.50 line-height and adequate spacing between items
- Carousel arrows: 44px+ touch targets at viewport edges
- Footer links: grouped with sufficient vertical spacing (16–20px) for touch accuracy

### Collapsing Strategy
- **Navigation**: Full horizontal nav collapses to centered Prancing Horse logo + hamburger menu on mobile
- **Editorial sections**: 2-column image+text layouts collapse to single-column with image stacking above text
- **Vehicle lineup**: Horizontal carousel maintains scroll behavior but reduces visible models from 5 to 2–3
- **Footer**: 4-column link grid collapses to 2-column on tablet, single-column accordion on mobile
- **Hero carousel**: Full-width at all breakpoints, dot indicators and arrows scale proportionally
- **Spacing reduction**: Section padding reduces from 40–80px (desktop) to 20–40px (mobile), maintaining proportional breathing room

### Image Behavior
- Hero images: full-bleed at all breakpoints, using `object-fit: cover` to maintain cinematic composition
- Editorial images: responsive within their containers, maintaining aspect ratio
- Vehicle lineup: thumbnail size scales but maintains consistent car-to-frame proportions
- Art direction: mobile crops may tighten on vehicle subjects, reducing environmental context
- Lazy loading: PrimeReact handles progressive image loading for below-fold content

---

## Agent Prompt Guide

### Quick Color Reference
- Primary CTA: "Ferrari Red (`{colors.primary}`)"
- Background Light: "Pure White (`{colors.background}`)"
- Background Dark: "Absolute Black (`{colors.surface-dark}`)"
- Secondary Dark Surface: "Dark Surface (`{colors.surface-mid-dark}`)"
- Heading text (light bg): "Near Black (`{colors.ink}`)"
- Body text: "Dark Gray (`{colors.text-secondary}`)"
- Tertiary text: "Mid Gray (`{colors.text-muted}`)"
- Border: "Border Gray (`{colors.border}`)"
- Button Hover: "Teal (`{colors.hover-teal}`)"
- Link Hover: "Link Blue (`{colors.link-hover}`)"

### Example Component Prompts
- "Create a hero section on Absolute Black (`{colors.surface-dark}`) background with a centered logo emblem at the top, generous vertical spacing (80px+), and a single editorial headline in FerrariSans at 26px weight 500 in white, with a small Body-Font uppercase caption (12px, 1px letter-spacing) in Silver Gray (`{colors.text-placeholder}`) below"
- "Design a Subscribe section on Dark Surface (`{colors.surface-mid-dark}`) with a left-aligned headline in white FerrariSans (24px/500), a subtitle in Mid Gray (`{colors.text-muted}`, 13px), an email input with transparent background and 1px `{colors.border}` border, and a Ferrari Red (`{colors.primary}`) Subscribe button with white text, `{rounded.sharp}` radius, and 12px 10px padding"
- "Build an editorial card on white background with a full-width image (16:9 ratio) above, a FerrariSans heading (16px/700, Near Black `{colors.ink}`) below, and a Body-Font uppercase label (11px, 1px letter-spacing, Mid Gray `{colors.text-muted}`) as the category tag — no border, no shadow, no border-radius"
- "Create a vehicle lineup carousel showing 5 car thumbnails in a horizontal scroll on white background, with left/right arrow navigation, dot indicators below, and a FerrariSans model name (16px/500) beneath each vehicle"
- "Design a dark cinematic section with full-bleed studio photography of a concept car on Absolute Black, a white FerrariSans headline (26px/500) positioned in the lower-left with generous padding (40px), and a Ghost Button (transparent bg, 1px white border, white text, `{rounded.sharp}`) as the CTA"

### Iteration Guide
When refining existing screens generated with this design system:
1. Focus on ONE component at a time — Ferrari's editorial rhythm means each section is a self-contained vignette
2. Reference specific color names and hex codes from this document — the palette is small but each color has a precise role
3. Use natural language descriptions, not CSS values — "razor-sharp 2px corners" conveys intent better than "border-radius: 2px"
4. Describe the desired "feel" alongside specific measurements — "editorial magazine page-turn between sections"
5. Always maintain the chiaroscuro contrast — if a section feels flat, check whether it needs to be on black or white to maintain the alternating rhythm
6. Reserve Ferrari Red for ONE element per screen — if red appears in more than one place, it loses its authority
