# Plan maestro de redacción / Master Writing Plan

```text
PLAN_VERSION = V3.46
TARGET_JOURNAL = Knowledge-Based Systems
ARTICLE_TYPE = Research article
EDITORIAL_BASIS = KBS_EWG_34_V01
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
LATEST_EDITORIAL_DECISION = D-146
CANONICAL_MASTER = ARTICLE_MASTER_V028
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V028.md
CANONICAL_MASTER_MD_SHA256 = c154257a2c203e580372dd404df875ef808c325947ce580171e2e306961e568e
CANONICAL_MASTER_MD_GIT_BLOB = a261d0909cf64cb5554bf4e40d68cbcaf11aaf69
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_DISCUSSION_B05_V01.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = 109d5b28bbedeccd36ecc7f7f87e28fe6795c3d91498c483ea6bce818eb97291
CANONICAL_CITATION_COMMENTS = 48
CANONICAL_TRACKED_CHANGES = 0
CANONICAL_DOCX_PAGE_COUNT = 67
CURRENT_DRAFTING_PHASE = DISCUSSION
RESULTS_SECTIONS_5_1_TO_5_7 = CLOSED / APPROVED / FROZEN / INTEGRATED
DISCUSSION_B01_SECTION_6_1 = CLOSED / APPROVED / FROZEN / INTEGRATED
DISCUSSION_B02_SECTION_6_2 = CLOSED / APPROVED / FROZEN / INTEGRATED
DISCUSSION_B03_SECTION_6_3 = CLOSED / APPROVED / FROZEN / INTEGRATED
DISCUSSION_B04_SECTION_6_4 = CLOSED / APPROVED / FROZEN / INTEGRATED
DISCUSSION_B05_SECTION_6_5 = CLOSED / APPROVED / FROZEN / INTEGRATED
DISCUSSION_B05_INTEGRATION = D-144
DISCUSSION_B06_SECTION_6_6 = AUTHORIZED_FOR_EXECUTION
DISCUSSION_B06_BOUNDARY = D-145
DISCUSSION_B06_PROMPT = article/prompts/7_DISCUSSION_B06_SECTION6_6_V01.md
DISCUSSION_B06_PROMPT_GIT_BLOB = f01fb117ba583a99f283044a2e11c0151d6b61f9
DISCUSSION_B06_PROMPT_REVIEW = article/reviews/7_DISCUSSION_B06_SECTION6_6_PROMPT_INTERNAL_REVIEW_V01.md
DISCUSSION_B06_PROMPT_REVIEW_RESULT = PASS
DISCUSSION_B06_AUTHORIZATION = D-146
CURRENT_GATE = DISCUSSION_B06_V01_DRAFTING
AUTHOR_APPROVAL_GATE = NOT_OPEN
NEXT_ACTOR = IA_REDACCION
LEGACY_EDITORIAL_DEBT = DISCUSSION_B02_INTERNAL_TERMINOLOGY_HYGIENE
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

---

# Español

## 1. Estado acumulativo

`ARTICLE_MASTER_V028.md` es el master Markdown canónico. Results §5.1–§5.7 y Discussion §6.1–§6.5 están cerrados, aprobados, congelados e integrados.

El Word acumulativo canónico es:

```text
ARTICLE_MASTER_CANDIDATE_DISCUSSION_B05_V01.docx
SHA256 = 109d5b28bbedeccd36ecc7f7f87e28fe6795c3d91498c483ea6bce818eb97291
COMMENTS = 48
TRACKED_CHANGES = 0
PAGE_COUNT = 67
```

## 2. Secuencia vigente de Discussion

```text
6.1 Separating candidate ranking from documentary evidence = INTEGRATED
6.2 Controlled use of the LLM for explanation              = INTEGRATED / LEGACY EDITORIAL DEBT LOGGED
6.3 Comparison with prior work                             = INTEGRATED
6.4 Implications for auditable decision support            = INTEGRATED
6.5 Configurability and transfer conditions                = INTEGRATED
6.6 Limitations                                            = AUTHORIZED FOR EXECUTION / B06 V01
```

## 3. Boundary B06

D-145 delimita §6.6 a consolidar limitaciones ya demostradas o documentadas. La sección debe integrar: muestra purposiva y alcance Chapter 87; dependencia intra-DAM y similitud residual; sensibilidad conjunta a tamaño/composición del banco; comparaciones H150/H200 descriptivas; objetos de robustness no estimables; drift del corpus documental; evaluación cualitativa de 50 casos con LLM-as-judge y no humanos; incompatibilidad instrucción–esquema; configurabilidad sin generalización empírica; ausencia de validación legal/deployment; y estado aún incompleto del paquete público para reproducción one-command desde clean clone.

Relaciones obligatorias:

```text
DAM_DISJOINT_PARTITIONS != IID_OBSERVATIONS
EXP11A_SIZE_COMPOSITION_SENSITIVITY != ISOLATED_CAUSAL_SIZE_EFFECT
EXP11B_DESCRIPTIVE != SEED_SUPERPOPULATION_INFERENCE
EXP12_DIVERSITY_EFFECT = NOT_ESTIMABLE
HE5 = INCONCLUSIVE
DOCUMENTARY_ASSOCIATION != SUBSTANTIVE_NORMATIVE_CORRECTNESS
AUDITABILITY != LEGAL_CORRECTNESS
LLM_AS_JUDGE != HUMAN_VALIDATION
CONFIGURABILITY != EMPIRICAL_GENERALIZATION
```

No se autorizan nueva literatura, citas, resultados, cálculos, inferencias, causalidad, novelty, SOTA, superioridad, deployment readiness, legal validity ni external generalization.

## 4. Prompt y autorización

Prompt activo:

`article/prompts/7_DISCUSSION_B06_SECTION6_6_V01.md@395d368e5cb91e2d972f7c804a9f6801d15a53b7`

Git blob:

`f01fb117ba583a99f283044a2e11c0151d6b61f9`

Review:

`article/reviews/7_DISCUSSION_B06_SECTION6_6_PROMPT_INTERNAL_REVIEW_V01.md@5ae0180b5890387265076a3bb58164fdb82e6ef7` — `PASS`.

Autorización:

`article/governance/D146_DISCUSSION_B06_SECTION6_6_EXECUTION_AUTHORIZATION.md@725fc66690b4f46a0d78879a29e6a4e1aa6b1b0f`.

## 5. Estándar acumulativo de auditoría

MWDP v1.0, SPCCR v1.0, KBS_EWG_34_V01 y D-136 permanecen vinculantes. El `PASS` posterior exige fidelidad científica, correspondencia claim-evidencia, fuerza epistémica correcta, coherencia con Methods/Results/Discussion, ausencia de invención/overclaiming, terminología reader-facing, prosa concreta, naturalidad bilingüe, integridad de citas, Word/OOXML, comentarios y render.

La deuda editorial heredada de §6.2 permanece fuera de B06 y debe resolverse mediante un gate transversal controlado antes del freeze final.

## 6. Gate inmediato

```text
NEXT_ACTOR = IA_REDACCION
NEXT_ACTION = EXECUTE_DISCUSSION_B06_V01_ONLY
PROMPT = article/prompts/7_DISCUSSION_B06_SECTION6_6_V01.md
PROMPT_GIT_BLOB = f01fb117ba583a99f283044a2e11c0151d6b61f9
AUTHORIZATION = D-146
BASELINE_MD = article/manuscript/ARTICLE_MASTER_V028.md
BASELINE_MD_SHA256 = c154257a2c203e580372dd404df875ef808c325947ce580171e2e306961e568e
BASELINE_MD_GIT_BLOB = a261d0909cf64cb5554bf4e40d68cbcaf11aaf69
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_DISCUSSION_B05_V01.docx
BASELINE_DOCX_SHA256 = 109d5b28bbedeccd36ecc7f7f87e28fe6795c3d91498c483ea6bce818eb97291
EXPECTED_COMMENTS = 48
EXPECTED_TRACKED_CHANGES = 0
EXPECTED_EXIT = DISCUSSION_B06_V01_COMPLETED_PENDING_GESTORA_AUDIT
CONCLUSION = NOT_AUTHORIZED
```

---

# English

V028 is canonical. Results §5.1–§5.7 and Discussion §6.1–§6.5 are integrated. D-145 bounds Section 6.6 to consolidation of already established limitations; the reviewed B06 V01 prompt is authorized by D-146.

```text
PLAN_VERSION = V3.46
DISCUSSION_B06 = AUTHORIZED_FOR_EXECUTION
CURRENT_GATE = DISCUSSION_B06_V01_DRAFTING
NEXT_ACTOR = IA_REDACCION
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```