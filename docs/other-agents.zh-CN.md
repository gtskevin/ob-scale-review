# 其他 Agent 工具

[English version](other-agents.md)

OB Scale Review 不只适用于 Codex 或 Claude Code。它的核心是一套可复用的量表和问卷审查流程，因此只要某个 agent 能读取本仓库的 `SKILL.md`、项目说明或自定义提示词，就可以使用。

对于中国用户，最现实的理解方式是：**能装 Skill 的就装 Skill；不能装 Skill 的，就让 agent 读取这个仓库作为审查说明。**

## 支持矩阵

| 工具 | 推荐接入方式 | 使用方式 |
|---|---|---|
| Codex | 安装到 `~/.codex/skills/ob-scale-review/` | `用 $ob-scale-review 检查这个问卷 Excel` |
| Claude Code | 安装到 `~/.claude/skills/ob-scale-review/` | `/ob-scale-review 检查这个问卷 Excel` |
| WorkBuddy / Work Buddy | 按 Claude Code Skill 路径安装 | `/ob-scale-review 检查这个问卷 Excel` |
| OpenCode | 创建自定义 command，指向本仓库 `SKILL.md` | `/ob-scale-review review ...` |
| Cursor | 在项目规则或说明文件中引用本仓库流程 | 让 Cursor 读取 `SKILL.md` 后审查问卷 |
| Windsurf | 在 rules / memories / 项目说明中引用本仓库流程 | 让 Windsurf 按 OB Scale Review 流程输出 HTML |
| Trae | 使用项目规则或自定义提示词 | 上传问卷并粘贴通用提示词 |
| Qoder | 使用项目说明或自定义提示词 | 上传问卷并粘贴通用提示词 |
| Gemini CLI | 通过 `AGENTS.md` 或项目上下文引用本仓库 | 让 Gemini 读取 `SKILL.md` 后审查 |
| GitHub Copilot CLI / coding agent | 通过仓库说明或项目指令引用本仓库 | 让 Copilot 按流程生成 HTML 审阅页 |
| 通义灵码、豆包 MarsCode、腾讯云 CodeBuddy 等 | 使用知识文件、项目规则或自定义提示词 | 上传问卷并粘贴通用提示词 |
| 普通聊天工具 | 手动粘贴提示词和问卷内容 | 可用，但稳定性低于 Skill |

## WorkBuddy

WorkBuddy 官方文档说明它基于 Claude Code 和 MCP，因此最简单的做法是按 Claude Code Skill 安装。详见：[WorkBuddy 安装说明](workbuddy.zh-CN.md)。

WorkBuddy 官方文档：https://docs.work-buddy.ai/

简版命令：

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/gtskevin/ob-scale-review.git ~/.claude/skills/ob-scale-review
```

使用：

```text
/ob-scale-review 检查这个问卷 Excel。
```

## OpenCode

OpenCode 推荐用自定义 command。详见：[OpenCode 使用说明](opencode.zh-CN.md)。

## Cursor / Windsurf / Trae / Qoder / Gemini CLI / Copilot

这些工具的 Skill 机制不完全相同，不建议在 README 里承诺某一个固定安装目录。更稳妥的做法是使用项目说明或自定义规则。

### 方式 A：把仓库放到项目里

```bash
mkdir -p tools
git clone https://github.com/gtskevin/ob-scale-review.git tools/ob-scale-review
```

然后在你的项目说明、rules、memories、custom instructions 或 `AGENTS.md` 中加入：

```markdown
# OB Scale Review

当用户要求检查组织行为学、管理学、HRM、领导力、AI at work 或心理测量问卷时，
请读取并遵循：

`tools/ob-scale-review/SKILL.md`

必要时参考：

- `tools/ob-scale-review/references/evaluation-rubric.md`
- `tools/ob-scale-review/references/adaptation-review.md`
- `tools/ob-scale-review/references/respondent-experience.md`
- `tools/ob-scale-review/references/output-formats.md`

默认输出中文。默认生成一个 HTML 审阅页，包含执行摘要、P0-P3 问题清单、
修改建议、变量/量表名、处理人/动作和下一步建议。不要在聊天窗口输出很长的 Markdown 报告。
```

### 方式 B：不克隆仓库，直接给 agent 链接

如果你的工具能联网或读取 GitHub，可以直接粘贴：

```text
请读取并遵循这个仓库中的 OB Scale Review 流程：
https://github.com/gtskevin/ob-scale-review

我要检查组织行为学/管理学问卷。请默认使用中文，输出一个 HTML 审阅页，
包括执行摘要、P0-P3 问题清单、变量/量表名、修改建议、处理人/动作和下一步建议。
不要默认输出很长的 Markdown 报告。
```

## 普通聊天工具

如果工具既不能安装 Skill，也不能读取仓库文件，就使用提示词手册：

1. 上传问卷文件，或粘贴变量和题项。
2. 从 [提示词手册](prompt-cookbook.zh-CN.md) 复制一个提示词。
3. 明确要求输出中文 HTML 审阅页。
4. 如果没有英文原题、来源、填写者或时间点，要让 agent 先列出缺失信息，不要直接判断改编质量。

这种方式不如 Skill 稳定，但对非技术用户仍然可用。
