# PROMPT106 — CORREGIR G6-F02: SCOPE CONSOLIDADO POST-FIG007

## 0. Rol y alcance

Actúa como **Codex ejecutor reproducible** del proyecto `elVladdi/gci-nandina-rag`.

Ejecuta exclusivamente una **corrección técnica localizada del candidato existente de G6-F02**.

Este prompt sustituye a Prompt105 porque la preauditoría FIG007 confirmó sus dos defectos conocidos y detectó cuatro correcciones adicionales que deben resolverse en la misma ejecución.

```text
PROMPT105 = SUPERSEDED / DO_NOT_EXECUTE
PROMPT106 = CURRENT_CORRECTIVE_SCOPE
```

No reinicies G6-F02 desde cero. No vuelvas a activar la ficha. No generes nuevas figuras distintas de las tres ya aprobadas. No cambies datos, claims, métricas, inferencia, CI, p-values, paneles ni semántica científica.

No ejecutes G6-F03. No modifiques artículo ni tesis. No reabras EXP12.

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
git fetch origin
```

STOP si:

1. el toplevel no corresponde exactamente al workspace canónico;
2. `origin` no corresponde a `elVladdi/gci-nandina-rag`;
3. estás en otro clon/worktree como repositorio primario;
4. existen cambios locales no relacionados que no puedan aislarse;
5. cualquiera de las refs congeladas de la sección 2 presenta drift material.

Si quedaron residuos locales de la ejecución interrumpida de Prompt104, no los descartes ciegamente: compáralos primero contra los commits remotos ya publicados y preserva únicamente el estado remoto rector indicado abajo.

---

# 2. Estado remoto rector congelado

Verifica exactamente:

```text
MAIN_BASE = b6404ca85c8cd0b18a6b318bae1236d2ef021f4a
PLAN_BASE = b74b96d0163807007e4579d86450dd235125b30f
FICHAS_POSTEXEC = 804b59b73d7d2803d15e0adcb80546410a6718b8
PROMPT104 = 350677e7af3427dcfb7a9fd3fd05ebfe8e450fd1
PROMPT105 = 75197b8c48d4290fee05642e388194a56aa6c569 / SUPERSEDED_DO_NOT_EXECUTE
FIG007_RESPONSE = b94312c0149a4f5d0cec1680495a0b9731982dca
G6_F02_BRANCH = figures/g6-f02-render-v01
G6_F02_CANDIDATE_V01 = 2a483984eddc60dbbd48e7188b6fe9dbd7e829c5
G6_F02_CANDIDATE_PARENT = b6404ca85c8cd0b18a6b318bae1236d2ef021f4a
```

Estado operacional esperado:

```text
G6-F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G6-F02 = CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
G6-F03 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
GROUP6 = IN_PROGRESS
```

No modifiques Plan Maestro durante esta corrección candidata.

---

# 3. Contratos rectores

Lee íntegramente antes de editar:

```text
outputs/figures/group6/g6_figure_spec_registry_v0.1.json@b6404ca85c8cd0b18a6b318bae1236d2ef021f4a
figure_prompts_tmp/FIG007_RESPUESTA_PREAUDITORIA_VISUAL_CANDIDATO_G6_F02.md@b94312c0149a4f5d0cec1680495a0b9731982dca
codex_prompts_tmp/105_CORREGIR_G6_F02_HASH_LEDGER_Y_ACCESIBILIDAD_FIG03.md@75197b8c48d4290fee05642e388194a56aa6c569
```

Prompt105 se usa solo como fuente histórica de las dos correcciones conocidas; Prompt106 gobierna la ejecución actual.

Preserva:

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
EXP12 = CLOSED_WITHOUT_RETRIEVAL / DIVERSITY_EFFECT_NOT_ESTIMABLE
```

Guardrails:

```text
HISTORICAL_RETRIEVAL_SUPERIORITY_EQUALS_GLOBAL_RAG_ACCURACY = false
NORMATIVE_EVIDENCE_EQUALS_BINDING_LEGAL_CORRECTNESS = false
AUDITABLE_EXPLANATION_EQUALS_CLASSIFICATION_OR_LEGAL_CORRECTNESS = false
```

---

# 4. Base de corrección

Trabaja sobre la rama ya publicada:

```text
figures/g6-f02-render-v01
```

Su HEAD inicial debe ser exactamente:

```text
2a483984eddc60dbbd48e7188b6fe9dbd7e829c5
```

No reescribas ni fuerces la historia publicada. Crea **un único commit correctivo descendiente directo** de ese commit.

Tras la corrección, la rama quedará idealmente:

```text
COMMITS_AHEAD_VS_MAIN_BASE = 2
COMMITS_BEHIND_VS_MAIN_BASE = 0
```

El diff acumulado contra `MAIN_BASE` debe seguir conteniendo exactamente los mismos diez paths autorizados de G6-F02, sin paths nuevos.

---

# 5. Paths autorizados para la corrección

Puedes modificar exclusivamente:

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

No modifiques `.gitattributes`, requirements, datos fuente, registry G6-F01 ni ningún otro path del candidato.

---

# 6. Correcciones obligatorias consolidadas

Aplica **todas** las siguientes correcciones y ninguna otra modificación científica.

## C1 — Ledger sobre bytes canónicos Git/index

El ledger actual registra SHA-256/tamaños de bytes materializados CRLF del workspace para artefactos textuales, mientras Git almacena bytes canónicos normalizados.

Corrige `g6_figure_hash_ledger_v0.1.csv` de forma que `sha256` y `size_bytes` correspondan a los **bytes canónicos que realmente quedan versionados en Git**, no a una representación CRLF del working tree.

Procedimiento recomendado y auditable:

1. genera los scripts/outputs finales;
2. `git add` de los nueve artefactos script/output antes de construir el ledger;
3. calcula SHA-256 y tamaño a partir del contenido del **index** (`git show :path` / `git cat-file` o equivalente binario seguro), no desde el working tree;
4. construye el ledger con esos valores;
5. stagea el ledger;
6. después del commit, vuelve a verificar que cada fila coincide con los bytes de `HEAD:path`.

Para PNG usa igualmente bytes exactos versionados. No uses Git blob SHA como sustituto del SHA-256; el blob puede mantenerse solo como nota.

No modifiques `.gitattributes` para resolver esto.

## C2 — Tipografía mínima de G6-FIG-03

El registry exige mínimo efectivo **8.5 pt**.

Actualmente existen al menos:

```text
x-category labels = 7.5 pt
y-axis tick labels = 8.0 pt
```

Corrige **todas** las etiquetas/ticks efectivos de G6-FIG-03 para que ninguno quede por debajo de `8.5 pt`.

Mantén labels horizontales, orden categórico y layout científico 2×3. Revisa después que el aumento no produzca recortes ni colisiones.

## C3 — Oclusión de corridas individuales en G6-FIG-03

FIG007 detectó oclusión material de puntos en regiones densas, especialmente Top50/H25 y Top50/H50-D2.

Debes mejorar la discernibilidad de las 31 observaciones sin alterar información científica.

Preserva exactamente:

```text
31 OBSERVED_RUN
condition counts = 10 / 5 / 5 / 10 / 1
condition order = H25 | H50-D1 | H50-D2 | H75 | H100 ref.
all y values
run/seed ordering
same run-to-jitter identity across all six panels
H100 = one reference mark per panel
```

Preserva también los **vectores normalizados de jitter congelados del registry**:

```text
n10 = [-0.18,-0.14,-0.10,-0.06,-0.02,0.02,0.06,0.10,0.14,0.18]
n5  = [-0.12,-0.06,0.00,0.06,0.12]
n1  = [0.00]
```

Puedes ajustar únicamente la geometría visual que convierte esos offsets normalizados a coordenadas de dibujo (por ejemplo ancho útil/escala horizontal) y/o el radio/tamaño de marcador, siempre que:

- no cambies los offsets normalizados ni su asignación;
- no añadas jitter vertical;
- no muevas valores y;
- no provoques solapamiento entre categorías adyacentes;
- las marcas sigan siendo claramente visibles a tamaño de publicación;
- el ratio/layout general siga siendo 3:2 y 2×3;
- no introduzcas boxplots, medias, medianas, densidades ni summaries.

Haz una comprobación geométrica de separación/oclusión después de renderizar y documenta el resultado.

## C4 — Retirar identificadores internos de los títulos visibles

Retira de los títulos visibles de las tres figuras:

```text
G6-FIG-01 |
G6-FIG-02 |
G6-FIG-03 |
```

Conserva los IDs únicamente en filenames, registry y trazabilidad interna.

Mantén el texto descriptivo posterior al separador como título de trabajo visible, salvo ajustes de puntuación estrictamente necesarios.

## C5 — G6-FIG-01 Panel C: estado Attempt06 explícito

El registry fija la identidad de Panel C como:

```text
Hierarchical (Attempt06)
```

El candidato muestra solo `Hierarchical`.

Corrige la etiqueta a `Hierarchical (Attempt06)` o una variante line-broken semánticamente idéntica. No cambies estimando, CI, rango ni contexto.

## C6 — G6-FIG-02: título del eje y fuera del campo de datos

`Exact-NANDINA coverage` está actualmente dibujado horizontalmente desde `x=25` y penetra en el área de trazado.

Recolócalo inequívocamente fuera del campo de datos, mediante rotación vertical o disposición externa equivalente.

Requisitos:

- tamaño efectivo >= 10 pt;
- no alterar rango `[0,0.35]`;
- no mover datos;
- mantener 15 marcas;
- no modificar orden 50/100/200;
- no modificar identidad/formas de las cinco variantes;
- no reducir peso perceptual de la variante contextual.

---

# 7. Revalidación científica obligatoria

Después de las correcciones verifica nuevamente:

## G6-FIG-01

```text
panel_count = 3
A: 5 metrics × Historical/Flat/Hierarchical/D1a; no arm-level CI; x=[0,1]
B: 15 paired Historical-comparator contrasts; frozen 99% CI; zero line; x=[-0.1,1]
C: exactly one Recall@200-Recall@100 estimate; frozen 95% CI; zero line; x=[-0.1,1]
Pool@200 confirmatory estimate count = 0
p_value_count = 0
```

## G6-FIG-02

```text
panel_count = 1
mark_count = 15
formal variants = 4
context-only variants = 1
depths = 50 / 100 / 200
y_range = [0,0.35]
diagnostic_union performance marks = 0
CI_count = 0
p_value_count = 0
connecting_lines = 0
```

## G6-FIG-03

```text
panel_count = 6
metrics = Top1 / Top3 / Top5 / Top10 / Top50 / MRR
observed_run_count = 31
condition_counts = 10 / 5 / 5 / 10 / 1
frozen_summary_marks = 0
y_range_all_panels = [0,1]
H100_marks_per_panel = 1
CI_count = 0
p_value_count = 0
regression_count = 0
vertical_jitter = 0
minimum_effective_font_pt >= 8.5
```

No generes ninguna métrica científica nueva durante esta validación. Una métrica geométrica de solapamiento visual usada solo para QC no es resultado científico y no debe incorporarse a la figura ni a claims.

---

# 8. Reproducibilidad y determinismo

Ejecuta los tres scripts corregidos dos veces consecutivas con los mismos inputs.

Confirma:

```text
SVG_BYTE_IDENTICAL_RUN1_RUN2 = true
PNG_BYTE_IDENTICAL_RUN1_RUN2 = true
```

para las tres figuras.

Verifica que SVG y PNG de cada figura representan la misma información científica.

Registra:

- versión exacta de Python;
- versión de Pillow usada;
- cualquier otra dependencia realmente utilizada;
- ausencia de instalación/descarga de dependencias durante la corrección, salvo que exista autorización explícita (no existe en este prompt).

No añadas archivos de entorno al candidato.

---

# 9. Ledger final

El ledger final debe contener como mínimo las mismas 16 filas conceptuales actuales:

- registry;
- 6 inputs científicos;
- 3 scripts;
- 3 SVG;
- 3 PNG.

Cada fila debe ser verificable contra los bytes canónicos versionados.

Después del commit correctivo ejecuta una validación independiente que recorra el ledger y confirme:

```text
LEDGER_ROW_COUNT = 16
LEDGER_CANONICAL_SHA256_MATCH_COUNT = 16
LEDGER_CANONICAL_SIZE_MATCH_COUNT = 16
```

Si una fila no coincide, STOP: no publiques el candidato como listo para auditoría.

---

# 10. Commit correctivo candidato

Crea un único commit correctivo sobre `figures/g6-f02-render-v01`, parent exacto:

```text
2a483984eddc60dbbd48e7188b6fe9dbd7e829c5
```

Publica la rama sin force-push.

Registra:

```text
G6_F02_CORRECTED_CANDIDATE_COMMIT = <sha>
CORRECTION_PARENT = 2a483984eddc60dbbd48e7188b6fe9dbd7e829c5
CORRECTION_COMMIT_COUNT = 1
CUMULATIVE_CHANGED_PATH_COUNT_VS_MAIN_BASE = 10
COMMITS_AHEAD_VS_MAIN_BASE = 2
COMMITS_BEHIND_VS_MAIN_BASE = 0
```

---

# 11. Registro postcorrección de fichas

Sobre `docs/fichas-grupos-3-8`, partiendo exactamente de:

```text
804b59b73d7d2803d15e0adcb80546410a6718b8
```

modifica exclusivamente:

```text
docs/fichas/grupos_3_8/04_REGISTRO_ESTADO_FICHAS.md
```

NO cambies el estado terminal actual de G6-F02. Debe permanecer:

```text
CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
```

Añade un bloque de postcorrección con:

```text
FICHA = G6-F02
CORRECTION_GOVERNANCE = PROMPT106
FIG007_RESPONSE_COMMIT = b94312c0149a4f5d0cec1680495a0b9731982dca
PREVIOUS_CANDIDATE_COMMIT = 2a483984eddc60dbbd48e7188b6fe9dbd7e829c5
CORRECTED_CANDIDATE_COMMIT = <sha>
CORRECTION_SCOPE_COUNT = 6
LEDGER_CANONICAL_HASH_FIX = COMPLETE
FIG03_MIN_FONT_FIX = COMPLETE
FIG03_OCCLUSION_FIX = COMPLETE
VISIBLE_INTERNAL_ID_REMOVAL = COMPLETE
FIG01_PANEL_C_ATTEMPT06_LABEL_FIX = COMPLETE
FIG02_Y_AXIS_LABEL_PLACEMENT_FIX = COMPLETE
DETERMINISM_CHECK = PASS
EXTERNAL_AUDIT = PENDING
RESULT = CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
GROUP6 = IN_PROGRESS
G6_F03 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
G6_F03_AUTHORIZED = false
G6_F03_STARTED = false
GROUP7_AUTHORIZED = false
```

No modifiques Plan Maestro todavía.

---

# 12. Respuesta oficial

Persiste la respuesta completa en:

```text
codex_prompts_tmp/106_RESPUESTA_CORREGIR_G6_F02_SCOPE_CONSOLIDADO_POST_FIG007.md
```

sobre:

```text
codex/prompts-temporary
```

Incluye como mínimo:

```text
PROMPT106_EXECUTION
WORKSPACE_CONTRACT
MAIN_BASE
PLAN_BASE
FICHAS_POSTEXEC
PREVIOUS_CANDIDATE_COMMIT
CORRECTED_CANDIDATE_COMMIT
CORRECTION_PARENT
CORRECTION_CHANGED_PATHS
CUMULATIVE_CHANGED_PATH_COUNT_VS_MAIN_BASE
COMMITS_AHEAD_VS_MAIN_BASE
COMMITS_BEHIND_VS_MAIN_BASE
CORRECTION_SCOPE_COUNT
C1_LEDGER_CANONICAL_BYTES
C2_FIG03_MIN_FONT
C3_FIG03_OCCLUSION
C4_VISIBLE_INTERNAL_IDS
C5_FIG01_ATTEMPT06_LABEL
C6_FIG02_Y_AXIS_LABEL
FIGURE_VALIDATION_SUMMARY
DETERMINISM_CHECK
LEDGER_ROW_COUNT
LEDGER_CANONICAL_SHA256_MATCH_COUNT
LEDGER_CANONICAL_SIZE_MATCH_COUNT
PYTHON_VERSION
PILLOW_VERSION
FICHAS_FINAL
MAIN_FINAL
PLAN_FINAL
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

No declares G6-F02 `PASS`, `APPROVED`, `CLOSED` ni `INTEGRATED`.

---

# 13. Criterios posteriores de auditoría externa

La auditoría independiente deberá verificar simultáneamente:

1. el commit correctivo es descendiente directo de `2a483984...` y no reescribe historia;
2. el diff acumulado vs `MAIN_BASE` sigue limitado a los diez paths autorizados;
3. las seis correcciones C1–C6 están efectivamente resueltas;
4. ledger 16/16 verificable sobre bytes canónicos versionados;
5. determinismo SVG/PNG confirmado;
6. exactitud de valores, conteos, rangos y CI contra fuentes congeladas;
7. G6-FIG-03 mantiene exactamente 31 observaciones y jitter normalizado congelado, sin oclusión material que impida discernir multiplicidad;
8. ninguna etiqueta efectiva de G6-FIG-03 queda por debajo de 8.5 pt;
9. G6-FIG-02 mantiene 15 marcas, carácter descriptivo y eje y claro fuera del campo de datos;
10. G6-FIG-01 conserva CI 99%/95% correctamente separados y explicita `Hierarchical (Attempt06)` en Panel C;
11. no aparecen IDs `G6-FIG-0X |` en títulos visibles;
12. no hay nueva inferencia, métrica, CI ni p-value;
13. artículo/tesis/Plan Maestro permanecen sin modificación;
14. EXP12 no se reabre;
15. G6-F03 permanece no autorizado.

Si falla cualquiera de estos puntos, mantén G6-F02 pendiente de corrección y no avances.
