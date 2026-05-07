---
version: alpha
name: Polaris
description: Shopify's commerce-first design system — quiet white chrome, warm-near-black ink, Inter weight 450 body, Shopify dark green for brand moments, and circular avatars dominating the surface.

colors:
  # Surfaces
  background: "#ffffff"
  surface: "#ffffff"
  surface-secondary: "#f6f6f7"
  surface-tertiary: "#f1f1f1"
  bg-fill: "#303030"  # strong buttons, selected states

  # Ink
  ink: "#1c1e1e"
  ink-inverted: "#ffffff"
  text-secondary: "#616161"
  text-subdued: "#767676"
  text-disabled: "#b3b3b3"

  # Brand
  primary: "#004c3f"  # Shopify green
  primary-hover: "#003d33"
  primary-subtle: "#f1f8f4"
  on-primary: "#ffffff"

  # Status
  success: "#008060"
  success-bg: "#dff8eb"
  warning: "#b98900"
  critical: "#d72c0d"
  info: "#156be8"

  # Borders
  border: "#e1e3e5"
  border-strong: "#ccc4c4"
  border-subdued: "#f0f0f0"

  # Shadow tints (flattened approximations)
  shadow-soft: "#ededed"  # was rgba(0,0,0,0.075) — flattened approx
  shadow-medium: "#e6e6e6"  # was rgba(0,0,0,0.1) — flattened approx
  shadow-strong: "#d9d9d9"  # was rgba(0,0,0,0.15) — flattened approx
  shadow-modal: "#bfbfbf"  # was rgba(0,0,0,0.25) — flattened approx
  table-row-line: "#e9e9e9"

typography:
  display-hero:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 58.448px
    fontWeight: 700
    lineHeight: 1.05
    letterSpacing: -2.63px
  display-large:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 28.832px
    fontWeight: 700
    lineHeight: 1.15
    letterSpacing: 0px
  h1:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 22.784px
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: -0.342px
  h2:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 22.784px
    fontWeight: 450
    lineHeight: 1.25
    letterSpacing: -0.57px
  body-large:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 20.256px
    fontWeight: 450
    lineHeight: 1.4
    letterSpacing: 0px
  body:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 450
    lineHeight: 1.5
    letterSpacing: 0px
  label:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 600
    lineHeight: 1.43
    letterSpacing: 0px
  caption:
    fontFamily: "Shopify Sans, Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 10px
    fontWeight: 450
    lineHeight: 1.5
    letterSpacing: 0px
  button:
    fontFamily: "Inter, ui-sans-serif, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 600
    lineHeight: 1.2
    letterSpacing: 0px

spacing:
  hairline: 0.4px
  micro: 2px
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
  2xl: 32px
  3xl: 48px
  4xl: 64px

rounded:
  none: 0px
  sm: 4px
  md: 6px
  lg: 8px
  xl: 12px
  2xl: 16px
  3xl: 30px
  pill: 9999px

components:
  # Primary admin button
  button-primary:
    backgroundColor: "{colors.bg-fill}"
    textColor: "{colors.ink-inverted}"
    typography: "{typography.label}"
    rounded: "{rounded.lg}"
    padding: 8px 16px
  button-primary-hover:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.ink-inverted}"

  # Shopify brand CTA (marketing)
  button-brand:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.label}"
    rounded: "{rounded.lg}"
    padding: 8px 16px
  button-brand-hover:
    backgroundColor: "{colors.primary-hover}"
    textColor: "{colors.on-primary}"

  # Default outline button
  button-default:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    rounded: "{rounded.lg}"
    padding: 8px 16px

  # Plain transparent button
  button-plain:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.bg-fill}"
    typography: "{typography.label}"
    rounded: "{rounded.lg}"
    padding: 8px 16px

  # Card
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.xl}"
    padding: 24px

  # Input
  input:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.lg}"
    padding: 8px 12px

  # Modal
  modal:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.2xl}"
    padding: 32px

  # Avatar — Polaris signature
  avatar:
    backgroundColor: "{colors.surface-secondary}"
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    rounded: "{rounded.pill}"
    padding: 0px

  # Status badge — Fulfilled (green)
  badge-fulfilled:
    backgroundColor: "{colors.success-bg}"
    textColor: "{colors.success}"
    typography: "{typography.caption}"
    rounded: "{rounded.md}"
    padding: 2px 10px

  # Status badge — Critical
  badge-critical:
    backgroundColor: "{colors.surface-secondary}"
    textColor: "{colors.critical}"
    typography: "{typography.caption}"
    rounded: "{rounded.md}"
    padding: 2px 10px
---

# Polaris Design System

## Overview

Polaris is Shopify's design system — the chrome that merchants use to run businesses. The homepage is sparse: white canvas (`{colors.background}`), a specific warm near-black (`{colors.ink}`), a muted gray (`{colors.text-subdued}`), and the Shopify-signature dark green (`{colors.primary}`) appearing in the brand moments. This is commerce design: quiet chrome, no decorative color, all attention routed to the merchant's content — products, orders, customers, reports.

Typography pairs **Inter** (for scannable SaaS body and UI text) with **Shopify Sans** (the brand typeface for marketing moments). Inter runs at weight 700 with `-2.63px` letter-spacing at 58px display — one of the tightest tracking values in mainstream UI. Weight 450 (an unusual custom value) handles body text at `-0.5696px` tracking. The pairing keeps Polaris grounded (Inter for app UI) while preserving a distinct brand voice on marketing (Shopify Sans).

The defining attribute is Polaris's **avatars-as-pills** pattern: 50+ instances of full-pill radius — meaning circular avatars dominate the homepage. Combined with `8px` radii on buttons and cards, the system creates a soft-but-structured aesthetic that serves e-commerce perfectly: merchant faces and product photos appear as circles, while actionable chrome stays `8px` rounded.

**Key Characteristics:**
- Pure white canvas with warm near-black text (`{colors.ink}`) — not pure black
- Shopify green (`{colors.primary}`) as the brand moment color — reserved, commercial
- Inter for app UI (weight 700, 450, 600) with tight `-2.63px` tracking
- Shopify Sans for marketing hero treatments
- `8px` dominant radius on buttons/cards, full-pill on avatars (50+ uses)
- Very subtle shadows: inset top highlight as a signature
- Merchant-first design — everything routes attention to products/data
- Open-source Polaris React + Figma kit; Shopify Admin itself is proprietary

## Colors

### Base
- **Bg Surface** (`{colors.surface}`): Canvas, card backgrounds.
- **Bg Surface Secondary** (`{colors.surface-secondary}`): Subtle muted surface.
- **Bg Surface Tertiary** (`{colors.surface-tertiary}`): Even more subtle.
- **Bg Fill** (`{colors.bg-fill}`): Strong buttons, selected states.

### Text
- **Text** (`{colors.ink}`): Primary text — most-used color in the system.
- **Text Secondary** (`{colors.text-secondary}`): Body, paragraph text.
- **Text Subdued** (`{colors.text-subdued}`): Muted text, captions.
- **Text Disabled** (`{colors.text-disabled}`): Disabled labels.
- **Text Inverse** (`{colors.ink-inverted}`): Text on dark fills.

### Border
- **Border** (`{colors.border}`): Default border color.
- **Border Strong** (`{colors.border-strong}`): Emphasized border.
- **Border Subdued** (`{colors.border-subdued}`): Very subtle divider.

### Semantic (Commerce-Aware)
- **Success** (`{colors.success}`): Positive state — orders paid, products in stock.
- **Success BG** (`{colors.success-bg}`): Success surface.
- **Warning** (`{colors.warning}`): Amber caution state.
- **Critical** (`{colors.critical}`): Destructive, errors, unpaid orders.
- **Info** (`{colors.info}`): Informational links and callouts.

### Brand
- **Brand Dark** (`{colors.primary}`): Shopify green — brand moments, dark hero sections.
- **Brand Hover** (`{colors.primary-hover}`): Darker variant for hovered brand elements.
- **Brand Subtle** (`{colors.primary-subtle}`): Very light green tint for brand-themed surfaces.

## Typography

### Font Family
- **UI**: `Inter`, `ui-sans-serif, system-ui, sans-serif` fallback
- **Marketing Display**: `Shopify Sans` — custom brand typeface
- The app (Shopify Admin) uses Inter exclusively; marketing pages use Shopify Sans

### Hierarchy

The complete type scale lives in the `typography:` token block above. Reference tokens directly.

| Token | Use |
|---|---|
| `display-hero` | Marketing hero (58px Inter 700 with -2.63px tracking) |
| `display-large` | Secondary display (28px Inter 700) |
| `h1` | Page-level Inter 700 heading |
| `h2` | Sub-section Inter 450 heading |
| `body-large` | Lead paragraphs |
| `body` | Standard reading text — Inter weight 450 (the Polaris signature) |
| `label` | UI labels, button text |
| `caption` | Small Shopify Sans metadata |
| `button` | Larger marketing button labels |

### Principles
- **Weight 450 is Polaris-specific**: Inter's variable-font axis allows weight 450 — slightly heavier than regular but lighter than medium. This is the Polaris body weight.
- **Tight tracking at display**: `-2.63px` at 58px is aggressive — among the tightest in mainstream UI.
- **Inter + Shopify Sans pairing**: App chrome in Inter, brand moments in Shopify Sans. Never mix within a section.

## Layout

### Spacing System
The complete spacing scale lives in the `spacing:` token block above. Base unit is 4px with hairline (0.4px) reserved for fine table dividers.

### Grid & Container
- Admin layout: 240px left nav + content column with 24px page padding
- Marketing: 12-column with 24px gutters, max 1280px
- Cards align to an 8px micro-grid

### Whitespace Philosophy
Polaris admin chrome is quiet by design — spacing creates clear separation between data clusters but never feels luxurious. Mid-density layouts let merchants see more orders/products on screen. Marketing pages relax this with more generous vertical rhythm.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat | None | Cards default |
| Inset 1 | `0 -2px 0 0 inset {colors.shadow-soft}` | Subtle top-highlight on cards |
| Inset 2 | `0 1px 0 0 inset {colors.table-row-line}` | Table row separator |
| Level 1 | `0 1px 3px {colors.shadow-medium}` | Popover, dropdown |
| Level 2 | `0 4px 12px {colors.shadow-strong}` | Card hover, notification toast |
| Level 3 | `0 10px 50px {colors.shadow-modal}` | Modal |

**Shadow Philosophy**: Polaris's most distinctive elevation is the **inset top highlight** — a subtle upper inner-shadow that makes cards look like they have a slight physical bevel. Combined with the modal's white inset border, Polaris creates a soft, tactile, commerce-ready surface quality.

## Shapes

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Edge-to-edge sections |
| `sm` | 4px | Input chrome |
| `md` | 6px | Badges (not pill) |
| `lg` | 8px | Buttons, inputs — the workhorse |
| `xl` | 12px | Cards |
| `2xl` | 16px | Modals |
| `3xl` | 30px | Nav items in hero (unusual) |
| `pill` | 9999px | Avatars (the dominant pattern), tags, filters |

Polaris's signature is the avatar-as-pill — circular avatars appear 50+ times on the homepage alone, while actionable chrome stays `8px` rounded.

## Components

The complete component spec lives in the `components:` token block above. Reference component tokens directly.

### Buttons
- **`button-primary`** — Dark fill (`{colors.bg-fill}`), white text, 8px radius. The default admin button.
- **`button-brand`** — Shopify green (`{colors.primary}`) for marketing CTAs.
- **`button-default`** — White bg with `{colors.border}` border for secondary actions.
- **`button-plain`** — Transparent for inline link-style actions, underline on hover.

### Cards
- **`card`** — White surface, `{colors.border}` border, 12px radius, with inset top-highlight at rest.

### Inputs
- **`input`** — White surface, `{colors.border}` border, 8px radius, 8x12px padding. Focus brings 2px solid `{colors.primary}` ring.

### Modal
- **`modal`** — White surface, 16px radius, 32px padding, with deep modal-grade shadow.

### Avatars (Signature)
- **`avatar`** — Full-pill (circular) with `{colors.surface-secondary}` background and centered initials in Inter weight 600.

### Badges
- **`badge-fulfilled`** — Green success badge (`{colors.success-bg}` / `{colors.success}`).
- **`badge-critical`** — Critical state badge for errors and unpaid orders.

## Do's and Don'ts

### Do
- Use semantic Polaris tokens — never hex
- Apply 8px radius to buttons/inputs, 12px to cards, full-pill to avatars
- Use Inter weight 450 for body — the Polaris weight
- Use the inset top-highlight shadow for cards
- Route decorative color away from chrome — let products/images be the color
- Use `{colors.primary}` Shopify green only for brand moments, not for admin CTAs

### Don't
- Don't use bright brand colors in admin chrome — merchants focus on their products
- Don't use pill radius on cards — stays 8-12px
- Don't use Shopify Sans in the admin app — Inter only
- Don't use drop shadows on static cards — the inset highlight is the elevation
- Don't skip the Polaris token layer — Shopify's design team reviews token changes formally

---

## Responsive Behavior

*(Preserved from original 9-section format — Google's parser keeps unknown sections.)*

### Breakpoints
| Name | Width | Changes |
|------|-------|---------|
| Mobile | `<490px` | Single column, bottom tab nav |
| sm | `490-768px` | Tablet, compact sidebar |
| md | `768-1040px` | Full sidebar + content |
| lg | `1040-1440px` | Multi-panel admin |
| xl | `>1440px` | Max content width applied |

### Touch Targets
- Buttons: `40px` minimum
- Avatar tap targets: `44px` minimum (slightly larger than the 40px avatar itself)

### Collapsing Strategy
- Display: 58px → 32px → 24px across breakpoints
- Admin sidebar: visible → collapsible → bottom tabs
- Data tables: horizontal scroll with sticky first column
- Product cards: 4-col → 2-col → stacked

---

## Agent Prompt Guide

*(Preserved from original 9-section format — the copy-paste payload section.)*

### Quick Color Reference
- Text: `{colors.ink}`
- Text Secondary: `{colors.text-secondary}`
- Text Subdued: `{colors.text-subdued}`
- Border: `{colors.border}`
- Background: `{colors.background}`
- Surface Secondary: `{colors.surface-secondary}`
- Brand Green: `{colors.primary}`
- Success: `{colors.success}`
- Critical: `{colors.critical}`

### Example Component Prompts
- "Create an admin button: `{colors.bg-fill}` bg, white text, 8px radius, 8px 16px padding, 14px Inter weight 600. Hover: `{colors.ink}` bg. Focus: 2px solid `{colors.primary}` ring."
- "Design an order card: white bg, 1px solid `{colors.border}`, 12px radius, 24px padding, inset shadow `0 -2px 0 0 inset {colors.shadow-soft}`. Title 20px Inter weight 700 color `{colors.ink}`. Status badge: 6px radius, 2px 10px padding, bg `{colors.success-bg}` text `{colors.success}` (Fulfilled)."
- "Build a merchant avatar: 40px × 40px, full-pill (circle), bg `{colors.surface-secondary}` with initials centered in Inter weight 600 color `{colors.ink}`. Online indicator: 8px green dot bottom-right with 2px white border."

### Iteration Guide
1. Admin chrome is quiet — `{colors.ink}` text on white, `{colors.border}` borders, no decoration
2. Inter weight 450 for body is the Polaris weight — unusual, specific
3. Avatars are full-pill (circular) — 50+ on the homepage alone
4. Use inset top-highlight shadow for cards, not drop shadows
5. Green (`{colors.primary}`) is for brand moments only — not admin CTAs
6. Polaris serves merchants — everything routes attention to products, orders, customers
