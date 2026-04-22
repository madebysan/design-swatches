# Design System Inspired by Tailwind Plus

## 1. Visual Theme & Atmosphere

Tailwind Plus is what Tailwind Labs themselves ship when they need component libraries. The homepage is a curated gallery of 500+ marketing components, 300+ e-commerce templates, and the Catalyst React kit — all by the same team that built Tailwind CSS. The aesthetic is the platonic ideal of Tailwind: pure white canvas (`#ffffff`), pure black text (`#000000`), Inter at weight 400 (unusual — most SaaS uses 600+) with aggressive `-4.8px` tracking at 96px display, and the IBM Plex Mono used for technical captions.

Typography's defining move is **weight 400 at 96px** with `-4.8px` letter-spacing. This is extraordinarily light for display sizes — most kits use 600-800 at that scale. It reads as editorial, book-like, sophisticated. Combined with `IBM Plex Mono` for eyebrow labels and captions (with positive letter-spacing of `+1.3-1.4px`), the system creates a type voice that feels more like The New York Times than a SaaS dashboard.

The defining structural choice is `32px` border-radius on hero sections — much larger than typical — paired with `12px` on cards and full-pill (`9999px`) on buttons. This three-tier radius (pill/medium/large) is distinctive. Shadows are almost entirely absent (41 occurrences of transparent shadow placeholders); the one active shadow is `oklab(0.13 -0.004 -0.028 / 0.08) 0px 0px 0px 1px inset` — a subtle inset hairline.

**Key Characteristics:**
- Inter (InterVariable) at weight 400 for display — editorial, not bold
- `-4.8px` letter-spacing at 96px — the most aggressive tracking in this corpus
- IBM Plex Mono for eyebrows/captions with positive tracking — technical voice
- Pure monochrome palette (black/white/slate) + single blue accent
- `32px` radius on heroes, `12px` on cards, `9999px` on buttons — three-tier
- Mostly no shadows — inset hairlines carry all elevation
- Includes Catalyst React UI kit — Tailwind's official component library
- Built, shipped, and maintained by Tailwind Labs themselves

## 2. Color Palette & Roles

### Core
- **White** (`#ffffff`): Canvas.
- **Black** (`#000000`): Primary text, primary button bg (45 occurrences).
- **Foreground** (`#0a0a0a`): Alternative near-black for text where pure black feels heavy.

### Slate Scale
- **Slate 900** (`#0f172a`): Primary text alternative — confident dark.
- **Slate 700** (`#334155`): Body emphasis.
- **Slate 500** (`#64748b`): Muted text.
- **Slate 300** (`#cbd5e1`): Disabled state.
- **Slate 200** (`#e2e8f0`): Default border.
- **Slate 100** (`#f1f5f9`): Muted surface.
- **Slate 50** (`#f8fafc`): Very subtle surface.

### Accent
- **Sky 500** (`#0ea5e9`): Primary accent — links, occasional hover states.
- **Sky 400** (`#38bdf8`): Lighter accent.

### Semantic
- **Emerald 500** (`#10b981`): Success.
- **Amber 500** (`#f59e0b`): Warning.
- **Red 500** (`#ef4444`): Error.

### CSS Variables (from scan)
- `--color-white`: `#fff`
- `--color-black`: `#000`
- Only 2 CSS variables — Tailwind Plus explicitly avoids a token system, relying on Tailwind's utility classes instead

## 3. Typography Rules

### Font Family
- **Primary**: `InterVariable`, fallback: `Inter, ui-sans-serif, system-ui, sans-serif`
- **Mono**: `IBM Plex Mono`, fallback: `ui-monospace, SFMono-Regular, Menlo, monospace`
- InterVariable is the full variable-font version of Inter, loaded once with the weight axis available 100-900

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing |
|------|------|------|--------|-------------|----------------|
| Display Huge | InterVariable | 96px | 400 | 0.95 | -4.8px |
| Display Hero | InterVariable | 60px | 400 | 1.05 | -1.5px |
| Display Light | InterVariable | 60px | 300 | 1.10 | normal |
| Display Medium | InterVariable | 60px | 500 | 1.10 | normal |
| H1 | InterVariable | 40px | 500 | 1.20 | -1px |
| H2 | InterVariable | 24px | 500 | 1.30 | -0.6px |
| Body | InterVariable | 16px | 400 | 1.60 | normal |
| Eyebrow | IBM Plex Mono | 14px | 600 | 1.43 | +1.4px |
| Mono Caption | IBM Plex Mono | 13px | 500 | 1.50 | +1.3px |
| Mono Small | IBM Plex Mono | 12px | 400 | 1.50 | +0.3px |

### Principles
- **Weight 400 at display**: Tailwind Plus's most defensible typographic choice. Editorial feel, anti-SaaS.
- **Aggressive negative tracking**: `-4.8px` at 96px is unusual — creates a dense, engineered display block.
- **Positive tracking on mono**: `+1.3-1.4px` on IBM Plex Mono eyebrows — airy, technical.
- **Mono as category voice**: Eyebrows ("INTRODUCING CATALYST") and captions render in IBM Plex Mono with uppercase + tracking — editorial branding.
- **InterVariable handles all body weight variation**: One font file, any weight 100-900 available at runtime.

## 4. Component Stylings

### Buttons
- **Primary (pill)**: `#0f172a` bg, white text, `9999px` radius (full pill), `10px 20px` padding, 14px InterVariable weight 500.
- **Secondary**: white bg, `1px solid #e2e8f0`, `#0f172a` text, `9999px` radius.
- **Ghost**: transparent bg, no border, `#334155` text, hover `#f1f5f9`.
- **Icon button**: circular (`9999px`), `40px × 40px`.

### Cards
- `#ffffff` bg, `1px solid #e2e8f0`, `12px` radius, `24-32px` padding.
- Shadow: `0 0 0 1px rgba(0,0,0,0.05) inset` — inset hairline, not drop shadow.

### Hero / Feature Sections
- `32px` radius (the largest in the system) — distinctive.
- Gradient or muted slate bg on feature callouts.

### Inputs
- `#f8fafc` bg (filled), no border at rest, `9999px` radius (pill-shaped inputs!), `10px 16px` padding.
- Focus: `2px solid #0f172a` with `3px` offset.

### Badges
- `9999px` radius (pill), `2px 12px` padding, 11px IBM Plex Mono weight 500 tracking `+0.2px`.
- Uppercase by default — editorial treatment.

### Dropdowns / Menus
- `#ffffff` bg, `1px solid #e2e8f0`, `12px` radius.
- Shadow: `0 12px 28px -8px rgba(0,0,0,0.1)`.

## 5. Layout Principles

### Spacing System
- Base unit: **4px** (Tailwind default)
- Dominant: `8px` (233 uses — very heavy), `12px` (38), `16px` (28), `24px` (8)
- `8px` dominance suggests tight UI chrome with generous section breathing

### Grid
- 12-column Tailwind
- Hero sections often full-bleed with `80-120px` vertical padding
- Marketing features: 2-3 column with `32px` gutters

### Border Radius Scale
- Sharp (`6px`): Search inputs, nav chrome (2 uses)
- Medium (`12px`): Cards, content blocks — the workhorse (74 uses)
- Large (`16px`): Testimonials, featured content
- Extra Large (`32px`): Hero sections, callouts (2 uses — reserved but impactful)
- Full (`9999px`): All buttons, inputs, chips, badges (17 uses)

## 6. Depth & Elevation

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (dominant) | None | Most static surfaces |
| Inset Hairline | `0 0 0 1px rgba(0,0,0,0.05) inset` | Card rest — subtle inner border |
| Inset Strong | `0 0 0 1px rgba(0,0,0,0.08) inset` | Hover state |
| Popover | `0 12px 28px -8px rgba(0,0,0,0.1)` | Dropdowns, menus |
| Modal | `0 24px 48px -12px rgba(0,0,0,0.18)` | Dialog, large overlay |

**Shadow Philosophy**: Tailwind Plus's most distinctive shadow treatment is the **inset hairline** — a subtle interior border via `0 0 0 1px rgba(0,0,0,0.05) inset`. This creates a "cut from the background" feel without casting a drop shadow. The 41 transparent-shadow placeholders in the scan represent components with `shadow-none` as the default. Elevation in Tailwind Plus is the absence of shadow combined with whitespace and typographic hierarchy.

## 7. Do's and Don'ts

### Do
- Use InterVariable at weight 400 for display — the editorial voice
- Apply `-4.8px` letter-spacing at 96px — the most aggressive tracking in this corpus
- Use IBM Plex Mono with positive tracking (`+1.3-1.4px`) for eyebrows and captions
- Default to `9999px` (pill) for buttons and inputs — the Tailwind Plus shape language
- Use `12px` cards, `32px` heroes — the three-tier radius
- Apply inset hairline shadows, not drop shadows
- Keep the palette monochrome + sky accent — resist adding colors

### Don't
- Don't use weight 700+ at display — Tailwind Plus is editorial, not bold
- Don't use `ui-monospace` instead of IBM Plex Mono — the branded mono is the voice
- Don't use drop shadows on static elements — inset hairlines are the elevation
- Don't use sharp (`<8px`) radii on interactive — Tailwind Plus is fully rounded
- Don't skip the positive letter-spacing on mono text — it's the editorial gesture

## 8. Responsive Behavior

### Breakpoints (Tailwind defaults)
| Name | Width | Changes |
|------|-------|---------|
| sm | `640px+` | 2-column layouts |
| md | `768px+` | 3-column features |
| lg | `1024px+` | Full desktop |
| xl | `1280px+` | Hero sections max-width |
| 2xl | `1536px+` | Max content 1440px |

### Touch Targets
- Buttons: `40-44px` minimum height via pill padding
- Icon buttons: `40px × 40px` circular

### Collapsing Strategy
- Display: 96px → 60px → 48px across breakpoints, weight 400 maintained
- Hero radius: 32px → 24px → 16px on mobile
- Marketing sections: 3-col → 2-col → stacked
- Mono captions: tracking reduces to `+0.5px` on mobile

## 9. Agent Prompt Guide

### Quick Color Reference
- Background: `#ffffff`
- Foreground: `#0a0a0a` or `#000000`
- Slate primary text: `#0f172a` (slate-900)
- Slate muted: `#64748b` (slate-500)
- Border: `#e2e8f0` (slate-200)
- Surface: `#f8fafc` (slate-50)
- Accent: `#0ea5e9` (sky-500)

### Example Component Prompts
- "Create a hero: white bg, 32px radius, 80px vertical padding. Eyebrow: 'INTRODUCING CATALYST' in IBM Plex Mono 12px weight 600 tracking +1.4px color #64748b. Headline: 96px InterVariable weight 400, letter-spacing -4.8px, line-height 0.95, color #000. Subtitle: 20px weight 400 color #334155. Pill button: #0f172a bg, white text, 9999px radius, 10px 20px padding, 14px weight 500."
- "Design a card: white bg, 12px radius, 24px padding, box-shadow 0 0 0 1px rgba(0,0,0,0.05) inset (inset hairline, no drop shadow). Title 24px InterVariable weight 500 letter-spacing -0.6px. Body 16px weight 400 line-height 1.60 color #334155. Pill badge: IBM Plex Mono 11px weight 500 tracking +0.2px uppercase."
- "Build a pill input: #f8fafc bg, no border at rest, 9999px radius, 10px 16px padding, 16px InterVariable weight 400 color #0f172a. Focus: 2px solid #0f172a ring with 3px offset."

### Iteration Guide
1. Weight 400 at display is the editorial signature — resist weight 600+
2. `-4.8px` tracking at 96px — aggressive, intentional
3. IBM Plex Mono with POSITIVE tracking for eyebrows — `+1.3-1.4px`
4. Three-tier radius: `9999px` (buttons/inputs), `12px` (cards), `32px` (heroes)
5. Inset hairlines (`0 0 0 1px inset`) replace drop shadows
6. Monochrome + one accent (sky blue) — resist adding palette
