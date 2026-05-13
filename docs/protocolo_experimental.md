# Protocolo experimental preliminar

Este documento resume las fases previstas para el piloto experimental offline.

## 1. Curación documental

Objetivo: construir o consolidar un corpus documental de referencia para NANDINA y documentos normativos relacionados.

Actividades principales:

- Identificar fuentes documentales públicas o autorizadas.
- Registrar fuente, fecha, versión y criterios de inclusión.
- Convertir documentos a texto cuando corresponda.
- Segmentar el corpus en unidades recuperables.
- Asignar metadatos mínimos: documento, sección, fragmento, versión y procedencia.

Producto verificable: corpus documentado y ficha de corpus.

## 2. Preparación de casos de evaluación

Objetivo: preparar instancias con descripción textual y subpartida NANDINA de referencia.

Actividades principales:

- Validar formato de subpartida de ocho dígitos.
- Depurar duplicados, registros incompletos o descripciones inválidas.
- Registrar criterios de exclusión.
- Documentar fuente, fecha y cobertura de los casos.

Producto verificable: dataset de evaluación documentado.

## 3. Recuperación documental base

Objetivo: generar candidatos Top-N para cada descripción textual.

Actividades principales:

- Definir estrategia de indexación.
- Ejecutar recuperación base por instancia.
- Registrar ranking inicial, puntajes y fragmentos recuperados.
- Calcular cobertura Top-N y métricas iniciales de ranking.

Producto verificable: ranking base y métricas de recuperación.

## 4. Reordenamiento y explicación mediante LLM+RAG

Objetivo: reordenar candidatos y producir una explicación auditable con evidencia documental.

Actividades principales:

- Diseñar plantilla de prompt.
- Incluir candidatos, fragmentos recuperados y restricciones de respuesta.
- Generar salida estructurada por caso.
- Registrar modelo, versión, temperatura, fecha y configuración.

Producto verificable: salidas estructuradas con justificación y evidencia.

## 5. Evaluación

Objetivo: medir desempeño de recomendación y calidad de explicación.

Métricas cuantitativas previstas:

- Top-1, Top-3 y Top-5.
- Mean Reciprocal Rank (MRR).
- Normalized Discounted Cumulative Gain (nDCG).

Criterios cualitativos previstos:

- Verificabilidad.
- Trazabilidad.
- Pertinencia documental.
- Concordancia evidencia-justificación.
- Claridad para auditoría.

Producto verificable: tablas de resultados, rúbrica aplicada y análisis de errores.
