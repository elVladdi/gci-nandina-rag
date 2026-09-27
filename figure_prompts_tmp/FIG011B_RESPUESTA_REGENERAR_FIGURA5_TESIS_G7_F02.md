# FIG011B - Figura 5 de tesis (candidato)

## Procedencia y alcance

- Rama de publicación: `codex/prompts-temporary`; prompt: `b8d29b810a2f973dabf69f7c6bbaa06ddc737326`.
- Baseline científico congelado: `main=db0d0ad0d8435921a7838db6720eaea86a263763`.
- Se leyeron completos FIG010 (respuesta y auditoría PASS) y FIG011A (auditoría PASS). La Figura 4 aprobada no fue editada.
- La Figura 5 se generó desde el renderer G6-FIG-02 y el CSV G5 congelados, fijados por blob Git. El renderer candidato sustituye exclusivamente texto visible, ajuste de sus líneas y ruta de salida; conserva el dibujo original para todos los elementos geométricos.
- Se crearon únicamente los cinco paths previstos por FIG011B. No se editó el DOCX ni se ejecutó 121F.

## Fuentes congeladas

| Fuente | Git blob | SHA-256 | Bytes |
| --- | --- | --- | ---: |
| `src/figures/group6/render_g6_fig_02_phase_e.py` | `e9dafe41e3b22cb1c8d09da08a723925cd300b7d` | `a6951cbaace0852936a6e4d2a562d208b15a95983b32d1a98e5cdaaa1fb5c384` | 6676 |
| `figures/group6/g6_fig_02_phase_e.svg` | `ec164ea41ab8605edf198c03785db63c442c1b64` | `02de449d911dfbca9863997671751ac2480880646c45e31c8b7549584b0fabc6` | 8425 |
| `figures/group6/g6_fig_02_phase_e.png` | `7917314c8fc54dd96dd9ddfb28c9927c9a577c76` | `867ca35d0c454a38bd122c6ecdf5bb693f98f86206828bd68c051aa263c7791f` | 145570 |
| `outputs/results/group5/tables/g5_secondary_01_phase_e_descriptive.csv` | `fa961cf3d6198ddba6a6b5eeadcc9a23c8801f61` | `77a9b3cf27881396162fa25464d9fcaa1c8c557b6140e1e48bdbe93858aa523e` | 2620 |

## Candidato generado

| Path | Git blob | SHA-256 del blob | Bytes del blob |
| --- | --- | --- | ---: |
| `src/figures/group7/render_g7_thesis_fig_05_coverage.py` | `cd7bdc2c189635ecbe499a01e0e96c9a961fff9c` | `aa0ef8d3ecbc065bf06ba28cfc2518c4ab3fad682d31e45f25c6881bde1ead4e` | 5172 |
| `figures/group7/g7_thesis_fig_05_coverage.svg` | `6cba4d776046e052ca4f76297ab627f2a3762046` | `f91302a0e1179fc52d1f647260b10bba7b1fbb75e302f241f6dbf158cba64051` | 9070 |
| `figures/group7/g7_thesis_fig_05_coverage.png` | `d63559e4da4b391d47968a60a41649c715d5408b` | `aecc77e8fd6272766eaf9f7a72d6bc531ef45d448264cac1b95a2ac30edd59c0` | 164051 |

El SVG recién renderizado en Windows usa CRLF: SHA-256 `78e95ab905f2e886e47156d28d741cf6366393fa627e010050ad9b93a9df42e7`, 9133 bytes. Git almacena el mismo SVG con LF, con el blob y SHA de la tabla. El PNG es binario y conserva el mismo SHA en checkout y blob.

## Verificación

- Dos invocaciones consecutivas del renderer en el worktree limpio dieron los mismos SHA-256: SVG de checkout `78e95ab905f2e886e47156d28d741cf6366393fa627e010050ad9b93a9df42e7` y PNG `aecc77e8fd6272766eaf9f7a72d6bc531ef45d448264cac1b95a2ac30edd59c0`.
- Comparación XML con G6: al excluir solo nodos `text`/`tspan`, la secuencia completa de etiquetas y atributos no textuales es idéntica. Esto incluye ejes, ticks, gridlines y las quince coordenadas de datos. Hay 15 marcas de datos, cinco variantes, profundidades 50/100/200 y un panel.
- No aparecen rótulos prohibidos ni identificadores internos visibles. Los quince valores son los del CSV congelado; no se recalcularon. Rango vertical `[0, 0.35]`, baseline cero, sin líneas de unión, IC, valores p ni ajustes.
- Canvas SVG `1200 x 675`; PNG `3000 x 1688` con DPI nominal 300. Las cajas de texto permanecen dentro del canvas y sin solapamiento material; tamaño mínimo 13,5 unidades SVG, equivalente a 8,1 pt. Se inspeccionó visualmente el PNG final.
- Los tres artefactos G6 y el CSV mantienen sus blobs originales. Los cuatro blobs Figura 4 siguen siendo `b22d25d41fa9014180fd63a36715942414e779a0`, `e84fa3ee6aaedb2d3d24b59ce7255214621aae3f`, `eb77a4f2289a8701d22ba399d9432defd2092e2a` y `d6d69a65614348f2fbeab192faacc435b134c99f` (renderer, SVG, PNG y manifest, respectivamente).
- No hay edición de datos científicos, tesis, Figura 4, `main` ni 121F. La integración en DOCX queda pendiente de auditoría externa.

## Reporte terminal

```text
FIG011B_EXECUTION = COMPLETE
FIGURE_5_CANDIDATE_CREATED = true
SCIENTIFIC_DATA_CHANGE = false
NON_TEXT_SVG_GEOMETRY_MATCH = true
DETERMINISTIC_RERUN_MATCH = true
THESIS_VISIBLE_INTERNAL_IDS = NONE
G6_PROTECTED_ARTIFACTS_UNCHANGED = true
FIGURE_4_CANDIDATE_UNCHANGED = true
DOCX_MODIFIED = false
121F_EXECUTED = false
EXTERNAL_AUDIT = PENDING_BY_IA_EXPERIMENTAL
```
