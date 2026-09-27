# FIG012 — Auditar adaptación para tesis de Figura 6 / G7-F02

## 0. Actor y alcance

Actúa como **IA Diseñadora y Auditora de Figuras Científicas** del proyecto `elVladdi/gci-nandina-rag`.

No eres CODEX. No eres la IA de Redacción Científica. No eres la IA Experimental.

Ejecuta exclusivamente la auditoría científico-visual necesaria para resolver **A043 / Figura 6** después del PASS externo de PROMPT121F.

No modifiques el DOCX. No regeneres SVG/PNG. No modifiques scripts. No ejecutes 121G ni ningún bloque posterior. No escribas todavía el binario final de Figura 6.

Tu producto es un **dictamen de adaptación**, no una nueva figura.

---

## 1. Estado gobernante

El cierre externo de 121F quedó registrado en:

```text
PATH = writing_prompts_tmp/121F_AUDITORIA_EXTERNA_PASS.md
BRANCH = codex/prompts-temporary
COMMIT = 625709b627f62fbcb7090282552ef96e11726b85
```

Estado vinculante:

```text
PROMPT121F_EXTERNAL_AUDIT = PASS
A041 = VERIFIED / COMPLETE
A042 = VERIFIED / COMPLETE
A043 = NOT_EXECUTED / DEFERRED_TO_FIGURE_WORKFLOW
121G_AUTHORIZED = false
G7_F02 = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
G7_F03_AUTHORIZED = false
```

La copia acumulativa vigente para esta frontera es:

```text
Molleapasa_gv_G7F02_REVIEW_V03_F.docx
SHA256 = c630bcc51b33b79e2d0d9fdfc92f2701816dd29116e3051d54f28a713f71216b
SIZE = 4572575 bytes
```

No debes modificarla.

---

## 2. Fuentes científicas obligatorias

Lee íntegramente, como mínimo:

```text
# Congelamiento editorial G7-F01
REF = d91298758dba674003bf650e7a303c36bd0b74d9
PATH = docs/writing/group7/g7_writing_source_freeze_v0.1.json

# Especificación de figuras congelada por G7-F01
REF = e93b44164a9619dad1f527a3b2d4479265858e39
PATH = outputs/figures/group6/g6_figure_spec_registry_v0.1.json
BLOB = 44cc30fc3c38639c6aa4370cb6f317458041f1b1

PATH = docs/figures/group6/g6_caption_registry_v0.1.md
BLOB = 0dcb43cfa56dfce2e6955f960184069beb36ba76

PATH = outputs/figures/group6/g6_figure_hash_ledger_v0.1.csv
BLOB = bfcbfe8a2232246476979506377ff3005166253f

# Especificación científica original de G6-FIG-03
REF = 89d95744b2ab446245a5522eefc8279f673a8a7c
PATH = figure_prompts_tmp/FIG004_RESPUESTA_ESPECIFICACION_CIENTIFICO_VISUAL_G6_FIG_03_EXP11A.md
```

Inspecciona además el contenido textual y visual de:

```text
PATH = figures/group6/g6_fig_03_exp11a.svg
SHA256 = a4a81b565ed2ceb22f23f9a52888e802b1e749186fb43d3bd71faf1b31d5f7c3

PATH = figures/group6/g6_fig_03_exp11a.png
SHA256 = 3c4bcf736b56fbc9ffd054562db0eea31be195792f2bade611a9e5205dfa97de
```

Fuentes científicas de datos de G6-FIG-03:

```text
outputs/results/group5/tables/g5_appendix_02_exp11a_size_composition_sensitivity.csv
Git blob = cf3aedab5935d6af9b3ac7be7b51b954fcb9c403

outputs/experiments/exp11a_historical_size_sensitivity_v0.3/exp11_metrics_by_run.csv
Git blob = 9b434d7e09e6db7e9de061953b59c53aac2337ad

outputs/experiments/exp11a_historical_size_sensitivity_v0.3/exp11_metrics_by_condition.csv
Git blob = 535dd377d107ddcbf09ecaa13cd66ca723ee738d
```

No recalcules métricas ni produzcas inferencia nueva.

---

## 3. Contrato científico que no puede cambiar

La figura científica aprobada representa una **sensibilidad conjunta tamaño–composición, descriptiva y no causal**.

Debe preservar exactamente:

- seis paneles;
- métricas: Top1, Top3, Top5, Top10, Top50 y MRR;
- 31 corridas observadas en total;
- inventario observado: 10 / 5 / 5 / 10 / 1 entre las cinco condiciones mostradas;
- distinción de las dos composiciones observadas dentro de la condición intermedia;
- una única referencia congelada en la condición de mayor banco, no una distribución de réplicas;
- todos los puntos individuales;
- jitter horizontal determinista únicamente visual;
- misma geometría científica de marcas;
- orden categórico no determinado por favorabilidad;
- escala lineal `[0,1]` en los seis paneles;
- ausencia de líneas entre condiciones;
- ausencia de summaries como marcas;
- ausencia de CI, valores p, regresiones, suavizados o tendencias ajustadas;
- prohibición de interpretar un efecto causal aislado o monotónico del tamaño del banco porque tamaño y composición cambian conjuntamente.

HE5 permanece `INCONCLUSIVE`.

No conviertas esta figura de sensibilidad en una figura de desempeño principal o confirmatorio.

---

## 4. Problema editorial que debes auditar

La Figura 6 actual del DOCX es legacy y A043 fue deliberadamente diferida.

El binario G6-FIG-03 aprobado tampoco debe asumirse automáticamente como publicable en la tesis. Su SVG contiene, entre otros, un título interno en inglés del tipo `EXP11A joint size-composition sensitivity` y una explicación interna en inglés. El caption G6 aprobado conserva igualmente nomenclatura de gobernanza/experimento como `EXP11A` y códigos de condiciones.

Debes determinar de forma independiente si:

```text
FIGURE_6_EXISTING_G6_BINARY_USABLE_AS_IS = true|false
FIGURE_6_ADAPTATION_REQUIRED = true|false
SCIENTIFIC_DATA_CHANGE_REQUIRED = true|false
```

El dictamen debe separar con precisión:

1. **contenido científico que debe permanecer idéntico**;
2. **texto visible que puede o debe naturalizarse para la tesis**;
3. **caption final propuesto para tesis**;
4. **cualquier ajuste tipográfico estrictamente necesario** para acomodar textos en español sin alterar la geometría científica.

---

## 5. Reglas editoriales de tesis

La adaptación debe cumplir el contrato REVIEW V03 de Prompt119:

- texto íntegramente natural para una tesis en español;
- no mostrar IDs de gobernanza, prompts, fichas, gates, commits, blobs o nombres de artefactos internos;
- no usar `EXP11A` como rótulo visible de publicación;
- no introducir lenguaje de desarrollo interno;
- no cambiar datos ni fuerza de los claims;
- no convertir una sensibilidad conjunta en un efecto de tamaño aislado;
- no usar expresiones como `mejor`, `peor`, `óptimo` o equivalentes si implican ordenamiento por favorabilidad.

### Códigos de condición

No asumas por el nombre qué significa `H25`, `H50`, `H75` o `H100`. Verifica su semántica exacta contra las fuentes congeladas antes de proponer etiquetas naturales.

Debes decidir expresamente si los códigos `H25`, `H50-D1`, `H50-D2`, `H75` y `H100` deben:

- mantenerse porque constituyen identificadores experimentales científicamente necesarios, pero acompañados de una explicación comprensible; o
- sustituirse visualmente por etiquetas descriptivas naturales de tesis, conservando una correspondencia explícita e inequívoca en el dictamen.

No inventes porcentajes, tamaños nominales o significados que las fuentes no sostengan.

---

## 6. Caption para tesis

Propón un caption final en español que:

- no contenga `EXP11A` ni IDs internos;
- identifique la figura como **sensibilidad conjunta del banco histórico a tamaño y composición**;
- indique que son 31 corridas observadas;
- describa las cinco condiciones/composiciones de forma comprensible y fiel;
- indique que cada punto es una corrida individual;
- aclare que la referencia de la condición de mayor banco es una sola corrida congelada;
- declare explícitamente que tamaño y composición varían conjuntamente;
- prohíba la lectura causal o monotónica del tamaño;
- indique ausencia de CI, valores p, regresiones/suavizados y summaries como marcas;
- mantenga alcance interno de Capítulo 87 cuando sea pertinente;
- no afirme exactitud global del RAG ni validez externa.

No agregues información científica nueva.

---

## 7. Dictamen de regeneración

Si concluyes que el binario G6 no puede insertarse tal cual, especifica exactamente qué debe cambiar en una futura regeneración determinística.

Clasifica cada cambio como:

```text
TEXT_ONLY
TYPOGRAPHIC_LAYOUT_ONLY
SCIENTIFIC_GEOMETRY_CHANGE
SCIENTIFIC_DATA_CHANGE
```

Para una adaptación exclusivamente editorial, `SCIENTIFIC_GEOMETRY_CHANGE` y `SCIENTIFIC_DATA_CHANGE` deben ser `false`.

Indica si la regeneración puede realizarse técnicamente mediante una sustitución controlada del renderer G6 que preserve todos los elementos SVG no textuales y todas las coordenadas científicas.

No ejecutes esa regeneración en FIG012.

---

## 8. Salida obligatoria

Publica exclusivamente la respuesta en:

```text
figure_prompts_tmp/FIG012_RESPUESTA_AUDITAR_ADAPTACION_TESIS_FIGURA6_G7_F02.md
```

rama:

```text
codex/prompts-temporary
```

La respuesta debe terminar con:

```text
FIG012_EXECUTION = COMPLETE
FIGURE_6_EXISTING_G6_BINARY_USABLE_AS_IS = true|false
FIGURE_6_ADAPTATION_REQUIRED = true|false
SCIENTIFIC_DATA_CHANGE_REQUIRED = true|false
SCIENTIFIC_GEOMETRY_CHANGE_REQUIRED = true|false
THESIS_VISIBLE_INTERNAL_IDS_AFTER_ADAPTATION = NONE|<detalle>
DOCX_MODIFIED = false
IMAGE_REGENERATED = false
A043_EXECUTED = false
121G_EXECUTED = false
EXTERNAL_AUDIT = PENDING_BY_IA_EXPERIMENTAL
```

Detente para auditoría externa de la IA Experimental.
