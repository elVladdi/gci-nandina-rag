# Estado del artículo / Article Status

## Español

### Estado general

- Rama de trabajo: `article/main-manuscript`.
- Estado global: `IN_ANALYSIS`.
- `0A — Ground truth documental y experimental`: **`CLOSED / APPROVED`**.
- `0B — Mapa crítico de literatura y taxonomía`: **`CLOSED / APPROVED`**.
- `0B-01` a `0B-06`: **`APPROVED / FROZEN`**.
- Siguiente fase editorial: **`0C — Gap, contribución y Research Questions`**.
- Estado formal de `0C`: **`NOT_STARTED`**.
- `0C_ENTRY_GATE = PENDING / NOT_OPENED`.
- `0D — Arquitectura editorial y journal fit`: **`BLOCKED`** hasta cerrar 0C.
- Target journal: `PENDING — se decidirá en Fase 0D`.
- `FINAL_GAP = NOT_DEFINED`.
- `NOVELTY = NOT_DECLARED`.
- `MANUSCRIPT_DRAFTING = NOT_AUTHORIZED`.
- `EXPERIMENTAL_REVIEW = NOT_REQUIRED` para el cierre de 0B.
- Corpus heredado consolidado: `62` obras/documentos con acceso primario verificable `62/62`.
- Registro de nueva literatura: `article/literature/BIBLIOGRAPHIC_ADMISSION_REGISTRY.md`.

### Gobernanza

Continúan gobernando:

- `article/ground_truth/0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md`;
- `article/ground_truth/0A02_EXPERIMENTAL_GROUND_TRUTH_FROZEN.md`;
- `article/ARTICLE_WRITING_PLAN.md`;
- `article/DECISIONS.md`;
- `article/SOURCE_REGISTRY.md`;
- `article/CLAIM_EVIDENCE_MATRIX.md`;
- freezes de 0B-01 a 0B-06.

La IA Experimental conserva autoridad exclusiva sobre el Plan Maestro y decisiones experimentales. La IA Gestora / Editor Científico Principal administra estados editoriales, gates, claims y admisión bibliográfica. La IA de Redacción ejecuta únicamente prompts cerrados versionados.

### Distinciones metodológicas/documentales congeladas

Se mantienen, entre otras:

`QUERY/DOCUMENT REPRESENTATION ≠ CANDIDATE GENERATION ≠ ANN/INDEX SEARCH ≠ RERANKING ≠ FINAL RANKING`.

`RAG ≠ RETRIEVAL_AUGMENTED_PRETRAINING ≠ RETRIEVE_THEN_GENERATE ≠ QUERY_EXPANSION ≠ QUERY_REWRITING ≠ PASSAGE_FUSION ≠ EVIDENTIALITY_GUIDED_GENERATION`.

`RETRIEVED PASSAGE ≠ EVIDENCE ATTRIBUTION ≠ EVIDENTIALITY ≠ GROUNDING GUARANTEE ≠ PROVENANCE VERIFICATION ≠ FORMAL AUDITABILITY ≠ LEGAL CORRECTNESS`.

`DATASET DOCUMENTATION ≠ DATASET IDENTITY/VERSIONING ≠ DATA PROVENANCE/LINEAGE ≠ WORKFLOW PROVENANCE ≠ REPRODUCIBILITY ≠ REPLICATION ≠ GENERALIZATION`.

`DOCUMENT RETRIEVAL ≠ EXPERT INTERPRETATION ≠ LEGAL CORRECTNESS`.

`EXPERIMENTAL_SOURCE_SNAPSHOT ≠ CURRENT_OFFICIAL_SOURCE_STATE`.

`SOURCE_VERSION_DRIFT ≠ SCOPE_OVERLAP ≠ RETRIEVAL_OUTPUT_OVERLAP ≠ EXPERIMENTAL_METRIC_IMPACT`.

### Cierre de 0B-05C preservado

0B-05C permanece `APPROVED / FROZEN`. Se preserva exactamente:

```text
EV03_METRIC_IMPACT = ZERO_AGGREGATE_CHANGE
EV04_METRIC_IMPACT = TINY_NONZERO_MRR_DECREASE_ONLY
D1A_METRIC_IMPACT = POSITIVE_NONZERO_EXACT_RANKING_CHANGE_WITH_MINOR_HS4_MIXED_EFFECT
0B05C_METRIC_IMPACT = METHOD_DEPENDENT / NONZERO_EV04_MRR_AND_D1A
DOWNSTREAM_REEXECUTION = NOT_REQUIRED
```

No está autorizado resumirlo como ausencia de impacto numérico.

### 0B-06 — cierre formal

Registros gobernantes:

- `article/reviews/0B06_BIBLIOGRAPHIC_NEED_ASSESSMENT.md`;
- `article/prompts/0B06_DIRECTED_NEW_LITERATURE_FALSIFICATION_SEARCH.md`;
- `article/responses/0B06_DIRECTED_NEW_LITERATURE_FALSIFICATION_SEARCH_RESPONSE_V01.md`;
- `article/reviews/0B06_INTERNAL_REVIEW.md`;
- `article/reviews/0B06_AUTHOR_APPROVAL.md`;
- `article/literature/0B06_DIRECTED_NEW_LITERATURE_FALSIFICATION_SEARCH_FROZEN.md`;
- `article/reviews/0B_PHASE_CLOSURE.md`.

Estado congelado del pressure test:

```text
F1 = NO_DIRECT_MATCH_FOUND_WITHIN_SEARCH_SCOPE
F2 = PARTIAL_PRIOR_ART_FOUND
F3 = NO_DIRECT_MATCH_FOUND_WITHIN_SEARCH_SCOPE
F5 = DIRECT_PRIOR_ART_FOUND
F5_GENERAL_REGULATORY_AI_ABSENCE_CLAIM = FALSIFIED
```

Interpretación para 0C:

- F1: candidato estrecho; el resultado negativo acotado no demuestra novelty.
- F2: candidato estrecho con prior art parcial; debe preservar un Top-k externo e inmutable y un generador únicamente explicativo sin alterar candidatos ni retroalimentar clasificación.
- F3: principio/candidato metodológico con caveat de aplicabilidad; ausencia de grouped split documentado no prueba leakage.
- F4: frontera metodológica, no novelty independiente.
- F5: la formulación general queda falsada; cualquier variante posterior debe ser más estrecha y contextual.
- G6: eliminado.
- G7: absorbido en F2.

Admisión bibliográfica:

```text
N01 = APPROVED_NEW
N02 = REVIEW_REQUIRED / NOT_ADMITTED_YET
N03 = REJECT
N04 = REJECT
```

### Gate vigente

```text
PHASE_0B = CLOSED / APPROVED
0C = NOT_STARTED
0C_ENTRY_GATE = PENDING / NOT_OPENED
NEXT_EDITORIAL_ACTION = DEFINE_0C_SCOPE_AND_ENTRY_GATE
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
```

El cierre de 0B no abre automáticamente 0C ni autoriza redacción del manuscrito.

---

## English

### Overall status

- Working branch: `article/main-manuscript`.
- Global state: `IN_ANALYSIS`.
- `0A — Documentary and experimental ground truth`: **`CLOSED / APPROVED`**.
- `0B — Critical literature map and taxonomy`: **`CLOSED / APPROVED`**.
- `0B-01` through `0B-06`: **`APPROVED / FROZEN`**.
- Next editorial phase: **`0C — Gap, contribution, and Research Questions`**.
- Formal 0C state: **`NOT_STARTED`**.
- `0C_ENTRY_GATE = PENDING / NOT_OPENED`.
- 0D remains **`BLOCKED`** until 0C closes.
- `FINAL_GAP = NOT_DEFINED`.
- `NOVELTY = NOT_DECLARED`.
- `MANUSCRIPT_DRAFTING = NOT_AUTHORIZED`.
- `EXPERIMENTAL_REVIEW = NOT_REQUIRED` for Phase-0B closure.

Frozen 0B distinctions remain authoritative through their canonical artifacts. 0B-05C retains exactly the differentiated EV03/EV04/D1a corrective interpretation and must not be reduced to no numerical impact.

### 0B-06 formal closure

Governing records are the 0B-06 need assessment, prompt, Writing-AI response, internal review, author approval, frozen artifact, and `article/reviews/0B_PHASE_CLOSURE.md`.

Frozen pressure-test state:

```text
F1 = NO_DIRECT_MATCH_FOUND_WITHIN_SEARCH_SCOPE
F2 = PARTIAL_PRIOR_ART_FOUND
F3 = NO_DIRECT_MATCH_FOUND_WITHIN_SEARCH_SCOPE
F5 = DIRECT_PRIOR_ART_FOUND
F5_GENERAL_REGULATORY_AI_ABSENCE_CLAIM = FALSIFIED
```

For 0C: F1 remains only a narrow candidate; F2 remains narrow with partial prior art and mandatory isolation of an explanation-only generator from an externally fixed immutable Top-k; F3 remains an applicability-conditioned methodological principle; F4 is a methodological boundary rather than independent novelty; broad F5 is falsified and any later variant must be narrower and contextual; G6 is eliminated and G7 is merged into F2.

Bibliographic admission state:

```text
N01 = APPROVED_NEW
N02 = REVIEW_REQUIRED / NOT_ADMITTED_YET
N03 = REJECT
N04 = REJECT
```

### Current gate

```text
PHASE_0B = CLOSED / APPROVED
0C = NOT_STARTED
0C_ENTRY_GATE = PENDING / NOT_OPENED
NEXT_EDITORIAL_ACTION = DEFINE_0C_SCOPE_AND_ENTRY_GATE
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
```

Phase-0B closure does not automatically open 0C and does not authorize manuscript drafting.
