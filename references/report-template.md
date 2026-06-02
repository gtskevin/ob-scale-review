# HTML Review Page Content Template

Use Chinese.

The default user-facing output should be an HTML review page, not a long Markdown report pasted into chat. The following structure can be used as the content model for that HTML page. If a Markdown source file is used to render HTML, keep it as an editable source and link the rendered HTML to the user.

```markdown
# 量表与问卷检查报告

**状态：** 待评审

> ⚠️ **免责声明**
>
> 本报告由 AI 基于当前问卷文件中的英文原题、中文题项、来源信息和问卷结构生成，属于研究辅助判断。AI 可以帮助发现翻译漂移、改编风险、指导语问题和被试理解风险，但不能替代研究者和领域专家的人工审核。

## 0. 版本与更新

Place this near the top, before the dashboard. It should be useful for non-technical users.

| 项目 | 内容 |
|---|---|
| Survey Scale Review 本地版本 | commit 短 SHA，如果可获得 |
| commit 日期 | 如果可获得 |
| 检查新版本 | Link/button: `检查新版本` |
| 更新方式 | 复制下面提示词，发给正在使用的 Agent |

If local commit SHA is known, `检查新版本` should link to:

`https://github.com/gtskevin/survey-scale-review/compare/<local-sha>...main`

If local commit SHA is unknown, link to:

`https://github.com/gtskevin/survey-scale-review/commits/main`

Use this copyable prompt:

```text
请帮我更新 https://github.com/gtskevin/survey-scale-review 这个 Agent Skill。
请检查 ~/.codex/skills/survey-scale-review 和 ~/.claude/skills/survey-scale-review 是否存在。
如果目录是 git clone 安装的，请运行 git pull --ff-only 更新。
如果不是 git 仓库，请先备份旧目录，再从 GitHub 重新安装最新版。
完成后告诉我当前本地 commit 和日期。
```

When creating custom HTML, make this a visually compact card with two obvious actions:

- `检查新版本`: opens the GitHub compare/commits link in the browser.
- `复制更新提示词`: copies the prompt above to clipboard. If clipboard JavaScript is blocked, show the prompt in a selectable text box.

Add a short note: 点击“检查新版本”只会打开 GitHub 页面；本地更新仍需要把提示词发给 Agent 执行。

## 1. 先看这里：10 分钟决策版

Use a compact dashboard table near the top so readers can quickly decide what to do. Keep this front section short.

| 指标 | 数量/结论 | 说明 |
|---|---:|---|
| 发放建议 |  | 不建议直接发放 / 修改后可发放 / 可发放 |
| P0 发放阻断 |  | 必须先修 |
| P1 高风险 |  | 研究者优先确认 |
| P2 中风险 |  | 建议修 |
| RA 可直接处理 |  | 格式、占位符、明显措辞 |
| 研究者确认 |  | 构念、改编、层级选择 |
| 建议专家复核 |  | 高度改编、自编量表 |

- 总体建议：
- 先做哪几件事：
- 哪些需要导师/专家确认：
- 建议修改版是否已包含：

## 2. 给新手的最小说明

Explain only the concepts needed to understand this report. Use hover glossary syntax sparingly:

- `{{回译|把中文题项再译回英文，用来检查是否仍保留英文原题核心含义。}}`
- `{{隐性改编|用户没有明说改编，但题项对象、语境、视角或构念已经发生变化。}}`
- `{{referent|题项中“我、我们、团队、部门、领导”等词具体指向谁。}}`
- `{{level of analysis|变量属于个体、团队、部门还是组织层级。不同层级会影响研究设计和统计分析。}}`
- `{{指导语污染|指导语提前告诉被试变量定义或研究意图，可能改变他们的回答。}}`

If creating custom HTML instead of relying on `pretty-doc`, implement glossary explanations as instant custom tooltips, not browser-native `title` tooltips. Tooltip text should appear immediately on hover/focus and use readable body text around 14px.

## 3. 立即处理清单

| 优先级 | 位置 | 问题 | 为什么重要 | 谁来处理 | 建议 |
|---|---|---|---|---|---|

## 4. 研究者必须确认的决策

List 3-6 decisions that determine how the questionnaire should be revised.

| 决策 | 为什么重要 | 推荐处理 |
|---|---|---|

## 5. 建议修改版：只列关键修改

| 编号 | 优先级 | 证据状态 | 位置 | 问题 | 为什么重要 | 谁来处理 | 建议 |
|---|---|---|---|---|---|---|---|

## 6. 量表级简短诊断

Use one compact row per scale. Do not paste every item unless necessary.

| 量表 | 类型判断 | 最主要风险 | 处理建议 |
|---|---|---|---|

## 7. 方法写作提示

Provide only short method-writing notes for the few most consequential adaptations.

## 8. 可选附录：详细问题索引

Use this only when useful. Keep row-by-row details in an appendix or separate file.

## 9. 免责声明

Repeat this prominently at the end of every formal report:

> ⚠️ **免责声明**
>
> 本报告由 AI 基于当前问卷文件中的英文原题、中文题项、来源信息和问卷结构生成，属于研究辅助判断。AI 可以帮助发现翻译漂移、改编风险、指导语问题和被试理解风险，但不能完全替代研究者和领域专家的人工审核。正式发放或投稿前，建议由熟悉构念、研究设计和目标被试群体的专家再次复核，必要时进行预测试、回译和信效度检验。

## 10. 下一步

如果需要，我可以把上面的建议修改版另存为 Excel 对照表，保留原始列并在右侧增加建议中文、修改理由、审稿解释和是否采纳列。
```
