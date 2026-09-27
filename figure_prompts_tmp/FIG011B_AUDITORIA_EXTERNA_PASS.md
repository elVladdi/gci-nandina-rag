# FIG011B — Auditoría externa IA Experimental — PASS

## Dictamen

```text
FIG011B_EXTERNAL_AUDIT = PASS
FIGURE_5_CANDIDATE = APPROVED_FOR_LATER_DOCX_INTEGRATION
SCIENTIFIC_DATA_CHANGE = false
NON_TEXT_SVG_GEOMETRY_MATCH = true
DETERMINISTIC_RERUN_MATCH = true
THESIS_VISIBLE_INTERNAL_IDS = NONE
G6_PROTECTED_ARTIFACTS_UNCHANGED = true
FIGURE_4_CANDIDATE_UNCHANGED = true
DOCX_MODIFIED = false
121F_AUTHORIZED = false
G7_F02 = ACTIVE / AUTHORIZED / REVISION_REQUIRED / NOT_APPROVED
G7_F03_AUTHORIZED = false
```

## Base auditada

Respuesta:

```text
figure_prompts_tmp/FIG011B_RESPUESTA_REGENERAR_FIGURA5_TESIS_G7_F02.md
```

Commit de generación auditado:

```text
0826792a01000105f3c4328784f08399ab2b1c02
```

Baseline científico congelado:

```text
main = db0d0ad0d8435921a7838db6720eaea86a263763
```

## Identidad del candidato aprobado

```text
src/figures/group7/render_g7_thesis_fig_05_coverage.py
GIT_BLOB = cd7bdc2c189635ecbe499a01e0e96c9a961fff9c
SHA256 = aa0ef8d3ecbc065bf06ba28cfc2518c4ab3fad682d31e45f25c6881bde1ead4e

figures/group7/g7_thesis_fig_05_coverage.svg
GIT_BLOB = 6cba4d776046e052ca4f76297ab627f2a3762046
SHA256_GIT_LF = f91302a0e1179fc52d1f647260b10bba7b1fbb75e302f241f6dbf158cba64051
SHA256_WINDOWS_CRLF = 78e95ab905f2e886e47156d28d741cf6366393fa627e010050ad9b93a9df42e7

figures/group7/g7_thesis_fig_05_coverage.png
GIT_BLOB = d63559e4da4b391d47968a60a41649c715d5408b
SHA256 = aecc77e8fd6272766eaf9f7a72d6bc531ef45d448264cac1b95a2ac30edd59c0
```

## Verificaciones independientes

1. El renderer candidato lee el renderer G6-FIG-02 y el CSV científico exclusivamente desde el commit congelado y verifica sus blobs antes de generar.
2. Las modificaciones del renderer candidato están confinadas a texto visible, saltos de línea y rutas de salida. No existe lógica de recálculo de los valores experimentales.
3. El SVG candidato conserva canvas `1200 x 675`, un panel, profundidades `50 / 100 / 200`, cinco variantes y quince marcas.
4. Las coordenadas visibles de las marcas corresponden a los quince valores congelados del CSV `g5_secondary_01_phase_e_descriptive.csv`.
5. Se conservan el eje Y `[0,00; 0,35]`, baseline cero, ausencia de líneas de conexión, ausencia de IC, ausencia de valores p y ausencia de tendencias ajustadas.
6. Los quince valores congelados permanecen:

```text
Solo jerárquico:                    0,0909 | 0,1013 | 0,3040
Solo dual:                          0,0919 | 0,1004 | 0,2661
Jerárquico prioridad primeros 100:  0,0909 | 0,1013 | 0,2652
Jerárquico 80 + backfill dual 20:   0,0909 | 0,1013 | 0,3040
Jerárquico 70 + backfill dual 30:   0,0909 | 0,1023 | 0,3040
```

7. El texto visible fue naturalizado conforme a FIG010/FIG011B. No aparecen `Phase E`, identificadores `hierarchical_*`, `A_historical_defined`, `G3C-005`, `diagnostic_union_hierarchical_dual` ni identificadores de gobernanza.
8. El encabezado visible aprobado es `Cobertura exacta NANDINA según profundidad y variante`.
9. La separación visual entre las cuatro variantes predefinidas y la quinta variante contextual se conserva sin alterar posiciones ni valores de las marcas.
10. El commit de generación contiene únicamente los cinco paths autorizados de FIG011B: respuesta, PNG, SVG, manifest y renderer.
11. La respuesta declara y documenta dos ejecuciones consecutivas deterministas y preservación byte-idéntica de G6 y del candidato aprobado de Figura 4.
12. No se modificó la tesis y no se ejecutó 121F.

## Consecuencia operativa

Con FIG011A y FIG011B aprobados, queda autorizado preparar una ejecución editorial mínima por la IA de Redacción Científica para incorporar las propuestas de reemplazo de Figuras 4 y 5 en la copia REVIEW V03, preservando físicamente las figuras legacy y la numeración 1–12 conforme a Prompt120/Prompt119.

La integración en DOCX no forma parte de FIG011B y debe ser auditada de manera independiente antes de autorizar el siguiente bloque de resultados.
