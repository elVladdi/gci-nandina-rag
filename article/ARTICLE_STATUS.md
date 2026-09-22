# Estado del artículo / Article Status

## Español

### Estado general

```text
WORKING_BRANCH = article/main-manuscript
TARGET_A = Knowledge-Based Systems
ARTICLE_TYPE_OPERATIVE = Research article
ARTICLE_WRITING_PLAN = V2.9
LATEST_EDITORIAL_DECISION = D-039
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
RELATED_WORK = CLOSED / APPROVED / FROZEN / INTEGRATED
INTRODUCTION_B01 = CLOSED / APPROVED / FROZEN / INTEGRATED
ARCHITECTURE_B01 = CLOSED / APPROVED / FROZEN / INTEGRATED
ARCHITECTURE_B02 = AUTHOR_APPROVED / SCIENTIFICALLY_CLOSED / INTEGRATION_PENDING
ARCHITECTURE_SECTIONS_3_1_TO_3_7 = AUTHOR_APPROVED / SCIENTIFICALLY_CLOSED
CANONICAL_MASTER = ARTICLE_MASTER_V008
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V008.md
CANONICAL_MASTER_MD_SHA256 = 895e45a4e0af6b72e8a0a1ff0ab53c7953d34f503429accf57df08367f32b99d
CANONICAL_MASTER_MD_GIT_BLOB = 0145d13e1bc4e4fdeab79f7bad83d00f67221a76
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_ARCH_B01_V02.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = f493c068645f253af757716a2dd2ae560bdfeb59cbffd4f5fac8bb566d79fea4
APPROVED_NEXT_MASTER_MD = ARTICLE_MASTER_CANDIDATE_ARCH_B02_V01.md
APPROVED_NEXT_MASTER_MD_SHA256 = ddbab5614856caf428aad0a7ee3f753288d600a6367908894184d3f72c98ab28
EXPECTED_ARTICLE_MASTER_V009_GIT_BLOB = 40f20437458715c615fc1762f025ebcdbb3b6fc2
APPROVED_NEXT_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_ARCH_B02_V01.docx / LOCAL_AUTHOR_CUSTODY
APPROVED_NEXT_MASTER_DOCX_SHA256 = 09a319b8e658d3888c75087d1f7db354ef686c449ad6ffd205ea86fbc9352657
CANONICAL_CITATION_COMMENTS = 40
CURRENT_DRAFTING_PHASE = DECISION SUPPORT ARCHITECTURE / TECHNICAL CLOSURE
CURRENT_GATE = ARCHITECTURE_B02_INTEGRATION
NEXT_ACTION = MATERIALIZE_AND_VERIFY_ARTICLE_MASTER_V009
ARTICLE_MASTER_V009 = AUTHORIZED / PENDING_MATERIALIZATION
EXPERIMENTAL_DESIGN = ELIGIBLE_AFTER_V009_INTEGRATION / NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### Decisiones de control vigentes

- D-021: política de custodia local del DOCX acumulativo.
- D-022: prompts y respuestas operativas sustantivas se versionan en GitHub.
- D-023: cierres técnicos mínimos; evitar mecanismos redundantes que reproduzcan timeouts.
- D-027: la custodia local exige entrega efectiva del binario exacto al autor.
- D-033: Introduction integrada y V007 promovido.
- D-034: Architecture y Experimental design pueden redactarse bajo sus propios gates sin que Group 6 bloquee por sí mismo esos bloques.
- D-035: handoff timeout-safe; no Base64 manual, fragmentación/chunking ni reintentos de transferencias grandes por una vía que ya falló.
- D-036: aprobación autoral de Architecture B01.
- D-037: Architecture B01 integrada y `ARTICLE_MASTER_V008` promovido a canónico.
- D-038: Architecture B02 abierta para Sections 3.5–3.7.
- D-039: Architecture B02 aprobada por el autor; integración y promoción de V009 autorizadas.

La codificación interna utilizada automáticamente por una API o conector no está prohibida por D-035. La restricción se refiere a Base64 manual, fragmentación, recomposición o reintentos como workaround.

### Secciones cerradas o aprobadas

- Related Work 2.1–2.6: `CLOSED / APPROVED / FROZEN / INTEGRATED`.
- Introduction B01: `CLOSED / APPROVED / FROZEN / INTEGRATED`.
- Architecture B01, Sections 3.1–3.4: `CLOSED / APPROVED / FROZEN / INTEGRATED`.
- Architecture B02, Sections 3.5–3.7: `AUTHOR_APPROVED / SCIENTIFICALLY_CLOSED / INTEGRATION_PENDING`.

El master canónico sigue siendo `ARTICLE_MASTER_V008.md` hasta que el Markdown aprobado de B02 sea materializado y verificado como `ARTICLE_MASTER_V009.md`. El DOCX B02 aprobado está bajo custodia local efectiva del autor con SHA-256 `09a319b8e658d3888c75087d1f7db354ef686c449ad6ffd205ea86fbc9352657`, 40 comentarios y 0 tracked changes en el control aprobado.

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
- la arquitectura puede reinstanciarse con otro banco histórico etiquetado, espacio de clases objetivo o corpus documental compatible si se preservan interfaces y trazabilidad;
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

### Gate vigente

```text
CURRENT_GATE = ARCHITECTURE_B02_INTEGRATION
NEXT_ACTOR = IA_GESTORA
NEXT_ACTION = MATERIALIZE_AND_VERIFY_ARTICLE_MASTER_V009
EXPECTED_V009_SHA256 = ddbab5614856caf428aad0a7ee3f753288d600a6367908894184d3f72c98ab28
EXPECTED_V009_GIT_BLOB = 40f20437458715c615fc1762f025ebcdbb3b6fc2
ARCHITECTURE_B02 = AUTHOR_APPROVED
EXPERIMENTAL_DESIGN = NOT_AUTHORIZED_UNTIL_V009_INTEGRATED
```

La IA Gestora debe continuar automáticamente al primer gate de Experimental Design una vez verificada la materialización de V009. No se requiere una nueva aprobación autoral para ejecutar ese cierre técnico.

---

## English

### General state

```text
WORKING_BRANCH = article/main-manuscript
TARGET_A = Knowledge-Based Systems
ARTICLE_TYPE_OPERATIVE = Research article
ARTICLE_WRITING_PLAN = V2.9
LATEST_EDITORIAL_DECISION = D-039
RELATED_WORK = CLOSED / APPROVED / FROZEN / INTEGRATED
INTRODUCTION_B01 = CLOSED / APPROVED / FROZEN / INTEGRATED
ARCHITECTURE_B01 = CLOSED / APPROVED / FROZEN / INTEGRATED
ARCHITECTURE_B02 = AUTHOR_APPROVED / SCIENTIFICALLY_CLOSED / INTEGRATION_PENDING
CANONICAL_MASTER = ARTICLE_MASTER_V008
APPROVED_NEXT_MASTER_MD_SHA256 = ddbab5614856caf428aad0a7ee3f753288d600a6367908894184d3f72c98ab28
EXPECTED_ARTICLE_MASTER_V009_GIT_BLOB = 40f20437458715c615fc1762f025ebcdbb3b6fc2
APPROVED_NEXT_MASTER_DOCX_SHA256 = 09a319b8e658d3888c75087d1f7db354ef686c449ad6ffd205ea86fbc9352657
CURRENT_GATE = ARCHITECTURE_B02_INTEGRATION
ARTICLE_MASTER_V009 = AUTHORIZED / PENDING_MATERIALIZATION
EXPERIMENTAL_DESIGN = ELIGIBLE_AFTER_V009_INTEGRATION / NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

Architecture B02 has passed independent review and has been explicitly approved by the author under D-039. Sections 3.1–3.7 are scientifically closed. The current canonical GitHub master remains V008 only until the exact approved B02 cumulative Markdown is materialized and verified as `ARTICLE_MASTER_V009.md`.

D-035 remains binding: no manual Base64, fragmentation/chunking, recomposition, or repeated use of a large-transfer path already known to timeout. Automatic internal encoding used by an API/connector is permitted.

The approved B02 DOCX is in effective local author custody with SHA-256 `09a319b8e658d3888c75087d1f7db354ef686c449ad6ffd205ea86fbc9352657`, 40 comments, and 0 tracked changes at the approved audit.

### Current gate

```text
CURRENT_GATE = ARCHITECTURE_B02_INTEGRATION
NEXT_ACTOR = MANAGING_AI
NEXT_ACTION = MATERIALIZE_AND_VERIFY_ARTICLE_MASTER_V009
EXPECTED_V009_SHA256 = ddbab5614856caf428aad0a7ee3f753288d600a6367908894184d3f72c98ab28
EXPECTED_V009_GIT_BLOB = 40f20437458715c615fc1762f025ebcdbb3b6fc2
EXPERIMENTAL_DESIGN = NOT_AUTHORIZED_UNTIL_V009_INTEGRATED
```

Once V009 is verified, the Managing AI must proceed automatically to the first eligible Experimental Design gate without asking the author for a redundant continuation instruction.
