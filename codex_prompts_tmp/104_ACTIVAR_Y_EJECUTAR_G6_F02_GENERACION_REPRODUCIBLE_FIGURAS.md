# PROMPT104 — ACTIVAR Y EJECUTAR G6-F02: GENERACIÓN REPRODUCIBLE DE FIGURAS

## 0. Rol y alcance

Actúa como **Codex ejecutor reproducible** del proyecto de tesis `elVladdi/gci-nandina-rag`.

Ejecuta exclusivamente **G6-F02 — Generación reproducible de figuras**.

G6-F01 ya está cerrado, aprobado e integrado en `main`. El único contrato visual/científico autorizado para esta ejecución es:

```text
outputs/figures/group6/g6_figure_spec_registry_v0.1.json
```

Debes generar **únicamente** las tres figuras aprobadas allí:

```text
G6-FIG-01 — evidencia primaria HE2_A + HE2_B
G6-FIG-02 — Phase E descriptivo
G6-FIG-03 — EXP11A sensibilidad tamaño/composición
```

Esta ejecución:

- **sí** autoriza escribir scripts Python reproducibles;
- **sí** autoriza generar SVG y PNG de las tres figuras;
- **sí** autoriza registrar hashes de inputs, scripts y outputs;
- **no** autoriza modificar cifras, claims, métricas o inferencia;
- **no** autoriza crear figuras adicionales;
- **no** autoriza modificar artículo o tesis;
- **no** autoriza ejecutar G6-F03;
- **no** autoriza recalcular resultados científicos;
- **no** autoriza nuevos CI, p-values, tests, regresiones, smoothing ni agregaciones no permitidas por el registry;
- **no** autoriza reabrir EXP12;
- **no** autoriza reinterpretar HE2 o HE5.

`Prompt103` permanece **SUPERSEDED / DO_NOT_EXECUTE** y no debe usarse.

---

# 1. Workspace local canónico obligatorio

Trabaja exclusivamente en:

```text
C:\Users\Vladimir\OneDrive\Documentos\Maestría UNMSM\LLM_RGA_NANDINA
```

Antes de cualquier cambio ejecuta y registra:

```powershell
cd "C:\Users\Vladimir\OneDrive\Documentos\Maestría UNMSM\LLM_RGA_NANDINA"
git rev-parse --show-toplevel
git remote get-url origin
git branch --show-current
git rev-parse HEAD
git status --porcelain
git worktree list
```

## STOP obligatorio

Detente sin modificar nada si ocurre cualquiera de estos casos:

1. `git rev-parse --show-toplevel` no corresponde exactamente al workspace canónico anterior;
2. `origin` no corresponde a `elVladdi/gci-nandina-rag`;
3. estás en un clon alternativo, worktree temporal o repositorio primario distinto;
4. el working tree contiene cambios no relacionados que impedirían aislar esta ejecución;
5. las refs rectoras congeladas de la sección 2 presentan drift material.

No uses otro clone/worktree como repositorio primario de ejecución.

---

# 2. Refs rectoras congeladas

Verifica exactamente antes de ejecutar:

```text
MAIN_BASE = b6404ca85c8cd0b18a6b318bae1236d2ef021f4a
PLAN_BASE = b74b96d0163807007e4579d86450dd235125b30f
FICHAS_BASE = 98b5c1edeb6bb1b78a06a08b549b4e068e14e62b
PROMPT104_BRANCH = codex/prompts-temporary
```

Estado esperado:

```text
GROUP6 = IN_PROGRESS
G6-F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G6-F02 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
G6-F03 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
GROUP7 = PENDING / NOT_AUTHORIZED
```

Fuente rectora de G6-F02:

```text
docs/fichas/grupos_3_8/grupo_6/G6_F02_GENERACION_REPRODUCIBLE_FIGURAS.md
```

Contrato integrado de figuras:

```text
outputs/figures/group6/g6_figure_spec_registry_v0.1.json
blob = 44cc30fc3c38639c6aa4370cb6f317458041f1b1
```

Si `main`, Plan Maestro, fichas o el registry presentan drift material, detente.

---

# 3. Contrato científico inmutable

Preserva sin reinterpretación:

```text
UNIT_OF_ANALYSIS = SERIE
DEPENDENCY_GROUP = DAM / DECLARACION cuando corresponda
EMPIRICAL_SCOPE = CAPITULO_87 / OFFLINE / INTERNAL_EVALUATION
EVAL_N = 1056
EVAL_DAM = 67
EVAL_NANDINA = 42

HE2 = SUPPORTED
HE5 = INCONCLUSIVE
EXP11A = JOINT_SIZE_COMPOSITION_SENSITIVITY / NONCAUSAL
EXP11B = DESCRIPTIVE_H150_H200 / TEN_OBSERVED_SEED_PAIRS / NO_SEED_SUPERPOPULATION_INFERENCE
EXP12 = CLOSED_WITHOUT_RETRIEVAL / DIVERSITY_EFFECT_NOT_ESTIMABLE
```

Guardrails permanentes:

```text
HISTORICAL_RETRIEVAL_SUPERIORITY_EQUALS_GLOBAL_RAG_ACCURACY = false
NORMATIVE_EVIDENCE_EQUALS_BINDING_LEGAL_CORRECTNESS = false
AUDITABLE_EXPLANATION_EQUALS_CLASSIFICATION_OR_LEGAL_CORRECTNESS = false
```

No generes ninguna interpretación científica nueva a partir de la forma visual.

---

# 4. Activación operacional de G6-F02

Sobre `docs/fichas-grupos-3-8`, partiendo exactamente de `FICHAS_BASE`, modifica **solo**:

```text
docs/fichas/grupos_3_8/04_REGISTRO_ESTADO_FICHAS.md
```

Actualiza G6-F02 a:

```text
ACTIVE / AUTHORIZED / EXECUTION_PENDING
```

Añade un bloque de activación con, como mínimo:

```text
FICHA = G6-F02
PREVIOUS_STATE = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
USER_AUTHORIZATION = PROMPT104_EXPLICIT_EXECUTION
ACTIVATION_STATE = ACTIVE / AUTHORIZED / EXECUTION_PENDING
ACTIVATION_DATE = <fecha local>
MAIN_AT_ACTIVATION = b6404ca85c8cd0b18a6b318bae1236d2ef021f4a
PLAN_AT_ACTIVATION = b74b96d0163807007e4579d86450dd235125b30f
FICHAS_AT_ACTIVATION = 98b5c1edeb6bb1b78a06a08b549b4e068e14e62b
G6_F01_REGISTRY = outputs/figures/group6/g6_figure_spec_registry_v0.1.json
G6_F01_REGISTRY_BLOB = 44cc30fc3c38639c6aa4370cb6f317458041f1b1
G6_F03_AUTHORIZED = false
GROUP7_AUTHORIZED = false
```

No modifiques Plan Maestro en esta etapa de ejecución candidata.

---

# 5. Rama candidata G6-F02

Crea exactamente desde `MAIN_BASE`:

```text
figures/g6-f02-render-v01
```

No uses otra rama candidata.

Todos los artefactos G6-F02 deben quedar en esa rama.

---

# 6. Inputs científicos permitidos

Usa exclusivamente los paths/hashes especificados dentro del registry integrado.

Como mínimo deberán verificarse estos blobs antes de renderizar:

## G6-FIG-01

```text
outputs/results/group5/tables/g5_main_01_he2a_primary_early_ranking.csv
blob = cb68583ee2260e4455796bac99ad90995ca7ef92

outputs/results/group5/tables/g5_main_02_he2b_deep_coverage.csv
blob = 359e4e19b5ef1d44983c03039162209293b2a44c
```

## G6-FIG-02

```text
outputs/results/group5/tables/g5_secondary_01_phase_e_descriptive.csv
blob = fa961cf3d6198ddba6a6b5eeadcc9a23c8801f61
```

## G6-FIG-03

```text
outputs/results/group5/tables/g5_appendix_02_exp11a_size_composition_sensitivity.csv
blob = cf3aedab5935d6af9b3ac7be7b51b954fcb9c403

outputs/experiments/exp11a_historical_size_sensitivity_v0.3/exp11_metrics_by_run.csv
blob = 9b434d7e09e6db7e9de061953b59c53aac2337ad

outputs/experiments/exp11a_historical_size_sensitivity_v0.3/exp11_metrics_by_condition.csv
blob = 535dd377d107ddcbf09ecaa13cd66ca723ee738d
```

No sustituyas estas fuentes por outputs históricos, superseded, derivados manuales o copias locales no versionadas.

---

# 7. Scripts obligatorios

Crea exactamente estos tres scripts:

```text
src/figures/group6/render_g6_fig_01_he2.py
src/figures/group6/render_g6_fig_02_phase_e.py
src/figures/group6/render_g6_fig_03_exp11a.py
```

Cada script debe:

1. leer únicamente sus fuentes autorizadas desde el repositorio;
2. verificar precondiciones estructurales relevantes antes de dibujar;
3. fallar con exit code != 0 ante cualquier inconsistencia;
4. ser determinista;
5. no depender de edición manual posterior;
6. guardar SVG y PNG;
7. no modificar datos fuente;
8. no calcular ninguna inferencia nueva;
9. implementar literalmente las transformaciones permitidas y prohibiciones del registry;
10. poder ejecutarse desde un checkout limpio del repositorio con Python y dependencias ya disponibles/documentadas.

Usa preferentemente `matplotlib` + biblioteca estándar/pandas si ya están disponibles. No introduzcas una dependencia nueva si no es necesaria.

No uses herramientas de edición gráfica manual para retocar posiciones, valores o etiquetas después del render.

---

# 8. Outputs gráficos obligatorios

Genera exactamente:

```text
figures/group6/g6_fig_01_he2.svg
figures/group6/g6_fig_01_he2.png

figures/group6/g6_fig_02_phase_e.svg
figures/group6/g6_fig_02_phase_e.png

figures/group6/g6_fig_03_exp11a.svg
figures/group6/g6_fig_03_exp11a.png
```

Requisitos comunes:

- SVG = vector principal;
- PNG = raster de publicación, mínimo 300 dpi equivalente a tamaño final razonable;
- fondo blanco o muy claro;
- tipografía sans serif;
- estilos consistentes entre las tres figuras;
- legibles en escala de grises;
- color nunca como único canal semántico;
- sin sombras, 3D, gradientes decorativos o pictogramas;
- sin ejes rotos;
- sin ordenamiento por favorabilidad;
- sin cambios manuales post-render.

No generes PDF/EPS salvo que sea técnicamente imprescindible; no se esperan como output de esta ficha.

---

# 9. Reglas exactas por figura

El registry es la autoridad final. Las reglas siguientes son un resumen operativo y **no sustituyen** ningún detalle más restrictivo del JSON.

## 9.1 G6-FIG-01 — HE2_A + HE2_B

Debe tener exactamente 3 paneles verticales:

```text
A — valores absolutos HE2_A
B — 15 contrastes Historical − comparator con CI 99%
C — único contraste Recall@200 − Recall@100 con CI 95%
```

### Panel A

- grouped dot plot;
- cinco métricas: Top-1, Top-3, Top-5, Top-10, MRR@100;
- Historical + Flat + Hierarchical + D1a;
- rango x `[0,1]`;
- **sin CI por brazo**;
- verificar identidad exacta de los valores Historical repetidos antes de deduplicarlos visualmente;
- no promediar repeticiones estructurales.

### Panel B

- 15 estimandos;
- `Historical − comparator`;
- CI congelado de 99% únicamente;
- rango x `[-0.10,1.00]`;
- línea vertical x=0;
- no omitir comparadores o métricas.

### Panel C

- exactamente un estimando `Recall@200 − Recall@100`;
- CI congelado de 95%;
- rango x `[-0.10,1.00]`;
- línea x=0;
- Recall@100/Recall@200 solo como contexto;
- `Pool@200` no debe aparecer como segundo estimando confirmatorio.

No calcules ni muestres p-values.

## 9.2 G6-FIG-02 — Phase E

- exactamente 1 panel;
- grouped dot plot sin líneas;
- profundidades categóricas `[50,100,200]`;
- eje y `[0,0.35]`;
- exactamente 15 marcas = 5 variantes × 3 profundidades;
- cuatro variantes formales:
  - `hierarchical_only`
  - `dual_only`
  - `hierarchical_first_100`
  - `hierarchical_80_dual_backfill_20`
- una variante contextual:
  - `hierarchical_70_dual_backfill_30`
- `diagnostic_union_hierarchical_dual` excluido del rendimiento ordinario;
- sin CI, error bars, p-values, regresiones, smoothing ni líneas de conexión;
- la variante contextual debe conservar igual peso perceptual; diferenciarla por forma/leyenda, no por opacidad baja.

## 9.3 G6-FIG-03 — EXP11A

- exactamente 6 paneles `2×3`;
- métricas: Top1, Top3, Top5, Top10, Top50, MRR;
- condiciones categóricas en orden fijo:

```text
H25 | H50-D1 | H50-D2 | H75 | H100 ref.
```

- usar únicamente las 31 filas `OBSERVED_RUN` para las marcas;
- inventario esperado `10 / 5 / 5 / 10 / 1`;
- D1/D2 debe resolverse desde `dominant_stratum`, nunca por orden de fila;
- 6 `FROZEN_CONDITION_SUMMARY` deben verificarse para trazabilidad pero **no** graficarse;
- rango y `[0,1]` en los seis paneles;
- jitter horizontal determinista exacto según registry;
- mismo mapping de jitter por `run/seed` en los seis paneles;
- H100 = un diamante, una marca por panel, sin jitter;
- sin CI, p-values, regresión, smoothing ni líneas entre condiciones;
- no interpretar el eje como dosis continua de tamaño;
- no calcular medias/medianas/boxplots/violines/intervalos nuevos.

---

# 10. Hash ledger obligatorio

Genera:

```text
outputs/figures/group6/g6_figure_hash_ledger_v0.1.csv
```

Una fila por artefacto versionado relevante de G6-F02.

Columnas mínimas:

```text
artifact_role
figure_id
path
sha256
size_bytes
source_or_output
source_binding
script_binding
notes
```

Debe incluir al menos:

- registry G6-F01;
- cada input científico realmente usado;
- los 3 scripts;
- los 3 SVG;
- los 3 PNG.

Para outputs, `script_binding` debe identificar el script exacto que los generó.

No uses Git blob SHA como sustituto del SHA-256 de archivos; si deseas registrar ambos, agrega una columna adicional.

---

# 11. Validación reproducible obligatoria

Después de generar los outputs:

1. ejecuta los tres scripts desde el workspace canónico;
2. registra versiones relevantes de Python/matplotlib/pandas usadas;
3. calcula SHA-256 de scripts, inputs y outputs;
4. vuelve a ejecutar los tres scripts sin cambiar inputs;
5. verifica que los outputs sean byte-identical entre las dos ejecuciones **cuando el formato lo permita**;
6. si SVG incorpora metadata temporal/no determinista, debes eliminar/configurar esa metadata desde el script y regenerar hasta lograr determinismo; no edites manualmente el SVG;
7. confirma que PNG y SVG representen la misma información científica;
8. valida dimensiones/panel count/mark counts/rangos y reglas de incertidumbre según el registry.

Cualquier fallo de determinismo o validación es bloqueante para el candidato.

No sustituyas la verificación visual/científica por el simple hecho de que el script termine con exit code 0.

---

# 12. Artefactos permitidos del candidato

La rama candidata debe añadir únicamente los siguientes paths:

```text
src/figures/group6/render_g6_fig_01_he2.py
src/figures/group6/render_g6_fig_02_phase_e.py
src/figures/group6/render_g6_fig_03_exp11a.py
figures/group6/g6_fig_01_he2.svg
figures/group6/g6_fig_01_he2.png
figures/group6/g6_fig_02_phase_e.svg
figures/group6/g6_fig_02_phase_e.png
figures/group6/g6_fig_03_exp11a.svg
figures/group6/g6_fig_03_exp11a.png
outputs/figures/group6/g6_figure_hash_ledger_v0.1.csv
```

```text
EXPECTED_CHANGED_PATH_COUNT = 10
```

No añadas README, notebooks, PDFs, previews, temporary files, caches, fonts ni outputs intermedios.

El candidato debe quedar idealmente:

```text
COMMITS_AHEAD = 1
COMMITS_BEHIND = 0
```

respecto a `MAIN_BASE`.

---

# 13. Estado postejecución de fichas

Una vez materializado y pushado el candidato, sobre `docs/fichas-grupos-3-8` actualiza **solo** `04_REGISTRO_ESTADO_FICHAS.md` a:

```text
G6-F02 = CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
G6-F03 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
GROUP6 = IN_PROGRESS
```

Añade bloque postejecución con:

```text
FICHA = G6-F02
ACTIVATION_COMMIT = <sha>
G6_F02_BRANCH = figures/g6-f02-render-v01
G6_F02_CANDIDATE_COMMIT = <sha>
G6_F02_CANDIDATE_PARENT = b6404ca85c8cd0b18a6b318bae1236d2ef021f4a
G6_F02_CHANGED_PATH_COUNT = 10
FIGURE_COUNT = 3
SVG_COUNT = 3
PNG_COUNT = 3
SCRIPT_COUNT = 3
HASH_LEDGER_COUNT = 1
DETERMINISM_CHECK = PASS
EXTERNAL_AUDIT = PENDING
RESULT = CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
G6_F03_AUTHORIZED = false
G6_F03_STARTED = false
```

No cierres G6-F02. No autorices G6-F03.

---

# 14. Respuesta oficial

Persiste tu respuesta completa en:

```text
codex_prompts_tmp/104_RESPUESTA_ACTIVAR_Y_EJECUTAR_G6_F02_GENERACION_REPRODUCIBLE_FIGURAS.md
```

sobre la rama:

```text
codex/prompts-temporary
```

La respuesta debe incluir como mínimo:

```text
PROMPT104_EXECUTION
WORKSPACE_CONTRACT
MAIN_BASE
PLAN_BASE
FICHAS_BASE
ACTIVATION_COMMIT
G6_F02_BRANCH
G6_F02_CANDIDATE_COMMIT
G6_F02_CANDIDATE_PARENT
COMMITS_AHEAD
COMMITS_BEHIND
CHANGED_PATH_COUNT
CHANGED_PATHS
FIGURE_COUNT
SVG_COUNT
PNG_COUNT
SCRIPT_COUNT
HASH_LEDGER_PATH
DETERMINISM_CHECK
INPUT_HASH_CHECKS
FIGURE_VALIDATION_SUMMARY
MAIN_FINAL
PLAN_FINAL
FICHAS_FINAL
G6_F02_FINAL_STATE
G6_F03_FINAL_STATE
ARTICLE_MODIFIED
THESIS_MODIFIED
NEW_SCIENTIFIC_METRIC_COUNT
NEW_INFERENCE_COUNT
NEW_CI_COUNT
NEW_P_VALUE_COUNT
EXP12_REOPENED
EXTERNAL_AUDIT = PENDING
```

No declares `PASS`, `APPROVED`, `CLOSED` ni `INTEGRATED` para G6-F02. Ese dictamen corresponde exclusivamente a la auditoría externa de la IA Experimental.

---

# 15. Criterios de aceptación externa posteriores

El candidato solo será aprobable si la auditoría independiente confirma simultáneamente:

1. exactitud de los 10 paths esperados;
2. parent exacto en `MAIN_BASE` y ausencia de drift;
3. tres figuras y ninguna adicional;
4. scripts reproducibles sin edición manual;
5. SVG + PNG por figura;
6. hashes completos y verificables;
7. determinismo reproducible;
8. exactitud de datos representados contra las tablas congeladas;
9. cumplimiento literal de escalas, paneles, marcas, CI y prohibiciones del registry;
10. ausencia de nueva inferencia, métricas o p-values;
11. EXP11A preservado como sensibilidad conjunta no causal;
12. Phase E preservado como descriptivo no confirmatorio;
13. HE2_A/HE2_B con niveles de CI correctos y sin CI por brazo;
14. ninguna modificación de artículo/tesis;
15. G6-F03 permanece no autorizado.

Si cualquier punto falla, deja el candidato pendiente de corrección y no avances.
