# PREF003 V02 — Preauditoría independiente de la tesis vigente para futuro G7-F02

## 0. Supersession y binding

Este prompt **supersede** para ejecución a:

```text
preflight_prompts_tmp/PREF003_PREAUDITORIA_INDEPENDIENTE_TESIS_G7_F02.md@9781085b0c07285c1896bc5312424aa6b7aedef8
```

Razón: el autor suministró y confirmó una tesis vigente exacta después de versionarse PREF003 V01.

```text
PREF003_V01 = SUPERSEDED / DO_NOT_EXECUTE
PREF003_V02 = CURRENT_PREFLIGHT_EXECUTION_SCOPE
```

No ejecutes PREF003 V01.

## 1. Rol

Actúa como **IA Ejecutora Independiente de Pretrabajo Metodológico**.

Tu tarea es realizar una preauditoría **no gobernante** de la tesis vigente exacta identificada por el autor.

No eres la IA Experimental gestora. No apruebes tu propio trabajo.

No actives G7-F01 ni G7-F02. No edites el Word. No modifiques Plan Maestro, fichas, `main`, artículo ni ramas científicas.

---

## 2. Tesis vigente obligatoria

Lee primero el manifiesto:

```text
preflight_tmp/THESIS_CURRENT_MASTER_MANIFEST_2026-09-22.md
commit = 4bea8c0034aa862b6b18de8d2307fdc8fffe80ea
```

La única tesis autorizada para este preflight es:

```text
ORIGINAL_UPLOADED_FILENAME = Molleapasa_gv(5).docx
CANONICAL_LIBRARY_FILENAME = Molleapasa_gv_vigente_2026-09-22.docx
CANONICAL_LIBRARY_PATH = /Tesis San Marcos/tesis_vigente/Molleapasa_gv_vigente_2026-09-22.docx
LIBRARY_FILE_ID = libfile_a4565dde90148191898d246f47c287e7
LIBRARY_BACKING_FILE_ID = file_0000000051cc820eba659f9c9c28771a
SHA256 = 08b48ec1687ae0a0d943724bf2d682aca02d2a9f5a124b3dc35270e041bc3aed
SIZE_BYTES = 4360620
PARSED_PAGE_COUNT = 129
THESIS_MASTER_STATUS = CURRENT_WORKING_MASTER / AUTHOR_CONFIRMED
```

La copia anterior:

```text
Molleapasa_gv(4).docx
```

es histórica y **no debe usarse** como tesis vigente.

Si no puedes acceder al archivo exacto por Library/path/file id, detente con `BLOCKED_CURRENT_THESIS_UNAVAILABLE`. No sustituyas otra copia por semejanza de nombre.

Si puedes materializar los bytes, verifica SHA-256 y exige coincidencia exacta. Si tu entorno solo permite lectura indexada y no materialización, registra expresamente `BYTE_HASH_RECHECK_NOT_AVAILABLE_IN_EXECUTOR`, pero no cambies la identidad fijada por el manifiesto.

---

## 3. Gobernanza y estado formal

La secuencia formal permanece:

```text
G6-F02 → G6-F03 → GROUP6 CLOSED/APPROVED → G7-F01 → G7-F02 → G7-F03 → G8
```

Estado esperado:

```text
G6-F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G6-F02 = CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
G6-F03 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
GROUP6 = IN_PROGRESS
G7-F01 = PROSPECTIVE / NOT_AUTHORIZED
G7-F02 = PROSPECTIVE
```

Este preflight no cambia estados.

---

## 4. Separación ejecutor–auditor

Existe un borrador previo generado directamente por la IA Experimental:

```text
preflight_tmp/PREG7_002_TESIS_PREAUDIT_G7_F02.md
```

Estado:

```text
SELF_GENERATED_UNAUDITED / NON_GOVERNING
```

Reglas:

1. NO leas PREG7-002 al inicio.
2. Ejecuta primero tu análisis desde cero usando la tesis vigente y las fuentes primarias.
3. Cierra tus hallazgos independientes.
4. Solo después lee PREG7-002 y compara convergencias/divergencias/omisiones.
5. No leas `PREG8-001` para construir tu análisis.

---

## 5. Fuentes rectoras obligatorias

### 5.1 Gobernanza

```text
docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md
  rama: docs/plan-maestro-temporal-2026-08-31

docs/fichas/grupos_3_8/02_MATRIZ_DEPENDENCIAS_Y_ENTRADAS.md
docs/fichas/grupos_3_8/04_REGISTRO_ESTADO_FICHAS.md
  rama: docs/fichas-grupos-3-8

preflight_prompts_tmp/PREF001_RESPUESTA_PRETRABAJO_G7_F01_FUENTES.md@90f5baef9a800ca0b44334af23a7a8caeff8fd09
preflight_prompts_tmp/PREF002_RESPUESTA_CORRECCION_PREF001_IDENTIDAD_TESIS_Y_PROMPT106.md@c159b17bb2747bd2231db374422be2b11fa69616
```

PREF001/PREF002 son preflight auditado; no sustituyen las fuentes científicas primarias.

### 5.2 Grupo 3

```text
outputs/analysis/group3/g3_hypothesis_disposition_v0.1.json
outputs/analysis/group3/g3_inferential_results_v0.1.json
docs/analysis/group3/g3_inferential_methods_and_checks_v0.1.md
```

### 5.3 Grupo 4

```text
outputs/analysis/group4/g4_result_claim_evidence_matrix_v0.1.json
docs/analysis/group4/g4_interpretation_synthesis_v0.1.md
outputs/analysis/group4/g4_limitations_registry_v0.1.json
docs/analysis/group4/g4_literature_contrast_v0.1.md
```

### 5.4 Grupo 5

```text
outputs/results/group5/g5_table_registry_v0.1.json
docs/results/group5/g5_canonical_tables_v0.1.md
docs/results/group5/g5_appendix_registry_v0.1.md
```

Consulta los nueve CSV G5 cuando sean necesarios para verificar cifras/roles.

### 5.5 Grupo 6

Usa únicamente como estado visual aprobado:

```text
outputs/figures/group6/g6_figure_spec_registry_v0.1.json
```

No trates los renders candidatos de G6-F02 como evidencia final.

---

## 6. Ground truth mínimo

Verifica y usa:

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

## 7. Cobertura obligatoria de la tesis

Cubre como mínimo:

- problema general y específicos;
- objetivos;
- hipótesis general y HE1–HE5;
- variables y operacionalización;
- unidad de análisis;
- población/muestra/particiones;
- selección y control de dependencia DAM;
- recuperación histórica;
- recuperación normativa;
- integración histórico–normativa;
- reranker diagnóstico;
- explicación LLM;
- técnicas de análisis e inferencia;
- resultados;
- contrastación de hipótesis;
- discusión;
- limitaciones;
- conclusiones;
- tablas y figuras de resultados relevantes.

No presupongas vigencia de una cifra por ausencia de contradicción inmediata.

---

## 8. Clasificación de hallazgos

Acción:

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

## 9. Entregable

### A. Identidad

Incluye:

```text
THESIS_FILE_IDENTIFIED = true
THESIS_ORIGINAL_FILENAME = Molleapasa_gv(5).docx
THESIS_CANONICAL_LIBRARY_FILENAME = Molleapasa_gv_vigente_2026-09-22.docx
THESIS_LIBRARY_FILE_ID = libfile_a4565dde90148191898d246f47c287e7
THESIS_EXPECTED_SHA256 = 08b48ec1687ae0a0d943724bf2d682aca02d2a9f5a124b3dc35270e041bc3aed
THESIS_MASTER_STATUS = CURRENT_WORKING_MASTER / AUTHOR_CONFIRMED
THESIS_FINAL_APPROVAL_STATUS = NOT_DECLARED
FORMAL_G7_F02_AUTHORIZED = false
PREF003_IS_NON_GOVERNING = true
```

Registra si pudiste recomprobar los bytes/hash.

### B. Mapa por macrosección

Para cada macrosección:

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

Cada hallazgo material:

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

Busca expresamente:

1. particiones/población legacy;
2. métricas históricas/normativas legacy;
3. HE2 provisional vs SUPPORTED;
4. HE5 parcial/soportada vs INCONCLUSIVE;
5. categorías de soporte histórico no congeladas;
6. inferencias sobre descripciones ambiguas/incompletas pese a NOT_ESTIMABLE;
7. outputs 0B-05C superseded;
8. EXP12 reinterpretado indebidamente;
9. generalización/accuracy/legal correctness;
10. figuras legacy fuera del catálogo G6-F01;
11. métodos/resultados que aún hablen de reejecuciones pendientes ya cerradas;
12. incongruencias SERIE/DAM;
13. ausencia o uso incorrecto de CI/niveles de incertidumbre de G3;
14. mezcla de evidencia descriptiva con confirmatoria;
15. cualquier texto que niegue inferencia estadística si G3 ya materializó inferencia autorizada;
16. dependencia entre series de una misma DAM insuficientemente reflejada en Methods/Results/Discussion.

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

HE2 y HE5 deben usar el cierre G3/G4 actual.

Para HG/HE1/HE3/HE4 no redecidas; usa `VERIFY_AGAINST_OTHER_FROZEN_SOURCE` si las fuentes suficientes están fuera de G3–G5.

### E. Tablas y figuras

Clasifica cada tabla/figura relevante:

```text
KEEP
UPDATE_FROM_G5
REPLACE_BY_G6_APPROVED_PRESENTATION
REMOVE_AS_LEGACY
VERIFY
```

No autorices figuras nuevas.

### F. Scope estimado de futura G7-F02

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

Solo al final lee:

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

---

## 10. Controles obligatorios

```text
PREF003_V02_CURRENT_THESIS_EXACTLY_BOUND
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

## 11. Resultado terminal

Uno de:

```text
READY_AS_THESIS_PREAUDIT
READY_AS_THESIS_PREAUDIT_WITH_NONBLOCKING_GAPS
REVISION_REQUIRED
BLOCKED_CURRENT_THESIS_UNAVAILABLE
BLOCKED
```

No equivale a aprobación de G7-F02 ni de la tesis.

---

## 12. Persistencia

Trabaja exclusivamente sobre:

```text
codex/prompts-temporary
```

Crea únicamente:

```text
preflight_prompts_tmp/PREF003_V02_RESPUESTA_PREAUDITORIA_INDEPENDIENTE_TESIS_G7_F02.md
```

Registra:

```text
SOURCE_PROMPT_COMMIT
THESIS_MANIFEST_COMMIT
MAIN_HEAD_OBSERVED
PLAN_HEAD_OBSERVED
FICHAS_HEAD_OBSERVED
THESIS_FILENAME_OBSERVED
THESIS_LIBRARY_FILE_ID_OBSERVED
THESIS_EXPECTED_SHA256
THESIS_HASH_RECHECK_STATUS
fuentes primarias consultadas
resultado terminal
```

Finaliza con:

```text
PENDING_EXTERNAL_AUDIT_BY_IA_EXPERIMENTAL = true
```
