# 在 OpenCode 中使用 OB Scale Review

[English version](opencode.md)

OpenCode 目前不是按 Codex/Claude Code 的 `SKILL.md` 方式自动发现技能。更实用的做法是创建一个 OpenCode 自定义命令，让它读取本仓库的 `SKILL.md`、references、templates 和脚本。

OpenCode 自定义命令文档：

- https://dev.opencode.ai/docs/commands

## 方式 A：项目级命令

把仓库克隆到你的研究项目中，例如：

```bash
mkdir -p tools
git clone https://github.com/gtskevin/ob-scale-review.git tools/ob-scale-review
```

创建 OpenCode 命令文件：

```bash
mkdir -p .opencode/commands
cat > .opencode/commands/ob-scale-review.md <<'EOF'
---
description: Review OB/management survey scales, translated questionnaires, adapted measures, and paired survey quality.
---

Use the OB Scale Review workflow in @tools/ob-scale-review/SKILL.md.

When relevant, consult:
- @tools/ob-scale-review/references/evaluation-rubric.md
- @tools/ob-scale-review/references/adaptation-review.md
- @tools/ob-scale-review/references/respondent-experience.md
- @tools/ob-scale-review/references/output-formats.md
- @tools/ob-scale-review/docs/prompt-cookbook.md

Review the questionnaire or scale file provided in the user request.
Default to Chinese. Create one HTML review page with an executive summary, P0-P3 issue list, variable/scale names, modification suggestions, owner/action labels, and next-step recommendations. Do not output a long Markdown report in the chat by default.
If an Excel file is available and Python dependencies work, you may run:

python tools/ob-scale-review/scripts/inspect_workbook.py <workbook-path> --outdir outputs/ob-scale-review

If the script dependencies are unavailable, do not fail. Infer the structure from the available file contents and report missing information.

User request:
$ARGUMENTS
EOF
```

然后在 OpenCode 里运行：

```text
/ob-scale-review review my questionnaire Excel file
```

## 方式 B：全局命令

把仓库安装到一个稳定位置：

```bash
mkdir -p ~/.agents/skills
git clone https://github.com/gtskevin/ob-scale-review.git ~/.agents/skills/ob-scale-review
```

创建全局命令：

```bash
mkdir -p ~/.config/opencode/commands
cat > ~/.config/opencode/commands/ob-scale-review.md <<'EOF'
---
description: Review OB/management survey scales, translated questionnaires, adapted measures, and paired survey quality.
---

Use the OB Scale Review workflow in ~/.agents/skills/ob-scale-review/SKILL.md.
Consult the repository references and templates when needed.
Default to Chinese. Create one HTML review page and keep the chat response short.

If an Excel file is available and Python dependencies work, you may run the bundled inspect_workbook.py script.
If dependencies are missing, infer the structure from available file contents and continue.

User request:
$ARGUMENTS
EOF
```

然后运行：

```text
/ob-scale-review review my questionnaire draft
```

## 注意

- 这是兼容方案，不是 OpenCode 原生 `SKILL.md` 支持。
- 请保留整个仓库文件夹，references、templates、examples 和 scripts 都可能被用到。
- 如果 OpenCode 访问不到问卷文件路径，请把问卷放到当前项目文件夹，或在请求中明确提供路径。
