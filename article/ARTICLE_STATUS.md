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
CURRENT_GATE = EXPERIMENTAL_DESIGN_B01_V03_STRUCTURE_SKELETON_ALIGNMENT
EXPERIMENTAL_DESIGN_B01_SCIENTIFIC_CONTENT = VERIFIED / PASS
EXPERIMENTAL_DESIGN_B01 = ACTIVE / TECHNICAL_EDITORIAL_CORRECTION_ONLY
B01_CANDIDATE_MD = ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V03.md
B01_CANDIDATE_MD_SHA256 = b7dc67489715465e9bfbd881efb8cac9a22f1cc43627c71bcb12e4d04da2c346
B01_CANDIDATE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V03.docx
B01_CANDIDATE_DOCX_SHA256 = 315607ab902454a199e63a5fc42dfd9858c262e3932482199b7e1f0bbb9cb7b7
CUMULATIVE_MASTER_STRUCTURE_V02_ALIGNMENT = CORRECTION_REQUIRED
STALE_SPANISH_SECTION4_PLACEHOLDER = CORRECTION_REQUIRED
AUTHOR_APPROVAL_GATE = NOT_OPEN
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
- D-047: la nueva prosa B01 V03 pasa la auditoría científica/editorial; queda únicamente una alineación estructural mecánica del esqueleto 4.3+ y la eliminación de un placeholder residual en el espejo español.

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

### Auditoría de B01 V03

La auditoría independiente `article/reviews/5_EXPERIMENTAL_DESIGN_B01_V03_STRUCTURE_V02_INTERNAL_REVIEW_V01.md` concluye:

```text
B01_SCIENTIFIC_PROSE = PASS
B01_FACTUAL_TRACEABILITY = PASS
B01_EDITORIAL_FOCUS = PASS
SECTION_3_FORWARD_REFERENCE_AMENDMENTS = PASS
DOCX_BINARY_AND_LAYOUT_QA = PASS
MASTER_STRUCTURE_ALIGNMENT = FAIL
STALE_SPANISH_PLACEHOLDER = FAIL
OVERALL = CONTENT_PASS / STRUCTURAL_CORRECTION_REQUIRED
```

El master candidato conserva desde 4.3 el esqueleto V01 porque D-046 prohibía modificar 4.3+ aunque Structure V02 ya era gobernante. D-047 corrige esa contradicción de alcance y permite únicamente el reemplazo mecánico del esqueleto no redactado por 4.3–4.8 de Structure V02, sin abrir redacción científica posterior. También debe eliminarse el placeholder español residual entre `4. Diseño experimental` y `4.1`.

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
CURRENT_GATE = EXPERIMENTAL_DESIGN_B01_V03_STRUCTURE_SKELETON_ALIGNMENT
NEXT_ACTOR = DRAFTING_AI
NEXT_ACTION = STRUCTURAL_ALIGNMENT_ONLY
BASELINE_CANDIDATE_MD = ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V03.md
BASELINE_CANDIDATE_MD_SHA256 = b7dc67489715465e9bfbd881efb8cac9a22f1cc43627c71bcb12e4d04da2c346
BASELINE_CANDIDATE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V03.docx
BASELINE_CANDIDATE_DOCX_SHA256 = 315607ab902454a199e63a5fc42dfd9858c262e3932482199b7e1f0bbb9cb7b7
B01_PROSE_REWRITE = NOT_AUTHORIZED
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
CURRENT_GATE = EXPERIMENTAL_DESIGN_B01_V03_STRUCTURE_SKELETON_ALIGNMENT
EXPERIMENTAL_DESIGN_B01_SCIENTIFIC_CONTENT = VERIFIED / PASS
EXPERIMENTAL_DESIGN_B01 = ACTIVE / TECHNICAL_EDITORIAL_CORRECTION_ONLY
AUTHOR_APPROVAL_GATE = NOT_OPEN
SECTION_4_3_AND_LATER_SCIENTIFIC_DRAFTING = NOT_AUTHORIZED
ARTICLE_MASTER_V010 = SUSPENDED / NOT_MATERIALIZED
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

The B01 V03 scientific prose, factual traceability, publication-facing focus, and two controlled Section-3 amendments independently pass. The cumulative candidate is not yet ready for author approval because its still-unwritten Section-4.3+ skeleton remains the superseded V01 layout and the Spanish mirror retains one stale placeholder before 4.1.

D-047 permits only mechanical alignment of the unfilled Section-4 skeleton to the already approved V02 headings and removal of that placeholder. It does not authorize scientific drafting of 4.3–4.8 or any later section. The canonical master remains V009 until the corrected candidate passes the remaining gates.