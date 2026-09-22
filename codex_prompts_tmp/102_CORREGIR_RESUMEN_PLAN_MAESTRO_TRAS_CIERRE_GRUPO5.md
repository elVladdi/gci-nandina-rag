# PROMPT102 — CORREGIR RESUMEN DEL PLAN MAESTRO TRAS CIERRE DE GRUPO 5

## 0. Naturaleza y alcance

Ejecuta **exclusivamente** una corrección administrativa localizada del Plan Maestro después de Prompt101.

La auditoría externa independiente de Prompt101 determinó:

```text
PROMPT101_EXTERNAL_AUDIT = PASS_WITH_CORRECTION_REQUIRED
PROMPT101_SCIENTIFIC_AND_GIT_CLOSURE = PASS
PLAN_MASTER_SUMMARY_RECONCILIATION = FAIL_LOCALIZED
SCIENTIFIC_CORRECTION_REQUIRED = false
NEW_INFERENCE_REQUIRED = false
METRICS_RECOMPUTATION_REQUIRED = false
```

El defecto está restringido a la tabla-resumen inicial de `## 2. Estado del plan de auditoría` del Plan Maestro: el bloque histórico agregado al final del documento registra correctamente el cierre de Grupo 5, pero la fila-resumen superior todavía conserva el estado anterior de Grupo 5 y Grupo 6.

Esta ejecución autoriza únicamente:

1. verificar que `main`, fichas y el bloque de cierre final del Plan continúan reflejando correctamente el cierre de Grupo 5;
2. corregir la tabla-resumen inicial del Plan Maestro para que sea coherente con ese cierre;
3. actualizar la fecha de actualización del Plan a `2026-09-21`;
4. persistir un reporte terminal de Prompt102.

No autoriza:

- modificar `main`;
- modificar el registro de fichas;
- modificar artefactos de G5-F01, G5-F02 o G5-F03;
- recalcular métricas, inferencia, bootstrap, intervalos o p-values;
- redecidir HE2 o HE5;
- modificar artículo o tesis;
- activar o ejecutar G6-F01;
- crear figuras;
- iniciar Grupo 6;
- reabrir EXP12;
- realizar búsqueda bibliográfica.

---

## 1. Workspace local canónico obligatorio

Trabaja exclusivamente dentro del repositorio local canónico:

```text
C:/Users/Vladimir/OneDrive/Documentos/Maestría UNMSM/LLM_RGA_NANDINA
```

Antes de cualquier operación registra:

```text
git rev-parse --show-toplevel
git remote get-url origin
git branch --show-current
git rev-parse HEAD
git status --porcelain
git worktree list --porcelain
```

Debe cumplirse:

```text
WORKSPACE_ROOT_MATCH_EXPECTED = true
WORKSPACE_ORIGIN_REPOSITORY = elVladdi/gci-nandina-rag
USER_CANONICAL_LOCAL_PATH_FROZEN = true
```

No uses otro clon, no crees worktrees nuevos y no limpies/resetées/stashees cambios locales preexistentes del usuario.

---

## 2. Refs congelados y preflight

Ejecuta `git fetch origin` y verifica exactamente:

```text
origin/main = ca065618d5df0019f76ef5a971e858d91c263e1f
origin/docs/fichas-grupos-3-8 = b17202cb1360f6ad01aaef42d1fd3fb86b201cbc
origin/docs/plan-maestro-temporal-2026-08-31 = 120aacfaba7d019e6156efef2891acaa2424cb90
PROMPT101_SOURCE = 6fbefce9be1569a34d2f75cc185a6b34cf2c76af
PROMPT101_RESPONSE = 2fe97378b100f27936a2c556609b36823d0508aa
G5_F03_INTEGRATION_COMMIT = ca065618d5df0019f76ef5a971e858d91c263e1f
```

La rama editorial es solo observacional. Registra su HEAD al inicio y al final; su avance concurrente no es bloqueo si no la modificas.

Si `main`, fichas o Plan presentan drift experimental no explicado:

```text
STOP / PROMPT102_REF_DRIFT
```

---

## 3. Hecho auditado que motiva la corrección

En el Plan Maestro `120aacfaba7d019e6156efef2891acaa2424cb90`, el bloque final de cierre ya declara correctamente:

```text
G5_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G5_F02 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G5_F03 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
GROUP5 = CLOSED / APPROVED
NEXT_ELIGIBLE_FICHA = G6-F01
G6_F01 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
G6_F01_AUTHORIZED = false
G6_F01_STARTED = false
GROUP6 = NOT_STARTED
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
```

Sin embargo, la tabla inicial `## 2. Estado del plan de auditoría` todavía contiene una fila obsoleta equivalente a:

```text
5. Presentación de resultados = IN_PROGRESS
G5-F02 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
6. Figuras y visualizaciones = Pendiente
```

Ese desacople hace que el Plan no sea inequívoco, aunque el cierre científico y Git de Prompt101 sea correcto.

---

## 4. Corrección exacta del Plan Maestro

Trabaja exclusivamente sobre:

```text
branch = docs/plan-maestro-temporal-2026-08-31
base = 120aacfaba7d019e6156efef2891acaa2424cb90
file = docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md
```

Modifica únicamente ese archivo.

### 4.1 Fecha

Cambia:

```text
Fecha de actualización: 2026-09-20
```

por:

```text
Fecha de actualización: 2026-09-21
```

### 4.2 Fila-resumen de Grupo 5

La fila `5. Presentación de resultados` debe quedar coherente con el cierre ya registrado. Debe expresar, como mínimo:

```text
CLOSED / APPROVED
G5-F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G5-F02 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G5-F03 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G5-F03_INTEGRATION_COMMIT = ca065618d5df0019f76ef5a971e858d91c263e1f
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
```

No introduzcas nuevas afirmaciones científicas ni resumas con mayor fuerza que los registros congelados.

### 4.3 Fila-resumen de Grupo 6

La fila `6. Figuras y visualizaciones` debe reflejar explícitamente:

```text
NOT_STARTED
G6-F01 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
G6_F01_AUTHORIZED = false
G6_F01_STARTED = false
```

No la marques como `ACTIVE`, `AUTHORIZED`, `IN_PROGRESS` ni equivalente.

### 4.4 No tocar otros contenidos

No edites las filas de Grupos 1–4, 7–8 salvo que sea estrictamente necesario para preservar el formato Markdown de la tabla.

No modifiques el bloque de cierre final de Grupo 5 salvo corrección tipográfica estrictamente necesaria; su contenido científico y administrativo ya fue auditado como correcto.

---

## 5. Verificaciones obligatorias

Después del cambio, demuestra:

```text
PLAN_SUMMARY_GROUP5_MATCHES_CLOSURE = true
PLAN_SUMMARY_GROUP6_MATCHES_CLOSURE = true
PLAN_INTERNAL_GROUP5_STATE_CONTRADICTION_COUNT = 0
PLAN_INTERNAL_G6_F01_AUTHORIZATION_CONTRADICTION_COUNT = 0
```

Busca en todo el Plan referencias operacionales actuales que todavía afirmen, para el estado presente:

```text
GROUP5 = IN_PROGRESS
G5-F02 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
G5-F03 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
G6-F01 = ACTIVE
G6-F01 = AUTHORIZED
G6-F01 = EXECUTION_PENDING
```

Las referencias históricas dentro de bloques fechados o registros de ejecución anteriores pueden permanecer si están claramente contextualizadas como estado histórico. No las reescribas retrospectivamente.

La tabla-resumen inicial y el bloque de cierre vigente deben ser mutuamente consistentes.

---

## 6. Commit y publicación

Haz un único commit documental sobre `docs/plan-maestro-temporal-2026-08-31` que modifique exclusivamente:

```text
docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md
```

Mensaje recomendado:

```text
docs: reconcile Group 5 summary state in master plan
```

Push normal.

No modifiques `main` ni `docs/fichas-grupos-3-8`.

---

## 7. Estado terminal permitido

Después de la corrección debe permanecer:

```text
origin/main = ca065618d5df0019f76ef5a971e858d91c263e1f
origin/docs/fichas-grupos-3-8 = b17202cb1360f6ad01aaef42d1fd3fb86b201cbc
GROUP5 = CLOSED / APPROVED
G5_F03 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G6_F01 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
G6_F01_AUTHORIZED = false
G6_F01_STARTED = false
GROUP6 = NOT_STARTED
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
```

Esta ejecución **no autoriza G6-F01**. Su eventual activación requerirá un prompt prospectivo posterior y auditoría externa de esta corrección.

---

## 8. Reporte terminal obligatorio

Crea y publica en `codex/prompts-temporary`:

```text
codex_prompts_tmp/102_RESPUESTA_CORREGIR_RESUMEN_PLAN_MAESTRO_TRAS_CIERRE_GRUPO5.md
```

El reporte debe incluir como mínimo:

```text
PROMPT102 = COMPLETED
WORKSPACE_ROOT_OBSERVED = ...
WORKSPACE_ROOT_MATCH_EXPECTED = true
WORKSPACE_INITIAL_DIRTY_COUNT = ...

PREFLIGHT_MAIN = ca065618d5df0019f76ef5a971e858d91c263e1f
PREFLIGHT_FICHAS = b17202cb1360f6ad01aaef42d1fd3fb86b201cbc
PREFLIGHT_PLAN = 120aacfaba7d019e6156efef2891acaa2424cb90
PROMPT102_SOURCE = <commit de este prompt>

POSTCORRECTION_PLAN_COMMIT = ...
PLAN_CHANGED_PATH_COUNT = 1
PLAN_CHANGED_PATH = docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md
PLAN_SUMMARY_GROUP5_MATCHES_CLOSURE = true
PLAN_SUMMARY_GROUP6_MATCHES_CLOSURE = true
PLAN_INTERNAL_GROUP5_STATE_CONTRADICTION_COUNT = 0
PLAN_INTERNAL_G6_F01_AUTHORIZATION_CONTRADICTION_COUNT = 0

FINAL_ORIGIN_MAIN = ca065618d5df0019f76ef5a971e858d91c263e1f
FINAL_ORIGIN_FICHAS = b17202cb1360f6ad01aaef42d1fd3fb86b201cbc
FINAL_ORIGIN_PLAN = <nuevo commit>

GROUP5 = CLOSED / APPROVED
G6_F01 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
G6_F01_AUTHORIZED = false
G6_F01_STARTED = false
GROUP6 = NOT_STARTED
HE2 = SUPPORTED
HE5 = INCONCLUSIVE

MAIN_MODIFIED = false
FICHAS_MODIFIED = false
ARTICLE_MODIFIED = false
THESIS_MODIFIED = false
NEW_SCIENTIFIC_STATEMENT_COUNT = 0
NEW_INFERENCE_PERFORMED = false
METRICS_RECOMPUTED = false
EXP12_REOPENED = false

BLOCKERS = ...
WARNINGS = ...
```

El commit que persista esta respuesta en `codex/prompts-temporary` debe añadir únicamente el archivo de respuesta.
