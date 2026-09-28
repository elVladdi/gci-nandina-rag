# D-094 — Results B02 V01 PASS WITH CORRECTIONS and narrow revision required

## Español

```text
DECISION_ID = D-094
DATE = 2026-09-27
STATUS = ACTIVE / BINDING
PARENT_DECISION = D-093
PHASE = RESULTS
BLOCK = RESULTS_B02_SECTION_5_2
CANDIDATE_REVISION = V01
INTERNAL_REVIEW = article/reviews/6_RESULTS_B02_SECTION5_2_INTERNAL_REVIEW_V01.md@9ab632e8a1f19a3b43a067467c401f76a4b3cd57
INTERNAL_REVIEW_RESULT = PASS_WITH_CORRECTIONS
RESULTS_B02_V01_STATE = SCIENTIFIC_PASS / NARROW_SPANISH_CORRECTION_REQUIRED
AUTHOR_APPROVAL_GATE = CLOSED
RESULTS_B03_PLUS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

## 1. Decisión

IA Gestora acepta el contenido científico, cifras, fronteras semánticas y alcance diferencial de Results B02 V01. No se requiere recalcular métricas ni reabrir D-092.

Antes de abrir el gate autoral se requiere una revisión estrecha del espejo español para eliminar tres formulaciones híbridas/calco detectadas por la auditoría Gestora. La revisión no puede alterar la Parte I inglesa ni modificar cifras, denominadores, orden de resultados, comparadores, deep coverage o reserva de inferencia.

## 2. Candidato base exacto de la corrección

```text
BASELINE_MD = ARTICLE_MASTER_CANDIDATE_RESULTS_B02_V01.md
BASELINE_MD_SHA256 = 87b85f095e0cef6d6f9b12e70223596b563014a38bcacfa37c4e0448a66dad6c
BASELINE_MD_GIT_BLOB_EXPECTED_FROM_BYTES = 804ae5709f08e878202f48465d4671bf70dc15c7

BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_RESULTS_B02_V01.docx
BASELINE_DOCX_SHA256 = c267f7da5415161b812aed10cef66929b6b6cd2be51ecb2196d43c2e1180ce6f
COMMENTS = 40 / PRESERVE
TRACKED_CHANGES = 0 / PRESERVE
```

## 3. Correcciones autorizadas

En §5.2 del espejo español solamente:

```text
"métricas de early ranking"
→ "métricas de desempeño en las primeras posiciones del ranking"

"framework primario"
→ "flujo primario del framework"

"Section 5.6"
→ "Sección 5.6"
```

La sustitución de `métricas de early ranking` aplica a sus dos ocurrencias en el cuerpo español de §5.2.

No se autoriza ninguna otra reescritura salvo ajustes mínimos de puntuación/gramática estrictamente necesarios para insertar esas sustituciones.

## 4. Gate

```text
CURRENT_GATE = RESULTS_B02_V01_NARROW_CORRECTION_PREPARATION
NEXT_ACTOR = IA_GESTORA
NEXT_ACTION = PREPARE_REVIEW_AND_AUTHORIZE_NARROW_CORRECTION_PROMPT
AUTHOR_APPROVAL_GATE = CLOSED
RESULTS_B03_PLUS = NOT_AUTHORIZED
```

D-094 no autoriza por sí sola a IA de Redacción. IA Gestora debe emitir y auditar el prompt correctivo antes de abrir su ejecución.

---

## English

Results B02 V01 is scientifically accepted but requires one narrow Spanish-mirror naturalness revision before author review. Only the three frozen phrase corrections above are allowed; the English text, all numerical results, scientific scope, and later-section placeholders must remain unchanged.