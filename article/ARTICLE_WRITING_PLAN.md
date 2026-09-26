# Plan maestro de redacción / Master Writing Plan

```text
PLAN_VERSION = V3.4
TARGET_JOURNAL = Knowledge-Based Systems
ARTICLE_TYPE = Research article
EDITORIAL_BASIS = KBS_EWG_34_V01
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
LATEST_EDITORIAL_DECISION = D-068
CANONICAL_MASTER = ARTICLE_MASTER_V013
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V013.md
CANONICAL_MASTER_MD_GIT_BLOB = 06beaa052e2f1bcc630647040762fe78d3838a62
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V02.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = cff5520d5bc31af929abaf796048ef3b452627f8fef8e5f727c4f8cc661d222f
CANONICAL_CITATION_COMMENTS = 40
CURRENT_DRAFTING_PHASE = EXPERIMENTAL DESIGN
CURRENT_GATE = EXPERIMENTAL_DESIGN_B05_SECTION_4_6_DRAFTING_V01
EXPERIMENTAL_DESIGN_B01 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B02 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B03 = CLOSED / APPROVED / FROZEN / INTEGRATED
EXPERIMENTAL_DESIGN_B04 = CLOSED / APPROVED / FROZEN / INTEGRATED
SECTION_4_6 = OPEN / AUTHORIZED_FOR_DRAFTING_UNDER_B05_V01_ONLY
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

El artículo se construye sobre masters acumulativos. V013 es el master Markdown canónico verificado. El Word acumulativo vigente es el B04 V02 aprobado bajo custodia local del autor. MWDP v1.0, SPCCR, D-021/D-022/D-027/D-035, las decisiones activas, `SOURCE_REGISTRY.md` y `CLAIM_EVIDENCE_MATRIX.md` permanecen vinculantes.

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
| B05 / 4.6 | OPEN / AUTHORIZED UNDER B05 V01 ONLY |
| B06 / 4.7 | NOT AUTHORIZED |
| 4.8 | NOT AUTHORIZED |
| Results | NOT AUTHORIZED |
| Discussion | NOT AUTHORIZED |
| Conclusion | NOT AUTHORIZED |

## 4. Fase activa — B05

Contrato único ejecutable:

`article/prompts/5_EXPERIMENTAL_DESIGN_B05_SECTION4_6.md@89a5e122c7ed6ab0ffe90a53e2a68e65830d6d99`

Git blob:

`55108c6628da436c601b8a69a8397c32b2c0589d`

Revisión interna:

`article/reviews/5_EXPERIMENTAL_DESIGN_B05_SECTION4_6_PROMPT_INTERNAL_REVIEW_V01.md@03d70a8f891b98956fd69f39a972497e6eec8886` — `PASS`.

Autorización: D-068.

### 4.1 Función científica

B05 debe mapear `RQ → función → salida → unidad → métrica/protocolo → interpretación permitida` y mantener tres familias separadas:

- RQ1 / candidate retrieval;
- RQ2 / documentary evidence;
- RQ3 / controlled explanation.

RQ4 se mantiene como frontera de validez/robustez y no se desarrolla aquí más allá del enlace con 4.4/4.7.

### 4.2 Fronteras

- Candidate retrieval ≠ overall classification accuracy.
- Documentary coverage/association ≠ substantive normative/legal correctness.
- Auditability ≠ legal correctness.
- Automatic HE4 checks ≠ qualitative rubric.
- La evaluación cualitativa HE4 efectiva fue `AI_EXPERT_ROLE / LLM-as-judge`; no fue human scoring.
- Los resultados numéricos observados no pertenecen a 4.6.
- Inferencia, sensibilidad y robustez se reservan principalmente para 4.7.

## 5. Baselines B05

```text
BASELINE_MD = article/manuscript/ARTICLE_MASTER_V013.md
BASELINE_MD_SHA256 = 2e6b4446ffddb18940625a72a871a84a36405930b21db3dbba352c1535972f43
BASELINE_MD_GIT_BLOB = 06beaa052e2f1bcc630647040762fe78d3838a62
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V02.docx
BASELINE_DOCX_SHA256 = cff5520d5bc31af929abaf796048ef3b452627f8fef8e5f727c4f8cc661d222f
PRIOR_CITATION_COMMENTS = 40 / PRESERVE
```

Entregables esperados:

- `article/sections/experimental_design/Experimental_Design_B05_V01.md`;
- `ARTICLE_MASTER_CANDIDATE_EXPDES_B05_V01.md`;
- `ARTICLE_MASTER_CANDIDATE_EXPDES_B05_V01.docx`;
- `article/responses/5_EXPERIMENTAL_DESIGN_B05_SECTION4_6_RESPONSE_V01.md`.

## 6. Concurrencia experimental

Último corte sincronizado antes de abrir B05:

```text
SRC03_HEAD = 87422102290a4f9a89c51e936cf7274d8e4687d8
SRC03_PLAN_BLOB = cf587b61b7bfbc66dca310a7bb3b4d3f64671eea
DEVELOPMENT_MAIN = db0d0ad0d8435921a7838db6720eaea86a263763
```

La IA de Redacción debe re-verificar el corte vivo y evaluar cualquier drift por impacto material. El avance de flujos externos no abre automáticamente 4.7 ni Results.

## 7. Gate inmediato

```text
NEXT_ACTOR = IA_REDACCION
NEXT_ACTION = EXECUTE_ONLY_B05_SECTION_4_6_PROMPT_V01
EXPECTED_EXIT = EXECUTION_COMPLETED_PENDING_GESTORA_AUDIT
AUTHOR_APPROVAL_GATE = NOT_OPEN
B06 / SECTION_4_7 = NOT_AUTHORIZED
SECTION_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

---

# English

## 1. Current cumulative state

V013 is the verified canonical Markdown master. The current cumulative Word baseline is the approved B04 V02 DOCX in local author custody. B01–B04 are closed, approved, frozen, and integrated.

B05/Section 4.6 is now open only under `article/prompts/5_EXPERIMENTAL_DESIGN_B05_SECTION4_6.md@89a5e122c7ed6ab0ffe90a53e2a68e65830d6d99`, which passed independent prompt review and was authorized by D-068.

## 2. Scientific function and boundaries

B05 maps each RQ to system function, output, evaluation unit, metric/protocol, and permitted interpretation. RQ1 maps to candidate retrieval, RQ2 to documentary evidence, and RQ3 to controlled explanation. RQ4 remains a validity/robustness boundary linked to Sections 4.4 and 4.7.

Candidate retrieval is not overall classification accuracy; documentary association is not substantive normative/legal correctness; auditability is not legal correctness; automatic HE4 checks are distinct from the qualitative rubric; and the actual qualitative evaluator modality was AI-expert/LLM-as-judge, not human scoring. Observed results remain outside Section 4.6, and inferential/robustness procedures remain primarily in Section 4.7.

## 3. Exact baselines and gate

```text
BASELINE_MD = article/manuscript/ARTICLE_MASTER_V013.md
BASELINE_MD_GIT_BLOB = 06beaa052e2f1bcc630647040762fe78d3838a62
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B04_V02.docx
BASELINE_DOCX_SHA256 = cff5520d5bc31af929abaf796048ef3b452627f8fef8e5f727c4f8cc661d222f
CURRENT_GATE = EXPERIMENTAL_DESIGN_B05_SECTION_4_6_DRAFTING_V01
NEXT_ACTOR = DRAFTING_AI
EXPECTED_EXIT = EXECUTION_COMPLETED_PENDING_GESTORA_AUDIT
B06 / SECTION_4_7 = NOT_AUTHORIZED
SECTION_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```