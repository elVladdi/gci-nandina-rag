# Estado del artículo / Article Status

## Español

### Estado general

- Rama de trabajo: `article/main-manuscript`.
- Estado global: `IN_ANALYSIS`.
- Fase vigente: `0A — Ground truth documental y experimental`.
- `0A-01 — Ground truth documental`: **`APPROVED / FROZEN`**.
- Bloque activo: **`0A-02 — Ground truth experimental`**.
- Estado de `0A-02`: **`AUTHOR_APPROVAL_PENDING`**.
- Prompt del bloque: `article/prompts/0A02_EXPERIMENTAL_GROUND_TRUTH.md`.
- Revisión interna: `article/reviews/0A02_INTERNAL_REVIEW.md`.
- Dictamen interno: **`PASS WITH MINOR NORMALIZATION`**.
- Revisión experimental: `article/reviews/0A02_EXPERIMENTAL_REVIEW.md`.
- Dictamen experimental: **`PASS WITH MINOR NORMALIZATION — READY FOR AUTHOR APPROVAL`**.
- Target journal: `PENDING — se decidirá en Fase 0D`.
- Idioma del chat: español.
- Artefactos GitHub del entorno del artículo: español + inglés con equivalencia semántica.
- Manuscrito redactado: no iniciado.

### 0A-01 congelado

`0A-01` permanece `APPROVED / FROZEN`. Su referencia es:

`article/ground_truth/0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md`

El congelamiento documental no congela el estado experimental completo. `SRC-03` continúa siendo fuente viva y solo la IA experimental posee autoridad de escritura sobre el Plan Maestro.

### Corte experimental verificado para 0A-02

La IA de redacción, la revisión científica/editorial interna y la auditoría experimental independiente verificaron el mismo corte experimental:

- `main = 95ffec45ae5a734545ae7bb2d8d530f42f8f056c`;
- `SRC-03` blob SHA `0a9a82181c6c3840f74f0272e5c225568474058b`;
- sin drift experimental material durante la ejecución y las revisiones de 0A-02.

### Resultado de la revisión interna

```text
0A-02 INTERNAL REVIEW = PASS WITH MINOR NORMALIZATION
READY_FOR_EXPERIMENTAL_REVIEW = true
```

La revisión interna verificó el benchmark v0.2, los resultados finales consolidados de EXP-04, la integración histórico–normativa, HE4, EXP-08, EXP-11A, los gates de expansión histórica y la distinción Bank Materialization ≠ retrieval.

### Resultado de la auditoría experimental independiente

```text
0A-02 EXPERIMENTAL AUDIT = PASS WITH MINOR NORMALIZATION
EXPERIMENTAL_FACTS = VERIFIED
MATERIAL_EXPERIMENTAL_ERRORS = 0
MINOR_GOVERNANCE_NORMALIZATION = 1
READY_FOR_AUTHOR_APPROVAL = true
0B_AUTHORIZED = false
```

La auditoría independiente confirmó, entre otros:

- benchmark v0.2 y métricas H100;
- Top-k como recuperación de candidatos;
- split sin DAM compartidas;
- duplicados/near-duplicates como dimensión distinta del solapamiento por DAM;
- uso de los valores finales de `exp04_final_results_registry_v0.2.csv`;
- integración histórico–normativa con `3168/3168` asociaciones exactas y preservación del ranking;
- reranker LLM como diagnóstico de 20 casos, no benchmark;
- HE4 como `PARTIALLY_SUPPORTED` con limitaciones prompt-schema y modalidad de evaluador IA;
- EXP-08 `HE5 = PARTIALLY_SUPPORTED` como interpretación histórica/intermedia específica, manteniendo `HE5 final = PENDING_GROUP3`;
- EXP-11A como descriptivo/no causal;
- Gate 02, Gate 03, Real Ingest y Bank Materialization separados de retrieval;
- 10 bancos H150 + 10 bancos H200 materializados sin convertirlos en resultados de retrieval;
- `EXP-11B retrieval = PENDING`;
- `EXP-12 = PENDING`;
- Grupo 2B = `PENDING`;
- Grupo 3 = `PENDING`.

### Normalización menor obligatoria para el artefacto definitivo

La única corrección pendiente es editorial/de gobernanza y **no modifica resultados ni claims**.

En la matriz experimental definitiva, cada fila deberá contener exactamente **un** estado 0A-02 de este vocabulario:

`FROZEN_CURRENT`, `EXECUTED_LIMITED`, `HISTORICAL_SNAPSHOT`, `PENDING`, `NOT_AUTHORIZED`, `REVIEW_REQUIRED`.

No se admitirán estados combinados. Las filas paraguas con componentes de diferente estado deberán desagregarse.

EXP-08 deberá quedar separado explícitamente en tres registros conceptuales:

- artefacto/análisis EXP-08: `FROZEN_CURRENT`;
- interpretación `HE5 = PARTIALLY_SUPPORTED` específica de EXP-08: `HISTORICAL_SNAPSHOT`;
- decisión inferencial final HE5: `PENDING`.

Esta normalización se aplicará durante la consolidación del artefacto definitivo después de la aprobación expresa del autor y antes de marcar `0A-02 = APPROVED / FROZEN`.

### Estado científico que debe conservar el cierre

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

El siguiente gate es **exclusivamente la aprobación expresa del autor de 0A-02**.

No se requiere otra ronda con la IA de redacción ni con la IA experimental antes de esa decisión. No iniciar 0B, no redactar el manuscrito y no modificar el Plan Maestro desde el flujo editorial.

### Próximo gate

1. obtener aprobación expresa del autor de 0A-02;
2. consolidar el artefacto bilingüe definitivo aplicando la normalización de estados;
3. registrar la aprobación del autor;
4. marcar `0A-02 = APPROVED / FROZEN`;
5. verificar que no se haya modificado el Plan Maestro desde el flujo editorial;
6. solo entonces evaluar el cierre completo de 0A y la apertura de 0B.

---

## English

### Overall status

- Working branch: `article/main-manuscript`.
- Overall status: `IN_ANALYSIS`.
- Current phase: `0A — Documentary and experimental ground truth`.
- `0A-01 — Documentary ground truth`: **`APPROVED / FROZEN`**.
- Active block: **`0A-02 — Experimental ground truth`**.
- `0A-02` status: **`AUTHOR_APPROVAL_PENDING`**.
- Block prompt: `article/prompts/0A02_EXPERIMENTAL_GROUND_TRUTH.md`.
- Internal review: `article/reviews/0A02_INTERNAL_REVIEW.md`.
- Internal verdict: **`PASS WITH MINOR NORMALIZATION`**.
- Experimental review: `article/reviews/0A02_EXPERIMENTAL_REVIEW.md`.
- Experimental verdict: **`PASS WITH MINOR NORMALIZATION — READY FOR AUTHOR APPROVAL`**.
- Target journal: `PENDING — to be decided in Phase 0D`.
- Chat language: Spanish.
- Article-workspace GitHub artifacts: Spanish + English with semantic equivalence.
- Manuscript drafting: not started.

### Frozen 0A-01

`0A-01` remains `APPROVED / FROZEN`. Its reference artifact is:

`article/ground_truth/0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md`

The documentary freeze does not freeze the full experimental state. `SRC-03` remains a living source and only the experimental AI has write authority over the Master Plan.

### Experimental cutoff verified for 0A-02

The drafting AI, internal scientific/editorial review, and independent experimental audit verified the same experimental cutoff:

- `main = 95ffec45ae5a734545ae7bb2d8d530f42f8f056c`;
- `SRC-03` blob SHA `0a9a82181c6c3840f74f0272e5c225568474058b`;
- no material experimental drift during 0A-02 execution and review.

### Internal-review result

```text
0A-02 INTERNAL REVIEW = PASS WITH MINOR NORMALIZATION
READY_FOR_EXPERIMENTAL_REVIEW = true
```

The internal review verified the v0.2 benchmark, final consolidated EXP-04 results, historical–normative integration, HE4, EXP-08, EXP-11A, historical-expansion gates, and the Bank Materialization ≠ retrieval distinction.

### Independent experimental-audit result

```text
0A-02 EXPERIMENTAL AUDIT = PASS WITH MINOR NORMALIZATION
EXPERIMENTAL_FACTS = VERIFIED
MATERIAL_EXPERIMENTAL_ERRORS = 0
MINOR_GOVERNANCE_NORMALIZATION = 1
READY_FOR_AUTHOR_APPROVAL = true
0B_AUTHORIZED = false
```

The independent audit confirmed, among other items:

- v0.2 benchmark and H100 metrics;
- Top-k as candidate retrieval;
- split without shared DAMs;
- duplicates/near-duplicates as a dimension distinct from DAM overlap;
- use of final `exp04_final_results_registry_v0.2.csv` values;
- historical–normative integration with `3168/3168` exact associations and preserved ranking;
- LLM reranker as a 20-case diagnostic rather than a benchmark;
- HE4 as `PARTIALLY_SUPPORTED` with prompt-schema and AI-evaluator modality limitations;
- EXP-08 `HE5 = PARTIALLY_SUPPORTED` as an experiment-specific historical/intermediate interpretation while keeping `final HE5 = PENDING_GROUP3`;
- EXP-11A as descriptive/non-causal;
- Gate 02, Gate 03, Real Ingest, and Bank Materialization separated from retrieval;
- 10 H150 + 10 H200 banks materialized without treating them as retrieval outcomes;
- `EXP-11B retrieval = PENDING`;
- `EXP-12 = PENDING`;
- Group 2B = `PENDING`;
- Group 3 = `PENDING`.

### Mandatory minor normalization for the final artifact

The only remaining correction concerns editorial/governance normalization and **does not alter results or claims**.

Each row in the final experimental matrix must contain exactly **one** 0A-02 status from:

`FROZEN_CURRENT`, `EXECUTED_LIMITED`, `HISTORICAL_SNAPSHOT`, `PENDING`, `NOT_AUTHORIZED`, `REVIEW_REQUIRED`.

Combined statuses are not permitted. Umbrella rows containing components with different statuses must be disaggregated.

EXP-08 must be explicitly separated into three conceptual records:

- EXP-08 artifact/analysis: `FROZEN_CURRENT`;
- experiment-specific `HE5 = PARTIALLY_SUPPORTED` interpretation: `HISTORICAL_SNAPSHOT`;
- final inferential HE5 decision: `PENDING`.

This normalization will be applied during final artifact consolidation after express author approval and before `0A-02 = APPROVED / FROZEN` is recorded.

### Scientific state to preserve at closure

- H100: `2,950` series / `28` DAM / `66` codes.
- DEV: `100` series / `6` DAM / `9` codes.
- EVAL: `1,056` series / `67` DAM / `42` codes.
- H100 Top-3: `709/1056 = 0.6714015151515151`, candidate retrieval.
- v0.1 `995/1006`: authorized historical finding.
- `48/59`: `REVIEW_REQUIRED`.
- EXP-08 `HE5 = PARTIALLY_SUPPORTED`: experiment-specific historical/intermediate interpretation.
- Final inferential HE5 decision: `PENDING_GROUP3`.
- EXP-11A: descriptive; isolated bank-size causality unauthorized.
- EXP-11B Bank Materialization: closed; retrieval not executed.
- H150/H200: no authorized retrieval metrics.
- EXP-12: pending.
- Group 2B: pending.
- Group 3 and final HE2/HE5 decisions: pending.
- HE4 does not demonstrate complete legal correctness.
- Normative association does not automatically establish substantive normative correctness.

### Work authorized now

The next gate is **exclusively the author's express approval of 0A-02**.

No additional drafting-AI or experimental-AI round is required before that decision. Do not start 0B, do not draft the manuscript, and do not modify the Master Plan from the editorial workflow.

### Next gate

1. obtain express author approval of 0A-02;
2. consolidate the final bilingual artifact while applying status normalization;
3. record author approval;
4. mark `0A-02 = APPROVED / FROZEN`;
5. verify that the editorial workflow did not modify the Master Plan;
6. only then evaluate full 0A closure and opening of 0B.
