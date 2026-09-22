# PREF003 — Preauditoría independiente de la copia de tesis para futuro G7-F02

## 0. Rol

Actúa como **IA Ejecutora Independiente de Pretrabajo Metodológico**.

Tu tarea es realizar una preauditoría **no gobernante** de la copia de tesis actualmente identificada en las superficies de archivos del proyecto/Library:

```text
Molleapasa_gv(4).docx
```

Esta copia está identificada documentalmente como tesis del proyecto, pero **NO está verificada como master vigente** y no tiene SHA-256 primario congelado.

No eres la IA Experimental gestora. No apruebes tu propio trabajo.

---

## 1. Gobernanza y alcance

La secuencia formal permanece:

```text
G6-F02 → G6-F03 → GROUP6 CLOSED/APPROVED → G7-F01 → G7-F02 → G7-F03 → G8
```

Estado rector esperado:

```text
G6-F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G6-F02 = CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
G6-F03 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
GROUP6 = IN_PROGRESS
G7-F01 = PROSPECTIVE / NOT_AUTHORIZED
G7-F02 = PROSPECTIVE
```

**PREF003 NO activa G7-F01 ni G7-F02.**

Objetivo: identificar, con trazabilidad, qué partes de la copia de tesis están alineadas, obsoletas, superseded, incompletas o requieren verificación frente al estado científico cerrado de G3–G5 y al diseño visual aprobado de G6-F01.

No edites el Word. No propongas texto final de reemplazo. No redacciones una nueva tesis.

---

## 2. Separación ejecutor–auditor

Existe un artefacto previo creado directamente por la IA Experimental:

```text
preflight_tmp/PREG7_002_TESIS_PREAUDIT_G7_F02.md
```

Estado:

```text
SELF_GENERATED_UNAUDITED / NON_GOVERNING
```

Reglas obligatorias:

1. NO leas PREG7-002 al inicio.
2. Ejecuta primero tu análisis desde cero usando la tesis y las fuentes rectoras.
3. Cierra tus hallazgos independientes antes de abrir PREG7-002.
4. Solo al final compáralo con tu resultado para reportar convergencias, divergencias, omisiones y afirmaciones no soportadas.
5. No leas ni uses `PREG8-001` para construir el análisis.

---

## 3. Fuentes rectoras obligatorias

### 3.1 Gobernanza

Lee directamente:

```text
docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md
  rama: docs/plan-maestro-temporal-2026-08-31

docs/fichas/grupos_3_8/02_MATRIZ_DEPENDENCIAS_Y_ENTRADAS.md
docs/fichas/grupos_3_8/04_REGISTRO_ESTADO_FICHAS.md
  rama: docs/fichas-grupos-3-8
```

Usa como contexto preauditado:

```text
preflight_prompts_tmp/PREF001_RESPUESTA_PRETRABAJO_G7_F01_FUENTES.md@90f5baef9a800ca0b44334af23a7a8caeff8fd09
preflight_prompts_tmp/PREF002_RESPUESTA_CORRECCION_PREF001_IDENTIDAD_TESIS_Y_PROMPT106.md@c159b17bb2747bd2231db374422be2b11fa69616
```

PREF001/PREF002 son insumos de preflight auditados; no sustituyen las fuentes científicas primarias.

### 3.2 Grupo 3

Lee como mínimo:

```text
outputs/analysis/group3/g3_hypothesis_disposition_v0.1.json
outputs/analysis/group3/g3_inferential_results_v0.1.json
docs/analysis/group3/g3_inferential_methods_and_checks_v0.1.md
```

### 3.3 Grupo 4

Lee como mínimo:

```text
outputs/analysis/group4/g4_result_claim_evidence_matrix_v0.1.json
docs/analysis/group4/g4_interpretation_synthesis_v0.1.md
outputs/analysis/group4/g4_limitations_registry_v0.1.json
docs/analysis/group4/g4_literature_contrast_v0.1.md
```

### 3.4 Grupo 5

Lee:

```text
outputs/results/group5/g5_table_registry_v0.1.json
docs/results/group5/g5_canonical_tables_v0.1.md
docs/results/group5/g5_appendix_registry_v0.1.md
```

Y los nueve CSV canónicos G5 cuando sean necesarios para verificar cifras/roles.

### 3.5 Grupo 6

Usa únicamente la especificación aprobada:

```text
outputs/figures/group6/g6_figure_spec_registry_v0.1.json
```

No uses como evidencia final los renders candidatos G6-F02 todavía no aprobados.

### 3.6 Tesis

Lee íntegramente o con cobertura suficiente de todo el documento:

```text
Molleapasa_gv(4).docx
```

Debes cubrir como mínimo:

- problema general y específicos;
- objetivos;
- hipótesis general y específicas;
- variables/operacionalización;
- metodología y particiones;
- recuperación histórica;
- recuperación normativa;
- integración histórico–normativa;
- reranker diagnóstico;
- explicación LLM;
- resultados;
- contrastación HE1–HE5 e hipótesis general;
- discusión;
- limitaciones;
- conclusiones;
- figuras/tablas de resultados relevantes.

No presupongas que una cifra de la tesis sigue vigente solo porque no encuentres contradicción inmediata.

---

## 4. Ground truth mínimo que debe verificarse

```text
UNIT_OF_ANALYSIS = SERIE
DEPENDENCY_GROUP = DAM / DECLARACION cuando corresponda
EMPIRICAL_SCOPE = CAPITULO_87 / OFFLINE / INTERNAL_EVALUATION
EVAL_N = 1056
EVAL_DAM = 67
EVAL_NANDINA = 42
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
```

Guardrails:

```text
EXP11A = joint size/composition sensitivity / noncausal
EXP11B = descriptive / ten observed seed pairs / no seed-superpopulation inference
0B-05C = Attempt06 corrected current state only
EXP12 = CLOSED_WITHOUT_RETRIEVAL / NOT_ESTIMABLE
historical retrieval superiority != global RAG accuracy
normative evidence != binding legal correctness
auditable explanation != classification/legal correctness
configurability != empirical generalization
```

Uncertainty/presentation:

```text
HE2_A = 15 primary paired contrasts / 99% CI on paired differences / no arm-level CI
HE2_B = one primary Recall@200 − Recall@100 contrast / 95% CI
Phase E = descriptive only
Top50 = supplementary only
HE5 hierarchy/support = descriptive only
EXP12 = text-only / not estimable
```

---

## 5. Objetivo analítico

No se busca “corregir la tesis” todavía. Se busca producir una **matriz de discrepancias y preservación** para que la futura G7-F02 sepa exactamente qué debe conservar, actualizar, eliminar, verificar o reescribir.

Clasifica cada hallazgo como uno de:

```text
KEEP_EXACT
KEEP_WITH_TERMINOLOGY_REVIEW
UPDATE_REQUIRED
REWRITE_REQUIRED
REMOVE_OR_SUPERSEDE
VERIFY_AGAINST_OTHER_FROZEN_SOURCE
NOT_APPLICABLE
```

Severidad:

```text
BLOCKING_FOR_FINAL_G7_THESIS_CANDIDATE
MAJOR
MINOR
INFORMATIONAL
```

---

## 6. Entregable requerido

### A. Identidad y alcance

```text
THESIS_FILE_IDENTIFIED
THESIS_FILENAME
THESIS_MASTER_STATUS
THESIS_SHA256
FORMAL_G7_F02_AUTHORIZED
PREF003_IS_NON_GOVERNING
```

### B. Mapa por macrosección

Para cada macrosección de la tesis:

```text
section_or_topic
current_state
alignment_status
action
severity
primary_source
reason
```

### C. Matriz de discrepancias científicas

Incluye cada discrepancia material con:

```text
finding_id
location_in_thesis
observed_thesis_claim_or_value
current_frozen_state
source_artifact
classification
severity
future_G7_F02_action
```

Debes buscar expresamente:

1. tamaños de partición/población legacy;
2. métricas históricas/normativas legacy;
3. HE2 provisional vs SUPPORTED;
4. HE5 parcial/soportada vs INCONCLUSIVE;
5. categorías de soporte histórico no congeladas;
6. inferencias sobre descripciones ambiguas/incompletas pese a NOT_ESTIMABLE;
7. outputs 0B-05C superseded;
8. EXP12 reinterpretado indebidamente;
9. claims de generalización/accuracy/legal correctness;
10. figuras legacy fuera del catálogo G6-F01;
11. métodos/resultados que sigan refiriéndose a reejecuciones “pendientes” ya cerradas;
12. incongruencias SERIE/DAM;
13. CI/niveles de incertidumbre incompatibles con G3;
14. cualquier mezcla de evidencia descriptiva con confirmatoria.

### D. Hipótesis

Audita por separado:

```text
HG
HE1
HE2
HE3
HE4
HE5
```

Para HE2 y HE5 debes usar el cierre G3/G4 actual.

Para HE1/HE3/HE4/HG:
- no redecidas la hipótesis;
- verifica si el texto de la tesis coincide con el estado documentado disponible;
- si la fuente cerrada suficiente no está dentro de G3–G5, marca `VERIFY_AGAINST_OTHER_FROZEN_SOURCE` en lugar de inventar un dictamen.

### E. Tablas y figuras

Clasifica las tablas/figuras de resultados relevantes de la tesis como:

```text
KEEP
UPDATE_FROM_G5
REPLACE_BY_G6_APPROVED_PRESENTATION
REMOVE_AS_LEGACY
VERIFY
```

No autorices nuevas figuras.

### F. Scope estimado de futura G7-F02

Resume:

```text
PRESERVABLE_CORE
CRITICAL_UPDATE_AREAS
CRITICAL_REWRITE_AREAS
VERIFY_ONLY_AREAS
LEGACY_CONTENT_TO_REMOVE
```

### G. Riesgos heredables a G8

Lista específica derivada de la tesis, sin ejecutar G8.

### H. Comparación posterior con PREG7-002

Solo al final, lee:

```text
preflight_tmp/PREG7_002_TESIS_PREAUDIT_G7_F02.md
```

y reporta:

```text
CONVERGENCES
DIVERGENCES
UNSUPPORTED_ITEMS_IN_PREG7_002
MISSING_ITEMS_IN_PREG7_002
```

No modifiques PREG7-002.

---

## 7. Controles obligatorios

```text
PREF003_INDEPENDENT_ANALYSIS_BEFORE_PREG7_002_READ
PREF003_NO_G7_ACTIVATION
PREF003_NO_PLAN_MODIFICATION
PREF003_NO_FICHAS_MODIFICATION
PREF003_NO_MAIN_MODIFICATION
PREF003_NO_ARTICLE_MODIFICATION
PREF003_NO_THESIS_MODIFICATION
PREF003_NO_NEW_METRICS
PREF003_NO_NEW_INFERENCE
PREF003_NO_HYPOTHESIS_REDECISION
PREF003_G3_G4_G5_SOURCE_TRACEABILITY
PREF003_G6_RENDER_NOT_TREATED_AS_FINAL
PREF003_LEGACY_OUTPUTS_IDENTIFIED
PREF003_PREG7_002_TREATED_AS_NON_GOVERNING
PREF003_PENDING_EXTERNAL_AUDIT
```

---

## 8. Resultado terminal permitido

Uno de:

```text
READY_AS_THESIS_PREAUDIT
READY_AS_THESIS_PREAUDIT_WITH_NONBLOCKING_GAPS
REVISION_REQUIRED
BLOCKED
```

Este resultado no equivale a aprobación de G7-F02 ni de la tesis.

---

## 9. Persistencia

Trabaja exclusivamente sobre:

```text
codex/prompts-temporary
```

Crea únicamente:

```text
preflight_prompts_tmp/PREF003_RESPUESTA_PREAUDITORIA_INDEPENDIENTE_TESIS_G7_F02.md
```

No modifiques ningún otro archivo.

Debes registrar:

```text
SOURCE_PROMPT_COMMIT
MAIN_HEAD_OBSERVED
PLAN_HEAD_OBSERVED
FICHAS_HEAD_OBSERVED
THESIS_FILENAME_OBSERVED
fuentes primarias consultadas
resultado terminal
```

Finaliza con:

```text
PENDING_EXTERNAL_AUDIT_BY_IA_EXPERIMENTAL = true
```
