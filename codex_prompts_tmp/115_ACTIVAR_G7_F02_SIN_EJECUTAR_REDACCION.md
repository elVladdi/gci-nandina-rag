# PROMPT115 — ACTIVAR G7-F02 SIN EJECUTAR REDACCIÓN

## 0. Rol y objetivo

Actúa como **CODEX ejecutor técnico-administrativo** del proyecto `elVladdi/gci-nandina-rag`.

La IA Experimental auditó independientemente la finalización de PREF005 y autoriza **solo la activación formal de G7-F02**. Esta ejecución NO redacta la tesis y NO genera candidato Word.

Tu tarea es exclusivamente:

1. verificar los refs de gobernanza;
2. verificar la respuesta final de PREF005 y su commit;
3. registrar formalmente que el gate de identidad binaria quedó satisfecho;
4. cambiar G7-F02 de `ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED` a `ACTIVE / AUTHORIZED / EXECUTION_PENDING`;
5. reconciliar el registro de fichas y el Plan Maestro;
6. dejar como siguiente actor sustantivo a la **IA de Redacción Científica**;
7. mantener G7-F03 y Grupo 8 sin autorización.

No modifiques `main`. No modifiques tesis, proyecto aprobado, v13, artículo ni staging.

---

## 1. Auditoría externa vinculante

La IA Experimental establece:

```text
PREF005_EXTERNAL_AUDIT = PASS
PREF005_RESULT_ACCEPTED = PASS_READY_FOR_EXTERNAL_AUDIT
SOURCE_IDENTITY_GATE = SATISFIED

THESIS_BINARY_RECHECK = PASS
THESIS_SHA256 = 08b48ec1687ae0a0d943724bf2d682aca02d2a9f5a124b3dc35270e041bc3aed
THESIS_SIZE_BYTES = 4360620

APPROVED_PROJECT_BINARY_IDENTITY = PASS / AUTHOR_CONFIRMED_EXACT_FILENAME
APPROVED_PROJECT_SHA256 = 25506900d3110902455458b2291b15d78a7a1bf26e88fa76a2283755b2753421
APPROVED_PROJECT_SIZE_BYTES = 1323188

V13_ROLE = AUTHOR_CONFIRMED_AUXILIARY_SOURCE / NOT_GENERAL_GATE
V13_SHA256 = 8f5a1ec96eec91cee6970f4ec6e1bea3970322160b8d0a759aed5a02fef25067
V13_SIZE_BYTES = 1573922

SOURCE_FILE_READABILITY_CHECK = PASS
G7_F02_ACTIVATION_AUTHORIZED = true
G7_F02_EXECUTION_BY_CODEX_AUTHORIZED = false
NEXT_SUBSTANTIVE_ACTOR = IA_DE_REDACCION_CIENTIFICA
```

Regla vinculante:

```text
THESIS + APPROVED_PROJECT = mandatory source-identity gates for G7-F02
V13 = confirmed auxiliary methodological source, not a general activation gate
```

---

## 2. Respuesta PREF005 que debes verificar

Rama:

```text
codex/prompts-temporary
```

Archivo:

```text
preflight_prompts_tmp/PREF005_RESPUESTA_G7_F02_IDENTIDAD_BINARIA_Y_FUENTES_PRIMARIAS.md
```

Commit esperado de la finalización con binarios suministrados por el autor:

```text
514924a83d6476279eaf40d126a42b6a81b037f4
```

Blob esperado del archivo:

```text
b3c8a3836dcf3bea401ea27e85c5a04568c15d89
```

Verifica que contenga, al menos:

```text
PROMPT114_EXECUTION = COMPLETED_WITH_AUTHOR_SUPPLIED_BINARIES / NO_G7_F02_EXECUTION
THESIS_BINARY_RECHECK = PASS
APPROVED_PROJECT_BINARY_IDENTITY = PASS / AUTHOR_CONFIRMED_EXACT_FILENAME
APPROVED_ANNEX_BINARY_IDENTITY = PASS / AUTHOR_CONFIRMED_AUXILIARY_SOURCE / NOT_GENERAL_GATE
SOURCE_FILE_READABILITY_CHECK = PASS / BOTH_DOCX_ZIP_CRC_OK / PDF_75_PAGES_FIRST_PAGE_TEXT_READABLE
PREF005_RESULT = PASS_READY_FOR_EXTERNAL_AUDIT
G7_F02_FINAL_STATE = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
```

STOP si no coincide.

---

## 3. Refs obligatorios de entrada

Debes observar exactamente:

```text
origin/main = db0d0ad0d8435921a7838db6720eaea86a263763
origin/docs/fichas-grupos-3-8 = 140f77a90ad79fe0c0b7c82aeab1e1b4dfc0ca49
origin/docs/plan-maestro-temporal-2026-08-31 = 60b7add68e2bb14101a6fa47c512f619516d0545
origin/codex/prompts-temporary >= 514924a83d6476279eaf40d126a42b6a81b037f4
```

Observa además, solo como control de deriva y sin modificarla:

```text
origin/article/main-manuscript = 92a46b78a0cb192dba2a5cff826990baed17db99
```

Si `main`, fichas o Plan difieren de los SHA exactos anteriores antes de iniciar, STOP por `GOVERNANCE_REF_DRIFT`.

Un avance posterior de `codex/prompts-temporary` es admisible únicamente si el archivo PREF005 en el commit `514924...` sigue siendo verificable e idéntico al blob esperado.

---

## 4. Workspace y preservación

Trabaja desde el workspace canónico:

```text
C:\Users\Vladimir\OneDrive\Documentos\Maestría UNMSM\LLM_RGA_NANDINA
```

No copies, edites, renombres ni borres los tres binarios autoritativos ni sus copias de staging. No los añadas a Git.

No cambies ningún archivo en `main`.

---

## 5. Fuente de gobernanza de G7-F02

Lee:

```text
docs/fichas/grupos_3_8/grupo_7/G7_F02_REDACCION_TESIS.md
```

La ficha exige que G7-F02 actualice la tesis usando exclusivamente claims y cifras aprobadas por G3–G6 y produzca, en su ejecución sustantiva futura:

```text
- candidato de tesis versionado
- g7_thesis_claim_traceability_v0.1.csv
```

Esta ejecución NO crea ninguno de esos outputs.

Preserva las prohibiciones científicas permanentes, incluyendo:

```text
EXP12 = CLOSED_WITHOUT_RETRIEVAL / NOT_ESTIMABLE / DO_NOT_REOPEN
EXP11A != CAUSAL_SIZE_EFFECT
EXP11B != SEED_SUPERPOPULATION_INFERENCE
HISTORICAL_RETRIEVAL_SUPERIORITY != GLOBAL_RAG_ACCURACY
NORMATIVE_EVIDENCE != BINDING_LEGAL_CORRECTNESS
AUDITABLE_EXPLANATION != CLASSIFICATION_OR_LEGAL_CORRECTNESS
```

---

## 6. Etapa A — actualizar registro de fichas

Sobre exactamente:

```text
origin/docs/fichas-grupos-3-8 = 140f77a90ad79fe0c0b7c82aeab1e1b4dfc0ca49
```

modifica exclusivamente:

```text
docs/fichas/grupos_3_8/04_REGISTRO_ESTADO_FICHAS.md
```

Añade un bloque final de activación de G7-F02 con, como mínimo:

```text
FICHA = G7-F02
PREVIOUS_STATE = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
PREF005_RESPONSE_COMMIT = 514924a83d6476279eaf40d126a42b6a81b037f4
PREF005_RESPONSE_BLOB = b3c8a3836dcf3bea401ea27e85c5a04568c15d89
PREF005_EXTERNAL_AUDIT = PASS
SOURCE_IDENTITY_GATE = SATISFIED

THESIS_SHA256 = 08b48ec1687ae0a0d943724bf2d682aca02d2a9f5a124b3dc35270e041bc3aed
THESIS_SIZE_BYTES = 4360620
APPROVED_PROJECT_SHA256 = 25506900d3110902455458b2291b15d78a7a1bf26e88fa76a2283755b2753421
APPROVED_PROJECT_SIZE_BYTES = 1323188
V13_SHA256 = 8f5a1ec96eec91cee6970f4ec6e1bea3970322160b8d0a759aed5a02fef25067
V13_ROLE = AUTHOR_CONFIRMED_AUXILIARY_SOURCE / NOT_GENERAL_GATE

ACTIVATION_AUTHORIZATION = IA_EXPERIMENTAL
ACTIVATION_STATE = ACTIVE / AUTHORIZED / EXECUTION_PENDING
NEXT_SUBSTANTIVE_ACTOR = IA_DE_REDACCION_CIENTIFICA
CODEX_REDACTION_AUTHORIZED = false

G7_F03 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
GROUP7 = IN_PROGRESS / NOT_CLOSED
GROUP8 = NOT_STARTED / NOT_AUTHORIZED
```

Registra además los SHA observados de `main`, Plan y artículo en el momento de activación.

No declares G7-F02 ejecutada ni cerrada.

---

## 7. Etapa B — actualizar Plan Maestro

Sobre exactamente:

```text
origin/docs/plan-maestro-temporal-2026-08-31 = 60b7add68e2bb14101a6fa47c512f619516d0545
```

modifica exclusivamente:

```text
docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md
```

Actualiza el estado operativo de Grupo 7 a:

```text
G7-F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G7-F02 = ACTIVE / AUTHORIZED / EXECUTION_PENDING
G7-F03 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
GROUP7 = IN_PROGRESS / NOT_CLOSED
```

Añade una entrada histórica breve indicando que PREF005 fue completado con binarios autoritativos suministrados por el autor y auditado externamente `PASS`, habilitando la activación de G7-F02.

No modifiques resultados científicos ni ningún estado de G3–G6.

---

## 8. Validación final

Debes demostrar:

```text
MAIN_MODIFIED = false
THESIS_MODIFIED = false
PROJECT_MODIFIED = false
V13_MODIFIED = false
ARTICLE_MODIFIED = false
STAGING_BINARIES_MODIFIED = false

FICHAS_CHANGED_PATH_COUNT = 1
PLAN_CHANGED_PATH_COUNT = 1

G7_F02 = ACTIVE / AUTHORIZED / EXECUTION_PENDING
G7_F02_EXECUTED = false
G7_F02_CANDIDATE_CREATED = false
G7_F02_NEXT_ACTOR = IA_DE_REDACCION_CIENTIFICA
G7_F03_AUTHORIZED = false
GROUP7_CLOSED = false
GROUP8_AUTHORIZED = false
EXP12_REOPENED = false
```

---

## 9. Prohibiciones

No:

- redactes ni edites la tesis;
- generes candidato Word;
- generes `g7_thesis_claim_traceability_v0.1.csv`;
- modifiques `main`;
- modifiques `article/main-manuscript`;
- edites los tres binarios autoritativos;
- añadas binarios a Git;
- cambies claims, cifras, hipótesis o inferencia;
- inventes disposición para HG o HE1;
- actives G7-F03;
- actives Grupo 8;
- reabras EXP12.

---

## 10. Respuesta oficial

Publica exclusivamente:

```text
codex_prompts_tmp/115_RESPUESTA_ACTIVAR_G7_F02_SIN_EJECUTAR_REDACCION.md
```

sobre:

```text
codex/prompts-temporary
```

Incluye como mínimo:

```text
PROMPT115_EXECUTION
WORKSPACE_CONTRACT
MAIN_OBSERVED
FICHAS_BASE
FICHAS_FINAL
PLAN_BASE
PLAN_FINAL
ARTICLE_HEAD_OBSERVED
PREF005_RESPONSE_COMMIT
PREF005_RESPONSE_BLOB
PREF005_EXTERNAL_AUDIT
SOURCE_IDENTITY_GATE
THESIS_SHA256
APPROVED_PROJECT_SHA256
V13_SHA256
V13_ROLE
FINAL_G7_F02_STATE
G7_F02_EXECUTED
G7_F02_CANDIDATE_CREATED
G7_F02_NEXT_ACTOR
G7_F03_FINAL_STATE
GROUP7_FINAL_STATE
GROUP8_FINAL_STATE
MAIN_MODIFIED
THESIS_MODIFIED
PROJECT_MODIFIED
V13_MODIFIED
ARTICLE_MODIFIED
STAGING_BINARIES_MODIFIED
EXP12_REOPENED
EXTERNAL_AUDIT_OF_PROMPT115 = PENDING_BY_IA_EXPERIMENTAL
```

Terminal esperado:

```text
PROMPT115_EXECUTION = COMPLETE
PREF005_EXTERNAL_AUDIT = PASS
SOURCE_IDENTITY_GATE = SATISFIED
FINAL_G7_F02_STATE = ACTIVE / AUTHORIZED / EXECUTION_PENDING
G7_F02_EXECUTED = false
G7_F02_CANDIDATE_CREATED = false
G7_F02_NEXT_ACTOR = IA_DE_REDACCION_CIENTIFICA
G7_F03_FINAL_STATE = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
GROUP7_FINAL_STATE = IN_PROGRESS / NOT_CLOSED
GROUP8_FINAL_STATE = NOT_STARTED / NOT_AUTHORIZED
EXTERNAL_AUDIT_OF_PROMPT115 = PENDING_BY_IA_EXPERIMENTAL
```
