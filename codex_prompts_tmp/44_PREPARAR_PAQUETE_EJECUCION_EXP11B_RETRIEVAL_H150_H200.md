# PROMPT 44 — PREPARAR Y VALIDAR PAQUETE DE EJECUCIÓN EXP11B RETRIEVAL H150/H200

## Rol y objetivo

Actúa como **ejecutor técnico controlado**.

Este bloque prepara y valida el paquete técnico que permitiría una futura ejecución oficial de `EXP11B Retrieval H150/H200`, pero **NO autoriza ni ejecuta dicha evaluación oficial**.

El objetivo es eliminar, antes de una futura autorización one-shot, fallos previsibles de implementación, entorno, bindings, paths, contratos de salida y semántica de ejecución.

Este bloque debe producir un **candidato de paquete de ejecución**, sujeto a auditoría externa posterior de IA Experimental.

Queda estrictamente prohibido observar o producir resultados científicos H150/H200 en este bloque.

---

# 1. Estado externo que gobierna este bloque

La auditoría externa de Prompt43 establece:

```text
PROMPT43_EXTERNAL_AUDIT = PASS
EXP11B_PORTABILITY_DEBT = CLOSED / APPROVED / INTEGRATED
CANONICAL_PLAN = RECONCILED
EXP11B_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```

El cierre de portabilidad **no equivale** a autorización de retrieval.

Este Prompt44 es preparación técnica prospectiva, no autorización.

---

# 2. Refs obligatorias de entrada

Repositorio:

`elVladdi/gci-nandina-rag`

Haz `git fetch --all --prune` y verifica exactamente:

```text
origin/main = 09ff184854659110f7711b3eee65fc18927649da
origin/docs/plan-maestro-temporal-2026-08-31 = 6e327d4bcde32a3804e6923015eaa505a0a53374
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
```

En `main` deben existir exactamente los cierres ya aprobados:

```text
outputs/audits/exp11b_retrieval_execution_gate_v0.1/exp11b_portability_replay_proof_v0.1.json
blob = ab3ed6aadaaebbfc3d23c725d3ad53e9518b1ead

outputs/audits/exp11b_retrieval_execution_gate_v0.1/exp11b_portability_debt_external_closure_v0.1.json
blob = bfbeedff9025ae928a85ab8b65a261ff475422cb
```

El candidato rechazado de Prompt40:

`799156b3c98858fbe081de73f381030426174ce1`

no debe ser ancestro de `main` ni reutilizarse.

El directorio oficial futuro:

`outputs/evaluation/exp11b_historical_retrieval_h150_h200_v0.1`

debe seguir **ausente**. Si existe, `STOP / OFFICIAL_OUTPUT_ROOT_ALREADY_EXISTS`.

Cualquier drift de las refs o precondiciones anteriores: `STOP / PRECONDITION_DRIFT`.

---

# 3. Diagnóstico técnico obligatorio antes de escribir

Lee y audita en `main` como mínimo:

- `src/configs/exp11b_retrieval_execution_gate_v0.1.json`;
- `outputs/audits/exp11b_retrieval_execution_gate_v0.1/exp11b_retrieval_execution_gate_manifest_v0.1.json`;
- `outputs/audits/exp11b_retrieval_execution_gate_v0.1/exp11b_retrieval_execution_input_inventory_v0.1.json`;
- `outputs/audits/exp11b_bank_materialization_v0.1/exp11b_bank_materialization_manifest_v0.1.json`;
- `outputs/audits/exp11b_bank_materialization_v0.1/exp11b_bank_hashes_v0.1.csv`;
- `src/experiments/evaluate_historical_retrieval_data_aduanas_v02.py`;
- `src/experiments/run_exp11a_historical_size_sensitivity_v03.py`;
- `src/evaluation/metrics.py`;
- `src/bm25_index.py`;
- `src/utils/paths.py`.

Confirma expresamente el siguiente hallazgo de diseño actual:

- el evaluador canónico EXP-04 contiene helpers BM25 reutilizables;
- su `evaluate()`/CLI está ligado al H100 congelado mediante hash y `EXPECTED_HISTORICAL_ROWS=2950`, por lo que **no debe invocarse directamente como CLI** sobre H150/H200;
- EXP11A demuestra la reutilización correcta de los helpers canónicos sobre bancos históricos variables.

Si este diagnóstico ya no es cierto por drift real del baseline, no improvises otra arquitectura: `STOP / EXECUTION_ARCHITECTURE_DRIFT` y reporta la evidencia.

---

# 4. Contrato científico que debe preservar el paquete

No redefinas la semántica BM25. Reutiliza directamente los helpers canónicos versionados del EXP-04, como ya hace EXP11A.

Debe preservarse exactamente:

```text
query_column = DESCRIPCION DE MERCANCIAS CONCATENADA
label_column = NANDINA
normalization = unicode_NFKD_lowercase_remove_combining_marks
tokenizer = regex_[a-z0-9]+
k1 = 1.5
b = 0.75
candidate_depth = 100
k_values = 1,3,5,10,50
ranking_order = descending_score_then_ascending_historical_case_id
candidate_deduplication = first_ranked_historical_row_per_NANDINA
reference_rank = one_based_rank_after_NANDINA_deduplication_or_zero_when_absent
reciprocal_rank = zero_when_rank_is_zero_else_1_over_rank
```

EVAL permanece congelado:

```text
path = data/processed/data_aduanas_evalset_clase87_v0.2.csv
rows = 1056
sha256 = 3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941
```

H100 de control:

```text
path = data/processed/data_aduanas_historico_clase87_v0.2.csv
rows = 2950
sha256 = 0990cdfe2a62638bff83a1182b0d6b0b727d670f63888044e99fd3ee0d7915ff
```

El denominador primario sigue siendo `1056`.

Los conjuntos common-clean permanecen **complementarios únicamente** y no cambian selección ni denominador primario.

---

# 5. Bancos H150/H200: validación permitida, retrieval prohibido

La ruta local oficial esperada de los bancos es:

`data/interim/exp11b_historical_banks_v0.1/`

En este bloque los bancos oficiales son **read-only**.

Debes comprobar localmente, antes de cualquier otra prueba:

- 20 archivos esperados;
- 10 H150 y 10 H200;
- IDs y filenames exactos;
- las 10 seeds congeladas;
- SHA-256;
- `size_bytes`;
- row counts;
- los 14 campos de identidad gobernada contra ledger/manifest.

Registra esta evidencia como:

`CODEX_LOCAL_BANK_PREFLIGHT / NOT_INDEPENDENT_GITHUB_RUNTIME_OBSERVATION`

No escribas, rematerialices ni reemplaces ninguno de esos CSV.

**Prohibición crítica:**

En Prompt44 NO ejecutes consultas EVAL contra ningún banco H150/H200, ni siquiera como shadow test.

No calcules ni observes para H150/H200:

- Top-1/3/5/10/50;
- MRR;
- ranks por caso;
- candidatos por caso;
- ninguna métrica o ranking derivado de EVAL.

El propósito es validar la capacidad técnica de ejecución sin anticipar los resultados científicos que todavía no están autorizados.

---

# 6. Construir paquete de ejecución candidato

Solo si las verificaciones anteriores pasan, crea desde `origin/main` exactamente:

`codex/exp11b-retrieval-execution-package-v01`

Parent obligatorio:

`09ff184854659110f7711b3eee65fc18927649da`

El paquete puede añadir únicamente estos tres paths nuevos:

```text
src/experiments/run_exp11b_historical_retrieval_h150_h200_v01.py
src/configs/exp11b_historical_retrieval_h150_h200_execution_v0.1.json
outputs/audits/exp11b_retrieval_execution_gate_v0.1/exp11b_retrieval_preexecution_readiness_v0.1.json
```

No modifiques archivos históricos existentes.

## 6.1 Runner prospectivo

El runner debe:

1. importar/reutilizar directamente los helpers BM25 canónicos de `evaluate_historical_retrieval_data_aduanas_v02.py`;
2. no copiar ni reimplementar silenciosamente la fórmula BM25;
3. cargar la lista de 20 bancos y sus identidades desde el contrato congelado versionado;
4. validar antes de cada futura ejecución que el banco observado coincide con su identidad congelada;
5. usar siempre el EVAL congelado de 1056 casos;
6. preservar `candidate_depth=100` y `k_values=[1,3,5,10,50]`;
7. producir, cuando esté autorizado en un bloque futuro, exactamente el contrato de salida ya congelado en `exp11b_retrieval_execution_gate_v0.1.json`;
8. impedir overwrite del output root oficial;
9. impedir resume/retry silencioso;
10. preservar failure evidence si una ejecución futura falla;
11. registrar entorno, commit, configuración, bank hash y eval hash;
12. permitir exactamente una corrida oficial por banco;
13. tratar el conjunto completo de 20 bancos como una única ejecución oficial gobernada;
14. fallar cerrado ante cualquier drift de bank/config/eval/source bindings;
15. no tocar EXP12, Grupo 2B, Plan ni Article.

## 6.2 Modos obligatorios

Diseña la CLI con separación inequívoca entre:

```text
--preflight
--self-test-h100
--execute-official
```

### `--preflight`

Solo valida contratos, archivos, hashes, entorno, paths, bancos y ausencia de output oficial. No ejecuta retrieval H150/H200 y no genera métricas.

### `--self-test-h100`

Ejecuta exclusivamente un control positivo sobre **H100 ya conocido**, en un directorio temporal fuera del output oficial.

Debe verificar contra los resultados H100 congelados:

```text
Top1 numerator = 538
Top3 numerator = 709
Top5 numerator = 806
Top10 numerator = 941
Top50 numerator = 1047
MRR = 0.6297077493524843
MRR abs tolerance = 1e-12
```

Este self-test puede validar también el schema/serialización futura usando outputs temporales, pero debe eliminarlos al finalizar.

Nunca use H150/H200 en `--self-test-h100`.

### `--execute-official`

Debe permanecer **inutilizable en este bloque**.

El runner debe exigir un artefacto de autorización prospectiva separado, todavía inexistente, y fallar cerrado si dicho artefacto no existe o no coincide exactamente con sus bindings.

No crees ese artefacto de autorización en Prompt44.

El test obligatorio de Prompt44 es demostrar que `--execute-official` se rechaza correctamente por ausencia de autorización, **antes de iniciar cualquier retrieval**.

---

# 7. Configuración prospectiva candidata

Crea:

`src/configs/exp11b_historical_retrieval_h150_h200_execution_v0.1.json`

Debe contener como mínimo:

```text
experiment_id = EXP-11B
scope = H150_H200_HISTORICAL_RETRIEVAL_ONLY
contract_status = CANDIDATE_EXECUTION_PACKAGE_PENDING_EXTERNAL_AUDIT
execution_authorized = false
execution_executed = false
expected_banks = 20
official_runs_per_bank = 1
primary_eval_n = 1056
candidate_depth = 100
k_values = [1,3,5,10,50]
automatic_retries = false
silent_resume = false
silent_overwrite = false
rerun_for_unexpected_results = false
configuration_mutable_after_authorization = false
```

Debe bindear explícitamente por path + hash/blob, según corresponda:

- EVAL;
- H100 de control;
- retrieval gate config/manifest/inventory;
- bank materialization manifest/ledger;
- Prompt41 replay proof;
- portability closure record;
- evaluator canónico EXP-04;
- EXP11A reuse proof;
- metrics helper;
- path helper;
- los 20 bank IDs y hashes congelados;
- output contract oficial ya congelado.

Define la ruta futura de autorización, pero no la crees:

`outputs/audits/exp11b_retrieval_execution_gate_v0.1/exp11b_retrieval_execution_authorization_v0.1.json`

El runner futuro debe requerir que dicha autorización bindee, al menos:

- commit del paquete aprobado/integrado;
- blob/hash del runner;
- blob/hash de esta config;
- EVAL SHA;
- ledger/manifest SHA;
- closure record blob;
- expected banks = 20;
- output root oficial;
- `authorization_status = AUTHORIZED_ONE_SHOT`.

---

# 8. Validaciones preventivas obligatorias en Prompt44

Ejecuta todas las verificaciones siguientes sin tocar el output oficial:

## 8.1 Estática

- `python -m py_compile` o equivalente sobre el nuevo runner;
- imports correctos;
- CLI help correcto;
- config JSON válida;
- todos los bindings resolubles;
- working tree controlado.

## 8.2 Preflight completo

Ejecuta exactamente una vez `--preflight` y exige:

```text
bank_count = 20
bank_identity_mismatch_count = 0
eval_sha_match = true
canonical_source_binding_mismatch_count = 0
official_output_root_exists = false
retrieval_executed = false
metrics_computed = false
```

## 8.3 Control H100

Ejecuta exactamente una vez `--self-test-h100`.

Debe reproducir los numeradores y MRR congelados anteriores y terminar PASS.

Si no reproduce H100 exactamente/tolerancia fijada: `STOP / H100_SEMANTIC_SELF_TEST_FAILED`.

No ajustes parámetros para hacerlo pasar.

## 8.4 Guard de autorización

Invoca el modo `--execute-official` **sin artefacto de autorización** y verifica que termina antes de cualquier scoring, antes de crear el output root oficial y con una clasificación explícita equivalente a:

`OFFICIAL_EXECUTION_BLOCKED_NO_AUTHORIZATION`.

Esta invocación es una prueba negativa del guard; **no cuenta como ejecución oficial ni puede consumir autorización porque no existe**.

## 8.5 No contaminación

Al final verifica:

```text
official_output_root_exists = false
h150_h200_retrieval_invocation_count = 0
h150_h200_metrics_observed = false
h150_h200_case_rankings_observed = false
official_bank_write_count = 0
official_bank_content_mutated = false
temporary_self_test_cleanup = PASS
EXP12_authorized = false
```

---

# 9. Readiness artifact

Crea el único artefacto de auditoría nuevo permitido:

`outputs/audits/exp11b_retrieval_execution_gate_v0.1/exp11b_retrieval_preexecution_readiness_v0.1.json`

Debe registrar como mínimo:

- baseline commit;
- candidate branch/commit parent esperado;
- runner path y blob/hash;
- config path y blob/hash;
- todos los source/input bindings;
- 20 bank identities y resultado local de validación;
- entorno Python/plataforma/dependencias relevantes;
- resultado de compilación/import/CLI;
- resultado `--preflight`;
- resultado del H100 self-test con numeradores/deltas;
- resultado del guard sin autorización;
- ausencia de output oficial;
- no mutación de bancos;
- no observación de H150/H200;
- cleanup temporal;
- clasificación epistemológica de checks locales.

Estado máximo permitido:

```text
status = CANDIDATE_PREEXECUTION_READY_PENDING_EXTERNAL_AUDIT
execution_package_ready = true
execution_authorized = false
retrieval_executed = false
h150_h200_results_observed = false
future_authorization_required = true
EXP12_authorized = false
```

Si cualquiera de los checks bloqueantes falla, no declares readiness. Registra el fallo de forma auditable y termina `STOP` sin intentar corregirlo mediante cambios de parámetros o ejecución H150/H200.

---

# 10. Restricciones Git del candidato

El candidato científico debe:

- partir directamente de `09ff184854659110f7711b3eee65fc18927649da`;
- tener solo los tres paths nuevos autorizados;
- no modificar ningún archivo existente;
- no contener resultados temporales;
- no contener autorización;
- no contener outputs H150/H200;
- no modificar Plan Maestro;
- no modificar Article;
- no modificar EXP12;
- no incorporar Prompt40 rechazado.

Publica únicamente:

`codex/exp11b-retrieval-execution-package-v01`

No la integres a `main` en este bloque.

---

# 11. Prohibiciones absolutas

NO:

- autorizar retrieval;
- ejecutar retrieval H150/H200;
- calcular/observar métricas H150/H200;
- calcular/observar rankings EVAL por caso para H150/H200;
- crear el output root oficial;
- crear el artefacto futuro de autorización;
- rematerializar bancos;
- modificar los bancos oficiales;
- modificar H100/DEV/EVAL;
- modificar semántica BM25;
- modificar el retrieval gate histórico;
- modificar closure/replay proof;
- modificar Plan Maestro;
- modificar Article;
- modificar EXP12;
- abrir Grupo 2B o Grupo 3;
- reintentar un check fallido alterando parámetros para obtener PASS.

---

# 12. Persistencia administrativa

Después del trabajo científico:

1. vuelve a `codex/prompts-temporary`;
2. haz `git fetch`;
3. no rebase/amend/force;
4. crea únicamente:

`codex_prompts_tmp/44_RESPUESTA_PREPARAR_PAQUETE_EJECUCION_EXP11B_RETRIEVAL_H150_H200.md`

5. persiste la respuesta en un commit administrativo separado;
6. no mezcles ningún archivo científico en ese commit administrativo.

---

# 13. Reporte obligatorio

La respuesta debe incluir, como mínimo:

1. estado final `COMPLETED` o `STOP`;
2. refs iniciales y finales;
3. diagnóstico del evaluador H100-bound y estrategia de reutilización de helpers;
4. identidad de los 20 bancos y resultado del preflight local;
5. runner/config/readiness paths y hashes/blobs;
6. resultados de compile/import/CLI;
7. resultado único de `--preflight`;
8. resultado único de `--self-test-h100`;
9. resultado del guard `--execute-official` sin autorización;
10. confirmación de cero retrieval/metrics/rankings H150/H200;
11. confirmación de output root oficial ausente;
12. branch/commit/parent/tree/ahead-behind/changed paths del candidato;
13. confirmación de no cambios en Plan/Article/EXP12;
14. ruta y commit administrativo de esta respuesta.

Estado máximo terminal permitido:

```text
PROMPT44 = COMPLETED
EXP11B_RETRIEVAL_EXECUTION_PACKAGE = CANDIDATE / PENDING_EXTERNAL_AUDIT
EXP11B_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
H150_H200_RESULTS = NOT_OBSERVED
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```
