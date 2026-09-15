# Plan de lotes de literatura 0B / 0B Literature Batch Plan

## Español

### 1. Propósito y reglas generales

La Fase `0B — Mapa crítico de literatura y taxonomía` se ejecuta mediante lotes temáticos controlados. Su finalidad es leer y auditar fuentes primarias completas, identificar qué problema resuelve o qué autoridad documental aporta realmente cada fuente y construir un mapa comparable para 0C. Durante 0B no se redacta el manuscrito ni se declara novelty o gap definitivo.

Reglas gobernantes:

- corpus académico/documental heredado consolidado: `62` obras/documentos distintos, acceso primario verificable `62/62`;
- lectura/auditoría claim-source-scope obligatoria;
- no inventar metadata, DOI, resultados, vigencia, jerarquía o estado editorial/normativo;
- una afirmación secundaria no se convierte en hecho independiente sin verificar su fuente primaria;
- no equiparar classification, candidate retrieval, evidence retrieval, reranking, explanation, provenance, reproducibility, auditability ni correctness;
- no imponer DIKW universal ni transformar automáticamente data→information→knowledge;
- literatura académica nueva se rige por `article/BIBLIOGRAPHIC_FRAMEWORK.md`;
- fuentes normativas/institucionales primarias constituyen una capa separada y se auditan por autoridad, identidad, vigencia, alcance y función documental.

### 2. Bloques cerrados

- `0B-01`: **`APPROVED / FROZEN`**.
- `0B-02`: **`APPROVED / FROZEN`**.
- `0B-03A`: **`APPROVED / FROZEN`**.
- `0B-03B`: **`APPROVED / FROZEN`**.
- `0B-04A`: **`APPROVED / FROZEN`**.
- `0B-04B`: **`APPROVED / FROZEN`**.
- `0B-05A`: **`APPROVED / FROZEN`**.
- `0B-05B`: **`APPROVED / FROZEN`**.
- `0B-05C`: **`APPROVED / FROZEN`**.

0B-05C cerró la auditoría de autoridad/vigencia de fuentes oficiales y la sensibilidad correctiva derivada del drift normativo. El estado congelado distingue `EXPERIMENTAL_SOURCE_SNAPSHOT` de `CURRENT_OFFICIAL_SOURCE_STATE` y mantiene `SOURCE_VERSION_DRIFT ≠ SCOPE_OVERLAP ≠ RETRIEVAL_OUTPUT_OVERLAP ≠ EXPERIMENTAL_METRIC_IMPACT`.

### 3. Estado de candidatos después de 0B-05C

Ninguno constituye novelty ni gap definitivo.

- **F1:** `CANDIDATE_GAP_ONLY — SURVIVES IN NARROW FORM`.
- **F2:** `CANDIDATE_GAP_ONLY — FURTHER NARROWED`.
- **F3:** `CANDIDATE_GAP_ONLY — RETAINED WITH APPLICABILITY CAVEAT`.
- **F4:** `CANDIDATE_GAP_ONLY — RETAINED AS METHODOLOGICAL DISTINCTION`.
- **F5:** `CANDIDATE_GAP_ONLY — FURTHER NARROWED`.
- **G6:** `ELIMINATED AS GAP CANDIDATE`.
- **G7:** `MERGED INTO F2 / ELIMINATED AS INDEPENDENT CANDIDATE`.

Las formulaciones supervivientes son:

- **F1:** precedentes históricos recuperados generan/fijan el ranking y la evidencia normativa se recupera solo después para documentar candidatos ya fijados, sin modificar el orden;
- **F2:** generador/LLM exclusivamente explicativo sobre un ranking/Top-k fijado externamente por un componente independiente, sin introducir, eliminar, sustituir o reordenar códigos y sin feedback clasificatorio;
- **F3:** control explícito de dependencia por unidad administrativa/grupo cuando observaciones correlacionadas pueden cruzar particiones;
- **F4:** candidate/predictive performance, evidence grounding o path validity no equivalen a corrección sustantiva/jurídica adjudicada;
- **F5:** evaluación formal, explícita y separada, por salida/caso, de auditabilidad documental, distinta de accuracy, citations visibles, provenance, faithfulness o rationale.

### 4. Evaluación de necesidad 0B-06

Registra el gate:

`article/reviews/0B06_BIBLIOGRAPHIC_NEED_ASSESSMENT.md`.

Dictamen:

```text
0B06_BIBLIOGRAPHIC_NEED_ASSESSMENT = REQUIRED
0B06_SCOPE = DIRECTED_FALSIFICATION_SEARCH_ONLY
OPEN_ENDED_LITERATURE_EXPANSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
```

La necesidad no deriva de insuficiencia general del corpus heredado. Antes de 0C, F1/F2/F5 y, secundariamente, F3 requieren un último pressure test reciente diseñado para encontrar prior art que los falsifique o estreche.

F4 no requiere búsqueda dedicada porque funciona como frontera metodológica, no como novelty candidata independiente.

### 5. 0B-06 — Búsqueda dirigida de literatura nueva

Estado: **`READY_FOR_DRAFTING`**.

Prompt gobernante:

`article/prompts/0B06_DIRECTED_NEW_LITERATURE_FALSIFICATION_SEARCH.md`.

Alcance autorizado, exclusivamente literatura académica nueva `2022–2026` conforme a `BIBLIOGRAPHIC_FRAMEWORK.md`:

1. **S1/F1:** ranking histórico/precedentes fijado antes de evidence retrieval normativo que no puede rerankear ni introducir códigos;
2. **S2/F2:** LLM/generador exclusivamente explicativo sobre Top-k externo e inmutable, sin modificación ni feedback clasificatorio;
3. **S3/F3:** grouped split, dependencia por declaración/entidad/familia o leakage control comparable en clasificación aduanera/comercial;
4. **S4/F5:** evaluación formal per-output/case-level de auditabilidad documental separada de predictive accuracy, provenance visible o faithfulness;
5. **S5:** trabajos que combinen dos o más de las propiedades anteriores.

Reglas adicionales:

- búsqueda falsacionista, no confirmatoria;
- no búsqueda general de HS classification;
- no reabrir G6/G7;
- no buscar F4 como novelty independiente;
- no incorporar directamente referencias nuevas al manuscrito;
- nuevas referencias solo pueden quedar `CANDIDATE_NEW` hasta revisión de la IA Gestora;
- no declarar novelty ni gap definitivo desde 0B-06.

### 6. Gate activo

```text
0B-05C = APPROVED / FROZEN
0B-06 = READY_FOR_DRAFTING
-> IA de Redacción ejecuta article/prompts/0B06_DIRECTED_NEW_LITERATURE_FALSIFICATION_SEARCH.md
-> respuesta en article/responses/0B06_DIRECTED_NEW_LITERATURE_FALSIFICATION_SEARCH_RESPONSE_V01.md
-> IA Gestora / Editor Científico Principal audita candidatos y pressure test
-> referencias nuevas solo pueden pasar a APPROVED_NEW tras auditoría
-> aprobación/cierre de 0B-06
-> cierre formal de Fase 0B
-> 0C solo después del cierre de 0B
```

### 7. Estado actual

- Fase 0A: `CLOSED / APPROVED`.
- Fase 0B: `OPEN`.
- 0B-01 a 0B-05C: `APPROVED / FROZEN`.
- Bloque activo: `0B-06`.
- 0B-06: `READY_FOR_DRAFTING`.
- 0C: `BLOCKED`.
- 0D: `BLOCKED`.
- `MANUSCRIPT_DRAFTING = NOT_AUTHORIZED`.
- Target journal: `PENDING — se decidirá en Fase 0D`.

---

## English

### 1. Purpose and general rules

Phase `0B — Critical literature map and taxonomy` uses controlled thematic batches to audit complete primary sources and construct the literature map needed for 0C. Phase 0B does not draft the manuscript or declare final novelty/gap.

The inherited academic/documentary corpus contains `62` distinct works/documents with verifiable primary access `62/62`. New academic literature is governed by `article/BIBLIOGRAPHIC_FRAMEWORK.md`; official normative/institutional sources remain a separate evidence layer.

### 2. Closed blocks

`0B-01` through `0B-05C` are **`APPROVED / FROZEN`**.

0B-05C froze the official-source authority/currency audit and the corrective sensitivity arising from normative drift. It preserves `EXPERIMENTAL_SOURCE_SNAPSHOT ≠ CURRENT_OFFICIAL_SOURCE_STATE` and `SOURCE_VERSION_DRIFT ≠ SCOPE_OVERLAP ≠ RETRIEVAL_OUTPUT_OVERLAP ≠ EXPERIMENTAL_METRIC_IMPACT`.

### 3. Candidate state after 0B-05C

No candidate is final novelty or a definitive gap.

- F1: `CANDIDATE_GAP_ONLY — SURVIVES IN NARROW FORM`.
- F2: `CANDIDATE_GAP_ONLY — FURTHER NARROWED`.
- F3: `CANDIDATE_GAP_ONLY — RETAINED WITH APPLICABILITY CAVEAT`.
- F4: `CANDIDATE_GAP_ONLY — RETAINED AS METHODOLOGICAL DISTINCTION`.
- F5: `CANDIDATE_GAP_ONLY — FURTHER NARROWED`.
- G6 is eliminated; G7 is merged into F2.

F1 now concerns fixed historical/precedent ranking followed only by non-reranking normative evidence; F2 concerns an explanation-only generator over an externally fixed immutable Top-k; F3 concerns grouped dependence control when applicable; F4 is the distinction between predictive/evidence/path metrics and substantive/legal correctness; F5 concerns formal separate per-output documentary-auditability evaluation.

### 4. 0B-06 need assessment

Governing review:

`article/reviews/0B06_BIBLIOGRAPHIC_NEED_ASSESSMENT.md`.

Verdict:

```text
0B06_BIBLIOGRAPHIC_NEED_ASSESSMENT = REQUIRED
0B06_SCOPE = DIRECTED_FALSIFICATION_SEARCH_ONLY
OPEN_ENDED_LITERATURE_EXPANSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
```

The need does not arise from broad inadequacy of the inherited corpus. Before 0C, F1/F2/F5 and secondarily F3 require one final recent falsification-oriented pressure test. F4 requires no dedicated search because it functions as a methodological boundary rather than stand-alone novelty.

### 5. 0B-06 — Directed new-literature search

Status: **`READY_FOR_DRAFTING`**.

Governing prompt:

`article/prompts/0B06_DIRECTED_NEW_LITERATURE_FALSIFICATION_SEARCH.md`.

Authorized 2022–2026 search families under `BIBLIOGRAPHIC_FRAMEWORK.md`:

1. S1/F1 fixed historical/precedent ranking before post-ranking normative evidence that cannot rerank or introduce codes;
2. S2/F2 explanation-only LLM/generator over an externally fixed immutable Top-k with no candidate modification or classificatory feedback;
3. S3/F3 grouped declaration/entity/family dependence or leakage controls in customs/commercial classification;
4. S4/F5 formal per-output/case-level documentary-auditability evaluation distinct from predictive accuracy, visible provenance, or faithfulness;
5. S5 papers combining two or more of the above properties.

The search must be falsification-oriented, not open-ended. It may not reopen G6/G7, treat F4 as independent novelty, insert references directly into the manuscript, or declare novelty/final gap. New references remain `CANDIDATE_NEW` until Managing-AI review.

### 6. Active gate

```text
0B-05C = APPROVED / FROZEN
0B-06 = READY_FOR_DRAFTING
-> Writing AI executes article/prompts/0B06_DIRECTED_NEW_LITERATURE_FALSIFICATION_SEARCH.md
-> response staged at article/responses/0B06_DIRECTED_NEW_LITERATURE_FALSIFICATION_SEARCH_RESPONSE_V01.md
-> Managing AI / Lead Scientific Editor audits candidates and the pressure test
-> new references may become APPROVED_NEW only after audit
-> approve/close 0B-06
-> formally close Phase 0B
-> 0C only after Phase 0B closes
```

### 7. Current state

Phase 0A is `CLOSED / APPROVED`; Phase 0B remains `OPEN`; 0B-01 through 0B-05C are `APPROVED / FROZEN`; 0B-06 is the active `READY_FOR_DRAFTING` block; 0C and 0D remain blocked; manuscript drafting remains unauthorized; target journal remains pending until 0D.