# Prompt 0B-04A — Fundamentos de ranking y recuperación de información / Ranking and information-retrieval foundations

## Español

### Rol y alcance

Actúa como IA de redacción y análisis bibliográfico del artículo científico principal. Ejecuta **exclusivamente** `0B-04A — Fundamentos de ranking y recuperación de información`.

Este bloque no busca demostrar novelty ni construir una revisión general de Information Retrieval. Su finalidad es establecer con precisión qué fundamentos metodológicos respaldan o delimitan las decisiones de recuperación del artículo: BM25, representación densa, bi-encoders, late interaction, reranking y búsqueda aproximada de vecinos.

No redactes secciones del manuscrito, no cierres el gap, no declares superioridad de un paradigma sobre otro, no busques literatura nueva y no modifiques GitHub ni el Plan Maestro.

### Onboarding obligatorio

Accede a la rama `article/main-manuscript` de `elVladdi/gci-nandina-rag` y lee primero:

1. `article/START_HERE.md`;
2. `article/ARTICLE_STATUS.md`;
3. `article/ARTICLE_WRITING_PLAN.md`;
4. `article/BIBLIOGRAPHIC_FRAMEWORK.md`;
5. `article/literature/0B_LITERATURE_BATCH_PLAN.md`;
6. `article/literature/0B01_HS_CLASSIFICATION_CORE_LITERATURE_FROZEN.md`;
7. `article/literature/0B02_RETRIEVAL_VALIDATION_KNOWLEDGE_AUDITABILITY_FROZEN.md`;
8. `article/literature/0B03A_LLM_RAG_MULTIMODAL_CUSTOMS_FROZEN.md`;
9. `article/literature/0B03B_AGENTS_HIERARCHICAL_REGULATORY_REASONING_FROZEN.md`;
10. `article/ground_truth/0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md`;
11. `article/ground_truth/0A02_EXPERIMENTAL_GROUND_TRUTH_FROZEN.md`;
12. este prompt completo.

No reabras ni reinterpretes los freezes anteriores.

### PDFs asignados

Analiza **exclusivamente** estos seis PDF del corpus heredado:

1. `The Probabilistic Relevance Framework: BM25 and Beyond.pdf`
2. `Sentence-BERT.pdf`
3. `Dense passage retrieval for open-domain question answering. Proceedings of EMNLP 2020.pdf`
4. `ColBERT- Efficient and effective passage search via contextualized late interaction over BERT.pdf`
5. `Efficient and robust approximate nearest neighbor search using hierarchical navigable small world graphs.pdf`
6. `Passage Re-Ranking with BERT.pdf`

Si existen sufijos automáticos o pequeñas variaciones de nombre, identifica la obra por su contenido. Si alguno no está accesible o no puede leerse íntegramente, identifica únicamente ese archivo. No sustituyas su contenido por web, abstracts, snippets, tesis, Anexo, conocimiento general ni otro PDF.

Todos los demás documentos del corpus quedan `OUT_OF_SCOPE_FOR_0B04A`.

### Objetivo científico del lote

El lote debe producir un mapa metodológico que permita responder, sin overclaiming:

1. Qué es realmente BM25 dentro del probabilistic relevance framework y qué supuestos/funciones cumple.
2. Qué diferencia hay entre lexical/sparse retrieval y representación densa.
3. Qué diferencia hay entre:
   - sentence embedding / semantic similarity;
   - dense passage retrieval;
   - late interaction;
   - cross-encoder reranking;
   - approximate nearest-neighbor indexing/search.
4. Qué componente **genera candidatos**, cuál **reordena candidatos** y cuál solo **acelera la búsqueda**.
5. Qué supervisión requiere cada método y sobre qué dominios/datasets fue evaluado.
6. Qué métricas utiliza cada paper y qué no puede compararse directamente entre trabajos.
7. Qué parte de estos fundamentos es pertinente para justificar el BM25 histórico y normativo del proyecto actual y qué parte sirve solo como contraste metodológico.
8. Qué afirmaciones NO pueden hacerse a partir de estos papers, especialmente:
   - “BM25 es superior a dense retrieval” en general;
   - “dense retrieval es superior a BM25” en general;
   - “HNSW mejora relevancia semántica”;
   - “SBERT es un buscador completo”;
   - “BERT reranking equivale a candidate generation”;
   - “resultados de QA/open-domain retrieval se transfieren directamente a HS/NANDINA”.

### Regla crítica de procedencia

Usa obligatoriamente:

- `REPORTADO_POR_AUTORES`;
- `INFERENCIA_CRITICA`;
- `NO_VERIFICABLE_EN_PDF`;
- `SECONDARY_CLAIM_UNVERIFIED`.

Una afirmación que un paper atribuya a una fuente tercera no se convierte en hecho independiente del artículo. Si una cifra, benchmark histórico, claim de superioridad o descripción de otro método proviene de una cita secundaria, márcala como `SECONDARY_CLAIM_UNVERIFIED` salvo que esté directamente evaluada en el propio paper.

### Distinciones metodológicas obligatorias

Mantén separadas las siguientes categorías:

- `SPARSE_LEXICAL_RETRIEVAL`;
- `SENTENCE_EMBEDDING`;
- `DENSE_BIENCODER_RETRIEVAL`;
- `LATE_INTERACTION_RETRIEVAL`;
- `CROSS_ENCODER_RERANKING`;
- `ANN_INDEX_SEARCH`;
- `CANDIDATE_GENERATION`;
- `RERANKING`;
- `INDEX_ACCELERATION`.

Reglas concretas:

- HNSW es un método de ANN/indexación/búsqueda; no es un modelo semántico de representación.
- Un sentence encoder no equivale automáticamente a un sistema de retrieval completo.
- Un cross-encoder de reranking normalmente presupone candidatos previos.
- Dense retrieval y late interaction no deben tratarse como la misma arquitectura.
- BM25 no debe describirse simplemente como “conteo de palabras”; reconstruye su fundamento y sus componentes solo en el nivel soportado por el paper.
- Las métricas y resultados de benchmarks distintos no se comparan como si provinieran del mismo experimento.
- Candidate recall/ranking metrics no equivalen a accuracy de clasificación arancelaria.

### Marco obligatorio por paper

Extrae únicamente lo soportado por el PDF:

- identificación bibliográfica y tipo documental;
- problema IR exacto;
- unidad recuperada: documento/passage/sentence/candidate;
- query y representación documental;
- sparse/dense/hybrid si aplica;
- arquitectura de encoder/interacción;
- supervisión y datos de entrenamiento;
- candidate generation vs reranking vs indexing;
- función del índice/ANN si aplica;
- complejidad/eficiencia/latencia solo si el paper la mide;
- benchmarks y tamaño de datos cuando sea necesario para interpretar el resultado;
- métricas;
- resultados principales relevantes al mecanismo, sin convertirlos en comparaciones cross-paper;
- ablations/controles importantes;
- limitaciones reconocidas por autores;
- limitaciones adicionales como `INFERENCIA_CRITICA`;
- qué decisión metodológica del presente artículo puede respaldar;
- qué decisión NO respalda;
- transferibilidad y límites hacia descripciones comerciales cortas/NANDINA.

### Relación con los candidatos F1–F5

Este lote es **fundacional**, no un lote de prior art aduanero. Por ello F1–F5 no deben recibir artificialmente `SUPPORTS_CANDIDATE` solo porque un paper no implemente la arquitectura actual.

Para cada paper usa una de estas etiquetas respecto de F1–F5:

- `METHOD_FOUNDATION_RELEVANT`;
- `METHOD_CONTRAST_RELEVANT`;
- `NOT_RELEVANT_TO_GAP_CANDIDATE`;
- `POTENTIAL_PRESSURE_ON_FORMULATION`.

Solo utiliza `POTENTIAL_PRESSURE_ON_FORMULATION` si el mecanismo del paper contradice realmente una formulación metodológica general. No conviertas ausencia de un componente en evidencia de gap.

Candidatos vigentes después de 0B-03B:

- **F1:** precedentes históricos recuperados generan/fijan ranking; normativa llega después y no reordena.
- **F2:** generador exclusivamente explicativo sobre ranking/Top-k fijado externamente por un componente previo independiente; no introduce/elimina/sustituye/reordena códigos ni retroalimenta clasificación.
- **F3:** control de dependencia por unidad/grupo cuando existen observaciones relacionadas susceptibles de cruzar particiones.
- **F4:** candidate/predictive performance, path validity, rule consistency y evidence grounding no equivalen a corrección sustantiva/jurídica adjudicada.
- **F5:** evaluación formal y separada de auditabilidad documental por salida.

G6 ya está eliminado como gap candidate. G7 ya está absorbido en F2. No los reabras.

### Verificaciones críticas específicas

Busca especialmente:

1. En BM25, qué significa TF saturation, document-length normalization e IDF dentro de la formulación descrita por los autores.
2. En SBERT, qué arquitectura permite producir embeddings independientes y qué tareas/métricas evalúa realmente.
3. En DPR, cómo se entrenan query/passage encoders, qué negativos utiliza y en qué sentido reemplaza o complementa lexical retrieval dentro de su benchmark.
4. En ColBERT, qué significa late interaction, cómo difiere de bi-encoder y cross-encoder y qué trade-off pretende resolver.
5. En HNSW, qué problema computacional resuelve, qué son los niveles/grafo navegable y qué relación tiene con ANN recall/eficiencia, no con relevancia semántica del embedding.
6. En BERT reranking, de dónde provienen los candidatos iniciales y qué parte del pipeline reordena.
7. Si alguna comparación BM25 vs dense/late interaction utiliza el mismo benchmark y protocolo; cuando no sea el caso, no sintetices una superioridad global.
8. Si las cifras citadas frecuentemente por otros trabajos están efectivamente en el PDF o son secundarias.
9. Si el paper reporta reproducibilidad/hiperparámetros suficientes para el claim concreto que se quiere extraer.
10. Si una afirmación de eficiencia depende de hardware/índice/configuración específica.

### Gobernanza bibliográfica

Los seis trabajos son referencias heredadas/fundacionales del corpus y pueden analizarse aunque sean anteriores a 2022 o proceedings. Esto **no obliga a citarlos todos** en el manuscrito final.

Para cada paper devuelve:

1. función científica: `KEEP_CORE_METHOD`, `KEEP_SUPPORTING_METHOD`, `REVIEW_REQUIRED`, `EXCLUDE_FROM_ARTICLE`;
2. uso potencial: `METHOD_DEFINITION`, `METHOD_JUSTIFICATION`, `METHOD_CONTRAST`, `METRIC_CONTEXT`, `IMPLEMENTATION_CONTEXT`;
3. claim concreto que podría respaldar y claim que explícitamente no debe respaldar.

### Formato de salida obligatorio

#### A. Control de integridad
`ID | archivo | lectura completa sí/no | metadata suficiente sí/no | tipo documental | observaciones`

#### B. Matriz funcional IR
Una fila por paper con: problema, unidad recuperada, representación, arquitectura, supervisión, candidate generation/reranking/indexing, métricas, benchmark, resultado relevante, limitación y función para el artículo.

#### C. Fichas individuales
Una por paper usando las cuatro etiquetas de procedencia.

#### D. Taxonomía metodológica
Clasifica cada trabajo según las categorías obligatorias del prompt.

#### E. Mapa del pipeline
Para cada método indica explícitamente si ocupa:
`QUERY/DOCUMENT REPRESENTATION -> CANDIDATE GENERATION -> ANN/INDEX SEARCH -> RERANKING -> FINAL RANKING`.
No fuerces a todos los papers a ocupar todas las etapas.

#### F. Matriz de relevancia para F1–F5
`paper | F1 | F2 | F3 | F4 | F5 | justificación` usando solo las cuatro etiquetas fundacionales definidas arriba.

#### G. Claims metodológicos autorizables
Lista únicamente formulaciones que, tras lectura completa, serían defendibles como antecedentes metodológicos. Para cada una indica el paper que la respalda y el límite de alcance.

#### H. Claims prohibidos o excesivos
Lista cerrada de formulaciones que estos papers **no** permiten sostener.

#### I. Inconsistencias y claims secundarios pendientes
Sin web. Registra `NO_VERIFICABLE_EN_PDF` y `SECONDARY_CLAIM_UNVERIFIED` cuando corresponda.

#### J. Recomendación bibliográfica
`paper | función científica | uso potencial | recomendación | justificación`.

#### K. Dictamen
`PASS`, `PASS WITH CORRECTIONS` o `BLOCKED`.

### Prohibiciones

- No web.
- No literatura nueva.
- No usar otros PDF del corpus.
- No redactar secciones del artículo.
- No declarar novelty, gap definitivo o superioridad general de métodos.
- No modificar GitHub.
- No modificar el Plan Maestro.
- No alterar el ground truth 0A.
- No reabrir G6/G7.
- No avanzar a 0B-04B, 0B-05, 0B-06, 0C ni fases posteriores.

### Idioma y gate

Responde únicamente en español. Detente al finalizar 0B-04A y devuelve la entrega al editor científico para revisión interna.

---

## English

### Role and scope

Act as the drafting/bibliographic-analysis AI for `0B-04A — Ranking and information-retrieval foundations`. Analyze only the six assigned foundational PDFs. The purpose is methodological clarification, not novelty discovery: distinguish lexical BM25 retrieval, sentence embeddings, dense bi-encoder retrieval, late interaction, cross-encoder reranking, and ANN index/search.

Do not search the web, add literature, draft manuscript sections, declare a final gap/novelty, modify GitHub or the Master Plan, reopen frozen blocks, or advance beyond 0B-04A.

Use the mandatory provenance labels and preserve the distinction between representation, candidate generation, ANN/index acceleration, reranking, and final ranking. HNSW is an ANN/index-search method rather than a semantic representation model; sentence embedding is not automatically a full retriever; reranking presupposes prior candidates; and benchmark results from different tasks must not be compared as global method superiority.

Because this is a foundational-method batch, F1–F5 must be evaluated with `METHOD_FOUNDATION_RELEVANT`, `METHOD_CONTRAST_RELEVANT`, `NOT_RELEVANT_TO_GAP_CANDIDATE`, or `POTENTIAL_PRESSURE_ON_FORMULATION`; absence of the current architecture is not evidence of a gap.

Produce sections A–K exactly as defined in the Spanish instructions, respond only in Spanish, and stop after 0B-04A.