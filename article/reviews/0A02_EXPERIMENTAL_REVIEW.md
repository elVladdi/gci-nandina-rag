# Revisión experimental 0A-02 / 0A-02 Experimental Review

## Español

### Identificación

- Bloque revisado: `0A-02 — Ground truth experimental`.
- Fecha de revisión: 2026-09-02.
- Revisor: IA experimental independiente.
- HEAD de `article/main-manuscript` revisado: `523ccba3109c2fe67fec57237461681e1a6d300c`.
- Dictamen experimental: **PASS WITH MINOR NORMALIZATION**.
- Estado de pase: **READY_FOR_AUTHOR_APPROVAL = true**, condicionado únicamente a aplicar la normalización de estados durante la consolidación del artefacto definitivo.
- Errores experimentales materiales detectados: `0`.
- `0B_AUTHORIZED = false`.

### Verificación independiente

La auditoría experimental contrastó directamente la reconstrucción de 0A-02 contra `main`, `SRC-03` y los artefactos experimentales versionados. Se verificaron como correctos:

- benchmark v0.2;
- métricas H100 Top-k y MRR;
- interpretación de Top-k como recuperación de candidatos;
- split sin DAM compartidas entre particiones;
- separación conceptual entre dependencia por DAM y duplicados/near-duplicates;
- valores finales consolidados de EXP-04;
- integración histórico–normativa;
- reranker LLM como diagnóstico de 20 casos;
- HE4 y sus limitaciones;
- EXP-08 y la separación entre HE5 histórico/intermedio y HE5 final;
- EXP-11A como análisis descriptivo/no causal;
- gates de expansión histórica;
- distinción Bank Materialization ≠ retrieval;
- `EXP-11B retrieval = PENDING`;
- `EXP-12 = PENDING`;
- Grupo 2B = `PENDING`;
- Grupo 3 = `PENDING`.

### EXP-04

La auditoría confirmó que 0A-02 utiliza el registro consolidado final `exp04_final_results_registry_v0.2.csv` y no cifras de snapshots previos. Se preservan, entre otros, H100 Top-3 `709/1056 = 0.671402`, los valores finales de los baselines normativos y los resultados finales de D1a.

Los baselines normativos se interpretan únicamente como recuperación de evidencia documental y no como sustitutos del ranking histórico.

### Integración histórico–normativa

Se verificaron:

- `1056` casos;
- `3168` slots candidatos;
- asociación exacta candidato–evidencia `3168/3168`;
- `candidate_exact_evidence_rate = 1.0`;
- `historical_rank_invariance_rate = 1.0`;
- `top3_invariance_rate = 1.0`;
- `traceability_complete_rate = 1.0`.

La interpretación autorizada permanece: **asociación documental exacta no equivale a corrección normativa sustantiva**.

### Reranker diagnóstico

Se verificó el alcance de 20 casos:

- `calls = 20`;
- Top-1 antes y después = `10/20 = 0.5`;
- Top-3 antes y después = `13/20 = 0.65`;
- `delta_mrr = 0`;
- sin prueba inferencial preespecificada;
- `scope = DIAGNOSTIC SAMPLE ONLY`.

No constituye benchmark ni evidencia de generalización.

### HE4

Se verificaron:

- `50` casos;
- `28/50 = 56%` auditables bajo la evaluación cualitativa;
- media `11.72`;
- mediana `12`;
- ausencia de hard violations en la evaluación cualitativa;
- evaluador IA en rol experto, no revisión humana independiente;
- `HE4 = PARTIALLY_SUPPORTED`;
- `PROMPT_SCHEMA_SPECIFICATION_MISMATCH`;
- `EVALUATOR_MODALITY_DEVIATION`.

Por tanto, HE4 puede utilizarse únicamente como evidencia limitada de estructura, trazabilidad y auditabilidad bajo su protocolo. No demuestra corrección jurídica completa.

### EXP-08 y HE5

La auditoría confirmó que:

- EXP-08 permanece como artefacto/análisis versionado;
- `HE5 = PARTIALLY_SUPPORTED` dentro de EXP-08 se conserva únicamente como interpretación histórica/intermedia específica de ese experimento;
- la decisión inferencial final permanece `HE5 = PENDING_GROUP3`.

### EXP-11A y expansión histórica

Se confirmó que EXP-11A está cerrado, aprobado y versionado, con interpretación exclusivamente descriptiva. No se autoriza inferir un efecto causal aislado del tamaño del banco.

Asimismo, Gate 02, Gate 03, Real Ingest y Bank Materialization permanecen correctamente separados de retrieval. La existencia de 10 bancos H150 y 10 bancos H200 materializados no constituye evidencia de rendimiento H150/H200.

### Estado experimental sin drift

Durante la auditoría:

- `main` permanecía en `95ffec45ae5a734545ae7bb2d8d530f42f8f056c`;
- no existían resultados de retrieval H150/H200;
- `EXP-11B retrieval = PENDING`;
- `EXP-12 = PENDING`;
- Grupo 2B = `PENDING`;
- Grupo 3 = `PENDING`.

### Normalización menor obligatoria para el artefacto definitivo

La única corrección pendiente es de gobernanza/editorial y no altera resultados ni claims.

En la matriz experimental congelada, cada fila deberá tener exactamente **un** estado de este vocabulario:

`FROZEN_CURRENT`, `EXECUTED_LIMITED`, `HISTORICAL_SNAPSHOT`, `PENDING`, `NOT_AUTHORIZED`, `REVIEW_REQUIRED`.

No se permiten estados combinados. Si una fila paraguas contiene componentes con estados distintos, deberá desagregarse.

En particular:

- EXP-08 como artefacto/análisis: `FROZEN_CURRENT`;
- interpretación `HE5 = PARTIALLY_SUPPORTED` de EXP-08: `HISTORICAL_SNAPSHOT` respecto de la decisión inferencial final;
- decisión inferencial final HE5: `PENDING`.

Esta normalización se aplicará al consolidar el artefacto definitivo después de la aprobación del autor y antes de marcar `0A-02 = APPROVED / FROZEN`.

### Gate experimental

Estado formal:

```text
0A-02 EXPERIMENTAL AUDIT = PASS WITH MINOR NORMALIZATION
EXPERIMENTAL_FACTS = VERIFIED
MATERIAL_EXPERIMENTAL_ERRORS = 0
MINOR_GOVERNANCE_NORMALIZATION = 1
READY_FOR_AUTHOR_APPROVAL = true
0B_AUTHORIZED = false
```

No se requiere repetir 0A-02 ni devolver la entrega a la IA de redacción.

---

## English

### Identification

- Reviewed block: `0A-02 — Experimental ground truth`.
- Review date: 2026-09-02.
- Reviewer: independent experimental AI.
- Reviewed `article/main-manuscript` HEAD: `523ccba3109c2fe67fec57237461681e1a6d300c`.
- Experimental verdict: **PASS WITH MINOR NORMALIZATION**.
- Gate status: **READY_FOR_AUTHOR_APPROVAL = true**, conditioned only on applying status normalization during final artifact consolidation.
- Material experimental errors found: `0`.
- `0B_AUTHORIZED = false`.

### Independent verification

The experimental audit directly checked the 0A-02 reconstruction against `main`, `SRC-03`, and versioned experimental artifacts. The following were verified as correct:

- v0.2 benchmark;
- H100 Top-k and MRR metrics;
- Top-k interpretation as candidate retrieval;
- no DAM overlap across partitions;
- conceptual separation between DAM dependence and duplicates/near-duplicates;
- final consolidated EXP-04 values;
- historical–normative integration;
- LLM reranker as a 20-case diagnostic;
- HE4 and its limitations;
- EXP-08 and separation between historical/intermediate HE5 and final HE5;
- EXP-11A as descriptive/non-causal analysis;
- historical-expansion gates;
- Bank Materialization ≠ retrieval distinction;
- `EXP-11B retrieval = PENDING`;
- `EXP-12 = PENDING`;
- Group 2B = `PENDING`;
- Group 3 = `PENDING`.

### EXP-04

The audit confirmed that 0A-02 uses the final consolidated `exp04_final_results_registry_v0.2.csv` rather than earlier snapshot figures. This preserves, among other values, H100 Top-3 `709/1056 = 0.671402`, the final normative-baseline values, and final D1a results.

Normative baselines are interpreted only as documentary-evidence retrieval and not as replacements for historical ranking.

### Historical–normative integration

Verified values include:

- `1056` cases;
- `3168` candidate slots;
- exact candidate–evidence association `3168/3168`;
- `candidate_exact_evidence_rate = 1.0`;
- `historical_rank_invariance_rate = 1.0`;
- `top3_invariance_rate = 1.0`;
- `traceability_complete_rate = 1.0`.

The authorized interpretation remains: **exact documentary association does not establish substantive normative correctness**.

### Diagnostic reranker

The 20-case scope was verified:

- `calls = 20`;
- Top-1 before and after = `10/20 = 0.5`;
- Top-3 before and after = `13/20 = 0.65`;
- `delta_mrr = 0`;
- no prespecified inferential test;
- `scope = DIAGNOSTIC SAMPLE ONLY`.

It is not a benchmark or evidence of generalization.

### HE4

The audit verified:

- `50` cases;
- `28/50 = 56%` auditable under qualitative evaluation;
- mean `11.72`;
- median `12`;
- no hard violations in qualitative evaluation;
- AI expert-role evaluator rather than independent human review;
- `HE4 = PARTIALLY_SUPPORTED`;
- `PROMPT_SCHEMA_SPECIFICATION_MISMATCH`;
- `EVALUATOR_MODALITY_DEVIATION`.

Therefore, HE4 may be used only as limited evidence of structure, traceability, and auditability under its protocol. It does not demonstrate complete legal correctness.

### EXP-08 and HE5

The audit confirmed that:

- EXP-08 remains a versioned artifact/analysis;
- EXP-08 `HE5 = PARTIALLY_SUPPORTED` is retained only as an experiment-specific historical/intermediate interpretation;
- final inferential HE5 remains `HE5 = PENDING_GROUP3`.

### EXP-11A and historical expansion

EXP-11A was confirmed as closed, approved, and versioned, with descriptive interpretation only. No isolated causal effect of bank size is authorized.

Gate 02, Gate 03, Real Ingest, and Bank Materialization are also correctly separated from retrieval. The existence of 10 materialized H150 banks and 10 materialized H200 banks does not constitute H150/H200 retrieval-performance evidence.

### Experimental state without drift

During the audit:

- `main` remained at `95ffec45ae5a734545ae7bb2d8d530f42f8f056c`;
- no H150/H200 retrieval results existed;
- `EXP-11B retrieval = PENDING`;
- `EXP-12 = PENDING`;
- Group 2B = `PENDING`;
- Group 3 = `PENDING`.

### Mandatory minor normalization for the final artifact

The only remaining correction concerns editorial/governance normalization and does not alter results or claims.

Each row in the frozen experimental matrix must have exactly **one** status from:

`FROZEN_CURRENT`, `EXECUTED_LIMITED`, `HISTORICAL_SNAPSHOT`, `PENDING`, `NOT_AUTHORIZED`, `REVIEW_REQUIRED`.

Combined statuses are not permitted. If an umbrella row contains components with different statuses, it must be disaggregated.

In particular:

- EXP-08 as an artifact/analysis: `FROZEN_CURRENT`;
- EXP-08 `HE5 = PARTIALLY_SUPPORTED` interpretation: `HISTORICAL_SNAPSHOT` relative to the final inferential decision;
- final inferential HE5 decision: `PENDING`.

This normalization will be applied when the final artifact is consolidated after author approval and before `0A-02 = APPROVED / FROZEN` is recorded.

### Experimental gate

Formal state:

```text
0A-02 EXPERIMENTAL AUDIT = PASS WITH MINOR NORMALIZATION
EXPERIMENTAL_FACTS = VERIFIED
MATERIAL_EXPERIMENTAL_ERRORS = 0
MINOR_GOVERNANCE_NORMALIZATION = 1
READY_FOR_AUTHOR_APPROVAL = true
0B_AUTHORIZED = false
```

0A-02 does not need to be repeated or returned to the drafting AI.
