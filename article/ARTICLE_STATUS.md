# Estado del artículo / Article Status

## Español

### Estado general

- Rama de trabajo: `article/main-manuscript`.
- Estado global: `IN_ANALYSIS`.
- Fase `0A — Ground truth documental y experimental`: **`CLOSED / APPROVED`**.
- `0A-01 — Ground truth documental`: **`APPROVED / FROZEN`**.
- `0A-02 — Ground truth experimental`: **`APPROVED / FROZEN`**.
- Bloque activo: **ninguno**.
- `0B — Mapa crítico de literatura y taxonomía`: **`NOT_STARTED / NOT_YET_OPENED`**.
- Target journal: `PENDING — se decidirá en Fase 0D`.
- Idioma del chat: español.
- Artefactos GitHub del entorno del artículo: español + inglés con equivalencia semántica.
- Manuscrito redactado: no iniciado.

### Cierre formal de 0A-01

Estado:

```text
0A-01 = APPROVED / FROZEN
INTERNAL_REVIEW = PASS
EXPERIMENTAL_REVIEW = PASS
AUTHOR_APPROVAL = RECEIVED
```

Artefacto congelado:

`article/ground_truth/0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md`

Registros:

- `article/reviews/0A01_INTERNAL_REVIEW.md`;
- `article/reviews/0A01_EXPERIMENTAL_REVIEW.md`;
- `article/reviews/0A01_AUTHOR_APPROVAL.md`.

### Cierre formal de 0A-02

0A-02 completó:

1. ejecución de ground truth experimental por la IA de redacción;
2. revisión científica/editorial interna: `PASS WITH MINOR NORMALIZATION`;
3. auditoría experimental independiente: `PASS WITH MINOR NORMALIZATION — READY FOR AUTHOR APPROVAL`;
4. aprobación expresa del autor el `2026-09-02`;
5. normalización de estados de la matriz canónica;
6. consolidación del artefacto bilingüe definitivo;
7. congelamiento del bloque.

Estado final:

```text
0A-02 = APPROVED / FROZEN
INTERNAL_REVIEW = PASS WITH MINOR NORMALIZATION
EXPERIMENTAL_AUDIT = PASS WITH MINOR NORMALIZATION
MATERIAL_EXPERIMENTAL_ERRORS = 0
STATUS_NORMALIZATION = APPLIED
AUTHOR_APPROVAL = RECEIVED
```

Artefacto congelado:

`article/ground_truth/0A02_EXPERIMENTAL_GROUND_TRUTH_FROZEN.md`

Registros:

- `article/reviews/0A02_INTERNAL_REVIEW.md`;
- `article/reviews/0A02_EXPERIMENTAL_REVIEW.md`;
- `article/reviews/0A02_AUTHOR_APPROVAL.md`.

### Corte experimental congelado de 0A-02

El corte verificado durante ejecución y revisiones fue:

- `main = 95ffec45ae5a734545ae7bb2d8d530f42f8f056c`;
- `SRC-03` blob SHA `0a9a82181c6c3840f74f0272e5c225568474058b`;
- sin drift experimental material durante el ciclo de 0A-02.

Antes del cierre se volvió a verificar que `SRC-03` permanecía en el mismo blob SHA. El flujo editorial **no modificó el Plan Maestro**.

### Normalización aplicada

La matriz congelada de 0A-02 utiliza exactamente un estado por fila:

`FROZEN_CURRENT`, `EXECUTED_LIMITED`, `HISTORICAL_SNAPSHOT`, `PENDING`, `NOT_AUTHORIZED` o `REVIEW_REQUIRED`.

No existen estados combinados. En particular:

- EXP-08 como artefacto/análisis = `FROZEN_CURRENT`;
- EXP-08 `HE5 = PARTIALLY_SUPPORTED` como interpretación histórica/intermedia = `HISTORICAL_SNAPSHOT`;
- decisión inferencial final HE5 = `PENDING`.

### Ground truth experimental congelado

El cierre preserva, entre otros, los siguientes límites y hechos:

- H100: `2,950` series / `28` DAM / `66` códigos;
- DEV: `100` series / `6` DAM / `9` códigos;
- EVAL: `1,056` series / `67` DAM / `42` códigos;
- cero DAM y cero `id_unico` compartidos entre particiones;
- H100 Top-3: `709/1056 = 0.6714015151515151`, **recuperación de candidatos**, no accuracy global;
- resultados normativos y D1a gobernados por `exp04_final_results_registry_v0.2.csv`;
- integración: `3168/3168` asociaciones exactas NANDINA-8 y trazabilidad, sin inferir corrección normativa sustantiva;
- reranker LLM: diagnóstico de 20 casos, no benchmark;
- HE4: `PARTIALLY_SUPPORTED` dentro de sus limitaciones; no demuestra corrección jurídica completa;
- v0.1 `3,000/100/1,006` = snapshot histórico;
- `995/1006` = hallazgo histórico autorizado para explicar el rediseño del split;
- `48/59` = `REVIEW_REQUIRED`;
- EXP-11A = descriptivo/no causal;
- Real Ingest 01: `6,029` elegibles / `43` DAM / `56` NANDINA;
- Bank Materialization: 10 bancos H150 + 10 H200 materializados/auditados;
- `EXP-11B retrieval = PENDING`;
- H150/H200 = sin métricas de retrieval autorizadas;
- `EXP-12 = PENDING`;
- Grupo 2B = `PENDING`;
- Grupo 3 = `PENDING`;
- HE2/HE5 finales = pendientes hasta Grupo 3;
- generalización empírica fuera de Clase/Capítulo 87 = no autorizada;
- clasificación jurídicamente vinculante = fuera de alcance.

### Cierre de la Fase 0A

Con `0A-01` y `0A-02` aprobados y congelados:

```text
PHASE_0A = CLOSED / APPROVED
DOCUMENTARY_GROUND_TRUTH = FROZEN
EXPERIMENTAL_GROUND_TRUTH_AT_CUTOFF = FROZEN
```

El congelamiento de 0A no impide que `SRC-03` y los experimentos pendientes evolucionen en el flujo experimental. Las actualizaciones posteriores deberán ingresar al artículo mediante gates explícitos y no reescribir silenciosamente los artefactos históricos congelados.

### Trabajo autorizado ahora

Ningún nuevo bloque ha sido abierto automáticamente.

`0B` permanece `NOT_STARTED / NOT_YET_OPENED`. Antes de ejecutarlo debe realizarse su apertura formal, fijar su prompt y establecer el protocolo bibliográfico aplicable.

La selección y congelamiento de la revista objetivo **no se realiza en 0A ni en 0B**. Según `ARTICLE_WRITING_PLAN.md`, el target journal principal y sus alternativas se decidirán en **Fase 0D**, después de 0B y 0C.

---

## English

### Overall status

- Working branch: `article/main-manuscript`.
- Overall status: `IN_ANALYSIS`.
- Phase `0A — Documentary and experimental ground truth`: **`CLOSED / APPROVED`**.
- `0A-01 — Documentary ground truth`: **`APPROVED / FROZEN`**.
- `0A-02 — Experimental ground truth`: **`APPROVED / FROZEN`**.
- Active block: **none**.
- `0B — Critical literature map and taxonomy`: **`NOT_STARTED / NOT_YET_OPENED`**.
- Target journal: `PENDING — to be decided in Phase 0D`.
- Chat language: Spanish.
- Article-workspace GitHub artifacts: Spanish + English with semantic equivalence.
- Manuscript drafting: not started.

### Formal 0A-01 closure

```text
0A-01 = APPROVED / FROZEN
INTERNAL_REVIEW = PASS
EXPERIMENTAL_REVIEW = PASS
AUTHOR_APPROVAL = RECEIVED
```

Frozen artifact:

`article/ground_truth/0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md`

Records:

- `article/reviews/0A01_INTERNAL_REVIEW.md`;
- `article/reviews/0A01_EXPERIMENTAL_REVIEW.md`;
- `article/reviews/0A01_AUTHOR_APPROVAL.md`.

### Formal 0A-02 closure

0A-02 completed:

1. experimental-ground-truth execution by the drafting AI;
2. internal scientific/editorial review: `PASS WITH MINOR NORMALIZATION`;
3. independent experimental audit: `PASS WITH MINOR NORMALIZATION — READY FOR AUTHOR APPROVAL`;
4. express author approval on `2026-09-02`;
5. canonical-matrix status normalization;
6. consolidation of the final bilingual artifact;
7. block freeze.

Final state:

```text
0A-02 = APPROVED / FROZEN
INTERNAL_REVIEW = PASS WITH MINOR NORMALIZATION
EXPERIMENTAL_AUDIT = PASS WITH MINOR NORMALIZATION
MATERIAL_EXPERIMENTAL_ERRORS = 0
STATUS_NORMALIZATION = APPLIED
AUTHOR_APPROVAL = RECEIVED
```

Frozen artifact:

`article/ground_truth/0A02_EXPERIMENTAL_GROUND_TRUTH_FROZEN.md`

Records:

- `article/reviews/0A02_INTERNAL_REVIEW.md`;
- `article/reviews/0A02_EXPERIMENTAL_REVIEW.md`;
- `article/reviews/0A02_AUTHOR_APPROVAL.md`.

### Frozen 0A-02 experimental cutoff

The cutoff verified during execution and review was:

- `main = 95ffec45ae5a734545ae7bb2d8d530f42f8f056c`;
- `SRC-03` blob SHA `0a9a82181c6c3840f74f0272e5c225568474058b`;
- no material experimental drift during the 0A-02 cycle.

Before closure, `SRC-03` was reverified at the same blob SHA. The editorial workflow **did not modify the Master Plan**.

### Applied normalization

The frozen 0A-02 matrix uses exactly one status per row:

`FROZEN_CURRENT`, `EXECUTED_LIMITED`, `HISTORICAL_SNAPSHOT`, `PENDING`, `NOT_AUTHORIZED`, or `REVIEW_REQUIRED`.

No combined statuses remain. In particular:

- EXP-08 artifact/analysis = `FROZEN_CURRENT`;
- EXP-08 `HE5 = PARTIALLY_SUPPORTED` historical/intermediate interpretation = `HISTORICAL_SNAPSHOT`;
- final inferential HE5 decision = `PENDING`.

### Frozen experimental ground truth

Closure preserves, among other facts and boundaries:

- H100: `2,950` series / `28` DAM / `66` codes;
- DEV: `100` series / `6` DAM / `9` codes;
- EVAL: `1,056` series / `67` DAM / `42` codes;
- zero shared DAM and zero shared `id_unico` across partitions;
- H100 Top-3: `709/1056 = 0.6714015151515151`, **candidate retrieval**, not overall accuracy;
- normative and D1a results governed by `exp04_final_results_registry_v0.2.csv`;
- integration: `3168/3168` exact NANDINA-8 associations and traceability, without inferring substantive normative correctness;
- LLM reranker: 20-case diagnostic, not benchmark;
- HE4: `PARTIALLY_SUPPORTED` within its limitations; does not establish complete legal correctness;
- v0.1 `3000/100/1006` = historical snapshot;
- `995/1006` = authorized historical finding for split-redesign explanation;
- `48/59` = `REVIEW_REQUIRED`;
- EXP-11A = descriptive/non-causal;
- Real Ingest 01: `6,029` eligible / `43` DAM / `56` NANDINA;
- Bank Materialization: 10 H150 + 10 H200 banks materialized/audited;
- `EXP-11B retrieval = PENDING`;
- H150/H200 = no authorized retrieval metrics;
- `EXP-12 = PENDING`;
- Group 2B = `PENDING`;
- Group 3 = `PENDING`;
- final HE2/HE5 = pending until Group 3;
- empirical generalization outside Class/Chapter 87 = unauthorized;
- legally binding classification = out of scope.

### Phase 0A closure

With 0A-01 and 0A-02 approved and frozen:

```text
PHASE_0A = CLOSED / APPROVED
DOCUMENTARY_GROUND_TRUTH = FROZEN
EXPERIMENTAL_GROUND_TRUTH_AT_CUTOFF = FROZEN
```

Freezing 0A does not prevent `SRC-03` and pending experiments from evolving in the experimental workflow. Later updates must enter the article through explicit gates and must not silently rewrite frozen historical artifacts.

### Work authorized now

No new block has been opened automatically.

`0B` remains `NOT_STARTED / NOT_YET_OPENED`. Before execution it must be formally opened, its prompt fixed, and its bibliographic protocol established.

Target-journal selection and freeze **does not occur in 0A or 0B**. Under `ARTICLE_WRITING_PLAN.md`, the primary target journal and alternatives will be decided in **Phase 0D**, after 0B and 0C.