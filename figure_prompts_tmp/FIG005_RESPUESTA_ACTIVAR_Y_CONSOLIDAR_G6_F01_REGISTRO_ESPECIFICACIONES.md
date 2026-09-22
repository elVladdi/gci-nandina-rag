# FIG005 — Respuesta oficial: activación y consolidación de G6-F01

```text
FIG005_EXECUTION = COMPLETE
SOURCE_CONTRACT = PASS

ACTIVATION_COMMIT = e7079755ad57033ef9cfa1a52664b47ca20125a5
FICHAS_POSTEXEC_COMMIT = f5686cc7aa7ffd11ab45dc52cf258b256523abc9

G6_F01_BRANCH = figures/g6-f01-spec-registry-v01
G6_F01_CANDIDATE_COMMIT = b6404ca85c8cd0b18a6b318bae1236d2ef021f4a
G6_F01_CANDIDATE_PARENT = ca065618d5df0019f76ef5a971e858d91c263e1f
COMMITS_AHEAD = 1
COMMITS_BEHIND = 0
CHANGED_PATH_COUNT = 1
CHANGED_PATHS =
  outputs/figures/group6/g6_figure_spec_registry_v0.1.json

FIGURE_SPEC_COUNT = 3
NON_FIGURE_DISPOSITION_COUNT = 6
NEW_SCIENTIFIC_METRIC_COUNT = 0
NEW_INFERENCE_COUNT = 0
NEW_CI_COUNT = 0
NEW_P_VALUE_COUNT = 0
FIGURE_BINARY_COUNT = 0
FIGURE_SCRIPT_COUNT = 0

MAIN_FINAL = ca065618d5df0019f76ef5a971e858d91c263e1f
PLAN_FINAL = 98b1a8c54d7a7ccfd86e70078acf77b4cdce9f6e
FICHAS_FINAL = f5686cc7aa7ffd11ab45dc52cf258b256523abc9

G6_F01_FINAL_STATE = CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
GROUP6_FINAL_STATE = IN_PROGRESS
G6_F02_FINAL_STATE = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
EXTERNAL_AUDIT = PENDING
```

## Verificación del contrato de ejecución

- `main` permaneció exactamente en `ca065618d5df0019f76ef5a971e858d91c263e1f`.
- el Plan Maestro permaneció exactamente en `98b1a8c54d7a7ccfd86e70078acf77b4cdce9f6e`.
- la rama de fichas partió de `b17202cb1360f6ad01aaef42d1fd3fb86b201cbc`; el commit de activación modificó únicamente `docs/fichas/grupos_3_8/04_REGISTRO_ESTADO_FICHAS.md`, y el commit postejecución volvió a modificar únicamente ese registro.
- la ficha individual `docs/fichas/grupos_3_8/grupo_6/G6_F01_CATALOGO_Y_ESPECIFICACION_FIGURAS.md` permaneció inalterada, con blob congelado `80771ddbfb4b4e54c90ed92f43942d8e3d30a764`.
- la rama candidata `figures/g6-f01-spec-registry-v01` se creó exactamente desde `ca065618d5df0019f76ef5a971e858d91c263e1f`.
- frente a ese parent, el candidato está `1` commit adelante, `0` atrás y contiene exactamente un path añadido: `outputs/figures/group6/g6_figure_spec_registry_v0.1.json`.
- el registro consolida exactamente tres especificaciones de figura aprobadas: `G6-FIG-01`, `G6-FIG-02` y `G6-FIG-03`, y seis disposiciones de material no gráfico.
- no se generaron imágenes, binarios, scripts, métricas nuevas, inferencia nueva, CI nuevos ni p-values; no se modificaron artículo o tesis; EXP12 no se reabrió; G6-F02 no fue autorizado ni iniciado.

## Fuentes de diseño consolidadas

```text
FIG001 = 2c31d0c7112abedab224023b33d8173f116b3712
FIG002 = d2f9e07923789709a52622bea922be84aefc526d
FIG003 = a9059e9a22a33e7a088ac832d00fcb941a49e4b7
FIG004 = 89d95744b2ab446245a5522eefc8279f673a8a7c
```

Las fuentes científicas canónicas y sus hashes se conservaron sin recomputación dentro del registro de especificaciones. El candidato queda pendiente de auditoría externa y no autoriza ejecutar G6-F02.
