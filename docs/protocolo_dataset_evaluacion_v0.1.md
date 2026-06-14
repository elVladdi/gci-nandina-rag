# Protocolo del dataset de evaluacion final v0.1

Este documento define el protocolo de preparacion del dataset separado de evaluacion final del piloto offline LLM+RAG NANDINA. Su objetivo es dejar listo el esquema, trazabilidad y control de calidad para que los casos puedan ser completados manualmente en una fase posterior sin modificar el devset preliminar existente.

## Alcance de Fase 3A

La Fase 3A no ejecuta evaluacion final, no reporta resultados y no valida hipotesis de investigacion. Solo prepara el protocolo, ficha, plantilla y validador del dataset de evaluacion final.

El archivo `data/processed/devset_validacion_intermedia.csv` se conserva intacto como devset preliminar de 13 casos para desarrollo, validacion intermedia y smoke tests. Ese archivo no debe ampliarse ni mezclarse con el dataset final.

El dataset de evaluacion final v0.1 queda congelado en `data/processed/evalset_v0.1.csv`, con metadata en `data/processed/evalset_v0.1_metadata.json`. La plantilla versionable queda en `docs/templates/evalset_v0.1_template.csv`.

## Fuente prevista

La fuente prevista para preparar los casos es la pagina oficial SUNAT ADUANET:

`http://www.aduanet.gob.pe/aduanas/informgest/sgdespa.htm#REGIMENES_DEFINITIVOS`

El usuario preparara o descargara manualmente los casos desde esa fuente, registrando como minimo descripcion, NANDINA y regimen. Cada caso debe conservar campos de trazabilidad que permitan reproducir la consulta o preparacion posterior.

## Tamano objetivo

El objetivo metodologico del evalset es aproximadamente 300 instancias, de acuerdo con la evidencia y alcance del proyecto de investigacion. Una muestra menor puede usarse para pruebas tecnicas del validador o del pipeline, pero no debe presentarse como validacion final de hipotesis.


## Decision metodologica de Fase 3B-2B

El Excel SUNAT real permitio extraer 647 casos validos antes de deduplicar. Luego de aplicar deduplicacion exacta por `descripcion + nandina_ref + regimen`, conservando la primera aparicion estable, el evalset final queda en 600 casos unicos validos.

Se usan todos los casos unicos validos y no se realiza muestreo a 300. Esta decision supera el minimo metodologico aproximado y evita un recorte arbitrario. Si en una fase futura se requiere limitar el tamano del evalset, debe hacerse mediante muestreo documentado y reproducible.

La deduplicacion exacta se aplica antes de cualquier evaluacion final para evitar que una misma combinacion metodologica tenga peso multiple en las metricas.

El alcance empirico queda delimitado por la composicion del Excel SUNAT procesado: 599 de 600 casos finales pertenecen al regimen `10` (importacion para el consumo) y 1 caso al regimen `12`. Por tanto, las conclusiones experimentales que se obtengan con este evalset no deben generalizarse automaticamente a otros regimenes aduaneros.

## Separacion entre devset y evalset

- `data/processed/devset_validacion_intermedia.csv`: devset preliminar de 13 casos, solo para desarrollo, pruebas de humo y validacion intermedia.
- `data/processed/evalset_v0.1.csv`: dataset separado de evaluacion final, a construir en fases posteriores.
- Los casos no deben duplicarse deliberadamente entre ambos archivos.
- Las metricas finales deben declararse solo sobre el evalset final y con el protocolo experimental correspondiente.

## Esquema minimo obligatorio

El archivo `evalset_v0.1.csv` debe contener las siguientes columnas obligatorias:

| Campo | Tipo esperado | Regla minima |
| --- | --- | --- |
| `case_id` | texto | Identificador unico y estable del caso. |
| `descripcion` | texto | Descripcion comercial o documental no vacia. |
| `nandina_ref` | texto | Codigo NANDINA de referencia con exactamente 8 digitos. |
| `regimen` | texto | Regimen asociado al caso, no vacio. |
| `fuente_url` | texto | URL de la fuente consultada, no vacia. |
| `fecha_consulta` | texto | Fecha de consulta o preparacion, no vacia; se recomienda formato ISO `AAAA-MM-DD`. |

## Campos opcionales o derivados

Se permiten las siguientes columnas adicionales:

| Campo | Tipo esperado | Uso |
| --- | --- | --- |
| `capitulo` | texto | Puede derivarse de los dos primeros digitos de `nandina_ref`; si se informa, debe coincidir. |
| `partida` | texto | Puede derivarse de los cuatro primeros digitos de `nandina_ref`. |
| `origen_caso` | texto | Nota corta sobre el origen operativo o documental del caso. |
| `observaciones` | texto | Comentarios de curacion, ambiguedades o decisiones de preparacion. |

## Reglas de calidad

- `nandina_ref` debe conservar ceros iniciales y tener exactamente 8 digitos.
- `descripcion`, `regimen`, `fuente_url` y `fecha_consulta` no deben estar vacios.
- `case_id` debe ser unico.
- La combinacion `descripcion + nandina_ref + regimen` no debe repetirse.
- Si `capitulo` existe y tiene valor, debe coincidir con los dos primeros digitos de `nandina_ref`.
- Los campos de trazabilidad deben permitir identificar la fuente y la fecha de consulta usada para preparar cada caso.

## Politica de interpretacion

Hasta completar las fases posteriores con un evalset suficiente y validado, no se debe afirmar validacion final de hipotesis. Cualquier corrida sobre muestras incompletas o sobre el devset preliminar debe reportarse como prueba tecnica, exploratoria o de humo.
