# PROMPT 53 — PUBLICAR CANDIDATO DEL PLAN EXP12 F007 PARA AUDITORÍA EXTERNA

## Rol y objetivo

Actúa como **ejecutor técnico controlado**.

Este bloque corrige exclusivamente una limitación de auditabilidad externa detectada después de Prompt52: el candidato de reconciliación del Plan Maestro fue creado localmente, pero no fue publicado en GitHub, por lo que IA Experimental no puede inspeccionarlo independientemente.

El objetivo único es **publicar sin modificar** el candidato local exacto ya creado en Prompt52.

Este bloque NO modifica ciencia, NO reconstruye el candidato, NO integra el Plan, NO ejecuta EXP12, NO busca ni ingiere `NUEVA_02`, NO ejecuta planeamiento, retrieval, BM25, Top-k o MRR y NO abre Grupo 2B ni Grupo 3.

---

# 1. Estado auditado que gobierna este bloque

La auditoría externa posterior a Prompt52 verificó independientemente:

```text
main = 2b9571eee76ecffcaef1abc7fd4a12051f76f906
F007_V02_INTEGRATION = PASS
rejected F007 v0.1 = NOT_INTEGRATED
plan canonical = 4b0775774cbd8e6287cd45c5c8d8d309b26f2c29
article = 254b1e6df736fa9938ac86a515d65b36f4d361c5
```

Prompt52 reportó el siguiente candidato local de Plan:

```text
branch = codex/plan-maestro-exp12-f007-v01
commit = 00adb8f6fc668609500be913203be50a5d402554
parent = 4b0775774cbd8e6287cd45c5c8d8d309b26f2c29
tree = 56e221039aee8d064173dbffb6b2a9e7a8088a4e
commits_ahead = 1
commits_behind = 0
changed_path_count = 1
changed_path = docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md
publication = LOCAL_ONLY
```

La auditoría externa NO aprueba todavía ese candidato porque el commit `00adb8...` no está disponible en GitHub y la rama remota `origin/codex/plan-maestro-exp12-f007-v01` no existe.

---

# 2. Precondiciones exactas

Ejecuta `git fetch` y verifica:

```text
origin/main = 2b9571eee76ecffcaef1abc7fd4a12051f76f906
origin/docs/plan-maestro-temporal-2026-08-31 = 4b0775774cbd8e6287cd45c5c8d8d309b26f2c29
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
```

Verifica que el candidato LOCAL original de Prompt52 siga existiendo exactamente:

```text
local branch = codex/plan-maestro-exp12-f007-v01
local HEAD = 00adb8f6fc668609500be913203be50a5d402554
parent = 4b0775774cbd8e6287cd45c5c8d8d309b26f2c29
tree = 56e221039aee8d064173dbffb6b2a9e7a8088a4e
commits_ahead_vs_plan = 1
commits_behind_vs_plan = 0
changed_path_count = 1
changed_path = docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md
```

Si la rama local o el commit exacto ya no existen, o si cualquiera de esos valores difiere:

```text
STOP / LOCAL_PLAN_CANDIDATE_NOT_AVAILABLE_EXACTLY
```

**No reconstruyas, no recrees y no regeneres el candidato.**

---

# 3. Publicación exacta permitida

Comprueba primero si existe:

```text
origin/codex/plan-maestro-exp12-f007-v01
```

## Caso A — no existe

Publica exactamente la rama local existente:

```text
codex/plan-maestro-exp12-f007-v01
```

sin crear commit nuevo y sin modificar working tree.

## Caso B — ya existe

Debe apuntar exactamente a:

```text
00adb8f6fc668609500be913203be50a5d402554
```

Si apunta a cualquier otro commit:

```text
STOP / REMOTE_PLAN_CANDIDATE_DRIFT
```

No uses force push.

---

# 4. Verificación posterior obligatoria

Después de la publicación exige:

```text
origin/codex/plan-maestro-exp12-f007-v01 = 00adb8f6fc668609500be913203be50a5d402554
parent = 4b0775774cbd8e6287cd45c5c8d8d309b26f2c29
tree = 56e221039aee8d064173dbffb6b2a9e7a8088a4e
commits_ahead = 1
commits_behind = 0
changed_path_count = 1
changed_path = docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md
```

Verifica además que permanezcan sin cambios:

```text
origin/main = 2b9571eee76ecffcaef1abc7fd4a12051f76f906
origin/docs/plan-maestro-temporal-2026-08-31 = 4b0775774cbd8e6287cd45c5c8d8d309b26f2c29
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
```

---

# 5. Prohibiciones absolutas

Durante Prompt53 NO:

- edites el Plan;
- generes un commit nuevo en el candidato;
- amend, rebase, squash, cherry-pick o force-push;
- integres el candidato a la rama canónica del Plan;
- modifiques `main`;
- modifiques Article;
- modifiques configs EXP12;
- crees autorización EXP12;
- ejecutes EXP12;
- ejecutes planeamiento de 10,000 candidatos por seed;
- ejecutes retrieval/BM25/Top-k/MRR;
- busques, abras, ingieras o asumas `NUEVA_02`;
- rematerialices historia nueva;
- abras Grupo 2B o Grupo 3.

Este bloque es exclusivamente de **publicación para auditabilidad externa**.

---

# 6. Persistencia administrativa

Al finalizar, vuelve a `codex/prompts-temporary` y crea únicamente:

```text
codex_prompts_tmp/53_RESPUESTA_PUBLICAR_CANDIDATO_PLAN_EXP12_F007_PARA_AUDITORIA.md
```

El commit administrativo debe contener solo esa respuesta.

No amend, no rebase, no force.

---

# 7. Reporte obligatorio

Reporta como mínimo:

```text
PROMPT53 = COMPLETED | STOP

main_initial
main_final
plan_initial
plan_final
article_initial
article_final

LOCAL_PLAN_CANDIDATE_PRESENT = true/false
LOCAL_PLAN_CANDIDATE_COMMIT
LOCAL_PLAN_CANDIDATE_PARENT
LOCAL_PLAN_CANDIDATE_TREE
LOCAL_PLAN_CANDIDATE_CHANGED_PATH_COUNT
LOCAL_PLAN_CANDIDATE_CHANGED_PATH

REMOTE_PLAN_CANDIDATE_BEFORE = ABSENT | <sha>
REMOTE_PLAN_CANDIDATE_AFTER
PUBLICATION_MODE = EXACT_PUSH_EXISTING_LOCAL_BRANCH | ALREADY_PRESENT_EXACT
NEW_SCIENTIFIC_COMMIT_CREATED = false
PLAN_CANONICAL_INTEGRATED = false

EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
EXP12_PLANNING_EXECUTED = false
EXP12_RETRIEVAL_EXECUTED = false
NUEVA_02_SEARCHED_OR_INGESTED = false
GROUP2B_STARTED = false
GROUP3_STARTED = false
```

Respuesta terminal máxima:

```text
PROMPT53 = COMPLETED
PLAN_RECONCILIATION_CANDIDATE = PUBLISHED_UNCHANGED / READY_FOR_EXTERNAL_AUDIT
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```
