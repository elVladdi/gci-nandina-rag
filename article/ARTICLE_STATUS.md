# Estado del artículo / Article Status

## Español

### Estado general

- Rama de trabajo: `article/main-manuscript`.
- Estado global: `IN_ANALYSIS`.
- Fase `0A — Ground truth documental y experimental`: **`CLOSED / APPROVED`**.
- Fase activa: **`0B — Mapa crítico de literatura y taxonomía`**.
- `0B-01`: **`APPROVED / FROZEN`**.
- `0B-02`: **`APPROVED / FROZEN`**.
- `0B-03A`: **`APPROVED / FROZEN`**.
- `0B-03B`: **`APPROVED / FROZEN`**.
- `0B-04A`: **`APPROVED / FROZEN`**.
- `0B-04B`: **`APPROVED / FROZEN`**.
- `0B-05A`: **`APPROVED / FROZEN`**.
- `0B-05B`: **`APPROVED / FROZEN`**.
- `0B-05C`: **`NOT_STARTED / ELIGIBLE_FOR_DEFINITION`**.
- `0B-06`: `NOT_STARTED`.
- `0C — Gap, contribución y Research Questions`: `BLOCKED` hasta cerrar 0B.
- `0D — Arquitectura editorial y journal fit`: `BLOCKED` hasta cerrar 0C.
- Target journal: `PENDING — se decidirá en Fase 0D`.
- Manuscrito redactado: no iniciado.
- Corpus consolidado: `62` obras/documentos distintos; acceso primario verificable `62/62`.
- Idioma del chat: español.
- Artefactos GitHub: español + inglés con equivalencia semántica.

### Ground truth y gobernanza

Continúan gobernando:

- `article/ground_truth/0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md`;
- `article/ground_truth/0A02_EXPERIMENTAL_GROUND_TRUTH_FROZEN.md`.

La revisión bibliográfica no modifica el Plan Maestro ni el ground truth 0A. La IA experimental conserva autoridad exclusiva sobre el Plan Maestro y solo interviene en el flujo bibliográfico cuando una interpretación afecta hechos/claims experimentales congelados o restricciones bajo su autoridad.

### Distinciones fundacionales congeladas

0B-04A:

`QUERY/DOCUMENT REPRESENTATION ≠ CANDIDATE GENERATION ≠ ANN/INDEX SEARCH ≠ RERANKING ≠ FINAL RANKING`.

0B-04B:

`RAG ≠ RETRIEVAL_AUGMENTED_PRETRAINING ≠ RETRIEVE_THEN_GENERATE ≠ QUERY_EXPANSION ≠ QUERY_REWRITING ≠ PASSAGE_FUSION ≠ EVIDENTIALITY_GUIDED_GENERATION`.

`RETRIEVED PASSAGE ≠ EVIDENCE ATTRIBUTION ≠ EVIDENTIALITY ≠ GROUNDING GUARANTEE ≠ PROVENANCE VERIFICATION ≠ FORMAL AUDITABILITY ≠ LEGAL CORRECTNESS`.

0B-05A:

`DATASET DOCUMENTATION ≠ DATASET IDENTITY / VERSIONING ≠ DATA PROVENANCE / LINEAGE ≠ WORKFLOW PROVENANCE ≠ REPRODUCIBILITY ≠ REPLICATION ≠ GENERALIZATION`.

`DOCUMENTATION / PROVENANCE ≠ TRANSPARENCY TRAIL ≠ INTERNAL LIFECYCLE AUDIT ≠ FORMAL OUTPUT-LEVEL AUDITABILITY ≠ SUBSTANTIVE / LEGAL CORRECTNESS`.

0B-05B:

- `data`, `information` y `knowledge` no se tratan como sinónimos universales ni como etapas lineales necesarias; sus relaciones dependen del marco conceptual.
- `DOCUMENTED / EXPLICIT KNOWLEDGE ≠ TOTAL EXPERT KNOWLEDGE`.
- `DOCUMENT RETRIEVAL ≠ EXPERT INTERPRETATION ≠ LEGAL CORRECTNESS`.
- `LLM-GENERATED EXPLANATION ≠ EXPERT KNOWLEDGE ≠ OFFICIAL CLASSIFICATION`.
- `DOCUMENTED_EXPLICIT_KNOWLEDGE` es únicamente `OPERACIONALIZACION_DEL_PROYECTO`, no ontología compartida por Zins, Hildreth & Kimble y Al-Hawamdeh.

Estas fronteras son metodológicas y no escalas de madurez ni cadenas de implicación.

### Candidatos provisionales

Ninguno constituye novelty ni gap definitivo.

- **F1:** `CANDIDATE_GAP_ONLY — SURVIVES IN NARROW FORM`.
- **F2:** `CANDIDATE_GAP_ONLY — FURTHER NARROWED`.
- **F3:** `CANDIDATE_GAP_ONLY — RETAINED WITH APPLICABILITY CAVEAT`.
- **F4:** `CANDIDATE_GAP_ONLY — RETAINED AS METHODOLOGICAL DISTINCTION`.
- **F5:** `CANDIDATE_GAP_ONLY — FURTHER NARROWED`; queda prohibida cualquier formulación amplia de ausencia de trazabilidad/auditabilidad. Solo permanece como candidato estrecho la evaluación formal, explícita y separada de auditabilidad documental por salida.
- **G6:** `ELIMINATED AS GAP CANDIDATE`.
- **G7:** `MERGED INTO F2 / ELIMINATED AS INDEPENDENT CANDIDATE`.

0B-05B no modifica estos estados: F1/F2/F4/F5 reciben únicamente `METHOD_BOUNDARY_RELEVANT`; F3 es `NOT_RELEVANT_TO_GAP_CANDIDATE` en ese lote.

### 0B-05B — cierre formal

Registros gobernantes:

- Prompt: `article/prompts/0B05B_INFORMATION_EXPLICIT_TACIT_KNOWLEDGE.md`.
- Revisión interna: `article/reviews/0B05B_INTERNAL_REVIEW.md` — `PASS WITH MINOR CORRECTIONS`, `MATERIAL_ERRORS = 0`.
- Aprobación del autor: `article/reviews/0B05B_AUTHOR_APPROVAL.md`.
- Artefacto canónico: `article/literature/0B05B_INFORMATION_EXPLICIT_TACIT_KNOWLEDGE_FROZEN.md`.
- Revisión experimental: `NOT_REQUIRED`.

Estado congelado:

```text
0B-05B = APPROVED / FROZEN
DRAFTING_DELIVERABLE = ANALYTICALLY_COMPLETE
INTERNAL_REVIEW = PASS WITH MINOR CORRECTIONS
MATERIAL_ERRORS = 0
AUTHOR_APPROVAL = RECEIVED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

Normalizaciones C1–C8 integradas:

- no congelar D-I-K como disyunción ontológica rígida;
- Zins: `44 panel contributors + researcher = 45 scholars`, aproximadamente `130` definiciones; separar participantes, síntesis y posición propia de Zins;
- Hildreth & Kimble: `duality`, no dicotomía rígida;
- claims anidados de Polanyi, Nonaka, Wenger, Lave, Cook & Brown, etc., permanecen secundarios si se usan independientemente;
- Al-Hawamdeh: externalized/explicit knowledge → information se trata como posición del autor, no consenso universal;
- `implicit/know-how` no se colapsa con `tacit` estricto;
- `DOCUMENTED_EXPLICIT_KNOWLEDGE` solo como operacionalización del proyecto;
- la autoridad, vigencia, jerarquía y suficiencia jurídica de fuentes oficiales se auditarán en 0B-05C.

### Siguiente gate

`0B-05C — Autoridad, vigencia y trazabilidad de fuentes normativas/oficiales` queda **`NOT_STARTED / ELIGIBLE_FOR_DEFINITION`**.

Antes de abrirlo se debe:

1. identificar el conjunto exacto de fuentes oficiales primarias que requieren auditoría;
2. definir alcance y criterios de autoridad, vigencia, fecha, jerarquía, identificador estable y función evidencial;
3. crear su prompt ejecutable;
4. mantener separado el rol de fuente normativa oficial de la literatura académica.

`0B-05C` no se abre automáticamente por el freeze de 0B-05B.

---

## English

### Overall status

- Working branch: `article/main-manuscript`.
- Global state: `IN_ANALYSIS`.
- Phase 0A: **`CLOSED / APPROVED`**.
- Active phase: **`0B — Critical literature map and taxonomy`**.
- 0B-01, 0B-02, 0B-03A, 0B-03B, 0B-04A, 0B-04B, 0B-05A, and 0B-05B are **`APPROVED / FROZEN`**.
- `0B-05C`: **`NOT_STARTED / ELIGIBLE_FOR_DEFINITION`**.
- `0B-06`: `NOT_STARTED`.
- 0C remains blocked until 0B closes; 0D remains blocked until 0C closes.
- Target journal remains pending until 0D; manuscript drafting has not started.
- Consolidated corpus: 62 distinct works/documents with primary access `62/62`.

### Ground truth and governance

Frozen 0A artifacts remain authoritative. Literature review cannot modify the Master Plan; the experimental AI retains exclusive authority over it and is invoked only when literature interpretation affects frozen experimental facts/claims or restrictions under its authority.

### Frozen foundational distinctions

0B-04A separates representation, candidate generation, ANN/index search, reranking, and final ranking.

0B-04B separates RAG variants, query transformation, passage fusion, evidentiality, provenance, formal auditability, and legal correctness.

0B-05A separates dataset documentation, identity/versioning, data/workflow provenance, reproducibility, replication, generalization, transparency trails, lifecycle audit, output-level auditability, and substantive/legal correctness.

0B-05B freezes that data/information/knowledge are not universal synonyms or necessary linear stages; it also freezes:

`DOCUMENTED / EXPLICIT KNOWLEDGE ≠ TOTAL EXPERT KNOWLEDGE`

`DOCUMENT RETRIEVAL ≠ EXPERT INTERPRETATION ≠ LEGAL CORRECTNESS`

`LLM-GENERATED EXPLANATION ≠ EXPERT KNOWLEDGE ≠ OFFICIAL CLASSIFICATION`.

`DOCUMENTED_EXPLICIT_KNOWLEDGE` is project operationalization only, not a shared ontology of the three conceptual sources.

### Provisional gap candidates

F1–F5 remain provisional; none is final novelty or a definitive gap. G6 remains eliminated and G7 remains merged into F2. 0B-05B changes none of these states: F1/F2/F4/F5 receive methodological boundary relevance only and F3 is not relevant to the gap candidate in this batch.

### 0B-05B formal closure

Governing records:

- `article/prompts/0B05B_INFORMATION_EXPLICIT_TACIT_KNOWLEDGE.md`;
- `article/reviews/0B05B_INTERNAL_REVIEW.md`;
- `article/reviews/0B05B_AUTHOR_APPROVAL.md`;
- `article/literature/0B05B_INFORMATION_EXPLICIT_TACIT_KNOWLEDGE_FROZEN.md`.

Frozen state:

```text
0B-05B = APPROVED / FROZEN
DRAFTING_DELIVERABLE = ANALYTICALLY_COMPLETE
INTERNAL_REVIEW = PASS WITH MINOR CORRECTIONS
MATERIAL_ERRORS = 0
AUTHOR_APPROVAL = RECEIVED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

C1–C8 are integrated: non-rigid D-I-K interpretation; normalized Zins attribution/counting; Hildreth & Kimble duality; nested-source control; Al-Hawamdeh's position kept as author-specific; implicit/know-how kept distinct from strict tacit knowledge; documented explicit knowledge restricted to project operationalization; and official-source authority/currency/hierarchy reserved for 0B-05C.

### Next gate

`0B-05C — Authority, currency, and traceability of normative/official sources` is now **`NOT_STARTED / ELIGIBLE_FOR_DEFINITION`**.

Before opening it, the workflow must identify the exact official primary sources to audit, define authority/currency/date/hierarchy/stable-identifier/evidentiary-role criteria, create an executable prompt, and preserve the separation between official normative sources and academic literature.

The 0B-05B freeze does not automatically open 0B-05C.
