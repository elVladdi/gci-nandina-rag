# D-040 — Architecture B02 integration and ARTICLE_MASTER_V009 promotion

## Español

```text
DECISION_ID = D-040
DATE = 2026-09-22
STATUS = ACTIVE / BINDING
PARENT_DECISION = D-039
ARCHITECTURE_B02 = CLOSED / APPROVED / FROZEN / INTEGRATED
ARCHITECTURE_SECTIONS_3_1_TO_3_7 = CLOSED / APPROVED / FROZEN / INTEGRATED
ARTICLE_MASTER_V009 = PROMOTED / CANONICAL
EXPERIMENTAL_DESIGN = ELIGIBLE / NOT_YET_AUTHORIZED
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### 1. Verificación de la promoción

La materialización de `ARTICLE_MASTER_V009.md` fue realizada por el autor en la rama `article/main-manuscript` después de la aprobación registrada en D-039.

La IA Gestora verificó independientemente:

```text
PROMOTION_COMMIT = bfdbaa2ad58e601f715392790451f4646964ad11
ONLY_CHANGED_FILE_IN_PROMOTION_COMMIT = article/manuscript/ARTICLE_MASTER_V009.md
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V009.md
APPROVED_MASTER_CANDIDATE_MD_SHA256 = ddbab5614856caf428aad0a7ee3f753288d600a6367908894184d3f72c98ab28
EXPECTED_GIT_BLOB = 40f20437458715c615fc1762f025ebcdbb3b6fc2
OBSERVED_GIT_BLOB = 40f20437458715c615fc1762f025ebcdbb3b6fc2
BLOB_IDENTITY = PASS
```

La coincidencia exacta del Git blob con el valor calculado y registrado para el artefacto aprobado demuestra que el Markdown promovido es byte-identical al candidato auditado. No hubo reescritura, normalización semántica, reconstrucción ni sustitución de contenido durante la promoción.

### 2. Baseline DOCX canónico

El DOCX acumulativo aprobado correspondiente queda como baseline canónico local para el siguiente bloque:

```text
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_ARCH_B02_V01.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = 09a319b8e658d3888c75087d1f7db354ef686c449ad6ffd205ea86fbc9352657
CANONICAL_CITATION_COMMENTS = 40
TRACKED_CHANGES = 0
```

D-021, D-027 y D-035 continúan gobernando la custodia y el handoff del DOCX. El siguiente bloque debe usar exactamente este binario; no puede reconstruirlo desde Markdown.

### 3. Cierre de Architecture

Architecture B02, Sections 3.5–3.7 de Part I y su espejo semántico de Part II, queda `CLOSED / APPROVED / FROZEN / INTEGRATED`.

Con ello, la totalidad de Section 3 — Decision-support architecture, Sections 3.1–3.7 — queda cerrada, aprobada, congelada e integrada. No se autoriza redacción adicional de Section 3 salvo futura enmienda expresa.

### 4. Compatibilidad de gobernanza antes del siguiente prompt

Antes de abrir Experimental Design, la IA Gestora verificó la precedencia de las reglas operativas activas:

- D-021: DOCX acumulativo bajo custodia local, identificado por SHA-256;
- D-022: prompt y respuesta operativa completa se versionan en GitHub; el chat conserva solo el puntero mínimo de ejecución;
- D-023: no se reabren revisiones cerradas durante cierres técnicos y no se usan workarounds de transferencia;
- D-035: después del antecedente de timeout, los artefactos acumulativos grandes se entregan al autor como archivos exactos y no se reintenta la vía directa fallida; Base64 manual, fragmentación y recomposición permanecen prohibidos;
- D-039/D-040: V009 y el DOCX B02 V01 constituyen los nuevos baselines canónicos;
- la regla de continuidad operativa exige avanzar automáticamente cuando no existe un gate autoral o externo real.

El patrón probado de Architecture B02 se reutilizará para Experimental Design: archivo de sección pequeño y respuesta operativa se versionan directamente; master Markdown acumulativo y DOCX candidato se entregan como adjuntos exactos al autor, con hashes, sin intentar transferir el master grande por la vía que ya produjo timeout.

### 5. Dependencia experimental externa

Se releyó `SRC-03` en su ubicación gobernante:

```text
SRC03_BRANCH = docs/plan-maestro-temporal-2026-08-31
SRC03_HEAD = b74b96d0163807007e4579d86450dd235125b30f
SRC03_PATH = docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md
SRC03_BLOB = 7b63fdb14b75eace173ac3c94775d39ed7ed7a57
GROUP6 = IN_PROGRESS
G6_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G6_F01_INTEGRATION_COMMIT = b6404ca85c8cd0b18a6b318bae1236d2ef021f4a
G6_F02 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
```

Este estado no bloquea la redacción de Experimental Design. La IA Gestora continúa en modo de solo lectura respecto de `SRC-03` y no modifica el Plan Maestro experimental.

### 6. Gate posterior

La integración de V009 satisface el gate técnico que impedía abrir Experimental Design. La IA Gestora debe abrir el primer bloque atómico de Section 4 sin pedir una aprobación redundante al autor.

---

## English

```text
DECISION_ID = D-040
DATE = 2026-09-22
STATUS = ACTIVE / BINDING
PARENT_DECISION = D-039
ARCHITECTURE_B02 = CLOSED / APPROVED / FROZEN / INTEGRATED
ARCHITECTURE_SECTIONS_3_1_TO_3_7 = CLOSED / APPROVED / FROZEN / INTEGRATED
ARTICLE_MASTER_V009 = PROMOTED / CANONICAL
EXPERIMENTAL_DESIGN = ELIGIBLE / NOT_YET_AUTHORIZED
RESULTS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### 1. Promotion verification

The author materialized `ARTICLE_MASTER_V009.md` on `article/main-manuscript` after the approval recorded in D-039.

The Managing AI independently verified:

```text
PROMOTION_COMMIT = bfdbaa2ad58e601f715392790451f4646964ad11
ONLY_CHANGED_FILE_IN_PROMOTION_COMMIT = article/manuscript/ARTICLE_MASTER_V009.md
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V009.md
APPROVED_MASTER_CANDIDATE_MD_SHA256 = ddbab5614856caf428aad0a7ee3f753288d600a6367908894184d3f72c98ab28
EXPECTED_GIT_BLOB = 40f20437458715c615fc1762f025ebcdbb3b6fc2
OBSERVED_GIT_BLOB = 40f20437458715c615fc1762f025ebcdbb3b6fc2
BLOB_IDENTITY = PASS
```

The exact Git-blob match proves that the promoted Markdown is byte-identical to the audited candidate. No scientific rewriting, semantic normalization, reconstruction, or content substitution occurred during promotion.

### 2. Canonical DOCX baseline

The approved cumulative DOCX becomes the canonical local baseline for the next block:

```text
CANONICAL_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_ARCH_B02_V01.docx / LOCAL_AUTHOR_CUSTODY
CANONICAL_MASTER_DOCX_SHA256 = 09a319b8e658d3888c75087d1f7db354ef686c449ad6ffd205ea86fbc9352657
CANONICAL_CITATION_COMMENTS = 40
TRACKED_CHANGES = 0
```

D-021, D-027, and D-035 continue to govern DOCX custody and handoff. The next block must use this exact binary and must not reconstruct it from Markdown.

### 3. Architecture closure

Architecture B02, Sections 3.5–3.7 in Part I and the Part-II semantic mirror, is `CLOSED / APPROVED / FROZEN / INTEGRATED`.

Accordingly, all of Section 3 — Decision-support architecture, Sections 3.1–3.7 — is closed, approved, frozen, and integrated. No further drafting of Section 3 is authorized unless a future explicit amendment is issued.

### 4. Governance compatibility check before the next prompt

Before opening Experimental Design, the Managing AI checked the precedence of active operational decisions. D-021 preserves exact local DOCX custody; D-022 requires full operational prompts and responses in GitHub; D-023 prevents redundant reopening and transfer workarounds; D-035 requires timeout-safe handoff after the prior large-artifact failure; D-039/D-040 establish V009 and the B02 V01 DOCX as the new canonical baselines; and the active continuity rule requires automatic progression when no genuine author or external gate exists.

The proven Architecture-B02 transfer pattern will be reused for Experimental Design: the small section artifact and small operational response may be versioned directly, while the large cumulative Markdown master and DOCX candidate are handed to the author as exact downloadable attachments with hashes, without retrying the large direct-transfer path that previously timed out.

### 5. External experimental dependency

`SRC-03` was re-read from its governing location:

```text
SRC03_BRANCH = docs/plan-maestro-temporal-2026-08-31
SRC03_HEAD = b74b96d0163807007e4579d86450dd235125b30f
SRC03_PATH = docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md
SRC03_BLOB = 7b63fdb14b75eace173ac3c94775d39ed7ed7a57
GROUP6 = IN_PROGRESS
G6_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G6_F01_INTEGRATION_COMMIT = b6404ca85c8cd0b18a6b318bae1236d2ef021f4a
G6_F02 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
```

This state does not block Experimental-Design drafting. The Managing AI remains read-only with respect to `SRC-03` and does not modify the experimental Master Plan.

### 6. Next gate

V009 integration satisfies the technical condition for opening Experimental Design. The Managing AI must open the first atomic Section-4 drafting block without requesting redundant author approval.
