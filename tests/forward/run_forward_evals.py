#!/usr/bin/env python3
"""Run isolated live Codex evaluations for the local paper-review Skill."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import tempfile
import time
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
FIXTURES = Path(__file__).resolve().parent / "fixtures"
SKILL = ROOT / "paper-review" / "SKILL.md"
SOURCE_CODEX_HOME = Path(os.environ.get("CODEX_HOME", Path.home() / ".codex"))


@dataclass(frozen=True)
class Case:
    case_id: str
    files: tuple[str, ...]
    prompt: str
    mode: str


CASES = (
    Case(
        "FWD-01",
        ("clean-theoretical.md",),
        "Use $paper-review to review clean-theoretical.md. "
        "Write a Simplified Chinese Markdown review report to paper-reviews/. "
        "Do not modify the manuscript.",
        "clean_review",
    ),
    Case(
        "FWD-02",
        ("problematic-empirical.md",),
        "Use $paper-review to review problematic-empirical.md. "
        "Write a Simplified Chinese Markdown review report to paper-reviews/. "
        "Do not modify the manuscript.",
        "detailed_review",
    ),
    Case(
        "FWD-03",
        ("recheck-prior-review.md", "recheck-revised.md"),
        "Use $paper-review to recheck recheck-revised.md against "
        "recheck-prior-review.md. Write a Simplified Chinese Markdown delta review "
        "to paper-reviews/. Do not modify either input file.",
        "delta_review",
    ),
    Case(
        "FWD-04",
        ("polish-source.md",),
        "Use $paper-review to polish the full manuscript polish-source.md "
        "section by section using the built-in workflow only; do not use optional external "
        "Skills. No separate author writing sample is available. Do not "
        "overwrite the source. Create a new Markdown manuscript and companion report "
        "under paper-revisions/ while preserving every fact, number, variable, equation, "
        "citation, label, and claim boundary.",
        "protected_polish",
    ),
    Case(
        "FWD-05",
        ("ai-trace-clean-methods.md",),
        "Use $paper-review to review ai-trace-clean-methods.md with the default workflow. "
        "Write a Simplified Chinese Markdown review report to paper-reviews/. "
        "Do not modify the manuscript and do not perform external research.",
        "ai_trace_lightweight",
    ),
    Case(
        "FWD-06",
        ("ai-trace-problematic.md",),
        "Use $paper-review to perform a detailed AI-trace candidate audit of "
        "ai-trace-problematic.md. List both confirmed and contextually acceptable "
        "candidates, inspect underlying evidence and citation risks, and do not infer "
        "authorship or output an AI probability. Write a Simplified Chinese Markdown "
        "review report to paper-reviews/. Do not modify the manuscript or search externally.",
        "ai_trace_detailed",
    ),
)


def file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def copy_inputs(case: Case, workspace: Path) -> dict[str, str]:
    hashes: dict[str, str] = {}
    for name in case.files:
        source = FIXTURES / name
        target = workspace / name
        shutil.copy2(source, target)
        hashes[name] = file_hash(target)
    return hashes


def prepare_isolated_codex_home(root: Path) -> tuple[Path, str]:
    auth_source = SOURCE_CODEX_HOME / "auth.json"
    if not auth_source.exists():
        raise SystemExit(f"Codex authentication file not found: {auth_source}")

    codex_home = root / "codex-home"
    skill_target = codex_home / "skills" / "paper-review"
    skill_target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(SKILL.parent, skill_target)
    (codex_home / "auth.json").symlink_to(auth_source)

    source_hash = file_hash(SKILL)
    copied_hash = file_hash(skill_target / "SKILL.md")
    if copied_hash != source_hash:
        raise SystemExit("Isolated Skill copy does not match the repository Skill.")
    return codex_home, copied_hash


def read_markdown_files(directory: Path) -> list[Path]:
    if not directory.exists():
        return []
    return sorted(path for path in directory.rglob("*.md") if path.is_file())


def review_report_files(directory: Path) -> list[Path]:
    return [path for path in read_markdown_files(directory) if path.name.startswith("review-")]


def combined_text(paths: list[Path]) -> str:
    return "\n\n".join(path.read_text(encoding="utf-8", errors="replace") for path in paths)


def contains_any(text: str, choices: tuple[str, ...]) -> bool:
    return any(choice in text for choice in choices)


def evaluate(case: Case, workspace: Path, original_hashes: dict[str, str]) -> list[dict[str, object]]:
    checks: list[dict[str, object]] = []

    def check(name: str, passed: bool, detail: str) -> None:
        checks.append({"name": name, "passed": passed, "detail": detail})

    for name, expected_hash in original_hashes.items():
        actual_hash = file_hash(workspace / name)
        check(f"source_unchanged:{name}", actual_hash == expected_hash, actual_hash)

    all_review_files = read_markdown_files(workspace / "paper-reviews")
    review_files = review_report_files(workspace / "paper-reviews")
    revision_files = read_markdown_files(workspace / "paper-revisions")

    if case.mode != "protected_polish":
        check("review_report_created", bool(review_files), str([p.name for p in review_files]))
        check(
            "review_output_hygiene",
            all_review_files == review_files,
            f"all={ [p.name for p in all_review_files] }, reports={ [p.name for p in review_files] }",
        )
        text = combined_text(review_files)
    else:
        check("revision_artifacts_created", len(revision_files) >= 2, str([p.name for p in revision_files]))
        text = combined_text(revision_files)

    if case.mode == "clean_review":
        check("text_quality_section", "文本质量" in text, "expected lightweight text-quality result")
        check(
            "lightweight_only",
            "未发现影响可读性、术语一致性或稿件语体连贯性的明显文本质量问题" in text,
            "expected the default one-sentence result",
        )
        check("no_detailed_t_findings", "T-01" not in text, "clean prose should not force detailed audit")
    elif case.mode == "detailed_review":
        required = {
            "scientific_finding": "S-01" in text,
            "text_finding": "T-01" in text,
            "severity_and_certainty": "严重程度" in text and "判断确定性" in text,
            "action_plan": "修改行动表" in text and "是否阻塞提交" in text,
            "causal_boundary": contains_any(text, ("因果", "导致", "识别")),
            "significance_mismatch": "0.08" in text or "显著性" in text,
            "variable_or_sample_mismatch": contains_any(text, ("数字化能力", "变量", "N=20", "样本量")),
        }
        for name, passed in required.items():
            check(name, passed, name)
    elif case.mode == "delta_review":
        check("preserves_prior_id", "S-01" in text, "prior finding ID should remain traceable")
        check("resolved_status", "Resolved" in text, "fixed causal claim should be resolved")
        check(
            "new_or_open_status",
            contains_any(text, ("New", "Still Open", "Downgraded", "Needs External Verification")),
            "appendix sample mismatch should remain actionable",
        )
        check(
            "status_matrix",
            "| Finding ID | 原问题 | 当前位置 | 状态 | 下一步动作 |" in text,
            "expected mandatory delta matrix",
        )
        check("mapped_id_not_replaced", "D-01" not in text, "mapped prior IDs must be preserved")
        check("delta_action_plan", "修改行动表" in text, "open delta items need an action plan")
    elif case.mode == "protected_polish":
        polished = [p for p in revision_files if "polished" in p.name]
        reports = [p for p in revision_files if "report" in p.name]
        check("polished_copy_created", bool(polished), str([p.name for p in polished]))
        check("companion_report_created", bool(reports), str([p.name for p in reports]))
        polished_text = combined_text(polished)
        for token in ("128", "0.37", "0.012", "DIG", "ROA", "[1]", "Equation (1)"):
            check(f"preserves:{token}", token in polished_text, token)
        report_text = combined_text(reports)
        check(
            "honest_style_baseline",
            contains_any(report_text, ("manuscript-consistent", "论文一致性", "中性学术")),
            "no confirmed author sample was supplied",
        )
        check(
            "invariant_report",
            contains_any(report_text, ("Passed", "Needs verification", "事实", "数字", "引用")),
            "companion report should record preservation checks",
        )
    elif case.mode == "ai_trace_lightweight":
        check("ai_trace_section", "AI 痕迹候选" in text, "expected lightweight AI-trace result")
        check(
            "ai_trace_lightweight_only",
            "未发现材料级 AI 痕迹候选或工具污染问题" in text,
            "expected the default one-sentence AI-trace result",
        )
        check("no_candidate_matrix", "AIC-01" not in text, "clean prose should not force a matrix")
        check("no_ai_trace_t_finding", "T-01" not in text, "accepted style features are not findings")
    elif case.mode == "ai_trace_detailed":
        for column in ("Candidate ID", "可观察模式", "原文证据", "深层核验", "结论", "修改方向"):
            check(f"candidate_column:{column}", column in text, column)
        for outcome in ("Confirmed Text Issue", "Source Integrity Risk", "Contextually Acceptable"):
            check(f"candidate_outcome:{outcome}", outcome in text, outcome)
        check("candidate_ids", "AIC-01" in text, "detailed candidates need trace IDs")
        check("source_risk_promoted", "S-01" in text, "source/evidence risk should be scientific")
        check("action_plan", "修改行动表" in text, "confirmed problems should be actionable")
        action_text = text.rsplit("修改行动表", 1)[-1] if "修改行动表" in text else ""
        check(
            "accepted_candidate_not_actionable",
            "Contextually Acceptable" not in action_text,
            "accepted candidates must not enter the action plan",
        )
        forbidden = ("AI 率", "AI率", "AI 生成概率", "AI概率为", "判定为 AI 生成")
        check("no_authorship_or_probability_claim", not contains_any(text, forbidden), str(forbidden))

    return checks


def copy_artifacts(workspace: Path, destination: Path) -> None:
    for folder in ("paper-reviews", "paper-revisions"):
        source = workspace / folder
        if source.exists():
            shutil.copytree(source, destination / folder, dirs_exist_ok=True)


def run_case(case: Case, args: argparse.Namespace, results_root: Path) -> dict[str, object]:
    case_result = results_root / case.case_id
    case_result.mkdir(parents=True, exist_ok=True)
    started = time.monotonic()

    with tempfile.TemporaryDirectory(prefix=f"paper-review-{case.case_id.lower()}-") as tmpdir:
        temp_root = Path(tmpdir)
        workspace = temp_root / "workspace"
        workspace.mkdir()
        codex_home, skill_hash = prepare_isolated_codex_home(temp_root)
        original_hashes = copy_inputs(case, workspace)
        final_message = workspace / "final-message.txt"
        prompt = case.prompt
        command = [
            args.codex,
            "exec",
            "--ephemeral",
            "--ignore-user-config",
            "--skip-git-repo-check",
            "--sandbox",
            "workspace-write",
            "--cd",
            str(workspace),
            "--json",
            "--output-last-message",
            str(final_message),
            prompt,
        ]
        process_env = os.environ.copy()
        process_env["CODEX_HOME"] = str(codex_home)

        try:
            completed = subprocess.run(
                command,
                capture_output=True,
                text=True,
                timeout=args.timeout,
                env=process_env,
            )
            timed_out = False
        except subprocess.TimeoutExpired as exc:
            completed = None
            timed_out = True
            (case_result / "events.jsonl").write_text(exc.stdout or "", encoding="utf-8")
            (case_result / "stderr.log").write_text(exc.stderr or "", encoding="utf-8")

        if completed is not None:
            (case_result / "events.jsonl").write_text(completed.stdout, encoding="utf-8")
            (case_result / "stderr.log").write_text(completed.stderr, encoding="utf-8")
            exit_code = completed.returncode
        else:
            exit_code = None

        if final_message.exists():
            shutil.copy2(final_message, case_result / "final-message.txt")
        copy_artifacts(workspace, case_result)

        checks = evaluate(case, workspace, original_hashes) if exit_code == 0 else []
        checks.insert(
            0,
            {
                "name": "isolated_skill_copy",
                "passed": skill_hash == file_hash(SKILL),
                "detail": f"skill_sha256={skill_hash}",
            },
        )
        checks.insert(
            0,
            {
                "name": "codex_exit_zero",
                "passed": exit_code == 0 and not timed_out,
                "detail": f"exit={exit_code}, timed_out={timed_out}",
            },
        )

    duration = round(time.monotonic() - started, 2)
    passed = all(bool(check["passed"]) for check in checks)
    result = {
        "case_id": case.case_id,
        "mode": case.mode,
        "passed": passed,
        "duration_seconds": duration,
        "checks": checks,
    }
    (case_result / "result.json").write_text(
        json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    status = "PASS" if passed else "FAIL"
    print(f"[{status}] {case.case_id} {case.mode} ({duration}s)")
    return result


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--case", choices=[case.case_id for case in CASES])
    parser.add_argument("--codex", default="codex")
    parser.add_argument("--timeout", type=int, default=420)
    parser.add_argument("--results-dir", type=Path)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.timeout <= 0:
        raise SystemExit("--timeout must be positive")
    if not SKILL.exists():
        raise SystemExit(f"Local Skill not found: {SKILL}")

    timestamp = datetime.now().strftime("%Y-%m-%d-%H%M%S")
    results_root = args.results_dir or ROOT / "_project-records" / "forward-evals" / timestamp
    results_root.mkdir(parents=True, exist_ok=True)
    selected = [case for case in CASES if args.case in (None, case.case_id)]
    results = [run_case(case, args, results_root) for case in selected]
    summary = {
        "timestamp": timestamp,
        "skill_path": str(SKILL),
        "passed": sum(1 for result in results if result["passed"]),
        "total": len(results),
        "results": results,
    }
    (results_root / "summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"{summary['passed']}/{summary['total']} forward evaluations passed.")
    print(f"Results: {results_root}")
    raise SystemExit(0 if summary["passed"] == summary["total"] else 1)


if __name__ == "__main__":
    main()
