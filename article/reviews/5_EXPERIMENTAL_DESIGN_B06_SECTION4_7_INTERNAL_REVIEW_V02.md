# Revisión interna — Experimental Design B06 / Section 4.7 — V02

## Español

```text
REVIEW_ID = EXPERIMENTAL_DESIGN_B06_SECTION4_7_INTERNAL_REVIEW_V02
DATE = 2026-09-27
ROLE = IA_GESTORA / EDITOR_CIENTIFICO_PRINCIPAL
BLOCK = EXPERIMENTAL_DESIGN_B06_SECTION_4_7
CANDIDATE_REVISION = V02 / NARROW_METHODS_CORRECTION
SCOPE_DECISION = D-074
EXECUTION_AUTHORIZATION = D-075
CORRECTION_PROMPT = article/prompts/5_EXPERIMENTAL_DESIGN_B06_V01_NARROW_METHODS_CORRECTION.md@c14ab0d5aec458870b05307e5bed521d3a104547
RESPONSE = article/responses/5_EXPERIMENTAL_DESIGN_B06_SECTION4_7_RESPONSE_V02.md@8469a6aa83b85dc64486877106cc6f05115b1751
RESPONSE_GIT_BLOB = 50f12ae688c0459cc396c6337c14e75d119a6128
SECTION_ARTIFACT = article/sections/experimental_design/Experimental_Design_B06_V02.md@b8d19af968cc9b3e0cc205a908a05a5c1549b4c4
SECTION_ARTIFACT_GIT_BLOB = 76d833b0f3c693ddafe997f0202e3893513a35a2
OVERALL_VERDICT = PASS
AUTHOR_APPROVAL_GATE = MAY_OPEN_FOR_B06_V02_ONLY
SECTION_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

## 1. Objeto y criterio de auditoría

Se auditó diferencialmente B06 V02 contra el microgate definido por D-074, autorizado para ejecución por D-075. La revisión se limitó a comprobar el cierre correcto de B06-C01, B06-C02, B06-C03 y B06-C04, la preservación acumulativa de los candidatos Markdown/DOCX B06 V01 y la ausencia de expansión científica o editorial no autorizada.

No se reabrieron Sections 1–4.6, no se evaluó Section 4.8 como contenido redactado y no se autorizó Results.

## 2. Identidad de baselines y candidatos

Los baselines exigidos por D-074/D-075 fueron respetados:

```text
B06_V01_BASELINE_MD_SHA256 = 1ba6d1ea0b0b0c748bf2b4c74e92a53b5ad98852d724157b682c689848bcbc76 / PASS
B06_V01_BASELINE_MD_GIT_BLOB = bda3bb6f9603039c48239deab779eec106588719 / PASS
B06_V01_BASELINE_DOCX_SHA256 = c58044f2b591eadf9dac0f2cb6bf30624e1c1124d43578bd17bf8c86c0e4dc5e / PASS
```

Los candidatos V02 recibidos fueron verificados independientemente:

```text
B06_V02_MASTER_MD = ARTICLE_MASTER_CANDIDATE_EXPDES_B06_V02.md
B06_V02_MASTER_MD_SHA256 = b04de5aa482561adc970f1c7e06e38f8c932fa110cc86605d2d7a0adb9c6983c / PASS
B06_V02_MASTER_MD_GIT_BLOB = e9a17899ccbcb9971e6dfb5002f908e17a0441d9 / PASS
B06_V02_MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B06_V02.docx
B06_V02_MASTER_DOCX_SHA256 = 86a0b9517ced0f8c411c04c990bc159d3b4b3f814ad592e669a8f1993cf0f3c2 / PASS
```

No existe evidencia de retorno a V014/B05 como baseline de edición ni de reconstrucción del Word desde Markdown.

## 3. Cierre de B06-C01

**PASS.** Section 4.7 declara ahora de forma explícita:

- 67 clusters DAM en EVAL para el procedimiento;
- un único flujo aleatorio congelado que genera una matriz común `10000 × 67` de índices DAM con reemplazo;
- reutilización de la misma matriz para todos los resultados inferenciales elegibles;
- multiplicidad `m` de todas las series de una DAM cuando esa DAM aparece `m` veces en una réplica;
- preservación del estimando ponderado por SERIE frente a una media no ponderada de medias por DAM.

La formulación es metodológica, no introduce resultados observados y coincide con el contrato inferencial congelado.

```text
B06-C01 = CLOSED / PASS
```

## 4. Cierre de B06-C02

**PASS.** Section 4.7 declara ahora que:

- Top-50 es suplementaria;
- su incertidumbre se resume con IC percentil bilateral de 95%;
- queda fuera de la familia primaria de cinco métricas y no interviene en la disposición de hipótesis;
- la medida de efecto congelada es la diferencia pareada no estandarizada de contribuciones `historical - comparator`;
- no se introdujo una medida de efecto estandarizada post hoc.

No se trasladaron bounds observados ni p-values.

```text
B06-C02 = CLOSED / PASS
```

## 5. Cierre de B06-C03

**PASS.** La versión V02 restituye los estados metodológicos HE5 requeridos:

- la prevalencia de descripciones ambiguas/incompletas no es estimable porque la calidad de descripción no fue operacionalizada;
- la proximidad jerárquica permanece descriptiva mediante `SAME_CHAPTER`, `SAME_HS4` y `SAME_HS6`;
- el soporte histórico conserva literalmente los buckets `1 DAM`, `2 DAM`, `3-4 DAM` y `5+ DAM`;
- ningún bucket se redefine post hoc como `insufficient` y no se crea un umbral nuevo de insuficiencia;
- estas familias siguen siendo descriptivas y no reciben una nueva prueba inferencial.

EXP12 también permanece no estimable dentro de su alcance congelado.

```text
B06-C03 = CLOSED / PASS
```

## 6. Cierre de B06-C04

**PASS.** La response V02 corrige las dos identidades de procedencia observadas en V01:

```text
G3_INFERENTIAL_METHODS_BLOB = 6cf424c9cf8aa7371dbbf5b8baaf7305cc66a436 / PASS
G3_INFERENTIAL_RESULTS_JSON_BLOB = f99b7e46d81b28ca2b7cfce8d24788ad14156dcc / PASS
```

Los blobs erróneos de la response V01 no fueron retenidos.

La response V02 usa `GOVERNING_DECISION = D-074`. Esta etiqueta se interpreta correctamente como la decisión que define el alcance del microgate. La autorización de ejecución aplicable es D-075. La response identifica el prompt correcto, usa los baselines exactos y fue ejecutada dentro del alcance de D-075; por tanto, esta diferencia de rotulado no constituye defecto material ni requiere nueva corrección.

```text
B06-C04 = CLOSED / PASS
RESPONSE_D074_LABEL = NON_BLOCKING / SCOPE_DECISION
EXECUTION_AUTHORIZATION = D-075 / VERIFIED
```

## 7. Auditoría diferencial Markdown

La comparación byte/textual de los candidatos B06 V01 y V02 confirma que solo cambiaron seis párrafos, todos dentro de Section 4.7: tres en inglés y sus tres espejos semánticos en español.

```text
MD_DIFF_ONLY_SECTION_4_7_EN_ES = PASS
SECTIONS_1_TO_4_6_PRESERVED = PASS
SECTION_4_8_PLUS_PRESERVED = PASS
EN_ES_SEMANTIC_EQUIVALENCE = PASS
RESULTS_LEAKAGE = NONE
HYPOTHESIS_DISPOSITION_LEAKAGE = NONE
SCIENTIFIC_SCOPE_EXPANDED = NO
```

Section 4.8 continúa como placeholder no redactado y Results continúa sin contenido nuevo.

## 8. Auditoría DOCX/OOXML independiente

El DOCX V02 fue auditado directamente contra el DOCX V01 exacto.

```text
ZIP_ENTRY_SET = 14/14 IDENTICAL / PASS
CHANGED_PACKAGE_CONTENT = word/document.xml ONLY / PASS
XML_AND_RELS_PARSE = PASS
COMMENTS = 40 / PRESERVED
COMMENT_IDS = 0-39 / PASS
COMMENT_RANGE_START = 40 / PASS
COMMENT_RANGE_END = 40 / PASS
COMMENT_REFERENCE = 40 / PASS
TRACKED_CHANGES = 0 / PASS
DOCX_PARAGRAPH_COUNT = 446 / 446
DOCX_CHANGED_PARAGRAPH_INDICES = [162, 163, 165, 382, 383, 385] / PASS
```

Los seis párrafos modificados coinciden con las tres correcciones científicas autorizadas en inglés y español. `word/comments.xml` y el resto del paquete permanecen sin cambios de contenido.

## 9. Render y control visual independiente

El DOCX V02 se renderizó de forma completa y se inspeccionaron las 49 páginas. No se observaron clipping, truncamiento, solapamientos, glifos ausentes ni pérdida material de formato.

```text
FULL_DOCX_RENDER = PASS / 49 OF 49 PAGES
VISUAL_QA = PASS
MATERIAL_FORMAT_LOSS = NONE
```

## 10. Control científico y de alcance

La redacción corregida conserva los límites metodológicos vigentes:

```text
PRIMARY_INFERENTIAL_CLUSTER = DAM
PRIMARY_ESTIMAND = SERIES_WEIGHTED
BOOTSTRAP_REPLICATES = 10000
BOOTSTRAP_SEED = 20263001
P_VALUES = NONE
HE2_A_PRIMARY_FAMILY = TOP1 / TOP3 / TOP5 / TOP10 / MRR@100
HE2_A_FAMILYWISE_CONTROL = 99_PERCENT_MARGINAL_CI / BONFERRONI_FWER_95
TOP50 = SUPPLEMENTARY / TWO_SIDED_95_PERCENT_PERCENTILE_CI / NO_HYPOTHESIS_DISPOSITION_ROLE
HE2_B = SINGLE_DEEP_COVERAGE_CONTRAST / TWO_SIDED_95_PERCENT_PERCENTILE_CI
EXP11A = DESCRIPTIVE_JOINT_SIZE_COMPOSITION_SENSITIVITY
EXP11B = DESCRIPTIVE_ONLY / NO_SEED_SUPERPOPULATION_INFERENCE
EXP12 = NOT_ESTIMABLE
HE5 = DESCRIPTIVE_ONLY_WITH_FROZEN_BOUNDARIES
CANDIDATE_RETRIEVAL != OVERALL_CLASSIFICATION_ACCURACY
NORMATIVE_ASSOCIATION != SUBSTANTIVE_NORMATIVE_CORRECTNESS
AUDITABILITY != LEGAL_CORRECTNESS
ROBUSTNESS != EMPIRICAL_GENERALIZATION
```

No hay valores observados, límites observados de intervalos, disposiciones HE2/HE5, conclusiones de significancia, claims de generalización externa, novelty ni final gap en Methods.

## 11. Dictamen

Las cuatro incidencias que motivaron `PASS WITH CORRECTIONS` en B06 V01 están cerradas. No se detecta defecto científico, semántico, documental, de procedencia o de continuidad que justifique otra revisión de redacción.

```text
OVERALL_VERDICT = PASS
B06-C01 = CLOSED
B06-C02 = CLOSED
B06-C03 = CLOSED
B06-C04 = CLOSED
B06_V02 = READY_FOR_AUTHOR_REVIEW
AUTHOR_APPROVAL_GATE = MAY_OPEN_FOR_B06_V02_ONLY
INTEGRATION = NOT_YET_AUTHORIZED
SECTION_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

---

## English

```text
REVIEW_ID = EXPERIMENTAL_DESIGN_B06_SECTION4_7_INTERNAL_REVIEW_V02
DATE = 2026-09-27
ROLE = MANAGING_AI / PRINCIPAL_SCIENTIFIC_EDITOR
BLOCK = EXPERIMENTAL_DESIGN_B06_SECTION_4_7
CANDIDATE_REVISION = V02 / NARROW_METHODS_CORRECTION
SCOPE_DECISION = D-074
EXECUTION_AUTHORIZATION = D-075
RESPONSE = article/responses/5_EXPERIMENTAL_DESIGN_B06_SECTION4_7_RESPONSE_V02.md@8469a6aa83b85dc64486877106cc6f05115b1751
RESPONSE_GIT_BLOB = 50f12ae688c0459cc396c6337c14e75d119a6128
SECTION_ARTIFACT = article/sections/experimental_design/Experimental_Design_B06_V02.md@b8d19af968cc9b3e0cc205a908a05a5c1549b4c4
SECTION_ARTIFACT_GIT_BLOB = 76d833b0f3c693ddafe997f0202e3893513a35a2
OVERALL_VERDICT = PASS
```

The Managing AI independently audited B06 V02 against the D-074 narrow correction scope and the D-075 execution authorization. All four required corrections close successfully.

B06-C01 now explicitly records the 67 EVAL DAM clusters, the common `10000 × 67` DAM-resample matrix used for every eligible inferential result, and multiplicity handling when the same DAM is sampled repeatedly while preserving the series-weighted estimand. B06-C02 now records the supplementary Top-50 two-sided 95% percentile interval, its exclusion from hypothesis disposition, and the frozen unstandardized paired contribution difference without a post-hoc standardized effect measure. B06-C03 restores the frozen HE5 non-estimable/descriptive boundaries and literal historical-support buckets without a new insufficiency threshold. B06-C04 uses the corrected Group-3 source blobs.

Independent Markdown comparison confirms that only six Section-4.7 paragraphs changed: three English paragraphs and their Spanish semantic mirrors. Sections 1–4.6 and 4.8 onward were preserved. No Results or hypothesis-disposition leakage occurred.

Independent DOCX inspection confirmed an identical 14-entry package set, only `word/document.xml` changed, all 40 inherited comments preserved with all 40 anchors/references, zero tracked changes, identical 446-paragraph count, and exactly six changed paragraph indices `[162, 163, 165, 382, 383, 385]`. The complete 49-page render passed visual inspection without material formatting loss.

The response field `GOVERNING_DECISION = D-074` is non-blocking: D-074 defines the correction scope, while D-075 is the verified execution authorization. No additional response correction is required.

```text
OVERALL_VERDICT = PASS
B06_V02 = READY_FOR_AUTHOR_REVIEW
AUTHOR_APPROVAL_GATE = MAY_OPEN_FOR_B06_V02_ONLY
INTEGRATION = NOT_YET_AUTHORIZED
SECTION_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```
