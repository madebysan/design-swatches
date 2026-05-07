---
version: alpha
name: Ollama
description: Radical grayscale minimalism with SF Pro Rounded display, zero shadows, and a binary radius system — 12px containers or 9999px pills on every interactive element.

colors:
  # Canvas
  background: "#ffffff"
  surface: "#ffffff"
  surface-snow: "#fafafa"
  surface-dark: "#090909"

  # Ink
  ink: "#000000"
  ink-near-black: "#262626"
  ink-inverted: "#ffffff"
  text-button-dark: "#404040"
  text-mid: "#525252"
  text-secondary: "#737373"
  text-muted: "#a3a3a3"

  # Brand accent — Ollama uses no chromatic primary; surface light gray plays the role
  primary: "#e5e5e5"  # workhorse light gray neutral, doubles as primary surface
  on-primary: "#262626"

  # Borders
  border: "#e5e5e5"
  border-input: "#d4d4d4"

  # Focus
  focus-ring: "#3b82f6"  # the ONLY chromatic color — Tailwind default focus ring

typography:
  display-hero:
    fontFamily: "SF Pro Rounded, system-ui, -apple-system, sans-serif"
    fontSize: 48px
    fontWeight: 500
    lineHeight: 1.0
    letterSpacing: 0px
  section-heading:
    fontFamily: "SF Pro Rounded, system-ui, -apple-system, sans-serif"
    fontSize: 36px
    fontWeight: 500
    lineHeight: 1.11
    letterSpacing: 0px
  sub-heading:
    fontFamily: "SF Pro Rounded, system-ui, -apple-system, sans-serif"
    fontSize: 30px
    fontWeight: 500
    lineHeight: 1.2
    letterSpacing: 0px
  card-title:
    fontFamily: "ui-sans-serif, system-ui, sans-serif"
    fontSize: 24px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0px
  body-large:
    fontFamily: "ui-sans-serif, system-ui, sans-serif"
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.56
    letterSpacing: 0px
  body:
    fontFamily: "ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  body-medium:
    fontFamily: "ui-sans-serif, system-ui, sans-serif"
    fontSize: 16px
    fontWeight: 500
    lineHeight: 1.5
    letterSpacing: 0px
  caption:
    fontFamily: "ui-sans-serif, system-ui, sans-serif"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0px
  small:
    fontFamily: "ui-sans-serif, system-ui, sans-serif"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.33
    letterSpacing: 0px
  code-body:
    fontFamily: "ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace"
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: 0px
  code-caption:
    fontFamily: "ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace"
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.43
    letterSpacing: 0px
  code-small:
    fontFamily: "ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace"
    fontSize: 12px
    fontWeight: 400
    lineHeight: 1.63
    letterSpacing: 0px

spacing:
  xs: 4px
  sm: 8px
  md: 12px
  lg: 16px
  xl: 24px
  2xl: 32px
  3xl: 40px
  4xl: 48px
  5xl: 88px
  6xl: 112px

rounded:
  none: 0px
  md: 12px
  pill: 9999px

components:
  # Gray pill — primary action
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.ink-near-black}"
    typography: "{typography.body-medium}"
    rounded: "{rounded.pill}"
    padding: 10px 24px

  # White pill — secondary
  button-secondary:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.text-button-dark}"
    typography: "{typography.body-medium}"
    rounded: "{rounded.pill}"
    padding: 10px 24px

  # Black pill — max emphasis CTA
  button-cta:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.ink-inverted}"
    typography: "{typography.body-medium}"
    rounded: "{rounded.pill}"
    padding: 10px 24px

  # Card / container
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: 24px

  # Code block container
  code-block:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.code-body}"
    rounded: "{rounded.md}"
    padding: 24px

  # Input — pill-shaped
  input:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink-near-black}"
    typography: "{typography.body}"
    rounded: "{rounded.pill}"
    padding: 10px 16px

  # Tab pill
  tab-active:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.ink-near-black}"
    typography: "{typography.body-medium}"
    rounded: "{rounded.pill}"
    padding: 8px 16px
  tab-inactive:
    backgroundColor: "{colors.background}"
    textColor: "{colors.text-secondary}"
    typography: "{typography.body-medium}"
    rounded: "{rounded.pill}"
    padding: 8px 16px

  # Pill tag
  tag:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.ink-near-black}"
    typography: "{typography.code-small}"
    rounded: "{rounded.pill}"
    padding: 4px 10px
---

# Ollama Design System

## Overview

Ollama's interface is radical minimalism taken to its logical conclusion — a pure-white void where content floats without decoration, shadow, or color. The design philosophy mirrors the product itself: strip away everything unnecessary until only the essential tool remains. This is the digital equivalent of a Dieter Rams object — every pixel earns its place, and the absence of design IS the design.

The entire page exists in pure grayscale. There is zero chromatic color in the interface — no brand blue, no accent green, no semantic red. The only colors that exist are shades between pure black (`{colors.ink}`) and pure white (`{colors.background}`), creating a monochrome environment that lets the user's mental model of "open models" remain uncolored by brand opinion. The Ollama llama mascot, rendered in simple black line art, is the only illustration — and even it's monochrome.

What makes Ollama distinctive is the combination of SF Pro Rounded (Apple's rounded system font) with an exclusively pill-shaped geometry (9999px radius on everything interactive). The rounded letterforms + rounded buttons + rounded containers create a cohesive "softness language" that makes a developer CLI tool feel approachable and friendly rather than intimidating. This is minimalism with warmth — not cold Swiss-style grid minimalism, but the kind where the edges are literally softened.

**Key Characteristics:**
- Pure white canvas with zero chromatic color — completely grayscale
- SF Pro Rounded headlines creating a distinctively Apple-like softness
- Binary border-radius system: 12px (containers) or 9999px (everything interactive)
- Zero shadows — depth comes exclusively from background color shifts and borders
- Pill-shaped geometry on all interactive elements (buttons, tabs, inputs, tags)
- The Ollama llama as the sole illustration — black line art, no color
- Extreme content restraint — the homepage is short, focused, and uncluttered

## Colors

### Primary
- **Pure Black** (`{colors.ink}`): Primary headlines, primary links, and the darkest text. The only "color" that demands attention.
- **Near Black** (`{colors.ink-near-black}`): Button text on light surfaces, secondary headline weight.
- **Darkest Surface** (`{colors.surface-dark}`): The darkest possible surface — barely distinguishable from pure black, used for footer or dark containers.

### Surface & Background
- **Pure White** (`{colors.background}`): The primary page background — not off-white, not cream, pure white. Button surfaces for secondary actions.
- **Snow** (`{colors.surface-snow}`): The subtlest possible surface distinction from white — used for section backgrounds and barely-elevated containers.
- **Light Gray** (`{colors.primary}`): Button backgrounds, borders, and the primary containment color. The workhorse neutral.

### Neutrals & Text
- **Stone** (`{colors.text-secondary}`): Secondary body text, footer links, and de-emphasized content. The primary "muted" tone.
- **Mid Gray** (`{colors.text-mid}`): Emphasized secondary text, slightly darker than Stone.
- **Silver** (`{colors.text-muted}`): Tertiary text, placeholders, and deeply de-emphasized metadata.
- **Button Text Dark** (`{colors.text-button-dark}`): Specific to white-surface button text.

### Semantic & Accent
- **Ring Blue** (`{colors.focus-ring}`): The ONLY non-gray color in the entire system — Tailwind's default focus ring, used exclusively for keyboard accessibility. Never visible in normal interaction flow.
- **Border Light** (`{colors.border-input}`): A slightly darker gray for white-surface button borders.

### Gradient System
- **None.** Ollama uses absolutely no gradients. Visual separation comes from flat color blocks and single-pixel borders. This is a deliberate, almost philosophical design choice.

## Typography

### Font Family
- **Display**: `SF Pro Rounded`, with fallbacks: `system-ui, -apple-system, sans-serif`
- **Body / UI**: `ui-sans-serif`, with fallbacks: `system-ui`
- **Monospace**: `ui-monospace`, with fallbacks: `SFMono-Regular, Menlo, Monaco, Consolas, monospace`

*Note: SF Pro Rounded is Apple's system font — it renders with rounded terminals on macOS/iOS and falls back to the system sans-serif on other platforms.*

### Hierarchy

The complete type scale lives in the `typography:` token block above. Reference tokens directly.

| Token | Use |
|---|---|
| `display-hero` | Maximum impact, rounded letterforms |
| `section-heading` | Feature section titles |
| `sub-heading` | Card headings, feature names |
| `card-title` | Medium emphasis headings |
| `body-large` | Hero descriptions, button text |
| `body` | Standard body text |
| `body-medium` | Navigation, button labels |
| `caption` | Metadata, descriptions |
| `small` | Smallest sans-serif text |
| `code-body` | Inline code, commands |
| `code-caption` | Code snippets, secondary |
| `code-small` | Tags, labels |

### Principles
- **Rounded display, standard body**: SF Pro Rounded carries display headlines with its distinctive rounded terminals, while the standard system sans handles all body text. The rounded font IS the brand expression.
- **Weight restraint**: Only two weights matter — 400 (regular) for body and 500 (medium) for headings. No bold, no light, no black weight.
- **Tight display, comfortable body**: Headlines compress to 1.0 line-height, while body text relaxes to 1.43–1.56.
- **Monospace for developer identity**: Code blocks and terminal commands appear throughout as primary content.

## Layout

### Spacing System
The complete spacing scale lives in the `spacing:` token block above. Base unit is 8px with very generous section spacing (`5xl`–`6xl`).

### Grid & Container
- Max container width: approximately 1024–1280px, centered
- Hero: centered single-column with llama illustration
- Feature sections: 2-column layout (text left, code right)
- Integration grid: responsive multi-column
- Footer: clean single-row

### Whitespace Philosophy
- **Emptiness as luxury**: The page is remarkably short and sparse — no feature section overstays its welcome. Each concept gets minimal but sufficient space.
- **Content density is low by design**: Where other AI companies pack feature after feature, Ollama presents three ideas (run models, use with apps, integrations) and stops.
- **The white space IS the brand**: Pure white space with zero decoration communicates "this tool gets out of your way."

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat (Level 0) | No shadow, no border | Page background, most content |
| Bordered (Level 1) | `1px solid {colors.border}` | Cards, code blocks, buttons |

**Shadow Philosophy**: Ollama uses **zero shadows**. This is not an oversight — it's a deliberate design decision. Every other major AI product site uses at least subtle shadows. Ollama's flat, shadowless approach creates a paper-like experience where elements are distinguished purely by background color and single-pixel borders. Depth is communicated through **content hierarchy and typography weight**, not visual layering.

## Shapes

| Token | Value | Use |
|---|---|---|
| `none` | 0px | Unused — not part of Ollama's binary system |
| `md` | 12px | The sole container radius — code blocks, cards, panels |
| `pill` | 9999px | Everything interactive — buttons, tabs, inputs, tags, badges |

This binary system is extreme and distinctive. There is no 4px, no 8px, no gradient of roundness. Elements are either containers (12px) or interactive (pill).

## Components

The complete component spec lives in the `components:` token block above. Reference component tokens directly.

### Buttons
- **`button-primary`** — Light Gray pill, primary action. Always pill-shaped, understated, grayscale.
- **`button-secondary`** — White pill with `1px solid {colors.border-input}` border. Visually lighter than primary.
- **`button-cta`** — Black pill with white text. Maximum emphasis (e.g., "Create account", "Download").

### Cards & Containers
- **`card`** — White or snow surface, optional `1px solid {colors.border}` border, 12px radius. Zero shadow.
- **`code-block`** — 12px-radius container with monospace content. Bordered, no shadow.

### Inputs
- **`input`** — Pill-shaped (9999px) form field. Focus brings the `{colors.focus-ring}` ring. Placeholder uses `{colors.text-muted}`.

### Tabs & Tags
- **`tab-active`** / **`tab-inactive`** — Pill-shaped tab selectors. Active state is light gray; inactive is transparent.
- **`tag`** — Small pill-shaped tags for model browsing. Light gray background, dark text.

### Navigation
Clean horizontal nav with minimal elements. Llama icon + wordmark in black. Links at 16px weight 400. Search bar pill-shaped. Right side: text "Sign in" link + black pill "Download" CTA. No borders, no background.

## Do's and Don'ts

### Do
- Use pure white (`{colors.background}`) as the page background — never off-white or cream
- Use pill-shaped (9999px) radius on all interactive elements — buttons, tabs, inputs, tags
- Use 12px radius on all non-interactive containers — code blocks, cards, panels
- Keep the palette strictly grayscale — no chromatic colors except the blue focus ring
- Use SF Pro Rounded at weight 500 for display headings — the rounded terminals are the brand expression
- Maintain zero shadows — depth comes from borders and background shifts only
- Keep content density low — each section should present one clear idea
- Use monospace for terminal commands and code — it's primary content, not decoration
- Keep all buttons at 10px 24px padding with pill shape — consistency is absolute

### Don't
- Don't introduce any chromatic color — no brand blue, no accent green, no warm tones
- Don't use border-radius between 12px and 9999px — the system is binary
- Don't add shadows to any element — the flat aesthetic is intentional
- Don't use font weights above 500 — no bold, no black weight
- Don't add decorative illustrations beyond the llama mascot
- Don't use gradients anywhere — flat blocks and borders only
- Don't overcomplicate the layout — two columns maximum, no complex grids
- Don't use borders heavier than 1px — containment is always the lightest possible touch
- Don't add hover animations or transitions — interactions should feel instant and direct

---

## Responsive Behavior

*(Preserved from original 9-section format — Google's parser keeps unknown sections.)*

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile | <640px | Single column, stacked everything, hamburger nav |
| Small Tablet | 640–768px | Minor adjustments to spacing |
| Tablet | 768–850px | 2-column layouts begin |
| Desktop | 850–1024px | Standard layout, expanded features |
| Large Desktop | 1024–1280px | Maximum content width |

### Touch Targets
- All buttons are pill-shaped with generous padding (10px 24px)
- Navigation links at comfortable 16px size
- Minimum touch area easily exceeds 44x44px

### Collapsing Strategy
- **Navigation**: Collapses to hamburger menu on mobile
- **Feature sections**: 2-column → stacked single column
- **Hero text**: 48px → 36px → 30px progressive scaling
- **Integration grid**: Multi-column → 2-column → single column
- **Code blocks**: Horizontal scroll maintained

### Image Behavior
- Llama mascot scales proportionally
- Code blocks maintain monospace formatting
- Integration icons reflow to fewer columns
- No art direction changes

---

## Agent Prompt Guide

*(Preserved from original 9-section format — the copy-paste payload section.)*

### Quick Color Reference
- Primary Text: Pure Black (`{colors.ink}`)
- Page Background: Pure White (`{colors.background}`)
- Secondary Text: Stone (`{colors.text-secondary}`)
- Button Background: Light Gray (`{colors.primary}`)
- Borders: Light Gray (`{colors.border}`)
- Muted Text: Silver (`{colors.text-muted}`)
- Dark Text: Near Black (`{colors.ink-near-black}`)
- Subtle Surface: Snow (`{colors.surface-snow}`)

### Example Component Prompts
- "Create a hero section on pure white (`{colors.background}`) with an illustration centered above a headline at 48px SF Pro Rounded weight 500, line-height 1.0. Use Pure Black text. Below, add a black pill-shaped CTA button (9999px radius, 10px 24px padding) and a gray pill button."
- "Design a code block with a 12px border-radius, 1px solid Light Gray (`{colors.border}`) border on white background. Use ui-monospace at 16px for the terminal command. No shadow."
- "Build a tab bar with pill-shaped tabs (9999px radius). Active tab: Light Gray (`{colors.primary}`) background, Near Black (`{colors.ink-near-black}`) text. Inactive: transparent background, Stone (`{colors.text-secondary}`) text."
- "Create an integration card grid. Each card is a bordered pill (9999px radius) or a 12px-radius card with 1px solid `{colors.border}` border. Icon + name inside. Grid of 4 columns on desktop."
- "Design a navigation bar: transparent background, no border. Ollama logo on the left, 3 text links (Pure Black, 16px, weight 400), pill search input in the center, 'Sign in' text link and black pill 'Download' button on the right."

### Iteration Guide
1. Focus on ONE component at a time
2. Keep all values grayscale — `{colors.text-secondary}` not "use a light color"
3. Always specify pill (9999px) or container (12px) radius — nothing in between
4. Shadows are always zero — never add them
5. Weight is always 400 or 500 — never bold
6. If something feels too decorated, remove it — less is always more for Ollama
