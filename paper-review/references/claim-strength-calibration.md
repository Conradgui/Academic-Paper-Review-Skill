# Claim Strength Calibration

Use this reference when a manuscript makes causal, significance, robustness, novelty, mechanism, policy, contribution, or generalization claims whose wording may be stronger than the evidence.

## Strength Ladder

| Claim strength | Typical wording | Evidence needed |
|---|---|---|
| Strong causal claim | proves, causes, leads to, determines, 证明, 导致, 决定性影响 | credible causal design, strong identification, robustness, and alternative explanations addressed |
| Strong robust support | fully supports, robustly improves, consistently confirms, 完全支持, 高度稳健, 稳定提升 | main model and core robustness checks point in the same direction with clear uncertainty handling |
| Moderate evidence | supports, is associated with, is positively related to, 支持, 正相关, 提供证据 | main evidence supports the claim, but design or robustness may limit strength |
| Boundary evidence | provides partial evidence, suggests, is consistent with, 边界证据, 初步证据 | mixed, marginal, subgroup-only, or specification-sensitive evidence |
| Exploratory signal | may indicate, offers a clue, warrants further study, 线索, 可能表明 | weak, preliminary, qualitative, or hypothesis-generating evidence |

## Calibration Rules

- If evidence is mixed, marginal, or sensitive to alternative specifications, recommend boundary-evidence wording.
- If the method is observational or correlational, avoid causal verbs unless the paper provides a credible identification strategy.
- If only a subgroup or robustness test supports the claim, do not let the abstract or conclusion state it as the paper's main result.
- If the manuscript uses "stable", "robust", "fully supports", or "proves", check whether the tables and appendices justify that strength.
- If a policy implication depends on causal interpretation, require explicit limitations or weaker wording.

## Required Output When Flagging Overclaiming

When overclaiming is a substantive finding, include:

```markdown
| Claim | Evidence | Calibrated Level | Minimal Phrase Options |
|---|---|---|---|
```

In review mode, identify the target evidence level and provide only short phrase or verb options. Do not draft a paste-ready replacement sentence or paragraph. Generate complete prose only when the user explicitly requests authorial polishing for that finding or location.

## Minimal Calibration Patterns

- `proves` -> `provides evidence consistent with`
- `causes` -> `is associated with` unless causal identification is credible
- `fully supports` -> `provides partial support for`
- `is robust` -> `remains directionally consistent in the reported checks`
- `mechanism is confirmed` -> `mechanism test offers suggestive evidence`
