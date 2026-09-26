# Prompt correctivo — Experimental Design B03 / completitud DOCX V01

## Rol

Actúa como **IA de Redacción** del artículo científico principal destinado a *Knowledge-Based Systems*. Ejecuta exclusivamente el microgate técnico de completitud DOCX de `EXPERIMENTAL_DESIGN_B03`.

Este prompt **no autoriza reescritura científica**. Section 4.4 V01 ya superó la auditoría científica de la IA Gestora. Tu única función es producir y auditar el candidato Word acumulativo faltante y actualizar la respuesta de ejecución con su trazabilidad.

## Fuentes gobernantes obligatorias

Trabaja en `elVladdi/gci-nandina-rag`, rama `article/main-manuscript`.

Lee íntegramente antes de actuar:

1. `article/governance/D021_DOCX_LOCAL_CUSTODY_AND_DEFERRED_REPOSITORY_UPLOAD.md`;
2. `article/governance/D055_EXPERIMENTAL_DESIGN_B02_INTEGRATION_AND_V011_PROMOTION.md`;
3. `article/governance/D056_EXPERIMENTAL_DESIGN_B03_SECTION4_4_START.md`;
4. `article/prompts/5_EXPERIMENTAL_DESIGN_B03_SECTION4_4.md`;
5. `article/reviews/5_EXPERIMENTAL_DESIGN_B03_SECTION4_4_INTERNAL_REVIEW_V01.md`;
6. `article/sections/experimental_design/Experimental_Design_B03_V01.md`;
7. `article/responses/5_EXPERIMENTAL_DESIGN_B03_SECTION4_4_RESPONSE_V01.md`.

## Identidades congeladas

Baseline Word obligatorio, bajo custodia local del autor:

`ARTICLE_MASTER_CANDIDATE_EXPDES_B02_V02.docx`

SHA-256 obligatorio:

`d805088bdfafd9beffcaff27bd7d43e95f9e2f932e3d345ababf4579ed47dfdf`

Master Markdown B03 exacto ya auditado:

`ARTICLE_MASTER_CANDIDATE_EXPDES_B03_V01.md`

SHA-256:

`d4b0e1941791e901e20c476b99206a92ef78ea18cb2c614d9721963bb8b9ae78`

Git blob esperado para esos bytes Markdown:

`dfea73f5f462fc65cf98347f796deadc6da58455`

## Precondición binaria obligatoria

Antes de editar Word, calcula SHA-256 del DOCX baseline recibido. Debe ser exactamente:

`d805088bdfafd9beffcaff27bd7d43e95f9e2f932e3d345ababf4579ed47dfdf`

Si no tienes acceso al binario exacto o el hash no coincide, **detente sin reconstruir nada** y responde `BLOCKED_MISSING_EXACT_B02_V02_DOCX_BASELINE`.

Está prohibido reconstruir el Word desde Markdown, HTML, PDF, texto plano u otro DOCX anterior.

## Única modificación autorizada

Partiendo exclusivamente del DOCX B02 V02 exacto:

1. sustituye el placeholder de Part I — Section 4.4 por el texto inglés **exactamente equivalente** al contenido aprobado en `Experimental_Design_B03_V01.md`;
2. sustituye el placeholder de Part II — Section 4.4 por el espejo español aprobado;
3. no modifiques ninguna otra sección, párrafo, tabla, caption, referencia, nota, comentario o metadato editorial salvo los cambios técnicos estrictamente necesarios para insertar 4.4;
4. preserva los comentarios Word heredados y sus anclajes;
5. preserva estilos, numeración, saltos, estructura y formato acumulativo;
6. `tracked changes` debe quedar en cero;
7. no aceptes una regeneración completa del DOCX como equivalente a edición acumulativa.

Nombre del candidato:

`ARTICLE_MASTER_CANDIDATE_EXPDES_B03_V01.docx`

El DOCX permanece bajo custodia local del autor conforme a D-021. **No intentes subir el binario a GitHub**.

## QA obligatorio

Antes de entregar, verifica y reporta:

- SHA-256 del baseline B02 V02 = PASS;
- SHA-256 del nuevo candidato B03;
- apertura ZIP/OOXML = PASS;
- `word/document.xml` legible = PASS;
- comentarios heredados preservados: conteo y anclajes = PASS;
- comentarios nuevos no autorizados = 0;
- tracked changes = 0;
- equivalencia semántica MD/DOCX para 4.4 = PASS;
- Sections 1–4.3 sin cambios de contenido = PASS;
- Sections 4.5+ sin cambios de contenido = PASS;
- únicamente los dos placeholders 4.4 sustituidos por la prosa aprobada = PASS;
- render completo del DOCX sin corrupción, truncamiento, desbordes graves ni pérdida de contenido = PASS.

Si cualquiera de estos controles falla, no declares PASS.

## Entregables

1. Entrega al autor como adjunto descargable:
   `ARTICLE_MASTER_CANDIDATE_EXPDES_B03_V01.docx`.

2. Crea en GitHub:
   `article/responses/5_EXPERIMENTAL_DESIGN_B03_DOCX_COMPLETION_RESPONSE_V01.md`

La respuesta versionada debe registrar, en español e inglés con equivalencia semántica:

- hash del baseline recibido y verificación;
- hash del candidato DOCX generado;
- conteo de comentarios heredados;
- tracked changes;
- resultado OOXML;
- resultado del control diferencial;
- resultado del render;
- confirmación de que no se reescribió 4.4 ni se modificó 4.5+;
- ruta y SHA del review de Gestora que origina este microgate.

No modifiques `Experimental_Design_B03_V01.md` ni el contenido científico del master Markdown B03. No generes V02 de 4.4. No abras B04.

## Gate de salida

Detente tras producir el DOCX candidato y la respuesta versionada.

```text
SCIENTIFIC_CONTENT = PRESERVED / NO_REWRITE
DOCX_COMPLETION = EXECUTED_PENDING_GESTORA_AUDIT
AUTHOR_APPROVAL_GATE = NOT_OPEN
B04 = NOT_AUTHORIZED
```

La entrega vuelve a la **IA Gestora** para auditoría independiente del DOCX y, solo si supera ese control, apertura del gate de aprobación autoral de B03.

Responde únicamente en español en el chat.