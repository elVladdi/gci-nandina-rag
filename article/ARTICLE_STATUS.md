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
- Estado de `0B-04B`: **`INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING`**.
- Revisión interna de `0B-04B`: **`PASS WITH MINOR CORRECTIONS`**, `MATERIAL_ERRORS = 0`.
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

### 0B-04B — revisión interna completada

Alcance:

`article/literature/0B04_SCOPE_AND_BATCH_PLAN.md`.

Prompt ejecutado:

`article/prompts/0B04B_RAG_QUERY_TRANSFORMATION_GROUNDING_FOUNDATIONS.md`.

Revisión interna:

`article/reviews/0B04B_INTERNAL_REVIEW.md` — **`PASS WITH MINOR CORRECTIONS`**, `MATERIAL_ERRORS = 0`, revisión experimental `NOT_REQUIRED`.

PDF verificados:

1. `Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.pdf`
2. `REALM-Retrieval-Augmented Language Model Pre-Training.pdf`
3. `Leveraging passage retrieval with generative models for open domain question answering.pdf`
4. `Query2doc-Query Expansion whit Large Lenguage Models.pdf`
5. `Query Rewriting for Retrieval-Augmented Large Language Models.pdf`
6. `Evidentiality-guided Generation for Knowledge-Intensive NLP Tasks.pdf`

La revisión primaria confirma las fronteras:

`RAG ≠ RETRIEVAL_AUGMENTED_PRETRAINING ≠ RETRIEVE_THEN_GENERATE ≠ QUERY_EXPANSION ≠ QUERY_REWRITING ≠ PASSAGE_FUSION ≠ EVIDENTIALITY_GUIDED_GENERATION`.

Y:

`RETRIEVED PASSAGE ≠ EVIDENCE ATTRIBUTION ≠ EVIDENTIALITY ≠ GROUNDING GUARANTEE ≠ PROVENANCE VERIFICATION ≠ FORMAL AUDITABILITY ≠ LEGAL CORRECTNESS`.

Normalizaciones obligatorias para el eventual freeze incluyen: gobernar la discrepancia RAG `17%` vs Tabla 4 `11.7%` por la tabla; preservar REALM como retrieval-augmented pretraining/span-based Open-QA; no convertir passage fusion en attribution; tratar Query2doc y query rewriting como transformaciones upstream que pueden cambiar retrieval; preservar resultados OOD mixtos y riesgos de pseudo-documentos; gobernar Asai et al. por cinco datasets pese al caption `six datasets`; interpretar el chequeo humano `95%/96%` como validación de labels bajo su protocolo y no como auditability/legal-correctness score.

Contrato del piloto usado únicamente como frontera comparativa:

`ranking histórico Top-k fijado -> evidencia normativa posterior por candidato -> LLM local exclusivamente explicativo -> sin códigos nuevos -> sin reordenamiento -> sin feedback clasificatorio`.

F1–F5 no cambian de estado por este lote; G6 permanece eliminado y G7 absorbido en F2.

### Gate vigente

```text
0B-04B = INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING
-> aprobación expresa del autor
-> integrar C1–C13 en artefacto canónico
-> freeze 0B-04B
-> evaluar apertura de 0B-05
```

Hasta aprobación expresa del autor no está autorizado crear el freeze de 0B-04B ni abrir 0B-05.

La IA experimental no fue requerida porque la revisión no modifica hechos/claims experimentales congelados ni restricciones bajo su autoridad.

### Prohibiciones vigentes

Mientras 0B-04B espere aprobación del autor no está autorizado:

- redactar Introduction/Related Work/Methods/Results/Discussion/Conclusions;
- declarar novelty, gap definitivo o superioridad general de RAG/métodos;
- buscar literatura nueva;
- equiparar provenance/evidentiality/grounding con auditabilidad o legal correctness;
- modificar 0A o el Plan Maestro;
- reinterpretar resultados experimentales congelados fuera de su alcance;
- reabrir G6/G7;
- congelar 0B-04B sin aprobación expresa;
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
- 0B-04B status: **`INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING`**.
- Internal review verdict: **`PASS WITH MINOR CORRECTIONS`**, `MATERIAL_ERRORS = 0`.
- 0B-05 is `NOT_STARTED / CLOSED_BY_GATE`; 0B-06 is not started.
- 0C remains blocked until 0B closes; 0D remains blocked until 0C closes.
- Target journal remains pending until 0D; manuscript drafting has not started.

### Governing ground truth

Frozen 0A documentary and experimental artifacts remain authoritative. Literature review cannot modify the Master Plan; exclusive Master-Plan authority remains with the experimental workflow.

### Closed blocks and provisional candidates

0B-04A froze `QUERY/DOCUMENT REPRESENTATION ≠ CANDIDATE GENERATION ≠ ANN/INDEX SEARCH ≠ RERANKING ≠ FINAL RANKING` and does not reinterpret D1a beyond its specific exploratory dense implementation.

F1–F5 remain provisional in narrowed/methodological forms; G6 remains eliminated and G7 remains merged into F2. 0B-04B does not change those candidate states.

### 0B-04B internal review complete

Executed prompt: `article/prompts/0B04B_RAG_QUERY_TRANSFORMATION_GROUNDING_FOUNDATIONS.md`.

Internal review: `article/reviews/0B04B_INTERNAL_REVIEW.md` — **`PASS WITH MINOR CORRECTIONS`**, `MATERIAL_ERRORS = 0`, experimental review `NOT_REQUIRED`.

The six assigned primary PDFs were independently checked. The review confirms the methodological boundaries:

`RAG ≠ RETRIEVAL_AUGMENTED_PRETRAINING ≠ RETRIEVE_THEN_GENERATE ≠ QUERY_EXPANSION ≠ QUERY_REWRITING ≠ PASSAGE_FUSION ≠ EVIDENTIALITY_GUIDED_GENERATION`.

And:

`RETRIEVED PASSAGE ≠ EVIDENCE ATTRIBUTION ≠ EVIDENTIALITY ≠ GROUNDING GUARANTEE ≠ PROVENANCE VERIFICATION ≠ FORMAL AUDITABILITY ≠ LEGAL CORRECTNESS`.

Required freeze normalizations include governing the RAG `17%` prose/Table-4 discrepancy by `11.7%`; preserving REALM as retrieval-augmented pretraining with span-based Open-QA; separating FiD passage fusion from attribution; treating Query2doc and query rewriting as upstream transformations capable of changing retrieval; preserving mixed OOD results and pseudo-document risks; governing Asai et al. by five datasets despite the `six datasets` caption; and interpreting the `95%/96%` human check only as label validation under its stated protocol rather than auditability or legal correctness.

The pilot contract remains only a comparison boundary: externally fixed historical ranked Top-k -> candidate-specific downstream normative evidence -> explanation-only local LLM -> no new codes -> no reordering -> no classification feedback.

### Gate

`0B-04B INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING -> express author approval -> integrate C1–C13 into the canonical artifact -> freeze -> assess opening 0B-05`.

Until express author approval, 0B-04B cannot be frozen and 0B-05 cannot be opened. Experimental-AI review was not required because no frozen experimental fact/claim or restriction was changed.

### Current prohibitions

Manuscript drafting, final novelty/gap claims, universal RAG superiority claims, new-literature search, conflating provenance/evidentiality/grounding with auditability/legal correctness, modifying 0A or the Master Plan, reopening G6/G7, freezing 0B-04B without author approval, or advancing to 0B-05/0B-06/0C remain prohibited until their gates.