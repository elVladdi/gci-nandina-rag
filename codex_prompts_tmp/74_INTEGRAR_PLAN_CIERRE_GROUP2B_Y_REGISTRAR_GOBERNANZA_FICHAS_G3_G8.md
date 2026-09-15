# PROMPT 74 — INTEGRAR PLAN DE CIERRE GROUP2B Y REGISTRAR GOBERNANZA DE FICHAS G3–G8

## Rol y objetivo

Actúa como **ejecutor técnico controlado**.

Este bloque realiza exclusivamente dos acciones documentales:

1. integrar mediante fast-forward exacto el Plan Maestro v0.2 de cierre de Grupo 2B ya auditado externamente;
2. preparar un candidato posterior del Plan Maestro que registre formalmente el sistema prospectivo de fichas de los Grupos 3–8, sin activar ni ejecutar ninguna ficha.

No ejecuta análisis, inferencia, experimentos, pipelines, tests científicos, retrieval, BM25, Top-k, MRR, generación de figuras, redacción científica ni modificación del artículo.

---

## 1. Dictamen externo que gobierna este bloque

La auditoría externa de IA Experimental sobre Prompt73 concluye:

```text
PROMPT73_EXTERNAL_AUDIT = PASS / APPROVED
GROUP2B_CLOSURE_RECORD = INTEGRATED / VERIFIED
G2B-CLOSE-F001 = RESOLVED
PLAN_GROUP2B_CLOSURE_V02 = APPROVED_FOR_INTEGRATION
GROUP2B = CLOSED / APPROVED_WITH_NONBLOCKING_LIMITATIONS
GROUP3 = NOT_STARTED
NEXT_ELIGIBLE_BLOCK = GROUP3_METRICS_AND_INFERENCE
```

Estado científico/documental canónico a exigir:

```text
origin/main = a33fc7e10b5bc25a053e982f0ff24ff60eda042f
origin/docs/plan-maestro-temporal-2026-08-31 = 0c77e86359bcd17ddd446429f21b62174c426f37
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
```

Plan aprobado para integración:

```text
branch = codex/plan-maestro-group2b-closure-v02
commit = d2c9bcdc8099df20890cd52cb1e6cc32208b686f
base canonical plan = 0c77e86359bcd17ddd446429f21b62174c426f37
commits_ahead = 2
commits_behind = 0
changed_path_count = 1
changed_path = docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md
```

Sistema prospectivo de fichas ya creado por IA Experimental:

```text
branch = docs/fichas-grupos-3-8
snapshot_commit = a42531ad96fc12bea2f2394b0ff8eb49b66a4238
root = docs/fichas/grupos_3_8/
```

Ese snapshot contiene 19 fichas ejecutables, más gobernanza, mapa maestro, matriz de dependencias, plantilla, registro de estados y handoff post-G8. Es un **diseño prospectivo**: su existencia no autoriza ejecución.

---

## 2. Precondiciones Git exactas

Ejecuta `git fetch` y exige exactamente:

```text
origin/main = a33fc7e10b5bc25a053e982f0ff24ff60eda042f
origin/docs/plan-maestro-temporal-2026-08-31 = 0c77e86359bcd17ddd446429f21b62174c426f37
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
origin/codex/plan-maestro-group2b-closure-v02 = d2c9bcdc8099df20890cd52cb1e6cc32208b686f
origin/docs/fichas-grupos-3-8 = a42531ad96fc12bea2f2394b0ff8eb49b66a4238
```

Verifica además:

```text
0c77e86359bcd17ddd446429f21b62174c426f37
  -> d2c9bcdc8099df20890cd52cb1e6cc32208b686f
status = ahead
commits_ahead = 2
commits_behind = 0
changed_path_count = 1
```

Para el snapshot de fichas, confirma que existen como mínimo:

```text
docs/fichas/grupos_3_8/README.md
docs/fichas/grupos_3_8/00_MAPA_MAESTRO_FICHAS_G3_G8.md
docs/fichas/grupos_3_8/01_GOBERNANZA_Y_ESTADOS.md
docs/fichas/grupos_3_8/02_MATRIZ_DEPENDENCIAS_Y_ENTRADAS.md
docs/fichas/grupos_3_8/03_PLANTILLA_FICHA.md
docs/fichas/grupos_3_8/04_REGISTRO_ESTADO_FICHAS.md
docs/fichas/grupos_3_8/99_POST_G8_FREEZE_HANDOFF.md
```

Y confirma que el mapa maestro contiene exactamente 19 IDs de ficha en esta secuencia:

```text
G3-F01, G3-F02, G3-F03, G3-F04,
G4-F01, G4-F02, G4-F03,
G5-F01, G5-F02, G5-F03,
G6-F01, G6-F02, G6-F03,
G7-F01, G7-F02, G7-F03,
G8-F01, G8-F02, G8-F03
```

Si existe drift de refs o falta alguno de esos controles:

```text
STOP / PRECONDITION_REF_OR_FICHA_SNAPSHOT_DRIFT
```

---

## 3. Fase A — integrar Plan v0.2 de cierre de Grupo 2B

Integra exclusivamente por fast-forward exacto la rama canónica:

```text
docs/plan-maestro-temporal-2026-08-31

0c77e86359bcd17ddd446429f21b62174c426f37
→
d2c9bcdc8099df20890cd52cb1e6cc32208b686f
```

Prohibidos merge commit, squash, cherry-pick, rebase, amend o reconstrucción manual.

Después exige:

```text
origin/docs/plan-maestro-temporal-2026-08-31 = d2c9bcdc8099df20890cd52cb1e6cc32208b686f
origin/main = a33fc7e10b5bc25a053e982f0ff24ff60eda042f
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
```

---

## 4. Fase B — candidato de gobernanza G3–G8 en Plan Maestro

Desde exactamente:

```text
d2c9bcdc8099df20890cd52cb1e6cc32208b686f
```

crea:

```text
branch = codex/plan-maestro-g3-g8-governance-v01
```

Modifica exclusivamente:

```text
docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md
```

Un solo commit. No modifiques `main`, Article ni la rama de fichas.

### 4.1 Registro obligatorio del sistema de fichas

Añade una subsección claramente identificable para **Gobernanza prospectiva de Grupos 3–8**, con al menos:

```text
FICHAS_G3_G8_BRANCH = docs/fichas-grupos-3-8
FICHAS_G3_G8_SNAPSHOT_COMMIT = a42531ad96fc12bea2f2394b0ff8eb49b66a4238
FICHAS_G3_G8_ROOT = docs/fichas/grupos_3_8/
FICHAS_G3_G8_COUNT = 19
FICHAS_G3_G8_STATUS = PROSPECTIVE / NOT_AUTHORIZED
GROUP3 = NOT_STARTED
NEXT_ELIGIBLE_FICHA = G3-F01
```

El Plan debe establecer explícitamente la jerarquía:

```text
PLAN MAESTRO
  gobierna estado, orden y autorización
    ↓
MAPA MAESTRO DE FICHAS
  gobierna secuencia y dependencias
    ↓
FICHA ACTIVA
  gobierna el contrato detallado del bloque
    ↓
PROMPT CODEX
  ejecuta solamente el bloque autorizado
    ↓
EVIDENCIA VERSIONADA
    ↓
AUDITORÍA EXTERNA IA EXPERIMENTAL
```

### 4.2 Regla de estados

Registra sin ambigüedad:

```text
FICHA_CREATED_OR_DEFINED
≠ FICHA_AUTHORIZED
≠ FICHA_EXECUTED
≠ FICHA_VERIFIED
≠ FICHA_APPROVED
≠ FICHA_INTEGRATED
≠ FICHA_CLOSED
```

La ficha siguiente solo puede activarse después del cierre auditado de su predecesora.

La activación de cada ficha debe congelar en ese momento —no reutilizar automáticamente el snapshot de diseño—:

- SHA vigente de `main`;
- SHA vigente del Plan Maestro;
- SHA de `article/main-manuscript` cuando aplique;
- fuentes primarias y artefactos de entrada;
- outputs esperados;
- prohibiciones;
- criterios PASS/FAIL;
- cualquier autorización one-shot o gate requerido.

El commit `a42531ad...` es únicamente el snapshot documental del sistema de fichas y **no es** un SHA científico de ejecución.

### 4.3 Secuencia oficial

Registra compactamente como secuencia prospectiva oficial:

```text
G3-F01 → G3-F02 → G3-F03 → G3-F04
→ G4-F01 → G4-F02 → G4-F03
→ G5-F01 → G5-F02 → G5-F03
→ G6-F01 → G6-F02 → G6-F03
→ G7-F01 → G7-F02 → G7-F03
→ G8-F01 → G8-F02 → G8-F03
→ POST-G8 FREEZE HANDOFF
```

No reproduzcas el contenido completo de las fichas dentro del Plan: referencia el mapa y la gobernanza por branch/path/snapshot.

### 4.4 Estado actual

El Plan candidato debe continuar reflejando:

```text
main = origin/main = a33fc7e10b5bc25a053e982f0ff24ff60eda042f
GROUP2B = CLOSED / APPROVED_WITH_NONBLOCKING_LIMITATIONS
GROUP3 = NOT_STARTED
NEXT_ELIGIBLE_BLOCK = GROUP3_METRICS_AND_INFERENCE
NEXT_ELIGIBLE_FICHA = G3-F01
```

No marques G3-F01 como `ACTIVE`, `AUTHORIZED`, `EXECUTED` ni equivalente. Solo queda elegible para futura activación después de auditoría/integración de este candidato del Plan.

### 4.5 Restricciones científicas a preservar

Mantén explícitamente vigentes, sin reinterpretación:

- EVAL v0.2 = 1,056 casos congelados;
- SERIE = unidad de análisis;
- DAM/DECLARACIÓN = agrupamiento cuando existe dependencia;
- EXP11A = sensibilidad, no efecto causal aislado del tamaño;
- todo análisis 0B-05C futuro usa Attempt06 corregido;
- EXP12 = cerrado sin retrieval y efecto de diversidad no estimable;
- 11 limitaciones no bloqueantes y 5 historical-only de Grupo 2B;
- `DECLARED_NOT_RECOVERABLE` y `HASH_BOUND_LOCAL_ONLY` permanecen visibles;
- no se cambian reglas analíticas después de observar resultados.

### 4.6 Historial

Añade entrada fechada 2026-09-15 indicando que:

- Grupo 2B ya quedó cerrado canónicamente;
- se registró el sistema prospectivo de 19 fichas G3–G8;
- el snapshot documental es `a42531ad...` en `docs/fichas-grupos-3-8`;
- ninguna ficha fue activada ni ejecutada;
- la siguiente ficha elegible es `G3-F01`;
- Grupo 3 sigue `NOT_STARTED`.

---

## 5. Verificaciones finales

Exige al finalizar:

```text
origin/main = a33fc7e10b5bc25a053e982f0ff24ff60eda042f
origin/docs/plan-maestro-temporal-2026-08-31 = d2c9bcdc8099df20890cd52cb1e6cc32208b686f
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
origin/docs/fichas-grupos-3-8 = a42531ad96fc12bea2f2394b0ff8eb49b66a4238
```

Para el candidato de gobernanza del Plan exige:

```text
parent = d2c9bcdc8099df20890cd52cb1e6cc32208b686f
commits_ahead_canonical = 1
commits_behind_canonical = 0
changed_path_count = 1
changed_path = docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md
```

Confirma:

```text
GROUP2B = CLOSED / APPROVED_WITH_NONBLOCKING_LIMITATIONS
FICHAS_G3_G8_STATUS = PROSPECTIVE / NOT_AUTHORIZED
NEXT_ELIGIBLE_FICHA = G3-F01
GROUP3_STARTED = false
SCIENTIFIC_EXECUTION_PERFORMED = false
RESULTS_RECOMPUTED = false
```

---

## 6. Prohibiciones absolutas

Durante Prompt74 NO:

- ejecutes ni actives G3-F01;
- produzcas análisis estadístico o inferencial;
- ejecutes experimentos, retrieval, BM25, Top-k, MRR o pipelines;
- regeneres resultados, datasets, manifests, logs o case-level;
- modifiques `main` salvo que un precondition check descubra drift, en cuyo caso debes STOP y no reparar;
- modifiques `article/main-manuscript`;
- modifiques `docs/fichas-grupos-3-8`;
- integres todavía el candidato de gobernanza G3–G8 al Plan canónico;
- cambies el contenido científico del cierre de Grupo 2B o EXP12.

---

## 7. Persistencia administrativa

Al finalizar vuelve a `codex/prompts-temporary` y crea únicamente:

```text
codex_prompts_tmp/74_RESPUESTA_INTEGRAR_PLAN_CIERRE_GROUP2B_Y_REGISTRAR_GOBERNANZA_FICHAS_G3_G8.md
```

El commit administrativo debe contener solo esa respuesta. No amend, no rebase, no force.

---

## 8. Reporte obligatorio

Reporta como mínimo:

```text
PROMPT74 = COMPLETED | STOP

main_final
plan_initial
plan_after_group2b_closure_integration
article_final
fichas_branch_final
fichas_snapshot_final

PLAN_GROUP2B_CLOSURE_V02_INTEGRATED

G3_G8_PLAN_CANDIDATE_BRANCH
G3_G8_PLAN_CANDIDATE_COMMIT
G3_G8_PLAN_CANDIDATE_PARENT
G3_G8_PLAN_CANDIDATE_COMMITS_AHEAD
G3_G8_PLAN_CANDIDATE_COMMITS_BEHIND
G3_G8_PLAN_CANDIDATE_CHANGED_PATH_COUNT
G3_G8_PLAN_CANDIDATE_PUBLISHED

FICHAS_G3_G8_COUNT
FICHAS_G3_G8_STATUS
NEXT_ELIGIBLE_FICHA
GROUP3_STARTED
SCIENTIFIC_EXECUTION_PERFORMED
RESULTS_RECOMPUTED
```

Respuesta terminal máxima:

```text
PROMPT74 = COMPLETED
PLAN_GROUP2B_CLOSURE_V02 = INTEGRATED
G3_G8_GOVERNANCE_PLAN = CANDIDATE_PENDING_EXTERNAL_AUDIT
FICHAS_G3_G8_STATUS = PROSPECTIVE / NOT_AUTHORIZED
NEXT_ELIGIBLE_FICHA = G3-F01
GROUP3_STARTED = false
```
