# Evaluation Rubric

## Severity

| Level | Name | Definition | Action |
|---|---|---|---|
| P0 | 发放阻断 | Causes wrong respondent, failed pairing, unusable data, or scoring conflict | Must fix before launch |
| P1 | 高风险 | Threatens translation equivalence, adaptation validity, reviewer defensibility, or major comprehension | Strongly fix before launch |
| P2 | 中风险 | Affects clarity, fluency, respondent experience, or minor measurement quality | Should fix |
| P3 | 低风险 | Formatting, punctuation, source style, minor wording polish | Batch optimize |

## Scale type logic

| Type | Indicators | Review focus |
|---|---|---|
| Mature direct translation | Source and original items present; Chinese item maps directly to original | Translation equivalence, clarity, response-option fit |
| Mature adapted scale | Source item is reused with changed object/context/referent | Adaptation defensibility and reviewer explanation |
| Self-developed scale | Source missing or marked self-developed; no original English item | Construct coverage, item-writing errors, social desirability, validation needs |
| Highly adapted scale | Source exists but item direction/object/meaning is substantially changed or new items are added | Treat like adaptation plus self-developed risk |
| Mixed scale | Some items adapted, some new | Flag new items and explain why they belong |

## Reverse-coded source items

Default preference: source reverse-coded items may be rewritten as positive Chinese items.

Check:

- Is the original reverse-coded marker visible, e.g. `Reverse coded`, `reverse`, `R`?
- Has the Chinese item been positive-worded?
- Does the positive wording accurately represent the opposite direction?
- Are scoring notes updated so the item is not reverse-scored again?
- Are all items in the scale aligned so higher scores mean more of the construct?

Flag as:

- P0/P1 if positive wording conflicts with scoring notes.
- P1 if item direction is unclear.
- P2 if negative wording is retained but hard to understand.
- P3 if only a method-note reminder is needed.

## Direct mature scale checks

Do not re-evaluate construct coverage. Check:

- English-Chinese semantic equivalence.
- Stable subject and referent.
- Accurate intensity and time qualifiers.
- Natural Chinese for employees/managers.
- Response option compatibility.
- No missing item, source, or placeholder.

When both English and Chinese items are available, do not stop at general fluency. For each row, identify the English item's core meaning and compare whether the Chinese adds, omits, or changes any measurement content. Large translation drift is P1 even if the Chinese sentence sounds natural.

Common P1 translation failures:

| Failure | Why it matters |
|---|---|
| `learn` becomes `熟练使用` | Changes learning confidence into actual skilled use |
| `appropriately use/learn` becomes only `熟练/高效使用` | Drops appropriateness and changes intensity |
| `inspires me` becomes `使我深受启发` | May change motivational inspiration into intellectual enlightenment |
| `benefits` becomes improved performance/efficiency | Adds outcome content not in the source |
| Top managers/direct supervisor/team members are swapped without explanation | Changes referent and possibly level of analysis |

## Self-developed and highly adapted item-writing checks

Check these common errors:

| Error | Meaning | Example pattern | Risk |
|---|---|---|---|
| Double-barreled item | One item asks multiple things | "use AI to improve efficiency and innovation" | Respondent may agree with only one part |
| Leading item | Wording nudges a desirable answer | "reasonably use AI to improve performance" | Inflates agreement |
| Loaded/moralized wording | Wording carries moral judgment | "falsely exaggerate AI use" | Defensive responding |
| Ambiguous referent | Subject/object/group unclear | "my team", "leader", "AI" | Different respondents answer different targets |
| Vague time frame | Period is unclear | "recently", "often" | Inconsistent recall |
| Frequency-agreement mismatch | Item asks frequency but uses agreement options | "I often..." with agree-disagree anchors | Response scale mismatch |
| Absolutist wording | Uses always/never/completely | "I always rely on AI" | Low endorsement and poor variance |
| Double negative | Hard to parse | "do not think AI cannot..." | Comprehension error |
| Unsupported premise | Assumes an experience not everyone has | "after AI training..." | Some respondents cannot answer |
| Formative-reflective confusion | Causes, behaviors, and outcomes mixed as reflective indicators | "I use AI, so performance improves" | Invalid measurement model |
| Causal item wording | Item states model hypothesis | "leader AI advocacy makes me engaged" | Contaminates hypothesis test |
| Construct contamination | Item includes another model variable | AI self-efficacy item says "I use AI more often" | Inflated relationships |
| Overbroad scenario | Combines too many tasks/roles | "communication, decisions, and innovation" | Unclear target behavior |
| Redundant near-synonyms | Multiple items repeat the same wording | all items say "make others think I use AI" | Weak content breadth |
| Academic wording | Terms are not natural to employees | "task-technology fit" | Poor comprehension |

For these scales, separate language polish from psychometric risk. Recommend pretest, expert review, EFA/CFA, reliability, convergent/discriminant validity, and criterion validity only when relevant.

## Instruction contamination checks

Instructions can create measurement bias when they explain the construct too directly. Flag instruction text when it:

- Gives a mini-theory of the variable before the items.
- Defines the variable in terms that overlap strongly with item content.
- Tells respondents what to include or exclude in a way that reveals the intended construct.
- Uses phrases like `这里关注的是...而不是...`, `以下陈述描述的是...`, or long conceptual definitions before sensitive or theoretically central variables.

Use P1 when the instruction is likely to prime the construct or demand characteristics. Use P2 when the instruction is useful but too leading or too academic and can be shortened.

Prefer neutral task framing:

- Use a short time window, respondent target, and response anchor.
- Avoid naming the latent variable unless the label is necessary for comprehension.
- Define broad terms such as `AI工具` only enough to prevent confusion, not enough to reveal the hypothesis.

## Leadership and level-of-analysis checks

Leadership, team, and paired survey items require explicit referent checks.

| Wording contrast | Risk |
|---|---|
| `我的领导劝我` vs `我的领导劝我们` | Individual-level perception vs team-level/shared target |
| `直属领导` vs `高层领导/领导层` | Direct supervisor construct may be confused with top management climate |
| `团队成员` vs `部门员工` | Work group, department, and organization-level targets may differ |
| `该员工对本部门贡献很大` | Leaders may interpret department as team, formal department, or whole unit |

Flag as P1 when the referent shift changes the theoretical level of analysis or the source scale's target. Flag as P2 when the target can be clarified with wording.
