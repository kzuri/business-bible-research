#!/usr/bin/env python3
import argparse
import re
from datetime import date
from pathlib import Path


def slugify(value: str) -> str:
    value = value.lower().strip()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "business"


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a business bible research scaffold.")
    parser.add_argument("name", help="Company, product, or business name")
    parser.add_argument("--url", default="", help="Target website URL")
    parser.add_argument("--out", default=".", help="Output directory")
    args = parser.parse_args()

    out = Path(args.out).expanduser().resolve()
    slug = slugify(args.name)
    screenshots = out / f"{slug}_screenshots"
    extracts = out / f"{slug}_extracts"
    screenshots.mkdir(parents=True, exist_ok=True)
    extracts.mkdir(parents=True, exist_ok=True)

    report = out / f"{slug}_bible.md"
    if not report.exists():
        report.write_text(
            f"""# {args.name} Bible

Research date: {date.today().isoformat()}
Target website: {args.url or "TBD"}
Screenshots: `./{screenshots.name}`
Text extracts: `./{extracts.name}`
Sitemap inventory: `./{slug}_sitemap_inventory.csv` if available

## Executive Summary

TODO

## Company Snapshot

TODO

## Website Positioning

TODO

## Product Architecture

TODO

## Use-Case Map

TODO

## Business Model and Pricing

TODO

## Customer Evidence

TODO

## Competitive Positioning

TODO

## External Review and Community Signal

TODO

## Pain Points

TODO

## Sales and BD Playbook

TODO

## CEO/Founder Blueprint

TODO

## Page Atlas

| Slug | Page title | H1 | Words | URL | Screenshot | Notes |
|---|---|---|---:|---|---|---|

## Source Appendix

TODO

## Gaps and Confidence

TODO
""",
            encoding="utf-8",
        )

    print(report)
    print(screenshots)
    print(extracts)


if __name__ == "__main__":
    main()
