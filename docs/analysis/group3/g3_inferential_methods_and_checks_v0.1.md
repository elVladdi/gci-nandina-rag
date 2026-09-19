# G3-F03 Inferential Methods and Checks v0.1

## State and frozen inputs

G3-F03 was prospectively activated before any bootstrap result was calculated. The scientific baseline is `adf70d6eb880c567d6efa0f27b5c79259b8db2a6`, the governing G3-F01 contract and G3-F02 registry are read-only inputs, and the activation is `6750ed15b0e8ed62f5deba517eddf92fa2616bca`. No retrieval or frozen experiment was reexecuted.

The EVAL binding is 1,056 series nested in 67 DAM, SHA-256 `3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941`. Historical, corrected flat, corrected hierarchical, and corrected D1a case sets were paired exactly by `case_id` and `id_unico`; labels matched. D1a DAM/SERIE fields were recovered only through that exact frozen join.

## Point-estimate reconstruction

Before resampling, every historical and normative Top-1/3/5/10/50 numerator and mean, each MRR@100 contribution sum and mean, and hierarchical Recall@100/Recall@200 were reconstructed from the frozen case-level files. All reconstructed values matched the G3-F02 registry within `1e-12`.

## Dependence and bootstrap

The analysis unit is SERIE and the dependency group is DAM / DECLARACIÓN. DAM identifiers were sorted lexicographically. A single `numpy.random.default_rng(20263001)` PCG64 stream produced one `10000 x 67` matrix of DAM indices sampled with replacement. The same matrix was used for every result.

If a DAM appears `m` times in a replicate, all of its series contribute with multiplicity `m`. Each replicate is therefore the sum of multiplicity-weighted within-DAM contribution sums divided by the corresponding multiplicity-weighted series count. This preserves the series-weighted estimand and does not substitute an unweighted mean of DAM means.

## HE2_A and multiplicity

For each corrected normative strategy (flat, hierarchical, D1a), the five primary contrasts are paired historical-minus-normative differences for Top-1, Top-3, Top-5, Top-10, and MRR@100. Each five-metric family uses a two-sided 99% percentile interval (`0.005`, `0.995`), implementing the frozen Bonferroni familywise 95% coverage rule. No p-values are calculated.

Top-50 is reported once per strategy as supplementary uncertainty with a two-sided 95% percentile interval. It is outside the primary five-metric family and has no hypothesis-decision role.

## HE2_B

The only HE2_B inferential contrast is paired `Recall@200 - Recall@100` for corrected hierarchical retrieval. It uses a two-sided 95% percentile interval (`0.025`, `0.975`) with no multiplicity adjustment. Pool@200 is not duplicated as another contrast.

## Deliberate inferential exclusions

- `HE2_B_PHASE_E_FROZEN_ROLE_POOLS`: frozen candidate-pool coverage inventory.
- `HE2_B_PHASE_E_70_30`: variant not formally frozen for confirmatory use.
- `HE2_B_PHASE_E_DIAGNOSTIC_UNION`: diagnostic coverage ceiling without ranking.
- `EXP11A_HISTORICAL_BANK_SENSITIVITY`: bank size and composition remain coupled.
- `EXP11B_H150_H200_PAIRED_SENSITIVITY`: no seed superpopulation and repeated EVAL.
- `0B05C_ATTEMPT06_CORRECTIVE_SENSITIVITY`: corrected governed sensitivity state.
- `HE5_AMBIGUOUS_INCOMPLETE_DESCRIPTIONS`: description quality not operationalized.
- `HE5_HIERARCHICAL_PROXIMITY`: frozen hierarchy counts only.
- `HE5_INSUFFICIENT_HISTORICAL_PRECEDENTS`: no frozen insufficiency threshold.
- `HE5_INTERNAL_EVALUATION_SCOPE`: internal benchmark boundary.
- `HE5_EXPLANATION_EVIDENCE_LIMITS`: heterogeneous diagnostic scopes.
- `EXP12_DIVERSITY`: no selected conditions or retrieval results.

## Scope and decisions

The intervals quantify cluster-aware resampling uncertainty inside the fixed internal Chapter 87 benchmark. They do not establish external-population validity. No standardized post-hoc effect measure is introduced; the frozen absolute paired contribution difference is the effect measure. No p-values are calculated. HE2 and HE5 remain undecided, and G3-F04 remains not authorized and not started.

## Reproducibility and warnings

CSV and JSON were regenerated in a separate temporary output root with the same inputs and runtime and compared byte for byte. The only inherited documentation warning is that some G3-F02 `source_commit_binding` values use two literal `main=` labels; exact SHA, blob, and path provenance remains explicit.
