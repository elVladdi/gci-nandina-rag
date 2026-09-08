# CODEX — CONSTRUIR CANDIDATURA DEL GATE/RUNNER NUMÉRICO 0B-05C v0.2

## 0. ROL Y OBJETIVO

Actúa exclusivamente como **EJECUTOR DE PREPARACIÓN PROSPECTIVA DEL GATE NUMÉRICO 0B-05C v0.2**.

Debes construir, congelar, probar y publicar en una **rama candidata separada** el contrato ejecutable futuro para la sensibilidad normativa 0B-05C después de la recuperación histórica EV03 v0.2 ya integrada.

Este bloque es **PRE-EJECUCIÓN**. Está terminantemente prohibido:

- autorizar ejecución numérica;
- ejecutar EV03 corrected Decision906;
- ejecutar EV04 control o corrected sobre EVAL real;
- ejecutar D1a corrected;
- ejecutar el runner unificado real;
- calcular métricas correctivas nuevas;
- crear runtime authorization record;
- escribir en los roots científicos futuros de v0.2;
- modificar `main`, Plan Maestro, `article/main-manuscript`, EXP11B o EXP12.

El resultado esperado es un **candidato audit-able**, no integrado, cuyo estado final sea:

`0B05C_NUMERICAL_GATE_V02 = CANDIDATE_PENDING_EXTERNAL_AUDIT`

`0B05C_V02_AUTHORIZATION_READINESS = NOT_AUTHORIZATION_READY`

Las cuatro ejecuciones deben permanecer `NOT_AUTHORIZED / NOT_EXECUTED`.

---

## 1. IDENTIDADES GOBERNANTES — VERIFICAR ANTES DE ESCRIBIR

Repositorio: `elVladdi/gci-nandina-rag`.

### Rama científica

Debe cumplirse exactamente:

`main = origin/main = 43291c312c2934aae03f3c087dd0a1ae594341b7`

Tree esperado:

`9f21cb79c37cbcdf93006503bb4f888f1acfc975`

### Plan Maestro

Rama:

`docs/plan-maestro-temporal-2026-08-31`

HEAD esperado:

`fe847f708d4d1ded92b5a50a38d4913bb69ed311`

Solo lectura. No modificar.

### Artículo

`article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5`

Solo lectura. No modificar.

### Recovery EV03 integrada

Commits:

`cef8d7ad58d877e933f8c86b9f721cb214d9058d`
→ `43291c312c2934aae03f3c087dd0a1ae594341b7`

Debe mantenerse:

- `EV03_HISTORICAL_RECOVERY_V02=APPROVED/VERSIONED/INTEGRATED`;
- `LOGICAL_INDEX_IDENTITY=EXACT`;
- `EV03_DECISION885_CONTROL_REPRODUCTION=PASS_EXACT`;
- `HISTORICAL_SEMANTICS_RECOVERED_AND_EXACTLY_VALIDATED`;
- `AUTHENTIC_HISTORICAL_SOURCE_PY=NOT_VERSIONED_AT_INDEX_CREATION`;
- política EV03 recuperada: `DROP_SINGLE_CHARACTER_TOKENS`.

Si cualquiera de las identidades de rama/commit no coincide: **STOP** y reporta. No improvises.

---

## 2. RAMA CANDIDATA

Crea exclusivamente, si no existe ya remotamente:

`codex/0b05c-corrective-numerical-gate-v02`

Debe partir exactamente de:

`43291c312c2934aae03f3c087dd0a1ae594341b7`

Si la rama ya existe en local o remoto, **STOP**. No reutilices, no reset, no force-push.

Preferir worktree limpio separado. No usar `git clean`, reset destructivo ni tocar el worktree que contiene evidencia local de Intentos 01/02.

---

## 3. FUENTES DE VERDAD QUE DEBES LEER ÍNTEGRAMENTE

### Recovery EV03 v0.2 integrada

- `docs/0B05C_EV03_HISTORICAL_BUILDER_RECOVERY_V02.md`
- `src/experiments/build_bm25_ev03_historical_recovered_v02.py`
- `src/experiments/verify_ev03_historical_builder_recovery_v02.py`
- `outputs/audits/0b05c_ev03_historical_builder_recovery_v0.2/ev03_corrective_execution_spec_v0.2.json`
- `outputs/audits/0b05c_ev03_historical_builder_recovery_v0.2/ev03_decision885_control_reproduction_v0.2.json`
- `outputs/audits/0b05c_ev03_historical_builder_recovery_v0.2/ev03_logical_index_identity_v0.2.json`
- `outputs/audits/0b05c_ev03_historical_builder_recovery_v0.2/0b05c_corrective_numerical_gate_v0.2.json`
- manifest y hash ledger del mismo root.

### v0.1 histórica — solo como contrato antecedente, nunca para ejecutar nuevamente

- `outputs/audits/0b05c_corrective_numerical_gate_v0.1/0b05c_corrective_numerical_execution_gate_v0.1.json`
- `outputs/audits/0b05c_corrective_numerical_gate_v0.1/ev03_corrective_execution_spec_v0.1.json`
- `outputs/audits/0b05c_corrective_numerical_gate_v0.1/ev04_corrective_execution_spec_v0.1.json`
- `outputs/audits/d1a_preexecution_0b05c_v0.1/d1a_0b05c_corrective_execution_spec_v0.1.json`
- `src/experiments/run_0b05c_corrective_numerical_v01.py`
- `src/experiments/build_bm25_corrective_0b05c_v01.py`
- `src/experiments/evaluate_normative_bm25_corrective_0b05c_v01.py`
- `src/experiments/run_d1a_corrective_0b05c_v01.py`
- tests correspondientes.

La v0.1 es `HISTORICAL / INTEGRATED / SUPERSEDED_FOR_NEW_EXECUTION`. No modificar ninguno de sus artefactos.

---

## 4. PRINCIPIO METODOLÓGICO OBLIGATORIO

La v0.2 no redefine el experimento. Corrige únicamente la reproducibilidad del brazo EV03 y separa los roots de una futura ejecución nueva.

### 4.1 EV03

EV03 debe usar **exclusivamente** la semántica histórica recuperada:

`DROP_SINGLE_CHARACTER_TOKENS`

con:

- `k1=1.5`;
- `b=0.75`;
- stopwords españolas congeladas;
- mismo esquema y orden del corpus;
- misma normalización restante;
- mismo ranking NANDINA-8;
- misma profundidad 100;
- mismo EVAL fijo de 1,056 casos;
- mismos contratos de métricas y comparación.

La semántica global actual de `src/bm25_index.py` **no puede usarse directamente para EV03** si conserva tokens de longitud 1.

No modifiques `src/bm25_index.py`.

La reproducción del control Decision885 durante la futura ejecución debe ser obligatoria y debe exigir:

- logical index identity exact;
- ranking completo exacto;
- ranking bytes exactos donde el contrato ya lo demuestra;
- case summary exacta;
- case summary bytes exactos;
- metric table exacta;
- full metrics exactas;
- 50,327 filas de ranking;
- 1,056 casos;
- frozen ranking SHA-256 `d2edc692d54b015525e193a1c067d2828aaedf48ff40e947d690b8aebd7ca015`;
- frozen case-summary SHA-256 `f75d7d8ae65dda30990b819e8f662614585563d5adeb7d54344b2ae14c3522e0`.

Solo después de ese PASS exacto puede alcanzarse el corrected arm EV03.

### 4.2 EV04

EV04 **NO hereda** la política recuperada de EV03.

Debe preservar la semántica jerárquica original v0.1, incluida:

- `texto_index_jerarquico` con fallback aprobado;
- collapse efectivo a código NANDINA-8 único;
- depth 200;
- mismo orden/tie behavior;
- mismos parámetros BM25;
- mismo EVAL y contratos de métricas.

Como la identidad original EV04 estaba clasificada `NOT_VERIFIABLE_FROM_FROZEN_ARTIFACTS`, la futura ejecución debe reproducir primero Decision885 y bloquear el corrected arm si la reproducción no es exacta conforme al contrato congelado.

No ejecutes esa reproducción real en este bloque. Solo congela y prueba la lógica del gate con fixtures/fakes/temporales.

### 4.3 D1a

D1a debe preservar exactamente:

- pesos originales congelados;
- `MODEL_POLICY=FREEZE_ORIGINAL_D1A_WEIGHTS`;
- sin retraining;
- misma consulta EVAL;
- misma configuración/modelo;
- misma profundidad 200;
- reconstrucción **FULL_ATOMIC_INDEX_AND_MAPPING_REBUILD** sobre el corpus corregido;
- mismos contratos de métricas;
- sin cambios de arquitectura, embeddings, loss, scoring o ranking.

Los únicos cambios permitidos respecto de la ejecución prospectiva v0.1 son:

1. namespace/roots v0.2 nuevos y no colisionantes;
2. binding al gate unificado v0.2;
3. ajustes técnicos estrictamente necesarios para hacer esos roots parametrizables y fail-closed, sin cambiar la semántica científica.

---

## 5. PATCH NORMATIVO CONGELADO

No reinterpretar la Decisión 906. Reutiliza exactamente el contrato ya congelado.

Únicamente se modifican los dos documentos NANDINA-8:

- `87044110`
- `87045110`

Texto oficial congelado:

`Inferior a 4,537 t`

Los replacements técnicos deben coincidir exactamente con el contrato v0.1/D1a ya versionado, incluyendo `titulo`, `texto_index`, `texto`, `version` y contexto sintético aprobado.

No ampliar el patch a otros códigos ni alterar Decision885 fuera de esos dos documentos.

---

## 6. ROOTS v0.2 — DISTINTOS Y FAIL-CLOSED

No usar ni sobrescribir ningún root v0.1 de Intentos 01/02.

Congela roots v0.2 nuevos como mínimo:

### EV03

Control Decision885:

- `data/processed/indexes/bm25_nandina8_ev03_decision885_control_v0.2/`
- `outputs/evaluation/normative_bm25_flat_ev03_decision885_control_v0.2/`

Corrected Decision906:

- `data/processed/corpus_rag_v1_index_ev03_corrective_decision906_v0.2.jsonl`
- `data/processed/indexes/bm25_nandina8_ev03_corrective_decision906_v0.2/`
- `outputs/evaluation/normative_bm25_flat_corrective_decision906_v0.2/`

### EV04

Control Decision885:

- `data/processed/indexes/bm25_nandina8_ev04_decision885_control_v0.2/`
- `outputs/evaluation/normative_bm25_hierarchical_ev04_decision885_control_v0.2/`

Corrected Decision906:

- `data/processed/corpus_rag_v1_index_ev04_corrective_decision906_v0.2.jsonl`
- `data/processed/indexes/bm25_nandina8_ev04_corrective_decision906_v0.2/`
- `outputs/evaluation/normative_bm25_hierarchical_corrective_decision906_v0.2/`

Si EV03 y EV04 comparten una misma materialización corregida por ser byte-idéntica, el contrato puede definir una fuente común **solo si queda explícitamente demostrado y hash-frozen**; no lo asumas por conveniencia.

### D1a

- `data/processed/corpus_rag_v1_index_d1a_corrective_decision906_v0.2.jsonl`
- `data/processed/indexes/text2trade_mnrl_nandina8_d1a_corrective_v0.2/`
- `outputs/evaluation/d1a_corrective_0b05c_v0.2/`
- `outputs/audits/d1a_corrective_0b05c_runtime_v0.2/`

### Unified runtime

- `outputs/evaluation/0b05c_corrective_numerical_v0.2/`
- `outputs/audits/0b05c_corrective_numerical_runtime_v0.2/`

Todos deben cumplir:

- ausencia obligatoria antes de autorización/ejecución;
- creación única;
- no overwrite;
- no resume;
- fallo cerrado si cualquier root ya existe.

**En este Prompt 09 ninguno de esos roots científicos puede crearse.** Los tests deben usar temporales externos o fixtures sintéticos.

---

## 7. ARTEFACTOS A CREAR EN LA RAMA CANDIDATA

Diseña lo mínimo necesario, pero el candidato debe contener como mínimo:

### Código

- `src/experiments/prepare_0b05c_corrective_numerical_gate_v02.py`
- `src/experiments/build_bm25_corrective_0b05c_v02.py`
- `src/experiments/run_0b05c_corrective_numerical_v02.py`

Si D1a no puede usar sus roots v0.2 sin alterar el runner v0.1, crea además:

- `src/experiments/run_d1a_corrective_0b05c_v02.py`

No modifiques el runner v0.1.

### Tests

- `tests/test_0b05c_corrective_numerical_gate_v02.py`

Si creas runner D1a v0.2, añade test específico cuando sea necesario.

### Documentación

- `docs/0B05C_CORRECTIVE_NUMERICAL_GATE_V02.md`

### Audit root nuevo

`outputs/audits/0b05c_corrective_numerical_gate_v0.2/`

Debe contener como mínimo:

- `ev03_numerical_execution_spec_v0.2.json`
- `ev04_numerical_execution_spec_v0.2.json`
- `d1a_numerical_execution_spec_v0.2.json`
- `0b05c_corrective_numerical_execution_gate_v0.2.json`
- `0b05c_corrective_numerical_gate_manifest_v0.2.json`
- `0b05c_corrective_numerical_gate_hash_ledger_v0.2.json`

Puedes añadir artefactos auxiliares si son necesarios para trazabilidad, pero no generes outputs numéricos de ejecución.

---

## 8. RUNNER UNIFICADO v0.2 — ORDEN CONGELADO

El runner futuro debe congelar este orden exacto:

1. `01_unified_preflight`
2. `02_EV03_Decision885_control_reproduction`
3. `03_EV03_control_reproduction_verification`
4. `04_EV03_corrected_corpus_materialization`
5. `05_EV03_corrected_index_build_RECOVERED_HISTORICAL_SEMANTICS`
6. `06_EV03_corrected_evaluation`
7. `07_EV04_Decision885_control_reproduction`
8. `08_EV04_control_reproduction_verification`
9. `09_EV04_corrected_corpus_materialization`
10. `10_EV04_corrected_index_build`
11. `11_EV04_corrected_evaluation`
12. `12_D1a_corrected_execution_under_v02_authorization`
13. `13_integrity_validation`
14. `14_case_level_comparisons`
15. `15_aggregate_comparisons`
16. `16_unified_sensitivity_summary`
17. `17_execution_manifest`
18. `18_exact_hash_ledger`
19. `19_final_completion_state`

Reglas:

- ningún side effect antes de validar autorización futura de los cuatro componentes;
- EV03 corrected inaccesible antes de PASS exacto del control;
- EV04 corrected inaccesible antes de PASS exacto del control;
- D1a se ejecuta después de ambos brazos BM25;
- si cualquier step falla, STOP; no continuar, no retry, no resume;
- `final_completion_state` solo puede ser PASS si los 18 pasos anteriores existen y pasaron conforme a contrato.

El runner debe tener, como mínimo:

- modo read-only `--preflight` para estado no autorizado;
- modo futuro `--execute-authorized` que en el estado candidato actual **debe fallar cerrado antes del primer side effect** porque no existe autorización;
- no debe existir ningún modo oculto que permita omitir controls o autorización.

---

## 9. GATE / AUTORIZACIÓN — ESTADO CANDIDATO

El gate versionado debe declarar inequívocamente:

`gate_version = v0.2`

`gate_status = CANDIDATE_PENDING_EXTERNAL_AUDIT`

`gate_scope = UNIFIED_0B05C_NUMERICAL_PREEXECUTION`

`authorization_readiness = NOT_AUTHORIZATION_READY`

Y:

- `EV03_NUMERICAL_EXECUTION = NOT_AUTHORIZED`
- `EV04_NUMERICAL_EXECUTION = NOT_AUTHORIZED`
- `D1A_NUMERICAL_EXECUTION = NOT_AUTHORIZED`
- `UNIFIED_0B05C_NUMERICAL_EXECUTION = NOT_AUTHORIZED`
- `corrective_retrieval_executed = false`
- `corrective_metrics_computed = false`
- `runtime_authorization_record_present = false`
- `0B05C_METRIC_IMPACT = NOT_DETERMINED`
- `DOWNSTREAM_REEXECUTION = NOT_YET_JUSTIFIED`
- `0B05C_CLOSURE = NOT_AUTHORIZED`

No crear authorization record v0.2 en este bloque.

Define prospectivamente el esquema de una futura transición de autorización, pero no la ejecutes. La futura autorización deberá ser un bloque separado y auditable.

---

## 10. BINDINGS CANÓNICOS

Congela fail-closed con Git blob SHA-1 + SHA-256 canónico sobre bytes `git cat-file blob` para todo código/input Git-tracked que determine el resultado.

Como mínimo:

### EV03

- recovered EV03 builder;
- verifier EV03 recovery;
- builder correctivo v0.2;
- evaluator BM25;
- `src/bm25_index.py` como dependencia residual, sin confundirla con la token policy EV03;
- retrieval BM25;
- metrics;
- config;
- corpus Decision885;
- EVAL;
- índice histórico EV03;
- ranking/case-summary/run metadata congelados.

### EV04

Congela todos los builders/evaluators/dependencies que determinan la jerarquía y el collapse, además de corpus/EVAL/control outputs originales.

### D1a

Congela:

- runner v0.2 si existe;
- builder del índice dense;
- evaluator;
- config/model policy;
- corpus original;
- EVAL;
- pesos/model snapshot;
- Top200 original;
- cualquier mapping/index identity contractual necesaria.

Para binarios usar Git blob SHA-1 + SHA-256 exacto del blob/file según corresponda.

No usar SHA del worktree CRLF como identidad autoritativa.

Añade reglas LF en `.gitattributes` **solo** para los nuevos archivos textuales v0.2 creados por este bloque. No alteres reglas no relacionadas.

---

## 11. PREFLIGHT READ-ONLY DEL CANDIDATO

Debe existir un preflight que pueda ejecutarse desde un checkout limpio del commit candidato y que no escriba en roots científicos.

Debe validar como mínimo:

- base/recovery commit `43291c...` es ancestro de HEAD;
- worktree tracked limpio;
- bindings canónicos exactos;
- recovery EV03 integrada presente y sus contratos `EXACT/PASS_EXACT`;
- v0.1 permanece histórica y no es usada como autorización vigente;
- todos los roots v0.2 científicos ausentes;
- cuatro autorizaciones `NOT_AUTHORIZED`;
- authorization record v0.2 ausente;
- runtime record v0.2 ausente;
- corrected metrics no calculadas.

Resultado esperado del candidato:

`status=PASS`

`mode=PREEXECUTION_CLOSED_READONLY`

`authorization_readiness=NOT_AUTHORIZATION_READY`

No debe producir archivos del repositorio.

---

## 12. TESTS MÍNIMOS OBLIGATORIOS

Los tests pueden usar fixtures, monkeypatch, fakes o `TemporaryDirectory`, pero **no EVAL real para ejecutar retrieval correctivo**.

Debes demostrar al menos:

1. preflight cerrado PASS en candidato limpio;
2. cuatro autorizaciones NOT_AUTHORIZED;
3. `--execute-authorized` falla antes de side effects;
4. ausencia de todos los roots científicos futuros;
5. no-overwrite/no-resume;
6. orden exacto de 19 pasos con operaciones fake;
7. failure short-circuit en cualquier step crítico;
8. EV03 corrected bloqueado si control no es PASS exacto;
9. EV04 corrected bloqueado si control no es PASS exacto;
10. EV03 builder v0.2 usa semántica `DROP_SINGLE_CHARACTER_TOKENS` y no la semántica global divergente;
11. EV04 no hereda `DROP_SINGLE_CHARACTER_TOKENS` por accidente;
12. patches Decision906 exactamente dos códigos y texto congelado;
13. D1a preserva pesos/config/model policy y no retraining;
14. roots v0.2 son distintos de todos los roots v0.1;
15. canonical Git bindings fallan cerrado ante mutación;
16. response/gate/manifests no contienen ningún `AUTHORIZED` operativo;
17. ningún test crea outputs persistentes fuera de temp.

Ejecuta además regresiones razonables sobre:

- EV03 recovery v0.2;
- 0B05C v0.1;
- D1a preexecution/runner;
- normative BM25 flat/hierarchical;

sin ejecutar ninguna sensibilidad real.

No afirmar CI si no existe CI.

---

## 13. ARTEFACTOS VERSIONADOS DEL GATE

El manifest debe distinguir:

- frozen inputs;
- code bindings;
- control baselines;
- future execution roots;
- audit roots;
- generated-at-future-runtime outputs;
- explicit non-executed state.

El hash ledger debe distinguir al menos:

- `VERSIONED_GIT_BLOB`
- `FROZEN_BINARY_GIT_BLOB`
- `FROZEN_FILE_IDENTITY` cuando aplique
- `FUTURE_GENERATED_OUTPUT_NOT_PRESENT`

No inventar hashes de outputs futuros.

El ledger debe tener `mismatch_count=0` para lo que existe y marcar outputs futuros como ausentes/no generados, no como hash vacío.

---

## 14. AISLAMIENTO OBLIGATORIO

Al finalizar candidato:

- `main` debe seguir `43291c312c2934aae03f3c087dd0a1ae594341b7`;
- Plan debe seguir `fe847f708d4d1ded92b5a50a38d4913bb69ed311`;
- article debe seguir `254b1e6df736fa9938ac86a515d65b36f4d361c5`;
- EXP11B/EXP12 sin cambios;
- v0.1 sin cambios;
- Intentos 01/02 preservados;
- ningún future execution root v0.2 presente;
- ninguna métrica nueva observada.

No actualices todavía el Plan Maestro con la candidatura. La actualización del Plan ocurrirá solo después de auditoría externa e integración si corresponde.

---

## 15. COMMIT / PUSH CANDIDATO

Solo si todo pasa:

- un único commit científico candidato sobre la rama nueva;
- mensaje sugerido: `feat: prepare 0b05c corrective numerical gate v0.2`;
- push solo a `codex/0b05c-corrective-numerical-gate-v02`;
- no merge a `main`;
- no rebase/amend/force-push.

Reporta SHA, parent, tree y lista exacta de files changed.

---

## 16. PERSISTENCIA ADMINISTRATIVA OBLIGATORIA DE TU RESPUESTA

Después de terminar el trabajo científico y publicar la rama candidata, debes guardar **exactamente tu reporte final** en la rama administrativa:

`codex/prompts-temporary`

Path obligatorio:

`codex_prompts_tmp/09_RESPUESTA_CONSTRUIR_GATE_RUNNER_NUMERICO_0B05C_V02.md`

Reglas:

1. No sobrescribas ni modifiques `09_CONSTRUIR_GATE_RUNNER_NUMERICO_0B05C_V02.md`.
2. No modifiques ningún otro archivo de la rama administrativa.
3. Haz un commit administrativo separado que contenga únicamente el archivo de respuesta.
4. Push solo a `codex/prompts-temporary`.
5. El commit administrativo no forma parte de la rama científica candidata.
6. Si el archivo de respuesta ya existe, **STOP** antes de sobrescribirlo y reporta la colisión.

Esta excepción administrativa es obligatoria; no interpretes ninguna restricción de ramas como prohibición de persistir esta respuesta.

---

## 17. REPORTE FINAL OBLIGATORIO

Responde únicamente con secciones A–N:

### A. Preflight Git
- heads exactos main/Plan/article;
- tree main;
- rama candidata;
- base/parent;
- clean state.

### B. Scope creado
- files exactos añadidos/modificados;
- justificación de cada uno.

### C. EV03 v0.2
- builder recuperado usado;
- cómo se impide semántica len1 divergente;
- control exacto requerido;
- roots congelados.

### D. EV04 v0.2
- semántica preservada;
- mandatory control reproduction;
- roots congelados.

### E. D1a v0.2
- pesos/config/model policy;
- no retraining;
- atomic rebuild;
- roots v0.2.

### F. Patch Decision906
- dos códigos exactos;
- texto congelado;
- ausencia de ampliaciones.

### G. Runner unificado
- 19 pasos exactos;
- fail-closed;
- no retry/resume/overwrite.

### H. Gate/autorización
- gate status/scope/readiness;
- cuatro NOT_AUTHORIZED;
- no authorization/runtime record;
- no ejecución.

### I. Canonical bindings
- cantidad y categorías;
- hashes/blob policy;
- EOL portability.

### J. Tests
- RUN/PASS/FAIL/ERROR/SKIP por suites;
- preflight candidate;
- confirmación de que no se ejecutó retrieval correctivo real.

### K. Aislamiento
- main/Plan/article/EXP11B/EXP12/v0.1;
- future roots ausentes;
- evidencia Intentos 01/02 preservada.

### L. Commit candidato
- SHA, parent, tree, files changed, push;
- ahead/behind vs main.

### M. Persistencia administrativa
- response path;
- parent/commit administrativo;
- único archivo administrativo;
- `RESPONSE_PERSISTENCE=PASS`.

### N. Estado científico

Termina exactamente con:

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

No declares integración aprobada. La auditoría externa posterior decidirá si la candidatura puede integrarse.