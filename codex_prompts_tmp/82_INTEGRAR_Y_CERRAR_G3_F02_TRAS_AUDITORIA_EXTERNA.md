# PROMPT 82 — INTEGRAR Y CERRAR EXCLUSIVAMENTE G3-F02 TRAS AUDITORÍA EXTERNA

## 0. Naturaleza de esta ejecución

Esta es una ejecución **administrativa de integración y cierre** de G3-F02.

La IA Experimental realizó auditoría externa independiente del candidato producido por Prompt81 y el dictamen es:

```text
G3_F02_EXTERNAL_AUDIT = PASS
SCIENTIFIC_CORRECTION_REQUIRED = false
SCIENTIFIC_RERUN_REQUIRED = false
METRICS_RECOMPUTATION_REQUIRED = false
INFERENTIAL_EXECUTION_AUTHORIZED = false
G3_F03_AUTHORIZED = false
```

La auditoría confirmó, entre otros puntos:

- candidato exactamente 1 commit por delante y 0 detrás de `main`;
- exactamente 3 paths científicos autorizados;
- 548 filas y 16 familias de evidencia;
- 4 familias `ELIGIBLE`, 11 `DESCRIPTIVE_ONLY`, 1 `NOT_ESTIMABLE`, 0 `NOT_APPLICABLE`;
- cero filas sin procedencia;
- cero uso vigente del split obsoleto 3000/1006;
- cero mezcla de EVAL incompatibles;
- 0B-05C usa únicamente Attempt06 corregido como evidencia vigente;
- EXP11A y EXP11B permanecen sensibilidad descriptiva, sin pseudorreplicación ni causalidad aislada;
- HE5 conserva límites descriptivos y evita operacionalizaciones post hoc;
- EXP12 permanece `NOT_ESTIMABLE`, sin retrieval ni condiciones seleccionadas;
- no se ejecutó inferencia, bootstrap, p-values, effect sizes ni decisión HE2/HE5.

Existe una observación documental **no bloqueante**: algunas filas de `source_commit_binding` contienen dos referencias etiquetadas literalmente como `main=...` para distinguir el anclaje actual y un snapshot histórico. Los SHA exactos, blobs y paths permanecen explícitos y verificables, por lo que esto no invalida la procedencia ni requiere modificar el candidato. **No corrijas ni regeneres los artefactos científicos por esta observación.** Regístrala únicamente como nota de auditoría para que futuros registros usen etiquetas más explícitas (`current_main`, `historical_main` o equivalente).

Tu tarea es integrar exactamente el candidato auditado, reconciliar Plan Maestro y registro de fichas y cerrar G3-F02. No debes ejecutar G3-F03.

---

## 1. Repositorio y refs congelados de entrada

Repositorio:

```text
elVladdi/gci-nandina-rag
```

Antes de modificar cualquier cosa ejecuta `git fetch origin` y verifica exactamente:

```text
origin/main = 366bf529c29cb999bfd043db33674a510ba184c7
origin/docs/plan-maestro-temporal-2026-08-31 = 59e7fc935dd5cde9a22bb2743a4116f35ad60a26
origin/docs/fichas-grupos-3-8 = af9fd5a39360a37c3c13d397592059592aee6d07
origin/article/main-manuscript = f02aef2448b7b8c0db2df4895c02860b66786716
```

Candidato G3-F02 auditado:

```text
branch = codex/group3-f02-metric-population-registry-v01
commit = adf70d6eb880c567d6efa0f27b5c79259b8db2a6
parent = 366bf529c29cb999bfd043db33674a510ba184c7
```

Prompt81 y respuesta:

```text
PROMPT81_COMMIT = 2fe464a244b0d75acfde9555d072db9be0142379
PROMPT81_RESPONSE_COMMIT = da08ded0eb0d518d60431860f7e1d2df82313a71
```

Activación y estado de fichas ya materializados:

```text
G3_F02_ACTIVATION_COMMIT = f7b377b09588cb051745f0daef72a1d87ecbd69c
G3_F02_FINAL_CANDIDATE_STATE_COMMIT = af9fd5a39360a37c3c13d397592059592aee6d07
```

Si `main`, Plan, fichas, artículo o la rama candidata científica presentan drift no explicado respecto de estos refs:

```text
STOP / REF_DRIFT_DETECTED
```

El avance de `codex/prompts-temporary` debido exclusivamente a la incorporación de este Prompt82 es esperado y no constituye drift científico.

---

## 2. Verificación obligatoria del candidato antes de integrar

Compara:

```text
366bf529c29cb999bfd043db33674a510ba184c7
..
adf70d6eb880c567d6efa0f27b5c79259b8db2a6
```

Debe resultar exactamente:

```text
commits_ahead = 1
commits_behind = 0
changed_path_count = 3
```

Únicos paths permitidos:

```text
outputs/analysis/group3/g3_metric_population_registry_v0.1.csv
outputs/analysis/group3/g3_metric_population_registry_v0.1.json
outputs/analysis/group3/g3_metric_population_registry_v0.1_hash_ledger.csv
```

Verifica además estos blobs del candidato:

```text
CSV_BLOB = c63619b56a07e6b6d7be78b515d941ec3b205c41
JSON_BLOB = 5ea33ca583b18426374fa15baf1b1759e76cd99e
HASH_LEDGER_BLOB = 521bfcdf34d03c4effa8b8ef19f9777b6827d439
```

Y hashes registrados:

```text
CSV_SHA256 = 65294f0e81de358f8cdab4d3997d1c8fe03062f2d3e5b6a95cbca5da885c5c41
JSON_SHA256 = 673b43e9ef5ed20bc6aafa9c674e6bbdba5cdbd054dd47f40bf14d05c8d1ae7b
HASH_LEDGER_SHA256 = 3c372dfcc9f4181795ad69418c4161b9dde63bc88c3261cf79b79082d97fb5f1
```

No recalcules resultados científicos. Las verificaciones de integridad/hash son administrativas y sí están permitidas.

Si la estructura, commits o blobs no coinciden:

```text
STOP / AUDITED_CANDIDATE_MISMATCH
```

---

## 3. Prohibiciones absolutas

Durante Prompt82 está prohibido:

- modificar cualquiera de los 3 artefactos científicos de G3-F02;
- regenerar CSV, JSON o ledger;
- recalcular métricas;
- reejecutar retrieval/BM25;
- ejecutar bootstrap;
- calcular intervalos nuevos;
- calcular p-values;
- calcular effect sizes;
- decidir HE2;
- decidir HE5;
- reabrir EXP12;
- iniciar, activar o ejecutar G3-F03;
- modificar `article/main-manuscript`;
- modificar definiciones prospectivas de fichas individuales para simular estados históricos;
- hacer force-push;
- hacer squash/rebase/amend del candidato científico.

---

## 4. Integración científica exacta a `main`

Integra el candidato auditado a `main` mediante **fast-forward only**.

Resultado obligatorio:

```text
origin/main = adf70d6eb880c567d6efa0f27b5c79259b8db2a6
```

No debe aparecer merge commit nuevo y los tres blobs deben conservar exactamente los SHA indicados en la sección 2.

Si el fast-forward exacto no es posible:

```text
STOP / MAIN_FAST_FORWARD_NOT_POSSIBLE
```

---

## 5. Reconciliación del Plan Maestro

Trabaja exclusivamente sobre:

```text
branch: docs/plan-maestro-temporal-2026-08-31
file: docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md
```

Partiendo de:

```text
59e7fc935dd5cde9a22bb2743a4116f35ad60a26
```

Realiza el cambio mínimo necesario para registrar:

```text
GROUP3 = IN_PROGRESS
G3_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G3_F02 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G3_F02_INTEGRATION_COMMIT = adf70d6eb880c567d6efa0f27b5c79259b8db2a6
G3_F02_REGISTRY_ROW_COUNT = 548
G3_F02_EVIDENCE_FAMILY_COUNT = 16
NEXT_ELIGIBLE_FICHA = G3-F03
G3_F03 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
```

Preserva expresamente:

```text
STATISTICAL_INFERENCE_EXECUTED = false
HE2_DECIDED = false
HE5_DECIDED = false
EXP12_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
```

No reescribas historia previa ni modifiques otros grupos.

Haz un único commit administrativo del Plan para este cierre y publícalo mediante push normal.

---

## 6. Reconciliación del registro de fichas

Trabaja exclusivamente sobre:

```text
branch: docs/fichas-grupos-3-8
file: docs/fichas/grupos_3_8/04_REGISTRO_ESTADO_FICHAS.md
```

Partiendo de:

```text
af9fd5a39360a37c3c13d397592059592aee6d07
```

### 6.1 Estado tabular

Actualiza únicamente lo necesario para que quede:

```text
G3-F01 = CLOSED / APPROVED
G3-F02 = CLOSED / APPROVED
G3-F03 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
```

Las fichas posteriores permanecen prospectivas/no autorizadas según sus precondiciones.

### 6.2 Registro de cierre G3-F02

Añade un bloque de cierre que conserve como mínimo:

```text
FICHA = G3-F02
ACTIVATION_COMMIT = f7b377b09588cb051745f0daef72a1d87ecbd69c
PROMPT81_COMMIT = 2fe464a244b0d75acfde9555d072db9be0142379
CANDIDATE_COMMIT = adf70d6eb880c567d6efa0f27b5c79259b8db2a6
CANDIDATE_PARENT = 366bf529c29cb999bfd043db33674a510ba184c7
EXTERNAL_AUDIT = PASS
SCIENTIFIC_CORRECTION_REQUIRED = false
SCIENTIFIC_RERUN_REQUIRED = false
REGISTRY_ROW_COUNT = 548
EVIDENCE_FAMILY_COUNT = 16
ELIGIBLE_FAMILY_COUNT = 4
DESCRIPTIVE_ONLY_FAMILY_COUNT = 11
NOT_ESTIMABLE_FAMILY_COUNT = 1
NOT_APPLICABLE_FAMILY_COUNT = 0
INTEGRATION_COMMIT = adf70d6eb880c567d6efa0f27b5c79259b8db2a6
FINAL_G3_F02_STATE = CLOSED / APPROVED / INTEGRATED_TO_MAIN
INFERENTIAL_CALCULATION_PERFORMED = false
HE2_DECIDED = false
HE5_DECIDED = false
G3_F03 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
```

Registra además, como nota no bloqueante y sin tocar los outputs científicos:

```text
AUDIT_DOCUMENTATION_NOTE = Some source_commit_binding rows use two literal main= labels for current and historical snapshots; exact SHA/blob/path provenance remains explicit and auditable. Future registries should use disambiguated labels.
```

No modifiques la ficha prospectiva original para fingir que su encabezado histórico cambió antes de la ejecución; el registro dinámico sigue siendo la fuente de estado operacional.

Haz un único commit administrativo del registro para este cierre y publícalo mediante push normal.

---

## 7. No activar G3-F03

El cierre correcto de Prompt82 deja:

```text
G3_F03 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
```

No crees rama científica de G3-F03.
No ejecutes su ficha.
No calcules inferencia.

La autorización de G3-F03 requiere un prompt posterior de la IA Experimental después de verificar externamente Prompt82.

---

## 8. Respuesta administrativa de Prompt82

Al finalizar, crea en `codex/prompts-temporary`:

```text
codex_prompts_tmp/82_RESPUESTA_INTEGRAR_Y_CERRAR_G3_F02_TRAS_AUDITORIA_EXTERNA.md
```

Commit únicamente ese archivo administrativo en la rama de prompts.

La respuesta debe registrar al menos:

- refs de preflight;
- resultado de la verificación del candidato;
- `main` final;
- blobs de los 3 outputs después de integrar;
- commit final del Plan Maestro;
- commit final del registro de fichas;
- confirmación de que artículo no cambió;
- confirmación de que no hubo modificación/recomputación científica;
- estado final de G3-F02;
- estado de G3-F03.

---

## 9. Reporte terminal obligatorio

Devuelve únicamente:

```text
PROMPT82 = COMPLETED | STOP

PREFLIGHT_MAIN =
PREFLIGHT_PLAN =
PREFLIGHT_FICHAS =
ARTICLE_HEAD_OBSERVED =

G3_F02_CANDIDATE_COMMIT =
G3_F02_COMMITS_AHEAD =
G3_F02_COMMITS_BEHIND =
G3_F02_CHANGED_PATH_COUNT =
G3_F02_CHANGED_PATHS =

MAIN_FINAL =
CSV_BLOB_FINAL =
JSON_BLOB_FINAL =
HASH_LEDGER_BLOB_FINAL =

PLAN_CLOSURE_COMMIT =
FICHAS_CLOSURE_COMMIT =
PROMPT82_RESPONSE_COMMIT =

G3_F02_EXTERNAL_AUDIT = PASS
G3_F02_FINAL_STATE = CLOSED / APPROVED / INTEGRATED_TO_MAIN
SCIENTIFIC_ARTIFACTS_MODIFIED = false
METRICS_RECOMPUTED = false
INFERENTIAL_CALCULATION_PERFORMED = false
P_VALUES_CALCULATED = false
EFFECT_SIZES_CALCULATED = false
HE2_DECIDED = false
HE5_DECIDED = false
EXP12_REOPENED = false

GROUP3 = IN_PROGRESS
G3_F03 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
G3_F03_STARTED = false

BLOCKERS =
WARNINGS =
```
