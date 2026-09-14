# PROMPT 69 — INTEGRAR PLAN FORENSE Y CERRAR DISPOSICIÓN METODOLÓGICA EXP12

## Rol y objetivo

Actúa como **ejecutor técnico controlado**.

Este bloque realiza exclusivamente, en este orden:

1. integrar mediante fast-forward exacto el candidato del Plan Maestro generado por Prompt68 y ya auditado externamente;
2. materializar en un nuevo candidato del Plan Maestro la **disposición metodológica final del EXP12 original congelado**;
3. cerrar el EXP12 original **sin retrieval**, porque una precondición obligatoria de su diseño congelado falló en el primer seed predeclarado y no puede corregirse mediante sustitución de seed, relajación de thresholds o rerun post hoc;
4. dejar como siguiente bloque elegible el cierre de reproducibilidad y trazabilidad del **Grupo 2B**.

Este bloque **NO ejecuta** diagnóstico, candidate generation, planning, otros seeds, thresholds alternativos, D-HIGH/D-MID/D-LOW, retrieval/BM25/Top-k/MRR, ni modifica código/config/datos/Article. Tampoco abre un EXP12 rediseñado.

---

## 1. Dictamen externo que gobierna este bloque

La auditoría externa de IA Experimental sobre Prompt68 concluye:

```text
PROMPT68_EXTERNAL_AUDIT = PASS / APPROVED

FORENSIC_EVIDENCE = INTEGRATED / VERIFIED
PLAN_FORENSIC_RECONCILIATION_V01 = APPROVED_FOR_INTEGRATION

EXP12_FORENSIC_ATTEMPT_001 = COMPLETED_ONE_SHOT / AUDITED / INTEGRATED
EXP12_FORENSIC_FINAL_UNIQUE_FEASIBLE = 0
EXP12_FORENSIC_MINIMUM_REQUIRED = 30
EXP12_FORENSIC_HISTORICAL_FAILURE_REPRODUCED = true

EXP12_FORENSIC_TVD_CHARACTERIZATION = UNIVERSAL_BINDING_CONSTRAINT_AMONG_VOLUME_PASS_FOR_OBSERVED_SEARCH
EXP12_FORENSIC_COVERAGE_CHARACTERIZATION = NEAR_UNIVERSAL_BINDING_CONSTRAINT_AMONG_VOLUME_PASS_FOR_OBSERVED_SEARCH
EXP12_FORENSIC_GLOBAL_INFEASIBILITY_PROVEN = false
EXP12_FORENSIC_OTHER_SEEDS_CHARACTERIZED = false
```

Candidato del Plan aprobado:

```text
branch = codex/plan-maestro-exp12-forensic-result-v01
commit = cf8e9386e2c6ffa4bf9e1f2c401e85b8574a3880
parent = 5a3df4c2665ac5d1b57f7ef19b800d39758e6920
commits_ahead = 1
commits_behind = 0
changed_path_count = 1
changed_path = docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md
```

Estado científico integrado:

```text
origin/main = 5787503329afd5ddd5e94d04cdbbdeb000260cda
origin/docs/plan-maestro-temporal-2026-08-31 = 5a3df4c2665ac5d1b57f7ef19b800d39758e6920
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
```

---

## 2. Decisión metodológica final de IA Experimental

La decisión que gobierna este bloque es:

```text
EXP12_ORIGINAL_FROZEN_DESIGN_DISPOSITION =
CLOSED_WITHOUT_RETRIEVAL / PLANNING_PRECONDITION_FAILED_UNDER_FROZEN_SEARCH

EXP12_REDESIGN_IN_CURRENT_EXPERIMENT = NOT_AUTHORIZED
EXP12_POST_HOC_PARAMETER_RELAXATION = PROHIBITED
EXP12_SEED_REPLACEMENT_OR_DROPPING = PROHIBITED
EXP12_RETRY = PROHIBITED
```

### Fundamento exacto

El contrato congelado de EXP12 exige:

```text
seeds = 20262001..20262010
candidate_count_per_seed = 10000
minimum_unique_feasible_per_seed = 30
conditions_per_seed = D-HIGH / D-MID / D-LOW
```

El seed predeclarado obligatorio `20262001` produjo, bajo las reglas congeladas v0.5:

```text
final_unique_feasible_count = 0
minimum_required_unique_feasible = 30
```

Por tanto, el seed `20262001` **no puede producir las tres condiciones prescritas** y el diseño original de diez seeds no puede ejecutarse como fue congelado.

No es necesario probar otros seeds para cerrar el diseño original: el seed `20262001` forma parte de la agenda predeclarada y es obligatorio. Eliminarlo, sustituirlo o continuar hasta encontrar diez seeds viables después de observar el fallo cambiaría retrospectivamente el protocolo.

### Alcance de la conclusión

Debe quedar explícito que este cierre:

- **sí** demuestra que el EXP12 original no pudo superar su gate de planning bajo la búsqueda congelada para un seed obligatorio;
- **sí** implica que no existen condiciones oficiales D-HIGH/D-MID/D-LOW para EXP12;
- **sí** implica que retrieval EXP12 no se ejecutó y el efecto de diversidad histórica previsto por EXP12 **no es estimable con este experimento**;
- **no** demuestra inviabilidad matemática global de todos los subconjuntos DAM posibles;
- **no** caracteriza otros seeds;
- **no** demuestra que TVD=0.05 o cobertura=1.0 sean thresholds incorrectos;
- **no** autoriza relajarlos;
- **no** convierte el resultado forense en resultado de retrieval;
- **no** autoriza un EXP12 rediseñado dentro del experimento original.

Si en el futuro se quisiera estudiar nuevamente diversidad histórica, deberá ser un **nuevo protocolo prospectivo, separado y explícitamente identificado**, nunca una continuación/retry del EXP12 original.

---

## 3. Precondiciones Git exactas

Ejecuta `git fetch` y exige exactamente:

```text
origin/main = 5787503329afd5ddd5e94d04cdbbdeb000260cda
origin/docs/plan-maestro-temporal-2026-08-31 = 5a3df4c2665ac5d1b57f7ef19b800d39758e6920
origin/codex/plan-maestro-exp12-forensic-result-v01 = cf8e9386e2c6ffa4bf9e1f2c401e85b8574a3880
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
```

Para el candidato de Prompt68 exige:

```text
parent = 5a3df4c2665ac5d1b57f7ef19b800d39758e6920
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

## 4. Fase A — integrar exactamente el Plan forense de Prompt68

Mueve exclusivamente:

```text
docs/plan-maestro-temporal-2026-08-31
```

mediante fast-forward exacto:

```text
5a3df4c2665ac5d1b57f7ef19b800d39758e6920
→
cf8e9386e2c6ffa4bf9e1f2c401e85b8574a3880
```

Prohibidos merge commit, squash, cherry-pick, rebase, amend o reconstrucción manual.

Después exige:

```text
origin/docs/plan-maestro-temporal-2026-08-31 = cf8e9386e2c6ffa4bf9e1f2c401e85b8574a3880
origin/main = 5787503329afd5ddd5e94d04cdbbdeb000260cda
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
```

---

## 5. Fase B — candidato de cierre metodológico del Plan Maestro

Crea desde exactamente:

```text
cf8e9386e2c6ffa4bf9e1f2c401e85b8574a3880
```

la rama nueva:

```text
codex/plan-maestro-exp12-methodological-disposition-v01
```

Modifica exclusivamente:

```text
docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md
```

Un solo commit.

### 5.1 Estado final obligatorio de EXP12

El Plan debe registrar de forma coherente, como mínimo:

```text
EXP12_ORIGINAL_FROZEN_DESIGN = CLOSED
EXP12_DISPOSITION = CLOSED_WITHOUT_RETRIEVAL / PLANNING_PRECONDITION_FAILED_UNDER_FROZEN_SEARCH
EXP12_PLANNING_ATTEMPT_001 = FAILED_ONE_SHOT / AUDITED / INTEGRATED
EXP12_PLANNING_RETRY = PROHIBITED_UNDER_AUTH_001
EXP12_FORENSIC_ATTEMPT_001 = COMPLETED_ONE_SHOT / AUDITED / INTEGRATED
EXP12_FORENSIC_FINAL_UNIQUE_FEASIBLE = 0
EXP12_FORENSIC_MINIMUM_REQUIRED = 30
EXP12_PLANNING_OFFICIAL_CONDITIONS = NOT_SELECTED
EXP12_DIVERSITY_EFFECT_ESTIMABLE = false
EXP12_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
EXP12_REDESIGN_IN_CURRENT_EXPERIMENT = NOT_AUTHORIZED
EXP12_POST_HOC_PARAMETER_RELAXATION = PROHIBITED
EXP12_SEED_REPLACEMENT_OR_DROPPING = PROHIBITED
EXP12_GLOBAL_MATHEMATICAL_INFEASIBILITY_PROVEN = false
EXP12_OTHER_SEEDS_CHARACTERIZED = false
```

No uses simplemente `EXP12=NOT_AUTHORIZED / NOT_EXECUTED` como estado final aislado. Debe distinguirse entre:

- el **diseño original**, que queda cerrado por fallo de precondición de planning;
- el **retrieval EXP12**, que nunca se ejecutó;
- el **efecto de diversidad**, que no puede estimarse mediante EXP12.

### 5.2 Limitación científica obligatoria

Registra explícitamente para análisis posteriores:

```text
EXP12_ANALYTICAL_LIMITATION =
HISTORICAL_BANK_DIVERSITY_EFFECT_NOT_ESTIMABLE_FROM_EXP12_BECAUSE_OFFICIAL_CONDITIONS_WERE_NOT_MATERIALIZED
```

Grupo 3 y la redacción futura no deberán presentar un efecto EXP12 ni inferir D-HIGH/D-MID/D-LOW como si hubieran sido ejecutados.

### 5.3 Próximo bloque

El orden maestro debe cambiar a:

```text
EXP12 Original Frozen Design ✅ CLOSED_WITHOUT_RETRIEVAL
  - planning precondition failed under frozen search
  - seed 20262001: 0 feasible / minimum 30
  - official D-HIGH/D-MID/D-LOW not selected
  - diversity effect not estimable from EXP12
  - no post-hoc relaxation, seed replacement or retry
  ↓
Grupo 2B — Reproducibilidad y trazabilidad ⏳ NEXT
  ↓
Grupo 3
```

Fija:

```text
NEXT_ELIGIBLE_BLOCK = GROUP2B_REPRODUCIBILITY_TRACEABILITY_CLOSURE
```

No marques Grupo 2B como iniciado todavía.

### 5.4 Historia y fecha

Conserva íntegramente la historia previa, incluyendo:

- Attempt001 de planning;
- diagnóstico forense;
- autorización forense v0.1 rechazada;
- autorización v0.2 integrada/consumida;
- resultado no gobernante;
- delimitación de no-inviabilidad global.

Mantén:

```text
Fecha de actualización = 2026-09-14
```

Añade una entrada cronológica `2026-09-14 — Disposición metodológica final EXP12` que explique que el cierre evita tuning post hoc y no equivale a demostrar inviabilidad global.

---

## 6. Prohibiciones absolutas

Durante Prompt69 NO:

- modifiques `main`;
- modifiques Article;
- ejecutes diagnóstico forense;
- ejecutes candidate generation;
- ejecutes planning;
- pruebes otros seeds;
- pruebes thresholds alternativos;
- calcules escenarios what-if;
- cambies TVD, cobertura, volumen, candidate_count, minimum feasible, seeds o quantiles;
- sustituyas o elimines el seed 20262001;
- selecciones D-HIGH/D-MID/D-LOW;
- ejecutes retrieval/BM25/Top-k/MRR;
- abras un EXP12 rediseñado;
- marques Grupo 2B como iniciado;
- avances a Grupo 3.

---

## 7. Verificaciones finales

Exige:

```text
origin/main = 5787503329afd5ddd5e94d04cdbbdeb000260cda
origin/docs/plan-maestro-temporal-2026-08-31 = cf8e9386e2c6ffa4bf9e1f2c401e85b8574a3880
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
```

Para el candidato de cierre exige:

```text
parent = cf8e9386e2c6ffa4bf9e1f2c401e85b8574a3880
commits_ahead = 1
commits_behind = 0
changed_path_count = 1
changed_path = docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md
```

Y confirma:

```text
EXP12_ORIGINAL_FROZEN_DESIGN = CLOSED
EXP12_RETRIEVAL_EXECUTED = false
EXP12_RETRIEVAL_AUTHORIZED = false
EXP12_DIVERSITY_EFFECT_ESTIMABLE = false
EXP12_REDESIGN_OPENED = false
GROUP2B_STARTED = false
GROUP3_STARTED = false
NEXT_ELIGIBLE_BLOCK = GROUP2B_REPRODUCIBILITY_TRACEABILITY_CLOSURE
```

---

## 8. Persistencia administrativa

Al finalizar vuelve a `codex/prompts-temporary` y crea únicamente:

```text
codex_prompts_tmp/69_RESPUESTA_INTEGRAR_PLAN_FORENSE_Y_CERRAR_DISPOSICION_METODOLOGICA_EXP12.md
```

El commit administrativo debe contener solo esa respuesta. No amend, no rebase, no force.

---

## 9. Reporte obligatorio

Reporta como mínimo:

```text
PROMPT69 = COMPLETED | STOP

main_final
plan_initial
plan_after_integration
article_final

PLAN_FORENSIC_RECONCILIATION_INTEGRATED
PLAN_INTEGRATION_MODE

EXP12_ORIGINAL_FROZEN_DESIGN
EXP12_DISPOSITION
EXP12_PLANNING_ATTEMPT_001
EXP12_FORENSIC_ATTEMPT_001
EXP12_FORENSIC_FINAL_UNIQUE_FEASIBLE
EXP12_FORENSIC_MINIMUM_REQUIRED
EXP12_PLANNING_OFFICIAL_CONDITIONS
EXP12_DIVERSITY_EFFECT_ESTIMABLE
EXP12_RETRIEVAL
EXP12_REDESIGN_IN_CURRENT_EXPERIMENT
EXP12_POST_HOC_PARAMETER_RELAXATION
EXP12_SEED_REPLACEMENT_OR_DROPPING
EXP12_GLOBAL_MATHEMATICAL_INFEASIBILITY_PROVEN
EXP12_OTHER_SEEDS_CHARACTERIZED
EXP12_ANALYTICAL_LIMITATION

PLAN_CANDIDATE_BRANCH
PLAN_CANDIDATE_COMMIT
PLAN_CANDIDATE_PARENT
PLAN_CANDIDATE_CHANGED_PATH_COUNT
PLAN_CANDIDATE_PUBLISHED

NEXT_ELIGIBLE_BLOCK = GROUP2B_REPRODUCIBILITY_TRACEABILITY_CLOSURE
GROUP2B_STARTED = false
GROUP3_STARTED = false
```

Respuesta terminal máxima:

```text
PROMPT69 = COMPLETED
EXP12_ORIGINAL_FROZEN_DESIGN = CLOSED
EXP12_DISPOSITION = CLOSED_WITHOUT_RETRIEVAL / PLANNING_PRECONDITION_FAILED_UNDER_FROZEN_SEARCH
EXP12_DIVERSITY_EFFECT_ESTIMABLE = false
EXP12_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
NEXT_ELIGIBLE_BLOCK = GROUP2B_REPRODUCIBILITY_TRACEABILITY_CLOSURE
```
