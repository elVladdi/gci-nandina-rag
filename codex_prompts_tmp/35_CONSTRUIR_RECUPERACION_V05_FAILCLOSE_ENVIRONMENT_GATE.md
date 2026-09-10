# PROMPT 35 — CONSTRUIR RECUPERACIÓN v0.5: FAIL-CLOSE ATTEMPT05 + ENVIRONMENT GATE PREAUTORIZACIÓN

## Rol

Actúa como **ejecutor técnico controlado**. Este bloque consolida en una sola construcción todo lo necesario después de Attempt05 para evitar nuevos ciclos por fallos previsibles de entorno:

1. materializar canónicamente el cierre fail-closed de Attempt05 sin publicar los outputs runtime potencialmente sensibles;
2. corregir la trazabilidad de hashes locales CRLF frente a blobs Git canónicos;
3. construir un candidato técnico v0.5 con roots completamente nuevos;
4. incorporar un **environment gate preautorización** que pruebe dependencias, módulos reales D1a y carga/encode mínimo del modelo antes de que una futura autorización pueda integrarse;
5. ejecutar tests y shadow validations únicamente read-only/sintéticos.

Este bloque **NO autoriza Attempt06** y **NO ejecuta retrieval, EV03 real, EV04 real, D1a real, EVAL ni inferencia científica del modelo**. El único encode permitido es el smoke test sintético de entorno definido expresamente más abajo.

---

## 1. Estado obligatorio de entrada

Repositorio: `elVladdi/gci-nandina-rag`

Main esperado:

`812cb69a498d0da1aaf4a363b52e1a8ff3c2b9ea`

Este main contiene v0.4 y la autorización Attempt05 ya integrada.

Evidencia audit-only de Attempt05 ya publicada:

- rama: `codex/0b05c-attempt05-failclosed-evidence-env-diagnosis`
- commit: `5144bbdfc3b36e6172ecdd604a3e71d256ab248b`
- parent: `812cb69a498d0da1aaf4a363b52e1a8ff3c2b9ea`
- tree: `dc8eb941ab16b6442495d1dca3e1a518f51c9050`
- exactamente 4 paths audit-only.

Evidencia de ejecución preservada:

- execution record blob `7e11eee9b30d3d72d3490c2adeb57d7a981b6642`, 13064 bytes;
- stderr blob `698015f64e8d8fa4ebccf9483c662be774157b21`, 2705 bytes;
- stdout blob `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391`, 0 bytes;
- diagnosis blob `52bf36e57514e728d16d01adc096c44862fb12a4`, 9962 bytes.

El stderr versionado demuestra el error terminal:

`ModuleNotFoundError: No module named 'sentence_transformers'`

Plan esperado:

`fe847f708d4d1ded92b5a50a38d4913bb69ed311`

Article esperado:

`254b1e6df736fa9938ac86a515d65b36f4d361c5`

Antes de editar verifica:

- `origin/main` exacto en `812cb69...`;
- rama audit-only exacta en `5144bbd...`;
- Plan/article en los heads indicados;
- Attempt05 no ha sido reejecutado;
- Attempt06 no existe ni está autorizado;
- no se han integrado a main los 26 outputs runtime parciales de Attempt05;
- working tree tracked limpio.

Si falla cualquiera: `STOP / FAIL_CLOSED`.

---

# 2. Tratamiento de la evidencia Prompt34

## 2.1 No integrar el candidato audit-only tal cual

La rama `5144bbd...` es evidencia válida, pero **NO debe fast-forwardearse a main tal cual** porque:

1. `attempt05_stderr.txt` y el diagnóstico contienen rutas absolutas host-locales;
2. el diagnóstico registra hashes/tamaños del working tree Windows con CRLF como si fueran identidades de archivos inspeccionados, mientras que para trazabilidad Git deben distinguirse explícitamente de los bytes canónicos del blob.

Conserva `5144bbd...` intacto como rama de evidencia. No la reescribas ni la borres.

## 2.2 Crear un fail-close canónico y sanitizado

En el candidato nuevo crea:

`outputs/audits/0b05c_attempt05_failclosed_v0.4/attempt05_failclosed_record_v0.4.json`

Debe contener como mínimo:

- `artifact_id` y `schema_version`;
- authorization commit `812cb69...`;
- evidence branch/commit `5144bbd...`;
- blobs exactos de execution record/stdout/stderr/diagnosis;
- SHA-256 y tamaños declarados del execution record/stdout/stderr;
- error terminal exacto `ModuleNotFoundError: No module named 'sentence_transformers'`;
- `failure_class = MISSING_RUNTIME_PYTHON_DEPENDENCY`;
- last completed step reportado = 11;
- last started step reportado = 12;
- `invocation_count = 1`, `retry_count = 0`, `resume_count = 0` **clasificados como evidencia del execution record de CODEX, no como observación independiente de Git**;
- `ATTEMPT05_AUTHORIZATION = OPERATIONALLY_CONSUMED`;
- `ATTEMPT05_RETRY = FORBIDDEN`;
- `ATTEMPT06 = NOT_AUTHORIZED / NOT_EXECUTED`;
- `0B05C_METRIC_IMPACT = NOT_DETERMINED`;
- `0B05C_CLOSURE = NOT_AUTHORIZED`;
- nota explícita de que raw stderr permanece solo en la rama audit-only y no se integra para evitar promover metadata host-local a main.

No copies a este candidato los 26 outputs runtime parciales ni el raw stderr/stdout.

## 2.3 Corregir provenance de hashes de texto

El diagnóstico Prompt34 registró bytes del checkout CRLF. En el fail-close record o en un pequeño bloque `hash_provenance_correction` registra ambos niveles y no los confundas:

### `requirements.txt`

- Git blob SHA-1: `19273fcbb593fcb089c79dfab7acf9d8076e44bc`
- canonical Git blob bytes: 80
- canonical Git blob SHA-256: `698fcd824a8ff840f5deb53e6a8dcda007014ee5108b89190bf4f8d312512724`
- Prompt34 local CRLF checkout bytes: 89
- Prompt34 local CRLF SHA-256: `5d063a971db0a2d88826f4dd2a6239ae482bdbf1554fe468b0b8b7918d5fb50b`

Clasifica el segundo como `LOCAL_CHECKOUT_CRLF_BYTES`, no como canonical Git identity.

Para los módulos fuente inspeccionados, deriva de Git las identidades canónicas y, si conservas las identidades locales de Prompt34, etiquétalas igualmente como working-tree bytes.

---

# 3. Materializar el estado fail-closed de v0.4

Usa como precedente semántico el cierre de Attempt04 en v0.3.

Modifica exclusivamente los campos de estado necesarios en los cuatro artefactos v0.4 ya autorizados:

1. `0b05c_corrective_numerical_execution_gate_v0.4.json`
2. `ev03_numerical_execution_spec_v0.4.json`
3. `ev04_numerical_execution_spec_v0.4.json`
4. `d1a_numerical_execution_spec_v0.4.json`

Contrato esperado:

- gate `attempt05 = FAIL_CLOSED / AUTHORIZATION_CONSUMED`;
- gate `authorization_readiness = ATTEMPT05_CONSUMED / REAUTHORIZATION_REQUIRED`;
- gate `gate_status` puede permanecer `APPROVED / INTEGRATED`, siguiendo el precedente v0.3;
- las cuatro flags `*_NUMERICAL_EXECUTION` permanecen `AUTHORIZED` como registro histórico de la autorización consumida;
- `authorization_record_present = true` permanece;
- retrieval/metrics/runtime-record flags no deben inventarse como completadas;
- cada spec cambia únicamente su `attempt05` a `FAIL_CLOSED / AUTHORIZATION_CONSUMED`, manteniendo su propia flag `AUTHORIZED` como estado histórico de la autorización consumida;
- no alteres contenido científico/técnico MRR, corpus, ranking, métricas, modelo ni bindings.

No modifiques el authorization record v0.4.

---

# 4. Construir candidato técnico v0.5

Crea una rama nueva desde `main = 812cb69...`:

`codex/0b05c-v05-environment-gated-recovery-candidate`

La rama final debe contener **un único commit científico/técnico** con parent directo `812cb69...`.

v0.5 es una recuperación técnica, no un cambio metodológico. Debe preservar exactamente:

- contrato MRR@100 prospectivo racional de v0.4;
- MRR@200 como legacy alias;
- contribución 101–200 racional;
- aggregate EV04 de 28 filas;
- EV03 semantics recuperadas;
- D1a frozen model/config/eval inputs;
- 19-step orchestration;
- ninguna modificación de objetivos, métricas científicas o corpus normativo.

La única diferencia conceptual permitida es:

`FRESH_ATTEMPT_ROOTS + ENVIRONMENT_READINESS_GATE`.

## 4.1 Roots nuevos

Todos los 16 roots prospectivos deben ser nuevos y terminar en `v0.5` o una denominación inequívocamente Attempt06/v0.5. Ningún root v0.4 parcial puede ser input, output o fallback.

Debe existir una aserción explícita:

`V04_PARTIAL_ROOTS = NEVER_INPUT / NEVER_REUSED / NEVER_CLEANED_BY_V05`.

## 4.2 Reutilización de componentes

Reutiliza sin cambios cuando sea científicamente correcto:

- builder BM25 recuperado;
- evaluator MRR v0.4;
- D1a model/config/base evaluator/builder;
- comparators v0.4.

Crea wrappers/adapters v0.5 únicamente donde sea necesario para root/spec/gate/environment binding. Evita duplicación gratuita.

Como mínimo se espera una nueva frontera v0.5 equivalente a:

- `prepare_0b05c_corrective_numerical_gate_v05.py`
- `run_0b05c_corrective_numerical_v05.py`
- `run_d1a_corrective_0b05c_v05.py`

más tests y artefactos gate/spec v0.5 correspondientes.

No crees todavía authorization record v0.5.

`ATTEMPT06 = NOT_AUTHORIZED / NOT_EXECUTED` en todo el bundle.

---

# 5. Environment gate preautorización — obligatorio

Este es el cambio principal de v0.5.

Implementa una función read-only explícita, por ejemplo:

`preauthorization_environment_preflight(root, interpreter=None)`

que pueda ejecutarse **ANTES de integrar cualquier autorización** y que vuelva a ejecutarse desde `preflight_authorized()` antes de cualquier side effect.

## 5.1 Identidad del intérprete

Debe usar el mismo intérprete que ejecutará el runner. Si `interpreter` no se proporciona, usa `sys.executable`.

Registra/verifica:

- Python executable existente;
- `sys.version` del intérprete objetivo;
- SHA-256 del ejecutable Python o una identidad binaria equivalente estable;
- plataforma;
- comando real utilizado para los probes.

No hardcodees `C:\Users\...` ni otra ruta host-local en artefactos científicos versionados.

## 5.2 Import probes

Usando subprocess con **ese mismo intérprete**, exige PASS al menos para:

- `numpy`;
- `sentence_transformers`;
- `torch`;
- `tqdm`;
- cualquier otra dependencia realmente importada por los módulos D1a transitivos que el código determine necesaria.

No exijas `hnswlib` solo porque aparece en requirements si puedes demostrar estáticamente que D1a v0.2 no lo usa (`index.hnsw = false`). Si decides exigirlo, justifica su necesidad real.

Además exige PASS a imports directos:

- `src.experiments.build_text2trade_mnrl_index_v02`;
- `src.experiments.evaluate_text2trade_mnrl_data_aduanas_v02`.

Un `find_spec()` no es suficiente: deben ser imports reales en subprocess, sin llamar a `main()`.

## 5.3 Frozen model y config

Antes de autorización verifica:

- modelo `models/text2trade_mnrl_v0.2/model.safetensors` existente;
- tamaño `470637416`;
- SHA-256 `ef9b92b2fb0239e46c0d81e403f00b3255d3822dfa25e0ce354d03828f7a8c87`;
- config `src/configs/text2trade_mnrl_v0.2.json` exacta;
- `training.device = cpu`;
- `max_sequence_length = 128`;
- `index.normalize_embeddings = true`.

## 5.4 Smoke test sintético del modelo

Para evitar consumir otra autorización por un fallo que solo aparezca al cargar el modelo, el environment gate debe poder ejecutar un smoke test **no científico** con el frozen model:

- cargar `SentenceTransformer` desde el model dir frozen;
- usar CPU;
- fijar `max_seq_length = 128`;
- encode exactamente una cadena sintética constante, por ejemplo `"0B05C_ENVIRONMENT_READINESS_PROBE"`;
- `convert_to_numpy=True`;
- `normalize_embeddings=True`;
- exigir shape `(1, 384)`;
- exigir valores finitos;
- no comparar ese vector con métricas experimentales;
- no usar EVAL, corpus, descripciones comerciales ni datos científicos;
- no persistir el vector.

Clasificación:

`NON_SCIENTIFIC_ENVIRONMENT_SMOKE_TEST / READ_ONLY_MODEL_LOAD`.

Este smoke test está permitido en Prompt35 **solo si existe ya un intérprete local que supera los imports**. No instales paquetes para forzarlo en este bloque.

## 5.5 Fresh-root gate

El environment preflight debe verificar también que los 16 roots v0.5 estén ausentes. Los roots v0.4 pueden existir localmente y no deben causar error, siempre que no sean usados.

---

# 6. Descubrimiento read-only de intérpretes existentes

Para evitar instalar innecesariamente, realiza una búsqueda acotada y read-only de intérpretes Python existentes:

1. `sys.executable` actual;
2. `py -0p` si `py` existe;
3. `where.exe python` / `where.exe py` en Windows;
4. `.venv/Scripts/python.exe` o `venv/Scripts/python.exe` dentro del proyecto si existen;
5. no hagas barrido amplio del disco.

Para cada intérprete candidato, ejecuta el environment import probe mínimo. No instales nada.

Si alguno pasa completamente, registra en el **reporte administrativo**, no en código hardcodeado:

`READY_INTERPRETER_FOUND = true`

con versión y executable hash. Si ninguno pasa:

`READY_INTERPRETER_FOUND = false / ENVIRONMENT_INSTALLATION_REQUIRED_BEFORE_ATTEMPT06_AUTHORIZATION`

Esto **no invalida el candidato técnico v0.5**; solo impide autorizar Attempt06 hasta preparar el entorno.

---

# 7. Environment readiness record futuro

Define en el bundle v0.5 el contrato para un futuro:

`outputs/audits/0b05c_corrective_numerical_gate_v0.5/environment_readiness_record_v0.5.json`

pero **NO lo crees como PASS real en este bloque** salvo como fixture sintético dentro de tests temporales.

El futuro record debe contener, sin rutas locales sensibles:

- artifact/schema id;
- v0.5 candidate/baseline commit;
- Python version;
- Python executable SHA-256;
- plataforma;
- required import names y versiones observadas;
- direct D1a module imports PASS;
- frozen model identity PASS;
- smoke test PASS y shape;
- all v0.5 roots absent;
- timestamp;
- `environment_ready = true`.

La futura autorización Attempt06 debe exigir que este record PASS exista y esté vinculado; `preflight_authorized()` debe repetir las comprobaciones críticas antes de side effects.

---

# 8. Pre-mortem y tests obligatorios

Antes de publicar el candidato ejecuta una sola auditoría pre-mortem que cubra como mínimo:

1. v0.4 fail-close state no puede volver a autorizar Attempt05;
2. Attempt05 authorization consumida;
3. v0.4 partial roots nunca se usan;
4. 16 roots v0.5 son nuevos y disjuntos;
5. no authorization record v0.5;
6. Attempt06 NOT_AUTHORIZED;
7. MRR@100/200/contribution sin drift;
8. EV04 aggregate 28 rows;
9. D1a frozen model/config unchanged;
10. environment import failure bloquea antes de side effect;
11. direct-module import failure bloquea;
12. model missing/hash mismatch bloquea;
13. smoke-load failure bloquea;
14. smoke shape/nonfinite failure bloquea;
15. future root existente bloquea;
16. positive synthetic environment path llega hasta `AUTHORIZED_PREFLIGHT_ONLY` sin ejecutar operaciones;
17. authorization transition futura solo puede cambiar campos permitidos;
18. no hardcoded host-local absolute paths en bundle v0.5;
19. canonical Git hashes se distinguen de local checkout bytes;
20. Plan/article/EXP11B/EXP12 intactos.

Añade tests específicos para los puntos 10–16. Usa mocks/fixtures para el positive synthetic path; no instales dependencias.

Los tests pueden ejecutar imports reales read-only del entorno actual, pero el resultado debe clasificarse:

`CODEX_LOCAL_ENVIRONMENT_PROBE / NOT_INDEPENDENT_GITHUB_CI`.

No ejecutes suites históricas completas si sus blobs no cambian; usa regresiones focalizadas.

---

# 9. Artefactos v0.5

Crea un bundle autocontenido bajo:

`outputs/audits/0b05c_corrective_numerical_gate_v0.5/`

con gate/specs/manifest/hash ledger necesarios y un shadow/preexecution audit v0.5.

Todos deben declarar:

- `V05_BUILD = CANDIDATE_PENDING_EXTERNAL_AUDIT` o equivalente no autorizado;
- `ATTEMPT06 = NOT_AUTHORIZED / NOT_EXECUTED`;
- `ENVIRONMENT_READINESS = REQUIRED_BEFORE_AUTHORIZATION`;
- `0B05C_METRIC_IMPACT = NOT_DETERMINED`;
- `0B05C_CLOSURE = NOT_AUTHORIZED`.

No declares PASS de environment real si el intérprete actual no lo cumple.

---

# 10. Alcance prohibido

No:

- instalar paquetes;
- modificar `requirements.txt` en este bloque;
- borrar/limpiar/reutilizar roots v0.4;
- ejecutar Attempt05 otra vez;
- crear autorización Attempt06;
- ejecutar Attempt06;
- ejecutar retrieval/EV03/EV04/D1a/EVAL científicos;
- usar datos EVAL para smoke test;
- modificar Plan/article/EXP11B/EXP12;
- cambiar el contrato científico MRR v0.4.

---

# 11. Commit y publicación

Produce un único commit científico/técnico en:

`codex/0b05c-v05-environment-gated-recovery-candidate`

con parent directo:

`812cb69a498d0da1aaf4a363b52e1a8ff3c2b9ea`

No integres a main.

La rama audit-only `5144bbd...` debe permanecer intacta y separada.

---

# 12. Reporte obligatorio

Persiste en `codex/prompts-temporary`:

`codex_prompts_tmp/35_RESPUESTA_CONSTRUIR_RECUPERACION_V05_FAILCLOSE_ENVIRONMENT_GATE.md`

Incluye obligatoriamente:

- refs protegidas;
- auditoría de la evidencia `5144bbd...` usada como fuente;
- branch/commit/tree/parent final v0.5;
- lista exacta de paths y blobs;
- failclose record v0.4 y su blob;
- cambios exactos de estado v0.4;
- explicación de hash canonical Git vs local CRLF;
- roots v0.5 exactos;
- environment gate implementado;
- lista exacta de imports requeridos y justificación;
- discovery de intérpretes existentes;
- `READY_INTERPRETER_FOUND`;
- smoke test sintético: ejecutado/PASS o no ejecutable por entorno no ready;
- tests y shadow results con clasificación correcta;
- ausencia de authorization record v0.5 real;
- `ATTEMPT05_RETRY = FORBIDDEN`;
- `ATTEMPT06 = NOT_AUTHORIZED / NOT_EXECUTED`;
- `0B05C_METRIC_IMPACT = NOT_DETERMINED`;
- `0B05C_CLOSURE = NOT_AUTHORIZED`;
- main sin cambios.

Responde únicamente con el reporte final exigido.
