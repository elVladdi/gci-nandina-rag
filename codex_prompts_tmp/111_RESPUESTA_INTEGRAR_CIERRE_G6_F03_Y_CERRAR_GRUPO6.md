# Prompt111 - Cierre G6-F03 y Grupo 6

```text
PROMPT111_EXECUTION = COMPLETE
WORKSPACE_CONTRACT = PASS / C:\Users\Vladimir\OneDrive\Documentos\Maestría UNMSM\LLM_RGA_NANDINA / origin=https://github.com/elVladdi/gci-nandina-rag.git
MAIN_PRE_INTEGRATION = 3390878a62ce32ba0e6f4fce69a394c903f5ff11
APPROVED_CANDIDATE = b5eb500ee3215fd4fcdb5a8bde20a00b2f1c17b6
LINEAGE_CHECK = PASS / direct parent 3390878a62ce32ba0e6f4fce69a394c903f5ff11 / ahead 1 / behind 0 / approved blobs 10e96b0399bfe45bad90c1b84a61c368d0f9716b and 0b35084e2b10397b329c42907593c17b40c55d1c
CANDIDATE_CHANGED_PATH_COUNT = 2
CANDIDATE_INTEGRATION_METHOD = FAST_FORWARD_ONLY
MAIN_AFTER_CANDIDATE_FF = b5eb500ee3215fd4fcdb5a8bde20a00b2f1c17b6
GROUP6_CLOSURE_COMMIT = e93b44164a9619dad1f527a3b2d4479265858e39
MAIN_FINAL = e93b44164a9619dad1f527a3b2d4479265858e39
FINAL_ADMIN_DIFF_PATH_COUNT = 2
FINAL_ADMIN_DIFF_PATHS = docs/figures/group6/g6_caption_registry_v0.1.md; outputs/audits/group6_closure_v0.1.json
FINAL_CAPTION_TEXT_MATCH_APPROVED_CANDIDATE = 3/3 / exact; only four administrative status lines changed
FINAL_CLOSURE_JSON_SCIENTIFIC_FIELDS_MATCH = PASS / only artifact_id, status, g6_f03_candidate_status, group6_closure_candidate, group6_closed, external_audit changed
FIGURE_COUNT = 3
CAPTION_COUNT = 3
FICHAS_BASE = 1037ff158512224c2a07f69643f7238776efe8b5
FICHAS_FINAL = bed229d81b2ce3258e1ac3c9efc171458e2891aa
PLAN_BASE = b74b96d0163807007e4579d86450dd235125b30f
PLAN_FINAL = cc9a47986dfbae138738ad9945f0c0b1859b9f4f
G6_F01_FINAL_STATE = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G6_F02_FINAL_STATE = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G6_F03_FINAL_STATE = CLOSED / APPROVED / INTEGRATED_TO_MAIN
GROUP6_FINAL_STATE = CLOSED / APPROVED
G7_F01_FINAL_STATE = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
G7_F01_AUTHORIZED = false
SCIENTIFIC_DATA_CHANGE_COUNT = 0
NEW_INFERENCE_COUNT = 0
NEW_CI_COUNT = 0
NEW_P_VALUE_COUNT = 0
ARTICLE_MODIFIED = false
THESIS_MODIFIED = false
EXP12_REOPENED = false
PROMPT110_EXTERNAL_AUDIT = PASS
EXTERNAL_AUDIT_OF_PROMPT111 = PENDING
```

## Verificacion de alcance

Se verificaron las cuatro refs iniciales, el parent exacto, ahead/behind `1/0`, los dos paths nuevos y ambos blobs aprobados antes de integrar. `main` recibio primero el candidato por fast-forward puro y se publico en `b5eb500ee3215fd4fcdb5a8bde20a00b2f1c17b6`. Un unico commit administrativo posterior modifico solo el caption registry y el closure JSON; ese commit se publico en `main = e93b44164a9619dad1f527a3b2d4479265858e39`.

La comparacion final contra el candidato confirma que los tres `final_caption` y todos los campos cientificos y bindings del JSON permanecen identicos. El Markdown difiere solo en cuatro estados `APPROVED`; el JSON solo en las seis claves administrativas indicadas arriba. El closure final declara `group6_closed=true`, `external_audit=PASS` y `g7_f01_authorized=false`.

La rama de fichas avanzo desde `1037ff1` a `bed229d` cambiando exclusivamente su registro de estado. El Plan Maestro avanzo por fast-forward desde `b74b96d` a `cc9a479`, modificando solo su archivo canonico: tabla de Grupos 6/7 y una entrada historica fechada de cierre. Grupo 8 quedo pendiente. No se editaron figuras, scripts, ledger, fuentes cientificas, tesis ni articulo; no se activo G7-F01 ni se reabrio EXP12. Los tres untracked historicos del workspace quedaron sin tocar.
