# Revisión interna — Experimental Design B06 / Section 4.7 — V01

## Español

```text
REVIEW_ID = B06_SECTION_4_7_INTERNAL_REVIEW_V01
ROLE = IA_GESTORA / EDITOR_CIENTIFICO_PRINCIPAL
BLOCK = EXPERIMENTAL_DESIGN_B06_SECTION_4_7
SUBMISSION_RESPONSE = article/responses/5_EXPERIMENTAL_DESIGN_B06_SECTION4_7_RESPONSE_V01.md@fc08bee93556809171262b6ab56b4124c30d0867
GOVERNING_PROMPT = article/prompts/5_EXPERIMENTAL_DESIGN_B06_SECTION4_7.md@f29d10e10c5b94e3c36947cc42031f6dbac4e7bf
GROUND_TRUTH_DECISION = D-072
EXECUTION_AUTHORIZATION = D-073
VERDICT = PASS WITH CORRECTIONS
AUTHOR_APPROVAL_GATE = NOT_OPEN
SECTION_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

## 1. Alcance de la auditoría

Se auditó independientemente:

- la response B06 V01;
- `article/sections/experimental_design/Experimental_Design_B06_V01.md`;
- el candidato acumulativo `ARTICLE_MASTER_CANDIDATE_EXPDES_B06_V01.md` entregado al autor;
- el candidato acumulativo `ARTICLE_MASTER_CANDIDATE_EXPDES_B06_V01.docx` entregado al autor;
- el baseline Markdown canónico V014, que es byte-idéntico al candidato B05 V01 aprobado;
- el baseline Word B05 V01;
- el contrato analítico Group 3 y el documento congelado de métodos inferenciales;
- la matriz claim–evidencia vigente.

## 2. Identidades verificadas

```text
BASELINE_MD_SHA256 = e7aa7e6706923520a5403ab4dec6713d5a1f7fe6b55edccbde43f2d54b755b97
BASELINE_MD_GIT_BLOB = 20105abb745e382b923e4eb43d9a771a722df9e3
BASELINE_DOCX_SHA256 = b1ab0ba79fe8d4dffad57208b2765f18e2c84b80ef4c1dbcfd3ac93eba8f78e2

B06_CANDIDATE_MD_SHA256 = 1ba6d1ea0b0b0c748bf2b4c74e92a53b5ad98852d724157b682c689848bcbc76
B06_CANDIDATE_MD_GIT_BLOB = bda3bb6f9603039c48239deab779eec106588719
B06_CANDIDATE_DOCX_SHA256 = c58044f2b591eadf9dac0f2cb6bf30624e1c1124d43578bd17bf8c86c0e4dc5e
```

Las identidades del candidato coinciden con las declaradas por la response.

## 3. Auditoría diferencial MD/DOCX

El diff del Markdown contra el baseline B05/V014 se limita a los dos placeholders de Section 4.7 EN/ES. No se detectaron cambios materiales en Sections 1–4.6 ni en 4.8 y posteriores.

En el DOCX, el conjunto de 14 entradas ZIP se conserva exactamente. El único componente cuyo contenido cambió es `word/document.xml`; `comments.xml` permanece byte-identical con SHA-256 `04ba296122c3b349bd7b741b49dcf41fdd53b13a8b1e56802d118894b4e37603`.

```text
ZIP_ENTRY_SET = PASS / 14 OF 14 PRESERVED
CHANGED_PACKAGE_CONTENT = word/document.xml ONLY
COMMENTS = 40
COMMENT_RANGE_START = 40
COMMENT_RANGE_END = 40
COMMENT_REFERENCE = 40
TRACKED_CHANGES = 0
DOCX_SECTION_SCOPE = PASS / ONLY 4.7 EN_ES REPLACED
FULL_RENDER = PASS / 49 PAGES
VISUAL_QA = PASS
```

La revisión visual completa no detectó clipping, overlap, truncation ni pérdida material de formato.

## 4. Evaluación científica

La redacción acierta en los elementos centrales:

- SERIE sigue siendo la unidad de análisis;
- DAM/declaración se trata como cluster de dependencia;
- el estimando permanece ponderado por series;
- se utiliza bootstrap pareado por clusters de DAM con 10.000 réplicas y seed 20263001;
- HE2_A mantiene Top-1/3/5/10 y MRR@100, contraste `historical - comparator`, IC percentiles marginales del 99% y control Bonferroni FWER 95%;
- HE2_B mantiene un único contraste `Recall@200 - Recall@100` con IC bilateral del 95% y sin multiplicidad;
- EXP11A no se convierte en efecto causal de tamaño;
- EXP11B permanece descriptivo y sin inferencia a superpoblación de seeds;
- Attempt06 y Phase E permanecen descriptivos;
- EXP12 permanece no estimable;
- no se filtran valores observados, bounds, p-values ni disposiciones HE2/HE5 a Methods;
- no se confunde candidate retrieval con accuracy global ni auditabilidad con corrección jurídica.

No obstante, el contrato B06 V01 exigía varios detalles metodológicos que la redacción condensó en exceso. Deben restituirse antes del gate autoral.

## 5. Correcciones obligatorias

### B06-C01 — matriz común de remuestreo, 67 DAM y multiplicidad

La redacción indica muestreo por DAM con reemplazo y pareamiento dentro de cada comparación, pero no deja explícito que el procedimiento congelado utilizó **una única matriz 10.000 × 67 de índices DAM para todos los resultados**, ni que cuando una DAM aparece `m` veces en una réplica **todas sus series contribuyen con multiplicidad `m`**. Estos detalles forman parte del procedimiento congelado y fueron exigidos por el prompt.

Corrección requerida EN/ES: hacer explícitos `DAM_CLUSTERS = 67`, `COMMON_RESAMPLE_MATRIX = YES` y la regla de multiplicidad sin convertir la prosa en inventario técnico.

### B06-C02 — Top-50 y medida de efecto

La redacción menciona Top-50 como suplementaria, pero omite que su incertidumbre se resume mediante **IC percentil bilateral del 95%**. También debe declarar que la **diferencia pareada no estandarizada de contribuciones** es la medida de efecto congelada y que no se introduce una medida estandarizada post hoc.

Corrección requerida EN/ES: añadir ambas precisiones en el párrafo HE2_A, sin reportar ningún valor observado.

### B06-C03 — familias HE5 que el prompt exigió explicitar

La redacción resume que «HE5 evidence families remained descriptive», pero omite tres reglas congeladas que B06 V01 exigía nombrar:

1. la prevalencia de descripciones ambiguas/incompletas es **no estimable** porque `description_quality_operationalized=0`;
2. la proximidad jerárquica se conserva descriptivamente mediante `SAME_CHAPTER`, `SAME_HS4` y `SAME_HS6`;
3. el soporte histórico conserva literalmente los buckets `1 DAM`, `2 DAM`, `3-4 DAM`, `5+ DAM`, sin crear un umbral post hoc de «insufficient».

Corrección requerida EN/ES: incorporar estas tres reglas al párrafo de sensibilidad/robustez. No introducir resultados de esos análisis.

### B06-C04 — metadata de procedencia incorrecta en la response

La response registra dos Git blobs que no corresponden a las fuentes observadas en `development main = db0d0ad0d8435921a7838db6720eaea86a263763`:

```text
RESPONSE_REPORTED_G3_INFERENTIAL_METHODS_BLOB = 7a01b75184d95f8df121506079939279957204f6
VERIFIED_G3_INFERENTIAL_METHODS_BLOB = 6cf424c9cf8aa7371dbbf5b8baaf7305cc66a436

RESPONSE_REPORTED_G3_INFERENTIAL_RESULTS_JSON_BLOB = 8dd92de02e77e6e496baa0af9b5a3d763c19d7f1
VERIFIED_G3_INFERENTIAL_RESULTS_JSON_BLOB = f99b7e46d81b28ca2b7cfce8d24788ad14156dcc
```

Esta incidencia es documental/provenance metadata; no demuestra error en el contenido científico redactado. La response corregida debe sustituir solo esas identidades y reflejar las correcciones B06-C01–C03.

## 6. Claims y fronteras

La matriz vigente mantiene C08, C26 y C27 en `AUTHORIZED` dentro de sus límites descriptivos. Por ello, `CONDITIONAL_CLAIMS_USED = NONE` no constituye por sí mismo un defecto en esta entrega. Deben mantenerse las limitaciones de uso de dichos claims y las prohibiciones C09–C13/C16/C18 aplicables.

## 7. Dictamen

```text
SCIENTIFIC_CORE = PASS
SCOPE_CONTROL = PASS
RESULTS_LEAKAGE = NONE
EN_ES_EQUIVALENCE = PASS
MD_DIFFERENTIAL = PASS
DOCX_CONTINUITY = PASS
OOXML_INTEGRITY = PASS
VISUAL_QA = PASS
METHOD_COMPLETENESS = CORRECTION_REQUIRED
RESPONSE_SOURCE_METADATA = CORRECTION_REQUIRED
OVERALL_VERDICT = PASS WITH CORRECTIONS
AUTHOR_APPROVAL_GATE = NOT_OPEN
B07 / SECTION_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

La corrección debe ser estrecha: únicamente B06-C01–B06-C04. No se autoriza reescritura general de 4.7 ni cambios en Sections 1–4.6, 4.8 o posteriores.

---

## English

```text
REVIEW_ID = B06_SECTION_4_7_INTERNAL_REVIEW_V01
ROLE = MANAGING_AI / PRINCIPAL_SCIENTIFIC_EDITOR
BLOCK = EXPERIMENTAL_DESIGN_B06_SECTION_4_7
VERDICT = PASS WITH CORRECTIONS
AUTHOR_APPROVAL_GATE = NOT_OPEN
SECTION_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

The B06 scientific core, scope control, bilingual equivalence, cumulative Markdown continuity, DOCX continuity, OOXML integrity, inherited comments, tracked-change state, and 49-page visual render all pass independent review. The correction gate is narrow.

Four corrections are required before author approval:

1. **B06-C01:** state the frozen common `10000 × 67` DAM-resample matrix and the rule that a DAM sampled `m` times contributes all of its series with multiplicity `m`.
2. **B06-C02:** state that supplementary Top-50 uncertainty uses a two-sided 95% percentile interval and that the frozen effect measure is the unstandardized paired contribution difference, with no post-hoc standardized effect measure.
3. **B06-C03:** explicitly retain the frozen HE5 methodological statuses: ambiguous/incomplete-description prevalence is not estimable because description quality was not operationalized; hierarchy proximity remains descriptive under `SAME_CHAPTER`, `SAME_HS4`, `SAME_HS6`; historical-support buckets remain literal `1 DAM`, `2 DAM`, `3-4 DAM`, `5+ DAM` with no post-hoc insufficiency threshold.
4. **B06-C04:** correct the response provenance metadata to `g3_inferential_methods_and_checks_v0.1.md` blob `6cf424c9cf8aa7371dbbf5b8baaf7305cc66a436` and `g3_inferential_results_v0.1.json` blob `f99b7e46d81b28ca2b7cfce8d24788ad14156dcc`.

No observed Results, hypothesis dispositions, new inferential tests, or broader rewriting is authorized. Section 4.8 and Results remain closed.