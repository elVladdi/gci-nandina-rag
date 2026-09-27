# FIG011B — Regeneración determinística editorial de Figura 5 para tesis G7-F02

## Actor

Actúa como **CODEX** exclusivamente para una tarea técnica reproducible de generación de figura. No eres la IA de Redacción Científica ni la IA Experimental.

## Estado autorizado

```text
FIG010_EXTERNAL_AUDIT = PASS
FIG011A_EXTERNAL_AUDIT = PASS
FIGURE_4_CANDIDATE = APPROVED_FOR_LATER_DOCX_INTEGRATION
FIGURE_5_ADAPTATION_REQUIRED = true
SCIENTIFIC_DATA_CHANGE_REQUIRED = false
DOCX_EDIT_AUTHORIZED = false
121F_AUTHORIZED = false
```

Lee íntegramente antes de ejecutar:

```text
figure_prompts_tmp/FIG010_RESPUESTA_AUDITAR_ADAPTACION_TESIS_FIGURAS_4_5_G7_F02.md
figure_prompts_tmp/FIG010_AUDITORIA_EXTERNA_PASS.md
figure_prompts_tmp/FIG011A_AUDITORIA_EXTERNA_PASS.md
```

## Objetivo único

Generar un **candidato específico para la Figura 5 de la tesis**, derivado de G6-FIG-02, cambiando exclusivamente textos visibles y distribución tipográfica necesaria para esos textos.

No modifiques el DOCX. No edites Figura 4. No ejecutes 121F.

## Fuentes congeladas

Trabaja contra:

```text
main = db0d0ad0d8435921a7838db6720eaea86a263763
```

Verifica antes de generar:

```text
src/figures/group6/render_g6_fig_02_phase_e.py
GIT_BLOB = e9dafe41e3b22cb1c8d09da08a723925cd300b7d

figures/group6/g6_fig_02_phase_e.svg
GIT_BLOB = ec164ea41ab8605edf198c03785db63c442c1b64

figures/group6/g6_fig_02_phase_e.png
GIT_BLOB = 7917314c8fc54dd96dd9ddfb28c9927c9a577c76
SHA256 = 867ca35d0c454a38bd122c6ecdf5bb693f98f86206828bd68c051aa263c7791f

outputs/results/group5/tables/g5_secondary_01_phase_e_descriptive.csv
GIT_BLOB = fa961cf3d6198ddba6a6b5eeadcc9a23c8801f61
SHA256 = 77a9b3cf27881396162fa25464d9fcaa1c8c557b6140e1e48bdbe93858aa523e
```

Si cualquiera no coincide, STOP.

## Protección de G6 y Figura 4

Está prohibido sobrescribir o modificar:

```text
src/figures/group6/render_g6_fig_02_phase_e.py
figures/group6/g6_fig_02_phase_e.svg
figures/group6/g6_fig_02_phase_e.png
outputs/figures/group6/*

src/figures/group7/render_g7_thesis_fig_04_he2.py
figures/group7/g7_thesis_fig_04_he2.svg
figures/group7/g7_thesis_fig_04_he2.png
outputs/figures/group7/g7_thesis_fig_04_he2_manifest_v0.1.json
```

## Salidas candidatas

Crea únicamente:

```text
src/figures/group7/render_g7_thesis_fig_05_coverage.py
figures/group7/g7_thesis_fig_05_coverage.svg
figures/group7/g7_thesis_fig_05_coverage.png
outputs/figures/group7/g7_thesis_fig_05_coverage_manifest_v0.1.json
figure_prompts_tmp/FIG011B_RESPUESTA_REGENERAR_FIGURA5_TESIS_G7_F02.md
```

Mantén todo como candidato en `codex/prompts-temporary`.

## Adaptación editorial vinculante

La estructura científica de G6-FIG-02 no cambia. Naturaliza exclusivamente los textos visibles.

Usa como encabezado de tesis:

```text
Cobertura exacta NANDINA según profundidad y variante
```

No uses `del conjunto candidato` en el título visible.

Sustituciones mínimas obligatorias:

```text
Phase E exact-NANDINA coverage
-> Cobertura exacta NANDINA según profundidad y variante

Descriptive only; no CI, p-values, fitted trends, or connecting lines
-> Resultados descriptivos; sin IC, valores p, tendencias ajustadas ni líneas de conexión

Exact-NANDINA coverage
-> Cobertura exacta NANDINA

Recovery depth (ordered categories)
-> Profundidad de recuperación

Formal claim variants
-> Variantes descriptivas predefinidas

hierarchical_only
-> Solo jerárquico

dual_only
-> Solo dual

hierarchical_first_100
-> Jerárquico con prioridad para los primeros 100 candidatos

hierarchical_80_dual_backfill_20
-> Jerárquico 80 + backfill dual 20

Context only
-> Contexto descriptivo adicional

hierarchical_70_dual_backfill_30
-> Jerárquico 70 + backfill dual 30

15 marks = 5 variants x 3 depths
-> 15 puntos = 5 variantes × 3 profundidades

N = 1,056 series
-> N = 1 056 series

The diagnostic union is excluded from ordinary performance. Context and formal variants retain equal visual weight.
-> La unión diagnóstica se excluye del rendimiento ordinario. Las variantes predefinidas y la variante contextual conservan igual peso visual.
```

Además, ningún texto visible de la figura candidata puede contener:

```text
Phase E
hierarchical_only
dual_only
hierarchical_first_100
hierarchical_80_dual_backfill_20
hierarchical_70_dual_backfill_30
A_historical_defined
G3C-005
diagnostic_union_hierarchical_dual
Formal claim variants
Context only
Exact-NANDINA coverage
Recovery depth
```

Se permiten saltos de línea y redistribución **solo de textos/leyendas** para evitar clipping o solapamiento. No muevas las 15 marcas, ejes, ticks, gridlines, profundidades ni posiciones de datos.

## Invariantes científicos obligatorios

Deben permanecer exactamente iguales a G6-FIG-02:

```text
CANVAS = 1200 x 675 SVG units
PNG = 3000 x 1688 px / 300 dpi
PANEL_COUNT = 1
DEPTH_ORDER = 50; 100; 200
VARIANT_COUNT = 5
MARK_COUNT = 15
Y_RANGE = [0.00, 0.35]
Y_BASELINE = 0
CONNECTING_LINES = NONE
CI = NONE
P_VALUES = NONE
FITTED_TRENDS = NONE
DIAGNOSTIC_UNION_AS_ORDINARY_PERFORMANCE = false
EVAL_N = 1056
DAM_N = 67
NANDINA_N = 42
```

Mantén exactamente estos quince valores:

```text
Solo jerárquico:                    0.0909 | 0.1013 | 0.3040
Solo dual:                          0.0919 | 0.1004 | 0.2661
Jerárquico prioridad primeros 100:  0.0909 | 0.1013 | 0.2652
Jerárquico 80 + backfill dual 20:   0.0909 | 0.1013 | 0.3040
Jerárquico 70 + backfill dual 30:   0.0909 | 0.1023 | 0.3040
```

No recalcules ni reordenas valores. No conviertas la quinta variante en favorita ni cambies su peso visual.

## Validaciones obligatorias

1. Ejecuta el script candidato dos veces desde un workspace limpio y verifica hashes idénticos de SVG y PNG entre ambas corridas.
2. Compara SVG G6 y candidato eliminando solo nodos `<text>`/`<tspan>` y whitespace asociado. La secuencia y atributos de todos los elementos geométricos no textuales deben ser idénticos.
3. Verifica identidad de coordenadas de las 15 marcas, ejes, ticks, gridlines y límites.
4. Verifica ausencia de todos los identificadores/rótulos prohibidos.
5. Verifica ausencia de IDs internos de gobernanza (`G3`, `G4`, `G5`, `G6`, claim IDs, prompts, gates, commits).
6. Verifica legibilidad: ningún texto fuera de canvas, ningún solapamiento material, mínimo efectivo >= 8 pt.
7. Calcula SHA-256, tamaño y Git blob del script, SVG y PNG candidatos.
8. Recalcula y confirma que renderer/SVG/PNG G6 permanezcan byte-idénticos.
9. Recalcula y confirma que los cuatro artefactos aprobados de Figura 4 permanezcan byte-idénticos.

## Manifest

`g7_thesis_fig_05_coverage_manifest_v0.1.json` debe registrar como mínimo:

- fuente G6 y hashes originales;
- fuente científica y blob;
- script candidato y SHA-256;
- SVG/PNG candidatos y SHA-256;
- sustituciones textuales;
- `scientific_data_change=false`;
- `non_text_svg_geometry_match=true`;
- `deterministic_rerun_match=true`;
- `thesis_visible_internal_ids=none`;
- `docx_modified=false`;
- `figure4_candidate_unchanged=true`.

## Respuesta terminal

Reporta y detente:

```text
FIG011B_EXECUTION = COMPLETE | STOPPED_PRECONDITION
FIGURE_5_CANDIDATE_CREATED = true|false
SCIENTIFIC_DATA_CHANGE = false
NON_TEXT_SVG_GEOMETRY_MATCH = true|false
DETERMINISTIC_RERUN_MATCH = true|false
THESIS_VISIBLE_INTERNAL_IDS = NONE|<detalle>
G6_PROTECTED_ARTIFACTS_UNCHANGED = true|false
FIGURE_4_CANDIDATE_UNCHANGED = true|false
DOCX_MODIFIED = false
121F_EXECUTED = false
EXTERNAL_AUDIT = PENDING_BY_IA_EXPERIMENTAL
```

No integres ninguna figura en la tesis. Detente para auditoría externa.