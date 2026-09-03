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
- Bloque activo: **`0B-04B — Fundamentos de RAG, transformación de consultas y grounding`**.
- Estado de `0B-04B`: **`READY_FOR_DRAFTING`**.
- `0B-05`: `NOT_STARTED / CLOSED_BY_GATE`.
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

0B-04A congeló la distinción:

`QUERY/DOCUMENT REPRESENTATION ≠ CANDIDATE GENERATION ≠ ANN/INDEX SEARCH ≠ RERANKING ≠ FINAL RANKING`.

Sus resultados fundacionales no reinterpretan D1a fuera de la implementación densa exploratoria específica.

### Candidatos provisionales

Ninguno constituye novelty ni gap definitivo.

- **F1:** `CANDIDATE_GAP_ONLY — SURVIVES IN NARROW FORM`.
- **F2:** `CANDIDATE_GAP_ONLY — FURTHER NARROWED`.
- **F3:** `CANDIDATE_GAP_ONLY — RETAINED WITH APPLICABILITY CAVEAT`.
- **F4:** `CANDIDATE_GAP_ONLY — RETAINED AS METHODOLOGICAL DISTINCTION`.
- **F5:** `CANDIDATE_GAP_ONLY — FURTHER NARROWED`.
- **G6:** `ELIMINATED AS GAP CANDIDATE`; queda solo como principio de calidad del ground truth.
- **G7:** `MERGED INTO F2 / ELIMINATED AS INDEPENDENT CANDIDATE`.

0B-04B es fundacional y no está autorizado a convertir estos candidatos en novelty ni a reabrir G6/G7.

### 0B-04B — apertura formal

Alcance actualizado:

`article/literature/0B04_SCOPE_AND_BATCH_PLAN.md`.

Prompt activo:

`article/prompts/0B04B_RAG_QUERY_TRANSFORMATION_GROUNDING_FOUNDATIONS.md`.

PDF asignados:

1. `Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.pdf`
2. `REALM-Retrieval-Augmented Language Model Pre-Training.pdf`
3. `Leveraging passage retrieval with generative models for open domain question answering.pdf`
4. `Query2doc-Query Expansion whit Large Lenguage Models.pdf`
5. `Query Rewriting for Retrieval-Augmented Large Language Models.pdf`
6. `Evidentiality-guided Generation for Knowledge-Intensive NLP Tasks.pdf`

Objetivo gobernante:

`QUERY -> [QUERY TRANSFORMATION?] -> RETRIEVAL -> [FUSION / EVIDENCE SELECTION?] -> GENERATION -> OUTPUT`.

El bloque debe distinguir:

1. RAG de retrieval-augmented pretraining.
2. Retrieve-then-generate de query expansion/query rewriting.
3. Retrieval que modifica el contexto disponible al generador de evidencia normativa posterior a un ranking histórico ya fijado.
4. Passage fusion de evidence attribution.
5. Provenance/inspectable passages de auditabilidad formal.
6. Evidentiality/grounding de corrección sustantiva o jurídica.

Contrato del piloto usado únicamente como frontera comparativa:

`ranking histórico Top-k fijado -> evidencia normativa posterior por candidato -> LLM local exclusivamente explicativo -> sin códigos nuevos -> sin reordenamiento -> sin feedback clasificatorio`.

### Gate vigente

```text
0B-04B = READY_FOR_DRAFTING
-> IA de redacción
-> revisión científica/editorial interna contra los seis PDF primarios
-> corrección si aplica
-> aprobación expresa del autor
-> freeze 0B-04B
-> evaluar apertura de 0B-05
```

La IA experimental solo se incorpora si una interpretación bibliográfica afecta directamente hechos/claims experimentales congelados o restricciones metodológicas bajo su autoridad.

### Prohibiciones vigentes

Durante 0B-04B no está autorizado:

- redactar Introduction/Related Work/Methods/Results/Discussion/Conclusions;
- declarar novelty, gap definitivo o superioridad general de RAG/métodos;
- usar otros PDF del corpus;
- buscar literatura nueva;
- equiparar provenance/evidentiality/grounding con auditabilidad o legal correctness;
- modificar 0A o el Plan Maestro;
- reinterpretar resultados experimentales congelados fuera de su alcance;
- reabrir G6/G7;
- abrir 0B-05, 0B-06 o 0C antes del gate correspondiente.

---

## English

### Overall status

- Working branch: `article/main-manuscript`.
- Global state: `IN_ANALYSIS`.
- Phase 0A is **`CLOSED / APPROVED`**.
- Active phase: **`0B — Critical literature map and taxonomy`**.
- 0B-01, 0B-02, 0B-03A, 0B-03B, and 0B-04A are **`APPROVED / FROZEN`**.
- Active block: **`0B-04B — RAG, query-transformation, and grounding foundations`**.
- 0B-04B status: **`READY_FOR_DRAFTING`**.
- 0B-05 is `NOT_STARTED / CLOSED_BY_GATE`; 0B-06 is not started.
- 0C remains blocked until 0B closes; 0D remains blocked until 0C closes.
- Target journal remains pending until 0D; manuscript drafting has not started.

### Governing ground truth

Frozen 0A documentary and experimental artifacts remain authoritative. Literature review cannot modify the Master Plan; exclusive Master-Plan authority remains with the experimental workflow.

### Closed blocks and provisional candidates

0B-04A froze the distinction `QUERY/DOCUMENT REPRESENTATION ≠ CANDIDATE GENERATION ≠ ANN/INDEX SEARCH ≠ RERANKING ≠ FINAL RANKING` and does not reinterpret D1a beyond its specific exploratory dense implementation.

F1–F5 remain provisional in narrowed/methodological forms; G6 remains eliminated and G7 remains merged into F2. 0B-04B is foundational and cannot convert them into novelty claims.

### 0B-04B formal opening

Active prompt: `article/prompts/0B04B_RAG_QUERY_TRANSFORMATION_GROUNDING_FOUNDATIONS.md`.

The six assigned PDFs are the Lewis et al. RAG paper, REALM, Fusion-in-Decoder, Query2doc, Query Rewriting for Retrieval-Augmented Large Language Models, and Evidentiality-guided Generation listed in the Spanish section.

The governing pipeline is `QUERY -> [QUERY TRANSFORMATION?] -> RETRIEVAL -> [FUSION / EVIDENCE SELECTION?] -> GENERATION -> OUTPUT`.

The block must distinguish RAG from retrieval-augmented pretraining, retrieve-then-generate from query transformation, retrieval-conditioned generation from post-ranking normative evidence, passage fusion from evidence attribution, inspectable provenance from formal auditability, and evidentiality/grounding from substantive or legal correctness.

The pilot contract is used only as a comparison boundary: externally fixed historical ranked Top-k -> candidate-specific downstream normative evidence -> explanation-only local LLM -> no new codes -> no reordering -> no classification feedback.

### Gate

`0B-04B READY_FOR_DRAFTING -> drafting AI -> internal primary-PDF review -> correction if needed -> express author approval -> freeze -> assess opening 0B-05`.

Experimental-AI review is required only if literature interpretation affects frozen experimental facts/claims or restrictions under its authority. Manuscript drafting, final novelty/gap claims, new-literature search, reopening G6/G7, and later-phase opening remain prohibited until their gates.