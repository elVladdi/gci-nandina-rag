# D-035 — Timeout-safe artifact handoff for large editorial artifacts

## Estado

`ACTIVE / BINDING`

## Motivo

El flujo editorial ya había identificado que la transferencia directa de artefactos textuales acumulativos grandes mediante el conector puede provocar timeouts. D-023 estableció que, ante un fallo de una llamada UTF-8 por límite o error del conector, la ejecución debe detenerse inmediatamente y no recurrir a Base64 manual, fragmentación, recomposición, placeholders, commits auxiliares ni reintentos exploratorios. D-032 demostró además un mecanismo de recuperación estable: entregar al autor los archivos exactos como adjuntos descargables, verificar sus SHA-256 y permitir que la IA Gestora complete posteriormente la materialización en GitHub.

La ejecución del prompt `4_ARCHITECTURE_B01_CORRECT_PLACEHOLDER_AND_COMPLETE_DELIVERY.md@6000972317488b5a0bb90a0ddc5fddb00a8e1731` volvió a exponer al proceso al mismo riesgo al exigir transferir nuevamente el master Markdown acumulativo completo mediante el conector textual. Este procedimiento queda sustituido para el caso actual y para futuras ejecuciones que invoquen expresamente D-035.

## Regla

Cuando un artefacto textual grande ya haya producido un timeout o exista antecedente inmediato de bloqueo por tamaño/transferencia en el mismo bloque:

1. **No se vuelve a intentar la transferencia directa del artefacto grande mediante el conector de la IA de Redacción.**
2. **No se usa Base64 manual, fragmentación, chunking, reensamblado, archivos auxiliares, ramas temporales ni múltiples commits como workaround.**
3. La IA de Redacción conserva/genera el archivo exacto local, calcula SHA-256 y lo entrega al autor como **archivo adjunto descargable**, sin pegar su contenido en chat.
4. La respuesta operacional pequeña sí debe versionarse en GitHub conforme a D-022, registrando los nombres y hashes de los artefactos entregados y que la materialización GitHub queda diferida a la IA Gestora.
5. La IA Gestora verifica los archivos recibidos y decide/materializa la integración posterior. La mera entrega al autor no equivale a `INTEGRATED` ni a promoción del master.
6. Si el artefacto adjunto no puede entregarse, la IA ejecutora se detiene; no intenta otra vía de serialización.
7. La codificación interna usada por una API o conector no se considera Base64 manual. La prohibición se refiere a usar Base64 como artefacto, workaround o mecanismo de fragmentación gestionado por la IA.

## Aplicación inmediata — Architecture B01

Para el cierre correctivo de Architecture B01, la IA de Redacción debe entregar al autor como adjuntos exactos:

- `Architecture_B01_V01.md`;
- `ARTICLE_MASTER_CANDIDATE_ARCH_B01_V02.md`;
- `ARTICLE_MASTER_CANDIDATE_ARCH_B01_V02.docx`.

Solo la respuesta operacional pequeña se versionará directamente en GitHub. La IA Gestora materializará posteriormente los Markdown después de verificar su identidad.

El prompt `4_ARCHITECTURE_B01_CORRECT_PLACEHOLDER_AND_COMPLETE_DELIVERY.md@6000972317488b5a0bb90a0ddc5fddb00a8e1731` queda **SUPERSEDED FOR EXECUTION** por el prompt timeout-safe que invoque D-035.

## Estados que D-035 no concede

D-035 no aprueba ni congela Architecture B01, no promueve `ARTICLE_MASTER_V008`, no abre Architecture B02 ni Experimental design, y no modifica `FINAL_GAP` ni `NOVELTY`.
