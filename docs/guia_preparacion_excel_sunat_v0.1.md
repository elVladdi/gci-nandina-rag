# Guía de preparación del Excel SUNAT para evalset v0.1

Esta guía describe cómo preparar el archivo fuente que luego se convertirá en `data/processed/evalset_v0.1.csv`. El Excel fuente no es el dataset final; es un insumo de curación para generar el evalset con el esquema definido en Fase 3A.

## Formatos aceptados

El script acepta dos formatos de entrada:

- Tabla simple con columnas explícitas de descripción, NANDINA y régimen.
- Reporte SUNAT por bloques, donde cada serie inicia en la primera columna, el código NANDINA aparece dentro del bloque y la descripción de mercancía queda en las filas posteriores.

La opción por defecto es `--format auto`: primero intenta detectar una tabla simple y, si no encuentra sus columnas obligatorias, intenta extraer el reporte SUNAT por bloques.

## Formato tabla simple

El archivo `.xlsx` o `.csv` preparado por el usuario debe incluir, como mínimo:

| Columna esperada | Variantes aceptadas |
| --- | --- |
| `Descripcion` | `Descripción`, `descripcion`, `DESCRIPCION` |
| `NANDINA` | `NANDINA`, `nandina`, `nandina_ref`, `codigo`, `código` |
| `Regimen` | `Régimen`, `regimen`, `REGIMEN` |

Opcionalmente puede incluir `observaciones`, que se copiará al evalset cuando exista.

## Formato reporte SUNAT por bloques

Para archivos SUNAT con estructura de reporte, usar `--format sunat-block` o dejar `--format auto`. El extractor aplica estas reglas:

- Lee cada hoja sin asumir encabezados normales.
- Detecta una nueva serie cuando la primera columna contiene un número de serie.
- Toma el régimen desde la última columna no vacía de la fila de inicio de la serie.
- Busca dentro del bloque un código con forma `94.04.90.00.00` o similar.
- Convierte el código punteado a NANDINA-8 usando los primeros ocho dígitos, por ejemplo `94.04.90.00.00` -> `94049000`.
- Toma la descripción de partida arancelaria desde la misma fila del código, si aparece.
- Une las filas posteriores del bloque como descripción de mercancía hasta antes de la siguiente serie.
- Registra en `observaciones` la hoja, serie, filas de inicio/fin y descripción de partida.

## Ubicación sugerida

Guardar el archivo fuente en una ruta local no versionada, por ejemplo:

```text
data/interim/sunat_evalset_input_v0.1.xlsx
```

Si el archivo contiene datos no revisados, datos operativos o información sensible, no debe subirse a Git. Antes de generar el evalset final se deben retirar identificadores innecesarios de personas, empresas, declaraciones, direcciones u otros datos sensibles.

## Previsualización sin escritura

Antes de generar el evalset final, se recomienda previsualizar la extracción:

```powershell
python -m src.evaluation.build_evalset_from_sunat_excel `
  --input data/interim/sunat_evalset_input_v0.1.xlsx `
  --format auto `
  --fecha-consulta 2026-06-13 `
  --preview 10
```

Con `--preview`, el script extrae y valida en memoria, imprime las primeras filas y no crea `data/processed/evalset_v0.1.csv` ni metadata.

## Generación del evalset

Desde la raíz del repositorio:

```powershell
python -m src.evaluation.build_evalset_from_sunat_excel `
  --input data/interim/sunat_evalset_input_v0.1.xlsx `
  --output data/processed/evalset_v0.1.csv `
  --source-url "http://www.aduanet.gob.pe/aduanas/informgest/sgdespa.htm#REGIMENES_DEFINITIVOS" `
  --fecha-consulta 2026-06-13 `
  --origen-caso SUNAT_ADUANET
```

Si `data/processed/evalset_v0.1.csv` ya existe y se desea reemplazarlo, agregar `--overwrite`.

El script también acepta archivos `.csv` con formato de tabla simple:

```powershell
python -m src.evaluation.build_evalset_from_sunat_excel `
  --input data/interim/sunat_evalset_input_v0.1.csv `
  --format table `
  --fecha-consulta 2026-06-13
```

## Salidas generadas

El script genera:

- `data/processed/evalset_v0.1.csv`
- `data/processed/evalset_v0.1_metadata.json`

El metadata registra rutas, fecha de consulta, formato detectado, columnas detectadas, reglas aplicadas, conteos y hashes SHA-256 del input y output.

## Validación

Después de generar el CSV, el script ejecuta las reglas del validador del evalset. También puede validarse manualmente:

```powershell
python -m src.evaluation.validate_dataset data/processed/evalset_v0.1.csv
```

La advertencia por tener menos de 300 casos no bloquea la generación, pero el evalset final de la investigación debe tener aproximadamente 300 instancias antes de usarse para validar hipótesis.