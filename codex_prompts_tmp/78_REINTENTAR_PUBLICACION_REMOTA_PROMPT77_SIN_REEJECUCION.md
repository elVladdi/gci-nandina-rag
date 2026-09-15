# PROMPT 78 — REINTENTAR PUBLICACIÓN REMOTA DE PROMPT77 SIN REEJECUCIÓN

## Rol y objetivo

Actúa como **ejecutor técnico controlado**.

Prompt76 ya fue ejecutado localmente y Prompt77 también fue ejecutado localmente. La publicación remota no pudo completarse porque GitHub no estaba accesible desde el entorno de Codex.

Este Prompt78 tiene un único objetivo administrativo: **publicar al remoto la evidencia local ya existente de Prompt76 y la respuesta local ya existente de Prompt77, sin reejecutar ciencia, sin regenerar artefactos y sin avanzar a G3-F02**.

No reejecutes Prompt76 ni Prompt77.

---

## 1. Estado remoto verificado antes de este prompt

Al emitirse Prompt78, el remoto verificado era:

```text
origin/codex/prompts-temporary = 2d1e5e543dd2de7d76243d9712883a328eb8f1d7
```

Ese commit contiene Prompt77.

La creación de este Prompt78 avanzará la misma rama administrativa. Por tanto, después de `git fetch origin`, es esperable que:

```text
origin/codex/prompts-temporary = <COMMIT_QUE_CONTIENE_PROMPT78>
```

No trates ese avance administrativo esperado como drift científico.

El estado científico congelado sigue siendo:

```text
origin/main = a33fc7e10b5bc25a053e982f0ff24ff60eda042f
origin/docs/plan-maestro-temporal-2026-08-31 = f4d20dfe46181cb2740c4e4cd6604b0bff7a48f6
origin/docs/fichas-grupos-3-8 = a42531ad96fc12bea2f2394b0ff8eb49b66a4238
```

Si cualquiera de esos tres refs científicos/gobernantes cambió:

```text
STOP / SCIENTIFIC_REF_DRIFT_DETECTED
```

No reejecutes nada.

---

## 2. Evidencia local que debe preservarse exactamente

En el repositorio local ya debe existir:

### 2.1 Rama científica de G3-F01

```text
codex/group3-f01-analytical-contract-v01
```

Debe conservar exactamente la evidencia producida por Prompt76.

Verifica:

```text
parent = a33fc7e10b5bc25a053e982f0ff24ff60eda042f
commits_ahead_vs_main = 1
commits_behind_vs_main = 0
changed_path_count = 2
```

Únicos paths:

```text
docs/analysis/group3/g3_analytical_contract_v0.1.md
outputs/analysis/group3/g3_analytical_contract_v0.1.json
```

No modifiques, regeneres ni reescribas esa rama.

### 2.2 Respuesta administrativa de Prompt76

Debe existir localmente:

```text
codex_prompts_tmp/76_RESPUESTA_EJECUTAR_G3_F01_FREEZE_ANALITICO_HIPOTESIS_Y_FUENTES.md
```

### 2.3 Respuesta administrativa de Prompt77

El usuario reportó localmente:

```text
rama = codex/prompts-temporary
path = codex_prompts_tmp/77_RESPUESTA_PUBLICAR_EVIDENCIA_LOCAL_PROMPT76_SIN_REEJECUCION.md
commit local reportado = a7bb903
```

Resuelve `a7bb903` al SHA completo local y verifica que ese commit contenga exclusivamente la persistencia administrativa esperada de Prompt77. Si el SHA corto no resuelve, localiza el commit por el path exacto anterior; no reconstruyas el contenido desde memoria.

---

## 3. Prohibiciones absolutas

Está prohibido:

- reejecutar Prompt76;
- reejecutar Prompt77;
- volver a ejecutar G3-F01;
- recalcular métricas;
- ejecutar pruebas estadísticas;
- calcular p-values, intervalos o tamaños de efecto;
- reejecutar retrieval;
- regenerar `g3_analytical_contract_v0.1.md`;
- regenerar `g3_analytical_contract_v0.1.json`;
- modificar `main`;
- modificar el Plan Maestro;
- modificar fichas G3-G8;
- modificar `article/main-manuscript`;
- abrir G3-F02;
- usar force-push;
- hacer amend sobre commits científicos.

Este bloque es exclusivamente de reconciliación/publicación administrativa.

---

## 4. Publicación de la rama científica

Después de `git fetch origin`, verifica si existe remotamente:

```text
origin/codex/group3-f01-analytical-contract-v01
```

### Caso A — no existe remotamente

Publica mediante push normal:

```text
codex/group3-f01-analytical-contract-v01
```

Exige:

```text
origin/codex/group3-f01-analytical-contract-v01 = <MISMO_SHA_LOCAL>
```

### Caso B — ya existe remotamente

Compara SHA local y remoto.

- Si son idénticos: no vuelvas a publicar ni modificar.
- Si difieren: `STOP / SCIENTIFIC_BRANCH_REMOTE_MISMATCH`.

Nunca force-push.

---

## 5. Reconciliación segura de la rama administrativa

La creación de Prompt78 en remoto provoca intencionalmente que el remoto administrativo pueda estar por delante del commit local `a7bb903` de Prompt77.

Por tanto, **no intentes sobrescribir el remoto**.

Procede así:

1. Ejecuta `git fetch origin`.
2. Crea una referencia local de seguridad al commit local de Prompt77:

```text
codex/prompt77-local-preserved
```

apuntando al SHA completo que corresponde a `a7bb903`.

3. Actualiza tu rama local `codex/prompts-temporary` para que parta exactamente de:

```text
origin/codex/prompts-temporary
```

que ya debe contener Prompt78.

4. Integra **únicamente el commit administrativo local de Prompt77** sobre ese HEAD remoto.

Para esta operación administrativa concreta se autoriza exclusivamente:

```text
git cherry-pick <SHA_COMPLETO_PROMPT77_LOCAL>
```

Esta autorización excepcional aplica solo al commit administrativo de Prompt77 y solo porque Prompt78 fue creado remotamente después de dicho commit local.

No cherry-pick de ningún commit científico.

5. Verifica que el cherry-pick añada únicamente:

```text
codex_prompts_tmp/77_RESPUESTA_PUBLICAR_EVIDENCIA_LOCAL_PROMPT76_SIN_REEJECUCION.md
```

Si modifica cualquier otro path:

```text
STOP / ADMIN_RECONCILIATION_SCOPE_VIOLATION
```

6. Publica `codex/prompts-temporary` mediante push normal, sin force.

---

## 6. Persistencia de Prompt78

Después de que ambas publicaciones remotas queden verificadas, crea en `codex/prompts-temporary`:

```text
codex_prompts_tmp/78_RESPUESTA_REINTENTAR_PUBLICACION_REMOTA_PROMPT77_SIN_REEJECUCION.md
```

El archivo debe registrar como mínimo:

- SHA remoto final de la rama científica G3-F01;
- SHA remoto final de `codex/prompts-temporary`;
- SHA local original de Prompt77 reportado como `a7bb903` y su SHA completo resuelto;
- SHA nuevo resultante del cherry-pick administrativo, si cambió;
- confirmación de disponibilidad remota de las respuestas 76 y 77;
- confirmación de disponibilidad remota de los dos artefactos de G3-F01;
- confirmación de ausencia de reejecución científica;
- confirmación de que G3-F02 sigue no autorizado.

Commit administrativo separado y push normal.

---

## 7. Criterio de éxito

Solo puede declarar `COMPLETED` si se verifica remotamente:

```text
PROMPT76_RESPONSE_REMOTE_AVAILABLE = true
PROMPT77_RESPONSE_REMOTE_AVAILABLE = true
G3_F01_MD_REMOTE_AVAILABLE = true
G3_F01_JSON_REMOTE_AVAILABLE = true
G3_F01_REMOTE_SHA_EQUALS_LOCAL = true
FORCE_PUSH_USED = false
SCIENTIFIC_REEXECUTION_PERFORMED = false
G3_F01_REGENERATED = false
G3_F02_STARTED = false
```

Si GitHub vuelve a estar inaccesible:

```text
STOP / REMOTE_UNAVAILABLE
```

No crees nuevos commits científicos ni repitas la ejecución.

---

## 8. Reporte terminal obligatorio

Devuelve únicamente:

```text
PROMPT78 = COMPLETED | STOP

REMOTE_ACCESS = AVAILABLE | UNAVAILABLE

G3_F01_LOCAL_COMMIT =
G3_F01_REMOTE_COMMIT =
G3_F01_REMOTE_MATCH = true|false

PROMPT77_LOCAL_ORIGINAL_SHORT_SHA = a7bb903
PROMPT77_LOCAL_ORIGINAL_FULL_SHA =
PROMPT77_RECONCILED_ADMIN_COMMIT =
ADMIN_REMOTE_HEAD_FINAL =

PROMPT76_RESPONSE_REMOTE_AVAILABLE = true|false
PROMPT77_RESPONSE_REMOTE_AVAILABLE = true|false
PROMPT78_RESPONSE_REMOTE_AVAILABLE = true|false
G3_F01_MD_REMOTE_AVAILABLE = true|false
G3_F01_JSON_REMOTE_AVAILABLE = true|false

PROMPT76_REEXECUTED = false
PROMPT77_REEXECUTED = false
SCIENTIFIC_REEXECUTION_PERFORMED = false
G3_F01_REGENERATED = false
FORCE_PUSH_USED = false
G3_F02_STARTED = false

G3_F01_EXTERNAL_AUDIT = PENDING
G3_F02_AUTHORIZED = NO

BLOCKERS =
```

Detente ahí.
