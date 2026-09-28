# Prompt — Results B02 / Section 5.2 Candidate retrieval performance

## Español

### Rol

Actúa como **IA de Redacción científica**. Ejecuta exclusivamente Results B02 / Section 5.2 — **Candidate retrieval performance** sobre el master acumulativo canónico. No avances a Section 5.3 ni a ninguna sección posterior.

Este prompt opera bajo MWDP v1.0, SPCCR, D-021/D-022/D-027/D-035, D-091 y D-092. `CLAIM_EVIDENCE_MATRIX.md`, `SOURCE_REGISTRY.md`, `ARTICLE_STATUS.md` y `ARTICLE_WRITING_PLAN.md` permanecen vinculantes.

### 1. Baselines exactos obligatorios

```text
BASELINE_MD = article/manuscript/ARTICLE_MASTER_V017.md
BASELINE_MD_SHA256 = 6027785ac8f5018920b1bd714f01e57050447cb705d0e9f516a325a4416a6318
BASELINE_MD_GIT_BLOB = 35edb134f3d060bad4257d314cf415d9ecf17b6c

BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_RESULTS_B01_V01.docx
BASELINE_DOCX_SHA256 = f872a6ed145c5f7759dbfabf03e19d0d87aae2f0838c4b02969139c08585841f
COMMENTS = 40 / PRESERVE
TRACKED_CHANGES = 0 / PRESERVE
```

Verifica las identidades antes de editar. Si no coinciden, detente con `BLOCKED_BASELINE_IDENTITY_MISMATCH`.

No reconstruyas el DOCX desde Markdown. Edita directamente el binario Word exacto y preserva comentarios, anchors, estilos, tablas, captions y OOXML heredado.

### 2. Snapshot y fuentes experimentales obligatorias

Usa únicamente el snapshot congelado:

```text
EXPERIMENTAL_REPOSITORY = elVladdi/gci-nandina-rag
FROZEN_DEVELOPMENT_SNAPSHOT = db0d0ad0d8435921a7838db6720eaea86a263763
EVAL_N = 1056
```

Reconsulta directamente estas cuatro fuentes:

```text
SOURCE_HIST = outputs/evaluation/historical_retrieval_data_aduanas_clase87_v0.2/historical_metrics.json
SOURCE_HIST_GIT_BLOB = a43893eca3dd756a1ff11935a9cf55afb728e8f4

SOURCE_FLAT = outputs/evaluation/normative_bm25_flat_corrective_decision906_v0.5/normative_flat_metrics.json
SOURCE_FLAT_GIT_BLOB = 922ecbee8316ee36cd8a53d3ac52f79fac4cd3ed

SOURCE_HIER = outputs/evaluation/normative_bm25_hierarchical_corrective_decision906_v0.5/normative_hierarchical_metrics.json
SOURCE_HIER_GIT_BLOB = 780a005130d1ad68867b290b832c394f8f488a23

SOURCE_D1A = outputs/evaluation/d1a_corrective_0b05c_v0.5/d1a_metrics.json
SOURCE_D1A_GIT_BLOB = 73e062b927d059a9f4e52caab7b785eafb6f2e01
```

No sustituyas estas fuentes por artefactos antiguos, ramas mutables, resultados pre-correctivos o literatura.

### 3. Función científica de §5.2

Section 5.2 debe reportar **desempeño descriptivo observado de recuperación/ranking de candidatos** para RQ1 en el EVAL común de 1,056 SERIE.

Debe distinguir claramente:

1. el ranking histórico H100, que constituye la fuente de candidatos del flujo primario;
2. flat normative BM25, hierarchical normative BM25 y D1a, que son comparadores de evaluación;
3. early-ranking performance frente a deep coverage descriptiva.

No describas los comparadores como componentes que reemplazan el ranking histórico del framework.

### 4. Early-ranking ground truth congelado

Reporta únicamente estos valores:

```text
HISTORICAL_BM25_H100
Top-1  = 538/1056 = 50.9469696969697%
Top-3  = 709/1056 = 67.14015151515152%
Top-5  = 806/1056 = 76.32575757575758%
Top-10 = 941/1056 = 89.10984848484848%
Top-50 = 1047/1056 = 99.14772727272727%
MRR@100 = 0.6297077493524843

FLAT_NORMATIVE_BM25
Top-1  = 29/1056 = 2.746212121212121%
Top-3  = 54/1056 = 5.113636363636364%
Top-5  = 65/1056 = 6.15530303030303%
Top-10 = 69/1056 = 6.534090909090909%
Top-50 = 74/1056 = 7.007575757575758%
MRR@100 = 0.04229731726741296

HIERARCHICAL_NORMATIVE_BM25
Top-1  = 28/1056 = 2.6515151515151514%
Top-3  = 55/1056 = 5.208333333333334%
Top-5  = 66/1056 = 6.25%
Top-10 = 69/1056 = 6.534090909090909%
Top-50 = 96/1056 = 9.090909090909092%
MRR@100 = 0.041971783226435376

D1A_TEXT2TRADE_INSPIRED_MNRL
Top-1  = 1/1056 = 0.0946969696969697%
Top-3  = 11/1056 = 1.0416666666666665%
Top-5  = 54/1056 = 5.113636363636364%
Top-10 = 188/1056 = 17.803030303030305%
Top-50 = 331/1056 = 31.34469696969697%
MRR@100 = 0.038087139731859634
```

En la prosa o tabla puedes redondear Top-k a dos decimales; conserva MRR con precisión suficiente para distinguir los métodos (por ejemplo, 0.630, 0.042, 0.042 y 0.038, o mayor precisión si mejora la lectura).

La interpretación descriptiva permitida es:

> En el EVAL fijo, historical BM25 H100 presentó los mayores valores observados en todas las métricas early-ranking listadas y en Top-50 suplementario.

No uses `significantly`, `statistically superior`, `proved`, `best overall`, `SOTA` ni equivalentes inferenciales/cross-study.

### 5. Deep coverage descriptivo

Para hierarchical normative BM25 puede reportarse:

```text
Exact Recall@100 = 107/1056 = 10.132575757575758%
Exact Recall@200 = 321/1056 = 30.39772727272727%
Pool@200 = 321/1056 = 30.39772727272727%
```

Presenta esto como profundidad/cobertura descriptiva separada de early ranking.

No reportes aún:

- `Recall@200 - Recall@100` como contraste inferencial;
- bootstrap;
- intervalos de confianza;
- multiplicidad;
- disposición HE2_B.

Todo ello corresponde a §5.6.

### 6. Tabla recomendada

Se recomienda **una tabla compacta** para Top-1/3/5/10/50 y MRR@100 de los cuatro métodos, porque reduce repetición numérica en prosa.

Si se usa:

- deriva el número de tabla de la secuencia real del master; no inventes numeración;
- deja claro en caption/nota que Top-50 es suplementario;
- identifica los tres métodos no históricos como comparadores;
- no incluyas CI ni símbolos de significancia;
- no dupliques exhaustivamente todos los números en la prosa.

La deep coverage jerárquica puede quedar en una frase separada y no requiere una segunda tabla.

### 7. Límites semánticos obligatorios

```text
C04 = AUTHORIZED
C05 = AUTHORIZED
C28_DISPOSITION = DO_NOT_USE_IN_B02
OVERALL_CLASSIFICATION_ACCURACY = PROHIBITED_TERM_FOR_THESE_METRICS
LEGAL_CORRECTNESS = NOT_MEASURED
EMPIRICAL_GENERALIZATION_BEYOND_CHAPTER_87 = NOT_SUPPORTED
```

Los resultados son candidate-retrieval/ranking performance sobre un benchmark offline fijo de Chapter 87. No implican decisión jurídica, clasificación vinculante ni desempeño operacional.

### 8. Qué NO pertenece a B02

No incluir:

- CI, bootstrap, p-values, significance o hypothesis disposition;
- diferencias historical-minus-comparator como resultados inferenciales;
- `HE2 = SUPPORTED`;
- Phase-E pools;
- EXP11A, EXP11B, Attempt06 como sensibilidad o EXP12;
- HE5;
- evidencia documental del Top-3;
- HE4 / explicación / LLM-as-judge;
- literatura o comparación cross-study;
- Discussion;
- `FINAL_GAP` o `NOVELTY`.

Sections 5.3–5.7, Discussion, Conclusion y end matter deben permanecer exactamente como placeholders heredados.

### 9. Estilo de Results

- Abre con el resultado histórico principal, no con la cronología experimental.
- Usa `candidate retrieval`, `candidate ranking`, `Top-k hit rate` o terminología equivalente precisa.
- Evita abstracciones como `strong performance` o `clear superiority` cuando una cifra concreta puede expresarse directamente.
- Explica en una sola frase que los comparadores no sustituyen el ranking histórico del pipeline primario.
- Reserva la interpretación inferencial para §5.6 y la interpretación científica amplia para Discussion.
- Mantén equivalencia semántica estricta EN/ES.

### 10. Alcance diferencial acumulativo

Solo puede sustituirse el placeholder de Section 5.2 en Part I English y Part II Spanish.

```text
SECTIONS_1_TO_5_1 = PRESERVE
SECTION_5_2 = DRAFT_THIS_BLOCK_ONLY
SECTIONS_5_3_TO_5_7 = PRESERVE_PLACEHOLDERS
DISCUSSION = PRESERVE_PLACEHOLDERS
CONCLUSION = PRESERVE_PLACEHOLDERS
END_MATTER = PRESERVE
NO_NEW_LITERATURE = TRUE
NO_SCOPE_EXPANSION = TRUE
```

### 11. D-035 — entrega timeout-safe

El antecedente de timeout en la cadena acumulativa mantiene la política conservadora:

```text
BASE64_MANUAL = PROHIBITED
CHUNKING = PROHIBITED
FRAGMENTATION = PROHIBITED
REASSEMBLY = PROHIBITED
DIRECT_GITHUB_MATERIALIZATION_OF_LARGE_MASTER = DO_NOT_ATTEMPT
REAL_FILE_HANDOFF_MD_DOCX_TO_AUTHOR = REQUIRED
```

Versiona en GitHub solo el artefacto pequeño de sección y la response. Entrega el MD acumulativo y DOCX acumulativo como archivos reales al autor.

### 12. Artefactos obligatorios

Genera exactamente:

1. `article/sections/results/Results_B02_V01.md`;
2. `ARTICLE_MASTER_CANDIDATE_RESULTS_B02_V01.md`;
3. `ARTICLE_MASTER_CANDIDATE_RESULTS_B02_V01.docx`;
4. `article/responses/6_RESULTS_B02_SECTION5_2_RESPONSE_V01.md`.

### 13. QA obligatorio

La response debe registrar como mínimo:

```text
PROTOCOL_READ = PASS
BLOCK = RESULTS_B02_SECTION_5_2
SOURCE_SNAPSHOT = db0d0ad0d8435921a7838db6720eaea86a263763
SOURCE_HIST_BLOB = a43893eca3dd756a1ff11935a9cf55afb728e8f4
SOURCE_FLAT_BLOB = 922ecbee8316ee36cd8a53d3ac52f79fac4cd3ed
SOURCE_HIER_BLOB = 780a005130d1ad68867b290b832c394f8f488a23
SOURCE_D1A_BLOB = 73e062b927d059a9f4e52caab7b785eafb6f2e01
SOURCE_RECHECK = PASS
BASELINE_MD_SHA256 = 6027785ac8f5018920b1bd714f01e57050447cb705d0e9f516a325a4416a6318
BASELINE_DOCX_SHA256 = f872a6ed145c5f7759dbfabf03e19d0d87aae2f0838c4b02969139c08585841f
SECTION_5_2_ONLY_DIFF = PASS
SECTIONS_1_TO_5_1_PRESERVED = PASS
SECTIONS_5_3_PLUS_PRESERVED = PASS
NO_INFERENTIAL_RESULT_LEAKAGE = PASS
NO_HE2_DISPOSITION_LEAKAGE = PASS
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

Si añades tabla, verifica también integridad, anchura, paginación y render de la tabla.

### 14. Exit

Cierra con:

```text
RESULTS_B02_V01_EXECUTION = COMPLETED_PENDING_GESTORA_AUDIT
AUTHOR_APPROVAL_GATE = NOT_OPEN
RESULTS_B03_PLUS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

En chat responde únicamente en español con la ruta+commit exactos de la response y entrega los candidatos acumulativos MD/DOCX como archivos reales. Detente después de B02.

---

## English

Draft only Results B02 / Section 5.2 from the exact V017 Markdown and B01 V01 DOCX baselines. Recheck the four frozen metric artifacts at development snapshot `db0d0ad0d8435921a7838db6720eaea86a263763`. Report descriptive candidate-retrieval performance for historical BM25 H100 and the three corrected comparator families using Top-1/3/5/10, MRR@100 and supplementary Top-50; hierarchical exact Recall@100 and Recall@200/Pool@200 may be reported descriptively. Do not report inference, confidence intervals, HE2 disposition, sensitivities, documentary evidence, explanation results, literature comparison or Discussion. Preserve all content outside §5.2, apply D-035 timeout-safe handoff, and stop after B02.