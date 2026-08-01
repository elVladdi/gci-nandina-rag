# Protocolo data_aduanas clase 87 v0.1

Este documento actualiza la Fase 3 para preparar particiones experimentales desde la fuente metodologica `data_aduanas`, con alcance `Clase = 87`. La actualizacion no borra ni modifica el evalset v0.1 anterior; ese evalset de 600 casos queda como artefacto historico/versionado.

## Alcance

- Fuente metodologica: `data_aduanas`.
- Capa normalizada de entrada: `data/interim/sunat_series_descripciones_normalized.csv`.
- Parser de origen: `src/ingestion/sunat_series_parser.py`.
- Fuente fisica local: `data/Series - Descripciones.xlsx`, no versionable.
- Alcance arancelario: `Clase = 87`.
- Script de construccion: `src/evaluation/build_data_aduanas_splits.py`.

La normalizacion disponible contiene 11,320 series. De ellas, 4,232 pertenecen a `Clase = 87` y cubren 69 NANDINAS distintas antes de curacion por `id_unico`.

## Salidas congeladas

La Fase 3 actualizada genera tres CSV finales con identico esquema y orden de columnas:

- `data/processed/data_aduanas_historico_clase87_v0.1.csv`
- `data/processed/data_aduanas_devset_clase87_v0.1.csv`
- `data/processed/data_aduanas_evalset_clase87_v0.1.csv`

La metadata queda en:

- `data/processed/data_aduanas_splits_clase87_v0.1_metadata.json`

Las auditorias regenerables quedan bajo:

- `outputs/audits/data_aduanas_splits_clase87_v0.1/`

## Criterios de inclusion

Se conserva una fila de la capa normalizada si cumple todas estas reglas:

- `Clase == 87`.
- `id_unico` no vacio.
- `DECLARACION` no vacia.
- `SERIE` no vacia.
- `NANDINA` valida de 8 digitos.
- `NANDINA ORIGINAL` no vacia.
- `Clase`, `Partida` y `Sub Partida` consistentes con los prefijos de `NANDINA`.
- `DESCRIPCION DE MERCANCIAS CONCATENADA` no vacia.
- `DESCRIPCION DE PARTIDA ARANCELARIA` no vacia.
- Sin advertencias criticas de parseo que afecten campos obligatorios.

Las columnas `DESCRIPCION DE MERCANCIAS 1` a `DESCRIPCION DE MERCANCIAS 5` se conservan en el esquema de salida, pero no se exige que cada una tenga valor porque la fuente puede usar menos de cinco lineas descriptivas.

## Criterios de exclusion

Se excluyen filas con campos obligatorios vacios, NANDINA no valida, jerarquia inconsistente o advertencias criticas de parseo sobre campos obligatorios. En la corrida v0.1 no hubo exclusiones por calidad/campos dentro de `Clase = 87`.

No se deduplica por `descripcion + NANDINA`. Esa regla pertenecia al evalset v0.1 anterior y no preserva la trazabilidad primaria de `data_aduanas`. Para esta fase la llave principal es `id_unico`.

## Politica de duplicados id_unico

La politica es conservadora:

- Si un `id_unico` repetido tiene payload no tecnico identico, se conserva la primera aparicion estable y se excluyen las filas excedentes.
- Si un `id_unico` repetido presenta conflicto de payload, se excluye el grupo completo.
- Todas las decisiones quedan auditadas en `outputs/audits/data_aduanas_splits_clase87_v0.1/id_unico_duplicate_policy.csv`.

Resultado de la corrida v0.1:

- 102 grupos de duplicado exacto.
- 114 filas excedentes excluidas por duplicado exacto.
- 6 grupos conflictivos.
- 12 filas excluidas por conflicto.
- 126 filas excluidas por duplicados en total.

## Split experimental

El split usa muestreo deterministico estratificado por `NANDINA` cuando es posible, con semilla `2026`. El objetivo metodologico es reservar aproximadamente 3,000 instancias como historico inicial, un desarrollo pequeno de 100 instancias y dejar el resto curado como evaluacion.

Resultado v0.1:

| Split | Filas | NANDINAS distintas |
| --- | ---: | ---: |
| historico | 3,000 | 69 |
| desarrollo | 100 | 44 |
| evaluacion | 1,006 | 62 |

Las NANDINAS con pocas instancias se asignan mediante cuota proporcional. Si un estrato no alcanza cuota en una particion pequena, permanece trazado en las particiones donde la cuota proporcional y el remanente lo permiten; no se replica ningun `id_unico` para forzar cobertura.

## Comando reproducible

```powershell
python -m src.evaluation.build_data_aduanas_splits `
  --input data\interim\sunat_series_descripciones_normalized.csv `
  --output-dir data\processed `
  --scope-class 87 `
  --historical-size 3000 `
  --dev-size 100 `
  --seed 2026 `
  --overwrite
```

Por defecto el script usa el CSV intermedio existente. Si se necesita regenerar la capa normalizada desde el Excel local, usar `--regenerate-normalized`; esto requiere que `data/Series - Descripciones.xlsx` exista localmente y no implica versionarlo.

## Relacion con el evalset v0.1 anterior

El evalset v0.1 anterior de 600 casos se conserva como artefacto historico/versionado junto con su metadata y documentos. Una vez validada esta Fase 3 actualizada, los splits `data_aduanas` clase 87 pasan a ser la base principal para fases experimentales futuras.
