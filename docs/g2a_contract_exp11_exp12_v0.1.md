# G2A Contract for EXP-11 and EXP-12 v0.1

## Status

This document and the two v0.3 JSON configurations are candidate pre-execution contracts. They are pending external audit and do not authorize EXP-11 or EXP-12 execution.

The fixed evaluation contract is `data/processed/data_aduanas_evalset_clase87_v0.2.csv` with SHA-256 `3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941` and 1,056 cases. The frozen H100 reference is `data/processed/data_aduanas_historico_clase87_v0.2.csv` with SHA-256 `0990cdfe2a62638bff83a1182b0d6b0b727d670f63888044e99fd3ee0d7915ff`, 2,950 rows and 28 DAM.

## EXP-11 Candidate Design

H25, H50 and H75 use independent complete-DAM subsets; nesting is `NOT_REQUIRED_STRUCTURALLY_INFEASIBLE`. Each condition receives its own SHA-256 order over the 26 eligible non-dominant DAM: `SHA-256(seed:condition_id:dam_id)`. The selector chooses the prefix nearest the condition target, with ties resolved by fewer prefix DAM and the SHA-256 of sorted final DAM identifiers. It never uses eval queries, labels, NANDINA, Top-k or MRR.

The initial stream starts at `20261001`, increments by one and is evaluated independently per condition. H25 must include zero dominant DAM and H75 both. Their original ten frozen candidate schedules remain `20261001` through `20261010`. H50 is stratified prospectively: a paired seed builds `H50-D1` with `SHA-256(seed:H50:D1:dam_id)` and forced inclusion of `118-2026-10-128583-00`, and `H50-D2` with `SHA-256(seed:H50:D2:dam_id)` and forced inclusion of `118-2026-10-146957-00`; each excludes the other dominant. The first five valid pairs, `20261001` through `20261005`, are frozen candidates. Each pair must remain within the H50 band, use complete DAM, contain exactly one appropriate dominant and be unique within its stratum. H100 remains one frozen reference. H150 and H200 remain disabled and fail closed until a separately approved expanded historical-data gate exists.

## EXP-12 Candidate Design

EXP-12 has no sampling universe yet. It fails closed when the expanded historical gate is absent and expressly cannot use H100 as a silent replacement; therefore all EXP-12 execution is blocked until that gate exists. After an approved source exists, D-LOW, D-MID and D-HIGH will each use ten predeclared seeds (`20262001` through `20262010`) and complete-DAM subsets near 2,950 rows within the frozen candidate integer tolerance.

## Microclose 1B Record

The original EXP-11 design used nominal targets H25=738, H50=1,475, H75=2,213 and H100=2,950, each derived as `floor(fraction * 2950 + 0.5)`, with nested complete-DAM subsets. The H100-only scan of 100,000 seeds is preserved as supplementary evidence of its failure. It is superseded by the structural proof and independent-condition correction below.

The authorized H100-only planner recorded `DESIGN_INFEASIBLE`: none of the initial ten seeds was valid and no set of ten valid, unique chains was found in 100,000 consecutive candidates. Consequently there are no final EXP-11 replicate seeds and no EXP-11 retrieval authorization. This is a methodological fail-closed result requiring external audit, not an EXP-11 scientific result.

EXP-12 fixes DAM concentration HHI as its sole primary diversity variable, with derived effective DAM, dominant share and Top-2 share. It requires 2,802-3,098 rows, complete DAM, 100% H100 NANDINA coverage and TVD at most 0.05 against the H100 label distribution. Per seed it generates 10,000 candidate DAM prefixes, requires at least 30 feasible unique candidates, and selects HHI quantiles 0.10, 0.50 and 0.90 for D-HIGH, D-MID and D-LOW. Exact and near-duplicate checks are secondary descriptive measures using the versioned Group 1 normalization and `token_jaccard_rare_block` method.

For each EXP-12 seed and candidate index, DAM identifiers are ordered by `SHA256(seed:candidate_index:dam_id)`. The nearest complete-DAM prefix to 2,950 rows is retained, breaking volume ties by fewer DAM and then the SHA-256 of sorted DAM identifiers; duplicate sorted DAM tuples are removed. Feasible candidates are then filtered by the frozen volume, coverage, TVD and zero-eval-DAM-overlap rules. HHI is the only primary selection variable: after HHI-ascending sorting, D-HIGH/D-MID/D-LOW use quantiles 0.10/0.50/0.90 with the frozen SHA tie-break, distinct DAM sets and strict HHI order. HHI, effective DAM, DAM count, dominant-DAM share and Top-2 DAM share define the diversity report; they do not use Top-k or MRR to construct a condition.

## Microclose 1C Structural Correction

G2A-F008 is frozen as `PRE_EXECUTION_DESIGN_INFEASIBILITY`, scoped to the superseded nested EXP-11A design. The two dominant DAM contain 1,045 and 940 series, leaving 965 in all remaining DAM. The frozen bands are H25=590-886, H50=1327-1623 and H75=2065-2361. Therefore H25 excludes both dominants, H50 requires exactly one, and H75 requires both. A nested H25 inside H75 would require at least `590 + 1045 + 940 = 2575` rows, greater than H75's upper bound 2,361. No retrieval occurred before this correction and Group 1 remains untouched.

The authorized independent planner produced ten unique compositions for each H25/H50/H75 condition. It records realized rows, realized fraction, absolute deviation, DAM count, dominant membership, composition SHA-256 and post-selection descriptors: DAM HHI, effective DAM, NANDINA coverage and independent-DAM support. These descriptors are not selection criteria.

G2A-F009 is a `DECLARED_LIMITATION`: historical bank size and DAM composition cannot vary independently under frozen H100 volume constraints. EXP-11A is therefore interpreted only as **sensitivity of historical retrieval performance to nominal historical bank size under complete-DAM sampling and the composition constraints of the frozen H100 bank**. An isolated causal effect of size is not claimable. This does not block redesigned EXP-11A, but it blocks causal overstatement.

## EXP-12 Conditional Freeze

`CONTRACT_STATUS = CONDITIONAL_FROZEN_PENDING_NEW_HISTORICAL_GATE`. EXP-12 remains non-executable with `sampling_universe=PENDING_NEW_HISTORICAL_GATE` and `must_not_fallback_to_h100=true`. Its candidate specification is unchanged: target 2,950, deviation 148, primary DAM HHI, H100 NANDINA coverage 1.0, TVD at most 0.05, 10,000 candidates, at least 30 feasible candidates and HHI quantiles 0.10/0.50/0.90. Near-duplicate measurement remains the canonical `token_jaccard_rare_block` method at 0.90/0.95/0.98 and is descriptive only. Before real retrieval, the future gate must report HHI q10/q50/q90 and span, effective-DAM q10/q50/q90 and ratio; it must fail closed unless `HHI_DLOW > HHI_DMID > HHI_DHIGH`, and external manipulation-strength review is required without adding a new threshold.

## Execution Manifest Contract

Every future EXP-11 run must record nominal condition, realized rows/fraction, DAM count, DAM HHI, effective DAM, NANDINA coverage, dominant structure and historical-support summary as descriptive fields, in addition to experiment, replicate and run identity; UTC timestamp and Git commit; historical and eval paths, SHA-256 values, complete DAM list; zero DAM overlap; selector version and seed; retrieval configuration; output hashes; and case-level evidence. Case-level output must include `reference_nandina_supported_in_bank` and `reference_independent_dam_support_count`. These fields are never selection criteria. The H50 primary analysis is `POOLED_EQUAL_WEIGHT_5_D1_5_D2`; `DOMINANT_STRATUM_COMPARISON` is secondary and not causal. EXP-12 additionally records HHI and effective DAM. The primary evaluation denominator remains the fixed 1,056-case evalset; any common-clean subset is secondary and must be defined against an approved maximum historical universe.

## Microclose 1D H50 Correction

G2A-F010 records a pre-execution imbalance in v0.1 H50: D1 appeared 2/10 times and D2 8/10 times. The respective observed HHI means were 0.5197288651 and 0.4232268197. `exp11_independent_condition_feasibility_v0.2.json` is the corrected planning evidence; it retains v0.1 as evidence of the finding and verifies unmodified H25/H75 composition SHA-256 lists. No retrieval, EXP-12 real planning, Top-k, MRR or scientific artifact regeneration occurred.

## Microclose 1E Candidate Versioned Freeze

The G2A taxonomy preserves historical provenance. F001 is `PARTIALLY_RESOLVED` because the historical environment is incomplete but explicitly delimited; F002 and F005 are `NOT_RECOVERABLE`; F003 and F004 are `PARTIALLY_RESOLVED`; F006, F008 and F010 are `VERIFIED_IN_G2`; F007 remains `OPEN` as a `FUTURE_DEPENDENCY`; and F009 is `VERIFIED_IN_G2` with its declared non-causal interpretation. These historical limitations do not reopen Group 1 and do not block EXP-11A H25/H50/H75/H100, while F007 continues to block EXP-11B H150/H200 and every EXP-12 execution.

`EXP11_V3_DESIGN = ACCEPTED_PENDING_VERSIONED_FREEZE`. The verified H50 state is five D1 and five D2 replicates from the five paired seeds already frozen in the v0.2 evidence. `EXP12_V3_METHOD = CONDITIONAL_ACCEPTED_PENDING_NEW_HISTORICAL_GATE`; `CONDITIONAL_FROZEN_PENDING_NEW_HISTORICAL_GATE`, `execution_authorized=false` and `must_not_fallback_to_h100=true` remain unchanged.

The following external thesis-governance documents are historical administrative evidence only. They are not inputs to a clean-checkout execution; the versioned configurations, planner, tests and G2A artifacts inside this repository are the reproducible dependency set.

| Path | SHA-256 | Role | Required for clean checkout execution |
|---|---|---|---|
| `C:/Users/Vladimir/OneDrive/Documentos/Maestría UNMSM/Cuarto ciclo/Tesis/Anexo 2 - Tesis/Fichas de mejora/Grupo 2/EXP-11_sensibilidad_tamano_banco_historico_v3.md` | `9478e4336cd01863432bc08eff1143e10dcbfa638085bbce81a8e7f54b1410d5` | `EXTERNAL_TESIS_GOVERNANCE_DOCUMENT` | false |
| `C:/Users/Vladimir/OneDrive/Documentos/Maestría UNMSM/Cuarto ciclo/Tesis/Anexo 2 - Tesis/Fichas de mejora/Grupo 2/EXP-12_efecto_diversidad_banco_historico_volumen_controlado_v3.md` | `07e1eff49501b1d6b1c3c088ec37c8cb31869788e2f74a66397fee3a0c3c7dfb` | `EXTERNAL_TESIS_GOVERNANCE_DOCUMENT` | false |

The candidate gate is `PENDING_EXTERNAL_FINAL_AUDIT` with recommendation `APPROVED_WITH_NONBLOCKING_LIMITATIONS`. It is not a final approval and leaves both EXP-11A and EXP-12 execution unauthorized until the external final audit after the versioned clean-checkout review.

## G2A Operational Final Closure

The external final audit approved candidate commit `c9751f67165b0bf6e06b54e4e979e7258481ded6` on `2026-08-31`. `G2A_FINAL_GATE = APPROVED_WITH_NONBLOCKING_LIMITATIONS` and `G2A_CLOSED = true`; the historical limitations F001/F002/F003/F004/F005/F009 remain nonblocking, F007 remains an `OPEN / FUTURE_DEPENDENCY`, and Group 1 is not reopened.

`EXP11A_AUTHORIZED = true` only for `H25`, `H50`, `H75` and `H100`, with `execution_authorized_scope = EXP11A_H25_H50_H75_H100_ONLY`. The frozen compositions, H50 5 D1/5 D2 paired seeds, tolerances, BM25 configuration, metrics, evalset and hashes remain unchanged. `EXP11B_AUTHORIZED = false`: H150 and H200 stay disabled with source `PENDING_NEW_HISTORICAL_GATE`. `EXP12_AUTHORIZED = false` and its conditional freeze remains unchanged. `NEXT_REQUIRED_DATA_GATE = AFTER_EXP11A_BEFORE_EXP11B_AND_EXP12`; `NEW_HISTORICAL_DATA_REQUIRED_NOW = false` and its next trigger is `AFTER_EXP11A_EXTERNAL_AUDIT`.

## Pending Scientific Decisions

External audit must review the 30 EXP-11 independent compositions and their F009 composition coupling before any EXP-11 retrieval. It must also approve a new historical gate before any EXP-12 execution. The contracts prevent retrospective selection because no performance metric is an input to either selector.
