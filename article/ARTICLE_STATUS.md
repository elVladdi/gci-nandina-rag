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
- `0C`: **`READY_FOR_DRAFTING`**.
- `0D — Arquitectura editorial y journal fit`: **`BLOCKED`** hasta cerrar 0C.
- Target journal: `PENDING — se decidirá en Fase 0D`.
- `FINAL_GAP = NOT_DEFINED`.
- `NOVELTY = NOT_DECLARED`.
- `MANUSCRIPT_DRAFTING = NOT_AUTHORIZED`.
- `NEW_LITERATURE_SEARCH = NOT_AUTHORIZED`.
- `EXPERIMENTAL_REVIEW = NOT_REQUIRED` para la apertura de 0C.
- Corpus heredado consolidado: `62` obras/documentos con acceso primario verificable `62/62`.
- Registro de nueva literatura: `article/literature/BIBLIOGRAPHIC_ADMISSION_REGISTRY.md`.

### Gobernanza

Continúan gobernando:

- `article/ground_truth/0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md`;
- `article/ground_truth/0A02_EXPERIMENTAL_GROUND_TRUTH_FROZEN.md`;
- freezes `0B-01` a `0B-06`;
- `article/reviews/0B_PHASE_CLOSURE.md`;
- `article/reviews/0C_ENTRY_GATE.md`;
- `article/ARTICLE_WRITING_PLAN.md`;
- `article/DECISIONS.md`;
- `article/SOURCE_REGISTRY.md`;
- `article/CLAIM_EVIDENCE_MATRIX.md`;
- `article/STYLE_GUIDE.md`.

La IA Experimental conserva autoridad exclusiva sobre el Plan Maestro y decisiones experimentales. La IA Gestora / Editor Científico Principal administra estados editoriales, gates, claims y admisión bibliográfica. La IA de Redacción ejecuta únicamente prompts cerrados versionados.

### Snapshot experimental de apertura 0C

El Plan Maestro `SRC-03` fue verificado en modo solo lectura al abrir 0C:

```text
branch = docs/plan-maestro-temporal-2026-08-31
HEAD = f4d20dfe46181cb2740c4e4cd6604b0bff7a48f6
blob = adcd9be3aaa9c13929575d6f348fa6f9693bccbf
```

El snapshot coincide con el registrado durante la reconciliación final de 0B-05C. No existe cambio de fuente viva que obligue a reabrir 0A/0B. La campaña experimental global sigue abierta y Grupo 3 permanece como bloque posterior de métricas/inferencia; 0C no puede transformar resultados pendientes en hechos.

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

N01 puede considerarse posteriormente dentro de sus límites; no existe obligación de citarlo. N02 no puede usarse como evidencia determinante hasta una revisión específica.

### Alcance operativo de 0C

0C debe producir un mapa candidato de posicionamiento, no manuscrito:

1. gap empírico candidato;
2. gap metodológico candidato;
3. gap de apoyo a decisiones/auditabilidad candidato;
4. exactamente tres alternativas de contribución central;
5. Research Questions candidatas;
6. claims principales/secundarios candidatos;
7. mapeo exacto de OE/HE a `IN_PAPER`, `CONDITIONAL` o `THESIS_ONLY`;
8. riesgos, dependencias y posibles triggers de revisión experimental.

Prompt gobernante:

`article/prompts/0C_GAP_CONTRIBUTION_RESEARCH_QUESTIONS.md`.

Artefacto esperado:

`article/responses/0C_GAP_CONTRIBUTION_RESEARCH_QUESTIONS_RESPONSE_V01.md`.

### Prohibiciones vigentes

Durante 0C no está autorizado:

- declarar gap final o novelty por cuenta propia;
- usar “first”, “novel”, “unprecedented”, “no prior work” o equivalentes como conclusión;
- convertir ausencia dentro del alcance buscado en ausencia universal;
- reabrir 0B o ejecutar nueva búsqueda bibliográfica;
- modificar Plan Maestro, 0A, freezes de 0B o resultados experimentales;
- usar resultados experimentales pendientes como hechos;
- restaurar la formulación general falsada de F5;
- equiparar auditabilidad/source support/trazabilidad con legal correctness;
- seleccionar revista;
- redactar secciones del manuscrito.

### Gate vigente

```text
PHASE_0B = CLOSED / APPROVED
0C_ENTRY_GATE = PASS / OPENED
0C = READY_FOR_DRAFTING
NEXT_ACTOR = IA_DE_REDACCION
PROMPT = article/prompts/0C_GAP_CONTRIBUTION_RESEARCH_QUESTIONS.md
EXPECTED_RESPONSE = article/responses/0C_GAP_CONTRIBUTION_RESEARCH_QUESTIONS_RESPONSE_V01.md
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
0D = BLOCKED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW = NOT_REQUIRED_AT_ENTRY
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
- `0C = READY_FOR_DRAFTING`.
- 0D remains `BLOCKED` until 0C closes.
- `FINAL_GAP = NOT_DEFINED`.
- `NOVELTY = NOT_DECLARED`.
- `MANUSCRIPT_DRAFTING = NOT_AUTHORIZED`.
- `NEW_LITERATURE_SEARCH = NOT_AUTHORIZED`.
- `EXPERIMENTAL_REVIEW = NOT_REQUIRED` at 0C entry.

### Governance and experimental snapshot

Frozen 0A/0B artifacts, Phase-0B closure, the 0C entry gate, Master Writing Plan, Decisions, Source Registry, Claim–Evidence Matrix, and Style Guide govern 0C. The Experimental AI retains exclusive authority over the Master Plan and experimental decisions.

The live Master Plan was checked read-only at branch `docs/plan-maestro-temporal-2026-08-31`, HEAD `f4d20dfe46181cb2740c4e4cd6604b0bff7a48f6`, blob `adcd9be3aaa9c13929575d6f348fa6f9693bccbf`. It is unchanged from the final 0B-05C reconciliation snapshot. The broader experimental campaign remains open; pending experimental work cannot be converted into established findings during 0C.

### State transferred from 0B

F1 has only a bounded negative search result. F2 has partial prior art and survives only under strict fixed-upstream-Top-k/downstream-explanation isolation. F3 is an applicability-conditioned methodological candidate. F4 is a methodological boundary, not independent novelty. F5 has direct prior art and its broad regulatory-AI absence claim is falsified. G6 is eliminated and G7 is merged into F2.

Bibliographic admission: N01 `APPROVED_NEW`; N02 `REVIEW_REQUIRED / NOT_ADMITTED_YET`; N03/N04 `REJECT`.

### Authorized 0C scope

0C must produce a candidate positioning map rather than manuscript prose: empirical/methodological/decision-support gap candidates; exactly three central-contribution alternatives; candidate RQs; candidate claims; exact OE/HE paper-scope mapping; and explicit risks/dependencies/experimental-review triggers.

Governing prompt:

`article/prompts/0C_GAP_CONTRIBUTION_RESEARCH_QUESTIONS.md`.

Expected artifact:

`article/responses/0C_GAP_CONTRIBUTION_RESEARCH_QUESTIONS_RESPONSE_V01.md`.

### Current gate

```text
PHASE_0B = CLOSED / APPROVED
0C_ENTRY_GATE = PASS / OPENED
0C = READY_FOR_DRAFTING
NEXT_ACTOR = WRITING_AI
PROMPT = article/prompts/0C_GAP_CONTRIBUTION_RESEARCH_QUESTIONS.md
EXPECTED_RESPONSE = article/responses/0C_GAP_CONTRIBUTION_RESEARCH_QUESTIONS_RESPONSE_V01.md
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
0D = BLOCKED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW = NOT_REQUIRED_AT_ENTRY
```

0C may not self-declare final gap/novelty, reopen literature search, alter frozen experimental/editorial state, treat pending results as facts, restore broad F5, equate auditability with legal correctness, select a journal, or draft manuscript sections.