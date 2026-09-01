# Protocolo de expansion historica multi-hoja v0.1

## Estado congelado

Este contrato pertenece a `NEW_HISTORICAL_GATE_02`. EXP-11A esta cerrado y sus resultados estan en `main`. No autoriza EXP-11B, EXP-12 ni Grupo 3.

La fuente actual se denomina `CURRENT_H100_REPRODUCING_SOURCE`. El workbook actual reproduce byte a byte los datasets congelados cuando es procesado mediante la cadena reconstruida, pero no se ha demostrado identidad binaria con el workbook historico completo. En consecuencia no se le denomina workbook historico original.

La fuente congelada es `data/Series - Descripciones.xlsx`, SHA-256 `db01d1fcdd41d1bd1ed8086fc6c19bcd56ba44b2534391aba7daa4c58f9f52d1`, con tamano de 7895186 bytes y orden de hojas `Hoja2`, `Hoja1`. La copia local se realiza mediante `shutil.copy2`, como bytes. El XLSX archivado no se versiona; el manifiesto de freeze si se versiona como evidencia del contrato.

## Datasets que no cambian

H100 es exclusivamente `data/processed/data_aduanas_historico_clase87_v0.2.csv`, SHA-256 `0990cdfe2a62638bff83a1182b0d6b0b727d670f63888044e99fd3ee0d7915ff`. No se reconstruira desde un workbook ampliado. Todo futuro banco sera `H100_FROZEN + NEW_ELIGIBLE_HISTORICAL_ROWS`.

DEV y EVAL permanecen, respectivamente, en `data/processed/data_aduanas_devset_clase87_v0.2.csv` (`434e08f13ed3d5529165abbd0e139b5a675e7dc164307a624caa95f60a271f00`) y `data/processed/data_aduanas_evalset_clase87_v0.2.csv` (`3ddb7a0e80d8bfa20b985655f03d6ab65470b40f0738093413909b6584aee941`). No se regeneran, amplian, reordenan ni reasignan.

En v0.2, el seed 2026 es un atributo de configuracion y procedencia. Las DAM estan materializadas como asignaciones explicitas T5-safe-159; el seed no es un mecanismo de seleccion aleatoria en `group_split_by_dam.py`.

## Contrato de hojas nuevas

`Hoja2` y `Hoja1` son `preexisting_source_sheets`, no una descripcion cientifica comun de hojas historicas procesadas. La hoja historicamente procesada es solo `Hoja2`, indice 0, mediante `DEFAULT_FIRST_WORKSHEET`. `Hoja1` queda clasificada como `PREEXISTING_UNPROCESSED_SOURCE_SHEET` salvo evidencia objetiva posterior.

Los unicos conjuntos validos para una ingesta real futura son `NEW_SHEET_SET_1 = [NUEVA_01]` y `NEW_SHEET_SET_2 = [NUEVA_01, NUEVA_02]`. `NUEVA_02` sola, orden inverso, conjunto vacio y terceras hojas fallan cerradamente. El workbook ampliado debe coincidir exactamente con `Hoja2`, `Hoja1`, `NUEVA_01`, y opcionalmente `NUEVA_02`, en ese orden.

La extraccion futura se hara con una invocacion explicita por hoja del parser historico `src/ingestion/sunat_series_parser.py`, mediante `--sheet NUEVA_01` o `--sheet NUEVA_02`. El contrato nunca usa la primera hoja del workbook para seleccionar datos nuevos.

Cada nueva hoja debe conservar una estructura SUNAT DAM raw/source-like procesable por el parser: `DECLARACION`, `SERIE`, `NANDINA` y `DESCRIPCION DE MERCANCIAS`, incluidos sus bloques posicionales. No se aceptan CSV pegados, tablas normalizadas manualmente, exportaciones de dataframe, ediciones por fila ni resultados de modelos. El pipeline `src/evaluation/build_evalset_from_sunat_excel.py` esta prohibido para esta expansion, pues tiene semantica de extraccion diferente.

## Pipeline futuro y controles

El unico recorrido permitido sera: PARSE, COMBINE NEW SHEETS, CLASSIFY/CURATE, FROZEN DAM/ID AUDIT, ELIGIBLE POOL, EXACT/NEAR DUPLICATE AUDIT, CAPACITY DESCRIPTORS, PROSPECTIVE OUTPUTS AND MANIFEST. No se construiran H150, H200 ni CSV historicos ampliados en Excel.

La normalizacion reutiliza `parse_workbook(..., sheet_name=<explicit>)` y por tanto conserva `clean_text`, DAM, SERIE, `id_unico`, jerarquia NANDINA, descripciones, `__sheet_name`, `__source_file`, warnings y trazabilidad de filas. La curacion reutilizara las reglas de `src/evaluation/build_data_aduanas_splits.py`: Clase 87, campos requeridos, NANDINA de ocho digitos, jerarquia consistente, warnings criticos, `id_unico`, duplicados y conflictos.

Antes de la elegibilidad, se obtienen las DAM congeladas de DEV y EVAL. Toda nueva fila con `DECLARACION` coincidente queda `EXCLUDED_FIXED_DEV_EVAL_DAM`. Un `id_unico` ya presente en H100, DEV o EVAL queda `EXISTING_FROZEN_ID_UNICO_OVERLAP`. Ambas causas se calculan y registran independientemente: una misma fila puede llevar ambas y nunca entra al pool elegible. Las coincidencias textuales exactas y near-duplicate 0.90, 0.95 y 0.98 se reportan como descriptores; no son exclusiones automaticas ni criterios de seleccion.

H100 tiene 2950 filas, H150 apunta a 4425 y H200 a 5900. Despues de parsing, curacion y controles se requieren al menos 1475 filas nuevas elegibles netas para factibilidad H150 y 2950 para H200. Si H200 no es factible, el gate falla: no se reduce H200.

## Operacion de Gate 02

Ejecutar el preflight y freeze con el Python del entorno:

```powershell
python src/ingestion/prepare_new_historical_multisheet_v0.1.py --preflight --freeze-source
```

El preflight actual es valido cuando Hoja2 y Hoja1 mantienen su orden y `NUEVA_01`/`NUEVA_02` estan ausentes. El resultado esperado es `CURRENT_SOURCE_FREEZE_READY=true`, `NEW_DATA_SHEETS_PRESENT=false` y `NEW_DATA_INGESTION_EXECUTED=false`.

La futura validacion, que no ingiere ni escribe datasets, requiere nombres explicitos:

```powershell
python src/ingestion/prepare_new_historical_multisheet_v0.1.py --validate-new-sheets --future-workbook <WORKBOOK_AMPLIADO> --new-sheet NUEVA_01
```

El modo prospectivo congelado `--ingest-new-data` requiere `--future-workbook` y `--new-sheet NUEVA_01`, con `--new-sheet NUEVA_02` solo como segunda seleccion. Reutiliza directamente `classify_rows(..., scope_class="87")` sobre la combinacion de todas las hojas nuevas y solo escribe en `data/interim/new_historical_gate_v0.1/` y `outputs/audits/new_historical_gate_v0.1/`. Produce normalizado, curado, elegible, exclusiones, auditorias de overlap y duplicados, manifiesto y hashes. Nunca escribe `data/processed`, H100, DEV, EVAL, H150 o H200; tampoco ejecuta retrieval o BM25.

El manifiesto de freeze y las auditorias quedan bajo `outputs/audits/new_historical_gate_v0.1/`. La copia XLSX se archiva fuera del repositorio para no convertirla en un artefacto rastreable.
