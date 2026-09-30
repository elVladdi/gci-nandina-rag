# FAST-F02 V03 Presentation-Consistency Correction V01

## Español

Corrección estrecha ejecutada bajo D-214 sobre los cuatro baselines FAST-F02 V02 exactos. No se modifica contenido científico, valores, inferencias, referencias ni End Matter científico.

### R01 — espejo completo de figuras en español

Se añadieron las instancias de imagen ausentes de Figura 2 y Figura 3 inmediatamente antes de sus captions ya existentes en la Parte II. Las instancias EN/ES reutilizan los mismos media assets:

- Figura/Figure 2 → PNG canónico FAST-F02 Figure 2 V02;
- Figura/Figure 3 → el mismo asset científico EXP11A ya aprobado.

Inventario final del master Markdown:

```text
EN Figure 1 = PRESENT
EN Figure 2 = PRESENT
EN Figure 3 = PRESENT
EN Figure 4 = PRESENT
ES Figura 1 = PRESENT
ES Figura 2 = PRESENT
ES Figura 3 = PRESENT
ES Figura 4 = PRESENT
TOTAL_MAIN_MD_IMAGE_REFERENCES = 8
```

Inventario final del Word:

```text
SCIENTIFIC_FIGURE_IDENTITIES = 4
EN_DRAWING_INSTANCES = 4
ES_DRAWING_INSTANCES = 4
TOTAL_SCIENTIFIC_DRAWING_INSTANCES = 8
UNIQUE_SCIENTIFIC_MEDIA_ASSETS = 4
```

### R02 — Supplementary visible-text consistency

El Supplementary V03 mantiene Tables S1–S7 y Figure S1 sin cambios científicos. La nota visible ahora indica correctamente que former Figure S2 / G6-FIG-03 fue retirada del Supplementary porque el mismo objeto científico fue promovido a main Figure 3.

### R03/R04 — Figure 2 canonicalization

Figure 2 se canonicalizó como una sola variante visual V02. SVG y PNG proceden del mismo SVG canónico, con:

- ocho medias congeladas sin cambios;
- eje x fijo 0–2;
- mismo título, etiquetas, orden de barras y value labels;
- diseño en escala de grises;
- sin subtitle divergente;
- sin CI, p-values, marcas de significancia o threshold inventado.

El mismo PNG canónico se embebe en las instancias inglesa y española.

### QA de layout

- Figure 2 + caption: misma página en inglés y español.
- Figure 3 + caption: misma página en inglés y español.
- Tables 2–7 EN/ES: filas con `cantSplit`.
- Tables 2–7 EN/ES: header row repetible.
- Table 7 EN/ES: columna Design note / Nota de diseño ensanchada y tipografía conservadora para evitar cortes de palabra impropios.

## English

This is the narrow D-214 FAST-F02 V03 presentation-consistency correction. Scientific content, table values, inferential interpretation, references, End Matter science, and the approved Figure 1/3/4 scientific content remain frozen.

The final bilingual master contains four scientific figure identities with four English and four Spanish drawing instances, reusing four unique scientific media assets. The Supplementary contains seven tables and one scientific figure. Figure 2 SVG/PNG were canonicalized from one visual source, and the exact same PNG bytes are used in both language instances.

No new experiment, metric, CI, p-value, inferential test, hypothesis disposition, literature, reference, or scientific claim was introduced.
