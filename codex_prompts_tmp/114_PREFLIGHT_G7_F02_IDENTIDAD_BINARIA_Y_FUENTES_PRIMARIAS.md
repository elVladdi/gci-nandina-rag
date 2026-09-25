# PROMPT114 — PREFLIGHT G7-F02: IDENTIDAD BINARIA DE TESIS Y FUENTES PRIMARIAS

## 0. Rol y objetivo

Actúa como **CODEX ejecutor técnico de preflight** del proyecto `elVladdi/gci-nandina-rag`.

Esta ejecución **NO activa ni ejecuta G7-F02**. Su único propósito es resolver, antes de autorizar cualquier edición del Word, los dos gaps técnicos que G7-F01 dejó abiertos:

```text
THESIS_BINARY_SHA_RECHECK_REQUIRED_BEFORE_G7_F02_EDIT
APPROVED_PROJECT_AND_ANNEX_BYTES_NOT_FROZEN_HERE_FOR_LITERAL_FORMULATION_OR_METHOD_EDITS
```

Debes verificar la identidad binaria exacta de la tesis vigente y establecer, sin adivinar, la identidad byte-level de las fuentes primarias aprobadas que gobernarán formulaciones literales y metodología durante G7-F02.

No redactes, no corrijas y no modifiques la tesis. No cambies `main`, fichas, Plan Maestro ni artículo.

---

## 1. Estado vinculante de entrada

La IA Experimental auditó Prompt113 y establece como estado de entrada:

```text
PROMPT113_EXTERNAL_AUDIT = PASS
MAIN = db0d0ad0d8435921a7838db6720eaea86a263763
FICHAS = 140f77a90ad79fe0c0b7c82aeab1e1b4dfc0ca49
PLAN = 60b7add68e2bb14101a6fa47c512f619516d0545
G7_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
GROUP7 = IN_PROGRESS / NOT_CLOSED
G7_F02 = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
G7_F02_AUTHORIZED = false
G7_F03 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
GROUP8 = NOT_STARTED / NOT_AUTHORIZED
```

El writing source freeze aprobado está en:

```text
docs/writing/group7/g7_writing_source_freeze_v0.1.md
docs/writing/group7/g7_writing_source_freeze_v0.1.json
```

sobre `main = db0d0ad0d8435921a7838db6720eaea86a263763`.

No cambies estos artefactos.

---

## 2. Ficha y gobernanza

Lee antes de ejecutar:

```text
docs/fichas/grupos_3_8/00_MAPA_MAESTRO_FICHAS_G3_G8.md
docs/fichas/grupos_3_8/01_GOBERNANZA_Y_ESTADOS.md
docs/fichas/grupos_3_8/02_MATRIZ_DEPENDENCIAS_Y_ENTRADAS.md
docs/fichas/grupos_3_8/04_REGISTRO_ESTADO_FICHAS.md
docs/fichas/grupos_3_8/grupo_7/G7_F02_REDACCION_TESIS.md
```

Regla vinculante:

```text
ELIGIBLE != AUTHORIZED
PREFLIGHT_PASS != G7_F02_EXECUTION
```

Aunque este preflight resulte PASS, G7-F02 debe permanecer `ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED` hasta auditoría independiente de la IA Experimental.

---

## 3. Workspace y refs

Trabaja desde el workspace canónico:

```text
C:\Users\Vladimir\OneDrive\Documentos\Maestría UNMSM\LLM_RGA_NANDINA
```

Registra:

```powershell
cd "C:\Users\Vladimir\OneDrive\Documentos\Maestría UNMSM\LLM_RGA_NANDINA"
git rev-parse --show-toplevel
git remote get-url origin
git status --porcelain
git fetch origin
git rev-parse origin/main
git rev-parse origin/docs/fichas-grupos-3-8
git rev-parse origin/docs/plan-maestro-temporal-2026-08-31
git rev-parse origin/codex/prompts-temporary
```

Debes observar exactamente:

```text
origin/main = db0d0ad0d8435921a7838db6720eaea86a263763
origin/docs/fichas-grupos-3-8 = 140f77a90ad79fe0c0b7c82aeab1e1b4dfc0ca49
origin/docs/plan-maestro-temporal-2026-08-31 = 60b7add68e2bb14101a6fa47c512f619516d0545
```

STOP por `GOVERNANCE_REF_DRIFT` si alguno cambió antes de iniciar.

Preserva sin tocar los untracked históricos conocidos.

---

## 4. Tesis vigente: recheck binario obligatorio

Fuente de identidad aprobada:

```text
preflight_tmp/THESIS_CURRENT_MASTER_MANIFEST_2026-09-22.md
manifest blob = 42b89b512b8db818238bfd0da22a7c75c207d9f1
```

Identidad esperada:

```text
ORIGINAL_UPLOADED_FILENAME = Molleapasa_gv(5).docx
CANONICAL_LIBRARY_FILENAME = Molleapasa_gv_vigente_2026-09-22.docx
EXPECTED_SHA256 = 08b48ec1687ae0a0d943724bf2d682aca02d2a9f5a124b3dc35270e041bc3aed
EXPECTED_SIZE_BYTES = 4360620
THESIS_CORRECTION_BASELINE = true
THESIS_IS_CURRENT_SCIENTIFIC_GROUND_TRUTH = false
```

### 4.1 Búsqueda local permitida

Busca de manera **read-only** únicamente dentro de:

```text
C:\Users\Vladimir\OneDrive\Documentos\Maestría UNMSM\
```

por nombres exactos o equivalentes claramente trazables:

```text
Molleapasa_gv_vigente_2026-09-22.docx
Molleapasa_gv(5).docx
```

No uses `Molleapasa_gv(4).docx` como baseline.

Si existe más de una copia candidata, calcula SHA-256 y tamaño de todas las candidatas y selecciona únicamente la que coincida exactamente con `EXPECTED_SHA256` y `EXPECTED_SIZE_BYTES`.

### 4.2 Resultado

Solo puede declararse:

```text
THESIS_BINARY_RECHECK = PASS
```

si los bytes accesibles producen exactamente:

```text
SHA256 = 08b48ec1687ae0a0d943724bf2d682aca02d2a9f5a124b3dc35270e041bc3aed
SIZE_BYTES = 4360620
```

Si el archivo no es accesible o el hash/tamaño no coincide:

```text
THESIS_BINARY_RECHECK = BLOCKED
G7_F02_ACTIVATION_RECOMMENDATION = DO_NOT_AUTHORIZE
```

y reporta la ruta exacta faltante o discrepante. No sustituyas el Word por otra versión similar.

---

## 5. Proyecto de tesis aprobado: identidad primaria

G7-F01 congeló que las formulaciones aprobadas de problema, objetivos e hipótesis no se reescriben silenciosamente y que el proyecto aprobado gobierna su literalidad.

Debes localizar read-only dentro del mismo árbol permitido una fuente inequívocamente identificada como el **proyecto de tesis aprobado**. Nombre conocido de referencia:

```text
Proyecto de tesis para maestría MOLLEAPASA GUTIERREZ VLADIMIR.pdf
```

No basta coincidencia semántica por contenido ni un nombre parecido si existen varias copias materialmente distintas.

Para cada candidato registra:

```text
absolute_path
filename
size_bytes
sha256
last_write_time
```

Si existe exactamente una identidad inequívoca, congela:

```text
APPROVED_PROJECT_BINARY_IDENTITY = PASS
APPROVED_PROJECT_PATH = <ruta>
APPROVED_PROJECT_SHA256 = <sha256>
APPROVED_PROJECT_SIZE_BYTES = <bytes>
```

Si existen múltiples binarios diferentes y no hay un binding previo versionado que permita decidir cuál es el aprobado:

```text
APPROVED_PROJECT_BINARY_IDENTITY = AMBIGUOUS
G7_F02_ACTIVATION_RECOMMENDATION = DO_NOT_AUTHORIZE
```

No elijas por fecha, tamaño o conveniencia.

---

## 6. Anexo metodológico aprobado: identidad primaria

El source freeze requiere congelar los bytes del Anexo metodológico que gobierna la arquitectura/metodología operativa.

Nombre lógico esperado:

```text
Anexo_1_NANDINA_LLM_RAG_v13.docx
```

Pueden existir copias con sufijos de descarga, por ejemplo:

```text
Anexo_1_NANDINA_LLM_RAG_v13(1).docx
Anexo_1_NANDINA_LLM_RAG_v13(2).docx
Anexo_1_NANDINA_LLM_RAG_v13(3).docx
Anexo_1_NANDINA_LLM_RAG_v13(4).docx
Anexo_1_NANDINA_LLM_RAG_v13(5).docx
```

El sufijo del nombre **no demuestra** una revisión distinta ni equivalencia binaria.

### 6.1 Procedimiento obligatorio

1. busca todas las copias `Anexo_1_NANDINA_LLM_RAG_v13*.docx` dentro del árbol permitido;
2. registra para cada una ruta, tamaño, SHA-256 y last-write-time;
3. agrupa por SHA-256;
4. busca en fuentes versionadas del repositorio cualquier binding explícito que identifique el Anexo aprobado usado por la investigación;
5. si todas las copias v13 accesibles son byte-idénticas, puede congelarse ese único SHA como identidad v13;
6. si existen dos o más hashes diferentes, **no selecciones uno por nombre, fecha o tamaño** salvo que exista un binding/versionamiento previo inequívoco o una autorización explícita del autor ya registrada.

Resultado permitido:

```text
APPROVED_ANNEX_BINARY_IDENTITY = PASS / AMBIGUOUS / NOT_FOUND
```

Si `AMBIGUOUS` o `NOT_FOUND`:

```text
G7_F02_ACTIVATION_RECOMMENDATION = DO_NOT_AUTHORIZE
```

---

## 7. Verificación de coherencia mínima de fuentes

Este preflight no reaudita científicamente proyecto ni Anexo. Sin embargo, una vez identificados los binarios, verifica de forma mínima y read-only que no sean archivos corruptos y que sean del tipo esperado:

```text
PROJECT = readable PDF
ANNEX = readable DOCX/ZIP package
THESIS = readable DOCX/ZIP package
```

No edites ni normalices internamente ninguno.

Si es técnicamente sencillo, registra además el nombre/título interno principal; esto es control de identidad, no interpretación científica.

---

## 8. Regla terminal

### PASS técnico completo

Solo si se cumplen simultáneamente:

```text
THESIS_BINARY_RECHECK = PASS
APPROVED_PROJECT_BINARY_IDENTITY = PASS
APPROVED_ANNEX_BINARY_IDENTITY = PASS
```

reporta:

```text
PREF005_RESULT = PASS_READY_FOR_EXTERNAL_AUDIT
G7_F02_ACTIVATION_RECOMMENDATION = ELIGIBLE_FOR_IA_EXPERIMENTAL_AUTHORIZATION
```

Esto **no autoriza G7-F02 por sí mismo**.

### Cualquier gap

Si falla cualquiera:

```text
PREF005_RESULT = BLOCKED_SOURCE_IDENTITY
G7_F02_ACTIVATION_RECOMMENDATION = DO_NOT_AUTHORIZE
```

Incluye exactamente qué archivo debe proporcionar/confirmar el autor y qué evidencia falta. No hagas una selección heurística.

---

## 9. Prohibiciones

No:

- actives G7-F02;
- modifiques la tesis;
- copies ni renombres archivos del autor salvo archivos temporales estrictamente necesarios para hashing, que deben eliminarse al terminar;
- modifiques `main`;
- modifiques fichas;
- modifiques Plan Maestro;
- modifiques `article/main-manuscript`;
- redactes secciones;
- redecidas hipótesis;
- recalcules resultados científicos;
- añadas métricas, CI o p-values;
- reabras EXP12;
- selecciones entre múltiples fuentes por heurística.

---

## 10. Respuesta oficial

Publica exclusivamente:

```text
preflight_prompts_tmp/PREF005_RESPUESTA_G7_F02_IDENTIDAD_BINARIA_Y_FUENTES_PRIMARIAS.md
```

sobre:

```text
codex/prompts-temporary
```

Incluye como mínimo:

```text
PROMPT114_EXECUTION
WORKSPACE_CONTRACT
MAIN_OBSERVED
FICHAS_OBSERVED
PLAN_OBSERVED
THESIS_MANIFEST_BLOB
THESIS_EXPECTED_SHA256
THESIS_EXPECTED_SIZE_BYTES
THESIS_BINARY_CANDIDATE_PATHS
THESIS_BINARY_RECHECK
THESIS_OBSERVED_SHA256
THESIS_OBSERVED_SIZE_BYTES
PROJECT_CANDIDATE_COUNT
PROJECT_CANDIDATES
APPROVED_PROJECT_BINARY_IDENTITY
APPROVED_PROJECT_PATH
APPROVED_PROJECT_SHA256
APPROVED_PROJECT_SIZE_BYTES
ANNEX_CANDIDATE_COUNT
ANNEX_DISTINCT_HASH_COUNT
ANNEX_CANDIDATES
APPROVED_ANNEX_BINARY_IDENTITY
APPROVED_ANNEX_PATH
APPROVED_ANNEX_SHA256
APPROVED_ANNEX_SIZE_BYTES
SOURCE_FILE_READABILITY_CHECK
PREF005_RESULT
G7_F02_ACTIVATION_RECOMMENDATION
G7_F02_FINAL_STATE = ELIGIBLE / NOT_AUTHORIZED / NOT_EXECUTED
THESIS_MODIFIED = false
ARTICLE_MODIFIED = false
MAIN_MODIFIED = false
FICHAS_MODIFIED = false
PLAN_MODIFIED = false
EXP12_REOPENED = false
EXTERNAL_AUDIT = PENDING
```

No publiques un candidato de tesis.
