# PROMPT119 — CORREGIR PLAN G7-F02 ANTES DE AUTORIZAR V03

## 0. Rol y propósito

Actúa como **IA de Redacción Científica** del proyecto `elVladdi/gci-nandina-rag`.

Esta ejecución sigue siendo **SOLO DE PLANIFICACIÓN**. No debes modificar ningún DOCX, no debes generar V03 y no debes reutilizar V01/V02 como base de redacción.

La IA Experimental auditó externamente la respuesta de Prompt118 y determinó que el enfoque baseline-first es correcto, pero el plan todavía contiene defectos editoriales que deben corregirse antes de autorizar cualquier nueva edición del Word.

Estado vinculante:

```text
G7_F02 = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
V01 = REJECTED_BY_AUTHOR / DO_NOT_USE_AS_DRAFT_SOURCE
V02 = REJECTED_BY_AUTHOR / DO_NOT_USE_AS_DRAFT_SOURCE
V03 = NOT_AUTHORIZED / NOT_CREATED
G7_F03_AUTHORIZED = false
GROUP7_CLOSED = false
PROMPT118_EXTERNAL_AUDIT = REVISION_REQUIRED
```

La base sigue siendo exclusivamente:

```text
Molleapasa_gv_vigente_2026-09-22.docx
SHA256 = 08b48ec1687ae0a0d943724bf2d682aca02d2a9f5a124b3dc35270e041bc3aed
SIZE_BYTES = 4360620
```

---

## 1. Correcciones obligatorias detectadas por auditoría externa

### C1 — Referencia interna incorrecta a Tabla 3 no detectada en Prompt118

El baseline contiene un defecto preexistente adicional que Prompt118 no registró:

```text
3.2.4 Organización del diseño experimental
"La Tabla 4 resume las operaciones ejecutadas en cada fase."
```

pero el objeto inmediatamente siguiente es:

```text
Tabla 3
Correspondencia entre las fases RAG y las operaciones ejecutadas en el piloto
```

Por tanto, el plan debe registrar explícitamente este defecto y proponer una corrección mínima:

```text
"La Tabla 4 resume..." -> "La Tabla 3 resume..."
```

sin renumerar la Tabla 3.

Además, realiza una auditoría completa de referencias cruzadas de **todas las Tablas 1–24** y **Figuras 1–12** del baseline. No basta con revisar la Lista de Tablas/Lista de Figuras: comprueba también cada mención `Tabla N` y `Figura N` en la prosa contra el objeto al que realmente remite.

La respuesta corregida debe incluir una sección:

```text
CROSS_REFERENCE_AUDIT
```

con:

```text
TABLE_CROSS_REFERENCE_ANOMALIES = <conteo y detalle>
FIGURE_CROSS_REFERENCE_ANOMALIES = <conteo y detalle>
TABLE_CROSS_REFERENCE_AUDIT = PASS | REVISION_REQUIRED
FIGURE_CROSS_REFERENCE_AUDIT = PASS | REVISION_REQUIRED
```

No declares PASS si queda una referencia no reconciliada.

### C2 — Comentarios solo donde exista un cambio real

Prompt118 marcó `requires_comment = YES` incluso en varias filas `KEEP` donde no se propone modificar nada.

Eso produciría ruido de revisión y contradice el objetivo de facilitar la inspección del autor.

Regla corregida:

```text
IF proposed_action == KEEP AND minimal_edit_scope == NONE:
    requires_comment = NO
```

Solo debe existir comentario Word cuando haya una modificación visible, una supresión propuesta, una sustitución de figura, una corrección de referencia cruzada o un cambio terminológico real.

Las verificaciones sin cambio pueden quedar registradas en la matriz de trazabilidad, pero **no deben generar comentarios en el Word**.

Revisa toda la MATRIZ A y corrige `requires_comment` conforme a esta regla.

### C3 — Prohibido afirmar "reproducibilidad completa"

En A025, Prompt118 dice simultáneamente que debe evitarse una promesa de reproducibilidad perfecta, pero en `comment_detail_summary` propone:

```text
"Explicar reproducibilidad completa con limitaciones declaradas..."
```

Esa formulación es inconsistente y demasiado fuerte.

Sustituye cualquier expresión de ese tipo por una formulación científicamente limitada, por ejemplo:

```text
"describir el grado/estado de reproducibilidad alcanzado según la auditoría experimental, junto con sus limitaciones documentadas"
```

No uses `reproducibilidad completa`, `reproducibilidad total` ni equivalentes salvo que una fuente primaria congelada lo establezca literalmente, lo cual no debe asumirse.

HE1 continúa sin disposición formal terminal y la evidencia de reproducibilidad no puede convertirse retrospectivamente en una decisión de HE1.

### C4 — La V03 de revisión debe conservar la numeración original de Figuras 1–12

Prompt118 propone retirar Figuras 7–10 y renumerar las actuales Figuras 11–12 a 7–8. Esa renumeración puede ser adecuada **solo para una versión limpia posterior a la aceptación del autor**, pero no para la copia V03 de revisión.

En V03 el autor debe poder comparar el baseline sin confusión. Por tanto:

```text
REVIEW_V03_FIGURE_NUMBERING = PRESERVE_BASELINE_1_TO_12
```

Reglas:

- Figuras 7–10 permanecen físicamente visibles en V03 si se propone su supresión;
- su caption/objeto se marca como `supresión propuesta` mediante el esquema amarillo + tachado correspondiente;
- Figuras 11 y 12 continúan numeradas como 11 y 12 en V03;
- la Lista de Figuras de V03 conserva 1–12 durante la revisión;
- NO se ejecuta 11→7 ni 12→8 en V03;
- solo después de aceptación explícita del autor de las supresiones, una versión limpia posterior podrá renumerar 11→7 y 12→8 y actualizar todas las referencias cruzadas.

Corrige MATRIZ C y A071 para reflejar esta separación entre:

```text
REVIEW_V03_NUMBER
POST_AUTHOR_ACCEPTANCE_CLEAN_NUMBER
```

Puedes añadir esas dos columnas a MATRIZ C si resulta más claro.

### C5 — Hacer explícita la decisión prosa vs tabla para los bloques nuevos/complejos

Prompt118 declara que no se justifica una tabla nueva, pero debe demostrar mejor esa decisión porque el autor observó que en V01/V02 varios bloques narrativos podían organizarse como tablas.

Añade una sección:

```text
PRESENTATION_MODE_AUDIT
```

Para cada bloque nuevo o materialmente actualizado de información comparativa/multidimensional —como mínimo HE2, HE4, HE5, EXP11A, EXP11B, EXP12 y reproducibilidad— registra:

```text
topic
information_shape
candidate_existing_table
final_presentation_mode
reason
redundancy_control
```

Regla:

- si la información compara múltiples configuraciones, métricas, condiciones o estados, prioriza una tabla existente adecuada;
- si ya existe una tabla que puede absorber el contenido, actualízala en vez de crear un párrafo largo o una tabla nueva;
- usa prosa para síntesis, interpretación y límites, sin repetir todas las cifras de la tabla;
- `NEW_TABLE_JUSTIFIED` solo si ninguna tabla existente puede comunicar la información sin forzar su semántica.

---

## 2. Elementos de Prompt118 que se mantienen

Conserva, salvo las correcciones anteriores:

- baseline original como contrato editorial;
- tablas corporales 1–24 como numeración base;
- corrección de Lista de Tablas: incorporar Tabla 3 faltante y retirar entrada fantasma Tabla 25, sujeto a la auditoría completa de referencias;
- edición mínima por fragmento/celda/fila;
- prohibición de lenguaje interno de gobernanza en la tesis;
- comentarios de cambio íntegramente en español y con seis apartados;
- ciencia congelada y jerarquía de fuentes;
- ausencia de nueva ciencia/inferencia/referencias;
- HG y HE1 sin disposición formal inventada;
- EXP12 cerrado sin recuperación y efecto no estimable;
- G7-F03 no autorizado.

---

## 3. Convención futura de revisión — sin cambios

La futura V03, todavía no autorizada, deberá usar:

```text
TEXTO_ANTERIOR_MODIFICADO = AMARILLO + TACHADO + VISIBLE
TEXTO_NUEVO = AMARILLO + NO_TACHADO + VISIBLE
TEXTO_SIN_CAMBIO = NORMAL
```

La unidad de marcado debe ser la mínima posible.

En tablas:

- palabra/cifra/frase cambiada -> solo ese fragmento;
- celda cambiada -> solo esa celda;
- fila cambiada -> solo celdas afectadas;
- tabla completa -> nunca tachada si la estructura sigue siendo válida.

---

## 4. Comentarios futuros — plantilla vinculante

Solo para cambios reales:

```text
Cambio exacto:
Motivo del cambio:
Evidencia concreta:
Fuente gobernante:
Efecto en la tesis:
Límite de interpretación:
```

Todo en español natural. La fuente técnica puede aparecer al final del comentario para trazabilidad, pero los identificadores internos de gobernanza no deben aparecer en la prosa visible de la tesis.

---

## 5. Entregable de esta ejecución

Corrige la respuesta de planificación y publícala como:

```text
writing_prompts_tmp/119_RESPUESTA_CORREGIR_PLAN_G7_F02_ANTES_DE_V03.md
```

Debe incluir:

1. MATRIZ A corregida;
2. MATRIZ B corregida;
3. MATRIZ C corregida, distinguiendo numeración de revisión y eventual numeración limpia post-aceptación;
4. MATRIZ D vigente;
5. `CROSS_REFERENCE_AUDIT` completo;
6. `PRESENTATION_MODE_AUDIT` completo;
7. auditoría final de coherencia.

No edites el Word.

---

## 6. Estado terminal esperado

```text
PROMPT119_EXECUTION = COMPLETE
PROMPT118_EXTERNAL_AUDIT = REVISION_REQUIRED
AUTHOR_REJECTION_OF_V01_V02 = ACKNOWLEDGED
REWRITE_BASE = ORIGINAL_BASELINE_ONLY
WORD_MODIFIED = false
V03_CREATED = false
TABLE_CROSS_REFERENCE_AUDIT = PASS
FIGURE_CROSS_REFERENCE_AUDIT = PASS
COMMENT_POLICY_CORRECTED = true
REPRODUCIBILITY_WORDING_CORRECTED = true
REVIEW_V03_FIGURE_NUMBERING = PRESERVE_BASELINE_1_TO_12
PRESENTATION_MODE_AUDIT = PASS
PLAN_READY_FOR_EXTERNAL_AUDIT = true
G7_F02 = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
G7_F03_AUTHORIZED = false
EXTERNAL_AUDIT = PENDING_BY_IA_EXPERIMENTAL
```

Detente ahí. **No generes V03** hasta que la IA Experimental audite y apruebe este plan corregido.
