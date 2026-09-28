# PROMPT121K — Ejecutar G7-F02 REVIEW V03 — Bloque K: 4.2 contrastación de hipótesis

## 0. Actor y autorización

Actúa como **IA de Redacción Científica** del proyecto `elVladdi/gci-nandina-rag`.

No eres CODEX. No eres la IA Experimental. No recalcules métricas, no generes nueva inferencia y no ejecutes 4.3 ni ningún bloque posterior.

Esta ejecución queda autorizada exclusivamente después del PASS externo de 121J:

```text
PROMPT121J_EXTERNAL_AUDIT = PASS
A051_EXTERNAL_AUDIT = PASS
A052_EXTERNAL_AUDIT = PASS
121J_CLOSED_FOR_DOWNSTREAM = true
121K_AUTHORIZED = true
G7_F02 = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
G7_F03_AUTHORIZED = false
```

Auditoría gobernante:

```text
writing_prompts_tmp/121J_AUDITORIA_EXTERNA_PASS.md
GIT_BLOB = d017ebe350c151d652e3b4a616975c6e62cdb089
```

Ejecuta exclusivamente **A053–A060** del plan aprobado.

No ejecutes A061, 4.3, 121L ni ningún bloque posterior.

---

## 1. Entradas acumulativas exactas

Trabaja exclusivamente sobre:

```text
Molleapasa_gv_G7F02_REVIEW_V03_J.docx
SHA256 = 0b158d02b298bd22e32577e9fa28ad7bc64bf49e295702deb90088507934819c
SIZE = 4673319

g7_thesis_claim_traceability_v0.3_J.csv
SHA256 = 953a62856cc4819df2c3c9e7511c79e08b78a8073fa2adec1bbcb578e704ca0c
SIZE = 106581
ROWS = 113
```

Verifica hashes, tamaños y filas antes de editar. Si alguno no coincide, `STOPPED_PRECONDITION`.

No reconstruyas J desde versiones anteriores.

Estado heredado obligatorio:

```text
TABLE_OBJECT_COUNT = 24
COMMENT_COUNT = 203
TRACE_ROWS = 113
SEQ_FIGURA_COUNT = 12
MEDIA_FILE_COUNT = 16
TRACKED_DELETION_COUNT = 0
```

---

## 2. Fuentes científicas gobernantes

Lee y verifica las siguientes fuentes congeladas antes de redactar:

```text
docs/writing/group7/g7_writing_source_freeze_v0.1.json
GIT_BLOB = 776fcb52e8ada9967504001b897c75b4108bfb63

docs/writing/group7/g7_writing_source_freeze_v0.1.md
GIT_BLOB = feea31e2a45ee5f3d9b8fa1f9a1e1bdc073d6430

outputs/analysis/group3/g3_hypothesis_disposition_v0.1.json
GIT_BLOB = d8f20498ebd26e467ba1916e3e0ed93d1dd06c61

outputs/analysis/group3/g3_inferential_results_v0.1.json
GIT_BLOB = f99b7e46d81b28ca2b7cfce8d24788ad14156dcc

outputs/evaluation/exp04_consolidated_closure_v0.2/gate_exp04_consolidated_closure_manifest_v0.2.json
GIT_BLOB = 643ca2a225572a8406302baa94cf6f8e7df90769

outputs/evaluation/exp04_consolidated_closure_v0.2/exp04_hypothesis_status_registry_v0.2.csv
GIT_BLOB = 28cd7fbc492ecc4d4744ec5c3433ce5342213e79

outputs/audits/g2a_reproducibility_v0.1/gate_g2a_reproducibility_manifest_v0.1.json
GIT_BLOB = dacbf468fea850ea04632aaf9ade4b43e7748f17

outputs/audits/group2b_reproducibility_closure_v0.1.json
GIT_BLOB = 82e49fc9a04cd0bc19b95c863caf209d542144cd

outputs/evaluation/historical_normative_integration_data_aduanas_clase87_v0.2/integration_ranking_invariance.json
GIT_BLOB = b295b399d80eee5fb21d1fd582cccae9afef4bdd

outputs/evaluation/historical_normative_integration_data_aduanas_clase87_v0.2/integration_traceability.json
GIT_BLOB = 4fbe3128ce8f453d9ae47eff6f76106b97b1ceea

outputs/evaluation/diagnostic_llm_reranker_data_aduanas_clase87_v0.2/summary.md
GIT_BLOB = 2e356497695551c9df61fb36e70d0cd6d2003daa

outputs/evaluation/he4_top3_explainer_data_aduanas_clase87_v0.2/he4_he4_joint_jk_assessment_v0.2.json
GIT_BLOB = b617b4f397d0ffb4f8882ddda06790b1c539543e

outputs/evaluation/he4_top3_explainer_data_aduanas_clase87_v0.2/he4_qualitative_findings_v0.2.md
GIT_BLOB = 4b9dd1b3079235b2c54d5777fc788f0e98b27e32

docs/analysis/group4/g4_interpretation_synthesis_v0.1.md
GIT_BLOB = 129a67b15db429b86af059d61753b1942c8f243f
```

### 2.1 Disposiciones científicas vinculantes

```text
HG = NO_FORMAL_DISPOSITION_FOUND
HE1 = NO_FORMAL_DISPOSITION_FOUND
HE2 = SUPPORTED
HE3 = SUPPORTED
HE4 = PARTIALLY_SUPPORTED
HE5 = INCONCLUSIVE
```

Estas disposiciones gobiernan la redacción. No derives una disposición nueva ni conviertas evidencia metodológica en una decisión no existente.

### 2.2 Reglas vinculantes por hipótesis

**HG**
- no existe disposición formal terminal localizada;
- no declarar `respaldada`, `rechazada`, `parcialmente respaldada` ni equivalente;
- describir la evidencia de los componentes por separado;
- no derivar un dictamen agregado a partir de HE1–HE5.

**HE1**
- no existe disposición formal terminal localizada;
- los controles de integridad, procedencia, trazabilidad y reproducibilidad son evidencia metodológica con limitaciones;
- no convertir el cierre de reproducibilidad G2A/G2B en una decisión post hoc sobre HE1;
- no usar “reproducibilidad completa/total/absoluta”.

**HE2**
- estado formal: `SUPPORTED`;
- evidencia primaria: quince contrastes pareados histórico menos tres comparadores para Top-1, Top-3, Top-5, Top-10 y MRR@100, con remuestreo por conglomerados de DAM e IC bilaterales del 99 %; los contrastes primarios quedan por encima de cero;
- evidencia primaria profunda: diferencia Recall@200 − Recall@100 de la recuperación jerárquica con IC 95 % por encima de cero;
- no se calcularon valores p;
- Phase E/conjuntos candidatos profundos son evidencia descriptiva y no un segundo contraste confirmatorio;
- superioridad de recuperación histórica no equivale a exactitud global del framework RAG ni a corrección jurídica.

**HE3**
- estado formal: `SUPPORTED`;
- la integración histórico–normativa preserva el ranking histórico; la evidencia normativa documenta candidatos y no los reordena;
- el reranker LLM es exclusivamente diagnóstico;
- muestra diagnóstica: 20 casos; referencia en pool 19 y ausente 1; Top-1 antes/después 0,5000/0,5000; Top-3 0,6500/0,6500; Top-5 0,8000/0,8000; MRR 0,6326/0,6326; win/tie/loss = 0/19/0; clausura exacta 20/20;
- no presentar el LLM como mecanismo principal de ranking.

**HE4**
- estado formal: `PARTIALLY_SUPPORTED`;
- controles estructurales: Top-3/orden 50/50 y trazabilidad 50/50;
- evaluación cualitativa: 28/50 auditables y 22/50 no auditables; 0/50 violaciones graves;
- advertencia normativa genérica: 41/50 conforme y 9/50 faltante;
- evaluador cualitativo: IA independiente configurada bajo rol experto; no hubo puntuación humana;
- conservar las dos limitaciones sustantivas en español natural: diferencia entre el esquema previsto y el efectivamente evaluado; y diferencia entre la modalidad de evaluación ejecutada mediante IA y la revisión humana preparada originalmente;
- auditabilidad no equivale a clasificación correcta ni corrección jurídica.

**HE5**
- estado formal: `INCONCLUSIVE`;
- calidad descriptiva no operacionalizada prospectivamente y no estimable como prevalencia/concentración;
- proximidad jerárquica y soporte por precedentes son descriptivos, sin umbrales retrospectivos;
- soporte histórico se conserva en `1 DAM`, `2 DAM`, `3–4 DAM`, `5+ DAM`, sin etiquetar ningún grupo como “insuficiente”;
- benchmark interno/offline del Capítulo 87: 1 056 series, 67 DAM, 42 NANDINA; sin validación externa;
- sensibilidad tamaño/composición no causal y H150/H200 descriptiva sobre diez pares observados;
- diversidad cerrada sin recuperación y efecto no estimable.

No introduzcas valores p, nueva inferencia, nuevos intervalos, nuevos umbrales, nuevas métricas, causalidad, generalización externa ni nueva evidencia.

No muestres en el texto visible nuevo de la tesis IDs internos, nombres de archivos, blobs, commits, prompts, gates ni etiquetas de gobernanza. Traduce los estados a español natural.

---

# 3. Contrato REVIEW V03

En todo cambio visible de 121K:

- texto legacy sustituido = amarillo + tachado, visible, sin `w:del`;
- texto nuevo = amarillo, no tachado;
- texto no afectado = formato normal;
- conservar estructura, estilos, numeración y objetos existentes;
- edición mínima por fragmento/celda, no reconstrucción masiva de secciones o tablas.

No cambies las formulaciones literales aprobadas de las hipótesis; el objeto de 121K es actualizar la **contrastación**, no reescribir las hipótesis del Capítulo 3.

---

# 4. A053 — 4.2 Introducción a la contrastación

Modifica únicamente los párrafos introductorios de **4.2. Contrastación de hipótesis** necesarios para eliminar el mecanismo legacy uniforme y presentar la regla vigente.

La prosa activa debe expresar en español natural que:

1. la contrastación se interpreta según evidencia y disposición formal disponible para cada hipótesis;
2. no existe una regla uniforme que obligue a asignar `respaldada/parcialmente respaldada/no respaldada` a todas;
3. HE2 y HE3 cuentan con disposición formal de respaldo;
4. HE4 cuenta con disposición formal de respaldo parcial;
5. HE5 permanece inconclusa;
6. para HE1 y la hipótesis general no se localizó una disposición formal terminal y no se fabricará retrospectivamente;
7. la inferencia primaria se restringe a HE2 dentro del benchmark interno; el resto conserva su naturaleza descriptiva/diagnóstica cuando corresponda;
8. no se calcularon valores p y no se generaliza a una población externa.

Elimina del texto activo afirmaciones legacy de que todas las hipótesis reciben obligatoriamente uno de tres dictámenes uniformes, de que no se usaron intervalos de confianza, o de que HE2/HE3/HE5 siguen pendientes por reejecuciones ya cerradas.

---

# 5. A054 — 4.2.1 Contrastación de HE1

Actualiza mínimamente la subsección **4.2.1. Contrastación de HE1**.

Debe:

- conservar la formulación conceptual de HE1 como referencia;
- describir la evidencia auditada de integridad, jerarquía, procedencia, ausencia de solapamiento por DAM/id_unico, versionamiento y reconstrucción sustancial del procedimiento;
- reconocer las limitaciones documentadas de reproducibilidad: activos locales o restringidos, componentes históricos no recuperables, información incompleta de algunos entornos y ejecuciones IA/LLM no reproducibles byte a byte;
- declarar expresamente que **no se localizó una disposición formal terminal para HE1**;
- no concluir “HE1 quedó respaldada”, “rechazada”, “parcialmente respaldada” ni equivalente;
- no interpretar los cierres G2A/G2B como una decisión retrospectiva sobre HE1.

---

# 6. A055 — 4.2.2 Contrastación de HE2

Actualiza mínimamente **4.2.2. Contrastación de HE2**.

La prosa activa debe:

- indicar que `HE2 = respaldada` por la evidencia primaria congelada;
- sintetizar, sin copiar innecesariamente todas las tablas, que la recuperación histórica superó a los tres comparadores normativos corregidos en las cinco métricas primarias de ranking temprano;
- indicar que los quince IC pareados del 99 % quedaron por encima de cero;
- indicar que el contraste profundo Recall@200 − Recall@100 de la recuperación jerárquica, con IC 95 %, quedó por encima de cero;
- dejar claro que no se calcularon valores p;
- mantener Phase E/conjuntos candidatos profundos como descripción complementaria, no evidencia confirmatoria duplicada;
- restringir el resultado al benchmark interno de 1 056 series agrupadas en 67 DAM;
- prohibir la lectura de “superioridad de recuperación” como exactitud global del RAG, validez externa o corrección jurídica.

Elimina del texto activo cifras legacy de 1 006 casos, resultados pre-corrección y cualquier “respaldo provisional”.

---

# 7. A056 — 4.2.3 Contrastación de HE3

Actualiza mínimamente **4.2.3. Contrastación de HE3**.

La prosa activa debe:

- indicar que `HE3 = respaldada`;
- separar los dos componentes: integración histórico–normativa y reranker diagnóstico;
- afirmar que la integración añade trazabilidad sin modificar el ranking histórico;
- mantener la recuperación normativa como evidencia documental, no mecanismo de reranking;
- describir el reranker como diagnóstico sobre 20 casos, con ausencia de mejora agregada: Top-1, Top-3, Top-5 y MRR iguales antes/después; win/tie/loss 0/19/0 entre casos con referencia en el pool; un caso con referencia ausente;
- evitar cualquier afirmación de que el LLM mejora o reemplaza el ranking principal.

Elimina del texto activo la afirmación legacy de que la prueba del reranker “permanece provisional” o debe repetirse.

---

# 8. A057 — 4.2.4 Contrastación de HE4

Actualiza mínimamente **4.2.4. Contrastación de HE4**.

La prosa activa debe:

- indicar que `HE4 = parcialmente respaldada`;
- distinguir controles estructurales de evaluación cualitativa;
- reflejar que 50/50 fichas preservaron Top-3/orden y 50/50 mantuvieron trazabilidad;
- reflejar que 28/50 fueron auditables bajo la rúbrica cualitativa, 22/50 no auditables y hubo 0/50 violaciones graves;
- indicar que la evaluación cualitativa fue realizada por una IA independiente bajo rol experto y que no hubo puntuación humana;
- conservar las limitaciones por diferencia de esquema y modalidad de evaluador en español natural;
- no reutilizar el score legacy 0,9520 como dictamen actual ni mezclarlo con la evaluación cualitativa;
- no inferir corrección jurídica, validación humana o suficiencia normativa universal.

---

# 9. A058 — 4.2.5 Contrastación de HE5

Actualiza mínimamente **4.2.5. Contrastación de HE5**.

La prosa activa debe:

- indicar que `HE5 = inconclusa`;
- mantener la calidad descriptiva como no estimable por falta de operacionalización prospectiva;
- tratar proximidad jerárquica y soporte por precedentes como evidencia descriptiva sin umbrales prospectivos de concentración/insuficiencia;
- conservar el límite interno/offline del Capítulo 87 y ausencia de validación externa;
- mantener las sensibilidades bajo sus límites no causales/descriptivos;
- indicar que el análisis de diversidad quedó cerrado sin recuperación y su efecto no es estimable;
- dejar explícito que ausencia de estimabilidad no constituye evidencia positiva ni negativa para HE5.

Elimina del texto activo el dictamen legacy “parcialmente respaldada”, las categorías retrospectivas de bajo soporte y cualquier referencia a un análisis integrado futuro pendiente.

---

# 10. A059 — 4.2.6 Contrastación de la hipótesis general

Actualiza mínimamente **4.2.6. Contrastación de la hipótesis general**.

La prosa activa debe:

- conservar la formulación aprobada como referencia conceptual;
- sintetizar por componentes la evidencia vigente: ranking histórico, evidencia normativa, explicación controlada y límites de las hipótesis específicas;
- declarar expresamente que **no se localizó una disposición formal terminal para la hipótesis general**;
- no derivar un dictamen agregado por convergencia de HE1–HE5;
- no escribir que la hipótesis general quedó respaldada, parcialmente respaldada, rechazada o equivalente;
- mantener el alcance interno/offline y la diferencia entre auditabilidad documental y corrección jurídica.

---

# 11. A060 — Tabla 21 y nota inmediata

Mantén el mismo objeto **Tabla 21**, su numeración, cuatro columnas y seis filas de datos más encabezado. No crees una tabla nueva ni reemplaces el objeto completo.

Mantén el título visible existente salvo corrección mínima de estilo estrictamente necesaria:

```text
Contrastación de las hipótesis específicas y de la hipótesis general
```

Las seis filas deben presentar, en español natural y sin IDs internos, el siguiente estado científico:

| Hipótesis | Evidencia principal | Interpretación | Dictamen |
|---|---|---|---|
| HE1 | Controles de integridad, procedencia, trazabilidad y reproducibilidad con limitaciones documentadas | La evidencia metodológica permite reconstruir una parte sustancial del procedimiento, pero no constituye por sí misma una decisión terminal de HE1 | Sin disposición formal terminal |
| HE2 | Quince contrastes primarios pareados con IC 99 % favorables y un contraste profundo Recall@200 − Recall@100 con IC 95 % favorable; sin valores p | La recuperación histórica supera los comparadores normativos corregidos en ranking temprano y la jerárquica amplía cobertura profunda bajo el benchmark interno | Respaldada |
| HE3 | Integración sin alteración del ranking; reranker diagnóstico sin cambio agregado en la muestra observada | La evidencia normativa añade trazabilidad y el LLM no es necesario para modificar el ranking principal | Respaldada |
| HE4 | 50/50 preservación Top-3/orden y trazabilidad; 28/50 auditables cualitativamente; 0/50 violaciones graves | El cumplimiento estructural no equivale a calidad cualitativa universal ni corrección jurídica; modalidad cualitativa mediante IA independiente | Parcialmente respaldada |
| HE5 | Calidad descriptiva no estimable; jerarquía y soporte descriptivos; alcance interno; diversidad no estimable | La proposición de concentración no puede cerrarse con la evidencia disponible y no se crean umbrales post hoc | Inconclusa |
| Hipótesis general | Evidencia diferenciada de HE1–HE5 y de las funciones del ranking, evidencia y explicación | Los componentes se describen según sus disposiciones y límites; no existe base formal para derivar retrospectivamente un dictamen agregado | Sin disposición formal terminal |

Puedes ajustar redacción menor por anchura de celdas, sin cambiar el significado científico ni los estados.

La nota inmediata debe:

- explicar que las disposiciones provienen de fuentes formales diferenciadas;
- indicar que HE1 y la hipótesis general no reciben un dictamen retrospectivo;
- recordar que el alcance es el benchmark interno/offline del Capítulo 87;
- aclarar que auditabilidad documental no equivale a corrección jurídica.

Conserva `tblPr`, `tblGrid`, anchuras, bordes y estructura del objeto Tabla 21. Edita solo las celdas afectadas.

---

# 12. Comentarios Word

Conserva sin modificación los **203 comentarios heredados** y añade exactamente **8 comentarios nuevos**:

```text
A053 -> comment_id 454
A054 -> comment_id 455
A055 -> comment_id 456
A056 -> comment_id 457
A057 -> comment_id 458
A058 -> comment_id 459
A059 -> comment_id 460
A060 -> comment_id 461
```

Cada comentario nuevo debe contener, íntegramente en español:

```text
Cambio exacto:
Motivo del cambio:
Evidencia concreta:
Fuente gobernante:
Efecto en la tesis:
Límite de interpretación:
```

No modifiques contenido ni anclajes de comentarios heredados.

Resultado obligatorio:

```text
INHERITED_COMMENT_COUNT = 203
COMMENTS_ADDED = 8
TOTAL_COMMENT_COUNT = 211
ALL_COMMENT_IDS_ANCHORED = true
```

Cada nuevo comentario debe anclarse exclusivamente al cambio real correspondiente. A060 se ancla en Tabla 21/nota inmediata y no en secciones posteriores.

---

# 13. Trazabilidad

Conserva las **113 filas heredadas** como prefijo byte-idéntico y añade exactamente ocho filas:

```text
G7F02-V03K-001 / A053 / 4.2 introducción / comment_id 454
G7F02-V03K-002 / A054 / 4.2.1 HE1 / comment_id 455
G7F02-V03K-003 / A055 / 4.2.2 HE2 / comment_id 456
G7F02-V03K-004 / A056 / 4.2.3 HE3 / comment_id 457
G7F02-V03K-005 / A057 / 4.2.4 HE4 / comment_id 458
G7F02-V03K-006 / A058 / 4.2.5 HE5 / comment_id 459
G7F02-V03K-007 / A059 / 4.2.6 HG / comment_id 460
G7F02-V03K-008 / A060 / Tabla 21 + nota / comment_id 461
```

Resultado obligatorio:

```text
INHERITED_TRACE_ROWS = 113
NEW_TRACE_ROWS_ADDED = 8
TOTAL_TRACE_ROWS = 121
INHERITED_TRACE_PREFIX_BYTE_IDENTICAL = true
```

Usa las fuentes y blobs gobernantes de este prompt. Registra las disposiciones sin convertir HG/HE1 en supported/rejected y sin conservar estados legacy de HE2–HE5.

---

# 14. Invariantes de alcance

Verifica:

```text
TABLE_OBJECT_COUNT = 24
TABLE_21_OBJECT_PRESERVED = true
TABLE_21_ROW_COUNT = 7
TABLE_21_COLUMN_COUNT = 4
TABLE_21_TBLPR_UNCHANGED = true
TABLE_21_TBLGRID_UNCHANGED = true
TABLES_1_TO_20_UNCHANGED = true
TABLES_22_TO_24_UNCHANGED = true

SEQ_FIGURA_COUNT = 12
NEW_SEQ_FIGURE_FIELDS = 0
MEDIA_FILE_COUNT = 16
NEW_MEDIA_FILES = 0
FIGURES_1_TO_12_UNCHANGED = true

TRACKED_DELETION_COUNT = 0
4_1_8_UNCHANGED_FROM_J = true
4_3_AND_AFTER_OOXML_UNCHANGED_FROM_J = true
121L_EXECUTED = false
```

No modifiques 4.3, Tabla 22, Figura 11 ni ningún bloque posterior.

No modifiques la Lista de Tablas, la Lista de Figuras ni el índice por este bloque, salvo que una corrupción técnica obligue a detenerse; en ese caso usa `STOPPED_PRECONDITION`, no realices una reparación fuera de alcance.

---

# 15. QA visual y estructural

Renderiza el DOCX final y revisa desde el inicio de 4.2 hasta el comienzo de 4.3.

Verifica:

- redline fragmentario, no reconstrucción masiva de subsecciones;
- legacy sustituido visible con amarillo+tachado y texto vigente amarillo sin tachado;
- Tabla 21 legible, sin clipping, solapamiento ni desborde;
- cuatro columnas y seis filas de datos más encabezado;
- estados visibles correctos: HE1 sin disposición terminal; HE2 respaldada; HE3 respaldada; HE4 parcialmente respaldada; HE5 inconclusa; HG sin disposición terminal;
- no aparecen estados legacy activos contradictorios;
- 4.1.8 permanece intacta;
- 4.3 inicia intacta;
- los 211 comentarios están anclados;
- 12 `SEQ Figura`;
- 16 medios;
- 0 `w:del`;
- ningún ID interno prohibido visible en el texto nuevo;
- no existe contenido nuevo atribuible a A061 o posteriores.

---

# 16. Salidas

No sobrescribas J. Genera exclusivamente:

```text
Molleapasa_gv_G7F02_REVIEW_V03_K.docx
g7_thesis_claim_traceability_v0.3_K.csv
```

Publica respuesta oficial en:

```text
writing_prompts_tmp/121K_RESPUESTA_G7_F02_V03_BLOQUE_K_4_2_CONTRASTACION_HIPOTESIS.md
```

Reporta como mínimo:

```text
PROMPT121K_EXECUTION = COMPLETE | STOPPED_PRECONDITION
A053_APPLIED = true|false
A054_APPLIED = true|false
A055_APPLIED = true|false
A056_APPLIED = true|false
A057_APPLIED = true|false
A058_APPLIED = true|false
A059_APPLIED = true|false
A060_APPLIED = true|false
TABLE_21_UPDATED_IN_PLACE = true|false
TABLE_21_TBLPR_UNCHANGED = true|false
TABLE_21_TBLGRID_UNCHANGED = true|false
INHERITED_TRACE_ROWS = 113
NEW_TRACE_ROWS_ADDED = 8
TOTAL_TRACE_ROWS = 121
INHERITED_TRACE_PREFIX_BYTE_IDENTICAL = true|false
INHERITED_COMMENT_COUNT = 203
COMMENTS_ADDED = 8
TOTAL_COMMENT_COUNT = 211
ALL_COMMENT_IDS_ANCHORED = true|false
TRACKED_DELETION_COUNT = 0
4_1_8_UNCHANGED_FROM_J = true|false
4_3_AND_AFTER_UNCHANGED_FROM_J = true|false
OUT_OF_SCOPE_VISIBLE_MODIFICATIONS = 0
OUT_OF_SCOPE_COMMENT_MODIFICATIONS = 0
LOCAL_VISUAL_REVIEW = PASS|FAIL
121L_EXECUTED = false
EXTERNAL_AUDIT = PENDING_BY_IA_EXPERIMENTAL
```

Detente para auditoría externa. No ejecutes 4.3, A061, 121L ni ningún bloque posterior.