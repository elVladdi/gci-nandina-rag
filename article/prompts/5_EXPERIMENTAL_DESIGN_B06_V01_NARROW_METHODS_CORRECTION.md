# Prompt — Experimental Design B06 V01 narrow methods correction

## Español

### Rol y alcance

Actúa como **IA de Redacción científica** únicamente para ejecutar el microgate correctivo B06 autorizado por D-074. Corrige exclusivamente B06-C01, B06-C02, B06-C03 y B06-C04. No reescribas Section 4.7 de forma general y no avances a Section 4.8 ni Results.

### 1. Fuentes vinculantes

Lee íntegramente:

1. `article/reviews/5_EXPERIMENTAL_DESIGN_B06_SECTION4_7_INTERNAL_REVIEW_V01.md@3d19fbb47fd48abe15520264eea3b29969084295`;
2. `article/governance/D074_EXPERIMENTAL_DESIGN_B06_NARROW_METHODS_CORRECTION.md@52269d2f317548d8cfadb020b9ffdb07ff7f6c83`;
3. `article/prompts/5_EXPERIMENTAL_DESIGN_B06_SECTION4_7.md@f29d10e10c5b94e3c36947cc42031f6dbac4e7bf`;
4. `docs/analysis/group3/g3_analytical_contract_v0.1.md` en `development main = db0d0ad0d8435921a7838db6720eaea86a263763`, blob `76862c10fd84fd70588da2d65f96dbe3b40914f6`;
5. `docs/analysis/group3/g3_inferential_methods_and_checks_v0.1.md` en el mismo commit, blob `6cf424c9cf8aa7371dbbf5b8baaf7305cc66a436`;
6. `outputs/analysis/group3/g3_inferential_results_v0.1.json` en el mismo commit, blob `f99b7e46d81b28ca2b7cfce8d24788ad14156dcc`, solo para identidad/procedencia metodológica;
7. `article/CLAIM_EVIDENCE_MATRIX.md` vigente.

### 2. Baselines exactos obligatorios

Trabaja exclusivamente sobre los dos candidatos B06 V01 entregados al autor:

```text
BASELINE_MD = ARTICLE_MASTER_CANDIDATE_EXPDES_B06_V01.md
BASELINE_MD_SHA256 = 1ba6d1ea0b0b0c748bf2b4c74e92a53b5ad98852d724157b682c689848bcbc76
BASELINE_MD_GIT_BLOB = bda3bb6f9603039c48239deab779eec106588719

BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B06_V01.docx
BASELINE_DOCX_SHA256 = c58044f2b591eadf9dac0f2cb6bf30624e1c1124d43578bd17bf8c86c0e4dc5e
PRIOR_COMMENTS = 40
PRIOR_TRACKED_CHANGES = 0
```

Si falta uno de los archivos o su identidad no coincide, detente sin modificar artefactos con:

`BLOCKED_MISSING_EXACT_B06_V01_CORRECTION_BASELINE`

No regreses a V014/B05 como baseline de edición. No reconstruyas el DOCX desde Markdown.

### 3. Correcciones científicas obligatorias

Modifica únicamente Section 4.7 EN/ES y solo lo necesario para incorporar las siguientes precisiones.

#### B06-C01 — bootstrap común y multiplicidad

En el párrafo del bootstrap deja explícito, con prosa natural de Methods, que:

- el EVAL contiene 67 clusters DAM para este procedimiento;
- un único stream congelado produjo una matriz común `10000 × 67` de índices DAM remuestreados con reemplazo;
- la misma matriz se utilizó para todos los resultados inferenciales elegibles;
- si una DAM aparece `m` veces en una réplica, todas sus series contribuyen con multiplicidad `m`;
- esto conserva el estimando ponderado por series y no lo sustituye por una media no ponderada de medias DAM.

No conviertas la prosa en un listado de implementación ni introduzcas resultados observados.

#### B06-C02 — Top-50 y medida de efecto

En el párrafo HE2_A deja explícito que:

- Top-50 es suplementaria y usa un intervalo percentil bilateral del 95%;
- está fuera de la familia primaria de cinco métricas y no tiene función en la disposición de hipótesis;
- la medida de efecto congelada es la diferencia pareada **no estandarizada** de contribuciones (`historical - comparator`);
- no se introdujo una medida de efecto estandarizada post hoc.

No introduzcas valores observados, bounds ni p-values.

#### B06-C03 — reglas HE5 omitidas

En el párrafo de sensibilidad/robustez deja explícito que:

- la prevalencia de descripciones ambiguas/incompletas no es estimable porque la calidad de descripción no fue operacionalizada;
- la proximidad jerárquica se conserva descriptivamente con `SAME_CHAPTER`, `SAME_HS4` y `SAME_HS6`;
- el soporte histórico conserva literalmente los buckets `1 DAM`, `2 DAM`, `3-4 DAM` y `5+ DAM`;
- ningún bucket se redefine post hoc como `insufficient` y no se crea un nuevo umbral de insuficiencia.

No reportes counts ni resultados de esas familias.

### 4. Corrección documental de response — B06-C04

Genera una response V02 que preserve semánticamente la response V01, refleje las correcciones B06-C01–C03 y corrija exactamente estas identidades:

```text
G3_INFERENTIAL_METHODS_BLOB = 6cf424c9cf8aa7371dbbf5b8baaf7305cc66a436
G3_INFERENTIAL_RESULTS_JSON_BLOB = f99b7e46d81b28ca2b7cfce8d24788ad14156dcc
```

No vuelvas a registrar los blobs incorrectos `7a01b75184d95f8df121506079939279957204f6` ni `8dd92de02e77e6e496baa0af9b5a3d763c19d7f1`.

La matriz claim–evidencia vigente mantiene C08, C26 y C27 en `AUTHORIZED` dentro de sus límites descriptivos; no los conviertas artificialmente en claims condicionales. Mantén todas las fronteras de interpretación ya vigentes.

### 5. Cambios prohibidos

No modifiques:

- Sections 1–4.6;
- Section 4.8 o posteriores;
- Results, Discussion o Conclusion;
- valores observados de resultados;
- disposiciones HE2/HE5;
- la dirección de contrasts;
- métricas, seeds, número de réplicas o reglas de multiplicidad;
- claims de novelty/final gap;
- comentarios heredados.

No introduzcas p-values, nuevas pruebas ni nuevas medidas de efecto.

### 6. Entregables obligatorios

Genera exactamente:

1. `article/sections/experimental_design/Experimental_Design_B06_V02.md`;
2. `ARTICLE_MASTER_CANDIDATE_EXPDES_B06_V02.md`;
3. `ARTICLE_MASTER_CANDIDATE_EXPDES_B06_V02.docx`;
4. `article/responses/5_EXPERIMENTAL_DESIGN_B06_SECTION4_7_RESPONSE_V02.md`.

El Markdown V02 debe diferir del B06 V01 únicamente dentro de Section 4.7 EN/ES.

El DOCX V02 debe partir directamente del binario exacto B06 V01, preservando comentarios y estructura OOXML. No reconstruyas el Word.

### 7. QA obligatorio

Registra:

```text
BASELINE_MD_SHA256
BASELINE_DOCX_SHA256
MD_DIFF_ONLY_4_7_EN_ES
SECTIONS_1_TO_4_6_PRESERVED
SECTION_4_8_PLUS_PRESERVED
EN_ES_EQUIVALENCE
RESULTS_LEAKAGE = NONE
HYPOTHESIS_DISPOSITION_LEAKAGE = NONE
ZIP_OOXML_INTEGRITY
ZIP_ENTRY_SET
CHANGED_PACKAGE_CONTENT
COMMENTS = 40
COMMENT_RANGE_START = 40
COMMENT_RANGE_END = 40
COMMENT_REFERENCE = 40
TRACKED_CHANGES = 0
MD_DOCX_SEMANTIC_EQUIVALENCE
FULL_DOCX_RENDER
VISUAL_QA
```

La response V02 debe cerrar con:

```text
B06_CORRECTIONS = B06-C01 / B06-C02 / B06-C03 / B06-C04 COMPLETED_PENDING_GESTORA_AUDIT
SCIENTIFIC_SCOPE_EXPANDED = NO
AUTHOR_APPROVAL_GATE = NOT_OPEN
SECTION_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

En chat responde únicamente en español con la ruta+commit exactos de la response V02 y realiza los handoffs reales de los candidatos MD/DOCX V02. Detente después del microgate.

---

## English

Act only as the scientific Drafting AI for the D-074 narrow B06 correction. Use the exact B06 V01 Markdown and DOCX candidates as editing baselines. Do not return to V014/B05 and never reconstruct Word from Markdown.

Implement only four corrections:

1. **B06-C01:** explicitly state 67 DAM clusters, the single common `10000 × 67` DAM-resample matrix used across eligible inferential results, and the rule that a DAM sampled `m` times contributes all of its series with multiplicity `m`, preserving the series-weighted estimand.
2. **B06-C02:** state supplementary Top-50 two-sided 95% percentile uncertainty and its non-decision role; state that the frozen effect measure is the unstandardized paired contribution difference and that no post-hoc standardized effect measure was introduced.
3. **B06-C03:** explicitly retain the frozen HE5 methodological statuses for non-operationalized ambiguous/incomplete description quality, descriptive hierarchy proximity categories, and literal historical-support buckets without a post-hoc insufficiency threshold.
4. **B06-C04:** correct response source identities to methods blob `6cf424c9cf8aa7371dbbf5b8baaf7305cc66a436` and inferential-results JSON blob `f99b7e46d81b28ca2b7cfce8d24788ad14156dcc`.

Create only `Experimental_Design_B06_V02.md`, cumulative B06 V02 Markdown/DOCX candidates, and response V02. Preserve all prior content outside Section 4.7, all 40 inherited comments, zero tracked changes, and the Section 4.8/Results gate. Perform full OOXML and render QA before handoff.