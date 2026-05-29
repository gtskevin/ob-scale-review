# 安装与更新指南

OB Scale Review 会持续优化。已经安装过的用户如果不更新，确实可能继续使用旧版本。因此，推荐把“更新 Skill”当成正式审问卷前的一个小步骤。

## 最简单做法：让 Agent 帮你更新

把下面这段话发给 Codex、Claude Code、WorkBuddy 或其他能操作本地文件的 Agent：

```text
请帮我更新 https://github.com/gtskevin/ob-scale-review 这个 Agent Skill。
请检查 ~/.codex/skills/ob-scale-review 和 ~/.claude/skills/ob-scale-review 是否存在。
如果目录是 git clone 安装的，请运行 git pull --ff-only 更新。
如果不是 git 仓库，请先备份旧目录，再从 GitHub 重新安装最新版。
完成后告诉我当前本地 commit 和日期。
```

更新后，重新开启一个会话，再使用：

```text
用 $ob-scale-review 检查这个问卷 Excel。
```

## 命令行更新

Codex 用户通常运行：

```bash
git -C ~/.codex/skills/ob-scale-review pull --ff-only
```

Claude Code 或 WorkBuddy 用户通常运行：

```bash
git -C ~/.claude/skills/ob-scale-review pull --ff-only
```

如果你同时安装在两个目录，可以两个命令都运行。

## 如何确认自己是不是新版？

在命令行运行：

```bash
git -C ~/.codex/skills/ob-scale-review log -1 --oneline --date=short
git -C ~/.claude/skills/ob-scale-review log -1 --oneline --date=short
```

也可以直接问 Agent：

```text
请检查我本地 ob-scale-review Skill 的版本，告诉我当前 commit、日期，以及是否需要更新。
```

新版正式评审报告会尽量在页脚显示本地 commit 和日期，方便你判断报告来自哪个版本。

## 如果当初不是 git clone 安装的

有些用户可能是下载 ZIP、复制文件夹，或者让 Agent 手工放进 skills 目录。这种情况下 `git pull` 不能更新。

推荐做法：

1. 先备份旧目录，例如改名为 `ob-scale-review.backup`。
2. 从 GitHub 重新安装最新版。
3. 重新开启 Agent 会话。

Codex 路径：

```bash
mv ~/.codex/skills/ob-scale-review ~/.codex/skills/ob-scale-review.backup
git clone https://github.com/gtskevin/ob-scale-review.git ~/.codex/skills/ob-scale-review
```

Claude Code/WorkBuddy 路径：

```bash
mv ~/.claude/skills/ob-scale-review ~/.claude/skills/ob-scale-review.backup
git clone https://github.com/gtskevin/ob-scale-review.git ~/.claude/skills/ob-scale-review
```

## 给老师或团队的建议

如果你把这个 Skill 推荐给学生、RA 或合作者，可以同时告诉他们两句话：

```text
正式审问卷前，先让 Agent 更新 ob-scale-review。
更新后，请让报告页脚显示本地 commit 和日期，便于追踪使用的是哪个版本。
```

这不能强制所有人自动更新，但能显著降低“大家还在用旧版”的风险。
