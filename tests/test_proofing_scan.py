from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "paper-review" / "scripts" / "proofing_scan.py"


def run_scan(text: str) -> str:
    with tempfile.TemporaryDirectory() as tmpdir:
        sample = Path(tmpdir) / "sample.md"
        sample.write_text(text, encoding="utf-8")
        result = subprocess.run(
            [sys.executable, str(SCRIPT), str(sample), "--max-hits", "40"],
            check=True,
            capture_output=True,
            text=True,
        )
    return result.stdout


class ProofingScanTests(unittest.TestCase):
    def test_flags_high_confidence_publication_artifacts(self) -> None:
        output = run_scan(
            "Here is the revised paragraph. I hope this helps! Let me know if you want more.\n"
            "请告诉我是否需要继续扩写。\n"
            "[INSERT SOURCE URL]\n"
            "The claim is supported by citeturn0search0.\n"
        )

        self.assertIn("[CHATBOT_LEAK_EN]", output)
        self.assertIn("[CHATBOT_LEAK_ZH]", output)
        self.assertIn("[UNFILLED_PLACEHOLDER]", output)
        self.assertIn("[AI_CITATION_MARKUP]", output)

    def test_preserves_existing_high_confidence_rules(self) -> None:
        output = run_scan("Bad,, javascript arctan(x/y)")

        self.assertIn("[PUNC_DOUBLE_COMMA]", output)
        self.assertIn("[CAP_JAVASCRIPT]", output)
        self.assertIn("[ARCTAN_DIV]", output)

    def test_does_not_flag_clean_bilingual_academic_prose(self) -> None:
        output = run_scan(
            "本文使用120个观测值检验变量 X 与 Y 的统计关系，并报告95%置信区间[1]。\n"
            "The analysis reports the association between X and Y with a 95% confidence interval."
        )

        self.assertEqual("[OK] No high-confidence pattern-scan hits found.\n", output)


if __name__ == "__main__":
    unittest.main()
