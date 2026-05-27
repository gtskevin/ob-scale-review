#!/usr/bin/env python3
"""Inspect an OB survey scale workbook and produce structured review inputs.

This script is intentionally conservative. It extracts workbook structure,
variable blocks, questionnaire items, placeholders, reverse-coded markers, and
basic consistency issues. The research judgment and final review should still be
done by the agent using the skill references.
"""

from __future__ import annotations

import argparse
import csv
import html
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter


PLACEHOLDER_RE = re.compile(
    r"(XX|xx|x月x日|X月X日|某某|姓名|name of school|name of organization|____+|【.*?】)"
)
REVERSE_RE = re.compile(r"\b(reverse|reverse[- ]?coded|reversed|反向|反向计分)\b", re.I)
TIME_RE = re.compile(r"^T\d+$", re.I)


@dataclass
class VariableRecord:
    sheet: str
    row: int
    english_name: str
    chinese_name: str
    item_count: str
    respondent: str
    wave: str
    questionnaire_id: str


@dataclass
class ItemRecord:
    sheet: str
    row: int
    wave: str
    respondent: str
    variable: str
    source_original: str
    current_chinese: str
    source_reference: str
    note: str
    block_start_row: int
    block_instruction: str


@dataclass
class IssueRecord:
    issue_id: str
    priority: str
    variable_name: str
    location: str
    issue_type: str
    current_text: str
    suggested_text: str
    rationale: str
    reviewer_action: str
    status: str = "待处理"


def clean(value: Any) -> str:
    if pd.isna(value):
        return ""
    return str(value).replace("\r", "\n").strip()


def norm(value: str) -> str:
    return re.sub(r"\s+", "", value or "").lower()


def read_workbook(path: Path) -> dict[str, pd.DataFrame]:
    return pd.read_excel(path, sheet_name=None, header=None, dtype=object)


def sheet_sample(df: pd.DataFrame, max_rows: int = 12, max_cols: int = 8) -> list[list[str]]:
    sample = df.iloc[: min(max_rows, len(df)), : min(max_cols, df.shape[1])]
    return [[clean(v) for v in row] for row in sample.to_numpy().tolist()]


def find_header_row(df: pd.DataFrame, required_terms: list[str]) -> int | None:
    for idx, row in df.iterrows():
        row_text = " ".join(clean(v) for v in row.tolist())
        if all(term in row_text for term in required_terms):
            return int(idx)
    return None


def map_headers(df: pd.DataFrame, header_row: int) -> dict[str, int]:
    headers = {}
    for col, value in enumerate(df.iloc[header_row].tolist()):
        text = clean(value)
        if text:
            headers[text] = col
    return headers


def col_for(headers: dict[str, int], candidates: list[str]) -> int | None:
    for cand in candidates:
        for header, idx in headers.items():
            if cand.lower() in header.lower():
                return idx
    return None


def extract_variables(sheets: dict[str, pd.DataFrame]) -> list[VariableRecord]:
    records: list[VariableRecord] = []
    for sheet_name, df in sheets.items():
        header_row = find_header_row(df, ["变量名称", "量表条目数"])
        if header_row is None:
            continue
        headers = map_headers(df, header_row)
        c_eng = col_for(headers, ["变量名称"])
        c_cn = col_for(headers, ["变量名称-中文", "中文"])
        c_count = col_for(headers, ["量表条目数", "条目数"])
        c_resp = col_for(headers, ["填写人", "评价者"])
        c_wave = col_for(headers, ["Time", "时间", "Wave"])
        c_qid = col_for(headers, ["问卷编号"])
        if c_cn is None:
            continue
        for row_idx in range(header_row + 1, len(df)):
            row = df.iloc[row_idx]
            first_text = " ".join(clean(v) for v in row.tolist())
            if "sum item num" in first_text.lower() or first_text.startswith("SUM"):
                break
            cn = clean(row.iloc[c_cn])
            eng = clean(row.iloc[c_eng]) if c_eng is not None else ""
            if not cn and not eng:
                continue
            records.append(
                VariableRecord(
                    sheet=sheet_name,
                    row=row_idx + 1,
                    english_name=eng,
                    chinese_name=cn,
                    item_count=clean(row.iloc[c_count]) if c_count is not None else "",
                    respondent=clean(row.iloc[c_resp]) if c_resp is not None else "",
                    wave=clean(row.iloc[c_wave]) if c_wave is not None else "",
                    questionnaire_id=clean(row.iloc[c_qid]) if c_qid is not None else "",
                )
            )
    return records


def is_questionnaire_header(row: list[str]) -> bool:
    row_text = " ".join(row)
    return "Measures" in row_text or "评价者" in row_text or "Source Reference" in row_text


def extract_items(sheets: dict[str, pd.DataFrame]) -> list[ItemRecord]:
    items: list[ItemRecord] = []
    for sheet_name, raw in sheets.items():
        header_row = None
        for idx, row in raw.iterrows():
            vals = [clean(v) for v in row.tolist()]
            if is_questionnaire_header(vals):
                header_row = int(idx)
                break
        if header_row is None:
            continue

        header = [clean(v) for v in raw.iloc[header_row].tolist()]
        col_map = {h: i for i, h in enumerate(header) if h}
        c_eval = col_for(col_map, ["评价者", "rater", "respondent"])
        c_var = col_for(col_map, ["Variables", "变量"])
        c_orig = col_for(col_map, ["original", "原始"])
        c_cn = col_for(col_map, ["Chinese", "中文", "adapted"])
        c_source = col_for(col_map, ["Source", "来源"])
        c_note = col_for(col_map, ["备注", "note"])
        if c_var is None or c_cn is None:
            continue

        current_wave = ""
        current_respondent = ""
        current_variable = ""
        current_source = ""
        current_note = ""
        current_instruction = ""
        block_start_row = 0

        for row_idx in range(header_row + 1, len(raw)):
            row = raw.iloc[row_idx]
            vals = [clean(v) for v in row.tolist()]
            respondent = clean(row.iloc[c_eval]) if c_eval is not None and c_eval < len(row) else ""
            variable = clean(row.iloc[c_var]) if c_var < len(row) else ""
            original = clean(row.iloc[c_orig]) if c_orig is not None and c_orig < len(row) else ""
            chinese = clean(row.iloc[c_cn]) if c_cn < len(row) else ""
            source = clean(row.iloc[c_source]) if c_source is not None and c_source < len(row) else ""
            note = clean(row.iloc[c_note]) if c_note is not None and c_note < len(row) else ""

            if variable and TIME_RE.match(variable):
                current_wave = variable.upper()
                continue

            # A block row usually has respondent/variable/source/instruction text.
            if variable and (respondent or source or (chinese and not original)):
                current_respondent = respondent or current_respondent
                current_variable = variable
                current_source = source
                current_note = note
                current_instruction = chinese
                block_start_row = row_idx + 1
                if original:
                    items.append(
                        ItemRecord(
                            sheet=sheet_name,
                            row=row_idx + 1,
                            wave=current_wave,
                            respondent=current_respondent,
                            variable=current_variable,
                            source_original=original,
                            current_chinese=chinese,
                            source_reference=current_source,
                            note=current_note,
                            block_start_row=block_start_row,
                            block_instruction=current_instruction,
                        )
                    )
                continue

            if original or chinese:
                items.append(
                    ItemRecord(
                        sheet=sheet_name,
                        row=row_idx + 1,
                        wave=current_wave,
                        respondent=current_respondent,
                        variable=current_variable,
                        source_original=original,
                        current_chinese=chinese,
                        source_reference=current_source,
                        note=current_note,
                        block_start_row=block_start_row,
                        block_instruction=current_instruction,
                    )
                )
    return items


def variable_key(text: str) -> str:
    text = re.sub(r"\s+", "", text)
    text = re.sub(r"[（）()]", "", text)
    return text.lower()


def respondent_alias(value: str) -> str:
    v = norm(value)
    if v in {"下属", "员工", "employee", "subordinate"}:
        return "员工"
    if v in {"领导", "主管", "leader", "supervisor"}:
        return "领导"
    return value.strip()


def build_issues(variables: list[VariableRecord], items: list[ItemRecord]) -> list[IssueRecord]:
    issues: list[IssueRecord] = []
    seen: set[tuple[str, str, str, str]] = set()

    def add(
        priority: str,
        variable_name: str,
        location: str,
        issue_type: str,
        current: str,
        suggested: str,
        rationale: str,
        action: str,
    ) -> None:
        key = (priority, variable_name, location, issue_type, current[:300])
        if key in seen:
            return
        seen.add(key)
        issues.append(
            IssueRecord(
                issue_id=f"I{len(issues) + 1:03d}",
                priority=priority,
                variable_name=variable_name,
                location=location,
                issue_type=issue_type,
                current_text=current,
                suggested_text=suggested,
                rationale=rationale,
                reviewer_action=action,
            )
        )

    for item in items:
        loc = f"{item.sheet}!row {item.row}"
        variable_name = item.variable.split("\n")[0] if item.variable else ""
        launch_text = "\n".join([item.variable, item.current_chinese, item.note, item.block_instruction])
        if PLACEHOLDER_RE.search(launch_text):
            if PLACEHOLDER_RE.search(item.block_instruction):
                placeholder_loc = f"{item.sheet}!row {item.block_start_row}"
                placeholder_text = "\n".join([item.variable, item.block_instruction])
            else:
                placeholder_loc = loc
                placeholder_text = launch_text
            add("P0", variable_name, placeholder_loc, "placeholder", placeholder_text[:500], "替换所有正式发放前占位符", "问卷中仍有占位符或内部模板文本。", "RA 可直接改")
        elif PLACEHOLDER_RE.search(item.source_original):
            add("P3", variable_name, loc, "source_placeholder", item.source_original, "通常无需修改原英文；确认中文改编已替换具体对象", "原英文成熟量表含模板占位符，这本身不是发放阻断，但审查时要确认中文已完成情境替换。", "仅提示")
        if REVERSE_RE.search(item.source_original):
            add("P3", variable_name, loc, "reverse_item", item.source_original, "确认中文已正向化且后续不再反向计分", "原题标注为反向题；按默认偏好可正向化，但需同步计分说明。", "研究者确认")
        if not item.current_chinese:
            add("P1", variable_name, loc, "missing_chinese", item.source_original, "补充中文题项或说明该行不是题项", "题项缺少当前中文文本。", "RA 可直接改")
        if not item.source_original and "自编" not in item.source_reference:
            add("P2", variable_name, loc, "missing_original", item.current_chinese, "补充英文原题，或标注为自编/新增题项", "非自编量表建议保留原英文以便审查翻译与改编。", "研究者确认")

    item_counts: dict[str, int] = {}
    respondent_by_item_var: dict[str, str] = {}
    wave_by_item_var: dict[str, str] = {}
    for item in items:
        key = variable_key(item.variable)
        if not key:
            continue
        item_counts[key] = item_counts.get(key, 0) + 1
        respondent_by_item_var.setdefault(key, item.respondent)
        wave_by_item_var.setdefault(key, item.wave)

    variable_groups: dict[str, list[VariableRecord]] = {}
    for var in variables:
        key_cn = variable_key(var.chinese_name or var.english_name)
        if key_cn:
            variable_groups.setdefault(key_cn, []).append(var)

    for key_cn, group in variable_groups.items():
        matched_keys = [
            item_key for item_key in item_counts
            if key_cn and (key_cn in item_key or item_key in key_cn)
        ]
        loc = "; ".join(f"{var.sheet}!row {var.row}" for var in group)
        label = " / ".join(v.chinese_name or v.english_name for v in group)
        if not matched_keys:
            add("P1", label, loc, "variable_missing_in_questionnaire", label, "确认该变量是否在问卷正文或另一个问卷版本中", "变量清单中有该变量，但问卷正文未能匹配到题项。", "研究者确认")
            continue
        expected = 0
        expected_known = True
        for var in group:
            try:
                expected += int(float(var.item_count))
            except ValueError:
                expected_known = False
        actual = sum(item_counts[matched_key] for matched_key in matched_keys)
        if expected_known and expected != actual:
            add("P1", label, loc, "item_count_mismatch", f"清单={expected}, 正文={actual}", "核对变量清单与问卷正文条目数", "条目数不一致会影响量表计分和问卷完整性。", "RA 可直接改")

        variable_respondents = {respondent_alias(v.respondent) for v in group if v.respondent}
        item_respondents = {respondent_alias(respondent_by_item_var.get(k, "")) for k in matched_keys if respondent_by_item_var.get(k, "")}
        if variable_respondents and item_respondents and not item_respondents.issubset(variable_respondents):
            add("P0", label, loc, "respondent_mismatch", f"清单={','.join(sorted(variable_respondents))}, 正文={','.join(sorted(item_respondents))}", "统一填写者/评价者设置", "配对问卷中填写者不一致会直接影响数据可用性。", "研究者确认")

        variable_waves = {norm(v.wave) for v in group if v.wave}
        item_waves = {norm(wave_by_item_var.get(k, "")) for k in matched_keys if wave_by_item_var.get(k, "")}
        if variable_waves and item_waves and not item_waves.issubset(variable_waves):
            add("P1", label, loc, "wave_mismatch", f"清单={','.join(sorted(variable_waves))}, 正文={','.join(sorted(item_waves))}", "统一时间点设置", "时间点不一致会影响纵向研究设计。", "研究者确认")

    return issues


def write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def human_sheet_title(name: str) -> str:
    safe = re.sub(r"[:\\/?*\[\]]", "_", name)
    return safe[:31] or "Sheet"


def as_rows(records: list[Any]) -> list[dict[str, Any]]:
    return [asdict(record) for record in records]


def add_table_sheet(
    workbook: Workbook,
    title: str,
    rows: list[dict[str, Any]],
    fieldnames: list[str],
    widths: dict[str, int] | None = None,
) -> None:
    ws = workbook.create_sheet(human_sheet_title(title))
    widths = widths or {}
    header_fill = PatternFill("solid", fgColor="1F4E78")
    header_font = Font(color="FFFFFF", bold=True)
    thin = Side(style="thin", color="D9E2F3")
    border = Border(bottom=thin)
    priority_fills = {
        "P0": PatternFill("solid", fgColor="F4CCCC"),
        "P1": PatternFill("solid", fgColor="FCE5CD"),
        "P2": PatternFill("solid", fgColor="FFF2CC"),
        "P3": PatternFill("solid", fgColor="D9EAD3"),
    }

    for col_idx, field in enumerate(fieldnames, start=1):
        cell = ws.cell(row=1, column=col_idx, value=field)
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        cell.border = border

    for row_idx, row in enumerate(rows, start=2):
        priority = str(row.get("priority", ""))
        for col_idx, field in enumerate(fieldnames, start=1):
            value = row.get(field, "")
            cell = ws.cell(row=row_idx, column=col_idx, value=value)
            cell.alignment = Alignment(vertical="top", wrap_text=True)
            if priority in priority_fills:
                if field == "priority":
                    cell.fill = priority_fills[priority]
                    cell.font = Font(bold=True)
                elif title.lower() == "issues":
                    cell.fill = priority_fills[priority]
        ws.row_dimensions[row_idx].height = 72

    ws.freeze_panes = "A2"
    if fieldnames:
        ws.auto_filter.ref = f"A1:{get_column_letter(len(fieldnames))}{max(1, len(rows) + 1)}"

    default_widths = {
        "issue_id": 12,
        "priority": 10,
        "location": 18,
        "issue_type": 20,
        "current_text": 58,
        "suggested_text": 46,
        "rationale": 48,
        "reviewer_action": 18,
        "status": 14,
        "sheet": 16,
        "row": 10,
        "english_name": 26,
        "chinese_name": 28,
        "item_count": 12,
        "respondent": 12,
        "wave": 10,
        "questionnaire_id": 14,
        "variable": 34,
        "source_original": 70,
        "current_chinese": 62,
        "source_reference": 52,
        "note": 42,
        "block_instruction": 54,
    }
    default_widths.update(widths)
    for col_idx, field in enumerate(fieldnames, start=1):
        ws.column_dimensions[get_column_letter(col_idx)].width = default_widths.get(field, 22)


def write_review_workbook(
    path: Path,
    summary: dict[str, Any],
    variables: list[VariableRecord],
    items: list[ItemRecord],
    issues: list[IssueRecord],
) -> None:
    wb = Workbook()
    ws = wb.active
    ws.title = "Summary"
    ws["A1"] = "OB Scale Review Inspection Summary"
    ws["A1"].font = Font(bold=True, size=14, color="1F4E78")
    summary_rows = [
        ("Workbook", summary["workbook"]),
        ("Sheet count", summary["sheet_count"]),
        ("Variable count", summary["variable_count"]),
        ("Item count", summary["item_count"]),
        ("Issue count", summary["issue_count"]),
    ]
    for idx, (key, value) in enumerate(summary_rows, start=3):
        ws.cell(row=idx, column=1, value=key).font = Font(bold=True)
        ws.cell(row=idx, column=2, value=value)
    start = len(summary_rows) + 5
    ws.cell(row=start, column=1, value="Priority").font = Font(bold=True)
    ws.cell(row=start, column=2, value="Count").font = Font(bold=True)
    for offset, level in enumerate(["P0", "P1", "P2", "P3"], start=1):
        ws.cell(row=start + offset, column=1, value=level)
        ws.cell(row=start + offset, column=2, value=summary["issue_counts_by_priority"].get(level, 0))
    ws.column_dimensions["A"].width = 24
    ws.column_dimensions["B"].width = 90
    ws.freeze_panes = "A3"

    issue_fields = [
        "issue_id",
        "priority",
        "location",
        "issue_type",
        "current_text",
        "suggested_text",
        "rationale",
        "reviewer_action",
        "status",
    ]
    variable_fields = list(asdict(variables[0]).keys()) if variables else [
        "sheet",
        "row",
        "english_name",
        "chinese_name",
        "item_count",
        "respondent",
        "wave",
        "questionnaire_id",
    ]
    item_fields = list(asdict(items[0]).keys()) if items else [
        "sheet",
        "row",
        "wave",
        "respondent",
        "variable",
        "source_original",
        "current_chinese",
        "source_reference",
        "note",
        "block_start_row",
        "block_instruction",
    ]

    add_table_sheet(wb, "Issues", as_rows(issues), issue_fields)
    add_table_sheet(wb, "Variables", as_rows(variables), variable_fields)
    add_table_sheet(wb, "Items", as_rows(items), item_fields)
    # Placeholder sheet for agent-generated suggestions; kept here so the workbook
    # remains the standard user-facing container after later review steps.
    suggestion_fields = [
        "variable",
        "respondent",
        "wave",
        "source_original",
        "current_chinese",
        "suggested_chinese",
        "reason",
        "priority",
    ]
    add_table_sheet(wb, "Suggestions", [], suggestion_fields)

    wb.save(path)


def write_html_table(path: Path, title: str, rows: list[dict[str, Any]], fieldnames: list[str]) -> None:
    labels = {
        "issue_id": "编号",
        "priority": "优先级",
        "variable_name": "变量/量表",
        "location": "位置",
        "issue_type": "问题类型",
        "current_text": "当前文本",
        "suggested_text": "建议处理",
        "rationale": "理由",
        "reviewer_action": "处理人/动作",
        "status": "状态",
    }
    type_labels = {
        "placeholder": "占位符未替换",
        "source_placeholder": "原英文模板占位符",
        "reverse_item": "反向题正向化提醒",
        "missing_chinese": "缺少中文题项",
        "missing_original": "缺少英文原题",
        "variable_missing_in_questionnaire": "变量清单与正文不匹配",
        "item_count_mismatch": "条目数不一致",
        "respondent_mismatch": "填写者不一致",
        "wave_mismatch": "时间点不一致",
    }
    style = """
body{font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;margin:28px;color:#1f2937}
h1{font-size:22px;margin:0 0 16px}
.hint{color:#64748b;margin:0 0 18px;font-size:13px}
table{border-collapse:collapse;width:100%;font-size:13px;line-height:1.45}
th{position:sticky;top:0;background:#1f4e78;color:white;text-align:left}
th,td{border:1px solid #d7dee8;padding:8px;vertical-align:top}
td{white-space:pre-wrap}
.P0{background:#f4cccc}.P1{background:#fce5cd}.P2{background:#fff2cc}.P3{background:#d9ead3}
.priority{font-weight:700;text-align:center;white-space:nowrap}
.id,.status{white-space:nowrap}
"""
    parts = [
        "<!doctype html><html><head><meta charset='utf-8'>",
        f"<title>{html.escape(title)}</title><style>{style}</style></head><body>",
        f"<h1>{html.escape(title)}</h1>",
        "<p class='hint'>颜色表示优先级：P0 发放阻断，P1 高风险，P2 中风险，P3 低风险/提示。</p>",
        "<table><thead><tr>",
        "".join(f"<th>{html.escape(labels.get(field, field))}</th>" for field in fieldnames),
        "</tr></thead><tbody>",
    ]
    for row in rows:
        priority = str(row.get("priority", ""))
        klass = priority if priority in {"P0", "P1", "P2", "P3"} else ""
        parts.append(f"<tr class='{klass}'>")
        for field in fieldnames:
            value = str(row.get(field, ""))
            if field == "issue_type":
                value = type_labels.get(value, value)
            cell_class = "priority" if field == "priority" else "id" if field == "issue_id" else "status" if field == "status" else ""
            parts.append(f"<td class='{cell_class}'>{html.escape(value)}</td>")
        parts.append("</tr>")
    parts.extend(["</tbody></table></body></html>"])
    path.write_text("".join(parts), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("workbook", type=Path)
    parser.add_argument("--outdir", type=Path, default=Path("scale_review_inspection"))
    parser.add_argument("--xlsx", action="store_true", help="Also create a formatted Excel review workbook.")
    args = parser.parse_args()

    args.outdir.mkdir(parents=True, exist_ok=True)
    sheets = read_workbook(args.workbook)
    variables = extract_variables(sheets)
    items = extract_items(sheets)
    issues = build_issues(variables, items)

    structure = []
    for sheet_name, df in sheets.items():
        nonempty_rows = int(df.dropna(how="all").shape[0])
        nonempty_cols = int(df.dropna(axis=1, how="all").shape[1])
        structure.append(
            {
                "sheet": sheet_name,
                "shape": [int(df.shape[0]), int(df.shape[1])],
                "nonempty_rows": nonempty_rows,
                "nonempty_cols": nonempty_cols,
                "sample": sheet_sample(df),
            }
        )

    summary = {
        "workbook": str(args.workbook),
        "sheet_count": len(sheets),
        "sheets": structure,
        "variable_count": len(variables),
        "item_count": len(items),
        "issue_count": len(issues),
        "issue_counts_by_priority": {
            level: sum(1 for issue in issues if issue.priority == level)
            for level in ["P0", "P1", "P2", "P3"]
        },
    }

    (args.outdir / "inspection_summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    (args.outdir / "variables.json").write_text(
        json.dumps([asdict(v) for v in variables], ensure_ascii=False, indent=2), encoding="utf-8"
    )
    (args.outdir / "items.json").write_text(
        json.dumps([asdict(i) for i in items], ensure_ascii=False, indent=2), encoding="utf-8"
    )
    (args.outdir / "issues.json").write_text(
        json.dumps([asdict(i) for i in issues], ensure_ascii=False, indent=2), encoding="utf-8"
    )

    write_csv(args.outdir / "variables.csv", [asdict(v) for v in variables], list(asdict(variables[0]).keys()) if variables else [])
    write_csv(args.outdir / "items.csv", [asdict(i) for i in items], list(asdict(items[0]).keys()) if items else [])
    issue_fields = list(asdict(issues[0]).keys()) if issues else [
        "issue_id",
        "priority",
        "location",
        "issue_type",
        "current_text",
        "suggested_text",
        "rationale",
        "reviewer_action",
        "status",
    ]
    write_csv(args.outdir / "issues.csv", [asdict(i) for i in issues], issue_fields)
    if args.xlsx:
        write_review_workbook(args.outdir / "scale_review_inspection.xlsx", summary, variables, items, issues)
    write_html_table(args.outdir / "issues.html", "量表问卷问题清单", [asdict(i) for i in issues], issue_fields)

    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
