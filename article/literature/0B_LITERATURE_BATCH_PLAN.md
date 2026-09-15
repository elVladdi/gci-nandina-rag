# Plan de lotes de literatura 0B / 0B Literature Batch Plan

## Español

### 1. Estado de fase

`0B — Mapa crítico de literatura y taxonomía` queda **`CLOSED / APPROVED`**.

Bloques:

- `0B-01`: `APPROVED / FROZEN`.
- `0B-02`: `APPROVED / FROZEN`.
- `0B-03A`: `APPROVED / FROZEN`.
- `0B-03B`: `APPROVED / FROZEN`.
- `0B-04A`: `APPROVED / FROZEN`.
- `0B-04B`: `APPROVED / FROZEN`.
- `0B-05A`: `APPROVED / FROZEN`.
- `0B-05B`: `APPROVED / FROZEN`.
- `0B-05C`: `APPROVED / FROZEN`.
- `0B-06`: `APPROVED / FROZEN`.

El cierre formal está registrado en `article/reviews/0B_PHASE_CLOSURE.md`.

### 2. Reglas de cierre preservadas

Durante 0B se congelaron, entre otras, las separaciones entre clasificación, candidate retrieval, evidence retrieval, reranking, explanation, provenance, auditability y correctness; entre documentación, versionamiento, provenance, reproducibilidad y generalización; y entre evidencia documental, interpretación experta y corrección jurídica.

0B no declara por sí solo novelty ni gap final.

### 3. Resultado acumulado de candidatos para 0C

```text
F1 = NO_DIRECT_MATCH_FOUND_WITHIN_SEARCH_SCOPE
F2 = PARTIAL_PRIOR_ART_FOUND
F3 = NO_DIRECT_MATCH_FOUND_WITHIN_SEARCH_SCOPE
F4 = METHODOLOGICAL_DISTINCTION_ONLY
F5 = DIRECT_PRIOR_ART_FOUND
F5_GENERAL_REGULATORY_AI_ABSENCE_CLAIM = FALSIFIED
G6 = ELIMINATED_AS_GAP_CANDIDATE
G7 = MERGED_INTO_F2
```

Interpretación:

- F1 puede pasar a 0C únicamente como candidato estrecho; no se autoriza inferir novelty desde el resultado negativo acotado.
- F2 puede pasar a 0C únicamente bajo un contrato estricto: Top-k externo e inmutable, generador downstream exclusivamente explicativo, sin introducir/eliminar/sustituir/reordenar candidatos y sin feedback clasificatorio.
- F3 se conserva como principio/candidato metodológico condicionado a que existan observaciones correlacionadas por unidad administrativa o entidad. No reportar grouped split no prueba leakage.
- F4 se conserva solo como frontera metodológica entre desempeño predictivo/retrieval y corrección sustantiva.
- F5 no puede presentarse como ausencia general en regulatory AI; cualquier reformulación deberá ser más estrecha y contextual.

### 4. 0B-06 — cierre

Registros gobernantes:

- `article/reviews/0B06_BIBLIOGRAPHIC_NEED_ASSESSMENT.md`;
- `article/prompts/0B06_DIRECTED_NEW_LITERATURE_FALSIFICATION_SEARCH.md`;
- `article/responses/0B06_DIRECTED_NEW_LITERATURE_FALSIFICATION_SEARCH_RESPONSE_V01.md`;
- `article/reviews/0B06_INTERNAL_REVIEW.md`;
- `article/reviews/0B06_AUTHOR_APPROVAL.md`;
- `article/literature/0B06_DIRECTED_NEW_LITERATURE_FALSIFICATION_SEARCH_FROZEN.md`.

Admisión bibliográfica resultante:

```text
N01 = APPROVED_NEW
N02 = REVIEW_REQUIRED / NOT_ADMITTED_YET
N03 = REJECT
N04 = REJECT
```

Registro: `article/literature/BIBLIOGRAPHIC_ADMISSION_REGISTRY.md`.

### 5. Gate de salida de 0B

```text
PHASE_0B = CLOSED / APPROVED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
0C = NOT_STARTED
0C_ENTRY_GATE = PENDING / NOT_OPENED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
```

La siguiente acción editorial es definir y abrir explícitamente el gate de 0C. El cierre de 0B no autoriza redacción del manuscrito.

---

## English

### 1. Phase status

`0B — Critical literature map and taxonomy` is **`CLOSED / APPROVED`**. Blocks `0B-01` through `0B-06` are all `APPROVED / FROZEN`. Formal closure is recorded in `article/reviews/0B_PHASE_CLOSURE.md`.

### 2. Preserved closure rules

Phase 0B froze distinctions among classification, candidate retrieval, evidence retrieval, reranking, explanation, provenance, auditability, and correctness; among documentation, versioning, provenance, reproducibility, and generalization; and between documentary evidence, expert interpretation, and substantive correctness.

Phase 0B does not itself declare novelty or a final gap.

### 3. Cumulative candidate state for 0C

```text
F1 = NO_DIRECT_MATCH_FOUND_WITHIN_SEARCH_SCOPE
F2 = PARTIAL_PRIOR_ART_FOUND
F3 = NO_DIRECT_MATCH_FOUND_WITHIN_SEARCH_SCOPE
F4 = METHODOLOGICAL_DISTINCTION_ONLY
F5 = DIRECT_PRIOR_ART_FOUND
F5_GENERAL_REGULATORY_AI_ABSENCE_CLAIM = FALSIFIED
G6 = ELIMINATED_AS_GAP_CANDIDATE
G7 = MERGED_INTO_F2
```

F1 passes to 0C only as a narrow candidate and the bounded negative search does not establish novelty. F2 requires an externally fixed immutable Top-k and a downstream explanation-only generator with no candidate modification or classificatory feedback. F3 remains an applicability-conditioned methodological principle and missing grouped splitting does not prove leakage. F4 remains only a methodological boundary. Broad F5 cannot be claimed as an absence in regulatory AI; any later version must be narrower and contextual.

### 4. 0B-06 closure

Governing records are the 0B-06 need assessment, prompt, Writing-AI response, internal review, author approval, and frozen artifact.

Bibliographic admission state:

```text
N01 = APPROVED_NEW
N02 = REVIEW_REQUIRED / NOT_ADMITTED_YET
N03 = REJECT
N04 = REJECT
```

Registry: `article/literature/BIBLIOGRAPHIC_ADMISSION_REGISTRY.md`.

### 5. Phase-0B exit gate

```text
PHASE_0B = CLOSED / APPROVED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
0C = NOT_STARTED
0C_ENTRY_GATE = PENDING / NOT_OPENED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
```

The next editorial action is to define and explicitly open the 0C entry gate. Phase-0B closure does not authorize manuscript drafting.
