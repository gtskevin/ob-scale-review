# 在 WorkBuddy 中使用 OB Scale Review

[English version](workbuddy.md)

WorkBuddy 官方文档说明它是基于 Claude Code 和 MCP 的个人 agent 框架。因此，OB Scale Review 最稳妥的安装方式是按 Claude Code Skill 路径安装。

WorkBuddy 官方文档：https://docs.work-buddy.ai/

## 不会用命令行的安装方式

打开 WorkBuddy，直接粘贴：

```text
请帮我把 https://github.com/gtskevin/ob-scale-review 安装为本地 Agent Skill。
因为我使用的是 WorkBuddy，请优先按 Claude Code Skill 方式安装到：
~/.claude/skills/ob-scale-review

安装完成后，请告诉我如何用 /ob-scale-review 检查问卷 Excel。
```

安装完成后，新开或刷新 WorkBuddy 会话，然后输入：

```text
/ob-scale-review 检查这个问卷 Excel。
```

## 命令行安装方式

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/gtskevin/ob-scale-review.git ~/.claude/skills/ob-scale-review
```

然后在 WorkBuddy/Claude Code 会话中使用：

```text
/ob-scale-review 检查这个问卷 Excel。
```

## 项目级安装

如果你希望某个研究项目固定使用这个 Skill，可以把它安装到项目目录中：

```bash
mkdir -p .claude/skills
git clone https://github.com/gtskevin/ob-scale-review.git .claude/skills/ob-scale-review
```

适合下面这些场景：

- 一个论文项目会反复修改问卷。
- RA 和老师在同一个项目文件夹里协作。
- 项目中有多轮问卷、配对问卷或多份 Excel。

## 使用提示词

完整审阅：

```text
/ob-scale-review 检查这个问卷 Excel。
重点看英文量表翻译、改编是否能向审稿人解释、反向题正向化与计分、
领导-员工配对、被试理解歧义和正式发放前阻断问题。
```

发放前终检：

```text
/ob-scale-review 做发放前终检。
只检查 P0/P1 问题：占位符、指导语、填写者不一致、时间窗口、
反应选项、配对 ID 风险和容易被不同被试理解不同的表达。
```

## 如果没有识别到 `/ob-scale-review`

可以让 WorkBuddy 自查：

```text
请检查 ~/.claude/skills/ob-scale-review/SKILL.md 是否存在。
如果存在，请读取这个 Skill，并按它的流程检查我提供的问卷文件。
如果当前会话无法自动识别，请告诉我是否需要重启或刷新 WorkBuddy。
```

如果仍然不能识别，可以使用通用方式：

```text
请读取这个仓库中的 SKILL.md：
https://github.com/gtskevin/ob-scale-review

然后按其中的 OB Scale Review 流程检查我上传的问卷。
请默认输出一个中文 HTML 审阅页，不要在聊天窗口输出很长的 Markdown 报告。
```
