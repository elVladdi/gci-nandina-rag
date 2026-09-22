# PREG7-001 — Preflight no gobernante para G7-F01

## 0. Naturaleza del artefacto

Este documento es un **pretrabajo no gobernante**. No activa G7-F01, no modifica Plan Maestro, fichas, `main`, artículo ni tesis, y no sustituye el futuro output formal `docs/writing/group7/g7_writing_source_freeze_v0.1.md/json`.

Estado rector observado:

```text
G6-F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G6-F02 = CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
G6-F03 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
G7-F01 = PROSPECTIVE
G7-F02 = PROSPECTIVE
G7-F03 = PROSPECTIVE
GROUP6 = IN_PROGRESS
```

La secuencia formal permanece bloqueada hasta `GROUP6 = CLOSED / APPROVED`.

---

## 1. Objetivo del preflight

Reducir el trabajo futuro de G7-F01 mediante:

1. inventario de fuentes científicas ya congelables;
2. mapeo preliminar `claim → evidencia → tabla → figura → destino tesis/artículo`;
3. identificación de fuentes aún no congelables;
4. detección de drift documental entre flujo experimental y flujo editorial;
5. identificación anticipada de insumos para G7-F02, G7-F03 y G8.

No se redacta ni modifica ninguna sección.

---

## 2. Contrato de G7-F01 revisado

La ficha G7-F01 exige formalmente:

- identificar tesis/Word maestro vigente y su hash;
- onboarding completo de `article/START_HERE.md` para el artículo;
- congelar Plan Maestro, outputs G3–G6, claim registry y fuente bibliográfica;
- separar texto nuevo, texto a actualizar y texto inmutable;
- registrar reglas institucionales UNMSM disponibles.

Dependencia formal: `G7 ← GROUP6 CLOSED/APPROVED`.

---

## 3. Fuentes científicas ya aptas para el futuro writing freeze

### 3.1 Grupo 3 — inferencia y disposición

Fuentes canónicas ya cerradas operacionalmente:

```text
outputs/analysis/group3/g3_analytical_contract_v0.1.json
outputs/analysis/group3/g3_metric_population_registry_v0.1.json
outputs/analysis/group3/g3_inferential_results_v0.1.json
outputs/analysis/group3/g3_hypothesis_disposition_v0.1.json
```

Disposiciones obligatorias:

```text
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
EXP11A = JOINT_SIZE_COMPOSITION_SENSITIVITY / NONCAUSAL
EXP11B = DESCRIPTIVE_H150_H200 / TEN_OBSERVED_SEED_PAIRS / NO_SEED_SUPERPOPULATION_INFERENCE
EXP12 = CLOSED_WITHOUT_RETRIEVAL / DIVERSITY_EFFECT_NOT_ESTIMABLE
```

Frontera empírica:

```text
UNIT_OF_ANALYSIS = SERIE
DEPENDENCY_GROUP = DAM / DECLARACION cuando corresponda
EMPIRICAL_SCOPE = CAPITULO_87 / OFFLINE / INTERNAL_EVALUATION
EVAL_N = 1056
EVAL_DAM = 67
EVAL_NANDINA = 42
```

### 3.2 Grupo 4 — claims e interpretación

Fuentes rectoras:

```text
outputs/analysis/group4/g4_result_claim_evidence_matrix_v0.1.csv
outputs/analysis/group4/g4_result_claim_evidence_matrix_v0.1.json
docs/analysis/group4/g4_interpretation_synthesis_v0.1.md
outputs/analysis/group4/g4_limitations_registry_v0.1.json
docs/analysis/group4/g4_literature_contrast_v0.1.md
```

El registro contiene 18 claims controlados `G3C-001..G3C-018` y mantiene las fronteras de causalidad, generalización, legal correctness, HE5 y EXP12.

### 3.3 Grupo 5 — sistema canónico de presentación

Nueve tablas congeladas:

```text
G5-MAIN-01      g5_main_01_he2a_primary_early_ranking.csv
G5-MAIN-02      g5_main_02_he2b_deep_coverage.csv
G5-SECONDARY-01 g5_secondary_01_phase_e_descriptive.csv
G5-SECONDARY-02 g5_secondary_02_he5_descriptive_components.csv
G5-APPENDIX-01  g5_appendix_01_top50_supplementary.csv
G5-APPENDIX-02  g5_appendix_02_exp11a_size_composition_sensitivity.csv
G5-APPENDIX-03  g5_appendix_03_exp11b_h150_h200_sensitivity.csv
G5-APPENDIX-04  g5_appendix_04_0b05c_attempt06_corrective_sensitivity.csv
G5-APPENDIX-05  g5_appendix_05_phase_e_diagnostic_union.csv
```

Además se conservan destinos `TEXT_ONLY` / `NOT_PRESENTED_AS_RESULT_WITH_REASON` para EXP12 y guardrails.

### 3.4 Grupo 6 — congelable parcialmente, no formalmente cerrado

Apto para preflight:

```text
outputs/figures/group6/g6_figure_spec_registry_v0.1.json
```

Figuras especificadas:

```text
G6-FIG-01 = HE2_A + HE2_B / MAIN
G6-FIG-02 = Phase E / SECONDARY
G6-FIG-03 = EXP11A / APPENDIX
```

No apto aún para freeze formal G7:

```text
figures/g6-f02-render-v01@2a483984eddc60dbbd48e7188b6fe9dbd7e829c5
```

porque G6-F02 sigue `NOT_APPROVED` y existe scope correctivo consolidado pendiente de Prompt106. G6-F03 todavía no ha producido captions ni cierre.

---

## 4. Matriz preliminar claim → evidencia → presentación → destino

| Claim | Rol | Evidencia/presentación principal | Figura | Tesis futura | Artículo futuro |
|---|---|---|---|---|---|
| G3C-001 | HE2_A primario | G5-MAIN-01 | G6-FIG-01 | Resultados | Results |
| G3C-002 | HE2_A primario | G5-MAIN-01 | G6-FIG-01 | Resultados | Results |
| G3C-003 | HE2_A primario | G5-MAIN-01 | G6-FIG-01 | Resultados | Results |
| G3C-004 | HE2_B primario | G5-MAIN-02 | G6-FIG-01 | Resultados | Results |
| G3C-005 | Phase E descriptivo | G5-SECONDARY-01 | G6-FIG-02 | Resultados/Discusión | Results/Discussion |
| G3C-006 | Top-50 suplementario | G5-APPENDIX-01 | TABLE_ONLY | Resultados/anexo | Results/supplement |
| G3C-007 | EXP11A sensibilidad | G5-APPENDIX-02 | G6-FIG-03 | Discusión/Limitaciones | Discussion |
| G3C-008 | EXP11B sensibilidad | G5-APPENDIX-03 | TABLE_ONLY | Discusión/Limitaciones | Discussion |
| G3C-009 | Attempt06 actual | G5-APPENDIX-04 | TABLE_ONLY | Discusión/Limitaciones | Discussion |
| G3C-010 | EXP12 no estimable | TEXT_ONLY | none | Limitaciones | Discussion/Limitations |
| G3C-011 | descripción ambigua no estimable | TEXT_ONLY | none | Limitaciones | Discussion/Limitations |
| G3C-012 | proximidad jerárquica descriptiva | G5-SECONDARY-02 | TABLE_ONLY | Resultados/Limitaciones | Results/Discussion |
| G3C-013 | soporte histórico descriptivo | G5-SECONDARY-02 | TABLE_ONLY | Resultados/Limitaciones | Results/Discussion |
| G3C-014 | frontera de validez | TEXT_ONLY | none | Metodología/Limitaciones | Methods scope |
| G3C-015 | separación arquitectónica | TEXT_ONLY | none | Metodología | Architecture/Methods |
| G3C-016 | retrieval ≠ accuracy global RAG | guardrail | none | Discusión/Limitaciones | Discussion |
| G3C-017 | evidencia normativa ≠ corrección jurídica | guardrail | none | Discusión/Limitaciones | Discussion |
| G3C-018 | explicación auditable ≠ correctness | guardrail | none | Discusión/Limitaciones | Discussion |

Este mapeo es preparatorio. No sustituye la trazabilidad formal futura de G7-F02/G7-F03 ni la auditoría de G8-F01.

---

## 5. Estado de la tesis vigente

Se localizó en los archivos del proyecto una copia titulada:

```text
Molleapasa_gv(4).docx
```

Esta copia coincide con el working draft de tesis más reciente identificado en el flujo previo, pero todavía no existe en este preflight un SHA-256 verificable ni una declaración formal de `APPROVED_MASTER`.

La materialización de bytes desde Project/Library no estuvo disponible en esta sesión, por lo que:

```text
THESIS_FILE_IDENTIFIED = true
THESIS_FILENAME = Molleapasa_gv(4).docx
THESIS_SHA256_VERIFIED = false
THESIS_APPROVED_MASTER_STATUS = NOT_ESTABLISHED
FORMAL_G7_F01_THESIS_FREEZE_READY = false
```

Consecuencia: **la parte tesis de G7-F01 no puede cerrarse formalmente todavía**, aunque sí puede preauditarse conceptualmente usando el documento cuando esté disponible como fuente legible.

---

## 6. Estado del artículo y drift detectado

El onboarding editorial vigente identifica:

```text
CANONICAL_MASTER = ARTICLE_MASTER_V007
CANONICAL_MASTER_MD = article/manuscript/ARTICLE_MASTER_V007.md
CANONICAL_MASTER_MD_GIT_BLOB = 436e0522db0ac348efaed86f4e53a7e6db372471
CURRENT_DRAFTING_PHASE = DECISION SUPPORT ARCHITECTURE
CURRENT_GATE = ARCHITECTURE_B01
AUTHORIZED_SCOPE = SECTIONS_3_1_TO_3_4_ONLY
```

El artículo ya registra D-034, que aclara que Grupo 6 bloquea la activación formal de G7 pero no Architecture/Experimental design bajo sus gates editoriales propios.

### Drift experimental/editorial observado

`ARTICLE_STATUS.md`, `ARTICLE_WRITING_PLAN.md` y `SOURCE_REGISTRY.md` todavía conservan como último corte experimental consumible:

```text
GROUP6 = NOT_STARTED
G6-F01 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
```

pero el estado experimental actual es posterior:

```text
G6-F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G6-F02 = CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
GROUP6 = IN_PROGRESS
```

Clasificación:

```text
DRIFT_ID = PREG7-DRIFT-001
TYPE = EDITORIAL_SNAPSHOT_STALENESS
SCIENTIFIC_CONTRADICTION = false
FORMAL_RECONCILIATION_REQUIRED_BEFORE_G7_F03 = true
IMMEDIATE_ARCHITECTURE_BLOCKER = false
```

No corresponde modificar la rama del artículo desde este preflight. La IA Gestora del artículo debe consumir un nuevo snapshot experimental cuando su gobernanza lo autorice.

---

## 7. Texto nuevo / a actualizar / inmutable — preclasificación

### Artículo

```text
INMUTABLE_UNDER_CURRENT_EDITORIAL_GOVERNANCE:
- Related Work 2.1–2.6
- Introduction B01 V02

CURRENTLY_AUTHORIZED_BY_ARTICLE_GOVERNANCE:
- Decision-support architecture B01 / 3.1–3.4

NOT_YET_AUTHORIZED_BY_ARTICLE_GOVERNANCE:
- Architecture B02
- Experimental design
- Results
- Discussion
- Conclusion
- final figures/captions/cross-references
```

### Tesis

Hasta verificar el master y su hash, la clasificación formal `NEW / UPDATE / IMMUTABLE` no debe congelarse. Como preparación, las áreas mínimas candidatas a actualización futura según G7-F02 son:

```text
- Resultados
- Discusión
- Limitaciones
- Conclusiones
- ajustes metodológicos estrictamente necesarios para reflejar el experimento ejecutado
```

---

## 8. Reglas de escritura que deben quedar congeladas en G7

1. ninguna cifra sin tabla/artefacto canónico;
2. `HE2 = SUPPORTED` solo dentro del benchmark congelado;
3. `HE5 = INCONCLUSIVE` y nunca supported/rejected por EXP12;
4. EXP12 = no estimable, sin retrieval y sin reapertura;
5. EXP11A = sensibilidad conjunta tamaño/composición, no causal;
6. EXP11B = descriptivo, diez pares observados, sin superpoblación de seeds;
7. Attempt06 es el único estado 0B-05C vigente;
8. retrieval histórico superior ≠ accuracy global RAG;
9. evidencia normativa ≠ corrección jurídica vinculante;
10. explicación auditable ≠ clasificación/legal correctness;
11. configurabilidad ≠ generalización empírica;
12. SERIE/DAM deben mantenerse coherentes en Métodos, Resultados y Discusión;
13. tablas y figuras deben conservar sus roles MAIN/SECONDARY/APPENDIX/TEXT_ONLY;
14. outputs históricos `CANDIDATE_PENDING_EXTERNAL_AUDIT` dentro de artefactos cerrados no reabren estados ya cerrados operacionalmente.

---

## 9. Preparación para G8

Este preflight ya permite anticipar la estructura mínima futura de G8-F01/G8-F02:

```text
DOCUMENTO/SECCION
→ CLAIM_ID
→ EVIDENCIA PRIMARIA
→ TABLA CANONICA
→ FIGURA/CAPTION SI APLICA
→ CIFRA/CI/N
→ LIMITACION OBLIGATORIA
→ OUTPUT SUPERSEDED PROHIBIDO
→ STATUS
```

Checks prioritarios futuros:

- 99% CI HE2_A vs 95% CI HE2_B;
- ningún CI por brazo en HE2_A;
- Phase E descriptivo sin inferencia;
- Top-50 suplementario sin rol decisional;
- HE5 sin umbral retrospectivo de concentración/insuficiencia;
- Attempt06 únicamente;
- EXP12 sin retrieval;
- SERIE/DAM consistentes;
- Chapter 87/offline/internal como frontera empírica;
- texto, tablas y figuras numéricamente consistentes.

---

## 10. Resultado del preflight

```text
PREG7_001_RESULT = PARTIAL_READY
FORMAL_G7_F01_AUTHORIZED = false
GROUP6_CLOSE_REQUIRED = true
G3_G4_G5_SOURCE_INVENTORY_READY = true
G6_F01_SPEC_SOURCE_READY = true
G6_F02_FIGURES_FREEZE_READY = false
G6_F03_CAPTION_PACKAGE_READY = false
ARTICLE_ONBOARDING_SOURCE_IDENTIFIED = true
ARTICLE_CURRENT_GATE = ARCHITECTURE_B01
ARTICLE_EXPERIMENTAL_SNAPSHOT_DRIFT = true
THESIS_FILE_IDENTIFIED = true
THESIS_SHA256_VERIFIED = false
THESIS_MASTER_STATUS_FROZEN = false
G8_PREFLIGHT_STRUCTURE_READY = true
```

### Próximo pretrabajo recomendado

1. preauditar `Molleapasa_gv(4).docx` contra los 18 claims G4, las nueve tablas G5 y los guardrails G3/G4;
2. producir una matriz de discrepancias de tesis **sin editar el Word**;
3. usar esa matriz como insumo preparatorio de G7-F02 y, posteriormente, G8-F01/G8-F02;
4. mantener Prompt106 pendiente para cerrar técnicamente G6-F02 cuando vuelva el ejecutor local.
