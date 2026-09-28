# FIG015 — Regenerar Figura 6 para tesis tras resolver etiqueta H100 / G7-F02

## 0. Actor y autorización

Actúa como **CODEX** exclusivamente para una tarea técnica reproducible de generación de figura.

No eres la IA de Redacción Científica, la IA Experimental ni la IA Diseñadora y Auditora de Figuras Científicas.

Lee íntegramente antes de ejecutar:

```text
figure_prompts_tmp/FIG012_RESPUESTA_AUDITAR_ADAPTACION_TESIS_FIGURA6_G7_F02.md
@ be0879c44b9d933bc0591bcf498b5e056cc31b20

figure_prompts_tmp/FIG012_AUDITORIA_EXTERNA_PASS.md
@ 547e1dbfc34a03b9c569cf4d8c1792c88f94901b

figure_prompts_tmp/FIG013_RESPUESTA_REGENERAR_FIGURA6_TESIS_G7_F02.md

figure_prompts_tmp/FIG013_AUDITORIA_EXTERNA_STOP_COMPLIANT.md
@ f9ddfcd5b1c4ffa74ecb34b16d240fb62c7d5f4a

figure_prompts_tmp/FIG014_RESPUESTA_RESOLVER_LEGIBILIDAD_H100_FIGURA6_G7_F02.md
@ e667642115f2fbd27e7052e8cfd43fa8af1a9d95

figure_prompts_tmp/FIG014_AUDITORIA_EXTERNA_PASS.md
@ a20f51496579446b86644022a64e2d68f1aab677
```

Estado vinculante:

```text
FIG014_EXTERNAL_AUDIT = PASS
H100_LABEL_SOLUTION_APPROVED = true
H100_VISIBLE_LABEL = H100 (ref.)
H100_TEXT_FONT_SIZE = mantener (14.5 unidades SVG; ~8.7 pt efectivos)
H100_TEXT_LINE_BREAK = none
H100_TEXT_ANCHOR = mantener (middle / centrado)
H100_TEXT_POSITION_ADJUSTMENT = none
SCIENTIFIC_DATA_CHANGE = false
SCIENTIFIC_GEOMETRY_CHANGE = false
DOCX_EDIT_AUTHORIZED = false
A043_EXECUTED = false
121G_AUTHORIZED = false
```

## 1. Objetivo único

Genera un candidato específico para la Figura 6 de la tesis derivado de G6-FIG-03, modificando únicamente los textos visibles aprobados por FIG012 y FIG014.

No modifiques el DOCX. No integres la figura. No ejecutes A043. No ejecutes 121G ni ningún bloque posterior.

FIG013 no produjo candidato; no intentes reutilizar salidas inexistentes de aquella ejecución.

## 2. Fuentes congeladas

Trabaja contra:

```text
REF_G6 = e93b44164a9619dad1f527a3b2d4479265858e39
```

Verifica antes de generar:

```text
src/figures/group6/render_g6_fig_03_exp11a.py
GIT_BLOB = 1723f139afd308c4966846247ffe4d2f330a0d4e
SHA256 = bb73e2ce324500a36053afa52bc25a03af44def36ea2a7c2fd5c2c14a3cf844f

figures/group6/g6_fig_03_exp11a.svg
GIT_BLOB = 1b2aca9aa9c2582cf0b7e16850cd5b22387cc771
SHA256 = a4a81b565ed2ceb22f23f9a52888e802b1e749186fb43d3bd71faf1b31d5f7c3

figures/group6/g6_fig_03_exp11a.png
SHA256 = 3c4bcf736b56fbc9ffd054562db0eea31be195792f2bade611a9e5205dfa97de
PNG = 3000 x 2000 px / 300 dpi

outputs/results/group5/tables/g5_appendix_02_exp11a_size_composition_sensitivity.csv
GIT_BLOB = cf3aedab5935d6af9b3ac7be7b51b954fcb9c403

outputs/experiments/exp11a_historical_size_sensitivity_v0.3/exp11_metrics_by_run.csv
GIT_BLOB = 9b434d7e09e6db7e9de061953b59c53aac2337ad

outputs/experiments/exp11a_historical_size_sensitivity_v0.3/exp11_metrics_by_condition.csv
GIT_BLOB = 535dd377d107ddcbf09ecaa13cd66ca723ee738d
```

Si alguna identidad no coincide, `STOPPED_PRECONDITION`.

## 3. Protección de artefactos existentes

No sobrescribas ni modifiques G6 ni las Figuras 4–5 aprobadas de G7.

Debes confirmar al final que siguen byte-idénticos.

## 4. Salidas candidatas

Crea únicamente:

```text
src/figures/group7/render_g7_thesis_fig_06_sensitivity.py
figures/group7/g7_thesis_fig_06_sensitivity.svg
figures/group7/g7_thesis_fig_06_sensitivity.png
outputs/figures/group7/g7_thesis_fig_06_sensitivity_manifest_v0.1.json
figure_prompts_tmp/FIG015_RESPUESTA_REGENERAR_FIGURA6_TESIS_TRAS_RESOLVER_H100_G7_F02.md
```

Mantén todo como candidato en `codex/prompts-temporary`.

## 5. Sustituciones visibles obligatorias

Aplica exactamente:

```text
EXP11A joint size-composition sensitivity
-> Sensibilidad conjunta del banco histórico a tamaño y composición

Observed runs only; descriptive and noncausal; no summaries, CI, p-values, or fitted trends
-> Solo corridas observadas; análisis descriptivo y no causal; sin resúmenes como marcas, IC, valores p ni tendencias ajustadas

Top1  -> Top-1
Top3  -> Top-3
Top5  -> Top-5
Top10 -> Top-10
Top50 -> Top-50
MRR   -> MRR

H100 ref.
-> H100 (ref.)

Conditions are categorical observed banks; H100 is one frozen reference. Size and composition vary jointly.
-> Las condiciones representan bancos observados categóricos; H100 es una única referencia congelada. El tamaño y la composición varían conjuntamente.
```

Mantén visibles sin cambio `H25`, `H50-D1`, `H50-D2`, `H75` y el identificador científico `H100` contenido en `H100 (ref.)`.

Para la etiqueta `H100 (ref.)` queda vinculante:

```text
font-size = 14.5 unidades SVG (~8.7 pt efectivos)
line-break = none
text-anchor = middle
posición = exactamente la posición categórica original de H100
```

No sustituyas `ref.` por `referencia` en el rótulo visual.

## 6. Invariantes científicos

Deben permanecer exactamente iguales a G6-FIG-03:

```text
CANVAS = 1200 x 800 SVG units
PNG = 3000 x 2000 px / 300 dpi
PANEL_COUNT = 6
SCIENTIFIC_METRIC_ORDER = Top1; Top3; Top5; Top10; Top50; MRR
VISIBLE_METRIC_LABELS = Top-1; Top-3; Top-5; Top-10; Top-50; MRR
CONDITION_ORDER = H25; H50-D1; H50-D2; H75; H100
OBSERVED_RUN_COUNT = 31
COUNTS_BY_CONDITION = 10; 5; 5; 10; 1
Y_RANGE_ALL_PANELS = [0,1]
JITTER = IDENTICAL_TO_G6
POINT_COORDINATES = IDENTICAL_TO_G6
H100_MARKER = SINGLE_SOLID_DIAMOND
OTHER_RUN_MARKERS = OPEN_CIRCLES
SEPARATOR_BEFORE_H100 = IDENTICAL_TO_G6
CONNECTING_LINES = NONE
CI = NONE
P_VALUES = NONE
REGRESSION = NONE
SMOOTHING = NONE
SUMMARY_MARKS = NONE
EVAL_N = 1056
DAM_N = 67
NANDINA_N = 42
SCIENTIFIC_ROLE = DESCRIPTIVE_SENSITIVITY / NONCAUSAL
HE5 = INCONCLUSIVE
```

No recalcules métricas, summaries, agregados o inferencia.

## 7. Tipografía

Conserva posiciones, tamaños y anclajes del renderer G6 salvo ajustes locales estrictamente necesarios en **título, subtítulo o nota inferior** para que el español quepa. Si necesitas alguno, documéntalo.

No ajustes posición, tamaño, anclaje ni número de líneas de `H100 (ref.)`; FIG014 ya resolvió esa etiqueta y fijó su presentación exacta.

Ningún ajuste textual puede mover paneles, ejes, puntos, categorías, gridlines, separador, jitter o marcas científicas.

## 8. Validaciones obligatorias

1. Ejecuta el renderer candidato dos veces desde un workspace limpio y verifica hashes idénticos de SVG y PNG.
2. Compara SVG G6 y candidato eliminando únicamente nodos `<text>`/`<tspan>` y whitespace asociado. Todos los elementos no textuales y sus atributos deben ser idénticos.
3. Verifica explícitamente coordenadas idénticas de los 31 puntos en los seis paneles.
4. Verifica paneles, escala `[0,1]`, gridlines, separador, jitter, orden de condiciones y diamante H100.
5. Verifica `H100 (ref.)` exactamente, a 14.5 unidades SVG, centrado y sin reposicionamiento.
6. Verifica ausencia de solapamiento material entre H75 y H100 en los seis paneles y ausencia de clipping.
7. Verifica tamaño efectivo mínimo >= 8 pt para todo texto visible.
8. Verifica que no queden en la figura `EXP11A`, cadenas inglesas legacy ni IDs de gobernanza.
9. Calcula SHA-256, tamaño y Git blob del script, SVG y PNG candidatos.
10. Confirma G6 y Figuras 4–5 G7 byte-idénticos.
11. No abras el DOCX para edición.

## 9. Manifest

El manifest debe registrar como mínimo:

```text
scientific_data_change = false
scientific_geometry_change = false
non_text_svg_geometry_match = true
observed_run_count = 31
deterministic_rerun_match = true
h100_visible_label = H100 (ref.)
h100_font_size_svg_units = 14.5
h100_text_anchor = middle
h100_position_adjustment = none
h100_overlap_with_h75 = false
thesis_visible_internal_ids = none
g6_protected_artifacts_unchanged = true
figure4_candidate_unchanged = true
figure5_candidate_unchanged = true
docx_modified = false
```

Incluye también fuentes, blobs/hashes, sustituciones textuales, hashes de salidas y cualquier ajuste textual de título/subtítulo/nota inferior.

## 10. Respuesta terminal

Reporta:

```text
FIG015_EXECUTION = COMPLETE | STOPPED_PRECONDITION
FIGURE_6_CANDIDATE_CREATED = true|false
SCIENTIFIC_DATA_CHANGE = false
SCIENTIFIC_GEOMETRY_CHANGE = false
NON_TEXT_SVG_GEOMETRY_MATCH = true|false
OBSERVED_RUN_COUNT = 31|<n>
DETERMINISTIC_RERUN_MATCH = true|false
H100_VISIBLE_LABEL = H100 (ref.)
H100_OVERLAP_WITH_H75 = false|true|NOT_EVALUATED
THESIS_VISIBLE_INTERNAL_IDS = NONE|<detalle>
G6_PROTECTED_ARTIFACTS_UNCHANGED = true|false
FIGURE_4_CANDIDATE_UNCHANGED = true|false
FIGURE_5_CANDIDATE_UNCHANGED = true|false
DOCX_MODIFIED = false
A043_EXECUTED = false
121G_EXECUTED = false
EXTERNAL_AUDIT = PENDING_BY_IA_EXPERIMENTAL
```

No integres la figura. Detente para auditoría externa.
