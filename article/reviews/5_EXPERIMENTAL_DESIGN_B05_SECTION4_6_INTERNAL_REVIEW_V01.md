# Revisión interna — Experimental Design B05 / Section 4.6 — V01

## Español

```text
BLOCK = EXPERIMENTAL_DESIGN_B05_SECTION_4_6
ROLE = IA_GESTORA / EDITOR_CIENTIFICO_PRINCIPAL
REVIEW_VERSION = V01
EXECUTION_RESPONSE = article/responses/5_EXPERIMENTAL_DESIGN_B05_SECTION4_6_RESPONSE_V01.md@ee7cd01b652d85791c84eeb26398b224038074ca
SECTION_ARTIFACT = article/sections/experimental_design/Experimental_Design_B05_V01.md@44e72613f9750425446d61987edb383e87feb222
SECTION_ARTIFACT_GIT_BLOB = 1cb53e31f86689a6c886e9f7a5e13ea2f5519d99
BASELINE_MASTER = article/manuscript/ARTICLE_MASTER_V013.md
BASELINE_MASTER_GIT_BLOB = 06beaa052e2f1bcc630647040762fe78d3838a62
CANDIDATE_MD = ARTICLE_MASTER_CANDIDATE_EXPDES_B05_V01.md
CANDIDATE_MD_SHA256_EXPECTED = e7aa7e6706923520a5403ab4dec6713d5a1f7fe6b55edccbde43f2d54b755b97
CANDIDATE_MD_SHA256_OBSERVED = e7aa7e6706923520a5403ab4dec6713d5a1f7fe6b55edccbde43f2d54b755b97
CANDIDATE_MD_GIT_BLOB_EXPECTED = 20105abb745e382b923e4eb43d9a771a722df9e3
CANDIDATE_MD_GIT_BLOB_OBSERVED = 20105abb745e382b923e4eb43d9a771a722df9e3
CANDIDATE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B05_V01.docx
CANDIDATE_DOCX_SHA256_EXPECTED = b1ab0ba79fe8d4dffad57208b2765f18e2c84b80ef4c1dbcfd3ac93eba8f78e2
CANDIDATE_DOCX_SHA256_OBSERVED = b1ab0ba79fe8d4dffad57208b2765f18e2c84b80ef4c1dbcfd3ac93eba8f78e2
SCIENTIFIC_CONTENT = PASS
CLAIM_EVIDENCE = PASS
RESULTS_LEAKAGE = NONE
EN_ES_SEMANTIC_EQUIVALENCE = PASS
MD_SCOPE_DIFFERENTIAL = PASS
DOCX_IDENTITY = PASS
OOXML_ZIP_INTEGRITY = PASS
XML_RELS_PARSE = 14/14 PASS
ZIP_ENTRY_SET = PASS
ZIP_METADATA = PASS
CHANGED_PACKAGE_CONTENT = word/document.xml ONLY
COMMENTS = 40 / PASS
COMMENT_RANGE_START = 40 / PASS
COMMENT_RANGE_END = 40 / PASS
COMMENT_REFERENCES = 40 / PASS
COMMENTS_XML_SHA256 = 04ba296122c3b349bd7b741b49dcf41fdd53b13a8b1e56802d118894b4e37603 / PASS
TRACKED_CHANGES = 0 / PASS
SECTION_4_7_BOUNDARY_EN_ES = PASS
MD_DOCX_SEMANTIC_EQUIVALENCE = PASS
FULL_RENDER = PASS / 47 PAGES
VISUAL_QA = PASS
RESPONSE_SELF_CHECK_CONDITIONAL_CLAIMS = FAIL
MANUSCRIPT_CORRECTION_REQUIRED = NO
DOCX_CORRECTION_REQUIRED = NO
RESPONSE_METADATA_CORRECTION_REQUIRED = YES
OVERALL_B05 = PASS_WITH_BLOCKING_RESPONSE_METADATA_CORRECTION
AUTHOR_APPROVAL_GATE = NOT_OPEN
B06 / SECTION_4_7 = NOT_AUTHORIZED
SECTION_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

## 1. Dictamen científico

La Sección 4.6 cumple el alcance de D-068. El texto mantiene separados los tres objetos de evaluación: ranking de candidatos para RQ1, asociación/trazabilidad documental sobre el Top-3 fijo para RQ2 y evaluación estructural/cualitativa de la explicación controlada para RQ3. RQ4 se conserva únicamente como frontera de validez y robustez y remite a 4.4/4.7.

La auditoría independiente contra las fuentes primarias confirmó la unidad SERIE, las métricas HE2_A, la separación de HE2_B, el carácter descriptivo de los candidate pools, el rol de Phase F sobre un Top-3 ya fijado, la separación entre evidencia exacta NANDINA-8 y contexto parental, la ausencia de autoridad de reranking y la modalidad efectiva de HE4. No se detectaron valores de Results, decisiones HE2/HE5, inferencia, p-values, intervalos, sensibilidad o conclusiones de superioridad dentro de 4.6.

La formulación de la evaluación HE4 es metodológicamente correcta: distingue controles automáticos de la rúbrica cualitativa, no inventa un `automatic_validation_pass` por caso, conserva el criterio `>=12/16 AND no hard violation`, declara la muestra cualitativa congelada y deja explícito que la modalidad ejecutada fue `AI_EXPERT_ROLE / LLM-as-judge`, no human scoring.

## 2. Auditoría claim–evidencia

La prosa respeta las fronteras activas:

- candidate retrieval no se presenta como overall classification accuracy;
- documentary association no se presenta como substantive normative/legal correctness;
- auditability no se presenta como legal correctness;
- la modalidad LLM-as-judge se declara como limitación y no se presenta como validación humana.

Se verificó, sin embargo, una inconsistencia en la **response de ejecución**, no en el manuscrito. `CLAIM_EVIDENCE_MATRIX.md` mantiene C14 —HE4 aporta evidencia sobre estructura, trazabilidad y auditabilidad bajo su protocolo— en estado `CONDITIONAL`, utilizable solo con límites explícitos. La Sección 4.6.3 usa precisamente ese claim de forma correctamente acotada al afirmar que las puntuaciones permiten analizar estructura, trazabilidad, verificabilidad y auditabilidad bajo el esquema de evaluación por IA, e inmediatamente excluye validación humana, corrección jurídica, decisión oficial y reconstrucción causal fiel.

Por tanto, la declaración de la response:

```text
CONDITIONAL_CLAIMS_USED = NONE
```

es incorrecta. Debe registrar C14 como claim condicional utilizado **con sus límites explícitos satisfechos**. Este defecto no exige modificar la Sección 4.6, el master Markdown candidato ni el DOCX candidato.

## 3. Auditoría de artefactos acumulativos

La identidad del Markdown candidato coincide exactamente con la reportada. La comparación diferencial contra V013 confirma que solo fueron sustituidos los bloques autorizados 4.6–4.6.3 en inglés y español; 1–4.5 y 4.7+ permanecen sin cambios de contenido.

El DOCX candidato coincide con el SHA-256 declarado. La auditoría OOXML confirmó integridad ZIP, parseo de 14/14 XML/RELS, cero cambios controlados, 40 comentarios con sus 40 starts/ends/references y conservación de `comments.xml`. Frente al baseline B04 V02, solo cambió `word/document.xml`; el conjunto de entradas y los metadatos ZIP permanecen preservados. La frontera 4.7 se conserva en ambos idiomas.

El render completo produjo 47 páginas. La inspección visual no detectó clipping, truncamiento, superposición ni pérdida material de formato.

## 4. Decisión de gate

El contenido científico y los candidatos acumulativos B05 V01 son técnicamente válidos y **no deben reescribirse**. El único bloqueo es la metadata de autocontrol de la response V01.

Se requiere una corrección atómica de response que registre C14 como claim condicional utilizado con limitaciones satisfechas. Hasta versionar y auditar esa corrección:

```text
B05_SCIENTIFIC_CONTENT = PASS
B05_MD_DOCX = PASS
B05_RESPONSE_METADATA = CORRECTION_REQUIRED
AUTHOR_APPROVAL_GATE = NOT_OPEN
B06 / SECTION_4_7 = NOT_AUTHORIZED
SECTION_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

---

## English

```text
BLOCK = EXPERIMENTAL_DESIGN_B05_SECTION_4_6
ROLE = MANAGING_AI / PRINCIPAL_SCIENTIFIC_EDITOR
REVIEW_VERSION = V01
EXECUTION_RESPONSE = article/responses/5_EXPERIMENTAL_DESIGN_B05_SECTION4_6_RESPONSE_V01.md@ee7cd01b652d85791c84eeb26398b224038074ca
SECTION_ARTIFACT = article/sections/experimental_design/Experimental_Design_B05_V01.md@44e72613f9750425446d61987edb383e87feb222
SCIENTIFIC_CONTENT = PASS
CLAIM_EVIDENCE = PASS
RESULTS_LEAKAGE = NONE
EN_ES_SEMANTIC_EQUIVALENCE = PASS
MD_SCOPE_DIFFERENTIAL = PASS
DOCX_IDENTITY = PASS
OOXML_ZIP_INTEGRITY = PASS
XML_RELS_PARSE = 14/14 PASS
COMMENTS = 40 / PASS
TRACKED_CHANGES = 0 / PASS
FULL_RENDER = PASS / 47 PAGES
VISUAL_QA = PASS
RESPONSE_SELF_CHECK_CONDITIONAL_CLAIMS = FAIL
MANUSCRIPT_CORRECTION_REQUIRED = NO
DOCX_CORRECTION_REQUIRED = NO
RESPONSE_METADATA_CORRECTION_REQUIRED = YES
OVERALL_B05 = PASS_WITH_BLOCKING_RESPONSE_METADATA_CORRECTION
AUTHOR_APPROVAL_GATE = NOT_OPEN
B06 / SECTION_4_7 = NOT_AUTHORIZED
SECTION_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

The Section 4.6 manuscript content passes independent scientific, evidence, scope, bilingual-equivalence, and Results-leakage review. The cumulative Markdown and DOCX candidates also pass identity, differential-scope, OOXML, comment-preservation, tracked-change, semantic-equivalence, and full-render checks.

One response-metadata inconsistency remains. The active claim–evidence matrix classifies C14—HE4 evidence about structure, traceability, and auditability under its evaluation protocol—as `CONDITIONAL`, permitted only with explicit limitations. Section 4.6.3 uses that bounded claim correctly and immediately states the required limitations. Therefore the execution response self-check `CONDITIONAL_CLAIMS_USED = NONE` is false; C14 must be recorded as a conditional claim used with its conditions satisfied.

This is a response-only correction. No scientific rewrite, Markdown-candidate change, or DOCX-candidate change is authorized or required. Author approval remains closed until the corrected response is versioned and independently checked. Section 4.7, Section 4.8, and Results remain unauthorized.