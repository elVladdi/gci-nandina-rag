# PROMPT 39 — CORREGIR INTERPRETACIÓN ATTEMPT06 Y RECONCILIAR PLAN

## Objetivo

Corregir **exclusivamente la interpretación científica/documental de Attempt06 que quedó registrada por Prompt38**, sin ejecutar ningún experimento, sin modificar los outputs científicos ya versionados y sin revertir la integración válida de Attempt06 en `main`.

La auditoría externa posterior a Prompt38 detectó que **la integración Git fue correcta, pero la interpretación numérica congelada en Prompt38 no corresponde a los artefactos efectivos de Attempt06**. En particular:

- los valores publicados para EV03 no coinciden con `ev03_aggregate_comparison_v0.5.json`;
- EV04 fue clasificado erróneamente como cambio agregado exactamente cero, aunque `MRR@100` y `MRR@200` presentan un delta negativo pequeño pero no nulo;
- los valores D1a registrados por Prompt38 no corresponden a `d1a_corrective_vs_original_comparison_v0.5.json`; además, ese contrato contiene `MRR@100` y `MRR@200`, no `MRR@10`;
- por lo tanto, `0B05C_METRIC_IMPACT = METHOD_DEPENDENT / NONZERO_ONLY_D1A` es incorrecto.

**No hay defecto identificado en la ejecución Attempt06 ni en el commit científico `684653...`. El defecto es interpretativo/documental.**

---

## 1. Refs congeladas

Repositorio: `elVladdi/gci-nandina-rag`

Verifica antes de escribir:

- `origin/main == 6846537602539506c8e90426daad05252cc982b9`;
- `origin/codex/0b05c-v05-attempt06-execution == 6846537602539506c8e90426daad05252cc982b9`;
- `origin/docs/plan-maestro-temporal-2026-08-31 == 6b1323cc97c1b94119f226768dd4b8cbda273ccb`;
- `origin/article/main-manuscript == 254b1e6df736fa9938ac86a515d65b36f4d361c5`.

Si cualquiera falla: STOP y reporta `PRECONDITION_REF_DRIFT`.

`main` **no debe cambiar** durante Prompt39.

---

## 2. Fuentes de verdad obligatorias

Lee directamente desde `main=684653...` estos artefactos y verifica sus blobs Git:

### EV03

`outputs/evaluation/0b05c_corrective_numerical_v0.5/ev03_aggregate_comparison_v0.5.json`

Blob esperado:

`1fa1aed2584c5612bbc5be16173e93d80c2dd92e`

### EV04

`outputs/evaluation/0b05c_corrective_numerical_v0.5/ev04_aggregate_comparison_v0.5.json`

Blob esperado:

`3bf28c036b0a0af5dd54d88c3b0050c60365b7f1`

### D1a comparación

`outputs/evaluation/d1a_corrective_0b05c_v0.5/d1a_corrective_vs_original_comparison_v0.5.json`

Blob esperado:

`6a26777395630722a18bca7826b7df96613ea4ea`

### D1a métricas original/corregida

Original:

`outputs/evaluation/text2trade_mnrl_data_aduanas_clase87_v0.2/d1a_metrics.json`

Blob esperado:

`ebdf4504614db6c702cdbad56edfbe012e799ba5`

Corregida:

`outputs/evaluation/d1a_corrective_0b05c_v0.5/d1a_metrics.json`

Blob esperado:

`73e062b927d059a9f4e52caab7b785eafb6f2e01`

Si alguno no coincide: STOP / `SOURCE_OF_TRUTH_BINDING_MISMATCH`.

No uses los números de Prompt38 como fuente de verdad. No recalcules desde datos crudos si los comparadores versionados ya contienen el valor contractual.

---

## 3. Interpretación correcta que debe registrarse

### 3.1 EV03

Clasificación:

```text
EV03_METRIC_IMPACT = ZERO_AGGREGATE_CHANGE
```

Valores contractuales original = corrected:

- MRR = `0.04229731726741296`;
- Top-1 = `0.027462121212121212`;
- Top-3 = `0.05113636363636364`;
- Top-5 = `0.061553030303030304`;
- Top-10 = `0.06534090909090909`;
- Top-50 = Recall@50 = `0.07007575757575757`;
- Recall@100 = `0.07102272727272728`.

La clasificación de cambio cero permanece válida, pero los números registrados por Prompt38 deben marcarse como **superseded / incorrect source binding**.

### 3.2 EV04

Clasificación canónica corregida:

```text
EV04_METRIC_IMPACT = TINY_NONZERO_MRR_DECREASE_ONLY
```

Valores contractuales:

- MRR@100 original = `0.04198129438896378`;
- MRR@100 corrected = `0.041971783226435376`;
- delta = `-9.511162528404171e-06`;
- MRR@200 original = `0.04334161160288281`;
- MRR@200 corrected = `0.043332100440354404`;
- delta = `-9.511162528404171e-06`;
- contribución MRR 101–200 original = corrected = `0.0013603172139190346`;
- Top-1 original = corrected = `0.026515151515151516`;
- Top-3 original = corrected = `0.052083333333333336`;
- Top-5 original = corrected = `0.0625`;
- Top-10 original = corrected = `0.06534090909090909`;
- Top-50 / Recall@50 original = corrected = `0.09090909090909091`;
- Recall@100 original = corrected = `0.10132575757575757`;
- Recall@200 original = corrected = `0.3039772727272727`.

El comparador versionado muestra que los demás indicadores discretos/hierárquicos contenidos en ese agregado permanecen con delta cero. El cambio no nulo está en MRR@100 y MRR@200 y ocurre dentro de los primeros 100 rangos, porque la contribución 101–200 permanece idéntica.

No llames a EV04 `ZERO_AGGREGATE_CHANGE`.

### 3.3 D1a

No existe `MRR@10` en el comparador contractual v0.5. Registra únicamente las métricas que realmente contiene `d1a_corrective_vs_original_comparison_v0.5.json`.

Clasificación:

```text
D1A_METRIC_IMPACT = POSITIVE_NONZERO_EXACT_RANKING_CHANGE_WITH_MINOR_HS4_MIXED_EFFECT
```

Valores contractuales principales:

| Métrica | Original | Corrected | Delta |
|---|---:|---:|---:|
| Top@1 | 0.0 | 0.000946969696969697 | +0.000946969696969697 |
| Top@3 | 0.003787878787878788 | 0.010416666666666666 | +0.006628787878787878 |
| Top@5 | 0.03409090909090909 | 0.05113636363636364 | +0.01704545454545455 |
| Top@10 | 0.15625 | 0.17803030303030304 | +0.02178030303030304 |
| Top@50 | 0.3058712121212121 | 0.3134469696969697 | +0.0075757575757576245 |
| Recall@100 | 0.3456439393939394 | 0.3456439393939394 | 0.0 |
| Recall@200 | 0.3626893939393939 | 0.36363636363636365 | +0.0009469696969697239 |
| MRR@100 | 0.03242432639034634 | 0.038087139731859634 | +0.0056628133415132925 |
| MRR@200 | 0.03254853477630825 | 0.038217181295822696 | +0.005668646519514445 |
| Exact@100 | 0.3456439393939394 | 0.3456439393939394 | 0.0 |
| Exact@200 | 0.3626893939393939 | 0.36363636363636365 | +0.0009469696969697239 |
| HS6@100 | 0.36553030303030304 | 0.36553030303030304 | 0.0 |
| HS6@200 | 0.38825757575757575 | 0.38825757575757575 | 0.0 |
| HS4@100 | 0.8731060606060606 | 0.8797348484848485 | +0.006628787878787956 |
| HS4@200 | 0.9640151515151515 | 0.9630681818181818 | -0.0009469696969697239 |
| Chapter@100 | 0.9801136363636364 | 0.9801136363636364 | 0.0 |
| Chapter@200 | 1.0 | 1.0 | 0.0 |

Interpretación permitida:

- las métricas exactas/ranking temprano de D1a mejoran de forma no nula;
- MRR@100 y MRR@200 aumentan;
- Recall/Exact@200 aumenta en un caso;
- HS4@100 mejora, mientras HS4@200 disminuye en un caso equivalente a `1/1056`;
- no es correcto decir que toda la jerarquía @100/@200 permanece sin cambio;
- no declarar significancia estadística, efecto causal ni generalización.

### 3.4 Conclusión 0B-05C corregida

Registra exactamente:

```text
0B05C_METRIC_IMPACT = METHOD_DEPENDENT / NONZERO_EV04_MRR_AND_D1A
```

Interpretación:

- EV03: cambio agregado exactamente cero;
- EV04: cambio no nulo, muy pequeño y negativo, restringido a MRR@100/MRR@200; los indicadores discretos reportados permanecen iguales;
- D1a: cambio no nulo predominantemente positivo en ranking exacto y MRR, con un efecto jerárquico menor mixto en HS4;
- el efecto del drift normativo no es uniforme entre métodos.

---

## 4. Decisión downstream

La auditoría externa mantiene:

```text
DOWNSTREAM_REEXECUTION = NOT_REQUIRED
FUTURE_ANALYSES_MUST_USE = ATTEMPT06_CORRECTED_RESULTS
```

Razón: EXP11B Retrieval y EXP12 siguen no ejecutados; Grupo 3 y Grupos 4–8 están pendientes. No hay resultado downstream completado que deba repetirse; los pasos futuros deben consumir/interpretar los resultados contractuales correctos de Attempt06.

Esto **no autoriza** EXP11B ni EXP12.

---

## 5. Estado de integración y cierre

No reviertas `main`. La integración científica de Attempt06 en `684653...` es válida y debe preservarse.

Durante esta corrección documental registra:

```text
ATTEMPT06 = COMPLETED / AUDITED_EXECUTION / INTEGRATED
PROMPT38_RESULT_INTERPRETATION = REJECTED / SUPERSEDED_BY_PROMPT39
0B05C_CLOSURE = PENDING_CORRECTIVE_RECONCILIATION
```

Tras completar correctamente la reconciliación del Plan en este Prompt39, el estado canónico puede quedar:

```text
0B05C_CLOSURE = CLOSED / APPROVED_AFTER_CORRECTIVE_RECONCILIATION
```

No abras una nueva ejecución 0B-05C y no autorices otra corrida.

---

## 6. Reconciliación correctiva del Plan Maestro

Trabaja exclusivamente en:

`docs/plan-maestro-temporal-2026-08-31`

Base obligatoria:

`6b1323cc97c1b94119f226768dd4b8cbda273ccb`

Modifica exclusivamente:

`docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md`

Haz **un único commit documental correctivo**, hijo directo de `6b1323...`.

Debes:

1. corregir el estado resumido de Grupo 2;
2. corregir el bloque de orden maestro 0B-05C;
3. conservar la entrada histórica de Prompt38, pero marcar explícitamente su interpretación numérica/clasificación como `SUPERSEDED_BY_POST_PROMPT38_EXTERNAL_AUDIT` en vez de borrarla silenciosamente;
4. agregar una nueva entrada cronológica `2026-09-12 — Corrección de interpretación Attempt06 posterior a Prompt38` con:
   - las tres rutas fuente y blobs Git de EV03/EV04/D1a;
   - los valores contractuales anteriores;
   - `EV03_METRIC_IMPACT=ZERO_AGGREGATE_CHANGE`;
   - `EV04_METRIC_IMPACT=TINY_NONZERO_MRR_DECREASE_ONLY`;
   - `D1A_METRIC_IMPACT=POSITIVE_NONZERO_EXACT_RANKING_CHANGE_WITH_MINOR_HS4_MIXED_EFFECT`;
   - `0B05C_METRIC_IMPACT=METHOD_DEPENDENT / NONZERO_EV04_MRR_AND_D1A`;
   - `DOWNSTREAM_REEXECUTION=NOT_REQUIRED`;
   - `FUTURE_ANALYSES_MUST_USE=ATTEMPT06_CORRECTED_RESULTS`;
   - `0B05C_CLOSURE=CLOSED / APPROVED_AFTER_CORRECTIVE_RECONCILIATION`;
   - EXP11B portability debt continúa `OPEN`;
   - EXP11B Retrieval y EXP12 continúan `NOT_AUTHORIZED / NOT_EXECUTED`.

No modifiques `main`, `article/`, EXP11B ni EXP12.

---

## 7. Prohibiciones

- NO ejecutar EV03, EV04, D1a ni unified nuevamente.
- NO ejecutar retrieval científico.
- NO ejecutar tests científicos.
- NO recalcular métricas desde datasets si el comparador versionado ya es la fuente contractual.
- NO modificar ningún output de Attempt06.
- NO modificar el commit `684653...`.
- NO hacer rollback de `main`.
- NO modificar Article.
- NO autorizar EXP11B ni EXP12.
- NO iniciar el siguiente bloque del Plan.

Solo Git/read-only + corrección documental del Plan.

---

## 8. Reporte obligatorio

Persistir en rama `codex/prompts-temporary`:

`codex_prompts_tmp/39_RESPUESTA_CORREGIR_INTERPRETACION_ATTEMPT06_Y_RECONCILIAR_PLAN.md`

El reporte debe separar factual y explícitamente:

- refs iniciales y finales;
- verificación de blobs fuente;
- lista de discrepancias Prompt38 → artefactos reales;
- valores correctos EV03/EV04/D1a;
- clasificación corregida;
- confirmación de que `main` permaneció exactamente en `684653...`;
- nuevo commit del Plan y parent exacto `6b1323...`;
- único path modificado en Plan;
- Article sin cambios;
- EXP11B/EXP12 sin cambios;
- confirmación de cero ejecución científica adicional.

Estado final esperado si todo cumple:

```text
PROMPT39 = COMPLETED
MAIN = 6846537602539506c8e90426daad05252cc982b9
ATTEMPT06 = COMPLETED / AUDITED_EXECUTION / INTEGRATED
PROMPT38_RESULT_INTERPRETATION = REJECTED / SUPERSEDED_BY_PROMPT39
EV03_METRIC_IMPACT = ZERO_AGGREGATE_CHANGE
EV04_METRIC_IMPACT = TINY_NONZERO_MRR_DECREASE_ONLY
D1A_METRIC_IMPACT = POSITIVE_NONZERO_EXACT_RANKING_CHANGE_WITH_MINOR_HS4_MIXED_EFFECT
0B05C_METRIC_IMPACT = METHOD_DEPENDENT / NONZERO_EV04_MRR_AND_D1A
DOWNSTREAM_REEXECUTION = NOT_REQUIRED
FUTURE_ANALYSES_MUST_USE = ATTEMPT06_CORRECTED_RESULTS
0B05C_CLOSURE = CLOSED / APPROVED_AFTER_CORRECTIVE_RECONCILIATION
GROUP_2 = EN_CURSO
EXP11B_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```

Responde únicamente con el reporte final exigido.
