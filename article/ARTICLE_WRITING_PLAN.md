# Plan maestro de redacción / Master Writing Plan

```text
PLAN_VERSION = V2.0
TARGET_JOURNAL = Knowledge-Based Systems
ARTICLE_TYPE = Research article
EDITORIAL_BASIS = KBS_EWG_34_V01
STRUCTURE_DECISION = D-014
LEGACY_METHODS_FIRST_ORDER = SUPERSEDED
WORKING_STRUCTURE = article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V01.md
WORKING_STRUCTURE_STATUS = WORKING / AUTHOR_EDITABLE / NOT_YET_FROZEN
```

## Español

### 1. Propósito

Administrar la construcción iterativa del artículo científico principal sin anticipar resultados, alterar el diseño experimental aprobado ni trasladar al manuscrito la lógica de un documento de gobernanza. El artículo se construirá sobre una **estructura acumulativa completa** y cada nueva versión deberá completar o corregir esa misma base, no crear documentos independientes por sección.

La redacción se guía por la evidencia editorial empírica de 34 artículos recientes de *Knowledge-Based Systems* (`KBS_EWG_34_V01`) y por las restricciones científicas ya congeladas del proyecto.

### 2. Principios rectores

- El artículo no será una versión abreviada de la tesis.
- El lector debe comprender primero el **problema y el posicionamiento**, después la **arquitectura general**, y solo entonces la **instanciación experimental específica**.
- El testbed NANDINA/Chapter-Class 87 y el corpus documental concreto no deben definir prematuramente el alcance conceptual de la arquitectura.
- La recuperación histórica genera y ordena candidatos.
- El conjunto Top-3 queda fijado antes de la recuperación documental y de la generación.
- La recuperación documental aporta evidencia para candidatos ya fijados y no sustituye ni reordena el ranking histórico.
- El LLM local opera después de la recuperación y se utiliza para explicación controlada; no clasifica desde cero ni retroalimenta la selección de candidatos.
- Candidate retrieval ≠ overall classification accuracy.
- Documentary association ≠ substantive legal correctness.
- Auditability ≠ legal correctness.
- Configurability/replicability ≠ empirical generalization.
- SERIE es la unidad de observación/análisis; DAM es unidad de agrupamiento cuando existe dependencia.
- Ningún resultado pendiente podrá redactarse como hallazgo.
- Todo claim debe estar trazado a evidencia autorizada.
- La parte inglesa es el manuscript master de publicación y la parte española funciona como espejo de control semántico.

### 3. Arquitectura acumulativa del artículo

La estructura de trabajo vigente es:

1. `Introduction`
2. `Related work`
3. `Decision-support architecture`
4. `Experimental design`
5. `Results`
6. `Discussion`
7. `Conclusion`
8. end matter de KBS.

La estructura detallada y editable está en:

`article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V01.md`

El Word editable correspondiente es `KBS_ARTICLE_WORKING_STRUCTURE_V01.docx`. Las futuras entregas deben preservar esa estructura acumulativa y completar progresivamente sus secciones. No se autoriza reconstruir el manuscrito desde cero ni entregar bloques aislados que no se integren en la base acumulativa.

`Limitations` permanece como subsección final de `Discussion` mientras la redacción definitiva no justifique elevarla a sección principal.

### 4. Estado del trabajo previo

| Fase histórica | Estado |
|---|---|
| 0A — Ground truth documental y experimental | CLOSED / APPROVED |
| 0B — Mapa crítico de literatura y taxonomía | CLOSED / APPROVED / FROZEN |
| 0C — Posicionamiento científico y RQs | CLOSED / APPROVED / FROZEN |
| 0D — Arquitectura editorial original | CLOSED / APPROVED / FROZEN, con estructura de secciones supersedida por D-014 |
| KBS-34 empirical writing guide | AUTHOR_APPROVED / ACTIVE / BINDING |
| Methods B01 V05 | HOLD / NOT APPROVED |
| Methods B01 V06 | NOT AUTHORIZED |

D-014 modifica únicamente la **arquitectura editorial y el orden de redacción**. No modifica el alcance científico, las RQ, la Claim–Evidence Matrix ni la gobernanza experimental.

### 5. Nuevo orden operativo de redacción

Una vez que el autor termine de editar y apruebe la estructura `KBS_ARTICLE_WORKING_STRUCTURE_V01`, el orden de trabajo será:

| Fase nueva | Entregable | Gate |
|---|---|---|
| 1 | Estructura completa del artículo | aprobación explícita del autor |
| 2 | Related Work | estructura aprobada + literatura 0B congelada |
| 3 | Introduction provisional | Related Work suficientemente estable + claims/RQs autorizados |
| 4 | Decision-support architecture | Introduction/positioning suficientemente estable |
| 5 | Experimental design | arquitectura suficientemente estable + ground truth experimental vigente |
| 6 | Results actualmente disponibles y autorizados | claims experimentales autorizados |
| 7 | Figuras y tablas preliminares | secciones 2–6 suficientemente estables |
| 8 | Integración de resultados experimentales pendientes | cierres/gates del Plan Maestro experimental |
| 9 | Results definitivos | Fase 8 cerrada |
| 10 | Discussion + Limitations | Results definitivos |
| 11 | Conclusion | Discussion cerrada |
| 12 | Abstract | manuscrito completo y resultados finales |
| 13 | Title + Keywords | Abstract y manuscrito completo |
| 14 | Adaptación final KBS | requisitos vigentes de submission verificados |

Este orden es una decisión de gobernanza para reducir reescritura y evitar que Methods/Experimental Design carguen con funciones retóricas que corresponden a Introduction/Related Work. No se presenta como una inferencia sobre el orden real de escritura seguido por los autores del corpus KBS-34.

### 6. Contenido esperado por sección

#### 1. Introduction

Debe conducir al lector por:

`problema → enfoques existentes → limitación técnica verificable → consecuencia → propuesta de alto nivel → contribuciones → contexto de evaluación → RQs → roadmap`.

La propuesta debe ser comprensible antes de introducir en detalle NANDINA/Chapter-Class 87 y el corpus experimental concreto.

#### 2. Related Work

Se organiza por familias funcionales, no autor por autor:

- automated tariff classification and candidate retrieval;
- knowledge-enhanced retrieval and regulatory reasoning;
- LLMs for classification, reasoning and explanation;
- evidence grounding, explainability and auditability;
- reproducibility and evaluation in knowledge-based decision support;
- positioning synthesis.

Cada subsección debe terminar conectando la literatura con el problema actual. La ausencia dentro del alcance revisado no equivale a novelty universal.

#### 3. Decision-support architecture

Debe explicar la arquitectura general mediante relaciones concretas de entrada–operación–salida:

`query → historical retrieval → ranked candidates → fixed Top-3 → candidate-specific documentary retrieval → evidence-context construction → local LLM → controlled explanation`.

Aquí se explican también configurabilidad y requisitos de interfaz. No debe abrirse con tamaños de muestra, H100, Chapter 87 ni el corpus peruano.

#### 4. Experimental design

Aquí se introduce la instanciación empírica concreta:

- evaluation setting/testbed;
- historical data;
- documentary corpus;
- partitioning and dependence control;
- system configuration;
- RQ-to-metric evaluation framework;
- candidate-retrieval evaluation;
- documentary-evidence evaluation;
- controlled-explanation evaluation;
- statistical analysis;
- reproducibility resources.

Esta sección debe identificar expresamente el repositorio público de reproducibilidad y el alcance de los artefactos disponibles.

#### 5. Results

Se organiza por función/RQ, no por códigos internos de experimentos:

- data and partition checks;
- candidate retrieval performance;
- documentary evidence retrieval;
- controlled explanation quality;
- sensitivity/robustness analyses;
- inferential results;
- optional RQ summary.

Cada subsección debe seguir:

`pregunta → métrica → comparación → resultado → interpretación permitida`.

#### 6. Discussion

Debe interpretar, comparar y delimitar:

- separación ranking/evidencia;
- uso controlado del LLM;
- comparación con literatura;
- implicaciones para apoyo a decisiones auditable;
- configurabilidad y condiciones de transferencia;
- limitaciones.

#### 7. Conclusion

Debe cerrar:

`aporte → evidencia principal → alcance → implicación`.

No introduce resultados nuevos ni generalización externa no demostrada.

### 7. Front matter y end matter

El `Title`, `Abstract` y `Keywords` se redactan al final.

El end matter debe contemplar, sujeto a requisitos KBS vigentes:

- `Data availability`;
- `Code and reproducibility resources` si corresponde como declaración separada;
- `CRediT authorship contribution statement`;
- `Funding`;
- `Declaration of competing interest`;
- `Acknowledgements` si aplica;
- `References`;
- `Supplementary material` si es necesario.

### 8. Política del Word acumulativo

El Word `KBS_ARTICLE_WORKING_STRUCTURE_V01.docx` es la base editable sobre la que se completará el artículo.

Reglas:

1. cada nueva versión parte de la última versión acumulativa aprobada para continuar trabajando;
2. no se crea un Word independiente por sección;
3. una sección nueva se inserta directamente en su ubicación estructural;
4. las notas editoriales grises son temporales y se eliminan al completar la sección;
5. Part I mantiene el manuscript master inglés;
6. Part II mantiene el espejo español de control semántico;
7. las versiones de trabajo siguen siendo candidatas hasta la aprobación expresa del autor;
8. ningún texto previamente rechazado se reutiliza automáticamente.

### 9. Ciclo de cada bloque

1. verificar estructura vigente y última versión acumulativa;
2. verificar fuentes y estado experimental;
3. actualizar claims autorizados/prohibidos;
4. preparar prompt cerrado para IA de Redacción;
5. redactar la sección dentro del Word/Markdown acumulativo;
6. auditar contenido científico, prosa KBS-34, fluidez y ubicación narrativa;
7. activar IA Experimental solo cuando exista trigger real;
8. resolver observaciones;
9. solicitar aprobación expresa del autor;
10. versionar e integrar solo después de la aprobación correspondiente.

### 10. Criterios de aprobación de una sección

Una sección solo puede pasar a `APPROVED` cuando:

- cumple la función narrativa asignada por la estructura;
- todas sus afirmaciones están respaldadas;
- no contiene resultados pendientes presentados como hechos;
- no adelanta el testbed experimental antes de que sea narrativamente pertinente;
- evita abstracción y nominalización innecesarias;
- mantiene relaciones claras de agente/entrada–acción–salida;
- respeta la separación histórico/normativo/LLM;
- no confunde reproducibilidad, configurabilidad y generalización;
- ES/EN son semánticamente equivalentes;
- cualquier cifra o referencia coincide entre idiomas;
- no existe objeción experimental crítica cuando la revisión experimental sea aplicable;
- el autor la aprueba expresamente.

### 11. Journal targeting

```text
TARGET_A = Knowledge-Based Systems
PLAN_B = Expert Systems with Applications
PLAN_C = Information Processing & Management
PUBLICATION_ROUTE_KBS = SUBSCRIPTION
```

La redacción seguirá KBS-34 mientras KBS sea Target A. Antes del paquete final se volverán a verificar los requisitos oficiales vigentes de plantilla, referencias, declaraciones y submission.

---

## English

### 1. Purpose

Manage iterative construction of the main research article without anticipating results, altering the approved experimental design, or transferring governance-document prose into the manuscript. The article will be built on a **complete cumulative structure**, and each new version must progressively complete that same base rather than create isolated section documents.

The editorial basis is the approved empirical guide derived from 34 recent *Knowledge-Based Systems* articles (`KBS_EWG_34_V01`), subject to the frozen scientific and experimental constraints of the project.

### 2. Governing principles

- The article is not an abbreviated thesis.
- The reader should encounter scientific problem/positioning first, general architecture second, and the specific experimental instantiation third.
- The specific NANDINA/Chapter-Class 87 testbed and documentary corpus must not prematurely define the conceptual scope of the architecture.
- Historical retrieval generates and ranks candidates.
- The Top-3 is fixed before documentary retrieval and generation.
- Documentary retrieval provides evidence for fixed candidates and does not rerank them.
- The local LLM is downstream and explanation-only; it does not classify from scratch or feed generated content back into candidate selection.
- Candidate retrieval is not overall classification accuracy.
- Documentary association is not substantive legal correctness.
- Auditability is not legal correctness.
- Configurability/replicability is not empirical generalization.
- SERIES is the observation/analysis unit; DAM is the grouping unit when dependence exists.
- Pending results may not be drafted as findings.
- Every scientific claim must be traceable to authorized evidence.
- Part I is the English publication-facing manuscript master; Part II is the Spanish semantic-control mirror.

### 3. Cumulative article architecture

Current working structure:

1. Introduction
2. Related work
3. Decision-support architecture
4. Experimental design
5. Results
6. Discussion
7. Conclusion
8. KBS end matter.

Detailed editable source:

`article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V01.md`

The corresponding editable Word is `KBS_ARTICLE_WORKING_STRUCTURE_V01.docx`. Future deliveries must preserve and progressively complete this cumulative structure. Rebuilding the manuscript from scratch or delivering isolated section-only Words is not authorized.

Limitations remain provisionally integrated as the final subsection of Discussion.

### 4. Prior-work state

0A is closed/approved; 0B and 0C are closed/approved/frozen; the original 0D section architecture is superseded only for structure/drafting order by D-014; the KBS-34 empirical writing guide is author-approved and binding; Methods B01 V05 is on hold and not approved; V06 is not authorized.

### 5. New operational drafting order

After the author finishes editing and explicitly approves the working structure, drafting proceeds as:

`Related Work → provisional Introduction → Decision-support architecture → Experimental design → currently authorized Results → preliminary figures/tables → pending experimental integration → final Results → Discussion + Limitations → Conclusion → Abstract → Title + Keywords → final KBS adaptation`.

This is a project-governance choice intended to reduce rewriting; it is not presented as evidence about the actual drafting order used by the authors of the KBS-34 corpus.

### 6. Section functions

- **Introduction:** problem → prior approaches → precise limitation → consequence → high-level proposal → contributions → evaluation context → RQs → roadmap.
- **Related Work:** function-based synthesis ending in explicit positioning.
- **Decision-support architecture:** general input–operation–output flow before experimental details.
- **Experimental design:** specific testbed, historical data, documentary corpus, partitions/dependence, configuration, evaluation framework, statistics and reproducibility.
- **Results:** organized by scientific function/RQ rather than internal experiment IDs.
- **Discussion:** interpretation, comparison, implications, transfer conditions and limitations.
- **Conclusion:** contribution → main evidence → scope → implication.

### 7. Front matter and end matter

Title, Abstract and Keywords are drafted late. End matter must cover Data availability, reproducibility/code resources as appropriate, CRediT, Funding, Declaration of competing interest, Acknowledgements if applicable, References, and Supplementary material if needed.

### 8. Cumulative Word policy

`KBS_ARTICLE_WORKING_STRUCTURE_V01.docx` is the editable base. Each new version starts from the latest cumulative version, inserts drafted text in its structural location, retains English Part I and Spanish semantic-control Part II, and removes drafting notes only as the corresponding sections are completed. No previously rejected prose is reused automatically.

### 9. Block cycle

Verify structure → verify sources/experimental state → update authorized/prohibited claims → issue drafting prompt → draft inside cumulative Markdown/Word → audit science/KBS prose/fluency/narrative placement → trigger Experimental AI only when required → resolve observations → obtain explicit author approval → version/integrate only after approval.

### 10. Approval criteria

A section must fulfill its narrative role, be evidence-grounded, avoid premature experimental-scope exposition, avoid unnecessary abstraction/nominalization, preserve clear agent/input–action–output relations, maintain historical/documentary/LLM separation, avoid conflating reproducibility/configurability/generalization, preserve EN/ES equivalence, and obtain explicit author approval.

### 11. Journal targeting

Target A remains Knowledge-Based Systems; Plans B/C remain Expert Systems with Applications and Information Processing & Management. KBS publication route is subscription. Official submission requirements will be rechecked before final submission.
