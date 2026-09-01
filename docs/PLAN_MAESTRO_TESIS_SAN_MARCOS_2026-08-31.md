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
| 2. Reproducibilidad y trazabilidad | **EN CURSO — EXP11B Bank Materialization CLOSED e integrado en `main` (`95ffec45`); reproducción post-push 20/20 y suite 368/368; solo limpieza local de worktree pendiente, no científica** |
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

**CLOSED / APPROVED / INTEGRATED TO MAIN.**

Cadena:

1. `7a80b1db657386705d3031559c2861d0a2f88eb2` — materialización y freeze de las 20 identidades de banco.
2. `95ffec45ae5a734545ae7bb2d8d530f42f8f056c` — procedencia DEV/EVAL, portabilidad float y verificación fail-closed del ledger.

Estado remoto verificado:

`main = origin/main = 95ffec45ae5a734545ae7bb2d8d530f42f8f056c`.

### Materialización congelada

- 10 H150 + 10 H200.
- H100 core: 20/20 PASS.
- selección Gate03: 20/20 PASS.
- descriptores: 20/20 PASS.
- nesting: 10/10 PASS.
- Los 20 CSV no se versionan en Git; son derivados deterministas regenerables.
- Bank identities, manifest y ledger sí están congelados.
- Los 20 bank SHA, tamaños, filas, composition SHA y hashes de orden de IDs permanecen fijos.

### Findings cerrados

- `EXP11B-MAT-F001=VERIFIED_RESOLVED`: DEV/EVAL pinneados por SHA y row count y registrados con SHA esperado/observado.
- `EXP11B-MAT-F002=VERIFIED_RESOLVED`: política float `rel_tol=0`, `abs_tol=1e-12`; diferencia observada 1 ULP en Python 3.12.13 sin cambio científico.
- `EXP11B-MAT-F003=VERIFIED_RESOLVED`: `--verify` compara las 14 columnas del ledger por bank_id y falla ante corrupción.

### Validación final post-push

- Gate02: 27/27.
- Gate03: 30/30.
- Materialization: 41/41.
- Suite completa: 368/368.
- Clean checkout post-push: PASS.
- Rematerialización temporal: **20/20 byte exacta, 0 discrepancias**.
- `retrieval_executed=false`.
- `evaluation_metrics_computed=false`.

Flags:

- `EXP11B_BANK_MATERIALIZATION_STATUS=CLOSED`.
- `BANK_MATERIALIZATION_IN_MAIN=true`.
- `BANK_IDENTITIES_FROZEN=true`.
- `BANK_IDENTITIES_MATCH=20/20`.
- `BANKS_BYTE_REPRODUCIBLE=true`.
- `H100_CORE_MATCH_ALL=true`.
- `SELECTION_MATCH_ALL=true`.
- `DESCRIPTORS_MATCH_ALL=true`.
- `NESTING_MATCH_ALL=true`.
- `EXP11B_RETRIEVAL_AUTHORIZED=false`.
- `EXP12_AUTHORIZED=false`.
- `GROUP3_STARTED=false`.

### Limpieza local pendiente

Codex dejó comprobado que el worktree post-push estaba limpio. Solo falta retirarlo con `git worktree remove <ruta>` y ejecutar `git worktree prune`, sin `--force`. Esta tarea es **operativa y no científica**; no bloquea el cierre del gate. Si Windows conserva metadatos huérfanos por permisos pero el worktree ya no aparece en `git worktree list`, se registra como limitación local no científica.

## 7. Próximo hito científico — EXP11B Retrieval Execution Gate

Antes de ejecutar BM25 debe congelarse prospectivamente:

- commit integrado `95ffec45...`;
- SHA del manifest de materialización;
- SHA del ledger de los 20 bancos;
- los 20 bank SHA;
- EVAL SHA;
- configuración BM25 exacta;
- normalización/tokenización;
- valores k;
- outputs y manifest esperados;
- ejecución única/fail-closed;
- denominador primario `N=1056`;
- common-clean solo como sensibilidad complementaria.

`EXP11B_RETRIEVAL_AUTHORIZED=false` hasta que ese gate sea auditado externamente.

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
Gate 03 ✅
  ↓
EXP11B Bank Materialization ✅ CLOSED / INTEGRATED 95ffec45
  ↓
EXP11B Retrieval Execution Gate ⏳
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
