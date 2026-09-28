# PROMPT121H-R1 — Corregir muestra diagnóstica y restaurar ancla del comentario 288

## 0. Actor y autorización

Actúa como **IA de Redacción Científica** del proyecto `elVladdi/gci-nandina-rag`.

No eres CODEX. No eres la IA Experimental. Esta es una corrección mínima de 121H después de auditoría externa `REVISION_REQUIRED`.

Lee íntegramente antes de editar:

```text
writing_prompts_tmp/121H_AUDITORIA_EXTERNA_REVISION_REQUIRED.md
@ 6276c0ddbdc7db5b6f9cc66a711bdab808f24bf2

writing_prompts_tmp/121H_EJECUTAR_G7_F02_V03_BLOQUE_H_4_1_6_RERANKER.md
@ 96da70c18ffd1e0125d7087379a66d35f119ba2e
```

Ejecuta exclusivamente las dos correcciones descritas aquí. **No ejecutes 121I ni ningún bloque posterior.**

---

## 1. Entradas exactas

Trabaja exclusivamente sobre los artefactos H auditados:

```text
Molleapasa_gv_G7F02_REVIEW_V03_H.docx
SHA256 = 77f2ecab58855a570e65c7a48e5b5d92325c84f8458d1ae446f941f3cbbd1468
SIZE = 4666858

g7_thesis_claim_traceability_v0.3_H.csv
SHA256 = bc9bf9cebe931e8747ca91c80f86726459f5a99b24e0c7dd076e3fa2e7314a31
SIZE = 100004
ROWS = 108
```

Verifica hashes, tamaños y filas antes de editar. Si no coinciden, `STOPPED_PRECONDITION`.

No reconstruyas H desde G ni desde versiones previas.

Para restaurar únicamente el anclaje heredado del comentario 288 puedes usar como **referencia estructural** el artefacto G aprobado:

```text
Molleapasa_gv_G7F02_REVIEW_V03_G.docx
SHA256 = aaa5dbd7f65b9db13c75b82fb7bcbbd75373fb67e4c3b683de0c7181ec13eeaf
SIZE = 4664480
```

No copies ningún otro contenido desde G.

---

## 2. Fuentes científicas gobernantes adicionales para la muestra diagnóstica

Verifica y usa únicamente para corregir la descripción de la muestra:

```text
outputs/evaluation/diagnostic_llm_reranker_data_aduanas_clase87_v0.2/reranker_diagnostic_sample_v0.2.csv
GIT_BLOB = 916af387acc1308831b776ea6c130932c3881904

outputs/evaluation/diagnostic_llm_reranker_data_aduanas_clase87_v0.2/reranker_case_results_v0.2.csv
GIT_BLOB = f16270142cd317276eb15ceac37be8fafb51ed7b

outputs/evaluation/diagnostic_llm_reranker_data_aduanas_clase87_v0.2/reranker_inputs_v0.2.jsonl
GIT_BLOB = d1f0e6958937026704175f31dea7c88874b71f8c
```

Estado vinculante para esta corrección:

```text
population = 1056
sample_size = 20
selection_rule = uniform_random_sample_without_replacement_over_sorted_case_ids_with_at_least_10_closed_candidates
seed = 0
LLM_CANDIDATES_PER_CASE = 10

REFERENCE_RANK_1 = 10 cases
REFERENCE_RANK_2_TO_9 = 9 cases
REFERENCE_ABSENT_FROM_POOL = 1 case
REFERENCE_RANK_11_TO_100 = 0 cases
```

No conviertas esta muestra en muestra probabilística representativa de una población externa. No introduzcas inferencia, valores p ni intervalos de confianza.

---

# 3. Corrección R1-A — primer párrafo de 4.1.6

El primer párrafo activo de **4.1.6. Resultados del reordenamiento diagnóstico con LLM** conserva una descripción legacy incorrecta de la composición de la muestra.

Texto legacy actualmente activo:

```text
La corrida diagnóstica disponible evaluó veinte casos y envió diez candidatos al modelo qwen2.5:7b-instruct. La muestra incluyó cinco casos con la etiqueta en la primera posición, cinco entre las posiciones 2 y 10, cinco entre las posiciones 11 y 100 y cinco códigos con un único precedente. El modelo se ejecutó localmente, con temperatura cero y sin acceso a códigos externos al pool.
```

### Acción exacta

1. **No elimines físicamente** ese texto.
2. Márcalo completo como **amarillo + tachado**.
3. En el mismo lugar añade inmediatamente después texto nuevo **amarillo, no tachado**, en español natural, que exprese sin IDs internos visibles:
   - 20 casos;
   - selección aleatoria uniforme sin reemplazo dentro del conjunto de evaluación elegible;
   - población de 1 056 series;
   - elegibilidad de al menos diez candidatos disponibles en el pool cerrado;
   - semilla fija 0;
   - diez candidatos entregados al LLM por caso;
   - ejecución local con temperatura cero y sin códigos externos al pool.

Redacción objetivo recomendada, ajustable solo para estilo nativo:

```text
La prueba diagnóstica utilizó una muestra de 20 casos seleccionados de forma aleatoria uniforme y sin reemplazo entre las 1 056 series elegibles del conjunto de evaluación, cada una con al menos diez candidatos disponibles en el pool cerrado, mediante una semilla fija de 0. Para cada caso se entregaron diez candidatos al modelo qwen2.5:7b-instruct. El modelo se ejecutó localmente, con temperatura cero y sin acceso a códigos externos al pool.
```

No menciones `case_id`, nombres de archivos, blobs, commits, prompts, gates ni IDs de gobernanza en la tesis visible.

No modifiques la Tabla 17, su nota ni el párrafo final ya corregido de 4.1.6.

---

# 4. Corrección R1-B — restaurar anclaje heredado del comentario 288

En H, el contenido del comentario 288 permanece intacto en `comments.xml`, pero se perdieron sus tres referencias en `document.xml`.

Debes restaurar exactamente:

```text
w:commentRangeStart w:id="288"
w:commentRangeEnd   w:id="288"
w:commentReference  w:id="288"
```

### Reglas

- usa G únicamente para identificar el rango heredado original del comentario 288;
- restaura el comentario 288 sobre el **texto legacy preservado y tachado** del párrafo de resultados de 4.1.6 al que estaba asociado en G;
- no cambies ni un carácter del comentario 288 en `comments.xml`;
- no elimines ni desancles el comentario 447 ya añadido por A046;
- no modifiques ningún otro comentario heredado;
- no añadas comentarios nuevos.

Resultado obligatorio:

```text
INHERITED_COMMENT_COUNT = 196
R1_NEW_COMMENTS_ADDED = 0
TOTAL_COMMENT_COUNT = 198
ALL_COMMENT_IDS_ANCHORED = true
COMMENT_288_CONTENT_UNCHANGED = true
COMMENT_288_ANCHOR_RESTORED = true
COMMENT_447_REMAINS_ANCHORED = true
COMMENT_448_REMAINS_ANCHORED = true
```

---

# 5. Trazabilidad

**No modifiques el CSV H.**

Debe conservarse byte-idéntico:

```text
INPUT_TRACE_SHA256 = bc9bf9cebe931e8747ca91c80f86726459f5a99b24e0c7dd076e3fa2e7314a31
ROWS = 108
NEW_TRACE_ROWS_ADDED = 0
```

La corrección R1 queda documentada en la respuesta de ejecución y en la auditoría externa posterior, no mediante una fila nueva.

---

# 6. Invariantes de alcance

Debes verificar:

```text
TABLE_OBJECT_COUNT = 24
TABLE_17_XML_UNCHANGED_FROM_H = true
TABLES_1_TO_24_EXCEPT_NONE_UNCHANGED = true

SEQ_FIGURA_COUNT = 12
NEW_SEQ_FIGURE_FIELDS = 0
MEDIA_FILE_COUNT = 16
ALL_MEDIA_BINARIES_UNCHANGED_FROM_H = true
FIGURE_8_UNCHANGED_FROM_H = true

TRACKED_DELETION_COUNT = 0

4_1_7_AND_AFTER_OOXML_UNCHANGED_FROM_H = true
121I_EXECUTED = false
```

No modifiques Figura 8, la línea de supresión propuesta, 4.1.7, Tabla 18, Figura 9 ni bloques posteriores.

No cambies márgenes, secciones, tamaño de página, estilos globales, listas de tablas/figuras ni numeración.

---

# 7. QA visual y estructural

Renderiza el DOCX resultante y revisa la zona 4.1.6–4.1.7.

Verifica:

- el párrafo legacy de selección de muestra permanece visible en amarillo + tachado;
- la nueva descripción de muestra aparece inmediatamente después, amarillo y no tachada;
- Tabla 17 conserva exactamente la presentación H ya aprobable;
- Figura 8 y su línea de supresión permanecen iguales a H;
- 4.1.7 inicia intacta;
- no hay clipping, solapamientos ni desbordes;
- el comentario 288 vuelve a estar estructuralmente anclado;
- los 198 comentarios tienen `commentRangeStart`, `commentRangeEnd` y `commentReference`.

---

# 8. Salidas

No sobrescribas H. Genera exclusivamente:

```text
Molleapasa_gv_G7F02_REVIEW_V03_H_R1.docx
g7_thesis_claim_traceability_v0.3_H_R1.csv
```

El CSV de salida debe ser una copia byte-idéntica de H.

Publica respuesta oficial en:

```text
writing_prompts_tmp/121H_R1_RESPUESTA_CORREGIR_MUESTRA_DIAGNOSTICA_Y_ANCLA_COMENTARIO288.md
```

La respuesta debe reportar como mínimo:

```text
PROMPT121H_R1_EXECUTION = COMPLETE | STOPPED_PRECONDITION
SAMPLE_DESCRIPTION_CORRECTED = true|false
COMMENT_288_ANCHOR_RESTORED = true|false
COMMENT_288_CONTENT_UNCHANGED = true|false
TOTAL_COMMENT_COUNT = 198
ALL_COMMENT_IDS_ANCHORED = true|false
TRACE_CSV_BYTE_IDENTICAL_TO_H = true|false
TABLE_17_UNCHANGED_FROM_H = true|false
FIGURE_8_UNCHANGED_FROM_H = true|false
4_1_7_AND_AFTER_UNCHANGED_FROM_H = true|false
121I_EXECUTED = false
EXTERNAL_AUDIT = PENDING_BY_IA_EXPERIMENTAL
```

Detente para auditoría externa.
