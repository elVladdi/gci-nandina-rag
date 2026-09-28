# FIG013 - Reporte de detención antes de regenerar Figura 6

## Alcance y fuentes

Se leyó íntegramente FIG013 en `2e7a55900b6db32ba6711880e17a3f17ab82dee6`, la respuesta FIG012 en `be0879c44b9d933bc0591bcf498b5e056cc31b20` y su auditoría externa PASS en `547e1dbfc34a03b9c569cf4d8c1792c88f94901b`.

Se trabajó en el checkout canónico `C:\Users\Vladimir\OneDrive\Documentos\Maestría UNMSM\LLM_RGA_NANDINA`, rama `codex/prompts-temporary`. Se preservaron todos los archivos no rastreados preexistentes, incluido `figures/group7.zip`.

Las identidades congeladas en `REF_G6=e93b44164a9619dad1f527a3b2d4479265858e39` coinciden con el prompt:

| Fuente | Git blob | SHA-256 del blob | Bytes |
| --- | --- | --- | ---: |
| `src/figures/group6/render_g6_fig_03_exp11a.py` | `1723f139afd308c4966846247ffe4d2f330a0d4e` | `bb73e2ce324500a36053afa52bc25a03af44def36ea2a7c2fd5c2c14a3cf844f` | 6523 |
| `figures/group6/g6_fig_03_exp11a.svg` | `1b2aca9aa9c2582cf0b7e16850cd5b22387cc771` | `a4a81b565ed2ceb22f23f9a52888e802b1e749186fb43d3bd71faf1b31d5f7c3` | 33417 |
| `figures/group6/g6_fig_03_exp11a.png` | `eaf59497ee49ab36d34d23e42cf002111bc9fe3e` | `3c4bcf736b56fbc9ffd054562db0eea31be195792f2bade611a9e5205dfa97de` | 108923 |
| `outputs/results/group5/tables/g5_appendix_02_exp11a_size_composition_sensitivity.csv` | `cf3aedab5935d6af9b3ac7be7b51b954fcb9c403` | `a88ec28a63143ac87a92b709997915857bb77e464ab8cbbb38576de650c27f7f` | 12782 |
| `outputs/experiments/exp11a_historical_size_sensitivity_v0.3/exp11_metrics_by_run.csv` | `9b434d7e09e6db7e9de061953b59c53aac2337ad` | `9e08376efb592221627c2c7227ef828c911d92b4ea5333718b76255dba78e0bd` | 16523 |
| `outputs/experiments/exp11a_historical_size_sensitivity_v0.3/exp11_metrics_by_condition.csv` | `535dd377d107ddcbf09ecaa13cd66ca723ee738d` | `25dca69c742746a6a1ab3b918a07d09c17a6522447b762ff4f8ad45d3233ad6b` | 4273 |

El inventario congelado contiene 31 corridas observadas: H25=10, H50-D1=5, H50-D2=5, H75=10 y H100=1. El SVG contiene 180 círculos abiertos y seis diamantes sólidos: las mismas 31 corridas representadas en cada uno de los seis paneles. No se recalcularon métricas ni summaries.

## Bloqueo contractual de legibilidad

La sustitución obligatoria `H100 ref.` por `H100 (referencia)`, manteniendo las posiciones, tamaños y anclajes originales, genera un solapamiento real con `H75` en los seis paneles.

El renderer congelado utiliza Arial, tamaño mínimo 14,5 unidades, escala raster 2,5 y anclaje centrado. Las posiciones de las etiquetas son:

| Panel | Y de ambas etiquetas | X de H75 | X de H100 | Intersección horizontal |
| --- | ---: | ---: | ---: | ---: |
| Top1 | 334 | 295 | 361 | 5,6 unidades |
| Top3 | 334 | 660 | 726 | 5,6 unidades |
| Top5 | 334 | 1025 | 1091 | 5,6 unidades |
| Top10 | 680 | 295 | 361 | 5,6 unidades |
| Top50 | 680 | 660 | 726 | 5,6 unidades |
| MRR | 680 | 1025 | 1091 | 5,6 unidades |

Medición con las fuentes del renderer, redondeadas a 36 px: `H75` ocupa 26,4 unidades y `H100 (referencia)` ocupa 116,8. Sus centros están separados por 66 unidades; la suma de semianchos es 71,6.

Una prueba aislada, exclusivamente tipográfica y en memoria, dibujó ambas cadenas en máscaras independientes con los parámetros originales. La intersección de tinta contiene 79 píxeles no nulos, con bounding box `(759, 27, 770, 53)` en el recorte de prueba. No es únicamente una intersección de cajas vacías.

FIG013 permite reducir, partir en líneas o reposicionar solo tres bloques: título, subtítulo y nota inferior. No permite ese ajuste local en las etiquetas de condición. La validación obligatoria exige ausencia de solapamiento material. Ambas condiciones no pueden satisfacerse simultáneamente con la sustitución indicada y la tipografía original.

Por ello se detuvo antes de crear renderer/SVG/PNG/manifest candidatos. No se desplazó H100, no se redujo su tamaño, no se cambió su anclaje ni se alteró la cadena aprobada. Se requiere resolver externamente el alcance de un eventual ajuste tipográfico de esa etiqueta antes de continuar; este bloque no lo autoriza.

## Preservación y verificaciones no ejecutadas

- Único path creado por esta ejecución: `figure_prompts_tmp/FIG013_RESPUESTA_REGENERAR_FIGURA6_TESIS_G7_F02.md`.
- Renderer, SVG, PNG G6 y fuentes científicas permanecen intactos; no se ejecutó el renderer G6 ni un renderer candidato.
- Figuras 4 y 5, incluidos sus scripts, SVG, PNG y manifests, permanecen sin cambios. Los PNG conservan respectivamente los SHA-256 `5cde004fc5b3b76578de02bd9d4751c52d26f921821c96a0bafc1cac65c1eb1e` y `aecc77e8fd6272766eaf9f7a72d6bc531ef45d448264cac1b95a2ac30edd59c0`.
- No se abrió el DOCX para edición, no se ejecutó A043 ni 121G y no se modificó `main`.
- No existe candidato Figura 6; comparación geométrica, doble render, hashes de salidas candidatas y examen de sus textos visibles no se ejecutaron. Los campos booleanos de validación del reporte terminal son `false` por ausencia de candidato, no por una diferencia geométrica o una falta de determinismo observada.

## Reporte terminal

```text
FIG013_EXECUTION = STOPPED_PRECONDITION
FIGURE_6_CANDIDATE_CREATED = false
SCIENTIFIC_DATA_CHANGE = false
SCIENTIFIC_GEOMETRY_CHANGE = false
NON_TEXT_SVG_GEOMETRY_MATCH = false
OBSERVED_RUN_COUNT = 31
DETERMINISTIC_RERUN_MATCH = false
THESIS_VISIBLE_INTERNAL_IDS = NOT_EVALUATED_NO_CANDIDATE
G6_PROTECTED_ARTIFACTS_UNCHANGED = true
FIGURE_4_CANDIDATE_UNCHANGED = true
FIGURE_5_CANDIDATE_UNCHANGED = true
DOCX_MODIFIED = false
A043_EXECUTED = false
121G_EXECUTED = false
EXTERNAL_AUDIT = PENDING_BY_IA_EXPERIMENTAL
```
