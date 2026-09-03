# Prompt 0B-03A — LLM, RAG y multimodalidad en clasificación/compliance aduanero / LLM, RAG, and multimodality in customs classification/compliance

## Español

### Rol y alcance

Actúa como IA de redacción y análisis bibliográfico del artículo científico principal. Ejecuta **exclusivamente** `0B-03A — LLM, RAG y multimodalidad aplicada a clasificación/compliance aduanero`.

No redactes secciones del manuscrito, no declares novelty, no cierres el gap y no busques literatura nueva. Tu tarea es leer íntegramente los seis PDF asignados, construir un mapa crítico comparable y someter a presión los candidatos provisionales heredados de 0B-01/0B-02.

### Onboarding obligatorio

Accede a la rama `article/main-manuscript` de `elVladdi/gci-nandina-rag` y lee primero:

1. `article/START_HERE.md`;
2. `article/ARTICLE_STATUS.md`;
3. `article/ARTICLE_WRITING_PLAN.md`;
4. `article/BIBLIOGRAPHIC_FRAMEWORK.md`;
5. `article/literature/0B_LITERATURE_BATCH_PLAN.md`;
6. `article/literature/0B01_HS_CLASSIFICATION_CORE_LITERATURE_FROZEN.md`;
7. `article/literature/0B02_RETRIEVAL_VALIDATION_KNOWLEDGE_AUDITABILITY_FROZEN.md`;
8. `article/ground_truth/0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md`;
9. `article/ground_truth/0A02_EXPERIMENTAL_GROUND_TRUTH_FROZEN.md`;
10. este prompt completo.

No reabras 0A, 0B-01 ni 0B-02.

### PDFs asignados

Analiza **exclusivamente** estos seis PDF ya disponibles en el corpus de 62:

1. `Automatic product classification in international trade Machine learning and large language models.pdf`
2. `Automating Harmonized System (HS) Code Classification from Unstructured Shipping Manifests using Large Language Models.pdf`
3. `Development of an Automated HS Code Classification System Using LLM Based on an Optimized RAG Framework.pdf`
4. `ICCA-RAG Intelligent Customs Clearance Assistant Using RAG.pdf`
5. `LLM-based robust product classification in commerce and compliance.pdf`
6. `Multimodal approach for Harmonized System code prediction.pdf`

Si existen copias con sufijos automáticos o pequeñas variaciones de título, trátalas como la misma obra cuando el contenido lo confirme. Si alguno no está accesible o no puede leerse íntegramente, identifica solo ese archivo; no sustituyas su contenido por abstracts, snippets, tesis, Anexo, conocimiento general ni referencias secundarias.

Los otros 56 PDF del corpus quedan `OUT_OF_SCOPE_FOR_0B03A`.

### Regla crítica de procedencia

Usa obligatoriamente:

- `REPORTADO_POR_AUTORES`;
- `INFERENCIA_CRITICA`;
- `NO_VERIFICABLE_EN_PDF`;
- `SECONDARY_CLAIM_UNVERIFIED`.

Una afirmación factual que un paper tome de una fuente tercera no se convierte en un hecho independiente para nuestro artículo hasta verificar la fuente primaria. Registra como `SECONDARY_CLAIM_UNVERIFIED` cualquier cifra sobre volumen mundial de comercio/declaraciones, error humano, sanciones, ahorro, eficiencia, costes, tiempos u otros efectos que no haya medido directamente el paper.

### Distinciones metodológicas obligatorias

Para el presente artículo:

- ranking histórico = recuperación de candidatos desde precedentes históricos;
- normativa = evidencia documental posterior a candidatos ya fijados; no reemplaza ni reordena el ranking histórico;
- RAG usado para **clasificar/decidir** ≠ RAG usado para **aportar evidencia** a candidatos ya fijados;
- LLM que produce el código ≠ LLM que solo explica códigos recibidos;
- LLM reranker ≠ LLM explainer;
- explanation/rationale ≠ documentary auditability;
- uso de documentos regulatorios como contexto de generación ≠ demostración de corrección jurídica;
- Top-k candidate retrieval ≠ accuracy global;
- `human-in-the-loop` ≠ garantía de auditabilidad;
- multimodalidad ≠ mayor validez por sí misma;
- ausencia de group split documentado ≠ leakage demostrado.

### Marco obligatorio por paper

Extrae únicamente lo soportado por el PDF:

- identificación bibliográfica, versión y tipo de publicación;
- tarea exacta;
- jurisdicción/nomenclatura/nivel HS;
- dataset/corpus, N, clases, origen, unidad de observación;
- split/validación y controles de duplicados/dependencia;
- input: texto, imagen, campos estructurados, documentos, reglas u otros;
- LLM/modelo(s), tamaño si está informado, prompting/fine-tuning/ICL;
- retrieval: qué recupera, desde qué corpus y con qué método;
- RAG: qué información entra al contexto y **para qué función causal**;
- reranking: sí/no y qué reordena;
- jerarquía: si gobierna la inferencia o solo aparece en labels/corpus;
- generación del código: quién decide/proporciona el código final;
- restricciones de salida: si existen códigos permitidos, Top-k fijo, validación de código, schema o guardrails;
- evidencia/citas: si son localizables, autoritativas y asociadas a la salida;
- explicabilidad/auditabilidad y cómo se evalúan;
- intervención humana;
- métricas, denominadores y principales resultados;
- robustez a descripciones incompletas/ruidosas si aplica;
- modalidad visual y contribución marginal/condicionada si aplica;
- limitaciones reconocidas por autores;
- limitaciones adicionales como `INFERENCIA_CRITICA`;
- transferibilidad a NANDINA/Clase 87;
- similitud/diferencia real respecto del presente proyecto.

### Pressure test obligatorio: F1–F5 y G6

Para cada paper clasifica el efecto sobre cada candidato como:

- `SUPPORTS_CANDIDATE`;
- `WEAKENS_CANDIDATE`;
- `FALSIFIES_CANDIDATE`;
- `NOT_RELEVANT`;
- `UNRESOLVED`.

Candidatos vigentes:

- **F1:** precedentes históricos recuperados fijan ranking; evidencia normativa se recupera solo después y no reordena.
- **F2:** generador posterior opera sobre Top-k fijo y no puede introducir códigos externos ni alterar orden.
- **F3:** control explícito de dependencia mediante unidad administrativa/grupo cuando observaciones relacionadas pueden cruzar particiones.
- **F4:** candidate retrieval/coherence scoring deben separarse de corrección sustantiva/jurídica.
- **F5:** evaluación formal y separada de trazabilidad/auditabilidad documental mediante protocolo explícito.
- **G6:** ground truth independiente/adjudicado para correctness, separado de labels históricos asumidos correctos.

No declares novelty aunque un candidato sobreviva.

### Verificaciones críticas específicas

Busca especialmente:

1. Si el LLM **clasifica desde cero** o trabaja sobre candidatos previamente fijados.
2. Si RAG recupera aranceles/notas/casos y si esos documentos determinan el código o solo lo justifican.
3. Si existe reranking y si la salida del LLM puede cambiar el orden de candidatos.
4. Si el sistema valida que el código generado exista en la nomenclatura.
5. Si aparecen hallucinated/invalid codes y cómo se controlan.
6. Si el paper usa términos como “explainable”, “compliant”, “accurate”, “robust” o “auditable” sin protocolo que mida exactamente ese constructo.
7. Si las comparaciones de LLMs usan mismos prompts, mismos datos, mismo contexto y mismos denominadores.
8. Si los datasets son realmente HS/HTS o clasificación de productos genérica con conexión indirecta a compliance.
9. Si los resultados multimodales mejoran respecto del texto y bajo qué combinación exacta de features.
10. Si cualquier claim de eficiencia/coste/tiempo proviene de medición directa o de extrapolación/terceros.

### Estado bibliográfico

Los seis trabajos son parte del corpus proporcionado por el autor. Recomienda uno de:

- `KEEP_CORE`;
- `KEEP_SUPPORTING`;
- `REVIEW_REQUIRED`;
- `EXCLUDE_FROM_ARTICLE`.

La recomendación no autoriza automáticamente su cita final.

### Formato de salida obligatorio

#### A. Control de integridad
`ID | archivo | lectura completa sí/no | metadata suficiente sí/no | observaciones`

#### B. Matriz crítica
Una fila por paper con tarea, datos, input, modelo/LLM, retrieval/RAG, función del conocimiento, output, restricciones, validación, métricas, resultados, explicación/auditabilidad, dependencia, limitaciones y función bibliográfica.

#### C. Fichas individuales
Una por paper usando las cuatro etiquetas de procedencia.

#### D. Taxonomía funcional
Usa, cuando corresponda: `DIRECT_LLM_CLASSIFICATION`, `IN_CONTEXT_CLASSIFICATION`, `FINE_TUNED_LLM`, `RAG_CLASSIFICATION`, `RAG_EVIDENCE_SUPPORT`, `RERANKING`, `MULTIMODAL_CLASSIFICATION`, `ROBUSTNESS_EVALUATION`, `HUMAN_DECISION_SUPPORT`, `EXPLAINABILITY`, `AUDITABILITY_SUPPORT`, `HYBRID`.

#### E. Matriz de presión F1–F5/G6
`paper | F1 | F2 | F3 | F4 | F5 | G6 | evidencia concreta`.

#### F. Patrones del lote
Solo patrones respaldados por al menos dos papers.

#### G. Candidatos a gap actualizados
Mantén, estrecha, debilita, falsifica o elimina candidatos. Los nuevos deben ser `CANDIDATE_GAP_ONLY` y explicar qué falta revisar en 0B-03B/0B-04/0B-05.

#### H. Claims secundarios pendientes
`paper | claim secundario | fuente primaria citada | posible utilidad | SECONDARY_CLAIM_UNVERIFIED`.

#### I. Inconsistencias y verificaciones pendientes
Lista cerrada, sin web.

#### J. Recomendación bibliográfica
`paper | recomendación | función potencial | justificación`.

#### K. Dictamen
`PASS`, `PASS WITH CORRECTIONS` o `BLOCKED`.

### Prohibiciones

- No web.
- No literatura nueva.
- No usar los otros 56 PDF.
- No redactar secciones del artículo.
- No declarar novelty, gap definitivo o superioridad.
- No modificar GitHub.
- No alterar claims experimentales congelados.
- No avanzar a 0B-03B, 0B-04, 0C ni fases posteriores.

### Idioma y gate

Responde únicamente en español. Detente al finalizar 0B-03A y devuelve la entrega al editor científico para revisión interna.

---

## English

### Role and scope

Act as the drafting/bibliographic-analysis AI for the main article. Execute only `0B-03A — LLM, RAG, and multimodality in customs classification/compliance`. Read in full only the six PDFs listed in the Spanish section. Do not search the web, add literature, draft manuscript sections, declare novelty, close the gap, modify GitHub, or advance further.

Use the mandatory provenance labels `REPORTED_BY_AUTHORS`, `CRITICAL_INFERENCE`, `NOT_VERIFIABLE_IN_PDF`, and `SECONDARY_CLAIM_UNVERIFIED`.

The analysis must distinguish LLMs that directly decide codes from LLMs that only explain fixed candidates; RAG used for code determination from RAG used only as post-ranking evidence; reranking from explanation; visible rationale from documentary auditability; multimodal input from evidence-based justification; and grouped-independence controls from simple random splits.

Pressure-test F1–F5 and G6 exactly as defined in the Spanish instructions. Any surviving or newly proposed gap remains `CANDIDATE_GAP_ONLY` until later batches and Phase 0C.

Produce sections A–K defined above, respond only in Spanish, and stop after 0B-03A.
