# PROMPT 42 — INTEGRAR REPLAY APROBADO Y CONSTRUIR CIERRE FORMAL DE DEUDA DE PORTABILIDAD EXP11B

## Rol y objetivo

Actúa como **ejecutor técnico controlado**. La IA Experimental realizó la auditoría externa de Prompt41 y aprobó la prueba de replay determinista para integración, con una calificación epistemológica explícita sobre la evidencia runtime local.

Este bloque tiene exactamente dos objetivos:

1. integrar por fast-forward el candidato de prueba de replay ya auditado externamente;
2. construir, pero **NO integrar todavía**, un registro formal mínimo de cierre de `EXP11B_PORTABILITY_DEBT`, para una auditoría Git externa posterior.

Este bloque **NO autoriza ni ejecuta EXP11B Retrieval H150/H200**, NO calcula métricas, NO modifica EXP12, NO modifica Article y NO actualiza todavía el Plan Maestro a deuda cerrada.

No integres el candidato rechazado de Prompt40.

---

# 1. Dictamen externo que gobierna este bloque

La IA Experimental establece:

```text
PROMPT41_EXTERNAL_AUDIT = PASS / APPROVED_FOR_INTEGRATION
EXP11B_PORTABILITY_REPLAY_PROOF = APPROVED_FOR_INTEGRATION
RUNTIME_REPLAY_AND_OFFICIAL_OBSERVATION = CODEX_LOCAL_RUNTIME_EVIDENCE / NOT_INDEPENDENTLY_REEXECUTED_BY_EXTERNAL_AUDITOR
PROCESS_RETURN_CODE_2 = NONBLOCKING_FOR_GOVERNED_BANK_IDENTITY
EXP11B_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```

La aprobación se limita a la deuda de portabilidad de los bancos EXP11B.

La razón para aceptar el `process_return_code = 2` de Prompt41 como no bloqueante es contractual y debe preservarse exactamente:

- el materializador produjo los 20 CSV antes de la comparación exacta adicional del manifest;
- los **14 campos que gobiernan la identidad de banco para EXP11B Retrieval** coinciden exactamente;
- `bank_csv_sha256` y `size_bytes` forman parte de esos 14 campos;
- las tres comparaciones reportadas fueron 20/20, 0 mismatches;
- el fallo terminal ocurrió en `total_bank_descriptor`, que no pertenece al contrato de 14 campos requerido por el retrieval gate;
- el materializador histórico valida esos descriptores con tolerancia `1e-12` antes de escribir/auditar los bancos;
- el máximo delta diagnosticado fue `5.329070518200751e-15`, dentro de dicha tolerancia;
- el código posterior `compare_manifest_identities()` usa igualdad Python exacta también para los descriptores y por eso puede terminar con código 2 aun después de producir bancos byte-idénticos bajo el contrato gobernante.

No conviertas esta decisión en una afirmación de que la IA Experimental reejecutó el replay. La observación de los bancos oficiales locales y la ejecución runtime permanecen clasificadas como evidencia CODEX-local versionada y coherente con los contratos Git auditados.

---

# 2. Refs obligatorias de entrada

Repositorio:

`elVladdi/gci-nandina-rag`

Haz `git fetch --all --prune` y verifica exactamente:

## 2.1 Main

`origin/main = 6846537602539506c8e90426daad05252cc982b9`

## 2.2 Candidato Prompt41 aprobado

Rama:

`codex/exp11b-portability-replay-proof-v01`

Commit:

`7d7267f8224e56ea5e945625a7e3955ddc15eadb`

Parent directo:

`6846537602539506c8e90426daad05252cc982b9`

Tree:

`5ead782eeb0d25a9ef1965f43de7036eedf0a0eb`

Único path añadido:

`outputs/audits/exp11b_retrieval_execution_gate_v0.1/exp11b_portability_replay_proof_v0.1.json`

Blob Git esperado:

`ab3ed6aadaaebbfc3d23c725d3ad53e9518b1ead`

El compare `684653... -> 7d7267f...` debe ser exactamente:

- 1 commit ahead;
- 0 behind;
- 1 changed path;
- solo el JSON anterior.

## 2.3 Otras refs protegidas

Plan Maestro:

`docs/plan-maestro-temporal-2026-08-31 = b814a8c2f976185209153e97e0d6ece0510526fb`

Article:

`article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5`

Respuesta administrativa Prompt41 existente:

`codex_prompts_tmp/41_RESPUESTA_AUDITAR_PORTABILIDAD_EXP11B_REPLAY_DETERMINISTA.md`

commit administrativo de creación de esa respuesta:

`2e2172a57a0db6560e6910477a97751eba52e269`

Si cualquiera de las refs científicas/protegidas o identidades del candidato difiere: `STOP / PRECONDITION_DRIFT`.

---

# 3. Verificación read-only del candidato Prompt41

Antes de integrar verifica que el artefacto aprobado conserve como mínimo:

```text
artifact_id = exp11b_portability_replay_proof_v0.1
status = CANDIDATE_PORTABILITY_REPLAY_VERIFIED_PENDING_EXTERNAL_AUDIT
main_baseline_commit = 6846537602539506c8e90426daad05252cc982b9
external_audit_origin = PROMPT40_REJECTED
```

Debe preservar:

- H100 hash match;
- EVAL hash match;
- input mismatch count = 0;
- materializer Git blob `ba64a85b4bb8bfa9f163a4f1115440486b7d8d2c`;
- config Git blob `cda209dc1ab8d6f623c6bb1c2b818c48e09d1bf8`;
- config provenance = `SAME_GIT_BLOB_EQUIVALENT_JSON_LF_VS_CRLF_CHECKOUT_REPRESENTATION`;
- 10 H150 + 10 H200;
- las 10 seeds congeladas;
- `process_return_code = 2` preservado, no ocultado;
- diagnóstico del descriptor float preservado;
- `governed_14_field_identity_status = PASS_EXACT`;
- `csv_byte_identity_status = PASS_EXACT`;
- frozen↔official = 20/20;
- frozen↔replay = 20/20;
- official↔replay = 20/20;
- `official_bank_write_count = 0`;
- `official_bank_content_mutated = false`;
- `temporary_replay_cleanup = PASS`;
- `retrieval_executed = false`;
- `evaluation_metrics_computed = false`;
- `exp11b_retrieval_authorized = false`;
- `exp12_authorized = false`.

No edites ni regeneres el artefacto.

---

# 4. FASE A — Integración exacta de la prueba de replay

Si el preflight pasa, integra únicamente mediante **fast-forward**:

`6846537602539506c8e90426daad05252cc982b9`

→

`7d7267f8224e56ea5e945625a7e3955ddc15eadb`

Reglas absolutas:

- no merge commit;
- no squash;
- no cherry-pick;
- no rebase;
- no amend;
- no force-push;
- no edición durante la integración;
- no commit adicional en esta fase.

Después del push verifica:

- `origin/main = 7d7267f8224e56ea5e945625a7e3955ddc15eadb`;
- tree = `5ead782eeb0d25a9ef1965f43de7036eedf0a0eb`;
- diff candidato vs `origin/main` vacío;
- Plan y Article intactos;
- ningún retrieval ni métrica ejecutados.

Si la integración no es exactamente fast-forward bit a bit: STOP y no construyas el cierre.

---

# 5. FASE B — Construir registro formal de cierre de deuda

Solo si FASE A pasa, crea desde el nuevo main exacto:

`codex/exp11b-portability-debt-external-closure-v01`

Parent científico obligatorio:

`7d7267f8224e56ea5e945625a7e3955ddc15eadb`

Añade **exactamente un único path nuevo**:

`outputs/audits/exp11b_retrieval_execution_gate_v0.1/exp11b_portability_debt_external_closure_v0.1.json`

No modifiques ningún archivo existente.

En particular NO modifiques todavía:

- `src/configs/exp11b_retrieval_execution_gate_v0.1.json`;
- `exp11b_retrieval_execution_gate_manifest_v0.1.json`;
- `exp11b_retrieval_execution_input_inventory_v0.1.json`;
- manifest/ledger de materialización;
- proof Prompt41;
- Plan Maestro;
- Article.

Los notices históricos permanecen inmutables; el nuevo closure record registra su resolución prospectiva.

## 5.1 Contenido mínimo obligatorio

El JSON debe contener como mínimo:

```text
artifact_id = exp11b_portability_debt_external_closure_v0.1
schema_version = 1
baseline_commit = 7d7267f8224e56ea5e945625a7e3955ddc15eadb
status = CANDIDATE_CLOSURE_RECORD / EXTERNAL_DECISION_ALREADY_PASS / PENDING_GIT_AUDIT_AND_INTEGRATION
external_audit_verdict = PASS / APPROVED_FOR_PORTABILITY_DEBT_CLOSURE
prompt40_candidate_status = REJECTED_BY_EXTERNAL_AUDIT / NOT_INTEGRATED
prompt41_replay_proof_status = APPROVED_BY_EXTERNAL_AUDIT / INTEGRATED
EXP11B_PORTABILITY_DEBT = CLOSED_BY_EXTERNAL_AUDIT / NOT_YET_INTEGRATED_AS_CLOSURE_RECORD
EXP11B_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```

Incluye bindings exactos de:

- proof Prompt41 path + Git blob `ab3ed6aadaaebbfc3d23c725d3ad53e9518b1ead`;
- materializer path + blob `ba64a85b4bb8bfa9f163a4f1115440486b7d8d2c`;
- materialization config path + blob `cda209dc1ab8d6f623c6bb1c2b818c48e09d1bf8`;
- frozen bank ledger;
- frozen materialization manifest;
- retrieval execution gate config;
- retrieval gate manifest;
- retrieval input inventory;
- H100 y EVAL hashes congelados.

Debe registrar explícitamente:

### `governed_bank_identity_contract`

Los 14 campos:

- bank_id
- filename
- seed
- condition
- row_count
- new_row_count
- total_dam_count
- new_dam_count
- bank_csv_sha256
- size_bytes
- composition_sha256
- H100_core_id_order_sha256
- increment_id_order_sha256
- total_bank_id_order_sha256

Y:

```text
triple_comparison_status = PASS_EXACT_20_OF_20
bank_identity_mismatch_count = 0
```

### `runtime_evidence_classification`

Registra exactamente que:

```text
classification = CODEX_LOCAL_RUNTIME_EVIDENCE / NOT_INDEPENDENTLY_REEXECUTED_BY_EXTERNAL_AUDITOR
```

No promociones los eventos runtime del host a GitHub CI ni a observación independiente de la IA Experimental.

### `process_return_code_assessment`

Debe registrar:

```text
observed_return_code = 2
blocking_for_governed_bank_identity = false
failure_field = total_bank_descriptor
failure_field_is_part_of_required_14_identity_contract = false
max_absolute_delta = 5.329070518200751e-15
historical_descriptor_tolerance = 1e-12
within_historical_descriptor_tolerance = true
bank_csv_content_affected = false
```

No borres ni maquilles el return code.

### `config_provenance_resolution`

Debe registrar:

- canonical LF SHA-256 `a7fa158dcf13e4b293e3de51351f814305cf5208b08395d5de8994f2d69c710c`;
- Windows CRLF SHA-256 `39c27e6791bcc5d574a2c132af59bbe99a4793ee0506d95724ad8f2d632a5e17`;
- Git blob `cda209dc1ab8d6f623c6bb1c2b818c48e09d1bf8`;
- `semantic_json_equal = true`;
- clasificación `SAME_GIT_BLOB_EQUIVALENT_JSON_LF_VS_CRLF_CHECKOUT_REPRESENTATION`;
- `semantic_config_drift = false`.

### `historical_notice_resolution`

Registra que el notice histórico que bloqueaba autorización por deuda de procedencia:

`retrieval_authorization_blocked_pending_external_audit = true`

permanece inmutable en el artefacto histórico, pero su condición de bloqueo se considera:

`SUPERSEDED_FOR_PORTABILITY_DEBT_BY_PROMPT41_EXTERNAL_AUDIT`

Esto NO equivale a autorizar retrieval.

Debe quedar expresamente:

```text
retrieval_authorization_requires_separate_future_block = true
retrieval_executed = false
evaluation_metrics_computed = false
exp11b_retrieval_authorized = false
exp12_authorized = false
historical_gate_artifacts_mutated = false
canonical_plan_modified = false
article_modified = false
```

---

# 6. Validación del candidato de cierre

Antes de publicar verifica:

- parent directo = `7d7267f...`;
- exactamente 1 commit;
- exactamente 1 changed path;
- ese path es únicamente `exp11b_portability_debt_external_closure_v0.1.json`;
- ningún archivo histórico/gate/config/manifiesto/ledger modificado;
- no retrieval;
- no métricas;
- no H150/H200 results;
- no cambios Plan/Article/EXP12;
- working tree tracked limpio.

Publica únicamente:

`codex/exp11b-portability-debt-external-closure-v01`

NO la integres a `main` en este bloque.

Estado máximo permitido del cierre:

```text
PORTABILITY_CLOSURE_RECORD = CANDIDATE / PENDING_EXTERNAL_GIT_AUDIT
EXP11B_PORTABILITY_DEBT = CLOSED_BY_EXTERNAL_DECISION / PENDING_CLOSURE_RECORD_INTEGRATION
EXP11B_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```

El Plan canónico sigue mostrando la deuda histórica OPEN hasta que este closure record sea auditado e integrado y se haga una reconciliación documental separada.

---

# 7. Prohibiciones absolutas

NO:

- integrar `799156b3c98858fbe081de73f381030426174ce1`;
- reejecutar Prompt41;
- rematerializar bancos oficiales;
- ejecutar EXP11B Retrieval H150/H200;
- calcular Top-k/MRR H150/H200;
- crear outputs de retrieval;
- autorizar retrieval;
- modificar H100/DEV/EVAL;
- modificar BM25;
- modificar Attempt06;
- modificar Plan Maestro;
- modificar Article;
- modificar EXP12;
- abrir Grupo 2B;
- avanzar a Grupo 3;
- reinterpretar resultados científicos.

---

# 8. Persistencia administrativa

Después del trabajo científico:

1. vuelve a `codex/prompts-temporary`;
2. haz `git fetch`;
3. no rebase/amend/force;
4. crea exclusivamente:

`codex_prompts_tmp/42_RESPUESTA_INTEGRAR_REPLAY_Y_CONSTRUIR_CIERRE_DEUDA_PORTABILIDAD_EXP11B.md`

El commit administrativo debe ser response-only.

El reporte debe incluir:

- refs iniciales/finales;
- verificación completa del candidato Prompt41;
- integración exacta a main;
- main final tras Fase A;
- branch/commit/tree/parent del closure candidate;
- path/blob del closure record;
- clasificación explícita del return code 2;
- clasificación epistemológica de la evidencia runtime;
- confirmación de 14-field contract y triple 20/20;
- confirmación de que no se modificaron gate/config/manifest/ledger históricos;
- Plan/Article intactos;
- retrieval/metrics/EXP12 no ejecutados/autorizados;
- estado final.

Responde únicamente con el reporte final y detente.
