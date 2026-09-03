# Revisión interna 0B-04B / 0B-04B Internal Review

## Español

### 1. Identificación

- Bloque: `0B-04B — Fundamentos de RAG, transformación de consultas y grounding`.
- Tipo de revisión: científica/editorial interna con verificación independiente de claims contra los seis PDF primarios asignados.
- Entrega revisada: análisis A–K producido por la IA de redacción.
- Estado previo: `READY_FOR_DRAFTING`.
- Dictamen interno: **`PASS WITH MINOR CORRECTIONS`**.
- Errores materiales detectados: **`0`**.
- Reejecución completa por la IA de redacción: **`NOT_REQUIRED`**.
- Revisión experimental: **`NOT_REQUIRED`**.
- Aprobación del autor: **`PENDING`**.
- Freeze: **`NOT_YET_AUTHORIZED`**.
- 0B-05: **`NOT_STARTED / CLOSED_BY_GATE`**.

### 2. Resultado general

La entrega cumple el objetivo metodológico de 0B-04B. La revisión independiente confirma que los seis trabajos fueron interpretados en su función causal correcta dentro de sus respectivos pipelines y que la entrega evita los errores de categoría que este bloque debía impedir.

Quedan verificadas las siguientes fronteras principales:

- Lewis et al. combinan memoria paramétrica seq2seq y memoria no paramétrica recuperada mediante un retriever denso; la recuperación condiciona directamente la generación y el output sigue siendo abierto.
- REALM incorpora un retriever latente al preentrenamiento y reutiliza retrieval en fine-tuning e inferencia; su Open-QA fine-tuning predice spans de respuesta y no debe equipararse a un generador seq2seq RAG de Lewis et al.
- Fusion-in-Decoder recupera primero y luego codifica pasajes por separado y los fusiona en el decoder; passage fusion no equivale a atribución de evidencia.
- Query2doc usa un LLM upstream para producir un pseudo-documento que expande la consulta antes del retrieval; el pseudo-documento no es evidencia documental.
- Rewrite-Retrieve-Read inserta un rewriter antes del retriever; al cambiar la consulta puede cambiar los documentos recuperados y, por esa vía, el output del reader.
- Asai et al. introducen supervisión auxiliar de evidentiality respecto del gold output de la tarea; dicha evidentiality no es una barrera lógica de generación, no es provenance formal y no constituye suficiencia normativa/jurídica.

La separación metodológica central es, por tanto, congelable después de aprobación del autor:

`RAG ≠ RETRIEVAL_AUGMENTED_PRETRAINING ≠ RETRIEVE_THEN_GENERATE ≠ QUERY_EXPANSION ≠ QUERY_REWRITING ≠ PASSAGE_FUSION ≠ EVIDENTIALITY_GUIDED_GENERATION`.

Y, de forma adicional:

`RETRIEVED PASSAGE ≠ EVIDENCE ATTRIBUTION ≠ EVIDENTIALITY ≠ GROUNDING GUARANTEE ≠ PROVENANCE VERIFICATION ≠ FORMAL AUDITABILITY ≠ LEGAL CORRECTNESS`.

### 3. Correcciones y normalizaciones obligatorias para el freeze

#### C1 — Lewis et al.: discrepancia interna 17% vs 11.7%

El texto narrativo de la sección de Jeopardy afirma que ambos sistemas fueron factuales en un `17%` adicional, mientras que la Tabla 4 reporta `Both good = 11.7%`. El freeze debe preservar la inconsistencia y, si se utiliza el valor cuantitativo, gobernar por **11.7% de la tabla**.

La evaluación humana fue realizada sobre **452 pares** de generaciones y es específica de Jeopardy question generation. No debe convertirse en una tasa universal de reducción de hallucination ni en prueba de grounding duro.

#### C2 — Lewis et al.: retrieval-conditioned generation ≠ hard grounding

RAG-Sequence marginaliza a nivel de secuencia y RAG-Token a nivel de token sobre el Top-k recuperado para la misma consulta; RAG-Token no ejecuta un nuevo retrieval por cada token.

Además, el propio análisis del paper muestra que la memoria paramétrica puede completar contenido después de que el contexto recuperado haya guiado la generación. En consecuencia, la formulación segura es `retrieval-conditioned generation`, no `output restricted to retrieved evidence`.

La inspeccionabilidad de documentos y el overlap con gold articles en FEVER aportan `PROVENANCE_SUPPORT`, no una evaluación formal de auditabilidad ni citation completeness.

#### C3 — REALM: pretraining aumentado por retrieval, no seq2seq RAG

REALM debe conservarse como `RETRIEVAL_AUGMENTED_PRETRAINING / RETRIEVE_THEN_PREDICT`. El retrieval participa durante pretraining, fine-tuning e inference. En el régimen de Open-QA, el fine-tuning modela posiciones de inicio/fin de un answer span; no es un BART/T5 free-form seq2seq generator equivalente a Lewis et al.

La ablation `30× stale MIPS` está correctamente delimitada al régimen de entrenamiento de REALM: `Exact Match 38.2 -> 28.7` y `zero-shot retrieval Recall@5 38.5 -> 15.1`. No se generaliza como requisito universal de refresh para cualquier índice vectorial.

`Grounded neural memory` significa aquí memoria explícitamente asociada a documentos recuperables/identificables; no significa provenance certificada, citation generation ni formal auditability.

#### C4 — Fusion-in-Decoder: fusion ≠ attribution

FiD codifica cada `question + passage` independientemente y concatena las representaciones para que el decoder atienda conjuntamente sobre ellas. El modelo consume múltiples pasajes, pero no produce por respuesta una atribución passage→claim, una cita obligatoria ni una medida separada de suficiencia evidencial.

Los resultados `FiD-large: NQ 51.4 EM; TriviaQA open 67.6 EM; hidden 80.1 EM; SQuAD Open 56.7 EM / 63.2 F1` están verificados en la tabla del PDF y siguen siendo específicos de esos benchmarks.

El aumento de 10 a 100 pasajes produjo aproximadamente `+3.5` puntos EM en Natural Questions y `+6` en TriviaQA en el análisis del paper. Debe presentarse exclusivamente como comportamiento observado en ese rango/configuración, no como ley general de que más pasajes siempre mejoran el output.

#### C5 — Query2doc: pseudo-documento upstream ≠ evidencia

Query2doc genera un pseudo-documento con LLM y lo incorpora a la consulta antes del retrieval. En sparse retrieval repite la query original y concatena el pseudo-documento; en dense retrieval concatena `q [SEP] pseudo-document`.

La entrega acierta al tratar el pseudo-documento como **artefacto de query expansion**, no como evidencia factual ni provenance. El propio paper documenta que los pseudo-documentos pueden contener false claims.

Los resultados OOD son explícitamente mixtos. Deben preservarse los contraejemplos, entre ellos SimLM en NFCorpus `32.7 -> 32.1`, SimLM en SciFact `62.4 -> 59.5` y E5 en SciFact `70.4 -> 67.5`.

#### C6 — Query2doc: normalización de incrementos y latencia

La Tabla 1 reporta, por ejemplo, BM25 `MRR@10 18.4 -> 21.4`, `TREC DL19 nDCG@10 51.2 -> 66.2` y `TREC DL20 47.7 -> 62.9`, mientras el abstract usa lenguaje de mejoras `3%–15%`.

Para evitar ambigüedad, el freeze debe priorizar valores inicial/final o cambios en **puntos de la métrica** cuando se derive directamente de la tabla, sin reinterpretar automáticamente los deltas impresos `+3.0`, `+15.0`, etc. como porcentajes relativos.

La latencia reportada (`BM25 index search 16 ms`; `Query2doc LLM call >2000 ms` y `index search 177 ms`) queda restringida a la configuración medida y conserva el caveat explícito de carga del servidor/API.

#### C7 — Query Rewriting: rewriter upstream y efecto causal sobre retrieval

Rewrite-Retrieve-Read debe conservarse como `QUERY_REWRITING / RETRIEVER_READER_INTERACTION`. En la variante entrenable, T5-large actúa como rewriter, mientras retriever y reader permanecen congelados; el rewriter se ajusta con warm-up y reinforcement learning usando feedback del output del reader.

La consulta reescrita determina qué contexto recupera el search engine. Por ello query rewriting puede modificar retrieval y downstream answer; no es explanation posterior.

Los resultados propios verifican además contraejemplos a una lectura universal de retrieval augmentation: en HotpotQA `Direct 32.36/43.05` frente a `Retrieve-then-read 30.47/41.34`, mientras el trainable rewriter alcanza `34.38/45.97`. En MMLU con ChatGPT, el rewriter no mejora la categoría Social Sciences respecto de retrieve-then-read (`76.4` frente a `78.2`).

Los claims introductorios sobre alleviating hallucination/factuality dependen de literatura citada; el experimento propio mide EM/F1/Hit y no una tasa directa de hallucination. Permanecen `SECONDARY_CLAIM_UNVERIFIED` para ese propósito.

#### C8 — Evidentiality: definición task-relative y labels model-dependent

Asai et al. definen evidentiality respecto de si un pasaje contiene evidencia correcta para respaldar el **gold output de la tarea**, incluso cuando un pasaje negativo pueda contener el answer string.

El labeling model utiliza parcialmente gold annotations y ejemplos obtenidos mediante leave-one-out generation; estos últimos dependen del comportamiento de un base generator y los propios autores reconocen que pueden perder evidencia cuando existen pasajes redundantes o la respuesta está memorizada. Por ello `mined gold` no debe reinterpretarse como adjudicación humana independiente universal.

La señal de evidentiality entra como objetivo auxiliar de multi-task learning; no constituye un filtro duro que impida la generación desde otras señales.

#### C9 — Evidentiality: cinco datasets, no seis

El abstract y las cinco filas de la Tabla 1 identifican **cinco datasets**:

1. Natural Questions Open;
2. TriviaQA unfiltered;
3. FEVER;
4. FaVIQ-Ambig;
5. Wizard of Wikipedia.

El caption de la Tabla 1 dice erróneamente `across six datasets`. El freeze debe registrar esta inconsistencia editorial y gobernar por **cinco datasets**.

#### C10 — Evidentiality: human evaluation 95%/96% no es auditability score

La evaluación humana de labels muestrea 50 preguntas de Natural Questions development y, cuando aplica, dos pasajes positivos y dos negativos con answer string por pregunta. La Tabla 4a y el texto reportan:

- positivos predichos correctamente: **95%**;
- negativos predichos correctamente: **96%**.

El `95% accuracy` resumido en el abstract no debe trasladarse como accuracy global del generador, score global de evidencia, provenance accuracy, formal auditability ni legal correctness.

#### C11 — Provenance, grounding, evidentiality y auditability permanecen separados

Los seis papers permiten establecer soporte de procedencia o evidencia en sentidos distintos, pero ninguno evalúa el contrato de auditabilidad documental del piloto. En particular:

- documentos inspeccionables no implican source-to-claim alignment completo;
- passage fusion no implica attribution;
- evidentiality positiva no implica suficiencia normativa;
- retrieval-conditioned generation no implica grounding garantizado;
- un Top-k de pasajes no equivale a un Top-k externo de códigos inmutable.

#### C12 — Protección de transferencia y claims HS/NANDINA

Los resultados cuantitativos de NQ, TriviaQA, FEVER, FaVIQ-A, Wizard of Wikipedia, MS MARCO, TREC DL, HotpotQA, AmbigNQ, PopQA y MMLU no son métricas de clasificación HS/NANDINA ni de corrección normativa aduanera. Se utilizarán solo como evidencia del comportamiento de las arquitecturas en sus tareas originales.

#### C13 — F1–F5: solo frontera metodológica

0B-04B no cambia el estado bibliográfico de F1–F5 establecido tras los lotes aduaneros. Solo aporta fundamento para precisar:

- F1: retrieval que determina contenido/candidatos ≠ evidencia normativa posterior a ranking histórico ya fijado;
- F2: generation abierta condicionada por retrieval y query transformation ≠ explainer contractual sobre Top-k externo e inmutable;
- F4: retrieval/EM/F1/factuality/evidentiality ≠ corrección sustantiva o jurídica adjudicada;
- F5: evidence/provenance/evidentiality ≠ evaluación formal y separada de auditabilidad por salida.

F3 permanece `NOT_RELEVANT_TO_GAP_CANDIDATE` para este lote. G6 no se reabre y G7 permanece absorbido en F2.

### 4. Taxonomía metodológica gobernante

Taxonomía congelable después de aprobación del autor:

- Lewis et al.: `RETRIEVAL_AUGMENTED_GENERATION / PARAMETRIC_MEMORY / NONPARAMETRIC_MEMORY / RETRIEVAL_CONDITIONED_GENERATION / PROVENANCE_SUPPORT`.
- REALM: `RETRIEVAL_AUGMENTED_PRETRAINING / LATENT_RETRIEVAL / RETRIEVE_THEN_PREDICT / DOCUMENT_ADDRESSABLE_MEMORY`.
- Izacard & Grave: `RETRIEVE_THEN_GENERATE / PASSAGE_FUSION`.
- Query2doc: `QUERY_EXPANSION / LLM_UPSTREAM_OF_RETRIEVAL`.
- Ma et al.: `QUERY_REWRITING / RETRIEVER_READER_INTERACTION`.
- Asai et al.: `EVIDENTIALITY_GUIDED_GENERATION / PASSAGE_EVIDENTIALITY_SUPERVISION / RETRIEVE_THEN_GENERATE`.

Esta taxonomía describe funciones y admite solapamientos; no fuerza a cada sistema dentro de una sola etiqueta.

### 5. Función bibliográfica provisional

Los seis trabajos pueden conservar `KEEP_CORE_METHOD` dentro del mapa metodológico 0B-04B. La etiqueta expresa función bibliográfica, no obligación de citarlos todos en el manuscrito final.

La metadata visible de las copias analizadas debe conservarse sin reconstrucciones silenciosas: Lewis et al. y REALM tienen venue visible; FiD, Query2doc, Query Rewriting y la copia suministrada de Evidentiality muestran versiones arXiv/preprint. Si en la fase final se desea citar una versión editorial diferente, deberá verificarse expresamente bajo las reglas del marco bibliográfico.

### 6. Revisión experimental

**`NOT_REQUIRED`**.

La presente revisión no modifica hechos, métricas, claims experimentales ni restricciones congeladas del proyecto. Únicamente fija fronteras metodológicas de la literatura. El Plan Maestro permanece intocado y bajo autoridad exclusiva de la IA experimental.

### 7. Dictamen y gate

**`0B-04B INTERNAL REVIEW = PASS WITH MINOR CORRECTIONS`**.

No se requiere una nueva ejecución completa de la IA de redacción. Las correcciones C1–C13 son normalizaciones deterministas de alcance, taxonomía y protección contra overclaiming que pueden incorporarse editorialmente al artefacto congelado después de aprobación expresa del autor.

Siguiente estado permitido:

`INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING`.

Hasta aprobación expresa del autor:

- no crear el freeze canónico de 0B-04B;
- no declarar 0B-04B `APPROVED / FROZEN`;
- no abrir 0B-05;
- no abrir 0B-06 ni 0C;
- no redactar secciones del manuscrito;
- no modificar el Plan Maestro.

---

## English

### 1. Identification

- Block: `0B-04B — RAG, query-transformation, and grounding foundations`.
- Review type: internal scientific/editorial review with independent claim-level verification against the six assigned primary PDFs.
- Internal verdict: **`PASS WITH MINOR CORRECTIONS`**.
- Material errors: **`0`**.
- Full drafting-AI rerun: **`NOT_REQUIRED`**.
- Experimental review: **`NOT_REQUIRED`**.
- Author approval: **`PENDING`**.
- Freeze: **`NOT_YET_AUTHORIZED`**.
- 0B-05: **`NOT_STARTED / CLOSED_BY_GATE`**.

### 2. Overall assessment

The deliverable fulfills 0B-04B. Independent primary-PDF verification confirms the core functional distinctions: Lewis et al. couple parametric and non-parametric memory in retrieval-conditioned generation; REALM augments pretraining with latent retrieval and uses span-based Open-QA fine-tuning; Fusion-in-Decoder performs retrieve-then-generate passage fusion; Query2doc expands the query upstream of retrieval; Rewrite-Retrieve-Read rewrites the query before a frozen retriever/reader pipeline; and Asai et al. use task-relative passage-evidentiality supervision rather than a hard grounding or auditability mechanism.

The methodological map eligible for freezing after author approval is:

`RAG ≠ RETRIEVAL_AUGMENTED_PRETRAINING ≠ RETRIEVE_THEN_GENERATE ≠ QUERY_EXPANSION ≠ QUERY_REWRITING ≠ PASSAGE_FUSION ≠ EVIDENTIALITY_GUIDED_GENERATION`.

Also:

`RETRIEVED PASSAGE ≠ EVIDENCE ATTRIBUTION ≠ EVIDENTIALITY ≠ GROUNDING GUARANTEE ≠ PROVENANCE VERIFICATION ≠ FORMAL AUDITABILITY ≠ LEGAL CORRECTNESS`.

### 3. Required corrections for freeze

**C1 — RAG factuality inconsistency.** The Jeopardy prose says both systems were factual in a further `17%`, whereas Table 4 reports `Both good = 11.7%`. Preserve the inconsistency and govern quantitative use by the table. The human comparison covers 452 generation pairs and is task-specific, not a universal hallucination rate.

**C2 — RAG is not hard grounding.** RAG-Sequence marginalizes documents at sequence level; RAG-Token marginalizes over the same retrieved Top-k at token level rather than issuing a new retrieval for each token. Parametric memory can complete content, so retrieval conditioning does not constrain all output to retrieved text. Inspectable documents/evidence overlap provide provenance support, not formal auditability.

**C3 — REALM.** Keep `RETRIEVAL_AUGMENTED_PRETRAINING / RETRIEVE_THEN_PREDICT`. Retrieval is used in pretraining, fine-tuning, and inference; Open-QA fine-tuning predicts answer spans rather than acting as a free-form seq2seq RAG generator. The `30× stale MIPS` ablation is specific to REALM's training regime. Document-addressable memory is not certified provenance or auditability.

**C4 — Fusion-in-Decoder.** Independently encoded query-passage representations are concatenated and fused by decoder attention, but this does not produce passage-to-claim attribution. Verified FiD-large benchmark values remain task-specific. The observed gain from 10 to 100 passages is bounded to that tested range/configuration and cannot support a universal more-passages-is-better rule.

**C5 — Query2doc.** The LLM creates an upstream pseudo-document used for query expansion; that pseudo-document is not evidence or provenance. Preserve mixed OOD results and the paper's own false-claim risk.

**C6 — Query2doc deltas/latency.** Prefer initial/final metric values or explicit metric-point changes instead of automatically converting printed `+3.0`, `+15.0`, etc. into relative percentages. Latency figures remain configuration-specific and retain the API/server-load caveat.

**C7 — Query Rewriting.** The rewriter changes the search query and therefore retrieved context and potentially the reader output; it is not post-retrieval explanation. HotpotQA provides a direct counterexample where standard retrieve-then-read hurts relative to Direct, while rewriting recovers/improves performance. With ChatGPT on MMLU, Social Sciences is also a counterexample to universal rewriting improvement. Hallucination-alleviation claims are secondary to cited literature because the paper's own metrics are EM/F1/Hit rather than a hallucination rate.

**C8 — Evidentiality.** Evidentiality is defined relative to support for the task's gold output. Silver/mined labels partly depend on a base generator and leave-one-out behavior, with acknowledged failure modes under redundant evidence or memorized answers. The auxiliary objective guides learning but is not a hard evidence filter.

**C9 — Dataset-count inconsistency.** The abstract and table rows identify five datasets, while Table 1's caption says six. Govern by five and preserve the editorial inconsistency.

**C10 — Human evidentiality check.** The protocol samples 50 NQ development questions and positive/negative passages with answer strings; reported correctness is 95% for positive labels and 96% for negative labels. This is not a generator accuracy, global evidence score, auditability score, provenance accuracy, or legal-correctness result.

**C11 — Provenance/grounding/auditability.** Inspectable retrieval, passage fusion, task evidentiality, and retrieval-conditioned generation remain distinct from source-to-claim alignment, formal auditability, and legal/normative sufficiency.

**C12 — Transfer boundary.** QA, fact-verification, dialogue, and IR benchmark scores are not HS/NANDINA classification or customs-correctness metrics and may only support methodological behavior within the original tasks.

**C13 — F1–F5.** This batch supplies methodological foundations only. It does not change the customs-prior-art status of F1–F5, does not reopen G6, and leaves G7 merged into F2.

### 4. Governing taxonomy

After author approval, the taxonomy may freeze as: Lewis et al. = retrieval-augmented generation with parametric/non-parametric memory; REALM = retrieval-augmented pretraining / latent retrieve-then-predict; FiD = retrieve-then-generate passage fusion; Query2doc = upstream LLM query expansion; Ma et al. = query rewriting and retriever-reader interaction; Asai et al. = evidentiality-guided generation and passage-evidentiality supervision.

### 5. Bibliographic function and metadata

All six works may remain `KEEP_CORE_METHOD`. This is a methodological-map label rather than a requirement to cite all six in the final manuscript. Visible version/venue metadata from the supplied primary copies must be preserved; any later substitution with a different published version requires explicit verification under the bibliographic framework.

### 6. Experimental review and gate

Experimental-AI review is **not required** because no frozen experimental fact, metric, claim, restriction, or Master-Plan content is changed.

**`0B-04B INTERNAL REVIEW = PASS WITH MINOR CORRECTIONS`**. No full drafting-AI rerun is required. The next allowed state is `INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING`. Until express author approval, 0B-04B must not be frozen and 0B-05, 0B-06, 0C, and manuscript drafting remain closed.