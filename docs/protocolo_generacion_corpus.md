# Protocolo de generación del corpus documental v0.1

## 1. Propósito

Este documento describe el procedimiento utilizado para generar el corpus documental procesado del proyecto **Gestión de información documental para la recomendación auditable de subpartidas NANDINA mediante recuperación documental y LLM+RAG: piloto experimental offline**.

El protocolo tiene tres finalidades:

1. asegurar trazabilidad documental;
2. permitir reproducibilidad del procesamiento;
3. dejar evidencia metodológica sobre cómo se transforma el material normativo fuente en fragmentos recuperables.

El corpus generado no constituye una versión oficial de la NANDINA ni del Arancel de Aduanas. Su uso se limita a investigación académica y evaluación experimental offline.

## 2. Documentos fuente

La versión v0.1 del corpus utiliza dos documentos fuente ubicados en `data/external`:

| doc_id | Documento fuente | Rol en el corpus |
|---|---|---|
| `nandina_decision_885` | CAN Decisión 885 - Nomenclatura Común NANDINA | Fuente normativa principal para subpartidas NANDINA, estructura jerárquica y disposiciones comunes. |
| `arancel_2022` | Arancel de Aduanas 2022 | Fuente complementaria operativa para reglas generales, estructura arancelaria, notas, unidades físicas y contexto aplicado. |

La inclusión de estos documentos permite construir una primera base documental suficiente para extracción, segmentación, recuperación y explicación basada en evidencia.

## 3. Ubicación esperada de archivos

El script espera encontrar los PDF en:

```text
data/external/
```

Los nombres de archivo pueden contener espacios, tildes o variaciones menores. El script utiliza patrones flexibles para ubicar:

```text
*Arancel*2022*.pdf
*885*NANDINA*.pdf
*885*Nandina*.pdf
*885*Nanadina*.pdf
*885*.pdf
```

Si algún documento no es localizado, la corrida continúa con los documentos disponibles y registra una advertencia en el reporte.

## 4. Script responsable

El procesamiento se ejecuta mediante:

```text
src/corpus/build_corpus.py
```

Comando básico:

```bash
python src/corpus/build_corpus.py
```

Comando con rutas explícitas:

```bash
python src/corpus/build_corpus.py \
  --external-dir data/external \
  --output-dir data/processed/corpus
```

## 5. Dependencias

El script intenta extraer texto desde PDF usando, en este orden:

1. `pypdf`;
2. `PyMuPDF`, mediante el paquete `pymupdf`.

Instalación sugerida:

```bash
pip install pypdf
```

Alternativa:

```bash
pip install pymupdf
```

En una versión posterior del proyecto, estas dependencias deberán consolidarse en `requirements.txt`.

## 6. Salidas generadas

La ejecución genera los siguientes artefactos:

```text
data/processed/corpus/
├── corpus_chunks_v0.1.jsonl
├── corpus_documents_v0.1.csv
└── corpus_generation_report_v0.1.md
```

### 6.1. `corpus_chunks_v0.1.jsonl`

Contiene un fragmento documental por línea en formato JSON. Es el archivo principal para indexación, recuperación documental y RAG.

Campos principales:

| Campo | Descripción |
|---|---|
| `chunk_id` | Identificador único del fragmento. |
| `version_corpus` | Versión del corpus procesado. |
| `doc_id` | Identificador del documento fuente. |
| `titulo_documento` | Título normalizado del documento. |
| `ruta_archivo_origen` | Ruta del archivo fuente. |
| `pagina` | Página desde la cual fue extraído el fragmento. |
| `bloque_en_pagina` | Número del bloque dentro de la página. |
| `tipo_fragmento` | Clasificación heurística del fragmento. |
| `seccion` | Sección detectada, si corresponde. |
| `capitulo` | Capítulo detectado, si corresponde. |
| `partida` | Partida detectada, si corresponde. |
| `subpartida` | Subpartida detectada, si corresponde. |
| `codigo_detectado` | Código arancelario detectado en el fragmento. |
| `texto_fragmento` | Texto normalizado del fragmento. |
| `hash_texto_sha256` | Hash SHA-256 del texto del fragmento. |

### 6.2. `corpus_documents_v0.1.csv`

Contiene el inventario de documentos procesados. Registra metadatos como nombre de archivo, hash SHA-256, tamaño, número de páginas y número de caracteres extraídos.

### 6.3. `corpus_generation_report_v0.1.md`

Resume la corrida de procesamiento. Incluye documentos procesados, fragmentos generados, tipos de fragmento y observaciones metodológicas.

## 7. Estrategia de extracción

El script extrae texto página por página. Esta decisión permite conservar trazabilidad mínima entre fragmento y ubicación documental.

El procesamiento por página facilita:

- inspección manual de errores;
- vinculación de evidencia con fuente;
- reporte de página de origen;
- reconstrucción parcial del contexto normativo.

## 8. Estrategia de limpieza

La limpieza textual es conservadora. El script realiza:

- eliminación de caracteres nulos;
- eliminación de guiones blandos;
- normalización de espacios repetidos;
- reducción de saltos de línea excesivos;
- eliminación limitada de encabezados o pies de página repetitivos.

No se eliminan tildes, códigos, puntuación normativa ni términos técnicos.

## 9. Estrategia de segmentación

La segmentación inicial es heurística. El script divide el texto por página y luego agrupa párrafos o líneas en bloques de tamaño controlado.

Parámetros iniciales:

| Parámetro | Valor aproximado |
|---|---:|
| Longitud mínima de bloque | 80 caracteres |
| Longitud máxima de bloque | 1800 caracteres |

La decisión busca equilibrar dos necesidades:

1. que los fragmentos sean suficientemente breves para recuperación y citación;
2. que conserven suficiente contexto para explicación auditable.

## 10. Tipos de fragmento

El script asigna un tipo de fragmento mediante reglas heurísticas:

| tipo_fragmento | Descripción |
|---|---|
| `regla_general_titulo` | Título de sección de reglas generales. |
| `regla_general` | Fragmento asociado a una regla general de interpretación. |
| `consideracion_general` | Consideraciones generales del documento. |
| `consideracion_arancel` | Consideraciones sobre el Arancel de Aduanas. |
| `titulo_seccion` | Encabezado de sección. |
| `titulo_capitulo` | Encabezado de capítulo. |
| `nota_complementaria` | Nota complementaria NANDINA o nacional. |
| `nota` | Nota de sección, capítulo o subpartida. |
| `descripcion_arancelaria` | Fragmento con código o descripción arancelaria. |
| `texto_normativo` | Texto normativo no clasificado en las categorías anteriores. |

Estos tipos no reemplazan una curación jurídica o aduanera experta. Sirven para organizar la primera versión recuperable del corpus.

## 11. Metadatos jerárquicos

El script intenta detectar:

- sección;
- capítulo;
- partida;
- subpartida;
- código arancelario visible.

La detección se basa en patrones textuales. En consecuencia, debe validarse antes de usar el corpus como base definitiva para evaluación.

## 12. Control de integridad

Cada documento fuente recibe un hash SHA-256. Cada fragmento textual recibe también un hash SHA-256 sobre el texto normalizado.

Esto permite:

- detectar cambios en archivos fuente;
- detectar cambios en fragmentos;
- reconstruir corridas experimentales;
- documentar versiones del corpus.

## 13. Limitaciones de la versión v0.1

La versión v0.1 tiene las siguientes limitaciones:

- la extracción desde PDF puede introducir errores en tablas;
- la segmentación por página puede cortar relaciones entre notas y descripciones;
- la detección de códigos puede capturar códigos nacionales de diez dígitos cuando se procese el Arancel;
- la inferencia de jerarquía es preliminar;
- la clasificación de tipos de fragmento es heurística;
- no existe aún validación manual completa;
- no se han construido todavía índices BM25 o vectoriales.

## 14. Criterios de aceptación de la corrida

Una corrida será aceptada para experimentación preliminar si cumple:

- procesa al menos un documento fuente principal;
- genera `corpus_chunks_v0.1.jsonl`;
- genera `corpus_documents_v0.1.csv`;
- genera reporte Markdown de la corrida;
- asigna `chunk_id` único por fragmento;
- conserva página de origen;
- registra hash de documento y hash de fragmento;
- permite inspección manual de fragmentos.

Para una evaluación formal, además deberá verificarse manualmente una muestra de reglas generales, notas y subpartidas.

## 15. Procedimiento reproducible

1. Confirmar que los PDF estén en `data/external`.
2. Instalar dependencias mínimas.
3. Ejecutar el script.
4. Revisar el reporte generado.
5. Inspeccionar manualmente una muestra de fragmentos.
6. Registrar observaciones en la ficha del corpus.
7. Realizar commit de código, documentación y salidas reproducibles permitidas.

Ejemplo:

```bash
python src/corpus/build_corpus.py

git add src/corpus/build_corpus.py docs/protocolo_generacion_corpus.md data/processed/corpus/
git commit -m "data: generate corpus v0.1"
```

## 16. Próximo hito

El siguiente hito metodológico será construir un primer índice de recuperación base sobre `corpus_chunks_v0.1.jsonl`, preferentemente con BM25, y evaluar si las descripciones de prueba recuperan fragmentos normativos pertinentes dentro de Top-N.
