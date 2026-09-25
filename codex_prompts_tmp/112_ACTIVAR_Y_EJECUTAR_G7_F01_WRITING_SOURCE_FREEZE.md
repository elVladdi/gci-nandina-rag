# PROMPT112 — ACTIVAR Y EJECUTAR G7-F01: SINCRONIZACIÓN EDITORIAL Y WRITING SOURCE FREEZE

## 0. Rol y objetivo

Actúa como **CODEX ejecutor reproducible** del proyecto `elVladdi/gci-nandina-rag`.

Esta es una utilización necesaria de CODEX porque G7-F01 exige reconstruir y versionar un **source freeze exacto**, con commits/blobs, onboarding del artículo, reconciliación de gobernanza y dos artefactos persistentes. No debes redactar ni modificar la tesis ni el artículo.

Debes ejecutar exclusivamente **G7-F01 — Sincronización editorial y contrato de redacción**.

Objetivo formal:

> congelar qué documentos se redactarán/actualizarán y qué fuente gobierna cada claim antes de escribir.

Tu ejecución debe:

1. activar formalmente G7-F01 después del cierre auditado de Grupo 6;
2. reconstruir el estado científico y editorial que gobernará G7;
3. congelar la identidad de la tesis vigente de corrección;
4. completar el onboarding vigente de `article/main-manuscript` sin modificar esa rama;
5. congelar fuentes y precedencia para cada familia de claims;
6. resolver formalmente el preflight pendiente de `HG` y `HE1` como **presencia o ausencia de disposición formal**, sin inventar una;
7. separar texto a conservar, actualizar, reescribir, verificar y texto nuevo permitido;
8. materializar únicamente el candidato de `writing source freeze`;
9. dejar G7-F02 sin autorización hasta auditoría externa de la IA Experimental.

No redactes secciones científicas. No edites Word. No edites el artículo. No redecidas hipótesis.

---

## 1. Estado vinculante de entrada

La IA Experimental auditó Prompt111 y establece como estado vinculante para esta activación:

```text
PROMPT111_EXTERNAL_AUDIT = PASS
MAIN = e93b44164a9619dad1f527a3b2d4479265858e39
G6_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G6_F02 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G6_F03 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
GROUP6 = CLOSED / APPROVED
G7_F01 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
G7_F02 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
G7_F03 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
GROUP7 = NOT_STARTED
GROUP8 = NOT_STARTED / NOT_AUTHORIZED
```

Refs documentales esperados:

```text
origin/main = e93b44164a9619dad1f527a3b2d4479265858e39
origin/docs/fichas-grupos-3-8 = bed229d81b2ce3258e1ac3c9efc171458e2891aa
origin/docs/plan-maestro-temporal-2026-08-31 = cc9a47986dfbae138738ad9945f0c0b1859b9f4f
```

La instrucción permanente del autor de continuar automáticamente autoriza **solo la activación y ejecución de G7-F01** una vez cumplida su dependencia. No autoriza G7-F02 ni G7-F03.

---

## 2. Ficha y gobernanza obligatorias

Lee íntegramente antes de ejecutar:

```text
docs/fichas/grupos_3_8/00_MAPA_MAESTRO_FICHAS_G3_G8.md
docs/fichas/grupos_3_8/01_GOBERNANZA_Y_ESTADOS.md
docs/fichas/grupos_3_8/02_MATRIZ_DEPENDENCIAS_Y_ENTRADAS.md
docs/fichas/grupos_3_8/04_REGISTRO_ESTADO_FICHAS.md
docs/fichas/grupos_3_8/grupo_7/G7_F01_SINCRONIZACION_EDITORIAL_Y_CONTRATO_REDACCION.md
```

Reglas obligatorias:

```text
ELIGIBLE != AUTHORIZED
G7-F01 puede activarse porque Grupo 6 está CLOSED / APPROVED
G7-F02 no puede activarse antes del cierre auditado de G7-F01
G7-F03 no puede activarse antes del cierre auditado de G7-F02
```

---

## 3. Workspace y preflight Git

Trabaja exclusivamente en el workspace canónico:

```text
C:\Users\Vladimir\OneDrive\Documentos\Maestría UNMSM\LLM_RGA_NANDINA
```

Antes de cualquier modificación registra:

```powershell
cd "C:\Users\Vladimir\OneDrive\Documentos\Maestría UNMSM\LLM_RGA_NANDINA"
git rev-parse --show-toplevel
git remote get-url origin
git status --porcelain
git worktree list
git fetch origin
git rev-parse origin/main
git rev-parse origin/docs/fichas-grupos-3-8
git rev-parse origin/docs/plan-maestro-temporal-2026-08-31
git rev-parse origin/article/main-manuscript
git rev-parse origin/codex/prompts-temporary
```

STOP si:

- workspace u origin no son los canónicos;
- `origin/main`, fichas o Plan no coinciden con los refs de la Sección 1;
- existen cambios tracked preexistentes no explicados;
- no puedes preservar los untracked históricos conocidos.

La rama del artículo es una fuente editorial viva. El head observado al diseñar este prompt fue:

```text
ARTICLE_HEAD_OBSERVED_AT_PROMPT_DESIGN = 2aad97aaceec0af6be0edb9ba0dd29170ad35baf
```

Si `origin/article/main-manuscript` cambió antes de ejecutar, **no hagas STOP solo por ese cambio**. Debes realizar onboarding completo en el head realmente observado, registrar el nuevo SHA y verificar si introduce una contradicción material con las fuentes científicas cerradas G3–G6. Si existe contradicción material, termina `BLOCKED_ARTICLE_STATE_CONFLICT` sin crear candidato.

---

## 4. Identidad formal de la tesis vigente

Fuente preparatoria de identidad:

```text
preflight_tmp/THESIS_CURRENT_MASTER_MANIFEST_2026-09-22.md
blob esperado = 42b89b512b8db818238bfd0da22a7c75c207d9f1
```

Congela literalmente:

```text
ORIGINAL_UPLOADED_FILENAME = Molleapasa_gv(5).docx
CANONICAL_LIBRARY_FILENAME = Molleapasa_gv_vigente_2026-09-22.docx
CANONICAL_LIBRARY_PATH = /Tesis San Marcos/tesis_vigente/Molleapasa_gv_vigente_2026-09-22.docx
LIBRARY_FILE_ID = libfile_a4565dde90148191898d246f47c287e7
SHA256 = 08b48ec1687ae0a0d943724bf2d682aca02d2a9f5a124b3dc35270e041bc3aed
SIZE_BYTES = 4360620
PARSED_PAGE_COUNT = 129
THESIS_MASTER_STATUS = CURRENT_WORKING_MASTER / AUTHOR_CONFIRMED
THESIS_CORRECTION_BASELINE = true
THESIS_IS_CURRENT_SCIENTIFIC_GROUND_TRUTH = false
```

G7-F01 no requiere editar ni volver a materializar el binario Word. No afirmes haber recalculado el SHA-256 si el executor no tiene acceso byte a byte.

Debes fijar:

```text
THESIS_IDENTITY_FREEZE_SOURCE = VERSIONED_MANIFEST
THESIS_BYTE_HASH_RECHECK_IN_G7_F01 = NOT_PERFORMED_UNLESS_BYTES_AVAILABLE
THESIS_BYTE_HASH_RECHECK_BEFORE_G7_F02_EDIT = REQUIRED
```

Si el manifest no coincide con el blob esperado o aparece un manifest posterior expresamente autor-confirmado, detente y reporta `THESIS_IDENTITY_CONFLICT`.

La copia `Molleapasa_gv(4).docx` es histórica y no debe usarse como baseline.

---

## 5. Prework permitido como evidencia auxiliar, nunca como autoridad científica

Lee íntegramente:

```text
preflight_prompts_tmp/PREF003_V02_RESPUESTA_PREAUDITORIA_INDEPENDIENTE_TESIS_G7_F02.md
response commit histórico = 7782041ac6749f383779aedb7303e91a87177d8a
blob actual esperado = 27d1ed8a54bc661485a6f38ac77a3d9ef0775e58

preflight_prompts_tmp/PREF004_RESPUESTA_TRAZABILIDAD_FUENTES_HG_HE1_HE3_HE4_PARA_G7.md
response commit histórico = f4d1d6f494537c023f0de2f632273b10c0f2146a
blob actual esperado = 693d43a0c7f87627de744a016f07c736a3160b1c
```

Semántica obligatoria:

```text
PREF003 = NON_GOVERNING / thesis discrepancy map only
PREF004 = NON_GOVERNING / hypothesis-source trace preflight only
```

No copies una conclusión de PREF003/PREF004 como verdad científica sin verificarla contra su fuente primaria indicada.

Usa PREF003 para localizar áreas del Word que G7-F02 deberá conservar, actualizar, reescribir o verificar.

Usa PREF004 para cerrar formalmente en G7-F01 la trazabilidad de `HG`, `HE1`, `HE3`, `HE4`.

---

## 6. Fuentes científicas mínimas que deben congelarse

### 6.1 Estado científico principal

Snapshot base:

```text
main = e93b44164a9619dad1f527a3b2d4479265858e39
```

Congela paths + blob SHA + rol de fuente, como mínimo:

### Grupo 3

```text
docs/analysis/group3/g3_analytical_contract_v0.1.md
outputs/analysis/group3/g3_analytical_contract_v0.1.json
outputs/analysis/group3/g3_metric_population_registry_v0.1.json
outputs/analysis/group3/g3_inferential_results_v0.1.json
docs/analysis/group3/g3_inferential_methods_and_checks_v0.1.md
outputs/analysis/group3/g3_hypothesis_disposition_v0.1.json
docs/analysis/group3/g3_claim_registry_v0.1.md
outputs/audits/group3_closure_v0.1.json
```

Freeze mínimo:

```text
UNIT_OF_ANALYSIS = SERIE
DEPENDENCY_GROUP = DAM / DECLARACION cuando corresponda
EMPIRICAL_SCOPE = CAPITULO_87 / OFFLINE / INTERNAL_EVALUATION
EVAL = 1056 series / 67 DAM / 42 NANDINA
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
EXP11A = JOINT_SIZE_COMPOSITION_SENSITIVITY / NONCAUSAL
EXP11B = DESCRIPTIVE / TEN_OBSERVED_SEED_PAIRS / NO_SEED_SUPERPOPULATION_INFERENCE
EXP12 = CLOSED_WITHOUT_RETRIEVAL / NOT_ESTIMABLE
P_VALUES = none
```

### Grupo 4

```text
outputs/analysis/group4/g4_result_claim_evidence_matrix_v0.1.json
docs/analysis/group4/g4_interpretation_synthesis_v0.1.md
outputs/analysis/group4/g4_limitations_registry_v0.1.json
docs/analysis/group4/g4_literature_contrast_v0.1.md
outputs/audits/group4_closure_v0.1.json
```

Estos artefactos gobiernan fuerza de claims, límites, discusión comparativa y prohibiciones de overclaiming.

### Grupo 5

```text
outputs/results/group5/g5_table_registry_v0.1.json
docs/results/group5/g5_canonical_tables_v0.1.md
docs/results/group5/g5_appendix_registry_v0.1.md
outputs/audits/group5_closure_v0.1.json
```

Las tablas G5 gobiernan cualquier cifra presentada en G7, salvo un source binding explícito más específico ya aprobado.

### Grupo 6

```text
outputs/figures/group6/g6_figure_spec_registry_v0.1.json
outputs/figures/group6/g6_figure_hash_ledger_v0.1.csv
docs/figures/group6/g6_caption_registry_v0.1.md
outputs/audits/group6_closure_v0.1.json
```

Debes observar en `main`:

```text
G6-F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G6-F02 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G6-F03 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
GROUP6 = CLOSED / APPROVED
figure_count = 3
caption_count = 3
```

---

## 7. Fuentes adicionales obligatorias para HG / HE1 / HE3 / HE4

G3 no gobierna las disposiciones terminales de HG, HE1, HE3 y HE4. Debes verificar las fuentes primarias identificadas por PREF004, incluyendo al menos:

```text
outputs/evaluation/exp04_consolidated_closure_v0.2/gate_exp04_consolidated_closure_manifest_v0.2.json
outputs/evaluation/exp04_consolidated_closure_v0.2/exp04_hypothesis_status_registry_v0.2.csv
outputs/evaluation/exp04_consolidated_closure_v0.2/summary_exp04_consolidated_closure_v0.2.md

outputs/audits/g2a_reproducibility_v0.1/gate_g2a_reproducibility_manifest_v0.1.json
outputs/audits/group2b_reproducibility_readiness_v0.2.json
outputs/audits/group2b_reproducibility_closure_v0.1.json

outputs/evaluation/historical_normative_integration_data_aduanas_clase87_v0.2/integration_ranking_invariance.json
outputs/evaluation/historical_normative_integration_data_aduanas_clase87_v0.2/integration_traceability.json
outputs/evaluation/diagnostic_llm_reranker_data_aduanas_clase87_v0.2/reranker_metrics_v0.2.json
outputs/evaluation/diagnostic_llm_reranker_data_aduanas_clase87_v0.2/summary.md

outputs/evaluation/he4_top3_explainer_data_aduanas_clase87_v0.2/he4_he4_joint_jk_assessment_v0.2.json
outputs/evaluation/he4_top3_explainer_data_aduanas_clase87_v0.2/he4_qualitative_findings_v0.2.md
```

Antes de congelar la matriz de hipótesis realiza una búsqueda final en el repositorio por una **disposición formal agregada** de `HG` y `HE1`.

Regla decisional:

### HG

Si no existe una fuente terminal explícita que declare una disposición formal agregada de HG:

```text
HG_FORMAL_DISPOSITION_FOUND = false
HG_FORMAL_DISPOSITION = NO_FORMAL_DISPOSITION_FOUND
HG_WRITING_RULE = DO_NOT_ASSERT_SUPPORTED_OR_REJECTED
HG_ALLOWED = describir por separado evidencia de componentes y límites, con sus fuentes propias
```

No derives HG combinando HE1–HE5.

### HE1

Si no existe un artefacto terminal explícito de disposición HE1:

```text
HE1_FORMAL_DISPOSITION_FOUND = false
HE1_FORMAL_DISPOSITION = NO_FORMAL_DISPOSITION_FOUND
HE1_WRITING_RULE = DO_NOT_ASSERT_SUPPORTED_OR_REJECTED
HE1_ALLOWED = describir evidencia de reproducibilidad/trazabilidad y sus limitaciones sin convertirla retrospectivamente en disposition
```

La ausencia formal registrada por Group1 debe preservarse; no transformes evidencia G2A/G2B en una decisión post hoc.

### HE3

Si las fuentes primarias permanecen iguales:

```text
HE3 = SUPPORTED
```

Preserva que el reranker LLM es diagnóstico y que la integración histórico-normativa no altera el ranking histórico salvo fuente posterior aprobada.

### HE4

Si las fuentes primarias permanecen iguales:

```text
HE4 = PARTIALLY_SUPPORTED
```

Preserva las limitaciones `PROMPT_SCHEMA_SPECIFICATION_MISMATCH` y `EVALUATOR_MODALITY_DEVIATION`; auditabilidad no equivale a corrección clasificatoria o jurídica.

Si encuentras una fuente formal posterior que contradiga cualquiera de estas cuatro reglas, no resuelvas silenciosamente: termina `BLOCKED_HYPOTHESIS_SOURCE_CONFLICT` e identifica el artefacto.

---

## 8. Onboarding obligatorio del artículo

Sobre el head real de `origin/article/main-manuscript`, lee íntegramente y en este orden:

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

Registra para cada archivo:

```text
path
blob SHA
role
```

Registra además:

```text
ARTICLE_HEAD_FROZEN = <head real observado>
ARTICLE_CURRENT_PHASE
ARTICLE_CURRENT_GATE
ARTICLE_CANONICAL_MASTER
ARTICLE_CURRENTLY_AUTHORIZED_SCOPE
ARTICLE_CURRENTLY_FORBIDDEN_SCOPE
```

No modifiques `article/main-manuscript`.

El source freeze de G7-F01 **no anula** la gobernanza editorial interna del artículo. Si `ARTICLE_STATUS.md` mantiene Results/Discussion/Conclusion no autorizados, congela esa restricción literalmente. G7-F03 deberá reconciliar el estado editorial real antes de modificar cualquier sección.

Si el head del artículo cambia después del freeze, G7-F03 deberá ejecutar un `ARTICLE_DRIFT_CHECK` contra `ARTICLE_HEAD_FROZEN`; un cambio de SHA por sí solo no implica conflicto, pero cualquier cambio científico debe reconciliarse antes de escribir.

---

## 9. Bibliografía y reglas institucionales

### 9.1 Fuente bibliográfica

Congela separadamente:

```text
THESIS_BIBLIOGRAPHY_BASELINE = bibliography/references present in current thesis baseline; NOT scientific ground truth by itself
ARTICLE_BIBLIOGRAPHIC_CONTROL = article/SOURCE_REGISTRY.md at ARTICLE_HEAD_FROZEN
SCIENTIFIC_COMPARATIVE_INTERPRETATION = docs/analysis/group4/g4_literature_contrast_v0.1.md
```

No añadas referencias nuevas en G7-F01.

### 9.2 Reglas institucionales UNMSM

Busca en fuentes versionadas del repositorio cualquier regla institucional UNMSM expresamente vigente para formato/redacción de tesis.

Si no existe una fuente versionada explícita:

```text
UNMSM_VERSIONED_INSTITUTIONAL_RULE_SOURCE_FOUND = false
INSTITUTIONAL_WRITING_RULE = PRESERVE_CURRENT_THESIS_STRUCTURE_AND_FORMAT_UNLESS_AUTHOR_OR_OFFICIAL_SOURCE_PROVIDES_OTHERWISE
DO_NOT_INVENT_INSTITUTIONAL_RULES = true
```

La ausencia de una regla versionada no bloquea el source freeze científico, pero bloquea cambios de formato que pretendan justificarse como requisito institucional nuevo.

---

## 10. Contrato de actualización de tesis para futuro G7-F02

Usa PREF003 solo como mapa de localización y verifica su clasificación contra fuentes primarias.

El source freeze debe contener una matriz completa con columnas mínimas:

```text
thesis_section_or_topic
baseline_state
writing_action
scientific_governing_source
claim_or_metric_rule
must_preserve
must_replace_or_remove
blocking_if_source_missing
```

Valores permitidos de `writing_action`:

```text
KEEP
KEEP_WITH_TERMINOLOGY_REVIEW
UPDATE_REQUIRED
REWRITE_REQUIRED
VERIFY_BEFORE_WRITING
NEW_TEXT_ALLOWED
IMMUTABLE
```

Como mínimo debe quedar explícitamente cubierto el tratamiento futuro de:

```text
problema y objetivos
hipótesis HG / HE1 / HE2 / HE3 / HE4 / HE5
variables y operacionalización
diseño y unidad de análisis
población / muestra / partición
recolección y normalización
corpus documental/normativo
recuperación histórica
recuperación normativa
integración histórico-normativa
reranker diagnóstico
explicación auditable
métricas e inferencia
HE5 y limitaciones
EXP11A
EXP11B
EXP12
resultados
contrastación de hipótesis
discusión
reproducibilidad
conclusiones
recomendaciones
figuras y tablas
```

Preserva la regla:

```text
approved problem/objective/hypothesis formulations are not silently rewritten
hypothesis dispositions/results may be updated only from their frozen governing source
```

No escribas todavía el texto final de ninguna sección.

---

## 11. Contrato de actualización del artículo para futuro G7-F03

El source freeze debe registrar por bloque editorial:

```text
article_block
current_status
future_G7_action = IMMUTABLE / VERIFY / UPDATE_IF_REQUIRED / NOT_AUTHORIZED
editorial_governing_source
scientific_governing_source
```

Reglas:

- contenido `CLOSED / APPROVED / FROZEN / INTEGRATED` no se reescribe silenciosamente;
- cualquier actualización requerida por G3–G6 debe ser explícita y trazada;
- `Results`, `Discussion`, `Conclusion`, `Abstract`, título final o claims de novelty no se habilitan por G7-F01 si la gobernanza editorial del artículo todavía los bloquea;
- el repositorio de artículo no reemplaza las fuentes científicas primarias;
- el artículo debe mantener arquitectura: historical ranking → fixed Top-3 → candidate-specific normative evidence → context → local LLM explanation;
- no convertir configurabilidad en generalización empírica.

No modifiques el artículo en esta ficha.

---

## 12. Guardrails científicos permanentes

El source freeze debe incorporar literalmente o de forma inequívocamente equivalente:

```text
HISTORICAL_RETRIEVAL_SUPERIORITY != GLOBAL_RAG_ACCURACY
NORMATIVE_EVIDENCE != BINDING_LEGAL_CORRECTNESS
AUDITABLE_EXPLANATION != CLASSIFICATION_OR_LEGAL_CORRECTNESS
CONFIGURABILITY != EMPIRICAL_GENERALIZATION
EXP11A != ISOLATED_CAUSAL_SIZE_EFFECT
EXP11B != SEED_SUPERPOPULATION_INFERENCE
ATTEMPT06 != GLOBAL_ZERO_IMPACT
EXP12 = CLOSED_WITHOUT_RETRIEVAL / NOT_ESTIMABLE / DO_NOT_REOPEN
```

No se autoriza nueva inferencia, nueva métrica, nuevo CI, p-value, experimento, retrieval ni redecisión de hipótesis.

---

## 13. Materialización del candidato G7-F01

Crea desde:

```text
BASE = e93b44164a9619dad1f527a3b2d4479265858e39
```

una rama:

```text
writing/g7-f01-source-freeze-v01
```

Crea exactamente dos paths nuevos:

```text
docs/writing/group7/g7_writing_source_freeze_v0.1.md
docs/writing/group7/g7_writing_source_freeze_v0.1.json
```

No modifiques ningún path existente en la rama candidata.

Ambos artefactos deben tener:

```text
status = CANDIDATE_PENDING_EXTERNAL_AUDIT
ficha = G7-F01
group = 7
main_source_commit = e93b44164a9619dad1f527a3b2d4479265858e39
```

El JSON debe contener como mínimo:

```text
governance_refs
thesis_baseline
article_baseline
scientific_source_registry
hypothesis_source_bindings
thesis_writing_contract
article_writing_contract
bibliographic_contract
institutional_rules_contract
permanent_guardrails
open_source_gaps
scientific_data_change_count = 0
new_inference_count = 0
new_ci_count = 0
new_p_value_count = 0
thesis_modified = false
article_modified = false
exp12_reopened = false
g7_f01_candidate_status = CANDIDATE_PENDING_EXTERNAL_AUDIT
g7_f02_authorized = false
g7_f03_authorized = false
group7_closed = false
external_audit = PENDING
```

Realiza exactamente un commit en la rama candidata.

Debe resultar:

```text
PARENT = e93b44164a9619dad1f527a3b2d4479265858e39
AHEAD_BY = 1
BEHIND_BY = 0
CHANGED_PATH_COUNT = 2
```

No integres a `main`.

---

## 14. Registro de estado de fichas

Sobre:

```text
origin/docs/fichas-grupos-3-8 = bed229d81b2ce3258e1ac3c9efc171458e2891aa
```

modifica únicamente:

```text
docs/fichas/grupos_3_8/04_REGISTRO_ESTADO_FICHAS.md
```

Registra primero la activación:

```text
FICHA = G7-F01
PREVIOUS_STATE = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
AUTHORIZATION_BASIS = STANDING_CONTINUATION_INSTRUCTION_AFTER_PROMPT111_EXTERNAL_PASS
ACTIVATION_STATE = ACTIVE / AUTHORIZED / EXECUTION_PENDING
GROUP6 = CLOSED / APPROVED
GROUP7 = IN_PROGRESS
G7_F02_AUTHORIZED = false
G7_F03_AUTHORIZED = false
```

Y después el estado postejecución:

```text
G7_F01_CANDIDATE_BRANCH = writing/g7-f01-source-freeze-v01
G7_F01_CANDIDATE_COMMIT = <commit>
G7_F01 = CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
GROUP7 = IN_PROGRESS / NOT_CLOSED
G7_F02 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
G7_F03 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
GROUP8 = NOT_STARTED / NOT_AUTHORIZED
PENDING_EXTERNAL_AUDIT = true
```

No cierres G7-F01.

---

## 15. Plan Maestro

Sobre:

```text
origin/docs/plan-maestro-temporal-2026-08-31 = cc9a47986dfbae138738ad9945f0c0b1859b9f4f
```

modifica únicamente:

```text
docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md
```

Actualiza Grupo 7 a estado de ejecución pendiente de auditoría, como mínimo:

```text
7. Redacción científica = IN_PROGRESS
G7-F01 = CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
G7-F02 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
G7-F03 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
```

Grupo 6 permanece `CLOSED / APPROVED` y Grupo 8 `PENDING / NOT_AUTHORIZED`.

Añade una entrada histórica breve de activación/ejecución G7-F01. No cambies resultados científicos.

---

## 16. Criterios de STOP / BLOCK

Termina sin candidato si ocurre cualquiera:

```text
GROUP6_NOT_CLOSED
THESIS_IDENTITY_CONFLICT
BLOCKED_ARTICLE_STATE_CONFLICT
BLOCKED_HYPOTHESIS_SOURCE_CONFLICT
MISSING_REQUIRED_G3_G6_SOURCE
GOVERNANCE_REF_DRIFT
```

No conviertas un gap documental en una conclusión científica.

La ausencia confirmada de disposición formal para HG/HE1 **no es por sí sola un bloqueo**: debe congelarse como restricción de redacción.

---

## 17. Prohibiciones

No:

- modifiques la tesis Word;
- materialices una tesis corregida;
- modifiques `article/main-manuscript`;
- redactes Results/Discussion/Conclusion del artículo;
- redactes capítulos/secciones finales de la tesis;
- cambies objetivos o formulaciones de hipótesis aprobadas;
- inventes disposición de HG o HE1;
- redecidas HE2/HE3/HE4/HE5;
- crees nueva inferencia, métricas, CI o p-values;
- ejecutes experimentos o retrieval;
- reabras EXP12;
- modifiques figuras/tablas científicas;
- actives G7-F02;
- actives G7-F03;
- actives Grupo 8;
- autoapruebes G7-F01;
- integres el candidato a `main`.

---

## 18. Respuesta oficial

Publica únicamente:

```text
codex_prompts_tmp/112_RESPUESTA_ACTIVAR_Y_EJECUTAR_G7_F01_WRITING_SOURCE_FREEZE.md
```

sobre:

```text
codex/prompts-temporary
```

Incluye como mínimo:

```text
PROMPT112_EXECUTION
WORKSPACE_CONTRACT
MAIN_BASE
GROUP6_PRECONDITION
FICHAS_BASE
PLAN_BASE
ARTICLE_HEAD_FROZEN
ARTICLE_ONBOARDING
THESIS_MANIFEST_BLOB
THESIS_CURRENT_SHA256
THESIS_BASELINE_STATUS
HG_FORMAL_DISPOSITION_FOUND
HG_FORMAL_DISPOSITION
HE1_FORMAL_DISPOSITION_FOUND
HE1_FORMAL_DISPOSITION
HE2_DISPOSITION
HE3_DISPOSITION
HE4_DISPOSITION
HE5_DISPOSITION
SCIENTIFIC_SOURCE_COUNT
ARTICLE_CONTROL_SOURCE_COUNT
THESIS_WRITING_CONTRACT_ROW_COUNT
ARTICLE_WRITING_CONTRACT_ROW_COUNT
UNMSM_VERSIONED_INSTITUTIONAL_RULE_SOURCE_FOUND
CANDIDATE_BRANCH
CANDIDATE_COMMIT
CANDIDATE_PARENT
CHANGED_PATH_COUNT
FICHAS_FINAL
PLAN_FINAL
SCIENTIFIC_DATA_CHANGE_COUNT
NEW_INFERENCE_COUNT
NEW_CI_COUNT
NEW_P_VALUE_COUNT
THESIS_MODIFIED
ARTICLE_MODIFIED
EXP12_REOPENED
G7_F01_FINAL_STATE
G7_F02_FINAL_STATE
G7_F03_FINAL_STATE
GROUP7_FINAL_STATE
GROUP8_FINAL_STATE
EXTERNAL_AUDIT
```

Terminal esperado si todo pasa:

```text
PROMPT112_EXECUTION = COMPLETE
G7_F01_FINAL_STATE = CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
G7_F02_FINAL_STATE = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
G7_F03_FINAL_STATE = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
GROUP7_FINAL_STATE = IN_PROGRESS / NOT_CLOSED
GROUP8_FINAL_STATE = NOT_STARTED / NOT_AUTHORIZED
EXTERNAL_AUDIT = PENDING
```

La siguiente acción tras esta ejecución debe ser una auditoría independiente de la **IA Experimental**.
