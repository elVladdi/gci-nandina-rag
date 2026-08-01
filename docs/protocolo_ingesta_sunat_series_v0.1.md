# Protocolo de ingesta SUNAT por series v0.1

Este documento describe el parser general para convertir el workbook local `data/Series - Descripciones.xlsx` en una tabla normalizada de una fila por serie/DAM.

## Principio de diseno


Nombre metodologico: `data_aduanas`. El archivo fisico puede conservar su ruta y nombre local `data/Series - Descripciones.xlsx`, y el parser puede conservar su nombre actual por compatibilidad operativa. En documentacion metodologica de Fase 2, la fuente se cita como `data_aduanas`.

El parser conserva `NANDINA ORIGINAL`, `Clase`, `Partida`, `Sub Partida`, `NANDINA`, `id_unico` y las cinco columnas de descripcion (`DESCRIPCION DE MERCANCIAS 1` a `DESCRIPCION DE MERCANCIAS 5`) para que las particiones futuras mantengan trazabilidad y esquema homogeneo.

El parser no traduce ni inventa nombres semanticos para las etiquetas SUNAT. Las columnas de datos usan las etiquetas visibles del encabezado DAM y del detalle de serie. Solo se agregan:

- `id_unico`, llave de negocio formada como `DECLARACION-SERIE`.
- `NANDINA ORIGINAL`, columna que conserva el codigo visible SUNAT con puntos.
- `Clase`, `Partida`, `Sub Partida` y `NANDINA`, columnas derivadas desde el codigo NANDINA visible y almacenadas sin puntos.
- columnas tecnicas con prefijo `__` para trazabilidad del parseo.

Los dos puntos finales de las etiquetas del encabezado se remueven solo para formar nombres de columna legibles; no se cambia el significado de la etiqueta.

## Script

Ruta versionable:

```text
src/ingestion/sunat_series_parser.py
```

Uso recomendado:

```powershell
python -m src.ingestion.sunat_series_parser `
  --input "data/Series - Descripciones.xlsx" `
  --output-csv "data/interim/sunat_series_descripciones_normalized.csv" `
  --output-xlsx "data/interim/sunat_series_descripciones_normalized.xlsx" `
  --metadata "data/interim/sunat_series_descripciones_normalized_metadata.json" `
  --label-audit "outputs/audits/sunat_series_labels_v0.1/labels.csv" `
  --duplicate-audit "outputs/audits/sunat_series_labels_v0.1/id_unico_duplicates.csv" `
  --overwrite
```

Para una prueba sin escritura:

```powershell
python -m src.ingestion.sunat_series_parser --dry-run
```

## Entrada

- Workbook fuente: `data/Series - Descripciones.xlsx`.
- Hoja por defecto: primera hoja del workbook.
- Formato esperado: bloques DAM que inician con `DECLARACION :` y contienen una tabla de series cuyo encabezado empieza con `SERIE`.

## Logica de normalizacion

Cada fila normalizada representa una serie de una DAM.

1. Se detecta cada DAM por la etiqueta `DECLARACION :`.
2. Se extraen las etiquetas visibles del encabezado DAM mediante pares etiqueta/valor.
3. Cuando un valor adyacente no tiene etiqueta propia, se conserva dentro del valor de la etiqueta real precedente.
4. La tabla `6. BASE IMPONIBLE` se normaliza combinando la etiqueta de fila con las cabeceras visibles de columnas, por ejemplo `6.1. FOB - TOTAL DOLARES (US$)`.
5. La tabla `LIQUIDACION DEL ADEUDO` se normaliza combinando el concepto con las cabeceras visibles de columnas, por ejemplo `3.1. AD/VALOREM - CANTIDAD A PAGAR $`.
6. El detalle de serie se extrae desde la grilla visible de etiquetas: `SERIE`, `PUERTO EMBARQUE`, `NANDINA`, `DESCRIPCION DE PARTIDA ARANCELARIA`, `DESCRIPCION DE MERCANCIAS`, entre otras.
7. El codigo NANDINA visible de SUNAT se conserva en `NANDINA ORIGINAL`, por ejemplo `70.09.10.00.00`.
8. Desde ese codigo se derivan columnas sin puntos: `Clase` (2 digitos), `Partida` (4 digitos), `Sub Partida` (6 digitos) y `NANDINA` (8 digitos).
9. `DESCRIPCION DE MERCANCIAS` se conserva en cinco columnas (`DESCRIPCION DE MERCANCIAS 1` a `DESCRIPCION DE MERCANCIAS 5`) porque el formato SUNAT separa esa descripcion en filas. Tambien se genera `DESCRIPCION DE MERCANCIAS CONCATENADA` para busqueda y recuperacion.
10. Se crea `id_unico = DECLARACION + '-' + SERIE`.

## Salidas

- CSV normalizado: `data/interim/sunat_series_descripciones_normalized.csv`.
- XLSX normalizado opcional: `data/interim/sunat_series_descripciones_normalized.xlsx`.
- Metadata JSON: `data/interim/sunat_series_descripciones_normalized_metadata.json`.
- Auditoria de etiquetas: `outputs/audits/sunat_series_labels_v0.1/labels.csv`.
- Auditoria de duplicados `id_unico`: `outputs/audits/sunat_series_labels_v0.1/id_unico_duplicates.csv`.

## Columnas tecnicas

Las siguientes columnas no provienen de SUNAT; se agregan para reproducibilidad:

- `id_unico`
- `__record_id`
- `__dam_index`
- `__series_index`
- `__source_file`
- `__sheet_name`
- `__dam_row_start`
- `__dam_row_end`
- `__series_row_start`
- `__series_row_end`
- `__parse_warnings`

Todas las demas columnas corresponden a etiquetas visibles en el workbook local o a combinaciones trazables de etiquetas visibles en tablas del encabezado.

## Uso posterior

La tabla normalizada es una capa intermedia. Desde ella se deben construir, con scripts separados y criterios documentados:

- devset;
- evalset;
- banco historico.

El parser no realiza balanceo, muestreo, deduplicacion experimental ni seleccion por capitulos/partidas. Si el Excel fuente repite una DAM y sus series, el parser conserva esas filas y reporta los `id_unico` repetidos en una auditoria separada, distinguiendo duplicados exactos de conflictos. La decision de conservar, excluir o resolver duplicados pertenece a fases posteriores de curacion.
