# Prompt — Experimental Design B06 / Section 4.7 — V01

## Español

### Rol

Actúa como **IA de Redacción científica**. Ejecuta exclusivamente B06 de Experimental Design: **Section 4.7 Statistical and robustness analysis** y su espejo español. No avances a Section 4.8 ni Results.

Este prompt opera bajo MWDP v1.0 y SPCCR. La omisión de una regla acumulativa no la deroga.

### 1. Onboarding obligatorio

Lee íntegramente y en este orden exacto:

1. `article/START_HERE.md`;
2. `article/README.md`;
3. `article/ARTICLE_STATUS.md`;
4. `article/ARTICLE_WRITING_PLAN.md`;
5. `article/DECISIONS.md`;
6. `article/SOURCE_REGISTRY.md`;
7. `article/CLAIM_EVIDENCE_MATRIX.md`;
8. `article/STYLE_GUIDE.md`;
9. este prompt específico.

Después lee íntegramente:

- `article/governance/MASTER_WRITING_AND_DELIVERY_PROTOCOL.md`;
- `article/governance/SCIENTIFIC_PROSE_CLARITY_AND_CONCRETENESS_RULE.md`;
- `article/governance/D021_DOCX_LOCAL_CUSTODY_AND_DEFERRED_REPOSITORY_UPLOAD.md`;
- `article/governance/D022_GITHUB_ONLY_OPERATIONAL_PROMPTS_AND_RESPONSES.md`;
- `article/governance/D027_DOCX_AUTHOR_HANDOFF_REQUIREMENT.md`;
- `article/governance/D035_TIMEOUT_SAFE_ARTIFACT_HANDOFF.md`;
- `article/governance/D045_SECTION4_RESTRUCTURE_AUTHOR_APPROVAL_AND_STRUCTURE_V02.md`;
- `article/governance/D071_EXPERIMENTAL_DESIGN_B05_INTEGRATION_AND_V014_PROMOTION.md`;
- `article/governance/D072_EXPERIMENTAL_DESIGN_B06_SECTION4_7_GROUND_TRUTH_SYNC.md`;
- `article/manuscript/KBS_ARTICLE_WORKING_STRUCTURE_V02.md`;
- `article/manuscript/ARTICLE_MASTER_V014.md`.

Si el onboarding no puede completarse, detente con `BLOCKED_ONBOARDING` y no modifiques ningún artefacto.

### 2. Baselines exactos

Markdown canónico obligatorio:

```text
BASELINE_MD = article/manuscript/ARTICLE_MASTER_V014.md
BASELINE_MD_SHA256 = e7aa7e6706923520a5403ab4dec6713d5a1f7fe6b55edccbde43f2d54b755b97
BASELINE_MD_GIT_BLOB = 20105abb745e382b923e4eb43d9a771a722df9e3
```

Word acumulativo obligatorio, proporcionado por el autor:

```text
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B05_V01.docx
BASELINE_DOCX_SHA256 = b1ab0ba79fe8d4dffad57208b2765f18e2c84b80ef4c1dbcfd3ac93eba8f78e2
PRIOR_CITATION_COMMENTS = 40
```

Si el DOCX no está disponible o su SHA-256 no coincide exactamente, detente con:

`BLOCKED_MISSING_EXACT_B05_DOCX_BASELINE`

No reconstruyas el DOCX desde Markdown. No uses un Word anterior. No elimines ni alteres comentarios heredados salvo autorización expresa; aquí no existe tal autorización.

### 3. Re-verificación de fuentes vivas

Antes de redactar, verifica en GitHub:

```text
EXPECTED_SRC03_HEAD = 87422102290a4f9a89c51e936cf7274d8e4687d8
EXPECTED_SRC03_PLAN_BLOB = cf587b61b7bfbc66dca310a7bb3b4d3f64671eea
EXPECTED_DEVELOPMENT_MAIN = db0d0ad0d8435921a7838db6720eaea86a263763
```

Fuentes primarias mínimas para B06:

- `docs/analysis/group3/g3_analytical_contract_v0.1.md` — blob esperado `76862c10fd84fd70588da2d65f96dbe3b40914f6`;
- `docs/analysis/group3/g3_inferential_methods_and_checks_v0.1.md` — blob esperado `6cf424c9cf8aa7371dbbf5b8baaf7305cc66a436`;
- `outputs/analysis/group3/g3_inferential_results_v0.1.json` — solo para verificar identidad/procedencia del procedimiento, **no para trasladar valores observados a Methods**;
- `outputs/analysis/group3/g3_metric_population_registry_v0.1.json` — solo para confirmar familias/estatus metodológicos cuando sea necesario;
- `article/CLAIM_EVIDENCE_MATRIX.md` vigente;
- D-072.

Si existe drift, determina si altera materialmente Section 4.7. Si sí, detente con `BLOCKED_MATERIAL_SOURCE_DRIFT`. No elijas retrospectivamente reglas por favorecer resultados.

### 4. Alcance científico exclusivo

Reemplaza únicamente los placeholders de:

- English: `## 4.7. Statistical and robustness analysis`;
- Spanish: `## 4.7. Análisis estadístico y de robustez` o el heading equivalente ya presente.

No modifiques Sections 1–4.6, Section 4.8, Results, Discussion, Conclusion ni end matter.

La función de 4.7 es describir **cómo se trató la dependencia, cómo se construyó la inferencia primaria y qué análisis quedaron como sensibilidad/descriptivos/no estimables**. No reportes resultados observados.

### 5. Contenido obligatorio

#### 5.1 Unidad, dependencia y estimando

Explica en prosa científica que:

- SERIE es la unidad primaria de análisis;
- DAM/declaración es la unidad de agrupamiento cuando existe dependencia;
- las comparaciones son pareadas sobre los mismos casos;
- el estimando es ponderado por series;
- el bootstrap por clusters remuestrea DAM completas y conserva todas sus series;
- si una DAM se selecciona varias veces, todas sus series contribuyen con esa multiplicidad;
- no se sustituye el estimando por una media no ponderada de medias por DAM.

#### 5.2 Early-ranking inference

Para cada comparador corregido de RQ1 —BM25 normativo plano, BM25 normativo jerárquico y D1a inspirado en Text2Trade— describe:

```text
CONTRAST = historical - comparator
PRIMARY_METRICS = Top-1, Top-3, Top-5, Top-10, MRR@100
BOOTSTRAP = paired DAM-cluster bootstrap
REPLICATES = 10000
SEED = 20263001
DAM_CLUSTERS = 67
COMMON_RESAMPLE_MATRIX = YES
PRIMARY_INTERVAL = two-sided 99% percentile interval
MULTIPLICITY = Bonferroni familywise 95% within each five-metric comparator family
P_VALUES = NONE
```

La diferencia absoluta pareada de contribuciones es la medida de efecto congelada. No introduzcas Cohen's d, odds ratios, standardized mean differences ni otra medida post hoc.

Top-50 puede mencionarse como métrica suplementaria con intervalo percentil bilateral del 95%, fuera de la familia primaria y sin función en la disposición de hipótesis.

#### 5.3 Deep-coverage inference

Describe un solo contraste inferencial:

`corrected hierarchical Recall@200 - Recall@100`.

Mismo bootstrap por DAM, 10.000 réplicas, seed 20263001 e intervalo percentil bilateral del 95%. Sin ajuste por multiplicidad. No dupliques Pool@200 como segundo contraste confirmatorio.

#### 5.4 Sensibilidad y robustez

Describe de forma metodológica, sin valores observados:

- H25/H50/H75 frente a H100 como **joint historical-bank size/composition sensitivity** descriptiva; tamaño y composición están acoplados;
- H150/H200 como sensibilidad descriptiva sobre diez seeds pareados y el mismo EVAL; no existe superpoblación congelada de seeds y no se permite inferencia sobre 10 × 1.056 filas como observaciones independientes;
- 0B-05C Attempt06 como estado correctivo de sensibilidad descriptiva; excluir intentos superseded;
- Phase-E candidate pools como inventarios descriptivos de cobertura, no rankings alternativos ni inferencia primaria;
- EXP12 diversity como `NOT_ESTIMABLE`; no reabrirlo;
- calidad ambigua/incompleta de descripción como no estimable por ausencia de operacionalización;
- proximidad jerárquica como descriptiva con categorías `SAME_CHAPTER`, `SAME_HS4`, `SAME_HS6`;
- soporte histórico con buckets literales `1 DAM`, `2 DAM`, `3-4 DAM`, `5+ DAM`, sin crear umbral post hoc de “insufficient”.

#### 5.5 Límite de interpretación

Explica que el bootstrap cuantifica incertidumbre de remuestreo cluster-aware dentro del benchmark interno fijo de Chapter 87. No establece inferencia hacia una población externa ni generalización empírica.

### 6. Contenido prohibido

No incluyas:

- point estimates observados;
- intervalos observados;
- p-values;
- decisiones `HE2 = SUPPORTED` o `HE5 = INCONCLUSIVE`;
- conclusiones de superioridad;
- cifras de sensibilidad observadas;
- resultados 0B-05C;
- resultados EXP11A/EXP11B;
- resultados de Phase E;
- una estimación de EXP12;
- claims de causalidad por tamaño del banco;
- inferencia a superpoblación de seeds;
- claims de generalización externa;
- claims de accuracy global del framework;
- claims de corrección jurídica;
- nombres de scripts/rutas/hashes en la prosa del manuscrito salvo que sean científicamente indispensables;
- narrativa organizada por IDs internos de experimento.

Mantén:

```text
EXP11A_SIZE_COMPOSITION_SENSITIVITY != ISOLATED_CAUSAL_SIZE_EFFECT
EXP11B_DESCRIPTIVE != SEED_SUPERPOPULATION_INFERENCE
EXP12_DIVERSITY_EFFECT = NOT_ESTIMABLE
CANDIDATE_RETRIEVAL != OVERALL_CLASSIFICATION_ACCURACY
AUDITABILITY != LEGAL_CORRECTNESS
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### 7. Estilo

Redacta como Methods de Knowledge-Based Systems:

- prosa concreta y operacional;
- agentes, objetos, procedimientos y límites explícitos;
- evitar abstracciones no aterrizadas y nominalizaciones densas;
- no convertir el texto en un manifiesto de gobernanza;
- no enumerar hashes o rutas en la prosa del artículo;
- inglés natural de publicación y espejo español semánticamente equivalente;
- explicar el porqué metodológico solo cuando ayude a interpretar el procedimiento.

### 8. Entregables obligatorios

Genera exactamente:

1. `article/sections/experimental_design/Experimental_Design_B06_V01.md`;
2. `ARTICLE_MASTER_CANDIDATE_EXPDES_B06_V01.md`;
3. `ARTICLE_MASTER_CANDIDATE_EXPDES_B06_V01.docx`;
4. `article/responses/5_EXPERIMENTAL_DESIGN_B06_SECTION4_7_RESPONSE_V01.md`.

El master Markdown candidato debe ser acumulativo y partir byte-semánticamente de V014, cambiando solo 4.7 EN/ES.

El DOCX debe partir del **binario exacto B05 V01** y editarse directamente; no reconstruirse desde Markdown.

### 9. QA obligatorio

Antes de entregar verifica y registra:

- hash del baseline Markdown y Git blob;
- SHA-256 exacto del DOCX baseline;
- diff Markdown limitado a 4.7 EN/ES;
- Sections 1–4.6 preservadas;
- Section 4.8 y posteriores preservadas;
- equivalencia semántica EN/ES;
- ausencia de Results leakage;
- ausencia de hypothesis-disposition leakage;
- integridad ZIP/OOXML;
- parse de XML y relationships;
- mismo conjunto de entradas ZIP salvo necesidad técnica justificada;
- `comments.xml` preservado byte-identical si no requiere cambio;
- 40 comment ranges/references preservados;
- 0 tracked changes;
- equivalencia semántica MD/DOCX;
- render completo de todas las páginas y revisión visual sin clipping, overlap, truncation o pérdida material de formato.

### 10. Response versionada

La response debe incluir el checklist MWDP:

```text
PROTOCOL_READ
BLOCK / REVISION
SOURCE_SNAPSHOTS
AUTHORIZED / CONDITIONAL / PROHIBITED CLAIMS
ACCESS_RECHECK
CITATION_COVERAGE
EN_ES_EQUIVALENCE
MASTER_CANDIDATE
ENGLISH_WORD_COUNT
EXPERIMENTAL_REVIEW_TRIGGER
```

Debe registrar las fuentes primarias efectivamente verificadas, las identidades de los candidatos y todo el QA. Si C08/C26/C27 u otros claims condicionados por alcance son usados para describir sensibilidad/estimabilidad, registra explícitamente su estado y límite; no declares `CONDITIONAL_CLAIMS_USED = NONE` si la matriz vigente indica lo contrario.

Finaliza con:

```text
EXECUTION_COMPLETED_PENDING_GESTORA_AUDIT
AUTHOR_APPROVAL_GATE = NOT_OPEN
SECTION_4_8 = NOT_AUTHORIZED
RESULTS = NOT_AUTHORIZED
```

En chat entrega únicamente la ruta+commit de la response versionada y los handoffs reales del Markdown y DOCX acumulativos. Detente después de B06.

---

## English

Act as the **scientific Drafting AI** only for Experimental Design B06: Section 4.7, `Statistical and robustness analysis`, plus its Spanish semantic-control mirror. Do not draft Section 4.8 or Results.

Complete the exact onboarding sequence specified above, then read MWDP v1.0, SPCCR, D-021, D-022, D-027, D-035, D-045, D-071, D-072, Structure V02, and canonical `ARTICLE_MASTER_V014.md`.

Use exact baselines:

```text
BASELINE_MD = article/manuscript/ARTICLE_MASTER_V014.md
BASELINE_MD_SHA256 = e7aa7e6706923520a5403ab4dec6713d5a1f7fe6b55edccbde43f2d54b755b97
BASELINE_MD_GIT_BLOB = 20105abb745e382b923e4eb43d9a771a722df9e3
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B05_V01.docx
BASELINE_DOCX_SHA256 = b1ab0ba79fe8d4dffad57208b2765f18e2c84b80ef4c1dbcfd3ac93eba8f78e2
PRIOR_CITATION_COMMENTS = 40
```

Stop with `BLOCKED_MISSING_EXACT_B05_DOCX_BASELINE` if the exact Word baseline is unavailable. Never reconstruct the DOCX from Markdown.

Recheck live SRC-03/main and the primary Group-3 analytical/inferential sources. Stop on material drift.

Draft only Section 4.7 EN/ES. Describe SERIE as the analysis unit, DAM as the dependence cluster, series-weighted paired estimands, and the paired DAM-cluster bootstrap. For the historical-versus-corrected-comparator early-ranking contrasts, report only the method: Top-1/3/5/10 and MRR@100, 10,000 common paired cluster-bootstrap replicates, seed 20263001, two-sided 99% percentile intervals and within-comparator Bonferroni familywise 95% control, with no p-values. Top-50 is supplementary with a two-sided 95% interval and no hypothesis-decision role.

For deep coverage, describe only corrected hierarchical `Recall@200 - Recall@100`, using the same bootstrap and a two-sided 95% interval without multiplicity adjustment. Do not duplicate Pool@200 as a second confirmatory contrast.

The effect measure is the absolute paired contribution difference; do not introduce standardized post-hoc effect sizes.

Describe the frozen robustness/sensitivity statuses without observed results: H25/H50/H75 versus H100 is descriptive joint size/composition sensitivity; H150/H200 is descriptive paired sensitivity across ten seeds with no seed-superpopulation inference; corrected 0B-05C Attempt06 is descriptive; Phase-E pools are descriptive inventories; EXP12 diversity and ambiguous/incomplete-description prevalence are not estimable; hierarchy categories and literal historical-support buckets are descriptive only.

Do not include observed values, confidence-interval values, p-values, final HE2/HE5 dispositions, superiority conclusions, Results claims, external-population inference, causal bank-size claims, global framework accuracy, or legal-correctness claims.

Produce exactly the four deliverables listed in the Spanish instructions, preserve the exact cumulative DOCX and its 40 inherited comments, perform full OOXML/differential/render QA, and stop after B06.