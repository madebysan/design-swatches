# DESIGN.md Template — Google Format

This is the exact structure to follow when generating a DESIGN.md file. It follows Google's official `design.md` spec ([github.com/google-labs-code/design.md](https://github.com/google-labs-code/design.md)) — a two-layer architecture:

- **YAML front matter** between `---` delimiters: machine-readable design tokens
- **Markdown body**: prose rationale referencing those tokens via `{path.notation}`

> *Tokens give agents exact values. Prose tells them why those values exist.*

The output **must pass** `npx @google/design.md lint` with 0 errors before saving. Warnings are acceptable.

---

## Document Structure

```markdown
---
version: alpha
name: {Brand Name}
description: {one-sentence design system summary}

colors:
  # All values must be opaque 6-digit hex. NO rgba(), NO 8-digit hex.
  # Convert transparency to opaque approximations and add a comment.

  # Surface / canvas
  background: "#hex"
  surface: "#hex"

  # Text / ink
  ink: "#hex"
  on-background: "#hex"
  on-surface: "#hex"

  # Brand accent
  primary: "#hex"
  on-primary: "#hex"
  primary-container: "#hex"   # tinted variant if present

  # State / interaction (flatten any rgba to opaque)
  text-hover: "#hex"   # was rgba(...) — Google format requires hex
  focus-tint: "#hex"
  focus-ring: "#hex"

  # Semantic (only if the brand actually has these)
  success: "#hex"
  warning: "#hex"
  error: "#hex"
  info: "#hex"

  # Borders
  border: "#hex"

  # Shadow tints (used by elevation table)
  shadow-soft: "#hex"

typography:
  # Required keys per token: fontFamily, fontSize, fontWeight, lineHeight, letterSpacing
  # Optional: fontFeature, fontVariation
  display-hero:
    fontFamily: "{font-name}, fallback, sans-serif"
    fontSize: 96px
    fontWeight: 400
    lineHeight: 1.0
    letterSpacing: -0.5px
  display:
    fontFamily: "..."
    fontSize: 48px
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: -0.5px
  heading-section:
    ...
  heading-sub:
    ...
  body-large:
    ...
  body:
    ...
  nav-link:
    ...
  button-ui:
    ...
  caption:
    ...
  # 8-13 tokens typical. Match what the brand actually uses.

spacing:
  # Brand-appropriate scale. Match the brand's actual usage.
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  2xl: 48px
  3xl: 64px

rounded:
  # Only declare what the brand uses. Some brands have only `none` and `pill`.
  none: 0px
  sm: 4px
  md: 8px
  lg: 16px
  pill: 9999px

components:
  # Each component variant is its own entry.
  # Hover/focus/active states get -hover / -focus / -active suffixes.
  # Reference base tokens via {path.x}, never hardcode color hexes inside components.

  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.md}"
    padding: 12px 24px
  button-primary-hover:
    backgroundColor: "..."

  button-secondary:
    ...

  card:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.lg}"
    padding: 24px

  input:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.body}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
  input-focus:
    backgroundColor: "..."

  badge:
    backgroundColor: "{colors.primary-container}"
    textColor: "{colors.on-primary}"
    typography: "{typography.button-ui}"
    rounded: "{rounded.pill}"
    padding: 4px 10px
---

# {Brand Name} Design System

## Overview

{2-3 paragraphs of evocative, design-critic-quality narrative. This was the original "Visual Theme & Atmosphere" section in the prior corpus format. Reference colors via `{colors.x}` tokens.

Cover:
- The dominant canvas color and brand accent strategy
- The typography choice and what it communicates (warm? precise? luxurious? playful?)
- The signature visual element (shadows? gradients? photography? dark mode? rounded shapes?)
- The overall impression — what experience/emotion does the design create?}

**Key Characteristics:**
- {8-12 bullet points, each a specific design decision}
- Reference tokens by path: `{colors.primary}`, `{typography.display-hero}`, etc.
- Example: "FK Grotesk at weight 300 for all display text — confident lightness over bold reassurance"

## Colors

### Primary
- **{Color Name}** (`{colors.background}`): {Role and usage description}
- **{Color Name}** (`{colors.ink}`): {Role and usage description}

### Brand Accent
- **{Color Name}** (`{colors.primary}`): {Where this is applied — CTAs, focus states, etc.}

### Text States
{Group remaining colors by role: hover, focus, semantic, borders, shadow tints}

{Group colors by role, not by hue. Reference the YAML token via `{colors.x}` syntax.
Note any rgba/transparency that was flattened — the YAML inline comments record the original.}

## Typography

### Font Family
- **Primary**: `{font-name}`, with fallbacks: `{full fallback stack}`
- **Monospace** (if present): `{mono-font}`, with fallbacks
- **OpenType Features**: {List font-feature-settings discovered, explain each}

### Hierarchy

The complete type scale is declared in the `typography:` token block above. Use those tokens directly via reference (`{typography.display-hero}`, `{typography.body}`) rather than restating values.

| Token | Use |
|---|---|
| `display-hero` | {context} |
| `display` | {context} |
| `heading-section` | {context} |
| ... | ... |

### Principles
- {3-5 bullet points explaining the typography philosophy}

## Layout

### Spacing System
The complete spacing scale is in the `spacing:` token block above. Base unit: {value}px.

{1-2 sentences on the spacing personality — generous? tight? what role does whitespace play?}

### Grid & Container
- Max content width: {value}px
- {Grid column structure}
- {Notable layout patterns}

### Whitespace Philosophy
- {2-3 bullet points describing the spacing personality}

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat (Level 0) | {shadow value or "No shadow"} | {usage} |
| Subtle (Level 1) | `{shadow value}` | {usage} |
| Card (Level 2) | `{shadow value}` | {usage} |
| Elevated (Level 3) | `{shadow value}` | {usage} |
| Dialog (Level 4+) | `{shadow value}` | {usage} |
| Focus Ring | `{focus ring treatment}` | {usage} |

**Shadow Philosophy**: {1 paragraph explaining the shadow approach. Is it flat? Multi-layered? Brand-tinted? What makes it distinctive?}

## Shapes

The complete radius scale is in the `rounded:` token block above. The system uses:

| Token | Value | Use |
|---|---|---|
| `none` | 0px | {usage} |
| `sm` | {Npx} | {usage} |
| `md` | {Npx} | {usage} |
| `lg` | {Npx} | {usage} |
| `pill` | 9999px | {usage} |

{1-2 sentences on the radius philosophy. Many systems are binary (none + pill); others have 4-5 tiers.}

## Components

The complete component spec lives in the `components:` token block above. Reference component tokens directly (`{components.button-primary}`, `{components.card}`) rather than reconstructing them.

### Button variants

- **`button-primary`** — {visual + use description}
- **`button-secondary`** — {...}
- **`button-ghost`** — {...}

### Cards
{Brief description per variant, full specs in YAML.}

### Inputs
{Brief description, focus state behavior.}

### Badges / Tags
{Brief description.}

### Navigation
{Layout + sticky behavior.}

## Do's and Don'ts

### Do
- {6-10 specific, actionable guidelines with token references where possible}
- Example: "Use `{colors.primary}` only for primary CTAs and focus states — preserve its stamp quality"

### Don't
- {6-10 specific anti-patterns}
- Example: "Don't introduce mid-range border-radius (4–16px) — the system is binary (`{rounded.none}` or `{rounded.pill}`)"

{These must be specific to THIS design system, not generic design advice.}

---

## Responsive Behavior

*(Preserved from the original corpus's 9-section format — Google's parser keeps unknown sections.)*

### Breakpoints
| Name | Width | Key Changes |
|---|---|---|
| Mobile Small | <{value}px | {changes} |
| Mobile | {range}px | {changes} |
| Tablet | {range}px | {changes} |
| Desktop | {range}px | {changes} |
| Large Desktop | >{value}px | {changes} |

### Touch Targets
- {How touch targets are handled}

### Collapsing Strategy
- {How the layout adapts: grid, navigation, hero size, spacing}

### Image Behavior
- {How images adapt}

---

## Agent Prompt Guide

*(Preserved from the original corpus's 9-section format — the copy-paste payload section.)*

### Quick Color Reference
- Background: `{colors.background}`
- Text: `{colors.ink}`
- Brand accent: `{colors.primary}`
- Secondary text: `{colors.on-surface}` (or token name)
- Border: `{colors.border}`
- CTA: `{colors.primary}`

### Example Component Prompts

- "{Copy-paste-ready prompt for creating a hero section with all CSS values via token references}"
- "{Copy-paste-ready prompt for creating a card}"
- "{Copy-paste-ready prompt for creating a button}"
- "{Copy-paste-ready prompt for creating navigation}"
- "{Copy-paste-ready prompt for creating a badge/tag}"

{Each prompt should reference YAML tokens explicitly. An agent should be able to build the component from the prompt + YAML tokens alone.}

### Iteration Guide

1. {Start with... — the foundation/canvas. Reference `{colors.background}`.}
2. {Brand accent usage rule}
3. {Typography weight/tracking rules}
4. {Shadow/elevation formula}
5. {Color hierarchy}
6. {Border radius range}
7. {Any signature element}
```

---

## Quality Checklist

Before finalizing, verify:

### YAML front matter
- [ ] `version: alpha` is set
- [ ] `name` and `description` are filled
- [ ] All colors use opaque 6-digit hex (no `rgba()`, no 8-digit hex, no `oklab()`)
- [ ] Any flattened transparency has an inline `# was rgba(...) — Google format requires hex` comment
- [ ] All `typography.*` entries have fontFamily, fontSize, fontWeight, lineHeight, letterSpacing
- [ ] Component entries reference base tokens via `{path.x}` — no raw hex inside `components`
- [ ] Hover/focus/active states are separate component entries with `-hover` / `-focus` / `-active` suffix
- [ ] Padding values include units (`12px 24px` not `12 24` or `0`)

### Markdown body
- [ ] Section order: Overview → Colors → Typography → Layout → Elevation & Depth → Shapes → Components → Do's and Don'ts → Responsive Behavior → Agent Prompt Guide
- [ ] Original "Visual Theme & Atmosphere" prose preserved as Overview body
- [ ] Responsive Behavior preserved verbatim as a non-canonical section
- [ ] Agent Prompt Guide preserved verbatim as a non-canonical section
- [ ] Color references use `{colors.x}` token notation throughout

### Lint validation
- [ ] `npx @google/design.md lint <file>` returns 0 errors (warnings OK)
- [ ] No `broken-ref` errors — every `{path.x}` resolves to a declared token
- [ ] No `section-order` warnings — canonical sections in canonical order

### Quality
- [ ] Overview reads like a design review, not a spec sheet
- [ ] Agent Prompt Guide has 5+ copy-paste-ready component prompts
- [ ] Do's and Don'ts are specific to this system (no generic "maintain consistency")
- [ ] CSS custom property names included where the source site exposes them
