# Chinese Academic Text Quality

Use this reference only for substantive Chinese manuscript prose.

## Check Dimensions

### Clarity And Sentence Control

- identify sentences carrying multiple unrelated propositions or missing an explicit subject
- check whether modifiers attach to the intended term
- split overloaded sentences only when the logical relation remains explicit
- preserve established technical terms instead of replacing them for variety

### Academic Register

- flag sustained shifts between academic prose, policy slogans, marketing language, conversational commentary, and administrative-document phrasing
- replace broad evaluative language with the manuscript's actual object, evidence, condition, or consequence
- retain necessary disciplinary conventions; formality alone is not a defect

### Translation And Bilingual Consistency

- check literal English-to-Chinese syntax, unnecessary nominalization, stacked `的`, and unclear pronoun references
- keep English abbreviations, variable names, product names, and mathematical symbols in canonical form
- flag unexplained switching between Chinese and English names for the same construct

### Cohesion And Redundancy

- check repeated paragraph conclusions, circular restatement, and mechanically repeated transition phrases
- require each paragraph to advance one main function: context, gap, method, result, interpretation, limitation, or implication
- do not delete repetition that is needed to distinguish a definition, result, and boundary

### Candidate Template Patterns

Candidate patterns include unsupported broad framing, empty significance statements, repeated `综上所述`-style summaries, formulaic policy recommendations, and chatbot-facing instructions. A phrase such as `此外`, `本文`, `研究表明`, or `综上` is not an error by itself. Flag it only when local use is repetitive, vague, or logically empty.

## Section Guardrails

- Abstract: concise problem, method, main evidence, and bounded implication
- Introduction: field context, precise gap, and present study without inflated novelty
- Methods: reproducible sequence and stable terminology; regular syntax is acceptable
- Results: observation and quantitative support before broad interpretation
- Discussion: interpretation, comparison, uncertainty, and limits may use more qualification
- Conclusion: no new evidence and no claim stronger than the results

Do not add anecdotes, personal opinions, fabricated examples, or new factual detail to make Chinese prose sound more natural.
