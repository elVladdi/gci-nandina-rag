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
- `0B-05A`: **`APPROVED / FROZEN`**.
- `0B-05B`: **`NOT_STARTED / ELIGIBLE_FOR_DEFINITION`**.
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
- `0B-05A = APPROVED / FROZEN` — `article/literature/0B05A_DATA_DOCUMENTATION_PROVENANCE_REPRODUCIBILITY_FROZEN.md`.

### Distinciones fundacionales ya congeladas

0B-04A:

`QUERY/DOCUMENT REPRESENTATION ≠ CANDIDATE GENERATION ≠ ANN/INDEX SEARCH ≠ RERANKING ≠ FINAL RANKING`.

0B-04B:

`RAG ≠ RETRIEVAL_AUGMENTED_PRETRAINING ≠ RETRIEVE_THEN_GENERATE ≠ QUERY_EXPANSION ≠ QUERY_REWRITING ≠ PASSAGE_FUSION ≠ EVIDENTIALITY_GUIDED_GENERATION`.

`RETRIEVED PASSAGE ≠ EVIDENCE ATTRIBUTION ≠ EVIDENTIALITY ≠ GROUNDING GUARANTEE ≠ PROVENANCE VERIFICATION ≠ FORMAL AUDITABILITY ≠ LEGAL CORRECTNESS`.

0B-05A:

`DATASET DOCUMENTATION ≠ DATASET IDENTITY / VERSIONING ≠ DATA PROVENANCE / LINEAGE ≠ WORKFLOW PROVENANCE ≠ REPRODUCIBILITY ≠ REPLICATION ≠ GENERALIZATION`.

`DOCUMENTATION / PROVENANCE ≠ TRANSPARENCY TRAIL ≠ INTERNAL LIFECYCLE AUDIT ≠ FORMAL OUTPUT-LEVEL AUDITABILITY ≠ SUBSTANTIVE / LEGAL CORRECTNESS`.

Las distinciones de 0B-05A son fronteras metodológicas, no una escala lineal de madurez o implicación.

### Candidatos provisionales

Ninguno constituye novelty ni gap definitivo.

- **F1:** `CANDIDATE_GAP_ONLY — SURVIVES IN NARROW FORM`.
- **F2:** `CANDIDATE_GAP_ONLY — FURTHER NARROWED`.
- **F3:** `CANDIDATE_GAP_ONLY — RETAINED WITH APPLICABILITY CAVEAT`.
- **F4:** `CANDIDATE_GAP_ONLY — RETAINED AS METHODOLOGICAL DISTINCTION`.
- **F5:** `CANDIDATE_GAP_ONLY — FURTHER NARROWED`; después de 0B-05A queda prohibida cualquier formulación amplia de ausencia de trazabilidad/auditabilidad. Solo permanece como candidato estrecho la evaluación formal, explícita y separada de auditabilidad documental por salida.
- **G6:** `ELIMINATED AS GAP CANDIDATE`.
- **G7:** `MERGED INTO F2 / ELIMINATED AS INDEPENDENT CANDIDATE`.

### 0B-05A — cierre formal

Registros:

- Prompt: `article/prompts/0B05A_DATA_DOCUMENTATION_PROVENANCE_REPRODUCIBILITY.md`.
- Revisión interna: `article/reviews/0B05A_INTERNAL_REVIEW.md` — `PASS WITH MINOR CORRECTIONS`, `MATERIAL_ERRORS = 0`.
- Aprobación del autor: `article/reviews/0B05A_AUTHOR_APPROVAL.md`.
- Artefacto canónico: `article/literature/0B05A_DATA_DOCUMENTATION_PROVENANCE_REPRODUCIBILITY_FROZEN.md`.
- Revisión experimental: `NOT_REQUIRED`.

Estado congelado:

```text
0B-05A = APPROVED / FROZEN
DRAFTING_DELIVERABLE = ANALYTICALLY_COMPLETE
INTERNAL_REVIEW = PASS WITH MINOR CORRECTIONS
MATERIAL_ERRORS = 0
AUTHOR_APPROVAL = RECEIVED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

Normalizaciones C1–C7 integradas: Bender & Friedman como documentación no causal; Gebru v8 con metadata editorial final pendiente y terminología de reproducibility no homogeneizada con Pineau; FAIR Data Pipeline centrado en provenance/lineage y version identification; Pineau como convención operacional no universal y sin causalizar asociaciones; SMACTR con cinco etapas y lifecycle audit separado de output-level/external/legal auditability; taxonomía cruzada como frontera y no escalera.

Impacto metodológico congelado:

- F3: documentar relaciones/particiones/dependencia no equivale a controlarla ni demostrar independencia.
- F4: `provenance/reproducibility/auditability ≠ substantive/legal correctness`.
- F5: prior art fuerte en provenance, transparency trails e internal audit; solo sobrevive el candidato estrecho de evaluación formal, explícita y separada de auditabilidad documental por salida, todavía sin novelty.

### Gate siguiente

`0B-05B — Información, conocimiento explícito documental y límites del conocimiento codificado` queda **`NOT_STARTED / ELIGIBLE_FOR_DEFINITION`**.

El freeze de 0B-05A no abre automáticamente 0B-05B. Corresponde confirmar las fuentes primarias, definir el lote final y crear su prompt mediante un cambio posterior explícito.

`0B-05C` permanece `NOT_STARTED / CLOSED_BY_GATE` hasta cerrar 0B-05B.

Mientras 0B permanezca abierto no está autorizado:

- redactar Introduction/Related Work/Methods/Results/Discussion/Conclusions;
- declarar novelty o gap definitivo;
- abrir 0C;
- modificar 0A o el Plan Maestro;
- reabrir G6/G7;
- buscar literatura nueva salvo apertura explícita de 0B-06;
- convertir claims secundarios en hechos sin verificar la fuente primaria.

---

## English

### Overall status

- Working branch: `article/main-manuscript`.
- Global state: `IN_ANALYSIS`.
- Phase 0A is **`CLOSED / APPROVED`**.
- Active phase: **`0B — Critical literature map and taxonomy`**.
- 0B-01, 0B-02, 0B-03A, 0B-03B, 0B-04A, 0B-04B, and 0B-05A are **`APPROVED / FROZEN`**.
- 0B-05B is **`NOT_STARTED / ELIGIBLE_FOR_DEFINITION`**.
- 0B-05C remains `NOT_STARTED / CLOSED_BY_GATE`; 0B-06 is not started.
- 0C remains blocked until 0B closes; 0D remains blocked until 0C closes.
- Target journal remains pending until 0D; manuscript drafting has not started.

### Governing ground truth

Frozen 0A documentary and experimental artifacts remain authoritative. Literature review cannot modify the Master Plan; exclusive Master-Plan authority remains with the experimental workflow.

### Closed blocks and foundational boundaries

0B-04A freezes representation vs candidate generation vs ANN/index search vs reranking vs final ranking. 0B-04B freezes the distinctions among RAG, retrieval-augmented pretraining, retrieve-then-generate, query expansion, query rewriting, passage fusion, and evidentiality-guided generation, and separately between retrieved passages, evidence attribution, evidentiality, grounding guarantees, provenance verification, formal auditability, and legal correctness.

0B-05A now freezes:

`DATASET DOCUMENTATION ≠ DATASET IDENTITY / VERSIONING ≠ DATA PROVENANCE / LINEAGE ≠ WORKFLOW PROVENANCE ≠ REPRODUCIBILITY ≠ REPLICATION ≠ GENERALIZATION`

and

`DOCUMENTATION / PROVENANCE ≠ TRANSPARENCY TRAIL ≠ INTERNAL LIFECYCLE AUDIT ≠ FORMAL OUTPUT-LEVEL AUDITABILITY ≠ SUBSTANTIVE / LEGAL CORRECTNESS`.

These are boundaries, not a linear maturity/implication ladder.

### 0B-05A closure

Governing records are the prompt, internal review, author approval, and canonical frozen artifact `article/literature/0B05A_DATA_DOCUMENTATION_PROVENANCE_REPRODUCIBILITY_FROZEN.md`.

```text
0B-05A = APPROVED / FROZEN
DRAFTING_DELIVERABLE = ANALYTICALLY_COMPLETE
INTERNAL_REVIEW = PASS WITH MINOR CORRECTIONS
MATERIAL_ERRORS = 0
AUTHOR_APPROVAL = RECEIVED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

C1–C7 are integrated: Bender & Friedman remain documentation rather than causal validation; the analyzed Gebru v8 copy remains the governed source and final editorial metadata is pending; Gebru/Pineau reproducibility usage remains source-specific; FAIR Data Pipeline is centered on provenance/lineage and version identification; Pineau's terminology remains a paper-specific convention and associations remain non-causal; SMACTR remains five-stage and lifecycle audit remains distinct from per-output/external/legal auditability; and the cross-paper taxonomy is not an implication ladder.

F3 receives documentation/dependency-reporting foundation only; F4 remains a correctness boundary; F5 is further narrowed by strong prior art on provenance, transparency trails, and internal auditing, leaving only the narrow candidate of formal, explicit, separate documentary auditability evaluation at output level, without novelty status. G6 remains eliminated and G7 remains merged into F2.

### Next gate

0B-05B is now `NOT_STARTED / ELIGIBLE_FOR_DEFINITION`. It requires confirmation of primary sources, a final controlled batch, and its own executable prompt before opening. 0B-05C remains closed until 0B-05B freezes.

Manuscript drafting, final novelty/gap claims, 0C opening, Master-Plan/0A modification, reopening G6/G7, and new-literature search outside an explicitly opened 0B-06 remain prohibited while 0B is open.
