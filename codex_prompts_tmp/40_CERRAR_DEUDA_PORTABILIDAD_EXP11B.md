# PROMPT 40 — CERRAR EXCLUSIVAMENTE LA DEUDA DE PORTABILIDAD EXP11B

## Objetivo

Cerrar, si la evidencia ya disponible lo permite, **exclusivamente** `EXP11B_PORTABILITY_DEBT=OPEN`, que actualmente bloquea la autorización de `EXP11B Retrieval Execution`.

Este bloque **NO autoriza ni ejecuta retrieval H150/H200**. No es una ronda de hardening general. No se deben introducir mejoras técnicas marginales ni rediseñar el gate.

La deuda conocida es puntual: el manifiesto histórico de materialización conserva un fingerprint de configuración distinto del archivo de configuración actualmente trackeado, mientras la identidad de los 20 bancos está gobernada por hashes/ledger/manifiesto ya congelados.

---

## 1. Referencias congeladas

Repositorio: `elVladdi/gci-nandina-rag`

Verifica primero con `git fetch`:

- `origin/main = 6846537602539506c8e90426daad05252cc982b9`;
- `origin/docs/plan-maestro-temporal-2026-08-31 = b814a8c2f976185209153e97e0d6ece0510526fb`;
- `origin/article/main-manuscript = 254b1e6df736fa9938ac86a515d65b36f4d361c5`.

Estado canónico relevante:

- `0B05C_CLOSURE=CLOSED / APPROVED_AFTER_CORRECTIVE_RECONCILIATION`;
- `EXP11B Bank Materialization=CLOSED / APPROVED / INTEGRATED`;
- `EXP11B Retrieval Execution Gate=APPROVED / INTEGRATED`;
- `EXP11B_PORTABILITY_DEBT=OPEN`;
- `EXP11B Retrieval Execution=NOT_AUTHORIZED / NOT_EXECUTED`;
- `EXP12=NOT_AUTHORIZED / NOT_EXECUTED`.

Si estas refs o estados no coinciden, STOP.

---

## 2. Alcance estricto de la deuda

Audita únicamente la discrepancia de procedencia ya registrada en:

`src/configs/exp11b_retrieval_execution_gate_v0.1.json`

entre:

- `manifest_embedded_config_sha256 = a7fa158dcf13e4b293e3de51351f814305cf5208b08395d5de8994f2d69c710c`
- `current_config_sha256 = 39c27e6791bcc5d574a2c132af59bbe99a4793ee0506d95724ad8f2d632a5e17`

No conviertas este bloque en una nueva auditoría completa de EXP11B.

Debes determinar de forma factual si esa discrepancia:

1. altera el contenido materializado de alguno de los 20 bancos;
2. altera seed, condition, row_count, new_row_count, DAM counts, `bank_csv_sha256`, `size_bytes`, `composition_sha256`, `H100_core_id_order_sha256`, `increment_id_order_sha256` o `total_bank_id_order_sha256`;
3. altera H100, EVAL o la semántica BM25 congelada;
4. o si es exclusivamente una diferencia histórica de fingerprint de configuración sin efecto sobre la identidad de los bancos ya materializados.

---

## 3. Fuentes obligatorias

Usa exclusivamente artefactos ya versionados en Git y comprobaciones read-only:

- `src/configs/exp11b_retrieval_execution_gate_v0.1.json`;
- `outputs/audits/exp11b_retrieval_execution_gate_v0.1/exp11b_retrieval_execution_gate_manifest_v0.1.json`;
- `outputs/audits/exp11b_retrieval_execution_gate_v0.1/exp11b_retrieval_execution_input_inventory_v0.1.json`;
- `outputs/audits/exp11b_bank_materialization_v0.1/exp11b_bank_materialization_manifest_v0.1.json`;
- `outputs/audits/exp11b_bank_materialization_v0.1/exp11b_bank_hashes_v0.1.csv`;
- `src/configs/exp11b_bank_materialization_v0.1.json`;
- los 20 CSV de bancos materializados ya versionados;
- historia Git del archivo `src/configs/exp11b_bank_materialization_v0.1.json`, si es necesaria para localizar el estado histórico que produjo el fingerprint embebido.

No uses Internet. No cambies datos científicos.

---

## 4. Criterio de cierre

La deuda puede proponerse como **CLOSED_PENDING_EXTERNAL_AUDIT** únicamente si se demuestra conjuntamente que:

1. los 20 bancos actuales son exactamente los bancos congelados por ledger/manifiesto;
2. no existe mismatch de identidad de banco en los campos congelados;
3. H100 y EVAL permanecen con sus hashes congelados;
4. la semántica retrieval BM25 no se altera;
5. la diferencia `a7fa...` vs `39c...` puede clasificarse como **provenance/config-history mismatch without bank-content mutation**;
6. no es necesario rematerializar H150/H200 para preservar validez experimental.

Si no puedes demostrar cualquiera de esos seis puntos, STOP con el motivo exacto. No rematerialices bancos y no intentes “arreglar” la historia.

---

## 5. Artefacto candidato mínimo

Si el criterio de cierre pasa, crea una rama nueva desde `main` exacto:

`codex/exp11b-portability-debt-closure-v01`

Debe contener **un único commit** hijo directo de:

`6846537602539506c8e90426daad05252cc982b9`

Añade únicamente:

`outputs/audits/exp11b_retrieval_execution_gate_v0.1/exp11b_portability_debt_closure_v0.1.json`

No modifiques todavía el gate/config existente, no cambies `exp11b_retrieval_authorized=false` y no crees authorization record.

El JSON debe incluir como mínimo:

- `artifact_id`;
- `status = CANDIDATE_CLOSED_PENDING_EXTERNAL_AUDIT`;
- `main_baseline_commit`;
- los dos fingerprints de configuración;
- clasificación de la discrepancia;
- referencias exactas a manifest, ledger y current config;
- evidencia de identidad de 20/20 bancos;
- `bank_identity_mismatch_count`;
- hashes H100 y EVAL verificados;
- confirmación de semántica BM25 preservada;
- `bank_rematerialization_required = false` solo si está demostrado;
- `retrieval_executed = false`;
- `evaluation_metrics_computed = false`;
- `exp11b_retrieval_authorized = false`;
- `external_audit_required = true`.

No agregues scripts, tests o nuevos contratos salvo que exista una imposibilidad objetiva para producir esta evidencia con los artefactos ya versionados. Si aparece esa imposibilidad, STOP en vez de expandir el alcance.

---

## 6. Prohibiciones

NO:

- ejecutar retrieval H150/H200;
- calcular métricas H150/H200;
- rematerializar los 20 bancos;
- modificar H100, DEV o EVAL;
- modificar los outputs de Attempt06;
- modificar `main`;
- modificar Plan Maestro;
- modificar Article;
- modificar EXP12;
- autorizar EXP11B Retrieval;
- abrir una ronda de hardening general.

Este bloque es únicamente cierre evidencial de una deuda de portabilidad ya conocida.

---

## 7. Reporte obligatorio

Persistir en `codex/prompts-temporary`:

`codex_prompts_tmp/40_RESPUESTA_CERRAR_DEUDA_PORTABILIDAD_EXP11B.md`

El reporte debe indicar:

- refs iniciales y finales;
- clasificación exacta de la discrepancia;
- si se recuperó o no el estado histórico de config que corresponde a `a7fa...`;
- verificación 20/20 bancos;
- mismatch count;
- H100/EVAL hashes;
- si rematerialización es necesaria o no;
- commit candidato y parent, si se publicó;
- changed paths exactos;
- confirmación de que retrieval/metrics no se ejecutaron;
- estado de `EXP11B_PORTABILITY_DEBT` como candidato, no como cierre externo definitivo.

### Estado permitido si pasa

```text
PROMPT40 = COMPLETED
EXP11B_PORTABILITY_DEBT = CANDIDATE_CLOSED_PENDING_EXTERNAL_AUDIT
EXP11B_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```

### Estado permitido si no puede cerrarse

```text
PROMPT40 = STOP / PORTABILITY_DEBT_NOT_EVIDENTIALLY_CLOSED
EXP11B_PORTABILITY_DEBT = OPEN
EXP11B_RETRIEVAL = NOT_AUTHORIZED / NOT_EXECUTED
EXP12 = NOT_AUTHORIZED / NOT_EXECUTED
```

Responde únicamente con el reporte final exigido.
