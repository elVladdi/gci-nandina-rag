# Plan maestro de redacción / Master Writing Plan

```text
PLAN_VERSION = V3.44
TARGET_JOURNAL = Knowledge-Based Systems
ARTICLE_TYPE = Research article
EDITORIAL_BASIS = KBS_EWG_34_V01
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
LATEST_EDITORIAL_DECISION = D-142
CANONICAL_MASTER = ARTICLE_MASTER_V027
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V027.md
CANONICAL_MASTER_MD_SHA256 = d27b6ed30fcbe6ff47b78e79cf5e78affcbf285ddaecfbe94366c63208e4c69b
CANONICAL_MASTER_MD_GIT_BLOB = ac5b71788a85a4bad7b475e5d099b3e57370b71e
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_DISCUSSION_B04_V02.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = 6e8bef5440c8a971d51cda6a3d1fc85e1b4793e83eb51ff3d8a7e2fa1a702b92
CANONICAL_CITATION_COMMENTS = 48
CANONICAL_TRACKED_CHANGES = 0
CANONICAL_DOCX_PAGE_COUNT = 66
CURRENT_DRAFTING_PHASE = DISCUSSION
RESULTS_SECTIONS_5_1_TO_5_7 = CLOSED / APPROVED / FROZEN / INTEGRATED
DISCUSSION_B01_SECTION_6_1 = CLOSED / APPROVED / FROZEN / INTEGRATED
DISCUSSION_B02_SECTION_6_2 = CLOSED / APPROVED / FROZEN / INTEGRATED
DISCUSSION_B03_SECTION_6_3 = CLOSED / APPROVED / FROZEN / INTEGRATED
DISCUSSION_B04_SECTION_6_4 = CLOSED / APPROVED / FROZEN / INTEGRATED
DISCUSSION_B05_SECTION_6_5 = AUTHORIZED_FOR_EXECUTION
DISCUSSION_B05_BOUNDARY = D-141
DISCUSSION_B05_PROMPT = article/prompts/7_DISCUSSION_B05_SECTION6_5_V01.md
DISCUSSION_B05_PROMPT_GIT_BLOB = 54b5da0ad1274ec00664cf0bef550485f794822a
DISCUSSION_B05_PROMPT_REVIEW_RESULT = PASS
DISCUSSION_B05_AUTHORIZATION = D-142
CURRENT_GATE = DISCUSSION_B05_V01_DRAFTING
AUTHOR_APPROVAL_GATE = NOT_OPEN
NEXT_ACTOR = IA_REDACCION
LEGACY_EDITORIAL_DEBT = DISCUSSION_B02_INTERNAL_TERMINOLOGY_HYGIENE
DISCUSSION_B06 = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

---

# Español

## 1. Estado acumulativo

`ARTICLE_MASTER_V027.md` es el master Markdown canónico después de la promoción byte-exact verificada por D-140. Results §5.1–§5.7 y Discussion §6.1–§6.4 están cerrados, aprobados, congelados e integrados.

El Word acumulativo canónico es:

```text
ARTICLE_MASTER_CANDIDATE_DISCUSSION_B04_V02.docx
SHA256 = 6e8bef5440c8a971d51cda6a3d1fc85e1b4793e83eb51ff3d8a7e2fa1a702b92
COMMENTS = 48
TRACKED_CHANGES = 0
PAGE_COUNT = 66
```

## 2. Secuencia vigente de Discussion

```text
6.1 Separating candidate ranking from documentary evidence = INTEGRATED
6.2 Controlled use of the LLM for explanation              = INTEGRATED / LEGACY EDITORIAL DEBT LOGGED
6.3 Comparison with prior work                             = INTEGRATED
6.4 Implications for auditable decision support            = INTEGRATED
6.5 Configurability and transfer conditions                = AUTHORIZED FOR EXECUTION / B05 V01
6.6 Limitations                                            = NOT AUTHORIZED
```

## 3. Boundary B05

D-141 delimita §6.5 a la interpretación de configurabilidad y transferencia como reinstanciación condicional. Deben preservarse interfaces y procedencia: consulta reproducible, histórico vinculado a códigos, ranking trazable, Top-3 fijado antes de downstream, evidencia candidate-linked, contexto con procedencia y generador restringido a explicación.

La sección debe mantener:

```text
CONFIGURABILITY != EMPIRICAL_GENERALIZATION
INTERFACE_COMPATIBILITY != PERFORMANCE_GENERALIZATION
REPRODUCTION != EXTERNAL_REPLICATION
REINSTANTIATION != DEPLOYMENT_READINESS
REINSTANTIATION != LEGAL_VALIDITY
```

No se autorizan nueva literatura, citas, resultados, inferencias, novelty, SOTA, superioridad, transferencia automática de métricas ni generalización fuera del benchmark Chapter 87.

## 4. Prompt y autorización

Prompt activo:

`article/prompts/7_DISCUSSION_B05_SECTION6_5_V01.md@c93ed03ce2c8fe90659099ff80984d99bcaa01b3`

Git blob:

`54b5da0ad1274ec00664cf0bef550485f794822a`

Review:

`article/reviews/7_DISCUSSION_B05_SECTION6_5_PROMPT_INTERNAL_REVIEW_V01.md@ae6c71e2512458fecd2a92976bd22c933b3e9557` — `PASS`.

Autorización:

`article/governance/D142_DISCUSSION_B05_SECTION6_5_EXECUTION_AUTHORIZATION.md@7d946385ed2eb18e5d7654520d1b2dc726964d4a`.

## 5. Estándar acumulativo de auditoría

MWDP v1.0, SPCCR v1.0, KBS_EWG_34_V01 y D-136 permanecen vinculantes. El `PASS` posterior deberá verificar contenido científico/editorial real además de identidades técnicas: fidelidad, fuerza epistémica, coherencia, no invención/overclaiming, terminología reader-facing, concreción, naturalidad bilingüe, citas, Word/OOXML y render.

La deuda editorial heredada de §6.2 permanece fuera de B05 y requerirá un gate transversal controlado antes del freeze final.

## 6. Gate inmediato

```text
NEXT_ACTOR = IA_REDACCION
NEXT_ACTION = EXECUTE_DISCUSSION_B05_V01_ONLY
PROMPT = article/prompts/7_DISCUSSION_B05_SECTION6_5_V01.md
PROMPT_GIT_BLOB = 54b5da0ad1274ec00664cf0bef550485f794822a
AUTHORIZATION = D-142
BASELINE_MD = article/manuscript/ARTICLE_MASTER_V027.md
BASELINE_MD_SHA256 = d27b6ed30fcbe6ff47b78e79cf5e78affcbf285ddaecfbe94366c63208e4c69b
BASELINE_MD_GIT_BLOB = ac5b71788a85a4bad7b475e5d099b3e57370b71e
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_DISCUSSION_B04_V02.docx
BASELINE_DOCX_SHA256 = 6e8bef5440c8a971d51cda6a3d1fc85e1b4793e83eb51ff3d8a7e2fa1a702b92
EXPECTED_COMMENTS = 48
EXPECTED_TRACKED_CHANGES = 0
EXPECTED_EXIT = DISCUSSION_B05_V01_COMPLETED_PENDING_GESTORA_AUDIT
DISCUSSION_B06 = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
```

---

# English

V027 is the canonical master. Results §5.1–§5.7 and Discussion §6.1–§6.4 are closed, approved, frozen, and integrated. D-141 bounds Section 6.5 to configurability and transfer as conditional re-instantiation under preserved interfaces and provenance; it expressly excludes empirical generalization or performance transfer. The B05 prompt passed internal review and D-142 authorizes only B05 V01.

```text
PLAN_VERSION = V3.44
CURRENT_GATE = DISCUSSION_B05_V01_DRAFTING
NEXT_ACTOR = IA_REDACCION
ACTIVE_PROMPT = article/prompts/7_DISCUSSION_B05_SECTION6_5_V01.md
DISCUSSION_B05 = AUTHORIZED_FOR_EXECUTION
DISCUSSION_B06 = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```