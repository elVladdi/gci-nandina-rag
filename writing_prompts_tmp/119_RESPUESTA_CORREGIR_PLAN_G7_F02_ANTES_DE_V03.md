# PROMPT119 — Respuesta de corrección del plan G7-F02 antes de V03

```text
PROMPT119_EXECUTION = COMPLETE
ACTOR = IA_DE_REDACCION_CIENTIFICA
SOURCE_PROMPT = writing_prompts_tmp/119_CORREGIR_PLAN_G7_F02_ANTES_DE_V03.md
SOURCE_PROMPT_COMMIT = 0148a2b83567636934fb3c7bf00a8514f2810bbf
PROMPT118_EXTERNAL_AUDIT = REVISION_REQUIRED
AUTHOR_REJECTION_OF_V01_V02 = ACKNOWLEDGED
REWRITE_BASE = ORIGINAL_BASELINE_ONLY
BASELINE_FILENAME = Molleapasa_gv_vigente_2026-09-22.docx
BASELINE_SHA256 = 08b48ec1687ae0a0d943724bf2d682aca02d2a9f5a124b3dc35270e041bc3aed
BASELINE_SIZE_BYTES = 4360620
WORD_MODIFIED = false
V03_CREATED = false
TABLE_CROSS_REFERENCE_AUDIT = PASS
FIGURE_CROSS_REFERENCE_AUDIT = PASS
COMMENT_POLICY_CORRECTED = true
REPRODUCIBILITY_WORDING_CORRECTED = true
REVIEW_V03_FIGURE_NUMBERING = PRESERVE_BASELINE_1_TO_12
PRESENTATION_MODE_AUDIT = PASS
NEW_SCIENTIFIC_CLAIMS = 0
NEW_METRICS = 0
NEW_INFERENCE = 0
NEW_P_VALUES = 0
NEW_CI = 0
NEW_REFERENCES = 0
PLAN_READY_FOR_EXTERNAL_AUDIT = true
G7_F02 = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
G7_F03_AUTHORIZED = false
GROUP7_CLOSED = false
EXTERNAL_AUDIT = PENDING_BY_IA_EXPERIMENTAL
```

## 1. Criterio rector corregido

La futura V03 se construirá exclusivamente desde el baseline original `Molleapasa_gv_vigente_2026-09-22.docx`. V01 y V02 permanecen rechazadas por el autor y no se utilizarán como fuente de redacción, formato, numeración, estructura ni contenido científico.

El baseline gobierna el estilo y la organización editorial. Las fuentes científicas aprobadas gobiernan método, resultados y límites cuando el baseline haya quedado desactualizado. La edición futura será mínima: primero fragmento, luego celda, luego fila; solo se alterará una estructura completa cuando sea imposible conservarla sin distorsionar su semántica.

La revisión de Prompt119 incorpora cinco correcciones vinculantes: auditoría completa de referencias cruzadas; comentarios únicamente para cambios reales; eliminación de cualquier formulación de “reproducibilidad completa”; preservación de la numeración de Figuras 1–12 durante V03; y decisión explícita de prosa frente a tabla/figura para los bloques complejos.

---

# 2. MATRIZ A — Mapa de intervención por sección corregido

| plan_id | baseline_section | baseline_locator | baseline_content_summary | scientific_issue | proposed_action | presentation_mode | minimal_edit_scope | scientific_source | human_readable_reason | internal_labels_to_translate_or_remove | requires_comment | comment_detail_summary |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| A001 | 1.1–1.4 | Situación problemática, problemas y objetivos | Planteamiento y formulaciones aprobadas | Compatible con el alcance actual | KEEP | PARAGRAPH | NONE | Proyecto aprobado + límites interpretativos vigentes | Las formulaciones aprobadas no se reescriben por cambios experimentales posteriores | Etiquetas internas si aparecieran | NO | No hay cambio visible; solo verificación de conservación |
| A002 | Capítulo II | Marco teórico | Antecedentes y base conceptual | No debe actualizarse por arrastre de resultados ni recibir bibliografía nueva | TERMINOLOGY_ONLY | PARAGRAPH | Solo términos que contradigan guardrails, si se identifican | Contraste bibliográfico y límites aprobados | Mantener estructura y referencias; corregir únicamente atribuciones incompatibles con el rol del LLM o la corrección jurídica | IDs internos | YES_IF_CHANGED | Si se materializa un ajuste, comentar el término exacto, motivo y límite sin introducir referencia nueva |
| A003 | 3.1.1 | Hipótesis general | Formulación HG aprobada | No existe disposición formal terminal | KEEP | PARAGRAPH | NONE | Proyecto aprobado | La formulación no cambia por ausencia de decisión terminal | `NO_FORMAL_DISPOSITION_FOUND` y códigos internos | NO | No hay cambio visible en la formulación |
| A004 | 3.1.2 | HE1–HE5 | Formulaciones literales aprobadas | Cambian evidencias/disposiciones, no el texto de hipótesis | KEEP | PARAGRAPH | NONE | Proyecto aprobado | Preservar literalmente las hipótesis | IDs internos | NO | No hay cambio visible en las formulaciones |
| A005 | 3.1.3 | Identificación de variables | VI, VD y métricas generales | Debe reflejar SERIE y dependencia DAM cuando corresponda | INLINE_REPLACE | PARAGRAPH | Frases de unidad/dependencia/métricas | Contrato analítico vigente | Actualización localizada sin rediseñar variables | IDs Gx/Fxx/claims | YES | Precisar frase anterior, frase nueva y uso de SERIE/DAM |
| A006 | 3.1.4 / Tabla 1 | Operacionalización de variables | Indicadores y técnicas | Semántica legacy de auditabilidad y roles analíticos | TABLE_CELL_UPDATE | EXISTING_TABLE_CELL_UPDATE | Solo celdas afectadas | Contrato analítico + evaluación HE4 | Corregir indicadores/técnicas sin reconstruir tabla | Scores/códigos internos | YES | Identificar cada celda y evidencia concreta que exige el cambio |
| A007 | 3.1.5 / Tabla 2 | Matriz de consistencia | Problema–objetivo–hipótesis–variables | Técnicas/indicadores requieren sincronización mínima | TABLE_CELL_UPDATE | EXISTING_TABLE_CELL_UPDATE | Solo celdas técnicas/indicadores | Proyecto aprobado + contrato analítico | Mantener formulaciones aprobadas intactas | IDs internos | YES | Explicar que solo cambia operacionalización, no problema/objetivo/hipótesis |
| A008 | 3.2.1 | Tipo de investigación | Piloto aplicado y offline | Debe mantener alcance interno | TERMINOLOGY_ONLY | PARAGRAPH | Frase puntual de alcance si corresponde | Síntesis interpretativa | Evitar generalización externa | IDs internos | YES_IF_CHANGED | Comentar únicamente si se modifica una frase concreta |
| A009 | 3.2.2 | Diseño de investigación | Diseño experimental | Falta procedimiento inferencial realmente ejecutado para HE2 | PARAGRAPH_REWRITE_MINIMAL | PARAGRAPH | Párrafo metodológico específico | Métodos inferenciales vigentes | Incorporar bootstrap pareado por DAM, CI 99/95 y ausencia de p-values sin reescribir toda la sección | IDs de fichas/resultados | YES | Evidencia concreta: 10 000 remuestras DAM, 15 contrastes 99%, 1 contraste 95% |
| A010 | 3.2.3 | Variables de control | Controles del piloto | Debe reflejar separación DAM-disjoint | INLINE_REPLACE | PARAGRAPH | Fragmentos de partición/dependencia | Split v0.2 + contrato analítico | Alinear control de dependencia con benchmark final | Gate/commit/versiones internas | YES | Explicar la regla DAM-disjoint y su efecto sobre fuga entre declaraciones |
| A011 | 3.2.4 | Arquitectura funcional | Ranking histórico, evidencia normativa, Top-3 y explicación | Sustancialmente vigente | KEEP | PARAGRAPH | NONE | Síntesis interpretativa | No rediseñar sección conceptualmente correcta | G1–G8 y equivalentes | NO | No hay cambio visible; la corrección de referencia a Tabla 3 se registra aparte |
| A012 | 3.2.4 / Tabla 3 | Correspondencia fases RAG–operaciones | Matriz funcional | Compatible con arquitectura vigente | KEEP | EXISTING_TABLE_ROW_UPDATE | NONE | Síntesis interpretativa | Conservar tabla y numeración | IDs internos | NO | No se modifica la tabla; solo la referencia previa se corrige en A073 |
| A013 | 3.2.4 / Figura 2 | Arquitectura funcional | Diagrama conceptual | Compatible | KEEP | FIGURE | NONE | Síntesis interpretativa | No reemplazar una figura válida por existencia de gráficos de resultados | IDs internos | NO | No hay cambio visible previsto |
| A014 | 3.3 | Unidad de análisis | SERIE | Falta declarar DAM/DECLARACIÓN como dependencia cuando aplica | INLINE_REPLACE | PARAGRAPH | Una frase | Contrato analítico | Completar dependencia sin alterar unidad principal | IDs internos | YES | Añadir DAM como grupo de dependencia y explicar dónde se usa |
| A015 | 3.4 | Población | Universo fuente y clase 87 | Debe distinguir universo fuente de benchmark final | INLINE_REPLACE | PARAGRAPH | Frases con cantidades finales legacy | Contrato analítico + split v0.2 | Preservar contexto fuente y actualizar solo conjunto final | Labels internos | YES | Aclarar H100/DEV/EVAL vigentes y límite interno |
| A016 | 3.5 | Tamaño de muestra | 3 000/100/1 006 y ausencia de inferencia | Split obsoleto y afirmación inferencial incorrecta | PARAGRAPH_REWRITE_MINIMAL | PARAGRAPH | Párrafos de tamaños y criterio analítico | Contrato analítico + métodos inferenciales | Actualizar a 2 950/100/1 056 y separar muestreo no probabilístico de inferencia interna | IDs internos | YES | Cifras exactas y explicación del bootstrap DAM dentro del benchmark fijo |
| A017 | 3.5 / Tabla 4 | Tamaño y función de conjuntos | H, DEV, EVAL | Valores legacy | TABLE_CELL_UPDATE | EXISTING_TABLE_CELL_UPDATE | Celdas de tamaño/DAM/NANDINA/función | Contrato analítico | Estructura válida; solo cambian valores/descriptores | IDs internos | YES | Marcar celdas exactas 3 000→2 950 y 1 006→1 056, con DAM/NANDINA aplicables |
| A018 | 3.6 | Selección de muestra | Estratificación por NANDINA y seed 2026 | Estado final DAM-disjoint | PARAGRAPH_REWRITE_MINIMAL | PARAGRAPH | Párrafos de partición final | Split v0.2 | Evitar describir seed/estratificación como regla final | Gate/commit/prompts | YES | Explicar asignación por DAM y ausencia de solapamiento |
| A019 | 3.6 / Tabla 5 | Criterios de selección | Selección y partición | Control de dependencia desactualizado | TABLE_CELL_UPDATE | EXISTING_TABLE_CELL_UPDATE | Celdas de partición/criterio | Split v0.2 | Mantener tabla, cambiar solo celdas afectadas | Labels internos | YES | Precisar DAM-disjoint y conjuntos finales |
| A020 | 3.7 + Tabla 6 | Recolección/preparación | Técnicas y productos | Parte del producto de partición es v0.1 | TABLE_CELL_UPDATE | EXISTING_TABLE_CELL_UPDATE | Celdas de partición/producto | Split v0.2 + fuentes de preparación | No alterar técnicas válidas | Rutas no necesarias | YES | Cambiar producto final únicamente donde está obsoleto |
| A021 | 3.7.1 | Corpus normativo | Constitución/conteos | Debe verificarse contra fuente propia antes de tocar cifras | KEEP | PARAGRAPH | NONE | Fuente primaria de corpus | Sin discrepancia confirmada no se modifica | IDs internos | NO | Verificación sin cambio no genera comentario |
| A022 | 3.7.3 | Normalización | Procedimiento textual | Sustancialmente compatible | TERMINOLOGY_ONLY | PARAGRAPH | Términos puntuales si se confirma obsolescencia | Fuentes metodológicas vigentes | Mantener procedimiento | Labels internos | YES_IF_CHANGED | Comentar solo el término efectivamente cambiado |
| A023 | 3.7.4 | Curación, validación y partición | Split legacy 3 000/100/1 006 | Debe reflejar DAM-disjoint v0.2 | PARAGRAPH_REWRITE_MINIMAL | PARAGRAPH | Párrafo/lista de partición | Split v0.2 | Evitar contradicción con 3.5–3.6 | IDs de gate/versiones | YES | Reemplazar cifras y regla de partición manteniendo estilo del baseline |
| A024 | 3.7.5 / Tabla 7 | Instrumentos y artefactos | Herramientas/rutas/outputs | Algunas rutas v0.1 ya no representan estado final | TABLE_ROW_UPDATE | EXISTING_TABLE_ROW_UPDATE | Solo filas cuyos artefactos cambiaron | Registro de reproducibilidad | Mantener inventario y actualizar lo estrictamente necesario | branch/commit/blob/gate | YES | Identificar fila, artefacto anterior y artefacto vigente en lenguaje comprensible |
| A025 | 3.7.6 | Registro experimental y reproducibilidad | Trazabilidad y condiciones | Debe reflejar el estado auditado con limitaciones documentadas | PARAGRAPH_REWRITE_MINIMAL | PARAGRAPH | Párrafo de estado de reproducibilidad | Auditoría/cierre de reproducibilidad | Describir el grado/estado de reproducibilidad alcanzado según la auditoría experimental, junto con sus limitaciones documentadas; no convertirlo en decisión HE1 | Estados administrativos internos | YES | Cambio exacto y evidencia de reproducibilidad/limitaciones; prohibido “reproducibilidad completa/total” |
| A026 | 3.8.1 | Esquema analítico | Marco descriptivo | Falta distinguir inferencia primaria HE2 del resto descriptivo | PARAGRAPH_REWRITE_MINIMAL | PARAGRAPH | Párrafos de reglas analíticas | Métodos inferenciales + disposiciones | Incorporar análisis realmente ejecutado | IDs internos | YES | 15 contrastes 99%, 1 contraste 95%, sin p-values; resto descriptivo |
| A027 | 3.8.1 / Tabla 8 | Clasificación/codificación | Buckets y salida LLM | Buckets/score legacy | TABLE_CELL_UPDATE | EXISTING_TABLE_CELL_UPDATE | Celdas soporte/auditabilidad | Contrato analítico + HE4 | Corregir codificación sin reconstruir tabla | J/K y score legacy | YES | Sustituir buckets y esquema de auditabilidad con lenguaje de tesis |
| A028 | 3.8.2 | Criterio HE1 | Regla decisional | No existe disposición formal HE1 | PARAGRAPH_REWRITE_MINIMAL | PARAGRAPH | Párrafo de criterio | Cierre experimental + reproducibilidad | Reportar evidencia sin fabricar decisión | Códigos internos | YES | Evidencia disponible y límite: no equivale a disposition HE1 |
| A029 | 3.8.3 | HE2 | Método de comparación | Debe usar comparadores corregidos y contraste profundo | PARAGRAPH_REWRITE_MINIMAL | PARAGRAPH | Párrafos HE2 | Contrato analítico + inferencia | Alinear con ejecución real | Attempt06/result IDs | YES | Comparadores, CI y alcance interno, sin p-values |
| A030 | 3.8.4 | HE3 | Integración/reranker | Estado legacy | PARAGRAPH_REWRITE_MINIMAL | PARAGRAPH | Párrafos HE3 | Integración + reranker v0.2 | Separar integración funcional de diagnóstico LLM | Fase F/G, Group1 | YES | Invariancia y carácter diagnóstico sin IDs internos visibles |
| A031 | 3.8.5 | HE4 | Score normalizado | Evaluación vigente separa estructura y cualitativo | PARAGRAPH_REWRITE_MINIMAL | PARAGRAPH | Párrafos HE4 | Assessment y hallazgos cualitativos | Explicar dos capas y modalidad del evaluador | Códigos de limitación | YES | Traducir limitaciones al español; no inferir corrección jurídica |
| A032 | 3.8.6 | HE5 y sensibilidad | Categorías legacy/análisis pendiente | HE5 inconclusa; EXP11A/B descriptivos; EXP12 no estimable | PARAGRAPH_REWRITE_MINIMAL | PARAGRAPH | Párrafos afectados | Disposición HE5 + síntesis vigente | No inventar umbrales ni causalidad | EXP11A/B/12 sin definir | YES | Sensibilidades en lenguaje natural y EXP12 cerrado sin recuperación |
| A033 | 3.8.7 | Reglas de contrastación | Regla uniforme legacy | HG/HE1 sin disposición; HE2/3/4/5 con estados diferenciados | PARAGRAPH_REWRITE_MINIMAL | PARAGRAPH | Párrafos de reglas finales | Binding de hipótesis | Evitar regla agregada que fabrique HG/HE1 | Códigos crudos de disposición | YES | Explicar cómo se reporta evidencia según cada hipótesis |
| A034 | 3.8.7 / Tabla 9 | Hipótesis–evidencia–criterio | Criterios legacy | Requiere actualización por hipótesis | TABLE_ROW_UPDATE | EXISTING_TABLE_ROW_UPDATE | Filas materialmente afectadas | Fuentes por hipótesis | Mantener tabla; no crear otra | IDs internos | YES | Un comentario por fila modificada, no por filas conservadas |
| A035 | 4.1.1 / Tabla 10 | Curación y partición | Split legacy | Benchmark final 2 950/100/1 056 DAM-disjoint | TABLE_CELL_UPDATE | EXISTING_TABLE_CELL_UPDATE | Celdas finales y párrafo inmediato | Split v0.2 | Actualizar cifras sin rehacer tabla | IDs internos | YES | Cifras concretas y alcance DAM/NANDINA |
| A036 | 4.1.2 / Tabla 11 | Corpus normativo | Auditoría/estructura | Verificación requerida, sin discrepancia confirmada en este plan | KEEP | EXISTING_TABLE_CELL_UPDATE | NONE | Fuente primaria de corpus | No modificar por inferencia | IDs internos | NO | Verificación sin cambio no genera comentario |
| A037 | 4.1.3 / Tabla 12 | Recuperación normativa | Ranking comparativo legacy | Comparadores actuales plano, jerárquico y denso corregidos | TABLE_STRUCTURE_UPDATE | EXISTING_TABLE_ROW_UPDATE | Encabezados/filas/valores necesarios | Resultados primarios HE2 | Adaptar tabla existente; no duplicarla | Attempt06/D1a si no se definen | YES | Explicar columnas/filas modificadas y ausencia de CI por brazo |
| A038 | 4.1.3 / Tabla 13 | Cobertura normativa | Cobertura legacy | Cinco variantes a 50/100/200, descriptivas | TABLE_STRUCTURE_UPDATE | EXISTING_TABLE_ROW_UPDATE | Encabezados y cinco filas | Cobertura descriptiva | Usar tabla existente para comparación multidimensional | Phase E/códigos internos | YES | Declarar carácter descriptivo, sin CI/p-values ni favorabilidad |
| A039 | 4.1.3 / Figura 4 | Desempeño temprano/cobertura | Figura legacy | Debe mostrar evidencia primaria HE2 vigente | FIGURE_UPDATE | FIGURE | Sustituir imagen/caption manteniendo número 4 | Especificación/caption científico vigente | Existe especificación actual que resume evidencia primaria | IDs gráficos internos | YES | Motivo, benchmark y límites no causales |
| A040 | 4.1.3 / Figura 5 | Cobertura por estrategia/profundidad | Figura legacy | Debe mostrar cobertura exacta actual | FIGURE_UPDATE | FIGURE | Sustituir imagen/caption manteniendo número 5 | Especificación descriptiva vigente | Actualización necesaria y descriptiva | IDs internos | YES | Explicar que no constituye inferencia confirmatoria |
| A041 | 4.1.4 / Tabla 14 | Recuperación histórica global | n=1 006 y métricas legacy | Histórico vigente sobre n=1 056 | TABLE_STRUCTURE_UPDATE | EXISTING_TABLE_ROW_UPDATE | Valores/filas obsoletos | Resultados HE2 + Top-50 suplementario | Tabla existente es el lugar adecuado | IDs internos | YES | n=1 056 y métricas vigentes; no confundir con exactitud end-to-end |
| A042 | 4.1.4 / Tabla 15 | Desempeño según precedentes | Buckets legacy | Buckets 1, 2, 3–4, 5+ DAM; descriptivos | TABLE_STRUCTURE_UPDATE | EXISTING_TABLE_ROW_UPDATE | Encabezados/filas/celdas | Evidencia descriptiva HE5 | Conservar tabla; no etiquetar “insuficiente” | IDs de soporte | YES | Buckets literales y ausencia de umbral retrospectivo |
| A043 | 4.1.4 / Figura 6 | Soporte histórico | Figura legacy | Se sustituirá por sensibilidad conjunta tamaño-composición | FIGURE_UPDATE | FIGURE | Sustituir imagen/caption, mantener número 6 | Sensibilidad EXP11A vigente | Evita duplicar Tabla 15 y usa el espacio gráfico para análisis ejecutado | ID de figura/EXP11A si no se define | YES | Condiciones observadas y prohibición de efecto causal aislado |
| A044 | 4.1.5 / Tabla 16 | Integración histórica–normativa | Conteos legacy | Ranking invariante 1 056/1 056 y trazabilidad 3 168/3 168 | TABLE_ROW_UPDATE | EXISTING_TABLE_ROW_UPDATE | Filas de métricas/controles | Integración vigente | La tabla comunica funciones diferenciadas | Fase F/Group1 | YES | Invariancia, trazabilidad y no reordenamiento |
| A045 | 4.1.5 / Figura 7 | Integración | Snapshot legacy | La evidencia vigente queda mejor en Tabla 16 + síntesis | REMOVE_SUPERSEDED_WITH_INLINE_MARKUP | FIGURE | Marcar figura/caption como supresión propuesta; conservar físicamente en V03 | Integración vigente + criterio de redundancia | No inventar nueva figura ni mantener visual obsoleto | IDs internos | YES | Justificar supresión propuesta; número 7 se conserva en V03 |
| A046 | 4.1.6 / Tabla 17 | Reranker diagnóstico | Resultado legacy | Estado vigente: 20 casos; 19 con referencia; métricas agregadas sin cambio | TABLE_STRUCTURE_UPDATE | EXISTING_TABLE_ROW_UPDATE | Filas/columnas necesarias | Reranker diagnóstico vigente | Mantener objeto tabular | Fase G/gate | YES | Muestra diagnóstica, valores antes/después y ausencia de test preespecificado |
| A047 | 4.1.6 / Figura 8 | Reranker | Figura de degradación legacy | Contradice estado actual y duplica Tabla 17 | REMOVE_SUPERSEDED_WITH_INLINE_MARKUP | FIGURE | Supresión propuesta; conservar físicamente en V03 | Métricas diagnósticas vigentes | Resultado actual se comunica mejor en tabla/prosa | IDs internos | YES | Explicar obsolescencia; número 8 permanece en V03 |
| A048 | 4.1.7 / Tabla 18 | Controles HE4 | Score/controles legacy | Preservación Top-3 y trazabilidad 50/50; otras limitaciones | TABLE_STRUCTURE_UPDATE | EXISTING_TABLE_ROW_UPDATE | Filas afectadas | Assessment HE4 | Separar estructura de calidad cualitativa | Códigos J/K/limitación | YES | Traducir limitación de esquema y eliminar score legacy |
| A049 | 4.1.7 / Tabla 19 | Evaluación cualitativa HE4 | Categorías legacy | 28/50 auditables, 22/50 no auditables, 0 hard violations; modalidad IA | TABLE_STRUCTURE_UPDATE | EXISTING_TABLE_ROW_UPDATE | Filas/columnas afectadas | Hallazgos cualitativos HE4 | Comunicar calidad cualitativa en tabla existente | AI_EXPERT_ROLE y códigos | YES | Modalidad no humana y límite de auditabilidad |
| A050 | 4.1.7 / Figura 9 | Auditabilidad | Score legacy | Evidencia vigente está en Tablas 18–19 | REMOVE_SUPERSEDED_WITH_INLINE_MARKUP | FIGURE | Supresión propuesta; conservar en V03 | HE4 vigente | No perpetuar score superseded | IDs internos | YES | Justificar supresión propuesta; HE4 no equivale a corrección jurídica |
| A051 | 4.1.8 / Tabla 20 | Errores/límites | Análisis pendiente/categorías legacy | HE5 inconclusa; descripción no estimable; EXP12 cerrado | TABLE_ROW_UPDATE | EXISTING_TABLE_ROW_UPDATE | Filas de categorías/estado | HE5 + síntesis interpretativa | Tabla sintética ya existe | IDs/códigos internos | YES | No estimabilidad y prohibición de umbrales post-hoc |
| A052 | 4.1.8 / Figura 10 | Categorías de error | Figura cuantitativa legacy | No existe base para nueva figura equivalente | REMOVE_SUPERSEDED_WITH_INLINE_MARKUP | FIGURE | Supresión propuesta; conservar en V03 | HE5/EXP12 vigentes | Evitar cuantificación no autorizada | IDs internos | YES | Información actual queda en Tabla 20/prosa; número 10 permanece en V03 |
| A053 | 4.2 | Introducción a contrastación | Marco decisional legacy | Debe separar decisiones formales y ausencias | PARAGRAPH_REWRITE_MINIMAL | PARAGRAPH | Párrafos introductorios | Binding de hipótesis | No usar mecanismo uniforme inexistente | Códigos internos | YES | Regla de lectura por hipótesis en español natural |
| A054 | 4.2.1 | HE1 | Concluye respaldada | Sin disposición formal terminal | PARAGRAPH_REWRITE_MINIMAL | PARAGRAPH | Contrastación HE1 | Cierre experimental + reproducibilidad | Reportar evidencia y límites sin decisión fabricada | Códigos internos | YES | Evidencia disponible y ausencia de disposición formal |
| A055 | 4.2.2 | HE2 | Estado provisional/legacy | HE2 respaldada por evidencia primaria | PARAGRAPH_REWRITE_MINIMAL | PARAGRAPH | Contrastación HE2 | Disposición + inferencia | Síntesis sin repetir todas las cifras de Tablas 12–14 | IDs internos | YES | Cinco métricas por tres comparadores + cobertura profunda, con límites |
| A056 | 4.2.3 | HE3 | Parcial/provisional | HE3 respaldada; reranker diagnóstico sin mejora agregada | PARAGRAPH_REWRITE_MINIMAL | PARAGRAPH | Contrastación HE3 | Registro HE3 + integración/reranker | Reflejar estado final sin exagerar LLM | F/G/Group1 | YES | Integración preserva ranking; reranker separado y diagnóstico |
| A057 | 4.2.4 | HE4 | Respaldada totalmente | HE4 parcialmente respaldada | PARAGRAPH_REWRITE_MINIMAL | PARAGRAPH | Contrastación HE4 | Registro HE4 + evaluación | Distinguir controles estructurales de auditabilidad cualitativa | Códigos J/K | YES | 50/50 estructura, 28/50 auditables y limitaciones |
| A058 | 4.2.5 | HE5 | Parcialmente respaldada | HE5 inconclusa | PARAGRAPH_REWRITE_MINIMAL | PARAGRAPH | Contrastación HE5 | Disposición HE5 | No estimabilidad no equivale a evidencia favorable/desfavorable | IDs internos | YES | Componentes no estimables/descriptivos y alcance interno |
| A059 | 4.2.6 | HG | Declara HG respaldada | Sin disposición formal terminal | PARAGRAPH_REWRITE_MINIMAL | PARAGRAPH | Contrastación HG | Binding HG + evidencia componentes | No derivar decisión agregada | Código de ausencia formal | YES | Reportar evidencia por componentes y ausencia de decisión terminal |
| A060 | 4.2.6 / Tabla 21 | Síntesis hipótesis | Estados legacy | Estados actuales/ausencias difieren | TABLE_ROW_UPDATE | EXISTING_TABLE_ROW_UPDATE | Seis filas, solo celdas afectadas | Bindings de hipótesis | Mantener tabla sintética | Códigos crudos de estado | YES | Comentario solo en filas modificadas, con evidencia y límite |
| A061 | 4.3.1 / Tabla 22 / Figura 11 | Gestión de información/conocimiento | Discusión conceptual | Conceptualmente vigente | TERMINOLOGY_ONLY | PARAGRAPH | Solo términos realmente incompatibles, si se identifican | Síntesis interpretativa | Preservar separación funcional | IDs internos | YES_IF_CHANGED | Sin cambio visible no habrá comentario; Figura 11 mantiene su número en V03 |
| A062 | 4.3.2 | Recuperación histórica | Métricas legacy | Debe usar resultados actuales y límites HE2 | PARAGRAPH_REWRITE_MINIMAL | PARAGRAPH | Párrafos con cifras/interpretación obsoletas | Resultados HE2 + síntesis | Actualizar argumento sin repetir Tabla 14 | IDs internos | YES | Síntesis del hallazgo y guardrail de no exactitud global RAG |
| A063 | 4.3.3 | Recuperación normativa | Comparadores legacy | Comparadores corregidos y rol documental | PARAGRAPH_REWRITE_MINIMAL | PARAGRAPH | Párrafos con métricas/rol obsoleto | HE2 + corrección vigente | Mantener normativa como evidencia, no ranking principal ni decisión legal | Attempt06/EV codes | YES | Traducir corrección a lenguaje metodológico natural |
| A064 | 4.3.4 | Integración funcional | Cifras legacy | Invariancia 1 056/1 056 y trazabilidad 3 168/3 168 | PARAGRAPH_REWRITE_MINIMAL | PARAGRAPH | Párrafos afectados | Integración vigente | Actualizar datos sin cambiar arquitectura | Fase F | YES | Evidencia se añade sin reordenar Top-3 |
| A065 | 4.3.5 / Tabla 23 | Comparación con antecedentes | Literatura + resultados propios | Resultados propios desactualizados | TABLE_CELL_UPDATE | EXISTING_TABLE_CELL_UPDATE | Solo celdas/frases de resultados propios | Contraste bibliográfico aprobado + resultados actuales | No agregar bibliografía | IDs internos | YES | Actualizar resultado propio conservando antecedente y límite de comparabilidad |
| A066 | 4.3.6 / Figura 12 | Auditabilidad y revisión experta | Discusión conceptual | Debe actualizar lectura HE4; figura conceptual sigue válida | PARAGRAPH_REWRITE_MINIMAL | PARAGRAPH | Párrafos HE4; figura sin cambio | HE4 + síntesis | Mantener diagrama; ajustar interpretación | Códigos internos | YES | 28/50 auditables y limitaciones; Figura 12 mantiene número en V03 |
| A067 | 4.3.7 / Tabla 24 | Validez/reproducibilidad | Límites + pendientes legacy | Debe reflejar estado de reproducibilidad y límites actuales | TABLE_ROW_UPDATE | EXISTING_TABLE_ROW_UPDATE | Filas desactualizadas | Síntesis de limitaciones + auditoría reproducibilidad | Reemplazar pendientes cerrados por limitaciones vigentes sin afirmar reproducibilidad completa | Códigos internos de reproducibilidad | YES | Describir grado/estado de reproducibilidad alcanzado y limitaciones; no convertirlo en HE1 |
| A068 | Conclusiones | Bloque final | Métricas/disposiciones legacy | Debe alinear conclusión con evidencia vigente | PARAGRAPH_REWRITE_MINIMAL | PARAGRAPH | Solo párrafos dependientes de ciencia superseded | HE2–HE5 + HE3/HE4 + límites | Conservar estructura/tono del baseline | IDs internos | YES | Cada conclusión modificada debe expresar hallazgo y límite, sin nueva ciencia |
| A069 | Recomendaciones | Bloque final | Prospectivas | Generalmente compatibles | TERMINOLOGY_ONLY | PARAGRAPH | Frases puntuales que afirmen generalización como hecho | Limitaciones vigentes | Mantener naturaleza prospectiva | IDs experimentales no definidos | YES_IF_CHANGED | Comentar únicamente la frase realmente modificada |
| A070 | Lista de Tablas | Página preliminar | Falta Tabla 3 y secuencia 4–25 está desplazada +1 respecto del cuerpo | Defecto preexistente | INLINE_REPLACE | NOTE | Insertar Tabla 3 y renumerar entradas de lista 4–25 a 4–24, sin tocar números corporales | Baseline estructural | La lista debe reflejar 24 tablas reales del cuerpo | Ninguno | YES | Explicar que se corrige solo la lista: Tabla 3 se incorpora y la entrada residual Tabla 25 desaparece |
| A071 | Lista de Figuras | Página preliminar | Lista 1–12 | V03 debe preservar numeración baseline 1–12 | KEEP | NOTE | NONE en numeración durante revisión | Matriz C corregida | Evitar confusión antes de aceptación de supresiones propuestas | IDs de figuras internos | NO | No hay cambio de numeración en V03; cualquier renumeración queda para copia limpia posterior |
| A072 | Índice/campos automáticos | TOC/listas/paginación | Campos baseline | La copia de revisión no debe introducir ruido por renumeración anticipada | KEEP | NOTE | NONE durante V03 salvo actualizaciones técnicas imprescindibles al cierre | Baseline editorial | Prioridad: comparabilidad humana | IDs internos | NO | Sin cambio visible planificado en esta etapa |
| A073 | 3.2.4 | Frase previa a Tabla 3 | “La Tabla 4 resume las operaciones ejecutadas en cada fase.” | Referencia interna incorrecta | INLINE_REPLACE | PARAGRAPH | Solo `Tabla 4`→`Tabla 3` | Baseline estructural | El objeto inmediatamente siguiente es Tabla 3 | Ninguno | YES | Corregir exclusivamente el número de referencia; no renumerar Tabla 3 |
| A074 | 3.2.4 | Frase sobre instrumentos | “La Tabla 6 de la sección 3.6…” | La tabla de instrumentos es Tabla 7 en 3.7.5 | INLINE_REPLACE | PARAGRAPH | `Tabla 6`→`Tabla 7` y `sección 3.6`→`sección 3.7.5` | Baseline estructural | Reconciliar referencia con el objeto real | Ninguno | YES | Corregir número y sección sin alterar contenido científico |
| A075 | 3.7.5 | Frase introductoria | “La Tabla 8 relaciona los scripts…” | El objeto siguiente es Tabla 7 | INLINE_REPLACE | PARAGRAPH | `Tabla 8`→`Tabla 7` | Baseline estructural | Referencia desplazada | Ninguno | YES | Corrección editorial mínima |
| A076 | 3.8.1 | Frase introductoria | “La Tabla 9 resume…” | El objeto siguiente es Tabla 8 | INLINE_REPLACE | PARAGRAPH | `Tabla 9`→`Tabla 8` | Baseline estructural | Referencia desplazada | Ninguno | YES | Corrección editorial mínima |
| A077 | 3.8.7 | Frase introductoria | “La Tabla 10 relaciona cada hipótesis…” | El objeto siguiente es Tabla 9 | INLINE_REPLACE | PARAGRAPH | `Tabla 10`→`Tabla 9` | Baseline estructural | Referencia desplazada | Ninguno | YES | Corrección editorial mínima |
| A078 | 4.1.3 | Primera frase de resultados normativos | “La Tabla 13 resume los resultados…” | Los resultados de ranking temprano están en Tabla 12 | INLINE_REPLACE | PARAGRAPH | `Tabla 13`→`Tabla 12` | Baseline estructural | La frase describe exactamente el contenido de Tabla 12 | Ninguno | YES | Corregir solo referencia |
| A079 | 4.1.3 | Párrafo posterior a Tabla 12 | “Los valores de la Tabla 13 se presentan…” | Los valores citados son los de Tabla 12 | INLINE_REPLACE | PARAGRAPH | `Tabla 13`→`Tabla 12` | Baseline estructural | Reconciliar cifras mencionadas con tabla fuente | Ninguno | YES | Corrección editorial mínima |
| A080 | 4.1.8 | Frase previa a Tabla 20 | “La Tabla 21 resume los hallazgos…” | El objeto siguiente es Tabla 20 | INLINE_REPLACE | PARAGRAPH | `Tabla 21`→`Tabla 20` | Baseline estructural | Referencia desplazada | Ninguno | YES | Corrección editorial mínima |
| A081 | 4.2 | Introducción a contrastación | “criterios operacionales definidos en la Tabla 10” | Los criterios operacionales por hipótesis están en Tabla 9 | INLINE_REPLACE | PARAGRAPH | `Tabla 10`→`Tabla 9` | Baseline estructural | Tabla 10 trata curación/partición, no criterios de hipótesis | Ninguno | YES | Corregir referencia semánticamente incorrecta |
| A082 | 4.3.5 | Frase previa a Tabla 23 | “La Tabla 24 resume…” | El objeto siguiente es Tabla 23 | INLINE_REPLACE | PARAGRAPH | `Tabla 24`→`Tabla 23` | Baseline estructural | Referencia desplazada | Ninguno | YES | Corrección editorial mínima |

**Política de comentarios corregida:** toda fila `KEEP` con `minimal_edit_scope = NONE` queda con `requires_comment = NO`. Las filas condicionales de terminología solo reciben comentario si efectivamente se modifica texto. Las verificaciones sin cambio permanecen en trazabilidad, no en comentarios Word.

---

# 3. MATRIZ B — Mapa maestro de tablas corregido

| baseline_table_number | baseline_caption | baseline_section | baseline_role | scientific_status | future_action | future_table_number | caption_action | cell_level_changes_expected | whole_table_replacement_required | whole_table_replacement_justification | cross_references_affected | list_of_tables_action |
|---:|---|---|---|---|---|---:|---|---|---|---|---|---|
| 1 | Operacionalización de variables | 3.1.4 | Operacionalización metodológica | PARTIALLY_OBSOLETE | TABLE_CELL_UPDATE | 1 | KEEP | Sí | NO | Estructura válida | Sin anomalía interna; una mención externa a “Tabla 1” en antecedentes pertenece a otro estudio y no es referencia a esta tabla | KEEP |
| 2 | Matriz de consistencia del proyecto. | 3.1.5 | Consistencia | SUBSTANTIALLY_ALIGNED | TABLE_CELL_UPDATE | 2 | KEEP | Sí, técnicas/indicadores | NO | Estructura válida | Sin anomalía detectada | KEEP |
| 3 | Correspondencia entre las fases RAG y las operaciones ejecutadas en el piloto | 3.2.4 | Arquitectura operativa | ALIGNED | KEEP | 3 | KEEP | No | NO | Tabla vigente | A073: frase previa dice Tabla 4 y debe decir Tabla 3 | ADD entrada Tabla 3; no renumerar cuerpo |
| 4 | Tamaño y función de los conjuntos utilizados en el piloto | 3.5 | Benchmark | OBSOLETE_VALUES | TABLE_CELL_UPDATE | 4 | KEEP | Sí | NO | Estructura válida | La referencia de 3.5 a Tabla 4 es correcta | Lista: corregir desplazamiento para que Tabla 4 apunte a su objeto real |
| 5 | Criterios aplicados para la selección de la muestra del piloto | 3.6 | Selección/partición | OBSOLETE_DEPENDENCY_CONTROL | TABLE_CELL_UPDATE | 5 | KEEP | Sí | NO | Estructura válida | La referencia previa a Tabla 5 es correcta | Corregir secuencia desplazada de lista |
| 6 | Técnicas, condiciones y productos de la recolección y preparación de datos | 3.7 | Preparación | MIXED | TABLE_CELL_UPDATE | 6 | KEEP | Sí | NO | Estructura válida | La referencia inmediata a Tabla 6 es correcta; A074 no apunta a esta tabla, sino erróneamente a instrumentos | Corregir secuencia desplazada de lista |
| 7 | Instrumentos computacionales y artefactos generados | 3.7.5 | Reproducibilidad/instrumentos | PARTIALLY_OBSOLETE | TABLE_ROW_UPDATE | 7 | KEEP | Sí | NO | Inventario válido | A074: Tabla 6/sección 3.6→Tabla 7/sección 3.7.5; A075: Tabla 8→Tabla 7 | Corregir secuencia desplazada de lista |
| 8 | Esquema de clasificación y codificación de los datos analíticos | 3.8.1 | Codificación | PARTIALLY_OBSOLETE | TABLE_CELL_UPDATE | 8 | KEEP | Sí | NO | Estructura válida | A076: Tabla 9→Tabla 8 | Corregir secuencia desplazada de lista |
| 9 | Correspondencia entre hipótesis, evidencia analítica y criterio operacional | 3.8.7 | Contrastación metodológica | OBSOLETE_DECISION_FRAME | TABLE_ROW_UPDATE | 9 | KEEP | Sí | NO | Resumen útil | A077: Tabla 10→Tabla 9; A081: Tabla 10→Tabla 9 | Corregir secuencia desplazada de lista |
| 10 | Resultados de curación, deduplicación y partición de las series de clase 87 | 4.1.1 | Split/resultados | LEGACY_V0_1 | TABLE_CELL_UPDATE | 10 | KEEP | Sí | NO | Estructura válida | No hay referencia corporal válida que deba cambiar a Tabla 10; A081 deja de apuntar erróneamente aquí | Corregir secuencia desplazada de lista |
| 11 | Resultados de la auditoría y estructuración del corpus normativo jerárquico | 4.1.2 | Resultado documental | VERIFY_REQUIRED | KEEP pending source verification | 11 | KEEP | Solo si se confirma discrepancia | NO | Sin evidencia para reconstrucción | Sin anomalía detectada | Corregir secuencia desplazada de lista |
| 12 | Comparación del desempeño de las estrategias de recuperación normativa | 4.1.3 | Ranking normativo | LEGACY_METRICS | TABLE_STRUCTURE_UPDATE | 12 | MINOR_UPDATE_IF_NEEDED | Sí | NO | Puede adaptarse in-place | A078 y A079: ambas menciones Tabla 13→Tabla 12 | Corregir secuencia desplazada de lista |
| 13 | Cobertura exacta y jerárquica del pool normativo por profundidad | 4.1.3 | Cobertura normativa | LEGACY_METRICS | TABLE_STRUCTURE_UPDATE | 13 | UPDATE_MINIMAL | Sí | NO | Estructura comparativa reutilizable | Sin referencia corporal incorrecta propia detectada | Corregir secuencia desplazada de lista |
| 14 | Desempeño global de la recuperación histórica | 4.1.4 | Ranking histórico | OBSOLETE_VALUES | TABLE_STRUCTURE_UPDATE | 14 | KEEP | Sí | NO | Lugar correcto para métricas históricas | Sin anomalía detectada | Corregir secuencia desplazada de lista |
| 15 | Desempeño de la recuperación histórica según disponibilidad de precedentes | 4.1.4 | Soporte histórico descriptivo | LEGACY_BUCKETS | TABLE_STRUCTURE_UPDATE | 15 | MINOR_UPDATE | Sí | NO | Estructura comparativa válida | Sin anomalía detectada | Corregir secuencia desplazada de lista |
| 16 | Contribución de las fuentes histórica y normativa en la integración híbrida | 4.1.5 | Integración HE3 | LEGACY_COUNTS | TABLE_ROW_UPDATE | 16 | MINOR_UPDATE | Sí | NO | Tabla funcional vigente | Sin anomalía detectada | Corregir secuencia desplazada de lista |
| 17 | Comparación del ranking original y del reordenamiento diagnóstico con LLM | 4.1.6 | Reranker diagnóstico | LEGACY_RESULT | TABLE_STRUCTURE_UPDATE | 17 | KEEP | Sí | NO | Puede actualizarse in-place | Sin anomalía detectada | Corregir secuencia desplazada de lista |
| 18 | Cumplimiento de los controles de estructura, trazabilidad y auditabilidad | 4.1.7 | HE4 estructural | LEGACY_SCORE_MIX | TABLE_STRUCTURE_UPDATE | 18 | MINOR_UPDATE | Sí | NO | Mantener tabla de controles | Sin anomalía detectada | Corregir secuencia desplazada de lista |
| 19 | Distribución de soporte y fallos secundarios de las explicaciones | 4.1.7 | HE4 cualitativa | LEGACY_CATEGORIES | TABLE_STRUCTURE_UPDATE | 19 | UPDATE | Sí | NO | Tabla existente puede absorber evaluación vigente | Sin anomalía detectada | Corregir secuencia desplazada de lista |
| 20 | Patrones de error y límites identificados por etapa | 4.1.8 | HE5/límites | OBSOLETE/PENDING | TABLE_ROW_UPDATE | 20 | MINOR_UPDATE | Sí | NO | Tabla sintética útil | A080: Tabla 21→Tabla 20 | Corregir secuencia desplazada de lista |
| 21 | Contrastación de las hipótesis específicas y de la hipótesis general | 4.2.6 | Síntesis de hipótesis | OBSOLETE_DISPOSITIONS | TABLE_ROW_UPDATE | 21 | KEEP | Sí | NO | Tabla útil con estados/ausencias | La mención previa en 4.1.8 deja de apuntar erróneamente a Tabla 21; no hay otra anomalía | Corregir secuencia desplazada de lista |
| 22 | Contribución del piloto a la gestión de información y conocimiento | 4.3.1 | Discusión conceptual | ALIGNED | TERMINOLOGY_ONLY | 22 | KEEP | Mínimas si alguna | NO | Concepto vigente | Sin anomalía detectada | Corregir secuencia desplazada de lista |
| 23 | Comparación de los resultados con los antecedentes de investigación | 4.3.5 | Contraste bibliográfico | PARTIALLY_STALE_OWN_RESULTS | TABLE_CELL_UPDATE | 23 | KEEP | Sí, solo resultados propios | NO | Literatura/estructura se conserva | A082: Tabla 24→Tabla 23 | Corregir secuencia desplazada de lista |
| 24 | Amenazas a la validez y medidas de control o delimitación | 4.3.7 | Limitaciones/reproducibilidad | PARTIALLY_OBSOLETE | TABLE_ROW_UPDATE | 24 | KEEP | Sí | NO | Tabla adecuada | La mención de 4.3.5 deja de apuntar erróneamente a Tabla 24; sin otra anomalía | En lista, antigua entrada Tabla 25@121 debe convertirse en Tabla 24@121 |

**Numeración de tablas:** el cuerpo conserva Tabla 1–24. La Lista de Tablas del baseline omite Tabla 3 y, desde ese punto, muestra una secuencia desplazada `Tabla 4@58 … Tabla 25@121`. La futura V03 corregirá únicamente la lista: insertará Tabla 3 para el objeto de la página 58 y desplazará las etiquetas posteriores una unidad hacia abajo hasta terminar en Tabla 24 para el objeto de la página 121. No se renumeran las tablas corporales.

---

# 4. MATRIZ C — Mapa maestro de figuras corregido

| baseline_figure_number | baseline_caption | baseline_section | scientific_status | future_action | review_v03_number | post_author_acceptance_clean_number | caption_action | replacement_required | cross_references_affected | list_of_figures_action |
|---:|---|---|---|---|---:|---|---|---|---|---|
| 1 | Estructura jerárquica del código arancelario en el Sistema Armonizado, la NANDINA y la nomenclatura nacional peruana. | 2.3.2 | CONCEPTUALLY_ALIGNED | KEEP | 1 | 1 | KEEP | NO | No referencia corporal adicional detectada | V03 KEEP 1 |
| 2 | Arquitectura funcional del piloto experimental offline para la recomendación auditable de subpartidas NANDINA | 3.2.4 | ALIGNED_WITH_CURRENT_ARCHITECTURE | KEEP | 2 | 2 | KEEP/terminology review | NO | La única mención corporal explícita “Figura 2” apunta correctamente a este objeto | V03 KEEP 2 |
| 3 | Flujo de transformación de datos aduaneros y fuentes normativas en información auditable | 4.1.2 | CONCEPTUALLY_ALIGNED | KEEP | 3 | 3 | KEEP/terminology review | NO | Sin referencia corporal adicional detectada | V03 KEEP 3 |
| 4 | Comparación del desempeño temprano y la cobertura profunda de los métodos de recuperación | 4.1.3 | SCIENTIFICALLY_OBSOLETE | FIGURE_UPDATE | 4 | 4 | REWRITE_MINIMAL_TO_THESIS_NATIVE_CAPTION | YES | Sin referencia corporal numerada adicional detectada | V03 UPDATE contenido/caption; número 4 se conserva |
| 5 | Cobertura del pool normativo según estrategia y profundidad de recuperación | 4.1.3 | SCIENTIFICALLY_OBSOLETE | FIGURE_UPDATE | 5 | 5 | REWRITE_MINIMAL_TO_THESIS_NATIVE_CAPTION | YES | Sin referencia corporal numerada adicional detectada | V03 UPDATE; número 5 se conserva |
| 6 | Desempeño de la recuperación histórica según disponibilidad de precedentes | 4.1.4 | LEGACY/REDUNDANT_WITH_TABLE15 | FIGURE_UPDATE | 6 | 6 | REWRITE_TO_JOINT_SIZE_COMPOSITION_SENSITIVITY | YES | Sin referencia corporal numerada adicional detectada | V03 UPDATE; número 6 se conserva |
| 7 | Contribución diferenciada de la recuperación histórica y la evidencia normativa en el pool híbrido | 4.1.5 | LEGACY_QUANTITATIVE_SNAPSHOT | REMOVE_SUPERSEDED_WITH_INLINE_MARKUP | 7 | REMOVED_IF_AUTHOR_ACCEPTS | SUPPRESSION_PROPOSED_IN_V03 | NO replacement | Sin referencia corporal numerada adicional detectada | V03 conserva entrada 7; copia limpia podrá retirarla tras aceptación |
| 8 | Variación del ranking antes y después del reordenamiento diagnóstico con LLM | 4.1.6 | LEGACY_RESULT | REMOVE_SUPERSEDED_WITH_INLINE_MARKUP | 8 | REMOVED_IF_AUTHOR_ACCEPTS | SUPPRESSION_PROPOSED_IN_V03 | NO replacement | Sin referencia corporal numerada adicional detectada | V03 conserva entrada 8; copia limpia podrá retirarla |
| 9 | Cumplimiento de los controles de auditabilidad de las explicaciones Top-3 | 4.1.7 | LEGACY_SCORE_VISUALIZATION | REMOVE_SUPERSEDED_WITH_INLINE_MARKUP | 9 | REMOVED_IF_AUTHOR_ACCEPTS | SUPPRESSION_PROPOSED_IN_V03 | NO replacement | Sin referencia corporal numerada adicional detectada | V03 conserva entrada 9; copia limpia podrá retirarla |
| 10 | Distribución de categorías de error y advertencias por etapa del piloto | 4.1.8 | NOT_SUPPORTED_BY_CURRENT_ESTIMABILITY | REMOVE_SUPERSEDED_WITH_INLINE_MARKUP | 10 | REMOVED_IF_AUTHOR_ACCEPTS | SUPPRESSION_PROPOSED_IN_V03 | NO replacement | Sin referencia corporal numerada adicional detectada | V03 conserva entrada 10; copia limpia podrá retirarla |
| 11 | Banco histórico y corpus normativo como componentes de gestión de información y conocimiento | 4.3.1 | CONCEPTUALLY_ALIGNED | KEEP | 11 | 7_IF_7_TO_10_REMOVED_AND_ACCEPTED | KEEP_IN_V03 | NO | Sin referencia corporal numerada adicional detectada | V03 KEEP 11; copia limpia podría renumerar a 7 únicamente tras aceptación |
| 12 | Relación entre datos, información organizada, conocimiento explícito y revisión experta en el piloto | 4.3.6 | CONCEPTUALLY_ALIGNED | KEEP | 12 | 8_IF_7_TO_10_REMOVED_AND_ACCEPTED | KEEP_IN_V03 | NO | Sin referencia corporal numerada adicional detectada | V03 KEEP 12; copia limpia podría renumerar a 8 únicamente tras aceptación |

**Regla vinculante:** `REVIEW_V03_FIGURE_NUMBERING = PRESERVE_BASELINE_1_TO_12`. Las Figuras 7–10 permanecen físicamente visibles en V03 con su supresión propuesta marcada. Figuras 11 y 12 continúan como 11 y 12. Solo una copia limpia posterior a aceptación explícita podrá retirar 7–10 y, entonces, renumerar 11→7 y 12→8 con actualización integral de referencias y lista.

---

# 5. MATRIZ D — Diccionario vigente de lenguaje interno → lenguaje de tesis

| internal_term | must_not_appear_in_thesis | approved_manuscript_expression | context_of_use |
|---|---|---|---|
| G1 / G2 / G3 / G4 / G5 / G6 / G7 / G8 | YES | Omitir; describir directamente método, análisis, resultado o etapa científica | Todo texto visible |
| Group1 / Group2 / Group3 / … | YES | “experimento”, “análisis”, “evaluación de reproducibilidad” o término científico específico | Método/resultados/discusión |
| G3-Fxx / G4-Fxx / G5-Fxx / G6-Fxx / G7-Fxx | YES | “análisis inferencial”, “síntesis interpretativa”, “tabla de resultados”, “figura de resultados” | Todas las secciones |
| ficha | YES | Omitir | Gobernanza interna |
| Prompt / Prompt116 / Prompt117 / Prompt118 / Prompt119 | YES | Omitir | Nunca en la tesis |
| PREFxxx / preflight | YES | Omitir | Nunca en la tesis |
| source freeze | YES | Normalmente omitir; si fuera imprescindible: “fuentes científicas versionadas utilizadas para la actualización” | Metodología/reproducibilidad |
| claim registry / claim ID | YES | “resultado”, “hallazgo”, “evidencia” o “limitación” | Resultados/discusión |
| G3C-xxx / G4Fxx-xxx | YES | Expresión natural del hallazgo, sin código | Resultados/discusión |
| branch | YES | “versión del repositorio” solo si es indispensable para reproducibilidad | Reproducibilidad técnica |
| commit | YES | “versión registrada” solo si es indispensable | Reproducibilidad/anexo técnico |
| blob | YES | “identidad/huella del archivo” solo si es indispensable | Reproducibilidad/anexo técnico |
| gate | YES | Omitir; describir criterio científico o limitación real | Nunca como prosa de tesis |
| candidate / pending external audit / revision required / not approved | YES | Omitir | Gobernanza interna |
| CLOSED / APPROVED como estados administrativos | YES | Describir resultado experimental o limitación concreta | Todas las secciones |
| G5-MAIN-01 / G5-MAIN-02 | YES | “resultados primarios de ranking” / “cobertura profunda” | Resultados |
| G5-SECONDARY / G5-APPENDIX | YES | “análisis descriptivo” / “análisis de sensibilidad” | Resultados/limitaciones |
| G6-FIG-01 / G6-FIG-02 / G6-FIG-03 | YES | Título científico natural de la figura | Captions/lista |
| Attempt06 | YES | “resultados corregidos de los comparadores” o nombre científico del método | Método/resultados |
| 0B-05C | YES | “corrección numérica aplicada a los comparadores” solo si es necesario | Método/limitaciones |
| EV03 / EV04 | YES salvo identificador técnico definido | “comparador normativo plano” / “comparador normativo jerárquico” | Método/resultados |
| D1a | CONDITIONAL | “recuperador denso entrenado con MNRL”; conservar D1a solo si se define como identificador técnico | Método/resultados |
| Phase E | YES | “análisis descriptivo de cobertura del conjunto candidato” | Resultados |
| A_historical_defined | YES | “variantes predefinidas del análisis descriptivo” | Resultados |
| diagnostic_union_hierarchical_dual | YES | “unión diagnóstica de cobertura”, solo si es imprescindible | Resultados/limitaciones |
| HE2_A | YES en prosa salvo definición académica previa | “componente de ranking temprano de HE2” | Método/resultados |
| HE2_B | YES en prosa salvo definición académica previa | “componente de cobertura profunda de HE2” | Método/resultados |
| EXP11A | CONDITIONAL | “análisis de sensibilidad conjunta del tamaño y la composición del banco histórico”; código solo si se define | Sensibilidad |
| H25 / H50 / H75 / H100 | CONDITIONAL | Condiciones técnicas definidas y explicadas al primer uso | Sensibilidad histórica |
| H50-D1 / H50-D2 | CONDITIONAL | “dos composiciones observadas de la condición H50” | Sensibilidad histórica |
| EXP11B | CONDITIONAL | “sensibilidad descriptiva H150/H200 sobre diez pares observados” | Sensibilidad/limitaciones |
| EXP12 | CONDITIONAL | “análisis planificado de diversidad del banco histórico, cerrado sin recuperación; efecto no estimable” | Limitaciones |
| HASH_BOUND_LOCAL_ONLY | YES | “artefacto local cuya identidad quedó registrada mediante huella y tamaño” | Reproducibilidad |
| DECLARED_NOT_RECOVERABLE | YES | “artefacto histórico no recuperable, registrado como limitación de trazabilidad” | Reproducibilidad |
| AI_EXPERT_ROLE | YES | “revisor asistido por IA bajo una rúbrica de rol experto; no correspondió a evaluación humana” | HE4/limitaciones |
| PROMPT_SCHEMA_SPECIFICATION_MISMATCH | YES | “limitación por discrepancia entre el esquema de generación y la especificación evaluada” | HE4/limitaciones |
| EVALUATOR_MODALITY_DEVIATION | YES | “limitación por desviación de la modalidad del evaluador respecto del protocolo previsto” | HE4/limitaciones |
| SUPPORTED | YES como código crudo | “respaldada por la evidencia evaluada” | Contrastación |
| PARTIALLY_SUPPORTED | YES como código crudo | “parcialmente respaldada” | HE4 |
| INCONCLUSIVE | YES como código crudo | “inconclusa con la evidencia disponible” | HE5 |
| NO_FORMAL_DISPOSITION_FOUND | YES | “no se localizó una disposición formal terminal” | HG/HE1 |
| CLOSED_WITHOUT_RETRIEVAL / NOT_ESTIMABLE | YES como código crudo | “cerrado sin ejecutar recuperación; el efecto de diversidad no pudo estimarse” | EXP12 |

---

# 6. CROSS_REFERENCE_AUDIT

Se auditó el baseline completo para todas las apariciones textuales `Tabla N` y `Figura N`, además de la Lista de Tablas y Lista de Figuras. La mención “su Tabla 1” en antecedentes corresponde a una tabla de un estudio citado y se excluye correctamente del inventario interno.

## 6.1 Referencias de tablas

```text
TABLE_BODY_CROSS_REFERENCE_ANOMALIES = 10
TABLE_LIST_ANOMALIES = 2
TABLE_CROSS_REFERENCE_ANOMALIES = 12 total / 10 en prosa + 2 en Lista de Tablas
TABLE_CROSS_REFERENCE_AUDIT = PASS
```

| audit_id | ubicación | referencia baseline | objeto real | corrección planificada |
|---|---|---|---|---|
| TCR-01 | 3.2.4, antes de Tabla 3 | “La Tabla 4 resume…” | Tabla 3 | Tabla 4→Tabla 3 |
| TCR-02 | 3.2.4, frase sobre instrumentos | “La Tabla 6 de la sección 3.6…” | Tabla 7, sección 3.7.5 | Tabla 6→7 y 3.6→3.7.5 |
| TCR-03 | 3.7.5 | “La Tabla 8 relaciona…” | Tabla 7 | Tabla 8→7 |
| TCR-04 | 3.8.1 | “La Tabla 9 resume…” | Tabla 8 | Tabla 9→8 |
| TCR-05 | 3.8.7 | “La Tabla 10 relaciona…” | Tabla 9 | Tabla 10→9 |
| TCR-06 | 4.1.3 | “La Tabla 13 resume…” | Tabla 12 | Tabla 13→12 |
| TCR-07 | 4.1.3 | “Los valores de la Tabla 13…” | Tabla 12 | Tabla 13→12 |
| TCR-08 | 4.1.8 | “La Tabla 21 resume…” | Tabla 20 | Tabla 21→20 |
| TCR-09 | 4.2 | “criterios… definidos en la Tabla 10” | Tabla 9 | Tabla 10→9 |
| TCR-10 | 4.3.5 | “La Tabla 24 resume…” | Tabla 23 | Tabla 24→23 |
| TCR-11 | Lista de Tablas | Falta Tabla 3 | Cuerpo contiene Tabla 3 en p.58 | Insertar Tabla 3 en la lista |
| TCR-12 | Lista de Tablas | Secuencia 4–25 está desplazada +1; aparece Tabla 25@121 | El cuerpo real termina en Tabla 24@121 | Renumerar solo entradas de lista 4–25 a 4–24; eliminar etiqueta residual 25 |

Después de estas correcciones planificadas no queda ninguna referencia tabular interna no reconciliada. Las referencias correctas existentes a Tablas 4, 5 y 6 se mantienen.

## 6.2 Referencias de figuras

```text
FIGURE_CROSS_REFERENCE_ANOMALIES = 0
FIGURE_CROSS_REFERENCE_AUDIT = PASS
```

La Lista de Figuras contiene 1–12 y coincide con los doce captions del cuerpo. La única mención corporal explícita encontrada fuera de los captions, “La Figura 2 representa esta organización”, apunta correctamente a Figura 2. No se detectaron menciones `Figura N` desplazadas. Para V03 no se introduce ninguna renumeración.

---

# 7. PRESENTATION_MODE_AUDIT

| topic | information_shape | candidate_existing_table | final_presentation_mode | reason | redundancy_control |
|---|---|---|---|---|---|
| HE2 | Comparación multidimensional: tres comparadores, cinco métricas primarias, un contraste de cobertura profunda y evidencia descriptiva adicional | Tablas 12, 13 y 14; Figuras 4 y 5 | EXISTING_TABLES + FIGURES + SYNTHESIS_PARAGRAPH | Las tablas existentes absorben métricas/condiciones; las figuras muestran patrones; la prosa de 4.2.2/4.3 sintetiza la conclusión sin repetir todas las cifras | No enumerar en prosa todos los valores ya visibles; remitir a tablas y conservar solo hallazgo principal/límite |
| HE3 | Integración funcional + diagnóstico de 20 casos, con invariancia, trazabilidad y métricas antes/después | Tablas 16 y 17 | EXISTING_TABLES + SYNTHESIS_PARAGRAPH | Tabla 16 organiza integración; Tabla 17 organiza diagnóstico; no se requiere tabla nueva ni figura nueva | Figuras 7–8 se proponen suprimir por obsolescencia/redundancia; prosa solo interpreta |
| HE4 | Dos capas: controles estructurales y evaluación cualitativa de 50 casos | Tablas 18 y 19 | EXISTING_TABLES + SYNTHESIS_PARAGRAPH | La separación en dos tablas existentes refleja mejor estructura vs. auditabilidad cualitativa | Figura 9 se propone suprimir; la prosa no repite todas las tasas |
| HE5 | Evidencia descriptiva por soporte, jerarquía, no estimabilidad y límites | Tablas 15 y 20 | EXISTING_TABLES + SYNTHESIS_PARAGRAPH | Tabla 15 conserva soporte descriptivo; Tabla 20 sintetiza límites/no estimabilidad | Figura 10 se propone suprimir; no crear umbrales ni repetir cifras de Tabla 15 en texto |
| EXP11A | Seis métricas observadas en múltiples condiciones H25/H50-D1/H50-D2/H75/H100; sensibilidad conjunta no causal | Ninguna tabla baseline semánticamente adecuada sin forzar Tabla 15 o 24 | FIGURE_6 + BRIEF_SYNTHESIS_PARAGRAPH | La figura científica aprobada comunica mejor múltiples condiciones/métricas; crear una tabla nueva alteraría la estructura sin necesidad | Prosa solo explica sensibilidad conjunta y límite no causal; no duplicar los 31 puntos ni inventar resumen |
| EXP11B | Diez pares observados H150/H200, varias métricas; evidencia suplementaria descriptiva | Tabla 24 puede absorber el límite metodológico, pero no la matriz completa de resultados | BRIEF_PARAGRAPH + EXISTING_TABLE_24_LIMITATION_ROW | No es evidencia principal ni inferencial; la tesis puede reportar la existencia del análisis y su límite sin importar toda la matriz técnica al cuerpo | No listar diez pares ni 10×métricas en prosa; detalle permanece en artefacto reproducible, no en nueva tabla del cuerpo |
| EXP12 | Estado de diseño/feasibility: cerrado sin recuperación; efecto no estimable | Tablas 20 y 24 | EXISTING_TABLE_ROW_UPDATE + BRIEF_PARAGRAPH | Es un resultado negativo/no estimable, no un conjunto de métricas que justifique tabla propia | No crear figura ni tabla nueva; una frase de síntesis y filas de límites son suficientes |
| Reproducibilidad | Inventario de trazabilidad, activos versionados/locales/no recuperables y limitaciones | Tabla 24 + Tabla 7 para artefactos | EXISTING_TABLES + SYNTHESIS_PARAGRAPH | Tabla 7 organiza instrumentos/artefactos y Tabla 24 organiza amenazas/limitaciones; la prosa debe describir el estado alcanzado con sus límites | Prohibido “reproducibilidad completa/total”; no duplicar inventarios técnicos extensos en narrativa |

```text
NEW_TABLE_JUSTIFIED = false
PRESENTATION_MODE_AUDIT = PASS
```

La decisión de no crear una tabla nueva no es automática: EXP11A se comunica mejor mediante la Figura 6 aprobada; EXP11B es suplementario y su matriz completa sería desproporcionada para el cuerpo; EXP12 es no estimable; y reproducibilidad ya dispone de Tablas 7 y 24. En HE2/HE3/HE4/HE5 existen tablas baseline aptas para absorber los cambios mediante celdas/filas/encabezados.

---

# 8. Comentarios futuros — política corregida

Solo habrá comentario Word cuando exista una modificación visible, supresión propuesta, sustitución de figura, corrección de referencia cruzada o cambio terminológico efectivamente aplicado. No se comentarán verificaciones `KEEP` sin cambio.

Plantilla vinculante:

```text
Cambio exacto:
Motivo del cambio:
Evidencia concreta:
Fuente gobernante:
Efecto en la tesis:
Límite de interpretación:
```

Todo comentario será íntegramente en español. La fuente se describirá primero en lenguaje comprensible; un path técnico podrá añadirse al final para trazabilidad sin filtrarlo a la prosa visible.

---

# 9. Convención futura de revisión

```text
TEXTO_ANTERIOR_MODIFICADO = AMARILLO + TACHADO + VISIBLE
TEXTO_NUEVO = AMARILLO + NO_TACHADO + VISIBLE
TEXTO_SIN_CAMBIO = NORMAL
REVIEW_V03_FIGURE_NUMBERING = PRESERVE_BASELINE_1_TO_12
```

En tablas el marcado se limitará al fragmento/celda/fila realmente afectado. Las Figuras 7–10, si se propone suprimirlas, permanecerán visibles en V03 con su supresión marcada; Figuras 11–12 seguirán numeradas 11–12.

---

# 10. Auditoría final de coherencia

| Control | Resultado | Verificación |
|---|---|---|
| El plan parte del baseline original, no de V01/V02 | YES | Baseline único de reejecución; V01/V02 rechazadas |
| Organización editorial preservada salvo cambio imprescindible | YES | Secciones y 24 tablas conservadas; figuras 1–12 conservan numeración en V03 |
| Cada tabla tiene un único número corporal | YES | Cuerpo 1–24 sin renumeración |
| Lista de Tablas reconciliada | YES | Falta 3 y desplazamiento 4–25 identificados y corregibles sin tocar cuerpo |
| Referencias `Tabla N` auditadas | YES | 10 anomalías corporales reconciliadas |
| Referencias `Figura N` auditadas | YES | 0 anomalías; lista/captions 1–12 consistentes |
| Cambios de tabla intentan primero fragmento/celda/fila | YES | Ningún reemplazo completo autorizado |
| Comentarios solo para cambios reales | YES | KEEP+NONE = NO; verificaciones sin cambio no generan comentario |
| Comentarios previstos en español y concretos | YES | Plantilla de seis apartados |
| “Reproducibilidad completa/total” eliminada del plan | YES | A025/A067 usan “grado/estado de reproducibilidad… con limitaciones documentadas” |
| Decisión prosa/tabla/figura explicitada | YES | PRESENTATION_MODE_AUDIT = PASS |
| No se crea ciencia nueva | YES | 0 claims/métricas/inferencia/p-values/CI/referencias nuevas |
| Problema, objetivos e hipótesis aprobadas preservados | YES | A001/A003/A004/A007 |
| HG sin disposición inventada | YES | A059 |
| HE1 sin disposición inventada | YES | A028/A054/A067 |
| EXP12 cerrado sin recuperación y no estimable | YES | A032/A051/A067 + auditoría de presentación |
| G7-F03 no autorizado | YES | `G7_F03_AUTHORIZED = false` |
| V03 no creada | YES | `V03_CREATED = false` |

---

# 11. Secuencia futura, aún no autorizada

1. Revalidar la identidad del baseline antes de editar.
2. Abrir exclusivamente el baseline como documento de trabajo.
3. Corregir primero las doce anomalías tabulares/lista registradas en `CROSS_REFERENCE_AUDIT`, con marcado mínimo.
4. Aplicar cambios metodológicos 3.1–3.8 según Matriz A.
5. Actualizar Tablas 1–9 únicamente a nivel de fragmento/celda/fila/encabezado.
6. Actualizar resultados 4.1 y Tablas 10–20; Figuras 4–6 conservan números 4–6.
7. Mantener Figuras 7–10 físicamente visibles como supresión propuesta y conservar Figuras 11–12 con sus números originales durante V03.
8. Actualizar contrastación 4.2 y Tabla 21.
9. Actualizar discusión 4.3 y Tablas 22–24, aplicando `PRESENTATION_MODE_AUDIT` para evitar redundancia.
10. Actualizar conclusiones y revisar recomendaciones con la voz del baseline.
11. Ejecutar búsqueda de lenguaje interno según Matriz D.
12. Mantener Lista de Figuras 1–12 en V03; cualquier renumeración queda diferida a una copia limpia posterior a aceptación explícita.
13. Renderizar y auditar visualmente toda futura V03 antes de presentarla al autor.

Esta secuencia no autoriza la creación de V03.

---

# 12. Estado terminal

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

No se modificaron el baseline, V01, V02, `main`, Plan Maestro, fichas, artículo, proyecto aprobado ni v13. La ejecución se detiene en planificación, como exige Prompt119.
