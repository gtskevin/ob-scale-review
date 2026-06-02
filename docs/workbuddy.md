# Using Survey Scale Review with WorkBuddy

[中文版](workbuddy.zh-CN.md)

WorkBuddy's documentation describes it as a personal agent framework built on Claude Code and MCP. The most reliable setup is therefore to install Survey Scale Review through the Claude Code skill path.

WorkBuddy docs: https://docs.work-buddy.ai/

## Install Without Using the Command Line

Open WorkBuddy and paste:

```text
Please install https://github.com/gtskevin/survey-scale-review as a local Agent Skill.
Because I use WorkBuddy, prefer the Claude Code skill path:
~/.claude/skills/survey-scale-review

After installation, tell me how to use /survey-scale-review to review a questionnaire Excel file.
```

After installation, start or refresh the WorkBuddy session and type:

```text
/survey-scale-review review my questionnaire Excel file.
```

## Command-Line Install

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/gtskevin/survey-scale-review.git ~/.claude/skills/survey-scale-review
```

Then use it in a WorkBuddy/Claude Code session:

```text
/survey-scale-review review my questionnaire Excel file.
```

## Project-Level Install

If a specific research project will repeatedly use this skill, install it inside that project:

```bash
mkdir -p .claude/skills
git clone https://github.com/gtskevin/survey-scale-review.git .claude/skills/survey-scale-review
```

This is useful when:

- One paper project will revise the questionnaire repeatedly.
- RAs and the researcher work in the same project folder.
- The project includes multiple waves, paired questionnaires, or several Excel files.

## Prompt Examples

Full review:

```text
/survey-scale-review review this questionnaire Excel file.
Focus on translation quality, adapted scale defensibility, reverse-coded item handling,
leader-employee pairing, respondent ambiguity, and launch-blocking problems.
```

Pre-launch check:

```text
/survey-scale-review run a pre-launch check.
Only check P0/P1 issues: placeholders, instructions, respondent mismatch, time windows,
response options, pairing ID risk, and expressions that different respondents may interpret differently.
```

## If `/survey-scale-review` Is Not Recognized

Ask WorkBuddy to inspect the install:

```text
Please check whether ~/.claude/skills/survey-scale-review/SKILL.md exists.
If it exists, read this skill and use its workflow to review my questionnaire file.
If the current session cannot discover it automatically, tell me whether I need to restart or refresh WorkBuddy.
```

If discovery still fails, use the generic fallback:

```text
Please read SKILL.md from this repository:
https://github.com/gtskevin/survey-scale-review

Then follow the Survey Scale Review workflow to review my uploaded questionnaire.
Default to a Chinese HTML review page. Do not output a long Markdown report in the chat.
```
