# CODEX — MICROCLOSE CORRECTIVO DEL GATE/RUNNER NUMÉRICO 0B-05C v0.2

## 0. ROL Y OBJETIVO

Actúa exclusivamente como **EJECUTOR DE CORRECCIONES DE PRE-EJECUCIÓN** sobre la candidatura ya publicada:

`codex/0b05c-corrective-numerical-gate-v02`

Candidato auditado:

`b0a1e61f70f42aa2048338965cc003e032d3a493`

Parent científico inmutable:

`43291c312c2934aae03f3c087dd0a1ae594341b7`

Tree auditado del candidato inicial:

`cd8247a143e8fbb033c96d358e15a408c86809d1`

La auditoría externa clasifica el candidato como:

`0B05C_NUMERICAL_GATE_V02 = PASS_WITH_FINDINGS / CORRECTION_REQUIRED`

La arquitectura científica general es válida, pero el runner/contrato todavía contiene defectos bloqueantes de autorización, control exacto, paths contractuales, ledger y resumen unificado.

Este bloque sigue siendo **PRE-EJECUCIÓN**. Está prohibido:

- autorizar EV03, EV04, D1a o unified;
- ejecutar retrieval correctivo real;
- ejecutar control EV03/EV04 sobre EVAL real;
- cargar el modelo D1a para una corrida real;
- calcular métricas correctivas;
- crear authorization record v0.2 real;
- crear runtime authorization record real;
- crear cualquiera de los 16 roots científicos futuros v0.2;
- modificar `main`, Plan Maestro, `article/main-manuscript`, EXP11B, EXP12 o cualquier artefacto v0.1;
- rebase, amend o force-push.

Trabaja sobre la **misma rama candidata** y agrega, si todo pasa, **un único commit correctivo adicional** encima de `b0a1e61...`.

---

## 1. IDENTIDADES QUE DEBES VERIFICAR ANTES DE ESCRIBIR

Debe cumplirse:

- `origin/main = 43291c312c2934aae03f3c087dd0a1ae594341b7`;
- `origin/codex/0b05c-corrective-numerical-gate-v02 = b0a1e61f70f42aa2048338965cc003e032d3a493`;
- parent de `b0a1e61...` = `43291c31...`;
- tree de `b0a1e61...` = `cd8247a143e8fbb033c96d358e15a408c86809d1`;
- Plan Maestro = `fe847f708d4d1ded92b5a50a38d4913bb69ed311`;
- article = `254b1e6df736fa9938ac86a515d65b36f4d361c5`.

Si no coincide: **STOP**.

Preferir worktree limpio separado. No tocar evidencia local de Intentos 01/02.

---

# 2. HALLAZGOS EXTERNOS OBLIGATORIOS

## F001 — AUTHORIZATION TRANSITION NOT MECHANICALLY ENFORCED / BLOCKING

### Evidencia

En `src/experiments/run_0b05c_corrective_numerical_v02.py`, `preflight_authorized()` actualmente:

1. lee únicamente el gate;
2. comprueba los cuatro strings `AUTHORIZED` del gate;
3. no exige que exista `authorization_record_path`;
4. no valida contenido/hash/procedencia de un authorization record;
5. no exige `gate_status = APPROVED / INTEGRATED`;
6. no exige un estado de readiness futuro explícito de autorización;
7. no valida que los authorization fields de `ev03_numerical_execution_spec_v0.2.json`, `ev04_numerical_execution_spec_v0.2.json` y `d1a_numerical_execution_spec_v0.2.json` también estén autorizados;
8. omite expresamente los bindings `FROZEN_FILE_IDENTITY`, incluido el modelo D1a, antes del primer side effect;
9. no congela/protege suficientemente la transición para impedir que, durante la autorización, cambien simultáneamente patches, roots, comandos, semántica, modelo, métricas o runner.

Por tanto, modificar solo los cuatro strings del gate podría superar el preflight unificado sin un authorization record auditado y permitir side effects EV03/EV04 antes de descubrir posteriormente que D1a/spec/model no están en estado válido.

### Corrección obligatoria

Diseña ahora el **contrato mecánico** de la futura autorización, sin autorizar nada.

El futuro `preflight_authorized()` debe exigir, antes del primer side effect:

- gate integrado/aprobado según el estado futuro definido;
- readiness futuro explícito, distinto del actual `NOT_AUTHORIZATION_READY`;
- cuatro autorizaciones en gate = `AUTHORIZED`;
- autorización correspondiente en EV03 spec = `AUTHORIZED`;
- autorización correspondiente en EV04 spec = `AUTHORIZED`;
- autorización D1a spec = `AUTHORIZED`;
- authorization record v0.2 presente;
- authorization record con schema/version y binding a un **baseline integrado externamente aprobado** del gate/specs;
- baseline commit debe ser ancestro apropiado de HEAD;
- hashes/blob identities de los cuatro artefactos baseline: gate + EV03 spec + EV04 spec + D1a spec;
- transición permitida limitada exclusivamente a campos de autorización/readiness/record que queden definidos;
- ningún cambio simultáneo en patches, roots, commands, ranking semantics, metric contracts, builders, evaluators, model policy, code bindings, execution order o comparison schema;
- worktree tracked limpio;
- todos los bindings Git exactos;
- todos los `FROZEN_FILE_IDENTITY` requeridos para la ejecución presentes y con size/SHA exactos **antes del primer side effect**;
- los 16 roots futuros ausentes.

El authorization record **NO se crea en este Prompt 10**. Solo congela schema, validación futura y tests sintéticos.

Añade test negativo que demuestre que cambiar únicamente los cuatro strings del gate, sin authorization record válido y sin specs autorizados, **NO permite ejecutar**.

Añade test negativo que demuestre que una mutación no autorizada del baseline contractual bloquea la transición.

`F001` solo puede cerrarse si la futura autorización queda mecánicamente vinculada y fail-closed.

---

## F002 — EV03 PASS_EXACT DECLARED BUT NOT FULLY ENFORCED / BLOCKING

### Evidencia

El `required_control` EV03 declara:

- `logical_index_identity = EXACT`;
- ranking rows = 50,327;
- cases = 1,056;
- ranking SHA-256 `d2edc692...`;
- case-summary SHA-256 `f75d7d8a...`;
- ranking bytes exact;
- case-summary bytes exact;
- metric table exact;
- full metrics exact;
- status `PASS_EXACT`.

Pero `reproduce("EV03")` llama a `compare_control_reproduction()`, que compara schemas, filas parseadas y metrics, y luego el runner transforma el resultado a:

`{**comparison, "status": "PASS_EXACT", "required_contract": required}`

sin verificar mecánicamente todos los campos adicionales del `required_control`.

### Corrección obligatoria

Antes de devolver `PASS_EXACT`, EV03 debe demostrar de forma ejecutable:

1. `LOGICAL_INDEX_IDENTITY = EXACT` contra el índice histórico congelado, reutilizando la lógica ya aprobada del recovery v0.2 o una función común inequívoca;
2. ranking row count = 50,327;
3. case-summary rows = 1,056;
4. SHA-256 de bytes del ranking reproducido = `d2edc692d54b015525e193a1c067d2828aaedf48ff40e947d690b8aebd7ca015`;
5. SHA-256 de bytes del case summary reproducido = `f75d7d8ae65dda30990b819e8f662614585563d5adeb7d54344b2ae14c3522e0`;
6. ranking schema/rows exactos;
7. case-summary schema/rows exactos;
8. metric table exacta;
9. full metrics exactas.

No basta con adjuntar `required_contract` al resultado. Cada requisito debe producir un boolean/veredicto comprobado y el status solo puede ser `PASS_EXACT` si todos pasan.

Añade tests unitarios/sintéticos que hagan fallar por separado:

- ranking byte mismatch con equivalencia lógica preservada;
- case-summary byte mismatch;
- row-count mismatch;
- logical-index mismatch;
- metrics mismatch.

No ejecutes el EVAL real en este prompt.

---

## F003 — EV04 PASS_EXACT + COMMAND/ROOT CONTRACT INCONSISTENCIES / BLOCKING

### Evidencia 1 — PASS_EXACT

EV04 `required_control` congela ranking SHA y case-summary SHA, pero el runner también convierte el PASS lógico de `compare_control_reproduction()` a `PASS_EXACT` sin comprobar esos SHA contractuales.

### Evidencia 2 — comandos inconsistentes

En `ev04_numerical_execution_spec_v0.2.json` existen discrepancias entre `commands` y los roots contractuales efectivos.

Ejemplos observados:

- command de control build usa:
  `data/processed/indexes/bm25_nandina8_hierarchical_ev04_decision885_control_v0.2/...`

  mientras `control_reproduction_index_root` es:
  `data/processed/indexes/bm25_nandina8_ev04_decision885_control_v0.2`;

- command corrected build usa corpus:
  `data/processed/corpus_nandina_hierarchical_ev04_corrective_decision906_v0.2.jsonl`

  mientras `corrective_corpus.prospective_path` y `future_roots` usan:
  `data/processed/corpus_rag_v1_index_ev04_corrective_decision906_v0.2.jsonl`;

- existen análogas divergencias en corrected index path.

La causa aparente es la transformación textual genérica `.replace("v0.1", "v0.2")`, que conserva nombres históricos v0.1 que ya no coinciden con los roots v0.2 elegidos.

### Corrección obligatoria

- EV04 debe comprobar mecánicamente sus SHA congelados antes de `PASS_EXACT`.
- `commands` debe generarse desde los roots v0.2 canónicos o corregirse explícitamente de forma que **cada path coincida exactamente** con `prospective_path`, `control_reproduction_*`, `corrected_*` y `future_roots`.
- Añade test que parse/compare todos los paths de command contra los roots contractuales; no deben existir dos nombres alternativos para un mismo output.
- No cambies la semántica jerárquica, patches, EVAL, depth ni collapse.

---

## F004 — “EXACT HASH LEDGER” OMITS FILE ROOTS / BLOCKING

### Evidencia

En el runner unificado:

```python
files = sorted(
    path
    for base in FUTURE_ROOTS
    for path in (root / base).rglob("*")
    if path.is_file() and path != ledger_path
)
```

Tres `FUTURE_ROOTS` son archivos JSONL, no directorios:

- EV03 corrected corpus;
- EV04 corrected corpus;
- D1a corrected corpus.

`Path.rglob("*")` sobre un path que ya es archivo no incorpora ese propio archivo. Por tanto, el ledger futuro puede omitir precisamente los corpora corregidos.

### Corrección obligatoria

No uses descubrimiento dinámico ambiguo como contrato “exact”. Congela un **expected runtime ledger contract** explícito que:

- incluya todos los corpora corregidos;
- incluya índices/metadata;
- incluya resultados/case summaries/metrics requeridos;
- incluya outputs D1a y sus comparaciones;
- incluya unified comparisons/summary/manifest/runtime authorization record;
- excluya únicamente el propio ledger cuando sea necesario evitar circularidad;
- falle si falta un path requerido;
- falle si aparece un output contractual inesperado que no esté permitido;
- registre path, SHA-256 y size bytes.

Añade tests que demuestren que los tres JSONL de corpus están incluidos y que eliminar uno provoca fail-closed.

---

## F005 — UNIFIED SUMMARY DOES NOT CARRY D1a METRIC COMPARISON / BLOCKING

### Evidencia

El paso `summary()` actual escribe:

- EV03 aggregate comparison;
- EV04 aggregate comparison;
- `D1a: d1a_result`.

Pero `d1a_result` es principalmente provenance de ejecución (`AUTHORIZED_EXECUTION`) y no sustituye el aggregate/case-level comparison D1a ya producido por su runner.

Así, el “unified sensitivity summary” no queda preparado para determinar objetivamente el impacto de D1a.

### Corrección obligatoria

Después de `d1a_execute`, el runner unificado debe localizar y validar los outputs contractuales D1a v0.2 ya producidos, al menos:

- aggregate comparison;
- case-level comparison;
- D1a execution manifest;
- D1a hash ledger.

El unified summary debe incorporar/referenciar con path + SHA-256 el aggregate comparison D1a y la evidencia case-level/manifest necesaria, no solo la provenance return value.

Reutiliza el patrón robusto del runner v0.1 (`_d1a_summary_reference`) adaptado a v0.2 si resulta apropiado.

Añade test que falle si el D1a aggregate comparison falta o no está incorporado al summary.

---

## F006 — TEST SUITE DOES NOT EXERCISE THE ABOVE RUNTIME CONTRACTS / BLOCKING_INTEGRATION

Los 20 tests actuales demuestran bien el estado cerrado y varias propiedades declarativas, pero no detectan F001–F005.

Amplía la suite para cubrir de manera sintética/temporal, sin EVAL real:

1. authorization record obligatorio;
2. gate + three spec authorization consistency;
3. frozen model identity validada antes de side effects futuros;
4. forbidden authorization-diff rejection;
5. EV03 full PASS_EXACT field-by-field;
6. EV04 SHA PASS_EXACT;
7. EV04 commands == canonical roots;
8. exact runtime ledger incluye file roots;
9. ledger missing/extra fail-closed;
10. unified summary incluye D1a aggregate evidence;
11. el candidato permanece sin roots reales y sin autorización.

Preserva las regresiones anteriores.

No afirmar CI si no existe CI.

---

# 3. RESTRICCIONES CIENTÍFICAS INMUTABLES

No cambies:

- política EV03 `DROP_SINGLE_CHARACTER_TOKENS`;
- `k1=1.5`, `b=0.75`;
- EVAL N=1,056;
- EV03 depth=100;
- EV04 depth=200;
- EV04 semántica jerárquica/collapse/tie behavior;
- Decision906 exactamente dos códigos `87044110`, `87045110`;
- texto `Inferior a 4,537 t`;
- D1a original model weights/config/scoring/ranking;
- `MODEL_POLICY=FREEZE_ORIGINAL_D1A_WEIGHTS`;
- `must_not_retrain=true`;
- `FULL_ATOMIC_INDEX_AND_MAPPING_REBUILD`;
- orden de 19 pasos;
- roots v0.2 aprobados, salvo corregir exclusivamente discrepancias documentales de `commands` para que apunten a esos roots;
- ningún artefacto v0.1.

No conviertas `PASS_EXACT` en una etiqueta menos estricta.

---

# 4. ARTEFACTOS A ACTUALIZAR

Modifica únicamente los paths v0.2 de la candidatura que sean necesarios, previsiblemente:

- `src/experiments/prepare_0b05c_corrective_numerical_gate_v02.py`
- `src/experiments/run_0b05c_corrective_numerical_v02.py`
- `src/experiments/run_d1a_corrective_0b05c_v02.py` solo si es necesario;
- `tests/test_0b05c_corrective_numerical_gate_v02.py`
- `docs/0B05C_CORRECTIVE_NUMERICAL_GATE_V02.md`
- los seis JSON bajo `outputs/audits/0b05c_corrective_numerical_gate_v0.2/`
- `.gitattributes` solo si aparece un nuevo path textual; no cambies reglas ajenas.

`build_bm25_corrective_0b05c_v02.py` solo si es estrictamente necesario.

No crees outputs numéricos.

---

# 5. VALIDACIÓN FINAL OBLIGATORIA

Antes del commit correctivo:

- candidato basado todavía en `b0a1e61...`;
- diff solo en paths v0.2 permitidos;
- gate/status aún `CANDIDATE_PENDING_EXTERNAL_AUDIT`;
- readiness aún `NOT_AUTHORIZATION_READY`;
- cuatro auth aún `NOT_AUTHORIZED`;
- authorization record v0.2 ausente;
- runtime authorization record ausente;
- 16 future roots reales ausentes;
- corrected metrics false;
- `0B05C_METRIC_IMPACT=NOT_DETERMINED`;
- `DOWNSTREAM_REEXECUTION=NOT_YET_JUSTIFIED`;
- `0B05C_CLOSURE=NOT_AUTHORIZED`.

Ejecuta:

- suite v0.2 ampliada;
- EV03 recovery v0.2;
- v0.1 gate regressions;
- D1a preexecution/runner regressions;
- flat/hierarchical BM25 regressions;
- suite total razonable.

Después del commit, valida desde un checkout limpio/detached del nuevo HEAD:

- `python -B -m src.experiments.run_0b05c_corrective_numerical_v02 --preflight` = PASS cerrado/read-only;
- suite v0.2 ampliada = PASS;
- ningún future root creado.

No ejecutes `--execute-authorized` contra el repo real. Su conducta futura solo se prueba con fixtures/temporales y mocks.

---

# 6. COMMIT Y PUSH CIENTÍFICO

Si todo pasa:

- un único commit adicional encima de `b0a1e61...`;
- mensaje sugerido:
  `fix: close 0b05c v0.2 numerical gate audit findings`
- push solo a:
  `codex/0b05c-corrective-numerical-gate-v02`
- no merge a main;
- no force-push.

Reporta SHA, parent, tree, compare contra main y contra `b0a1e61...`.

---

# 7. PERSISTENCIA ADMINISTRATIVA OBLIGATORIA

Al finalizar, debes persistir **exactamente tu reporte final** en:

Rama:

`codex/prompts-temporary`

Archivo nuevo obligatorio:

`codex_prompts_tmp/10_RESPUESTA_MICROCLOSE_GATE_RUNNER_0B05C_V02_F001_F006.md`

Reglas:

- no sobrescribas ni modifiques `10_MICROCLOSE_GATE_RUNNER_0B05C_V02_F001_F006.md`;
- no modifiques respuestas anteriores;
- el commit administrativo debe contener exclusivamente el archivo de respuesta anterior;
- mensaje sugerido: `docs: persist prompt 10 gate microclose report`;
- push normal, sin force;
- esta persistencia administrativa es independiente del commit científico de la rama candidata.

Si no puedes persistir la respuesta, reporta `RESPONSE_PERSISTENCE=FAIL`, pero no repitas trabajo científico ya completado.

---

# 8. REPORTE FINAL OBLIGATORIO

Responder únicamente con secciones A–N:

### A. Preflight Git
heads/tree/base/candidate exactos.

### B. F001 — authorization transition
qué se cambió, baseline bindings, authorization record schema y tests negativos.

### C. F002 — EV03 exact control
lista de checks realmente ejecutables antes de PASS_EXACT.

### D. F003 — EV04 exact control + commands
SHA checks y coherencia exacta commands/roots.

### E. F004 — exact runtime ledger
expected paths, corpora file-roots incluidos, missing/extra behavior.

### F. F005 — D1a unified summary
qué artefactos D1a se incorporan y cómo se verifican.

### G. F006 — tests
nuevos tests y cobertura.

### H. Invariantes científicos
confirmación explícita de que no cambiaron.

### I. Gate state
NOT_AUTHORIZATION_READY, cuatro NOT_AUTHORIZED, no records, no execution.

### J. Tests/regresiones
RUN/PASS/FAIL/ERROR/SKIP y postcommit clean checkout.

### K. Aislamiento
main/Plan/article/EXP11B/EXP12/v0.1 sin cambios; future roots ausentes.

### L. Commit candidato corregido
SHA, parent, tree, files, push, ahead/behind.

### M. Persistencia administrativa
response path, admin commit, único archivo, `RESPONSE_PERSISTENCE`.

### N. Estado científico
Terminar exactamente con:

`GROUP_2 = EN_CURSO`

`0B05C_NUMERICAL_GATE_V02 = CANDIDATE_PENDING_EXTERNAL_AUDIT`

`0B05C_V02_AUTHORIZATION_READINESS = NOT_AUTHORIZATION_READY`

`EV03_V02_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED`

`EV04_V02_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED`

`D1A_V02_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED`

`UNIFIED_0B05C_V02_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED`

`0B05C_METRIC_IMPACT = NOT_DETERMINED`

`DOWNSTREAM_REEXECUTION = NOT_YET_JUSTIFIED`

`0B05C_CLOSURE = NOT_AUTHORIZED`

No declares integración aprobada. La auditoría externa posterior decidirá.