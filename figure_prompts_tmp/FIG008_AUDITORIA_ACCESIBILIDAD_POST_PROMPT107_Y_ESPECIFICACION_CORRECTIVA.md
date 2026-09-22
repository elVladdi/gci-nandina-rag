# FIG008 — Auditoría independiente de accesibilidad post-Prompt107 y especificación correctiva

## 0. Rol

Actúa como **IA Diseñadora y Auditora de Figuras Científicas** del proyecto `elVladdi/gci-nandina-rag`.

Tu función en esta tarea es **auditar científicamente y visualmente** las tres figuras vigentes de Grupo 6 después de la integración de G6-F02 y del STOP registrado por Prompt107.

No eres CODEX. No ejecutes scripts, no regeneres SVG/PNG, no modifiques `main`, no integres commits, no edites las figuras y no cierres G6-F03. Debes producir únicamente un **dictamen independiente y una especificación correctiva mínima y completa**, si corresponde.

La finalidad es evitar una nueva corrección parcial: antes de volver a CODEX debe quedar determinado si el problema detectado en G6-FIG-01 es real, si existen otros defectos de accesibilidad/legibilidad que deban corregirse en la misma intervención y qué cambios visuales pueden hacerse sin alterar ningún valor científico.

---

## 1. Estado vinculante de entrada

Trabaja sobre el estado siguiente:

```text
MAIN = 71b13caf6b97e254b4c701b23318bcb0682714bd
G6_F01 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G6_F02 = CLOSED / APPROVED / INTEGRATED_TO_MAIN
G6_F03 = ACTIVE / AUTHORIZED / REVISION_REQUIRED_G6_F02_ARTIFACT
GROUP6 = IN_PROGRESS / NOT_CLOSED
G7_F01 = PROSPECTIVE / NOT_AUTHORIZED / NOT_EXECUTED
```

Prompt107 se detuvo sin crear candidato de G6-F03 porque detectó un posible incumplimiento de accesibilidad en G6-FIG-01.

No cambies estos estados. Tu respuesta es **evidencia de auditoría visual**, no una autorización ni un cierre formal.

---

## 2. Fuentes obligatorias

Consulta directamente en GitHub, como mínimo:

### Registry científico-visual aprobado

```text
outputs/figures/group6/g6_figure_spec_registry_v0.1.json@71b13caf6b97e254b4c701b23318bcb0682714bd
```

### Figuras y scripts vigentes

```text
figures/group6/g6_fig_01_he2.svg@71b13caf6b97e254b4c701b23318bcb0682714bd
figures/group6/g6_fig_01_he2.png@71b13caf6b97e254b4c701b23318bcb0682714bd
src/figures/group6/render_g6_fig_01_he2.py@71b13caf6b97e254b4c701b23318bcb0682714bd

figures/group6/g6_fig_02_phase_e.svg@71b13caf6b97e254b4c701b23318bcb0682714bd
figures/group6/g6_fig_02_phase_e.png@71b13caf6b97e254b4c701b23318bcb0682714bd
src/figures/group6/render_g6_fig_02_phase_e.py@71b13caf6b97e254b4c701b23318bcb0682714bd

figures/group6/g6_fig_03_exp11a.svg@71b13caf6b97e254b4c701b23318bcb0682714bd
figures/group6/g6_fig_03_exp11a.png@71b13caf6b97e254b4c701b23318bcb0682714bd
src/figures/group6/render_g6_fig_03_exp11a.py@71b13caf6b97e254b4c701b23318bcb0682714bd
```

### Ledger

```text
outputs/figures/group6/g6_figure_hash_ledger_v0.1.csv@71b13caf6b97e254b4c701b23318bcb0682714bd
```

### Reporte que originó el STOP

```text
codex_prompts_tmp/107_RESPUESTA_CERRAR_G6_F02_Y_EJECUTAR_G6_F03_CAPTIONS_ACCESIBILIDAD.md@7e46f10ba42dc2ea54562da1c1f0dffb9ee2bf9f
```

### Ficha rectora

```text
docs/fichas/grupos_3_8/grupo_6/G6_F03_CAPTIONS_ACCESIBILIDAD_Y_CIERRE.md@docs/fichas-grupos-3-8
```

Puedes consultar FIG002, FIG003, FIG004 y FIG007 como antecedentes de diseño/auditoría, pero el registry integrado de G6-F01 y los artefactos actuales son la autoridad principal.

---

## 3. Pregunta A — validez del hallazgo bloqueante de G6-FIG-01

Audita independientemente el hallazgo de Prompt107. No lo aceptes por autoridad.

El registry exige para G6-FIG-01:

```text
Minimum effective font size 8 pt
preferred axis/tick 8.5–9 pt
```

Debes determinar:

1. cuál es el menor `font-size` realmente materializado en el SVG actual;
2. en qué elementos aparece;
3. cuáles son las dimensiones `viewBox` y las dimensiones declaradas del SVG;
4. cuáles son las dimensiones de píxel y DPI del PNG actual;
5. cuál es el tamaño físico efectivo de la etiqueta mínima al tamaño nativo de publicación del PNG;
6. si la representación SVG, usando su tamaño declarado actual, satisface o no el mínimo efectivo de 8 pt;
7. si existe alguna interpretación razonable del requisito aprobado bajo la cual el artefacto actual sí cumpla, o si el incumplimiento es inequívoco.

Expón las fórmulas de conversión y los resultados numéricos suficientes para que otra IA pueda reproducir el cálculo.

Clasifica:

```text
FIG01_ACCESSIBILITY_FINDING = CONFIRMED_BLOCKING / NOT_CONFIRMED / AMBIGUOUS_REQUIRES_GOVERNANCE_DECISION
```

No modifiques el artefacto.

---

## 4. Pregunta B — auditoría preventiva completa de accesibilidad de las tres figuras

No te limites al problema ya detectado. Revisa las tres figuras para evitar una nueva secuencia de correcciones fragmentadas.

Para cada figura verifica como mínimo:

```text
minimum_effective_font
axis_label_font
panel_title_font
legend_or_category_font
physical_output_size
contrast_and_legibility
marker_discrimination
color_independence
label_overlap_or_clipping
internal_ids_hidden
axis_baseline_and_scale
caption_readiness
```

### G6-FIG-01

Distingue explícitamente entre:

- requisito obligatorio: mínimo efectivo 8 pt;
- preferencia: ejes/ticks 8.5–9 pt.

Identifica todos los textos que quedarían por debajo del requisito o de la preferencia al tamaño físico del PNG actual.

### G6-FIG-02

El registry establece:

```text
Minimum recommended 9 pt for ticks/legend
at least 10 pt for axis labels
```

Prompt107 confirmó que `Exact-NANDINA coverage` está fuera del campo de datos y alcanza aproximadamente 10.2 pt, pero señaló que otros textos podrían quedar alrededor de 5.4 pt al tamaño físico del PNG.

Debes decidir cuidadosamente:

1. si `minimum recommended 9 pt` es una recomendación no bloqueante o una condición que, por legibilidad real, debe tratarse como corrección necesaria antes de cerrar G6;
2. qué textos concretos no alcanzan la recomendación;
3. si son legibles en un tamaño realista de publicación;
4. si conviene corregirlos en la misma intervención técnica que G6-FIG-01 para evitar deuda visual, aunque no sean por sí solos un incumplimiento formal bloqueante.

No eleves una recomendación a requisito obligatorio sin justificarlo.

### G6-FIG-03

Confirma independientemente:

```text
minimum effective font size >= 8.5 pt
panel titles >= 9.5–10 pt
observations remain discernible
no vertical jitter
no overlap/clipping material
```

Si está conforme, decláralo explícitamente y no propongas cambios cosméticos innecesarios.

---

## 5. Pregunta C — especificación correctiva mínima

Si detectas una o más correcciones necesarias, define un único paquete correctivo consolidado.

Para cada figura afectada especifica:

```text
figure_id
issue_id
severity = BLOCKING / NONBLOCKING_BUT_RECOMMENDED / INFORMATIONAL
current_state
required_target
allowed_visual_changes
forbidden_changes
validation_after_render
```

La corrección debe cumplir:

- cero modificación de datos;
- cero cambio de valores, CI, denominadores, métricas o claims;
- cero cambio de orden por favorabilidad;
- cero nueva inferencia;
- preservar paneles, escalas, rangos, posiciones científicas y semántica de marcas salvo que una redistribución puramente espacial sea imprescindible para legibilidad;
- preservar las restricciones científicas ya aprobadas por G6-F01;
- corregir solo lo necesario para accesibilidad y publicación.

Cuando existan varias soluciones visuales posibles, recomienda una principal y explica por qué es la menos invasiva.

No escribas código.

---

## 6. Pregunta D — actor siguiente

Determina el actor correcto después de esta auditoría:

```text
NEXT_ACTOR = CODEX / IA_EXPERIMENTAL / NONE
```

Usa `CODEX` únicamente si la corrección exige modificar scripts/renderizar archivos/actualizar ledger y artefactos versionados.

Si concluyes que no existe corrección técnica necesaria, usa `IA_EXPERIMENTAL` para que decida la reanudación de G6-F03.

---

## 7. Prohibiciones

No:

- modificar GitHub salvo publicar tu archivo de respuesta;
- editar figuras;
- regenerar SVG/PNG;
- ejecutar G6-F03;
- crear captions finales;
- cerrar Grupo 6;
- activar G7;
- modificar tesis o artículo;
- reabrir EXP12;
- recalcular resultados científicos;
- crear nuevas métricas o inferencia;
- diseñar nuevas figuras;
- sustituir el registry aprobado por preferencias personales.

---

## 8. Salida obligatoria

Publica tu respuesta en:

```text
figure_prompts_tmp/FIG008_RESPUESTA_AUDITORIA_ACCESIBILIDAD_POST_PROMPT107_Y_ESPECIFICACION_CORRECTIVA.md
```

La respuesta debe contener, en este orden:

1. `DICTAMEN_TERMINAL`;
2. fuentes exactas revisadas;
3. auditoría independiente de G6-FIG-01;
4. auditoría preventiva de G6-FIG-02;
5. auditoría preventiva de G6-FIG-03;
6. matriz consolidada de hallazgos;
7. especificación correctiva mínima;
8. actor siguiente;
9. declaraciones de no-ejecución/no-modificación.

Usa una de estas clasificaciones terminales:

```text
ACCESSIBILITY_CORRECTION_REQUIRED
ACCESSIBILITY_PASS_NO_CORRECTION_REQUIRED
ACCESSIBILITY_GOVERNANCE_DECISION_REQUIRED
```

No declares `GROUP6=CLOSED`, `G6_F03=APPROVED` ni autorización de G7.
