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
| 2. Reproducibilidad y trazabilidad | **EN CURSO — EXP11B Bank Materialization microclose `95ffec45` aprobado externamente; integración a main pendiente; retrieval bloqueado** |
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

## 5. Real Ingest 01 y diseño EXP-11B

- `new_historical_eligible.csv` SHA `a78e8c517d50f53fa0f8b95a6c94f841dda4c0e3e5cf28cc4c4fccc576c083a4`.
- 6,029 filas / 43 DAM / 56 NANDINA.
- H100/new DAM overlap = 0.
- Pool máximo H100+new = 8,979 filas / 71 DAM / 77 NANDINA.
- H150/H200 factibles.
- Selección por DAM completa; H100 núcleo fijo.
- Selector: DAM id + row count + seed + namespace; no NANDINA, descripción, EVAL, performance, BM25 ni duplicados.
- H150 estrictamente anidado en H200.
- Tolerancia ±148.
- Seeds: `20261005, 20261006, 20261007, 20261010, 20261011, 20261013, 20261017, 20261021, 20261023, 20261024`.
- Common-clean: primary 1056; exact clean 1020; near090 981; near095 1002; near098 1010.

## 6. EXP11B Bank Materialization Gate

Rama: `codex/exp11b-bank-materialization-v01`  
Candidato inicial: `7a80b1db657386705d3031559c2861d0a2f88eb2`  
Microclose: `95ffec45ae5a734545ae7bb2d8d530f42f8f056c`  
Base/main: `ed470d67315f505cb3bde471177268db6d16a676`.

**AUDITORÍA EXTERNA DEL MICROCLOSE: APPROVED_FOR_MAIN_INTEGRATION.**

### Materialización validada

- 10 bancos H150 + 10 bancos H200.
- H100 core 20/20 PASS.
- selección Gate03 20/20 PASS.
- descriptores 20/20 PASS.
- nesting 10/10 PASS.
- Los 20 CSV canónicos no se versionan en Git; son derivados deterministas.
- Clean checkout reproduce 20/20 byte exacto.
- Los 20 bank SHA, tamaños, filas, composition SHA y hashes de orden de IDs permanecen idénticos al candidato inicial `7a80b1d`.
- `retrieval_executed=false`; `evaluation_metrics_computed=false`.

### Microclose F001–F003

- `EXP11B-MAT-F001=VERIFIED_RESOLVED`.
  - DEV y EVAL quedan pinneados por SHA y row count.
  - El materializer falla si cualquiera cambia.
  - El manifest registra SHA esperado y observado para ambos.

- `EXP11B-MAT-F002=VERIFIED_RESOLVED`.
  - Diferencia float observada en Python 3.12.13: `2.7755575615628914e-17` (1 ULP).
  - Política explícita: `rel_tol=0`, `abs_tol=1e-12`.
  - Gate03 30/30 PASS.
  - Planner, feasibility, selección y bancos no cambian.

- `EXP11B-MAT-F003=VERIFIED_RESOLVED`.
  - `--verify` compara campo a campo las 14 columnas del ledger por bank_id.
  - Pruebas de corrupción son fail-closed.

### Reconciliación de tests

Mismo runtime Python 3.12.13:

- base `ed470d6`: 326 tests; único fallo = comparación float exacta documentada;
- candidato corregido: 368/368;
- Gate02: 27/27;
- Gate03: 30/30;
- materialización: 41/41.

Formal `--verify`: PASS.

### Estado

- `EXP11B_BANK_MATERIALIZATION_MICROCLOSE=APPROVED_FOR_MAIN_INTEGRATION`.
- `BANK_IDENTITIES_UNCHANGED=true`.
- `BANK_IDENTITIES_MATCH=20/20`.
- `BANKS_BYTE_REPRODUCIBLE=20/20`.
- `RETRIEVAL_EXECUTED=false`.
- `EXP11B_RETRIEVAL_AUTHORIZED=false`.
- `EXP12_AUTHORIZED=false`.
- `GROUP3_STARTED=false`.

**Siguiente paso:** integrar `95ffec45ae5a734545ae7bb2d8d530f42f8f056c` por fast-forward a `main`, validar post-integración y rematerializar temporalmente 20/20. Solo después de ese cierre puede abrirse el gate de ejecución EXP-11B retrieval.

## 7. Orden maestro

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
EXP11B Bank Materialization 7a80b1d + microclose 95ffec45 ✅ auditoría externa
  ↓
Integración fast-forward a main ⏳
  ↓
EXP-11B retrieval gate
  ↓
EXP-12
  ↓
Grupo 2B
  ↓
Grupo 3
  ↓
Grupos 4–8
```
