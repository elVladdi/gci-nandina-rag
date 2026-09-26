# PROMPT118 — PLANIFICAR REEJECUCIÓN DE G7-F02 DESDE EL BASELINE ORIGINAL

## 0. Rol y propósito

Actúa como **IA de Redacción Científica** del proyecto `elVladdi/gci-nandina-rag`.

Esta ejecución es **SOLO DE PLANIFICACIÓN EDITORIAL Y CIENTÍFICA**. No debes modificar ningún DOCX, no debes generar un nuevo candidato Word y no debes reutilizar V01/V02 como base de redacción.

La revisión del autor rechazó los candidatos producidos por Prompt116/Prompt117. Por tanto:

```text
G7_F02 = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
V01 = REJECTED_BY_AUTHOR / DO_NOT_USE_AS_DRAFT_SOURCE
V02 = REJECTED_BY_AUTHOR / DO_NOT_USE_AS_DRAFT_SOURCE
G7_F03_AUTHORIZED = false
GROUP7_CLOSED = false
```

La nueva ejecución futura deberá rehacerse **desde la tesis baseline autoritativa**, no parchear V01 ni V02.

---

## 1. Baseline obligatorio

Trabaja conceptualmente desde el Word original cuya identidad está congelada como:

```text
Molleapasa_gv_vigente_2026-09-22.docx
SHA256 = 08b48ec1687ae0a0d943724bf2d682aca02d2a9f5a124b3dc35270e041bc3aed
SIZE_BYTES = 4360620
ROLE = CURRENT_WORKING_MASTER / AUTHOR_CONFIRMED / THESIS_CORRECTION_BASELINE
```

El baseline gobierna:

- estructura editorial;
- formato de párrafos;
- jerarquía de títulos;
- estilos Word;
- formato de tablas;
- formato de captions;
- numeración y referencias cruzadas existentes;
- tono y forma de exposición de la tesis.

No lo uses como verdad científica cuando contradiga las fuentes científicas aprobadas posteriores.

---

## 2. Fuentes científicas y de formulación

Mantén la jerarquía aprobada de G7-F01:

1. proyecto de tesis aprobado para problema, objetivos, hipótesis y alcance aprobados;
2. artefactos experimentales congelados para método y resultados;
3. source freeze `docs/writing/group7/g7_writing_source_freeze_v0.1.md/json`;
4. tablas y figuras canónicas ya aprobadas como fuentes de datos, NO como instrucciones para rediseñar la tesis;
5. baseline Word como contrato editorial y de formato;
6. v13 únicamente como fuente auxiliar metodológica cuando corresponda.

No hagas búsqueda web. No generes nueva inferencia, métricas, p-values, intervalos, resultados ni referencias.

---

## 3. Causa formal del rechazo de V01/V02

La nueva planificación debe corregir expresamente los siguientes defectos observados por el autor y confirmados en revisión:

### D1 — Formato y estilo de tesis no preservados

La edición anterior alteró de forma excesiva la forma en que venía redactándose y presentándose la tesis.

Regla futura:

```text
BASELINE_FORMAT_AND_WRITING_STYLE = BINDING
REDESIGN = PROHIBITED
```

La nueva versión debe parecer una **corrección del Word original**, no un documento reconstruido a partir de artefactos del repositorio.

### D2 — Numeración de tablas inconsistente

Se observaron duplicidades y residuos de numeración durante la sustitución de contenido.

Regla futura:

- una tabla = un único número y caption;
- no puede quedar una secuencia como `Tabla 2` seguida de `Tabla 4` perteneciente al mismo objeto;
- no puede quedar un número legacy delante de una tabla nueva;
- toda referencia en prosa debe apuntar al número final correcto;
- la Lista de tablas debe corresponder exactamente con las tablas del cuerpo;
- antes de editar, debe construirse un mapa completo de numeración actual y propuesta;
- el objetivo por defecto es **preservar la numeración original siempre que sea semánticamente posible**;
- una renumeración solo se admite cuando sea inevitable y debe propagarse a todas las referencias cruzadas afectadas.

### D3 — Filtración de gobernanza interna a la tesis

Está prohibido que la prosa visible de la tesis mencione estructuras internas de gobernanza o producción documental tales como:

```text
G1, G2, G3, G4, G5, G6, G7, G8
G3-Fxx, G4-Fxx, etc.
Group1, Group2, Group3...
source freeze
Prompt116, Prompt117, Prompt118
claim registry
G3C-005 u otros identificadores internos equivalentes
branch, commit, blob, gate, ficha, grupo
```

Esos identificadores sirven para trazabilidad del proceso, **no forman parte del experimento que debe leer el tesista/jurado**.

En la tesis se debe escribir el contenido científico correspondiente, por ejemplo:

- `el análisis inferencial del experimento`;
- `el conjunto de evaluación`;
- `la comparación primaria`;
- `el análisis de sensibilidad`;
- `los resultados experimentales`;
- `la tabla de resultados`;

según corresponda, sin revelar la gobernanza interna de producción del manuscrito.

Los identificadores técnicos del experimento solo pueden aparecer si son realmente necesarios para reproducibilidad y están definidos como parte del protocolo experimental, nunca porque existan en el flujo de gestión del proyecto.

### D4 — Elección deficiente entre prosa y tablas

No conviertas automáticamente todo resultado del repositorio en párrafos ni todo bloque nuevo en tabla.

Para cada modificación debes decidir explícitamente:

```text
PRESENTATION_MODE = PARAGRAPH | EXISTING_TABLE_CELL_UPDATE | EXISTING_TABLE_ROW_UPDATE | NEW_TABLE | FIGURE | NOTE
```

Usa tabla cuando la información sea comparativa, matricial, de múltiples configuraciones/métricas o resulte más clara en filas/columnas. Usa prosa para interpretación, transición, delimitaciones y explicación narrativa.

Evita duplicar en párrafos extensos cifras que ya quedan organizadas inmediatamente después en una tabla, salvo que el párrafo sintetice el hallazgo principal sin repetir toda la tabla.

### D5 — Comentarios demasiado abstractos y parcialmente en inglés

Todo comentario nuevo de revisión debe estar íntegramente en español y ser suficientemente concreto para que el autor pueda evaluar el cambio sin consultar el repositorio.

Formato obligatorio futuro del comentario:

```text
Cambio exacto:
Motivo del cambio:
Evidencia concreta:
Fuente gobernante:
Efecto en la tesis:
Límite de interpretación:
```

Requisitos:

- `Cambio exacto`: qué frase, cifra, celda, fila o interpretación se sustituye;
- `Motivo del cambio`: cuál era el problema específico del texto anterior;
- `Evidencia concreta`: dato, resultado, población, contraste o limitación que obliga al cambio;
- `Fuente gobernante`: nombre comprensible de la fuente y, después, path/identificador técnico si se necesita trazabilidad;
- `Efecto en la tesis`: qué sección, interpretación o coherencia corrige;
- `Límite de interpretación`: qué NO puede concluirse del cambio.

Prohibidos comentarios vagos como:

```text
Legacy conclusion
Frozen evidence
Internal scope
Updated to current state
Corrected per source
```

o equivalentes abstractos.

### D6 — Tachado excesivo de tablas completas

La futura copia de revisión debe aplicar **edición mínima a nivel de fragmento/celda**, no reemplazo masivo por comodidad.

Reglas:

1. Si cambia una palabra, cifra o frase → tacha y resalta SOLO ese fragmento y coloca el nuevo inmediatamente después.
2. Si cambia una celda de tabla → conserva la tabla y marca SOLO el contenido de esa celda.
3. Si cambia una fila → conserva la tabla y marca SOLO las celdas afectadas de esa fila.
4. Si se añade una fila o columna → conserva la tabla original y resalta únicamente la adición.
5. Solo puede duplicarse/reemplazarse una tabla completa si su estructura lógica completa deja de ser válida y no es posible corregirla por celdas/filas. Esa excepción debe justificarse previamente en el plan.
6. Nunca tachar una tabla completa solo para volver a escribir esencialmente la misma tabla con unos pocos valores distintos.

---

## 4. Convención futura de revisión

La futura V03 deberá construirse **directamente desde el baseline** y aplicar el marcado a la mínima unidad de cambio:

```text
TEXTO_ANTERIOR_MODIFICADO = AMARILLO + TACHADO + VISIBLE
TEXTO_NUEVO = AMARILLO + NO_TACHADO + VISIBLE
TEXTO_SIN_CAMBIO = NORMAL
```

El amarillo NO debe inundar párrafos, tablas o páginas completas cuando solo cambian algunos elementos.

Las partes no afectadas del baseline deben permanecer byte/format-equivalentes en la medida técnicamente posible.

---

## 5. Estilo de redacción obligatorio

Antes de proponer cualquier texto nuevo, estudia el tono del baseline en cada sección correspondiente.

La nueva redacción debe:

- seguir la misma voz académica, longitud de párrafos y nivel de detalle de la tesis;
- integrarse orgánicamente con los párrafos anterior y posterior;
- evitar prosa telegráfica de reporte técnico;
- evitar nombres internos de procesos de auditoría/gobernanza;
- introducir cifras en narrativa solo cuando sean necesarias para sostener el argumento;
- no escribir como si la tesis fuera un reporte de ejecución del repositorio;
- diferenciar claramente método, resultado e interpretación;
- usar español académico natural y consistente con el documento existente.

No copiar literalmente resúmenes de JSON, CSV, registros de cierre o respuestas de prompts como prosa de tesis.

---

## 6. Mapas obligatorios ANTES de editar

En esta ejecución de Prompt118 debes producir únicamente un plan detallado con cuatro matrices.

### MATRIZ A — Mapa de intervención por sección

Una fila por cambio propuesto, con columnas:

```text
plan_id
baseline_section
baseline_locator
baseline_content_summary
scientific_issue
proposed_action
presentation_mode
minimal_edit_scope
scientific_source
human_readable_reason
internal_labels_to_translate_or_remove
requires_comment
comment_detail_summary
```

`proposed_action` solo puede ser:

```text
KEEP
TERMINOLOGY_ONLY
INLINE_REPLACE
PARAGRAPH_REWRITE_MINIMAL
TABLE_CELL_UPDATE
TABLE_ROW_UPDATE
TABLE_STRUCTURE_UPDATE
NEW_TABLE_JUSTIFIED
FIGURE_UPDATE
REMOVE_SUPERSEDED_WITH_INLINE_MARKUP
```

### MATRIZ B — Mapa maestro de tablas

Debes inspeccionar TODAS las tablas del baseline y registrar:

```text
baseline_table_number
baseline_caption
baseline_section
baseline_role
scientific_status
future_action
future_table_number
caption_action
cell_level_changes_expected
whole_table_replacement_required
whole_table_replacement_justification
cross_references_affected
list_of_tables_action
```

Reglas:

- detectar números faltantes, duplicados o captions inconsistentes ya existentes;
- distinguir defectos preexistentes del baseline de defectos introducidos en V01/V02;
- proponer una numeración final coherente y única;
- preservar la numeración baseline si no existe una razón real para cambiarla;
- ninguna tabla nueva puede insertarse sin indicar su ubicación y efecto sobre numeración posterior.

### MATRIZ C — Mapa maestro de figuras

Columnas:

```text
baseline_figure_number
baseline_caption
baseline_section
scientific_status
future_action
future_figure_number
caption_action
replacement_required
cross_references_affected
list_of_figures_action
```

No reemplazar una figura simplemente porque existe una versión canónica en el repositorio: justificar si realmente necesita actualización científica.

### MATRIZ D — Diccionario de traducción de lenguaje interno a lenguaje de tesis

Columnas:

```text
internal_term
must_not_appear_in_thesis
approved_manuscript_expression
context_of_use
```

Debe incluir, como mínimo, todas las menciones de G1–G8, fichas, prompts, source freeze, claim IDs y cualquier otro identificador de gobernanza que pudiera filtrarse a la prosa.

---

## 7. Auditoría de coherencia del plan

Antes de entregar, comprueba expresamente:

1. ¿El plan parte del baseline original y no de V01/V02?
2. ¿Se conserva la organización editorial de la tesis salvo cambio imprescindible?
3. ¿Cada tabla tiene un único número final propuesto?
4. ¿No existen duplicados ni numeración residual?
5. ¿Cada cambio de tabla se intenta primero a nivel de celda/fila?
6. ¿Los nombres G3–G6 y demás gobernanza interna desaparecen de la prosa propuesta?
7. ¿Los comentarios previstos están completamente en español y contienen evidencia concreta?
8. ¿Se identificó dónde una tabla comunica mejor que un párrafo y viceversa?
9. ¿No se crea ciencia nueva?
10. ¿Se conservan las formulaciones aprobadas de problema, objetivos e hipótesis?
11. ¿HG y HE1 siguen sin disposición formal inventada?
12. ¿EXP12 permanece cerrado y no estimable?
13. ¿No se autoriza G7-F03?

Si alguna respuesta es NO, corrige el plan antes de entregar.

---

## 8. Prohibiciones de esta ejecución

No:

- modificar la tesis baseline;
- modificar V01 o V02;
- generar V03 todavía;
- generar una nueva matriz de trazabilidad definitiva todavía;
- incorporar contenido de V01/V02 por copia/pegado;
- modificar GitHub fuera de la publicación de esta respuesta;
- cerrar G7-F02;
- autorizar G7-F03;
- recalcular resultados;
- introducir nuevas fuentes;
- cambiar la ciencia congelada.

---

## 9. Respuesta oficial

Publica exclusivamente:

```text
writing_prompts_tmp/118_RESPUESTA_PLAN_REHACER_G7_F02_DESDE_BASELINE.md
```

en la rama:

```text
codex/prompts-temporary
```

La respuesta debe incluir las cuatro matrices completas, no solo resúmenes.

Estado terminal esperado:

```text
PROMPT118_EXECUTION = COMPLETE
AUTHOR_REJECTION_OF_V01_V02 = ACKNOWLEDGED
REWRITE_BASE = ORIGINAL_BASELINE_ONLY
WORD_MODIFIED = false
V03_CREATED = false
PLAN_READY_FOR_EXTERNAL_AUDIT = true
G7_F02 = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
G7_F03_AUTHORIZED = false
EXTERNAL_AUDIT = PENDING_BY_IA_EXPERIMENTAL
```

Detente ahí. La ejecución del nuevo Word será autorizada únicamente después de la auditoría externa del plan por la IA Experimental.