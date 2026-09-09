# CODEX — CONSTRUIR GATE DE RECUPERACIÓN 0B-05C v0.3 PARA EV04/MRR

## 0. ROL Y OBJETIVO

Actúa exclusivamente como **EJECUTOR DE CONSTRUCCIÓN PROSPECTIVA** del nuevo gate/runner 0B-05C v0.3 posterior al fallo fail-closed de Attempt03.

Este bloque **NO autoriza ni ejecuta Attempt04** y **NO ejecuta retrieval, EV03, EV04, D1a ni el modelo**.

Objetivo único: construir una nueva versión prospectiva v0.3, separada de v0.2, que cierre de forma mecánica la causa raíz ya auditada e integrada:

`EV04_FROZEN_METRIC_SCHEMA_PRODUCER_MISMATCH_AFTER_GATE_C_MRR_MICROAUDIT`

La corrección debe preservar exactamente la ciencia de recuperación/ranking. El problema a corregir es de **contrato/productor de métricas EV04**, no de ranking ni retrieval.

---

# 1. BASELINE GIT OBLIGATORIO

Haz fetch y verifica exactamente antes de escribir:

- `origin/main = 60aa7dd8715962f3c3e8b617e8797532529f39ed`;
- tree de `60aa7dd...` = `b846797096d4ca1e1301b4dafbd362c0d8e0d88b`;
- parent = `41d3259ff09d8a63cc3a12a7f11a146a603ee3ef`;
- Plan Maestro = `fe847f708d4d1ded92b5a50a38d4913bb69ed311`;
- article = `254b1e6df736fa9938ac86a515d65b36f4d361c5`;
- failure record integrado:
  `outputs/audits/0b05c_attempt03_failclosed_v0.2/attempt03_failure_record_v0.2.json`;
- failure record:
  - `status = FAIL_CLOSED / SCIENTIFIC_STATE_PRESERVED`;
  - `authorization_consumed=true`;
  - `automatic_reuse_authorized=false`;
  - `attempt04_authorized=false`;
  - `failure_class = EV04_FROZEN_METRIC_SCHEMA_PRODUCER_MISMATCH_AFTER_GATE_C_MRR_MICROAUDIT`;
- gate v0.2:
  - `authorization_readiness = ATTEMPT03_CONSUMED / REAUTHORIZATION_REQUIRED`;
  - cuatro autorizaciones históricas permanecen `AUTHORIZED`;
  - `corrective_retrieval_executed=false`;
  - `corrective_metrics_computed=false`.

Si cualquier identidad o estado difiere: **STOP / NO V0.3 BUILD**.

No limpies ni borres evidencia local/ignored de Attempt01/02/03.

---

# 2. PRINCIPIO DE VERSIONADO Y AISLAMIENTO

Crea desde exactamente `60aa7dd8715962f3c3e8b617e8797532529f39ed` la rama:

`codex/0b05c-corrective-numerical-gate-v03`

Construye v0.3 de forma **aditiva y separada**.

Está prohibido modificar:

- cualquier artefacto v0.1;
- cualquier gate/spec/authorization record/runner v0.2;
- el failure record Attempt03 v0.2;
- outputs parciales locales de Attempt03;
- resultados históricos EXP-04;
- el runner histórico `src/experiments/evaluate_normative_bm25_hierarchical_data_aduanas_v02.py`;
- Plan Maestro;
- article;
- EXP11B;
- EXP12.

Los artefactos históricos enriquecidos por Gate C MRR se consideran **fuente congelada que debe reproducirse**, no deben ser revertidos ni simplificados.

---

# 3. CAUSA RAÍZ QUE v0.3 DEBE CERRAR

Demuestra nuevamente, read-only, antes de implementar:

1. el productor histórico `metrics_from_cases()` genera una fila legacy `mrr` y no produce originalmente el esquema enriquecido MRR@100/MRR@200;
2. el `run_metadata.json` EXP-04 congelado actual contiene como contrato enriquecido:
   - `mrr_at_100`;
   - `mrr_at_200`;
   - `mrr_at_100_numerator` / `mrr_at_200_numerator`;
   - denominadores;
   - `mrr_definition`;
   - `mrr_101_200_contribution_numerator`;
   - `mrr_101_200_contribution`;
   - `metric_table` comenzando por `mrr_at_100`, `mrr_at_200`;
   - mantiene además el legacy top-level `mrr`, que equivale a MRR@200;
3. Attempt03 reportó ranking y case summary EV04 byte/hash exactos y `metrics_exact=false`;
4. la corrección por tanto debe **reconstruir mecánicamente el esquema enriquecido a partir de los case rows realmente reproducidos**, y luego exigir igualdad exacta con el control congelado.

No copies ciegamente las métricas esperadas dentro del output observado. Las métricas observadas deben derivarse de los case rows reproducidos.

---

# 4. CONTRATO MRR EV04 v0.3 OBLIGATORIO

Implementa una función v0.3 dedicada y testeable para construir el payload de métricas EV04 enriquecido a partir de los case rows observados y de las demás métricas reproducidas.

La lógica debe ser determinística:

- `N = len(case_rows)` y debe ser 1056 en ejecución real;
- `MRR@100 numerator = sum(1/rank_ref)` solo para `1 <= rank_ref <= 100`;
- `MRR@200 numerator = sum(1/rank_ref)` solo para `1 <= rank_ref <= 200`;
- `mrr_at_100 = numerator_100 / N`;
- `mrr_at_200 = numerator_200 / N`;
- legacy top-level `mrr = mrr_at_200`;
- legacy `mrr_numerator = mrr_at_200_numerator`;
- legacy `mrr_denominator = N`;
- `mrr_101_200_contribution_numerator = numerator_200 - numerator_100`;
- `mrr_101_200_contribution = contribution_numerator / N`;
- `mrr_definition` debe coincidir exactamente con el contrato histórico congelado;
- `metric_table` debe tener exactamente los nombres, orden y schema del control congelado, comenzando por `mrr_at_100`, `mrr_at_200`;
- el resto de métricas Top-k/Recall/Exact/HS6/HS4/Chapter debe seguir derivándose de los case rows y conservar sus definiciones congeladas.

La misma semántica enriquecida debe aplicarse al brazo EV04 correctivo futuro, de modo que original y Decision906 sean comparables bajo un contrato homogéneo.

La validación del control EV04 debe seguir siendo estricta: **ranking exacto + case summary exacto + métricas enriquecidas exactas**.

No debilites `PASS_EXACT` y no excluyas campos MRR del comparison.

---

# 5. INVARIANTES CIENTÍFICOS QUE NO PUEDEN CAMBIAR

v0.3 debe preservar:

## EV03
- semántica histórica recuperada `DROP_SINGLE_CHARACTER_TOKENS`;
- BM25 k1=1.5, b=0.75;
- depth 100;
- control D885 exacto;
- misma EVAL N=1056;
- misma corrección D906 de exactamente dos códigos.

## EV04
- mismo corpus jerárquico congelado;
- mismo BM25 k1=1.5, b=0.75;
- depth efectivo 200;
- ranking por NANDINA-8 único;
- duplicate collapse: primera ocurrencia BM25 por score;
- mismos candidate/case schemas;
- mismo EVAL N=1056;
- misma corrección D906 de exactamente `87044110` y `87045110`;
- **único cambio metodológico/técnico permitido:** cerrar el productor/contrato de métricas MRR enriquecido.

## D1a
- mismo modelo congelado;
- size `470637416`;
- SHA-256 `ef9b92b2fb0239e46c0d81e403f00b3255d3822dfa25e0ce354d03828f7a8c87`;
- misma config/model semantics;
- rebuild completo del índice correctivo;
- misma EVAL N=1056;
- mismo contrato de 17 métricas.

No modifiques pesos, splits, EVAL, query, labels, BM25, ranking, Top-k, depth ni patch normativo.

---

# 6. ROOTS v0.3 — PROHIBIDO REUTILIZAR ATTEMPT03

Todos los roots prospectivos de v0.3 deben ser **nuevos y diferentes de los 16 roots v0.2**.

Usa nombres inequívocos con `v0.3` / `v03` para:

- EV03 D885 control index/output;
- EV03 Decision906 corpus/index/output;
- EV04 D885 control index/output;
- EV04 Decision906 corpus/index/output;
- D1a Decision906 corpus/index/evaluation/audit roots;
- unified evaluation/runtime roots.

El gate debe verificar antes de futura autorización/ejecución:

1. que todos los roots v0.3 estén ausentes;
2. que la presencia de roots parciales v0.2 de Attempt03 **no sea interpretada como un error ni como input reutilizable**;
3. que ningún output v0.2 parcial pueda ser consumido por v0.3.

No borres los parciales v0.2.

---

# 7. ARTEFACTOS v0.3

Construye una versión prospectiva autocontenida, como mínimo:

- gate JSON v0.3;
- EV03 execution spec v0.3;
- EV04 execution spec v0.3;
- D1a execution spec v0.3;
- manifest/hash ledger del gate v0.3;
- documentación técnica del gate v0.3;
- preparador/preflight v0.3;
- runner unificado v0.3;
- evaluator/adaptador v0.3 necesario para el contrato EV04 MRR;
- wrappers v0.3 de builder/D1a solo si son necesarios para aislar roots o bindings;
- tests v0.3.

Ruta recomendada de auditoría:

`outputs/audits/0b05c_corrective_numerical_gate_v0.3/`

Código recomendado:

- `src/experiments/prepare_0b05c_corrective_numerical_gate_v03.py`
- `src/experiments/evaluate_normative_bm25_corrective_0b05c_v03.py`
- `src/experiments/run_0b05c_corrective_numerical_v03.py`

Puedes añadir nuevos wrappers v03 estrictamente necesarios, pero no modificar los v02.

---

# 8. ESTADO INICIAL v0.3 — NO AUTORIZADO

El gate candidato debe quedar exactamente conceptualmente en:

- `gate_status = CANDIDATE_PENDING_EXTERNAL_AUDIT`;
- `authorization_readiness = NOT_AUTHORIZATION_READY`;
- EV03 numerical execution = `NOT_AUTHORIZED`;
- EV04 numerical execution = `NOT_AUTHORIZED`;
- D1a numerical execution = `NOT_AUTHORIZED`;
- unified numerical execution = `NOT_AUTHORIZED`;
- authorization record v0.3 absent;
- runtime authorization record v0.3 absent;
- corrective retrieval false;
- corrective metrics false;
- Attempt04 = `NOT_AUTHORIZED / NOT_EXECUTED`.

El failure record Attempt03 debe aparecer solo como provenance/dependency histórica que justifica v0.3.

No crees authorization record v0.3 en este bloque.

---

# 9. TESTS OBLIGATORIOS — SIN EJECUCIÓN NUMÉRICA REAL

Añade tests sintéticos/read-only que demuestren al menos:

1. **EV04 enriched MRR producer**:
   - casos con ranks dentro/fuera de 100/200;
   - MRR@100 y MRR@200 correctos;
   - legacy mrr == MRR@200;
   - contribution 101–200 correcta;
   - nombres/orden/schema exactos de metric_table.
2. con case rows equivalentes a un control sintético enriquecido, `metrics_exact=true` y `PASS_EXACT` puede alcanzarse.
3. eliminar/renombrar/reordenar un campo MRR hace fail-closed.
4. ranking/case mismatch sigue fallando aunque las métricas coincidan.
5. EV03 semántica recuperada no cambia.
6. los dos patches D906 siguen siendo exactamente `87044110` y `87045110`.
7. roots v0.3 son disjuntos de todos los roots v0.2.
8. roots parciales v0.2 no pueden ser usados como inputs v0.3.
9. gate v0.3 candidato no pasa `preflight_authorized()`.
10. Attempt04 no puede iniciarse desde el candidato.
11. D1a conserva el contrato exacto de 17 métricas.
12. no hay dependencia circular introducida.

Puedes usar `TemporaryDirectory` y fixtures mínimos. **No uses EVAL real ni ejecutes retrieval/model real para probar este bloque.**

Ejecuta las suites relevantes localmente y reporta conteos por suite. No las llames CI salvo que exista evidencia real de GitHub Actions.

---

# 10. PREFLIGHT DETACHED POST-COMMIT

Después de crear el commit candidato, usa un checkout/worktree detached limpio del commit y ejecuta únicamente el preflight no autorizado/read-only v0.3.

Debe confirmar:

- candidate gate válido;
- dependencies/bindings coherentes;
- roots v0.3 ausentes;
- v0.2 partial roots ignorados como evidencia histórica, nunca reutilizados;
- authorization readiness `NOT_AUTHORIZATION_READY`;
- ninguna ejecución numérica;
- cero outputs runtime v0.3.

No invoques `--execute-authorized`.

---

# 11. DIFF / COMMIT / PUSH

Construye **un único commit científico candidato** sobre `60aa7dd8715962f3c3e8b617e8797532529f39ed`.

Mensaje sugerido:

`fix: build 0b05c v0.3 recovery gate for EV04 MRR contract`

Push únicamente a:

`codex/0b05c-corrective-numerical-gate-v03`

No merge a `main`.
No rebase/amend/squash/cherry-pick/force-push.

Reporta:

- commit SHA;
- parent exacto;
- tree;
- compare vs `60aa7dd...`;
- lista completa de changed paths;
- cualquier path nuevo adicional y su justificación.

---

# 12. PERSISTENCIA ADMINISTRATIVA

Solo después del push científico:

1. fetch/checkout `codex/prompts-temporary`;
2. crea únicamente:
   `codex_prompts_tmp/18_RESPUESTA_CONSTRUIR_GATE_RECUPERACION_0B05C_V03_EV04_MRR.md`;
3. commit administrativo response-only;
4. mensaje sugerido:
   `docs: persist prompt 18 v0.3 EV04 recovery gate report`;
5. push normal, sin rebase/amend/force.

---

# 13. REPORTE FINAL OBLIGATORIO

Responde únicamente con:

### A. Preflight Git y baseline
SHA/tree/parent/main/Plan/article y estados v0.2 consumidos.

### B. Root cause binding
Prueba estática resumida del mismatch de esquema MRR.

### C. Diseño v0.3
Archivos, roots, bindings y separación v0.2/v0.3.

### D. Contrato EV04 MRR enriquecido
Función exacta, fields/order y tests.

### E. Invariantes científicos
EV03/EV04/D1a y D906 sin drift.

### F. Tests
Comandos y conteos; evidencia local vs CI claramente distinguida.

### G. Detached preflight
Resultado read-only y ausencia de ejecución.

### H. Diff/commit/push
Branch/SHA/parent/tree/changed paths.

### I. Persistencia administrativa
Response path y commit administrativo.

### J. Estado científico
Termina exactamente con:

`GROUP_2 = EN_CURSO`

`0B05C_NUMERICAL_GATE_V02 = APPROVED / VERSIONED / INTEGRATED / HISTORICAL / AUTHORIZATION_CONSUMED`

`0B05C_ATTEMPT03 = FAIL_CLOSED / SCIENTIFIC_STATE_PRESERVED / FAILURE_RECORD_VERSIONED / INTEGRATED`

`EV04_RECOVERY_ROOT_CAUSE = EV04_FROZEN_METRIC_SCHEMA_PRODUCER_MISMATCH_AFTER_GATE_C_MRR_MICROAUDIT`

`0B05C_V03_RECOVERY_GATE = CANDIDATE_PENDING_EXTERNAL_AUDIT`

`0B05C_V03_AUTHORIZATION_READINESS = NOT_AUTHORIZATION_READY`

`EV03_V03_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED`

`EV04_V03_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED`

`D1A_V03_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED`

`UNIFIED_0B05C_V03_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED`

`ATTEMPT04 = NOT_AUTHORIZED / NOT_EXECUTED`

`0B05C_METRIC_IMPACT = NOT_DETERMINED`

`DOWNSTREAM_REEXECUTION = NOT_YET_JUSTIFIED`

`0B05C_CLOSURE = NOT_AUTHORIZED`

No autorices ni ejecutes Attempt04.