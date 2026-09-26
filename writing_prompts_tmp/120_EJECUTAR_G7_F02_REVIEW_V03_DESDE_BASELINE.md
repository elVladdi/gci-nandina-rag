# PROMPT120 — EJECUTAR G7-F02 REVIEW V03 DESDE EL BASELINE ORIGINAL

## 0. Rol y autorización

Actúa como **IA de Redacción Científica** del proyecto `elVladdi/gci-nandina-rag`.

No eres CODEX. No eres la IA Experimental. Tu función en esta ejecución es **materializar una nueva copia de revisión V03 de la tesis**, partiendo exclusivamente del baseline autoritativo y aplicando el plan corregido y auditado de Prompt119.

La IA Experimental auditó independientemente Prompt119 y establece como vinculante:

```text
PROMPT119_EXTERNAL_AUDIT = PASS
PLAN_FOR_V03 = APPROVED_FOR_EXECUTION
AUTHOR_REJECTION_OF_V01_V02 = BINDING
REWRITE_BASE = ORIGINAL_BASELINE_ONLY
G7_F02 = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
G7_F03_AUTHORIZED = false
GROUP7_CLOSED = false
```

Esta autorización permite generar **solo una copia REVIEW V03 para revisión humana**. No permite generar una copia limpia final, aprobar G7-F02 ni avanzar a G7-F03.

---

## 1. Entradas vinculantes

### 1.1 Baseline único de edición

```text
FILENAME = Molleapasa_gv_vigente_2026-09-22.docx
SHA256 = 08b48ec1687ae0a0d943724bf2d682aca02d2a9f5a124b3dc35270e041bc3aed
SIZE_BYTES = 4360620
ROLE = CURRENT_WORKING_MASTER / AUTHOR_CONFIRMED / THESIS_CORRECTION_BASELINE
```

Antes de editar, recalcula SHA-256 y tamaño. Si no coinciden exactamente, STOP.

**V01 y V02 están rechazadas por el autor.** No debes copiar de ellas texto, tablas, estructura, numeración, estilos ni decisiones editoriales. Solo pueden consultarse, si fuera técnicamente imprescindible, como evidencia negativa de qué no repetir; no son fuente de redacción.

### 1.2 Plan aprobado para esta ejecución

Usa como contrato de ejecución:

```text
writing_prompts_tmp/119_RESPUESTA_CORREGIR_PLAN_G7_F02_ANTES_DE_V03.md
commit = 583138f94646b1e84de1c28f32342e59f82988a3
blob = 5472f7183618ed1a806220c8ee679ab186b7bc79
```

Debes ejecutar MATRIZ A, MATRIZ B, MATRIZ C, MATRIZ D, `CROSS_REFERENCE_AUDIT` y `PRESENTATION_MODE_AUDIT` exactamente como fueron corregidos en Prompt119.

Si durante la edición descubres una contradicción material entre Prompt119 y una fuente científica gobernante, **STOP** y reporta el conflicto. No improvises una nueva decisión editorial o científica.

### 1.3 Fuentes científicas

Mantén la jerarquía ya aprobada en G7-F01:

1. proyecto de tesis aprobado → formulaciones de problema, objetivos, hipótesis y alcance aprobado;
2. artefactos experimentales congelados → métodos y resultados;
3. G3 → inferencia, poblaciones, HE2 y HE5;
4. fuentes congeladas de Group1/Group2 → HE3, HE4, reproducibilidad y ausencia formal HE1;
5. G4 → fuerza de claims, interpretación, limitaciones y contraste con literatura;
6. G5 → cifras/tablas canónicas;
7. G6 → figuras/captions científicos aprobados;
8. baseline → contrato editorial, no verdad científica cuando esté superseded;
9. v13 → fuente auxiliar metodológica, no gobernante.

No hagas búsqueda web. No introduzcas nuevas referencias, métricas, inferencias, p-values, CI, hipótesis o resultados.

---

## 2. Principio editorial rector

La V03 debe verse como **el mismo Word del baseline, corregido localmente**, no como una tesis reconstruida.

```text
BASELINE_FORMAT_AND_WRITING_STYLE = BINDING
REDESIGN = PROHIBITED
REBUILD_DOCX_FROM_SCRATCH = PROHIBITED
```

Preserva, salvo donde una modificación aprobada lo haga estrictamente necesario:

- orden y jerarquía de secciones;
- estilos Word existentes;
- márgenes y secciones;
- encabezados y pies;
- numeración de páginas;
- formato de párrafos;
- formato y ancho de tablas;
- formato de captions;
- tipografías, tamaños, interlineado y sangrías del baseline;
- elementos institucionales;
- referencias bibliográficas existentes;
- estructura general del índice.

No crees nuevos estilos personalizados salvo imposibilidad técnica documentada. Todo texto nuevo debe heredar el estilo del párrafo/celda/caption equivalente del baseline.

---

## 3. Convención de revisión visible

La V03 es una copia de revisión, no una copia limpia.

Aplica físicamente:

```text
TEXTO_ANTERIOR_MODIFICADO = AMARILLO + TACHADO + VISIBLE
TEXTO_NUEVO = AMARILLO + NO_TACHADO + VISIBLE
TEXTO_SIN_CAMBIO = NORMAL
```

Reglas de granularidad:

1. Si cambia una cifra, palabra o frase → marca únicamente ese fragmento.
2. Si cambia una oración → conserva la oración antigua marcada y coloca la nueva de forma inmediata y legible.
3. No marques un párrafo completo cuando el cambio real afecte solo una parte.
4. Solo cuando la mayor parte del contenido semántico de un párrafo deba sustituirse conforme a `PARAGRAPH_REWRITE_MINIMAL`, puede conservarse el párrafo anterior completo tachado+amarillo y colocarse debajo el párrafo nuevo amarillo. Debe justificarse en comentario.
5. No uses tracked deletion (`w:del`) como mecanismo de ocultamiento. El material anterior debe permanecer físicamente visible.
6. No elimines silenciosamente contenido del baseline dentro del alcance de G7-F02.

---

## 4. Política de tablas — vinculante

El baseline contiene **24 objetos de tabla**. La V03 debe mantener:

```text
BASELINE_TABLE_OBJECT_COUNT = 24
REVIEW_V03_TABLE_OBJECT_COUNT = 24
TABLE_OBJECT_COUNT_DELTA = 0
WHOLE_TABLE_DUPLICATION = 0
```

No dupliques ni reemplaces una tabla completa.

Para cada Tabla 1–24:

- conserva el mismo objeto de tabla;
- modifica primero el fragmento mínimo dentro de una celda;
- si cambia una celda, marca solo el contenido afectado de esa celda;
- si cambia una fila, marca solo las celdas afectadas;
- si cambia un encabezado, marca solo el encabezado afectado;
- conserva ancho, bordes, estilos, alineación y propiedades del baseline salvo necesidad técnica inevitable y documentada.

Las actualizaciones `TABLE_STRUCTURE_UPDATE` de Prompt119 significan **adaptar el objeto existente in-place**, nunca crear una segunda tabla.

### 4.1 Numeración corporal

Conserva exactamente:

```text
TABLAS_EN_CUERPO = 1..24
```

No renumeres ninguna tabla corporal.

### 4.2 Lista de Tablas

Corrige el defecto preexistente según Prompt119:

- incorporar la entrada faltante de Tabla 3;
- corregir el desplazamiento de etiquetas de la lista desde Tabla 4 hasta la entrada residual Tabla 25;
- terminar la lista en Tabla 24;
- no modificar la numeración corporal 1–24.

El marcado de revisión debe mostrar exactamente los números antiguos modificados y sus números nuevos, no reemplazar la Lista de Tablas completa.

### 4.3 Diez referencias corporales incorrectas

Aplica de forma mínima las correcciones A073–A082 de Prompt119:

```text
3.2.4   Tabla 4 -> Tabla 3
3.2.4   Tabla 6 / sección 3.6 -> Tabla 7 / sección 3.7.5
3.7.5   Tabla 8 -> Tabla 7
3.8.1   Tabla 9 -> Tabla 8
3.8.7   Tabla 10 -> Tabla 9
4.1.3   Tabla 13 -> Tabla 12
4.1.3   Los valores de la Tabla 13 -> Tabla 12
4.1.8   Tabla 21 -> Tabla 20
4.2     Tabla 10 -> Tabla 9
4.3.5   Tabla 24 -> Tabla 23
```

No modifiques referencias correctas.

---

## 5. Política de figuras — V03 de revisión

La V03 conserva la numeración oficial del baseline:

```text
REVIEW_V03_FIGURE_NUMBERING = 1..12
```

### 5.1 Figuras 1–3

Conservar según Prompt119. Solo aplicar cambios terminológicos si realmente están autorizados y son necesarios.

### 5.2 Figuras 4–6 — sustitución propuesta

Las figuras antiguas deben permanecer físicamente visibles para revisión del autor.

Procedimiento:

1. conserva la figura antigua;
2. marca su caption antiguo con amarillo+tachado solo en la parte que cambiará;
3. añade comentario Word detallando por qué la figura está científicamente desactualizada;
4. inserta inmediatamente después la figura científica vigente de G6 correspondiente;
5. **no crees un segundo caption oficial numerado**;
6. usa sobre la imagen nueva una etiqueta temporal de revisión, resaltada en amarillo y con estilo no-caption, por ejemplo:

```text
PROPUESTA DE REEMPLAZO DEL ELEMENTO GRÁFICO ANTERIOR — NO ES NUMERACIÓN FINAL
```

7. coloca el caption final propuesto resaltado en amarillo, pero sin crear un segundo campo `SEQ Figura` ni alterar la Lista de Figuras;
8. la figura oficial conserva durante V03 su número 4, 5 o 6.

Usa exclusivamente las figuras/captions aprobados de G6, adaptados únicamente al lenguaje editorial natural de la tesis y sin IDs internos.

### 5.3 Figuras 7–10 — supresión propuesta

No borres las imágenes.

- deben permanecer visibles;
- conserva los números 7, 8, 9 y 10;
- marca el caption como supresión propuesta mediante amarillo+tachado en el texto afectado;
- añade comentario detallado explicando la obsolescencia/redundancia o no estimabilidad que justifica la propuesta;
- no insertes figura de reemplazo;
- mantén sus entradas 7–10 en la Lista de Figuras durante V03.

### 5.4 Figuras 11–12

Conservar como 11 y 12. No ejecutar 11→7 ni 12→8 en V03.

Solo una futura copia limpia, posterior a aceptación explícita del autor de la supresión de 7–10, podría renumerarlas.

---

## 6. Presentación prosa vs. tabla/figura

Ejecuta exactamente `PRESENTATION_MODE_AUDIT` de Prompt119.

Reglas vinculantes:

- HE2 → Tablas 12–14 + Figuras 4–5 + párrafo de síntesis; no repetir todas las cifras en prosa.
- HE3 → Tablas 16–17 + párrafo de síntesis; no crear tabla/figura nueva.
- HE4 → Tablas 18–19 + síntesis; Figura 9 queda como supresión propuesta.
- HE5 → Tablas 15 y 20 + síntesis; Figura 10 queda como supresión propuesta.
- sensibilidad conjunta del tamaño/composición del banco histórico → Figura 6 + síntesis breve; no crear tabla nueva.
- sensibilidad descriptiva H150/H200 sobre diez pares observados → párrafo breve + fila de limitación en Tabla 24; no importar la matriz completa al cuerpo.
- análisis planificado de diversidad cerrado sin recuperación → filas pertinentes en Tablas 20/24 + párrafo breve; no crear figura ni tabla nueva.
- reproducibilidad → Tablas 7/24 + síntesis; prohibido “reproducibilidad completa” o “reproducibilidad total”.

No crees ninguna tabla nueva en V03.

---

## 7. Lenguaje de tesis y prohibición de gobernanza interna

La prosa visible debe leerse como tesis académica, no como reporte de gobernanza.

Ejecuta MATRIZ D de Prompt119 y realiza una búsqueda final exhaustiva.

No deben aparecer en prosa visible, captions ni tablas del manuscrito términos internos tales como:

```text
G1, G2, G3, G4, G5, G6, G7, G8
Group1, Group2, ...
G3-Fxx, G4-Fxx, G5-Fxx, G6-Fxx, G7-Fxx
Prompt116, Prompt117, Prompt118, Prompt119, Prompt120
PREFxxx
source freeze
claim registry / claim ID
G3C-xxx / G4Fxx-xxx
candidate pending external audit
revision required
ficha / gate
CLOSED / APPROVED como estados administrativos
G5-MAIN-xx / G5-SECONDARY / G6-FIG-xx
Attempt06
Phase E
A_historical_defined
diagnostic_union_hierarchical_dual
PROMPT_SCHEMA_SPECIFICATION_MISMATCH
EVALUATOR_MODALITY_DEVIATION
AI_EXPERT_ROLE
```

Cuando el concepto científico sea necesario, tradúcelo al español académico natural según MATRIZ D.

Los identificadores experimentales técnicos condicionales (`H25`, `H50`, etc.) pueden mantenerse solo si se definen claramente y son necesarios para reproducibilidad científica.

Los IDs y paths técnicos sí pueden aparecer en **comentarios Word o CSV de trazabilidad**, nunca como lenguaje visible del manuscrito salvo que sean auténticos identificadores del protocolo que deban conservarse.

---

## 8. Comentarios Word — solo cambios reales

No añadas comentarios a elementos `KEEP` sin modificación.

Cada cambio visible, supresión propuesta, figura sustituida o referencia cruzada corregida debe tener un comentario en español con los seis apartados exactos:

```text
Cambio exacto:
Motivo del cambio:
Evidencia concreta:
Fuente gobernante:
Efecto en la tesis:
Límite de interpretación:
```

### Requisitos de calidad

- `Cambio exacto`: citar el valor/frase anterior y el nuevo cuando sea razonable.
- `Motivo del cambio`: explicar el defecto específico, no usar “legacy” como explicación autónoma.
- `Evidencia concreta`: incluir cifras, población, resultado o limitación que obliga al cambio cuando corresponda.
- `Fuente gobernante`: primero nombre comprensible en español; luego, opcionalmente, path/blob para trazabilidad.
- `Efecto en la tesis`: indicar qué incoherencia corrige.
- `Límite de interpretación`: decir qué conclusión no está autorizada.

Prohibidos comentarios abstractos o en inglés.

---

## 9. Ciencia congelada que no puede degradarse

Preserva, entre otros, estos límites:

```text
UNIT_OF_ANALYSIS = SERIE
DEPENDENCY_GROUP = DAM / DECLARACION WHEN_APPLICABLE
EVAL = 1056 series / 67 DAM / 42 NANDINA
HG = NO_FORMAL_DISPOSITION_FOUND
HE1 = NO_FORMAL_DISPOSITION_FOUND
HE2 = SUPPORTED
HE3 = SUPPORTED
HE4 = PARTIALLY_SUPPORTED
HE5 = INCONCLUSIVE
EXP11A = JOINT_SIZE_COMPOSITION_SENSITIVITY / NONCAUSAL
EXP11B = DESCRIPTIVE / TEN_OBSERVED_SEED_PAIRS / NO_SEED_SUPERPOPULATION_INFERENCE
EXP12 = CLOSED_WITHOUT_RETRIEVAL / NOT_ESTIMABLE / DO_NOT_REOPEN
ATTEMPT06 = METHOD_DEPENDENT / NONZERO_EV04_MRR_AND_D1A
P_VALUES_CALCULATED = false
```

En prosa visible, traduce los códigos administrativos/experimentales a lenguaje académico natural conforme a Prompt119.

No conviertas:

- superioridad del recuperador histórico en exactitud global del RAG;
- evidencia normativa en corrección jurídica vinculante;
- auditabilidad en corrección de clasificación;
- EXP11A en efecto causal aislado;
- EXP11B en inferencia a una superpoblación de semillas;
- Attempt06 en impacto global cero;
- configurabilidad en generalización empírica.

No reabras EXP12.

---

## 10. Trazabilidad V03

Genera:

```text
g7_thesis_claim_traceability_v0.3.csv
```

Debe permitir auditar tanto ciencia como edición. Incluye como mínimo:

```text
trace_id
plan_id
thesis_section
locator
change_type
presentation_mode
baseline_text_or_value
review_v03_text_or_value
scientific_claim_or_number
hypothesis_binding
scientific_source_path
scientific_source_blob
canonical_table_or_figure_id
comment_id
old_text_visible
old_text_strikethrough
old_text_yellow_highlight
new_text_yellow_highlight
minimal_edit_scope_respected
table_or_figure_number
cross_reference_status
internal_language_scan_status
scope_limitation
forbidden_interpretation_checked
status
```

Para `KEEP` sin cambio puedes registrar `NO_CHANGE_REQUIRED`, pero no debe existir comentario Word.

La trazabilidad no sustituye la revisión visual del Word.

---

## 11. Entregables

Genera exclusivamente:

```text
Molleapasa_gv_G7F02_REVIEW_V03.docx
g7_thesis_claim_traceability_v0.3.csv
```

No sobrescribas el baseline.

No añadas los binarios a Git.

Publica únicamente la respuesta textual en:

```text
writing_prompts_tmp/120_RESPUESTA_EJECUTAR_G7_F02_REVIEW_V03_DESDE_BASELINE.md
```

rama:

```text
codex/prompts-temporary
```

---

## 12. QA estructural obligatorio antes de entregar

Debes verificar y reportar:

```text
BASELINE_SHA256_BEFORE = 08b48ec...
BASELINE_SHA256_AFTER = 08b48ec...
BASELINE_UNCHANGED = true
DOCX_ZIP_INTEGRITY = PASS
REVIEW_V03_TABLE_OBJECT_COUNT = 24
TABLE_OBJECT_COUNT_DELTA = 0
WHOLE_TABLE_DUPLICATION = 0
REVIEW_V03_OFFICIAL_FIGURE_NUMBERING = 1..12
G7_F02_INTERNAL_GOVERNANCE_TERMS_VISIBLE = 0
TRACKED_DELETION_COUNT = 0
```

Además:

- verificar que las 12 anomalías tabulares/lista de Prompt119 quedaron corregidas según el plan;
- verificar que no se generaron nuevas anomalías de referencia;
- verificar que las referencias de figuras siguen correctas y sin renumeración;
- verificar que ningún `KEEP` sin cambio recibió comentario;
- verificar que todos los comentarios nuevos contienen los seis encabezados obligatorios y están en español;
- verificar que no existen comentarios genéricos del tipo “actualizado al estado vigente”, “evidencia congelada”, “legacy conclusion”, etc.;
- verificar que no existe `G3`, `G4`, `G5`, `G6` ni otra gobernanza interna en prosa visible;
- verificar que tablas completas no fueron tachadas/duplicadas;
- verificar que el contenido nuevo de tablas se marcó al nivel mínimo posible;
- verificar que la Lista de Tablas termina en Tabla 24 y que la Lista de Figuras permanece 1–12 en V03.

---

## 13. QA visual obligatorio

Usa el flujo de QA de documentos:

1. renderiza `Molleapasa_gv_G7F02_REVIEW_V03.docx` completo con el renderer de documentos;
2. inspecciona **todas las páginas** a 100 %;
3. corrige y vuelve a renderizar si existe cualquier problema;
4. no entregues hasta que la última renderización pase.

Revisa específicamente:

- desbordes/clipping;
- tablas partidas de forma ilegible;
- bordes o anchos alterados;
- imágenes/captions separados de forma incorrecta;
- encabezados/pies desplazados;
- páginas vacías inesperadas;
- exceso de amarillo por cambios no mínimos;
- comentarios/anclajes estructurales;
- legibilidad de la comparación anterior/nueva;
- preservación del estilo del baseline.

No declares `VISUAL_REVIEW = PASS` sin inspección completa.

---

## 14. Auditoría previa a respuesta

Antes de terminar, comprueba:

```text
V01_USED_AS_DRAFT_SOURCE = false
V02_USED_AS_DRAFT_SOURCE = false
NEW_SCIENTIFIC_CLAIMS = 0
NEW_METRICS = 0
NEW_INFERENCE = 0
NEW_P_VALUES = 0
NEW_CI = 0
NEW_REFERENCES = 0
HG_FORMAL_DISPOSITION_INVENTED = false
HE1_FORMAL_DISPOSITION_INVENTED = false
EXP12_REOPENED = false
G7_F03_AUTHORIZED = false
GROUP7_CLOSED = false
```

La V03 debe quedar:

```text
REVIEW_CANDIDATE_PENDING_AUTHOR_AND_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
```

---

## 15. Respuesta oficial

La respuesta debe incluir como mínimo:

```text
PROMPT120_EXECUTION
SOURCE_PLAN_COMMIT
SOURCE_PLAN_BLOB
BASELINE_SHA256_BEFORE
BASELINE_SHA256_AFTER
REVIEW_V03_FILENAME
REVIEW_V03_SHA256
REVIEW_V03_SIZE_BYTES
TRACE_V03_FILENAME
TRACE_V03_SHA256
TRACE_ROW_COUNT
TABLE_OBJECT_COUNT
TABLE_OBJECT_COUNT_DELTA
WHOLE_TABLE_DUPLICATION
TABLE_CROSS_REFERENCE_RECHECK
FIGURE_CROSS_REFERENCE_RECHECK
REVIEW_V03_OFFICIAL_FIGURE_NUMBERING
VISIBLE_STRIKETHROUGH_COUNT
YELLOW_HIGHLIGHT_COUNT
TRACKED_DELETION_COUNT
NEW_REVIEW_COMMENT_COUNT
COMMENT_SCHEMA_PASS
KEEP_NO_CHANGE_COMMENT_VIOLATIONS
INTERNAL_GOVERNANCE_VISIBLE_COUNT
PROHIBITED_LANGUAGE_SCAN
DOCX_ZIP_INTEGRITY
RENDER_PAGE_COUNT
VISUAL_REVIEW
NEW_SCIENTIFIC_CLAIMS
NEW_METRICS
NEW_INFERENCE
NEW_P_VALUES
NEW_CI
NEW_REFERENCES
EXP12_REOPENED
G7_F02_STATUS
G7_F03_AUTHORIZED
EXTERNAL_AUDIT
```

Estado terminal esperado:

```text
PROMPT120_EXECUTION = COMPLETE
G7_F02_STATUS = REVIEW_CANDIDATE_PENDING_AUTHOR_AND_EXTERNAL_AUDIT / EXECUTED / NOT_APPROVED
G7_F03_AUTHORIZED = false
EXTERNAL_AUDIT = PENDING_BY_IA_EXPERIMENTAL
```

Detente ahí. No generes una copia limpia ni cierres G7-F02.