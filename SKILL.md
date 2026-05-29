---
name: ob-scale-review
description: Use when reviewing research survey scales, especially organizational behavior or management questionnaires with English source items, Chinese translations, adapted scales, reverse-coded items, paired leader-employee surveys, multi-wave surveys, or pre-launch questionnaire quality checks.
---

# OB Scale Review

Use this skill to review OB/management research questionnaires and scale translation/adaptation files. Default language is Chinese unless the user asks otherwise.

## Default stance

- Default mode is **修改建议模式**: produce a concise Chinese chat summary plus a user-facing HTML review page. The HTML should contain the executive summary, issue list, and modification suggestions in one copy-friendly page.
- Do not output a long Markdown report by default. Use Markdown only as an internal/source format when needed to render HTML, or when the user explicitly asks for Markdown.
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

1. Inspect the source file structure. For Excel, prefer `scripts/inspect_workbook.py` to summarize sheets, columns, variable blocks, items, sources, placeholders, reverse-coded markers, and obvious consistency issues when the local environment can run Python with `pandas` and `openpyxl`.
   - The user does not need to run this script manually.
   - If the script dependencies are unavailable, do not fail the review. Use the agent's available spreadsheet/file-reading tools to inspect the workbook, or tell the user what dependency is missing only if no fallback is available.
   - If the file is not in the template format, first infer its structure and report missing information before judging translation or adaptation quality.
   - The script output is only a **structure pre-check**. Never treat the script-generated `issues.html` as the final review for a formal review, because it cannot judge translation equivalence, adaptation quality, instruction contamination, double-barreled wording, or level-of-analysis problems.
2. Build a variable-item index: variable name, Chinese name, respondent, wave, item count, source, original item, current Chinese item, notes.
3. Classify each scale as mature direct translation, mature adapted scale, self-developed scale, highly adapted scale, or mixed scale.
4. Run blocking checks first: item-count mismatch, respondent mismatch, wave mismatch, missing original/current item text, missing source, placeholders, unresolved internal notes, reverse-scoring conflicts.
5. Run a **row-by-row semantic audit** before writing the final report:
   - For every item with English source text, compare the English and Chinese item directly. Identify added concepts, omitted concepts, changed intensity, changed actor, changed object, changed time frame, changed valence, and changed observability.
   - For every adapted item, separate reasonable object/context replacement from meaning-changing adaptation. If the Chinese item measures a different behavior, cognition, emotion, outcome, or causal mechanism, flag it even when the Chinese reads fluently.
   - For every instruction block, check whether it defines the construct, reveals the intended variable, explains what the scale is "really" measuring, or tells respondents what not to consider. Such instructions can contaminate responses and should be flagged.
   - For every self-developed or highly adapted item, check double-barreled wording, social desirability, moralized/accusatory wording, construct contamination, causal wording, unsupported premises, and response-option fit.
   - For leadership, team, and paired designs, explicitly check referent and level of analysis: `我的领导/领导层`, `我/我们`, `团队/部门/组织`, `员工/下属/团队成员`, and whether the respondent can observe the target.
6. Review scales using the appropriate standard:
   - Direct mature scales: translation equivalence and respondent clarity.
   - Adapted mature scales: adaptation logic and reviewer defensibility.
   - Self-developed/highly adapted scales: common item-writing errors and psychometric design risks.
7. Review respondent experience: ambiguity, referents, team/leader/AI definitions, time windows, sensitive wording, response-option fit.
8. Produce concise Chinese outputs. For long or structured reviews, make HTML the primary user-facing artifact and keep the chat response short. If using the user's Pretty Doc workflow, save Markdown only as the editable source, render with `pretty-doc path/to/file.md --open`, and link the HTML rather than pasting the Markdown report.

## When to load references

- Load `references/evaluation-rubric.md` for severity levels, core criteria, reverse-item handling, and scale-type-specific standards.
- Load `references/translation-equivalence.md` when English source items and Chinese translations are both present.
- Load `references/adaptation-review.md` when a file includes adapted scales or AI/context replacement.
- Load `references/respondent-experience.md` for ambiguity, instructions, response options, and paired survey checks.
- Load `references/report-template.md` before writing a full review report.
- Load `references/output-formats.md` when creating an issue list, suggestion table, or optimized questionnaire comparison.

## Output requirements

Default formal review outputs:

1. One user-facing HTML review page in Chinese: executive summary, structure overview, P0/P1 issues, adapted-scale review, translation/expression issues, reverse-item positive wording record, respondent experience, method-writing suggestions, issue list, modification suggestions, and next-step question about optimized questionnaire.
2. The HTML issue and suggestion tables must be copy-friendly. Use Chinese column headers, priority colors, a top summary, top P0/P1 issues, a `变量/量表` column, a short issue summary, and clear action ownership (`RA 可直接处理`, `研究者确认`, `仅提示`) whenever available.
3. Optional formatted Excel workbook only when the user explicitly wants spreadsheet processing.

Avoid long Markdown, CSV, and Excel as the default user-facing output because long questionnaire text is easier to review in the cleaner HTML page. CSV/JSON can be kept as machine-readable support files.

## Boundaries

- Do not claim to have verified original journal scale wording unless the source document or article text was provided or explicitly looked up.
- Do not replace researcher judgment on construct boundaries, high adaptation, or self-developed scale validity.
- Do not silently overwrite original questionnaire content.
- Do not treat all item wording changes as final. Label high-adaptation suggestions as needing researcher confirmation.
