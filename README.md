# OB Scale Review

**OB Scale Review** is a Codex skill for reviewing organizational behavior and management research questionnaires. It focuses on English source scales, Chinese translations, adapted scales, reverse-coded items, leader-employee paired surveys, multi-wave designs, and pre-launch survey quality checks.

中文说明：这是一个用于组织行为学、管理学和心理测量研究的 Codex Skill，帮助研究者检查英文原始量表、中文翻译/改编条目、领导-员工配对问卷、多时间点问卷和正式发放前的问卷质量。

## What It Helps Review

- Scale translation quality between English source items and Chinese questionnaire items
- Adapted scale defensibility, especially whether reviewers will see the adaptation as reasonable rather than a newly invented scale
- Reverse-coded source items rewritten into positive wording, with scoring reminders
- Self-developed or highly adapted scale problems, including double-barreled items, leading wording, construct contamination, causal wording, vague referents, and response-scale mismatch
- Respondent experience for employees and managers in organizations
- Leader-employee paired survey issues, including respondent mismatch, referent ambiguity, and time-window problems
- Pre-launch blocking issues such as placeholders, missing sources, missing items, and inconsistent variable lists

## Quick Start

1. Install the skill:

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/gtskevin/ob-scale-review.git ~/.codex/skills/ob-scale-review
```

2. Start a new Codex session.

3. Ask Codex to review your questionnaire:

```text
Use $ob-scale-review to review my questionnaire Excel file.
```

4. Review the generated HTML issue table first. It is designed for fast scanning, with Chinese headers, priority colors, and a variable/scale column.

## Typical Use Cases

Use `$ob-scale-review` when you have:

- An Excel file prepared by a research assistant with variables, source items, translated items, and references
- A Chinese questionnaire adapted from English OB, psychology, management, or AI-at-work scales
- A paired leader-subordinate survey with separate employee and supervisor versions
- A longitudinal survey with T1/T2/T3 waves
- A final survey draft before launching on Wenjuanxing, Qualtrics, or another survey platform

Example prompt:

```text
Use $ob-scale-review to review this Excel questionnaire.
Please check translation quality, adapted scale defensibility, reverse-coded item handling,
paired survey issues, respondent ambiguity, and launch-blocking problems.
```

中文示例：

```text
用 $ob-scale-review 检查这个问卷 Excel。
重点看英文量表翻译、改编是否能向审稿人解释、反向题是否已正向化且计分清楚、
领导-员工配对问卷是否有填写者/指代/时间点问题，以及正式发放前是否有阻断问题。
```

## Default Output

The skill defaults to Chinese outputs:

1. A structured review report in Markdown/HTML
2. A clean HTML issue table with Chinese headers, priority colors, and a `变量/量表` column
3. A modification suggestion table when item-level revisions are needed
4. Optional optimized questionnaire comparison table only after the user confirms they want it

The issue table uses four priority levels:

| Priority | Meaning |
|---|---|
| P0 | Launch blocker: must fix before distribution |
| P1 | High risk: likely affects data quality, scoring, pairing, or reviewer defensibility |
| P2 | Medium risk: affects clarity, wording, or respondent experience |
| P3 | Low risk or reminder: useful for polishing or documentation |

## Design Principles

- Mature non-adapted scales are not re-judged for construct coverage; the review focuses on translation equivalence and respondent clarity.
- Adapted scales receive special attention because reviewers may ask whether the adaptation is still faithful to the source scale.
- Reverse-coded source items may be rewritten as positive Chinese items by default, but scoring notes must be updated.
- Self-developed and highly adapted scales are checked for common psychometric item-writing problems.
- Respondent experience matters: ambiguous phrases like "my team", "leader", "recently", and "AI tools" are flagged when they may be interpreted differently by employees and managers.

## Included Files

```text
ob-scale-review/
├── SKILL.md
├── README.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── adaptation-review.md
│   ├── evaluation-rubric.md
│   ├── output-formats.md
│   ├── report-template.md
│   └── respondent-experience.md
└── scripts/
    └── inspect_workbook.py
```

## Optional Workbook Inspection Script

The bundled script extracts workbook structure and generates a clean HTML issue list.

Install script dependencies if needed:

```bash
pip install -r requirements.txt
```

```bash
python scripts/inspect_workbook.py path/to/questionnaire.xlsx --outdir outputs/review
```

Primary user-facing output:

```text
outputs/review/issues.html
```

Optional spreadsheet output:

```bash
python scripts/inspect_workbook.py path/to/questionnaire.xlsx --outdir outputs/review --xlsx
```

The script is intentionally conservative. It finds structural and launch-readiness issues, but the full review still depends on the Codex skill's domain reasoning.

## Manual Installation

Clone this repository into your Codex skills directory:

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/gtskevin/ob-scale-review.git ~/.codex/skills/ob-scale-review
```

Then start a new Codex session and invoke:

```text
Use $ob-scale-review to review my questionnaire.
```

## Keywords

organizational behavior, OB research, survey scale review, questionnaire review, scale adaptation, Chinese translation, management research, psychology scales, reverse-coded items, leader-member exchange, leader-employee paired survey, multi-wave survey, AI at work, psychometrics, measurement validity, Codex skill

## License

MIT
