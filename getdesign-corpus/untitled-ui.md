# Design System Inspired by Untitled UI

## 1. Visual Theme & Atmosphere

Untitled UI is the most-purchased Figma kit on the planet. The homepage is a showcase of the SaaS aesthetic perfected — clean white canvas (`#ffffff`), near-black headings (`#181d27`), a rich purple brand scale (`#6941c6` → `#9e77ed` → `#7f56d9`), and the polished, competent look that has become the baseline for every B2B SaaS landing page since 2021. This is the kit that defined "shipped SaaS" — Jordan Hughes distilled the industry-standard aesthetic into 10,000+ Figma frames.

Typography is **Inter** — the SaaS typeface — with weight 600 at 48px display and `-0.96px` letter-spacing. Inter appears at every size, in every weight from 400 to 700. The choice is anti-signature: Untitled UI wants to look universally polished, not distinctively different. That's the entire value proposition — buy the kit, ship product that looks like it was designed by a ten-person team.

The distinctive attribute is Untitled UI's **radius scale**: `1px`, `4px`, `5px`, `6px`, `7px`, `8px`, `10px` — 1-pixel granularity at the small end. Combined with `4,515` occurrences of the gray-500 color (`#525252`), the kit reads as meticulously calibrated. Every component has been drawn at multiple radii, every radius maps to a component class. The scan found 124 elements at `6px` radius — mostly badges and image frames — and 111 elements at `8px` — mostly buttons.

**Key Characteristics:**
- Inter typeface at weight 600 for display, weight 400 for body — universal SaaS
- Purple brand scale (100-900) with `#7f56d9` as the primary CTA
- `1-pixel radius granularity` (1, 2, 4, 5, 6, 7, 8, 10px) — precisely calibrated
- Shadows use SaaS-standard `0 1px 2px rgba(16,24,40,...)` values
- Gray scale from `#fafafa` to `#0a0a0a` with `#525252` as the dominant chrome
- 10,000+ Figma components — the kit's differentiator is coverage, not novelty
- Separate React component library that mirrors the Figma exactly

## 2. Color Palette & Roles

### Brand Purple Scale
- **Brand 50** (`#f4ebff`): Very subtle purple tint.
- **Brand 100** (`#e9d7fe`): Muted purple surface — `--brand200`.
- **Brand 200** (`#d6bbfb`): Light purple — `--brand300`.
- **Brand 300** (`#b692f6`): Mid-light — `--brand400`.
- **Brand 400** (`#9e77ed`): Brand accent — `--brand500`.
- **Brand 500** (`#7f56d9`): Primary CTA background. Default brand anchor.
- **Brand 600** (`#6941c6`): Hover/pressed state — appears 243 times on homepage.
- **Brand 700** (`#53389e`): Deep brand — `--brand800`.
- **Brand 800** (`#42307d`): Brand dark — `--brand900`.
- **Brand 900** (`#2e2458`): Maximum depth.

### Gray Scale
- **Gray 25** (`#fafafa`): Page background variant.
- **Gray 50** (`#f9fafb`): Subtle surface.
- **Gray 100** (`#f2f4f7`): Muted surface.
- **Gray 200** (`#e4e7ec`): Border default.
- **Gray 300** (`#d0d5dd`): Strong border.
- **Gray 400** (`#98a2b3`): Placeholder.
- **Gray 500** (`#525252`): Secondary text — 4,515 occurrences (the most-used color).
- **Gray 600** (`#475467`): Strong secondary.
- **Gray 700** (`#344054`): Label text.
- **Gray 800** (`#1d2939`): Near-black heading.
- **Gray 900** (`#181d27`): Primary heading.

### Semantic Colors
- **Success** (`#12b76a`): Success green.
- **Success 50** (`#ecfdf3`): Success surface.
- **Warning** (`#f79009`): Warning amber.
- **Error** (`#d92d20`): Error red.
- **Error 50** (`#fef3f2`): Error surface.

## 3. Typography Rules

### Font Family
- **Primary**: `Inter`, fallback: `ui-sans-serif, system-ui, -apple-system, sans-serif`
- **Monospace**: `ui-monospace, SFMono-Regular, Menlo, monospace`
- Untitled UI uses Inter exclusively — no custom typefaces, no alternates.

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display 2xl | Inter | 72px | 600 | 1.10 | -1.44px |
| Display xl | Inter | 60px | 600 | 1.10 | -1.2px |
| Display lg | Inter | 48px | 600 | 1.15 | -0.96px |
| Display md | Inter | 44px | 600 | 1.20 | -0.88px |
| Display sm | Inter | 34px | 600 | 1.24 | -0.68px |
| Display xs | Inter | 24px | 600 | 1.33 | normal |
| Text xl | Inter | 20px | 500 | 1.50 | normal |
| Text lg | Inter | 18px | 500 | 1.56 | normal |
| Text md | Inter | 16px | 400 | 1.50 | normal |
| Text sm | Inter | 14px | 500 | 1.43 | normal |
| Text xs | Inter | 12px | 500 | 1.50 | normal |

### Principles
- **Weight 600 across all display sizes**: Untitled UI's signature weight for hero and headlines.
- **Weight 500 for UI labels, 400 for body**: Standard two-weight UI typography.
- **Progressive letter-spacing**: `-1.44px` at 72px, `-0.68px` at 34px, normal below 24px.
- **Text size-t suffix (not px)**: Figma components are named `Text md`, `Display lg` — Tailwind-friendly.

## 4. Component Stylings

### Buttons
- **Primary**: `#7f56d9` bg, white text, `8px` radius, `8px 14px` padding, 14px Inter weight 600.
- **Secondary Color**: `#f9f5ff` bg (brand-50), `#7f56d9` text, `1px solid transparent`.
- **Secondary Gray**: `#ffffff` bg, `1px solid #d0d5dd`, `#344054` text.
- **Tertiary Color**: transparent bg, `#7f56d9` text, no border.
- **Tertiary Gray**: transparent, `#475467` text, no border.
- **Link Color**: `#7f56d9`, no padding, underline on hover.
- Size variants: xs (28px), sm (32px), md (40px), lg (44px), xl (48px), 2xl (60px).

### Cards
- `#ffffff` bg, `1px solid #e4e7ec`, `12px` radius, `24px` padding.
- Shadow: `0 1px 2px rgba(16,24,40,0.06), 0 1px 3px rgba(16,24,40,0.1)`.

### Inputs
- `#ffffff` bg, `1px solid #d0d5dd`, `8px` radius, `10px 14px` padding.
- Focus: `1px solid #7f56d9`, `0 0 0 4px rgba(127,86,217,0.18)` ring — the thick 4px ring is distinctive.
- Error: `1px solid #d92d20`, `0 0 0 4px rgba(217,45,32,0.18)`.

### Badges
- **Radius variants**: `4px` (square), `6px` (subtle rounding), `16px` (pill).
- Sizes: sm (22px height), md (26px), lg (30px).
- Color variants: gray, brand, error, warning, success, blue-light, blue, indigo, purple, pink, rose, orange.

### Dropdowns / Menus
- `#ffffff` bg, `1px solid #e4e7ec`, `8px` radius, `4px` item padding.
- Shadow: `0 12px 16px -4px rgba(16,24,40,0.08), 0 4px 6px -2px rgba(16,24,40,0.03)`.

## 5. Layout Principles

### Spacing System
- Base unit: **4px** (Tailwind-aligned)
- Dominant values: `4px` (1,017 uses), `2px` (130), `8px` (145), `12px` (73), `10px` (64), `6px` (78)
- Untitled UI uses 1-pixel granularity at small sizes — unusual for a Figma kit

### Grid
- 12-column with `32px` gutters
- Max content widths: `1280px` (standard), `1440px` (wide), `1600px` (max)
- Section padding: `96px` vertical on desktop, `64px` on tablet, `48px` on mobile

### Border Radius Scale
- `1px`: Fine chrome elements (100 uses)
- `4-5px`: Small inline elements
- `6px`: Badges, small images (124 uses)
- `8px`: Buttons, inputs — the workhorse (111 uses)
- `10px`: Featured cards (57 uses)
- `12px`: Large cards, modals
- `16px`: Hero cards, callouts
- `9999px`: Avatars, switches, occasionally badges

## 6. Depth & Elevation

| Level | Treatment | Use |
|-------|-----------|-----|
| XS | `0 1px 2px rgba(16,24,40,0.06)` | Subtle card lift |
| SM | `0 1px 2px rgba(16,24,40,0.06), 0 1px 3px rgba(16,24,40,0.1)` | Card rest (default) |
| MD | `0 2px 4px -2px rgba(16,24,40,0.06), 0 4px 8px -2px rgba(16,24,40,0.1)` | Card hover, menu |
| LG | `0 4px 6px -2px rgba(16,24,40,0.03), 0 12px 16px -4px rgba(16,24,40,0.08)` | Dropdown, popover |
| XL | `0 8px 8px -4px rgba(16,24,40,0.03), 0 20px 24px -4px rgba(16,24,40,0.08)` | Modal |
| 2XL | `0 24px 48px -12px rgba(16,24,40,0.18)` | Large modal, hero images |

**Shadow Philosophy**: Untitled UI uses the SaaS-standard shadow system — dual-layer with `rgba(16,24,40,...)` (a slate-blue tinted near-black) for consistent depth across the palette. The 4px focus ring (not 2px or 3px) is a signature touch — more visible than shadcn's, less clinical than Atlassian's.

## 7. Do's and Don'ts

### Do
- Use the brand purple scale (50-900) progressively — don't pick only `#7f56d9`
- Apply `8px` radius to buttons, `12px` to cards — the Untitled UI rhythm
- Use Inter weight 600 for display, weight 500 for UI labels, weight 400 for body
- Use the 4px focus ring (`0 0 0 4px rgba(127,86,217,0.18)`) — the signature
- Pair with gray scale 50-900 — resist mixing with shadcn's neutrals
- Apply dual-layer SaaS shadows for elevation

### Don't
- Don't use pill radius on buttons — stays `8px`
- Don't use weight 700 for headings — Untitled UI is weight 600
- Don't use letter-spacing on text below 24px — tracking stays normal
- Don't substitute Inter — the kit is Inter-specific
- Don't use `#000000` for text — always gray-900 (`#181d27`)

## 8. Responsive Behavior

### Breakpoints
| Name | Width | Changes |
|------|-------|---------|
| Mobile | `<640px` | Single column, 48px section padding |
| sm | `640px+` | 2-column layouts |
| md | `768px+` | 3-column features, tablet nav |
| lg | `1024px+` | Full desktop, 12-col grid active |
| xl | `1280px+` | Max-width applied |

### Touch Targets
- Button `sm` (32px) minimum
- Button `md` (40px) default for both touch and desktop
- Icon buttons: `40px × 40px`

### Collapsing Strategy
- Display sizes: 72px → 48px → 34px across breakpoints
- Nav: horizontal → slide-over drawer on mobile
- Cards: 4-col → 2-col → single column
- Sidebars: visible → collapsible → overlay

## 9. Agent Prompt Guide

### Quick Color Reference
- Brand Primary: `#7f56d9` (brand-500)
- Brand Hover: `#6941c6` (brand-600)
- Brand Light: `#f4ebff` (brand-50)
- Background: `#ffffff`
- Surface: `#fafafa` (gray-25)
- Text: `#181d27` (gray-900), `#525252` (gray-500)
- Border: `#e4e7ec` (gray-200)

### Example Component Prompts
- "Create a hero: white bg. Headline at 60px Inter weight 600, letter-spacing -1.2px, line-height 1.10, color #181d27. Subtitle 20px weight 500 color #475467. Primary button: #7f56d9 bg, white text, 8px radius, 10px 18px padding, 14px weight 600. Secondary gray: white bg, 1px solid #d0d5dd, #344054 text, 8px radius."
- "Design a card: white bg, 1px solid #e4e7ec, 12px radius, 24px padding, box-shadow 0 1px 2px rgba(16,24,40,0.06), 0 1px 3px rgba(16,24,40,0.1). Title 20px Inter weight 600 color #181d27. Body 14px weight 400 color #475467."
- "Build an input: white bg, 1px solid #d0d5dd, 8px radius, 10px 14px padding, 14px Inter weight 400. Focus: 1px solid #7f56d9 + 0 0 0 4px rgba(127,86,217,0.18) ring. Placeholder color #98a2b3."

### Iteration Guide
1. Think in Untitled UI's gray scale — every chrome element maps to a gray 25-900 token
2. Button radius is `8px`, card radius is `12px` — the workhorse rhythm
3. Focus rings are 4px thick (not 2-3px) — makes them highly perceivable
4. Inter weight 600 at display, 500 for UI, 400 for body — the SaaS standard
5. Shadow tokens follow `rgba(16,24,40,...)` — the slate-blue-black of SaaS
6. For dark mode, invert gray scale and reduce shadow opacity by ~50%
