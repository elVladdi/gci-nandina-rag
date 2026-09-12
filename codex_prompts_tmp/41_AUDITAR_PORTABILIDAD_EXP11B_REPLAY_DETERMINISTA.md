# PROMPT 41 — AUDITAR PORTABILIDAD EXP11B MEDIANTE REPLAY DETERMINISTA

## Objetivo

Resolver exclusivamente la brecha evidencial detectada por la auditoría externa de `codex_prompts_tmp/40_RESPUESTA_CERRAR_DEUDA_PORTABILIDAD_EXP11B.md`.

La auditoría externa NO aprobó el candidato `799156b3c98858fbe081de73f381030426174ce1`, porque los 20 CSV oficiales de bancos EXP11B no están versionados como blobs Git y, por tanto, la coincidencia local 20/20 reportada por Codex no puede verificarse independientemente desde GitHub.

Este bloque debe determinar si los 20 bancos EXP11B pueden reconstruirse determinísticamente desde inputs, configuración y lógica versionados, y si el replay coincide exactamente con las identidades congeladas por ledger/manifiesto y con los bancos oficiales locales observados en modo read-only.

Este bloque NO autoriza ni ejecuta retrieval H150/H200, NO calcula métricas y NO modifica Plan Maestro ni Article.

---

## 1. Referencias congeladas

Repositorio: `elVladdi/gci-nandina-rag`

Verifica primero con `git fetch`:

- `origin/main = 6846537602539506c8e90426daad05252cc982b9`;
- `origin/docs/plan-maestro-temporal-2026-08-31 = b814a8c2f976185209153e97e0d6ece0510526fb`;
- `origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5`.

Estado canónico relevante:

- `0B05C_CLOSURE = CLOSED / APPROVED_AFTER_CORRECTIVE_RECONCILIATION`;
- `EXP11B Bank Materialization = CLOSED / APPROVED / INTEGRATED`;
- `EXP11B Retrieval Execution Gate = APPROVED / INTEGRATED`;
- `EXP11B_PORTABILITY_DEBT = OPEN`;
- `EXP11B Retrieval Execution = NOT_AUTHORIZED / NOT_EXECUTED`;
- `EXP12 = NOT_AUTHORIZED / NOT_EXECUTED`.

Si cualquiera de estas refs o estados difiere, STOP con `PRECONDITION_DRIFT`.

---

## 2. Alcance estricto

Audita únicamente portabilidad/reproducibilidad de los 20 bancos EXP11B.

Debes demostrar si la materialización histórica puede repetirse desde estado versionado sin reimplementar decisiones científicas y sin usar los bancos oficiales como input del replay.

No conviertas este bloque en hardening general.

---

## 3. Fuentes obligatorias

Usa como mínimo:

- `src/configs/exp11b_bank_materialization_v0.1.json`;
- `outputs/audits/exp11b_bank_materialization_v0.1/exp11b_bank_materialization_manifest_v0.1.json`;
- `outputs/audits/exp11b_bank_materialization_v0.1/exp11b_bank_hashes_v0.1.csv`;
- `outputs/audits/exp11b_retrieval_execution_gate_v0.1/exp11b_retrieval_execution_gate_manifest_v0.1.json`;
- `outputs/audits/exp11b_retrieval_execution_gate_v0.1/exp11b_retrieval_execution_input_inventory_v0.1.json`;
- el builder/materializador histórico versionado y cualquier helper del que dependa;
- todos los inputs científicos requeridos por ese materializador;
- el schedule de seeds y reglas de composición congeladas.

No inventes un materializador nuevo. Si la lógica histórica necesaria no puede recuperarse de artefactos versionados de forma suficiente para reconstruir los bancos, STOP con `VERSIONED_REPLAY_LOGIC_INSUFFICIENT`.

---

## 4. Inputs congelados

Verifica SHA-256 de todos los inputs utilizados por el materializador.

Como mínimo:

- H100: `data/processed/data_aduanas_historico_clase87_v0.2.csv` = `0990cdfe2a62638bff83a1182b0d6b0b727d670f63888044e99fd3ee0d7915ff`;
- EVAL: `data/processed/data_aduanas_evalset_clase87_v0.2.csv` = `3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941`.

Verifica además cualquier otro input requerido contra la evidencia congelada disponible.

Si un input necesario no está versionado, no existe, no coincide con su hash o depende de estado local no gobernado, STOP con `REPLAY_INPUT_NOT_PORTABLE`.

---

## 5. Discrepancia de configuración

Vuelve a verificar la discrepancia ya registrada:

- `manifest_embedded_config_sha256 = a7fa158dcf13e4b293e3de51351f814305cf5208b08395d5de8994f2d69c710c`;
- working-tree Windows observado previamente = `39c27e6791bcc5d574a2c132af59bbe99a4793ee0506d95724ad8f2d632a5e17`;
- Git blob canónico identificado = `cda209dc1ab8d6f623c6bb1c2b818c48e09d1bf8`.

Distingue explícitamente identidad de blob Git, contenido Git canónico, representación working-tree, EOL y equivalencia semántica de configuración.

No reescribas archivos para forzar hashes. Si la explicación LF/CRLF no puede demostrarse de forma reproducible, STOP con `CONFIG_PROVENANCE_NOT_DEMONSTRATED`.

---

## 6. No mutación de bancos oficiales

Los bancos oficiales locales bajo `data/interim/exp11b_historical_banks_v0.1/`, si existen, son INMUTABLES.

Está prohibido sobrescribirlos, regenerarlos in place, renombrarlos, moverlos, borrarlos o usarlos como input de construcción.

Antes y después del replay registra sus SHA-256 y tamaños en modo read-only.

Debe quedar:

- `official_bank_write_count = 0`;
- `official_bank_content_mutated = false`.

Si no puede garantizarse, STOP con `OFFICIAL_BANK_MUTATION_RISK`.

---

## 7. Replay aislado

Ejecuta la reconstrucción en un entorno temporal aislado, preferentemente `git worktree` detached, anclado exactamente a `6846537602539506c8e90426daad05252cc982b9`.

El replay debe:

1. partir del commit exacto;
2. comenzar con worktree limpio;
3. usar solo inputs/config/lógica gobernados;
4. no copiar ni leer bancos oficiales durante la construcción;
5. producir outputs exclusivamente temporales;
6. reconstruir exactamente 10 bancos H150 y 10 bancos H200.

Registra comando exacto, versión de Python, plataforma, dependencias relevantes, materializador y hashes/blobs de código/configuración.

Si requiere Internet, archivos externos no gobernados, decisiones manuales o instalación ad hoc no documentada, STOP con `REPLAY_NOT_SELF_CONTAINED`.

---

## 8. Seeds congeladas

Usa exclusivamente:

- 20261005
- 20261006
- 20261007
- 20261010
- 20261011
- 20261013
- 20261017
- 20261021
- 20261023
- 20261024

No ejecutes seeds adicionales ni sustituyas réplicas.

---

## 9. Comparación triple obligatoria

Para cada banco compara:

- `FROZEN`: ledger/manifiesto/inventory;
- `OFFICIAL_OBSERVED`: CSV oficial local leído solo después de reconstruir, exclusivamente para comparación read-only;
- `REPLAY`: CSV generado en el entorno temporal.

Compara como mínimo:

- `bank_id`;
- `filename`;
- `seed`;
- `condition`;
- `row_count`;
- `new_row_count`;
- `total_dam_count`;
- `new_dam_count`;
- `bank_csv_sha256`;
- `size_bytes`;
- `composition_sha256`;
- `H100_core_id_order_sha256`;
- `increment_id_order_sha256`;
- `total_bank_id_order_sha256`.

Genera:

- `frozen_official_match_count` / `frozen_official_mismatch_count`;
- `frozen_replay_match_count` / `frozen_replay_mismatch_count`;
- `official_replay_match_count` / `official_replay_mismatch_count`.

Éxito exige 20 matches y 0 mismatches en las tres comparaciones.

Si los bancos oficiales no están disponibles localmente, STOP con `OFFICIAL_BANK_OBSERVATION_UNAVAILABLE`. No debilites el criterio a solo frozen-vs-replay.

---

## 10. BM25

No ejecutes retrieval.

Verifica estáticamente que los bindings congelados siguen siendo:

- normalization = `unicode_NFKD_lowercase_remove_combining_marks`;
- tokenizer = `regex_[a-z0-9]+`;
- `k1 = 1.5`;
- `b = 0.75`;
- `candidate_depth = 100`;
- `k_values = 1,3,5,10,50`;
- ranking = `descending_score_then_ascending_historical_case_id`.

Debe quedar:

- `bm25_semantics_preserved = true`;
- `retrieval_executed = false`;
- `evaluation_metrics_computed = false`.

---

## 11. Artefacto candidato mínimo

Solo si todo pasa, crea una rama nueva desde `main` exacto:

`codex/exp11b-portability-replay-proof-v01`

Debe ser hija directa de `6846537602539506c8e90426daad05252cc982b9`.

Añade únicamente:

`outputs/audits/exp11b_retrieval_execution_gate_v0.1/exp11b_portability_replay_proof_v0.1.json`

No incluyas bancos replay, worktree temporal ni cambios científicos.

El JSON debe incluir como mínimo:

- `artifact_id`;
- `status = CANDIDATE_PORTABILITY_REPLAY_VERIFIED_PENDING_EXTERNAL_AUDIT`;
- `main_baseline_commit`;
- `external_audit_origin = PROMPT40_REJECTED`;
- evidencia de inputs versionados;
- binding del materializador y configuración;
- evidencia de procedencia/configuración;
- conteos esperados, observados y replay;
- comparación por banco;
- seis contadores match/mismatch;
- `H100_hash_match`;
- `EVAL_hash_match`;
- `bm25_semantics_preserved`;
- `official_bank_write_count`;
- `official_bank_content_mutated`;
- `replay_outputs_temporary`;
- `replay_outputs_removed_after_audit`;
- `retrieval_executed = false`;
- `evaluation_metrics_computed = false`;
- `exp11b_retrieval_authorized = false`;
- `exp12_authorized = false`;
- `external_audit_required = true`.

Codex NO puede cerrar definitivamente la deuda. Debe quedar `EXP11B_PORTABILITY_DEBT = OPEN_PENDING_EXTERNAL_AUDIT`.

---

## 12. Limpieza

Después de capturar la evidencia elimina únicamente el entorno temporal del replay y verifica que los artefactos oficiales permanecen intactos.

Registra:

- `temporary_replay_cleanup = PASS`;
- `official_artifacts_preserved = true`.

---

## 13. Prohibiciones

NO:

- integrar `799156b3c98858fbe081de73f381030426174ce1`;
- modificar `main`;
- modificar Plan Maestro;
- modificar Article;
- modificar EXP12;
- ejecutar EXP11B Retrieval H150/H200;
- calcular Top-k/MRR H150/H200;
- rematerializar bancos oficiales in place;
- cambiar seeds, H100, DEV o EVAL;
- modificar Attempt06;
- reinterpretar resultados científicos;
- abrir Grupo 2B o bloques posteriores.

---

## 14. Estado terminal

Si todo pasa:

```text
PROMPT41 = COMPLETED
EXP11B_PORTABILITY_REPLAY = CANDIDATE_VERIFIED_PENDING_EXTERNAL_AUDIT
EXP11B_PORTABILITY_DEBT = OPEN_PENDING_EXTERNAL_AUDIT
EXP11B_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```

Si cualquier requisito falla:

```text
PROMPT41 = STOP / PORTABILITY_REPLAY_EVIDENCE_INCOMPLETE
EXP11B_PORTABILITY_DEBT = OPEN
EXP11B_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```

---

## 15. Reporte obligatorio

Persistir en la rama `codex/prompts-temporary`:

`codex_prompts_tmp/41_RESPUESTA_AUDITAR_PORTABILIDAD_EXP11B_REPLAY_DETERMINISTA.md`

El reporte debe contener refs iniciales/finales, precondiciones, materializador/helpers, inputs/hashes, comando y entorno de replay, evidencia de independencia respecto de los bancos oficiales, comparación triple 20/20, detalle por banco, mismatch counts, H100/EVAL, BM25 estático, no mutación, limpieza, commit candidato/parent/changed paths si existe, y confirmación expresa de que retrieval, métricas, Plan Maestro, Article y EXP12 no fueron modificados/ejecutados.

Responde únicamente con el reporte final exigido y DETENTE.
