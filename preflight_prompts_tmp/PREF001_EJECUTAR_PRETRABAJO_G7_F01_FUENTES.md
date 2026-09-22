# PREF001 — Ejecutar pretrabajo independiente para G7-F01: inventario y freeze preliminar de fuentes

## 0. Rol

Actúa como **IA Ejecutora Independiente de Pretrabajo Metodológico**.

Tu función en este prompt es ejecutar un preflight **no gobernante** y producir una respuesta versionada que luego será auditada externamente por la IA Experimental.

No eres la IA Experimental gestora. No debes aprobar tu propio trabajo ni cambiar estados operacionales.

---

## 1. Contexto de gobernanza

La secuencia formal de fichas sigue siendo vinculante:

```text
G6-F02 → G6-F03 → GROUP6 CLOSED/APPROVED → G7-F01 → G7-F02 → G7-F03 → G8
```

Estado rector esperado al iniciar este pretrabajo:

```text
G6-F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G6-F02 = CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
G6-F03 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
G7-F01 = PROSPECTIVE
G7-F02 = PROSPECTIVE
G7-F03 = PROSPECTIVE
GROUP6 = IN_PROGRESS
```

Debes verificar estos estados directamente en las fuentes actuales. Si observas divergencia entre Plan Maestro, registro de fichas y otras fuentes, repórtala; no la resuelvas silenciosamente.

**Este prompt NO activa G7-F01.**

---

## 2. Importante: reparación de separación ejecutor–auditor

Existen tres artefactos previos creados directamente por la IA Experimental:

```text
preflight_tmp/PREG7_001_G7_F01_SOURCE_FREEZE_PREFLIGHT.md
preflight_tmp/PREG7_002_TESIS_PREAUDIT_G7_F02.md
preflight_tmp/PREG8_001_PREFLIGHT_COHERENCIA_Y_CLAIM_EVIDENCE.md
```

Esos artefactos son **SELF_GENERATED_UNAUDITED / NON_GOVERNING**.

Regla obligatoria:

1. NO los leas al inicio.
2. Ejecuta tu análisis desde cero usando solo fuentes rectoras.
3. Solo después de completar y fijar tus hallazgos independientes puedes leer `PREG7_001_G7_F01_SOURCE_FREEZE_PREFLIGHT.md` para comparar convergencias/divergencias.
4. No uses PREG7-001 como evidencia primaria.
5. No leas PREG7-002 ni PREG8-001 en esta tarea, porque pertenecen a etapas posteriores del pretrabajo.

El objetivo es restaurar independencia entre **ejecución** y **auditoría**.

---

## 3. Objetivo

Construir un **preflight independiente de G7-F01** que determine, sin activar Grupo 7:

1. qué fuentes G3–G6 están ya suficientemente cerradas para formar parte del futuro `writing source freeze`;
2. cuáles todavía no pueden congelarse por depender de G6-F02/G6-F03;
3. qué estado tiene el artículo y qué fuentes editoriales gobiernan su futura sincronización;
4. qué requisitos de tesis no pueden todavía congelarse si no existe Word maestro identificado/hash verificable;
5. qué claims/guardrails deben quedar obligatoriamente protegidos en el futuro Grupo 7;
6. qué drift existe entre el snapshot editorial del artículo y el estado experimental actual;
7. qué riesgos deben heredarse después a G7-F02/G7-F03 y G8.

No redactes tesis ni artículo.

---

## 4. Fuentes obligatorias a leer íntegramente

### 4.1 Gobernanza experimental

Lee directamente en GitHub:

```text
docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md
  rama: docs/plan-maestro-temporal-2026-08-31

docs/fichas/grupos_3_8/00_MAPA_MAESTRO_FICHAS_G3_G8.md
docs/fichas/grupos_3_8/02_MATRIZ_DEPENDENCIAS_Y_ENTRADAS.md
docs/fichas/grupos_3_8/04_REGISTRO_ESTADO_FICHAS.md
docs/fichas/grupos_3_8/grupo_7/G7_F01_SINCRONIZACION_EDITORIAL_Y_CONTRATO_REDACCION.md
```

Usa la rama viva `docs/fichas-grupos-3-8` para las fichas.

### 4.2 Fuentes científicas G3–G5

Como mínimo verifica existencia, rol y estado operativo de:

```text
outputs/analysis/group3/g3_hypothesis_disposition_v0.1.json
outputs/analysis/group4/g4_result_claim_evidence_matrix_v0.1.json
docs/analysis/group4/g4_interpretation_synthesis_v0.1.md
outputs/analysis/group4/g4_limitations_registry_v0.1.json
docs/analysis/group4/g4_literature_contrast_v0.1.md
outputs/results/group5/g5_table_registry_v0.1.json
docs/results/group5/g5_canonical_tables_v0.1.md
docs/results/group5/g5_appendix_registry_v0.1.md
```

Consulta también los nueve CSV canónicos G5 cuando sea necesario para verificar roles.

### 4.3 Grupo 6

Verifica:

```text
outputs/figures/group6/g6_figure_spec_registry_v0.1.json
```

en `main` vigente.

Verifica además el estado actual de G6-F02 en fichas y la existencia del candidato remoto si está registrado.

No apruebes G6-F02 y no audites el render aquí.

### 4.4 Artículo

Realiza onboarding completo en `article/main-manuscript` siguiendo:

```text
article/START_HERE.md
article/README.md
article/ARTICLE_STATUS.md
article/ARTICLE_WRITING_PLAN.md
article/DECISIONS.md
article/SOURCE_REGISTRY.md
article/CLAIM_EVIDENCE_MATRIX.md
article/STYLE_GUIDE.md
```

Debes identificar expresamente:

```text
CANONICAL_MASTER
CURRENT_DRAFTING_PHASE
CURRENT_AUTHORIZED_BLOCK
CURRENT_EXPERIMENTAL_SNAPSHOT_CONSUMED_BY_ARTICLE
G6/G7 concurrency rule
```

No modifiques la rama del artículo.

### 4.5 Tesis

Para esta tarea **no es obligatorio leer el contenido completo de la tesis**.

Solo determina si existe una copia de tesis/Word maestro identificable y si puedes verificar de manera fiable:

```text
filename
master status
SHA-256
```

Si no puedes verificar alguno, registra el bloqueo exacto para el futuro freeze formal. No inventes hash ni master status.

---

## 5. Verificaciones científicas mínimas

Debes verificar de fuentes primarias, no de memoria:

```text
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
UNIT_OF_ANALYSIS = SERIE
DEPENDENCY_GROUP = DAM / DECLARACION cuando corresponda
EMPIRICAL_SCOPE = CAPITULO_87 / OFFLINE / INTERNAL_EVALUATION
EVAL_N = 1056
EVAL_DAM = 67
EVAL_NANDINA = 42
```

Y los guardrails:

```text
EXP11A = joint size/composition sensitivity / noncausal
EXP11B = descriptive / ten observed seed pairs / no seed-superpopulation inference
0B-05C = Attempt06 current corrected state only
EXP12 = CLOSED_WITHOUT_RETRIEVAL / NOT_ESTIMABLE
historical retrieval superiority != global RAG accuracy
normative evidence != binding legal correctness
auditable explanation != classification/legal correctness
```

---

## 6. Entregable requerido

Tu respuesta debe contener como mínimo:

### A. Estado de gobernanza observado

Tabla o bloque con:

```text
main HEAD
Plan HEAD
fichas HEAD
article HEAD
G6-F01 state
G6-F02 state
G6-F03 state
Group6 state
G7-F01 state
```

Si Plan y fichas divergen, clasifica la divergencia.

### B. Inventario de fuentes para futuro G7-F01

Clasifica cada familia como:

```text
READY_FOR_FUTURE_FREEZE
PARTIALLY_READY
NOT_READY
BLOCKED_MISSING_IDENTITY
```

para:

```text
G3
G4
G5
G6
thesis master
article governance
bibliographic/literature controls
```

### C. Matriz preliminar claim → presentación → destino

Como mínimo G3C-001..G3C-018, indicando:

```text
claim_id
scientific role
canonical evidence/table
figure if applicable
future thesis destination
future article destination
mandatory qualification
```

No inventes destino si la gobernanza no lo soporta; marca `TO_BE_FROZEN_IN_G7`.

### D. Estado del artículo

Determina si existe drift entre su snapshot experimental consumido y el estado experimental actual.

Clasifica:

```text
SCIENTIFIC_CONTRADICTION
EDITORIAL_SNAPSHOT_STALENESS
NO_DRIFT
```

Indica si ese drift bloquea Architecture B01 ahora o solo requiere reconciliación futura.

### E. Estado de tesis para freeze

Solo identidad/gobernanza:

```text
THESIS_FILE_IDENTIFIED
THESIS_SHA256_VERIFIED
THESIS_MASTER_STATUS
FORMAL_G7_F01_THESIS_FREEZE_READY
```

### F. Guardrails obligatorios para G7

Lista controlada de afirmaciones/interpretaciones prohibidas o condicionadas.

### G. Riesgos heredables a G7/G8

Lista priorizada, sin ejecutar G8.

### H. Comparación posterior con PREG7-001

Solo al final, después de cerrar tu análisis independiente, lee:

```text
preflight_tmp/PREG7_001_G7_F01_SOURCE_FREEZE_PREFLIGHT.md
```

y reporta:

```text
CONVERGENCES
DIVERGENCES
UNSUPPORTED_ITEMS_IN_PREG7_001
MISSING_ITEMS_IN_PREG7_001
```

No corrijas el archivo previo.

---

## 7. Controles obligatorios PASS/FAIL

Debes cerrar con estos controles:

```text
PREF001_INDEPENDENT_ANALYSIS_BEFORE_PREG_READ
PREF001_NO_G7_ACTIVATION
PREF001_NO_PLAN_MODIFICATION
PREF001_NO_FICHAS_MODIFICATION
PREF001_NO_MAIN_MODIFICATION
PREF001_NO_ARTICLE_MODIFICATION
PREF001_NO_THESIS_MODIFICATION
PREF001_G3_G4_G5_SOURCE_TRACEABILITY
PREF001_G6_NOT_PREMATURELY_FROZEN
PREF001_ARTICLE_ONBOARDING_COMPLETE
PREF001_THESIS_IDENTITY_NOT_INVENTED
PREF001_HE2_HE5_GUARDRAILS_PRESERVED
PREF001_EXP11A_EXP11B_EXP12_GUARDRAILS_PRESERVED
PREF001_PREG7_001_TREATED_AS_NON_GOVERNING
```

Si alguno falla, el resultado terminal no puede ser `READY_AS_PREFLIGHT`.

---

## 8. Resultado terminal permitido

Uno de:

```text
READY_AS_PREFLIGHT
READY_AS_PREFLIGHT_WITH_NONBLOCKING_GAPS
REVISION_REQUIRED
BLOCKED
```

Este resultado **no equivale a aprobación de G7-F01**.

---

## 9. Persistencia obligatoria

Trabaja exclusivamente sobre la rama:

```text
codex/prompts-temporary
```

Crea únicamente:

```text
preflight_prompts_tmp/PREF001_RESPUESTA_PRETRABAJO_G7_F01_FUENTES.md
```

No modifiques ningún otro archivo.

La respuesta debe registrar:

```text
source prompt path
source prompt commit
refs/commits efectivamente observados
fuentes primarias consultadas
resultado terminal
```

No crees commits en `main`, Plan, fichas ni artículo.

---

## 10. Regla de cierre

No te declares aprobado. El output queda:

```text
PENDING_EXTERNAL_AUDIT_BY_IA_EXPERIMENTAL = true
```

La IA Experimental hará la auditoría independiente posterior.
