# Prompt — Results B05 / Section 5.5 Sensitivity and robustness analyses

## Español

### Rol

Actúa como **IA de Redacción científica**. Ejecuta exclusivamente Results B05 / Section 5.5 — **Sensitivity and robustness analyses** sobre el master acumulativo canónico. No avances a Section 5.6 ni a ninguna sección posterior.

Este prompt opera bajo MWDP v1.0, SPCCR, D-021/D-022/D-027/D-035, D-108 y D-109. `CLAIM_EVIDENCE_MATRIX.md`, `SOURCE_REGISTRY.md`, `ARTICLE_STATUS.md`, `ARTICLE_WRITING_PLAN.md` y `STYLE_GUIDE.md` permanecen vinculantes.

### 1. Baselines exactos obligatorios

```text
BASELINE_MD = article/manuscript/ARTICLE_MASTER_V020.md
BASELINE_MD_SHA256 = eeb2ad72ba563267ea64cb6c91a798ff4f56a56b1d2946088a81ea02fc63006b
BASELINE_MD_GIT_BLOB = 7393bf0db2d577d27168ccbb2a1060f1b337c872

BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_RESULTS_B04_V01.docx
BASELINE_DOCX_SHA256 = 57181016380550901c4c4e9dc9f8aa4bddb07bc3e7912e5e0c07088d9de42b92
COMMENTS = 40 / PRESERVE
TRACKED_CHANGES = 0 / PRESERVE
PAGE_COUNT_BASELINE = 54
```

Verifica estas identidades antes de editar. Si alguna no coincide, detente y reporta `BLOCKED`.

### 2. Ground truth vinculante

Lee íntegramente:

```text
article/governance/D109_RESULTS_B05_GROUND_TRUTH_SYNC_AND_SECTION5_5_BOUNDARY.md
```

Snapshot experimental vinculante:

```text
main@db0d0ad0d8435921a7838db6720eaea86a263763
```

Fuentes primarias principales:

```text
outputs/analysis/group3/g3_metric_population_registry_v0.1.csv
GIT_BLOB = c63619b56a07e6b6d7be78b515d941ec3b205c41

outputs/experiments/exp11a_historical_size_sensitivity_v0.3/exp11_metrics_by_condition.csv
GIT_BLOB = 535dd377d107ddcbf09ecaa13cd66ca723ee738d

outputs/evaluation/exp11b_historical_retrieval_h150_h200_v0.1/exp11b_retrieval_condition_summary_v0.1.csv
GIT_BLOB = 144922ecee8ce9deda74db88e8dea85fb3af6f2e

outputs/evaluation/0b05c_corrective_numerical_v0.5/ev03_aggregate_comparison_v0.5.json
GIT_BLOB = 1fa1aed2584c5612bbc5be16173e93d80c2dd92e

outputs/evaluation/0b05c_corrective_numerical_v0.5/ev04_aggregate_comparison_v0.5.json
GIT_BLOB = 3bf28c036b0a0af5dd54d88c3b0050c60365b7f1

outputs/evaluation/d1a_corrective_0b05c_v0.5/d1a_corrective_vs_original_comparison_v0.5.json
GIT_BLOB = 6a26777395630722a18bca7826b7df96613ea4ea

outputs/evaluation/he5_integrated_error_analysis_v0.2/he5_historical_errors_by_support_v0.2.csv
GIT_BLOB = 0f70928ba83eec87c116e62cf104f505293bc092

outputs/evaluation/he5_integrated_error_analysis_v0.2/he5_historical_hierarchy_errors_v0.2.csv
GIT_BLOB = b5bd099114e7262f316dfc846b867bec9e7f176d
```

No sustituyas estas fuentes por resultados superseded, literatura, memoria del modelo ni inferencia propia.

### 3. Claims autorizados

B05 se apoya exclusivamente en:

```text
C08 = AUTHORIZED
C22 = AUTHORIZED
C23 = AUTHORIZED
C24 = AUTHORIZED
C25 = AUTHORIZED
C26 = AUTHORIZED
C27 = AUTHORIZED
C29 = AUTHORIZED / bounded disposition only
```

Guardrails relevantes:

```text
C09 = PROHIBITED
C10 = PROHIBITED
C11 = PROHIBITED
C16 = PROHIBITED
C18 = PROHIBITED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

No abras C28/HE2 en §5.5: la disposición inferencial HE2 y sus intervalos pertenecen a §5.6.

### 4. Contenido científico que §5.5 debe cubrir

Redacta §5.5 como resultados, no como metodología ni Discussion. Organiza el bloque por fenómenos científicos, no por cronología interna de ejecución. Se permiten subtítulos internos solo si mejoran claramente la legibilidad; evita nombres internos de experimento como encabezados si pueden traducirse a lenguaje científico.

#### 4.1. Sensibilidad a tamaño/composición del banco histórico

Reporta EXP11A como **sensibilidad conjunta tamaño/composición**. Los tamaños nominales H25, H50 y H75 fueron construidos por DAM completos; por ello cambian simultáneamente cantidad y composición. H100 es la referencia congelada.

Valores congelados:

```text
CONDITION  RUNS  TOP1_MEAN   TOP3_MEAN   TOP5_MEAN   TOP10_MEAN  TOP50_MEAN  MRR100_MEAN
H25        10    0.493371    0.645170    0.737405    0.843277    0.973106    0.603787
H50        10    0.428598    0.597917    0.680303    0.776042    0.930492    0.542492
H75        10    0.298295    0.463352    0.548769    0.653883    0.837121    0.414030
H100        1    0.509470    0.671402    0.763258    0.891098    0.991477    0.629708
```

Rangos autorizados para contextualizar variabilidad entre ejecuciones:

```text
H25 TOP3 = 0.540720–0.689394 ; MRR@100 = 0.510735–0.641314
H50 TOP3 = 0.491477–0.689394 ; MRR@100 = 0.431954–0.623899
H75 TOP3 = 0.283144–0.678977 ; MRR@100 = 0.248757–0.608612
H100 TOP3 = 0.671402          ; MRR@100 = 0.629708
```

No describas el patrón como efecto causal, monotónico o aislado del tamaño. No derives una relación dosis-respuesta.

#### 4.2. Bancos ampliados H150/H200

Reporta EXP11B como comparación **descriptiva pareada por seed** sobre diez pares, todos evaluados en el mismo EVAL de 1,056 series / 67 DAM.

```text
CONDITION  RUNS  TOP1_MEAN   TOP3_MEAN   TOP5_MEAN   TOP10_MEAN  TOP50_MEAN  MRR100_MEAN
H150       10    0.512689    0.689962    0.783333    0.891572    0.989583    0.633268
H200       10    0.514110    0.689489    0.782008    0.895265    0.985227    0.633310
```

Describe únicamente que las diferencias observadas son pequeñas y de signo mixto según métrica. No concluyas que aumentar a H150/H200 mejora, empeora, estabiliza o no afecta el desempeño como proposición general. No trates 10 × 1,056 como observaciones independientes y no infieras a una superpoblación de seeds.

#### 4.3. Sensibilidad a la corrección del recurso normativo

Explica el resultado final 0B-05C con Attempt06 solamente y como **sensibilidad descriptiva dependiente del método**.

EV03:

```text
ZERO_AGGREGATE_CHANGE
```

EV04:

```text
MRR@100: 0.0419812944 -> 0.0419717832 ; DELTA = -0.00000951116
MRR@200: 0.0433416116 -> 0.0433321004 ; DELTA = -0.00000951116
TOP1/TOP3/TOP5/TOP10/TOP50 = ZERO DELTA
RECALL@50/@100/@200 = ZERO DELTA
```

D1a:

```text
                 ORIGINAL     CORRECTED    DELTA
Top@1            0.000000     0.000947   +0.000947
Top@3            0.003788     0.010417   +0.006629
Top@5            0.034091     0.051136   +0.017045
Top@10           0.156250     0.178030   +0.021780
Top@50           0.305871     0.313447   +0.007576
MRR@100          0.032424     0.038087   +0.005663
Recall@100       0.345644     0.345644    0.000000
Recall@200       0.362689     0.363636   +0.000947
HS4@100          0.873106     0.879735   +0.006629
HS4@200          0.964015     0.963068   -0.000947
```

Síntesis autorizada:

```text
METHOD_DEPENDENT / NONZERO_EV04_MRR_AND_D1A
DOWNSTREAM_REEXECUTION = NOT_REQUIRED
```

No resumas toda la sensibilidad normativa como cero. No atribuyas causalidad ni significancia.

#### 4.4. Error structure y límites de robustez HE5

Puedes incluir una síntesis compacta de las dimensiones descriptivas HE5, siempre preservando los límites.

Errores históricos Top-1, categorías jerárquicas literales:

```text
TOTAL_TOP1_ERRORS = 518
SAME_CHAPTER = 147
SAME_HS4 = 284
SAME_HS6 = 87
```

No combines ni redefinas categorías después de observar resultados y no afirmes concentración causal.

Buckets literales de soporte histórico:

```text
BUCKET    CASES   TOP1       TOP3       MRR@100
1 DAM       27    0.370370   0.703704   0.564447
2 DAM       21    0.047619   0.190476   0.239384
3-4 DAM    425    0.691765   0.767059   0.760152
5+ DAM     583    0.399657   0.617496   0.551697
```

No llames “insufficient support” a ningún bucket: no existe umbral congelado de insuficiencia. No derives efecto causal del soporte.

Objetos no estimables:

```text
EXP12_DIVERSITY_EFFECT = NOT_ESTIMABLE
DESCRIPTION_QUALITY_PREVALENCE = NOT_ESTIMABLE
```

EXP12 no produjo retrievals D-HIGH/D-MID/D-LOW. La calidad/ambigüedad de descripción no tuvo una operacionalización case-level congelada. Estos faltantes son límites del análisis, no resultados positivos o negativos sobre diversidad o calidad textual.

`HE5 = INCONCLUSIVE` puede expresarse funcionalmente como imposibilidad de sostener una conclusión global bajo todas las dimensiones previstas, no como supported/rejected.

### 5. Prohibiciones específicas de §5.5

No incluyas:

- intervalos bootstrap ni límites de confianza;
- p-values, significancia o tests inferenciales;
- `HE2 = SUPPORTED` ni disposición HE2_A/HE2_B;
- causalidad del tamaño/composición, soporte o corrección normativa;
- inferencia a una superpoblación de seeds o a población externa;
- accuracy global del framework;
- corrección normativa sustantiva o legal;
- claims de generalización fuera de Chapter 87;
- comparación con literatura o interpretación propia de Discussion;
- novelty, first/SOTA o gap definitivo.

No conviertas `DOWNSTREAM_REEXECUTION = NOT_REQUIRED` en una conclusión de ausencia de impacto; significa únicamente que el cierre correctivo gobernado no requirió reejecutar etapas downstream.

### 6. Alcance diferencial

```text
SECTIONS_1_TO_5_4 = FROZEN / PRESERVE EXACTLY
SECTION_5_5 = AUTHORIZED FOR DRAFTING V01 ONLY
SECTIONS_5_6_PLUS = NOT AUTHORIZED / PRESERVE PLACEHOLDERS
DISCUSSION = NOT AUTHORIZED
CONCLUSION = NOT AUTHORIZED
END_MATTER = PRESERVE
```

Sustituye únicamente el placeholder de §5.5 en la Parte I inglesa y su espejo semántico en la Parte II española. No reformules §5.1–§5.4 para evitar repetición.

### 7. Requisitos de redacción

- La Parte I inglesa es el master de publicación.
- La Parte II española debe ser semánticamente equivalente, no una paráfrasis que cambie fuerza causal o inferencial.
- Mantén el estilo KBS ya consolidado: prosa científica compacta, resultados primero, limitación junto al claim que califica.
- No cites literatura en §5.5 salvo que ya exista una razón editorial explícita; este bloque se apoya en resultados experimentales propios.
- No uses códigos internos como `G3F02-*` en la prosa del manuscrito.
- `EXP11A`, `EXP11B`, `0B-05C`, `Attempt06` y `HE5` pueden aparecer en response/auditoría, pero en la prosa del artículo tradúcelos preferentemente a descripciones científicas funcionales.
- No inventes cifras faltantes ni redondeos incompatibles. Mantén suficiente precisión para que los valores reportados sean trazables a D-109.

### 8. Word / MWDP / D-035

Edita el DOCX directamente desde el baseline Word B04 V01. No reconstruyas Word desde Markdown.

Preserva:

```text
COMMENTS = 40
TRACKED_CHANGES = 0
STYLES / COMMENTS / RELATIONSHIPS / EXISTING TABLES = PRESERVE
```

Tras editar:

- verifica OOXML;
- verifica que la única modificación sustantiva sea §5.5 EN/ES;
- renderiza el DOCX completo;
- inspecciona visualmente todas las páginas;
- verifica equivalencia semántica MD↔DOCX para §5.5;
- reporta SHA-256 exactos.

D-035 es obligatorio: no Base64 manual, chunking, fragmentación, reensamblado ni workarounds para entregar archivos grandes. Entrega los dos candidatos acumulativos como archivos reales al autor.

### 9. Entregables obligatorios

Genera:

```text
article/sections/results/Results_B05_V01.md
ARTICLE_MASTER_CANDIDATE_RESULTS_B05_V01.md
ARTICLE_MASTER_CANDIDATE_RESULTS_B05_V01.docx
article/responses/6_RESULTS_B05_SECTION5_5_RESPONSE_V01.md
```

Versiona en GitHub solamente el artefacto pequeño de sección y la response, conforme D-035. No materialices los masters acumulativos grandes en GitHub.

La response debe incluir al menos:

```text
PROTOCOL_READ
SOURCE_RECHECK
BASELINE_MD_SHA256 / GIT_BLOB
BASELINE_DOCX_SHA256
CANDIDATE_MD_SHA256 / EXPECTED_GIT_BLOB
CANDIDATE_DOCX_SHA256
SECTION_ARTIFACT_SHA256
AUTHORIZED_CLAIMS_USED
PROHIBITED_CLAIMS_USED
SECTION_5_5_ONLY_DIFF
SECTIONS_1_TO_5_4_PRESERVED
SECTIONS_5_6_PLUS_PRESERVED
NUMERICAL_CONTENT
INFERENTIAL_LEAKAGE = NONE
EN_ES_EQUIVALENCE
COMMENTS
TRACKED_CHANGES
OOXML_INTEGRITY
FULL_DOCX_RENDER
FULL_DOCX_PAGE_COUNT
D035_TIMEOUT_SAFE_HANDOFF
RESULTS_B05_V01_EXECUTION = COMPLETED_PENDING_GESTORA_AUDIT
```

### 10. Stop condition

Detente después de completar B05 V01. No abras Section 5.6, no redactes Discussion ni Conclusion y no solicites aprobación del autor por tu cuenta.

---

## English control

Draft only Results B05 / Section 5.5 from the exact V020 Markdown and approved B04 Word baselines. Report the reconciled descriptive sensitivity/robustness evidence only: joint size/composition sensitivity for H25/H50/H75 relative to H100; paired descriptive H150/H200 summaries across ten seeds on the same EVAL; final method-dependent 0B-05C corrective sensitivity; and bounded HE5 descriptive/non-estimable results. Do not introduce HE2 inference, confidence intervals, significance, causal claims, seed-superpopulation claims, overall system accuracy, legal correctness, external generalization, literature comparison, or novelty. Preserve all other manuscript sections exactly and stop after B05 V01.