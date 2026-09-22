# PREF002 — Corrección localizada de PREF001: identidad de tesis y trazabilidad de Prompt106

## 0. Rol

Actúa como **IA Ejecutora Independiente de Pretrabajo Metodológico**.

Esta tarea corrige exclusivamente dos hallazgos de auditoría externa sobre:

```text
preflight_prompts_tmp/PREF001_RESPUESTA_PRETRABAJO_G7_F01_FUENTES.md
commit = 90f5baef9a800ca0b44334af23a7a8caeff8fd09
```

No reejecutes PREF001 completo y no cambies sus conclusiones científicas válidas.

No eres la IA Experimental gestora. No apruebes tu propia corrección.

---

## 1. Resultado de auditoría externa que gobierna esta corrección

La auditoría independiente de la IA Experimental concluyó:

```text
PREF001_EXTERNAL_AUDIT = PASS_WITH_CORRECTION_REQUIRED
SCIENTIFIC_CORRECTION_REQUIRED = false
GOVERNANCE_SEQUENCE_CORRECTION_REQUIRED = false
LOCALIZED_DOCUMENTARY_CORRECTIONS_REQUIRED = 2
```

Los dos puntos son:

### C1 — Identidad de tesis

PREF001 declaró:

```text
THESIS_FILE_IDENTIFIED = false
THESIS_FILENAME = NOT_VERIFIED
```

pero existe en los archivos accesibles del proyecto/Library una copia:

```text
Molleapasa_gv(4).docx
```

cuyo contenido corresponde inequívocamente a la tesis NANDINA de este proyecto (incluye problema/objetivos/hipótesis HE1–HE5, metodología y Capítulo 4 de resultados/discusión).

La corrección NO autoriza inferir que esa copia sea el master vigente ni permite inventar su SHA-256.

Estado corregido mínimo:

```text
THESIS_FILE_IDENTIFIED = true
THESIS_FILENAME = Molleapasa_gv(4).docx
THESIS_MASTER_STATUS = NOT_VERIFIED
THESIS_SHA256 = NOT_VERIFIED
FORMAL_G7_F01_THESIS_FREEZE_READY = false
THESIS_FREEZE_CLASSIFICATION = BLOCKED_MISSING_MASTER_IDENTITY_AND_HASH
```

Si durante tu ejecución puedes verificar de forma primaria un master status o SHA que no estaban disponibles en PREF001, repórtalo como evidencia nueva separada; no lo infieras.

### C2 — Prompt106

PREF001 clasificó la referencia de PREG7-001 a Prompt106 como no establecida/unsupported dentro del preflight.

Sin embargo existe el artefacto versionado:

```text
codex_prompts_tmp/106_CORREGIR_G6_F02_SCOPE_CONSOLIDADO_POST_FIG007.md
commit = 9c1d17db8b0846041c67fb0e7efa265fcb716616
```

Ese prompt declara expresamente:

```text
PROMPT105 = SUPERSEDED / DO_NOT_EXECUTE
PROMPT106 = CURRENT_CORRECTIVE_SCOPE
```

y gobierna la corrección técnica localizada del candidato existente G6-F02.

Por tanto, la comparación correcta con PREG7-001 es:

```text
PREG7_001_PROMPT106_REFERENCE = SUPPORTED_BY_VERSIONED_REPOSITORY_ARTIFACT
PROMPT106_ROLE_IN_PREF001 = CONTEXTUAL_G6_F02_CORRECTIVE_STATE / NOT_A_G7_FREEZE_SOURCE
```

No conviertas Prompt106 en fuente científica de G7; únicamente corrige la afirmación de que su referencia carecía de soporte.

---

## 2. Elementos de PREF001 que deben preservarse

Salvo evidencia primaria objetiva de contradicción, conserva sin reabrir:

```text
PREF001_RESULT = READY_AS_PREFLIGHT_WITH_NONBLOCKING_GAPS
FORMAL_G7_F01_AUTHORIZED = false
G6-F02 = CANDIDATE_PENDING_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
G6-F03 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
GROUP6 = IN_PROGRESS
G7-F01 = PROSPECTIVE / NOT_AUTHORIZED
ARTICLE_DRIFT_CLASSIFICATION = EDITORIAL_SNAPSHOT_STALENESS
SCIENTIFIC_CONTRADICTION = false
BLOCKS_ARCHITECTURE_B01_NOW = false
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
```

Preserva asimismo el inventario G3–G6, la matriz G3C-001..018, guardrails y riesgos que no dependan de C1/C2.

No redecidas ciencia, métricas, CI, claims o estados de grupos.

---

## 3. Fuentes mínimas a verificar

Lee directamente:

```text
preflight_prompts_tmp/PREF001_RESPUESTA_PRETRABAJO_G7_F01_FUENTES.md@90f5baef9a800ca0b44334af23a7a8caeff8fd09
codex_prompts_tmp/106_CORREGIR_G6_F02_SCOPE_CONSOLIDADO_POST_FIG007.md@9c1d17db8b0846041c67fb0e7efa265fcb716616
```

Para la tesis, usa las superficies de archivos disponibles del proyecto/Library y verifica que `Molleapasa_gv(4).docx` existe y que su contenido corresponde a esta tesis. No necesitas leerla integralmente: basta evidencia suficiente de identidad temática/documental para `THESIS_FILE_IDENTIFIED=true`.

No uses el contenido de la tesis para ejecutar G7-F02.

---

## 4. Entregable

Crea exclusivamente:

```text
preflight_prompts_tmp/PREF002_RESPUESTA_CORRECCION_PREF001_IDENTIDAD_TESIS_Y_PROMPT106.md
```

en la rama:

```text
codex/prompts-temporary
```

La respuesta debe contener:

### A. Binding

```text
SOURCE_PREF001_COMMIT
SOURCE_PREF002_PROMPT_COMMIT
PREF001_EXTERNAL_AUDIT_RESULT
```

### B. Corrección C1

Estado original, evidencia independiente, estado corregido y efecto sobre el resultado terminal.

### C. Corrección C2

Estado original, verificación de Prompt106, clasificación corregida y efecto sobre el preflight.

### D. Estado consolidado de PREF001 tras corrección

Como mínimo:

```text
PREF001_CORRECTED_RESULT
THESIS_FILE_IDENTIFIED
THESIS_FILENAME
THESIS_MASTER_STATUS
THESIS_SHA256
FORMAL_G7_F01_THESIS_FREEZE_READY
PROMPT106_REFERENCE_SUPPORTED
PROMPT106_IS_G7_FREEZE_SOURCE
FORMAL_G7_F01_AUTHORIZED
```

### E. Controles

```text
PREF002_ONLY_LOCALIZED_CORRECTIONS
PREF002_NO_G7_ACTIVATION
PREF002_NO_PLAN_MODIFICATION
PREF002_NO_FICHAS_MODIFICATION
PREF002_NO_MAIN_MODIFICATION
PREF002_NO_ARTICLE_MODIFICATION
PREF002_NO_THESIS_MODIFICATION
PREF002_NO_SCIENTIFIC_REDECISION
PREF002_PENDING_EXTERNAL_AUDIT
```

---

## 5. Restricciones

No:

- modifiques PREF001 original;
- modifiques PREG7-001/PREG7-002/PREG8-001;
- actives G7;
- edites tesis;
- modifiques Plan, fichas, `main` o artículo;
- ejecutes Prompt106;
- apruebes G6-F02;
- uses el Word de tesis para adelantar G7-F02.

---

## 6. Resultado terminal

Uno de:

```text
CORRECTION_COMPLETE_PENDING_EXTERNAL_AUDIT
REVISION_REQUIRED
BLOCKED
```

Debe terminar con:

```text
PENDING_EXTERNAL_AUDIT_BY_IA_EXPERIMENTAL = true
```
