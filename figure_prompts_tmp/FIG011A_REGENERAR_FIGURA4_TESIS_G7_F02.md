# FIG011A — Regeneración determinística editorial de Figura 4 para tesis G7-F02

## Actor

Actúa como **CODEX** exclusivamente para una tarea técnica reproducible de generación de figura. No eres la IA de Redacción Científica ni la IA Experimental.

## Estado autorizado

```text
FIG010_EXTERNAL_AUDIT = PASS
FIGURE_4_ADAPTATION_REQUIRED = true
SCIENTIFIC_DATA_CHANGE_REQUIRED = false
DOCX_EDIT_AUTHORIZED = false
121F_AUTHORIZED = false
```

Lee íntegramente antes de ejecutar:

```text
figure_prompts_tmp/FIG010_RESPUESTA_AUDITAR_ADAPTACION_TESIS_FIGURAS_4_5_G7_F02.md
figure_prompts_tmp/FIG010_AUDITORIA_EXTERNA_PASS.md
```

## Objetivo único

Generar un **candidato específico para la Figura 4 de la tesis**, derivado de G6-FIG-01, cambiando exclusivamente textos visibles y distribución tipográfica necesaria para esos textos.

No modifiques el DOCX. No generes Figura 5. No ejecutes 121F.

## Fuentes congeladas

Trabaja contra `main = db0d0ad0d8435921a7838db6720eaea86a263763` y verifica antes de editar:

```text
src/figures/group6/render_g6_fig_01_he2.py
GIT_BLOB = 678d5fd49b3bd090c7d7729702741e6dcfe293fa

figures/group6/g6_fig_01_he2.svg
GIT_BLOB = f57511c1ddbed5d2177e7cf7b5c9a4a180a3c7e3

figures/group6/g6_fig_01_he2.png
GIT_BLOB = 1860898f13cdefb311489dd1ec3d8fb28bf24538
SHA256 = 3136a814647384eaa1f85c2ce90033a78dde48b661d0b1c078e5b272c6e85d6f

outputs/results/group5/tables/g5_main_01_he2a_primary_early_ranking.csv
GIT_BLOB = cb68583ee2260e4455796bac99ad90995ca7ef92

outputs/results/group5/tables/g5_main_02_he2b_deep_coverage.csv
GIT_BLOB = 359e4e19b5ef1d44983c03039162209293b2a44c
```

Si cualquiera no coincide, STOP.

## Protección de G6

Los artefactos G6 son inmutables. Está prohibido sobrescribir o modificar:

```text
src/figures/group6/render_g6_fig_01_he2.py
figures/group6/g6_fig_01_he2.svg
figures/group6/g6_fig_01_he2.png
outputs/figures/group6/*
```

## Salidas candidatas

Crea únicamente:

```text
src/figures/group7/render_g7_thesis_fig_04_he2.py
figures/group7/g7_thesis_fig_04_he2.svg
figures/group7/g7_thesis_fig_04_he2.png
outputs/figures/group7/g7_thesis_fig_04_he2_manifest_v0.1.json
figure_prompts_tmp/FIG011A_RESPUESTA_REGENERAR_FIGURA4_TESIS_G7_F02.md
```

No escribas estas salidas en `main`; mantenlas como candidato en `codex/prompts-temporary` hasta auditoría externa.

## Adaptación permitida

Usa como especificación vinculante la tabla de sustituciones de FIG010 para Figura 4. En particular deben desaparecer de la figura visible:

```text
Attempt06
D1a
Historical
Flat
Hierarchical
Observed values
Paired difference
frozen
Offline internal benchmark
```

cuando aparezcan como rótulos ingleses/internos, sustituyéndolos por los equivalentes en español aprobados en FIG010.

Se permiten saltos de línea y redistribución **solo de textos/leyendas** para evitar clipping. No muevas marcas de datos, barras/whiskers, líneas de referencia, ejes, ticks o paneles.

## Invariantes científicos obligatorios

Deben permanecer exactamente iguales a G6-FIG-01:

```text
CANVAS = 1000 x 1250 SVG units
PNG = 2500 x 3125 px / 300 dpi
PANEL_COUNT = 3
METRIC_ORDER = Top-1; Top-3; Top-5; Top-10; MRR@100
COMPARATOR_ORDER = flat; hierarchical; dense-MNRL
PANEL_A_ARM_LEVEL_CI = NONE
PANEL_B_CONTRAST_COUNT = 15
PANEL_B_CI = frozen 99% paired-difference CI
PANEL_C_CONTRAST_COUNT = 1
PANEL_C_CI = frozen 95% CI
P_VALUES = NONE
EVAL_N = 1056
DAM_N = 67
NANDINA_N = 42
```

No recalcules datos, intervalos ni posiciones.

## Validaciones obligatorias

1. Ejecuta el script candidato dos veces desde un workspace limpio y verifica que SVG y PNG tengan hashes idénticos entre ambas corridas.
2. Compara el SVG G6 y el SVG candidato eliminando solo nodos `<text>`/`<tspan>` y whitespace asociado. La secuencia de todos los elementos geométricos no textuales (`line`, `circle`, `polygon`, etc.) debe ser idéntica.
3. Verifica que las coordenadas, escalas, ticks, zero-lines y marks sean idénticos a G6-FIG-01.
4. Verifica ausencia visible de `Attempt06` y `D1a` y de rótulos ingleses que FIG010 ordenó naturalizar.
5. Verifica que no aparezcan IDs internos de gobernanza (`G3`, `G4`, `G5`, `G6`, claim IDs, prompts, gates, commits).
6. Verifica legibilidad: sin clipping, solapamiento material o texto fuera de canvas; mínimo efectivo de texto >= 8 pt.
7. Calcula SHA-256, tamaño y Git blob de script, SVG y PNG candidatos.
8. Recalcula y confirma que los tres artefactos G6 protegidos continúan byte-idénticos.

## Manifest

`g7_thesis_fig_04_he2_manifest_v0.1.json` debe registrar como mínimo:

- fuente G6 y hashes originales;
- fuentes científicas y blobs;
- script candidato y SHA-256;
- SVG/PNG candidatos y SHA-256;
- lista de sustituciones textuales;
- `scientific_data_change=false`;
- `non_text_svg_geometry_match=true`;
- `deterministic_rerun_match=true`;
- `thesis_visible_internal_ids=none`;
- `docx_modified=false`.

## Respuesta terminal

Reporta exactamente el estado y detente:

```text
FIG011A_EXECUTION = COMPLETE | STOPPED_PRECONDITION
FIGURE_4_CANDIDATE_CREATED = true|false
SCIENTIFIC_DATA_CHANGE = false
NON_TEXT_SVG_GEOMETRY_MATCH = true|false
DETERMINISTIC_RERUN_MATCH = true|false
THESIS_VISIBLE_INTERNAL_IDS = NONE|<detalle>
G6_PROTECTED_ARTIFACTS_UNCHANGED = true|false
DOCX_MODIFIED = false
FIGURE_5_EXECUTED = false
121F_EXECUTED = false
EXTERNAL_AUDIT = PENDING_BY_IA_EXPERIMENTAL
```

No integres la figura en la tesis. Detente para auditoría externa.