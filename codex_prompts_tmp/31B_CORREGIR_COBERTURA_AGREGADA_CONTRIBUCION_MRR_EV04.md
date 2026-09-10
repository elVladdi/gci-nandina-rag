# PROMPT 31B — CORREGIR COBERTURA AGREGADA EV04: CONTRIBUCIÓN MRR 101–200

## Rol

Actúa como **ejecutor técnico controlado**. Corrige exclusivamente el nuevo hallazgo bloqueante detectado por la auditoría externa del candidato Prompt31A. No reinicies el diseño v0.4 y no reabras los hallazgos F31A-01..04 ya corregidos salvo para verificar que continúan cerrados.

Este bloque **NO autoriza Attempt05** y **NO autoriza ejecución numérica real**.

No ejecutes retrieval, EV03 real, EV04 real, D1a real, EVAL real ni inferencia del modelo.

---

## 1. Baseline y ramas protegidas

Repositorio: `elVladdi/gci-nandina-rag`

Baseline científico protegido:

`main = ba4bd2936bbf1930b87aa5f3abe028df1dbdf6a9`

Candidato Prompt31 rechazado:

`69a05710295556e365086c52f93933c5b3a2ad1c`

Candidato Prompt31A rechazado por este hallazgo:

`9cfbf28f221f2f2761b3a4b7ab60cd870a8557de`

No modifiques ni fuerces ninguna de esas ramas publicadas.

Crea una rama nueva desde el baseline exacto:

`codex/0b05c-v04-complete-preexecution-candidate-v03`

La historia final debe tener como parent científico directo `ba4bd2936bbf1930b87aa5f3abe028df1dbdf6a9`; ni `69a057...` ni `9cfbf28...` deben ser ancestros. Puedes traer el diff de `9cfbf28...` al índice con `git cherry-pick -n` o mecanismo equivalente sin crear commit intermedio, aplicar la corrección y producir un único commit científico final.

Antes de editar verifica:

- `origin/main == ba4bd2936bbf1930b87aa5f3abe028df1dbdf6a9`;
- Plan `fe847f708d4d1ded92b5a50a38d4913bb69ed311`;
- article `254b1e6df736fa9938ac86a515d65b36f4d361c5`;
- rama Prompt31 sigue en `69a05710295556e365086c52f93933c5b3a2ad1c`;
- rama Prompt31A sigue en `9cfbf28f221f2f2761b3a4b7ab60cd870a8557de`;
- no existe authorization record v0.4 real;
- Attempt05 sigue `NOT_AUTHORIZED / NOT_EXECUTED`;
- working tree tracked limpio.

Si falla cualquiera: `STOP / FAIL_CLOSED`.

---

# 2. Hallazgo F31B-01 — la contribución MRR 101–200 desaparece del aggregate comparison

El candidato Prompt31A corrigió correctamente el baseline agregado EV04 para usar métricas canónicas derivadas del control. Sin embargo, el productor agregado sigue heredando:

`src/experiments/evaluate_normative_bm25_corrective_0b05c_v01.py:produce_aggregate_comparison`

Ese helper compara **exclusivamente `metric_table`**.

En v0.4, el `metric_table` canónico tiene 27 filas:

- `mrr_at_100`;
- `mrr_at_200`;
- las 25 filas legacy posteriores a `mrr`.

La métrica:

`mrr_101_200_contribution`

existe como campo top-level, junto con `mrr_101_200_contribution_numerator`, pero **no forma parte de `metric_table`**. Por tanto, el aggregate comparison producido actualmente omite silenciosamente la contribución 101–200.

Esto incumple la exigencia de Prompt31A de que el zero-delta agregado incluya también `mrr_101_200_contribution`, y dejaría fuera del artefacto comparativo una métrica específicamente definida para cuantificar la masa MRR entre rangos 101–200.

La respuesta Prompt31A afirmó que esa contribución estaba incluida en las filas agregadas, pero el código y el test no lo garantizan: el test solo exige presencia de `mrr_at_100` y `mrr_at_200`.

## Corrección obligatoria

**No cambies el schema canónico de métricas v0.4 de 92 keys / 27 filas `metric_table`**, salvo que encuentres una contradicción metodológica nueva y te detengas `FAIL_CLOSED`. La contribución puede seguir siendo top-level.

Crea una comparación agregada específica para EV04, explícita y auditable, por ejemplo:

`produce_ev04_aggregate_comparison_v04(original_metrics, corrective_metrics)`

en `evaluate_normative_bm25_corrective_0b05c_v04.py`.

Contrato obligatorio:

1. conservar las 27 filas canónicas actuales de `metric_table`;
2. representar además `mrr_101_200_contribution` como una fila agregada propia;
3. orden agregado exacto recomendado:
   - `mrr_at_100`
   - `mrr_at_200`
   - `mrr_101_200_contribution`
   - las 25 métricas legacy restantes en el orden ya congelado;
4. total esperado: **28 filas agregadas EV04**;
5. la fila de contribución debe usar:
   - `original_numerator = original_metrics["mrr_101_200_contribution_numerator"]`;
   - `corrected_numerator = corrective_metrics["mrr_101_200_contribution_numerator"]`;
   - denominador = case count canónico, validado de forma exacta entre original y corrected;
   - `original_value = original_metrics["mrr_101_200_contribution"]`;
   - `corrected_value = corrective_metrics["mrr_101_200_contribution"]`;
   - `absolute_delta = corrected - original`;
6. exige presencia, tipos numéricos finitos y coherencia del denominador antes de emitir la fila;
7. define un orden/contrato explícito, por ejemplo `EV04_AGGREGATE_METRIC_ORDER`, para impedir omisiones silenciosas;
8. `mrr` legacy no debe duplicarse como fila adicional: `mrr_at_200` ya es su alias contractual;
9. `mrr_definition` y campos auxiliares no métricos no se convierten en filas;
10. EV03 debe seguir usando su comparación agregada histórica sin cambios científicos.

Actualiza `run_0b05c_corrective_numerical_v04.py:compare_aggregates()` para usar:

- EV03 → helper legacy existente;
- EV04 → nuevo helper agregado v0.4 de 28 filas.

---

# 3. Auditoría ampliada de cobertura métrica — obligatoria

Antes de publicar, realiza una auditoría de cobertura para evitar otro ciclo por omisión de métricas.

Debes demostrar explícitamente:

1. canonical EV04 mantiene `92 keys` y `27 metric_table rows`;
2. aggregate EV04 contiene exactamente `28 rows`;
3. sus nombres son exactamente:
   `mrr_at_100`, `mrr_at_200`, `mrr_101_200_contribution` + las 25 métricas legacy restantes;
4. ninguna métrica numérica científicamente reportable de la extensión MRR v0.4 queda omitida;
5. `mrr_at_200 == mrr` sigue siendo alias exacto y no se duplica en el aggregate;
6. original canonical vs original canonical produce delta `0.0` en las 28 filas;
7. alterar únicamente `mrr_101_200_contribution` y/o su numerador produce una fila de contribución distinta y no puede quedar invisible;
8. falta de `mrr_101_200_contribution`, falta de su numerador o incoherencia de denominador debe `FAIL_CLOSED`;
9. el unified summary puede consumir el aggregate EV04 de 28 filas sin asumir 27;
10. runtime ledger, manifest y paths no cambian salvo bindings/hash derivados mecánicamente de los archivos v0.4 modificados.

Persistir esta revisión en:

`outputs/audits/0b05c_v04_preexecution_shadow/preexecution_shadow_audit_v0.4.json`

Añade:

- `F31B-01 = CORRECTED` solo si pasa;
- `ev04_aggregate_metric_count = 28`;
- orden exacto;
- zero-delta 28/28;
- negative coverage controls.

Conserva F31A-01..04 como corregidos únicamente si siguen verificándose.

---

# 4. Positive authorization path no debe degradarse

Como cambiarán blobs del evaluator/runner y por tanto los bindings canónicos, regenera mecánicamente gate/specs/manifest/ledger v0.4 según corresponda.

Repite **solo** las comprobaciones positivas necesarias para confirmar que el cambio de blobs no rompe:

- candidate → authorization transition;
- `preflight_authorized()`;
- adapter D1a v0.4;
- immutable projection;
- future roots absent.

Puedes reutilizar el mecanismo disposable Git de Shadow G2. No ejecutes `execute_authorized()`.

La clasificación sigue siendo:

`CODEX_LOCAL_PURE_READ_ONLY_OR_DISPOSABLE_GIT_TEST / NOT_INDEPENDENT_GITHUB_CI`.

---

# 5. Tests mínimos

Ejecuta como mínimo:

```text
python -B -m unittest \
  tests.test_0b05c_ev04_mrr_contract_v04 \
  tests.test_0b05c_corrective_numerical_gate_v04 \
  tests.test_d1a_corrective_0b05c_runner_v04
```

Añade/ajusta tests para exigir expresamente:

- aggregate EV04 = 28 filas;
- contribución presente en posición contractual;
- zero-delta de contribución;
- mutación de contribución observable;
- missing contribution/numerator/denominator mismatch → fail closed;
- canonical metric schema permanece 92/27;
- positive auth path sigue PASS en shadow disposable.

No repitas suites históricas v0.1/v0.2/v0.3 si sus blobs no cambian.

---

# 6. Alcance del candidato

Mantén los mismos **14 paths v0.4** del candidato Prompt31A. No añadas nuevos archivos salvo necesidad estrictamente justificada.

No modifiques ningún path histórico/v0.3.

No crear:

- authorization record v0.4 real;
- outputs runtime;
- Attempt05;
- cambios Plan/article/EXP11B/EXP12.

El candidato final debe seguir completamente no autorizado.

---

# 7. Commit y publicación

Produce un único commit científico con parent directo:

`ba4bd2936bbf1930b87aa5f3abe028df1dbdf6a9`

Publica únicamente:

`codex/0b05c-v04-complete-preexecution-candidate-v03`

No integres a `main`.

No publiques ninguna rama sintética de autorización.

---

# 8. Reporte obligatorio

Persiste el reporte en:

`codex_prompts_tmp/31B_RESPUESTA_CORREGIR_COBERTURA_AGREGADA_CONTRIBUCION_MRR_EV04.md`

sobre:

`codex/prompts-temporary`

Incluye obligatoriamente:

- baseline y refs protegidas;
- candidatos rechazados `69a057...` y `9cfbf28...`;
- branch/commit/tree/parent final;
- lista exacta de 14 paths y blobs;
- `F31B-01` y evidencia;
- cobertura aggregate 28 filas y orden exacto;
- zero-delta 28/28;
- controles negativos de contribución;
- estado F31A-01..04;
- resultado Shadow G2 actualizado;
- tests locales y su clasificación probatoria;
- ausencia de authorization record real;
- `Attempt05 = NOT_AUTHORIZED / NOT_EXECUTED`;
- `0B05C_METRIC_IMPACT = NOT_DETERMINED`;
- `0B05C_CLOSURE = NOT_AUTHORIZED`;
- `main` sin cambios.

Responde únicamente con el reporte final exigido.
