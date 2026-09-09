# 0B-05C Corrective Numerical Gate v0.2

## Purpose

This candidate freezes a prospective, unified EV03/EV04/D1a execution contract. It does not authorize or execute numerical work. Its only scientific change relative to the historical v0.1 contract is the recovered EV03 build semantics and the isolated v0.2 output namespace.

## Scientific invariants

- EV03 uses `build_bm25_ev03_historical_recovered_v02` and `DROP_SINGLE_CHARACTER_TOKENS`, with `k1=1.5`, `b=0.75`, depth 100, and the frozen Spanish stopwords.
- EV03 cannot reach its corrected arm until Decision885 reproduces with logical index identity `EXACT` and control status `PASS_EXACT`, including exact ranking, case-summary, metric table, and full metrics.
- EV04 retains the original hierarchical v0.1 semantics: `texto_index_jerarquico` with the approved fallback, unique NANDINA-8 collapse, depth 200, and its original tie behavior. It does not inherit the EV03 token policy.
- D1a freezes the original Text2Trade MNRL weights, configuration, query construction, scoring, and depth 200. Retraining is forbidden and the corrected index requires a `FULL_ATOMIC_INDEX_AND_MAPPING_REBUILD`.
- The Decision906 patch is restricted to `87044110` and `87045110`, both with the frozen text `Inferior a 4,537 t` and the exact v0.1 replacements.

## Closed state

The gate is `CANDIDATE_PENDING_EXTERNAL_AUDIT`, has scope `UNIFIED_0B05C_NUMERICAL_PREEXECUTION`, and is `NOT_AUTHORIZATION_READY`. EV03, EV04, D1a, and the unified execution are all `NOT_AUTHORIZED`. There is no authorization record or runtime authorization record, no corrected retrieval, and no corrected metric.

The read-only command is:

```bash
python -B -m src.experiments.run_0b05c_corrective_numerical_v02 --preflight
```

The future `--execute-authorized` entry point validates all four authorizations before any operation. In this candidate it fails closed. A later authorization requires a separate, auditable transition.

## Isolation and persistence

All prospective roots use the v0.2 namespace and must be absent before execution. Creation is single-shot: overwrite, resume, retry, and reuse of v0.1 evidence roots are forbidden. The v0.1 gate remains historical, integrated, and superseded for new execution; its artifacts are not modified.

Canonical tracked identities are Git blob SHA-1 plus SHA-256 of `git cat-file blob` bytes. Text files created by this gate are pinned to LF in `.gitattributes`. The ignored model weights retain their frozen file size and SHA-256 identity but are not required for the closed read-only preflight.
