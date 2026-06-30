# Empirical Paper Audit

Use this reference only when the manuscript has empirical-research features such as variables, models, regression, experiments, robustness checks, heterogeneity, mechanism tests, tables of results, or quantitative claims.

This is an enhancement module. It does not replace the Core Manuscript Audit Protocol in `SKILL.md`.

## Variable Audit

Check whether each important variable or construct has:

- concept definition
- operationalization or measurement rule
- data source
- unit of observation
- time window
- expected direction or role in the model
- overlap risk with other variables
- enough detail for a reader to reproduce or understand the measure

Flag variables that are named in the hypothesis, model, table, or conclusion but not defined clearly enough.

## Model And Identification Audit

Check whether the model can answer the research question:

- dependent variable and key independent variable align with the research question
- controls are justified and not mechanically overlapping with the treatment/explanatory variable
- fixed effects, clustering, sample restrictions, and time windows are stated clearly
- causal wording is supported by design; otherwise recommend associational wording
- sample size, cluster count, missing data, and selection criteria are sufficient for the stated claims
- model assumptions and identification boundaries are acknowledged
- effect sizes and confidence intervals are reported when they are needed to interpret practical or scientific importance
- statistical assumptions, diagnostics, and multiple-testing adjustments are addressed when applicable
- missing-data handling is stated and does not silently change the estimand or sample
- sample-size or power reasoning is proportionate to the design and claim
- machine-learning evaluations prevent train/validation/test leakage and separate tuning from final evaluation
- human- or animal-subject studies report ethics approval and consent when required

## Robustness And Extension Audit

Check whether robustness, sensitivity, mechanism, and heterogeneity tests support the main claim:

- alternative variable definitions
- lagged or placebo specifications
- sensitivity checks
- small-cluster or weak-inference risks
- heterogeneity tests
- mechanism tests
- subgroup claims

Distinguish between main-claim support and weaker exploratory evidence.

## Table/Text Consistency Audit

Compare result tables with the surrounding prose:

- significance stars and p-value wording
- coefficient direction and magnitude
- sample size and model count
- whether "stable", "robust", "significant", or "supports" is stronger than the table allows
- whether non-significant, mixed, or boundary results are described honestly

When the text overstates results, propose a calibrated wording instead of only flagging the problem.

## Conclusion Boundary Audit

Check whether the conclusion, discussion, and policy implications stay within the evidence:

- no causal conclusion without credible identification
- no policy recommendation stronger than the design supports
- no generalization beyond sample, region, period, or setting
- limitations are not contradicted by stronger language elsewhere
- practical implications are tied to actual findings
