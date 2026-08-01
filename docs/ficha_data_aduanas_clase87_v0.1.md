# Ficha data_aduanas clase 87 v0.1

## Identificacion

- Nombre metodologico: `data_aduanas`.
- Version de particiones: `data_aduanas_splits_clase87_v0.1`.
- Alcance: `Clase = 87`.
- Script generador: `src/evaluation/build_data_aduanas_splits.py`.
- Metadata: `data/processed/data_aduanas_splits_clase87_v0.1_metadata.json`.
- Auditorias regenerables: `outputs/audits/data_aduanas_splits_clase87_v0.1/`.

## Fuente

La fuente fisica local es `data/Series - Descripciones.xlsx`. No se versiona en Git por politica de datos locales. La capa normalizada usada para esta version es:

```text
data/interim/sunat_series_descripciones_normalized.csv
```

La capa normalizada fue producida por `src/ingestion/sunat_series_parser.py`, que preserva etiquetas SUNAT, deriva `id_unico` como `DECLARACION-SERIE` y agrega columnas tecnicas de trazabilidad con prefijo `__`.

## Tamano y composicion

| Concepto | Conteo |
| --- | ---: |
| Series normalizadas fuente | 11,320 |
| Instancias fuente en `Clase = 87` | 4,232 |
| NANDINAS distintas fuente en `Clase = 87` | 69 |
| Filas curadas finales | 4,106 |
| Excluidas por campos/calidad | 0 |
| Excluidas por duplicados `id_unico` | 126 |

## Particiones finales

| Split | Ruta | Filas | NANDINAS distintas |
| --- | --- | ---: | ---: |
| historico | `data/processed/data_aduanas_historico_clase87_v0.1.csv` | 3,000 | 69 |
| desarrollo | `data/processed/data_aduanas_devset_clase87_v0.1.csv` | 100 | 44 |
| evaluacion | `data/processed/data_aduanas_evalset_clase87_v0.1.csv` | 1,006 | 62 |

No hay `id_unico` repetidos dentro de las particiones ni solapamiento de `id_unico` entre particiones.

## Campos principales

Las tres particiones tienen exactamente las mismas columnas y el mismo orden. Las columnas principales son:

```text
case_id
split
id_unico
DECLARACION
SERIE
Clase
Partida
Sub Partida
NANDINA
NANDINA ORIGINAL
DESCRIPCION DE PARTIDA ARANCELARIA
DESCRIPCION DE MERCANCIAS 1
DESCRIPCION DE MERCANCIAS 2
DESCRIPCION DE MERCANCIAS 3
DESCRIPCION DE MERCANCIAS 4
DESCRIPCION DE MERCANCIAS 5
DESCRIPCION DE MERCANCIAS CONCATENADA
```

Despues de las columnas principales se conservan columnas SUNAT adicionales y columnas tecnicas de trazabilidad disponibles en la capa normalizada.

## Uso previsto

- `historico`: banco inicial de precedentes para recuperacion historica o modelos posteriores.
- `desarrollo`: desarrollo, pruebas de humo y seleccion preliminar de configuraciones.
- `evaluacion`: evaluacion controlada futura despues de congelar decisiones en desarrollo.

El historico de 3,000 instancias se adopta para disponer de masa suficiente de precedentes y, al mismo tiempo, reservar un bloque separado de evaluacion. El devset pequeno permite iterar sin tocar el conjunto de evaluacion.

## Limitaciones

- La ficha no valida hipotesis ni reporta desempeno de recuperacion.
- El alcance es solo `Clase = 87`.
- La cobertura por NANDINA en desarrollo/evaluacion depende de la disponibilidad posterior a la curacion y de cuotas proporcionales; no se fuerzan duplicados para cubrir estratos escasos.
- El evalset v0.1 anterior queda historico; no debe mezclarse automaticamente con estas particiones.
