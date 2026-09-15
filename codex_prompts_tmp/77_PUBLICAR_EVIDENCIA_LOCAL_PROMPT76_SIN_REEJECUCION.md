# PROMPT 77 — PUBLICAR EVIDENCIA LOCAL DE PROMPT76 SIN REEJECUCIÓN

## Rol y objetivo

Actúa como **ejecutor técnico controlado**.

Prompt76 ya fue ejecutado localmente y reportó como ubicación administrativa:

```text
Rama administrativa local: codex/prompts-temporary
Archivo de respuesta: codex_prompts_tmp/76_RESPUESTA_EJECUTAR_G3_F01_FREEZE_ANALITICO_HIPOTESIS_Y_FUENTES.md
```

Sin embargo, la evidencia aún no está disponible en GitHub remoto para auditoría externa. Este Prompt77 tiene un único objetivo administrativo: **publicar exactamente la evidencia local ya producida por Prompt76, sin reejecutar G3-F01, sin regenerar resultados y sin modificar contenido científico**.

No avances a G3-F02.

---

## 1. Estado remoto verificado antes de este prompt

Verifica mediante `git fetch`:

```text
origin/main = a33fc7e10b5bc25a053e982f0ff24ff60eda042f
origin/docs/plan-maestro-temporal-2026-08-31 = f4d20dfe46181cb2740c4e4cd6604b0bff7a48f6
origin/docs/fichas-grupos-3-8 = a42531ad96fc12bea2f2394b0ff8eb49b66a4238
origin/codex/prompts-temporary = 409dd7b7302bce1d41cc69e24b9debe3db05982e
```

Si alguno cambió, no reejecutes nada. Registra el drift y continúa solo si el cambio remoto afecta exclusivamente la rama administrativa `codex/prompts-temporary` por la incorporación de este Prompt77. Cualquier drift científico en `main`, Plan o fichas obliga a:

```text
STOP / SCIENTIFIC_REF_DRIFT_DETECTED
```

---

## 2. Prohibición de reejecución

Está expresamente prohibido:

- volver a ejecutar Prompt76;
- recalcular métricas;
- ejecutar tests inferenciales;
- generar p-values;
- reejecutar retrieval;
- regenerar el contrato analítico si ya existe localmente;
- alterar HE2 o HE5;
- modificar outputs científicos ya producidos por Prompt76;
- abrir G3-F02;
- modificar `main`, el Plan Maestro, las fichas o `article/main-manuscript`.

Este bloque es exclusivamente de **persistencia/publicación de evidencia existente**.

---

## 3. Verificación local obligatoria de la ejecución de Prompt76

Verifica que exista localmente la rama:

```text
codex/group3-f01-analytical-contract-v01
```

Verifica que su commit científico candidato cumpla exactamente:

```text
parent = a33fc7e10b5bc25a053e982f0ff24ff60eda042f
commits_ahead_vs_main = 1
commits_behind_vs_main = 0
changed_path_count = 2
```

Los únicos paths modificados deben ser:

```text
docs/analysis/group3/g3_analytical_contract_v0.1.md
outputs/analysis/group3/g3_analytical_contract_v0.1.json
```

Verifica además que ambos artefactos declaren:

```text
status = CANDIDATE_PENDING_EXTERNAL_AUDIT
ficha = G3-F01
scientific_main_commit = a33fc7e10b5bc25a053e982f0ff24ff60eda042f
canonical_plan_commit = f4d20dfe46181cb2740c4e4cd6604b0bff7a48f6
fichas_snapshot_commit = a42531ad96fc12bea2f2394b0ff8eb49b66a4238
```

No corrijas ni edites estos artefactos en Prompt77. Si cualquiera de estas condiciones falla:

```text
STOP / LOCAL_PROMPT76_EVIDENCE_DOES_NOT_MATCH_CONTRACT
```

---

## 4. Verificación de la respuesta administrativa local

En la rama local:

```text
codex/prompts-temporary
```

verifica que exista:

```text
codex_prompts_tmp/76_RESPUESTA_EJECUTAR_G3_F01_FREEZE_ANALITICO_HIPOTESIS_Y_FUENTES.md
```

La respuesta debe corresponder a la ejecución ya realizada y no debe reconstruirse desde memoria.

Si no existe:

```text
STOP / PROMPT76_RESPONSE_FILE_NOT_FOUND_LOCALLY
```

Si existe pero está sin commit, crea un commit administrativo que añada únicamente ese archivo. Si ya está committeado localmente, no hagas amend ni reescritura; conserva el commit existente.

---

## 5. Publicación remota obligatoria

### 5.1 Rama científica candidata

Publica mediante push normal, sin force:

```text
codex/group3-f01-analytical-contract-v01
```

No cambies su commit científico.

Después verifica en remoto:

```text
origin/codex/group3-f01-analytical-contract-v01 = <MISMO_COMMIT_LOCAL>
```

### 5.2 Rama administrativa

Publica mediante push normal, sin force, la rama:

```text
codex/prompts-temporary
```

Debe quedar disponible remotamente el archivo:

```text
codex_prompts_tmp/76_RESPUESTA_EJECUTAR_G3_F01_FREEZE_ANALITICO_HIPOTESIS_Y_FUENTES.md
```

No modifiques el Prompt76 ya versionado.

---

## 6. Persistencia de Prompt77

Después de publicar la evidencia de Prompt76, crea en `codex/prompts-temporary` únicamente:

```text
codex_prompts_tmp/77_RESPUESTA_PUBLICAR_EVIDENCIA_LOCAL_PROMPT76_SIN_REEJECUCION.md
```

Este archivo debe registrar:

- commit científico publicado;
- parent;
- changed paths;
- commit administrativo que contiene la respuesta de Prompt76;
- HEAD remoto final de `codex/prompts-temporary`;
- confirmación de que no hubo reejecución científica;
- confirmación de que G3-F02 sigue no autorizado.

Commit administrativo separado, sin amend, rebase ni force.

---

## 7. Reporte terminal obligatorio

Devuelve únicamente:

```text
PROMPT77 = COMPLETED | STOP

PROMPT76_REEXECUTED = false
SCIENTIFIC_REEXECUTION_PERFORMED = false

G3_F01_LOCAL_BRANCH =
G3_F01_LOCAL_COMMIT =
G3_F01_REMOTE_BRANCH =
G3_F01_REMOTE_COMMIT =
G3_F01_PARENT =
G3_F01_COMMITS_AHEAD =
G3_F01_COMMITS_BEHIND =
G3_F01_CHANGED_PATH_COUNT =
G3_F01_CHANGED_PATHS =

PROMPT76_RESPONSE_LOCAL_PATH =
PROMPT76_RESPONSE_ADMIN_COMMIT =
PROMPT76_RESPONSE_REMOTE_AVAILABLE = true|false

PROMPT77_RESPONSE_ADMIN_COMMIT =
ADMIN_REMOTE_HEAD_FINAL =

G3_F01_EXTERNAL_AUDIT = PENDING
G3_F02_AUTHORIZED = NO
```

Detente ahí.
