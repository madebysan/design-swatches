# Design System Inspired by Polaris

## 1. Visual Theme & Atmosphere

Polaris is Shopify's design system — the chrome that merchants use to run businesses. The homepage is sparse: white canvas (`#ffffff`), a specific warm near-black (`#1c1e1e`), a muted gray (`#767676`), and the Shopify-signature dark green (`#004c3f`) appearing in the brand moments. This is commerce design: quiet chrome, no decorative color, all attention routed to the merchant's content — products, orders, customers, reports.

Typography pairs **Inter** (for scannable SaaS body and UI text) with **Shopify Sans** (the brand typeface for marketing moments). Inter runs at weight 700 with `-2.63px` letter-spacing at 58px display — one of the tightest tracking values in mainstream UI. Weight 450 (an unusual custom value) handles body text at `-0.5696px` tracking. The pairing keeps Polaris grounded (Inter for app UI) while preserving a distinct brand voice on marketing (Shopify Sans).

The defining attribute is Polaris's **avatars-as-pills** pattern: 50 out of the top radius values are `50%` — meaning circular avatars dominate the homepage. Combined with `8px` radii on buttons and cards, the system creates a soft-but-structured aesthetic that serves e-commerce perfectly: merchant faces and product photos appear as circles, while actionable chrome stays `8px` rounded.

**Key Characteristics:**
- Pure white canvas with warm near-black text (`#1c1e1e`) — not pure black
- Shopify green (`#004c3f`) as the brand moment color — reserved, commercial
- Inter for app UI (weight 700, 450, 600) with tight `-2.63px` tracking
- Shopify Sans for marketing hero treatments
- `8px` dominant radius on buttons/cards, `50%` on avatars (50+ uses)
- Very subtle shadows: `rgba(0,0,0,0.075) 0px -2px 0px 0px inset` as a signature
- Merchant-first design — everything routes attention to products/data
- Open-source Polaris React + Figma kit; Shopify Admin itself is proprietary

## 2. Color Palette & Roles

### Base
- **Bg Surface** (`#ffffff`): Canvas, card backgrounds.
- **Bg Surface Secondary** (`#f6f6f7`): Subtle muted surface.
- **Bg Surface Tertiary** (`#f1f1f1`): Even more subtle.
- **Bg Fill** (`#303030`): Strong buttons, selected states.

### Text
- **Text** (`#1c1e1e`): Primary text — 95 occurrences.
- **Text Secondary** (`#616161`): Body, paragraph text.
- **Text Subdued** (`#767676`): Muted text, captions (3 scan occurrences).
- **Text Disabled** (`#b3b3b3`): Disabled labels.
- **Text Inverse** (`#ffffff`): Text on dark fills.

### Border
- **Border** (`#e1e3e5`): Default border color.
- **Border Strong** (`#ccc4c4`): Emphasized border.
- **Border Subdued** (`#f0f0f0`): Very subtle divider.

### Semantic (Commerce-Aware)
- **Success** (`#008060`): Positive state — orders paid, products in stock.
- **Success BG** (`#dff8eb`): Success surface.
- **Warning** (`#b98900`): Amber caution state.
- **Critical** (`#d72c0d`): Destructive, errors, unpaid orders.
- **Info** (`#156be8`): Informational links and callouts.

### Brand
- **Brand Dark** (`#004c3f`): Shopify green — brand moments, dark hero sections.
- **Brand Hover** (`#003d33`): Darker variant for hovered brand elements.
- **Brand Subtle** (`#f1f8f4`): Very light green tint for brand-themed surfaces.

## 3. Typography Rules

### Font Family
- **UI**: `Inter`, `ui-sans-serif, system-ui, sans-serif` fallback
- **Marketing Display**: `Shopify Sans` — custom brand typeface
- **Mono**: `Mono Sans` (Shopify's own mono, not widely shipped)
- The app (Shopify Admin) uses Inter exclusively; marketing pages use Shopify Sans

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display Hero | Inter | 58.448px | 700 | 1.05 | -2.63px |
| Display Large | Inter | 28.832px | 700 | 1.15 | normal |
| H1 | Inter | 22.784px | 700 | 1.20 | -0.342px |
| H2 | Inter | 22.784px | 450 | 1.25 | -0.57px |
| Body Large | Inter | 20.256px | 450 | 1.40 | normal |
| Body | Inter | 16px | 450 | 1.50 | normal |
| Label | Inter | 14px | 600 | 1.43 | normal |
| Caption | Shopify Sans | 10px | 450 | 1.50 | normal |
| Button | Inter | 18px | 600 | 1.20 | normal |

### Principles
- **Weight 450 is Polaris-specific**: Inter's variable-font axis allows weight 450 — slightly heavier than regular but lighter than medium. This is the Polaris body weight.
- **Tight tracking at display**: `-2.63px` at 58px is aggressive — among the tightest in mainstream UI.
- **Inter + Shopify Sans pairing**: App chrome in Inter, brand moments in Shopify Sans. Never mix within a section.

## 4. Component Stylings

### Buttons
- **Primary**: `#303030` bg, white text, `8px` radius, `16px 32px` padding, 14px weight 400. (Polaris uses less padding on admin buttons — `5.28px 10.56px`.)
- **Shopify Brand**: `#004c3f` bg, white text, `8px` radius, for marketing CTAs.
- **Default**: white bg, `1px solid #e1e3e5`, `#1c1e1e` text, `8px` radius.
- **Plain**: transparent, no border, `#303030` text, underline hover.

### Cards
- `#ffffff` bg, `1px solid #e1e3e5`, `12px` radius, variable padding.
- Shadow (at rest): `rgba(0,0,0,0.075) 0px -2px 0px 0px inset` — a subtle top highlight instead of a drop shadow.
- Shadow (elevated): `0 1px 3px rgba(0,0,0,0.1)`.

### Inputs
- `#ffffff` bg, `1px solid #e1e3e5`, `8px` radius, `8px 12px` padding.
- Focus: `2px solid #004c3f`, no additional ring.

### Modals
- `#ffffff` bg, `16px` radius, `24-32px` padding.
- Heavy shadow: `0 10px 50px rgba(0,0,0,0.25), 0 0 0 1px rgba(255,255,255,0.25) inset`.

### Avatars
- `50%` radius (circular) — 50+ occurrences on the homepage alone
- Sizes: `20px` (micro), `32px` (small), `40px` (default), `48px` (large)
- Fallback: initials in centered Inter weight 600

### Badges
- `6px` radius (not pill), `2px 10px` padding, 12px Inter weight 500.
- Color-coded by state: Fulfilled (green), Pending (amber), Unpaid (orange), Critical (red).

## 5. Layout Principles

### Spacing System
- Base unit: **4px**
- Dominant values: `0.4px` (24 uses — hairline!), `0.528px` (24), `5.28px` (6), `8px` (7), `16px` (7)
- The sub-pixel values (`0.4px`, `0.528px`) are hairline separators — Shopify's commerce tables use extremely fine dividers

### Grid
- Admin layout: `240px` left nav + content column with `24px` page padding
- Marketing: 12-column with `24px` gutters, max `1280px`
- Cards align to a `8px` micro-grid

### Border Radius Scale
- Sharp (`4px`): Input chrome
- Standard (`8px`): Buttons, inputs, badges (13 uses) — the workhorse
- Comfortable (`10-12px`): Cards
- Large (`30px`): Nav items in hero (unusual)
- Pill (`1000px`, `9999px`): Tags, filters
- Circle (`50%`): Avatars, profile images — dominant (50 uses)

## 6. Depth & Elevation

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat | None | Cards default |
| Inset 1 | `rgba(0,0,0,0.075) 0px -2px 0px 0px inset` | Subtle top-highlight on cards |
| Inset 2 | `rgb(233,233,233) 0px 1px 0px 0px inset` | Table row separator |
| Level 1 | `0 1px 3px rgba(0,0,0,0.1)` | Popover, dropdown |
| Level 2 | `0 4px 12px rgba(0,0,0,0.15)` | Card hover, notification toast |
| Level 3 | `0 10px 50px rgba(0,0,0,0.25), 0 0 0 1px rgba(255,255,255,0.25) inset` | Modal |

**Shadow Philosophy**: Polaris's most distinctive elevation is the **inset top highlight** — `rgba(0,0,0,0.075) 0px -2px 0px 0px inset`. This isn't a drop shadow; it's a subtle upper inner-shadow that makes cards look like they have a slight physical bevel. Combined with the modal's white inset border (`rgba(255,255,255,0.25) 0px 0px 0px 1px inset`), Polaris creates a soft, tactile, commerce-ready surface quality.

## 7. Do's and Don'ts

### Do
- Use semantic Polaris tokens (`text`, `bg-surface`, `border`) — never hex
- Apply `8px` radius to buttons/inputs, `12px` to cards, `50%` to avatars
- Use Inter weight 450 for body — the Polaris weight
- Use the inset top-highlight shadow (`rgba(0,0,0,0.075) inset`) for cards
- Route decorative color away from chrome — let products/images be the color
- Use `#004c3f` green only for brand moments, not for CTAs

### Don't
- Don't use bright brand colors in admin chrome — merchants focus on their products
- Don't use pill radius on cards — stays `8-12px`
- Don't use Shopify Sans in the admin app — Inter only
- Don't use drop shadows on static cards — the inset highlight is the elevation
- Don't skip the Polaris token layer — Shopify's design team reviews token changes formally

## 8. Responsive Behavior

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

## 9. Agent Prompt Guide

### Quick Color Reference
- Text: `#1c1e1e`
- Text Secondary: `#616161`
- Text Subdued: `#767676`
- Border: `#e1e3e5`
- Background: `#ffffff`
- Surface Secondary: `#f6f6f7`
- Brand Green: `#004c3f`
- Success: `#008060`
- Critical: `#d72c0d`

### Example Component Prompts
- "Create an admin button: #303030 bg, white text, 8px radius, 8px 16px padding, 14px Inter weight 400. Hover: #1c1e1e bg. Focus: 2px solid #004c3f ring."
- "Design an order card: white bg, 1px solid #e1e3e5, 12px radius, 24px padding, inset shadow rgba(0,0,0,0.075) 0px -2px 0px 0px. Title 20px Inter weight 700 color #1c1e1e. Status badge: 6px radius, 2px 10px padding, bg #dff8eb text #005e46 (Fulfilled)."
- "Build a merchant avatar: 40px × 40px, 50% radius (circle), bg #f6f6f7 with initials centered in Inter weight 600 color #1c1e1e. Online indicator: 8px green dot bottom-right with 2px white border."

### Iteration Guide
1. Admin chrome is quiet — `#1c1e1e` text on white, `#e1e3e5` borders, no decoration
2. Inter weight 450 for body is the Polaris weight — unusual, specific
3. Avatars are `50%` (circular) — 50+ on the homepage alone
4. Use inset top-highlight shadow for cards, not drop shadows
5. Green (`#004c3f`) is for brand moments only — not admin CTAs
6. Polaris serves merchants — everything routes attention to products, orders, customers
