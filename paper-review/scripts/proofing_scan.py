#!/usr/bin/env python3
"""Quick, high-yield proofing scan for scientific manuscripts."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


def _read_pdf_pages(pdf_path: Path) -> list[str]:
    try:
        from pypdf import PdfReader
    except ImportError as exc:
        raise SystemExit("PDF input requires the 'pypdf' package.") from exc

    reader = PdfReader(str(pdf_path))
    pages = []
    for page in reader.pages:
        try:
            text = page.extract_text() or ""
        except Exception:
            text = ""
        pages.append(re.sub(r"\s+", " ", text).strip())
    return pages


def _read_text_as_single_page(path: Path) -> list[str]:
    text = path.read_text(errors="ignore")
    return [re.sub(r"\s+", " ", text).strip()]


def _read_docx_as_single_page(path: Path) -> list[str]:
    import zipfile
    import xml.etree.ElementTree as ET
    try:
        with zipfile.ZipFile(path) as docx:
            xml_files = [f for f in docx.namelist() if f.startswith('word/') and f.endswith('.xml')]
            target_files = [f for f in xml_files if any(p in f for p in ['document', 'header', 'footer', 'footnote', 'endnote'])]
            texts = []
            for xml_file in target_files:
                try:
                    xml_content = docx.read(xml_file)
                    root = ET.fromstring(xml_content)
                    for elem in root.iter():
                        if elem.tag.endswith('}t') and elem.text:
                            texts.append(elem.text)
                except Exception:
                    continue
            full_text = " ".join(texts)
            return [re.sub(r"\s+", " ", full_text).strip()]
    except Exception as exc:
        raise SystemExit(f"Failed to read DOCX file: {exc}")


def _snip(text: str, start: int, end: int, window: int = 60) -> str:
    lo = max(0, start - window)
    hi = min(len(text), end + window)
    return text[lo:hi].strip()


def _find_regex(
    rule_id: str,
    pattern: re.Pattern[str],
    pages: list[str],
    max_hits: int,
) -> list[tuple[str, int, str]]:
    hits: list[tuple[str, int, str]] = []
    seen: set[tuple[str, int, str]] = set()
    for page_number, page_text in enumerate(pages, start=1):
        if not page_text:
            continue
        for match in pattern.finditer(page_text):
            hit = (rule_id, page_number, _snip(page_text, match.start(), match.end()))
            if hit in seen:
                continue
            seen.add(hit)
            hits.append(hit)
            if len(hits) >= max_hits:
                return hits
    return hits


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=str, help="PDF, DOCX, or text file")
    parser.add_argument("--max-hits", type=int, default=80, help="Cap total hits across all rules")
    args = parser.parse_args()

    path = Path(args.path)
    if not path.exists():
        raise SystemExit(f"File not found: {path}")

    suffix = path.suffix.lower()
    if suffix == ".pdf":
        pages = _read_pdf_pages(path)
    elif suffix == ".docx":
        pages = _read_docx_as_single_page(path)
    else:
        pages = _read_text_as_single_page(path)

    rules: list[tuple[str, re.Pattern[str]]] = [
        ("PUNC_DOUBLE_COMMA", re.compile(r",\s*,")),
        ("PUNC_DOUBLE_PERIOD", re.compile(r"\.\s*\.")),
        ("PUNC_QUOTE_DOUBLE_COMMA", re.compile(r"\"\s*,\s*,")),
        ("SEMICOLON_CAP", re.compile(r";\s+[A-Z]")),
        ("FRAME_INTO_INTO", re.compile(r"\binto\b.{0,80}?\binto\b", re.IGNORECASE)),
        ("FRAME_PLUGGING_INTO_TOGETHER", re.compile(r"plugging\s+into\s+together", re.IGNORECASE)),
        ("CAP_JAVASCRIPT", re.compile(r"\bjavascript\b")),
        ("CAP_IOS", re.compile(r"\bios\b")),
        ("CAP_IPHONE", re.compile(r"\biphone\b")),
        ("ARCTAN_DIV", re.compile(r"\barctan\s*\(\s*[^()]{0,40}?/[^()]{0,40}?\)", re.IGNORECASE)),
        ("ZH_OVERCLAIM_CAUSAL", re.compile(r"证明|导致|决定性影响")),
        ("ZH_OVERCLAIM_STABILITY", re.compile(r"完全支持|高度稳健|稳定提升")),
        ("ZH_OVERCLAIM_SCOPE", re.compile(r"全面提升|整体优化|显著改善所有")),
        ("ZH_MIXED_EVIDENCE_LANGUAGE", re.compile(r"显著正相关.{0,120}边界证据|边界证据.{0,120}显著正相关")),
        (
            "CHATBOT_LEAK_EN",
            re.compile(
                r"\bI hope this helps\b|\bLet me know if\b|\bWould you like me to\b",
                re.IGNORECASE,
            ),
        ),
        (
            "CHATBOT_LEAK_ZH",
            re.compile(r"希望这对(?:你|您)有帮助|请告诉我是否需要|是否需要我继续|如果(?:你|您)需要我"),
        ),
        (
            "UNFILLED_PLACEHOLDER",
            re.compile(
                r"\[(?:INSERT|ADD|TODO|TBD|Your\s+(?:Name|Topic)|待补充|请填写)[^\]\n]{0,100}\]"
                r"|\b20\d{2}-XX-XX\b",
                re.IGNORECASE,
            ),
        ),
        (
            "AI_CITATION_MARKUP",
            re.compile(
                r"\bciteturn\d+(?:search|view|fetch)\d+\b|contentReference\[oaicite:[^\]]+\]"
                r"|\boai_citation\b|\[attached_file:\d+\]|\bgrok_card\b",
                re.IGNORECASE,
            ),
        ),
    ]

    remaining = args.max_hits
    out: list[tuple[str, int, str]] = []
    for rule_id, pattern in rules:
        if remaining <= 0:
            break
        hits = _find_regex(rule_id, pattern, pages, remaining)
        out.extend(hits)
        remaining = args.max_hits - len(out)

    if not out:
        print("[OK] No high-confidence pattern-scan hits found.")
        return

    for rule_id, page, snippet in out:
        print(f"[{rule_id}] p{page}: {snippet}")


if __name__ == "__main__":
    main()
