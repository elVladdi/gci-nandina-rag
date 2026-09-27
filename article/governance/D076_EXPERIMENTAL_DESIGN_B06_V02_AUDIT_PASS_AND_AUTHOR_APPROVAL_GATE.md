# D-076 — B06 V02 audit PASS and author-approval gate / Auditoría PASS de B06 V02 y apertura de gate autoral

## Español

```text
DECISION_ID = D-076
DATE = 2026-09-27
STATUS = ACTIVE / BINDING
PARENT_DECISION = D-075
BLOCK = EXPERIMENTAL_DESIGN_B06_SECTION_4_7
CANDIDATE_REVISION = V02
INTERNAL_REVIEW = article/reviews/5_EXPERIMENTAL_DESIGN_B06_SECTION4_7_INTERNAL_REVIEW_V02.md@5f154e54faf5b59f301bbb07787616468304a04b
INTERNAL_REVIEW_RESULT = PASS
RESPONSE = article/responses/5_EXPERIMENTAL_DESIGN_B06_SECTION4_7_RESPONSE_V02.md@8469a6aa83b85dc64486877106cc6f05115b1751
RESPONSE_GIT_BLOB = 50f12ae688c0459cc396c6337c14e75d119a6128
SECTION_ARTIFACT = article/sections/experimental_design/Experimental_Design_B06_V02.md@b8d19af968cc9b3e0cc205a908a05a5c1549b4c4
SECTION_ARTIFACT_GIT_BLOB = 76d833b0f3c693ddafe997f0202e3893513a35a2
B06_STATE = DRAFT_COMPLETE / GESTORA_PASS / PENDING_AUTHOR_APPROVAL
AUTHOR_APPROVAL_GATE = OPEN_FOR_B06_V02_ONLY
INTEGRATION = NOT_AUTHORIZED_UNTIL_EXPLICIT_AUTHOR_APPROVAL
SECTION_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

## 1. Decisión

La auditoría diferencial independiente de B06 V02 concluyó `PASS`. Las cuatro incidencias que motivaron la corrección estrecha de B06 V01 quedaron cerradas sin expansión científica del bloque, sin filtración de Results y sin daño a la continuidad acumulativa Markdown/DOCX.

Se abre exclusivamente el gate de revisión/aprobación autoral para B06 V02. Esta decisión **no** integra todavía el candidato en el master canónico, **no** promueve una nueva versión canónica y **no** autoriza Section 4.8 ni Results.

## 2. Candidatos sometidos a aprobación autoral

```text
CANDIDATE_MD = ARTICLE_MASTER_CANDIDATE_EXPDES_B06_V02.md
CANDIDATE_MD_SHA256 = b04de5aa482561adc970f1c7e06e38f8c932fa110cc86605d2d7a0adb9c6983c
CANDIDATE_MD_GIT_BLOB = e9a17899ccbcb9971e6dfb5002f908e17a0441d9

CANDIDATE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B06_V02.docx
CANDIDATE_DOCX_SHA256 = 86a0b9517ced0f8c411c04c990bc159d3b4b3f814ad592e669a8f1993cf0f3c2
COMMENTS = 40 / PRESERVED
TRACKED_CHANGES = 0
FULL_DOCX_RENDER = PASS / 49 OF 49 PAGES
VISUAL_QA = PASS
```

La identidad de estos candidatos debe permanecer fija durante el gate autoral. Cualquier cambio solicitado por el autor requerirá una nueva revisión/versionado antes de integración.

## 3. Estado científico cerrado por la auditoría

```text
B06-C01 = CLOSED / PASS
B06-C02 = CLOSED / PASS
B06-C03 = CLOSED / PASS
B06-C04 = CLOSED / PASS
RESULTS_LEAKAGE = NONE
HYPOTHESIS_DISPOSITION_LEAKAGE = NONE
SCIENTIFIC_SCOPE_EXPANDED = NO
EN_ES_EQUIVALENCE = PASS
MD_DOCX_CONTINUITY = PASS
OOXML_INTEGRITY = PASS
```

El rotulado `GOVERNING_DECISION = D-074` de la response V02 no constituye incidencia pendiente: D-074 es la decisión de alcance del microgate y D-075 es la autorización de ejecución verificada.

## 4. Canonicalidad durante el gate autoral

Hasta que exista aprobación autoral explícita y posterior integración gobernada, el master canónico **no cambia**:

```text
CANONICAL_MASTER = ARTICLE_MASTER_V014
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V014.md
CANONICAL_MASTER_MD_SHA256 = e7aa7e6706923520a5403ab4dec6713d5a1f7fe6b55edccbde43f2d54b755b97
CANONICAL_MASTER_MD_GIT_BLOB = 20105abb745e382b923e4eb43d9a771a722df9e3
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B05_V01.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = b1ab0ba79fe8d4dffad57208b2765f18e2c84b80ef4c1dbcfd3ac93eba8f78e2
```

B06 V02 es un candidato aprobado por IA Gestora, no un master integrado.

## 5. Gate vigente

```text
CURRENT_GATE = AUTHOR_APPROVAL_B06_V02
NEXT_ACTOR = AUTHOR
NEXT_ACTION = APPROVE_OR_REQUEST_CHANGES_B06_V02
AUTHOR_APPROVAL_GATE = OPEN_FOR_B06_V02_ONLY
B06_INTEGRATION = BLOCKED_UNTIL_EXPLICIT_AUTHOR_APPROVAL
SECTION_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

Una aprobación autoral explícita permitirá crear el gate de integración y verificar la promoción byte-exacta del candidato aprobado. La aprobación no autoriza automáticamente Section 4.8; esa sección requerirá su propio ground truth, prompt, revisión y autorización.

---

## English

```text
DECISION_ID = D-076
DATE = 2026-09-27
STATUS = ACTIVE / BINDING
PARENT_DECISION = D-075
BLOCK = EXPERIMENTAL_DESIGN_B06_SECTION_4_7
CANDIDATE_REVISION = V02
INTERNAL_REVIEW = article/reviews/5_EXPERIMENTAL_DESIGN_B06_SECTION4_7_INTERNAL_REVIEW_V02.md@5f154e54faf5b59f301bbb07787616468304a04b
INTERNAL_REVIEW_RESULT = PASS
B06_STATE = DRAFT_COMPLETE / GESTORA_PASS / PENDING_AUTHOR_APPROVAL
AUTHOR_APPROVAL_GATE = OPEN_FOR_B06_V02_ONLY
INTEGRATION = NOT_AUTHORIZED_UNTIL_EXPLICIT_AUTHOR_APPROVAL
SECTION_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

The independent differential audit of B06 V02 returned `PASS`. B06-C01 through B06-C04 are closed, with no Results leakage, hypothesis-disposition leakage, scientific-scope expansion, or cumulative-document damage.

The only gate opened by D-076 is author review/approval of the exact B06 V02 candidates:

```text
CANDIDATE_MD_SHA256 = b04de5aa482561adc970f1c7e06e38f8c932fa110cc86605d2d7a0adb9c6983c
CANDIDATE_MD_GIT_BLOB = e9a17899ccbcb9971e6dfb5002f908e17a0441d9
CANDIDATE_DOCX_SHA256 = 86a0b9517ced0f8c411c04c990bc159d3b4b3f814ad592e669a8f1993cf0f3c2
COMMENTS = 40 / PRESERVED
TRACKED_CHANGES = 0
```

`ARTICLE_MASTER_V014.md` and the approved B05 V01 DOCX remain canonical until explicit author approval and a governed integration step. Section 4.8, Results, Discussion, and Conclusion remain unauthorized.

```text
CURRENT_GATE = AUTHOR_APPROVAL_B06_V02
NEXT_ACTOR = AUTHOR
NEXT_ACTION = APPROVE_OR_REQUEST_CHANGES_B06_V02
B06_INTEGRATION = BLOCKED_UNTIL_EXPLICIT_AUTHOR_APPROVAL
SECTION_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```
