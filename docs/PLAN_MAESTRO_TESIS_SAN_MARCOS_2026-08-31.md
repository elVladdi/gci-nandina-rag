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
| 2. Reproducibilidad y trazabilidad | **EN CURSO — Gate 02 cerrado; NUEVA_01 agregada; Real Ingest 01 detenido antes de ingesta por comparación parser demasiado estricta; microauditoría de diferencias en Hoja2 pendiente** |
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
