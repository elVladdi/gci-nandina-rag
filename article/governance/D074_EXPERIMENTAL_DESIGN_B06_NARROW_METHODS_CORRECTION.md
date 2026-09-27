# D-074 — Corrección estrecha de B06 / Section 4.7 / Narrow B06 Section 4.7 correction

## Español

```text
DECISION_ID = D-074
DATE = 2026-09-27
STATUS = ACTIVE / BINDING
PARENT_DECISION = D-073
BLOCK = EXPERIMENTAL_DESIGN_B06_SECTION_4_7
INTERNAL_REVIEW = article/reviews/5_EXPERIMENTAL_DESIGN_B06_SECTION4_7_INTERNAL_REVIEW_V01.md@3d19fbb47fd48abe15520264eea3b29969084295
INTERNAL_REVIEW_RESULT = PASS WITH CORRECTIONS
CORRECTION_SCOPE = B06-C01 / B06-C02 / B06-C03 / B06-C04 ONLY
AUTHOR_APPROVAL_GATE = NOT_OPEN
SECTION_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### 1. Decisión

La auditoría independiente de B06 V01 confirma que el núcleo científico de Section 4.7 es correcto, que no existe filtración de Results y que la continuidad acumulativa Markdown/DOCX es válida. Sin embargo, el bloque no puede abrir todavía el gate autoral porque la redacción condensó en exceso varios detalles obligatorios del procedimiento congelado y la response contiene dos identidades Git incorrectas de fuentes primarias.

Se autoriza una corrección estrecha, sin reescritura general.

### 2. Baselines de corrección

La corrección debe partir exclusivamente de los candidatos B06 V01 ya auditados:

```text
BASELINE_MD = ARTICLE_MASTER_CANDIDATE_EXPDES_B06_V01.md
BASELINE_MD_SHA256 = 1ba6d1ea0b0b0c748bf2b4c74e92a53b5ad98852d724157b682c689848bcbc76
BASELINE_MD_GIT_BLOB = bda3bb6f9603039c48239deab779eec106588719

BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B06_V01.docx
BASELINE_DOCX_SHA256 = c58044f2b591eadf9dac0f2cb6bf30624e1c1124d43578bd17bf8c86c0e4dc5e
COMMENTS = 40 / PRESERVE
TRACKED_CHANGES = 0 / PRESERVE
```

No se permite regresar a V014/B05 como baseline de edición ni reconstruir el DOCX desde Markdown.

### 3. Correcciones autorizadas

- **B06-C01:** explicitar la matriz común 10.000 × 67 de remuestreo DAM y la multiplicidad de todas las series cuando una DAM es seleccionada `m` veces.
- **B06-C02:** explicitar IC percentil bilateral del 95% para Top-50 suplementario y la diferencia pareada no estandarizada de contribuciones como medida de efecto congelada, sin medida estandarizada post hoc.
- **B06-C03:** explicitar las tres reglas HE5 omitidas: descripciones ambiguas/incompletas no estimables por falta de operacionalización; proximidad jerárquica descriptiva `SAME_CHAPTER`/`SAME_HS4`/`SAME_HS6`; buckets literales de soporte histórico `1 DAM`, `2 DAM`, `3-4 DAM`, `5+ DAM` sin umbral de insuficiencia.
- **B06-C04:** corregir en la response las identidades de procedencia:
  - `g3_inferential_methods_and_checks_v0.1.md` → blob `6cf424c9cf8aa7371dbbf5b8baaf7305cc66a436`;
  - `g3_inferential_results_v0.1.json` → blob `f99b7e46d81b28ca2b7cfce8d24788ad14156dcc`.

### 4. Cambios prohibidos

No se autoriza:

- cambiar resultados observados o trasladarlos a Methods;
- introducir p-values, nuevas pruebas, nuevas medidas de efecto o nuevas disposiciones HE2/HE5;
- modificar Sections 1–4.6;
- redactar 4.8;
- redactar Results;
- alterar comentarios heredados;
- reestructurar Section 4.7 fuera de lo necesario para B06-C01–C03;
- cambiar claims finales de gap o novelty.

### 5. Gate

```text
B06_STATE = REVISION_REQUIRED / NARROW_METHODS_AND_RESPONSE_METADATA_ONLY
NEXT_ACTOR = IA_REDACCION
NEXT_ACTION = EXECUTE_ONLY_B06_NARROW_CORRECTION_PROMPT
AUTHOR_APPROVAL_GATE = NOT_OPEN
SECTION_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

---

## English

```text
DECISION_ID = D-074
STATUS = ACTIVE / BINDING
BLOCK = EXPERIMENTAL_DESIGN_B06_SECTION_4_7
REVIEW_RESULT = PASS WITH CORRECTIONS
CORRECTION_SCOPE = B06-C01 / B06-C02 / B06-C03 / B06-C04 ONLY
AUTHOR_APPROVAL_GATE = NOT_OPEN
SECTION_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

Independent review confirms that the B06 scientific core, Results boundary, bilingual equivalence, Markdown continuity, and DOCX/OOXML continuity are valid. A narrow correction is nevertheless required before author approval.

The Drafting AI must edit only the audited B06 V01 candidate MD/DOCX and the versioned response. It must not return to V014/B05 as an editing baseline and must never reconstruct the DOCX from Markdown.

Authorized changes are limited to: the common `10000 × 67` DAM resample matrix and multiplicity rule; supplementary Top-50 95% interval and frozen unstandardized paired-difference effect measure; the omitted HE5 methodological statuses; and the two corrected Git source identities. No later section is opened by this decision.