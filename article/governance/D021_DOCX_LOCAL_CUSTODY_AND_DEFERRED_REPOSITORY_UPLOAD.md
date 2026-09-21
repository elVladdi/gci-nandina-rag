# D-021 — Custodia local del DOCX y carga diferida al repositorio

## Estado

AUTHOR_APPROVED / ACTIVE / BINDING

## Motivo

Durante el cierre técnico de Related Work B05 V01 se confirmó que exigir la transferencia byte-for-byte del DOCX mediante `create_blob` + base64 introduce un cuello de botella operativo que puede provocar timeouts y no aporta valor científico proporcional en cada bloque de redacción.

El DOCX acumulativo sigue siendo necesario porque conserva comentarios de auditoría, anclajes y estructura editorial que no deben reconstruirse desde Markdown. Sin embargo, su presencia inmediata en GitHub no es necesaria para mantener trazabilidad, siempre que el binario aprobado quede bajo custodia local del autor y se identifique inequívocamente mediante SHA-256.

## Decisión

A partir de D-021, para los bloques de redacción del artículo:

1. El DOCX acumulativo aprobado queda bajo custodia local del autor.
2. El SHA-256 del DOCX es obligatorio y debe registrarse en el informe de ejecución, revisión interna y estado editorial correspondiente.
3. La carga del DOCX a GitHub queda diferida a hitos editoriales definidos por la IA Gestora o al cierre final del manuscrito.
4. Los commits semánticos ordinarios de bloques de redacción pueden contener únicamente los artefactos textuales autorizados (`.md`) y la trazabilidad correspondiente.
5. La ausencia temporal del DOCX en GitHub no constituye defecto de entrega si el autor conserva el binario exacto aprobado y su SHA-256 está fijado.
6. El siguiente bloque que requiera continuar sobre el Word acumulativo debe usar el binario local exacto aprobado; queda prohibido reconstruirlo desde Markdown.
7. La igualdad binaria entre una copia local posterior y el baseline aprobado se verifica mediante SHA-256 antes de continuar la edición.
8. Si en un hito posterior se decide subir el DOCX a GitHub, la identidad remota deberá verificarse contra el SHA-256 aprobado, pero esa carga no debe bloquear la redacción ordinaria.

## Aplicación inmediata a B05 V01

El DOCX aprobado de B05 V01 es:

`ARTICLE_MASTER_CANDIDATE_RW_B05_V01.docx`

SHA-256:

`042952002c2caeb86ec854b0bfcd7332724ddd4712589e25dfddb52718bf159a`

Estado:

- revisión interna: PASS;
- aprobación del autor: RECIBIDA;
- comentarios Word: 32;
- tracked changes: 0;
- render: 27/27 PASS;
- custodia: LOCAL / AUTHOR;
- carga GitHub: DEFERRED.

El cierre técnico de B05 debe versionar únicamente los tres artefactos Markdown exactos ya auditados. No debe intentar subir, regenerar, reguardar ni reconstruir el DOCX.

## Relación con reglas previas

D-021 modifica únicamente la exigencia operativa de carga inmediata del binario DOCX. No modifica:

- el principio de master acumulativo;
- la obligación de preservar comentarios Word;
- la obligación de trabajar desde el DOCX baseline exacto;
- la disciplina de aprobación por bloque;
- la prohibición de reconstruir el Word desde Markdown;
- la necesidad de SHA-256 para identidad del binario;
- las fronteras científicas o editoriales vigentes.

Cuando una instrucción previa exija que el DOCX sea necesariamente comprometido en GitHub en cada bloque, D-021 prevalece para los bloques posteriores a su aprobación, salvo instrucción explícita de la IA Gestora para un hito específico.
