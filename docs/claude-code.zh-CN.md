# 在 Claude Code 中使用 Survey Scale Review

Claude Code 支持基于 `SKILL.md` 的 Agent Skills，因此 Survey Scale Review 可以同时用于 Codex、Claude Code，以及按 Claude Code Skill 路径工作的 WorkBuddy。

Claude Code 官方 Skills 文档：

- https://code.claude.com/docs/en/skills

[English version](claude-code.md)

## 非技术安装方式

如果你不会使用命令行，可以打开 Claude Code，直接粘贴：

```text
请帮我把 https://github.com/gtskevin/survey-scale-review 安装为 Claude Code 个人技能，
安装位置是 ~/.claude/skills/survey-scale-review。
安装完成后告诉我如何调用它。
```

## 命令行安装为个人 Skill

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/gtskevin/survey-scale-review.git ~/.claude/skills/survey-scale-review
```

然后启动 Claude Code：

```bash
claude
```

使用：

```text
/survey-scale-review 检查这个问卷 Excel。
```

Claude Code 使用技能目录名作为 slash command，所以这里是 `/survey-scale-review`。

## 安装为项目 Skill

如果你只想在某个研究项目文件夹中使用：

```bash
mkdir -p .claude/skills
git clone https://github.com/gtskevin/survey-scale-review.git .claude/skills/survey-scale-review
```

然后在该项目目录中启动 Claude Code，并使用：

```text
/survey-scale-review 检查这个问卷草稿。
```

## Claude Code 示例提示词

完整审阅：

```text
/survey-scale-review 检查这个 Excel 问卷。
重点看英文量表翻译、改编是否能向审稿人解释、反向题正向化与计分、
领导-员工配对、被试理解歧义和正式发放前阻断问题。
```

发放前终检：

```text
/survey-scale-review 做发放前终检。
不要大幅重写所有条目，只检查占位符、指导语、填写者不一致、
时间窗口、反应选项和配对风险。
```

非模板文件：

```text
/survey-scale-review 检查这个问卷草稿。
它不是模板格式，请先推断变量、填写者、时间点、来源和条目结构，
再告诉我哪些信息缺失。
```

## 注意事项

- Claude Code 个人技能位置是 `~/.claude/skills/<skill-name>/SKILL.md`。
- 项目级技能位置是 `.claude/skills/<skill-name>/SKILL.md`。
- Claude Code 也支持旧式 `.claude/commands/`，但这里推荐使用 `SKILL.md` 技能格式。
- 安装时请保留整个仓库文件夹，因为 Survey Scale Review 包含 references、templates、examples 和脚本。
