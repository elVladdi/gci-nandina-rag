# Prompt 0A-01 — Ground truth documental / Documentary ground truth

## Español

### Rol

Actúa como IA de redacción y análisis documental del artículo científico principal. En este bloque no redactarás ninguna sección del manuscrito. Tu tarea es reconstruir el ground truth documental que gobernará la redacción posterior.

### Incorporación obligatoria

Accede a la rama `article/main-manuscript` del repositorio `gci-nandina-rag` y comienza por `article/START_HERE.md`. Cumple el onboarding exigido por la rama y consulta también `article/SOURCE_REGISTRY.md` antes de analizar los adjuntos.

### Fuentes obligatorias para este bloque

**Adjuntos proporcionados por el autor:**

1. Proyecto de tesis aprobado.
2. `Anexo_1_NANDINA_LLM_RAG_v13.docx` o la versión posterior expresamente aprobada.
3. Versión preliminar vigente de la tesis: `Molleapasa_gv(3).docx`.

**Fuente GitHub obligatoria — no debe solicitarse como adjunto:**

4. Plan Maestro experimental en el repositorio `elVladdi/gci-nandina-rag`, rama `docs/plan-maestro-temporal-2026-08-31`, ruta `docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md`.

Para el proceso del artículo, esa copia GitHub es el **equivalente operativo** de la copia local iterativa `PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-09-01_v20.md`. Consulta directamente la copia GitHub y no pidas al autor que adjunte la v20 local mientras `SOURCE_REGISTRY.md` mantenga esta equivalencia.

No se adjuntarán todavía los PDF de la bibliografía científica. No realices búsqueda web ni incorpores literatura nueva en este bloque.

### Objetivo del bloque 0A-01

Reconstruir, comparar y dejar explícito el ground truth documental del estudio sin corregir silenciosamente discrepancias y sin convertir formulaciones preliminares en formulaciones aprobadas.

### Jerarquía documental obligatoria

Aplica la precedencia definida en la rama:

1. Plan Maestro vigente: estado experimental actual.
2. Anexo vigente: arquitectura y metodología operativa actual.
3. Proyecto de tesis aprobado: problema, objetivos, hipótesis, justificación y alcance aprobados.
4. Tesis preliminar: borrador de trabajo y síntesis posterior; no puede sustituir silenciosamente formulaciones aprobadas.

Si dos documentos difieren, muestra ambas formulaciones, identifica la diferencia y aplica la precedencia solo para indicar qué documento gobierna cada dimensión. No armonices ni reescribas por cuenta propia.

### Tareas

1. Confirma la legibilidad de las tres fuentes adjuntas y de la fuente GitHub. Registra nombre/ruta exactos, versión/fecha si puede determinarse y función documental.
2. Transcribe exactamente, desde el Proyecto aprobado, cuando existan:
   - título aprobado;
   - problema general;
   - problemas específicos;
   - objetivo general;
   - OE1–OE5;
   - hipótesis general;
   - HE1–HE5;
   - alcance y delimitaciones relevantes para el paper.
3. Localiza las formulaciones equivalentes o posteriores en el Anexo y en la tesis preliminar y compáralas con las aprobadas.
4. Usa el Plan Maestro GitHub exclusivamente para el estado experimental y para contrastar cualquier dimensión operativa que el propio documento gobierne.
5. Identifica toda discrepancia material en redacción, alcance, arquitectura, rol del LLM, rol del ranking histórico, rol de la recuperación normativa, Top-3, reranking, unidad de análisis, unidad de agrupamiento, hipótesis u objetivos.
6. Distingue explícitamente entre:
   - `APPROVED_FORMULATION` — formulación aprobada que no puede sustituirse silenciosamente;
   - `CURRENT_OPERATIONAL_FORMULATION` — formulación metodológica/arquitectónica vigente;
   - `PRELIMINARY_DRAFT_FORMULATION` — redacción de la tesis preliminar;
   - `EXPERIMENTAL_STATUS` — información gobernada por el Plan Maestro.
7. Determina qué elementos están suficientemente claros para cerrar el componente documental de 0A y cuáles permanecen bloqueados o requieren decisión del autor/editor.
8. No redactes Introduction, Related Work, Methods, Results, Discussion, Abstract, Conclusions ni título del artículo.
9. No declares novelty, contribución publicable definitiva, RQs ni revista objetivo.
10. No modifiques GitHub ni propongas cambios experimentales.

### Formato de salida obligatorio

Entrega todo primero en español y luego en inglés con equivalencia semántica completa.

#### A. Onboarding

Reproduce el reporte de onboarding exigido por `START_HERE.md`.

#### B. Inventario documental

Tabla con: `Fuente | archivo/ruta exacta | versión/fecha | dimensión que gobierna | legibilidad | observaciones`.

#### C. Formulaciones aprobadas exactas

Transcribe las formulaciones del Proyecto aprobado sin parafrasearlas. Separa claramente título, PG, PE, OG, OE, HG y HE.

#### D. Comparación documental

Tabla con: `Elemento | Proyecto aprobado | Anexo vigente | Tesis preliminar | Plan Maestro si aplica | diferencia material | documento que gobierna | acción necesaria`.

#### E. Arquitectura y alcance vigentes

Resume únicamente aquello que pueda sostenerse como arquitectura/metodología operativa actual, dejando explícito qué proviene del Anexo y qué no modifica las formulaciones aprobadas del Proyecto.

#### F. Discrepancias y riesgos

Clasifica cada hallazgo como `CRITICAL`, `MAJOR`, `MINOR` o `EDITORIAL`.

#### G. Bloqueos y decisiones pendientes

Enumera solo cuestiones que realmente requieran resolución antes de cerrar 0A-01.

#### H. Dictamen

Uno de: `PASS`, `PASS WITH CORRECTIONS`, `BLOCKED`.

No avances a 0A-02.

---

## English

### Role

Act as the drafting and documentary-analysis AI for the main scientific article. In this block, you must not draft any manuscript section. Your task is to reconstruct the documentary ground truth that will govern later writing.

### Mandatory onboarding

Access the `article/main-manuscript` branch of the `gci-nandina-rag` repository and begin with `article/START_HERE.md`. Complete the onboarding required by the branch and also consult `article/SOURCE_REGISTRY.md` before analyzing the attachments.

### Mandatory sources for this block

**Attachments supplied by the author:**

1. Approved thesis project.
2. `Anexo_1_NANDINA_LLM_RAG_v13.docx` or a later expressly approved version.
3. Current preliminary thesis version: `Molleapasa_gv(3).docx`.

**Mandatory GitHub source — must not be requested as an attachment:**

4. Experimental Master Plan in repository `elVladdi/gci-nandina-rag`, branch `docs/plan-maestro-temporal-2026-08-31`, path `docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md`.

For the article workflow, this GitHub copy is the **operational equivalent** of the iterative local copy `PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-09-01_v20.md`. Consult the GitHub copy directly and do not ask the author to attach the local v20 while `SOURCE_REGISTRY.md` preserves this equivalence.

The scientific-literature PDFs will not be attached yet. Do not perform web searches or add new literature in this block.

### Objective of block 0A-01

Reconstruct, compare, and make explicit the study's documentary ground truth without silently correcting discrepancies or converting preliminary formulations into approved formulations.

### Mandatory documentary hierarchy

Apply the precedence defined in the branch:

1. Current Master Plan: current experimental status.
2. Current Annex: current operational architecture and methodology.
3. Approved thesis project: approved problem, objectives, hypotheses, justification, and scope.
4. Preliminary thesis: working draft and later synthesis; it may not silently replace approved formulations.

If two documents differ, show both formulations, identify the difference, and apply precedence only to state which document governs each dimension. Do not harmonize or rewrite them on your own.

### Tasks

1. Confirm readability of the three attached sources and the GitHub source. Record exact file/path, version/date where determinable, and documentary function.
2. Transcribe exactly from the approved Project, where present:
   - approved title;
   - general problem;
   - specific problems;
   - general objective;
   - OE1–OE5;
   - general hypothesis;
   - HE1–HE5;
   - scope and delimitations relevant to the paper.
3. Locate equivalent or later formulations in the Annex and preliminary thesis and compare them with the approved formulations.
4. Use the GitHub Master Plan only for experimental status and any operational dimension that the document itself governs.
5. Identify every material discrepancy in wording, scope, architecture, LLM role, historical-ranking role, normative-retrieval role, fixed Top-3, reranking, analysis unit, grouping unit, hypotheses, or objectives.
6. Explicitly distinguish among:
   - `APPROVED_FORMULATION` — approved wording that may not be silently replaced;
   - `CURRENT_OPERATIONAL_FORMULATION` — current methodological/architectural wording;
   - `PRELIMINARY_DRAFT_FORMULATION` — preliminary-thesis wording;
   - `EXPERIMENTAL_STATUS` — information governed by the Master Plan.
7. Determine which elements are sufficiently clear to close the documentary component of 0A and which remain blocked or require an author/editor decision.
8. Do not draft the Introduction, Related Work, Methods, Results, Discussion, Abstract, Conclusions, or article title.
9. Do not declare novelty, a final publishable contribution, RQs, or a target journal.
10. Do not modify GitHub or propose experimental changes.

### Mandatory output format

Deliver everything first in Spanish and then in English with complete semantic equivalence.

#### A. Onboarding

Reproduce the onboarding report required by `START_HERE.md`.

#### B. Documentary inventory

Table: `Source | exact file/path | version/date | dimension governed | readability | observations`.

#### C. Exact approved formulations

Transcribe the Project formulations without paraphrasing them. Clearly separate title, GP, SPs, GO, SOs, GH, and SHs.

#### D. Documentary comparison

Table: `Element | approved Project | current Annex | preliminary thesis | Master Plan if applicable | material difference | governing document | required action`.

#### E. Current architecture and scope

Summarize only what can be supported as the current operational architecture/methodology, explicitly distinguishing what comes from the Annex and what does not alter the approved Project formulations.

#### F. Discrepancies and risks

Classify each finding as `CRITICAL`, `MAJOR`, `MINOR`, or `EDITORIAL`.

#### G. Blockers and pending decisions

List only issues that genuinely require resolution before closing 0A-01.

#### H. Verdict

One of: `PASS`, `PASS WITH CORRECTIONS`, `BLOCKED`.

Do not advance to 0A-02.
