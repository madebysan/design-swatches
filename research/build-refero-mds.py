#!/usr/bin/env python3
"""Convert refero-styles.json (1328 entries from styles.refero.design) into:

  research/refero-data/{slug}.json   — split per-entry JSON, identical shape
  research/refero-data/{slug}.md     — thin DESIGN.md derived from refero data

Filters out any entry whose domain already exists in
explorer/shared/brand-domains.json (san already has those documented deeply).

This is a mechanical conversion — no LLM, no extra fetches. The .md files are
intentionally thin (frontmatter + tagline + colors + fonts only) and tagged
`source: refero` in frontmatter so any downstream tool can distinguish them
from the canonical 174.
"""
import json
import re
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path("/Users/san/Projects/_done/design-swatches")
SRC = ROOT / "research" / "refero-styles.json"
DEST = ROOT / "research" / "refero-data"
DEST.mkdir(parents=True, exist_ok=True)

# Domain index for filtering
domains = json.loads((ROOT / "explorer/shared/brand-domains.json").read_text())


def normalize_domain(url: str) -> str:
    try:
        d = urlparse(url).netloc.lower()
        return re.sub(r"^www\.", "", d)
    except Exception:
        return ""


sans_domains = {normalize_domain("http://" + d): slug for slug, d in domains.items()}


def slugify(name: str, url: str) -> str:
    """Make a safe filename. Prefer siteName, fall back to domain."""
    base = name.strip()
    base = re.sub(r"&", "and", base)
    base = re.sub(r"['']", "", base)
    base = re.sub(r"[^\w\s.-]", "", base)
    base = re.sub(r"\s+", "-", base).lower()
    base = re.sub(r"\.com$|\.dev$|\.io$|\.app$", "", base)
    base = re.sub(r"-+", "-", base).strip("-")
    if not base or base in {"www", "the", "an", "a"}:
        d = normalize_domain(url)
        base = d.split(".")[0] if d else "unknown"
    return base[:60]


def to_md(entry: dict, slug: str) -> str:
    domain = normalize_domain(entry.get("url", ""))
    color_scheme = entry.get("colorScheme", "")
    colors = entry.get("colors") or []
    fonts = entry.get("fonts") or []
    tagline = (entry.get("northStar") or "").strip().replace('"', "'")
    site_name = entry.get("siteName", "")
    url = entry.get("url", "")
    refero_url = f"https://styles.refero.design/style/{entry['id']}"
    primary_hex = colors[0]["hex"] if colors else None

    fonts_yaml = "[" + ", ".join(f"{f}" for f in fonts) + "]" if fonts else "[]"
    primary_line = f'primary_color: "{primary_hex}"' if primary_hex else "primary_color: null"

    lines = [
        "---",
        f"slug: {slug}",
        f"name: {site_name}",
        f"url: {url}",
        f"domain: {domain}",
        f"source: refero",
        f"refero_id: {entry['id']}",
        f"color_scheme: {color_scheme}",
        f'tagline: "{tagline}"',
        f"fonts: {fonts_yaml}",
        primary_line,
        "---",
        "",
        f"# Design Reference: {site_name}",
        "",
        f"> {tagline}" if tagline else "",
        "",
        f"_Source: [Refero Styles]({refero_url}) — thin reference, not a full DESIGN.md._",
        "",
        "## Colors",
        "",
    ]
    for c in colors:
        cname = c.get("name", "Unnamed")
        chex = c.get("hex", "")
        lines.append(f"- **{cname}** (`{chex}`)")
    lines.append("")

    if fonts:
        lines.append("## Fonts")
        lines.append("")
        for f in fonts:
            lines.append(f"- {f}")
        lines.append("")

    if entry.get("thumbnailUrl"):
        lines.append("## Preview")
        lines.append("")
        lines.append(f"![{site_name} thumbnail]({entry['thumbnailUrl']})")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main():
    raw = json.loads(SRC.read_text())
    print(f"Loaded {len(raw)} refero entries")

    new = []
    skipped_overlap = []
    used_slugs: dict[str, int] = {}

    for entry in raw:
        d = normalize_domain(entry.get("url", ""))
        if d in sans_domains:
            skipped_overlap.append((entry["siteName"], sans_domains[d]))
            continue

        base_slug = slugify(entry.get("siteName", ""), entry.get("url", ""))
        # Disambiguate collisions
        if base_slug in used_slugs:
            used_slugs[base_slug] += 1
            slug = f"{base_slug}-{used_slugs[base_slug]}"
        else:
            used_slugs[base_slug] = 1
            slug = base_slug

        # Write .json
        json_path = DEST / f"{slug}.json"
        json_path.write_text(json.dumps(entry, indent=2))

        # Write .md
        md_path = DEST / f"{slug}.md"
        md_path.write_text(to_md(entry, slug))
        new.append(slug)

    print(f"\n✓ Wrote {len(new)} entry pairs to {DEST}")
    print(f"  ({len(new)} .json + {len(new)} .md)")
    print(f"\nSkipped (already in your corpus): {len(skipped_overlap)}")
    print(f"  e.g. {[f'{n}→{s}' for n,s in skipped_overlap[:5]]}")
    print(f"\nSample new slugs:")
    for s in sorted(new)[:15]:
        print(f"  {s}")


if __name__ == "__main__":
    main()
