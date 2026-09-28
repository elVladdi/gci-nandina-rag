# 121H — Auditoría externa — REVISION_REQUIRED

## Dictamen

```text
PROMPT121H_EXTERNAL_AUDIT = REVISION_REQUIRED
A046_EXTERNAL_AUDIT = REVISION_REQUIRED
A047_EXTERNAL_AUDIT = PASS
121I_AUTHORIZED = false
G7_F02 = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
```

La ejecución 121H aplicó correctamente la actualización cuantitativa principal de A046 y la supresión propuesta de A047, pero no puede recibir PASS externo porque persisten dos defectos verificables en 4.1.6 / comentarios heredados.

## Artefactos auditados

```text
Molleapasa_gv_G7F02_REVIEW_V03_H.docx
SHA256 = 77f2ecab58855a570e65c7a48e5b5d92325c84f8458d1ae446f941f3cbbd1468
SIZE = 4666858

g7_thesis_claim_traceability_v0.3_H.csv
SHA256 = bc9bf9cebe931e8747ca91c80f86726459f5a99b24e0c7dd076e3fa2e7314a31
SIZE = 100004
ROWS = 108
```

La respuesta oficial auditada es:

```text
writing_prompts_tmp/121H_RESPUESTA_G7_F02_V03_BLOQUE_H_4_1_6_RERANKER.md
commit = c6a977f2fc702a73cb0c385e61e9ae751a976c43
```

## Verificaciones que sí pasan

- hashes y tamaños de los artefactos H coinciden con la respuesta oficial;
- el CSV contiene 106 filas heredadas byte-idénticas + A046 + A047 = 108 filas;
- 24 objetos de tabla; solo Tabla 17 cambia;
- `tblPr`, `tblGrid` y `tcPr` de Tabla 17 permanecen estructuralmente idénticos;
- 12 campos `SEQ Figura`; ningún `SEQ Figura` nuevo;
- `w:del = 0`;
- 16 archivos de medios antes y después, todos byte-idénticos;
- Figura 8 legacy permanece físicamente preservada y sin deformación;
- caption legacy de Figura 8 = amarillo + tachado;
- línea temporal de supresión propuesta visible;
- 4.1.7 y todo el contenido posterior permanecen OOXML-idénticos respecto de G;
- Tabla 17 presenta los valores científicos vigentes: 20 casos, 19 con referencia en pool, 1 fuera, Top-1 0.5000/0.5000, Top-3 0.6500/0.6500, Top-5 0.8000/0.8000, MRR 0.6326/0.6326 y distribución RR 0/19/0;
- QA visual externo sobre las páginas 116–119: PASS para legibilidad, ausencia de clipping/solapamiento y continuidad hacia 4.1.7;
- render externo: 148 páginas.

## Hallazgo H1 — descripción activa de la muestra diagnóstica no corregida

El primer párrafo activo de 4.1.6 se heredó sin cambios desde G y sigue afirmando:

> “La muestra incluyó cinco casos con la etiqueta en la primera posición, cinco entre las posiciones 2 y 10, cinco entre las posiciones 11 y 100 y cinco códigos con un único precedente.”

Esta descripción no corresponde a la muestra diagnóstica v0.2 vigente.

La fuente exacta vigente:

```text
outputs/evaluation/diagnostic_llm_reranker_data_aduanas_clase87_v0.2/reranker_diagnostic_sample_v0.2.csv
GIT_BLOB = 916af387acc1308831b776ea6c130932c3881904
```

registra:

```text
selection_rule = uniform_random_sample_without_replacement_over_sorted_case_ids_with_at_least_10_closed_candidates
seed = 0
population = 1056
sample_size = 20
candidate_count = 100
```

Además, `reranker_case_results_v0.2.csv` (`GIT_BLOB = f16270142cd317276eb15ceac37be8fafb51ed7b`) muestra la distribución realmente observada: 10 casos con referencia en posición 1, 9 casos con referencia en posiciones 2–9 y 1 caso con referencia ausente del pool; no existen cinco casos en posiciones 11–100 en la muestra vigente.

La entrada al LLM sí contiene diez candidatos por caso, como confirma:

```text
outputs/evaluation/diagnostic_llm_reranker_data_aduanas_clase87_v0.2/reranker_inputs_v0.2.jsonl
GIT_BLOB = d1f0e6958937026704175f31dea7c88874b71f8c
```

Por tanto, A046 dejó activa una descripción metodológica legacy incompatible con la muestra v0.2. Esto viola el requisito de corregir la prosa desactualizada y la fidelidad científica del bloque.

## Hallazgo H2 — comentario heredado 288 quedó huérfano

En G existían 196 comentarios y cada uno tenía `commentRangeStart`, `commentRangeEnd` y `commentReference`.

En H:

```text
comments.xml = 198 comentarios
commentRangeStart = 197
commentRangeEnd = 197
commentReference = 197
```

Los comentarios nuevos 447 y 448 están correctamente anclados. Sin embargo, el comentario heredado **288** conserva su contenido en `comments.xml` pero perdió los tres anclajes en `document.xml`.

El comentario 288 estaba anclado en G al párrafo legacy de resultados de 4.1.6 y decía:

```text
Resultado diagnóstico provisional. La corrida disponible se ejecutó sobre el pool híbrido anterior y una muestra legacy de 20 casos de varios capítulos, no sobre el conjunto final de clase 87. Debe repetirse con outputs/evaluation/hybrid_pool_data_aduanas_clase87_v0.1/hybrid_pool.csv. Los valores de esta subsección y la contrastación de HE3 pueden cambiar.
```

Por ello las afirmaciones de la respuesta 121H:

```text
ALL_COMMENT_IDS_ANCHORED = true
OUT_OF_SCOPE_COMMENT_MODIFICATIONS = 0
```

no son correctas. El contenido XML del comentario heredado no fue alterado, pero su anclaje sí fue removido, lo que constituye una modificación estructural de un comentario heredado.

## Corrección requerida

R1 debe partir exclusivamente de los artefactos H auditados y limitarse a:

1. corregir el primer párrafo activo de 4.1.6 para reflejar la muestra diagnóstica v0.2 real, conservando el texto legacy visible con amarillo + tachado y añadiendo la redacción vigente con amarillo sin tachado;
2. restaurar los tres anclajes del comentario heredado 288 sobre el texto legacy al que estaba asociado, sin modificar el contenido de `comments.xml` para ese comentario;
3. mantener byte-idénticas las 108 filas de trazabilidad existentes: no añadir nuevas filas;
4. mantener exactamente 198 comentarios: no añadir ni eliminar comentarios;
5. no modificar Tabla 17, Figura 8, 4.1.7 ni ningún bloque posterior salvo lo estrictamente necesario para restaurar el ancla 288;
6. volver a ejecutar QA estructural y visual localizado.

## Estado final de auditoría

```text
A046 = REVISION_REQUIRED
A047 = PASS
PROMPT121H = REVISION_REQUIRED
121I = NOT_AUTHORIZED
```
