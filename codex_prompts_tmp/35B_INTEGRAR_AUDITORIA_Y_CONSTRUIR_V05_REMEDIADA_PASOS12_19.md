# PROMPT 35B — INTEGRAR AUDITORÍA PREAUTORIZACIÓN Y CONSTRUIR v0.5 REMEDIADA PARA PASOS 12–19

## Rol y objetivo

Actúa como **ejecutor técnico controlado**. Este bloque parte de la auditoría preautorización Prompt35A y debe hacer dos cosas, en este orden:

1. integrar exactamente el artefacto audit-only de Prompt35A ya auditado externamente;
2. construir un único candidato técnico v0.5 que cierre los cinco blockers demostrados y endurezca los riesgos residuales de los pasos 12–19.

**Este bloque NO autoriza Attempt06 y NO ejecuta Attempt06.** Tampoco reejecuta Attempt05.

El Prompt35 anterior queda supersedido. No lo ejecutes.

---

# 1. Estado exacto de entrada

Repositorio: `elVladdi/gci-nandina-rag`

Main científico actual esperado:

`812cb69a498d0da1aaf4a363b52e1a8ff3c2b9ea`

Audit-only Prompt35A aprobado para integración:

- rama: `codex/0b05c-preauthorization-risk-audit-12-19`
- commit: `c873ff1bd10f4e86c6f80f7f34a4dad1126965f1`
- parent: `812cb69a498d0da1aaf4a363b52e1a8ff3c2b9ea`
- tree: `11f7c59d66c858022c1d75282a8c77b93606c8aa`
- único path:
  `outputs/audits/0b05c_preauthorization_risk_audit_v0.4/preauthorization_risk_audit_steps12_19_v0.4.json`
- blob: `4bbb25940f5a14f88c4ed51daaa8475116facd29`
- size: `26355`

Evidencia Attempt05 preservada:

- rama `codex/0b05c-attempt05-failclosed-evidence-env-diagnosis`
- commit `5144bbdfc3b36e6172ecdd604a3e71d256ab248b`
- execution record blob `7e11eee9b30d3d72d3490c2adeb57d7a981b6642`
- stderr blob `698015f64e8d8fa4ebccf9483c662be774157b21`
- stdout blob `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391`
- diagnosis blob `52bf36e57514e728d16d01adc096c44862fb12a4`

Refs protegidas:

- Plan `fe847f708d4d1ded92b5a50a38d4913bb69ed311`
- Article `254b1e6df736fa9938ac86a515d65b36f4d361c5`

Antes de cualquier acción:

- `git fetch`;
- verifica `origin/main` exacto;
- verifica candidato Prompt35A exacto y `ahead=1 / behind=0`;
- verifica Plan/article;
- verifica working tree tracked limpio;
- verifica que Attempt05 no fue reejecutado;
- verifica que Attempt06 no existe ni está autorizado.

Si cualquiera falla: `STOP / FAIL_CLOSED`.

---

# 2. FASE A — Integrar únicamente Prompt35A

Integra en `main` exclusivamente `c873ff1bd10f4e86c6f80f7f34a4dad1126965f1` mediante `git merge --ff-only` o fast-forward equivalente.

Después verifica:

- `main == origin/main == c873ff1bd10f4e86c6f80f7f34a4dad1126965f1`;
- no merge commit adicional;
- el único cambio frente a `812cb69...` es el JSON de auditoría Prompt35A;
- Plan/article intactos.

No integres ninguna otra rama.

---

# 3. Hallazgos obligatorios a cerrar

Prompt35A demostró cinco blockers que deben quedar corregidos conjuntamente:

```text
R12-02_INTERPRETER_READINESS_NOT_GATED
R12-03_COMPLETE_MODEL_DIRECTORY_NOT_GATED
R14-01_EV03_EMPTY_RANKING_CASES_BREAK_COMPARISON
R15-02_NONFINITE_NONCONTRIBUTION_METRICS_NOT_REJECTED
R16-01_UNIFIED_SUMMARY_SCHEMA_UNDERVALIDATED
```

Además deben endurecerse, aunque no fueran blocker determinista:

- R13: integrity actual es existence-only;
- R15: persist/reload EV04 falla por depender del orden de keys dentro de objetos JSON;
- R17: serialización real debe validarse antes de write;
- R18: contrato expected/producer debe rederivarse para v0.5;
- riesgos runtime de D1a deben reducirse al máximo antes de una futura autorización.

No cierres un finding solo por cambiar un string de estado. Debe existir código, test y shadow positivo/negativo que demuestre la corrección.

---

# 4. Rama y alcance del candidato v0.5

Después de Fase A crea desde `main = c873ff1...`:

`codex/0b05c-v05-remediated-preauthorization-candidate`

La rama final debe contener **un único commit técnico/científico** con parent directo `c873ff1bd10f4e86c6f80f7f34a4dad1126965f1`.

v0.5 es recuperación técnica. Debe preservar sin cambios metodológicos:

- MRR@100 prospectivo racional de v0.4;
- MRR@200 legacy y aliases;
- contribución 101–200 racional;
- aggregate EV04 de 28 filas;
- semántica EV03 recuperada;
- Decision 906 limitada a `87044110` y `87045110`;
- D1a frozen model/config/EVAL y prohibición de retraining;
- 19-step orchestration.

No modifiques Plan, Article, EXP11B ni EXP12.

---

# 5. Cierre canónico de Attempt05 en v0.4

En el mismo candidato v0.5 materializa el estado histórico real de Attempt05.

## 5.1 Registro sanitizado

Crea:

`outputs/audits/0b05c_attempt05_failclosed_v0.4/attempt05_failclosed_record_v0.4.json`

Debe referenciar por branch/commit/blob la evidencia `5144bbd...` y registrar:

- failure class `MISSING_RUNTIME_PYTHON_DEPENDENCY`;
- terminal error exacto `ModuleNotFoundError: No module named 'sentence_transformers'`;
- last completed step reportado 11;
- last started step reportado 12;
- invocation/retry/resume como **CODEX execution-record evidence**, no observación independiente de Git;
- `ATTEMPT05_AUTHORIZATION = OPERATIONALLY_CONSUMED`;
- `ATTEMPT05_RETRY = FORBIDDEN`;
- `ATTEMPT06 = NOT_AUTHORIZED / NOT_EXECUTED`;
- `0B05C_METRIC_IMPACT = NOT_DETERMINED`;
- `0B05C_CLOSURE = NOT_AUTHORIZED`.

No copies raw stderr/stdout ni rutas absolutas host-locales a main.

Incluye corrección explícita de provenance CRLF/Git al menos para `requirements.txt`:

- Git blob `19273fcbb593fcb089c79dfab7acf9d8076e44bc`
- canonical Git bytes `80`
- canonical Git blob SHA-256 `698fcd824a8ff840f5deb53e6a8dcda007014ee5108b89190bf4f8d312512724`
- Prompt34 local checkout CRLF bytes `89`
- Prompt34 local CRLF SHA-256 `5d063a971db0a2d88826f4dd2a6239ae482bdbf1554fe468b0b8b7918d5fb50b`
- etiqueta del segundo: `LOCAL_CHECKOUT_CRLF_BYTES`.

## 5.2 Estados v0.4

Modifica únicamente estados históricos necesarios en:

- `0b05c_corrective_numerical_execution_gate_v0.4.json`
- `ev03_numerical_execution_spec_v0.4.json`
- `ev04_numerical_execution_spec_v0.4.json`
- `d1a_numerical_execution_spec_v0.4.json`

Contrato:

- gate `attempt05 = FAIL_CLOSED / AUTHORIZATION_CONSUMED`;
- gate `authorization_readiness = ATTEMPT05_CONSUMED / REAUTHORIZATION_REQUIRED`;
- `gate_status` permanece `APPROVED / INTEGRATED`;
- flags `*_NUMERICAL_EXECUTION = AUTHORIZED` permanecen como registro histórico de autorización consumida;
- authorization record v0.4 no se modifica;
- specs: `attempt05 = FAIL_CLOSED / AUTHORIZATION_CONSUMED`;
- no inventar retrieval/metrics como completadas.

---

# 6. Roots v0.5 frescos

Todos los 16 roots futuros deben ser nuevos y no colisionar con v0.4.

Usa sufijo inequívoco `v0.5` para todos los roots de Attempt06.

Debe existir y probarse la invariante:

`V04_PARTIAL_ROOTS = NEVER_INPUT / NEVER_REUSED / NEVER_CLEANED_BY_V05`

No copies ni uses como inputs científicos los partial roots de Attempt05.

---

# 7. R12 — Environment readiness gate obligatorio

Implementa una frontera explícita, por ejemplo:

`preauthorization_environment_preflight(root, interpreter=None)`

Debe poder ejecutarse **antes de que exista autorización v0.5** y debe volver a ejecutarse desde el futuro `preflight_authorized()` antes de cualquier side effect.

## 7.1 Intérprete

Si `interpreter` es `None`, usa `sys.executable`.

El environment contract debe bindear el intérprete que pasó Prompt35A mediante atributos sanitizados, nunca ruta absoluta:

- Python `3.10.11`;
- executable SHA-256 `b2c836c52cdf063180b9ee76f67ac42946101b79ac457f3494035a67c090d961`;
- `numpy 2.2.6`;
- `sentence_transformers 5.5.1`;
- `torch 2.12.0+cpu`;
- `tqdm 4.68.2`.

Registra por separado la evidencia histórica disponible en Git:

- `outputs/training/text2trade_mnrl_v0.2/training_metadata.json` prueba Python `3.10.11` y torch `2.12.0+cpu` para el entrenamiento D1a;
- no declares una versión histórica de `sentence_transformers` si no existe evidencia versionada.

El binding de las versiones actuales significa `TESTED_EXECUTION_ENVIRONMENT`, no `HISTORICAL_PROVENANCE` para campos no documentados históricamente.

Probe real obligatorio con el mismo `sys.executable`:

- imports `numpy`, `sentence_transformers`, `torch`, `tqdm`;
- registra además versiones de transitivos críticos usados por SentenceTransformer cuando estén disponibles (`transformers`, `tokenizers`, `safetensors`, `huggingface_hub`);
- import directo de builder D1a;
- import directo de evaluator D1a.

`hnswlib` no es blocker mientras el path permanezca `hnsw=false` y exact brute-force.

## 7.2 Directorio completo del modelo

No basta `model.safetensors`.

Verifica exactamente los 9 archivos gobernados por:

`data/processed/indexes/text2trade_mnrl_nandina8_v0.2/text2trade_mnrl_nandina8_v02_run_metadata.json`

Debe exigirse path relativo, tamaño y SHA-256 exactos. Si falta uno o cambia uno: environment preflight FAIL.

El directorio puede ser preparado localmente en el execution checkout antes de autorización, desde una copia local ya existente, pero:

- no descargar nada;
- no modificar el modelo fuente;
- no commitear/pushear el modelo;
- verificar todos los hashes después de copiar;
- no almacenar rutas absolutas en artefactos públicos.

## 7.3 Smoke offline

Con el mismo intérprete y mismo directorio:

- `HF_HUB_OFFLINE=1`;
- `TRANSFORMERS_OFFLINE=1`;
- CPU;
- `max_seq_length=128`;
- 32 strings sintéticos;
- batch 32;
- normalized embeddings.

Exige:

- load PASS;
- `(32,384)`;
- `float32`;
- todos finitos;
- normas dentro de `8 * eps(float32)`.

## 7.4 Reproducción de estabilidad histórica opcional-fuerte

Intenta localizar **sin búsqueda ilimitada** el índice D1a histórico local ya existente gobernado por el run metadata. Si están disponibles `vectors.npy`, docstore e id_map y sus hashes coinciden con el manifest histórico, ejecuta un replay read-only de los 21 `vector_index` de:

`data/processed/indexes/text2trade_mnrl_nandina8_v0.2/vector_integrity_sample_v0.2.csv`

Reconstruye esos 21 embeddings con el intérprete/modelo candidato y compáralos contra los vectores históricos almacenados usando el mismo criterio histórico de `8 * eps(float32)` para cosine y max absolute difference.

- Si los artefactos históricos locales están disponibles y el replay falla: **BLOCKER**.
- Si no están disponibles: registra `OPTIONAL_HISTORICAL_VECTOR_REPLAY_NOT_AVAILABLE`; no inventes PASS.
- No publiques los vectores ni textos.

Este control debe distinguir `ENVIRONMENT_PARITY_EVIDENCE` de resultado científico nuevo.

## 7.5 Recursos

Reprobe disk/RAM en cada preauthorization environment preflight. Conserva un margen derivado de footprints observados, no un número arbitrario. Si el host cae por debajo del margen razonado: FAIL antes de autorización.

---

# 8. R14 — Comparator EV03 con ranking vacío contractual

Corrige el comparator sin cambiar retrieval.

Hecho congelado que debe respetarse:

- EV03 tiene 1056 case summaries;
- frozen metrics registran `cases_with_retrieval = 1046` y `zero_retrieval_cases = 10`;
- `_candidate_rows()` produce cero filas cuando `hits=[]`.

Por tanto un case_id sin candidate rows es válido **solo** cuando el case summary correspondiente declara coherentemente:

- `retrieved_count == 0`;
- `rank_ref == 0`;
- top1 code/doc/score vacíos según schema;
- no candidate rows para ese case_id.

Contrato v0.5:

- missing candidate group + summary `retrieved_count=0` => ranking efectivo vacío válido `()`;
- missing candidate group + `retrieved_count>0` => FAIL;
- candidate rows presentes + `retrieved_count=0` => FAIL;
- candidate row count debe coincidir con `retrieved_count` cuando sea aplicable;
- ranks presentes deben ser contiguos `1..N`;
- EV04 mantiene unicidad de códigos.

Prueba obligatoria sobre frozen EV03 original-vs-original:

- 1056 comparison rows;
- exactamente 10 casos con ranking vacío válido;
- no se altera retrieval ni ningún rank;
- rank convention `0=NOT_FOUND/EMPTY` según contrato.

Controles negativos específicos para falsos vacíos.

No modifiques el evaluator histórico v0.2 ni v0.4. Implementa una frontera v0.5 nueva.

---

# 9. R15 — Finitud numérica y persist/reload

Para todo aggregate EV03/EV04:

- cada numerator, denominator y value debe ser numeric no-bool y `math.isfinite(float(value))`;
- denominadores deben ser enteros positivos donde el contrato así lo exige;
- NaN e Infinity deben fallar para **cualquier** métrica, no solo contribution.

No dependas del orden de keys dentro de un objeto JSON. La semántica requerida es:

- field **set** exacto por fila;
- tipos exactos/aceptados;
- **orden de filas por nombre de métrica** exacto.

El round-trip `write JSON -> reload -> validate` debe PASS con contenido equivalente aunque el writer ordene keys.

Debe seguir fallando ante missing/extra field, missing/extra metric, reordered metric, denominator mismatch, NaN/Inf.

Preserva 92 keys / 27 metric-table rows / 28 aggregate rows EV04 y contribution como tercera fila.

---

# 10. R13 — Integrity hardening

El step 13 v0.5 no puede ser solo `is_file()`.

Después de productores 2–12 debe validar al menos:

- existencia de outputs contractuales EV03/EV04/D1a relevantes;
- archivos legibles y no truncados;
- case summary EV03/EV04: 1056 case IDs únicos;
- coherencia candidate rows vs `retrieved_count`, incluyendo 10 empty rankings válidos EV03 si corresponde;
- schemas esperados;
- métricas cargables y finitas;
- D1a contractual outputs exigidos por su adapter;
- hashes de snapshot runtime calculados read-only para poder detectar modificación posterior antes del ledger.

No compares hashes futuros contra valores inventados. La finalidad es integridad interna y read-after-write.

Añade negativos: truncado, duplicate case_id, malformed schema, nonfinite metric y missing file.

---

# 11. R16 — Unified summary estricto

La función v0.5 debe rechazar:

- D1a ausente;
- D1a wrong type;
- D1a mapping vacío;
- D1a status != PASS;
- D1a references incompletas;
- EV03/EV04 payload ausente o malformed;
- EV03/EV04 status != PASS;
- métricas aggregate con cardinalidad/nombres/orden incorrectos.

Debe aceptar únicamente:

- EV03 aggregate contractual válido de 17 filas;
- EV04 aggregate contractual válido de 28 filas;
- D1a summary ya validado por `_d1a_summary_reference` con sus cuatro referencias contractuales.

Prueba positive y todos los negativos anteriores.

---

# 12. R17 — Manifest hardening

Antes de escribir el manifest real:

- valida schema completo en memoria;
- ejecuta `json.dumps(..., allow_nan=False)` o equivalente fail-closed;
- exige 19-step order exacto;
- autorización/provenance completa;
- no referencia v0.4 partial roots;
- path nuevo/no overwrite.

Test round-trip persist/reload y negativos de NaN, key faltante y path preexistente.

---

# 13. R18 — Ledger v0.5

Rederiva de manera independiente:

- `EXPECTED_SET` desde gate/specs v0.5;
- `PRODUCER_SET` desde todos los productores success-path pasos 1–17.

Deben ser exactamente iguales antes de considerar el candidato listo.

No asumas que seguirá siendo 47: reporta la cardinalidad v0.5 realmente derivada. Si cambia por nuevos artefactos runtime contractuales, documenta y justifica cada cambio.

El ledger debe:

- detectar missing y unexpected;
- no incluir `execution_failed.json` en success path;
- excluir únicamente su propio self path cuando corresponda;
- calcular hash/size de bytes realmente existentes;
- comparar, si se capturó snapshot en step13, que archivos ya existentes entonces no hayan cambiado inesperadamente.

Prueba exact/remove-one/add-one/collision.

---

# 14. R19 — Final state

Preserva los 19 pasos.

Tests sintéticos:

- 18 previos PASS + final PASS => PASS;
- cualquier previo FAIL => FAIL_CLOSED;
- missing/reordered operation => FAIL_CLOSED;
- final antes de 18 => FAIL_CLOSED.

No cambies la orquestación científica solo para hacer pasar tests.

---

# 15. Full preauthorization shadow v0.5

Antes de publicar el candidato ejecuta un shadow integral sin retrieval científico:

1. environment preflight con el intérprete candidato;
2. model manifest completo;
3. synthetic model smoke;
4. optional historical 21-vector replay si artefactos locales disponibles;
5. input/patch/config shadow;
6. EV03 original-vs-original con 10 empty rankings;
7. EV04 frozen structural shadow;
8. aggregate positive y NaN/Inf negatives;
9. unified-summary positive y malformed negatives;
10. manifest round-trip;
11. ledger expected-vs-producer + placeholder negatives;
12. 19-step synthetic pipeline.

El máximo estado permitido:

`V05_CANDIDATE = BUILT / TESTED_CODEX_LOCAL / PENDING_EXTERNAL_AUDIT`

Nunca `AUTHORIZED`.

---

# 16. Código/artefactos esperados

Puedes diseñar la mínima estructura necesaria, pero se espera como mínimo una frontera equivalente a:

- `src/experiments/evaluate_normative_bm25_corrective_0b05c_v05.py`
- `src/experiments/prepare_0b05c_corrective_numerical_gate_v05.py`
- `src/experiments/run_d1a_corrective_0b05c_v05.py`
- `src/experiments/run_0b05c_corrective_numerical_v05.py`

Tests mínimos separados por riesgo:

- environment/D1a readiness;
- comparator + aggregate + integrity;
- summary + manifest + ledger + orchestration.

No modifiques componentes históricos/v0.1–v0.4 para implementar lógica nueva, salvo los cuatro campos de estado v0.4 autorizados en §5.2.

Gate directory:

`outputs/audits/0b05c_corrective_numerical_gate_v0.5/`

Mínimo:

- `0b05c_corrective_numerical_execution_gate_v0.5.json`
- `ev03_numerical_execution_spec_v0.5.json`
- `ev04_numerical_execution_spec_v0.5.json`
- `d1a_numerical_execution_spec_v0.5.json`
- `0b05c_corrective_numerical_gate_manifest_v0.5.json`
- `0b05c_corrective_numerical_gate_hash_ledger_v0.5.json`

No crear authorization record v0.5.

Añade:

`outputs/audits/0b05c_v05_preauthorization_readiness/preauthorization_readiness_v0.5.json`

que contenga closure matrix de R12/R13/R14/R15/R16/R17/R18/R19, evidencias locales clasificadas correctamente y riesgos residuales.

Estados obligatorios en todo v0.5:

- `gate_status = CANDIDATE_READY_FOR_EXTERNAL_AUDIT / NOT_AUTHORIZED`
- `authorization_readiness = NOT_AUTHORIZED`
- EV03/EV04/D1a/UNIFIED = `NOT_AUTHORIZED`
- `ATTEMPT06 = NOT_AUTHORIZED / NOT_EXECUTED`
- `Attempt05 = FAIL_CLOSED / AUTHORIZATION_CONSUMED` como antecedente histórico.

---

# 17. Riesgos residuales que NO deben falsamente cerrarse

Incluso con todos los tests PASS deben permanecer explícitos como residuales:

- full encode real de 7644 documentos;
- full query encode/evaluación de 1056 casos;
- pico runtime de memoria/CPU/I/O;
- hashes concretos de outputs futuros;
- fallos extraordinarios del host después de side effects.

Mitigaciones obligatorias:

- environment/capacity preflight nuevamente **antes de integrar autorización**;
- mismo intérprete fingerprinted;
- roots v0.5 ausentes;
- una sola invocación futura;
- no retry/resume;
- preservación fail-closed de evidencia.

No declares `RISK_ZERO` ni garantía de éxito.

---

# 18. Prohibiciones absolutas

NO:

- autorizar Attempt06;
- crear authorization record v0.5;
- ejecutar Attempt06;
- reejecutar Attempt05;
- instalar/actualizar/desinstalar paquetes;
- entrenar o modificar modelo;
- ejecutar full corpus embeddings D1a;
- ejecutar EVAL científico real;
- ejecutar EV03/EV04 retrieval real salvo lecturas/shadows de frozen artifacts expresamente permitidos;
- usar v0.4 partial roots como inputs;
- borrar/limpiar v0.4 partial roots;
- modificar Plan/article/EXP11B/EXP12;
- publicar modelos, vectores históricos o partial outputs sensibles.

---

# 19. Pruebas y clasificación probatoria

Ejecuta tests focalizados y regresiones razonables sin retrieval real.

Clasificación obligatoria:

`CODEX_LOCAL_TEST_EXECUTION / NOT_INDEPENDENT_GITHUB_CI`

No presentes tests locales como CI independiente.

Reporta comandos exactos, counts PASS/SKIP/FAIL y duración si está disponible.

---

# 20. Publicación científica

Antes de commit:

- diff completo contra `c873ff1...`;
- ningún path fuera de alcance;
- no authorization record v0.5;
- ninguna raíz runtime v0.5 producida por ejecución científica;
- no v0.4 partial output copiado;
- no rutas absolutas en artefactos públicos;
- working tree tracked limpio tras commit.

Publica únicamente:

`codex/0b05c-v05-remediated-preauthorization-candidate`

No integres este candidato a main.

---

# 21. Persistencia administrativa

Después del trabajo científico:

1. vuelve a `codex/prompts-temporary`;
2. `git fetch` antes de escribir;
3. no rebase/amend/force;
4. crea exclusivamente:

`codex_prompts_tmp/35B_RESPUESTA_INTEGRAR_AUDITORIA_Y_CONSTRUIR_V05_REMEDIADA_PASOS12_19.md`

El reporte debe incluir:

- integración exacta de `c873ff1...`;
- nuevo main;
- branch/commit/tree/parent v0.5;
- lista exacta de paths/blobs;
- closure de los cinco blockers;
- hardening R13/R15 reload/R17/R18;
- fingerprint del environment candidato sanitizado;
- resultado del optional 21-vector replay o razón factual de no disponibilidad;
- resultados completos de tests/shadow;
- riesgos residuales explícitos;
- `ATTEMPT06 = NOT_AUTHORIZED / NOT_EXECUTED`;
- `0B05C_METRIC_IMPACT = NOT_DETERMINED`;
- `0B05C_CLOSURE = NOT_AUTHORIZED`.

Responde únicamente con ese reporte final.
