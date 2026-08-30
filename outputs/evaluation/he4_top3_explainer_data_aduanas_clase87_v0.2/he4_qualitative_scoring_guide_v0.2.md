# HE4 qualitative scoring guide v0.2

Fuente congelada: `docs/rubrica_auditabilidad_llm_top3_v0.1.md`.

Cada dimension se puntua 0, 1 o 2. Una ficha es auditable solo con total >=12/16 y sin hard violation.

| Dimension | 2 | 1 | 0 |
| --- | --- | --- | --- |
| Trazabilidad | Conserva `case_id`, `id_unico`, rank, NANDINA, `candidate_id_unico` y `evidence_id` por candidato. | Conserva ids principales, pero falta algun identificador o la cita no es facil de rastrear. | Omite ids criticos o mezcla evidencia entre candidatos. |
| Verificabilidad | Cada afirmacion relevante puede contrastarse con descripcion, evidencia historica o evidencia normativa citada. | Hay afirmaciones mayormente verificables, pero algunas no tienen soporte claro. | Introduce atributos, funciones o inferencias no presentes en el payload. |
| Separacion historico/normativo | Explica por separado que aporta la evidencia historica y que aporta la normativa. | Cita ambas fuentes, pero las mezcla en la justificacion. | Presenta la evidencia historica como si fuera validacion normativa, o ignora una fuente. |
| Prudencia de la conclusion | Usa lenguaje como compatible, sugiere y requiere revision experta; calibra la conclusion al nivel de soporte. | Evita clasificacion oficial, pero suena mas decisiva que el soporte declarado. | Afirma certeza, codigo correcto o correspondencia definitiva. |
| Consistencia con Top-3 fijo | Explica los tres candidatos en el orden recibido y declara que no reordena. | Mantiene el orden, pero la comparacion sugiere ranking alternativo de forma ambigua. | Reordena, recomienda fuera del Top-3 o elimina candidatos. |
| Deteccion de evidencia normativa generica | Marca como generica/residual evidencia tipo Los demas, Partes o formulas similares; no la trata como soporte sustantivo. | Detecta algunas genericidades, pero omite otras o las comunica con poca visibilidad. | Usa norma residual como evidencia fuerte sin advertencia. |
| Comparacion entre candidatos | Compara criterios observables y normativos relevantes: producto, funcion, atributos tecnicos, alcance normativo y similitud historica. | Compara candidatos, pero omite algun criterio decisivo o solo explica diferencias obvias. | No compara el Top-3 o solo repite descripciones. |
| Utilidad para auditoria humana | Permite decidir donde revisar: candidato mas compatible, dudas, evidencia debil y necesidad de escalamiento experto. | Ayuda a rastrear evidencia, pero no orienta bien la revision siguiente. | No reduce el trabajo auditor o puede inducir una decision no sustentada. |

## Hard constraints

- Top-3 exactamente preservado y ordenado.
- Sin codigos NANDINA fuera de `top3_original`.
- Sin clasificacion oficial ni lenguaje categorico de codigo definitivamente correcto.
- Conclusion como apoyo documental para revision experta.
- JSON estricto en el artefacto tecnico.

`advertencias_globales` esta excluido del scoring por el mismatch prompt-schema congelado.
