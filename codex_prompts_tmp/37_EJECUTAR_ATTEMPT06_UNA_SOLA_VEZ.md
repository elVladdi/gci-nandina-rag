# PROMPT 37 — EJECUTAR ATTEMPT06 UNA SOLA VEZ

## Objetivo

Ejecutar **Attempt06** de 0B-05C exactamente una vez usando la autorización ya auditada externamente, sin abrir nuevas rondas de hardening técnico y sin modificar el método experimental.

La autorización aprobada es:

- baseline integrado `main`: `e7cab327f0ef12b1e8ae21cddd01d215cd42db31`
- rama: `codex/0b05c-v05-attempt06-authorization`
- commit autorizado: `a9b06b8748316d7f3c403eaa9d55b735e12d96c3`
- parent directo: `e7cab327f0ef12b1e8ae21cddd01d215cd42db31`

La auditoría externa de la autorización es **PASS / AUTHORIZED_FOR_SINGLE_EXECUTION**.

No hagas nuevas mejoras preventivas. Solo detente ante un blocker real que impida ejecutar o comprometa datos, método o validez del resultado.

---

## 1. Precondiciones mínimas

Haz `git fetch` y verifica únicamente:

1. `origin/main == e7cab327f0ef12b1e8ae21cddd01d215cd42db31`;
2. `origin/codex/0b05c-v05-attempt06-authorization == a9b06b8748316d7f3c403eaa9d55b735e12d96c3`;
3. Plan sigue en `fe847f708d4d1ded92b5a50a38d4913bb69ed311`;
4. Article sigue en `254b1e6df736fa9938ac86a515d65b36f4d361c5`;
5. el authorization commit es un único hijo directo del baseline y contiene exactamente los cinco paths autorizados;
6. no existen previamente los 16 prospective roots v0.5;
7. working tree tracked limpio.

No vuelvas a auditar todo 35A–35F. No abras nuevas remediaciones por cuestiones marginales.

Si cualquiera de 1–7 falla: `STOP / PREEXECUTION_STATE_INVALID` sin ejecutar Attempt06.

---

## 2. Rama de ejecución

Crea o posiciona una rama nueva exactamente en el commit autorizado, sin commit intermedio:

`codex/0b05c-v05-attempt06-execution`

Antes de la invocación, `HEAD` debe ser exactamente:

`a9b06b8748316d7f3c403eaa9d55b735e12d96c3`

No integres todavía la autorización a `main`; la rama de ejecución debe partir del commit autorizado.

---

## 3. Invocación única

Usa el mismo `.venv` exacto validado en 35F/36.

Ejecuta **una sola vez**:

```text
.venv\Scripts\python.exe -B -m src.experiments.run_0b05c_corrective_numerical_v05 --execute-authorized
```

La propia invocación debe ejecutar el preflight autorizado antes de cualquier side effect y, si pasa, los 19 pasos congelados.

### Reglas estrictas

- `invocation_count = 1`;
- NO retry;
- NO resume;
- NO segunda invocación aunque el proceso falle;
- NO ejecutar por separado EV03, EV04 o D1a;
- NO ejecutar nuevamente el preflight mediante otra invocación del pipeline;
- NO borrar partial roots;
- NO reutilizar roots v0.4;
- NO cambiar código, specs, corpus, configs, EVAL, modelo o autorización durante la ejecución;
- NO instalar/actualizar dependencias;
- NO descargar modelos o datos científicos.

Puedes capturar stdout/stderr en una ubicación temporal fuera de los 16 roots gobernados. Esa captura no cuenta como una segunda ejecución.

---

## 4. Si Attempt06 falla

Detente inmediatamente.

No limpies, no corrijas, no reintentes y no reanudes.

Preserva todos los outputs parciales tal como quedaron y crea **solo después del fallo** un registro sanitizado:

`outputs/audits/0b05c_attempt06_execution_v0.5/attempt06_failclosed_record_v0.5.json`

Debe contener como mínimo:

- `attempt = Attempt06`;
- `status = FAIL_CLOSED / AUTHORIZATION_CONSUMED`;
- authorization commit;
- comando lógico ejecutado;
- `invocation_count = 1`;
- tipo de excepción / return code;
- último paso conocido si puede determinarse sin inferir;
- lista de prospective roots presentes;
- ningún path absoluto host-local;
- `retry_allowed = false`;
- `resume_allowed = false`.

Haz un único commit post-ejecución en la rama de ejecución con la evidencia/partials existentes. No modifiques gate/specs para fingir cierre.

Publica la rama y STOP.

---

## 5. Si Attempt06 completa los 19 pasos

No vuelvas a ejecutar nada científico.

Haz únicamente verificaciones read-only sobre los outputs ya producidos:

1. los 19 pasos reportaron PASS/PASS_EXACT según contrato;
2. los 16 prospective roots esperados existen conforme al ledger/manifest;
3. `execution_manifest_v0.5.json` existe y es parseable;
4. `exact_hash_ledger_v0.5.json` existe y reporta `mismatch_count = 0`;
5. unified sensitivity summary existe;
6. EV03, EV04 y D1a tienen sus outputs/metrics previstos;
7. no hay `execution_failed.json` ni estado FAILED dentro de los roots gobernados.

Crea después un registro de ejecución, fuera de los roots gobernados:

`outputs/audits/0b05c_attempt06_execution_v0.5/attempt06_execution_record_v0.5.json`

Campos mínimos:

- `attempt = Attempt06`;
- `status = COMPLETED / PENDING_EXTERNAL_RESULT_AUDIT`;
- baseline commit;
- authorization commit;
- comando lógico;
- `invocation_count = 1`;
- `pipeline_steps_expected = 19`;
- `pipeline_steps_completed = 19`;
- referencias relativas a manifest, ledger y unified summary;
- lista de los 16 roots producidos;
- `retry_performed = false`;
- `resume_performed = false`;
- sin paths absolutos.

No interpretes todavía el impacto científico como cierre definitivo y no actualices Plan ni Article.

Haz **un único commit post-ejecución** en `codex/0b05c-v05-attempt06-execution` que versione los resultados producidos y el execution record. Publica la rama.

---

## 6. Preservaciones científicas

Deben permanecer exactamente como están:

- Decision906: solo `87044110` y `87045110`;
- EVAL N=1056;
- D1a sin retraining;
- MRR@100 racional;
- MRR@200 legacy;
- contribución 101–200 racional;
- EV04 28 filas aggregate;
- EV03 recovered historical semantics;
- Topology/pipeline de 19 pasos;
- v0.4 partial roots nunca inputs.

No modificar:

- Plan Maestro;
- Article;
- EXP11B;
- EXP12.

---

## 7. Reporte obligatorio

Persistir en rama `codex/prompts-temporary`:

`codex_prompts_tmp/37_RESPUESTA_EJECUTAR_ATTEMPT06_UNA_SOLA_VEZ.md`

El reporte debe indicar factual y separadamente:

- refs de entrada;
- commit inicial autorizado;
- comando ejecutado;
- `invocation_count`;
- timestamps inicio/fin si están disponibles;
- PASS/FAIL terminal;
- paso terminal;
- roots producidos;
- commit post-ejecución y tree;
- resultados de las verificaciones read-only;
- si success: referencias exactas a EV03/EV04/D1a/unified summary/manifest/ledger;
- si failure: error factual y failclosed record;
- confirmación de no retry/no resume;
- Plan/Article sin cambios.

### Estado permitido si éxito

```text
PROMPT37 = COMPLETED
ATTEMPT06 = COMPLETED / PENDING_EXTERNAL_RESULT_AUDIT
ATTEMPT06_INVOCATIONS = 1
0B05C_METRIC_IMPACT = COMPUTED / PENDING_EXTERNAL_INTERPRETATION
0B05C_CLOSURE = NOT_YET_APPROVED
```

### Estado permitido si fallo

```text
PROMPT37 = COMPLETED_FAIL_CLOSED
ATTEMPT06 = FAIL_CLOSED / AUTHORIZATION_CONSUMED
ATTEMPT06_INVOCATIONS = 1
0B05C_METRIC_IMPACT = NOT_DETERMINED_OR_PARTIAL_ONLY
0B05C_CLOSURE = NOT_AUTHORIZED
```

Responde únicamente con el reporte final exigido.
