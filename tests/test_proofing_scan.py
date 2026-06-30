from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
import zipfile
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

    def test_flags_extended_ai_tool_artifacts(self) -> None:
        output = run_scan(
            'Metadata leaked as {"attributableIndex": 2}.\n'
            ":::writing\n"
            "https://example.org/article?utm_source=chatgpt.com&utm_medium=referral\n"
        )

        self.assertIn("[AI_TOOL_METADATA]", output)
        self.assertIn("[AI_TOOL_TRACKING_URL]", output)

    def test_does_not_treat_academic_style_features_as_artifacts(self) -> None:
        output = run_scan(
            "Additionally, the samples were carefully analyzed using a robust protocol—"
            "temperature, pressure, and duration were recorded. The attributable index "
            "was defined before analysis."
        )

        self.assertEqual("[OK] No high-confidence pattern-scan hits found.\n", output)

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

    def test_clusters_nearby_matches_from_the_same_rule(self) -> None:
        output = run_scan(
            f"{'前置说明' * 20}。本文证明了 X 在给定条件下会影响中间机制，进而导致 Y。"
            f"{'后续说明' * 20}\n"
            f"{'前置说明' * 20}。该结果完全支持假设，并表现出高度稳健性。"
            f"{'后续说明' * 20}\n"
            f"{'前置说明' * 20}。希望这对你有帮助，请告诉我是否需要继续。"
            f"{'后续说明' * 20}"
        )

        self.assertEqual(1, output.count("[ZH_OVERCLAIM_CAUSAL]"))
        self.assertEqual(1, output.count("[ZH_OVERCLAIM_STABILITY]"))
        self.assertEqual(1, output.count("[CHATBOT_LEAK_ZH]"))

    def test_does_not_cluster_distinct_punctuation_errors(self) -> None:
        output = run_scan(
            f"{'A' * 70} First,, {'B' * 80} Second,, {'C' * 70}"
        )

        self.assertEqual(2, output.count("[PUNC_DOUBLE_COMMA]"))

    def test_rejects_nonpositive_max_hits(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            sample = Path(tmpdir) / "sample.md"
            sample.write_text("clean text", encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(SCRIPT), str(sample), "--max-hits", "0"],
                capture_output=True,
                text=True,
            )

        self.assertNotEqual(0, result.returncode)
        self.assertIn("must be a positive integer", result.stderr)

    def test_rejects_malformed_primary_docx_xml(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            sample = Path(tmpdir) / "malformed.docx"
            with zipfile.ZipFile(sample, "w") as docx:
                docx.writestr("word/document.xml", "<w:document>")
            result = subprocess.run(
                [sys.executable, str(SCRIPT), str(sample)],
                capture_output=True,
                text=True,
            )

        self.assertNotEqual(0, result.returncode)
        self.assertIn("Failed to parse required DOCX part", result.stderr)

    def test_scans_minimal_valid_docx(self) -> None:
        document_xml = """<?xml version="1.0" encoding="UTF-8"?>
        <w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
          <w:body><w:p><w:r><w:t>I hope this helps.</w:t></w:r></w:p></w:body>
        </w:document>
        """
        with tempfile.TemporaryDirectory() as tmpdir:
            sample = Path(tmpdir) / "valid.docx"
            with zipfile.ZipFile(sample, "w") as docx:
                docx.writestr("word/document.xml", document_xml)
            result = subprocess.run(
                [sys.executable, str(SCRIPT), str(sample)],
                check=True,
                capture_output=True,
                text=True,
            )

        self.assertIn("[CHATBOT_LEAK_EN]", result.stdout)


if __name__ == "__main__":
    unittest.main()
