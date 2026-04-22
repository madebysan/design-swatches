# DESIGN.md Template

This is the exact structure to follow when generating a DESIGN.md file. Every section is required. Adapt the content depth to match what the target site actually provides — don't fabricate data, but do analyze thoroughly.

---

## Document Structure

```markdown
# Design System Inspired by {Brand Name}

## 1. Visual Theme & Atmosphere

{2-3 paragraphs of evocative, design-critic-quality narrative describing the overall visual personality. Cover:
- The dominant canvas color and brand accent strategy
- The typography choice and what it communicates (warm? precise? luxurious? playful?)
- The signature visual element (shadows? gradients? photography? dark mode? rounded shapes?)
- The overall impression — what experience/emotion does the design create?}

**Key Characteristics:**
- {8-12 bullet points, each a specific design decision with exact values}
- Example: "sohne-var with OpenType `"ss01"` on all text — a custom stylistic set that defines the brand's letterforms"
- Example: "Near-black immersive dark theme (`#121212`–`#1f1f1f`) — UI disappears behind content"

## 2. Color Palette & Roles

### Primary Brand
- **{Color Name}** (`{hex}`): {CSS variable if any}. {Role and usage description}.

### Text Scale
- **{Color Name}** (`{hex}`): {CSS variable if any}. {What text level uses this}.

### Interactive / Accent
- **{Color Name}** (`{hex}`): {CSS variable if any}. {Interactive purpose}.

### Status / Semantic
- **{Color Name}** (`{hex}`): {Role — error, success, warning, info}.

### Surface & Borders
- **{Color Name}** (`{hex}` or `rgba(...)`): {Surface, border, or divider usage}.

### Shadows
- **{Shadow Name}** (`{full rgba value}`): {What this shadow color is used for}.

{Group colors by role, not by hue. Include ALL discovered colors.
Use the site's own CSS variable names where available.}

## 3. Typography Rules

### Font Family
- **Primary**: `{font-name}`, with fallbacks: `{full fallback stack}`
- **Monospace** (if present): `{mono-font}`, with fallbacks: `{mono fallbacks}`
- **OpenType Features**: {List all font-feature-settings discovered, explain each}

### Hierarchy

| Role | Font | Size | Weight | Line Height | Letter Spacing | Notes |
|------|------|------|--------|-------------|----------------|-------|
| Display Hero | {font} | {px} ({rem}) | {weight} | {value} (description) | {value} | {context} |
| Display Large | ... | ... | ... | ... | ... | ... |
| Section Heading | ... | ... | ... | ... | ... | ... |
| Sub-heading | ... | ... | ... | ... | ... | ... |
| Body Large | ... | ... | ... | ... | ... | ... |
| Body | ... | ... | ... | ... | ... | ... |
| Button | ... | ... | ... | ... | ... | ... |
| Caption | ... | ... | ... | ... | ... | ... |
| Small / Micro | ... | ... | ... | ... | ... | ... |
| Code (if any) | ... | ... | ... | ... | ... | ... |

{Include ALL observed text styles. Minimum 10 rows for a thorough analysis.
Line heights should include both the numeric value AND a descriptor: tight, normal, relaxed.
Letter spacing should be exact px values. "normal" if 0.}

### Principles
- {3-5 bullet points explaining the typography philosophy}
- What makes this type system distinctive?
- What's the weight strategy? (light signature? bold binary? variable precision?)
- How does tracking (letter-spacing) behave at different sizes?

## 4. Component Stylings

### Buttons

**{Variant Name}** (e.g., Primary Dark, Ghost, Outlined, Pill, Circular)
- Background: `{value}`
- Text: `{value}`
- Padding: {value}
- Radius: {value}
- Border: `{value}` (if any)
- Font: {size} {font} weight {weight}
- Hover: {hover state description with values}
- Focus: {focus state if observed}
- Use: {when this variant is used}

{Document ALL button variants found. Minimum 3 variants.}

### Cards & Containers
- Background: `{value}`
- Border: `{value}`
- Radius: {value}
- Shadow: `{full box-shadow value}`
- Hover: {hover behavior}

### Inputs & Forms
- Border: `{value}`
- Radius: {value}
- Focus: {focus state}
- Label: {color}, {size} {font}
- Text: `{value}`
- Placeholder: `{value}`

### Badges / Tags / Pills
{If present on the site}

### Navigation
- {Layout description: sticky? transparent? dark/light?}
- {Logo placement}
- {Link styles: font, size, weight, color}
- {CTA placement and style}
- {Mobile behavior}

### Image Treatment
- {Border radius on images}
- {Overlay effects}
- {Aspect ratios used}
- {Carousel/gallery patterns}

## 5. Layout Principles

### Spacing System
- Base unit: {value}px
- Scale: {comma-separated list of all observed spacing values}

### Grid & Container
- Max content width: {value}px
- {Grid column structure}
- {Notable layout patterns}

### Whitespace Philosophy
- {2-3 bullet points describing the spacing personality}
- How generous is the spacing? Tight and dense? Airy and magazine-like?
- What role does whitespace play in the design?

### Border Radius Scale
- Micro ({value}px): {usage}
- Standard ({value}px): {usage}
- Card ({value}px): {usage}
- Large ({value}px): {usage}
- Pill ({value}px or 9999px): {usage}
- Circle (50%): {usage}

## 6. Depth & Elevation

| Level | Treatment | Use |
|-------|-----------|-----|
| Flat (Level 0) | {shadow value or "No shadow"} | {usage} |
| Subtle (Level 1) | `{shadow value}` | {usage} |
| Card (Level 2) | `{shadow value}` | {usage} |
| Elevated (Level 3) | `{shadow value}` | {usage} |
| Dialog (Level 4+) | `{shadow value}` | {usage} |
| Focus Ring | `{focus ring treatment}` | {usage} |

**Shadow Philosophy**: {1 paragraph explaining the shadow approach. Is it flat? Multi-layered? Brand-tinted? Heavy or subtle? What makes it distinctive?}

## 7. Do's and Don'ts

### Do
- {6-10 specific, actionable guidelines with exact values}
- Each "Do" should reference a specific design decision from the system
- Example: "Use #222222 (warm near-black) for text — never pure #000000"

### Don't
- {6-10 specific anti-patterns with values}
- Each "Don't" should prevent a specific mistake
- Example: "Don't use weight 600-700 for sohne-var headlines — weight 300 is the brand voice"

{These must be specific to THIS design system, not generic design advice.}

## 8. Responsive Behavior

### Breakpoints
| Name | Width | Key Changes |
|------|-------|-------------|
| Mobile Small | <{value}px | {changes} |
| Mobile | {range}px | {changes} |
| Tablet | {range}px | {changes} |
| Desktop | {range}px | {changes} |
| Large Desktop | >{value}px | {changes} |

### Touch Targets
- {How touch targets are handled — button padding, link spacing, tap areas}

### Collapsing Strategy
- {How the layout adapts: grid columns, navigation, hero size, spacing}
- {Each major element type: hero, navigation, cards, footer, images}

### Image Behavior
- {How images adapt: responsive sizing, quality, crop behavior}

## 9. Agent Prompt Guide

### Quick Color Reference
- Background: {Color Name} (`{hex}`)
- Text: {Color Name} (`{hex}`)
- Brand accent: {Color Name} (`{hex}`)
- Secondary text: `{hex}`
- Border: `{hex or rgba}`
- Card shadow: {full shadow value}
- CTA: {Color Name} (`{hex}`)

### Example Component Prompts
- "{Copy-paste-ready prompt for creating a hero section with ALL CSS values inline}"
- "{Copy-paste-ready prompt for creating a card with ALL CSS values inline}"
- "{Copy-paste-ready prompt for creating a button with ALL CSS values inline}"
- "{Copy-paste-ready prompt for creating navigation with ALL CSS values inline}"
- "{Copy-paste-ready prompt for creating a badge/tag with ALL CSS values inline}"

{Each prompt must include: font family, size, weight, line-height, letter-spacing, colors, padding, radius, shadow, OpenType features. An agent should be able to build the component from the prompt alone.}

### Iteration Guide
1. {Start with... — the foundation/canvas}
2. {Brand accent usage rule}
3. {Typography weight/tracking rules}
4. {Shadow/elevation formula}
5. {Color hierarchy: heading, body, label, muted}
6. {Border radius range}
7. {Any signature element: dark mode, photography, gradients, etc.}
```

---

## Quality Checklist

Before finalizing, verify:

- [ ] Every color has an exact hex/rgba value
- [ ] Every typography entry has size, weight, line-height, letter-spacing
- [ ] Every component has exact CSS values (not "rounded corners" — the actual px value)
- [ ] Shadow values are complete box-shadow syntax
- [ ] The "Visual Theme & Atmosphere" reads like a design review, not a spec sheet
- [ ] The "Agent Prompt Guide" has 5+ copy-paste-ready component prompts
- [ ] Do's and Don'ts are specific to this system (no generic "maintain consistency")
- [ ] Font family includes full fallback stack as declared in CSS
- [ ] OpenType features are documented if present
- [ ] CSS custom property names are included where available
- [ ] The document could be used by an AI agent to build a faithful UI without seeing the original site
