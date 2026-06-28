---
name: paper-review
description: Use when reviewing, proofreading, auditing, or authorially polishing scientific and technical manuscripts in Markdown, DOCX, PDF, LaTeX, or plain text; checking research questions, argument logic, variables, methods, equations, evidence, figures, tables, appendices, citations, unsupported claims, text clarity, terminology, style consistency, or producing a structured manuscript review or protected revision.
---

# Paper Review

## Overview

Produce a concrete manuscript review across two parallel quality tracks:

1. **Scientific Review:** research questions, methods, evidence, variables, equations, figures/tables, citations, and conclusion boundaries.
2. **Text Quality Review:** clarity, terminology, redundancy, paragraph flow, register, and authorial-style consistency.

Default to a Markdown review report unless the user requests another output format. Scientific validity remains the first priority; text-quality review must not weaken or replace it.

## Default Behavior

1. Read the full manuscript or all provided manuscript material before writing findings.
2. Preserve equations, symbols, citation keys, table/figure labels, and quoted snippets exactly when needed for accuracy.
3. Match the user's requested language; default to Simplified Chinese (简体中文) unless specified otherwise.
4. Create a new timestamped review file at `paper-reviews/review-YYYY-MM-DD-HHMMSS.md` when writing to disk, unless the user gives another path.
5. Do not modify the manuscript unless the user explicitly requests edits or a revision pass.
6. Do not require a fixed review template. Use the structure that best exposes actionable issues.
7. If the manuscript is incomplete, review what is available and state which checks are limited by missing files.
8. Run both review tracks by default. Keep the text-quality result concise unless material problems or an explicit request trigger detailed reporting.
9. Do not infer authorship or output an AI probability.

## Input Handling

Support Markdown, DOCX, PDF, LaTeX source, and plain text.

- **Markdown or plain text:** review structure, claims, citations, tables, formulas, and prose directly.
- **DOCX:** extract or inspect content with available document tools; preserve section/table context in findings.
- **PDF:** review visible content; note that source-level comments, hidden metadata, and some cross-reference checks may be limited. Do not perform full-manuscript polishing from PDF alone.
- **LaTeX:** inspect source when available; for LaTeX-specific source, macro, cross-reference, and compileability concerns, prefer `$latex-paper-review` when installed.
- **Multi-file projects:** inspect the main file plus included chapters, bibliography, appendices, tables, figures/captions, and supporting notes when available.

## Manuscript Understanding Model

Before formulating any review findings, build a structured internal map covering:

- **Research Question Map**: Identify the core research questions, primary claims, and intended contributions.
- **Construct / Variable / Parameter Map**: Identify independent/dependent variables, mediators, moderators, control variables, mathematical parameters, system components, or theoretical constructs (as applicable to the manuscript type).
- **Relationship Map**: Identify hypothesized directions, causal links, logical dependencies, mathematical relationships, or system interactions.
- **Method Fit Assessment**: Evaluate whether the selected research design or method logically answers the research questions, whether the generated evidence supports the stated claims, and whether conclusion boundaries match the evidence.

Use this map to test whether the paper's claims, method, evidence, and wording align. Do not output this model in the final report unless it directly exposes an issue.

## Dual-Track Review Protocol

Apply both tracks during every review, including recheck mode unless the user explicitly narrows the scope:

- **Scientific Review:** apply the Core Manuscript Audit Protocol and all relevant manuscript-type enhancement modules.
- **Text Quality Review:** read `references/text-quality-audit.md` and run its lightweight audit after the scientific review. Load the Chinese and/or English reference only when its routing rules require it.

Keep the tracks distinct. A vague causal claim belongs in Scientific Review even if the sentence is also awkward. A sustained register shift or redundant paragraph belongs in Text Quality Review unless it changes scientific meaning.

## Core Manuscript Audit Protocol

Every manuscript must receive a transparent core audit before optional type-specific checks. Apply these checks across manuscript types without forcing empirical-paper concepts onto non-empirical work:

1. **Research question audit:** identify the main question, contribution, and whether the paper's structure keeps returning to that question.
2. **Core concept / variable / symbol / construct audit:** identify the key units of analysis for this manuscript type and check whether they are defined, used consistently, and operational enough for readers to follow.
3. **Claim-evidence chain audit:** test whether each important claim is supported by the paper's method, data, figures, tables, derivations, citations, appendices, or explicit assumptions.
4. **Method-question fit audit:** check whether the selected method, model, experiment, proof, system evaluation, or review framework can answer the research question.
5. **Structural coherence audit:** check whether title, abstract, introduction, related work, method, results, discussion, conclusion, and appendices form a coherent path.
6. **Support-material audit:** check whether figures, tables, appendices, references, formulas, and supplementary material support rather than contradict the main text.
7. **Conclusion boundary audit:** check whether conclusion strength, limitations, causal wording, and practical implications match the actual evidence.
8. **Actionability audit:** convert the most important findings into the action plan table defined in `Output Contract`.

Interpret "variables" broadly:

- empirical papers: variables, indicators, controls, mediators, moderators
- theoretical papers: concepts, propositions, assumptions, definitions
- mathematical papers: symbols, parameters, functions, theorem conditions
- systems papers: modules, inputs/outputs, metrics, baselines
- review papers: taxonomy dimensions, concept boundaries, literature streams

## Review Workflow

1. Identify manuscript type: empirical, theoretical/mathematical, systems/technical, review/conceptual, or mixed.
2. Build the manuscript understanding model.
3. Apply the Core Manuscript Audit Protocol.
4. Trace the Evidence Chain for identified claims: Check the path `Claim` -> `Evidence` -> `Figure/Table` -> `Method` -> `Citation` -> `Appendix` (if applicable) for inconsistencies, missing links, or overreaching assertions.
5. If the manuscript has empirical-research features, read `references/empirical-paper-audit.md` and apply it as an enhancement module, not as a replacement for the core audit.
6. Read `references/claim-strength-calibration.md` when the manuscript contains causal, significance, robustness, novelty, policy, or contribution claims whose wording may be stronger than the evidence.
7. Audit the highest-risk content first: research question, method, variables/symbols, evidence, results, equations, figures/tables, appendices, and citations.
8. Re-check the scientific findings and classify them by severity and certainty.
9. Read `references/text-quality-audit.md`, run the lightweight text-quality track, and conditionally load `references/text-quality-zh.md` and/or `references/text-quality-en.md`.
10. Run `scripts/proofing_scan.py` when code execution is available and the input is PDF, DOCX, Markdown, or text-like; otherwise do the manual proofing scan below.
11. Spot-check all script and style candidates in context before reporting them.
12. Write the review report with scientific findings prioritized and a separate text-quality section.

## Recheck / Delta Review

Use this mode when the user asks to recheck, review a revised draft, compare against a prior review, verify whether issues were fixed, or provides an earlier review file.

In recheck mode:

1. Read the prior review and the current manuscript materials.
2. Preserve prior finding IDs when available and map findings to their current manuscript locations, accounting for section or wording changes.
3. Classify each prior finding as:
   - **Resolved:** the issue is fixed.
   - **Still Open:** the issue remains materially unchanged.
   - **Downgraded:** the issue remains but has been narrowed, qualified, or partially addressed.
   - **Upgraded:** the issue became more serious or now affects a higher-priority claim.
   - **New:** a newly introduced or newly discovered issue.
   - **Needs External Verification:** the status depends on data, literature, code, or context not available in the manuscript.
4. Do not simply repeat the old review. Focus on status changes, remaining blockers, and new issues.
5. Include next action for each still-open, downgraded, upgraded, new, or verification-needed item.

Use a compact status matrix when helpful:

```markdown
| Finding ID | 原问题 | 当前位置 | 状态 | 下一步动作 |
|---|---|---|---|---|
```

## Review Lenses

Use these lenses as applicable:

- **Structure:** title, abstract, introduction, related work, method, results, discussion, conclusion, and appendices form a coherent path.
- **Evidence:** claims are supported by data, figures, tables, experiments, citations, derivations, or stated assumptions.
- **Method:** study design, variables, model, experiment, proof, or review method can answer the research question.
- **Expression:** terms, paragraphs, figures, tables, references, and formatting support reader comprehension.
- **Risk:** overclaiming, causal overreach, missing caveats, sample limits, external validity, unsupported novelty, or ambiguity.

## Manuscript-Type Checks

For each manuscript type, check specific methodological validity dimensions (if applicable):

- **Empirical papers**: Check variable definitions, measurement validity, model specification, table interpretation, robustness checks, causal language, causal boundary limits, selection bias, endogeneity, construct reliability, and conclusion boundaries.
- **Theoretical or mathematical papers**: Check definitions, assumptions, notation, boundary conditions, theorem/proposition statements, proof steps, dimensions, signs, branches, and symbol drift.
- **Systems or technical papers**: Check task framing, baseline fairness, evaluation metrics, implementation ambiguity, reproducibility, ablations, external validity, and claim-to-result alignment.
- **Review or conceptual papers**: Check taxonomy logic, concept boundaries, source representativeness, citation support, and whether synthesis goes beyond summary.

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

When a finding concerns claim strength, use `references/claim-strength-calibration.md` to identify an evidence-appropriate wording level and minimal phrase options. Do not draft a paste-ready replacement sentence unless the user explicitly requests polishing.

## Severity And Certainty Classification

For each finding, you must determine both its severity and certainty:

### Severity Levels
- **Critical Issues**: Factual, logical, or methodological issues that threaten the primary validity of the manuscript (e.g., unsupported core claims, missing identification strategy, undefined key variables, contradictory results).
- **Major Issues**: Significant problems that weaken confidence in the findings (e.g., measurement ambiguity, incomplete methodological justification, weak evidence chain).
- **Minor Issues**: Localized errors that affect clarity, consistency, or readability (e.g., terminology inconsistency, local figure-text mismatches, formatting problems).
- **Writing Suggestions**: Non-essential suggestions to improve flow, grammar, or phrasing.

### Certainty Labels
- **确定错误 (Definite Error)**: Contradicted directly by the manuscript's own contents, math, or established logic.
- **证据不足 (Unsupported Claim)**: Stated more strongly than the manuscript's data or references justify.
- **疑似问题 (Likely Issue)**: Highly probable issue that requires authors' attention but cannot be proven definitively from the text alone.
- **需核对/确认 (Requires Verification)**: Depends on external literature or context outside the manuscript.

## External Research Policy

Do not perform external web or literature searches by default. Only perform searches when explicitly authorized by the user, when a finding cannot be assessed without external knowledge, or when the manuscript explicitly requests fact validation.

When searching, protect manuscript privacy by using anonymized queries (do not upload the title, author names, or sensitive draft text).

### Source Credibility Hierarchy
- **Tier 1 (Authoritative)**: Original cited papers, peer-reviewed journals/conferences (e.g., ACM/IEEE, Nature, MISQ, AER), official standards, standard textbooks, official documentation, academic databases (OpenAlex, PubMed, arXiv).
- **Tier 2 (Supporting)**: University lecture notes, technical manuals, high-quality reviews, preprints.
- **Tier 3 (Non-authoritative)**: General forums (StackOverflow, Reddit), commercial/marketing blogs, AI summaries without sources.
*Rule: Tier 3 sources may only serve as search leads or prompts to check further, but MUST NEVER be cited as academic evidence, consensus, or proof of error.*

### Cross-Validation Rule
When a review conclusion depends on external academic consensus, cross-check multiple authoritative (Tier 1/2) sources whenever feasible. If evidence remains uncertain, label the issue as "requires verification" rather than asserting that the manuscript is incorrect.

## Text Quality Review

Read `references/text-quality-audit.md` for every review. Include observable issues that affect meaning, technical clarity, authorial consistency, or professionalism:

- ambiguous phrasing that changes interpretation
- inconsistent terminology
- weak transitions that obscure argument logic
- unclear figure/table descriptions
- malformed equation-adjacent prose
- broken references, duplicated punctuation, malformed titles, or obvious citation-format glitches
- high-confidence grammar, spelling, or capitalization issues
- sustained register, person, tense, or terminology drift
- redundant restatement, template residue, chatbot framing, or unfilled placeholders

Avoid subjective line editing, word blacklists, or style fingerprinting. Do not force variation for its own sake.

## Authorial Polishing

Use polishing only when the user explicitly requests a finding-level edit, paragraph/section polish, revision pass, or full-manuscript polish.

1. Read `references/authorial-polishing.md`.
2. Build the author-style baseline and immutable content ledger before editing.
3. For an explicit full-manuscript request, read `references/external-polishing-routing.md`; check only local Skill availability and ask once before optional enhancement.
4. Generate a new revision file and companion report. Never overwrite the source manuscript.
5. Re-run scientific, terminology, and claim-boundary checks on the revised content.

Nature Polishing may provide constrained academic-expression candidates when installed and authorized. Humanizer variants may only provide audit candidates; they must not control full rewrites, output AI scores, or optimize perplexity/burstiness.

## Final Proofing Sweep

Run when useful:

```bash
python3 scripts/proofing_scan.py <path-to-pdf-or-text> --max-hits 80
```

Use hits as candidates and spot-check before including them. Chatbot residue, placeholder, and citation-markup hits are publication-artifact warnings, not authorship judgments.

If code execution is unavailable, manually scan for duplicated punctuation, malformed equation-adjacent prose, product/language capitalization, citation-format glitches, and branch/quad ambiguity patterns such as `arctan(x/y)`.

## Output Contract

Generate the default report in Simplified Chinese (简体中文) unless the user requests another language.

### Anti-Generic Feedback Rules
You must NOT output low-value, vague suggestions (e.g., "增强创新性", "扩展文献", "提升贡献") that lack precise local facts or actionable advice.
If no concrete issues are identified, output "未发现明显问题" directly. Do not invent minor issues just to fill space.

### Finding Format
For every identified finding, you MUST include:
1. **Finding ID:** `S-01`, `S-02`, ... for Scientific Review; `T-01`, `T-02`, ... for detailed Text Quality Review.
2. **Location** (e.g., section number, page, line number, or equation/figure label).
3. **Problem** (factual explanation of the issue).
4. **Why it matters** (impact on manuscript validity or readability).
5. **Revision guidance / 修改指导** (the change objective, constraints to preserve, and concrete edit actions).
6. **Severity** (Critical, Major, Minor, or Writing Suggestion).
7. **Certainty** (确定错误, 证据不足, 疑似问题, or 需核对/确认).
*Note: Only output the Evidence Chain trace path if an issue or discrepancy in the chain is found.*

By default, revision guidance must not contain a paste-ready replacement paragraph. Use structure, operations, evidence-appropriate wording levels, or short phrase alternatives. Generate complete replacement sentences or paragraphs only after the user explicitly requests authorial polishing for a named finding, location, section, or manuscript.

Default Markdown report structure:
- Concise overall assessment (整体评估)
- Detailed findings grouped by **Severity** (from Critical down to Minor/Suggestions)
- Text quality review (文本质量审阅): one-sentence result by default, detailed table only when triggered
- High-priority fixes (高优先级修改建议)
- Items needing external verification (需核对/确认事项)
- Action plan table (修改行动表)

When detailed text-quality reporting is triggered, use:

```markdown
| Finding ID | 位置 | 文本问题 | 具体证据 | 影响 | 修改方向 |
|---|---|---|---|---|---|
```

### Action Plan Table

End the report with a concise action plan table when concrete fixes exist. Do not force rows when there are no actionable issues.

```markdown
| 优先级 | 问题 | 修改类型 | 建议修改位置 | 是否阻塞提交 |
|---|---|---|---|---|
```

Use:

- **优先级:** `P0`, `P1`, or `P2`
- **修改类型:** `主张强度校准`, `变量定义补充`, `表文一致性`, `方法说明补充`, `文献支撑补充`, `结构调整`, `表达澄清`, `文本清晰度`, `文风一致性`, `冗余压缩`, `作者化润色`, `格式/引用修正`, or `需外部核查`
- **是否阻塞提交:** `是`, `否`, or `取决于要求`

Prefix the `问题` cell with its finding ID when applicable, for example `[S-01]` or `[T-01]`. Do not use `P0/P1/P2` as finding IDs.

When actionable findings exist, end with one concise next-step example:

```text
按本文作者文风润色 finding S-01，仅修改相关位置，并保留事实、术语、数据、引用、公式和结论强度。
```
