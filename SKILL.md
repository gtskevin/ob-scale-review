---
name: ob-scale-review
description: Use when reviewing research survey scales, especially organizational behavior or management questionnaires with English source items, Chinese translations, adapted scales, reverse-coded items, paired leader-employee surveys, multi-wave surveys, or pre-launch questionnaire quality checks.
---

# OB Scale Review

Use this skill to review OB/management research questionnaires and scale translation/adaptation files. Default language is Chinese unless the user asks otherwise.

## Default stance

- Default mode is **修改建议模式**: produce a Chinese HTML/Markdown report plus clean, copy-friendly HTML issue and suggestion tables.
- Do not automatically create a rewritten questionnaire. After the report and suggestion table, ask whether the user wants an optimized comparison questionnaire.
- For optimized questionnaires, preserve the original columns and add right-side comparison columns such as `AI建议中文`, `修改类型`, `修改理由`, `审稿解释`, `建议采纳级别`, `用户确认`.
- Treat reverse-coded source items according to Huang Mingpeng's default preference: reverse items are usually rewritten into positive wording to reduce respondent confusion. Check whether positive wording is accurate and whether scoring notes are updated; do not mark positive wording as an error by itself.
- For mature non-adapted scales, do not re-evaluate whether items cover the construct. Check translation equivalence, clarity, response options, respondent experience, and file consistency.
- For adapted, self-developed, or highly adapted scales, focus on whether the adaptation is defensible to reviewers and whether items have common scale-design problems.

## Modes

Choose the mode from the user's request; when unclear, use `formal_review`.

| Mode | When to use | Output focus |
|---|---|---|
| `quick_check` | RA has just prepared a scale file | Blocking issues: item counts, respondent/time mismatch, placeholders, missing fields |
| `formal_review` | Researcher wants a full review | Report + issue list + modification suggestions |
| `pre_launch_check` | Survey is nearly ready to distribute | Launch readiness: instructions, referents, pairing IDs, time windows, response options |

## Workflow

1. Inspect the source file structure. For Excel, prefer `scripts/inspect_workbook.py` to summarize sheets, columns, variable blocks, items, sources, placeholders, reverse-coded markers, and obvious consistency issues.
2. Build a variable-item index: variable name, Chinese name, respondent, wave, item count, source, original item, current Chinese item, notes.
3. Classify each scale as mature direct translation, mature adapted scale, self-developed scale, highly adapted scale, or mixed scale.
4. Run blocking checks first: item-count mismatch, respondent mismatch, wave mismatch, missing original/current item text, missing source, placeholders, unresolved internal notes, reverse-scoring conflicts.
5. Review scales using the appropriate standard:
   - Direct mature scales: translation equivalence and respondent clarity.
   - Adapted mature scales: adaptation logic and reviewer defensibility.
   - Self-developed/highly adapted scales: common item-writing errors and psychometric design risks.
6. Review respondent experience: ambiguity, referents, team/leader/AI definitions, time windows, sensitive wording, response-option fit.
7. Produce concise Chinese outputs. If the content is long or structured, follow the user's Pretty Doc rule: save Markdown under `docs/`, render with `pretty-doc path/to/file.md --open`, and link the HTML.

## When to load references

- Load `references/evaluation-rubric.md` for severity levels, core criteria, reverse-item handling, and scale-type-specific standards.
- Load `references/adaptation-review.md` when a file includes adapted scales or AI/context replacement.
- Load `references/respondent-experience.md` for ambiguity, instructions, response options, and paired survey checks.
- Load `references/report-template.md` before writing a full review report.
- Load `references/output-formats.md` when creating an issue list, suggestion table, or optimized questionnaire comparison.

## Output requirements

Default formal review outputs:

1. Chinese review report: executive summary, structure overview, P0/P1 issues, adapted-scale review, translation/expression issues, reverse-item positive wording record, respondent experience, method-writing suggestions, and next-step question about optimized questionnaire.
2. Copy-friendly HTML tables for issue list and modification suggestions. Use Chinese column headers, priority colors, a top summary, top P0/P1 issues, a `变量/量表` column, a short issue summary, and clear action ownership (`RA 可直接处理`, `研究者确认`, `仅提示`) whenever available.
3. Optional formatted Excel workbook only when the user explicitly wants spreadsheet processing.

Avoid CSV and Excel as the default user-facing output because long questionnaire text is easier to review in the cleaner HTML table. CSV/JSON can be kept as machine-readable support files.

## Boundaries

- Do not claim to have verified original journal scale wording unless the source document or article text was provided or explicitly looked up.
- Do not replace researcher judgment on construct boundaries, high adaptation, or self-developed scale validity.
- Do not silently overwrite original questionnaire content.
- Do not treat all item wording changes as final. Label high-adaptation suggestions as needing researcher confirmation.
