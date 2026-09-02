# EMPIEZA AQUÍ / START HERE

> **Punto de entrada obligatorio para cualquier persona o IA que trabaje en el artículo científico principal.**  
> **Mandatory entry point for any person or AI working on the main scientific article.**

---

# Español

## 1. Propósito

Este directorio administra la planificación, redacción, revisión y congelamiento del artículo científico principal derivado de la investigación sobre recomendación auditable de subpartidas NANDINA mediante recuperación histórica, evidencia normativa y explicación controlada con un LLM local.

No es el repositorio experimental ni el repositorio final de reproducibilidad. La rama `article/main-manuscript` contiene exclusivamente el proceso editorial y científico del manuscrito.

Antes de realizar cualquier tarea en esta rama, debes leer los archivos indicados en la Sección 2 y reconstruir el estado actual del artículo. No debes asumir que el estado observado en una conversación anterior sigue vigente.

## 2. Orden obligatorio de lectura

Lee, en este orden:

1. `article/START_HERE.md` — protocolo de incorporación y reglas de operación.
2. `article/README.md` — propósito del entorno, flujo de trabajo y regla bilingüe.
3. `article/ARTICLE_STATUS.md` — **fuente de verdad del estado editorial actual**, fase activa, bloqueos y próximos pasos.
4. `article/ARTICLE_WRITING_PLAN.md` — plan maestro de redacción, fases, gates, dependencias y orden de construcción del manuscrito.
5. `article/DECISIONS.md` — decisiones científicas, metodológicas y editoriales ya congeladas.
6. `article/CLAIM_EVIDENCE_MATRIX.md` — claims autorizados, condicionales, pendientes o prohibidos y su soporte evidencial.
7. `article/STYLE_GUIDE.md` — reglas de redacción científica, terminología, equivalencia bilingüe y control de overclaiming.
8. El archivo específico de `article/prompts/`, `article/reviews/` o `article/sections/` relacionado con la tarea asignada.

Si existe contradicción entre una conversación y estos archivos, no la resuelvas silenciosamente. Identifica la contradicción y consulta la fuente de verdad aplicable.

## 3. Regla bilingüe absoluta

Todo contenido creado para el artículo debe existir en **español e inglés**.

Ambas versiones deben decir científicamente lo mismo. Deben conservar la misma:

- afirmación;
- fuerza de la afirmación;
- incertidumbre;
- relación causal o no causal;
- cifra y métrica;
- limitación;
- advertencia;
- cita o referencia;
- condición experimental.

No se permite que una versión sea más fuerte, más general, más completa o más favorable que la otra.

La versión española funciona como control semántico durante el proceso de investigación y revisión. La versión inglesa sirve como base para la futura presentación internacional. Ninguna tiene autorización para introducir contenido científico ausente en la otra.

## 4. Jerarquía de fuentes de verdad

Cuando una tarea requiera comprobar hechos científicos o experimentales, no uses los archivos editoriales como sustituto de las fuentes primarias.

La precedencia documental general es:

1. `PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-09-01_v20.md` o su versión posterior expresamente aprobada — estado experimental actual.
2. `Anexo_1_NANDINA_LLM_RAG_v13.docx` o su versión posterior expresamente aprobada — arquitectura y metodología operativa actual.
3. Proyecto de tesis aprobado — problema, objetivos, hipótesis, justificación y alcance aprobado.
4. Otros documentos de tesis vigentes.
5. Literatura científica utilizada para Related Work, gap y posicionamiento.

Para resultados, artefactos, commits, configuraciones, scripts y trazabilidad experimental, consulta además el repositorio de desarrollo `gci-nandina-rag` y el artefacto congelado correspondiente.

El repositorio `gci-nandina-rag-reproducibility` es el paquete científico de reproducción y replicación y no sustituye al repositorio de desarrollo mientras la campaña experimental siga abierta.

Si una fuente necesaria no está disponible, decláralo como bloqueo. No reconstruyas su contenido a partir de memoria, conocimiento general o una versión antigua.

## 5. Arquitectura científica que debe preservarse

El flujo conceptual oficial es:

```text
Descripción comercial
→ normalización
→ recuperación histórica
→ ranking histórico Top-k
→ Top-3 fijo
→ recuperación de evidencia normativa para esos candidatos
→ construcción de contexto
→ LLM local
→ explicación auditable del Top-3
```

Separación funcional obligatoria:

- **Recuperación histórica:** genera y ordena candidatos.
- **Recuperación normativa:** aporta evidencia documental para los candidatos; no sustituye ni reordena el ranking histórico.
- **LLM local:** explica el Top-3 fijo usando el contexto recuperado; no clasifica desde cero, no introduce códigos externos y no reemplaza el ranking histórico.
- **Reranking mediante LLM:** es diagnóstico salvo decisión experimental posterior expresamente aprobada.

No reformules esta arquitectura sin una decisión registrada en `DECISIONS.md`.

## 6. Límites interpretativos obligatorios

Mientras no exista evidencia expresamente aprobada en sentido contrario:

- `Top-3 candidate retrieval` no debe denominarse `accuracy global del RAG`.
- La asociación de evidencia normativa a un candidato no demuestra por sí sola corrección normativa sustantiva.
- Una explicación estructurada o auditable no equivale automáticamente a corrección jurídica de la clasificación.
- La configurabilidad del framework para otros capítulos, países o profundidades HS no demuestra generalización empírica fuera de la evaluación realizada.
- Las series pertenecientes a una misma DAM no deben tratarse automáticamente como observaciones independientes para inferencia cuando exista dependencia intra-DAM.
- No deben mezclarse métricas provenientes de particiones experimentales incompatibles o contaminadas.
- No deben anticiparse resultados de experimentos cuyo estado sea `PENDING`, `BLOCKED` o todavía no aprobado.
- No debe atribuirse efecto causal al tamaño del banco histórico si el diseño solo permite análisis de sensibilidad bajo restricciones naturales de composición.

La lista completa y vigente de claims autorizados y prohibidos está en `CLAIM_EVIDENCE_MATRIX.md`.

## 7. Cómo determinar el avance actual

No deduzcas el avance a partir de fechas, nombres de commits o conversaciones previas.

Para saber dónde está el artículo:

1. consulta `ARTICLE_STATUS.md`;
2. contrasta la fase con `ARTICLE_WRITING_PLAN.md`;
3. revisa si existen dependencias experimentales pendientes;
4. revisa `DECISIONS.md` y `CLAIM_EVIDENCE_MATRIX.md` antes de redactar;
5. no avances automáticamente a la siguiente fase sin que el gate correspondiente haya sido aprobado.

`ARTICLE_STATUS.md` es la fuente de verdad del progreso editorial y debe actualizarse cuando una fase o bloque cambie de estado.

## 8. Estados editoriales permitidos

Los únicos estados operativos son:

`NOT_STARTED`, `IN_ANALYSIS`, `READY_FOR_DRAFTING`, `DRAFTING`, `INTERNAL_REVIEW`, `EXPERIMENTAL_REVIEW`, `REVISION_REQUIRED`, `APPROVED`, `FROZEN`, `BLOCKED`.

Una sección no puede redactarse solo porque exista un archivo para ella. Debe encontrarse en un estado que autorice la redacción según `ARTICLE_WRITING_PLAN.md` y `ARTICLE_STATUS.md`.

## 9. Protocolo antes de producir trabajo

Antes de redactar, revisar o modificar cualquier contenido, informa explícitamente:

```text
ARCHIVOS LEÍDOS:
FASE ACTIVA:
ESTADO DEL BLOQUE ASIGNADO:
REDACCIÓN AUTORIZADA: SÍ / NO
DECISIONES CONGELADAS RELEVANTES:
CLAIMS AUTORIZADOS RELEVANTES:
CLAIMS PROHIBIDOS O PENDIENTES RELEVANTES:
FUENTES EXTERNAS QUE DEBEN VERIFICARSE:
BLOQUEOS O CONTRADICCIONES DETECTADOS:
```

Si no puedes completar estos campos de manera confiable, no redactes todavía.

## 10. Protocolo de redacción

Cuando la redacción esté autorizada:

1. trabaja únicamente sobre el bloque asignado;
2. usa solo fuentes y claims autorizados;
3. conserva la terminología congelada;
4. redacta primero una versión científicamente controlada y luego su equivalente en el otro idioma, verificando equivalencia semántica oración por oración o claim por claim;
5. no introduzcas resultados, métricas, citas o interpretaciones no proporcionadas o no verificadas;
6. señala cualquier dato que requiera validación en lugar de completarlo por inferencia;
7. aplica `STYLE_GUIDE.md`;
8. entrega el bloque para revisión; no lo declares aprobado por cuenta propia.

## 11. Protocolo de revisión

Toda revisión debe distinguir, como mínimo:

- fidelidad a las fuentes;
- consistencia experimental;
- consistencia metodológica;
- exactitud de claims;
- overclaiming;
- coherencia argumental;
- calidad editorial;
- consistencia terminológica;
- equivalencia español-inglés;
- contradicciones con decisiones congeladas.

El dictamen debe ser uno de:

`PASS`, `PASS WITH CORRECTIONS`, `BLOCKED`.

Una revisión estilística no puede anular una restricción experimental ni una decisión congelada.

## 12. Flujo de aprobación

El flujo oficial es:

```text
planificación del bloque
→ verificación de fuentes y evidencia
→ prompt cerrado de redacción
→ borrador bilingüe
→ auditoría científica/editorial
→ correcciones
→ auditoría experimental independiente
→ resolución de observaciones
→ aprobación del autor
→ integración en la rama
→ actualización de plan, estado, claims y decisiones cuando corresponda
```

No omitas gates por conveniencia.

## 13. Regla para cambios metodológicos o de alcance

Si durante la redacción aparece una propuesta que cambia:

- arquitectura;
- unidad de análisis;
- unidad de agrupamiento;
- particiones;
- métrica;
- hipótesis;
- claim central;
- interpretación experimental;
- alcance de generalización;
- estrategia de revista;

no la incorpores silenciosamente.

Regístrala como decisión pendiente y solicita evaluación antes de modificar el manuscrito o los archivos de control.

## 14. Resultado esperado del onboarding

Una IA correctamente incorporada a esta rama debe ser capaz de responder, antes de trabajar:

- qué artículo se está construyendo;
- cuál es la fase editorial activa;
- qué bloque puede o no puede redactarse;
- qué fuentes gobiernan cada tipo de afirmación;
- qué claims están autorizados, pendientes o prohibidos;
- qué decisiones ya están congeladas;
- cómo debe redactarse y revisarse;
- qué significa la regla bilingüe;
- qué dependencias experimentales siguen abiertas;
- cuál es el siguiente gate.

Si no puede responder todo lo anterior, el onboarding no está completo.

---

# English

## 1. Purpose

This directory manages the planning, drafting, review, and freezing of the main scientific article derived from the research on auditable NANDINA subheading recommendation through historical retrieval, normative evidence, and controlled explanation with a local LLM.

It is neither the experimental repository nor the final reproducibility repository. The `article/main-manuscript` branch contains only the editorial and scientific manuscript process.

Before performing any task on this branch, you must read the files listed in Section 2 and reconstruct the current state of the article. You must not assume that the state observed in a previous conversation is still current.

## 2. Mandatory reading order

Read, in this order:

1. `article/START_HERE.md` — onboarding protocol and operating rules.
2. `article/README.md` — workspace purpose, workflow, and bilingual rule.
3. `article/ARTICLE_STATUS.md` — **source of truth for the current editorial state**, active phase, blockers, and next steps.
4. `article/ARTICLE_WRITING_PLAN.md` — master writing plan, phases, gates, dependencies, and manuscript-construction order.
5. `article/DECISIONS.md` — already frozen scientific, methodological, and editorial decisions.
6. `article/CLAIM_EVIDENCE_MATRIX.md` — authorized, conditional, pending, or prohibited claims and their evidential support.
7. `article/STYLE_GUIDE.md` — scientific writing rules, terminology, bilingual equivalence, and overclaiming control.
8. The specific file under `article/prompts/`, `article/reviews/`, or `article/sections/` related to the assigned task.

If there is a contradiction between a conversation and these files, do not resolve it silently. Identify the contradiction and consult the applicable source of truth.

## 3. Absolute bilingual rule

All content created for the article must exist in **Spanish and English**.

Both versions must communicate the same scientific meaning. They must preserve the same:

- claim;
- claim strength;
- uncertainty;
- causal or non-causal relationship;
- figure and metric;
- limitation;
- warning;
- citation or reference;
- experimental condition.

Neither version may be stronger, more general, more complete, or more favorable than the other.

The Spanish version functions as the semantic-control version during the research and review process. The English version serves as the basis for future international submission. Neither version is authorized to introduce scientific content absent from the other.

## 4. Source-of-truth hierarchy

When a task requires verification of scientific or experimental facts, do not use the editorial files as a substitute for primary sources.

The general documentary precedence is:

1. `PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-09-01_v20.md` or a later version expressly approved — current experimental state.
2. `Anexo_1_NANDINA_LLM_RAG_v13.docx` or a later version expressly approved — current operational architecture and methodology.
3. Approved thesis project — approved problem, objectives, hypotheses, justification, and scope.
4. Other current thesis documents.
5. Scientific literature used for Related Work, gap identification, and positioning.

For results, artifacts, commits, configurations, scripts, and experimental traceability, also consult the `gci-nandina-rag` development repository and the corresponding frozen artifact.

The `gci-nandina-rag-reproducibility` repository is the scientific reproduction and replication package and does not replace the development repository while the experimental campaign remains open.

If a required source is unavailable, declare it as a blocker. Do not reconstruct its content from memory, general knowledge, or an older version.

## 5. Scientific architecture that must be preserved

The official conceptual flow is:

```text
Commercial description
→ normalization
→ historical retrieval
→ historical Top-k ranking
→ fixed Top-3
→ retrieval of normative evidence for those candidates
→ context construction
→ local LLM
→ auditable explanation of the Top-3
```

Mandatory functional separation:

- **Historical retrieval:** generates and ranks candidates.
- **Normative retrieval:** provides documentary evidence for the candidates; it does not replace or reorder the historical ranking.
- **Local LLM:** explains the fixed Top-3 using the retrieved context; it does not classify from scratch, introduce external codes, or replace the historical ranking.
- **LLM reranking:** is diagnostic unless a later experimental decision expressly approves otherwise.

Do not reformulate this architecture without a decision recorded in `DECISIONS.md`.

## 6. Mandatory interpretation boundaries

Unless expressly approved evidence establishes otherwise:

- `Top-3 candidate retrieval` must not be described as `global RAG accuracy`.
- Associating normative evidence with a candidate does not by itself demonstrate substantive normative correctness.
- A structured or auditable explanation does not automatically equal legal correctness of the classification.
- Framework configurability for other chapters, countries, or HS depths does not demonstrate empirical generalization beyond the performed evaluation.
- Series belonging to the same DAM must not automatically be treated as independent observations for inference when intra-DAM dependence exists.
- Metrics from incompatible or contaminated experimental partitions must not be mixed.
- Results from experiments whose status is `PENDING`, `BLOCKED`, or not yet approved must not be anticipated.
- A causal effect must not be attributed to historical-bank size when the design only supports sensitivity analysis under natural composition constraints.

The complete and current list of authorized and prohibited claims is in `CLAIM_EVIDENCE_MATRIX.md`.

## 7. How to determine current progress

Do not infer progress from dates, commit names, or previous conversations.

To determine where the article stands:

1. consult `ARTICLE_STATUS.md`;
2. cross-check the phase against `ARTICLE_WRITING_PLAN.md`;
3. inspect whether experimental dependencies remain pending;
4. review `DECISIONS.md` and `CLAIM_EVIDENCE_MATRIX.md` before drafting;
5. do not advance automatically to the next phase unless the corresponding gate has been approved.

`ARTICLE_STATUS.md` is the source of truth for editorial progress and must be updated whenever a phase or block changes state.

## 8. Allowed editorial states

The only operating states are:

`NOT_STARTED`, `IN_ANALYSIS`, `READY_FOR_DRAFTING`, `DRAFTING`, `INTERNAL_REVIEW`, `EXPERIMENTAL_REVIEW`, `REVISION_REQUIRED`, `APPROVED`, `FROZEN`, `BLOCKED`.

A section cannot be drafted merely because a file exists for it. It must be in a state that authorizes drafting under `ARTICLE_WRITING_PLAN.md` and `ARTICLE_STATUS.md`.

## 9. Protocol before producing work

Before drafting, reviewing, or modifying any content, explicitly report:

```text
FILES READ:
ACTIVE PHASE:
ASSIGNED BLOCK STATUS:
DRAFTING AUTHORIZED: YES / NO
RELEVANT FROZEN DECISIONS:
RELEVANT AUTHORIZED CLAIMS:
RELEVANT PROHIBITED OR PENDING CLAIMS:
EXTERNAL SOURCES THAT MUST BE VERIFIED:
DETECTED BLOCKERS OR CONTRADICTIONS:
```

If you cannot complete these fields reliably, do not draft yet.

## 10. Drafting protocol

When drafting is authorized:

1. work only on the assigned block;
2. use only authorized sources and claims;
3. preserve frozen terminology;
4. draft a scientifically controlled version first and then its equivalent in the other language, verifying semantic equivalence sentence by sentence or claim by claim;
5. do not introduce results, metrics, citations, or interpretations that were not provided or verified;
6. flag any datum requiring validation instead of completing it by inference;
7. apply `STYLE_GUIDE.md`;
8. submit the block for review; do not declare it approved yourself.

## 11. Review protocol

Every review must distinguish, at minimum:

- source fidelity;
- experimental consistency;
- methodological consistency;
- claim accuracy;
- overclaiming;
- argumentative coherence;
- editorial quality;
- terminological consistency;
- Spanish-English equivalence;
- contradictions with frozen decisions.

The verdict must be one of:

`PASS`, `PASS WITH CORRECTIONS`, `BLOCKED`.

A stylistic review cannot override an experimental restriction or a frozen decision.

## 12. Approval workflow

The official workflow is:

```text
block planning
→ source and evidence verification
→ constrained drafting prompt
→ bilingual draft
→ scientific/editorial audit
→ corrections
→ independent experimental audit
→ resolution of observations
→ author approval
→ branch integration
→ update of plan, status, claims, and decisions when applicable
```

Do not skip gates for convenience.

## 13. Rule for methodological or scope changes

If drafting produces a proposal that changes:

- architecture;
- analysis unit;
- grouping unit;
- partitions;
- metric;
- hypothesis;
- central claim;
- experimental interpretation;
- generalization scope;
- journal strategy;

do not incorporate it silently.

Record it as a pending decision and request evaluation before modifying the manuscript or control files.

## 14. Expected onboarding outcome

An AI correctly onboarded to this branch must be able to answer, before working:

- what article is being built;
- what the active editorial phase is;
- what block may or may not be drafted;
- what sources govern each type of statement;
- what claims are authorized, pending, or prohibited;
- what decisions are already frozen;
- how content must be drafted and reviewed;
- what the bilingual rule means;
- what experimental dependencies remain open;
- what the next gate is.

If it cannot answer all of the above, onboarding is not complete.
