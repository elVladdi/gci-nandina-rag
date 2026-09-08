# CODEX — INTEGRAR EV03 HISTORICAL RECOVERY v0.2 EN `main`

## 0. ROL Y AUTORIZACIÓN DE ESTE BLOQUE

Actúa exclusivamente como **EJECUTOR DE INTEGRACIÓN CONTROLADA**.

La auditoría externa independiente de la candidatura:

`codex/0b05c-ev03-historical-builder-recovery-v02`

HEAD candidato:

`43291c312c2934aae03f3c087dd0a1ae594341b7`

ha concluido:

`0B05C_EV03_HISTORICAL_RECOVERY_V02 = PASS / APPROVED_FOR_INTEGRATION`

Esta aprobación cubre **solo la integración del bundle de recuperación/preexecution EV03 v0.2**. No constituye autorización numérica 0B-05C, no autoriza EV03 corrected, EV04 corrected, D1a ni el runner unificado.

Base científica previa esperada:

`origin/main = 06cc75ec173eb6c4b134a45eeb88fe25999f396e`

La candidatura debe estar exactamente 2 commits por delante y 0 por detrás de esa base, con la cadena:

`06cc75ec... -> cef8d7ad58d877e933f8c86b9f721cb214d9058d -> 43291c312c2934aae03f3c087dd0a1ae594341b7`

No modifiques archivos durante esta integración. No generes un commit adicional de contenido. La integración debe ser **fast-forward exacto** de `main` al candidato aprobado.

---

## 1. PROHIBICIONES

No:

- ejecutes ninguna sensibilidad numérica 0B-05C;
- ejecutes EV03 corrected, EV04 corrected o D1a numerical;
- crees `run_0b05c_corrective_numerical_v02.py`;
- crees authorization record v0.2;
- cambies `NOT_AUTHORIZED` a `AUTHORIZED`;
- edites el gate/spec v0.2 para cambiar `CANDIDATE_PENDING_EXTERNAL_AUDIT`;
- edites el Plan Maestro;
- edites `article/main-manuscript`;
- edites EXP11B o EXP12;
- limpies, borres o sobrescribas evidencia de Intentos 01/02;
- uses merge commit, squash, rebase, cherry-pick, amend o force-push;
- borres la rama candidata después de integrar.

La aprobación externa se registrará posteriormente en la gobernanza/Plan; **no alteres retrospectivamente los artefactos candidatos para incrustar la aprobación**.

---

## 2. PREFLIGHT GIT OBLIGATORIO

Haz `git fetch origin` y verifica antes de cualquier escritura:

1. `origin/main == 06cc75ec173eb6c4b134a45eeb88fe25999f396e`.
2. `origin/codex/0b05c-ev03-historical-builder-recovery-v02 == 43291c312c2934aae03f3c087dd0a1ae594341b7`.
3. El commit `43291c...` tiene parent `cef8d7ad58d877e933f8c86b9f721cb214d9058d`.
4. `cef8d7ad...` tiene parent `06cc75ec173eb6c4b134a45eeb88fe25999f396e`.
5. Compare `06cc75ec...` vs `43291c...`: `ahead=2`, `behind=0`.
6. El tree final es `9f21cb79c37cbcdf93006503bb4f888f1acfc975`.
7. No hay operación Git en progreso.
8. El worktree usado para validación está tracked-clean.

Si cualquiera falla: **STOP**, no integres.

---

## 3. VALIDACIÓN PREINTEGRACIÓN OBLIGATORIA

Usa un checkout/worktree limpio detached del commit candidato `43291c...` y ejecuta:

```powershell
python -B -m src.experiments.verify_ev03_historical_builder_recovery_v02 --verify-committed
```

Debe devolver exit code 0 y, como mínimo:

- `status = PASS`
- `mode = COMMITTED_REPLAY_READONLY`
- `base_commit_ancestor = true`
- `tracked_worktree_clean = true`
- `canonical_dependency_bindings.status = PASS`
- `canonical_dependency_bindings.checked = 13`
- `canonical_dependency_bindings.mismatch_count = 0`
- `LOGICAL_INDEX_IDENTITY = EXACT`
- `EV03_DECISION885_CONTROL_REPRODUCTION = PASS_EXACT`
- `ranking_bytes_exact = true`
- `case_summary_bytes_exact = true`
- `full_metrics_exact = true`
- `repo_files_created = 0`
- `repo_files_modified = 0`
- `repo_files_deleted = 0`
- `audit_artifacts_modified = false`
- `future_numerical_roots_present = false`

Ejecuta además:

```powershell
python -B -m unittest tests.test_0b05c_ev03_historical_builder_recovery_v02 -v
```

Debe resultar `RUN=16 / PASS=16 / FAIL=0 / ERROR=0 / SKIP=0` en checkout limpio.

Si cualquiera falla: **STOP**, no integres.

No ejecutes suites que invoquen ejecución numérica.

---

## 4. VERIFICAR ALCANCE DEL DIFF

Antes del fast-forward, confirma que el compare completo `06cc75ec... -> 43291c...` contiene exclusivamente estos 12 paths:

1. `.gitattributes`
2. `docs/0B05C_EV03_HISTORICAL_BUILDER_RECOVERY_V02.md`
3. `outputs/audits/0b05c_ev03_historical_builder_recovery_v0.2/0b05c_corrective_numerical_gate_v0.2.json`
4. `outputs/audits/0b05c_ev03_historical_builder_recovery_v0.2/0b05c_ev03_historical_builder_recovery_hash_ledger_v0.2.json`
5. `outputs/audits/0b05c_ev03_historical_builder_recovery_v0.2/0b05c_ev03_historical_builder_recovery_manifest_v0.2.json`
6. `outputs/audits/0b05c_ev03_historical_builder_recovery_v0.2/ev03_corrective_execution_spec_v0.2.json`
7. `outputs/audits/0b05c_ev03_historical_builder_recovery_v0.2/ev03_decision885_control_reproduction_v0.2.json`
8. `outputs/audits/0b05c_ev03_historical_builder_recovery_v0.2/ev03_historical_builder_provenance_v0.2.json`
9. `outputs/audits/0b05c_ev03_historical_builder_recovery_v0.2/ev03_logical_index_identity_v0.2.json`
10. `src/experiments/build_bm25_ev03_historical_recovered_v02.py`
11. `src/experiments/verify_ev03_historical_builder_recovery_v02.py`
12. `tests/test_0b05c_ev03_historical_builder_recovery_v02.py`

No debe haber ningún path de:

- Plan Maestro;
- `article/`;
- EXP11B;
- EXP12;
- future numerical roots v0.2;
- outputs de Intentos 01/02.

Si el alcance difiere: **STOP**.

---

## 5. INTEGRACIÓN FAST-FORWARD

Solo si los bloques 2–4 pasan:

1. cambia al worktree de `main` de forma segura;
2. confirma nuevamente que está clean y que `main == origin/main == 06cc75ec...`;
3. ejecuta un **fast-forward only** de `main` a `43291c312c2934aae03f3c087dd0a1ae594341b7`;
4. confirma que no se creó merge commit;
5. confirma `HEAD == 43291c...` y tree `9f21cb79...`;
6. push normal de `main` a `origin/main`;
7. confirma remotamente `origin/main == 43291c312c2934aae03f3c087dd0a1ae594341b7`.

No hagas ninguna edición de contenido antes o después del fast-forward.

---

## 6. VALIDACIÓN POSTINTEGRACIÓN

En un checkout limpio de `origin/main` ya integrado, vuelve a ejecutar obligatoriamente:

```powershell
python -B -m src.experiments.verify_ev03_historical_builder_recovery_v02 --verify-committed
```

Y:

```powershell
python -B -m unittest tests.test_0b05c_ev03_historical_builder_recovery_v02 -v
```

Exigir los mismos resultados PASS del bloque 3.

Confirma además:

- `main == origin/main == 43291c312c2934aae03f3c087dd0a1ae594341b7`;
- tracked worktree clean;
- rama candidata remota preservada en `43291c...`;
- Plan branch sin cambios;
- article branch sin cambios;
- no existe runner numérico v0.2;
- no existe authorization record v0.2;
- no existen future numerical roots v0.2;
- no se ejecutó ninguna métrica correctiva.

Si la validación postintegración falla, **no intentes una remediación automática ni un reset destructivo**. Reporta el fallo y detente.

---

## 7. ESTADO CIENTÍFICO DESPUÉS DE INTEGRAR

La integración correcta significa solamente:

`EV03_HISTORICAL_RECOVERY_V02 = APPROVED / VERSIONED / INTEGRATED`

No significa autorización numérica.

Deben permanecer:

- `gate_scope = EV03_HISTORICAL_RECOVERY_PREEXECUTION_ONLY`
- `authorization_readiness = NOT_AUTHORIZATION_READY`
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

No actualices el Plan Maestro en este bloque. La reconciliación del Plan será una acción separada posterior a la auditoría de esta integración.

---

## 8. REPORTE FINAL OBLIGATORIO

Responde únicamente con secciones A–H:

### A. Preflight Git
- main/origin-main inicial;
- candidato remoto;
- parents/tree;
- ahead/behind;
- clean state.

### B. Validación preintegración
- committed replay completo;
- suite recovery RUN/PASS/FAIL/ERROR/SKIP.

### C. Diff scope
- lista exacta de 12 paths;
- confirmación de ausencia de paths prohibidos.

### D. Integración
- método exacto (`FAST_FORWARD_ONLY`);
- HEAD/tree final;
- ausencia de merge commit;
- push result.

### E. Validación postintegración
- replay y tests;
- clean state;
- remote main exacto.

### F. Aislamiento
- Plan/article/EXP11B/EXP12/v0.1 sin cambios;
- rama candidata preservada;
- no numerical roots/runner/auth record.

### G. Estado de integración
Debe declarar solo si todo pasó:

`EV03_HISTORICAL_RECOVERY_V02 = APPROVED / VERSIONED / INTEGRATED`

### H. Estado científico
Termina exactamente con:

`0B05C_METRIC_IMPACT = NOT_DETERMINED`

`DOWNSTREAM_REEXECUTION = NOT_YET_JUSTIFIED`

`0B05C_CLOSURE = NOT_AUTHORIZED`

`EV03_V02_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED`

`EV04_V02_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED`

`D1A_V02_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED`

`UNIFIED_0B05C_V02_NUMERICAL_EXECUTION = NOT_AUTHORIZED / NOT_EXECUTED`
