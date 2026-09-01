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
11. No se reabre Grupo 1 salvo evidencia objetiva nueva de severidad suficiente.
12. EXP-11A no permite inferir un efecto causal aislado del tamaño del banco.
13. Toda nueva data histórica debe seguir el flujo **Excel fuente → Python versionado → dataset derivado → auditoría → hashes → gate**. No se construyen CSV finales manualmente.

## 2. Estado del plan de auditoría

| Grupo | Estado |
|---|---|
| 1. Diseño y ejecución experimental | **CLOSED / APPROVED** |
| 2. Reproducibilidad y trazabilidad | **EN CURSO — Gate 02 cerrado; Real Ingest 01 completado y auditado externamente para freeze; siguiente: Gate 03 freeze del pool elegible + diseño H150/H200** |
| 3. Métricas e inferencia | Pendiente |
| 4. Análisis e interpretación | Pendiente |
| 5. Presentación de resultados | Pendiente |
| 6. Figuras y visualizaciones | Pendiente |
| 7. Redacción científica | Pendiente |
| 8. Coherencia metodológica/documental | Pendiente |

## 3. Benchmark v0.2 congelado

- Histórico H100: **2,950 series / 28 DAM / 66 códigos**.
- Desarrollo: **100 series / 6 DAM**.
- Evaluación: **1,056 series / 67 DAM / 42 códigos**.
- H100 SHA-256: `0990cdfe2a62638bff83a1182b0d6b0b727d670f63888044e99fd3ee0d7915ff`.
- DEV SHA-256: `434e08f13ed3d5529165abbd0e139b5a675e7dc164307a624caa95f60a271f00`.
- EVAL SHA-256: `3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941`.

H100 histórico: Top-1 0.509470; Top-3 0.671402; Top-5 0.763258; Top-10 0.891098; Top-50 0.991477; MRR 0.629708.

## 4. Grupo 1

**CLOSED / APPROVED.**

## 5. Grupo 2A

**CLOSED / APPROVED_WITH_NONBLOCKING_LIMITATIONS.**

Commit final G2A: `a6140b66cf2975313be327d6d3d4e18e38f1fdf5`.

F001 `PARTIALLY_RESOLVED`; F002 `NOT_RECOVERABLE`; F003 `PARTIALLY_RESOLVED`; F004 `PARTIALLY_RESOLVED`; F005 `NOT_RECOVERABLE`; F006 `VERIFIED_IN_G2`; F007 `OPEN / FUTURE_DEPENDENCY`; F008 `VERIFIED_IN_G2`; F009 `VERIFIED_IN_G2 / DECLARED_LIMITATION`; F010 `VERIFIED_IN_G2`.

## 6. EXP-11A — cierre definitivo

**CLOSED / APPROVED / VERSIONED / INTEGRATED TO MAIN.**

`main = origin/main = 9e8af129ca586bd1929e6afe6aa1a1c64d8fe667`.

- H25=10, H50=10, H75=10, H100=1 referencia.
- H50=5 D1 / 5 D2.
- H100 Gate PASS.
- 32,736 filas case-level.
- Sin rerun/resume.
- Freeze de 47 artefactos; 0 hash mismatches.
- Tests finales 13/13 y 270/270.
- HE2/HE5 permanecen pendientes de Grupo 3.

Resultados descriptivos:

| Condición | Top-3 | MRR |
|---|---:|---:|
| H25 | 0.645170 ± 0.051964 | 0.603787 ± 0.047775 |
| H50 | 0.597917 ± 0.066393 | 0.542492 ± 0.060405 |
| H75 | 0.463352 ± 0.132774 | 0.414030 ± 0.126668 |
| H100 | 0.671402 | 0.629708 |

## 7. NEW_HISTORICAL_GATE — Forensic Audit 01

**EXTERNAL AUDIT: APPROVED_WITH_TERMINOLOGY_CORRECTIONS.**

- Excel fuente actual congelado/reproductor H100: SHA `db01d1fcdd41d1bd1ed8086fc6c19bcd56ba44b2534391aba7daa4c58f9f52d1`.
- `Hoja2` fue la hoja históricamente procesada; `Hoja1` es preexistente no procesada.
- Pipeline Excel→Python→v0.1→v0.2 parcialmente reconstruido con reproducción byte-exacta de H100/DEV/EVAL.

## 8. NEW_HISTORICAL_GATE — Gate 02

**CLOSED / APPROVED / INTEGRATED TO MAIN.**

`main = origin/main = ad4c630a6a4d442776740b59b9552ba72141ea48`.

- Fuente actual congelada byte-a-byte.
- Contrato multi-hoja integrado.
- Conjuntos permitidos: `["NUEVA_01"]` o `["NUEVA_01","NUEVA_02"]`.
- Selección futura explícita por `--sheet`.
- H100/DEV/EVAL inmutables.
- Pipeline prospectivo: `PARSE → COMBINE → CLASSIFY/CURATE → FROZEN DAM/ID AUDIT → ELIGIBLE → EXACT/NEAR → CAPACITY → OUTPUTS/MANIFEST`.
- Tests: 27/27 Gate02; 297/297 suite.

## 9. Real Ingest 01 — NUEVA_01

**Estado externo:** `APPROVED_FOR_FREEZE_AND_GATE03_DESIGN`.

- `NHG_REAL01-F001=VERIFIED_RESOLVED`: única diferencia literal de Hoja2 fue `__source_file` en 11,320 filas; igualdad funcional confirmada.
- `NHG_REAL01-F002=VERIFIED_RESOLVED`: invocación directa por path sustituyó al `-m` inválido sin cambiar código.
- Fuente ampliada congelada:
  - `Series - Descripciones_EXPANDED_NUEVA_01_SOURCE_087efd97.xlsx`
  - SHA `087efd97cb17fd166c2e7eb5089690577491e99ab5d415f9e3a8614923ee4ba3`
  - 16,060,154 bytes.
- `SOURCE_PREEXISTING_SHEETS_UNCHANGED=true`.
- `validate-new-sheets=PASS`.
- NUEVA_01: 15,596 series parseadas; 6,029 Clase 87; 6,029 final elegibles.
- 0 DAM DEV/EVAL excluidas; 0 overlaps `id_unico` congelados.
- Pool nuevo: **6,029 filas / 43 DAM / 56 NANDINA**.
- Largest DAM = 990 (16.42%); HHI = 0.08755655; effective DAM = 11.4212.
- 45/66 códigos H100 presentes (68.18%); 11 códigos nuevos.
- `H100 + NEW_ELIGIBLE`: 8,979 filas / 71 DAM / 77 NANDINA; HHI = 0.06496386; effective DAM = 15.3932; largest DAM share 11.64%.
- Capacidad: `H150_AND_H200_FEASIBLE`.
- Exact/near descriptions permanecen descriptores, no exclusiones:
  - vs H100: exact 1,364; near 0.90/0.95/0.98 = 1,394/1,379/1,367;
  - vs DEV: 0;
  - vs EVAL: exact 23; near = 70/45/32.
- 7/7 artefactos listados verificados; 0 mismatches.
- H100/DEV/EVAL hashes preservados.
- Sin retrieval, sin H150/H200 materializados.

## 10. NEW HISTORICAL GATE 03 — siguiente hito

Gate 03 debe:

1. congelar/versionar los outputs de Real Ingest 01 y un manifest durable de la fuente ampliada;
2. congelar SHA de `new_historical_eligible.csv`;
3. diseñar H150/H200 **antes de retrieval**, usando únicamente composición del banco;
4. preservar DAM completas;
5. prohibir uso de labels/performance del eval para selección;
6. materializar H150/H200 solo después de aprobar externamente el diseño;
7. definir prospectivamente el análisis complementario de exact/near duplicates contra el máximo banco disponible, manteniendo 1,056 casos como denominador primario.

`EXP11B_AUTHORIZED=false` hasta cerrar Gate 03.

## 11. EXP-11B

Objetivos nominales:
- H150 ≈ 4,425 series.
- H200 ≈ 5,900 series.

H100 permanece como núcleo exacto de 2,950 filas.

## 12. EXP-12

Estado: `CONDITIONAL_FROZEN_PENDING_NEW_HISTORICAL_GATE`.

## 13. Orden maestro actual

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
Real Ingest 01 NUEVA_01 ✅
  ↓
Gate 03: freeze pool + diseño H150/H200 ⏳
  ↓
EXP-11B H150/H200
  ↓
EXP-12
  ↓
Grupo 2B
  ↓
Grupo 3
  ↓
Grupos 4–8
```
