# Business Bible Research

An agent skill for creating comprehensive, sourced "business bible" reports on companies, competitors, products, and markets.

Use it when you want a sales, BD, strategy, or founder-ready dossier that goes beyond a surface summary: website screenshots, source URLs, feature and use-case analysis, customer evidence, review pain points, competitor positioning, GTM notes, and a CEO/founder blueprint for building something similar.

## What It Produces

The skill guides an AI agent to produce:

- A Markdown `*_bible.md` report
- Full-page website screenshots
- Visible-page text extracts
- Sitemap or URL inventory when available
- Page atlas with source URLs and screenshot links
- Sales and BD playbook
- CEO/founder blueprint
- Source appendix and confidence/gaps section

## Install

Install with the Skills CLI:

```bash
npx skills add kzuri/business-bible-research
```

Use the Skills CLI options to choose the agent or destination you want.

## Usage

Invoke the skill directly:

```text
Use $business-bible-research to create a full business bible for Acme Corp: https://example.com/
```

Example prompts:

```text
Use $business-bible-research to research Ramp and create a CEO-ready business bible.
```

```text
Use $business-bible-research to build a sales and competitive dossier for Pleo, including screenshots and review pain points.
```

```text
Use $business-bible-research to analyze this startup so we can decide whether to build a similar product.
```

## Recommended Workflow

1. Browse the target website like a real user.
2. Capture screenshots for important pages.
3. Save visible text extracts and page metadata.
4. Build a sitemap or URL inventory when available.
5. Research external sources such as LinkedIn, G2, Capterra, Trustpilot, Reddit, press, funding pages, and customer stories.
6. Synthesize the report using the included outline.
7. Verify every screenshot link has a source URL.

## Included Files

- `SKILL.md` - core skill instructions and trigger description
- `references/report-outline.md` - complete report structure
- `references/research-checklist.md` - research checklist and source list
- `scripts/create_business_bible_scaffold.py` - helper to create report folders and a starter Markdown file
- `agents/openai.yaml` - optional agent UI metadata

## Scaffold Helper

```bash
python3 scripts/create_business_bible_scaffold.py "Company Name" --url https://example.com --out .
```

This creates:

- `company-name_bible.md`
- `company-name_screenshots/`
- `company-name_extracts/`

## Notes

This skill is designed for public-source research. It should clearly separate confirmed facts from inference and call out gaps that require private diligence, such as pricing quotes, revenue, unit economics, support SLAs, payment partner economics, or behind-login product behavior.

## License

MIT
