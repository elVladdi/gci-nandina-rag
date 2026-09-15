# PROMPT 73 — INTEGRAR CIERRE DE GRUPO 2B Y MICROCLOSE DEL PLAN POST-INTEGRACIÓN

## Rol y objetivo

Actúa como **ejecutor técnico controlado**.

Este bloque realiza exclusivamente:

1. integrar mediante fast-forward exacto el registro de cierre de Grupo 2B ya auditado externamente;
2. NO integrar el candidato del Plan v0.1 de Prompt72, porque al integrar el registro de cierre `main` avanzará y el SHA de `main` consignado en ese candidato quedará desactualizado;
3. crear un candidato v0.2 del Plan Maestro que preserve íntegramente el cierre sustantivo de Grupo 2B y corrija únicamente la identidad canónica posterior a la integración;
4. publicar el candidato corregido para auditoría externa.

Este bloque **NO ejecuta** experimentos, pipelines, tests científicos, retrieval, BM25, Top-k, MRR, planning, candidate generation, inferencia ni regeneración de datos/resultados. No reabre EXP12 y no inicia Grupo 3.

---

## 1. Dictamen externo que gobierna este bloque

La auditoría externa de IA Experimental sobre Prompt72 concluye:

```text
PROMPT72_EXTERNAL_AUDIT = PASS_WITH_PLAN_MICROCLOSE_REQUIRED

READINESS_V02_INTEGRATED = VERIFIED
GROUP2B_CLOSURE_V01 = APPROVED_FOR_INTEGRATION

PLAN_GROUP2B_CLOSURE_V01 = SUBSTANTIVELY_APPROVED / DO_NOT_INTEGRATE_AS_IS
G2B-CLOSE-F001 = POST_CLOSURE_MAIN_SHA_STALENESS / DOCUMENTARY

GROUP2B_DISPOSITION = CLOSED / APPROVED_WITH_NONBLOCKING_LIMITATIONS
GROUP2B_BLOCKING_GAP_COUNT = 0
GROUP2B_NONBLOCKING_LIMITATION_COUNT = 11
GROUP2B_HISTORICAL_ONLY_COUNT = 5
GROUP3 = NOT_STARTED
```

Fundamento del microclose:

- `codex/plan-maestro-group2b-closure-v01` registra correctamente el estado sustantivo, pero consigna `main = origin/main = fbd321d817d22fef78417064e0d5bc8df37165ca`.
- El registro de cierre aprobado está en `a33fc7e10b5bc25a053e982f0ff24ff60eda042f`, cuyo parent es `fbd321d817d22fef78417064e0d5bc8df37165ca`.
- Una vez integrado ese registro, el `main` canónico será `a33fc7e10b5bc25a053e982f0ff24ff60eda042f`.
- Por tanto, integrar después el Plan v0.1 sin corregir esa referencia produciría una reconciliación canónica inmediatamente desactualizada.

Este hallazgo es exclusivamente documental y no cuestiona el readiness v0.2, los conteos, las limitaciones ni la disposición de cierre.

---

## 2. Precondiciones Git exactas

Ejecuta `git fetch` y exige exactamente:

```text
origin/main = fbd321d817d22fef78417064e0d5bc8df37165ca
origin/codex/group2b-reproducibility-closure-v01 = a33fc7e10b5bc25a053e982f0ff24ff60eda042f
origin/docs/plan-maestro-temporal-2026-08-31 = 0c77e86359bcd17ddd446429f21b62174c426f37
origin/codex/plan-maestro-group2b-closure-v01 = fb1c59d2ff2f92098ad9b7fcfb16a8d7232ed28a
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
```

Para el cierre Group2B exige:

```text
parent = fbd321d817d22fef78417064e0d5bc8df37165ca
commits_ahead = 1
commits_behind = 0
changed_path_count = 1
changed_path = outputs/audits/group2b_reproducibility_closure_v0.1.json
```

Para el Plan v0.1 exige:

```text
parent = 0c77e86359bcd17ddd446429f21b62174c426f37
commits_ahead = 1
commits_behind = 0
changed_path_count = 1
changed_path = docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md
```

Si existe drift:

```text
STOP / PRECONDITION_REF_DRIFT
```

---

## 3. Fase A — integrar exactamente el registro de cierre Group2B

Mueve exclusivamente `main` mediante fast-forward exacto:

```text
fbd321d817d22fef78417064e0d5bc8df37165ca
→
a33fc7e10b5bc25a053e982f0ff24ff60eda042f
```

Prohibidos merge commit, squash, cherry-pick, rebase, amend o reconstrucción manual.

Después exige:

```text
origin/main = a33fc7e10b5bc25a053e982f0ff24ff60eda042f
origin/docs/plan-maestro-temporal-2026-08-31 = 0c77e86359bcd17ddd446429f21b62174c426f37
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
```

Verifica que el commit integrado contiene exclusivamente:

```text
outputs/audits/group2b_reproducibility_closure_v0.1.json
```

No modifiques ese JSON.

---

## 4. Fase B — microclose del Plan Maestro

**NO integres** `fb1c59d2ff2f92098ad9b7fcfb16a8d7232ed28a` en la rama canónica del Plan.

Desde exactamente:

```text
fb1c59d2ff2f92098ad9b7fcfb16a8d7232ed28a
```

crea la rama nueva:

```text
codex/plan-maestro-group2b-closure-v02
```

Haz un solo commit adicional modificando exclusivamente:

```text
docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md
```

### 4.1 Cambio permitido y obligatorio

Conserva íntegramente el contenido sustantivo del cierre de Grupo 2B del candidato v0.1 y corrige únicamente las referencias de estado canónico afectadas por la integración del cierre.

Donde el Plan describa el `main` **vigente/post-cierre**, debe quedar:

```text
main = origin/main = a33fc7e10b5bc25a053e982f0ff24ff60eda042f
```

Debe quedar distinguido correctamente:

```text
GROUP2B_READINESS_V02_COMMIT = fbd321d817d22fef78417064e0d5bc8df37165ca
GROUP2B_CLOSURE_RECORD = INTEGRATED
GROUP2B_CLOSURE_INTEGRATION_COMMIT = a33fc7e10b5bc25a053e982f0ff24ff60eda042f
```

Puedes expresarlo con redacción equivalente si el Plan no usa exactamente esas claves, pero no confundas el commit de readiness con el `main` vigente tras integrar el cierre.

### 4.2 Estado que debe permanecer sin cambios

Preserva exactamente el sentido de:

```text
GROUP2B = CLOSED / APPROVED_WITH_NONBLOCKING_LIMITATIONS
GROUP2B_BLOCKING_GAP_COUNT = 0
GROUP2B_NONBLOCKING_LIMITATION_COUNT = 11
GROUP2B_HISTORICAL_ONLY_COUNT = 5
ENVIRONMENT_REPRODUCIBILITY = COMPLETE_WITH_DECLARED_LIMITATION
CLEAN_CHECKOUT_REPRODUCIBILITY = COMPLETE_WITH_DECLARED_LIMITATION
GROUP2B_SCIENTIFIC_REEXECUTION_REQUIRED = false
GROUP2B_RESULTS_RECOMPUTATION_REQUIRED = false
GROUP3 = NOT_STARTED
NEXT_ELIGIBLE_BLOCK = GROUP3_METRICS_AND_INFERENCE
```

Preserva también:

- las limitaciones `DECLARED_NOT_RECOVERABLE`;
- los assets `HASH_BOUND_LOCAL_ONLY`;
- la advertencia de que el cierre no equivale a reproducibilidad perfecta;
- toda la disposición final de EXP12;
- la fecha `2026-09-15`;
- la cronología previa.

No cambies conteos, clasificaciones, resultados, conclusiones ni el estado de ningún experimento.

### 4.3 Relación Git esperada

El candidato v0.2 será descendiente lineal del Plan v0.1:

```text
0c77e86359bcd17ddd446429f21b62174c426f37
→ fb1c59d2ff2f92098ad9b7fcfb16a8d7232ed28a
→ <PLAN_V02_COMMIT>
```

Respecto de la rama canónica del Plan debe quedar:

```text
commits_ahead = 2
commits_behind = 0
```

No muevas todavía:

```text
docs/plan-maestro-temporal-2026-08-31
```

---

## 5. Verificaciones finales

Exige:

```text
origin/main = a33fc7e10b5bc25a053e982f0ff24ff60eda042f
origin/docs/plan-maestro-temporal-2026-08-31 = 0c77e86359bcd17ddd446429f21b62174c426f37
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
```

Para `codex/plan-maestro-group2b-closure-v02` exige:

```text
base canonical plan = 0c77e86359bcd17ddd446429f21b62174c426f37
commits_ahead = 2
commits_behind = 0
latest_parent = fb1c59d2ff2f92098ad9b7fcfb16a8d7232ed28a
changed paths across the two commits = docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md only
latest commit changes that same Plan path only
```

Confirma:

```text
GROUP2B_CLOSURE_RECORD = INTEGRATED
GROUP2B = CLOSED / APPROVED_WITH_NONBLOCKING_LIMITATIONS
GROUP3_STARTED = false
NEXT_ELIGIBLE_BLOCK = GROUP3_METRICS_AND_INFERENCE
SCIENTIFIC_EXECUTION_PERFORMED = false
RESULTS_RECOMPUTED = false
EXP12_REOPENED = false
```

---

## 6. Prohibiciones absolutas

Durante Prompt73 NO:

- ejecutes experimentos, pipelines ni tests científicos;
- ejecutes retrieval/BM25/Top-k/MRR;
- regeneres resultados, datasets, manifests, logs o case-level;
- reconstruyas assets local-only;
- cambies los conteos o clasificaciones del readiness/cierre;
- recuperes retrospectivamente elementos `DECLARED_NOT_RECOVERABLE`;
- reabras EXP12;
- modifiques Article;
- integres el Plan v0.1;
- integres todavía el Plan v0.2;
- inicies Grupo 3.

---

## 7. Persistencia administrativa

Al finalizar vuelve a `codex/prompts-temporary` y crea únicamente:

```text
codex_prompts_tmp/73_RESPUESTA_INTEGRAR_CIERRE_GROUP2B_Y_MICROCLOSE_PLAN_POST_INTEGRACION.md
```

El commit administrativo debe contener solo esa respuesta. No amend, no rebase, no force.

---

## 8. Reporte obligatorio

Reporta como mínimo:

```text
PROMPT73 = COMPLETED | STOP

main_initial
main_final
plan_canonical_final
article_final
GROUP2B_CLOSURE_INTEGRATED

PLAN_V01_COMMIT
PLAN_V01_INTEGRATED
PLAN_V02_BRANCH
PLAN_V02_COMMIT
PLAN_V02_PARENT
PLAN_V02_COMMITS_AHEAD_CANONICAL
PLAN_V02_COMMITS_BEHIND_CANONICAL
PLAN_V02_CHANGED_PATH_COUNT
PLAN_V02_PUBLISHED

G2B_CLOSE_F001
GROUP2B_DISPOSITION
BLOCKING_GAP_COUNT
NONBLOCKING_LIMITATION_COUNT
HISTORICAL_ONLY_COUNT
ENVIRONMENT_REPRODUCIBILITY
CLEAN_CHECKOUT_REPRODUCIBILITY
NEXT_ELIGIBLE_BLOCK

SCIENTIFIC_EXECUTION_PERFORMED = false
RESULTS_RECOMPUTED = false
EXP12_REOPENED = false
GROUP3_STARTED = false
```

Respuesta terminal máxima:

```text
PROMPT73 = COMPLETED
GROUP2B_CLOSURE_RECORD = INTEGRATED
G2B-CLOSE-F001 = RESOLVED
PLAN_GROUP2B_CLOSURE_V02 = CANDIDATE_PENDING_EXTERNAL_AUDIT
GROUP2B = CLOSED / APPROVED_WITH_NONBLOCKING_LIMITATIONS
NEXT_ELIGIBLE_BLOCK = GROUP3_METRICS_AND_INFERENCE
GROUP3_STARTED = false
```
