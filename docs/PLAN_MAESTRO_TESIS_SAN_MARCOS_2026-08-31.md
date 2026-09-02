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
| 2. Reproducibilidad y trazabilidad | **EN CURSO — EXP11B Bank Materialization CLOSED e integrado en `main` (`95ffec45`); reproducción post-push 20/20 y 368/368; solo limpieza local de worktree pendiente, no científica** |
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

Estado:

- `FORENSIC_EXCEL_PIPELINE_AUDIT_COMPLETED=true`.
- Excel actual: `data/Series - Descripciones.xlsx`.
- SHA actual antes/después: `db01d1fcdd41d1bd1ed8086fc6c19bcd56ba44b2534391aba7daa4c58f9f52d1`.
- Tamaño: `7,895,186` bytes.
- Hojas: índice 0 `Hoja2` (126,524×9), índice 1 `Hoja1` (41,578×10).
- Hoja activa actual: `Hoja1`.
- Hoja procesada históricamente: `Hoja2`, índice 0, por **default first worksheet**, sin `--sheet`.
- El parser usa `openpyxl.load_workbook(..., read_only=True, data_only=True)`.
- `__sheet_name` del intermedio histórico: únicamente `Hoja2`.
- Intermedio reproducido: 107 DAM / 11,320 series.
- Clase 87: 4,232 filas; 4,106 curadas.
- v0.1: split por fila, estratificado por NANDINA, seed 2026, tamaños 3000/100/1006.
- v0.2: unión de v0.1 y **asignaciones explícitas de DAM** de la configuración T5-safe-159.
- H100/DEV/EVAL v0.2 se reprodujeron byte a byte.
- Clasificación conservadora: `PIPELINE_PARTIALLY_RECONSTRUCTED`.

### Correcciones terminológicas de auditoría externa

1. El workbook histórico completo **no es byte-identificable** con el workbook actual: la metadata histórica registra SHA `cfc85f3d…`, mientras el actual es `db01d1fc…`.
2. La reproducción byte-exacta demuestra **equivalencia funcional del contenido procesado para el parser**, no identidad binaria de la hoja ni del workbook histórico completo.
3. En v0.2, el `seed=2026` queda como atributo de configuración/procedencia; el script materializa el split desde **listas explícitas de DAM** y no usa aleatoriedad para decidir la asignación v0.2.
4. `build_evalset_from_sunat_excel.py` no se reutilizará para la expansión histórica: es un flujo distinto y produce otro esquema, aunque su modo `sunat-block` sea capaz de iterar varias hojas.

### Consecuencia para las nuevas pestañas

El parser histórico actual procesa **una sola hoja por invocación**. Si no se pasa `--sheet`, procesa `workbook.worksheets[0]`. Por tanto, nuevas pestañas no se incorporan automáticamente.

## 8. NEW_HISTORICAL_GATE — Gate 02: freeze fuente + contrato multi-hoja

**CLOSED / APPROVED / INTEGRATED TO MAIN.**

Rama:
`codex/new-historical-gate-source-contract-v01`

Cadena candidata sobre `main=9e8af129...`:

1. `7a7153e6e8bebbc00486bd33e32613209b5febda` — freeze inicial y contrato candidato.
2. `ad4c630a6a4d442776740b59b9552ba72141ea48` — microclose correctivo prospectivo.

El candidato final está exactamente **2 commits delante y 0 detrás** de main y añade cinco artefactos versionados:
- protocolo multi-hoja;
- contrato JSON;
- script prospectivo de ingesta;
- tests Gate 02;
- manifiesto versionado de freeze de fuente.

### Hallazgos Gate 02

- `NHG02-F001 = VERIFIED_RESOLVED`
- `NHG02-F002 = VERIFIED_RESOLVED`
- `NHG02-F003 = VERIFIED_RESOLVED`
- `NHG02-F004 = VERIFIED_RESOLVED`
- `NHG02-F005 = VERIFIED_RESOLVED`

### Contrato prospectivo aprobado

- Fuente clasificada `CURRENT_H100_REPRODUCING_SOURCE`.
- SHA fuente/copia archivada: `db01d1fcdd41d1bd1ed8086fc6c19bcd56ba44b2534391aba7daa4c58f9f52d1`.
- `preexisting_source_sheets = ["Hoja2", "Hoja1"]`.
- `historically_processed_sheet = "Hoja2"`, índice 0.
- `Hoja1 = PREEXISTING_UNPROCESSED_SOURCE_SHEET`.
- Conjuntos nuevos válidos:
  - `["NUEVA_01"]`;
  - `["NUEVA_01", "NUEVA_02"]`.
- `NUEVA_02` sola falla.
- La selección futura es siempre explícita mediante `--sheet`.
- Pipeline congelado:
  `PARSE → COMBINE → CLASSIFY/CURATE → FROZEN DAM/ID AUDIT → ELIGIBLE → EXACT/NEAR → CAPACITY → OUTPUTS/MANIFEST`.
- `classify_rows(..., scope_class="87")` se reutiliza sobre el conjunto combinado.
- DAM DEV/EVAL e `id_unico` congelado se auditan de forma independiente.
- Near duplicate 0.90/0.95/0.98 = descriptores, no exclusión automática.
- Umbrales de capacidad:
  - H150: 1,475 nuevas filas elegibles netas;
  - H200: 2,950 nuevas filas elegibles netas.
- El modo `--ingest-new-data` no construye H150/H200 y no ejecuta retrieval/BM25.
- Tests Gate 02: 27/27.
- Suite total: 297/297.

### Limitaciones no bloqueantes a vigilar en la ejecución real

1. El path futuro verifica el **orden y nombres** de las hojas preexistentes, pero no calcula por sí mismo una huella semántica de su contenido. Esto no afecta H100 —que nunca se reconstruye desde el workbook ampliado y permanece congelado—, pero la ejecución real debe verificar procedimentalmente que `Hoja2` y `Hoja1` no fueron editadas al añadir nuevas hojas.
2. `execution_commit` se registra desde Git. En la ejecución real se exigirá además working tree limpio y commit conocido antes de observar/procesar la nueva data.

Estas dos limitaciones no cambian la semántica del pipeline prospectivo ni requieren otro cambio de código antes de integrar Gate 02.

### Estado

- `NEW_HISTORICAL_GATE_02_STATUS=CLOSED`.
- `main = origin/main = ad4c630a6a4d442776740b59b9552ba72141ea48`.
- `CURRENT_H100_REPRODUCING_SOURCE_FROZEN=true`.
- `MULTISHEET_CONTRACT_FROZEN=true`.
- `MULTISHEET_CONTRACT_IN_MAIN=true`.
- `NEW_HISTORICAL_DATA_PROCESSED=false`.
- `NEW_SHEETS_ADDED=false`.
- `EXP11B_AUTHORIZED=false`.
- `EXP12_AUTHORIZED=false`.

**Siguiente paso autorizado: el usuario puede agregar `NUEVA_01` al final del workbook actual, preservando sin cambios `Hoja2` y `Hoja1`. `NUEVA_02` solo se añadirá si la cantidad de nueva data requiere una segunda hoja.**

## 9. EXP-11B

Objetivos:

- H150 ≈ 4,425 series.
- H200 ≈ 5,900 series.

H100 debe permanecer exactamente preservado como núcleo del histórico ampliado.

Para capacidad H200 se necesitan al menos **2,950 series nuevas elegibles netas** sobre H100; esta es una condición post-procesamiento, no un número bruto de filas Excel.

## 10. EXP-12

Estado: `CONDITIONAL_FROZEN_PENDING_NEW_HISTORICAL_GATE`.

Mantener HHI primario, volumen 2,950±148, cobertura H100=1.0, TVD≤0.05, 10,000 candidatos/seed, mínimo 30 factibles, cuantiles 0.10/0.50/0.90 y `must_not_fallback_to_h100=true`.

## 11. Grupo 2B

Después de EXP-11B/EXP-12: manifests, hashes, configs, seeds, scripts, logs, case-level, entorno, clean checkout, matriz end-to-end y nivel final de reproducibilidad.

## 12. Grupos 3–8

Grupo 3 realizará análisis cuantitativo/inferencia y decisión HE2/HE5. Grupos 4–8: interpretación, presentación, figuras, redacción y coherencia documental.

## 13. Orden maestro actual

```text
Grupo 1 ✅
  ↓
Grupo 2A ✅
  ↓
EXP-11A ✅
  ↓
NEW_HISTORICAL_GATE — Forensic Audit 01 ✅
  ↓
Gate 02 ad4c630... ✅ CLOSED / INTEGRATED
  ↓
Usuario agrega NUEVA_01 según contrato ⏳
  ↓
Python valida e ingiere exclusivamente NUEVA_01
  ↓
Gate de capacidad / integridad de nueva data
  ↓
Python procesa exclusivamente nueva(s) hoja(s)
  ↓
NEW_HISTORICAL_GATE de datos ampliados
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
  ↓
Freeze científico
  ↓
Repositorio público / artículos / tesis final
```

## 14. Historial reciente

### 2026-09-01 — Forensic Audit 01 aprobado

- Pipeline Excel→Python→v0.1→v0.2 reconstruido parcialmente con reproducción byte-exacta de outputs.
- Workbook histórico completo no recuperado byte a byte.
- `Hoja2` fue la fuente funcional procesada mediante selección predeterminada de primera hoja.
- El workbook actual permanece intacto con SHA `db01d1fc...`.
- Próximo hito: congelar esa fuente actual reproducente y versionar el contrato de expansión multi-hoja antes de editar el Excel.

### 2026-09-01 — Gate 02 candidato auditado externamente

- Rama candidata `codex/new-historical-gate-source-contract-v01` = `7a7153e6e8bebbc00486bd33e32613209b5febda`.
- `main` permanece `9e8af129ca586bd1929e6afe6aa1a1c64d8fe667`.
- Commit candidato: 1 commit / 4 archivos añadidos.
- Freeze externo de fuente actual: SHA origen=copia `db01d1fc...`; 7,895,186 bytes; Python `shutil.copy2`.
- 17/17 tests nuevos y 287/287 suite reportados.
- Gate 02 **NO cerrado externamente** por cinco hallazgos prospectivos: manifiesto de freeze no versionado, path de ingesta futura no congelado, `NUEVA_02` aceptada sin `NUEVA_01`, masking de razones de overlap y terminología demasiado amplia sobre “historical_sheets”.
- No se autoriza modificar el Excel ni incorporar nueva data hasta resolver y auditar esos hallazgos.

### 2026-09-01 — Gate 02 microclose aprobado externamente

- Candidato final: `ad4c630a6a4d442776740b59b9552ba72141ea48`.
- Relación con main: 2 commits delante, 0 detrás.
- Cinco archivos versionados en el scope Gate 02.
- F001–F005: `VERIFIED_RESOLVED`.
- Manifiesto de freeze versionado y consistente con SHA `db01d1fc...`.
- Path `--ingest-new-data` congelado y probado sintéticamente.
- 27/27 tests Gate 02; 297/297 suite completa.
- Gate 02: **EXTERNAL APPROVAL = true; INTEGRATION TO MAIN = pending**.
- El Excel sigue intacto; nueva data aún no procesada.

### 2026-09-01 — Gate 02 cerrado e integrado

- `main = origin/main = ad4c630a6a4d442776740b59b9552ba72141ea48`.
- Integración fast-forward desde `9e8af129...`, sin merge commit.
- 27/27 tests Gate 02 y 297/297 suite completa en candidata, main y clean checkout.
- H100/DEV/EVAL hashes preservados.
- Fuente congelada `db01d1fc...` preservada.
- `NEW_HISTORICAL_GATE_02_STATUS=CLOSED`.
- `MULTISHEET_CONTRACT_IN_MAIN=true`.
- Se autoriza al usuario a agregar `NUEVA_01` al workbook actual bajo el contrato congelado.
- `NUEVA_02` es opcional y solo debe agregarse si es necesaria por capacidad física/operativa.
- Antes de la ingesta real se verificará que `Hoja2` y `Hoja1` no hayan cambiado respecto de la copia congelada.
- La nueva data se procesará exclusivamente con Python; no se construyen manualmente H150/H200.

### 2026-09-01 — Real Ingest 01 detenido antes de procesar NUEVA_01

- Workbook ampliado: orden corregido `["Hoja2", "Hoja1", "NUEVA_01"]`.
- `HOJA2_CANONICAL_CONTENT_MATCH=true`.
- `HOJA1_CANONICAL_CONTENT_MATCH=true`.
- Coincidencia en `data_only=True` y `data_only=False`; no existen fórmulas.
- Parser Hoja2: mismas columnas y 11,320 filas, pero la igualdad literal de todos los diccionarios devolvió `false`.
- No se congeló el workbook ampliado.
- No se ejecutó `--validate-new-sheets`.
- No se ejecutaron tests de la pasada.
- No se ejecutó `--ingest-new-data`.
- No se generaron outputs de nueva data.
- Código/config/datasets congelados sin cambios.

#### Diagnóstico externo preliminar

El parser incorpora `__source_file = str(source_file)` en cada fila y `parse_workbook()` pasa el `path` del workbook directamente a `parse_series_block`. Por tanto, comparar literalmente filas obtenidas desde el archivo congelado y desde el workbook ampliado **debe producir una diferencia de procedencia en `__source_file` aunque todo el contenido científico sea idéntico**.

Estado provisional:

`NHG_REAL01-F001 = PARSER_PROVENANCE_PATH_FALSE_MISMATCH / OPEN_FORENSIC_CHECK`.

No se autoriza todavía la ingesta. El siguiente paso es una comparación campo-a-campo READ-ONLY. Solo `__source_file` puede diferir. Si cualquier otro campo, fila, orden, warning o metadato funcional difiere, la ingesta seguirá bloqueada. Si la única diferencia es `__source_file`, el control histórico se considerará PASS y podrá continuar la ejecución real sin modificar código.

### 2026-09-01 — Real Ingest 01: F001 resuelto y F002 de invocación CLI

- `NHG_REAL01-F001=VERIFIED_RESOLVED`.
- Única diferencia parser Hoja2: `__source_file` en 11,320 filas.
- Comparación funcional excluyendo exclusivamente `__source_file`: `true`.
- `SOURCE_PREEXISTING_SHEETS_UNCHANGED=true`.
- Workbook ampliado congelado externamente:
  - `Series - Descripciones_EXPANDED_NUEVA_01_SOURCE_087efd97.xlsx`
  - SHA `087efd97...ee4ba3`
  - 16,060,154 bytes.
- La ejecución se detuvo antes de validar/ingerir NUEVA_01 porque el comando `python -m src.ingestion.prepare_new_historical_multisheet_v0.1` es inválido: el punto en el nombre del archivo hace que Python interprete `v0.1` como segmentos de módulo.
- Nuevo hallazgo:
  `NHG_REAL01-F002 = INVALID_PYTHON_MODULE_INVOCATION_FOR_DOTTED_FILENAME`.
- F002 es procedimental y no científico; no requiere cambio de código.
- Resolución autorizada: ejecutar el mismo archivo congelado mediante ruta directa:
  `python src/ingestion/prepare_new_historical_multisheet_v0.1.py ...`
- No se modifica código/configuración ni se renombra el archivo después de observar nueva data.
- Nueva ingesta real sigue pendiente; no existen outputs científicos nuevos.

### 2026-09-01 — Real Ingest 01 completado con NUEVA_01

**Estado externo:** `APPROVED_FOR_FREEZE_AND_GATE03_DESIGN`.

- `NHG_REAL01-F001=VERIFIED_RESOLVED`.
- `NHG_REAL01-F002=VERIFIED_RESOLVED`.
- Fuente ampliada congelada:
  - `Series - Descripciones_EXPANDED_NUEVA_01_SOURCE_087efd97.xlsx`
  - SHA `087efd97cb17fd166c2e7eb5089690577491e99ab5d415f9e3a8614923ee4ba3`
  - 16,060,154 bytes.
- `SOURCE_PREEXISTING_SHEETS_UNCHANGED=true`.
- `validate-new-sheets=PASS`.
- Tests pre/post: 27/27 Gate 02; 297/297 suite.
- NUEVA_01 parseada: 15,596 series.
- Clase 87: 6,029.
- Quality/duplicate policy: 6,029.
- DEV/EVAL DAM exclusions: 0.
- Frozen `id_unico` overlaps: 0.
- Pool final elegible: **6,029 filas / 43 DAM / 56 NANDINA**.
- Composición nueva:
  - largest DAM = 990 (16.42%);
  - HHI = 0.08755655;
  - effective DAM = 11.4212;
  - 45/66 códigos H100 presentes (68.18%);
  - 11 códigos nuevos respecto de H100.
- Pool potencial `H100 + NEW_ELIGIBLE`:
  - 8,979 filas;
  - 71 DAM;
  - 77 NANDINA;
  - HHI = 0.06496386;
  - effective DAM = 15.3932;
  - largest DAM share = 11.64%.
- Capacidad: `H150_AND_H200_FEASIBLE`.
- Exact/near descriptions permanecen descriptores, no exclusiones:
  - vs H100: exact 1,364; near 0.90/0.95/0.98 = 1,394/1,379/1,367;
  - vs DEV: 0;
  - vs EVAL: exact 23; near = 70/45/32.
- 7/7 artefactos listados por el inventario verificados; 0 mismatches.
- H100/DEV/EVAL hashes preservados.
- Sin retrieval, sin H150/H200 materializados, sin cambios científicos.

### Próximo hito: NEW HISTORICAL GATE 03

Gate 03 debe:

1. congelar/versionar los outputs de Real Ingest 01 y un manifest durable de la fuente ampliada;
2. congelar SHA del `new_historical_eligible.csv`;
3. diseñar H150/H200 **antes de retrieval**, usando únicamente composición del banco;
4. preservar DAM completas;
5. prohibir uso de labels/performance del eval para selección;
6. materializar H150/H200 solo después de aprobar externamente el diseño;
7. definir prospectivamente el análisis complementario de exact/near duplicates contra el máximo banco evaluado, manteniendo 1,056 casos como denominador primario.

`EXP11B_AUTHORIZED=false` hasta cerrar Gate 03.

### 2026-09-01 — Gate 03 candidato `b380619` auditado externamente

**Estado:** `APPROVED_WITH_BLOCKING_MICROCLOSE_BEFORE_MAIN`.

- Rama candidata: `codex/new-historical-gate-expanded-pool-v01`.
- Candidato: `b3806190cb645d35c2a121c0f1d0c07fbfe21605`.
- Relación contra `main=ad4c630...`: 1 commit delante, 0 detrás.
- Real Ingest 01 queda congelado en Git:
  - `new_historical_eligible.csv` SHA `a78e8c517d50f53fa0f8b95a6c94f841dda4c0e3e5cf28cc4c4fccc576c083a4`;
  - 6,029 filas / 43 DAM / 56 NANDINA;
  - H100/new DAM overlap = 0.
- Diseño de selección EXP-11B:
  - selección únicamente por DAM id + row count + seed + namespace;
  - H100 fijo;
  - DAM completas;
  - H150 estrictamente anidado en H200;
  - tolerancia ±148;
  - 10 pares válidos tras evaluar 24 seeds;
  - accepted seeds exactos:
    `20261005, 20261006, 20261007, 20261010, 20261011, 20261013, 20261017, 20261021, 20261023, 20261024`.
- No se ejecutó retrieval y H150/H200 no fueron materializados.
- Common-clean:
  - primary N=1056;
  - casos afectados: exact=36, near90=75, near95=54, near98=46;
  - denominadores clean derivados: exact=1020, near90=981, near95=1002, near98=1010.

#### NHG03-F001 — TOTAL_BANK_DESCRIPTORS_MISSING / S2

El planner calcula `descriptor` usando únicamente las DAM incrementales seleccionadas de `NEW_ELIGIBLE`. Esto no representa la composición real de los bancos experimentales futuros, que serán `H100_FROZEN + selected_new_DAMs`.

Antes de integrar Gate 03 se debe agregar, sin cambiar selección/seeds:
- `increment_descriptor` para el subconjunto nuevo;
- `total_bank_descriptor` para H100 + incremento;
- total DAM count;
- HHI/effective DAM del banco total;
- largest DAM share total;
- NANDINA total;
- H100 NANDINA coverage;
- new NANDINA count.

La corrección es descriptiva y no puede alterar ninguna composición aceptada.

#### NHG03-F002 — COMMON_CLEAN_DENOMINATORS_NOT_EXPLICIT / S2

La evidencia conserva los casos afectados pero no congela explícitamente los denominadores clean requeridos. Deben registrarse:
- N_PRIMARY=1056
- N_EXACT_CLEAN=1020
- N_NEAR090_CLEAN=981
- N_NEAR095_CLEAN=1002
- N_NEAR098_CLEAN=1010.

No modifica máscaras ni selección.

**Gate 03 todavía no se integra a main.**

### 2026-09-01 — Gate 03 microclose `ed470d6` aprobado externamente

**Estado:** `APPROVED_FOR_MAIN_INTEGRATION`.

- Candidato corregido: `ed470d67315f505cb3bde471177268db6d16a676`.
- Rama remota `codex/new-historical-gate-expanded-pool-v01` apunta al mismo SHA.
- `main` permanece en `ad4c630a6a4d442776740b59b9552ba72141ea48`.
- El microclose añade únicamente tres cambios: planner, tests y evidencia de factibilidad.
- `NHG03-F001=VERIFIED_RESOLVED`.
- `NHG03-F002=VERIFIED_RESOLVED`.
- Las 10 semillas y las 20 composiciones H150/H200 permanecen idénticas a `b380619`.
- Descriptores separados:
  - `increment_descriptor`;
  - `total_bank_descriptor = H100_FROZEN + incremento seleccionado`.
- Todos los bancos totales preservan cobertura H100 `66/66`.
- Common-clean:
  - primary = 1056;
  - exact clean = 1020;
  - near090 clean = 981;
  - near095 clean = 1002;
  - near098 clean = 1010.
- `eval_common_clean_masks_v0.1.csv` permanece sin cambios.
- `new_historical_eligible.csv` permanece SHA `a78e8c...c083a4`, 6,029 filas y 43 DAM.
- Tests: Gate 02 27/27; Gate 03 29/29; suite completa 326/326.
- No retrieval, no BM25, no materialización H150/H200.

### Próximo paso

Integrar Gate 03 por fast-forward a `main` y validar en clean checkout.

Solo después del cierre post-integración podrá iniciarse el siguiente subgate:

`EXP11B_BANK_MATERIALIZATION_GATE`

para materializar, hash-ear y auditar los 10 H150 + 10 H200 **sin retrieval**. `EXP11B_AUTHORIZED=false` hasta cerrar ese subgate.

### 2026-09-01 — Gate 03 cerrado e integrado a main

**Estado:** `CLOSED / APPROVED / INTEGRATED TO MAIN`.

- `main = origin/main = ed470d67315f505cb3bde471177268db6d16a676`.
- Integración por `git merge --ff-only`, sin merge commit.
- Relación contra base `ad4c630...`: `0 behind / 2 ahead`.
- Real Ingest freeze: 9 artefactos, 0 mismatches.
- Pool elegible congelado:
  - SHA `a78e8c517d50f53fa0f8b95a6c94f841dda4c0e3e5cf28cc4c4fccc576c083a4`;
  - 6,029 filas;
  - 43 DAM.
- H100/DEV/EVAL permanecen sin cambios.
- EXP-11B:
  - 10 seeds exactas congeladas;
  - 20 composiciones H150/H200 idénticas a baseline;
  - nesting estricto;
  - tolerancia <=148;
  - descriptores incrementales y del banco total congelados.
- Common-clean:
  - primary 1056;
  - exact clean 1020;
  - near090 clean 981;
  - near095 clean 1002;
  - near098 clean 1010.
- Tests en candidata/main/clean checkout:
  - Gate 02 27/27;
  - Gate 03 29/29;
  - suite completa 326/326.
- No retrieval, no BM25, no H150/H200 materializados.
- `EXP11B_AUTHORIZED=false`.
- `EXP12_AUTHORIZED=false`.
- `GROUP3_STARTED=false`.

### Próximo hito obligatorio

`EXP11B_BANK_MATERIALIZATION_GATE`

Objetivo:

1. materializar exactamente los 10 H150 y 10 H200 desde `H100_FROZEN + DAM lists congeladas`;
2. verificar que H100 es núcleo idéntico;
3. verificar DAM exactas, sin faltantes ni extras;
4. verificar row counts y composition SHA;
5. verificar nesting H150⊂H200 por réplica;
6. recalcular descriptores totales;
7. generar manifest e inventario SHA de los 20 bancos;
8. validar en clean checkout;
9. **NO ejecutar retrieval/BM25**.

Solo después de auditoría externa de esta materialización podrá considerarse `EXP11B_RETRIEVAL_AUTHORIZED=true`.

### 2026-09-01 — EXP11B Bank Materialization candidato `7a80b1d` auditado externamente

**Estado:** `APPROVED_WITH_BLOCKING_MICROCLOSE_BEFORE_MAIN`.

- Rama: `codex/exp11b-bank-materialization-v01`.
- Candidato: `7a80b1db657386705d3031559c2861d0a2f88eb2`.
- Padre directo: `ed470d67315f505cb3bde471177268db6d16a676`.
- Relación main→candidate: 0 behind / 1 ahead.
- 20 bancos materializados localmente:
  - 10 H150;
  - 10 H200.
- H100 core: 20/20 PASS.
- Selección Gate03: 20/20 PASS.
- Descriptores: 20/20 PASS.
- Nesting: 10/10 PASS.
- Hashes de bancos: 20 identidades congeladas; clean checkout reprodujo 20/20 byte exacto.
- Bancos CSV no versionados en Git; son derivados regenerables.
- Manifest y hash inventory sí están versionados.
- No retrieval, BM25 ni métricas de evaluación.

#### EXP11B-MAT-F001 — DEV_EVAL_PROVENANCE_NOT_HASH_FROZEN — S2

El materializer usa DEV y EVAL para bloquear overlap de DAM, por lo que ambos son inputs científicos efectivos. Sin embargo:

- `exp11b_bank_materialization_v0.1.json` registra solo sus paths, no SHA;
- `load_inputs()` los lee sin `validate_file_contract`;
- el manifest de materialización no registra DEV/EVAL como inputs observados.

Antes de integrar debe fijarse en config y manifest:

- DEV SHA `434e08f13ed3d5529165abbd0e139b5a675e7dc164307a624caa95f60a271f00`;
- EVAL SHA `3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941`;

y el script debe fallar si cambian. Esto no puede modificar ninguno de los 20 bank SHA.

#### EXP11B-MAT-F002 — FROZEN_GATE03_TEST_WEAKENED_OUTSIDE_SCOPE — S2

El commit candidato modificó además `tests/test_exp11b_historical_size_extension_v01.py`, cambiando una aserción de HHI de `assertEqual` a `assertAlmostEqual(..., places=15)`.

Este archivo no formaba parte del scope materializador y Gate03 ya estaba cerrado. La modificación debe revertirse exactamente al contenido de `ed470d6`. Si el test exacto falla, debe detenerse y reportar los dos floats; no se permite debilitar silenciosamente un test congelado.

#### EXP11B-MAT-F003 — HASH_INVENTORY_VERIFY_NOT_FAIL_CLOSED — S2

`verify()` reconstruye y compara correctamente el manifest de bancos, pero al leer `exp11b_bank_hashes_v0.1.csv` solo exige 20 filas y bank_id completos. No compara los valores de cada fila del inventario contra los bancos/manifest.

Debe verificar al menos, por bank_id:

- bank_csv_sha256;
- size_bytes;
- row_count;
- new_row_count;
- total_dam_count;
- new_dam_count;
- composition_sha256;
- H100_core_id_order_sha256;
- increment_id_order_sha256;
- total_bank_id_order_sha256.

La corrección no puede alterar los 20 CSV ni sus hashes.

### Estado

- `EXP11B_BANK_MATERIALIZATION_CANDIDATE_CREATED=true`.
- `BANKS_BYTE_REPRODUCIBLE=20/20`.
- `EXP11B_BANK_MATERIALIZATION_EXTERNAL_APPROVAL=false`.
- `EXP11B_RETRIEVAL_AUTHORIZED=false`.
- `RETRIEVAL_EXECUTED=false`.
- `EXP12_AUTHORIZED=false`.
- `GROUP3_STARTED=false`.

**No integrar a main hasta cerrar MAT-F001..F003.**

### 2026-09-01 — Microclose materialization detenido por diferencia float de 1 ULP

- HEAD/remoto permanecen `7a80b1db657386705d3031559c2861d0a2f88eb2`.
- `main = origin/main = ed470d67315f505cb3bde471177268db6d16a676`.
- Los 20 bancos canónicos no fueron reescritos.
- MAT-F001 y MAT-F003 no se iniciaron.
- El test Gate03 se restauró exactamente a `ed470d6`.
- Resultado Gate03 con igualdad exacta: 28/29.
- Valor congelado `dam_hhi = 0.13446841032608695`.
- Recomputación Python 3.12.13: `0.13446841032608697`.
- Diferencia binaria real: `2.7755575615628914e-17`, exactamente **1 ULP** en esa magnitud.
- Python 3.12 cambió el algoritmo de `sum()` para floats por uno de mayor precisión; por tanto, igualdad bit-a-bit de un descriptor float recalculado entre runtimes no es un contrato portable.
- El criterio ya usado por el materializer para descriptores es tolerancia absoluta `1e-12`.

#### Re-clasificación externa de MAT-F002

`EXP11B-MAT-F002 = GATE03_FLOAT_SUM_PORTABILITY_DEFECT / S2_PROCEDURAL`.

Resolución autorizada:

- NO cambiar el descriptor congelado Gate03;
- NO recalcular ni reescribir feasibility;
- NO cambiar los 20 bank SHA;
- sustituir el test exacto por una comparación explícita con `abs_tol=1e-12`, `rel_tol=0`, documentando que es una corrección de portabilidad numérica;
- añadir control de que el delta observado está dentro de tolerancia y que el descriptor sigue siendo distinto del descriptor incremental;
- después continuar MAT-F001 y MAT-F003.

Esto no altera selección, composición, resultados ni interpretación científica.

### 2026-09-01 — EXP11B Bank Materialization microclose `95ffec45` aprobado externamente

**Estado:** `APPROVED_FOR_MAIN_INTEGRATION`.

- Rama: `codex/exp11b-bank-materialization-v01`.
- Candidato inicial: `7a80b1db657386705d3031559c2861d0a2f88eb2`.
- Microclose: `95ffec45ae5a734545ae7bb2d8d530f42f8f056c`.
- `main = origin/main = ed470d67315f505cb3bde471177268db6d16a676` permanece sin merge.
- Relación `7a80b1d → 95ffec45`: 1 commit, 0 behind.
- Relación `main → 95ffec45`: 2 commits prospectivos del gate de materialización.

#### Findings cerrados

- `EXP11B-MAT-F001=VERIFIED_RESOLVED`.
  - DEV SHA `434e08f13ed3d5529165abbd0e139b5a675e7dc164307a624caa95f60a271f00`, 100 filas.
  - EVAL SHA `3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941`, 1,056 filas.
  - Ambos inputs se validan fail-closed y quedan registrados con SHA esperado/observado en el manifest.

- `EXP11B-MAT-F002=VERIFIED_RESOLVED`.
  - Política de portabilidad float: `rel_tol=0`, `abs_tol=1e-12`.
  - Diferencia documentada: `2.7755575615628914e-17` (1 ULP) en Python 3.12.13.
  - Gate03: 30/30 PASS.
  - Planner, feasibility, selección y bank identities no cambiaron.

- `EXP11B-MAT-F003=VERIFIED_RESOLVED`.
  - `--verify` compara campo a campo las 14 columnas del ledger de hashes.
  - Pruebas de corrupción del ledger fallan de forma cerrada.

#### Identidad y reproducibilidad

- 20/20 bank SHA preservados contra `7a80b1d`.
- 20/20 tamaños, filas, composition SHA y hashes de orden de IDs preservados.
- Los CSV canónicos no fueron reescritos.
- Clean checkout: bancos ausentes como corresponde; rematerialización temporal 20/20 byte exacta.
- Tests en Python 3.12.13:
  - base `ed470d6`: 326 tests; único fallo = comparación float exacta documentada;
  - candidato corregido: 368/368;
  - Gate02 27/27;
  - Gate03 30/30;
  - materialización 41/41.
- Formal `--verify`: PASS.
- `retrieval_executed=false`.
- `EXP11B_RETRIEVAL_AUTHORIZED=false`.

### Próximo paso

Integrar `95ffec45ae5a734545ae7bb2d8d530f42f8f056c` a `main` por fast-forward, ejecutar verificación post-integración y rematerialización temporal 20/20.

**Solo después de cerrar la integración del Bank Materialization Gate podrá abrirse el gate de ejecución EXP-11B retrieval.**

### 2026-09-01 — EXP11B Bank Materialization Gate cerrado e integrado

**Estado:** `CLOSED / APPROVED / INTEGRATED TO MAIN`.

- `main = origin/main = 95ffec45ae5a734545ae7bb2d8d530f42f8f056c`.
- Cadena de integración:
  - `7a80b1db657386705d3031559c2861d0a2f88eb2` — materialización y freeze de identidades;
  - `95ffec45ae5a734545ae7bb2d8d530f42f8f056c` — microclose de procedencia/fail-closed.
- La relación desde `ed470d6` es 0 behind / 2 ahead.
- Post-push clean checkout:
  - suite completa `368/368`;
  - rematerialización temporal `20/20` byte exacta;
  - 0 discrepancias.
- F001/F002/F003 permanecen `VERIFIED_RESOLVED`.
- Los 20 bancos no están versionados en Git; sus identidades, manifests y hashes sí están congelados.
- `BANK_IDENTITIES_MATCH=20/20`.
- `BANKS_BYTE_REPRODUCIBLE=true`.
- `H100_CORE_MATCH_ALL=true`.
- `SELECTION_MATCH_ALL=true`.
- `DESCRIPTORS_MATCH_ALL=true`.
- `NESTING_MATCH_ALL=true`.
- `RETRIEVAL_EXECUTED=false`.
- `EXP11B_RETRIEVAL_AUTHORIZED=false`.
- `EXP12_AUTHORIZED=false`.
- `GROUP3_STARTED=false`.

#### Limpieza local pendiente

Codex alcanzó a verificar que el worktree post-push estaba limpio y que podía retirarse. Solo quedó pendiente ejecutar:

`git worktree remove "<ruta-del-worktree-post-push>"`

y luego:

`git worktree prune`

sin `--force`.

Esta limpieza es **operativa, no científica** y no bloquea el cierre del Bank Materialization Gate. Si Windows deja metadatos huérfanos por permisos, se registra como limitación local no científica siempre que el worktree ya no aparezca en `git worktree list`.

### Próximo hito científico

`EXP11B RETRIEVAL EXECUTION GATE`

Debe congelar prospectivamente, antes de BM25:
- commit integrado `95ffec45...`;
- SHA del materialization manifest;
- SHA del ledger de los 20 bancos;
- 20 bank SHA;
- EVAL SHA;
- configuración BM25 exacta;
- normalización/tokenización;
- valores k;
- outputs/manifest;
- política de ejecución única y fail-closed;
- denominador primario `N=1056`;
- common-clean solo como sensibilidad complementaria.

No ejecutar retrieval hasta aprobar externamente ese gate.
