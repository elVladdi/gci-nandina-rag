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
| 2. Reproducibilidad y trazabilidad | **EN CURSO — G2A cerrado; EXP-11A cerrado; Forensic Audit 01 aprobado; siguiente Gate 02: freeze fuente + contrato multi-hoja** |
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

| Condición | Top-3 | MRR |
|---|---:|---:|
| H25 | 0.645170 ± 0.051964 | 0.603787 ± 0.047775 |
| H50 | 0.597917 ± 0.066393 | 0.542492 ± 0.060405 |
| H75 | 0.463352 ± 0.132774 | 0.414030 ± 0.126668 |
| H100 | 0.671402 | 0.629708 |

## 7. NEW_HISTORICAL_GATE — Forensic Audit 01

**EXTERNAL AUDIT: APPROVED_WITH_TERMINOLOGY_CORRECTIONS.**

- `FORENSIC_EXCEL_PIPELINE_AUDIT_COMPLETED=true`.
- Excel actual: `data/Series - Descripciones.xlsx`.
- SHA actual antes/después: `db01d1fcdd41d1bd1ed8086fc6c19bcd56ba44b2534391aba7daa4c58f9f52d1`.
- Tamaño: `7,895,186` bytes.
- Hojas: índice 0 `Hoja2` (126,524×9), índice 1 `Hoja1` (41,578×10).
- Hoja activa actual: `Hoja1`.
- Hoja procesada históricamente: `Hoja2`, índice 0, por selección predeterminada de primera hoja, sin `--sheet`.
- Parser: `openpyxl.load_workbook(..., read_only=True, data_only=True)`.
- `__sheet_name` histórico: únicamente `Hoja2`.
- Intermedio reproducido: 107 DAM / 11,320 series.
- Clase 87: 4,232 filas; 4,106 curadas.
- v0.1: split por fila, estratificado por NANDINA, seed 2026, tamaños 3000/100/1006.
- v0.2: unión de v0.1 y **asignaciones explícitas de DAM** de T5-safe-159.
- H100/DEV/EVAL v0.2 reproducidos byte a byte.
- Clasificación conservadora: `PIPELINE_PARTIALLY_RECONSTRUCTED`.

### Correcciones terminológicas

1. El workbook histórico completo no es byte-identificable con el actual: metadata histórica `cfc85f3d…` vs actual `db01d1fc…`.
2. La reproducción byte-exacta demuestra **equivalencia funcional del contenido procesado para el parser**, no identidad binaria de la hoja ni del workbook histórico completo.
3. En v0.2, `seed=2026` queda como atributo de configuración/procedencia; el script materializa el split desde **listas explícitas de DAM** y no usa aleatoriedad para decidir la asignación v0.2.
4. `build_evalset_from_sunat_excel.py` no se reutilizará para la expansión histórica: es un flujo distinto y produce otro esquema, aunque su modo `sunat-block` pueda iterar varias hojas.

El parser histórico procesa una sola hoja por invocación. Si no se pasa `--sheet`, procesa `workbook.worksheets[0]`. Nuevas pestañas no se incorporan automáticamente.

## 8. NEW_HISTORICAL_GATE — Gate 02: freeze fuente + contrato multi-hoja

**SIGUIENTE HITO.**

Antes de que el usuario modifique el Excel:

1. congelar localmente una copia byte-a-byte del workbook actual `db01d1fc…`;
2. denominarla como **fuente actual que reproduce H100**, no como “original histórico”;
3. verificar SHA origen=copia;
4. congelar mediante código/config/test el contrato de incorporación de nuevas pestañas;
5. reutilizar `sunat_series_parser.py` explícitamente por nombre de hoja;
6. preservar H100 congelado como núcleo, sin reconstruirlo desde el workbook modificado;
7. procesar únicamente las hojas nuevas con Python;
8. aplicar las mismas reglas de Clase 87, jerarquía, `id_unico`, warnings y curación;
9. bloquear DAM de DEV/EVAL y overlaps de `id_unico`;
10. auditar exact/near duplicates como descriptores;
11. exigir capacidad posterior suficiente para H150/H200 y factibilidad de EXP-12.

**El usuario todavía NO debe agregar las nuevas pestañas hasta cerrar Gate 02.**

## 9. EXP-11B

- H150 ≈ 4,425 series.
- H200 ≈ 5,900 series.
- H100 debe permanecer exactamente preservado como núcleo.
- Para capacidad H200 se necesitan al menos **2,950 series nuevas elegibles netas** sobre H100; condición post-procesamiento, no número bruto de filas Excel.

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
Gate 02: freeze fuente actual + contrato multi-hoja ⏳
  ↓
Usuario agrega nueva(s) pestaña(s) según contrato
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
- Workbook actual intacto con SHA `db01d1fc...`.
- Próximo hito: congelar esa fuente actual reproducente y versionar el contrato de expansión multi-hoja antes de editar el Excel.
