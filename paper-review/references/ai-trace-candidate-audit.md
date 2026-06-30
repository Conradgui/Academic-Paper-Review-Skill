# AI-Trace Candidate Audit

Use this reference when an AI-trace candidate appears during the default lightweight text-quality audit or when the user explicitly requests a detailed AI-trace candidate audit.

## Boundary

Evaluate observable manuscript patterns and their consequences. Do not infer authorship, claim that a passage is AI-generated, or use style as evidence of misconduct. Do not output an AI probability, detector score, authenticity score, or prediction about who wrote the text.

A surface pattern is only a candidate. The review target is the underlying defect, if one exists: vague content, unsupported significance, source-to-claim mismatch, citation pollution, terminology drift, section mismatch, or publication residue.

## Default Lightweight Audit

Screen every manuscript for these candidate families without generating a detailed matrix by default:

- **Tool or publication artifacts:** chatbot-facing language, unfilled placeholders, broken citation markup, leaked tool metadata, or tool-tracking URLs.
- **Inflated significance:** generic claims about importance, broad trends, impact, novelty, or legacy without manuscript-specific evidence.
- **Vague attribution:** `experts`, `many studies`, `researchers`, or equivalent wording that lacks a traceable source or exaggerates the number or agreement of cited sources.
- **Low-information analysis:** sentences that announce what a result `highlights`, `reflects`, `promotes`, or `demonstrates` without naming the mechanism, condition, evidence, or consequence.
- **Formulaic structure:** repeated binary contrasts, negative build-ups, rule-of-three lists, generic challenge/future sections, or canned conclusions that replace logical development.
- **Style and terminology drift:** unexplained changes in technical vocabulary, citation behavior, English variety, formatting, or claim strength.

A single word, transition, passive construction, or isolated rhetorical pattern is not a finding.

## Detailed-Audit Trigger

Produce the detailed candidate matrix only when at least one condition is met:

- the user explicitly requests an AI-trace candidate audit
- a high-confidence tool or publication artifact appears
- the same candidate family recurs across two or more paragraphs or sections
- the candidate affects the abstract, conclusion, research question, or a central claim
- the candidate creates an evidence, citation, terminology, or meaning risk

Co-occurrence alone is insufficient when every use is specific, evidence-linked, and appropriate to the section.

## Verification Chain

Apply this chain to every reported candidate:

`Surface candidate -> Context function -> Specificity -> Evidence/citation -> Section fit -> Final judgment`

1. **Surface candidate:** quote the exact local pattern and identify its family.
2. **Context function:** determine what the sentence or paragraph is trying to do.
3. **Specificity:** test whether the wording names the actual object, condition, mechanism, quantity, or consequence. Ask whether it could be pasted into many unrelated papers unchanged.
4. **Evidence/citation:** check whether the manuscript's data, result, citation, or appendix supports the statement and whether plural or consensus wording matches the number and scope of sources actually provided.
5. **Section fit:** preserve legitimate differences between Methods, Results, Discussion, and Conclusion.
6. **Final judgment:** select one exact outcome from the list below.

## Outcomes And Promotion

- **Confirmed Text Issue:** the candidate causes vagueness, redundancy, mechanical flow, terminology drift, or unsuitable register. If material, promote it to a `T-*` finding.
- **Source Integrity Risk:** the candidate exposes an unsupported claim, citation mismatch, source-count exaggeration, or tool-polluted reference. Promote it to an `S-*` finding.
- **Contextually Acceptable:** the construction is specific, evidence-linked, and suitable for the section or discipline. Do not create a finding or action-plan row.
- **Needs Verification:** the manuscript alone cannot establish source accuracy or disciplinary acceptability. Follow the external-research opt-in policy; do not search without authorization.

Candidate IDs use `AIC-01`, `AIC-02`, and so on only inside the detailed candidate matrix. They are audit trace IDs, not findings or action priorities.

## Detailed Output

When detailed reporting is triggered, include both plausible confirmed candidates and high-signal candidates judged contextually acceptable. Do not enumerate every word-list match.

```markdown
| Candidate ID | 位置 | 可观察模式 | 原文证据 | 深层核验 | 结论 | 修改方向 |
|---|---|---|---|---|---|---|
```

Only `Confirmed Text Issue`, `Source Integrity Risk`, and unresolved `Needs Verification` items may be promoted to findings or the action plan. Keep the candidate ID visible when promoting an item so the audit trail remains traceable.

If no material candidate exists during default review, report one sentence:

`未发现材料级 AI 痕迹候选或工具污染问题。`

## Anti-False-Positive Rules

- Do not ban adverbs or remove justified hedging and uncertainty.
- Do not treat passive voice as defective when it fits disciplinary or Methods conventions.
- Do not ban em dashes, Oxford commas, simple copular clauses, or formal academic vocabulary.
- Do not treat three-item lists, binary contrasts, repeated technical terms, or regular sentence lengths as defects unless repetition becomes mechanical or obscures reasoning.
- Do not force sentence-length variation, fragments, second person, informal language, personal anecdotes, or human subjects for inanimate scientific processes.
- Do not replace precise disciplinary terms merely to increase lexical variety.
- Do not use detector avoidance as a revision objective. Improve specificity, evidence alignment, source integrity, and section-appropriate clarity.

## Source-Integrity Boundary

Use only material available in the manuscript by default. You may detect malformed identifiers, broken tool markup, inconsistent citation metadata, or a mismatch between a claim and a provided source. Do not resolve DOI/ISBN records or search external databases unless the user explicitly authorizes external research.
