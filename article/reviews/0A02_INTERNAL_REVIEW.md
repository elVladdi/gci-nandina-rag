# Revisión interna 0A-02 / 0A-02 Internal Review

## Español

### Identificación

- Bloque revisado: `0A-02 — Ground truth experimental`.
- Insumo revisado: entrega de la IA de redacción ejecutada contra el corte de apertura de 0A-02.
- Fecha de revisión: 2026-09-02.
- Dictamen interno: **PASS WITH MINOR NORMALIZATION**.
- Siguiente gate autorizado: **auditoría experimental independiente de 0A-02**.
- No se autoriza 0B ni ninguna sección del manuscrito.

### Corte verificado por la edición científica

Durante esta revisión se volvió a comprobar directamente:

- `article/main-manuscript` en el corte abierto para 0A-02;
- `main = 95ffec45ae5a734545ae7bb2d8d530f42f8f056c`;
- `SRC-03` blob SHA `0a9a82181c6c3840f74f0272e5c225568474058b`.

No se detectó drift experimental respecto del corte utilizado por la IA de redacción.

### Aspectos científicamente validados

La entrega reconstruye correctamente, dentro del alcance de 0A-02:

1. el benchmark v0.2 vigente: H100 `2,950` series / `28` DAM / `66` códigos; DEV `100` / `6` / `9`; EVAL `1,056` / `67` / `42`, con los hashes congelados y cero solapamiento de DAM e `id_unico` entre particiones;
2. la distinción `SERIE = unidad de análisis` y `DAM = unidad de agrupamiento cuando existe dependencia`, sin convertir las 1,056 series de EVAL en observaciones automáticamente independientes;
3. las métricas H100 congeladas: Top-1 `538/1056 = 0.509469696969697`, Top-3 `709/1056 = 0.6714015151515151`, Top-5 `806/1056 = 0.7632575757575758`, Top-10 `941/1056 = 0.8910984848484849`, Top-50 `1047/1056 = 0.9914772727272727` y MRR `0.6297077493524843`;
4. el carácter de **recuperación de candidatos** del Top-k histórico y la prohibición de denominarlo accuracy global del sistema/RAG;
5. v0.1 `3,000/100/1,006` como `HISTORICAL_SNAPSHOT`, incluido `995/1006` como hallazgo histórico autorizado para explicar el rediseño del split, mientras `48/59` permanece `REVIEW_REQUIRED`;
6. los duplicados y near-duplicates residuales de v0.2 como dimensión distinta del solapamiento por DAM: exactos `35/1056`; near >=0.90 `55`; near >=0.95 `44`; near >=0.98 `37`;
7. los valores vigentes del registro final EXP-04 para los baselines normativos y D1a. En particular, la entrega usa correctamente el **registro final consolidado**, por lo que no deben reintroducirse cifras anteriores de snapshots pre-cierre;
8. la integración histórico-normativa: `3168/3168` slots con asociación exacta NANDINA-8 y trazabilidad, preservando el ranking histórico; asociación/cobertura no equivale a corrección normativa sustantiva;
9. el reranker LLM de 20 casos como diagnóstico limitado y no como benchmark;
10. HE4 como evidencia limitada: 50 explicaciones, `28/50` auditables, media `11.72`, `HE4 = PARTIALLY_SUPPORTED`, evaluador IA y limitación prompt-schema; no demuestra corrección jurídica completa;
11. EXP-08 como análisis versionado vigente, manteniendo `HE5 = PARTIALLY_SUPPORTED` únicamente como interpretación histórica/intermedia específica de EXP-08 y `HE5 final = PENDING_GROUP3`;
12. Grupo 1 cerrado/aprobado y Grupo 2A cerrado con limitaciones no bloqueantes, sin reinterpretar cierre operativo como ausencia de limitaciones;
13. EXP-11A cerrado/versionado y exclusivamente descriptivo. Los agregados verificados en `exp11_learning_curve.csv` coinciden con la entrega: H25 Top-3 `0.6451704545` / MRR `0.6037871777`; H50 `0.5979166667` / `0.5424923539`; H75 `0.4633522727` / `0.4140298710`; H100 `0.6714015152` / `0.6297077494`. No se autoriza efecto causal aislado del tamaño;
14. la reconstrucción forense histórica como parcial, aun cuando H100/DEV/EVAL puedan reproducirse byte a byte desde el contenido procesado disponible;
15. Gate 02, Real Ingest 01/Gate 03 y Bank Materialization como evidencia de ingesta, diseño, identidad y reproducibilidad de bancos, no como resultados de retrieval;
16. Real Ingest 01: `6,029` filas elegibles, `43` DAM y `56` NANDINA, sin modificación de H100/DEV/EVAL congelados;
17. Bank Materialization Gate: 10 bancos H150 + 10 bancos H200 materializados y auditados, con preservación del núcleo H100;
18. `EXP-11B retrieval = PENDING`, sin métricas H150/H200 autorizadas; `EXP-12 = PENDING`; Grupo 2B = pendiente; Grupo 3 = pendiente; HE2/HE5 finales = pendientes;
19. consistencia sustantiva con `CLAIM_EVIDENCE_MATRIX.md`, sin necesidad de modificar actualmente los estados de C01–C20.

### Corrección menor obligatoria para la consolidación final

La evidencia científica no requiere una nueva ejecución de 0A-02, pero la futura matriz congelada debe normalizar la columna `estado 0A-02` para que **cada fila tenga un único estado del vocabulario permitido**: `FROZEN_CURRENT`, `EXECUTED_LIMITED`, `HISTORICAL_SNAPSHOT`, `PENDING`, `NOT_AUTHORIZED` o `REVIEW_REQUIRED`.

Por tanto:

- filas paraguas como EV-03 no deben usar `FROZEN_CURRENT / EXECUTED_LIMITED según componente`; deben desagregarse por componente o dejar el estado fuera de la fila paraguas y trasladar la clasificación a filas específicas;
- EXP-08 y su interpretación HE5 deben mantenerse en filas conceptualmente distintas: el artefacto/análisis EXP-08 puede ser `FROZEN_CURRENT`, mientras la interpretación `HE5 = PARTIALLY_SUPPORTED` es `HISTORICAL_SNAPSHOT` respecto de la decisión inferencial final;
- calificadores explicativos deben ir en `alcance permitido` o `limitaciones`, no concatenarse al valor del estado.

Esta normalización es editorial/de gobernanza y no cambia ningún resultado ni claim.

### Precauciones que deben preservarse

- Los valores normativos y D1a del `exp04_final_results_registry_v0.2.csv` son los valores finales gobernantes para 0A-02; no mezclar con cifras de estados experimentales anteriores.
- La cobertura normativa exacta NANDINA-8 `3168/3168` expresa asociación documental por candidato, no suficiencia semántica, validez normativa ni corrección jurídica.
- Los denominadores `common-clean` prospectivos de EXP-11B son análisis complementarios futuros y no reemplazan el N primario de EVAL = `1056`.
- `exp11_findings.md` conserva la etiqueta histórica `DESCRIPTIVE_PRE_EXTERNAL_AUDIT`; el estado final de EXP-11A se rige por los artefactos posteriores de freeze/reconciliación y por el Plan Maestro.
- La materialización H150/H200 no autoriza ninguna dirección del efecto sobre retrieval.

### Gate

La entrega supera la revisión científica/editorial interna. No es necesario devolverla a la IA de redacción antes de la auditoría experimental; la normalización menor se aplicará al artefacto definitivo si el bloque supera el gate experimental y la aprobación del autor.

Estado interno:

```text
0A-02 INTERNAL REVIEW = PASS WITH MINOR NORMALIZATION
READY_FOR_EXPERIMENTAL_REVIEW = true
0B_AUTHORIZED = false
```

---

## English

### Identification

- Reviewed block: `0A-02 — Experimental ground truth`.
- Reviewed input: drafting-AI delivery executed against the 0A-02 opening cutoff.
- Review date: 2026-09-02.
- Internal verdict: **PASS WITH MINOR NORMALIZATION**.
- Authorized next gate: **independent experimental audit of 0A-02**.
- Phase 0B and all manuscript sections remain unauthorized.

### Cutoff independently checked by scientific editing

This review rechecked directly:

- the `article/main-manuscript` cutoff opened for 0A-02;
- `main = 95ffec45ae5a734545ae7bb2d8d530f42f8f056c`;
- `SRC-03` blob SHA `0a9a82181c6c3840f74f0272e5c225568474058b`.

No experimental drift was detected relative to the cutoff used by the drafting AI.

### Scientifically validated aspects

The delivery correctly reconstructs, within the scope of 0A-02:

1. the current v0.2 benchmark: H100 `2,950` series / `28` DAM / `66` codes; DEV `100` / `6` / `9`; EVAL `1,056` / `67` / `42`, with frozen hashes and zero DAM and `id_unico` overlap across partitions;
2. `SERIES = analysis unit` and `DAM = grouping unit when dependence exists`, without treating the 1,056 EVAL series as automatically independent observations;
3. frozen H100 metrics: Top-1 `538/1056 = 0.509469696969697`, Top-3 `709/1056 = 0.6714015151515151`, Top-5 `806/1056 = 0.7632575757575758`, Top-10 `941/1056 = 0.8910984848484849`, Top-50 `1047/1056 = 0.9914772727272727`, and MRR `0.6297077493524843`;
4. the candidate-retrieval meaning of historical Top-k and the prohibition on calling it overall system/RAG accuracy;
5. v0.1 `3,000/100/1,006` as a `HISTORICAL_SNAPSHOT`, including `995/1006` as an authorized historical finding for explaining split redesign, while `48/59` remains `REVIEW_REQUIRED`;
6. residual duplicates and near-duplicates in v0.2 as distinct from DAM overlap: exact `35/1056`; near >=0.90 `55`; near >=0.95 `44`; near >=0.98 `37`;
7. the current final EXP-04 registry values for normative baselines and D1a. The delivery correctly uses the **final consolidated registry**, so earlier pre-closure snapshot figures must not be reintroduced;
8. historical–normative integration: `3168/3168` candidate slots with exact NANDINA-8 association and traceability while preserving historical ranking; association/coverage is not substantive normative correctness;
9. the 20-case LLM reranker as a limited diagnostic rather than a benchmark;
10. HE4 as limited evidence: 50 explanations, `28/50` auditable, mean `11.72`, `HE4 = PARTIALLY_SUPPORTED`, AI evaluator, and prompt-schema limitation; it does not demonstrate complete legal correctness;
11. EXP-08 as a current versioned analysis while keeping `HE5 = PARTIALLY_SUPPORTED` only as a historical/intermediate interpretation specific to EXP-08 and `final HE5 = PENDING_GROUP3`;
12. Group 1 closed/approved and Group 2A closed with nonblocking limitations, without interpreting operational closure as absence of limitations;
13. EXP-11A closed/versioned and descriptive only. Verified aggregates in `exp11_learning_curve.csv` match the delivery: H25 Top-3 `0.6451704545` / MRR `0.6037871777`; H50 `0.5979166667` / `0.5424923539`; H75 `0.4633522727` / `0.4140298710`; H100 `0.6714015152` / `0.6297077494`. No isolated causal bank-size effect is authorized;
14. historical forensic reconstruction as partial even though H100/DEV/EVAL can be reproduced byte-for-byte from the available processed content;
15. Gate 02, Real Ingest 01/Gate 03, and Bank Materialization as evidence of ingestion, design, bank identity, and reproducibility, not retrieval outcomes;
16. Real Ingest 01: `6,029` eligible rows, `43` DAM, and `56` NANDINA, with frozen H100/DEV/EVAL unchanged;
17. Bank Materialization Gate: 10 H150 + 10 H200 banks materialized and audited, preserving the H100 core;
18. `EXP-11B retrieval = PENDING`, with no authorized H150/H200 retrieval metrics; `EXP-12 = PENDING`; Group 2B pending; Group 3 pending; final HE2/HE5 decisions pending;
19. substantive consistency with `CLAIM_EVIDENCE_MATRIX.md`, with no current need to change C01–C20 statuses.

### Mandatory minor correction for final consolidation

The scientific evidence does not require rerunning 0A-02, but the future frozen matrix must normalize the `0A-02 status` column so that **each row has exactly one permitted status**: `FROZEN_CURRENT`, `EXECUTED_LIMITED`, `HISTORICAL_SNAPSHOT`, `PENDING`, `NOT_AUTHORIZED`, or `REVIEW_REQUIRED`.

Therefore:

- umbrella rows such as EV-03 must not use `FROZEN_CURRENT / EXECUTED_LIMITED depending on component`; they must be disaggregated by component or leave classification to specific rows;
- EXP-08 and its HE5 interpretation must remain conceptually separate: the EXP-08 artifact/analysis may be `FROZEN_CURRENT`, while the `HE5 = PARTIALLY_SUPPORTED` interpretation is `HISTORICAL_SNAPSHOT` relative to the final inferential decision;
- explanatory qualifiers belong in `permitted scope` or `limitations`, not concatenated into the status value.

This is an editorial/governance normalization and does not alter any experimental result or claim.

### Precautions to preserve

- Normative and D1a values in `exp04_final_results_registry_v0.2.csv` are the governing final values for 0A-02; do not mix them with earlier experimental-state figures.
- Exact NANDINA-8 coverage `3168/3168` means candidate-linked documentary association, not semantic sufficiency, normative validity, or legal correctness.
- Prospective EXP-11B `common-clean` denominators are complementary future analyses and do not replace primary EVAL N = `1056`.
- `exp11_findings.md` retains the historical label `DESCRIPTIVE_PRE_EXTERNAL_AUDIT`; final EXP-11A status is governed by later freeze/reconciliation artifacts and the Master Plan.
- H150/H200 bank materialization authorizes no direction of retrieval effect.

### Gate

The delivery passes internal scientific/editorial review. It does not need to be returned to the drafting AI before experimental audit; the minor normalization will be applied to the final artifact if the block passes the experimental gate and author approval.

Internal status:

```text
0A-02 INTERNAL REVIEW = PASS WITH MINOR NORMALIZATION
READY_FOR_EXPERIMENTAL_REVIEW = true
0B_AUTHORIZED = false
```
