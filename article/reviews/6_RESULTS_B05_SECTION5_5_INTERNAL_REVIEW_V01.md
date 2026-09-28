# Internal Review — Results B05 / Section 5.5 — V01

## Español

```text
REVIEW = RESULTS_B05_SECTION_5_5_INTERNAL_REVIEW_V01
BLOCK = RESULTS_B05_SECTION_5_5
SECTION = 5.5 SENSITIVITY AND ROBUSTNESS ANALYSES
VERDICT = PASS
REVIEWER = IA_GESTORA
BASELINE_MASTER = ARTICLE_MASTER_V020
AUTHOR_APPROVAL_GATE = OPEN_AFTER_D111
RESULTS_B06_PLUS = NOT_AUTHORIZED
```

### 1. Identidad de la entrega

La respuesta versionada fue verificada en `article/responses/6_RESULTS_B05_SECTION5_5_RESPONSE_V01.md@53419aca4b7805733a3c804512eb757764c2acae` y el artefacto de sección en `article/sections/results/Results_B05_V01.md@bebe259868921a4f04539418b5f4a934d92ee44d`.

Los candidatos recibidos y auditados tienen las siguientes identidades:

```text
ARTICLE_MASTER_CANDIDATE_RESULTS_B05_V01.md
SHA256 = a40e403ff89bce022c2b8adc894a6d92083a40ee31d7c9b20360ef36761fbd06
GIT_BLOB = e76b5b1789de1f82c9623dd6543c38ae639715b0

ARTICLE_MASTER_CANDIDATE_RESULTS_B05_V01.docx
SHA256 = 3cf78e027953d8c311be2c99e16c9f2909b93b106e323eec7aee2281eaaa2b70
```

La identidad del baseline local volvió a comprobarse antes del diff:

```text
ARTICLE_MASTER_CANDIDATE_RESULTS_B04_V01.md
SHA256 = eeb2ad72ba563267ea64cb6c91a798ff4f56a56b1d2946088a81ea02fc63006b
GIT_BLOB = 7393bf0db2d577d27168ccbb2a1060f1b337c872

ARTICLE_MASTER_CANDIDATE_RESULTS_B04_V01.docx
SHA256 = 57181016380550901c4c4e9dc9f8aa4bddb07bc3e7912e5e0c07088d9de42b92
```

### 2. Control de alcance Markdown

El diff acumulativo V020 → B05 V01 contiene exactamente dos operaciones sustantivas: sustitución del placeholder de §5.5 inglesa por cinco párrafos y sustitución del placeholder de §5.5 española por cinco párrafos. No se observó modificación de Sections 1–5.4, §5.6, §5.7, Discussion, Conclusion ni end matter.

El Git blob calculado localmente para el Markdown candidato coincide con el declarado por la IA de Redacción: `e76b5b1789de1f82c9623dd6543c38ae639715b0`.

### 3. Auditoría científica y numérica

Los resultados EXP11A se recontrastaron contra `exp11_metrics_by_condition.csv` en `main@db0d0ad0d8435921a7838db6720eaea86a263763`. Las medias, rangos y la referencia H100 reportadas en §5.5 coinciden con el artefacto congelado. La redacción conserva explícitamente la restricción obligatoria `EXP11A_SIZE_COMPOSITION_SENSITIVITY ≠ ISOLATED_CAUSAL_SIZE_EFFECT`.

Los resultados EXP11B se recontrastaron contra `exp11b_retrieval_condition_summary_v0.1.csv`. Las medias H150/H200 coinciden y el texto conserva el diseño descriptivo pareado sobre diez seeds y el mismo EVAL, sin inferencia a una superpoblación de seeds o casos.

La sensibilidad correctiva final 0B-05C se recontrastó contra `ev03_aggregate_comparison_v0.5.json`, `ev04_aggregate_comparison_v0.5.json` y `d1a_corrective_vs_original_comparison_v0.5.json`. El texto reproduce correctamente: EV03 sin cambio agregado; EV04 con disminución únicamente de MRR de `-9.511162528404171e-06`; y D1a con cambios positivos no nulos en ranking exacto, junto con el efecto HS4 mixto congelado. No se reduce el cierre conjunto a impacto global cero.

El análisis HE5 se recontrastó contra `he5_historical_hierarchy_errors_v0.2.csv`, `he5_historical_errors_by_support_v0.2.csv` y `g3_hypothesis_disposition_v0.1.json`. Los 518 errores Top-1 se descomponen exactamente en `147 SAME_CHAPTER + 284 SAME_HS4 + 87 SAME_HS6`; los cuatro buckets literales de soporte y sus métricas coinciden con la fuente; no se crea un umbral post hoc de soporte insuficiente; `description_component = NOT_ESTIMABLE`; `EXP12 = NOT_ESTIMABLE`; y la disposición HE5 se mantiene `INCONCLUSIVE`.

No se encontraron intervalos de confianza, bootstrap, p-values, significancia, disposición HE2 ni otra inferencia reservada para §5.6. Las menciones a causalidad o superpoblación aparecen únicamente como límites negativos explícitos.

### 4. Equivalencia bilingüe

La sección inglesa y la española contienen la misma secuencia científica y 160 tokens numéricos equivalentes tras normalizar separadores decimal/millar. No se detectó pérdida, adición o inversión de interpretación entre EN y ES.

### 5. Integridad DOCX

La auditoría OOXML independiente comparó el DOCX B05 contra el baseline B04:

```text
ZIP_ENTRIES_BASELINE = 14
ZIP_ENTRIES_CANDIDATE = 14
ZIP_ENTRY_NAMES = IDENTICAL
CHANGED_ZIP_PARTS = word/document.xml ONLY
COMMENTS_XML = BYTE_IDENTICAL
RELATIONSHIPS = BYTE_IDENTICAL
STYLES = BYTE_IDENTICAL
OTHER_OOXML_PARTS = BYTE_IDENTICAL
TRACKED_CHANGES = 0
COMMENT_RANGE_START = 40
COMMENT_RANGE_END = 40
COMMENT_REFERENCE = 40
COMMENTS = 40 / IDs 0..39
```

El texto Word pasó de 480 a 488 párrafos. El diff de párrafos contiene exactamente dos sustituciones: `1 placeholder → 5 párrafos` en §5.5 inglesa y `1 placeholder → 5 párrafos` en §5.5 española. La equivalencia normalizada Markdown↔DOCX es exacta para los cinco párrafos ingleses y los cinco españoles; la nota editorial inglesa heredada también coincide.

### 6. Render y QA visual

El candidato DOCX se renderizó de forma independiente a 57 páginas. Las páginas 1–25 son pixel-identical al baseline previamente auditado; las páginas 30–54 son pixel-identical a las páginas 28–52 del baseline después del desplazamiento de paginación. Las páginas materialmente afectadas por la inserción (`26–29` y `55–57`) fueron inspeccionadas visualmente y no presentan clipping, superposición, truncamiento, glifos faltantes, tablas rotas ni encabezados/pies desplazados.

La página 29 contiene únicamente la nota estructural heredada `[Optional.]` por efecto de la paginación antes del salto a la Parte II. Es una consecuencia del master interno y no una corrupción, pérdida de contenido ni defecto bloqueante.

### 7. Scope y claims

Claims autorizados usados: `C08`, `C22`, `C23`, `C24`, `C25`, `C26`, `C27`, `C29`.

No se detectó uso de claims prohibidos. Permanecen preservadas las distinciones:

- candidate retrieval ≠ overall classification accuracy;
- joint bank size/composition sensitivity ≠ isolated causal size effect;
- EXP11B descriptive paired seeds ≠ superpopulation inference;
- EXP12 diversity effect = NOT_ESTIMABLE;
- HE5 = INCONCLUSIVE;
- documentary drift/correction sensitivity ≠ legal correctness;
- §5.5 descriptive robustness ≠ §5.6 inference.

### Veredicto

`PASS`.

B05 V01 es científicamente consistente con D-109/D-110, conserva el alcance autorizado, mantiene equivalencia EN/ES y preserva íntegramente el master acumulativo salvo la sustitución prevista de §5.5. Puede abrirse el gate de aprobación del autor. Este `PASS` no equivale a aprobación del autor ni autoriza integración o apertura de B06.

---

## English

```text
VERDICT = PASS
B05_V01 = GESTORA_AUDITED
AUTHOR_APPROVAL = REQUIRED_BEFORE_INTEGRATION
RESULTS_B06_PLUS = NOT_AUTHORIZED
```

The independent audit verified candidate identities, Section-5.5-only scope, frozen numerical evidence, descriptive-only interpretation, EN/ES equivalence, OOXML preservation, 40 preserved comments, zero tracked changes, exact MD↔DOCX paragraph equivalence, and clean 57-page rendering. B05 V01 may proceed to the author-approval gate; no integration or Section 5.6 drafting is authorized by this review alone.
