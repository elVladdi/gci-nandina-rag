# CODEX — MICROCLOSE ADICIONAL DEL GATE/RUNNER NUMÉRICO 0B-05C v0.2 — F007–F010

## 0. ROL Y OBJETIVO

Actúa exclusivamente como **EJECUTOR DE CORRECCIONES DE PRE-EJECUCIÓN** sobre la misma candidatura:

`codex/0b05c-corrective-numerical-gate-v02`

Estado remoto que debe existir antes de escribir:

- candidato inicial Prompt 09: `b0a1e61f70f42aa2048338965cc003e032d3a493`;
- microclose Prompt 10: `59dc445d8128dd71f48d26eac66c9ae8d0c21e38`;
- parent de `59dc445...` = `b0a1e61f70f42aa2048338965cc003e032d3a493`;
- tree de `59dc445...` = `3243c6bcc5030dd07c86bd593596e420212541cf`;
- `origin/main = 43291c312c2934aae03f3c087dd0a1ae594341b7`;
- Plan Maestro = `fe847f708d4d1ded92b5a50a38d4913bb69ed311`;
- article = `254b1e6df736fa9938ac86a515d65b36f4d361c5`.

La auditoría externa del Prompt 10 concluye:

- **F001–F006 = CLOSED / PASS**;
- pero la candidatura aún es **`PASS_WITH_FINDINGS / CORRECTION_REQUIRED`** por cuatro hallazgos nuevos F007–F010 descritos abajo.

Este bloque continúa siendo **PRE-EJECUCIÓN**. Está prohibido:

- autorizar EV03, EV04, D1a o unified;
- ejecutar retrieval/control real sobre EVAL;
- cargar el modelo D1a para una corrida;
- calcular métricas correctivas nuevas;
- crear authorization record v0.2 real;
- crear runtime authorization record real;
- crear cualquiera de los 16 roots científicos futuros v0.2;
- modificar `main`, Plan Maestro, article, EXP11B, EXP12 o artefactos v0.1;
- amend, rebase o force-push.

Trabaja sobre la misma rama candidata y, si todo pasa, agrega **un único commit correctivo adicional** encima de `59dc445d8128dd71f48d26eac66c9ae8d0c21e38`.

---

# 1. F007 — BUILDER v0.2 / EVALUATOR METADATA CONTRACT MISMATCH — BLOCKING_INTEGRATION

## Evidencia externa

`src/experiments/build_bm25_corrective_0b05c_v02.py` escribe actualmente metadata con campos top-level:

- `input_sha256`;
- `index_sha256`;
- `bm25_params`;
- `semantics`.

Pero el evaluator congelado que el runner v0.2 invoca:

`src/experiments/evaluate_normative_bm25_corrective_0b05c_v01.py`

consume en `validate_dynamic_inputs()` el contrato histórico:

- `metadata["input"]["corpus_sha256"]`;
- `metadata["output"]["bm25_index_sha256"]`;
- `metadata["arm"]`;
- `metadata["bm25_params"]`.

Por tanto, una futura llamada real:

`builder.build(...) -> evaluator.evaluate_arm(...)`

fallará antes del retrieval por incompatibilidad estructural de metadata, aunque las suites declarativas actuales pasen.

## Corrección obligatoria

Haz compatible el builder v0.2 con el evaluator contractual **sin cambiar ninguna semántica científica**.

El metadata v0.2 debe preservar explícitamente como mínimo:

```text
arm
bm25_params.k1
bm25_params.b
input.corpus_path
input.corpus_sha256
input.config_path
input.config_sha256
output.bm25_index_path
output.bm25_index_sha256
output.metadata_path
```

Puedes conservar además `semantics`, `artifact_id`, `index_stats`, `identity_policy`, etc., pero el contrato consumido por `validate_dynamic_inputs()` debe quedar satisfecho inequívocamente.

No modifiques el evaluator v0.1 salvo que sea absolutamente imprescindible; preferencia fuerte: corregir únicamente el producer v0.2.

### Test obligatorio F007

Añade un test sintético real, usando `TemporaryDirectory`, que:

1. cree config BM25 mínimo `k1=1.5`, `b=0.75`;
2. cree corpus sintético válido;
3. ejecute realmente `build_bm25_corrective_0b05c_v02.build()` sobre ese corpus en temp;
4. invoque realmente `evaluate_normative_bm25_corrective_0b05c_v01.validate_dynamic_inputs()` sobre el índice/metadata generados;
5. demuestre que `corpus_sha256` e `index_sha256` coinciden y el índice carga correctamente.

Hazlo al menos para EV03. Si es razonable y barato, añade fixture EV04 sintético también. **No invoques EVAL real ni `evaluate_arm()` sobre el dataset real.**

Añade test negativo para metadata incompatible/mutada.

---

# 2. F008 — D1a STANDALONE EXECUTION CAN BYPASS UNIFIED AUTHORIZATION — BLOCKING_AUTHORIZATION

## Evidencia externa

`src/experiments/run_d1a_corrective_0b05c_v02.py::execute_authorized()` actualmente exige únicamente:

`spec["authorization"]["D1A_NUMERICAL_EXECUTION"] == "AUTHORIZED"`

antes de iniciar su propio flujo.

No exige por sí mismo:

- gate unified `APPROVED / INTEGRATED`;
- readiness `AUTHORIZATION_APPROVED / READY_FOR_SINGLE_EXECUTION`;
- las cuatro autorizaciones;
- authorization record v0.2;
- baseline transition válido.

Sin embargo, el propio spec publica un command standalone:

`python -B -m src.experiments.run_d1a_corrective_0b05c_v02 --execute-authorized`

Así, un D1a spec aislado marcado `AUTHORIZED` podría iniciar side effects sin demostrar el gate unificado completo.

## Corrección obligatoria

La ejecución D1a v0.2 debe quedar ligada mecánicamente a la **misma prueba de autorización unificada** cerrada por F001.

Diseño recomendado:

- permitir que `run_d1a_corrective_0b05c_v02.execute_authorized()` reciba opcionalmente un `authorization_proof` ya validado;
- cuando se invoque directamente por CLI, obtener primero un proof mediante el preflight autorizado unificado **antes del primer side effect**;
- cuando el runner unificado llegue al paso 12, pasar el proof ya obtenido en `01_unified_preflight`, evitando reejecutar un preflight que exigiría roots ausentes después de que EV03/EV04 ya produjeron sus roots;
- validar el proof recibido: `status=PASS`, `mode=AUTHORIZED_PREFLIGHT_ONLY`, cuatro estados `AUTHORIZED`, baseline commit presente y authorization record válido/referenciado;
- conservar además la autorización propia D1a spec = `AUTHORIZED`.

No introduzcas dependencia circular a import time. Si necesitas importar el runner unificado, hazlo localmente dentro del camino CLI/directo o factoriza validación común en un módulo ya permitido.

### Tests obligatorios F008

- cambiar solo D1a spec a `AUTHORIZED`, manteniendo gate/unified cerrado, debe fallar antes de cualquier escritura;
- direct `execute_authorized` sin proof válido debe intentar validar gate unified y fallar cerrado en fixture cerrado;
- un proof sintético completo/validado puede pasar a la función D1a sin reejecutar el check de `FUTURE_ROOTS` en el paso 12;
- ningún test crea roots reales.

---

# 3. F009 — RUNTIME AUTHORIZATION PROVENANCE IS DISCARDED — BLOCKING_POSTEXECUTION_AUDITABILITY

## Evidencia externa

`preflight_authorized()` ya devuelve correctamente:

- `authorization_baseline_commit`;
- `authorization_record`;
- bundle autorizado.

Pero el paso `01_unified_preflight` actualmente escribe `runtime_authorization_record_v0.2.json` solo con:

- `status`;
- `mode`;
- `authorization`.

Y `execution_manifest_v0.2.json` tampoco conserva de forma explícita el baseline/authorization-record que permitió esa corrida.

Así, la prueba de autorización se valida en memoria pero se pierde de los outputs auditables de runtime.

## Corrección obligatoria

Congela ahora un contrato de provenance de runtime. En una ejecución futura autorizada, el `runtime_authorization_record_v0.2.json` debe incluir como mínimo:

- `status`;
- `execution_authorization_commit` = commit HEAD de la autorización que ejecuta;
- `authorization_baseline_commit`;
- los cuatro estados `AUTHORIZED`;
- referencia al authorization record comprometido, incluyendo como mínimo `path`, Git blob SHA-1, SHA-256 canónico y size;
- `baseline_external_audit`;
- identidad/referencia de gate + EV03 spec + EV04 spec + D1a spec autorizados, o una referencia inequívoca a bindings ya validados.

El execution manifest debe referenciar el runtime authorization record por `path + SHA-256 + size` y conservar al menos `execution_authorization_commit` y `authorization_baseline_commit`.

No crear esos records ahora. Solo congelar schema/lógica y probar con fixtures/mocks.

El `runtime_hash_ledger_contract` debe seguir incluyendo runtime auth record y manifest; si cambian schemas, regenera contratos determinísticamente.

### Tests obligatorios F009

- construir un proof sintético válido y verificar que la función que arma runtime provenance no pierde baseline/record/current commit;
- manifest debe contener referencia hash/size al runtime authorization record;
- falta de baseline o record binding debe fallar cerrado.

---

# 4. F010 — D1a AGGREGATE VALIDATION ACCEPTS EMPTY METRICS — BLOCKING_INTEGRITY

## Evidencia externa

`_d1a_summary_reference()` valida actualmente:

```python
require(isinstance(aggregate.get("metrics"), list), ...)
```

pero acepta `metrics=[]`.

De hecho, el test actual `test_37_d1a_summary_requires_aggregate_and_integrity_evidence` construye `{"metrics": []}` y lo considera válido.

El producer D1a real `build_aggregate_comparison()` genera la tabla de **17 métricas congeladas**:

- Top@1, Top@3, Top@5, Top@10, Top@50;
- Recall@100, Recall@200;
- MRR@100, MRR@200;
- Exact@100, Exact@200;
- HS6@100, HS6@200;
- HS4@100, HS4@200;
- Chapter@100, Chapter@200.

## Corrección obligatoria

`_d1a_summary_reference()` debe validar como mínimo:

- `metrics` es lista no vacía;
- longitud exacta conforme al `comparison_contract.aggregate_metrics` del spec;
- nombres y orden exactos según contrato;
- cada fila contiene los campos contractuales necesarios: `metric`, `original_numerator`, `corrected_numerator`, `denominator`, `original_value`, `corrected_value`, `absolute_delta`;
- campos numéricos válidos;
- no métricas duplicadas.

No recalcules resultados; solo valida la estructura contractual ya producida por D1a.

### Tests obligatorios F010

- `metrics=[]` debe fallar;
- una métrica faltante debe fallar;
- orden/nombre alterado debe fallar;
- schema de fila incompleto debe fallar;
- fixture completo con las 17 métricas debe pasar.

---

# 5. PRESERVAR F001–F006 Y TODOS LOS INVARIANTES CIENTÍFICOS

No reabras ni debilites las correcciones del Prompt 10:

- authorization transition + record schema;
- EV03 `PASS_EXACT` completo;
- EV04 `PASS_EXACT` completo y commands/roots coherentes;
- runtime exact ledger allowlist;
- unified D1a references;
- tests F001–F006.

No cambies:

- EV03 `DROP_SINGLE_CHARACTER_TOKENS`;
- k1=1.5, b=0.75;
- EVAL N=1,056;
- depths 100/200;
- EV04 hierarchy/collapse/ties;
- Decision906 exactamente `87044110` y `87045110` y texto congelado;
- D1a weights/config/scoring/ranking;
- `FREEZE_ORIGINAL_D1A_WEIGHTS`;
- `must_not_retrain=true`;
- `FULL_ATOMIC_INDEX_AND_MAPPING_REBUILD`;
- 19-step order;
- los 16 roots v0.2;
- ningún artefacto v0.1.

Gate final de este prompt sigue:

`CANDIDATE_PENDING_EXTERNAL_AUDIT`

`NOT_AUTHORIZATION_READY`

cuatro `NOT_AUTHORIZED / NOT_EXECUTED`.

---

# 6. PATHS PERMITIDOS

Modifica únicamente lo estrictamente necesario dentro de la candidatura v0.2, previsiblemente:

- `src/experiments/build_bm25_corrective_0b05c_v02.py`;
- `src/experiments/run_0b05c_corrective_numerical_v02.py`;
- `src/experiments/run_d1a_corrective_0b05c_v02.py`;
- `src/experiments/prepare_0b05c_corrective_numerical_gate_v02.py` si congelas schema de runtime provenance;
- `tests/test_0b05c_corrective_numerical_gate_v02.py`;
- `docs/0B05C_CORRECTIVE_NUMERICAL_GATE_V02.md`;
- JSONs contractuales bajo `outputs/audits/0b05c_corrective_numerical_gate_v0.2/` que deban regenerarse por bindings/schema.

No modificar `.gitattributes` salvo que agregues un path textual nuevo, cosa que no debería ser necesaria.

---

# 7. VALIDACIÓN OBLIGATORIA

Antes del commit:

- HEAD base de trabajo = `59dc445d8128dd71f48d26eac66c9ae8d0c21e38`;
- diff exclusivamente en paths permitidos;
- authorization record real ausente;
- runtime record real ausente;
- 16 future roots ausentes;
- ninguna métrica correctiva nueva;
- main/Plan/article/EXP11B/EXP12/v0.1 intactos.

Ejecuta:

1. suite v0.2 ampliada;
2. EV03 recovery v0.2;
3. v0.1 gate regressions;
4. D1a preexecution/runner regressions;
5. BM25 flat/hierarchical regressions;
6. suite total razonable.

Añade específicamente un **builder→evaluator metadata compatibility test real en temp**, pues ese es el defecto que las suites previas omitieron.

Después del commit, desde checkout limpio/detached del nuevo HEAD:

- `python -B -m src.experiments.run_0b05c_corrective_numerical_v02 --preflight` = PASS cerrado/read-only;
- suite v0.2 = PASS;
- future roots reales ausentes.

No ejecutar `--execute-authorized` contra el repo real.

No afirmar CI si no existe.

---

# 8. COMMIT Y PUSH

Si todo pasa:

- exactamente un commit nuevo encima de `59dc445...`;
- mensaje sugerido: `fix: close remaining 0b05c v0.2 execution contract gaps`;
- push normal solo a `codex/0b05c-corrective-numerical-gate-v02`;
- sin merge a main;
- sin force-push.

Reporta commit, parent, tree, compare vs `59dc445...` y vs `origin/main`.

---

# 9. PERSISTENCIA ADMINISTRATIVA OBLIGATORIA

Al finalizar, persiste **exactamente tu reporte final** en:

Rama:

`codex/prompts-temporary`

Archivo nuevo:

`codex_prompts_tmp/11_RESPUESTA_MICROCLOSE_GATE_RUNNER_0B05C_V02_F007_F010.md`

Reglas:

- no modifiques este prompt 11;
- no modifiques prompts/respuestas anteriores;
- commit administrativo separado con **solo** el response path;
- mensaje sugerido: `docs: persist prompt 11 gate microclose report`;
- push normal, sin force.

---

# 10. REPORTE FINAL OBLIGATORIO

Responde únicamente con secciones A–O:

### A. Preflight Git
SHAs/tree/branch exactos.

### B. F007 — metadata builder/evaluator
schema antes/después y test real de compatibilidad temp.

### C. F008 — D1a unified authorization binding
cómo se impide ejecución standalone con autorización parcial y cómo el unified runner pasa proof al step 12.

### D. F009 — runtime authorization provenance
campos congelados, runtime record y manifest contractuales.

### E. F010 — D1a aggregate integrity
validación exacta de las 17 métricas y tests negativos.

### F. Preservación F001–F006
confirmación y regresiones.

### G. Invariantes científicos
confirmación completa.

### H. Gate state
CANDIDATE_PENDING_EXTERNAL_AUDIT, NOT_AUTHORIZATION_READY, cuatro NOT_AUTHORIZED.

### I. Tests v0.2
RUN/PASS/FAIL/ERROR/SKIP, incluyendo test builder→evaluator.

### J. Regresiones
EV03 recovery, v0.1, D1a, flat/hierarchical, suite total.

### K. Postcommit detached validation
preflight/suite/roots.

### L. Aislamiento
main/Plan/article/EXP11B/EXP12/v0.1 sin cambios.

### M. Commit candidato
SHA, parent=`59dc445...`, tree, paths, ahead/behind, push.

### N. Persistencia administrativa
response path, admin commit, único archivo, PASS/FAIL.

### O. Estado científico
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

No declares integración aprobada. La auditoría externa posterior decidirá.