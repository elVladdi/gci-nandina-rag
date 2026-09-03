# Prompt 0B-04B — Fundamentos de RAG, transformación de consultas y grounding / RAG, query-transformation, and grounding foundations

## Español

### Rol y alcance

Actúa como IA de redacción y análisis bibliográfico del artículo científico principal. Ejecuta **exclusivamente** `0B-04B — Fundamentos de RAG, transformación de consultas y grounding`.

Este bloque es **fundacional y metodológico**. No busca demostrar novelty ni establecer un gap aduanero. Su finalidad es reconstruir con precisión distintas formas de acoplar recuperación y generación, distinguir recuperación durante preentrenamiento de recuperación en inferencia, separar query transformation de evidence retrieval y analizar qué significan realmente `grounding`, `evidentiality`, `provenance` y generación condicionada por pasajes recuperados.

No redactes secciones del manuscrito, no cierres el gap, no declares superioridad universal de RAG sobre modelos paramétricos, no busques literatura nueva y no modifiques GitHub ni el Plan Maestro.

### Onboarding obligatorio

Accede a la rama `article/main-manuscript` de `elVladdi/gci-nandina-rag` y lee primero:

1. `article/START_HERE.md`;
2. `article/ARTICLE_STATUS.md`;
3. `article/ARTICLE_WRITING_PLAN.md`;
4. `article/DECISIONS.md`;
5. `article/SOURCE_REGISTRY.md`;
6. `article/CLAIM_EVIDENCE_MATRIX.md`;
7. `article/STYLE_GUIDE.md`;
8. `article/BIBLIOGRAPHIC_FRAMEWORK.md`;
9. `article/literature/0B_LITERATURE_BATCH_PLAN.md`;
10. `article/literature/0B04_SCOPE_AND_BATCH_PLAN.md`;
11. `article/literature/0B01_HS_CLASSIFICATION_CORE_LITERATURE_FROZEN.md`;
12. `article/literature/0B02_RETRIEVAL_VALIDATION_KNOWLEDGE_AUDITABILITY_FROZEN.md`;
13. `article/literature/0B03A_LLM_RAG_MULTIMODAL_CUSTOMS_FROZEN.md`;
14. `article/literature/0B03B_AGENTS_HIERARCHICAL_REGULATORY_REASONING_FROZEN.md`;
15. `article/literature/0B04A_IR_RANKING_RETRIEVAL_FOUNDATIONS_FROZEN.md`;
16. `article/ground_truth/0A01_DOCUMENTARY_GROUND_TRUTH_FROZEN.md`;
17. `article/ground_truth/0A02_EXPERIMENTAL_GROUND_TRUTH_FROZEN.md`;
18. este prompt completo.

No reabras ni reinterpretes los freezes anteriores.

### PDFs asignados

Analiza **exclusivamente** estos seis PDF del corpus heredado:

1. `Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.pdf`
2. `REALM-Retrieval-Augmented Language Model Pre-Training.pdf`
3. `Leveraging passage retrieval with generative models for open domain question answering.pdf`
4. `Query2doc-Query Expansion whit Large Lenguage Models.pdf`
5. `Query Rewriting for Retrieval-Augmented Large Language Models.pdf`
6. `Evidentiality-guided Generation for Knowledge-Intensive NLP Tasks.pdf`

Si hay duplicados, sufijos automáticos o pequeñas variaciones ortográficas del nombre, identifica cada obra por su identidad científica. Si alguno no está accesible o no puede leerse íntegramente, identifica únicamente ese archivo. No sustituyas su contenido con web, abstracts, snippets, tesis, Anexo, conocimiento general ni otros PDF.

Todos los demás documentos del corpus quedan `OUT_OF_SCOPE_FOR_0B04B`.

### Objetivo científico del lote

El lote debe permitir responder, sin overclaiming:

1. Qué significa `retrieval-augmented generation` en Lewis et al. y cómo se relacionan memoria paramétrica, memoria no paramétrica, retriever y generator.
2. En qué se diferencia REALM por incorporar retrieval en el **preentrenamiento** y cómo usa retrieval en fine-tuning/inferencia.
3. Cómo Fusion-in-Decoder agrega múltiples pasajes y qué diferencia existe entre **retrieval quality**, **evidence aggregation** y **answer generation**.
4. Cómo Query2doc transforma/expande la consulta **antes** de recuperar y cómo un LLM puede por tanto influir en el ranking sin ser el generador final de respuesta.
5. Cómo Query Rewriting for Retrieval-Augmented LLMs modifica la consulta o interacción retriever–LLM y en qué etapa del pipeline opera realmente.
6. Qué define Asai et al. como `evidentiality`, cómo obtiene etiquetas gold/silver y cómo esa señal modifica el entrenamiento del generador.
7. Qué papers permiten inspeccionar documentos/pasajes recuperados y qué significa eso para provenance; qué **no** equivale a auditabilidad formal.
8. Qué resultados son de QA/fact verification/dialogue y por qué no se transfieren directamente a HS/NANDINA.
9. Qué diferencia existe entre:
   - retrieval que determina el contenido disponible al generador;
   - query transformation que modifica el retrieval;
   - evidence selection/evidentiality que guía generación;
   - post-ranking normative evidence usada solo para documentar candidatos fijos.
10. Por qué las arquitecturas fundacionales no equivalen automáticamente al contrato del piloto:

`ranking histórico Top-k fijado -> evidencia normativa posterior por candidato -> LLM local exclusivamente explicativo -> sin códigos nuevos -> sin reordenamiento -> sin feedback clasificatorio`.

### Regla crítica de procedencia

Usa obligatoriamente:

- `REPORTADO_POR_AUTORES`;
- `INFERENCIA_CRITICA`;
- `NO_VERIFICABLE_EN_PDF`;
- `SECONDARY_CLAIM_UNVERIFIED`.

Una afirmación que un paper atribuya a un tercero no se convierte en hecho independiente del artículo. Claims generales sobre hallucination, factuality, provenance, conocimiento paramétrico, actualidad, ventajas de retrieval, superioridad frente a otros sistemas o comportamiento de modelos citados deben mantenerse como `SECONDARY_CLAIM_UNVERIFIED` salvo que el propio paper los mida directamente.

### Distinciones metodológicas obligatorias

Mantén separadas estas categorías:

- `RETRIEVAL_AUGMENTED_GENERATION`;
- `RETRIEVAL_AUGMENTED_PRETRAINING`;
- `RETRIEVE_THEN_GENERATE`;
- `PARAMETRIC_MEMORY`;
- `NONPARAMETRIC_MEMORY`;
- `PASSAGE_FUSION`;
- `QUERY_EXPANSION`;
- `QUERY_REWRITING`;
- `RETRIEVER_READER_INTERACTION`;
- `EVIDENTIALITY_GUIDED_GENERATION`;
- `GENERATION_GROUNDING`;
- `PROVENANCE_SUPPORT`;
- `FORMAL_AUDITABILITY_EVALUATION`.

Reglas concretas:

- `RAG` no equivale a cualquier sistema que muestre documentos al LLM.
- Retrieval usado durante pretraining no equivale a retrieval ejecutado únicamente en inferencia.
- Query expansion/rewriting ocurre **antes o alrededor de retrieval** y puede modificar qué documentos se recuperan; no es explanation posterior.
- Un generador condicionado por pasajes recuperados puede producir contenido nuevo; no implica un output space cerrado ni un Top-k de códigos inmutable.
- Un paper que recupera evidencia para responder no implementa por ello `normative evidence after fixed ranking`.
- `provenance`, `inspectable retrieved passages`, `evidence`, `grounding`, `factuality`, `evidentiality` y `auditability` no son sinónimos.
- `evidentiality-positive passage` bajo una tarea NLP no equivale a validez jurídica/normativa de evidencia aduanera.
- Que un pasaje contenga el answer string no demuestra que sea evidencia correcta; verifica cómo lo trata cada paper.
- Que retrieval mejore exact match, F1 u otra métrica no demuestra que toda salida esté sustentada por evidencia.
- Los resultados de NQ, TriviaQA, FEVER, Wizard of Wikipedia, MS MARCO u otros benchmarks no son métricas de clasificación HS.
- No convertir frases como `more factual`, `less hallucination`, `provenance` o `state of the art` en garantías universales.

### Verificaciones específicas por paper

#### P01 — Lewis et al., RAG

Verifica:

- definición de memoria paramétrica y no paramétrica;
- retriever y generador utilizados;
- RAG-Sequence vs RAG-Token;
- qué se marginaliza y cuándo puede cambiar el documento condicionado durante generación;
- qué métricas/tareas se evalúan;
- si provenance se operacionaliza o solo se presenta como ventaja/posibilidad de inspección;
- qué claims de factuality están directamente medidos y contra qué baseline.

No describas RAG como un `fixed-candidate explainer` salvo que el PDF lo soporte, lo cual deberá comprobarse explícitamente.

#### P02 — REALM

Verifica:

- retrieval como variable latente durante pretraining;
- qué se entrena conjuntamente;
- cómo se actualizan o indexan representaciones documentales y cualquier mecanismo de MIPS/staleness;
- qué cambia en fine-tuning;
- qué tareas/resultados son realmente del paper;
- diferencia entre `retrieval-augmented pretraining` y retrieve-then-generate en inferencia.

No etiquetes REALM automáticamente como generador seq2seq si el PDF no lo define así.

#### P03 — Fusion-in-Decoder / Izacard & Grave

Verifica:

- retrievers usados y si el reader/generator cambia el ranking;
- procesamiento independiente de pasajes en encoder y fusión en decoder;
- número de pasajes evaluado y efecto sobre EM solo dentro del benchmark;
- diferencia entre disponibilidad de evidencia y evidence attribution;
- si el modelo produce citas/provenance por respuesta o simplemente consume pasajes.

#### P04 — Query2doc

Verifica:

- pseudo-document generation por LLM;
- cómo se concatena/transforma la query para sparse vs dense retrieval;
- qué modelos y datasets se evalúan;
- resultados positivos y negativos/out-of-domain;
- latencia/coste si está directamente medido;
- riesgos reconocidos de false claims en pseudo-documents.

No describas Query2doc como RAG de generación final: su LLM opera en **query expansion antes del retrieval**.

#### P05 — Query Rewriting for Retrieval-Augmented Large Language Models

Verifica:

- arquitectura exacta de rewriter, retriever y frozen LLM/reader;
- señal/objetivo de entrenamiento del rewriter;
- si se usa feedback del LLM y de qué forma;
- qué se congela y qué se entrena;
- si la query reescrita cambia directamente los documentos recuperados;
- benchmarks y métricas exactos;
- claims de hallucination/factuality que sean secundarios.

No equipares query rewriting con post-retrieval explanation.

#### P06 — Evidentiality-guided Generation

Verifica:

- definición operacional de `evidentiality`;
- generator base y retriever usados;
- multi-task objective;
- cómo se obtienen labels gold/silver;
- función de leave-one-out generation;
- human evaluation de la labeling model y su denominador/protocolo;
- diferencia entre `correct evidence for the output` y simple presence of answer string;
- si hay evaluación separada de auditability/provenance o solo evidentiality/generation quality.

No traduzcas evidentiality como demostración de corrección jurídica.

### Relación con F1–F5

0B-04B es principalmente fundacional. **No** debe utilizar estos papers para afirmar que un gap aduanero existe o no existe en toda la literatura.

Usa solo estas etiquetas:

- `METHOD_FOUNDATION_RELEVANT`;
- `METHOD_CONTRAST_RELEVANT`;
- `METHOD_BOUNDARY_RELEVANT`;
- `NOT_RELEVANT_TO_GAP_CANDIDATE`.

Evalúa especialmente:

- **F1:** distinguir retrieval que determina contenido/candidatos de normativa posterior que no reordena un ranking histórico ya fijado.
- **F2:** distinguir generation condicionada por retrieval de un explainer contractual sobre Top-k externo e inmutable.
- **F4:** distinguir answer/retrieval/factuality/evidentiality metrics de correctness sustantiva/jurídica adjudicada.
- **F5:** distinguir evidence/provenance/evidentiality de una evaluación formal y separada de auditabilidad documental por salida.

F3 puede marcarse `NOT_RELEVANT_TO_GAP_CANDIDATE` salvo que un paper contenga una estructura de observaciones correlacionadas realmente pertinente.

**G6 permanece eliminado y G7 permanece absorbido en F2; no se reabren.**

### Marco obligatorio por paper

Extrae únicamente lo soportado por el PDF:

- identificación bibliográfica, versión y tipo documental visible;
- tarea exacta;
- dataset/corpus y unidad de recuperación;
- retriever, índice y representación;
- momento del retrieval: pretraining, fine-tuning, inference;
- query original vs query transformada;
- Top-k/Top-N y si queda fijo o cambia durante generación;
- generador/reader y arquitectura;
- mecanismo de fusión/marginalización/conditioning;
- si retrieval modifica directamente la salida o solo proporciona contexto;
- si el generador puede producir contenido fuera de los pasajes/candidatos;
- evidence/evidentiality/provenance/grounding y cómo se operacionalizan;
- supervisión y etiquetas;
- métricas y denominadores;
- resultados principales y baselines;
- limitaciones reconocidas por autores;
- limitaciones adicionales como `INFERENCIA_CRITICA`;
- claims secundarios pendientes de fuente primaria;
- transferibilidad limitada al presente proyecto.

### Formato obligatorio de salida

#### A. Control de integridad
`ID | archivo | lectura completa sí/no | metadata suficiente sí/no | tipo documental visible | observaciones`.

#### B. Matriz funcional RAG/generación
Una fila por paper con:
`paper | tarea | retrieval timing | query transformation | retriever | Top-k | generator/reader | fusion/conditioning | evidence/evidentiality | provenance | métricas | resultado | límite | función`.

#### C. Fichas individuales
Una por paper usando obligatoriamente las cuatro etiquetas de procedencia.

#### D. Taxonomía metodológica
Clasifica cada paper con las categorías definidas arriba y explica solapamientos sin forzar una sola etiqueta.

#### E. Mapa de pipeline por paper
Representa el flujo real, por ejemplo:

`QUERY -> [TRANSFORMATION?] -> RETRIEVAL -> [FUSION/SELECTION?] -> GENERATION -> OUTPUT`

Incluye pretraining cuando corresponda y marca qué componentes están entrenados/congelados.

#### F. Relación metodológica con F1–F5
`paper | F1 | F2 | F3 | F4 | F5 | justificación` usando solo las etiquetas metodológicas autorizadas.

#### G. Claims metodológicos autorizables
Propón formulaciones precisas potencialmente utilizables después en Methods/Related Work, cada una con fuente y límite explícito. **No redactes todavía el manuscrito.**

#### H. Claims prohibidos o excesivos
Lista cerrada de formulaciones que estos seis papers no autorizan.

#### I. Claims secundarios e inconsistencias pendientes
Incluye:
`paper | claim/inconsistencia | estado | acción futura necesaria`.

#### J. Recomendación bibliográfica
`paper | función científica | uso potencial | recomendación | justificación`.

Usa cuando corresponda:
- `KEEP_CORE_METHOD`;
- `KEEP_SUPPORTING_METHOD`;
- `REVIEW_REQUIRED`;
- `EXCLUDE_FROM_ARTICLE`.

Esto no obliga a citar el paper final.

#### K. Dictamen
`PASS`, `PASS WITH CORRECTIONS` o `BLOCKED`.

### Prohibiciones

- No web.
- No literatura nueva.
- No utilizar otros PDF del corpus.
- No redactar Introduction, Related Work, Methods, Results, Discussion ni Conclusions.
- No declarar novelty, gap definitivo ni superioridad universal.
- No afirmar que RAG elimina hallucinations o garantiza factuality.
- No equiparar evidentiality/provenance con auditabilidad o legal correctness.
- No modificar GitHub.
- No modificar el Plan Maestro ni los freezes 0A/0B previos.
- No reinterpretar resultados experimentales congelados.
- No reabrir G6/G7.
- No avanzar a 0B-05, 0B-06, 0C ni fases posteriores.

### Idioma y gate

Responde únicamente en español. Detente al finalizar 0B-04B y devuelve la entrega al editor científico para revisión interna.

---

## English

### Role and scope

Act as the drafting/bibliographic-analysis AI for `0B-04B — RAG, query-transformation, and grounding foundations`. This is a methodological foundation block, not a novelty or customs-gap search. Analyze only the six assigned inherited PDFs and do not use web, add literature, draft manuscript sections, modify GitHub/Master Plan, reinterpret frozen experiments, reopen G6/G7, or advance further.

### Assigned works

The batch consists of the six works listed in the Spanish section: Lewis et al. RAG, REALM, Fusion-in-Decoder, Query2doc, Query Rewriting for Retrieval-Augmented Large Language Models, and Evidentiality-guided Generation.

### Governing distinctions

Differentiate retrieval-augmented generation from retrieval-augmented pretraining; retrieve-then-generate from query expansion/rewriting; query transformation before retrieval from post-ranking explanation; passage fusion from evidence attribution; inspectable retrieved passages/provenance from formal auditability; and evidentiality/grounding from substantive or legal correctness.

The present pilot's contract remains distinct unless primary evidence shows otherwise: an externally fixed historical ranked Top-k is followed by candidate-specific normative evidence and an explanation-only local LLM that cannot add/delete/substitute/reorder codes or feed back into classification.

### Provenance and candidate-gap governance

Use `REPORTADO_POR_AUTORES`, `INFERENCIA_CRITICA`, `NO_VERIFICABLE_EN_PDF`, and `SECONDARY_CLAIM_UNVERIFIED`. For F1–F5 use only methodological relevance labels; foundational papers are not proof of missing customs prior art. G6 stays eliminated and G7 stays merged into F2.

### Output and gate

Produce sections A–K exactly as specified in the Spanish instructions. Respond only in Spanish, stop after 0B-04B, and return the deliverable for internal scientific/editorial review.