# PROMPT109 — INTEGRAR REMEDIACIÓN DE ACCESIBILIDAD Y DEJAR G6-F03 LISTA PARA REANUDACIÓN VISUAL

## 0. Rol y alcance

Actúa como **CODEX ejecutor reproducible** del proyecto `elVladdi/gci-nandina-rag`.

Debes realizar exclusivamente la **integración técnica** del candidato correctivo de accesibilidad aprobado externamente por la IA Experimental y reconciliar el registro de estado de fichas.

No ejecutes el contenido científico-visual restante de G6-F03. No redactes captions finales. No crees el cierre de Grupo 6. No actives G7-F01.

Después de esta integración, el siguiente actor sustantivo debe ser la **IA Diseñadora y Auditora de Figuras Científicas**, que retomará la auditoría visual/captions de G6-F03 sobre los artefactos corregidos ya integrados.

---

## 1. Estado vinculante y auditoría externa

La IA Experimental realizó auditoría independiente del resultado de Prompt108 y establece como vinculante:

```text
PROMPT108_EXTERNAL_AUDIT = PASS
SCIENTIFIC_CORRECTION_REQUIRED = false
RERUN_REQUIRED = false
APPROVED_ACCESSIBILITY_REMEDIATION_CANDIDATE = 3390878a62ce32ba0e6f4fce69a394c903f5ff11
APPROVED_PARENT = 71b13caf6b97e254b4c701b23318bcb0682714bd
SCIENTIFIC_DATA_CHANGE_COUNT = 0
METRIC_CHANGE_COUNT = 0
CI_CHANGE_COUNT = 0
DENOMINATOR_CHANGE_COUNT = 0
CLAIM_CHANGE_COUNT = 0
NEW_INFERENCE_COUNT = 0
NEW_P_VALUE_COUNT = 0
```

La auditoría verificó además:

```text
candidate is exactly 1 commit ahead / 0 behind main base
changed path count = 10
changed paths = 3 SVG + 3 PNG + 3 render scripts + 1 hash ledger
G6-FIG-01 accessibility thresholds = PASS
G6-FIG-02 mandatory axis-label thresholds = PASS
G6-FIG-02 ticks/legend remediation target = PASS for ticks and legend entries
G6-FIG-03 general minimum and six panel-title thresholds = PASS
scientific sources and G6-F01 registry unchanged
```

No reaudites ni modifiques el contenido científico de las figuras en este prompt. Solo revalida integridad/lineage antes de integrar.

---

## 2. Workspace canónico

Trabaja exclusivamente en:

```text
C:\Users\Vladimir\OneDrive\Documentos\Maestría UNMSM\LLM_RGA_NANDINA
```

Antes de cualquier cambio ejecuta y registra:

```powershell
cd "C:\Users\Vladimir\OneDrive\Documentos\Maestría UNMSM\LLM_RGA_NANDINA"
git rev-parse --show-toplevel
git remote get-url origin
git status --porcelain
git worktree list
git fetch origin
git rev-parse origin/main
git rev-parse origin/figures/g6-f03-accessibility-remediation-v01
git rev-parse origin/docs/fichas-grupos-3-8
git rev-parse origin/codex/prompts-temporary
```

Debes observar al inicio:

```text
origin/main = 71b13caf6b97e254b4c701b23318bcb0682714bd
origin/figures/g6-f03-accessibility-remediation-v01 = 3390878a62ce32ba0e6f4fce69a394c903f5ff11
origin/docs/fichas-grupos-3-8 = 031c94037939d57c6cf1224e81bf713f3541cd12
```

STOP si cualquiera de estos refs cambió antes de iniciar, si el workspace no es el canónico o si aparecen modificaciones tracked preexistentes no explicadas.

Preserva sin tocar los untracked históricos conocidos.

---

## 3. Revalidación mínima obligatoria del candidato

Antes de integrar confirma:

```text
BASE = 71b13caf6b97e254b4c701b23318bcb0682714bd
HEAD = 3390878a62ce32ba0e6f4fce69a394c903f5ff11
STATUS = ahead
AHEAD_BY = 1
BEHIND_BY = 0
PARENT_OF_HEAD = BASE
```

El diff BASE→HEAD debe contener exactamente estos 10 paths y ningún otro:

```text
figures/group6/g6_fig_01_he2.png
figures/group6/g6_fig_01_he2.svg
figures/group6/g6_fig_02_phase_e.png
figures/group6/g6_fig_02_phase_e.svg
figures/group6/g6_fig_03_exp11a.png
figures/group6/g6_fig_03_exp11a.svg
outputs/figures/group6/g6_figure_hash_ledger_v0.1.csv
src/figures/group6/render_g6_fig_01_he2.py
src/figures/group6/render_g6_fig_02_phase_e.py
src/figures/group6/render_g6_fig_03_exp11a.py
```

No modifiques ninguno de estos 10 archivos durante este prompt.

Confirma también que siguen fuera del diff:

```text
outputs/figures/group6/g6_figure_spec_registry_v0.1.json
outputs/results/**
outputs/analysis/**
article/**
la tesis
Plan Maestro
```

---

## 4. Integración a main

Integra exclusivamente mediante **FAST_FORWARD_ONLY**:

```text
MAIN_FROM = 71b13caf6b97e254b4c701b23318bcb0682714bd
MAIN_TO = 3390878a62ce32ba0e6f4fce69a394c903f5ff11
INTEGRATION_METHOD = FAST_FORWARD_ONLY
```

No uses cherry-pick, squash, merge commit, rebase ni force-push.

Después confirma:

```text
origin/main = 3390878a62ce32ba0e6f4fce69a394c903f5ff11
ACCESSIBILITY_REMEDIATION = CLOSED / APPROVED / INTEGRATED_TO_MAIN
```

La integración técnica **no reabre G6-F02 científicamente**. Mantén:

```text
G6_F02 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
```

---

## 5. Actualización exclusiva del registro de fichas

Sobre `docs/fichas-grupos-3-8`, partiendo exactamente de:

```text
031c94037939d57c6cf1224e81bf713f3541cd12
```

actualiza únicamente el registro de estado de fichas para añadir un bloque de cierre de la remediación de accesibilidad con al menos:

```text
FICHA = G6-F03
PREVIOUS_STATE = ACTIVE / AUTHORIZED / CORRECTIVE_CANDIDATE_PENDING_EXTERNAL_AUDIT
PROMPT108_RESPONSE_COMMIT = 8348d4d06218ab0472d01d074a35b32b4b81b9c9
ACCESSIBILITY_REMEDIATION_CANDIDATE = 3390878a62ce32ba0e6f4fce69a394c903f5ff11
ACCESSIBILITY_REMEDIATION_PARENT = 71b13caf6b97e254b4c701b23318bcb0682714bd
EXTERNAL_AUDIT = PASS
SCIENTIFIC_CORRECTION_REQUIRED = false
RERUN_REQUIRED = false
INTEGRATION_METHOD = FAST_FORWARD_ONLY
INTEGRATION_COMMIT = 3390878a62ce32ba0e6f4fce69a394c903f5ff11
ACCESSIBILITY_REMEDIATION_FINAL_STATE = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G6_F02_SCIENTIFIC_STATE = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G6_F03 = ACTIVE / AUTHORIZED / EXECUTION_PENDING
G6_F03_NEXT_ACTOR = IA_DISENADORA_Y_AUDITORA_DE_FIGURAS
GROUP6 = IN_PROGRESS / NOT_CLOSED
G7_F01 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
GROUP7_AUTHORIZED = false
```

No cambies la ficha científica G6-F03; solo su registro de estado.

No modifiques el Plan Maestro: su estado de alto nivel `GROUP6 = IN_PROGRESS` no cambia.

---

## 6. Prohibiciones

No:

- regeneres figuras;
- edites scripts;
- edites SVG/PNG;
- recalcules ledger;
- cambies datos, métricas, CI, denominadores o claims;
- ejecutes la auditoría sustantiva restante de G6-F03;
- redactes captions finales;
- crees `docs/figures/group6/g6_caption_registry_v0.1.md`;
- crees `outputs/audits/group6_closure_v0.1.json`;
- cierres Grupo 6;
- actives G7-F01;
- modifiques tesis o artículo;
- reabras EXP12.

---

## 7. Respuesta oficial

Publica la respuesta en:

```text
codex_prompts_tmp/109_RESPUESTA_INTEGRAR_REMEDIACION_ACCESIBILIDAD_Y_REANUDAR_G6_F03.md
```

sobre la rama:

```text
codex/prompts-temporary
```

Incluye como mínimo:

```text
PROMPT109_EXECUTION
WORKSPACE_CONTRACT
MAIN_PRE_INTEGRATION
APPROVED_CANDIDATE
LINEAGE_CHECK
CHANGED_PATH_COUNT
INTEGRATION_METHOD
MAIN_FINAL
FICHAS_BASE
FICHAS_FINAL
ACCESSIBILITY_REMEDIATION_FINAL_STATE
G6_F02_FINAL_STATE
G6_F03_FINAL_STATE
G6_F03_NEXT_ACTOR
GROUP6_FINAL_STATE
G7_F01_FINAL_STATE
PLAN_FINAL
ARTICLE_MODIFIED
THESIS_MODIFIED
EXTERNAL_AUDIT
```

El terminal esperado es:

```text
PROMPT109_EXECUTION = COMPLETE
ACCESSIBILITY_REMEDIATION_FINAL_STATE = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G6_F02_FINAL_STATE = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G6_F03_FINAL_STATE = ACTIVE / AUTHORIZED / EXECUTION_PENDING
G6_F03_NEXT_ACTOR = IA_DISENADORA_Y_AUDITORA_DE_FIGURAS
GROUP6_FINAL_STATE = IN_PROGRESS / NOT_CLOSED
G7_F01_FINAL_STATE = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
EXTERNAL_AUDIT = PENDING_BY_IA_EXPERIMENTAL_FOR_INTEGRATION_ONLY
```
