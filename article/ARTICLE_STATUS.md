# Estado del artículo / Article Status

## Español

### Estado general

- Rama de trabajo: `article/main-manuscript`.
- Estado global: `IN_ANALYSIS`.
- Fase vigente: `0A — Ground truth documental y experimental`.
- `0A-01 — Ground truth documental`: **`APPROVED / FROZEN`**.
- Bloque activo: **`0A-02 — Ground truth experimental`**.
- Estado de `0A-02`: **`EXPERIMENTAL_REVIEW`**.
- Prompt del bloque: `article/prompts/0A02_EXPERIMENTAL_GROUND_TRUTH.md`.
- Revisión interna: `article/reviews/0A02_INTERNAL_REVIEW.md`.
- Dictamen interno: **`PASS WITH MINOR NORMALIZATION`**.
- Target journal: `PENDING — se decidirá en Fase 0D`.
- Idioma del chat: español.
- Artefactos GitHub del entorno del artículo: español + inglés con equivalencia semántica.
- Manuscrito redactado: no iniciado.

### 0A-01 congelado

`0A-01` permanece `APPROVED / FROZEN`. Su referencia es:

`article/ground_truth/0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md`

El congelamiento documental no congela el estado experimental completo. `SRC-03` continúa siendo fuente viva y solo la IA experimental posee autoridad de escritura sobre el Plan Maestro.

### Corte experimental verificado para 0A-02

En la ejecución de la IA de redacción y en la revisión científica/editorial interna se verificó el mismo corte:

- `main = 95ffec45ae5a734545ae7bb2d8d530f42f8f056c`;
- `SRC-03` blob SHA `0a9a82181c6c3840f74f0272e5c225568474058b`;
- sin drift material entre la apertura, la ejecución de 0A-02 y la revisión interna.

### Dictamen interno de 0A-02

La entrega de 0A-02 superó la revisión científica/editorial interna con:

```text
0A-02 INTERNAL REVIEW = PASS WITH MINOR NORMALIZATION
READY_FOR_EXPERIMENTAL_REVIEW = true
```

Se validaron, entre otros, los siguientes puntos:

- benchmark v0.2 H100/DEV/EVAL, hashes e independencia entre particiones por DAM e `id_unico`;
- `SERIE` como unidad de análisis y `DAM` como unidad de agrupamiento cuando existe dependencia;
- métricas H100 congeladas y su interpretación como recuperación de candidatos;
- v0.1 como snapshot histórico y `995/1006` como hallazgo histórico autorizado, manteniendo `48/59 = REVIEW_REQUIRED`;
- duplicados y near-duplicates residuales separados conceptualmente del solapamiento por DAM;
- valores finales consolidados de EXP-04 para recuperación histórica, baselines normativos y D1a;
- integración candidato–evidencia con `3168/3168` asociaciones exactas NANDINA-8 y trazabilidad, sin convertir cobertura en corrección normativa;
- reranker LLM de 20 casos como diagnóstico limitado;
- HE4 como `PARTIALLY_SUPPORTED` con sus limitaciones reales de auditoría;
- EXP-08 como artefacto versionado, manteniendo su `HE5 = PARTIALLY_SUPPORTED` como interpretación histórica/intermedia y la decisión final `HE5 = PENDING_GROUP3`;
- Grupo 1 y Grupo 2A con sus cierres y limitaciones preservadas;
- EXP-11A cerrado/versionado y exclusivamente descriptivo, sin causalidad aislada del tamaño del banco;
- Forensic Audit 01, Gate 02, Real Ingest 01/Gate 03 y Bank Materialization como evidencia de procedencia/ingesta/materialización, no como resultados de retrieval;
- 10 bancos H150 + 10 bancos H200 materializados, con núcleo H100 preservado;
- `EXP-11B retrieval = PENDING`, H150/H200 sin resultados de retrieval, `EXP-12 = PENDING`, Grupo 2B pendiente y Grupo 3 pendiente;
- consistencia sustantiva actual de C01–C20.

### Normalización menor pendiente para el artefacto final

No se requiere repetir la ejecución de 0A-02. En el artefacto definitivo, cada fila de la matriz experimental deberá contener **un único estado 0A-02** de este vocabulario:

`FROZEN_CURRENT`, `EXECUTED_LIMITED`, `HISTORICAL_SNAPSHOT`, `PENDING`, `NOT_AUTHORIZED`, `REVIEW_REQUIRED`.

Las filas paraguas que mezclen estados deberán desagregarse, y los calificadores explicativos pasarán a las columnas de alcance o limitaciones. EXP-08 y su interpretación HE5 deben permanecer conceptualmente separados.

Esta normalización no modifica resultados ni claims.

### Estado científico que debe preservar la auditoría experimental

- H100: `2,950` series / `28` DAM / `66` códigos.
- DEV: `100` series / `6` DAM / `9` códigos.
- EVAL: `1,056` series / `67` DAM / `42` códigos.
- H100 Top-3: `709/1056 = 0.6714015151515151`, recuperación de candidatos.
- v0.1 `995/1006`: hallazgo histórico autorizado.
- `48/59`: `REVIEW_REQUIRED`.
- EXP-08 `HE5 = PARTIALLY_SUPPORTED`: interpretación histórica/intermedia específica.
- Decisión inferencial final HE5: `PENDING_GROUP3`.
- EXP-11A: descriptivo; causalidad aislada del tamaño no autorizada.
- EXP-11B Bank Materialization: cerrado; retrieval no ejecutado.
- H150/H200: sin métricas de retrieval autorizadas.
- EXP-12: pendiente.
- Grupo 2B: pendiente.
- Grupo 3 y decisión final HE2/HE5: pendientes.
- HE4 no demuestra corrección jurídica completa.
- Asociación normativa no equivale automáticamente a corrección normativa sustantiva.

### Trabajo autorizado ahora

Realizar exclusivamente la **auditoría experimental independiente de 0A-02**.

La IA experimental debe reconstruir y verificar directamente el estado experimental contra `main`, `SRC-03` y los artefactos versionados; revisar la entrega consolidada a través de este registro interno; comprobar especialmente las métricas finales EXP-04, EXP-11A, HE4, EXP-08, los gates de expansión histórica y la separación Bank Materialization vs EXP-11B retrieval; y reportar cualquier error material o regresión.

No iniciar 0B, no redactar el manuscrito y no modificar el Plan Maestro desde el flujo editorial.

### Próximo gate

1. recibir feedback de la IA experimental sobre 0A-02;
2. resolver observaciones experimentales, si las hubiera;
3. obtener `PASS — READY FOR AUTHOR APPROVAL`;
4. obtener aprobación expresa del autor;
5. consolidar el artefacto bilingüe definitivo de 0A-02;
6. marcar `0A-02 = APPROVED / FROZEN`;
7. solo entonces evaluar el cierre de 0A y la apertura de 0B.

---

## English

### Overall status

- Working branch: `article/main-manuscript`.
- Overall status: `IN_ANALYSIS`.
- Current phase: `0A — Documentary and experimental ground truth`.
- `0A-01 — Documentary ground truth`: **`APPROVED / FROZEN`**.
- Active block: **`0A-02 — Experimental ground truth`**.
- `0A-02` status: **`EXPERIMENTAL_REVIEW`**.
- Block prompt: `article/prompts/0A02_EXPERIMENTAL_GROUND_TRUTH.md`.
- Internal review: `article/reviews/0A02_INTERNAL_REVIEW.md`.
- Internal verdict: **`PASS WITH MINOR NORMALIZATION`**.
- Target journal: `PENDING — to be decided in Phase 0D`.
- Chat language: Spanish.
- Article-workspace GitHub artifacts: Spanish + English with semantic equivalence.
- Manuscript drafting: not started.

### Frozen 0A-01

`0A-01` remains `APPROVED / FROZEN`. Its reference artifact is:

`article/ground_truth/0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md`

The documentary freeze does not freeze the full experimental state. `SRC-03` remains a living source and only the experimental AI has write authority over the Master Plan.

### Experimental cutoff verified for 0A-02

The drafting-AI execution and the internal scientific/editorial review verified the same cutoff:

- `main = 95ffec45ae5a734545ae7bb2d8d530f42f8f056c`;
- `SRC-03` blob SHA `0a9a82181c6c3840f74f0272e5c225568474058b`;
- no material drift between 0A-02 opening, execution, and internal review.

### Internal verdict for 0A-02

The 0A-02 delivery passed internal scientific/editorial review with:

```text
0A-02 INTERNAL REVIEW = PASS WITH MINOR NORMALIZATION
READY_FOR_EXPERIMENTAL_REVIEW = true
```

Validated items include:

- v0.2 H100/DEV/EVAL benchmark, hashes, and cross-partition DAM/`id_unico` independence;
- `SERIES` as analysis unit and `DAM` as grouping unit when dependence exists;
- frozen H100 metrics and their candidate-retrieval interpretation;
- v0.1 as a historical snapshot and `995/1006` as an authorized historical finding, while `48/59 = REVIEW_REQUIRED`;
- residual duplicates/near-duplicates conceptually separated from DAM overlap;
- final consolidated EXP-04 values for historical retrieval, normative baselines, and D1a;
- candidate–evidence integration with `3168/3168` exact NANDINA-8 associations and traceability, without converting coverage into normative correctness;
- 20-case LLM reranker as a limited diagnostic;
- HE4 as `PARTIALLY_SUPPORTED` with its actual audit limitations;
- EXP-08 as a versioned artifact, retaining `HE5 = PARTIALLY_SUPPORTED` as historical/intermediate interpretation and `final HE5 = PENDING_GROUP3`;
- Group 1 and Group 2A closures with preserved limitations;
- EXP-11A closed/versioned and descriptive only, without isolated bank-size causality;
- Forensic Audit 01, Gate 02, Real Ingest 01/Gate 03, and Bank Materialization as provenance/ingestion/materialization evidence rather than retrieval outcomes;
- 10 H150 + 10 H200 banks materialized with preserved H100 core;
- `EXP-11B retrieval = PENDING`, no H150/H200 retrieval results, `EXP-12 = PENDING`, Group 2B pending, and Group 3 pending;
- current substantive consistency of C01–C20.

### Minor normalization pending for the final artifact

0A-02 does not need to be rerun. In the final artifact, each experimental-matrix row must contain **exactly one 0A-02 status** from:

`FROZEN_CURRENT`, `EXECUTED_LIMITED`, `HISTORICAL_SNAPSHOT`, `PENDING`, `NOT_AUTHORIZED`, `REVIEW_REQUIRED`.

Umbrella rows mixing statuses must be disaggregated, and explanatory qualifiers must move to scope or limitations fields. EXP-08 and its HE5 interpretation must remain conceptually separate.

This normalization does not alter results or claims.

### Scientific state the experimental audit must preserve

- H100: `2,950` series / `28` DAM / `66` codes.
- DEV: `100` series / `6` DAM / `9` codes.
- EVAL: `1,056` series / `67` DAM / `42` codes.
- H100 Top-3: `709/1056 = 0.6714015151515151`, candidate retrieval.
- v0.1 `995/1006`: authorized historical finding.
- `48/59`: `REVIEW_REQUIRED`.
- EXP-08 `HE5 = PARTIALLY_SUPPORTED`: experiment-specific historical/intermediate interpretation.
- Final inferential HE5 decision: `PENDING_GROUP3`.
- EXP-11A: descriptive; isolated causal bank-size effect unauthorized.
- EXP-11B Bank Materialization: closed; retrieval not executed.
- H150/H200: no authorized retrieval metrics.
- EXP-12: pending.
- Group 2B: pending.
- Group 3 and final HE2/HE5 decision: pending.
- HE4 does not demonstrate complete legal correctness.
- Normative association does not automatically establish substantive normative correctness.

### Work authorized now

Perform only the **independent experimental audit of 0A-02**.

The experimental AI must independently reconstruct and verify the experimental state against `main`, `SRC-03`, and versioned artifacts; review the consolidated delivery through this internal-review record; specifically check final EXP-04 metrics, EXP-11A, HE4, EXP-08, historical-expansion gates, and the Bank Materialization versus EXP-11B retrieval distinction; and report any material error or regression.

Do not start 0B, do not draft the manuscript, and do not modify the Master Plan from the editorial workflow.

### Next gate

1. receive experimental-AI feedback on 0A-02;
2. resolve experimental observations, if any;
3. obtain `PASS — READY FOR AUTHOR APPROVAL`;
4. obtain the author's express approval;
5. consolidate the final bilingual 0A-02 artifact;
6. mark `0A-02 = APPROVED / FROZEN`;
7. only then evaluate closure of 0A and opening of 0B.
