# Plan maestro de redacción / Master Writing Plan

```text
PLAN_VERSION = V3.43
TARGET_JOURNAL = Knowledge-Based Systems
ARTICLE_TYPE = Research article
EDITORIAL_BASIS = KBS_EWG_34_V01
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
LATEST_EDITORIAL_DECISION = D-139
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
DISCUSSION_B04_V01 = PASS_WITH_CORRECTIONS / SUPERSEDED_BY_V02
DISCUSSION_B04_V02 = AUDITED / PASS / AUTHOR_APPROVED
DISCUSSION_B04_INTEGRATION = BLOCKED_PENDING_V027_PATH_CORRECTION
EXPECTED_V027_PATH = article/manuscript/ARTICLE_MASTER_V027.md
EXPECTED_V027_SHA256 = d27b6ed30fcbe6ff47b78e79cf5e78affcbf285ddaecfbe94366c63208e4c69b
EXPECTED_V027_GIT_BLOB = ac5b71788a85a4bad7b475e5d099b3e57370b71e
OBSERVED_V027_PATH = article/ARTICLE_MASTER_V027.md
OBSERVED_V027_GIT_BLOB = ac5b71788a85a4bad7b475e5d099b3e57370b71e
V027_CONTENT_IDENTITY = PASS / BYTE_EXACT
V027_PATH_CONFORMANCE = FAIL
CURRENT_GATE = DISCUSSION_B04_V027_PATH_CORRECTION
AUTHOR_APPROVAL_GATE = CLOSED / APPROVED
NEXT_ACTOR = AUTHOR
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

Discussion §6.4 / B04 V02 fue reaudited con `PASS` y aprobado explícitamente por el autor. El candidato aprobado conserva:

```text
ARTICLE_MASTER_CANDIDATE_DISCUSSION_B04_V02.md
SHA256 = d27b6ed30fcbe6ff47b78e79cf5e78affcbf285ddaecfbe94366c63208e4c69b
GIT_BLOB = ac5b71788a85a4bad7b475e5d099b3e57370b71e

ARTICLE_MASTER_CANDIDATE_DISCUSSION_B04_V02.docx
SHA256 = 6e8bef5440c8a971d51cda6a3d1fc85e1b4793e83eb51ff3d8a7e2fa1a702b92
COMMENTS = 48
TRACKED_CHANGES = 0
PAGE_COUNT = 66
```

## 2. Verificación de promoción V027

D-138 fijó la promoción aprobada en:

```text
article/manuscript/ARTICLE_MASTER_V027.md
```

El autor subió un archivo byte-exacto en el commit `e036ce10ef723f0ae51c880a18953c44cea8f389`, pero la ruta observada es:

```text
article/ARTICLE_MASTER_V027.md
GIT_BLOB = ac5b71788a85a4bad7b475e5d099b3e57370b71e
```

La identidad de contenido pasa, pero la ubicación no coincide con el destino canónico. D-139 registra:

```text
CONTENT_IDENTITY = PASS / BYTE_EXACT
PATH_CONFORMANCE = FAIL
PROMOTION = BLOCKED_PENDING_PATH_CORRECTION
```

No se debe editar ni regenerar el contenido. Debe materializarse el mismo archivo en `article/manuscript/ARTICLE_MASTER_V027.md`. Tras verificar allí el mismo Git blob, IA Gestora podrá cerrar B04 como `CLOSED / APPROVED / FROZEN / INTEGRATED`, promover V027 a canónico y continuar con el siguiente bloque.

## 3. Secuencia vigente de Discussion

```text
6.1 Separating candidate ranking from documentary evidence = INTEGRATED
6.2 Controlled use of the LLM for explanation              = INTEGRATED / LEGACY EDITORIAL DEBT LOGGED
6.3 Comparison with prior work                             = INTEGRATED
6.4 Implications for auditable decision support            = AUTHOR APPROVED / PATH CORRECTION REQUIRED
6.5 Configurability and transfer conditions                = NOT AUTHORIZED
6.6 Limitations                                            = NOT AUTHORIZED
```

## 4. Estándar acumulativo de auditoría

D-136 permanece vinculante. Un `PASS` exige fidelidad científica, fuerza epistémica correcta, coherencia argumental, ausencia de invenciones/overclaiming, terminología reader-facing, concreción SPCCR, adecuación KBS, naturalidad bilingüe, citas válidas e integridad técnica. La verificación de SHA/commit/OOXML es necesaria pero no sustituye la auditoría científica/editorial.

La deuda editorial heredada de §6.2 sigue registrada para un gate transversal antes del freeze final y no se corrige silenciosamente durante B04/B05.

## 5. Gate inmediato

```text
NEXT_ACTOR = AUTHOR
NEXT_ACTION = MATERIALIZE_BYTE_EXACT_V027_AT_EXPECTED_PATH
EXPECTED_PATH = article/manuscript/ARTICLE_MASTER_V027.md
EXPECTED_SHA256 = d27b6ed30fcbe6ff47b78e79cf5e78affcbf285ddaecfbe94366c63208e4c69b
EXPECTED_GIT_BLOB = ac5b71788a85a4bad7b475e5d099b3e57370b71e
CANONICAL_MASTER = ARTICLE_MASTER_V026
DISCUSSION_B05_PLUS = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
```

---

# English

V026 remains the canonical master. Discussion B04 V02 has passed substantive re-audit and has been explicitly approved by the author. The uploaded V027 content is byte-exact to the approved candidate, but it was materialized at `article/ARTICLE_MASTER_V027.md` instead of the governed canonical target `article/manuscript/ARTICLE_MASTER_V027.md`.

```text
PLAN_VERSION = V3.43
DISCUSSION_B04_V02 = AUDITED / PASS / AUTHOR_APPROVED
V027_CONTENT_IDENTITY = PASS / BYTE_EXACT
V027_PATH_CONFORMANCE = FAIL
CURRENT_GATE = DISCUSSION_B04_V027_PATH_CORRECTION
NEXT_ACTOR = AUTHOR
DISCUSSION_B05_PLUS = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

After the exact same blob is materialized at the expected path and reverified, IA Gestora may close B04, promote V027 to canonical status, and prepare the next authorized Discussion block.