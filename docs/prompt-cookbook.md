# OB Scale Review Prompt Cookbook

[中文版](prompt-cookbook.zh-CN.md)

Use these prompts when you are not sure how to ask for the review.

## First-Time Use

```text
Use $ob-scale-review to inspect this questionnaire file.
First tell me whether the file has enough information for a full review.
If anything is missing, list what I need to add before you evaluate translation or adaptation quality.
```

Claude Code:

```text
/ob-scale-review inspect this questionnaire file.
First tell me whether the file has enough information for a full review.
```

## Quick RA Check

```text
Use $ob-scale-review for a quick RA check.
Only check item counts, respondent labels, time waves, missing source information,
missing Chinese items, and launch placeholders.
```

## Full Formal Review

```text
Use $ob-scale-review to do a full formal review of this questionnaire.
Check English-Chinese translation, adapted-scale defensibility, reverse-coded source items,
self-developed or highly adapted item risks, paired survey structure, respondent ambiguity,
time windows, response options, and launch-blocking problems.
```

## Adapted Scale Review

```text
Use $ob-scale-review to focus on adapted scales.
For each adapted item, tell me whether the adaptation can be defended to reviewers,
what changed from the source item, whether the construct meaning shifted,
and what method-section explanation I should prepare.
```

## Reverse-Coded Item Check

```text
Use $ob-scale-review to check all reverse-coded source items.
I usually rewrite reverse-coded items into positive Chinese wording.
Please verify whether the positive wording is accurate and whether scoring notes need to be updated.
```

## Self-Developed Scale Check

```text
Use $ob-scale-review to review the self-developed or highly adapted items.
Check for double-barreled items, leading wording, social desirability,
construct contamination, causal wording, vague referents, vague time windows,
and response-scale mismatch.
```

## Pre-Launch Check

```text
Use $ob-scale-review for a pre-launch check.
Do not rewrite every item. Focus on P0/P1 issues:
placeholders, confusing instructions, respondent mismatch, time windows,
response options, pairing ID risks, and wording that respondents may interpret differently.
```

## Non-Template File

```text
Use $ob-scale-review to review this questionnaire draft.
It is not in the template format. First infer the structure:
variables, respondents, waves, source items, Chinese items, sources, and notes.
Then tell me what is missing and what can still be reviewed.
```

## Ask for an Optimized Comparison Table

```text
Use $ob-scale-review to create an optimized questionnaire comparison table
after the review. Keep the original source item and current Chinese item,
and add suggested Chinese wording, rationale, priority, and researcher-confirmation columns.
```

## 中文提示词

第一次使用：

```text
用 $ob-scale-review 检查这个问卷文件。
请先判断这个文件是否足够做完整审阅；如果信息不够，先列出缺失信息，
不要直接开始评价翻译和改编质量。
```

完整审阅：

```text
用 $ob-scale-review 对这个问卷做完整审阅。
请检查英文-中文翻译、改编量表是否能向审稿人解释、反向题正向化与计分、
自编或高度改编题项风险、领导-员工配对结构、被试理解歧义、时间窗口、
反应选项和正式发放前阻断问题。
```

发放前终检：

```text
用 $ob-scale-review 做发放前终检。
不要大幅重写题项，只检查 P0/P1 问题：占位符、指导语、填写者不一致、
时间窗口、反应选项、配对 ID 风险和容易被不同被试理解不同的表达。
```
