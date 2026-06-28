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

    def test_required_text_quality_references_exist(self) -> None:
        reference_dir = ROOT / "paper-review" / "references"
        required = {
            "text-quality-audit.md",
            "text-quality-zh.md",
            "text-quality-en.md",
            "authorial-polishing.md",
            "external-polishing-routing.md",
        }

        self.assertTrue(required.issubset({path.name for path in reference_dir.iterdir()}))

    def test_public_readme_avoids_detector_positioning(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")

        self.assertIn("Scientific Review / 科学性审阅", readme)
        self.assertIn("Text Quality Review / 文本质量审阅", readme)
        self.assertIn("全文作者化润色", readme)
        self.assertNotIn("AI 率", readme)
        self.assertNotIn("AIGC", readme)

    def test_agent_prompt_keeps_review_non_editing(self) -> None:
        agent = (ROOT / "paper-review" / "agents" / "openai.yaml").read_text(
            encoding="utf-8"
        )

        self.assertIn("scientific validity and text quality", agent)
        self.assertIn("without editing the source", agent)


if __name__ == "__main__":
    unittest.main()
