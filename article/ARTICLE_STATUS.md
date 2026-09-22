# Estado del artículo / Article Status

## Español

### Estado general

```text
WORKING_BRANCH = article/main-manuscript
TARGET_A = Knowledge-Based Systems
ARTICLE_TYPE_OPERATIVE = Research article
ARTICLE_WRITING_PLAN = V3.0
LATEST_EDITORIAL_DECISION = D-041
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
RELATED_WORK = CLOSED / APPROVED / FROZEN / INTEGRATED
INTRODUCTION_B01 = CLOSED / APPROVED / FROZEN / INTEGRATED
ARCHITECTURE_B01 = CLOSED / APPROVED / FROZEN / INTEGRATED
ARCHITECTURE_B02 = CLOSED / APPROVED / FROZEN / INTEGRATED
ARCHITECTURE_SECTIONS_3_1_TO_3_7 = CLOSED / APPROVED / FROZEN / INTEGRATED
CANONICAL_MASTER = ARTICLE_MASTER_V009
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V009.md
CANONICAL_MASTER_MD_SHA256 = ddbab5614856caf428aad0a7ee3f753288d600a6367908894184d3f72c98ab28
CANONICAL_MASTER_MD_GIT_BLOB = 40f20437458715c615fc1762f025ebcdbb3b6fc2
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_ARCH_B02_V01.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = 09a319b8e658d3888c75087d1f7db354ef686c449ad6ffd205ea86fbc9352657
CANONICAL_CITATION_COMMENTS = 40
CURRENT_DRAFTING_PHASE = EXPERIMENTAL DESIGN
CURRENT_GATE = EXPERIMENTAL_DESIGN_B01
AUTHORIZED_SCOPE = SECTION_4_1_AND_4_2_1_TO_4_2_4_ONLY
EXPERIMENTAL_DESIGN_B01 = AUTHORIZED / ACTIVE
SECTION_4_3_AND_LATER = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### Decisiones de control vigentes

- D-021: el DOCX acumulativo aprobado permanece bajo custodia local exacta del autor y se identifica por SHA-256.
- D-022: prompts y respuestas operativas sustantivas de la IA de Redacción se versionan en GitHub; el chat conserva solo el puntero mínimo.
- D-023: los cierres técnicos no reabren revisión científica y no usan mecanismos redundantes de transferencia.
- D-027: la custodia local exige entrega efectiva del binario exacto al autor.
- D-034: Architecture y Experimental Design pueden redactarse bajo gates editoriales propios sin que Group 6 bloquee por sí mismo esos bloques.
- D-035: handoff timeout-safe para artefactos acumulativos grandes; no Base64 manual, fragmentación/chunking, recomposición ni reintentos de la vía grande que ya falló.
- D-037: Architecture B01 integrada y V008 promovido.
- D-038: Architecture B02 abierta.
- D-039: Architecture B02 aprobada por el autor y V009 autorizado.
- D-040: Architecture B02 integrada; Section 3 cerrada; `ARTICLE_MASTER_V009` promovido a master canónico.
- D-041: Experimental Design B01 abierto para 4.1 y 4.2.1–4.2.4 exclusivamente.

La codificación interna automática de una API/conector no constituye Base64 manual.

### Secciones cerradas

- Related Work 2.1–2.6: `CLOSED / APPROVED / FROZEN / INTEGRATED`.
- Introduction B01: `CLOSED / APPROVED / FROZEN / INTEGRATED`.
- Decision-support architecture 3.1–3.7: `CLOSED / APPROVED / FROZEN / INTEGRATED`.

El master canónico es `ARTICLE_MASTER_V009.md`. El DOCX canónico correspondiente es `ARTICLE_MASTER_CANDIDATE_ARCH_B02_V01.docx`, bajo custodia local efectiva del autor, SHA-256 `09a319b8e658d3888c75087d1f7db354ef686c449ad6ffd205ea86fbc9352657`, con 40 comentarios heredados y 0 tracked changes en la auditoría aprobada.

### Arquitectura científica congelada

```text
commercial description
→ normalization
→ historical retrieval
→ historical Top-k ranking
→ fixed Top-3
→ candidate-specific documentary/normative evidence retrieval
→ evidence-context construction
→ local LLM
→ controlled explanation of the fixed Top-3
```

La recuperación histórica genera y ordena candidatos. El Top-3 se fija antes de etapas downstream. La recuperación documental/normativa asocia evidencia sin insertar, eliminar, sustituir ni reordenar candidatos. El LLM local explica el Top-3 fijo y no clasifica desde cero ni retroalimenta el ranking. El reranking LLM permanece diagnóstico y fuera del flujo principal.

### Fronteras científicas obligatorias

- `LITERATURE_GAP ≠ PROJECT_FEATURE ≠ SCIENTIFIC_CONTRIBUTION ≠ EXPERIMENTAL_RESULT ≠ NOVELTY_CLAIM`.
- `ABSENCE_WITHIN_SEARCH_SCOPE ≠ UNIVERSAL_ABSENCE`.
- `ARCHITECTURAL_DIFFERENCE ≠ NOVELTY_BY_ITSELF`.
- `CANDIDATE_RETRIEVAL ≠ OVERALL_CLASSIFICATION_ACCURACY`.
- `NORMATIVE_ASSOCIATION ≠ SUBSTANTIVE_NORMATIVE_CORRECTNESS`.
- `AUDITABILITY ≠ LEGAL_CORRECTNESS`.
- `CONFIGURABILITY ≠ EMPIRICAL_GENERALIZATION`.
- `EXP11A_SIZE_COMPOSITION_SENSITIVITY ≠ ISOLATED_CAUSAL_SIZE_EFFECT`.
- `EXP11B_DESCRIPTIVE ≠ SEED_SUPERPOPULATION_INFERENCE`.
- `EXP12_DIVERSITY_EFFECT = NOT_ESTIMABLE`.
- `FINAL_GAP = NOT_DEFINED`.
- `NOVELTY = NOT_DECLARED`.

### Dependencia experimental externa verificada

```text
SRC03_BRANCH = docs/plan-maestro-temporal-2026-08-31
SRC03_HEAD = b74b96d0163807007e4579d86450dd235125b30f
SRC03_BLOB = 7b63fdb14b75eace173ac3c94775d39ed7ed7a57
DEVELOPMENT_MAIN = b6404ca85c8cd0b18a6b318bae1236d2ef021f4a
```

`SRC-03` se consulta en modo de solo lectura. Su estado actual no bloquea Experimental Design B01.

### Bloque activo — Experimental Design B01

Alcance exclusivo:

- 4.1 Evaluation setting;
- 4.2 Historical data;
- 4.2.1 Data source and selection;
- 4.2.2 Target class space;
- 4.2.3 Preparation and curation;
- 4.2.4 Versioned datasets used in the experiment.

B01 debe describir la instanciación empírica concreta: piloto offline no vinculante en NANDINA Chapter 87, SERIE como unidad de análisis, DAM/declaración como unidad de agrupamiento cuando corresponda, procedencia/selección de los datos históricos, espacio de códigos representado, preparación/curación y las identidades versionadas H100/DEV/EVAL. No debe introducir resultados de retrieval, hipótesis, HE2/HE5 ni EXP11/EXP12.

La trazabilidad forense debe distinguir equivalencia funcional del contenido procesado de identidad binaria del workbook histórico original. El detalle de dependencia, leakage, duplicados y near-duplicates se reserva principalmente para 4.4.

### Gate vigente

```text
CURRENT_GATE = EXPERIMENTAL_DESIGN_B01
NEXT_ACTOR = DRAFTING_AI
NEXT_ACTION = EXECUTE_EXPERIMENTAL_DESIGN_B01_ONLY
BASELINE_MASTER_MD = article/manuscript/ARTICLE_MASTER_V009.md
BASELINE_MASTER_MD_GIT_BLOB = 40f20437458715c615fc1762f025ebcdbb3b6fc2
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_ARCH_B02_V01.docx
BASELINE_DOCX_SHA256 = 09a319b8e658d3888c75087d1f7db354ef686c449ad6ffd205ea86fbc9352657
PRIOR_CITATION_COMMENTS = 40 / PRESERVE_EXACTLY
SECTION_4_3_AND_LATER = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

---

## English

### General state

```text
WORKING_BRANCH = article/main-manuscript
TARGET_A = Knowledge-Based Systems
ARTICLE_TYPE_OPERATIVE = Research article
ARTICLE_WRITING_PLAN = V3.0
LATEST_EDITORIAL_DECISION = D-041
RELATED_WORK = CLOSED / APPROVED / FROZEN / INTEGRATED
INTRODUCTION_B01 = CLOSED / APPROVED / FROZEN / INTEGRATED
ARCHITECTURE_SECTIONS_3_1_TO_3_7 = CLOSED / APPROVED / FROZEN / INTEGRATED
CANONICAL_MASTER = ARTICLE_MASTER_V009
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V009.md
CANONICAL_MASTER_MD_SHA256 = ddbab5614856caf428aad0a7ee3f753288d600a6367908894184d3f72c98ab28
CANONICAL_MASTER_MD_GIT_BLOB = 40f20437458715c615fc1762f025ebcdbb3b6fc2
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_ARCH_B02_V01.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = 09a319b8e658d3888c75087d1f7db354ef686c449ad6ffd205ea86fbc9352657
CANONICAL_CITATION_COMMENTS = 40
CURRENT_DRAFTING_PHASE = EXPERIMENTAL DESIGN
CURRENT_GATE = EXPERIMENTAL_DESIGN_B01
AUTHORIZED_SCOPE = SECTION_4_1_AND_4_2_1_TO_4_2_4_ONLY
EXPERIMENTAL_DESIGN_B01 = AUTHORIZED / ACTIVE
SECTION_4_3_AND_LATER = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

D-040 closes and integrates Architecture B02 and promotes `ARTICLE_MASTER_V009` as canonical. D-041 opens the first Experimental-Design block. D-021/D-027 preserve exact local DOCX custody; D-022 keeps substantive Drafting-AI prompts/responses in GitHub; D-023 prevents redundant technical re-review; D-035 governs timeout-safe transfer of large cumulative artifacts.

The frozen architecture remains historical ranking → fixed Top-3 → candidate-specific documentary evidence → traceable context → local LLM controlled explanation, with no downstream authority to alter candidate membership/order.

The active block covers only Sections 4.1 and 4.2.1–4.2.4. It establishes the offline non-binding Chapter-87 evaluation setting, SERIE/DAM units, historical-data provenance and selection, the represented target-code space, preparation/curation, and the frozen H100/DEV/EVAL identities. Performance results and later Experimental-Design subsections remain closed.

Current external snapshot: `SRC-03@b74b96d0163807007e4579d86450dd235125b30f`, blob `7b63fdb14b75eace173ac3c94775d39ed7ed7a57`; development `main@b6404ca85c8cd0b18a6b318bae1236d2ef021f4a`. This dependency does not block B01.

### Current gate

```text
CURRENT_GATE = EXPERIMENTAL_DESIGN_B01
NEXT_ACTOR = DRAFTING_AI
NEXT_ACTION = EXECUTE_EXPERIMENTAL_DESIGN_B01_ONLY
BASELINE_MASTER_MD = article/manuscript/ARTICLE_MASTER_V009.md
BASELINE_MASTER_MD_GIT_BLOB = 40f20437458715c615fc1762f025ebcdbb3b6fc2
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_ARCH_B02_V01.docx
BASELINE_DOCX_SHA256 = 09a319b8e658d3888c75087d1f7db354ef686c449ad6ffd205ea86fbc9352657
PRIOR_CITATION_COMMENTS = 40 / PRESERVE_EXACTLY
SECTION_4_3_AND_LATER = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```
