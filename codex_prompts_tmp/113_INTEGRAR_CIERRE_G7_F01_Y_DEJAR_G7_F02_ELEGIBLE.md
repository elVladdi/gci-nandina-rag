# PROMPT113 — INTEGRAR CIERRE G7-F01 Y DEJAR G7-F02 ELEGIBLE

## 0. Rol y objetivo

Actúa como **CODEX ejecutor reproducible** del proyecto `elVladdi/gci-nandina-rag`.

Esta ejecución es exclusivamente técnica-administrativa. La IA Experimental auditó independientemente el candidato de **G7-F01 — Sincronización editorial y contrato de redacción** y emitió `PASS`.

Debes:

1. revalidar la identidad exacta del candidato aprobado;
2. integrarlo a `main` exclusivamente por fast-forward;
3. convertir únicamente sus estados administrativos de candidato a estados finales aprobados;
4. cerrar formalmente G7-F01;
5. mantener Grupo 7 abierto;
6. dejar G7-F02 **solo elegible**, no autorizada ni ejecutada;
7. reconciliar el registro de fichas y el Plan Maestro;
8. no modificar tesis ni artículo.

No redactes tesis. No redactes artículo. No ejecutes G7-F02.

---

## 1. Auditoría externa vinculante

La IA Experimental establece:

```text
PROMPT112_EXTERNAL_AUDIT = PASS
SCIENTIFIC_CORRECTION_REQUIRED = false
SOURCE_FREEZE_CORRECTION_REQUIRED = false
RERUN_REQUIRED = false

APPROVED_G7_F01_CANDIDATE = d91298758dba674003bf650e7a303c36bd0b74d9
APPROVED_PARENT = e93b44164a9619dad1f527a3b2d4479265858e39
APPROVED_CANDIDATE_BRANCH = writing/g7-f01-source-freeze-v01
APPROVED_CHANGED_PATH_COUNT = 2

APPROVED_MD_BLOB = 0c66432a5a041deedb5d0dc59972886d67d73e54
APPROVED_JSON_BLOB = 92370b163f53ad89b960270a62fd82a0625c5de8

ARTICLE_HEAD_FROZEN = 2aad97aaceec0af6be0edb9ba0dd29170ad35baf
THESIS_MANIFEST_BLOB = 42b89b512b8db818238bfd0da22a7c75c207d9f1
THESIS_CURRENT_SHA256 = 08b48ec1687ae0a0d943724bf2d682aca02d2a9f5a124b3dc35270e041bc3aed

HG_FORMAL_DISPOSITION = NO_FORMAL_DISPOSITION_FOUND
HE1_FORMAL_DISPOSITION = NO_FORMAL_DISPOSITION_FOUND
HE2 = SUPPORTED
HE3 = SUPPORTED
HE4 = PARTIALLY_SUPPORTED
HE5 = INCONCLUSIVE

THESIS_BYTE_HASH_RECHECK_BEFORE_G7_F02_EDIT = REQUIRED
APPROVED_PROJECT_AND_ANNEX_BYTES_NOT_FROZEN_HERE_FOR_LITERAL_FORMULATION_OR_METHOD_EDITS = true
ARTICLE_DRIFT_CHECK_BEFORE_G7_F03 = REQUIRED

G7_F01_CLOSURE_AUTHORIZED = true
G7_F02_ACTIVATION_AUTHORIZED = false
G7_F03_ACTIVATION_AUTHORIZED = false
GROUP8_AUTHORIZED = false
```

La auditoría confirmó que el candidato:

```text
PARENT = e93b44164a9619dad1f527a3b2d4479265858e39
AHEAD_BY = 1
BEHIND_BY = 0
CHANGED_PATH_COUNT = 2
```

con los únicos paths:

```text
docs/writing/group7/g7_writing_source_freeze_v0.1.md
docs/writing/group7/g7_writing_source_freeze_v0.1.json
```

No cambies el contenido científico ni los contratos de escritura aprobados.

---

## 2. Refs obligatorios al iniciar

Debes observar exactamente:

```text
origin/main = e93b44164a9619dad1f527a3b2d4479265858e39
origin/writing/g7-f01-source-freeze-v01 = d91298758dba674003bf650e7a303c36bd0b74d9
origin/docs/fichas-grupos-3-8 = 6e8956086d9bed0e826d158175593d5c9ff2c9a4
origin/docs/plan-maestro-temporal-2026-08-31 = 2f22158cb07ad0c54379a4d5f0f043066207a1f6
```

La respuesta de Prompt112 vigente es:

```text
codex_prompts_tmp/112_RESPUESTA_ACTIVAR_Y_EJECUTAR_G7_F01_WRITING_SOURCE_FREEZE.md
```

STOP si cualquiera de esos cuatro refs cambió antes de iniciar.

`origin/article/main-manuscript` es una rama editorial viva y no debe modificarse en esta ejecución. Registra su head observado solo como control de deriva. No actualices el `ARTICLE_HEAD_FROZEN` del source freeze: ese campo debe seguir identificando el snapshot aprobado por G7-F01.

---

## 3. Workspace canónico

Trabaja exclusivamente en:

```text
C:\Users\Vladimir\OneDrive\Documentos\Maestría UNMSM\LLM_RGA_NANDINA
```

Antes de cualquier cambio registra:

```powershell
cd "C:\Users\Vladimir\OneDrive\Documentos\Maestría UNMSM\LLM_RGA_NANDINA"
git rev-parse --show-toplevel
git remote get-url origin
git status --porcelain
git worktree list
git fetch origin
git rev-parse origin/main
git rev-parse origin/writing/g7-f01-source-freeze-v01
git rev-parse origin/docs/fichas-grupos-3-8
git rev-parse origin/docs/plan-maestro-temporal-2026-08-31
git rev-parse origin/article/main-manuscript
git rev-parse origin/codex/prompts-temporary
```

STOP si:

- workspace u origin no son canónicos;
- existen cambios tracked preexistentes no explicados;
- no puedes preservar los untracked históricos conocidos;
- algún ref obligatorio no coincide.

---

## 4. Revalidación exacta del candidato aprobado

Antes de integrar verifica:

```text
BASE = e93b44164a9619dad1f527a3b2d4479265858e39
HEAD = d91298758dba674003bf650e7a303c36bd0b74d9
STATUS = ahead
AHEAD_BY = 1
BEHIND_BY = 0
PARENT_OF_HEAD = BASE
CHANGED_PATH_COUNT = 2
```

Los únicos paths deben ser:

```text
docs/writing/group7/g7_writing_source_freeze_v0.1.md
docs/writing/group7/g7_writing_source_freeze_v0.1.json
```

Verifica además exactamente:

```text
MD_BLOB = 0c66432a5a041deedb5d0dc59972886d67d73e54
JSON_BLOB = 92370b163f53ad89b960270a62fd82a0625c5de8
```

Si cualquiera no coincide, STOP sin integrar.

---

## 5. Etapa A — integración exacta del candidato

Integra exclusivamente mediante fast-forward:

```text
MAIN_FROM = e93b44164a9619dad1f527a3b2d4479265858e39
MAIN_TO_CANDIDATE = d91298758dba674003bf650e7a303c36bd0b74d9
METHOD = FAST_FORWARD_ONLY
```

No uses cherry-pick, squash, merge commit, rebase ni force-push.

Después de esta etapa:

```text
origin/main = d91298758dba674003bf650e7a303c36bd0b74d9
```

---

## 6. Etapa B — normalización administrativa final en main

Sobre `main` ya integrado, crea **un único commit administrativo** que modifique exclusivamente los mismos dos paths.

### 6.1 `g7_writing_source_freeze_v0.1.md`

Está prohibido alterar:

- source precedence;
- lista/contenido de fuentes;
- identidad de la tesis;
- disposiciones HG/HE1/HE2/HE3/HE4/HE5;
- contratos de escritura de tesis/artículo;
- guardrails;
- gaps abiertos;
- cifras, métricas o interpretaciones.

Normaliza únicamente los estados administrativos necesarios:

```text
status = CANDIDATE_PENDING_EXTERNAL_AUDIT
→ status = APPROVED

external_audit = PENDING
→ external_audit = PASS

g7_f02 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
→ g7_f02 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
```

Si el Markdown no contiene exactamente alguno de estos campos como línea editable, no inventes un bloque nuevo dentro del contenido científico. Haz solo la mínima normalización administrativa coherente con su estructura existente y reporta exactamente qué líneas cambiaron.

### 6.2 `g7_writing_source_freeze_v0.1.json`

Preserva todos los bindings, matrices, fuentes, guardrails y gaps. Cambia únicamente campos administrativos:

```json
"status": "APPROVED",
"governance_refs": {
  "g7_f02": "ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED"
},
"g7_f01_candidate_status": "CLOSED / APPROVED / INTEGRATED_TO_MAIN",
"g7_f02_authorized": false,
"g7_f03_authorized": false,
"group7_closed": false,
"external_audit": "PASS"
```

Los demás campos deben quedar idénticos al candidato aprobado.

No elimines los gaps:

```text
HG_FORMAL_AGGREGATE_DISPOSITION_NOT_FOUND
HE1_FORMAL_DISPOSITION_NOT_FOUND_GROUP1_EXPLICIT_NO_ASSESSMENT
THESIS_BINARY_SHA_RECHECK_REQUIRED_BEFORE_G7_F02_EDIT
APPROVED_PROJECT_AND_ANNEX_BYTES_NOT_FROZEN_HERE_FOR_LITERAL_FORMULATION_OR_METHOD_EDITS
NO_EXPLICIT_VERSIONED_UNMSM_THESIS_FORMAT_RULE_LOCATED
ARTICLE_DRIFT_CHECK_REQUIRED_BEFORE_G7_F03
```

Después del commit registra:

```text
G7_F01_CLOSURE_COMMIT = <nuevo commit main>
MAIN_FINAL = <mismo commit>
```

El diff `d912987... → MAIN_FINAL` debe contener exactamente los dos paths y solo normalizaciones administrativas.

---

## 7. Etapa C — registro de fichas

Sobre:

```text
origin/docs/fichas-grupos-3-8 = 6e8956086d9bed0e826d158175593d5c9ff2c9a4
```

modifica exclusivamente:

```text
docs/fichas/grupos_3_8/04_REGISTRO_ESTADO_FICHAS.md
```

Añade un bloque final que registre como mínimo:

```text
FICHA = G7-F01
PREVIOUS_STATE = CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
PROMPT112_RESPONSE_COMMIT = <commit de la respuesta Prompt112 en codex/prompts-temporary>
CANDIDATE_COMMIT = d91298758dba674003bf650e7a303c36bd0b74d9
EXTERNAL_AUDIT = PASS
SCIENTIFIC_CORRECTION_REQUIRED = false
SOURCE_FREEZE_CORRECTION_REQUIRED = false
INTEGRATION_METHOD = FAST_FORWARD_ONLY
CANDIDATE_INTEGRATION_COMMIT = d91298758dba674003bf650e7a303c36bd0b74d9
G7_F01_CLOSURE_COMMIT = <MAIN_FINAL>
FINAL_G7_F01_STATE = CLOSED / APPROVED / INTEGRATED_TO_MAIN
GROUP7 = IN_PROGRESS / NOT_CLOSED
G7_F02 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
G7_F02_AUTHORIZED = false
G7_F03 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
GROUP8 = NOT_STARTED / NOT_AUTHORIZED
```

No actives G7-F02.

---

## 8. Etapa D — Plan Maestro

Sobre:

```text
origin/docs/plan-maestro-temporal-2026-08-31 = 2f22158cb07ad0c54379a4d5f0f043066207a1f6
```

modifica exclusivamente:

```text
docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md
```

Actualiza Grupo 7 a:

```text
7. Redacción científica = IN_PROGRESS
G7-F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G7-F02 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
G7-F03 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
```

Grupo 6 permanece cerrado. Grupo 8 permanece pendiente/no autorizado.

Añade una entrada histórica breve del cierre G7-F01 tras auditoría externa. No cambies resultados científicos.

---

## 9. Validación final

Debes verificar como mínimo:

```text
MAIN_FINAL_PARENT = d91298758dba674003bf650e7a303c36bd0b74d9
FINAL_ADMIN_DIFF_PATH_COUNT = 2
SOURCE_REGISTRY_SCIENTIFIC_BINDINGS_CHANGED = 0
ARTICLE_CONTROL_BINDINGS_CHANGED = 0
HYPOTHESIS_BINDINGS_CHANGED = 0
THESIS_WRITING_CONTRACT_CHANGED = 0
ARTICLE_WRITING_CONTRACT_CHANGED = 0
PERMANENT_GUARDRAILS_CHANGED = 0
OPEN_SOURCE_GAPS_REMOVED = 0
SCIENTIFIC_DATA_CHANGE_COUNT = 0
NEW_INFERENCE_COUNT = 0
NEW_CI_COUNT = 0
NEW_P_VALUE_COUNT = 0
THESIS_MODIFIED = false
ARTICLE_MODIFIED = false
EXP12_REOPENED = false
G7_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
GROUP7 = IN_PROGRESS / NOT_CLOSED
G7_F02 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
G7_F03 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
GROUP8 = NOT_STARTED / NOT_AUTHORIZED
```

---

## 10. Prohibiciones

No:

- modifiques ninguna fuente científica;
- modifiques tesis Word;
- modifiques `article/main-manuscript`;
- cambies fuentes/claims/guardrails del source freeze;
- elimines gaps abiertos;
- inventes una disposición HG o HE1;
- actives o ejecutes G7-F02;
- actives o ejecutes G7-F03;
- actives Grupo 8;
- añadas inferencia, métricas, CI o p-values;
- reabras EXP12.

---

## 11. Respuesta oficial

Publica únicamente:

```text
codex_prompts_tmp/113_RESPUESTA_INTEGRAR_CIERRE_G7_F01_Y_DEJAR_G7_F02_ELEGIBLE.md
```

sobre:

```text
codex/prompts-temporary
```

Incluye como mínimo:

```text
PROMPT113_EXECUTION
WORKSPACE_CONTRACT
MAIN_PRE_INTEGRATION
APPROVED_CANDIDATE
LINEAGE_CHECK
CANDIDATE_INTEGRATION_METHOD
MAIN_AFTER_CANDIDATE_FF
G7_F01_CLOSURE_COMMIT
MAIN_FINAL
FINAL_ADMIN_DIFF_PATH_COUNT
FINAL_ADMIN_DIFF_PATHS
SOURCE_REGISTRY_SCIENTIFIC_BINDINGS_CHANGED
ARTICLE_CONTROL_BINDINGS_CHANGED
HYPOTHESIS_BINDINGS_CHANGED
THESIS_WRITING_CONTRACT_CHANGED
ARTICLE_WRITING_CONTRACT_CHANGED
PERMANENT_GUARDRAILS_CHANGED
OPEN_SOURCE_GAPS_REMOVED
FICHAS_BASE
FICHAS_FINAL
PLAN_BASE
PLAN_FINAL
FINAL_G7_F01_STATE
GROUP7_FINAL_STATE
G7_F02_FINAL_STATE
G7_F02_AUTHORIZED
G7_F03_FINAL_STATE
GROUP8_FINAL_STATE
SCIENTIFIC_DATA_CHANGE_COUNT
NEW_INFERENCE_COUNT
NEW_CI_COUNT
NEW_P_VALUE_COUNT
THESIS_MODIFIED
ARTICLE_MODIFIED
EXP12_REOPENED
PROMPT112_EXTERNAL_AUDIT
EXTERNAL_AUDIT_OF_PROMPT113
```

Terminal esperado:

```text
PROMPT113_EXECUTION = COMPLETE
FINAL_G7_F01_STATE = CLOSED / APPROVED / INTEGRATED_TO_MAIN
GROUP7_FINAL_STATE = IN_PROGRESS / NOT_CLOSED
G7_F02_FINAL_STATE = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
G7_F02_AUTHORIZED = false
G7_F03_FINAL_STATE = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
GROUP8_FINAL_STATE = NOT_STARTED / NOT_AUTHORIZED
EXTERNAL_AUDIT_OF_PROMPT113 = PENDING
```
