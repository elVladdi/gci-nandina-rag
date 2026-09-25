# FIG009 — Respuesta: reanudar G6-F03, captions, autosuficiencia y cierre visual

## 1. DICTAMEN_TERMINAL

```text
FIG009_RESULT = PASS_READY_FOR_EXTERNAL_AUDIT
NEXT_ACTOR = IA_EXPERIMENTAL
MAIN_AUDITED = 3390878a62ce32ba0e6f4fce69a394c903f5ff11
ACCESSIBILITY_REMEDIATION = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G6_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G6_F02 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G6_F03 = ACTIVE / AUTHORIZED / EXECUTION_PENDING
GROUP6_CLOSED = false
G7_F01_AUTHORIZED = false
SCIENTIFIC_DATA_CHANGE_COUNT = 0
NEW_INFERENCE_COUNT = 0
NEW_CI_COUNT = 0
NEW_P_VALUE_COUNT = 0
EXP12_REOPENED = false
ARTICLE_MODIFIED = false
THESIS_MODIFIED = false
```

La auditoría científico-visual final no identifica un defecto técnico nuevo que requiera volver a editar SVG, PNG o scripts. Las tres figuras integradas conservan sus contratos científicos, las restricciones de incertidumbre, la semántica de marks y los límites de interpretación aprobados. La remediación tipográfica integrada en `main=3390878a62ce32ba0e6f4fce69a394c903f5ff11` satisface los objetivos fijados por FIG008 para G6-FIG-01, G6-FIG-02 y G6-FIG-03.

Los captions propuestos a continuación son autosuficientes y no introducen claims, resultados, inferencia o disposiciones de hipótesis nuevas. Esta respuesta no materializa `g6_caption_registry_v0.1.md`, no escribe `group6_closure_v0.1.json`, no cierra Grupo 6 y no activa G7-F01.

---

## 2. Fuentes exactas revisadas

### 2.1 Estado rector y ficha

```text
main = 3390878a62ce32ba0e6f4fce69a394c903f5ff11

docs/fichas/grupos_3_8/04_REGISTRO_ESTADO_FICHAS.md
  branch = docs/fichas-grupos-3-8
  current G6-F03 = ACTIVE / AUTHORIZED / EXECUTION_PENDING

docs/fichas/grupos_3_8/grupo_6/G6_F03_CAPTIONS_ACCESIBILIDAD_Y_CIERRE.md
  git blob = 68432ee2383cb510fcbd3267a592a8c2cd5b854d
```

La etiqueta histórica `PROSPECTIVE / NOT_AUTHORIZED` contenida dentro de la ficha rectora no sustituye al registro de estado vivo posterior a Prompt109; para esta ejecución se aplica el estado vinculante fijado por FIG009 y confirmado por el registro actual.

### 2.2 Registry, ledger y artefactos finales

```text
outputs/figures/group6/g6_figure_spec_registry_v0.1.json
  governing git blob = 44cc30fc3c38639c6aa4370cb6f317458041f1b1

outputs/figures/group6/g6_figure_hash_ledger_v0.1.csv
  current git blob = bfcbfe8a2232246476979506377ff3005166253f
  row count = 16
  hash semantics = CANONICAL_GIT_CONTENT_BYTES
```

G6-FIG-01:

```text
figures/group6/g6_fig_01_he2.svg
  git blob = f57511c1ddbed5d2177e7cf7b5c9a4a180a3c7e3
  ledger SHA-256 = 534aade80e669db62d86764d2b1695d26654c1d042144ef141f462983d422ca8

figures/group6/g6_fig_01_he2.png
  ledger SHA-256 = 3136a814647384eaa1f85c2ce90033a78dde48b661d0b1c078e5b272c6e85d6f
  dimensions = 2500 x 3125 px @ 300 dpi

src/figures/group6/render_g6_fig_01_he2.py
  git blob = 678d5fd49b3bd090c7d7729702741e6dcfe293fa
```

G6-FIG-02:

```text
figures/group6/g6_fig_02_phase_e.svg
  git blob = ec164ea41ab8605edf198c03785db63c442c1b64
  ledger SHA-256 = 02de449d911dfbca9863997671751ac2480880646c45e31c8b7549584b0fabc6

figures/group6/g6_fig_02_phase_e.png
  ledger SHA-256 = 867ca35d0c454a38bd122c6ecdf5bb693f98f86206828bd68c051aa263c7791f
  dimensions = 3000 x 1688 px @ 300 dpi

src/figures/group6/render_g6_fig_02_phase_e.py
  git blob = e9dafe41e3b22cb1c8d09da08a723925cd300b7d
```

G6-FIG-03:

```text
figures/group6/g6_fig_03_exp11a.svg
  ledger SHA-256 = a4a81b565ed2ceb22f23f9a52888e802b1e749186fb43d3bd71faf1b31d5f7c3

figures/group6/g6_fig_03_exp11a.png
  ledger SHA-256 = 3c4bcf736b56fbc9ffd054562db0eea31be195792f2bade611a9e5205dfa97de
  dimensions = 3000 x 2000 px @ 300 dpi

src/figures/group6/render_g6_fig_03_exp11a.py
  git blob = 1723f139afd308c4966846247ffe4d2f330a0d4e
```

### 2.3 Tablas canónicas de Grupo 5

Se revisaron directamente:

```text
outputs/results/group5/g5_table_registry_v0.1.json
  git blob = 4fe9318d52fad093066ff9f42d524fc95e436245

docs/results/group5/g5_canonical_tables_v0.1.md
  git blob = 9f63767b1b93166a8e6bfd2685eaee4f4ae44a4d

docs/results/group5/g5_appendix_registry_v0.1.md
  git blob = 9e2e8a5fb1a7e1fa9e4b252611703cd0d848ee0a

outputs/results/group5/tables/g5_main_01_he2a_primary_early_ranking.csv
  git blob = cb68583ee2260e4455796bac99ad90995ca7ef92

outputs/results/group5/tables/g5_main_02_he2b_deep_coverage.csv
  git blob = 359e4e19b5ef1d44983c03039162209293b2a44c

outputs/results/group5/tables/g5_secondary_01_phase_e_descriptive.csv
  git blob = fa961cf3d6198ddba6a6b5eeadcc9a23c8801f61

outputs/results/group5/tables/g5_appendix_02_exp11a_size_composition_sensitivity.csv
  git blob = cf3aedab5935d6af9b3ac7be7b51b954fcb9c403
```

### 2.4 Claims, límites e inferencia

Se revisaron directamente:

```text
outputs/analysis/group4/g4_result_claim_evidence_matrix_v0.1.json
  git blob = cc5d85bad5d0a2610ffb086f99052fd344b6d8ab

docs/analysis/group4/g4_interpretation_synthesis_v0.1.md
  git blob = 129a67b15db429b86af059d61753b1942c8f243f

outputs/analysis/group4/g4_limitations_registry_v0.1.json
  git blob = ae00b93431e912cb78a58344057d9bf7a51fcd47

docs/analysis/group4/g4_literature_contrast_v0.1.md
  git blob = 2baff53184b17c23380693235a2f3257de5e2bba

outputs/analysis/group3/g3_hypothesis_disposition_v0.1.json
  git blob = d8f20498ebd26e467ba1916e3e0ed93d1dd06c61

outputs/analysis/group3/g3_inferential_results_v0.1.json
  git blob = f99b7e46d81b28ca2b7cfce8d24788ad14156dcc

docs/analysis/group3/g3_inferential_methods_and_checks_v0.1.md
  git blob = 6cf424c9cf8aa7371dbbf5b8baaf7305cc66a436
```

### 2.5 Antecedentes de accesibilidad

```text
figure_prompts_tmp/FIG008_RESPUESTA_AUDITORIA_ACCESIBILIDAD_POST_PROMPT107_Y_ESPECIFICACION_CORRECTIVA.md
  commit = cbb248ed87836a8c31978344fda08021dc0ea2d2

codex_prompts_tmp/108_RESPUESTA_CORREGIR_ACCESIBILIDAD_FIGURAS_POST_FIG008.md
  current branch source reviewed

codex_prompts_tmp/109_RESPUESTA_INTEGRAR_REMEDIACION_ACCESIBILIDAD_Y_REANUDAR_G6_F03.md
  current branch source reviewed
```

Prompt108 documenta determinismo 6/6, ledger canónico 16/16 y las medidas físicas corregidas; Prompt109 confirma que el candidato correctivo fue integrado a `main` por fast-forward exacto y deja G6-F03 activo para esta auditoría sustantiva.

---

## 3. Auditoría de G6-FIG-01 — HE2

### 3.1 Fidelidad científica

```text
scientific_role = PRIMARY_INFERENTIAL
destination = MAIN
benchmark = 1,056 series / 67 DAM / 42 NANDINA
panel_count = 3
```

**Panel A.** El script y el SVG preservan cinco métricas primarias en orden congelado: `Top-1`, `Top-3`, `Top-5`, `Top-10`, `MRR@100`. Historical se muestra una vez por métrica después de verificar identidad exacta de sus tres repeticiones estructurales; Flat, Hierarchical y D1a corresponden exclusivamente al estado corregido Attempt06. No existe CI por brazo.

**Panel B.** Se representan exactamente los 15 contrastes `Historical - comparator`, tres comparadores × cinco métricas. Los whiskers se enlazan exclusivamente a los CI congelados de 99% de la diferencia pareada. La referencia cero permanece visible y el eje conserva `[-0.1, 1]`.

**Panel C.** Se representa exactamente un contraste `Recall@200 - Recall@100`, identidad `Hierarchical (Attempt06)`, con su único CI congelado de 95%. `Recall@100` y `Recall@200` aparecen solo como contexto. `Pool@200` no aparece como segundo estimando confirmatorio. No hay p-values.

Los valores y denominadores coinciden con G5-MAIN-01/G5-MAIN-02 y con G3-F03. No se detecta cambio de métrica, CI, denominador o interpretación.

### 3.2 Accesibilidad integrada

El SVG final declara:

```text
width = 8.333333333333334 in
height = 10.416666666666666 in
viewBox = 0 0 1000 1250
```

La escala física vectorial es `120 drawing units/in`. El mínimo de texto no vacío materializado es `13.5` unidades:

```text
13.5 / 120 * 72 = 8.10 pt SVG
```

El PNG usa `round(13.5 * 2.5) = 34 px` a 300 dpi:

```text
34 / 300 * 72 = 8.16 pt PNG
```

Por tanto:

```text
mandatory minimum >= 8 pt = PASS
```

Los ticks y títulos de eje se materializan a 15 unidades:

```text
15 / 120 * 72 = 9.00 pt SVG
round(15 * 2.5)=38 px -> 9.12 pt PNG
preferred axis/tick ~8.5–9 pt = PASS
```

Los títulos internos se materializan a 16 unidades = 9.6 pt. La leyenda y los comparadores conservan forma redundante además del color: círculo, cuadrado, triángulo y diamante. No se observan IDs internos como título visible de publicación. Los límites del `viewBox`, las posiciones finales de ejes/leyenda y la anotación de contexto mantienen margen suficiente; no se detecta clipping ni solapamiento material nuevo.

```text
FIG01_SCIENTIFIC_FIDELITY = PASS
FIG01_ACCESSIBILITY = PASS
FIG01_CAPTION_READINESS = PASS
```

---

## 4. Auditoría de G6-FIG-02 — Phase E

### 4.1 Fidelidad científica

```text
scientific_role = DESCRIPTIVE_SUPPLEMENTARY
panel_count = 1
mark_count = 15
formal_variants = 4
context_only_variant = hierarchical_70_dual_backfill_30
depths = 50 / 100 / 200
y_range = [0, 0.35]
CI = 0
p_values = 0
connecting_lines = 0
diagnostic_union_ordinary_marks = 0
```

El script exige exactamente 15 filas y excluye explícitamente `diagnostic_union_hierarchical_dual`. Los cuatro miembros formales son `hierarchical_only`, `dual_only`, `hierarchical_first_100` y `hierarchical_80_dual_backfill_20`; `hierarchical_70_dual_backfill_30` se mantiene como contexto, con hexágono abierto y sin reducción de opacidad o tamaño. El eje y parte de cero y conserva `[0,0.35]`. No hay líneas entre profundidades ni inferencia visual implícita.

Los 15 valores coinciden con G5-SECONDARY-01. La figura continúa siendo descriptiva y no modifica la evidencia confirmatoria ni `HE2 = SUPPORTED`.

### 4.2 Accesibilidad integrada

El SVG final declara:

```text
width = 10.0 in
height = 5.625 in
viewBox = 0 0 1200 675
```

Escala física: `120 drawing units/in`.

Ejes:

```text
x-axis title = 17 units -> 10.20 pt SVG / 10.08 pt PNG
y-axis title = 17 units -> 10.20 pt SVG / 10.08 pt PNG
axis-title minimum >=10 pt = PASS
```

Ticks y entradas nominales de leyenda:

```text
15 units -> 9.00 pt SVG
round(15*2.5)=38 px -> 9.12 pt PNG
tick/legend target >=9 pt = PASS
```

Los rótulos `Formal claim variants` y `Context only` funcionan como encabezados de agrupación, no como entradas nominales de leyenda; están a 13.5 unidades = 8.10/8.16 pt y no reducen la legibilidad de las entradas, que sí alcanzan 9 pt. Los textos auxiliares también permanecen por encima del floor general adoptado en la remediación.

La etiqueta vertical `Exact-NANDINA coverage` permanece fuera del campo de datos. Las cinco variantes conservan formas distintas y la variante contextual mantiene peso visual. No se observa clipping o solapamiento material en las posiciones finales. El eje parte de cero y no magnifica diferencias mediante truncación.

```text
FIG02_SCIENTIFIC_FIDELITY = PASS
FIG02_ACCESSIBILITY = PASS
FIG02_CAPTION_READINESS = PASS
```

---

## 5. Auditoría de G6-FIG-03 — EXP11A

### 5.1 Fidelidad científica

```text
scientific_role = DESCRIPTIVE_SENSITIVITY / NONCAUSAL
destination = APPENDIX
metrics = Top1 / Top3 / Top5 / Top10 / Top50 / MRR
panel_count = 6
observed_run_count = 31
condition_counts = 10 / 5 / 5 / 10 / 1
condition_order = H25 / H50-D1 / H50-D2 / H75 / H100 ref.
y_range = [0,1]
summary_marks = 0
CI = 0
p_values = 0
regression = 0
vertical_jitter = 0
H100 = one frozen reference per panel
```

El script verifica 31 filas `OBSERVED_RUN` y seis `FROZEN_CONDITION_SUMMARY`; solo las 31 observaciones se grafican. H50-D1 y H50-D2 se derivan del `dominant_stratum` congelado. H100 se representa una sola vez por panel mediante diamante y no como distribución de réplicas. El jitter es exclusivamente horizontal y determinista; el valor y de cada mark deriva directamente de la métrica observada.

El contenido coincide con G5-APPENDIX-02 y con G3C-007: EXP11A es sensibilidad conjunta tamaño/composición y no permite aislar causalmente ni asumir monotonía del tamaño.

### 5.2 Accesibilidad integrada

El SVG final declara:

```text
width = 10.0 in
height = 6.666666666666667 in
viewBox = 0 0 1200 800
```

El floor efectivo es 14.5 unidades:

```text
14.5 / 120 * 72 = 8.70 pt SVG
round(14.5*2.5)=36 px -> 8.64 pt PNG
minimum effective font >=8.5 pt = PASS
```

Los seis títulos de panel se materializan a 16 unidades:

```text
16 / 120 * 72 = 9.60 pt SVG
40 px / 300 * 72 = 9.60 pt PNG
panel-title target >=9.5 pt = PASS
```

Las categorías permanecen horizontales. Para H25/H75 la separación horizontal determinista entre centros es 6.4 unidades con radio 2.2; para H50-D1/D2 es 9.6 unidades. Esto preserva discernibilidad de observaciones incluso cuando comparten valores y próximos. No existe jitter vertical. La línea punteada antes de H100 es una separación contextual, no una codificación de inferencia. No se detecta clipping o solapamiento material nuevo ni dependencia exclusiva del color para identificar H100, que además usa diamante sólido.

```text
FIG03_SCIENTIFIC_FIDELITY = PASS
FIG03_ACCESSIBILITY = PASS
FIG03_CAPTION_READINESS = PASS
```

---

## 6. Auditoría transversal de accesibilidad y autosuficiencia

| Control | G6-FIG-01 | G6-FIG-02 | G6-FIG-03 |
|---|---|---|---|
| population / denominator identifiable | PASS | PASS | PASS |
| metric/evidence family identifiable | PASS | PASS | PASS |
| uncertainty role explicit | PASS | PASS | PASS |
| descriptive vs inferential role explicit | PASS | PASS | PASS |
| material limitation explicit | PASS | PASS | PASS |
| caption matches visible panels/marks | PASS | PASS | PASS |
| minimum effective font | PASS | PASS | PASS |
| axis/legend targets | PASS | PASS | PASS |
| marker discrimination | PASS | PASS | PASS |
| color is not sole required encoding | PASS | PASS | PASS |
| material clipping | NOT DETECTED | NOT DETECTED | NOT DETECTED |
| material label overlap | NOT DETECTED | NOT DETECTED | NOT DETECTED |
| misleading axis truncation | NONE | NONE | NONE |
| internal workflow IDs visible as image titles | NO | NO | NO |
| new scientific claim introduced | NO | NO | NO |

### 6.1 Consistencia con Grupo 5

```text
G6-FIG-01:
  G5-MAIN-01 = 15 HE2_A rows
  G5-MAIN-02 = 1 HE2_B row
  values/CI/denominators = consistent

G6-FIG-02:
  G5-SECONDARY-01 = 15 rows = 5 variants x 3 depths
  formal/context role = consistent

G6-FIG-03:
  G5-APPENDIX-02 = 31 observed runs + 6 frozen summaries
  plotted summaries = 0
  condition counts = 10/5/5/10/1
```

```text
CANONICAL_TABLE_CONSISTENCY = PASS
```

### 6.2 Consistencia con Grupo 4

Se preservan los claims y restricciones relevantes:

```text
G3C-001:G3C-003 = historical retrieval superiority inside frozen HE2_A benchmark only
G3C-004 = one hierarchical Recall@200 - Recall@100 primary contrast
G3C-005 = Phase E descriptive only; no confirmatory promotion
G3C-007 = EXP11A joint size/composition sensitivity / NONCAUSAL
```

No se formula exactitud global del RAG, causalidad, corrección jurídica, superioridad externa, efecto aislado de tamaño ni inferencia a elementos no autorizados.

```text
CLAIM_SCOPE_CONSISTENCY = PASS
```

### 6.3 Consistencia con Grupo 3

```text
HE2_A = 15 primary paired contrasts / 99% CI on paired differences
HE2_B = one primary contrast / 95% CI
arm-level CI = none
Phase E = descriptive / no CI
EXP11A = descriptive sensitivity / no CI
p-values = none
```

```text
UNCERTAINTY_CONSISTENCY = PASS
```

---

## 7. Tres captions finales propuestos

### G6-FIG-01

**Final caption propuesto**

> **Evidencia primaria de HE2 en el benchmark interno offline del Capítulo 87 (1,056 series, 67 DAM y 42 NANDINA).** (A) Valores observados de Historical y de los tres comparadores corregidos Attempt06 en Top-1, Top-3, Top-5, Top-10 y MRR@100; estos valores por brazo son descriptivos y no tienen CI por brazo autorizado. (B) Quince diferencias pareadas `Historical − comparator` correspondientes a las cinco métricas primarias y los tres comparadores, con CI congelados de 99% sobre cada diferencia pareada. (C) Único contraste primario HE2_B del retrieval jerárquico corregido, `Recall@200 − Recall@100`, con CI congelado de 95%; Recall@100 y Recall@200 se muestran únicamente como contexto y Pool@200 no se duplica como evidencia confirmatoria. Los contrastes son no causales, cuantifican incertidumbre dentro del benchmark fijo y no representan exactitud global del framework RAG ni validez externa.

### G6-FIG-02

**Final caption propuesto**

> **Cobertura exacta NANDINA de Phase E según profundidad y variante en el benchmark interno offline del Capítulo 87 (1,056 series, 67 DAM y 42 NANDINA).** Se muestran 15 proporciones descriptivas de cobertura exacta NANDINA: cinco variantes en cada profundidad de recuperación 50, 100 y 200. `hierarchical_only`, `dual_only`, `hierarchical_first_100` y `hierarchical_80_dual_backfill_20` son las cuatro variantes formales `A_historical_defined` asociadas al claim descriptivo G3C-005; `hierarchical_70_dual_backfill_30` se incluye únicamente como contexto descriptivo adicional y no fue seleccionada por favorabilidad ni constituye evidencia confirmatoria. No se presentan CI, p-values, tendencias ajustadas ni contrastes inferenciales. `diagnostic_union_hierarchical_dual` se excluye del rendimiento ordinario porque representa un techo diagnóstico. La figura no modifica la evidencia confirmatoria ni la disposición de HE2.

### G6-FIG-03

**Final caption propuesto**

> **Sensibilidad conjunta del banco histórico a tamaño y composición (EXP11A) en el benchmark interno offline del Capítulo 87 (1,056 series, 67 DAM y 42 NANDINA).** Los seis paneles muestran Top1, Top3, Top5, Top10, Top50 y MRR para 31 corridas observadas distribuidas como H25 (`n=10`), H50-D1 (`n=5`), H50-D2 (`n=5`), H75 (`n=10`) y la referencia congelada H100 (`n=1`). D1 y D2 son composiciones diferenciadas dentro de H50; H25, H75 y H100 conservan asimismo sus composiciones observadas. Cada punto representa una corrida individual y H100 se muestra como una única referencia, no como una distribución de réplicas. EXP11A es una sensibilidad descriptiva y no causal en la que tamaño y composición varían conjuntamente; por ello, las diferencias entre condiciones no identifican un efecto causal aislado ni monotónico del tamaño. No se muestran CI, p-values, regresiones, suavizados ni summaries congelados como marks de la figura.

---

## 8. Propuesta completa de `g6_caption_registry_v0.1.md`

La siguiente es una **propuesta de contenido**, no un archivo materializado.

```markdown
# G6-F03 — Caption Registry v0.1

status: READY_FOR_EXTERNAL_AUDIT
main_source_commit: 3390878a62ce32ba0e6f4fce69a394c903f5ff11
figure_count: 3
caption_count: 3

## G6-FIG-01

figure_id: G6-FIG-01
working_title: Evidencia primaria de HE2: ranking temprano y cobertura profunda
scientific_role: PRIMARY_INFERENTIAL
destination: MAIN

final_caption: **Evidencia primaria de HE2 en el benchmark interno offline del Capítulo 87 (1,056 series, 67 DAM y 42 NANDINA).** (A) Valores observados de Historical y de los tres comparadores corregidos Attempt06 en Top-1, Top-3, Top-5, Top-10 y MRR@100; estos valores por brazo son descriptivos y no tienen CI por brazo autorizado. (B) Quince diferencias pareadas `Historical − comparator` correspondientes a las cinco métricas primarias y los tres comparadores, con CI congelados de 99% sobre cada diferencia pareada. (C) Único contraste primario HE2_B del retrieval jerárquico corregido, `Recall@200 − Recall@100`, con CI congelado de 95%; Recall@100 y Recall@200 se muestran únicamente como contexto y Pool@200 no se duplica como evidencia confirmatoria. Los contrastes son no causales, cuantifican incertidumbre dentro del benchmark fijo y no representan exactitud global del framework RAG ni validez externa.

population_and_denominator: 1,056 series / 67 DAM / 42 NANDINA; benchmark interno offline, Capítulo 87.
metric_or_evidence_family: HE2_A primary early-ranking metrics (Top-1, Top-3, Top-5, Top-10, MRR@100) + HE2_B corrected hierarchical deep-coverage contrast.
uncertainty_statement: Panel A has no authorized arm-level CI; Panel B uses frozen 99% CI only on the 15 paired Historical-minus-comparator differences; Panel C uses one frozen 95% CI on Recall@200-minus-Recall@100; no p-values.
scope_limitation: Noncausal contrasts and cluster-resampling uncertainty inside the fixed internal benchmark; no external validation.
forbidden_interpretation: Do not infer global RAG accuracy, causal superiority, arm-level uncertainty, external-population validity, or duplicate Pool@200 as confirmatory evidence.
source_table_paths:
  - outputs/results/group5/tables/g5_main_01_he2a_primary_early_ranking.csv
  - outputs/results/group5/tables/g5_main_02_he2b_deep_coverage.csv
figure_svg_path: figures/group6/g6_fig_01_he2.svg
figure_png_path: figures/group6/g6_fig_01_he2.png
accessibility_checks:
  - all nonempty text >= 8 pt effective at native vector/raster size
  - axis/tick text approximately 9 pt effective
  - redundant circle/square/triangle/diamond encoding
  - visible zero references in contrast panels
  - no material clipping or label overlap detected
  - no internal workflow ID displayed as publication title
status: READY_FOR_EXTERNAL_AUDIT

## G6-FIG-02

figure_id: G6-FIG-02
working_title: Cobertura exacta NANDINA de Phase E según profundidad y variante
scientific_role: DESCRIPTIVE_SUPPLEMENTARY
destination: SECONDARY

final_caption: **Cobertura exacta NANDINA de Phase E según profundidad y variante en el benchmark interno offline del Capítulo 87 (1,056 series, 67 DAM y 42 NANDINA).** Se muestran 15 proporciones descriptivas de cobertura exacta NANDINA: cinco variantes en cada profundidad de recuperación 50, 100 y 200. `hierarchical_only`, `dual_only`, `hierarchical_first_100` y `hierarchical_80_dual_backfill_20` son las cuatro variantes formales `A_historical_defined` asociadas al claim descriptivo G3C-005; `hierarchical_70_dual_backfill_30` se incluye únicamente como contexto descriptivo adicional y no fue seleccionada por favorabilidad ni constituye evidencia confirmatoria. No se presentan CI, p-values, tendencias ajustadas ni contrastes inferenciales. `diagnostic_union_hierarchical_dual` se excluye del rendimiento ordinario porque representa un techo diagnóstico. La figura no modifica la evidencia confirmatoria ni la disposición de HE2.

population_and_denominator: 1,056 series / 67 DAM / 42 NANDINA; benchmark interno offline, Capítulo 87.
metric_or_evidence_family: Phase E exact-NANDINA descriptive coverage at depths 50, 100 and 200.
uncertainty_statement: DESCRIPTIVE_NO_CI_AUTHORIZED; no p-values or inferential contrasts.
scope_limitation: Four formal A_historical_defined variants plus hierarchical_70_dual_backfill_30 as context only; diagnostic union excluded from ordinary performance.
forbidden_interpretation: Do not promote Phase E to confirmatory evidence, infer significance between variants, rank variants by favorability, or use the diagnostic union as ordinary performance.
source_table_paths:
  - outputs/results/group5/tables/g5_secondary_01_phase_e_descriptive.csv
figure_svg_path: figures/group6/g6_fig_02_phase_e.svg
figure_png_path: figures/group6/g6_fig_02_phase_e.png
accessibility_checks:
  - both axis titles >= 10 pt effective
  - ticks and nominal legend entries >= 9 pt effective
  - five distinct marker shapes; color not sole required encoding
  - 70/30 contextual variant retains equal visual weight
  - y-axis baseline at zero and range [0,0.35]
  - no material clipping or label overlap detected
  - no internal workflow ID displayed as publication title
status: READY_FOR_EXTERNAL_AUDIT

## G6-FIG-03

figure_id: G6-FIG-03
working_title: Sensibilidad conjunta del banco histórico a tamaño y composición (EXP11A)
scientific_role: DESCRIPTIVE_SENSITIVITY / NONCAUSAL
destination: APPENDIX

final_caption: **Sensibilidad conjunta del banco histórico a tamaño y composición (EXP11A) en el benchmark interno offline del Capítulo 87 (1,056 series, 67 DAM y 42 NANDINA).** Los seis paneles muestran Top1, Top3, Top5, Top10, Top50 y MRR para 31 corridas observadas distribuidas como H25 (`n=10`), H50-D1 (`n=5`), H50-D2 (`n=5`), H75 (`n=10`) y la referencia congelada H100 (`n=1`). D1 y D2 son composiciones diferenciadas dentro de H50; H25, H75 y H100 conservan asimismo sus composiciones observadas. Cada punto representa una corrida individual y H100 se muestra como una única referencia, no como una distribución de réplicas. EXP11A es una sensibilidad descriptiva y no causal en la que tamaño y composición varían conjuntamente; por ello, las diferencias entre condiciones no identifican un efecto causal aislado ni monotónico del tamaño. No se muestran CI, p-values, regresiones, suavizados ni summaries congelados como marks de la figura.

population_and_denominator: EVAL fijo de 1,056 series / 67 DAM / 42 NANDINA; 31 bancos/corridas observados con inventario 10/5/5/10/1 por condición.
metric_or_evidence_family: EXP11A joint size-composition sensitivity; Top1, Top3, Top5, Top10, Top50 and MRR.
uncertainty_statement: DESCRIPTIVE_NO_CI_AUTHORIZED; no p-values, regressions, smoothing or summary marks.
scope_limitation: Bank size and natural composition vary jointly; H100 is one frozen reference; H50-D1 and H50-D2 are distinct observed compositions.
forbidden_interpretation: Do not infer an isolated or monotonic causal size effect, treat H100 n=1 as a replicate distribution, or convert frozen condition summaries into uncertainty intervals.
source_table_paths:
  - outputs/results/group5/tables/g5_appendix_02_exp11a_size_composition_sensitivity.csv
  - outputs/experiments/exp11a_historical_size_sensitivity_v0.3/exp11_metrics_by_run.csv
  - outputs/experiments/exp11a_historical_size_sensitivity_v0.3/exp11_metrics_by_condition.csv
figure_svg_path: figures/group6/g6_fig_03_exp11a.svg
figure_png_path: figures/group6/g6_fig_03_exp11a.png
accessibility_checks:
  - minimum effective font >= 8.5 pt
  - all six panel titles = 9.6 pt effective
  - category labels horizontal in frozen non-favorability order
  - deterministic horizontal jitter only; no vertical jitter
  - individual observations remain discernible
  - H100 additionally encoded by solid diamond
  - no material clipping or label overlap detected
  - no internal workflow ID displayed as publication title
status: READY_FOR_EXTERNAL_AUDIT
```

---

## 9. Propuesta de `group6_closure_v0.1.json`

La siguiente es una **propuesta de contenido** para auditoría externa. No se escribe el archivo en esta ejecución.

```json
{
  "artifact_id": "GROUP6_CLOSURE_CANDIDATE_V0.1",
  "version": "v0.1",
  "group": 6,
  "ficha": "G6-F03",
  "status": "READY_FOR_EXTERNAL_AUDIT",
  "main_source_commit": "3390878a62ce32ba0e6f4fce69a394c903f5ff11",
  "g6_f01_registry_path": "outputs/figures/group6/g6_figure_spec_registry_v0.1.json",
  "g6_f01_registry_blob": "44cc30fc3c38639c6aa4370cb6f317458041f1b1",
  "g6_f02_ledger_path": "outputs/figures/group6/g6_figure_hash_ledger_v0.1.csv",
  "g6_f02_ledger_blob": "bfcbfe8a2232246476979506377ff3005166253f",
  "figure_count": 3,
  "figure_ids": [
    "G6-FIG-01",
    "G6-FIG-02",
    "G6-FIG-03"
  ],
  "caption_count": 3,
  "per_figure_source_bindings": {
    "G6-FIG-01": [
      "outputs/results/group5/tables/g5_main_01_he2a_primary_early_ranking.csv@cb68583ee2260e4455796bac99ad90995ca7ef92",
      "outputs/results/group5/tables/g5_main_02_he2b_deep_coverage.csv@359e4e19b5ef1d44983c03039162209293b2a44c"
    ],
    "G6-FIG-02": [
      "outputs/results/group5/tables/g5_secondary_01_phase_e_descriptive.csv@fa961cf3d6198ddba6a6b5eeadcc9a23c8801f61"
    ],
    "G6-FIG-03": [
      "outputs/results/group5/tables/g5_appendix_02_exp11a_size_composition_sensitivity.csv@cf3aedab5935d6af9b3ac7be7b51b954fcb9c403",
      "outputs/experiments/exp11a_historical_size_sensitivity_v0.3/exp11_metrics_by_run.csv@9b434d7e09e6db7e9de061953b59c53aac2337ad",
      "outputs/experiments/exp11a_historical_size_sensitivity_v0.3/exp11_metrics_by_condition.csv@535dd377d107ddcbf09ecaa13cd66ca723ee738d"
    ]
  },
  "per_figure_caption_checks": {
    "G6-FIG-01": "PASS / population, arm-vs-paired distinction, 99% and 95% CI, no arm-level CI, internal scope and forbidden global-RAG interpretation explicit",
    "G6-FIG-02": "PASS / descriptive role, four formal variants, 70/30 context only, diagnostic-union ceiling and no-confirmatory-role explicit",
    "G6-FIG-03": "PASS / 31 observed runs, condition counts, H100 single reference, joint size-composition sensitivity and noncausal/nonmonotonic limitation explicit"
  },
  "per_figure_accessibility_checks": {
    "G6-FIG-01": "PASS / min text 8.10 pt SVG and 8.16 pt PNG; axis/ticks 9.00/9.12 pt; redundant shapes; no material clipping",
    "G6-FIG-02": "PASS / axis titles 10.20/10.08 pt; ticks and nominal legend 9.00/9.12 pt; distinct shapes; no material clipping",
    "G6-FIG-03": "PASS / min text 8.70/8.64 pt; panel titles 9.60 pt; observations discernible; no vertical jitter; no material clipping"
  },
  "scientific_consistency": "PASS",
  "accessibility": "PASS",
  "caption_self_containment": "PASS",
  "canonical_table_consistency": "PASS",
  "numeric_consistency_with_group5": "PASS",
  "claim_consistency_with_group4": "PASS",
  "claim_scope_consistency": "PASS",
  "uncertainty_consistency_with_group3": "PASS",
  "forbidden_claim_count": 0,
  "scientific_data_change_count": 0,
  "new_scientific_metric_count": 0,
  "new_inference_count": 0,
  "new_ci_count": 0,
  "new_p_value_count": 0,
  "exp12_reopened": false,
  "article_modified": false,
  "thesis_modified": false,
  "g6_f03_candidate_status": "READY_FOR_EXTERNAL_AUDIT",
  "group6_closure_candidate": true,
  "group6_closed": false,
  "external_audit": "PENDING",
  "g7_f01_authorized": false,
  "recommended_group6_state_after_external_pass": "CLOSED / APPROVED",
  "recommended_next_ficha_after_external_pass": "G7-F01"
}
```

---

## 10. Siguiente actor

```text
NEXT_ACTOR = IA_EXPERIMENTAL
```

La IA Experimental debe auditar de forma independiente esta propuesta, verificando al menos: fidelidad de los tres captions contra G3–G6, autosuficiencia, alcance de claims, incertidumbre, accesibilidad integrada y ausencia de nueva ciencia. Solo después de un PASS externo corresponde materializar técnicamente los outputs de G6-F03 y decidir el cierre formal de Grupo 6 conforme a la gobernanza vigente.

---

## 11. Declaraciones de no modificación / no cierre

```text
MAIN_MODIFIED = false
FIGURE_SVG_MODIFIED = false
FIGURE_PNG_MODIFIED = false
RENDER_SCRIPT_MODIFIED = false
HASH_LEDGER_MODIFIED = false
SCIENTIFIC_TABLE_MODIFIED = false
SCIENTIFIC_DATA_MODIFIED = false
CAPTION_REGISTRY_MATERIALIZED = false
GROUP6_CLOSURE_JSON_MATERIALIZED = false
NEW_SCIENTIFIC_METRIC_COUNT = 0
NEW_INFERENCE_COUNT = 0
NEW_CI_COUNT = 0
NEW_P_VALUE_COUNT = 0
HE2_REDECIDED = false
HE5_REDECIDED = false
EXP12_REOPENED = false
ARTICLE_MODIFIED = false
THESIS_MODIFIED = false
GROUP6_CLOSED = false
G6_F03_APPROVED = false
G7_F01_AUTHORIZED = false
```

```text
FIG009_RESULT = PASS_READY_FOR_EXTERNAL_AUDIT
NEXT_ACTOR = IA_EXPERIMENTAL
GROUP6_CLOSED = false
G7_F01_AUTHORIZED = false
```
