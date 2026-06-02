# Output Formats

## Issue list fields

| Field | Meaning |
|---|---|
| issue_id | Stable issue number |
| priority | P0/P1/P2/P3 |
| variable_name | Variable/scale name if available |
| location | Sheet, row, variable, or item |
| issue_type | translation, adaptation, instruction_contamination, double_barreled, referent_level, reverse_item, wave, respondent, source, placeholder, formatting |
| issue_summary | One short human-readable summary of the issue |
| current_text | Existing text |
| suggested_text | Suggested revision |
| rationale | Why this matters |
| evidence_status | 资料确认 / 模型推断 / 需源文核验 |
| why_it_matters | Plain-language explanation for early-stage doctoral students |
| reviewer_action | RA 可直接处理 / 研究者确认 / 建议专家复核 / 仅提示 |
| status | 待处理 / 已采纳 / 不采纳 / 需讨论 |

For translation, adaptation, instruction contamination, and referent-level issues, include concrete evidence in `rationale`: what the source says, what the current Chinese changes, and how that affects measurement or respondent interpretation. `why_it_matters` should be readable by a beginner. `suggested_text` should contain concrete revised wording whenever possible. If one revision depends on theory choice, provide clearly labeled alternatives.

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
| adoption_level | 必须采纳 / 建议采纳 / 研究者确认 / 可选 |
| reviewer_note | Method or reviewer explanation if needed |
| evidence_status | 资料确认 / 模型推断 / 需源文核验 |
| owner | RA 可直接处理 / 研究者确认 / 建议专家复核 / 仅提示 |

For translation suggestions, the `reason` field should name the drift type, such as `新增概念`, `遗漏限定`, `actor shift`, `referent shift`, `level-of-analysis`, `valence shift`, or `back-translation risk`.

## Suggested revised wording columns

Include these columns in the default HTML review page. Add them to the right of original content if the user asks for an Excel workbook:

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
- HTML formal reports should include a compact version/update panel near the top and a smaller repeat in the footer: local commit/date when available, `检查新版本` link, and copyable update prompt for non-technical users.
- Use Markdown only when the user explicitly asks for Markdown or when it is an internal editable source used to render HTML.
- Generate a formatted `.xlsx` workbook only when the user explicitly requests it.
- Keep CSV/JSON only as machine-readable support files, not as the main user-facing output.

## HTML update panel fields

| Field | Meaning |
|---|---|
| local_commit | Local short SHA if available; otherwise `未知` |
| commit_date | Local commit date if available; otherwise `未知` |
| check_update_url | `https://github.com/gtskevin/survey-scale-review/compare/<local-sha>...main` when SHA is available, otherwise `https://github.com/gtskevin/survey-scale-review/commits/main` |
| update_prompt | Plain-language prompt users can copy into Codex/Claude Code/WorkBuddy |
| update_note | Explain that the link checks GitHub only; the local skill updates after the Agent runs the update prompt |

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
