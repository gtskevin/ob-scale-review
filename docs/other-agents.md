# Other Agent Tools

[中文版](other-agents.zh-CN.md)

OB Scale Review is packaged natively for Codex and Claude Code. Other agent tools can still reuse the same workflow through compatibility bridges.

## Support Matrix

| Tool | Recommended setup | Status |
|---|---|---|
| Codex | `~/.codex/skills/ob-scale-review/SKILL.md` | Native |
| Claude Code | `~/.claude/skills/ob-scale-review/SKILL.md` or `.claude/skills/` | Native |
| Work Buddy | Install as a Claude Code skill, because Work Buddy is built on Claude Code | Claude Code path |
| OpenCode | Create a custom command that points to this repository's `SKILL.md` | Compatibility bridge |
| Other agents with `AGENTS.md` support | Add a short project instruction pointing to this repository | Compatibility bridge |
| Generic chat/agent tools | Paste the relevant prompt cookbook entry and upload the questionnaire | Manual fallback |

## Work Buddy

Work Buddy is built on Claude Code and MCP, so the simplest path is to install OB Scale Review as a Claude Code skill:

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/gtskevin/ob-scale-review.git ~/.claude/skills/ob-scale-review
```

Then use the same Claude Code invocation:

```text
/ob-scale-review review my questionnaire Excel file.
```

If Work Buddy manages a project workspace for you, a project-level install may also be appropriate:

```bash
mkdir -p .claude/skills
git clone https://github.com/gtskevin/ob-scale-review.git .claude/skills/ob-scale-review
```

## AGENTS.md Fallback

For tools that read `AGENTS.md`, add a short project instruction:

```markdown
# Survey Scale Review

When reviewing organizational behavior or management survey questionnaires, use the OB Scale Review workflow from:

`tools/ob-scale-review/SKILL.md`

Consult its references for evaluation rubric, adapted scale review, respondent experience, and output formats. If an Excel file is available and Python dependencies work, the helper script can be used:

`python tools/ob-scale-review/scripts/inspect_workbook.py <workbook-path> --outdir outputs/ob-scale-review`

If the script cannot run, infer the workbook structure from available file contents and continue the review.
```

## Generic Manual Fallback

If your agent does not support skills, commands, or project instruction files:

1. Upload or point it to the questionnaire file.
2. Paste a prompt from [prompt-cookbook.md](prompt-cookbook.md).
3. If possible, also provide `SKILL.md` and the relevant reference file.
4. Ask it to output a Chinese report and an HTML issue table with P0-P3 priorities.

This is less reliable than native skill support but still useful.
