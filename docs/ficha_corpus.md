# Ficha del corpus documental v0.1

## 1. Identificación general

- **Nombre del corpus:** Corpus documental normativo NANDINA-Arancel v0.1.
- **Proyecto:** Gestión de información documental para la recomendación auditable de subpartidas NANDINA mediante recuperación documental y LLM+RAG: piloto experimental offline.
- **Versión de la ficha:** v0.1.
- **Fecha de elaboración:** 2026-05-13.
- **Responsable de curación:** Vladimir Molleapasa Gutiérrez.
- **Estado del corpus:** Preliminar; pendiente de validación completa de extracción, segmentación y cobertura.
- **Uso previsto:** Recuperación documental, generación de candidatos, reordenamiento LLM+RAG y explicación basada en evidencia para evaluación offline.

## 2. Documentos fuente incluidos

| doc_id | Documento | Tipo de fuente | Rol en el corpus | Estado de uso |
|---|---|---|---|---|
| `nandina` | NANDINA / Nomenclatura Arancelaria Común de los Países Miembros de la Comunidad Andina | Norma o nomenclatura arancelaria regional | Fuente principal para subpartidas NANDINA de ocho dígitos | Incluido como documento base |
| `arancel` | Arancel de Aduanas / documento arancelario complementario | Documento normativo o técnico-arancelario | Fuente complementaria para reglas, notas, estructura arancelaria y contexto normativo | Incluido como documento complementario |

> **Nota de trazabilidad:** esta ficha registra el corpus documental inicial declarado para el piloto. En la siguiente iteración deben completarse los nombres exactos de archivo, ubicación en el repositorio, fecha de descarga, institución emisora, versión normativa y hash de cada documento fuente.

## 3. Cobertura documental prevista

El corpus v0.1 se orienta a cubrir información normativa y técnico-arancelaria necesaria para la recomendación auditable de subpartidas NANDINA. La cobertura esperada incluye:

- estructura jerárquica de la nomenclatura: secciones, capítulos, partidas y subpartidas;
- códigos NANDINA de ocho dígitos;
- descripciones legales o técnico-arancelarias asociadas a cada código;
- reglas generales de interpretación, cuando estén disponibles en el documento fuente;
- notas de sección y notas de capítulo, cuando estén disponibles;
- referencias complementarias contenidas en el Arancel de Aduanas o documento arancelario utilizado.

## 4. Alcance del corpus

El corpus será utilizado únicamente para fines académicos y experimentales. Su función dentro del piloto es servir como base documental para:

1. construir fragmentos recuperables;
2. generar candidatos Top-N mediante recuperación documental;
3. aportar evidencia para el componente LLM+RAG;
4. sustentar explicaciones auditables;
5. permitir trazabilidad entre recomendación, fragmento recuperado y documento fuente.

El corpus no convierte las salidas del piloto en clasificación oficial ni sustituye la revisión experta. Las recomendaciones producidas serán resultados experimentales bajo condiciones offline.

## 5. Criterios de inclusión

Se incluirán documentos que cumplan al menos una de las siguientes condiciones:

- contienen estructura NANDINA o información directamente relacionada con subpartidas NANDINA;
- contienen reglas generales, notas legales, notas de sección, notas de capítulo o descripciones arancelarias relevantes;
- proceden de fuentes públicas, institucionales o autorizadas para uso académico;
- tienen procedencia identificable y pueden ser versionados;
- son convertibles a texto para fines de segmentación y recuperación documental.

## 6. Criterios de exclusión

Se excluirán o no se usarán como fuente activa del corpus:

- documentos sin procedencia verificable;
- versiones duplicadas sin control de cambios;
- documentos corruptos o no convertibles a texto útil;
- archivos sin autorización de uso académico o con restricciones incompatibles con el piloto;
- fragmentos que no aporten información normativa, arancelaria o técnica relevante;
- documentos cuyo contenido no pueda vincularse de forma trazable con la recomendación de subpartidas.

## 7. Formato y procesamiento documental

### 7.1. Formato fuente

Los documentos fuente pueden encontrarse inicialmente en formato PDF, DOCX, XLSX, CSV, HTML u otro formato documental. Para el piloto, los documentos deberán convertirse a una representación textual estructurada.

### 7.2. Formato procesado esperado

El corpus procesado se almacenará preferentemente en formato `JSONL`, con un registro por fragmento documental. También podrá mantenerse una versión tabular en `CSV` o `Parquet` para inspección y validación.

Campos mínimos esperados por fragmento:

```json
{
  "chunk_id": "nandina_v0.1_cap84_000001",
  "doc_id": "nandina",
  "titulo_documento": "NANDINA",
  "version_documento": "pendiente",
  "fuente": "pendiente",
  "fecha_descarga": "pendiente",
  "seccion": "pendiente",
  "capitulo": "pendiente",
  "partida": "pendiente",
  "subpartida": "pendiente",
  "tipo_fragmento": "descripcion_subpartida | nota | regla | otro",
  "texto_fragmento": "pendiente",
  "pagina_origen": "pendiente",
  "ruta_archivo_origen": "pendiente"
}
```

## 8. Estrategia preliminar de segmentación

La segmentación deberá preservar la relación entre el fragmento y su contexto jerárquico. Se propone la siguiente granularidad inicial:

| Tipo de contenido | Unidad recuperable recomendada | Observación |
|---|---|---|
| Descripción de subpartida | Una subpartida por fragmento | Debe conservar capítulo, partida y código NANDINA. |
| Notas de sección | Una nota o bloque normativo por fragmento | Debe conservar sección y referencia documental. |
| Notas de capítulo | Una nota o bloque normativo por fragmento | Debe conservar capítulo y página o ubicación. |
| Reglas generales | Una regla por fragmento | Debe conservar numeración y texto completo. |
| Texto complementario del arancel | Fragmentos temáticos breves | Solo si aporta evidencia útil para explicación. |

La segmentación no debe cortar códigos, notas o reglas de forma que pierdan significado normativo. Cuando un fragmento dependa de su jerarquía, deben agregarse metadatos de contexto.

## 9. Metadatos obligatorios

Cada documento fuente deberá registrar:

- `doc_id`;
- `titulo_documento`;
- `institucion_emisora`;
- `version_documento`;
- `fecha_publicacion`;
- `fecha_descarga`;
- `url_fuente` o referencia de procedencia;
- `ruta_archivo_origen`;
- `formato_original`;
- `hash_archivo`, cuando se calcule;
- `restricciones_uso`;
- `observaciones_curacion`.

Cada fragmento documental deberá registrar:

- `chunk_id`;
- `doc_id`;
- `tipo_fragmento`;
- `texto_fragmento`;
- `pagina_origen` o ubicación equivalente;
- `seccion`, si aplica;
- `capitulo`, si aplica;
- `partida`, si aplica;
- `subpartida`, si aplica;
- `version_corpus`.

## 10. Restricciones de uso

- El corpus se usará exclusivamente para investigación académica y evaluación experimental offline.
- No se publicarán datos sensibles, documentos restringidos ni registros institucionales no autorizados.
- Los documentos normativos públicos podrán referenciarse y documentarse, pero su redistribución dependerá de las condiciones de la fuente original.
- En el repositorio Git se versionarán código, documentación, configuraciones, fichas y salidas reproducibles. Los archivos fuente de gran tamaño o con restricciones de redistribución podrán mantenerse fuera del repositorio y documentarse mediante metadatos.

## 11. Riesgos y limitaciones del corpus

| Riesgo o limitación | Impacto potencial | Medida de control |
|---|---|---|
| Versión normativa desactualizada | Recomendaciones basadas en texto no vigente | Registrar versión, fecha y fuente de cada documento. |
| Errores de extracción desde PDF | Fragmentos incompletos o mal segmentados | Validación manual de muestra y control de calidad textual. |
| Pérdida de contexto jerárquico | Recuperación de fragmentos sin relación clara con capítulo o partida | Incorporar metadatos jerárquicos obligatorios. |
| Ambigüedad entre texto de NANDINA y Arancel | Evidencia documental mezclada o no distinguible | Usar `doc_id`, `tipo_fragmento` y `ruta_archivo_origen`. |
| Cobertura incompleta de notas o reglas | Explicaciones débiles o no auditables | Registrar vacíos de cobertura y actualizar corpus en versiones posteriores. |
| Restricciones de redistribución | Imposibilidad de publicar archivos fuente completos | Versionar fichas, hashes, scripts y rutas; excluir archivos restringidos. |

## 12. Control de versiones

| Versión | Fecha | Descripción | Responsable |
|---|---|---|---|
| v0.1 | 2026-05-13 | Ficha inicial del corpus documental NANDINA-Arancel para el piloto experimental offline. | Vladimir Molleapasa Gutiérrez |

## 13. Pendientes de validación

Antes de ejecutar la indexación y recuperación, deben completarse los siguientes puntos:

- confirmar ruta exacta de los archivos fuente en el repositorio o almacenamiento local;
- registrar nombre exacto de cada archivo;
- registrar institución emisora y versión normativa;
- registrar fecha de descarga o incorporación;
- calcular hash de integridad de cada archivo;
- verificar si los documentos pueden redistribuirse en Git o deben mantenerse fuera del repositorio;
- ejecutar una extracción preliminar de texto;
- validar manualmente una muestra de fragmentos;
- generar `corpus_chunks_v0.1.jsonl`.

## 14. Criterio de aceptación de la versión v0.1

La versión v0.1 del corpus será considerada lista para indexación cuando cumpla con lo siguiente:

- al menos dos documentos fuente registrados: NANDINA y Arancel;
- metadatos mínimos completos para cada documento;
- fragmentos generados con `chunk_id` único;
- preservación de jerarquía arancelaria en los metadatos;
- validación manual de una muestra de fragmentos;
- almacenamiento de la salida procesada en un formato reproducible;
- registro de la configuración de extracción y segmentación.
