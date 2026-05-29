# Developer and Advanced Usage

[中文版](developer-advanced.zh-CN.md)

Most users do not need this page. After installing the skill, they can upload an Excel, Word, Markdown, or plain-text questionnaire and ask Codex, Claude Code, WorkBuddy, or another agent connected to this repository's workflow to review it.

This page is for maintainers and advanced users who want to run the helper script directly.

## Workbook Inspection Script

The repository includes:

```text
scripts/inspect_workbook.py
```

It extracts workbook structure and generates:

- `issues.html`
- `inspection_summary.json`
- `variables.json` / `variables.csv`
- `items.json` / `items.csv`
- `issues.json` / `issues.csv`

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python scripts/inspect_workbook.py path/to/questionnaire.xlsx --outdir outputs/review
```

Optional formatted Excel output:

```bash
python scripts/inspect_workbook.py path/to/questionnaire.xlsx --outdir outputs/review --xlsx
```

## Important

The script is intentionally conservative. It catches structural and launch-readiness issues, but it does not replace the full skill review. Translation quality, adaptation defensibility, self-developed scale risk, and respondent experience still require the agent's domain reasoning.
