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
2. `article/README.md` — propósito del entorno y flujo de trabajo.
3. `article/ARTICLE_STATUS.md` — **fuente de verdad del estado editorial actual**, fase activa, bloqueos y próximos pasos.
4. `article/ARTICLE_WRITING_PLAN.md` — plan maestro de redacción, fases, gates, dependencias y orden de construcción del manuscrito.
5. `article/DECISIONS.md` — decisiones científicas, metodológicas y editoriales ya congeladas.
6. `article/SOURCE_REGISTRY.md` — fuentes nucleares, ubicación, precedencia y reglas de versionamiento.
7. `article/CLAIM_EVIDENCE_MATRIX.md` — claims autorizados, condicionales, pendientes o prohibidos y su soporte evidencial.
8. `article/STYLE_GUIDE.md` — reglas de redacción científica, terminología, equivalencia bilingüe de artefactos y control de overclaiming.
9. El archivo específico de `article/prompts/`, `article/reviews/` o `article/sections/` relacionado con la tarea asignada.

Si existe contradicción entre una conversación y estos archivos, no la resuelvas silenciosamente. Identifica la contradicción y consulta la fuente de verdad aplicable.

## 3. Idioma del chat y regla bilingüe de GitHub

Las respuestas al autor dentro del **chat deben emitirse en español**, salvo que el autor solicite expresamente otro idioma.

La obligación de bilingüismo aplica exclusivamente a los **artefactos que se crean o integran en GitHub** dentro del entorno del artículo. Todo artefacto versionado de redacción, planificación, revisión, decisión o control editorial debe existir en español e inglés con equivalencia semántica.

En los artefactos GitHub, ambas versiones deben conservar la misma:

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

La versión española funciona como control semántico. La versión inglesa sirve como base para una futura presentación internacional. **No se debe duplicar en inglés una respuesta ordinaria del chat.** Si esa respuesta se aprueba posteriormente para GitHub, entonces el artefacto versionado debe generarse en ambos idiomas.

## 4. Jerarquía de fuentes de verdad

Cuando una tarea requiera comprobar hechos científicos o experimentales, no uses los archivos editoriales como sustituto de las fuentes primarias.

La precedencia documental general es:

1. Plan Maestro experimental definido como `SRC-03` en `SOURCE_REGISTRY.md` — estado experimental actual.
2. `Anexo_1_NANDINA_LLM_RAG_v13.docx` o versión posterior expresamente aprobada — arquitectura y metodología operativa actual.
3. Proyecto de tesis aprobado — problema, objetivos, hipótesis, justificación y alcance aprobados.
4. Otros documentos de tesis vigentes.
5. Literatura científica utilizada para Related Work, gap y posicionamiento.

Para resultados, artefactos, commits, configuraciones, scripts y trazabilidad experimental, consulta además el repositorio de desarrollo `gci-nandina-rag` y el artefacto congelado correspondiente.

`SRC-03` es una fuente viva mientras la investigación siga abierta. Su rama y ruta determinan la fuente operativa; el blob SHA leído debe registrarse como snapshot de cada corte. Un cambio de blob SHA en la misma rama/ruta no es por sí solo un bloqueo: debe verificarse si cambia hechos, claims, resultados o decisiones ya utilizados.

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
4. revisa `DECISIONS.md`, `SOURCE_REGISTRY.md` y `CLAIM_EVIDENCE_MATRIX.md` antes de redactar;
5. no avances automáticamente a la siguiente fase sin que el gate correspondiente haya sido aprobado.

`ARTICLE_STATUS.md` es la fuente de verdad del progreso editorial y debe actualizarse cuando una fase o bloque cambie de estado.

## 8. Estados editoriales permitidos

Los únicos estados operativos son:

`NOT_STARTED`, `IN_ANALYSIS`, `READY_FOR_DRAFTING`, `DRAFTING`, `INTERNAL_REVIEW`, `EXPERIMENTAL_REVIEW`, `REVISION_REQUIRED`, `APPROVED`, `FROZEN`, `BLOCKED`.

Una sección no puede redactarse solo porque exista un archivo para ella. Debe encontrarse en un estado que autorice la redacción según `ARTICLE_WRITING_PLAN.md` y `ARTICLE_STATUS.md`.

## 9. Protocolo antes de producir trabajo

Antes de redactar, revisar o modificar cualquier contenido, informa explícitamente en español:

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
4. entrega en chat la versión de trabajo en español, salvo que el prompt específico indique que debe producirse directamente un artefacto GitHub;
5. si el contenido es aprobado para integración, genera el artefacto GitHub en español e inglés y verifica equivalencia semántica oración por oración o claim por claim;
6. no introduzcas resultados, métricas, citas o interpretaciones no proporcionadas o no verificadas;
7. señala cualquier dato que requiera validación en lugar de completarlo por inferencia;
8. aplica `STYLE_GUIDE.md`;
9. entrega el bloque para revisión; no lo declares aprobado por cuenta propia.

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
- equivalencia español-inglés cuando se revise un artefacto GitHub bilingüe;
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
→ borrador de trabajo en español
→ auditoría científica/editorial
→ correcciones
→ auditoría experimental independiente cuando corresponda
→ resolución de observaciones
→ aprobación del autor
→ generación/verificación del artefacto bilingüe
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
- que el chat se responde en español y que el bilingüismo aplica a artefactos GitHub;
- qué dependencias experimentales siguen abiertas;
- cuál es el siguiente gate.

Si no puede responder todo lo anterior, el onboarding no está completo.

---

# English

## 1. Purpose

This directory manages the planning, drafting, review, and freezing of the main scientific article derived from the research on auditable NANDINA subheading recommendation through historical retrieval, normative evidence, and controlled explanation with a local LLM.

It is neither the experimental repository nor the final reproducibility repository. The `article/main-manuscript` branch contains only the editorial and scientific manuscript process.

Before performing any task on this branch, read the files listed in Section 2 and reconstruct the current state of the article. Do not assume that a state observed in a previous conversation is still current.

## 2. Mandatory reading order

Read, in this order:

1. `article/START_HERE.md` — onboarding protocol and operating rules.
2. `article/README.md` — workspace purpose and workflow.
3. `article/ARTICLE_STATUS.md` — **source of truth for the current editorial state**, active phase, blockers, and next steps.
4. `article/ARTICLE_WRITING_PLAN.md` — master writing plan, phases, gates, dependencies, and manuscript-construction order.
5. `article/DECISIONS.md` — frozen scientific, methodological, and editorial decisions.
6. `article/SOURCE_REGISTRY.md` — nuclear sources, location, precedence, and versioning rules.
7. `article/CLAIM_EVIDENCE_MATRIX.md` — authorized, conditional, pending, or prohibited claims and their evidential support.
8. `article/STYLE_GUIDE.md` — scientific writing rules, terminology, bilingual artifact equivalence, and overclaiming control.
9. The specific file under `article/prompts/`, `article/reviews/`, or `article/sections/` related to the assigned task.

If a conversation conflicts with these files, do not resolve the contradiction silently. Identify it and consult the applicable source of truth.

## 3. Chat language and GitHub bilingual rule

Responses to the author in **chat must be in Spanish**, unless the author expressly requests another language.

The bilingual requirement applies exclusively to **artifacts created or integrated into GitHub** within the article workspace. Every versioned writing, planning, review, decision, or editorial-control artifact must exist in Spanish and English with semantic equivalence.

For GitHub artifacts, both versions must preserve the same claim, claim strength, uncertainty, causal status, figures, metrics, limitations, warnings, citations, and experimental conditions. Neither version may be stronger, more general, more complete, or more favorable than the other.

The Spanish version is the semantic-control version and the English version is the basis for future international submission. **Ordinary chat responses must not be duplicated in English.** If chat content is later approved for GitHub, the versioned artifact must then be generated in both languages.

## 4. Source-of-truth hierarchy

Do not use editorial control files as substitutes for primary scientific or experimental sources.

The general precedence is:

1. Experimental Master Plan defined as `SRC-03` in `SOURCE_REGISTRY.md` — current experimental status.
2. `Anexo_1_NANDINA_LLM_RAG_v13.docx` or a later expressly approved version — current operational architecture and methodology.
3. Approved thesis project — approved problem, objectives, hypotheses, justification, and scope.
4. Other current thesis documents.
5. Scientific literature used for Related Work, gap identification, and positioning.

For results, artifacts, commits, configurations, scripts, and experimental traceability, also consult the `gci-nandina-rag` development repository and the corresponding frozen artifact.

`SRC-03` is a living source while the research remains open. Its branch and path define the operational source; the blob SHA actually read is recorded as the snapshot for each cutoff. A changed blob SHA on the same branch/path is not by itself a blocker: determine whether it changes facts, claims, results, or decisions already used.

The `gci-nandina-rag-reproducibility` repository is the scientific reproduction and replication package and does not replace the development repository while the experimental campaign remains open.

If a required source is unavailable, declare it as a blocker. Do not reconstruct it from memory, general knowledge, or an older version.

## 5. Scientific architecture that must be preserved

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

Mandatory separation:

- **Historical retrieval:** generates and ranks candidates.
- **Normative retrieval:** provides documentary evidence; it does not replace or reorder the historical ranking.
- **Local LLM:** explains the fixed Top-3 using retrieved context; it does not classify from scratch, introduce external codes, or replace the ranking.
- **LLM reranking:** diagnostic unless a later experimental decision expressly approves otherwise.

Do not reformulate this architecture without a decision recorded in `DECISIONS.md`.

## 6. Mandatory interpretation boundaries

Unless expressly approved evidence establishes otherwise:

- `Top-3 candidate retrieval` is not `global RAG accuracy`.
- Candidate-linked normative evidence does not by itself establish substantive normative correctness.
- An auditable explanation does not automatically equal legal correctness.
- Configurability does not establish empirical generalization beyond the performed evaluation.
- Series from the same DAM must not automatically be treated as independent for inference when intra-DAM dependence exists.
- Metrics from incompatible or contaminated partitions must not be mixed.
- Pending or blocked results must not be anticipated.
- Historical-bank size must not be given a causal interpretation when the design supports only sensitivity under natural composition constraints.

See `CLAIM_EVIDENCE_MATRIX.md` for the complete current claim policy.

## 7. How to determine current progress

1. Consult `ARTICLE_STATUS.md`.
2. Cross-check the phase against `ARTICLE_WRITING_PLAN.md`.
3. Inspect pending experimental dependencies.
4. Review `DECISIONS.md`, `SOURCE_REGISTRY.md`, and `CLAIM_EVIDENCE_MATRIX.md` before drafting.
5. Do not advance automatically without the corresponding approved gate.

`ARTICLE_STATUS.md` is the source of truth for editorial progress.

## 8. Allowed editorial states

`NOT_STARTED`, `IN_ANALYSIS`, `READY_FOR_DRAFTING`, `DRAFTING`, `INTERNAL_REVIEW`, `EXPERIMENTAL_REVIEW`, `REVISION_REQUIRED`, `APPROVED`, `FROZEN`, `BLOCKED`.

A section cannot be drafted merely because a file exists for it.

## 9. Protocol before producing work

Before drafting, reviewing, or modifying content, report the onboarding fields required by the Spanish section. The report itself must be delivered to the author in Spanish.

If the fields cannot be completed reliably, do not draft.

## 10. Drafting protocol

When drafting is authorized:

1. work only on the assigned block;
2. use only authorized sources and claims;
3. preserve frozen terminology;
4. deliver the working version in chat in Spanish unless the specific task directly requests a GitHub artifact;
5. when approved for integration, generate the GitHub artifact in Spanish and English and verify semantic equivalence;
6. do not introduce unverified results, metrics, citations, or interpretations;
7. flag data requiring validation rather than inferring it;
8. apply `STYLE_GUIDE.md`;
9. submit the block for review and do not self-approve it.

## 11. Review protocol

Every review must distinguish source fidelity, experimental consistency, methodological consistency, claim accuracy, overclaiming, argumentative coherence, editorial quality, terminology, contradictions with frozen decisions, and Spanish-English equivalence when a bilingual GitHub artifact is being reviewed.

Verdict: `PASS`, `PASS WITH CORRECTIONS`, or `BLOCKED`.

A stylistic review cannot override an experimental restriction or frozen decision.

## 12. Approval workflow

```text
block planning
→ source and evidence verification
→ constrained drafting prompt
→ Spanish working draft in chat
→ scientific/editorial audit
→ corrections
→ independent experimental audit when applicable
→ resolution of observations
→ author approval
→ bilingual artifact generation/verification
→ branch integration
→ update plan, status, claims, and decisions when applicable
```

Do not skip gates for convenience.

## 13. Rule for methodological or scope changes

Do not silently incorporate changes to architecture, analysis unit, grouping unit, partitions, metrics, hypotheses, central claims, experimental interpretation, generalization scope, or journal strategy. Record them as pending decisions and request evaluation.

## 14. Expected onboarding outcome

A correctly onboarded AI must be able to state what article is being built, the active phase, what may or may not be drafted, governing sources, authorized/pending/prohibited claims, frozen decisions, drafting and review rules, that chat responses are in Spanish while GitHub artifacts are bilingual, open experimental dependencies, and the next gate.

If it cannot do so, onboarding is incomplete.
