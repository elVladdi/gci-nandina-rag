# D-087 — Sincronización de ground truth de Results y frontera B01 / Results ground-truth synchronization and B01 boundary

## Español

```text
DECISION_ID = D-087
DATE = 2026-09-27
STATUS = ACTIVE / BINDING
PARENT_DECISION = D-086
PHASE = RESULTS
BLOCK = RESULTS_B01_SECTION_5_1
SECTION = 5.1 DATA_AND_PARTITION_CHECKS
CANONICAL_MASTER = ARTICLE_MASTER_V016
RESULTS_B01 = GROUND_TRUTH_SYNCHRONIZED / PROMPT_PREPARATION_ALLOWED
RESULTS_SECTIONS_5_2_PLUS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

## 1. Decisión

IA Gestora sincronizó de forma independiente el ground truth necesario para abrir exclusivamente Results B01 / Section 5.1 — Data and partition checks. La sincronización usa el snapshot experimental congelado `main@db0d0ad0d8435921a7838db6720eaea86a263763` del repositorio `elVladdi/gci-nandina-rag` y no reabre Experimental Design.

La apertura de B01 autoriza únicamente reportar resultados observados de composición y controles de partición ya materializados y auditados. No autoriza todavía desempeño de retrieval, evidencia documental, explicación, sensibilidades, resultados inferenciales ni disposiciones HE2/HE5.

## 2. Fuentes congeladas para B01

```text
DEVELOPMENT_SNAPSHOT = db0d0ad0d8435921a7838db6720eaea86a263763

SOURCE_A = data/processed/data_aduanas_splits_clase87_v0.2_metadata.json
SOURCE_A_GIT_BLOB = bcb02c9c3493235a6f80991158c5b24fa7c04510

SOURCE_B = outputs/audits/data_aduanas_splits_clase87_v0.2/audit_summary_v0.2.json
SOURCE_B_GIT_BLOB = fb21eb0d8ef77cdedaa32698b854595629ed526d
SOURCE_B_SHA256_RECORDED_BY_SOURCE_A = 79097fcc162cca8690f9382b5e529cfbd8d714575ad7fb96fc044eca2343d027
```

Estos dos artefactos agregados son suficientes para los resultados autorizados en §5.1. Los archivos de detalle permanecen disponibles para trazabilidad, pero B01 no debe introducir resultados adicionales que no estén contenidos en estas fuentes o expresamente congelados aquí.

## 3. Ground truth autorizado para Section 5.1

### 3.1 Composición del benchmark v0.2

```text
TOTAL_CURATED_AND_ASSIGNED_SERIES = 4106
FULL_ASSIGNMENT = TRUE
UNIQUE_ID_UNICO_SOURCE = 4106
UNIQUE_ID_UNICO_OUTPUT = 4106

HISTORICAL_H100 = 2950 SERIES / 28 DAM / 66 CODES
DEVELOPMENT_DEV = 100 SERIES / 6 DAM / 9 CODES
EVALUATION_EVAL = 1056 SERIES / 67 DAM / 42 CODES
```

### 3.2 Independencia entre particiones por identificadores congelados

```text
DAM_OVERLAP_DEV_EVAL = 0
DAM_OVERLAP_DEV_HIST = 0
DAM_OVERLAP_EVAL_HIST = 0

ID_UNICO_OVERLAP_DEV_EVAL = 0
ID_UNICO_OVERLAP_DEV_HIST = 0
ID_UNICO_OVERLAP_EVAL_HIST = 0
```

Estas cifras demuestran separación por DAM e `id_unico` entre las particiones congeladas. No autorizan afirmar independencia estadística de las SERIE dentro de una misma DAM ni ausencia total de similitud textual residual.

### 3.3 Soporte histórico nominal de las clases de evaluación

```text
EVAL_CASES_WITH_HISTORICAL_SUPPORT = 1056 / 1056 = 100.0%
EVAL_CASES_WITHOUT_HISTORICAL_SUPPORT = 0
EVAL_CODES_WITH_HISTORICAL_SUPPORT = 42 / 42
EVAL_CODES_WITHOUT_HISTORICAL_SUPPORT = 0
```

Este resultado significa únicamente que el código de referencia de cada caso de evaluación está representado en H100. No es un resultado Top-k y no implica que el retrieval encuentre ese código en una posición determinada.

### 3.4 Duplicados exactos residuales entre histórico y evaluación

Bajo `exact_normalized_description`:

```text
HIST_EVAL_RIGHT_ROWS = 1056
HIST_EVAL_AFFECTED_ROWS = 35
HIST_EVAL_AFFECTED_PCT = 3.3143939393939394%
HIST_EVAL_SAME_NANDINA_ROWS = 34
HIST_EVAL_DIFFERENT_NANDINA_ROWS = 1
HIST_EVAL_SAME_DAM_ROWS = 0
HIST_EVAL_DIFFERENT_DAM_ROWS = 35

HIST_DEV_AFFECTED_ROWS = 0 / 100
DEV_EVAL_AFFECTED_ROWS = 0 / 1056
```

Los conteos `same_nandina_rows` / `different_nandina_rows` describen asociaciones detectadas bajo el audit y no deben reinterpretarse como evidencia de leakage por DAM, que es cero en v0.2.

### 3.5 Near-duplicates históricos–evaluación

Bajo `token_jaccard_rare_block`:

```text
THRESHOLD_0.90 = 55 / 1056 EVAL ROWS AFFECTED = 5.208333333333334%; 82 PAIRS
THRESHOLD_0.95 = 44 / 1056 EVAL ROWS AFFECTED = 4.166666666666666%; 46 PAIRS
THRESHOLD_0.98 = 37 / 1056 EVAL ROWS AFFECTED = 3.5037878787878785%; 38 PAIRS
```

Estos son diagnósticos de similitud residual. No son filtros de exclusión, no invalidan automáticamente el benchmark y no prueban independencia i.i.d.

## 4. Frontera narrativa de Results B01

Section 5.1 debe:

- reportar observaciones, no repetir extensamente el procedimiento de Methods;
- distinguir separación por DAM/`id_unico` de similitud textual residual;
- presentar el soporte histórico nominal como condición de cobertura de clases, no como desempeño de retrieval;
- evitar causalidad, significancia, generalización externa o conclusiones legales;
- usar `candidate retrieval` cuando corresponda y nunca convertir estos controles en `overall classification accuracy`;
- reservar interpretación amplia para Discussion.

Puede emplearse una tabla compacta de resultados de composición/validación si mejora la legibilidad, siempre que no agregue datos no congelados en esta decisión y que su numeración se derive de la secuencia real del master acumulativo, no se invente.

## 5. Claims y límites

Para B01:

```text
C06 = AUTHORIZED
C07 = CONTEXTUAL_BOUNDARY_ONLY
C16 = PROHIBITED
C18 = PROHIBITED
C28 = NOT_FOR_B01
C29 = NOT_FOR_B01
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

C04/C05, C08, C14, C21–C29 permanecen fuera del alcance de B01 salvo que una cifra sea estrictamente necesaria para evitar una contradicción; en tal caso debe detenerse y escalar a IA Gestora, no incorporarla por inferencia.

## 6. Baselines acumulativos obligatorios

```text
BASELINE_MD = article/manuscript/ARTICLE_MASTER_V016.md
BASELINE_MD_SHA256 = 3c8b64104b11f2e07f85d0275e5ac6c4a96cb0c5cd5b183704949705c8e120a5
BASELINE_MD_GIT_BLOB = e8f9ffddb616b4a7d036f1b57fbe9f18d73613cc

BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B07_V02.docx
BASELINE_DOCX_SHA256 = c9c12609e7aefc5c2b260a967df88d87641252e2be28eab838f984952f48b4de
COMMENTS = 40 / PRESERVE
TRACKED_CHANGES = 0 / PRESERVE
```

El DOCX debe editarse directamente desde el binario exacto; no puede reconstruirse desde Markdown.

## 7. Gate

```text
CURRENT_GATE = RESULTS_B01_PROMPT_PREPARATION
NEXT_ACTOR = IA_GESTORA
NEXT_ACTION = CREATE_AND_REVIEW_RESULTS_B01_PROMPT
RESULTS_B01 = NOT_YET_AUTHORIZED_FOR_EXECUTION
RESULTS_5_2_PLUS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
```

---

## English

D-087 synchronizes the frozen ground truth needed only for Results B01 / Section 5.1. The frozen development snapshot is `db0d0ad0d8435921a7838db6720eaea86a263763`. The controlling aggregate artifacts are `data_aduanas_splits_clase87_v0.2_metadata.json` (Git blob `bcb02c9c3493235a6f80991158c5b24fa7c04510`) and `outputs/audits/data_aduanas_splits_clase87_v0.2/audit_summary_v0.2.json` (Git blob `fb21eb0d8ef77cdedaa32698b854595629ed526d`).

B01 may report only frozen dataset composition, zero cross-partition DAM and `id_unico` overlap, complete nominal historical support for EVAL reference classes, and the exact/near-duplicate diagnostics recorded above. It must not report retrieval performance, HE2/HE5 dispositions, explanation results, sensitivity results, inferential results, legal correctness, or empirical generalization. Section 5.2 and later sections remain unauthorized.