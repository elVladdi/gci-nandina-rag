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
- Bloque activo: **`0B-05B — Información, conocimiento explícito documental y límites del conocimiento codificado`**.
- Estado de `0B-05B`: **`READY_FOR_DRAFTING`**.
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

Registros gobernantes:

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

### 0B-05B — apertura formal

Alcance:

`article/literature/0B05_SCOPE_AND_BATCH_PLAN.md`.

Prompt activo:

`article/prompts/0B05B_INFORMATION_EXPLICIT_TACIT_KNOWLEDGE.md`.

Lote final:

1. `Conceptual Approaches for Deﬁning Data, Information,and Knowledge.pdf`
2. `The Duality of Knowledge.pdf`
3. `Knowledge management - re-thinking information management and facing the challenge of managing tacit knowledge.pdf`

Un sufijo automático de adjunto como `(2)` no constituye versión científica; gobierna la identidad del trabajo visible en el PDF. Si la IA de redacción no puede leer íntegramente cualquiera de las tres copias, debe identificar el faltante y detenerse sin suplementar con fuentes secundarias.

Objetivos/controles de 0B-05B:

- reconstruir la diversidad conceptual de `data`, `information` y `knowledge` sin imponer DIKW universal;
- separar `explicit/codified/documented knowledge` de conocimiento tácito/no codificado y de expertise total;
- distinguir `information management` de `knowledge management` según las fuentes;
- separar conceptos reportados por autores de `OPERACIONALIZACION_DEL_PROYECTO`;
- auditar, no asumir, las fronteras:

`DATA ≠ INFORMATION ≠ KNOWLEDGE`

`DOCUMENTED / EXPLICIT KNOWLEDGE ≠ TOTAL EXPERT KNOWLEDGE`

`DOCUMENT RETRIEVAL ≠ EXPERT INTERPRETATION ≠ LEGAL CORRECTNESS`

`LLM-GENERATED EXPLANATION ≠ EXPERT KNOWLEDGE ≠ OFFICIAL CLASSIFICATION`.

Cualquier aplicación al piloto —por ejemplo corpus normativo como fuente de conocimiento explícito documental o banco histórico como experiencia registrada— debe etiquetarse `OPERACIONALIZACION_DEL_PROYECTO`; no puede atribuirse a los autores como resultado sobre NANDINA/customs/LLM.

0B-05B es fundacional y no puede declarar novelty. No modifica por sí mismo los estados F1–F5; F1/F2/F4/F5 pueden recibir solo relevancia de frontera metodológica y F3 es normalmente no relevante. G6/G7 no se reabren.

### Gate vigente

```text
0B-05B = READY_FOR_DRAFTING
-> IA de redacción
-> revisión científica/editorial interna contra los tres PDF primarios
-> corrección si aplica
-> aprobación expresa del autor
-> freeze 0B-05B
-> recién entonces evaluar definición/apertura de 0B-05C
```

La IA experimental solo interviene si una interpretación bibliográfica afecta directamente hechos/claims experimentales congelados o restricciones bajo su autoridad.

### Prohibiciones vigentes

Durante 0B-05B no está autorizado:

- redactar Introduction/Related Work/Methods/Results/Discussion/Conclusions;
- declarar novelty o gap definitivo;
- buscar literatura nueva;
- usar otros PDF para completar el lote;
- imponer una pirámide DIKW universal;
- equiparar explícito/codificado/documentado/almacenado sin soporte;
- confundir conocimiento explícito documental con totalidad de expertise;
- convertir retrieval documental en comprensión, juicio experto o corrección jurídica;
- describir la explicación del LLM como conocimiento experto o clasificación oficial;
- modificar 0A o el Plan Maestro;
- reabrir G6/G7;
- abrir 0B-05C, 0B-06 o 0C antes del gate correspondiente.

---

## English

### Overall status

- Working branch: `article/main-manuscript`.
- Global state: `IN_ANALYSIS`.
- Phase 0A is **`CLOSED / APPROVED`**.
- Active phase: **`0B — Critical literature map and taxonomy`**.
- 0B-01 through 0B-05A are **`APPROVED / FROZEN`**.
- Active block: **`0B-05B — Information, documented explicit knowledge, and limits of codified knowledge`**.
- 0B-05B status: **`READY_FOR_DRAFTING`**.
- 0B-05C remains `NOT_STARTED / CLOSED_BY_GATE`; 0B-06 is not started.
- 0C remains blocked until 0B closes; 0D remains blocked until 0C closes.
- Target journal remains pending until 0D; manuscript drafting has not started.

### Governing ground truth and prior freezes

Frozen 0A artifacts remain authoritative. Literature review cannot modify the Master Plan. 0B-04A/0B-04B/0B-05A foundational distinctions remain frozen, including strict separation of retrieval/reranking/generation concepts, provenance/auditability/legal-correctness concepts, and documentation/versioning/provenance/reproducibility/replication/generalization concepts.

F1–F5 remain provisional. G6 remains eliminated and G7 remains merged into F2.

### 0B-05A closure

0B-05A is approved/frozen. Its governing prompt, internal review, author approval, and canonical artifact remain authoritative; experimental review was not required.

### 0B-05B formal opening

Formal scope: `article/literature/0B05_SCOPE_AND_BATCH_PLAN.md`.

Active prompt: `article/prompts/0B05B_INFORMATION_EXPLICIT_TACIT_KNOWLEDGE.md`.

Final controlled batch:

1. `Conceptual Approaches for Deﬁning Data, Information,and Knowledge.pdf`
2. `The Duality of Knowledge.pdf`
3. `Knowledge management - re-thinking information management and facing the challenge of managing tacit knowledge.pdf`

Automatic physical attachment suffixes such as `(2)` are not scientific version identifiers. The drafting AI must stop if any full source is unavailable rather than substituting secondary material.

0B-05B must reconstruct conceptual diversity without imposing a universal DIKW sequence; separate explicit/codified/documented knowledge from tacit/non-codified knowledge and complete expertise; distinguish information management from knowledge management; and label every mapping onto pilot components as `PROJECT_OPERATIONALIZATION` rather than an author-reported customs result.

Candidate boundaries to audit rather than assume are:

`DATA ≠ INFORMATION ≠ KNOWLEDGE`

`DOCUMENTED / EXPLICIT KNOWLEDGE ≠ TOTAL EXPERT KNOWLEDGE`

`DOCUMENT RETRIEVAL ≠ EXPERT INTERPRETATION ≠ LEGAL CORRECTNESS`

`LLM-GENERATED EXPLANATION ≠ EXPERT KNOWLEDGE ≠ OFFICIAL CLASSIFICATION`.

This remains a foundational conceptual batch and cannot establish novelty. F1/F2/F4/F5 may receive boundary relevance only; F3 is normally not relevant. G6/G7 remain closed.

### Gate

`0B-05B READY_FOR_DRAFTING -> drafting AI -> internal scientific/editorial review against the three primary PDFs -> correction if needed -> express author approval -> freeze -> only then assess definition/opening of 0B-05C`.

Experimental-AI review is triggered only if literature interpretation affects frozen experimental facts/claims or restrictions under its authority.

No manuscript drafting, final novelty/gap claims, new-literature search, out-of-batch supplementation, universal DIKW framing, unsupported conflation of explicit/codified/documented/stored knowledge, conversion of retrieval into expert/legal correctness, Master-Plan/0A modification, reopening G6/G7, or opening 0B-05C/0B-06/0C is authorized before the corresponding gate.