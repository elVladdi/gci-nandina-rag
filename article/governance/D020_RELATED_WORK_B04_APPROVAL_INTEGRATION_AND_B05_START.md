# D-020 — Aprobación e integración de Related Work B04 y apertura de B05 / Related Work B04 Approval, Integration, and B05 Start

## Español

```text
DECISION_ID = D-020
DECISION_DATE = 2026-09-20
AUTHOR_DECISION = RECEIVED
INTERNAL_REVIEW = PASS
BLOCK = RELATED_WORK_B04
BLOCK_REVISION = V02
SECTION = 2.4 Evidence grounding, explainability, and auditability
DELIVERY_COMMIT = 119d6f9b46320d4970c7c46e421d66649269885f
B04_CONTENT = PASS
SOURCE_SUPPORT = PASS / 6_OF_6
DOCX_OOXML_INTEGRITY = PASS
DOCX_TRACKED_CHANGES = 0
DOCX_RENDER = PASS / 23_OF_23_PAGES
APPROVED_DOCX_SHA256 = e26f4cbe2ae88e0424805e5fa1e1385e5d2fe19e5c00bebb948763cc28179162
APPROVED_DOCX_GIT_BLOB = 64519f62da55bd92acbc7c62c30f97a23b529efc
DOCX_BINARY_IDENTITY = PASS
NET_FILE_SCOPE = PASS / EXACTLY_4_AUTHORIZED_B04_V02_FILES
SINGLE_COMMIT_DISCIPLINE = FAIL / NONBLOCKING_PROCESS_DEVIATION
DRAFTING_AI_DEVIATION_COMMITS = b72e1c963f4264148030365fd883f91cbb77a3e3; be3e5003edc1d5bc2a9286fd7d1afe578e98fad5
MANAGING_AI_PREINTEGRATION_TRANSIENT_COMMITS = 5d2d4acf8db2b5f8bf4e0c2bb39866fdbdf9e1b2; 25ec0255fcb606cf0756528ef806fc335bb8b6a4; c200b30593a2a585a379dea470262fce04aa150e; b8a14e3f9983d19447e48f0c9515f3f3c72f9d36; 81a91f0b86a3837b7322d7f973a70743716ca020; 89c6936da44bf7b5f8c60b958ed66d8c27c97fcc; 7809fc8aaf8997f83d3f5ddadc712a6a56d5ca76; 6f62d3f8f90f3a76291e402e4819f43566e86698; 2bc128423305172d2ae4e79569de1fd5ab7be8ac
HISTORY_REWRITE = NOT_PERFORMED / INTENTIONAL
BLOCK_STATUS = APPROVED / FROZEN / INTEGRATED
CANONICAL_MASTER = ARTICLE_MASTER_V004
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V004.md
CANONICAL_MASTER_DOCX = article/manuscript/ARTICLE_MASTER_V004.docx
CANONICAL_DOCX_SHA256 = e26f4cbe2ae88e0424805e5fa1e1385e5d2fe19e5c00bebb948763cc28179162
CITATION_COMMENTS_TOTAL = 25
EXPERIMENTAL_REVIEW = NOT_REQUIRED
NEXT_BLOCK = RELATED_WORK_B05
NEXT_SECTION = 2.5 Reproducibility and evaluation in knowledge-based decision support
RELATED_WORK_B05 = AUTHORIZED
RELATED_WORK_B06 / SECTION_2.6 = NOT_AUTHORIZED
```

### Decisión

El autor aprobó expresamente `Related Work B04 V02` después de la auditoría independiente de la IA Gestora. La revisión verificó las tres correcciones exigidas, las seis relaciones claim–fuente contra los full texts primarios, la equivalencia EN–ES, la preservación de los diecinueve comentarios heredados, los seis comentarios nuevos, la integridad OOXML, cero tracked changes y el render completo del documento.

La identidad binaria del Word queda cerrada: el DOCX aprobado tiene SHA-256 `e26f4cbe2ae88e0424805e5fa1e1385e5d2fe19e5c00bebb948763cc28179162` y Git blob `64519f62da55bd92acbc7c62c30f97a23b529efc`; el blob coincide con el `git hash-object` del binario aprobado.

### Regularización de la desviación de historial

Durante el cierre técnico de la IA de Redacción se generó accidentalmente `__noop__` en `b72e1c...` y se eliminó inmediatamente en `be3e500...`. El commit semántico B04 V02 `119d6f9...` contiene los cuatro artefactos autorizados. La comparación neta desde el prompt de cierre `ccd59261...` hasta `119d6f9...` muestra únicamente esos cuatro archivos; `__noop__` no persiste. La disciplina de un único commit se registra por ello como `FAIL / NONBLOCKING_PROCESS_DEVIATION`, sin impacto científico, documental o binario.

Durante la preparación de esta integración, la IA Gestora produjo además varios commits transitorios de prueba/placeholder por uso incorrecto del conector. Se conservan en el historial por trazabilidad y no se reescriben. El commit de integración elimina cualquier archivo temporal residual y reemplaza los placeholders por sus contenidos definitivos. Esta desviación adicional también es procesal y no altera el contenido científico ni los artefactos aprobados.

No se realiza `force push`, rebase destructivo ni reescritura de historial. La decisión es conservar la trazabilidad completa y normalizar el árbol final.

### Promoción canónica

B04 V02 se promueve byte-for-byte al master acumulativo:

- `article/manuscript/ARTICLE_MASTER_V004.md` reutiliza el blob del candidato aprobado;
- `article/manuscript/ARTICLE_MASTER_V004.docx` reutiliza exactamente el blob binario aprobado.

El master V004 contiene Sections 2.1–2.4 y veinticinco comentarios de auditoría de citas.

### Apertura de B05

Se autoriza exclusivamente `Related Work B05 — Section 2.5 Reproducibility and evaluation in knowledge-based decision support`.

B05 debe partir de `ARTICLE_MASTER_V004`, preservar exactamente 2.1–2.4 y los veinticinco comentarios, y sintetizar literatura sobre documentación de datos, identidad/versionado, provenance/lineage, reproducibilidad y diseño de evaluación alineado con la función del sistema. Debe mantener separadas reproducibilidad, corrección, generalización y validez jurídica, y no debe anticipar Section 2.6, arquitectura propia, testbed, resultados, FINAL_GAP ni novelty.

Section 2.6 permanece no autorizada.

---

## English

The author expressly approved Related Work B04 V02 after independent Managing-AI review. All three required source-scope corrections, six primary-source claim checks, bilingual equivalence, twenty-five total citation comments, OOXML integrity, zero tracked changes, and the full render passed. The approved DOCX SHA-256 is `e26f4cbe2ae88e0424805e5fa1e1385e5d2fe19e5c00bebb948763cc28179162`, with Git blob `64519f62da55bd92acbc7c62c30f97a23b529efc`; binary identity is verified.

The accidental `__noop__` add/remove commits and the Managing-AI transient connector-probe commits are retained in history rather than hidden by force-push or destructive rewrite. They are recorded as nonblocking process deviations because the final tree is normalized, the approved artifact is byte-identical, and no scientific content is affected.

B04 is therefore `APPROVED / FROZEN / INTEGRATED`. `ARTICLE_MASTER_V004.md/.docx` becomes canonical, with twenty-five citation-audit comments. Only Related Work B05 / Section 2.5 is now authorized; Section 2.6 remains blocked.