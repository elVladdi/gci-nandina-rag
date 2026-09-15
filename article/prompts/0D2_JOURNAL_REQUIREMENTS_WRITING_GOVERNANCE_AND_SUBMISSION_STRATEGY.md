# 0D-2 — Requisitos de revista, gobernanza de escritura y estrategia de envío / Journal Requirements, Writing Governance, and Submission Strategy

## Español

### Rol

Actúa exclusivamente como **IA de Redacción y análisis científico-editorial** del artículo principal del proyecto Tesis San Marcos.

Ejecuta únicamente 0D-2. No redactes secciones del manuscrito.

### Objetivo

Cerrar antes de Fase 1 las decisiones que podrían forzar reescritura posterior: requisitos reales de `Knowledge-Based Systems` (KBS), formato/plantilla, estructura, referencias, política de escritura, controles anti-error, flujo `.md`/`.docx`, auditoría de citas en Word y estrategia de cascada de revistas.

### Lectura obligatoria

Lee íntegramente, como mínimo:

1. `article/START_HERE.md`;
2. `article/ARTICLE_STATUS.md`;
3. `article/ARTICLE_WRITING_PLAN.md`;
4. `article/DECISIONS.md`;
5. `article/SOURCE_REGISTRY.md`;
6. `article/CLAIM_EVIDENCE_MATRIX.md`;
7. `article/STYLE_GUIDE.md`;
8. `article/reviews/0D2_ENTRY_GATE.md`;
9. `article/responses/0D_EDITORIAL_ARCHITECTURE_AND_JOURNAL_FIT_RESPONSE_V02.md`;
10. `article/reviews/0D_V02_INTERNAL_REVIEW.md`;
11. `article/positioning/0C_SCIENTIFIC_POSITIONING_FROZEN.md`;
12. 0A y 0B freezes pertinentes cuando una regla dependa de ellos.

Consulta `SRC-03` solo en modo lectura si fuera estrictamente necesario. No modifiques Plan Maestro.

### Búsqueda web obligatoria

Debes verificar requisitos vigentes a fecha de ejecución mediante fuentes oficiales/primarias.

Para KBS, busca y verifica explícitamente:

- tipo(s) de artículo aplicables al presente trabajo;
- si existe plantilla oficial Word y/o LaTeX, y si es obligatoria, recomendada o no requerida;
- modalidad de primera submission (`free format` si aplica o formato estricto);
- estructura/secciones requeridas, recomendadas o permitidas;
- abstract: tipo y límite si existe;
- keywords: número/formato si existe;
- highlights: obligación/opcionalidad y formato;
- graphical abstract: obligación/opcionalidad;
- límites de palabras/páginas si existen;
- reglas de tablas y figuras;
- material suplementario;
- anonimización/double-blind si aplica;
- estilo final de citas y referencias;
- Data Availability / Research Data;
- Code Availability si existe regla específica;
- declaración de uso de IA;
- CRediT, funding, competing interests y declaraciones requeridas;
- checklist y elementos obligatorios de submission;
- cualquier requisito que afecte la estructura del manuscrito desde el primer borrador.

Distingue siempre:

```text
JOURNAL_SPECIFIC_REQUIREMENT
PUBLISHER_LEVEL_REQUIREMENT
RECOMMENDATION
OBSERVED_CONVENTION
UNVERIFIED
```

No conviertas una convención observada en requisito oficial.

### Cascada de revistas

Evalúa como mínimo:

```text
TARGET_A = Knowledge-Based Systems
PLAN_B = Expert Systems with Applications
PLAN_C = Information Processing & Management
```

No cambies este orden salvo evidencia editorial fuerte y explícita. Si recomiendas cambiarlo, trátalo como propuesta para auditoría, no como decisión.

Para A/B/C determina:

- fit científico del mismo núcleo del artículo;
- requisitos estructurales/formales que cambiarían;
- cambios de framing necesarios;
- elementos que pueden permanecer intactos;
- riesgo de desk rejection;
- magnitud de reescritura si se migra A→B o B→C (`LOW`, `MEDIUM`, `HIGH`);
- estrategia para que Methods/Results/arquitectura permanezcan reutilizables.

### Tarea A — Requisitos KBS y plantilla

Produce una matriz:

`elemento | estado oficial | requisito exacto | fuente oficial | impacto sobre redacción | acción antes de Fase 1`

Debe incluir plantilla/formato oficial y concluir con uno de estos estados:

```text
KBS_TEMPLATE_STATUS = OFFICIAL_TEMPLATE_CONFIRMED
KBS_TEMPLATE_STATUS = NO_MANDATORY_TEMPLATE_CONFIRMED
KBS_TEMPLATE_STATUS = UNVERIFIED
```

Si hay plantilla oficial, identifica la fuente oficial exacta y el formato disponible. No inventes ni reconstruyas una plantilla por similitud.

### Tarea B — Arquitectura definitiva compatible con KBS

Toma la arquitectura 0D-1 como base y determina qué debe:

- `KEEP`;
- `RENAME`;
- `REORDER`;
- `MERGE`;
- `SPLIT`;
- `DEFER`.

No cambies la lógica científica para acomodar artificialmente la revista.

Entrega una arquitectura candidata final para iniciar redacción, pero mantenla `PENDING_EDITORIAL_FREEZE`.

### Tarea C — Política de referencias

Determina:

1. estilo final oficial requerido por KBS;
2. reglas de citas en texto y bibliografía para submission;
3. política operativa de trabajo ya decidida por el autor:
   - durante redacción, **solo el Word** usará citas/referencias provisionales en APA 7;
   - el autor gestionará las citas con Mendeley al final;
   - el estilo final se convertirá entonces al estilo oficial de la revista.

No introduzcas campos Mendeley ni supongas gestión automática de Mendeley durante la redacción.

### Tarea D — Política maestra de escritura científica

Propón reglas explícitas y auditables para congelar antes de Fase 1, incluyendo:

- idioma maestro del manuscrito: inglés;
- variante de inglés recomendada/permitida;
- estilo técnico, preciso y no promocional;
- reglas de voz activa/pasiva y primera persona cuando proceda;
- tiempos verbales por sección;
- longitud y complejidad de oración/párrafo;
- terminología científica controlada;
- consistencia de abreviaturas;
- tratamiento de números, porcentajes, unidades y precisión decimal;
- prohibición de lenguaje absoluto sin evidencia;
- prohibición de adjetivos promocionales (`novel`, `groundbreaking`, `superior`, etc.) salvo autorización claim-level;
- no antropomorfizar modelos/sistemas;
- no convertir diseño o intención en resultado;
- no convertir asociación/cobertura/trazabilidad en correctness;
- no convertir diferencia arquitectónica en novelty;
- no convertir configurabilidad en generalización empírica;
- no introducir causalidad sin diseño causal.

### Tarea E — Protocolo anti-error, anti-alucinación y anti-overclaiming

Construye un protocolo mínimo obligatorio para toda entrega futura.

Debe exigir que:

- ninguna cifra aparezca sin fuente experimental/documental identificable;
- ninguna referencia/DOI/dato bibliográfico sea inventado o completado por memoria;
- ninguna afirmación de literatura se escriba sin comprobar el texto fuente que la respalda;
- snippets de buscador no sean evidencia suficiente;
- un paper no respalde un claim más amplio que su contenido;
- toda inferencia editorial se marque como inferencia y no como hallazgo del estudio;
- claims `CONDITIONAL`, `REVIEW_REQUIRED` y `PROHIBITED` sean respetados literalmente;
- `candidate retrieval ≠ overall classification accuracy`;
- `normative association ≠ substantive normative correctness`;
- `auditability ≠ legal correctness`;
- `configurability ≠ empirical generalization`;
- `journal fit ≠ novelty proof`;
- `architectural difference ≠ novelty by itself`;
- `absence within search scope ≠ universal absence`.

Incluye un checklist pre-entrega que la IA de Redacción deba ejecutar en cada bloque.

### Tarea F — Workflow acumulativo `.md` + Word

Formaliza el flujo obligatorio decidido por el autor:

1. La **IA de Redacción** es responsable de generar y actualizar los artefactos de manuscrito.
2. Cada entrega de un bloque deberá producir:
   - `.md` del bloque;
   - `.md` maestro acumulativo candidato;
   - `.docx` maestro acumulativo candidato.
3. El Word debe actualizarse sobre la **última versión aprobada** y no reconstruirse desde cero, excepto en la creación inicial a partir del formato/plantilla oficialmente adoptado.
4. La IA Gestora, la IA Experimental y el autor auditan; no sustituyen a la IA de Redacción como responsable de generación/actualización del manuscrito.
5. Una versión candidata no se convierte en nueva base canónica hasta superar las auditorías aplicables y la aprobación del autor.
6. Si una entrega requiere V02/V03, la nueva candidata debe preservar todo lo aprobado y modificar únicamente lo autorizado.
7. Al final existirá un único `.md` maestro y un único `.docx` maestro final, además del historial versionado.

Propón una convención de nombres/versionado que minimice ambigüedad.

### Tarea G — Protocolo de comentarios por cita en Word

Toda cita incluida en el Word deberá tener un comentario de Word anclado exactamente a esa cita.

El comentario debe contener obligatoriamente:

```text
FUENTE / REVISTA:
AUTOR(ES):
AFIRMACIÓN ORIGINAL / EXTRACTO TEXTUAL EXACTO Y SUFICIENTE:
TRADUCCIÓN AL ESPAÑOL:
JUSTIFICACIÓN DE RESPALDO:
LÍMITE DE LA CITA / QUÉ NO DEMUESTRA: [cuando sea pertinente]
```

Reglas:

- la afirmación original debe preservar el idioma de la fuente;
- la traducción al español debe ser semánticamente fiel;
- la justificación debe explicar la relación exacta entre la fuente y la oración/claim del manuscrito;
- una misma referencia usada para claims distintos requiere comentarios distintos;
- el comentario no puede suplir una cita incorrecta: si la fuente no respalda el claim, la cita debe corregirse;
- cada comentario debe permitir una auditoría posterior afirmación–cita–fuente.

### Tarea H — Estrategia de aceptación y desk-rejection

Para KBS define una estrategia concreta de framing y presentación que aumente el fit sin overclaiming.

Incluye:

- qué debe ser el centro científico del paper;
- qué no debe parecer el paper;
- riesgos principales de desk rejection;
- mitigación de cada riesgo;
- cómo presentar el alcance Clase 87;
- cómo presentar HE4;
- cómo tratar resultados negativos o limitaciones;
- cómo hacer visibles interfaces, invariantes, evaluación function-specific, provenance y reproducibilidad;
- qué elementos deben aparecer en Title/Abstract/Introduction más adelante;
- qué elementos conviene mantener fuera del framing principal.

No declares novelty final.

### Tarea I — Matriz de cascada A/B/C

Entrega:

`dimension | KBS (A) | ESWA (B) | IPM (C) | núcleo común | cambio requerido al migrar | riesgo de reescritura`

El objetivo es que un rechazo en A no obligue a rehacer Methods o Results salvo requisito formal imprescindible.

### Tarea J — Gate pre-redacción

Clasifica cada decisión crítica como:

```text
CLOSED_FOR_DRAFTING
CLOSED_WITH_OPERATIONAL_CONDITION
UNVERIFIED_BLOCKING
UNVERIFIED_NONBLOCKING
DEFERRED_WITHOUT_REWRITE_RISK
```

No recomiendes abrir Fase 1 si existe cualquier `UNVERIFIED_BLOCKING` relativo a plantilla/formato inicial, estructura, tipo de artículo, política de citas/referencias o workflow maestro.

### Restricciones científicas vigentes

Preserva íntegramente:

```text
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
RQ1 = RETAINED
RQ2 = RETAINED
RQ3 = RETAINED_WITH_HE4_LIMITATIONS
RQ4 = RETAINED_CONDITIONAL_ON_GROUP3
C10_C11_RECONCILIATION = REQUIRED_BEFORE_EXP11B_ARTICLE_USE
GROUP3 = REQUIRED_BEFORE_FINAL_RQ4_AND_HE2_HE5_INFERENCE
```

No redactes Methods, Related Work, Results, Introduction ni ninguna otra sección del manuscrito.

### Artefacto obligatorio

Crea únicamente:

`article/responses/0D2_JOURNAL_REQUIREMENTS_WRITING_GOVERNANCE_AND_SUBMISSION_STRATEGY_RESPONSE_V01.md`

Debe ser bilingüe ES/EN con equivalencia semántica.

No modifiques ningún otro archivo.

### Cierre obligatorio

Finaliza con:

```text
0D2_ANALYSIS = COMPLETED_PENDING_EDITORIAL_REVIEW
TARGET_A = Knowledge-Based Systems
PLAN_B = Expert Systems with Applications
PLAN_C = Information Processing & Management
KBS_TEMPLATE_STATUS = <valor>
KBS_ARTICLE_TYPE_STATUS = <valor>
KBS_REFERENCE_STYLE_STATUS = <valor>
ARTICLE_ARCHITECTURE_STATUS = <valor>
WRITING_POLICY_STATUS = <valor>
CLAIM_EVIDENCE_PROTOCOL_STATUS = <valor>
MD_DOCX_WORKFLOW_STATUS = <valor>
WORD_CITATION_COMMENT_PROTOCOL_STATUS = <valor>
JOURNAL_CASCADE_STATUS = <valor>
PRE_DRAFTING_GATE_RECOMMENDATION = PASS | PASS_WITH_CORRECTIONS | BLOCKED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
AUTHOR_APPROVAL = NOT_REQUESTED
FREEZE_0D = NOT_PERFORMED
PHASE_1 = NOT_OPENED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW_TRIGGER = ABSENT | PRESENT
```

Commit sugerido:

`article: add 0D2 journal requirements and writing governance response v01`

En el chat informa únicamente commit SHA, ruta y estado `COMPLETED_PENDING_EDITORIAL_REVIEW`.

---

## English

Act exclusively as the Writing/scientific-editorial analysis AI for 0D-2. Do not draft manuscript sections.

Use the governing repository artifacts listed above and perform current official-source web verification for KBS and the A/B/C journal cascade. Resolve journal/article-type/template/format requirements, final reference style, definitive article architecture, scientific writing policy, anti-error and claim–evidence rules, cumulative Markdown/Word workflow, provisional APA-7 references in Word until final author-side Mendeley management, mandatory citation-anchored Word comments, acceptance strategy, and journal-transfer strategy.

The Drafting AI owns generation and updating of manuscript `.md` and `.docx` artifacts. Every future drafting delivery must include the block Markdown, cumulative candidate master Markdown, and cumulative candidate master Word document. Candidate versions become canonical only after the required audits and author approval. The master Word must be updated from the last approved Word rather than rebuilt, except for initial creation from the officially adopted journal format/template.

Every citation in Word must carry a citation-anchored comment containing source/journal, authors, an exact sufficient supporting statement in the source language, Spanish translation, precise support justification, and—when relevant—the boundary of what the source does not establish. Distinct claims supported by the same reference require distinct comments.

Preserve all frozen scientific boundaries and do not declare final gap or novelty. Create only:

`article/responses/0D2_JOURNAL_REQUIREMENTS_WRITING_GOVERNANCE_AND_SUBMISSION_STRATEGY_RESPONSE_V01.md`

The response must be bilingual and finish with the required status block. Modify no other file.