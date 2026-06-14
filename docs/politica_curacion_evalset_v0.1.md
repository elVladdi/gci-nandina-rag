# Politica de curacion del evalset v0.1

Este documento define una politica conservadora para revisar duplicados antes de generar `data/processed/evalset_v0.1.csv`. La auditoria se realiza sobre los casos extraidos desde el Excel SUNAT, sin modificar todavia el dataset final.

## Principios

- El devset preliminar `data/processed/devset_validacion_intermedia.csv` no se modifica ni se mezcla con el evalset final.
- El archivo final `data/processed/evalset_v0.1.csv` debe generarse solo despues de auditar duplicados, trazabilidad y reglas minimas de calidad.
- La eliminacion o conservacion de filas debe quedar documentada mediante reportes reproducibles.
- No se debe declarar validacion final de hipotesis hasta completar la curacion y ejecutar las fases de evaluacion posteriores.

## Criterio de duplicado exacto

Se considera duplicado exacto de evaluacion cuando dos o mas filas tienen la misma combinacion:

```text
descripcion + nandina_ref + regimen
```

normalizada para comparacion textual. Estos duplicados exactos no deben contarse multiples veces en la evaluacion final, porque inflarian el peso de un mismo caso metodologico.

## Politica recomendada

- Para duplicados exactos por `descripcion + nandina_ref + regimen`, conservar una instancia representativa.
- Registrar cuantas filas fueron excluidas por duplicado exacto y conservar evidencia en `outputs/audits/evalset_v0.1_duplicates/`.
- Usar como representante la primera aparicion estable del extractor, salvo que la revision manual identifique una fila con mejor trazabilidad.
- No eliminar casos que comparten la misma `nandina_ref` si la descripcion de mercancia es distinta.
- No eliminar automaticamente casos que comparten la misma descripcion si `nandina_ref` o `regimen` difiere; estos casos deben marcarse para revision manual porque pueden revelar ambiguedad, error de fuente o diferencia metodologicamente relevante.
- Mantener en `observaciones` la trazabilidad de hoja, serie, fila de inicio, fila de fin y descripcion de partida cuando provenga del reporte SUNAT por bloques.

## Tamano metodologico

El objetivo metodologico inicial era aproximadamente 300 instancias. Sin embargo, el Excel real puede permitir extraer mas casos unicos validos. La recomendacion es usar todos los casos unicos validos cuando el numero final sea razonable, trazable y auditable.

Si por diseno experimental se necesita limitar el evalset a cerca de 300 casos, la reduccion debe hacerse mediante muestreo documentado y reproducible, no por recorte arbitrario. El muestreo debe declarar semilla, criterio de estratificacion si aplica, fecha y conteos antes/despues.

La composicion final queda concentrada en regimen `10` (importacion para el consumo). Esta concentracion debe documentarse como limite empirico y no autoriza generalizar resultados a otros regimenes aduaneros.

## Reportes de auditoria

La auditoria de duplicados debe generar:

- `outputs/audits/evalset_v0.1_duplicates/extracted_preview.csv`: todos los casos extraidos en esquema evalset antes de deduplicar.
- `outputs/audits/evalset_v0.1_duplicates/duplicate_groups.csv`: grupos duplicados por `descripcion + nandina_ref + regimen`.
- `outputs/audits/evalset_v0.1_duplicates/duplicate_summary.json`: conteos agregados y distribuciones.
- `outputs/audits/evalset_v0.1_duplicates/extraction_summary.json`: resumen de extraccion, validez, duplicados y casos unicos.

Estos reportes son evidencia de curacion previa; no sustituyen el evalset final ni constituyen resultados de evaluacion.