# FIG011A — Auditoría externa de Figura 4 candidata para G7-F02

```text
FIG011A_EXTERNAL_AUDIT = PASS
FIGURE_4_CANDIDATE = APPROVED_FOR_LATER_DOCX_INTEGRATION
SCIENTIFIC_DATA_CHANGE = false
NON_TEXT_SVG_GEOMETRY_MATCH = true
DETERMINISTIC_RERUN_MATCH = true
THESIS_VISIBLE_INTERNAL_IDS = NONE
G6_PROTECTED_ARTIFACTS_UNCHANGED = true
DOCX_MODIFIED = false
FIGURE_5_EXECUTED = false
121F_AUTHORIZED = false
NEXT_STEP = FIG011B
```

## Alcance auditado

Se auditó el candidato técnico generado por FIG011A en `codex/prompts-temporary`:

- `src/figures/group7/render_g7_thesis_fig_04_he2.py`
- `figures/group7/g7_thesis_fig_04_he2.svg`
- `figures/group7/g7_thesis_fig_04_he2.png`
- `outputs/figures/group7/g7_thesis_fig_04_he2_manifest_v0.1.json`
- `figure_prompts_tmp/FIG011A_RESPUESTA_REGENERAR_FIGURA4_TESIS_G7_F02.md`

La revisión se realizó contra la especificación vinculante FIG010, el renderer G6 congelado y las dos fuentes numéricas G5 congeladas.

## Identidad y reproducibilidad

La respuesta final de FIG011A fija como candidato:

```text
SCRIPT_GIT_BLOB = b22d25d41fa9014180fd63a36715942414e779a0
SCRIPT_SHA256_LF = 2af80603d59ef6690fa3e63f7e6e5daea21cb1326e186a56470f35f562a84442

SVG_GIT_BLOB = e84fa3ee6aaedb2d3d24b59ce7255214621aae3f
SVG_SHA256_LF = 6946594f2543f4dced0e2f19ee73b8adc5e7fa3a2fdb92f7c68cb55f0e1e93b9

PNG_GIT_BLOB = eb77a4f2289a8701d22ba399d9432defd2092e2a
PNG_SHA256 = 5cde004fc5b3b76578de02bd9d4751c52d26f921821c96a0bafc1cac65c1eb1e
```

La aclaración posterior sobre LF/CRLF es consistente: distingue el hash del blob Git del archivo materializado en Windows sin cambiar el candidato científico ni gráfico.

## Fidelidad científica

PASS. El script candidato obtiene el renderer G6 y las dos tablas G5 exclusivamente desde `main = db0d0ad0d8435921a7838db6720eaea86a263763`, valida los blobs congelados y reutiliza la lógica G6. La adaptación intercepta únicamente `Canvas.text` y el nombre de salida; no sustituye funciones de líneas, marcadores, ejes, intervalos ni mapeo de datos.

Se preservan:

- tres paneles A/B/C;
- cinco métricas en el orden Top-1, Top-3, Top-5, Top-10, MRR@100;
- tres comparadores;
- ausencia de IC por brazo en A;
- quince diferencias pareadas y sus IC congelados del 99 % en B;
- un único contraste `Recall@200 − Recall@100` con IC congelado del 95 % en C;
- ausencia de valores p;
- EVAL = 1 056 series, 67 DAM y 42 NANDINA;
- escalas, ticks, zero-lines, marcas e intervalos no textuales.

El manifest registra `non_text_svg_geometry_match=true` para 115 elementos no textuales y no existe evidencia de recalculo científico.

## Adecuación editorial para tesis

PASS. El SVG candidato elimina de la figura visible los identificadores internos y rótulos ingleses que FIG010 prohibió. En particular no aparecen `Attempt06`, `D1a`, `Historical`, `Flat`, `Hierarchical`, `Observed values`, `Paired difference`, `frozen` ni `Offline internal benchmark` como rótulos originales.

La terminología visible queda naturalizada, entre otros, como:

- `Recuperación histórica`;
- `BM25 normativo plano`;
- `BM25 normativo jerárquico`;
- `Recuperador denso entrenado con MNRL`;
- `Diferencia pareada`;
- `Recall@200 − Recall@100 (IC del 95 %)`.

Los saltos de línea introducidos son exclusivamente tipográficos. La revisión de coordenadas del SVG confirma que los rótulos largos se mantienen separados de las marcas/intervalos y dentro del canvas. El tamaño mínimo efectivo reportado es 8,1 pt, por encima del umbral de 8 pt.

## Protección de artefactos y alcance

PASS. Los artefactos G6 permanecen protegidos; el candidato se creó en rutas nuevas de `group7`. No se modificó el DOCX, no se creó Figura 5 y no se ejecutó 121F.

## Dictamen

Figura 4 candidata aprobada para integración posterior en la copia de revisión de la tesis. La integración en Word continúa bloqueada hasta disponer también de una Figura 5 candidata auditada. El siguiente paso autorizado es exclusivamente FIG011B para regenerar editorialmente Figura 5.