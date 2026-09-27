# Plan maestro de redacción / Master Writing Plan

```text
PLAN_VERSION = V3.10
TARGET_JOURNAL = Knowledge-Based Systems
ARTICLE_TYPE = Research article
EDITORIAL_BASIS = KBS_EWG_34_V01
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
LATEST_EDITORIAL_DECISION = D-083
CANONICAL_MASTER = ARTICLE_MASTER_V015
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V015.md
CANONICAL_MASTER_MD_SHA256 = b04de5aa482561adc970f1c7e06e38f8c932fa110cc86605d2d7a0adb9c6983c
CANONICAL_MASTER_MD_GIT_BLOB = e9a17899ccbcb9971e6dfb5002f908e17a0441d9
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B06_V02.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = 86a0b9517ced0f8c411c04c990bc159d3b4b3f814ad592e669a8f1993cf0f3c2
CANONICAL_CITATION_COMMENTS = 40 / PRESERVED
CURRENT_DRAFTING_PHASE = EXPERIMENTAL DESIGN
CURRENT_GATE = B07_V01_NARROW_PUBLIC_REPRO_SCOPE_CORRECTION
EXPERIMENTAL_DESIGN_B01_TO_B06 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B07 = REVISION_REQUIRED / AUTHORIZED_FOR_NARROW_CORRECTION
SECTION_4_8 = REVISION_REQUIRED / B07-C01 ONLY
AUTHOR_APPROVAL_GATE = CLOSED
B07_INTEGRATION = BLOCKED
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

---

# Español

## 1. Estado acumulativo

`ARTICLE_MASTER_V015.md` permanece como master Markdown canónico verificado. El Word acumulativo canónico continúa siendo `ARTICLE_MASTER_CANDIDATE_EXPDES_B06_V02.docx`.

B07 V01 fue científicamente consistente y superó la auditoría Gestora, pero el autor no lo aprobó porque Section 4.8 introducía el repositorio interno de desarrollo experimental como contraparte del repositorio público de reproducibilidad. Esa presentación no debe formar parte de la prosa del manuscrito.

## 2. Corrección autoral congelada — B07-C01

D-082 establece la nueva frontera:

```text
PUBLIC_REPRO_REPOSITORY = gci-nandina-rag-reproducibility
INTERNAL_DEVELOPMENT_REPOSITORY_MENTION_IN_SECTION_4_8 = REMOVE
PUBLIC_RESOURCE_FOCUS = REQUIRED
MATERIALIZED_VS_PLANNED_VS_RESTRICTED = PRESERVE
REFERENCE_REPRODUCTION_VS_EXTERNAL_REPLICATION = PRESERVE
CONFIGURABILITY_IS_NOT_GENERALIZATION = PRESERVE
```

El repositorio interno puede seguir siendo fuente de trabajo y trazabilidad del proceso experimental/editorial, pero no debe aparecer en Section 4.8 como recurso de reproducibilidad para el lector.

## 3. Baselines de revisión

La corrección se realiza sobre los candidatos B07 V01 exactos, no sobre V015/B06:

```text
ARTICLE_MASTER_CANDIDATE_EXPDES_B07_V01.md
SHA256 = a2a7e5527bf69cebab1e6ab3d36a95dd16b5ceac34862038f7fff4ef38d3db12
GIT_BLOB = 0d8a4ad3dd03c5b69feeec6a5710d296a5a76662

ARTICLE_MASTER_CANDIDATE_EXPDES_B07_V01.docx
SHA256 = dc51307ed3ca6918dd1c43de67d366e82121a5f5ed047ccf542d4f400b0abf6c
COMMENTS = 40 / PRESERVE
TRACKED_CHANGES = 0
```

## 4. Contrato correctivo vigente

Prompt autorizado:

`article/prompts/5_EXPERIMENTAL_DESIGN_B07_V01_NARROW_PUBLIC_REPRO_SCOPE_CORRECTION.md@e7ee988c42c2095a0e0b60dd7a216bf148949419`

Git blob:

`a492b8f53b463aba3295fd71b12dc9f637e74fea`

Revisión interna:

`article/reviews/5_EXPERIMENTAL_DESIGN_B07_NARROW_PUBLIC_REPRO_SCOPE_CORRECTION_PROMPT_REVIEW_V01.md@60d25426aa0e092617f9df866ee9a4d06101d77f` — `PASS`.

Autorización: D-083.

La revisión debe ser mínima: eliminar la mención/comparación con el repositorio interno en EN/ES y conservar el resto de Section 4.8 salvo ajustes estrictamente necesarios para fluidez.

## 5. D-035 obligatorio

El timeout previo de B07 mantiene D-035 activado:

```text
BASE64_MANUAL = PROHIBITED
CHUNKING = PROHIBITED
FRAGMENTATION = PROHIBITED
REASSEMBLY = PROHIBITED
DIRECT_GITHUB_MATERIALIZATION_OF_LARGE_MASTER = DO_NOT_ATTEMPT
REAL_FILE_HANDOFF_MD_DOCX = REQUIRED
```

## 6. Gate

```text
NEXT_ACTOR = IA_REDACCION
NEXT_ACTION = EXECUTE_B07_C01_ONLY
EXPECTED_SECTION_ARTIFACT = article/sections/experimental_design/Experimental_Design_B07_V02.md
EXPECTED_MASTER_MD = ARTICLE_MASTER_CANDIDATE_EXPDES_B07_V02.md
EXPECTED_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B07_V02.docx
EXPECTED_RESPONSE = article/responses/5_EXPERIMENTAL_DESIGN_B07_SECTION4_8_RESPONSE_V02.md
EXPECTED_EXIT = COMPLETED_PENDING_GESTORA_AUDIT
AUTHOR_APPROVAL_GATE = CLOSED
RESULTS = NOT_AUTHORIZED
```

---

# English

## 1. Current state

`ARTICLE_MASTER_V015.md` remains canonical. B07 V01 passed technical review but was not approved by the author. The author requested one narrow editorial correction: remove the internal experimental-development repository from Section 4.8 manuscript prose and focus directly on the public `gci-nandina-rag-reproducibility` package.

## 2. Authorized correction

D-082 freezes B07-C01 and D-083 authorizes its execution. Use the exact B07 V01 MD/DOCX candidates as baselines. Preserve all other correct B07 boundaries and all content outside Section 4.8.

D-035 remains mandatory because of the prior timeout. The corrected cumulative MD/DOCX must be handed off as real files; manual Base64, chunking, fragmentation, reassembly, and direct GitHub materialization of the large master are prohibited.

```text
CURRENT_GATE = B07_V01_NARROW_PUBLIC_REPRO_SCOPE_CORRECTION
NEXT_ACTOR = DRAFTING_AI
EXPECTED_REVISION = B07_V02
AUTHOR_APPROVAL_GATE = CLOSED
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```