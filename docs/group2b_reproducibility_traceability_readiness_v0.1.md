# Group 2B reproducibility and traceability readiness v0.1

## Scope and status

This is a read-only provenance audit over the scientific tree at
`5787503329afd5ddd5e94d04cdbbdeb000260cda`. It did not execute experiments,
tests, retrieval, BM25, Top-k, MRR, planning, candidate generation, or model
inference. It did not regenerate datasets, manifests, results, logs, or
case-level artifacts.

Status: `CANDIDATE_PENDING_EXTERNAL_AUDIT`. This document does not close Group
2B and does not reopen EXP12.

## Canonical commits read

| Surface | Commit |
|---|---|
| Scientific main | `5787503329afd5ddd5e94d04cdbbdeb000260cda` |
| Canonical Plan | `0c77e86359bcd17ddd446429f21b62174c426f37` |
| Article | `254b1e6df736fa9938ac86a515d65b36f4d361c5` |

The Plan records Group 1 as closed, Group 2A as closed with nonblocking
limitations, EXP11A and EXP11B as closed, 0B-05C Attempt06 as closed after
corrective reconciliation, and the original frozen EXP12 design as
`CLOSED_WITHOUT_RETRIEVAL / PLANNING_PRECONDITION_FAILED_UNDER_FROZEN_SEARCH`.

## Inventory by scientific block

| Block | Evidence found | Classification |
|---|---|---|
| Benchmark v0.2 | H100, DEV, EVAL, metadata, split config, audits and manifest | `VERSIONED_AND_IDENTITY_VERIFIED` |
| Group 1 | Consolidated closure, result/provenance registries and clean-checkout evidence | `VERSIONED_AND_IDENTITY_VERIFIED` with accepted historical limits |
| Group 2A | Gate manifest, findings, environment inventory and traceability matrices | `DECLARED_LIMITATION` for incomplete historical environment |
| EXP11A | 31-run manifest, frozen compositions, aggregate metrics, case-level and freeze hashes | `VERSIONED_AND_IDENTITY_VERIFIED` |
| New historical gates | NUEVA_01/v0.1 and NUEVA_02/v0.2 pools, source freezes and audits | `VERSIONED_AND_IDENTITY_VERIFIED`; acquisition attestation retained |
| EXP11B bank materialization | Config, 20-bank manifest and 14-field hash ledger | Versioned controls; bank CSVs `HASH_BOUND_LOCAL_ONLY` |
| EXP11B portability | Deterministic replay proof and external debt closure | `VERSIONED_AND_IDENTITY_VERIFIED` with runtime caveat |
| EXP11B retrieval | Authorization, one-shot record, manifest, metrics, case-level, environment and hashes | Versioned except full candidates `HASH_BOUND_LOCAL_ONLY` |
| 0B-05C | v0.5 gate, Attempt06 record, 19/19 execution steps, exact hash ledger, aggregate and case-level evidence | `VERSIONED_AND_IDENTITY_VERIFIED`; model weights hash-bound local-only |
| EXP12 planning | Source binding, corrected frozen contract, consumed authorization and failed one-shot report | `VERSIONED_AND_IDENTITY_VERIFIED` with declared fail-closed outcome |
| EXP12 forensic/final | Design, consumed authorization, execution report, aggregate diagnostic and Plan disposition | `VERSIONED_AND_IDENTITY_VERIFIED`; retrieval and retrieval case-level `NOT_APPLICABLE` |

The machine-readable inventory contains 47 entries and uses only the required
classification vocabulary.

## End-to-end matrix

| Block | Source to closure chain | Status |
|---|---|---|
| Benchmark v0.2 | Source provenance -> split config/script -> H100/DEV/EVAL -> audits/manifest -> integration | `COMPLETE` |
| Group 1 | Frozen benchmark -> phase contracts/runners -> results/case-level -> consolidated closure | `COMPLETE_WITH_DECLARED_LIMITATION` |
| Group 2A | Group1 evidence -> reproducibility contracts -> read-only audit -> approved gate | `COMPLETE_WITH_DECLARED_LIMITATION` |
| EXP11A | H100/compositions -> nested design -> gated 31 runs -> metrics/case-level -> freeze | `COMPLETE_WITH_DECLARED_LIMITATION` |
| New historical gates | Source freezes -> ingestion logic -> eligible pools -> overlap/duplicate audits -> integration | `COMPLETE_WITH_DECLARED_LIMITATION` |
| EXP11B materialization | H100/eligible pool -> config/materializer -> 20 banks -> identity ledger -> gate | `COMPLETE_WITH_DECLARED_LIMITATION` |
| EXP11B portability | Versioned inputs -> clean detached replay -> 20/20 triple identity -> debt closure | `COMPLETE_WITH_DECLARED_LIMITATION` |
| EXP11B retrieval | Banks/EVAL -> execution package -> AUTH_001 -> one-shot -> metrics/case-level -> closure | `COMPLETE_WITH_DECLARED_LIMITATION` |
| 0B-05C Attempt06 | Frozen inputs -> v0.5 gate -> authorization -> one-shot 19/19 -> results/case-level -> closure | `COMPLETE_WITH_DECLARED_LIMITATION` |
| EXP12 planning | Bound source/frozen seeds -> AUTH_001 -> failed one-shot -> audited fail-closed disposition | `COMPLETE_WITH_DECLARED_LIMITATION` |
| EXP12 forensic/final | Frozen source -> non-governing protocol -> AUTH_002 -> one-shot aggregate -> final closure without retrieval | `COMPLETE_WITH_DECLARED_LIMITATION` |

No chain is silently completed. The limitations are carried in the JSON and
remain visible to external audit.

## Identity and hash verification

Thirty-five relevant declared path/SHA bindings were checked without changing
files. Thirty-one passed, including two `PASS_EOL_EQUIVALENT` checks where the
historical SHA used Windows CRLF while Git stores canonical LF content. The
four non-pass classifications are not mismatches: two sample materialized
banks, the complete EXP11B candidate ranking, and the frozen D1a model weights
are intentionally local-only and remain bound by their recorded SHA-256 and
size.

The benchmark H100, DEV and EVAL SHA-256 values pass exactly. EXP11A aggregate
and case-level hashes pass. Both eligible historical pools and their duplicate
audits pass. All versioned EXP11B outputs selected for verification pass. The
0B-05C runtime ledger reports zero mismatches and the selected corpus/D1a
bindings pass. The EXP12 forensic marker, logs and aggregate pass, applying the
documented CRLF/LF equivalence to the aggregate JSON.

## Manifest, config, seed, script, log and case-level status

- Manifests and configs are tracked for every row in the end-to-end matrix.
- EXP11A preserves the H25/H50/H75/H100 compositions and seeds
  `20261001..20261010` in its run evidence.
- EXP11B preserves ten accepted seeds, both H150/H200 conditions, the 20-bank
  identity ledger, one-shot execution record and environment record.
- EXP12 preserves seeds `20262001..20262010` without post-hoc substitution,
  `candidate_count=10000`, coverage `1.0`, maximum TVD `0.05`, and the consumed
  planning/forensic authorizations.
- Versioned logs exist for the relevant one-shot EXP12 attempts.
- Case-level is versioned for EXP11A, EXP11B and 0B-05C. EXP12 retrieval output
  and retrieval case-level are `NOT_APPLICABLE / NOT_EXECUTED_BY_FINAL_DISPOSITION`.

## Environment and clean checkout

`ENVIRONMENT_REPRODUCIBILITY = COMPLETE_WITH_DECLARED_LIMITATION`. Historical
runtime records exist for G2A, EXP11B and 0B-05C. They do not create a complete
dependency lock for every historical Group1 phase, and current observations
are not treated as historical facts. The local-only D1a model remains bound by
SHA-256 and size.

`CLEAN_CHECKOUT_REPRODUCIBILITY = COMPLETE_WITH_DECLARED_LIMITATION`. Group1
records a clean-checkout 229/229 suite, EXP11B records a clean detached replay,
and this readiness worktree was tracked-clean before artifact creation.
Prompt70 intentionally did not execute a current scientific pipeline or test
suite, and a pure Git checkout intentionally omits local-only assets.

## Gaps and limitations

`BLOCKING_GAP_COUNT = 0` for this readiness candidate. This is a proposed
classification pending external audit, not a Group2B closure decision.

Eleven nonblocking limitations are retained: incomplete historical environment;
the unrecoverable historical EXP04-C runner and EXP08 v0.1 metadata; non-byte-
exact LLM evaluation; EXP11A size/composition coupling; user-attested NUEVA_02
acquisition; local-only EXP11B banks and candidate ranking; portability runtime
not independently rerun by the external auditor; local-only D1a weights; the
failed one-shot EXP12 planning outcome; and the non-governing nature of the
EXP12 forensic diagnostic.

Five items are historical-only: legacy CRLF contracts mapped to canonical LF,
G2A F002/F005, prior fail-closed 0B-05C attempts, the superseded EXP11B
portability notice, and rejected/superseded EXP12 candidates.

## Proposed next step

`GROUP2B_EXTERNAL_AUDIT_AND_CLOSURE_DECISION`.

External audit should validate this inventory, severity classification and the
proposed absence of blocking gaps. Only a separate approved block may close
Group 2B. Group 3 remains not started.
