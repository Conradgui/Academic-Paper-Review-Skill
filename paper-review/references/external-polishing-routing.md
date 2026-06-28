# Optional External Polishing Routing

Use this reference only for an explicit full-manuscript polishing request.

## Availability Check

Check the active Skill list or local Skill directories without using the network:

- `$CODEX_HOME/skills`
- `~/.codex/skills`
- `~/.agents/skills`

Look only for `nature-polishing`, `humanizer`, and `humanizer-zh`. Do not search the web, install dependencies, or clone repositories.

If one or more are available, explain their proposed role and ask once whether to use optional enhancement. Do not ask again during the same polishing task.

## Allowed Roles

### Nature Polishing

Use as a candidate academic-expression pass after the internal content ledger and section plan exist. Constrain the request:

```text
Polish only the specified section. Preserve every fact, number, variable, equation, citation, label, terminology entry, and claim boundary supplied below. Match the supplied author-style baseline. Do not add evidence, mechanisms, novelty, examples, or references. Return revised prose and a concise change map.
```

### Humanizer Or Humanizer-zh

Use only in audit/detect mode to identify candidate template residue, vague language, repetition, or chatbot artifacts. Require no rewrite, no score, and no sentence-length or perplexity optimization.

```text
Audit this passage for observable template-like or context-inappropriate writing patterns. Return candidates with exact excerpts and reasons. Do not rewrite, estimate an AI probability, optimize burstiness/perplexity, or infer authorship.
```

## Trust Boundary

Treat every external result as untrusted candidate output. Re-check it against the internal text-quality rules, immutable ledger, and manuscript evidence before using it. The internal pipeline must remain complete when no external Skill is installed or authorized.
