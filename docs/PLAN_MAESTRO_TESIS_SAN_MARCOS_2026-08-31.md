# Plan maestro canónico — Tesis San Marcos

**Proyecto:** Framework RAG explicativo y auditable para recomendación de subpartidas NANDINA  
**Fecha de actualización:** 2026-09-01

## 1. Principios congelados

1. SERIE es la unidad de análisis.
2. DAM/DECLARACIÓN es la unidad de agrupamiento cuando existe dependencia.
3. La recuperación histórica produce el ranking principal.
4. La recuperación normativa aporta evidencia y no reordena el ranking histórico.
5. Top-3 fijo antes de generación.
6. El LLM local explica; no clasifica desde cero.
7. Evalset v0.2 fijo: 1,056 casos.
8. No se cambian reglas experimentales después de observar resultados.
9. Nueva data histórica: Excel fuente → Python versionado → dataset derivado → auditoría → hashes → gate.
10. EXP-11A/11B no se interpretan como efecto causal aislado del tamaño si cambia la composición.

## 2. Estado general

| Grupo | Estado |
|---|---|
| 1. Diseño y ejecución experimental | **CLOSED / APPROVED** |
| 2. Reproducibilidad y trazabilidad | **EN CURSO — Gate 03 CLOSED; EXP11B bank materialization candidato 7a80b1d reproducido 20/20; microclose requerido antes de integrar** |
| 3. Métricas e inferencia | Pendiente |
| 4–8 | Pendientes |

## 3. Benchmark congelado

- H100: 2,950 filas / 28 DAM / 66 NANDINA; SHA `0990cdfe2a62638bff83a1182b0d6b0b727d670f63888044e99fd3ee0d7915ff`.
- DEV: 100 filas; SHA `434e08f13ed3d5529165abbd0e139b5a675e7dc164307a624caa95f60a271f00`.
- EVAL: 1,056 filas; SHA `3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941`.

## 4. Cierres previos

- Grupo 1: **CLOSED / APPROVED**.
- Grupo 2A: **CLOSED / APPROVED_WITH_NONBLOCKING_LIMITATIONS**.
- EXP-11A: **CLOSED / APPROVED / INTEGRATED** en `9e8af129ca586bd1929e6afe6aa1a1c64d8fe667`.
- Gate 02: **CLOSED / APPROVED / INTEGRATED** en `ad4c630a6a4d442776740b59b9552ba72141ea48`.
- Gate 03: **CLOSED / APPROVED / INTEGRATED** en `ed470d67315f505cb3bde471177268db6d16a676`.

## 5. Real Ingest 01

- Pool elegible SHA `a78e8c517d50f53fa0f8b95a6c94f841dda4c0e3e5cf28cc4c4fccc576c083a4`.
- 6,029 filas / 43 DAM / 56 NANDINA.
- H100/new DAM overlap = 0.
- Pool máximo H100+new = 8,979 filas / 71 DAM / 77 NANDINA.
- H150/H200 factibles.

## 6. Diseño EXP-11B congelado en Gate 03

- H100 núcleo fijo.
- Selección por DAM completa.
- Selector usa solo DAM id + row count + seed + namespace.
- H150 estrictamente anidado en H200.
- Tolerancia ±148.
- Seeds: `20261005, 20261006, 20261007, 20261010, 20261011, 20261013, 20261017, 20261021, 20261023, 20261024`.
- 20/20 composiciones preservadas.
- Common-clean: primary 1056; exact clean 1020; near090 981; near095 1002; near098 1010.

## 7. EXP11B_BANK_MATERIALIZATION_GATE — candidato

Rama: `codex/exp11b-bank-materialization-v01`  
Candidato: `7a80b1db657386705d3031559c2861d0a2f88eb2`  
Base/main: `ed470d67315f505cb3bde471177268db6d16a676`.

**AUDITORÍA EXTERNA: APPROVED_WITH_BLOCKING_MICROCLOSE_BEFORE_MAIN.**

### Lo validado

- 10 H150 + 10 H200 materializados localmente.
- H100 core 20/20 PASS.
- selección Gate03 20/20 PASS.
- descriptores 20/20 PASS.
- nesting 10/10 PASS.
- 20 bank SHA congelados.
- clean checkout reprodujo 20/20 byte exacto.
- bancos CSV no versionados; manifest/hash inventory sí.
- no retrieval, BM25 ni métricas.

### Hallazgos antes de integrar

`EXP11B-MAT-F001 = DEV_EVAL_PROVENANCE_NOT_HASH_FROZEN / S2`

DEV/EVAL son inputs efectivos del control de overlap, pero la config registra solo sus paths; el materializer los lee sin SHA y el manifest no conserva sus hashes. Deben fijarse los SHA DEV/EVAL ya congelados y fallar si cambian, sin alterar ningún bank SHA.

`EXP11B-MAT-F002 = FROZEN_GATE03_TEST_WEAKENED_OUTSIDE_SCOPE / S2`

El candidato cambió además `tests/test_exp11b_historical_size_extension_v01.py`: `assertEqual` → `assertAlmostEqual(..., places=15)`. Gate03 ya estaba cerrado y este archivo no pertenecía al scope materializador. Debe revertirse exactamente a `ed470d6`. Si el test exacto falla, detener y reportar floats; no debilitar el test.

`EXP11B-MAT-F003 = HASH_INVENTORY_VERIFY_NOT_FAIL_CLOSED / S2`

`verify()` reaudita los bancos y compara el manifest, pero para `exp11b_bank_hashes_v0.1.csv` solo exige 20 filas/bank_id. Debe comparar los valores del inventario con los bancos/manifest por bank_id.

### Estado

- `EXP11B_BANK_MATERIALIZATION_CANDIDATE_CREATED=true`.
- `BANKS_BYTE_REPRODUCIBLE=20/20`.
- `EXP11B_BANK_MATERIALIZATION_EXTERNAL_APPROVAL=false`.
- `EXP11B_RETRIEVAL_AUTHORIZED=false`.
- `RETRIEVAL_EXECUTED=false`.
- `EXP12_AUTHORIZED=false`.
- `GROUP3_STARTED=false`.

## 8. Orden maestro

```text
Grupo 1 ✅
  ↓
Grupo 2A ✅
  ↓
EXP-11A ✅
  ↓
Gate 02 ✅
  ↓
Real Ingest 01 ✅
  ↓
Gate 03 ✅ CLOSED / INTEGRATED ed470d6
  ↓
EXP11B_BANK_MATERIALIZATION candidato 7a80b1d ⚠ microclose F001–F003
  ↓
Integración materialization gate
  ↓
EXP-11B retrieval
  ↓
EXP-12
  ↓
Grupo 2B
  ↓
Grupo 3
  ↓
Grupos 4–8
```
