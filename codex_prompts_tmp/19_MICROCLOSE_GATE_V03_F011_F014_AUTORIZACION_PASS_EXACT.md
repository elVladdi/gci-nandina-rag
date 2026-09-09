# CODEX — MICROCLOSE 0B-05C v0.3 F011–F014: AUTORIZACIÓN Y PASS_EXACT

## 0. ROL Y OBJETIVO

Actúa exclusivamente como **EJECUTOR DE CORRECCIÓN DEL CANDIDATO 0B-05C v0.3** después de auditoría externa independiente del Prompt18.

NO integres a `main`.
NO autorices Attempt04.
NO crees authorization record v0.3 real.
NO ejecutes retrieval, EV03, EV04, D1a, EVAL real ni modelo.

Candidato auditado:

- rama: `codex/0b05c-corrective-numerical-gate-v03`
- head: `815309b2b4ab6df2307d534ba20ec76e8077dcff`
- parent: `60aa7dd8715962f3c3e8b617e8797532529f39ed`
- tree: `93d9024079385209f3a9306449620743fd9a947c`
- compare contra `main`: `1 ahead / 0 behind`, exactamente 13 paths.

La corrección EV04/MRR del Prompt18 se considera válida y debe preservarse. Este microclose corrige únicamente cuatro hallazgos de gobernanza/ejecución prospectiva antes de que el gate pueda aprobarse para integración.

---

# 1. PREFLIGHT GIT OBLIGATORIO

Haz fetch y verifica antes de escribir:

- `origin/main = 60aa7dd8715962f3c3e8b617e8797532529f39ed`;
- rama candidata remota = `815309b2b4ab6df2307d534ba20ec76e8077dcff`;
- parent y tree exactos indicados arriba;
- Plan Maestro = `fe847f708d4d1ded92b5a50a38d4913bb69ed311`;
- article = `254b1e6df736fa9938ac86a515d65b36f4d361c5`;
- candidate gate sigue `CANDIDATE_PENDING_EXTERNAL_AUDIT` / `NOT_AUTHORIZATION_READY`;
- cuatro ejecuciones v0.3 = `NOT_AUTHORIZED`;
- Attempt04 = `NOT_AUTHORIZED / NOT_EXECUTED`;
- authorization record v0.3 ausente;
- runtime authorization record v0.3 ausente;
- ningún root v0.3 creado.

Si algo difiere: STOP / NO MICROCLOSE.

No borres evidencia local de Attempt01/02/03.

---

# 2. HALLAZGOS EXTERNOS A CERRAR

## F011 — transición de autorización v0.3 insuficientemente ligada al baseline

En `run_0b05c_corrective_numerical_v03.preflight_authorized()` el candidato actual solo exige, entre otros, que:

- exista authorization record;
- tenga un `authorization_baseline_commit` de 40 caracteres;
- `baseline_external_audit == PASS / APPROVED_FOR_INTEGRATION`;
- el baseline sea ancestro de HEAD.

Eso NO es suficiente. No exige actualmente:

- **proper ancestor** (`baseline != HEAD`);
- schema/artifact_id exactos del authorization record;
- bindings exactos de los cuatro artefactos baseline (gate + EV03 + EV04 + D1a);
- que esos bindings correspondan realmente al commit baseline;
- una proyección inmutable que demuestre que entre baseline y autorización solo cambiaron campos de autorización permitidos.

Debes implementar una transición de autorización fail-closed equivalente en rigor a la v0.2 endurecida, adaptada a v0.3.

### Contrato mínimo obligatorio

Define explícitamente en v0.3:

`AUTHORIZATION_BASELINE_ARTIFACTS`:

- unified gate v0.3;
- EV03 spec v0.3;
- EV04 spec v0.3;
- D1a spec v0.3.

El futuro authorization record v0.3 deberá tener schema estable, por ejemplo:

```json
{
  "artifact_id": "0b05c_numerical_authorization_record_v0.3",
  "schema_version": 3,
  "authorization_baseline_commit": "<40-char SHA>",
  "baseline_external_audit": "PASS / APPROVED_FOR_INTEGRATION",
  "baseline_artifacts": {
    "unified_gate": {"path":"...","git_blob_sha1":"...","canonical_git_blob_sha256":"...","canonical_size_bytes":0},
    "ev03_spec": {"path":"...","git_blob_sha1":"...","canonical_git_blob_sha256":"...","canonical_size_bytes":0},
    "ev04_spec": {"path":"...","git_blob_sha1":"...","canonical_git_blob_sha256":"...","canonical_size_bytes":0},
    "d1a_spec": {"path":"...","git_blob_sha1":"...","canonical_git_blob_sha256":"...","canonical_size_bytes":0}
  }
}
```

No crees ese record real ahora; define y valida su contrato prospectivo.

El baseline debe ser **proper ancestor** del commit autorizado futuro.

Los bindings del record deben recalcularse con `git show <baseline>:<path>` / `git_binding(..., baseline)` y coincidir exactamente.

Implementa una proyección inmutable baseline→authorized que permita SOLO campos explícitos de autorización. Como mínimo:

### Gate permitido

- `gate_status`;
- `authorization_readiness`;
- `authorization.EV03_NUMERICAL_EXECUTION`;
- `authorization.EV04_NUMERICAL_EXECUTION`;
- `authorization.D1A_NUMERICAL_EXECUTION`;
- `authorization.UNIFIED_0B05C_NUMERICAL_EXECUTION`;
- `authorization.authorization_record_present`;
- `attempt04` si se usa para representar `AUTHORIZED / NOT_EXECUTED`.

No permitir cambios simultáneos en:

- roots;
- patches;
- MRR contract;
- retrieval/ranking semantics;
- EVAL;
- BM25;
- model policy;
- code bindings;
- pipeline steps;
- runtime ledger contract;
- scientific_state;
- corrective_retrieval_executed;
- corrective_metrics_computed;
- runtime_authorization_record_present.

### Specs permitido

Solo el estado de autorización propio de cada spec y, si existe, `attempt04`.
No debe cambiar ningún contenido científico/técnico del spec.

El loader/validator debe devolver una prueba estructurada que `preflight_authorized()` consuma, no confiar en strings sueltos.

---

## F012 — el preflight unificado no exige las autorizaciones de los specs

Actualmente `preflight_authorized()` comprueba las cuatro autorizaciones del gate, pero no exige mecánicamente que:

- EV03 spec = `AUTHORIZED`;
- EV04 spec = `AUTHORIZED`;
- D1a spec = `AUTHORIZED`.

D1a termina comprobándose tarde en su wrapper, pero EV03/EV04 pueden comenzar desde el gate aunque su spec siga `NOT_AUTHORIZED`.

Corrige esto: **antes de cualquier side effect**, `preflight_authorized()` debe cargar los tres specs y exigir el estado propio `AUTHORIZED` en los tres.

También debe exigir coherencia de `attempt04` entre gate/specs si dicho campo se usa en la transición futura.

Añade tests donde una sola autorización de spec permanezca `NOT_AUTHORIZED` y el preflight/validador falle antes de cualquier side effect.

---

## F013 — regresión de PASS_EXACT en el orquestador v0.3

La v0.2 endurecida exige explícitamente `PASS_EXACT` para `verify_ev03` y `verify_ev04`.

El v0.3 actual acepta genéricamente `PASS` o `PASS_EXACT` para cualquier paso, incluidos esos dos pasos.

Esto contradice el Prompt18: **“No debilites PASS_EXACT”**.

Restaura en `run_authorized_pipeline()` la lógica fail-closed:

- `verify_ev03` => status obligatorio `PASS_EXACT`;
- `verify_ev04` => status obligatorio `PASS_EXACT`;
- `final_state` solo puede pasar tras los 18 pasos anteriores y con `status=PASS`;
- demás pasos `PASS` o `PASS_EXACT` según corresponda;
- conserva orden exacto de 19 pasos.

Añade test donde `verify_ev04={"status":"PASS"}` y el pipeline falle.

---

## F014 — test sintético no demuestra realmente PASS_EXACT

El `test_04_synthetic_enriched_control_can_pass_exactly` actual solo llama `compare_control_reproduction()` y comprueba `status=PASS`; no demuestra el `PASS_EXACT` contractual del gate.

Amplía el test para pasar por `validate_control_exact()` (o la ruta v0.3 equivalente) con:

- ranking/case files sintéticos idénticos;
- hashes esperados calculados sobre esos archivos;
- métricas enriquecidas iguales;
- contract fields suficientes;
- resultado final `status=PASS_EXACT`.

Conserva además los tests negativos de ranking y métricas.

Añade tests específicos de F011/F012/F013.

---

# 3. PRESERVACIONES OBLIGATORIAS

No modifiques la lógica científica ya auditada del Prompt18:

- `build_ev04_enriched_metrics()` debe seguir derivando MRR de case rows observados;
- MRR@100/MRR@200 y contribution exactos;
- legacy mrr = MRR@200;
- EV03 `DROP_SINGLE_CHARACTER_TOKENS`;
- EV04 corpus/ranking/collapse/depth sin cambios;
- D906 exactamente dos códigos `87044110`, `87045110`;
- BM25 1.5/0.75;
- EVAL N=1056;
- D1a model SHA/size y 17 métricas;
- 16 roots v0.3 disjuntos de v0.2;
- no usar parciales v0.2 como inputs.

No modifiques v0.1/v0.2, failure record Attempt03, Plan, article, EXP11B ni EXP12.

---

# 4. PATHS PERMITIDOS

Modifica únicamente lo estrictamente necesario dentro de este conjunto:

- `src/experiments/prepare_0b05c_corrective_numerical_gate_v03.py`
- `src/experiments/run_0b05c_corrective_numerical_v03.py`
- `src/experiments/run_d1a_corrective_0b05c_v03.py` solo si la prueba de autorización D1a necesita endurecimiento coherente;
- `tests/test_0b05c_corrective_numerical_gate_v03.py`
- `docs/0b05c_corrective_numerical_gate_v03.md` solo para documentar el cierre F011–F014;
- los seis JSON de `outputs/audits/0b05c_corrective_numerical_gate_v0.3/` únicamente si deben regenerarse para reflejar bindings/canonical contract cambiados.

No modifiques `evaluate_normative_bm25_corrective_0b05c_v03.py` salvo que encuentres un defecto real estrictamente necesario para F011–F014; si lo haces, debes justificarlo expresamente.

---

# 5. REGENERACIÓN CONTRACTUAL

Si cambian code bindings versionados, regenera los seis artefactos v0.3 mediante el preparador canónico; no edites hashes manualmente.

El candidato debe seguir quedando:

- `CANDIDATE_PENDING_EXTERNAL_AUDIT`;
- `NOT_AUTHORIZATION_READY`;
- cuatro ejecuciones `NOT_AUTHORIZED`;
- Attempt04 `NOT_AUTHORIZED / NOT_EXECUTED`;
- authorization record v0.3 ausente;
- runtime record v0.3 ausente;
- retrieval/metrics false.

---

# 6. TESTS READ-ONLY/SINTÉTICOS

Ejecuta como mínimo:

1. suite v0.3 completa;
2. EV03 recovery suite;
3. frozen EV04 suite.

No ejecutes EVAL/retrieval/model real.

La suite v0.3 debe cubrir explícitamente:

- enriched MRR derivado de rows;
- `PASS_EXACT` real;
- `PASS` simple rechazado en verify EV03/EV04;
- proper-ancestor requerido;
- authorization record schema/artifact id;
- baseline artifact binding mismatch rechazado;
- cambio científico simultáneo a autorización rechazado;
- spec EV03 no autorizado rechazado;
- spec EV04 no autorizado rechazado;
- spec D1a no autorizado rechazado;
- candidato actual permanece no autorizado.

Los conteos son evidencia local de Codex, no CI.

---

# 7. PREFLIGHT DETACHED POST-COMMIT

Desde checkout detached limpio del nuevo candidato ejecuta únicamente el preflight cerrado/no autorizado v0.3.

Debe devolver `PASS / PREEXECUTION_CLOSED_READONLY` sin crear roots/output runtime.

No invoques `preflight_authorized()` contra un authorization record real porque no debe existir. Puedes probar sus validadores con fixtures/synthetic Git worktrees si es necesario.

---

# 8. COMMIT Y PUSH

Haz exactamente **un commit adicional** sobre `815309b2b4ab6df2307d534ba20ec76e8077dcff` en la misma rama:

`codex/0b05c-corrective-numerical-gate-v03`

Mensaje sugerido:

`fix: harden v0.3 authorization and pass-exact contracts`

No rebase, amend, squash, cherry-pick ni force-push.
No merge a main.

Reporta:

- new head;
- parent exacto `815309b2...`;
- tree;
- compare `815309b2... -> new head`;
- compare `60aa7dd... -> new head`;
- lista exacta de paths modificados por este microclose.

---

# 9. PERSISTENCIA ADMINISTRATIVA

Después del push científico, persiste únicamente:

`codex_prompts_tmp/19_RESPUESTA_MICROCLOSE_GATE_V03_F011_F014_AUTORIZACION_PASS_EXACT.md`

en `codex/prompts-temporary`, commit response-only, sin rebase/amend/force.

---

# 10. REPORTE FINAL

Usa secciones:

### A. Preflight
### B. F011 — Authorization transition
### C. F012 — Spec authorization consistency
### D. F013 — PASS_EXACT orchestration
### E. F014 — Test PASS_EXACT real
### F. Preservación científica
### G. Tests
### H. Detached preflight
### I. Diff/commit/push
### J. Persistencia administrativa
### K. Estado científico

Termina exactamente con:

`GROUP_2 = EN_CURSO`

`0B05C_ATTEMPT03 = FAIL_CLOSED / SCIENTIFIC_STATE_PRESERVED / FAILURE_RECORD_VERSIONED / INTEGRATED`

`0B05C_V03_RECOVERY_GATE = CANDIDATE_PENDING_EXTERNAL_AUDIT / CORRECTED_F011_F014`

`0B05C_V03_AUTHORIZATION_READINESS = NOT_AUTHORIZATION_READY`

`EV03_V03_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED`

`EV04_V03_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED`

`D1A_V03_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED`

`UNIFIED_0B05C_V03_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED`

`ATTEMPT04 = NOT_AUTHORIZED / NOT_EXECUTED`

`0B05C_METRIC_IMPACT = NOT_DETERMINED`

`DOWNSTREAM_REEXECUTION = NOT_YET_JUSTIFIED`

`0B05C_CLOSURE = NOT_AUTHORIZED`
