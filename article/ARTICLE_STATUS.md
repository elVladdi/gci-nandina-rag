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
- Estado de `0B-05A`: **`INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING`**.
- Revisión interna 0B-05A: **`PASS WITH MINOR CORRECTIONS`**, `MATERIAL_ERRORS = 0`, `EXPERIMENTAL_REVIEW = NOT_REQUIRED`.
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

### 0B-05A — revisión interna completada

Alcance:

`article/literature/0B05_SCOPE_AND_BATCH_PLAN.md`.

Prompt:

`article/prompts/0B05A_DATA_DOCUMENTATION_PROVENANCE_REPRODUCIBILITY.md`.

Revisión interna:

`article/reviews/0B05A_INTERNAL_REVIEW.md`.

PDF auditados:

1. `Data statements for natural language processing- Toward mitigating system bias and enabling better science..pdf`
2. `Datasheets for Datasets.pdf`
3. `AIR data pipeline-Provenance-driven data management for traceable scientific workflows.pdf`
4. `Improving Reproducibility in Machine Learning Research(A Report from the NeurIPS 2019 Reproducibility Program).pdf`
5. `Closing the AI accountability gap - defining an end-to-end framework for internal algorithmic auditing.pdf`

La identidad científica del tercer archivo es **FAIR Data Pipeline: provenance-driven data management for traceable scientific workflows**.

La revisión primaria acepta, con correcciones menores, las fronteras:

`DATASET DOCUMENTATION ≠ DATASET IDENTITY / VERSIONING ≠ DATA PROVENANCE / LINEAGE ≠ WORKFLOW PROVENANCE ≠ REPRODUCIBILITY ≠ REPLICATION ≠ GENERALIZATION`

Y:

`DOCUMENTATION / PROVENANCE ≠ TRANSPARENCY TRAIL ≠ INTERNAL LIFECYCLE AUDIT ≠ FORMAL OUTPUT-LEVEL AUDITABILITY ≠ SUBSTANTIVE / LEGAL CORRECTNESS`.

Correcciones obligatorias C1–C7 para el freeze:

- Bender & Friedman: casos retrospectivos/value scenarios no constituyen validación causal de beneficios.
- Gebru et al.: la copia analizada gobierna como arXiv v8; metadata editorial final queda `REVIEW_REQUIRED_FOR_FINAL_CITATION`, sin reconstrucción silenciosa.
- Gebru vs Pineau: no homogeneizar silenciosamente el término reproducibility.
- FAIR Data Pipeline: provenance/lineage y version identification son el núcleo; full reproducibility no es core requirement.
- Pineau: preservar `reproducible ≠ replicable ≠ robust ≠ generalisable` como convención del paper y no causalizar asociaciones.
- Raji: SMACTR tiene cinco etapas; Post-Audit no es una sexta etapa; lifecycle audit trail no equivale a output-level auditability, external audit o legal correctness.
- La taxonomía cruzada es una frontera metodológica, no una escala lineal de madurez o implicación.

Impacto provisional:

- F3 recibe solo fundamento documental/metodológico; documentación no equivale a control de dependencia.
- F4 refuerza `provenance/reproducibility/auditability ≠ substantive/legal correctness`.
- F5 queda aún más restringido: existe prior art fuerte en provenance, transparency trails e internal audit; solo permanece como candidato estrecho la evaluación formal, explícita y separada de auditabilidad documental por salida, todavía sin novelty.
- G6 y G7 no se reabren.

### Gate vigente

```text
0B-05A = INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING
-> aprobación expresa del autor
-> integrar C1–C7 en el artefacto canónico
-> freeze 0B-05A
-> recién entonces definir/abrir 0B-05B
```

No es necesario devolver el bloque a la IA de redacción porque `MATERIAL_ERRORS = 0`.

### Prohibiciones vigentes

Mientras la aprobación del autor permanezca pendiente no está autorizado:

- congelar 0B-05A;
- abrir 0B-05B, 0B-05C, 0B-06 o 0C;
- redactar Introduction/Related Work/Methods/Results/Discussion/Conclusions;
- declarar novelty o gap definitivo;
- buscar literatura nueva;
- equiparar documentación, provenance, reproducibility o audit trail con correctness/legal validity;
- modificar 0A o el Plan Maestro;
- reinterpretar resultados experimentales congelados;
- reabrir G6/G7.

---

## English

### Overall status

- Working branch: `article/main-manuscript`.
- Global state: `IN_ANALYSIS`.
- Phase 0A is **`CLOSED / APPROVED`**.
- Active phase: **`0B — Critical literature map and taxonomy`**.
- 0B-01, 0B-02, 0B-03A, 0B-03B, 0B-04A, and 0B-04B are **`APPROVED / FROZEN`**.
- Active block: **`0B-05A — Data documentation, provenance, reproducibility, and audit trail`**.
- 0B-05A status: **`INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING`**.
- Internal review: **`PASS WITH MINOR CORRECTIONS`**, `MATERIAL_ERRORS = 0`, `EXPERIMENTAL_REVIEW = NOT_REQUIRED`.
- 0B-05B and 0B-05C remain **`NOT_STARTED / CLOSED_BY_GATE`**; 0B-06 is not started.
- 0C remains blocked until 0B closes; 0D remains blocked until 0C closes.
- Target journal remains pending until 0D; manuscript drafting has not started.

### Governing freezes

Frozen 0A artifacts remain authoritative. Literature review cannot modify the Master Plan. F1–F5 remain provisional; G6 remains eliminated and G7 remains merged into F2.

### 0B-05A internal review

Scope: `article/literature/0B05_SCOPE_AND_BATCH_PLAN.md`.  
Prompt: `article/prompts/0B05A_DATA_DOCUMENTATION_PROVENANCE_REPRODUCIBILITY.md`.  
Internal review: `article/reviews/0B05A_INTERNAL_REVIEW.md`.

The primary-PDF review accepts, subject to C1–C7, the following boundaries:

`DATASET DOCUMENTATION ≠ DATASET IDENTITY / VERSIONING ≠ DATA PROVENANCE / LINEAGE ≠ WORKFLOW PROVENANCE ≠ REPRODUCIBILITY ≠ REPLICATION ≠ GENERALIZATION`

and

`DOCUMENTATION / PROVENANCE ≠ TRANSPARENCY TRAIL ≠ INTERNAL LIFECYCLE AUDIT ≠ FORMAL OUTPUT-LEVEL AUDITABILITY ≠ SUBSTANTIVE / LEGAL CORRECTNESS`.

Mandatory freeze corrections preserve Bender & Friedman as documentation rather than causal validation; keep the analyzed Gebru copy as arXiv v8 with final-citation metadata review pending; preserve Gebru/Pineau terminology differences; keep FAIR Data Pipeline centered on provenance rather than full reproducibility; preserve Pineau's 2×2 terminology and non-causal interpretation; keep SMACTR at five stages and separate lifecycle audit from output-level/legal auditability; and treat the cross-paper taxonomy as methodological boundaries rather than a linear maturity ladder.

F3 gains documentation/dependency-reporting foundation only; F4 is reinforced as a correctness boundary; F5 is further narrowed because provenance, transparency trails, and internal auditing have strong prior art. Only the narrow candidate of a formal, explicit, separate documentary auditability evaluation at output level remains, without novelty status.

### Gate

`0B-05A INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING -> express author approval -> integrate C1–C7 -> freeze 0B-05A -> only then define/open 0B-05B`.

No return to the drafting AI is required because no material errors were found. Until author approval, no 0B-05A freeze, 0B-05B/05C/06/0C opening, manuscript drafting, final novelty/gap declaration, new-literature search, Master-Plan/0A modification, experimental reinterpretation, or reopening of G6/G7 is authorized.
