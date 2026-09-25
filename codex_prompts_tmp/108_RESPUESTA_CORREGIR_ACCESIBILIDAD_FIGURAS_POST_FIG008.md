# Prompt108 - Remediacion de accesibilidad de figuras G6

```text
PROMPT108_EXECUTION = COMPLETE
WORKSPACE_CONTRACT = PASS / C:\Users\Vladimir\OneDrive\Documentos\Maestría UNMSM\LLM_RGA_NANDINA / origin=https://github.com/elVladdi/gci-nandina-rag.git
MAIN_BASE = 71b13caf6b97e254b4c701b23318bcb0682714bd
FIG008_RESPONSE_COMMIT = cbb248ed87836a8c31978344fda08021dc0ea2d2
CORRECTION_BRANCH = figures/g6-f03-accessibility-remediation-v01
CORRECTION_CANDIDATE_COMMIT = 3390878a62ce32ba0e6f4fce69a394c903f5ff11
CORRECTION_PARENT = 71b13caf6b97e254b4c701b23318bcb0682714bd
CORRECTION_TREE = ee2c0513bd34148d12b15f4a655b563d3746ff5c
CHANGED_PATH_COUNT = 10
CHANGED_PATHS =
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
FIGURE_COUNT = 3
FIG01_ACCESSIBILITY_RESULT = PASS / physical SVG 8.333333333333334in x 10.416666666666666in; 2500x3125 PNG; all nonempty text >=8pt; no text collision or clipping detected
FIG02_ACCESSIBILITY_RESULT = PASS / physical SVG 10.0in x 5.625in; 3000x1688 PNG; both axis titles >=10pt; ticks and legend >=9pt; no text collision or clipping detected
FIG03_ACCESSIBILITY_RESULT = PASS / physical SVG 10.0in x 6.666666666666667in; 3000x2000 PNG; six panel titles 9.6pt; no text collision or clipping detected
FIG01_MIN_FONT_PNG_PT = 8.16
FIG01_MIN_FONT_SVG_PT = 8.10
FIG02_X_AXIS_PNG_PT = 10.08
FIG02_X_AXIS_SVG_PT = 10.20
FIG02_Y_AXIS_PNG_PT = 10.08
FIG02_Y_AXIS_SVG_PT = 10.20
FIG02_TICK_LEGEND_MIN_PNG_PT = 9.12
FIG02_TICK_LEGEND_MIN_SVG_PT = 9.00
FIG03_PANEL_TITLE_PNG_PT = 9.60
FIG03_PANEL_TITLE_SVG_PT = 9.60
DETERMINISM_CHECK = PASS / two consecutive executions of each of the three scripts; SVG and PNG run1/run2 SHA-256 identical, 6/6
LEDGER_ROW_COUNT = 16
LEDGER_CANONICAL_SHA256_MATCH_COUNT = 16
LEDGER_CANONICAL_SIZE_MATCH_COUNT = 16
LEDGER_HASH_SEMANTICS = CANONICAL_GIT_CONTENT_BYTES
SCIENTIFIC_DATA_CHANGE_COUNT = 0
METRIC_CHANGE_COUNT = 0
CI_CHANGE_COUNT = 0
DENOMINATOR_CHANGE_COUNT = 0
CLAIM_CHANGE_COUNT = 0
NEW_INFERENCE_COUNT = 0
NEW_P_VALUE_COUNT = 0
FICHAS_FINAL = 031c94037939d57c6cf1224e81bf713f3541cd12 / docs/fichas-grupos-3-8
MAIN_FINAL = 71b13caf6b97e254b4c701b23318bcb0682714bd / unchanged
PLAN_FINAL = b74b96d0163807007e4579d86450dd235125b30f / unchanged
G6_F03_FINAL_STATE = ACTIVE / AUTHORIZED / CORRECTIVE_CANDIDATE_PENDING_EXTERNAL_AUDIT
GROUP6_FINAL_STATE = IN_PROGRESS / NOT_CLOSED
G7_F01_FINAL_STATE = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
EXTERNAL_AUDIT = PENDING
```

## Alcance y tipografia

La rama correctiva es un unico commit, hijo directo del `MAIN_BASE`. Los diez paths del diff son exactamente los autorizados. Los siete registros del ledger correspondientes a registry e inputs cientificos permanecen intactos. No se modificaron Plan Maestro, articulo, tesis, fichas cientificas, datasets, resultados experimentales ni configuraciones.

| Figura y clase | Antes (drawing units) | Despues (drawing units) | SVG final (pt) | PNG final (pt) |
|---|---:|---:|---:|---:|
| FIG01 minimo de texto no vacio | 8.5 | 13.5 | 8.10 | 8.16 |
| FIG01 ticks y titulos de eje | 10-11 | 15 | 9.00 | 9.12 |
| FIG01 titulos internos | 13 | 16 | 9.60 | 9.60 |
| FIG02 minimo general | 9 | 13.5 | 8.10 | 8.16 |
| FIG02 ticks/categorias/leyenda | 9-11 | 15 | 9.00 | 9.12 |
| FIG02 titulo del eje x | 11 | 17 | 10.20 | 10.08 |
| FIG02 titulo del eje y | 17 | 17 | 10.20 | 10.08 |
| FIG03 floor general | 14.5 | 14.5 | 8.70 | 8.64 |
| FIG03 seis titulos de panel | 14.5 efectivo | 16 | 9.60 | 9.60 |

La escala vectorial final es de 120 drawing units/in. Para PNG se uso la fuente realmente rasterizada, `round(size*2.5)` px a 300 dpi. El PNG FIG02 conserva el redondeo a 1688 px exigido por el contrato. Una comprobacion de cajas de texto con Arial regular/negrita sobre los tres SVG no detecto texto fuera de sus limites ni pares solapados; la etiqueta rotada del eje y de FIG02 se comprobo tambien visualmente. Los seis renders se inspeccionaron visualmente.

## Invariantes por figura

- FIG01: viewBox `0 0 1000 1250`, tres paneles; A conserva 5 metricas x 4 brazos y cero CI arm-level; B conserva 15 contrastes pareados y CI congelado 99%; C conserva el unico contraste Recall@200-Recall@100 con CI congelado 95% e identidad Hierarchical (Attempt06). No hay marks confirmatorios Pool@200 ni p-values. Los rangos A `[0,1]`, B/C `[-0.1,1]` y sus lineas cero no cambiaron. Se aumento tipografia, se ajustaron textos del eje/encabezado y se separo la leyenda. Solo cuatro simbolos **decorativos** de esa leyenda cambiaron de x; todos los marks, CI, ejes y demas elementos no textuales tienen atributos identicos al SVG de `MAIN_BASE`.
- FIG02: viewBox `0 0 1200 675`, un panel, 15 marks, cuatro variantes formales y `hierarchical_70_dual_backfill_30` solo contextual; profundidades 50/100/200, eje y `[0,0.35]`, cero CI, p-values, lineas conectoras y marks ordinarios de diagnostic union. Se elevaron textos de ejes, ticks, leyenda y auxiliares, con microajustes solo de texto. **Todos** los elementos no textuales son identicos al SVG de `MAIN_BASE`.
- FIG03: viewBox `0 0 1200 800`, seis paneles y 31 corridas observadas (10/5/5/10/1), orden H25/H50-D1/H50-D2/H75/H100 ref., rango `[0,1]` en cada panel; sin resumenes, jitter vertical, CI, p-values ni regresion. Se elevaron exclusivamente los seis titulos Top1/Top3/Top5/Top10/Top50/MRR a 16 unidades. Todos los elementos no textuales, incluidos radio y jitter horizontal, son identicos al SVG de `MAIN_BASE`; las observaciones siguen discernibles.

Las secuencias de contenido de los textos SVG son identicas al baseline en las tres figuras. El conteo de elementos SVG tambien se conserva (FIG01 186, FIG02 58, FIG03 304). Las fuentes cientificas y el registry no estan en el diff, de modo que no hay cambio de metricas, denominadores, CI ni claims.

## Determinismo y ledger

Se ejecutaron los tres renderizadores corregidos dos veces consecutivas con el Python local existente, sin instalar ni descargar dependencias. Los SHA-256 de run1 y run2 coincidieron para los seis outputs. Los PNG conservan 300 dpi (metadata leida como 299.9994 por conversion de unidades) y dimensiones contractuales.

Para el ledger se prepararon los nueve scripts/outputs cambiados en el indice Git y se calcularon SHA-256 y tamanos desde `git show :path`, no desde archivos CRLF del workspace. Despues del commit se valido independientemente cada fila contra `git show HEAD:path`: 16/16 SHA-256 y 16/16 tamanos. El inventario sigue siendo de 16 entidades y todas declaran `CANONICAL_GIT_CONTENT_BYTES`.

## Gobernanza

El candidato cientifico `3390878a62ce32ba0e6f4fce69a394c903f5ff11` se publico solo en `origin/figures/g6-f03-accessibility-remediation-v01`; no se integro a `main`. La rama `docs/fichas-grupos-3-8` avanzo desde `87d446197096b3b6ecf8280277637afe67d5dc29` a `031c94037939d57c6cf1224e81bf713f3541cd12`, modificando unicamente su registro de estado: G6-F02 sigue cerrado cientificamente, G6-F03 espera auditoria externa y G7-F01 permanece desautorizado. Los tres untracked historicos del workspace quedaron sin anadir, borrar ni modificar. No se ejecuto G6-F03, no se crearon captions finales y no se cerro Grupo 6.
