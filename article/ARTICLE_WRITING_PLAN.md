# Plan maestro de redacción / Master Writing Plan

```text
PLAN_VERSION = V3.14
TARGET_JOURNAL = Knowledge-Based Systems
ARTICLE_TYPE = Research article
EDITORIAL_BASIS = KBS_EWG_34_V01
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
LATEST_EDITORIAL_DECISION = D-088
CANONICAL_MASTER = ARTICLE_MASTER_V016
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V016.md
CANONICAL_MASTER_MD_SHA256 = 3c8b64104b11f2e07f85d0275e5ac6c4a96cb0c5cd5b183704949705c8e120a5
CANONICAL_MASTER_MD_GIT_BLOB = e8f9ffddb616b4a7d036f1b57fbe9f18d73613cc
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B07_V02.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = c9c12609e7aefc5c2b260a967df88d87641252e2be28eab838f984952f48b4de
CANONICAL_CITATION_COMMENTS = 40 / PRESERVED
CURRENT_DRAFTING_PHASE = RESULTS
CURRENT_GATE = RESULTS_B01_SECTION_5_1_DRAFTING_V01
EXPERIMENTAL_DESIGN = CLOSED / APPROVED / FROZEN / INTEGRATED
RESULTS_B01_SECTION_5_1 = OPEN / AUTHORIZED_FOR_DRAFTING_UNDER_B01_V01_ONLY
RESULTS_B02_PLUS = NOT_AUTHORIZED
AUTHOR_APPROVAL_GATE = NOT_OPEN
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

---

# Español

## 1. Estado acumulativo

`ARTICLE_MASTER_V016.md` es el master Markdown canónico verificado. El Word acumulativo canónico es `ARTICLE_MASTER_CANDIDATE_EXPDES_B07_V02.docx`, bajo custodia local del autor, con 40 comentarios y 0 tracked changes.

Experimental Design está cerrado, aprobado, congelado e integrado. La fase activa pasa a Results, pero exclusivamente mediante bloques independientes y gates explícitos.

## 2. Estructura congelada de Results

```text
5.1 Data and partition checks
5.2 Candidate retrieval performance
5.3 Documentary evidence retrieval
5.4 Controlled explanation quality
5.5 Sensitivity and robustness analyses
5.6 Inferential results
5.7 Summary by research question
```

Solo §5.1 está abierta. La existencia de evidencia elegible para secciones posteriores no las autoriza por anticipado.

## 3. Ground truth de Results B01

D-087:

`article/governance/D087_RESULTS_GROUND_TRUTH_SYNC_AND_B01_BOUNDARY.md@22a63fa715ae2c7bddb92af06d65c417f257932b`

Snapshot experimental congelado:

`db0d0ad0d8435921a7838db6720eaea86a263763`

Fuentes B01:

```text
data/processed/data_aduanas_splits_clase87_v0.2_metadata.json
GIT_BLOB = bcb02c9c3493235a6f80991158c5b24fa7c04510

outputs/audits/data_aduanas_splits_clase87_v0.2/audit_summary_v0.2.json
GIT_BLOB = fb21eb0d8ef77cdedaa32698b854595629ed526d
```

B01 está limitado a:

- composición v0.2: H100 2,950 SERIE / 28 DAM / 66 códigos; DEV 100 / 6 / 9; EVAL 1,056 / 67 / 42;
- asignación completa de 4,106 SERIE;
- cero solapamiento cross-partition de DAM e `id_unico`;
- soporte histórico nominal de 1,056/1,056 casos y 42/42 códigos EVAL;
- duplicados exactos H100–EVAL: 35/1,056 (3.31%), con DAM distintas;
- near-duplicates H100–EVAL: 55 (5.21%) a Jaccard ≥0.90, 44 (4.17%) a ≥0.95 y 37 (3.50%) a ≥0.98.

No pertenecen a B01 retrieval performance, evidence coverage, explanation quality, sensibilidades, inferencia, HE2/HE5 ni Discussion.

## 4. Contrato de redacción activo

Prompt:

`article/prompts/6_RESULTS_B01_SECTION5_1.md@cc75fb9b732de6b9162cf90b8eacb8462372405e`

Git blob:

`a0f4005e8c406574d39b5540dfbf676f3d4acc0d`

Revisión:

`article/reviews/6_RESULTS_B01_SECTION5_1_PROMPT_INTERNAL_REVIEW_V01.md@275c6e14d7d3eab0ada488e829dcd07f8b1254df` — `PASS`.

Autorización:

`article/governance/D088_RESULTS_B01_SECTION5_1_EXECUTION_AUTHORIZATION.md@da7fa50368439304fd9cd43042ed1c3dfd1b5b08`.

## 5. Baselines y entrega

```text
BASELINE_MASTER_MD = article/manuscript/ARTICLE_MASTER_V016.md
BASELINE_MASTER_MD_SHA256 = 3c8b64104b11f2e07f85d0275e5ac6c4a96cb0c5cd5b183704949705c8e120a5
BASELINE_MASTER_MD_GIT_BLOB = e8f9ffddb616b4a7d036f1b57fbe9f18d73613cc

BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B07_V02.docx
BASELINE_DOCX_SHA256 = c9c12609e7aefc5c2b260a967df88d87641252e2be28eab838f984952f48b4de
COMMENTS = 40 / PRESERVE
TRACKED_CHANGES = 0 / PRESERVE
```

D-035 continúa activado para la cadena acumulativa: Base64 manual, chunking, fragmentación y reensamblado están prohibidos; el MD/DOCX acumulativo debe entregarse como archivo real al autor. El DOCX no se reconstruye desde Markdown.

## 6. Gate inmediato

```text
NEXT_ACTOR = IA_REDACCION
NEXT_ACTION = EXECUTE_ONLY_RESULTS_B01_SECTION_5_1
EXPECTED_SECTION_ARTIFACT = article/sections/results/Results_B01_V01.md
EXPECTED_MASTER_MD = ARTICLE_MASTER_CANDIDATE_RESULTS_B01_V01.md
EXPECTED_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_RESULTS_B01_V01.docx
EXPECTED_RESPONSE = article/responses/6_RESULTS_B01_SECTION5_1_RESPONSE_V01.md
EXPECTED_EXIT = COMPLETED_PENDING_GESTORA_AUDIT
RESULTS_B02_PLUS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
```

---

# English

## 1. Current state

V016 is the canonical verified Markdown master and the B07 V02 DOCX is the canonical cumulative Word baseline. Experimental Design is fully integrated. Results B01 / Section 5.1 is now the only open drafting block.

## 2. B01 contract

Ground truth is frozen by D-087 from the v0.2 metadata and audit summary at development snapshot `db0d0ad0d8435921a7838db6720eaea86a263763`. The active drafting contract is `article/prompts/6_RESULTS_B01_SECTION5_1.md@cc75fb9b732de6b9162cf90b8eacb8462372405e`, reviewed PASS and authorized by D-088.

```text
CURRENT_GATE = RESULTS_B01_SECTION_5_1_DRAFTING_V01
NEXT_ACTOR = DRAFTING_AI
RESULTS_B01 = AUTHORIZED
RESULTS_B02_PLUS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```