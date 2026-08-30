# EXP-04 Gate C microaudit v0.2

## Status

GATE C APROBADO.

No se repitio retrieval, no se modificaron corpus/BM25/params/split/evalset y no se inicio Fase D.

## MRR comparability

- MRR@100: 44.33224687474574/1056 = 0.04198129438896377.
- MRR@200: 45.76874185264425/1056 = 0.04334161160288281.
- El MRR reportado previamente `0.04334161160288281` incluye ranks 101-200.
- Contribucion ranks 101-200: 1.436494977898505/1056 = 0.0013603172139190387.
- Comparacion justa: BM25 plano MRR@100 vs BM25 jerarquico MRR@100.

## Hierarchical metrics from rankings

| Cutoff | Exact | HS6 | HS4 | Chapter |
| --- | ---: | ---: | ---: | ---: |
| @100 | 107/1056 | 118/1056 | 264/1056 | 538/1056 |
| @200 | 321/1056 | 363/1056 | 529/1056 | 810/1056 |

Chapter@100 queda confirmado como 538/1056, calculado exclusivamente desde rankings jerarquicos.

## Position distribution

| Bucket | Cases |
| --- | ---: |
| 1 | 28 |
| 2-3 | 27 |
| 4-5 | 11 |
| 6-10 | 3 |
| 11-50 | 27 |
| 51-100 | 11 |
| 101-200 | 214 |
| >200_or_not_retrieved | 735 |
| Total | 1056 |

## Coverage

- Eval unique codes: 42.
- Eval codes present exact NANDINA-8 in corpus: 42.
- Eval cases present: 1056.
- Parent codes were not counted as exact coverage.

## Limitation stratification

| Group | n | Exact@100 | HS6@100 | HS4@100 | MRR@100 |
| --- | ---: | ---: | ---: | ---: | ---: |
| parent_hs4_present | 1056 | 0.10132575757575757 | 0.11174242424242424 | 0.25 | 0.04198129438896378 |
| parent_hs4_missing | 0 |  |  |  |  |
| parent_hs6_present | 675 | 0.06962962962962962 | 0.08592592592592592 | 0.22814814814814816 | 0.009110401658893536 |
| parent_hs6_missing | 381 | 0.15748031496062992 | 0.15748031496062992 | 0.2887139107611549 | 0.10021712796585987 |
| both_parents_missing | 0 |  |  |  |  |
| not_both_parents_missing | 1056 | 0.10132575757575757 | 0.11174242424242424 | 0.25 | 0.04198129438896378 |

Conflict flag: no se calcula estrato porque la auditoria fuente reporta conflictos a nivel de grupos duplicados, pero Fase C no contiene una bandera deterministica por caso.

## Large output file

- File: `normative_hierarchical_results.csv`.
- Size: 85426164 bytes (81.47 MiB).
- Schema: case_id, id_unico, nandina_ref, candidate_rank, candidate_raw_rank, candidate_doc_id, candidate_code, candidate_partida, candidate_sub_partida, candidate_clase, score, candidate_text, is_reference_code, method.
- Reason: stores up to 200 effective candidates for each of 1056 cases, with scores and truncated candidate text snippets.
- Redundancy: partially redundant for aggregate metrics; not deleted or modified in this task.

## Commit traceability

- `63b748a` was an unpublished local runner commit from the first Fase C attempt.
- GitHub rejected the first output history because the CSV exceeded the 100 MB hard limit.
- After approved local history cleanup, the runner commit was recreated as `ce23905`; only CSV serialization was reduced, while retrieval, corpus, split, evalset, BM25 parameters and metrics logic stayed unchanged.
- `63b748a` is not in current branch history and was not reverted by a later commit.

## git log --oneline --decorate -15

```
13d3176 (HEAD -> codex/exp04-rerun-v02, origin/codex/exp04-rerun-v02) test: add EXP-04 hierarchical normative BM25 gate checks
0015809 results: add EXP-04 hierarchical normative BM25 v0.2 outputs
ce23905 feat: add EXP-04 hierarchical normative BM25 v0.2 runner
e3590cf test: harden EXP-04 flat normative BM25 code-level checks
ce9cd0b docs: add EXP-04 flat normative BM25 code-level microaudit
24149c2 test: add EXP-04 flat normative BM25 v0.2 integrity checks
24aac2b results: add EXP-04 flat normative BM25 v0.2 outputs
df60c77 feat: add EXP-04 flat normative BM25 v0.2 runner
e9325e7 docs: update README with v0.2 experimental status
def17c9 test: add EXP-04 historical BM25 v0.2 integrity checks
52784ce results: add EXP-04 historical BM25 v0.2 outputs
c92da6e feat: add EXP-04 historical BM25 v0.2 runner
a2f0b82 (origin/main, origin/HEAD, main) test: enforce reproducible LF dataset serialization
7a9f43d merge: integrate split v0.2 Gate 5
1e7960d (codex/exp01-exp03-exp02-group-dam-split) docs: document split v0.2 concentration limitations
```
