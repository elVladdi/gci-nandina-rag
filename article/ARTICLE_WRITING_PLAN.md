# Plan maestro de redacción / Master Writing Plan

```text
PLAN_VERSION = V3.4
TARGET_JOURNAL = Knowledge-Based Systems
ARTICLE_TYPE = Research article
EDITORIAL_BASIS = KBS_EWG_34_V01
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
LATEST_EDITORIAL_DECISION = D-070
CANONICAL_MASTER = ARTICLE_MASTER_V013
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V013.md
CANONICAL_MASTER_MD_GIT_BLOB = 06beaa052e2f1bcc630647040762fe78d3838a62
CURRENT_CANONICAL_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V02.docx / LOCAL_AUTHOR_CUSTODY
CURRENT_CANONICAL_DOCX_SHA256 = cff5520d5bc31af929abaf796048ef3b452627f8fef8e5f727c4f8cc661d222f
B05_APPROVED_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B05_V01.docx / LOCAL_AUTHOR_CUSTODY
B05_APPROVED_DOCX_SHA256 = b1ab0ba79fe8d4dffad57208b2765f18e2c84b80ef4c1dbcfd3ac93eba8f78e2
CANONICAL_CITATION_COMMENTS = 40 / PRESERVED
CURRENT_DRAFTING_PHASE = EXPERIMENTAL DESIGN
CURRENT_GATE = B05_V014_PROMOTION
EXPERIMENTAL_DESIGN_B01 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B02 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B03 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B04 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B05 = CLOSED / APPROVED / FROZEN / READY_FOR_INTEGRATION
SECTION_4_6 = CLOSED / APPROVED / FROZEN / READY_FOR_INTEGRATION
TARGET_CANONICAL_MASTER = ARTICLE_MASTER_V014
B06 / SECTION_4_7 = NOT_AUTHORIZED_UNTIL_V014_INTEGRATION_CLOSE
SECTION_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

---

# Español

## 1. Política acumulativa

El artículo se construye sobre masters acumulativos. `ARTICLE_MASTER_V013.md` permanece canónico hasta completar la promoción técnica autorizada por D-070. B05/Section 4.6 ya cuenta con aprobación autoral expresa y está congelado para integración.

MWDP v1.0, SPCCR, D-021/D-022/D-027/D-035, las decisiones activas, `SOURCE_REGISTRY.md` y `CLAIM_EVIDENCE_MATRIX.md` permanecen vinculantes. No se reconstruyen masters acumulativos ni se alteran bloques aprobados durante una promoción.

## 2. Estructura congelada de Experimental Design

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

## 3. Estado de construcción

| Bloque | Estado |
|---|---|
| Related Work | CLOSED / APPROVED / FROZEN / INTEGRATED |
| Introduction | CLOSED / APPROVED / FROZEN / INTEGRATED |
| Architecture 3.1–3.7 | CLOSED / APPROVED / FROZEN / INTEGRATED |
| B01 / 4.1–4.2.3 | CLOSED / APPROVED / FROZEN / INTEGRATED |
| B02 / 4.3 | CLOSED / APPROVED / FROZEN / INTEGRATED |
| B03 / 4.4 | CLOSED / APPROVED / FROZEN / INTEGRATED |
| B04 / 4.5 | CLOSED / APPROVED / FROZEN / INTEGRATED |
| ARTICLE_MASTER_V013 | CANONICAL / VERIFIED |
| B05 / 4.6 | CLOSED / APPROVED / FROZEN / READY_FOR_INTEGRATION |
| ARTICLE_MASTER_V014 | AUTHORIZED / PENDING_MATERIALIZATION_AND_VERIFICATION |
| B06 / 4.7 | NOT AUTHORIZED UNTIL V014 INTEGRATION CLOSE |
| 4.8 | NOT AUTHORIZED |
| Results | NOT AUTHORIZED |
| Discussion | NOT AUTHORIZED |
| Conclusion | NOT AUTHORIZED |

## 4. B05 / Section 4.6 — cierre autoral

La ejecución B05 se realizó bajo:

`article/prompts/5_EXPERIMENTAL_DESIGN_B05_SECTION4_6.md@89a5e122c7ed6ab0ffe90a53e2a68e65830d6d99`.

La response final es:

`article/responses/5_EXPERIMENTAL_DESIGN_B05_SECTION4_6_RESPONSE_V02.md@9e9546a9d052c1fc1145bf42d37f53e7bcd0ba84`.

La auditoría científica/técnica y el microgate correctivo de metadata recibieron `PASS`. D-070 registra la aprobación autoral explícita y congela 4.6/4.6.1–4.6.3 para integración.

Se mantienen:

- candidate retrieval ≠ overall classification accuracy;
- documentary association ≠ substantive normative/legal correctness;
- auditability ≠ legal correctness;
- automatic HE4 checks ≠ qualitative rubric;
- evaluación cualitativa efectiva `AI_EXPERT_ROLE / LLM-as-judge`, `HUMAN_SCORING = FALSE`;
- C14 como único claim condicional de 4.6, bajo límites explícitos;
- ausencia de resultados observados en Methods.

## 5. Promoción autorizada a V014

El candidato aprobado es:

```text
B05_CANDIDATE_MD = ARTICLE_MASTER_CANDIDATE_EXPDES_B05_V01.md
B05_CANDIDATE_MD_SHA256 = e7aa7e6706923520a5403ab4dec6713d5a1f7fe6b55edccbde43f2d54b755b97
B05_CANDIDATE_MD_GIT_BLOB_EXPECTED = 20105abb745e382b923e4eb43d9a771a722df9e3
B05_CANDIDATE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B05_V01.docx
B05_CANDIDATE_DOCX_SHA256 = b1ab0ba79fe8d4dffad57208b2765f18e2c84b80ef4c1dbcfd3ac93eba8f78e2
TARGET_CANONICAL_MASTER = ARTICLE_MASTER_V014
```

La promoción Markdown debe ser byte-exacta. El DOCX permanece bajo custodia local del autor y será la base acumulativa de B06 una vez se cierre técnicamente la integración V014.

## 6. Orden operativo inmediato

```text
CURRENT_GATE = B05_V014_PROMOTION
NEXT_ACTION = MATERIALIZE_AND_VERIFY_ARTICLE_MASTER_V014
CURRENT_CANONICAL_MASTER = ARTICLE_MASTER_V013
TARGET_CANONICAL_MASTER = ARTICLE_MASTER_V014
AFTER_VERIFIED_PROMOTION = CLOSE_B05_INTEGRATION_AND_PREPARE_B06
B06 / SECTION_4_7 = NOT_AUTHORIZED_UNTIL_THEN
SECTION_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

---

# English

## Current state

B05/Section 4.6 has passed scientific/technical review, the response-metadata corrective microgate, and explicit author approval. D-070 freezes Sections 4.6 and 4.6.1–4.6.3 for integration.

`ARTICLE_MASTER_V013.md` remains canonical until the approved B05 Markdown candidate is materialized and verified byte-exactly as `ARTICLE_MASTER_V014.md`.

```text
B05_CANDIDATE_MD_SHA256 = e7aa7e6706923520a5403ab4dec6713d5a1f7fe6b55edccbde43f2d54b755b97
B05_CANDIDATE_MD_GIT_BLOB_EXPECTED = 20105abb745e382b923e4eb43d9a771a722df9e3
B05_CANDIDATE_DOCX_SHA256 = b1ab0ba79fe8d4dffad57208b2765f18e2c84b80ef4c1dbcfd3ac93eba8f78e2
CURRENT_GATE = B05_V014_PROMOTION
TARGET_CANONICAL_MASTER = ARTICLE_MASTER_V014
B06 / SECTION_4_7 = NOT_AUTHORIZED_UNTIL_V014_INTEGRATION_CLOSE
SECTION_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

After verified V014 promotion, the Managing AI may close B05 integration and prepare the Section 4.7 gate. No later section is opened by D-070 itself.