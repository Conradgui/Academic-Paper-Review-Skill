# Text Quality Audit

Use this reference for the text-quality track of every manuscript review. This track evaluates observable writing quality and authorial consistency. It must not infer who wrote the text or assign an AI probability.

## Lightweight Audit

Build an internal style baseline from the manuscript while respecting normal differences between sections. Check:

- clarity and precision of sentences
- stable terminology, abbreviations, variable names, and notation
- person, tense, register, and claim verbs appropriate to each section
- paragraph purpose, information order, and transitions
- redundancy, repeated conclusions, and low-information restatement
- abrupt shifts in vocabulary, syntax, formatting, or authorial stance
- template residue, chatbot framing, placeholders, or malformed citation artifacts

Do not compare Methods prose mechanically with Discussion prose. Methods may be procedural and past-tense while Discussion may be interpretive and more qualified. Exclude quotations, bibliography entries, equations, tables, code, and supplied templates when estimating the author's baseline.

## Detailed-Audit Trigger

Expand the text-quality section when the user explicitly requests it or when at least one material condition is present:

- the same problem recurs across two or more paragraphs or sections
- a problem affects the abstract, conclusion, research question, or a central claim
- style drift makes terminology, evidence strength, or meaning ambiguous
- adjacent passages show a sustained and unexplained register or authorial-voice break
- publication text contains chatbot residue, unfilled placeholders, or broken AI citation markup

An isolated awkward sentence normally remains a concise Writing Suggestion. Do not create a detailed style profile merely to fill the report.

## Language Routing

- Read `text-quality-zh.md` when the manuscript is mainly Chinese or contains Chinese-influenced academic prose.
- Read `text-quality-en.md` when the manuscript is mainly English.
- For mixed-language manuscripts, load both only when both languages contain substantive prose. Do not load both for translated titles, abstracts, keywords, or isolated terminology.

## Reporting

If no material issue exists, write one sentence:

`未发现影响可读性、术语一致性或作者文风连贯性的明显文本质量问题。`

If detailed reporting is triggered, use:

```markdown
| Finding ID | 位置 | 文本问题 | 具体证据 | 影响 | 修改方向 |
|---|---|---|---|---|---|
```

Report only observable properties. Use labels such as `文风漂移`, `模板化表达`, `术语不一致`, `冗余复述`, or `语义不清`. Never label a passage as AI-generated.

## Guardrails

- Treat word lists and script hits as candidates, not proof.
- Prefer exact excerpts and local evidence over general style judgments.
- Do not force sentence-length variation, unusual vocabulary, first person, fragments, humor, or informality.
- Do not change scientific content while diagnosing writing quality.
- Keep scientific validity findings in the scientific-review track even when wording contributed to the problem.
