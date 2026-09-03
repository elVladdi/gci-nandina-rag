# 0B-04B — Fundamentos de RAG, transformación de consultas y grounding / RAG, query-transformation, and grounding foundations

## Español

### 1. Estado

- Bloque: `0B-04B — Fundamentos de RAG, transformación de consultas y grounding`.
- Estado: **`APPROVED / FROZEN`**.
- Entrega inicial: análisis metodológico A–K de seis PDF primarios por la IA de redacción.
- Revisión científica/editorial interna: **`PASS WITH MINOR CORRECTIONS`**.
- Errores materiales detectados: `0`.
- Aprobación expresa del autor: recibida el `2026-09-03`.
- Revisión experimental: `NOT_REQUIRED`.
- Novelty: `NOT_DECLARED`.
- Gap definitivo: `NOT_DEFINED`.
- Manuscrito: `NOT_DRAFTED`.

Registros gobernantes:

- `article/prompts/0B04B_RAG_QUERY_TRANSFORMATION_GROUNDING_FOUNDATIONS.md`;
- `article/reviews/0B04B_INTERNAL_REVIEW.md`;
- `article/reviews/0B04B_AUTHOR_APPROVAL.md`.

Este artefacto congela el mapa metodológico canónico de 0B-04B. `KEEP_CORE_METHOD` expresa función bibliográfica dentro del mapa y no obligación de cita final.

### 2. Corpus congelado

1. `Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.pdf`
2. `REALM-Retrieval-Augmented Language Model Pre-Training.pdf`
3. `Leveraging passage retrieval with generative models for open domain question answering.pdf`
4. `Query2doc-Query Expansion whit Large Lenguage Models.pdf`
5. `Query Rewriting for Retrieval-Augmented Large Language Models.pdf`
6. `Evidentiality-guided Generation for Knowledge-Intensive NLP Tasks.pdf`

Los seis se trataron como fuentes primarias del sub-lote. Los demás documentos del corpus quedaron fuera de alcance.

### 3. Distinciones metodológicas congeladas

La taxonomía gobernante es:

`RAG ≠ RETRIEVAL_AUGMENTED_PRETRAINING ≠ RETRIEVE_THEN_GENERATE ≠ QUERY_EXPANSION ≠ QUERY_REWRITING ≠ PASSAGE_FUSION ≠ EVIDENTIALITY_GUIDED_GENERATION`.

Y, para evidencia/procedencia/auditabilidad:

`RETRIEVED PASSAGE ≠ EVIDENCE ATTRIBUTION ≠ EVIDENTIALITY ≠ GROUNDING GUARANTEE ≠ PROVENANCE VERIFICATION ≠ FORMAL AUDITABILITY ≠ LEGAL CORRECTNESS`.

Pipeline metodológico general de contraste:

`QUERY -> [QUERY TRANSFORMATION?] -> RETRIEVAL -> [FUSION / EVIDENCE SELECTION?] -> GENERATION -> OUTPUT`.

Estas funciones pueden estar operacionalmente acopladas, pero no son sinónimos.

### 4. Taxonomía por paper

- Lewis et al.: `RETRIEVAL_AUGMENTED_GENERATION / PARAMETRIC_MEMORY / NONPARAMETRIC_MEMORY / RETRIEVAL_CONDITIONED_GENERATION / PROVENANCE_SUPPORT`.
- Guu et al. (REALM): `RETRIEVAL_AUGMENTED_PRETRAINING / LATENT_RETRIEVAL / RETRIEVE_THEN_PREDICT / DOCUMENT_ADDRESSABLE_MEMORY`.
- Izacard & Grave: `RETRIEVE_THEN_GENERATE / PASSAGE_FUSION`.
- Query2doc: `QUERY_EXPANSION / LLM_UPSTREAM_OF_RETRIEVAL`.
- Ma et al.: `QUERY_REWRITING / RETRIEVER_READER_INTERACTION`.
- Asai et al.: `EVIDENTIALITY_GUIDED_GENERATION / PASSAGE_EVIDENTIALITY_SUPERVISION / RETRIEVE_THEN_GENERATE`.

### 5. Normalizaciones C1–C13 integradas

#### C1 — Lewis et al.: 17% vs 11.7%

La prosa de Jeopardy menciona `17%`, pero la Tabla 4 reporta `Both good = 11.7%`. La inconsistencia se conserva y, si se usa el valor cuantitativo, gobierna **11.7%**. La evaluación humana cubre 452 pares y no es una tasa universal de reducción de hallucination.

#### C2 — RAG: retrieval-conditioned generation ≠ hard grounding

RAG-Sequence marginaliza documentos a nivel de secuencia; RAG-Token lo hace a nivel de token sobre el Top-k recuperado para la misma consulta. RAG-Token no ejecuta un retrieval nuevo por token. El generador sigue siendo abierto y puede apoyarse en memoria paramétrica; por ello `retrieval-conditioned generation` no equivale a output restringido a evidencia recuperada.

Los documentos inspeccionables y el overlap con gold articles aportan `PROVENANCE_SUPPORT`, no citation completeness ni formal auditability.

#### C3 — REALM

REALM queda congelado como `RETRIEVAL_AUGMENTED_PRETRAINING / RETRIEVE_THEN_PREDICT`. Retrieval participa durante pretraining, fine-tuning e inference. En Open-QA predice answer spans, no una salida seq2seq libre equivalente al RAG de Lewis et al.

La ablation `30× stale MIPS` (`EM 38.2 -> 28.7`; zero-shot retrieval `Recall@5 38.5 -> 15.1`) queda restringida al régimen de entrenamiento de REALM. `Grounded neural memory` significa memoria asociada a documentos identificables, no provenance certificada ni auditability formal.

#### C4 — Fusion-in-Decoder

FiD codifica `question + passage` por separado y concatena las representaciones para que el decoder las fusione. `PASSAGE_FUSION ≠ EVIDENCE_ATTRIBUTION`.

Los resultados verificados permanecen específicos de sus benchmarks: `FiD-large NQ 51.4 EM`, `TriviaQA open 67.6 EM`, `hidden 80.1 EM`, `SQuAD Open 56.7 EM / 63.2 F1`. El aumento observado entre 10 y 100 pasajes no se generaliza como regla universal de que más pasajes siempre mejoran.

#### C5 — Query2doc: pseudo-documento upstream

Query2doc usa un LLM antes del retrieval para generar un pseudo-documento que expande la consulta. El pseudo-documento es un artefacto de query expansion, no evidencia factual ni provenance. El paper documenta false claims y resultados OOD mixtos; se preservan los contraejemplos reportados.

#### C6 — Query2doc: deltas y latencia

Los resultados se expresan mediante valores inicial/final o puntos de la métrica cuando se deriven directamente de tablas; no se reinterpretan automáticamente deltas como porcentajes relativos. La latencia (`BM25 index search 16 ms`; `Query2doc LLM call >2000 ms`; `index search 177 ms`) queda limitada a la configuración evaluada y conserva el caveat de server/API load.

#### C7 — Query Rewriting

Rewrite-Retrieve-Read queda congelado como `QUERY_REWRITING / RETRIEVER_READER_INTERACTION`. En la variante entrenable, el rewriter T5 se ajusta mediante warm-up + reinforcement learning con feedback del reader, mientras retriever y reader permanecen congelados.

La query reescrita puede cambiar los documentos recuperados y el downstream output; por ello no es explanation posterior. Los contraejemplos del paper a beneficios universales de retrieval/rewriting se conservan. Los claims de hallucination/factuality no medidos directamente permanecen secundarios.

#### C8 — Evidentiality task-relative

En Asai et al., evidentiality expresa si un pasaje respalda el gold output de la tarea. Un pasaje puede contener el answer string y ser evidentiality-negative. Los labels combinan anotaciones disponibles con ejemplos minados mediante leave-one-out generation; estos últimos dependen parcialmente del generador base y no constituyen adjudicación humana independiente universal.

La señal de evidentiality es una supervisión auxiliar de multi-task learning, no un filtro duro que impida generar contenido desde otras señales.

#### C9 — Cinco datasets

Gobiernan cinco datasets: Natural Questions Open, TriviaQA unfiltered, FEVER, FaVIQ-Ambig y Wizard of Wikipedia. El caption `across six datasets` se registra como inconsistencia editorial.

#### C10 — 95%/96% no es auditability score

El chequeo humano de labels sobre 50 preguntas de NQ development reporta 95% para positivos y 96% para negativos bajo el protocolo descrito. No se interpreta como accuracy global del generador, provenance accuracy, formal auditability ni legal correctness.

#### C11 — Provenance, grounding, evidentiality y auditability

La inspectabilidad de pasajes, passage fusion, evidentiality o retrieval-conditioned generation pueden apoyar distintas formas de procedencia/soporte, pero no equivalen a source-to-claim alignment completo, suficiencia normativa, grounding garantizado ni evaluación formal de auditabilidad.

#### C12 — Límites de transferencia

Los resultados cuantitativos de NQ, TriviaQA, FEVER, FaVIQ-A, Wizard of Wikipedia, MS MARCO, TREC DL, HotpotQA, AmbigNQ, PopQA y MMLU se interpretan solo dentro de sus tareas originales. No son métricas de clasificación HS/NANDINA ni de corrección normativa aduanera.

#### C13 — Relación con F1–F5

0B-04B no modifica el estado bibliográfico de F1–F5. Solo aporta precisión metodológica:

- F1: retrieval que determina contenido/candidatos ≠ evidencia normativa posterior a un ranking histórico ya fijado.
- F2: generation abierta condicionada por retrieval y query transformation ≠ explainer contractual sobre Top-k externo e inmutable.
- F3: `NOT_RELEVANT_TO_GAP_CANDIDATE` en este lote.
- F4: retrieval/EM/F1/factuality/evidentiality ≠ corrección sustantiva/jurídica adjudicada.
- F5: evidence/provenance/evidentiality ≠ evaluación formal y separada de auditabilidad por salida.

G6 permanece eliminado como candidato a gap. G7 permanece absorbido en F2.

### 6. Frontera comparativa con el piloto

El contrato del piloto permanece:

`ranking histórico Top-k fijado -> evidencia normativa posterior por candidato -> LLM local exclusivamente explicativo -> sin códigos nuevos -> sin reordenamiento -> sin feedback clasificatorio`.

0B-04B solo fundamenta por qué ese contrato es funcionalmente distinto de RAG, query transformation, passage fusion o evidentiality-guided generation. No demuestra novelty ni ausencia de prior art aduanero.

### 7. Función bibliográfica

Los seis trabajos quedan `KEEP_CORE_METHOD` dentro del mapa metodológico 0B-04B. Esto no obliga a citarlos todos en el manuscrito final.

Se conserva la metadata visible de cada copia analizada. Cualquier sustitución por una versión editorial diferente deberá verificarse expresamente antes de la citación final.

### 8. Estado de cierre

```text
0B-04B = APPROVED / FROZEN
DRAFTING_DELIVERABLE = ANALYTICALLY_COMPLETE
INTERNAL_REVIEW = PASS WITH MINOR CORRECTIONS
MATERIAL_ERRORS = 0
AUTHOR_APPROVAL = RECEIVED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

El cierre no abre automáticamente 0B-05, 0B-06 o 0C y no autoriza redacción del manuscrito.

---

## English

### 1. Status

- Block: `0B-04B — RAG, query-transformation, and grounding foundations`.
- Status: **`APPROVED / FROZEN`**.
- Initial deliverable: A–K methodological analysis of six primary PDFs by the drafting AI.
- Internal scientific/editorial review: **`PASS WITH MINOR CORRECTIONS`**.
- Material errors: `0`.
- Express author approval: received on `2026-09-03`.
- Experimental review: `NOT_REQUIRED`.
- Novelty: `NOT_DECLARED`.
- Final gap: `NOT_DEFINED`.
- Manuscript: `NOT_DRAFTED`.

Governing records are the 0B-04B prompt, internal review, and author-approval record. This artifact freezes the canonical 0B-04B methodological map.

### 2. Frozen corpus

The six primary works are Lewis et al. RAG, REALM, Fusion-in-Decoder, Query2doc, Query Rewriting for Retrieval-Augmented Large Language Models, and Evidentiality-guided Generation for Knowledge-Intensive NLP Tasks. Other corpus documents remained out of scope.

### 3. Frozen methodological distinctions

`RAG ≠ RETRIEVAL_AUGMENTED_PRETRAINING ≠ RETRIEVE_THEN_GENERATE ≠ QUERY_EXPANSION ≠ QUERY_REWRITING ≠ PASSAGE_FUSION ≠ EVIDENTIALITY_GUIDED_GENERATION`.

`RETRIEVED PASSAGE ≠ EVIDENCE ATTRIBUTION ≠ EVIDENTIALITY ≠ GROUNDING GUARANTEE ≠ PROVENANCE VERIFICATION ≠ FORMAL AUDITABILITY ≠ LEGAL CORRECTNESS`.

General comparison pipeline: `QUERY -> [QUERY TRANSFORMATION?] -> RETRIEVAL -> [FUSION / EVIDENCE SELECTION?] -> GENERATION -> OUTPUT`.

### 4. Frozen taxonomy by paper

- Lewis et al.: retrieval-augmented generation with parametric/nonparametric memory, retrieval-conditioned generation, and limited provenance support.
- REALM: retrieval-augmented pretraining, latent retrieval, retrieve-then-predict, and document-addressable memory.
- Izacard & Grave: retrieve-then-generate and passage fusion.
- Query2doc: query expansion with an LLM upstream of retrieval.
- Ma et al.: query rewriting and retriever-reader interaction.
- Asai et al.: evidentiality-guided generation, passage-evidentiality supervision, and retrieve-then-generate.

### 5. Integrated C1–C13 normalizations

**C1.** Lewis et al.'s narrative `17%` versus Table-4 `Both good = 11.7%` discrepancy is preserved; `11.7%` governs quantitative use. The 452-pair human evaluation is not a universal hallucination-reduction rate.

**C2.** RAG is retrieval-conditioned generation rather than hard grounding. RAG-Token does not retrieve again at each token, and the generator can still use parametric memory. Inspectable retrieved documents provide limited provenance support, not citation completeness or formal auditability.

**C3.** REALM remains retrieval-augmented pretraining/retrieve-then-predict, with retrieval used in pretraining, fine-tuning, and inference. Open-QA predicts answer spans. The `30× stale MIPS` ablation remains specific to REALM's training regime; document-addressable memory is not certified provenance or formal auditability.

**C4.** FiD encodes passages separately and fuses them in the decoder; passage fusion is not evidence attribution. Its reported benchmark scores and passage-count effects remain benchmark/range-specific.

**C5.** Query2doc uses an upstream LLM-generated pseudo-document for query expansion. The pseudo-document is not factual evidence or provenance, may contain false claims, and OOD outcomes are mixed.

**C6.** Query2doc changes are reported through initial/final metric values or metric-point changes, not automatically as relative percentages. Reported latency remains configuration-specific.

**C7.** Rewrite-Retrieve-Read is query rewriting/retriever-reader interaction. Rewritten queries can causally alter retrieved context and downstream outputs; it is not post-retrieval explanation. Unmeasured hallucination/factuality claims remain secondary.

**C8.** Evidentiality in Asai et al. is task-relative to whether a passage supports the gold output. Mined labels partly depend on base-generator behavior and are not universal independent human adjudication. Evidentiality is auxiliary supervision rather than a hard filter.

**C9.** Five datasets govern Asai et al.; the `six datasets` table caption is recorded as an editorial inconsistency.

**C10.** The 95% positive / 96% negative human label check is limited to the stated protocol and is not generator-wide accuracy, provenance accuracy, formal auditability, or legal correctness.

**C11.** Provenance, grounding, evidentiality, and auditability remain distinct. Inspectable passages do not imply complete claim-source alignment, passage fusion does not imply attribution, and evidentiality does not imply normative sufficiency.

**C12.** QA/IR/fact-verification/dialogue benchmark results do not transfer as HS/NANDINA classification metrics or customs normative/legal correctness.

**C13.** 0B-04B provides methodological boundaries only and does not change F1–F5's literature status. F3 is not relevant in this batch; G6 remains eliminated and G7 remains merged into F2.

### 6. Pilot comparison boundary

The pilot contract remains: externally fixed historical ranked Top-k -> candidate-specific downstream normative evidence -> explanation-only local LLM -> no new codes -> no reordering -> no classification feedback.

0B-04B only establishes why this contract is functionally distinct from RAG, query transformation, passage fusion, and evidentiality-guided generation. It does not establish novelty or missing customs prior art.

### 7. Bibliographic role

All six papers remain `KEEP_CORE_METHOD` within the 0B-04B methodological map. This does not require all six to appear in the final manuscript. Visible copy metadata is preserved; any later substitution with a different editorial version requires explicit verification.

### 8. Closure state

```text
0B-04B = APPROVED / FROZEN
DRAFTING_DELIVERABLE = ANALYTICALLY_COMPLETE
INTERNAL_REVIEW = PASS WITH MINOR CORRECTIONS
MATERIAL_ERRORS = 0
AUTHOR_APPROVAL = RECEIVED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

Closure does not automatically open 0B-05, 0B-06, or 0C and does not authorize manuscript drafting.
