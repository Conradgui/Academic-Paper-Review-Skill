from __future__ import annotations

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class SkillContractTests(unittest.TestCase):
    def test_general_skill_exposes_dual_track_contract(self) -> None:
        skill = (ROOT / "paper-review" / "SKILL.md").read_text(encoding="utf-8")

        self.assertIn("## Dual-Track Review Protocol", skill)
        self.assertIn("## Text Quality Review", skill)
        self.assertIn("Revision guidance / 修改指导", skill)
        self.assertIn("`S-01`, `S-02`", skill)
        self.assertIn("`T-01`, `T-02`", skill)
        self.assertIn("references/authorial-polishing.md", skill)
        self.assertIn("references/external-polishing-routing.md", skill)
        self.assertNotIn("**Suggested revision**", skill)

        detailed_header = (
            "| Finding ID | 位置 | 严重程度 | 判断确定性 | 文本问题 | 具体证据 | 影响 | 修改方向 |"
        )
        self.assertIn(detailed_header, skill)
        self.assertIn("Do not place plans, scratch notes, logs, or temporary files", skill)

    def test_delta_review_requires_exact_status_matrix_and_ids(self) -> None:
        skill = (ROOT / "paper-review" / "SKILL.md").read_text(encoding="utf-8")

        self.assertIn("The status matrix is mandatory", skill)
        self.assertIn("Use the exact English status tokens", skill)
        self.assertIn("Do not replace a mapped prior ID with `D-*`", skill)
        self.assertIn("Include every unresolved delta item in the Action Plan Table", skill)

    def test_language_specific_audits_are_deep_routes(self) -> None:
        audit = (ROOT / "paper-review" / "references" / "text-quality-audit.md").read_text(
            encoding="utf-8"
        )

        self.assertIn("Only after detailed reporting is triggered", audit)
        self.assertIn("first-use abbreviation expansion", audit)
        self.assertIn("punctuation and number/unit formatting", audit)
        self.assertIn("Do not assign a T-series finding ID", audit)

    def test_polishing_contract_distinguishes_authorial_and_manuscript_baselines(self) -> None:
        polishing = (
            ROOT / "paper-review" / "references" / "authorial-polishing.md"
        ).read_text(encoding="utf-8")

        self.assertIn("confirmed authorial baseline", polishing)
        self.assertIn("manuscript-consistent baseline", polishing)
        self.assertIn("do not claim a preserved DOCX output", polishing)
        self.assertIn("invariant verification table", polishing)

    def test_language_references_cover_common_academic_writing_failures(self) -> None:
        reference_dir = ROOT / "paper-review" / "references"
        zh = (reference_dir / "text-quality-zh.md").read_text(encoding="utf-8")
        en = (reference_dir / "text-quality-en.md").read_text(encoding="utf-8")

        for phrase in ("全角与半角", "数字与单位", "缩写首次出现", "文献逐篇罗列"):
            self.assertIn(phrase, zh)
        for phrase in (
            "subject-verb agreement",
            "articles and countability",
            "US or UK spelling",
            "first-use abbreviation expansion",
            "paper-by-paper list",
        ):
            self.assertIn(phrase, en)

    def test_research_policy_is_strictly_opt_in(self) -> None:
        skill = (ROOT / "paper-review" / "SKILL.md").read_text(encoding="utf-8")

        self.assertIn("Do not search until the user explicitly authorizes it", skill)
        tier_one = skill.split("### Source Credibility Hierarchy", 1)[1].split(
            "### Cross-Validation Rule", 1
        )[0]
        self.assertNotIn("arXiv", tier_one.split("- **Tier 1", 1)[1].split("- **Tier 2", 1)[0])

    def test_common_manuscript_failure_modes_are_explicit(self) -> None:
        skill = (ROOT / "paper-review" / "SKILL.md").read_text(encoding="utf-8")
        empirical = (
            ROOT / "paper-review" / "references" / "empirical-paper-audit.md"
        ).read_text(encoding="utf-8")

        self.assertIn("## Common Manuscript Failure Modes", skill)
        for phrase in (
            "paper-by-paper inventory",
            "data or material provenance",
            "Results reports observation before interpretation",
            "Discussion distinguishes findings from interpretation",
            "required declarations",
        ):
            self.assertIn(phrase, skill)
        for phrase in (
            "effect sizes and confidence intervals",
            "multiple-testing",
            "missing-data handling",
            "train/validation/test leakage",
        ):
            self.assertIn(phrase, empirical)

    def test_required_text_quality_references_exist(self) -> None:
        reference_dir = ROOT / "paper-review" / "references"
        required = {
            "text-quality-audit.md",
            "text-quality-zh.md",
            "text-quality-en.md",
            "authorial-polishing.md",
            "external-polishing-routing.md",
            "ai-trace-candidate-audit.md",
        }

        self.assertTrue(required.issubset({path.name for path in reference_dir.iterdir()}))

    def test_ai_trace_candidate_audit_is_routed_and_non_attributive(self) -> None:
        skill = (ROOT / "paper-review" / "SKILL.md").read_text(encoding="utf-8")
        text_audit = (
            ROOT / "paper-review" / "references" / "text-quality-audit.md"
        ).read_text(encoding="utf-8")
        ai_audit = (
            ROOT / "paper-review" / "references" / "ai-trace-candidate-audit.md"
        ).read_text(encoding="utf-8")

        self.assertIn("references/ai-trace-candidate-audit.md", skill)
        self.assertIn("AI-trace candidate audit", text_audit)
        self.assertIn("未发现材料级 AI 痕迹候选或工具污染问题。", text_audit)
        self.assertIn(
            "Surface candidate -> Context function -> Specificity -> Evidence/citation -> Section fit -> Final judgment",
            ai_audit,
        )
        self.assertIn(
            "| Candidate ID | 位置 | 可观察模式 | 原文证据 | 深层核验 | 结论 | 修改方向 |",
            ai_audit,
        )
        for outcome in (
            "Confirmed Text Issue",
            "Source Integrity Risk",
            "Contextually Acceptable",
            "Needs Verification",
        ):
            self.assertIn(outcome, ai_audit)
        self.assertIn("promote it to a `T-*` finding", ai_audit)
        self.assertIn("promote it to an `s-*` finding", ai_audit.lower())
        self.assertIn("Do not infer authorship", ai_audit)
        self.assertIn("Do not output an AI probability", ai_audit)

    def test_ai_trace_audit_rejects_style_blacklists(self) -> None:
        ai_audit = (
            ROOT / "paper-review" / "references" / "ai-trace-candidate-audit.md"
        ).read_text(encoding="utf-8")

        for phrase in (
            "Do not ban adverbs",
            "passive voice",
            "em dashes",
            "three-item lists",
            "sentence-length variation",
        ):
            self.assertIn(phrase, ai_audit)
        self.assertNotIn("## Scoring", ai_audit)
        self.assertNotIn("Below 35/50", ai_audit)

    def test_public_readme_avoids_detector_positioning(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("Scientific Review / 科学性审阅", readme)
        self.assertIn("Text Quality Review / 文本质量审阅", readme)
        self.assertIn("全文受保护润色", readme)
        self.assertNotIn("AI 率", readme)
        self.assertNotIn("AIGC", readme)
        self.assertIn("只有在具备可用的 DOCX 编辑与渲染核验工具时", readme)
        self.assertIn("论文一致性基线", readme)
        self.assertIn("PDF 扫描需要本地 Python 环境提供 `pypdf`", readme)

    def test_public_readme_explains_current_review_contract(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        for phrase in (
            "轻量观察不分配 `T-*`",
            "The status matrix is mandatory",
            "Needs External Verification",
            "只允许存放面向用户的最终交付物",
            "通用版扫描器",
            "LaTeX 专项版保留原有基础扫描器",
            "4/4 个用例、47/47 项断言通过",
            "<原文件名>-polish-report-<timestamp>.md",
        ):
            self.assertIn(phrase, readme)

        self.assertNotIn("<原文件名>-polishing-report-<timestamp>.md", readme)
        self.assertIn("合成任务的单次独立运行", readme)
        self.assertIn("不能外推到所有学科", readme)

    def test_public_readme_explains_ai_trace_default_and_explicit_modes(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("AI 痕迹候选审阅", readme)
        self.assertIn("默认轻量扫描", readme)
        self.assertIn("用户明确要求", readme)
        self.assertIn("不判断作者身份", readme)
        self.assertIn("不输出 AI 概率", readme)
        self.assertIn("Contextually Acceptable", readme)
        self.assertIn("hardikpandya/stop-slop", readme)
        self.assertIn("Wikipedia:Signs of AI writing", readme)

    def test_forward_suite_covers_ai_trace_modes(self) -> None:
        runner = (ROOT / "tests" / "forward" / "run_forward_evals.py").read_text(
            encoding="utf-8"
        )
        fixtures = ROOT / "tests" / "forward" / "fixtures"

        self.assertIn('"FWD-05"', runner)
        self.assertIn('"FWD-06"', runner)
        self.assertIn('"ai_trace_lightweight"', runner)
        self.assertIn('"ai_trace_detailed"', runner)
        self.assertTrue((fixtures / "ai-trace-clean-methods.md").exists())
        self.assertTrue((fixtures / "ai-trace-problematic.md").exists())

    def test_agent_prompt_keeps_review_non_editing(self) -> None:
        agent = (ROOT / "paper-review" / "agents" / "openai.yaml").read_text(
            encoding="utf-8"
        )

        self.assertIn("scientific validity and text quality", agent)
        self.assertIn("without editing the source", agent)

        prompt_line = next(
            line for line in agent.splitlines() if line.strip().startswith("default_prompt:")
        )
        prompt = prompt_line.split('"', 1)[1].rsplit('"', 1)[0]
        self.assertLessEqual(len(prompt), 128)


if __name__ == "__main__":
    unittest.main()
