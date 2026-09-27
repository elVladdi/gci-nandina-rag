# PROMPT121E-FIG45 — Integrar Figuras 4 y 5 aprobadas en REVIEW V03

## 0. Actor y autorización

Actúa como **IA de Redacción Científica** del proyecto `elVladdi/gci-nandina-rag`.

No eres CODEX. No eres la IA Experimental. No regeneres figuras ni recalcules datos.

Esta ejecución está autorizada únicamente para integrar en la copia REVIEW V03 las propuestas aprobadas de reemplazo de las Figuras 4 y 5, preservando las figuras antiguas para revisión humana.

```text
PROMPT121E_EXTERNAL_AUDIT = PASS
FIG010_EXTERNAL_AUDIT = PASS
FIG011A_EXTERNAL_AUDIT = PASS
FIG011B_EXTERNAL_AUDIT = PASS
FIGURE_4_CANDIDATE = APPROVED_FOR_LATER_DOCX_INTEGRATION
FIGURE_5_CANDIDATE = APPROVED_FOR_LATER_DOCX_INTEGRATION
121F_AUTHORIZED = false
G7_F02 = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
G7_F03_AUTHORIZED = false
```

No ejecutes 121F ni ningún bloque posterior.

---

## 1. Entradas obligatorias

### 1.1 Word acumulativo autorizado

Usa exclusivamente:

```text
Molleapasa_gv_G7F02_REVIEW_V03_E.docx
SHA256 = f6eb5a9f4db80faa36306df64ec51ddd865df2a081d69f65ca6a3e063ec2b7ba
```

### 1.2 Trazabilidad acumulativa autorizada

```text
g7_thesis_claim_traceability_v0.3_E.csv
SHA256 = c8bd644af8b660269f6bb7ea6f7cebf615ad9a3d23a42ac9a2814949ae8be05f
INHERITED_ROWS = 99
```

Recalcula ambos SHA-256 antes de editar. Si alguno no coincide, STOP.

### 1.3 Figura 4 aprobada

```text
figures/group7/g7_thesis_fig_04_he2.png
GIT_BLOB = eb77a4f2289a8701d22ba399d9432defd2092e2a
SHA256 = 5cde004fc5b3b76578de02bd9d4751c52d26f921821c96a0bafc1cac65c1eb1e

figures/group7/g7_thesis_fig_04_he2.svg
GIT_BLOB = e84fa3ee6aaedb2d3d24b59ce7255214621aae3f
```

Auditoría externa:

```text
figure_prompts_tmp/FIG011A_AUDITORIA_EXTERNA_PASS.md
```

### 1.4 Figura 5 aprobada

```text
figures/group7/g7_thesis_fig_05_coverage.png
GIT_BLOB = d63559e4da4b391d47968a60a41649c715d5408b
SHA256 = aecc77e8fd6272766eaf9f7a72d6bc531ef45d448264cac1b95a2ac30edd59c0

figures/group7/g7_thesis_fig_05_coverage.svg
GIT_BLOB = 6cba4d776046e052ca4f76297ab627f2a3762046
```

Auditoría externa:

```text
figure_prompts_tmp/FIG011B_AUDITORIA_EXTERNA_PASS.md
```

Si no puedes acceder exactamente a los dos PNG aprobados, STOP. No los reconstruyas ni sustituyas por imágenes similares.

---

## 2. Fuentes de procedimiento que debes leer

Lee íntegramente antes de editar:

```text
writing_prompts_tmp/119_RESPUESTA_CORREGIR_PLAN_G7_F02_ANTES_DE_V03.md
writing_prompts_tmp/120_EJECUTAR_G7_F02_REVIEW_V03_DESDE_BASELINE.md
figure_prompts_tmp/FIG010_RESPUESTA_AUDITAR_ADAPTACION_TESIS_FIGURAS_4_5_G7_F02.md
figure_prompts_tmp/FIG010_AUDITORIA_EXTERNA_PASS.md
figure_prompts_tmp/FIG011A_AUDITORIA_EXTERNA_PASS.md
figure_prompts_tmp/FIG011B_AUDITORIA_EXTERNA_PASS.md
```

Ejecuta exclusivamente A039 y A040 del plan aprobado.

---

## 3. Alcance único

Modifica únicamente el bloque de **4.1.3** correspondiente a las actuales Figuras 4 y 5 y sus captions.

No modifiques:

- la prosa ya aprobada de 4.1.3;
- Tabla 12;
- Tabla 13;
- 4.1.4;
- Tabla 14;
- Figura 6;
- ninguna sección anterior;
- ninguna sección posterior;
- ninguna otra figura;
- la numeración oficial 1–12;
- la Lista de Figuras en esta ejecución.

---

## 4. Convención de revisión obligatoria para figuras

Esta es una copia REVIEW V03. **No elimines las Figuras 4 y 5 legacy.**

Para cada figura:

1. conserva físicamente la imagen legacy original;
2. conserva su número oficial actual;
3. marca el texto del caption antiguo que queda superseded con **amarillo + tachado**, de forma visible;
4. añade un comentario Word detallado en español asociado al cambio;
5. inmediatamente después inserta una línea temporal de revisión, resaltada en amarillo y con estilo de párrafo normal/no-caption:

```text
PROPUESTA DE REEMPLAZO DEL ELEMENTO GRÁFICO ANTERIOR — NO ES NUMERACIÓN FINAL
```

6. inserta inmediatamente después el PNG aprobado correspondiente;
7. debajo, incorpora el caption final propuesto **resaltado en amarillo**, pero como texto de revisión: no crees un segundo campo `SEQ Figura` ni una nueva entrada automática de Lista de Figuras;
8. no alteres ni ocultes la imagen legacy;
9. no insertes el SVG en el Word; usa el PNG aprobado para evitar variaciones de render.

No uses `w:del` ni elimines contenido previo.

---

## 5. Caption final propuesto — Figura 4

Usa exactamente como texto visible de propuesta:

**Figura 4. Evidencia primaria de HE2: ordenamiento temprano y cobertura profunda en la evaluación interna realizada fuera de línea del Capítulo 87 (1 056 series, 67 DAM y 42 subpartidas NANDINA).** (A) Valores observados de la recuperación histórica y de los tres comparadores corregidos —BM25 normativo plano, BM25 normativo jerárquico y recuperador denso entrenado con MNRL— en Top-1, Top-3, Top-5, Top-10 y MRR@100; los valores por brazo son descriptivos y no tienen intervalos de confianza por brazo autorizados. (B) Quince diferencias pareadas entre la recuperación histórica y cada comparador, correspondientes a las cinco métricas primarias y los tres comparadores, con intervalos de confianza del 99 % sobre cada diferencia pareada. (C) Único contraste primario de cobertura profunda del recuperador jerárquico, `Recall@200 − Recall@100`, con intervalo de confianza del 95 %; Recall@100 y Recall@200 se muestran únicamente como contexto y Pool@200 no se duplica como evidencia confirmatoria. No se calcularon valores p. Los contrastes son no causales y se limitan a esta evaluación interna; la figura no representa la exactitud global del marco RAG, corrección jurídica ni validez externa.

No introduzcas `Attempt06`, `D1a`, G5/G6 ni identificadores internos en el caption visible.

---

## 6. Caption final propuesto — Figura 5

Usa exactamente como texto visible de propuesta:

**Figura 5. Cobertura exacta NANDINA según profundidad y variante en la evaluación interna realizada fuera de línea del Capítulo 87 (1 056 series, 67 DAM y 42 subpartidas NANDINA).** Se muestran 15 proporciones descriptivas de cobertura exacta NANDINA: cinco variantes en cada profundidad de recuperación 50, 100 y 200. Solo jerárquico, Solo dual, Jerárquico con prioridad para los primeros 100 candidatos y Jerárquico 80 + backfill dual 20 corresponden a las cuatro variantes descriptivas predefinidas; Jerárquico 70 + backfill dual 30 se incluye únicamente como contexto descriptivo adicional y no fue seleccionada por favorabilidad. No se presentan intervalos de confianza, valores p, tendencias ajustadas ni contrastes inferenciales entre variantes. La unión diagnóstica jerárquica-dual se excluye del rendimiento ordinario porque representa un techo de cobertura y no una variante de desempeño ordinario. La figura no establece un orden de favorabilidad entre variantes ni modifica la evidencia confirmatoria o la disposición de HE2.

No introduzcas `Phase E`, `hierarchical_*`, `A_historical_defined`, `G3C-005`, `diagnostic_union_hierarchical_dual` ni identificadores internos en el caption visible.

---

## 7. Comentarios Word

Añade **exactamente 2 comentarios nuevos**, uno por cada figura. No modifiques comentarios heredados.

Cada comentario debe estar íntegramente en español y contener exactamente estos seis apartados:

```text
Cambio exacto:
Motivo del cambio:
Evidencia concreta:
Fuente gobernante:
Efecto en la tesis:
Límite de interpretación:
```

### Contenido mínimo comentario Figura 4

Debe explicar que la figura legacy se conserva para revisión, pero la propuesta la sustituye porque contenía representación desactualizada/identificadores internos; la nueva figura conserva datos e inferencia ya aprobados de HE2 sin recalcular valores; mantiene 15 contrastes con IC 99 % y un contraste profundo con IC 95 %; no introduce p-values ni CI por brazo; no representa exactitud global del RAG ni corrección jurídica.

### Contenido mínimo comentario Figura 5

Debe explicar que la figura legacy se conserva para revisión, pero la propuesta naturaliza el gráfico vigente de cobertura; conserva las cinco variantes × tres profundidades y sus quince valores descriptivos; no introduce inferencia, IC, valores p o ranking de favorabilidad; la quinta variante es contexto descriptivo adicional y la unión diagnóstica no es rendimiento ordinario.

Los paths/hashes técnicos pueden aparecer en comentarios para trazabilidad, pero no en la prosa visible de la tesis.

---

## 8. Trazabilidad

Conserva byte-lógicamente las 99 filas heredadas: no cambies sus valores científicos/editoriales.

Añade exactamente dos filas nuevas:

```text
A039 = Figura 4
A040 = Figura 5
```

Cada fila debe registrar al menos:

- acción `FIGURE_UPDATE`;
- imagen legacy preservada = YES;
- candidato aprobado insertado = YES;
- caption legacy visible = YES;
- caption legacy marcado amarillo+tachado = YES;
- caption propuesto amarillo = YES;
- segundo `SEQ Figura` creado = NO;
- comentario detallado añadido = YES;
- candidate PNG path;
- candidate PNG SHA-256;
- `scientific_data_change = NO`;
- `internal_ids_visible = NO`;
- estado `APPLIED`.

Resultado esperado:

```text
INHERITED_TRACE_ROWS = 99
NEW_TRACE_ROWS_ADDED = 2
TOTAL_TRACE_ROWS = 101
```

---

## 9. Validaciones estructurales

Antes de entregar verifica:

```text
BASELINE_TABLE_OBJECT_COUNT = 24
FINAL_TABLE_OBJECT_COUNT = 24
TABLE_CONTENT_CHANGED = false

INHERITED_COMMENT_COUNT = 189
COMMENTS_ADDED = 2
TOTAL_COMMENT_COUNT = 191
ALL_COMMENT_IDS_ANCHORED = true

TRACKED_DELETION_COUNT = 0
OLD_FIGURE_4_PHYSICALLY_PRESERVED = true
OLD_FIGURE_5_PHYSICALLY_PRESERVED = true
NEW_FIGURE_4_PNG_INSERTED = true
NEW_FIGURE_5_PNG_INSERTED = true
FIGURE_NUMBERING_OFFICIAL = 1..12 / UNCHANGED
NEW_SEQ_FIGURE_FIELDS = 0
OUT_OF_SCOPE_VISIBLE_MODIFICATIONS = 0
OUT_OF_SCOPE_COMMENT_MODIFICATIONS = 0
```

Busca además en todo texto visible nuevo alrededor de las propuestas:

```text
Attempt06
D1a
Phase E
hierarchical_only
dual_only
hierarchical_first_100
hierarchical_80_dual_backfill_20
hierarchical_70_dual_backfill_30
A_historical_defined
G3C-005
diagnostic_union_hierarchical_dual
G5
G6
FIG011
Prompt
source freeze
gate
```

Resultado permitido: cero apariciones nuevas visibles atribuibles a esta ejecución.

---

## 10. QA visual localizado

Renderiza el DOCX resultante.

Inspecciona visualmente todas las páginas que contengan:

- Figura 4 legacy;
- propuesta Figura 4;
- caption propuesto Figura 4;
- Figura 5 legacy;
- propuesta Figura 5;
- caption propuesto Figura 5;
- una página anterior y una posterior como fronteras.

Verifica:

- ningún clipping;
- ninguna imagen deformada;
- proporciones originales de cada PNG preservadas;
- resolución visual suficiente;
- captions legibles;
- ausencia de superposición;
- continuidad razonable de 4.1.3;
- 4.1.4 permanece intacta.

Si insertar ambas propuestas produce un layout materialmente defectuoso, STOP y reporta; no cambies márgenes, secciones ni tamaño global de página para hacerlo caber.

---

## 11. Salidas

Genera exclusivamente:

```text
Molleapasa_gv_G7F02_REVIEW_V03_E_FIG45.docx
g7_thesis_claim_traceability_v0.3_E_FIG45.csv
```

No sobrescribas E.

Publica la respuesta oficial en:

```text
writing_prompts_tmp/121E_FIG45_RESPUESTA_INTEGRAR_FIGURAS_4_5_REVIEW_V03.md
```

sobre `codex/prompts-temporary`.

La respuesta debe incluir SHA-256 y tamaño de ambas salidas y el estado terminal:

```text
PROMPT121E_FIG45_EXECUTION = COMPLETE | STOPPED_PRECONDITION
FIGURE_4_LEGACY_PRESERVED = true|false
FIGURE_4_APPROVED_CANDIDATE_INSERTED = true|false
FIGURE_5_LEGACY_PRESERVED = true|false
FIGURE_5_APPROVED_CANDIDATE_INSERTED = true|false
NEW_SEQ_FIGURE_FIELDS = 0|<n>
INHERITED_TRACE_ROWS = 99
NEW_TRACE_ROWS_ADDED = 2|<n>
INHERITED_COMMENT_COUNT = 189
COMMENTS_ADDED = 2|<n>
ALL_COMMENT_IDS_ANCHORED = true|false
TRACKED_DELETION_COUNT = 0|<n>
OUT_OF_SCOPE_VISIBLE_MODIFICATIONS = 0|<n>
OUT_OF_SCOPE_COMMENT_MODIFICATIONS = 0|<n>
LOCAL_VISUAL_REVIEW = PASS|FAIL
121F_EXECUTED = false
G7_F02_STATE = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
G7_F03_AUTHORIZED = false
EXTERNAL_AUDIT = PENDING_BY_IA_EXPERIMENTAL
```

Detente para auditoría externa. No ejecutes 121F.
