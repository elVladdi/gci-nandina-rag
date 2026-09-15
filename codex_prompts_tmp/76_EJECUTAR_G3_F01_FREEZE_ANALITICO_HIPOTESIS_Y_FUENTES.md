# PROMPT 76 — EJECUTAR EXCLUSIVAMENTE G3-F01: FREEZE ANALÍTICO, HIPÓTESIS Y FUENTES

## Rol y objetivo

Actúa como **ejecutor técnico controlado**.

El autor ha autorizado expresamente iniciar **Grupo 3 — Métricas e inferencia**. Esta autorización abre únicamente la primera ficha elegible:

`G3-F01 — Freeze analítico, hipótesis y fuentes`.

Este bloque debe producir un **contrato analítico candidato para auditoría externa** antes de cualquier cálculo inferencial. G3-F01 es una tarea de diseño analítico, trazabilidad y congelamiento prospectivo.

Este prompt **NO** ejecuta pruebas estadísticas, no calcula p-values, intervalos inferenciales ni tamaños de efecto, no reejecuta retrieval, no recalcula métricas científicas y no decide todavía HE2 ni HE5.

No avances a G3-F02.

---

## 1. Autoridad y estado que gobiernan este bloque

La autorización actual del autor es:

```text
USER_AUTHORIZATION_TO_START_GROUP3 = YES
GROUP3 = AUTHORIZED_TO_START
G3-F01 = AUTHORIZED_FOR_EXECUTION
G3-F02 = NOT_AUTHORIZED
STATISTICAL_INFERENCE = NOT_AUTHORIZED
HE2_FINAL_DECISION = NOT_AUTHORIZED
HE5_FINAL_DECISION = NOT_AUTHORIZED
```

`PROMPT75` permanece como registro histórico supersedido y **NO debe ejecutarse, editarse, reutilizarse ni completarse**.

Lee obligatoriamente:

```text
codex_prompts_tmp/75_SUPERSEDED_NO_EJECUTAR_G3_F01.md
```

Debe quedar confirmado:

```text
PROMPT75 = SUPERSEDED / DO_NOT_EXECUTE
```

Prompt76 constituye una autorización nueva, independiente y limitada exclusivamente a G3-F01.

---

## 2. Refs congelados al emitir Prompt76

Antes de cualquier modificación ejecuta `git fetch` y verifica exactamente:

```text
origin/main = a33fc7e10b5bc25a053e982f0ff24ff60eda042f
origin/docs/plan-maestro-temporal-2026-08-31 = f4d20dfe46181cb2740c4e4cd6604b0bff7a48f6
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
origin/docs/fichas-grupos-3-8 = a42531ad96fc12bea2f2394b0ff8eb49b66a4238
```

La ficha gobernante es:

```text
docs/fichas/grupos_3_8/grupo_3/G3_F01_FREEZE_ANALITICO_HIPOTESIS_Y_FUENTES.md
```

En el snapshot de fichas `a42531ad96fc12bea2f2394b0ff8eb49b66a4238`, su blob Git esperado es:

```text
4208e70a464e2a645644e9f9c5289cd7333afe48
```

Si cualquiera de los cuatro refs anteriores ha cambiado:

```text
STOP / REF_DRIFT_DETECTED
```

Reporta los SHA observados y no continúes.

No resuelvas drift por rebase, cherry-pick, merge, amend, reconstrucción manual ni inferencia.

---

## 3. Precondición formal de G3-F01

Lee íntegramente, desde `origin/docs/fichas-grupos-3-8 = a42531ad96fc12bea2f2394b0ff8eb49b66a4238`:

```text
docs/fichas/grupos_3_8/00_MAPA_MAESTRO_FICHAS_G3_G8.md
docs/fichas/grupos_3_8/01_GOBERNANZA_Y_ESTADOS.md
docs/fichas/grupos_3_8/02_MATRIZ_DEPENDENCIAS_Y_ENTRADAS.md
docs/fichas/grupos_3_8/04_REGISTRO_ESTADO_FICHAS.md
docs/fichas/grupos_3_8/grupo_3/G3_F01_FREEZE_ANALITICO_HIPOTESIS_Y_FUENTES.md
```

Lee también íntegramente el Plan Maestro desde:

```text
origin/docs/plan-maestro-temporal-2026-08-31 = f4d20dfe46181cb2740c4e4cd6604b0bff7a48f6
```

ruta:

```text
docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md
```

Verifica como mínimo:

```text
GROUP2B = CLOSED / APPROVED_WITH_NONBLOCKING_LIMITATIONS
BLOCKING_GAP_COUNT = 0
SCIENTIFIC_REEXECUTION_REQUIRED = false
RESULTS_RECOMPUTATION_REQUIRED = false
GROUP3 = NOT_STARTED
NEXT_ELIGIBLE_BLOCK = GROUP3_METRICS_AND_INFERENCE
NEXT_ELIGIBLE_FICHA = G3-F01

EXP12_ORIGINAL_FROZEN_DESIGN = CLOSED
EXP12_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
EXP12_DIVERSITY_EFFECT_ESTIMABLE = false
```

Si la precondición de G3-F01 no se cumple:

```text
STOP / G3_F01_PRECONDITION_FAILED
```

No modifiques el Plan Maestro ni la rama de fichas durante este bloque.

---

## 4. Fuente aprobada de HE2 y HE5

### 4.1 Regla de acceso a SRC-01

El Proyecto de tesis aprobado es `SRC-01` y gobierna la formulación exacta de las hipótesis.

Para esta ejecución, Codex NO debe afirmar que leyó directamente los bytes del PDF original si ese adjunto no está montado en su entorno.

IA Experimental verificó independientemente SRC-01 y la transcripción congelada, aprobada por el autor, disponible en GitHub. Por tanto, para G3-F01 usa como **transcripción verificable y congelada de SRC-01**:

```text
article/ground_truth/0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md
article/reviews/0A01_AUTHOR_APPROVAL.md
```

sobre:

```text
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
```

Bindings esperados:

```text
article/ground_truth/0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md
Git blob = 52c45948bbc085a25faf4df850ae15e6ca682d17

article/reviews/0A01_AUTHOR_APPROVAL.md
Git blob = db5cd447df1d85ee0f9d271e2a85af66e050aea1
```

Registra explícitamente en el contrato:

```text
SRC01_ORIGINAL = Proyecto de tesis para maestría MOLLEAPASA GUTIERREZ VLADIMIR.pdf
SRC01_ACCESS_MODE = AUTHOR_APPROVED_FROZEN_TRANSCRIPTION_IN_GITHUB
SRC01_DIRECT_PDF_BYTES_READ_BY_CODEX = false
SRC01_TRANSCRIPTION_STATUS = APPROVED / FROZEN / INDEPENDENTLY_VERIFIED_BY_IA_EXPERIMENTAL
```

Esto no convierte el artefacto editorial en sustituto general de fuentes científicas primarias. Se usa únicamente para recuperar las formulaciones aprobadas exactas congeladas por 0A-01. Para resultados experimentales consulta los artefactos científicos primarios versionados en `main`.

### 4.2 Texto exacto obligatorio

HE2 debe quedar literalmente:

```text
La recuperación histórica alcanzará un desempeño Top-k y MRR superior al de las estrategias de recuperación normativa, mientras que las variantes normativas jerárquicas y de conjunto candidato ampliarán la cobertura documental en posiciones más profundas.
```

HE5 debe quedar literalmente:

```text
Los errores y límites del piloto se concentrarán en descripciones ambiguas o incompletas, subpartidas jerárquicamente próximas, casos con precedentes históricos insuficientes y condiciones que restringirán la validez de los resultados al conjunto interno evaluado.
```

Si cualquiera de estos textos no coincide exactamente con el ground truth congelado:

```text
STOP / APPROVED_HYPOTHESIS_TEXT_MISMATCH
```

No reformules, resumas, fortalezas ni “mejores” ninguna hipótesis.

---

## 5. Lecturas obligatorias adicionales

Desde `article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5`, lee como mínimo:

```text
article/ground_truth/0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md
article/reviews/0A01_AUTHOR_APPROVAL.md
article/SOURCE_REGISTRY.md
```

Cuando leas archivos del artículo, hazlo directamente desde su rama. No los copies a `main` y no modifiques `article/main-manuscript`.

---

## 6. Principios experimentales congelados que G3-F01 debe preservar

El contrato debe preservar obligatoriamente:

```text
UNIT_OF_ANALYSIS = SERIE
DEPENDENCY_GROUP = DAM / DECLARACIÓN cuando exista dependencia
EVAL_V02_N = 1056
```

No trates automáticamente las 1,056 series como observaciones independientes cuando el contraste tenga estructura intra-DAM.

Arquitectura congelada:

```text
Descripción comercial
→ normalización
→ recuperación histórica
→ ranking histórico Top-k
→ Top-3 fijo
→ recuperación de evidencia normativa para esos candidatos
→ construcción de contexto
→ LLM local
→ explicación auditable del Top-3
```

Separación funcional:

```text
HISTORICAL_RETRIEVAL = genera y ordena candidatos
NORMATIVE_RETRIEVAL = aporta evidencia documental; no reemplaza ni reordena el ranking histórico
TOP3 = FIXED
LLM_LOCAL = explica el Top-3 recuperado; no clasifica desde cero
LLM_RERANKER = DIAGNOSTIC_ONLY
```

Restricciones congeladas:

```text
EXP11A_INFERENCE_SCOPE = SENSITIVITY_ONLY
EXP11A_ISOLATED_CAUSAL_BANK_SIZE_EFFECT = NOT_AUTHORIZED
EXP12_DIVERSITY_EFFECT = NOT_ESTIMABLE
FUTURE_0B05C_ANALYSES_MUST_USE = ATTEMPT06_CORRECTED_RESULTS
```

No mezcles particiones experimentales incompatibles.

---

## 7. Fuentes científicas mínimas a inventariar

G3-F01 no debe volver a calcular resultados. Debe reconstruir estáticamente qué familias de evidencia están disponibles y son admisibles para Grupo 3 a partir de:

```text
main = a33fc7e10b5bc25a053e982f0ff24ff60eda042f
```

Usa como índices de procedencia, pero no como sustitutos de evidencia primaria:

```text
outputs/audits/group2b_reproducibility_readiness_v0.2.json
outputs/audits/group2b_reproducibility_closure_v0.1.json
outputs/evaluation/exp04_consolidated_closure_v0.2/exp04_final_results_registry_v0.2.csv
outputs/evaluation/exp04_consolidated_closure_v0.2/exp04_final_provenance_registry_v0.2.csv
outputs/evaluation/exp04_consolidated_closure_v0.2/exp04_hypothesis_status_registry_v0.2.csv
```

A partir de esos registros y del Plan, abre los artefactos científicos primarios necesarios para verificar por lo menos estas familias:

1. **Grupo 1 / recuperación normativa e histórica H100 vigente**, relevantes para HE2.
2. **EXP11A**, H25/H50/H75/H100, únicamente como sensibilidad con tamaño/composición acoplados y sin interpretación causal aislada.
3. **EXP11B**, H150/H200 y sus réplicas aprobadas por condición.
4. **0B-05C**, exclusivamente Attempt06 corregido para cualquier resultado de ese bloque.
5. **HE5**, incluida la evidencia aprobada de errores y límites: matrices integradas, inventarios, case-level y artefactos cualitativos vigentes cuando sean metodológicamente compatibles.
6. **EXP12**, únicamente para registrar su disposición final: diseño original cerrado sin retrieval y efecto de diversidad `NOT_ESTIMABLE`.

No uses como resultado vigente ningún snapshot preliminar 3,000/1,006 ni outputs supersedidos.

No uses la tesis preliminar como fuente de cifras experimentales actuales.

---

## 8. Contrato analítico candidato

Crea una rama desde exactamente:

```text
a33fc7e10b5bc25a053e982f0ff24ff60eda042f
```

con nombre:

```text
codex/group3-f01-analytical-contract-v01
```

Publica un solo commit que añada exclusivamente:

```text
docs/analysis/group3/g3_analytical_contract_v0.1.md
outputs/analysis/group3/g3_analytical_contract_v0.1.json
```

No modifiques ningún archivo existente.

Ambos artefactos deben declarar:

```text
status = CANDIDATE_PENDING_EXTERNAL_AUDIT
ficha = G3-F01
scientific_main_commit = a33fc7e10b5bc25a053e982f0ff24ff60eda042f
canonical_plan_commit = f4d20dfe46181cb2740c4e4cd6604b0bff7a48f6
article_commit = 254b1e6df736fa9938ac86a515d65b36f4d361c5
fichas_snapshot_commit = a42531ad96fc12bea2f2394b0ff8eb49b66a4238
ficha_blob = 4208e70a464e2a645644e9f9c5289cd7333afe48
prompt = PROMPT76
```

---

## 9. Matriz obligatoria por familia de evidencia

Para cada familia relevante registra como mínimo:

- `evidence_family_id`;
- hipótesis/componente al que aporta (`HE2_A`, `HE2_B`, `HE5_*`, sensibilidad, limitación, etc.);
- experimento/bloque;
- paths científicos primarios;
- commit o binding aplicable;
- dataset/evalset exacto;
- N de series y, cuando corresponda, número de DAM;
- unidad de observación;
- unidad de agrupamiento/dependencia;
- condiciones comparadas;
- métrica(s) elegible(s);
- estimando que podría analizarse posteriormente;
- dirección prevista por la hipótesis cuando exista;
- clasificación de uso;
- limitaciones de interpretación;
- comparabilidad o no comparabilidad directa;
- necesidad posterior de control de multiplicidad;
- dependencia entre réplicas, seeds o condiciones;
- regla prospectiva de análisis si ese componente llega a G3-F02/G3-F03.

Las únicas clasificaciones terminales permitidas por G3-F01 son:

```text
ELIGIBLE
DESCRIPTIVE_ONLY
NOT_ESTIMABLE
NOT_APPLICABLE
```

No uses en G3-F01:

```text
SUPPORTED
PARTIALLY_SUPPORTED
REJECTED
SIGNIFICANT
NONSIGNIFICANT
```

ni ningún dictamen equivalente sobre hipótesis.

---

## 10. Descomposición obligatoria de HE2

HE2 contiene dos proposiciones distintas que no deben confundirse:

```text
HE2_A = historical early-ranking superiority
HE2_B = deeper documentary coverage from normative hierarchical / expanded-candidate variants
```

El contrato debe impedir comparaciones semánticamente inválidas.

Reglas obligatorias:

- Top-k/MRR histórico y normativo solo pueden contrastarse directamente cuando definición de métrica, población y unidad de evaluación sean comparables.
- Recall@N/Pool@N/cobertura documental profunda no se reinterpreta como MRR ni exactitud Top-k.
- Mayor cobertura profunda normativa no equivale a mejor ranking temprano.
- H150/H200 y EXP11A aportan sensibilidad/robustez del componente histórico; no sustituyen por sí solos la comparación primaria histórico-vs-normativo de HE2.

---

## 11. Tratamiento obligatorio de EXP11A

Registra como mínimo:

```text
EXP11A_INFERENCE_SCOPE = SENSITIVITY_ONLY
ISOLATED_CAUSAL_BANK_SIZE_EFFECT = NOT_AUTHORIZED
DESIGN = independent complete-DAM conditions
H50 = paired D1/D2 stratification
NESTING = NOT_REQUIRED / STRUCTURALLY_INFEASIBLE
SIZE_COMPOSITION_COUPLING = DECLARED_LIMITATION
```

Si se prevé una comparación inferencial futura, define prospectivamente la unidad y la estructura de dependencia apropiadas.

No trates las 1,056 series multiplicadas por las réplicas como observaciones independientes.

---

## 12. Tratamiento obligatorio de EXP11B

Registra H150/H200 como sensibilidad de expansión histórica con sus réplicas aprobadas.

Si más adelante se compara H150 vs H200, identifica documentalmente si existe pairing por seed y congela la unidad inferencial correspondiente antes de cualquier cálculo.

No atribuyas causalidad aislada al tamaño del banco si composición y tamaño no están separados experimentalmente.

---

## 13. Tratamiento obligatorio de 0B-05C

Debe quedar explícito:

```text
FUTURE_ANALYSES_MUST_USE = ATTEMPT06_CORRECTED_RESULTS
```

Todo output anterior supersedido debe quedar excluido del contrato inferencial.

No recalcules Attempt06.

---

## 14. Tratamiento obligatorio de EXP12

Debe quedar explícito:

```text
EXP12_ORIGINAL_FROZEN_DESIGN = CLOSED
EXP12_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
EXP12_DIVERSITY_EFFECT_ESTIMABLE = false
EXP12_ANALYTICAL_CLASSIFICATION = NOT_ESTIMABLE
D_HIGH_D_MID_D_LOW = NOT_SELECTED
```

No reconstruyas post hoc un experimento de diversidad y no uses diagnósticos no gobernantes para inventar un efecto estimable.

---

## 15. Tratamiento obligatorio de HE5

Separa, cuando los artefactos vigentes lo permitan, al menos:

- descripción ambigua o incompleta;
- proximidad jerárquica;
- soporte/precedentes históricos insuficientes;
- límites internos y de generalización;
- fallas de recuperación, evidencia o explicación cuando estén registradas por instrumentos compatibles.

El contrato debe indicar qué componentes son:

```text
ELIGIBLE
DESCRIPTIVE_ONLY
NOT_ESTIMABLE
NOT_APPLICABLE
```

No conviertas ausencia de evaluación en fallo.

Cuando una dimensión solo haya sido evaluada sobre una submuestra o instrumento específico, registra su población efectiva y no extrapoles automáticamente a las 1,056 series.

---

## 16. Regla estadística prospectiva

G3-F01 debe decidir **antes de cualquier inferencia** qué análisis posteriores son metodológicamente admisibles basándose en diseño, tipo de variable y dependencia, nunca en la significación o dirección que produzca un cálculo posterior.

Reglas obligatorias:

1. SERIE permanece como unidad de análisis.
2. DAM/DECLARACIÓN se preserva como unidad de agrupamiento cuando exista dependencia intra-DAM.
3. Réplicas, seeds y condiciones pareadas conservan su estructura; no pseudorreplicar series × corridas como independientes.
4. Cada contraste futuro debe quedar clasificado previamente como inferencialmente elegible, descriptivo/sensibilidad solamente, no estimable o no aplicable.
5. Si se propone una prueba futura, congela ahora, sin ejecutarla:
   - estimando;
   - hipótesis/contraste;
   - unidad inferencial;
   - pairing/cluster;
   - prueba o procedimiento;
   - intervalo de confianza si aplica;
   - tamaño de efecto si aplica;
   - familia de multiplicidad y corrección, o justificación expresa de que no aplica.
6. No introduzcas un umbral de significación como sustituto automático del criterio operacional aprobado de HE2/HE5.
7. No selecciones ninguna prueba en función del p-value o del resultado que produciría.

Si un procedimiento no puede justificarse prospectivamente con la información de diseño disponible, clasifica el componente conservadoramente y documenta la limitación; no improvises.

---

## 17. Verificación estática previa a publicar el candidato

Antes de crear el commit candidato verifica:

- refs exactos sin drift;
- existencia de todos los inputs citados;
- bindings Git/paths de los artefactos científicos primarios usados;
- ausencia de resultados supersedidos presentados como vigentes;
- ninguna mezcla de benchmark v0.2 con split preliminar 3,000/1,006;
- ningún cambio de métrica/población/exclusión inducido por resultados;
- ningún cálculo inferencial accidental;
- ningún write fuera de los dos outputs autorizados en la rama candidata.

Si detectas un riesgo que impida congelar prospectivamente un contraste sin ambigüedad:

```text
STOP / ANALYTICAL_CONTRACT_BLOCKER
```

No lo resuelvas observando inferencia.

---

## 18. Prohibiciones absolutas de Prompt76

Durante este bloque NO:

- calcules p-values;
- calcules nuevos intervalos de confianza;
- calcules nuevos tamaños de efecto;
- ejecutes tests estadísticos;
- recalcules métricas de recuperación;
- ejecutes retrieval, BM25, Top-k, MRR o candidate generation;
- reejecutes experimentos;
- regeneres case-level, rankings, manifests o datasets;
- modifiques resultados congelados;
- cambies HE2 o HE5;
- cierres HE2 o HE5;
- declares la hipótesis general respaldada/no respaldada;
- mezcles el antiguo split 3,000/1,006 con benchmark v0.2;
- trates series de una misma DAM como independientes cuando la inferencia requiera independencia;
- atribuyas efecto causal aislado a EXP11A/EXP11B;
- reabras EXP12;
- pruebes otros seeds de EXP12;
- generes D-HIGH/D-MID/D-LOW;
- modifiques `main`;
- modifiques `docs/plan-maestro-temporal-2026-08-31`;
- modifiques `docs/fichas-grupos-3-8`;
- modifiques `article/main-manuscript`;
- avances a G3-F02;
- avances a Grupo 4;
- redactes resultados, discusión o conclusiones de tesis/artículo.

---

## 19. Verificaciones finales

Exige al terminar:

```text
origin/main = a33fc7e10b5bc25a053e982f0ff24ff60eda042f
origin/docs/plan-maestro-temporal-2026-08-31 = f4d20dfe46181cb2740c4e4cd6604b0bff7a48f6
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
origin/docs/fichas-grupos-3-8 = a42531ad96fc12bea2f2394b0ff8eb49b66a4238
```

Para la rama candidata G3-F01 exige:

```text
parent = a33fc7e10b5bc25a053e982f0ff24ff60eda042f
commits_ahead = 1
commits_behind = 0
changed_path_count = 2
changed_paths =
  docs/analysis/group3/g3_analytical_contract_v0.1.md
  outputs/analysis/group3/g3_analytical_contract_v0.1.json
```

Confirma además:

```text
INFERENTIAL_CALCULATION_PERFORMED = false
P_VALUES_CALCULATED = false
METRICS_RECOMPUTED = false
SCIENTIFIC_EXPERIMENT_REEXECUTED = false
EXP12_REOPENED = false
HE2_DECIDED = false
HE5_DECIDED = false
G3_F02_STARTED = false
```

---

## 20. Persistencia administrativa

Al finalizar vuelve a `codex/prompts-temporary` y crea únicamente:

```text
codex_prompts_tmp/76_RESPUESTA_EJECUTAR_G3_F01_FREEZE_ANALITICO_HIPOTESIS_Y_FUENTES.md
```

El commit administrativo debe contener solo la respuesta de Prompt76.

No amend, no rebase, no force.

No modifiques Prompt75 ni su registro de supersesión.

---

## 21. Reporte obligatorio

Reporta como mínimo:

```text
PROMPT76 = COMPLETED | STOP

main_final
plan_final
article_final
fichas_snapshot_final

PROMPT75_STATUS
SRC01_ACCESS_MODE
SRC01_DIRECT_PDF_BYTES_READ_BY_CODEX
HE2_TEXT_EXACT_MATCH
HE5_TEXT_EXACT_MATCH

G3_F01_BRANCH
G3_F01_COMMIT
G3_F01_PARENT
G3_F01_COMMITS_AHEAD
G3_F01_COMMITS_BEHIND
G3_F01_CHANGED_PATH_COUNT
G3_F01_CHANGED_PATHS
G3_F01_PUBLISHED

EVIDENCE_FAMILY_COUNT
ELIGIBLE_COUNT
DESCRIPTIVE_ONLY_COUNT
NOT_ESTIMABLE_COUNT
NOT_APPLICABLE_COUNT

EXP11A_INFERENCE_SCOPE
ATTEMPT06_ONLY
EXP12_ANALYTICAL_CLASSIFICATION

INFERENTIAL_CALCULATION_PERFORMED = false
P_VALUES_CALCULATED = false
METRICS_RECOMPUTED = false
SCIENTIFIC_EXPERIMENT_REEXECUTED = false
EXP12_REOPENED = false
HE2_DECIDED = false
HE5_DECIDED = false
G3_F02_STARTED = false

EXTERNAL_AUDIT_REQUIRED = true
```

Respuesta terminal máxima:

```text
PROMPT76 = COMPLETED
G3_F01 = CANDIDATE_PENDING_EXTERNAL_AUDIT
INFERENTIAL_CALCULATION_PERFORMED = false
HE2_DECIDED = false
HE5_DECIDED = false
G3_F02_STARTED = false
```
