# G2A Reproducibility Microclose v0.1

## Scope and Status

This is a documentation and pre-execution-contract microclose. It neither ran EXP-11/EXP-12 nor regenerated scientific artifacts. The candidate gate is `PENDING_EXTERNAL_FINAL_AUDIT` with recommendation `APPROVED_WITH_NONBLOCKING_LIMITATIONS`; G2A is not declared closed.

Group 1 remains closed evidence. The clean-checkout gate records 229 historical tests, zero failures, zero errors, zero skips, canonical SHA 55/55 and no scientific-result change.

## D1a Forensic Result

`outputs/training/text2trade_mnrl_v0.2/training_metadata.json` records a start at `2026-08-30T05:06:12.903099+00:00`, command `python -B -m src.experiments.train_text2trade_mnrl_v02`, seed `2026`, Python `3.10.11`, Windows `10.0.26200` and Torch `2.12.0+cpu`.

Local Git reconstruction used `git log`, `git log --follow`, `git show`, `git rev-list` and `git diff`. `a91269ed3b5c52d08511063465be130adf185f0a` modified the training runner at `2026-08-30T05:05:54Z`, about 18 seconds before training began. `c82e6232ef5f0678c3b10fbdb9c3850910aacee0` was the last config modification before training. Direct dependency provenance was recovered for `src/retrieval/text2trade_mnrl_v02.py` and `src/utils/paths.py`; neither changed during the final D1a interval. No versioned artifact establishes the complete repository HEAD that executed training, so `execution_repository_head = UNKNOWN`. F003 is therefore `PARTIALLY_RESOLVED`, not `NOT_RECOVERABLE`.

## H150/H200

F007 is `OPEN / FUTURE_DEPENDENCY`. It is not a defect in Group 1 and does not block contractual G2A work or EXP-11A H25/H50/H75/H100. It blocks EXP-11B H150/H200 and all EXP-12 execution until a separately approved, frozen expanded historical bank exists. No prospective configuration invents a path or SHA for that source.

## Prospective Contracts

`src/configs/exp11_historical_size_sensitivity_v0.3.json` and `src/configs/exp12_historical_diversity_control_v0.3.json` are candidates only. Their deterministic planning logic is implemented in `src/experiments/plan_historical_bank_conditions_v03.py`. It has no retrieval, ranking or metric code. The contracts retain the v0.2 fixed eval SHA and H100 reference, use complete DAM units, predeclare ten candidate seeds, forbid performance-based selection and fail closed when an expanded historical-data gate is missing.

The audit inventory, traceability matrix, environment registry and asset classification distinguish historical records from current environment observations. Heavy models and index structures are not added to Git. Current package observations are marked `CURRENT_ENV_ONLY` and are not treated as historical dependency locks.

## Microclose 1B Methodological Freeze

The H100-only EXP-11 planner read DAM identifiers and row counts from the frozen 2,950-row reference, with no retrieval and no eval descriptions or labels. The initial seeds `20261001` through `20261010` all retained complete-DAM nesting but failed at least one frozen size tolerance. The deterministic acceptance stream then examined 100,000 consecutive seeds and found no ten valid, unique DAM chains. The recorded outcome is `DESIGN_INFEASIBLE`; final candidate seeds are empty and EXP-11 retrieval remains unauthorized pending external methodological review.

EXP-12 remains synthetic-contract-only. Its frozen selector uses complete DAM prefixes nearest 2,950 rows, H100 NANDINA coverage of 1.0, TVD at most 0.05, DAM concentration HHI quantiles 0.10/0.50/0.90, and fail-closed conditions. F007 blocks every EXP-12 execution until an approved expanded historical gate exists. The Group 1 canonical near-duplicate method was found at `src/evaluation/group_split_by_dam.py` in provenance commit `327762363898be99d5c66c1e7e0ff2178b8ed221`: NFC/casefold whitespace normalization with `token_jaccard_rare_block` at thresholds 0.90/0.95/0.98. It is descriptive only, never a selection objective.

## Microclose 1C Independent EXP-11 Design

G2A-F008 is frozen as `PRE_EXECUTION_DESIGN_INFEASIBILITY`, not as an unsuccessful seed search. Under complete DAM and the frozen plus/minus 148 row bands, H25 must exclude both dominant DAM, H50 must contain exactly one, and H75 must contain both. A nested H25 inside H75 would have at least `590 + 1045 + 940 = 2575` rows, above H75's 2,361-row maximum. The 100,000-seed scan remains supplementary evidence. No scientific result was affected and Group 1 is not reopened.

The corrected selector uses independent SHA-256 seed streams and complete-DAM prefixes for H25/H50/H75. It accepted ten unique compositions for each condition, recorded in `exp11_independent_condition_feasibility_v0.1.json`; H100 stays the sole frozen reference. Post-selection descriptors show the natural DAM composition induced by volume and are not selector inputs. G2A-F009 is the declared limitation that EXP-11A measures sensitivity to nominal bank size under those natural composition constraints, not an isolated causal effect of size.

EXP-12 remains `CONDITIONAL_PENDING_NEW_HISTORICAL_GATE`: its HHI, H100 NANDINA/TVD and canonical near-duplicate specification are frozen, but all real-data planning and execution remain blocked by F007.

## Microclose 1D H50 Stratification and Final Freeze Preparation

G2A-F010 is `OPEN_CORRECTABLE_PRE_EXECUTION` with severity `S2`: the v0.1 H50 schedule had only 2 D1 and 8 D2 dominant-DAM compositions. The observed pre-retrieval mean HHI was 0.5197288651 for D1 and 0.4232268197 for D2, so an unstratified H50 aggregate would depend on arbitrary seed frequency. This affects no scientific result and does not reopen Group 1.

`exp11_independent_condition_feasibility_v0.2.json` preserves v0.1 and keeps H25/H75 composition SHA-256 lists identical. It replaces only H50 with five accepted paired seeds: `20261001` through `20261005`. Every pair creates one complete-DAM H50-D1 candidate forced to include `118-2026-10-128583-00` and exclude D2, and one H50-D2 candidate forced to include `118-2026-10-146957-00` and exclude D1. Both must be in the frozen 1327-1623 band, contain exactly one dominant DAM, and be unique within stratum. The primary future analysis is `POOLED_EQUAL_WEIGHT_5_D1_5_D2`; D1/D2 comparison is descriptive and cannot establish a causal effect of dominant identity.

The EXP-11 future manifest now requires nominal/realized condition descriptors, DAM HHI/effective DAM, coverage, dominant structure and historical support, plus case-level NANDINA support fields. They are post-selection descriptors only. EXP-12 is now `CONDITIONAL_FROZEN_PENDING_NEW_HISTORICAL_GATE`, remains non-executable, cannot fall back to H100, and will require HHI/effective-DAM quantile reporting plus strict HHI ordering and external manipulation-strength review before real retrieval.

## Microclose 1E Taxonomy Normalization and Candidate Freeze

F001 is `PARTIALLY_RESOLVED`: historical environment completeness is limited but now explicitly delimited. F002 and F005 are `NOT_RECOVERABLE`; F003 and F004 are `PARTIALLY_RESOLVED`; F006, F008 and F010 are `VERIFIED_IN_G2`; F007 remains `OPEN` with dependency type `FUTURE_DEPENDENCY`; F009 is `VERIFIED_IN_G2` and retains the declared non-causal size limitation. None of these statuses reopen Group 1. F007 alone remains a future blocker for EXP-11B H150/H200 and all EXP-12 execution.

F010 is `VERIFIED_IN_G2` with resolution `RESOLVED_PRE_EXECUTION_BY_H50_STRATIFICATION`: v0.1 remains evidence for the prior `2_D1_8_D2` state and v0.2 preserves the final `5_D1_5_D2` paired design. H25/H75 SHA lists remain unchanged. The external v3 thesis fichas are recorded by path and SHA in the candidate gate as `EXTERNAL_TESIS_GOVERNANCE_DOCUMENT`; they are not required for clean-checkout execution.

The candidate gate is `PENDING_EXTERNAL_FINAL_AUDIT` and recommends `APPROVED_WITH_NONBLOCKING_LIMITATIONS`. EXP-11A and EXP-12 remain unauthorized. The external final audit must inspect the versioned commit and clean checkout; this summary does not certify G2A as closed.

## G2A Operational Final Closure

External audit approved candidate commit `c9751f67165b0bf6e06b54e4e979e7258481ded6` on `2026-08-31`. G2A is `CLOSED / APPROVED_WITH_NONBLOCKING_LIMITATIONS`; Group 1 remains closed and the historical limitation taxonomy is unchanged. EXP-11A is authorized only for H25/H50/H75/H100 under the frozen design, including the paired H50 5 D1/5 D2 schedule. EXP-11B H150/H200 and EXP-12 remain fail-closed, and no retrieval, metric computation or scientific-artifact generation occurred in this closure. New historical data are not required now; the next trigger is `AFTER_EXP11A_EXTERNAL_AUDIT` before EXP-11B or EXP-12.
