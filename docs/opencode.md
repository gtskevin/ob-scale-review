# Using OB Scale Review with OpenCode

[中文版](opencode.zh-CN.md)

OpenCode does not currently use the same `SKILL.md` discovery convention as Codex or Claude Code. The most practical integration is an OpenCode custom command that tells OpenCode to use this repository's `SKILL.md`, references, templates, and scripts as the review workflow.

OpenCode custom command documentation:

- https://dev.opencode.ai/docs/commands

## Option A: Project Command

Clone this repository into your project, for example:

```bash
mkdir -p tools
git clone https://github.com/gtskevin/ob-scale-review.git tools/ob-scale-review
```

Create a command file:

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

Then run in OpenCode:

```text
/ob-scale-review review my questionnaire Excel file
```

## Option B: Global Command

Install the repository somewhere stable:

```bash
mkdir -p ~/.agents/skills
git clone https://github.com/gtskevin/ob-scale-review.git ~/.agents/skills/ob-scale-review
```

Create a global command:

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

Then run:

```text
/ob-scale-review review my questionnaire draft
```

## Notes

- This is a compatibility bridge, not native OpenCode `SKILL.md` support.
- Keep the repository folder intact so references, templates, examples, and scripts remain available.
- If OpenCode cannot access the questionnaire file path, pass the file explicitly or place it in the current project folder.
