# CODEX — MICROCLOSE ATTEMPT04 FAIL-CLOSED Y CONSUMIR AUTORIZACIÓN 0B-05C v0.3

## 0. ROL Y OBJETIVO

Actúa exclusivamente como **EJECUTOR DEL MICROCLOSE FAIL-CLOSED DE ATTEMPT04**.

Attempt04 ya fue invocado una sola vez bajo la autorización v0.3 integrada y, según el reporte administrativo versionado del Prompt23, terminó con exit code 1 durante el control EV04 Decision885. Este bloque NO reejecuta nada. Su único objetivo científico es hacer durable en Git que:

- Attempt04 terminó `FAIL_CLOSED / SCIENTIFIC_STATE_PRESERVED`;
- la autorización v0.3 quedó consumida operativamente;
- no existe autorización automática para Attempt05;
- el diagnóstico causal fino del mismatch EV04 todavía NO está cerrado;
- los outputs parciales locales de Attempt04 no se versionan ni se usan como resultados científicos.

NO construyas v0.4.
NO autorices Attempt05.
NO ejecutes retrieval, EV03, EV04, D1a, EVAL ni el modelo.
NO interpretes impacto.
NO actualices Plan ni article.

---

# 1. BASELINE GIT OBLIGATORIO

Haz fetch y verifica antes de escribir:

- `origin/main = e3476d952bb025011ba1ac3ffeab6b51b85ffaa7`;
- tree de main = `d10ea04228d2754dc8156b0abaedfceee9fe297f`;
- parent = `8b1444aed67d322714189846f98a3169145ea3d4`;
- Plan Maestro = `fe847f708d4d1ded92b5a50a38d4913bb69ed311`;
- article = `254b1e6df736fa9938ac86a515d65b36f4d361c5`;
- Prompt23 response branch `codex/prompts-temporary` contiene:
  `codex_prompts_tmp/23_RESPUESTA_EJECUTAR_ATTEMPT04_NUMERICO_0B05C_V03.md`;
- blob Git del response Prompt23 = `f58472d09138c2c8e71f47707470d505530ba219`;
- commit administrativo que persistió el response = `358ca3c20064304bc87f92eec31e5c9f0857ee32`.

Verifica en `main`:

- gate v0.3 `APPROVED / INTEGRATED`;
- readiness `AUTHORIZATION_APPROVED / READY_FOR_SINGLE_EXECUTION`;
- cuatro autorizaciones numéricas = `AUTHORIZED`;
- `authorization_record_present=true`;
- `runtime_authorization_record_present=false`;
- `corrective_retrieval_executed=false`;
- `corrective_metrics_computed=false`;
- `attempt04 = AUTHORIZED / NOT_EXECUTED` en gate + EV03 spec + EV04 spec + D1a spec;
- authorization record v0.3 presente y baseline `8b1444aed...`.

Si cualquier identidad difiere: STOP / NO MICROCLOSE.

No borres ni limpies evidencia local/ignored de Attempt01–04.

---

# 2. EVIDENCIA QUE PUEDE REGISTRARSE

Usa como evidencia administrativa versionada únicamente el response Prompt23 indicado arriba. Clasifica explícitamente sus hechos de runtime como:

`CODEX_LOCAL_EXECUTION_REPORT_NOT_INDEPENDENTLY_VERSIONED_RUNTIME_OUTPUTS`

No eleves esos hechos a CI ni a verificación Git independiente.

Registra, como hechos REPORTADOS por Prompt23:

- command: `python -B -m src.experiments.run_0b05c_corrective_numerical_v03 --execute-authorized`;
- invocation_count = 1;
- exit_code_reported = 1;
- last_step_completed = `06_EV03_corrected_evaluation`;
- last_step_started = `07_EV04_Decision885_control_reproduction_ENRICHED_MRR`;
- exception = `src.experiments.run_d1a_corrective_0b05c_v01.ContractViolation: Mandatory control reproduction is not exact`;
- EV03 control reportado `PASS_EXACT`;
- EV04 ranking SHA reportado `fca13c411c5eff32fa73f72e6afe3527dc76c1b33477c9698e7e4da41e5ed662`;
- EV04 case-summary SHA reportado `17af79c3a2166100520cea289060c35a1d4ef1936055fb4291a42295ccc42634`;
- EV04 PASS_EXACT = false;
- D1a not started;
- runtime authorization record local reportado presente;
- manifest/ledger/unified summary no alcanzados;
- 8/16 roots locales reportados presentes;
- 17 archivos locales reportados preservados;
- no scientific commit de parciales.

IMPORTANTE: no declares todavía cuál campo concreto de métricas causó el mismatch. La clasificación causal debe quedar deliberadamente:

`EV04_DECISION885_CONTROL_REPRODUCTION_NOT_EXACT_AFTER_V03_MRR_RECOVERY / ROOT_CAUSE_FIELD_NOT_YET_ISOLATED`

El hecho estático versionado sí permite registrar que `compare_control_reproduction()` exige igualdad exacta de schema/ranking/case-summary/metrics y falla con `Mandatory control reproduction is not exact`; pero no inventes cuál subcampo falló sin una auditoría posterior específica.

---

# 3. RAMA CIENTÍFICA Y ALCANCE EXACTO

Crea desde exactamente `e3476d952bb025011ba1ac3ffeab6b51b85ffaa7`:

`codex/0b05c-attempt04-failclosed-microclose`

El candidato debe modificar exactamente cinco paths:

1. `outputs/audits/0b05c_corrective_numerical_gate_v0.3/0b05c_corrective_numerical_execution_gate_v0.3.json`
2. `outputs/audits/0b05c_corrective_numerical_gate_v0.3/ev03_numerical_execution_spec_v0.3.json`
3. `outputs/audits/0b05c_corrective_numerical_gate_v0.3/ev04_numerical_execution_spec_v0.3.json`
4. `outputs/audits/0b05c_corrective_numerical_gate_v0.3/d1a_numerical_execution_spec_v0.3.json`
5. `outputs/audits/0b05c_attempt04_failclosed_v0.3/attempt04_failure_record_v0.3.json`

No modifiques código, tests, authorization record, manifest/hash-ledger del gate, docs, v0.1/v0.2, Attempt03 failure record, Plan, article, EXP11B ni EXP12.

---

# 4. TRANSICIÓN POST-ATTEMPT04

## 4.1 Gate v0.3

Cambia únicamente:

- `authorization_readiness`:
  `AUTHORIZATION_APPROVED / READY_FOR_SINGLE_EXECUTION`
  → `ATTEMPT04_CONSUMED / REAUTHORIZATION_REQUIRED`;

- `attempt04`:
  `AUTHORIZED / NOT_EXECUTED`
  → `FAIL_CLOSED / AUTHORIZATION_CONSUMED`.

Preserva exactamente:

- `gate_status = APPROVED / INTEGRATED`;
- las cuatro autorizaciones numéricas históricas = `AUTHORIZED`;
- `authorization_record_present = true`;
- `runtime_authorization_record_present = false`;
- `corrective_retrieval_executed = false`;
- `corrective_metrics_computed = false`;
- scientific_state = NOT_DETERMINED / NOT_YET_JUSTIFIED / NOT_AUTHORIZED;
- todos los demás campos.

La autorización histórica permanece como evidencia de que Attempt04 fue permitido; la readiness consumida impide reutilización automática.

## 4.2 EV03 / EV04 / D1a specs

En cada spec cambia exclusivamente:

`attempt04 = AUTHORIZED / NOT_EXECUTED`
→ `attempt04 = FAIL_CLOSED / AUTHORIZATION_CONSUMED`.

Conserva su autorización propia = `AUTHORIZED` como evidencia histórica.
Conserva todos los flags de creación/cómputo serializados exactamente como estaban.
No cambies ningún contenido científico/técnico.

---

# 5. FAILURE RECORD v0.3

Crea:

`outputs/audits/0b05c_attempt04_failclosed_v0.3/attempt04_failure_record_v0.3.json`

Debe incluir como mínimo, con estructura estable y determinista:

```json
{
  "artifact_id": "0b05c_attempt04_failure_record_v0.3",
  "schema_version": 1,
  "attempt": "ATTEMPT04",
  "execution_authorization_commit": "e3476d952bb025011ba1ac3ffeab6b51b85ffaa7",
  "authorization_baseline_commit": "8b1444aed67d322714189846f98a3169145ea3d4",
  "status": "FAIL_CLOSED / SCIENTIFIC_STATE_PRESERVED",
  "authorization_consumed": true,
  "automatic_reuse_authorized": false,
  "attempt05_authorized": false,
  "runtime_evidence_classification": "CODEX_LOCAL_EXECUTION_REPORT_NOT_INDEPENDENTLY_VERSIONED_RUNTIME_OUTPUTS",
  "prompt23_admin_commit": "358ca3c20064304bc87f92eec31e5c9f0857ee32",
  "prompt23_response_path": "codex_prompts_tmp/23_RESPUESTA_EJECUTAR_ATTEMPT04_NUMERICO_0B05C_V03.md",
  "prompt23_response_git_blob_sha1": "f58472d09138c2c8e71f47707470d505530ba219",
  "exit_code_reported": 1,
  "last_step_completed": "06_EV03_corrected_evaluation",
  "last_step_started": "07_EV04_Decision885_control_reproduction_ENRICHED_MRR",
  "exception_reported": "src.experiments.run_d1a_corrective_0b05c_v01.ContractViolation: Mandatory control reproduction is not exact",
  "failure_class": "EV04_DECISION885_CONTROL_REPRODUCTION_NOT_EXACT_AFTER_V03_MRR_RECOVERY",
  "root_cause_field_status": "NOT_YET_ISOLATED",
  "partial_outputs": "LOCAL_PRESERVED_NOT_VERSIONED",
  "metric_impact": "NOT_DETERMINED",
  "downstream_reexecution": "NOT_YET_JUSTIFIED",
  "closure": "NOT_AUTHORIZED"
}
```

Puedes añadir campos de trazabilidad estática versionada, pero no conviertas valores locales no versionados en evidencia independiente.

Incluye bindings Git estáticos, si los registras, para:

- runner v0.3 blob `b4c7e6a596b6b6870cc487e68997dae4c1f67e1e`;
- evaluator v0.3 blob `3fb1346dcee357d7b1d2d430e3ca98c0bba1d1a0`;
- comparator legacy blob `c6f4121fe5f5f50e71e27eb4cf1e28eb8986d062`;
- frozen EV04 run_metadata blob `3cbbabd9d9446958e5a0b386f13bd32aec817fa1`.

No incluyas un supuesto campo culpable de MRR todavía.

---

# 6. VALIDACIÓN FAIL-CLOSED READ-ONLY

Sin ejecutar ningún componente numérico:

1. verifica que el candidato conserve las cuatro autorizaciones históricas `AUTHORIZED`;
2. verifica readiness `ATTEMPT04_CONSUMED / REAUTHORIZATION_REQUIRED`;
3. verifica `attempt04 = FAIL_CLOSED / AUTHORIZATION_CONSUMED` en gate y los tres specs;
4. verifica `attempt05_authorized=false` en el failure record;
5. verifica que el authorization record v0.3 no se modificó;
6. verifica que ningún output parcial v0.3 fue staged/versionado;
7. verifica que Plan/article no cambian;
8. confirma mecánicamente que `preflight_authorized()` ya no puede satisfacer el contrato de ejecución desde el candidato. Esta prueba es local/read-only y debe reportarse como tal, no CI.

No borres roots locales de Attempt04 para hacer pasar el preflight; el rechazo debe ocurrir por estado consumido antes de cualquier reutilización.

---

# 7. COMMIT Y PUSH

Haz exactamente un commit científico candidato sobre `e3476d952bb025011ba1ac3ffeab6b51b85ffaa7`.

Mensaje sugerido:

`chore: record attempt04 fail-closed and consume v0.3 authorization`

Push únicamente a:

`codex/0b05c-attempt04-failclosed-microclose`

No merge a main.
No rebase/amend/squash/cherry-pick/force-push.

Reporta:

- SHA candidato;
- parent exacto;
- tree;
- compare base→candidato;
- exactamente 5 changed paths;
- blobs de gate, tres specs y failure record.

---

# 8. PERSISTENCIA ADMINISTRATIVA

Después del push científico, persiste únicamente:

`codex_prompts_tmp/24_RESPUESTA_MICROCLOSE_ATTEMPT04_FAIL_CLOSED_CONSUMIR_AUTORIZACION_V03.md`

en `codex/prompts-temporary`, con commit response-only.

No modifiques este Prompt24 ni respuestas anteriores.
No mezcles rama administrativa con main.

---

# 9. REPORTE FINAL

Usa secciones:

### A. Preflight Git
### B. Evidencia Prompt23 y clasificación
### C. Transición post-Attempt04
### D. Failure record
### E. Validación fail-closed
### F. Aislamiento
### G. Diff/commit/push
### H. Persistencia administrativa
### I. Estado científico

Termina exactamente con:

`GROUP_2 = EN_CURSO`

`0B05C_V03_GATE_ARTIFACTS = VERSIONED / INTEGRATED`

`0B05C_V03_AUTHORIZATION = APPROVED / VERSIONED / INTEGRATED / CONSUMED_BY_ATTEMPT04`

`0B05C_ATTEMPT04 = FAIL_CLOSED / SCIENTIFIC_STATE_PRESERVED`

`0B05C_ATTEMPT04_FAILURE_RECORD = CANDIDATE_PENDING_EXTERNAL_AUDIT`

`EV04_ATTEMPT04_ROOT_CAUSE_FIELD = NOT_YET_ISOLATED`

`ATTEMPT05 = NOT_AUTHORIZED / NOT_EXECUTED`

`0B05C_METRIC_IMPACT = NOT_DETERMINED`

`DOWNSTREAM_REEXECUTION = NOT_YET_JUSTIFIED`

`0B05C_CLOSURE = NOT_AUTHORIZED`
