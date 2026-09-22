# PREF004 — Trazabilidad independiente de fuentes para HG, HE1, HE3 y HE4 antes de G7

## 0. Rol y naturaleza

Actúa como **IA Ejecutora Independiente de Pretrabajo Metodológico**.

Esta tarea es **no gobernante**. No activa G7-F01/G7-F02/G7-F03, no modifica tesis, artículo, Plan Maestro, fichas, `main`, datos, resultados ni hipótesis.

No eres la IA Experimental gestora. No apruebes tu propio trabajo.

Objetivo: resolver, mediante trazabilidad primaria, los cuatro vacíos `VERIFY_AGAINST_OTHER_FROZEN_SOURCE` identificados por PREF003 V02 para:

```text
HG
HE1
HE3
HE4
```

No debes redecidir ninguna hipótesis. Debes localizar qué artefacto(s) cerrados y qué estado científico vigente gobiernan cada una, o demostrar que no existe todavía un freeze formal suficiente.

---

## 1. Contexto rector

Preflight auditado previo:

```text
PREF001 + PREF002 = source-freeze preflight validado
PREF003 V02 response = preauditoría independiente de tesis, pendiente de auditoría externa de IA Experimental al inicio de esta tarea
```

Usa como referencia documental de los vacíos:

```text
preflight_prompts_tmp/PREF003_V02_RESPUESTA_PREAUDITORIA_INDEPENDIENTE_TESIS_G7_F02.md@7782041ac6749f383779aedb7303e91a87177d8a
```

No asumas que sus cuatro estados `VERIFY` son incorrectos o correctos: reconstrúyelos desde fuentes primarias.

La tesis vigente exacta está identificada por:

```text
preflight_tmp/THESIS_CURRENT_MASTER_MANIFEST_2026-09-22.md
CURRENT MANIFEST STATE = use latest branch content
THESIS_CURRENT_WORKING_MASTER = true
THESIS_CORRECTION_BASELINE = true
ORIGINAL_UPLOADED_FILENAME = Molleapasa_gv(5).docx
CANONICAL_LIBRARY_FILENAME = Molleapasa_gv_vigente_2026-09-22.docx
LIBRARY_FILE_ID = libfile_a4565dde90148191898d246f47c287e7
EXPECTED_SHA256 = 08b48ec1687ae0a0d943724bf2d682aca02d2a9f5a124b3dc35270e041bc3aed
```

No edites la tesis.

---

## 2. Secuencia formal que no puede alterarse

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

Si observas drift entre Plan y fichas, regístralo, pero no lo corrijas.

---

## 3. Formulaciones de hipótesis que deben rastrearse

Usa la tesis vigente únicamente para identificar la formulación textual actual, no como fuente de verdad del dictamen.

### HG

```text
En un piloto experimental offline aplicado, la diferenciación funcional de los componentes permitirá obtener una recomendación auditable de subpartidas NANDINA: la recuperación histórica alcanzará el mejor desempeño de ranking, la recuperación normativa aportará evidencia documental trazable y el LLM local generará explicaciones controladas sobre un Top-3 fijo sin necesidad de modificar el orden de los candidatos.
```

### HE1

```text
La estructuración y el versionamiento del banco histórico etiquetado y del corpus normativo NANDINA permitirán preservar la integridad jerárquica, la procedencia de la evidencia y la reproducibilidad de las corridas experimentales.
```

### HE3

```text
La integración del ranking histórico con evidencia normativa conservará el desempeño del ranking histórico y aumentará la trazabilidad documental; el uso diagnóstico del LLM local como reordenador no producirá una mejora consistente del orden de los candidatos.
```

### HE4

```text
El LLM local restringido a un Top-3 fijo generará salidas estructuradas que conservarán los tres candidatos y su orden, no incorporarán códigos externos y vincularán las explicaciones con evidencia histórica o normativa identificable. La calidad de esta vinculación se evaluará mediante criterios de verificabilidad, trazabilidad y concordancia entre evidencia y justificación.
```

---

## 4. Fuentes que debes revisar

### 4.1 Gobernanza central

Lee directamente:

```text
docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md
  rama: docs/plan-maestro-temporal-2026-08-31

docs/fichas/grupos_3_8/00_MAPA_MAESTRO_FICHAS_G3_G8.md
docs/fichas/grupos_3_8/02_MATRIZ_DEPENDENCIAS_Y_ENTRADAS.md
docs/fichas/grupos_3_8/04_REGISTRO_ESTADO_FICHAS.md
  rama: docs/fichas-grupos-3-8
```

### 4.2 Main y artefactos científicos cerrados

En `main` actual, localiza mediante búsqueda y lectura directa todos los artefactos que gobiernen:

```text
HE1 / reproducibilidad, integridad, procedencia
HE3 / integración histórico–normativa y reranker diagnóstico
HE4 / explicación Top-3, validación estructural, auditabilidad
HG / disposición agregada o regla de derivación de la hipótesis general
```

Debes revisar como mínimo:

- cierres y artefactos finales de Grupo 1;
- cierres y artefactos finales de Grupo 2A/2B;
- cualquier output/registry/report final de experimentos asociados a HE3 y HE4;
- decisiones/cierres de 0B-05C solo si son materialmente relevantes a HE3 y siempre usando Attempt06 actual;
- Plan Maestro para estados terminales explícitos;
- cualquier manifiesto o summary final que declare una disposición de HE1/HE3/HE4/HG.

No uses archivos `superseded` como fuente vigente salvo para demostrar supersesión.

### 4.3 Fuentes excluidas como autoridad terminal

No uses como fuente de verdad terminal:

- la tesis vigente;
- PREG7-001/PREG7-002/PREG8-001;
- artículo en redacción;
- respuestas de chats no persistidas;
- outputs marcados candidate/pending external audit;
- Prompt106 como fuente científica de hipótesis.

---

## 5. Preguntas obligatorias por hipótesis

Para cada una de HG, HE1, HE3 y HE4 responde:

1. ¿Existe una **disposición formal final** explícita (`SUPPORTED`, `INCONCLUSIVE`, etc.)?
2. Si existe, ¿en qué artefacto exacto, commit/blob/path está congelada?
3. ¿Existe evidencia experimental cerrada suficiente aunque no exista disposición formal explícita?
4. ¿Qué partes de la hipótesis están materializadas y cuáles no?
5. ¿Hay diferencias entre el estado de la tesis y el estado científico vigente?
6. ¿Puede G7-F02 conservar el dictamen actual de la tesis, debe actualizarlo, o debe mantenerlo como `VERIFY` hasta G7-F01?
7. ¿Qué fuente exacta debería congelar G7-F01 para esa hipótesis?

---

## 6. Regla de no redecisión

No conviertas evidencia parcial en un nuevo dictamen propio.

Estados permitidos para tu conclusión por hipótesis:

```text
FORMALLY_FROZEN_DISPOSITION_FOUND
EVIDENCE_FROZEN_BUT_NO_FORMAL_HYPOTHESIS_DISPOSITION_FOUND
PARTIALLY_TRACEABLE / ADDITIONAL_SOURCE_REQUIRED
NO_GOVERNING_FROZEN_SOURCE_FOUND
```

Si encuentras un dictamen formal ya cerrado, puedes reportarlo literalmente.

Si no lo encuentras, no infieras `SUPPORTED`, `REJECTED`, `PARTIAL`, etc. desde métricas o narrativa.

---

## 7. Entregable

Crea exclusivamente:

```text
preflight_prompts_tmp/PREF004_RESPUESTA_TRAZABILIDAD_FUENTES_HG_HE1_HE3_HE4_PARA_G7.md
```

en:

```text
codex/prompts-temporary
```

### A. Binding

Incluye:

```text
SOURCE_PROMPT_COMMIT
MAIN_HEAD_OBSERVED
PLAN_HEAD_OBSERVED
FICHAS_HEAD_OBSERVED
PREF003_RESPONSE_COMMIT
THESIS_MANIFEST_HEAD_OBSERVED
PREF004_IS_NON_GOVERNING = true
FORMAL_G7_AUTHORIZED = false
```

### B. Matriz de fuentes por hipótesis

Columnas mínimas:

```text
hypothesis
thesis_current_disposition
formal_frozen_disposition_found
formal_disposition_value
formal_source_path
formal_source_commit_or_blob
evidence_sources[]
evidence_scope
superseded_sources_detected[]
traceability_status
recommended_G7_F01_freeze_source
future_G7_F02_action
```

### C. Auditoría individual HG / HE1 / HE3 / HE4

Para cada una:

```text
FORMULATION_MATCH
GOVERNING_SOURCE
FORMAL_DISPOSITION_STATUS
EVIDENCE_STATUS
THESIS_STATE_ALIGNMENT
G7_F01_SOURCE_FREEZE_RECOMMENDATION
G7_F02_HANDLING_RECOMMENDATION
```

### D. Riesgos y vacíos

Lista cualquier:

- evidencia cerrada sin dictamen formal;
- dictamen en tesis sin fuente congelada;
- dependencia de un artefacto local/hash-bound;
- conflicto entre Plan y main;
- fuente superseded todavía visible en la tesis;
- estado candidate/pending que impida freeze.

### E. Impacto sobre PREF003 V02

Para los cuatro `VERIFY` de PREF003 clasifica:

```text
VERIFY_RESOLVED
VERIFY_PARTIALLY_RESOLVED
VERIFY_REMAINS_REQUIRED
```

No modifiques PREF003.

### F. Resultado terminal

Uno de:

```text
READY_AS_HYPOTHESIS_SOURCE_PREFLIGHT
READY_AS_HYPOTHESIS_SOURCE_PREFLIGHT_WITH_NONBLOCKING_GAPS
REVISION_REQUIRED
BLOCKED
```

El resultado no activa G7 ni aprueba la tesis.

---

## 8. Controles

```text
PREF004_NO_G7_ACTIVATION = true
PREF004_NO_PLAN_MODIFICATION = true
PREF004_NO_FICHAS_MODIFICATION = true
PREF004_NO_MAIN_MODIFICATION = true
PREF004_NO_ARTICLE_MODIFICATION = true
PREF004_NO_THESIS_MODIFICATION = true
PREF004_NO_NEW_METRICS = true
PREF004_NO_NEW_INFERENCE = true
PREF004_NO_HYPOTHESIS_REDECISION = true
PREF004_SUPERSEDED_SOURCES_NOT_USED_AS_CURRENT = true
PREF004_PRIMARY_SOURCE_TRACEABILITY = true
PREF004_PENDING_EXTERNAL_AUDIT = true
```

Finaliza con:

```text
PENDING_EXTERNAL_AUDIT_BY_IA_EXPERIMENTAL = true
```
