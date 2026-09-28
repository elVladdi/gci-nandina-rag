# PROMPT121K-R1 — Ejecutar G7-F02 REVIEW V03 — Bloque K: 4.2 contrastación de hipótesis

## 0. Estado de este prompt y actor

Este prompt **supersede para ejecución** a:

```text
writing_prompts_tmp/121K_EJECUTAR_G7_F02_V03_BLOQUE_K_4_2_CONTRASTACION_HIPOTESIS.md
commit = 5f60b8bf116b5d638ad65b69e4d603a61e40e072
blob = 8ab3752976f68bf8e4c7331d4e4fa82d36b8d7c7
status = NO_EJECUTAR / SUPERSEDED_BY_121K_R1
```

No borres ni reescribas el prompt histórico anterior.

Actúa como **IA de Redacción Científica** del proyecto `elVladdi/gci-nandina-rag`.

No eres CODEX. No eres la IA Experimental. No recalcules métricas, no generes nueva inferencia, no hagas búsqueda web, no agregues referencias bibliográficas y no ejecutes 4.3 ni ningún bloque posterior.

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

Lee íntegramente y aplica además, como contratos heredados:

```text
writing_prompts_tmp/119_RESPUESTA_CORREGIR_PLAN_G7_F02_ANTES_DE_V03.md
GIT_BLOB = 5472f7183618ed1a806220c8ee679ab186b7bc79

writing_prompts_tmp/120_EJECUTAR_G7_F02_REVIEW_V03_DESDE_BASELINE.md
GIT_BLOB = 80a2a3d7fbf88f1a7868bdf350d8ef85b0ad37bd

docs/writing/group7/g7_writing_source_freeze_v0.1.json
GIT_BLOB = 776fcb52e8ada9967504001b897c75b4108bfb63

docs/writing/group7/g7_writing_source_freeze_v0.1.md
GIT_BLOB = feea31e2a45ee5f3d9b8fa1f9a1e1bdc073d6430
```

Si existe contradicción material entre este prompt, Prompt119, Prompt120 o una fuente científica gobernante, usa `STOPPED_PRECONDITION` y reporta el conflicto. No improvises.

Ejecuta exclusivamente **A053–A060** del plan aprobado.

No ejecutes A061, A073–A082, 4.3, 121L ni ningún bloque posterior.

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
TRACKED_INSERTION_COUNT = 0
```

Verifica además antes de editar:

```text
TABLE_21_ROW_COUNT = 7
TABLE_21_COLUMN_COUNT = 4
TABLE_21_HEADER = Hipótesis | Evidencia principal | Interpretación | Dictamen
SECTION_4_2_PRESENT = true
SECTION_4_3_PRESENT = true
```

Si cualquiera de estas precondiciones estructurales falla, detente.

---

## 2. Jerarquía y fuentes científicas gobernantes

Mantén la jerarquía de fuentes de G7-F01 / Prompt120:

1. proyecto aprobado → formulaciones de problema, objetivos e hipótesis;
2. artefactos experimentales congelados → métodos y resultados;
3. G3 → inferencia, poblaciones, HE2 y HE5;
4. Group1/Group2 congelados → HE3, HE4, reproducibilidad y ausencia formal de HE1;
5. G4 → fuerza de claims, interpretación y limitaciones;
6. G5 → cifras/tablas canónicas;
7. G6 → figuras/captions aprobados;
8. baseline/J → contrato editorial y acumulativo, no verdad científica cuando esté superseded.

Lee y verifica las siguientes fuentes antes de redactar:

```text
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

outputs/audits/group2b_reproducibility_readiness_v0.2.json
GIT_BLOB = 802f85bf44922ca2dbeb395042908d5bd2efc133

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

outputs/analysis/group4/g4_result_claim_evidence_matrix_v0.1.json
GIT_BLOB = cc5d85bad5d0a2610ffb086f99052fd344b6d8ab

outputs/analysis/group4/g4_limitations_registry_v0.1.json
GIT_BLOB = ae00b93431e912cb78a58344057d9bf7a51fcd47

docs/analysis/group4/g4_interpretation_synthesis_v0.1.md
GIT_BLOB = 129a67b15db429b86af059d61753b1942c8f243f
```

No uses fuentes externas a este freeze. No agregues citas o referencias nuevas.

### 2.1 Disposiciones vinculantes

```text
HG = NO_FORMAL_DISPOSITION_FOUND
HE1 = NO_FORMAL_DISPOSITION_FOUND
HE2 = SUPPORTED
HE3 = SUPPORTED
HE4 = PARTIALLY_SUPPORTED
HE5 = INCONCLUSIVE
```

No derives nuevas disposiciones ni conviertas evidencia metodológica en una decisión inexistente.

### 2.2 Reglas por hipótesis

**HG**
- no existe disposición formal terminal localizada;
- no declarar respaldada, rechazada, parcialmente respaldada ni equivalente;
- describir evidencia de componentes por separado;
- no derivar un dictamen agregado desde HE1–HE5.

**HE1**
- no existe disposición formal terminal localizada;
- integridad, procedencia, trazabilidad y reproducibilidad son evidencia metodológica con limitaciones;
- no convertir G2A/G2B en decisión post hoc de HE1;
- no usar “reproducibilidad completa”, “total” o “absoluta”.

**HE2**
- estado formal: `SUPPORTED`;
- quince contrastes pareados histórico menos tres comparadores para Top-1, Top-3, Top-5, Top-10 y MRR@100, con remuestreo por conglomerados DAM e IC bilaterales del 99 %, todos con límite inferior mayor que cero;
- contraste profundo Recall@200 − Recall@100 de recuperación jerárquica con IC 95 % por encima de cero;
- no se calcularon valores p;
- la evidencia de conjuntos candidatos profundos es descriptiva y no un segundo contraste confirmatorio;
- superioridad de recuperación histórica no equivale a exactitud global del RAG ni corrección jurídica.

**HE3**
- estado formal: `SUPPORTED`;
- integración histórico–normativa preserva ranking histórico; evidencia normativa documenta candidatos y no los reordena;
- reranker LLM exclusivamente diagnóstico;
- muestra diagnóstica: 20 casos; referencia en pool 19, ausente 1; Top-1 0,5000/0,5000; Top-3 0,6500/0,6500; Top-5 0,8000/0,8000; MRR 0,6326/0,6326; win/tie/loss 0/19/0; clausura 20/20;
- no presentar LLM como mecanismo principal de ranking.

**HE4**
- estado formal: `PARTIALLY_SUPPORTED`;
- Top-3/orden 50/50 y trazabilidad 50/50;
- 28/50 auditables y 22/50 no auditables; 0/50 violaciones graves;
- advertencia normativa genérica conforme 41/50, faltante 9/50;
- evaluación cualitativa mediante IA independiente bajo rol experto; no hubo puntuación humana;
- conservar en español natural las limitaciones por diferencia entre esquema previsto/efectivamente evaluado y modalidad IA/revisión humana originalmente preparada;
- auditabilidad no equivale a clasificación correcta ni corrección jurídica.

**HE5**
- estado formal: `INCONCLUSIVE`;
- calidad descriptiva no operacionalizada prospectivamente y no estimable como prevalencia/concentración;
- proximidad jerárquica y soporte por precedentes descriptivos, sin umbrales retrospectivos;
- grupos de soporte: 1 DAM, 2 DAM, 3–4 DAM, 5+ DAM, sin etiquetar retrospectivamente ninguno como insuficiente;
- benchmark interno/offline Capítulo 87: 1 056 series, 67 DAM, 42 NANDINA; sin validación externa;
- sensibilidad tamaño/composición no causal; H150/H200 descriptiva sobre diez pares observados;
- diversidad cerrada sin recuperación y efecto no estimable.

No introduzcas nuevas métricas, nuevos intervalos, valores p, nuevos umbrales, nueva inferencia, nuevas hipótesis, nuevos resultados, causalidad, generalización externa, nueva evidencia ni nuevas referencias.

---

## 3. Contrato editorial REVIEW V03

Preserva el Word acumulativo como el mismo documento corregido localmente; no lo reconstruyas.

```text
REDESIGN = PROHIBITED
REBUILD_DOCX_FROM_SCRATCH = PROHIBITED
NEW_CUSTOM_STYLES = 0
NEW_REFERENCES = 0
```

Preserva estructura, estilos Word, márgenes, secciones, encabezados/pies, numeración de páginas, formato de párrafos, anchos y propiedades de tablas, captions, tipografías, tamaños, interlineado, sangrías, elementos institucionales, bibliografía existente e índice.

Todo texto nuevo debe heredar el estilo del párrafo/celda equivalente.

En todo cambio visible de 121K-R1:

- texto legacy sustituido = amarillo + tachado, visible;
- texto nuevo = amarillo, no tachado;
- texto no afectado = normal;
- `w:del = 0`;
- `w:ins = 0`;
- edición mínima por fragmento/celda; no reconstrucción masiva.

No cambies formulaciones literales aprobadas de las hipótesis en Capítulo 3.

No muestres en el texto visible nuevo identificadores o lenguaje interno tales como `G1–G8`, `Group1`, `Gx-Fxx`, `Prompt...`, `PREF...`, `source freeze`, `claim registry`, IDs de claims, `Attempt06`, `Phase E`, nombres de archivos, paths, blobs, commits, gates, `CLOSED/APPROVED`, `PROMPT_SCHEMA_SPECIFICATION_MISMATCH`, `EVALUATOR_MODALITY_DEVIATION`, `AI_EXPERT_ROLE` o identificadores de evaluador. Traduce a español académico natural.

Los IDs/path técnicos pueden aparecer solo en comentarios Word y CSV de trazabilidad.

---

## 4. Regla especial de A081 diferido

Existe una corrección editorial futura, **A081**, en la introducción de 4.2: `Tabla 10` → `Tabla 9`.

A081 **no está autorizada en 121K-R1**.

- no realices esa sustitución como cambio independiente;
- si la referencia `Tabla 10` permanece en texto activo tras A053, déjala intacta para A081;
- si la oración completa desaparece naturalmente por la sustitución mínima autorizada de A053, no reintroduzcas una referencia nueva y no generes comentario/traza A081;
- no ejecutes ninguna otra corrección A073–A082.

---

## 5. A053 — 4.2 Introducción a la contrastación

Modifica únicamente los párrafos introductorios de **4.2. Contrastación de hipótesis** necesarios para eliminar el mecanismo legacy uniforme y presentar la regla vigente.

La prosa activa debe expresar en español natural que:

1. la contrastación se interpreta según evidencia y disposición formal disponible para cada hipótesis;
2. no existe una regla uniforme que obligue a asignar respaldada/parcialmente respaldada/no respaldada a todas;
3. HE2 y HE3 cuentan con disposición formal de respaldo;
4. HE4 cuenta con disposición formal de respaldo parcial;
5. HE5 permanece inconclusa;
6. para HE1 y HG no se localizó disposición formal terminal y no se fabricará retrospectivamente;
7. la inferencia primaria se restringe a HE2 dentro del benchmark interno; el resto conserva naturaleza descriptiva/diagnóstica cuando corresponda;
8. no se calcularon valores p y no se generaliza a población externa.

Elimina de la presentación activa el mecanismo decisional uniforme, la afirmación de que no se usaron intervalos de confianza y estados pendientes ya cerrados.

---

## 6. A054 — 4.2.1 Contrastación de HE1

Actualiza mínimamente **4.2.1**.

Debe:

- conservar la formulación conceptual de HE1 como referencia;
- describir evidencia auditada de integridad, jerarquía, procedencia, ausencia de solapamiento por DAM/id_unico, versionamiento y reconstrucción sustancial bajo condiciones documentadas;
- reconocer limitaciones documentadas de reproducibilidad: activos locales/restringidos, componentes históricos no recuperables, información incompleta de algunos entornos y ejecuciones IA/LLM no reproducibles byte a byte cuando las fuentes lo documenten;
- declarar que no se localizó disposición formal terminal para HE1;
- no concluir respaldada/rechazada/parcialmente respaldada;
- no convertir cierres G2A/G2B en una decisión retrospectiva.

No uses lenguaje más fuerte que las limitaciones explícitamente documentadas en las fuentes.

---

## 7. A055 — 4.2.2 Contrastación de HE2

Actualiza mínimamente **4.2.2**.

La prosa activa debe:

- indicar que HE2 quedó respaldada por la evidencia primaria congelada;
- sintetizar que la recuperación histórica superó a los tres comparadores normativos corregidos en cinco métricas primarias de ranking temprano;
- indicar que los quince IC pareados del 99 % quedaron por encima de cero;
- indicar que Recall@200 − Recall@100 de recuperación jerárquica, con IC 95 %, quedó por encima de cero;
- dejar claro que no se calcularon valores p;
- presentar los conjuntos candidatos profundos como evidencia descriptiva complementaria, sin usar la etiqueta interna `Phase E` en texto visible;
- restringir el resultado a 1 056 series / 67 DAM del benchmark interno;
- prohibir lectura como exactitud global RAG, validez externa o corrección jurídica.

Elimina cifras legacy de 1 006 casos, resultados pre-corrección y “respaldo provisional”.

---

## 8. A056 — 4.2.3 Contrastación de HE3

Actualiza mínimamente **4.2.3**.

La prosa activa debe:

- indicar HE3 respaldada;
- separar integración histórico–normativa y reranker diagnóstico;
- afirmar que la integración añade trazabilidad sin modificar ranking histórico;
- mantener recuperación normativa como evidencia documental, no reranking;
- describir el reranker sobre 20 casos, sin mejora agregada: Top-1, Top-3, Top-5 y MRR iguales antes/después; win/tie/loss 0/19/0 entre casos con referencia en pool; un caso con referencia ausente;
- evitar cualquier afirmación de mejora o reemplazo del ranking principal.

Elimina la afirmación legacy de prueba provisional o pendiente de repetición.

---

## 9. A057 — 4.2.4 Contrastación de HE4

Actualiza mínimamente **4.2.4**.

La prosa activa debe:

- indicar HE4 parcialmente respaldada;
- distinguir controles estructurales de evaluación cualitativa;
- reflejar 50/50 preservación Top-3/orden y 50/50 trazabilidad;
- reflejar 28/50 auditables, 22/50 no auditables y 0/50 violaciones graves;
- indicar evaluación cualitativa mediante IA independiente bajo rol experto, sin puntuación humana, en español natural;
- conservar limitaciones por diferencia de esquema y modalidad de evaluador en español natural;
- no reutilizar score legacy 0,9520;
- no inferir corrección jurídica, validación humana ni suficiencia normativa universal.

---

## 10. A058 — 4.2.5 Contrastación de HE5

Actualiza mínimamente **4.2.5**.

La prosa activa debe:

- indicar HE5 inconclusa;
- mantener calidad descriptiva no estimable por falta de operacionalización prospectiva;
- tratar proximidad jerárquica y soporte por precedentes como evidencia descriptiva sin umbrales retrospectivos;
- conservar alcance interno/offline Capítulo 87 y ausencia de validación externa;
- mantener sensibilidades bajo límites no causales/descriptivos;
- indicar que diversidad quedó cerrada sin recuperación y su efecto no es estimable;
- explicitar que ausencia de estimabilidad no es evidencia positiva ni negativa.

Elimina dictamen legacy “parcialmente respaldada”, categorías retrospectivas de bajo soporte y referencia a análisis futuro pendiente.

---

## 11. A059 — 4.2.6 Contrastación de la hipótesis general

Actualiza mínimamente **4.2.6**.

La prosa activa debe:

- conservar formulación aprobada como referencia conceptual;
- sintetizar por componentes ranking histórico, evidencia normativa, explicación controlada y límites de hipótesis específicas;
- declarar que no se localizó disposición formal terminal para HG;
- no derivar dictamen agregado por convergencia HE1–HE5;
- no escribir que HG quedó respaldada, parcialmente respaldada, rechazada o equivalente;
- mantener alcance interno/offline y diferencia entre auditabilidad documental y corrección jurídica.

---

## 12. A060 — Tabla 21 y nota inmediata

Mantén el mismo objeto **Tabla 21**, su numeración, cuatro columnas y seis filas de datos más encabezado. No crees tabla nueva ni reemplaces el objeto completo.

Conserva el título visible salvo corrección mínima estrictamente necesaria:

```text
Contrastación de las hipótesis específicas y de la hipótesis general
```

Las seis filas deben presentar, en español natural y sin IDs internos:

| Hipótesis | Evidencia principal | Interpretación | Dictamen |
|---|---|---|---|
| HE1 | Controles de integridad, procedencia, trazabilidad y reproducibilidad con limitaciones documentadas | La evidencia metodológica permite reconstruir una parte sustancial del procedimiento, pero no constituye por sí misma una decisión terminal de HE1 | Sin disposición formal terminal |
| HE2 | Quince contrastes primarios pareados con IC 99 % favorables y un contraste profundo Recall@200 − Recall@100 con IC 95 % favorable; sin valores p | La recuperación histórica supera los comparadores normativos corregidos en ranking temprano y la jerárquica amplía cobertura profunda bajo el benchmark interno | Respaldada |
| HE3 | Integración sin alteración del ranking; reranker diagnóstico sin cambio agregado en la muestra observada | La evidencia normativa añade trazabilidad y el LLM no es necesario para modificar el ranking principal | Respaldada |
| HE4 | 50/50 preservación Top-3/orden y trazabilidad; 28/50 auditables cualitativamente; 0/50 violaciones graves | El cumplimiento estructural no equivale a calidad cualitativa universal ni corrección jurídica; modalidad cualitativa mediante IA independiente | Parcialmente respaldada |
| HE5 | Calidad descriptiva no estimable; jerarquía y soporte descriptivos; alcance interno; diversidad no estimable | La proposición de concentración no puede cerrarse con la evidencia disponible y no se crean umbrales post hoc | Inconclusa |
| Hipótesis general | Evidencia diferenciada de HE1–HE5 y de las funciones del ranking, evidencia y explicación | Los componentes se describen según sus disposiciones y límites; no existe base formal para derivar retrospectivamente un dictamen agregado | Sin disposición formal terminal |

Puedes ajustar redacción menor por anchura sin cambiar significado ni estados.

La nota inmediata debe:

- explicar que las disposiciones provienen de fuentes formales diferenciadas;
- indicar que HE1 y HG no reciben dictamen retrospectivo;
- recordar alcance interno/offline Capítulo 87;
- aclarar que auditabilidad documental no equivale a corrección jurídica.

Conserva `tblPr`, `tblGrid`, anchos, bordes y estructura. Edita solo celdas afectadas.

---

## 13. Comentarios Word

Conserva sin modificación los **203 comentarios heredados** y añade exactamente **8 comentarios nuevos**, uno por plan_id:

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

Cada comentario debe contener íntegramente en español:

```text
Cambio exacto:
Motivo del cambio:
Evidencia concreta:
Fuente gobernante:
Efecto en la tesis:
Límite de interpretación:
```

Requisitos:

- cambio exacto: identificar frase/estado/celda legacy y vigente cuando sea razonable;
- motivo: defecto específico, no “legacy” como explicación autónoma;
- evidencia concreta: cifras/población/limitación cuando corresponda;
- fuente gobernante: nombre comprensible y, opcionalmente, path/blob;
- efecto: incoherencia corregida;
- límite: conclusión no autorizada.

No modifiques contenido ni anclajes heredados. Cada comentario nuevo debe anclarse al cambio real de su plan_id. A060 se ancla dentro de Tabla 21 en una región modificada; su texto debe explicar también la actualización de la nota inmediata.

Resultado obligatorio:

```text
INHERITED_COMMENT_COUNT = 203
COMMENTS_ADDED = 8
TOTAL_COMMENT_COUNT = 211
ALL_COMMENT_IDS_ANCHORED = true
```

---

## 14. Trazabilidad

Conserva las **113 filas heredadas como prefijo byte-idéntico**. El prefijo K correspondiente a J debe conservar:

```text
INHERITED_TRACE_PREFIX_SIZE = 106581
INHERITED_TRACE_PREFIX_SHA256 = 953a62856cc4819df2c3c9e7511c79e08b78a8073fa2adec1bbcb578e704ca0c
```

Añade exactamente ocho filas:

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

Usa fuentes/blobs gobernantes. No conviertas HG/HE1 en supported/rejected ni conserves estados legacy HE2–HE5.

---

## 15. Invariantes de alcance

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
TRACKED_INSERTION_COUNT = 0
4_1_8_UNCHANGED_FROM_J = true
4_3_AND_AFTER_OOXML_UNCHANGED_FROM_J = true
OUT_OF_SCOPE_VISIBLE_MODIFICATIONS = 0
OUT_OF_SCOPE_COMMENT_MODIFICATIONS = 0
A061_EXECUTED = false
A073_TO_A082_EXECUTED = false
121L_EXECUTED = false
```

No modifiques 4.3, Tabla 22, Figura 11, listas de tablas/figuras, índice ni bloques posteriores. Si detectas corrupción técnica fuera de alcance, detente; no la repares aquí.

---

## 16. QA visual y estructural

Renderiza **el DOCX final completo**. Haz una revisión global de paginación/continuidad y una revisión focal a resolución de página desde el inicio de 4.2 hasta el comienzo de 4.3.

Verifica:

- no hay clipping, solapamientos, desbordes, saltos anómalos ni corrupción visual global;
- redline fragmentario, no reconstrucción masiva;
- legacy sustituido amarillo+tachado y vigente amarillo sin tachado;
- Tabla 21 legible, 4 columnas + 6 filas de datos, sin clipping/desborde;
- estados visibles correctos: HE1 sin disposición terminal; HE2 respaldada; HE3 respaldada; HE4 parcialmente respaldada; HE5 inconclusa; HG sin disposición terminal;
- no aparecen estados legacy activos contradictorios;
- 4.1.8 permanece intacta;
- 4.3 inicia intacta;
- 211 comentarios anclados;
- 12 `SEQ Figura`;
- 16 medios;
- 0 `w:del` y 0 `w:ins`;
- ningún identificador interno prohibido visible en texto nuevo;
- no existe contenido nuevo atribuible a A061 o posteriores.

---

## 17. Salidas y reporte obligatorio

No sobrescribas J. Genera exclusivamente:

```text
Molleapasa_gv_G7F02_REVIEW_V03_K.docx
g7_thesis_claim_traceability_v0.3_K.csv
```

Calcula y reporta obligatoriamente para ambos artefactos:

```text
OUTPUT_DOCX_SHA256 = <sha256>
OUTPUT_DOCX_SIZE_BYTES = <bytes>
OUTPUT_CSV_SHA256 = <sha256>
OUTPUT_CSV_SIZE_BYTES = <bytes>
OUTPUT_CSV_ROWS = 121
```

Publica respuesta oficial en:

```text
writing_prompts_tmp/121K_RESPUESTA_G7_F02_V03_BLOQUE_K_4_2_CONTRASTACION_HIPOTESIS.md
```

La respuesta debe incluir, como mínimo:

```text
PROMPT121K_EXECUTION = COMPLETE | STOPPED_PRECONDITION
SOURCE_PROMPT = 121K_R1
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
INHERITED_TRACE_PREFIX_SIZE = 106581
INHERITED_TRACE_PREFIX_SHA256 = 953a62856cc4819df2c3c9e7511c79e08b78a8073fa2adec1bbcb578e704ca0c
INHERITED_TRACE_PREFIX_BYTE_IDENTICAL = true|false
INHERITED_COMMENT_COUNT = 203
COMMENTS_ADDED = 8
TOTAL_COMMENT_COUNT = 211
ALL_COMMENT_IDS_ANCHORED = true|false
TABLE_OBJECT_COUNT = 24
SEQ_FIGURA_COUNT = 12
MEDIA_FILE_COUNT = 16
NEW_SEQ_FIGURE_FIELDS = 0
NEW_MEDIA_FILES = 0
TRACKED_DELETION_COUNT = 0
TRACKED_INSERTION_COUNT = 0
4_1_8_UNCHANGED_FROM_J = true|false
4_3_AND_AFTER_OOXML_UNCHANGED_FROM_J = true|false
OUT_OF_SCOPE_VISIBLE_MODIFICATIONS = 0
OUT_OF_SCOPE_COMMENT_MODIFICATIONS = 0
A061_EXECUTED = false
A073_TO_A082_EXECUTED = false
LOCAL_VISUAL_REVIEW = PASS|FAIL
OUTPUT_DOCX_SHA256 = <sha256>
OUTPUT_DOCX_SIZE_BYTES = <bytes>
OUTPUT_CSV_SHA256 = <sha256>
OUTPUT_CSV_SIZE_BYTES = <bytes>
OUTPUT_CSV_ROWS = 121
121L_EXECUTED = false
EXTERNAL_AUDIT = PENDING_BY_IA_EXPERIMENTAL
```

Detente para auditoría externa. No ejecutes 4.3, A061, A073–A082, 121L ni ningún bloque posterior.
