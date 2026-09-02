# Entorno de redacción del artículo / Article Writing Workspace

> **Entrada obligatoria / Mandatory entry point:** antes de trabajar en esta rama, lee [`START_HERE.md`](START_HERE.md) y sigue su protocolo de incorporación. / Before working on this branch, read [`START_HERE.md`](START_HERE.md) and follow its onboarding protocol.

## Español

Este directorio contiene el entorno de trabajo exclusivo para la redacción del artículo científico principal derivado de la investigación sobre recomendación auditable de subpartidas NANDINA mediante recuperación histórica, evidencia normativa y explicación controlada con LLM local.

La rama `article/main-manuscript` se utiliza exclusivamente para planificar, redactar, revisar y congelar el manuscrito. El repositorio principal continúa siendo la fuente de verdad para desarrollo experimental, ejecución, auditoría y trazabilidad técnica. El repositorio `gci-nandina-rag-reproducibility` se reservará para el paquete final de reproducción y replicación científica.

### Incorporación obligatoria

Toda persona o IA que se incorpore al trabajo debe comenzar por `START_HERE.md`. Ese archivo define el orden obligatorio de lectura, la jerarquía de fuentes, los límites interpretativos, el protocolo previo a la redacción y la información mínima que debe reconstruirse antes de producir trabajo.

Además, `SOURCE_REGISTRY.md` identifica la ubicación vigente de las fuentes nucleares y las equivalencias operativas entre copias locales y GitHub. Debe consultarse siempre que una tarea dependa de Proyecto, Anexo, Plan Maestro o tesis preliminar.

Cuando la tarea involucre literatura, Related Work, gap, novelty, posicionamiento o incorporación de referencias, también es obligatorio leer `BIBLIOGRAPHIC_FRAMEWORK.md` antes de trabajar.

### Marco bibliográfico

El corpus bibliográfico inicial procede del proyecto de investigación aprobado, del Anexo vigente y de la versión preliminar vigente de la tesis. Los PDF originales serán proporcionados por el autor cuando el editor científico abra la Fase 0B y solicite lotes temáticos concretos.

Las referencias heredadas no se descartan por antigüedad. Toda nueva referencia académica debe cumplir las reglas de recencia, impacto, acceso a PDF, trazabilidad y aprobación definidas en `BIBLIOGRAPHIC_FRAMEWORK.md`.

### Regla bilingüe obligatoria

Todo contenido destinado al artículo y todo artefacto de planificación, revisión, decisión o control editorial creado en este directorio debe existir en español e inglés. Ambas versiones deben transmitir el mismo contenido científico, sin añadir, omitir o reinterpretar información entre idiomas.

La versión en español sirve como versión de control semántico durante el proceso de investigación y revisión. La versión en inglés será la base de la eventual presentación internacional, pero no puede divergir de la versión en español.

### Flujo de trabajo

1. El editor científico principal administra `ARTICLE_WRITING_PLAN.md`.
2. Antes de redactar cada bloque se verifica la evidencia autorizada y el estado experimental.
3. Se genera un prompt cerrado para la IA de redacción.
4. La respuesta se audita científicamente, metodológicamente y editorialmente.
5. La IA responsable de la ejecución experimental realiza una auditoría independiente de consistencia con el estado real de la investigación.
6. Se resuelven observaciones y contradicciones.
7. El autor aprueba el bloque.
8. Solo entonces el bloque se integra y se actualizan el plan, el estado, la matriz de claims y el registro de decisiones.

### Estados permitidos

`NOT_STARTED`, `IN_ANALYSIS`, `READY_FOR_DRAFTING`, `DRAFTING`, `INTERNAL_REVIEW`, `EXPERIMENTAL_REVIEW`, `REVISION_REQUIRED`, `APPROVED`, `FROZEN`, `BLOCKED`.

---

## English

This directory contains the dedicated workspace for drafting the main scientific article derived from the research on auditable NANDINA subheading recommendation through historical retrieval, normative evidence, and controlled explanation with a local LLM.

The `article/main-manuscript` branch is used exclusively to plan, draft, review, and freeze the manuscript. The main repository remains the source of truth for experimental development, execution, auditing, and technical traceability. The `gci-nandina-rag-reproducibility` repository will be reserved for the final scientific reproduction and replication package.

### Mandatory onboarding

Any person or AI joining the work must begin with `START_HERE.md`. That file defines the mandatory reading order, source hierarchy, interpretation boundaries, pre-drafting protocol, and the minimum information that must be reconstructed before producing work.

In addition, `SOURCE_REGISTRY.md` identifies the current locations of the nuclear sources and the operational equivalences between local copies and GitHub. It must be consulted whenever a task depends on the Project, Annex, Master Plan, or preliminary thesis.

When the assigned task involves literature, Related Work, gap identification, novelty, scientific positioning, or adding references, `BIBLIOGRAPHIC_FRAMEWORK.md` must also be read before any work is produced.

### Bibliographic framework

The initial bibliographic corpus comes from the approved research project, the current Annex, and the current preliminary thesis. Original PDFs will be supplied by the author when the scientific editor opens Phase 0B and requests specific thematic batches.

Inherited references are not discarded because of age. Every new academic reference must satisfy the recency, impact, PDF-access, traceability, and approval rules defined in `BIBLIOGRAPHIC_FRAMEWORK.md`.

### Mandatory bilingual rule

All article-bound content and every planning, review, decision, or editorial-control artifact created in this directory must exist in Spanish and English. Both versions must convey the same scientific content, with no addition, omission, or reinterpretation across languages.

The Spanish version serves as the semantic-control version during the research and review process. The English version will be the basis for eventual international submission, but it must not diverge from the Spanish version.

### Workflow

1. The lead scientific editor maintains `ARTICLE_WRITING_PLAN.md`.
2. Before drafting each block, the authorized evidence and experimental status are verified.
3. A constrained prompt is prepared for the drafting AI.
4. The response is audited scientifically, methodologically, and editorially.
5. The AI responsible for experimental execution performs an independent consistency audit against the actual state of the research.
6. Observations and contradictions are resolved.
7. The author approves the block.
8. Only then is the block integrated and the plan, status, claim matrix, and decision log updated.

### Allowed statuses

`NOT_STARTED`, `IN_ANALYSIS`, `READY_FOR_DRAFTING`, `DRAFTING`, `INTERNAL_REVIEW`, `EXPERIMENTAL_REVIEW`, `REVISION_REQUIRED`, `APPROVED`, `FROZEN`, `BLOCKED`.
