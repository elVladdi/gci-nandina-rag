# Prompt106 - Respuesta oficial

## Reporte terminal

```text
PROMPT106_EXECUTION = COMPLETE
PROMPT106_COMMIT = 9c1d17db8b0846041c67fb0e7efa265fcb716616
WORKSPACE_CONTRACT = VERIFIED / C:\Users\Vladimir\OneDrive\Documentos\Maestría UNMSM\LLM_RGA_NANDINA
ORIGIN = https://github.com/elVladdi/gci-nandina-rag.git
MAIN_BASE = b6404ca85c8cd0b18a6b318bae1236d2ef021f4a
PLAN_BASE = b74b96d0163807007e4579d86450dd235125b30f
FICHAS_POSTEXEC = 804b59b73d7d2803d15e0adcb80546410a6718b8
PREVIOUS_CANDIDATE_COMMIT = 2a483984eddc60dbbd48e7188b6fe9dbd7e829c5
CORRECTED_CANDIDATE_COMMIT = 71b13caf6b97e254b4c701b23318bcb0682714bd
CORRECTED_CANDIDATE_TREE = 17419cddc7c9425fdcf4843823511b9ccab3e099
CORRECTION_PARENT = 2a483984eddc60dbbd48e7188b6fe9dbd7e829c5
CORRECTION_BRANCH = figures/g6-f02-render-v01
CORRECTION_PUBLISHED = true
CORRECTION_COMMIT_COUNT = 1
CUMULATIVE_CHANGED_PATH_COUNT_VS_MAIN_BASE = 10
COMMITS_AHEAD_VS_MAIN_BASE = 2
COMMITS_BEHIND_VS_MAIN_BASE = 0
CORRECTION_SCOPE_COUNT = 6
C1_LEDGER_CANONICAL_BYTES = COMPLETE
C2_FIG03_MIN_FONT = COMPLETE
C3_FIG03_OCCLUSION = COMPLETE
C4_VISIBLE_INTERNAL_IDS = COMPLETE
C5_FIG01_ATTEMPT06_LABEL = COMPLETE
C6_FIG02_Y_AXIS_LABEL = COMPLETE
FIGURE_VALIDATION_SUMMARY = COUNTS_VALUES_RANGES_CI_AND_SOURCE_BINDINGS_PRESERVED
DETERMINISM_CHECK = PASS
LEDGER_ROW_COUNT = 16
LEDGER_CANONICAL_SHA256_MATCH_COUNT = 16
LEDGER_CANONICAL_SIZE_MATCH_COUNT = 16
PYTHON_VERSION = 3.12.14 (main, Aug 25 2026, 14:01:42) [MSC v.1944 64 bit (AMD64)]
PILLOW_VERSION = 12.3.0
DEPENDENCIES_INSTALLED_OR_DOWNLOADED = false
FICHAS_FINAL = ea5bc84b8e01f1f7fa0c365a7a83bb69d370d37f
MAIN_FINAL = b6404ca85c8cd0b18a6b318bae1236d2ef021f4a
PLAN_FINAL = b74b96d0163807007e4579d86450dd235125b30f
G6_F02_FINAL_STATE = CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
G6_F03_FINAL_STATE = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
GROUP6 = IN_PROGRESS
ARTICLE_MODIFIED = false
THESIS_MODIFIED = false
PLAN_MODIFIED = false
NEW_SCIENTIFIC_METRIC_COUNT = 0
NEW_INFERENCE_COUNT = 0
NEW_CI_COUNT = 0
NEW_P_VALUE_COUNT = 0
EXP12_REOPENED = false
EXTERNAL_AUDIT = PENDING
```

## Paths exactos del candidato

El commit correctivo y el diff acumulado contra MAIN_BASE se limitan a:

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

No se modificaron fuentes cientificas, registry, .gitattributes, requirements,
resultados historicos ni autorizaciones. No se integro el candidato a main.

## Correcciones y verificacion

- C1: se stagearon primero los nueve scripts/outputs. El ledger se construyo
  sobre bytes binarios de `git show :path`, con SHA-256 y longitud reales,
  y explicita `hash_semantics=CANONICAL_GIT_CONTENT_BYTES`. Posteriormente una
  comprobacion independiente leyo cada `71b13caf:path`: 16/16 SHA-256 y 16/16
  tamanos coinciden. Incluye registry, seis inputs, tres scripts y seis renders.
  No se confundio SHA-256 de contenido con el identificador Git del blob.
- C2: FIG03 tiene dimensiones SVG fisicas coherentes con el PNG de 300 dpi.
  Minimo efectivo SVG: 8.7 pt; minimo raster considerando redondeo: 8.64 pt.
  Se inspeccionaron las tres imagenes; labels horizontales y layout 2x3
  conservados, sin recortes observados.
- C3: offsets normalizados y asignacion run/seed intactos. Solo se cambio la
  escala horizontal de 55 a 160, anclas de categorias y radio de circulos
  a 2.2 unidades. H100 conserva su diamante. Se verificaron 186/186 marcas
  contra sus coordenadas fuente: 180 circulos y seis diamantes; 31 por panel.
  Todos los y coinciden exactamente con el candidato anterior. El control
  geometrico, incluidos los contornos, encontro cero pares de circulos
  solapados; separacion minima de bordes: 0.500499980470253 unidades.
  Este numero es QC geometrico, no una metrica cientifica ni un claim.
- C4: titulos visibles descriptivos sin prefijos G6-FIG-0X.
- C5: Panel C explicita `Hierarchical (Attempt06)`.
- C6: FIG02 usa titulo de eje y vertical centrado en x=30, exterior al campo
  de datos que comienza en x=100. Tamano SVG 10.2 pt; raster efectivo 10.08 pt.
  Las marcas y sus coordenadas no cambiaron.

Los seis bindings de inputs corresponden a los blobs congelados. Para FIG01
y FIG02, todos los elementos SVG distintos del texto son identicos a los
del candidato original, preservando posiciones, CI, rangos y marcas.
Los scripts generan SVG y PNG desde los mismos valores y geometria; se
inspeccionaron los PNG finales y se verificaron las estructuras SVG.

```text
FIG01_panel_count = 3
FIG01_A = 5 metrics x 4 arms; x=[0,1]; no arm-level CI
FIG01_B = 15 paired contrasts; frozen 99% CI; zero line; x=[-0.1,1]
FIG01_C = 1 Recall@200-Recall@100 estimate; frozen 95% CI; zero line; x=[-0.1,1]
FIG01_Pool200_confirmatory_estimates = 0
FIG01_p_values = 0
FIG02_panel_count = 1
FIG02_mark_count = 15
FIG02_variants = 4 formal + 1 context-only
FIG02_depths = 50 / 100 / 200
FIG02_y_range = [0,0.35]
FIG02_diagnostic_union_performance_marks = 0
FIG02_CI_p_values_connecting_lines = 0 / 0 / 0
FIG03_panel_count = 6
FIG03_metrics = Top1 / Top3 / Top5 / Top10 / Top50 / MRR
FIG03_observed_run_count = 31
FIG03_condition_counts = 10 / 5 / 5 / 10 / 1
FIG03_condition_order = H25 / H50-D1 / H50-D2 / H75 / H100 ref.
FIG03_frozen_summary_marks = 0
FIG03_y_range_all_panels = [0,1]
FIG03_H100_marks_per_panel = 1
FIG03_CI_p_values_regression_vertical_jitter = 0 / 0 / 0 / 0
FIG03_jitter_n10 = [-0.18,-0.14,-0.10,-0.06,-0.02,0.02,0.06,0.10,0.14,0.18]
FIG03_jitter_n5 = [-0.12,-0.06,0.00,0.06,0.12]
FIG03_jitter_n1 = [0.00]
```

## Determinismo y entorno

Se ejecutaron consecutivamente dos veces los tres scripts corregidos, con
los mismos inputs y el runtime existente:

```text
C:\Users\Vladimir\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe
src/figures/group6/render_g6_fig_01_he2.py
src/figures/group6/render_g6_fig_02_phase_e.py
src/figures/group6/render_g6_fig_03_exp11a.py
```

Se uso biblioteca estandar, Pillow y fuentes Arial de Windows ya disponibles.
No se instalaron ni descargaron dependencias. No se ejecutaron experimentos
ni suites cientificas ajenas al alcance.

| Figura | SVG run1=run2 | PNG run1=run2 | PNG dimensiones |
|---|---|---|---|
| FIG01 | true | true | 2500x3125 |
| FIG02 | true | true | 3000x1688 |
| FIG03 | true | true | 3000x2000 |

Los SHA siguientes son de bytes canonicos Git, no de materializacion CRLF:

| Archivo | SHA-256 | Bytes |
|---|---|---:|
| g6_fig_01_he2.svg | 4019a92b15178339fb45fd0272c898217cc2dcc9040c56c36fbf81ad4fca61eb | 23713 |
| g6_fig_01_he2.png | 27d6148a1a851eff3329bcf2f0261b3f1e46a5c71b4a6a4714721e1fce572247 | 146071 |
| g6_fig_02_phase_e.svg | a9625057d936e79da9bf28f36dc43ecce403bc3b826d8f3ee05828efaddf7c4e | 8387 |
| g6_fig_02_phase_e.png | 5412d1eee7a58d6ec8a06f9a296f718d0725e1c121d176bfbc3fbeb30850ea9c | 107303 |
| g6_fig_03_exp11a.svg | cc8ec9b60cc88dc18e52cbe21dffa6f622173591f8faf5b2269b413185083d0a | 33429 |
| g6_fig_03_exp11a.png | f9d9b3a8cee9db4442b016a96d137247d000204d84b7bb15b5e01c599baac0eb | 108044 |

## Gobernanza y preservacion

Fichas se actualizo desde 804b59b73d7d2803d15e0adcb80546410a6718b8 mediante
un commit que solo anade el bloque de postcorreccion a
`docs/fichas/grupos_3_8/04_REGISTRO_ESTADO_FICHAS.md`. No cambia el estado
terminal de G6-F02. El HEAD remoto final es
ea5bc84b8e01f1f7fa0c365a7a83bb69d370d37f.

Main y Plan fueron verificados remotamente sin cambios. La rama candidata
remota apunta a 71b13caf6b97e254b4c701b23318bcb0682714bd. No hubo force-push,
amend, rebase ni nuevas figuras. Prompt105 se leyo solo como antecedente;
Prompt106 gobierna las seis correcciones. FIG007 y el registry congelado
fueron las fuentes rectoras.

Se preservan HE2=SUPPORTED, HE5=INCONCLUSIVE, EVAL 1056 series/67 DAM/42
NANDINA, alcance capitulo 87/offline/interno, EXP11A no causal y EXP12
CLOSED_WITHOUT_RETRIEVAL / DIVERSITY_EFFECT_NOT_ESTIMABLE. No se equipara
retrieval historico con exactitud global RAG, evidencia normativa con
correccion legal vinculante ni explicacion auditable con correccion legal.

Los untracked preexistentes Referencias/Antecedentes/, Referencias/Glosario/
y data/Series - Descripciones.xlsx no fueron anadidos ni modificados.
Git emitio avisos de permisos al intentar limpiar metadatos de worktrees
antiguos durante mantenimiento automatico; commits y pushes finalizaron
correctamente. No se intento remediar esos avisos fuera del alcance.

Se detiene la ejecucion para auditoria externa. G6-F03 y Grupo7 no se
activaron ni ejecutaron en esta operacion.
