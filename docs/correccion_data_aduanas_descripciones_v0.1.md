# Correccion data_aduanas descripciones v0.1

Fecha de actualizacion: 2026-08-01.

## Problema detectado

La recuperacion base usa `DESCRIPCION DE MERCANCIAS CONCATENADA`, construida desde `DESCRIPCION DE MERCANCIAS 1` a `DESCRIPCION DE MERCANCIAS 5`. En los splits previos se detectaron encabezados/secciones DAM dentro de esas columnas descriptivas.

Linea base reportada antes de la correccion:

| Split | Casos con `REGISTRO DE ADUANAS` en descripcion concatenada |
| --- | ---: |
| historico | 55 |
| devset | 0 |
| evalset | 14 |

Tambien se observaron casos donde el texto administrativo caia en `DESCRIPCION DE MERCANCIAS 4` o `DESCRIPCION DE MERCANCIAS 5`.

## Causa

En `src/ingestion/sunat_series_parser.py`, `series_end` se define por la siguiente fila de serie o por el final de la tabla/DAM. Cuando el final de tabla alcanzaba secciones administrativas posteriores, `description_lines` tomaba todas las filas no vacias desde `series_start + DETAIL_VALUE_ROWS` hasta `series_end`, sin distinguir encabezados DAM.

## Regla de correccion

Se agregaron funciones auxiliares:

- `is_dam_section_header_line(...)`: detecta encabezados/secciones DAM claros.
- `trim_dam_section_header_fragment(...)`: recorta fragmentos de encabezado pegados al final de una linea descriptiva.
- `extract_description_lines(...)`: extrae solo lineas reales de mercancia y se detiene ante secciones DAM.

La regla excluye como minimo `REGISTRO DE ADUANAS`, `DECLARACION`, `FECHA NUMERACION`, `IDENTIFICACION`, `TRANSACCION`, `BASE IMPONIBLE`, `LIQUIDACION DEL ADEUDO` y encabezados DAM equivalentes. Se mantienen las cinco columnas originales y la concatenada completa solo con lineas reales de mercancia.

## Conteos corregidos

| Conteo | Valor |
| --- | ---: |
| Filas clase 87 de entrada | 4,232 |
| Filas curadas finales | 4,106 |
| Historico | 3,000 |
| Devset | 100 |
| Evalset | 1,006 |
| Grupos duplicados exactos | 102 |
| Filas exactas excedentes excluidas | 114 |
| Grupos con conflicto de `id_unico` | 6 |
| Filas conflictivas excluidas | 12 |

## Validacion de encabezados

Resultado post-correccion en `DESCRIPCION DE MERCANCIAS 1..5` y `DESCRIPCION DE MERCANCIAS CONCATENADA`:

| Patron | historico | devset | evalset |
| --- | ---: | ---: | ---: |
| `REGISTRO DE ADUANAS` | 0 | 0 | 0 |
| `DECLARACION` | 0 | 0 | 0 |
| `FECHA NUMERACION` | 0 | 0 | 0 |
| `IDENTIFICACION` | 0 | 0 | 0 |
| `TRANSACCION` | 0 | 0 | 0 |
| `BASE IMPONIBLE` | 0 | 0 | 0 |
| `LIQUIDACION DEL ADEUDO` | 0 | 0 | 0 |

Validaciones estructurales: mismas columnas en los tres splits, sin `id_unico` repetidos dentro de cada split, sin solapamiento entre historico/dev/eval, `Clase = 87`, `NANDINA` de 8 digitos, `Partida` de 4 digitos, `Sub Partida` de 6 digitos y `NANDINA ORIGINAL` conservada.

## Impacto en metricas

| Fase | Estado | Top-1 | Top-3 | Top-10 | Recall@100 | MRR | Fuera Top-100 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 9A historica real | antes | 0.8638 | 0.9384 | 0.9791 | 0.9980 | 0.9071 | 2 |
| 9A historica real | despues | 0.8628 | 0.9374 | 0.9801 | 1.0000 | 0.9062 | 0 |
| 9B hibrido recomendado | antes | 0.8638 | 0.9384 | 0.9791 | 0.9980 | 0.9071 | 2 |
| 9B hibrido recomendado | despues | 0.8628 | 0.9374 | 0.9801 | 1.0000 | 0.9062 | 0 |

La estrategia 9B recomendada se mantiene: `historical_with_normative_backfill_if_missing_code`. En la corrida regenerada completa, el historico corregido ya alcanza `Recall@100 = 1.0000`; el backfill normativo no aumenta cobertura exacta, pero se conserva como respaldo documental y trazabilidad.

## Decision metodologica

La correccion pertenece a ingesta, no a edicion manual de CSV. Los CSV intermedios se regeneran desde `data/Series - Descripciones.xlsx` y permanecen ignorados por Git. Los cuatro artefactos finales de splits clase 87 se consideran versionables y reproducibles.

Fase 10A queda como diagnostico previo ejecutado sobre splits anteriores a esta limpieza. La siguiente iteracion 10B debera usar los splits corregidos.
