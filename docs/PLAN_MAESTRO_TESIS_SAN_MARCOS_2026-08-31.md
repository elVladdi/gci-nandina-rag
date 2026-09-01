# Plan maestro canónico — Tesis San Marcos

**Proyecto:** Framework RAG explicativo y auditable para recomendación de subpartidas NANDINA  
**Repositorio principal:** `elVladdi/gci-nandina-rag`  
**Repositorio público de reproducibilidad:** `elVladdi/gci-nandina-rag-reproducibility`  
**Fecha de actualización:** 2026-09-01

## 1. Principios congelados

1. **SERIE** es la unidad de análisis.
2. **DAM / DECLARACIÓN** es la unidad de agrupamiento cuando existe dependencia.
3. La recuperación histórica produce el ranking principal de candidatos.
4. La recuperación normativa aporta evidencia documental y no sustituye ni reordena el ranking histórico.
5. El **Top-3 es fijo** antes de la generación.
6. El **LLM local** explica el Top-3 recuperado; no clasifica desde cero.
7. El reranker LLM es únicamente diagnóstico.
8. El piloto permanece restringido experimentalmente a Clase 87.
9. El evalset v0.2 de **1,056 casos** permanece fijo.
10. No se cambian reglas experimentales después de observar resultados.
11. Toda nueva data histórica sigue **Excel fuente → Python versionado → dataset derivado → auditoría → hashes → gate**.
12. EXP-11A/11B no permiten inferir un efecto causal aislado del tamaño si cambia la composición.

## 2. Estado del plan de auditoría

| Grupo | Estado |
|---|---|
| 1. Diseño y ejecución experimental | **CLOSED / APPROVED** |
| 2. Reproducibilidad y trazabilidad | **EN CURSO — Gate 03 microclose aprobado externamente; integración a main pendiente antes de materialización H150/H200** |
| 3. Métricas e inferencia | Pendiente |
| 4. Análisis e interpretación | Pendiente |
| 5. Presentación de resultados | Pendiente |
| 6. Figuras y visualizaciones | Pendiente |
| 7. Redacción científica | Pendiente |
| 8. Coherencia metodológica/documental | Pendiente |

## 3. Benchmark v0.2 congelado

- H100: 2,950 series / 28 DAM / 66 NANDINA.
- DEV: 100 series / 6 DAM.
- EVAL: 1,056 series / 67 DAM / 42 NANDINA.
- H100 SHA: `0990cdfe2a62638bff83a1182b0d6b0b727d670f63888044e99fd3ee0d7915ff`.
- DEV SHA: `434e08f13ed3d5529165abbd0e139b5a675e7dc164307a624caa95f60a271f00`.
- EVAL SHA: `3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941`.
- H100: Top-1 0.509470; Top-3 0.671402; Top-5 0.763258; Top-10 0.891098; Top-50 0.991477; MRR 0.629708.

## 4. Grupo 1 / Grupo 2A / EXP-11A

- Grupo 1: **CLOSED / APPROVED**.
- Grupo 2A: **CLOSED / APPROVED_WITH_NONBLOCKING_LIMITATIONS**.
- EXP-11A: **CLOSED / APPROVED / VERSIONED / INTEGRATED**.
- Commit final EXP-11A: `9e8af129ca586bd1929e6afe6aa1a1c64d8fe667`.
- HE2/HE5 permanecen pendientes hasta Grupo 3.

## 5. Forensic Audit 01 + Gate 02

- Pipeline Excel→Python→v0.1→v0.2: `PIPELINE_PARTIALLY_RECONSTRUCTED` con outputs H100/DEV/EVAL reproducidos byte a byte.
- Fuente H100 reproducing source congelada: SHA `db01d1fcdd41d1bd1ed8086fc6c19bcd56ba44b2534391aba7daa4c58f9f52d1`.
- `Hoja2` fue la hoja históricamente procesada; `Hoja1` es preexistente no procesada.
- Gate 02: **CLOSED / APPROVED / INTEGRATED TO MAIN** en `ad4c630a6a4d442776740b59b9552ba72141ea48`.
- Contrato nuevo: `NUEVA_01` o `NUEVA_01,NUEVA_02`, siempre por selección explícita `--sheet`.

## 6. Real Ingest 01 — NUEVA_01

**APPROVED / FROZEN IN GATE 03 CANDIDATE.**

- F001 `VERIFIED_RESOLVED`: única diferencia histórica parser = `__source_file`.
- F002 `VERIFIED_RESOLVED`: invocación directa por path para archivo `v0.1.py`.
- Fuente ampliada congelada: SHA `087efd97cb17fd166c2e7eb5089690577491e99ab5d415f9e3a8614923ee4ba3`, 16,060,154 bytes.
- NUEVA_01: 15,596 parseadas; 6,029 Clase 87; 6,029 elegibles.
- Pool nuevo: 6,029 filas / 43 DAM / 56 NANDINA.
- Pool elegible SHA: `a78e8c517d50f53fa0f8b95a6c94f841dda4c0e3e5cf28cc4c4fccc576c083a4`.
- H100/new DAM overlap = 0.
- H100+new máximo: 8,979 filas / 71 DAM / 77 NANDINA.
- Capacidad: `H150_AND_H200_FEASIBLE`; `NUEVA_02_REQUIRED=false`.
- Sin retrieval; sin H150/H200 materializados.

## 7. NEW HISTORICAL GATE 03

Rama: `codex/new-historical-gate-expanded-pool-v01`  
Candidato inicial: `b3806190cb645d35c2a121c0f1d0c07fbfe21605`  
Microclose corregido: `ed470d67315f505cb3bde471177268db6d16a676`  
Base `main`: `ad4c630a6a4d442776740b59b9552ba72141ea48`.

**AUDITORÍA EXTERNA DEL MICROCLOSE: APPROVED_FOR_MAIN_INTEGRATION.**

### Diseño prospectivo EXP-11B congelado

- Selección usa solo: DAM id + row count + seed + namespace.
- No usa NANDINA, descripción, EVAL, performance, BM25 ni duplicados.
- H100 permanece núcleo fijo de 2,950 filas.
- Unidad de selección: DAM completa.
- H150 estrictamente anidado en H200 por réplica.
- Tolerancia de incremento: ±148.
- 24 seeds evaluados; 10 pares aceptados.
- Seeds exactos: `20261005, 20261006, 20261007, 20261010, 20261011, 20261013, 20261017, 20261021, 20261023, 20261024`.
- Identidad de selección contra `b380619`: 20/20 composiciones H150/H200 intactas.
- `H150_MATERIALIZED=false`; `H200_MATERIALIZED=false`; `RETRIEVAL_EXECUTED=false`.

### Hallazgos del candidato inicial y cierre

- `NHG03-F001 = TOTAL_BANK_DESCRIPTORS_MISSING` → **VERIFIED_RESOLVED**.
  - Cada condición contiene `increment_descriptor`.
  - Cada condición contiene `total_bank_descriptor = H100_FROZEN + incremento`.
  - Se registran rows, DAM count, HHI, effective DAM, largest DAM share, NANDINA y cobertura H100.
  - Todos los bancos totales conservan cobertura H100 `66/66`.

- `NHG03-F002 = COMMON_CLEAN_DENOMINATORS_NOT_EXPLICIT` → **VERIFIED_RESOLVED**.
  - `N_PRIMARY=1056`.
  - masked: exact=36, near090=75, near095=54, near098=46.
  - clean: exact=1020, near090=981, near095=1002, near098=1010.
  - La máscara no afecta selección ni denominador primario.

### Validación

- `eval_common_clean_masks_v0.1.csv` intacto.
- `new_historical_eligible.csv` intacto.
- Real Ingest freeze: 9 artefactos, 0 mismatches.
- H100/DEV/EVAL SHA sin cambios.
- Tests: Gate 02 27/27; Gate 03 29/29; suite completa 326/326.
- Clean checkout en `ed470d6` aprobado.
- No retrieval, no BM25, no materialización H150/H200.

### Estado Gate 03

- `NHG03-F001=VERIFIED_RESOLVED`.
- `NHG03-F002=VERIFIED_RESOLVED`.
- `GATE03_CANDIDATE_APPROVED_FOR_MAIN_INTEGRATION=true`.
- `EXP11B_SELECTION_FROZEN=true`.
- `EXP11B_AUTHORIZED=false`.
- `EXP12_AUTHORIZED=false`.
- `GROUP3_STARTED=false`.

**Siguiente paso:** integrar `ed470d67315f505cb3bde471177268db6d16a676` por fast-forward a `main`, validar post-integración y recién después abrir `EXP11B_BANK_MATERIALIZATION_GATE` para materializar los 10 H150 + 10 H200 sin retrieval.

## 8. EXP-11B

Objetivos nominales:
- H150 ≈ 4,425 series.
- H200 ≈ 5,900 series.

Estado: selección prospectiva congelada en candidato Gate 03. `EXP11B_AUTHORIZED=false` hasta cerrar Gate 03 en main y cerrar un gate separado de materialización/hash de los 20 bancos.

## 9. EXP-12

Estado: `CONDITIONAL_FROZEN_PENDING_NEW_HISTORICAL_GATE`.

## 10. Orden maestro actual

```text
Grupo 1 ✅
  ↓
Grupo 2A ✅
  ↓
EXP-11A ✅
  ↓
Forensic Audit 01 ✅
  ↓
Gate 02 ✅
  ↓
Real Ingest 01 ✅
  ↓
Gate 03 microclose ed470d6 ✅ auditoría externa
  ↓
Gate 03 fast-forward a main ⏳
  ↓
EXP11B_BANK_MATERIALIZATION_GATE — 20 bancos, sin retrieval
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
