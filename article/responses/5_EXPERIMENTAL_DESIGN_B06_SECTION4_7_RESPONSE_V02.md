# Respuesta — Experimental Design B06 / Section 4.7 — V02

## Español

```text
BLOCK = EXPERIMENTAL_DESIGN_B06_SECTION_4_7
BLOCK_REVISION = V02 / NARROW_METHODS_CORRECTION
ROLE = IA_REDACCION
GOVERNING_PROMPT = article/prompts/5_EXPERIMENTAL_DESIGN_B06_V01_NARROW_METHODS_CORRECTION.md@c14ab0d5aec458870b05307e5bed521d3a104547
GOVERNING_DECISION = D-074
INTERNAL_REVIEW = article/reviews/5_EXPERIMENTAL_DESIGN_B06_SECTION4_7_INTERNAL_REVIEW_V01.md@3d19fbb47fd48abe15520264eea3b29969084295
ORIGINAL_B06_PROMPT = article/prompts/5_EXPERIMENTAL_DESIGN_B06_SECTION4_7.md@f29d10e10c5b94e3c36947cc42031f6dbac4e7bf
CORRECTION_SCOPE = B06-C01 / B06-C02 / B06-C03 / B06-C04 ONLY
AUTHOR_APPROVAL_GATE = NOT_OPEN
SECTION_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### Baselines exactos y control de identidad

La corrección se ejecutó exclusivamente sobre los candidatos B06 V01 auditados. No se regresó a V014/B05 como baseline de edición y el DOCX no fue reconstruido desde Markdown.

```text
BASELINE_MD = ARTICLE_MASTER_CANDIDATE_EXPDES_B06_V01.md
BASELINE_MD_SHA256 = 1ba6d1ea0b0b0c748bf2b4c74e92a53b5ad98852d724157b682c689848bcbc76 / PASS
BASELINE_MD_GIT_BLOB = bda3bb6f9603039c48239deab779eec106588719 / PASS
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B06_V01.docx
BASELINE_DOCX_SHA256 = c58044f2b591eadf9dac0f2cb6bf30624e1c1124d43578bd17bf8c86c0e4dc5e / PASS
PRIOR_COMMENTS = 40
PRIOR_TRACKED_CHANGES = 0
DOCX_RECONSTRUCTED_FROM_MD = NO
```

### Fuentes primarias y procedencia corregida

Se verificaron las fuentes vinculantes del microgate. El artefacto de resultados inferenciales fue utilizado únicamente para identidad y procedencia metodológica; no se trasladaron valores observados, límites de intervalos ni disposiciones de hipótesis a Methods.

```text
G3_ANALYTICAL_CONTRACT_BLOB = 76862c10fd84fd70588da2d65f96dbe3b40914f6
G3_INFERENTIAL_METHODS_BLOB = 6cf424c9cf8aa7371dbbf5b8baaf7305cc66a436
G3_INFERENTIAL_RESULTS_JSON_BLOB = f99b7e46d81b28ca2b7cfce8d24788ad14156dcc
DEVELOPMENT_MAIN = db0d0ad0d8435921a7838db6720eaea86a263763
RESPONSE_V01_WRONG_METHODS_BLOB_RETAINED = NO
RESPONSE_V01_WRONG_RESULTS_BLOB_RETAINED = NO
```

La matriz claim–evidencia vigente mantiene C08, C26 y C27 en `AUTHORIZED` dentro de sus límites descriptivos. Esos límites se preservaron: EXP11A continúa como sensibilidad conjunta tamaño/composición sin efecto causal aislado; EXP11B continúa como sensibilidad descriptiva pareada sin inferencia a una superpoblación de seeds; y EXP12 permanece no estimable. No se utilizaron C28/C29 para trasladar disposiciones HE2/HE5 a Methods.

### Correcciones ejecutadas

**B06-C01.** Se precisó que EVAL contiene 67 clusters DAM para el procedimiento inferencial; un único flujo congelado generó una matriz común `10000 × 67` de índices DAM remuestreados con reemplazo y esa misma matriz se utilizó para todos los resultados inferenciales elegibles. También se explicitó que una DAM seleccionada `m` veces aporta todas sus series con multiplicidad `m`, preservando el estimando ponderado por SERIE y sin sustituirlo por una media no ponderada de medias por DAM.

**B06-C02.** Se precisó que Top-50 es suplementaria, utiliza un intervalo percentil bilateral del 95%, queda fuera de la familia primaria de cinco métricas y no participa en la disposición de hipótesis. La medida de efecto congelada se identificó como la diferencia pareada no estandarizada de contribuciones (`historical - comparator`), sin introducir una medida estandarizada post hoc.

**B06-C03.** Se restituyeron las reglas HE5 omitidas: la prevalencia de descripciones ambiguas/incompletas no es estimable porque la calidad de descripción no fue operacionalizada; la proximidad jerárquica permanece descriptiva mediante `SAME_CHAPTER`, `SAME_HS4` y `SAME_HS6`; y el soporte histórico conserva literalmente `1 DAM`, `2 DAM`, `3-4 DAM` y `5+ DAM`, sin redefinir ningún bucket como `insufficient` ni crear un umbral post hoc de insuficiencia.

**B06-C04.** Se corrigieron exclusivamente en esta response las identidades Git de `g3_inferential_methods_and_checks_v0.1.md` y `g3_inferential_results_v0.1.json` a los blobs verificados indicados arriba.

No se realizó una reescritura general de Section 4.7. Las únicas modificaciones de contenido del manuscrito corresponden a los tres párrafos afectados por B06-C01–C03 en inglés y sus tres espejos semánticos en español.

### Artefactos candidatos

```text
SECTION_ARTIFACT = article/sections/experimental_design/Experimental_Design_B06_V02.md
SECTION_ARTIFACT_COMMIT = b8d19af968cc9b3e0cc205a908a05a5c1549b4c4
SECTION_ARTIFACT_GIT_BLOB = 76d833b0f3c693ddafe997f0202e3893513a35a2
SECTION_ARTIFACT_SHA256 = 71d9c7d8a306ed92ff33712fedb5c32cc93965d455c5fd94f0adaad47a668b32

MASTER_CANDIDATE = ARTICLE_MASTER_CANDIDATE_EXPDES_B06_V02.md
MASTER_CANDIDATE_SHA256 = b04de5aa482561adc970f1c7e06e38f8c932fa110cc86605d2d7a0adb9c6983c
MASTER_CANDIDATE_GIT_BLOB_EXPECTED_FROM_BYTES = e9a17899ccbcb9971e6dfb5002f908e17a0441d9
MASTER_CANDIDATE_GITHUB_MATERIALIZATION = NOT_REQUIRED / LOCAL_AUTHOR_HANDOFF

DOCX_CANDIDATE = ARTICLE_MASTER_CANDIDATE_EXPDES_B06_V02.docx
DOCX_CANDIDATE_SHA256 = 86a0b9517ced0f8c411c04c990bc159d3b4b3f814ad592e669a8f1993cf0f3c2
DOCX_SOURCE = EXACT_B06_V01_BINARY / DIRECT_OOXML_EDIT
DOCX_RECONSTRUCTED_FROM_MD = NO
```

### QA diferencial y DOCX

```text
MD_DIFF_ONLY_4_7_EN_ES = PASS
SECTIONS_1_TO_4_6_PRESERVED = PASS
SECTION_4_8_PLUS_PRESERVED = PASS
EN_ES_EQUIVALENCE = PASS
RESULTS_LEAKAGE = NONE
HYPOTHESIS_DISPOSITION_LEAKAGE = NONE
ZIP_OOXML_INTEGRITY = PASS
ZIP_ENTRY_SET = PRESERVED / 14 OF 14
CHANGED_PACKAGE_CONTENT = word/document.xml ONLY
XML_RELS_PARSE = 14/14 PASS
COMMENTS_XML_SHA256 = 04ba296122c3b349bd7b741b49dcf41fdd53b13a8b1e56802d118894b4e37603 / BYTE_IDENTICAL_TO_BASELINE
COMMENTS = 40
COMMENT_RANGE_START = 40
COMMENT_RANGE_END = 40
COMMENT_REFERENCE = 40
TRACKED_CHANGES = 0
DOCX_PARAGRAPH_COUNT = 446 / 446
DOCX_CHANGED_PARAGRAPH_INDICES = [162, 163, 165, 382, 383, 385]
MD_DOCX_SEMANTIC_EQUIVALENCE = PASS
FULL_DOCX_RENDER = PASS / 49 OF 49 PAGES INSPECTED
VISUAL_QA = PASS / NO CLIPPING, TRUNCATION, OVERLAP OR MATERIAL FORMAT LOSS
```

No se modificaron Sections 1–4.6, Section 4.8 ni contenido posterior. No se introdujeron valores observados, p-values, nuevas pruebas, nuevas medidas de efecto, cambios de dirección de contraste, cambios de seed/réplicas/multiplicidad, disposiciones HE2/HE5, novelty ni final gap.

---

## English

```text
BLOCK = EXPERIMENTAL_DESIGN_B06_SECTION_4_7
BLOCK_REVISION = V02 / NARROW_METHODS_CORRECTION
GOVERNING_PROMPT = article/prompts/5_EXPERIMENTAL_DESIGN_B06_V01_NARROW_METHODS_CORRECTION.md@c14ab0d5aec458870b05307e5bed521d3a104547
GOVERNING_DECISION = D-074
CORRECTION_SCOPE = B06-C01 / B06-C02 / B06-C03 / B06-C04 ONLY
BASELINE_MD_SHA256 = 1ba6d1ea0b0b0c748bf2b4c74e92a53b5ad98852d724157b682c689848bcbc76
BASELINE_DOCX_SHA256 = c58044f2b591eadf9dac0f2cb6bf30624e1c1124d43578bd17bf8c86c0e4dc5e
G3_INFERENTIAL_METHODS_BLOB = 6cf424c9cf8aa7371dbbf5b8baaf7305cc66a436
G3_INFERENTIAL_RESULTS_JSON_BLOB = f99b7e46d81b28ca2b7cfce8d24788ad14156dcc
```

The correction used only the audited B06 V01 Markdown and DOCX candidates as editing baselines. B06-C01 now states the 67 DAM clusters, the single shared `10000 × 67` resampling matrix, and multiplicity handling for all series within a repeatedly sampled DAM while retaining the series-weighted estimand. B06-C02 now states the supplementary Top-50 two-sided 95% percentile interval and its non-decision role, together with the frozen unstandardized paired contribution difference and the absence of a post-hoc standardized effect measure. B06-C03 restores the frozen HE5 methodological statuses for non-operationalized description quality, descriptive hierarchy-proximity categories, and literal historical-support buckets without an insufficiency threshold. B06-C04 corrects the two source-identity blobs in this response.

No scientific scope was expanded. C08, C26, and C27 remain authorized only within their established descriptive limits. No observed Results, p-values, new tests, new effect measures, HE2/HE5 dispositions, Section 4.8 content, novelty claim, or final-gap claim was introduced.

```text
MD_DIFF_ONLY_4_7_EN_ES = PASS
SECTIONS_1_TO_4_6_PRESERVED = PASS
SECTION_4_8_PLUS_PRESERVED = PASS
EN_ES_EQUIVALENCE = PASS
RESULTS_LEAKAGE = NONE
HYPOTHESIS_DISPOSITION_LEAKAGE = NONE
ZIP_OOXML_INTEGRITY = PASS
ZIP_ENTRY_SET = PRESERVED / 14 OF 14
CHANGED_PACKAGE_CONTENT = word/document.xml ONLY
COMMENTS = 40
COMMENT_RANGE_START = 40
COMMENT_RANGE_END = 40
COMMENT_REFERENCE = 40
TRACKED_CHANGES = 0
MD_DOCX_SEMANTIC_EQUIVALENCE = PASS
FULL_DOCX_RENDER = PASS / 49 OF 49 PAGES INSPECTED
VISUAL_QA = PASS
```

```text
B06_CORRECTIONS = B06-C01 / B06-C02 / B06-C03 / B06-C04 COMPLETED_PENDING_GESTORA_AUDIT
SCIENTIFIC_SCOPE_EXPANDED = NO
AUTHOR_APPROVAL_GATE = NOT_OPEN
SECTION_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```
