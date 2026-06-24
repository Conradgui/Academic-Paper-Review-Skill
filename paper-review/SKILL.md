---
name: paper-review
description: Use when reviewing, proofreading, or auditing scientific and technical manuscripts in Markdown, DOCX, PDF, LaTeX, or plain text; checking research questions, argument logic, variables, methods, equations, evidence, figures, tables, appendices, citations, unsupported claims, writing clarity, or producing a structured manuscript review.
---

# Paper Review

## Overview

Produce a concrete, evidence-focused manuscript review. Default to a Markdown review report unless the user requests LaTeX, DOCX-ready prose, inline edits, Chinese, English, or another output format.

Prioritize research quality and internal consistency over surface-level polishing.

## Default Behavior

1. Read the full manuscript or all provided manuscript material before writing findings.
2. Preserve equations, symbols, citation keys, table/figure labels, and quoted snippets exactly when needed for accuracy.
3. Match the user's requested language; otherwise use the user's language when clear.
4. Create a new timestamped review file at `paper-reviews/review-YYYY-MM-DD-HHMMSS.md` when writing to disk, unless the user gives another path.
5. Do not modify the manuscript unless the user explicitly requests edits or a revision pass.
6. Do not require a fixed review template. Use the structure that best exposes actionable issues.
7. If the manuscript is incomplete, review what is available and state which checks are limited by missing files.

## Input Handling

Support Markdown, DOCX, PDF, LaTeX source, and plain text.

- **Markdown or plain text:** review structure, claims, citations, tables, formulas, and prose directly.
- **DOCX:** extract or inspect content with available document tools; preserve section/table context in findings.
- **PDF:** review visible content; note that source-level comments, hidden metadata, and some cross-reference checks may be limited.
- **LaTeX:** inspect source when available; for LaTeX-specific source, macro, cross-reference, and compileability concerns, prefer `$latex-paper-review` when installed.
- **Multi-file projects:** inspect the main file plus included chapters, bibliography, appendices, tables, figures/captions, and supporting notes when available.

## Manuscript Understanding Model

Before judging individual issues, build a short internal map of:

- field or domain
- research question and intended contribution
- core concepts, variables, constructs, or symbols
- relationships between variables or claims
- research method, model, experiment, proof strategy, or review framework
- data, material, corpus, assumptions, or evidence base
- main results and conclusion boundaries

Use this map to test whether the paper's claims, method, evidence, and wording align. Do not output the map unless it helps the review.

## Review Workflow

1. Identify manuscript type: empirical, theoretical/mathematical, systems/technical, review/conceptual, or mixed.
2. Build the manuscript understanding model.
3. Audit the highest-risk content first: research question, method, variables/symbols, evidence, results, equations, figures/tables, appendices, and citations.
4. Re-check the highest-risk findings before presenting them.
5. Run `scripts/proofing_scan.py` when code execution is available and the input is PDF or text-like; otherwise do the manual proofing scan below.
6. Perform a bounded editorial pass after the technical and evidence audit.
7. Write the review report with technical and factual issues before prose issues unless the user asks for prose-first review.

## Review Lenses

Use these lenses as applicable:

- **Structure:** title, abstract, introduction, related work, method, results, discussion, conclusion, and appendices form a coherent path.
- **Evidence:** claims are supported by data, figures, tables, experiments, citations, derivations, or stated assumptions.
- **Method:** study design, variables, model, experiment, proof, or review method can answer the research question.
- **Expression:** terms, paragraphs, figures, tables, references, and formatting support reader comprehension.
- **Risk:** overclaiming, causal overreach, missing caveats, sample limits, external validity, unsupported novelty, or ambiguity.

## Manuscript-Type Checks

For empirical papers, check variable definitions, measurement, model specification, table interpretation, robustness checks, causal language, and conclusion boundaries.

For theoretical or mathematical papers, check definitions, assumptions, notation, theorem/proposition statements, proof steps, dimensions, signs, branches, and symbol drift.

For systems or technical papers, check task framing, baseline fairness, evaluation metrics, implementation ambiguity, reproducibility, ablations, and claim-to-result alignment.

For review or conceptual papers, check taxonomy logic, concept boundaries, source representativeness, citation support, and whether synthesis goes beyond summary.

## Technical And Evidence Audit

Always check for:

- unsupported or overstated claims
- conclusions that do not follow from reported results
- inconsistency between text, equations, figures, tables, captions, appendices, and conclusions
- undefined variables, constructs, terms, symbols, or abbreviations
- notation or terminology drift
- unit, dimensional, arithmetic, or quantitative inconsistencies
- sign errors, missing factors, normalization ambiguity, or missing case distinctions
- inverse-trig, branch, or quadrant ambiguity, such as `arctan(x/y)` where `atan2` or an explicit branch convention may be needed
- mismatch between definitions, formulas, appendix material, and implementation-facing expressions
- missing assumptions, qualifiers, limitations, or uncertainty that materially affect interpretation
- citation/reference mismatch or citation used to support a claim it does not actually establish

Label findings clearly as **definite error**, **unsupported claim**, **likely issue**, or **needs external verification**. Do not present verification-needed items as definite errors.

## External Research Policy

Do not perform external web or literature searches by default.

Suggest or request user authorization before external research when:

- a finding depends on field background, classic theory, method norms, or factual claims outside the manuscript
- the user asks for review against authoritative sources, literature, or domain standards
- citation accuracy or source relevance cannot be judged from provided materials

When authorized:

- prefer the manuscript's cited sources, official institutions, textbooks/handbooks, top journals/conferences, authoritative reviews, and methods papers
- do not treat blogs, marketing pages, forums, or unsourced summaries as strong evidence
- cite source links in the review
- use external evidence to strengthen judgment or mark items for verification, not to overstate certainty
- for unpublished or sensitive manuscripts, search with minimal keywords or bibliographic metadata rather than uploading full text

## Editorial Review

Editorial review is secondary. Include issues that affect meaning, technical clarity, or professionalism:

- ambiguous phrasing that changes interpretation
- inconsistent terminology
- weak transitions that obscure argument logic
- unclear figure/table descriptions
- malformed equation-adjacent prose
- broken references, duplicated punctuation, malformed titles, or obvious citation-format glitches
- high-confidence grammar, spelling, or capitalization issues

Avoid subjective line editing unless the user requests exhaustive proofreading.

## Final Proofing Sweep

Run when useful:

```bash
python3 scripts/proofing_scan.py <path-to-pdf-or-text> --max-hits 80
```

Use hits as candidates and spot-check before including them.

If code execution is unavailable, manually scan for duplicated punctuation, malformed equation-adjacent prose, product/language capitalization, citation-format glitches, and branch/quad ambiguity patterns such as `arctan(x/y)`.

## Output Contract

Default Markdown report should include:

- concise overall assessment
- most important technical, methodological, or evidence findings
- meaningful editorial findings
- proofing-sweep items when present
- highest-priority fixes
- items needing external verification

For each substantive finding, include location, problem, why it matters, and suggested fix.

If no concrete technical or evidence issues are found, say which checks were performed and that no concrete issue was identified.

Read `references/review-rubric.md` when a broader checklist would help, especially for long manuscripts or revisions after local edits.
