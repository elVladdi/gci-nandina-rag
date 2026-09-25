# PROMPT110 — MATERIALIZAR CANDIDATO G6-F03 DE CAPTIONS Y CIERRE DE GRUPO 6

## 0. Rol y objetivo

Actúa como **CODEX ejecutor reproducible** del proyecto `elVladdi/gci-nandina-rag`.

Debes ejecutar exclusivamente la **materialización técnica del candidato G6-F03** cuyos contenidos científico-visuales fueron propuestos por FIG009 y aprobados externamente por la IA Experimental.

Tu tarea NO es volver a diseñar captions, NO es reauditar las figuras, NO es cerrar formalmente Grupo 6 y NO es activar G7-F01.

Debes:

1. materializar los dos outputs obligatorios de G6-F03;
2. preservar exactamente el contenido científico aprobado por FIG009;
3. ajustar únicamente campos administrativos de estado para reflejar que ahora existe un candidato materializado pendiente de auditoría externa de la IA Experimental;
4. publicar el candidato en una rama dedicada sin integrarlo a `main`;
5. reconciliar el registro de estado de fichas en su rama documental;
6. dejar Grupo 6 abierto hasta nueva auditoría externa.

---

## 1. Estado vinculante de entrada

```text
MAIN_BASE = 3390878a62ce32ba0e6f4fce69a394c903f5ff11
G6_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G6_F02 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G6_F03 = ACTIVE / AUTHORIZED / EXECUTION_PENDING
GROUP6 = IN_PROGRESS / NOT_CLOSED
G7_F01 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
```

La remediación de accesibilidad ya está cerrada e integrada.

La IA Experimental establece como vinculante:

```text
FIG009_EXTERNAL_AUDIT = PASS
SCIENTIFIC_CORRECTION_REQUIRED = false
CAPTION_CORRECTION_REQUIRED = false
TECHNICAL_ARTIFACT_CORRECTION_REQUIRED = false
FIG009_RESPONSE_COMMIT = 71fd23d18b2343dcdd933234227e77e455520a5a
MAIN_SOURCE_COMMIT = 3390878a62ce32ba0e6f4fce69a394c903f5ff11
FIGURE_COUNT = 3
CAPTION_COUNT = 3
SCIENTIFIC_DATA_CHANGE_COUNT = 0
NEW_INFERENCE_COUNT = 0
NEW_CI_COUNT = 0
NEW_P_VALUE_COUNT = 0
EXP12_REOPENED = false
GROUP6_CLOSURE_AUTHORIZED_FOR_MATERIALIZED_CANDIDATE_ONLY = true
GROUP6_FORMAL_CLOSURE_AUTHORIZED = false
G7_F01_AUTHORIZED = false
```

El PASS externo aprueba el **contenido científico y visual propuesto** por FIG009. Esta ejecución todavía debe producir un candidato materializado para verificación de integridad antes del cierre formal.

---

## 2. Fuentes rectoras obligatorias

Lee íntegramente antes de escribir:

```text
figure_prompts_tmp/FIG009_RESPUESTA_REANUDAR_G6_F03_CAPTIONS_AUTOSUFICIENCIA_Y_CIERRE_VISUAL.md
commit = 71fd23d18b2343dcdd933234227e77e455520a5a
```

Usa específicamente:

- Sección 8 — propuesta completa de `g6_caption_registry_v0.1.md`;
- Sección 9 — propuesta de `group6_closure_v0.1.json`.

También verifica:

```text
origin/main = 3390878a62ce32ba0e6f4fce69a394c903f5ff11
origin/docs/fichas-grupos-3-8 = 796dad55c491843fccf925431bd14b5848638d10
origin/codex/prompts-temporary incluye FIG009 response commit 71fd23d18b2343dcdd933234227e77e455520a5a
```

Autoridades científicas de solo lectura:

```text
outputs/figures/group6/g6_figure_spec_registry_v0.1.json
outputs/figures/group6/g6_figure_hash_ledger_v0.1.csv
outputs/results/group5/**
outputs/analysis/group3/**
outputs/analysis/group4/**
```

No uses tesis ni artículo como fuente de verdad.

---

## 3. Workspace canónico y preflight

Trabaja exclusivamente en:

```text
C:\Users\Vladimir\OneDrive\Documentos\Maestría UNMSM\LLM_RGA_NANDINA
```

Registra:

```powershell
cd "C:\Users\Vladimir\OneDrive\Documentos\Maestría UNMSM\LLM_RGA_NANDINA"
git rev-parse --show-toplevel
git remote get-url origin
git status --porcelain
git worktree list
git fetch origin
git rev-parse origin/main
git rev-parse origin/docs/fichas-grupos-3-8
git rev-parse origin/codex/prompts-temporary
```

STOP si:

- el workspace u origin no son los canónicos;
- `origin/main` no es exactamente `3390878a62ce32ba0e6f4fce69a394c903f5ff11`;
- `origin/docs/fichas-grupos-3-8` no es exactamente `796dad55c491843fccf925431bd14b5848638d10`;
- existen cambios tracked preexistentes no explicados;
- no puedes preservar los untracked históricos conocidos sin tocarlos.

---

## 4. Materialización del candidato G6-F03

Crea una rama nueva desde `MAIN_BASE`:

```text
figures/g6-f03-caption-closure-v01
```

En esa rama crea **exactamente dos paths nuevos**:

```text
docs/figures/group6/g6_caption_registry_v0.1.md
outputs/audits/group6_closure_v0.1.json
```

No modifiques ningún path ya existente.

### 4.1 Caption registry

Materializa el contenido científico de la Sección 8 de FIG009 **sin cambiar una sola afirmación científica ni el texto de los tres `final_caption`**.

Se permiten exclusivamente estas normalizaciones administrativas de estado:

```text
registry top-level status:
READY_FOR_EXTERNAL_AUDIT
→ CANDIDATE_PENDING_EXTERNAL_AUDIT

per-figure status:
READY_FOR_EXTERNAL_AUDIT
→ CANDIDATE_PENDING_EXTERNAL_AUDIT
```

Mantén exactamente:

```text
main_source_commit = 3390878a62ce32ba0e6f4fce69a394c903f5ff11
figure_count = 3
caption_count = 3
```

Los tres captions, rutas, roles, límites, declaraciones de incertidumbre, bindings y controles de accesibilidad deben permanecer semántica y textualmente iguales a la propuesta aprobada, salvo las normalizaciones de estado descritas arriba.

### 4.2 Closure JSON

Materializa la Sección 9 de FIG009 preservando todos sus bindings y checks científicos.

Normaliza únicamente los campos administrativos para representar **candidato materializado pendiente de auditoría externa**, con estos valores obligatorios:

```json
"status": "CANDIDATE_PENDING_EXTERNAL_AUDIT",
"g6_f03_candidate_status": "CANDIDATE_PENDING_EXTERNAL_AUDIT",
"group6_closure_candidate": true,
"group6_closed": false,
"external_audit": "PENDING",
"g7_f01_authorized": false,
"recommended_group6_state_after_external_pass": "CLOSED / APPROVED",
"recommended_next_ficha_after_external_pass": "G7-F01"
```

Mantén:

```text
scientific_consistency = PASS
accessibility = PASS
caption_self_containment = PASS
canonical_table_consistency = PASS
claim_scope_consistency = PASS
scientific_data_change_count = 0
new_inference_count = 0
new_ci_count = 0
new_p_value_count = 0
exp12_reopened = false
article_modified = false
thesis_modified = false
```

No añadas nuevas conclusiones.

---

## 5. Validación del candidato

Antes de publicar valida al menos:

```text
NEW_PATH_COUNT = 2
MODIFIED_EXISTING_PATH_COUNT = 0
FIGURE_COUNT = 3
CAPTION_COUNT = 3
FINAL_CAPTION_TEXT_MATCH_FIG009 = 3/3
SOURCE_BINDINGS_MATCH_FIG009 = PASS
FIGURE_BINDINGS_MATCH_MAIN = PASS
SCIENTIFIC_DATA_CHANGE_COUNT = 0
NEW_INFERENCE_COUNT = 0
NEW_CI_COUNT = 0
NEW_P_VALUE_COUNT = 0
EXP12_REOPENED = false
ARTICLE_MODIFIED = false
THESIS_MODIFIED = false
```

Compara cada caption materializado con FIG009 y reporta cualquier diferencia byte/textual deliberada. Fuera de los campos de estado autorizados, la diferencia debe ser cero.

Realiza exactamente **un commit** en la rama candidata.

El candidato debe cumplir:

```text
PARENT = 3390878a62ce32ba0e6f4fce69a394c903f5ff11
AHEAD_BY = 1
BEHIND_BY = 0
CHANGED_PATH_COUNT = 2
```

No integres a `main`.

---

## 6. Registro de estado de fichas

En `docs/fichas-grupos-3-8`, partiendo exactamente de:

```text
796dad55c491843fccf925431bd14b5848638d10
```

modifica únicamente:

```text
docs/fichas/grupos_3_8/04_REGISTRO_ESTADO_FICHAS.md
```

Añade un bloque que registre como mínimo:

```text
FICHA = G6-F03
FIG009_RESPONSE_COMMIT = 71fd23d18b2343dcdd933234227e77e455520a5a
FIG009_EXTERNAL_AUDIT = PASS
CAPTION_CLOSURE_CANDIDATE_BRANCH = figures/g6-f03-caption-closure-v01
CAPTION_CLOSURE_CANDIDATE_COMMIT = <commit creado>
CAPTION_REGISTRY_PATH = docs/figures/group6/g6_caption_registry_v0.1.md
GROUP6_CLOSURE_PATH = outputs/audits/group6_closure_v0.1.json
G6_F03 = CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
GROUP6 = IN_PROGRESS / NOT_CLOSED
GROUP6_CLOSED = false
G7_F01 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
G7_F01_AUTHORIZED = false
PENDING_EXTERNAL_AUDIT = true
```

No cierres G6-F03 todavía.

No modifiques Plan Maestro porque su estado alto nivel continúa siendo `GROUP6 = IN_PROGRESS`.

---

## 7. Prohibiciones

No:

- edites SVG/PNG;
- edites scripts de render;
- recalcules ledger;
- edites el registry G6-F01;
- cambies tablas G5;
- cambies análisis G3/G4;
- cambies cifras, métricas, CI, denominadores o claims;
- reescribas captions;
- introduzcas nueva inferencia;
- reabras EXP12;
- modifiques tesis o artículo;
- integres el candidato a `main`;
- declares `G6_F03 = CLOSED / APPROVED`;
- declares `GROUP6 = CLOSED / APPROVED`;
- autorices ni actives G7-F01.

---

## 8. Respuesta oficial

Publica la respuesta únicamente en:

```text
codex_prompts_tmp/110_RESPUESTA_MATERIALIZAR_CANDIDATO_G6_F03_CAPTIONS_Y_CIERRE.md
```

sobre:

```text
codex/prompts-temporary
```

Incluye como mínimo:

```text
PROMPT110_EXECUTION
WORKSPACE_CONTRACT
MAIN_BASE
FIG009_RESPONSE_COMMIT
FIG009_EXTERNAL_AUDIT
CANDIDATE_BRANCH
CANDIDATE_COMMIT
CANDIDATE_PARENT
CANDIDATE_TREE
CHANGED_PATH_COUNT
CHANGED_PATHS
CAPTION_COUNT
FIGURE_COUNT
FINAL_CAPTION_TEXT_MATCH_FIG009
SOURCE_BINDINGS_MATCH_FIG009
SCIENTIFIC_DATA_CHANGE_COUNT
NEW_INFERENCE_COUNT
NEW_CI_COUNT
NEW_P_VALUE_COUNT
EXP12_REOPENED
ARTICLE_MODIFIED
THESIS_MODIFIED
FICHAS_BASE
FICHAS_FINAL
G6_F03_FINAL_STATE
GROUP6_FINAL_STATE
G7_F01_FINAL_STATE
EXTERNAL_AUDIT
```

Terminal esperado:

```text
PROMPT110_EXECUTION = COMPLETE
G6_F03_FINAL_STATE = CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
GROUP6_FINAL_STATE = IN_PROGRESS / NOT_CLOSED
G7_F01_FINAL_STATE = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
EXTERNAL_AUDIT = PENDING
```
