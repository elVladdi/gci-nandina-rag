# EXP12 Feasibility Failure Forensic Protocol v0.1

## Status

```text
status = FORENSIC_DESIGN_PENDING_EXTERNAL_AUDIT
scientific_base_commit = 428dfecca5cff313f910032a28a8a3c7ae13c2ef
authorization_id_historical = EXP12_PLANNING_AUTH_001
attempt_id_historical = EXP12_PLANNING_ATTEMPT_001
historical_attempt_status = FAILED_ONE_SHOT / AUTHORIZATION_CONSUMED
forensic_non_governing = true
forensic_seed = 20262001
candidate_indices = 0..9999
other_seeds_allowed = false
alternative_thresholds_allowed = false
condition_selection_allowed = false
retrieval_allowed = false
```

This protocol addresses `EXP12-P61-F001 = FAILURE_OBSERVABILITY_GAP /
NON_INVALIDATING_FOR_ATTEMPT`. It does not retry, resume, replace, or
reinterpret the historical attempt. A future diagnostic may reproduce only
the frozen feasibility accounting for seed `20262001`; its aggregates cannot
be used as an official planning summary or retrieval input.

## Frozen Bindings

```text
config = src/configs/exp12_historical_diversity_control_v0.5.json
config_sha256 = 1565df9fd1ba61eaf6724035a1f186350567fa0ecb8edf5fca81ef8f06cd3264
runner = src/experiments/plan_exp12_historical_diversity_v01.py
runner_sha256 = cefb3dc5b16a6ce52c7313f5627ca1f56e08b814adb0823f2755f2b09bec64ac
sampling_universe = data/interim/new_historical_gate_v0.2/new_historical_eligible.csv
sampling_universe_sha256 = f039ad25f39dd4bff7c5318bfe49993d57c505ee0340d92ee95d1f9006751457
H100 = data/processed/data_aduanas_historico_clase87_v0.2.csv
H100_sha256 = 0990cdfe2a62638bff83a1182b0d6b0b727d670f63888044e99fd3ee0d7915ff
EVAL = data/processed/data_aduanas_evalset_clase87_v0.2.csv
EVAL_sha256 = 3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941
```

EVAL use is restricted to `DECLARACION` for DAM overlap. NANDINA labels,
descriptions, and performance fields from EVAL are prohibited.

## Frozen Scope

The production diagnostic must reject any request that changes seed `20262001`,
candidate count `10000`, target rows `2950`, volume range `[2802,3098]`,
coverage `1.0`, or maximum TVD `0.05`. It must validate the v0.5 contract and
all source identities before diagnostics.

For each candidate index, accounting follows the frozen generator order:

1. deterministic SHA-256 order and nearest prefix;
2. duplicate DAM-set rejection;
3. EVAL DAM-overlap rejection;
4. unique non-overlap classification by volume;
5. coverage and full-support TVD classification for volume-pass candidates.

The output contains only aggregate counters, frozen bindings, and invariant
results. It does not contain DAM lists, candidate rankings, selected
conditions, HHI condition values, threshold recommendations, retrieval
results, or EVAL metrics.

## Required Accounting

```text
candidate_indices_attempted = duplicate_dam_set_rejections + eval_overlap_rejections + unique_nonoverlap_candidates
unique_nonoverlap_candidates = volume_below_min_count + volume_within_range_count + volume_above_max_count
volume_within_range_count = coverage_and_tvd_pass_count + coverage_pass_tvd_fail_count + coverage_fail_tvd_pass_count + coverage_and_tvd_fail_count
final_unique_feasible_count = coverage_and_tvd_pass_count
minimum_required_unique_feasible = 30
historical_failure_condition_reproduced = final_unique_feasible_count < 30
```

## Future Output And Guard

Reserved output, not created by Prompt64:

```text
outputs/audits/exp12_planning_gate_v0.4/attempt_001_forensic/exp12_feasibility_failure_diagnostic_v0.1.json
```

The CLI is fail-closed unless `--execute-forensic-diagnostic` is supplied.
Use of that flag on the official pool requires a later, separate authorization
after external audit. No planning, condition selection, or retrieval is
authorized by this design.
