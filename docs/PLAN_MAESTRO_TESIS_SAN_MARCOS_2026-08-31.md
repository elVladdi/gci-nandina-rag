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
| 2. Reproducibilidad y trazabilidad | **EN CURSO — Gate 03 CLOSED e integrado; siguiente: EXP11B_BANK_MATERIALIZATION_GATE sin retrieval** |
| 3. Métricas e inferencia | Pendiente |
| 4–8 | Pendientes |

## 3. Benchmark congelado

- H100: 2,950 filas / 28 DAM / 66 NANDINA; SHA `0990cdfe2a62638bff83a1182b0d6b0b727d670f63888044e99fd3ee0d7915ff`.
- DEV: 100 filas; SHA `434e08f13ed3d5529165abbd0e139b5a675e7dc164307a624caa95f60a271f00`.
- EVAL: 1,056 filas; SHA `3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941`.
- H100: Top-1 0.509470; Top-3 0.671402; Top-5 0.763258; Top-10 0.891098; Top-50 0.991477; MRR 0.629708.

## 4. Cierres previos

- Grupo 1: **CLOSED / APPROVED**.
- Grupo 2A: **CLOSED / APPROVED_WITH_NONBLOCKING_LIMITATIONS**.
- EXP-11A: **CLOSED / APPROVED / INTEGRATED** en `9e8af129ca586bd1929e6afe6aa1a1c64d8fe667`.
- Gate 02 multi-hoja: **CLOSED / APPROVED / INTEGRATED** en `ad4c630a6a4d442776740b59b9552ba72141ea48`.

## 5. Real Ingest 01 — NUEVA_01

**APPROVED / FROZEN.**

- Fuente ampliada SHA `087efd97cb17fd166c2e7eb5089690577491e99ab5d415f9e3a8614923ee4ba3`.
- 15,596 series parseadas.
- 6,029 Clase 87 y 6,029 elegibles.
- Pool nuevo: 6,029 filas / 43 DAM / 56 NANDINA.
- Pool elegible SHA `a78e8c517d50f53fa0f8b95a6c94f841dda4c0e3e5cf28cc4c4fccc576c083a4`.
- H100/new DAM overlap = 0.
- Pool máximo H100+new = 8,979 filas / 71 DAM / 77 NANDINA.
- H150 y H200 son factibles; NUEVA_02 no es necesaria.

## 6. NEW HISTORICAL GATE 03

**CLOSED / APPROVED / INTEGRATED TO MAIN.**

`main = origin/main = ed470d67315f505cb3bde471177268db6d16a676`.

Cadena Gate 03:

1. `b3806190cb645d35c2a121c0f1d0c07fbfe21605` — freeze del pool elegible + diseño EXP-11B.
2. `ed470d67315f505cb3bde471177268db6d16a676` — descriptores del banco total + denominadores common-clean.

### Diseño EXP-11B congelado

- H100 es núcleo fijo.
- Unidad de selección: DAM completa.
- Selección usa solo DAM id + row count + seed + namespace.
- No usa NANDINA, descripción, eval, performance, BM25 ni duplicados.
- H150 estrictamente anidado en H200 por réplica.
- Tolerancia: ±148 filas del incremento nominal.
- 24 seeds evaluados; 10 pares aceptados.
- Seeds exactos: `20261005, 20261006, 20261007, 20261010, 20261011, 20261013, 20261017, 20261021, 20261023, 20261024`.
- 20/20 composiciones H150/H200 preservadas contra baseline `b380619`.
- Cada condición tiene `increment_descriptor` y `total_bank_descriptor`.
- Todos los bancos totales preservan cobertura H100 66/66.

### Common-clean congelado

- N primary = 1056.
- Masked: exact 36; near090 75; near095 54; near098 46.
- Clean: exact 1020; near090 981; near095 1002; near098 1010.
- La máscara no afecta selección ni denominador primario.

### Validación final Gate 03

- Real Ingest freeze: 9 artefactos, 0 mismatches.
- H100/DEV/EVAL sin cambios.
- Gate 02 tests: 27/27.
- Gate 03 tests: 29/29.
- Suite completa: 326/326.
- Clean checkout post-main: PASS.
- No retrieval, no BM25, no H150/H200 materializados.

Flags:

- `NEW_HISTORICAL_GATE_03_STATUS=CLOSED`
- `REAL_INGEST_01_FROZEN=true`
- `NEW_ELIGIBLE_POOL_FROZEN=true`
- `EXP11B_SELECTION_FROZEN=true`
- `COMMON_CLEAN_POLICY_FROZEN=true`
- `H150_MATERIALIZED=false`
- `H200_MATERIALIZED=false`
- `RETRIEVAL_EXECUTED=false`
- `EXP11B_AUTHORIZED=false`
- `EXP12_AUTHORIZED=false`
- `GROUP3_STARTED=false`

## 7. Próximo hito obligatorio — EXP11B_BANK_MATERIALIZATION_GATE

Objetivo: materializar físicamente los 10 bancos H150 y 10 H200 **sin ejecutar retrieval**.

Cada banco debe construirse exactamente como:

`H100_FROZEN + filas NEW_ELIGIBLE de las DAM congeladas para esa réplica/condición`.

El gate debe verificar:

- H100 como núcleo exacto;
- DAM nuevas exactas, sin extras ni faltantes;
- row count realizado;
- composition SHA de DAM;
- nesting H150⊂H200 por réplica;
- descriptores incrementales y totales;
- cobertura H100 66/66;
- hashes de los 20 CSV;
- manifest e inventario;
- clean checkout;
- no BM25/retrieval.

Solo después de auditoría externa del gate de materialización podrá cambiarse `EXP11B_AUTHORIZED=true`.

## 8. Orden maestro

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
Gate 03 ✅ CLOSED / INTEGRATED ed470d6
  ↓
EXP11B_BANK_MATERIALIZATION_GATE ⏳ sin retrieval
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
