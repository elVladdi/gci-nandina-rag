# PROMPT121L — Ejecutar G7-F02 REVIEW V03 — Bloque L: 4.3 Discusión de resultados

## 0. Actor, autorización y alcance exclusivo

Actúa como **IA de Redacción Científica** del proyecto `elVladdi/gci-nandina-rag`.

No eres CODEX. No eres la IA Experimental. No recalcules métricas, no ejecutes experimentos, no hagas búsqueda web, no agregues referencias bibliográficas y no avances a conclusiones ni recomendaciones.

Este bloque queda autorizado por el cierre externo definitivo de 121K tras la formalización F1:

```text
PROMPT121K_EXTERNAL_AUDIT = PASS_AFTER_F1
121K_CLOSED_FOR_DOWNSTREAM = true
121L_AUTHORIZED = true
121K_R1 = SUPERSEDED / DO_NOT_EXECUTE
G7_F02 = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
G7_F03_AUTHORIZED = false
```

Auditoría gobernante:

```text
writing_prompts_tmp/121K_AUDITORIA_EXTERNA_PASS_AFTER_F1.md
commit = 4800908fd4906b72dc2e7e1c2597ca100e79a2a8
GIT_BLOB = 15f596f67c1dcc20cad4a3d3261ace30baf45569
```

Ejecuta **exclusivamente A061–A067**, correspondientes a la sección **4.3. Discusión de resultados**.

```text
AUTHORIZED = A061,A062,A063,A064,A065,A066,A067
NOT_AUTHORIZED = A068,A069,A070,A071,A072,A073,A074,A075,A076,A077,A078,A079,A080,A081,A082
CONCLUSIONES = NOT_AUTHORIZED
RECOMENDACIONES = NOT_AUTHORIZED
121M_AND_AFTER = NOT_AUTHORIZED
G7_F03 = NOT_AUTHORIZED
```

Detente al terminar 121L para auditoría externa.

---

## 1. Entradas acumulativas exactas

Trabaja exclusivamente sobre los artefactos K cerrados:

```text
Molleapasa_gv_G7F02_REVIEW_V03_K.docx
SHA256 = 93cad8010e02e1cdbae092bcba93e8d1f32310baf2e693554e1c3ae54cc2c279
SIZE = 4680083

g7_thesis_claim_traceability_v0.3_K.csv
SHA256 = 30438bef703edc512bcf88db62f1dc3340ac4666a3f00c98f716217df649ffd1
SIZE = 116276
ROWS = 121
```

Verifica identidad antes de editar. Si un hash, tamaño o número de filas no coincide, devuelve `STOPPED_PRECONDITION` y no modifiques nada.

No reconstruyas K desde J ni desde el baseline. No ejecutes el 121K-R1 preventivo.

Estado OOXML heredado obligatorio:

```text
TABLE_OBJECT_COUNT = 24
COMMENT_COUNT = 211
TRACE_ROWS = 121
SEQ_FIGURA_COUNT = 12
MEDIA_FILE_COUNT = 16
TRACKED_DELETION_COUNT = 0
TRACKED_INSERTION_COUNT = 0
TABLE_22_ROW_COUNT = 8
TABLE_22_COLUMN_COUNT = 4
TABLE_23_ROW_COUNT = 9
TABLE_23_COLUMN_COUNT = 4
TABLE_24_ROW_COUNT = 11
TABLE_24_COLUMN_COUNT = 4
FIGURE_11_PRESENT = true
FIGURE_12_PRESENT = true
SECTION_4_2_PRESENT = true
SECTION_4_3_PRESENT = true
CONCLUSIONES_PRESENT = true
```

Si cualquiera de estas precondiciones estructurales falla, detente.

---

## 2. Contratos heredados obligatorios

Lee íntegramente y aplica como contratos heredados:

```text
writing_prompts_tmp/119_RESPUESTA_CORREGIR_PLAN_G7_F02_ANTES_DE_V03.md
GIT_BLOB = 5472f7183618ed1a806220c8ee679ab186b7bc79

writing_prompts_tmp/120_EJECUTAR_G7_F02_REVIEW_V03_DESDE_BASELINE.md
GIT_BLOB = 80a2a3d7fbf88f1a7868bdf350d8ef85b0ad37bd

docs/writing/group7/g7_writing_source_freeze_v0.1.json
GIT_BLOB = 776fcb52e8ada9967504001b897c75b4108bfb63

docs/writing/group7/g7_writing_source_freeze_v0.1.md
GIT_BLOB = feea31e2a45ee5f3d9b8fa1f9a1e1bdc073d6430

writing_prompts_tmp/121K_RESPUESTA_G7_F02_V03_BLOQUE_K_4_2_CONTRASTACION_HIPOTESIS.md
GIT_BLOB = 9b93829a7dddffe0d108a7c6a5515aa37f72585e

writing_prompts_tmp/121K_AUDITORIA_EXTERNA_PASS_AFTER_F1.md
GIT_BLOB = 15f596f67c1dcc20cad4a3d3261ace30baf45569
```

Si encuentras contradicción material entre estos contratos y una fuente científica gobernante, usa `STOPPED_PRECONDITION`. No improvises una conciliación.

---

## 3. Fuentes científicas gobernantes

La jerarquía de fuentes es la congelada en G7-F01: proyecto aprobado para formulaciones; artefactos experimentales para métodos/resultados; G3 para inferencia y HE2/HE5; Group1/Group2 para HE3/HE4 y reproducibilidad; G4 para interpretación, limitaciones y contraste bibliográfico; G5 para números canónicos; G6 para figuras/captions.

Lee y verifica antes de redactar, como mínimo:

```text
outputs/analysis/group3/g3_hypothesis_disposition_v0.1.json
GIT_BLOB = d8f20498ebd26e467ba1916e3e0ed93d1dd06c61

outputs/analysis/group3/g3_inferential_results_v0.1.json
GIT_BLOB = f99b7e46d81b28ca2b7cfce8d24788ad14156dcc

docs/analysis/group4/g4_interpretation_synthesis_v0.1.md
GIT_BLOB = 129a67b15db429b86af059d61753b1942c8f243f

outputs/analysis/group4/g4_result_claim_evidence_matrix_v0.1.json
GIT_BLOB = cc5d85bad5d0a2610ffb086f99052fd344b6d8ab

outputs/analysis/group4/g4_limitations_registry_v0.1.json
GIT_BLOB = ae00b93431e912cb78a58344057d9bf7a51fcd47

docs/analysis/group4/g4_literature_contrast_v0.1.md
GIT_BLOB = 2baff53184b17c23380693235a2f3257de5e2bba

docs/results/group5/g5_canonical_tables_v0.1.md
GIT_BLOB = 9f63767b1b93166a8e6bfd2685eaee4f4ae44a4d

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

outputs/audits/g2a_reproducibility_v0.1/gate_g2a_reproducibility_manifest_v0.1.json
GIT_BLOB = dacbf468fea850ea04632aaf9ade4b43e7748f17

outputs/audits/group2b_reproducibility_readiness_v0.2.json
GIT_BLOB = 802f85bf44922ca2dbeb395042908d5bd2efc133

outputs/audits/group2b_reproducibility_closure_v0.1.json
GIT_BLOB = 82e49fc9a04cd0bc19b95c863caf209d542144cd
```

No uses fuentes externas a este freeze. No hagas navegación web. No agregues autores, citas o entradas bibliográficas nuevas.

---

## 4. Estado científico vinculante para la discusión

```text
UNIT_OF_ANALYSIS = SERIE
DEPENDENCY_GROUP = DAM / DECLARACIÓN WHEN_APPLICABLE
SCOPE = CAPITULO_87 / OFFLINE / INTERNAL_EVALUATION
EVAL_SERIES = 1056
EVAL_DAM = 67
EVAL_NANDINA = 42
P_VALUES_CALCULATED = false

HG = NO_FORMAL_DISPOSITION_FOUND
HE1 = NO_FORMAL_DISPOSITION_FOUND
HE2 = SUPPORTED
HE3 = SUPPORTED
HE4 = PARTIALLY_SUPPORTED
HE5 = INCONCLUSIVE
```

Guardrails permanentes:

```text
HISTORICAL_RETRIEVAL_SUPERIORITY != GLOBAL_RAG_ACCURACY
NORMATIVE_EVIDENCE != BINDING_LEGAL_CORRECTNESS
AUDITABLE_EXPLANATION != CLASSIFICATION_OR_LEGAL_CORRECTNESS
CONFIGURABILITY != EMPIRICAL_GENERALIZATION
EXP11A != ISOLATED_CAUSAL_SIZE_EFFECT
EXP11B != SEED_SUPERPOPULATION_INFERENCE
ATTEMPT06 != GLOBAL_ZERO_IMPACT
EXP12 = CLOSED_WITHOUT_RETRIEVAL / NOT_ESTIMABLE / DO_NOT_REOPEN
```

Arquitectura fija:

```text
descripción comercial
→ normalización
→ recuperación histórica
→ ranking histórico
→ Top-3 fijo
→ evidencia normativa específica por candidato
→ constructor de contexto
→ LLM local
→ explicación auditable del Top-3 fijo
```

La evidencia normativa no reordena. El LLM final no clasifica desde cero ni altera el Top-3. El reranker LLM es únicamente diagnóstico.

---

## 5. Números y lecturas canónicas que pueden aparecer

### 5.1 Recuperación histórica vigente

Sobre 1 056 series / 67 DAM:

```text
Top-1 = 0.509469696969697  (~0,5095)
Top-3 = 0.6714015151515151 (~0,6714)
Top-5 = 0.7632575757575758 (~0,7633)
Top-10 = 0.8910984848484849 (~0,8911)
Top-50 = 0.9914772727272727 (~0,9915) [SUPLEMENTARIO]
MRR@100 = 0.6297077493524843 (~0,6297)
```

Los quince contrastes primarios histórico menos comparador, para tres comparadores y cinco métricas, tienen IC bilaterales del 99 % con límite inferior > 0. HE2 = respaldada dentro del benchmark interno. No presentes esto como exactitud end-to-end del RAG, causalidad o superioridad externa.

### 5.2 Recuperación normativa

Comparadores corregidos, 1 056 casos:

```text
BM25 plano: Top-1 0,0275; Top-3 0,0511; Top-5 0,0616; Top-10 0,0653; MRR@100 0,0423
BM25 jerárquico: Top-1 0,0265; Top-3 0,0521; Top-5 0,0625; Top-10 0,0653; MRR@100 0,0420
Denso MNRL: Top-1 0,0009; Top-3 0,0104; Top-5 0,0511; Top-10 0,1780; MRR@100 0,0381
```

Cobertura jerárquica profunda:

```text
Recall@100 = 0.10132575757575757
Recall@200 = 0.3039772727272727
Difference = 0.20265151515151514
95% CI = [0.06676310583580614, 0.34160130792395144]
```

El análisis de variantes profundas adicionales es descriptivo. No conviertas Pool@200 en un segundo contraste confirmatorio.

### 5.3 Integración histórico–normativa y reranker

```text
RANKING_INVARIANCE = 1056/1056
TOP3_CANDIDATE_POSITIONS = 3168
HISTORICAL_TRACEABILITY = 3168/3168
NORMATIVE_TRACEABILITY = 3168/3168
CANDIDATES_INSERTED_OR_REMOVED_BY_NORMATIVE_EVIDENCE = 0
```

Reranker diagnóstico:

```text
N = 20
REFERENCE_IN_POOL = 19
REFERENCE_OUTSIDE_POOL = 1
Top-1 before/after = 0.5000 / 0.5000
Top-3 before/after = 0.6500 / 0.6500
Top-5 before/after = 0.8000 / 0.8000
MRR before/after = 0.6326 / 0.6326
win/tie/loss among reference-in-pool = 0/19/0
```

No conservar lenguaje legacy de degradación, 13 rankings incompletos o necesidad de repetir la corrida.

### 5.4 HE4

```text
Top-3/order preserved = 50/50
Traceability complete = 50/50
Generic normative warning conformant = 41/50
Generic normative warning missing = 9/50
Qualitatively auditable = 28/50
Qualitatively non-auditable = 22/50
Severe violations = 0/50
Evaluator = independent AI configured under expert role
Human scoring = none
HE4 = PARTIALLY_SUPPORTED
```

Conservar en lenguaje natural las dos limitaciones: diferencia entre el esquema previsto y el efectivamente evaluado; y diferencia entre la modalidad ejecutada mediante IA y la revisión humana originalmente preparada. Auditabilidad no equivale a corrección jurídica.

### 5.5 HE5, sensibilidades y reproducibilidad

- calidad descriptiva no operacionalizada prospectivamente; prevalencia/concentración no estimable;
- proximidad jerárquica y soporte histórico son descriptivos sin umbral post hoc;
- grupos de soporte: `1 DAM`, `2 DAM`, `3–4 DAM`, `5+ DAM`; ninguno se denomina retrospectivamente “insuficiente”;
- EXP11A = sensibilidad conjunta tamaño/composición, no causal;
- EXP11B = diez pares H150/H200 observados, descriptivo, sin superpoblación de semillas;
- EXP12 = cerrado sin recuperación; diversidad no estimable; no reabrir;
- reproducibilidad: existen activos locales/restringidos, componentes históricos no recuperables, información incompleta de algunos entornos, ejecución IA/LLM no byte-reproducible y runtime de portabilidad no reejecutado independientemente por el auditor; estas limitaciones no invalidan retrospectivamente los resultados aprobados y no equivalen a una disposición HE1.

---

## 6. Contrato editorial REVIEW V03

Preserva el documento acumulativo K como el mismo Word corregido localmente. No reconstruyas el DOCX.

```text
REDESIGN = PROHIBITED
REBUILD_DOCX_FROM_SCRATCH = PROHIBITED
NEW_CUSTOM_STYLES = 0
NEW_REFERENCES = 0
NEW_MEDIA_FILES = 0
NEW_SEQ_FIGURE_FIELDS = 0
```

En todo cambio visible:

- texto legacy sustituido = amarillo + tachado + visible;
- texto nuevo = amarillo + no tachado + visible;
- texto no afectado = formato normal;
- `w:del = 0`;
- `w:ins = 0`;
- editar primero fragmento, luego celda, luego fila; no reconstruir tablas completas;
- heredar estilos existentes de párrafo/celda;
- conservar encabezados, pies, márgenes, paginación, captions, numeración, tipografías, interlineado y estructura institucional.

No expongas en texto visible IDs o lenguaje interno (`Gx`, `Prompt`, `A061`, paths, blobs, commits, gates, Attempt06, Phase E, códigos de limitación, `SUPPORTED`, etc.). Traduce a prosa académica natural.

Los IDs técnicos pueden aparecer únicamente en comentarios Word y CSV de trazabilidad.

---

## 7. A061 — 4.3.1 / Tabla 22 / Figura 11

**Acción planificada: `TERMINOLOGY_ONLY / YES_IF_CHANGED`.**

Revisa 4.3.1, Tabla 22 y su nota, y Figura 11/caption únicamente para detectar términos materialmente incompatibles con el estado congelado.

Reglas:

- preservar la separación entre datos, información organizada, conocimiento explícito y revisión experta;
- preservar el banco histórico como memoria documental, no fuente normativa ni verdad jurídica;
- preservar el corpus normativo como conocimiento explícito/evidencia revisable, no ruling vinculante;
- preservar Figura 11 físicamente, su número 11, medio, caption y `SEQ Figura`;
- no modificar Tabla 22 si su contenido ya cumple el contrato;
- no introducir números nuevos.

Si no existe incompatibilidad real, **A061 se cierra por verificación sin cambio visible**. En ese caso:

```text
A061_VISIBLE_CHANGE = false
A061_WORD_COMMENT = none
A061_TRACE_ROW = required
```

No fabriques un comentario Word para justificar una verificación sin cambio.

---

## 8. A062 — 4.3.2 Recuperación histórica

Actualiza mínimamente los párrafos con cifras y lectura legacy.

Debe quedar claro que:

1. la recuperación histórica produjo el ranking principal;
2. sobre el benchmark vigente de 1 056 series / 67 DAM obtuvo aproximadamente Top-1 0,5095; Top-3 0,6714; Top-5 0,7633; Top-10 0,8911; MRR@100 0,6297;
3. fue superior internamente a los tres comparadores normativos corregidos en las cinco métricas primarias, con los quince IC 99 % por encima de cero;
4. el resultado es desempeño de recuperación dentro del benchmark interno, no exactitud global del RAG, no causalidad, no generalización externa y no corrección jurídica;
5. cualquier lectura por soporte histórico debe usar exclusivamente los grupos `1 DAM`, `2 DAM`, `3–4 DAM`, `5+ DAM`, sin afirmar un umbral de insuficiencia.

Elimina del texto activo cifras legacy como Top-1 0,8628, Top-3 0,9374, Top-10 0,9801, MRR 0,9062, “62 subpartidas” y buckets `2–4`/`10+` cuando se presenten como estado vigente.

No repitas en prosa todos los valores ya contenidos en tablas; sintetiza el hallazgo y el límite.

---

## 9. A063 — 4.3.3 Recuperación normativa

Actualiza mínimamente los párrafos con resultados o estado provisional legacy.

La prosa activa debe:

- usar los comparadores corregidos plano, jerárquico y denso MNRL;
- reconocer su bajo desempeño temprano frente al histórico dentro del benchmark;
- describir la cobertura profunda jerárquica y el aumento Recall@100→Recall@200 como evidencia de cobertura, no como ranking principal;
- eliminar cualquier afirmación de que las métricas “deben volver a ejecutarse” o permanecen provisionales;
- mantener la función normativa como evidencia documental posterior al ranking;
- mantener que la presencia de un fragmento no garantiza pertinencia, suficiencia ni corrección jurídica;
- no presentar el corpus normativo como mecanismo de reranking del Top-3.

Si se menciona el estado correctivo, exprésalo sin IDs internos: el impacto de la corrección fue dependiente del método; no lo resumas como “sin impacto global”.

---

## 10. A064 — 4.3.4 Integración funcional

Actualiza mínimamente 4.3.4 para reflejar el estado cerrado de HE3.

Debe expresar que:

- la integración histórico–normativa preservó el ranking histórico en 1 056/1 056 casos;
- las 3 168 posiciones del Top-3 conservaron trazabilidad a precedente histórico y a documento normativo;
- la evidencia normativa se añadió sin insertar, eliminar ni reordenar candidatos;
- el reranker LLM fue únicamente diagnóstico y no mostró cambio agregado en Top-1, Top-3, Top-5 ni MRR en la muestra de 20 casos;
- 19 casos tenían la referencia en el pool y uno no; entre los 19 no hubo mejora ni deterioro de posición (`0/19/0` mejora/empate/deterioro);
- HE3 está respaldada, pero el diagnóstico no autoriza presentar el LLM como ranking principal.

Elimina del texto activo conteos legacy `633`, `373`, `0` asociados a la integración anterior y toda lectura de reranker provisional/degradado que deba repetirse.

En la función explicativa, no uses el score legacy 0,9520 como resumen de auditabilidad. Si 4.3.4 necesita mencionar HE4, usa solo los resultados vigentes de §5.4.

---

## 11. A065 — 4.3.5 / Tabla 23 Comparación con antecedentes

Mantén el contraste estrictamente cualitativo y gobernado por:

```text
docs/analysis/group4/g4_literature_contrast_v0.1.md
GIT_BLOB = 2baff53184b17c23380693235a2f3257de5e2bba
```

No agregues bibliografía y no hagas búsqueda web.

Actualiza únicamente las frases/celdas de **resultados propios** que quedaron desactualizadas. Preserva los hallazgos atribuidos a los antecedentes salvo error de transmisión evidente.

Reglas de comparabilidad:

- no comparar porcentajes externos como si provinieran del mismo experimento;
- no afirmar SOTA, “mejor que la literatura”, novelty absoluta, ser el primero ni gap definitivo;
- retrieval histórico ≠ clasificación directa;
- evidencia/citas/rationale ≠ auditabilidad formal ≠ corrección jurídica;
- provenance/reproducibilidad ≠ correctness;
- ausencia de group split equivalente en otro estudio no demuestra leakage.

Tabla 23 debe permanecer como el mismo objeto de **9 filas × 4 columnas**. Cambia solo las celdas de la columna de relación con el piloto que dependan de resultados superseded.

### Regla especial A082 diferida

Existe una corrección futura A082 en la frase previa a Tabla 23:

```text
"La Tabla 24 resume..." → "La Tabla 23 resume..."
```

**A082 NO está autorizada en 121L.** No hagas esa sustitución como acción independiente. Evita editar esa oración en A065; déjala para el bloque editorial futuro A073–A082.

---

## 12. A066 — 4.3.6 / Figura 12

Actualiza mínimamente la discusión de auditabilidad y revisión experta.

La prosa activa debe distinguir:

- controles estructurales: 50/50 preservación Top-3/orden y 50/50 trazabilidad;
- advertencia normativa genérica: 41/50 conforme y 9/50 faltante;
- evaluación cualitativa: 28/50 auditables, 22/50 no auditables, 0/50 violaciones graves;
- evaluador independiente de IA configurado bajo rol experto; no hubo puntuación humana;
- diferencia entre el esquema previsto y el efectivamente evaluado;
- diferencia entre la modalidad IA ejecutada y la revisión humana originalmente preparada;
- auditabilidad documental no equivale a corrección de clasificación ni validez jurídica;
- revisión experta permanece fuera del sistema automatizado.

Elimina del texto activo el score medio legacy 0,9520 y la afirmación legacy de `49/50` conclusiones auditables cuando funcionen como medida de calidad vigente.

**Figura 12 debe permanecer intacta:** mismo número 12, mismo medio, mismo caption, mismo `SEQ Figura`. No crear reemplazo ni nueva figura.

---

## 13. A067 — 4.3.7 / Tabla 24 Validez, reproducibilidad y transferencia

Actualiza mínimamente la prosa y únicamente las filas de Tabla 24 que estén desactualizadas.

La discusión debe:

1. limitar la validez empírica al benchmark offline interno del Capítulo 87, 1 056 series, 67 DAM y 42 NANDINA;
2. mantener la separación DAM-disjoint y la unidad SERIE;
3. eliminar pendientes ya cerrados de “repetir métricas normativas”, “repetir reranker” o “generar análisis integrado de 1 006 descripciones”;
4. expresar HE5 como inconclusa: descripción no estimable prospectivamente, jerarquía/soporte descriptivos, diversidad no estimable;
5. describir EXP11A como sensibilidad conjunta tamaño–composición no causal y EXP11B como diez pares observados sin inferencia a superpoblación de semillas cuando corresponda;
6. registrar que el análisis de diversidad se cerró sin ejecutar recuperación y que su efecto no fue estimable, sin reabrirlo;
7. describir reproducibilidad como estado documentado con limitaciones: activos locales/restringidos, componentes históricos no recuperables, entornos incompletos, IA/LLM no reproducible byte a byte y alcance limitado de la auditoría de portabilidad;
8. no usar “reproducibilidad completa”, “total”, “absoluta” ni equivalente;
9. no convertir la evidencia de reproducibilidad en una decisión retrospectiva sobre HE1;
10. no afirmar validación externa ni transferencia demostrada; cualquier extensión futura debe presentarse como recomendación/prospectiva, no resultado observado.

Tabla 24 debe permanecer como el mismo objeto de **11 filas × 4 columnas**. Prioriza actualizar las filas actualmente obsoletas de resultados normativos, reordenamiento LLM, análisis de errores y reproducibilidad. No reconstruyas la tabla.

No modifiques el encabezado `CONCLUSIONES` ni ningún contenido posterior.

---

## 14. Comentarios Word

Usa comentario Word únicamente cuando exista cambio visible real.

Para A062–A067 se espera al menos un comentario por acción material. A061 solo recibe comentario si efectivamente cambia texto/celda/caption.

Cada comentario debe estar íntegramente en español y contener exactamente estos seis apartados:

```text
Cambio exacto:
Motivo del cambio:
Evidencia concreta:
Fuente gobernante:
Efecto en la tesis:
Límite de interpretación:
```

No agregues secciones adicionales al comentario.

Si A061 es `VERIFIED_NO_CHANGE`, no agregues comentario Word para A061.

Los nuevos IDs de comentario, si se requieren, deben comenzar en el siguiente ID disponible después de 461 y ser consecutivos únicamente para cambios reales.

---

## 15. Trazabilidad CSV

Partir exactamente del CSV K. El archivo completo K debe permanecer como prefijo byte-idéntico del CSV L:

```text
INHERITED_TRACE_PREFIX_SIZE = 116276
INHERITED_TRACE_PREFIX_SHA256 = 30438bef703edc512bcf88db62f1dc3340ac4666a3f00c98f716217df649ffd1
INHERITED_TRACE_ROWS = 121
```

Añade **exactamente siete filas de trazabilidad**, una por A061–A067, sin alterar las 121 heredadas:

```text
G7F02-V03L-001 = A061
G7F02-V03L-002 = A062
G7F02-V03L-003 = A063
G7F02-V03L-004 = A064
G7F02-V03L-005 = A065
G7F02-V03L-006 = A066
G7F02-V03L-007 = A067
TOTAL_TRACE_ROWS_EXPECTED = 128
```

Para A061 sin cambio visible:

- registra la verificación en la fila de trazabilidad;
- `comment_id` debe quedar vacío, no se debe inventar un comentario;
- registra estado equivalente a `VERIFIED_NO_CHANGE` de forma compatible con el esquema existente;
- los campos de marcado visible deben indicar que no hubo sustitución.

Para A061 con cambio visible y para A062–A067, registra el comment_id real y los controles de marcado, fuente, alcance y forbidden interpretation.

No cambies columnas ni encabezado del CSV.

---

## 16. Controles de alcance y no contaminación

Después de editar, verifica:

```text
4_2_UNCHANGED_FROM_K = true
CONCLUSIONES_AND_AFTER_UNCHANGED_FROM_K = true
A068_A069_EXECUTED = false
A070_A082_EXECUTED = false
121M_EXECUTED = false
NEW_REFERENCES = 0
NEW_MEDIA_FILES = 0
NEW_SEQ_FIGURE_FIELDS = 0
TRACKED_DELETION_COUNT = 0
TRACKED_INSERTION_COUNT = 0
TABLE_OBJECT_COUNT = 24
SEQ_FIGURA_COUNT = 12
MEDIA_FILE_COUNT = 16
FIGURE_11_PRESERVED = true
FIGURE_12_PRESERVED = true
TABLE_22_SAME_OBJECT = true
TABLE_23_SAME_OBJECT = true
TABLE_24_SAME_OBJECT = true
```

No cambies Lista de Tablas, Lista de Figuras, índice, referencias bibliográficas, Conclusiones, Recomendaciones ni contenido anterior a 4.3.

---

## 17. QA visual local obligatorio

Renderiza el DOCX L y revisa específicamente:

- toda la sección 4.3;
- Tabla 22 y Figura 11;
- 4.3.2–4.3.4;
- Tabla 23;
- 4.3.6 y Figura 12;
- Tabla 24;
- límite entre 4.3.7 y `CONCLUSIONES`.

Verifica:

```text
NO_CLIPPING
NO_OVERFLOW
NO_OVERLAP
TABLES_LEGIBLE
FIGURES_NOT_DISTORTED
LEGACY_VS_NEW_MARKUP_DISTINGUISHABLE
PAGINATION_ACCEPTABLE
CONCLUSIONES_BOUNDARY_INTACT
```

Si existe defecto visual material, no declares COMPLETE: devuelve `REVISION_REQUIRED` y detente.

---

## 18. Salidas obligatorias

Genera:

```text
Molleapasa_gv_G7F02_REVIEW_V03_L.docx
g7_thesis_claim_traceability_v0.3_L.csv
```

Calcula y reporta SHA-256 y tamaño de ambos; reporta filas del CSV.

Publica la respuesta oficial en:

```text
writing_prompts_tmp/121L_RESPUESTA_G7_F02_V03_BLOQUE_L_4_3_DISCUSION_RESULTADOS.md
```

La respuesta debe informar como mínimo:

```text
PROMPT121L_EXECUTION = COMPLETE | REVISION_REQUIRED | STOPPED_PRECONDITION
A061_STATUS = APPLIED | VERIFIED_NO_CHANGE | REVISION_REQUIRED
A062_APPLIED = true|false
A063_APPLIED = true|false
A064_APPLIED = true|false
A065_APPLIED = true|false
A066_APPLIED = true|false
A067_APPLIED = true|false
TABLE_22_SAME_OBJECT = true|false
TABLE_23_UPDATED_IN_PLACE = true|false
TABLE_24_UPDATED_IN_PLACE = true|false
FIGURE_11_PRESERVED = true|false
FIGURE_12_PRESERVED = true|false
NEW_MEDIA_FILES = <n>
NEW_SEQ_FIGURE_FIELDS = <n>
INHERITED_TRACE_ROWS = 121
NEW_TRACE_ROWS_ADDED = 7
TOTAL_TRACE_ROWS = 128
INHERITED_TRACE_PREFIX_BYTE_IDENTICAL = true|false
INHERITED_COMMENT_COUNT = 211
COMMENTS_ADDED = <6_or_7_expected_if_complete>
TOTAL_COMMENT_COUNT = <actual>
ALL_NONEMPTY_COMMENT_IDS_ANCHORED = true|false
TRACKED_DELETION_COUNT = 0
TRACKED_INSERTION_COUNT = 0
TABLE_OBJECT_COUNT = 24
SEQ_FIGURA_COUNT = 12
MEDIA_FILE_COUNT = 16
4_2_UNCHANGED_FROM_K = true|false
CONCLUSIONES_AND_AFTER_UNCHANGED_FROM_K = true|false
OUT_OF_SCOPE_VISIBLE_MODIFICATIONS = 0
OUT_OF_SCOPE_COMMENT_MODIFICATIONS = 0
NEW_REFERENCES = 0
LOCAL_VISUAL_REVIEW = PASS|FAIL
DOCX_L_SHA256 = <hash>
DOCX_L_SIZE = <bytes>
CSV_L_SHA256 = <hash>
CSV_L_SIZE = <bytes>
CSV_L_ROWS = 128
121K_R1_EXECUTED = false
121M_EXECUTED = false
EXTERNAL_AUDIT = PENDING_BY_IA_EXPERIMENTAL
```

Si A061 no cambia, `COMMENTS_ADDED` debe ser 6 y el total esperado 217. Si A061 cambia, `COMMENTS_ADDED` debe ser 7 y el total esperado 218. No fuerces una edición de A061 solo para alcanzar siete comentarios.

---

## 19. Parada obligatoria

Al finalizar, detente para auditoría externa.

No ejecutes Conclusiones, Recomendaciones, Lista de Tablas, correcciones A073–A082, 121M ni ningún bloque posterior.