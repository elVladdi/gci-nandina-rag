# Auditoría externa — PROMPT121E-FIG45

## Dictamen

```text
PROMPT121E_FIG45_EXTERNAL_AUDIT = REVISION_REQUIRED
FULL_RERUN_REQUIRED = false
TARGETED_REVISION_REQUIRED = true
SCIENTIFIC_DATA_CORRECTION_REQUIRED = false
FIGURE_BINARY_CORRECTION_REQUIRED = false
121F_AUTHORIZED = false
G7_F02 = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
G7_F03_AUTHORIZED = false
```

La integración conserva correctamente los binarios científicos aprobados y respeta el alcance estructural, pero el DOCX/CSV entregado no cumple literalmente varias obligaciones del prompt `121E_FIG45_INTEGRAR_FIGURAS_4_5_REVIEW_V03.md`.

## Entradas auditadas

### Baseline acumulativo E

```text
Molleapasa_gv_G7F02_REVIEW_V03_E.docx
SHA256 = f6eb5a9f4db80faa36306df64ec51ddd865df2a081d69f65ca6a3e063ec2b7ba
SIZE = 4199560

g7_thesis_claim_traceability_v0.3_E.csv
SHA256 = c8bd644af8b660269f6bb7ea6f7cebf615ad9a3d23a42ac9a2814949ae8be05f
SIZE = 87358
ROWS = 99
```

### Entregables efectivamente auditados

```text
Molleapasa_gv_G7F02_REVIEW_V03_E_FIG45.docx
SHA256 = e77e20a496b4075c14645005126637dfd0d8ed13201f52583b103d4147ed4897
SIZE = 4569156

g7_thesis_claim_traceability_v0.3_E_FIG45.csv
SHA256 = 9b8b81f0856bc1e23a861af1eda0c547eebc00ecbe49aed91ff8dee4e34db673
SIZE = 89000
ROWS = 101
```

## Verificaciones que pasan

1. Las 99 filas heredadas del CSV son idénticas y se agregan exactamente 2 filas.
2. Los 189 comentarios heredados permanecen byte-lógicamente sin cambio; se agregan solo los IDs 440 y 441.
3. Hay 191 `commentRangeStart`, 191 `commentRangeEnd` y 191 `commentReference`, con conjuntos de IDs coincidentes y sin huérfanos.
4. `w:del = 0`.
5. El documento mantiene 24 objetos de tabla.
6. Continúan existiendo exactamente 12 campos `SEQ Figura`; no se creó un segundo `SEQ` para las propuestas.
7. Solo se agregaron dos imágenes al paquete DOCX y sus SHA-256 coinciden exactamente con los candidatos aprobados:

```text
word/media/image14.png
SHA256 = 5cde004fc5b3b76578de02bd9d4751c52d26f921821c96a0bafc1cac65c1eb1e

word/media/image15.png
SHA256 = aecc77e8fd6272766eaf9f7a72d6bc531ef45d448264cac1b95a2ac30edd59c0
```

8. La comparación E → E_FIG45 muestra cambios visibles confinados a los dos captions legacy y a seis párrafos insertados en los bloques de Figuras 4–5. No se identificaron modificaciones visibles fuera de ese alcance.
9. Los captions legacy permanecen visibles con amarillo + tachado.
10. El render localizado no presenta clipping, deformación, superposición ni alteración material de 4.1.4.

## Hallazgos que impiden PASS

### H1 — Línea temporal obligatoria incorrecta y sin resaltado

El prompt exige literalmente, para ambas figuras:

```text
PROPUESTA DE REEMPLAZO DEL ELEMENTO GRÁFICO ANTERIOR — NO ES NUMERACIÓN FINAL
```

resaltada en amarillo y con estilo normal/no-caption.

El DOCX auditado contiene en cambio:

```text
Propuesta de actualización de Figura 4 para revisión editorial de tesis (sin cambio de datos).
Propuesta de actualización de Figura 5 para revisión editorial de tesis (sin cambio de datos).
```

Ambos párrafos carecen de `w:highlight` amarillo. Esto viola directamente el apartado 4.5 del prompt.

### H2 — Caption propuesto de Figura 4 incompleto

El prompt exige el caption final completo y exacto del apartado 5. El DOCX contiene únicamente:

```text
Evidencia primaria de HE2: comparación del desempeño temprano y la cobertura profunda entre la recuperación histórica y los comparadores normativos.
```

Faltan el número y denominación completa, la población 1 056/67/42, la explicación de paneles A/B/C, los 15 contrastes con IC 99 %, el contraste Recall@200 − Recall@100 con IC 95 %, ausencia de valores p, límites no causales y prohibiciones interpretativas.

### H3 — Caption propuesto de Figura 5 incompleto

El prompt exige el caption final completo y exacto del apartado 6. El DOCX contiene únicamente:

```text
Cobertura exacta NANDINA según profundidad y variante.
```

Faltan la población, las cinco variantes y tres profundidades, el carácter descriptivo, la condición contextual de 70/30, ausencia de IC/p-values/tendencias, exclusión de la unión diagnóstica del rendimiento ordinario y límites sobre favorabilidad/HE2.

### H4 — Comentario 440 incompleto respecto del contenido mínimo obligatorio

El comentario 440 sí contiene los seis encabezados, pero no consigna los elementos mínimos exigidos: 15 contrastes con IC 99 %, un contraste profundo con IC 95 %, ausencia de p-values y de IC por brazo, ni los límites explícitos de exactitud global del RAG y corrección jurídica.

### H5 — Comentario 441 incompleto respecto del contenido mínimo obligatorio

El comentario 441 sí contiene los seis encabezados, pero no declara que la quinta variante es solo contexto descriptivo adicional ni que la unión diagnóstica no representa rendimiento ordinario, ambos requisitos expresos del prompt.

### H6 — Las dos filas nuevas de trazabilidad no usan A039/A040 ni `FIGURE_UPDATE`

Las filas nuevas registran:

```text
plan_id = FIG010
change_type = FIGURE_REVIEW_INSERT
```

El prompt exige exactamente:

```text
A039 = Figura 4
A040 = Figura 5
action = FIGURE_UPDATE
```

Por tanto, la trazabilidad no refleja el contrato de ejecución aunque sus demás campos y los blobs de imagen sean correctos.

### H7 — La respuesta oficial publicada no identifica los binarios realmente auditados

La respuesta en GitHub (commit `c5aebdf20fb83a85f7e08dfcfbecda04804728a4`) declara:

```text
DOCX SHA256 = 341cc3ab126345a7ec6681cbb9896e93b3032e2cbd4efbf29cb091599fc5edea
DOCX size = 4570250
CSV SHA256 = bffbe01c94ba240e914e4b3f487ca78bcad615fc5f62ea586267682c697dba20
CSV size = 89295
```

Los archivos entregados para auditoría tienen identidades distintas (`e77e20...` / `4569156` y `9b8b81...` / `89000`). La respuesta oficial debe actualizarse después de la corrección localizada para cerrar la trazabilidad binaria.

## QA visual

Render independiente con LibreOffice: 141 páginas. Se inspeccionaron las páginas 100–108, incluyendo las páginas frontera, ambas figuras legacy, las dos propuestas, los captions propuestos y el inicio de 4.1.4.

Resultado visual físico: `PASS_WITH_EDITORIAL_CONTRACT_DEFECTS`.

Las imágenes nuevas son legibles y mantienen proporciones. Los defectos son contractuales/editoriales, no de geometría científica ni de render.

## Corrección requerida

No se autoriza reejecución completa. Debe ejecutarse una revisión R1 localizada sobre el candidato auditado, preservando:

- las dos imágenes PNG ya insertadas;
- las dos figuras legacy;
- los captions legacy y su marcado;
- los IDs de comentario 440 y 441;
- las 99 filas heredadas de trazabilidad;
- tablas, secciones y contenido fuera de Figuras 4–5.

R1 debe corregir exclusivamente las líneas temporales, captions completos, contenido de comentarios 440/441, las dos filas nuevas del CSV y la respuesta oficial/hashes.

```text
NEXT_ACTION = PROMPT121E_FIG45_R1
121F_AUTHORIZED = false
```
