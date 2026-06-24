# Academic Paper Review Skill Generalization Plan

## Goal

Upgrade the repository from a LaTeX-only paper review skill into a broader academic manuscript review skill while preserving the original LaTeX-focused workflow.

## Decisions

- `main` becomes the general academic manuscript review version.
- `paper-review/` remains the general skill package with invocation `$paper-review`.
- `latex-paper-review/` preserves the LaTeX-focused skill package with invocation `$latex-paper-review`.
- A remote branch named `latex-paper-review` preserves the original LaTeX-only snapshot.
- Default general review output is Markdown.
- External source lookup is opt-in and must respect manuscript privacy and source quality.
- The GitHub repository should be renamed to `Academic-Paper-Review-Skill`.

## Validation Table

1. Preserve original LaTeX version -> Verify branch `latex-paper-review` exists locally and remotely.
2. Add LaTeX-specific package -> Verify `latex-paper-review/SKILL.md` frontmatter name is `latex-paper-review`.
3. Generalize main package -> Verify `paper-review/SKILL.md` supports Markdown, DOCX, PDF, LaTeX, and plain text, and defaults to Markdown output.
4. Avoid invocation conflict -> Verify README examples use `$paper-review` and `$latex-paper-review` distinctly.
5. Validate skills -> Run `quick_validate.py` for both skill directories.
6. Verify proofing script -> Run syntax check and a sample scan.
7. Update GitHub -> Rename repository, update description, topics, and remote URL.

## Execution Evidence

- Created and pushed the `latex-paper-review` branch from the original LaTeX-only commit.
- Copied the original LaTeX skill package to `latex-paper-review/`.
- Updated `latex-paper-review/SKILL.md` frontmatter to `name: latex-paper-review`.
- Rewrote `paper-review/SKILL.md` as a general academic manuscript review skill covering Markdown, DOCX, PDF, LaTeX, and plain text.
- Rewrote `README.md` around the general `$paper-review` skill and the specialized `$latex-paper-review` skill.
- Verified both skill directories with `quick_validate.py`.
- Verified both `proofing_scan.py` scripts compile with `PYTHONPYCACHEPREFIX=/tmp/paper-review-pycache python3 -m py_compile ...`.
- Verified both proofing scripts catch `PUNC_DOUBLE_COMMA`, `CAP_JAVASCRIPT`, and `ARCTAN_DIV` on a text sample.
