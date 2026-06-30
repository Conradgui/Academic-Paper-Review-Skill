# Text Quality Audit

Use this reference for the text-quality track of every manuscript review. This track evaluates observable writing quality and manuscript-level style consistency. It must not infer who wrote the text or assign an AI probability.

## Lightweight Audit

Build an internal style baseline from the manuscript while respecting normal differences between sections. Check:

- clarity and precision of sentences
- stable terminology, abbreviations, variable names, and notation
- person, tense, register, and claim verbs appropriate to each section
- paragraph purpose, information order, and transitions
- redundancy, repeated conclusions, and low-information restatement
- abrupt shifts in vocabulary, syntax, formatting, or narrative stance
- template residue, chatbot framing, placeholders, or malformed citation artifacts
- high-confidence sentence mechanics that impede meaning, including broken parallel structure, unclear reference, or incomplete clauses
- first-use abbreviation expansion and stable abbreviation use
- punctuation and number/unit formatting when inconsistency affects professionalism or interpretation
- whether citations are grammatically integrated with the claim they support

Run a default lightweight AI-trace candidate audit for tool artifacts, unsupported significance, vague attribution, low-information analysis, formulaic structure, and sustained style drift. A single word or construction is not evidence of authorship or a text defect.

Do not compare Methods prose mechanically with Discussion prose. Methods may be procedural and past-tense while Discussion may be interpretive and more qualified. Exclude quotations, bibliography entries, equations, tables, code, and supplied templates when estimating the manuscript baseline.

## Detailed-Audit Trigger

Expand the text-quality section when the user explicitly requests it or when at least one material condition is present:

- the same problem recurs across two or more paragraphs or sections
- a problem affects the abstract, conclusion, research question, or a central claim
- style drift makes terminology, evidence strength, or meaning ambiguous
- adjacent passages show a sustained and unexplained register or manuscript-voice break
- publication text contains chatbot residue, unfilled placeholders, or broken AI citation markup

An isolated awkward sentence normally remains a concise Writing Suggestion. Do not create a detailed style profile merely to fill the report.

## Language Routing

Only after detailed reporting is triggered, or when the user explicitly requests language-focused review:

- Read `text-quality-zh.md` when the manuscript is mainly Chinese or contains material Chinese academic prose problems.
- Read `text-quality-en.md` when the manuscript is mainly English or contains material English academic prose problems.
- For mixed-language manuscripts, load both only when both languages contain substantive prose requiring detailed review. Do not load both for translated titles, abstracts, keywords, or isolated terminology.

The lightweight audit above remains mandatory for every manuscript and is sufficient when no material text-quality issue is present.

## AI-Trace Candidate Routing

Read `ai-trace-candidate-audit.md` when the user explicitly requests AI-trace review or the lightweight scan identifies a material candidate. Follow its verification chain before reporting any candidate. Its detailed candidate matrix is separate from the `T-*` finding table: promote only confirmed text problems to `T-*` and source/evidence problems to `S-*`.

## Reporting

If no material issue exists, write one sentence:

`未发现影响可读性、术语一致性或稿件语体连贯性的明显文本质量问题。`

Also include one lightweight AI-trace sentence without loading the detailed reference when no material candidate exists:

`未发现材料级 AI 痕迹候选或工具污染问题。`

Do not expand it into a matrix unless the detailed trigger fires.

If an isolated non-material issue exists, keep it in the same lightweight section as one concise sentence that names the location and edit direction. Do not assign a T-series finding ID, create a detailed table, or add an action-plan row for that issue. Promote it to a scientific finding only when it changes technical meaning or evidence interpretation.

If detailed reporting is triggered, use:

```markdown
| Finding ID | 位置 | 严重程度 | 判断确定性 | 文本问题 | 具体证据 | 影响 | 修改方向 |
|---|---|---|---|---|---|---|---|
```

Report only observable properties. Use labels such as `文风漂移`, `模板化表达`, `术语不一致`, `冗余复述`, or `语义不清`. Never label a passage as AI-generated.

## Guardrails

- Treat word lists and script hits as candidates, not proof.
- Prefer exact excerpts and local evidence over general style judgments.
- Do not force sentence-length variation, unusual vocabulary, first person, fragments, humor, or informality.
- Do not change scientific content while diagnosing writing quality.
- Keep scientific validity findings in the scientific-review track even when wording contributed to the problem.
