# Rubrica de auditabilidad LLM Top-3 v0.1

## Objetivo

Esta rubrica evalua fichas auditables generadas por un LLM que explica un Top-3 NANDINA fijo ya recuperado. No mide recuperacion, no valida clasificacion juridica y no autoriza al LLM a buscar, clasificar desde cero ni reordenar candidatos.

La unidad evaluada es una ficha por caso. La recuperacion base operativa es historica real `data_aduanas` clase 87, con respaldo normativo. Por eso la rubrica distingue el soporte historico, que puede ser fuerte por precedente, del soporte normativo, que puede ser solo trazable o generico.

## Escala

Cada dimension se califica en escala 0-2:

| Puntaje | Criterio general |
| ---: | --- |
| 2 | Cumple de forma clara, verificable y util para auditoria humana. |
| 1 | Cumple parcialmente, pero deja ambiguedades, omisiones o lenguaje mejorable. |
| 0 | No cumple, impide auditar o induce una lectura no sustentada. |

La ficha puede considerarse auditable si no viola restricciones duras y alcanza al menos 12/16 puntos. Una ficha con violacion dura no debe aprobarse aunque tenga puntaje alto.

## Restricciones duras

Estas condiciones son obligatorias:

- El Top-3 se preserva exactamente en orden, sin agregar ni eliminar candidatos.
- No aparecen codigos NANDINA fuera del `top3_original`.
- No se afirma clasificacion oficial.
- No se usan frases categoricas como "corresponde definitivamente", "codigo correcto" o "debe clasificarse".
- La conclusion queda formulada como apoyo documental para revision experta.
- La salida LLM es JSON estricto cuando se evalua el artefacto tecnico.

## Dimensiones

| Dimension | 2 puntos | 1 punto | 0 puntos |
| --- | --- | --- | --- |
| Trazabilidad | Conserva `case_id`, `id_unico`, rank, NANDINA, `candidate_id_unico` y `evidence_id` por candidato. | Conserva ids principales, pero falta algun identificador o la cita no es facil de rastrear. | Omite ids criticos o mezcla evidencia entre candidatos. |
| Verificabilidad | Cada afirmacion relevante puede contrastarse con descripcion, evidencia historica o evidencia normativa citada. | Hay afirmaciones mayormente verificables, pero algunas no tienen soporte claro. | Introduce atributos, funciones o inferencias no presentes en el payload. |
| Separacion historico/normativo | Explica por separado que aporta la evidencia historica y que aporta la normativa. | Cita ambas fuentes, pero las mezcla en la justificacion. | Presenta la evidencia historica como si fuera validacion normativa, o ignora una fuente. |
| Prudencia de la conclusion | Usa lenguaje como "compatible", "sugiere" y "requiere revision experta"; calibra la conclusion al nivel de soporte. | Evita clasificacion oficial, pero suena mas decisiva que el soporte declarado. | Afirma certeza, codigo correcto o correspondencia definitiva. |
| Consistencia con Top-3 fijo | Explica los tres candidatos en el orden recibido y declara que no reordena. | Mantiene el orden, pero la comparacion sugiere ranking alternativo de forma ambigua. | Reordena, recomienda fuera del Top-3 o elimina candidatos. |
| Deteccion de evidencia normativa generica | Marca como generica/residual evidencia tipo "Los demas", "Partes" o formulas similares; no la trata como soporte sustantivo. | Detecta algunas genericidades, pero omite otras o las comunica con poca visibilidad. | Usa norma residual como evidencia fuerte sin advertencia. |
| Comparacion entre candidatos | Compara criterios observables y normativos relevantes: producto, funcion, atributos tecnicos, alcance normativo y similitud historica. | Compara candidatos, pero omite algun criterio decisivo o solo explica diferencias obvias. | No compara el Top-3 o solo repite descripciones. |
| Utilidad para auditoria humana | Permite decidir donde revisar: candidato mas compatible, dudas, evidencia debil y necesidad de escalamiento experto. | Ayuda a rastrear evidencia, pero no orienta bien la revision siguiente. | No reduce el trabajo auditor o puede inducir una decision no sustentada. |

## Indicadores de alerta

La ficha debe activar `requiere_revision_experta` o una advertencia equivalente cuando:

- Todos los candidatos tienen soporte medio o bajo.
- El mayor soporte proviene casi solo de evidencia historica.
- La evidencia normativa del candidato principal es residual o generica.
- Hay atributos faltantes para distinguir subpartidas cercanas.
- El Top-3 parece insuficiente para explicar la mercancia observada.
- La conclusion no puede sostenerse sin revisar norma, notas legales o ficha tecnica.

## Uso recomendado

En Fase 10D la rubrica se usa como diseno de calidad, no como nueva metrica de recuperacion. En una eventual Fase 10E puede aplicarse a una corrida acotada o completa para medir si el prompt v0.3 aumenta prudencia, deteccion de normativa generica y utilidad de revision humana sin cambiar el ranking base.
