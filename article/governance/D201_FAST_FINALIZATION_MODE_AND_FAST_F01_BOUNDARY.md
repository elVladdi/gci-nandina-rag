# D-201 — Formalización de FAST_FINALIZATION_MODE y boundary de FAST-F01

## Español

```text
DECISION = D-201
PHASE = FAST_FINALIZATION
PREVIOUS_DECISION = D-200

CANONICAL_MASTER = ARTICLE_MASTER_V037
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V037.md
CANONICAL_MASTER_MD_GIT_BLOB =
338344b1bc520378337a6760377aa3400cf6d5d1
CANONICAL_MASTER_MD_SHA256 =
c1fea282d41d338a10ee7c01ee4e831baa16a792f34beb644c2a3ceb6a200919

CANONICAL_MASTER_DOCX =
ARTICLE_MASTER_CANDIDATE_G7F03_A09_A10_V01.docx
CANONICAL_MASTER_DOCX_SHA256 =
6d88e393109fb7f7962dea75013c4ad28924bbabb0ab10e10d37400322d88c5c
CANONICAL_MASTER_DOCX_SIZE_BYTES = 112705
CANONICAL_MASTER_DOCX_PAGE_COUNT = 73
CANONICAL_CITATION_COMMENTS = 48
CANONICAL_TRACKED_CHANGES = 0

G7_F03 = CLOSED / APPROVED
GROUP7 = CLOSED / APPROVED

EXPERIMENTAL_G8_F01 =
ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED

FAST_FINALIZATION_MODE = FORMALIZED

EDITORIAL_FAST_F01 =
SCIENTIFIC_PRESENTATION_AND_VISUAL_STRUCTURING
EDITORIAL_FAST_F02 =
END_MATTER_REFERENCE_AND_SUPPLEMENTARY_INTEGRITY
EDITORIAL_FAST_F03 =
SUBMISSION_ASSEMBLY_AND_FINAL_QA

CURRENT_GATE = FAST_F01_PROMPT_PREPARATION
NEXT_ACTOR = IA_GESTORA_DEL_ARTICULO
```

## 1. Nomenclatura

Para evitar confusión con el Plan Maestro Experimental, las macrofichas editoriales se denominan:

- `FAST-F01`;
- `FAST-F02`;
- `FAST-F03`.

No deben confundirse con `G8-F01`, `G8-F02` o `G8-F03` del Plan Experimental.

## 2. Objetivo del modo FAST

El Autor solicitó terminar el artículo con la misma trazabilidad utilizada durante la redacción, pero minimizando ciclos administrativos.

Se adopta:

```text
ONE_MAIN_WRITING_CYCLE_PER_FAST_FICHA
ONE_GESTORA_AUDIT_PER_FAST_FICHA
ONE_AUTHOR_GATE_PER_FAST_FICHA
NO_EXPERIMENTAL_REAUDIT_UNLESS_NEW_SCIENTIFIC_CONTENT_OR_CONTRADICTION_APPEARS
```

## 3. FAST-F01 — Scientific Presentation & Visual Structuring

### Objetivo

Mejorar legibilidad científica del cuerpo del artículo mediante una combinación sobria de prosa, tablas y figuras, sin modificar resultados, inferencia o claims.

### Base editorial

`article/reviews/16_FAST_F01_KBS34_TABLE_FIGURE_EDITORIAL_REVIEW_V01.md`

Git blob:

`0122c06db0a8a35251ea5535d6386a95c24f344a`

### Scope principal

Objetivo de cuerpo principal:

```text
MAIN_BODY_TABLES = 3
MAIN_BODY_FIGURES = 2
```

#### Table 1 — Experimental benchmark and partition/evaluation overview

Síntesis editorial exclusiva de contenido ya aprobado en V037.

No puede crear nuevas métricas, porcentajes, agregados o inferencias.

#### Table 2 — G5-MAIN-01

Debe utilizar la tabla canónica:

`outputs/results/group5/tables/g5_main_01_he2a_primary_early_ranking.csv`

y su contrato G5.

#### Table 3 — G5-MAIN-02

Debe utilizar la tabla canónica:

`outputs/results/group5/tables/g5_main_02_he2b_deep_coverage.csv`

y su contrato G5.

#### Figure 1 — Architecture

Debe materializar visualmente el flujo congelado:

```text
INPUT
-> QUERY NORMALIZATION
-> HISTORICAL RETRIEVAL / RANKING
-> FIXED TOP-3
-> CANDIDATE-SPECIFIC DOCUMENTARY EVIDENCE
-> CONTEXT ASSEMBLY
-> LOCAL LLM EXPLANATION
```

El reranker diagnóstico, si se representa, debe aparecer como ruta lateral separada y explícitamente diagnóstica, sin flecha de retorno al ranking principal ni al Top-3 fijo.

#### Figure 2 — G6-FIG-01

Debe utilizar sin alteración científica:

- `figures/group6/g6_fig_01_he2.svg`;
- o su PNG aprobado `figures/group6/g6_fig_01_he2.png`;
- caption gobernado por `docs/figures/group6/g6_caption_registry_v0.1.md`.

### Compresión permitida

Puede compactarse únicamente la prosa inmediatamente redundante con las tablas/figuras incorporadas.

Toda compresión debe preservar:

- denominadores;
- cifras;
- comparadores;
- incertidumbre;
- condiciones de interpretación;
- RQ/HE;
- límites causales;
- benchmark scope.

## 4. Material suplementario reservado para FAST-F02

FAST-F01 no debe insertar en el cuerpo:

- G5-SECONDARY-01;
- G5-SECONDARY-02;
- G5-APPENDIX-01;
- G5-APPENDIX-02;
- G5-APPENDIX-03;
- G5-APPENDIX-04;
- G5-APPENDIX-05;
- G6-FIG-02;
- G6-FIG-03.

Estos artefactos quedan congelados para ensamblaje suplementario en FAST-F02.

## 5. FAST-F02

Scope previsto:

- Author metadata;
- CRediT;
- funding;
- competing interests;
- acknowledgements;
- Data availability;
- reproducibility wording;
- reference integrity;
- material suplementario aprobado G5/G6.

Los hechos autorales deberán ser proporcionados por el Autor; IA de Redacción no puede inventarlos.

## 6. FAST-F03

Scope previsto:

- limpieza de drafting notes;
- eliminación de español de la versión publication-facing;
- numeración final y cross-references;
- captions;
- revisión de comentarios y tracked changes;
- assembly del Word de sumisión;
- QA visual integral;
- verificación de archivos de figuras/suplemento;
- gate autoral final.

## 7. Separación respecto de G8

D-201 no inicia, autoriza ni ejecuta G8-F01.

El Plan Experimental puede continuar bajo su propia gobernanza independientemente de las macrofichas FAST editoriales.

## 8. Gate

```text
CURRENT_DRAFTING_PHASE = FAST_FINALIZATION
CURRENT_GATE = FAST_F01_PROMPT_PREPARATION
NEXT_ACTOR = IA_GESTORA_DEL_ARTICULO
NEXT_ACTION = VERSION_AND_AUDIT_FAST_F01_PROMPT

AUTHOR_APPROVAL_GATE = NOT_OPEN
FAST_F01_WRITING_EXECUTION = NOT_AUTHORIZED_YET
FAST_F02 = NOT_AUTHORIZED
FAST_F03 = NOT_AUTHORIZED
```

---

## English

D-201 formally defines the three editorial FAST finalization macro-blocks and separates their naming from Experimental Group 8.

FAST-F01 is limited to scientific presentation and visual structuring from the V037 baseline: three main-body tables and two main-body figures, using approved G5/G6 scientific artifacts and one architecture schematic that introduces no new evidence.

Supplementary G5/G6 artifacts are deferred to FAST-F02. No Experimental G8 task is started or authorized.
