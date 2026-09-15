# PROMPT 70 — INTEGRAR CIERRE EXP12 E INICIAR READINESS DE GRUPO 2B

## Rol y objetivo

Actúa como **ejecutor técnico controlado**.

Este bloque realiza exclusivamente, en este orden:

1. integrar mediante fast-forward exacto el candidato del Plan Maestro que materializa el cierre metodológico definitivo del EXP12 original congelado;
2. iniciar **Grupo 2B — Reproducibilidad y trazabilidad** únicamente mediante una auditoría READ-ONLY de readiness sobre el estado científico ya versionado;
3. construir una matriz versionada de trazabilidad/reproducibilidad que identifique qué evidencia existe, dónde está, qué identidad/hashes la atan y qué brechas siguen abiertas;
4. publicar el paquete de readiness para auditoría externa.

Este bloque **NO ejecuta** experimentos, retrieval, BM25, Top-k, MRR, candidate generation, planning, diagnósticos, tests científicos, reconstrucciones de resultados ni regeneración de datasets. No modifica código, configs, datos, resultados científicos, Article ni outputs históricos.

---

## 1. Dictamen externo que gobierna este bloque

La auditoría externa de IA Experimental sobre Prompt69 concluye:

```text
PROMPT69_EXTERNAL_AUDIT = PASS / APPROVED

EXP12_ORIGINAL_FROZEN_DESIGN = CLOSED
EXP12_DISPOSITION = CLOSED_WITHOUT_RETRIEVAL / PLANNING_PRECONDITION_FAILED_UNDER_FROZEN_SEARCH
EXP12_DIVERSITY_EFFECT_ESTIMABLE = false
EXP12_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
EXP12_REDESIGN_IN_CURRENT_EXPERIMENT = NOT_AUTHORIZED
NEXT_ELIGIBLE_BLOCK = GROUP2B_REPRODUCIBILITY_TRACEABILITY_CLOSURE
```

Candidato de cierre del Plan aprobado:

```text
branch = codex/plan-maestro-exp12-methodological-disposition-v01
commit = 0c77e86359bcd17ddd446429f21b62174c426f37
parent = cf8e9386e2c6ffa4bf9e1f2c401e85b8574a3880
commits_ahead = 1
commits_behind = 0
changed_path_count = 1
changed_path = docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md
```

Estado científico que debe permanecer intacto:

```text
origin/main = 5787503329afd5ddd5e94d04cdbbdeb000260cda
origin/docs/plan-maestro-temporal-2026-08-31 = cf8e9386e2c6ffa4bf9e1f2c401e85b8574a3880
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
```

---

## 2. Precondiciones Git exactas

Ejecuta `git fetch` y exige exactamente:

```text
origin/main = 5787503329afd5ddd5e94d04cdbbdeb000260cda
origin/docs/plan-maestro-temporal-2026-08-31 = cf8e9386e2c6ffa4bf9e1f2c401e85b8574a3880
origin/codex/plan-maestro-exp12-methodological-disposition-v01 = 0c77e86359bcd17ddd446429f21b62174c426f37
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
```

Para el candidato del Plan exige:

```text
parent = cf8e9386e2c6ffa4bf9e1f2c401e85b8574a3880
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

## 3. Fase A — integrar exactamente el cierre EXP12 en el Plan canónico

Mueve exclusivamente:

```text
docs/plan-maestro-temporal-2026-08-31
```

mediante fast-forward exacto:

```text
cf8e9386e2c6ffa4bf9e1f2c401e85b8574a3880
→
0c77e86359bcd17ddd446429f21b62174c426f37
```

Prohibidos merge commit, squash, cherry-pick, rebase, amend o reconstrucción manual.

Después exige:

```text
origin/docs/plan-maestro-temporal-2026-08-31 = 0c77e86359bcd17ddd446429f21b62174c426f37
origin/main = 5787503329afd5ddd5e94d04cdbbdeb000260cda
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
```

---

## 4. Alcance exacto de Grupo 2B en este bloque

El Plan Maestro define Grupo 2B como el cierre posterior a EXP11B/EXP12 sobre:

```text
manifests
hashes
configs
seeds
scripts
logs
case-level
environment
clean checkout
end-to-end traceability matrix
final reproducibility level
```

Prompt70 **no cierra Grupo 2B**. Solo produce el inventario y diagnóstico de readiness necesario para decidir qué falta realmente antes del cierre.

La auditoría debe ser de procedencia y trazabilidad, no una reejecución experimental.

---

## 5. Fase B — checkout aislado y auditoría READ-ONLY

Trabaja desde un checkout/worktree nuevo, aislado y limpio del commit exacto:

```text
5787503329afd5ddd5e94d04cdbbdeb000260cda
```

Exige:

```text
TRACKED_WORKING_TREE_CLEAN = true
```

No modifiques nada durante el inventario.

### 5.1 Universo mínimo que debe cubrir la auditoría

Reconstruye la cadena de evidencia versionada de, como mínimo:

1. benchmark v0.2 congelado H100 / DEV / EVAL;
2. Grupo 1;
3. Grupo 2A;
4. EXP11A;
5. NEW_HISTORICAL_GATE / Gate 02 / Gate 03 / ingestas NUEVA_01 y NUEVA_02;
6. EXP11B Bank Materialization;
7. EXP11B portability replay/debt closure;
8. EXP11B Retrieval H150/H200;
9. 0B-05C y Attempt06 corregido;
10. EXP12 source binding / preplanning correction / planning Attempt001;
11. EXP12 diagnóstico forense y disposición final sin retrieval.

No inventes etapas que no existan. Si un elemento no es aplicable, clasifícalo `NOT_APPLICABLE`.

### 5.2 Fuentes de verdad permitidas

Usa únicamente evidencia versionada en Git del repositorio y el Plan Maestro canónico recién integrado. Puedes inspeccionar:

- archivos tracked;
- commits/trees/historia Git;
- manifests y readiness/closure records;
- configs;
- scripts;
- outputs versionados;
- logs versionados;
- case-level versionado;
- documentación de entorno ya existente;
- hashes declarados y artefactos a los que apuntan.

No dependas de archivos locales no versionados como fuente de verdad. Si un registro histórico declara que un artefacto fue local-only y solo está ligado por hash/tamaño, consérvalo como tal y clasifícalo explícitamente.

### 5.3 Clasificación obligatoria por artefacto/dependencia

Para cada dependencia relevante usa una de estas clases:

```text
VERSIONED_AND_IDENTITY_VERIFIED
VERSIONED_BUT_IDENTITY_NOT_FULLY_VERIFIABLE
HASH_BOUND_LOCAL_ONLY
DECLARED_NOT_RECOVERABLE
DECLARED_LIMITATION
NOT_APPLICABLE
MISSING_OR_UNBOUND
```

No conviertas automáticamente limitaciones históricas ya aceptadas en bloqueos nuevos. Distingue:

```text
BLOCKING_FOR_GROUP2B_CLOSURE
NONBLOCKING_DECLARED_LIMITATION
HISTORICAL_ONLY
```

### 5.4 Verificación de identidad

Cuando exista simultáneamente path versionado + SHA-256 declarado, verifica la identidad sin modificar el archivo.

Registra al menos:

```text
path
role
expected_sha256
observed_sha256
identity_status
source_commit_or_record
```

Para archivos textuales con historial de normalización LF, respeta la convención canónica ya utilizada por el proyecto y documenta cuál se aplicó.

No recalcules resultados científicos; hash de bytes no equivale a reejecución.

### 5.5 Trazabilidad end-to-end

Construye una matriz que, para cada bloque científico relevante, intente enlazar:

```text
SOURCE / INPUT
→ CONFIG / CONTRACT
→ SCRIPT / EXECUTION LOGIC
→ AUTHORIZATION / GATE cuando aplique
→ EXECUTION / ATTEMPT
→ RESULT / OUTPUT
→ CASE-LEVEL EVIDENCE cuando aplique
→ AUDIT / CLOSURE RECORD
→ INTEGRATION COMMIT / FINAL STATUS
```

Cada fila debe indicar si la cadena está:

```text
COMPLETE
COMPLETE_WITH_DECLARED_LIMITATION
PARTIAL_NONBLOCKING
BLOCKING_GAP
NOT_APPLICABLE
```

No rellenes silenciosamente enlaces faltantes.

### 5.6 Entorno y clean-checkout

Audita únicamente evidencia ya versionada sobre entorno/runtime y clean checkout.

No instales dependencias, no actualices lockfiles y no ejecutes el pipeline.

Clasifica por separado:

```text
ENVIRONMENT_REPRODUCIBILITY
CLEAN_CHECKOUT_REPRODUCIBILITY
```

indicando evidencia existente, limitaciones heredadas y si alguna brecha bloquea Grupo 2B.

### 5.7 Seeds y parámetros prospectivos

Verifica que los seeds/configs relevantes estén versionados o congelados en evidencia trazable. No generes seeds nuevos ni ejecutes selectors.

Incluye expresamente:

- EXP11A seeds/composiciones;
- EXP11B condiciones/materializaciones;
- EXP12 seeds congelados `20262001..20262010` y cierre sin sustitución post hoc.

### 5.8 Outputs y case-level

Inventaría outputs agregados y case-level que existan realmente.

Para EXP12 registra expresamente:

```text
retrieval output = NOT_APPLICABLE / NOT_EXECUTED_BY_FINAL_DISPOSITION
case-level retrieval evidence = NOT_APPLICABLE
forensic aggregate evidence = VERSIONED_AND_IDENTITY_VERIFIED si corresponde
```

No marques la ausencia de retrieval EXP12 como gap de reproducibilidad: es consecuencia científica del cierre aprobado.

---

## 6. Artefactos candidatos de readiness

Desde exactamente:

```text
5787503329afd5ddd5e94d04cdbbdeb000260cda
```

crea la rama:

```text
codex/group2b-reproducibility-readiness-v01
```

Un solo commit que añada exclusivamente:

```text
docs/group2b_reproducibility_traceability_readiness_v0.1.md
outputs/audits/group2b_reproducibility_readiness_v0.1.json
```

No modifiques ningún archivo existente.

### 6.1 Markdown obligatorio

`docs/group2b_reproducibility_traceability_readiness_v0.1.md` debe incluir:

1. scope y estado;
2. commits canónicos leídos;
3. inventario por bloque científico;
4. matriz end-to-end;
5. identity/hash verification summary;
6. manifest/config/seed/script/log/case-level status;
7. environment y clean-checkout status;
8. gaps clasificados por severidad;
9. limitaciones históricas ya aceptadas que permanecen no bloqueantes;
10. recomendación de siguiente paso **sin cerrar todavía Grupo 2B**.

### 6.2 JSON obligatorio

`outputs/audits/group2b_reproducibility_readiness_v0.1.json` debe contener al menos:

```text
artifact = GROUP2B_REPRODUCIBILITY_TRACEABILITY_READINESS
version = v0.1
status = CANDIDATE_PENDING_EXTERNAL_AUDIT
scientific_main_commit = 5787503329afd5ddd5e94d04cdbbdeb000260cda
canonical_plan_commit = 0c77e86359bcd17ddd446429f21b62174c426f37
article_commit = 254b1e6df736fa9938ac86a515d65b36f4d361c5
read_only_audit = true
scientific_execution_performed = false
results_recomputed = false
tracked_working_tree_clean = true
```

Incluye arrays/objetos para:

```text
artifact_inventory
identity_checks
end_to_end_matrix
blocking_gaps
nonblocking_limitations
historical_only_items
environment_reproducibility
clean_checkout_reproducibility
proposed_next_block
```

No declares `GROUP2B_CLOSED=true` en Prompt70.

---

## 7. Verificaciones finales

Exige:

```text
origin/main = 5787503329afd5ddd5e94d04cdbbdeb000260cda
origin/docs/plan-maestro-temporal-2026-08-31 = 0c77e86359bcd17ddd446429f21b62174c426f37
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
```

Para el candidato Group2B exige:

```text
parent = 5787503329afd5ddd5e94d04cdbbdeb000260cda
commits_ahead = 1
commits_behind = 0
changed_path_count = 2
changed_paths =
  docs/group2b_reproducibility_traceability_readiness_v0.1.md
  outputs/audits/group2b_reproducibility_readiness_v0.1.json
```

Confirma:

```text
GROUP2B_READINESS_AUDIT = COMPLETED_CANDIDATE_PENDING_EXTERNAL_AUDIT
GROUP2B_CLOSED = false
SCIENTIFIC_EXECUTION_PERFORMED = false
RESULTS_RECOMPUTED = false
EXP12_REOPENED = false
GROUP3_STARTED = false
```

---

## 8. Prohibiciones absolutas

Durante Prompt70 NO:

- modifiques `main`;
- modifiques Article;
- modifiques datos/configs/scripts/tests/results/logs históricos;
- ejecutes experimentos o pipelines;
- ejecutes retrieval/BM25/Top-k/MRR;
- ejecutes tests científicos como sustituto de evidencia histórica;
- regeneres manifests/results/case-level;
- reconstruyas artefactos local-only;
- abras EXP12;
- marques Grupo 2B como cerrado;
- avances a Grupo 3.

---

## 9. Persistencia administrativa

Al finalizar vuelve a `codex/prompts-temporary` y crea únicamente:

```text
codex_prompts_tmp/70_RESPUESTA_INTEGRAR_CIERRE_EXP12_E_INICIAR_READINESS_GROUP2B_REPRODUCIBILIDAD.md
```

El commit administrativo debe contener solo esa respuesta. No amend, no rebase, no force.

---

## 10. Reporte obligatorio

Reporta como mínimo:

```text
PROMPT70 = COMPLETED | STOP

main_final
plan_initial
plan_final
article_final
PLAN_EXP12_CLOSURE_INTEGRATED
PLAN_INTEGRATION_MODE

GROUP2B_BRANCH
GROUP2B_COMMIT
GROUP2B_PARENT
GROUP2B_CHANGED_PATH_COUNT
GROUP2B_PUBLISHED

TRACKED_WORKING_TREE_CLEAN
READ_ONLY_AUDIT
SCIENTIFIC_EXECUTION_PERFORMED
RESULTS_RECOMPUTED

ARTIFACT_INVENTORY_COUNT
IDENTITY_CHECK_COUNT
IDENTITY_CHECK_PASS_COUNT
IDENTITY_CHECK_NONPASS_COUNT
END_TO_END_MATRIX_ROW_COUNT
COMPLETE_ROW_COUNT
COMPLETE_WITH_DECLARED_LIMITATION_ROW_COUNT
PARTIAL_NONBLOCKING_ROW_COUNT
BLOCKING_GAP_ROW_COUNT
NOT_APPLICABLE_ROW_COUNT
BLOCKING_GAP_COUNT
NONBLOCKING_LIMITATION_COUNT
HISTORICAL_ONLY_COUNT
ENVIRONMENT_REPRODUCIBILITY_STATUS
CLEAN_CHECKOUT_REPRODUCIBILITY_STATUS
PROPOSED_NEXT_BLOCK

GROUP2B_CLOSED = false
EXP12_REOPENED = false
GROUP3_STARTED = false
```

Respuesta terminal máxima:

```text
PROMPT70 = COMPLETED
PLAN_EXP12_CLOSURE_INTEGRATED = true
GROUP2B_READINESS_AUDIT = COMPLETED_CANDIDATE_PENDING_EXTERNAL_AUDIT
GROUP2B_CLOSED = false
SCIENTIFIC_EXECUTION_PERFORMED = false
RESULTS_RECOMPUTED = false
GROUP3_STARTED = false
```
