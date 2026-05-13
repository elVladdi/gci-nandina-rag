# Rúbrica preliminar de calidad de explicación auditable

La rúbrica permite evaluar la calidad de las explicaciones generadas por el componente LLM+RAG.

| Criterio | 0: insuficiente | 1: parcial | 2: adecuado |
|---|---|---|---|
| Verificabilidad | No cita evidencia o la evidencia no existe. | Cita evidencia, pero la relación es débil o incompleta. | Cita evidencia localizable y directamente revisable. |
| Trazabilidad | No identifica documento, versión o fragmento. | Identifica algunos elementos de procedencia. | Identifica documento, versión, fragmento y relación con la recomendación. |
| Pertinencia documental | La evidencia no corresponde al atributo relevante. | La evidencia es parcialmente pertinente. | La evidencia corresponde al atributo decisivo de clasificación. |
| Concordancia evidencia-justificación | La explicación introduce afirmaciones no sustentadas. | La explicación es mayormente consistente, con omisiones menores. | La explicación se limita a inferencias sustentadas por evidencia recuperada. |
| Claridad para auditoría | No permite reconstruir el criterio. | Permite reconstrucción parcial. | Permite revisar el criterio aplicado de forma clara y ordenada. |

## Uso previsto

La rúbrica se aplicará sobre una submuestra estratificada de salidas del piloto, procurando incluir casos correctos, incorrectos, ambiguos y casos con cercanía jerárquica entre candidatos.
