# D-027 — Entrega obligatoria del DOCX al autor antes de continuar el master

## Estado

AUTHOR_CORRECTION / ACTIVE / BINDING

## Motivo

Durante la reanudación de `INTRODUCTION_B01` se detectó una brecha operativa en la aplicación de D-021. La respuesta de ejecución de Related Work B06 registró que `ARTICLE_MASTER_CANDIDATE_RW_B06_V01.docx` fue generado localmente y fijó su SHA-256, pero el binario no fue entregado efectivamente al autor antes de promover B06 y abrir Introduction.

D-021 establecía `LOCAL / AUTHOR CUSTODY`, pero no definía de forma suficientemente explícita el acto de transferencia desde el entorno local de la IA de Redacción hacia la custodia real del autor. El almacenamiento temporal dentro de la sesión de una IA no constituye custodia del autor.

## Decisión

Con efecto inmediato:

1. Cuando un bloque genere un DOCX acumulativo y su carga a GitHub quede diferida, el binario exacto DEBE ser entregado al autor mediante un archivo descargable/adjunto en el chat de ejecución antes de que el bloque pueda considerarse técnicamente cerrado para el siguiente bloque dependiente del DOCX.
2. `LOCAL_AUTHOR_CUSTODY` solo puede declararse cuando el autor haya recibido efectivamente el binario o haya proporcionado él mismo una copia byte-for-byte idéntica.
3. El SHA-256 del archivo entregado debe coincidir exactamente con el SHA-256 registrado en la respuesta de ejecución.
4. Un archivo conservado únicamente en el filesystem temporal o sesión local de la IA NO cumple `LOCAL_AUTHOR_CUSTODY`.
5. D-022 mantiene el principio de respuesta sustantiva versionada en GitHub, pero D-027 introduce una excepción operativa mínima: cuando corresponda entregar el DOCX al autor, el chat puede contener el enlace/adjunto del archivo además del puntero GitHub mínimo.
6. No se debe pedir al autor que proporcione un DOCX que nunca le fue entregado. Primero debe intentarse recuperar el binario exacto desde la sesión que lo generó.
7. Si el binario exacto ya no está disponible, la IA de Redacción debe detenerse y registrar `DOCX_CUSTODY_RECOVERY_FAILED`; queda prohibido regenerar o reconstruir silenciosamente el DOCX desde Markdown.
8. Cualquier regeneración controlada de un DOCX perdido requiere una autorización posterior específica de la IA Gestora, con nueva identidad SHA-256 y trazabilidad explícita. No puede presentarse como el mismo binario original.

## Aplicación al caso B06

El binario reportado por la ejecución B06 es:

`ARTICLE_MASTER_CANDIDATE_RW_B06_V01.docx`

SHA-256 gobernante reportado:

`3a07568b8f6ac80ed2df39ee60c0aab65c06df5bb3e1988d3e4f8c752d84bf0`

Estado corregido de custodia:

```text
B06_DOCX_GENERATED = REPORTED / YES
B06_DOCX_SHA256 = 3a07568b8f6ac80ed2df39ee60c0aab65c06df5bb3e1988d3e4f8c752d84bf0
B06_DOCX_AUTHOR_HANDOFF = NOT_COMPLETED
B06_DOCX_AUTHOR_CUSTODY = NOT_ESTABLISHED
SCIENTIFIC_APPROVAL_B06 = UNAFFECTED
INTRODUCTION_B01 = AUTHORIZED / BLOCKED_PENDING_DOCX_RECOVERY
```

La prioridad inmediata es recuperar y entregar al autor el binario B06 exacto sin modificarlo. Solo después puede reanudarse Introduction B01.
