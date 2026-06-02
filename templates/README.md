# Templates

[中文版](README.zh-CN.md)

This folder provides optional templates for preparing questionnaire files before using `$survey-scale-review`.

## Recommended

Use [`survey_scale_review_template.xlsx`](survey_scale_review_template.xlsx) if you want the cleanest review workflow.

It contains:

- `README`: short instructions
- `Guide`: column explanations, examples, and common notes
- `Variables`: one row per variable or scale block
- `Questionnaire`: instruction rows and item rows with source items and Chinese translations/adaptations side by side

## CSV Option

Use these if you prefer plain tables or Google Sheets:

- [`variables_template.csv`](variables_template.csv)
- [`questionnaire_template.csv`](questionnaire_template.csv)

## You Can Also Skip the Template

If you already have an Excel, Word, Markdown, or plain-text questionnaire draft, upload it and ask:

```text
Use $survey-scale-review to review this questionnaire draft.
It is not in your template format, so first infer the structure and tell me what is missing.
```

## 中文说明

这里提供可选模板。推荐使用 `survey_scale_review_template.xlsx`，其中包含：

- `Variables`：变量名称、中文变量名、条目数、填写者、时间点、量表类型和来源
- `Questionnaire`：英文原题、中文翻译/改编、来源和备注
- `Guide`：每一类字段的填写说明，以及反向题、自编题项、新增题项等示例

如果你已有现成问卷文件，也可以不使用模板，直接让 `$survey-scale-review` 先推断结构并指出缺失信息。
