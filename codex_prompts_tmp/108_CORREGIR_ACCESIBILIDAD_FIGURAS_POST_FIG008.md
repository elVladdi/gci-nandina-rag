# PROMPT108 — CORREGIR ACCESIBILIDAD DE LAS TRES FIGURAS TRAS FIG008

## 0. Rol y objetivo

Actúa como **CODEX ejecutor reproducible** del proyecto `elVladdi/gci-nandina-rag`.

Debes realizar exclusivamente una **remediación técnica consolidada de accesibilidad** sobre las tres figuras ya integradas de Grupo 6, siguiendo la auditoría científico-visual FIG008.

Esta operación NO reabre resultados científicos, NO ejecuta G6-F03, NO crea captions finales y NO cierra Grupo 6. Su único objetivo es generar un **candidato técnico correctivo** de los artefactos gráficos y sus scripts/ledger para posterior auditoría independiente de la IA Experimental.

No autoapruebes el candidato.

---

## 1. Workspace canónico obligatorio

Trabaja exclusivamente en:

```text
C:\Users\Vladimir\OneDrive\Documentos\Maestría UNMSM\LLM_RGA_NANDINA
```

Antes de cualquier modificación registra:

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

1. el workspace no es el canónico;
2. `origin` no corresponde a `elVladdi/gci-nandina-rag`;
3. `origin/main` no es exactamente `71b13caf6b97e254b4c701b23318bcb0682714bd` al iniciar;
4. existen modificaciones tracked preexistentes no explicadas;
5. no puedes preservar los untracked preexistentes sin tocarlos.

Los untracked históricos conocidos (`Referencias/Antecedentes/`, `Referencias/Glosario/`, `data/Series - Descripciones.xlsx`) no deben añadirse, borrarse ni modificarse.

---

## 2. Estado vinculante de entrada

```text
MAIN_BASE = 71b13caf6b97e254b4c701b23318bcb0682714bd
G6_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G6_F02 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G6_F03 = ACTIVE / AUTHORIZED / REVISION_REQUIRED_G6_F02_ARTIFACT
GROUP6 = IN_PROGRESS / NOT_CLOSED
G7_F01 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
```

La corrección es un **post-closure technical artifact remediation** originado por la auditoría de accesibilidad de G6-F03. No cambies la disposición científica de G6-F02 ni declares que G6-F03 está ejecutado o aprobado.

---

## 3. Fuentes rectoras obligatorias

### 3.1 Auditoría científico-visual vinculante para esta corrección

```text
figure_prompts_tmp/FIG008_RESPUESTA_AUDITORIA_ACCESIBILIDAD_POST_PROMPT107_Y_ESPECIFICACION_CORRECTIVA.md
commit = cbb248ed87836a8c31978344fda08021dc0ea2d2
```

Debes leerla íntegramente antes de editar.

### 3.2 Registry científico-visual integrado

```text
outputs/figures/group6/g6_figure_spec_registry_v0.1.json
blob esperado = 44cc30fc3c38639c6aa4370cb6f317458041f1b1
```

El registry NO debe modificarse.

### 3.3 Artefactos y scripts actuales

```text
figures/group6/g6_fig_01_he2.svg
figures/group6/g6_fig_01_he2.png
src/figures/group6/render_g6_fig_01_he2.py

figures/group6/g6_fig_02_phase_e.svg
figures/group6/g6_fig_02_phase_e.png
src/figures/group6/render_g6_fig_02_phase_e.py

figures/group6/g6_fig_03_exp11a.svg
figures/group6/g6_fig_03_exp11a.png
src/figures/group6/render_g6_fig_03_exp11a.py

outputs/figures/group6/g6_figure_hash_ledger_v0.1.csv
```

### 3.4 Antecedentes de control

```text
codex_prompts_tmp/107_RESPUESTA_CERRAR_G6_F02_Y_EJECUTAR_G6_F03_CAPTIONS_ACCESIBILIDAD.md@7e46f10ba42dc2ea54562da1c1f0dffb9ee2bf9f
figure_prompts_tmp/FIG007_RESPUESTA_PREAUDITORIA_VISUAL_CANDIDATO_G6_F02.md
```

---

## 4. Rama correctiva

Desde `origin/main = 71b13caf6b97e254b4c701b23318bcb0682714bd` crea una rama nueva:

```text
figures/g6-f03-accessibility-remediation-v01
```

Debe tener como parent exacto el `MAIN_BASE` anterior.

No reutilices ni reescribas `figures/g6-f02-render-v01`.

No integres a `main` durante este prompt.

---

# 5. Alcance exacto de la corrección

La corrección debe limitarse a los siguientes 10 paths:

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

`CHANGED_PATH_COUNT` acumulado de este candidato respecto de `MAIN_BASE` debe ser exactamente 10.

No modifiques:

- registry de G6-F01;
- fuentes de Grupo 3/4/5;
- datasets;
- resultados experimentales;
- Plan Maestro;
- tesis;
- artículo;
- requirements;
- `.gitattributes`;
- ninguna ficha científica.

---

# 6. Corrección obligatoria G6-FIG-01

## 6.1 Tamaño físico SVG

Conserva:

```text
viewBox = 0 0 1000 1250
PNG = 2500 x 3125 px / 300 dpi
```

Declara el SVG con dimensiones físicas coherentes con el PNG:

```text
width = 8.333333333333334in
height = 10.416666666666666in
```

Se admite redondeo decimal equivalente que preserve exactamente la escala de `120 drawing units/in`.

No resuelvas el problema alterando solo metadata DPI ni ampliando artificialmente el tamaño editorial.

## 6.2 Tipografía

Debe cumplirse simultáneamente:

```text
ALL_NONEMPTY_TEXT_EFFECTIVE_PNG_PT >= 8.0
ALL_NONEMPTY_TEXT_EFFECTIVE_SVG_PT >= 8.0
AXIS_AND_TICK_EFFECTIVE_PT = target 8.5–9.0 or higher without breaking hierarchy
```

Con 120 drawing units/in, usa como floor técnico seguro:

```text
GENERAL_TEXT_FLOOR = 13.5 drawing units
```

porque:

```text
SVG = 13.5/120*72 = 8.10 pt
PNG = round(13.5*2.5)=34 px -> 8.16 pt @300dpi
```

Para ticks y títulos de eje usa como objetivo preferente:

```text
15 drawing units ≈ 9.0 pt SVG / 9.12 pt PNG
```

Los títulos internos de panel pueden elevarse a 15–16 unidades si hace falta mantener jerarquía visual.

Puedes microajustar posiciones de texto, márgenes y espacios blancos exclusivamente para evitar solapamientos o clipping provocados por la tipografía mayor.

## 6.3 Invariantes científicas G6-FIG-01

Debes preservar exactamente:

```text
panel_count = 3
Panel A = 5 metrics x 4 arms
Panel A arm-level CI = 0
Panel B = 15 paired contrasts
Panel B CI = frozen 99%
Panel C = 1 paired Recall@200-Recall@100 contrast
Panel C CI = frozen 95%
Panel C identity = Hierarchical (Attempt06)
Pool@200 confirmatory marks = 0
p-values = 0
A_x = [0,1]
B_x = [-0.1,1]
C_x = [-0.1,1]
zero reference lines = preserved
```

No cambies valores, posición científica de marks/CI, orden de métricas, comparadores, rangos o semántica.

---

# 7. Corrección obligatoria G6-FIG-02

## 7.1 Tamaño físico SVG

Conserva:

```text
viewBox = 0 0 1200 675
PNG = 3000 x 1688 px / 300 dpi
```

Declara el SVG en escala física de 120 drawing units/in:

```text
width = 10.0in
height = 5.625in
```

La diferencia mínima causada por el redondeo del raster a 1688 px es aceptable; no deformes el aspect ratio para hacerla desaparecer.

## 7.2 Títulos de ejes

El registry exige al menos 10 pt para axis labels.

Mantén el título de eje y en 17 unidades y fuera del campo de datos.

Eleva:

```text
Recovery depth (ordered categories)
```

hasta al menos:

```text
17 drawing units
```

que produce aproximadamente 10.2 pt SVG y 10.08 pt PNG.

## 7.3 Ticks y leyenda

La recomendación de 9 pt debe satisfacerse en esta misma intervención, según FIG008.

Usa como objetivo:

```text
15 drawing units
```

para:

- ticks del eje y;
- categorías 50 / 100 / 200;
- entradas de leyenda de las cinco variantes.

Los textos auxiliares actualmente de 9–10 unidades deben elevarse preferentemente al floor general de legibilidad de 13.5 unidades cuando el espacio lo permita, sin alterar semántica. Puedes usar line breaks ya permitidos y redistribución mínima de la caja de leyenda/márgenes para evitar clipping.

## 7.4 Invariantes científicas G6-FIG-02

Preserva exactamente:

```text
panel_count = 1
mark_count = 15
formal variants = 4
context-only variant = hierarchical_70_dual_backfill_30
depths = 50 / 100 / 200
y_range = [0,0.35]
CI = 0
p-values = 0
connecting lines = 0
diagnostic_union ordinary-performance marks = 0
```

La variante 70/30 debe seguir con igual peso visual y marcada solo como contexto descriptivo. No cambies valores, orden por favorabilidad, escalas ni marks.

---

# 8. Corrección obligatoria G6-FIG-03

La paridad física SVG/PNG actual es correcta y debe conservarse:

```text
SVG = 10.0in x 6.666666666666667in
viewBox = 0 0 1200 800
PNG = 3000 x 2000 px / 300 dpi
```

El floor general de `14.5` unidades debe permanecer intacto.

Modifica únicamente los seis títulos de panel:

```text
Top1
Top3
Top5
Top10
Top50
MRR
```

para que se materialicen en:

```text
16 drawing units
```

Resultado esperado:

```text
SVG panel title = 9.60 pt
PNG panel title = 9.60 pt
```

Solo se permite microajuste vertical del título si es necesario para evitar colisión.

Preserva exactamente:

```text
panel_count = 6
observed_run_count = 31
condition_counts = 10 / 5 / 5 / 10 / 1
condition_order = H25 / H50-D1 / H50-D2 / H75 / H100 ref.
y_range_all_panels = [0,1]
summary_marks = 0
vertical_jitter = 0
H100_marks_per_panel = 1
CI = 0
p-values = 0
regression = 0
```

No cambies marker radius ni jitter horizontal aprobado.

---

# 9. Prohibición de drift científico

Antes y después del render verifica y reporta:

```text
SCIENTIFIC_DATA_CHANGE_COUNT = 0
METRIC_CHANGE_COUNT = 0
CI_CHANGE_COUNT = 0
DENOMINATOR_CHANGE_COUNT = 0
CLAIM_CHANGE_COUNT = 0
NEW_INFERENCE_COUNT = 0
NEW_P_VALUE_COUNT = 0
FIGURE_COUNT = 3
```

Para cada SVG compara el artefacto corregido contra `MAIN_BASE` y demuestra que los cambios son tipográficos/espaciales/declaración física. En lo posible:

- los elementos no textuales de datos deben conservar exactamente sus coordenadas;
- si un microajuste de márgenes obliga a mover texto, no muevas marks, CI ni escalas científicas;
- cualquier diferencia no textual debe explicarse y debe ser exclusivamente decorativa/no científica.

STOP si para cumplir accesibilidad necesitas cambiar un valor científico, escala, rango, posición científica de un mark/CI o contenido de fuente.

---

# 10. Determinismo y validación

Ejecuta consecutivamente dos veces cada script corregido usando el runtime existente. No instales ni descargues dependencias.

Los SVG y PNG de run1/run2 deben ser byte-idénticos por figura.

Verifica al menos:

### FIG01

```text
all nonempty text >= 8.0 pt PNG and SVG
axis/tick target >= 8.5 pt
no text overlap/clipping
all 15 Panel-B contrasts preserved
Panel-A arm CI count = 0
Panel-C estimate count = 1
Pool@200 confirmatory mark count = 0
```

### FIG02

```text
x-axis title >= 10 pt PNG and SVG
y-axis title >= 10 pt PNG and SVG
ticks/legend >= 9 pt PNG and SVG
mark_count = 15
connecting lines = 0
CI = 0
p-values = 0
no overlap/clipping
```

### FIG03

```text
minimum effective font >= 8.5 pt
six panel titles >= 9.5 pt
observed_run_count = 31
summary marks = 0
vertical jitter = 0
observations discernible = true
no overlap/clipping
```

Incluye en el reporte una tabla de tamaños efectivos finales por clase tipográfica relevante.

---

# 11. Ledger canónico

Regenera `outputs/figures/group6/g6_figure_hash_ledger_v0.1.csv` después de producir los scripts y renders finales.

Mantén la semántica corregida previamente:

```text
hash_semantics = CANONICAL_GIT_CONTENT_BYTES
```

Los hashes y tamaños deben calcularse sobre bytes canónicos Git, no sobre una materialización CRLF del workspace.

El ledger debe continuar cubriendo exactamente su inventario canónico de 16 entidades, actualizando los hashes/tamaños de los scripts/renders que cambien y preservando los inputs/registry que no cambian.

Antes de publicar el candidato, verifica independientemente contra el commit candidato:

```text
LEDGER_ROW_COUNT = 16
LEDGER_CANONICAL_SHA256_MATCH_COUNT = 16
LEDGER_CANONICAL_SIZE_MATCH_COUNT = 16
```

No confundas SHA-256 de contenido con Git blob SHA.

---

# 12. Commit candidato

Crea **un solo commit candidato** sobre la nueva rama:

```text
figures/g6-f03-accessibility-remediation-v01
```

Parent exacto:

```text
71b13caf6b97e254b4c701b23318bcb0682714bd
```

El commit debe contener únicamente los 10 paths autorizados.

Publícalo en `origin`.

No hagas merge a `main`.

No hagas amend, rebase, force-push, squash o cherry-pick.

---

# 13. Registro de fichas

Después de publicar el candidato, sobre `docs/fichas-grupos-3-8` partiendo de:

```text
87d446197096b3b6ecf8280277637afe67d5dc29
```

actualiza únicamente:

```text
docs/fichas/grupos_3_8/04_REGISTRO_ESTADO_FICHAS.md
```

Añade un bloque de trazabilidad de la remediación, sin cambiar cierres científicos previos:

```text
FICHA = G6-F03
PREVIOUS_AUDIT_OUTCOME = REVISION_REQUIRED_G6_F02_ARTIFACT
FIG008_RESPONSE_COMMIT = cbb248ed87836a8c31978344fda08021dc0ea2d2
ACCESSIBILITY_REMEDIATION_BRANCH = figures/g6-f03-accessibility-remediation-v01
ACCESSIBILITY_REMEDIATION_CANDIDATE = <commit>
ACCESSIBILITY_REMEDIATION_PARENT = 71b13caf6b97e254b4c701b23318bcb0682714bd
CORRECTED_FIGURE_COUNT = 3
SCIENTIFIC_DATA_CHANGE_COUNT = 0
G6_F02_SCIENTIFIC_STATE = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G6_F03_STATE = ACTIVE / AUTHORIZED / CORRECTIVE_CANDIDATE_PENDING_EXTERNAL_AUDIT
GROUP6 = IN_PROGRESS / NOT_CLOSED
G7_F01_AUTHORIZED = false
PENDING_EXTERNAL_AUDIT = true
```

No modifiques el Plan Maestro en este prompt.

---

# 14. Respuesta oficial

Publica una respuesta en:

```text
codex_prompts_tmp/108_RESPUESTA_CORREGIR_ACCESIBILIDAD_FIGURAS_POST_FIG008.md
```

La respuesta debe incluir obligatoriamente:

```text
PROMPT108_EXECUTION
WORKSPACE_CONTRACT
MAIN_BASE
FIG008_RESPONSE_COMMIT
CORRECTION_BRANCH
CORRECTION_CANDIDATE_COMMIT
CORRECTION_PARENT
CHANGED_PATH_COUNT
CHANGED_PATHS
FIG01_ACCESSIBILITY_RESULT
FIG02_ACCESSIBILITY_RESULT
FIG03_ACCESSIBILITY_RESULT
FIG01_MIN_FONT_PNG_PT
FIG01_MIN_FONT_SVG_PT
FIG02_X_AXIS_PNG_PT
FIG02_X_AXIS_SVG_PT
FIG02_TICK_LEGEND_MIN_PNG_PT
FIG02_TICK_LEGEND_MIN_SVG_PT
FIG03_PANEL_TITLE_PNG_PT
FIG03_PANEL_TITLE_SVG_PT
DETERMINISM_CHECK
LEDGER_ROW_COUNT
LEDGER_CANONICAL_SHA256_MATCH_COUNT
LEDGER_CANONICAL_SIZE_MATCH_COUNT
SCIENTIFIC_DATA_CHANGE_COUNT
METRIC_CHANGE_COUNT
CI_CHANGE_COUNT
DENOMINATOR_CHANGE_COUNT
CLAIM_CHANGE_COUNT
NEW_INFERENCE_COUNT
NEW_P_VALUE_COUNT
FICHAS_FINAL
MAIN_FINAL
PLAN_FINAL
G6_F03_FINAL_STATE
GROUP6_FINAL_STATE
G7_F01_FINAL_STATE
EXTERNAL_AUDIT
```

Incluye además:

1. inventario exacto de cambios por figura;
2. tabla before/after de tamaños tipográficos relevantes;
3. verificación de invariantes científicos por figura;
4. determinismo;
5. ledger;
6. gobernanza final.

---

# 15. Estado terminal obligatorio

Si todo cumple:

```text
PROMPT108_EXECUTION = COMPLETE
G6_F03_FINAL_STATE = ACTIVE / AUTHORIZED / CORRECTIVE_CANDIDATE_PENDING_EXTERNAL_AUDIT
GROUP6_FINAL_STATE = IN_PROGRESS / NOT_CLOSED
G7_F01_FINAL_STATE = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
EXTERNAL_AUDIT = PENDING
```

Si cualquier requisito no puede satisfacerse sin drift científico o sin salir del scope:

```text
PROMPT108_EXECUTION = STOPPED
RESULT = REVISION_REQUIRED
```

y documenta exactamente el motivo.

En ambos casos, **detente**. No reanudes G6-F03, no crees captions finales, no cierres Grupo 6 y no actives G7.
