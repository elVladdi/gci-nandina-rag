### A. Preflight Git

- `main = origin/main = 43291c312c2934aae03f3c087dd0a1ae594341b7`
- `main tree = 9f21cb79c37cbcdf93006503bb4f888f1acfc975`
- `Plan Maestro = fe847f708d4d1ded92b5a50a38d4913bb69ed311`
- `article = 254b1e6df736fa9938ac86a515d65b36f4d361c5`
- Rama candidata: `codex/0b05c-corrective-numerical-gate-v02`
- Base/parent: `43291c312c2934aae03f3c087dd0a1ae594341b7`
- Estado final del candidato: clean; `origin` sincronizado.

### B. Scope creado

- Modificado: `.gitattributes`, exclusivamente con reglas LF para los nuevos paths v0.2.
- Añadidos: `docs/0B05C_CORRECTIVE_NUMERICAL_GATE_V02.md`; los cuatro módulos `prepare/build/run/run_d1a` v0.2; `tests/test_0b05c_corrective_numerical_gate_v02.py`; y los seis JSON contractuales exigidos bajo `outputs/audits/0b05c_corrective_numerical_gate_v0.2/`.
- Total: 13 paths, todos necesarios para congelar preparación, ejecución prospectiva, contratos, trazabilidad, pruebas y portabilidad EOL. Ningún path v0.1 fue modificado.

### C. EV03 v0.2

- Builder: `build_bm25_ev03_historical_recovered_v02.build_ev03_recovered_historical_from_corpus`.
- La ruta EV03 no llama directamente al builder global divergente; congela `DROP_SINGLE_CHARACTER_TOKENS`, stopwords españolas, `k1=1.5`, `b=0.75`, profundidad 100 y orden NANDINA-8.
- Control obligatorio: `LOGICAL_INDEX_IDENTITY=EXACT` y `PASS_EXACT` para ranking completo/bytes, case summary/bytes, tabla y métricas completas; 50,327 filas, 1,056 casos y los dos SHA-256 congelados.
- Roots: los cinco roots EV03 Decision885/Decision906 v0.2 especificados, todos ausentes.

### D. EV04 v0.2

- Semántica jerárquica v0.1 preservada: `texto_index_jerarquico` con fallback `texto_index`, collapse por primera ocurrencia NANDINA-8 única, profundidad 200, parámetros y tie behavior congelados.
- No hereda `DROP_SINGLE_CHARACTER_TOKENS`; la reproducción Decision885 es obligatoria y debe ser `PASS_EXACT` antes del brazo corregido.
- Roots: los cinco roots EV04 Decision885/Decision906 v0.2 especificados, todos ausentes.

### E. D1a v0.2

- Pesos congelados: `470637416` bytes, SHA-256 `ef9b92b2fb0239e46c0d81e403f00b3255d3822dfa25e0ce354d03828f7a8c87`; configuración y EVAL ligados canónicamente.
- `MODEL_POLICY=FREEZE_ORIGINAL_D1A_WEIGHTS`; `must_not_retrain=true`; profundidad 200; scoring, embeddings y ranking preservados.
- Reconstrucción: `FULL_ATOMIC_INDEX_AND_MAPPING_REBUILD`.
- Roots: corpus, índice, evaluación y runtime audit D1a v0.2, todos ausentes.

### F. Patch Decision906

- Códigos exactos: `87044110`, `87045110`.
- Texto congelado: `Inferior a 4,537 t`.
- Replacements `titulo`, `texto_index`, `texto`, `version` y contexto preservados exactamente desde los contratos v0.1; no se amplió el patch.

### G. Runner unificado

- Orden exacto: `01_unified_preflight`; `02_EV03_Decision885_control_reproduction`; `03_EV03_control_reproduction_verification`; `04_EV03_corrected_corpus_materialization`; `05_EV03_corrected_index_build_RECOVERED_HISTORICAL_SEMANTICS`; `06_EV03_corrected_evaluation`; `07_EV04_Decision885_control_reproduction`; `08_EV04_control_reproduction_verification`; `09_EV04_corrected_corpus_materialization`; `10_EV04_corrected_index_build`; `11_EV04_corrected_evaluation`; `12_D1a_corrected_execution_under_v02_authorization`; `13_integrity_validation`; `14_case_level_comparisons`; `15_aggregate_comparisons`; `16_unified_sensitivity_summary`; `17_execution_manifest`; `18_exact_hash_ledger`; `19_final_completion_state`.
- Fail-closed antes del primer side effect; controles EV03/EV04 `PASS_EXACT`; short-circuit inmediato; sin retry, resume ni overwrite; el paso 19 requiere los 18 previos.

### H. Gate/autorización

- `gate_version=v0.2`; `gate_status=CANDIDATE_PENDING_EXTERNAL_AUDIT`; `gate_scope=UNIFIED_0B05C_NUMERICAL_PREEXECUTION`; `authorization_readiness=NOT_AUTHORIZATION_READY`.
- EV03, EV04, D1a y unified: `NOT_AUTHORIZED`; authorization record ausente; runtime record ausente.
- `corrective_retrieval_executed=false`; `corrective_metrics_computed=false`; ninguna ejecución numérica ocurrió.

### I. Canonical bindings

- 36 bindings congelados.
- Categorías: `VERSIONED_GIT_BLOB`, `FROZEN_BINARY_GIT_BLOB`, `FROZEN_FILE_IDENTITY`, `FUTURE_GENERATED_OUTPUT_NOT_PRESENT`.
- Texto/binarios tracked: Git blob SHA-1 más SHA-256 de bytes `git cat-file blob`; modelo local: tamaño/SHA-256 exactos; outputs futuros: ausentes, sin hashes inventados; `mismatch_count=0`.
- Portabilidad: reglas LF limitadas a los nuevos archivos textuales v0.2.

### J. Tests

- Gate v0.2: RUN=20, PASS=20, FAIL=0, ERROR=0, SKIP=0.
- EV03 recovery v0.2 post-commit: RUN=16, PASS=16, FAIL=0, ERROR=0, SKIP=0.
- Gate v0.1: RUN=33, PASS=33, FAIL=0, ERROR=0, SKIP=0.
- D1a preexecution/runner: RUN=34, PASS=34, FAIL=0, ERROR=0, SKIP=0.
- BM25 flat/hierarchical: RUN=30, PASS=30, FAIL=0, ERROR=0, SKIP=0.
- Suite total: RUN=513, PASS=513, FAIL=0, ERROR=0, SKIP=1; el skip pre-commit del replay limpio fue ejecutado post-commit y pasó.
- Preflight candidato: `status=PASS`, `mode=PREEXECUTION_CLOSED_READONLY`, `authorization_readiness=NOT_AUTHORIZATION_READY`; funciona sin modelo ignorado.
- No se ejecutó retrieval correctivo real ni se cargó el modelo. La dependencia local temporal usada por la regresión v0.1 fue retirada.

### K. Aislamiento

- `main`, Plan Maestro y `article/` permanecen en sus HEAD verificados; EXP11B, EXP12 y todo v0.1 sin cambios.
- Los 16 roots científicos v0.2 permanecen ausentes; no se observaron métricas nuevas.
- Evidencia de Intentos 01/02 preservada y fuera del diff candidato.

### L. Commit candidato

- SHA: `b0a1e61f70f42aa2048338965cc003e032d3a493`
- Parent: `43291c312c2934aae03f3c087dd0a1ae594341b7`
- Tree: `cd8247a143e8fbb033c96d358e15a408c86809d1`
- Files changed: los 13 paths declarados en B; contenido adicional: ninguno.
- Push: `origin/codex/0b05c-corrective-numerical-gate-v02 = b0a1e61f70f42aa2048338965cc003e032d3a493`.
- Ahead/behind frente a `origin/main`: `1/0`.

### M. Persistencia administrativa

- Response path: `codex_prompts_tmp/09_RESPUESTA_CONSTRUIR_GATE_RUNNER_NUMERICO_0B05C_V02.md`.
- Parent administrativo: `a60a75f33bec660c7ae5706d49f254090f3df0cb`.
- Commit administrativo: `refs/heads/codex/prompts-temporary`, commit que contiene este archivo.
- Único archivo administrativo: el response path anterior.
- `RESPONSE_PERSISTENCE=PASS`.

### N. Estado científico

`GROUP_2 = EN_CURSO`

`0B05C_NUMERICAL_GATE_V02 = CANDIDATE_PENDING_EXTERNAL_AUDIT`

`0B05C_V02_AUTHORIZATION_READINESS = NOT_AUTHORIZATION_READY`

`EV03_V02_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED`

`EV04_V02_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED`

`D1A_V02_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED`

`UNIFIED_0B05C_V02_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED`

`0B05C_METRIC_IMPACT = NOT_DETERMINED`

`DOWNSTREAM_REEXECUTION = NOT_YET_JUSTIFIED`

`0B05C_CLOSURE = NOT_AUTHORIZED`
