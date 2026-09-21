# Plan maestro de redacción / Master Writing Plan

```text
PLAN_VERSION = V2.6
TARGET_JOURNAL = Knowledge-Based Systems
ARTICLE_TYPE = Research article
EDITORIAL_BASIS = KBS_EWG_34_V01
STRUCTURE_RESET_DECISION = D-014
STRUCTURE_APPROVAL_DECISION = D-015
EXPERIMENTAL_RECONCILIATION_DECISION = D-019
DOCX_CUSTODY_DECISION = D-021
GITHUB_ONLY_RESPONSE_DECISION = D-022
TECHNICAL_CLOSURE_MODE_DECISION = D-023
RELATED_WORK_CLOSURE_DECISION = D-025
LATEST_EDITORIAL_DECISION = D-026
LEGACY_METHODS_FIRST_ORDER = SUPERSEDED
STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V01.md
STRUCTURE_STATUS = AUTHOR_APPROVED / FROZEN_FOR_DRAFTING
CANONICAL_MASTER = ARTICLE_MASTER_V006
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V006.md
CANONICAL_MASTER_MD_GIT_BLOB = 7d3c7a71cd6578ffc0b93df80ea12e4172833a1a
CANONICAL_MASTER_DOCX = LOCAL_AUTHOR_CUSTODY / D021
CANONICAL_MASTER_DOCX_SOURCE_FILENAME = ARTICLE_MASTER_CANDIDATE_RW_B06_V01.docx
CANONICAL_MASTER_DOCX_SHA256 = 3a07568b8f6ac80ed2df39ee60c0aab65c06df5bb3e1988d3e4f8c752d84bf0
CANONICAL_CITATION_COMMENTS = 36
CURRENT_DRAFTING_PHASE = INTRODUCTION
CURRENT_AUTHORIZED_BLOCK = INTRODUCTION_B01 / SECTION_1_PROVISIONAL_ONLY
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

## Español

### 1. Propósito

Administrar la construcción iterativa del artículo científico principal sin anticipar resultados, alterar el diseño experimental aprobado ni trasladar al manuscrito la lógica de un documento de gobernanza. El artículo se construye sobre una estructura acumulativa aprobada y cada bloque autorizado completa esa misma base.

La redacción se rige por `KBS_EWG_34_V01`, `MWDP_V1.0`, SPCCR, la Claim–Evidence Matrix, la literatura congelada de 0B, el posicionamiento 0C y las fuentes experimentales gobernantes cuando correspondan.

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
- En Introduction y secciones posteriores, las abstracciones deben traducirse a componentes, acciones, entradas, salidas y restricciones observables.

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
2. El baseline Markdown actual es `ARTICLE_MASTER_V006.md`, blob Git `7d3c7a71cd6578ffc0b93df80ea12e4172833a1a`.
3. Conforme a D-021, el baseline DOCX actual permanece bajo custodia local del autor. El binario aprobado procede de `ARTICLE_MASTER_CANDIDATE_RW_B06_V01.docx`, SHA-256 `3a07568b8f6ac80ed2df39ee60c0aab65c06df5bb3e1988d3e4f8c752d84bf0`.
4. Un renombrado local a `ARTICLE_MASTER_V006.docx` es aceptable solo si no modifica bytes y conserva exactamente el SHA-256 gobernante.
5. No se crean Words independientes por sección.
6. La sección nueva se inserta en su ubicación estructural.
7. Solo se eliminan las notas editoriales correspondientes a la sección completada.
8. Part I y Part II conservan equivalencia semántica.
9. Candidatos no se vuelven canónicos hasta aprobación expresa del autor y auditoría de la IA Gestora.
10. Si el baseline DOCX exacto no está disponible, la IA de Redacción se detiene con `BASELINE_DOCX_ACCESS_REQUIRED`; no reconstruye silenciosamente el Word desde Markdown.
11. Todo bloque preserva exactamente texto y comentarios de las secciones aprobadas.
12. El SHA-256 del DOCX candidato se registra obligatoriamente en la respuesta versionada en GitHub; la carga del binario queda diferida conforme a D-021 salvo hito explícito.
13. Desviaciones de proceso se registran explícitamente y no se corrigen mediante reescritura destructiva del historial salvo autorización expresa del autor y justificación de gobernanza.
14. D-022 exige prompts y respuestas sustantivas en GitHub; el chat de la IA de Redacción solo puede contener el puntero mínimo autorizado.
15. D-023 aplica a cierres puramente técnicos: sin Base64 para Markdown, sin fragmentación, sin verificaciones redundantes y sin reauditoría científica innecesaria.
16. D-026 registra la recuperación del master V006 tras una desviación técnica; el blob canónico de V006 es el indicado en este plan.

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
| Related Work B06 V01 / 2.6 | APPROVED / FROZEN / INTEGRATED |
| Related Work | CLOSED / APPROVED / FROZEN |
| Introduction B01 | AUTHORIZED / ACTIVE / PROVISIONAL |
| Methods B01 V05 | HOLD / NOT APPROVED |
| Methods B01 V06 | NOT AUTHORIZED |

B06 V01 fue integrado mediante D-025 después de revisión científica independiente y aprobación expresa del autor. Su revisión V02 corrige únicamente el conteo de páginas renderizadas a `28/28`; no cambia el `PASS` científico. D-026 conserva transparentemente la desviación técnica del placeholder V006 y su recuperación posterior sin reescritura del historial.

### 6. Orden operativo de redacción

| Fase | Entregable | Gate |
|---|---|---|
| 1 | Estructura completa | CLOSED / AUTHOR_APPROVED / FROZEN_FOR_DRAFTING |
| 2 | Related Work | CLOSED / APPROVED / FROZEN |
| 3 | Introduction provisional | EN PROGRESO / B01 AUTHORIZED |
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

`Introduction provisional → Decision-support architecture → Experimental design → Results autorizados → figures/tables → integración experimental pendiente cuando aplique → Results definitivos → Discussion + Limitations → Conclusion → Abstract → Title + Keywords → adaptación final KBS`.

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

### 8. Fase activa — Introduction B01

Prompt activo:

`article/prompts/3_INTRODUCTION_B01_PROVISIONAL.md`

La Introduction debe seguir la secuencia narrativa:

`problema concreto → enfoques existentes → limitación verificable → consecuencia → propuesta de alto nivel → contribuciones acotadas → contexto de evaluación → RQs → roadmap`.

La limitación no puede formularse como ausencia universal de trabajos previos. Related Work ya estableció prior art de clasificación directa, candidate prediction + evidence retrieval, sistemas regulatorios donde evidencia/LLM intervienen en búsqueda o decisión, y regulatory AI con evaluación explícita de explicación/source support.

La propuesta debe describir acciones concretas:

1. la recuperación histórica genera y ordena candidatos;
2. el Top-3 queda fijado antes de recuperar normativa;
3. la evidencia normativa se asocia a candidatos ya fijados sin alterar el ranking;
4. el LLM local downstream explica sin insertar, eliminar, sustituir, reordenar ni retroalimentar clasificación;
5. ranking, evidencia y explicación se evalúan con métricas alineadas a su función;
6. DAM se usa como agrupamiento cuando existe dependencia.

Las contribuciones autorizadas son acotadas:

- formalización arquitectónica-metodológica de esa separación funcional;
- evaluación por función con control de dependencia;
- reproducibilidad/reinstanciación del procedimiento con banco histórico, espacio de clases y corpus documental alternativos.

La tercera contribución expresa configurabilidad/replicabilidad del procedimiento, no generalización empírica de los resultados.

La Introduction debe introducir el testbed solo después de la propuesta/contribuciones y presentar RQ1–RQ4 sin códigos internos de gobernanza o experimento.

### 9. Función de las secciones posteriores

- **Decision-support architecture:** arquitectura general en relaciones entrada–operación–salida, antes de detalles experimentales.
- **Experimental design:** testbed específico, datos históricos, corpus documental, particiones/dependencia, configuración, evaluación, estadística y reproducibilidad.
- **Results:** organizados por función/RQ, no por códigos internos de experimento.
- **Discussion:** interpretación y comparación limitadas por G4-F03; implicaciones, condiciones de transferencia y limitaciones sin SOTA, novelty absoluta, causalidad no identificada ni generalización no evaluada.
- **Conclusion:** `aporte → evidencia principal → alcance → implicación`.

Ninguna de esas secciones se abre automáticamente con la autorización de Introduction B01.

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

Para Introduction B01, además, se exige:

- problema concreto y no retórica genérica sobre IA;
- limitación técnica soportada por Related Work y fuentes primarias;
- propuesta de alto nivel expresada con componentes y acciones observables;
- contribuciones separadas de features y de novelty;
- testbed presentado después de la propuesta;
- RQ1–RQ4 semánticamente alineadas con 0C y sin códigos internos;
- mención acotada de reproducibilidad/configurabilidad sin generalización;
- ausencia de resultados, SOTA, universal-absence claims y legal-correctness claims;
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

Writing Plan V2.6 closes Related Work after B06 V01 passed independent review and explicit author approval. D-025 promotes the approved B06 cumulative Markdown unchanged to `ARTICLE_MASTER_V006.md`, using Git blob `7d3c7a71cd6578ffc0b93df80ea12e4172833a1a`.

Under D-021, the cumulative DOCX remains in author-local custody with SHA-256 `3a07568b8f6ac80ed2df39ee60c0aab65c06df5bb3e1988d3e4f8c752d84bf0` and thirty-six citation-audit comments. The corrected render record is `28/28 PASS`. D-026 records and transparently preserves the technical placeholder-recovery deviation; the canonical V006 blob is unchanged from the approved B06 candidate.

Introduction B01 is the only active drafting authorization. It must establish the concrete problem, verified limitation, high-level proposal, bounded contributions, evaluation context, retained RQs, and roadmap. The proposal must concretely state that historical retrieval fixes the Top-3, normative retrieval documents those fixed candidates without reranking, and the downstream local LLM explains without classification authority.

The Introduction may state that the documented procedure can be re-instantiated with alternative historical data, label spaces, and documentary corpora, but this must not be converted into empirical generalization. It must not claim absolute novelty, universal absence, SOTA, study results, or legal correctness. `FINAL_GAP = NOT_DEFINED` and `NOVELTY = NOT_DECLARED` remain unchanged.

D-019 remains the governing experimental reconciliation after full Group 4 closure. Future Discussion remains constrained by the G4-F03 contrast registry. Group 5 remains not started.
