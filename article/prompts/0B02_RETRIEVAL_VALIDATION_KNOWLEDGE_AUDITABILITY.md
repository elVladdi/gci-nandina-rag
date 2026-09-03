# Prompt 0B-02 — Retrieval, validación, conocimiento y auditabilidad aduanera / Retrieval, validation, knowledge, and customs auditability

## Español

### Rol

Actúa como IA de redacción y análisis bibliográfico del artículo científico principal. Ejecuta exclusivamente `0B-02 — Retrieval, validación, conocimiento y auditabilidad aduanera`.

No redactes ninguna sección del manuscrito, no declares novelty, no cierres el gap y no busques literatura nueva. Tu tarea es leer íntegramente los PDF asignados, construir un mapa crítico comparable y someter a presión los `CANDIDATE_GAP_ONLY` heredados de 0B-01.

### Onboarding obligatorio

Accede a `article/main-manuscript` de `elVladdi/gci-nandina-rag` y lee primero:

1. `article/START_HERE.md`;
2. `article/ARTICLE_STATUS.md`;
3. `article/ARTICLE_WRITING_PLAN.md`;
4. `article/BIBLIOGRAPHIC_FRAMEWORK.md`;
5. `article/literature/0B_LITERATURE_BATCH_PLAN.md`;
6. `article/literature/0B01_HS_CLASSIFICATION_CORE_LITERATURE_FROZEN.md`;
7. `article/ground_truth/0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md`;
8. `article/ground_truth/0A02_EXPERIMENTAL_GROUND_TRUTH_FROZEN.md`;
9. este prompt completo.

No reabras 0A ni 0B-01.

### PDFs asignados

Analiza **exclusivamente** estos seis PDF ya disponibles en el corpus de 62:

1. `Classification of Goods Using Text Descriptions With Sentences Retrieval.pdf`
2. `Text2Trade. A semantic search system whith Monte Carlo Droput Uncertainty Quantification For HS Code Retrieval..pdf`
3. `Explainable Product Classification for Customs.pdf`
4. `Application of machine learning for assessment of HS code correctness.pdf`
5. `Customs Tariff Classification and the Use of Assistive Technologies.pdf`
6. `Attribute knowledge and KBGAT for predicting the accuracy of the harmonized system code for classifying import and export commodities.pdf`

Si existen copias con sufijos automáticos o títulos con pequeñas variaciones, trátalas como la misma obra cuando el contenido lo confirme. Si alguno no está accesible o no puede leerse íntegramente, identifica únicamente ese archivo y no sustituyas su contenido por abstracts, snippets, conocimiento general ni referencias secundarias.

Los otros PDF del corpus de 62 están `OUT_OF_SCOPE_FOR_CURRENT_BATCH`.

### Regla crítica de procedencia

Distingue siempre:

- `REPORTADO_POR_AUTORES`: hecho que el PDF atribuye a sus propios autores/resultados;
- `INFERENCIA_CRITICA`: inferencia metodológica nuestra derivada del diseño descrito;
- `NO_VERIFICABLE_EN_PDF`: el PDF no permite sostener la afirmación;
- `SECONDARY_CLAIM_UNVERIFIED`: afirmación que el paper toma de una fuente tercera y que no ha sido verificada contra esa fuente primaria.

Una afirmación de terceros citada dentro de un paper **no se convierte en hecho independiente** para nuestro artículo. Si pudiera ser útil posteriormente, regístrala como `SECONDARY_CLAIM_UNVERIFIED` con la referencia primaria que el paper cita, si puede identificarse.

### Definiciones que no deben confundirse

Para el presente artículo:

- **ranking histórico** = recuperación de candidatos desde precedentes históricos;
- **recuperación normativa** = recuperación posterior de evidencia documental para candidatos ya fijados; no sustituye ni reordena el ranking histórico;
- **conocimiento de nomenclatura usado para seleccionar/clasificar** ≠ **evidencia normativa posterior al ranking**;
- **explicabilidad local/model-centric** ≠ **trazabilidad documental/auditabilidad**;
- **asociación de evidencia** ≠ **corrección normativa sustantiva**;
- **Top-k candidate retrieval** ≠ **accuracy global**;
- ausencia de `group split` documentado ≠ demostración de leakage.

### Marco de análisis obligatorio por paper

Extrae únicamente lo que el PDF soporte:

- identificación bibliográfica y tipo de publicación;
- problema y tarea exacta;
- jurisdicción/contexto;
- dataset/corpus, N y origen;
- nivel HS/HTS/CN/otro;
- unidad de observación;
- input;
- método/modelo;
- tipo de retrieval/clasificación/validación;
- uso de jerarquía;
- uso de descripciones HS/tariff/normativas;
- papel exacto del conocimiento normativo o de nomenclatura: selección, clasificación, retrieval, explicación, validación o evidencia;
- uso de precedentes históricos;
- output y Top-k si aplica;
- métricas y denominadores;
- split/validación;
- controles de duplicados/leakage/dependencia;
- baselines;
- principales resultados;
- incertidumbre/calibración/rejection si existe;
- explicabilidad;
- trazabilidad/provenance;
- auditabilidad y evaluación humana/experta si existe;
- límites reconocidos por autores;
- limitaciones adicionales como `INFERENCIA_CRITICA`;
- transferibilidad al contexto NANDINA/Clase 87;
- similitud y diferencia sustantiva con el presente trabajo.

### Presión explícita sobre los candidatos F1–F5 de 0B-01

Para cada paper determina si aporta evidencia que:

- `SUPPORTS_CANDIDATE`;
- `WEAKENS_CANDIDATE`;
- `FALSIFIES_CANDIDATE`;
- `NOT_RELEVANT`;
- `UNRESOLVED`.

Candidatos a someter a presión:

- F1: separación funcional histórico->ranking y normativa->evidencia posterior;
- F2: explicación restringida a un Top-k fijo sin introducir/reordenar códigos;
- F3: control explícito de dependencia por unidad administrativa/grupo;
- F4: separar candidate retrieval de corrección sustantiva;
- F5: evaluar trazabilidad/auditabilidad de evidencia aparte del predictive performance.

No declares novelty aunque ningún paper falsifique un candidato.

### Verificación crítica específica

Busca especialmente:

- si `retrieval` significa recuperación de códigos, documentos, sentencias, precedentes o evidencia;
- si la jerarquía solo aparece en etiquetas o gobierna realmente la búsqueda;
- si una explicación es post-hoc o está respaldada por evidencia documental identificable;
- si se evalúa correctness frente a labels históricas o adjudicación experta;
- si el trabajo reporta human-in-the-loop, rechazo, uncertainty o escalamiento;
- si los datos de entrenamiento/evaluación pueden compartir entidades/grupos/duplicados y qué controles se documentan;
- si métricas Top-k, MRR, accuracy, F1 o uncertainty son comparables o no;
- si se utiliza WCO/HS/tariff nomenclature como feature/conocimiento para decidir el código o como evidencia posterior;
- si hay afirmaciones de auditabilidad sin protocolo de evaluación.

### Estado bibliográfico

Los seis trabajos pertenecen al corpus proporcionado por el autor. Recomienda uno de:

- `KEEP_CORE`;
- `KEEP_SUPPORTING`;
- `REVIEW_REQUIRED`;
- `EXCLUDE_FROM_ARTICLE`.

La recomendación no autoriza automáticamente la cita final.

### Formato de salida obligatorio

#### A. Control de integridad

`ID | archivo | lectura completa sí/no | metadata suficiente sí/no | observaciones`

#### B. Matriz crítica

Una fila por paper con tarea, datos, método, output, validación, métricas, jerarquía, papel del conocimiento/normativa, histórico, explicabilidad, trazabilidad, auditabilidad, principales resultados, limitaciones y función bibliográfica.

#### C. Fichas individuales

Una ficha por paper utilizando las etiquetas de procedencia obligatorias.

#### D. Taxonomía funcional

Clasifica cada trabajo según una o varias funciones: `DIRECT_CLASSIFICATION`, `CODE_RETRIEVAL`, `SENTENCE_RETRIEVAL`, `PRECEDENT_RETRIEVAL`, `CORRECTNESS_VALIDATION`, `STRUCTURED_KNOWLEDGE`, `EXPLAINABILITY`, `AUDITABILITY_SUPPORT`, `HUMAN_DECISION_SUPPORT`, `UNCERTAINTY`, `HYBRID`.

#### E. Matriz de presión F1–F5

`paper | F1 | F2 | F3 | F4 | F5 | evidencia concreta`.

#### F. Patrones del lote

Solo patrones respaldados por al menos dos papers del lote.

#### G. Candidatos a gap actualizados

Mantén, reformula, debilita o elimina F1–F5 según la evidencia. Cualquier candidato nuevo debe etiquetarse `CANDIDATE_GAP_ONLY` y declarar qué lotes faltan para validarlo.

#### H. Claims secundarios pendientes

Tabla: `paper | claim secundario | fuente primaria citada por el paper | posible utilidad | estado SECONDARY_CLAIM_UNVERIFIED`.

#### I. Inconsistencias y verificaciones pendientes

Lista cerrada; no uses web para resolverla.

#### J. Recomendación bibliográfica

`paper | recomendación | función potencial | justificación`.

#### K. Dictamen

`PASS`, `PASS WITH CORRECTIONS` o `BLOCKED`.

### Prohibiciones

- No web.
- No búsqueda de literatura nueva.
- No usar los otros 56 PDF para completar este lote.
- No redactar secciones del artículo.
- No declarar novelty, gap definitivo o superioridad.
- No alterar claims experimentales congelados.
- No modificar GitHub.
- No avanzar a 0B-03, 0C ni fases posteriores.

### Idioma y gate

Responde únicamente en español. Detente al finalizar 0B-02 y devuelve la entrega al editor científico para revisión interna.

---

## English

### Role and scope

Act as the drafting and bibliographic-analysis AI for the main article. Execute only `0B-02 — Retrieval, validation, knowledge, and customs auditability`. Do not draft manuscript sections, declare novelty, close the gap, search the web, or search for new literature.

Read in full only the six PDFs listed in the Spanish section. All other PDFs remain `OUT_OF_SCOPE_FOR_CURRENT_BATCH`.

### Mandatory provenance labels

Use `REPORTED_BY_AUTHORS`, `CRITICAL_INFERENCE`, `NOT_VERIFIABLE_IN_PDF`, and `SECONDARY_CLAIM_UNVERIFIED`. A statement that a paper inherits from a third-party source is not independently verified for our manuscript until the primary source is checked.

### Required distinctions

Historical candidate ranking is distinct from post-ranking normative evidence; nomenclature knowledge used to select a code is distinct from evidence retrieved after ranking; local/model-centric explainability is distinct from documentary traceability/auditability; evidence association is distinct from substantive normative correctness; Top-k candidate retrieval is distinct from overall accuracy; missing grouped splitting does not prove leakage.

### F1–F5 pressure test

For each paper classify its effect on each frozen provisional candidate from 0B-01 as `SUPPORTS_CANDIDATE`, `WEAKENS_CANDIDATE`, `FALSIFIES_CANDIDATE`, `NOT_RELEVANT`, or `UNRESOLVED`. Do not convert surviving candidates into novelty claims.

### Mandatory output

Produce sections A–K defined in the Spanish instructions: integrity control, critical matrix, individual records, functional taxonomy, F1–F5 pressure matrix, batch patterns, updated provisional gap candidates, secondary unverified claims, unresolved verification items, bibliographic recommendations, and final verdict.

### Gate

Respond only in Spanish. Stop after 0B-02 and return the delivery to the scientific editor. Do not advance further and do not modify GitHub.