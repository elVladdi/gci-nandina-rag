# PROMPT 75 — INTEGRAR GOBERNANZA G3–G8 Y EJECUTAR EXCLUSIVAMENTE G3-F01

## Rol y objetivo

Actúa como **ejecutor técnico controlado**.

Este bloque realiza exclusivamente dos transiciones ya autorizadas metodológicamente:

1. integrar mediante fast-forward exacto el candidato del Plan Maestro que registra la gobernanza prospectiva de las 19 fichas G3–G8;
2. ejecutar **únicamente G3-F01 — Freeze analítico, hipótesis y fuentes**, produciendo un contrato analítico candidato para auditoría externa.

G3-F01 es una tarea de diseño analítico y trazabilidad **sin cálculo inferencial**. Este prompt NO ejecuta pruebas estadísticas, no calcula p-values, intervalos o tamaños de efecto, no reejecuta retrieval, no recalcula métricas científicas y no decide todavía HE2 ni HE5.

No avances a G3-F02.

---

## 1. Dictamen externo que gobierna este bloque

La auditoría externa de IA Experimental sobre Prompt74 concluye:

```text
PROMPT74_EXTERNAL_AUDIT = PASS / APPROVED
PLAN_GROUP2B_CLOSURE_V02 = INTEGRATED / VERIFIED
G3_G8_GOVERNANCE_PLAN_V01 = APPROVED_FOR_INTEGRATION
FICHAS_G3_G8 = REGISTERED_PROSPECTIVELY / NOT_AUTHORIZED
GROUP3 = NOT_STARTED
NEXT_ELIGIBLE_FICHA = G3-F01
```

Estado exacto previo:

```text
origin/main = a33fc7e10b5bc25a053e982f0ff24ff60eda042f
origin/docs/plan-maestro-temporal-2026-08-31 = d2c9bcdc8099df20890cd52cb1e6cc32208b686f
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
origin/docs/fichas-grupos-3-8 = a42531ad96fc12bea2f2394b0ff8eb49b66a4238
origin/codex/plan-maestro-g3-g8-governance-v01 = f4d20dfe46181cb2740c4e4cd6604b0bff7a48f6
```

El candidato de gobernanza del Plan:

```text
parent = d2c9bcdc8099df20890cd52cb1e6cc32208b686f
commits_ahead = 1
commits_behind = 0
changed_path_count = 1
changed_path = docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md
```

La ficha gobernante es:

```text
docs/fichas/grupos_3_8/grupo_3/G3_F01_FREEZE_ANALITICO_HIPOTESIS_Y_FUENTES.md
```

En el snapshot de fichas `a42531ad96fc12bea2f2394b0ff8eb49b66a4238`, su blob Git es:

```text
4208e70a464e2a645644e9f9c5289cd7333afe48
```

---

## 2. Fase A — integrar el Plan de gobernanza G3–G8

Ejecuta `git fetch` y verifica exactamente los refs del apartado 1.

Integra exclusivamente mediante fast-forward exacto:

```text
d2c9bcdc8099df20890cd52cb1e6cc32208b686f
→
f4d20dfe46181cb2740c4e4cd6604b0bff7a48f6
```

en:

```text
docs/plan-maestro-temporal-2026-08-31
```

Prohibidos merge commit, squash, cherry-pick, rebase, amend o reconstrucción manual.

Después exige:

```text
origin/docs/plan-maestro-temporal-2026-08-31 = f4d20dfe46181cb2740c4e4cd6604b0bff7a48f6
origin/main = a33fc7e10b5bc25a053e982f0ff24ff60eda042f
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
origin/docs/fichas-grupos-3-8 = a42531ad96fc12bea2f2394b0ff8eb49b66a4238
```

No modifiques ninguna de esas ramas salvo el fast-forward exacto del Plan indicado.

---

## 3. Fuente aprobada de HE2 y HE5

### 3.1 Regla de acceso a SRC-01

El Proyecto de tesis aprobado es `SRC-01` y continúa gobernando la formulación exacta de las hipótesis. Para esta ejecución, Codex NO debe afirmar que leyó directamente los bytes del PDF original si ese adjunto no está montado en su entorno.

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

Esto no convierte el artefacto editorial en sustituto general de las fuentes científicas primarias: se usa únicamente para la **formulación aprobada exacta** que dicho artefacto congela. Para resultados experimentales debes consultar los artefactos científicos primarios versionados en `main`.

### 3.2 Texto exacto obligatorio

HE2 debe quedar **literalmente**:

```text
La recuperación histórica alcanzará un desempeño Top-k y MRR superior al de las estrategias de recuperación normativa, mientras que las variantes normativas jerárquicas y de conjunto candidato ampliarán la cobertura documental en posiciones más profundas.
```

HE5 debe quedar **literalmente**:

```text
Los errores y límites del piloto se concentrarán en descripciones ambiguas o incompletas, subpartidas jerárquicamente próximas, casos con precedentes históricos insuficientes y condiciones que restringirán la validez de los resultados al conjunto interno evaluado.
```

Si cualquiera de estos textos no coincide exactamente con el ground truth congelado:

```text
STOP / APPROVED_HYPOTHESIS_TEXT_MISMATCH
```

No reformules, resumas ni “mejores” ninguna hipótesis.

---

## 4. Lecturas obligatorias de gobernanza

En checkout/lectura estática de los refs exactos ya fijados, lee como mínimo:

```text
# Plan ya integrado
docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md

# Fichas
docs/fichas/grupos_3_8/00_MAPA_MAESTRO_FICHAS_G3_G8.md
docs/fichas/grupos_3_8/01_GOBERNANZA_Y_ESTADOS.md
docs/fichas/grupos_3_8/02_MATRIZ_DEPENDENCIAS_Y_ENTRADAS.md
docs/fichas/grupos_3_8/grupo_3/G3_F01_FREEZE_ANALITICO_HIPOTESIS_Y_FUENTES.md

# Formulación aprobada
article/ground_truth/0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md
article/reviews/0A01_AUTHOR_APPROVAL.md
article/SOURCE_REGISTRY.md
```

Cuando leas archivos del artículo, hazlo desde `article/main-manuscript`; no los copies a `main`.

---

## 5. Fuentes científicas mínimas a inventariar

G3-F01 no debe volver a calcular resultados. Debe reconstruir estáticamente qué familias de evidencia están disponibles y son admisibles para G3 a partir de `main=a33fc7e...`.

Usa como índices de procedencia, pero no como sustitutos de la evidencia primaria:

```text
outputs/audits/group2b_reproducibility_readiness_v0.2.json
outputs/audits/group2b_reproducibility_closure_v0.1.json
outputs/evaluation/exp04_consolidated_closure_v0.2/exp04_final_results_registry_v0.2.csv
outputs/evaluation/exp04_consolidated_closure_v0.2/exp04_final_provenance_registry_v0.2.csv
outputs/evaluation/exp04_consolidated_closure_v0.2/exp04_hypothesis_status_registry_v0.2.csv
```

A partir de esos registros y del Plan, abre los artefactos científicos primarios necesarios para verificar por lo menos estas familias:

1. **Grupo 1 / recuperación normativa e histórica H100 vigente**, relevantes para HE2;
2. **EXP11A**, H25/H50/H75/H100, únicamente como análisis de sensibilidad con tamaño/composición acoplados y sin interpretación causal aislada;
3. **EXP11B**, H150/H200 y sus 10 réplicas aprobadas por condición;
4. **0B-05C**, exclusivamente Attempt06 corregido para cualquier resultado que pertenezca a ese bloque;
5. **evidencia de errores y límites** disponible para HE5, incluida la matriz integrada/error inventories y artefactos cualitativos/case-level que estén aprobados y vigentes;
6. **EXP12**, exclusivamente para registrar su disposición final: diseño original cerrado sin retrieval y efecto de diversidad `NOT_ESTIMABLE`.

No uses como resultado vigente ningún snapshot experimental preliminar de 3,000/1,006 ni outputs supersedidos.

No uses la tesis preliminar como fuente de cifras experimentales actuales.

---

## 6. Contrato analítico que debe congelarse

Crea una rama desde exactamente:

```text
a33fc7e10b5bc25a053e982f0ff24ff60eda042f
```

con nombre:

```text
codex/group3-f01-analytical-contract-v01
```

Un solo commit que añada exclusivamente:

```text
docs/analysis/group3/g3_analytical_contract_v0.1.md
outputs/analysis/group3/g3_analytical_contract_v0.1.json
```

No modifiques archivos existentes.

Ambos artefactos deben tener:

```text
status = CANDIDATE_PENDING_EXTERNAL_AUDIT
ficha = G3-F01
scientific_main_commit = a33fc7e10b5bc25a053e982f0ff24ff60eda042f
canonical_plan_commit = f4d20dfe46181cb2740c4e4cd6604b0bff7a48f6
article_commit = 254b1e6df736fa9938ac86a515d65b36f4d361c5
fichas_snapshot_commit = a42531ad96fc12bea2f2394b0ff8eb49b66a4238
ficha_blob = 4208e70a464e2a645644e9f9c5289cd7333afe48
```

### 6.1 Matriz obligatoria por familia de evidencia

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
- si existe o no comparabilidad directa entre métricas/estrategias;
- si requiere control de multiplicidad posteriormente;
- cualquier dependencia entre réplicas/seed/condiciones.

Las únicas clasificaciones terminales permitidas por G3-F01 son:

```text
ELIGIBLE
DESCRIPTIVE_ONLY
NOT_ESTIMABLE
NOT_APPLICABLE
```

No uses `SUPPORTED`, `REJECTED`, `SIGNIFICANT`, `NONSIGNIFICANT` ni dictámenes de hipótesis en G3-F01.

### 6.2 Descomposición mínima de HE2

HE2 contiene dos proposiciones distintas y no deben confundirse:

```text
HE2_A = historical early-ranking superiority
HE2_B = deeper documentary coverage from normative hierarchical / expanded-candidate variants
```

El contrato debe impedir comparaciones semánticamente inválidas. En particular:

- Top-k/MRR histórico y normativo solo pueden contrastarse directamente cuando la definición de la métrica, la población y la unidad de evaluación sean comparables;
- Recall@N/Pool@N/cobertura documental profunda no debe reinterpretarse como MRR o exactitud Top-k;
- una mayor cobertura profunda normativa no equivale a mejor ranking temprano;
- H150/H200 y EXP11A son evidencia de sensibilidad/robustez del componente histórico, no sustituyen por sí solos la comparación primaria histórico-vs-normativo de HE2.

### 6.3 Tratamiento obligatorio de EXP11A

Registra como mínimo:

```text
EXP11A_INFERENCE_SCOPE = SENSITIVITY_ONLY
ISOLATED_CAUSAL_BANK_SIZE_EFFECT = NOT_AUTHORIZED
DESIGN = independent complete-DAM conditions
H50 = paired D1/D2 stratification
NESTING = NOT_REQUIRED / STRUCTURALLY_INFEASIBLE
SIZE_COMPOSITION_COUPLING = DECLARED_LIMITATION
```

Si se prevé una comparación inferencial futura, debe definirse por adelantado la unidad y estructura de dependencia apropiadas. No trates las 1,056 series multiplicadas por las réplicas como observaciones independientes.

### 6.4 Tratamiento obligatorio de EXP11B

Registra H150/H200 como sensibilidad de expansión histórica con sus réplicas aprobadas. Si más adelante se compara H150 vs H200, identifica si existe pairing por seed y congela la unidad inferencial correspondiente antes de cualquier cálculo.

No atribuyas causalidad aislada al tamaño del banco si composición y tamaño no están separados experimentalmente.

### 6.5 Tratamiento obligatorio de 0B-05C

```text
FUTURE_ANALYSES_MUST_USE = ATTEMPT06_CORRECTED_RESULTS
```

Cualquier output anterior supersedido debe quedar excluido explícitamente.

### 6.6 Tratamiento obligatorio de EXP12

```text
EXP12_ORIGINAL_FROZEN_DESIGN = CLOSED
EXP12_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
EXP12_DIVERSITY_EFFECT_ESTIMABLE = false
EXP12_ANALYTICAL_CLASSIFICATION = NOT_ESTIMABLE
D_HIGH_D_MID_D_LOW = NOT_SELECTED
GLOBAL_MATHEMATICAL_INFEASIBILITY_PROVEN = false
OTHER_SEEDS_CHARACTERIZED = false
```

No uses el diagnóstico forense no gobernante para inventar un efecto de diversidad.

### 6.7 HE5

Para HE5 separa, cuando la evidencia lo permita, al menos:

- descripción ambigua/incompleta;
- proximidad jerárquica;
- soporte/precedentes históricos insuficientes;
- límites internos y de generalización;
- fallas de recuperación, evidencia o explicación cuando estén registradas por instrumentos compatibles.

El contrato debe indicar qué componentes son cuantificables, cuáles solo descriptivos/cualitativos y cuáles no son comparables entre instrumentos.

No conviertas ausencia de evaluación en fallo.

---

## 7. Regla estadística prospectiva

G3-F01 debe decidir **antes de cualquier inferencia** qué análisis posteriores son metodológicamente admisibles, basándose en diseño, tipo de variable y dependencia; no en la significación o dirección observada.

Reglas obligatorias:

1. **SERIE** permanece como unidad de análisis.
2. **DAM/DECLARACIÓN** debe preservarse como unidad de agrupamiento cuando exista dependencia intra-DAM.
3. Réplicas, seeds y condiciones pareadas deben conservar su estructura; no deben pseudorreplicarse series × corridas como independientes.
4. Para cada contraste futuro indica si será:
   - inferencial elegible;
   - descriptivo/sensibilidad solamente;
   - no estimable;
   - no aplicable.
5. Si se propone una prueba estadística futura, congela en este contrato, sin ejecutarla:
   - estimando;
   - hipótesis/contraste;
   - unidad inferencial;
   - estructura de pairing/cluster;
   - prueba o procedimiento;
   - intervalo de confianza si aplica;
   - tamaño de efecto si aplica;
   - familia de multiplicidad y corrección, o justificación explícita de que no aplica.
6. No introduzcas un umbral de significación como sustituto automático del criterio operacional aprobado de HE2/HE5. La evidencia inferencial puede apoyar la interpretación, pero la decisión posterior de HE2/HE5 deberá mantener trazabilidad a su formulación y criterios aprobados.
7. No selecciones una prueba en función del p-value o del resultado que produciría.

Si alguna prueba no puede justificarse prospectivamente con la información de diseño disponible, clasifica ese componente conservadoramente y documenta la limitación; no improvises.

---

## 8. Prohibiciones absolutas de Prompt75

Durante este bloque NO:

- calcules p-values;
- calcules nuevos intervalos de confianza;
- calcules nuevos tamaños de efecto;
- ejecutes tests estadísticos;
- recalcules métricas de recuperación;
- ejecutes retrieval, BM25, Top-k, MRR o candidate generation;
- reejecutes ningún experimento;
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
- modifiques la rama `docs/fichas-grupos-3-8`;
- modifiques `article/main-manuscript`;
- avances a G3-F02;
- redactes resultados, discusión o conclusiones de tesis/artículo.

---

## 9. Verificaciones finales

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

## 10. Persistencia administrativa

Al finalizar vuelve a `codex/prompts-temporary` y crea únicamente:

```text
codex_prompts_tmp/75_RESPUESTA_INTEGRAR_GOBERNANZA_G3_G8_Y_EJECUTAR_G3_F01_FREEZE_ANALITICO.md
```

El commit administrativo debe contener solo esa respuesta. No amend, no rebase, no force.

---

## 11. Reporte obligatorio

Reporta como mínimo:

```text
PROMPT75 = COMPLETED | STOP

main_final
plan_initial
plan_final
article_final
fichas_snapshot_final
PLAN_G3_G8_GOVERNANCE_INTEGRATED

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
HE2_DECIDED = false
HE5_DECIDED = false
G3_F02_STARTED = false
```

Respuesta terminal máxima:

```text
PROMPT75 = COMPLETED
PLAN_G3_G8_GOVERNANCE = INTEGRATED
G3_F01 = CANDIDATE_PENDING_EXTERNAL_AUDIT
INFERENTIAL_CALCULATION_PERFORMED = false
HE2_DECIDED = false
HE5_DECIDED = false
G3_F02_STARTED = false
```
