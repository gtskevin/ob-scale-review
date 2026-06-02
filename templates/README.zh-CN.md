# 模板说明

[English version](README.md)

这个文件夹提供 `$survey-scale-review` 的可选模板。不是必须使用模板，但使用模板可以让审阅更稳定。

## 推荐模板

优先使用 [`survey_scale_review_template.xlsx`](survey_scale_review_template.xlsx)。

它包含：

- `README`：简短说明
- `Guide`：字段说明、填写示例和常见备注
- `Variables`：每个变量或量表一行
- `Questionnaire`：指导语行和题项行，英文原题与中文翻译/改编并排

## CSV 模板

如果你更喜欢普通表格或 Google Sheets，可以使用：

- [`variables_template.csv`](variables_template.csv)
- [`questionnaire_template.csv`](questionnaire_template.csv)

## 可以不使用模板

如果你已有 Excel、Word、Markdown 或纯文本问卷草稿，可以直接上传并说：

```text
用 $survey-scale-review 检查这个问卷草稿。
它不是模板格式，请先推断变量、填写者、时间点、来源和条目结构，
再告诉我哪些信息缺失。
```

## 填写建议

- `Variables` 里写变量层面的信息：变量名、条目数、填写者、时间点、量表类型和来源。
- `Questionnaire` 里写题项层面的信息：英文原题、当前中文题项、指导语、来源和备注。
- 如果原题是反向题，请保留英文里的 `Reverse coded` 标记，并在备注中说明中文是否已正向化。
- 如果题项是新增或自编，请明确写 `Self-developed`、`new item` 或 `added item`。
- 如果是配对问卷，请明确写“员工”还是“领导”填写。
