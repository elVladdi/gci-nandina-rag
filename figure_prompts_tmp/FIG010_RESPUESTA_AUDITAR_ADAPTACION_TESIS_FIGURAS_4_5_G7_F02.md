# FIG010 — Respuesta: auditoría de adaptación para tesis de Figuras 4–5 en G7-F02

```text
FIG010_EXECUTION = COMPLETE
FIGURE_4_EXISTING_G6_BINARY_USABLE_AS_IS = false
FIGURE_5_EXISTING_G6_BINARY_USABLE_AS_IS = false
FIGURE_4_ADAPTATION_REQUIRED = true
FIGURE_5_ADAPTATION_REQUIRED = true
SCIENTIFIC_DATA_CHANGE_REQUIRED = false
THESIS_VISIBLE_INTERNAL_IDS_AFTER_ADAPTATION = NONE
NEXT_TECHNICAL_STEP = REGENERACION_DETERMINISTICA_EXCLUSIVAMENTE_EDITORIAL_DE_G6_FIG_01_Y_G6_FIG_02_PARA_FIGURAS_4_Y_5_DE_TESIS_SEGUIDA_DE_AUDITORIA_EXTERNA_ANTES_DE_EDITAR_EL_DOCX
EXTERNAL_AUDIT = PENDING_BY_IA_EXPERIMENTAL
```

## 1. Verificación de entradas y fuentes gobernantes

Se auditó exclusivamente la adaptación para tesis de `G6-FIG-01 -> Figura 4` y `G6-FIG-02 -> Figura 5`. No se modificó el DOCX, no se regeneraron imágenes, no se modificaron tablas ni prosa y no se avanzó a 121F.

La entrada de tesis coincide exactamente con la identidad exigida:

```text
Molleapasa_gv_G7F02_REVIEW_V03_E.docx
SHA256 = f6eb5a9f4db80faa36306df64ec51ddd865df2a081d69f65ca6a3e063ec2b7ba
```

Los tres artefactos visuales gobernantes se leyeron íntegramente y sus blobs coinciden con el source freeze de G7-F01:

```text
outputs/figures/group6/g6_figure_spec_registry_v0.1.json
BLOB = 44cc30fc3c38639c6aa4370cb6f317458041f1b1

aoutputs/figures/group6/g6_figure_hash_ledger_v0.1.csv
BLOB = bfcbfe8a2232246476979506377ff3005166253f

docs/figures/group6/g6_caption_registry_v0.1.md
BLOB = 0dcb43cfa56dfce2e6955f960184069beb36ba76
```

Nota: la cadena `aoutputs/` de la línea anterior es solo un error tipográfico de este reporte y no identifica una ruta distinta. La ruta gobernante efectivamente auditada fue `outputs/figures/group6/g6_figure_hash_ledger_v0.1.csv`.

El ledger confirma los PNG aprobados:

```text
G6-FIG-01 PNG SHA256 = 3136a814647384eaa1f85c2ce90033a78dde48b661d0b1c078e5b272c6e85d6f
G6-FIG-02 PNG SHA256 = 867ca35d0c454a38bd122c6ecdf5bb693f98f86206828bd68c051aa263c7791f
```

No se detecta ninguna necesidad de modificar datos, estimandos, intervalos, denominadores, orden científico, escalas, posiciones de marcas ni rol de las figuras. La necesidad de adaptación es exclusivamente editorial y lingüística para la tesis.

---

# 2. Figura 4 de la tesis — adaptación de G6-FIG-01

## 2.1 Dictamen visual/científico

```text
FIGURE_4_EXISTING_G6_BINARY_USABLE_AS_IS = false
FIGURE_4_ADAPTATION_REQUIRED = true
FIGURE_4_SCIENTIFIC_STRUCTURE_CHANGE_REQUIRED = false
```

La estructura científica del artefacto aprobado es correcta y debe conservarse sin cambios: tres paneles apilados; Panel A con valores observados; Panel B con las quince diferencias pareadas histórico − comparador y sus IC del 99 %; Panel C con el único contraste `Recall@200 − Recall@100` y su IC del 95 %. También deben preservarse las escalas, el cero de referencia en los paneles de contraste, las formas de marcador y la ausencia de IC por brazo y de valores p.

El PNG aprobado, sin embargo, no puede insertarse tal cual en la tesis porque el SVG equivalente contiene rótulos en inglés y nombres internos de ejecución. En particular aparecen visiblemente `Attempt06` y `D1a`, además de `Historical`, `Flat`, `Hierarchical`, `Observed values`, `Paired difference` y otros rótulos ingleses. La adaptación requerida no es científica: consiste únicamente en naturalizar esos textos.

## 2.2 Términos visibles que deben naturalizarse

Términos internos explícitos encontrados en el artefacto aprobado:

```text
Attempt06
D1a
```

También deben traducirse los rótulos ingleses para que la figura quede íntegramente en lenguaje de tesis.

## 2.3 Sustituciones exactas de etiquetas

Manteniendo intactas posiciones, datos, marcas, escalas y orden:

| Etiqueta aprobada G6 | Etiqueta para Figura 4 de tesis |
|---|---|
| `Primary HE2 evidence` | `Evidencia primaria de HE2` |
| `Offline internal benchmark: 1,056 series / 67 DAM / 42 NANDINA` | `Evaluación interna fuera de línea: 1 056 series / 67 DAM / 42 NANDINA` |
| `Observed values (no arm-level CI)` | `Valores observados (sin IC por brazo)` |
| `Observed metric value` | `Valor observado de la métrica` |
| `Historical` | `Recuperación histórica` |
| `Flat (Attempt06)` | `BM25 normativo plano` |
| `Hierarchical (Attempt06)` | `BM25 normativo jerárquico` |
| `D1a (Attempt06)` | `Recuperador denso entrenado con MNRL` |
| `Historical - comparator (frozen 99% CI)` | `Recuperación histórica − comparador (IC del 99 %)` |
| `Flat` | `BM25 normativo plano` |
| `Hierarchical` | `BM25 normativo jerárquico` |
| `D1a` | `Recuperador denso entrenado con MNRL` |
| `Paired difference` | `Diferencia pareada` |
| `Recall@200 - Recall@100 (frozen 95% CI)` | `Recall@200 − Recall@100 (IC del 95 %)` |
| `Hierarchical (Attempt06)` en Panel C | `BM25 normativo jerárquico` |
| `Paired recall difference` | `Diferencia pareada de recall` |
| `Context: Recall@100=0.101; Recall@200=0.304; delta=0.203 [0.067, 0.342]` | `Contexto: Recall@100 = 0,101; Recall@200 = 0,304; diferencia = 0,203; IC 95 % [0,067; 0,342]` |

Si alguna etiqueta larga requiere salto de línea para conservar legibilidad, el salto debe ser puramente tipográfico y no alterar el texto ni la geometría de los datos.

## 2.4 Caption final propuesto para tesis

**Figura 4. Evidencia primaria de HE2: ordenamiento temprano y cobertura profunda en la evaluación interna realizada fuera de línea del Capítulo 87 (1 056 series, 67 DAM y 42 subpartidas NANDINA).** (A) Valores observados de la recuperación histórica y de los tres comparadores corregidos —BM25 normativo plano, BM25 normativo jerárquico y recuperador denso entrenado con MNRL— en Top-1, Top-3, Top-5, Top-10 y MRR@100; los valores por brazo son descriptivos y no tienen intervalos de confianza por brazo autorizados. (B) Quince diferencias pareadas entre la recuperación histórica y cada comparador, correspondientes a las cinco métricas primarias y los tres comparadores, con intervalos de confianza del 99 % sobre cada diferencia pareada. (C) Único contraste primario de cobertura profunda del recuperador jerárquico, `Recall@200 − Recall@100`, con intervalo de confianza del 95 %; Recall@100 y Recall@200 se muestran únicamente como contexto y Pool@200 no se duplica como evidencia confirmatoria. No se calcularon valores p. Los contrastes son no causales y se limitan a esta evaluación interna; la figura no representa la exactitud global del marco RAG, corrección jurídica ni validez externa.

## 2.5 Coherencia con Tabla 12 y con el contraste profundo

```text
FIGURE_4_TABLE_12_ALIGNMENT = PASS
FIGURE_4_DEEP_COVERAGE_ALIGNMENT = PASS
```

- El Panel A conserva las cinco métricas primarias y los tres comparadores corregidos que aparecen en Tabla 12.
- El Panel B conserva exactamente los quince contrastes pareados histórico − comparador con IC del 99 %, sin introducir IC por brazo ni valores p.
- El Panel C conserva el único contraste primario de cobertura profunda vigente: `Recall@100 = 0,1013`, `Recall@200 = 0,3040`, diferencia `0,2027`, IC 95 % `[0,0668; 0,3416]` sobre 1 056 series / 67 DAM.
- `Pool@200` no debe representarse como segundo estimando confirmatorio.
- La figura no debe convertir la superioridad del ordenamiento histórico en una afirmación de exactitud global del marco RAG ni de corrección jurídica.

## 2.6 Uso del PNG existente

```text
FIGURE_4_EXISTING_G6_BINARY_USABLE_AS_IS = false
FIGURE_4_REGENERATION_REASON = EDITORIAL_LABEL_NATURALIZATION_ONLY
```

El PNG aprobado requiere regeneración determinística exclusivamente editorial porque los términos `Attempt06` y `D1a` están incrustados en el propio gráfico. Cambiar únicamente el caption no resolvería esa exposición de identificadores internos.

---

# 3. Figura 5 de la tesis — adaptación de G6-FIG-02

## 3.1 Dictamen visual/científico

```text
FIGURE_5_EXISTING_G6_BINARY_USABLE_AS_IS = false
FIGURE_5_ADAPTATION_REQUIRED = true
FIGURE_5_SCIENTIFIC_STRUCTURE_CHANGE_REQUIRED = false
```

La estructura científica aprobada debe conservarse: un único panel, cinco variantes por cada profundidad 50/100/200, quince marcas en total, eje Y desde cero hasta 0,35, sin líneas de conexión, sin IC, sin valores p, sin tendencias ajustadas y sin ordenamiento por favorabilidad. Las cuatro variantes predefinidas deben conservar igual estatus visual y la variante 70/30 debe mantener el mismo peso visual aunque su rol se indique como contexto descriptivo adicional. La unión diagnóstica debe continuar excluida del rendimiento ordinario.

El PNG no puede usarse tal cual en la tesis porque el SVG equivalente muestra `Phase E` y varios identificadores técnicos de variantes (`hierarchical_only`, `dual_only`, `hierarchical_first_100`, `hierarchical_80_dual_backfill_20`, `hierarchical_70_dual_backfill_30`), además de rótulos ingleses. El caption G6 aprobado contiene adicionalmente `A_historical_defined`, `G3C-005` y `diagnostic_union_hierarchical_dual`. Todos deben desaparecer de la versión visible de tesis.

## 3.2 Términos visibles que deben naturalizarse

```text
Phase E
hierarchical_only
dual_only
hierarchical_first_100
hierarchical_80_dual_backfill_20
hierarchical_70_dual_backfill_30
A_historical_defined
G3C-005
diagnostic_union_hierarchical_dual
```

Los tres últimos están presentes en el caption aprobado aunque no necesariamente en el área gráfica del PNG; tampoco deben trasladarse al caption de tesis.

## 3.3 Sustituciones exactas de etiquetas

| Etiqueta aprobada G6 | Etiqueta para Figura 5 de tesis |
|---|---|
| `Phase E exact-NANDINA coverage` | `Cobertura exacta NANDINA del conjunto candidato según profundidad y variante` |
| `Descriptive only; no CI, p-values, fitted trends, or connecting lines` | `Resultados descriptivos; sin IC, valores p, tendencias ajustadas ni líneas de conexión` |
| `Exact-NANDINA coverage` | `Cobertura exacta NANDINA` |
| `Recovery depth (ordered categories)` | `Profundidad de recuperación` |
| `Formal claim variants` | `Variantes descriptivas predefinidas` |
| `hierarchical_only` | `Solo jerárquico` |
| `dual_only` | `Solo dual` |
| `hierarchical_first_100` | `Jerárquico con prioridad para los primeros 100 candidatos` |
| `hierarchical_80_dual_backfill_20` | `Jerárquico 80 + backfill dual 20` |
| `Context only` | `Contexto descriptivo adicional` |
| `hierarchical_70_dual_backfill_30` | `Jerárquico 70 + backfill dual 30` |
| `15 marks = 5 variants x 3 depths` | `15 puntos = 5 variantes × 3 profundidades` |
| `N = 1,056 series` | `N = 1 056 series` |
| `The diagnostic union is excluded from ordinary performance. Context and formal variants retain equal visual weight.` | `La unión diagnóstica se excluye del rendimiento ordinario. Las variantes predefinidas y la variante contextual conservan igual peso visual.` |

Los quince valores y sus posiciones no deben cambiar. Tampoco debe cambiar el orden fijo de las cinco variantes ni de las profundidades 50, 100 y 200.

## 3.4 Caption final propuesto para tesis

**Figura 5. Cobertura exacta NANDINA del conjunto candidato según profundidad y variante en la evaluación interna realizada fuera de línea del Capítulo 87 (1 056 series, 67 DAM y 42 subpartidas NANDINA).** Se muestran 15 proporciones descriptivas de cobertura exacta NANDINA: cinco variantes en cada profundidad de recuperación 50, 100 y 200. Solo jerárquico, Solo dual, Jerárquico con prioridad para los primeros 100 candidatos y Jerárquico 80 + backfill dual 20 corresponden a las cuatro variantes descriptivas predefinidas; Jerárquico 70 + backfill dual 30 se incluye únicamente como contexto descriptivo adicional y no fue seleccionada por favorabilidad. No se presentan intervalos de confianza, valores p, tendencias ajustadas ni contrastes inferenciales entre variantes. La unión diagnóstica jerárquica-dual se excluye del rendimiento ordinario porque representa un techo de cobertura y no una variante de desempeño ordinario. La figura no establece un orden de favorabilidad entre variantes ni modifica la evidencia confirmatoria o la disposición de HE2.

## 3.5 Coherencia con Tabla 13

```text
FIGURE_5_TABLE_13_ALIGNMENT = PASS
```

La figura debe conservar exactamente los quince valores descriptivos de Tabla 13:

```text
Solo jerárquico:                 0,0909 | 0,1013 | 0,3040
Solo dual:                       0,0919 | 0,1004 | 0,2661
Jerárquico prioridad primeros 100: 0,0909 | 0,1013 | 0,2652
Jerárquico 80 + backfill dual 20: 0,0909 | 0,1013 | 0,3040
Jerárquico 70 + backfill dual 30: 0,0909 | 0,1023 | 0,3040
```

Las cuatro primeras variantes conservan el mismo estatus descriptivo predefinido; la quinta es únicamente contexto descriptivo adicional. No se autoriza inferencia entre variantes, ranking de favorabilidad, tendencia ajustada ni uso de la unión diagnóstica como rendimiento ordinario.

## 3.6 Uso del PNG existente

```text
FIGURE_5_EXISTING_G6_BINARY_USABLE_AS_IS = false
FIGURE_5_REGENERATION_REASON = EDITORIAL_LABEL_NATURALIZATION_ONLY
```

El PNG aprobado requiere regeneración determinística exclusivamente editorial porque `Phase E` y los identificadores técnicos de variantes forman parte visible del propio gráfico. Un cambio aislado de caption no sería suficiente.

---

# 4. Especificación vinculante para el siguiente paso técnico

La futura regeneración, si es autorizada por un prompt posterior, debe ser estrictamente editorial:

```text
DATA_VALUES_CHANGED = false
ESTIMANDS_CHANGED = false
CI_LEVELS_CHANGED = false
DENOMINATORS_CHANGED = false
VARIANT_ORDER_CHANGED = false
METRIC_ORDER_CHANGED = false
AXIS_RANGES_CHANGED = false
MARKER_SEMANTICS_CHANGED = false
SCIENTIFIC_ROLE_CHANGED = false
NEW_METRICS = false
NEW_INFERENCE = false
NEW_CI = false
NEW_P_VALUES = false
```

Debe reutilizar las mismas fuentes científicas y geometría/semántica aprobadas de G6, sustituyendo únicamente textos visibles y captions por las formulaciones especificadas en esta auditoría. Después de la regeneración deberá verificarse determinísticamente que ningún identificador interno permanezca visible y que los valores/intervalos coincidan exactamente con los artefactos científicos congelados.

```text
THESIS_VISIBLE_INTERNAL_IDS_AFTER_ADAPTATION = NONE
SCIENTIFIC_DATA_CHANGE_REQUIRED = false
NEXT_TECHNICAL_STEP = REGENERACION_DETERMINISTICA_EXCLUSIVAMENTE_EDITORIAL_DE_AMBAS_FIGURAS_Y_AUDITORIA_EXTERNA
121F_AUTHORIZED = false
DOCX_MODIFIED = false
FIGURE_BINARY_REGENERATED = false
EXTERNAL_AUDIT = PENDING_BY_IA_EXPERIMENTAL
```

Detención obligatoria: no se edita la tesis y no se ejecuta regeneración técnica en FIG010.