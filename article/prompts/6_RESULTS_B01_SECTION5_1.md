# Prompt — Results B01 / Section 5.1 Data and partition checks

## Español

### Rol

Actúa como **IA de Redacción científica**. Ejecuta exclusivamente Results B01 / Section 5.1 — **Data and partition checks** sobre el master acumulativo canónico. No avances a Section 5.2 ni a ninguna sección posterior.

Este prompt opera bajo MWDP v1.0, SPCCR, D-021/D-022/D-027/D-035, D-086 y D-087. `CLAIM_EVIDENCE_MATRIX.md`, `SOURCE_REGISTRY.md`, `ARTICLE_STATUS.md` y `ARTICLE_WRITING_PLAN.md` permanecen vinculantes.

### 1. Baselines exactos obligatorios

```text
BASELINE_MD = article/manuscript/ARTICLE_MASTER_V016.md
BASELINE_MD_SHA256 = 3c8b64104b11f2e07f85d0275e5ac6c4a96cb0c5cd5b183704949705c8e120a5
BASELINE_MD_GIT_BLOB = e8f9ffddb616b4a7d036f1b57fbe9f18d73613cc

BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B07_V02.docx
BASELINE_DOCX_SHA256 = c9c12609e7aefc5c2b260a967df88d87641252e2be28eab838f984952f48b4de
COMMENTS = 40 / PRESERVE
TRACKED_CHANGES = 0 / PRESERVE
```

Verifica las identidades antes de editar. Si no coinciden, detente con `BLOCKED_BASELINE_IDENTITY_MISMATCH`.

No reconstruyas el DOCX desde Markdown. Edita directamente el binario Word exacto y preserva comentarios, anchors, estilos, tablas heredadas, captions y OOXML no relacionado.

### 2. Fuentes experimentales obligatorias

Usa únicamente el snapshot congelado:

```text
EXPERIMENTAL_REPOSITORY = elVladdi/gci-nandina-rag
FROZEN_DEVELOPMENT_SNAPSHOT = db0d0ad0d8435921a7838db6720eaea86a263763
```

Fuentes primarias agregadas para B01:

```text
SOURCE_A = data/processed/data_aduanas_splits_clase87_v0.2_metadata.json
SOURCE_A_GIT_BLOB = bcb02c9c3493235a6f80991158c5b24fa7c04510

SOURCE_B = outputs/audits/data_aduanas_splits_clase87_v0.2/audit_summary_v0.2.json
SOURCE_B_GIT_BLOB = fb21eb0d8ef77cdedaa32698b854595629ed526d
```

Reconsulta directamente ambas fuentes en el commit congelado. No uses el HEAD mutable de desarrollo para sustituirlas. No uses búsqueda web ni literatura científica en este bloque.

### 3. Función científica de Section 5.1

Section 5.1 debe **reportar los resultados observados que caracterizan el benchmark y verifican las condiciones de partición usadas por los análisis posteriores**. Debe ser Results, no una repetición extensa de Methods.

La secuencia recomendada es:

1. composición final del benchmark v0.2;
2. separación entre particiones por DAM e `id_unico`;
3. soporte histórico nominal de los códigos de referencia de EVAL;
4. similitud textual residual: duplicados exactos y near-duplicates;
5. cierre breve que delimite qué verifican estos controles y qué no verifican.

Mantén la prosa factual y compacta. La interpretación causal, la comparación con literatura y las implicaciones amplias pertenecen a Discussion.

### 4. Resultados autorizados y cifras congeladas

#### 4.1 Composición y asignación

```text
TOTAL_SERIES = 4106
FULL_ASSIGNMENT = TRUE
SOURCE_UNIQUE_ID_UNICO = 4106
OUTPUT_UNIQUE_ID_UNICO = 4106

H100 = 2950 SERIES / 28 DAM / 66 REPRESENTED CODES
DEV = 100 SERIES / 6 DAM / 9 REPRESENTED CODES
EVAL = 1056 SERIES / 67 DAM / 42 REPRESENTED REFERENCE CODES
```

No afirmar que los 66 códigos de H100 agoten Chapter 87.

#### 4.2 Solapamiento entre particiones

```text
DAM_OVERLAP_H100_DEV = 0
DAM_OVERLAP_H100_EVAL = 0
DAM_OVERLAP_DEV_EVAL = 0

ID_UNICO_OVERLAP_H100_DEV = 0
ID_UNICO_OVERLAP_H100_EVAL = 0
ID_UNICO_OVERLAP_DEV_EVAL = 0
```

Reportar como separación de grupos/identificadores entre particiones. No convertirlo en afirmación de independencia estadística entre SERIE dentro de una DAM ni en ausencia de toda similitud textual.

#### 4.3 Soporte histórico nominal

```text
EVAL_CASES_WITH_HISTORICAL_SUPPORT = 1056 / 1056 = 100.0%
EVAL_CASES_WITHOUT_HISTORICAL_SUPPORT = 0
EVAL_CODES_WITH_HISTORICAL_SUPPORT = 42 / 42
EVAL_CODES_WITHOUT_HISTORICAL_SUPPORT = 0
```

La interpretación permitida es únicamente que el código de referencia de cada SERIE evaluada estaba representado en H100. Esto **no es candidate-retrieval performance**, no implica Top-k hit y no debe describirse como accuracy.

#### 4.4 Duplicados exactos cross-partition

Método congelado: `exact_normalized_description`.

```text
H100–EVAL: 35 / 1056 EVAL ROWS = 3.3143939393939394%
SAME_NANDINA_ROWS = 34
DIFFERENT_NANDINA_ROWS = 1
SAME_DAM_ROWS = 0
DIFFERENT_DAM_ROWS = 35

H100–DEV: 0 / 100
DEV–EVAL: 0 / 1056
```

Puedes redondear porcentajes en la prosa a dos decimales (3.31%) preservando los conteos exactos. No llames a estos casos `DAM leakage`: las 35 coincidencias H100–EVAL corresponden a DAM distintas.

#### 4.5 Near-duplicates H100–EVAL

Método congelado: `token_jaccard_rare_block`.

```text
JACCARD >= 0.90: 55 / 1056 EVAL ROWS = 5.208333333333334%; 82 PAIRS
JACCARD >= 0.95: 44 / 1056 EVAL ROWS = 4.166666666666666%; 46 PAIRS
JACCARD >= 0.98: 37 / 1056 EVAL ROWS = 3.5037878787878785%; 38 PAIRS
```

Puedes reportar porcentajes redondeados a 5.21%, 4.17% y 3.50%. Los thresholds son diagnósticos y no filtros de exclusión. No afirmar que el benchmark sea i.i.d. ni que la similitud residual esté eliminada.

### 5. Qué NO pertenece a B01

No incluir:

- Top-1/Top-3/Top-5/Top-10/Top-50 o MRR;
- comparadores flat normative, hierarchical normative o D1a;
- HE2_A, HE2_B o su disposición `SUPPORTED`;
- asociación/coverage normativa del Top-3;
- HE4 o resultados del LLM-as-judge;
- EXP11A, EXP11B, Attempt06 o EXP12;
- HE5 o su disposición `INCONCLUSIVE`;
- bootstrap, intervalos de confianza o inferencia;
- literatura, comparación cross-study o SOTA;
- claims de corrección jurídica o accuracy global;
- generalización empírica fuera de Chapter 87;
- `FINAL_GAP` o `NOVELTY`.

Sections 5.2–5.7, Discussion y Conclusion deben permanecer exactamente como placeholders heredados.

### 6. Estilo de Results

- Usa voz científica directa: `The final v0.2 benchmark contained...`, `No DAM overlap was observed...`.
- Prioriza conteos y proporciones observadas.
- No repitas cómo se construyó el split salvo una frase mínima necesaria para interpretar el resultado.
- No uses abstracciones vagas como `strong validity`, `robust independence` o `clean split` sin definir el control concreto.
- No conviertas un diagnóstico en una conclusión causal.
- El cierre de §5.1 puede señalar que la separación por DAM/identificador coexistió con similitud textual residual; no debe anticipar el efecto de esa similitud sobre métricas que aún no se han reportado.
- Mantén equivalencia semántica estricta EN/ES.

Puede incorporarse **como máximo una tabla compacta** de composición/controles si mejora claramente la lectura. Si se usa, deriva la numeración de la secuencia real del master acumulativo; no inventes un número. Los mismos datos no deben duplicarse exhaustivamente en tabla y prosa.

### 7. Alcance diferencial acumulativo

Solo puede sustituirse el placeholder de Section 5.1 en Part I English y Part II Spanish.

```text
SECTIONS_1_TO_4_8 = PRESERVE
SECTION_5_1 = DRAFT_THIS_BLOCK_ONLY
SECTIONS_5_2_TO_5_7 = PRESERVE_PLACEHOLDERS
DISCUSSION = PRESERVE_PLACEHOLDERS
CONCLUSION = PRESERVE_PLACEHOLDERS
END_MATTER = PRESERVE
NO_NEW_LITERATURE = TRUE
NO_SCOPE_EXPANSION = TRUE
```

### 8. D-035 — entrega timeout-safe

El antecedente de timeout en la cadena acumulativa mantiene la política conservadora de handoff:

```text
BASE64_MANUAL = PROHIBITED
CHUNKING = PROHIBITED
FRAGMENTATION = PROHIBITED
REASSEMBLY = PROHIBITED
DIRECT_GITHUB_MATERIALIZATION_OF_LARGE_MASTER = DO_NOT_ATTEMPT
REAL_FILE_HANDOFF_MD_DOCX_TO_AUTHOR = REQUIRED
```

Versiona en GitHub solo el artefacto pequeño de sección y la response. Entrega el MD acumulativo y DOCX acumulativo como archivos reales al autor.

### 9. Artefactos obligatorios

Genera exactamente:

1. `article/sections/results/Results_B01_V01.md`;
2. `ARTICLE_MASTER_CANDIDATE_RESULTS_B01_V01.md`;
3. `ARTICLE_MASTER_CANDIDATE_RESULTS_B01_V01.docx`;
4. `article/responses/6_RESULTS_B01_SECTION5_1_RESPONSE_V01.md`.

### 10. QA obligatorio

La response debe registrar, como mínimo:

```text
PROTOCOL_READ = PASS
BLOCK = RESULTS_B01_SECTION_5_1
SOURCE_SNAPSHOT = db0d0ad0d8435921a7838db6720eaea86a263763
SOURCE_A_BLOB = bcb02c9c3493235a6f80991158c5b24fa7c04510
SOURCE_B_BLOB = fb21eb0d8ef77cdedaa32698b854595629ed526d
SOURCE_RECHECK = PASS
BASELINE_MD_SHA256 = 3c8b64104b11f2e07f85d0275e5ac6c4a96cb0c5cd5b183704949705c8e120a5
BASELINE_DOCX_SHA256 = c9c12609e7aefc5c2b260a967df88d87641252e2be28eab838f984952f48b4de
SECTION_5_1_ONLY_DIFF = PASS
SECTIONS_1_TO_4_8_PRESERVED = PASS
SECTIONS_5_2_PLUS_PRESERVED = PASS
NO_RETRIEVAL_PERFORMANCE_LEAKAGE = PASS
NO_INFERENTIAL_RESULT_LEAKAGE = PASS
NO_DISCUSSION_LEAKAGE = PASS
EN_ES_EQUIVALENCE = PASS
COMMENTS = 40
COMMENT_RANGE_START = 40
COMMENT_RANGE_END = 40
COMMENT_REFERENCE = 40
TRACKED_CHANGES = 0
ZIP_OOXML_INTEGRITY = PASS
MD_DOCX_SEMANTIC_EQUIVALENCE = PASS
FULL_DOCX_RENDER = PASS
D035_TIMEOUT_SAFE_HANDOFF = PASS
BASE64_MANUAL = NO
CHUNKING = NO
FRAGMENTATION = NO
REASSEMBLY = NO
```

Si añades una tabla, verifica también integridad de tabla, anchura, paginación y render.

### 11. Exit

Cierra con:

```text
RESULTS_B01_V01_EXECUTION = COMPLETED_PENDING_GESTORA_AUDIT
AUTHOR_APPROVAL_GATE = NOT_OPEN
RESULTS_B02_PLUS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

En chat responde únicamente en español con la ruta+commit exactos de la response y entrega los candidatos acumulativos MD/DOCX como archivos reales. Detente después de B01.

---

## English

Draft only Results B01 / Section 5.1 from the exact V016 Markdown and B07 V02 DOCX baselines. Recheck the two frozen v0.2 aggregate artifacts at development snapshot `db0d0ad0d8435921a7838db6720eaea86a263763`. Report only dataset composition, zero cross-partition DAM/`id_unico` overlap, complete nominal historical support of EVAL reference classes, and the frozen exact/near-duplicate diagnostics. Do not report retrieval performance, documentary-evidence results, explanation results, sensitivities, inference, HE2/HE5 dispositions, literature comparison, legal correctness, or generalization. Preserve all content outside §5.1. Apply D-035 timeout-safe handoff and stop after B01.