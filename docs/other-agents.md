# Other Agent Tools

[中文版](other-agents.zh-CN.md)

OB Scale Review is not limited to Codex or Claude Code. Its core is a reusable survey-scale review workflow, so any agent that can read this repository's `SKILL.md`, project instructions, or reusable prompts can use it.

For practical use: **install it as a skill when the tool supports skills; otherwise point the agent to this repository as its review instruction.**

## Support Matrix

| Tool | Recommended setup | How to invoke |
|---|---|---|
| Codex | Install under `~/.codex/skills/ob-scale-review/` | `Use $ob-scale-review to review this questionnaire Excel file` |
| Claude Code | Install under `~/.claude/skills/ob-scale-review/` | `/ob-scale-review review this questionnaire Excel file` |
| WorkBuddy / Work Buddy | Install through the Claude Code skill path | `/ob-scale-review review this questionnaire Excel file` |
| OpenCode | Create a custom command pointing to this repository's `SKILL.md` | `/ob-scale-review review ...` |
| Cursor | Reference this repository in project rules/instructions | Ask Cursor to read `SKILL.md` before reviewing |
| Windsurf | Reference this repository in rules, memories, or project instructions | Ask Windsurf to follow the OB Scale Review workflow |
| Trae | Use project rules or a reusable prompt | Upload the questionnaire and paste the generic prompt |
| Qoder | Use project instructions or a reusable prompt | Upload the questionnaire and paste the generic prompt |
| Gemini CLI | Reference this repository through `AGENTS.md` or project context | Ask Gemini to read `SKILL.md` before reviewing |
| GitHub Copilot CLI / coding agent | Reference this repository through repository instructions | Ask Copilot to follow the workflow and create an HTML review page |
| Tongyi Lingma, Doubao MarsCode, Tencent Cloud CodeBuddy, and similar tools | Use knowledge files, project rules, or reusable prompts | Upload the questionnaire and paste the generic prompt |
| Generic chat tools | Paste the prompt and questionnaire content manually | Usable, but less stable than a skill |

## WorkBuddy

WorkBuddy's documentation describes it as built on Claude Code and MCP, so the simplest setup is to install through the Claude Code skill path. See [WorkBuddy setup](workbuddy.md).

WorkBuddy docs: https://docs.work-buddy.ai/

Short version:

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/gtskevin/ob-scale-review.git ~/.claude/skills/ob-scale-review
```

Invoke:

```text
/ob-scale-review review this questionnaire Excel file.
```

## OpenCode

OpenCode works best through a custom command. See [OpenCode setup](opencode.md).

## Cursor / Windsurf / Trae / Qoder / Gemini CLI / Copilot

These tools do not all share the same skill mechanism, so this repository does not promise one fixed install directory for all of them. The most reliable approach is to use project instructions or custom rules.

### Option A: Clone the repository into your project

```bash
mkdir -p tools
git clone https://github.com/gtskevin/ob-scale-review.git tools/ob-scale-review
```

Then add this to your project instructions, rules, memories, custom instructions, or `AGENTS.md`:

```markdown
# OB Scale Review

When the user asks to review organizational behavior, management, HRM, leadership,
AI at work, or psychometrics survey questionnaires, read and follow:

`tools/ob-scale-review/SKILL.md`

When needed, consult:

- `tools/ob-scale-review/references/evaluation-rubric.md`
- `tools/ob-scale-review/references/adaptation-review.md`
- `tools/ob-scale-review/references/respondent-experience.md`
- `tools/ob-scale-review/references/output-formats.md`

Default to Chinese. Create one HTML review page with an executive summary,
P0-P3 issue list, modification suggestions, variable/scale names,
owner/action labels, and next-step recommendations. Do not output a long
Markdown report in the chat by default.
```

### Option B: Point the agent to GitHub

If your tool can browse or read GitHub, paste:

```text
Please read and follow the OB Scale Review workflow in this repository:
https://github.com/gtskevin/ob-scale-review

I need to review an organizational behavior/management questionnaire.
Default to Chinese. Output one HTML review page with an executive summary,
P0-P3 issue list, variable/scale names, modification suggestions,
owner/action labels, and next-step recommendations. Do not output a long
Markdown report by default.
```

## Generic Chat Tools

If the tool cannot install skills or read repository files:

1. Upload the questionnaire file or paste the variables and items.
2. Copy a prompt from [Prompt cookbook](prompt-cookbook.md).
3. Ask for a Chinese HTML review page.
4. If source items, references, respondents, or waves are missing, ask the agent to list missing information before judging adaptation quality.

This fallback is less reliable than a skill, but still useful for non-technical users.
