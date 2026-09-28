# Plan maestro de redacción / Master Writing Plan

```text
PLAN_VERSION = V3.35
TARGET_JOURNAL = Knowledge-Based Systems
ARTICLE_TYPE = Research article
EDITORIAL_BASIS = KBS_EWG_34_V01
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
LATEST_EDITORIAL_DECISION = D-126
CANONICAL_MASTER = ARTICLE_MASTER_V024
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V024.md
CANONICAL_MASTER_MD_SHA256 = 0b6ea338cf325c1c59e23f91633791f97868c91eeaea44cca89f8d65c6ee7864
CANONICAL_MASTER_MD_GIT_BLOB = d0ecf9f4a44b8900dd1b65f289fb0b2abf6d29c0
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_DISCUSSION_B01_V01.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = cc0bb87adacbfbca7403335f6a1070acf27f04b05c2d6a8772b0608c3923f0e0
CANONICAL_CITATION_COMMENTS = 42
CURRENT_DRAFTING_PHASE = DISCUSSION
RESULTS_SECTIONS_5_1_TO_5_7 = CLOSED / APPROVED / FROZEN / INTEGRATED
DISCUSSION_B01_SECTION_6_1 = CLOSED / APPROVED / FROZEN / INTEGRATED
DISCUSSION_B02_SECTION_6_2 = OPEN / AUTHORIZED_FOR_DRAFTING
CURRENT_GATE = DISCUSSION_B02_SECTION_6_2_DRAFTING_V01
AUTHOR_APPROVAL_GATE = NOT_OPEN
DISCUSSION_B03_PLUS = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

---

# Español

## 1. Estado acumulativo

`ARTICLE_MASTER_V024.md` es el master Markdown canónico verificado. Results §5.1–§5.7 y Discussion §6.1 están cerrados, aprobados, congelados e integrados.

La promoción B01 a V024 fue byte-exacta y está registrada en:

`article/governance/D124_DISCUSSION_B01_AUTHOR_APPROVAL_V024_VERIFICATION_AND_INTEGRATION.md@e59007e8d235c63ab67c5a5d34a7ca6c1addb918`.

El Word acumulativo canónico es:

```text
ARTICLE_MASTER_CANDIDATE_DISCUSSION_B01_V01.docx
SHA256 = cc0bb87adacbfbca7403335f6a1070acf27f04b05c2d6a8772b0608c3923f0e0
COMMENTS = 42
TRACKED_CHANGES = 0
PAGE_COUNT = 60
```

## 2. Secuencia vigente de Discussion

```text
6.1 Separating candidate ranking from documentary evidence = INTEGRATED
6.2 Controlled use of the LLM for explanation              = AUTHORIZED B02 V01
6.3 Comparison with prior work                             = NOT AUTHORIZED
6.4 Implications for auditable decision support            = NOT AUTHORIZED
6.5 Configurability and transfer conditions                = NOT AUTHORIZED
6.6 Limitations                                            = NOT AUTHORIZED
```

## 3. Discussion B02 / Section 6.2

Boundary:

`article/governance/D125_DISCUSSION_B02_SECTION6_2_INTERPRETIVE_BOUNDARY_AND_LITERATURE_TRACE.md@ecc20192dd87d168dc49bac2935cc73b2de4dc1a`

Prompt:

`article/prompts/7_DISCUSSION_B02_SECTION6_2.md@4c54ca73d4886e7b5885727f9bd46b77d64580d8`

Git blob:

`2f4ac3dbb8175116b31127b03c402ca8bd147822`

Revisión:

`article/reviews/7_DISCUSSION_B02_SECTION6_2_PROMPT_INTERNAL_REVIEW_V01.md@4025791c3fce6d0e3fabea38b94bcda9cc2a11e3` — `PASS`.

Autorización:

`article/governance/D126_DISCUSSION_B02_SECTION6_2_EXECUTION_AUTHORIZATION.md@73b736ff9e95e244bbbde56b48853f1350cf5714`.

## 4. Contrato científico B02

§6.2 debe interpretar el LLM como componente downstream de explicación sin autoridad para modificar candidatos. La evidencia integrada obliga a mantener simultáneamente:

```text
STRUCTURAL_PRESERVATION = 50/50 CASES
SLOT_LEVEL_CONTROLS = 150/150 SLOTS
QUALITATIVE_AUDITABILITY = 28/50 = 56.0%
VERIFIABILITY_MEAN = 0.54/2
HISTORICAL_NORMATIVE_SEPARATION_MEAN = 1.04/2
SCHEMA_COMPLIANCE = 0/50 / PROMPT_SCHEMA_SPECIFICATION_MISMATCH ONLY
QUALITATIVE_EVALUATOR = LLM_AS_JUDGE / NOT HUMAN
```

La interpretación autorizada es que restringir la autoridad del LLM permite preservar atribución entre componentes y controlar invariantes del pipeline, pero no garantiza por sí sola calidad explicativa, verificabilidad, reducción de alucinaciones, seguridad, corrección jurídica ni fidelidad causal.

El contraste de literatura se limita a Marra de Artiñano et al. (2023), como ejemplo de clasificación generativa directa, y Kim et al. (2025), como ejemplo de clasificación HS condicionada por recuperación. La diferencia se expresa únicamente en términos de autoridad y secuenciación funcional del LLM.

## 5. Política Word y citas

El baseline Word tiene 42 comentarios. B02 debe introducir exactamente dos nuevas citas en la Parte I inglesa —Marra de Artiñano et al. (2023) y Kim et al. (2025)— y exactamente dos nuevos comentarios de fuente. El candidato esperado debe contener:

```text
COMMENTS = 44
TRACKED_CHANGES = 0
```

Los 42 comentarios heredados deben preservarse sin modificación. D-035 continúa activo y Word no debe reconstruirse desde Markdown.

## 6. Gate inmediato

```text
NEXT_ACTOR = IA_REDACCION
NEXT_ACTION = EXECUTE_ONLY_DISCUSSION_B02_SECTION_6_2
BASELINE_MASTER_MD = article/manuscript/ARTICLE_MASTER_V024.md
BASELINE_MASTER_MD_SHA256 = 0b6ea338cf325c1c59e23f91633791f97868c91eeaea44cca89f8d65c6ee7864
BASELINE_MASTER_MD_GIT_BLOB = d0ecf9f4a44b8900dd1b65f289fb0b2abf6d29c0
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_DISCUSSION_B01_V01.docx
BASELINE_DOCX_SHA256 = cc0bb87adacbfbca7403335f6a1070acf27f04b05c2d6a8772b0608c3923f0e0
EXPECTED_COMMENTS = 44
EXPECTED_MASTER_MD = ARTICLE_MASTER_CANDIDATE_DISCUSSION_B02_V01.md
EXPECTED_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_DISCUSSION_B02_V01.docx
EXPECTED_SECTION = article/sections/discussion/Discussion_B02_V01.md
EXPECTED_RESPONSE = article/responses/7_DISCUSSION_B02_SECTION6_2_RESPONSE_V01.md
EXPECTED_EXIT = DISCUSSION_B02_V01_COMPLETED_PENDING_GESTORA_AUDIT
DISCUSSION_B03_PLUS = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
```

---

# English

V024 is canonical and verified. Discussion B01 is integrated. Discussion B02 / Section 6.2 is the only open drafting block. It must interpret the explanation-only role of the local LLM while preserving the distinction between structural preservation and partial qualitative auditability. Functional literature comparison is limited to Marra de Artiñano et al. (2023) and Kim et al. (2025). Exactly two new English citation comments are authorized, taking the cumulative Word count from 42 to 44. No Section 6.3+, Conclusion, novelty, causal safety, hallucination-reduction, superiority, human-validation, legal-correctness, or faithful-causal-explanation claim is authorized.

```text
CURRENT_GATE = DISCUSSION_B02_SECTION_6_2_DRAFTING_V01
NEXT_ACTOR = IA_REDACCION
DISCUSSION_B02 = AUTHORIZED
DISCUSSION_B03_PLUS = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```