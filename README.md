# Gestión de información documental para la recomendación auditable de subpartidas NANDINA mediante recuperación documental y LLM+RAG

Repositorio del proyecto de investigación de maestría en Gestión del Conocimiento e Información.

**Título del proyecto:** Gestión de información documental para la recomendación auditable de subpartidas NANDINA mediante recuperación documental y LLM+RAG: piloto experimental offline.

## Descripción

Este repositorio contiene la estructura inicial, documentación técnica y artefactos reproducibles del piloto experimental offline orientado a evaluar un enfoque de gestión de información documental para la recomendación auditable de subpartidas NANDINA.

El proyecto busca organizar, recuperar, reordenar y explicar evidencia documental normativa para apoyar la recomendación de subpartidas NANDINA a partir de descripciones textuales de mercancías. El piloto no sustituye la revisión experta ni produce clasificación oficial de mercancías; sus salidas tienen finalidad estrictamente experimental y académica.

## Enfoque general

El pipeline experimental contempla cinco componentes principales:

1. Curación y documentación del corpus normativo.
2. Preparación de casos de evaluación con descripción textual y subpartida de referencia.
3. Recuperación documental base para generar candidatos Top-N.
4. Reordenamiento y explicación mediante LLM+RAG.
5. Evaluación cuantitativa y cualitativa del desempeño y de la explicación auditable.

## Alcance

El estudio se delimita a una evaluación offline. No se contempla despliegue productivo, integración con sistemas institucionales, clasificación oficial ni reemplazo de especialistas. La investigación se concentra en subpartidas NANDINA de ocho dígitos y en la evaluación de desempeño Top-k/ranking, trazabilidad documental y calidad de explicación basada en evidencia.

## Estructura del repositorio

```text
.
├── data/              # Datos locales o referencias a datos; no subir información sensible
├── docs/              # Documentación metodológica, fichas y notas del proyecto
├── notebooks/         # Cuadernos de exploración, validación y experimentación
├── outputs/           # Resultados generados por corridas experimentales
├── src/               # Código fuente del pipeline experimental
├── .gitignore         # Reglas para excluir archivos locales, temporales o sensibles
└── README.md          # Descripción general del repositorio
```

## Principios de trabajo

- Mantener trazabilidad de corpus, configuraciones y resultados.
- Registrar versiones de documentos, parámetros, prompts y salidas.
- Evitar subir datos sensibles, confidenciales o no anonimizados.
- Separar datos fuente, datos procesados, código y resultados.
- Priorizar reproducibilidad, auditabilidad y documentación.

## Métricas previstas

El desempeño de recomendación se evaluará mediante métricas como Top-1, Top-3, Top-5, Mean Reciprocal Rank (MRR) y Normalized Discounted Cumulative Gain (nDCG). La calidad de explicación se evaluará mediante criterios de verificabilidad, trazabilidad, pertinencia documental y concordancia evidencia-justificación.

## Estado del repositorio

Estructura inicial creada para organizar el desarrollo del proyecto. La implementación técnica, los experimentos y la documentación metodológica se incorporarán progresivamente.

## Nota de confidencialidad

No deben subirse al repositorio registros sensibles, datos personales, documentos no autorizados o información institucional restringida. Los datos de evaluación deben documentarse y anonimizarse según corresponda antes de cualquier uso compartido.
