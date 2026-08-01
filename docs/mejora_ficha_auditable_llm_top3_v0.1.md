# Mejora de ficha auditable LLM Top-3 v0.1

## Motivacion de Fase 10D

La Fase 10C cerro la revision cualitativa de 10 fichas auditables producidas en Fase 10B. La conclusion fue positiva para trazabilidad formal: las fichas permiten identificar el caso, conservar el Top-3 fijo, rastrear evidencia historica y normativa, y revisar la comparacion entre candidatos.

La misma revision mostro limites cualitativos que conviene corregir antes de una corrida mayor:

- La evidencia normativa residual o generica, como "Los demas" o "Partes", a veces se leia como soporte sustantivo.
- La evidencia historica dominaba la explicacion.
- Algunas conclusiones sonaban mas decisivas que el soporte declarado.
- Faltaba una senal visible de escalamiento cuando el Top-3 era debil o la norma no discriminaba.

Fase 10D se define como una fase corta de mejora de diseno. No ejecuta generacion masiva, no recalcula recuperacion y no cambia metricas de ranking.

## Que cambia respecto a 10B

Se incorporan tres cambios versionables:

1. Prompt v0.3: refuerza tono prudente, prohibe afirmar clasificacion oficial, exige separar evidencia historica y normativa, marca normativa generica/residual, mantiene Top-3 fijo y agrega `requiere_revision_experta`.
2. Rubrica de auditabilidad: formaliza dimensiones de trazabilidad, verificabilidad, separacion historico/normativo, prudencia, consistencia con Top-3 fijo, deteccion de normativa generica y utilidad para auditoria humana.
3. Renderizador de fichas: mantiene compatibilidad con outputs 10B y, si existen campos nuevos, muestra alertas globales, tipo de evidencia normativa, lectura historica y motivo de revision experta.

No se modifica el rol metodologico del LLM. El LLM sigue siendo explicador del Top-3 fijo, no recuperador, clasificador ni re-ranker.

## Respuesta a los hallazgos de 10C

| Hallazgo 10C | Respuesta 10D |
| --- | --- |
| Trazabilidad formal fuerte | Se conserva la exigencia de `candidate_id_unico`, `evidence_id`, rank y NANDINA por candidato. |
| Evidencia normativa demasiado generica | El prompt v0.3 obliga a etiquetar norma generica/residual y prohibe tratarla como coincidencia normativa fuerte. |
| Evidencia historica domina la explicacion | La salida separa `lectura_historica` y `tipo_evidencia_normativa`, y la comparacion distingue historico vs normativo. |
| Conclusiones demasiado decisivas | El tono obligatorio usa "compatible", "sugiere" y "requiere revision experta"; se prohiben frases categoricas. |
| Mejorar formato, rubrica y prompt sin regeneracion masiva | La fase crea prompt, rubrica, cierre metodologico y ajuste compatible del renderizador; no ejecuta LLM. |

## Decision metodologica

10D mejora el diseno de explicacion auditable. No cambia las metricas de recuperacion historica ni normativa, no altera la seleccion del Top-3 y no reinterpreta los resultados cuantitativos de 10B.

La recuperacion base operativa sigue siendo historica real `data_aduanas` clase 87, con respaldo normativo. El historico conserva el rol principal y lo normativo queda como respaldo documental, trazabilidad y fuente de advertencias cuando es generico o insuficiente.

## Ejecucion LLM

No se ejecuto LLM en Fase 10D. No se uso Ollama, OpenAI, APIs remotas ni servicios con costo. No se regeneraron fichas de muestra.

## Pendiente para una eventual Fase 10E

Una Fase 10E podria ejecutar una corrida acotada o completa con prompt v0.3 para medir:

- tasa de JSON valido con el esquema extendido;
- preservacion exacta del Top-3;
- frecuencia de `requiere_revision_experta`;
- deteccion de evidencia normativa generica;
- mejora de prudencia en conclusiones;
- utilidad de fichas revisada por auditor humano;
- estabilidad frente a los outputs 10B.

Si se usa Ollama en 10E, debe documentarse el modelo, temperatura, URL local, numero exacto de casos regenerados y ausencia de APIs remotas.

## Artefactos 10D

- `src/llm/explain_top3_nandina_prompt_v0.3.md`
- `docs/rubrica_auditabilidad_llm_top3_v0.1.md`
- `docs/mejora_ficha_auditable_llm_top3_v0.1.md`
- `src/experiments/render_llm_explanation_audit_cards.py`
- `README.md`
- `docs/manifiesto_artefactos_v0.1.md`
- `docs/manifest_artifacts_v0.1.json`
