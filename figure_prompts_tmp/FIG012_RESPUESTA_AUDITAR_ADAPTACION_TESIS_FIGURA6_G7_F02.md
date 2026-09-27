# FIG012 — Respuesta: auditoría de adaptación para tesis de Figura 6 / G7-F02

## 0. Alcance ejecutado

Se ejecutó exclusivamente `figure_prompts_tmp/FIG012_AUDITAR_ADAPTACION_TESIS_FIGURA6_G7_F02.md@c5935e52e51069e376a13003613297689d984a0b` bajo el rol de **IA Diseñadora y Auditora de Figuras Científicas**.

No se modificó el DOCX, no se regeneró SVG/PNG, no se modificaron scripts, no se ejecutó A043 y no se ejecutó 121G ni ningún bloque posterior.

Se verificó la copia acumulativa vigente sin modificarla:

```text
Molleapasa_gv_G7F02_REVIEW_V03_F.docx
SHA256 = c630bcc51b33b79e2d0d9fdfc92f2701816dd29116e3051d54f28a713f71216b
SIZE = 4572575 bytes
```

El cierre externo gobernante de 121F fue leído en `writing_prompts_tmp/121F_AUDITORIA_EXTERNA_PASS.md@625709b627f62fbcb7090282552ef96e11726b85` y confirma que A041/A042 están completos, que A043 sigue diferida al flujo de figuras y que 121G no está autorizado.

---

## 1. Fuentes verificadas

Se leyeron las fuentes exigidas por FIG012:

- `docs/writing/group7/g7_writing_source_freeze_v0.1.json@d91298758dba674003bf650e7a303c36bd0b74d9`.
- `outputs/figures/group6/g6_figure_spec_registry_v0.1.json`, blob `44cc30fc3c38639c6aa4370cb6f317458041f1b1`.
- `docs/figures/group6/g6_caption_registry_v0.1.md`, blob `0dcb43cfa56dfce2e6955f960184069beb36ba76`.
- `outputs/figures/group6/g6_figure_hash_ledger_v0.1.csv`, blob `bfcbfe8a2232246476979506377ff3005166253f`.
- `figure_prompts_tmp/FIG004_RESPUESTA_ESPECIFICACION_CIENTIFICO_VISUAL_G6_FIG_03_EXP11A.md@89d95744b2ab446245a5522eefc8279f673a8a7c`, blob `b30c4c98d735207d028224fc7965aedeef2d88c9`.
- `outputs/results/group5/tables/g5_appendix_02_exp11a_size_composition_sensitivity.csv`, blob `cf3aedab5935d6af9b3ac7be7b51b954fcb9c403`.
- `outputs/experiments/exp11a_historical_size_sensitivity_v0.3/exp11_metrics_by_run.csv`, blob `9b434d7e09e6db7e9de061953b59c53aac2337ad`.
- `outputs/experiments/exp11a_historical_size_sensitivity_v0.3/exp11_metrics_by_condition.csv`, blob `535dd377d107ddcbf09ecaa13cd66ca723ee738d`.

También se inspeccionaron el SVG aprobado, su renderer determinista y la identidad registrada del PNG:

```text
figures/group6/g6_fig_03_exp11a.svg
SHA256 = a4a81b565ed2ceb22f23f9a52888e802b1e749186fb43d3bd71faf1b31d5f7c3

figures/group6/g6_fig_03_exp11a.png
SHA256 = 3c4bcf736b56fbc9ffd054562db0eea31be195792f2bade611a9e5205dfa97de
PNG = 3000 x 2000 px / 300 dpi
```

El renderer `src/figures/group6/render_g6_fig_03_exp11a.py` confirma que SVG y PNG comparten exactamente la misma geometría científica y el mismo inventario de puntos; la diferencia entre ambos es únicamente el formato de salida.

---

## 2. Dictamen principal

El binario G6-FIG-03 **no debe insertarse tal cual en la tesis**.

La razón no es científica ni geométrica. El artefacto aprobado conserva texto visible propio de la fase experimental/interna y parcialmente en inglés:

```text
EXP11A joint size-composition sensitivity
Observed runs only; descriptive and noncausal; no summaries, CI, p-values, or fitted trends
Conditions are categorical observed banks; H100 is one frozen reference. Size and composition vary jointly.
```

Además, el caption G6 aprobado contiene el identificador `EXP11A`, que no corresponde a la capa visible final de una tesis en español.

Por tanto:

```text
FIGURE_6_EXISTING_G6_BINARY_USABLE_AS_IS = false
FIGURE_6_ADAPTATION_REQUIRED = true
SCIENTIFIC_DATA_CHANGE_REQUIRED = false
SCIENTIFIC_GEOMETRY_CHANGE_REQUIRED = false
```

La adaptación requerida es exclusivamente editorial y textual.

---

## 3. Contenido científico que debe permanecer idéntico

La futura adaptación debe conservar sin cambio:

1. **Seis paneles**, en orden `Top1`, `Top3`, `Top5`, `Top10`, `Top50`, `MRR`.
2. **31 corridas observadas** y ninguna fila summary como marca.
3. Inventario visible exacto:
   - H25: 10 corridas;
   - H50-D1: 5 corridas;
   - H50-D2: 5 corridas;
   - H75: 10 corridas;
   - H100: 1 referencia congelada.
4. Los mismos valores y coordenadas verticales de todos los puntos.
5. El mismo jitter horizontal determinista, asignado por `run/seed` y repetido idénticamente en los seis paneles.
6. Círculo abierto para las corridas observadas y diamante sólido para la única referencia H100.
7. Orden categórico fijo `H25 | H50-D1 | H50-D2 | H75 | H100`, no determinado por favorabilidad.
8. Separador visual antes de H100.
9. Escala lineal `[0,1]` en los seis paneles, sin truncamiento.
10. Ausencia de líneas de conexión entre condiciones.
11. Ausencia de CI, valores p, regresiones, suavizados, interpolaciones, boxplots, violines o summaries como marcas.
12. Interpretación exclusivamente descriptiva y no causal: tamaño y composición cambian conjuntamente.
13. HE5 permanece `INCONCLUSIVE`; esta figura no redefine HE5 ni constituye evidencia confirmatoria de desempeño global.

No se autoriza recomputación, nuevo agregado ni cambio de fuerza del claim.

---

## 4. Semántica verificada de las condiciones H25/H50/H75/H100

Los códigos no deben interpretarse solo a partir de su nombre. La semántica se contrastó contra las fuentes congeladas de corridas y condiciones.

La fuente de hallazgos define el experimento como sensibilidad del retrieval histórico al **tamaño nominal del banco histórico bajo muestreo por DAM completas y restricciones de composición del H100 congelado**. La fuente por corrida muestra además las fracciones realizadas y la composición de cada banco.

Resumen verificable:

| Código | Rol verificable | Corridas | Tamaño observado en series | Observación composicional |
|---|---|---:|---:|---|
| H25 | condición nominal reducida | 10 | 727–767 | composición observada variable por corrida |
| H50-D1 | condición nominal intermedia, composición D1 | 5 | 1 404–1 492 | `dominant_stratum=D1` documentado |
| H50-D2 | condición nominal intermedia, composición D2 | 5 | 1 409–1 532 | `dominant_stratum=D2` documentado |
| H75 | condición nominal ampliada | 10 | 2 156–2 286 | composición observada variable por corrida |
| H100 | referencia completa congelada | 1 | 2 950 | 28 DAM; `realized_fraction=1.0`; referencia única |

Las fracciones realizadas de las condiciones reducidas no son idénticas en todas las corridas porque el diseño conserva DAM completas. Por ello **no se recomienda sustituir los códigos por etiquetas visuales simples `25 %`, `50 %`, `75 %` y `100 %`**, ya que ello sugeriría tamaños exactos homogéneos y ocultaría la variación composicional.

### Decisión de etiquetas

Se recomienda **mantener `H25`, `H50-D1`, `H50-D2`, `H75` y `H100` como identificadores científicos de condición**, pero acompañarlos de una explicación natural en el caption. No son IDs de gobernanza; son identificadores experimentales necesarios para la trazabilidad de las 31 corridas.

En el eje puede naturalizarse únicamente:

```text
H100 ref.  ->  H100 (referencia)
```

Las demás etiquetas pueden mantenerse sin expansión dentro del panel para preservar legibilidad y geometría.

---

## 5. Texto visible que debe naturalizarse

### 5.1 Título

Actual:

```text
EXP11A joint size-composition sensitivity
```

Propuesto:

```text
Sensibilidad conjunta del banco histórico a tamaño y composición
```

Clasificación: `TEXT_ONLY`.

### 5.2 Subtítulo

Actual:

```text
Observed runs only; descriptive and noncausal; no summaries, CI, p-values, or fitted trends
```

Propuesto:

```text
Solo corridas observadas; análisis descriptivo y no causal; sin resúmenes como marcas, IC, valores p ni tendencias ajustadas
```

Clasificación: `TEXT_ONLY`.

### 5.3 Títulos de panel

Para uniformidad con la tesis, se recomienda:

```text
Top1  -> Top-1
Top3  -> Top-3
Top5  -> Top-5
Top10 -> Top-10
Top50 -> Top-50
MRR   -> MRR
```

Clasificación: `TEXT_ONLY`.

### 5.4 Nota inferior

Actual:

```text
Conditions are categorical observed banks; H100 is one frozen reference. Size and composition vary jointly.
```

Propuesto:

```text
Las condiciones representan bancos observados categóricos; H100 es una única referencia congelada. El tamaño y la composición varían conjuntamente.
```

Clasificación: `TEXT_ONLY`.

### 5.5 Etiqueta H100

Actual:

```text
H100 ref.
```

Propuesto:

```text
H100 (referencia)
```

Clasificación: `TEXT_ONLY`.

No se propone añadir texto de gobernanza, nombres de prompts, grupos, gates, commits, blobs o nombres de artefactos en la figura final.

---

## 6. Ajustes tipográficos

No se identifica un ajuste tipográfico obligatorio que requiera mover ejes, puntos, gridlines o categorías. El lienzo aprobado (`1200 × 800`, 3:2; PNG `3000 × 2000`) dispone de anchura suficiente para las sustituciones propuestas.

La regeneración debe conservar inicialmente los tamaños tipográficos aprobados. Si una comprobación determinística del renderer detectara overflow únicamente en el subtítulo, se permite como máximo un ajuste **tipográfico local** del subtítulo o de la nota inferior, sin desplazar paneles ni marcas científicas.

Clasificación:

```text
TYPOGRAPHIC_LAYOUT_ONLY = NO_CHANGE_EXPECTED / LOCAL_ADJUSTMENT_ONLY_IF_NEEDED_FOR_TEXT_FIT
SCIENTIFIC_GEOMETRY_CHANGE = false
```

---

## 7. Caption final propuesto para tesis

**Figura 6. Sensibilidad conjunta del banco histórico a tamaño y composición en el benchmark interno offline del Capítulo 87 (1 056 series, 67 DAM y 42 NANDINA).** Los seis paneles muestran Top-1, Top-3, Top-5, Top-10, Top-50 y MRR para 31 corridas observadas distribuidas en cinco condiciones: H25 (`n=10`), H50-D1 (`n=5`), H50-D2 (`n=5`), H75 (`n=10`) y H100 (`n=1`, referencia congelada). H25, H50, H75 y H100 corresponden a condiciones nominales de tamaño del banco histórico, mientras que D1 y D2 distinguen dos composiciones documentadas dentro de H50; las demás condiciones conservan asimismo sus composiciones observadas. Cada punto representa una corrida individual y H100 se muestra como una única referencia, no como una distribución de réplicas. El tamaño nominal y la composición del banco varían conjuntamente entre condiciones; por ello, las diferencias observadas no permiten identificar un efecto causal aislado ni monotónico del tamaño. No se muestran intervalos de confianza, valores p, regresiones, suavizados ni resúmenes congelados como marcas. La figura constituye una sensibilidad descriptiva dentro del benchmark interno y no representa exactitud global del framework RAG ni validez externa.

Este caption elimina `EXP11A` y el lenguaje de gobernanza visible sin modificar la evidencia científica aprobada.

---

## 8. Dictamen de regeneración futura

La Figura 6 debe regenerarse antes de integrarse en la tesis, pero la regeneración puede realizarse de forma **determinística y exclusivamente editorial** a partir del renderer G6 existente.

### Cambios autorizables

| Cambio | Clasificación | Requerido |
|---|---|---|
| Sustituir título inglés e identificador `EXP11A` por título natural en español | `TEXT_ONLY` | Sí |
| Traducir/naturalizar subtítulo | `TEXT_ONLY` | Sí |
| Normalizar Top1/Top3/Top5/Top10/Top50 a Top-1/Top-3/Top-5/Top-10/Top-50 | `TEXT_ONLY` | Sí |
| Naturalizar `H100 ref.` a `H100 (referencia)` | `TEXT_ONLY` | Sí |
| Traducir la nota inferior | `TEXT_ONLY` | Sí |
| Ajustar localmente fuente/espaciado solo si el texto español no cabe | `TYPOGRAPHIC_LAYOUT_ONLY` | Condicional |
| Mover puntos, ejes, gridlines, categorías o jitter | `SCIENTIFIC_GEOMETRY_CHANGE` | No / prohibido |
| Cambiar valores, corridas, summaries, métricas o denominadores | `SCIENTIFIC_DATA_CHANGE` | No / prohibido |

### Viabilidad técnica

`src/figures/group6/render_g6_fig_03_exp11a.py` define por separado los textos visibles y la geometría científica. Por tanto, la adaptación puede implementarse mediante **sustitución controlada de cadenas en el renderer**, manteniendo sin cambios:

- fuentes de datos y blobs de entrada;
- `METRICS` como inventario científico;
- `CONDITIONS` y su orden científico, salvo la presentación textual de `H100 ref.`;
- `JITTER`;
- anclajes de categorías;
- coordenadas y valores de todos los puntos;
- rango `[0,1]`;
- marcas, separador, gridlines y paneles.

La regeneración futura deberá comparar explícitamente el SVG adaptado contra el SVG G6 aprobado y demostrar que todas las diferencias no textuales son cero, salvo cualquier ajuste tipográfico local previamente justificado.

---

## 9. Dictamen terminal

El artefacto científico G6-FIG-03 es correcto como base científica, pero **no es publicable tal cual en la tesis** por su capa textual interna/inglesa. La corrección requerida no afecta datos, estimandos, distribución de puntos, paneles, ejes ni interpretación científica. Los códigos H25/H50-D1/H50-D2/H75/H100 deben conservarse como identificadores experimentales de condición y explicarse en el caption, evitando reemplazarlos por porcentajes simples que oculten la variación real de tamaño y composición entre corridas.

```text
FIG012_EXECUTION = COMPLETE
FIGURE_6_EXISTING_G6_BINARY_USABLE_AS_IS = false
FIGURE_6_ADAPTATION_REQUIRED = true
SCIENTIFIC_DATA_CHANGE_REQUIRED = false
SCIENTIFIC_GEOMETRY_CHANGE_REQUIRED = false
THESIS_VISIBLE_INTERNAL_IDS_AFTER_ADAPTATION = NONE
DOCX_MODIFIED = false
IMAGE_REGENERATED = false
A043_EXECUTED = false
121G_EXECUTED = false
EXTERNAL_AUDIT = PENDING_BY_IA_EXPERIMENTAL
```
