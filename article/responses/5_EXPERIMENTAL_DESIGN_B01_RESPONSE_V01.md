# Experimental Design B01 — Execution response / Respuesta de ejecución

## English

```text
BLOCK = EXPERIMENTAL_DESIGN_B01
SOURCE_MASTER_V009_GIT_BLOB = 40f20437458715c615fc1762f025ebcdbb3b6fc2 / PASS
BASELINE_DOCX_SHA256 = 09a319b8e658d3888c75087d1f7db354ef686c449ad6ffd205ea86fbc9352657 / PASS
SRC03_HEAD_READ = b74b96d0163807007e4579d86450dd235125b30f
SRC03_BLOB_READ = 7b63fdb14b75eace173ac3c94775d39ed7ed7a57
SRC03_MATERIAL_CHANGE = NO
AUTHORIZED_SCOPE_ONLY = PASS
INTRODUCTION_MODIFIED = NO
RELATED_WORK_MODIFIED = NO
ARCHITECTURE_3_1_TO_3_7_MODIFIED = NO
SECTION_4_3_AND_LATER_MODIFIED = NO
RESULTS_LEAKAGE = NONE
NEW_LITERATURE = NONE
INHERITED_COMMENT_COUNT = 40
FINAL_COMMENT_COUNT = 40
TRACKED_CHANGES = 0
OOXML_QA = PASS
FULL_RENDER_QA = PASS
RENDERED_PAGE_COUNT = 41
SECTION_MD_PATH = article/sections/experimental_design/Experimental_Design_B01_V01.md
SECTION_MD_SHA256 = fe80017f26010c4125b3abaec41ce066d91b63e1ff5ca54fa98baea0bea90e78
SECTION_MD_GIT_BLOB = b876bef94d75c0c8c676f5a4fa3276cbb22fbd28
MASTER_CANDIDATE_MD_FILENAME = ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V01.md
MASTER_CANDIDATE_MD_SHA256 = 6e443353c362410ffe70c880b49647a12b1a88d3ec72a12675cce5e086435754
CANDIDATE_DOCX_FILENAME = ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V01.docx
CANDIDATE_DOCX_SHA256 = 4089ca75267ed05d1406b9bf2c1f895300f4da77ccb3e0559b2ef43ad49f3e5c
DIRECT_LARGE_MASTER_GITHUB_TRANSFER = NOT_ATTEMPTED / D035
MANUAL_BASE64 = NOT_USED
FRAGMENTATION_OR_CHUNKING = NOT_USED
ARTICLE_MASTER_V010 = NOT_PROMOTED
SECTION_4_3 = NOT_STARTED
RESULTS = NOT_STARTED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

| Claim/fact | Primary source | Scope |
|---|---|---|
| The empirical pilot is offline, non-binding, restricted to Chapter 87; SERIE is the analysis unit and DAM is the grouping unit when dependence is relevant. | Current SRC-03 (`docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md@7b63fdb14b75eace173ac3c94775d39ed7ed7a57`) and D-041 | Section 4.1 only; no legal-validity or external-generalization claim. |
| v0.2 uses explicit DAM assignments, contains 2,950/100/1,056 series in H100/DEV/EVAL, and has zero DAM and `id_unico` overlap across partitions. | `data_aduanas_splits_clase87_v0.2_metadata.json@bcb02c9c3493235a6f80991158c5b24fa7c04510`; `data_aduanas_split_clase87_v0.2.json@059eb81677dad92d6f9241f0b8cbbff9bba332cd` | Sections 4.1 and 4.2; no retrieval-performance interpretation. |
| The available source workbook was processed through the SUNAT series parser; historical processing used `Hoja2` as worksheet index 0 under the no-sheet default, and the reconstructed intermediate contains 107 DAM/11,320 series, 4,232 Chapter-87 rows pre-curation, and 4,106 curated records. | Current SRC-03 plus `sunat_series_parser.py@87dafb5f2b5f1febfc588b7b763adc9ab5523339` | Section 4.2.1; functional processed-content reproduction only, not binary identity of the complete historical workbook. |
| Chapter-87 curation applies required-field, 8-digit NANDINA, hierarchy-consistency, parser-warning, and duplicate/conflict rules. | `build_data_aduanas_splits.py@dfe80aa20a1ec3c791dff01c0080886613d7af93`; `sunat_series_parser.py@87dafb5f2b5f1febfc588b7b763adc9ab5523339` | Section 4.2.3 only. |
| The frozen H100/DEV/EVAL v0.2 files, counts, represented code counts, and SHA-256 identities are those reported in the manuscript block. | v0.2 metadata/configuration and `exp04_bm25_historico_v02_inventory.md@64e7049ae8fb056a5fcc2173b39bdcb244567a89` | Section 4.2.4; dataset identity and composition only, not BM25 results. |

Points omitted for insufficient evidence: none required by the authorized B01 scope. Documentary-corpus details, cross-partition duplicate/near-duplicate diagnostics, system/BM25/LLM configuration, and performance results were intentionally deferred because they belong to Section 4.3 or later authorized blocks, not because of an evidential substitution.

## Español

```text
BLOQUE = EXPERIMENTAL_DESIGN_B01
GIT_BLOB_MASTER_V009_FUENTE = 40f20437458715c615fc1762f025ebcdbb3b6fc2 / PASS
SHA256_DOCX_BASELINE = 09a319b8e658d3888c75087d1f7db354ef686c449ad6ffd205ea86fbc9352657 / PASS
HEAD_SRC03_LEIDO = b74b96d0163807007e4579d86450dd235125b30f
BLOB_SRC03_LEIDO = 7b63fdb14b75eace173ac3c94775d39ed7ed7a57
CAMBIO_MATERIAL_SRC03 = NO
SOLO_ALCANCE_AUTORIZADO = PASS
INTRODUCTION_MODIFICADA = NO
RELATED_WORK_MODIFICADO = NO
ARQUITECTURA_3_1_A_3_7_MODIFICADA = NO
SECCION_4_3_Y_POSTERIORES_MODIFICADAS = NO
FILTRACION_DE_RESULTADOS = NONE
LITERATURA_NUEVA = NONE
COMENTARIOS_HEREDADOS = 40
COMENTARIOS_FINALES = 40
CAMBIOS_CONTROLADOS = 0
QA_OOXML = PASS
QA_RENDER_COMPLETO = PASS
PAGINAS_RENDERIZADAS = 41
RUTA_MD_SECCION = article/sections/experimental_design/Experimental_Design_B01_V01.md
SHA256_MD_SECCION = fe80017f26010c4125b3abaec41ce066d91b63e1ff5ca54fa98baea0bea90e78
GIT_BLOB_MD_SECCION = b876bef94d75c0c8c676f5a4fa3276cbb22fbd28
ARCHIVO_MD_MASTER_CANDIDATO = ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V01.md
SHA256_MD_MASTER_CANDIDATO = 6e443353c362410ffe70c880b49647a12b1a88d3ec72a12675cce5e086435754
ARCHIVO_DOCX_CANDIDATO = ARTICLE_MASTER_CANDIDATE_EXPDES_B01_V01.docx
SHA256_DOCX_CANDIDATO = 4089ca75267ed05d1406b9bf2c1f895300f4da77ccb3e0559b2ef43ad49f3e5c
TRANSFERENCIA_DIRECTA_MASTER_GRANDE_GITHUB = NOT_ATTEMPTED / D035
BASE64_MANUAL = NOT_USED
FRAGMENTACION_O_CHUNKING = NOT_USED
ARTICLE_MASTER_V010 = NOT_PROMOTED
SECCION_4_3 = NOT_STARTED
RESULTS = NOT_STARTED
FINAL_GAP = NOT_DEFINED
NOVELTY = NOT_DECLARED
```

| Claim/hecho | Fuente primaria | Alcance |
|---|---|---|
| El piloto empírico es offline, no vinculante y restringido al Capítulo 87; SERIE es la unidad de análisis y DAM la unidad de agrupamiento cuando la dependencia es relevante. | SRC-03 vigente (`docs/PLAN_MAESTRO_TESIS_SAN_MARCOS_2026-08-31.md@7b63fdb14b75eace173ac3c94775d39ed7ed7a57`) y D-041 | Solo Sección 4.1; sin claim de validez jurídica ni generalización externa. |
| v0.2 usa asignaciones explícitas de DAM, contiene 2,950/100/1,056 series en H100/DEV/EVAL y presenta cero solapamiento de DAM y de `id_unico` entre particiones. | `data_aduanas_splits_clase87_v0.2_metadata.json@bcb02c9c3493235a6f80991158c5b24fa7c04510`; `data_aduanas_split_clase87_v0.2.json@059eb81677dad92d6f9241f0b8cbbff9bba332cd` | Secciones 4.1 y 4.2; sin interpretación de desempeño de recuperación. |
| El workbook fuente disponible fue procesado mediante el parser de series SUNAT; el procesamiento histórico utilizó `Hoja2` como worksheet de índice 0 bajo el comportamiento por defecto sin hoja especificada, y el intermedio reconstruido contiene 107 DAM/11,320 series, 4,232 filas del Capítulo 87 antes de curación y 4,106 registros curados. | SRC-03 vigente más `sunat_series_parser.py@87dafb5f2b5f1febfc588b7b763adc9ab5523339` | Sección 4.2.1; solo reproducción funcional del contenido procesado, no identidad binaria del workbook histórico completo. |
| La curación del Capítulo 87 aplica reglas de campos obligatorios, NANDINA de 8 dígitos, consistencia jerárquica, advertencias del parser y duplicados/conflictos. | `build_data_aduanas_splits.py@dfe80aa20a1ec3c791dff01c0080886613d7af93`; `sunat_series_parser.py@87dafb5f2b5f1febfc588b7b763adc9ab5523339` | Solo Sección 4.2.3. |
| Los archivos congelados H100/DEV/EVAL v0.2, sus conteos, códigos representados y SHA-256 son los reportados en el bloque del manuscrito. | Metadata/configuración v0.2 y `exp04_bm25_historico_v02_inventory.md@64e7049ae8fb056a5fcc2173b39bdcb244567a89` | Sección 4.2.4; identidad y composición de datasets, no resultados BM25. |

Puntos omitidos por evidencia insuficiente: ninguno requerido por el alcance autorizado de B01. Los detalles del corpus documental, los diagnósticos de duplicados/near-duplicates entre particiones, la configuración del sistema/BM25/LLM y los resultados de desempeño se difirieron deliberadamente porque corresponden a la Sección 4.3 o a bloques posteriores, no por sustitución de evidencia.
