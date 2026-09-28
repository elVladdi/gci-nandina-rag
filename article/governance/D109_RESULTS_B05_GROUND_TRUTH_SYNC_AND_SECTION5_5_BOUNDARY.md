# D-109 — Results B05 ground-truth synchronization and Section 5.5 boundary

## Español

```text
DECISION = D-109
PHASE = RESULTS
BLOCK = RESULTS_B05_SECTION_5_5
SECTION = 5.5 SENSITIVITY AND ROBUSTNESS ANALYSES
RQ = RQ4
CANONICAL_MASTER = ARTICLE_MASTER_V020
GROUND_TRUTH = SYNCHRONIZED
PROMPT_PREPARATION = ALLOWED
DRAFTING = NOT_YET_AUTHORIZED
RESULTS_B06_PLUS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

### 1. Baseline editorial

```text
MASTER_MD = article/manuscript/ARTICLE_MASTER_V020.md
MASTER_MD_SHA256 = eeb2ad72ba563267ea64cb6c91a798ff4f56a56b1d2946088a81ea02fc63006b
MASTER_MD_GIT_BLOB = 7393bf0db2d577d27168ccbb2a1060f1b337c872

MASTER_DOCX = ARTICLE_MASTER_CANDIDATE_RESULTS_B04_V01.docx
MASTER_DOCX_SHA256 = 57181016380550901c4c4e9dc9f8aa4bddb07bc3e7912e5e0c07088d9de42b92
COMMENTS = 40 / PRESERVE
TRACKED_CHANGES = 0 / PRESERVE
PAGE_COUNT = 54
```

### 2. Snapshot experimental y control de claims

```text
EXPERIMENTAL_SNAPSHOT = db0d0ad0d8435921a7838db6720eaea86a263763
PRIMARY_REGISTRY = outputs/analysis/group3/g3_metric_population_registry_v0.1.csv
PRIMARY_REGISTRY_GIT_BLOB = c63619b56a07e6b6d7be78b515d941ec3b205c41
CONTROL_REGISTRY = docs/analysis/group3/g3_claim_registry_v0.1.md
CONTROL_REGISTRY_GIT_BLOB = f3f6594277bfeede555f10887bcdb922efd23680
```

B05 consume únicamente evidencia descriptiva/sensibilidad ya gobernada por `C08`, `C22`, `C23`, `C24`, `C25`, `C26`, `C27` y, cuando se sintetiza la evidencia HE5, `C29`. Los valores numéricos siguientes son instanciaciones trazables de esos claims ya autorizados; no crean un claim causal, inferencial o de generalización nuevo.

`C09`, `C10` y `C11` permanecen prohibidos en sus formulaciones generales/causales. `C28` y los intervalos inferenciales de HE2 quedan reservados para §5.6.

### 3. EXP-11A — sensibilidad conjunta tamaño/composición

Fuente primaria:

```text
outputs/experiments/exp11a_historical_size_sensitivity_v0.3/exp11_metrics_by_condition.csv
GIT_BLOB = 535dd377d107ddcbf09ecaa13cd66ca723ee738d
```

La lectura científica autorizada es `EXP11A_SIZE_COMPOSITION_SENSITIVITY`, no efecto causal aislado del tamaño. Cada condición H25/H50/H75 contiene diez ejecuciones sobre el mismo EVAL; H100 es la referencia congelada única. El muestreo por DAM completo hace que el tamaño nominal y la composición cambien conjuntamente.

Resumen descriptivo congelado:

```text
CONDITION  RUNS  TOP1_MEAN   TOP3_MEAN   TOP5_MEAN   TOP10_MEAN  TOP50_MEAN  MRR100_MEAN
H25        10    0.493371    0.645170    0.737405    0.843277    0.973106    0.603787
H50        10    0.428598    0.597917    0.680303    0.776042    0.930492    0.542492
H75        10    0.298295    0.463352    0.548769    0.653883    0.837121    0.414030
H100        1    0.509470    0.671402    0.763258    0.891098    0.991477    0.629708
```

Rangos especialmente informativos, también congelados:

```text
H25 TOP3 = 0.540720–0.689394 ; MRR@100 = 0.510735–0.641314
H50 TOP3 = 0.491477–0.689394 ; MRR@100 = 0.431954–0.623899
H75 TOP3 = 0.283144–0.678977 ; MRR@100 = 0.248757–0.608612
H100 TOP3 = 0.671402          ; MRR@100 = 0.629708
```

El patrón observado no debe transformarse en una conclusión causal o monotónica sobre el tamaño del banco. La composición por DAM y cobertura NANDINA varía con las condiciones.

### 4. EXP-11B — H150/H200 pareado descriptivo

Fuente primaria:

```text
outputs/evaluation/exp11b_historical_retrieval_h150_h200_v0.1/exp11b_retrieval_condition_summary_v0.1.csv
GIT_BLOB = 144922ecee8ce9deda74db88e8dea85fb3af6f2e
```

Se completaron diez bancos H150 y diez H200, emparejados por seed y evaluados sobre el mismo EVAL de 1,056 series / 67 DAM. Las 10 x 1,056 filas repetidas no son 10,560 observaciones independientes y no existe una superpoblación congelada de seeds.

```text
CONDITION  RUNS  TOP1_MEAN   TOP3_MEAN   TOP5_MEAN   TOP10_MEAN  TOP50_MEAN  MRR100_MEAN
H150       10    0.512689    0.689962    0.783333    0.891572    0.989583    0.633268
H200       10    0.514110    0.689489    0.782008    0.895265    0.985227    0.633310
```

Las diferencias descriptivas son pequeñas y de signo mixto según métrica. Está prohibido convertir esta tabla en una conclusión general de mejora, empeoramiento, estabilización o ausencia de efecto, y está prohibida inferencia a una superpoblación de seeds/casos.

### 5. Sensibilidad correctiva 0B-05C — Attempt06

Solo Attempt06 es estado correctivo vigente. Intentos anteriores quedan superseded para la lectura actual.

#### EV03

Fuente:

```text
outputs/evaluation/0b05c_corrective_numerical_v0.5/ev03_aggregate_comparison_v0.5.json
GIT_BLOB = 1fa1aed2584c5612bbc5be16173e93d80c2dd92e
```

Resultado autorizado: `ZERO_AGGREGATE_CHANGE`. Los deltas agregados congelados para las métricas registradas son 0. Esto es una sensibilidad acotada del brazo ejecutado y no demuestra ausencia global de impacto normativo.

#### EV04

Fuente:

```text
outputs/evaluation/0b05c_corrective_numerical_v0.5/ev04_aggregate_comparison_v0.5.json
GIT_BLOB = 3bf28c036b0a0af5dd54d88c3b0050c60365b7f1
```

Resultado autorizado: `TINY_NONZERO_MRR_DECREASE_ONLY`.

```text
MRR@100: 0.0419812944 -> 0.0419717832 ; DELTA = -0.00000951116
MRR@200: 0.0433416116 -> 0.0433321004 ; DELTA = -0.00000951116
TOP1/TOP3/TOP5/TOP10/TOP50 = ZERO DELTA
RECALL@50/@100/@200 = ZERO DELTA
```

No se autoriza significancia ni causalidad.

#### D1a

Fuente:

```text
outputs/evaluation/d1a_corrective_0b05c_v0.5/d1a_corrective_vs_original_comparison_v0.5.json
GIT_BLOB = 6a26777395630722a18bca7826b7df96613ea4ea
```

Resultado autorizado: `POSITIVE_NONZERO_EXACT_RANKING_CHANGE_WITH_MINOR_HS4_MIXED_EFFECT`.

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

La lectura conjunta 0B-05C continúa siendo `METHOD_DEPENDENT / NONZERO_EV04_MRR_AND_D1A`, con `DOWNSTREAM_REEXECUTION = NOT_REQUIRED`. No resumir como impacto global cero.

### 6. HE5 / robustez descriptiva y no-estimabilidad

El registro cerrado mantiene:

```text
EXP12_DIVERSITY_EFFECT = NOT_ESTIMABLE
REASON = no D-HIGH / D-MID / D-LOW retrieval outputs were produced
DESCRIPTION_QUALITY_PREVALENCE = NOT_ESTIMABLE
REASON = no frozen case-level description-quality operationalization
HE5 = INCONCLUSIVE
```

Los errores Top-1 históricos (518 casos = 1056 - 538) se distribuyen en las categorías jerárquicas literales congeladas:

```text
SAME_CHAPTER = 147
SAME_HS4     = 284
SAME_HS6     = 87
```

Estos conteos son descriptivos y no autorizan concentración causal, umbral post-hoc ni inferencia externa.

La estratificación por soporte histórico conserva literalmente los cuatro buckets, sin etiquetar ninguno como “insuficiente”:

```text
BUCKET    CASES   TOP1       TOP3       MRR@100
1 DAM       27    0.370370   0.703704   0.564447
2 DAM       21    0.047619   0.190476   0.239384
3-4 DAM    425    0.691765   0.767059   0.760152
5+ DAM     583    0.399657   0.617496   0.551697
```

Fuente:

```text
outputs/evaluation/he5_integrated_error_analysis_v0.2/he5_historical_errors_by_support_v0.2.csv
GIT_BLOB = 0f70928ba83eec87c116e62cf104f505293bc092
outputs/evaluation/he5_integrated_error_analysis_v0.2/he5_historical_hierarchy_errors_v0.2.csv
GIT_BLOB = b5bd099114e7262f316dfc846b867bec9e7f176d
```

No existe umbral congelado que convierta uno de estos buckets en “insufficient support”, y las diferencias no son un efecto causal del soporte.

### 7. Frontera narrativa de §5.5

§5.5 puede reportar exclusivamente sensibilidad y robustez descriptiva ya reconciliadas:

1. EXP11A como variación conjunta de tamaño/composición;
2. EXP11B como comparación descriptiva pareada de diez seeds sobre el mismo EVAL;
3. sensibilidad correctiva final 0B-05C con respuesta dependiente del método;
4. resultados HE5 descriptivos y sus objetos no estimables.

§5.5 no debe contener intervalos de confianza, bootstrap DAM, p-values, significancia, disposición HE2, ni presentar `HE2 = SUPPORTED`; esos objetos pertenecen a §5.6. Tampoco debe declarar causalidad, generalización fuera del benchmark, legal correctness, ni resultados de Discussion.

`HE5 = INCONCLUSIVE` puede expresarse funcionalmente como evidencia insuficiente para una conclusión global bajo las dimensiones previstas; no usar EXP12 como evidencia positiva o negativa del efecto de diversidad.

### 8. Gate

```text
RESULTS_B05_GROUND_TRUTH = SYNCHRONIZED
NEXT_ACTOR = IA_GESTORA
NEXT_ACTION = PREPARE_AND_AUDIT_B05_PROMPT
AUTHOR_APPROVAL_GATE = NOT_OPEN
RESULTS_B06_PLUS = NOT_AUTHORIZED
```

---

## English

Results B05 / Section 5.5 ground truth is synchronized to the frozen Group-3 registry and surviving sensitivity artifacts at `main@db0d0ad0d8435921a7838db6720eaea86a263763`. EXP11A is a joint size/composition sensitivity and cannot identify an isolated causal bank-size effect. EXP11B is a ten-seed paired descriptive H150/H200 sensitivity on the same 1,056-case EVAL and supports no seed-superpopulation inference. Final 0B-05C Attempt06 is method-dependent: EV03 shows zero aggregate change, EV04 only a tiny non-zero MRR decrease, and D1a shows non-zero exact-ranking changes with a minor mixed HS4 effect. EXP12 diversity and ambiguous/incomplete-description prevalence remain not estimable; HE5 remains inconclusive. Inferential HE2 intervals/disposition are reserved for Section 5.6.