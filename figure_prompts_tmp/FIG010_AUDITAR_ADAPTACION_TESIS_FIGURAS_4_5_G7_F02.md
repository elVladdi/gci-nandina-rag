# FIG010 — Auditar adaptación para tesis de Figuras 4–5 en G7-F02

## Rol

Actúa como **IA Diseñadora y Auditora de Figuras Científicas**. No eres CODEX ni la IA de Redacción Científica.

El Bloque textual/tabular 121E fue auditado `PASS`. Antes de continuar con 121F deben reconciliarse las Figuras 4 y 5 con las Tablas 12 y 13.

```text
PROMPT121E_EXTERNAL_AUDIT = PASS
A039_A040_STATUS = PENDING_SCIENTIFIC_VISUAL_WORKFLOW
121F_AUTHORIZED = false
```

## Objetivo exclusivo

Audita y especifica la adaptación **para la tesis** de:

```text
G6-FIG-01 -> Figura 4 de la tesis
G6-FIG-02 -> Figura 5 de la tesis
```

No edites el DOCX. No generes todavía nuevas imágenes. No modifiques tablas ni prosa.

## Estado de tesis a reconciliar

Documento actual de revisión:

```text
Molleapasa_gv_G7F02_REVIEW_V03_E.docx
SHA256 = f6eb5a9f4db80faa36306df64ec51ddd865df2a081d69f65ca6a3e063ec2b7ba
```

La Figura 4 debe ser coherente con Tabla 12 y con el contraste primario de cobertura profunda de 4.1.3.
La Figura 5 debe ser coherente con Tabla 13.

No revises otras figuras.

## Fuentes visuales gobernantes

Lee íntegramente:

```text
outputs/figures/group6/g6_figure_spec_registry_v0.1.json
outputs/figures/group6/g6_figure_hash_ledger_v0.1.csv
docs/figures/group6/g6_caption_registry_v0.1.md
```

Artefactos aprobados:

```text
G6-FIG-01
figures/group6/g6_fig_01_he2.svg
figures/group6/g6_fig_01_he2.png
PNG SHA256 = 3136a814647384eaa1f85c2ce90033a78dde48b661d0b1c078e5b272c6e85d6f

G6-FIG-02
figures/group6/g6_fig_02_phase_e.svg
figures/group6/g6_fig_02_phase_e.png
PNG SHA256 = 867ca35d0c454a38bd122c6ecdf5bb693f98f86206828bd68c051aa263c7791f
```

No cambies datos, estimandos, CI, denominadores, orden no favorable ni rol científico.

## Regla especial para lenguaje de tesis

Los artefactos G6 fueron aprobados científicamente, pero la tesis no debe mostrar nombres de gobernanza o ejecución interna.

Audita específicamente si las figuras/captions aprobadas contienen cualquiera de estos términos visibles:

```text
Attempt06
D1a
Phase E
A_historical_defined
G3C-005
G5-MAIN
G5-SECONDARY
G6-FIG
```

Si aparecen, especifica una **adaptación editorial mínima** que preserve exactamente la semántica y los números. Usa lenguaje natural de tesis, por ejemplo:

```text
Historical -> Recuperación histórica
Flat -> BM25 normativo plano
Hierarchical -> BM25 normativo jerárquico
D1a -> Recuperador denso entrenado con MNRL
Phase E -> Análisis descriptivo de cobertura del conjunto candidato
```

No introduzcas nombres nuevos ni reinterpretaciones.

## Contenido científico que debe quedar visible

### Figura 4

Debe representar la evidencia primaria de HE2:

- valores observados de recuperación histórica y los tres comparadores en Top-1, Top-3, Top-5, Top-10 y MRR@100;
- 15 diferencias pareadas histórico − comparador con IC congelados de 99%;
- único contraste `Recall@200 − Recall@100` del recuperador jerárquico con IC congelado de 95%;
- benchmark interno: 1 056 series / 67 DAM / 42 NANDINA;
- sin CI por brazo y sin p-values;
- no causal y no equivalente a exactitud global del framework RAG.

### Figura 5

Debe representar descriptivamente cinco variantes a profundidades 50, 100 y 200:

- cuatro variantes predefinidas con igual estatus visual;
- variante 70/30 solo como contexto descriptivo adicional;
- unión diagnóstica excluida del rendimiento ordinario;
- eje desde cero;
- sin CI, p-values, tendencia ajustada, ranking de favorabilidad ni inferencia entre variantes.

## Caption de tesis

Propón para cada figura un caption final **íntegramente en español**, autosuficiente y compatible con el estilo actual de la tesis.

No uses identificadores internos. No agregues referencias bibliográficas nuevas.

## Salida

Publica exclusivamente:

```text
figure_prompts_tmp/FIG010_RESPUESTA_AUDITAR_ADAPTACION_TESIS_FIGURAS_4_5_G7_F02.md
```

Debe contener:

```text
FIG010_EXECUTION = COMPLETE
FIGURE_4_EXISTING_G6_BINARY_USABLE_AS_IS = true|false
FIGURE_5_EXISTING_G6_BINARY_USABLE_AS_IS = true|false
FIGURE_4_ADAPTATION_REQUIRED = true|false
FIGURE_5_ADAPTATION_REQUIRED = true|false
SCIENTIFIC_DATA_CHANGE_REQUIRED = false
THESIS_VISIBLE_INTERNAL_IDS_AFTER_ADAPTATION = NONE
NEXT_TECHNICAL_STEP = ...
EXTERNAL_AUDIT = PENDING_BY_IA_EXPERIMENTAL
```

Incluye para cada figura:

1. dictamen visual/científico;
2. términos visibles que deban naturalizarse;
3. especificación exacta de sustitución de etiquetas, si aplica;
4. caption final propuesto en español;
5. confirmación de coherencia con Tabla 12 o Tabla 13;
6. si el PNG aprobado puede usarse sin cambios o si requiere regeneración determinística exclusivamente editorial.

Detente ahí. No edites la tesis ni ejecutes regeneración técnica.