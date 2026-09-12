# PROMPT 38 — INTEGRAR ATTEMPT06 Y CERRAR 0B-05C

## Objetivo

Integrar la ejecución **Attempt06** ya auditada externamente y cerrar científicamente/documentalmente **0B-05C**, sin abrir nuevas rondas de hardening técnico y sin ejecutar ningún experimento adicional.

La auditoría externa del resultado de Attempt06 es:

```text
AUDIT_VERDICT = PASS
INDEPENDENT_GIT_VERIFICATION = VERIFIED
ARTIFACT_STATE = APPROVED_FOR_INTEGRATION
ATTEMPT06 = COMPLETED / VERSIONED / RESULT_AUDITED
```

El hecho operacional `invocation_count=1 / no retry / no resume` queda respaldado por evidencia CODEX-local versionada y coherente, pero no se reinterpreta como observación independiente del host.

## 1. Refs congeladas de entrada

Repositorio: `elVladdi/gci-nandina-rag`

- `main` esperado: `e7cab327f0ef12b1e8ae21cddd01d215cd42db31`
- autorización Attempt06: `a9b06b8748316d7f3c403eaa9d55b735e12d96c3`
- ejecución Attempt06 auditada: `6846537602539506c8e90426daad05252cc982b9`
- rama ejecución: `codex/0b05c-v05-attempt06-execution`
- Plan canónico: rama `docs/plan-maestro-temporal-2026-08-31`, head de entrada `fe847f708d4d1ded92b5a50a38d4913bb69ed311`
- Article: `254b1e6df736fa9938ac86a515d65b36f4d361c5`

Antes de escribir, haz `git fetch` y verifica esas refs. Verifica además que:

1. `684653...` desciende linealmente de `a9b06b...`, que a su vez es hijo directo de `e7cab327...`;
2. el diff `a9b06b... -> 684653...` corresponde a outputs/versionado de Attempt06 y no modifica Plan, Article, EXP11B ni EXP12;
3. no existe otro commit posterior en la rama de ejecución que deba integrarse.

Si algo de esto falla: STOP.

---

# 2. Integración científica en main

Integra la rama de ejecución mediante **fast-forward only**:

```text
git checkout main
git merge --ff-only origin/codex/0b05c-v05-attempt06-execution
git push origin main
```

El `main` resultante debe ser exactamente:

`6846537602539506c8e90426daad05252cc982b9`

No hagas squash, rebase, amend, cherry-pick ni merge commit.

No ejecutes nuevamente ningún pipeline, retrieval, evaluación, D1a, EV03, EV04 o preflight científico. Solo verificaciones Git/read-only.

---

# 3. Interpretación científica congelada de 0B-05C

Registra exactamente la siguiente interpretación, derivada de los outputs ya auditados.

## 3.1 EV03

**Impacto agregado: cero.** Original y corrected son exactamente iguales en las métricas reportadas, incluyendo:

- MRR `0.40223149245938034`
- Top-1 `0.3494318181818182`
- Top-3 `0.4431818181818182`
- Top-5 `0.47632575757575757`
- Top-10 `0.5208333333333334`
- Top-50 / Recall@50 `0.5928030303030303`
- Recall@100 `0.6401515151515151`

Clasificación:

`EV03_METRIC_IMPACT = ZERO_AGGREGATE_CHANGE`

## 3.2 EV04

**Impacto agregado: cero.** Original y corrected son exactamente iguales, incluyendo:

- MRR `0.41801769149469725`
- MRR@100 `0.4209029085295853`
- MRR@200 `0.42114657818747986`
- contribución 101–200 `0.00024366965789453498`
- Top-1 `0.36742424242424243`
- Top-3 `0.45738636363636365`
- Top-5 `0.48295454545454547`
- Top-10 `0.5265151515151515`
- Top-50 / Recall@50 `0.6742424242424242`
- Recall@100 `0.740530303030303`

Clasificación:

`EV04_METRIC_IMPACT = ZERO_AGGREGATE_CHANGE`

## 3.3 D1a

La corrección Decision 906 produce un **impacto positivo no nulo en posiciones tempranas**, sin retraining:

| Métrica | Original | Corregida | Delta |
|---|---:|---:|---:|
| MRR@10 | 0.06823809523809526 | 0.08020006613756614 | +0.011961970899470875 |
| Top-1 | 0.032196969696969696 | 0.038825757575757576 | +0.006628787878787879 |
| Top-3 | 0.06723484848484848 | 0.08238636363636363 | +0.015151515151515152 |
| Top-5 | 0.08712121212121213 | 0.10321969696969698 | +0.01609848484848485 |
| Top-10 | 0.16287878787878787 | 0.17897727272727273 | +0.016098484848484862 |
| partida@10 | 0.42045454545454547 | 0.4393939393939394 | +0.018939393939393923 |
| sub_partida@10 | 0.3494318181818182 | 0.3683712121212121 | +0.018939393939393923 |
| clase@10 | 0.2774621212121212 | 0.29640151515151514 | +0.018939393939393923 |
| partida@50 | 0.7367424242424242 | 0.7414772727272727 | +0.004734848484848509 |
| sub_partida@50 | 0.6676136363636364 | 0.6714015151515151 | +0.0037878787878787845 |
| clase@50 | 0.6136363636363636 | 0.6174242424242424 | +0.0037878787878787845 |

Las métricas de jerarquía @100 y @200 permanecen sin cambio.

Clasificación:

`D1A_METRIC_IMPACT = POSITIVE_NONZERO_EARLY_RANK_CHANGE`

No declares significancia estadística, efecto causal ni generalización fuera de este análisis de sensibilidad determinista.

## 3.4 Conclusión 0B-05C

Registra:

```text
0B05C_METRIC_IMPACT = METHOD_DEPENDENT / NONZERO_ONLY_D1A
```

Interpretación concisa:

- la actualización normativa no altera las métricas agregadas de los recuperadores normativos BM25 EV03/EV04;
- sí mejora las métricas tempranas del recuperador denso D1a;
- por tanto, el drift normativo era material para D1a y debía corregirse, pero su efecto no es uniforme entre métodos.

---

# 4. Decisión downstream

No se requiere reejecución de experimentos downstream ya completados por este hallazgo, porque:

1. EXP11B Retrieval sigue sin haberse ejecutado;
2. EXP12 sigue sin haberse ejecutado;
3. Grupo 3 (métricas/inferencia) y Grupos 4–8 aún están pendientes;
4. por tanto, los pasos futuros pueden consumir directamente los resultados D1a corregidos de Attempt06.

Registra:

```text
DOWNSTREAM_REEXECUTION = NOT_REQUIRED
FUTURE_ANALYSES_MUST_USE = ATTEMPT06_CORRECTED_D1A_RESULTS
```

Esto no autoriza EXP11B ni EXP12; sus gates/deudas propios permanecen vigentes.

---

# 5. Cierre de 0B-05C

Tras integrar `684653...`, 0B-05C puede cerrarse:

```text
ATTEMPT06 = COMPLETED / AUDITED / INTEGRATED
0B05C_METRIC_IMPACT = METHOD_DEPENDENT / NONZERO_ONLY_D1A
DOWNSTREAM_REEXECUTION = NOT_REQUIRED
0B05C_CLOSURE = CLOSED / APPROVED
```

No abras otra remediación 0B-05C.

---

# 6. Reconciliación del Plan Maestro

Trabaja después **separadamente** en la rama:

`docs/plan-maestro-temporal-2026-08-31`

Modifica exclusivamente:

`docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md`

Actualiza el estado canónico de Grupo 2 y agrega una entrada cronológica de cierre 0B-05C que registre:

- `main = origin/main = 6846537602539506c8e90426daad05252cc982b9`;
- v0.5 integrada;
- autorización Attempt06 auditada;
- Attempt06 completado;
- 19/19 pasos PASS;
- impacto EV03 cero agregado;
- impacto EV04 cero agregado;
- D1a positivo no nulo en early-rank;
- `0B05C_METRIC_IMPACT=METHOD_DEPENDENT / NONZERO_ONLY_D1A`;
- `DOWNSTREAM_REEXECUTION=NOT_REQUIRED`;
- `0B05C_CLOSURE=CLOSED / APPROVED`;
- EXP11B portability debt conserva su estado previo;
- EXP11B/EXP12 no quedan autorizados por este cierre.

No reescribas historia previa ni borres los Attempts fail-closed; conserva su trazabilidad histórica.

Haz un único commit documental en esa rama y publícalo. No mezcles el commit del Plan con `main`.

Article debe permanecer exactamente en `254b1e6df736fa9938ac86a515d65b36f4d361c5`.

---

# 7. Reporte

Persiste obligatoriamente en `codex/prompts-temporary`:

`codex_prompts_tmp/38_RESPUESTA_INTEGRAR_ATTEMPT06_Y_CERRAR_0B05C.md`

Incluye:

- refs antes/después;
- verificación del fast-forward;
- main final;
- Plan commit nuevo y parent;
- Article ref sin cambios;
- resumen de impacto EV03/EV04/D1a;
- decisión downstream;
- estado de cierre 0B-05C;
- confirmación de que no se ejecutó ningún experimento adicional.

Estado final esperado:

```text
PROMPT38 = COMPLETED
MAIN = 6846537602539506c8e90426daad05252cc982b9
ATTEMPT06 = COMPLETED / AUDITED / INTEGRATED
0B05C_METRIC_IMPACT = METHOD_DEPENDENT / NONZERO_ONLY_D1A
DOWNSTREAM_REEXECUTION = NOT_REQUIRED
0B05C_CLOSURE = CLOSED / APPROVED
GROUP_2 = EN_CURSO
EXP11B_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```

No hagas ninguna otra actividad fuera de este alcance.
