# Plan maestro de redacción / Master Writing Plan

```text
PLAN_VERSION = V3.41
TARGET_JOURNAL = Knowledge-Based Systems
ARTICLE_TYPE = Research article
EDITORIAL_BASIS = KBS_EWG_34_V01
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
LATEST_EDITORIAL_DECISION = D-137
CANONICAL_MASTER = ARTICLE_MASTER_V026
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V026.md
CANONICAL_MASTER_MD_SHA256 = 76107b20419329ef7a5c6643fec892fbdc0e0779c1ab58f6de41bc36711f4156
CANONICAL_MASTER_MD_GIT_BLOB = f6a63be554317e62103aa96c1091f4039249e5ee
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_DISCUSSION_B03_V01.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = bd57ee1242222fbb25e41c47cc6dd7417ea245af87e3034a5a34a6ea78656b57
CANONICAL_CITATION_COMMENTS = 48
CURRENT_DRAFTING_PHASE = DISCUSSION
RESULTS_SECTIONS_5_1_TO_5_7 = CLOSED / APPROVED / FROZEN / INTEGRATED
DISCUSSION_B01_SECTION_6_1 = CLOSED / APPROVED / FROZEN / INTEGRATED
DISCUSSION_B02_SECTION_6_2 = CLOSED / APPROVED / FROZEN / INTEGRATED
DISCUSSION_B03_SECTION_6_3 = CLOSED / APPROVED / FROZEN / INTEGRATED
DISCUSSION_B04_V01 = PASS_WITH_CORRECTIONS
DISCUSSION_B04_V02 = AUTHORIZED_FOR_NARROW_CORRECTION
CURRENT_GATE = DISCUSSION_B04_V02_NARROW_CORRECTION
AUTHOR_APPROVAL_GATE = NOT_OPEN
NEXT_ACTOR = IA_REDACCION
LEGACY_EDITORIAL_DEBT = DISCUSSION_B02_INTERNAL_TERMINOLOGY_HYGIENE
DISCUSSION_B05_PLUS = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

---

# Español

## 1. Estado acumulativo

`ARTICLE_MASTER_V026.md` continúa como master Markdown canónico. Results §5.1–§5.7 y Discussion §6.1–§6.3 están cerrados, aprobados, congelados e integrados.

El Word acumulativo canónico permanece:

```text
ARTICLE_MASTER_CANDIDATE_DISCUSSION_B03_V01.docx
SHA256 = bd57ee1242222fbb25e41c47cc6dd7417ea245af87e3034a5a34a6ea78656b57
COMMENTS = 48
TRACKED_CHANGES = 0
PAGE_COUNT = 64
```

## 2. Secuencia vigente de Discussion

```text
6.1 Separating candidate ranking from documentary evidence = INTEGRATED
6.2 Controlled use of the LLM for explanation              = INTEGRATED / LEGACY EDITORIAL DEBT LOGGED
6.3 Comparison with prior work                             = INTEGRATED
6.4 Implications for auditable decision support            = V01 PASS WITH CORRECTIONS / V02 AUTHORIZED
6.5 Configurability and transfer conditions                = NOT AUTHORIZED
6.6 Limitations                                            = NOT AUTHORIZED
```

## 3. Auditoría sustantiva B04 V01

IA Redacción completó B04 V01 y versionó la response en:

`article/responses/7_DISCUSSION_B04_SECTION6_4_RESPONSE_V01.md@e27f03b3d4103a3436fe26566a97a22c974ce57c`.

El bloque redactado es:

`article/sections/discussion/Discussion_B04_V01.md@3f8749234d3535fb7ccdf8d1546295160c64e3d0`.

IA Gestora realizó auditoría sustantiva/editorial bajo `MWDP_V1.0`, `SPCCR_V1.0`, `KBS_EWG_34_V01` y la aclaración autoral formalizada en D-136:

`article/governance/D136_SUBSTANTIVE_EDITORIAL_AUDIT_AND_INTERNAL_TERMINOLOGY_CONTROL.md@e845725f48448e13987f785dc646bc533d7b5854`.

Review:

`article/reviews/7_DISCUSSION_B04_SECTION6_4_INTERNAL_REVIEW_V01.md@29fa044040c4b061641e711b7a4b906d3b51cb6b`.

```text
B04_V01_VERDICT = PASS WITH CORRECTIONS
SCIENTIFIC_CORE = PASS
NUMERICAL_GROUND_TRUTH = PASS
PROHIBITED_SCIENTIFIC_CLAIMS = NONE
INTERNAL_TERMINOLOGY_LEAKAGE = CORRECTION_REQUIRED
RETRIEVER_RATIONALE_OVERSTATEMENT = CORRECTION_REQUIRED
SPANISH_NATURALNESS = CORRECTION_REQUIRED
AUTHOR_APPROVAL_GATE = NOT_OPEN
```

El bloque conserva correctamente las cifras y límites de D-133, pero no pasa aún a gate autoral porque la prosa publicable contiene identificadores internos de implementación/QA, voz de gobernanza interna y una formulación que podría interpretarse como explicación de por qué el recuperador produjo una posición determinada. La corrección debe preservar el hallazgo científico y retirar la capa de lenguaje interno.

## 4. Corrección B04 V02 autorizada

Prompt activo:

`article/prompts/7_DISCUSSION_B04_V01_NARROW_EDITORIAL_PRECISION_CORRECTION.md@660768b25ae639185181e22433213a1886e13bfd`

Git blob:

`398a87aafb3627abc54f50abd9c51a1be59898ec`

Review del prompt:

`article/reviews/7_DISCUSSION_B04_V01_NARROW_EDITORIAL_PRECISION_CORRECTION_PROMPT_REVIEW_V01.md@68e15b98c4451c9af803691ff592f33540f2ca75` — `PASS`.

Autorización:

`article/governance/D137_DISCUSSION_B04_V02_NARROW_CORRECTION_EXECUTION_AUTHORIZATION.md@6d759785c1ba511056c8ced806aba5266c919aa8`.

Inputs exactos requeridos:

```text
ARTICLE_MASTER_CANDIDATE_DISCUSSION_B04_V01.md
SHA256 = bfd15b2a3d28278b317a028e9cff0baeef8458ada5f8083f1b54cf267dd0d0ac

ARTICLE_MASTER_CANDIDATE_DISCUSSION_B04_V01.docx
SHA256 = 8abb1dc3ca1885066be8588db328121eca907447faf5959be3f1b2d89d193b8b
COMMENTS = 48
TRACKED_CHANGES = 0
```

La V02 debe modificar exclusivamente §6.4 EN/ES. No puede corregir §6.2 ni ningún bloque previamente integrado.

## 5. Estándar acumulativo de auditoría

A partir de D-136, un `PASS` exige simultáneamente fidelidad científica, fuerza epistémica correcta, coherencia argumental, ausencia de invenciones y overclaiming, terminología reader-facing sin filtración de identificadores internos, concreción SPCCR, adecuación KBS, naturalidad bilingüe, citas válidas e integridad técnica. SHA/commit/OOXML son controles necesarios, no sustituyen la auditoría científica/editorial.

La revisión de B04 detectó además deuda editorial heredada en §6.2 por etiquetas internas ya integradas. Se registra para un gate transversal controlado antes del freeze final; no se autoriza edición silenciosa durante B04.

## 6. Gate inmediato

```text
NEXT_ACTOR = IA_REDACCION
NEXT_ACTION = EXECUTE_DISCUSSION_B04_V02_NARROW_CORRECTION_ONLY
PROMPT = article/prompts/7_DISCUSSION_B04_V01_NARROW_EDITORIAL_PRECISION_CORRECTION.md
PROMPT_GIT_BLOB = 398a87aafb3627abc54f50abd9c51a1be59898ec
AUTHORIZATION = D-137
INPUT_CANDIDATE_MD = ARTICLE_MASTER_CANDIDATE_DISCUSSION_B04_V01.md
INPUT_CANDIDATE_MD_SHA256 = bfd15b2a3d28278b317a028e9cff0baeef8458ada5f8083f1b54cf267dd0d0ac
INPUT_CANDIDATE_DOCX = ARTICLE_MASTER_CANDIDATE_DISCUSSION_B04_V01.docx
INPUT_CANDIDATE_DOCX_SHA256 = 8abb1dc3ca1885066be8588db328121eca907447faf5959be3f1b2d89d193b8b
EXPECTED_COMMENTS = 48
EXPECTED_TRACKED_CHANGES = 0
EXPECTED_EXIT = DISCUSSION_B04_V02_COMPLETED_PENDING_GESTORA_REAUDIT
DISCUSSION_B05_PLUS = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
```

---

# English

V026 remains the canonical master. Discussion B04 V01 has been substantively audited, not merely checksum-checked. Its scientific core and authorized metrics pass, but the block requires a narrow V02 correction for retrieval-rationale overstatement, internal implementation/QA terminology leakage, internal-governance voice, and Spanish naturalness.

D-136 formalizes the cumulative audit standard: scientific fidelity, epistemic strength, coherence, no invention/overclaiming, reader-facing terminology, SPCCR concreteness, KBS editorial fit, bilingual naturalness, citation validity, and technical integrity are all required for `PASS`. D-137 authorizes only the B04 V02 correction.

```text
PLAN_VERSION = V3.41
CURRENT_GATE = DISCUSSION_B04_V02_NARROW_CORRECTION
NEXT_ACTOR = IA_REDACCION
ACTIVE_PROMPT = article/prompts/7_DISCUSSION_B04_V01_NARROW_EDITORIAL_PRECISION_CORRECTION.md
DISCUSSION_B04_V01 = PASS_WITH_CORRECTIONS
DISCUSSION_B04_V02 = AUTHORIZED_FOR_EXECUTION
DISCUSSION_B05_PLUS = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```