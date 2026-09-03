# Estado del artículo / Article Status

## Español

### Estado general

- Rama de trabajo: `article/main-manuscript`.
- Estado global: `IN_ANALYSIS`.
- Fase `0A — Ground truth documental y experimental`: **`CLOSED / APPROVED`**.
- `0A-01`: **`APPROVED / FROZEN`**.
- `0A-02`: **`APPROVED / FROZEN`**.
- Fase activa: **`0B — Mapa crítico de literatura y taxonomía`**.
- `0B-01`: **`APPROVED / FROZEN`**.
- `0B-02`: **`APPROVED / FROZEN`**.
- `0B-03A`: **`APPROVED / FROZEN`**.
- `0B-03B`: **`APPROVED / FROZEN`**.
- `0B-04A`: **`APPROVED / FROZEN`**.
- `0B-04B`: **`APPROVED / FROZEN`**.
- Bloque activo: **`0B-05A — Documentación de datos, procedencia, reproducibilidad y audit trail`**.
- Estado de `0B-05A`: **`READY_FOR_DRAFTING`**.
- `0B-05B`: **`NOT_STARTED / CLOSED_BY_GATE`**.
- `0B-05C`: **`NOT_STARTED / CLOSED_BY_GATE`**.
- `0B-06`: `NOT_STARTED`.
- `0C — Gap, contribución y Research Questions`: `BLOCKED` hasta cerrar 0B.
- `0D — Arquitectura editorial y journal fit`: `BLOCKED` hasta cerrar 0C.
- Target journal: `PENDING — se decidirá en Fase 0D`.
- Manuscrito redactado: no iniciado.
- Corpus consolidado: `62` obras/documentos distintos; acceso primario verificable `62/62`.
- Idioma del chat: español.
- Artefactos GitHub: español + inglés con equivalencia semántica.

### Ground truth gobernante

Continúan gobernando:

- `article/ground_truth/0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md`;
- `article/ground_truth/0A02_EXPERIMENTAL_GROUND_TRUTH_FROZEN.md`.

La revisión bibliográfica no modifica el Plan Maestro ni el ground truth 0A. La IA experimental conserva autoridad exclusiva sobre el Plan Maestro.

### Bloques 0B cerrados

- `0B-01 = APPROVED / FROZEN` — `article/literature/0B01_HS_CLASSIFICATION_CORE_LITERATURE_FROZEN.md`.
- `0B-02 = APPROVED / FROZEN` — `article/literature/0B02_RETRIEVAL_VALIDATION_KNOWLEDGE_AUDITABILITY_FROZEN.md`.
- `0B-03A = APPROVED / FROZEN` — `article/literature/0B03A_LLM_RAG_MULTIMODAL_CUSTOMS_FROZEN.md`.
- `0B-03B = APPROVED / FROZEN` — `article/literature/0B03B_AGENTS_HIERARCHICAL_REGULATORY_REASONING_FROZEN.md`.
- `0B-04A = APPROVED / FROZEN` — `article/literature/0B04A_IR_RANKING_RETRIEVAL_FOUNDATIONS_FROZEN.md`.
- `0B-04B = APPROVED / FROZEN` — `article/literature/0B04B_RAG_QUERY_TRANSFORMATION_GROUNDING_FOUNDATIONS_FROZEN.md`.

0B-04A congeló:

`QUERY/DOCUMENT REPRESENTATION ≠ CANDIDATE GENERATION ≠ ANN/INDEX SEARCH ≠ RERANKING ≠ FINAL RANKING`.

0B-04B congeló:

`RAG ≠ RETRIEVAL_AUGMENTED_PRETRAINING ≠ RETRIEVE_THEN_GENERATE ≠ QUERY_EXPANSION ≠ QUERY_REWRITING ≠ PASSAGE_FUSION ≠ EVIDENTIALITY_GUIDED_GENERATION`.

`RETRIEVED PASSAGE ≠ EVIDENCE ATTRIBUTION ≠ EVIDENTIALITY ≠ GROUNDING GUARANTEE ≠ PROVENANCE VERIFICATION ≠ FORMAL AUDITABILITY ≠ LEGAL CORRECTNESS`.

Los resultados fundacionales de 0B-04 no reinterpretan D1a fuera de la implementación densa exploratoria específica.

### Candidatos provisionales

Ninguno constituye novelty ni gap definitivo.

- **F1:** `CANDIDATE_GAP_ONLY — SURVIVES IN NARROW FORM`.
- **F2:** `CANDIDATE_GAP_ONLY — FURTHER NARROWED`.
- **F3:** `CANDIDATE_GAP_ONLY — RETAINED WITH APPLICABILITY CAVEAT`.
- **F4:** `CANDIDATE_GAP_ONLY — RETAINED AS METHODOLOGICAL DISTINCTION`.
- **F5:** `CANDIDATE_GAP_ONLY — FURTHER NARROWED`.
- **G6:** `ELIMINATED AS GAP CANDIDATE`; queda solo como principio de calidad del ground truth.
- **G7:** `MERGED INTO F2 / ELIMINATED AS INDEPENDENT CANDIDATE`.

0B-05 tampoco está autorizado a convertir estos candidatos en novelty.

### 0B-05 — apertura formal

Alcance:

`article/literature/0B05_SCOPE_AND_BATCH_PLAN.md`.

#### 0B-05A — bloque activo

Prompt:

`article/prompts/0B05A_DATA_DOCUMENTATION_PROVENANCE_REPRODUCIBILITY.md`.

PDF asignados:

1. `Data statements for natural language processing- Toward mitigating system bias and enabling better science..pdf`
2. `Datasheets for Datasets.pdf`
3. `AIR data pipeline-Provenance-driven data management for traceable scientific workflows.pdf`
4. `Improving Reproducibility in Machine Learning Research(A Report from the NeurIPS 2019 Reproducibility Program).pdf`
5. `Closing the AI accountability gap - defining an end-to-end framework for internal algorithmic auditing.pdf`

El tercer archivo corresponde científicamente a **FAIR Data Pipeline: provenance-driven data management for traceable scientific workflows**; el nombre físico suministrado se conserva para localizarlo.

Objetivo gobernante:

`DATA/DOCUMENTATION -> VERSION/IDENTITY -> PROVENANCE/LINEAGE -> REPRODUCIBLE WORKFLOW -> AUDIT TRAIL`

sin inferir:

`CORRECTNESS -> LEGAL VALIDITY -> GENERALIZATION`.

Distinciones obligatorias:

- dataset documentation ≠ dataset quality/adequacy;
- dataset identity/versioning ≠ description;
- versioning ≠ reproducibility;
- provenance/lineage ≠ correctness;
- reproducibility ≠ external replication/generalization;
- lifecycle/internal audit ≠ output-level auditability evaluation;
- transparency trail ≠ legal correctness.

0B-05A puede aportar fundamentos metodológicos a F3/F4/F5, pero no es un pressure test de novelty aduanera.

#### 0B-05B y 0B-05C

- `0B-05B — Información, conocimiento explícito documental y límites del conocimiento codificado`: **`NOT_STARTED / CLOSED_BY_GATE`**.
- `0B-05C — Autoridad, vigencia y trazabilidad de fuentes normativas/oficiales`: **`NOT_STARTED / CLOSED_BY_GATE`**.

No se abren hasta completar sus gates previos.

### Gate vigente

```text
0B-05A = READY_FOR_DRAFTING
-> IA de redacción
-> revisión científica/editorial interna contra los cinco PDF primarios
-> corrección si aplica
-> aprobación expresa del autor
-> freeze 0B-05A
-> definir/abrir 0B-05B
```

La IA experimental solo se incorpora si una interpretación bibliográfica afecta directamente hechos/claims experimentales congelados o restricciones bajo su autoridad.

### Prohibiciones vigentes

Durante 0B-05A no está autorizado:

- redactar Introduction/Related Work/Methods/Results/Discussion/Conclusions;
- declarar novelty o gap definitivo;
- buscar literatura nueva;
- utilizar otros PDF para completar el lote;
- equiparar documentación, provenance, reproducibility o audit trail con correctness/legal validity;
- modificar 0A o el Plan Maestro;
- reinterpretar resultados experimentales congelados fuera de su alcance;
- reabrir G6/G7;
- abrir 0B-05B, 0B-05C, 0B-06 o 0C antes del gate correspondiente.

---

## English

### Overall status

- Working branch: `article/main-manuscript`.
- Global state: `IN_ANALYSIS`.
- Phase 0A is **`CLOSED / APPROVED`**.
- Active phase: **`0B — Critical literature map and taxonomy`**.
- 0B-01, 0B-02, 0B-03A, 0B-03B, 0B-04A, and 0B-04B are **`APPROVED / FROZEN`**.
- Active block: **`0B-05A — Data documentation, provenance, reproducibility, and audit trail`**.
- 0B-05A status: **`READY_FOR_DRAFTING`**.
- 0B-05B and 0B-05C are **`NOT_STARTED / CLOSED_BY_GATE`**; 0B-06 is not started.
- 0C remains blocked until 0B closes; 0D remains blocked until 0C closes.
- Target journal remains pending until 0D; manuscript drafting has not started.

### Governing freezes

Frozen 0A artifacts remain authoritative. Literature review cannot modify the Master Plan. 0B-04A/0B-04B methodological distinctions remain frozen and do not reinterpret the project's D1a result beyond its specific exploratory dense implementation.

F1–F5 remain provisional; G6 remains eliminated and G7 remains merged into F2. 0B-05 cannot convert them into novelty claims.

### 0B-05 formal opening

Scope: `article/literature/0B05_SCOPE_AND_BATCH_PLAN.md`.

Active prompt: `article/prompts/0B05A_DATA_DOCUMENTATION_PROVENANCE_REPRODUCIBILITY.md`.

The five assigned inherited PDFs are Bender & Friedman data statements, Gebru et al. datasheets, the supplied FAIR Data Pipeline paper, Pineau et al. reproducibility report, and Raji et al. end-to-end internal algorithmic auditing framework.

The governing chain is:

`DATA/DOCUMENTATION -> VERSION/IDENTITY -> PROVENANCE/LINEAGE -> REPRODUCIBLE WORKFLOW -> AUDIT TRAIL`

and explicitly not:

`CORRECTNESS -> LEGAL VALIDITY -> GENERALIZATION`.

Required distinctions include documentation vs dataset adequacy, versioning vs reproducibility, provenance vs correctness, reproducibility vs external replication/generalization, lifecycle/internal audit vs output-level auditability evaluation, and transparency trail vs legal correctness.

0B-05B (information/documented explicit knowledge) and 0B-05C (official normative-source authority/currency/traceability) remain closed by gate.

### Gate

`0B-05A READY_FOR_DRAFTING -> drafting AI -> internal review against the five primary PDFs -> correction if needed -> express author approval -> freeze -> define/open 0B-05B`.

Experimental-AI review is triggered only if a literature interpretation affects frozen experimental facts/claims or restrictions under its authority.

No manuscript drafting, final novelty/gap claims, new-literature search, out-of-batch PDF use, conflation of documentation/provenance/reproducibility/audit trail with correctness/legal validity, Master-Plan/0A modification, reopening G6/G7, or opening 0B-05B/0B-05C/0B-06/0C is authorized before the corresponding gate.
