# D-200 — Aprobación autoral e integración canónica G7-F03 A09+A10 como V037

## Español

```text
DECISION = D-200
PHASE = PRE_FAST_SCIENTIFIC_CORRECTION / CANONICAL_INTEGRATION
PREVIOUS_DECISION = D-199

AUTHOR_DECISION =
APPROVED / EXPLICIT

AUTHOR_APPROVAL_TEXT =
Apruebo el candidato G7F03-A09+A10 V01.

AUTHOR_APPROVAL_GATE =
CLOSED / APPROVED

GESTORA_REVIEW =
article/reviews/14_PRE_FAST_A09_A10_DIAGNOSTIC_RERANKER_INTERNAL_REVIEW_V01.md@f9f5ffdbed54fbfbe7618bc823fd7885a11e5f5d
GESTORA_REVIEW_GIT_BLOB =
e08df7d8d1e00c56da6acc48907679af5e3b1682
GESTORA_REVIEW_RESULT = PASS

EXPERIMENTAL_FOCUSED_REAUDIT =
docs/writing/group7/g7_f03_a09_a10_focused_reaudit_v0.1.md@a40003788363e45d52448df36c756ce53a8d8c7a
EXPERIMENTAL_FOCUSED_REAUDIT_GIT_BLOB =
bb0f283027fd9b4d4ca7cd0fc1f84e5650d33327

EXPERIMENTAL_CLOSURE_AUDIT =
outputs/audits/group7_closure_v0.2.json@155e1dd7c0000b6dafc32adbf15565b5d35707ec
EXPERIMENTAL_CLOSURE_AUDIT_GIT_BLOB =
488e62af83417ff2c3a4e290b8c3bd1293f6bdfe

G7_F03 = CLOSED / APPROVED
GROUP7 = CLOSED / APPROVED
G8_F01 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED

APPROVED_CANDIDATE_MD =
ARTICLE_MASTER_CANDIDATE_G7F03_A09_A10_V01.md
APPROVED_CANDIDATE_MD_SHA256 =
c1fea282d41d338a10ee7c01ee4e831baa16a792f34beb644c2a3ceb6a200919
APPROVED_CANDIDATE_MD_GIT_BLOB =
338344b1bc520378337a6760377aa3400cf6d5d1

APPROVED_CANDIDATE_DOCX =
ARTICLE_MASTER_CANDIDATE_G7F03_A09_A10_V01.docx
APPROVED_CANDIDATE_DOCX_SHA256 =
6d88e393109fb7f7962dea75013c4ad28924bbabb0ab10e10d37400322d88c5c
APPROVED_CANDIDATE_DOCX_SIZE_BYTES = 112705
APPROVED_CANDIDATE_DOCX_PAGE_COUNT = 73
APPROVED_CANDIDATE_DOCX_COMMENTS = 48
APPROVED_CANDIDATE_DOCX_TRACKED_CHANGES = 0

PROMOTED_MASTER =
article/manuscript/ARTICLE_MASTER_V037.md
PROMOTION_COMMIT =
3e68521aa0c1ce82c363a099aa9f13fba49acf01
PROMOTED_MASTER_GIT_BLOB =
338344b1bc520378337a6760377aa3400cf6d5d1
EXPECTED_PROMOTED_MASTER_GIT_BLOB =
338344b1bc520378337a6760377aa3400cf6d5d1
PROMOTION_VERIFICATION =
PASS / BYTE_EXACT_BY_GIT_BLOB_IDENTITY

CANONICAL_MASTER = ARTICLE_MASTER_V037
CANONICAL_MASTER_MD_SHA256 =
c1fea282d41d338a10ee7c01ee4e831baa16a792f34beb644c2a3ceb6a200919
CANONICAL_MASTER_MD_GIT_BLOB =
338344b1bc520378337a6760377aa3400cf6d5d1

CANONICAL_MASTER_DOCX =
ARTICLE_MASTER_CANDIDATE_G7F03_A09_A10_V01.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 =
6d88e393109fb7f7962dea75013c4ad28924bbabb0ab10e10d37400322d88c5c
CANONICAL_MASTER_DOCX_PAGE_COUNT = 73

PRE_FAST_SCIENTIFIC_CORRECTION =
CLOSED / APPROVED / INTEGRATED

FAST_FINALIZATION_MODE =
READY_FOR_FORMALIZATION / NOT_EXECUTED

FINAL_F01 =
ELIGIBLE_FOR_GESTORA_BOUNDARY / NOT_AUTHORIZED_FOR_WRITING_EXECUTION
```

## 1. Verificación de identidad antes de promoción

IA Gestora verificó sobre los archivos reales entregados al Autor:

```text
MD_SIZE_BYTES = 283664
MD_SHA256 =
c1fea282d41d338a10ee7c01ee4e831baa16a792f34beb644c2a3ceb6a200919
MD_GIT_BLOB =
338344b1bc520378337a6760377aa3400cf6d5d1

DOCX_SIZE_BYTES = 112705
DOCX_SHA256 =
6d88e393109fb7f7962dea75013c4ad28924bbabb0ab10e10d37400322d88c5c
```

Las identidades coinciden exactamente con D-199 y con la auditoría Gestora previa.

## 2. Aprobación del Autor

El Autor aprobó explícitamente el candidato G7F03-A09+A10 V01.

La aprobación cubre exclusivamente los cuatro bloques auditados:

- A09 Method EN;
- A10 Result EN;
- A09 Método ES;
- A10 Resultado ES.

No se reabre ni modifica ningún otro contenido.

## 3. Promoción canónica

Antes de la promoción, IA Gestora verificó que no existía un
`ARTICLE_MASTER_V037.md` legítimo en la rama.

El Markdown aprobado fue materializado byte-exacto como:

`article/manuscript/ARTICLE_MASTER_V037.md`

Commit de promoción:

`3e68521aa0c1ce82c363a099aa9f13fba49acf01`

Git blob observado:

`338344b1bc520378337a6760377aa3400cf6d5d1`

El blob observado coincide exactamente con el blob calculado y aprobado del candidato.

## 4. Word acumulativo

El Word aprobado pasa a ser el nuevo baseline acumulativo bajo custodia del Autor:

`ARTICLE_MASTER_CANDIDATE_G7F03_A09_A10_V01.docx`

con:

```text
SHA256 =
6d88e393109fb7f7962dea75013c4ad28924bbabb0ab10e10d37400322d88c5c
SIZE_BYTES = 112705
PAGE_COUNT = 73
COMMENTS = 48
TRACKED_CHANGES = 0
```

## 5. Cierre de G7-F03 en la gobernanza editorial

La gobernanza editorial adopta el cierre experimental ya emitido:

```text
G7_F03 = CLOSED / APPROVED
GROUP7 = CLOSED / APPROVED
G8_F01 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
```

D-200 no autoriza G8-F01.

## 6. Transición a FAST finalization

La corrección científica pre-FAST queda cerrada.

La siguiente fase editorial puede organizarse ahora con las restricciones ya aprobadas por IA Experimental:

- cuerpo principal: G5-MAIN-01, G5-MAIN-02 y G6-FIG-01;
- Supplementary/Appendix: G5-SECONDARY-01, G5-SECONDARY-02, G5-APPENDIX-01..05, G6-FIG-02 y G6-FIG-03;
- Figure 1 arquitectónica permitida como esquema editorial;
- cualquier reranker diagnóstico en Figure 1 debe aparecer como ruta lateral separada y sin feedback al flujo primario.

La autorización de ejecución de FINAL-F01 requiere una decisión posterior de IA Gestora con scope y prompt exactos.

## 7. Gate vigente

```text
CURRENT_DRAFTING_PHASE = FAST_FINALIZATION_PREPARATION
CURRENT_GATE = FINAL_F01_BOUNDARY_PREPARATION
NEXT_ACTOR = IA_GESTORA_DEL_ARTICULO
NEXT_ACTION = FORMALIZE_FAST_FINALIZATION_AND_FINAL_F01

AUTHOR_APPROVAL_GATE = CLOSED / APPROVED
CANONICAL_MASTER = ARTICLE_MASTER_V037
PRE_FAST_SCIENTIFIC_CORRECTION = CLOSED

FINAL_F01_WRITING_EXECUTION = NOT_AUTHORIZED
FINAL_F02 = NOT_AUTHORIZED
FINAL_F03 = NOT_AUTHORIZED
```

---

## English

D-200 records the Author's explicit approval of the exact G7-F03 A09+A10 candidate and promotes its byte-exact Markdown as ARTICLE_MASTER_V037.

The approved cumulative DOCX becomes the new local canonical Word baseline. G7-F03 and Group 7 remain closed/approved; G8-F01 is eligible under the Experimental Plan but remains unauthorized and unexecuted.

The pre-FAST scientific correction is closed. FAST finalization may now be formally organized by Managing AI, but no FINAL-F01 Writing-AI execution is authorized by this decision.
