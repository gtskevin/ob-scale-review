# Install and Update Guide

OB Scale Review will keep improving. Users who installed it earlier may continue using an older version unless they update it. Treat "update the skill" as a small pre-review step before serious questionnaire review.

## Easiest Option: Ask Your Agent to Update It

Paste this into Codex, Claude Code, WorkBuddy, or another local-file-capable agent:

```text
Please update the Agent Skill at https://github.com/gtskevin/ob-scale-review.
Check whether ~/.codex/skills/ob-scale-review and ~/.claude/skills/ob-scale-review exist.
If the directory is a git clone, run git pull --ff-only.
If it is not a git repository, back up the old directory and reinstall the latest version from GitHub.
When done, tell me the local commit and commit date.
```

After updating, start a new session and ask:

```text
Use $ob-scale-review to review my questionnaire Excel file.
```

## Command-Line Update

Codex users usually run:

```bash
git -C ~/.codex/skills/ob-scale-review pull --ff-only
```

Claude Code or WorkBuddy users usually run:

```bash
git -C ~/.claude/skills/ob-scale-review pull --ff-only
```

If you installed the skill in both locations, run both commands.

## Check Your Local Version

Run:

```bash
git -C ~/.codex/skills/ob-scale-review log -1 --oneline --date=short
git -C ~/.claude/skills/ob-scale-review log -1 --oneline --date=short
```

Or ask your agent:

```text
Please check my local ob-scale-review skill version. Tell me the current commit, commit date, and whether it needs updating.
```

Newer formal review reports should include the local commit and date in the footer when available.

## If You Did Not Install with git clone

Some users may have downloaded a ZIP, copied a folder, or asked an agent to place files manually. In that case, `git pull` will not work.

Recommended steps:

1. Back up the old directory, for example by renaming it to `ob-scale-review.backup`.
2. Reinstall the latest version from GitHub.
3. Start a new agent session.

Codex path:

```bash
mv ~/.codex/skills/ob-scale-review ~/.codex/skills/ob-scale-review.backup
git clone https://github.com/gtskevin/ob-scale-review.git ~/.codex/skills/ob-scale-review
```

Claude Code/WorkBuddy path:

```bash
mv ~/.claude/skills/ob-scale-review ~/.claude/skills/ob-scale-review.backup
git clone https://github.com/gtskevin/ob-scale-review.git ~/.claude/skills/ob-scale-review
```

## Recommendation for Teams

If you recommend this skill to students, RAs, or collaborators, give them these two instructions:

```text
Before serious questionnaire review, ask your agent to update ob-scale-review.
After updating, make sure the report footer shows the local commit and date.
```

This cannot force every installed copy to update automatically, but it substantially reduces the risk that collaborators continue using an old version.
