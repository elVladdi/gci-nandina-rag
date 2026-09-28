# Prompt — Results B03 / Section 5.3 Documentary evidence retrieval

## Español

### Rol

Actúa como **IA de Redacción científica**. Ejecuta exclusivamente Results B03 / Section 5.3 — **Documentary evidence retrieval** sobre el master acumulativo canónico. No avances a Section 5.4 ni a ninguna sección posterior.

Este prompt opera bajo MWDP v1.0, SPCCR, D-021/D-022/D-027/D-035, D-098 y D-099. `CLAIM_EVIDENCE_MATRIX.md`, `SOURCE_REGISTRY.md`, `ARTICLE_STATUS.md`, `ARTICLE_WRITING_PLAN.md` y `STYLE_GUIDE.md` permanecen vinculantes.

### 1. Baselines exactos obligatorios

```text
BASELINE_MD = article/manuscript/ARTICLE_MASTER_V018.md
BASELINE_MD_SHA256 = 6b36a1260fadadce350d222fdbe580982eb3e3be39a117d18143eaa43f72fc54
BASELINE_MD_GIT_BLOB = d392bdc2ae139ab692637c8c3a42ff6804f4d41a

BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_RESULTS_B02_V02.docx
BASELINE_DOCX_SHA256 = 3e27fd12997f581ab55c1b5ac16a28d45b28fa3896989b75da50792e3763e9e9
COMMENTS = 40 / PRESERVE
TRACKED_CHANGES = 0 / PRESERVE
```

Verifica ambas identidades antes de editar. Si alguna no coincide, detente con `BLOCKED_BASELINE_IDENTITY_MISMATCH`.

No reconstruyas el DOCX desde Markdown. Edita directamente el binario Word exacto B02 V02 y preserva comentarios, anchors, estilos, tablas, captions y OOXML heredado.

### 2. Snapshot y fuentes experimentales obligatorias

Usa únicamente el snapshot congelado:

```text
EXPERIMENTAL_REPOSITORY = elVladdi/gci-nandina-rag
SOURCE_SNAPSHOT = db0d0ad0d8435921a7838db6720eaea86a263763
EXPERIMENT = EXP-04-F
EVAL_CASES = 1056
CANDIDATE_SLOTS = 3168
```

Reconsulta directamente estas fuentes:

```text
SOURCE_METRICS = outputs/evaluation/historical_normative_integration_data_aduanas_clase87_v0.2/integration_metrics.json
SOURCE_METRICS_GIT_BLOB = 3fddeba15d080468001b1a855749ab23b1f0f0fb

SOURCE_EVIDENCE_COVERAGE = outputs/evaluation/historical_normative_integration_data_aduanas_clase87_v0.2/integration_evidence_coverage.json
SOURCE_EVIDENCE_COVERAGE_GIT_BLOB = f8a746933655864cda005f14b41938ae750ec9e5

SOURCE_RANKING_INVARIANCE = outputs/evaluation/historical_normative_integration_data_aduanas_clase87_v0.2/integration_ranking_invariance.json
SOURCE_RANKING_INVARIANCE_GIT_BLOB = b295b399d80eee5fb21d1fd582cccae9afef4bdd

SOURCE_LABEL_LEAKAGE = outputs/evaluation/historical_normative_integration_data_aduanas_clase87_v0.2/integration_label_leakage_audit.json
SOURCE_LABEL_LEAKAGE_GIT_BLOB = cad4b3c5daee8988ecd56a38d6150d98cdd96d94

SOURCE_COMPATIBILITY = outputs/evaluation/historical_normative_integration_data_aduanas_clase87_v0.2/integration_compatibility.json
SOURCE_COMPATIBILITY_GIT_BLOB = 1d9070daea5875f47d9a10cbe714880fc9a06bf2
```

No sustituyas estas fuentes por artefactos antiguos, outputs pre-correctivos, ramas mutables, literatura ni inferencias tuyas.

### 3. Función científica de §5.3

Section 5.3 debe reportar exclusivamente el resultado de RQ2: **cobertura/asociación documental identificable para el Top-3 histórico fijo, trazabilidad de esa asociación y preservación del ranking histórico**.

Debe quedar claro que:

1. el Top-3 ya estaba fijado antes de esta etapa;
2. la evidencia documental se asocia a los candidatos existentes;
3. la asociación documental no inserta, elimina, sustituye ni reordena candidatos;
4. las métricas de coverage/traceability no son métricas de legal correctness ni de classification accuracy.

### 4. Ground truth congelado — asociación exacta

Reporta:

```text
EXACT_NANDINA8_EVIDENCE = 3168 / 3168 = 100.00%
CASE_ALL_TOP3_EXACT_EVIDENCE = 1056 / 1056 = 100.00%

RANK_1_EXACT_EVIDENCE = 1056 / 1056 = 100.00%
RANK_2_EXACT_EVIDENCE = 1056 / 1056 = 100.00%
RANK_3_EXACT_EVIDENCE = 1056 / 1056 = 100.00%
```

Puedes expresar el resultado de forma compacta: todos los 3,168 slots del Top-3 tuvieron asociación exacta NANDINA-8 y los 1,056 casos tuvieron evidencia exacta para los tres candidatos.

No describas este 100% como:

- 100% de corrección normativa;
- 100% de precisión legal;
- validación jurídica;
- evidencia de que el candidato es correcto;
- accuracy del sistema.

### 5. Contexto jerárquico, precedente y trazabilidad

Reporta de forma descriptiva:

```text
HS6_CONTEXT = 2168 / 3168 = 68.43%
HS4_CONTEXT = 3168 / 3168 = 100.00%
CHAPTER_CONTEXT = 3168 / 3168 = 100.00%
HISTORICAL_PRECEDENT_COVERAGE = 3168 / 3168 = 100.00%
TRACEABILITY_COMPLETE = 3168 / 3168 = 100.00%
```

Mantén explícita la distinción:

```text
HS6/HS4/CHAPTER = HIERARCHICAL_PARENT_CONTEXT
EXACT_NANDINA8 = CANDIDATE_LEVEL_EXACT_DOCUMENTARY_ASSOCIATION
```

La disponibilidad parcial de HS6 no reduce el resultado `EXACT_NANDINA8_EVIDENCE = 3168/3168`; son objetos distintos.

### 6. Invariancia del ranking histórico

Debe reportarse que la asociación documental preservó completamente el ranking histórico:

```text
RANKING_INVARIANCE_CASES = 1056 / 1056 = 100.00%
TOP1_UNCHANGED = TRUE
TOP3_UNCHANGED = TRUE
POSITIONS_UNCHANGED = TRUE
HISTORICAL_SCORES_UNCHANGED = TRUE
NO_NEW_CANDIDATE_INSERTED = TRUE
NO_CANDIDATE_REMOVED = TRUE
NORMATIVE_SCORE_AFFECTS_ORDER = FALSE
```

La frase permitida debe ser factual, por ejemplo:

> Documentary association preserved the historical Top-3 membership and order in all 1,056 evaluation cases.

No uses `improved`, `validated`, `corrected` o equivalentes para describir el ranking a partir de esta etapa.

### 7. Control de uso de etiqueta

Puede incluirse una oración breve, si mejora la trazabilidad del resultado:

```text
LABEL_USED_FOR_CANDIDATE_SELECTION = FALSE
LABEL_USED_FOR_PRECEDENT_SELECTION = FALSE
LABEL_USED_FOR_EVIDENCE_SELECTION = FALSE
LABEL_USED_FOR_ORDER_OR_FALLBACK = FALSE
LABELS_ONLY_USED_AFTER_CONSTRUCTION_FOR_METRICS = TRUE
```

No lo conviertas en una afirmación de independencia estadística, ausencia total de leakage en todo el estudio o corrección jurídica.

### 8. Claims autorizados y límites vinculantes

```text
C30 = AUTHORIZED
C31 = AUTHORIZED
C32 = AUTHORIZED
C33 = AUTHORIZED
C34 = AUTHORIZED

C12 = PROHIBITED
C18 = PROHIBITED
C21 = AUTHORIZED_WITH_LIMITS
```

C30-C34 están registrados en `article/CLAIM_EVIDENCE_MATRIX.md` y rigen B03.

La ejecución primaria utilizó el corpus congelado derivado de Decisión 885. El drift respecto de Decisión 906 ya está documentado en Methods/Validity. En B03 basta una delimitación corta de que estas métricas describen asociación dentro del corpus congelado; **no desarrolles aquí el análisis de drift**, que corresponde a sensibilidad/Discussion cuando el gate lo permita.

### 9. Qué NO pertenece a B03

No incluir:

- HE4 o resultados de explicación;
- LLM-as-judge;
- automatic explanation validation;
- auditable-case scores;
- inferencia, bootstrap, CI, p-values o HE2;
- EXP11A, EXP11B, Attempt06 o EXP12;
- HE5;
- literatura o comparación cross-study;
- Discussion;
- `FINAL_GAP` o `NOVELTY`;
- afirmaciones de legal/substantive normative correctness;
- generalización empírica fuera de Chapter 87.

### 10. Forma recomendada de §5.3

Redacta una subsección concisa, orientada a resultados y sin cronología experimental:

1. abre con la cobertura exacta 3168/3168 y 1056/1056;
2. reporta contexto jerárquico + precedente/trazabilidad;
3. cierra con invariancia del Top-3/ranking y la frontera de interpretación.

No es obligatorio añadir tabla. Usa tabla solo si mejora materialmente la lectura; de hacerlo, debe ser compacta y no duplicar todos los valores en prosa. No inventes numeración: deriva cualquier número de tabla de la secuencia real del master.

Evita abstracciones como `complete success`, `perfect legal coverage`, `validated evidence` o `full correctness`. Prefiere los objetos medidos concretos: exact documentary association, hierarchical context, precedent coverage, traceability, ranking invariance.

En el espejo español evita calcos innecesarios. Conserva únicamente denominaciones técnicas que aporten precisión y traduce `Section` como `Sección`.

### 11. Alcance diferencial acumulativo

Solo puede sustituirse el placeholder de Section 5.3 en Part I English y Part II Spanish.

```text
SECTIONS_1_TO_5_2 = PRESERVE
SECTION_5_3 = DRAFT_THIS_BLOCK_ONLY
SECTIONS_5_4_TO_5_7 = PRESERVE_PLACEHOLDERS
DISCUSSION = PRESERVE_PLACEHOLDERS
CONCLUSION = PRESERVE_PLACEHOLDERS
END_MATTER = PRESERVE
NO_NEW_LITERATURE = TRUE
NO_SCOPE_EXPANSION = TRUE
```

### 12. D-035 — entrega timeout-safe

```text
BASE64_MANUAL = PROHIBITED
CHUNKING = PROHIBITED
FRAGMENTATION = PROHIBITED
REASSEMBLY = PROHIBITED
DIRECT_GITHUB_MATERIALIZATION_OF_LARGE_MASTER = DO_NOT_ATTEMPT
REAL_FILE_HANDOFF_MD_DOCX_TO_AUTHOR = REQUIRED
```

Versiona en GitHub solo el artefacto pequeño de sección y la response. Entrega el MD acumulativo y DOCX acumulativo como archivos reales al autor.

### 13. Artefactos obligatorios

Genera exactamente:

1. `article/sections/results/Results_B03_V01.md`;
2. `ARTICLE_MASTER_CANDIDATE_RESULTS_B03_V01.md`;
3. `ARTICLE_MASTER_CANDIDATE_RESULTS_B03_V01.docx`;
4. `article/responses/6_RESULTS_B03_SECTION5_3_RESPONSE_V01.md`.

### 14. QA obligatorio

La response debe registrar como mínimo:

```text
PROTOCOL_READ = PASS
BLOCK = RESULTS_B03_SECTION_5_3
SOURCE_SNAPSHOT = db0d0ad0d8435921a7838db6720eaea86a263763
SOURCE_METRICS_GIT_BLOB = 3fddeba15d080468001b1a855749ab23b1f0f0fb
SOURCE_EVIDENCE_COVERAGE_GIT_BLOB = f8a746933655864cda005f14b41938ae750ec9e5
SOURCE_RANKING_INVARIANCE_GIT_BLOB = b295b399d80eee5fb21d1fd582cccae9afef4bdd
SOURCE_LABEL_LEAKAGE_GIT_BLOB = cad4b3c5daee8988ecd56a38d6150d98cdd96d94
SOURCE_COMPATIBILITY_GIT_BLOB = 1d9070daea5875f47d9a10cbe714880fc9a06bf2
SOURCE_RECHECK = PASS
BASELINE_MD_SHA256 = 6b36a1260fadadce350d222fdbe580982eb3e3be39a117d18143eaa43f72fc54
BASELINE_MD_GIT_BLOB = d392bdc2ae139ab692637c8c3a42ff6804f4d41a
BASELINE_DOCX_SHA256 = 3e27fd12997f581ab55c1b5ac16a28d45b28fa3896989b75da50792e3763e9e9
SECTION_5_3_ONLY_DIFF = PASS
SECTIONS_1_TO_5_2_PRESERVED = PASS
SECTIONS_5_4_PLUS_PRESERVED = PASS
NUMERICAL_CONTENT = PASS
ASSOCIATION_VS_CORRECTNESS_BOUNDARY = PASS
RANKING_INVARIANCE_BOUNDARY = PASS
NO_EXPLANATION_RESULT_LEAKAGE = PASS
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

### 15. Exit

Cierra con:

```text
RESULTS_B03_V01_EXECUTION = COMPLETED_PENDING_GESTORA_AUDIT
AUTHOR_APPROVAL_GATE = NOT_OPEN
RESULTS_B04_PLUS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

En chat responde únicamente en español con la ruta+commit exactos de la response y entrega los candidatos acumulativos MD/DOCX como archivos reales. Detente después de B03.

---

## English

Draft only Results B03 / Section 5.3 from the exact V018 Markdown and approved B02 V02 DOCX baselines. Recheck the frozen EXP-04-F documentary-integration artifacts at `main@db0d0ad0d8435921a7838db6720eaea86a263763`. Report exact NANDINA-8 documentary association coverage, hierarchical parent-context availability, precedent coverage, candidate-level traceability, and historical Top-3/ranking invariance. Keep association/coverage strictly separate from substantive normative or legal correctness, preserve the Decision-885 frozen-corpus boundary, introduce no explanation or inferential results, preserve all content outside §5.3, apply D-035 timeout-safe handoff, and stop after B03.