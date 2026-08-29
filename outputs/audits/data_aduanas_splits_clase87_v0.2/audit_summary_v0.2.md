# Auditoria split Aduanas Clase 87 v0.2

Split aprobado: T5-safe-159. Las particiones son independientes por DAM y no fueron seleccionadas por metricas de modelo.

## Resultado de compuerta

- DAM compartidas entre particiones: 0.
- id_unico compartidos entre particiones: 0.
- Casos de evaluacion con soporte historico: 1056 de 1056.
- Concentracion maxima DAM en evaluacion: 14.109848%.

## Duplicados

- Duplicados exactos historico-evaluacion: 35 filas de evaluacion afectadas; 1 con NANDINA distinta.
- Near-duplicates historico-evaluacion:
  - umbral 0.90: 55 filas afectadas, 82 pares.
  - umbral 0.95: 44 filas afectadas, 46 pares.
  - umbral 0.98: 37 filas afectadas, 38 pares.

## Soporte historico por bucket

- C. 3-4 DAM historicas: 18 codigos / 425 casos.
- D. 5+ DAM historicas: 15 codigos / 583 casos.
- B. 2 DAM historicas: 2 codigos / 21 casos.
- A. 1 DAM historica: 7 codigos / 27 casos.
