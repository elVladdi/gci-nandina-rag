# CODEX — PREPARAR REMEDIACIÓN PROSPECTIVA EV03 / 0B-05C v0.2

## 0. ROL Y OBJETIVO

Actúa exclusivamente como **EJECUTOR DE INGENIERÍA DE REPRODUCIBILIDAD**, no como decisor científico.

Debes preparar una **candidatura de remediación prospectiva** del gate 0B-05C después del fallo cerrado del Intento 02 y del diagnóstico read-only que identificó:

`EV03_REPRODUCTION_ROOT_CAUSE = CURRENT_BUILDER_SEMANTICS_MISMATCH`

El problema demostrado es que el índice EV03 histórico congelado fue generado con una semántica de tokenización que elimina tokens de longitud 1, mientras `src/bm25_index.py` actual conserva esos tokens. La variante `titulo + texto_index + filtro len(token)>1`, manteniendo el resto de semánticas, reprodujo lógicamente el índice histórico de forma exacta según el diagnóstico.

**NO ejecutes ninguna sensibilidad correctiva. NO ejecutes EV03 corrected, EV04 corrected ni D1a. NO autorices numéricamente nada.**

Tu entrega debe ser una rama candidata, auditable externamente, que restaure la capacidad de reproducir el control EV03 sin alterar retrospectivamente el baseline histórico.

---

## 1. ESTADO BASE Y PRESERVACIÓN

Repositorio: `elVladdi/gci-nandina-rag`.

Base científica obligatoria:

`main = origin/main = 06cc75ec173eb6c4b134a45eeb88fe25999f396e`

Tree:

`c84da63249619e94ae69fb2a6f080dd3f84cbcf4`

El worktree del Intento 02 contiene seis artefactos ignorados que son evidencia de fallo y **NO deben eliminarse, modificarse, sobrescribirse ni reutilizarse**.

No ejecutes `git clean`, no borres `outputs/evaluation/0b05c_corrective_numerical_v0.1`, no borres el índice de control fallido, no reutilices sus roots y no realices cleanup.

Si para desarrollar/testear necesitas aislamiento, usa un checkout/worktree limpio separado, sin tocar el worktree de evidencia.

Crear solo si no existe la rama candidata:

`codex/0b05c-ev03-historical-builder-recovery-v02`

desde exactamente `06cc75ec173eb6c4b134a45eeb88fe25999f396e`.

Si esa rama ya existe local o remotamente, **STOP** y reporta; no la reutilices ni fuerces.

---

## 2. HECHOS DE PROCEDENCIA QUE DEBEN QUEDAR DOCUMENTADOS

Verifica directamente en Git antes de editar y registra evidencia reproducible:

1. `src/__pycache__/bm25_index.cpython-311.pyc` aparece antes del índice histórico.
2. El índice `data/processed/indexes/bm25_nandina8.pkl` y su metadata aparecen en el commit histórico correspondiente.
3. En el commit que incorporó el índice, `src/bm25_index.py` y `notebooks/04_BM25_Indexacion_NANDINA.ipynb` todavía no estaban versionados.
4. El fuente posterior `src/bm25_index.py` conserva tokens de longitud 1.
5. La metadata histórica declara: Python 3.11.7, 7644 documentos, `avg_doc_len_tokens=5.793302059173584`, vocabulario 5646, stopwords activas y corpus SHA-256 congelado.
6. La identidad SHA-256 del índice histórico permanece `fd5eb111f95dc4de09f1a47fdb1117f455a5caeed96548a25219664a28857b6b`.
7. El diagnóstico read-only del Intento 02 no es una nueva fuente científica por sí mismo: los hechos que se congelen deben quedar respaldados por Git/versioned artifacts y/o por nuevas verificaciones deterministas incluidas en esta candidatura.

No presentes un `.py` decompilado como “fuente histórico auténtico”. Si inspeccionas/decompilas el `.pyc`, denomínalo **evidencia derivada de bytecode versionado**.

---

## 3. POLÍTICA CIENTÍFICA DE REMEDIACIÓN

La remediación seleccionada es:

**RECOVERED_HISTORICAL_EV03_SEMANTICS_WITH_EXACT_CONTROL_GATE**.

Principios obligatorios:

- Preservar el índice y resultados Decision885 originales como baseline histórico inmutable.
- No modificar `src/bm25_index.py` global.
- No cambiar la semántica de retrieval histórico general, EXP11A, EXP11B, EV04, D1a ni otros experimentos.
- Implementar la semántica recuperada **solo para EV03 dentro del corrective runner/builder v0.2**.
- La semántica recuperada debe eliminar tokens alfanuméricos de longitud 1 en la indexación EV03, manteniendo el resto de la lógica congelada.
- No asumir que EV04 usa esa semántica. EV04 debe conservar su contrato actual y seguirá sujeto a su propia reproducción de control.
- El control EV03 v0.2 debe reconstruirse desde el corpus Decision885 congelado y superar exact-match antes de que exista cualquier posibilidad de materializar el corpus corrected.
- La validación debe ser, como mínimo, exacta en ranking completo, case summary y métricas; además debe documentar identidad lógica del índice reconstruido frente al índice histórico congelado.
- No exigir igualdad de bytes pickle entre plataformas si la estructura lógica es idéntica; distinguir `PICKLE_BYTE_IDENTITY` de `LOGICAL_INDEX_IDENTITY`.

---

## 4. VERSIONADO: NO MUTAR EL GATE AUTORIZADO v0.1

El bundle `0b05c ... v0.1` ya fue autorizado y produjo dos intentos fail-closed. Debe preservarse como registro histórico.

**No edites in-place los artefactos v0.1 autorizados.**

Crea una nueva versión prospectiva **v0.2** para cualquier artefacto contractual que deba cambiar por esta remediación.

Como mínimo, versiona separadamente:

- builder/runner que cambie;
- EV03 corrective execution spec;
- unified numerical gate/bundle;
- tests contractuales;
- artifact manifest / hash ledger del gate;
- documentación de recuperación de semántica.

Los nuevos roots prospectivos v0.2 deben ser distintos de los roots v0.1 para no requerir cleanup ni overwrite. No reutilices:

`outputs/evaluation/0b05c_corrective_numerical_v0.1`

o los roots EV03 de control ya creados por Intento 02.

Usa nombres v0.2 claros y deterministas.

La candidatura v0.2 debe comenzar con:

- `EV03_NUMERICAL_EXECUTION = NOT_AUTHORIZED`
- `EV04_NUMERICAL_EXECUTION = NOT_AUTHORIZED`
- `D1A_NUMERICAL_EXECUTION = NOT_AUTHORIZED`
- `UNIFIED_0B05C_NUMERICAL_EXECUTION = NOT_AUTHORIZED`
- `corrective_retrieval_executed = false`
- `corrective_metrics_computed = false`
- `runtime_authorization_record_present = false`
- `0B05C_METRIC_IMPACT = NOT_DETERMINED`
- `DOWNSTREAM_REEXECUTION = NOT_YET_JUSTIFIED`
- `0B05C_CLOSURE = NOT_AUTHORIZED`

No heredes silenciosamente la autorización numérica v0.1.

---

## 5. IMPLEMENTACIÓN EV03 RECUPERADA

Implementa una función/build path dedicado y explícito para EV03 que:

1. consuma el corpus canónico congelado;
2. use exactamente `tipo=nandina_8`, código de 8 dígitos, `titulo + texto_index` con fallback histórico;
3. normalice como la implementación BM25 congelada;
4. tokenice con el regex histórico aplicable;
5. elimine tokens con `len(token) == 1`;
6. aplique las stopwords congeladas;
7. preserve k1=1.5 y b=0.75;
8. preserve orden de documentos y tie-breaking/ranking;
9. produzca metadatos que declaren explícitamente `EV03_RECOVERED_HISTORICAL_TOKEN_POLICY = DROP_SINGLE_CHARACTER_TOKENS`;
10. no afecte EV04.

Evita duplicación innecesaria, pero **no cambies el comportamiento global** para “arreglar” EV03.

---

## 6. EVIDENCIA DE REPRODUCCIÓN OBLIGATORIA ANTES DE FREEZE

La candidatura debe incluir una verificación determinista read-only/build-only del control Decision885 EV03, sin ejecutar el corrected arm.

Debe demostrar y registrar:

### A. Identidad lógica del índice

Comparar reconstruido vs `data/processed/indexes/bm25_nandina8.pkl`:

- k1, b;
- doc_ids y orden;
- doc_texts y orden;
- doc_lens;
- avgdl;
- vocabulario;
- IDF mapping;
- inverted index/postings.

Emitir un artefacto JSON con hashes canónicos de cada estructura y estado `LOGICAL_INDEX_IDENTITY = EXACT` solo si todas coinciden.

### B. Reproducción experimental EV03

Con el índice reconstruido Decision885, producir únicamente control artifacts en roots de **preexecution verification v0.2**, distintos de los roots de ejecución futura.

Comparar contra los outputs congelados originales:

- full effective TOP100 ranking;
- case summary de 1056 casos;
- metric table completa;
- exact denominators/numerators/values;
- hashes/row counts;
- caso testigo `DA-EVAL-V02-00001` como diagnóstico adicional, no como sustituto del full check.

Debe resultar:

`EV03_DECISION885_CONTROL_REPRODUCTION = PASS_EXACT`

Si no es exacto, **STOP**, no generes un gate v0.2 que pueda autorizar ejecución.

No ejecutes el corpus Decision906 corrected.

---

## 7. TESTS MÍNIMOS OBLIGATORIOS

Agrega tests que demuestren al menos:

1. EV03 recovered tokenizer elimina tokens de longitud 1.
2. Tokens de longitud >=2 conservan la semántica normal.
3. Stopwords, NFKD/lowercase, k1/b y orden determinista quedan congelados.
4. El global `src/bm25_index.py` permanece sin cambios.
5. EV04 no consume la política `DROP_SINGLE_CHARACTER_TOKENS`.
6. Un índice EV03 control construido con la política actual (sin filtro len1) **no** pasa el exact-match histórico.
7. Un índice EV03 control construido con la política recuperada sí alcanza `LOGICAL_INDEX_IDENTITY = EXACT`.
8. El full EV03 control reproduce ranking/case summary/metrics exactamente.
9. La reproducción exacta es precondición independiente de cualquier corrected arm.
10. El bundle v0.2 está `NOT_AUTHORIZED` y no crea runtime roots futuros.
11. Los roots v0.1 del Intento 02 no son tocados ni considerados outputs v0.2.
12. Ninguna prueba ejecuta EV03 corrected, EV04 corrected o D1a numerical.

Ejecuta las suites relevantes. Si ejecutas suite global, distingue deuda preexistente no relacionada de fallos introducidos por esta candidatura.

---

## 8. ARTEFACTO DE PROCEDENCIA / AUDITORÍA

Crea un artefacto versionado, por ejemplo bajo:

`outputs/audits/0b05c_ev03_historical_builder_recovery_v0.2/`

que registre como mínimo:

- commits históricos relevantes;
- Git blob SHA-1 y SHA-256 canónico cuando corresponda;
- identidad del `.pyc` versionado y aclaración de que es bytecode, no fuente original;
- identidad del índice histórico;
- identidad del corpus/eval/config;
- identidad del source actual divergente;
- regla recuperada `DROP_SINGLE_CHARACTER_TOKENS`;
- evidencia estructural exacta;
- resultado del full EV03 Decision885 reproduction check;
- límites epistemológicos: `AUTHENTIC_HISTORICAL_SOURCE_PY = NOT_VERSIONED_AT_INDEX_CREATION`;
- conclusión permitida: `HISTORICAL_SEMANTICS_RECOVERED_AND_EXACTLY_VALIDATED` solo si el full check pasa.

No afirmes que el código fuente histórico original fue recuperado si solo se reconstruyó su semántica.

---

## 9. PROHIBICIONES

No modificar:

- `main`;
- Plan Maestro;
- `article/main-manuscript`;
- EXP11B;
- EXP12;
- baseline Decision885 original;
- outputs originales congelados;
- artefactos locales del Intento 02;
- `.gitignore` para forzar binaries pesados;
- ACL, Defender/CFA, OneDrive.

No crear authorization record v0.2.
No cambiar `NOT_AUTHORIZED -> AUTHORIZED`.
No ejecutar `--execute-authorized`.
No ejecutar D1a corrected.
No limpiar evidencia.

---

## 10. VERSIONADO DE LA CANDIDATURA

Si y solo si:

- la implementación está completa;
- `EV03_DECISION885_CONTROL_REPRODUCTION = PASS_EXACT`;
- `LOGICAL_INDEX_IDENTITY = EXACT`;
- los tests contractuales pasan;
- no hubo corrected execution;

entonces crea **un único commit candidato** en:

`codex/0b05c-ev03-historical-builder-recovery-v02`

Publícalo únicamente en esa rama.

No hagas merge a `main`.

Para outputs ignorados/pesados que no deban versionarse, registra path, tamaño, SHA-256 y razón; el artefacto de auditoría versionado debe contener suficiente ledger para revisión externa.

---

## 11. REPORTE FINAL OBLIGATORIO

Responde exclusivamente con secciones A–L:

### A. Git/base
- repo, branch, HEAD inicial, main/origin-main, tree, estado limpio, worktree usado, preservación del Intento 02.

### B. Procedencia histórica
- commits, archivos presentes/ausentes, pyc/index/source/notebook identities, metadata histórica.

### C. Causa reproducida
- evidencia exacta de tokens len1, current-vs-recovered semantics.

### D. Implementación v0.2
- archivos modificados/creados y justificación de cada uno.

### E. Aislamiento
- prueba de que `src/bm25_index.py`, EV04, EXP11B, EXP12 y outputs v0.1 no fueron modificados.

### F. Logical index identity
- todos los hashes/contadores y `EXACT`/`FAIL`.

### G. EV03 Decision885 full control reproduction
- ranking rows/hash/exact, case rows/hash/exact, metrics exact, caso testigo.

### H. Gate v0.2
- paths, specs, roots futuros, los cuatro estados `NOT_AUTHORIZED`, flags false.

### I. Tests
- comandos, RUN/PASS/FAIL/ERROR/SKIP; distinguir deuda preexistente.

### J. Provenance/ledger
- cada artefacto con path, tamaño, SHA-256, Git blob SHA-1 si versionado; distinguir SHA-1 de SHA-256.

### K. Candidate commit
- branch, commit SHA, parent, tree, message, files, ahead/behind, push status.

### L. Estado científico
Debe terminar exactamente manteniendo:

`0B05C_METRIC_IMPACT = NOT_DETERMINED`

`DOWNSTREAM_REEXECUTION = NOT_YET_JUSTIFIED`

`0B05C_CLOSURE = NOT_AUTHORIZED`

`EV03_V02_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED`

`EV04_V02_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED`

`D1A_V02_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED`

`UNIFIED_0B05C_V02_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED`

Después, **STOP**.