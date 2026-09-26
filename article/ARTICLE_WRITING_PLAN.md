# Plan maestro de redacción / Master Writing Plan

```text
PLAN_VERSION = V3.4
TARGET_JOURNAL = Knowledge-Based Systems
ARTICLE_TYPE = Research article
EDITORIAL_BASIS = KBS_EWG_34_V01
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
LATEST_EDITORIAL_DECISION = D-069
CANONICAL_MASTER = ARTICLE_MASTER_V013
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V013.md
CANONICAL_MASTER_MD_GIT_BLOB = 06beaa052e2f1bcc630647040762fe78d3838a62
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V02.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = cff5520d5bc31af929abaf796048ef3b452627f8fef8e5f727c4f8cc661d222f
CANONICAL_CITATION_COMMENTS = 40
CURRENT_DRAFTING_PHASE = EXPERIMENTAL DESIGN
CURRENT_GATE = EXPERIMENTAL_DESIGN_B05_AUTHOR_APPROVAL
EXPERIMENTAL_DESIGN_B01 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B02 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B03 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B04 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B05 = PASS / PENDING_AUTHOR_APPROVAL
SECTION_4_6 = PASS / PENDING_AUTHOR_APPROVAL
SECTION_4_7_TO_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

---

# Español

## 1. Política acumulativa

El artículo se construye sobre masters acumulativos. V013 es el master Markdown canónico verificado. El Word acumulativo canónico vigente es el B04 V02 aprobado bajo custodia local del autor. MWDP v1.0, SPCCR, D-021/D-022/D-027/D-035, las decisiones activas, `SOURCE_REGISTRY.md` y `CLAIM_EVIDENCE_MATRIX.md` permanecen vinculantes.

No se reconstruyen masters acumulativos. Cada bloque nuevo modifica únicamente los placeholders expresamente autorizados y vuelve a Gestora para auditoría antes de cualquier aprobación o promoción.

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
| B05 / 4.6 | PASS / PENDING_AUTHOR_APPROVAL |
| B06 / 4.7 | NOT AUTHORIZED |
| 4.8 | NOT AUTHORIZED |
| Results | NOT AUTHORIZED |
| Discussion | NOT AUTHORIZED |
| Conclusion | NOT AUTHORIZED |

## 4. B05 / Section 4.6 — estado de cierre científico

Contrato de redacción ejecutado:

`article/prompts/5_EXPERIMENTAL_DESIGN_B05_SECTION4_6.md@89a5e122c7ed6ab0ffe90a53e2a68e65830d6d99`

Respuesta final de ejecución:

`article/responses/5_EXPERIMENTAL_DESIGN_B05_SECTION4_6_RESPONSE_V02.md@9e9546a9d052c1fc1145bf42d37f53e7bcd0ba84`

Revisión científica/técnica primaria:

`article/reviews/5_EXPERIMENTAL_DESIGN_B05_SECTION4_6_INTERNAL_REVIEW_V01.md@bad6a978ef0a6e70c6db675cf77ff8bf7f2942cf`

Revisión del microgate de metadata:

`article/reviews/5_EXPERIMENTAL_DESIGN_B05_RESPONSE_METADATA_CORRECTION_REVIEW_V01.md@f8e611bc359bd9c408595907355b755bf82c602f` — `PASS`.

Decisión vigente: D-069.

### 4.1 Función científica

B05 mapea `RQ → función → salida → unidad → métrica/protocolo → interpretación permitida` y mantiene tres familias separadas:

- RQ1 / candidate retrieval;
- RQ2 / documentary evidence;
- RQ3 / controlled explanation.

RQ4 se mantiene como frontera de validez/robustez y remite a 4.4/4.7.

### 4.2 Fronteras preservadas

- Candidate retrieval ≠ overall classification accuracy.
- Documentary coverage/association ≠ substantive normative/legal correctness.
- Auditability ≠ legal correctness.
- Automatic HE4 checks ≠ qualitative rubric.
- La evaluación cualitativa HE4 efectiva fue `AI_EXPERT_ROLE / LLM-as-judge`; `HUMAN_SCORING = FALSE`.
- C14 es el único claim condicional utilizado en 4.6 y se emplea con los límites explícitos exigidos.
- Los resultados numéricos observados permanecen fuera de 4.6.
- Inferencia, sensibilidad y robustez permanecen reservadas principalmente para 4.7.

## 5. Candidatos B05 bajo gate autoral

```text
B05_CANDIDATE_MD = ARTICLE_MASTER_CANDIDATE_EXPDES_B05_V01.md
B05_CANDIDATE_MD_SHA256 = e7aa7e6706923520a5403ab4dec6713d5a1f7fe6b55edccbde43f2d54b755b97
B05_CANDIDATE_MD_GIT_BLOB_EXPECTED = 20105abb745e382b923e4eb43d9a771a722df9e3
B05_CANDIDATE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B05_V01.docx
B05_CANDIDATE_DOCX_SHA256 = b1ab0ba79fe8d4dffad57208b2765f18e2c84b80ef4c1dbcfd3ac93eba8f78e2
PRIOR_CITATION_COMMENTS = 40 / PRESERVED
TARGET_CANONICAL_MASTER_IF_APPROVED = ARTICLE_MASTER_V014
```

Los candidatos han recibido `PASS` científico y técnico, pero todavía no son canónicos. La aprobación expresa del autor es requisito previo para cualquier promoción a V014.

## 6. Concurrencia experimental

Último corte sincronizado antes de abrir B05:

```text
SRC03_HEAD = 87422102290a4f9a89c51e936cf7274d8e4687d8
SRC03_PLAN_BLOB = cf587b61b7bfbc66dca310a7bb3b4d3f64671eea
DEVELOPMENT_MAIN = db0d0ad0d8435921a7838db6720eaea86a263763
```

El avance de flujos externos no abre automáticamente 4.7 ni Results.

## 7. Gate inmediato

```text
NEXT_ACTOR = AUTHOR
NEXT_ACTION = APPROVE_OR_REQUEST_CORRECTION_FOR_B05_SECTION_4_6
AUTHOR_APPROVAL_GATE = OPEN
CURRENT_CANONICAL_MASTER = ARTICLE_MASTER_V013
TARGET_CANONICAL_MASTER_IF_APPROVED = ARTICLE_MASTER_V014
INTEGRATION = NOT_AUTHORIZED_PENDING_AUTHOR_DECISION
B06 / SECTION_4_7 = NOT_AUTHORIZED
SECTION_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

---

# English

## 1. Current cumulative state

V013 remains the verified canonical Markdown master. The current canonical cumulative Word baseline is the approved B04 V02 DOCX in local author custody. B01–B04 are closed, approved, frozen, and integrated.

B05/Section 4.6 has passed independent scientific/technical review. Its sole response-metadata defect was corrected in response V02 and the corrective microgate review passed. B05 is therefore pending explicit author approval under D-069.

## 2. Scientific function and boundaries

B05 maps each RQ to system function, output, evaluation unit, metric/protocol, and permitted interpretation. RQ1 maps to candidate retrieval, RQ2 to documentary evidence, and RQ3 to controlled explanation. RQ4 remains a validity/robustness boundary linked to Sections 4.4 and 4.7.

Candidate retrieval is not overall classification accuracy; documentary association is not substantive normative/legal correctness; auditability is not legal correctness; automatic HE4 checks remain distinct from the qualitative rubric; and the actual qualitative evaluator modality was AI-expert/LLM-as-judge with no human scoring. C14 is the sole conditional claim used in Section 4.6 and is used under satisfied explicit limitations. Observed Results remain outside Section 4.6.

## 3. Candidate identities and gate

```text
CURRENT_CANONICAL_MASTER = ARTICLE_MASTER_V013
B05_CANDIDATE_MD = ARTICLE_MASTER_CANDIDATE_EXPDES_B05_V01.md
B05_CANDIDATE_MD_SHA256 = e7aa7e6706923520a5403ab4dec6713d5a1f7fe6b55edccbde43f2d54b755b97
B05_CANDIDATE_MD_GIT_BLOB_EXPECTED = 20105abb745e382b923e4eb43d9a771a722df9e3
B05_CANDIDATE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B05_V01.docx
B05_CANDIDATE_DOCX_SHA256 = b1ab0ba79fe8d4dffad57208b2765f18e2c84b80ef4c1dbcfd3ac93eba8f78e2
TARGET_CANONICAL_MASTER_IF_APPROVED = ARTICLE_MASTER_V014
CURRENT_GATE = EXPERIMENTAL_DESIGN_B05_AUTHOR_APPROVAL
NEXT_ACTOR = AUTHOR
INTEGRATION = NOT_AUTHORIZED_PENDING_AUTHOR_DECISION
B06 / SECTION_4_7 = NOT_AUTHORIZED
SECTION_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```