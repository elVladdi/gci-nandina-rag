# Plan maestro de redacción / Master Writing Plan

```text
PLAN_VERSION = V3.42
TARGET_JOURNAL = Knowledge-Based Systems
ARTICLE_TYPE = Research article
EDITORIAL_BASIS = KBS_EWG_34_V01
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
LATEST_EDITORIAL_DECISION = D-138
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
DISCUSSION_B04_V02 = AUDITED / PASS / PENDING_AUTHOR_APPROVAL
CURRENT_GATE = DISCUSSION_B04_V02_AUTHOR_APPROVAL
AUTHOR_APPROVAL_GATE = OPEN
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

El Word acumulativo canónico permanece, hasta aprobación de B04:

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
6.4 Implications for auditable decision support            = V02 AUDITED / PASS / PENDING AUTHOR APPROVAL
6.5 Configurability and transfer conditions                = NOT AUTHORIZED
6.6 Limitations                                            = NOT AUTHORIZED
```

## 3. Historial B04

B04 V01 fue redactado y auditado sustantivamente bajo MWDP, SPCCR, KBS_EWG_34_V01 y D-136. El resultado fue `PASS WITH CORRECTIONS` por cuatro familias de defectos: sobreinterpretación de la rationale del recuperador, filtración de terminología interna de QA/implementación, voz de gobernanza interna y naturalidad insuficiente del español.

D-137 autorizó una corrección estrecha V02 sin alterar el boundary científico D-133, sin nueva literatura/citas/resultados y sin tocar §6.2 ni otros bloques integrados.

## 4. B04 V02 ejecutado y reaudited

Response de IA Redacción:

`article/responses/7_DISCUSSION_B04_SECTION6_4_RESPONSE_V02.md@66df19f0d5a7ec5febfea7ecae4fd7121b774eec`.

Bloque V02:

`article/sections/discussion/Discussion_B04_V02.md@8d301d519bcd8275a085d5c0fa96f80c073c7c7d`.

Identidades candidatas:

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

Review independiente de IA Gestora:

`article/reviews/7_DISCUSSION_B04_SECTION6_4_INTERNAL_REVIEW_V02.md@7addbe4fc7719e64ebead5326ed9370db45bc6dc`.

```text
B04_V02_VERDICT = PASS
SCIENTIFIC_CORE = PASS
NUMERICAL_GROUND_TRUTH = PASS
CLAIM_STRENGTH_EVIDENCE_MATCH = PASS
INTERNAL_TERMINOLOGY_LEAKAGE = ABSENT
RETRIEVER_RATIONALE_OVERSTATEMENT = RESOLVED
SPANISH_NATURALNESS = PASS
EN_ES_SEMANTIC_EQUIVALENCE = PASS
MD_DOCX_SECTION_6_4_EQUIVALENCE = PASS
OOXML_AND_COMMENT_INTEGRITY = PASS
VISUAL_QA = PASS
AUTHOR_APPROVAL_GATE = OPEN
```

La reauditoría confirma que las correcciones V01 quedaron resueltas y que no se introdujeron defectos materiales nuevos. La auditoría incluyó contenido científico/editorial real, no solo identidades técnicas.

## 5. Gate autoral B04 V02

D-138 abre el gate de aprobación:

`article/governance/D138_DISCUSSION_B04_V02_REAUDIT_PASS_AND_AUTHOR_APPROVAL_GATE.md@a1eac4c7971347f1ce8189a65cd5c26b00b5e54b`.

El autor debe aprobar o rechazar B04 V02. Hasta entonces, `ARTICLE_MASTER_V026` sigue siendo el master canónico y §6.5 permanece cerrado.

Si el autor aprueba, la promoción prevista es:

```text
SOURCE = ARTICLE_MASTER_CANDIDATE_DISCUSSION_B04_V02.md
TARGET = article/manuscript/ARTICLE_MASTER_V027.md
EXPECTED_SHA256 = d27b6ed30fcbe6ff47b78e79cf5e78affcbf285ddaecfbe94366c63208e4c69b
EXPECTED_GIT_BLOB = ac5b71788a85a4bad7b475e5d099b3e57370b71e
EXPECTED_CANONICAL_DOCX = ARTICLE_MASTER_CANDIDATE_DISCUSSION_B04_V02.docx
EXPECTED_CANONICAL_DOCX_SHA256 = 6e8bef5440c8a971d51cda6a3d1fc85e1b4793e83eb51ff3d8a7e2fa1a702b92
```

Tras aprobación, IA Gestora deberá verificar materialización byte-exact de `ARTICLE_MASTER_V027.md`, cerrar B04 como `CLOSED / APPROVED / FROZEN / INTEGRATED` y solo entonces preparar §6.5.

## 6. Estándar acumulativo de auditoría

D-136 sigue siendo vinculante. Un `PASS` exige simultáneamente fidelidad científica, fuerza epistémica correcta, coherencia argumental, ausencia de invenciones y overclaiming, terminología reader-facing sin filtración de identificadores internos, concreción SPCCR, adecuación KBS, naturalidad bilingüe, citas válidas e integridad técnica. SHA/commit/OOXML son controles necesarios, no sustituyen la auditoría científica/editorial.

La deuda editorial heredada en §6.2 continúa registrada para un gate transversal controlado antes del freeze final. No debe corregirse silenciosamente dentro de B04 o de otro bloque no autorizado.

## 7. Gate inmediato

```text
NEXT_ACTOR = AUTHOR
NEXT_ACTION = APPROVE_OR_REJECT_DISCUSSION_B04_V02
CURRENT_GATE = DISCUSSION_B04_V02_AUTHOR_APPROVAL
CANDIDATE_MD = ARTICLE_MASTER_CANDIDATE_DISCUSSION_B04_V02.md
CANDIDATE_MD_SHA256 = d27b6ed30fcbe6ff47b78e79cf5e78affcbf285ddaecfbe94366c63208e4c69b
CANDIDATE_DOCX = ARTICLE_MASTER_CANDIDATE_DISCUSSION_B04_V02.docx
CANDIDATE_DOCX_SHA256 = 6e8bef5440c8a971d51cda6a3d1fc85e1b4793e83eb51ff3d8a7e2fa1a702b92
EXPECTED_PROMOTION_IF_APPROVED = article/manuscript/ARTICLE_MASTER_V027.md
EXPECTED_PROMOTION_SHA256 = d27b6ed30fcbe6ff47b78e79cf5e78affcbf285ddaecfbe94366c63208e4c69b
EXPECTED_PROMOTION_GIT_BLOB = ac5b71788a85a4bad7b475e5d099b3e57370b71e
DISCUSSION_B05_PLUS = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
```

---

# English

V026 remains the canonical master. Discussion B04 V02 has completed an independent scientific, editorial, bilingual, and technical re-audit with `PASS`. D-138 opens the author-approval gate. No later Discussion section or Conclusion is authorized.

If the author approves, the planned V027 promotion must be byte-exact to the audited B04 V02 cumulative Markdown candidate. The legacy Section 6.2 internal-terminology debt remains logged for a controlled transversal gate before final manuscript freeze.

```text
PLAN_VERSION = V3.42
CURRENT_GATE = DISCUSSION_B04_V02_AUTHOR_APPROVAL
NEXT_ACTOR = AUTHOR
DISCUSSION_B04_V02 = AUDITED / PASS / PENDING_AUTHOR_APPROVAL
DISCUSSION_B05_PLUS = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```
