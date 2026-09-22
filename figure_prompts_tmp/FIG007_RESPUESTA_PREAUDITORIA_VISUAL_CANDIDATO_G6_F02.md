# FIG007 — Respuesta de preauditoría visual y científica del candidato G6-F02

```text
FIG007_PREAUDIT_RESULT = ADDITIONAL_CORRECTIONS_REQUIRED
CANDIDATE_COMMIT = 2a483984eddc60dbbd48e7188b6fe9dbd7e829c5
CANDIDATE_PARENT = b6404ca85c8cd0b18a6b318bae1236d2ef021f4a
REGISTRY_COMMIT_OR_BLOB = b6404ca85c8cd0b18a6b318bae1236d2ef021f4a / 44cc30fc3c38639c6aa4370cb6f317458041f1b1
KNOWN_PROMPT105_FINDINGS_CONFIRMED = true
ADDITIONAL_FINDING_COUNT = 4
G6_F02_APPROVAL_AUTHORIZED = false
G6_F03_AUTHORIZED = false
```

## 1. Alcance y fuentes auditadas

La preauditoría se realizó exclusivamente sobre el candidato remoto congelado `figures/g6-f02-render-v01@2a483984eddc60dbbd48e7188b6fe9dbd7e829c5`, que se verificó exactamente `1 commit ahead / 0 commits behind` respecto de `b6404ca85c8cd0b18a6b318bae1236d2ef021f4a` y modifica acumulativamente solo los diez paths previstos para G6-F02.

Se revisaron íntegramente el registry rector `outputs/figures/group6/g6_figure_spec_registry_v0.1.json` (blob `44cc30fc3c38639c6aa4370cb6f317458041f1b1`), los tres scripts de render, los tres SVG candidatos, la presencia y metadata Git de los tres PNG, el ledger `g6_figure_hash_ledger_v0.1.csv`, y las fuentes canónicas utilizadas por las tres figuras. También se consultó Prompt105 únicamente para distinguir sus dos correcciones ya conocidas de cualquier hallazgo adicional.

No se ejecutó Prompt105, no se generaron figuras ni scripts, no se editó el candidato, no se recalcularon métricas, CI o inferencia, y no se modificaron `main`, Plan Maestro, fichas, artículo o tesis.

## 2. FIGURE_01_AUDIT — G6-FIG-01

**Resultado:** `PASS_WITH_MINOR_ADDITIONAL_LABEL_CORRECTION`.

La figura conserva los tres paneles verticales y la relación aproximada 4:5. El Panel A representa exactamente las cinco métricas primarias `Top-1`, `Top-3`, `Top-5`, `Top-10` y `MRR@100`, con Historical más Flat, Hierarchical y D1a; Historical se deduplica visualmente solo después de comprobar identidad literal entre sus tres repeticiones estructurales. No existen CI por brazo. El rango es `[0,1]` y no hay líneas de conexión entre métricas.

El Panel B representa los 15 contrastes pareados `Historical − comparator`, en el orden científico congelado y con los CI de 99% tomados directamente de las columnas congeladas. El cero es visible y el rango es `[-0.1,1]`. No aparecen p-values, significancia, CI por brazo ni métricas adicionales.

El Panel C representa exactamente un estimando HE2_B, `Recall@200 − Recall@100`, con su CI congelado de 95%, rango `[-0.1,1]` y referencia en cero. `Recall@100=0.101`, `Recall@200=0.304` y el contraste/CI se muestran solo como contexto; `Pool@200` no se materializa como un segundo estimando. No se detectó sobreclaim inferencial o causal.

La codificación usa formas redundantes además del color y es interpretable en escala de grises. Los tamaños tipográficos observados cumplen el mínimo específico de esta figura. No se detectaron recortes de los elementos relevantes ni truncación de ejes.

Se detectó, no obstante, una discrepancia menor de etiqueta en Panel C: el registry fija el eje/categoría como `Hierarchical (Attempt06)`, mientras el SVG muestra solo `Hierarchical`. El valor, CI y método subyacente son correctos; el problema es de identificación explícita del estado corregido vigente.

## 3. FIGURE_02_AUDIT — G6-FIG-02

**Resultado:** `PASS_WITH_MINOR_ADDITIONAL_AXIS_LABEL_CORRECTION`.

La figura es un solo panel horizontal 16:9, con exactamente 15 marcas: cinco variantes por cada una de las profundidades ordenadas `50`, `100` y `200`. Las cuatro variantes formales son `hierarchical_only`, `dual_only`, `hierarchical_first_100` y `hierarchical_80_dual_backfill_20`; `hierarchical_70_dual_backfill_30` aparece como variante contextual mediante hexágono abierto y está separada explícitamente bajo `Context only`.

Las posiciones verticales proceden exclusivamente de `exact-NANDINA coverage`; el rango y es `[0,0.35]` con baseline cero. No hay CI, p-values, estrellas, regresiones, smoothing, interpolación ni líneas que conecten profundidades. `diagnostic_union_hierarchical_dual` está excluido. El orden de variantes no se deriva de favorabilidad. Los 12 registros formales y los 3 contextuales quedan representados sin promover Phase E a evidencia confirmatoria.

La identidad visual no depende solo del color: cada variante tiene forma propia y la variante contextual conserva tamaño y contraste, sin reducción de opacidad. Ticks y leyenda están en 9 pt y las etiquetas de eje en 11 pt, compatibles con el registry.

Se detectó un defecto menor de colocación del título del eje y: `Exact-NANDINA coverage` se dibuja horizontalmente desde `x=25` a la altura media del panel. Como el área de trazado comienza en `x=100`, el texto cruza el eje vertical y penetra visualmente en el campo de datos. No altera ningún valor, pero reduce la asociación inequívoca del texto con el eje y y es impropio para una salida de publicación. Debe recolocarse fuera del campo de datos —mediante rotación o una ubicación externa equivalente— sin alterar el rango, los puntos ni el layout científico.

## 4. FIGURE_03_AUDIT — G6-FIG-03

**Resultado:** `CORRECTION_REQUIRED`.

La estructura científica es correcta: seis paneles `2×3`, orden `Top1`, `Top3`, `Top5`, `Top10`, `Top50`, `MRR`; eje x categórico con orden `H25`, `H50-D1`, `H50-D2`, `H75`, `H100 ref.`; rango y `[0,1]` en todos los paneles. Se grafican exclusivamente las 31 corridas `OBSERVED_RUN` con inventario `10 / 5 / 5 / 10 / 1`. Los seis `FROZEN_CONDITION_SUMMARY` se verifican pero no se grafican. D1/D2 se resuelve mediante `dominant_stratum`, H100 aparece como una única referencia en diamante y el jitter usa la misma asignación determinista por `run/seed` en los seis paneles. No se muestran CI, p-values, regresiones, suavizados, líneas entre condiciones ni agregados nuevos. Título, subtítulo y nota inferior preservan explícitamente el carácter descriptivo, conjunto tamaño-composición y no causal.

El defecto tipográfico conocido se confirma y es más amplio que la mención inicial de las categorías: las etiquetas `H25`, `H50-D1`, `H50-D2`, `H75` y `H100 ref.` están a 7.5 pt y los ticks del eje y están a 8.0 pt. Ambos están por debajo del mínimo efectivo de 8.5 pt del registry. Prompt105 ya ordena que ninguna etiqueta efectiva de G6-FIG-03 quede por debajo de 8.5 pt, por lo que ambos subconjuntos quedan cubiertos por la corrección conocida.

Además se detectó un problema de oclusión de marcas no cubierto explícitamente por Prompt105. El jitter se materializa como `offset × 55` con círculos de radio `4.8`. En paneles con valores muy concentrados, varias corridas quedan superpuestas y no son visualmente distinguibles como observaciones individuales. El caso más claro está en `Top50 / H25`: el SVG contiene, entre otros, círculos con centros `(448.10,432.23)` y `(454.70,432.23)`, ambos con `r=4.8`, además de varios centros adyacentes entre `y≈430.7–435.1`. En `Top50 / H50-D2` aparecen cuatro círculos consecutivos alrededor de `y≈432.5–433.8` con separación horizontal pequeña. Las marcas existen, pero la oclusión dificulta recuperar visualmente el inventario de corridas y debilita la función del strip/dot plot como representación de observaciones individuales.

La corrección debe conservar exactamente los valores y posiciones y, el orden fijo de jitter y su identidad entre paneles, pero ajustar solo la geometría de dispersión/marker size necesaria para que las observaciones superpuestas resulten distinguibles a tamaño de publicación. No debe añadirse jitter vertical, resumen, densidad, boxplot ni transformación de datos.

## 5. ACCESSIBILITY_AUDIT

**Resultado:** `FAIL_PENDING_CORRECTION`.

G6-FIG-01 cumple los mínimos tipográficos y usa redundancia forma+color. G6-FIG-02 usa formas únicas, agrupación de leyenda formal/contextual y tamaños compatibles con el registry; su título de eje y requiere recolocación por claridad espacial. G6-FIG-03 incumple el mínimo de 8.5 pt en categorías y ticks y presenta oclusión de puntos en paneles densos. En las tres figuras el color no es el único canal semántico, los fondos son blancos, las grillas son subordinadas y no existen sombras, gradientes o 3D.

La legibilidad en escala de grises se considera preservada por forma, posición y/o relleno: G6-FIG-01 diferencia círculo/cuadrado/triángulo/diamante; G6-FIG-02 usa cinco formas distintas y separación formal/contextual; G6-FIG-03 identifica categorías primariamente por posición y rótulo, con H100 adicionalmente diferenciado mediante diamante.

## 6. SCIENTIFIC_FIDELITY_AUDIT

**Resultado:** `PASS`.

No se detectó cambio científico respecto del registry. Se preservan:

```text
HE2 = SUPPORTED
HE5 = INCONCLUSIVE
EXP11A = JOINT_SIZE_COMPOSITION_SENSITIVITY / NONCAUSAL
EXP12 = CLOSED_WITHOUT_RETRIEVAL / DIVERSITY_EFFECT_NOT_ESTIMABLE
```

G6-FIG-01 conserva 15 contrastes HE2_A con CI 99% y un único contraste HE2_B con CI 95%; no crea CI por brazo ni duplica `Pool@200` como estimando. G6-FIG-02 sigue siendo descriptiva, usa las 15 filas canónicas y excluye la unión diagnóstica. G6-FIG-03 usa las 31 corridas observadas, no grafica los seis summaries y no convierte tamaño del banco en dosis causal o monotónica.

No se identificaron métricas, CI, p-values, efectos, tendencias o conclusiones nuevas producidas por los scripts.

## 7. CROSS_FIGURE_CONSISTENCY_AUDIT

**Resultado:** `PASS_WITH_EDITORIAL_CORRECTION`.

Las tres figuras usan fondo blanco, tipografía sans serif, jerarquía visual similar, gris subordinado para contexto, líneas finas y codificación redundante. Las diferencias de orientación y panelización corresponden al registry y no son inconsistencias.

Sin embargo, los tres SVG llevan incrustados como parte visible del título los identificadores de gobernanza `G6-FIG-01 |`, `G6-FIG-02 |` y `G6-FIG-03 |`. Esos identificadores pertenecen al flujo interno de Grupo 6 y pueden entrar en conflicto con la numeración editorial real de figura en tesis/artículo o con el caption externo. El problema no afecta ciencia, pero sí la aptitud editorial del arte final. Deben retirarse de los títulos visibles y mantenerse solo como identificadores de archivo/registry; el texto descriptivo posterior al separador puede conservarse.

La equivalencia científica SVG/PNG está estructuralmente preservada por los scripts: cada llamada que dibuja texto, línea o marca en Pillow añade en el mismo punto del flujo el elemento SVG equivalente con las mismas coordenadas y datos; no existen ramas de contenido científico específicas por formato. Los seis archivos de salida están presentes en Git con tamaños no nulos. No se detectó una divergencia de contenido científico entre formatos.

## 8. KNOWN_PROMPT105_FINDINGS_CONFIRMED

### FIG007-KNOWN-001

```text
finding_id = FIG007-KNOWN-001
figure_id = ALL / LEDGER
severity = BLOCKING
registry_requirement = reproducible candidate with traceable canonical sources/outputs
observed_candidate_behavior = g6_figure_hash_ledger_v0.1.csv records SHA-256/size for materialized CRLF text bytes rather than canonical Git content bytes; e.g. g6_fig_01_he2.svg is recorded as 23901 bytes while Git canonical content is 23713 bytes; analogous text-size drift is present for the other SVG/text artifacts.
evidence_path = outputs/figures/group6/g6_figure_hash_ledger_v0.1.csv; Git metadata at candidate commit
scientific_or_visual_risk = remote ledger cannot verify the canonical versioned bytes directly
required_correction = recompute ledger SHA-256 and size over canonical Git/index bytes exactly as Prompt105 prescribes
whether_already_covered_by_Prompt105 = true
```

### FIG007-KNOWN-002

```text
finding_id = FIG007-KNOWN-002
figure_id = G6-FIG-03
severity = BLOCKING
registry_requirement = minimum effective font size 8.5 pt
observed_candidate_behavior = categorical labels are 7.5 pt and y-axis ticks are 8.0 pt in the SVG/script
 evidence_path = src/figures/group6/render_g6_fig_03_exp11a.py; figures/group6/g6_fig_03_exp11a.svg
scientific_or_visual_risk = publication-size accessibility/legibility below frozen minimum
required_correction = make every effective G6-FIG-03 label at least 8.5 pt while keeping labels horizontal and preserving scientific layout
whether_already_covered_by_Prompt105 = true
```

## 9. FINDINGS — adicionales a Prompt105

### FIG007-ADD-001

```text
finding_id = FIG007-ADD-001
figure_id = G6-FIG-03
severity = MAJOR_NONBLOCKING
registry_requirement = 31 observed runs must be represented as individual marks in categorical strip/dot plots with deterministic jitter; legibility at publication size and overlap audit are required
observed_candidate_behavior = several observed-run circles are materially occluded in dense regions, especially Top50/H25 and Top50/H50-D2; the marks exist but multiple outlines overlap strongly because the realized horizontal separation is small relative to r=4.8
evidence_path = figures/group6/g6_fig_03_exp11a.svg; src/figures/group6/render_g6_fig_03_exp11a.py
scientific_or_visual_risk = individual observed runs become visually non-recoverable, weakening the intended run-level sensitivity display and potentially making multiplicity appear smaller than the frozen 10/5/5/10/1 inventory
required_correction = adjust only horizontal visual separation and/or marker radius so individual observations remain discernible; preserve exact y values, category order, deterministic run/seed assignment, identical jitter identity across panels, H100 single-reference semantics and all 31 marks
whether_already_covered_by_Prompt105 = false
```

### FIG007-ADD-002

```text
finding_id = FIG007-ADD-002
figure_id = ALL
severity = MINOR
registry_requirement = visible titles/annotations should function as scientific/editorial figure content and should not confuse internal workflow identifiers with publication numbering
observed_candidate_behavior = all three visible titles begin with internal identifiers `G6-FIG-01 |`, `G6-FIG-02 |`, `G6-FIG-03 |`
evidence_path = figures/group6/g6_fig_01_he2.svg; figures/group6/g6_fig_02_phase_e.svg; figures/group6/g6_fig_03_exp11a.svg
scientific_or_visual_risk = possible conflict with final thesis/article figure numbering and unnecessary exposure of internal governance nomenclature in the published graphic
required_correction = remove the visible `G6-FIG-0X |` prefixes while retaining descriptive titles and keeping the identifiers in filenames/registry only
whether_already_covered_by_Prompt105 = false
```

### FIG007-ADD-003

```text
finding_id = FIG007-ADD-003
figure_id = G6-FIG-01
severity = MINOR
registry_requirement = Panel C categorical/y identity is `Hierarchical (Attempt06)`
observed_candidate_behavior = Panel C renders only `Hierarchical`
evidence_path = figures/group6/g6_fig_01_he2.svg; src/figures/group6/render_g6_fig_01_he2.py; outputs/figures/group6/g6_figure_spec_registry_v0.1.json
scientific_or_visual_risk = reduced explicitness that the plotted HE2_B estimand corresponds to the corrected Attempt06 hierarchical state
required_correction = render `Hierarchical (Attempt06)` or an unambiguous line-broken equivalent without changing the estimate, CI, range or panel geometry beyond what is needed for the label
whether_already_covered_by_Prompt105 = false
```

### FIG007-ADD-004

```text
finding_id = FIG007-ADD-004
figure_id = G6-FIG-02
severity = MINOR
registry_requirement = clear scientific axis labeling with axis label >=10 pt and no problematic overlap/placement
observed_candidate_behavior = `Exact-NANDINA coverage` is drawn horizontally from x=25 at the vertical midpoint while the plotting region starts at x=100, so the y-axis title crosses the y-axis and extends into the plotting field
 evidence_path = figures/group6/g6_fig_02_phase_e.svg; src/figures/group6/render_g6_fig_02_phase_e.py
scientific_or_visual_risk = ambiguous visual association of the y-axis title and avoidable intrusion into the data field at publication size
required_correction = place the y-axis title clearly outside the plotting field, by rotation or equivalent external positioning, preserving font >=10 pt and all scientific geometry/data
whether_already_covered_by_Prompt105 = false
```

## 10. RECOMMENDED_SINGLE_CORRECTION_SCOPE

La próxima ejecución correctiva debe tratarse como una única corrección técnica del candidato existente, no como rediseño científico ni nueva ejecución de G6-F02. El alcance recomendado es:

1. aplicar las dos correcciones ya gobernadas por Prompt105: ledger sobre bytes canónicos Git/index y mínimo tipográfico efectivo de 8.5 pt en **todas** las etiquetas/ticks de G6-FIG-03;
2. en G6-FIG-03, reducir la oclusión de puntos mediante ajuste puramente geométrico de jitter horizontal y/o tamaño de marcador, sin alterar valores y, condiciones, inventario, orden de run/seed ni identidad de jitter entre paneles;
3. retirar de los tres títulos visibles los prefijos internos `G6-FIG-0X |`, conservando los IDs en filenames/registry;
4. en G6-FIG-01 Panel C, restituir la etiqueta explícita `Hierarchical (Attempt06)`;
5. en G6-FIG-02, recolocar el título del eje y fuera del campo de datos manteniendo tamaño >=10 pt;
6. regenerar únicamente los outputs afectados y repetir la validación completa de conteos, rangos, incertidumbre autorizada, escala de grises, no sobreclaim y equivalencia científica SVG/PNG;
7. mantener `NEW_SCIENTIFIC_METRIC_COUNT=0`, `NEW_INFERENCE_COUNT=0`, `NEW_CI_COUNT=0`, `NEW_P_VALUE_COUNT=0` y no modificar Plan Maestro, artículo, tesis ni EXP12.

## 11. Dictamen final

```text
FIG007_PREAUDIT_RESULT = ADDITIONAL_CORRECTIONS_REQUIRED
KNOWN_PROMPT105_FINDINGS_CONFIRMED = true
ADDITIONAL_FINDING_COUNT = 4
SCIENTIFIC_FIDELITY_AUDIT = PASS
ACCESSIBILITY_AUDIT = FAIL_PENDING_CORRECTION
CROSS_FIGURE_CONSISTENCY_AUDIT = PASS_WITH_EDITORIAL_CORRECTION
G6_F02_APPROVAL_AUTHORIZED = false
G6_F03_AUTHORIZED = false
```

El candidato no se rechaza científicamente: la información, los estimandos, los CI autorizados, los conteos y los guardrails son coherentes con el registry. Sin embargo, antes de una eventual integración de G6-F02 conviene incorporar en una sola ejecución correctiva los dos defectos ya conocidos de Prompt105 y los cuatro hallazgos adicionales anteriores.