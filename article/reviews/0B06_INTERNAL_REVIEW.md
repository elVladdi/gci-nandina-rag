# Revisión interna 0B-06 / 0B-06 Internal Review

## Español

### 1. Dictamen

```text
0B06_INTERNAL_REVIEW = PASS
MATERIAL_ERRORS = 0
MINOR_CORRECTIONS_REQUIRED = 0
EXPERIMENTAL_REVIEW = NOT_REQUIRED
AUTHOR_APPROVAL = PENDING
FREEZE_0B06 = NOT_AUTHORIZED_YET
0C = BLOCKED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
```

La IA Gestora / Editor Científico Principal auditó la entrega versionada en:

`article/responses/0B06_DIRECTED_NEW_LITERATURE_FALSIFICATION_SEARCH_RESPONSE_V01.md`

commit:

`74ea8055e675e4faf2968b89de206aa68c8b82b6`.

La entrega cumple el propósito falsacionista y acotado de 0B-06, respeta las familias S1–S5, no convierte resultados negativos en prueba de novelty, conserva la separación entre prior art directo, parcial, negativos cercanos y leads no admisibles, y no modifica resultados experimentales ni el Plan Maestro.

La integridad del commit fue verificada contra el estado de apertura `9d7a482b05d30def281ea5ef4c2e34c54cb2cf5d`: existe un único commit adicional y un único archivo añadido, el artefacto de respuesta V01, con 409 líneas añadidas y sin modificaciones a archivos de gobernanza, freezes o resultados.

### 2. Verificación independiente de referencias determinantes

#### N01 — Chen & Tanaka-Ishii (2026)

Se verificó en la fuente primaria oficial de Frontiers:

- título: *Executable explanation traces for legal LLM predictions via retrieval-augmented codification*;
- revista: *Frontiers in Artificial Intelligence*;
- publicación: 20 de agosto de 2026;
- DOI: `10.3389/frai.2026.1905145`;
- tipo: Original Research, revisado por pares y open access;
- indexación declarada por la revista: Scopus y Web of Science ESCI, entre otras;
- métricas vigentes publicadas por Frontiers en 2026: JIF 6.7, CiteScore 8.0, JIF Q1 y CiteScore Q1.

También se verificó en el texto primario que el paper:

- usa recuperación de fuentes legales `R1` y ejemplos in-domain fold-safe `R2`;
- genera y refina una representación ejecutable que participa en la predicción, por lo que no constituye un explicador downstream causalmente aislado;
- evalúa propiedades de explicación separadas de label accuracy;
- realiza un análisis post-hoc de predicate/source support contra el corpus legal recuperado;
- evalúa predicate support sobre 1,000 instancias muestreadas;
- reporta 99.12%/0.88% supported/unsupported para CAIL y 91.13%/8.87% para CAP en la configuración completa;
- limita expresamente source support a un diagnóstico de grounding y no a prueba de legal correctness o completitud doctrinal.

Por tanto, la caracterización de N01 en la respuesta V01 es materialmente correcta.

**Decisión editorial de admisión:**

`N01 = APPROVED_NEW`.

N01 es admisible como literatura nueva y relevante para el pressure test de F2/F5. Su uso futuro debe mantener explícitamente que se trata de regulatory/legal AI, no HS/customs, y que su evaluación de source support no demuestra legal correctness.

#### N02 — Wube et al. (2026)

Se verificó en Springer Nature la identidad del artículo:

- título: *A review of machine learning, deep learning and large language model based harmonized system code classification techniques for import and export commodities*;
- revista: *Discover Computing*;
- volumen 29, artículo 505;
- publicación: 5 de agosto de 2026;
- DOI: `10.1007/s10791-026-10428-y`;
- tipo: Review, open access.

La respuesta V01 usa correctamente N02 como fuente secundaria de discovery/corroboración y no como prueba independiente de ausencia de prior art.

Sin embargo, la señal de cuartil reportada es dependiente de categoría y la propia entrega conserva el paper como `CANDIDATE_NEW — REVIEW`. No es necesario resolver su admisión para cerrar el pressure test, porque ninguna conclusión determinante de F1–F5 depende exclusivamente de N02.

**Decisión editorial de admisión:**

`N02 = REVIEW_REQUIRED / NOT_ADMITTED_YET`.

#### N03 y N04

N03 y N04 están correctamente tratados como negativos cercanos/rechazos funcionales. Sus tareas directas de clasificación no satisfacen las arquitecturas estrictas F1/F2 ni la evaluación F5. No se admiten como nuevas referencias por este gate.

`N03 = REJECT`.

`N04 = REJECT`.

Los proceedings, preprints, tesis y otros leads registrados en la sección G permanecen `NON_ADMISSIBLE_LEAD` y no determinan el resultado del pressure test.

### 3. Auditoría del pressure test

#### F1

Resultado V01:

`NO_DIRECT_MATCH_FOUND_WITHIN_SEARCH_SCOPE`.

Se acepta. La entrega no convierte esta ausencia acotada en novelty. La formulación superviviente continúa siendo estricta:

> precedentes históricos recuperados generan/fijan el ranking y la evidencia normativa se recupera después exclusivamente para documentar esos candidatos, sin capacidad de reordenar, sustituir o introducir códigos.

No se autoriza afirmar ausencia universal de prior art ni novelty de esta combinación.

#### F2

Resultado V01:

`PARTIAL_PRIOR_ART_FOUND`.

Se acepta. N01 es un antecedente cercano porque combina recuperación, fuentes legales y una explicación/audit trace evaluada, pero el programa/trace participa en producir y refinar la predicción. Por tanto, no satisface el contrato estricto del proyecto.

La formulación que sobrevive debe conservar como condición constitutiva:

`EXTERNAL_FIXED_TOP_K + DOWNSTREAM_EXPLANATION_ONLY + NO_INSERT/DELETE/SUBSTITUTE/REORDER + NO_CLASSIFICATION_FEEDBACK`.

No se autoriza novelty todavía.

#### F3

Resultado V01:

`NO_DIRECT_MATCH_FOUND_WITHIN_SEARCH_SCOPE`.

Se acepta únicamente como resultado negativo acotado. F3 continúa siendo un principio/candidato metodológico condicionado a la existencia de observaciones correlacionadas por unidad administrativa o entidad. La ausencia de grouped split documentado en un antecedente no prueba leakage ni novelty.

#### F5

Resultado V01:

`DIRECT_PRIOR_ART_FOUND`.

Se acepta con la interpretación estrecha ya expresada por la propia entrega. N01 constituye prior art directo contra una formulación amplia de que regulatory AI carece de evaluación explícita y separada de source support/audit-oriented traces por salida/instancia.

En consecuencia:

`F5_GENERAL_REGULATORY_AI_ABSENCE_CLAIM = FALSIFIED`.

F5 no puede conservarse en 0C como un supuesto gap general de regulatory AI. Si alguna propiedad relacionada permanece útil para posicionamiento posterior, deberá formularse únicamente de manera contextual, por ejemplo como integración HS/customs-specific con la arquitectura fija del proyecto, y deberá volver a justificarse sin transformar esa contextualización en novelty automática.

### 4. Coherencia metodológica y epistemológica

La entrega distingue correctamente:

- `DIRECT_PRIOR_ART_FOUND` de `PARTIAL_PRIOR_ART_FOUND`;
- resultado negativo acotado de inexistencia universal;
- fuente primaria de revisión secundaria;
- source support/auditability de legal correctness;
- explicación acoplada a decisión de explicación downstream causalmente aislada;
- grouped split de mera partición aleatoria/estratificada;
- proceedings/preprints/leads de referencias académicas admisibles.

No se detecta reinterpretación de resultados experimentales congelados, ni modificación de C21–C25, ni reapertura de G6/G7, ni declaración de gap final o novelty.

### 5. Equivalencia bilingüe

Se revisó la correspondencia ES/EN de las secciones de estado, búsqueda, candidatos, fichas, falsación, resultados acumulados, leads, dictamen y trazabilidad. No se detectaron diferencias materiales de fuerza, alcance, cifras o límites entre ambos idiomas.

### 6. Estado editorial resultante

```text
0B-06 = INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING
0B06_INTERNAL_REVIEW = PASS
MATERIAL_ERRORS = 0
MINOR_CORRECTIONS_REQUIRED = 0
N01 = APPROVED_NEW
N02 = REVIEW_REQUIRED / NOT_ADMITTED_YET
N03 = REJECT
N04 = REJECT
F1 = NO_DIRECT_MATCH_FOUND_WITHIN_SEARCH_SCOPE
F2 = PARTIAL_PRIOR_ART_FOUND
F3 = NO_DIRECT_MATCH_FOUND_WITHIN_SEARCH_SCOPE
F5 = DIRECT_PRIOR_ART_FOUND
F5_GENERAL_REGULATORY_AI_ABSENCE_CLAIM = FALSIFIED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
AUTHOR_APPROVAL = PENDING
FREEZE_0B06 = NOT_AUTHORIZED_YET
0C = BLOCKED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
```

### 7. Gate

No se requiere retorno a la IA de Redacción. La respuesta V01 es suficientemente completa y científicamente consistente para pasar al gate de aprobación del autor.

La aprobación del autor debe autorizar exclusivamente:

- congelar 0B-06 con los resultados de pressure test anteriores;
- incorporar N01 como `APPROVED_NEW` al registro bibliográfico editorial;
- mantener N02 como `REVIEW_REQUIRED / NOT_ADMITTED_YET`;
- actualizar los estados provisionales F1/F2/F3/F5 para su consumo posterior en 0C;
- cerrar formalmente la Fase 0B si no existe otro bloqueo bibliográfico.

La aprobación no debe autorizar todavía una formulación final de gap/novelty ni la redacción del manuscrito.

---

## English

### 1. Verdict

```text
0B06_INTERNAL_REVIEW = PASS
MATERIAL_ERRORS = 0
MINOR_CORRECTIONS_REQUIRED = 0
EXPERIMENTAL_REVIEW = NOT_REQUIRED
AUTHOR_APPROVAL = PENDING
FREEZE_0B06 = NOT_AUTHORIZED_YET
0C = BLOCKED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
```

The Managing AI / Lead Scientific Editor audited the versioned deliverable at `article/responses/0B06_DIRECTED_NEW_LITERATURE_FALSIFICATION_SEARCH_RESPONSE_V01.md`, commit `74ea8055e675e4faf2968b89de206aa68c8b82b6`.

The deliverable satisfies the bounded falsification-oriented purpose of 0B-06, follows S1–S5, does not turn negative search results into novelty evidence, preserves the distinction among direct prior art, partial prior art, close negatives, and non-admissible leads, and does not modify experimental results or the Master Plan.

Commit integrity was verified against opening state `9d7a482b05d30def281ea5ef4c2e34c54cb2cf5d`: exactly one additional commit and one added file, the V01 response artifact, with 409 added lines and no modifications to governance files, freezes, or results.

### 2. Independent verification of determinant references

#### N01 — Chen & Tanaka-Ishii (2026)

The primary Frontiers source verifies the title, journal, publication date (20 August 2026), DOI `10.3389/frai.2026.1905145`, Original Research article type, peer review, open access status, Scopus/WoS-ESCI indexing, and current 2026 publisher-reported metrics (JIF 6.7, CiteScore 8.0, JIF Q1, CiteScore Q1).

The primary article also verifies R1 legal-source retrieval, fold-safe R2 examples, an executable representation that participates in prediction/refinement, explanation-level evaluation separate from label accuracy, post-hoc predicate/source-support auditing, 1,000 sampled instances for predicate support, the reported CAIL/CAP support values, and the explicit boundary that source support is a grounding diagnostic rather than proof of legal correctness or doctrinal completeness.

Therefore the V01 characterization of N01 is materially correct.

**Editorial admission decision:** `N01 = APPROVED_NEW`.

N01 is admissible as new literature relevant to the F2/F5 pressure test. Future use must state that it concerns regulatory/legal AI rather than HS/customs and that source-support evaluation does not establish legal correctness.

#### N02 — Wube et al. (2026)

Springer Nature verifies the title, *Discover Computing*, volume 29 article 505, publication date 5 August 2026, DOI `10.1007/s10791-026-10428-y`, Review type, and open-access status.

V01 correctly treats N02 as secondary discovery/corroboration rather than independent proof of prior-art absence. Because the reported quartile signal varies by category and V01 itself retains the paper as `CANDIDATE_NEW — REVIEW`, its admission need not be resolved to close the pressure test.

**Editorial admission decision:** `N02 = REVIEW_REQUIRED / NOT_ADMITTED_YET`.

#### N03 and N04

N03 and N04 are correctly handled as close negatives/functional rejections. Their direct-classification tasks do not satisfy strict F1/F2 architectures or F5 evaluation. They are not admitted as new references through this gate.

`N03 = REJECT`.

`N04 = REJECT`.

Proceedings, preprints, theses, and other Section-G leads remain `NON_ADMISSIBLE_LEAD` and do not determine the pressure-test result.

### 3. Pressure-test audit

**F1 — `NO_DIRECT_MATCH_FOUND_WITHIN_SEARCH_SCOPE`: accepted.** The bounded negative result does not establish universal absence or novelty. The surviving formulation remains fixed historical/precedent ranking followed by non-reranking normative evidence for those candidates only.

**F2 — `PARTIAL_PRIOR_ART_FOUND`: accepted.** N01 is close prior art, but its program/trace participates in prediction and refinement. The surviving condition must retain `EXTERNAL_FIXED_TOP_K + DOWNSTREAM_EXPLANATION_ONLY + NO_INSERT/DELETE/SUBSTITUTE/REORDER + NO_CLASSIFICATION_FEEDBACK`. Novelty is not authorized.

**F3 — `NO_DIRECT_MATCH_FOUND_WITHIN_SEARCH_SCOPE`: accepted only as a bounded negative.** F3 remains methodological and applicable only when data contain correlated observations by administrative/entity grouping. Missing reported grouping does not prove leakage or novelty.

**F5 — `DIRECT_PRIOR_ART_FOUND`: accepted.** N01 directly defeats a broad claim that regulatory AI lacks explicit separate source-support/audit-oriented trace evaluation by output/instance. Therefore `F5_GENERAL_REGULATORY_AI_ABSENCE_CLAIM = FALSIFIED`. Any later F5-related positioning must be narrower and contextual, such as HS/customs-specific integration with the project's fixed architecture, and must not be converted automatically into novelty.

### 4. Methodological and epistemic consistency

The deliverable correctly separates direct from partial prior art, bounded negatives from universal absence, primary from secondary evidence, source support/auditability from legal correctness, decision-coupled explanations from causally isolated downstream explanation, grouped splitting from random/stratified partitioning, and non-admissible documentary types from admissible academic references.

No frozen experimental result is reinterpreted; C21–C25 are not modified; G6/G7 are not reopened; and no final gap or novelty is declared.

### 5. Bilingual equivalence

The Spanish and English status, search, candidate, full-record, falsification, cumulative-result, lead, verdict, and traceability sections were checked. No material difference in claim strength, scope, numbers, or limitations was identified.

### 6. Resulting editorial state

```text
0B-06 = INTERNAL_REVIEW_COMPLETE / AUTHOR_APPROVAL_PENDING
0B06_INTERNAL_REVIEW = PASS
MATERIAL_ERRORS = 0
MINOR_CORRECTIONS_REQUIRED = 0
N01 = APPROVED_NEW
N02 = REVIEW_REQUIRED / NOT_ADMITTED_YET
N03 = REJECT
N04 = REJECT
F1 = NO_DIRECT_MATCH_FOUND_WITHIN_SEARCH_SCOPE
F2 = PARTIAL_PRIOR_ART_FOUND
F3 = NO_DIRECT_MATCH_FOUND_WITHIN_SEARCH_SCOPE
F5 = DIRECT_PRIOR_ART_FOUND
F5_GENERAL_REGULATORY_AI_ABSENCE_CLAIM = FALSIFIED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
EXPERIMENTAL_REVIEW = NOT_REQUIRED
AUTHOR_APPROVAL = PENDING
FREEZE_0B06 = NOT_AUTHORIZED_YET
0C = BLOCKED
MANUSCRIPT_DRAFTING = NOT_AUTHORIZED
```

### 7. Gate

No return to the Writing AI is required. V01 is sufficiently complete and scientifically consistent to proceed to author approval.

Author approval should authorize only freezing 0B-06 with the pressure-test results above, admitting N01 as `APPROVED_NEW`, retaining N02 as `REVIEW_REQUIRED / NOT_ADMITTED_YET`, updating provisional F1/F2/F3/F5 states for later 0C use, and formally closing Phase 0B if no other bibliographic blocker exists.

Approval must not yet authorize a final gap/novelty formulation or manuscript drafting.