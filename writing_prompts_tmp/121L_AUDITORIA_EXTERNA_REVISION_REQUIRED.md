# 121L — Auditoría externa — REVISION_REQUIRED

## Dictamen

```text
PROMPT121L_EXTERNAL_AUDIT = REVISION_REQUIRED
A061_EXTERNAL_AUDIT = PASS / VERIFIED_NO_CHANGE
A062_EXTERNAL_AUDIT = PASS
A063_EXTERNAL_AUDIT = PASS
A064_EXTERNAL_AUDIT = PASS
A065_EXTERNAL_AUDIT = REVISION_REQUIRED
A066_EXTERNAL_AUDIT = PASS
A067_EXTERNAL_AUDIT = PASS
121M_AUTHORIZED = false
G7_F02 = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
G7_F03_AUTHORIZED = false
```

La ejecución 121L es materialmente correcta en ciencia, alcance, estructura OOXML, trazabilidad acumulativa y presentación visual. No puede recibir PASS externo todavía porque el comentario Word 465, obligatorio para A065, contiene una descripción inexacta del cambio realizado en la Tabla 23. La corrección requerida es exclusivamente documental y no exige modificar la prosa visible de la tesis, la Tabla 23, el CSV L, las figuras ni ningún resultado científico.

## Artefactos auditados

```text
Molleapasa_gv_G7F02_REVIEW_V03_L.docx
SHA256 = 01599c2b012964dc934daa43cdf831e10598a97d7c9fd642b1ef9190df8caebe
SIZE = 4685977

g7_thesis_claim_traceability_v0.3_L.csv
SHA256 = d6d27bf608f141ff490fa2c91f73d3e28c0637e5a94107abd0aae64f6362d5ee
SIZE = 123152
ROWS = 128
```

La respuesta oficial auditada es:

```text
writing_prompts_tmp/121L_RESPUESTA_G7_F02_V03_BLOQUE_L_4_3_DISCUSION_RESULTADOS.md
commit = 3819d394caca49889898747d8b5f9298b6b07dd6
blob = 8fd3272c01864190bdd0bbb82a3457633d23c01c
```

## Verificaciones que pasan

La auditoría independiente confirmó:

- identidad SHA-256 y tamaño de ambos artefactos L;
- 128 filas de trazabilidad: las 121 heredadas permanecen byte-idénticas como prefijo y se añadieron exactamente siete filas, A061–A067;
- A061 registrado como `VERIFIED_NO_CHANGE` con `comment_id` vacío;
- 24 objetos de tabla, 12 campos `SEQ Figura` y 16 archivos de medios;
- `w:del = 0` y `w:ins = 0`;
- 217 comentarios: 211 heredados + seis nuevos, IDs 462–467;
- cada comentario no vacío conserva `commentRangeStart`, `commentRangeEnd` y `commentReference`;
- los comentarios heredados permanecen estructuralmente intactos;
- 4.2 permanece idéntico a K y `CONCLUSIONES` y todo el contenido posterior permanecen idénticos a K;
- no existen modificaciones visibles ni de comentarios fuera del alcance 4.3;
- no se añadieron referencias, medios ni campos de numeración de figuras;
- Tabla 22 permanece sin cambios, como el mismo objeto de 8 × 4;
- Tabla 23 permanece como el mismo objeto de 9 × 4 y conserva `tblPr`, `tblGrid`, propiedades de fila y propiedades de celda;
- en Tabla 23 cambiaron únicamente las celdas de la columna `Relación con el piloto` que dependían de resultados propios desactualizados; las columnas `Antecedente`, `Hallazgo relevante` y `Límite de comparación` permanecen sin cambios;
- la frase previa a Tabla 23 que contiene `La Tabla 24 resume...` permanece sin corregir, como exigía la postergación de A082;
- Tabla 24 permanece como el mismo objeto de 11 × 4 y solo actualiza las filas autorizadas;
- Figuras 11 y 12 permanecen intactas, sin medio nuevo ni deformación;
- la ciencia de A062–A067 respeta el benchmark interno de 1 056 series / 67 DAM / 42 NANDINA, la separación funcional del ranking histórico, la evidencia normativa y la explicación, la naturaleza diagnóstica del reranker, la lectura vigente de HE4, HE5 y reproducibilidad, y los límites de comparabilidad bibliográfica;
- no se detectó SOTA, novelty absoluta, generalización externa, equivalencia entre auditabilidad y corrección jurídica, ni reapertura de EXP12;
- QA visual independiente de la sección 4.3, Tablas 22–24, Figuras 11–12 y el límite con `CONCLUSIONES`: PASS; no se observaron clipping, overflow, solapamiento ni distorsión material.

## Hallazgo L1 — comentario 465 describe un cambio que no ocurrió

El comentario Word 465, correspondiente a A065, contiene en su apartado obligatorio `Cambio exacto:` la formulación:

```text
Cambio exacto: Se actualizan únicamente las celdas propias de relación y límite de comparación de la misma Tabla 23, además de una interpretación inmediata, preservando antecedentes y referencias bibliográficas.
```

Esta frase no coincide con la modificación realmente realizada.

La comparación OOXML independiente entre K y L demuestra que en la Tabla 23 se modificaron únicamente las celdas de la columna `Relación con el piloto`; la columna `Límite de comparación` permaneció inalterada. La respuesta oficial de 121L declara lo mismo: se modificaron exclusivamente celdas de `Relación con el piloto` y se preservó la columna de límites de comparación.

Por tanto, el comentario 465 incumple el contrato de comentario auditable que exige que `Cambio exacto:` describa de forma precisa el cambio visible real. El defecto no afecta la ciencia de la tesis ni el contenido visible de A065, pero sí afecta la fidelidad de la trazabilidad editorial obligatoria de REVIEW V03.

## Corrección requerida

121L-R1 debe partir exclusivamente de los artefactos L auditados y limitarse a:

1. conservar sin cambios todo el contenido visible del DOCX L;
2. conservar la Tabla 23 y todas sus celdas byte/OOXML-equivalentes respecto de L;
3. conservar el mismo comentario 465, su ID y sus tres anclajes;
4. modificar únicamente el texto del apartado `Cambio exacto:` del comentario 465 para que indique que se actualizaron las celdas de `Relación con el piloto` dependientes de resultados propios desactualizados y la interpretación inmediata asociada, preservando los antecedentes, las referencias bibliográficas y la columna `Límite de comparación`;
5. mantener sin cambios los otros cinco apartados del comentario 465 salvo que sea estrictamente necesario ajustar una concordancia gramatical derivada de la corrección anterior; no añadir secciones;
6. no añadir, eliminar, renumerar ni desanclar comentarios;
7. no modificar el CSV L: debe copiarse byte-idéntico, con 128 filas y el mismo SHA-256;
8. no ejecutar A068–A082, Conclusiones, Recomendaciones, 121M ni bloques posteriores;
9. volver a verificar estructura y QA visual localizado, aunque no se espera cambio visible en la tesis.

## Estado final de auditoría

```text
PROMPT121L = REVISION_REQUIRED
A061 = PASS / VERIFIED_NO_CHANGE
A062 = PASS
A063 = PASS
A064 = PASS
A065 = REVISION_REQUIRED
A066 = PASS
A067 = PASS
121M = NOT_AUTHORIZED
```
