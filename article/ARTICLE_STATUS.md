# Estado del artículo / Article Status

## Español

### Estado general

```text
WORKING_BRANCH = article/main-manuscript
TARGET_A = Knowledge-Based Systems
ARTICLE_TYPE_OPERATIVE = Research article
ARTICLE_WRITING_PLAN = V3.1
LATEST_EDITORIAL_DECISION = D-046
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
RELATED_WORK = CLOSED / APPROVED / FROZEN / INTEGRATED
INTRODUCTION_B01 = CLOSED / APPROVED / FROZEN / INTEGRATED
ARCHITECTURE_B01 = CLOSED / APPROVED / FROZEN / INTEGRATED
ARCHITECTURE_B02 = CLOSED / APPROVED / FROZEN / INTEGRATED
ARCHITECTURE_SECTIONS_3_1_TO_3_7 = CLOSED / APPROVED / FROZEN / INTEGRATED_WITH_TWO_EDITORIAL_FORWARD_REFERENCES_AUTHORIZED_FOR_CONTROLLED_AMENDMENT
CANONICAL_MASTER = ARTICLE_MASTER_V009
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V009.md
CANONICAL_MASTER_MD_SHA256 = ddbab5614856caf428aad0a7ee3f753288d600a6367908894184d3f72c98ab28
CANONICAL_MASTER_MD_GIT_BLOB = 40f20437458715c615fc1762f025ebcdbb3b6fc2
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_ARCH_B02_V01.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = 09a319b8e658d3888c75087d1f7db354ef686c449ad6ffd205ea86fbc9352657
CANONICAL_CITATION_COMMENTS = 40
CURRENT_DRAFTING_PHASE = EXPERIMENTAL DESIGN
CURRENT_GATE = EXPERIMENTAL_DESIGN_B01_V02_REWRITE
EXPERIMENTAL_DESIGN_B01 = REOPENED / AUTHORIZED / ACTIVE
AUTHORIZED_SCOPE = SECTION_3_FORWARD_REFERENCE_EDITORIAL_AMENDMENTS_PLUS_SECTION_4_1_AND_4_2_1_TO_4_2_3
SECTION_4_3_AND_LATER = NOT_AUTHORIZED
ARTICLE_MASTER_V010 = SUSPENDED / NOT_MATERIALIZED
PREVIOUS_B01_V02_PROSE = OBSERVED / NOT_BASELINE
PREVIOUS_KBS34_4_2_CORRECTION_PROMPT = SUPERSEDED / DO_NOT_EXECUTE
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### Decisiones de control vigentes

- D-021/D-027: custodia local exacta del DOCX acumulativo.
- D-022: prompts y respuestas operativas sustantivas de la IA de Redacción se versionan en GitHub; el chat usa puntero mínimo.
- D-023: cierre técnico minimalista; no reabrir revisión científica sin causa.
- D-034: Architecture y Experimental Design no dependen por sí mismos del cierre de Group 6.
- D-035: handoff timeout-safe para artefactos acumulativos grandes; no Base64 manual, chunking, recomposición ni reintentos de la vía fallida.
- D-040: Architecture integrada y `ARTICLE_MASTER_V009` promovido.
- D-041/D-042: primer intento de B01 abierto y luego aprobado por el autor, sin llegar a integración.
- D-043: suspensión de V010 por exceso de metadata interna en la prosa de 4.2.
- D-044: reapertura conceptual de Section 4 y superación del prompt correctivo estrecho.
- D-045: nueva estructura Section 4 aprobada por el autor y materializada como `KBS_ARTICLE_WORKING_STRUCTURE_V02.md`.
- D-046: B01 reabierto bajo Structure V02.

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

La arquitectura científica no se reabre. Las únicas modificaciones autorizadas en Section 3 son dos referencias editoriales hacia Section 4: retirar la promesa de hashes en 3.5 y evitar presentar reproducibilidad como inventario narrativo de identidades técnicas en 3.7.

### Section 4 — estructura aprobada

```text
4.1 Experimental setting and scope
4.2 Historical data and experimental dataset construction
  4.2.1 Source and data collection
  4.2.2 Processing and curation
  4.2.3 Partition construction and dataset composition
4.3 Documentary corpus and evidence resource
4.4 Partition validity and dependence controls
4.5 Experimental system configuration and execution
4.6 Evaluation framework and protocols
  4.6.1 Candidate-retrieval evaluation
  4.6.2 Documentary-evidence evaluation
  4.6.3 Controlled-explanation evaluation
4.7 Statistical and robustness analysis
4.8 Reproducibility resources
```

Regla editorial transversal: Methods explica objetos, procedimientos, decisiones, condiciones de ejecución, protocolos y controles científicos. Los SHA-256, rutas internas y nombres físicos de archivos pertenecen a manifiestos/recursos de reproducibilidad salvo necesidad metodológica excepcional.

La procedencia histórica debe comenzar por la fuente administrativa y el procedimiento real de recolección/acopio; el Excel intermedio no es la fuente científica que gobierna la narrativa. `evaluate/evaluar` es preferible a `validate/validar`. Configurabilidad/reinstanciación no equivale a generalización empírica.

### Fronteras científicas obligatorias

- `LITERATURE_GAP ≠ PROJECT_FEATURE ≠ SCIENTIFIC_CONTRIBUTION ≠ EXPERIMENTAL_RESULT ≠ NOVELTY_CLAIM`.
- `CANDIDATE_RETRIEVAL ≠ OVERALL_CLASSIFICATION_ACCURACY`.
- `NORMATIVE_ASSOCIATION ≠ SUBSTANTIVE_NORMATIVE_CORRECTNESS`.
- `AUDITABILITY ≠ LEGAL_CORRECTNESS`.
- `CONFIGURABILITY ≠ EMPIRICAL_GENERALIZATION`.
- `EXP11A_SIZE_COMPOSITION_SENSITIVITY ≠ ISOLATED_CAUSAL_SIZE_EFFECT`.
- `EXP11B_DESCRIPTIVE ≠ SEED_SUPERPOPULATION_INFERENCE`.
- `EXP12_DIVERSITY_EFFECT = NOT_ESTIMABLE`.
- `FINAL_GAP = NOT_DEFINED`.
- `NOVELTY = NOT_DECLARED`.

### Dependencia experimental externa

`SRC-03` sigue siendo fuente viva en modo de solo lectura. El último snapshot editorial registrado es HEAD `b74b96d0163807007e4579d86450dd235125b30f`, blob `7b63fdb14b75eace173ac3c94775d39ed7ed7a57`, desarrollo `main@b6404ca85c8cd0b18a6b318bae1236d2ef021f4a`. La IA de Redacción debe comprobar si existe cambio material al ejecutar B01.

### Gate vigente

```text
CURRENT_GATE = EXPERIMENTAL_DESIGN_B01_V02_REWRITE
NEXT_ACTOR = DRAFTING_AI
NEXT_ACTION = EXECUTE_ONLY_NEW_B01_PROMPT_UNDER_STRUCTURE_V02
BASELINE_MASTER_MD = article/manuscript/ARTICLE_MASTER_V009.md
BASELINE_MASTER_MD_GIT_BLOB = 40f20437458715c615fc1762f025ebcdbb3b6fc2
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_ARCH_B02_V01.docx
BASELINE_DOCX_SHA256 = 09a319b8e658d3888c75087d1f7db354ef686c449ad6ffd205ea86fbc9352657
PREVIOUS_OBSERVED_B01_V02 = NOT_BASELINE
SECTION_4_3_AND_LATER = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

---

## English

```text
WORKING_BRANCH = article/main-manuscript
TARGET_A = Knowledge-Based Systems
ARTICLE_TYPE_OPERATIVE = Research article
ARTICLE_WRITING_PLAN = V3.1
LATEST_EDITORIAL_DECISION = D-046
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
CANONICAL_MASTER = ARTICLE_MASTER_V009
CURRENT_GATE = EXPERIMENTAL_DESIGN_B01_V02_REWRITE
EXPERIMENTAL_DESIGN_B01 = REOPENED / AUTHORIZED / ACTIVE
AUTHORIZED_SCOPE = SECTION_3_FORWARD_REFERENCE_EDITORIAL_AMENDMENTS_PLUS_SECTION_4_1_AND_4_2_1_TO_4_2_3
SECTION_4_3_AND_LATER = NOT_AUTHORIZED
ARTICLE_MASTER_V010 = SUSPENDED / NOT_MATERIALIZED
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

The author approved the controlled Section-4 restructuring as Structure V02. B01 is reopened from canonical V009, not from the previously observed B01 prose. Section 4 now follows experimental setting/scope → historical-data construction → documentary corpus → partition validity → concrete system configuration/execution → evaluation framework/protocols → statistical/robustness analysis → reproducibility resources.

Publication-facing Methods must prioritize scientific provenance, acquisition, processing, design decisions, execution, evaluation, and validity controls rather than internal artifact identities. Only two editorial forward-reference amendments are authorized in the otherwise frozen Section 3. Section 4.3 and later remain closed until B01 passes its gates.