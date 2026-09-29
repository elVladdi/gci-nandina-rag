# D-199 — Gate de aprobación del Autor para corrección G7-F03 A09+A10

## Español

```text
DECISION = D-199
PHASE = PRE_FAST_SCIENTIFIC_CORRECTION
PREVIOUS_DECISION = D-198

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

EXPERIMENTAL_REAUDIT_RESULT = PASS
G7F03_A09 = PASS / SATISFIED
G7F03_A10 = PASS / SATISFIED
G7_F03 = CLOSED / APPROVED
GROUP7 = CLOSED / APPROVED
G8_F01 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED

CANDIDATE_MD =
ARTICLE_MASTER_CANDIDATE_G7F03_A09_A10_V01.md
CANDIDATE_MD_SHA256 =
c1fea282d41d338a10ee7c01ee4e831baa16a792f34beb644c2a3ceb6a200919
CANDIDATE_MD_EXPECTED_GIT_BLOB =
338344b1bc520378337a6760377aa3400cf6d5d1

CANDIDATE_DOCX =
ARTICLE_MASTER_CANDIDATE_G7F03_A09_A10_V01.docx
CANDIDATE_DOCX_SHA256 =
6d88e393109fb7f7962dea75013c4ad28924bbabb0ab10e10d37400322d88c5c
CANDIDATE_DOCX_SIZE_BYTES = 112705
CANDIDATE_DOCX_PAGE_COUNT = 73

CURRENT_GATE = AUTHOR_APPROVAL_G7F03_A09_A10
NEXT_ACTOR = AUTHOR
NEXT_ACTION = APPROVE_OR_REJECT_G7F03_A09_A10_CANDIDATE

CANONICAL_MASTER = ARTICLE_MASTER_V036
CANONICAL_PROMOTION = NOT_AUTHORIZED_UNTIL_AUTHOR_APPROVAL
FINAL_F01 = NOT_AUTHORIZED_UNTIL_AUTHOR_APPROVAL_AND_INTEGRATION
```

## 1. Motivo

IA Experimental completó la reauditoría focalizada exigida por D-198 y devolvió PASS.

Los dos hallazgos que habían impedido cerrar G7-F03 están satisfechos:

- G7F03-A09 — método del reranker LLM diagnóstico;
- G7F03-A10 — resultados congelados del reranker diagnóstico.

No existe contradicción científica directa nueva.

IA Experimental cerró formalmente:

```text
G7_F03 = CLOSED / APPROVED
GROUP7 = CLOSED / APPROVED
```

y dejó G8-F01 únicamente elegible, no autorizado ni ejecutado.

## 2. Estado del candidato

IA Gestora ya auditó el candidato y obtuvo PASS.

El Markdown difiere de V036 exclusivamente en los cuatro párrafos autorizados A09/A10 EN/ES. La restauración de esos cuatro bloques devuelve V036 byte-exacto.

El DOCX entregado conserva:

```text
COMMENTS = 48
COMMENT_RANGE_START = 48
COMMENT_RANGE_END = 48
COMMENT_REFERENCE = 48
TRACKED_CHANGES = 0
OOXML_INTEGRITY = PASS
FULL_RENDER = PASS
FULL_VISUAL_QA = PASS
PAGE_COUNT = 73
```

## 3. Contenido sometido a aprobación del Autor

La aprobación se limita a las cuatro inserciones ya auditadas:

1. A09 Method EN en §4.5;
2. A10 Result EN al final de §5.2;
3. A09 Método ES en §4.5;
4. A10 Resultado ES al final de §5.2.

No se solicita reabrir ninguna otra sección.

## 4. Efecto de una aprobación

Si el Autor aprueba el candidato:

1. IA Gestora verificará nuevamente las identidades del MD/DOCX recibidos;
2. promoverá el Markdown exacto como el siguiente master canónico disponible, previsiblemente ARTICLE_MASTER_V037 si no existe una versión legítima posterior;
3. registrará el Word candidato como nuevo Word acumulativo canónico bajo custodia del Autor;
4. actualizará ARTICLE_STATUS y ARTICLE_WRITING_PLAN;
5. cerrará la corrección pre-FAST;
6. podrá abrir FINAL-F01 — Scientific Presentation & Visual Structuring.

La aprobación de A09+A10 no autoriza G8-F01; esa ficha permanece bajo gobernanza de IA Experimental.

## 5. Efecto de un rechazo

Si el Autor rechaza o solicita cambios, no habrá promoción canónica y FINAL-F01 permanecerá bloqueado. La corrección deberá volver al scope exacto que indique el Autor.

## 6. Gate

```text
AUTHOR_APPROVAL_GATE = OPEN
AUTHOR_DECISION = PENDING

READY_FOR_CANONICAL_PROMOTION = CONDITIONAL_ON_AUTHOR_APPROVAL
READY_FOR_FINAL_F01 = CONDITIONAL_ON_AUTHOR_APPROVAL_AND_INTEGRATION

NEXT_ACTOR = AUTHOR
```

---

## English

D-199 opens the Author approval gate for the narrow G7-F03 A09+A10 correction after both Managing-AI audit and focused Experimental-AI re-audit returned PASS.

G7-F03 and Group 7 are scientifically closed and approved. G8-F01 is eligible under the Experimental Plan but remains unauthorized and unexecuted.

The canonical master remains V036 until the Author explicitly approves the exact A09+A10 cumulative candidate. If approved, Managing AI will verify identities, promote the exact Markdown to the next legitimate canonical master, register the corresponding Word candidate as the new cumulative Word baseline, and only then open FINAL-F01.
