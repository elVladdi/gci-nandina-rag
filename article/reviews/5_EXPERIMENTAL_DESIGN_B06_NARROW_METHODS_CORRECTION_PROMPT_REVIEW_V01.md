# Revisión del prompt correctivo B06 / B06 narrow-correction prompt review — V01

## Español

```text
REVIEW_ID = B06_NARROW_METHODS_CORRECTION_PROMPT_REVIEW_V01
ROLE = IA_GESTORA / EDITOR_CIENTIFICO_PRINCIPAL
PROMPT = article/prompts/5_EXPERIMENTAL_DESIGN_B06_V01_NARROW_METHODS_CORRECTION.md@c14ab0d5aec458870b05307e5bed521d3a104547
PROMPT_GIT_BLOB = 90592518a2197ee6a7889797bf43da60b8b06fcf
PARENT_DECISION = D-074
PARENT_REVIEW = article/reviews/5_EXPERIMENTAL_DESIGN_B06_SECTION4_7_INTERNAL_REVIEW_V01.md@3d19fbb47fd48abe15520264eea3b29969084295
VERDICT = PASS
```

### 1. Baselines y continuidad

El prompt fija correctamente como únicos baselines de edición los candidatos B06 V01 ya auditados:

```text
BASELINE_MD = ARTICLE_MASTER_CANDIDATE_EXPDES_B06_V01.md
BASELINE_MD_SHA256 = 1ba6d1ea0b0b0c748bf2b4c74e92a53b5ad98852d724157b682c689848bcbc76
BASELINE_MD_GIT_BLOB = bda3bb6f9603039c48239deab779eec106588719
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B06_V01.docx
BASELINE_DOCX_SHA256 = c58044f2b591eadf9dac0f2cb6bf30624e1c1124d43578bd17bf8c86c0e4dc5e
COMMENTS = 40 / PRESERVE
TRACKED_CHANGES = 0 / PRESERVE
```

También prohíbe correctamente regresar a V014/B05 como baseline de edición y prohíbe reconstruir el DOCX desde Markdown.

### 2. Cobertura de las cuatro correcciones

El prompt cubre íntegramente los cuatro defectos de la auditoría:

- **B06-C01:** 67 DAM, matriz común `10000 × 67`, misma matriz para los resultados inferenciales elegibles y regla de multiplicidad `m` por DAM remuestreada;
- **B06-C02:** Top-50 suplementaria con IC percentil bilateral 95%, sin rol de decisión, y diferencia pareada no estandarizada como medida de efecto congelada;
- **B06-C03:** no estimabilidad de calidad ambigua/incompleta por falta de operacionalización, categorías descriptivas `SAME_CHAPTER`/`SAME_HS4`/`SAME_HS6` y buckets literales `1 DAM`/`2 DAM`/`3-4 DAM`/`5+ DAM` sin threshold post hoc;
- **B06-C04:** corrección de las dos identidades de procedencia a los blobs verificados `6cf424c9cf8aa7371dbbf5b8baaf7305cc66a436` y `f99b7e46d81b28ca2b7cfce8d24788ad14156dcc`.

### 3. Control de alcance

El prompt no abre una reescritura general. Limita el cambio manuscrito a Section 4.7 EN/ES y prohíbe modificar Sections 1–4.6, Section 4.8, Results, Discussion, Conclusion, disposiciones HE2/HE5, métricas, seed, número de réplicas, claims de novelty/final gap o comentarios heredados.

No autoriza p-values, nuevas pruebas ni nuevas medidas de efecto.

### 4. Entregables y QA

Los cuatro entregables V02 están especificados sin ambigüedad:

1. `article/sections/experimental_design/Experimental_Design_B06_V02.md`;
2. `ARTICLE_MASTER_CANDIDATE_EXPDES_B06_V02.md`;
3. `ARTICLE_MASTER_CANDIDATE_EXPDES_B06_V02.docx`;
4. `article/responses/5_EXPERIMENTAL_DESIGN_B06_SECTION4_7_RESPONSE_V02.md`.

El contrato preserva el flujo MWDP: edición directa del Word exacto, 40 comentarios, cero tracked changes, QA ZIP/OOXML, equivalencia MD/DOCX, render completo y revisión visual. El gate de salida conserva cerrados Section 4.8 y Results.

### 5. Fuentes y claims

Las fuentes de Group 3 están identificadas con las identidades verificadas. El prompt no transforma C08, C26 ni C27 en claims condicionales: la matriz vigente los mantiene `AUTHORIZED` dentro de sus límites descriptivos. Las prohibiciones científicas previas permanecen intactas.

### 6. Dictamen

```text
BASELINE_CONTROL = PASS
CORRECTION_SCOPE = PASS
SOURCE_IDENTITY_CONTROL = PASS
CLAIM_CONTROL = PASS
DOCX_CONTINUITY = PASS
DELIVERABLE_CONTRACT = PASS
EN_ES_EQUIVALENCE_OF_PROMPT = PASS
SECTION_4_8_GATE = CLOSED
RESULTS_GATE = CLOSED
VERDICT = PASS
```

El prompt puede ejecutarse como único contrato correctivo B06.

---

## English

```text
REVIEW_ID = B06_NARROW_METHODS_CORRECTION_PROMPT_REVIEW_V01
ROLE = MANAGING_AI / PRINCIPAL_SCIENTIFIC_EDITOR
PROMPT = article/prompts/5_EXPERIMENTAL_DESIGN_B06_V01_NARROW_METHODS_CORRECTION.md@c14ab0d5aec458870b05307e5bed521d3a104547
PROMPT_GIT_BLOB = 90592518a2197ee6a7889797bf43da60b8b06fcf
PARENT_DECISION = D-074
VERDICT = PASS
```

The corrective prompt passes independent review. It fixes the exact B06 V01 Markdown and DOCX candidates as the sole editing baselines, prohibits returning to V014/B05, and forbids DOCX reconstruction from Markdown.

It fully covers B06-C01 through B06-C04: the common `10000 × 67` DAM resampling matrix and multiplicity rule; supplementary Top-50 95% interval and the unstandardized paired-difference effect measure; the omitted frozen HE5 methodological statuses; and the two corrected Group-3 source blobs.

The correction is strictly bounded to Section 4.7 EN/ES plus response provenance metadata. Sections 1–4.6, Section 4.8 and all later sections remain protected. The prompt preserves 40 inherited comments, zero tracked changes, direct OOXML editing, full technical QA, bilingual semantic equivalence, and the no-Results boundary.

```text
BASELINE_CONTROL = PASS
CORRECTION_SCOPE = PASS
SOURCE_IDENTITY_CONTROL = PASS
CLAIM_CONTROL = PASS
DOCX_CONTINUITY = PASS
DELIVERABLE_CONTRACT = PASS
EN_ES_EQUIVALENCE_OF_PROMPT = PASS
SECTION_4_8_GATE = CLOSED
RESULTS_GATE = CLOSED
VERDICT = PASS
```