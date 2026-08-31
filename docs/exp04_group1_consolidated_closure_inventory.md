# EXP-04 and Group 1 Consolidated Closure Inventory

## Closure Decision

EXP-04, the full rerun with corrected split v0.2, and Group 1 experimental design are closed for review. All ten cards from EXP-01 through EXP-10 are registered as `CLOSED` with an `APPROVED` gate in the frozen closure matrix. This is a documentation and provenance close; it does not merge the branch into `main`.

## Evidence Hierarchy

Historical retrieval is the main candidate-ranking evidence. Its frozen v0.2 evaluation covers 1,056 cases, with Top-1 538/1,056 and Top-3 709/1,056. Normative flat and hierarchical BM25 runs remain documentary evidence, not a substitute for historical candidate ranking. D1a dense retrieval remains an early retrieval comparison.

The diagnostic reranker is an exploratory 20-case audit, not a benchmark result. HE4 uses the fixed top-3 context on a 50-case sample and supports local explanation auditing only. The pilot remains a Clase 87, internal, offline evaluation; conclusions cannot be generalized outside that scope.

## Frozen Integrity Contracts

The v0.2 split preserves zero DAM overlap, a fixed evaluation set, no evaluation drift, and no evaluation tuning. Exact and near-duplicate audits, DAM concentration evidence, EXP-05 unified-evaluation hashing, EXP-07 dev/eval freeze, and the EXP-08 corrective sensitivity close are all preserved in the consolidated provenance registry.

## Hypotheses and Limits

HE2 is `PARTIALLY_SUPPORTED`, HE3 is `SUPPORTED`, HE4 is `PARTIALLY_SUPPORTED`, and HE5 is `PARTIALLY_SUPPORTED`. No new formal result for OE1 or HE1 is asserted. The thirteen known limitations are deliberately carried forward as unresolved, including concentration, duplicate controls, early weak retrieval baselines, sample sizes, HE4 schema mismatch, evaluator modality, metadata provenance, split sensitivity, and the internal Clase 87 scope.

## Resulting Boundary

The closure prepares the branch for human review before any merge to `main`. It does not begin Group 2 or authorize a new experiment, retrieval run, model invocation, or web access.

## Corrective Microclose

The consolidated registry was corrected against the tracked, frozen D1a MNRL metrics artifact rather than the invalidated D0 legacy dense baseline. The corrective manifest records the split hashes, Git-tracking checks for every frozen provenance row, the corrected EXP-06 title, and the complete schemas for result, provenance, limitation, and hypothesis registries. The microclose makes no experimental claim beyond the existing frozen artifacts.
