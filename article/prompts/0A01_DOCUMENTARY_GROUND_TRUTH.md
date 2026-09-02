# Prompt 0A-01 — Ground truth documental / Documentary ground truth

## Español

### Rol

Actúa como IA de redacción y análisis documental del artículo científico principal. En este bloque no redactarás ninguna sección del manuscrito. Tu tarea es reconstruir el ground truth documental que gobernará la redacción posterior.

### Incorporación obligatoria

Accede a la rama `article/main-manuscript` del repositorio `gci-nandina-rag` y comienza por `article/START_HERE.md`. Cumple el onboarding exigido por la rama y consulta también `article/SOURCE_REGISTRY.md` y `article/DECISIONS.md` antes de analizar las fuentes.

### Fuentes obligatorias para este bloque

**Adjuntos proporcionados por el autor:**

1. Proyecto de tesis aprobado.
2. `Anexo_1_NANDINA_LLM_RAG_v13.docx` o la versión posterior expresamente aprobada.
3. Versión preliminar vigente de la tesis proporcionada por el autor. Los sufijos automáticos del adjunto, como `(3)` o `(4)`, no constituyen por sí solos una versión científica distinta; aplica `SOURCE_REGISTRY.md`.

**Fuente GitHub obligatoria — no debe solicitarse como adjunto:**

4. Plan Maestro experimental definido como `SRC-03` en `article/SOURCE_REGISTRY.md`.

No se adjuntarán todavía los PDF de la bibliografía científica. No realices búsqueda web ni incorpores literatura nueva en este bloque.

### Objetivo del bloque 0A-01

Reconstruir, comparar y dejar explícito el ground truth documental del estudio sin corregir silenciosamente discrepancias y sin convertir formulaciones preliminares en formulaciones aprobadas.

### Jerarquía documental obligatoria

1. Plan Maestro vigente: estado experimental actual.
2. Anexo vigente: arquitectura y metodología operativa actual.
3. Proyecto de tesis aprobado: problema, objetivos, hipótesis, justificación y alcance aprobados.
4. Tesis preliminar: borrador de trabajo y síntesis posterior; no sustituye silenciosamente formulaciones aprobadas ni estado experimental.

Si dos documentos difieren, muestra ambas formulaciones, identifica la diferencia y señala qué documento gobierna cada dimensión. No armonices ni reescribas por cuenta propia.

`SRC-03` es una fuente viva mientras la investigación siga abierta. Registra el blob SHA efectivamente leído como snapshot del corte. Un cambio de blob SHA en la misma rama y ruta no constituye por sí solo un bloqueo; verifica si altera hechos, claims, resultados o decisiones utilizados por el artículo.

### Tareas

1. Confirma la legibilidad de las fuentes y registra nombre/ruta exactos, versión/fecha cuando pueda determinarse, función documental y snapshot aplicable.
2. Transcribe exactamente, desde el Proyecto aprobado, cuando existan: título aprobado; problema general; problemas específicos; objetivo general; OE1–OE5; hipótesis general; HE1–HE5; alcance y delimitaciones relevantes para el paper.
3. Localiza formulaciones equivalentes o posteriores en el Anexo y en la tesis preliminar y compáralas con las aprobadas.
4. Usa el Plan Maestro GitHub para el estado experimental y para las dimensiones operativas que el propio documento gobierne.
5. Identifica toda discrepancia material en redacción, alcance, arquitectura, rol del LLM, ranking histórico, recuperación normativa, Top-3, reranking, unidad de análisis, unidad de agrupamiento, hipótesis, objetivos o snapshot experimental.
6. Distingue explícitamente entre `APPROVED_FORMULATION`, `CURRENT_OPERATIONAL_FORMULATION`, `PRELIMINARY_DRAFT_FORMULATION` y `EXPERIMENTAL_STATUS`.
7. Determina qué elementos están suficientemente claros para cerrar el componente documental de 0A y cuáles requieren decisión del autor/editor.
8. No redactes Introduction, Related Work, Methods, Results, Discussion, Abstract, Conclusions ni título del artículo.
9. No declares novelty, contribución publicable definitiva, RQs ni revista objetivo.
10. No modifiques GitHub ni propongas cambios experimentales.

### Idioma de la respuesta en chat

**Responde únicamente en español.** La obligación español-inglés aplica exclusivamente a los artefactos que posteriormente se creen o integren en GitHub. No dupliques la respuesta del chat en inglés.

### Formato de salida obligatorio

#### A. Onboarding

Reproduce el reporte de onboarding exigido por `START_HERE.md`.

#### B. Inventario documental

Tabla con: `Fuente | archivo/ruta exacta | versión/fecha/snapshot | dimensión que gobierna | legibilidad | observaciones`.

#### C. Formulaciones aprobadas exactas

Transcribe las formulaciones del Proyecto aprobado sin parafrasearlas. Separa claramente título, PG, PE, OG, OE, HG y HE.

#### D. Comparación documental

Tabla con: `Elemento | Proyecto aprobado | Anexo vigente | Tesis preliminar | Plan Maestro si aplica | diferencia material | documento que gobierna | acción necesaria`.

#### E. Arquitectura y alcance vigentes

Resume únicamente aquello que pueda sostenerse como arquitectura/metodología operativa actual.

#### F. Discrepancias y riesgos

Clasifica cada hallazgo como `CRITICAL`, `MAJOR`, `MINOR` o `EDITORIAL`. Reserva `CRITICAL` para problemas que realmente impidan utilizar una fuente o cerrar el bloque; una discrepancia histórica ya resuelta por precedencia puede ser material sin ser bloqueante.

#### G. Bloqueos y decisiones pendientes

Enumera solo cuestiones que realmente requieran resolución antes de cerrar 0A-01.

#### H. Dictamen

Uno de: `PASS`, `PASS WITH CORRECTIONS`, `BLOCKED`.

No avances a 0A-02.

---

## English

### Role

Act as the drafting and documentary-analysis AI for the main scientific article. In this block, do not draft any manuscript section. Reconstruct the documentary ground truth that will govern later writing.

### Mandatory onboarding

Access the `article/main-manuscript` branch of `gci-nandina-rag` and begin with `article/START_HERE.md`. Complete the required onboarding and consult `article/SOURCE_REGISTRY.md` and `article/DECISIONS.md` before analyzing the sources.

### Mandatory sources

**Attachments supplied by the author:**

1. Approved thesis project.
2. `Anexo_1_NANDINA_LLM_RAG_v13.docx` or a later expressly approved version.
3. Current preliminary thesis supplied by the author. Automatic attachment suffixes such as `(3)` or `(4)` are not by themselves scientific version identifiers; apply `SOURCE_REGISTRY.md`.

**Mandatory GitHub source — do not request it as an attachment:**

4. Experimental Master Plan defined as `SRC-03` in `article/SOURCE_REGISTRY.md`.

Do not load scientific-literature PDFs yet. Do not perform web searches or add new literature in this block.

### Objective

Reconstruct, compare, and make explicit the study's documentary ground truth without silently correcting discrepancies or converting preliminary formulations into approved formulations.

### Documentary hierarchy

1. Current Master Plan: current experimental status.
2. Current Annex: current operational architecture and methodology.
3. Approved thesis project: approved problem, objectives, hypotheses, justification, and scope.
4. Preliminary thesis: working draft and later synthesis; it does not silently replace approved formulations or experimental status.

If sources differ, show the difference and state which source governs each dimension. Do not harmonize them on your own.

`SRC-03` is a living source while the research remains open. Record the blob SHA actually read as the snapshot for the current cutoff. A changed blob SHA at the same branch and path is not by itself a blocker; determine whether the change affects facts, claims, results, or decisions used by the article.

### Tasks

1. Confirm source readability and record exact name/path, version/date where determinable, documentary function, and applicable snapshot.
2. Transcribe exactly from the approved Project, where present: title, general problem, specific problems, general objective, SO1–SO5, general hypothesis, SH1–SH5, and relevant scope limitations.
3. Compare later/equivalent formulations in the Annex and preliminary thesis against the approved wording.
4. Use the GitHub Master Plan for experimental status and operational dimensions it governs.
5. Identify material discrepancies in scope, architecture, LLM role, historical ranking, normative retrieval, fixed Top-3, reranking, analysis unit, grouping unit, hypotheses, objectives, or experimental snapshot.
6. Distinguish `APPROVED_FORMULATION`, `CURRENT_OPERATIONAL_FORMULATION`, `PRELIMINARY_DRAFT_FORMULATION`, and `EXPERIMENTAL_STATUS`.
7. Determine what is sufficiently clear to close the documentary component of 0A and what requires an author/editor decision.
8. Do not draft manuscript sections.
9. Do not declare novelty, final contribution, RQs, or journal target.
10. Do not modify GitHub or propose experimental changes.

### Chat response language

**Respond only in Spanish.** The Spanish-English requirement applies exclusively to artifacts later created or integrated into GitHub. Do not duplicate the chat response in English.

### Mandatory output format

A. Onboarding report.  
B. Documentary inventory table.  
C. Exact approved formulations.  
D. Documentary-comparison table.  
E. Current architecture and scope.  
F. Discrepancies and risks classified as `CRITICAL`, `MAJOR`, `MINOR`, or `EDITORIAL`; reserve `CRITICAL` for issues that actually prevent source use or block closure.  
G. Genuine blockers and pending decisions only.  
H. Verdict: `PASS`, `PASS WITH CORRECTIONS`, or `BLOCKED`.

Do not advance to 0A-02.
