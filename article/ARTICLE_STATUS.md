# Estado del artículo / Article Status

## Español

### Estado general

```text
WORKING_BRANCH = article/main-manuscript
TARGET_A = Knowledge-Based Systems
ARTICLE_TYPE_OPERATIVE = Research article
ARTICLE_WRITING_PLAN = V2.9
LATEST_EDITORIAL_DECISION = D-038
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
RELATED_WORK = CLOSED / APPROVED / FROZEN / INTEGRATED
INTRODUCTION_B01 = CLOSED / APPROVED / FROZEN / INTEGRATED
ARCHITECTURE_B01 = CLOSED / APPROVED / FROZEN / INTEGRATED
CANONICAL_MASTER = ARTICLE_MASTER_V008
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V008.md
CANONICAL_MASTER_MD_SHA256 = 895e45a4e0af6b72e8a0a1ff0ab53c7953d34f503429accf57df08367f32b99d
CANONICAL_MASTER_MD_GIT_BLOB = 0145d13e1bc4e4fdeab79f7bad83d00f67221a76
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_ARCH_B01_V02.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = f493c068645f253af757716a2dd2ae560bdfeb59cbffd4f5fac8bb566d79fea4
CANONICAL_CITATION_COMMENTS = 40
CURRENT_DRAFTING_PHASE = DECISION SUPPORT ARCHITECTURE
CURRENT_GATE = ARCHITECTURE_B02
AUTHORIZED_SCOPE = SECTIONS_3_5_TO_3_7_ONLY
ARCHITECTURE_B02 = AUTHORIZED / ACTIVE
EXPERIMENTAL_DESIGN = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
ARTICLE_MASTER_V009 = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### Decisiones de control vigentes

- D-021: política de custodia local del DOCX acumulativo.
- D-022: prompts y respuestas operativas sustantivas se versionan en GitHub.
- D-023: cierres técnicos mínimos; evitar mecanismos redundantes que reproduzcan timeouts.
- D-027: la custodia local exige entrega efectiva del binario exacto al autor.
- D-033: Introduction integrada y V007 promovido.
- D-034: reconciliación editorial con la secuencia experimental G6/G7; Architecture y Experimental design pueden redactarse bajo sus propios gates.
- D-035: handoff timeout-safe; no Base64 manual, fragmentación/chunking ni reintentos de transferencias grandes por una vía que ya falló.
- D-036: aprobación autoral de Architecture B01.
- D-037: Architecture B01 integrada y `ARTICLE_MASTER_V008` promovido a canónico.
- D-038: Architecture B02 abierta y autorizada para Sections 3.5–3.7 únicamente.

La codificación interna utilizada automáticamente por una API o conector no está prohibida por D-035. La prohibición se refiere al uso manual de Base64, fragmentación o recomposición como workaround de transferencia.

### Secciones cerradas

- Related Work 2.1–2.6: `CLOSED / APPROVED / FROZEN / INTEGRATED`.
- Introduction B01: `CLOSED / APPROVED / FROZEN / INTEGRATED`.
- Architecture B01, Sections 3.1–3.4: `CLOSED / APPROVED / FROZEN / INTEGRATED`.

El master canónico es `ARTICLE_MASTER_V008.md`. El DOCX canónico correspondiente permanece bajo custodia local efectiva del autor con SHA-256 `f493c068645f253af757716a2dd2ae560bdfeb59cbffd4f5fac8bb566d79fea4`, 40 comentarios heredados y 0 tracked changes en el último control.

### Arquitectura científica obligatoria

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

Reglas vinculantes:

- la recuperación histórica genera y ordena candidatos;
- el Top-3 se fija antes de cualquier etapa documental o generativa downstream;
- la recuperación documental/normativa asocia evidencia con candidatos ya fijados y no puede insertar, eliminar, sustituir ni reordenar candidatos;
- el LLM local explica el Top-3 fijo y no clasifica desde cero ni retroalimenta el ranking;
- el reranking LLM es diagnóstico y permanece fuera del flujo principal;
- el corpus documental concreto del experimento se describe en Experimental design, no define universalmente la arquitectura;
- la arquitectura puede reinstanciarse con otro banco histórico etiquetado, espacio de clases objetivo o corpus documental compatible si se preservan los contratos de interfaz y trazabilidad;
- configurabilidad/reinstanciación no implica transferencia de desempeño ni generalización empírica.

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

### Bloque activo — Architecture B02

Architecture B02 comprende exclusivamente:

1. `3.5 Candidate-specific documentary retrieval`;
2. `3.6 Evidence-context construction and controlled explanation`;
3. `3.7 Configurability and interface requirements`.

Función narrativa:

`fixed Top-3 → documentary evidence per candidate → traceable context → controlled local-LLM explanation → configurable interfaces`

B02 debe dejar explícito qué corpus alimenta la evidencia/contexto de explicación a nivel arquitectónico y qué función cumple el repositorio de reproducibilidad, sin anticipar el inventario experimental concreto de Section 4.

No puede modificar 3.1–3.4, Introduction o Related Work, ni abrir Experimental design.

### Claims relevantes

Autorizados para B02:

- C02: la recuperación normativa/documental aporta evidencia y no reemplaza el ranking histórico;
- C03: el LLM local explica un Top-3 previamente recuperado y no clasifica desde cero;
- C15: configurabilidad como propiedad de diseño, no generalización empírica;
- C17: separación entre reproducción del estudio y replicación externa con datos independientes.

Prohibidos/restringidos:

- C12: asociación normativa no demuestra corrección sustantiva;
- C13: explicaciones no demuestran corrección jurídica completa;
- C16: no se ha demostrado generalización empírica fuera del setting evaluado;
- C18: no se producen clasificaciones jurídicamente vinculantes.

### Dependencia experimental externa

La IA Gestora no administra el Plan Maestro experimental. Para hechos experimentales debe consultarse `SRC-03` en modo de solo lectura. El último HEAD externo verificado durante la apertura de B02 fue:

`docs/plan-maestro-temporal-2026-08-31@b74b96d0163807007e4579d86450dd235125b30f`

Ese estado no bloquea Architecture B02 y no autoriza por sí mismo ningún bloque editorial posterior.

### Gate vigente

```text
CURRENT_GATE = ARCHITECTURE_B02
NEXT_ACTOR = DRAFTING_AI
NEXT_ACTION = EXECUTE_ARCHITECTURE_B02_ONLY
BASELINE_MASTER = ARTICLE_MASTER_V008
ARCHITECTURE_B02 = AUTHORIZED
EXPERIMENTAL_DESIGN = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
```

---

## English

### General state

```text
WORKING_BRANCH = article/main-manuscript
TARGET_A = Knowledge-Based Systems
ARTICLE_TYPE_OPERATIVE = Research article
ARTICLE_WRITING_PLAN = V2.9
LATEST_EDITORIAL_DECISION = D-038
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
RELATED_WORK = CLOSED / APPROVED / FROZEN / INTEGRATED
INTRODUCTION_B01 = CLOSED / APPROVED / FROZEN / INTEGRATED
ARCHITECTURE_B01 = CLOSED / APPROVED / FROZEN / INTEGRATED
CANONICAL_MASTER = ARTICLE_MASTER_V008
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V008.md
CANONICAL_MASTER_MD_SHA256 = 895e45a4e0af6b72e8a0a1ff0ab53c7953d34f503429accf57df08367f32b99d
CANONICAL_MASTER_MD_GIT_BLOB = 0145d13e1bc4e4fdeab79f7bad83d00f67221a76
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_ARCH_B01_V02.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = f493c068645f253af757716a2dd2ae560bdfeb59cbffd4f5fac8bb566d79fea4
CANONICAL_CITATION_COMMENTS = 40
CURRENT_DRAFTING_PHASE = DECISION SUPPORT ARCHITECTURE
CURRENT_GATE = ARCHITECTURE_B02
AUTHORIZED_SCOPE = SECTIONS_3_5_TO_3_7_ONLY
ARCHITECTURE_B02 = AUTHORIZED / ACTIVE
EXPERIMENTAL_DESIGN = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
ARTICLE_MASTER_V009 = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### Active control decisions

D-021 governs local cumulative-DOCX custody; D-022 governs versioned operational prompts/responses; D-023 requires minimal technical closure; D-027 requires effective handoff of the exact binary to the author; D-034 reconciles article drafting with the external experimental sequence; D-035 establishes timeout-safe artifact handoff; D-036 records author approval of Architecture B01; D-037 integrates Architecture B01 and promotes `ARTICLE_MASTER_V008`; D-038 opens Architecture B02.

Internal API/connector encoding is not prohibited by D-035. The prohibition concerns manual Base64, fragmentation/chunking, recomposition, or repeated large transfers used as workarounds after a timeout.

### Closed sections

Related Work 2.1–2.6, Introduction B01, and Architecture B01 Sections 3.1–3.4 are `CLOSED / APPROVED / FROZEN / INTEGRATED`.

The canonical master is `ARTICLE_MASTER_V008.md`. The corresponding DOCX remains in effective local author custody with SHA-256 `f493c068645f253af757716a2dd2ae560bdfeb59cbffd4f5fac8bb566d79fea4`, 40 inherited comments, and 0 tracked changes at the latest control.

### Mandatory scientific architecture

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

Historical retrieval generates and ranks candidates. The Top-3 is fixed before downstream documentary or generative processing. Documentary/normative retrieval associates evidence with already fixed candidates and cannot insert, delete, substitute, or reorder them. The local LLM explains the fixed Top-3 and cannot classify from scratch or feed information back into ranking. LLM reranking remains diagnostic and outside the primary flow.

A new instantiation may replace the labeled historical bank, target class space, or compatible documentary corpus if the required interfaces and traceability contracts are preserved. Configurability/re-instantiation is not evidence of empirical performance transfer or generalization.

### Mandatory scientific boundaries

`LITERATURE_GAP ≠ PROJECT_FEATURE ≠ SCIENTIFIC_CONTRIBUTION ≠ EXPERIMENTAL_RESULT ≠ NOVELTY_CLAIM`; `ABSENCE_WITHIN_SEARCH_SCOPE ≠ UNIVERSAL_ABSENCE`; `ARCHITECTURAL_DIFFERENCE ≠ NOVELTY_BY_ITSELF`; `CANDIDATE_RETRIEVAL ≠ OVERALL_CLASSIFICATION_ACCURACY`; `NORMATIVE_ASSOCIATION ≠ SUBSTANTIVE_NORMATIVE_CORRECTNESS`; `AUDITABILITY ≠ LEGAL_CORRECTNESS`; `CONFIGURABILITY ≠ EMPIRICAL_GENERALIZATION`; `EXP11A_SIZE_COMPOSITION_SENSITIVITY ≠ ISOLATED_CAUSAL_SIZE_EFFECT`; `EXP11B_DESCRIPTIVE ≠ SEED_SUPERPOPULATION_INFERENCE`; `EXP12_DIVERSITY_EFFECT = NOT_ESTIMABLE`. `FINAL_GAP = NOT_DEFINED` and `NOVELTY = NOT_DECLARED` remain binding.

### Active block — Architecture B02

Architecture B02 exclusively covers Sections 3.5–3.7: candidate-specific documentary retrieval; evidence-context construction and controlled explanation; and configurability/interface requirements.

Its narrative function is:

`fixed Top-3 → documentary evidence per candidate → traceable context → controlled local-LLM explanation → configurable interfaces`.

B02 must make explicit, at architecture level, which documentary corpus feeds the evidence/context for explanation and the role of the reproducibility repository, while deferring the concrete experimental corpus, parameters, hashes, and artifact inventory to Section 4.

Introduction, Related Work, and Sections 3.1–3.4 are frozen. Experimental design remains unauthorized.

### Relevant claims

Authorized: C02, C03, C15, C17. Prohibited/restricted: C12, C13, C16, C18.

### External experimental dependency

The Managing AI does not manage the experimental Master Plan. Experimental facts must be read from `SRC-03`. The latest external HEAD verified when B02 was opened was `docs/plan-maestro-temporal-2026-08-31@b74b96d0163807007e4579d86450dd235125b30f`. It does not block B02 and does not itself authorize later editorial blocks.

### Current gate

```text
CURRENT_GATE = ARCHITECTURE_B02
NEXT_ACTOR = DRAFTING_AI
NEXT_ACTION = EXECUTE_ARCHITECTURE_B02_ONLY
BASELINE_MASTER = ARTICLE_MASTER_V008
ARCHITECTURE_B02 = AUTHORIZED
EXPERIMENTAL_DESIGN = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
```
