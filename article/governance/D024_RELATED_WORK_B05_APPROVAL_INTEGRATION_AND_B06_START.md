# D024 — Related Work B05 approval, integration, and B06 start

## Español

### Estado

```text
DECISION = D-024
RELATED_WORK_B05_V01 = APPROVED / FROZEN / INTEGRATED
B05_SEMANTIC_COMMIT = a132d97de0c56617db6dcc8f872e45d869e65c20
CANONICAL_MASTER_MD = ARTICLE_MASTER_V005.md
CANONICAL_MASTER_DOCX = LOCAL_AUTHOR_CUSTODY / D021
CANONICAL_MASTER_DOCX_SHA256 = 042952002c2caeb86ec854b0bfcd7332724ddd4712589e25dfddb52718bf159a
CANONICAL_CITATION_COMMENTS = 32
RELATED_WORK_B06 = AUTHORIZED / ACTIVE
SECTION_2_6 = AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### 1. Base de la decisión

B05 V01 fue auditado independientemente por la IA Gestora y aprobado expresamente por el autor antes de su cierre técnico. La auditoría científica concluyó `PASS`, sin correcciones científicas obligatorias ni necesidad de una V02. Se verificaron el soporte de las fuentes primarias utilizadas, la equivalencia EN–ES, la preservación de Sections 2.1–2.4, la cobertura de comentarios de auditoría y la integridad del DOCX local.

El cierre técnico definitivo se realizó en `a132d97de0c56617db6dcc8f872e45d869e65c20` bajo D-021, D-022 y D-023. La comparación contra su parent `0c34f54fbd30fce12b84a4b61bc1720bc525d7bb` muestra exactamente un commit y tres archivos Markdown añadidos:

1. `article/sections/related_work/RelatedWork_B05_V01.md`;
2. `article/manuscript/ARTICLE_MASTER_CANDIDATE_RW_B05_V01.md`;
3. `article/responses/2_RELATED_WORK_B05_RESPONSE_V01.md`.

No se modificó B06 ni ningún archivo adicional. La identidad Git de los dos artefactos científicos coincide con los archivos previamente auditados:

```text
RelatedWork_B05_V01.md Git blob = 7f0c67fd3a3449a92e23e27a371660793622013e
ARTICLE_MASTER_CANDIDATE_RW_B05_V01.md Git blob = 25782b8b2305b546f2f5ff69514893d045e50762
NET_FILE_SCOPE = PASS / EXACTLY_3_MD_FILES
SINGLE_COMMIT_DISCIPLINE = PASS
```

### 2. Promoción del master

El Markdown acumulativo aprobado de B05 se promueve sin cambios a:

`article/manuscript/ARTICLE_MASTER_V005.md`

La promoción reutiliza exactamente el blob Git `25782b8b2305b546f2f5ff69514893d045e50762`.

Conforme a D-021, el DOCX no se duplica ni se sube nuevamente al repositorio. El binario acumulativo aprobado permanece bajo custodia local del autor:

`ARTICLE_MASTER_CANDIDATE_RW_B05_V01.docx`

SHA-256 canónico del binario local:

`042952002c2caeb86ec854b0bfcd7332724ddd4712589e25dfddb52718bf159a`

Ese binario conserva 32 comentarios de auditoría, cero tracked changes y render verificado de 27/27 páginas. Puede renombrarse localmente como `ARTICLE_MASTER_V005.docx` únicamente sin modificar sus bytes; la identidad gobernante es el SHA-256 anterior.

### 3. Freeze de B05

Queda congelada la Section 2.5 `Reproducibility and evaluation in knowledge-based decision support`. Su integración no modifica las fronteras ya vigentes:

- documentación de datos ≠ certificación de calidad;
- provenance/lineage ≠ substantive correctness;
- reproducibility ≠ generalization;
- metric alignment ≠ task equivalence;
- lifecycle audit ≠ review of an individual output;
- auditability ≠ legal correctness.

### 4. Apertura de B06

Se autoriza exclusivamente `RELATED_WORK_B06 / Section 2.6 Positioning of this study`.

B06 debe cerrar Related Work mediante una síntesis comparativa breve y estrictamente soportada. Debe posicionar el estudio por la separación funcional y la autoridad asignada a cada componente, no por afirmar que los componentes individuales son nuevos.

El posicionamiento debe preservar como contrato del estudio:

```text
EXTERNAL_FIXED_HISTORICAL_RANKING
+ POST_RANKING_NORMATIVE_EVIDENCE_WITHOUT_RERANKING
+ DOWNSTREAM_EXPLANATION_ONLY
+ NO_INSERT_DELETE_SUBSTITUTE_REORDER
+ NO_CLASSIFICATION_FEEDBACK
+ DAM_AWARE_PARTITIONING_WHERE_DEPENDENCE_EXISTS
+ FUNCTION_SPECIFIC_EVALUATION
```

B06 debe reconocer explícitamente el prior art parcial y cercano ya identificado. En particular, candidate prediction + evidence retrieval no constituye por sí solo una contribución nueva, y existe prior art de regulatory AI con evaluación de explicación/auditabilidad. La diferencia científicamente defendible está en el contrato funcional completo y sus límites de autoridad, sin convertir esa diferencia en una declaración de novelty.

### 5. Prohibiciones de B06

B06 no está autorizado a:

- declarar `first`, `novel`, `unique`, `unprecedented` o equivalentes;
- declarar ausencia universal de prior art;
- definir `FINAL_GAP`;
- declarar `NOVELTY`;
- presentar resultados o métricas del presente estudio;
- afirmar SOTA o superioridad frente a otros trabajos;
- convertir asociación normativa en corrección jurídica;
- convertir explicaciones trazables en legal correctness;
- afirmar generalización empírica fuera del testbed;
- abrir Introduction, Architecture, Experimental Design, Results o Discussion.

Al cierre de B06, cualquier paso posterior requiere revisión independiente de la IA Gestora y aprobación expresa del autor.

---

## English

### Status

```text
DECISION = D-024
RELATED_WORK_B05_V01 = APPROVED / FROZEN / INTEGRATED
B05_SEMANTIC_COMMIT = a132d97de0c56617db6dcc8f872e45d869e65c20
CANONICAL_MASTER_MD = ARTICLE_MASTER_V005.md
CANONICAL_MASTER_DOCX = LOCAL_AUTHOR_CUSTODY / D021
CANONICAL_MASTER_DOCX_SHA256 = 042952002c2caeb86ec854b0bfcd7332724ddd4712589e25dfddb52718bf159a
CANONICAL_CITATION_COMMENTS = 32
RELATED_WORK_B06 = AUTHORIZED / ACTIVE
SECTION_2_6 = AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

B05 V01 passed independent scientific review and explicit author approval. Its final technical closure at `a132d97de0c56617db6dcc8f872e45d869e65c20` contains exactly the three authorized Markdown artifacts in one commit. The two scientific artifacts are byte-identical at the Git-blob level to the versions previously audited.

The cumulative B05 Markdown is promoted unchanged to `ARTICLE_MASTER_V005.md`, reusing Git blob `25782b8b2305b546f2f5ff69514893d045e50762`. Under D-021, the approved cumulative DOCX remains in author-local custody with SHA-256 `042952002c2caeb86ec854b0bfcd7332724ddd4712589e25dfddb52718bf159a`; immediate repository upload is not required.

Section 2.5 is frozen. B06 / Section 2.6 is now the only authorized drafting scope. It must provide a concise, evidence-bounded positioning synthesis based on functional separation and component authority. It must acknowledge close and partial prior art and must not turn architectural difference into novelty. `FINAL_GAP` remains `NOT_DEFINED` and `NOVELTY` remains `NOT_DECLARED`.
