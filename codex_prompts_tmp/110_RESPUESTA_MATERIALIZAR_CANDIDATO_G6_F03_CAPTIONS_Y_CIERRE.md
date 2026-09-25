# Prompt110 - Candidato materializado G6-F03

```text
PROMPT110_EXECUTION = COMPLETE
WORKSPACE_CONTRACT = PASS / C:\Users\Vladimir\OneDrive\Documentos\Maestría UNMSM\LLM_RGA_NANDINA / origin=https://github.com/elVladdi/gci-nandina-rag.git
MAIN_BASE = 3390878a62ce32ba0e6f4fce69a394c903f5ff11
FIG009_RESPONSE_COMMIT = 71fd23d18b2343dcdd933234227e77e455520a5a
FIG009_EXTERNAL_AUDIT = PASS
CANDIDATE_BRANCH = figures/g6-f03-caption-closure-v01
CANDIDATE_COMMIT = b5eb500ee3215fd4fcdb5a8bde20a00b2f1c17b6
CANDIDATE_PARENT = 3390878a62ce32ba0e6f4fce69a394c903f5ff11
CANDIDATE_TREE = cb619c45122368f3ad30d6758effe3817f9f3137
AHEAD_BY = 1
BEHIND_BY = 0
CHANGED_PATH_COUNT = 2
CHANGED_PATHS =
  docs/figures/group6/g6_caption_registry_v0.1.md
  outputs/audits/group6_closure_v0.1.json
NEW_PATH_COUNT = 2
MODIFIED_EXISTING_PATH_COUNT = 0
CAPTION_COUNT = 3
FIGURE_COUNT = 3
FINAL_CAPTION_TEXT_MATCH_FIG009 = 3/3 / exact
SOURCE_BINDINGS_MATCH_FIG009 = PASS
FIGURE_BINDINGS_MATCH_MAIN = PASS / 6 of 6 SVG/PNG paths exist at main source commit
CAPTION_REGISTRY_DIFF_FROM_FIG009 = four READY_FOR_EXTERNAL_AUDIT status values changed to CANDIDATE_PENDING_EXTERNAL_AUDIT; all other text identical
CLOSURE_JSON_DIFF_FROM_FIG009 = status and g6_f03_candidate_status changed to CANDIDATE_PENDING_EXTERNAL_AUDIT; all other values identical
SCIENTIFIC_DATA_CHANGE_COUNT = 0
NEW_INFERENCE_COUNT = 0
NEW_CI_COUNT = 0
NEW_P_VALUE_COUNT = 0
EXP12_REOPENED = false
ARTICLE_MODIFIED = false
THESIS_MODIFIED = false
FICHAS_BASE = 796dad55c491843fccf925431bd14b5848638d10
FICHAS_FINAL = 1037ff158512224c2a07f69643f7238776efe8b5
MAIN_FINAL = 3390878a62ce32ba0e6f4fce69a394c903f5ff11 / unchanged
G6_F03_FINAL_STATE = CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
GROUP6_FINAL_STATE = IN_PROGRESS / NOT_CLOSED
G7_F01_FINAL_STATE = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
EXTERNAL_AUDIT = PENDING
```

## Integridad del candidato

La propuesta de FIG009 fue leida en su totalidad. El caption registry materializado coincide textualmente con la Seccion 8 tras reemplazar solo los cuatro estados administrativos autorizados (uno global y tres por figura). Los tres `final_caption`, las rutas, roles, limites, declaraciones de incertidumbre, source bindings y controles de accesibilidad quedaron identicos a FIG009. El cierre JSON se comparo por objeto con la Seccion 9: las unicas claves de valor diferente son `status` y `g6_f03_candidate_status`. Los demas 38 campos, incluidos todos los checks cientificos y bindings, son iguales. Los blobs fuente versionados coinciden 6/6, y los blobs del registry y ledger de G6 coinciden con los identificadores declarados.

La rama candidata, previamente existente solo como ref local sin commits propios ni rama remota, avanzo por fast-forward a `MAIN_BASE` antes de crear un unico commit. El commit final es hijo directo de `MAIN_BASE`, un commit ahead/cero behind, y agrega exclusivamente los dos paths obligatorios. Se publico solo `figures/g6-f03-caption-closure-v01`; no se integro a `main`.

La rama `docs/fichas-grupos-3-8` avanzo mediante un commit que modifica unicamente `docs/fichas/grupos_3_8/04_REGISTRO_ESTADO_FICHAS.md`, registrando el candidato y dejando G6-F03 pendiente de auditoria externa, Grupo 6 abierto y G7-F01 sin autorizacion. Los tres untracked historicos del workspace se preservaron. No se editaron figuras, scripts, ledger, fuentes cientificas, Plan Maestro, tesis ni articulo; tampoco se recalcularon metricas o inferencia.
