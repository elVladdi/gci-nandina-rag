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
| 2. Reproducibilidad y trazabilidad | **EN CURSO — Real Ingest 01 congelado en candidato Gate 03; selección H150/H200 prospectiva válida; microclose requerido para descriptores del banco total y denominadores common-clean antes de integrar** |
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

**APPROVED_FOR_FREEZE_AND_GATE03_DESIGN.**

- F001 `VERIFIED_RESOLVED`: única diferencia histórica parser = `__source_file`.
- F002 `VERIFIED_RESOLVED`: invocación directa por path para archivo `v0.1.py`.
- Fuente ampliada congelada: SHA `087efd97cb17fd166c2e7eb5089690577491e99ab5d415f9e3a8614923ee4ba3`, 16,060,154 bytes.
- NUEVA_01: 15,596 parseadas; 6,029 Clase 87; 6,029 elegibles.
- Pool nuevo: 6,029 filas / 43 DAM / 56 NANDINA.
- H100+new máximo: 8,979 filas / 71 DAM / 77 NANDINA.
- Capacidad: `H150_AND_H200_FEASIBLE`; `NUEVA_02_REQUIRED=false`.
- Sin retrieval; sin H150/H200 materializados.

## 7. Gate 03 candidato

Rama: `codex/new-historical-gate-expanded-pool-v01`  
Candidato: `b3806190cb645d35c2a121c0f1d0c07fbfe21605`  
Base `main`: `ad4c630a6a4d442776740b59b9552ba72141ea48`  
Relación: 1 commit delante / 0 detrás.

### Elementos aprobados

- Real Ingest 01 versionado y congelado.
- `new_historical_eligible.csv` SHA: `a78e8c517d50f53fa0f8b95a6c94f841dda4c0e3e5cf28cc4c4fccc576c083a4`.
- H100/new DAM overlap = 0.
- Planner prospectivo usa solo DAM id + row count + seed + namespace.
- DAM completas, H100 fijo, H150 estrictamente anidado en H200, tolerancia ±148.
- 24 seeds evaluados; 10 pares válidos.
- Seeds aceptados exactos: `20261005, 20261006, 20261007, 20261010, 20261011, 20261013, 20261017, 20261021, 20261023, 20261024`.
- Common-clean sobre máximo pool: afectados exact=36; near90=75; near95=54; near98=46.
- Primario permanece N=1056.
- Tests reportados: Gate02 27/27, Gate03 19/19, suite 316/316.
- No retrieval; H150/H200 no materializados.

### NHG03-F001 — TOTAL_BANK_DESCRIPTORS_MISSING — S2

El artefacto de factibilidad calcula el `descriptor` solo sobre las DAM incrementales de `NEW_ELIGIBLE`. Los bancos reales serán `H100_FROZEN + selected_new_DAMs`; por tanto, antes de integrar Gate 03 se deben congelar, sin alterar selección ni seeds:

- `increment_descriptor`;
- `total_bank_descriptor`;
- total DAM count;
- HHI/effective DAM del banco total;
- largest DAM share total;
- NANDINA total;
- H100 NANDINA coverage;
- new NANDINA count.

La corrección es descriptiva y no puede cambiar las composiciones aceptadas.

### NHG03-F002 — COMMON_CLEAN_DENOMINATORS_NOT_EXPLICIT — S2

Congelar explícitamente:

- `N_PRIMARY=1056`
- `N_EXACT_CLEAN=1020`
- `N_NEAR090_CLEAN=981`
- `N_NEAR095_CLEAN=1002`
- `N_NEAR098_CLEAN=1010`

Las máscaras existentes no cambian.

**Gate 03 todavía no se integra a main.**

## 8. EXP-11B

Objetivos nominales:
- H150 ≈ 4,425 series.
- H200 ≈ 5,900 series.

Estado: diseño prospectivo candidato existe, pero `EXP11B_AUTHORIZED=false` hasta cerrar Gate 03 y materializar bancos en un gate separado.

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
Gate 03 candidato b380619 ⚠ microclose F001/F002
  ↓
Gate 03 integración
  ↓
Materialización H150/H200 sin retrieval
  ↓
EXP-11B
  ↓
EXP-12
  ↓
Grupo 2B
  ↓
Grupo 3
  ↓
Grupos 4–8
```
