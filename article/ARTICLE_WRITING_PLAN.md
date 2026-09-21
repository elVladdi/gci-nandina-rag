# Plan maestro de redacción / Master Writing Plan

```text
PLAN_VERSION = V2.5
TARGET_JOURNAL = Knowledge-Based Systems
ARTICLE_TYPE = Research article
EDITORIAL_BASIS = KBS_EWG_34_V01
STRUCTURE_RESET_DECISION = D-014
STRUCTURE_APPROVAL_DECISION = D-015
EXPERIMENTAL_RECONCILIATION_DECISION = D-019
DOCX_CUSTODY_DECISION = D-021
GITHUB_ONLY_RESPONSE_DECISION = D-022
TECHNICAL_CLOSURE_MODE_DECISION = D-023
LATEST_EDITORIAL_DECISION = D-024
LEGACY_METHODS_FIRST_ORDER = SUPERSEDED
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V01.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
CANONICAL_MASTER = ARTICLE_MASTER_V005
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V005.md
CANONICAL_MASTER_MD_GIT_BLOB = 25782b8b2305b546f2f5ff69514893d045e50762
CANONICAL_MASTER_DOCX = LOCAL_AUTHOR_CUSTODY / D021
CANONICAL_MASTER_DOCX_SOURCE_FILENAME = ARTICLE_MASTER_CANDIDATE_RW_B05_V01.docx
CANONICAL_MASTER_DOCX_SHA256 = 042952002c2caeb86ec854b0bfcd7332724ddd4712589e25dfddb52718bf159a
CANONICAL_CITATION_COMMENTS = 32
CURRENT_DRAFTING_PHASE = RELATED_WORK
CURRENT_AUTHORIZED_BLOCK = RELATED_WORK_B06 / SECTION_2.6_ONLY
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

## Español

### 1. Propósito

Administrar la construcción iterativa del artículo científico principal sin anticipar resultados, alterar el diseño experimental aprobado ni trasladar al manuscrito la lógica de un documento de gobernanza. El artículo se construye sobre una estructura acumulativa aprobada y cada bloque autorizado completa esa misma base.

La redacción se rige por `KBS_EWG_34_V01`, `MWDP_V1.0`, SPCCR, la Claim–Evidence Matrix, la literatura congelada de 0B y las fuentes experimentales gobernantes cuando correspondan.

### 2. Principios rectores

- El artículo no será una versión abreviada de la tesis.
- El lector debe comprender primero problema y posicionamiento, después la arquitectura general y solo entonces la instanciación experimental específica.
- NANDINA/Chapter-Class 87 y el corpus concreto no deben definir prematuramente el alcance conceptual de la arquitectura.
- La recuperación histórica genera y ordena candidatos.
- El Top-3 queda fijado antes de recuperación documental y generación.
- La recuperación documental aporta evidencia para candidatos ya fijados y no sustituye ni reordena el ranking.
- El LLM local opera después de recuperación y se usa para explicación controlada; no clasifica desde cero ni retroalimenta la selección de candidatos.
- `candidate retrieval ≠ overall classification accuracy`.
- `documentary association ≠ substantive legal correctness`.
- `auditability ≠ legal correctness`.
- `configurability/replicability ≠ empirical generalization`.
- SERIE es unidad de observación/análisis; DAM es unidad de agrupamiento cuando existe dependencia.
- Ningún resultado pendiente se redactará como hallazgo.
- Toda afirmación científica debe trazarse a evidencia autorizada.
- Part I es el manuscript master inglés; Part II es el espejo español de control semántico.
- El posicionamiento compara funciones y autoridad de los componentes; no convierte diferencias arquitectónicas en novelty.

### 3. Arquitectura acumulativa aprobada

1. `Introduction`
2. `Related work`
3. `Decision-support architecture`
4. `Experimental design`
5. `Results`
6. `Discussion`
7. `Conclusion`
8. end matter de KBS.

La estructura detallada permanece en `article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V01.md`, aprobada mediante D-015. `Limitations` permanece integrada como `6.6 Limitations` salvo futura enmienda expresa.

### 4. Política acumulativa del Word y del master

1. Cada bloque parte del último master acumulativo aprobado.
2. El baseline Markdown actual es `ARTICLE_MASTER_V005.md`, blob Git `25782b8b2305b546f2f5ff69514893d045e50762`.
3. Conforme a D-021, el baseline DOCX actual permanece bajo custodia local del autor. El binario aprobado procede de `ARTICLE_MASTER_CANDIDATE_RW_B05_V01.docx`, SHA-256 `042952002c2caeb86ec854b0bfcd7332724ddd4712589e25dfddb52718bf159a`.
4. Un renombrado local a `ARTICLE_MASTER_V005.docx` es aceptable solo si no modifica bytes y conserva exactamente el SHA-256 gobernante.
5. No se crean Words independientes por sección.
6. La sección nueva se inserta en su ubicación estructural.
7. Solo se eliminan las notas editoriales correspondientes a la sección completada.
8. Part I y Part II conservan equivalencia semántica.
9. Candidatos no se vuelven canónicos hasta aprobación expresa del autor y auditoría de la IA Gestora.
10. Si el baseline DOCX exacto no está disponible, la IA de Redacción se detiene con `BASELINE_DOCX_ACCESS_REQUIRED`; no reconstruye silenciosamente el Word desde Markdown.
11. Todo bloque preserva exactamente texto y comentarios de las secciones aprobadas.
12. El SHA-256 del DOCX candidato se registra obligatoriamente en la respuesta versionada en GitHub; la carga del binario a GitHub queda diferida conforme a D-021 salvo hito explícito.
13. Desviaciones de proceso se registran explícitamente y no se corrigen mediante reescritura destructiva del historial salvo autorización expresa del autor y justificación de gobernanza.
14. D-022 exige prompts y respuestas sustantivas en GitHub; el chat de la IA de Redacción solo puede contener el puntero mínimo autorizado.
15. D-023 aplica a cierres puramente técnicos: sin Base64 para Markdown, sin fragmentación, sin verificaciones redundantes y sin reauditoría científica innecesaria.

### 5. Estado de fases y bloques

| Elemento | Estado |
|---|---|
| 0A | CLOSED / APPROVED |
| 0B | CLOSED / APPROVED / FROZEN |
| 0C | CLOSED / APPROVED / FROZEN |
| 0D original | CLOSED / APPROVED / FROZEN; arquitectura supersedida por D-014 |
| KBS-34 guide | AUTHOR_APPROVED / ACTIVE / BINDING |
| Estructura KBS V01 | AUTHOR_APPROVED / FROZEN_FOR_DRAFTING |
| Related Work B01 / 2.1 | APPROVED / FROZEN / INTEGRATED |
| Related Work B02 / 2.2 | APPROVED / FROZEN / INTEGRATED |
| Related Work B03 / 2.3 | APPROVED / FROZEN / INTEGRATED |
| Related Work B04 V01 / 2.4 | SUPERSEDED_BY_V02 |
| Related Work B04 V02 / 2.4 | APPROVED / FROZEN / INTEGRATED |
| Related Work B05 V01 / 2.5 | APPROVED / FROZEN / INTEGRATED |
| Related Work B06 / 2.6 | AUTHORIZED / ACTIVE |
| Methods B01 V05 | HOLD / NOT APPROVED |
| Methods B01 V06 | NOT AUTHORIZED |

B04 V02 fue integrado mediante D-020. Su desviación histórica se conserva como `NONBLOCKING_PROCESS_DEVIATION` sin reescritura del historial. B05 V01 fue integrado mediante D-024 después de revisión científica independiente, aprobación del autor y cierre técnico en un único commit de tres Markdown bajo D-021–D-023.

### 6. Orden operativo de redacción

| Fase | Entregable | Gate |
|---|---|---|
| 1 | Estructura completa | CLOSED / AUTHOR_APPROVED / FROZEN_FOR_DRAFTING |
| 2 | Related Work | EN PROGRESO; 2.1–2.5 integradas; 2.6 activa |
| 3 | Introduction provisional | Related Work suficientemente estable + claims/RQs autorizados |
| 4 | Decision-support architecture | Introduction/positioning suficientemente estable |
| 5 | Experimental design | arquitectura suficientemente estable + ground truth experimental vigente |
| 6 | Results disponibles y autorizados | claims experimentales autorizados + gate editorial |
| 7 | Figuras/tablas preliminares | secciones relevantes suficientemente estables |
| 8 | Integración experimental pendiente | cierres/gates restantes del Plan Maestro si fueran necesarios |
| 9 | Results definitivos | evidencia requerida cerrada |
| 10 | Discussion + Limitations | Results definitivos + contraste autorizado |
| 11 | Conclusion | Discussion cerrada |
| 12 | Abstract | manuscrito completo |
| 13 | Title + Keywords | Abstract/manuscrito completos |
| 14 | Adaptación final KBS | requisitos vigentes verificados |

Orden activo:

`Related Work → Introduction provisional → Decision-support architecture → Experimental design → Results autorizados → figures/tables → integración experimental pendiente cuando aplique → Results definitivos → Discussion + Limitations → Conclusion → Abstract → Title + Keywords → adaptación final KBS`.

### 7. Estado experimental disponible para fases futuras

D-019 sincroniza el artículo con `SRC-03` después del cierre completo de Grupo 4:

```text
EXPERIMENTAL_PLAN_HEAD = 3ba3557eb10e741b8f49c420850940dee1df08ef
EXPERIMENTAL_MAIN_CHECKPOINT = 38e22c19a0eb0d344e7675761a88d7968091eead
GROUP2 = CLOSED / APPROVED_WITH_NONBLOCKING_LIMITATIONS
GROUP3 = CLOSED / APPROVED
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
GROUP4 = CLOSED / APPROVED
G4_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G4_F02 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G4_F03 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
GROUP5 = NOT_STARTED
G5_F01 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
```

El cierre de Grupo 4 elimina la antigua dependencia editorial de esperar ese cierre para futuros contrastes con literatura, pero no abre automáticamente Experimental design, Results o Discussion y no autoriza Grupo 5.

G4-F03 gobierna el futuro contraste con literatura mediante `docs/analysis/group4/g4_literature_contrast_v0.1.md`: 11 registros, 8 puntos autorizados y 14 prohibidos. Cuando se abra Discussion, ese registro será vinculante. `FINAL_GAP = NOT_DEFINED` y `NOVELTY = NOT_DECLARED` permanecen sin cambios.

### 8. Fase activa — Related Work B06

Related Work se organiza por familias funcionales:

- 2.1 `Automated tariff classification and candidate retrieval` — **APPROVED / FROZEN / INTEGRATED**;
- 2.2 `Knowledge-enhanced retrieval and regulatory reasoning` — **APPROVED / FROZEN / INTEGRATED**;
- 2.3 `LLMs for classification, reasoning, and explanation` — **APPROVED / FROZEN / INTEGRATED**;
- 2.4 `Evidence grounding, explainability, and auditability` — **APPROVED / FROZEN / INTEGRATED**;
- 2.5 `Reproducibility and evaluation in knowledge-based decision support` — **APPROVED / FROZEN / INTEGRATED**;
- 2.6 `Positioning of this study` — **AUTHORIZED / ACTIVE**.

Prompt activo:

`article/prompts/2_RELATED_WORK_B06_POSITIONING_OF_THIS_STUDY.md`

B06 debe cerrar Related Work mediante una síntesis comparativa breve y soportada por fuentes primarias ya admitidas/frozen. No es una búsqueda bibliográfica abierta ni una declaración de novelty. Su función es mostrar dónde se ubica el estudio frente a antecedentes cercanos distinguiendo qué componente fija candidatos, cuándo entra la evidencia normativa, si el LLM puede alterar la decisión y qué función evalúa cada métrica.

El posicionamiento debe reconocer que existen antecedentes parciales y próximos, entre ellos sistemas que combinan candidate prediction con evidence retrieval y trabajos de regulatory AI con evaluación formal de explicación/auditabilidad. El estudio se diferencia de manera defendible por el contrato funcional completo:

```text
EXTERNAL_FIXED_HISTORICAL_RANKING
+ POST_RANKING_NORMATIVE_EVIDENCE_WITHOUT_RERANKING
+ DOWNSTREAM_EXPLANATION_ONLY
+ NO_INSERT_DELETE_SUBSTITUTE_REORDER
+ NO_CLASSIFICATION_FEEDBACK
+ DAM_AWARE_PARTITIONING_WHERE_DEPENDENCE_EXISTS
+ FUNCTION_SPECIFIC_EVALUATION
```

Este contrato es el objeto de posicionamiento. No se autoriza afirmar que cada componente sea nuevo, ni convertir la combinación en novelty absoluta. No se define `FINAL_GAP` en B06.

### 9. Función de las secciones posteriores

- **Introduction:** `problema → enfoques existentes → limitación verificable → consecuencia → propuesta de alto nivel → contribuciones → contexto de evaluación → RQs → roadmap`.
- **Decision-support architecture:** arquitectura general en relaciones entrada–operación–salida, antes de detalles experimentales.
- **Experimental design:** testbed específico, datos históricos, corpus documental, particiones/dependencia, configuración, evaluación, estadística y reproducibilidad.
- **Results:** organizados por función/RQ, no por códigos internos de experimento.
- **Discussion:** interpretación y comparación limitadas por G4-F03; implicaciones, condiciones de transferencia y limitaciones sin SOTA, novelty absoluta, causalidad no identificada ni generalización no evaluada.
- **Conclusion:** `aporte → evidencia principal → alcance → implicación`.

Ninguna de esas secciones se abre automáticamente con la autorización de B06.

### 10. Ciclo obligatorio de cada bloque

1. verificar baseline/master acumulativo vigente;
2. leer onboarding y controles gobernantes una vez por sesión/tarea;
3. verificar fuentes/dependencias necesarias para el bloque;
4. re-recuperar full text primario para cada cita nueva o reusada cuando sea necesario para verificar el claim exacto;
5. redactar exclusivamente el bloque autorizado;
6. incluir comentarios de auditoría anclados a cada cita inglesa;
7. auditar contenido científico, prosa, fluidez y ubicación narrativa;
8. activar IA Experimental solo si existe trigger real;
9. resolver observaciones;
10. versionar en GitHub la respuesta oficial conforme a D-022;
11. solicitar aprobación expresa del autor;
12. integrar al master canónico solo después de aprobación y auditoría.

### 11. Criterios de aprobación

Una sección solo pasa a `APPROVED` cuando cumple su función narrativa, cada claim citado está respaldado por fuente primaria exacta, los comentarios Word contienen pasajes reales y pertinentes, no anticipa resultados ni testbed indebidamente, respeta límites claim–evidencia, mantiene equivalencia EN/ES, preserva artefactos aprobados y recibe aprobación expresa del autor tras auditoría interna.

Para B06, además, se exige:

- reconocimiento explícito de prior art parcial/cercano;
- ausencia de `first/novel/unique/unprecedented` y equivalentes;
- ausencia de universal absence claims;
- ausencia de resultados del presente estudio;
- ausencia de SOTA o superioridad cross-study;
- separación clara entre candidate ranking, documentary evidence y explanation authority;
- `FINAL_GAP = NOT_DEFINED` y `NOVELTY = NOT_DECLARED` preservados.

### 12. Front matter, end matter y journal targeting

Title, Abstract y Keywords se redactan al final. El end matter contemplará `Data availability`, `Code and reproducibility resources` si corresponde, CRediT, Funding, Declaration of competing interest, Acknowledgements si aplica, References y Supplementary material cuando sea necesario.

```text
TARGET_A = Knowledge-Based Systems
PLAN_B = Expert Systems with Applications
PLAN_C = Information Processing & Management
PUBLICATION_ROUTE_KBS = SUBSCRIPTION
```

Antes del paquete final se verificarán nuevamente los requisitos oficiales vigentes de KBS.

---

## English

Writing Plan V2.5 preserves the author-approved KBS structure and cumulative-master policy. Sections 2.1–2.5 are approved, frozen, and integrated. D-024 promotes the approved B05 cumulative Markdown unchanged to `ARTICLE_MASTER_V005.md`, using Git blob `25782b8b2305b546f2f5ff69514893d045e50762`.

Under D-021, the cumulative DOCX is held locally by the author rather than uploaded on every drafting block. The current approved binary has SHA-256 `042952002c2caeb86ec854b0bfcd7332724ddd4712589e25dfddb52718bf159a` and thirty-two citation-audit comments. D-022 keeps substantive Drafting-AI prompts and responses in GitHub; D-023 governs minimal technical closures.

B06 / Section 2.6 is the only active drafting authorization. It must close Related Work with a concise, primary-source-supported positioning synthesis. The section must acknowledge close and partial prior art and distinguish the study through the complete functional contract: fixed historical ranking, post-ranking normative evidence without reranking, downstream explanation-only generation, no candidate modification or classification feedback, DAM-aware dependence control where applicable, and function-specific evaluation.

B06 must not claim absolute novelty, universal absence, SOTA, empirical generalization, legal correctness, or a final literature gap. `FINAL_GAP = NOT_DEFINED` and `NOVELTY = NOT_DECLARED` remain unchanged. Introduction and all later sections remain unauthorized until B06 passes independent review and author approval.

D-019 remains the governing experimental reconciliation after full Group 4 closure: Group 3 is closed, `HE2 = SUPPORTED`, `HE5 = INCONCLUSIVE`, Group 4 is closed/approved, and G4-F01–F03 are integrated. Future Discussion remains constrained by the G4-F03 contrast registry. Group 5 remains not started.
