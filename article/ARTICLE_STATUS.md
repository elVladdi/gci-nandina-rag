# Estado del artículo / Article Status

## Español

### Estado general

```text
WORKING_BRANCH = article/main-manuscript
TARGET_A = Knowledge-Based Systems
ARTICLE_TYPE_OPERATIVE = Research article
ARTICLE_WRITING_PLAN = V3.1
LATEST_EDITORIAL_DECISION = D-047
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
RELATED_WORK = CLOSED / APPROVED / FROZEN / INTEGRATED
INTRODUCTION_B01 = CLOSED / APPROVED / FROZEN / INTEGRATED
ARCHITECTURE_SECTIONS_3_1_TO_3_7 = CLOSED / APPROVED / FROZEN / INTEGRATED_WITH_TWO_EDITORIAL_FORWARD_REFERENCES_CORRECTED_IN_B01_V03
CANONICAL_MASTER = ARTICLE_MASTER_V009
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V009.md
CANONICAL_MASTER_MD_SHA256 = ddbab5614856caf428aad0a7ee3f753288d600a6367908894184d3f72c98ab28
CANONICAL_MASTER_MD_GIT_BLOB = 40f20437458715c615fc1762f025ebcdbb3b6fc2
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_ARCH_B02_V01.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = 09a319b8e658d3888c75087d1f7db354ef686c449ad6ffd205ea86fbc9352657
CANONICAL_CITATION_COMMENTS = 40
CURRENT_DRAFTING_PHASE = EXPERIMENTAL DESIGN
CURRENT_GATE = EXPERIMENTAL_DESIGN_B01_AUTHOR_APPROVAL
EXPERIMENTAL_DESIGN_B01_SCIENTIFIC_CONTENT = VERIFIED / PASS
EXPERIMENTAL_DESIGN_B01 = VERIFIED / PASS / READY_FOR_AUTHOR_APPROVAL
B01_CANDIDATE_MD = ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V04.md
B01_CANDIDATE_MD_SHA256 = 0a689a47b4b17fe32aa9252a5ffeed3db955d58b917b6a04114248d14b99e6f8
B01_CANDIDATE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V04.docx
B01_CANDIDATE_DOCX_SHA256 = bfd41dcb873289b993ccdc45d1e09c835e4efa3dd1aa39fbe4de7d257c914a6d
CUMULATIVE_MASTER_STRUCTURE_V02_ALIGNMENT = PASS
STALE_SPANISH_SECTION4_PLACEHOLDER = RESOLVED
AUTHOR_APPROVAL_GATE = OPEN
SECTION_4_3_AND_LATER_SCIENTIFIC_DRAFTING = NOT_AUTHORIZED
ARTICLE_MASTER_V010 = SUSPENDED / NOT_MATERIALIZED
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### Decisiones de control vigentes

- D-021/D-027: custodia local exacta del DOCX acumulativo.
- D-022: prompts y respuestas operativas sustantivas de la IA de Redacción se versionan en GitHub; el chat usa puntero mínimo.
- D-023: no Base64 manual ni mecanismos redundantes de transferencia para cierres técnicos.
- D-034: Architecture y Experimental Design no dependen por sí mismos del cierre de Group 6.
- D-035: handoff timeout-safe para artefactos acumulativos grandes; no Base64 manual, chunking, recomposición ni reintentos de la vía fallida.
- D-040: Architecture integrada y `ARTICLE_MASTER_V009` promovido.
- D-043/D-044: V010 suspendido y Section 4 reabierta después de detectar un enfoque excesivamente orientado a artefactos/repositorio.
- D-045: Structure V02 aprobada por el autor y congelada para redacción.
- D-046: B01 reabierto desde V009 bajo Structure V02.
- D-047: autoriza únicamente la alineación mecánica del esqueleto 4.3+ con Structure V02 y la eliminación del placeholder residual español.

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

La recuperación histórica genera y ordena candidatos. El Top-3 queda fijado antes de la recuperación documental y de la generación. La etapa documental aporta evidencia sin insertar, eliminar, sustituir ni reordenar candidatos. El LLM local opera downstream para explicación controlada y no retroalimenta la clasificación.

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

Methods debe describir procedencia, adquisición, procesamiento, decisiones experimentales, condiciones de ejecución, protocolos y controles científicos. SHA-256, rutas internas, nombres físicos de archivos y demás identidad técnica exhaustiva se reservan para manifiestos/recursos de reproducibilidad salvo necesidad metodológica excepcional.

La procedencia histórica comienza en la fuente administrativa y el proceso real de recolección/acopio. El Excel intermedio no gobierna la narrativa. `evaluate/evaluar` es preferible a `validate/validar`. Configurabilidad/reinstanciación no equivale a generalización empírica.

### Auditoría de B01 V04

La auditoría independiente `article/reviews/5_EXPERIMENTAL_DESIGN_B01_V04_STRUCTURE_ALIGNMENT_INTERNAL_REVIEW_V01.md` concluye:

```text
B01_V04_DIFFERENTIAL_REVIEW = PASS
B01_SCIENTIFIC_CONTENT = VERIFIED / PASS
B01_EDITORIAL_FOCUS = VERIFIED / PASS
CUMULATIVE_MASTER_STRUCTURE_V02_ALIGNMENT = PASS
STALE_SPANISH_SECTION4_PLACEHOLDER = RESOLVED
DOCX_QA = PASS
EXPERIMENTAL_DESIGN_B01 = VERIFIED / PASS / READY_FOR_AUTHOR_APPROVAL
AUTHOR_APPROVAL_GATE = OPEN
```

La V04 preserva la prosa científica ya auditada de 4.1–4.2.3 y las enmiendas editoriales de 3.5/3.7. El esqueleto no redactado de 4.3–4.8 quedó alineado a Structure V02 en ambos idiomas, sin introducir prosa científica nueva. Section 5 y posteriores permanecen inalterados. El DOCX conserva 40 comentarios, cero tracked changes y supera el render completo de 39 páginas.

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

### Gate vigente

```text
CURRENT_GATE = EXPERIMENTAL_DESIGN_B01_AUTHOR_APPROVAL
NEXT_ACTOR = AUTHOR
NEXT_ACTION = APPROVE_OR_REJECT_B01_V04
B01_CANDIDATE_MD = ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V04.md
B01_CANDIDATE_MD_SHA256 = 0a689a47b4b17fe32aa9252a5ffeed3db955d58b917b6a04114248d14b99e6f8
B01_CANDIDATE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V04.docx
B01_CANDIDATE_DOCX_SHA256 = bfd41dcb873289b993ccdc45d1e09c835e4efa3dd1aa39fbe4de7d257c914a6d
SECTION_4_3_AND_LATER_SCIENTIFIC_DRAFTING = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

---

## English

```text
WORKING_BRANCH = article/main-manuscript
TARGET_A = Knowledge-Based Systems
ARTICLE_WRITING_PLAN = V3.1
LATEST_EDITORIAL_DECISION = D-047
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
CANONICAL_MASTER = ARTICLE_MASTER_V009
CURRENT_GATE = EXPERIMENTAL_DESIGN_B01_AUTHOR_APPROVAL
EXPERIMENTAL_DESIGN_B01_SCIENTIFIC_CONTENT = VERIFIED / PASS
EXPERIMENTAL_DESIGN_B01 = VERIFIED / PASS / READY_FOR_AUTHOR_APPROVAL
B01_CANDIDATE_MD_SHA256 = 0a689a47b4b17fe32aa9252a5ffeed3db955d58b917b6a04114248d14b99e6f8
B01_CANDIDATE_DOCX_SHA256 = bfd41dcb873289b993ccdc45d1e09c835e4efa3dd1aa39fbe4de7d257c914a6d
AUTHOR_APPROVAL_GATE = OPEN
SECTION_4_3_AND_LATER_SCIENTIFIC_DRAFTING = NOT_AUTHORIZED
ARTICLE_MASTER_V010 = SUSPENDED / NOT_MATERIALIZED
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

The V04 differential correction independently passes. The already audited B01 scientific prose and Section-3 amendments remain unchanged; the cumulative Section-4 skeleton is now aligned to the author-approved Structure V02, and the stale Spanish placeholder has been removed. The candidate is ready for explicit author approval. The canonical master remains V009 until the author approves B01 and a subsequent integration gate is completed.