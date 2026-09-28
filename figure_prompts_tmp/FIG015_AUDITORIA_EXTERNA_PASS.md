# FIG015 — Auditoría externa de IA Experimental

## Dictamen

```text
FIG015_EXTERNAL_AUDIT = PASS
FIGURE_6_CANDIDATE_APPROVED_FOR_DOCX_INTEGRATION = true
FIGURE_6_CANDIDATE_COMMIT = 78894c96cd59df36673def8647db88c96d50f953
FIGURE_6_PNG_GIT_BLOB = 667765204adbdb7ab7567e9546f6ed8c71051d91
FIGURE_6_PNG_SHA256 = 4eeb3a63d4bb8a22c5b00f6d3efe4d2733c2caeec52373fa7e1c05ac27a24ae3
FIGURE_6_SVG_GIT_BLOB = f6b4a1459b70daa5e2106dc6cd999a12668131a8
FIGURE_6_SVG_GIT_SHA256 = 780cbf167cb597ebd7e644638a5a3b5c648b47299dfdf8b66b357014a4549584
SCIENTIFIC_DATA_CHANGE = false
SCIENTIFIC_GEOMETRY_CHANGE = false
NON_TEXT_SVG_GEOMETRY_MATCH = true
OBSERVED_RUN_COUNT = 31
RENDERED_POINT_COUNT = 186
DETERMINISTIC_RERUN_MATCH = true
H100_VISIBLE_LABEL = H100 (ref.)
H100_OVERLAP_WITH_H75 = false
THESIS_VISIBLE_INTERNAL_IDS = NONE
G6_PROTECTED_ARTIFACTS_UNCHANGED = true
FIGURE_4_CANDIDATE_UNCHANGED = true
FIGURE_5_CANDIDATE_UNCHANGED = true
DOCX_MODIFIED = false
A043_EXECUTED = false
121G_AUTHORIZED = false
G7_F02 = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
G7_F03_AUTHORIZED = false
```

## Verificación independiente

Se auditó la respuesta `figure_prompts_tmp/FIG015_RESPUESTA_REGENERAR_FIGURA6_TESIS_TRAS_RESOLVER_H100_G7_F02.md` y las salidas candidatas de la rama `codex/prompts-temporary` contra FIG012, FIG014 y el prompt FIG015.

### 1. Alcance y commit

La rama quedó en `78894c96cd59df36673def8647db88c96d50f953`, hijo directo del commit de autorización FIG015 `c028b0a8ad1a7e7e3005ab635d60475d64a6a3a5`. La comparación entre ambos commits muestra exactamente cinco archivos añadidos y ningún archivo modificado o eliminado:

1. `src/figures/group7/render_g7_thesis_fig_06_sensitivity.py`;
2. `figures/group7/g7_thesis_fig_06_sensitivity.svg`;
3. `figures/group7/g7_thesis_fig_06_sensitivity.png`;
4. `outputs/figures/group7/g7_thesis_fig_06_sensitivity_manifest_v0.1.json`;
5. `figure_prompts_tmp/FIG015_RESPUESTA_REGENERAR_FIGURA6_TESIS_TRAS_RESOLVER_H100_G7_F02.md`.

Esto confirma que no se modificaron DOCX, fuentes científicas G6, Figuras 4–5 ni otros artefactos fuera de alcance.

### 2. Renderer y fuentes congeladas

El renderer candidato obtiene el renderer G6 y las tres fuentes científicas mediante `git show` contra `REF_G6=e93b44164a9619dad1f527a3b2d4479265858e39`, verifica sus blobs y SHA-256, y aplica sustituciones exactas solo sobre cadenas de texto y nombres de archivos de salida. Las rutinas de agrupación, condiciones, jitter, cálculo de coordenadas y dibujo provienen del renderer G6 congelado.

La sustitución `Top* -> Top-*` afecta únicamente la presentación textual de las métricas. La condición científica subyacente sigue siendo `H100 ref.` para la lógica del renderer, pero el nodo visible se transforma exactamente a `H100 (ref.)`; no cambia la posición de la categoría ni la marca H100.

El propio renderer compara el SVG candidato con el SVG G6 excluyendo únicamente nodos `<text>`/`<tspan>` y falla si existe cualquier diferencia no textual.

### 3. SVG candidato e invariantes científicas

La inspección independiente del SVG candidato confirma:

- lienzo `1200 × 800`;
- seis paneles: `Top-1`, `Top-3`, `Top-5`, `Top-10`, `Top-50` y `MRR`;
- cinco condiciones en el orden `H25 | H50-D1 | H50-D2 | H75 | H100`;
- escala visible `0.00–1.00` en los seis paneles;
- separador antes de H100 conservado;
- H100 representado por diamante sólido;
- demás corridas representadas por círculos abiertos;
- ninguna línea de conexión entre condiciones;
- ausencia de CI, valores p, regresiones, suavizados y summary marks;
- rótulo `H100 (ref.)` a `14.5` unidades SVG, centrado en la posición original;
- título, subtítulo, paneles y nota inferior naturalizados al español;
- ausencia visible de `EXP11A`, IDs G3–G6, prompts, gates, commits, blobs o lenguaje de gobernanza.

La secuencia de 31 corridas repetida en seis paneles produce 186 marcas científicas, coherente con el inventario congelado `10 + 5 + 5 + 10 + 1 = 31`.

### 4. Resolución del bloqueo H100

FIG014 fijó `H100 (ref.)` como solución mínima. El candidato cumple exactamente esa decisión: misma fuente, misma posición, mismo anclaje y una sola línea. No se aplicó ningún ajuste tipográfico local adicional. La holgura respecto de H75 permanece positiva y no se altera la posición científica de ninguna categoría o marca.

El caption completo debe conservar posteriormente en el DOCX la forma explícita `H100 (n=1, referencia congelada)`; la abreviatura pertenece solo al rótulo visual.

### 5. Determinismo, hashes y manifest

El manifest registra dos ejecuciones consecutivas idénticas del renderer para SVG y PNG. También registra `scientific_data_change=false`, `scientific_geometry_change=false`, `non_text_svg_geometry_match=true`, `observed_run_count=31`, `rendered_point_count=186` y las identidades de las Figuras 4–5 protegidas.

Identidades aprobadas del candidato:

```text
RENDERER
Git blob = b433fa5d45246ee22bae324835cdc9ff15c744cf
SHA256 = 76d93530e802629985a85619bac9932598b465674f66a8d1bd3ee37169142c0b

SVG Git/LF
Git blob = f6b4a1459b70daa5e2106dc6cd999a12668131a8
SHA256 = 780cbf167cb597ebd7e644638a5a3b5c648b47299dfdf8b66b357014a4549584

SVG checkout/CRLF
SHA256 = 6c0aa9502070b1fb9b04bfdf01e40df1e7a45d7d02db86f851cf7fd15e194c9b

PNG
Git blob = 667765204adbdb7ab7567e9546f6ed8c71051d91
SHA256 = 4eeb3a63d4bb8a22c5b00f6d3efe4d2733c2caeec52373fa7e1c05ac27a24ae3
PNG = 3000 × 2000 px / 300 dpi nominal
```

La diferencia de SHA del SVG entre checkout Windows y Git corresponde únicamente a normalización CRLF/LF y está registrada explícitamente; no es una diferencia del contenido gráfico.

## Consecuencia de gobernanza

El candidato de Figura 6 queda **aprobado para integración posterior en REVIEW V03**. La integración debe realizarla la **IA de Redacción Científica**, no CODEX, siguiendo la convención REVIEW V03: preservar la Figura 6 legacy y su numeración oficial, marcar el caption legacy como superseded, insertar una propuesta claramente temporal sin crear un nuevo `SEQ Figura`, insertar el PNG aprobado y añadir el caption completo y comentario de trazabilidad.

A043 todavía no se considera ejecutado hasta que la integración en el DOCX sea completada y auditada externamente. `121G` permanece no autorizado hasta ese cierre.
