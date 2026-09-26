# Auditoría de gobernanza y continuidad del tramo reciente / Recent governance and continuity audit — V01

## Español

```text
AUDIT_ID = INSTANT_MODE_GOVERNANCE_AND_CONTINUITY_AUDIT_V01
DATE = 2026-09-26
ROLE = IA_GESTORA / EDITOR_CIENTIFICO_PRINCIPAL
SCOPE = D054_TO_B04_PROMPT_V01 + CHAT_EXECUTION_CONTINUITY
VERDICT = PASS WITH CORRECTIONS
SCIENTIFIC_REOPENING_B02 = NOT_REQUIRED
SCIENTIFIC_REOPENING_B03 = NOT_REQUIRED
CANONICAL_MASTER_V011 = VALID / RATIFIED
CANONICAL_MASTER_V012 = VALID / RATIFIED
B04_PROMPT_V01 = DEFECTIVE / SUPERSESSION_REQUIRED
ARTICLE_STATUS = STALE / SYNCHRONIZATION_REQUIRED
ARTICLE_WRITING_PLAN = STALE / SYNCHRONIZATION_REQUIRED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### 1. Objeto y criterio

Se reaudita de forma retrospectiva el tramo editorial ejecutado desde la aprobación autoral de Experimental Design B02 V02 hasta la apertura de B04. El contraste se realizó contra `START_HERE.md`, `README.md`, `DECISIONS.md`, `STYLE_GUIDE.md`, `SOURCE_REGISTRY.md`, `CLAIM_EVIDENCE_MATRIX.md`, `MASTER_WRITING_AND_DELIVERY_PROTOCOL.md` (MWDP v1.0), SPCCR, D-021, D-022, D-027, D-035, D-045, la Structure V02 congelada y las fuentes experimentales primarias pertinentes.

Esta auditoría distingue fallas de conducción/procedimiento de errores científicos persistentes. No se reabre una sección aprobada cuando el defecto ya fue corregido y la identidad final del artefacto fue verificada.

### 2. Hallazgos

#### A-01 — Conducción de la IA Gestora: ejecución diferida en chat

**Severidad:** procedimental alta, sin daño científico persistente.

En varios turnos la IA Gestora informó lo que haría después en lugar de ejecutar en ese mismo turno las acciones disponibles. Esto contradice la función operativa asumida por la Gestora y provocó detenciones artificiales del flujo. También se produjo una interpretación transitoria incorrecta según la cual el avance externo de Grupos 6/7 podía significar que el manuscrito había avanzado más allá de B02; esa interpretación fue corregida antes de cualquier integración destructiva.

**Corrección:** desde esta auditoría, todo gate ejecutable se procesa en el mismo turno. Solo se detiene el flujo por decisión autoral real, dependencia externa material, ausencia de un artefacto exacto obligatorio o contradicción que no pueda resolverse legítimamente por la Gestora.

#### A-02 — B03 V01: DOCX inicialmente omitido

**Severidad:** técnica bloqueante en su momento; **resuelta**.

El prompt B03 dejó la continuidad DOCX condicionada a una fórmula del tipo “si el flujo vigente…”, pese a que MWDP, D-021 y D-027 hacían obligatorio el master Word acumulativo. La IA de Redacción ejecutó literalmente esa ambigüedad y no generó el DOCX.

La Gestora detectó el defecto, impidió la aprobación autoral, abrió un microgate exclusivamente técnico y exigió el baseline exacto B02 V02. El candidato `ARTICLE_MASTER_CANDIDATE_EXPDES_B03_V01.docx` fue generado y auditado con SHA-256 `9616634f687410eec877678050a7a5176fd48c685fff457b0b9b39006abd775b`, integridad OOXML, 40 comentarios/anclajes, tracked changes = 0 y equivalencia de 4.4. Por tanto, el defecto no exige reabrir el contenido científico de B03.

#### A-03 — Vocabulario de verdict en la primera revisión B03

**Severidad:** procedimental menor; resuelta por cierre posterior.

La revisión `5_EXPERIMENTAL_DESIGN_B03_SECTION4_4_INTERNAL_REVIEW_V01.md` utilizó `PASS_WITH_BLOCKING_TECHNICAL_CORRECTION`. `START_HERE.md` limita los verdicts de revisión a `PASS`, `PASS WITH CORRECTIONS` o `BLOCKED`.

**Normalización retrospectiva:** el significado canónico de aquella revisión es `PASS WITH CORRECTIONS`, con corrección técnica bloqueante antes de abrir aprobación autoral. El microgate posterior cerró la corrección y B03 terminó en `PASS`. No se altera el archivo histórico de revisión ni se simula una nueva auditoría científica.

#### A-04 — Integraciones V011 y V012

**Severidad:** sin defecto científico/material.

Se verificó que las promociones fueron byte-exactas respecto de los candidatos aprobados:

- `ARTICLE_MASTER_V011.md`: SHA-256 `ef6e4cb77181f47dbc2dbd4f74ae84c2c7696de06dfe9207475cde68214f284f`; Git blob `c2aee16c219ed33c16e8e647fbd56f4dacc2cd61`.
- `ARTICLE_MASTER_V012.md`: SHA-256 `d4b0e1941791e901e20c476b99206a92ef78ea18cb2c614d9721963bb8b9ae78`; Git blob `dfea73f5f462fc65cf98347f796deadc6da58455`.

B02/4.3 y B03/4.4 permanecen `CLOSED / APPROVED / FROZEN / INTEGRATED`. No procede reabrirlos.

#### A-05 — Incumplimiento bilingüe en artefactos recientes de gobernanza

**Severidad:** de gobernanza, no científica.

D-055, D-056 y D-058 fueron creados únicamente en español. D-057 contiene una sección inglesa mucho más breve que la española y, por tanto, no satisface plenamente la regla de equivalencia de completitud y fuerza. El prompt B03 y el microgate DOCX también fueron versionados solo en español. D-059 y B04 Prompt V01 repiten el problema.

Esto contradice D002, `README.md` y `START_HERE.md`, que exigen que decisiones, prompts, reviews y controles editoriales versionados existan en español e inglés con la misma información científica.

**Tratamiento:** no se sobrescriben silenciosamente decisiones históricas ya ejecutadas. D-060 registra y corrige la gobernanza prospectiva, ratifica sus efectos sustantivos válidos y prohíbe usar esos artefactos monolingües como precedente de formato. Todo artefacto nuevo desde D-060 debe ser bilingüe y semánticamente equivalente.

#### A-06 — `ARTICLE_STATUS.md` y `ARTICLE_WRITING_PLAN.md` desfasados

**Severidad:** de gobernanza alta.

Aunque D-055–D-059 y V011/V012 fueron creados, `ARTICLE_STATUS.md` seguía declarando D-054, V010 y el gate de integración V011. `ARTICLE_WRITING_PLAN.md` seguía declarando V010/B02/4.3 como estado activo. Esto contradice el workflow de `README.md` y la obligación de `START_HERE.md` de mantener `ARTICLE_STATUS.md` como fuente de verdad editorial vigente.

**Corrección obligatoria:** sincronizar ambos archivos al estado V012/B04 antes de continuar una ejecución B04 válida.

#### A-07 — D-059 y B04 Prompt V01 contradicen Structure V02

**Severidad:** **científica/editorial material; corrección obligatoria antes de ejecutar B04**.

D-045 y `KBS_ARTICLE_WORKING_STRUCTURE_V02.md` congelan 4.5 como:

`4.5 Experimental system configuration and execution / Configuración y ejecución experimental`.

La función aprobada de 4.5 incluye, como mínimo, decisiones de ejecución materialmente relevantes sobre:

- representación de consulta;
- configuración de recuperación histórica;
- construcción Top-k/Top-3;
- asociación/recuperación documental específica por candidato;
- construcción del contexto;
- modelo local y restricciones de generación;
- condiciones materiales de software/hardware/runtime.

D-059 y `5_EXPERIMENTAL_DESIGN_B04_SECTION4_5.md@7a7aef7994c909e1fde6c01fa8dad7c2cb52f525` redujeron indebidamente 4.5 a `Historical retrieval configuration and candidate-generation protocol`. Aunque ese subalcance es científicamente pertinente, no cubre la subsección congelada completa y desplazaría componentes obligatorios hacia ninguna sección o hacia 4.6, cuya función es evaluación, no configuración/ejecución.

**Decisión de auditoría:** D-059 y B04 Prompt V01 quedan `SUPERSEDED FOR EXECUTION`. No debe ejecutarse ese prompt. Si una ejecución ya hubiera comenzado, su producto no puede pasar a aprobación bajo ese contrato estrecho; debe reconciliarse contra el prompt corregido de alcance completo.

#### A-08 — B04 Prompt V01 omite obligaciones acumulativas del MWDP

**Severidad:** gobernanza material.

El prompt V01 no referencia expresamente `MASTER_WRITING_AND_DELIVERY_PROTOCOL.md`, pese a MWDP-B02, y no exige el checklist completo MWDP de cada entrega. Sí corrigió adecuadamente la continuidad DOCX, pero la ausencia de MWDP como contrato explícito repite el patrón de omisión que originó el problema B03.

**Corrección:** el nuevo prompt B04 debe leer e invocar expresamente MWDP v1.0 y SPCCR, exigir el checklist completo, conservar D-022/D-027/D-035 y mantener el DOCX como entregable obligatorio.

### 3. Verificación científica del alcance correcto de 4.5

Las fuentes primarias vivas sostienen el alcance completo sin necesidad de inventar contenido:

- Recuperación histórica: el run congelado usa H100=2,950, query `DESCRIPCION DE MERCANCIAS CONCATENADA`, BM25 `k1=1.5`, `b=0.75`, `history_depth=2950`, `candidate_depth=100`; el código ordena por score y `case_id`, deduplica por NANDINA y conserva la primera aparición de cada código.
- Integración documental Phase F: el ranking histórico Top-3 es la única fuente de candidatos; cada candidato usa lookup directo por NANDINA-8 en el corpus jerárquico; no existe query retrieval, fallback, reranking, score fusion, inserción o sustitución en esa ruta.
- Generación HE4: el contexto se construye antes de generación y la fase generativa no ejecuta retrieval; el backend congelado es Ollama local con `qwen2.5:7b-instruct`, temperatura 0, JSON, `num_ctx=8192`, sin autoridad para alterar el Top-3.

Estos hechos son de configuración/ejecución y pueden describirse en Methods. Los valores de desempeño, cobertura observada, resultados de HE4, latencias agregadas y decisiones inferenciales permanecen fuera de 4.5.

### 4. Estado después de la auditoría

```text
B02_SECTION_4_3 = VALID / CLOSED / INTEGRATED
B03_SECTION_4_4 = VALID / CLOSED / INTEGRATED
CANONICAL_MASTER = ARTICLE_MASTER_V012
B03_DOCX_BASELINE = ARTICLE_MASTER_CANDIDATE_EXPDES_B03_V01.docx
B03_DOCX_SHA256 = 9616634f687410eec877678050a7a5176fd48c685fff457b0b9b39006abd775b
D059 = SUPERSEDED_FOR_B04_SCOPE
B04_PROMPT_V01 = SUPERSEDED_FOR_EXECUTION
B04 = REQUIRES_CORRECTED_FULL_SCOPE_PROMPT
B05_SECTION_4_6 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

---

## English

```text
AUDIT_ID = INSTANT_MODE_GOVERNANCE_AND_CONTINUITY_AUDIT_V01
DATE = 2026-09-26
ROLE = MANAGING_AI / PRINCIPAL_SCIENTIFIC_EDITOR
SCOPE = D054_TO_B04_PROMPT_V01 + CHAT_EXECUTION_CONTINUITY
VERDICT = PASS WITH CORRECTIONS
SCIENTIFIC_REOPENING_B02 = NOT_REQUIRED
SCIENTIFIC_REOPENING_B03 = NOT_REQUIRED
CANONICAL_MASTER_V011 = VALID / RATIFIED
CANONICAL_MASTER_V012 = VALID / RATIFIED
B04_PROMPT_V01 = DEFECTIVE / SUPERSESSION_REQUIRED
ARTICLE_STATUS = STALE / SYNCHRONIZATION_REQUIRED
ARTICLE_WRITING_PLAN = STALE / SYNCHRONIZATION_REQUIRED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### 1. Purpose and criterion

The editorial interval from author approval of Experimental Design B02 V02 through the opening of B04 was retrospectively audited against `START_HERE.md`, `README.md`, `DECISIONS.md`, `STYLE_GUIDE.md`, `SOURCE_REGISTRY.md`, `CLAIM_EVIDENCE_MATRIX.md`, MWDP v1.0, SPCCR, D-021, D-022, D-027, D-035, D-045, frozen Structure V02, and the relevant primary experimental sources.

The audit separates workflow/governance failures from persistent scientific errors. An approved section is not reopened when the defect was subsequently corrected and the final artifact identity was independently verified.

### 2. Findings

**A-01 — Managing-AI execution continuity.** Several chat turns announced a future action rather than executing available gate work in the same turn. A transient interpretation also conflated external Group-6/7 progress with manuscript progress. The latter was corrected before any destructive integration. Prospectively, every executable gate must be processed immediately; stopping is reserved for a genuine author decision, material external dependency, missing exact required artifact, or irreconcilable contradiction.

**A-02 — Initial B03 DOCX omission.** The B03 prompt incorrectly made DOCX continuity conditional even though MWDP, D-021, and D-027 made it mandatory. This was a blocking technical defect at the time, but it was fully closed through a dedicated microgate. `ARTICLE_MASTER_CANDIDATE_EXPDES_B03_V01.docx` was verified at SHA-256 `9616634f687410eec877678050a7a5176fd48c685fff457b0b9b39006abd775b`, with OOXML integrity, 40 comments/anchors, zero tracked changes, and approved 4.4 content. No scientific reopening of B03 is required.

**A-03 — Noncanonical review-verdict token.** The first B03 review used `PASS_WITH_BLOCKING_TECHNICAL_CORRECTION`, whereas `START_HERE.md` allows `PASS`, `PASS WITH CORRECTIONS`, or `BLOCKED`. Its canonical retrospective meaning is `PASS WITH CORRECTIONS`, with a blocking technical correction required before author approval. The later microgate closed that correction and B03 ultimately passed. The historical review file is not silently rewritten.

**A-04 — V011/V012 integrations.** No scientific/material defect was found. V011 matches SHA-256 `ef6e4cb77181f47dbc2dbd4f74ae84c2c7696de06dfe9207475cde68214f284f` and Git blob `c2aee16c219ed33c16e8e647fbd56f4dacc2cd61`; V012 matches SHA-256 `d4b0e1941791e901e20c476b99206a92ef78ea18cb2c614d9721963bb8b9ae78` and Git blob `dfea73f5f462fc65cf98347f796deadc6da58455`. B02/4.3 and B03/4.4 remain closed, approved, frozen, and integrated.

**A-05 — Bilingual-governance noncompliance.** D-055, D-056, and D-058 were created only in Spanish; D-057 contains an English summary materially shorter than the Spanish decision; the B03 prompt and DOCX microgate were also monolingual. D-059 and B04 Prompt V01 repeat the issue. This violates D002, `README.md`, and `START_HERE.md`. Historical executed artifacts are not silently overwritten; D-060 documents and prospectively corrects the defect, while ratifying the valid substantive effects of those decisions. New artifacts must be fully bilingual and semantically equivalent.

**A-06 — Stale `ARTICLE_STATUS.md` and `ARTICLE_WRITING_PLAN.md`.** Both files remained at V010/B02 despite the creation and verification of V011/V012 and D-055–D-059. This conflicts with the workflow requiring the status file to remain the current editorial source of truth. Both files must be synchronized before a valid B04 execution continues.

**A-07 — D-059 and B04 Prompt V01 conflict with frozen Structure V02.** D-045 freezes 4.5 as `Experimental system configuration and execution`, whose approved function covers query representation, historical retrieval configuration, Top-k/Top-3 construction, candidate-specific documentary retrieval/association, context construction, local model/generation restrictions, and material software/hardware/runtime conditions. D-059 and B04 Prompt V01 narrowed 4.5 to historical retrieval and candidate generation only. That subset is valid but incomplete, and it would leave required execution content without a correct Methods home. D-059 and B04 Prompt V01 are therefore superseded for execution. Any already-started output under the narrow prompt is ineligible for approval until reconciled against the corrected full-scope prompt.

**A-08 — B04 Prompt V01 omits cumulative MWDP obligations.** It does not expressly invoke/read MWDP v1.0 and does not require the complete MWDP delivery checklist. Although its DOCX continuity rule is correct, the omission repeats the governance pattern that caused B03's DOCX defect. The corrected prompt must explicitly bind MWDP v1.0, SPCCR, D-022/D-027/D-035, the full checklist, and mandatory DOCX delivery.

### 3. Scientific verification of the correct 4.5 scope

The live primary sources already support a complete 4.5 without speculation. The frozen historical run uses H100=2,950, `DESCRIPCION DE MERCANCIAS CONCATENADA`, BM25 `k1=1.5`, `b=0.75`, `history_depth=2950`, and `candidate_depth=100`; the implementation orders historical records by score and `case_id`, deduplicates by NANDINA, and retains the first occurrence of each code. Phase F uses the frozen historical Top-3 as the sole candidate source and performs direct NANDINA-8 documentary lookup, without query retrieval, fallback, reranking, score fusion, insertion, or substitution. HE4 generation receives a prebuilt context and performs no retrieval during generation; the frozen backend is local Ollama with `qwen2.5:7b-instruct`, temperature 0, JSON output, and `num_ctx=8192`, with no authority to alter the Top-3.

These are Methods configuration/execution facts. Performance values, observed documentary-coverage rates, HE4 outcomes, aggregate latencies, and inferential conclusions remain outside 4.5.

### 4. Post-audit state

```text
B02_SECTION_4_3 = VALID / CLOSED / INTEGRATED
B03_SECTION_4_4 = VALID / CLOSED / INTEGRATED
CANONICAL_MASTER = ARTICLE_MASTER_V012
B03_DOCX_BASELINE = ARTICLE_MASTER_CANDIDATE_EXPDES_B03_V01.docx
B03_DOCX_SHA256 = 9616634f687410eec877678050a7a5176fd48c685fff457b0b9b39006abd775b
D059 = SUPERSEDED_FOR_B04_SCOPE
B04_PROMPT_V01 = SUPERSEDED_FOR_EXECUTION
B04 = REQUIRES_CORRECTED_FULL_SCOPE_PROMPT
B05_SECTION_4_6 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```