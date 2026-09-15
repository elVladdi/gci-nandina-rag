# Estado del artículo / Article Status

## Español

### Estado general

- Rama de trabajo: `article/main-manuscript`.
- Estado global: `IN_ANALYSIS`.
- `0A — Ground truth documental y experimental`: **`CLOSED / APPROVED`**.
- `0B — Mapa crítico de literatura y taxonomía`: **`CLOSED / APPROVED`**.
- `0B-01` a `0B-06`: **`APPROVED / FROZEN`**.
- Fase activa: **`0C — Gap, contribución y Research Questions`**.
- `0C_ENTRY_GATE`: **`PASS / OPENED`**.
- `0C_DRAFTING_ANALYSIS`: **`COMPLETED_PENDING_EDITORIAL_REVIEW`**.
- `0C_INTERNAL_REVIEW`: **`PASS`**.
- `0C`: **`INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING`**.
- `AUTHOR_APPROVAL`: **`PENDING`**.
- `FREEZE_0C`: **`NOT_AUTHORIZED_YET`**.
- `0D — Arquitectura editorial y journal fit`: **`BLOCKED`** hasta cerrar 0C.
- Target journal: `PENDING — se decidirá en Fase 0D`.
- `FINAL_GAP = NOT_DEFINED`.
- `NOVELTY = NOT_DECLARED`.
- `MANUSCRIPT_DRAFTING = NOT_AUTHORIZED`.
- `NEW_LITERATURE_SEARCH = NOT_AUTHORIZED`.
- `EXPERIMENTAL_REVIEW = NOT_REQUIRED` para el gate editorial actual.
- Corpus heredado consolidado: `62` obras/documentos con acceso primario verificable `62/62`.
- Registro de nueva literatura: `article/literature/BIBLIOGRAPHIC_ADMISSION_REGISTRY.md`.

### Gobernanza

Continúan gobernando:

- `article/ground_truth/0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md`;
- `article/ground_truth/0A02_EXPERIMENTAL_GROUND_TRUTH_FROZEN.md`;
- freezes `0B-01` a `0B-06`;
- `article/reviews/0B_PHASE_CLOSURE.md`;
- `article/reviews/0C_ENTRY_GATE.md`;
- `article/prompts/0C_GAP_CONTRIBUTION_RESEARCH_QUESTIONS.md`;
- `article/responses/0C_GAP_CONTRIBUTION_RESEARCH_QUESTIONS_RESPONSE_V01.md`;
- `article/reviews/0C_INTERNAL_REVIEW.md`;
- `article/ARTICLE_WRITING_PLAN.md`;
- `article/DECISIONS.md`;
- `article/SOURCE_REGISTRY.md`;
- `article/CLAIM_EVIDENCE_MATRIX.md`;
- `article/STYLE_GUIDE.md`.

La IA Experimental conserva autoridad exclusiva sobre el Plan Maestro y decisiones experimentales. La IA Gestora / Editor Científico Principal administra estados editoriales, gates, claims y admisión bibliográfica. La IA de Redacción ejecuta únicamente prompts cerrados versionados.

### Snapshot experimental consumido por 0C

El Plan Maestro `SRC-03` fue consumido en modo solo lectura:

```text
branch = docs/plan-maestro-temporal-2026-08-31
HEAD = f4d20dfe46181cb2740c4e4cd6604b0bff7a48f6
blob = adcd9be3aaa9c13929575d6f348fa6f9693bccbf
```

El estado vivo registra, entre otros puntos, Grupo 2B cerrado con limitaciones no bloqueantes, EXP-11B retrieval cerrado/aprobado/integrado, EXP-12 cerrado sin retrieval bajo el diseño congelado y Grupo 3 como siguiente bloque de métricas/inferencia todavía no ejecutado. 0C no transforma resultados pendientes en hechos ni modifica el Plan Maestro.

### Distinciones congeladas relevantes

Se mantienen, entre otras:

`QUERY/DOCUMENT REPRESENTATION ≠ CANDIDATE GENERATION ≠ ANN/INDEX SEARCH ≠ RERANKING ≠ FINAL RANKING`.

`RAG ≠ RETRIEVAL_AUGMENTED_PRETRAINING ≠ RETRIEVE_THEN_GENERATE ≠ QUERY_EXPANSION ≠ QUERY_REWRITING ≠ PASSAGE_FUSION ≠ EVIDENTIALITY_GUIDED_GENERATION`.

`RETRIEVED PASSAGE ≠ EVIDENCE ATTRIBUTION ≠ EVIDENTIALITY ≠ GROUNDING GUARANTEE ≠ PROVENANCE VERIFICATION ≠ FORMAL AUDITABILITY ≠ LEGAL CORRECTNESS`.

`DATASET DOCUMENTATION ≠ DATASET IDENTITY/VERSIONING ≠ DATA PROVENANCE/LINEAGE ≠ WORKFLOW PROVENANCE ≠ REPRODUCIBILITY ≠ REPLICATION ≠ GENERALIZATION`.

`DOCUMENT RETRIEVAL ≠ EXPERT INTERPRETATION ≠ LEGAL CORRECTNESS`.

`EXPERIMENTAL_SOURCE_SNAPSHOT ≠ CURRENT_OFFICIAL_SOURCE_STATE`.

`SOURCE_VERSION_DRIFT ≠ SCOPE_OVERLAP ≠ RETRIEVAL_OUTPUT_OVERLAP ≠ EXPERIMENTAL_METRIC_IMPACT`.

`LITERATURE_GAP ≠ PROJECT_FEATURE ≠ SCIENTIFIC_CONTRIBUTION ≠ EXPERIMENTAL_RESULT ≠ NOVELTY_CLAIM`.

### Estado transferido desde 0B hacia 0C

```text
F1 = NO_DIRECT_MATCH_FOUND_WITHIN_SEARCH_SCOPE
F2 = PARTIAL_PRIOR_ART_FOUND
F3 = NO_DIRECT_MATCH_FOUND_WITHIN_SEARCH_SCOPE
F4 = METHODOLOGICAL_BOUNDARY_NOT_INDEPENDENT_NOVELTY
F5 = DIRECT_PRIOR_ART_FOUND
F5_GENERAL_REGULATORY_AI_ABSENCE_CLAIM = FALSIFIED
G6 = ELIMINATED_AS_GAP_CANDIDATE
G7 = MERGED_INTO_F2
```

Interpretación:

- F1 es solo un candidato estrecho; la búsqueda negativa acotada no demuestra novelty.
- F2 debe preservar `EXTERNAL_FIXED_TOP_K + DOWNSTREAM_EXPLANATION_ONLY + NO_INSERT/DELETE/SUBSTITUTE/REORDER + NO_CLASSIFICATION_FEEDBACK`.
- F3 es metodológico y condicionado por la estructura de dependencia; ausencia de grouped split documentado no prueba leakage.
- F4 es una frontera metodológica, no novelty independiente.
- F5 general está falsado; cualquier variante posterior debe ser más estrecha y contextual.
- G6 permanece eliminado; G7 permanece absorbido en F2.

### Admisión bibliográfica posterior a 0B-06

```text
N01 = APPROVED_NEW
N02 = REVIEW_REQUIRED / NOT_ADMITTED_YET
N03 = REJECT
N04 = REJECT
```

N01 puede considerarse dentro de sus límites; no existe obligación de citarlo. N02 no puede usarse como evidencia determinante hasta una revisión específica.

### Resultado de la revisión interna 0C

La revisión `article/reviews/0C_INTERNAL_REVIEW.md` concluyó:

```text
0C_INTERNAL_REVIEW = PASS
MATERIAL_ERRORS = 0
MINOR_CORRECTIONS_REQUIRED = 0
0C_PROVISIONAL_CENTRAL_CONTRIBUTION = B_ARCHITECTURAL_METHODOLOGICAL
RQ1 = RETAINED
RQ2 = RETAINED
RQ3 = RETAINED_WITH_HE4_LIMITATIONS
RQ4 = RETAINED_CONDITIONAL_ON_GROUP3
EXP11B_EDITORIAL_GOVERNANCE_LAG = PRESENT / NONBLOCKING_FOR_0C_CURRENT_SCOPE
EXPERIMENTAL_REVIEW = NOT_REQUIRED
```

La alternativa B queda recomendada para aprobación del autor como **contribución central provisional de posicionamiento**, no como novelty demostrada. La alternativa A se conserva como fallback editorial conservador. La alternativa C no se selecciona como contribución primaria porque F5 general fue falsado y N01 constituye prior art directo para evaluación de source support/audit-oriented traces en regulatory/legal AI.

El posicionamiento metodológico solo sobrevive bajo el contrato completo y acotado:

```text
EXTERNAL_FIXED_HISTORICAL_RANKING
+ POST_RANKING_NORMATIVE_EVIDENCE_WITHOUT_RERANKING
+ DOWNSTREAM_EXPLANATION_ONLY
+ NO_INSERT_DELETE_SUBSTITUTE_REORDER
+ NO_CLASSIFICATION_FEEDBACK
+ DAM_AWARE_PARTITIONING_WHERE_DEPENDENCE_EXISTS
+ FUNCTION_SPECIFIC_EVALUATION
```

Esto no autoriza afirmar que cada componente sea novedoso ni que no exista prior art equivalente fuera del alcance revisado.

### Desfase editorial EXP-11B

`SRC-03` registra EXP-11B retrieval como cerrado/aprobado/integrado, mientras `CLAIM_EVIDENCE_MATRIX.md` conserva C10/C11 como `PROHIBITED` con evidencia todavía redactada en términos de retrieval pendiente.

Estado editorial:

`EXP11B_EDITORIAL_GOVERNANCE_LAG = PRESENT / NONBLOCKING_FOR_0C_CURRENT_SCOPE`.

0C no utiliza la dirección H150/H200 para sostener el gap, la contribución B o las RQs. Por ello el desfase no bloquea el gate actual. Antes de usar resultados EXP-11B en el manuscrito se requerirá reconciliación editorial explícita de C10/C11 contra la evidencia experimental gobernante.

### Prohibiciones vigentes

Hasta el freeze formal de 0C no está autorizado:

- declarar novelty final;
- convertir el gap candidato en ausencia universal de prior art;
- usar la diferencia arquitectónica por sí sola como prueba de novelty;
- restaurar la formulación general falsada de F5;
- integrar resultados EXP-11B como claims del artículo sin reconciliar C10/C11;
- cerrar inferencialmente HE2 o HE5 antes del gate experimental aplicable;
- equiparar auditabilidad/source support/trazabilidad con legal correctness;
- seleccionar revista;
- abrir 0D;
- redactar secciones del manuscrito.

### Gate vigente

```text
PHASE_0B = CLOSED / APPROVED
0C_ENTRY_GATE = PASS / OPENED
0C = INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING
0C_INTERNAL_REVIEW = PASS
NEXT_ACTOR = AUTHOR
0C_PROVISIONAL_CENTRAL_CONTRIBUTION = B_ARCHITECTURAL_METHODOLOGICAL
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
AUTHOR_APPROVAL = PENDING
FREEZE_0C = NOT_AUTHORIZED_YET
0D = BLOCKED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
```

---

## English

### Overall status

- Working branch: `article/main-manuscript`.
- Global state: `IN_ANALYSIS`.
- Phase 0A: **`CLOSED / APPROVED`**.
- Phase 0B: **`CLOSED / APPROVED`**; 0B-01 through 0B-06 are `APPROVED / FROZEN`.
- Active phase: **`0C — Gap, contribution, and Research Questions`**.
- `0C_ENTRY_GATE = PASS / OPENED`.
- `0C_DRAFTING_ANALYSIS = COMPLETED_PENDING_EDITORIAL_REVIEW`.
- `0C_INTERNAL_REVIEW = PASS`.
- `0C = INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING`.
- `AUTHOR_APPROVAL = PENDING`.
- `FREEZE_0C = NOT_AUTHORIZED_YET`.
- 0D remains `BLOCKED` until 0C closes.
- `FINAL_GAP = NOT_DEFINED`.
- `NOVELTY = NOT_DECLARED`.
- `MANUSCRIPT_DRAFTING = NOT_AUTHORIZED`.
- `NEW_LITERATURE_SEARCH = NOT_AUTHORIZED`.
- `EXPERIMENTAL_REVIEW = NOT_REQUIRED` for the current editorial gate.

### Governance and experimental state

Frozen 0A/0B artifacts, Phase-0B closure, the 0C entry gate, 0C prompt/response/internal review, Master Writing Plan, Decisions, Source Registry, Claim–Evidence Matrix, and Style Guide govern the current state. The Experimental AI retains exclusive authority over the Master Plan and experimental decisions.

The read-only `SRC-03` snapshot consumed by 0C is branch `docs/plan-maestro-temporal-2026-08-31`, HEAD `f4d20dfe46181cb2740c4e4cd6604b0bff7a48f6`, blob `adcd9be3aaa9c13929575d6f348fa6f9693bccbf`. It records Group 2B closed with nonblocking limitations, EXP-11B retrieval closed/approved/integrated, EXP-12 closed without retrieval under the frozen design, and Group 3 as the next metrics/inference block not yet executed.

### Frozen bibliographic transfer state

F1 has a bounded negative result only; F2 has partial prior art and survives only under strict fixed-ranking/downstream-explanation isolation; F3 is applicability-conditioned; F4 is a methodological boundary; broad F5 is falsified; G6 is eliminated and G7 merged into F2. N01 is `APPROVED_NEW`; N02 is not admitted; N03/N04 are rejected.

### 0C internal-review result

```text
0C_INTERNAL_REVIEW = PASS
MATERIAL_ERRORS = 0
MINOR_CORRECTIONS_REQUIRED = 0
0C_PROVISIONAL_CENTRAL_CONTRIBUTION = B_ARCHITECTURAL_METHODOLOGICAL
RQ1 = RETAINED
RQ2 = RETAINED
RQ3 = RETAINED_WITH_HE4_LIMITATIONS
RQ4 = RETAINED_CONDITIONAL_ON_GROUP3
EXP11B_EDITORIAL_GOVERNANCE_LAG = PRESENT / NONBLOCKING_FOR_0C_CURRENT_SCOPE
EXPERIMENTAL_REVIEW = NOT_REQUIRED
```

Alternative B is recommended for author approval as the **provisional central positioning contribution**, not as demonstrated novelty. Alternative A remains the conservative fallback. C is not selected as primary because broad F5 is falsified and N01 provides direct regulatory/legal-AI prior art for source-support/audit-oriented trace evaluation.

The methodological positioning survives only as the complete bounded contract: externally fixed historical ranking; subsequent normative evidence that cannot rerank; downstream explanation-only generation; no insertion/deletion/substitution/reordering; no classification feedback; DAM-aware partitioning where dependence exists; and function-specific evaluation.

### EXP-11B editorial lag

`SRC-03` records EXP-11B retrieval as closed/approved/integrated while C10/C11 in the Claim–Evidence Matrix remain prohibited and still use pending-retrieval evidence wording.

`EXP11B_EDITORIAL_GOVERNANCE_LAG = PRESENT / NONBLOCKING_FOR_0C_CURRENT_SCOPE`.

The direction of H150/H200 is not used to support the 0C gap, contribution B, or candidate RQs. Any later article use of EXP-11B requires explicit editorial reconciliation of C10/C11 against governing experimental evidence.

### Current gate

```text
PHASE_0B = CLOSED / APPROVED
0C_ENTRY_GATE = PASS / OPENED
0C = INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING
0C_INTERNAL_REVIEW = PASS
NEXT_ACTOR = AUTHOR
0C_PROVISIONAL_CENTRAL_CONTRIBUTION = B_ARCHITECTURAL_METHODOLOGICAL
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
AUTHOR_APPROVAL = PENDING
FREEZE_0C = NOT_AUTHORIZED_YET
0D = BLOCKED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
```

Until formal 0C freeze, the workflow may not declare final novelty, convert the bounded gap candidate into universal absence, treat architectural difference alone as novelty, restore broad F5, use EXP-11B claims before C10/C11 reconciliation, inferentially close HE2/HE5 prematurely, equate auditability with legal correctness, select a journal, open 0D, or draft manuscript sections.