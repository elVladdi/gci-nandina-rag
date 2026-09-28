# PROMPT121F-FIG6 — Integrar Figura 6 aprobada en REVIEW V03 / A043

## 0. Actor y autorización

Actúa como **IA de Redacción Científica** del proyecto `elVladdi/gci-nandina-rag`.

No eres CODEX. No eres la IA Experimental. No eres la IA Diseñadora y Auditora de Figuras Científicas. No regeneres figuras, no recalcules datos y no ejecutes 121G.

Esta ejecución está autorizada **exclusivamente para A043 / Figura 6** después del PASS externo de FIG015.

Lee íntegramente antes de editar:

```text
writing_prompts_tmp/121F_RESPUESTA_G7_F02_V03_BLOQUE_F_RESULTADOS_4_1_4_TABLAS.md
@ c3e73e72bcee360e4b5365bc55361d37140ee7c3

writing_prompts_tmp/121F_AUDITORIA_EXTERNA_PASS.md
@ 625709b627f62fbcb7090282552ef96e11726b85

figure_prompts_tmp/FIG012_RESPUESTA_AUDITAR_ADAPTACION_TESIS_FIGURA6_G7_F02.md
@ be0879c44b9d933bc0591bcf498b5e056cc31b20

figure_prompts_tmp/FIG014_RESPUESTA_RESOLVER_LEGIBILIDAD_H100_FIGURA6_G7_F02.md
@ e667642115f2fbd27e7052e8cfd43fa8af1a9d95

figure_prompts_tmp/FIG014_AUDITORIA_EXTERNA_PASS.md
@ a20f51496579446b86644022a64e2d68f1aab677

figure_prompts_tmp/FIG015_RESPUESTA_REGENERAR_FIGURA6_TESIS_TRAS_RESOLVER_H100_G7_F02.md
@ 78894c96cd59df36673def8647db88c96d50f953

figure_prompts_tmp/FIG015_AUDITORIA_EXTERNA_PASS.md
@ 4b916b6b2909fde6216654843aebdedcf2115cc3
```

Estado vinculante:

```text
PROMPT121F_EXTERNAL_AUDIT = PASS
FIG015_EXTERNAL_AUDIT = PASS
FIGURE_6_CANDIDATE_APPROVED_FOR_DOCX_INTEGRATION = true
A041 = VERIFIED / COMPLETE
A042 = VERIFIED / COMPLETE
A043 = NOT_EXECUTED
121G_AUTHORIZED = false
G7_F02 = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
G7_F03_AUTHORIZED = false
```

No ejecutes 121G ni ningún bloque posterior.

---

## 1. Entradas exactas

### 1.1 Word acumulativo autorizado

Trabaja exclusivamente sobre:

```text
Molleapasa_gv_G7F02_REVIEW_V03_F.docx
SHA256 = c630bcc51b33b79e2d0d9fdfc92f2701816dd29116e3051d54f28a713f71216b
SIZE = 4572575 bytes
```

### 1.2 Trazabilidad acumulativa autorizada

```text
g7_thesis_claim_traceability_v0.3_F.csv
SHA256 = 14d44b27012181bc943fa0325eb3c5964295ff040455ffe8c7c2b16f025eb337
SIZE = 93547 bytes
INHERITED_TRACE_ROWS = 103
```

Recalcula ambos SHA-256 antes de cualquier edición. Si alguno no coincide exactamente, `STOPPED_PRECONDITION`.

### 1.3 Figura 6 aprobada

Usa exclusivamente el PNG aprobado:

```text
PATH = figures/group7/g7_thesis_fig_06_sensitivity.png
SOURCE_COMMIT = 78894c96cd59df36673def8647db88c96d50f953
GIT_BLOB = 667765204adbdb7ab7567e9546f6ed8c71051d91
SHA256 = 4eeb3a63d4bb8a22c5b00f6d3efe4d2733c2caeec52373fa7e1c05ac27a24ae3
PIXELS = 3000 x 2000
DPI_NOMINAL = 300
```

Artefactos asociados, solo para verificación/trazabilidad:

```text
SVG = figures/group7/g7_thesis_fig_06_sensitivity.svg
SVG_GIT_BLOB = f6b4a1459b70daa5e2106dc6cd999a12668131a8
SVG_GIT_SHA256 = 780cbf167cb597ebd7e644638a5a3b5c648b47299dfdf8b66b357014a4549584

RENDERER = src/figures/group7/render_g7_thesis_fig_06_sensitivity.py
RENDERER_GIT_BLOB = b433fa5d45246ee22bae324835cdc9ff15c744cf
RENDERER_SHA256 = 76d93530e802629985a85619bac9932598b465674f66a8d1bd3ee37169142c0b
```

Si no puedes acceder exactamente al PNG aprobado o su hash no coincide, STOP. No lo regeneres ni lo sustituyas por una imagen similar.

---

## 2. Alcance único

Ejecuta exclusivamente **A043** en la zona actual de Figura 6, inmediatamente después de Tabla 15 y su interpretación, antes del inicio de 4.1.5.

No modifiques:

- la prosa ya aprobada de 4.1.4;
- Tabla 14;
- Tabla 15;
- sus valores o interpretaciones;
- Figuras 4 o 5;
- ninguna sección anterior;
- 4.1.5 ni ninguna sección posterior;
- Lista de Figuras;
- numeración oficial de figuras 1–12;
- ningún otro comentario o fila de trazabilidad heredada.

No introduzcas nueva inferencia ni recalcules métricas.

---

## 3. Convención REVIEW V03 obligatoria para Figura 6

La copia es de revisión. **No elimines la Figura 6 legacy.**

Debes aplicar exactamente esta secuencia:

1. conserva físicamente la imagen legacy actual de Figura 6;
2. conserva su número oficial `Figura 6` y su campo `SEQ Figura` existente;
3. marca el texto del caption legacy que queda superseded con **amarillo + tachado**, de forma visible;
4. no uses `w:del` ni borres el caption legacy;
5. añade exactamente **un comentario Word nuevo**, íntegramente en español, asociado al cambio;
6. inmediatamente después de la figura/caption legacy inserta esta línea temporal exacta, en estilo normal/no-caption, **amarillo y sin tachado**:

```text
PROPUESTA DE REEMPLAZO DEL ELEMENTO GRÁFICO ANTERIOR — NO ES NUMERACIÓN FINAL
```

7. inserta inmediatamente después el PNG aprobado `g7_thesis_fig_06_sensitivity.png`;
8. preserva su relación de aspecto original `3:2`; no deformes ni recortes la imagen;
9. debajo del PNG incorpora el caption final propuesto del apartado 4, **resaltado íntegramente en amarillo y sin tachado**;
10. el caption propuesto es texto de revisión: **no crees un segundo `SEQ Figura`** ni una nueva entrada automática en Lista de Figuras;
11. no insertes el SVG en el DOCX.

---

## 4. Caption final propuesto — Figura 6

Usa exactamente este texto visible, sin abreviar ni añadir lenguaje interno:

**Figura 6. Sensibilidad conjunta del banco histórico a tamaño y composición en el benchmark interno offline del Capítulo 87 (1 056 series, 67 DAM y 42 NANDINA).** Los seis paneles muestran Top-1, Top-3, Top-5, Top-10, Top-50 y MRR para 31 corridas observadas distribuidas en cinco condiciones: H25 (`n=10`), H50-D1 (`n=5`), H50-D2 (`n=5`), H75 (`n=10`) y H100 (`n=1`, referencia congelada). H25, H50, H75 y H100 corresponden a condiciones nominales de tamaño del banco histórico, mientras que D1 y D2 distinguen dos composiciones documentadas dentro de H50; las demás condiciones conservan asimismo sus composiciones observadas. Cada punto representa una corrida individual y H100 se muestra como una única referencia, no como una distribución de réplicas. El tamaño nominal y la composición del banco varían conjuntamente entre condiciones; por ello, las diferencias observadas no permiten identificar un efecto causal aislado ni monotónico del tamaño. No se muestran intervalos de confianza, valores p, regresiones, suavizados ni resúmenes congelados como marcas. La figura constituye una sensibilidad descriptiva dentro del benchmark interno y no representa exactitud global del framework RAG ni validez externa.

Reglas del caption:

- no mostrar `EXP11A`;
- no mostrar G3/G4/G5/G6/G7;
- no mostrar prompts, fichas, gates, commits, blobs ni nombres de artefactos;
- no presentar HE5 como soportada o rechazada; HE5 permanece `INCONCLUSIVE`;
- no atribuir efecto causal aislado o monotónico al tamaño;
- no afirmar validez jurídica ni exactitud global del RAG.

El rótulo visual abreviado `H100 (ref.)` del PNG es correcto. El caption conserva la semántica completa `H100 (n=1, referencia congelada)`.

---

## 5. Comentario Word nuevo

Añade exactamente **un comentario nuevo**. Los 193 comentarios heredados deben permanecer intactos.

El comentario debe estar anclado al cambio de Figura 6 y contener exactamente estos seis encabezados:

```text
Cambio exacto:
Motivo del cambio:
Evidencia concreta:
Fuente gobernante:
Efecto en la tesis:
Límite de interpretación:
```

Contenido mínimo obligatorio:

- la Figura 6 legacy se conserva físicamente para revisión humana;
- se inserta como propuesta el PNG aprobado de Figura 6 sin recalcular datos;
- la nueva figura representa 31 corridas observadas en seis paneles;
- distribución de condiciones `10 / 5 / 5 / 10 / 1`;
- H100 es una única referencia congelada, no una distribución de réplicas;
- tamaño y composición varían conjuntamente;
- sensibilidad descriptiva y no causal;
- no se muestran IC, valores p, regresiones, suavizados ni summaries como marcas;
- HE5 permanece inconclusa;
- no representa exactitud global del RAG, corrección jurídica ni validez externa;
- PNG aprobado: SHA-256 `4eeb3a63d4bb8a22c5b00f6d3efe4d2733c2caeec52373fa7e1c05ac27a24ae3`.

Los paths/hashes técnicos pueden aparecer en el comentario para trazabilidad, pero nunca en la prosa visible de la tesis.

`INHERITED_COMMENT_COUNT = 193`.

Usa el siguiente ID disponible. El estado heredado termina en los comentarios 442 y 443; por tanto, **se espera ID 444**. Si 444 ya está ocupado en el paquete de entrada, STOP y reporta la colisión; no renumeres comentarios heredados.

---

## 6. Trazabilidad

Conserva byte-lógicamente las 103 filas heredadas: ningún valor científico o editorial heredado puede cambiar.

Añade exactamente una fila nueva:

```text
trace_id = G7F02-V03F-FIG6-001
plan_id = A043
change_type = FIGURE_UPDATE
```

La fila debe registrar al menos:

```text
legacy_figure_preserved = YES
approved_candidate_inserted = YES
legacy_caption_visible = YES
legacy_caption_yellow_strikethrough = YES
proposed_caption_yellow = YES
second_seq_figure_created = NO
comment_added = YES
candidate_png_path = figures/group7/g7_thesis_fig_06_sensitivity.png
candidate_png_git_blob = 667765204adbdb7ab7567e9546f6ed8c71051d91
candidate_png_sha256 = 4eeb3a63d4bb8a22c5b00f6d3efe4d2733c2caeec52373fa7e1c05ac27a24ae3
scientific_data_change = NO
scientific_geometry_change = NO
internal_ids_visible = NO
status = APPLIED
```

Resultado esperado:

```text
INHERITED_TRACE_ROWS = 103
NEW_TRACE_ROWS_ADDED = 1
TOTAL_TRACE_ROWS = 104
```

---

## 7. Invariantes estructurales

Antes de entregar verifica obligatoriamente:

```text
BASELINE_TABLE_OBJECT_COUNT = 24
FINAL_TABLE_OBJECT_COUNT = 24
TABLE_CONTENT_CHANGED = false

INHERITED_COMMENT_COUNT = 193
COMMENTS_ADDED = 1
TOTAL_COMMENT_COUNT = 194
COMMENT_444_ANCHORED = true
ALL_COMMENT_IDS_ANCHORED = true

TRACKED_DELETION_COUNT = 0
OLD_FIGURE_6_PHYSICALLY_PRESERVED = true
NEW_FIGURE_6_PNG_INSERTED = true
FIGURE_NUMBERING_OFFICIAL = 1..12 / UNCHANGED
SEQ_FIGURA_COUNT = 12
NEW_SEQ_FIGURE_FIELDS = 0

FIGURE_4_CHANGED = false
FIGURE_5_CHANGED = false
TABLE_14_CHANGED = false
TABLE_15_CHANGED = false
SECTION_4_1_5_CHANGED = false
OUT_OF_SCOPE_VISIBLE_MODIFICATIONS = 0
OUT_OF_SCOPE_COMMENT_MODIFICATIONS = 0
```

Los binarios aprobados de Figuras 4 y 5 ya integrados deben permanecer byte-idénticos dentro del DOCX.

El PNG nuevo incrustado para Figura 6 debe ser byte-idéntico al candidato aprobado antes de empaquetarlo en el Word.

---

## 8. Búsqueda de lenguaje interno visible

En todo el texto visible nuevo atribuible a esta ejecución, verifica cero apariciones de:

```text
EXP11A
G3
G4
G5
G6
G7
FIG012
FIG013
FIG014
FIG015
Prompt
source freeze
gate
commit
blob
```

Los identificadores científicos `H25`, `H50-D1`, `H50-D2`, `H75`, `H100`, Top-1/3/5/10/50 y MRR sí están permitidos.

---

## 9. QA visual localizado

Renderiza el DOCX resultante e inspecciona visualmente, como mínimo:

- página de Tabla 15 y su interpretación;
- Figura 6 legacy;
- caption legacy marcado amarillo + tachado;
- línea temporal de propuesta;
- PNG propuesto de Figura 6;
- caption propuesto completo;
- inicio de 4.1.5 como frontera posterior.

Verifica:

- ausencia de clipping;
- ausencia de solapamiento;
- imagen no deformada;
- proporción 3:2 preservada;
- texto interno del PNG legible;
- rótulo `H100 (ref.)` legible y sin solapamiento con H75;
- caption legible;
- continuidad editorial razonable;
- 4.1.5 intacta;
- no modificación de márgenes, tamaño de página o secciones para hacer caber la propuesta.

Si existe un defecto material de layout, STOP y reporta; no corrijas fuera del alcance.

---

## 10. Salidas

No sobrescribas F. Genera exclusivamente:

```text
Molleapasa_gv_G7F02_REVIEW_V03_F_FIG6.docx
g7_thesis_claim_traceability_v0.3_F_FIG6.csv
```

Publica la respuesta oficial en:

```text
writing_prompts_tmp/121F_FIG6_RESPUESTA_INTEGRAR_FIGURA6_REVIEW_V03.md
```

sobre `codex/prompts-temporary`.

Calcula hashes **después de cerrar definitivamente** los archivos.

La respuesta debe reportar SHA-256 y tamaño exactos del DOCX y CSV y terminar con:

```text
PROMPT121F_FIG6_EXECUTION = COMPLETE | STOPPED_PRECONDITION
A043_APPLIED = true|false
FIGURE_6_LEGACY_PRESERVED = true|false
FIGURE_6_APPROVED_CANDIDATE_INSERTED = true|false
FIGURE_6_APPROVED_PNG_SHA256 = 4eeb3a63d4bb8a22c5b00f6d3efe4d2733c2caeec52373fa7e1c05ac27a24ae3 | <detalle>
LEGACY_CAPTION_YELLOW_STRIKETHROUGH = true|false
TEMPORARY_LABEL_EXACT = true|false
TEMPORARY_LABEL_YELLOW = true|false
FIGURE_6_FULL_CAPTION_EXACT = true|false
NEW_SEQ_FIGURE_FIELDS = 0|<n>
INHERITED_TRACE_ROWS = 103
NEW_TRACE_ROWS_ADDED = 1|<n>
TOTAL_TRACE_ROWS = 104|<n>
INHERITED_COMMENT_COUNT = 193
COMMENTS_ADDED = 1|<n>
TOTAL_COMMENT_COUNT = 194|<n>
COMMENT_444_ANCHORED = true|false
ALL_COMMENT_IDS_ANCHORED = true|false
TRACKED_DELETION_COUNT = 0|<n>
TABLE_OBJECT_COUNT = 24|<n>
FIGURE_4_CHANGED = false|true
FIGURE_5_CHANGED = false|true
TABLE_14_CHANGED = false|true
TABLE_15_CHANGED = false|true
SECTION_4_1_5_CHANGED = false|true
OUT_OF_SCOPE_VISIBLE_MODIFICATIONS = 0|<n>
OUT_OF_SCOPE_COMMENT_MODIFICATIONS = 0|<n>
LOCAL_VISUAL_REVIEW = PASS|FAIL
121G_EXECUTED = false
G7_F02_STATE = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
G7_F03_AUTHORIZED = false
EXTERNAL_AUDIT = PENDING_BY_IA_EXPERIMENTAL
```

Detente para auditoría externa de IA Experimental. No ejecutes 121G.
