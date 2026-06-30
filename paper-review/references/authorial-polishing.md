# Authorial Polishing Protocol

Use this reference only when the user explicitly requests a local edit, section polish, revision pass, or full-manuscript polish. Review mode remains non-editing by default.

## Style Baseline Priority

Use the first reliable source available:

1. a **confirmed authorial baseline** from writing samples the user explicitly identifies as their own preferred style
2. a **manuscript-consistent baseline** from stable, unflagged passages in the manuscript
3. a **neutral academic baseline** appropriate to the language, paper type, and section

Only the first source justifies calling the result a match to the author's personal voice. The second supports manuscript consistency, not verified authorship. If the manuscript is too mixed or uniformly generic, state that limitation and ask the user to identify representative passages before a major rewrite. Match style, not the sample's facts or claims.

## Immutable Content Ledger

Before editing, record and preserve:

- core claims and evidence boundaries
- terminology, abbreviations, variables, and notation
- numbers, units, statistical values, and sample descriptions
- equations, citation keys, references, figure/table labels, and cross-references
- stated assumptions, limitations, and causal/associational wording

Never add examples, mechanisms, data, citations, or interpretations merely to improve prose.

## Scope Rules

### Finding Or Paragraph

- change only the named location
- preserve surrounding text verbatim unless a local transition must change
- return the revised passage plus a concise change note

### Section

- outline the section's paragraph functions before editing
- edit from claim and evidence outward, then improve flow and sentence quality
- run terminology and claim-strength checks after the edit

### Full Manuscript

1. confirm the source is editable
2. build the immutable ledger and style baseline
3. process one section at a time
4. verify each section against the ledger
5. run a final cross-section terminology, voice, and claim-boundary audit
6. write a new manuscript file and a companion Markdown polish report

Do not perform a single-pass whole-document rewrite.

## File And Format Policy

- Markdown, LaTeX, and TXT: create a new editable file under `paper-revisions/`
- DOCX: create a new DOCX only when document-editing and render-verification tools are available
- use `<source-stem>-polished-YYYY-MM-DD-HHMMSS.<ext>` for the manuscript
- use `<source-stem>-polish-report-YYYY-MM-DD-HHMMSS.md` for the companion report
- never overwrite the source manuscript
- for DOCX, preserve and visually verify headings, tables, equations, notes, citations, and pagination-sensitive elements as far as the tools allow
- when DOCX editing or render verification is unavailable, do not claim a preserved DOCX output; provide structured DOCX-ready revision text or request Markdown/LaTeX/TXT instead
- disclose that comments, tracked changes, text boxes, field codes, complex tables, and advanced styles may require manual Word verification
- PDF is review-only; request an editable source or return structured revision guidance

## Companion Report

Include:

- source and output paths
- polish scope and style-baseline source
- immutable-content checks performed
- an invariant verification table covering claims, terminology, numbers/units, citations, equations, and labels, with each category marked `Passed`, `Changed with author approval`, or `Needs verification`
- sections or findings changed
- unresolved ambiguities or content requiring author confirmation
- confirmation that the source file was not modified

## Final Verification

Compare source and polished output for numbers, variables, citations, equations, labels, and claim strength. Any unexplained change is a defect to fix, not a stylistic choice.
