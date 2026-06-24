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
    for page_number, page_text in enumerate(pages, start=1):
        if not page_text:
            continue
        for match in pattern.finditer(page_text):
            hits.append((rule_id, page_number, _snip(page_text, match.start(), match.end())))
            if len(hits) >= max_hits:
                return hits
    return hits


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=str, help="PDF or text file")
    parser.add_argument("--max-hits", type=int, default=80, help="Cap total hits across all rules")
    args = parser.parse_args()

    path = Path(args.path)
    if not path.exists():
        raise SystemExit(f"File not found: {path}")

    pages = _read_pdf_pages(path) if path.suffix.lower() == ".pdf" else _read_text_as_single_page(path)

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
