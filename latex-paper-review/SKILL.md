---
name: latex-paper-review
description: Use when reviewing scientific and technical manuscripts written in LaTeX; checking LaTeX source, equations, derivations, notation, appendix formulas, cross-references, citation keys, compileability, implementation ambiguity, unsupported claims, writing issues, or generating a LaTeX review file.
---

# LaTeX Paper Review

## Overview

Produce one concrete, compileable LaTeX review file. Prioritize scientific and technical correctness over prose polish, then add bounded editorial findings that materially improve clarity or professionalism.

## Default Behavior

1. Read the full manuscript before writing findings.
2. Use extra thinking by default, but do not narrate the reasoning process.
3. Write a standalone LaTeX review to `paper-reviews/review-YYYY-MM-DD-HHMMSS.tex`, unless the user gives a different path.
4. Match the user's requested output language; otherwise use the user's language when clear.
5. Preserve equations, symbols, citation keys, and quoted manuscript snippets exactly when needed for technical accuracy.
6. Do not require a fixed review template or section layout unless the user asks for one.
7. Create a new timestamped review file by default. Only update an existing review file if the user explicitly asks.
8. Compiling to PDF is optional unless the user asks for it or compilation is needed to validate the LaTeX.

## Review Priority

Spend attention in this order:

1. equations, derivations, notation, units, definitions, algorithms, and implementation-facing formulas
2. consistency between claims, evidence, figures, tables, captions, appendices, and conclusions
3. editorial quality, especially high-confidence issues that are cheap to verify and fix

Do not let editorial findings crowd out technical findings. Treat `proofread`, `flag typos`, `grammar`, `writing quality`, and similar wording as a request to spend more budget on the editorial sweep after the technical audit.

## Workflow

1. Read the manuscript to understand the main claims, evidence, equations, appendices, and structure.
2. Identify the highest-risk technical content: key equations, symbol definitions, quantitative claims, coordinate transformations, appendix formulas, and implementation-facing expressions.
3. Perform the technical audit first.
4. Re-check the highest-risk technical findings before presenting them.
5. Perform a bounded editorial pass after the technical audit.
6. Run `scripts/proofing_scan.py` when code execution is available; otherwise do the manual pattern scan in `Final Proofing Sweep`.
7. Spot-check proofing-scan candidates before presenting them as issues.
8. Write the review file.

For long papers, inspect sections in chunks when helpful, but do not force a ritual that does not improve the review.

## Technical Audit

Always check for:

- unsupported or overstated claims
- conclusions that do not follow from the reported results
- inconsistency between text, equations, figures, tables, captions, and appendices
- undefined symbols or symbols used before definition
- notation drift between sections or between main text and appendix
- unit errors or dimensional inconsistencies
- arithmetic or quantitative inconsistencies
- sign errors, missing factors, normalization ambiguity, or missing case distinctions
- inverse-trig, branch, or quadrant ambiguity, such as `arctan(x/y)` where `atan2` or an explicit branch convention may be needed
- coordinate-system ambiguity, including misuse of initial, final, source, observer, local, global, polar, or azimuthal
- mismatch between mathematical definitions and appendix or code-facing formulas
- missing assumptions, qualifiers, or uncertainty that materially affect interpretation
- factual statements that appear unsupported or likely incorrect

### Notation And Terminology Drift

For frequently used symbols, especially subscripted or superscripted angles, radii, and frame labels, record:

- where the symbol is first defined
- the verbal descriptor attached to it
- later descriptor variants and whether they conflict

Flag conflicts where the same symbol is described with inconsistent role or temporal adjectives, such as initial/final, source/observer, or emission/reception.

### Confidence Labels

Label technical judgments clearly:

- **Definite error:** contradicted by the manuscript itself or by straightforward math, logic, or internal evidence.
- **Unsupported claim:** stated more strongly than the manuscript supports.
- **Likely issue:** plausibly wrong or misleading, but not fully provable from the manuscript alone.
- **Needs external verification:** depends on outside literature or facts not established in the manuscript.

Do not present verification-needed items as definite errors.

## Coverage Requirement

If the manuscript contains equations, derivations, appendices, or implementation formulas, inspect them explicitly. Do not finish the review without checking branch conventions, sign conventions, symbol definitions, dimensional consistency, and implementation ambiguity.

If no concrete technical issues are found, say explicitly in the review file that these checks were performed and no concrete issues were identified.

## Editorial Review

Include meaningful editorial issues that affect meaning, create technical ambiguity, or noticeably reduce professionalism.

Look for:

- typos, spelling, grammar, and punctuation issues
- awkward, vague, or ambiguous phrasing
- sentences that obscure a technical point
- broken references or citation mismatches
- inconsistent terminology or notation
- malformed derivation or equation-adjacent prose
- duplicated punctuation, malformed quoted titles, inconsistent capitalization, and obvious citation-format glitches in references
- capitalization or styling mistakes in proper names, product names, languages, or branded terms

Do not spend space on subjective line editing or style preferences. Include only a bounded number of minor proofing items unless the user explicitly asks for exhaustive proofreading.

## Final Proofing Sweep

Run:

```bash
python3 scripts/proofing_scan.py <path-to-pdf-or-text> --max-hits 80
```

Use hits as candidates, then spot-check each before including it. If code execution is unavailable, manually scan for:

- duplicated punctuation and spacing artifacts: `, ,`, `,,`, `..`, `" , ,`, `" ,`
- semicolon capitalization anomalies: `;` followed by a capital letter where the second clause is not a new sentence or proper noun
- malformed equation-adjacent grammar frames: `into ... into ...`, `with ... into ...`, `plugging ... into together ...`
- programming or product-name capitalization: JavaScript, iOS, iPhone
- quadrant or branch ambiguity patterns, especially `arctan(x/y)` expressions

Before finishing, check bibliography/reference hygiene and dense derivation prose near equations.

## Output Contract

Write LaTeX only in the review file. Use minimal standalone scaffolding that can compile.

Cover:

- overall assessment of manuscript quality
- most important technical findings
- meaningful editorial findings
- a short proofing-sweep subsection when there are obvious high-confidence copyediting defects worth fixing
- highest-priority fixes
- items that need external verification

For each technical finding, include location, problem, why it matters, and suggested fix.

For each editorial finding, include location, problem, why it matters, suggested fix, and an optional candidate rewrite.

For proofing-sweep items, a compact bullet list is acceptable if each bullet includes location, problem, and suggested fix.

Put technical and factual issues before prose issues unless the user explicitly asks for a prose-first review.

## Useful Reference

Read `references/review-rubric.md` when a broader checklist would help, especially for long manuscripts or revisions after local edits.
