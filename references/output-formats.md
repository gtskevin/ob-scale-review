# Output Formats

## Issue list fields

| Field | Meaning |
|---|---|
| issue_id | Stable issue number |
| priority | P0/P1/P2/P3 |
| variable_name | Variable/scale name if available |
| location | Sheet, row, variable, or item |
| issue_type | translation, adaptation, reverse_item, referent, wave, respondent, source, placeholder, formatting |
| issue_summary | One short human-readable summary of the issue |
| current_text | Existing text |
| suggested_text | Suggested revision |
| rationale | Why this matters |
| reviewer_action | RA can edit / researcher confirmation needed / note only |
| status | 待处理 / 已采纳 / 不采纳 / 需讨论 |

## Modification suggestion table

| Field | Meaning |
|---|---|
| variable | Variable name |
| respondent | Employee/leader/other |
| wave | T1/T2/T3 if available |
| source_original | English source item |
| current_chinese | Current Chinese item |
| suggested_chinese | Suggested Chinese item |
| reason | Concise rationale |
| priority | P0-P3 |

## Optimized questionnaire comparison columns

Add these to the right of original content:

| Column | Purpose |
|---|---|
| AI建议中文 | Revised item/instruction |
| 修改类型 | 翻译优化 / 歧义消除 / 改编增强 / 正向化说明 / 格式 |
| 修改理由 | Why the change helps |
| 审稿解释 | Especially for adapted scales |
| 建议采纳级别 | 必须采纳 / 建议采纳 / 可选 |
| 用户确认 | Blank for researcher decision |

## File choices

- Use one HTML review page as the default user-facing deliverable for long reviews.
- Put the executive summary, issue list, and modification suggestions in that HTML page so the user does not need to read a long Markdown report in chat.
- Use clean, copy-friendly HTML tables as the primary issue/suggestion format.
- HTML issue tables should use Chinese column headers, priority row colors, a top summary, top P0/P1 issues, a `变量/量表` column, and a short issue summary.
- Use Markdown only when the user explicitly asks for Markdown or when it is an internal editable source used to render HTML.
- Generate a formatted `.xlsx` workbook only when the user explicitly requests it.
- Keep CSV/JSON only as machine-readable support files, not as the main user-facing output.

## Recommended review workbook sheets

| Sheet | Purpose |
|---|---|
| Summary | File overview and P0-P3 counts |
| Issues | Main issue register for RA/researcher processing |
| Suggestions | Revised wording table; empty if no item-level suggestions were generated yet |
| Variables | Extracted variable index |
| Items | Extracted item-level data |

## Excel readability defaults

| Column type | Width |
|---|---:|
| IDs, priority, status | 12-16 |
| Location, type, respondent, wave | 16-22 |
| Current text, suggested text, rationale | 36-70 |
| Source original and current Chinese item | 45-75 |

Set vertical alignment to top, wrap text for long columns, and cap row heights so sheets remain navigable.
