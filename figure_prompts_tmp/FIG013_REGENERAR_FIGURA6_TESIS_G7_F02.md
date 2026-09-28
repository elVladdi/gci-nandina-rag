# FIG013 — Regeneración determinística editorial de Figura 6 para tesis G7-F02

## Actor

Actúa como **CODEX** exclusivamente para una tarea técnica reproducible de generación de figura.

No eres la IA de Redacción Científica, la IA Experimental ni la IA Diseñadora y Auditora de Figuras Científicas.

## Estado autorizado

Lee íntegramente antes de ejecutar:

```text
figure_prompts_tmp/FIG012_RESPUESTA_AUDITAR_ADAPTACION_TESIS_FIGURA6_G7_F02.md
@ be0879c44b9d933bc0591bcf498b5e056cc31b20

figure_prompts_tmp/FIG012_AUDITORIA_EXTERNA_PASS.md
@ 547e1dbfc34a03b9c569cf4d8c1792c88f94901b
```

Estado vinculante:

```text
FIG012_EXTERNAL_AUDIT = PASS
FIGURE_6_EXISTING_G6_BINARY_USABLE_AS_IS = false
FIGURE_6_ADAPTATION_REQUIRED = true
SCIENTIFIC_DATA_CHANGE_REQUIRED = false
SCIENTIFIC_GEOMETRY_CHANGE_REQUIRED = false
DOCX_EDIT_AUTHORIZED = false
A043_EXECUTED = false
121G_AUTHORIZED = false
```

## Objetivo único

Generar un **candidato específico para la Figura 6 de la tesis**, derivado de G6-FIG-03, modificando exclusivamente texto visible y, solo si fuera estrictamente necesario para ajuste del español, parámetros tipográficos pertenecientes a nodos de texto.

No modifiques el DOCX. No integres la figura. No ejecutes A043. No ejecutes 121G ni ningún bloque posterior.

## Fuentes congeladas

Trabaja contra el estado científico congelado:

```text
REF_G6 = e93b44164a9619dad1f527a3b2d4479265858e39
```

Verifica antes de generar:

```text
src/figures/group6/render_g6_fig_03_exp11a.py
GIT_BLOB = 1723f139afd308c4966846247ffe4d2f330a0d4e

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

Si cualquiera de estas identidades no coincide, `STOPPED_PRECONDITION`.

## Protección de artefactos existentes

Está prohibido sobrescribir o modificar:

```text
src/figures/group6/render_g6_fig_03_exp11a.py
figures/group6/g6_fig_03_exp11a.svg
figures/group6/g6_fig_03_exp11a.png
outputs/figures/group6/*

src/figures/group7/render_g7_thesis_fig_04_he2.py
figures/group7/g7_thesis_fig_04_he2.svg
figures/group7/g7_thesis_fig_04_he2.png
outputs/figures/group7/g7_thesis_fig_04_he2_manifest_v0.1.json

src/figures/group7/render_g7_thesis_fig_05_coverage.py
figures/group7/g7_thesis_fig_05_coverage.svg
figures/group7/g7_thesis_fig_05_coverage.png
outputs/figures/group7/g7_thesis_fig_05_coverage_manifest_v0.1.json
```

## Salidas candidatas

Crea únicamente:

```text
src/figures/group7/render_g7_thesis_fig_06_sensitivity.py
figures/group7/g7_thesis_fig_06_sensitivity.svg
figures/group7/g7_thesis_fig_06_sensitivity.png
outputs/figures/group7/g7_thesis_fig_06_sensitivity_manifest_v0.1.json
figure_prompts_tmp/FIG013_RESPUESTA_REGENERAR_FIGURA6_TESIS_G7_F02.md
```

Mantén todo como candidato en `codex/prompts-temporary`.

## Adaptación editorial vinculante

La geometría y los datos científicos de G6-FIG-03 no cambian.

Aplica exactamente estas sustituciones visibles:

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
-> H100 (referencia)

Conditions are categorical observed banks; H100 is one frozen reference. Size and composition vary jointly.
-> Las condiciones representan bancos observados categóricos; H100 es una única referencia congelada. El tamaño y la composición varían conjuntamente.
```

Mantén visibles sin sustitución los identificadores científicos:

```text
H25
H50-D1
H50-D2
H75
H100
```

No deben aparecer en el texto visible del candidato:

```text
EXP11A
joint size-composition sensitivity
Observed runs only
noncausal
summaries
p-values
fitted trends
Conditions are categorical observed banks
H100 ref.
Size and composition vary jointly
G3
G4
G5
G6
claim IDs
Prompt
source freeze
gate
commit
blob
```

Las palabras españolas equivalentes como `no causal`, `valores p` o `resúmenes` sí están autorizadas cuando forman parte de los textos aprobados arriba.

## Invariantes científicos obligatorios

Deben permanecer exactamente iguales a G6-FIG-03:

```text
CANVAS = 1200 x 800 SVG units
PNG = 3000 x 2000 px / 300 dpi
PANEL_COUNT = 6
METRIC_ORDER = Top1; Top3; Top5; Top10; Top50; MRR [semántica científica; solo cambia presentación a Top-1 etc.]
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

No recalcules datos, no generes summaries nuevos, no reordenes condiciones, no cambies la fuerza del claim y no conviertas la figura en evidencia confirmatoria o causal.

## Tipografía

Conserva inicialmente posiciones, tamaños y anclajes de texto del renderer G6.

Si el texto español no cabe, se permite exclusivamente:

- reducir localmente el tamaño del título, subtítulo o nota inferior;
- introducir saltos de línea únicamente en esos tres bloques textuales;
- ajustar el anclaje/posición únicamente de esos nodos de texto.

Todo ajuste debe quedar documentado en el manifest y **no puede mover paneles, ejes, puntos, categorías, gridlines, separador, jitter ni otras marcas científicas**.

## Validaciones obligatorias

1. Ejecuta el renderer candidato dos veces desde un workspace limpio y verifica hashes idénticos de SVG y PNG entre ambas ejecuciones.
2. Compara el SVG G6 y el candidato eliminando únicamente nodos `<text>`/`<tspan>` y whitespace asociado. La secuencia y atributos de todos los elementos no textuales deben ser idénticos.
3. Verifica explícitamente que los 31 puntos mantengan coordenadas científicas idénticas.
4. Verifica los seis paneles, escala `[0,1]`, gridlines, separador, jitter, orden de condiciones y H100 como diamante único.
5. Verifica ausencia de texto visible prohibido e IDs internos de gobernanza.
6. Verifica legibilidad del candidato: sin clipping ni solapamiento material y tamaño efectivo mínimo >= 8 pt. Si el subtítulo requiere ajuste local, documéntalo.
7. Calcula SHA-256, tamaño y Git blob del script, SVG y PNG candidatos.
8. Recalcula y confirma que renderer/SVG/PNG G6 permanezcan byte-idénticos.
9. Recalcula y confirma que los artefactos aprobados de Figuras 4 y 5 permanezcan byte-idénticos.
10. No modifiques ni abras para edición el DOCX acumulativo.

## Manifest

`outputs/figures/group7/g7_thesis_fig_06_sensitivity_manifest_v0.1.json` debe registrar como mínimo:

- fuente G6 y sus identidades originales;
- fuentes científicas y blobs;
- script candidato y SHA-256;
- SVG/PNG candidatos y SHA-256;
- sustituciones textuales realizadas;
- cualquier ajuste tipográfico local;
- `scientific_data_change=false`;
- `scientific_geometry_change=false`;
- `non_text_svg_geometry_match=true`;
- `observed_run_count=31`;
- `deterministic_rerun_match=true`;
- `thesis_visible_internal_ids=none`;
- `g6_protected_artifacts_unchanged=true`;
- `figure4_candidate_unchanged=true`;
- `figure5_candidate_unchanged=true`;
- `docx_modified=false`.

## Respuesta terminal

Reporta y detente:

```text
FIG013_EXECUTION = COMPLETE | STOPPED_PRECONDITION
FIGURE_6_CANDIDATE_CREATED = true|false
SCIENTIFIC_DATA_CHANGE = false
SCIENTIFIC_GEOMETRY_CHANGE = false
NON_TEXT_SVG_GEOMETRY_MATCH = true|false
OBSERVED_RUN_COUNT = 31|<n>
DETERMINISTIC_RERUN_MATCH = true|false
THESIS_VISIBLE_INTERNAL_IDS = NONE|<detalle>
G6_PROTECTED_ARTIFACTS_UNCHANGED = true|false
FIGURE_4_CANDIDATE_UNCHANGED = true|false
FIGURE_5_CANDIDATE_UNCHANGED = true|false
DOCX_MODIFIED = false
A043_EXECUTED = false
121G_EXECUTED = false
EXTERNAL_AUDIT = PENDING_BY_IA_EXPERIMENTAL
```

No integres la figura en la tesis. Detente para auditoría externa.
