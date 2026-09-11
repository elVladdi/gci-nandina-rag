# PROMPT 35D — CERRAR BINDINGS REALES + ENTORNO EJECUTABLE + VALIDACIÓN D1a v0.5

## Rol y objetivo

Actúa como **ejecutor técnico controlado preautorización**. Este bloque corrige en una sola pasada los hallazgos de la auditoría externa de Prompt35C y debe dejar un candidato v0.5 limpio y realmente preparado para una futura autorización, **sin autorizar ni ejecutar Attempt06**.

El candidato Prompt35C:

- rama `codex/0b05c-v05-remediated-preauthorization-candidate-v2`
- commit `6511e6e72c5f77978699a290c8449c3c6736a71c`

queda **REJECTED_BY_EXTERNAL_AUDIT / NOT_INTEGRATED**. Puede usarse solo como fuente de trabajo; no debe ser parent ni integrarse.

No ejecutes Prompt35B/35C de nuevo.

---

# 1. Estado exacto de entrada

Repositorio: `elVladdi/gci-nandina-rag`

Main científico esperado:

`c873ff1bd10f4e86c6f80f7f34a4dad1126965f1`

Refs protegidas:

- Plan `fe847f708d4d1ded92b5a50a38d4913bb69ed311`
- Article `254b1e6df736fa9938ac86a515d65b36f4d361c5`

Evidencia administrativa Prompt35C parte del commit de prompt:

`210b7daf919d05524c10e21b1db72f94432775f3`

Antes de trabajar:

1. `git fetch`;
2. verifica `origin/main == c873ff1...`;
3. verifica que `6511e6e...` existe, parent directo `c873ff1...`, pero NO está integrado;
4. verifica Plan/Article exactos;
5. verifica que no exista authorization record v0.5 en `main`;
6. verifica `ATTEMPT06 = NOT_AUTHORIZED / NOT_EXECUTED`;
7. verifica que no se haya reejecutado Attempt05;
8. no uses partial roots v0.4 como inputs científicos.

Si falla cualquiera: `STOP / FAIL_CLOSED`.

---

# 2. Rama corregida

Crea desde `main = c873ff1...`:

`codex/0b05c-v05-remediated-preauthorization-candidate-v3`

Puedes recuperar el contenido útil de `6511e6e...` al working tree/index sin introducirlo como ancestro.

El candidato final debe ser **un único commit** con parent directo `c873ff1...` y ningún merge.

No modifiques Plan, Article, EXP11B ni EXP12.

---

# 3. Hallazgos externos a cerrar

Debes cerrar conjuntamente:

```text
F35D-01_AUTHORIZATION_CURRENT_DEPENDENCIES_NOT_BOUND
F35D-02_RUNTIME_PROJECT_DEPENDENCY_CLOSURE_INCOMPLETE
F35D-03_D1A_SUMMARY_REFERENCE_VALIDATION_REGRESSION
F35D-04_CURRENT_EXECUTION_ENVIRONMENT_NOT_AVAILABLE
F35D-05_ENVIRONMENT_TRANSITIVE_STACK_NOT_FULLY_BOUND
```

No cierres ningún finding solo por cambiar strings. Requiere código + tests + shadow/probe efectivo.

---

# 4. F35D-01 — La autorización debe congelar el commit ACTUAL, no solo el baseline

La auditoría externa confirmó que Prompt35C hace:

`validate_dependency_bindings(..., baseline)`

pero no demuestra que los mismos source/data bindings sigan idénticos en el commit de autorización. Una autorización podría modificar código fuera de gate/specs y conservar intactos los metadatos del baseline.

## Contrato obligatorio

La futura autorización v0.5 debe ser **exactamente un commit hijo directo** del baseline auditado.

Exige:

1. `parent(authorization_commit) == authorization_baseline_commit`;
2. diff de paths baseline→authorization **exactamente**:
   - `outputs/audits/0b05c_corrective_numerical_gate_v0.5/0b05c_corrective_numerical_execution_gate_v0.5.json`
   - `outputs/audits/0b05c_corrective_numerical_gate_v0.5/ev03_numerical_execution_spec_v0.5.json`
   - `outputs/audits/0b05c_corrective_numerical_gate_v0.5/ev04_numerical_execution_spec_v0.5.json`
   - `outputs/audits/0b05c_corrective_numerical_gate_v0.5/d1a_numerical_execution_spec_v0.5.json`
   - `outputs/audits/0b05c_corrective_numerical_gate_v0.5/0b05c_numerical_authorization_record_v0.5.json`
3. los primeros cuatro son modificaciones y el authorization record es alta nueva;
4. ningún otro path puede cambiar;
5. valida los dependency bindings del baseline contra el baseline **y contra el authorization commit**;
6. para cada dependencia, path/blob SHA-1/canonical SHA-256/size deben ser idénticos baseline↔authorization;
7. filesystem tracked bytes deben corresponder al authorization commit; tracked tree limpio;
8. conserva además la immutable projection gate/specs ya implementada.

Añade un negativo real en un repositorio temporal: baseline válido → commit de autorización que cambia además un source Python manteniendo metadata intacta => **FAIL_CLOSED**.

El negativo Prompt35C que solo mutaba `candidate_source_bindings` dentro del gate NO es suficiente.

---

# 5. F35D-02 — Cierre automático de dependencias Python del path real

El binding manual de Prompt35C es incompleto. La auditoría confirmó imports runtime que no aparecen en `VERSIONED_DEPENDENCY_PATHS`, entre ellos como mínimo:

- `src/experiments/prepare_0b05c_corrective_numerical_gate_v01.py`
- `src/experiments/prepare_0b05c_corrective_numerical_gate_v02.py`
- `src/experiments/prepare_0b05c_corrective_numerical_gate_v03.py`
- `src/experiments/evaluate_normative_bm25_flat_data_aduanas_v02.py`
- `src/evaluation/metrics.py`
- `src/utils/paths.py`

No te limites a añadir manualmente esos seis.

## 5.1 Import closure determinista

Implementa una derivación read-only del **project-local Python import closure** a partir de los entrypoints reales de Attempt06, al menos:

- `src/experiments/run_0b05c_corrective_numerical_v05.py`
- `src/experiments/run_d1a_corrective_0b05c_v05.py`
- `src/experiments/build_text2trade_mnrl_index_v02.py`
- `src/experiments/evaluate_text2trade_mnrl_data_aduanas_v02.py`

Incluye recursivamente imports absolutos/relativos que resuelvan dentro de `src/`. Excluye stdlib y paquetes externos. Puede usarse AST estático; no ejecutes retrieval científico.

El gate debe:

- almacenar/bindear todo el closure local real mediante Git blob SHA-1 + canonical SHA-256 + size;
- rederivarlo en preflight y exigir igualdad exacta del path set;
- fallar si falta o aparece una dependencia local nueva no binded;
- validar los bindings tanto en baseline como en authorization commit.

Pruebas:

- closure positivo;
- elimina cada uno de los seis paths mínimos anteriores del binding => FAIL;
- introduce en fixture un import local nuevo no binded => FAIL.

## 5.2 Dependencias de archivos versionados leídos en runtime

Audita también inputs versionados leídos para producir outputs contractuales, aunque no sean imports Python.

Incluye explícitamente los archivos que `evaluate_text2trade_mnrl_data_aduanas_v02.py:baseline_values()` lee:

- `outputs/evaluation/historical_retrieval_data_aduanas_clase87_v0.2/historical_metrics.json`
- `outputs/evaluation/normative_bm25_flat_data_aduanas_clase87_v0.2/normative_metrics.json`
- `outputs/evaluation/normative_bm25_hierarchical_data_aduanas_clase87_v0.2/normative_hierarchical_metrics.json`
- `outputs/evaluation/text2trade_dense_data_aduanas_clase87_v0.2/run_metadata.json`

Mantén los frozen corpus/config/EVAL/control/index ya gobernados. Si descubres otros inputs versionados efectivamente leídos por el success path 1–17, incorpóralos y documenta por qué.

---

# 6. F35D-03 — Restaurar y fortalecer validación de contenidos D1a

Prompt35C sustituyó la referencia D1a por `d1a_runner.d1a_summary_reference()`, pero esa función solo comprueba presencia/tamaño/hash de los cuatro outputs. No debe ser más débil que la validación previa de `common._d1a_summary_reference()`.

Implementa una validación v0.5 fuerte compatible con filenames v0.5.

Antes de producir `d1a_summary = PASS`, exige como mínimo:

## Aggregate comparison

- JSON object válido;
- exactamente 17 métricas contractuales;
- nombres y orden exactos;
- field set exacto por fila;
- numerator/value/delta finitos y numeric no-bool;
- denominator entero positivo y coherente original/corrected;
- ningún NaN/Inf.

## Case-level comparison

- JSONL legible y no vacío;
- exactamente 1056 case IDs únicos;
- schema contractual requerido;
- `nandina_ref` no vacío;
- ranks enteros no negativos;
- sin filas duplicadas;
- cardinalidad exacta.

## D1a execution manifest

- `status == PASS`;
- `runner_version == v0.5`;
- `runner_outputs` exactamente iguales al spec v0.5;
- no referencia output actual v0.1/v0.4.

## D1a internal hash ledger

- CSV legible;
- path set exactamente igual a `hash_ledger_contract.included_paths`;
- ningún duplicado;
- SHA-256 de 64 hex;
- size > 0;
- recomputa hash/size de cada path y exige exactitud;
- self-path excluido exactamente.

Solo después crea las cuatro referencias `{path, sha256, size_bytes}` para el unified summary.

Negativos mínimos: aggregate métrica faltante/NaN, case duplicate o 1055 rows, manifest runner output stale, ledger missing/extra/hash incorrecto.

---

# 7. F35D-04/F35D-05 — El entorno ejecutable actual es un blocker y debe quedar estabilizado

Prompt35C registró:

`FINGERPRINTED_INTERPRETER_NOT_AVAILABLE`

y el runtime disponible carece de `sentence_transformers`.

No presentes el environment actual como PASS mientras esto siga así.

## 7.1 Separación de estados

El readiness público debe distinguir:

- `LAST_KNOWN_TESTED_ENVIRONMENT` — evidencia histórica CODEX-local de Prompt35B;
- `CURRENT_EXECUTION_ENVIRONMENT_READINESS` — probe realizado en este bloque.

Si el entorno actual no pasa, `CURRENT_EXECUTION_ENVIRONMENT_READINESS = BLOCKED`.

## 7.2 Preparación aislada permitida

En este bloque **sí se permite** preparar un entorno Python aislado exclusivamente para Attempt06, con estas restricciones:

- nunca instalar globalmente;
- no modificar el modelo;
- no entrenar;
- no ejecutar full D1a, EVAL científico ni retrieval;
- no commitear el venv;
- no publicar rutas absolutas;
- no sustituir silenciosamente versiones críticas.

Usa Python **3.10.11** preexistente en el host. Si no existe, STOP; no descargues/instales otra versión de Python.

Crea un venv local no versionado, preferentemente `.venv-0b05c-v05`, y exclúyelo solo localmente (`.git/info/exclude` o equivalente), sin modificar `.gitignore` salvo necesidad justificada y auditada.

Para el stack crítico exige exactamente:

- numpy `2.2.6`
- sentence-transformers `5.5.1`
- torch `2.12.0+cpu`
- tqdm `4.68.2`
- transformers `5.12.1`
- tokenizers `0.22.2`
- safetensors `0.8.0`
- huggingface_hub `1.19.0`

Puedes instalar paquetes **solo dentro del venv**. Usa cache local cuando exista; si necesitas índice de paquetes, registra que se usó para preparar el entorno, pero no descargues modelos ni datos científicos. Si una versión crítica exacta no puede instalarse, STOP; no la reemplaces por otra.

Instala además únicamente las dependencias externas necesarias para importar el closure real del pipeline. Registra sus versiones finales exactas.

## 7.3 Contrato ambiental completo

El gate v0.5 debe bindear al menos:

- Python version;
- implementation/architecture/platform relevante;
- executable SHA-256 observado;
- versiones exactas de las 8 dependencias críticas anteriores;
- versiones de cualquier otro paquete externo requerido por el import closure;
- 9-file model manifest exacto;
- offline synthetic smoke;
- capacity margins.

Repite imports reales de todos los entrypoints/project modules bajo ese venv.

Repite:

- model load offline;
- 32 strings sintéticos;
- shape `(32,384)`;
- float32;
- finitud;
- normas dentro de `8*eps(float32)`.

Si los artefactos históricos `vectors.npy`/docstore/id_map continúan disponibles y gobernados, el replay de 21 vectores debe PASS. Si estaban disponibles al comienzo y dejan de estarlo, STOP. Si no están disponibles desde el comienzo, registra factual y no inventes PASS.

Al final del bloque ejecuta un **reprobe fresco** con el mismo venv. Para publicar el candidato v3 se exige:

`CURRENT_EXECUTION_ENVIRONMENT_READINESS = PASS`

Si no se logra, **NO publiques candidato científico v3**. Persiste solo el reporte administrativo con `STOP / ENVIRONMENT_REMEDIATION_FAILED` y diagnóstico.

## 7.4 No depender solo de 4 paquetes

No mantengas un contrato que compruebe únicamente numpy/sentence_transformers/torch/tqdm mientras los transitivos críticos registrados puedan derivar. La comparación preauthorization debe validar el stack externo exacto gobernado por el nuevo environment contract.

---

# 8. Authorization preflight final

Después de las correcciones, el futuro `preflight_authorized()` debe hacer, antes de cualquier write:

1. tracked tree clean;
2. authorization record presente y schema exacto;
3. baseline == parent directo del authorization commit;
4. exact five-path authorization diff;
5. baseline bindings exactos;
6. current authorization-commit dependency bindings exactos e iguales al baseline;
7. gate/spec filesystem == authorization commit;
8. immutable projection PASS;
9. 16 roots v0.5 ausentes;
10. current import closure exacto;
11. current environment contract exacto;
12. 9-file model manifest exacto;
13. offline smoke PASS;
14. capacity PASS;
15. historical vector replay según disponibilidad contractual;
16. solo entonces `AUTHORIZED_PREFLIGHT_ONLY`.

Shadow positivo completo sin side effects y negativos de cada familia.

---

# 9. Preservaciones metodológicas

No cambies:

- MRR@100 racional prospectivo v0.4;
- MRR@200 legacy;
- contribución 101–200 racional;
- aggregate EV04 28 filas;
- EV03 recovered historical token semantics;
- Decision906 exactamente dos códigos `87044110`, `87045110`;
- modelo D1a frozen y sin retraining;
- EVAL N=1056;
- 19 pasos;
- política `V04_PARTIAL_ROOTS = NEVER_INPUT / NEVER_REUSED / NEVER_CLEANED_BY_V05`.

---

# 10. Prohibiciones científicas

NO:

- integres el candidato 35C;
- modifiques `main`;
- autorices Attempt06;
- crees authorization record v0.5 real;
- ejecutes Attempt06;
- reejecutes Attempt05;
- ejecutes full encode de 7644 documentos;
- ejecutes las 1056 queries reales D1a;
- ejecutes EV03/EV04 corrected retrieval real;
- uses partial roots v0.4 como inputs;
- borres partial roots v0.4;
- entrenes/modifiques modelo;
- modifiques Plan/Article/EXP11B/EXP12.

Preparación de venv + imports + synthetic smoke + optional historical 21-vector replay son preauthorization diagnostics, no ejecución científica.

---

# 11. Tests obligatorios

Añade/ajusta tests para demostrar:

1. authorization direct-parent + exact five-path diff;
2. actual source file changed in authorization commit => FAIL;
3. import closure exacto y completeness negatives;
4. runtime data dependency set exacto;
5. D1a aggregate/case/manifest/ledger strong validation;
6. current environment full-stack contract;
7. stale identities 0;
8. physical runtime ledger exact/missing/extra/snapshot;
9. manifest provenance;
10. 19-step synthetic orchestration.

Ejecuta suite focalizada v0.5 y regresión razonable. Clasifica siempre:

`CODEX_LOCAL_TEST_EXECUTION / NOT_INDEPENDENT_GITHUB_CI`.

No ocultes FAIL/ERROR históricos.

---

# 12. Candidato y artefactos

Preserva la estructura v0.5 de 35C, corrigiéndola. Puede añadirse un test nuevo o un artifact de environment contract si es necesario, pero mantén alcance mínimo.

Gate/readiness deben indicar:

- `gate_status = CANDIDATE_READY_FOR_EXTERNAL_AUDIT / NOT_AUTHORIZED`;
- `authorization_readiness = NOT_AUTHORIZED`;
- `ATTEMPT06 = NOT_AUTHORIZED / NOT_EXECUTED`;
- `CURRENT_EXECUTION_ENVIRONMENT_READINESS = PASS` para poder publicar;
- ningún authorization record v0.5.

Antes de commit:

- scan de rutas absolutas;
- stale identities;
- diff contra `c873ff1...`;
- no path fuera de alcance;
- no runtime roots v0.5 científicos;
- no partial output sensible publicado;
- tracked worktree limpio.

Publica únicamente:

`codex/0b05c-v05-remediated-preauthorization-candidate-v3`

No lo integres a main.

---

# 13. Estado máximo permitido

```text
V05_CANDIDATE = BUILT / CURRENT_ENVIRONMENT_VERIFIED_CODEX_LOCAL / PENDING_EXTERNAL_AUDIT
ATTEMPT05 = FAIL_CLOSED / AUTHORIZATION_CONSUMED
ATTEMPT06 = NOT_AUTHORIZED / NOT_EXECUTED
0B05C_METRIC_IMPACT = NOT_DETERMINED
0B05C_CLOSURE = NOT_AUTHORIZED
```

No declares `READY_FOR_ATTEMPT06`, `AUTHORIZED` ni `RISK_ZERO`.

---

# 14. Persistencia administrativa

Después del trabajo:

1. vuelve a `codex/prompts-temporary`;
2. `git fetch`;
3. no amend/rebase/force;
4. crea exclusivamente:

`codex_prompts_tmp/35D_RESPUESTA_CERRAR_BINDINGS_ENTORNO_Y_VALIDACION_D1A_V05.md`

El reporte debe incluir:

- branch/commit/tree/parent del candidato v3 o STOP factual;
- diff exacto paths/blobs;
- cierre de F35D-01..05;
- import closure completo y count;
- lista de nuevos runtime data dependencies añadidos;
- prueba de exact five-path authorization diff shadow;
- prueba de actual source-drift-in-auth-commit => FAIL_CLOSED;
- validación D1a fuerte;
- environment creation/reuse procedure;
- full governed external package versions;
- current final reprobe;
- model 9-file manifest;
- smoke/replay;
- tests completos;
- riesgos residuales;
- `ATTEMPT06 = NOT_AUTHORIZED / NOT_EXECUTED`;
- `0B05C_METRIC_IMPACT = NOT_DETERMINED`;
- `0B05C_CLOSURE = NOT_AUTHORIZED`.

Responde únicamente con ese reporte final.