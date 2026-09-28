# FIG015 - Candidato Figura 6 de tesis

## Alcance y procedencia

Se ejecutó exclusivamente FIG015 en `c028b0a8ad1a7e7e3005ab635d60475d64a6a3a5`, tras lectura íntegra de las respuestas y auditorías FIG012, FIG013 y FIG014 exigidas por el prompt. La auditoría FIG014 PASS gobierna la etiqueta `H100 (ref.)`.

Checkout canónico: `C:\Users\Vladimir\OneDrive\Documentos\Maestría UNMSM\LLM_RGA_NANDINA`, rama `codex/prompts-temporary`. El estado rastreado estaba limpio antes de generar; se preservaron los untracked preexistentes (Referencias, XLSX y `figures/group7.zip`). No se reutilizaron salidas de FIG013: no existían.

El renderer candidato lee el código G6 y sus entradas directamente de blobs congelados, verifica sus identidades y cambia únicamente las cadenas visibles aprobadas y las rutas de salidas candidatas. No se materializan ni reescriben las fuentes científicas. Las instrucciones originales de agrupación, orden, jitter y dibujo permanecen intactas.

## Fuentes congeladas verificadas

`REF_G6=e93b44164a9619dad1f527a3b2d4479265858e39`.

| Path | Git blob | SHA-256 del blob | Bytes |
| --- | --- | --- | ---: |
| `src/figures/group6/render_g6_fig_03_exp11a.py` | `1723f139afd308c4966846247ffe4d2f330a0d4e` | `bb73e2ce324500a36053afa52bc25a03af44def36ea2a7c2fd5c2c14a3cf844f` | 6523 |
| `figures/group6/g6_fig_03_exp11a.svg` | `1b2aca9aa9c2582cf0b7e16850cd5b22387cc771` | `a4a81b565ed2ceb22f23f9a52888e802b1e749186fb43d3bd71faf1b31d5f7c3` | 33417 |
| `figures/group6/g6_fig_03_exp11a.png` | `eaf59497ee49ab36d34d23e42cf002111bc9fe3e` | `3c4bcf736b56fbc9ffd054562db0eea31be195792f2bade611a9e5205dfa97de` | 108923 |
| `outputs/results/group5/tables/g5_appendix_02_exp11a_size_composition_sensitivity.csv` | `cf3aedab5935d6af9b3ac7be7b51b954fcb9c403` | `a88ec28a63143ac87a92b709997915857bb77e464ab8cbbb38576de650c27f7f` | 12782 |
| `outputs/experiments/exp11a_historical_size_sensitivity_v0.3/exp11_metrics_by_run.csv` | `9b434d7e09e6db7e9de061953b59c53aac2337ad` | `9e08376efb592221627c2c7227ef828c911d92b4ea5333718b76255dba78e0bd` | 16523 |
| `outputs/experiments/exp11a_historical_size_sensitivity_v0.3/exp11_metrics_by_condition.csv` | `535dd377d107ddcbf09ecaa13cd66ca723ee738d` | `25dca69c742746a6a1ab3b918a07d09c17a6522447b762ff4f8ad45d3233ad6b` | 4273 |

## Cinco paths creados

```text
src/figures/group7/render_g7_thesis_fig_06_sensitivity.py
figures/group7/g7_thesis_fig_06_sensitivity.svg
figures/group7/g7_thesis_fig_06_sensitivity.png
outputs/figures/group7/g7_thesis_fig_06_sensitivity_manifest_v0.1.json
figure_prompts_tmp/FIG015_RESPUESTA_REGENERAR_FIGURA6_TESIS_TRAS_RESOLVER_H100_G7_F02.md
```

| Candidato | Git blob | SHA-256 del blob | Bytes |
| --- | --- | --- | ---: |
| `src/figures/group7/render_g7_thesis_fig_06_sensitivity.py` | `b433fa5d45246ee22bae324835cdc9ff15c744cf` | `76d93530e802629985a85619bac9932598b465674f66a8d1bd3ee37169142c0b` | 4615 |
| `figures/group7/g7_thesis_fig_06_sensitivity.svg` | `f6b4a1459b70daa5e2106dc6cd999a12668131a8` | `780cbf167cb597ebd7e644638a5a3b5c648b47299dfdf8b66b357014a4549584` | 33540 |
| `figures/group7/g7_thesis_fig_06_sensitivity.png` | `667765204adbdb7ab7567e9546f6ed8c71051d91` | `4eeb3a63d4bb8a22c5b00f6d3efe4d2733c2caeec52373fa7e1c05ac27a24ae3` | 112767 |

El SVG generado tiene CRLF en Windows: SHA-256 `6c0aa9502070b1fb9b04bfdf01e40df1e7a45d7d02db86f851cf7fd15e194c9b`, 33846 bytes. Git almacena el SVG con LF: SHA-256 `780cbf167cb597ebd7e644638a5a3b5c648b47299dfdf8b66b357014a4549584`, 33540 bytes. El PNG permanece binario, con el mismo SHA en checkout y blob. El manifest registra ambas representaciones.

## Validaciones ejecutadas

- Dos ejecuciones consecutivas del renderer produjeron hashes idénticos: SVG CRLF `6c0aa9502070b1fb9b04bfdf01e40df1e7a45d7d02db86f851cf7fd15e194c9b`; PNG `4eeb3a63d4bb8a22c5b00f6d3efe4d2733c2caeec52373fa7e1c05ac27a24ae3`.
- Comparación XML: excluidos únicamente los nodos de texto y whitespace asociado, todos los elementos no textuales coinciden en secuencia y atributos con G6. Las 186 marcas tienen coordenadas idénticas: 31 corridas en cada uno de seis paneles, con 30 círculos abiertos y un diamante sólido H100 por panel.
- Inventario observado preservado: H25=10, H50-D1=5, H50-D2=5, H75=10, H100=1. No se dibujaron filas summary; no se recalcularon métricas, agregados ni inferencia.
- Orden científico Top1/Top3/Top5/Top10/Top50/MRR, presentado como Top-1/Top-3/Top-5/Top-10/Top-50/MRR. Orden de condiciones, escala lineal [0,1], jitter, ejes, gridlines y seis separadores antes de H100 idénticos a G6.
- Cada etiqueta H100 es exactamente `H100 (ref.)`, tamaño 14.5 unidades SVG, anclaje middle, una sola línea y todos sus atributos posicionales idénticos al nodo original. La separación horizontal con H75 es 17.6 unidades en cada uno de los seis paneles, sin solapamiento.
- Todas las cajas tipográficas permanecen dentro del canvas y sin intersecciones materiales. Mínimo efectivo: 8.7 pt SVG y 8.64 pt raster. Se inspeccionó visualmente el PNG final. No hicieron falta ajustes locales en título, subtítulo ni nota inferior; se mantuvieron sus posiciones, tamaños y anclajes originales.
- Canvas SVG 1200 x 800; PNG 3000 x 2000, DPI nominal 300 (metadato raster 299.9994 por cuantización PNG).
- No quedan cadenas inglesas legacy ni identificadores de gobernanza visibles. Se mantienen los identificadores científicos de condición y MRR.
- G6 y las Figuras 4 y 5 permanecen byte-idénticos en sus representaciones registradas. El manifest incluye las ocho identidades Git y de checkout de Figuras 4/5 y las identidades congeladas G6. Sus PNG conservan `5cde004fc5b3b76578de02bd9d4751c52d26f921821c96a0bafc1cac65c1eb1e` y `aecc77e8fd6272766eaf9f7a72d6bc531ef45d448264cac1b95a2ac30edd59c0`, respectivamente.

La interpretación sigue siendo sensibilidad descriptiva y no causal; HE5 permanece INCONCLUSIVE. No se abrió el DOCX para edición ni se integró la figura. No se ejecutaron A043, 121G ni bloques posteriores. `main` no se modificó.

## Reporte terminal

```text
FIG015_EXECUTION = COMPLETE
FIGURE_6_CANDIDATE_CREATED = true
SCIENTIFIC_DATA_CHANGE = false
SCIENTIFIC_GEOMETRY_CHANGE = false
NON_TEXT_SVG_GEOMETRY_MATCH = true
OBSERVED_RUN_COUNT = 31
DETERMINISTIC_RERUN_MATCH = true
H100_VISIBLE_LABEL = H100 (ref.)
H100_OVERLAP_WITH_H75 = false
THESIS_VISIBLE_INTERNAL_IDS = NONE
G6_PROTECTED_ARTIFACTS_UNCHANGED = true
FIGURE_4_CANDIDATE_UNCHANGED = true
FIGURE_5_CANDIDATE_UNCHANGED = true
DOCX_MODIFIED = false
A043_EXECUTED = false
121G_EXECUTED = false
EXTERNAL_AUDIT = PENDING_BY_IA_EXPERIMENTAL
```
