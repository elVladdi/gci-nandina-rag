# Politica de curacion data_aduanas clase 87 v0.1

Esta politica define las reglas de inclusion, exclusion, duplicados y auditoria para las particiones `data_aduanas` de `Clase = 87`.

## Principios

- Usar el nombre metodologico `data_aduanas`.
- Preservar trazabilidad operativa mediante `id_unico`, `DECLARACION`, `SERIE` y columnas tecnicas `__`.
- No modificar ni borrar el evalset v0.1 anterior, su metadata ni el devset preliminar.
- No versionar `data/Series - Descripciones.xlsx`.
- No tratar `descripcion + NANDINA` como llave de deduplicacion principal.
- Generar auditorias reproducibles bajo `outputs/audits/data_aduanas_splits_clase87_v0.1/`.

## Inclusion

Una fila entra al universo curado si:

- pertenece a `Clase = 87`;
- tiene `id_unico`, `DECLARACION` y `SERIE`;
- tiene `NANDINA` de 8 digitos;
- conserva `NANDINA ORIGINAL`;
- `Clase`, `Partida` y `Sub Partida` coinciden con prefijos de `NANDINA`;
- tiene `DESCRIPCION DE PARTIDA ARANCELARIA`;
- tiene `DESCRIPCION DE MERCANCIAS CONCATENADA`;
- no presenta advertencias criticas de parseo sobre campos obligatorios.

Las lineas `DESCRIPCION DE MERCANCIAS 1` a `5` son parte del esquema de salida. No todas tienen que estar llenas si la descripcion fuente ocupa menos lineas.

## Exclusion

Se excluyen filas con:

- campos obligatorios vacios;
- NANDINA no numerica de 8 digitos;
- inconsistencia entre `Clase`, `Partida`, `Sub Partida` y `NANDINA`;
- advertencias criticas de parseo que afecten campos obligatorios;
- conflicto de `id_unico`.

En la corrida v0.1 no se excluyeron filas por campos o calidad dentro de `Clase = 87`.

## Duplicados id_unico

La llave primaria de curacion es `id_unico`. La politica v0.1 es:

- Duplicado exacto: si todas las columnas no tecnicas coinciden, se conserva la primera aparicion estable y se excluyen las filas excedentes.
- Conflicto: si el mismo `id_unico` tiene payload no tecnico distinto, se excluye el grupo completo.

Conteos de la corrida v0.1:

- 108 grupos de `id_unico` repetido detectados dentro de filas validas de `Clase = 87`.
- 102 grupos fueron duplicados exactos.
- 114 filas excedentes se excluyeron por duplicado exacto.
- 6 grupos fueron conflictivos.
- 12 filas se excluyeron por conflicto.
- 4,106 filas quedaron en el universo curado final.

## Auditorias

El script genera:

- `excluded_quality_rows.csv`: filas excluidas por calidad/campos.
- `excluded_duplicate_rows.csv`: filas excluidas por politica de duplicados.
- `id_unico_duplicate_policy.csv`: resumen por grupo de `id_unico` repetido.
- `nandina_distribution_by_split.csv`: distribucion por NANDINA en historico/desarrollo/evaluacion.

Estos archivos son regenerables y no se fuerzan a Git.

## Split

El split es deterministico con semilla `2026` y estratificacion proporcional por `NANDINA` cuando es posible:

- historico: 3,000 filas;
- desarrollo: 100 filas;
- evaluacion: 1,006 filas.

Ningun `id_unico` se replica para mejorar cobertura. Si una NANDINA tiene pocas instancias, su presencia en cada particion depende de la cuota proporcional y del remanente disponible.

## Artefacto historico previo

El evalset v0.1 anterior de 600 casos queda conservado como artefacto historico/versionado. No sera la base principal de fases futuras una vez validada la Fase 3 actualizada con `data_aduanas`.
