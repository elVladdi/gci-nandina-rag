# Estado del artículo / Article Status

## Español

```text
WORKING_BRANCH = article/main-manuscript
TARGET_A = Knowledge-Based Systems
ARTICLE_TYPE_OPERATIVE = Research article
ARTICLE_WRITING_PLAN = V3.4
LATEST_EDITORIAL_DECISION = D-066
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
RELATED_WORK = CLOSED / APPROVED / FROZEN / INTEGRATED
INTRODUCTION_B01 = CLOSED / APPROVED / FROZEN / INTEGRATED
ARCHITECTURE_SECTIONS_3_1_TO_3_7 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B01 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B02 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B03 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B04 = CLOSED / APPROVED / FROZEN / INTEGRATED
SECTION_4_5 = CLOSED / APPROVED / FROZEN / INTEGRATED
CANONICAL_MASTER = ARTICLE_MASTER_V013
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V013.md
CANONICAL_MASTER_MD_SHA256 = 2e6b4446ffddb18940625a72a871a84a36405930b21db3dbba352c1535972f43
CANONICAL_MASTER_MD_GIT_BLOB = 06beaa052e2f1bcc630647040762fe78d3838a62
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V02.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = cff5520d5bc31af929abaf796048ef3b452627f8fef8e5f727c4f8cc661d222f
CANONICAL_CITATION_COMMENTS = 40
CURRENT_DRAFTING_PHASE = EXPERIMENTAL DESIGN
CURRENT_GATE = EXPERIMENTAL_DESIGN_B05_SECTION_4_6_GROUND_TRUTH_SYNC_AND_PROMPT_PREPARATION
SECTION_4_6 = ELIGIBLE / NOT_YET_AUTHORIZED_FOR_DRAFTING
SECTION_4_7_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
AUTHOR_APPROVAL_GATE = NOT_OPEN
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### Cierre de B04 y V013

B04/Section 4.5 superó la auditoría científica, las correcciones estrechas B04-C01/B04-C02, la auditoría diferencial independiente y la aprobación expresa del autor. D-065 autorizó la promoción exacta del candidato B04 V02.

La IA Gestora verificó directamente que `article/manuscript/ARTICLE_MASTER_V013.md` expone el Git blob `06beaa052e2f1bcc630647040762fe78d3838a62`, exactamente igual al blob esperado del candidato aprobado. D-066 cierra por tanto la integración y establece V013 como master canónico. No hubo reconstrucción o reescritura durante la promoción.

El baseline Word acumulativo pasa a ser `ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V02.docx`, SHA-256 `cff5520d5bc31af929abaf796048ef3b452627f8fef8e5f727c4f8cc661d222f`, bajo custodia local del autor, con 40 comentarios heredados y cero tracked changes según la auditoría aprobada.

### Preparación de B05 / Section 4.6

La estructura congelada define:

```text
4.6 Evaluation framework and protocols
  4.6.1 Candidate-retrieval evaluation
  4.6.2 Documentary-evidence evaluation
  4.6.3 Controlled-explanation evaluation
```

B05 debe mapear `RQ → función del sistema → salida → unidad de evaluación → métrica/protocolo → interpretación permitida` y mantener separadas las tres familias de evaluación. No puede anticipar valores de Results ni invadir 4.7.

Corte experimental vivo observado durante la preparación:

```text
SRC03_HEAD = 87422102290a4f9a89c51e936cf7274d8e4687d8
SRC03_PLAN_BLOB = cf587b61b7bfbc66dca310a7bb3b4d3f64671eea
DEVELOPMENT_MAIN = db0d0ad0d8435921a7838db6720eaea86a263763
GROUP3 = CLOSED / APPROVED
GROUP4 = CLOSED / APPROVED
GROUP5 = CLOSED / APPROVED
GROUP6 = CLOSED / APPROVED
GROUP7 = IN_PROGRESS / NOT_CLOSED
G7_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G7_F02 = ACTIVE / AUTHORIZED / EXECUTION_PENDING
G7_F03 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
```

El estado de Grupo 7 corresponde al flujo de redacción científica de la tesis y no autoriza por sí mismo ninguna modificación del artículo. Para B05 gobiernan los contratos y artefactos experimentales congelados ya integrados a `main`, junto con las fronteras del artículo.

### Fronteras científicas obligatorias

- `CANDIDATE_RETRIEVAL ≠ OVERALL_CLASSIFICATION_ACCURACY`.
- `NORMATIVE_ASSOCIATION ≠ SUBSTANTIVE_NORMATIVE_CORRECTNESS`.
- `AUDITABILITY ≠ LEGAL_CORRECTNESS`.
- `CONFIGURABILITY ≠ EMPIRICAL_GENERALIZATION`.
- SERIE es unidad primaria de análisis; DAM/declaración se usa como agrupamiento cuando la dependencia es relevante.
- EXP11A = sensibilidad tamaño/composición, no efecto causal aislado.
- EXP11B = descriptivo, no inferencia a una superpoblación de seeds.
- EXP12 = `NOT_ESTIMABLE`.
- `FINAL_GAP = NOT_DEFINED`.
- `NOVELTY = NOT_DECLARED`.

```text
CURRENT_GATE = EXPERIMENTAL_DESIGN_B05_SECTION_4_6_GROUND_TRUTH_SYNC_AND_PROMPT_PREPARATION
NEXT_ACTOR = IA_GESTORA
BASELINE_MASTER_MD = article/manuscript/ARTICLE_MASTER_V013.md
BASELINE_MASTER_MD_GIT_BLOB = 06beaa052e2f1bcc630647040762fe78d3838a62
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V02.docx / LOCAL_AUTHOR_CUSTODY
BASELINE_DOCX_SHA256 = cff5520d5bc31af929abaf796048ef3b452627f8fef8e5f727c4f8cc661d222f
SECTION_4_6 = ELIGIBLE / NOT_YET_AUTHORIZED_FOR_DRAFTING
SECTION_4_7_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

---

## English

```text
WORKING_BRANCH = article/main-manuscript
TARGET_A = Knowledge-Based Systems
LATEST_EDITORIAL_DECISION = D-066
EXPERIMENTAL_DESIGN_B04 = CLOSED / APPROVED / FROZEN / INTEGRATED
SECTION_4_5 = CLOSED / APPROVED / FROZEN / INTEGRATED
CANONICAL_MASTER = ARTICLE_MASTER_V013
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V013.md
CANONICAL_MASTER_MD_SHA256 = 2e6b4446ffddb18940625a72a871a84a36405930b21db3dbba352c1535972f43
CANONICAL_MASTER_MD_GIT_BLOB = 06beaa052e2f1bcc630647040762fe78d3838a62
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V02.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = cff5520d5bc31af929abaf796048ef3b452627f8fef8e5f727c4f8cc661d222f
CANONICAL_CITATION_COMMENTS = 40
CURRENT_GATE = EXPERIMENTAL_DESIGN_B05_SECTION_4_6_GROUND_TRUTH_SYNC_AND_PROMPT_PREPARATION
SECTION_4_6 = ELIGIBLE / NOT_YET_AUTHORIZED_FOR_DRAFTING
SECTION_4_7_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

The Managing AI directly verified that `ARTICLE_MASTER_V013.md` has Git blob `06beaa052e2f1bcc630647040762fe78d3838a62`, exactly matching the frozen approved B04 V02 candidate. D-066 therefore closes B04 integration and makes V013 canonical. The cumulative Word baseline is the approved B04 V02 DOCX in local author custody.

The next section is 4.6 `Evaluation framework and protocols`, with candidate-retrieval, documentary-evidence, and controlled-explanation evaluation as distinct subsections. Drafting is not yet authorized until the Managing AI finishes the ground-truth synchronization and emits an atomic B05 contract. Results, Section 4.7, and Section 4.8 remain closed.