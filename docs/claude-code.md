# Using OB Scale Review with Claude Code

[中文版](claude-code.zh-CN.md)

Claude Code supports Agent Skills defined by a `SKILL.md` file. OB Scale Review is therefore usable in both Codex and Claude Code.

Official Claude Code skill documentation:

- https://code.claude.com/docs/en/skills

## Install as a Personal Claude Code Skill

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/gtskevin/ob-scale-review.git ~/.claude/skills/ob-scale-review
```

Then start Claude Code:

```bash
claude
```

Invoke the skill:

```text
/ob-scale-review review my questionnaire Excel file.
```

Claude Code uses the skill directory name as the slash command name, so the command is `/ob-scale-review`.

## Install as a Project Skill

If you want the skill available only inside one project repository:

```bash
mkdir -p .claude/skills
git clone https://github.com/gtskevin/ob-scale-review.git .claude/skills/ob-scale-review
```

Then run Claude Code from that project folder and use:

```text
/ob-scale-review review this questionnaire draft.
```

## Non-Technical Installation Prompt

If you do not use the command line, open Claude Code and paste:

```text
Please install this Agent Skill from https://github.com/gtskevin/ob-scale-review
as a personal Claude Code skill under ~/.claude/skills/ob-scale-review.
Then tell me how to invoke it.
```

## Claude Code Prompt Examples

Full review:

```text
/ob-scale-review review this Excel questionnaire.
Focus on translation quality, adapted scale defensibility, reverse-coded item handling,
leader-employee pairing, respondent ambiguity, and launch-blocking problems.
```

Pre-launch check:

```text
/ob-scale-review do a pre-launch check.
Do not rewrite every item; focus on placeholders, confusing instructions,
respondent mismatch, time windows, response options, and pairing risks.
```

Non-template file:

```text
/ob-scale-review inspect this questionnaire draft.
It may not follow the template. First infer variables, respondents, waves,
source items, translated items, and missing information.
```

## Notes

- Claude Code skills live under `~/.claude/skills/<skill-name>/SKILL.md` for personal use or `.claude/skills/<skill-name>/SKILL.md` for project use.
- Existing `.claude/commands/` workflows are still supported by Claude Code, but `SKILL.md` skills are the recommended format for reusable procedures with supporting files.
- OB Scale Review includes references, templates, and a helper script; keep the whole repository folder together when installing.
