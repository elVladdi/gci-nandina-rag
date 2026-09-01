# Plan maestro canónico — Tesis San Marcos

**Proyecto:** Framework RAG explicativo y auditable para recomendación de subpartidas NANDINA  
**Fecha de actualización:** 2026-09-01

## 1. Principios congelados

1. SERIE es la unidad de análisis.
2. DAM/DECLARACIÓN es la unidad de agrupamiento cuando existe dependencia.
3. Recuperación histórica = ranking principal; recuperación normativa = evidencia; LLM local = explicación del Top-3 fijo.
4. Evalset v0.2 fijo: 1,056 casos.
5. No se cambian reglas experimentales después de observar resultados.
6. Nueva data histórica: Excel fuente → Python versionado → dataset derivado → auditoría → hashes → gate.
7. EXP-11A/11B no se interpretan como efecto causal aislado del tamaño cuando cambia la composición.

## 2. Estado general

| Grupo | Estado |
|---|---|
| 1. Diseño y ejecución experimental | **CLOSED / APPROVED** |
| 2. Reproducibilidad y trazabilidad | **EN CURSO — materialization candidato 7a80b1d reproducido 20/20; F002 re-clasificado como portabilidad numérica; F001/F003 pendientes** |
| 3. Métricas e inferencia | Pendiente |
| 4–8 | Pendientes |

## 3. Cierres previos

- Grupo 2A: **CLOSED / APPROVED_WITH_NONBLOCKING_LIMITATIONS**.
- EXP-11A: **CLOSED / APPROVED / INTEGRATED** en `9e8af129ca586bd1929e6afe6aa1a1c64d8fe667`.
- Gate 02: **CLOSED / APPROVED / INTEGRATED** en `ad4c630a6a4d442776740b59b9552ba72141ea48`.
- Gate 03: **CLOSED / APPROVED / INTEGRATED** en `ed470d67315f505cb3bde471177268db6d16a676`.

## 4. Real Ingest 01 y diseño EXP-11B

- Pool elegible SHA `a78e8c517d50f53fa0f8b95a6c94f841dda4c0e3e5cf28cc4c4fccc576c083a4`.
- 6,029 filas / 43 DAM / 56 NANDINA.
- H100/new DAM overlap = 0.
- H100 núcleo fijo: 2,950 filas / 28 DAM / 66 NANDINA.
- 10 pares H150/H200 congelados; H150 estrictamente anidado en H200.
- Seeds: `20261005, 20261006, 20261007, 20261010, 20261011, 20261013, 20261017, 20261021, 20261023, 20261024`.
- Common-clean: primary 1056; exact 1020; near090 981; near095 1002; near098 1010.

## 5. EXP11B_BANK_MATERIALIZATION_GATE — candidato

Rama: `codex/exp11b-bank-materialization-v01`  
Candidato: `7a80b1db657386705d3031559c2861d0a2f88eb2`  
Base/main: `ed470d67315f505cb3bde471177268db6d16a676`.

### Validado

- 10 H150 + 10 H200 materializados localmente.
- H100 core 20/20 PASS.
- selección Gate03 20/20 PASS.
- descriptores 20/20 PASS bajo tolerancia numérica del contrato.
- nesting 10/10 PASS.
- 20 bank SHA congelados.
- clean checkout reprodujo 20/20 byte exacto.
- CSV de bancos no versionados; manifest/hash inventory sí.
- no retrieval/BM25/métricas.

### Hallazgos pendientes

`EXP11B-MAT-F001 = DEV_EVAL_PROVENANCE_NOT_HASH_FROZEN / S2`

DEV/EVAL son inputs efectivos del control de overlap. Deben fijarse SHA y row count en config/manifest y validarse fail-closed.

`EXP11B-MAT-F003 = HASH_INVENTORY_VERIFY_NOT_FAIL_CLOSED / S2`

`verify()` debe comparar campo por campo el inventario SHA con bancos/manifest, no solo bank_id y cardinalidad.

### MAT-F002 re-clasificado

El intento de restaurar igualdad exacta del HHI Gate03 falló en Python 3.12.13:

- congelado: `0.13446841032608695`;
- recomputado: `0.13446841032608697`;
- delta real: `2.7755575615628914e-17` = **1 ULP**.

Python 3.12 cambió el algoritmo de `sum()` para floats, por lo que igualdad bit-a-bit entre runtimes no es un contrato portable.

Nuevo estado:

`EXP11B-MAT-F002 = GATE03_FLOAT_SUM_PORTABILITY_DEFECT / S2_PROCEDURAL`.

Resolución autorizada: comparación con `rel_tol=0` y `abs_tol=1e-12`, consistente con el materializer, sin reescribir feasibility, sin cambiar selección y sin cambiar ninguno de los 20 bank SHA.

## 6. Estado actual

- `main = origin/main = ed470d67315f505cb3bde471177268db6d16a676`.
- rama candidata sigue en `7a80b1db657386705d3031559c2861d0a2f88eb2`.
- no commit correctivo todavía.
- MAT-F001/MAT-F003 aún no ejecutados.
- bancos canónicos intactos.
- `EXP11B_RETRIEVAL_AUTHORIZED=false`.
- `RETRIEVAL_EXECUTED=false`.
- `EXP12_AUTHORIZED=false`.
- `GROUP3_STARTED=false`.

## 7. Orden maestro

```text
Gate 03 ✅ CLOSED / INTEGRATED ed470d6
  ↓
EXP11B_BANK_MATERIALIZATION candidato 7a80b1d
  ↓
Microclose: F002 portabilidad float + F001 provenance + F003 hash verify ⏳
  ↓
Auditoría externa / integración materialization gate
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
