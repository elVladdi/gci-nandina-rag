# PROMPT111 — INTEGRAR CIERRE G6-F03 Y CERRAR FORMALMENTE GRUPO 6

## 0. Rol y objetivo

Actúa como **CODEX ejecutor reproducible** del proyecto `elVladdi/gci-nandina-rag`.

Debes ejecutar exclusivamente el **cierre técnico-administrativo final de G6-F03 y del Grupo 6**, después de que la IA Experimental auditó independientemente el candidato materializado de captions/cierre y emitió `PASS`.

Esta ejecución sí está autorizada para:

1. integrar por fast-forward el candidato G6-F03 aprobado;
2. normalizar únicamente los campos administrativos necesarios para convertir los dos artefactos de candidato en artefactos finales aprobados;
3. registrar `G6-F03 = CLOSED / APPROVED / INTEGRATED_TO_MAIN`;
4. registrar `GROUP6 = CLOSED / APPROVED`;
5. reconciliar el registro de fichas y el Plan Maestro;
6. dejar `G7-F01 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED`.

No ejecutes G7-F01. No modifiques tesis ni artículo. No cambies una sola afirmación científica de los captions.

---

## 1. Auditoría externa vinculante

La IA Experimental establece:

```text
PROMPT110_EXTERNAL_AUDIT = PASS
SCIENTIFIC_CORRECTION_REQUIRED = false
CAPTION_CORRECTION_REQUIRED = false
MATERIALIZATION_CORRECTION_REQUIRED = false
APPROVED_G6_F03_CANDIDATE = b5eb500ee3215fd4fcdb5a8bde20a00b2f1c17b6
APPROVED_PARENT = 3390878a62ce32ba0e6f4fce69a394c903f5ff11
APPROVED_CANDIDATE_BRANCH = figures/g6-f03-caption-closure-v01
APPROVED_CHANGED_PATH_COUNT = 2
APPROVED_CAPTION_REGISTRY_BLOB = 10e96b0399bfe45bad90c1b84a61c368d0f9716b
APPROVED_GROUP6_CLOSURE_BLOB = 0b35084e2b10397b329c42907593c17b40c55d1c
FIGURE_COUNT = 3
CAPTION_COUNT = 3
SCIENTIFIC_DATA_CHANGE_COUNT = 0
NEW_INFERENCE_COUNT = 0
NEW_CI_COUNT = 0
NEW_P_VALUE_COUNT = 0
EXP12_REOPENED = false
GROUP6_FORMAL_CLOSURE_AUTHORIZED = true
G7_F01_ACTIVATION_AUTHORIZED = false
```

La auditoría confirmó que el candidato es exactamente un commit ahead / cero behind de `main`, contiene exclusivamente dos paths nuevos y materializa de forma exacta los contenidos científico-visuales aprobados por FIG009 salvo las normalizaciones administrativas autorizadas por Prompt110.

---

## 2. Refs obligatorios al iniciar

Debes observar exactamente:

```text
origin/main = 3390878a62ce32ba0e6f4fce69a394c903f5ff11
origin/figures/g6-f03-caption-closure-v01 = b5eb500ee3215fd4fcdb5a8bde20a00b2f1c17b6
origin/docs/fichas-grupos-3-8 = 1037ff158512224c2a07f69643f7238776efe8b5
origin/docs/plan-maestro-temporal-2026-08-31 = b74b96d0163807007e4579d86450dd235125b30f
```

El reporte Prompt110 vigente es:

```text
codex_prompts_tmp/110_RESPUESTA_MATERIALIZAR_CANDIDATO_G6_F03_CAPTIONS_Y_CIERRE.md
response commit on codex/prompts-temporary = 10dbde22172de4132ffc8558509cb468d8d6f009
```

STOP si cualquiera de los cuatro refs anteriores cambió antes de iniciar.

---

## 3. Workspace canónico

Trabaja exclusivamente en:

```text
C:\Users\Vladimir\OneDrive\Documentos\Maestría UNMSM\LLM_RGA_NANDINA
```

Registra antes de cualquier cambio:

```powershell
cd "C:\Users\Vladimir\OneDrive\Documentos\Maestría UNMSM\LLM_RGA_NANDINA"
git rev-parse --show-toplevel
git remote get-url origin
git status --porcelain
git worktree list
git fetch origin
git rev-parse origin/main
git rev-parse origin/figures/g6-f03-caption-closure-v01
git rev-parse origin/docs/fichas-grupos-3-8
git rev-parse origin/docs/plan-maestro-temporal-2026-08-31
git rev-parse origin/codex/prompts-temporary
```

STOP si:

- workspace u origin no son canónicos;
- existen modificaciones tracked preexistentes no explicadas;
- no puedes preservar los untracked históricos conocidos sin tocarlos.

---

## 4. Revalidación mínima del candidato aprobado

Antes de integrar confirma:

```text
BASE = 3390878a62ce32ba0e6f4fce69a394c903f5ff11
HEAD = b5eb500ee3215fd4fcdb5a8bde20a00b2f1c17b6
STATUS = ahead
AHEAD_BY = 1
BEHIND_BY = 0
PARENT_OF_HEAD = BASE
CHANGED_PATH_COUNT = 2
```

Los únicos paths deben ser:

```text
docs/figures/group6/g6_caption_registry_v0.1.md
outputs/audits/group6_closure_v0.1.json
```

Verifica además:

```text
caption registry blob = 10e96b0399bfe45bad90c1b84a61c368d0f9716b
group6 closure blob = 0b35084e2b10397b329c42907593c17b40c55d1c
```

Si cualquiera no coincide, STOP sin integrar.

---

## 5. Etapa A — integración exacta del candidato

Integra exclusivamente mediante fast-forward:

```text
MAIN_FROM = 3390878a62ce32ba0e6f4fce69a394c903f5ff11
MAIN_TO_CANDIDATE = b5eb500ee3215fd4fcdb5a8bde20a00b2f1c17b6
METHOD = FAST_FORWARD_ONLY
```

No uses cherry-pick, squash, merge commit, rebase ni force-push.

Después de esta etapa:

```text
origin/main = b5eb500ee3215fd4fcdb5a8bde20a00b2f1c17b6
```

No alteres aún el texto científico.

---

## 6. Etapa B — normalización administrativa final en main

Sobre `main` ya integrado, crea **un único commit administrativo de cierre** que modifique exclusivamente:

```text
docs/figures/group6/g6_caption_registry_v0.1.md
outputs/audits/group6_closure_v0.1.json
```

### 6.1 Caption registry

Está prohibido modificar los tres `final_caption`, títulos de trabajo, roles, destinos, población, incertidumbre, limitaciones, source paths o controles de accesibilidad.

Cambia únicamente los cuatro estados administrativos:

```text
top-level:
status: CANDIDATE_PENDING_EXTERNAL_AUDIT
→ status: APPROVED

G6-FIG-01:
status: CANDIDATE_PENDING_EXTERNAL_AUDIT
→ status: APPROVED

G6-FIG-02:
status: CANDIDATE_PENDING_EXTERNAL_AUDIT
→ status: APPROVED

G6-FIG-03:
status: CANDIDATE_PENDING_EXTERNAL_AUDIT
→ status: APPROVED
```

Fuera de esas cuatro sustituciones, el archivo debe ser textualmente idéntico al candidato aprobado.

### 6.2 Closure JSON

Preserva todos los bindings, counts y checks científicos. Cambia exclusivamente estos campos administrativos:

```json
"artifact_id": "GROUP6_CLOSURE_V0.1",
"status": "APPROVED",
"g6_f03_candidate_status": "CLOSED / APPROVED / INTEGRATED_TO_MAIN",
"group6_closure_candidate": false,
"group6_closed": true,
"external_audit": "PASS",
"g7_f01_authorized": false
```

Mantén sin cambio:

```text
recommended_group6_state_after_external_pass = CLOSED / APPROVED
recommended_next_ficha_after_external_pass = G7-F01
scientific_consistency = PASS
accessibility = PASS
caption_self_containment = PASS
canonical_table_consistency = PASS
numeric_consistency_with_group5 = PASS
claim_consistency_with_group4 = PASS
claim_scope_consistency = PASS
uncertainty_consistency_with_group3 = PASS
forbidden_claim_count = 0
scientific_data_change_count = 0
new_scientific_metric_count = 0
new_inference_count = 0
new_ci_count = 0
new_p_value_count = 0
exp12_reopened = false
article_modified = false
thesis_modified = false
```

No agregues nuevas claves científicas ni nuevas conclusiones.

Después del commit registra:

```text
GROUP6_CLOSURE_COMMIT = <nuevo commit de main>
MAIN_FINAL = <mismo commit>
```

El diff `b5eb500... → MAIN_FINAL` debe contener exactamente 2 paths y únicamente las normalizaciones administrativas indicadas.

---

## 7. Etapa C — cierre en registro de fichas

Sobre:

```text
origin/docs/fichas-grupos-3-8 = 1037ff158512224c2a07f69643f7238776efe8b5
```

modifica exclusivamente:

```text
docs/fichas/grupos_3_8/04_REGISTRO_ESTADO_FICHAS.md
```

Añade un bloque final con al menos:

```text
FICHA = G6-F03
PREVIOUS_STATE = CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
PROMPT110_RESPONSE_COMMIT = 10dbde22172de4132ffc8558509cb468d8d6f009
CANDIDATE_COMMIT = b5eb500ee3215fd4fcdb5a8bde20a00b2f1c17b6
EXTERNAL_AUDIT = PASS
SCIENTIFIC_CORRECTION_REQUIRED = false
CAPTION_CORRECTION_REQUIRED = false
MATERIALIZATION_CORRECTION_REQUIRED = false
INTEGRATION_METHOD = FAST_FORWARD_ONLY
CANDIDATE_INTEGRATION_COMMIT = b5eb500ee3215fd4fcdb5a8bde20a00b2f1c17b6
GROUP6_CLOSURE_COMMIT = <MAIN_FINAL>
FINAL_G6_F03_STATE = CLOSED / APPROVED / INTEGRATED_TO_MAIN
GROUP6 = CLOSED / APPROVED
G7_F01 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
G7_F01_AUTHORIZED = false
GROUP7 = NOT_STARTED
```

No actives G7-F01.

---

## 8. Etapa D — reconciliación del Plan Maestro

Sobre:

```text
origin/docs/plan-maestro-temporal-2026-08-31 = b74b96d0163807007e4579d86450dd235125b30f
```

modifica exclusivamente:

```text
docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md
```

### 8.1 Tabla de estado

Actualiza Grupo 6 para expresar como mínimo:

```text
6. Figuras y visualizaciones = CLOSED / APPROVED
G6-F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G6-F02 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G6-F03 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
GROUP6_CLOSURE_COMMIT = <MAIN_FINAL>
```

Actualiza Grupo 7 únicamente a:

```text
7. Redacción científica = ELIGIBLE / NOT_AUTHORIZED
G7-F01 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
```

Grupo 8 permanece pendiente/no autorizado.

### 8.2 Entrada de trazabilidad

Añade al final una entrada fechada de cierre de Grupo 6 que consigne como mínimo:

- candidato G6-F03 aprobado `b5eb500ee3215fd4fcdb5a8bde20a00b2f1c17b6`;
- integración fast-forward;
- `GROUP6_CLOSURE_COMMIT = <MAIN_FINAL>`;
- exactamente 3 figuras y 3 captions aprobados;
- G6-F01/F02/F03 cerradas/aprobadas/integradas;
- `GROUP6 = CLOSED / APPROVED`;
- `G7-F01 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED`;
- cero cambio científico, cero nueva inferencia/CI/p-value;
- tesis y artículo no modificados;
- EXP12 no reabierto.

No reescribas ninguna otra sección del Plan.

---

## 9. Validación final obligatoria

Confirma:

```text
main contains approved G6-F03 candidate = true
caption_count = 3
figure_count = 3
caption_text_changed_after_external_audit = false
scientific_binding_changed = false
scientific_data_change_count = 0
new_inference_count = 0
new_ci_count = 0
new_p_value_count = 0
EXP12_REOPENED = false
ARTICLE_MODIFIED = false
THESIS_MODIFIED = false
G6_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G6_F02 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G6_F03 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
GROUP6 = CLOSED / APPROVED
G7_F01 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
G7_F01_AUTHORIZED = false
```

Comprueba que el caption registry y closure JSON finales difieren del candidato aprobado exclusivamente en los campos administrativos autorizados en §6.

---

## 10. Prohibiciones

No:

- cambies ningún `final_caption`;
- edites SVG/PNG o scripts;
- recalcules ledger;
- cambies registry G6-F01;
- cambies tablas G5 o análisis G3/G4;
- generes ciencia nueva;
- cambies métricas, CI, denominadores o claims;
- reabras EXP12;
- modifiques tesis o artículo;
- actives o ejecutes G7-F01;
- redactes contenido de tesis o artículo;
- autorices G8;
- uses cherry-pick/squash/rebase/merge commit/force-push para integrar el candidato.

---

## 11. Respuesta oficial

Publica únicamente:

```text
codex_prompts_tmp/111_RESPUESTA_INTEGRAR_CIERRE_G6_F03_Y_CERRAR_GRUPO6.md
```

sobre:

```text
codex/prompts-temporary
```

Incluye como mínimo:

```text
PROMPT111_EXECUTION
WORKSPACE_CONTRACT
MAIN_PRE_INTEGRATION
APPROVED_CANDIDATE
LINEAGE_CHECK
CANDIDATE_CHANGED_PATH_COUNT
CANDIDATE_INTEGRATION_METHOD
MAIN_AFTER_CANDIDATE_FF
GROUP6_CLOSURE_COMMIT
MAIN_FINAL
FINAL_ADMIN_DIFF_PATH_COUNT
FINAL_CAPTION_TEXT_MATCH_APPROVED_CANDIDATE
FINAL_CLOSURE_JSON_SCIENTIFIC_FIELDS_MATCH
FICHAS_BASE
FICHAS_FINAL
PLAN_BASE
PLAN_FINAL
G6_F01_FINAL_STATE
G6_F02_FINAL_STATE
G6_F03_FINAL_STATE
GROUP6_FINAL_STATE
G7_F01_FINAL_STATE
G7_F01_AUTHORIZED
SCIENTIFIC_DATA_CHANGE_COUNT
NEW_INFERENCE_COUNT
NEW_CI_COUNT
NEW_P_VALUE_COUNT
ARTICLE_MODIFIED
THESIS_MODIFIED
EXP12_REOPENED
EXTERNAL_AUDIT_OF_PROMPT111
```

Terminal esperado:

```text
PROMPT111_EXECUTION = COMPLETE
G6_F03_FINAL_STATE = CLOSED / APPROVED / INTEGRATED_TO_MAIN
GROUP6_FINAL_STATE = CLOSED / APPROVED
G7_F01_FINAL_STATE = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
G7_F01_AUTHORIZED = false
EXTERNAL_AUDIT_OF_PROMPT111 = PENDING
```
