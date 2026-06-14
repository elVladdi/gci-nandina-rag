# Ficha del dataset de evaluacion final v0.1

## Identificacion

- Nombre del dataset: `evalset_v0.1`.
- Ruta del dataset final: `data/processed/evalset_v0.1.csv`.
- Metadata asociada: `data/processed/evalset_v0.1_metadata.json`.
- Plantilla versionable: `docs/templates/evalset_v0.1_template.csv`.
- Estado actual: dataset final v0.1 generado, deduplicado y validado.

## Proposito

Construir un dataset separado para evaluacion final del pipeline offline LLM+RAG NANDINA, evitando mezclar casos de desarrollo con casos destinados a medir resultados finales.

## Fuente

Fuente usada: SUNAT ADUANET, pagina de informacion sobre regimenes definitivos:

`http://www.aduanet.gob.pe/aduanas/informgest/sgdespa.htm#REGIMENES_DEFINITIVOS`

Archivo local de preparacion: Excel SUNAT real procesado en modo `sunat-block`.

## Preparacion

- Fecha de consulta: 2026-06-13.
- Responsable de preparacion: pendiente de consignar por el usuario.
- Tamano objetivo metodologico: aproximadamente 300 casos.
- Tamano actual: 600 casos unicos validos.
- Total extraido antes de deduplicar: 647 casos.
- Duplicados exactos excluidos: 47 filas.
- Grupos duplicados exactos detectados: 31.
- Total final: 600 casos.
- Distribucion por regimen: regimen `10` con 599 casos en el evalset deduplicado; regimen `12` con 1 caso. El regimen `10` corresponde al alcance empirico dominante de importacion para el consumo.

## Criterios de inclusion

- Casos con descripcion suficiente para ejecutar recuperacion documental.
- Casos con codigo NANDINA de referencia a ocho digitos.
- Casos con regimen asociado.
- Casos trazables a la fuente consultada y a una fecha de consulta.
- Casos preparados de forma separada al devset preliminar.
- Casos unicos segun la llave `descripcion + nandina_ref + regimen`.

## Criterios de exclusion

- Registros sin descripcion, NANDINA o regimen.
- Registros con NANDINA incompleta, no numerica o distinta de ocho digitos.
- Registros sin fuente o fecha de consulta.
- Duplicados exactos por `case_id` o por la combinacion `descripcion + nandina_ref + regimen`.
- Casos cuya procedencia no pueda documentarse suficientemente.

## Campos obligatorios

| Campo | Descripcion |
| --- | --- |
| `case_id` | Identificador unico del caso. |
| `descripcion` | Descripcion comercial o documental del caso. |
| `nandina_ref` | Codigo NANDINA de referencia con ocho digitos. |
| `regimen` | Regimen asociado al caso. |
| `fuente_url` | URL de la fuente consultada. |
| `fecha_consulta` | Fecha de consulta o preparacion del caso. |

## Campos opcionales

| Campo | Descripcion |
| --- | --- |
| `capitulo` | Dos primeros digitos de `nandina_ref`, informado o derivable. |
| `partida` | Cuatro primeros digitos de `nandina_ref`, informado o derivable. |
| `origen_caso` | Nota sobre el origen documental u operativo del caso. |
| `observaciones` | Trazabilidad de hoja, serie, filas y descripcion de partida cuando proviene del reporte SUNAT por bloques. |

## Anonimizacion

La fuente prevista es publica y documental. Si en fases posteriores se incorporan descripciones provenientes de documentos operativos, deben removerse identificadores de personas, empresas, numeros de declaracion, direcciones, contactos u otros datos sensibles que no sean necesarios para la evaluacion metodologica.

## Limitaciones

- La ficha no acredita resultados ni validacion final de hipotesis.
- El evalset supera el objetivo minimo aproximado de 300 instancias; se conserva completo por ser trazable y validado.
- Existe alta concentracion por regimen: el regimen `10` concentra 599 de 600 casos y el regimen `12` aporta 1 caso.
- La concentracion por regimen debe considerarse al interpretar resultados finales y al discutir generalizacion; los resultados no deben extrapolarse automaticamente a otros regimenes aduaneros.
- La calidad del evalset depende de la consistencia del reporte SUNAT fuente, de la extraccion por bloques y de la politica de deduplicacion exacta aplicada.