---
version: alpha
name: Cohere
description: Polished enterprise command deck — bright white canvas, signature 22px card radius, dual custom typeface (CohereText serif display + Unica77 sans), cool gray containment, deep purple hero bands, and ghost-to-blue interactive states.

colors:
  # Primary canvas + ink
  background: "#ffffff"
  surface: "#ffffff"
  surface-snow: "#fafafa"
  surface-subtle: "#f2f2f2"
  ink: "#000000"                 # Cohere Black
  ink-near: "#212121"             # Near Black
  ink-deep-dark: "#17171c"        # Deep Dark
  ink-inverted: "#ffffff"

  # Brand accent — interactive blue
  primary: "#1863dc"             # Interaction Blue
  primary-ring: "#4c6ee6"
  focus-purple: "#9b60aa"

  # Purple hero band
  purple-hero: "#3d1a78"         # representative deep purple for hero band

  # Text
  on-background: "#000000"
  on-surface: "#000000"
  on-primary: "#ffffff"
  text-muted: "#93939f"           # Muted Slate

  # Borders
  border: "#d9d9dd"               # Border Cool
  border-light: "#e5e7eb"         # Border Light

  # Error focus shadow
  focus-error: "#b30000"

typography:
  display-hero:
    fontFamily: "CohereText, Space Grotesk, Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 72px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: -1.44px
  display-secondary:
    fontFamily: "CohereText, Space Grotesk, Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 60px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: -1.2px
  section-heading:
    fontFamily: "Unica77 Cohere Web, Inter, Arial, ui-sans-serif, sans-serif"
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.20
    letterSpacing: -0.48px
  sub-heading:
    fontFamily: "Unica77 Cohere Web, Inter, Arial, ui-sans-serif, sans-serif"
    fontSize: 32px
    fontWeight: 400
    lineHeight: 1.20
    letterSpacing: -0.32px
  feature-title:
    fontFamily: "Unica77 Cohere Web, Inter, Arial, ui-sans-serif, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.30
    letterSpacing: 0px
  body-large:
    fontFamily: "Unica77 Cohere Web, Inter, Arial, ui-sans-serif, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.40
    letterSpacing: 0px
  body:
    fontFamily: "Unica77 Cohere Web, Inter, Arial, ui-sans-serif, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.50
    letterSpacing: 0px
  button-medium:
    fontFamily: "Unica77 Cohere Web, Inter, Arial, ui-sans-serif, sans-serif"
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.71
    letterSpacing: 0px
  caption:
    fontFamily: "Unica77 Cohere Web, Inter, Arial, ui-sans-serif, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.40
    letterSpacing: 0px
  uppercase-label:
    fontFamily: "CohereMono, Arial, ui-sans-serif, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.40
    letterSpacing: 0.28px
  small:
    fontFamily: "Unica77 Cohere Web, Inter, Arial, ui-sans-serif, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.40
    letterSpacing: 0px
  code-micro:
    fontFamily: "CohereMono, Arial, ui-sans-serif, sans-serif"
    fontSize: 8px
    fontWeight: 400
    lineHeight: 1.40
    letterSpacing: 0.16px

spacing:
  micro: 2px
  2xs: 6px
  xs: 8px
  sm: 12px
  md: 16px
  lg: 22px
  xl: 24px
  2xl: 32px
  3xl: 56px
  4xl: 60px

rounded:
  sm: 4px
  md: 8px
  lg: 16px
  xl: 20px
  signature: 22px
  pill: 9999px

components:
  # Top navigation
  nav-bar:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    padding: 16px 24px
  nav-link:
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    padding: 8px 12px

  # Ghost / transparent — primary button style
  button-ghost:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.pill}"
    padding: 8px 16px
  button-ghost-hover:
    backgroundColor: "{colors.background}"
    textColor: "{colors.primary}"

  # Dark solid CTA
  button-dark:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.on-primary}"
    typography: "{typography.body}"
    rounded: "{rounded.pill}"
    padding: 8px 16px

  # Outlined
  button-outlined:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.pill}"
    padding: 8px 16px

  # Signature 22px card
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.signature}"
    padding: 24px
  card-emphasized:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.signature}"
    padding: 32px

  # Snow surface card
  card-snow:
    backgroundColor: "{colors.surface-snow}"
    textColor: "{colors.ink}"
    rounded: "{rounded.signature}"
    padding: 24px

  # Dialog
  dialog:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: 24px

  # Purple hero band
  section-purple:
    backgroundColor: "{colors.purple-hero}"
    textColor: "{colors.ink-inverted}"
    typography: "{typography.display-secondary}"
    rounded: "{rounded.signature}"
    padding: 60px

  # Form input
  input:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.md}"
    padding: 8px 12px
  input-focus:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
---

# Cohere Design System

## Overview

Cohere's interface is a polished enterprise command deck — confident, clean, and designed to make AI feel like serious infrastructure rather than a consumer toy. The experience lives on a bright white canvas where content is organized into generously rounded cards (22px radius) that create an organic, cloud-like containment language. This is a site that speaks to CTOs and enterprise architects: professional without being cold, sophisticated without being intimidating.

The design language bridges two worlds with a dual-typeface system: CohereText, a custom display serif with tight tracking, gives headlines the gravitas of a technology manifesto, while Unica77 Cohere Web handles all body and UI text with geometric Swiss precision. This serif/sans pairing creates a "confident authority meets engineering clarity" personality that perfectly reflects an enterprise AI platform.

Color is used with extreme restraint — the interface is almost entirely black-and-white with cool gray borders (`{colors.border}`, `{colors.border-light}`). Purple-violet appears only in photographic hero bands, gradient sections, and the interactive blue (`{colors.primary}`) that signals hover and focus states. This chromatic restraint means that when color DOES appear — in product screenshots, enterprise photography, and the deep purple section — it carries maximum visual weight.

**Key Characteristics:**
- Bright white canvas with cool gray containment borders
- 22px signature border-radius — the distinctive "Cohere card" roundness
- Dual custom typeface: CohereText (display serif) + Unica77 (body sans)
- Enterprise-grade chromatic restraint: black, white, cool grays, minimal purple-blue accent
- Deep purple/violet hero sections providing dramatic contrast
- Ghost/transparent buttons that shift to blue on hover
- Enterprise photography showing diverse real-world applications
- CohereMono for code and technical labels with uppercase transforms

## Colors

### Primary
- **Cohere Black** (`{colors.ink}`): Primary headline text and maximum-emphasis elements.
- **Near Black** (`{colors.ink-near}`): Standard body link color.
- **Deep Dark** (`{colors.ink-deep-dark}`): A blue-tinted near-black for navigation and dark-section text.

### Secondary & Accent
- **Interaction Blue** (`{colors.primary}`): The primary interactive accent — appears on button hover, focus states, and active links.
- **Ring Blue** (`{colors.primary-ring}`): Tailwind ring color for keyboard focus.
- **Focus Purple** (`{colors.focus-purple}`): Input focus border color — a muted violet.

### Surface & Background
- **Pure White** (`{colors.surface}`): Primary page background and card surface.
- **Snow** (`{colors.surface-snow}`): Subtle elevated surfaces and light-section backgrounds.
- **Lightest Gray** (`{colors.surface-subtle}`): Card borders and softest containment lines.

### Text & Borders
- **Muted Slate** (`{colors.text-muted}`): De-emphasized footer links and tertiary text — a cool-toned gray with slight blue-violet tint.
- **Border Cool** (`{colors.border}`): Standard section and list-item borders.
- **Border Light** (`{colors.border-light}`): Lighter border variant — Tailwind's standard gray-200.

### Gradient System
- **Purple-Violet Hero Band**: Deep purple gradient sections (`{colors.purple-hero}`) creating dramatic contrast against the white canvas. Full-width bands housing product screenshots and key messaging.
- **Dark Footer Gradient**: Page transitions through deep purple/charcoal to the black footer, creating a "dusk" effect.

## Typography

### Font Families
- **Display**: `CohereText`, fallbacks `Space Grotesk, Inter, ui-sans-serif, system-ui`
- **Body / UI**: `Unica77 Cohere Web`, fallbacks `Inter, Arial, ui-sans-serif, system-ui`
- **Code**: `CohereMono`, fallbacks `Arial, ui-sans-serif, system-ui`

The complete type scale lives in the `typography:` token block above.

| Token | Use |
|---|---|
| `display-hero` | 72px CohereText hero — serif authority |
| `display-secondary` | 60px secondary display |
| `section-heading` | 48px feature section title |
| `sub-heading` | 32px card heading, feature name |
| `feature-title` | 24px smaller section title |
| `body-large` | 18px intro paragraph |
| `body` | 16px standard body, button text |
| `button-medium` | 14px medium button label |
| `caption` | 14px metadata |
| `uppercase-label` | 14px CohereMono uppercase with 0.28px tracking |
| `small` | 12px smallest text, footer |
| `code-micro` | 8px tiny uppercase code label |

### Principles
- **Serif for declaration, sans for utility**: CohereText carries the brand voice at display scale; Unica77 handles everything functional.
- **Negative tracking at scale**: CohereText uses -1.2px to -1.44px letter-spacing at 60–72px.
- **Single body weight**: Nearly all Unica77 usage is weight 400. Weight 500 only for small button emphasis.
- **Uppercase code labels**: CohereMono uppercase with positive letter-spacing for technical tags.

## Layout

### Spacing System
The complete spacing scale lives in the `spacing:` token block above. Base unit is 8px. Section vertical spacing is generous (`{spacing.3xl}`–`{spacing.4xl}`).

### Grid & Container
- Max container width: up to 2560px (very wide) with responsive scaling
- Hero: centered with dramatic typography
- Feature sections: multi-column card grids
- Enterprise sections: full-width purple bands
- 26 breakpoints detected — extremely granular responsive system

### Whitespace Philosophy
- **Enterprise clarity**: Each section presents one clear proposition with breathing room.
- **Photography as hero**: Large photographic sections provide visual interest without decoration.
- **Card grouping**: Related content grouped into 22px-rounded cards.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat (Level 0) | No shadow, no border | Page background, text blocks |
| Bordered (Level 1) | 1px solid `{colors.border-light}` or `{colors.border}` | Standard cards, list separators |
| Purple Band (Level 2) | Full-width dark purple background `{colors.purple-hero}` | Hero sections, feature showcases |

**Shadow Philosophy**: Cohere is nearly shadow-free. Depth is communicated through **background color contrast** (white cards on purple bands, white surface on snow), **border containment** (cool gray borders), and the dramatic **light-to-dark section alternation**. When elements need elevation, they achieve it through being white-on-dark rather than through shadow casting.

## Shapes

| Token | Value | Use |
|---|---|---|
| `sm` | 4px | Navigation elements, small tags, pagination |
| `md` | 8px | Dialog boxes, secondary containers |
| `lg` | 16px | Featured containers, medium cards |
| `xl` | 20px | Large feature cards |
| `signature` | 22px | Primary cards, hero images, main containers — THE Cohere radius |
| `pill` | 9999px | Buttons, tags, status indicators |

## Components

The complete component spec lives in the `components:` token block above.

### Buttons
- **`button-ghost`** — Transparent, near-black text. Primary button style — invisible until interacted with. Hover: text shifts to Interaction Blue.
- **`button-dark`** — Dark/black, white text. CTA on light surfaces.
- **`button-outlined`** — Border-based containment for secondary actions.

### Cards & Containers
- **`card`** — 22px signature radius — the visual signature.
- **`card-emphasized`** — Same radius, larger padding for emphasized cards.
- **`card-snow`** — Snow surface variant for subtle elevation.
- **`dialog`** — 8px radius for modal/dialog boxes.

### Inputs
- **`input`** — Black on white. Focus border: Focus Purple `{colors.focus-purple}` with 1px solid. Focus outline: Interaction Blue.

### Navigation
- Clean horizontal nav. Cohere wordmark, dark text at 16px Unica77, dark solid CTA.

### Distinctive Components

**22px Card System**: Visual signature. All primary cards, images, and containers use this radius. Cloud-like, organic softness.

**Enterprise Trust Bar**: Company logos in a horizontal strip, monochrome treatment.

**Purple Hero Bands**: Full-width deep purple sections (`{components.section-purple}`) housing product showcases.

**Uppercase Code Tags**: CohereMono in uppercase with letter-spacing for section markers.

## Do's and Don'ts

### Do
- Use 22px border-radius on all primary cards — visual signature
- Use CohereText for display headings (72px, 60px) with negative letter-spacing
- Use Unica77 for all body and UI text at weight 400
- Keep the palette black-and-white with cool gray borders
- Use Interaction Blue (`{colors.primary}`) only for hover/focus interactive states
- Use deep purple sections for dramatic visual breaks
- Apply uppercase + letter-spacing on CohereMono for section labels
- Maintain enterprise-appropriate photography

### Don't
- Don't use border-radius other than 22px on primary cards
- Don't introduce warm colors — palette is strictly cool-toned
- Don't use heavy shadows — depth comes from color contrast and borders
- Don't use bold (700+) weight on body text — 400–500 is the range
- Don't skip the serif/sans hierarchy
- Don't use purple as a surface color for cards — purple is reserved for full-width sections
- Don't reduce section spacing below 40px
- Don't use decoration on buttons by default — ghost/transparent is the base state

---

## Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|---|---|---|
| Small Mobile | <425px | Compact layout, minimal spacing |
| Mobile | 425–640px | Single column, stacked cards |
| Large Mobile | 640–768px | Minor spacing adjustments |
| Tablet | 768–1024px | 2-column grids begin |
| Desktop | 1024–1440px | Full multi-column layout |
| Large Desktop | 1440–2560px | Maximum container width |

*26 breakpoints detected — one of the most granularly responsive sites in the dataset.*

### Touch Targets
- Buttons adequately sized for touch
- Navigation links with comfortable spacing
- Card surfaces as touch targets

### Collapsing Strategy
- **Navigation**: full nav → hamburger
- **Feature grids**: multi-column → 2-column → single
- **Hero text**: 72px → 48px → 32px progressive scaling
- **Purple sections**: maintain full-width, content stacks
- **Card grids**: 3 → 2 → 1 column

### Image Behavior
- Photography scales proportionally within 22px-radius containers
- Product screenshots maintain aspect ratio
- Purple sections scale proportionally

---

## Agent Prompt Guide

### Quick Color Reference
- Primary Text: Cohere Black `{colors.ink}`
- Page Background: Pure White `{colors.background}`
- Secondary Text: Near Black `{colors.ink-near}`
- Hover Accent: Interaction Blue `{colors.primary}`
- Muted Text: Muted Slate `{colors.text-muted}`
- Card Borders: Lightest Gray `{colors.surface-subtle}`
- Section Borders: Border Cool `{colors.border}`

### Example Component Prompts
- "Create a hero section on Pure White (`{colors.background}`) with CohereText at 72px weight 400, line-height 1.0, letter-spacing -1.44px. Cohere Black text. Subtitle in Unica77 at 18px weight 400, line-height 1.4."
- "Design a feature card with 22px border-radius, 1px solid Lightest Gray (`{colors.surface-subtle}`) border on white. Title in Unica77 at 32px, letter-spacing -0.32px. Body in Unica77 at 16px, Muted Slate (`{colors.text-muted}`)."
- "Build a ghost button: transparent background, Cohere Black text in Unica77 at 16px. On hover, text shifts to Interaction Blue (`{colors.primary}`) with 0.8 opacity. Focus: 2px solid Interaction Blue outline."
- "Create a deep purple full-width section with white text. CohereText at 60px for the heading. Product screenshot floats within using 22px border-radius."
- "Design a section label using CohereMono at 14px, uppercase, letter-spacing 0.28px. Muted Slate (`{colors.text-muted}`) text."

### Iteration Guide
1. Focus on ONE component at a time
2. Always use 22px radius for primary cards — "the Cohere card roundness"
3. Specify the typeface — CohereText for headlines, Unica77 for body, CohereMono for labels
4. Interactive elements use Interaction Blue (`{colors.primary}`) on hover only
5. Keep surfaces white with cool gray borders — no warm tones
6. Purple is for full-width sections, never card backgrounds
