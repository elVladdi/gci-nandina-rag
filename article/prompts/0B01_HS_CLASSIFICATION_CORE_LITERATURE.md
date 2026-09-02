# Prompt 0B-01 — Núcleo de literatura sobre clasificación HS / Core HS-classification literature

## Español

### Rol

Actúa como IA de redacción y análisis bibliográfico del artículo científico principal. Ejecuta exclusivamente el bloque `0B-01 — Clasificación HS directa y aprendizaje supervisado`.

En este bloque **no redactarás ninguna sección del manuscrito**, **no declararás novelty**, **no definirás todavía el gap definitivo** y **no buscarás literatura nueva**. Tu tarea es leer íntegramente el primer lote de PDF heredados y construir una matriz crítica comparable y auditable.

### Onboarding obligatorio

Accede a la rama `article/main-manuscript` del repositorio `elVladdi/gci-nandina-rag` y lee primero:

1. `article/START_HERE.md`;
2. `article/ARTICLE_STATUS.md`;
3. `article/ARTICLE_WRITING_PLAN.md`;
4. `article/BIBLIOGRAPHIC_FRAMEWORK.md`;
5. `article/literature/0B_LITERATURE_BATCH_PLAN.md`;
6. `article/ground_truth/0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md`;
7. `article/ground_truth/0A02_EXPERIMENTAL_GROUND_TRUTH_FROZEN.md`;
8. este prompt completo.

Usa el ground truth 0A solo para comparar correctamente los antecedentes con el trabajo actual. No reabras 0A ni alteres sus hechos congelados.

### PDFs obligatorios del lote

El autor debe adjuntar exactamente estos ocho PDF del corpus heredado:

1. `Best approaches for HS code prediction.pdf`
2. `An ensemble-based approach for assigning text to correct Harmonized system code.pdf`
3. `Classifying Short Text for the Hrmonized System with Convolutional Neural Networks.pdf`
4. `Automatic Tariff Classification System using Deep Learning.pdf`
5. `HARMONIZED SYSTEM CODE CLASSIFICATION USING TRANSFER LEARNING WITH PRE-TRAINED WEIGHTS.pdf`
6. `Harmonized System Code Classification using Supervised Contrastive Learning with Sentence BERT and Multiple Negative Reannking Loss.PDF`
7. `Application of machine learning for automated HS-6 code assignment.pdf`
8. `Auto-Categorization of HS Code Using Background Net Approach.pdf`

Debes leer **íntegramente** cada PDF. Si falta alguno, si está corrupto o si no puede leerse completamente, identifica el archivo exacto y marca el lote `BLOCKED` o `PASS WITH CORRECTIONS` según la gravedad. No sustituyas un PDF ausente por snippets, conocimiento general, abstracts web ni una referencia secundaria.

### Prohibiciones

- No realizar búsqueda web.
- No buscar literatura nueva.
- No añadir referencias no incluidas en los ocho PDF, salvo mencionar referencias citadas internamente únicamente como contexto bibliográfico no verificado y claramente etiquetado como tal.
- No redactar Introduction, Related Work, Methods, Results, Discussion, Conclusions, Abstract ni Title.
- No declarar que el presente artículo es novedoso o superior.
- No usar resultados experimentales pendientes como si estuvieran cerrados.
- No modificar GitHub.
- No avanzar a 0B-02, 0C o fases posteriores.
- No corregir silenciosamente inconsistencias de los papers; regístralas.

### Marco de análisis obligatorio por paper

Para cada trabajo extrae únicamente lo que el PDF completo soporte:

- identificación bibliográfica tal como aparece en el PDF;
- año;
- tipo de publicación, si puede determinarse desde el PDF;
- problema que aborda;
- tarea exacta;
- país/jurisdicción o contexto comercial, si está indicado;
- dataset/corpus y tamaño;
- origen de datos;
- idioma(s);
- nivel objetivo de la jerarquía HS (capítulo/partida/subpartida/HS-6/otro);
- unidad de observación;
- input utilizado;
- método/modelo;
- representación de texto/features;
- uso explícito de jerarquía;
- uso de descripciones normativas/tariff nomenclature;
- uso de precedentes históricos;
- tipo de salida: clasificación, ranking, retrieval, validación, etc.;
- métricas;
- esquema de partición/validación;
- controles contra leakage o dependencia, si existen;
- baselines;
- principales resultados reportados;
- explicabilidad;
- auditabilidad/trazabilidad;
- uso de LLM, si existe;
- limitaciones reconocidas por los autores;
- limitaciones metodológicas adicionales que se desprendan directamente del diseño descrito, marcándolas como `INFERENCIA_CRITICA` y no como afirmación del paper;
- transferibilidad al contexto NANDINA/Clase 87;
- similitud con el presente trabajo;
- diferencia sustantiva con el presente trabajo.

### Reglas de comparación con el presente artículo

Recuerda que el trabajo actual:

- separa recuperación histórica para ranking de candidatos, recuperación normativa para evidencia y LLM local para explicación controlada;
- usa Top-3 fijo;
- no permite que el LLM clasifique desde cero ni reordene el ranking oficial;
- trata Top-k histórico como candidate retrieval, no accuracy global;
- mantiene SERIE como unidad de análisis y DAM como unidad de agrupamiento cuando existe dependencia;
- enfatiza trazabilidad documental y auditabilidad;
- está restringido experimentalmente a Clase 87;
- no constituye clasificación legal vinculante.

No fuerces diferencias artificiales: si un paper comparte una característica, indícalo. Si no puede determinarse desde el PDF, usa `NO_VERIFICABLE_EN_PDF`.

### Estado bibliográfico

Como estos trabajos pertenecen al corpus heredado, su estado inicial es `INHERITED_CORE`. Al final del análisis recomienda para cada uno uno de:

- `KEEP_CORE`: claramente pertinente para el artículo;
- `KEEP_SUPPORTING`: útil como apoyo secundario/metodológico;
- `REVIEW_REQUIRED`: metadata, integridad o interpretación requiere comprobación posterior;
- `EXCLUDE_FROM_ARTICLE`: revisado pero no suficientemente pertinente para el artículo principal.

La recomendación no modifica por sí sola el registro bibliográfico ni elimina referencias heredadas de la tesis.

### Verificación de consistencia interna

Busca explícitamente:

- totales que no coincidan con sumas de train/dev/test;
- cambios de nivel HS entre título, método y evaluación;
- confusión entre clasificación y retrieval;
- métricas sin denominador o protocolo claro;
- comparación de modelos bajo particiones distintas;
- posible leakage por duplicados, entidades o agrupamientos si el diseño lo permite inferir;
- uso de accuracy que oculte jerarquía o imbalance;
- afirmaciones de explicabilidad no acompañadas de evidencia verificable;
- claims de generalización no respaldados por el diseño.

No declares un error si el PDF no permite demostrarlo. Clasifica incertidumbres como `REVIEW_REQUIRED`.

### Formato de salida obligatorio

#### A. Control de integridad del lote

Tabla:

`ID | archivo | lectura completa sí/no | metadata suficiente sí/no | observaciones de integridad`.

#### B. Matriz crítica paper por paper

Una fila por trabajo con, como mínimo:

`ID | referencia corta | tarea | nivel HS | dataset/origen | N | método | validación | métricas principales | jerarquía | normativa | precedentes históricos | explicabilidad/auditabilidad | principales resultados | limitaciones | estado recomendado`.

#### C. Fichas analíticas individuales

Para cada uno de los ocho papers, presenta una ficha estructurada con todos los campos del marco de análisis obligatorio. Distingue expresamente:

- `REPORTADO_POR_AUTORES`;
- `INFERENCIA_CRITICA`;
- `NO_VERIFICABLE_EN_PDF`.

#### D. Comparación transversal

Construye una tabla comparativa centrada en dimensiones relevantes para el artículo actual:

`paper | clasificación directa | ranking/retrieval | jerarquía | evidencia normativa | precedentes históricos | LLM | explicación | trazabilidad/auditabilidad | control de dependencia/leakage | cercanía al presente enfoque`.

#### E. Patrones de la literatura del lote

Resume únicamente patrones respaldados por al menos dos papers del lote. No generalices a toda la literatura HS.

#### F. Candidatos provisionales a gap

Formula de 3 a 6 **candidatos provisionales**, no conclusiones de novelty. Para cada candidato indica:

- qué papers del lote lo motivan;
- qué evidencia falta todavía en otros lotes;
- qué podría falsarlo o debilitarlo.

Usa la etiqueta `CANDIDATE_GAP_ONLY`.

#### G. Inconsistencias y verificaciones pendientes

Lista cerrada de DOI/metadatos/cifras/diseños que necesiten verificación posterior. No uses web para resolverlos en este bloque.

#### H. Recomendación de función bibliográfica

Tabla:

`paper | KEEP_CORE / KEEP_SUPPORTING / REVIEW_REQUIRED / EXCLUDE_FROM_ARTICLE | función potencial en el artículo | justificación`.

#### I. Dictamen

Uno de:

- `PASS`;
- `PASS WITH CORRECTIONS`;
- `BLOCKED`.

### Idioma

Responde únicamente en español. El bilingüismo aplica a los artefactos que posteriormente se integren en GitHub, no a esta respuesta de chat.

### Gate

Detente al terminar 0B-01. La entrega debe regresar al editor científico para revisión interna. No avances a 0B-02 y no busques literatura nueva salvo instrucción posterior explícita.

---

## English

### Role

Act as the drafting and bibliographic-analysis AI for the main scientific article. Execute only `0B-01 — Direct HS classification and supervised learning`.

In this block, **do not draft any manuscript section**, **do not declare novelty**, **do not define the final gap**, and **do not search for new literature**. Read the complete inherited PDFs in the first batch and build a critical, comparable, auditable matrix.

### Mandatory onboarding

Access branch `article/main-manuscript` of `elVladdi/gci-nandina-rag` and first read:

1. `article/START_HERE.md`;
2. `article/ARTICLE_STATUS.md`;
3. `article/ARTICLE_WRITING_PLAN.md`;
4. `article/BIBLIOGRAPHIC_FRAMEWORK.md`;
5. `article/literature/0B_LITERATURE_BATCH_PLAN.md`;
6. `article/ground_truth/0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md`;
7. `article/ground_truth/0A02_EXPERIMENTAL_GROUND_TRUTH_FROZEN.md`;
8. this complete prompt.

Use frozen 0A ground truth only to compare prior work correctly against the present study. Do not reopen 0A or alter its frozen facts.

### Required PDFs

The author must attach exactly the eight inherited-corpus PDFs listed in the Spanish section above. Read each PDF **in full**. If any file is missing, corrupted, or not fully readable, identify it exactly and mark the batch `BLOCKED` or `PASS WITH CORRECTIONS` depending on severity. Do not replace a missing PDF with snippets, general knowledge, web abstracts, or secondary references.

### Prohibitions

- No web search.
- No search for new literature.
- No manuscript drafting.
- No novelty/superiority claims.
- No use of pending experiments as closed findings.
- No GitHub modifications.
- Do not advance beyond 0B-01.

### Required analysis

For every paper, extract only what the full PDF supports: bibliographic identification, year, publication type when determinable, problem, exact task, context/jurisdiction, dataset/corpus and size, data origin, language, HS level, observation unit, input, method/model, text representation/features, hierarchy use, normative descriptions, historical precedents, output type, metrics, split/validation scheme, leakage/dependence controls, baselines, reported results, explainability, auditability/traceability, LLM use, author-acknowledged limitations, critical design inferences clearly labelled as such, transferability to NANDINA/Class 87, similarities with the present work, and substantive differences.

Use `NO_VERIFICABLE_EN_PDF` whenever the PDF does not establish a point.

### Bibliographic recommendation

All eight start as `INHERITED_CORE`. Recommend one of `KEEP_CORE`, `KEEP_SUPPORTING`, `REVIEW_REQUIRED`, or `EXCLUDE_FROM_ARTICLE`. The recommendation does not itself alter the bibliographic registry or remove inherited thesis references.

### Mandatory output

Produce sections A–I exactly as defined in the Spanish instructions: batch-integrity control, paper-level critical matrix, individual analytical records, cross-paper comparison, batch-level patterns, provisional gap candidates labelled `CANDIDATE_GAP_ONLY`, unresolved verification items, bibliographic-function recommendation, and final verdict `PASS`, `PASS WITH CORRECTIONS`, or `BLOCKED`.

### Language and gate

Respond only in Spanish. Stop after 0B-01 and return the delivery to the scientific editor for internal review. Do not advance to 0B-02 or search for new literature unless explicitly instructed later.
