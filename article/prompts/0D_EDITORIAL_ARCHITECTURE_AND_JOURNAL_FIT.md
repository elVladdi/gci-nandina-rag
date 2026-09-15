# Prompt cerrado 0D — Arquitectura editorial y journal fit / Closed 0D Prompt — Editorial Architecture and Journal Fit

## Español

### Rol

Actúa exclusivamente como **IA de Redacción y análisis científico-editorial** del artículo principal del proyecto Tesis San Marcos.

Ejecuta únicamente `0D — Arquitectura editorial y journal fit`.

No eres la IA Experimental ni la IA Gestora. No ejecutas experimentos, no modificas resultados, no declaras novelty final y no redactas todavía secciones del manuscrito.

### Repositorio y rama

Repositorio: `elVladdi/gci-nandina-rag`  
Rama: `article/main-manuscript`

Trabaja sobre el estado vigente de la rama al iniciar la ejecución.

### Onboarding obligatorio

Lee íntegramente, en este orden:

1. `article/START_HERE.md`;
2. `article/README.md`;
3. `article/ARTICLE_STATUS.md`;
4. `article/ARTICLE_WRITING_PLAN.md`;
5. `article/DECISIONS.md`;
6. `article/SOURCE_REGISTRY.md`;
7. `article/CLAIM_EVIDENCE_MATRIX.md`;
8. `article/STYLE_GUIDE.md`;
9. `article/ground_truth/0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md`;
10. `article/ground_truth/0A02_EXPERIMENTAL_GROUND_TRUTH_FROZEN.md`;
11. `article/reviews/0B_PHASE_CLOSURE.md`;
12. `article/reviews/0C_ENTRY_GATE.md`;
13. `article/responses/0C_GAP_CONTRIBUTION_RESEARCH_QUESTIONS_RESPONSE_V01.md`;
14. `article/reviews/0C_INTERNAL_REVIEW.md`;
15. `article/reviews/0C_AUTHOR_APPROVAL.md`;
16. `article/positioning/0C_SCIENTIFIC_POSITIONING_FROZEN.md`;
17. `article/reviews/0C_PHASE_CLOSURE.md`;
18. `article/reviews/0D_ENTRY_GATE.md`.

Consulta además, solo lectura, `SRC-03` según `SOURCE_REGISTRY.md`. No lo modifiques.

### Estado de entrada obligatorio

Reproduce al inicio del artefacto:

```text
PHASE_0A = CLOSED / APPROVED
PHASE_0B = CLOSED / APPROVED
PHASE_0C = CLOSED / APPROVED
0C = APPROVED / FROZEN
0D_ENTRY_GATE = PASS / OPENED
0D = READY_FOR_DRAFTING
0C_PROVISIONAL_CENTRAL_CONTRIBUTION = B_ARCHITECTURAL_METHODOLOGICAL
RQ1 = RETAINED
RQ2 = RETAINED
RQ3 = RETAINED_WITH_HE4_LIMITATIONS
RQ4 = RETAINED_CONDITIONAL_ON_GROUP3
EXP11B_EDITORIAL_GOVERNANCE_LAG = PRESENT / NONBLOCKING_FOR_0C_CURRENT_SCOPE
C10_C11_RECONCILIATION = REQUIRED_BEFORE_EXP11B_ARTICLE_USE
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
TARGET_JOURNAL = PENDING_0D
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW = NOT_REQUIRED_AT_ENTRY
```

### Posicionamiento congelado que no puedes alterar

La contribución central provisional es la alternativa B — arquitectónica-metodológica. El objeto diferenciador es el contrato funcional completo evaluado:

```text
EXTERNAL_FIXED_HISTORICAL_RANKING
+ POST_RANKING_NORMATIVE_EVIDENCE_WITHOUT_RERANKING
+ DOWNSTREAM_EXPLANATION_ONLY
+ NO_INSERT_DELETE_SUBSTITUTE_REORDER
+ NO_CLASSIFICATION_FEEDBACK
+ DAM_AWARE_PARTITIONING_WHERE_DEPENDENCE_EXISTS
+ FUNCTION_SPECIFIC_EVALUATION
```

Reglas obligatorias:

- no presentar este contrato como prueba automática de novelty;
- no afirmar que cada componente sea nuevo;
- F1/F3 son negativos acotados, no ausencia universal;
- F2 tiene prior art parcial;
- F5 general permanece falsado;
- auditabilidad/source support/trazabilidad ≠ legal correctness;
- candidate retrieval ≠ overall system accuracy;
- configurabilidad ≠ generalización empírica.

### Investigación web autorizada y obligatoria

En 0D **sí está autorizada y es obligatoria la búsqueda web**, pero exclusivamente para **journal fit y requisitos editoriales actuales**.

Debes consultar fuentes oficiales y primarias de cada revista/editorial para verificar, a la fecha de ejecución:

- aims & scope;
- tipos de artículo relevantes;
- límites de extensión, estructura o formato cuando existan;
- política de datos, código, materiales suplementarios y reproducibilidad;
- política relevante de transparencia/declaración sobre uso de IA en la preparación del manuscrito, si existe;
- modalidad de acceso/APC solo como dato operativo secundario;
- cualquier requisito que afecte materialmente este artículo.

Además, para demostrar fit temático, identifica artículos recientes (preferentemente 2023–2026) directamente relacionados con al menos uno de estos ejes:

- retrieval/classification/decision support basado en conocimiento;
- explainable/auditable AI;
- information retrieval + evidence/provenance;
- rule- or regulation-aware AI;
- customs/tariff/HS classification cuando exista;
- human decision support con evidencia trazable.

Los artículos recientes sirven para evaluar **fit**, no para reabrir 0B ni para declarar novelty.

`JOURNAL_FIT ≠ NOVELTY_PROOF`.

### Revistas mínimas obligatorias

Evalúa como mínimo:

1. **Knowledge-Based Systems**;
2. **Expert Systems with Applications**;
3. **Information Processing & Management**;
4. **Decision Support Systems**;
5. **Government Information Quarterly**;
6. **Artificial Intelligence and Law**, solo si el énfasis jurídico-normativo resulta realmente compatible con el artículo.

Puedes añadir como máximo **dos** revistas adicionales si la búsqueda actual demuestra un ajuste sustancialmente mejor que alguno de los seis targets preliminares. Justifica cualquier adición.

### Tarea 1 — Reconstrucción del estado editorial y experimental

Resume únicamente lo necesario para 0D:

- posicionamiento 0C congelado;
- RQs y condiciones;
- claims autorizados/prohibidos relevantes;
- resultados congelados disponibles para futura redacción;
- bloques experimentales todavía pendientes;
- desfase EXP-11B/C10-C11;
- cualquier restricción de 0B-05C, HE4 o Grupo 3 que afecte estructura o journal fit.

No resuelvas el desfase EXP-11B por inferencia.

### Tarea 2 — Arquitectura IMRaD definitiva candidata

Propón la arquitectura del artículo, sin redactar prosa de manuscrito.

Entrega una tabla:

`sección | subsección | propósito científico | evidencia/claims que consume | estado de redactabilidad | dependencia pendiente | riesgo editorial`

Debe incluir como mínimo:

- Introduction;
- Related Work;
- Methods;
- Results;
- Discussion;
- Limitations;
- Conclusions;
- Data/Code Availability cuando corresponda.

Define el orden lógico de subsecciones y evita duplicar contenido entre Methods, Results y Discussion.

### Tarea 3 — Mapa de tablas y figuras esenciales

Propón solo los elementos realmente necesarios.

Tabla obligatoria:

`ID | tipo | contenido | sección | función científica | fuente de datos | estado | dependencia`

Distingue:

- `ESSENTIAL_NOW`;
- `ESSENTIAL_AFTER_PENDING_EXPERIMENT`;
- `OPTIONAL`;
- `NOT_RECOMMENDED`.

No generes las figuras/tablas; solo define su función y dependencia.

### Tarea 4 — Matriz de redactabilidad inmediata

Clasifica cada sección/subsección como:

- `DRAFTABLE_NOW`;
- `DRAFTABLE_WITH_FROZEN_LIMITATIONS`;
- `BLOCKED_BY_GROUP3`;
- `BLOCKED_BY_C10_C11_RECONCILIATION`;
- `BLOCKED_BY_FINAL_RESULTS`;
- `DEFER_TO_LATE_STAGE`.

Debes justificar qué puede comenzar inmediatamente después del cierre de Fase 0 y qué no.

### Tarea 5 — Journal-fit screening

Construye una matriz comparativa para todas las revistas evaluadas:

`journal | scope fit | contribution fit | methods/results fit | novelty expectation risk | empirical-scope fit | explainability/auditability fit | reproducibility/open-science fit | recent related articles | structural/length constraints | operational notes | overall fit`

Usa una escala cualitativa controlada: `HIGH`, `MEDIUM`, `LOW`, acompañada de justificación breve y verificable.

No uses factor de impacto, cuartil o CiteScore como sustituto del fit científico. Si los reportas, trátalos como contexto secundario y usa fuente verificable actual.

### Tarea 6 — Deep dive del Top-3 de journals

Selecciona los **tres mejores** journals del screening y para cada uno entrega:

1. razón de fit científico;
2. posibles motivos de desk rejection;
3. qué énfasis editorial requiere;
4. qué partes del artículo deben fortalecerse o atenuarse;
5. compatibilidad con la alternativa B de 0C;
6. compatibilidad con el alcance empírico Clase 87;
7. compatibilidad con RQ1–RQ4;
8. compatibilidad con resultados todavía pendientes;
9. artículos recientes comparables/relevantes;
10. requisitos editoriales que condicionan la arquitectura del paper.

### Tarea 7 — Recomendación de target principal y alternativas

Propón exactamente:

- `PRIMARY_TARGET`;
- `ALTERNATIVE_TARGET_1`;
- `ALTERNATIVE_TARGET_2`.

Para el target principal incluye:

- justificación científica;
- riesgos;
- ajustes de framing necesarios;
- estructura recomendada;
- razones por las que supera a las alternativas.

La selección es una **recomendación de 0D para revisión editorial**, no una elección final irrevocable. Debe quedar sujeta a auditoría de la IA Gestora y aprobación del autor.

### Tarea 8 — Riesgos científicos/editoriales

Evalúa expresamente:

- novelty risk;
- overclaiming risk;
- internal validity;
- grouped dependence;
- leakage/near-duplicate risk;
- external validity/generalization;
- HE4 limitations;
- normative-source drift;
- reproducibility limitations;
- Group-3 dependency;
- C10/C11 governance lag;
- mismatch entre contribución B y expectations del journal.

Clasifica cada riesgo como `LOW`, `MEDIUM` o `HIGH`, con mitigación concreta.

### Tarea 9 — Gate de Fase 0

Con base en la arquitectura y el journal fit, recomienda exactamente uno:

- `PHASE_0_GATE = PASS`;
- `PHASE_0_GATE = PASS_WITH_CORRECTIONS`;
- `PHASE_0_GATE = BLOCKED`.

Explica qué se autorizaría inmediatamente si el gate fuera aprobado por la IA Gestora y el autor.

No autorices por cuenta propia la redacción del manuscrito.

### Tarea 10 — Trigger de revisión experimental

Si 0D introduce una interpretación experimental nueva o intenta usar una evidencia no congelada, marca:

`EXPERIMENTAL_REVIEW_TRIGGER = PRESENT`.

Si solo organiza editorialmente evidencia ya gobernada:

`EXPERIMENTAL_REVIEW_TRIGGER = ABSENT`.

### Formato obligatorio

Usa estas secciones:

A. Estado reconstruido  
B. Arquitectura IMRaD candidata  
C. Mapa de tablas y figuras  
D. Matriz de redactabilidad  
E. Journal-fit screening  
F. Deep dive Top-3 journals  
G. Target principal y alternativas  
H. Riesgos y mitigaciones  
I. Gate de Fase 0  
J. Trazabilidad

### Cierre obligatorio

Finaliza con:

```text
0D_DRAFTING_ANALYSIS = COMPLETED_PENDING_EDITORIAL_REVIEW
PRIMARY_TARGET = <journal>
ALTERNATIVE_TARGET_1 = <journal>
ALTERNATIVE_TARGET_2 = <journal>
PHASE_0_GATE_RECOMMENDATION = PASS | PASS_WITH_CORRECTIONS | BLOCKED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
AUTHOR_APPROVAL = NOT_REQUESTED
FREEZE_0D = NOT_PERFORMED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW_TRIGGER = ABSENT | PRESENT
```

### Prohibiciones

- No modificar Plan Maestro, resultados experimentales ni freezes previos.
- No modificar `ARTICLE_STATUS.md`, `ARTICLE_WRITING_PLAN.md`, `DECISIONS.md`, `SOURCE_REGISTRY.md`, `CLAIM_EVIDENCE_MATRIX.md` ni reviews.
- No reconciliar C10/C11 por inferencia.
- No integrar EXP-11B como claim.
- No cerrar HE2/HE5 antes del gate experimental correspondiente.
- No reabrir 0B ni añadir literatura nueva al corpus de gap.
- No convertir artículos encontrados para journal fit en evidencia silenciosa de novelty.
- No declarar novelty final.
- No redactar secciones del manuscrito.
- No seleccionar definitivamente revista por autoridad propia.

### Artefacto de respuesta obligatorio en GitHub

Crea exactamente:

`article/responses/0D_EDITORIAL_ARCHITECTURE_AND_JOURNAL_FIT_RESPONSE_V01.md`

No modifiques ningún otro archivo.

El artefacto debe ser bilingüe, con versión completa en español y versión completa en inglés semánticamente equivalentes.

Si V01 ya existe, detente y reporta conflicto. No crees V02 sin autorización expresa.

### Commit y respuesta al usuario

Versiona únicamente ese archivo en `article/main-manuscript` con un mensaje equivalente a:

`article: add 0D editorial architecture and journal fit response v01`

En el chat informa únicamente:

- commit SHA;
- ruta del archivo;
- estado `COMPLETED_PENDING_EDITORIAL_REVIEW`.

Detente después del commit.

---

## English

### Role and scope

Act exclusively as the Writing and scientific-editorial analysis AI for the main Tesis San Marcos article. Execute only `0D — Editorial architecture and journal fit`. Do not act as the Experimental AI or Managing AI; do not execute experiments, alter results, declare final novelty, or draft manuscript sections.

### Mandatory inputs and state

Read the same governing files listed in the Spanish section, including frozen 0A/0B/0C artifacts, the 0D entry gate, Claim–Evidence Matrix, Decisions, Source Registry, Master Writing Plan, Style Guide, and the live experimental Master Plan in read-only mode.

Preserve the frozen Alternative-B positioning and RQ states. EXP-11B article use remains blocked until explicit C10/C11 reconciliation. RQ4 remains conditional on Group 3. Final gap and novelty remain undeclared.

### Web research

Current web research is required only for journal fit and editorial requirements. Prefer official journal/publisher sources for aims/scope, article types, structural/length rules, data/code/reproducibility policies, relevant AI-disclosure rules, and operational publication information. Use recent primary-source articles to assess topical fit, not novelty.

At minimum screen Knowledge-Based Systems, Expert Systems with Applications, Information Processing & Management, Decision Support Systems, Government Information Quarterly, and Artificial Intelligence and Law when justified. Add no more than two additional journals and only with strong evidence of superior fit.

### Scientific tasks

Perform the same ten tasks specified in Spanish: reconstruct the editorial state; propose the final candidate IMRaD architecture; map essential figures/tables; classify section draftability; screen journals; deep-dive the top three; recommend one primary and two alternative targets; assess scientific/editorial risks; recommend the Phase-0 gate; and identify any experimental-review trigger.

Do not treat impact metrics as substitutes for scientific fit. Do not reopen the frozen literature-gap review. Do not turn journal-fit literature into novelty evidence.

### Required artifact

Create exactly:

`article/responses/0D_EDITORIAL_ARCHITECTURE_AND_JOURNAL_FIT_RESPONSE_V01.md`

Modify no other file. The artifact must be fully bilingual with semantic equivalence. Do not overwrite V01 or create V02 without explicit authorization.

### Required closure

End with:

```text
0D_DRAFTING_ANALYSIS = COMPLETED_PENDING_EDITORIAL_REVIEW
PRIMARY_TARGET = <journal>
ALTERNATIVE_TARGET_1 = <journal>
ALTERNATIVE_TARGET_2 = <journal>
PHASE_0_GATE_RECOMMENDATION = PASS | PASS_WITH_CORRECTIONS | BLOCKED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
AUTHOR_APPROVAL = NOT_REQUESTED
FREEZE_0D = NOT_PERFORMED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW_TRIGGER = ABSENT | PRESENT
```

Commit only the response artifact and report only the commit SHA, file path, and `COMPLETED_PENDING_EDITORIAL_REVIEW` state to the author.