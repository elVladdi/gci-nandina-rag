# Results B01 V01 — Section 5.1

```text
BLOCK = RESULTS_B01_SECTION_5_1
VERSION = V01
GOVERNING_PROMPT = article/prompts/6_RESULTS_B01_SECTION5_1.md@cc75fb9b732de6b9162cf90b8eacb8462372405e
GOVERNING_DECISION = D-088
GROUND_TRUTH_DECISION = D-087
BASELINE_MASTER = article/manuscript/ARTICLE_MASTER_V016.md
BASELINE_MASTER_SHA256 = 3c8b64104b11f2e07f85d0275e5ac6c4a96cb0c5cd5b183704949705c8e120a5
BASELINE_DOCX = ARTICLE_MASTER_CANDIDATE_EXPDES_B07_V02.docx
BASELINE_DOCX_SHA256 = c9c12609e7aefc5c2b260a967df88d87641252e2be28eab838f984952f48b4de
SOURCE_SNAPSHOT = db0d0ad0d8435921a7838db6720eaea86a263763
AUTHORIZED_SCOPE = SECTION_5_1_ONLY
RESULTS_B02_PLUS = NOT_AUTHORIZED
DISCUSSION = NOT_AUTHORIZED
CONCLUSION = NOT_AUTHORIZED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

## Part I — English manuscript text

## 5.1. Data and partition checks

The final v0.2 benchmark contained 4,106 curated SERIE records, all assigned to one of the three frozen partitions. H100 contained 2,950 series from 28 DAMs and 66 represented NANDINA codes; DEV contained 100 series from 6 DAMs and 9 codes; and EVAL contained 1,056 series from 67 DAMs and 42 represented reference codes. The source and output each contained 4,106 unique `id_unico` values, confirming complete assignment of the curated records.

No cross-partition DAM overlap or `id_unico` overlap was observed for H100–DEV, H100–EVAL, or DEV–EVAL. These checks establish separation of the frozen partitions by customs declaration and series identifier; they do not imply statistical independence among series belonging to the same DAM.

All 1,056 EVAL series had their reference eight-digit NANDINA code represented in H100, covering all 42 reference codes represented in EVAL. This was nominal historical class support only; it does not indicate whether historical retrieval placed the reference code within any Top-k position.

Residual textual similarity remained despite the group and identifier separation. Under `exact_normalized_description`, 35 of 1,056 EVAL rows (3.31%) matched a normalized description in H100; 34 shared the same NANDINA code and one had a different code, and all 35 matches came from different DAMs. No exact cross-partition description matches were observed for H100–DEV or DEV–EVAL. Under `token_jaccard_rare_block`, 55 EVAL rows (5.21%; 82 pairs), 44 (4.17%; 46 pairs), and 37 (3.50%; 38 pairs) had at least one H100 near-duplicate at Jaccard thresholds of 0.90, 0.95, and 0.98, respectively.

Thus, the frozen v0.2 benchmark satisfied the specified cross-partition DAM and identifier separation and complete nominal class support, while the exact- and near-duplicate diagnostics documented residual lexical similarity across distinct declarations. These diagnostics characterize the benchmark; they do not establish i.i.d. observations or quantify the effect of residual similarity on later performance measures.

## Part II — Spanish semantic-control mirror

## 5.1. Controles de datos y particiones

El benchmark final v0.2 contenía 4.106 registros de SERIE curados, todos asignados a una de las tres particiones congeladas. H100 contenía 2.950 series de 28 DAM y 66 códigos NANDINA representados; DEV contenía 100 series de 6 DAM y 9 códigos; y EVAL contenía 1.056 series de 67 DAM y 42 códigos de referencia representados. Tanto la fuente como la salida contenían 4.106 valores únicos de `id_unico`, lo que confirma la asignación completa de los registros curados.

No se observó solapamiento de DAM ni de `id_unico` entre H100–DEV, H100–EVAL o DEV–EVAL. Estos controles establecen la separación de las particiones congeladas por declaración aduanera e identificador de serie; no implican independencia estadística entre series pertenecientes a una misma DAM.

Las 1.056 series de EVAL tenían su código NANDINA de referencia de ocho dígitos representado en H100, con cobertura de los 42 códigos de referencia representados en EVAL. Este resultado corresponde únicamente a soporte histórico nominal de las clases; no indica si la recuperación histórica situó el código de referencia en alguna posición Top-k.

Persistió similitud textual residual a pesar de la separación por grupos e identificadores. Bajo `exact_normalized_description`, 35 de las 1.056 filas de EVAL (3,31%) coincidían con una descripción normalizada en H100; 34 compartían el mismo código NANDINA y una tenía un código diferente, y las 35 coincidencias correspondían a DAM distintas. No se observaron coincidencias exactas de descripción entre H100–DEV ni DEV–EVAL. Bajo `token_jaccard_rare_block`, 55 filas de EVAL (5,21%; 82 pares), 44 (4,17%; 46 pares) y 37 (3,50%; 38 pares) tenían al menos un near-duplicate en H100 con umbrales Jaccard de 0,90, 0,95 y 0,98, respectivamente.

Por tanto, el benchmark v0.2 congelado cumplió la separación especificada entre particiones por DAM e identificador y el soporte nominal completo de clases, mientras que los diagnósticos de duplicados exactos y near-duplicates documentaron similitud léxica residual entre declaraciones distintas. Estos diagnósticos caracterizan el benchmark; no establecen observaciones i.i.d. ni cuantifican el efecto de la similitud residual sobre medidas de desempeño posteriores.
