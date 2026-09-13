# PROMPT 49 — INTEGRAR RESULTADOS EXP11B Y RECONCILIAR PLAN

## Rol y objetivo

Actúa como **ejecutor técnico controlado**.

Este bloque es exclusivamente de **integración y cierre documental** posterior a la ejecución oficial EXP11B H150/H200 ya auditada externamente. NO ejecuta retrieval, NO recalcula métricas, NO crea otra autorización y NO abre EXP12.

Debes, en este orden:

1. integrar exactamente en `main` el candidato de resultados EXP11B aprobado externamente;
2. verificar de forma read-only un notice de procedencia sobre el SHA del config registrado en el run manifest;
3. reconciliar mínimamente el Plan Maestro canónico para reflejar el cierre de EXP11B y preservar las limitaciones epistemológicas/persistencia;
4. no ejecutar ni autorizar EXP12.

---

# 1. Dictamen externo que gobierna este bloque

La auditoría externa de IA Experimental de Prompt48 concluyó:

```text
PROMPT48_EXTERNAL_AUDIT = PASS / APPROVED_WITH_NONBLOCKING_LIMITATIONS

EXP11B_RETRIEVAL_AUTHORIZATION = APPROVED / INTEGRATED / CONSUMED
EXP11B_RETRIEVAL_ATTEMPT_001 = EXECUTED_ONCE / COMPLETED / APPROVED
EXP11B_RETRIEVAL_RESULTS = APPROVED_FOR_INTEGRATION

EXP11B_FULL_CANDIDATE_RANKING_ARTIFACT =
LOCAL_OFFICIAL_ARTIFACT_NOT_VERSIONED_DUE_TO_GIT_BLOB_LIMIT_GUARD /
HASH_AND_SIZE_RECORDED / NONBLOCKING_PERSISTENCE_LIMITATION

RUNTIME_EXECUTION_EVIDENCE =
CODEX_LOCAL_OFFICIAL_EXECUTION_EVIDENCE /
NOT_INDEPENDENTLY_REEXECUTED_BY_EXTERNAL_AUDITOR

EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```

Candidato de resultados aprobado:

```text
branch = codex/exp11b-retrieval-h150-h200-results-v01
commit = dfd04f0db26383624d54e52bf4fd72f06bbb869c
parent = ea4bc0bde3246b40a25453dabeef5d571cf7c021
```

`main` esperado antes de integración:

```text
ea4bc0bde3246b40a25453dabeef5d571cf7c021
```

Plan Maestro esperado antes de reconciliación:

```text
branch = docs/plan-maestro-temporal-2026-08-31
commit = 6e327d4bcde32a3804e6923015eaa505a0a53374
path = docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md
```

Article esperado e inmutable:

```text
branch = article/main-manuscript
commit = 254b1e6df736fa9938ac86a515d65b36f4d361c5
```

---

# 2. Precondiciones Git exactas

Ejecuta `git fetch` y verifica exactamente:

```text
origin/main = ea4bc0bde3246b40a25453dabeef5d571cf7c021
origin/codex/exp11b-retrieval-h150-h200-results-v01 = dfd04f0db26383624d54e52bf4fd72f06bbb869c
origin/docs/plan-maestro-temporal-2026-08-31 = 6e327d4bcde32a3804e6923015eaa505a0a53374
origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5
```

Verifica para el candidato:

```text
dfd04f0... parent = ea4bc0b...
commits_ahead_of_main = 1
commits_behind_main = 0
changed_path_count = 9
```

Los nueve paths deben ser exactamente:

```text
outputs/audits/exp11b_retrieval_execution_attempts/EXP11B_H150_H200_AUTH_001--EXP11B_H150_H200_ATTEMPT_001.json
outputs/audits/exp11b_retrieval_execution_gate_v0.1/exp11b_retrieval_official_execution_record_v0.1.json
outputs/evaluation/exp11b_historical_retrieval_h150_h200_v0.1/exp11b_retrieval_case_level_v0.1.csv
outputs/evaluation/exp11b_historical_retrieval_h150_h200_v0.1/exp11b_retrieval_condition_summary_v0.1.csv
outputs/evaluation/exp11b_historical_retrieval_h150_h200_v0.1/exp11b_retrieval_environment_v0.1.json
outputs/evaluation/exp11b_historical_retrieval_h150_h200_v0.1/exp11b_retrieval_failures_v0.1.json
outputs/evaluation/exp11b_historical_retrieval_h150_h200_v0.1/exp11b_retrieval_metrics_by_bank_v0.1.csv
outputs/evaluation/exp11b_historical_retrieval_h150_h200_v0.1/exp11b_retrieval_output_hashes_v0.1.csv
outputs/evaluation/exp11b_historical_retrieval_h150_h200_v0.1/exp11b_retrieval_run_manifest_v0.1.json
```

No debe aparecer el archivo grande local-only:

```text
outputs/evaluation/exp11b_historical_retrieval_h150_h200_v0.1/exp11b_retrieval_candidates_v0.1.csv
```

Su identidad oficial permanece únicamente como:

```text
sha256 = 1dde84b65d8fb060211120ac73a04f1d5a5f7593e6381ed601fbdfb3f4bc9024
size_bytes = 264935868
row_count = 1350992
versioning_status = LOCAL_OFFICIAL_ARTIFACT_NOT_VERSIONED_DUE_TO_GIT_BLOB_LIMIT_GUARD
```

Si cualquier ref, ancestry, path o identidad difiere: `STOP / PRECONDITION_REF_OR_RESULT_DRIFT`.

---

# 3. Fase A — integración exacta de resultados

Integra mediante **fast-forward exacto**:

```text
ea4bc0bde3246b40a25453dabeef5d571cf7c021
→
dfd04f0db26383624d54e52bf4fd72f06bbb869c
```

Usa `--ff-only`.

NO hagas merge commit, squash, cherry-pick, rebase, amend ni reconstrucción de artefactos.

Después del push exige:

```text
origin/main = dfd04f0db26383624d54e52bf4fd72f06bbb869c
```

No debe existir commit adicional en `main`.

No modifiques ninguno de los nueve artefactos ni intentes añadir/recrear el CSV local-only grande.

---

# 4. Verificación documental read-only del SHA de config registrado en run manifest

Existe una diferencia de fingerprints que debe quedar explicada, no corregida retroactivamente:

```text
authorized/canonical config SHA256 = 2b91c06762409d10478cbf112bb25486ef3ffa410e5819fb0704f61fe64aa6af
run_manifest retrieval_config_sha256 = 0decc631705ae09078bd122b271f25912659574d86166a19e0a431c94af205b9
config Git blob = 08cc58f95b2d6989bf75e64b16c0d9aa8158f642
```

Sin modificar archivos científicos y sin ejecutar retrieval:

1. obtén los bytes exactos del blob Git `08cc58f95b2d6989bf75e64b16c0d9aa8158f642`;
2. confirma que su SHA-256 es exactamente `2b91c06762409d10478cbf112bb25486ef3ffa410e5819fb0704f61fe64aa6af`;
3. construye **solo en memoria/temporal** la transformación textual LF→CRLF del blob, sin tocar el archivo versionado;
4. calcula su SHA-256;
5. si el resultado es exactamente `0decc631705ae09078bd122b271f25912659574d86166a19e0a431c94af205b9`, clasifica:

```text
EXP11B_EXECUTION_CONFIG_SHA_NOTICE = VERIFIED_EOL_ONLY_WORKTREE_VARIATION
CONFIG_SEMANTIC_DRIFT = false
```

6. confirma además que el JSON parseado desde bytes LF y desde la variante CRLF produce el mismo objeto.

Si el hash CRLF NO coincide o los objetos JSON difieren:

```text
STOP / EXP11B_CONFIG_EXECUTION_PROVENANCE_UNRESOLVED
```

No alteres resultados ni hagas rerun. La verificación es únicamente de procedencia documental.

---

# 5. Fase B — reconciliación mínima del Plan Maestro

Solo después de completar Fase A y la verificación documental anterior, trabaja sobre:

```text
origin/docs/plan-maestro-temporal-2026-08-31 = 6e327d4bcde32a3804e6923015eaa505a0a53374
```

Crea una rama prospectiva nueva desde ese commit para modificar exclusivamente:

```text
docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md
```

No reconstruyas el Plan desde cero. Conserva íntegramente la historia previa y actualiza solo el estado vigente / añade una subsección cronológica de cierre EXP11B.

El estado canónico actual debe quedar inequívocamente como mínimo:

```text
main = origin/main = dfd04f0db26383624d54e52bf4fd72f06bbb869c

PROMPT48_EXTERNAL_AUDIT = PASS / APPROVED_WITH_NONBLOCKING_LIMITATIONS
EXP11B_RETRIEVAL_AUTHORIZATION = APPROVED / INTEGRATED / CONSUMED
EXP11B_RETRIEVAL_ATTEMPT_001 = EXECUTED_ONCE / COMPLETED / APPROVED
EXP11B_RETRIEVAL_RESULTS = APPROVED / INTEGRATED
EXP11B = CLOSED / APPROVED / INTEGRATED

EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
Grupo 2B = NOT_STARTED
Grupo 3 = NOT_STARTED
```

Registra los resultados descriptivos oficiales sin interpretación causal adicional:

```text
H150 (10 bancos):
Top-1 = 0.512689393939394
Top-3 = 0.6899621212121212
Top-5 = 0.7833333333333333
Top-10 = 0.8915719696969697
Top-50 = 0.9895833333333334
MRR = 0.6332675214603809

H200 (10 bancos):
Top-1 = 0.5141098484848485
Top-3 = 0.6894886363636363
Top-5 = 0.7820075757575757
Top-10 = 0.8952651515151515
Top-50 = 0.9852272727272726
MRR = 0.6333104425906166
```

Registra explícitamente las dos limitaciones no bloqueantes:

### A. Persistencia del candidate ranking completo

```text
exp11b_retrieval_candidates_v0.1.csv
size_bytes = 264935868
sha256 = 1dde84b65d8fb060211120ac73a04f1d5a5f7593e6381ed601fbdfb3f4bc9024
status = LOCAL_OFFICIAL_ARTIFACT_NOT_VERSIONED_DUE_TO_GIT_BLOB_LIMIT_GUARD
```

Aclara que:

- no fue independientemente byte-verificado por la auditoría Git externa;
- su identidad quedó fijada por hash/tamaño en el ledger y execution record;
- los outputs primarios/versionables (metrics, case-level, summaries, manifest, environment, failure ledger, hash ledger) sí quedaron versionados;
- la limitación de persistencia NO invalida los resultados ni bloquea EXP12;
- Grupo 2B deberá conservar esta limitación en su matriz final de reproducibilidad/trazabilidad y, si corresponde, definir su mecanismo final de archivo/distribución sin modificar el resultado científico.

### B. Evidencia runtime

Aclara que:

```text
runtime_evidence_classification =
CODEX_LOCAL_OFFICIAL_EXECUTION_EVIDENCE /
NOT_INDEPENDENTLY_REEXECUTED_BY_EXTERNAL_AUDITOR
```

La auditoría externa verificó Git, artefactos versionados, contratos y consistencia matemática disponible; no reejecutó la corrida oficial ni inspeccionó directamente los bytes del CSV local-only.

### C. Notice de SHA del config

Si Fase 4 PASS, registra:

```text
canonical_git_config_sha256 = 2b91c06762409d10478cbf112bb25486ef3ffa410e5819fb0704f61fe64aa6af
run_manifest_raw_worktree_config_sha256 = 0decc631705ae09078bd122b271f25912659574d86166a19e0a431c94af205b9
EXP11B_EXECUTION_CONFIG_SHA_NOTICE = VERIFIED_EOL_ONLY_WORKTREE_VARIATION
CONFIG_SEMANTIC_DRIFT = false
```

No edites el run manifest ni la autorización histórica para “hacer coincidir” hashes.

---

# 6. Estado de EXP12

Prompt49 NO autoriza EXP12.

El Plan debe indicar únicamente:

```text
NEXT_ELIGIBLE_BLOCK = EXP12_PROSPECTIVE_PREPARATION_OR_AUTHORIZATION
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```

No cambies parámetros congelados de EXP12 y no crees outputs EXP12.

---

# 7. Restricciones

NO:

- ejecutar retrieval H150/H200 otra vez;
- ejecutar EXP12;
- crear otra autorización EXP11B;
- editar resultados EXP11B;
- recalcular métricas EXP11B;
- intentar versionar/comprimir/dividir/recrear el CSV grande local-only;
- modificar runner/config/autorización/readiness/gate;
- modificar Article;
- abrir Grupo 2B o Grupo 3;
- borrar evidencia histórica;
- reescribir estados históricos previos del Plan.

---

# 8. Candidato del Plan

El candidato de reconciliación del Plan debe:

```text
parent = 6e327d4bcde32a3804e6923015eaa505a0a53374
commits_ahead = 1
commits_behind = 0
changed_path_count = 1
```

Único path:

```text
docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md
```

Publícalo en una rama nueva claramente nombrada. NO lo integres todavía; queda pendiente de auditoría externa.

---

# 9. Persistencia administrativa

Después del trabajo:

1. vuelve a `codex/prompts-temporary`;
2. `git fetch`;
3. no hagas rebase/amend/force;
4. crea únicamente:

```text
codex_prompts_tmp/49_RESPUESTA_INTEGRAR_RESULTADOS_EXP11B_Y_RECONCILIAR_PLAN.md
```

El commit administrativo debe contener solo esa respuesta.

---

# 10. Reporte obligatorio

Reporta al menos:

```text
PROMPT49 = COMPLETED | STOP

main_initial
main_final
results_integration_mode
results_commit_integrated
results_changed_path_count

EXP11B_EXECUTION_CONFIG_SHA_NOTICE
canonical_git_config_sha256
crlf_variant_sha256
run_manifest_raw_worktree_config_sha256
config_json_semantic_identity

PLAN_CANDIDATE_BRANCH
PLAN_CANDIDATE_COMMIT
PLAN_CANDIDATE_PARENT
PLAN_CANDIDATE_CHANGED_PATH_COUNT
PLAN_CANDIDATE_INTEGRATED = false

plan_main_state_recorded
EXP11B_RETRIEVAL_AUTHORIZATION
EXP11B_RETRIEVAL_ATTEMPT_001
EXP11B_RETRIEVAL_RESULTS
EXP11B
EXP12
NEXT_ELIGIBLE_BLOCK

large_candidate_artifact_status
large_candidate_artifact_sha256
large_candidate_artifact_size_bytes
runtime_evidence_classification

article_head_initial/final
EXP12_executed = false
GROUP2B_started = false
GROUP3_started = false
```

Estado terminal máximo permitido:

```text
PROMPT49 = COMPLETED
EXP11B_RETRIEVAL_RESULTS = APPROVED / INTEGRATED
EXP11B = CLOSED / APPROVED / INTEGRATED
CANONICAL_PLAN = CANDIDATE_RECONCILED / PENDING_EXTERNAL_AUDIT
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```

No declares el Plan reconciliado como canónico hasta la auditoría externa posterior.