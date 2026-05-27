# 其他 Agent 工具

[English version](other-agents.md)

OB Scale Review 原生支持 Codex 和 Claude Code。其他 agent 工具也可以通过兼容方式复用这套审查流程。

## 支持矩阵

| 工具 | 推荐安装方式 | 状态 |
|---|---|---|
| Codex | `~/.codex/skills/ob-scale-review/SKILL.md` | 原生支持 |
| Claude Code | `~/.claude/skills/ob-scale-review/SKILL.md` 或 `.claude/skills/` | 原生支持 |
| Work Buddy | 按 Claude Code Skill 安装，因为 Work Buddy 基于 Claude Code | 走 Claude Code 路径 |
| OpenCode | 创建自定义 command，指向本仓库的 `SKILL.md` | 兼容方案 |
| 支持 `AGENTS.md` 的 agent | 在项目说明中指向本仓库 | 兼容方案 |
| 普通聊天/agent 工具 | 粘贴提示词手册中的 prompt，并上传问卷 | 手动方案 |

## Work Buddy

Work Buddy 基于 Claude Code 和 MCP，因此最简单的做法是按 Claude Code Skill 安装：

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/gtskevin/ob-scale-review.git ~/.claude/skills/ob-scale-review
```

然后使用：

```text
/ob-scale-review review my questionnaire Excel file.
```

如果 Work Buddy 管理的是某个具体项目，也可以安装为项目级 skill：

```bash
mkdir -p .claude/skills
git clone https://github.com/gtskevin/ob-scale-review.git .claude/skills/ob-scale-review
```

## AGENTS.md 兼容方案

如果你的工具会读取 `AGENTS.md`，可以在项目中加入：

```markdown
# Survey Scale Review

When reviewing organizational behavior or management survey questionnaires, use the OB Scale Review workflow from:

`tools/ob-scale-review/SKILL.md`

Consult its references for evaluation rubric, adapted scale review, respondent experience, and output formats. If an Excel file is available and Python dependencies work, the helper script can be used:

`python tools/ob-scale-review/scripts/inspect_workbook.py <workbook-path> --outdir outputs/ob-scale-review`

If the script cannot run, infer the workbook structure from available file contents and continue the review.
```

## 通用手动方案

如果你的 agent 不支持 skills、commands 或项目说明文件：

1. 上传问卷文件，或提供文件路径。
2. 从 [prompt-cookbook.zh-CN.md](prompt-cookbook.zh-CN.md) 复制一个提示词。
3. 如果可以，同时提供 `SKILL.md` 和相关 reference 文件。
4. 要求它输出中文报告和带 P0-P3 优先级的 HTML 问题清单。

这种方式不如原生 Skill 稳定，但仍然有用。
