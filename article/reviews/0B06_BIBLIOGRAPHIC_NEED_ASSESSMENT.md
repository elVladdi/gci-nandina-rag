# Evaluación de necesidad bibliográfica 0B-06 / 0B-06 Bibliographic Need Assessment

## Español

### 1. Objeto

Esta revisión ejecuta exclusivamente el gate `ASSESS_GENUINE_NEED_FOR_0B-06` posterior al freeze de `0B-05C`. No abre todavía 0C, no declara novelty ni gap definitivo, no modifica resultados experimentales, no modifica 0A ni el Plan Maestro y no redacta el manuscrito.

Fuentes editoriales gobernantes para este gate:

- `article/START_HERE.md`;
- `article/ARTICLE_STATUS.md`;
- `article/ARTICLE_WRITING_PLAN.md`;
- `article/BIBLIOGRAPHIC_FRAMEWORK.md`;
- `article/literature/0B_LITERATURE_BATCH_PLAN.md`;
- freezes `0B-01`, `0B-02`, `0B-03A`, `0B-03B`, `0B-04A`, `0B-04B`, `0B-05A`, `0B-05B` y `0B-05C`;
- `article/CLAIM_EVIDENCE_MATRIX.md`.

### 2. Criterio de decisión

Según `BIBLIOGRAPHIC_FRAMEWORK.md`, literatura académica nueva solo debe buscarse cuando exista un vacío bibliográfico real y concreto. La búsqueda no puede abrirse para aumentar el número de citas ni para confirmar una conclusión ya deseada.

Para este gate se considera que existe necesidad real si, antes de 0C, queda al menos un candidato de gap potencialmente central cuya ausencia de prior art no haya sido sometida a una búsqueda contemporánea dirigida y falsacionista fuera del corpus heredado.

### 3. Estado acumulado del mapa 0B

El corpus heredado ya cubre de forma amplia:

- clasificación HS directa y supervisada;
- candidate retrieval, precedent retrieval y evidence retrieval;
- validación/correctness assessment;
- LLM, RAG y multimodalidad;
- agentes, deep search, búsqueda jerárquica y razonamiento regulatorio;
- fundamentos IR, reranking, RAG, query transformation, grounding y evidentiality;
- provenance, reproducibilidad, documentación y lifecycle audit;
- conocimiento explícito/documental y límites del expertise codificado;
- autoridad, vigencia y trazabilidad de fuentes oficiales.

El pressure test acumulado ya eliminó `G6`, absorbió `G7` en `F2` y estrechó sustancialmente F1, F2 y F5. F4 quedó como distinción metodológica, no como novelty candidata.

### 4. Necesidad residual por candidato

#### F1 — separación ranking histórico / evidencia normativa posterior

Estado previo: `CANDIDATE_GAP_ONLY — SURVIVES IN NARROW FORM`.

El corpus ya contiene prior art cercano que combina candidate prediction, retrieval, normativa/reglas, RAG y evidencia visible. Sin embargo, la formulación superviviente es mucho más estricta: **precedentes históricos recuperados fijan el ranking y la evidencia normativa se incorpora únicamente después, sin capacidad de alterar ese orden**.

Esta formulación puede ser central para el posicionamiento del artículo. El corpus heredado la ha sometido a presión, pero no constituye una búsqueda contemporánea específicamente diseñada para falsarla en literatura académica 2022–2026 de revista. Por ello existe una necesidad bibliográfica residual concreta.

#### F2 — LLM exclusivamente explicativo sobre Top-k externo e inmutable

Estado previo: `CANDIDATE_GAP_ONLY — FURTHER NARROWED`.

0B-03B ya falsificó la formulación amplia de que no existe explicación posterior a una decisión fijada. La versión superviviente exige un **generador exclusivamente explicativo sobre un ranking/Top-k fijado externamente por un componente independiente, sin introducir, eliminar, sustituir o reordenar códigos y sin feedback clasificatorio**.

Dado que esta diferencia arquitectónica puede formar parte de la contribución central, necesita una búsqueda reciente dirigida a encontrar prior art funcionalmente equivalente o suficientemente cercano.

#### F3 — control de dependencia por unidad administrativa/grupo

Estado previo: `CANDIDATE_GAP_ONLY — RETAINED WITH APPLICABILITY CAVEAT`.

La literatura heredada no documenta un control directamente comparable a DAM en los estudios donde tal dependencia sería aplicable. No obstante, F3 debe tratarse principalmente como requisito de validez metodológica y no como novelty por sí mismo.

Se justifica una búsqueda secundaria y acotada de literatura reciente sobre grouped splitting, entity/declaration leakage, duplicate-family leakage o controles de dependencia en clasificación aduanera/comercial. El objetivo es evitar una afirmación indebida de ausencia, no convertir F3 en la contribución central.

#### F4 — retrieval/performance ≠ corrección sustantiva

Estado previo: `CANDIDATE_GAP_ONLY — RETAINED AS METHODOLOGICAL DISTINCTION`.

No requiere 0B-06 específico. El corpus ya sustenta ampliamente que candidate performance, coherence, evidence grounding, path validity y legal/substantive correctness no son equivalentes. F4 debe pasar a 0C como frontera metodológica, no como novelty candidata independiente.

#### F5 — evaluación formal y separada de auditabilidad documental por salida

Estado previo: `CANDIDATE_GAP_ONLY — FURTHER NARROWED`.

El corpus ya documenta provenance, citations, evidence snippets, transparency trails, internal audit, faithfulness y traceability. Por ello está prohibida cualquier formulación amplia de que la literatura carece de auditabilidad.

La formulación superviviente —**evaluación formal, explícita y separada, a nivel de salida/caso, de auditabilidad documental mediante criterios o rúbrica distinta de predictive performance**— puede ser relevante para el artículo y merece una búsqueda contemporánea dirigida a prior art equivalente.

### 5. Dictamen

```text
0B06_BIBLIOGRAPHIC_NEED_ASSESSMENT = REQUIRED
0B06_SCOPE = DIRECTED_FALSIFICATION_SEARCH_ONLY
OPEN_ENDED_LITERATURE_EXPANSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
```

La necesidad no deriva de insuficiencia general del corpus de 62 documentos. Deriva de una pregunta más estrecha: antes de que 0C convierta F1/F2/F5 —y secundariamente F3— en posibles formulaciones de gap/contribución, debe existir un último pressure test reciente y dirigido que intente **falsarlas**, no confirmarlas.

### 6. Alcance autorizado de 0B-06

0B-06 queda limitado a literatura académica nueva `2022–2026`, conforme a `BIBLIOGRAPHIC_FRAMEWORK.md`, y únicamente a cuatro familias de búsqueda:

1. `F1`: ranking histórico/precedentes fijado antes de evidence retrieval normativo no-reranking;
2. `F2`: LLM/generador exclusivamente explicativo sobre Top-k externo e inmutable;
3. `F3`: grouped split / declaration- or entity-level dependence / leakage control en clasificación aduanera o comercial comparable;
4. `F5`: evaluación formal per-output/case-level de auditabilidad documental separada de accuracy/faithfulness/traceability visible.

Debe buscar también trabajos que combinen dos o más de estas propiedades.

No se autoriza:

- una búsqueda general de “HS code classification”;
- reabrir G6 o G7;
- buscar F4 como novelty independiente;
- sustituir literatura heredada por recencia;
- insertar directamente referencias nuevas en el manuscrito;
- modificar claims o estados experimentales durante la búsqueda.

### 7. Gate resultante

```text
0B-05C = APPROVED / FROZEN
0B-06 = READY_FOR_DRAFTING
0C = BLOCKED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
```

Siguiente actor: **IA de Redacción**, mediante prompt cerrado y versionado de búsqueda bibliográfica dirigida. La respuesta debe quedar en `article/responses/` y volver a la IA Gestora / Editor Científico Principal para auditoría antes de admitir cualquier nueva referencia.

---

## English

### 1. Purpose

This review executes only the post-0B-05C-freeze `ASSESS_GENUINE_NEED_FOR_0B-06` gate. It does not open 0C, declare final novelty/gap, modify experiments, 0A, or the Master Plan, or draft the manuscript.

### 2. Decision criterion

Under `BIBLIOGRAPHIC_FRAMEWORK.md`, new academic literature is searched only for a concrete bibliographic need. Search must not be opened merely to increase citation count or confirm a preferred conclusion.

A genuine need exists here if a potentially central surviving gap candidate has not yet been subjected to a recent, targeted, falsification-oriented search beyond the inherited corpus.

### 3. Accumulated 0B map

The inherited corpus already covers direct HS classification, candidate/precedent/evidence retrieval, correctness assessment, LLM/RAG/multimodality, agentic and hierarchical regulatory reasoning, IR and RAG foundations, provenance/reproducibility/auditing, documented knowledge, and official-source authority/currency/traceability.

The accumulated pressure test eliminated G6, merged G7 into F2, and substantially narrowed F1, F2, and F5. F4 now functions as a methodological distinction rather than an independent novelty candidate.

### 4. Residual need

- **F1:** a directed recent search is needed for systems where historical/precedent retrieval fixes the ranking before normative evidence retrieval that cannot alter order.
- **F2:** a directed recent search is needed for explanation-only generators operating on an externally fixed immutable Top-k, with no code insertion/deletion/substitution/reordering and no classificatory feedback.
- **F3:** only a secondary bounded search is needed for customs/commercial grouped splitting, declaration/entity dependence, and leakage control; F3 should primarily remain a validity principle rather than stand-alone novelty.
- **F4:** no dedicated 0B-06 search is required; the distinction between retrieval/performance and substantive/legal correctness is already well supported.
- **F5:** a directed recent search is needed for formal, explicit, separate per-output/case-level documentary-auditability evaluation, distinct from accuracy, visible traceability, citations, provenance, or faithfulness.

### 5. Verdict

```text
0B06_BIBLIOGRAPHIC_NEED_ASSESSMENT = REQUIRED
0B06_SCOPE = DIRECTED_FALSIFICATION_SEARCH_ONLY
OPEN_ENDED_LITERATURE_EXPANSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
```

The need does not arise from general insufficiency of the 62-document corpus. It arises because F1/F2/F5 — and secondarily F3 — may influence the eventual contribution statement, and therefore require one final recent search explicitly designed to falsify them before 0C.

### 6. Authorized 0B-06 scope

0B-06 is restricted to new 2022–2026 academic literature under `BIBLIOGRAPHIC_FRAMEWORK.md` and only four search families: F1 historical-ranking/normative-evidence separation; F2 explanation-only LLM over immutable external Top-k; F3 grouped/declaration/entity dependence or leakage control; and F5 formal per-output documentary-auditability evaluation. Combined-property papers must also be sought.

General HS-classification searching, reopening G6/G7, treating F4 as independent novelty, replacing inherited literature merely for recency, direct manuscript insertion, or modification of experimental claims/states are not authorized.

### 7. Resulting gate

```text
0B-05C = APPROVED / FROZEN
0B-06 = READY_FOR_DRAFTING
0C = BLOCKED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
```

Next actor: **Writing AI**, through a closed versioned prompt for the directed bibliographic search. Its response must be staged under `article/responses/` and return to the Managing AI / Lead Scientific Editor for audit before any new reference is admitted.