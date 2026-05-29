# 开发者与高级用法

[English version](developer-advanced.md)

大多数用户不需要阅读这一页。安装 Skill 后，直接上传 Excel、Word、Markdown 或纯文本问卷，并让 Codex、Claude Code、WorkBuddy 或其他已接入本仓库流程的 agent 检查即可。

本页只面向维护者和希望手动运行辅助脚本的高级用户。

## 工作簿检查脚本

仓库包含：

```text
scripts/inspect_workbook.py
```

它会抽取工作簿结构，并生成：

- `issues.html`
- `inspection_summary.json`
- `variables.json` / `variables.csv`
- `items.json` / `items.csv`
- `issues.json` / `issues.csv`

安装依赖：

```bash
pip install -r requirements.txt
```

运行：

```bash
python scripts/inspect_workbook.py path/to/questionnaire.xlsx --outdir outputs/review
```

如果需要格式化 Excel 输出：

```bash
python scripts/inspect_workbook.py path/to/questionnaire.xlsx --outdir outputs/review --xlsx
```

## 注意

这个脚本只做结构化和发放前阻断问题的初步检查。它不能替代完整 Skill 审阅。翻译质量、改编合理性、自编量表风险和被试填写体验仍需要 agent 的领域判断。
